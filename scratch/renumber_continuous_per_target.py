# -*- coding: utf-8 -*-
"""
Script de Renumeração Global Contínua de Testes por Caderno / Volume
Renumera os testes (### Teste 001 até Teste N) de forma estritamente sequencial:
  - Volume 1: Conhecimentos Gerais (Módulos 01 a 03) -> Teste 001 a Teste 181
  - Volume 2: Técnico Administrativo (Módulos 15 a 25) -> Teste 001 a Teste 469
  - Volume 3: Técnico de TI (Módulos 04 a 14) -> Teste 001 a Teste 594
Atualiza tanto o cabeçalho '### Teste XXX' quanto os links do Sumário '[Teste XXX](#Teste-XXX)'.
"""

import os
import re
import sys
import build_all_guides

def renumber_file_tests(fpath, start_num):
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Localizar testes existentes no arquivo
    matches = list(re.finditer(r'^###\s+Teste\s+(\d+)', text, flags=re.MULTILINE))
    num_tests = len(matches)
    if num_tests == 0:
        return 0

    # Construir mapa de substituição ordenado
    test_map = {}
    for i, m in enumerate(matches):
        old_num = int(m.group(1))
        new_num = start_num + i
        old_id = f"Teste {old_num:03d}"
        new_id = f"Teste {new_num:03d}"
        old_anc = f"#Teste-{old_num:03d}"
        new_anc = f"#Teste-{new_num:03d}"
        test_map[old_id] = new_id
        test_map[old_anc] = new_anc

    # 1. Substituir cabeçalhos ### Teste XXX
    def repl_heading(m):
        old_num = int(m.group(1))
        old_id = f"Teste {old_num:03d}"
        new_id = test_map.get(old_id, old_id)
        return f"### {new_id}"

    text = re.sub(r'^###\s+Teste\s+(\d+)', repl_heading, text, flags=re.MULTILINE)

    # 2. Substituir links no Sumário [Teste XXX](#Teste-XXX)
    def repl_sum_link(m):
        old_num = int(m.group(1))
        old_id = f"Teste {old_num:03d}"
        new_id = test_map.get(old_id, old_id)
        old_anc = f"#Teste-{old_num:03d}"
        new_anc = test_map.get(old_anc, old_anc)
        return f"[{new_id}]({new_anc})"

    text = re.sub(r'\[Teste\s+(\d+)\]\(#Teste-\d+\)', repl_sum_link, text)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(text)

    return num_tests

def run_global_renumbering():
    targets = ['conhecimentos_gerais', 'tecnico_administrativo', 'tecnico_ti']

    total_all_targets = 0
    for target in targets:
        cfg = build_all_guides.TARGETS[target]
        print(f"\n==================================================")
        print(f"Renumeração Global para: {target.upper()}")
        print(f"==================================================")

        current_q = 0
        file_count = 0
        for mid in cfg['module_ids']:
            m = build_all_guides.MODULES_BY_ID[mid]
            fs = sorted([f for f in os.listdir(m['dir']) if f.endswith('.md') and not f.lower().startswith('readme')])
            file_count += len(fs)
            for f in fs:
                fpath = os.path.join(m['dir'], f)
                count = renumber_file_tests(fpath, current_q + 1)
                start_range = current_q + 1
                end_range = current_q + count
                current_q += count
                print(f"  [{m['num']}] {f[:42]:42s} -> Teste {start_range:03d} a Teste {end_range:03d} ({count:2d} testes)")

        print(f">> Total em {target}: {current_q} testes contínuos em {file_count} arquivos (1 a {current_q}).")
        total_all_targets += current_q

    print(f"\nConcluído! Total global de testes renumerados: {total_all_targets}")

if __name__ == "__main__":
    run_global_renumbering()

