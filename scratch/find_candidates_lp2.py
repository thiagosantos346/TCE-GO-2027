import json

data = json.load(open('banco_questoes_extraidas.json', 'r', encoding='utf-8'))
questoes = [q for q in data['questoes'] if q.get('status_integracao') == 'pendente']

topics = [
    ("Teste 012: Acentuação Gráfica Geral (Proparoxítonas, Paroxítonas, Oxítonas)", ['acentuam-se', 'mesma regra de acentuação', 'justifica o acento', 'acento gráfico', 'proparoxítona', 'paroxítona']),
    ("Teste 013: Regras Especiais de Acentuação (Hiato, Ditongo, Acento Diferencial)", ['hiato', 'ditongo aberto', 'acento diferencial', 'pôde', 'têm', 'veem']),
    ("Teste 014: Emprego do Hífen", ['hífen', 'uso do hífen', 'grafada com hífen', 'acordo ortográfico']),
    ("Teste 015: Ortografia Oficial / Grafia de Palavras", ['grafadas corretamente', 'ortografia correta', 'grafia correta', 'escrita corretamente']),
    ("Teste 016: Semântica Lexical / Sentido e Substituição de Vocábulos", ['substituído pelo que se encontra', 'sentido de um segmento', 'vocábulo sublinhado', 'mesmo sentido']),
    ("Teste 017: Parônimos / Homônimos / Emprego de Palavras", ['elemento sublinhado', 'emprego do elemento', 'palavra sublinhada', 'termo sublinhado']),
    ("Teste 018: Estrutura da Palavra / Sufixos e Prefixos", ['sufixo', 'prefixo', 'valor semântico do prefixo', 'elemento de composição', 'formação de palavra']),
    ("Teste 019: Processos de Formação (Derivação)", ['processo de formação', 'derivação parassintética', 'derivação imprópria', 'derivação regressiva']),
    ("Teste 020: Composição de Palavras (Justaposição / Aglutinação)", ['composição por', 'justaposição', 'aglutinação', 'formada pelo processo']),
    ("Teste 021: Vocabulário e Relações Morfológicas", ['classe gramatical', 'adjetivo', 'substantivo', 'formação vocabular', 'valor do adjetivo'])
]

for title, kws in topics:
    matches = []
    for q in questoes:
        if q.get('numero_original', 99) <= 30: # focar em questoes de linguagens
            text = (q['enunciado'] + ' ' + ' '.join(q['alternativas'].values())).lower()
            if any(k in text for k in kws):
                matches.append(q)
    matches.sort(key=lambda q: (0 if q['banca'] == 'FCC' else 1, -q['ano']))
    print(f"\n{title} -> Total encontradas: {len(matches)}")
    if matches:
        m = matches[0]
        print(f"  Top: ID={m['id']} | {m['banca']} {m['ano']} | Num={m['numero_original']}")
        print(f"  Enunciado: {m['enunciado'][:120].strip().replace(chr(10), ' ')}...")
        print(f"  Gabarito: {m['gabarito_oficial']}")

