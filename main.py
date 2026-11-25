"""emo6: single glyph desk. Codepoints are counted one friendly face at a time."""
import json
import os
import sys
from pathlib import Path

FACE = 8


def glyphs(raw: str) -> int:
    return len([ch for ch in raw.strip() if not ch.isspace()])


def main():
    raw = Path(__file__).resolve().parent.joinpath("entry.txt").read_text(encoding="utf-8")
    bare = raw.strip()
    faces = glyphs(bare)
    warm = 1 <= faces and len(bare) <= FACE and not bare.isspace()
    if warm:
        sun = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
        sun.mkdir(parents=True, exist_ok=True)
        (sun / "entry.txt").write_bytes(bare.encode("utf-8"))
    print("VERDICT", json.dumps({"desk": "emo6-glyph-r11251422", "faces": faces, "chars": len(bare), "cap": FACE, "warm": warm}))
    return 0 if warm else 1


if __name__ == "__main__":
    sys.exit(main())
