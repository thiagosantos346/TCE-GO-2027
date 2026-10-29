import json
import re

with open('banco_questoes_extraidas.json', 'r', encoding='utf-8') as f:
    questoes = json.load(f).get('questoes', [])

def norm(t):
    return re.sub(r'\W+', '', (t or '').lower())[:60]

seen = set()
unique_questoes = []
for q in questoes:
    k = norm(q.get('enunciado'))
    if k and len(k) > 15:
        if k not in seen:
            seen.add(k)
            alts = q.get('alternativas', {})
            if isinstance(alts, dict) and len(alts) >= 4 and q.get('gabarito_oficial'):
                unique_questoes.append(q)

print(f"Total únicas válidas com gabarito e alternativas completas: {len(unique_questoes)}")

# Amostras de TI reais
ti_qs = []
for q in unique_questoes:
    en = (q.get('enunciado') or '').lower()
    if any(k in en for k in ['software', 'java', 'sql', 'banco de dados', 'rede', 'linux', 'ip', 'segurança', 'scrum', 'uml', 'requisito', 'memória', 'processador', 'algoritmo', 'protocolo', 'tabela']):
        ti_qs.append(q)

print(f"Total questões de TI válidas no banco: {len(ti_qs)}")
for q in ti_qs[:5]:
    print(f"[{q['id']}] {q.get('banca')} {q.get('orgao')} ({q.get('ano')})")
    print("  Enunc:", q.get('enunciado')[:110].strip().replace('\n', ' '))
    print("  Gabarito:", q.get('gabarito_oficial'))
    for l, txt in list(q.get('alternativas', {}).items())[:2]:
        print(f"    {l}) {txt[:70].strip()}")

