"""news-image-20261127: write the day's news image to the output directory.

Standard library only. The image is shipped in this repository as entry.png
(a 1024x1024 PNG drawn from the public reporting of Friday 27 November 2026)
and is copied byte for byte to /output/entry.png, or to
$MAKEFUN_OUTPUT_DIR/entry.png when that is set. No network is used.
A plain copy is deterministic: every run writes the same bytes.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT, exist_ok=True)
shutil.copyfile(
    os.path.join(HERE, "entry.png"),
    os.path.join(OUT, "entry.png"),
)
