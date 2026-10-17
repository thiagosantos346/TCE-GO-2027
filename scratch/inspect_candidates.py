import json
import os

with open("scratch/candidates_by_file.json", "r", encoding="utf-8") as f:
    data = json.load(f)

modules = [
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/15_nocoes_de_direito_administrativo",
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/16_licitacoes_e_contratos_administrativos",
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/17_nocoes_de_direito_constitucional",
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/18_nocoes_de_controle_externo"
]

for m in modules:
    print("\n" + "="*80)
    print(f"MODULE: {m}")
    for k, qs in sorted(data.items()):
        if k.startswith(m):
            print(f"\n--- FILE: {os.path.basename(k)} (Total candidates: {len(qs)}) ---")
            for idx, q in enumerate(qs[:3]):
                print(f"  [{idx+1}] {q.get('id')} | {q.get('banca')} {q.get('ano')} | {q.get('orgao')} | {q.get('cargo')}")
                print(f"      Enunciado: {q.get('enunciado', '').replace(chr(10), ' ')[:130]}...")
                print(f"      Gabarito: {q.get('gabarito_oficial')} | Alts: {list(q.get('alternativas', {}).keys())}")
