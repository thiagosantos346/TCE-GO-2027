# -*- coding: utf-8 -*-
import sys
import re

with open("scratch/enrich_mod15_part1.py", "r", encoding="utf-8") as f:
    code = f.read()

exec(code)

with open(f01_path, "r", encoding="utf-8") as f:
    text = f.read()

# Verificações de segurança
orig_q_count = len(re.findall(r"### Questão \d+", text))
assert orig_q_count == 5, f"Expected 5 questions, found {orig_q_count}"

# Inserções ordenadas de trás para frente para manter os offsets válidos se usarmos regex,
# ou usando substituição precisa de âncoras.

# 1. Âncora 5.1 -> Q11
ancora_51 = "### 5.1 Consequencialismo Jurídico e Vedação de Valores Abstratos (Art. 20)"
# Vamos achar o final da seção 5.1 antes da 5.2
pos_51 = text.find(ancora_51)
pos_52 = text.find("### 5.2 Obstáculos Reais", pos_51)
assert pos_51 != -1 and pos_52 != -1
block_q11 = "\n\n" + q11_01.strip() + "\n\n---\n\n"
text = text[:pos_52] + block_q11 + text[pos_52:]

# 2. Âncora 4.4 -> Q10
ancora_44 = "### 4.4 Princípio da Motivação e a Teoria dos Motivos Determinantes"
pos_44 = text.find(ancora_44)
pos_45 = text.find("### 4.5 Princípio da Continuidade", pos_44)
assert pos_44 != -1 and pos_45 != -1
block_q10 = "\n\n" + q10_01.strip() + "\n\n---\n\n"
text = text[:pos_45] + block_q10 + text[pos_45:]

# 3. Âncora 3.5 -> Q09
ancora_35 = "### 3.5 Princípio da Eficiência (Emenda Constitucional nº 19/1998)"
pos_35 = text.find(ancora_35)
pos_4 = text.find("## 4. Princípios Administrativos Implícitos", pos_35)
assert pos_35 != -1 and pos_4 != -1
block_q09 = "\n\n" + q09_01.strip() + "\n\n---\n\n"
text = text[:pos_4] + block_q09 + text[pos_4:]

# 4. Âncora 3.1 -> Q08
ancora_31 = "### 3.1 Princípio da Legalidade Estrita"
pos_31 = text.find(ancora_31)
pos_32 = text.find("### 3.2 Princípio da Impessoalidade", pos_31)
assert pos_31 != -1 and pos_32 != -1
block_q08 = "\n\n" + q08_01.strip() + "\n\n---\n\n"
text = text[:pos_32] + block_q08 + text[pos_32:]

# 5. Âncora 2.2 -> Q07
ancora_22 = "### 2.2 Princípio da Indisponibilidade do Interesse Público"
pos_22 = text.find(ancora_22)
pos_23 = text.find("### 2.3 Interesse Público Primário", pos_22)
assert pos_22 != -1 and pos_23 != -1
block_q07 = "\n\n" + q07_01.strip() + "\n\n---\n\n"
text = text[:pos_23] + block_q07 + text[pos_23:]

# 6. Âncora 1.2 -> Q06
ancora_12 = "### 1.2 Sentido Objetivo, Material ou Funcional"
pos_12 = text.find(ancora_12)
pos_13 = text.find("### 1.3 Critérios Distintivos", pos_12)
assert pos_12 != -1 and pos_13 != -1
block_q06 = "\n\n" + q06_01.strip() + "\n\n---\n\n"
text = text[:pos_13] + block_q06 + text[pos_13:]

# Validação final do arquivo 01
final_qs = re.findall(r"### Questão (\d+)", text)
print("Questões no arquivo 01:", final_qs)
assert len(final_qs) == 11
assert sorted(final_qs) == ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']

with open(f01_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Arquivo 01 gravado com sucesso! Total: 11 questões.")
