"""One warm emoji, out for delivery.

The cargo is a single code point. The program drops it in the output
folder, picks it up again, and checks nobody swapped the parcel.
"""
import json
import os

FACE = "\U0001F917"
HUGS = 2


def drop(base):
    base = base or "output"
    os.makedirs(base, exist_ok=True)
    p = os.path.join(base, "entry.txt")
    open(p, "w", encoding="utf-8", newline="\n").write(FACE)
    back = open(p, encoding="utf-8").read().strip()
    assert back == FACE, "parcel swapped in transit"
    return back


w = drop(os.environ.get("MAKEFUN_OUTPUT_DIR"))
print(json.dumps({"who": "emo2", "wide": len(w), "hugs": HUGS, "sent": True}))
