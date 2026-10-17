import json
import re

with open("scratch/headings_summary.json", "r", encoding="utf-8") as f:
    files = json.load(f)

for item in files[:6]:
    fpath = item["path"]
    with open(fpath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    print("="*70)
    print("FILE:", item["filename"])
    current_sec = ""
    for idx, l in enumerate(lines):
        if l.startswith("## ") or l.startswith("### "):
            if l.startswith("### Questão"):
                print(f"  Line {idx+1}: {l.strip()} [UNDER {current_sec}]")
            else:
                current_sec = l.strip()
