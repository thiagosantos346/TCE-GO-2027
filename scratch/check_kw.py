import json

with open('banco_questoes_extraidas.json', 'r', encoding='utf-8') as f:
    questoes = json.load(f).get('questoes', [])

ti_keywords = ['software', 'scrum', 'requisito', 'kanban', 'uml', 'bpmn', 'banco de dados', 'sql', 'python', 'java', 'docker', 'kubernetes', 'linux', 'rede', 'tcp', 'ip', 'segurança', 'firewall', 'itil', 'cobit', 'lgpd', 'constitucional', 'administrativo', 'licitação', 'orçamento', 'receita', 'despesa', 'controle externo', 'tribunal de contas']

by_kw = {}
for q in questoes:
    en = (q.get('enunciado') or '').lower()
    for kw in ti_keywords:
        if kw in en:
            by_kw[kw] = by_kw.get(kw, 0) + 1

print(f"Total questões no banco: {len(questoes)}")
for kw, c in sorted(by_kw.items(), key=lambda x: x[1], reverse=True):
    print(f"  {c:3d} questoes com '{kw}'")

