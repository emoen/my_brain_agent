#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


REF_PATTERN = re.compile(
    r"\b(Theorem|Lemma|Corollary|Proposition)\s+(\d+(?:\.\d+)*)\b",
    re.IGNORECASE,
)


@dataclass
class Node:
    node_id: str
    chapter_id: str
    chapter_title: str
    kind: str
    number: str
    title: str
    line_start: int


@dataclass
class Edge:
    source: str
    target: str
    reason: str


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def chapter_meta(path: Path) -> tuple[str, str]:
    stem = path.stem
    match = re.match(r"chapter_(\d+)_", stem)
    chapter_id = f"ch{int(match.group(1)):02d}" if match else slugify(stem)
    chapter_title = stem.replace("chapter_", "").replace("_", " ")
    return chapter_id, chapter_title


def clean_heading(line: str) -> str:
    heading = re.sub(r"^\s*#+\s*", "", line).strip()
    heading = heading.replace("**", "")
    return heading.strip()


def parse_heading(heading: str) -> tuple[str, str, str] | None:
    match = re.match(
        r"^(Theorem|Lemma|Corollary|Proposition)\s+(\d+(?:\.\d+)*)\s*:?\s*(.*)$",
        heading,
        flags=re.IGNORECASE,
    )
    if not match:
        return None
    kind = match.group(1).title()
    number = match.group(2)
    title = match.group(3).strip() or f"{kind} {number}"
    return kind, number, title


def canonical_title(node: Node) -> str:
    base = normalize_text(node.title)
    if base == normalize_text(f"{node.kind} {node.number}"):
        return ""
    return base


def find_nodes_in_chapter(path: Path) -> tuple[list[Node], list[tuple[Node, int, int]]]:
    chapter_id, chapter_title = chapter_meta(path)
    lines = path.read_text(encoding="utf-8").splitlines()

    section_start = 0
    section_pattern = re.compile(r"^\s*##\s+Theorems, Lemmas\s*&\s*Corollaries", re.IGNORECASE)
    for index, line in enumerate(lines):
        if section_pattern.search(line):
            section_start = index
            break

    raw_nodes: list[tuple[Node, int]] = []

    for index in range(section_start, len(lines)):
        line = lines[index]
        if not line.lstrip().startswith("#"):
            continue

        heading = clean_heading(line)
        parsed = parse_heading(heading)
        if not parsed:
            continue

        kind, number, title = parsed
        node_id = f"{chapter_id}:{kind.lower()}_{number}"
        raw_nodes.append(
            (
                Node(
                    node_id=node_id,
                    chapter_id=chapter_id,
                    chapter_title=chapter_title,
                    kind=kind,
                    number=number,
                    title=title,
                    line_start=index + 1,
                ),
                index,
            )
        )

    nodes: list[Node] = []
    blocks: list[tuple[Node, int, int]] = []

    for idx, (node, start_index) in enumerate(raw_nodes):
        end_index = raw_nodes[idx + 1][1] if idx + 1 < len(raw_nodes) else len(lines)
        nodes.append(node)
        blocks.append((node, start_index, end_index))

    return nodes, blocks


def resolve_local_ref(
    current: Node,
    kind: str,
    number: str,
    local_index: dict[tuple[str, str], str],
    global_title_index: dict[str, str],
) -> str | None:
    key = (kind.lower(), number)
    local = local_index.get(key)
    if local:
        return local

    name_key = f"{kind.title()} {number}".lower()
    return global_title_index.get(name_key)


def dedupe_edges(edges: list[Edge]) -> list[Edge]:
    deduped: dict[tuple[str, str], Edge] = {}

    def score(reason: str) -> int:
        return 0 if "title" in reason.lower() else 1

    for edge in edges:
        key = (edge.source, edge.target)
        current = deduped.get(key)
        if current is None or score(edge.reason) > score(current.reason):
            deduped[key] = edge
    return list(deduped.values())


