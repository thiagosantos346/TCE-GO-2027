import os
import re

mod16_dir = "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/16_licitacoes_e_contratos_administrativos"
files = sorted([f for f in os.listdir(mod16_dir) if f.endswith(".md")])

for f in files:
    fpath = f"{mod16_dir}/{f}"
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
