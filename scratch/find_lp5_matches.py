import json

data = json.load(open('banco_questoes_extraidas.json', 'r', encoding='utf-8'))
questoes = [q for q in data['questoes'] if q.get('status_integracao') == 'pendente']

ti_blacklist = ['tcp', 'ip', 'udp', 'sql', 'linux', 'windows', 'código', 'tabela', 'servidor', 'software', 'hardware', 'cpu', 'memória', 'rede', 'protocolo', 'java', 'python', 'html', 'css', 'javascript', 'contábil', 'patrimônio', 'balanço']

lp_clean = [q for q in questoes if q.get('numero_original', 99) <= 25 and not any(w in q['enunciado'].lower() for w in ti_blacklist)]

topics = [
    ("Teste 042: Concordância Verbal", ['concordância verbal', 'concordância verbal estão', 'normas de concordância verbal']),
    ("Teste 043: Concordância Verbal / Sujeito / Verbos", ['concordância verbal', 'verbo deverá flexionar-se', 'flexão verbal sublinhada']),
    ("Teste 044: Concordância Nominal (Dupla Concordância / Regras)", ['dupla concordância nominal', 'concordância nominal', 'palavra sublinhada']),
    ("Teste 045: Concordância Padrão", ['quanto à concordância padrão', 'concordância padrão', 'concordância']),
    ("Teste 046: Regência Verbal", ['regência verbal', 'regência', 'substituição de uma oração']),
    ("Teste 047: Regência e Preposição", ['preposição', 'exigida pelo verbo', 'regência do verbo']),
    ("Teste 048: Regência e Lacunas", ['preenchem corretamente', 'na ordem dada', 'lacunas']),
    ("Teste 049: Crase (Casos Gerais e Proibidos)", ['acento grave indicativo da crase', 'acento grave', 'crase']),
    ("Teste 050: Crase (Casos Específicos)", ['sinal indicativo de crase', 'indicativo da crase', 'crase']),
    ("Teste 051: Crase e Regência", ['crase num contexto', 'utilização do acento grave', 'crase está'])
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

