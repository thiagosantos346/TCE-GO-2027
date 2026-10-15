# -*- coding: utf-8 -*-
"""
Script de Conversão Automatizada de Markdown para PDF com Layout ABNT
e Estilo Baseado no Guia_Estudos_TCE_GO_TI.html.
"""

import os
import re
import sys
import subprocess
import markdown
import pypdf

BASE_DIR = r"c:\Users\thiag\OneDrive\Desktop\Sefaz Go"
FONTES_DIR = os.path.join(BASE_DIR, "fontes_de_estudo")
EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
NODE_RENDERER = os.path.join(BASE_DIR, "render_html_to_pdf.js")

TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

def load_template_file(filename):
    """Carrega arquivo de template do diretório templates/ ou do diretório raiz."""
    paths = [
        os.path.join(TEMPLATES_DIR, filename),
        os.path.join(BASE_DIR, filename)
    ]
    for p in paths:
        if os.path.exists(p):
            with open(p, "r", encoding="utf-8") as f:
                return f.read()
    raise FileNotFoundError(f"Arquivo de template não encontrado: {filename}")

def get_base_css():
    return load_template_file("style.css")

def get_html_template():
    return load_template_file("template.html")

EXTRACTED_CSS = get_base_css()

def remove_emojis_for_pdf(text):
    """Remove emojis Unicode sem destruir quebras de linha Markdown ('  \n') ou indentação."""
    emoji_pattern = re.compile(
        "["
        "\U00010000-\U0010FFFF"
        "\u2600-\u27BF"
        "\u2300-\u23FF"
        "]+",
        flags=re.UNICODE
    )
    cleaned = emoji_pattern.sub("", text)
    cleaned = re.sub(r'(?<=\S)[ \t]{2,}(?=\S)', ' ', cleaned)
    return cleaned

def generate_toc_and_anchors(raw_md):
    """
    Analisa os títulos h2 (##) e h3 (###) do Markdown para:
    1. Inserir âncoras navegáveis (id)
    2. Construir um Sumário (TOC) automático com a estrutura do documento.
    """
    lines = raw_md.split('\n')
    processed_lines = []
    
    sections = [] # Lista de dicts: {"title": ..., "id": ..., "subs": [{"title": ..., "id": ...}]}
    current_sec = None
    sec_counter = 0
    sub_counter = 0

    for line in lines:
        h2_match = re.match(r'^##\s+(.+)$', line)
        h3_match = re.match(r'^###\s+(.+)$', line)

        if h2_match:
            sec_counter += 1
            raw_title = h2_match.group(1).strip()
            anchor_id = f"sec_{sec_counter}"
            
            clean_title = re.sub(r'[^\w\s-]', '', raw_title).strip()
            current_sec = {
                "title": raw_title,
                "clean_title": clean_title,
                "id": anchor_id,
                "subs": []
            }
            sections.append(current_sec)
            processed_lines.append(f'\n<div class="pdf-marker">[[SECTION:{raw_title}]]</div>')
            processed_lines.append(f'## <span id="{anchor_id}">{raw_title}</span>')

        elif h3_match and current_sec is not None:
            sub_counter += 1
            raw_title = h3_match.group(1).strip()
            anchor_id = f"sub_{sub_counter}"
            clean_title = re.sub(r'[^\w\s-]', '', raw_title).strip()
            
            current_sec["subs"].append({
                "title": raw_title,
                "clean_title": clean_title,
                "id": anchor_id
            })
            processed_lines.append(f'\n<div class="pdf-marker">[[SUBSECTION:{raw_title}]]</div>')
            processed_lines.append(f'### <span id="{anchor_id}">{raw_title}</span>')

        else:
            processed_lines.append(line)

    # Constrói o HTML do Sumário
    toc_html = []
    toc_html.append('<div class="toc-container" id="toc">')
    toc_html.append('<h2 class="toc-title">SUMÁRIO EXECUTIVO DO CONTEÚDO</h2>')
    toc_html.append('<div style="column-count: 2; column-gap: 22px;">')

    for idx, sec in enumerate(sections, 1):
        toc_html.append('<div class="toc-module-block">')
        toc_html.append(f'<h3><a href="#{sec["id"]}"><span class="toc-num">{idx:02d}.</span> {sec["title"]}</a></h3>')
        if sec["subs"]:
            toc_html.append('<ul>')
            for sidx, sub in enumerate(sec["subs"], 1):
                # Limita título no sumário se for muito longo
                display_sub = sub["title"]
                if len(display_sub) > 65:
                    display_sub = display_sub[:62] + "..."
                toc_html.append(f'<li><a href="#{sub["id"]}"><span class="toc-num">{idx}.{sidx}</span> {display_sub}</a></li>')
            toc_html.append('</ul>')
        toc_html.append('</div>')

    toc_html.append('</div>') # fecha columns
    toc_html.append('</div>') # fecha toc-container

    return '\n'.join(processed_lines), '\n'.join(toc_html)

