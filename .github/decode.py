#!/usr/bin/env python3
import re, base64, pathlib, sys

src = pathlib.Path("src.all")
if not src.exists():
    print("ERROR: src.all not found")
    sys.exit(1)

text = src.read_text(encoding="utf-8", errors="replace")
pattern = r"===\s*FILE:\s*(\S+)\s*===\s*\n(.*?)\n===\s*END\s*==="
blocks = re.findall(pattern, text, re.S)
print("blocks:", len(blocks))

out = pathlib.Path("AmapClean")
out.mkdir(exist_ok=True)

for name, b64 in blocks:
    raw = b64.strip().replace("\n", "").replace("\r", "")
    data = base64.b64decode(raw)
    (out / name).write_bytes(data)
    print("  wrote %-20s %6d bytes" % (name, len(data)))

print("done")
