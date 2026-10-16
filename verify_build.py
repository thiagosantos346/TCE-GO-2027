# -*- coding: utf-8 -*-
"""
FASE 3: Script de Auditoria Automatizada de Qualidade DOM (verify_build.py)
Analisa:
  - fontes_de_estudo/conhecimentos_gerais.html
  - fontes_de_estudo/tecnico_ti.html
  - fontes_de_estudo/tecnico_administrativo.html

Executa os 7 testes determinísticos de qualidade e retorna código != 0 se houver qualquer erro.
"""

import os
import re
import sys
from collections import Counter
from bs4 import BeautifulSoup

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

HTML_FILES = [
    os.path.join(BASE_DIR, "fontes_de_estudo", "conhecimentos_gerais.html"),
    os.path.join(BASE_DIR, "fontes_de_estudo", "tecnico_ti.html"),
    os.path.join(BASE_DIR, "fontes_de_estudo", "tecnico_administrativo.html"),
]


def audit_html_file(filepath):
    filename = os.path.basename(filepath)
    print("\n" + "=" * 76)
    print(f" AUDITANDO ARQUIVO: {filename}")
    print("=" * 76)

    if not os.path.exists(filepath):
        print(f"  [ERRO FATAL] Arquivo não encontrado: {filepath}")
        return 1

    with open(filepath, "r", encoding="utf-8") as f:
        raw_html = f.read()

    soup = BeautifulSoup(raw_html, "html.parser")
    errors = []

    # Mapear todos os IDs do documento e verificar unicidade
    all_ids = [tag["id"] for tag in soup.find_all(id=True)]
    id_counts = Counter(all_ids)
    id_set = set(all_ids)

    # -------------------------------------------------------------------------
    # TESTE 1: Links do Sumário (100% apontam para ID existente e único)
    # -------------------------------------------------------------------------
    toc_links = soup.select(".toc-container a[href^='#'], ul.sumario-list a[href^='#']")
    t1_errors = []
    for a in toc_links:
        target_id = a["href"][1:]
        if target_id not in id_set:
            t1_errors.append(f"Link '{a.get_text().strip()[:40]}' aponta para ID inexistente: #{target_id}")
        elif id_counts[target_id] > 1:
            t1_errors.append(f"Link '{a.get_text().strip()[:40]}' aponta para ID duplicado ({id_counts[target_id]}x): #{target_id}")

    if not toc_links:
        t1_errors.append("Nenhum link de sumário encontrado no documento.")

    if t1_errors:
        errors.extend(t1_errors)
        print(f"  [FALHOU] Teste 1 (Links do Sumário): {len(t1_errors)} erro(s)")
        for e in t1_errors[:5]:
            print(f"           - {e}")
    else:
        print(f"  [PASSOU] Teste 1 (Links do Sumário): {len(toc_links)} links validados (100% existentes e únicos)")

    # -------------------------------------------------------------------------
    # TESTE 2: Links de Retorno (Todos os h2 e h3 numerados apontam de volta ao sumário)
    # -------------------------------------------------------------------------
    t2_errors = []
    numbered_headings_count = 0
    num_re = re.compile(r'^(?:[^\w\d\s]+\s*)*\d+(?:\.\d+)*\.?\s+')

    for h in soup.select("main.content-body h2, main.content-body h3"):
        htext = h.get_text().strip()
        if not num_re.match(htext):
            continue
        numbered_headings_count += 1
        back_a = h.find("a", class_="heading-backlink")
        if not back_a or not back_a.get("href", "").startswith("#"):
            t2_errors.append(f"Cabeçalho sem link de retorno (.heading-backlink): {htext[:50]}")
            continue
        back_target = back_a["href"][1:]
        if back_target not in id_set:
            t2_errors.append(f"Link de retorno de '{htext[:40]}' aponta para ID inexistente no sumário: #{back_target}")

    if numbered_headings_count == 0:
        t2_errors.append("Nenhum título h2/h3 numerado encontrado.")

    if t2_errors:
        errors.extend(t2_errors)
        print(f"  [FALHOU] Teste 2 (Links de Retorno): {len(t2_errors)} erro(s)")
        for e in t2_errors[:5]:
            print(f"           - {e}")
    else:
        print(f"  [PASSOU] Teste 2 (Links de Retorno): {numbered_headings_count} títulos h2/h3 numerados com retorno válido ao sumário")

    # -------------------------------------------------------------------------
    # TESTE 3: Links Externos (100% dos links http/https possuem target="_blank")
    # -------------------------------------------------------------------------
    ext_links = [
        a for a in soup.find_all("a", href=True)
        if a["href"].strip().startswith(("http://", "https://"))
    ]
    t3_errors = []
    for a in ext_links:
        if a.get("target") != "_blank":
            t3_errors.append(f"Link externo sem target='_blank': {a['href']}")

    if t3_errors:
        errors.extend(t3_errors)
        print(f"  [FALHOU] Teste 3 (Links Externos): {len(t3_errors)} erro(s)")
        for e in t3_errors[:5]:
            print(f"           - {e}")
    else:
        print(f"  [PASSOU] Teste 3 (Links Externos): {len(ext_links)} links http/https com target='_blank'")

    # -------------------------------------------------------------------------
    # TESTE 4: Listas e Sub-listas (Sem marcadores crus em <p>/<blockquote> e sub-listas no sumário)
    # -------------------------------------------------------------------------
    t4_errors = []
    raw_list_re = re.compile(
        r'(?:\s+[-*]\s+\*\*[A-E]\)\*\*|\n\s*[-*+]\s+\*\*|\n\s*\d+\.\s+\*\*|\n\s*(?:I|II|III|IV|V)\.\s+)'
    )
    for p in soup.select("main.content-body p"):
        txt = p.get_text()
        m = raw_list_re.search(txt)
        if m:
            t4_errors.append(f"<p> contém marcador de lista cru ({repr(m.group(0))}): {repr(txt[:90])}")

    # Verificar se sumários possuem sub-listas <ul> aninhadas para os itens 1.1, 1.2, etc.
    sumario_lists = soup.select("ul.sumario-list")
    nested_sublists_count = 0
    for ul in sumario_lists:
        sub_uls = ul.find_all("ul")
        nested_sublists_count += len(sub_uls)
        # Verificar se algum item 1.1 ficou solto no nível raiz do ul.sumario-list
        for top_li in ul.find_all("li", recursive=False):
            a_first = top_li.find("a", recursive=False)
            if a_first and re.match(r'^\s*\d+\.\d+\b', a_first.get_text()):
                t4_errors.append(f"Sub-item '{a_first.get_text().strip()[:40]}' não está em sub-lista <ul> aninhada no sumário")

    if nested_sublists_count == 0:
        t4_errors.append("Nenhuma sub-lista <ul> aninhada encontrada nos sumários.")

    if t4_errors:
        errors.extend(t4_errors)
        print(f"  [FALHOU] Teste 4 (Listas e Sub-listas): {len(t4_errors)} erro(s)")
        for e in t4_errors[:5]:
            print(f"           - {e}")
    else:
        print(f"  [PASSOU] Teste 4 (Listas e Sub-listas): 0 marcadores crus e {nested_sublists_count} sub-listas <ul> aninhadas nos sumários")

    # -------------------------------------------------------------------------
    # TESTE 5: Alternativas e Question Cards (90+ questões em .question-card e ul.options-list)
    # -------------------------------------------------------------------------
    t5_errors = []
    q_headings = [
        h for h in soup.select("main.content-body h3")
        if re.match(r'^Questão\s+\d+', h.get_text().strip(), flags=re.I)
    ]
    q_cards = soup.select("div.question-card")
    opt_lists = soup.select("div.question-card ul.options-list")

    if len(q_cards) < 80:
        t5_errors.append(f"Quantidade insuficiente de .question-card: {len(q_cards)} (esperado >= 80)")
    if len(q_headings) != len(q_cards):
        t5_errors.append(f"Divergência entre títulos de questões ({len(q_headings)}) e .question-card ({len(q_cards)})")
    for qc in q_cards:
        if not qc.find("ul", class_="options-list"):
            h_txt = qc.find("h3").get_text().strip() if qc.find("h3") else "Questão desconhecida"
            t5_errors.append(f"Questão sem ul.options-list dentro de .question-card: {h_txt}")

    if t5_errors:
        errors.extend(t5_errors)
        print(f"  [FALHOU] Teste 5 (Alternativas e Question Cards): {len(t5_errors)} erro(s)")
        for e in t5_errors[:5]:
            print(f"           - {e}")
    else:
        print(f"  [PASSOU] Teste 5 (Alternativas e Question Cards): {len(q_cards)} question-cards com {len(opt_lists)} listas .options-list")

    # -------------------------------------------------------------------------
    # TESTE 6: KaTeX e HTML Escapado (Sem \centernot, R&dollar; em fórmulas, \<ins\> ou &lt;ins&gt;)
    # -------------------------------------------------------------------------
    t6_errors = []
    if r"\centernot" in raw_html:
        t6_errors.append(r"Encontrada string inválida '\centernot' no HTML.")
    if r"\<ins\>" in raw_html or r"\</ins\>" in raw_html:
        t6_errors.append(r"Encontrada tag escapada '\<ins\>' no HTML.")
    if "&lt;ins&gt;" in raw_html or "&lt;/ins&gt;" in raw_html:
        t6_errors.append("Encontrada tag escapada '&lt;ins&gt;' visível no HTML.")

    for m in re.finditer(r'\$\$.*?\$\$|(?<!\\)(?<!R)(?<!US)\$(?!\s)(.+?)(?<!\s)(?<!\\)\$', raw_html, flags=re.S):
        math_str = m.group(0)
        if "R&dollar;" in math_str:
            t6_errors.append(f"Encontrado 'R&dollar;' dentro de fórmula matemática: {math_str[:60]}")

    if t6_errors:
        errors.extend(t6_errors)
        print(f"  [FALHOU] Teste 6 (KaTeX e HTML Escapado): {len(t6_errors)} erro(s)")
        for e in t6_errors[:5]:
            print(f"           - {e}")
    else:
        print("  [PASSOU] Teste 6 (KaTeX e HTML Escapado): 0 ocorrências de \\centernot, R&dollar; em fórmulas ou <ins> escapado")

    # -------------------------------------------------------------------------
    # TESTE 7: Emojis Preservados
    # -------------------------------------------------------------------------
    t7_errors = []
    required_emojis = ["📌", "🧭", "🚨", "⭐", "💡"]
    if filename == "conhecimentos_gerais.html":
        required_emojis.extend(["♠", "♥"])

    for emj in required_emojis:
        if emj not in raw_html:
            t7_errors.append(f"Emoji obrigatório '{emj}' ausente em {filename}")

    if t7_errors:
        errors.extend(t7_errors)
        print(f"  [FALHOU] Teste 7 (Emojis Preservados): {len(t7_errors)} erro(s)")
        for e in t7_errors:
            print(f"           - {e}")
    else:
        print(f"  [PASSOU] Teste 7 (Emojis Preservados): Todos os emojis ({', '.join(required_emojis)}) presentes")

    return len(errors)


def main():
    print("#" * 76)
    print(" FASE 3: AUDITORIA AUTOMATIZADA DE QUALIDADE DOM (verify_build.py)")
    print("#" * 76)

    total_errors = 0
    for fpath in HTML_FILES:
        total_errors += audit_html_file(fpath)

    print("\n" + "#" * 76)
    if total_errors == 0:
        print(" RESULTADO FINAL: ZERO ERROS NOS 3 ARQUIVOS HTML! (100% APROVADO)")
        print("#" * 76)
        sys.exit(0)
    else:
        print(f" RESULTADO FINAL: {total_errors} ERRO(S) ENCONTRADO(S)!")
        print("#" * 76)
        sys.exit(1)


if __name__ == "__main__":
    main()

