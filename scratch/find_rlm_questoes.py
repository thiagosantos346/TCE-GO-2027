import json

data = json.load(open('banco_questoes_extraidas.json', 'r', encoding='utf-8'))
questoes = [q for q in data['questoes'] if q.get('status_integracao') == 'pendente']

rlm_kws = ['silogismo', 'premissa', 'conclusão', 'tabela-verdade', 'tautologia', 'equivalência', 'negação', 'proposição', 'probabilidade', 'combinações', 'arranjo', 'anagrama', 'porcentagem', 'regra de três', 'fração', 'verdadeiro', 'falso', 'se joão', 'se então', 'todos os', 'algum', 'nenhum']

rlm_matches = []
for q in questoes:
    text = (q['enunciado'] + ' ' + ' '.join(q['alternativas'].values())).lower()
    if any(k in text for k in rlm_kws):
        # descartar questoes tipicas de programacao ou direito
        if not any(w in text for w in ['sql', 'tabela do banco', 'servidor', 'tcp', 'ip', 'constituição', 'artigo', 'servidor público', 'probidade']):
            rlm_matches.append(q)

print(f"Total de questões de RLM encontradas no banco: {len(rlm_matches)}")
for q in rlm_matches[:10]:
    print(f"ID={q['id']} | Num={q['numero_original']} | {q['banca']} {q['ano']} | Enunciado: {q['enunciado'][:100].strip().replace(chr(10), ' ')}")

