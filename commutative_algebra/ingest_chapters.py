"""
Chapter-level Knowledge Base Ingestion
=======================================
Produces one rich wiki article per chapter of each PDF book.

Pipeline per PDF:
  1. Detect chapter boundaries from page text (no bookmarks required)
  2. For each chapter, chunk text to fit the 16k-token request limit
  3. Summarise each chunk with a rich prompt (theorems, proofs, examples, exercises)
  4. Hierarchically merge chunk summaries into one final article
  5. Write wiki/chapters/<pdf_stem>/chapter_NN_<slug>.md

Usage:
    cd functional_analysis
    source ../.venv/bin/activate
    python ingest_chapters.py              # skip chapters already done
    python ingest_chapters.py --force      # redo all chapters
    python ingest_chapters.py --dry-run    # just print detected chapters, no API calls
"""

import os
import re
import sys
import argparse
import textwrap
from datetime import date
from pathlib import Path

from pypdf import PdfReader
from openai import OpenAI

# ── Config ────────────────────────────────────────────────────────────────────
TOKEN    = os.environ["GITHUB_MODELS_TOKEN"]
DEFAULT_MODEL = "gpt-4o"
FALLBACK_MODEL = "gpt-4o-mini"
BASE_URL = "https://models.inference.ai.azure.com"

# Endpoint limits vary by model on this API.
# Conservative defaults so prompt + text + response stay under body limits.
MODEL_CHUNK_DEFAULTS = {
    "gpt-4o": 12_000,
    "gpt-4o-mini": 5_000,
}

MODEL_MERGE_BATCH_DEFAULTS = {
    "gpt-4o": 5,
    "gpt-4o-mini": 2,
}


def is_rate_limit_error(exc: Exception) -> bool:
    msg = str(exc)
    return (
        "RateLimitReached" in msg
        or "429" in msg
        or "UserByModelByDay" in msg
        or "Please wait" in msg
    )


def is_model_unavailable_error(exc: Exception) -> bool:
    msg = str(exc)
    return "unknown_model" in msg or "not found" in msg.lower()


def probe_model(client: OpenAI, model: str) -> tuple[bool, str]:
    """Lightweight availability check for a model on this endpoint."""
    try:
        client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": "ping"}],
            max_tokens=16,
            temperature=0,
        )
        return True, "ok"
    except Exception as exc:
        return False, str(exc)


def resolve_model(client: OpenAI, requested_model: str) -> str:
    """
    Resolve model with automatic fallback behavior:
    - auto: try gpt-4o, fallback to gpt-4o-mini
    - gpt-4o: try gpt-4o, fallback to gpt-4o-mini if unavailable/rate-limited
    - anything else: use as-is
    """
    req = requested_model.strip()
    if req not in {"auto", "gpt-4o"}:
        return req

    ok, reason = probe_model(client, "gpt-4o")
    if ok:
        print("[MODEL] gpt-4o is available.")
        return "gpt-4o"

    if is_rate_limit_error(Exception(reason)) or is_model_unavailable_error(Exception(reason)):
        print("[MODEL] gpt-4o unavailable/rate-limited; falling back to gpt-4o-mini.")
        return FALLBACK_MODEL

    print("[MODEL] gpt-4o probe failed; falling back to gpt-4o-mini.")
    return FALLBACK_MODEL

# ── Chapter detection regex ───────────────────────────────────────────────────
# Matches pages starting with: "Chapter N" or just a bare number on its own line
# followed by a title on the next line (Atiyah-Macdonald style).
CHAP_START_RE = re.compile(
    r'^(?:Chapter\s+)?(\d{1,2})\s*\n\s*(.+?)(?:\n|$)',
    re.MULTILINE,
)

