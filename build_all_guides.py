# -*- coding: utf-8 -*-
"""
Compilador Automatizado Profissional de Guias de Estudo TCE-GO (ABNT / FCC)
Gera os 3 PDFs finais indexados:
  1. conhecimentos_gerais.pdf     (Módulos 01 a 03)
  2. tecnico_administrativo.pdf   (Cargo A01: Módulos 15 a 25)
  3. tecnico_ti.pdf               (Cargo B02: Módulos 04 a 14)
"""

import os
import re
import sys
import time
import shutil
import subprocess
import uuid
import markdown
import pypdf

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONTES_DIR = os.path.join(BASE_DIR, "fontes_de_estudo")
GERAIS_DIR = os.path.join(FONTES_DIR, "conhecimentos_gerais")
TI_DIR = os.path.join(FONTES_DIR, "conhecimentos_especificos_b02_ti")
ADM_DIR = os.path.join(FONTES_DIR, "conhecimentos_especificos_a01_tecnico_administrativo")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

NODE_RENDER_SCRIPT = os.path.join(BASE_DIR, "render_html_to_pdf.js")

# Catálogo completo e rigoroso de todos os 25 módulos
ALL_MODULES = [
    # PARTE I: CONHECIMENTOS GERAIS (01 a 03)
    {
        "id": "mod_01",
        "num": "01",
        "part": "CONHECIMENTOS GERAIS COMUNS",
        "title": "Módulo 01: Língua Portuguesa",
        "dir": os.path.join(GERAIS_DIR, "01_lingua_portuguesa"),
        "desc": "Gramática, Interpretação de Textos, Redação Oficial e Sintaxe da FCC",
        "badge": "COMUM A TODOS OS CARGOS"
    },
    {
        "id": "mod_02",
        "num": "02",
        "part": "CONHECIMENTOS GERAIS COMUNS",
        "title": "Módulo 02: Matemática e Raciocínio Lógico",
        "dir": os.path.join(GERAIS_DIR, "02_matematica_e_raciocinio_logico"),
        "desc": "Aritmética, Proporções, Conjuntos, Lógica Proposicional e Argumentação",
        "badge": "COMUM A TODOS OS CARGOS"
    },
    {
        "id": "mod_03",
        "num": "03",
        "part": "CONHECIMENTOS GERAIS COMUNS",
        "title": "Módulo 03: Legislação Institucional (TCE-GO & Goiás)",
        "dir": os.path.join(GERAIS_DIR, "03_legislacao_institucional"),
        "desc": "CF/88, Constituição Estadual de Goiás, Lei Orgânica e Regimento do TCE-GO",
        "badge": "COMUM A TODOS OS CARGOS"
    },
    # PARTE II: CONHECIMENTOS ESPECÍFICOS - CARGO B02: TI (04 a 14)
    {
        "id": "mod_04",
        "num": "04",
        "part": "CONHECIMENTOS ESPECÍFICOS – TECNOLOGIA DA INFORMAÇÃO",
        "title": "Módulo 04: Engenharia de Software",
        "dir": os.path.join(TI_DIR, "04_engenharia_de_software"),
        "desc": "Ciclos Preditivo e Ágil, Requisitos, Modelagem UML/BPMN, Arquitetura e Padrões GoF",
        "badge": "CARGO B02: TI"
    },
    {
        "id": "mod_05",
        "num": "05",
        "part": "CONHECIMENTOS ESPECÍFICOS – TECNOLOGIA DA INFORMAÇÃO",
        "title": "Módulo 05: Desenvolvimento de Sistemas",
        "dir": os.path.join(TI_DIR, "05_desenvolvimento_de_sistemas"),
        "desc": "Algoritmos, POO, Java, JS/Node, Python, Frontend Web, APIs RESTful/GraphQL e Git",
        "badge": "CARGO B02: TI"
    },
    {
        "id": "mod_06",
        "num": "06",
        "part": "CONHECIMENTOS ESPECÍFICOS – TECNOLOGIA DA INFORMAÇÃO",
        "title": "Módulo 06: Engenharia de Software Assistida por IA e Sistemas Agentivos",
        "dir": os.path.join(TI_DIR, "06_engenharia_software_ia_e_sistemas_agentivos"),
        "desc": "LLMs para Código, Agentes CLI/IDE, MCP, RAG de Código e Self-Healing",
        "badge": "CARGO B02: TI"
    },
    {
        "id": "mod_07",
        "num": "07",
        "part": "CONHECIMENTOS ESPECÍFICOS – TECNOLOGIA DA INFORMAÇÃO",
        "title": "Módulo 07: DevOps e Plataforma de Entrega",
        "dir": os.path.join(TI_DIR, "07_devops_e_plataforma_de_entrega"),
        "desc": "CI/CD, Git Flow/Trunk, Docker, Kubernetes, IaC Terraform/Ansible e Observabilidade",
        "badge": "CARGO B02: TI"
    },
    {
        "id": "mod_08",
        "num": "08",
        "part": "CONHECIMENTOS ESPECÍFICOS – TECNOLOGIA DA INFORMAÇÃO",
        "title": "Módulo 08: Banco de Dados Relacional e NoSQL",
        "dir": os.path.join(TI_DIR, "08_banco_de_dados"),
        "desc": "Modelagem MER, Álgebra Relacional, SQL Avançado, ACID, NoSQL, Vetoriais e Tuning",
        "badge": "CARGO B02: TI"
    },
    {
        "id": "mod_09",
        "num": "09",
        "part": "CONHECIMENTOS ESPECÍFICOS – TECNOLOGIA DA INFORMAÇÃO",
        "title": "Módulo 09: Inteligência Artificial e Ciência de Dados",
        "dir": os.path.join(TI_DIR, "09_inteligencia_artificial_e_ciencia_de_dados"),
        "desc": "Machine Learning, Redes Neurais/LLMs, NLP, RAG, IPA, Análise de Dados e Big Data",
        "badge": "CARGO B02: TI"
    },
    {
        "id": "mod_10",
        "num": "10",
        "part": "CONHECIMENTOS ESPECÍFICOS – TECNOLOGIA DA INFORMAÇÃO",
        "title": "Módulo 10: Segurança da Informação e Cibersegurança",
        "dir": os.path.join(TI_DIR, "10_seguranca_da_informacao"),
        "desc": "Princípios CIDAN, ISO 27001/27002, Criptografia, Zero Trust, OWASP e DevSecOps",
        "badge": "CARGO B02: TI"
    },
    {
        "id": "mod_11",
        "num": "11",
        "part": "CONHECIMENTOS ESPECÍFICOS – TECNOLOGIA DA INFORMAÇÃO",
        "title": "Módulo 11: Sistemas Operacionais, Redes e Computação em Nuvem",
        "dir": os.path.join(TI_DIR, "11_sistemas_operacionais_redes_e_nuvem"),
        "desc": "Linux/Windows, TCP/IP, DNS/DHCP, Protocolos Web, Wi-Fi e Cloud IaaS/PaaS/SaaS",
        "badge": "CARGO B02: TI"
    },
    {
        "id": "mod_12",
        "num": "12",
        "part": "CONHECIMENTOS ESPECÍFICOS – TECNOLOGIA DA INFORMAÇÃO",
        "title": "Módulo 12: Governança e Gestão de TI",
        "dir": os.path.join(TI_DIR, "12_governanca_de_ti"),
        "desc": "ISO 38500, COBIT 2019, ITIL v4, PMBOK 8ª Ed, Contratações TIC Lei 14.133 e ENGD",
        "badge": "CARGO B02: TI"
    },
    {
        "id": "mod_13",
        "num": "13",
        "part": "CONHECIMENTOS ESPECÍFICOS – TECNOLOGIA DA INFORMAÇÃO",
        "title": "Módulo 13: Legislação Aplicada à Tecnologia da Informação",
        "dir": os.path.join(TI_DIR, "13_legislacao_aplicada_a_ti"),
        "desc": "LGPD Técnica, Marco Civil, Assinaturas Digitais, LC GO 205/2025 e Normativos TCE-GO",
        "badge": "CARGO B02: TI"
    },
    {
        "id": "mod_14",
        "num": "14",
        "part": "CONHECIMENTOS ESPECÍFICOS – TECNOLOGIA DA INFORMAÇÃO",
        "title": "Módulo 14: Língua Inglesa (Leitura Técnica)",
        "dir": os.path.join(TI_DIR, "14_lingua_inglesa_leitura_tecnica"),
        "desc": "Skimming, Scanning, Falsos Cognatos, Vocabulário Técnico de TI e Artigos",
        "badge": "CARGO B02: TI"
    },
    # PARTE III: CONHECIMENTOS ESPECÍFICOS - CARGO A01: ADMINISTRATIVO (15 a 25)
    {
        "id": "mod_15",
        "num": "15",
        "part": "CONHECIMENTOS ESPECÍFICOS – TÉCNICO ADMINISTRATIVO",
        "title": "Módulo 15: Noções de Direito Administrativo",
        "dir": os.path.join(ADM_DIR, "15_nocoes_de_direito_administrativo"),
        "desc": "Regime Jurídico, Organização, Atos, Poderes, Bens, Serviços, Responsabilidade e Improbidade",
        "badge": "CARGO A01: ADMINISTRATIVO"
    },
    {
        "id": "mod_16",
        "num": "16",
        "part": "CONHECIMENTOS ESPECÍFICOS – TÉCNICO ADMINISTRATIVO",
        "title": "Módulo 16: Licitações e Contratos Administrativos",
        "dir": os.path.join(ADM_DIR, "16_licitacoes_e_contratos_administrativos"),
        "desc": "Nova Lei de Licitações (Lei nº 14.133/2021), Planejamento, Contratação Direta e Sanções",
        "badge": "CARGO A01: ADMINISTRATIVO"
    },
    {
        "id": "mod_17",
        "num": "17",
        "part": "CONHECIMENTOS ESPECÍFICOS – TÉCNICO ADMINISTRATIVO",
        "title": "Módulo 17: Noções de Direito Constitucional",
        "dir": os.path.join(ADM_DIR, "17_nocoes_de_direito_constitucional"),
        "desc": "Princípios, Direitos Fundamentais, Organização do Estado, Poder Legislativo, Executivo e Judiciário",
        "badge": "CARGO A01: ADMINISTRATIVO"
    },
    {
        "id": "mod_18",
        "num": "18",
        "part": "CONHECIMENTOS ESPECÍFICOS – TÉCNICO ADMINISTRATIVO",
        "title": "Módulo 18: Noções de Controle Externo",
        "dir": os.path.join(ADM_DIR, "18_nocoes_de_controle_externo"),
        "desc": "Sistema Constitucional de Controle, Jurisdição dos TCs, Auditorias Governamentais (NBASP) e TCE",
        "badge": "CARGO A01: ADMINISTRATIVO"
    },
    {
        "id": "mod_19",
        "num": "19",
        "part": "CONHECIMENTOS ESPECÍFICOS – TÉCNICO ADMINISTRATIVO",
        "title": "Módulo 19: Noções de Administração Financeira e Orçamentária (AFO)",
        "dir": os.path.join(ADM_DIR, "19_nocoes_de_administracao_financeira_e_orcamentaria"),
        "desc": "PPA, LDO, LOA, Receita, Despesa, Créditos Adicionais, Dívida Pública e LRF (LC 101/2000)",
        "badge": "CARGO A01: ADMINISTRATIVO"
    },
    {
        "id": "mod_20",
        "num": "20",
        "part": "CONHECIMENTOS ESPECÍFICOS – TÉCNICO ADMINISTRATIVO",
        "title": "Módulo 20: Contabilidade Aplicada ao Setor Público (CASP)",
        "dir": os.path.join(ADM_DIR, "20_contabilidade_aplicada_ao_setor_publico"),
        "desc": "NBC TSP Estrutura Conceitual, MCASP 11ª Edição (PCO e PCP), PCASP e DCASP",
        "badge": "CARGO A01: ADMINISTRATIVO"
    },
    {
        "id": "mod_21",
        "num": "21",
        "part": "CONHECIMENTOS ESPECÍFICOS – TÉCNICO ADMINISTRATIVO",
        "title": "Módulo 21: Noções de Administração Pública",
        "dir": os.path.join(ADM_DIR, "21_nocoes_de_administracao_publica"),
        "desc": "Organizações Formais, Modelos de Gestão Pública, Governança, LAI, Decreto 9.094/17 e Processos",
        "badge": "CARGO A01: ADMINISTRATIVO"
    },
    {
        "id": "mod_22",
        "num": "22",
        "part": "CONHECIMENTOS ESPECÍFICOS – TÉCNICO ADMINISTRATIVO",
        "title": "Módulo 22: Administração Geral",
        "dir": os.path.join(ADM_DIR, "22_administracao_geral"),
        "desc": "Teorias da Administração, ORT, Eficiência vs. Eficácia, Ambientes, Processo Decisório e Projetos",
        "badge": "CARGO A01: ADMINISTRATIVO"
    },
    {
        "id": "mod_23",
        "num": "23",
        "part": "CONHECIMENTOS ESPECÍFICOS – TÉCNICO ADMINISTRATIVO",
        "title": "Módulo 23: Administração Estratégica",
        "dir": os.path.join(ADM_DIR, "23_administracao_estrategica"),
        "desc": "Missão, Visão, Valores, Escolas de Mintzberg, SWOT, Cinco Forças de Porter, RBV e Cadeia de Valor",
        "badge": "CARGO A01: ADMINISTRATIVO"
    },
    {
        "id": "mod_24",
        "num": "24",
        "part": "CONHECIMENTOS ESPECÍFICOS – TÉCNICO ADMINISTRATIVO",
        "title": "Módulo 24: Comportamento Organizacional",
        "dir": os.path.join(ADM_DIR, "24_comportamento_organizacional"),
        "desc": "Personalidade (Big Five), Atitudes, Motivação, Equipes, Liderança, Conflitos, Negociação e Cultura",
        "badge": "CARGO A01: ADMINISTRATIVO"
    },
    {
        "id": "mod_25",
        "num": "25",
        "part": "CONHECIMENTOS ESPECÍFICOS – TÉCNICO ADMINISTRATIVO",
        "title": "Módulo 25: Gestão de Pessoas e Estatuto Estadual",
        "dir": os.path.join(ADM_DIR, "25_gestao_de_pessoas"),
        "desc": "Recrutamento, Seleção, T&D, Gestão do Conhecimento, Avaliação de Desempenho e Lei Estadual nº 20.756/20",
        "badge": "CARGO A01: ADMINISTRATIVO"
    }
]

