# -*- coding: utf-8 -*-
"""
Script de Auditoria, Limpeza e Padronização de Arquivos Markdown
Audita e sanitiza todos os arquivos .md em:
  - fontes_de_estudo/conhecimentos_gerais
  - fontes_de_estudo/conhecimentos_especificos_b02_ti
  - fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo

Preserva 100% de todos os emojis Unicode e caracteres especiais.
"""

import os
import re
import sys

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

def sanitize_html_tags(content):
    """Regra 1: Desescapar tags HTML corrompidas para <ins> e </ins>."""
    modifications = 0
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
    for pattern, repl in patterns:
        content, count = re.subn(pattern, repl, content)
        modifications += count
    return content, modifications

def sanitize_latex_and_formatting(content, filename):
    """Regra 5: Consertar erros de sintaxe LaTeX/KaTeX, negrito/itálico e linha órfã."""
    modifications = 0

    # 1. \centernot{\longleftrightarrow} -> \not\longleftrightarrow
    content, c = re.subn(r'\\centernot\{\\longleftrightarrow\}', r'\\not\\longleftrightarrow', content)
    modifications += c

    # 2. \mathbf{R\$\  -> \text{R\$ }\mathbf{
    content, c = re.subn(r'\\mathbf\{R\\\$\s+', r'\\text{R\\$ }\\mathbf{', content)
    modifications += c

    # 3. Fechamento incorreto de itálico + negrito: *Texto **negrito***; -> *Texto* **negrito**;
    pattern_bi = r'\*([A-Za-zÀ-ÿ\s]+?)\s+\*\*([A-Za-zÀ-ÿ\s/]+?)\*\*\*([;.]?)'
    content, c = re.subn(pattern_bi, r'*\1* **\2**\3', content)
    modifications += c

    # 4. Remover linha órfã em 02_ortografia_acentuacao_e_formacao_de_palavras.md
    if "02_ortografia_acentuacao_e_formacao_de_palavras.md" in filename:
        orphan_pattern = r'(\n)5\.1 Critérios Cumulativos da Paráfrase Legítima\s*\n+'
        content, c = re.subn(orphan_pattern, r'\1\n', content)
        modifications += c

    return content, modifications

def sanitize_generic_module_titles(lines, filename):
    """Regra 6: Corrigir primeiro título se for genérico como # Módulo 08: Banco de Dados."""
    modifications = 0
    if not lines:
        return lines, modifications

    first_line = lines[0].strip()
    if re.match(r'^#\s*Módulo\s+\d+:', first_line):
        # Tenta pegar subtítulo da linha 2 ou 3
        real_title = None
        remove_idx = -1
        for i in range(1, min(5, len(lines))):
            cand = lines[i].strip()
            if cand.startswith('## '):
                real_title = cand.replace('## ', '').strip()
                remove_idx = i
                break
        
        if not real_title:
            # Fallback para o nome do arquivo
            base = os.path.basename(filename).replace('.md', '')
            parts = base.split('_', 1)
            num = parts[0] if parts[0].isdigit() else ""
            title_text = parts[1].replace('_', ' ').title() if len(parts) > 1 else base.replace('_', ' ').title()
            real_title = f"{num} - {title_text}" if num else title_text

        # Padroniza como # <real_title> com traço se tiver número com ponto
        # Ex: "04. Índices..." -> "04 - Índices..."
        real_title = re.sub(r'^(\d+)\.\s*', r'\1 - ', real_title)
        lines[0] = f"# {real_title}\n"
        if remove_idx != -1:
            lines.pop(remove_idx)
            # Remove linha em branco que ficou sobrando se houver
            if remove_idx < len(lines) and lines[remove_idx].strip() == "":
                lines.pop(remove_idx)
        modifications += 1

    return lines, modifications

