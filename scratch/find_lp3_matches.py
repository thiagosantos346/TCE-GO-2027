import json

data = json.load(open('banco_questoes_extraidas.json', 'r', encoding='utf-8'))
questoes = [q for q in data['questoes'] if q.get('status_integracao') == 'pendente']

ti_blacklist = ['tcp', 'ip', 'udp', 'sql', 'linux', 'windows', 'código', 'tabela', 'servidor', 'software', 'hardware', 'cpu', 'memória', 'rede', 'protocolo', 'java', 'python', 'html', 'css', 'javascript', 'contábil', 'patrimônio', 'balanço']

lp_clean = [q for q in questoes if q.get('numero_original', 99) <= 25 and not any(w in q['enunciado'].lower() for w in ti_blacklist)]

topics = [
    ("Teste 022: Pronomes Oblíquos (O vs LHE)", ['o/lhe', 'lhe', 'substituição do termo sublinhado pelo pronome', 'emprego do pronome']),
    ("Teste 023: Pronomes Relativos com Preposição", ['onde e em cujo', 'cujo', 'em que', 'pronome relativo', 'preposição']),
    ("Teste 024: Substituição Pronominal Enclítica", ['substitui o elemento sublinhado', 'substituição do termo grifado', 'pronome correspondente']),
    ("Teste 025: Colocação Pronominal (Próclise / Ênclise)", ['colocação pronominal', 'próclise', 'ênclise', 'posição do pronome']),
    ("Teste 026: Correlação entre Tempos e Modos Verbais", ['correlação entre os tempos', 'tempos e modos verbais', 'articulação entre os tempos']),
    ("Teste 027: Flexão Verbal e Verbos Irregulares", ['formas verbais estão', 'flexão verbal', 'verbo indicado entre parênteses']),
    ("Teste 028: Voz Passiva (Admissibilidade)", ['admite transposição para a voz passiva', 'pode ser reescrita com o verbo na voz passiva', 'voz passiva']),
    ("Teste 029: Transposição para a Voz Passiva", ['transpondo-se para a voz passiva', 'transposição para a voz passiva', 'passando para a voz passiva']),
    ("Teste 030: Partícula SE e Voz Apassivadora", ['partícula se', 'pronome se', 'apassivador', 'indeterminação do sujeito']),
    ("Teste 031: Correlação Verbal / Consecutio Temporum", ['correlação verbal', 'tempos verbais', 'tempo verbal'])
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
        print(f"Gabarito: {m['gabarito_oficial']}")

