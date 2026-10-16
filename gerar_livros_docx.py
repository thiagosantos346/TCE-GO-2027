#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de Livros Digitais em Microsoft Word (.docx) - TCE-GO 2027
Consolidação dos materiais de estudo com formatação ABNT e Design Editorial Didático.
Inclui Transpiler Mermaid para HTML e injeção nativa via altChunk no OpenXML.
"""

import os
import re
import glob
import uuid
import docx
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn
from docx.opc.part import Part
from docx.opc.packuri import PackURI
from docx.opc.constants import RELATIONSHIP_TYPE

# --- Paleta de Cores Editorial ---
COLOR_PRIMARY_NAVY = RGBColor(0x1B, 0x36, 0x5D)     # Azul Marinho Real (#1B365D)
COLOR_HEADING_2 = RGBColor(0x2C, 0x52, 0x82)        # Azul Aço (#2C5282)
COLOR_HEADING_3 = RGBColor(0x2B, 0x6C, 0xB0)        # Azul Safira (#2B6CB0)
COLOR_HEADING_4 = RGBColor(0x33, 0x41, 0x55)        # Cinza Ardósia (#334155)
COLOR_TEXT_DARK = RGBColor(0x11, 0x18, 0x27)        # Preto Suave / Quase preto (#111827)
COLOR_MUTED_GRAY = RGBColor(0x4B, 0x55, 0x63)       # Cinza Médio (#4B5563)
COLOR_CODE_TEXT = RGBColor(0x0F, 0x17, 0x2A)        # Azul Noite Escuro (#0F172A)
COLOR_GABARITO = RGBColor(0x04, 0x78, 0x57)         # Verde Esmeralda (#047857)
COLOR_ALERT_BORDER = "D97706"                       # Âmbar (#D97706)
COLOR_ALERT_BG = "FFFBEB"                           # Fundo Âmbar Claro
COLOR_DICA_BORDER = "2563EB"                        # Azul Royal (#2563EB)
COLOR_DICA_BG = "EFF6FF"                            # Fundo Azul Claro
COLOR_NOTE_BORDER = "059669"                        # Verde Menta (#059669)
COLOR_NOTE_BG = "ECFDF5"                            # Fundo Verde Claro
COLOR_COMMENT_BORDER = "475569"                     # Cinza Ardósia (#475569)
COLOR_COMMENT_BG = "F8FAFC"                         # Fundo Cinza Gelo
COLOR_TABLE_HEADER_BG = "1B365D"                    # Fundo Cabeçalho Tabela
COLOR_TABLE_ZEBRA_BG = "F8FAFC"                     # Fundo Zebra Tabela

TOTAL_CONTENT_WIDTH_CM = 16.0  # 21.0cm (A4) - 3.0cm (esq) - 2.0cm (dir)


def configure_document_abnt(doc):
    """Configura o documento com parâmetros estritos da ABNT."""
    for section in doc.sections:
        section.top_margin = Cm(3.0)
        section.left_margin = Cm(3.0)
        section.bottom_margin = Cm(2.0)
        section.right_margin = Cm(2.0)
        section.page_width = Cm(21.0)
        section.page_height = Cm(29.7)

    # Configuração do Estilo Normal
    style_normal = doc.styles['Normal']
    style_normal.font.name = 'Arial'
    style_normal.font.size = Pt(12)
    style_normal.font.color.rgb = COLOR_TEXT_DARK
    style_normal.paragraph_format.line_spacing = 1.5
    style_normal.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    style_normal.paragraph_format.space_after = Pt(4)
    style_normal.paragraph_format.space_before = Pt(0)


def create_book_cover(doc, title, subtitle, area_label):
    """Gera uma capa editorial sofisticada e institucional na primeira página."""
    p_top = doc.add_paragraph()
    p_top.paragraph_format.space_before = Pt(72)
    p_top.paragraph_format.space_after = Pt(12)
    p_top.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    r_inst = p_top.add_run("TRIBUNAL DE CONTAS DO ESTADO DE GOIÁS — TCE-GO")
    r_inst.bold = True
    r_inst.font.name = 'Arial'
    r_inst.font.size = Pt(14)
    r_inst.font.color.rgb = COLOR_PRIMARY_NAVY

    p_subinst = doc.add_paragraph()
    p_subinst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_subinst.paragraph_format.space_after = Pt(90)
    r_subinst = p_subinst.add_run("CONCURSO PÚBLICO 2027 • BANCA FUNDAÇÃO CARLOS CHAGAS (FCC)")
    r_subinst.bold = True
    r_subinst.font.name = 'Arial'
    r_subinst.font.size = Pt(11)
    r_subinst.font.color.rgb = COLOR_MUTED_GRAY

    # Título do Livro
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_after = Pt(18)
    r_title = p_title.add_run(title)
    r_title.bold = True
    r_title.font.name = 'Arial'
    r_title.font.size = Pt(24)
    r_title.font.color.rgb = COLOR_PRIMARY_NAVY

    # Subtítulo
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(28)
    r_sub = p_sub.add_run(subtitle)
    r_sub.italic = True
    r_sub.font.name = 'Arial'
    r_sub.font.size = Pt(14)
    r_sub.font.color.rgb = COLOR_MUTED_GRAY

    # Área / Eixo Temático
    p_area = doc.add_paragraph()
    p_area.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_area.paragraph_format.space_after = Pt(120)
    r_area = p_area.add_run(f"EIXO TEMÁTICO: {area_label.upper()}")
    r_area.bold = True
    r_area.font.name = 'Arial'
    r_area.font.size = Pt(12)
    r_area.font.color.rgb = COLOR_HEADING_2

    # Rodapé da Capa
    p_bot = doc.add_paragraph()
    p_bot.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_bot.paragraph_format.space_after = Pt(4)
    r_bot1 = p_bot.add_run("GUIA DIDÁTICO CONSOLIDADO — TEORIA COMPLETA E QUESTÕES COMENTADAS\n")
    r_bot1.bold = True
    r_bot1.font.name = 'Arial'
    r_bot1.font.size = Pt(10)
    r_bot1.font.color.rgb = COLOR_MUTED_GRAY

    r_bot2 = p_bot.add_run("GOIÂNIA - GO • EDIÇÃO DE REFERÊNCIA 2027")
    r_bot2.font.name = 'Arial'
    r_bot2.font.size = Pt(10)
    r_bot2.font.color.rgb = COLOR_MUTED_GRAY

    doc.add_page_break()


def inject_html_altchunk(doc, html_string):
    """
    Injeta código HTML puro diretamente no documento Word via altChunk (OpenXML).
    O Microsoft Word e o Google Docs interpretam essa part e a convertem em blocos nativos editáveis.
    """
    part = doc.part
    chunk_id = f'altChunk{uuid.uuid4().hex[:8]}'
    partname = PackURI(f'/word/{chunk_id}.html')
    alt_part = Part(
        partname=partname,
        content_type='text/html',
        blob=html_string.encode('utf-8'),
        package=part.package
    )
    part.package.parts.append(alt_part)
    rel_id = part.relate_to(alt_part, RELATIONSHIP_TYPE.A_F_CHUNK)

    # Injeta a tag <w:altChunk> no final do corpo XML do documento
    alt_chunk = OxmlElement('w:altChunk')
    alt_chunk.set(qn('r:id'), rel_id)
    doc.element.body.append(alt_chunk)


def transpile_mermaid_to_html(code_lines):
    """
    Transpiler Mermaid para HTML:
    Lê o código do diagrama Mermaid, extrai nós e conexões, e gera HTML semântico com estilos
    inline no padrão visual de livro didático de alta qualidade.
    """
    nodes = {}
    edges = []

    node_pattern = re.compile(
        r'([a-zA-Z0-9_\-]+)\s*(?:\[\["?(.*?)"?\]\]|\["?(.*?)"?\]|\(\("?(.*?)"?\)\)|\("?([^)]*?)"?\)|\{"?([^}]*?)"?\})'
    )
    edge_pattern = re.compile(
        r'([a-zA-Z0-9_\-]+)\s*(?:-->|-.->|---|===|==>)\s*(?:\|([^|]+)\|\s*)?([a-zA-Z0-9_\-]+)'
    )

    for line in code_lines:
        line_clean = line.strip()
        if not line_clean or line_clean.startswith(('flowchart', 'graph', 'sequenceDiagram', 'subgraph', 'end', '%%', 'classDef', 'style')):
            continue

        # Capturar nós declarados na linha
        for nm in node_pattern.finditer(line_clean):
            node_id = nm.group(1)
            label = next((g for g in nm.groups()[1:] if g is not None), node_id).strip('"\'')
            if node_id not in nodes or len(label) > len(nodes[node_id]):
                nodes[node_id] = label

        # Capturar conexões na linha
        for em in edge_pattern.finditer(line_clean):
            src, label, dst = em.groups()
            edges.append((src, label.strip() if label else None, dst))

    html_parts = [
        '<!DOCTYPE html>',
        '<html><head><meta charset="utf-8"></head><body>',
        '<div style="width: 100%; margin: 16px auto; text-align: center; font-family: Arial, sans-serif;">',
        '<div style="font-size: 8.5pt; font-family: Arial, sans-serif; font-weight: bold; color: #1E40AF; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 8px;">📊 FLUXOGRAMA CONCEITUAL</div>'
    ]

    if edges:
        last_rendered_node = None
        for src, label, dst in edges:
            src_label = nodes.get(src, src).replace('\n', '<br/>')
            dst_label = nodes.get(dst, dst).replace('\n', '<br/>')

            # Renderizar nó de origem se não for o último exibido
            if src != last_rendered_node:
                html_parts.append(
                    f'<div style="background-color: #EFF6FF; border: 2px solid #2563EB; padding: 10px 14px; text-align: center; font-family: Arial, sans-serif; border-radius: 5px; margin: 5px auto; width: 65%; color: #1E3A8A; font-weight: bold; font-size: 11pt; line-height: 1.3;">'
                    f'{src_label}'
                    f'</div>'
                )

            # Rótulo de condição e Seta
            if label:
                html_parts.append(
                    f'<div style="text-align: center; margin: 3px auto;">'
                    f'<span style="font-size: 9.5pt; font-family: Arial, sans-serif; color: #475569; font-weight: bold; background-color: #F1F5F9; border: 1px dashed #94A3B8; padding: 2px 8px; border-radius: 4px;">{label}</span>'
                    f'</div>'
                )

            html_parts.append(
                '<div style="text-align: center; font-size: 24px; color: #64748B; margin: 2px auto; line-height: 1;">⬇</div>'
            )

            # Renderizar nó de destino
            html_parts.append(
                f'<div style="background-color: #EFF6FF; border: 2px solid #2563EB; padding: 10px 14px; text-align: center; font-family: Arial, sans-serif; border-radius: 5px; margin: 5px auto; width: 65%; color: #1E3A8A; font-weight: bold; font-size: 11pt; line-height: 1.3;">'
                f'{dst_label}'
                f'</div>'
            )
            last_rendered_node = dst

    elif nodes:
        # Diagrama sem conexões explícitas: renderizar cartões sequenciais
        node_items = list(nodes.items())
        for idx, (nid, label) in enumerate(node_items):
            clean_label = label.replace('\n', '<br/>')
            html_parts.append(
                f'<div style="background-color: #EFF6FF; border: 2px solid #2563EB; padding: 10px 14px; text-align: center; font-family: Arial, sans-serif; border-radius: 5px; margin: 5px auto; width: 65%; color: #1E3A8A; font-weight: bold; font-size: 11pt; line-height: 1.3;">'
                f'{clean_label}'
                f'</div>'
            )
            if idx < len(node_items) - 1:
                html_parts.append(
                    '<div style="text-align: center; font-size: 24px; color: #64748B; margin: 2px auto; line-height: 1;">⬇</div>'
                )

    html_parts.append('</div></body></html>')
    return '\n'.join(html_parts)


def add_formatted_runs(paragraph, text, default_size=Pt(12), default_color=None, default_bold=False, default_italic=False, default_font="Arial"):
    """
    Interpreta sintaxe inline de Markdown (negrito, itálico, código, fórmulas, links)
    e injeta runs correspondentes com a respectiva formatação.
    """
    pattern = re.compile(
        r'(?P<bold_italic>\*\*\*[^*]+\*\*\*)'
        r'|(?P<bold>\*\*[^*]+\*\*)'
        r'|(?P<italic>(?<!\*)\*[^*]+\*(?!\*)|(?<!_)_[^_]+_(?!_))'
        r'|(?P<code>`[^`]+`)'
        r'|(?P<math>\$[^$]+\$)'
        r'|(?P<link>\[[^\]]+\]\([^)]+\))'
    )
    last_end = 0
    for match in pattern.finditer(text):
        start, end = match.span()
        if start > last_end:
            plain_text = text[last_end:start]
            r = paragraph.add_run(plain_text)
            r.font.name = default_font
            r.font.size = default_size
            r.bold = default_bold
            r.italic = default_italic
            if default_color:
                r.font.color.rgb = default_color

        kind = match.lastgroup
        raw = match.group()

        if kind == 'bold_italic':
            content = raw[3:-3]
            r = paragraph.add_run(content)
            r.font.name = default_font
            r.font.size = default_size
            r.bold = True
            r.italic = True
            if default_color:
                r.font.color.rgb = default_color

        elif kind == 'bold':
            content = raw[2:-2]
            r = paragraph.add_run(content)
            r.font.name = default_font
            r.font.size = default_size
            r.bold = True
            r.italic = default_italic
            if default_color:
                r.font.color.rgb = default_color

        elif kind == 'italic':
            content = raw[1:-1]
            r = paragraph.add_run(content)
            r.font.name = default_font
            r.font.size = default_size
            r.bold = default_bold
            r.italic = True
            if default_color:
                r.font.color.rgb = default_color

        elif kind == 'code':
            content = raw[1:-1]
            r = paragraph.add_run(content)
            r.font.name = 'Consolas'
            r.font.size = Pt(10)
            r.bold = False
            r.font.color.rgb = RGBColor(0x99, 0x1B, 0x1B)

        elif kind == 'math':
            content = raw[1:-1]
            r = paragraph.add_run(content)
            r.font.name = 'Cambria Math'
            r.font.size = default_size
            r.italic = True
            r.font.color.rgb = COLOR_PRIMARY_NAVY

        elif kind == 'link':
            link_match = re.match(r'\[([^\]]+)\]\(([^)]+)\)', raw)
            if link_match:
                link_text = link_match.group(1)
                r = paragraph.add_run(link_text)
                r.font.name = default_font
                r.font.size = default_size
                r.font.color.rgb = COLOR_HEADING_3
                r.underline = True

        last_end = end

    if last_end < len(text):
        plain_text = text[last_end:]
        r = paragraph.add_run(plain_text)
        r.font.name = default_font
        r.font.size = default_size
        r.bold = default_bold
        r.italic = default_italic
        if default_color:
            r.font.color.rgb = default_color


def render_callout_box(doc, lines, box_type="alert"):
    """
    Renderiza um box de destaque lateral (livro didático) usando tabela de 1 célula.
    box_type: 'alert' (âmbar/vermelho), 'dica' (azul), 'note' (verde), 'comment' (cinza neutro)
    """
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.cell(0, 0)
    tcPr = cell._tc.get_or_add_tcPr()

    if box_type == "alert":
        bg_hex = COLOR_ALERT_BG
        border_hex = COLOR_ALERT_BORDER
    elif box_type == "dica":
        bg_hex = COLOR_DICA_BG
        border_hex = COLOR_DICA_BORDER
    elif box_type == "note":
        bg_hex = COLOR_NOTE_BG
        border_hex = COLOR_NOTE_BORDER
    else:  # comment
        bg_hex = COLOR_COMMENT_BG
        border_hex = COLOR_COMMENT_BORDER

    # Shading (Fundo suave)
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{bg_hex}"/>')
    tcPr.append(shd)

    # Borda esquerda grossa e demais vazias
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:left w:val="single" w:sz="32" w:space="0" w:color="{border_hex}"/>'
        f'<w:top w:val="none"/><w:right w:val="none"/><w:bottom w:val="none"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)

    # Margens internas / Padding da célula
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="140" w:type="dxa"/><w:bottom w:w="140" w:type="dxa"/>'
        f'<w:left w:w="220" w:type="dxa"/><w:right w:w="220" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

    first_p = True
    for line in lines:
        cleaned_line = re.sub(r'^>\s?', '', line).strip()
        if not cleaned_line:
            continue

        if first_p:
            p = cell.paragraphs[0]
            first_p = False
        else:
            p = cell.add_paragraph()

        p.paragraph_format.line_spacing = 1.2
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)

        if "Gabarito:" in cleaned_line:
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(4)
            add_formatted_runs(p, cleaned_line, default_size=Pt(11), default_color=COLOR_GABARITO, default_bold=True)
        elif cleaned_line.startswith("- **") or cleaned_line.startswith("* **"):
            p.paragraph_format.left_indent = Cm(0.4)
            add_formatted_runs(p, cleaned_line, default_size=Pt(10.5), default_color=COLOR_TEXT_DARK)
        else:
            add_formatted_runs(p, cleaned_line, default_size=Pt(10.5), default_color=COLOR_TEXT_DARK)

    p_spacer = doc.add_paragraph()
    p_spacer.paragraph_format.space_before = Pt(0)
    p_spacer.paragraph_format.space_after = Pt(6)


def render_code_block(doc, lines, language=""):
    """Renderiza blocos de código fonte (Python, SQL, JSON, etc.) em caixa monoespaçada."""
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.cell(0, 0)
    tcPr = cell._tc.get_or_add_tcPr()

    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="F8FAFC"/>')
    tcPr.append(shd)

    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:left w:val="single" w:sz="8" w:space="0" w:color="CBD5E1"/>'
        f'<w:top w:val="single" w:sz="8" w:space="0" w:color="CBD5E1"/>'
        f'<w:right w:val="single" w:sz="8" w:space="0" w:color="CBD5E1"/>'
        f'<w:bottom w:val="single" w:sz="8" w:space="0" w:color="CBD5E1"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)

    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="120" w:type="dxa"/><w:bottom w:w="120" w:type="dxa"/>'
        f'<w:left w:w="180" w:type="dxa"/><w:right w:w="180" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

    p0 = cell.paragraphs[0]
    p0.paragraph_format.line_spacing = 1.0
    p0.paragraph_format.space_before = Pt(0)
    p0.paragraph_format.space_after = Pt(4)

    r_badge = p0.add_run(f"💻 CÓDIGO FONTE ({language.upper() if language else 'TEXT'})")
    r_badge.font.name = 'Consolas'
    r_badge.font.size = Pt(8.5)
    r_badge.bold = True
    r_badge.font.color.rgb = COLOR_HEADING_3

    code_content = "\n".join(lines)
    p_code = cell.add_paragraph()
    p_code.paragraph_format.line_spacing = 1.0
    p_code.paragraph_format.space_before = Pt(2)
    p_code.paragraph_format.space_after = Pt(2)
    r_code = p_code.add_run(code_content)
    r_code.font.name = 'Consolas'
    r_code.font.size = Pt(9.0)
    r_code.font.color.rgb = COLOR_CODE_TEXT

    p_spacer = doc.add_paragraph()
    p_spacer.paragraph_format.space_after = Pt(6)


def render_markdown_table(doc, table_lines):
    """Converte tabelas Markdown para tabelas nativas do Word com estilo ABNT e linhas zebradas."""
    rows_data = []
    for line in table_lines:
        line_clean = line.strip()
        if not line_clean.startswith('|'):
            continue
        cells = [c.strip() for c in line_clean.strip('|').split('|')]
        if all(re.match(r'^:?-+:?$', c) for c in cells if c):
            continue
        rows_data.append(cells)

    if not rows_data:
        return

    num_cols = max(len(r) for r in rows_data)
    for r in rows_data:
        while len(r) < num_cols:
            r.append('')

    table = doc.add_table(rows=len(rows_data), cols=num_cols)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False

    col_width = Cm(TOTAL_CONTENT_WIDTH_CM / num_cols)

    for row_idx, row in enumerate(rows_data):
        is_header = (row_idx == 0)
        table_row = table.rows[row_idx]

        trPr = table_row._tr.get_or_add_trPr()
        trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))

        for col_idx, cell_value in enumerate(row):
            cell = table_row.cells[col_idx]
            cell.width = col_width
            tcPr = cell._tc.get_or_add_tcPr()

            if is_header:
                shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{COLOR_TABLE_HEADER_BG}"/>')
            elif row_idx % 2 == 0:
                shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{COLOR_TABLE_ZEBRA_BG}"/>')
            else:
                shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="FFFFFF"/>')
            tcPr.append(shd)

            borders = parse_xml(
                f'<w:tcBorders {nsdecls("w")}>'
                f'<w:top w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>'
                f'<w:bottom w:val="single" w:sz="6" w:space="0" w:color="CBD5E1"/>'
                f'<w:left w:val="none"/><w:right w:val="none"/>'
                f'</w:tcBorders>'
            )
            tcPr.append(borders)

            tcMar = parse_xml(
                f'<w:tcMar {nsdecls("w")}>'
                f'<w:top w:w="100" w:type="dxa"/><w:bottom w:w="100" w:type="dxa"/>'
                f'<w:left w:w="120" w:type="dxa"/><w:right w:w="120" w:type="dxa"/>'
                f'</w:tcMar>'
            )
            tcPr.append(tcMar)

            p = cell.paragraphs[0]
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(1)

            if is_header:
                add_formatted_runs(p, cell_value, default_size=Pt(10), default_color=RGBColor(0xFF, 0xFF, 0xFF), default_bold=True)
            else:
                add_formatted_runs(p, cell_value, default_size=Pt(9.5), default_color=COLOR_TEXT_DARK)

    p_spacer = doc.add_paragraph()
    p_spacer.paragraph_format.space_after = Pt(6)


def process_markdown_file(doc, file_path):
    """Lê e converte com fidelidade um arquivo Markdown para elementos nativos do Word."""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    idx = 0
    total_lines = len(lines)

    while idx < total_lines:
        line = lines[idx].rstrip('\r\n')
        line_stripped = line.strip()

        # 1. Ignorar linhas vazias
        if not line_stripped:
            idx += 1
            continue

        # 2. Divisores horizontais
        if re.match(r'^(\-{3,}|\*{3,}|_{3,})$', line_stripped):
            idx += 1
            continue

        # 3. Blocos de Código e Diagramas
        if line_stripped.startswith('```'):
            lang = line_stripped.lstrip('`').strip()
            code_lines = []
            idx += 1
            while idx < total_lines and not lines[idx].strip().startswith('```'):
                code_lines.append(lines[idx].rstrip('\r\n'))
                idx += 1
            if idx < total_lines:
                idx += 1  # consome fechamento ```

            if 'mermaid' in lang.lower():
                # Transpila para HTML e injeta nativamente via altChunk
                html_diagram = transpile_mermaid_to_html(code_lines)
                inject_html_altchunk(doc, html_diagram)
                p_sp = doc.add_paragraph()
                p_sp.paragraph_format.space_after = Pt(6)
            else:
                render_code_block(doc, code_lines, language=lang)
            continue

        # 4. Tabelas Markdown
        if line_stripped.startswith('|') and line_stripped.endswith('|'):
            table_lines = []
            while idx < total_lines and lines[idx].strip().startswith('|') and lines[idx].strip().endswith('|'):
                table_lines.append(lines[idx].strip())
                idx += 1
            render_markdown_table(doc, table_lines)
            continue

        # 5. Blocos de Citação, Alertas e Comentários (>)
        if line_stripped.startswith('>'):
            quote_lines = []
            while idx < total_lines and lines[idx].strip().startswith('>'):
                quote_lines.append(lines[idx].strip())
                idx += 1

            full_quote_text = " ".join(quote_lines)

            # Classificar tipo de Callout Box
            if any(k in full_quote_text for k in ["🚨", "🛑", "ALERTA"]):
                render_callout_box(doc, quote_lines, box_type="alert")
            elif any(k in full_quote_text for k in ["💡", "DICA"]):
                render_callout_box(doc, quote_lines, box_type="dica")
            elif any(k in full_quote_text for k in ["⭐", "📌", "IMPORTANTE", "NOTA"]):
                render_callout_box(doc, quote_lines, box_type="note")
            elif any(k in full_quote_text for k in ["Comentário Detalhado", "Gabarito:"]):
                render_callout_box(doc, quote_lines, box_type="comment")
            elif any(k in full_quote_text for k in ["Matéria:", "Cargo:", "Conteúdo Oficial:"]):
                # Metadados de cabeçalho: recuo de 4 cm (ABNT)
                for ql in quote_lines:
                    clean_meta = re.sub(r'^>\s?', '', ql).strip()
                    if clean_meta:
                        p_meta = doc.add_paragraph()
                        p_meta.paragraph_format.left_indent = Cm(4.0)
                        p_meta.paragraph_format.line_spacing = 1.0
                        p_meta.paragraph_format.space_before = Pt(1)
                        p_meta.paragraph_format.space_after = Pt(2)
                        add_formatted_runs(p_meta, clean_meta, default_size=Pt(10), default_color=COLOR_MUTED_GRAY)
                p_sp = doc.add_paragraph()
                p_sp.paragraph_format.space_after = Pt(6)
            else:
                # Citação normal ABNT (recuo de 4 cm, fonte 10, simples)
                for ql in quote_lines:
                    clean_q = re.sub(r'^>\s?', '', ql).strip()
                    if clean_q:
                        p_q = doc.add_paragraph()
                        p_q.paragraph_format.left_indent = Cm(4.0)
                        p_q.paragraph_format.line_spacing = 1.0
                        p_q.paragraph_format.space_before = Pt(2)
                        p_q.paragraph_format.space_after = Pt(2)
                        add_formatted_runs(p_q, clean_q, default_size=Pt(10), default_color=COLOR_TEXT_DARK)
                p_sp = doc.add_paragraph()
                p_sp.paragraph_format.space_after = Pt(4)
            continue

        # 6. Cabeçalhos / Títulos (Heading 1 a 4)
        if line_stripped.startswith('#'):
            h_match = re.match(r'^(#{1,6})\s+(.*)$', line_stripped)
            if h_match:
                level = len(h_match.group(1))
                h_text = h_match.group(2).strip()

                p = doc.add_paragraph()
                p.paragraph_format.keep_with_next = True

                if level == 1:
                    p.paragraph_format.space_before = Pt(18)
                    p.paragraph_format.space_after = Pt(8)
                    add_formatted_runs(p, h_text, default_size=Pt(18), default_color=COLOR_PRIMARY_NAVY, default_bold=True)
                elif level == 2:
                    p.paragraph_format.space_before = Pt(14)
                    p.paragraph_format.space_after = Pt(6)
                    add_formatted_runs(p, h_text, default_size=Pt(14), default_color=COLOR_HEADING_2, default_bold=True)
                elif level == 3:
                    p.paragraph_format.space_before = Pt(10)
                    p.paragraph_format.space_after = Pt(4)
                    add_formatted_runs(p, h_text, default_size=Pt(12), default_color=COLOR_HEADING_3, default_bold=True)
                else:
                    p.paragraph_format.space_before = Pt(6)
                    p.paragraph_format.space_after = Pt(2)
                    add_formatted_runs(p, h_text, default_size=Pt(11), default_color=COLOR_HEADING_4, default_bold=True, default_italic=True)

                idx += 1
                continue

        # 7. Itens de Lista Marcada (- ou *)
        bullet_match = re.match(r'^(\s*)[-*]\s+(.*)$', line)
        if bullet_match:
            indent_spaces = len(bullet_match.group(1))
            item_text = bullet_match.group(2)
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.75 + (indent_spaces // 2) * 0.5)
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(2)

            r_bullet = p.add_run("• ")
            r_bullet.bold = True
            r_bullet.font.name = 'Arial'
            r_bullet.font.size = Pt(11)
            r_bullet.font.color.rgb = COLOR_HEADING_3

            add_formatted_runs(p, item_text, default_size=Pt(11), default_color=COLOR_TEXT_DARK)
            idx += 1
            continue

        # 8. Itens de Lista Numerada (1. , 2. )
        num_match = re.match(r'^(\s*)(\d+)\.\s+(.*)$', line)
        if num_match:
            indent_spaces = len(num_match.group(1))
            num_str = num_match.group(2)
            item_text = num_match.group(3)
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.75 + (indent_spaces // 2) * 0.5)
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(2)

            r_num = p.add_run(f"{num_str}. ")
            r_num.bold = True
            r_num.font.name = 'Arial'
            r_num.font.size = Pt(11)
            r_num.font.color.rgb = COLOR_PRIMARY_NAVY

            add_formatted_runs(p, item_text, default_size=Pt(11), default_color=COLOR_TEXT_DARK)
            idx += 1
            continue

        # 9. Parágrafos Comuns (Texto Normal ABNT)
        p = doc.add_paragraph()
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(4)
        add_formatted_runs(p, line_stripped, default_size=Pt(12), default_color=COLOR_TEXT_DARK)

        idx += 1

    # Quebra de página ao final do módulo/capítulo
    doc.add_page_break()


def build_book(source_dir, output_filename, book_title, book_subtitle, area_label):
    """Compila todos os arquivos Markdown de um diretório em um Livro Digital Word (.docx)."""
    print(f"\n=======================================================")
    print(f"📖 Iniciando compilação: {output_filename}")
    print(f"📁 Diretório de origem: {source_dir}")
    print(f"=======================================================")

    doc = docx.Document()
    configure_document_abnt(doc)
    create_book_cover(doc, book_title, book_subtitle, area_label)

    files = sorted([
        f for f in glob.glob(os.path.join(source_dir, "**", "*.md"), recursive=True)
        if not os.path.basename(f).lower().startswith("readme")
    ])

    print(f"Total de arquivos temáticos identificados: {len(files)}")

    for i, file_path in enumerate(files, 1):
        rel_path = os.path.relpath(file_path, source_dir)
        print(f"  [{i:02d}/{len(files):02d}] Processando: {rel_path}")
        process_markdown_file(doc, file_path)

    doc.save(output_filename)
    file_size_mb = os.path.getsize(output_filename) / (1024 * 1024)
    print(f"✅ Livro gerado com sucesso: {output_filename} ({file_size_mb:.2f} MB)")


def main():
    base_dir = os.getcwd()

    books_config = [
        {
            "dir": os.path.join(base_dir, "fontes_de_estudo", "conhecimentos_gerais"),
            "output": os.path.join(base_dir, "Livro_Conhecimentos_Gerais.docx"),
            "title": "LIVRO DIGITAL — CONHECIMENTOS GERAIS",
            "subtitle": "Língua Portuguesa • Controle Externo • Legislação TCE-GO",
            "area": "Conhecimentos Gerais (Comum a Todos os Cargos)"
        },
        {
            "dir": os.path.join(base_dir, "fontes_de_estudo", "conhecimentos_especificos_b02_ti"),
            "output": os.path.join(base_dir, "Livro_Conhecimentos_TI.docx"),
            "title": "LIVRO DIGITAL — CONHECIMENTOS ESPECÍFICOS: TI",
            "subtitle": "Especialidade B02: Tecnologia da Informação • Engenharia de Software • Governança • Redes • Segurança",
            "area": "Especialidade B02 — Tecnologia da Informação"
        },
        {
            "dir": os.path.join(base_dir, "fontes_de_estudo", "conhecimentos_especificos_a01_tecnico_administrativo"),
            "output": os.path.join(base_dir, "Livro_Conhecimentos_Administrativo.docx"),
            "title": "LIVRO DIGITAL — CONHECIMENTOS ESPECÍFICOS: TÉCNICO ADMINISTRATIVO",
            "subtitle": "Especialidade A01: Direito Administrativo • Lei 14.133 • Constitucional • AFO • CASP • Gestão de Pessoas",
            "area": "Especialidade A01 — Técnico Administrativo"
        }
    ]

    for cfg in books_config:
        build_book(
            source_dir=cfg["dir"],
            output_filename=cfg["output"],
            book_title=cfg["title"],
            book_subtitle=cfg["subtitle"],
            area_label=cfg["area"]
        )

    print("\n🎉 Compilação dos 3 Livros Digitais concluída com absoluto sucesso!")


if __name__ == "__main__":
    main()

