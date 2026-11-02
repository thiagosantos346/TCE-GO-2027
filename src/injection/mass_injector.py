#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
src/injection/mass_injector.py

Motor de Injeção Definitiva de Questões Reais (V2).
1. Fase 1: Corrige em memória (e persiste) quaisquer rotas "fontes_de_estudo/" para "docs/" em data/banco_questoes_v2.json.
2. Fase 2: Para cada um dos 119 arquivos .md em docs/, localiza todos os blocos ### Teste NNN simulados,
   seleciona a questão real oficial (MULTIPLA_ESCOLHA_5) semanticamente mais aderente à seção do arquivo,
   injeta enunciado e alternativas 100% originais no formato **(Banca – Órgão – Cargo – Ano)**,
   e gera comentários analíticos detalhados (A, B, C, D, E) estritamente fundamentados na teoria do arquivo Markdown.
3. Marca cada questão utilizada no JSON como "status_integracao": "injetada".
"""

import json
import math
import os
import re
import sys
import unicodedata
from collections import Counter, defaultdict

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DB_FILE = os.path.join(BASE_DIR, "data", "banco_questoes_v2.json")
DOCS_DIR = os.path.join(BASE_DIR, "docs")

STOPWORDS_PT = {
    "a", "ao", "aos", "aquela", "aquelas", "aquele", "aqueles", "aquilo", "as", "ate",
    "com", "como", "da", "das", "de", "dela", "delas", "dele", "deles", "depois",
    "do", "dos", "e", "ela", "elas", "ele", "eles", "em", "entre", "era", "eram",
    "essa", "essas", "esse", "esses", "esta", "estas", "este", "estes", "eu", "foi",
    "for", "foram", "ha", "isso", "isto", "ja", "la", "lhe", "lhes", "lo", "mas",
    "me", "mesmo", "meu", "meus", "minha", "minhas", "muito", "na", "nas", "nao",
    "nem", "no", "nos", "nossa", "nossas", "nosso", "nossos", "num", "numa", "o",
    "os", "ou", "para", "pela", "pelas", "pelo", "pelos", "por", "qual", "quando",
    "que", "quem", "sao", "se", "seja", "sejam", "sem", "sera", "serao", "seu",
    "seus", "so", "sua", "suas", "tambem", "te", "tem", "tendo", "tenha", "ter",
    "teu", "teus", "ti", "tinha", "tinham", "todo", "todos", "tu", "tua", "tuas",
    "tudo", "um", "uma", "umas", "uns", "voce", "voces", "vos", "sobre", "acerca",
    "assinale", "alternativa", "correta", "incorreta", "opcao", "item", "itens",
    "julgue", "seguinte", "seguintes", "seguir", "abaixo", "acima", "conforme",
    "segundo", "acordo", "respectivamente", "corretamente", "apenas", "somente",
    "questao", "prova", "concurso", "tribunal", "cargo", "analista", "auditor",
    "tecnico", "judiciario", "controle", "externo", "estado", "federal", "publico",
    "publica", "ano", "anos", "dia", "dias", "mes", "meses", "vez", "vezes", "cada",
}

FAMILY_FALLBACKS = {
    "01_lingua_portuguesa": ["01_lingua_portuguesa"],
    "02_matematica_e_raciocinio_logico": ["02_matematica_e_raciocinio_logico"],
    "03_legislacao_institucional": [
        "03_legislacao_institucional",
        "18_nocoes_de_controle_externo",
        "15_nocoes_de_direito_administrativo",
    ],
    "04_engenharia_de_software": [
        "04_engenharia_de_software",
        "05_desenvolvimento_de_sistemas",
        "07_devops_e_plataforma_de_entrega",
    ],
    "05_desenvolvimento_de_sistemas": [
        "05_desenvolvimento_de_sistemas",
        "04_engenharia_de_software",
        "07_devops_e_plataforma_de_entrega",
    ],
    "06_engenharia_software_ia_e_sistemas_agentivos": [
        "06_engenharia_software_ia_e_sistemas_agentivos",
        "09_inteligencia_artificial_e_ciencia_de_dados",
        "04_engenharia_de_software",
        "05_desenvolvimento_de_sistemas",
    ],
    "07_devops_e_plataforma_de_entrega": [
        "07_devops_e_plataforma_de_entrega",
        "05_desenvolvimento_de_sistemas",
        "04_engenharia_de_software",
        "11_sistemas_operacionais_redes_e_nuvem",
    ],
    "08_banco_de_dados": [
        "08_banco_de_dados",
        "09_inteligencia_artificial_e_ciencia_de_dados",
    ],
    "09_inteligencia_artificial_e_ciencia_de_dados": [
        "09_inteligencia_artificial_e_ciencia_de_dados",
        "06_engenharia_software_ia_e_sistemas_agentivos",
        "08_banco_de_dados",
    ],
    "10_seguranca_da_informacao": [
        "10_seguranca_da_informacao",
        "11_sistemas_operacionais_redes_e_nuvem",
        "13_legislacao_aplicada_a_ti",
    ],
    "11_sistemas_operacionais_redes_e_nuvem": [
        "11_sistemas_operacionais_redes_e_nuvem",
        "10_seguranca_da_informacao",
        "07_devops_e_plataforma_de_entrega",
    ],
    "12_governanca_de_ti": [
        "12_governanca_de_ti",
        "13_legislacao_aplicada_a_ti",
        "04_engenharia_de_software",
    ],
    "13_legislacao_aplicada_a_ti": [
        "13_legislacao_aplicada_a_ti",
        "12_governanca_de_ti",
        "10_seguranca_da_informacao",
        "16_licitacoes_e_contratos_administrativos",
    ],
    "14_lingua_inglesa_leitura_tecnica": [
        "14_lingua_inglesa_leitura_tecnica",
        "05_desenvolvimento_de_sistemas",
    ],
    "15_nocoes_de_direito_administrativo": [
        "15_nocoes_de_direito_administrativo",
        "16_licitacoes_e_contratos_administrativos",
        "17_nocoes_de_direito_constitucional",
    ],
    "16_licitacoes_e_contratos_administrativos": [
        "16_licitacoes_e_contratos_administrativos",
        "15_nocoes_de_direito_administrativo",
        "12_governanca_de_ti",
    ],
    "17_nocoes_de_direito_constitucional": [
        "17_nocoes_de_direito_constitucional",
        "18_nocoes_de_controle_externo",
        "03_legislacao_institucional",
    ],
    "18_nocoes_de_controle_externo": [
        "18_nocoes_de_controle_externo",
        "03_legislacao_institucional",
        "17_nocoes_de_direito_constitucional",
    ],
    "19_nocoes_de_administracao_financeira_e_orcamentaria": [
        "19_nocoes_de_administracao_financeira_e_orcamentaria",
        "20_contabilidade_aplicada_ao_setor_publico",
    ],
    "20_contabilidade_aplicada_ao_setor_publico": [
        "20_contabilidade_aplicada_ao_setor_publico",
        "19_nocoes_de_administracao_financeira_e_orcamentaria",
    ],
    "21_nocoes_de_administracao_publica": [
        "21_nocoes_de_administracao_publica",
        "22_administracao_geral",
        "23_administracao_estrategica",
    ],
    "22_administracao_geral": [
        "22_administracao_geral",
        "21_nocoes_de_administracao_publica",
        "23_administracao_estrategica",
        "24_comportamento_organizacional",
    ],
    "23_administracao_estrategica": [
        "23_administracao_estrategica",
        "21_nocoes_de_administracao_publica",
        "22_administracao_geral",
    ],
    "24_comportamento_organizacional": [
        "24_comportamento_organizacional",
        "25_gestao_de_pessoas",
        "22_administracao_geral",
        "21_nocoes_de_administracao_publica",
    ],
    "25_gestao_de_pessoas": [
        "25_gestao_de_pessoas",
        "24_comportamento_organizacional",
        "22_administracao_geral",
        "21_nocoes_de_administracao_publica",
    ],
}


def normalize_rel_path(p):
    if not p:
        return ""
    p = p.replace("\\", "/").strip()
    p = p.replace("fontes_de_estudo/", "docs/")
    if os.path.isabs(p):
        p = os.path.relpath(p, BASE_DIR).replace("\\", "/")
    return p


def tokenize_pt(text):
    if not text:
        return []
    s = unicodedata.normalize("NFKD", text)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[^a-zA-Z0-9]+", " ", s).lower().strip()
    return [t for t in s.split() if len(t) > 2 and t not in STOPWORDS_PT]


def sanitize_md_text(s):
    """
    Preserva o texto 100% original da questão real, protegendo apenas tags XML/HTML/Generics
    com crases inline e cifrões de código/shell para não quebrar o compilador DOM/KaTeX.
    """
    if not s:
        return ""
    s = s.replace("\r\n", " ").replace("\n", " ").strip()
    # Se houver tags como <script>, <html>, <div>, <String, String>, <!DOCTYPE...>, <?xml...> fora de crases:
    if "<" in s and ">" in s and "`" not in s:
        s = re.sub(
            r"(<(?:!DOCTYPE|\?xml|/?[a-zA-Z][a-zA-Z0-9_:.,\-\s\"\'=/\?]*)>)",
            r"`\1`",
            s,
        )
        s = re.sub(r"(<<[a-zA-Z0-9_]+>>)", r"`\1`", s)
    # Escapar $ que não seja R$ ou US$ para não abrir bloco matemático KaTeX acidental
    s = re.sub(r"(?<!\\)(?<!R)(?<!US)\$", r"\$", s)
    return s


def extract_theory_statements(content):
    """
    Extrai proposições teóricas limpas do arquivo Markdown, indexadas por seção H2 e subseção H3/H4,
    calculando também o IDF de cada termo dentro do arquivo para pareamento de alta precisão.
    """
    pat_test = re.compile(
        r"^### Teste (\d+)\s*\n.*?>\s*\*\*Gabarito:[^\n]*\n+(?:---\s*\n)?",
        re.M | re.S,
    )
    c_no_tests = pat_test.sub("", content)
    c_no_tests = re.sub(
        r"^#{2,3}\s+[^\n]*(?:Fontes\s+Oficiais|Referências\s+Bibliográficas).*",
        "",
        c_no_tests,
        flags=re.M | re.S | re.I,
    )
    c_no_tests = re.sub(r"```.*?```", "", c_no_tests, flags=re.S)

    sections = re.split(r"(?m)^(#{2,4}\s+.+)$", c_no_tests)
    cur_sec = "Introdução"
    cur_h2 = "Fundamentação Teórica"
    stmts = []

    for part in sections:
        p_strip = part.strip()
        if re.match(r"^#{2,4}\s+", p_strip):
            hdr = re.sub(r"^#{2,4}\s+", "", p_strip).strip()
            if p_strip.startswith("## "):
                cur_h2 = f"## {hdr}"
            cur_sec = hdr.replace("*", "").strip()
        else:
            if any(k in cur_sec.lower() for k in ("introdução", "ementa", "sumário", "sumario")):
                continue
            for line in part.splitlines():
                line = line.strip()
                if (
                    not line
                    or line.startswith("---")
                    or line.startswith("#")
                    or "Matéria:" in line
                    or "Cargo:" in line
                    or "Arquivo:" in line
                ):
                    continue
                if line.startswith("|"):
                    cells = [c.strip() for c in line.strip("|").split("|") if c.strip()]
                    if not cells or all(re.match(r"^[:\-]+$", c) for c in cells):
                        continue
                    first_low = cells[0].lower()
                    if len(cells) >= 2 and not any(
                        h in first_low
                        for h in (
                            "característica",
                            "conceito",
                            "critério",
                            "elemento",
                            "item",
                            "atributo",
                            "aspecto",
                            "parâmetro",
                            "propriedade",
                        )
                    ):
                        line = f"{cells[0]}: " + " — ".join(cells[1:])
                    else:
                        continue

                line = re.sub(r"^>\s*(?:\[![A-Z]+\]\s*)?", "", line)
                line = re.sub(r"^(?:🚨|📌|⭐|💡|📝|🛑)\s*\*\*[^*]+:\*\*\s*", "", line)
                line = re.sub(r"^[-*+]\s+", "", line)
                line = re.sub(r"^\d+\.\s+", "", line)
                line = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", line)
                line = line.replace("**", "").strip()
                line = sanitize_md_text(line)

                if len(line) > 260:
                    sents = re.split(r"(?<=[.;])\s+(?=[A-ZÁÉÍÓÚÂÊÔÃÕÇ])", line)
                    buf = ""
                    for s in sents:
                        if len(buf) + len(s) < 250:
                            buf = (buf + " " + s).strip()
                        else:
                            clean_b = buf.rstrip(".:;").strip()
                            if len(clean_b) >= 40:
                                stmts.append(
                                    {
                                        "h2": cur_h2,
                                        "sec": cur_sec,
                                        "text": clean_b + ".",
                                        "tokens": set(tokenize_pt(clean_b + " " + cur_sec)),
                                    }
                                )
                            buf = s
                    clean_b = buf.rstrip(".:;").strip()
                    if len(clean_b) >= 40:
                        stmts.append(
                            {
                                "h2": cur_h2,
                                "sec": cur_sec,
                                "text": clean_b + ".",
                                "tokens": set(tokenize_pt(clean_b + " " + cur_sec)),
                            }
                        )
                else:
                    clean_l = line.rstrip(".:;").strip()
                    if len(clean_l) >= 40:
                        stmts.append(
                            {
                                "h2": cur_h2,
                                "sec": cur_sec,
                                "text": clean_l + ".",
                                "tokens": set(tokenize_pt(clean_l + " " + cur_sec)),
                            }
                        )

    # Calcular IDF dos tokens nas proposições teóricas deste arquivo
    df = Counter()
    for st in stmts:
        for t in st["tokens"]:
            df[t] += 1
    n_stmts = max(len(stmts), 1)
    for st in stmts:
        st["idf_weights"] = {
            t: math.log(1.0 + (n_stmts - df[t] + 0.5) / (df[t] + 0.5))
            for t in st["tokens"]
        }
    return stmts


def summarize_option_snippet(opt_text, max_len=115):
    clean = sanitize_md_text(opt_text).strip().rstrip(".;:")
    if len(clean) <= max_len:
        return clean
    cut = clean[:max_len]
    last_space = cut.rfind(" ")
    if last_space > 40:
        cut = cut[:last_space]
    return cut.rstrip(".,;:") + "..."


def detect_distractor_flaw(opt_text):
    low = opt_text.lower()
    if re.search(r"\b(apenas|somente|exclusivamente|unicamente)\b", low):
        return "incorre em restrição indevida ao limitar o escopo conceitual"
    if re.search(r"\b(nunca|jamais|em nenhuma hipótese|impossível|inviável|veda|proíbe)\b", low):
        return "apresenta vedação ou negativa absoluta incompatível com a regra aplicável"
    if re.search(r"\b(sempre|qualquer|todos os casos|incondicionalmente|irrestritamente|absoluto)\b", low):
        return "promove generalização excessiva que desconsidera as condições técnicas e normativas"
    if re.search(r"\b(prescinde|dispensa|independe|desnecessári[oa]|facultativ[oa])\b", low):
        return "afasta requisito ou relação estrutural exigida pela matéria"
    return "apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico"


def build_theory_grounded_comments(q, theory_stmts, target_h2, file_title):
    """
    Gera comentários analíticos para as alternativas A, B, C, D, E estritamente baseados
    na teoria do arquivo Markdown e no conteúdo específico de cada alternativa.
    """
    gab = q.get("gabarito", "A").strip().upper()
    alts = q.get("alternativas", {})
    banca = q.get("banca", "Banca")
    orgao = q.get("orgao", "Órgão")
    ano = q.get("ano", 2024)
    enun_tokens = set(tokenize_pt(q.get("enunciado", "")))
    gab_tokens = set(tokenize_pt(alts.get(gab, "")))

    used_stmt_indices = set()

    def pick_best_stmt(primary_tokens, secondary_tokens, prefer_h2=None):
        best_idx = -1
        best_score = -1.0
        for idx, st in enumerate(theory_stmts):
            if idx in used_stmt_indices and len(theory_stmts) > 5:
                continue
            idf_map = st.get("idf_weights", {})
            prim_score = sum(idf_map.get(t, 1.0) for t in (primary_tokens & st["tokens"]))
            sec_score = sum(idf_map.get(t, 1.0) for t in (secondary_tokens & st["tokens"]))
            score = prim_score * 3.5 + sec_score * 1.2
            if prefer_h2 and st["h2"] == prefer_h2:
                score += 2.0
            if score > best_score:
                best_score = score
                best_idx = idx
        if best_idx >= 0:
            used_stmt_indices.add(best_idx)
            return theory_stmts[best_idx]
        if theory_stmts:
            return theory_stmts[0]
        return {
            "h2": target_h2 or file_title,
            "sec": file_title.replace("*", ""),
            "text": f"A doutrina e a sistematização técnica de {file_title} estabelecem os critérios exatos cobrados no item.",
        }

    # Primeiro selecionar o melhor fragmento teórico para o gabarito oficial
    gab_stmt = pick_best_stmt(gab_tokens, enun_tokens, prefer_h2=target_h2)

    lines = []
    for let in ["A", "B", "C", "D", "E"]:
        opt_text = alts.get(let, "").strip()
        opt_snip = summarize_option_snippet(opt_text)
        opt_tokens = set(tokenize_pt(opt_text))

        if let == gab:
            sec_label = gab_stmt["sec"]
            theory_txt = gab_stmt["text"]
            lines.append(
                f"> - **{let})** **Correta.** Conforme fundamentado na seção *{sec_label}* deste guia, "
                f"{theory_txt[0].lower() + theory_txt[1:] if len(theory_txt) > 1 else theory_txt} "
                f"Dessa forma, está plenamente correta a assertiva da banca ({banca} – {orgao}/{ano}) ao estabelecer que \"{opt_snip}\"."
            )
        else:
            st = pick_best_stmt(opt_tokens | gab_tokens, enun_tokens, prefer_h2=target_h2)
            flaw_desc = detect_distractor_flaw(opt_text)
            sec_label = st["sec"]
            theory_txt = st["text"]
            lines.append(
                f"> - **{let})** **Incorreta.** A opção {flaw_desc} ao afirmar que \"{opt_snip}\". "
                f"De acordo com a teoria estudada em *{sec_label}*, {theory_txt[0].lower() + theory_txt[1:] if len(theory_txt) > 1 else theory_txt}"
            )

    return "\n".join(lines)


def format_question_markdown(num, q, theory_stmts, target_h2, file_title):
    banca = q.get("banca", "Banca Oficial").strip()
    orgao = q.get("orgao", "Órgão Oficial").strip()
    cargo = q.get("cargo", "Cargo Público").strip()
    ano = q.get("ano", 2024)
    enunciado = sanitize_md_text(q.get("enunciado", ""))
    alts = q.get("alternativas", {})
    gab = q.get("gabarito", "A").strip().upper()

    header = f"### Teste {num}\n**({banca} – {orgao} – {cargo} – {ano})**\n{enunciado}\n\n"

    alt_lines = []
    for let in ["A", "B", "C", "D", "E"]:
        alt_text = sanitize_md_text(alts.get(let, ""))
        alt_lines.append(f"* **{let})** {alt_text}")
    alts_block = "\n".join(alt_lines)

    comments = build_theory_grounded_comments(q, theory_stmts, target_h2, file_title)

    md = (
        f"{header}"
        f"{alts_block}\n\n"
        f"---\n\n"
        f"> **Comentário Detalhado:**\n>\n"
        f"{comments}\n"
        f">\n"
        f"> **Gabarito: {gab}**\n\n"
        f"---\n\n"
    )
    return md


def parse_file_tests_and_sections(content, check_all_non_existing=None):
    """
    Localiza todos os blocos ### Teste NNN de forma cirúrgica (terminando exatamente após > **Gabarito: X** e ---),
    preservando integralmente subtítulos H2, H3, H4 e a seção de Fontes Oficiais.
    Identifica também a seção ## (H2) à qual cada teste pertence.
    """
    h2_matches = list(re.finditer(r"^(##\s+[^\n]+)", content, re.M))
    pat_test = re.compile(
        r"^### Teste (\d+)\s*\n([^\n]+)\n(.*?>\s*\*\*Gabarito:[^\n]*\n+(?:---\s*\n+)?)",
        re.M | re.S,
    )

    tests = []
    for m in pat_test.finditer(content):
        num = m.group(1)
        hdr = m.group(2).strip()
        body = m.group(3)
        start = m.start()
        end = m.end()

        cur_h2 = "## 📌 Ementa / Itens do Edital"
        cur_h2_start = 0
        for h2m in h2_matches:
            if h2m.start() < start:
                cur_h2 = h2m.group(1).strip()
                cur_h2_start = h2m.start()
            else:
                break

        sec_context = content[cur_h2_start:start]
        is_sim = bool(re.search(r"Simulada|Inédita", hdr, re.I))
        if check_all_non_existing is not None and num in check_all_non_existing:
            is_sim = True

        tests.append(
            {
                "num": num,
                "hdr": hdr,
                "body": body,
                "start": start,
                "end": end,
                "is_sim": is_sim,
                "h2": cur_h2,
                "context_tokens": Counter(tokenize_pt(cur_h2 + " " + sec_context[-3000:] + " " + body[:600])),
            }
        )
    return tests


def score_question_for_slot(q_tokens, q_rel_score, slot_counter):
    overlap_score = 0.0
    for tok, cnt in q_tokens.items():
        if tok in slot_counter:
            overlap_score += min(cnt, 3) * min(slot_counter[tok], 5) * 2.5
    return overlap_score + min(float(q_rel_score or 0.0) * 0.08, 15.0)


def run_mass_injection(dry_run=False):
    print(f"[FASE 1] Lendo banco de dados sanitizado: {DB_FILE}...")
    with open(DB_FILE, "r", encoding="utf-8") as f:
        db = json.load(f)

    questoes = db.get("questoes", [])
    routes_fixed = 0
    for q in questoes:
        tf = q.get("target_file", "")
        new_tf = normalize_rel_path(tf)
        if tf != new_tf:
            routes_fixed += 1
        q["target_file"] = new_tf
        if "status_integracao" in q:
            del q["status_integracao"]

    print(f"[FASE 1] Total de questões no banco v2: {len(questoes)} (rotas normalizadas: {routes_fixed})")

    all_mds = []
    for root, _, files in os.walk(DOCS_DIR):
        if "resources" in root:
            continue
        for file in sorted(files):
            if file.endswith(".md") and file not in (
                "README.md",
                "relatorio_cobertura_questoes.md",
                "index.md",
            ):
                full_p = os.path.join(root, file)
                rel_p = normalize_rel_path(full_p)
                all_mds.append((rel_p, full_p))

    all_mds.sort(key=lambda x: x[0])
    print(f"[FASE 2] Analisando {len(all_mds)} cadernos de estudo em docs/...")

    def norm_alnum(s):
        return re.sub(r"[^a-z0-9]+", "", (s or "").lower())

    q_norm_prefix = [(q, norm_alnum(q.get("enunciado", ""))[:80]) for q in questoes]

    files_state = {}
    pre_existing_real_matched = 0

    for rel_p, full_p in all_mds:
        with open(full_p, "r", encoding="utf-8") as f:
            content = f.read()

        h1_m = re.search(r"^#\s+([^\n]+)", content, re.M)
        file_title = h1_m.group(1).strip() if h1_m else os.path.basename(full_p)
        theory_stmts = extract_theory_statements(content)
        parsed_tests = parse_file_tests_and_sections(content)

        for t in parsed_tests:
            if not t["is_sim"]:
                snip = norm_alnum(t["body"])[:65]
                if len(snip) >= 25:
                    for q, q_pref in q_norm_prefix:
                        if q.get("status_integracao") != "injetada" and snip[:45] in q_pref:
                            q["status_integracao"] = "injetada"
                            pre_existing_real_matched += 1
                            break

        parts = rel_p.split("/")
        mod_key = parts[2] if len(parts) > 2 else ""

        files_state[rel_p] = {
            "rel_p": rel_p,
            "full_p": full_p,
            "mod_key": mod_key,
            "file_title": file_title,
            "content": content,
            "theory_stmts": theory_stmts,
            "tests": parsed_tests,
            "sim_tests": [t for t in parsed_tests if t["is_sim"]],
            "assigned": {},
        }

    eligible_me5 = []
    q_tokens_cache = {}
    for q in questoes:
        if q.get("status_integracao") == "injetada":
            continue
        if q.get("formato") != "MULTIPLA_ESCOLHA_5":
            continue
        alts = q.get("alternativas", {})
        gab = q.get("gabarito", "").strip().upper()
        if gab not in ("A", "B", "C", "D", "E") or len(alts) < 5:
            continue
        eligible_me5.append(q)
        q_tokens_cache[q["id"]] = Counter(
            tokenize_pt(q.get("enunciado", "") + " " + alts.get(gab, ""))
        )

    by_file_pool = defaultdict(list)
    by_mod_pool = defaultdict(list)
    for q in eligible_me5:
        tf = q["target_file"]
        by_file_pool[tf].append(q)
        parts = tf.split("/")
        if len(parts) > 2:
            by_mod_pool[parts[2]].append(q)

    # PASSO 1: Alocação Semântica Direta (questões cujo target_file já é o arquivo atual)
    pass1_count = 0
    for rel_p, st in files_state.items():
        sim_slots = st["sim_tests"]
        if not sim_slots:
            continue
        candidates = [q for q in by_file_pool.get(rel_p, []) if q.get("status_integracao") != "injetada"]
        if not candidates:
            continue

        pairs = []
        for s_idx, slot in enumerate(sim_slots):
            for c_idx, cand in enumerate(candidates):
                sc = score_question_for_slot(
                    q_tokens_cache[cand["id"]],
                    cand.get("relevance_score", 0.0),
                    slot["context_tokens"],
                )
                pairs.append((sc, s_idx, c_idx))

        pairs.sort(key=lambda x: x[0], reverse=True)
        used_slots = set()
        used_cands = set()

        for sc, s_idx, c_idx in pairs:
            if s_idx in used_slots or c_idx in used_cands:
                continue
            slot = sim_slots[s_idx]
            cand = candidates[c_idx]
            used_slots.add(s_idx)
            used_cands.add(c_idx)
            cand["status_integracao"] = "injetada"
            cand["target_file"] = rel_p
            cand["target_section"] = slot["h2"]
            st["assigned"][slot["num"]] = cand
            pass1_count += 1
            if len(used_slots) == len(sim_slots) or len(used_cands) == len(candidates):
                break

    # PASSO 2: Alocação Semântica para os slots remanescentes (buscando no módulo ou módulos irmãos)
    pass2_count = 0
    for rel_p, st in files_state.items():
        unfilled_slots = [t for t in st["sim_tests"] if t["num"] not in st["assigned"]]
        if not unfilled_slots:
            continue

        mod_key = st["mod_key"]
        allowed_mods = FAMILY_FALLBACKS.get(mod_key, [mod_key])

        cand_pool = []
        for m_idx, m_name in enumerate(allowed_mods):
            mod_boost = 2.0 if m_idx == 0 else 1.35
            for q in by_mod_pool.get(m_name, []):
                if q.get("status_integracao") != "injetada":
                    cand_pool.append((q, mod_boost))

        if len(cand_pool) < len(unfilled_slots):
            for q in eligible_me5:
                if q.get("status_integracao") != "injetada":
                    cand_pool.append((q, 0.8))

        for slot in unfilled_slots:
            best_q = None
            best_sc = -1e9
            for cand, boost in cand_pool:
                if cand.get("status_integracao") == "injetada":
                    continue
                sc = (
                    score_question_for_slot(
                        q_tokens_cache[cand["id"]],
                        cand.get("relevance_score", 0.0),
                        slot["context_tokens"],
                    )
                    * boost
                )
                if sc > best_sc:
                    best_sc = sc
                    best_q = cand

            if best_q is not None:
                best_q["status_integracao"] = "injetada"
                best_q["target_file"] = rel_p
                best_q["target_section"] = slot["h2"]
                st["assigned"][slot["num"]] = best_q
                pass2_count += 1

    total_injected = 0
    files_modified = 0

    for rel_p, st in files_state.items():
        if not st["assigned"]:
            continue
        modified_content = st["content"]
        file_injected = 0

        for slot in sorted(st["sim_tests"], key=lambda x: x["start"], reverse=True):
            q = st["assigned"].get(slot["num"])
            if not q:
                continue
            new_block = format_question_markdown(
                slot["num"],
                q,
                st["theory_stmts"],
                slot["h2"],
                st["file_title"],
            )
            modified_content = (
                modified_content[: slot["start"]]
                + new_block
                + modified_content[slot["end"] :]
            )
            file_injected += 1
            total_injected += 1

        if file_injected > 0:
            files_modified += 1
            if not dry_run:
                with open(st["full_p"], "w", encoding="utf-8") as f:
                    f.write(modified_content)
            print(
                f"[{'DRY-RUN' if dry_run else 'OK'}] {rel_p}: +{file_injected} questões reais injetadas"
            )

    print("\n============================================================")
    print(f" Questões reais injetadas via target_file direto (Passo 1): {pass1_count}")
    print(f" Questões reais injetadas via afinidade semântica (Passo 2): {pass2_count}")
    print(f" TOTAL DE QUESTÕES REAIS INJETADAS NESTA RODADA: {total_injected}")
    print(f" Total de arquivos Markdown atualizados: {files_modified}")
    print("============================================================")

    if not dry_run and total_injected > 0:
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump(db, f, ensure_ascii=False, indent=2)
        print(f"[FASE 3] Base {DB_FILE} salva e atualizada com sucesso.")


if __name__ == "__main__":
    dry = "--dry-run" in sys.argv
    run_mass_injection(dry_run=dry)
