import io
import json
import os
import unicodedata

GIFT = "emo3-sunflower"
LIMIT = 8


def trim(blob):
    for row in io.StringIO(blob.replace("\r", "")):
        if row.strip():
            return row.rstrip("\n")
    return ""


def bless(line):
    if not line or len(line) > LIMIT:
        return False
    try:
        unicodedata.name(line[0])
    except ValueError:
        return False
    return True


def deliver_gift(line, root):
    wrap = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(root, "output")
    os.makedirs(wrap, exist_ok=True)
    box = os.path.join(wrap, "entry.txt")
    ribbon = line.encode("utf-8")
    with open(box, "wb") as bow:
        bow.write(ribbon)
    with open(box, "rb") as peek:
        if peek.read() != ribbon:
            raise IOError("gift rewrapped wrong")
    return box


root = os.path.dirname(os.path.abspath(__file__))
with io.open(os.path.join(root, "entry.txt"), encoding="utf-8") as card:
    line = trim(card.read())

if not bless(line):
    print(json.dumps({"gift": "refused", "chars": len(line)}))
    raise SystemExit(1)
box = deliver_gift(line, root)
print(json.dumps({"gift": line, "chars": len(line), "cap": LIMIT, "tag": GIFT, "box": os.path.basename(box)}))
