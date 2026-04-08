#!/usr/bin/env python3
from __future__ import annotations

import argparse
import functools
import http.server
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILD_SCRIPT = ROOT / "scripts" / "build_help_center.py"
OUTPUT_DIR = ROOT / "help-center-dist"
PREVIEW_ROOT = ROOT / ".help-center-preview-root"
# Must match the last segment of HELP_CENTER_BASE_PATH (no leading slash).
PREVIEW_SEGMENT = "evoto-help-center-site"


def preview_env() -> dict[str, str]:
    return {
        **os.environ,
        "HELP_CENTER_BASE_PATH": f"/{PREVIEW_SEGMENT}",
        "HELP_CENTER_SITE_ORIGIN": os.environ.get(
            "HELP_CENTER_SITE_ORIGIN", "https://federica-nube.github.io"
        ),
    }


def ensure_preview_symlink() -> Path:
    PREVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    link_path = PREVIEW_ROOT / PREVIEW_SEGMENT
    target_rel = os.path.relpath(OUTPUT_DIR.resolve(), PREVIEW_ROOT)
    if link_path.is_symlink() or link_path.exists():
        if link_path.is_symlink():
            try:
                if link_path.resolve() == OUTPUT_DIR.resolve():
                    return PREVIEW_ROOT
            except OSError:
                pass
        link_path.unlink()
    link_path.symlink_to(target_rel, target_is_directory=True)
    return PREVIEW_ROOT


def main() -> None:
    parser = argparse.ArgumentParser(description="Preview the generated Evoto help center locally.")
    parser.add_argument("--port", type=int, default=4173, help="Port to bind the preview server to.")
    parser.add_argument(
        "--skip-build",
        action="store_true",
        help="Serve the existing output directory without rebuilding first.",
    )
    args = parser.parse_args()

    if not args.skip_build or not OUTPUT_DIR.exists():
        subprocess.run(
            [sys.executable, str(BUILD_SCRIPT)],
            cwd=ROOT,
            check=True,
            env=preview_env(),
        )

    parent = ensure_preview_symlink()
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(parent))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", args.port), handler)
    print(
        f"Serving Evoto Help Center at http://127.0.0.1:{args.port}/{PREVIEW_SEGMENT}/\n"
        f"(matches HELP_CENTER_BASE_PATH=/{PREVIEW_SEGMENT})"
    )
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping preview server.")


if __name__ == "__main__":
    main()
