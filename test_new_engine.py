import os
import re
import tempfile
import subprocess
import markdown
import pypdf

# 1. Math formatter with real typographical fractions
def render_math_to_clean_html(text):
    code_blocks = []
    def save_code(m):
        code_blocks.append(m.group(0))
        return f"@@@CODE_BLOCK_{len(code_blocks)-1}@@@"
    
    text = re.sub(r'```.*?```', save_code, text, flags=re.DOTALL)
    text = re.sub(r'`[^`]+`', save_code, text)

    # Substituições de símbolos matemáticos
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

    # Frações verticais
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

    # Blocos de fórmulas
    text = re.sub(r'\$\$(.*?)\$\$', r'<div class="math-display">\1</div>', text, flags=re.DOTALL)
    text = re.sub(r'(?<!\\)\$([^\$\n]+?)(?<!\\)\$', r'<span class="math-inline">\1</span>', text)

    for i, c in enumerate(code_blocks):
        text = text.replace(f"@@@CODE_BLOCK_{i}@@@", c)

    return text

# 2. Markdown processor with post-wrap for question cards
def process_markdown(raw_md):
    # Protege blocos mermaid
    def repl_mermaid(m):
        code = m.group(1).strip()
        safe_code = code.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        return f'\n\n<pre class="mermaid">\n{safe_code}\n</pre>\n\n'

    content = re.sub(r'```mermaid(.*?)```', repl_mermaid, raw_md, flags=re.DOTALL)

    # Escapar moedas
    content = re.sub(r'R\$(?=\s*\d)', r'R&dollar;', content)
    content = re.sub(r'US\$(?=\s*\d)', r'US&dollar;', content)

    # Renderizar matemática
    content = render_math_to_clean_html(content)

    # Gabaritos e Metadados
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

    # Alertas
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

    # Markdown compile PRIMEIRO (para preservar 100% da formatação!)
    html = markdown.markdown(content, extensions=['extra', 'sane_lists'])

    # Envelopar questões DEPOIS da compilação de markdown!
    pattern = r'(<h3>Questão\s+\d+.*?)(?=(?:<h3>Questão\s+\d+|<h2|<h1|\Z))'
    html = re.sub(pattern, r'<div class="question-card">\n\1\n</div>\n', html, flags=re.DOTALL)

    return html

# 3. Test HTML generator
def generate_test_page(theme='dracula'):
    is_dracula = (theme == 'dracula')
    bg_page = "#282a36" if is_dracula else "#fbf7ee"
    bg_card = "#343746" if is_dracula else "#ffffff"
    text_main = "#f8f8f2" if is_dracula else "#2b261f"
    text_heading = "#bd93f9" if is_dracula else "#1e3a5f"
    border_card = "#44475a" if is_dracula else "#e4d7c5"
    mermaid_theme = "dark" if is_dracula else "default"

    sample_md = """# 01 - Teste Geral de Matemática e Questão

> **Matéria:** Matemática e Raciocínio Lógico  
> **Cargo:** A01 / B02  
> **Arquivo:** `teste.md`  

---

## 📖 Resumo Teórico & Fórmulas

A taxa de juros composta equivalente é calculada por:
$$ (1 + i_a) = (1 + i_m)^{12} $$

E a taxa conjunta de trabalho com frações reais:
$$ v_{\\text{juntos}} = \\frac{1}{6} + \\frac{1}{4} = \\frac{2 + 3}{12} = \\frac{5}{12}\\text{ do serviço por hora} $$

E conjuntos numéricos:
$x \\in \\mathbb{Q} \\implies x = \\frac{a}{b}$, com $b \\neq 0$.

```mermaid
flowchart LR
    A["Início do Fluxo"] --> B["Cálculo da Taxa"]
    B --> C["Resultado Aprovado"]
```

---

## 🎯 Bateria de Questões

### Questão 01 - FCC - SEFAZ-GO
Um auditor fiscal analisa o seguinte período hipotético sobre o rendimento de um título:
A) R$ 10.000,00  
B) R$ 12.500,00  
C) R$ 15.000,00  

> **Gabarito: B**  
> **Comentário Analítico:** O cálculo exato utiliza a fórmula: $M = C \\times (1 + i)^t = \\text{R\\$} 12.500,00$.
"""

    rendered_body = process_markdown(sample_md)

    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<script src="assets/mermaid.min.js"></script>
