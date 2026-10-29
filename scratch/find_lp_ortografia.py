import json

data = json.load(open('banco_questoes_extraidas.json', 'r', encoding='utf-8'))
questoes = [q for q in data['questoes'] if q.get('status_integracao') == 'pendente' and q.get('numero_original', 99) <= 25]

kws = ['acento', 'acentua', 'ortograf', 'grafia', 'hífen', 'parassintét', 'sufixo', 'prefixo', 'derivação', 'grafad', 'oxítona', 'paroxítona', 'proparoxítona', 'sublinhad', 'palavra']

matches = []
seen_texts = set()
for q in questoes:
    text = (q['enunciado'] + ' ' + ' '.join(q['alternativas'].values())).lower()
    if any(k in text for k in kws):
        sample = q['enunciado'][:60]
        if sample not in seen_texts:
            seen_texts.add(sample)
            matches.append(q)

print(f"Total encontradas em Língua Portuguesa: {len(matches)}")
for q in matches[:20]:
    print(f"ID={q['id']} | Num={q['numero_original']} | {q['banca']} {q['ano']} | {q['enunciado'][:100].strip().replace(chr(10), ' ')}")