MODULES_BY_ID = {m["id"]: m for m in ALL_MODULES}

# Definição dos 3 alvos de compilação
TARGETS = {
    "conhecimentos_gerais": {
        "output_pdf": "fontes_de_estudo/conhecimentos_gerais.pdf",
        "output_html": "fontes_de_estudo/conhecimentos_gerais.html",
        "title": "GUIA DEFINITIVO DE ESTUDOS",
        "cargo": "TÉCNICO DE CONTROLE EXTERNO — CONHECIMENTOS GERAIS (COMUM A TODOS OS CARGOS)",
        "subtitle": "Módulos 01 a 03: Língua Portuguesa, Matemática/Raciocínio Lógico e Legislação Institucional",
        "module_ids": ["mod_01", "mod_02", "mod_03"],
    },
    "tecnico_administrativo": {
        "output_pdf": "fontes_de_estudo/tecnico_administrativo.pdf",
        "output_html": "fontes_de_estudo/tecnico_administrativo.html",
        "title": "GUIA DEFINITIVO DE ESTUDOS",
        "cargo": "TÉCNICO DE CONTROLE EXTERNO — ESPECIALIDADE: TÉCNICO ADMINISTRATIVO (CARGO A01)",
        "subtitle": "Conhecimentos Específicos: Módulos 15 a 25",
        "module_ids": [f"mod_{i:02d}" for i in range(15, 26)],
    },
    "tecnico_ti": {
        "output_pdf": "fontes_de_estudo/tecnico_ti.pdf",
        "output_html": "fontes_de_estudo/tecnico_ti.html",
        "title": "GUIA DEFINITIVO DE ESTUDOS",
        "cargo": "TÉCNICO DE CONTROLE EXTERNO — ESPECIALIDADE: TECNOLOGIA DA INFORMAÇÃO (CARGO B02)",
        "subtitle": "Conhecimentos Específicos: Módulos 04 a 14",
        "module_ids": [f"mod_{i:02d}" for i in range(4, 15)],
    }
}

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