# ── Prompts ───────────────────────────────────────────────────────────────────
CHUNK_PROMPT = """\
You are building a dense personal knowledge-base wiki.

The text below is an excerpt (~3 pages) from Chapter {chap_num} ("{chap_title}") \
of the graduate textbook "{book_title}".

Write a rich Markdown article covering ONLY what is in this excerpt.

STRICT REQUIREMENTS:
1) Use ONLY evidence from the excerpt text.
2) Do not invent theorem names, assumptions, proofs, or examples.
3) If a section has no material in this excerpt, write: "Not present in this excerpt."
4) Keep notation exact whenever possible.
5) For math rendering, use `$...$` for inline math and `$$...$$` for display math.
    Do NOT use `\\(...\\)` or `\\[...\\]` delimiters.

Use this exact structure:

## Definitions & Notation
- List each definition explicitly.
- Include symbols and precise meaning.

## Theorems, Lemmas & Corollaries
- For each result, provide:
    - Label/name (if present)
    - Full statement (hypotheses + conclusion)
    - Where it appears (section/page label if visible)

## Proof Ideas
- For each theorem/lemma/corollary above, give the proof idea or proof sketch
    only if present/implied by the excerpt.

## Worked Examples & Constructions
- Describe each example/construction and why it is introduced.

## Exercises (notable)
- List notable exercises and what concept they reinforce.

## Key Insights
- 3–8 concise bullets about what matters most from this excerpt.

---
EXCERPT:
{text}
"""

MERGE_PROMPT = """\
The following are partial wiki notes for Chapter {chap_num} ("{chap_title}") \
of "{book_title}". Each partial note covers a different passage in the chapter.

Produce a single, cohesive richly-detailed wiki article for the whole chapter.
Do NOT simply concatenate — deduplicate, synthesise, and write flowing prose \
where appropriate.

STRICT REQUIREMENTS:
1) Preserve mathematical correctness and notation consistency.
2) Include explicit theorem/lemma/corollary statements with hypotheses and conclusions.
3) Include proof ideas for each major result when available in the partial notes.
4) Do not add external facts not present in the partial notes.
5) If a requested section has no evidence in notes, write "Not present in chapter notes."
6) For math rendering, use `$...$` (inline) and `$$...$$` (display), never `\\(...\\)` / `\\[...\\]`.

Final article structure:
## Overview
2–3 paragraph narrative: what this chapter covers, its role in the book, \
why the material matters.

## Definitions & Notation
All key terms, symbols, and definitions introduced in this chapter.

## Theorems, Lemmas & Corollaries
All named results, each with:
- Formal statement (hypotheses + conclusion)
- Minimal notation definitions needed to parse statement

## Proof Ideas
Proof strategy/intuitions for each major result (only from notes).

## Worked Examples & Constructions
All significant examples shown in the chapter.

## Exercises (selected)
Most instructive exercises, with brief discussion.

## Key Insights
5–10 distilled bullet points a student should remember from this chapter.

## Connections & Backlinks
`[[Wikilinks]]` to related chapters, topics, or standard results \
(use Obsidian wikilink format).

## Further Reading
Papers, books, or online resources that go deeper on this chapter's themes.

---
PARTIAL NOTES:
{combined}
"""


# ── PDF helpers ───────────────────────────────────────────────────────────────

def extract_pages(pdf_path: Path) -> list[str]:
    """Return list of per-page text strings."""
    reader = PdfReader(str(pdf_path))
    pages = []
    for i, page in enumerate(reader.pages):
        try:
            t = page.extract_text() or ""
        except Exception:
            t = ""
        pages.append(t)
    return pages


def detect_chapters(pages: list[str]) -> list[tuple[int, int, str]]:
    """
    Return list of (chapter_number, start_page_index, chapter_title).
    chapter_title is the cleaned title line from the chapter-start page.
    """
    chapters = []
    for i, text in enumerate(pages):
        stripped = text.strip()
        m = CHAP_START_RE.match(stripped)
        if m:
            chapter_num = int(m.group(1))
            # Title may have OCR artefacts (extra spaces); normalise
            title = re.sub(r'\s+', ' ', m.group(2)).strip()
            chapters.append((chapter_num, i, title))

    # Detect unnumbered chapter starts (e.g. "Modules\n..." for Ch 2)
    # by looking for gaps in the chapter numbering and pages whose first
    # line is a single capitalized word/phrase that looks like a title.
    NON_TITLE_STARTS = re.compile(
        r'^(Exercise|Proposition|Theorem|Lemma|Corollary|Proof|Example|Remark|\d)',
        re.IGNORECASE,
    )
    if chapters:
        nums = {c[0] for c in chapters}
        for gap_num in range(1, max(nums) + 1):
            if gap_num not in nums:
                # Search between start of book and next chapter
                next_chaps = [c for c in chapters if c[0] > gap_num]
                end_page = next_chaps[0][1] if next_chaps else len(pages)
                prev_chaps = [c for c in chapters if c[0] < gap_num]
                start_page = prev_chaps[-1][1] + 1 if prev_chaps else 0
                for j in range(start_page, end_page):
                    first_line = pages[j].strip().split('\n')[0].strip()
                    # A title-like line: starts with uppercase, short, no numbers at end
                    if (first_line and first_line[0].isupper()
                            and not NON_TITLE_STARTS.match(first_line)
                            and len(first_line) < 60
                            and not re.search(r'\d+\s*$', first_line)):
                        title = re.sub(r'\s+', ' ', first_line).strip()
                        chapters.append((gap_num, j, title))
                        break
        chapters.sort(key=lambda c: c[1])

    return chapters


