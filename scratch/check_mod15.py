import json
import os

with open("scratch/candidates_by_file.json", "r", encoding="utf-8") as f:
    data = json.load(f)

mod15 = "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/15_nocoes_de_direito_administrativo"
files = sorted([f for f in os.listdir(mod15) if f.endswith(".md")])

for f in files:
    full_path = f"{mod15}/{f}"
    candidates = data.get(full_path, [])
    # deduplicate by enunciado prefix
    seen = set()
    unique_candidates = []
    for c in candidates:
        en = c.get("enunciado", "").strip()[:80]
        if en and en not in seen:
            seen.add(en)
            unique_candidates.append(c)
    
    print("="*70)
    print(f"FILE: {f} | Total raw: {len(candidates)} | Unique: {len(unique_candidates)}")
    for i, c in enumerate(unique_candidates[:8]):
        b = c.get("banca")
        y = c.get("ano")
        org = c.get("orgao")
        cid = c.get("id")
        gab = c.get("gabarito_oficial")
        en = c.get("enunciado", "").replace("\n", " ")[:100]
        print(f"  ({i+1}) [{cid}] {b} {y} {org} | Gab: {gab} | {en}")
