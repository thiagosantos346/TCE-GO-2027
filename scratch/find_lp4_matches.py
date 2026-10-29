import json

data = json.load(open('banco_questoes_extraidas.json', 'r', encoding='utf-8'))
questoes = [q for q in data['questoes'] if q.get('status_integracao') == 'pendente']

ti_blacklist = ['tcp', 'ip', 'udp', 'sql', 'linux', 'windows', 'código', 'tabela', 'servidor', 'software', 'hardware', 'cpu', 'memória', 'rede', 'protocolo', 'java', 'python', 'html', 'css', 'javascript', 'contábil', 'patrimônio', 'balanço']

lp_clean = [q for q in questoes if q.get('numero_original', 99) <= 25 and not any(w in q['enunciado'].lower() for w in ti_blacklist)]

topics = [
    ("Teste 032: Coordenação e Oposição / Conjunção OU / Adversativas", ['conjunção ou', 'oração adversativa', 'conjunção', 'adversativa']),
    ("Teste 033: Orações Substantivas e Função Sintática", ['oração substantiva', 'função sintática', 'sujeito', 'objeto direto']),
    ("Teste 034: Causa e Efeito / Causa e Consequência", ['causa e efeito', 'relação de causa', 'indicativo de causa']),
    ("Teste 035: Concessão e Oposição", ['concessão', 'concessiva', 'embora', 'apesar de', 'ao passo que']),
    ("Teste 036: Conectivos / Oração Subordinada", ['sentido da oração', 'conectivo', 'circunstância restritiva', 'circunstância']),
    ("Teste 037: Oração Adjetiva Restritiva vs Explicativa", ['circunstância restritiva', 'restritiva', 'explicativa', 'sentido restritivo']),
    ("Teste 038: Valores do 'COMO'", ['como', 'valor de como', 'causal', 'comparativo', 'conformativo']),
    ("Teste 039: Pontuação na Norma Culta", ['pontuação está plenamente adequada', 'pontuação correta', 'pontuação']),
    ("Teste 040: Emprego da Vírgula", ['vírgula', 'vírgulas', 'pontuação plenamente']),
    ("Teste 041: Correção Estrutural e Pontuação", ['falha estrutural', 'está correta a pontuação', 'redação deste livre comentário'])
]

for title, kws in topics:
    matches = []
    for q in lp_clean:
        text = (q['enunciado'] + ' ' + ' '.join(q['alternativas'].values())).lower()
        if any(w in text for w in kws):
            matches.append(q)
    matches.sort(key=lambda q: (0 if q['banca'] == 'FCC' else 1, -q['ano']))
    print("=" * 60)
    print(f"{title} -> Total: {len(matches)}")
    if matches:
        m = matches[0]
        print(f"Top: ID={m['id']} | {m['banca']} {m['ano']} | Num={m['numero_original']}")
        print(f"Enunciado: {m['enunciado'][:120].strip().replace(chr(10), ' ')}...")
        print(f"GAB: {m['gabarito_oficial']}")

