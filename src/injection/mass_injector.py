#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
src/injection/mass_injector.py

Motor de Injeção de Alta Precisão de Questões Reais (Banco V3 - MCP).
1. Fase 1: Lê `data/banco_questoes_v3.json` (3.520 questões reais extraídas via MCP),
   mantém ativa a Blacklist de temas inéditos/fronteira tecnológica (preservando as questões
   simuladas calibradas nesses arquivos), e utiliza as chaves `"target_area"`,
   `"target_materia"` e `"target_topico"` para localizar o arquivo `.md` e a seção correta.
2. Fase 2: Para cada arquivo em `docs/` (exceto os da Blacklist), substitui os blocos
   `### Teste NNN`, insere enunciado e alternativas (A-E ou Certo/Errado) *ipsis litteris*
   com cabeçalho oficial `**(Banca – Órgão – Ano – Cargo)**`, gera o bloco de
   "Comentário Detalhado" ancorado estritamente na teoria do próprio arquivo Markdown,
   e marca cada questão utilizada no JSON V3 como `"status_integracao": "injetada"`.
"""

import json
import math
import os
import re
import sys
import unicodedata
from collections import Counter, defaultdict

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DB_FILE = os.path.join(BASE_DIR, "data", "banco_questoes_v3.json")
DOCS_DIR = os.path.join(BASE_DIR, "docs")

# Blacklist estrita: temas de fronteira tecnológica e leis estaduais/normativos inéditos sem histórico em provas
BLACKLIST_PATHS = (
    "docs/conhecimentos_especificos_b02_ti/06_engenharia_software_ia_e_sistemas_agentivos/",
    "docs/conhecimentos_especificos_b02_ti/13_legislacao_aplicada_a_ti/04_lei_complementar_estadual_205_2025.md",
    "docs/conhecimentos_gerais/03_legislacao_institucional/06_politicas_institucionais_e_resolucoes_normativas.md",
)

AREA_TO_DIR = {
    "CONHECIMENTOS GERAIS (A01 E B02)": "conhecimentos_gerais",
    "CONHECIMENTOS ESPECÍFICOS A01 - TÉCNICO ADMINISTRATIVO": "conhecimentos_especificos_a01_tecnico_administrativo",
    "CONHECIMENTOS ESPECÍFICOS B02 - TI": "conhecimentos_especificos_b02_ti",
}

MATERIA_TO_MODULE = {
    "Língua Portuguesa": "01_lingua_portuguesa",
    "Matemática e Raciocínio Lógico": "02_matematica_e_raciocinio_logico",
    "Legislação Institucional": "03_legislacao_institucional",
    "Engenharia de Software": "04_engenharia_de_software",
    "Desenvolvimento de Sistemas": "05_desenvolvimento_de_sistemas",
    "Engenharia de Software Assistida por Inteligência Artificial e Sistemas Agentivos": "06_engenharia_software_ia_e_sistemas_agentivos",
    "DevOps, Plataforma de Desenvolvimento e Engenharia de Entrega": "07_devops_e_plataforma_de_entrega",
    "Banco de Dados": "08_banco_de_dados",
    "Inteligência Artificial, Ciência de Dados e Automação": "09_inteligencia_artificial_e_ciencia_de_dados",
    "Segurança da Informação": "10_seguranca_da_informacao",
    "Sistemas Operacionais, Redes e Computação em Nuvem": "11_sistemas_operacionais_redes_e_nuvem",
    "Governança de Tecnologia da Informação": "12_governanca_de_ti",
    "Legislação Aplicada à Tecnologia da Informação": "13_legislacao_aplicada_a_ti",
    "Língua Inglesa (Leitura Técnica)": "14_lingua_inglesa_leitura_tecnica",
    "Noções de Direito Administrativo": "15_nocoes_de_direito_administrativo",
    "Licitações e Contratos Administrativos": "16_licitacoes_e_contratos_administrativos",
    "Noções de Direito Constitucional": "17_nocoes_de_direito_constitucional",
    "Noções de Controle Externo": "18_nocoes_de_controle_externo",
    "Noções de Administração Financeira e Orçamentária": "19_nocoes_de_administracao_financeira_e_orcamentaria",
    "Contabilidade aplicada ao Setor Público": "20_contabilidade_aplicada_ao_setor_publico",
    "Noções de Administração Pública": "21_nocoes_de_administracao_publica",
    "Administração Geral": "22_administracao_geral",
    "Administração Estratégica": "23_administracao_estrategica",
    "Comportamento Organizacional": "24_comportamento_organizacional",
    "Gestão de Pessoas": "25_gestao_de_pessoas",
}

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
        "06_engenharia_software_ia_e_sistemas_agentivos",
    ],
    "05_desenvolvimento_de_sistemas": [
        "05_desenvolvimento_de_sistemas",
        "04_engenharia_de_software",
        "07_devops_e_plataforma_de_entrega",
        "06_engenharia_software_ia_e_sistemas_agentivos",
    ],
    "07_devops_e_plataforma_de_entrega": [
        "07_devops_e_plataforma_de_entrega",
        "06_engenharia_software_ia_e_sistemas_agentivos",
        "05_desenvolvimento_de_sistemas",
        "04_engenharia_de_software",
        "11_sistemas_operacionais_redes_e_nuvem",
    ],
    "08_banco_de_dados": [
        "08_banco_de_dados",
        "09_inteligencia_artificial_e_ciencia_de_dados",
        "06_engenharia_software_ia_e_sistemas_agentivos",
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
        "04_engenharia_de_software",
        "06_engenharia_software_ia_e_sistemas_agentivos",
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


def is_blacklisted(rel_path):
    """Verifica se o caminho relativo pertence à Blacklist de preservação de questões simuladas."""
    norm = normalize_rel_path(rel_path)
    for bp in BLACKLIST_PATHS:
        if bp.endswith("/"):
            if norm.startswith(bp):
                return True
        else:
            if norm == bp:
                return True
    return False


def normalize_ascii_lower(text):
    if not text:
        return ""
    s = unicodedata.normalize("NFKD", text)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-zA-Z0-9]+", " ", s).lower().strip()


def tokenize_pt(text):
    norm = normalize_ascii_lower(text)
    if not norm:
        return []
    return [t for t in norm.split() if len(t) > 2 and t not in STOPWORDS_PT]


def is_english_question(q):
    text = (q.get("enunciado", "") + " " + " ".join(q.get("alternativas", {}).values())).lower()
    en_hits = len(
        re.findall(
            r"\b(the|and|with|for|that|this|from|which|are|is|in|of|to|following|according|read|text)\b",
            text,
        )
    )
    return en_hits >= 6


def is_literary_or_grammar_only_question(q):
    text = (q.get("enunciado", "") + " " + " ".join(q.get("alternativas", {}).values())).lower()
    return bool(
        re.search(
            r"leia o poema|eu lírico|guimarães rosa|machado de assis|cruz e souza|"
            r"sinais de pontuação|oração subordinada|regência verbal|indicativo de crase|"
            r"sentido conotativo|figuras de linguagem|tipologias textuais",
            text,
        )
    )


def sanitize_theory_snippet(s):
    if not s:
        return ""
    s = s.replace("\r\n", " ").replace("\n", " ").strip()
    if "<" in s and ">" in s and "`" not in s:
        s = re.sub(
            r"(<(?:!DOCTYPE|\?xml|/?[a-zA-Z][a-zA-Z0-9_:.,\-\s\"\'=/\?]*)>)",
            r"`\1`",
        s,
        )
        s = re.sub(r"(<<[a-zA-Z0-9_]+>>)", r"`\1`", s)
    non_currency_dollars = re.findall(r"(?<!\\)(?<!R)(?<!US)\$", s)
    if len(non_currency_dollars) % 2 == 1:
        s = re.sub(r"(?<!\\)(?<!R)(?<!US)\$", r"\$", s)
    return s


def extract_ementa_and_h2_metadata(content):
    """Extrai o texto da Ementa e os títulos/textos de cada seção H2 para pareamento com target_topico."""
    m_em = re.search(r"## [^\n]*Ementa[^\n]*\n(.*?)(?=\n---|\n## )", content, re.S | re.I)
    ementa_raw = m_em.group(1).strip() if m_em else ""
    ementa_norm = normalize_ascii_lower(ementa_raw)
    ementa_tokens = Counter(tokenize_pt(ementa_raw))

    h2_sections = []
    h2_matches = list(re.finditer(r"^(##\s+[^\n]+)", content, re.M))
    for i, m in enumerate(h2_matches):
        h2_title = m.group(1).strip()
        if any(k in h2_title.lower() for k in ("ementa", "sumário", "sumario", "fontes", "referências")):
            continue
        start = m.start()
        end = h2_matches[i + 1].start() if i + 1 < len(h2_matches) else len(content)
        sec_body = content[start:end]
        # Remover blocos de teste para avaliar apenas a teoria da seção H2
        sec_theory = re.sub(
            r"^### Teste (\d+)\s*\n.*?>\s*\*\*Gabarito:[^\n]*\n+(?:---\s*\n+)?",
            "",
            sec_body,
            flags=re.M | re.S,
        )
        h2_sections.append(
            {
                "h2": h2_title,
                "norm_title": normalize_ascii_lower(h2_title),
                "title_tokens": set(tokenize_pt(h2_title)),
                "body_tokens": Counter(tokenize_pt(sec_theory[:4000])),
            }
        )
    return ementa_norm, ementa_tokens, h2_sections


def extract_theory_statements(content):
    """
    Extrai proposições teóricas limpas do arquivo Markdown, indexadas por seção H2 e subseção H3/H4,
    calculando também o IDF de cada termo dentro do arquivo para fundamentação analítica dos comentários.
    """
    pat_test = re.compile(
        r"^### Teste (\d+)\s*\n.*?>\s*\*\*Gabarito:[^\n]*\n+(?:---\s*\n)?",
        re.M | re.S,
    )
    c_no_tests = pat_test.sub("", content)
    c_no_tests = re.sub(
        r"^#{2,3}\s+[^\n]*(?:Fontes\s+Oficiais|Fontes\s+Recomendadas|Referências\s+Bibliográficas).*",
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
                line = sanitize_theory_snippet(line)

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
    clean = sanitize_theory_snippet(opt_text).strip().rstrip(".;:")
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
    Gera o bloco de 'Comentário Detalhado' justificando o erro ou acerto de cada alternativa
    (A-E ou Certo/Errado) ancorando-se estritamente na teoria presente no texto do próprio arquivo Markdown.
    """
    gab = (q.get("gabarito_oficial") or q.get("gabarito") or "A").strip().upper()
    alts = q.get("alternativas", {})
    formato = q.get("formato", "MULTIPLA_ESCOLHA_5")
    banca = q.get("banca", "Banca")
    orgao = q.get("orgao", "Órgão")
    ano = q.get("ano", 2024)
    enun_text = q.get("enunciado", "")
    enun_tokens = set(tokenize_pt(enun_text))
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

    if formato == "CERTO_ERRADO" or set(alts.keys()) == {"C", "E"}:
        st_main = pick_best_stmt(enun_tokens, enun_tokens, prefer_h2=target_h2)
        st_comp = pick_best_stmt(enun_tokens, enun_tokens, prefer_h2=target_h2)
        sec1 = st_main["sec"]
        txt1 = st_main["text"]
        txt1_low = txt1[0].lower() + txt1[1:] if len(txt1) > 1 else txt1
        sec2 = st_comp["sec"]
        txt2 = st_comp["text"]
        txt2_low = txt2[0].lower() + txt2[1:] if len(txt2) > 1 else txt2
        enun_snip = summarize_option_snippet(enun_text, max_len=110)

        if gab == "C":
            return "\n".join(
                [
                    f"> - **C)** **Correta.** O item está **Certo**. Conforme fundamentado na seção *{sec1}* deste guia, {txt1_low} Dessa forma, está plenamente correta a proposição da banca ({banca} – {orgao}/{ano}) ao afirmar que \"{enun_snip}\".",
                    f"> - **E)** **Incorreta.** A marcação como **Errado** não procede, visto que a assertiva guarda integral conformidade com a teoria estudada em *{sec2}*, segundo a qual {txt2_low}",
                ]
            )
        else:
            flaw_desc = detect_distractor_flaw(enun_text)
            return "\n".join(
                [
                    f"> - **C)** **Incorreta.** A marcação como **Certo** não procede, pois o enunciado {flaw_desc} ao afirmar que \"{enun_snip}\". De acordo com a teoria estudada em *{sec2}*, {txt2_low}",
                    f"> - **E)** **Correta.** O item está **Errado** (gabarito oficial: **E**). Conforme fundamentado na seção *{sec1}* deste guia, {txt1_low} Portanto, a assertiva examinada pela banca ({banca} – {orgao}/{ano}) viola os preceitos técnicos do tópico.",
                ]
            )

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
    """
    Formata o bloco ### Teste NNN preservando ipsis litteris o enunciado e as alternativas
    da banca e utilizando o cabeçalho oficial **(Banca – Órgão – Ano – Cargo)**.
    """
    banca = str(q.get("banca", "Banca Oficial")).strip()
    orgao = str(q.get("orgao", "Órgão Oficial")).strip()
    ano = q.get("ano", 2024)
    cargo = str(q.get("cargo", "Cargo Público")).strip()
    enunciado = q.get("enunciado", "").strip()
    alts = q.get("alternativas", {})
    formato = q.get("formato", "MULTIPLA_ESCOLHA_5")
    gab = (q.get("gabarito_oficial") or q.get("gabarito") or "A").strip().upper()

    header = f"### Teste {num}\n**({banca} – {orgao} – {ano} – {cargo})**\n{enunciado}\n\n"

    alt_lines = []
    if formato == "CERTO_ERRADO" or set(alts.keys()) == {"C", "E"}:
        for let in ["C", "E"]:
            alt_text = alts.get(let, "Certo" if let == "C" else "Errado").strip()
            alt_lines.append(f"* **{let})** {alt_text}")
    else:
        for let in ["A", "B", "C", "D", "E"]:
            alt_text = alts.get(let, "").strip()
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


