"""
Knowledge Base Ingestion — Karpathy-style LLM wiki builder
===========================================================
Step 1: Ingest raw PDFs → structured markdown summaries in wiki/

For each PDF in <topic>/raw/:
  - Extract full text (chunked so large books fit)
    - Ask gpt-4o for a structured summary: overview, key concepts,
    important theorems/results, open questions, suggested links
  - Write <topic>/wiki/<paper>.md with Obsidian-compatible frontmatter
  - Skip files already summarised (incremental, safe to re-run)

Usage (run from this directory or project root):
    cd functional_analysis
    source ../.venv/bin/activate
    python ingest_knowledge_base.py              # process this directory
    python ingest_knowledge_base.py --force      # re-process all PDFs
"""

import os
import sys
import argparse
import textwrap
from datetime import date
from pathlib import Path

from pypdf import PdfReader
from openai import OpenAI

# ── Auth ──────────────────────────────────────────────────────────────────────
TOKEN = os.environ["GITHUB_MODELS_TOKEN"]

MODEL   = "gpt-4o"
BASE_URL = "https://models.inference.ai.azure.com"

# ── Chunking ──────────────────────────────────────────────────────────────────
# This endpoint reports 16,000-token max request body for gpt-4o.
# Keep chunk input conservative so prompt + text + response fit comfortably.
# 1 token ≈ 4 chars (rough; content-dependent), so 12k chars ≈ ~3k tokens.
CHUNK_CHARS     = 12_000
MAX_CHUNKS      = 120
MERGE_BATCH_SIZE = 6

SUMMARY_PROMPT = """\
You are building a personal knowledge-base wiki in the style described by Andrej Karpathy.
Given the following text extracted from a PDF document, produce a structured Markdown article.

The article MUST include these sections (use ## headings):
## Overview
A 2-4 paragraph summary of what this document is about, its scope, and its significance.

## Key Concepts
Bullet list of the most important concepts, definitions, theorems or results introduced.
For each, give a one-sentence explanation.

## Chapter / Section Map
A brief outline of the document's structure (what each major part covers).

## Connections & Backlinks
List related topics, fields, or concepts this document connects to.
Format as: `[[Concept Name]]` (Obsidian wikilink style).

## Open Questions & Further Reading
Questions this document raises or leaves open. Related papers or books worth exploring.

---
TEXT:
{text}
"""


def extract_text(pdf_path: Path) -> str:
    """Extract all text from a PDF, page by page."""
    reader = PdfReader(str(pdf_path))
    pages = []
    for i, page in enumerate(reader.pages):
        try:
            t = page.extract_text() or ""
            if t.strip():
                pages.append(f"[Page {i+1}]\n{t}")
        except Exception:
            pass
    return "\n\n".join(pages)


def chunk_text(text: str, chunk_size: int = CHUNK_CHARS) -> list[str]:
    """Split text into overlapping chunks that fit within the model context."""
    chunks = []
    start = 0
    overlap = chunk_size // 10  # 10% overlap so context carries over
    while start < len(text) and len(chunks) < MAX_CHUNKS:
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks


def summarise_chunk(client: OpenAI, chunk: str, chunk_index: int, total: int) -> str:
    """Ask the model to summarise one chunk of text."""
    print(f"    Summarising chunk {chunk_index+1}/{total} ({len(chunk):,} chars)...")
    prompt = SUMMARY_PROMPT.format(text=chunk)
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    return response.choices[0].message.content or ""


def merge_summaries(client: OpenAI, summaries: list[str], title: str) -> str:
    """Merge chunk summaries into one coherent article, batching to stay under token limits."""
    if len(summaries) == 1:
        return summaries[0]

    round_num = 1
    current = summaries

    while len(current) > 1:
        next_round = []
        print(f"    Merge round {round_num}: {len(current)} summaries")
        for start in range(0, len(current), MERGE_BATCH_SIZE):
            batch = current[start:start + MERGE_BATCH_SIZE]
            if len(batch) == 1:
                next_round.append(batch[0])
                continue

            combined = "\n\n---CHUNK BOUNDARY---\n\n".join(batch)
            merge_prompt = f"""\
The following are partial summaries of different sections of a document titled "{title}".
Merge them into a single cohesive wiki article.

Keep the same section structure:
## Overview
## Key Concepts
## Chapter / Section Map
## Connections & Backlinks
## Open Questions & Further Reading

Deduplicate, synthesise, and make the article coherent. Do not simply concatenate.

PARTIAL SUMMARIES:
{combined}
"""
            response = client.chat.completions.create(
                model=MODEL,
                messages=[{"role": "user", "content": merge_prompt}],
                temperature=0.3,
            )
            next_round.append(response.choices[0].message.content or "")

        current = next_round
        round_num += 1

    return current[0]


