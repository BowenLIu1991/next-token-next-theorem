"""Token count measurements for the talk.

Run:
    ./.venv/bin/python assets/demos/token_count.py
"""

import tiktoken

SAMPLES = {
    "english": "Celestial mechanics is the poetry of orbits.",
    "chinese": "天体力学是研究天体运动的学科。",
    "mixed": "三体问题 is a classic problem in celestial mechanics.",
    "code": "def f(x):\n    return x**2\n",
    "numbers": "1234567890",
    "formula": "x'' + 2y' = dΩ/dx",
}

ENCODINGS = ["o200k_base", "cl100k_base", "gpt2"]

rows = []
for name, text in SAMPLES.items():
    row = {"sample": name, "chars": len(text)}
    for enc_name in ENCODINGS:
        enc = tiktoken.get_encoding(enc_name)
        ids = enc.encode(text)
        row[enc_name] = len(ids)
    rows.append(row)

header = ["sample", "chars"] + ENCODINGS
print("| " + " | ".join(header) + " |")
print("|" + "|".join(["---"] * len(header)) + "|")
for r in rows:
    print("| " + " | ".join(str(r[h]) for h in header) + " |")

print()
for name, text in SAMPLES.items():
    enc = tiktoken.get_encoding("o200k_base")
    ids = enc.encode(text)
    pieces = [enc.decode_single_token_bytes(i).decode("utf-8", errors="replace") for i in ids]
    print(f"{name}: {pieces}")
