import json

with open("scratch/candidates_by_file.json", "r", encoding="utf-8") as f:
    cand_by_file = json.load(f)

fkey_01 = "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/15_nocoes_de_direito_administrativo/01_regime_juridico_principios_e_lindb.md"
qs = cand_by_file.get(fkey_01, [])

target_ids = ["TRT-2024-FGV-Q29", "TRT9-2015-FCC-Q26", "TRT1-2024-FGV-Q45", "TJMT-2024-FGV-Q33", "TRT-2024-FGV-Q70"]

seen = set()
for q in qs:
    qid = q.get("id")
    if qid in target_ids and qid not in seen:
        seen.add(qid)
        print("="*70)
        print(f"ID: {qid} | Banca: {q.get('banca')} {q.get('ano')} | Gabarito: {q.get('gabarito_oficial')}")
        print("ENUNCIADO:")
        print(q.get("enunciado"))
        print("\nALTERNATIVAS:")
        for k, v in sorted(q.get("alternativas", {}).items()):
            print(f"  {k}) {v}")
