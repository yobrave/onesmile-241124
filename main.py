"""Emoji greenhouse: waters the emoji, picks it, places it in the output vase."""
STAMP = "onebug-11251142-emo3"
import json
import os
import shutil
from pathlib import Path

PLOT = Path(__file__).resolve().parent
STEM_MAX = 8
BLOOM = "\U0001F33B"


def water():
    stem = PLOT / "entry.txt"
    petal = stem.read_text(encoding="utf-8").strip()
    grown = 1 <= len(petal) <= STEM_MAX
    bay = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if bay and grown:
        Path(bay).mkdir(parents=True, exist_ok=True)
        shutil.copyfile(stem, Path(bay) / "entry.txt")
    print(json.dumps({"grown": grown, "stamp": STAMP, "petals": len(petal), "stem_max": STEM_MAX}))


if __name__ == "__main__":
    water()
