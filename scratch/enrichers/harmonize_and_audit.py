# -*- coding: utf-8 -*-
"""
Script de Harmonização e Ordenação Sequencial:
1. Atualiza Status Geral nos READMEs de 12 e 13 para 🟢 Concluído.
2. Renumera as questões de 01 a 10 sequencialmente de acordo com a ordem linear no arquivo.
"""

import os, glob, re

base = "fontes_de_estudo/conhecimentos_especificos_b02_ti"
modules = ["12_governanca_de_ti", "13_legislacao_aplicada_a_ti", "14_lingua_inglesa_leitura_tecnica"]

# 1. Atualizar READMEs
for mod in ["12_governanca_de_ti", "13_legislacao_aplicada_a_ti"]:
    readme_path = os.path.join(base, mod, "README.md")
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
    content = content.replace(
        "> **Status Geral:** 🟡 Em mapeamento de fontes teóricas",
        "> **Status Geral:** 🟢 Concluído (100% enriquecido e auditado)"
    )
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[README] {mod}/README.md atualizado!")

# 2. Renumerar questões sequencialmente de 01 a 10
class Counter:
    def __init__(self):
        self.val = 1
    def inc(self, match):
        res = f"### Questão {self.val:02d}"
        self.val += 1
        return res

for mod in modules:
    mod_path = os.path.join(base, mod)
    files = sorted(glob.glob(os.path.join(mod_path, "*.md")))
    for f in files:
        if os.path.basename(f) == "README.md":
            continue
        with open(f, "r", encoding="utf-8") as fp:
            content = fp.read()

        c = Counter()
        new_content = re.sub(r"### Questão \d\d", c.inc, content)
        
        with open(f, "w", encoding="utf-8") as fp:
            fp.write(new_content)
        print(f"[RENUMERADO] {os.path.basename(f)}: {c.val - 1} questões ajustadas de 01 a 10.")

print("Processamento concluído com sucesso!")
