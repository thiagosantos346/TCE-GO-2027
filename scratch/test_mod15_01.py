import re
import os

fpath = "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/15_nocoes_de_direito_administrativo/01_regime_juridico_principios_e_lindb.md"

with open(fpath, "r", encoding="utf-8") as f:
    content = f.read()

# Verify pre-existing questions
assert "### Questão 01" in content
assert "### Questão 02" in content
assert "### Questão 03" in content
assert "### Questão 04" in content
assert "### Questão 05" in content

print("All 5 original questions verified in file 01.")
