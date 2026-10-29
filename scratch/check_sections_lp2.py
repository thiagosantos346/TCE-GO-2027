with open('fontes_de_estudo/conhecimentos_gerais/01_lingua_portuguesa/02_ortografia_acentuacao_e_formacao_de_palavras.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if l.startswith('#') or l.startswith('### Teste'):
        print(f"{i+1}: {l.strip()}")

