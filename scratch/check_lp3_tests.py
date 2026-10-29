import re

TARGET_FILE = 'fontes_de_estudo/conhecimentos_gerais/01_lingua_portuguesa/03_morfossintaxe_pronomes_e_verbos.md'
with open(TARGET_FILE, 'r', encoding='utf-8') as f:
    text = f.read()

tests = re.findall(r'(### Teste \d+[\s\S]*?(?=(?:### Teste \d+|## \d+|\Z)))', text)
print(f"Total testes no arquivo 03: {len(tests)}")
for i, t in enumerate(tests):
    lines = [l.strip() for l in t.split('\n') if l.strip()]
    print(f"--- TESTE {i+1} ---")
    print(lines[0])
    print(lines[1])
    print(lines[2][:120] if len(lines)>2 else '')