def parse_file_tests_and_sections(content):
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

        tests.append(
            {
                "num": num,
                "hdr": hdr,
                "body": body,
                "start": start,
                "end": end,
                "is_sim": is_sim,
                "h2": cur_h2,
                "h2_norm": normalize_ascii_lower(cur_h2),
                "context_tokens": Counter(
                    tokenize_pt(cur_h2 + " " + sec_context[-3000:] + " " + body[:600])
                ),
            }
        )
    return tests


def resolve_question_target_via_edital_tags(q, files_by_mod, all_files_state):
    """
    Utiliza as chaves 'target_area', 'target_materia' e 'target_topico' do JSON V3
    para localizar o arquivo .md correspondente e a seção H2 mais aderente.
    """
    t_area = q.get("target_area", "")
    t_mat = q.get("target_materia", "")
    t_top = q.get("target_topico", "")

    area_dir = AREA_TO_DIR.get(t_area, "")
    mod_key = MATERIA_TO_MODULE.get(t_mat, "")

    top_norm = normalize_ascii_lower(t_top)
    top_tokens = set(tokenize_pt(t_top))
    gab = (q.get("gabarito_oficial") or q.get("gabarito") or "").strip().upper()
    q_text_tokens = Counter(
        tokenize_pt(
            t_top
            + " "
            + q.get("enunciado", "")
            + " "
            + q.get("alternativas", {}).get(gab, "")
        )
    )

    candidate_files = files_by_mod.get(mod_key, [])
    if area_dir:
        filtered = [st for st in candidate_files if f"/{area_dir}/" in f"/{st['rel_p']}/"]
        if filtered:
            candidate_files = filtered

    best_file = None
    best_file_score = -1e9
    best_h2 = None

    for st in candidate_files:
        sc = 0.0
        # 1. Substring exata ou parcial de target_topico na Ementa ou no Título do arquivo
        if top_norm and len(top_norm) >= 6:
            if top_norm in st["ementa_norm"]:
                sc += 35.0
            elif top_norm[:22] in st["ementa_norm"] or top_norm in st["title_norm"]:
                sc += 22.0

        # 2. Interseção de tokens de target_topico com Ementa e Título do arquivo
        for tok in top_tokens:
            if tok in st["title_tokens"]:
                sc += 8.0
            if tok in st["ementa_tokens"]:
                sc += 5.0

        # 3. Interseção com as seções H2 do arquivo para localizar a seção correta
        local_best_h2 = None
        local_best_h2_sc = -1.0
        for h2_info in st["h2_sections"]:
            h2_sc = 0.0
            if top_norm and len(top_norm) >= 6 and top_norm[:18] in h2_info["norm_title"]:
                h2_sc += 15.0
            for tok in top_tokens:
                if tok in h2_info["title_tokens"]:
                    h2_sc += 6.0
                if tok in h2_info["body_tokens"]:
                    h2_sc += min(h2_info["body_tokens"][tok], 4) * 1.5
            for tok, cnt in q_text_tokens.items():
                if tok in h2_info["body_tokens"]:
                    h2_sc += min(cnt, 3) * min(h2_info["body_tokens"][tok], 4) * 0.8
            if h2_sc > local_best_h2_sc:
                local_best_h2_sc = h2_sc
                local_best_h2 = h2_info["h2"]

        sc += max(local_best_h2_sc, 0.0)
        if sc > best_file_score:
            best_file_score = sc
            best_file = st["rel_p"]
            best_h2 = local_best_h2

    return mod_key, best_file, best_h2


