import json

data = json.load(open('banco_questoes_extraidas.json', 'r', encoding='utf-8'))
for q in data['questoes']:
    if q['id'] in ['TRT1-2014-FCC-Q34', 'TRT14-2016-FCC-Q39', 'TRT23-2016-FCC-Q35', 'TRT23-2016-FCC-Q39', 'TRT6-2012-FCC-Q35', 'TRT9-2015-FCC-Q32', 'TJAP-2023-FGV-Q53', 'TRT13-2014-FCC-Q33']:
        if len(q.get('alternativas', {})) == 5:
            print('='*50)
            print(q['id'], q['banca'], q['ano'])
            print(q['enunciado'][:120].replace('\n', ' '))
            print('GAB:', q['gabarito_oficial'])

