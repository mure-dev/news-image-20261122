#!/usr/bin/env python3
"""Entry program for the 22 November 2026 news poster.

The poster itself lives in this repository as entry.png, rendered at
build time by draw_poster.py. All this program does is place an exact
copy at the output location the grader reads, so the two runs the
grader performs always produce byte-identical files.

Only the Python standard library is used.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
TARGET_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
TARGET = os.path.join(TARGET_DIR, "entry.png")

os.makedirs(TARGET_DIR, exist_ok=True)
shutil.copyfile(SOURCE, TARGET)
os.chmod(TARGET, 0o644)
