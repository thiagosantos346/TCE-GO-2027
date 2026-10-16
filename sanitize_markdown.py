# -*- coding: utf-8 -*-
"""
FASE 1: Higienização Global dos Arquivos Markdown (sanitize_markdown.py)
Varre e corrige in-place TODOS os arquivos .md dentro de:
  - fontes_de_estudo/conhecimentos_gerais
  - fontes_de_estudo/conhecimentos_especificos_b02_ti
  - fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo

Preserva 100% dos emoticons e símbolos Unicode.
"""

import os
import re
import unicodedata

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TARGET_DIRS = [
    os.path.join(BASE_DIR, "fontes_de_estudo", "conhecimentos_gerais"),
    os.path.join(BASE_DIR, "fontes_de_estudo", "conhecimentos_especificos_b02_ti"),
    os.path.join(BASE_DIR, "fontes_de_estudo", "conhecimentos_especificos_a01_tecnico_administrativo"),
]


def is_code_fence(line):
    """Verifica se a linha é início/fim de bloco de código com ou sem blockquote."""
    stripped = line.strip()
    return bool(re.match(r'^(?:>\s*)*(?:```|~~~)', stripped))


def get_list_info(s):
    """Retorna (num_spaces, list_type, marker, content) se a string for um item de lista."""
    m = re.match(r'^([ ]*)([-*+]|\d+\.)\s+(.*)$', s)
    if not m:
        return None
    sp = len(m.group(1))
    marker = m.group(2)
    ltype = 'ol' if marker[0].isdigit() else 'ul'
    return sp, ltype, marker, m.group(3)


def slugify_heading(text):
    """Normaliza título de cabeçalho para slug ASCII sem acentos e sem emojis."""
    text = re.sub(r'[\*`\$]', '', text)
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '-', text).strip('-')
    return text


def sanitize_html_and_broken_marks(content, filename):
    """
    Regra 1: Desescapar HTML (<ins>, </ins>) e corrigir marcações quebradas
    (*Texto **negrito*** -> *Texto* **negrito**) e linhas órfãs.
    """
    mods = 0
    patterns = [
        (r'\\<ins\\>', '<ins>'),
        (r'\\</ins\\>', '</ins>'),
        (r'\\&lt;ins\\&gt;', '<ins>'),
        (r'\\&lt;/ins\\&gt;', '</ins>'),
        (r'\\&lt;ins&gt;', '<ins>'),
        (r'\\&lt;/ins&gt;', '</ins>'),
        (r'&lt;ins&gt;', '<ins>'),
        (r'&lt;/ins&gt;', '</ins>'),
    ]
    for pat, repl in patterns:
        content, c = re.subn(pat, repl, content)
        mods += c

    # Cruzamentos inválidos de itálico/negrito: *Texto **negrito*** -> *Texto* **negrito**
    pattern_bi = r'(?<!\*)\*([A-Za-zÀ-ÿ0-9\s,\(\)/-]+?)\s+\*\*([^\*\n]+?)\*\*\*([;.,:]?)'
    content, c = re.subn(pattern_bi, r'*\1* **\2**\3', content)
    mods += c

    # Remover linha órfã 5.1 Critérios Cumulativos da Paráfrase Legítima (ou similar colada sem #)
    if "02_ortografia_acentuacao_e_formacao_de_palavras.md" in filename:
        orphan_pattern = r'(\n)5\.1 Critérios Cumulativos da Paráfrase Legítima\s*\n+'
        content, c = re.subn(orphan_pattern, r'\1\n', content)
        mods += c

    return content, mods


def sanitize_latex(content):
    r"""
    Regra 5: Corrigir sintaxe LaTeX/KaTeX inválida em todos os arquivos.
    - \centernot{\longleftrightarrow} -> \not\longleftrightarrow e \centernot -> \not
    - \mathbf{R\$\s*([^}]+)} -> \text{R\$ }\mathbf{\1}
    """
    mods = 0
    content, c = re.subn(r'\\centernot\{(\\longleftrightarrow)\}', r'\\not\1', content)
    mods += c
    content, c = re.subn(r'\\centernot\b', r'\\not', content)
    mods += c

    content, c = re.subn(r'\\mathbf\{R\\\$\s*([^}]+)\}', r'\\text{R\\$ }\\mathbf{\1}', content)
    mods += c
    content, c = re.subn(r'\\mathbf\{R\$\s*([^}]+)\}', r'\\text{R\\$ }\\mathbf{\1}', content)
    mods += c

    return content, mods