<style>
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
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
        font-size: 10pt;
        line-height: 1.55;
    }}
    .page-wrapper {{
        padding: 16mm 14mm;
        background-color: {bg_page};
        min-height: 100vh;
    }}
    h1 {{
        color: {text_heading};
        font-size: 16pt;
        border-bottom: 2px solid #8be9fd;
        padding-bottom: 6px;
    }}
    h2 {{
        color: {text_heading};
        font-size: 12pt;
        border-left: 4px solid #8be9fd;
        padding-left: 8px;
    }}
    h3 {{
        color: {text_heading};
        font-size: 11pt;
    }}
    .topic-meta-box {{
        background: {bg_card};
        border: 1px solid {border_card};
        border-radius: 6px;
        padding: 8px 12px;
        font-size: 8.5pt;
        margin-bottom: 15px;
    }}
    .question-card {{
        background: {bg_card};
        border: 1px solid {border_card};
        border-radius: 8px;
        padding: 14px 18px;
        margin: 18px 0;
        break-inside: avoid !important;
        page-break-inside: avoid !important;
    }}
    .gabarito-badge {{
        display: inline-block;
        background: #50fa7b;
        color: #282a36;
        font-weight: 800;
        font-size: 8.5pt;
        padding: 3px 8px;
        border-radius: 4px;
        margin-bottom: 6px;
    }}
    blockquote {{
        background: {bg_card};
        border-left: 4px solid #50fa7b;
        padding: 10px 14px;
        margin: 12px 0;
        border-radius: 0 6px 6px 0;
    }}
    .mermaid {{
        background: {bg_card};
        border: 1px solid {border_card};
        border-radius: 6px;
        padding: 12px;
        margin: 14px 0;
        text-align: center;
        break-inside: avoid !important;
    }}
    .mermaid svg {{
        max-width: 100% !important;
        height: auto !important;
    }}
    .math-display {{
        background: {bg_card};
        border-left: 3px solid #8be9fd;
        padding: 10px 16px;
        margin: 12px 0;
        font-family: 'Cambria Math', Georgia, serif;
        font-size: 11pt;
        text-align: center;
        border-radius: 4px;
    }}
    .math-inline {{
        font-family: 'Cambria Math', Georgia, serif;
        font-size: 10pt;
        color: #8be9fd;
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
</style>
</head>
<body>
    <div class="page-wrapper">
        {rendered_body}
    </div>

    <script>
        document.addEventListener("DOMContentLoaded", async function() {{
            mermaid.initialize({{
                startOnLoad: false,
                theme: '{mermaid_theme}',
                securityLevel: 'loose',
                flowchart: {{ htmlLabels: false, useMaxWidth: true }}
            }});
            await mermaid.run();
        }});
    </script>
</body>
</html>"""
    return html

# Test Dracula output
html_dracula = generate_test_page('dracula')
open('test_engine_dracula.html', 'w', encoding='utf-8').write(html_dracula)

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
pdf_path = os.path.abspath("test_engine_dracula.pdf")
tmp_profile = os.path.join(tempfile.gettempdir(), "edge_tmp_profile_engine")

cmd = [
    edge_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    f"--user-data-dir={tmp_profile}",
    "--virtual-time-budget=6000",
    f"--print-to-pdf={pdf_path}",
    os.path.abspath("test_engine_dracula.html")
]

res = subprocess.run(cmd, capture_output=True, text=True)
print("Exit code:", res.returncode)
print("PDF created:", os.path.exists(pdf_path))

# Inject outline bookmark test
reader = pypdf.PdfReader(pdf_path)
writer = pypdf.PdfWriter()
writer.append(reader)
m1 = writer.add_outline_item("Módulo de Teste", 0)
writer.add_outline_item("01. Teste Geral de Matemática", 0, parent=m1)
with open(pdf_path, 'wb') as f:
    writer.write(f)
print("Bookmarks successfully injected into PDF!")