def build_note(title: str, source_path: Path, wiki_dir: Path, body: str) -> str:
    """Wrap the LLM body in Obsidian-compatible frontmatter."""
    rel_source = str(source_path).replace(str(wiki_dir.parent.parent), "")
    return textwrap.dedent(f"""\
        ---
        title: "{title}"
        type: source-summary
        status: auto-generated
        source: "{rel_source}"
        model: {MODEL}
        date: {date.today().isoformat()}
        tags: [knowledge-base, auto-ingested]
        ---

        # {title}

        > *Auto-generated summary. Source: `{source_path.name}`*

        {body}

        ---
        *Ingested by `ingest_knowledge_base.py` on {date.today().isoformat()}*
    """)


def process_topic(topic_dir: Path, force: bool, client: OpenAI) -> None:
    raw_dir  = topic_dir / "raw"
    wiki_dir = topic_dir / "wiki"

    if not raw_dir.exists():
        print(f"[SKIP] No raw/ directory found at {raw_dir}")
        return

    wiki_dir.mkdir(exist_ok=True)
    print(f"\nWiki output: {wiki_dir}\n")

    pdfs = sorted(raw_dir.rglob("*.pdf"))
    if not pdfs:
        print(f"[SKIP] No PDFs found in {raw_dir}")
        return

    print(f"Found {len(pdfs)} PDF(s) in {raw_dir}\n")

    for pdf_path in pdfs:
        title = pdf_path.stem.replace("_", " ").replace(".", " ").strip()
        out_path = wiki_dir / (pdf_path.stem + ".md")

        if out_path.exists() and not force:
            print(f"[SKIP] Already processed: {pdf_path.name}")
            continue

        print(f"[PROC] {pdf_path.name}")
        print(f"  Extracting text...")

        try:
            full_text = extract_text(pdf_path)
        except Exception as e:
            print(f"  [ERR] Text extraction failed: {e}")
            continue

        if not full_text.strip():
            print(f"  [ERR] No text extracted (scanned PDF?). Skipping.")
            continue

        print(f"  Extracted {len(full_text):,} chars from {pdf_path.name}")

        chunks = chunk_text(full_text)
        print(f"  Split into {len(chunks)} chunk(s) ({CHUNK_CHARS:,} chars/chunk)")
        if len(chunks) >= MAX_CHUNKS:
            print(f"  [WARN] Reached MAX_CHUNKS={MAX_CHUNKS}; trailing content may be truncated")

        try:
            summaries = [
                summarise_chunk(client, chunk, i, len(chunks))
                for i, chunk in enumerate(chunks)
            ]
            body = merge_summaries(client, summaries, title)
        except Exception as e:
            print(f"  [ERR] LLM call failed: {e}")
            continue

        note = build_note(title, pdf_path, wiki_dir, body)

        out_path.write_text(note, encoding="utf-8")
        print(f"  [OK ] Written: {out_path.relative_to(topic_dir.parent)}\n")


def main():
    parser = argparse.ArgumentParser(description="Ingest PDFs into LLM knowledge base wiki")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-process PDFs that already have a wiki entry",
    )
    args = parser.parse_args()

    token = TOKEN.strip().strip('"').strip("'")
    if not token or token == "PASTE_YOUR_GITHUB_PAT_HERE":
        print("ERROR: TOKEN not set in this file.")
        sys.exit(1)

    client = OpenAI(base_url=BASE_URL, api_key=token)

    # The script lives inside the topic directory it processes
    topic_dir = Path(__file__).parent

    print(f"=== Knowledge Base Ingestion ===")
    print(f"Topic:    {topic_dir.name}")
    print(f"Model:    {MODEL}")
    print(f"Force:    {args.force}")

    process_topic(topic_dir, args.force, client)

    print("\nDone. Open the wiki/ folder in Obsidian to view results.")


if __name__ == "__main__":
    main()
