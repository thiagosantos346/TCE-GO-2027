import os
import re

ROOT = os.getcwd()
dirs = [
    'fontes_de_estudo/conhecimentos_gerais',
    'fontes_de_estudo/conhecimentos_especificos_b02_ti',
    'fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo'
]

fixed_files = 0

for d in dirs:
    base = os.path.join(ROOT, d)
    for dp, _, fns in os.walk(base):
        for fn in sorted(fns):
            if fn.endswith('.md') and fn.lower() != 'readme.md':
                p = os.path.join(dp, fn)
                with open(p, 'r', encoding='utf-8') as f:
                    content = f.read()

                class QReplacer:
                    def __init__(self):
                        self.count = 0
                    def __call__(self, m):
                        self.count += 1
                        prefix = m.group(1)
                        return f"{prefix}Questão {self.count:02d}"

                replacer = QReplacer()
                new_content = re.sub(r'^(#{2,4}\s+)(?:\*\*)?Quest[ãa]o\s+\d+(?:\*\*)?', replacer, content, flags=re.MULTILINE | re.IGNORECASE)

                if new_content != content:
                    with open(p, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    fixed_files += 1

print(f"Arquivos renumerados sequencialmente com sucesso: {fixed_files}")

