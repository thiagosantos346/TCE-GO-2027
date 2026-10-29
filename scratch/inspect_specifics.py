import json

data = json.load(open('banco_questoes_extraidas.json', 'r', encoding='utf-8'))
questoes_dict = {q['id']: q for q in data['questoes']}

for qid in ['TJBA-2015-FGV-Q05', 'TJRR-2024-FGV-Q06', 'TRT-2009-FCC-Q17', 'TRT-2024-FGV-Q01', 'TRT-2024-FGV-Q05', 'TRT-2024-FGV-Q07']:
    q = questoes_dict.get(qid)
    print("=" * 60)
    print(f"ID: {qid} | {q['banca']} - {q['orgao']} - {q['cargo']} - {q['ano']}")
    print(q['enunciado'])
    for k, v in sorted(q['alternativas'].items()):
        print(f"  {k}) {v}")
    print(f"GAB: {q['gabarito_oficial']}")

