# -*- coding: utf-8 -*-
"""
Compilador Profissional Unificado de Alta Resolução TCE-GO
CARGO B02: TÉCNICO DE CONTROLE EXTERNO – ESPECIALIDADE: TECNOLOGIA DA INFORMAÇÃO
- Formatação matemática tipográfica nativa de alta precisão (Frações com traço, potências, conjuntos).
- Diagramas vetoriais Mermaid renderizados em SVG puro (sem foreignObject, sem blocos vazios).
- Envelopamento de questões comentadas pós-compilação (preservação 100% da formatação e anti-quebra).
- Fundo 100% de ponta a ponta sem bordas brancas (Sépia #fbf7ee e Drácula #282a36).
- Indexação hierárquica completa em PDF (Menu Lateral / Bookmarks para todos os Módulos e Tópicos).
"""

import os
import re
import subprocess
import time
import shutil
import tempfile
import markdown
import pypdf

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONTES_DIR = os.path.join(BASE_DIR, "fontes_de_estudo")
GERAIS_DIR = os.path.join(FONTES_DIR, "conhecimentos_gerais")
ESPECIFICOS_TI_DIR = os.path.join(FONTES_DIR, "conhecimentos_especificos_b02_ti")
EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

def get_module_dir(mod):
    p_gerais = os.path.join(GERAIS_DIR, mod)
    if os.path.isdir(p_gerais):
        return p_gerais
    p_ti = os.path.join(ESPECIFICOS_TI_DIR, mod)
    if os.path.isdir(p_ti):
        return p_ti
    return os.path.join(FONTES_DIR, mod)


MODULE_TITLES = {
    "01_lingua_portuguesa": "Módulo 01: Língua Portuguesa",
    "02_matematica_e_raciocinio_logico": "Módulo 02: Matemática e Raciocínio Lógico",
    "03_legislacao_institucional": "Módulo 03: Legislação Institucional (TCE-GO & Goiás)",
    "04_engenharia_de_software": "Módulo 04: Engenharia de Software",
    "05_desenvolvimento_de_sistemas": "Módulo 05: Desenvolvimento de Sistemas",
    "06_engenharia_software_ia_e_sistemas_agentivos": "Módulo 06: Engenharia de Software Assistida por IA e Agentes",
    "07_devops_e_plataforma_de_entrega": "Módulo 07: DevOps, Plataforma e Entrega Contínua",
    "08_banco_de_dados": "Módulo 08: Banco de Dados Relacional e NoSQL",
    "09_inteligencia_artificial_e_ciencia_de_dados": "Módulo 09: Inteligência Artificial, Ciência de Dados e Automação",
    "10_seguranca_da_informacao": "Módulo 10: Segurança da Informação e Cibersegurança",
    "11_sistemas_operacionais_redes_e_nuvem": "Módulo 11: Sistemas Operacionais, Redes e Computação em Nuvem",
    "12_governanca_de_ti": "Módulo 12: Governança e Gestão de TI",
    "13_legislacao_aplicada_a_ti": "Módulo 13: Legislação Aplicada à Tecnologia da Informação",
    "14_lingua_inglesa_leitura_tecnica": "Módulo 14: Língua Inglesa (Leitura Técnica)",
}

