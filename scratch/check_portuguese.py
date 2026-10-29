import json

data = json.load(open('banco_questoes_extraidas.json', 'r', encoding='utf-8'))
questoes = [q for q in data['questoes'] if q.get('status_integracao') == 'pendente']

print("Amostra das questões 1 a 5 de várias provas:")
for q in questoes:
    if q.get('numero_original') in [1, 2, 3, 4, 5] and q.get('banca') == 'FCC':
        print(f"ID={q['id']} | Num={q['numero_original']} | Banca={q['banca']} | Ano={q['ano']} | Enunciado={q['enunciado'][:100].strip()}...")

