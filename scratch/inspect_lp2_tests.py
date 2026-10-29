import re

with open('fontes_de_estudo/conhecimentos_gerais/01_lingua_portuguesa/02_ortografia_acentuacao_e_formacao_de_palavras.md', 'r', encoding='utf-8') as f:
    text = f.read()

tests = re.findall(r'(### Teste \d+[\s\S]*?(?=(?:### Teste \d+|## \d+|\Z)))', text)
for i, t in enumerate(tests):
    lines = [l.strip() for l in t.split('\n') if l.strip()]
    print(f"--- TESTE {i+1} ---")
    print(lines[0])
    print(lines[1])
    print(lines[2][:150] if len(lines)>2 else '')