def render_math_to_clean_html(text):
    """Converte comandos LaTeX em elementos HTML tipográficos estilizados com Cambria Math."""
    code_blocks = []
    def save_code(m):
        code_blocks.append(m.group(0))
        return f"@@@CODE_BLOCK_{len(code_blocks)-1}@@@"
    
    text = re.sub(r'```.*?```', save_code, text, flags=re.DOTALL)
    text = re.sub(r'`[^`]+`', save_code, text)

    syms = [
        (r'\\mathbb\{N\}', 'ℕ'),
        (r'\\mathbb\{Z\}', 'ℤ'),
        (r'\\mathbb\{Q\}', 'ℚ'),
        (r'\\mathbb\{R\}', 'ℝ'),
        (r'\\rightarrow', ' → '),
        (r'\\leftarrow', ' ← '),
        (r'\\leftrightarrow', ' ↔ '),
        (r'\\implies', ' ⇒ '),
        (r'\\Rightarrow', ' ⇒ '),
        (r'\\equiv', ' ≡ '),
        (r'\\approx', ' ≈ '),
        (r'\\land', ' ∧ '),
        (r'\\lor', ' ∨ '),
        (r'\\underline\{\\lor\}', ' ⊻ '),
        (r'\\neg', '¬'),
        (r'\\sim', '¬'),
        (r'\\le\b', '≤'),
        (r'\\ge\b', '≥'),
        (r'\\ne\b', '≠'),
        (r'\\neq\b', '≠'),
        (r'\\subset', '⊂'),
        (r'\\cap', '∩'),
        (r'\\cup', '∪'),
        (r'\\emptyset', '∅'),
        (r'\\times', ' × '),
        (r'\\cdot', ' · '),
        (r'\\dots', '...'),
        (r'\\cdots', '···'),
        (r'\\Delta', 'Δ'),
        (r'\\sum', '∑'),
        (r'\\in\b', '∈'),
        (r'\\notin\b', '∉'),
        (r'\\sqrt\{([^{}]+)\}', r'√(\1)'),
        (r'\\sqrt', '√'),
        (r'\\text\{([^}]*)\}', r'\1'),
        (r'\\textbf\{([^}]*)\}', r'<strong>\1</strong>'),
        (r'\\textit\{([^}]*)\}', r'<em>\1</em>'),
        (r'\\quad', ' &nbsp; '),
        (r'\\qquad', ' &nbsp;&nbsp; '),
        (r'\\left\(', '('),
        (r'\\right\)', ')'),
        (r'\\left\[', '['),
        (r'\\right\]', ']'),
    ]

    for pat, rep in syms:
        text = re.sub(pat, rep, text)

    # Frações verticais tipográficas com traço de divisão
    for _ in range(3):
        text = re.sub(
            r'\\frac\{([^{}]+)\}\{([^{}]+)\}',
            r'<span class="math-frac"><span class="math-num">\1</span><span class="math-den">\2</span></span>',
            text
        )

    # Potências e subscritos
    text = re.sub(r'\^\{([^{}]+)\}', r'<sup>\1</sup>', text)
    text = re.sub(r'\^([0-9a-zA-Z]+)', r'<sup>\1</sup>', text)
    text = re.sub(r'_\{([^{}]+)\}', r'<sub>\1</sub>', text)
    text = re.sub(r'_([0-9a-zA-Z]+)', r'<sub>\1</sub>', text)

    # Delimitadores matemáticos display $$ e inline $
    text = re.sub(r'\$\$(.*?)\$\$', r'<div class="math-display">\1</div>', text, flags=re.DOTALL)
    text = re.sub(r'(?<!\\)\$([^\$\n]+?)(?<!\\)\$', r'<span class="math-inline">\1</span>', text)

    for i, c in enumerate(code_blocks):
        text = text.replace(f"@@@CODE_BLOCK_{i}@@@", c)

    return text