def chapter_page_ranges(
    chapters: list[tuple[int, int, str]],
    total_pages: int,
) -> list[tuple[int, int, str, int]]:
    """
    Return (chap_num, start_page, title, end_page_exclusive) for each chapter.
    """
    result = []
    for idx, (num, start, title) in enumerate(chapters):
        end = chapters[idx + 1][1] if idx + 1 < len(chapters) else total_pages
        result.append((num, start, title, end))
    return result


def chapter_text(pages: list[str], start: int, end: int) -> str:
    """Concatenate pages for one chapter, attaching page labels."""
    parts = []
    for i in range(start, end):
        t = pages[i].strip()
        if t:
            parts.append(f"[p.{i+1}]\n{t}")
    return "\n\n".join(parts)


def chunk_text(text: str, chunk_size: int) -> list[str]:
    """Split text into chunk_size-sized pieces with 10% overlap."""
    chunks = []
    overlap = chunk_size // 10
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks


# ── LLM calls ────────────────────────────────────────────────────────────────

def summarise_chunk(
    client: OpenAI,
    model: str,
    chunk: str,
    idx: int,
    total: int,
    chap_num: int,
    chap_title: str,
    book_title: str,
) -> str:
    print(f"      chunk {idx+1}/{total} ({len(chunk):,} chars)...", end=" ", flush=True)
    prompt = CHUNK_PROMPT.format(
        chap_num=chap_num,
        chap_title=chap_title,
        book_title=book_title,
        text=chunk,
    )
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    result = resp.choices[0].message.content or ""
    print("ok")
    return result


def merge_batch(
    client: OpenAI,
    model: str,
    summaries: list[str],
    chap_num: int,
    chap_title: str,
    book_title: str,
    round_num: int,
    batch_idx: int,
) -> str:
    combined = "\n\n---CHUNK BOUNDARY---\n\n".join(summaries)
    prompt = MERGE_PROMPT.format(
        chap_num=chap_num,
        chap_title=chap_title,
        book_title=book_title,
        combined=combined,
    )
    print(
        f"      merge r{round_num} batch {batch_idx+1} "
        f"({len(summaries)} summaries)...",
        end=" ",
        flush=True,
    )
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    result = resp.choices[0].message.content or ""
    print("ok")
    return result


def hierarchical_merge(
    client: OpenAI,
    model: str,
    summaries: list[str],
    chap_num: int,
    chap_title: str,
    book_title: str,
    merge_batch_size: int,
) -> str:
    if len(summaries) == 1:
        return summaries[0]

    current = summaries
    rnd = 1
    while len(current) > 1:
        next_round = []
        for i in range(0, len(current), merge_batch_size):
            batch = current[i : i + merge_batch_size]
            if len(batch) == 1:
                next_round.append(batch[0])
            else:
                merged = merge_batch(
                    client,
                    model,
                    batch,
                    chap_num,
                    chap_title,
                    book_title,
                    rnd,
                    i // merge_batch_size,
                )
                next_round.append(merged)
        current = next_round
        rnd += 1

    return current[0]


# ── Output ────────────────────────────────────────────────────────────────────

