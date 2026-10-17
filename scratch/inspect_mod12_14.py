import json
import os

with open("scratch/candidates_by_file.json", "r", encoding="utf-8") as f:
    data = json.load(f)

modules = [
    "fontes_de_estudo/conhecimentos_especificos_b02_ti/12_governanca_de_ti",
    "fontes_de_estudo/conhecimentos_especificos_b02_ti/13_legislacao_aplicada_a_ti",
    "fontes_de_estudo/conhecimentos_especificos_b02_ti/14_lingua_inglesa_leitura_tecnica"
]

for m in modules:
    print("\n" + "="*80)
    print(f"MODULE: {m}")
    for k, qs in sorted(data.items()):
        if k.startswith(m):
            print(f"\n--- FILE: {os.path.basename(k)} (Total candidates: {len(qs)}) ---")
            for idx, q in enumerate(qs):
                print(f"  [{idx}] {q.get('id')} | {q.get('banca')} {q.get('ano')} | {q.get('orgao')} | Sec: {q.get('target_section')}")
                enunc = q.get('enunciado', '').replace('\n', ' ')[:100]
                print(f"      {enunc}...")
                print(f"      Gab: {q.get('gabarito_oficial')}")