def sanitize_embedded_enumerations(lines):
    """
    Regra 4 (Parte B): Em parágrafos teóricos que contenham listas embutidas após dois-pontos
    no formato ': (1) texto; (2) texto; (3) texto' ou ': (a) texto, (b) texto',
    converter essas enumerações em itens de lista em linhas separadas e indentadas.
    """
    new_lines = []
    modifications = 0
    in_code = False

    for line in lines:
        if is_code_fence(line):
            in_code = not in_code
            new_lines.append(line)
            continue

        if in_code:
            new_lines.append(line)
            continue

        has_num = (": (1) " in line) and ("; (2) " in line or ", (2) " in line or "e (2) " in line)
        has_alpha = (": (a) " in line) and ("; (b) " in line or ", (b) " in line or "e (b) " in line)

        if has_num or has_alpha:
            bq_match = re.match(r'^(?:>\s*)+', line)
            bq_prefix = bq_match.group(0) if bq_match else ""
            line_body = line[len(bq_prefix):].rstrip('\r\n')

            is_subitem = bool(re.search(r'[-*]\s+\*\*[A-E]\)\*\*', line))
            indent = "    " if is_subitem else ""

            if has_num:
                parts_split = line_body.split(': (1) ', 1)
                intro = parts_split[0] + ':'
                rest = parts_split[1]
                sub_parts = re.split(r'[;,]\s*(?:e\s+)?\((\d+)\)\s+', rest)
                items = [("1", sub_parts[0])]
                for k in range(1, len(sub_parts), 2):
                    items.append((sub_parts[k], sub_parts[k+1]))
            else:
                parts_split = line_body.split(': (a) ', 1)
                intro = parts_split[0] + ':'
                rest = parts_split[1]
                sub_parts = re.split(r'[;,]\s*(?:e\s+)?\(([a-e])\)\s+', rest)
                items = [("a", sub_parts[0])]
                for k in range(1, len(sub_parts), 2):
                    items.append((sub_parts[k], sub_parts[k+1]))

            last_lbl, last_txt = items[-1]
            trailing = ""
            m_trail = re.search(r'^(.*?\.)\s+([A-ZÁ-Ú].*)$', last_txt)
            if m_trail:
                items[-1] = (last_lbl, m_trail.group(1))
                trailing = m_trail.group(2)

            new_lines.append(f"{bq_prefix}{intro}\n")
            if bq_prefix:
                new_lines.append(f"{bq_prefix.rstrip()}\n")
            else:
                new_lines.append("\n")

            for lbl, itxt in items:
                itxt_clean = itxt.strip()
                if has_num:
                    new_lines.append(f"{bq_prefix}{indent}{lbl}. {itxt_clean}\n")
                else:
                    new_lines.append(f"{bq_prefix}{indent}- **{lbl})** {itxt_clean}\n")

            if trailing:
                if bq_prefix:
                    new_lines.append(f"{bq_prefix.rstrip()}\n")
                    new_lines.append(f"{bq_prefix}{trailing}\n")
                else:
                    new_lines.append("\n")
                    new_lines.append(f"{trailing}\n")

            modifications += 1
            continue

        new_lines.append(line)

    return new_lines, modifications

def sanitize_question_options_and_romans(lines):
    """
    Regra 4 (Parte A): Converter opções de questões cruas A) B) C) em listas padronizadas * **A)**,
    garantir que itens em algarismos romanos tenham quebras adequadas e não colem.
    """
    new_lines = []
    modifications = 0
    in_code = False

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

        # 1. Alternativas de questões cruas: 'A) ...', 'B) ...' fora de blockquote
        # que não sejam seguidas de comentário (ex: em blocos de 5 alternativas)
        m_opt = re.match(r'^([A-E])\)\s+(.*)$', line.strip())
        if m_opt and not line.strip().startswith('>'):
            letter = m_opt.group(1)
            opt_text = m_opt.group(2)
            # Se a linha anterior for texto e não estiver vazia, inserir linha em branco antes do bloco
            if new_lines and new_lines[-1].strip() != "" and not re.match(r'^\*\s+\*\*[A-E]\)\*\*', new_lines[-1].strip()):
                new_lines.append("\n")
            new_lines.append(f"* **{letter})** {opt_text}\n")
            modifications += 1
            i += 1
            continue

        # 2. Algarismos romanos em enunciados (I. ..., II. ...)
        # Se uma linha começa com I., II., etc., e a próxima também começa com número romano
        # garantir que termine com dois espaços '  \n' para não colar em parágrafo único
        m_rom = re.match(r'^(>*\s*)(I|II|III|IV|V|VI|VII|VIII|IX|X)\.\s+', line)
        if m_rom:
            clean_line = line.rstrip('\r\n')
            if not clean_line.endswith('  '):
                # Verifica se a próxima linha é outro romano ou texto relacionado
                if i + 1 < n:
                    next_clean = lines[i+1].strip()
                    if re.match(r'^(?:>\s*)?(?:I|II|III|IV|V|VI|VII|VIII|IX|X)\.\s+', next_clean) or next_clean.startswith('* **A)**'):
                        clean_line += '  '
                        modifications += 1
            new_lines.append(clean_line + '\n')
            i += 1
            continue

        new_lines.append(line)
        i += 1

    return new_lines, modifications

