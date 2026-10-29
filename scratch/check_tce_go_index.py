import json

data = json.load(open('banco_questoes_extraidas.json', 'r', encoding='utf-8'))
questoes = data['questoes']

tce_go_questoes = [q for q in questoes if 'tce-go' in q.get('id', '').lower() or 'tce_go' in q.get('id', '').lower() or ('tce' in q.get('orgao', '').lower() and 'go' in q.get('orgao', '').lower())]

print(f"Total identificadas pelo ID/orgao: {len(tce_go_questoes)}")

# Se não encontrou pelo ID direto, vamos ver como as questoes do TCE-GO 2024 foram rotuladas
sample_tce = [q for q in questoes if '16.168' in q.get('enunciado', '') or 'Constituição do Estado de Goiás' in q.get('enunciado', '')]
print(f"Total encontradas por menção à Lei 16.168/Const GO: {len(sample_tce)}")
for q in sample_tce[:5]:
    print(f"ID={q['id']} | Banca={q['banca']} | Orgao={q['orgao']} | Ano={q['ano']} | Cargo={q['cargo']}")