def score_question_for_slot(q, q_tokens, slot, target_mod_key):
    overlap_score = 0.0
    slot_counter = slot["context_tokens"]
    for tok, cnt in q_tokens.items():
        if tok in slot_counter:
            overlap_score += min(cnt, 3) * min(slot_counter[tok], 5) * 2.5

    # Bônus se target_topico ou resolved_h2 coincidir com a seção H2 do slot
    if q.get("_resolved_h2") and q["_resolved_h2"] == slot["h2"]:
        overlap_score += 18.0
    top_tokens = q.get("_topico_tokens", set())
    for tok in top_tokens:
        if tok in slot_counter:
            overlap_score += 4.5

    # Preferência por Múltipla Escolha 5 alternativas (FCC/FGV), mantendo suporte a Certo/Errado
    if q.get("formato") == "MULTIPLA_ESCOLHA_5":
        overlap_score += 6.0
    if q.get("banca") == "FCC":
        overlap_score += 2.5

    # Guardas de domínio
    if target_mod_key != "01_lingua_portuguesa" and is_literary_or_grammar_only_question(q):
        overlap_score -= 120.0
    if target_mod_key == "14_lingua_inglesa_leitura_tecnica" and q.get("_is_english"):
        overlap_score += 45.0

    return overlap_score


