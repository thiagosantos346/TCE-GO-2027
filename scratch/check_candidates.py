import json

with open('scratch/candidates_by_file.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

f1 = 'fontes_de_estudo/conhecimentos_gerais/01_lingua_portuguesa/01_compreensao_e_interpretacao_de_texto.md'
qs = data[f1]
fcc = [q for q in qs if q.get('banca') == 'FCC']

for q in fcc[:5]:
    print("="*60)
    print("ID:", q['id'])
    print("ENUNCIADO:\n", q['enunciado'])
    print("ALTERNATIVAS:\n", json.dumps(q['alternativas'], ensure_ascii=False, indent=2))