def get_mandatory_css():
    return get_base_css()

def get_complementary_css():
    return ""

def get_html_template():
    return load_template_file("template.html")

# Carregamento do CSS Base a partir do arquivo compartilhado style.css
MANDATORY_CSS = get_base_css()
COMPLEMENTARY_CSS = ""

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
    # Colapsar apenas espaços repetidos estritamente dentro de uma linha (preservando início e fim de linha)
    cleaned = re.sub(r'(?<=\S)[ \t]{2,}(?=\S)', ' ', cleaned)
    return cleaned

def render_mermaid_to_svg(code):
    """Renderiza código Mermaid para SVG via Mermaid CLI (mmdc)."""
    uid = uuid.uuid4().hex[:8]
    temp_mmd = f"temp_{uid}.mmd"
    temp_svg = f"temp_{uid}.svg"
    try:
        with open(temp_mmd, "w", encoding="utf-8") as f:
            f.write(code)
        subprocess.run(
            ["mmdc", "-i", temp_mmd, "-o", temp_svg, "-b", "transparent"],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            shell=(sys.platform == "win32")
        )
        with open(temp_svg, "r", encoding="utf-8") as f:
            svg_content = f.read()
        return f'<div class="mermaid-svg-wrapper">\n{svg_content}\n</div>'
    except Exception:
        safe_code = code.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        return f'<pre class="mermaid">\n{safe_code}\n</pre>'
    finally:
        for tmp_file in (temp_mmd, temp_svg):
            if os.path.exists(tmp_file):
                try:
                    os.remove(tmp_file)
                except OSError:
                    pass

