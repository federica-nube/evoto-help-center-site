#!/usr/bin/env python3
from __future__ import annotations

import json
import os
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "help-center-dist"


def normalize_base_path(value: str) -> str:
    cleaned = value.strip().strip("/")
    return f"/{cleaned}" if cleaned else ""


BASE_PATH = normalize_base_path(os.environ.get("HELP_CENTER_BASE_PATH", ""))


class HtmlLinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.hrefs: list[str] = []
        self.srcs: list[str] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = {key: value for key, value in attrs if value is not None}
        if tag == "a" and "href" in attr_map:
            self.hrefs.append(attr_map["href"])
        if tag in {"img", "script", "source"} and "src" in attr_map:
            self.srcs.append(attr_map["src"])
        element_id = attr_map.get("id")
        if element_id:
            self.ids.add(element_id)


def public_url_for_html(html_file: Path, root: Path) -> str:
    rel = html_file.relative_to(root)
    if rel == Path("index.html"):
        return f"{BASE_PATH}/" if BASE_PATH else "/"
    if rel == Path("search/index.html"):
        return f"{BASE_PATH}/search/" if BASE_PATH else "/search/"
    if rel.name == "index.html":
        parent = "/".join(quote(part, safe="") for part in rel.parent.parts)
        return f"{BASE_PATH}/{parent}/" if BASE_PATH else f"/{parent}/"
    encoded = "/".join(quote(part, safe="") for part in rel.parts)
    return f"{BASE_PATH}/{encoded}" if BASE_PATH else f"/{encoded}"


def resolve_local_ref(raw_ref: str, current_file: Path, root: Path) -> tuple[Path | None, str | None]:
    if not raw_ref or raw_ref.startswith(("mailto:", "tel:", "javascript:", "data:")):
        return None, None

    split = urlsplit(raw_ref)
    if split.scheme or split.netloc:
        return None, None

    ref_path = unquote(split.path)
    fragment = split.fragment or None

    if raw_ref.startswith("#"):
        return current_file.resolve(), fragment

    if BASE_PATH and ref_path.startswith(f"{BASE_PATH}/"):
        target = root / ref_path[len(BASE_PATH):].lstrip("/")
    elif BASE_PATH and ref_path == BASE_PATH:
        target = root / "index.html"
    elif ref_path.startswith("/"):
        target = root / ref_path.lstrip("/")
    else:
        target = current_file.parent / ref_path

    if target.is_dir():
        target = target / "index.html"
    elif target.suffix == "":
        target = target / "index.html"

    return target.resolve(), fragment


def main() -> None:
    if not OUTPUT_DIR.exists():
        raise SystemExit(f"Missing build output: {OUTPUT_DIR}")

    html_files = sorted(OUTPUT_DIR.rglob("*.html"))
    built_files = {path.resolve() for path in OUTPUT_DIR.rglob("*") if path.is_file()}
    parser_data: dict[Path, HtmlLinkParser] = {}

    for html_file in html_files:
        parser = HtmlLinkParser()
        parser.feed(html_file.read_text(encoding="utf-8"))
        parser_data[html_file.resolve()] = parser

    missing_targets: Counter[str] = Counter()
    missing_anchors: Counter[str] = Counter()

    for html_file, parser in parser_data.items():
        for ref in parser.hrefs + parser.srcs:
            target, fragment = resolve_local_ref(ref, html_file, OUTPUT_DIR)
            if target is None:
                continue
            if target not in built_files:
                missing_targets[ref] += 1
                continue
            if fragment and target.suffix == ".html":
                target_ids = parser_data.get(target)
                if target_ids and fragment not in target_ids.ids:
                    missing_anchors[f"{ref} -> #{fragment}"] += 1

    search_index_path = OUTPUT_DIR / "search-index.json"
    if not search_index_path.exists():
        raise SystemExit(f"Missing search index: {search_index_path}")

    search_entries = json.loads(search_index_path.read_text(encoding="utf-8"))
    search_urls = [entry.get("url") for entry in search_entries if isinstance(entry, dict)]
    search_url_counts = Counter(search_urls)

    duplicate_search_urls = Counter({url: count for url, count in search_url_counts.items() if url and count > 1})

    expected_search_urls = {
        public_url_for_html(html_file, OUTPUT_DIR)
        for html_file in html_files
        if html_file.relative_to(OUTPUT_DIR) not in {Path("index.html"), Path("404.html"), Path("search/index.html")}
    }
    actual_search_urls = {url for url in search_urls if isinstance(url, str)}

    missing_search_urls = sorted(expected_search_urls - actual_search_urls)
    unexpected_search_urls = sorted(actual_search_urls - expected_search_urls)

    issue_count = (
        sum(missing_targets.values())
        + sum(missing_anchors.values())
        + len(missing_search_urls)
        + len(unexpected_search_urls)
        + sum(duplicate_search_urls.values())
    )

    print(f"Validated {len(html_files)} HTML files in {OUTPUT_DIR}")
    print(f"Search entries: {len(search_entries)}")

    if missing_targets:
        print(f"Broken local refs: {sum(missing_targets.values())}")
        for ref, count in missing_targets.most_common(20):
            print(f"  {count}x {ref}")

    if missing_anchors:
        print(f"Broken anchors: {sum(missing_anchors.values())}")
        for ref, count in missing_anchors.most_common(20):
            print(f"  {count}x {ref}")

    if duplicate_search_urls:
        print(f"Duplicate search URLs: {sum(duplicate_search_urls.values())}")
        for url, count in duplicate_search_urls.most_common(20):
            print(f"  {count}x {url}")

    if missing_search_urls:
        print(f"Missing search URLs: {len(missing_search_urls)}")
        for url in missing_search_urls[:20]:
            print(f"  {url}")

    if unexpected_search_urls:
        print(f"Unexpected search URLs: {len(unexpected_search_urls)}")
        for url in unexpected_search_urls[:20]:
            print(f"  {url}")

    if issue_count:
        raise SystemExit("Help center validation failed.")

    print("Help center validation passed.")


if __name__ == "__main__":
    main()
