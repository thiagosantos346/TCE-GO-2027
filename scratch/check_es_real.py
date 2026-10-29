import json

data = json.load(open('banco_questoes_extraidas.json', 'r', encoding='utf-8'))
folder = 'fontes_de_estudo/conhecimentos_especificos_b02_ti/04_engenharia_de_software/'

for q in data['questoes']:
    if q.get('status_integracao') == 'pendente' and q.get('target_file', '').startswith(folder):
        print(f"ID={q['id']} | {q['banca']} {q['ano']} | TF={q['target_file'].split('/')[-1]} | {q['enunciado'][:100].strip().replace(chr(10), ' ')}")