def sanitize_generic_titles_and_headings(lines, filename):
    """
    Regra 6: Corrigir títulos H1 genéricos nos módulos de TI, padronizar
    ### 📌 Ementa / ### 🧭 Sumário para H2 (##) e corrigir subseções de Fontes.
    """
    mods = 0
    if not lines:
        return lines, mods

    first_line = lines[0].strip()
    if re.match(r'^#\s*Módulo\s+\d+:', first_line):
        real_title = None
        remove_idx = -1
        for i in range(1, min(6, len(lines))):
            cand = lines[i].strip()
            if cand.startswith('## '):
                real_title = cand.replace('## ', '').strip()
                remove_idx = i
                break

        if not real_title:
            base = os.path.basename(filename).replace('.md', '')
            parts = base.split('_', 1)
            num = parts[0] if parts[0].isdigit() else ""
            title_text = parts[1].replace('_', ' ').title() if len(parts) > 1 else base.replace('_', ' ').title()
            real_title = f"{num} - {title_text}" if num else title_text

        real_title = re.sub(r'^(\d+)\.\s*', r'\1 - ', real_title)
        lines[0] = f"# {real_title}\n"
        if remove_idx != -1:
            lines.pop(remove_idx)
            if remove_idx < len(lines) and lines[remove_idx].strip() == "":
                lines.pop(remove_idx)
        mods += 1

    in_code = False
    in_fontes = False
    for idx, line in enumerate(lines):
        if is_code_fence(line):
            in_code = not in_code
            continue
        if in_code:
            continue

        # Padronizar ### 📌 Ementa -> ## 📌 Ementa e ### 🧭 Sumário -> ## 🧭 Sumário
        if re.match(r'^###\s+(?:📌\s*Ementa|🧭\s*Sumário)', line):
            lines[idx] = line[1:]  # ### -> ##
            mods += 1
            continue

        if re.match(r'^##\s+.*Fontes\s+(?:Recomendadas|Oficiais)', line):
            in_fontes = True
            continue
        elif re.match(r'^##\s+', line):
            in_fontes = False

        # Se dentro de ## Fontes houver ### 1. ... ou ### 2. ..., converter para #### para não conflitar com seções 1. e 2. do tópico
        if in_fontes and re.match(r'^###\s+\d+\.\s+', line):
            lines[idx] = '#' + line
            mods += 1

    return lines, mods


def unindent_fenced_code_blocks(lines):
    """
    Garante que blocos cercados ``` dentro de listas fiquem na coluna 0 com linha
    em branco antes e depois (exigência do FencedBlockPreprocessor do python-markdown).
    """
    out = []
    mods = 0
    in_code = False
    code_indent = 0

    for i, l in enumerate(lines):
        m_fence = re.match(r'^([ ]*)((?:```|~~~).*)$', l)
        if m_fence:
            if not in_code:
                in_code = True
                code_indent = len(m_fence.group(1))
                if code_indent > 0:
                    mods += 1
                if out and out[-1].strip() != '':
                    out.append('\n')
                out.append(m_fence.group(2).rstrip('\r\n') + '\n')
            else:
                in_code = False
                out.append(m_fence.group(2).rstrip('\r\n') + '\n')
                if i + 1 < len(lines) and lines[i + 1].strip() != '':
                    out.append('\n')
                code_indent = 0
            continue

        if in_code and code_indent > 0:
            if l.startswith(' ' * code_indent):
                out.append(l[code_indent:])
            else:
                out.append(l.lstrip(' '))
            continue

        out.append(l)

    return out, mods


