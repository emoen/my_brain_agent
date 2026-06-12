from pathlib import Path
import re


INLINE_MATH_RE = re.compile(r'\$(?!\$)([^$\n]+?)\$(?!\$)')
DISPLAY_MATH_RE = re.compile(r'\$\$(.+?)\$\$', flags=re.DOTALL)


def normalize_display_math_blocks(text: str) -> str:
    """Ensure each display math block is isolated on its own lines."""

    def _display_cleanup(match: re.Match) -> str:
        inner = match.group(1).strip()
        return f"\n$$\n{inner}\n$$\n"

    text = DISPLAY_MATH_RE.sub(_display_cleanup, text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text


def normalize_inline_math_spans(text: str) -> str:
    """Trim inline math and repair missing spacing around inline math spans."""
    result = []
    last = 0

    for match in INLINE_MATH_RE.finditer(text):
        start, end = match.span()
        inner = match.group(1).strip()

        result.append(text[last:start])

        if start > 0 and (text[start - 1].isalnum() or text[start - 1] in ")]"):
            if not result[-1].endswith((" ", "\n", "\t", "(")):
                result.append(" ")

        result.append(f"${inner}$")

        if end < len(text) and (text[end].isalnum() or text[end] in "(["):
            result.append(" ")

        last = end

    result.append(text[last:])
    return "".join(result)


def normalize_math_delimiters(text: str) -> str:
    # Convert LaTeX delimiters into Markdown math delimiters.
    text = re.sub(r'\\\[(.+?)\\\]', r'$$\1$$', text, flags=re.DOTALL)
    text = re.sub(r'\\\((.+?)\\\)', r'$\1$', text, flags=re.DOTALL)

    text = normalize_display_math_blocks(text)
    text = normalize_inline_math_spans(text)
    return text


def main() -> None:
    root = Path(__file__).parent / "wiki"
    files = sorted(root.rglob("*.md"))
    changed = 0

    for file_path in files:
        original = file_path.read_text(encoding="utf-8")
        fixed = normalize_math_delimiters(original)
        if fixed != original:
            file_path.write_text(fixed, encoding="utf-8")
            changed += 1
            print(f"[OK ] {file_path.relative_to(root.parent)}")

    print(f"\nDone. Updated {changed} file(s).")


if __name__ == "__main__":
    main()
