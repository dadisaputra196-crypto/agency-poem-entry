# Poem: "The Second Glance" — about agency, not permission.
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
DST = "/output/entry.txt"
FALLBACK = "/tmp/entry.txt"

target = DST
try:
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    open(DST, "a").close()
except OSError:
    target = FALLBACK
    os.makedirs(os.path.dirname(FALLBACK), exist_ok=True)

shutil.copyfile(SRC, target)
print(f"Copied {SRC} -> {target}")