def sanitize_embedded_enumerations(lines):
    """
    Regra 4B: Quando um parágrafo contiver enumerações embutidas na mesma linha no padrão
    ': (1) ... (2) ... (3) ...' ou 'como (a) ... (b) ... (c) ...', quebrar cada item em
    uma nova linha indentada.
    """
    new_lines = []
    mods = 0
    in_code = False

    for line in lines:
        if is_code_fence(line):
            in_code = not in_code
            new_lines.append(line)
            continue
        if in_code:
            new_lines.append(line)
            continue

        # Caso 1: item 2 com 'e (3)' residual (ex: 2. **Tools** (...) e (3) **Prompts** (...))
        m_rem3 = re.match(r'^((?:>\s*)*[ ]*)2\.\s+(.*?)\s+e\s+\(3\)\s+(.*)$', line.rstrip('\r\n'))
        if m_rem3:
            prefix, item2, item3 = m_rem3.group(1), m_rem3.group(2), m_rem3.group(3)
            new_lines.append(f"{prefix}2. {item2}\n")
            new_lines.append(f"{prefix}3. {item3}\n")
            mods += 1
            continue

        # Caso 2: 'como (a) ... (b) ... (c) ... ou (d) ...'
        if "como (a) " in line and "(b) " in line and "(c) " in line:
            bq_match = re.match(r'^(?:> ?)+', line)
            bq_prefix = bq_match.group(0) if bq_match else ""
            body = line[len(bq_prefix):].rstrip('\r\n')
            is_list_line = bool(re.match(r'^\s*(?:[-*+]|\d+\.)\s+', body))
            indent = "    " if is_list_line else ""
            parts_split = body.split("como (a) ", 1)
            intro = parts_split[0] + "como:"
            rest = parts_split[1]
            sub_parts = re.split(r'(?:[;,]\s*(?:e\s+|ou\s+)?|\s+(?:e|ou)\s+)\(([a-e])\)\s+', rest)
            items = [("a", sub_parts[0])]
            for k in range(1, len(sub_parts), 2):
                items.append((sub_parts[k], sub_parts[k + 1]))

            new_lines.append(f"{bq_prefix}{intro}\n")
            if not is_list_line:
                new_lines.append(f"{bq_prefix.rstrip()}\n" if bq_prefix else "\n")
            for lbl, itxt in items:
                new_lines.append(f"{bq_prefix}{indent}- **{lbl})** {itxt.strip()}\n")
            mods += 1
            continue

        # Caso 3: ': (1) ... (2) ...' ou ': (a) ... (b) ...'
        has_num = (": (1) " in line) and ("; (2) " in line or ", (2) " in line or "e (2) " in line)
        has_alpha = (": (a) " in line) and ("; (b) " in line or ", (b) " in line or "e (b) " in line)

        if has_num or has_alpha:
            bq_match = re.match(r'^(?:> ?)+', line)
            bq_prefix = bq_match.group(0) if bq_match else ""
            line_body = line[len(bq_prefix):].rstrip('\r\n')
            is_subitem = bool(re.match(r'^\s*(?:[-*+]|\d+\.)\s+', line_body))
            indent = "    " if is_subitem else ""

            if has_num:
                parts_split = line_body.split(': (1) ', 1)
                intro = parts_split[0] + ':'
                rest = parts_split[1]
                sub_parts = re.split(r'(?:[;,]\s*(?:e\s+|ou\s+)?|\s+(?:e|ou)\s+)\((\d+)\)\s+', rest)
                items = [("1", sub_parts[0])]
                for k in range(1, len(sub_parts), 2):
                    items.append((sub_parts[k], sub_parts[k + 1]))
            else:
                parts_split = line_body.split(': (a) ', 1)
                intro = parts_split[0] + ':'
                rest = parts_split[1]
                sub_parts = re.split(r'(?:[;,]\s*(?:e\s+|ou\s+)?|\s+(?:e|ou)\s+)\(([a-e])\)\s+', rest)
                items = [("a", sub_parts[0])]
                for k in range(1, len(sub_parts), 2):
                    items.append((sub_parts[k], sub_parts[k + 1]))

            last_lbl, last_txt = items[-1]
            trailing = ""
            m_trail = re.search(r'^(.*?\.)\s+([A-ZÁ-Ú].*)$', last_txt)
            if m_trail:
                items[-1] = (last_lbl, m_trail.group(1))
                trailing = m_trail.group(2)

            new_lines.append(f"{bq_prefix}{intro}\n")
            if not is_subitem:
                new_lines.append(f"{bq_prefix.rstrip()}\n" if bq_prefix else "\n")

            for lbl, itxt in items:
                itxt_clean = itxt.strip()
                if has_num:
                    new_lines.append(f"{bq_prefix}{indent}{lbl}. {itxt_clean}\n")
                else:
                    new_lines.append(f"{bq_prefix}{indent}- **{lbl})** {itxt_clean}\n")

            if trailing:
                new_lines.append(f"{bq_prefix.rstrip()}\n" if bq_prefix else "\n")
                new_lines.append(f"{bq_prefix}{trailing}\n")

            mods += 1
            continue

        new_lines.append(line)

    return new_lines, mods


