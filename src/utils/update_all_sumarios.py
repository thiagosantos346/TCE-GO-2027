#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Atualiza e sincroniza todos os índices (## 🧭 Sumário) em todos os cadernos de estudo Markdown em docs/
"""

import os
import glob
import re
import unicodedata

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DOCS_DIR = os.path.join(BASE_DIR, "docs")

def normalize_slug(text):
    """Gera slug idêntico ao build_all_guides.py para garantir 100% de precisão nos links."""
    text = re.sub(r'[\*`\$]', '', text)
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '-', text).strip('-')
    return text or "sec"

def build_sumario_for_file(content):
    # Find all H2 and H3 headings after '## 🧭 Sumário' or after ementa
    lines = content.splitlines()
    headings = [] # list of (level, text, line_num)

    in_sumario = False
    past_sumario = False

    for i, line in enumerate(lines):
        if line.startswith("## 🧭 Sumário"):
            in_sumario = True
            continue
        if in_sumario and line.startswith("## "):
            in_sumario = False
            past_sumario = True

        if past_sumario:
            if line.startswith("## "):
                htext = line[3:].strip()
                headings.append((2, htext))
            elif line.startswith("### "):
                htext = line[4:].strip()
                headings.append((3, htext))

    if not headings:
        return None

    # Track used slugs to handle duplicate titles if any
    used_slugs = {}
    
    # Pre-calculate slugs for each heading in the file order
    heading_slugs = []
    for level, text in headings:
        base_slug = normalize_slug(text)
        if base_slug in used_slugs:
            used_slugs[base_slug] += 1
            slug = f"{base_slug}-{used_slugs[base_slug]}"
        else:
            used_slugs[base_slug] = 1
            slug = base_slug
        heading_slugs.append((level, text, slug))

    # Build markdown sumario
    sumario_lines = ["## 🧭 Sumário\n"]
    current_h2_idx = 0

    for level, text, slug in heading_slugs:
        # Clean text for display in link
        clean_text = re.sub(r'[\*`\$]', '', text).strip()
        if level == 2:
            # Check if text starts with a number like "1. " or "2. "
            m_num = re.match(r'^(\d+)\.\s+(.*)$', clean_text)
            if m_num:
                num_str = m_num.group(1)
                title_str = m_num.group(2)
                sumario_lines.append(f"{num_str}. [{title_str}](#{slug})")
            else:
                current_h2_idx += 1
                sumario_lines.append(f"{current_h2_idx}. [{clean_text}](#{slug})")
        elif level == 3:
            # Sub-item
            sumario_lines.append(f"    - [{clean_text}](#{slug})")

    return "\n".join(sumario_lines) + "\n\n---\n"

def update_guide(fpath):
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Locate '## 🧭 Sumário' and the next '## '
    pattern = r"(## 🧭 Sumário\s*\n.*?)(?=\n## |\Z)"
    m = re.search(pattern, content, re.DOTALL)
    if not m:
        return False, "Sem bloco Sumário"

    new_sumario = build_sumario_for_file(content)
    if not new_sumario:
        return False, "Nenhum heading encontrado para gerar Sumário"

    # Replace old sumario with new
    old_block = m.group(1)
    # Ensure separator after sumario
    new_content = content[:m.start()] + new_sumario + content[m.end():]
    
    # Clean up double dividers if any
    new_content = re.sub(r'(---\s*\n\s*)+---', '---', new_content)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(new_content)

    return True, "Atualizado"

def main():
    md_files = glob.glob(os.path.join(DOCS_DIR, "**/*.md"), recursive=True)
    guides = [
        f for f in md_files
        if "resources" not in f
        and not f.endswith("README.md")
        and "relatorio" not in f
        and "prompts" not in f
    ]

    print(f"Atualizando índices (Sumário) em {len(guides)} cadernos de estudo...")
    updated = 0
    failed = 0

    for g in sorted(guides):
        ok, msg = update_guide(g)
        rel = os.path.relpath(g, BASE_DIR).replace("\\", "/")
        if ok:
            updated += 1
        else:
            failed += 1
            print(f"  [AVISO] {rel}: {msg}")

    print(f"Concluído: {updated} cadernos atualizados com sucesso, {failed} falhas.")

if __name__ == "__main__":
    main()
