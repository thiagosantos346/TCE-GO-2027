import json

with open('banco_questoes_extraidas.json', 'r', encoding='utf-8') as f:
    questoes = json.load(f).get('questoes', [])

# Agrupar por enunciado normalizado
import re
def norm(t):
    return re.sub(r'\W+', '', (t or '').lower())[:60]

seen = {}
unique_questoes = []
for q in questoes:
    k = norm(q.get('enunciado'))
    if k and len(k) > 15:
        if k not in seen:
            seen[k] = q
            unique_questoes.append(q)

print(f"Total de questões únicas por texto no banco: {len(unique_questoes)}")

# Disciplinas presentes
portugues = 0
ingles = 0
direito = 0
ti = 0
controle = 0
outros = 0

for q in unique_questoes:
    en = (q.get('enunciado') or '').lower()
    if any(k in en for k in ['the ', 'text', 'which', 'according to', 'paragraph', 'meaning']):
        ingles += 1
    elif any(k in en for k in ['texto', 'autor', 'parágrafo', 'frase', 'oração', 'vírgula', 'crase', 'sintático', 'concordância', 'regência', 'vocábulo', 'sentido do termo']):
        portugues += 1
    elif any(k in en for k in ['cf/88', 'constituição', 'art.', 'servidor', 'administrativo', 'licitação', 'improbidade', 'ato administrativo']):
        direito += 1
    elif any(k in en for k in ['tce', 'tribunal de contas', 'nbasp', 'auditoria', 'controle externo', 'loa', 'ldo', 'ppa', 'orçamento']):
        controle += 1
    elif any(k in en for k in ['software', 'java', 'sql', 'banco de dados', 'rede', 'linux', 'ip', 'segurança', 'scrum', 'uml', 'requisito', 'memória', 'processador', 'dados', 'algoritmo']):
        ti += 1
    else:
        outros += 1

print(f"  Inglês: {ingles}")
print(f"  Português: {portugues}")
print(f"  Direito / Legislação: {direito}")
print(f"  Controle Externo / Orçamento: {controle}")
print(f"  Tecnologia da Informação: {ti}")
print(f"  Outros: {outros}")

