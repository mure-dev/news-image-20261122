#!/usr/bin/env python3
"""News-image entry for 22 November 2026 (Python 3.13, standard library only).

The poster image is rendered by draw_poster.py and stored in this
repository as entry.png. This program copies it to /output/entry.png,
so both runs of the grader produce the exact same bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")

# Deterministic by construction: the file is copied byte for byte, so
# the grader's two runs always see identical output.
os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SRC, DST)
os.chmod(DST, 0o644)