def process_markdown_content(raw_md):
    """
    Processa o Markdown preservando KaTeX, Mermaid e aplicando estilos de FCC.
    """
    clean_md = remove_emojis_for_pdf(raw_md)
    text, toc_html = generate_toc_and_anchors(clean_md)

    # 1. Proteger blocos Mermaid
    mermaid_blocks = []
    def save_mermaid(m):
        code = m.group(1).strip()
        safe_code = code.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        mermaid_blocks.append(safe_code)
        return f"@@@MERMAID_BLOCK_{len(mermaid_blocks)-1}@@@"
    text = re.sub(r'```mermaid(.*?)```', save_mermaid, text, flags=re.DOTALL)

    # 2. Proteger símbolos de moeda (R$ e US$)
    text = re.sub(r'R\$(?=\s*\d)', r'R&dollar;', text)
    text = re.sub(r'US\$(?=\s*\d)', r'US&dollar;', text)

    # 3. Proteger expressões matemáticas LaTeX (Display e Inline)
    math_blocks = []
    def save_math(m):
        math_blocks.append(m.group(0))
        return f"@@@MATH_BLOCK_{len(math_blocks)-1}@@@"
    text = re.sub(r'\$\$.*?\$\$', save_math, text, flags=re.DOTALL)
    text = re.sub(r'(?<!\\)\$(?!\s)(.+?)(?<!\s)(?<!\\)\$', save_math, text)

    # 4. Garantir que opções de alternativas (A a E) tenham quebra de linha individual ('  \n')
    text = re.sub(
        r'(?m)^(\s*(?:[A-E]\)|\([A-E]\)|\*\s+\*\*[A-E]\)\*\*|\*\s+[A-E]\)|-\s+\*\*[A-E]\)\*\*|-\s+[A-E]\)))(.*?) *$',
        r'\1\2  ',
        text
    )

    # 5. Badges e Alertas
    text = re.sub(
        r'> \*\*Gabarito:\s*([A-E])\*\*',
        r'> <span class="gabarito-badge">GABARITO OFICIAL: \1</span>  \n>',
        text
    )
    text = re.sub(
        r'> \*\*Matéria:\*\* (.*?)\n> \*\*Cargo.*?\*\* (.*?)\n> \*\*Arquivo:\*\* (.*?)\n',
        r'<div class="topic-meta-box"><strong>Matéria:</strong> \1 &nbsp;|&nbsp; <strong>Cargo:</strong> \2</div>\n',
        text,
        flags=re.DOTALL
    )

    text = re.sub(r'> \[!NOTE\]\s*', r'> <strong class="alert-label note">[NOTA]:</strong> ', text)
    text = re.sub(r'> \[!IMPORTANT\]\s*', r'> <strong class="alert-label important">[IMPORTANTE]:</strong> ', text)
    text = re.sub(r'> \[!WARNING\]\s*', r'> <strong class="alert-label warning">[ALERTA DE PROVA / PEGADINHA FCC]:</strong> ', text)
    text = re.sub(r'> \[!CAUTION\]\s*', r'> <strong class="alert-label warning">[ATENÇÃO / CUIDADO]:</strong> ', text)
    text = re.sub(r'> \[!TIP\]\s*', r'> <strong class="alert-label tip">[DICA]:</strong> ', text)

    text = re.sub(r'> \*\*ALERTA DE PROVA / PEGADINHA FCC:\*\*', r'> <strong class="alert-label warning">[ALERTA DE PROVA / PEGADINHA FCC]:</strong>', text)
    text = re.sub(r'> \*\*IMPORTANTE(.*?):\*\*', r'> <strong class="alert-label important">[IMPORTANTE\1]:</strong>', text)
    text = re.sub(r'> \*\*NOTA EXPLICATIVA(.*?):\*\*', r'> <strong class="alert-label note">[NOTA EXPLICATIVA\1]:</strong>', text)
    text = re.sub(r'> \*\*ATENÇÃO(.*?):\*\*', r'> <strong class="alert-label warning">[ATENÇÃO\1]:</strong>', text)
    text = re.sub(r'> \*\*DICA(.*?):\*\*', r'> <strong class="alert-label tip">[DICA\1]:</strong>', text)

    # 6. Compilar Markdown para HTML
    html = markdown.markdown(text, extensions=['extra', 'sane_lists'])

    # 7. Restaurar Matemática
    for i, mb in enumerate(math_blocks):
        html = html.replace(f"@@@MATH_BLOCK_{i}@@@", mb)

    # 8. Restaurar Mermaid encapsulado em container controlado
    for i, code in enumerate(mermaid_blocks):
        block_html = f'<div class="mermaid-container"><pre class="mermaid">\n{code}\n</pre></div>'
        html = html.replace(f"<p>@@@MERMAID_BLOCK_{i}@@@</p>", block_html)
        html = html.replace(f"@@@MERMAID_BLOCK_{i}@@@", block_html)

    # 9. Envelopamento das questões comentadas em .question-card (anti-quebra)
    pattern = r'(<h3>(?:<span[^>]*>)?Questão\s+\d+.*?)(?=(?:<h3>(?:<span[^>]*>)?Questão\s+\d+|<h2|<h1|\Z))'
    html = re.sub(pattern, r'<div class="question-card">\n\1\n</div>\n', html, flags=re.DOTALL)

    return toc_html, html