def run_mass_injection(dry_run=False):
    print(f"[FASE 1] Lendo banco de dados V3 (MCP): {DB_FILE}...")
    with open(DB_FILE, "r", encoding="utf-8") as f:
        db = json.load(f)

    questoes = db if isinstance(db, list) else db.get("questoes", [])
    for q in questoes:
        if "status_integracao" in q:
            del q["status_integracao"]

    print(f"[FASE 1] Total de questões reais no banco V3: {len(questoes)}")

    all_mds = []
    skipped_blacklist = []
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
                if is_blacklisted(rel_p):
                    skipped_blacklist.append((rel_p, full_p))
                else:
                    all_mds.append((rel_p, full_p))

    all_mds.sort(key=lambda x: x[0])
    skipped_blacklist.sort(key=lambda x: x[0])
    print(
        f"[FASE 1] Blacklist ativa: {len(skipped_blacklist)} arquivos ignorados (questões simuladas calibradas preservadas):"
    )
    for rel_p, _ in skipped_blacklist:
        print(f"  -> [BLACKLIST] {rel_p}")

    print(f"[FASE 2] Analisando {len(all_mds)} cadernos elegíveis em docs/...")

    files_state = {}
    files_by_mod = defaultdict(list)

    for rel_p, full_p in all_mds:
        with open(full_p, "r", encoding="utf-8") as f:
            content = f.read()

        h1_m = re.search(r"^#\s+([^\n]+)", content, re.M)
        file_title = h1_m.group(1).strip() if h1_m else os.path.basename(full_p)
        ementa_norm, ementa_tokens, h2_sections = extract_ementa_and_h2_metadata(content)
        theory_stmts = extract_theory_statements(content)
        parsed_tests = parse_file_tests_and_sections(content)

        parts = rel_p.split("/")
        mod_key = parts[2] if len(parts) > 2 else ""

        st = {
            "rel_p": rel_p,
            "full_p": full_p,
            "mod_key": mod_key,
            "file_title": file_title,
            "title_norm": normalize_ascii_lower(file_title + " " + os.path.basename(rel_p)),
            "title_tokens": set(tokenize_pt(file_title + " " + os.path.basename(rel_p))),
            "ementa_norm": ementa_norm,
            "ementa_tokens": ementa_tokens,
            "h2_sections": h2_sections,
            "content": content,
            "theory_stmts": theory_stmts,
            "tests": parsed_tests,
            "assigned": {},
        }
        files_state[rel_p] = st
        files_by_mod[mod_key].append(st)

    # Preparar e indexar questões do banco V3 usando target_area, target_materia e target_topico
    eligible_questions = []
    q_tokens_cache = {}
    by_file_pool = defaultdict(list)
    by_mod_pool = defaultdict(list)
    english_pool = []

    for q in questoes:
        fmt = q.get("formato", "MULTIPLA_ESCOLHA_5")
        alts = q.get("alternativas", {})
        gab = (q.get("gabarito_oficial") or q.get("gabarito") or "").strip().upper()
        if fmt == "MULTIPLA_ESCOLHA_5":
            if gab not in ("A", "B", "C", "D", "E") or len(alts) < 5:
                continue
        elif fmt == "CERTO_ERRADO":
            if gab not in ("C", "E"):
                continue
        else:
            continue

        mod_key, resolved_file, resolved_h2 = resolve_question_target_via_edital_tags(
            q, files_by_mod, files_state
        )
        q["_mod_key"] = mod_key
        q["_resolved_file"] = resolved_file
        q["_resolved_h2"] = resolved_h2
        q["_topico_tokens"] = set(tokenize_pt(q.get("target_topico", "")))
        q["_is_english"] = is_english_question(q)

        q_tokens_cache[q["id"]] = Counter(
            tokenize_pt(
                q.get("target_topico", "")
                + " "
                + q.get("enunciado", "")
                + " "
                + " ".join(alts.values())
            )
        )

        eligible_questions.append(q)
        if resolved_file:
            by_file_pool[resolved_file].append(q)
        if mod_key:
            by_mod_pool[mod_key].append(q)
        if q["_is_english"]:
            english_pool.append(q)

    # PASSO 1: Alocação Direta via (target_area, target_materia, target_topico) -> arquivo .md e seção H2
    pass1_count = 0
    for rel_p, st in files_state.items():
        slots = st["tests"]
        if not slots:
            continue
        candidates = [
            q for q in by_file_pool.get(rel_p, []) if q.get("status_integracao") != "injetada"
        ]
        if not candidates:
            continue

        pairs = []
        for s_idx, slot in enumerate(slots):
            for c_idx, cand in enumerate(candidates):
                sc = score_question_for_slot(
                    cand,
                    q_tokens_cache[cand["id"]],
                    slot,
                    st["mod_key"],
                )
                pairs.append((sc, s_idx, c_idx))

        pairs.sort(key=lambda x: x[0], reverse=True)
        used_slots = set()
        used_cands = set()

        for sc, s_idx, c_idx in pairs:
            if s_idx in used_slots or c_idx in used_cands:
                continue
            if sc < 0:
                continue
            slot = slots[s_idx]
            cand = candidates[c_idx]
            used_slots.add(s_idx)
            used_cands.add(c_idx)
            cand["status_integracao"] = "injetada"
            st["assigned"][slot["num"]] = cand
            pass1_count += 1
            if len(used_slots) == len(slots) or len(used_cands) == len(candidates):
                break

    # PASSO 2: Alocação Semântica nos slots remanescentes do arquivo (a partir de target_materia e módulos correlatos)
    pass2_count = 0
    for rel_p, st in files_state.items():
        unfilled_slots = [t for t in st["tests"] if t["num"] not in st["assigned"]]
        if not unfilled_slots:
            continue

        mod_key = st["mod_key"]
        allowed_mods = FAMILY_FALLBACKS.get(mod_key, [mod_key])

        cand_pool = []
        if mod_key == "14_lingua_inglesa_leitura_tecnica":
            for q in english_pool:
                if q.get("status_integracao") != "injetada":
                    cand_pool.append((q, 2.2))

        for m_idx, m_name in enumerate(allowed_mods):
            mod_boost = 2.0 if m_idx == 0 else 1.35
            for q in by_mod_pool.get(m_name, []):
                if q.get("status_integracao") != "injetada":
                    cand_pool.append((q, mod_boost))

        if len(cand_pool) < len(unfilled_slots):
            for q in eligible_questions:
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
                        cand,
                        q_tokens_cache[cand["id"]],
                        slot,
                        mod_key,
                    )
                    * boost
                )
                if sc > best_sc:
                    best_sc = sc
                    best_q = cand

            if best_q is not None:
                best_q["status_integracao"] = "injetada"
                st["assigned"][slot["num"]] = best_q
                pass2_count += 1

    total_injected = 0
    files_modified = 0

    for rel_p, st in files_state.items():
        if not st["assigned"]:
            continue
        modified_content = st["content"]
        file_injected = 0

        for slot in sorted(st["tests"], key=lambda x: x["start"], reverse=True):
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
                f"[{'DRY-RUN' if dry_run else 'OK'}] {rel_p}: {file_injected} questões reais V3 injetadas"
            )

    # Limpar chaves auxiliares temporárias antes de persistir o JSON V3
    for q in questoes:
        for k in list(q.keys()):
            if k.startswith("_"):
                del q[k]

    print("\n============================================================")
    print(f" Arquivos na Blacklist preservados intactos: {len(skipped_blacklist)}")
    print(f" Questões reais V3 injetadas via target_topico direto (Passo 1): {pass1_count}")
    print(f" Questões reais V3 injetadas via target_materia/afinidade (Passo 2): {pass2_count}")
    print(f" TOTAL DE QUESTÕES REAIS INJETADAS (BANCO V3): {total_injected}")
    print(f" Total de arquivos Markdown atualizados: {files_modified}")
    print("============================================================")

    if not dry_run and total_injected > 0:
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump(db, f, ensure_ascii=False, indent=2)
        print(f"[FASE 2] Base {DB_FILE} salva e atualizada com 'status_integracao': 'injetada'.")


if __name__ == "__main__":
    dry = "--dry-run" in sys.argv
    run_mass_injection(dry_run=dry)