def process_markdown(raw_md):
    """Compila markdown preservando rich text, diagramas Mermaid e questões completas."""
    def repl_mermaid(m):
        code = m.group(1).strip()
        safe_code = code.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        return f'\n\n<pre class="mermaid">\n{safe_code}\n</pre>\n\n'

    content = re.sub(r'```mermaid(.*?)```', repl_mermaid, raw_md, flags=re.DOTALL)

    content = re.sub(r'R\$(?=\s*\d)', r'R&dollar;', content)
    content = re.sub(r'US\$(?=\s*\d)', r'US&dollar;', content)

    content = render_math_to_clean_html(content)

    content = re.sub(
        r'> \*\*Gabarito:\s*([A-E])\*\*',
        r'> <span class="gabarito-badge">GABARITO OFICIAL: \1</span>',
        content
    )
    content = re.sub(
        r'> \*\*Matéria:\*\* (.*?)\n> \*\*Cargo.*?\*\* (.*?)\n> \*\*Arquivo:\*\* (.*?)\n',
        r'<div class="topic-meta-box"><strong>📚 Matéria:</strong> \1 &nbsp;|&nbsp; <strong>🎯 Cargo:</strong> \2</div>\n',
        content,
        flags=re.DOTALL
    )

    content = re.sub(r'> \[!NOTE\]\s*', r'> <strong class="alert-label note">ℹ️ NOTA:</strong> ', content)
    content = re.sub(r'> \[!IMPORTANT\]\s*', r'> <strong class="alert-label important">⭐ IMPORTANTE:</strong> ', content)
    content = re.sub(r'> \[!WARNING\]\s*', r'> <strong class="alert-label warning">⚠️ ALERTA DE PROVA / PEGADINHA FCC:</strong> ', content)
    content = re.sub(r'> \[!CAUTION\]\s*', r'> <strong class="alert-label warning">🛑 CUIDADO / ATENÇÃO:</strong> ', content)
    content = re.sub(r'> \[!TIP\]\s*', r'> <strong class="alert-label tip">💡 DICA:</strong> ', content)

    content = re.sub(r'> 🚨 \*\*ALERTA DE PROVA / PEGADINHA FCC:\*\*', r'> <strong class="alert-label warning">🚨 ALERTA DE PROVA / PEGADINHA FCC:</strong>', content)
    content = re.sub(r'> ⭐ \*\*IMPORTANTE(.*?):\*\*', r'> <strong class="alert-label important">⭐ IMPORTANTE\1:</strong>', content)
    content = re.sub(r'> 📌 \*\*NOTA EXPLICATIVA(.*?):\*\*', r'> <strong class="alert-label note">📌 NOTA EXPLICATIVA\1:</strong>', content)
    content = re.sub(r'> 🛑 \*\*ATENÇÃO(.*?):\*\*', r'> <strong class="alert-label warning">🛑 ATENÇÃO\1:</strong>', content)
    content = re.sub(r'> 💡 \*\*DICA(.*?):\*\*', r'> <strong class="alert-label tip">💡 DICA\1:</strong>', content)

    # 1. Compilação de Markdown com Python-Markdown
    html = markdown.markdown(content, extensions=['extra', 'sane_lists'])

    # 2. Envelopamento das questões DEPOIS do markdown (preserva 100% da formatação e badges!)
    pattern = r'(<h3>Questão\s+\d+.*?)(?=(?:<h3>Questão\s+\d+|<h2|<h1|\Z))'
    html = re.sub(pattern, r'<div class="question-card">\n\1\n</div>\n', html, flags=re.DOTALL)

    return html

