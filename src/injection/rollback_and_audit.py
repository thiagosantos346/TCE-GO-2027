#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/rollback_and_audit.py

FASE 1: Auditoria Semântica 1:1 e Rollback via Git.
Varre todos os 119 arquivos .md nas pastas:
- conhecimentos_gerais
- conhecimentos_especificos_a01_tecnico_administrativo
- conhecimentos_especificos_b02_ti

Identifica questões intrusas/desconexas (com template genérico do mass_injector ou comentários incongruentes)
e restaura via Git (git show 6a1eac1:<arquivo>) o bloco Markdown completo e aderente que ocupava aquele lugar.
Preserva com rigor as 212 questões reais legítimas, auditadas e comprovadamente aderentes.
"""

import os
import glob
import re
import subprocess
import json

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
DOCS_DIR = os.path.join(BASE_DIR, 'docs')
GIT_BASE_COMMIT = '6a1eac1'

def normalize_path(p):
    return p.replace('\\', '/')

def extract_test_blocks_with_spans(content):
    matches = list(re.finditer(r'^### Teste (\d+)', content, re.MULTILINE))
    blocks = []
    for i, m in enumerate(matches):
        num = m.group(1)
        start = m.start()
        next_pos = matches[i+1].start() if i+1 < len(matches) else len(content)
        sec = re.search(r'\n## ', content[m.end():next_pos])
        if sec:
            end = m.end() + sec.start() + 1
        else:
            end = next_pos
        blocks.append({
            'num': num,
            'start': start,
            'end': end,
            'block': content[start:end]
        })
    return blocks

def is_intrusive_question(num, path, block):
    # 1. Comentários genéricos falsos produzidos pelo mass_injector.py
    if 'Discrepa das diretrizes normativas e jurisprudenciais' in block:
        return True, 'Template genérico do mass_injector (900cf56)'
    if 'Trata-se da opção que expressa com exatidão o regramento da matéria na ótica da banca' in block:
        return True, 'Template genérico do mass_injector (900cf56)'

    # 2. Incongruências pontuais identificadas na auditoria
    if num in ['078', '079'] and '01_conjuntos' in path:
        return True, 'Conflito de comentário / Matéria estranha no subitem'

    # 3. Questões de engenharia civil/sanitária ou mecânica que porventura tenham sobrado
    if re.search(r'\b(viga biapoiada|classificação dos solos em argila|lagoas? de estabilização|termodinâmica)\b', block, re.I):
        return True, 'Assunto de Engenharia fora do escopo'

    return False, 'Aderente/Legítima'

def run():
    print("Iniciando Fase 1: Auditoria Semântica e Rollback via Git...")

    md_files = glob.glob(os.path.join(DOCS_DIR, '**/*.md'), recursive=True)
    md_files = [f for f in md_files if 'resources' not in f and not f.endswith('README.md') and not f.endswith('relatorio_cobertura_questoes.md')]

    total_files = len(md_files)
    print(f"Total de arquivos para auditar: {total_files}")

    total_tests_audited = 0
    total_reverted = 0
    total_kept_real = 0
    total_kept_sim = 0

    audit_log = []

    for fpath in sorted(md_files):
        norm_path = normalize_path(fpath)
        # Caminho relativo ao projeto para buscar no git antigo sob fontes_de_estudo/
        rel_to_docs = normalize_path(os.path.relpath(fpath, DOCS_DIR))
        git_path = f"fontes_de_estudo/{rel_to_docs}"

        with open(fpath, 'r', encoding='utf-8') as f:
            curr_content = f.read()

        # Obter a versão limpa de referência via Git
        cmd = ['git', 'show', f'{GIT_BASE_COMMIT}:{git_path}']
        res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
        if res.returncode != 0:
            print(f"ERRO ao obter versão Git para {norm_path}: {res.stderr}")
            continue

        base_content = res.stdout
        base_blocks = {b['num']: b['block'] for b in extract_test_blocks_with_spans(base_content)}

        curr_blocks = extract_test_blocks_with_spans(curr_content)
        
        # Processar blocos de trás para frente para preservar índices de substituição
        modified_content = curr_content
        file_reverted_count = 0

        for b_info in sorted(curr_blocks, key=lambda x: x['start'], reverse=True):
            num = b_info['num']
            start = b_info['start']
            end = b_info['end']
            block_text = b_info['block']

            total_tests_audited += 1

            intrusive, reason = is_intrusive_question(num, norm_path, block_text)

            if intrusive:
                # Extrair o bloco de teste do commit 6a1eac1
                if num in base_blocks:
                    restored_block = base_blocks[num]
                    # Substituir no texto do arquivo atual
                    modified_content = modified_content[:start] + restored_block + modified_content[end:]
                    total_reverted += 1
                    file_reverted_count += 1
                    audit_log.append({
                        'path': norm_path,
                        'num': num,
                        'action': 'REVERTED_VIA_GIT',
                        'reason': reason,
                        'restored_source': GIT_BASE_COMMIT
                    })
                else:
                    print(f"AVISO: Teste {num} não encontrado no commit base {GIT_BASE_COMMIT} para {norm_path}!")
            else:
                if 'Simulada' in block_text or 'Inédita' in block_text:
                    total_kept_sim += 1
                    action = 'KEPT_SIMULATED'
                else:
                    total_kept_real += 1
                    action = 'KEPT_REAL'
                audit_log.append({
                    'path': norm_path,
                    'num': num,
                    'action': action,
                    'reason': reason
                })

        if file_reverted_count > 0:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(modified_content)

    print("=" * 70)
    print("RELATÓRIO DA FASE 1 (AUDITORIA E ROLLBACK VIA GIT):")
    print(f"Total de arquivos auditados: {total_files}")
    print(f"Total de testes auditados: {total_tests_audited}")
    print(f"Total de questões intrusas revertidas via Git: {total_reverted}")
    print(f"Total de questões reais legítimas mantidas: {total_kept_real}")
    print(f"Total de questões simuladas mantidas: {total_kept_sim}")
    print("=" * 70)

    log_file = os.path.join(DOCS_DIR, 'audit_execution_log.json')
    with open(log_file, 'w', encoding='utf-8') as f:
        json.dump(audit_log, f, ensure_ascii=False, indent=2)

    print(f"Log detalhado salvo em {log_file}.")

if __name__ == '__main__':
    run()