def slug(title: str) -> str:
    """Turn a chapter title into a filesystem-safe slug."""
    s = title.lower()
    s = re.sub(r'[^a-z0-9\s]', '', s)
    s = re.sub(r'\s+', '_', s.strip())
    return s[:60]


def normalize_math_delimiters(text: str) -> str:
    """
    Normalize LaTeX math delimiters for Markdown renderers (VS Code + Obsidian).
    - Convert \\(...\\) -> $...$
    - Convert \\[...\\] -> $$...$$
    """

    inline_math_re = re.compile(r'\$(?!\$)([^$\n]+?)\$(?!\$)')
    display_math_re = re.compile(r'\$\$(.+?)\$\$', flags=re.DOTALL)

    def _display_cleanup(match: re.Match) -> str:
        inner = match.group(1).strip()
        return f"\n$$\n{inner}\n$$\n"

    def _normalize_inline_spans(value: str) -> str:
        result = []
        last = 0
        for match in inline_math_re.finditer(value):
            start, end = match.span()
            inner = match.group(1).strip()

            result.append(value[last:start])

            if start > 0 and (value[start - 1].isalnum() or value[start - 1] in ")]"):
                if not result[-1].endswith((" ", "\n", "\t", "(")):
                    result.append(" ")

            result.append(f"${inner}$")

            if end < len(value) and (value[end].isalnum() or value[end] in "(["):
                result.append(" ")

            last = end

        result.append(value[last:])
        return "".join(result)

    text = re.sub(r'\\\[(.+?)\\\]', r'$$\1$$', text, flags=re.DOTALL)
    text = re.sub(r'\\\((.+?)\\\)', r'$\1$', text, flags=re.DOTALL)
    text = display_math_re.sub(_display_cleanup, text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = _normalize_inline_spans(text)
    return text


def build_note(
    chap_num: int,
    chap_title: str,
    book_title: str,
    pdf_name: str,
    page_start: int,
    page_end: int,
    model: str,
    body: str,
) -> str:
    return textwrap.dedent(f"""\
        ---
        title: "Ch {chap_num}: {chap_title}"
        book: "{book_title}"
        source: "{pdf_name}"
        pages: "{page_start}–{page_end}"
        chapter: {chap_num}
        type: chapter-summary
        status: auto-generated
        model: {model}
        date: {date.today().isoformat()}
        tags: [knowledge-base, auto-ingested, chapter-note]
        ---

        # Chapter {chap_num}: {chap_title}

        > *Auto-generated rich summary — {book_title}*
        > *Pages {page_start}–{page_end} | Ingested {date.today().isoformat()}*

        {body}

        ---
        *Generated by `ingest_chapters.py` · model: {model}*
    """)


# ── Main ──────────────────────────────────────────────────────────────────────

def process_pdf(
    pdf_path: Path,
    out_dir: Path,
    force: bool,
    dry_run: bool,
    client: OpenAI,
    model: str,
    chunk_chars: int,
    merge_batch_size: int,
) -> None:
    book_title = re.sub(r'[_.]', ' ', pdf_path.stem).strip()
    print(f"\n{'='*60}")
    print(f"  Book: {pdf_path.name}")
    print(f"  Output: {out_dir}")
    print(f"{'='*60}")

    print("  Extracting pages...", end=" ", flush=True)
    pages = extract_pages(pdf_path)
    print(f"{len(pages)} pages")

    chapters = detect_chapters(pages)
    if not chapters:
        print("  [WARN] No chapter headings detected — skipping chapter-level ingestion.")
        return

    ranges = chapter_page_ranges(chapters, len(pages))
    print(f"  Detected {len(ranges)} chapter(s):\n")
    for num, start, title, end in ranges:
        chars = len(chapter_text(pages, start, end))
        print(f"    Ch {num:2d}  p{start+1:4d}–{end:4d}  {chars:7,} chars  {title}")

    if dry_run:
        print("\n  [DRY RUN] No API calls made.")
        return

    out_dir.mkdir(parents=True, exist_ok=True)

    for chap_num, start, chap_title, end in ranges:
        fname = f"chapter_{chap_num:02d}_{slug(chap_title)}.md"
        out_path = out_dir / fname

        if out_path.exists() and not force:
            print(f"\n  [SKIP] Ch {chap_num}: {chap_title}")
            continue

        print(f"\n  [PROC] Ch {chap_num}: {chap_title}")
        text = chapter_text(pages, start, end)
        if not text.strip():
            print("    [WARN] No text — skipping.")
            continue

        chunks = chunk_text(text, chunk_chars)
        print(f"    {len(chunks)} chunk(s), {len(text):,} chars total ({chunk_chars:,} chars/chunk)")

        try:
            summaries = [
                summarise_chunk(client, model, c, i, len(chunks), chap_num, chap_title, book_title)
                for i, c in enumerate(chunks)
            ]
            body = hierarchical_merge(
                client,
                model,
                summaries,
                chap_num,
                chap_title,
                book_title,
                merge_batch_size,
            )
            body = normalize_math_delimiters(body)
        except Exception as e:
            print(f"    [ERR] {e}")
            continue

        note = build_note(
            chap_num, chap_title, book_title, pdf_path.name,
            start + 1, end, model, body
        )
        out_path.write_text(note, encoding="utf-8")
        print(f"    [OK ] Written: {out_path.relative_to(out_dir.parent.parent)}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Ingest PDFs chapter-by-chapter into wiki")
    parser.add_argument("--force",   action="store_true", help="Re-process already-done chapters")
    parser.add_argument("--dry-run", action="store_true", help="Detect chapters only, no API calls")
    parser.add_argument(
        "--pdf",
        help="Process only this PDF filename (default: all GTM-style PDFs in raw/)",
    )
    parser.add_argument(
        "--model",
        default="auto",
        help="Model name (default: auto; tries gpt-4o then falls back to gpt-4o-mini)",
    )
    parser.add_argument(
        "--chunk-chars",
        type=int,
        default=0,
        help="Override chunk size in characters (default depends on model)",
    )
    args = parser.parse_args()

    topic_dir = Path(__file__).parent
    raw_dir   = topic_dir / "raw"
    wiki_dir  = topic_dir / "wiki"

    if not raw_dir.exists():
        print(f"[ERR] raw/ not found at {raw_dir}")
        sys.exit(1)

    pdfs = sorted(raw_dir.rglob("*.pdf"))
    if args.pdf:
        pdfs = [p for p in pdfs if p.name == args.pdf]

    # Exclude homework-style files unless explicitly requested
    if not args.pdf:
        pdfs = [p for p in pdfs if not re.search(r'hw|homework|exercise', p.name, re.IGNORECASE)]

    if not pdfs:
        print("[ERR] No matching PDFs found.")
        sys.exit(1)

    model = args.model.strip()
    if not model:
        print("[ERR] --model cannot be empty")
        sys.exit(1)

    if args.dry_run:
        client = None
    else:
        token = TOKEN.strip().strip('"').strip("'")
        if not token or "PASTE" in token:
            print("[ERR] TOKEN not set.")
            sys.exit(1)
        client = OpenAI(base_url=BASE_URL, api_key=token)

    if not args.dry_run:
        model = resolve_model(client, model)
    elif model == "auto":
        model = DEFAULT_MODEL

    chunk_chars = args.chunk_chars or MODEL_CHUNK_DEFAULTS.get(model, 12_000)
    merge_batch_size = MODEL_MERGE_BATCH_DEFAULTS.get(model, 4)
    if chunk_chars < 1_000:
        print("[ERR] --chunk-chars must be at least 1000")
        sys.exit(1)

    print(f"=== Chapter-level Ingestion ===")
    print(
        f"Model:    {model}  |  Chunk: {chunk_chars:,} chars  |  "
        f"Merge batch: {merge_batch_size}  |  Force: {args.force}"
    )

    for pdf_path in pdfs:
        book_slug = re.sub(r'[^a-zA-Z0-9]', '_', pdf_path.stem)[:40]
        out_dir   = wiki_dir / "chapters" / book_slug
        process_pdf(
            pdf_path,
            out_dir,
            args.force,
            args.dry_run,
            client,
            model,
            chunk_chars,
            merge_batch_size,
        )

    print("\nDone.")


if __name__ == "__main__":
    main()
