#!/usr/bin/env python3
"""Sync multilingual spaces content from gitbook-monorepo-live3 to this repo."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from normalize_spaces_markdown import normalize_spaces


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source",
        default="../gitbook-monorepo-live3/spaces",
        help="Source spaces directory (default: ../gitbook-monorepo-live3/spaces)",
    )
    parser.add_argument(
        "--target",
        default="spaces",
        help="Target spaces directory (default: spaces)",
    )
    parser.add_argument(
        "--no-clean",
        action="store_true",
        help="Do not remove target before copying; merge into existing files.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    here = Path(__file__).resolve().parent
    repo_root = here.parent
    source = (repo_root / args.source).resolve()
    target = (repo_root / args.target).resolve()

    if not source.exists() or not source.is_dir():
        raise SystemExit(f"Source directory not found: {source}")

    if source == target:
        raise SystemExit("Source and target cannot be the same directory.")

    if target.exists() and not args.no_clean:
        shutil.rmtree(target)
    target.mkdir(parents=True, exist_ok=True)

    # Python 3.8+ supports dirs_exist_ok; workspace uses newer runtime.
    shutil.copytree(source, target, dirs_exist_ok=True)
    normalized = normalize_spaces(target)

    print(
        f"Synchronized spaces content:\n- source: {source}\n- target: {target}\n- normalized_files: {normalized}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