def build_graph(chapter_files: list[Path]) -> tuple[dict[str, Node], list[Edge], dict[str, list[Node]], list[str]]:
    all_nodes: dict[str, Node] = {}
    chapter_blocks: list[tuple[Path, list[Node], list[tuple[Node, int, int]]]] = []
    chapter_nodes: dict[str, list[Node]] = {}
    chapter_order: list[str] = []

    for chapter_file in chapter_files:
        nodes, blocks = find_nodes_in_chapter(chapter_file)
        chapter_id, _ = chapter_meta(chapter_file)
        chapter_order.append(chapter_id)
        chapter_nodes[chapter_id] = list(nodes)
        for node in nodes:
            all_nodes[node.node_id] = node
        chapter_blocks.append((chapter_file, nodes, blocks))

    global_title_index: dict[str, str] = {}
    canonical_to_ids: dict[str, set[str]] = {}
    for node_id, node in all_nodes.items():
        global_title_index[f"{node.kind} {node.number}".lower()] = node_id
        ctitle = canonical_title(node)
        if ctitle:
            canonical_to_ids.setdefault(ctitle, set()).add(node_id)

    edges: list[Edge] = []

    for chapter_file, nodes, blocks in chapter_blocks:
        lines = chapter_file.read_text(encoding="utf-8").splitlines()
        local_index = {(node.kind.lower(), node.number): node.node_id for node in nodes}

        for node, start, end in blocks:
            body = "\n".join(lines[start:end])

            for match in REF_PATTERN.finditer(body):
                ref_kind = match.group(1).title()
                ref_number = match.group(2)

                target_id = resolve_local_ref(node, ref_kind, ref_number, local_index, global_title_index)
                if not target_id or target_id == node.node_id:
                    continue

                edges.append(
                    Edge(
                        source=node.node_id,
                        target=target_id,
                        reason=f"mentions {ref_kind} {ref_number}",
                    )
                )

            body_norm = normalize_text(body)
            for ctitle, candidate_ids in canonical_to_ids.items():
                if len(ctitle) < 12:
                    continue
                if ctitle not in body_norm:
                    continue
                candidates = list(candidate_ids)
                if len(candidates) > 1:
                    same_chapter = [cid for cid in candidates if all_nodes[cid].chapter_id == node.chapter_id]
                    if len(same_chapter) == 1:
                        candidates = same_chapter
                    else:
                        continue

                for candidate_id in candidates:
                    if candidate_id == node.node_id:
                        continue
                    candidate_node = all_nodes[candidate_id]
                    edges.append(
                        Edge(
                            source=node.node_id,
                            target=candidate_id,
                            reason=f"mentions {candidate_node.kind} {candidate_node.number} title",
                        )
                    )

    logical_edges = dedupe_edges(edges)

    incoming_by_target: dict[str, list[Edge]] = {}
    for edge in logical_edges:
        incoming_by_target.setdefault(edge.target, []).append(edge)

    inferred_edges: list[Edge] = []
    parent_kinds = {"Theorem", "Proposition", "Lemma"}
    for chapter_id in chapter_order:
        nodes_in_chapter = chapter_nodes.get(chapter_id, [])
        for index, node in enumerate(nodes_in_chapter):
            if node.kind != "Corollary":
                continue
            if incoming_by_target.get(node.node_id):
                continue

            parent: Node | None = None
            for back in range(index - 1, -1, -1):
                candidate = nodes_in_chapter[back]
                if candidate.kind in parent_kinds:
                    parent = candidate
                    break

            if parent is None:
                continue

            inferred_edges.append(
                Edge(
                    source=parent.node_id,
                    target=node.node_id,
                    reason=f"inferred parent for {node.kind.lower()} {node.number}",
                )
            )

    return all_nodes, dedupe_edges(logical_edges + inferred_edges), chapter_nodes, chapter_order


