import json

data = json.load(open('banco_questoes_extraidas.json', 'r', encoding='utf-8'))
questoes = [q for q in data['questoes'] if q.get('status_integracao') == 'pendente']

kws = ['acento', 'acentuação', 'ortografia', 'grafia', 'hífen', 'parassintética', 'sufixo', 'prefixo', 'derivação', 'grafadas', 'oxítona', 'paroxítona', 'proparoxítona']

matches = []
seen_texts = set()
for q in questoes:
    text = (q['enunciado'] + ' ' + ' '.join(q['alternativas'].values())).lower()
    if any(k in text for k in kws):
        # deduplicar
        sample = q['enunciado'][:60]
        if sample not in seen_texts:
            seen_texts.add(sample)
            matches.append(q)

print(f"Total encontradas no banco sobre ortografia/acentuação: {len(matches)}")
for q in matches[:15]:
    print(f"ID={q['id']} | {q['banca']} {q['ano']} | Enunciado: {q['enunciado'][:100].strip()}...")

