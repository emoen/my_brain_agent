#!/usr/bin/env python3
"""
LLM-Enhanced Theorem Dependency Graph Builder
==============================================
Uses GPT-4o to identify conceptual dependencies between theorems,
producing a much richer graph than regex-based reference detection.

For each theorem/proposition/lemma, the LLM is asked:
  "Which earlier results does this theorem depend on or use in its proof?"

Usage:
    cd commutative_algebra
    source ../load_env.sh
    python3 build_theorem_graph_llm.py
    python3 build_theorem_graph_llm.py --dry-run   # just list theorems, no API calls
    python3 build_theorem_graph_llm.py --force     # re-analyze all (ignore cache)
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from dataclasses import dataclass, asdict
from pathlib import Path

from openai import OpenAI

# ── Config ────────────────────────────────────────────────────────────────────
TOKEN = os.environ["GITHUB_MODELS_TOKEN"]
MODEL = "gpt-4o"
BASE_URL = "https://models.inference.ai.azure.com"

MAX_RETRIES = 3
RETRY_DELAY = 65  # seconds to wait on rate limit


# ── Data classes ──────────────────────────────────────────────────────────────
@dataclass
class TheoremNode:
    node_id: str
    chapter: int
    kind: str       # Theorem, Proposition, Lemma, Corollary
    number: str     # e.g. "5.10"
    title: str      # e.g. "(Going-Up Theorem)" or just "Proposition 3.3"
    statement: str  # Full statement text from wiki


@dataclass
class Edge:
    source: str
    target: str
    reason: str


# ── Parsing ───────────────────────────────────────────────────────────────────
HEADING_RE = re.compile(
    r"^###?\s+(?:\*\*)?(Theorem|Proposition|Lemma|Corollary)\s+"
    r"(\d+(?:\.\d+)*)\s*:?\s*(.*?)(?:\*\*)?$",
    re.IGNORECASE,
)


def parse_chapter_num(path: Path) -> int:
    """Extract chapter number from filename like chapter_05_..."""
    m = re.search(r"chapter_(\d+)", path.stem)
    return int(m.group(1)) if m else 0


def extract_theorems(chapter_files: list[Path]) -> list[TheoremNode]:
    """Parse all theorem headings and their statements from chapter markdown files."""
    theorems = []
    seen_ids = set()

    for path in chapter_files:
        chapter_num = parse_chapter_num(path)
        lines = path.read_text(encoding="utf-8").splitlines()

        # Only look in the "Theorems, Lemmas & Corollaries" section
        in_section = False
        i = 0
        while i < len(lines):
            line = lines[i].strip()

            # Detect start of theorems section
            if re.match(r"^##\s+Theorems", line, re.IGNORECASE):
                in_section = True
                i += 1
                continue

            # Detect end of section (next ## heading that isn't a theorem)
            if in_section and re.match(r"^##\s+(?!#)", line) and not re.match(r"^##\s+Theorems", line, re.IGNORECASE):
                in_section = False
                i += 1
                continue

            if not in_section:
                i += 1
                continue

            m = HEADING_RE.match(line)
            if m:
                kind = m.group(1).title()
                number = m.group(2)
                title = m.group(3).strip().rstrip("*").strip()
                if not title:
                    title = f"{kind} {number}"

                node_id = f"ch{chapter_num:02d}:{kind.lower()}_{number}"

                # Skip duplicates
                if node_id in seen_ids:
                    i += 1
                    continue
                seen_ids.add(node_id)

                # Collect the body until next heading
                body_lines = []
                i += 1
                while i < len(lines):
                    if lines[i].strip().startswith("#"):
                        break
                    body_lines.append(lines[i])
                    i += 1

                statement = "\n".join(body_lines).strip()
                # Limit statement to ~800 chars to save tokens
                if len(statement) > 800:
                    statement = statement[:800] + "..."

                theorems.append(TheoremNode(
                    node_id=node_id,
                    chapter=chapter_num,
                    kind=kind,
                    number=number,
                    title=title,
                    statement=statement,
                ))
            else:
                i += 1

    return theorems


# ── LLM Dependency Detection ─────────────────────────────────────────────────
SYSTEM_PROMPT = """\
You are an expert in commutative algebra analyzing theorem dependencies.
Given a theorem and a list of earlier results, identify which earlier results
this theorem DIRECTLY depends on (used in its proof or required as a hypothesis).

