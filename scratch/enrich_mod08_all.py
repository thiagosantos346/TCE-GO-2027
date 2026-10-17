# -*- coding: utf-8 -*-
import os
import re

BASE_DIR = "fontes_de_estudo/conhecimentos_especificos_b02_ti/08_banco_de_dados"

def enrich_file_01():
    path = os.path.join(BASE_DIR, "01_modelagem_de_dados_mer_e_normalizacao.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Verify questions 01-05 exist
    for q in ["### Questão 01", "### Questão 02", "### Questão 03", "### Questão 04", "### Questão 05"]:
        assert q in content, f"Missing {q} in {path}"

    from enrich_module_08 import q06_f01, q07_f01, q08_f01, q09_f01, q10_f01, q11_f01

    # Insert Q06 after 1.4 table (before ## 2. Modelo Entidade-Relacionamento)
    p1 = "## 2. Modelo Entidade-Relacionamento (MER / DER de Peter Chen)"
    assert p1 in content
    content = content.replace(p1, q06_f01 + "\n" + p1, 1)

    # Insert Q07 after 2.2 table (before ### 2.3 Relacionamentos)
    p2 = "### 2.3 Relacionamentos, Cardinalidade e Participação (Total vs. Parcial)"
    assert p2 in content
    content = content.replace(p2, q07_f01 + "\n" + p2, 1)

    # Insert Q08 after 2.3 (before ## 3. Álgebra Relacional: Operações Formais e Consultas)
    p3 = "## 3. Álgebra Relacional: Operações Formais e Consultas"
    assert p3 in content
    content = content.replace(p3, q08_f01 + "\n" + p3, 1)

    # Insert Q09 after 4.1 (before ### 4.2 A Escada da Normalização: 1ª FN, 2ª FN e 3ª FN)
    p4 = "### 4.2 A Escada da Normalização: 1ª FN, 2ª FN e 3ª FN"
    assert p4 in content
    content = content.replace(p4, q09_f01 + "\n" + p4, 1)

    # Insert Q10 after 4.2 (before ### 4.3 Forma Normal de Boyce-Codd)
    p5 = "### 4.3 Forma Normal de Boyce-Codd (FNBC / BCNF) vs. 3ª FN"
    assert p5 in content
    content = content.replace(p5, q10_f01 + "\n" + p5, 1)

    # Insert Q11 after 5.2 (before ## 🌐 Fontes Oficiais e Referências Bibliográficas)
    p6 = "## 🌐 Fontes Oficiais e Referências Bibliográficas"
    assert p6 in content
    content = content.replace(p6, q11_f01 + "\n" + p6, 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("File 01 successfully enriched! Total questions:", len(re.findall(r"### Questão \d+", content)))

enrich_file_01()
