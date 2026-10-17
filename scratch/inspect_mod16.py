import os
import re

mod16_dir = "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/16_licitacoes_e_contratos_administrativos"
files = sorted([f for f in os.listdir(mod16_dir) if f.endswith(".md")])

for f in files:
    fpath = f"{mod16_dir}/{f}"
    with open(fpath, "r", encoding="utf-8") as fl:
        text = fl.read()
    
    qs = re.findall(r"### Questão (\d+)", text)
    headings = [l.strip() for l in text.splitlines() if l.startswith("## ") or (l.startswith("### ") and not l.startswith("### Questão"))]
    print("="*70)
    print(f"FILE: {f} | Existing Questions: {qs}")
    for h in headings[:12]:
        print("  *", h)
