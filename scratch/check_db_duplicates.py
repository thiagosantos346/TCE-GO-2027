import json

with open('banco_questoes_extraidas.json', 'r', encoding='utf-8') as f:
    questoes = json.load(f).get('questoes', [])

unique_ids = set()
duplicates = 0
for q in questoes:
    qid = q.get('id')
    if qid in unique_ids:
        duplicates += 1
    else:
        unique_ids.add(qid)

print(f"Total registros no JSON: {len(questoes)}")
print(f"IDs únicos: {len(unique_ids)}")
print(f"Duplicatas de ID: {duplicates}")

# Provas representadas
provas = set()
for q in questoes:
    provas.add((q.get('banca'), q.get('orgao'), q.get('ano'), q.get('cargo')))

print(f"Total de provas/cargos distintos: {len(provas)}")
for p in sorted(list(provas))[:15]:
    print("  ", p)