def process_markdown(raw_md):
    """Compila Markdown preservando blocos Mermaid, LaTeX matemático e envelopando questões."""
    text = remove_emojis_for_pdf(raw_md)

    # 1. Renderizar blocos Mermaid via CLI (mmdc) com fallback para <pre>
    mermaid_blocks = []
    def save_mermaid(m):
        code = m.group(1).strip()
        rendered = render_mermaid_to_svg(code)
        mermaid_blocks.append(rendered)
        return f"@@@MERMAID_BLOCK_{len(mermaid_blocks)-1}@@@"
    text = re.sub(r'```mermaid(.*?)```', save_mermaid, text, flags=re.DOTALL)

    # 2. Proteger símbolos de moeda
    text = re.sub(r'R\$(?=\s*\d)', r'R&dollar;', text)
    text = re.sub(r'US\$(?=\s*\d)', r'US&dollar;', text)

    # 3. Proteger expressões matemáticas LaTeX (Display e Inline)
    math_blocks = []
    def save_math(m):
        math_blocks.append(m.group(0))
        return f"@@@MATH_BLOCK_{len(math_blocks)-1}@@@"
    # Display math $$...$$
    text = re.sub(r'\$\$.*?\$\$', save_math, text, flags=re.DOTALL)
    # Inline math $...$
    text = re.sub(r'(?<!\\)\$(?!\s)(.+?)(?<!\s)(?<!\\)\$', save_math, text)

    # 4. Garantir que opções de alternativas (A a E) tenham quebra de linha individual ('  \n')
    text = re.sub(
        r'(?m)^(\s*(?:[A-E]\)|\([A-E]\)|\*\s+\*\*[A-E]\)\*\*|\*\s+[A-E]\)|-\s+\*\*[A-E]\)\*\*|-\s+[A-E]\)))(.*?) *$',
        r'\1\2  ',
        text
    )

    # 5. Formatar Alertas e Badges de Prova FCC
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

    # Correção do achatamento das listas dentro dos blockquotes de comentários
    text = re.sub(r'(>\s*\*\*Comentário Detalhado:\*\*\s*\n)(>\s*[-*]\s)', r'\1>\n\2', text)

    # 6. Compilar com Python Markdown
    html = markdown.markdown(text, extensions=['extra', 'sane_lists', 'toc'])

    # 7. Restaurar blocos de matemática
    for i, mb in enumerate(math_blocks):
        html = html.replace(f"@@@MATH_BLOCK_{i}@@@", mb)

    # 8. Restaurar blocos Mermaid renderizados em SVG
    for i, svg_html in enumerate(mermaid_blocks):
        html = html.replace(f"<p>@@@MERMAID_BLOCK_{i}@@@</p>", svg_html)
        html = html.replace(f"@@@MERMAID_BLOCK_{i}@@@", svg_html)

    # 9. Envelopamento das questões comentadas em .question-card (anti-quebra de página)
    pattern = r'(<h3>(?:<span[^>]*>)?Questão\s+\d+.*?)(?=(?:<h3>(?:<span[^>]*>)?Questão\s+\d+|<h2|<h1|\Z))'
    html = re.sub(pattern, r'<div class="question-card">\n\1\n</div>\n', html, flags=re.DOTALL)

    return html

