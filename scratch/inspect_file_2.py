import json
import re

TARGET_FILE = 'fontes_de_estudo/conhecimentos_gerais/01_lingua_portuguesa/02_ortografia_acentuacao_e_formacao_de_palavras.md'

with open(TARGET_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

# extrair os testes atuais
tests = re.findall(r'### Teste \d+[\s\S]*?(?=(?:### Teste \d+|## \d+|\Z))', content)
print(f"Total testes no arquivo: {len(tests)}")
for i, t in enumerate(tests):
    lines = t.strip().split('\n')
    print(f"Teste {i+1}: {lines[0]} | {lines[1] if len(lines)>1 else ''}")

# Carregar questões do banco
data = json.load(open('banco_questoes_extraidas.json', 'r', encoding='utf-8'))
pendentes = [q for q in data['questoes'] if q.get('target_file') == TARGET_FILE and q.get('status_integracao') == 'pendente']
print(f"\nTotal pendentes no banco para este arquivo: {len(pendentes)}")
print("Amostra de 5 questões pendentes:")
for q in pendentes[:5]:
    print(f"ID={q['id']} | {q['banca']} {q['ano']} | Enunciado: {q['enunciado'][:120].strip()}...")

