import json

data = json.load(open('banco_questoes_extraidas.json', 'r', encoding='utf-8'))
for q in data['questoes']:
    if q['id'] in ['TRT-2024-FGV-Q36', 'TRT-2024-FGV-Q37', 'TRT-2024-FGV-Q38', 'TRT-2024-FGV-Q39', 'TRT-2024-FGV-Q40', 'TRT-2024-FGV-Q41']:
        print("=" * 60)
        print(f"ID={q['id']} | GAB={q['gabarito_oficial']}")
        print(q['enunciado'])
        for k, v in sorted(q['alternativas'].items()):
            print(f"  {k}) {v}")

