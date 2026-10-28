# -*- coding: utf-8 -*-
"""
Script de Padronização Global dos Guias de Estudo TCE-GO
Aplica com máxima precisão as regras extraídas do arquivo modelo:
1. Renomeação de '### Questão XX' para '### Teste 00X' com extração limpa de banca.
2. Inserção de linha divisória '---' antes de cada '> **Comentário Detalhado:**'.
3. Inserção de linha divisória dupla '--- \n---' em torno de Ementa, Sumário e antes de cada seção principal (##).
4. Reestruturação do Sumário:
   - Lista ordenada Markdown ('1. [Título](#...)', '    1. [Subtítulo](#...)').
   - Inclusão dos Testes no sumário ('    1. [Teste 00X](#Teste-00X)') posicionados exatamente sob seus tópicos.
5. Preservação estrita de 100% da teoria, Mermaid, fórmulas KaTeX e metadados.
"""

import os
import re
import sys
import unicodedata
import build_all_guides

def generate_anchor(text):
    s = text.lower().strip()
    s = ''.join(c for c in unicodedata.normalize('NFKD', s) if not unicodedata.combining(c))
    anc = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return f"#{anc}"

def standardize_file(fpath):
    # Arquivo modelo já está 100% no padrão novo
    if fpath.endswith("01_compreensao_e_interpretacao_de_texto.md"):
        return False, "Arquivo modelo (ignorado)"

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    orig_content = content

    # 1. Extração do Sumário Atual e Mapeamento de Âncoras Existentes
    # Padrão: ## 🧭 (Sumário|Sumário Interativo)
    sum_m = re.search(r'## 🧭 (?:Sumário Interativo|Sumário)\s*\n(.*?)(?=\n---\s*\n## |\n## 📖|\n## \d|\n## 🌐|\n## [A-ZÁÉÍÓÚ])', content, re.DOTALL)
    if not sum_m:
        return False, f"Sumário não localizado em {os.path.basename(fpath)}"

    existing_sum_text = sum_m.group(1)
    anchor_map = {}
    for line in existing_sum_text.splitlines():
        lm = re.search(r'\[([^\]]+)\]\((#[^\)]+)\)', line)
        if lm:
            txt = lm.group(1).strip()
            anc = lm.group(2).strip()
            anchor_map[txt] = anc
            clean = re.sub(r'^\d+(\.\d+)*\s*', '', txt).strip()
            anchor_map[clean] = anc
            no_emoji = re.sub(r'^[^\w\s]+\s*', '', clean).strip()
            anchor_map[no_emoji] = anc

    # 2. Processar Cabeçalhos de Questões -> Teste 00X
    # Tratar casos onde a banca está no cabeçalho: ### Questão 03 (FCC - ...)
    q_counter = 0
    def repl_question_header(m):
        nonlocal q_counter
        q_counter += 1
        num_str = f"Teste {q_counter:03d}"
        extra = m.group(1).strip()
        if extra:
            clean_banca = extra
            if clean_banca.startswith("(") and clean_banca.endswith(")"):
                clean_banca = f"**{clean_banca}**"
            elif not clean_banca.startswith("**"):
                clean_banca = f"**({clean_banca})**"
            return f"### {num_str}\n{clean_banca}"
        else:
            return f"### {num_str}"

    content = re.sub(r'^###\s+(?:Questão|Questao|Teste)\s+\d+(.*?)$', repl_question_header, content, flags=re.MULTILINE)

    # 3. Inserção de '---' antes de '> **Comentário Detalhado:**' se não houver
    content = re.sub(
        r'(?<!\n---\n)(?<!\n---\s\n)\n([ \t]*>[ \t]*\*\*Comentário Detalhado:\*\*)',
        r'\n\n---\n\n\1',
        content
    )

    # 4. Reconstrução do Sumário Interativo Ordenado com Testes
    # Re-localizar onde termina o Sumário
    sum_m = re.search(r'## 🧭 (?:Sumário Interativo|Sumário)\s*\n(.*?)(?=\n---\s*\n## |\n## 📖|\n## \d|\n## 🌐|\n## [A-ZÁÉÍÓÚ])', content, re.DOTALL)
    body_content = content[sum_m.end():]

    # Parse dos tokens do corpo (H2, H3, TESTE, FONTES)
    body_tokens = []
    teste_idx = 0
    for line in body_content.splitlines():
        if line.startswith("## "):
            t = line[3:].strip()
            if "fontes" in t.lower() or "referências" in t.lower():
                body_tokens.append(("FONTES", t))
            elif "resumo teórico" in t.lower() or "conteúdo teórico" in t.lower():
                # Manter como H2 estrutural se presente
                body_tokens.append(("H2", t))
            else:
                body_tokens.append(("H2", t))
        elif re.match(r'^###\s+Teste\s+\d+', line):
            teste_idx += 1
            body_tokens.append(("TESTE", f"Teste {teste_idx:03d}", f"#Teste-{teste_idx:03d}"))
        elif line.startswith("### "):
            t = line[4:].strip()
            body_tokens.append(("H3", t))

    # Construir linhas do novo sumário
    new_sum_lines = []
    for tok in body_tokens:
        tok_type = tok[0]
        if tok_type in ("H2", "FONTES"):
            title = tok[1]
            clean_title = re.sub(r'^\d+(\.\d+)*\s*', '', title).strip()
            clean_title_no_emoji = re.sub(r'^[^\w\s]+\s*', '', clean_title).strip()
            anc = anchor_map.get(title) or anchor_map.get(clean_title) or anchor_map.get(clean_title_no_emoji)
            if not anc:
                anc = generate_anchor(clean_title_no_emoji)
            new_sum_lines.append(f"1. [{clean_title_no_emoji}]({anc})")
        elif tok_type == "H3":
            title = tok[1]
            clean_title = re.sub(r'^\d+(\.\d+)*\s*', '', title).strip()
            clean_title_no_emoji = re.sub(r'^[^\w\s]+\s*', '', clean_title).strip()
            anc = anchor_map.get(title) or anchor_map.get(clean_title) or anchor_map.get(clean_title_no_emoji)
            if not anc:
                anc = generate_anchor(clean_title_no_emoji)
            new_sum_lines.append(f"    1. [{clean_title_no_emoji}]({anc})")
        elif tok_type == "TESTE":
            new_sum_lines.append(f"    1. [{tok[1]}]({tok[2]})")

    new_sumario_block = "\n".join(new_sum_lines)

    # 5. Substituir o bloco do sumário no conteúdo
    head_content = content[:sum_m.start()]
    tail_content = content[sum_m.end():]

    # Assegurar cabeçalho padronizado '## 🧭 Sumário'
    content = f"{head_content}## 🧭 Sumário\n\n{new_sumario_block}\n\n{tail_content.lstrip()}"

    # 6. Padronizar Divisórias Duplas ('--- \n---')
    # a) Antes da Ementa:
    content = re.sub(r'(?:\n---\s*)+\n+(## 📌 Ementa)', r'\n\n---\n--- \n\n\1', content)
    # b) Antes do Sumário (após a Ementa):
    content = re.sub(r'(?:\n---\s*)+\n+(## 🧭 Sumário)', r'\n\n---\n---\n\n\1', content)
    # c) Depois do Sumário (antes do primeiro ##):
    content = re.sub(r'(\[.*?\]\(#.*?\)\n+)(?:\n---\s*)*\n+(## (?:[0-9]|📖|🌐|[A-ZÁÉÍÓÚ]))', r'\1\n---\n---\n\n\2', content)
    # d) Antes de cada ## principal subsequente (## 2., ## 3., ## 🌐, etc):
    def repl_h2_div(m):
        return f"\n\n---\n---\n\n{m.group(1)}"
    content = re.sub(r'(?:\n---\s*)*\n+(## (?:[0-9]+\.|🌐|Fontes|Referências)[^\n]*)', repl_h2_div, content)

    # Limpeza de múltiplos '---' acidentais (mais de 2 seguidos)
    content = re.sub(r'(\n---\s*){3,}', r'\n---\n--- \n', content)

    if content != orig_content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        return True, f"Padronizado: {q_counter} testes, sumário reconstruído."
    else:
        return False, "Nenhuma alteração necessária."

if __name__ == "__main__":
    all_fs = []
    for m in build_all_guides.ALL_MODULES:
        d = m['dir']
        fs = [os.path.join(d, f) for f in os.listdir(d) if f.endswith('.md') and not f.lower().startswith('readme')]
        all_fs.extend(fs)

    print(f"Iniciando padronização em {len(all_fs)} arquivos...")
    modified = 0
    for fpath in all_fs:
        changed, msg = standardize_file(fpath)
        if changed:
            modified += 1
            print(f"[OK] {os.path.basename(fpath)}: {msg}")
        else:
            print(f"[SKIP] {os.path.basename(fpath)}: {msg}")

    print(f"\nFinalizado! Total de arquivos modificados: {modified}/{len(all_fs)}")

