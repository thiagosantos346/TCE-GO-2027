import json

data = json.load(open('banco_questoes_extraidas.json', 'r', encoding='utf-8'))
lp_questoes = [q for q in data['questoes'] if q.get('status_integracao') == 'pendente' and q.get('numero_original', 99) <= 20]

print(f"Total de questões de Língua Portuguesa no banco: {len(lp_questoes)}")

# Vamos listar todas as questões de Língua Portuguesa que contenham palavras-chave de ortografia, acentuação, morfologia, vocabulário
for q in lp_questoes:
    text = (q['enunciado'] + ' ' + ' '.join(q['alternativas'].values())).lower()
    if any(k in text for k in ['acento', 'acentu', 'ortograf', 'grafia', 'hífen', 'deriva', 'formação', 'prefix', 'sufix', 'sentido', 'significa', 'substitui', 'vocábulo', 'palavra']):
        print(f"ID={q['id']} | Num={q['numero_original']} | {q['banca']} {q['ano']} | Enunciado: {q['enunciado'][:90].strip().replace(chr(10), ' ')}")

