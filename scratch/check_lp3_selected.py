import json

data = json.load(open('banco_questoes_extraidas.json', 'r', encoding='utf-8'))
questoes_dict = {q['id']: q for q in data['questoes']}

ids = [
    'TRT-2024-FGV-Q06',   # Teste 022: Troca indevida O vs LHE
    'TRT1-2014-FCC-Q14',  # Teste 023: Onde e Em Cujo (Pronomes Relativos com preposição)
    'TRT-2009-FCC-Q17',   # Teste 024: Emprego de elemento/pronome relativo com preposição
    'TRT1-2014-FCC-Q05',  # Teste 025: Dissesse alguém isso hoje / Correlação e colocação
    'TRT16-2014-FCC-Q08', # Teste 026: Correlação entre tempos e modos verbais
    'TRT1-2014-FCC-Q18',  # Teste 027: Formas verbais adequadamente empregadas e flexionadas
    'TRT24-2017-FCC-Q01', # Teste 028: Construção que admite transposição para voz passiva
    'TRT1-2014-FCC-Q07',  # Teste 029: Transpondo-se para a voz passiva o segmento
    'TRT14-2016-FCC-Q08', # Teste 030: Transposição voz ativa para passiva
    'TRT2-2014-FCC-Q12'   # Teste 031: Correspondência de tempo verbal na voz passiva
]

for qid in ids:
    q = questoes_dict.get(qid)
    print("=" * 60)
    print(f"ID: {qid} | {q['banca']} - {q['orgao']} - {q['cargo']} - {q['ano']}")
    print(q['enunciado'][:180].replace(chr(10), ' '))
    print(f"GAB: {q['gabarito_oficial']}")

