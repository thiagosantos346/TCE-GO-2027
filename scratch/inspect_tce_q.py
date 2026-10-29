import json
with open('banco_questoes_extraidas.json', 'r', encoding='utf-8') as f:
    questoes = json.load(f).get('questoes', [])

for q in questoes:
    if q.get('id') == 'TRT-2024-FGV-Q24':
        print(q)
        break

