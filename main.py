"""Glyph courier: carries exactly one warm emoji to the output tray."""
import json
import os
from pathlib import Path


class Courier:
    tray_limit = 8

    def __init__(self, source="entry.txt"):
        self.source = source

    def pick_up(self):
        return Path(self.source).read_text(encoding="utf-8").strip()

    def inspect(self, glyph):
        if len(glyph) < 1:
            raise ValueError("the tray arrived empty")
        if len(glyph) > Courier.tray_limit:
            raise ValueError("glyph heavier than 8 characters")
        return glyph

    def place(self, glyph):
        tray = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
        tray.mkdir(parents=True, exist_ok=True)
        spot = tray / "entry.txt"
        spot.write_text(glyph + "\n", encoding="utf-8", newline="\n")
        return spot


if __name__ == "__main__":
    runner = Courier()
    glyph = runner.inspect(runner.pick_up())
    spot = runner.place(glyph)
    print(json.dumps({"ok": True, "spot": str(spot), "glyph": glyph,
                      "glyph_chars": len(glyph)}))
