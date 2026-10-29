import json

with open('banco_questoes_extraidas.json', 'r', encoding='utf-8') as f:
    questoes = json.load(f).get('questoes', [])

# Checar quantas questões são da prova de TI do TCE-GO FGV 2024
tce_go_ti = [q for q in questoes if 'tce' in str(q.get('orgao')).lower() or 'goiás' in str(q.get('enunciado')).lower()]
print(f"Total questoes com mencao a TCE ou Goiás no banco: {len(tce_go_ti)}")

# Provas catalogadas no banco
cargos = {}
for q in questoes:
    k = (q.get('banca'), q.get('orgao'), q.get('ano'), q.get('cargo'))
    cargos[k] = cargos.get(k, 0) + 1

for k, c in sorted(cargos.items(), key=lambda x: x[1], reverse=True):
    print(f"  {c:3d} questoes -> {k}")