Reply with a JSON array of objects: [{"number": "X.Y", "reason": "brief explanation"}]
Only include results that are genuinely used. If none apply, return [].
Be specific about WHY each dependency exists (e.g. "uses Nakayama to show...")."""


def build_prompt(theorem: TheoremNode, earlier: list[TheoremNode]) -> str:
    """Build the user prompt for dependency detection."""
    earlier_list = "\n".join(
        f"  - {t.kind} {t.number}: {t.title}"
        + (f"\n    Statement: {t.statement[:200]}" if t.statement else "")
        for t in earlier
    )

    return f"""Analyze dependencies for:

**{theorem.kind} {theorem.number}: {theorem.title}**
{theorem.statement[:600]}

---
Earlier results available (from chapters 1–{theorem.chapter}):
{earlier_list}

Which of these earlier results does {theorem.kind} {theorem.number} directly depend on?
Return JSON array: [{{"number": "X.Y", "reason": "why"}}]"""


def query_dependencies(
    client: OpenAI,
    theorem: TheoremNode,
    earlier: list[TheoremNode],
) -> list[dict]:
    """Ask the LLM which earlier results this theorem depends on."""
    if not earlier:
        return []

    prompt = build_prompt(theorem, earlier)

    for attempt in range(MAX_RETRIES):
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt},
                ],
                max_tokens=1000,
                temperature=0,
            )
            text = response.choices[0].message.content.strip()

            # Extract JSON from response (handle markdown code blocks)
            json_match = re.search(r"\[.*\]", text, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
            return []

        except Exception as exc:
            msg = str(exc)
            if "429" in msg or "RateLimitReached" in msg:
                print(f"    [RATE LIMIT] Waiting {RETRY_DELAY}s...")
                time.sleep(RETRY_DELAY)
            else:
                print(f"    [ERROR] {msg}")
                if attempt == MAX_RETRIES - 1:
                    return []
                time.sleep(5)

    return []


# ── Graph Output ──────────────────────────────────────────────────────────────
def write_dot(nodes: list[TheoremNode], edges: list[Edge], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "digraph theorem_graph {",
        "  rankdir=TB;",
        "  node [shape=box, style=rounded];",
        "",
        "  // Color by chapter",
    ]

    colors = [
        "#FFB3BA", "#FFDFBA", "#FFFFBA", "#BAFFC9", "#BAE1FF",
        "#E8BAFF", "#FFB3E6", "#B3FFE6", "#FFE6B3", "#B3D9FF",
        "#D9B3FF",
    ]

    for node in sorted(nodes, key=lambda n: (n.chapter, n.number)):
        color = colors[(node.chapter - 1) % len(colors)]
        label = f"{node.kind} {node.number}\\n{node.title}".replace('"', '\\"')
        lines.append(f'  "{node.node_id}" [label="{label}", fillcolor="{color}", style="rounded,filled"];')

    lines.append("")

    for edge in sorted(edges, key=lambda e: (e.source, e.target)):
        reason = edge.reason.replace('"', '\\"')
        # Truncate long reasons for readability
        if len(reason) > 50:
            reason = reason[:47] + "..."
        lines.append(f'  "{edge.source}" -> "{edge.target}" [label="{reason}", fontsize=9];')

    lines.append("}")
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_mermaid(nodes: list[TheoremNode], edges: list[Edge], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["graph TB"]

    def slug(node_id: str) -> str:
        return re.sub(r"[^a-z0-9]+", "_", node_id.lower()).strip("_")

    for node in sorted(nodes, key=lambda n: (n.chapter, n.number)):
        label = f"{node.kind} {node.number}: {node.title}".replace('"', "'")
        lines.append(f'    {slug(node.node_id)}["{label}"]')

    lines.append("")

    for edge in sorted(edges, key=lambda e: (e.source, e.target)):
        reason = edge.reason.replace('"', "'")
        if len(reason) > 40:
            reason = reason[:37] + "..."
        lines.append(f'    {slug(edge.source)} -->|"{reason}"| {slug(edge.target)}')

    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


# ── Cache ─────────────────────────────────────────────────────────────────────
def load_cache(cache_path: Path) -> dict:
    if cache_path.exists():
        return json.loads(cache_path.read_text(encoding="utf-8"))
    return {}


def save_cache(cache_path: Path, cache: dict) -> None:
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(json.dumps(cache, indent=2), encoding="utf-8")


# ── Main ──────────────────────────────────────────────────────────────────────
def main() -> None:
    parser = argparse.ArgumentParser(
        description="LLM-enhanced theorem dependency graph builder."
    )
    parser.add_argument(
        "--chapters-dir", type=Path, default=Path("wiki/chapters"),
        help="Directory containing chapter markdown files.",
    )
    parser.add_argument(
        "--dot-out", type=Path, default=Path("wiki/graphs/theorem_graph_llm.dot"),
        help="Path for Graphviz DOT output.",
    )
    parser.add_argument(
        "--mermaid-out", type=Path, default=Path("wiki/graphs/theorem_graph_llm.mmd"),
        help="Path for Mermaid graph output.",
    )
    parser.add_argument("--dry-run", action="store_true", help="List theorems only, no API calls.")
    parser.add_argument("--force", action="store_true", help="Ignore cache, re-analyze all.")
    args = parser.parse_args()

    chapter_files = sorted(args.chapters_dir.glob("**/*.md"))
    if not chapter_files:
        raise SystemExit(f"No chapter markdown files found under {args.chapters_dir}")

    print(f"=== LLM-Enhanced Theorem Graph Builder ===")
    print(f"Chapters: {len(chapter_files)}")

    theorems = extract_theorems(chapter_files)
    print(f"Theorems/Propositions/Lemmas found: {len(theorems)}")
    print()

    if args.dry_run:
        for t in theorems:
            print(f"  {t.kind:12s} {t.number:6s} Ch{t.chapter:02d}  {t.title}")
        print(f"\n[DRY RUN] No API calls made.")
        return

    # LLM dependency analysis
    client = OpenAI(base_url=BASE_URL, api_key=TOKEN)

    cache_path = Path("wiki/graphs/.dep_cache.json")
    cache = {} if args.force else load_cache(cache_path)

    edges: list[Edge] = []
    node_index = {t.number: t for t in theorems}

    total = len(theorems)
    for idx, theorem in enumerate(theorems):
        # Get all earlier theorems (from earlier chapters, or earlier in same chapter)
        earlier = [t for t in theorems if t.chapter < theorem.chapter
                   or (t.chapter == theorem.chapter and t.number < theorem.number)]

        if theorem.node_id in cache:
            deps = cache[theorem.node_id]
            print(f"  [{idx+1}/{total}] {theorem.kind} {theorem.number} — {len(deps)} deps (cached)")
        else:
            print(f"  [{idx+1}/{total}] {theorem.kind} {theorem.number} — querying LLM...", end="", flush=True)
            deps = query_dependencies(client, theorem, earlier)
            cache[theorem.node_id] = deps
            save_cache(cache_path, cache)
            print(f" {len(deps)} deps found")
            # Small delay to stay under rate limits
            time.sleep(2)

        for dep in deps:
            ref_num = dep.get("number", "")
            reason = dep.get("reason", "depends on")
            target = node_index.get(ref_num)
            if target:
                edges.append(Edge(
                    source=target.node_id,
                    target=theorem.node_id,
                    reason=reason,
                ))

    # Write outputs
    write_dot(theorems, edges, args.dot_out)
    write_mermaid(theorems, edges, args.mermaid_out)

    print(f"\n=== Results ===")
    print(f"Nodes: {len(theorems)}")
    print(f"Edges: {len(edges)}")
    print(f"DOT:     {args.dot_out}")
    print(f"Mermaid: {args.mermaid_out}")
    print(f"Cache:   {cache_path}")

    # Stats
    in_degree = {}
    out_degree = {}
    for e in edges:
        in_degree[e.target] = in_degree.get(e.target, 0) + 1
        out_degree[e.source] = out_degree.get(e.source, 0) + 1

    if out_degree:
        most_used = sorted(out_degree.items(), key=lambda x: -x[1])[:5]
        print(f"\nMost depended-on results:")
        for node_id, count in most_used:
            node = next(t for t in theorems if t.node_id == node_id)
            print(f"  {count:3d} deps ← {node.kind} {node.number}: {node.title}")


if __name__ == "__main__":
    main()