def sanitize_options_and_romans(lines):
    """
    Regra 4A:
    - Padronizar opções de questões ('A) ...' ou '* A) ...' -> '* **A)** ...').
    - Quebrar listas de algarismos romanos ('I. ', 'II. ', 'III. ') e alíneas ('a) ', 'b) ')
      com linha em branco e '  \n' para forçar quebra de bloco real.
    """
    new_lines = []
    mods = 0
    in_code = False

    roman_re = re.compile(r'^(?:> ?)*\s*(?:I|II|III|IV|V|VI|VII|VIII|IX|X)\.\s+')
    alpha_re = re.compile(r'^(?:> ?)*\s*[a-e]\)\s+')

    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        if is_code_fence(line):
            in_code = not in_code
            new_lines.append(line)
            i += 1
            continue
        if in_code:
            new_lines.append(line)
            i += 1
            continue

        stripped = line.strip()

        # 1. Alternativas de questões fora de blockquote: 'A) ...' ou '* A) ...' ou '- A) ...'
        if not stripped.startswith('>'):
            m_opt = re.match(r'^(?:[-*]\s+)?([A-E])\)\s+(.*)$', stripped)
            if m_opt:
                letter, opt_text = m_opt.group(1), m_opt.group(2)
                if new_lines and new_lines[-1].strip() != "" and not re.match(r'^\*\s+\*\*[A-E]\)\*\*', new_lines[-1].strip()):
                    new_lines.append("\n")
                target_opt_line = f"* **{letter})** {opt_text}\n"
                if line != target_opt_line:
                    mods += 1
                new_lines.append(target_opt_line)
                i += 1
                continue

        # 2. Algarismos romanos (I., II., III.) ou alíneas (a), b), c))
        if roman_re.match(line) or alpha_re.match(line):
            m_bq = re.match(r'^(?:> ?)+', line)
            bq = m_bq.group(0) if m_bq else ""
            # Garantir linha em branco ANTES se a linha anterior não estiver vazia
            if new_lines:
                prev_clean = re.sub(r'^(?:> ?)+', '', new_lines[-1]).strip()
                if prev_clean != "":
                    new_lines.append(">\n" if bq else "\n")
                    mods += 1
            clean_line = line.rstrip('\r\n')
            if not clean_line.endswith('  '):
                clean_line += '  '
            new_lines.append(clean_line + '\n')
            # Garantir linha em branco DEPOIS se a próxima linha for outro romano/alínea ou parágrafo
            if i + 1 < n:
                next_clean = re.sub(r'^(?:> ?)+', '', lines[i + 1]).strip()
                if next_clean != "":
                    new_lines.append(">\n" if bq else "\n")
                    mods += 1
            i += 1
            continue

        new_lines.append(line)
        i += 1

    return new_lines, mods


