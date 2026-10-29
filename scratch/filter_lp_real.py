import json

data = json.load(open('banco_questoes_extraidas.json', 'r', encoding='utf-8'))
questoes = [q for q in data['questoes'] if q.get('status_integracao') == 'pendente']

# filtrar questoes que contenham termos especificos de lingua portuguesa e nao sejam TI
ti_words = ['tcp', 'ip', 'udp', 'sql', 'linux', 'windows', 'código', 'tabela', 'servidor', 'software', 'hardware', 'cpu', 'memória', 'dado', 'rede', 'protocolo', 'classe', 'java', 'python', 'html', 'css', 'javascript', 'pat', 'nat', 'osi', 'contábil', 'patrimônio', 'balanço', 'ativo', 'passivo']

lp_real = []
for q in questoes:
    enunc = q['enunciado'].lower()
    alts = ' '.join(q['alternativas'].values()).lower()
    full = enunc + ' ' + alts
    if q.get('numero_original', 99) <= 20:
        # checar se nao tem ti words no enunciado
        if not any(w in enunc for w in ['protocolo', 'ip', 'roteador', 'sql', 'servidor', 'software', 'java', 'html', 'patrimônio', 'contábil', 'balanço', 'tabela']):
            lp_real.append(q)

print(f"Total de questões reais de Língua Portuguesa identificadas: {len(lp_real)}")

# Amostra de questões com enunciados e alternativas
for q in lp_real[:10]:
    print(f"ID={q['id']} | Num={q['numero_original']} | {q['banca']} {q['ano']} | Enunciado: {q['enunciado'][:100].strip().replace(chr(10), ' ')}")

