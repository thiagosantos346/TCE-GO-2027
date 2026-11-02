#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
src/injection/mass_injector.py

Motor de Injeção Cirúrgica de Questões Reais (Banco V3 - LLM Classified).
1. Lê `data/banco_questoes_v3.json` (apenas questões válidas pós-purga de LIXO).
2. Preserva estritamente a Blacklist (temas inéditos/fronteira tecnológica e leis sem histórico).
3. Utiliza as chaves "target_area", "target_materia" e "target_topico" geradas pelo LLM
   para direcionar cada questão ao caderno correto (.md) e à seção teórica correspondente (## Tópico).
4. Insere (append) as questões no final de cada seção teórica correspondente, com enunciado e alternativas
   ipsis litteris, cabeçalho oficial **(Banca – Órgão – Ano – Cargo)** e comentários detalhados
   ancorados na teoria do arquivo.
5. Renumera todos os testes sequencialmente (### Teste 001, ### Teste 002, ...) por arquivo.
6. Marca no banco JSON "status_integracao": "injetada".
"""

import json
import math
import os
import re
import sys
import unicodedata
from collections import Counter, defaultdict

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DB_FILE = os.path.join(BASE_DIR, "data", "banco_questoes_v3_limpo.json")
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


def normalize_rel_path(path: str) -> str:
    rel = os.path.relpath(path, BASE_DIR).replace("\\", "/")
    if rel.startswith("./"):
        rel = rel[2:]
    return rel


def is_blacklisted(rel_path: str) -> bool:
    norm = rel_path.replace("\\", "/")
    for bl in BLACKLIST_PATHS:
        if bl.endswith("/") and norm.startswith(bl):
            return True
        elif norm == bl:
            return True
    return False


def normalize_ascii_lower(text: str) -> str:
    if not text:
        return ""
    nfkd = unicodedata.normalize("NFKD", text)
    no_accent = "".join([c for c in nfkd if not unicodedata.combining(c)])
    return no_accent.lower()


def tokenize_pt(text: str):
    norm = normalize_ascii_lower(text)
    raw_tokens = re.findall(r"\b[a-z0-9_]{3,}\b", norm)
    return [t for t in raw_tokens if t not in STOPWORDS_PT]


def sanitize_theory_snippet(text: str) -> str:
    t = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
    t = re.sub(r"[*_`#>-]", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


def extract_theory_statements(content: str):
    stmts = []
    cur_h2 = "Introdução Geral"
    cur_sec = "Fundamentos Teóricos"

    sections = re.split(r"(^#{2,4}\s+[^\n]+)", content, flags=re.M)
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
                        for h in ("característica", "conceito", "critério", "elemento", "item", "atributo", "aspecto", "parâmetro", "propriedade")
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

                clean_l = line.rstrip(".:;").strip()
                if len(clean_l) >= 30:
                    stmts.append({
                        "h2": cur_h2,
                        "sec": cur_sec,
                        "text": clean_l + ".",
                        "tokens": set(tokenize_pt(clean_l + " " + cur_sec)),
                    })

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
            "text": f"A doutrina e a sistematização técnica estabelecem os critérios exatos cobrados no item.",
        }

    if formato == "CERTO_ERRADO" or set(alts.keys()) == {"C", "E"}:
        st_main = pick_best_stmt(enun_tokens, enun_tokens, prefer_h2=target_h2)
        sec1 = st_main["sec"]
        txt1 = st_main["text"]
        txt1_low = txt1[0].lower() + txt1[1:] if len(txt1) > 1 else txt1
        enun_snip = summarize_option_snippet(enun_text, max_len=110)

        if gab == "C":
            return (
                f"> - **C)** **Correta.** O item está **Certo**. Conforme fundamentado na seção *{sec1}*, {txt1_low} "
                f"Dessa forma, está plenamente correta a assertiva da banca ({banca} – {orgao}/{ano}) ao afirmar que \"{enun_snip}\".\n"
                f"> - **E)** **Incorreta.** A assertiva não incorre em erro conceitual, guardando conformidade com a teoria estudada."
            )
        else:
            flaw_desc = detect_distractor_flaw(enun_text)
            return (
                f"> - **C)** **Incorreta.** A proposição {flaw_desc} ao afirmar que \"{enun_snip}\". "
                f"De acordo com a teoria em *{sec1}*, {txt1_low}\n"
                f"> - **E)** **Correta.** O item está **Errado** (gabarito oficial: **E**), pois contraria a disciplina teórica aplicável."
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


def format_question_markdown(num: str, q: dict, theory_stmts: list, target_h2: str, file_title: str) -> str:
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


NON_THEORY_REGEX = re.compile(
    r"\b(?:ementa|sumario|destaques pedagogicos|fontes recomendadas|fontes oficiais|referencias bibliograficas|recomendad[ao]s)\b"
)
MIN_CONTAIN_LEN = 8
OVERLAP_THRESHOLD = 0.34


def norm_title(text: str) -> str:
    """Normaliza: sem acentos, sem numeração inicial, sem pontuação/emoji, minúsculo."""
    t = normalize_ascii_lower(text)
    t = re.sub(r"^\s*\d+(\.\d+)*\.?\s*", "", t)
    t = re.sub(r"[^a-z0-9 ]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def parse_sections(content: str):
    """Retorna lista de seções '## ' com offsets e títulos de subseções '###'."""
    h2 = list(re.finditer(r"^##\s+([^\n]+)$", content, re.M))
    sections = []
    for i, m in enumerate(h2):
        end = h2[i + 1].start() if i + 1 < len(h2) else len(content)
        title = m.group(1).strip()
        body = content[m.end():end]
        heads = [title] + [h.strip() for h in re.findall(r"^###\s+([^\n]+)$", body, re.M)]
        norm_t = norm_title(title)
        is_theory = not bool(NON_THEORY_REGEX.search(norm_t))
        sections.append({
            "title": title,
            "start": m.start(),
            "end": end,
            "theory": is_theory,
            "heads": heads,
            "heads_norm": [norm_title(h) for h in heads],
            "tokens": set(tokenize_pt(" ".join(heads))),
        })
    return sections


def load_files():
    files = []
    for root, _, names in os.walk(DOCS_DIR):
        if os.path.abspath(root) == DOCS_DIR:
            continue
        for name in sorted(names):
            if not name.endswith(".md") or name == "README.md":
                continue
            full = os.path.join(root, name)
            rel = normalize_rel_path(full)
            if is_blacklisted(rel):
                continue
            with open(full, "r", encoding="utf-8") as f:
                content = f.read()
            if re.search(r"^### Teste \d+", content, re.M):
                print(f"[ERRO] {rel} ainda contém '### Teste'. Rode src/utils/scrubber.py antes.")
                sys.exit(1)
            parts = rel.split("/")
            sections = parse_sections(content)
            ementa = ""
            m = re.search(r"^##\s+[^\n]*Ementa[^\n]*\n(.*?)(?=^##\s)", content, re.M | re.S)
            if m:
                ementa = m.group(1)
            files.append({
                "rel": rel, "full": full, "content": content,
                "area_dir": parts[1] if len(parts) > 1 else "",
                "mod": parts[2] if len(parts) > 2 else "",
                "title": (re.search(r"^#\s+([^\n]+)", content, re.M) or [None, name])[1],
                "sections": sections,
                "ementa_tokens": set(tokenize_pt(ementa + " " + name.replace("_", " "))),
                "stmts": extract_theory_statements(content),
            })
    return files


def match_question(q, candidates):
    """Retorna (arquivo, seção, camada). Camadas: 1 exata, 2 contenção, 3 sobreposição, 4 fallback."""
    topico = norm_title(q.get("target_topico", ""))
    ttoks = set(tokenize_pt(q.get("target_topico", "")))

    # Camada 1: exata
    for f in candidates:
        for s in f["sections"]:
            if not s["theory"]:
                continue
            if topico and topico in s["heads_norm"]:
                return f, s, 1
    # Camada 2: contenção (tópico contido no cabeçalho ou vice-versa)
    if len(topico) >= MIN_CONTAIN_LEN:
        for f in candidates:
            for s in f["sections"]:
                if not s["theory"]:
                    continue
                for h in s["heads_norm"]:
                    if len(h) >= MIN_CONTAIN_LEN and (topico in h or h in topico):
                        return f, s, 2
    # Camada 3: sobreposição de tokens com cabeçalhos (+ ementa do arquivo como desempate)
    best = (0.0, None, None)
    if ttoks:
        qtoks = ttoks | set(tokenize_pt(q.get("enunciado", "")[:300]))
        for f in candidates:
            for s in f["sections"]:
                if not s["theory"] or not s["tokens"]:
                    continue
                t_cov = len(ttoks & s["tokens"]) / len(ttoks)
                s_cov = len(ttoks & s["tokens"]) / max(len(s["tokens"]), 1)
                q_cov = len(qtoks & s["tokens"]) / max(len(s["tokens"]), 1)
                score = max(t_cov, s_cov * 0.75) + 0.25 * q_cov + 0.10 * (len(ttoks & f["ementa_tokens"]) / len(ttoks))
                if score > best[0]:
                    best = (score, f, s)
        if best[0] >= OVERLAP_THRESHOLD:
            return best[1], best[2], 3
    # Camada 4: fallback — arquivo da matéria com maior afinidade; última seção teórica
    def file_aff(f):
        return len(ttoks & f["ementa_tokens"])
    f = max(candidates, key=file_aff)
    theory = [s for s in f["sections"] if s["theory"]]
    return f, (theory[-1] if theory else None), 4


def run_mass_injection(dry_run=False):
    if not os.path.exists(DB_FILE):
        print(f"[ERRO] Banco não encontrado: {DB_FILE}")
        sys.exit(1)
    with open(DB_FILE, "r", encoding="utf-8") as f:
        raw = json.load(f)

    seen, valid = set(), []
    for q in raw:
        if q.get("target_topico") in ("LIXO", "DESCARTADA", "", None):
            continue
        if q["id"] in seen:
            continue
        seen.add(q["id"])
        valid.append(q)
    print(f"[*] Questões válidas no JSON: {len(valid)}")

    files = load_files()
    by_mod = defaultdict(list)
    for f in files:
        by_mod[(f["area_dir"], f["mod"])].append(f)

    assign = defaultdict(lambda: defaultdict(list))  # rel -> section_start -> [q]
    layers, unmatched = Counter(), []
    for q in valid:
        key = (AREA_TO_DIR.get(q.get("target_area", ""), ""), MATERIA_TO_MODULE.get(q.get("target_materia", ""), ""))
        cands = by_mod.get(key, [])
        if not cands:
            unmatched.append((q["id"], q.get("target_materia"), q.get("target_topico"), "sem arquivo elegível"))
            continue
        f, s, layer = match_question(q, cands)
        if s is None:
            unmatched.append((q["id"], q.get("target_materia"), q.get("target_topico"), "sem seção teórica"))
            continue
        layers[layer] += 1
        assign[f["rel"]][s["start"]].append(q)

    injected, per_file = 0, {}
    for f in files:
        if f["rel"] not in assign:
            continue
        content = f["content"]
        out, cursor, num = [], 0, 1
        for s in sorted(f["sections"], key=lambda x: x["start"]):
            qs = assign[f["rel"]].get(s["start"])
            if not qs:
                continue
            out.append(content[cursor:s["end"]].rstrip() + "\n\n")
            for q in qs:
                out.append(format_question_markdown(f"{num:03d}", q, f["stmts"], s["title"], f["title"]))
                num += 1
                injected += 1
                q["status_integracao"] = "injetada"
            cursor = s["end"]
        out.append(content[cursor:])
        per_file[f["rel"]] = num - 1
        if not dry_run:
            with open(f["full"], "w", encoding="utf-8") as fh:
                fh.write("".join(out))

    if not dry_run:
        with open(DB_FILE, "w", encoding="utf-8") as fh:
            json.dump(raw, fh, ensure_ascii=False, indent=2)

    print(f"\n[{'DRY-RUN' if dry_run else 'OK'}] Injetadas: {injected} / {len(valid)} | arquivos: {len(per_file)}")
    print(f"  Camadas: exata={layers[1]} contenção={layers[2]} sobreposição={layers[3]} fallback={layers[4]}")
    print("  Top arquivos:")
    for rel, n in sorted(per_file.items(), key=lambda x: -x[1])[:8]:
        print(f"    {n:5d}  {rel}")
    print(f"  Sem correspondência: {len(unmatched)}")
    for u in unmatched[:50]:
        print("   -", u)


if __name__ == "__main__":
    run_mass_injection(dry_run="--dry-run" in sys.argv)
