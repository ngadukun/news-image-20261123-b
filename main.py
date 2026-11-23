#!/usr/bin/env python3
"""news-image-20261123 entry: THE WORLD TODAY, Monday 23 November 2026.

The front page is rendered by render.py and held in this repository as
entry.png. This program copies those exact bytes to /output/entry.png.
It uses only the Python standard library, needs no network, and writes
the same bytes on every run.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil
from pathlib import Path


def main() -> None:
    src = Path(__file__).resolve().parent / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out_dir / "entry.png")


if __name__ == "__main__":
    main()