def get_theme_css(theme):
    if theme == 'dracula':
        bg_page = "#282a36"
        bg_card = "#343746"
        bg_surface = "#21222c"
        text_main = "#f8f8f2"
        text_heading = "#bd93f9"
        border_card = "#44475a"
        accent_blue = "#8be9fd"
        badge_bg = "#50fa7b"
        badge_text = "#282a36"
        code_bg = "#1e1f29"
        code_text = "#50fa7b"
        quote_bg = "#21222c"
        quote_border = "#ff79c6"
        table_th = "#44475a"
        table_th_text = "#8be9fd"
        table_alt = "#2c2e3c"
    elif theme == 'sepia':
        bg_page = "#fbf7ee"
        bg_card = "#ffffff"
        bg_surface = "#f5ede0"
        text_main = "#2b261f"
        text_heading = "#1e3a5f"
        border_card = "#e4d7c5"
        accent_blue = "#1d4ed8"
        badge_bg = "#16a34a"
        badge_text = "#ffffff"
        code_bg = "#f4eee2"
        code_text = "#991b1b"
        quote_bg = "#f7f2e7"
        quote_border = "#d97706"
        table_th = "#1e3a5f"
        table_th_text = "#ffffff"
        table_alt = "#f9f5ec"
    else: # padrao / white
        bg_page = "#ffffff"
        bg_card = "#ffffff"
        bg_surface = "#f8fafc"
        text_main = "#1e293b"
        text_heading = "#0f294a"
        border_card = "#cbd5e1"
        accent_blue = "#2563eb"
        badge_bg = "#16a34a"
        badge_text = "#ffffff"
        code_bg = "#f8fafc"
        code_text = "#b91c1c"
        quote_bg = "#f0fdf4"
        quote_border = "#16a34a"
        table_th = "#0f294a"
        table_th_text = "#ffffff"
        table_alt = "#f8fafc"

    return f"""
        @page {{
            size: A4;
            margin: 0;
        }}
        * {{
            box-sizing: border-box;
            -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
        }}
        html, body {{
            margin: 0;
            padding: 0;
            background-color: {bg_page} !important;
            color: {text_main};
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            font-size: 9.8pt;
            line-height: 1.58;
            width: 100%;
        }}
        .page-container {{
            padding: 16mm 14mm 16mm 14mm;
            background-color: {bg_page};
            width: 100%;
            min-height: 100%;
        }}

        /* CAPA */
        .cover-page {{
            page-break-after: always;
            break-after: always;
            min-height: 85vh;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            text-align: center;
            padding: 35px 20px;
            border: 3px double {border_card};
            border-radius: 10px;
            background: {bg_card};
            margin-bottom: 30px;
        }}
        .cover-institution {{
            font-size: 13pt;
            font-weight: 800;
            letter-spacing: 2px;
            color: {text_heading};
            text-transform: uppercase;
            margin-bottom: 6px;
        }}
        .cover-jurisdiction {{
            font-size: 10.5pt;
            color: {text_main};
            text-transform: uppercase;
            letter-spacing: 1.5px;
            opacity: 0.85;
        }}
        .cover-title {{
            font-size: 24pt;
            font-weight: 900;
            color: {text_heading};
            line-height: 1.25;
            margin: 25px 0 10px 0;
        }}
        .cover-subtitle {{
            font-size: 12pt;
            font-weight: 600;
            color: {accent_blue};
            margin-bottom: 25px;
        }}
        .cover-badges {{
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-bottom: 25px;
            flex-wrap: wrap;
        }}
        .badge-pill {{
            background: {bg_surface};
            color: {text_main};
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 9pt;
            font-weight: 700;
            border: 1px solid {border_card};
        }}
        .cover-stats-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
            max-width: 650px;
            margin: 0 auto;
        }}
        .stat-card {{
            background: {bg_surface};
            border: 1px solid {border_card};
            border-radius: 8px;
            padding: 14px 10px;
        }}
        .stat-num {{
            font-size: 20pt;
            font-weight: 900;
            color: {text_heading};
            line-height: 1;
        }}
        .stat-lbl {{
            font-size: 7.5pt;
            text-transform: uppercase;
            font-weight: 700;
            opacity: 0.8;
            margin-top: 4px;
        }}
        .cover-footer {{
            font-size: 8.5pt;
            opacity: 0.75;
            margin-top: 25px;
        }}

        /* SUMÁRIO */
        .toc-container {{
            page-break-after: always;
            break-after: always;
            background: {bg_card};
            border: 1px solid {border_card};
            border-radius: 8px;
            padding: 24px;
            margin-bottom: 35px;
        }}
        .toc-title {{
            font-size: 16pt;
            font-weight: 800;
            color: {text_heading};
            margin: 0 0 16px 0;
            border-bottom: 2px solid {accent_blue};
            padding-bottom: 6px;
        }}
        .toc-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 16px;
        }}
        .toc-module-block {{
            background: {bg_surface};
            border: 1px solid {border_card};
            border-radius: 6px;
            padding: 10px 14px;
        }}
        .toc-module-block h3 {{
            font-size: 9.5pt;
            margin: 0 0 6px 0;
            color: {text_heading};
        }}
        .toc-module-block ul {{
            list-style: none;
            padding-left: 0;
            margin: 0;
            font-size: 8.5pt;
        }}
        .toc-module-block li {{
            margin-bottom: 3px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }}
        .toc-module-block a {{
            color: {text_main};
            text-decoration: none;
        }}
        .toc-module-block a:hover {{
            color: {accent_blue};
            text-decoration: underline;
        }}

        /* DIVISOR DE MÓDULO */
        .module-divider {{
            page-break-before: always;
            break-before: always;
            background: {table_th};
            color: #ffffff;
            border-radius: 8px;
            padding: 24px 20px;
            margin: 35px 0 25px 0;
            text-align: center;
            box-shadow: 0 3px 8px rgba(0,0,0,0.08);
            page-break-after: avoid !important;
            break-after: avoid !important;
        }}
        .module-badge {{
            display: inline-block;
            background: rgba(255,255,255,0.15);
            font-size: 7.5pt;
            font-weight: 800;
            letter-spacing: 1.5px;
            padding: 3px 10px;
            border-radius: 12px;
            margin-bottom: 8px;
            text-transform: uppercase;
        }}
        .module-title {{
            font-size: 17pt;
            font-weight: 800;
            margin: 0 0 6px 0;
            color: #ffffff;
        }}
        .module-subtitle {{
            font-size: 9pt;
            opacity: 0.85;
            margin: 0;
        }}

        /* TÓPICOS */
        .topic-section {{
            margin-bottom: 35px;
            page-break-before: always;
            break-before: always;
        }}
        h1 {{
            font-size: 15pt;
            font-weight: 800;
            color: {text_heading};
            border-bottom: 2.5px solid {accent_blue};
            padding-bottom: 6px;
            margin-top: 10px;
            margin-bottom: 14px;
            page-break-after: avoid !important;
            break-after: avoid !important;
        }}
        h2 {{
            font-size: 12pt;
            font-weight: 700;
            color: {text_heading};
            margin-top: 22px;
            margin-bottom: 10px;
            border-left: 4px solid {accent_blue};
            padding-left: 10px;
            page-break-after: avoid !important;
            break-after: avoid !important;
        }}
        h3 {{
            font-size: 10.5pt;
            font-weight: 700;
            color: {text_heading};
            margin-top: 16px;
            margin-bottom: 8px;
            page-break-after: avoid !important;
            break-after: avoid !important;
        }}
        h4 {{
            font-size: 9.5pt;
            font-weight: 700;
            margin-top: 12px;
            margin-bottom: 6px;
            page-break-after: avoid !important;
            break-after: avoid !important;
        }}

        .topic-meta-box {{
            background: {bg_card};
            border: 1px solid {border_card};
            border-radius: 6px;
            padding: 8px 14px;
            margin-bottom: 16px;
            font-size: 8.8pt;
            break-inside: avoid !important;
        }}

        /* CARTÕES DE QUESTÕES (ISOLAMENTO CONTRA CORTE DE PÁGINA) */
        .question-card {{
            background: {bg_card};
            border: 1.5px solid {border_card};
            border-radius: 8px;
            padding: 16px 20px;
            margin: 20px 0;
            box-shadow: 0 1px 4px rgba(0,0,0,0.04);
            page-break-inside: avoid !important;
            break-inside: avoid !important;
        }}
        .question-card h3 {{
            margin-top: 0;
            color: {text_heading};
            font-size: 10.5pt;
            border-bottom: 1px dashed {border_card};
            padding-bottom: 6px;
        }}

        .gabarito-badge {{
            display: inline-block;
            background: {badge_bg};
            color: {badge_text};
            font-weight: 800;
            font-size: 8.5pt;
            padding: 3px 8px;
            border-radius: 4px;
            margin-bottom: 6px;
        }}

        /* ALERTAS E CITAÇÕES */
        blockquote {{
            margin: 14px 0;
            padding: 12px 16px;
            background: {quote_bg};
            border-left: 4px solid {quote_border};
            border-radius: 0 6px 6px 0;
            font-size: 9.2pt;
            page-break-inside: avoid !important;
            break-inside: avoid !important;
        }}
        blockquote p {{
            margin: 4px 0;
        }}
        .alert-label {{
            font-weight: 700;
        }}

        /* DIAGRAMAS MERMAID */
        .mermaid {{
            background: {bg_card};
            border: 1px solid {border_card};
            border-radius: 6px;
            padding: 14px;
            margin: 16px auto;
            text-align: center;
            max-width: 100%;
            overflow: hidden;
            page-break-inside: avoid !important;
            break-inside: avoid !important;
        }}
        .mermaid svg {{
            display: inline-block;
            max-width: 100% !important;
            max-height: 480px !important;
            height: auto !important;
        }}

        /* TABELAS */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 16px 0;
            font-size: 8.8pt;
        }}
        thead {{
            display: table-header-group;
        }}
        tr {{
            page-break-inside: avoid !important;
            break-inside: avoid !important;
        }}
        th, td {{
            border: 1px solid {border_card};
            padding: 7px 10px;
            text-align: left;
        }}
        th {{
            background: {table_th};
            color: {table_th_text};
            font-weight: 700;
        }}
        tr:nth-child(even) {{
            background: {table_alt};
        }}

        /* CÓDIGOS */
        pre {{
            background: {code_bg};
            border: 1px solid {border_card};
            border-radius: 6px;
            padding: 10px 14px;
            font-size: 8pt;
            line-height: 1.45;
            overflow-x: auto;
            page-break-inside: avoid !important;
            break-inside: avoid !important;
        }}
        code {{
            font-family: 'Consolas', 'Cascadia Code', 'Courier New', monospace;
            font-size: 8.5pt;
            color: {code_text};
            background: {code_bg};
            padding: 2px 4px;
            border-radius: 3px;
        }}
        pre code {{
            background: transparent;
            color: inherit;
            padding: 0;
        }}

        /* MATEMÁTICA TIPOGRÁFICA DE ALTA PRECISÃO */
        .math-display {{
            background: {bg_surface};
            border-left: 3px solid {accent_blue};
            padding: 10px 16px;
            margin: 12px 0;
            font-family: 'Cambria Math', 'Latin Modern Math', Georgia, serif;
            font-size: 11pt;
            text-align: center;
            border-radius: 4px;
            page-break-inside: avoid !important;
            break-inside: avoid !important;
        }}
        .math-inline {{
            font-family: 'Cambria Math', 'Latin Modern Math', Georgia, serif;
            font-size: 10pt;
            font-style: normal;
            color: {accent_blue};
            padding: 0 2px;
        }}
        .math-frac {{
            display: inline-flex;
            flex-direction: column;
            vertical-align: middle;
            text-align: center;
            padding: 0 3px;
            font-size: 0.88em;
            line-height: 1.1;
        }}
        .math-num {{
            border-bottom: 1.2px solid currentColor;
            padding-bottom: 1px;
        }}
        .math-den {{
            padding-top: 1px;
        }}

        a {{
            color: {accent_blue};
            text-decoration: underline;
        }}

        /* Marcadores invisíveis para indexação em PDF */
        .pdf-marker {{
            position: absolute;
            width: 1px;
            height: 1px;
            overflow: hidden;
            opacity: 0.01;
            color: transparent;
            font-size: 1pt;
        }}
    """

