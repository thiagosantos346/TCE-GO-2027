import json

data = json.load(open('banco_questoes_extraidas.json', 'r', encoding='utf-8'))
questoes_by_id = {q['id']: q for q in data['questoes']}

candidate_ids = [
    'TRT23-2016-FCC-Q01', # Teste 1: Compreensao
    'TRT3-2015-FCC-Q02',  # Teste 2: Generos / Analise
    'TRT-2024-FCC-Q05',   # Teste 3: Tipologia / Progressao
    'TRT1-2014-FCC-Q01',  # Teste 4: Argumentacao e Tese
    'TRT14-2016-FCC-Q03', # Teste 5: Pressupostos / Sentido
    'TRTDA24REGIO-2025-FGV-Q06', # Teste 6: Denotacao / Sentido Figurado
    'TRT3-2015-FCC-Q10',  # Teste 7: Discurso Direto e Indireto
    'TRT-2025-FGV-Q07',   # Teste 8: Transposicao de Discurso
    'TRT24-2017-FCC-Q04', # Teste 9: Reescreve preservando sentido (Parafrase)
    'TRTDA24REGIO-2025-FGV-Q10', # Teste 10: Figuras de Linguagem
    'TRT1-2014-FCC-Q02'   # Teste 11: Analise de sentido / Ironia / Expressao figurada
]

for qid in candidate_ids:
    q = questoes_by_id.get(qid)
    print("=" * 70)
    print(f"ID: {qid} | {q['banca']} - {q['orgao']} - {q['cargo']} - {q['ano']}")
    print("ENUNCIADO:")
    print(q['enunciado'])
    print("ALTERNATIVAS:")
    for k, v in sorted(q['alternativas'].items()):
        print(f"  {k}) {v}")
    print(f"GABARITO: {q['gabarito_oficial']}")

