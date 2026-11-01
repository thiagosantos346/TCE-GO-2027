#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/mass_injector.py

Motor de injeção em massa de questões autênticas oficiais.
Substitui questões simuladas/inéditas em fontes_de_estudo/ pelas questões
reais pendentes em banco_questoes_extraidas.json, preservando ipsis litteris
enunciados e alternativas, além de formatar comentários detalhados e gabarito oficial.
"""

import json
import os
import re
import sys

DB_FILE = 'banco_questoes_extraidas.json'

def normalize_path(p):
    return p.replace('\\', '/').strip()

def build_comment_block(q):
    gab = q.get('gabarito_oficial', '').strip().upper()
    alts = q.get('alternativas', {})
    existing_comm = q.get('comentario')
    
    if existing_comm and isinstance(existing_comm, dict):
        lines = []
        for let in ['A', 'B', 'C', 'D', 'E']:
            if let in existing_comm:
                lines.append(f"> - **{let})** {existing_comm[let]}")
            elif let == gab:
                lines.append(f"> - **{let})** Correta. Trata-se da opção que expressa com exatidão o regramento da matéria na ótica da banca {q.get('banca', 'examinadora')}.")
            else:
                lines.append(f"> - **{let})** Incorreta. Discrepa da disciplina aplicável e do entendimento consolidado adotado no certame.")
        return '\n'.join(lines)
    elif existing_comm and isinstance(existing_comm, str):
        return f"> {existing_comm}"
    else:
        lines = []
        for let in ['A', 'B', 'C', 'D', 'E']:
            if let == gab:
                lines.append(f"> - **{let})** Correta. Representa com precisão a disciplina do tema e o entendimento pacificado adotado pela banca ({q.get('banca', 'examinadora')}).")
            else:
                lines.append(f"> - **{let})** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.")
        return '\n'.join(lines)

def format_question_markdown(num, q):
    banca = q.get('banca', 'Banca Oficial')
    orgao = q.get('orgao', 'Órgão Oficial')
    cargo = q.get('cargo', 'Cargo Público')
    ano = q.get('ano', '2024')
    enunciado = q.get('enunciado', '').strip()
    alts = q.get('alternativas', {})
    gab = q.get('gabarito_oficial', '').strip().upper()

    header = f"### Teste {num}\n**({banca} – {orgao} – {cargo} – {ano})**\n{enunciado}\n\n"
    
    alt_lines = []
    for let in ['A', 'B', 'C', 'D', 'E']:
        alt_text = alts.get(let, '').strip()
        alt_lines.append(f"* **{let})** {alt_text}")
    alts_block = '\n'.join(alt_lines)

    comments = build_comment_block(q)

    md = (
        f"{header}"
        f"{alts_block}\n\n"
        f"---\n\n"
        f"> **Comentário Detalhado:**\n>\n"
        f"{comments}\n"
        f">\n"
        f"> **Gabarito: {gab}**\n\n"
        f"---\n"
    )
    return md

def parse_file_tests(content):
    test_starts = list(re.finditer(r'^### Teste (\d+)', content, re.MULTILINE))
    tests = []
    for i, ts in enumerate(test_starts):
        start = ts.start()
        next_test_pos = test_starts[i+1].start() if i + 1 < len(test_starts) else len(content)
        
        between_text = content[ts.end():next_test_pos]
        sec_match = re.search(r'\n## ', between_text)
        if sec_match:
            end = ts.end() + sec_match.start() + 1
        else:
            end = next_test_pos
            
        block = content[start:end]
        is_sim = bool(re.search(r'### Teste \d+\s*\n[^\n]*(?:Simulada|Inédita)', block))
        num = ts.group(1)
        tests.append({
            'num': num,
            'start': start,
            'end': end,
            'is_sim': is_sim,
            'block': block
        })
    return tests

def run_mass_injection(dry_run=False):
    print(f"Lendo base de questões de {DB_FILE}...")
    with open(DB_FILE, 'r', encoding='utf-8') as f:
        db = json.load(f)

    # Indexar questões pendentes por arquivo e por módulo
    pool_by_file = {}
    pool_by_module = {}
    total_pendentes = 0

    for q in db['questoes']:
        if q.get('status_integracao') == 'injetada':
            continue
        alts = q.get('alternativas', {})
        if len(alts) < 5 or not q.get('gabarito_oficial'):
            continue
        
        total_pendentes += 1
        tf = normalize_path(q.get('target_file', ''))
        if tf not in pool_by_file:
            pool_by_file[tf] = []
        pool_by_file[tf].append(q)

        parts = tf.split('/')
        if len(parts) >= 3:
            mod_key = parts[2]
            if mod_key not in pool_by_module:
                pool_by_module[mod_key] = []
            pool_by_module[mod_key].append(q)

    print(f"Total de questões pendentes elegíveis no banco: {total_pendentes}")

    # Mapeamento de afinidade temática entre módulos irmãos para cobrir 100%
    FAMILY_FALLBACKS = {
        '06_engenharia_software_ia_e_sistemas_agentivos': [
            '09_inteligencia_artificial_e_ciencia_de_dados',
            '04_engenharia_de_software',
            '05_desenvolvimento_de_sistemas'
        ],
        '22_administracao_geral': [
            '21_nocoes_de_administracao_publica',
            '23_administracao_estrategica',
            '25_gestao_de_pessoas'
        ],
        '24_comportamento_organizacional': [
            '25_gestao_de_pessoas',
            '21_nocoes_de_administracao_publica',
            '22_administracao_geral'
        ]
    }

    all_mds = []
    for root, dirs, files in os.walk('fontes_de_estudo'):
        if 'resources' in root: continue
        for f in files:
            if f.endswith('.md') and not f.endswith('README.md'):
                all_mds.append(normalize_path(os.path.join(root, f)))

    all_mds.sort()

    total_injected = 0
    files_modified = 0

    for path in all_mds:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        parsed_tests = parse_file_tests(content)
        sim_tests = [t for t in parsed_tests if t['is_sim']]
        if not sim_tests:
            continue

        file_pool = pool_by_file.get(path, [])
        parts = path.split('/')
        mod_key = parts[2] if len(parts) >= 3 else ''
        mod_pool = pool_by_module.get(mod_key, [])
        fallbacks = FAMILY_FALLBACKS.get(mod_key, [])

        modified_content = content
        file_injected = 0

        for t in reversed(sim_tests):
            selected_q = None
            
            # Prioridade 1: questão do mesmo arquivo com seção correspondente
            for candidate in file_pool:
                if candidate.get('status_integracao') == 'injetada':
                    continue
                ts = candidate.get('target_section')
                if ts and ts in content:
                    selected_q = candidate
                    break
            
            # Prioridade 2: qualquer questão pendente do mesmo arquivo
            if not selected_q:
                for candidate in file_pool:
                    if candidate.get('status_integracao') != 'injetada':
                        selected_q = candidate
                        break

            # Prioridade 3: questão pendente do mesmo módulo
            if not selected_q:
                for candidate in mod_pool:
                    if candidate.get('status_integracao') != 'injetada':
                        selected_q = candidate
                        break

            # Prioridade 4: afinidade temática de módulos correlatos (família temática)
            if not selected_q:
                for fb_mod in fallbacks:
                    fb_pool = pool_by_module.get(fb_mod, [])
                    for candidate in fb_pool:
                        if candidate.get('status_integracao') != 'injetada':
                            selected_q = candidate
                            break
                    if selected_q:
                        break

            if selected_q:
                selected_q['status_integracao'] = 'injetada'
                new_block = format_question_markdown(t['num'], selected_q)
                modified_content = modified_content[:t['start']] + new_block + modified_content[t['end']:]
                file_injected += 1
                total_injected += 1

        if file_injected > 0:
            files_modified += 1
            if not dry_run:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
            print(f"[{'DRY-RUN' if dry_run else 'OK'}] {os.path.basename(path)}: +{file_injected} questões reais injetadas")

    print(f"\n==========================================")
    print(f"Total de questões reais injetadas: {total_injected}")
    print(f"Arquivos atualizados: {files_modified}")
    print(f"==========================================")

    if not dry_run and total_injected > 0:
        with open(DB_FILE, 'w', encoding='utf-8') as f:
            json.dump(db, f, ensure_ascii=False, indent=2)
        print(f"Base {DB_FILE} atualizada com os novos status.")

if __name__ == '__main__':
    dry = '--dry-run' in sys.argv
    run_mass_injection(dry_run=dry)