def generate_ti_html(theme='sepia'):
    modules = [mod for mod in sorted(MODULE_TITLES.keys()) if os.path.isdir(get_module_dir(mod))]
    
    toc_html = []
    content_html = []
    
    topic_counter = 0
    question_counter = 0

    for mod in modules:
        mod_title = MODULE_TITLES.get(mod, mod.replace('_', ' ').title())
        mod_id = f"mod_{mod}"
        mod_dir = get_module_dir(mod)
        
        files = sorted([f for f in os.listdir(mod_dir) if f.endswith('.md') and f != 'README.md'])
        
        toc_html.append(f'<div class="toc-module-block">')
        toc_html.append(f'<h3><a href="#{mod_id}">{mod_title}</a></h3>')
        toc_html.append('<ul>')
        
        # Marcador de módulo para o extrator de PDF Outline
        content_html.append(f'''
        <div class="pdf-marker">[[MODULE:{mod_title}]]</div>
        <div class="module-divider" id="{mod_id}">
            <div class="module-badge">CONCURSO TCE-GO • BANCA FCC</div>
            <h1 class="module-title">{mod_title}</h1>
            <p class="module-subtitle">Conteúdo Teórico Estruturado, Diagramas Vetoriais e Bateria de Questões FCC</p>
        </div>
        ''')
        
        for f in files:
            topic_counter += 1
            topic_id = f"topic_{topic_counter}"
            filepath = os.path.join(mod_dir, f)
            
            with open(filepath, 'r', encoding='utf-8') as fh:
                raw_md = fh.read()
            
            q_matches = len(re.findall(r'### Questão\s+\d+', raw_md, re.IGNORECASE))
            question_counter += q_matches

            first_line = raw_md.split('\n')[0].replace('#', '').strip()
            if not first_line:
                first_line = f.replace('.md', '').replace('_', ' ').title()
                
            toc_html.append(f'<li><a href="#{topic_id}"><span class="toc-num">{topic_counter:02d}.</span> {first_line}</a></li>')
            
            html_chunk = process_markdown(raw_md)
            
            # Marcador de tópico para o extrator de PDF Outline
            topic_bookmark_title = f"{topic_counter:02d}. {first_line}"
            content_html.append(f'''
            <article class="topic-section" id="{topic_id}">
                <div class="pdf-marker">[[TOPIC:{topic_bookmark_title}]]</div>
                {html_chunk}
            </article>
            ''')
            
        toc_html.append('</ul></div>')
        
    toc_rendered = '\n'.join(toc_html)
    content_rendered = '\n'.join(content_html)

    theme_label = "Modo Sépia (Papel Suave)" if theme == 'sepia' else ("Modo Drácula (VS Code Oficial)" if theme == 'dracula' else "Modo Padrão (Papel Branco)")
    mermaid_theme = "dark" if theme == 'dracula' else "default"

    full_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Guia de Estudos TCE-GO - TI ({theme_label})</title>
    <script src="assets/mermaid.min.js"></script>
    <style>
        {get_theme_css(theme)}
    </style>
