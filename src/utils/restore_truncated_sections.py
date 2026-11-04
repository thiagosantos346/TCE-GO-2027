#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Restaura seções teóricas que foram truncadas acidentalmente durante a injeção RAG em 13 cadernos.
"""

import os
import re
import subprocess

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def get_old_content(rel_path):
    cmd = ["git", "show", f"66311d0:{rel_path}"]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    if res.returncode != 0:
        raise RuntimeError(f"Erro ao ler {rel_path} do git 66311d0")
    return res.stdout

def restore_section_between(rel_path, sec_header_pattern, next_sec_in_curr):
    fpath = os.path.join(BASE_DIR, rel_path)
    with open(fpath, "r", encoding="utf-8") as f:
        curr = f.read()

    # Check if section header is already present
    if re.search(rf"^##\s+{sec_header_pattern}", curr, re.MULTILINE):
        print(f"Seção '{sec_header_pattern}' já presente em {rel_path}.")
        return

    old = get_old_content(rel_path)
    # Extract from old starting at sec_header_pattern until the next section or tests
    # We want only the theory part (exclude ### Teste if any)
    pat = rf"(##\s+{sec_header_pattern}.*?\n)(?=^## |\Z)"
    m = re.search(pat, old, re.MULTILINE | re.DOTALL)
    if not m:
        print(f"[ERRO] Não encontrou '{sec_header_pattern}' em 66311d0 para {rel_path}")
        return

    sec_text = m.group(1)
    # Remove any old tests from this section text if any
    sec_text = re.sub(r"### Teste \d+.*?\n(?=## |### (?!Teste)|\Z)", "", sec_text, flags=re.DOTALL)
    sec_text = sec_text.rstrip() + "\n\n"

    # Find next_sec_in_curr in curr
    idx = curr.find(next_sec_in_curr)
    if idx == -1:
        print(f"[ERRO] Ponto de inserção '{next_sec_in_curr}' não encontrado em {rel_path}")
        return

    curr = curr[:idx] + sec_text + curr[idx:]
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(curr)
    print(f"Restauração bem-sucedida de '{sec_header_pattern}' em: {rel_path}")

def run():
    print("Restauração das 8 seções restantes...")

    # 1. 02_receita_publica_estagios_fontes_e_classificacoes.md
    restore_section_between(
        "docs/conhecimentos_especificos_a01_tecnico_administrativo/19_nocoes_de_administracao_financeira_e_orcamentaria/02_receita_publica_estagios_fontes_e_classificacoes.md",
        r"3\.\s+Classificações da Receita Orçamentária",
        "## 4. Regras Fiscais Restritivas da Receita e a LRF"
    )

    # 2. 01_teorias_da_administracao_e_escolas_administrativas.md
    restore_section_between(
        "docs/conhecimentos_especificos_a01_tecnico_administrativo/22_administracao_geral/01_teorias_da_administracao_e_escolas_administrativas.md",
        r"4\.\s+Teoria da Burocracia \(Max Weber\)",
        "## 5. Abordagem Comportamental"
    )

    # 3. 01_planejamento_estrategico_missao_visao_valores_e_escolas.md
    restore_section_between(
        "docs/conhecimentos_especificos_a01_tecnico_administrativo/23_administracao_estrategica/01_planejamento_estrategico_missao_visao_valores_e_escolas.md",
        r"2\.\s+O Ciclo da Gestão Estratégica Integrada",
        "## 3. Estratégias Deliberadas"
    )

    # 4. 01_fundamentos_ia_machine_learning_e_deep_learning.md
    restore_section_between(
        "docs/conhecimentos_especificos_b02_ti/09_inteligencia_artificial_e_ciencia_de_dados/01_fundamentos_ia_machine_learning_e_deep_learning.md",
        r"3\.\s+Aprendizado Não Supervisionado e por Reforço",
        "## 4. Redes Neurais Artificiais e Deep Learning"
    )

    # 5. 04_ciencia_de_dados_estatistica_e_big_data.md
    restore_section_between(
        "docs/conhecimentos_especificos_b02_ti/09_inteligencia_artificial_e_ciencia_de_dados/04_ciencia_de_dados_estatistica_e_big_data.md",
        r"2\.\s+Estatística Aplicada, Probabilidades e Testes de Hipóteses",
        "## 3. Avaliação de Modelos Preditivos"
    )

    # 6. 05_computacao_em_nuvem_modelos_serverless_e_hibridos.md
    restore_section_between(
        "docs/conhecimentos_especificos_b02_ti/11_sistemas_operacionais_redes_e_nuvem/05_computacao_em_nuvem_modelos_serverless_e_hibridos.md",
        r"2\.\s+Modelos de Serviço e Matriz de Responsabilidade Compartilhada",
        "## 3. Computação Serverless"
    )

    # 7. 02_gestao_de_servicos_de_ti_itil_v4.md
    # In this file, check what next section is
    with open("docs/conhecimentos_especificos_b02_ti/12_governanca_de_ti/02_gestao_de_servicos_de_ti_itil_v4.md", "r", encoding="utf-8") as f:
        c = f.read()
    # Find next H2 after section 1
    next_h2 = re.search(r"^##\s+(?:3\.|4\.|5\.|6\.|🌐).*$", c, re.MULTILINE)
    if next_h2:
        restore_section_between(
            "docs/conhecimentos_especificos_b02_ti/12_governanca_de_ti/02_gestao_de_servicos_de_ti_itil_v4.md",
            r"2\.\s+Práticas Essenciais de Gerenciamento de Serviços da ITIL v4",
            next_h2.group(0)
        )

    # 8. 01_lgpd_aplicada_ao_desenvolvimento_e_sistemas.md
    restore_section_between(
        "docs/conhecimentos_especificos_b02_ti/13_legislacao_aplicada_a_ti/01_lgpd_aplicada_ao_desenvolvimento_e_sistemas.md",
        r"2\.\s+Princípios do Art\. 6º sob a Ótica da Arquitetura e Engenharia de Software",
        "## 3. Privacy by Design e Privacy by Default"
    )

    print("Restauração das 8 seções finalizada!")

if __name__ == "__main__":
    run()