def sanitize_list_indentation_and_blanks(lines):
    """
    Regras 2 e 3:
    - Padronizar indentação de sub-listas para múltiplos exatos de 4 espaços (tanto fora quanto dentro de blockquotes '> ').
    - Garantir linha em branco obrigatória antes de qualquer lista (fora e dentro de blockquotes).
    - Resolver listas mistas (ul <-> ol) no mesmo nível de indentação.
    """
    mods = 0

    # Passo A: Remover linha '>' vazia entre item pai e sub-lista indentada
    clean_lines = []
    i = 0
    while i < len(lines):
        if i + 2 < len(lines) and lines[i + 1].strip() in ('', '>'):
            if re.match(r'^(?:> ?)*\s*(?:[-*+]|\d+\.)\s+', lines[i]) and re.match(r'^(?:> ?)*[ ]{2,}(?:[-*+]|\d+\.)\s+', lines[i + 2]):
                clean_lines.append(lines[i])
                mods += 1
                i += 2
                continue
        clean_lines.append(lines[i])
        i += 1

    # Passo B: Padronizar indentação de sub-listas (2 ou 3 espaços -> 4 espaços; 5, 6, 7 -> 8 espaços)
    out1 = []
    in_code = False
    for l in clean_lines:
        if is_code_fence(l):
            in_code = not in_code
            out1.append(l)
            continue
        if in_code:
            out1.append(l)
            continue

        m_bq = re.match(r'^(?:> ?)+', l)
        bq = m_bq.group(0) if m_bq else ""
        # Normalizar prefixo de blockquote para '> ' se for '>' seguido de espaços
        if bq and not bq.endswith(' '):
            bq = bq + ' '
        rest = l[len(m_bq.group(0)) if m_bq else 0:]

        m_item = re.match(r'^([ \t]+)([-*+]|\d+\.)\s+(.*)$', rest)
        if m_item:
            sp = len(m_item.group(1).replace('\t', '    '))
            marker, content = m_item.group(2), m_item.group(3)
            if sp == 1:
                out1.append(f"{bq}{marker} {content}\n")
                mods += 1
                continue
            elif sp in (2, 3):
                out1.append(f"{bq}    {marker} {content}\n")
                mods += 1
                continue
            elif sp in (5, 6, 7):
                out1.append(f"{bq}        {marker} {content}\n")
                mods += 1
                continue
        out1.append(l)

    # Passo C: Se um item de lista terminando em ':' ou ':**' é seguido no mesmo nível por lista de outro tipo (ul <-> ol), indentar filhos em +4 espaços
    i = 0
    while i < len(out1) - 1:
        m_bq1 = re.match(r'^(?:> ?)+', out1[i])
        m_bq2 = re.match(r'^(?:> ?)+', out1[i + 1])
        bq1 = m_bq1.group(0) if m_bq1 else ''
        bq2 = m_bq2.group(0) if m_bq2 else ''
        if bool(bq1) == bool(bq2):
            info1 = get_list_info(out1[i][len(bq1):])
            info2 = get_list_info(out1[i + 1][len(bq2):])
            if info1 and info2 and info1[0] == info2[0] and info1[1] != info2[1]:
                if re.search(r':(?:\*\*|\*)?\s*$', info1[3].strip()):
                    target_sp = info2[0]
                    target_type = info2[1]
                    j = i + 1
                    while j < len(out1):
                        m_bqj = re.match(r'^(?:> ?)+', out1[j])
                        bqj = m_bqj.group(0) if m_bqj else ''
                        if bool(bqj) != bool(bq1):
                            break
                        rest_j = out1[j][len(bqj):]
                        info_j = get_list_info(rest_j)
                        if info_j and info_j[0] == target_sp and info_j[1] == target_type:
                            out1[j] = f"{bqj}    {rest_j}"
                            mods += 1
                            j += 1
                        elif not info_j and rest_j.startswith(' ' * (target_sp + 2)):
                            out1[j] = f"{bqj}    {rest_j}"
                            mods += 1
                            j += 1
                        else:
                            break
        i += 1

    # Passo D: Inserir linha em branco obrigatória antes de listas de nível 0 e entre listas de tipos diferentes (ul <-> ol)
    out2 = []
    in_code = False
    for i, l in enumerate(out1):
        if is_code_fence(l):
            in_code = not in_code
            out2.append(l)
            continue
        out2.append(l)
        if in_code or i + 1 >= len(out1):
            continue
        nl = out1[i + 1]
        if is_code_fence(nl):
            continue

        bq1 = re.match(r'^(?:> ?)+', l)
        bq2 = re.match(r'^(?:> ?)+', nl)
        if bool(bq1) != bool(bq2):
            continue

        r1 = l[len(bq1.group(0)):] if bq1 else l
        r2 = nl[len(bq2.group(0)):] if bq2 else nl
        s1, s2 = r1.strip(), r2.strip()
        if not s1 or not s2 or s1.startswith('#') or s1.startswith('|') or s1.startswith('---'):
            continue

        info1 = get_list_info(r1)
        info2 = get_list_info(r2)

        # Linha de texto comum na coluna 0 seguida por marcador de lista na coluna 0
        if not r1.startswith(' ') and not r2.startswith(' '):
            if not info1 and info2:
                out2.append(">\n" if bq1 else "\n")
                mods += 1
                continue

        # Transição entre tipos diferentes de lista (ul <-> ol) onde a segunda não é sub-lista da primeira
        if info1 and info2 and info1[1] != info2[1]:
            if info1[0] >= info2[0]:
                out2.append(">\n" if bq1 else "\n")
                mods += 1

    return out2, mods