</head>
<body>
    <div class="page-container">
        <!-- CAPA -->
        <div class="cover-page">
            <div class="cover-header">
                <div class="cover-institution">Estado de Goiás • Tribunal de Contas do Estado</div>
                <div class="cover-jurisdiction">Concurso Público • Especialidade: Tecnologia da Informação</div>
            </div>

            <div class="cover-body">
                <div class="cover-title">GUIA DEFINITIVO DE ESTUDOS<br>& QUESTÕES COMENTADAS</div>
                <div class="cover-subtitle">14 Módulos Teóricos • Diagramas Vetoriais • Notações Matemáticas • Banca FCC</div>

                <div class="cover-badges">
                    <span class="badge-pill">Cargo B02: Tecnologia da Informação</span>
                    <span class="badge-pill">Banca Oficial: Fundação Carlos Chagas (FCC)</span>
                    <span class="badge-pill">Edição: {theme_label}</span>
                </div>

                <div class="cover-stats-grid">
                    <div class="stat-card">
                        <div class="stat-num">14</div>
                        <div class="stat-lbl">Módulos</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-num">{topic_counter}</div>
                        <div class="stat-lbl">Tópicos</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-num">{question_counter}</div>
                        <div class="stat-lbl">Questões FCC</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-num">100%</div>
                        <div class="stat-lbl">Edital Mapeado</div>
                    </div>
                </div>
            </div>

            <div class="cover-footer">
                Compilação Oficial de Alta Resolução &bull; Padrões ISO/NIST, RFCs IETF, Leis Federais e Legislação de Goiás
            </div>
        </div>

        <!-- SUMÁRIO -->
        <div class="toc-container" id="toc">
            <h2 class="toc-title">SUMÁRIO GERAL DO CONTEÚDO PROGRAMÁTICO</h2>
            <div class="toc-grid">
                {toc_rendered}
            </div>
        </div>

        <!-- CONTEÚDO PRINCIPAL -->
        {content_rendered}
    </div>

    <script>
        document.addEventListener("DOMContentLoaded", async function() {{
            try {{
                mermaid.initialize({{
                    startOnLoad: false,
                    theme: '{mermaid_theme}',
                    securityLevel: 'loose',
                    flowchart: {{ htmlLabels: false, useMaxWidth: true, curve: 'basis' }},
                    sequence: {{ useMaxWidth: true }}
                }});

                const els = document.querySelectorAll('.mermaid');
                for (let i = 0; i < els.length; i++) {{
                    try {{
                        await mermaid.run({{ nodes: [els[i]] }});
                    }} catch (err) {{
                        console.warn("Diagrama " + i + " tratado com fallback:", err);
                        els[i].style.whiteSpace = "pre";
                        els[i].style.fontFamily = "Consolas, monospace";
                        els[i].style.fontSize = "8pt";
                        els[i].style.textAlign = "left";
                    }}
                }}
            }} catch(e) {{
                console.warn("Aviso global Mermaid:", e);
            }}
            document.body.setAttribute('data-ready', 'true');
        }});
    </script>