def build_complete_html(toc_html, content_html, title="Guia de Estudos TCE-GO"):
    """
    Gera o documento HTML completo pronto para renderização pelo Puppeteer
    utilizando o template e CSS externos compartilhados com build_all_guides.py.
    """
    template = get_html_template()
    css = get_base_css()
    return (template
            .replace("{{TITLE}}", title).replace("__TITLE__", title)
            .replace("{{CSS}}", css).replace("__CSS__", css)
            .replace("{{COVER}}", "").replace("__COVER__", "")
            .replace("{{TOC}}", toc_html).replace("__TOC__", toc_html)
            .replace("{{CONTENT}}", content_html).replace("__CONTENT__", content_html))

def inject_bookmarks(raw_pdf_path, final_pdf_path):
    """
    Adiciona Bookmarks (menu lateral hierárquico) ao PDF final.
    """
    print(f"[pypdf] Indexando marcadores no menu lateral de {os.path.basename(final_pdf_path)}...")
    reader = pypdf.PdfReader(raw_pdf_path)
    writer = pypdf.PdfWriter()
    writer.append(reader)

    writer.add_outline_item("Sumário Geral", 0)

    current_sec_outline = None

    for p_num, page in enumerate(reader.pages):
        txt = page.extract_text()
        if not txt:
            continue

        sec_matches = re.findall(r'\[\[SECTION:(.*?)\]\]', txt)
        for s_title in sec_matches:
            current_sec_outline = writer.add_outline_item(s_title.strip(), p_num)

        sub_matches = re.findall(r'\[\[SUBSECTION:(.*?)\]\]', txt)
        for sub_title in sub_matches:
            if current_sec_outline:
                writer.add_outline_item(sub_title.strip(), p_num, parent=current_sec_outline)
            else:
                writer.add_outline_item(sub_title.strip(), p_num)

    with open(final_pdf_path, 'wb') as f_out:
        writer.write(f_out)
    print(f"[pypdf] Indexação concluída! Total de páginas: {len(reader.pages)}")

def convert_markdown_file(md_path, output_pdf_path):
    print(f"\n=======================================================")
    print(f"Iniciando conversão de:")
    print(f"MD:  {md_path}")
    print(f"PDF: {output_pdf_path}")
    print(f"=======================================================\n")

    with open(md_path, 'r', encoding='utf-8') as f:
        raw_md = f.read()

    # Extrai título
    first_line = raw_md.split('\n')[0].replace('#', '').strip()
    title = first_line if first_line else "Guia de Estudos TCE-GO"

    print("1. Processando Markdown, gerando Sumário, KaTeX e Mermaid...")
    toc_html, content_html = process_markdown_content(raw_md)

    full_html = build_complete_html(toc_html, content_html, title=title)

    # Grava o HTML temporário no mesmo diretório de fontes_de_estudo para resolver assets relativos
    html_temp_path = os.path.splitext(output_pdf_path)[0] + ".html"
    with open(html_temp_path, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f"2. HTML compilado gerado: {html_temp_path}")

    raw_pdf_temp = os.path.splitext(output_pdf_path)[0] + "_raw.pdf"

    print("3. Executando Puppeteer (Edge Headless) com regras ABNT...")
    node_cmd = ["node", NODE_RENDERER, html_temp_path, raw_pdf_temp]
    result = subprocess.run(node_cmd, capture_output=True, text=True, cwd=BASE_DIR)

    if result.returncode != 0:
        print("[Erro no Puppeteer]:", result.stderr)
        raise RuntimeError("Falha na renderização do PDF pelo Puppeteer.")

    print(result.stdout.strip())

    print("4. Indexando marcadores no PDF...")
    inject_bookmarks(raw_pdf_temp, output_pdf_path)

    # Limpeza de arquivos intermediários
    if os.path.exists(raw_pdf_temp):
        os.remove(raw_pdf_temp)

    print(f"\n[SUCESSO] PDF gerado com sucesso em: {output_pdf_path}")

if __name__ == "__main__":
    test_md = os.path.join(
        FONTES_DIR,
        "conhecimentos_especificos_b02_ti",
        "09_inteligencia_artificial_e_ciencia_de_dados",
        "01_fundamentos_ia_machine_learning_e_deep_learning.md"
    )
    output_pdf = os.path.join(FONTES_DIR, "previa_layout_real.pdf")

    convert_markdown_file(test_md, output_pdf)