def build_target_html(target_key):
    cfg = TARGETS[target_key]
    module_ids = cfg["module_ids"]
    target_modules = [MODULES_BY_ID[mid] for mid in module_ids if mid in MODULES_BY_ID]

    toc_html = []
    content_html = []
    
    total_topics = 0
    total_questions = 0

    print(f"\n[{target_key}] Mapeando e compilando {len(target_modules)} módulos...")

    for mod in target_modules:
        mod_title = mod["title"]
        mod_id = mod["id"]
        mod_dir = mod["dir"]
        mod_desc = mod.get("desc", "")
        mod_badge = mod.get("badge", "TCE-GO • FCC")

        if not os.path.exists(mod_dir):
            print(f"  [Aviso] Diretório não encontrado: {mod_dir}")
            continue

        files = sorted([f for f in os.listdir(mod_dir) if f.endswith('.md') and f != 'README.md'])

        toc_html.append('<div class="toc-module-block">')
        toc_html.append(f'<h3><a href="#{mod_id}">{mod_title}</a></h3>')
        toc_html.append('<ul>')

        # Marcador de Módulo para extração de outline em PDF
        content_html.append(f'''
        <div class="pdf-marker">[[MODULE:{mod_title}]]</div>
        <div class="module-divider" id="{mod_id}">
            <div class="module-badge">{mod_badge}</div>
            <h1 class="module-title">{mod_title}</h1>
            <p class="module-subtitle">{mod_desc}</p>
        </div>
        ''')

        for f in files:
            total_topics += 1
            topic_id = f"topic_{total_topics}"
            filepath = os.path.join(mod_dir, f)

            with open(filepath, 'r', encoding='utf-8') as fh:
                raw_md = fh.read()

            q_matches = len(re.findall(r'### Questão\s+\d+', raw_md, re.IGNORECASE))
            total_questions += q_matches

            first_line = raw_md.split('\n')[0].replace('#', '').strip()
            if not first_line:
                first_line = f.replace('.md', '').replace('_', ' ').title()

            toc_html.append(f'<li><a href="#{topic_id}"><span class="toc-num">{total_topics:02d}.</span> {first_line}</a></li>')

            html_chunk = process_markdown(raw_md)

            topic_bookmark_title = f"{total_topics:02d}. {first_line}"
            content_html.append(f'''
            <article class="topic-section" id="{topic_id}">
                <div class="pdf-marker">[[TOPIC:{topic_bookmark_title}]]</div>
                {html_chunk}
            </article>
            ''')

        toc_html.append('</ul></div>')

    toc_rendered = '\n'.join(toc_html)
    content_rendered = '\n'.join(content_html)

    # Capa Institucional e Sumário
    cover_html = f"""
    <!-- CAPA OFICIAL -->
    <div class="cover-page">
        <div>
            <div class="cover-institution">Tribunal de Contas do Estado de Goiás</div>
            <div class="cover-jurisdiction">Concurso Público • Coordenação Pedagógica</div>
            <h1 class="cover-title">{cfg["title"]}</h1>
            <div class="cover-subtitle">{cfg["cargo"]}</div>
            
            <div class="cover-badges">
                <span class="badge-pill">Banca Fundação Carlos Chagas (FCC)</span>
                <span class="badge-pill">Padrão ABNT (NBR 14724)</span>
                <span class="badge-pill">Fórmulas Vetoriais KaTeX</span>
                <span class="badge-pill">Diagramas Mermaid SVG</span>
                <span class="badge-pill">100% Teoria & Questões Comentadas</span>
            </div>
        </div>

        <div>
            <div class="cover-stats-grid">
                <div class="stat-card">
                    <div class="stat-num">{len(target_modules)}</div>
                    <div class="stat-lbl">Módulos</div>
                </div>
                <div class="stat-card">
                    <div class="stat-num">{total_topics}</div>
                    <div class="stat-lbl">Tópicos Teóricos</div>
                </div>
                <div class="stat-card">
                    <div class="stat-num">{total_questions}</div>
                    <div class="stat-lbl">Questões FCC</div>
                </div>
            </div>
        </div>

        <div class="cover-footer">
            <strong>{cfg["subtitle"]}</strong><br>
            Material didático consolidado para preparação de alto rendimento no Tribunal de Contas de Goiás.<br>
            Edição Atualizada • Todos os direitos reservados.
        </div>
    </div>
    """

    toc_container_html = f"""
    <!-- SUMÁRIO GERAL -->
    <div class="toc-container">
        <h2 class="toc-title">Sumário Executivo e Relação de Conteúdos</h2>
        <div style="column-count: 2; column-gap: 20px;">
            {toc_rendered}
        </div>
    </div>
    """

    # Montagem do HTML completo a partir do template compartilhado
    html_template = get_html_template()
    doc_title = f"{cfg['title']} — {cfg['cargo']}"
    css_content = get_base_css()

    full_html = (
        html_template
        .replace("{{TITLE}}", doc_title).replace("__TITLE__", doc_title)
        .replace("{{CSS}}", css_content).replace("__CSS__", css_content)
        .replace("{{COVER}}", cover_html).replace("__COVER__", cover_html)
        .replace("{{TOC}}", toc_container_html).replace("__TOC__", toc_container_html)
        .replace("{{CONTENT}}", content_rendered).replace("__CONTENT__", content_rendered)
    )

    return full_html, total_topics, total_questions

