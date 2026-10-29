import json

data = json.load(open('banco_questoes_extraidas.json', 'r', encoding='utf-8'))
TARGET_FILE = 'fontes_de_estudo/conhecimentos_especificos_b02_ti/08_banco_de_dados/01_modelagem_de_dados_mer_e_normalizacao.md'

matches = [q for q in data['questoes'] if q.get('target_file') == TARGET_FILE and q.get('status_integracao') == 'pendente' and len(q.get('alternativas', {})) == 5]

print(f"Total de questões reais com 5 alternativas para DB 01: {len(matches)}")
for q in matches[:10]:
    print("=" * 60)
    print(f"ID={q['id']} | {q['banca']} {q['ano']} | {q['enunciado'][:120].strip().replace(chr(10), ' ')}")
    print(f"GAB={q['gabarito_oficial']}")