def sanitize_list_indentation(lines):
    """
    Regra 2: Corrigir Indentação de Sub-listas (2 ou 3 espaços -> 4 espaços).
    Regula múltiplos exatos de 4 espaços em sumários e listas no corpo/blockquotes.
    """
    new_lines = []
    modifications = 0
    in_code = False

    for line in lines:
        if is_code_fence(line):
            in_code = not in_code
            new_lines.append(line)
            continue

        if in_code:
            new_lines.append(line)
            continue

        # Isolar prefixo de blockquote
        m_bq = re.match(r'^(?:>\s*)+', line)
        bq_prefix = m_bq.group(0) if m_bq else ""
        rest = line[len(bq_prefix):]

        # Verificar se é item de lista com indentação
        # Marcador: -, *, +, ou número 1.
        m_item = re.match(r'^([ \t]+)([-*+]|\d+\.)\s+(.*)$', rest)
        if m_item:
            spaces_str = m_item.group(1).replace('\t', '    ')
            num_spaces = len(spaces_str)
            marker = m_item.group(2)
            content = m_item.group(3)

            # Converter 2 ou 3 espaços para 4; 5, 6 ou 7 para 8; etc.
            if num_spaces >= 2 and (num_spaces % 4 != 0):
                new_spaces = ((num_spaces + 2) // 4) * 4
                rest_corrected = (" " * new_spaces) + f"{marker} {content}\n"
                new_lines.append(f"{bq_prefix}{rest_corrected}")
                modifications += 1
                continue
            elif num_spaces == 1:
                # 1 espaço solto acidental: remover para alinhar com nível 0
                rest_corrected = f"{marker} {content}\n"
                new_lines.append(f"{bq_prefix}{rest_corrected}")
                modifications += 1
                continue

        new_lines.append(line)

    return new_lines, modifications

def sanitize_blank_lines_before_lists(lines):
    """
    Regra 3: Garantir Linha em Branco Antes de Listas e Sub-listas.
    Sempre que uma linha de texto normal (terminada em ':') for seguida imediatamente por
    um item de lista, inserir uma linha em branco (ou linha contendo apenas '>' em blockquote).
    """
    new_lines = []
    modifications = 0
    in_code = False

    list_item_pattern = re.compile(r'^(?:[-*+]|\d+\.|[IVXLCDM]+\.|\*\s*\*\*[A-E]\)\*\*|[A-E]\))\s+')

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

        new_lines.append(line)

        if i + 1 < n:
            next_line = lines[i + 1]
            if not is_code_fence(next_line):
                # Verificar se ambas estão em blockquote
                is_bq1 = line.strip().startswith('>')
                is_bq2 = next_line.strip().startswith('>')

                if is_bq1 and is_bq2:
                    c1 = re.sub(r'^(?:>\s*)+', '', line).strip()
                    c2 = re.sub(r'^(?:>\s*)+', '', next_line).strip()
                    if c1 and not c1.startswith('#') and not list_item_pattern.match(c1):
                        if c1.endswith(':') and list_item_pattern.match(c2):
                            new_lines.append(">\n")
                            modifications += 1
                elif not is_bq1 and not is_bq2:
                    c1 = line.strip()
                    c2 = next_line.strip()
                    if c1 and not c1.startswith('#') and not c1.startswith('|') and not list_item_pattern.match(c1):
                        if c1.endswith(':') and list_item_pattern.match(c2):
                            new_lines.append("\n")
                            modifications += 1

        i += 1

    return new_lines, modifications

def sanitize_markdown_file(filepath):
    """Processa um arquivo Markdown aplicando todas as 6 regras com segurança."""
    with open(filepath, 'r', encoding='utf-8') as f:
        original_text = f.read()

    # 1. Regra 1: Desescapar HTML
    text, mod_html = sanitize_html_tags(original_text)

    # 2. Regra 5: LaTeX e formatação
    text, mod_latex = sanitize_latex_and_formatting(text, filepath)

    # Linhas para transformações estruturais
    lines = text.splitlines(keepends=True)

    # 3. Regra 6: Títulos genéricos
    lines, mod_title = sanitize_generic_module_titles(lines, filepath)

    # 4. Regra 4B: Enumerações embutidas (: (1) ...; (2) ...)
    lines, mod_enum = sanitize_embedded_enumerations(lines)

    # 5. Regra 4A: Alternativas A) B) C) e Romanos
    lines, mod_opts = sanitize_question_options_and_romans(lines)

    # 6. Regra 2: Indentação de sub-listas (2 -> 4 espaços)
    lines, mod_indent = sanitize_list_indentation(lines)

    # 7. Regra 3: Linha em branco antes de listas
    lines, mod_blank = sanitize_blank_lines_before_lists(lines)

    sanitized_text = "".join(lines)

    total_mods = mod_html + mod_latex + mod_title + mod_enum + mod_opts + mod_indent + mod_blank

    if sanitized_text != original_text:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(sanitized_text)
        return True, {
            "html": mod_html,
            "latex": mod_latex,
            "title": mod_title,
            "enum": mod_enum,
            "opts": mod_opts,
            "indent": mod_indent,
            "blank": mod_blank,
            "total": total_mods
        }

    return False, {}

def main():
    print("=" * 70)
    print(" AUDITORIA E HIGIENIZAÇÃO DE ARQUIVOS MARKDOWN (TCE-GO)")
    print(" Preservação estrita de 100% dos emojis e caracteres Unicode")
    print("=" * 70)

    total_scanned = 0
    total_modified = 0
    stats = {
        "html": 0,
        "latex": 0,
        "title": 0,
        "enum": 0,
        "opts": 0,
        "indent": 0,
        "blank": 0,
    }

    modified_files = []

    for target_dir in TARGET_DIRS:
        folder_name = os.path.basename(target_dir)
        print(f"\n📂 Analisando diretório: {folder_name}...")
        
        if not os.path.exists(target_dir):
            print(f"   [AVISO] Pasta não encontrada: {target_dir}")
            continue

        for root, dirs, files in os.walk(target_dir):
            # Ignorar expressamente pasta resources
            if "resources" in root:
                continue

            for file in sorted(files):
                if file.endswith('.md'):
                    total_scanned += 1
                    filepath = os.path.join(root, file)
                    rel_path = os.path.relpath(filepath, BASE_DIR)

                    changed, report = sanitize_markdown_file(filepath)
                    if changed:
                        total_modified += 1
                        modified_files.append((rel_path, report))
                        for k in stats:
                            stats[k] += report.get(k, 0)
                        
                        summary_parts = []
                        if report.get("html"): summary_parts.append(f"HTML:{report['html']}")
                        if report.get("latex"): summary_parts.append(f"LaTeX:{report['latex']}")
                        if report.get("title"): summary_parts.append(f"Título:{report['title']}")
                        if report.get("enum"): summary_parts.append(f"Enum:{report['enum']}")
                        if report.get("opts"): summary_parts.append(f"Opções/Rom:{report['opts']}")
                        if report.get("indent"): summary_parts.append(f"Indent:{report['indent']}")
                        if report.get("blank"): summary_parts.append(f"Linhas:{report['blank']}")

                        print(f"  ✓ Modificado: {rel_path} [{' | '.join(summary_parts)}]")

    print("\n" + "=" * 70)
    print(" RELATÓRIO CONSOLIDADO DE SANEAMENTO")
    print("=" * 70)
    print(f"Total de arquivos .md analisados : {total_scanned}")
    print(f"Total de arquivos .md modificados : {total_modified}")
    print(f"Arquivos já em plena conformidade: {total_scanned - total_modified}")
    print("-" * 70)
    print("Totais de correções aplicadas por categoria:")
    print(f"  1. Tags HTML desescapadas (<ins>)               : {stats['html']}")
    print(f"  2. Indentações de sub-listas ajustadas (2->4 sp): {stats['indent']}")
    print(f"  3. Linhas em branco inseridas antes de listas   : {stats['blank']}")
    print(f"  4. Enumerações teóricas inline convertidas      : {stats['enum']}")
    print(f"  5. Alternativas de questões / Romanos ajustados : {stats['opts']}")
    print(f"  6. Erros LaTeX/KaTeX, formatação e órfãos       : {stats['latex']}")
    print(f"  7. Títulos genéricos de módulo padronizados     : {stats['title']}")
    print("=" * 70)

if __name__ == "__main__":
    main()