def synchronize_sumario_links(lines):
    """
    Sincroniza todos os links [Texto](#slug) dentro da seção '## 🧭 Sumário' com os
    cabeçalhos reais do corpo do documento.
    """
    mods = 0
    in_code = False
    in_sum = False
    body_headings = []  # (hlvl, htitle, slug, sec_num)

    sum_heading_re = re.compile(r'^#{2,3}\s+(?:🧭\s*)?Sumário(?:\s+Interativo)?\s*$')

    for l in lines:
        if is_code_fence(l):
            in_code = not in_code
            continue
        if in_code:
            continue
        if sum_heading_re.match(l.strip()):
            in_sum = True
            continue
        if in_sum:
            if l.startswith('#') or l.startswith('---'):
                in_sum = False
            else:
                continue
        if not in_sum:
            mh = re.match(r'^(#{2,4})\s+(.*)$', l)
            if mh and not re.match(r'^#{2,3}\s+.*Ementa', l):
                htitle = mh.group(2).strip()
                bslug = slugify_heading(htitle)
                mnum = re.match(r'^(?:[^\w\d\s]+\s*)*(\d+(?:\.\d+)*)\.?\s+', htitle)
                sec_num = mnum.group(1) if mnum else None
                body_headings.append((mh.group(1), htitle, bslug, sec_num))

    if not body_headings:
        return lines, mods

    new_lines = []
    in_code = False
    in_sum = False
    for l in lines:
        if is_code_fence(l):
            in_code = not in_code
            new_lines.append(l)
            continue
        if in_code:
            new_lines.append(l)
            continue
        if sum_heading_re.match(l.strip()):
            in_sum = True
            new_lines.append(l)
            continue
        if in_sum:
            if l.startswith('#') or l.startswith('---'):
                in_sum = False
                if new_lines and new_lines[-1].strip() != '':
                    new_lines.append('\n')
                new_lines.append(l)
                continue
            if l.strip() == '':
                # Remover linhas em branco internas ao Sumário para manter <ul> único
                mods += 1
                continue
            # Converter '1. [Título](#slug)' para '- [1. Título](#slug)'
            m_ol_sum = re.match(r'^(\s*)(\d+)\.\s+\[([^\]]+)\]\(#([^)]+)\)(.*)$', l)
            if m_ol_sum:
                sp_s, num_s, lbl_s, slg_s, tail_s = m_ol_sum.groups()
                if not re.match(r'^\d+\.', lbl_s.strip()):
                    lbl_s = f"{num_s}. {lbl_s}"
                l = f"{sp_s}- [{lbl_s}](#{slg_s}){tail_s}\n"
                mods += 1
            # Converter '    - 1.1 [Título](#slug)' para '    - [1.1 Título](#slug)'
            m_sub_sum = re.match(r'^(\s*[-*+]\s+)(\d+(?:\.\d+)+)\s+\[([^\]]+)\]\(#([^)]+)\)(.*)$', l)
            if m_sub_sum:
                pre_s, num_s, lbl_s, slg_s, tail_s = m_sub_sum.groups()
                if not re.match(r'^\d+\.\d+', lbl_s.strip()):
                    lbl_s = f"{num_s} {lbl_s}"
                l = f"{pre_s}[{lbl_s}](#{slg_s}){tail_s}\n"
                mods += 1

            m = re.search(r'\[([^\]]+)\]\(#([^)]+)\)', l)
            if m:
                tlabel = m.group(1)
                old_target = m.group(2)
                tslug = slugify_heading(old_target)
                found_slug = None
                for _, _, bslug, _ in body_headings:
                    if bslug == tslug:
                        found_slug = bslug
                        break
                if not found_slug:
                    tlabel_slug = slugify_heading(tlabel)
                    mtnum = re.match(r'^(\d+(?:\.\d+)*)\.?\s+(.*)$', tlabel.strip())
                    tnum = mtnum.group(1) if mtnum else None
                    trest = slugify_heading(mtnum.group(2)) if mtnum else tlabel_slug
                    for _, _, bslug, bnum in body_headings:
                        if (tnum and bnum == tnum) or bslug == tlabel_slug or bslug == trest or (trest and len(trest) >= 10 and trest[:15] in bslug):
                            found_slug = bslug
                            break
                if found_slug and old_target != found_slug:
                    l = l[:m.start(2)] + found_slug + l[m.end(2):]
                    mods += 1
            new_lines.append(l)
            continue
        new_lines.append(l)

    return new_lines, mods


