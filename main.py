import os

ENTRY = "1 star. Moon showed up late, half-lit, and still dragged the whole ocean around like it owned it."

assert 1 <= len(ENTRY) <= 120, "entry must be 1-120 characters"
assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
