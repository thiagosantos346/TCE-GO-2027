import json

data = json.load(open('banco_questoes_extraidas.json', 'r', encoding='utf-8'))
questoes_dict = {q['id']: q for q in data['questoes']}

ids = [
    'TRT14-2016-FCC-Q06', # Teste 042: Concordância Verbal
    'TRT1-2014-FCC-Q20',  # Teste 043: Concordância Verbal
    'TJAP-2023-FGV-Q24',  # Teste 044: Dupla Concordância Nominal
    'TRT24-2017-FCC-Q05', # Teste 045: Concordância Padrão
    'TRT15-2015-FCC-Q06', # Teste 046: Mesma Regência Verbal
    'TRT9-2015-FCC-Q04',  # Teste 047: Justificativa da Flexão Verbal
    'TRT2-2014-FCC-Q05',  # Teste 048: Flexão Verbal e Sujeito
    'TRT23-2016-FCC-Q14', # Teste 049: Regência e Preposição em Lacunas
    'TRT-2024-FGV-Q09',   # Teste 050: Crase Proibida vs Permitida
    'TRT-2009-FCC-Q20'    # Teste 051: Concordância Verbal e Regência
]

for qid in ids:
    q = questoes_dict.get(qid)
    print("=" * 60)
    print(f"ID: {qid} | {q['banca']} - {q['orgao']} - {q['cargo']} - {q['ano']}")
    print(q['enunciado'][:160].replace(chr(10), ' '))
    print(f"GAB: {q['gabarito_oficial']}")

