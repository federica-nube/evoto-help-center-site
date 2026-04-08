#!/usr/bin/env python3
"""Normalize synced GitBook markdown for cleaner GitBook/help-center rendering."""

from __future__ import annotations

import argparse
import re
from pathlib import Path, PurePosixPath


FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?(.*)$", re.S)
TITLE_RE = re.compile(r'^title:\s*"?(.*?)"?\s*$', re.M)
SOURCE_TYPE_RE = re.compile(r'^source_type:\s*"?(.*?)"?\s*$', re.M)
LANGUAGE_RE = re.compile(r'^language:\s*"?(.*?)"?\s*$', re.M)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")
IMAGE_RE = re.compile(r"!\[[^\]]*\]\([^)]+\)")
LIST_ITEM_RE = re.compile(r"^(\s*(?:[-*]|\d+\.)\s+)(.*)$")
WP_BLOCK_MARKER_RE = re.compile(r"^\s*/?wp:[\w/-]+(?:\s.*)?\s*$")

ARTICLE_SOURCE_TYPES = {"page", "post"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default="spaces", help="Root directory that contains language spaces")
    return parser.parse_args()


def normalize_space(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def strip_wrapping_emphasis(text: str) -> str:
    value = (text or "").strip()
    changed = True
    while changed and value:
        changed = False
        for marker in ("**", "*"):
            if value.startswith(marker) and value.endswith(marker) and len(value) > len(marker) * 2:
                inner = value[len(marker) : -len(marker)].strip()
                if inner:
                    value = inner
                    changed = True
    return value


def parse_frontmatter(text: str) -> tuple[str, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return "", text
    return match.group(1), match.group(2)


def extract_frontmatter_value(pattern: re.Pattern[str], frontmatter: str) -> str:
    match = pattern.search(frontmatter)
    return match.group(1).strip() if match else ""


def derive_language_from_path(source_path: str) -> str:
    parts = PurePosixPath(source_path).parts
    if not parts:
        return ""
    if "spaces" in parts:
        index = parts.index("spaces")
        if index + 1 < len(parts):
            return parts[index + 1]
    for part in parts:
        if part not in {"", "/"}:
            return part
    return ""


def normalize_frontmatter(frontmatter: str, source_path: str) -> str:
    if not frontmatter:
        return frontmatter

    expected_language = derive_language_from_path(source_path)
    if not expected_language:
        return frontmatter

    if LANGUAGE_RE.search(frontmatter):
        return LANGUAGE_RE.sub(f'language: "{expected_language}"', frontmatter, count=1)

    lines = frontmatter.splitlines()
    insert_at = len(lines)
    for index, line in enumerate(lines):
        if line.startswith("source_id:"):
            insert_at = index + 1
            break
    lines.insert(insert_at, f'language: "{expected_language}"')
    return "\n".join(lines)


def strip_inline_wp_markers(line: str) -> str:
    result: list[str] = []
    index = 0
    length = len(line)

    while index < length:
        starts_marker = (
            (line.startswith("wp:", index) or line.startswith("/wp:", index))
            and (index == 0 or line[index - 1].isspace())
        )
        if not starts_marker:
            result.append(line[index])
            index += 1
            continue

        marker_is_closing = line.startswith("/wp:", index)
        marker_end = index + (3 if not marker_is_closing else 4)
        while marker_end < length and re.match(r"[\w/-]", line[marker_end]):
            marker_end += 1

        index = marker_end
        while index < length and line[index].isspace():
            index += 1

        if index < length and line[index] == "{":
            depth = 0
            in_string = False
            escaped = False
            while index < length:
                char = line[index]
                if in_string:
                    if escaped:
                        escaped = False
                    elif char == "\\":
                        escaped = True
                    elif char == '"':
                        in_string = False
                else:
                    if char == '"':
                        in_string = True
                    elif char == "{":
                        depth += 1
                    elif char == "}":
                        depth -= 1
                        if depth == 0:
                            index += 1
                            break
                index += 1

        while index < length and line[index].isspace():
            index += 1

        if not marker_is_closing and index < length and line[index] == "/":
            index += 1

        while index < length and line[index].isspace():
            index += 1

    normalized = "".join(result)
    normalized = re.sub(r"[ \t]{2,}", " ", normalized)
    return normalized.strip()


def split_line_around_images(line: str) -> list[str]:
    list_match = LIST_ITEM_RE.match(line)
    prefix = ""
    content = line
    if list_match:
        prefix, content = list_match.groups()

    matches = list(IMAGE_RE.finditer(content))
    if not matches:
        return [line]

    blocks: list[str] = []
    last = 0
    for match in matches:
        text = content[last : match.start()].strip()
        if text:
            blocks.append(text)
        blocks.append(match.group())
        last = match.end()

    tail = content[last:].strip()
    if tail:
        blocks.append(tail)

    if len(blocks) <= 1:
        if prefix and blocks and IMAGE_RE.fullmatch(blocks[0]):
            return [blocks[0]]
        return [line]

    if prefix:
        lines: list[str] = []
        indent = " " * len(prefix)
        first_block = blocks.pop(0)
        if IMAGE_RE.fullmatch(first_block):
            lines.append(prefix.rstrip())
            blocks.insert(0, first_block)
        else:
            lines.append(f"{prefix}{first_block}".rstrip())
        if blocks:
            lines.append("")
        for index, block in enumerate(blocks):
            lines.append(f"{indent}{block}".rstrip())
            if index != len(blocks) - 1:
                lines.append("")
        return lines

    lines = []
    for index, block in enumerate(blocks):
        lines.append(block)
        if index != len(blocks) - 1:
            lines.append("")
    return lines


def compact_paragraphs(lines: list[str]) -> list[str]:
    compacted: list[str] = []
    paragraph: list[str] = []

    def flush_paragraph() -> None:
        if paragraph:
            compacted.append(normalize_space(" ".join(paragraph)))
            paragraph.clear()

    for line in lines:
        stripped = line.strip()
        is_block = (
            not stripped
            or stripped.startswith(("#", ">", "```", "|"))
            or stripped == "---"
            or IMAGE_RE.fullmatch(stripped) is not None
            or LIST_ITEM_RE.match(line) is not None
            or line.startswith("    ")
        )
        if is_block:
            flush_paragraph()
            compacted.append(line)
            continue
        paragraph.append(stripped)

    flush_paragraph()
    return compacted


def normalize_body(body: str, page_title: str, source_type: str, source_path: str) -> str:
    cleaned_lines: list[str] = []
    first_heading_checked = False
    pending_details_summary = False
    demote_all_headings = source_type in ARTICLE_SOURCE_TYPES and not source_path.endswith("README.md")
    in_code_block = False

    for raw_line in body.splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()

        if stripped.startswith("```"):
            in_code_block = not in_code_block
            cleaned_lines.append(line)
            continue

        if not in_code_block:
            line = strip_inline_wp_markers(line)
            stripped = line.strip()

        if stripped == "wp:details":
            pending_details_summary = True
            continue
        if WP_BLOCK_MARKER_RE.fullmatch(stripped):
            continue

        if pending_details_summary and stripped:
            pending_details_summary = False
            if not stripped.startswith("#"):
                cleaned_lines.extend([f"## {strip_wrapping_emphasis(stripped)}", ""])
                continue

        line = re.sub(r"\*\*(\s*!\[[^\]]*\]\([^)]+\)\s*)\*\*", r"\1", line)
        line = re.sub(r"\*(\s*!\[[^\]]*\]\([^)]+\)\s*)\*", r"\1", line)

        heading_match = HEADING_RE.match(line)
        if heading_match:
            hashes, text = heading_match.groups()
            text = strip_wrapping_emphasis(text)
            text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
            text = re.sub(r"\*(.*?)\*", r"\1", text)
            if not first_heading_checked:
                first_heading_checked = True
                if normalize_space(text).casefold() == normalize_space(page_title).casefold():
                    continue
            level = len(hashes)
            if demote_all_headings:
                level = min(level + 1, 6)
            elif level == 1:
                level = 2
            line = f"{'#' * level} {text}"

        if IMAGE_RE.search(line):
            cleaned_lines.extend(split_line_around_images(line))
            continue

        cleaned_lines.append(line)

    compact = "\n".join(compact_paragraphs(cleaned_lines))
    compact = re.sub(r"[ \t]+\n", "\n", compact)
    compact = re.sub(r"\n{3,}", "\n\n", compact)
    return compact.strip() + "\n"


def normalize_markdown(text: str, source_path: str) -> str:
    frontmatter, body = parse_frontmatter(text)
    normalized_frontmatter = normalize_frontmatter(frontmatter, source_path)
    page_title = extract_frontmatter_value(TITLE_RE, normalized_frontmatter)
    source_type = extract_frontmatter_value(SOURCE_TYPE_RE, normalized_frontmatter)
    normalized_body = normalize_body(body, page_title, source_type, source_path)
    if not normalized_frontmatter:
        return normalized_body
    return f"---\n{normalized_frontmatter}\n---\n\n{normalized_body}"


def normalize_spaces(root: Path) -> int:
    changed = 0
    for markdown_path in sorted(root.rglob("*.md")):
        original = markdown_path.read_text(encoding="utf-8")
        normalized = normalize_markdown(original, markdown_path.as_posix())
        if normalized != original:
            markdown_path.write_text(normalized, encoding="utf-8")
            changed += 1
    return changed


def main() -> int:
    args = parse_args()
    root = Path(args.root).expanduser().resolve()
    if not root.exists() or not root.is_dir():
        raise SystemExit(f"Spaces root not found: {root}")

    changed = normalize_spaces(root)
    print(f"Normalized markdown files: {changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
