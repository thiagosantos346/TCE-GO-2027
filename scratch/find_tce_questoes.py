import json

data = json.load(open('banco_questoes_extraidas.json', 'r', encoding='utf-8'))
questoes = data['questoes']

tce_questoes = [q for q in questoes if 'TCE' in q['enunciado'] or 'TRIBUNAL DE CONTAS' in q['enunciado'] or 'TCE' in q.get('orgao', '')]

print(f"Total de questões de TCE identificadas no texto: {len(tce_questoes)}")
for q in tce_questoes[:10]:
    print(f"ID={q['id']} | Num={q['numero_original']} | {q['banca']} {q['ano']} | Enunciado: {q['enunciado'][:120].strip().replace(chr(10), ' ')}")