def inject_bookmarks_and_finalize(raw_pdf_path, final_pdf_path):
    """Indexa Módulos e Tópicos no menu lateral hierárquico do PDF."""
    print(f"Indexando bookmarks no menu lateral de {os.path.basename(final_pdf_path)}...")
    reader = pypdf.PdfReader(raw_pdf_path)
    writer = pypdf.PdfWriter()
    writer.append(reader)

    writer.add_outline_item("Capa Oficial", 0)
    if len(reader.pages) > 1:
        writer.add_outline_item("Sumário Geral", 1)

    current_module_outline = None
    seen_modules = set()
    seen_topics = set()

    modules_count = 0
    topics_count = 0

    for p_num, page in enumerate(reader.pages):
        txt = page.extract_text()
        if not txt or p_num < 2:
            continue

        # 1. Detectar Módulo via marcador ou cabeçalho
        mod_matches = re.findall(r'\[\[MODULE:(.*?)\]\]', txt)
        if not mod_matches:
            # Fallback para regex direta do texto
            mod_fallback = re.findall(r'(Módulo\s+\d\d:\s+[^\n]+)', txt)
            if mod_fallback and 'TRIBUNAL DE CONTAS' not in mod_fallback[0]:
                mod_matches = [mod_fallback[0]]

        for mod_title in mod_matches:
            mod_title = mod_title.strip()
            if mod_title not in seen_modules:
                seen_modules.add(mod_title)
                current_module_outline = writer.add_outline_item(mod_title, p_num)
                modules_count += 1

        # 2. Detectar Tópico via marcador ou cabeçalho
        top_matches = re.findall(r'\[\[TOPIC:(.*?)\]\]', txt)
        if not top_matches:
            # Fallback para regex direta do primeiro cabeçalho
            lines = [l.strip() for l in txt.splitlines() if l.strip()]
            for line in lines[:5]:
                if re.match(r'^\d\d\s*-\s+[A-Za-zÀ-ÿ]', line) and any('Matéria:' in l for l in lines[:6]):
                    top_matches = [line]
                    break

        for topic_title in top_matches:
            topic_title = topic_title.strip()
            if topic_title not in seen_topics:
                seen_topics.add(topic_title)
                writer.add_outline_item(topic_title, p_num, parent=current_module_outline)
                topics_count += 1

    with open(final_pdf_path, 'wb') as f:
        writer.write(f)

    print(f"Sucesso! {modules_count} Módulos e {topics_count} Tópicos indexados no menu lateral ({len(reader.pages)} páginas).")
    return True

