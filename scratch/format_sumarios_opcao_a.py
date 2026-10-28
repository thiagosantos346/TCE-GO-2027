# -*- coding: utf-8 -*-
"""
Formata todos os sumários dos 119 arquivos Markdown para a Opção A:
Hierarquia ordenada Markdown progressiva:
1. [Item Maior A](#...)
    1. [Subtópico 1](#...)
    2. [Subtópico 2](#...)
    3. [Teste 001](#...)
2. [Item Maior B](#...)
    1. [Subtópico 1](#...)
    2. [Teste 002](#...)
"""

import os
import re
import sys
import build_all_guides

def format_sumario_opcao_a(fpath):
    with open(fpath, "r", encoding="utf-8") as f:
        text = f.read()

    # Localizar sumário
    m = re.search(r'## 🧭 (?:Sumário Interativo|Sumário)\s*\n(.*?)(?=\n---\s*\n## |\n## 📖|\n## \d|\n## 🌐)', text, re.DOTALL)
    if not m:
        return False, "Sumário não encontrado"

    sum_block = m.group(1)
    lines = sum_block.splitlines()

    new_lines = []
    h2_counter = 0
    h3_counter = 0

    for line in lines:
        if not line.strip():
            continue
        # Detectar indentação e link
        m_link = re.match(r'^(\s*)(?:\d+\.|\-)\s*(\[.*?\]\(#.*?\))', line)
        if not m_link:
            # caso seja texto sem link
            continue
        indent = len(m_link.group(1))
        link = m_link.group(2)

        if indent == 0:
            h2_counter += 1
            h3_counter = 0
            new_lines.append(f"{h2_counter}. {link}")
        else:
            h3_counter += 1
            new_lines.append(f"    {h3_counter}. {link}")

    new_sum_text = "\n".join(new_lines)

    # Substituir no arquivo
    head = text[:m.start()]
    tail = text[m.end():]
    new_text = f"{head}## 🧭 Sumário\n\n{new_sum_text}\n\n{tail.lstrip()}"

    if new_text != text:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_text)
        return True, f"Sumário formatado: {h2_counter} itens maiores, subitens ordenados progressivamente."
    return False, "Já formatado."

if __name__ == "__main__":
    all_fs = []
    for m in build_all_guides.ALL_MODULES:
        d = m['dir']
        fs = [os.path.join(d, f) for f in os.listdir(d) if f.endswith('.md') and not f.lower().startswith('readme')]
        all_fs.extend(fs)

    print(f"Formatando sumários na Opção A em {len(all_fs)} arquivos...")
    mod_count = 0
    for f in all_fs:
        ok, msg = format_sumario_opcao_a(f)
        if ok:
            mod_count += 1
            print(f"[OK] {os.path.basename(f)}: {msg}")
        else:
            print(f"[SKIP] {os.path.basename(f)}: {msg}")

    print(f"\nFinalizado! {mod_count}/{len(all_fs)} sumários atualizados.")

