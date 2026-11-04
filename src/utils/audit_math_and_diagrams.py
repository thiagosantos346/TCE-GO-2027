#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Auditor e validador de fórmulas matemáticas (KaTeX / LaTeX) e diagramas (Mermaid).
"""

import os
import glob
import re

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DOCS_DIR = os.path.join(BASE_DIR, "docs")

def audit():
    md_files = glob.glob(os.path.join(DOCS_DIR, "**/*.md"), recursive=True)
    md_files = [f for f in md_files if "resources" not in f and not f.endswith("README.md") and "relatorio" not in f]

    print(f"Total de cadernos para auditar fórmulas e diagramas: {len(md_files)}")

    mermaid_count = 0
    display_math_count = 0
    inline_math_count = 0
    issues = []

    for fpath in md_files:
        rel = os.path.relpath(fpath, BASE_DIR).replace("\\", "/")
        with open(fpath, "r", encoding="utf-8") as fp:
            content = fp.read()

        # 1. Mermaid audit
        m_matches = list(re.finditer(r"```mermaid(.*?)```", content, re.DOTALL))
        mermaid_count += len(m_matches)
        for i, m in enumerate(m_matches):
            code = m.group(1).strip()
            lines = [l.strip() for l in code.splitlines() if l.strip() and not l.strip().startswith("%%")]
            if not lines:
                issues.append((rel, f"Mermaid #{i+1} vazio"))
                continue
            header = lines[0]
            valid_headers = (
                "flowchart", "graph", "sequenceDiagram", "classDiagram",
                "stateDiagram", "stateDiagram-v2", "erDiagram", "journey",
                "gantt", "pie", "quadrantChart", "gitGraph", "C4Context",
                "mindmap", "timeline", "xychart-beta"
            )
            if not any(header.startswith(vh) for vh in valid_headers):
                issues.append((rel, f"Mermaid #{i+1} tipo inválido ou desconhecido: '{header[:30]}'"))

        # 2. Math audit
        # Display math $$ ... $$
        d_matches = list(re.finditer(r"\$\$(.*?)\$\$", content, re.DOTALL))
        display_math_count += len(d_matches)
        for i, dm in enumerate(d_matches):
            formula = dm.group(1).strip()
            if not formula:
                issues.append((rel, f"Fórmula display #{i+1} vazia ($$$$)"))
            if r"\centernot" in formula:
                issues.append((rel, f"Fórmula display #{i+1} contém \\centernot incompatível"))
            # Check for unescaped HTML entities or common KaTeX syntax traps
            if "&" in formula and not any(env in formula for env in ("matrix", "aligned", "array", "cases", "align")):
                # Ampersand outside alignment environment
                if not re.search(r"\\(?:text|operatorname)\{.*&.*\}", formula):
                    issues.append((rel, f"Fórmula display #{i+1} '&' fora de ambiente de alinhamento: {formula[:40]}"))

        # Inline math $ ... $
        # Remove code blocks and display math first to avoid false positives
        clean_text = re.sub(r"```.*?```", "", content, flags=re.DOTALL)
        clean_text = re.sub(r"`[^`\n]+`", "", clean_text)
        clean_text = re.sub(r"\$\$.*?\$\$", "", clean_text, flags=re.DOTALL)

        i_matches = list(re.finditer(r"(?<!\\)\$(?!\$)([^\$\n]+?)(?<!\\)\$", clean_text))
        inline_math_count += len(i_matches)
        for i, im in enumerate(i_matches):
            formula = im.group(1).strip()
            # If formula contains Brazilian currency like R$ 100 or numbers like 100,00
            if re.match(r"^[0-9\.,\s]+$", formula):
                issues.append((rel, f"Inline math #{i+1} suspeito de ser valor monetário/numérico: ${formula}$"))
            if r"\centernot" in formula:
                issues.append((rel, f"Inline math #{i+1} contém \\centernot incompatível"))

    print(f"\nResultados da Auditoria:")
    print(f"  - Blocos Mermaid encontrados: {mermaid_count}")
    print(f"  - Fórmulas Display ($$...$$): {display_math_count}")
    print(f"  - Fórmulas Inline ($...$): {inline_math_count}")
    print(f"  - Inconsistências / Alertas encontrados: {len(issues)}")
    for rel, iss in issues:
        print(f"    [{rel}] {iss}")

    return len(issues)

if __name__ == "__main__":
    audit()