def build_tree_edges(chapter_node_ids: dict[str, list[str]], chapter_order: list[str]) -> list[Edge]:
    edges: list[Edge] = []

    for chapter_id in chapter_order:
        node_ids = chapter_node_ids.get(chapter_id, [])
        for index in range(len(node_ids) - 1):
            edges.append(
                Edge(
                    source=node_ids[index],
                    target=node_ids[index + 1],
                    reason="next in chapter",
                )
            )

    for index in range(len(chapter_order) - 1):
        left_nodes = chapter_node_ids.get(chapter_order[index], [])
        right_nodes = chapter_node_ids.get(chapter_order[index + 1], [])
        if not left_nodes or not right_nodes:
            continue

        edges.append(
            Edge(
                source=left_nodes[-1],
                target=right_nodes[0],
                reason="next chapter",
            )
        )

    return dedupe_edges(edges)


def node_label(node: Node) -> str:
    return f"{node.chapter_id.upper()} {node.kind} {node.number}: {node.title}"


def write_dot(nodes: dict[str, Node], edges: list[Edge], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "digraph theorem_graph {",
        "  rankdir=LR;",
        "  node [shape=box, style=rounded];",
    ]

    for node_id, node in sorted(nodes.items()):
        label = node_label(node).replace('"', "\\\"")
        lines.append(f'  "{node_id}" [label="{label}"];')

    for edge in sorted(edges, key=lambda e: (e.source, e.target, e.reason)):
        label = edge.reason.replace('"', "\\\"")
        lines.append(f'  "{edge.source}" -> "{edge.target}" [label="{label}"];')

    lines.append("}")
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_mermaid(nodes: dict[str, Node], edges: list[Edge], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["graph LR"]

    for node_id, node in sorted(nodes.items()):
        label = node_label(node).replace('"', "'")
        lines.append(f'    {slugify(node_id)}["{label}"]')

    node_key_map = {node_id: slugify(node_id) for node_id in nodes}

    for edge in sorted(edges, key=lambda e: (e.source, e.target, e.reason)):
        source = node_key_map[edge.source]
        target = node_key_map[edge.target]
        reason = edge.reason.replace('"', "'")
        lines.append(f'    {source} -- "{reason}" --> {target}')

    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build logical theorem dependency graph from chapter markdown files.")
    parser.add_argument(
        "--chapters-dir",
        type=Path,
        default=Path("wiki/chapters"),
        help="Directory containing chapter markdown files.",
    )
    parser.add_argument(
        "--dot-out",
        type=Path,
        default=Path("wiki/graphs/theorem_graph.dot"),
        help="Path for Graphviz DOT output.",
    )
    parser.add_argument(
        "--mermaid-out",
        type=Path,
        default=Path("wiki/graphs/theorem_graph.mmd"),
        help="Path for Mermaid graph output.",
    )
    parser.add_argument(
        "--mode",
        choices=["dependency", "logical"],
        default="logical",
        help="dependency: numbered references only; logical: numbered + explicit theorem-title mentions.",
    )
    args = parser.parse_args()

    chapter_files = sorted(args.chapters_dir.glob("**/*.md"))
    if not chapter_files:
        raise SystemExit(f"No chapter markdown files found under {args.chapters_dir}")

    nodes, dependency_edges, _, _ = build_graph(chapter_files)

    if args.mode == "dependency":
        edges = dependency_edges
    else:
        edges = dependency_edges

    write_dot(nodes, edges, args.dot_out)
    write_mermaid(nodes, edges, args.mermaid_out)

    print(f"Chapters scanned: {len(chapter_files)}")
    print(f"Nodes found: {len(nodes)}")
    print(f"Mode: {args.mode}")
    print(f"Logical dependency edges found: {len(dependency_edges)}")
    print(f"Edges written: {len(edges)}")
    print(f"DOT output: {args.dot_out}")
    print(f"Mermaid output: {args.mermaid_out}")


if __name__ == "__main__":
    main()