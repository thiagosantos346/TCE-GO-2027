import re

for fname in ['06_redacao_reescrita_e_equivalencia_de_estruturas.md', '07_redacao_oficial.md']:
    path = f'fontes_de_estudo/conhecimentos_gerais/01_lingua_portuguesa/{fname}'
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    tests = re.findall(r'(### Teste \d+[\s\S]*?(?=(?:### Teste \d+|## \d+|\Z)))', text)
    print(f"\n===== {fname} ({len(tests)} testes) =====")
    for i, t in enumerate(tests):
        lines = [l.strip() for l in t.split('\n') if l.strip()]
        print(f"--- TESTE {i+1} ---")
        print(lines[0])
        print(lines[1])
        print(lines[2][:120] if len(lines)>2 else '')

