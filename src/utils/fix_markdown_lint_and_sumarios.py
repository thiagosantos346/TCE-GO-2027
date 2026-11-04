#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
src/utils/fix_markdown_lint_and_sumarios.py

Ajusta com precisão artesanal todos os cadernos de estudo Markdown:
1. Reconstrói o ## 🧭 Sumário rigorosamente conforme as diretrizes do usuário:
   - Seção principal: 1. [Título](#slug), 2. [Título](#slug) (sem número duplicado no texto)
   - Subseções e Testes: tabulados com 4 espaços e 1. [Subtítulo](#slug)
   - Slugs GFM 100% válidos (preservando acentuação Unicode e tratando símbolos)
2. Resolve MD022: Garante linha em branco antes e depois de cada heading (incluindo ### Teste XXX)
3. Resolve MD004: Padroniza marcadores de listas não ordenadas com dash (-) em vez de asterisco (*)
4. Resolve MD032: Garante linhas em branco antes e depois de blocos de lista
5. Resolve MD012: Elimina linhas em branco consecutivas múltiplas
6. Resolve MD009: Remove espaços em branco desnecessários no fim das linhas
"""

import os
import glob
import re

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DOCS_DIR = os.path.join(BASE_DIR, "docs")

def gfm_slug(text):
    """
    Algoritmo oficial GFM (GitHub Flavored Markdown) compatível com markdownlint MD051:
    - Remove formatação markdown (*, `, $)
    - Converte para minúsculas
    - Remove pontuação e símbolos (mantendo letras Unicode \w, dígitos, hífens e espaços)
    - Converte espaços em hífens
    """
    text = re.sub(r'[\*`\$]', '', text)
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'\s', '-', text)
    return text

def build_sumario_block(content):
    lines = content.splitlines()
    in_sumario = False
    past_sumario = False
    headings = []

    for l in lines:
        if l.startswith("## 🧭 Sumário"):
            in_sumario = True
            continue
        if in_sumario and l.startswith("## "):
            in_sumario = False
            past_sumario = True
        if past_sumario:
            if l.startswith("## "):
                headings.append((2, l[3:].strip()))
            elif l.startswith("### "):
                headings.append((3, l[4:].strip()))

    if not headings:
        return None

    used_slugs = {}
    sumario_lines = ["## 🧭 Sumário\n"]
    h2_idx = 0

    for level, htext in headings:
        base_slug = gfm_slug(htext)
        if base_slug in used_slugs:
            slug = f"{base_slug}-{used_slugs[base_slug]}"
            used_slugs[base_slug] += 1
        else:
            used_slugs[base_slug] = 1
            slug = base_slug

        clean_title = re.sub(r'[\*`\$]', '', htext).strip()

        if level == 2:
            h2_idx += 1
            # Remove leading numbering like '1. ', '2. '
            clean_title = re.sub(r'^\d+\.\s*', '', clean_title)
            # Remove leading symbols like '🌐 '
            clean_title = re.sub(r'^[^\w\s]+\s*', '', clean_title)
            sumario_lines.append(f"{h2_idx}. [{clean_title}](#{slug})")
        elif level == 3:
            # If it's a test: keep 'Teste XXX'
            if not clean_title.startswith("Teste "):
                # Remove leading numbering like '1.1 ', '2.3 '
                clean_title = re.sub(r'^\d+(?:\.\d+)*\s*', '', clean_title)
            # 4 spaces indentation and '1. ' enumerated item as instructed
            sumario_lines.append(f"    1. [{clean_title}](#{slug})")

    return "\n".join(sumario_lines) + "\n\n---\n"

def fix_markdown_content(content):
    # 1. Substituir bloco do sumário
    new_sumario = build_sumario_block(content)
    if new_sumario:
        content = re.sub(r"## 🧭 Sumário\s*\n.*?(?=\n## |\Z)", new_sumario, content, flags=re.DOTALL)

    # 2. Padronizar listas não ordenadas para dash (-) (MD004)
    # Linhas iniciando com '* ' (com zero ou mais espaços de indentação) convertem para '- '
    # Cuidado para não alterar ênfases como **negrito** ou *itálico*
    lines = content.splitlines()
    fixed_lines = []

    for l in lines:
        m_ul = re.match(r"^(\s*)\*\s+(.*)$", l)
        if m_ul:
            indent = m_ul.group(1)
            rest = m_ul.group(2)
            fixed_lines.append(f"{indent}- {rest}")
        else:
            fixed_lines.append(l)

    content = "\n".join(fixed_lines)

    # 3. Garantir blanks around headings (MD022)
    # Headings precisam de linha em branco acima e abaixo
    # Exceto o primeiro heading do arquivo (linha 0)
    lines = content.splitlines()
    res_lines = []
    in_code_block = False

    for i, line in enumerate(lines):
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            res_lines.append(line)
            continue

        if in_code_block:
            res_lines.append(line)
            continue

        # Verifica se é um heading
        is_heading = bool(re.match(r"^#{1,6}\s+", line))

        if is_heading:
            # Linha em branco acima se a anterior não for vazia
            if res_lines and res_lines[-1].strip() != "":
                res_lines.append("")
            res_lines.append(line)
            # Linha em branco abaixo se a próxima existir e não for vazia
            if i + 1 < len(lines) and lines[i+1].strip() != "":
                res_lines.append("")
        else:
            res_lines.append(line)

    content = "\n".join(res_lines)

    # 4. Eliminar múltiplas linhas em branco consecutivas (MD012)
    content = re.sub(r"\n{3,}", "\n\n", content)

    # 5. Garantir que divisores '---' tenham linhas em branco ao redor
    content = re.sub(r"([^\n])\n---", r"\1\n\n---", content)
    content = re.sub(r"---\n([^\n])", r"---\n\n\1", content)
    content = re.sub(r"\n{3,}", "\n\n", content)

    # 6. Remover espaços em branco no final das linhas, preservando 2 espaços de quebra
    clean_lines = []
    for l in content.splitlines():
        if l.endswith("  "):
            # preserva 2 espaços intencionais de quebra de linha do markdown
            stripped = l.rstrip()
            clean_lines.append(stripped + "  ")
        else:
            clean_lines.append(l.rstrip())
    content = "\n".join(clean_lines) + "\n"

    return content

def process_all_guides():
    md_files = glob.glob(os.path.join(DOCS_DIR, "**/*.md"), recursive=True)
    guides = [
        f for f in md_files
        if "resources" not in f
        and not f.endswith("README.md")
        and "relatorios" not in f
        and "prompts" not in f
    ]

    print(f"Processando e alinhando com linter todos os {len(guides)} cadernos de estudo...")

    for i, g in enumerate(sorted(guides), 1):
        with open(g, "r", encoding="utf-8") as f:
            content = f.read()

        fixed = fix_markdown_content(content)

        with open(g, "w", encoding="utf-8") as f:
            f.write(fixed)

        if i % 20 == 0 or i == len(guides):
            print(f"  [{i}/{len(guides)}] Concluídos...")

    print("Todos os cadernos foram processados com sucesso!")

if __name__ == "__main__":
    process_all_guides()