</body>
</html>"""
    return full_html, topic_counter, question_counter

def print_pdf_raw(html_path, pdf_path, virtual_time_ms=30000):
    """Executa o Microsoft Edge Headless para transformar HTML em PDF bruto."""
    tmp_profile = os.path.join(tempfile.gettempdir(), "edge_pdf_" + str(int(time.time()*1000)))
    os.makedirs(tmp_profile, exist_ok=True)
    
    cmd = [
        EDGE_PATH,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        f"--user-data-dir={tmp_profile}",
        f"--virtual-time-budget={virtual_time_ms}",
        "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={pdf_path}",
        html_path
    ]
    
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=360)
    except subprocess.TimeoutExpired:
        print(f"Aviso: Timeout no processo Edge para {pdf_path}.")
    
    shutil.rmtree(tmp_profile, ignore_errors=True)
    return os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 0

def inject_bookmarks_and_finalize(raw_pdf_path, final_pdf_path):
    """Lê o PDF gerado, indexa todos os módulos e tópicos e gera os Bookmarks no Menu Lateral."""
    print(f"Indexando bookmarks no menu lateral de {os.path.basename(final_pdf_path)}...")
    reader = pypdf.PdfReader(raw_pdf_path)
    writer = pypdf.PdfWriter()
    writer.append(reader)

    current_module_outline = None
    current_module_title = None

    writer.add_outline_item("Capa Oficial", 0)
    if len(reader.pages) > 1:
        writer.add_outline_item("Sumário Geral", 1)

    modules_count = 0
    topics_count = 0

    for p_num, page in enumerate(reader.pages):
        txt = page.extract_text()
        if not txt or p_num < 3:
            continue

        # 1. Detectar Módulo
        m_mod = re.search(r'(Módulo\s+\d\d:\s+[^\n]+)', txt)
        if m_mod and 'C O N C U R S O' in txt:
            mod_title = m_mod.group(1).strip()
            if mod_title != current_module_title:
                current_module_title = mod_title
                current_module_outline = writer.add_outline_item(mod_title, p_num)
                modules_count += 1
                continue

        # 2. Detectar Tópico
        lines = [line.strip() for line in txt.splitlines() if line.strip()]
        if lines:
            first_line = lines[0]
            if re.match(r'^\d\d\s*-\s+[A-Za-zÀ-ÿ]', first_line) and any('Matéria:' in l for l in lines[:4]):
                topic_title = first_line
                writer.add_outline_item(topic_title, p_num, parent=current_module_outline)
                topics_count += 1

    with open(final_pdf_path, 'wb') as f:
        writer.write(f)

    print(f"Sucesso! {modules_count} Módulos e {topics_count} Tópicos indexados no menu lateral de {os.path.basename(final_pdf_path)} (Total: {len(reader.pages)} págs).")
    return True

def compile_theme(theme_key, html_path, pdf_path):
    print(f"\n--- Processando Edição {theme_key.upper()} ---")
    html_content, topics, questions = generate_ti_html(theme_key)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"HTML gerado: {html_path} ({len(html_content)/1024:.1f} KB)")

    raw_pdf_path = pdf_path.replace(".pdf", "_raw.pdf")
    print(f"Renderizando PDF com Microsoft Edge Headless...")
    ok = print_pdf_raw(os.path.abspath(html_path), os.path.abspath(raw_pdf_path))
    if not ok:
        print(f"Erro ao renderizar PDF {theme_key}!")
        return False

    inject_bookmarks_and_finalize(raw_pdf_path, pdf_path)
    if os.path.exists(raw_pdf_path):
        os.remove(raw_pdf_path)

    pdf_size_mb = os.path.getsize(pdf_path) / (1024*1024)
    print(f"PDF {theme_key.upper()} Finalizado com Sucesso: {pdf_path} ({pdf_size_mb:.2f} MB)")
    return True

def main():
    print("=" * 70)
    print("COMPILADOR PROFISSIONAL TCE-GO: TECNOLOGIA DA INFORMAÇÃO (CARGO B02)")
    print("=" * 70)
    t0 = time.time()

    # 1. Compilar Edição Sépia (Papel Suave Amarelado)
    pdf_sepia = os.path.join(BASE_DIR, "Guia_Estudos_TCE_GO_TI_Sepia.pdf")
    html_sepia = os.path.join(BASE_DIR, "Guia_Estudos_TCE_GO_TI_Sepia.html")
    compile_theme('sepia', html_sepia, pdf_sepia)
    
    # Atualizar PDF padrão
    default_pdf = os.path.join(BASE_DIR, "Guia_Estudos_TCE_GO.pdf")
    shutil.copyfile(pdf_sepia, default_pdf)

    # 2. Compilar Edição Drácula (Modo Escuro VS Code Oficial)
    pdf_dracula = os.path.join(BASE_DIR, "Guia_Estudos_TCE_GO_TI_Dracula.pdf")
    html_dracula = os.path.join(BASE_DIR, "Guia_Estudos_TCE_GO_TI_Dracula.html")
    compile_theme('dracula', html_dracula, pdf_dracula)

    print("\n" + "=" * 70)
    print(f"COMPILAÇÃO DE TI TOTALMENTE CONCLUÍDA EM {time.time() - t0:.2f} SEGUNDOS!")
    print("=" * 70)

if __name__ == "__main__":
    main()
