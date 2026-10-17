import os
import re

mod18_dir = "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/18_nocoes_de_controle_externo"
files = sorted([f for f in os.listdir(mod18_dir) if f.endswith(".md")])

for f in files:
    fpath = f"{mod18_dir}/{f}"
    with open(fpath, "r", encoding="utf-8") as fl:
        lines = fl.readlines()
    print("="*70)
    print("FILE:", f)
    curr = ""
    for idx, l in enumerate(lines):
        if l.startswith("## ") or l.startswith("### "):
            if l.startswith("### Questão"):
                print(f"  Line {idx+1}: {l.strip()} [UNDER {curr}]")
            else:
                curr = l.strip()
