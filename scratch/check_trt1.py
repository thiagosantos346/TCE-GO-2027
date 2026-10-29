import json

data = json.load(open('banco_questoes_extraidas.json', 'r', encoding='utf-8'))
for q in data['questoes']:
    if 'TRT1-2014-FCC' in q['id']:
        print(q['id'], q['enunciado'][:100].replace('\n', ' '))

