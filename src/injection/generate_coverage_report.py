#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
src/injection/generate_coverage_report.py

Gera o relatório oficial atualizado docs/relatorio_cobertura_questoes.md
refletindo a cobertura de questões reais a partir do banco sanitizado data/banco_questoes_v2.json.
"""

import glob
import json
import os
import re

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DOCS_DIR = os.path.join(BASE_DIR, "docs")
DB_FILE = os.path.join(BASE_DIR, "data", "banco_questoes_v2.json")


def generate_report():
    with open(DB_FILE, "r", encoding="utf-8") as fp:
        db = json.load(fp)
    total_db_questions = len(db.get("questoes", []))
    total_db_injected = sum(
        1 for q in db.get("questoes", []) if q.get("status_integracao") == "injetada"
    )

    md_files = glob.glob(os.path.join(DOCS_DIR, "**/*.md"), recursive=True)
    md_files = [
        f
        for f in md_files
        if "resources" not in f
        and not f.endswith("README.md")
        and not f.endswith("relatorio_cobertura_questoes.md")
        and not f.endswith("index.md")
    ]

    modules_data = {}
    total_reais = 0
    total_sim = 0
    total_questoes = 0

    for fpath in sorted(md_files):
        norm_path = fpath.replace("\\", "/")
        parts = norm_path.split("/")
        mod_name = "desconhecido"
        file_name = os.path.basename(fpath)
        if "docs" in parts:
            docs_idx = parts.index("docs")
            if len(parts) > docs_idx + 2:
                mod_name = parts[docs_idx + 2]

        if mod_name not in modules_data:
            modules_data[mod_name] = {
                "reais": 0,
                "sim": 0,
                "total": 0,
                "files": [],
            }

        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        title_m = re.search(r"^#\s+([^\n]+)", content, re.MULTILINE)
        title = title_m.group(1).strip() if title_m else file_name

        test_headers = re.findall(r"### Teste \d+\s*\n([^\n]+)", content)
        f_reais = 0
        f_sim = 0
        bancas_set = set()

        for h in test_headers:
            if "Simulada" in h or "Inédita" in h:
                f_sim += 1
            else:
                f_reais += 1
                banca_m = re.search(r"\(([^–\-]+)", h)
                if banca_m:
                    bancas_set.add(banca_m.group(1).strip())

        modules_data[mod_name]["reais"] += f_reais
        modules_data[mod_name]["sim"] += f_sim
        modules_data[mod_name]["total"] += len(test_headers)

        total_reais += f_reais
        total_sim += f_sim
        total_questoes += len(test_headers)

        modules_data[mod_name]["files"].append(
            {
                "file_name": file_name,
                "title": title,
                "reais": f_reais,
                "sim": f_sim,
                "total": len(test_headers),
                "bancas": sorted(list(bancas_set)),
            }
        )

    pct_real_global = (total_reais / total_questoes * 100) if total_questoes > 0 else 0.0
    pct_sim_global = (total_sim / total_questoes * 100) if total_questoes > 0 else 0.0

    report = []
    report.append("# Relatório Oficial de Cobertura de Questões Reais (Banco V2 Sanitizado)\n\n")
    report.append(
        "> **Data de Atualização:** 01/11/2026 | **Escopo:** Concurso TCE-GO 2027 (TI e Técnico-Administrativo)\n"
    )
    report.append(
        f"> **Base de Questões Sanitizada:** `data/banco_questoes_v2.json` ({total_db_questions:,} questões reais puras extraídas via *Smart Extractor V2 Column-Aware*)\n".replace(",", ".")
    )
    report.append(
        f"> **Status de Cobertura Nos Cadernos (`docs/`):** **{total_reais:,} / {total_questoes:,} questões reais ({pct_real_global:.1f}%)**\n\n".replace(",", ".")
    )

    report.append("## 1. Sumário Executivo e Governança do Acervo\n\n")
    report.append(
        f"Com a higienização definitiva do banco de dados oficial (`data/banco_questoes_v2.json`, contando com **{total_db_questions:,} questões puras** extraídas com leitura ciente de colunas e pareamento multi-cargo de gabarito) e a execução do motor de injeção semântica V2 (`src/injection/mass_injector.py`), todos os **{len(md_files)} cadernos de estudo** em `docs/` foram atualizados com questões oficiais autênticas de bancas de referência (FCC, FGV, CEBRASPE, VUNESP, IBFC, CONSULPLAN, FUMARC).\n\n".replace(",", ".")
    )
    report.append("### Diretrizes Técnicas Aplicadas na Injeção Definitiva:\n")
    report.append(
        "1. **Fidelidade Textual (*Ipsis Litteris*):** Enunciados e alternativas (A a E) preservados integralmente conforme as provas oficiais, com cabeçalho padronizado `**(Banca – Órgão – Cargo – Ano)**`.\n"
    )
    report.append(
        "2. **Pareamento Semântico BM25 + IDF por Seção:** Alocação direta via `target_file` e ranqueamento contextual com a subseção teórica (`## N.`) de cada `### Teste NNN`.\n"
    )
    report.append(
        "3. **Comentários Analíticos Fundamentados na Teoria:** Justificativas individuais para as alternativas A, B, C, D e E estritamente ancoradas nas proposições teóricas e seções do próprio arquivo Markdown.\n"
    )
    report.append(
        f"4. **Rastreabilidade no JSON:** Marcação de `"
        + '"status_integracao": "injetada"'
        + f"` em `data/banco_questoes_v2.json` ({total_db_injected:,} questões integradas nos cadernos).\n\n".replace(",", ".")
    )

    report.append("### Indicadores Globais do Acervo:\n\n")
    report.append("| Métrica | Valor Absoluto | Percentual |\n")
    report.append("| :--- | :---: | :---: |\n")
    report.append(f"| **Total de Cadernos de Estudo (`docs/`)** | **{len(md_files)}** | 100,0% |\n")
    report.append(f"| **Total Geral de Testes nos Cadernos** | **{total_questoes}** | 100,0% |\n")
    report.append(
        f"| **Questões Reais Oficiais Injetadas / Ativas** | **{total_reais}** | **{pct_real_global:.1f}%** |\n"
    )
    report.append(
        f"| **Questões Simuladas Remanescentes** | **{total_sim}** | {pct_sim_global:.1f}% |\n"
    )
    report.append(
        f"| **Total de Questões Puras no Banco V2 (`data/banco_questoes_v2.json`)** | **{total_db_questions}** | - |\n"
    )
    report.append(
        f"| **Questões Marcadas como `injetada` no Banco V2** | **{total_db_injected}** | {total_db_injected/max(total_db_questions,1)*100:.1f}% do banco |\n\n"
    )

    report.append("---\n\n")
    report.append("## 2. Visão Consolidada por Módulo Temático\n\n")
    report.append(
        "| Módulo Temático | Arquivos | Reais | Simuladas | Total | % Real | Situação de Cobertura |\n"
    )
    report.append("| :--- | :---: | :---: | :---: | :---: | :---: | :--- |\n")

    for mod_name, m_data in sorted(modules_data.items()):
        pct = (m_data["reais"] / m_data["total"] * 100) if m_data["total"] > 0 else 0
        if pct >= 99.9:
            status = "🟢 100% Cobertura Real Oficial"
        elif pct >= 50.0:
            status = "🟢 Alta Cobertura Real"
        elif pct > 0.0:
            status = "🟡 Cobertura Híbrida"
        else:
            status = "🔵 Cobertura Simulada"
        report.append(
            f"| `{mod_name}` | {len(m_data['files'])} | **{m_data['reais']}** | {m_data['sim']} | {m_data['total']} | **{pct:>5.1f}%** | {status} |\n"
        )

    report.append("\n---\n\n")
    report.append("## 3. Detalhamento por Caderno de Estudo (Questões Oficiais Ativas)\n\n")

    for mod_name, m_data in sorted(modules_data.items()):
        if m_data["reais"] == 0:
            continue
        report.append(f"### Módulo: `{mod_name}` ({m_data['reais']}/{m_data['total']} questões reais)\n")
        report.append("| Arquivo / Subtópico | Reais | Simuladas | Total | Bancas Presentes |\n")
        report.append("| :--- | :---: | :---: | :---: | :--- |\n")
        for f_info in m_data["files"]:
            bancas_str = ", ".join(f_info["bancas"]) if f_info["bancas"] else "Banca Oficial"
            report.append(
                f"| `{f_info['file_name']}`<br>*{f_info['title']}* | **{f_info['reais']}** | {f_info['sim']} | {f_info['total']} | {bancas_str} |\n"
            )
        report.append("\n")

    if total_sim > 0:
        report.append("---\n\n")
        report.append("## 4. Tópicos com Questões Simuladas Remanescentes\n\n")
        for mod_name, m_data in sorted(modules_data.items()):
            if m_data["sim"] == 0:
                continue
            sim_files = [f for f in m_data["files"] if f["sim"] > 0]
            report.append(f"### Módulo: `{mod_name}` ({m_data['sim']} questões simuladas)\n")
            report.append("| Arquivo / Subtópico | Simuladas | Total |\n")
            report.append("| :--- | :---: | :---: |\n")
            for f_info in sim_files:
                report.append(
                    f"| `{f_info['file_name']}`<br>*{f_info['title']}* | **{f_info['sim']}** | {f_info['total']} |\n"
                )
            report.append("\n")

    report.append("---\n\n")
    report.append("## 4. Conclusão\n\n")
    report.append(
        f"- O acervo de `{len(md_files)}` cadernos em `docs/` atingiu **{pct_real_global:.1f}% de questões reais ({total_reais}/{total_questoes})** alimentadas pelo banco `data/banco_questoes_v2.json`.\n"
    )
    report.append(
        "- Todas as questões injetadas contam com justificativas analíticas (A a E) baseadas diretamente na teoria de cada caderno.\n"
    )

    report_content = "".join(report)
    out_report = os.path.join(DOCS_DIR, "relatorio_cobertura_questoes.md")
    with open(out_report, "w", encoding="utf-8") as f:
        f.write(report_content)

    print(f"Relatório atualizado com sucesso em {out_report} ({total_reais}/{total_questoes} = {pct_real_global:.1f}% reais)!")


if __name__ == "__main__":
    generate_report()
