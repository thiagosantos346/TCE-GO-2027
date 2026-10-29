import json

with open('banco_questoes_extraidas.json', 'r', encoding='utf-8') as f:
    questoes = json.load(f).get('questoes', [])

candidates = [q for q in questoes if q.get('target_file') == 'fontes_de_estudo/conhecimentos_gerais/01_lingua_portuguesa/01_compreensao_e_interpretacao_de_texto.md']

figuras = [q for q in candidates if 'figura' in q.get('target_section', '').lower() or 'figura' in q.get('enunciado', '').lower()]
print(f"Total candidatas para figuras de linguagem: {len(figuras)}")
for q in figuras[:5]:
    print(f"[{q['id']}] {q.get('banca')} {q.get('orgao')} {q.get('ano')} | Seção: {q.get('target_section')}")
    print("  Enunc:", q.get('enunciado')[:100].strip().replace('\n', ' '))
    print("  Gab:", q.get('gabarito_oficial'))