def compile_target(target_key):
    cfg = TARGETS[target_key]
    html_file = os.path.join(BASE_DIR, cfg["output_html"])
    final_pdf_file = os.path.join(BASE_DIR, cfg["output_pdf"])
    raw_pdf_file = os.path.join(BASE_DIR, f"{target_key}_raw.pdf")

    t0 = time.time()
    print("=" * 70)
    print(f"INICIANDO COMPILAÇÃO DO ALVO: {target_key.upper()}")
    print(f"Arquivo Final: {cfg['output_pdf']}")
    print("=" * 70)

    # 1. Gerar HTML
    html_content, topics, questions = build_target_html(target_key)
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"HTML gravado: {html_file} ({len(html_content)/1024:.1f} KB, {topics} tópicos, {questions} questões)")

    # 2. Renderizar via Puppeteer / Edge
    print(f"Chamando renderizador Node.js (Puppeteer com Edge Headless)...")
    res = subprocess.run(["node", NODE_RENDER_SCRIPT, html_file, raw_pdf_file], capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Erro na renderização Puppeteer de {target_key}:")
        print(res.stderr)
        return False
    print(res.stdout.strip())

    if not os.path.exists(raw_pdf_file) or os.path.getsize(raw_pdf_file) == 0:
        print(f"Erro: PDF raw não foi gerado em {raw_pdf_file}")
        return False

    # 3. Injetar Bookmarks com pypdf
    inject_bookmarks_and_finalize(raw_pdf_file, final_pdf_file)

    # Limpeza do arquivo raw temporário
    if os.path.exists(raw_pdf_file):
        os.remove(raw_pdf_file)

    size_mb = os.path.getsize(final_pdf_file) / (1024 * 1024)
    print(f"ALVO {target_key.upper()} CONCLUÍDO EM {time.time() - t0:.1f}s: {final_pdf_file} ({size_mb:.2f} MB)")
    return True

def main():
    targets_to_run = sys.argv[1:] if len(sys.argv) > 1 else ["conhecimentos_gerais", "tecnico_administrativo", "tecnico_ti"]

    t_global = time.time()
    print("=" * 75)
    print("GERAÇÃO EM LOTE DOS 3 GUIAS DEFINITIVOS DE ESTUDO TCE-GO")
    print(f"Alvos selecionados: {', '.join(targets_to_run)}")
    print("=" * 75)

    for target in targets_to_run:
        if target in TARGETS:
            ok = compile_target(target)
            if not ok:
                print(f"Falha ao compilar alvo: {target}")
                sys.exit(1)
        else:
            print(f"Alvo desconhecido: {target}")

    print("\n" + "=" * 75)
    print(f"TODAS AS COMPILAÇÕES CONCLUÍDAS COM SUCESSO EM {time.time() - t_global:.1f} SEGUNDOS!")
    print("=" * 75)

if __name__ == "__main__":
    main()
