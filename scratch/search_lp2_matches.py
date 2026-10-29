import json

data = json.load(open('banco_questoes_extraidas.json', 'r', encoding='utf-8'))
questoes = [q for q in data['questoes'] if q.get('status_integracao') == 'pendente']

# filtrar apenas questoes com numero original <= 25 (area de linguagens/conhecimentos gerais)
# e sem termos de computacao/ti/contabilidade
ti_blacklist = ['tcp', 'ip', 'udp', 'sql', 'linux', 'windows', 'código', 'tabela', 'servidor', 'software', 'hardware', 'cpu', 'memória', 'rede', 'protocolo', 'java', 'python', 'html', 'css', 'javascript', 'contábil', 'patrimônio', 'balanço']

def is_clean_portuguese(q):
    if q.get('numero_original', 99) > 25:
        return False
    enunc = q['enunciado'].lower()
    if any(w in enunc for w in ti_blacklist):
        return False
    return True

lp_clean = [q for q in questoes if is_clean_portuguese(q)]

def search_best(kws):
    res = []
    for q in lp_clean:
        text = (q['enunciado'] + ' ' + ' '.join(q['alternativas'].values())).lower()
        score = sum(1 for w in kws if w in text)
        if score > 0:
            res.append((score, q))
    res.sort(key=lambda x: (x[0], 0 if x[1]['banca'] == 'FCC' else 1, -x[1]['ano']), reverse=True)
    return [q for score, q in res]

targets = [
    ("Teste 012 (Acentuação geral)", ['mesma regra de acentuação', 'acentuam-se', 'acento gráfico', 'proparoxítona', 'paroxítona']),
    ("Teste 013 (Acentuação especial / Hiatos / Diferencial)", ['acento diferencial', 'hiato', 'ditongo aberto', 'têm', 'pôde', 'vem']),
    ("Teste 014 (Hífen e prefixos)", ['hífen', 'acordo ortográfico', 'prefixo', 'auto-']),
    ("Teste 015 (Grafia e Ortografia)", ['grafia correta', 'grafadas corretamente', 'escrita correta', 'ortografia']),
    ("Teste 016 (Semântica / Substituição de termos)", ['substituído pelo que', 'sentido de um segmento', 'mesmo sentido', 'troca de posição']),
    ("Teste 017 (Emprego de palavras / Parônimos / Homônimos)", ['elemento sublinhado', 'emprego do elemento', 'palavra sublinhada', 'termo sublinhado', 'cerca de']),
    ("Teste 018 (Mesma regra gramatical / Morfologia)", ['mesma regra', 'regra gramatical', 'paralelismo sintático', 'valor do adjetivo']),
    ("Teste 019 (Processos de formação / Derivação)", ['processo de formação', 'derivação', 'formação de palavras', 'sufixo', 'prefixo']),
    ("Teste 020 (Derivação regressiva / Classes de palavras)", ['oração reduzida', 'desenvolvida', 'forma negativa', 'reduzida para']),
    ("Teste 021 (Formação e relações lexicais)", ['adjetivo', 'qualidade', 'característica', 'estado', 'relação', 'celso cunha'])
]

for title, kws in targets:
    matches = search_best(kws)
    print("=" * 60)
    print(f"{title} -> Total encontradas: {len(matches)}")
    if matches:
        top = matches[0]
        print(f"Top: ID={top['id']} | {top['banca']} {top['ano']} | Num={top['numero_original']}")
        print(f"Enunciado: {top['enunciado'][:120].strip().replace(chr(10), ' ')}")
        print(f"Gabarito: {top['gabarito_oficial']}")