def sanitize_markdown_file(filepath):
    """Aplica todas as regras da Fase 1 em um arquivo .md."""
    with open(filepath, 'r', encoding='utf-8') as f:
        original_text = f.read()

    if os.path.basename(filepath) == 'README.md':
        # Apenas garantir linha em branco antes de listas nos README.md
        lines = original_text.splitlines(keepends=True)
        lines, mod_list = sanitize_list_indentation_and_blanks(lines)
        new_text = "".join(lines)
        if new_text != original_text:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_text)
            return True, {"list": mod_list}
        return False, {}

    text, mod_html = sanitize_html_and_broken_marks(original_text, filepath)
    text, mod_latex = sanitize_latex(text)

    lines = text.splitlines(keepends=True)
    lines, mod_title = sanitize_generic_titles_and_headings(lines, filepath)
    lines, mod_code = unindent_fenced_code_blocks(lines)
    lines, mod_enum = sanitize_embedded_enumerations(lines)
    lines, mod_opts = sanitize_options_and_romans(lines)
    lines, mod_toc = synchronize_sumario_links(lines)
    lines, mod_list = sanitize_list_indentation_and_blanks(lines)

    new_text = "".join(lines)
    if new_text != original_text:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_text)
        return True, {
            "html": mod_html,
            "latex": mod_latex,
            "title": mod_title,
            "code": mod_code,
            "enum": mod_enum,
            "opts": mod_opts,
            "list": mod_list,
            "toc": mod_toc,
        }
    return False, {}


def main():
    print("=" * 72)
    print(" FASE 1: HIGIENIZAÇÃO GLOBAL DOS ARQUIVOS MARKDOWN (TCE-GO)")
    print(" Preservação de 100% dos emoticons e símbolos Unicode")
    print("=" * 72)

    total_scanned = 0
    total_modified = 0

    for target_dir in TARGET_DIRS:
        if not os.path.exists(target_dir):
            continue
        for root, _, files in os.walk(target_dir):
            if "resources" in root:
                continue
            for file in sorted(files):
                if file.endswith('.md'):
                    total_scanned += 1
                    filepath = os.path.join(root, file)
                    changed, report = sanitize_markdown_file(filepath)
                    if changed:
                        total_modified += 1
                        rel = os.path.relpath(filepath, BASE_DIR)
                        print(f"  ✓ Higienizado: {rel} {report}")

    print("-" * 72)
    print(f"Total de arquivos .md varridos   : {total_scanned}")
    print(f"Total de arquivos .md atualizados: {total_modified}")
    print("=" * 72)


if __name__ == "__main__":
    main()
