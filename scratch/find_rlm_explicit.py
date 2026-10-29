import json

data = json.load(open('banco_questoes_extraidas.json', 'r', encoding='utf-8'))
for q in data['questoes']:
    text = q['enunciado'] + ' ' + ' '.join(q['alternativas'].values())
    if 'raciocínio lógico' in text.lower() or 'silogismo' in text.lower() or 'conclusão verdadeira' in text.lower() or 'negação lógica' in text.lower() or 'diagrama' in text.lower():
        print(f"ID={q['id']} | Num={q.get('numero_original')} | {q['banca']} {q['ano']} | {q['enunciado'][:110].strip().replace(chr(10), ' ')}")

