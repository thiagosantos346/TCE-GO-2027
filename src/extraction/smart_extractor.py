#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
src/extraction/smart_extractor.py

SMART EXTRACTION V2 — Extrator Inteligente Ciente de Layout (Column-Aware)
Resistente a diagramação em múltiplas colunas (FGV, FCC, CEBRASPE, IBFC, VUNESP, CONSULPLAN, FUMARC, FAPERP).

Arquitetura V2:
1. Leitura Ciente de Layout (Column Awareness):
   - Extrai blocos visuais via PyMuPDF (fitz) e pdfplumber, ordenando-os respeitando bandas horizontais
     e colunas visuais (coluna da esquerda inteira de cima a baixo antes da coluna da direita).
2. Filtro Anti-Lixo (Header/Footer & Base-Text Stripping):
   - Remove cabeçalhos/rodapés repetitivos ("pciconcursos", "pcimarkpci", "Caderno de Prova", "Tipo 001",
     datas, códigos de barra, números de página) e trunca textos-base/passagens de interpretação ou títulos
     de seção que sucedem a última alternativa ou item.
3. Suporte Multi-Banca (Regex Inteligente + Programação Dinâmica de Sequência):
   - Padrão A-E / A-D (FCC/FGV/VUNESP/IBFC/CEBRASPE-ME): Identifica o enunciado e separa as alternativas
     (A)-(E), A)-E), a)-e) ou A..E em início de linha, usando programação dinâmica (LIS ponderada) para
     garantir a sequência numérica exata das questões sem ser enganado por números dentro de alternativas.
   - Padrão Certo/Errado (CEBRASPE/CESPE): Identifica blocos de itens para julgamento (sem opções A-E).
4. Cruzamento Preciso com Gabarito (Multi-Cargo / Multi-Tipo Aware):
   - Pareia cada PDF de prova com seu gabarito correspondente e localiza a tabela/seção exata do cargo,
     caderno e tipo de prova (com suporte a blocos visuais ordenados e fallback tabular via pdfplumber).
5. Sanitização Nativa:
   - Descarta silenciosamente questões anuladas, dependentes de imagens/figuras/tabelas gráficas,
     legislação revogada (Lei 8.666/93, Lei 10.520/02, RDC) e matérias fora de escopo.
"""

import io
import json
import math
import os
import re
import unicodedata
from collections import Counter

import pdfplumber
import pymupdf as fitz

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PROVAS_DIR = os.path.join(BASE_DIR, "raw_provas")
DOCS_DIR = os.path.join(BASE_DIR, "docs")
OUTPUT_JSON = os.path.join(BASE_DIR, "data", "banco_questoes_v2.json")

# ==============================================================================
# STOPWORDS E NORMALIZAÇÃO PARA INDEXAÇÃO SEMÂNTICA BM25 (DOCS/)
# ==============================================================================
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
    "outro", "outra", "outros", "outras", "qualquer", "quaisquer", "tanto", "quanto",
    "pode", "podem", "deve", "devem", "sendo", "feito", "feita", "forma", "modo",
    "caso", "casos", "parte", "partes", "meio", "meios", "tipo", "tipos", "uso",
}

DISCIPLINE_HINT_RULES = [
    (
        r"\b(?:python|pandas|numpy|scikit|sql|postgre|oracle|mysql|nosql|mongodb|redis|"
        r"docker|kubernetes|git|gitlab|jenkins|scrum|kanban|xp|pmbok|cobit|itil|togaf|"
        r"owasp|oauth|jwt|saml|ldap|kerberos|firewall|ids|ips|siem|vlan|ospf|bgp|tcp|"
        r"udp|ipv4|ipv6|dns|dhcp|http|https|rest|soap|graphql|json|xml|html|css|react|"
        r"angular|vue|node|java|spring|hibernate|uml|bpmn|data\s+warehouse|data\s+lake|"
        r"etl|olap|spark|hadoop|kafka|airflow|power\s+bi|tableau|lgpd|criptografia|"
        r"chave\s+p[úu]blica|hash|assinatura\s+digital|certificado\s+digital|backup|"
        r"raid|san|nas|virtualiza[çc][ãa]o|vmware|hyper-v|cloud|aws|azure|gcp|iaas|"
        r"paas|saas|devops|ci/cd|microsservi[çc]os|api|active\s+directory|windows\s+server|"
        r"linux|bash|shell|arvore\s+b|grafo|pilha|fila|orienta[çc][ãa]o\s+a\s+objetos|"
        r"polimorfismo|heran[çc]a|encapsulamento|normaliza[çc][ãa]o|formas?\s+normais|"
        r"acid|trigger|stored\s+procedure|view|indice|chave\s+prim[áa]ria|chave\s+estrangeira|"
        r"aprendizado\s+de\s+m[áa]quina|machine\s+learning|deep\s+learning|rede\s+neural|"
        r"regress[ãa]o|classifica[çc][ãa]o|clusteriza[çc][ãa]o|k-means|random\s+forest|"
        r"svm|overfitting|underfitting|bpmn|babok|pontos?\s+de\s+fun[çc][ãa]o|ifpug|"
        r"iso\s*27001|iso\s*27002|iso\s*27005|nist|engenharia\s+de\s+software|"
        r"banco\s+de\s+dados|seguran[çc]a\s+da\s+informa[çc][ãa]o|redes\s+de\s+computadores)\b",
        {
            "1-arquitetura-de-software",
            "2-engenharia-de-software",
            "3-bancos-de-dados",
            "4-seguranca-da-informacao",
            "5-redes-e-infraestrutura",
            "6-governanca-e-gestao-de-ti",
            "7-ciencia-de-dados-e-ia",
        },
        1.45,
    ),
    (
        r"\b(?:constitui[çc][ãa]o\s+federal|direitos?\s+fundamentais|rem[ée]dios?\s+constitucionais|"
        r"habeas\s+corpus|mandado\s+de\s+seguran[çc]a|mandado\s+de\s+injun[çc][ãa]o|habeas\s+data|"
        r"a[çc][ãa]o\s+popular|controle\s+de\s+constitucionalidade|adi|adc|adpf|stf|stj|cnj|"
        r"poder\s+constituinte|reparti[çc][ãa]o\s+de\s+compet[êe]ncias|processo\s+legislativo|"
        r"medida\s+provis[óo]ria|emenda\s+constitucional|interven[çc][ãa]o\s+federal)\b",
        {"direito-constitucional"},
        1.45,
    ),
    (
        r"\b(?:ato\s+administrativo|atos\s+administrativos|poderes?\s+administrativos|"
        r"poder\s+de\s+pol[íi]cia|poder\s+disciplinar|poder\s+hier[áa]rquico|poder\s+regulamentar|"
        r"improbidade\s+administrativa|lei\s+8\.?429|lei\s+14\.?230|lei\s+14\.?133|"
        r"licita[çc][ãa]o|licita[çc][õo]es|preg[ãa]o|concorr[êe]ncia|dispensa\s+de\s+licita[çc][ãa]o|"
        r"inexigibilidade|contrato\s+administrativo|servi[çc]o\s+p[úu]blico|concess[ãa]o|"
        r"permiss[ãa]o|autarquia|funda[çc][ãa]o\s+p[úu]blica|empresa\s+p[úu]blica|"
        r"sociedade\s+de\s+economia\s+mista|ag[êe]ncia\s+reguladora|responsabilidade\s+civil\s+do\s+estado|"
        r"bens\s+p[úu]blicos|interven[çc][ãa]o\s+do\s+estado\s+na\s+propriedade|desapropria[çc][ãa]o|"
        r"tombamento|requisi[çc][ãa]o\s+administrativa|servid[ãa]o\s+administrativa|"
        r"processo\s+administrativo|lei\s+9\.?784|agentes?\s+p[úu]blicos|lei\s+8\.?112)\b",
        {"direito-administrativo"},
        1.45,
    ),
    (
        r"\b(?:or[çc]amento\s+p[úu]blico|ppa|ldo|loa|plano\s+plurianual|diretrizes\s+or[çc]ament[áa]rias|"
        r"cr[ée]ditos?\s+adicionais|suplementar|especial|extraordin[áa]rio|restos\s+a\s+pagar|"
        r"despesas?\s+de\s+exerc[íi]cios\s+anteriores|suprimento\s+de\s+fundos|empenho|liquida[çc][ãa]o|"
        r"receita\s+corrente\s+l[íi]quida|lei\s+de\s+responsabilidade\s+fiscal|lrf|"
        r"lei\s+complementar\s+101|lei\s+4\.?320|princ[íi]pios?\s+or[çc]ament[áa]rios|"
        r"ciclo\s+or[çc]ament[áa]rio|d[íi]vida\s+ativa|d[íi]vida\s+p[úu]blica|ren[úu]ncia\s+de\s+receita)\b",
        {"direito-financeiro", "administracao-financeira-e-orcamentaria-afo"},
        1.45,
    ),
    (
        r"\b(?:controle\s+externo|tribunal\s+de\s+contas|tcu|tce|tomada\s+de\s+contas\s+especial|"
        r"julgamento\s+de\s+contas|aprecia[çc][ãa]o\s+de\s+contas|parecer\s+pr[ée]vio|"
        r"sustar\s+ato|sustar\s+contrato|auditoria\s+governamental|nbasp|issai|intosai|"
        r"achados?\s+de\s+auditoria|evid[êe]ncia\s+de\s+auditoria|risco\s+de\s+auditoria|"
        r"matriz\s+de\s+planejamento|matriz\s+de\s+achados|matriz\s+de\s+responsabiliza[çc][ãa]o|"
        r"auditoria\s+operacional|auditoria\s+de\s+conformidade|auditoria\s+financeira)\b",
        {"controle-externo", "auditoria-governamental"},
        1.45,
    ),
    (
        r"\b(?:crase|concord[âa]ncia\s+verbal|concord[âa]ncia\s+nominal|reg[êe]ncia\s+verbal|"
        r"reg[êe]ncia\s+nominal|coloca[çc][ãa]o\s+pronominal|pr[óo]clise|[êe]nclise|mes[óo]clise|"
        r"ora[çc][ãa]o\s+subordinada|ora[çc][ãa]o\s+coordenada|sujeito|predicado|objeto\s+direto|"
        r"objeto\s+indireto|adjunto\s+adnominal|adjunto\s+adverbial|complemento\s+nominal|"
        r"aposto|vocativo|voz\s+passiva|voz\s+ativa|part[íi]cula\s+apassivadora|"
        r"[íi]ndice\s+de\s+indetermina[çc][ãa]o|pontua[çc][ãa]o|v[íi]rgula|acentua[çc][ãa]o\s+gr[áa]fica|"
        r"ortografia|h[íi]fen|coes[ãa]o|coer[êe]ncia|tipologia\s+textual|g[êe]nero\s+textual|"
        r"reescrita|sentido\s+original|corre[çc][ãa]o\s+gramatical| Manual\s+de\s+Reda[çc][ãa]o)\b",
        {"lingua-portuguesa"},
        1.5,
    ),
    (
        r"\b(?:proposi[çc][ãa]o|tautologia|contradi[çc][ãa]o|conting[êe]ncia|tabela-verdade|"
        r"equival[êe]ncia\s+l[óo]gica|nega[çc][ãa]o\s+da\s+proposi[çc][ãa]o| leyes?\s+de\s+de\s+morgan|"
        r"silogismo|argumento\s+v[áa]lido|quantificadores?\s+l[óo]gicos|arranjo|combina[çc][ãa]o|"
        r"permuta[çc][ãa]o|an[áa]lise\s+combinat[óo]ria|juros\s+simples|juros\s+compostos|"
        r"taxa\s+interna\s+de\s+retorno|valor\s+presente\s+l[íi]quido|sistema\s+price|"
        r"sistema\s+sac|amortiza[çc][ãa]o|desconto\s+racional|desconto\s+comercial|"
        r"taxa\s+efetiva|taxa\s+nominal|progress[ãa]o\s+aritm[ée]tica|progress[ãa]o\s+geom[ée]trica)\b",
        {"raciocinio-logico-e-matematico", "matematica-financeira"},
        1.5,
    ),
    (
        r"\b(?:m[ée]dia\s+aritm[ée]tica|mediana|moda|vari[âa]ncia|desvio\s+padr[ãa]o|"
        r"coeficiente\s+de\s+varia[çc][ãa]o|distribui[çc][ãa]o\s+normal|distribui[çc][ãa]o\s+binomial|"
        r"distribui[çc][ãa]o\s+de\s+poisson|teste\s+de\s+hip[óo]tese|p-valor|erro\s+tipo\s+i|"
        r"erro\s+tipo\s+ii|intervalo\s+de\s+confian[çc]a|amostragem\s+aleat[óo]ria|"
        r"amostragem\s+estratificada|correla[çc][ãa]o\s+de\s+pearson|anova|qui-quadrado|"
        r"teorema\s+de\s+bayes|probabilidade\s+condicional|vari[áa]vel\s+aleat[óo]ria|"
        r"esperan[çc]a\s+matem[áa]tica)\b",
        {"estatistica"},
        1.5,
    ),
]


def open_pdf_fitz(path):
    """Abre um PDF no PyMuPDF suportando caminhos longos no Windows (>260 chars)."""
    ap = os.path.abspath(path)
    if os.name == "nt" and not ap.startswith("\\\\?\\"):
        ap = "\\\\?\\" + ap
    with open(ap, "rb") as fp:
        return fitz.open(stream=fp.read(), filetype="pdf")


def open_pdf_plumber(path):
    """Abre um PDF no pdfplumber suportando caminhos longos no Windows (>260 chars)."""
    ap = os.path.abspath(path)
    if os.name == "nt" and not ap.startswith("\\\\?\\"):
        ap = "\\\\?\\" + ap
    with open(ap, "rb") as fp:
        return pdfplumber.open(io.BytesIO(fp.read()))


def normalize_text(s):
    if not s:
        return ""
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-zA-Z0-9]+", " ", s).lower().strip()


def tokenize_pt(text):
    norm = normalize_text(text)
    return [t for t in norm.split() if len(t) > 2 and t not in STOPWORDS_PT]


# ==============================================================================
# INDEXADOR SEMÂNTICO BM25 SOBRE OS GUIAS DE ESTUDO (docs/)
# ==============================================================================
class SemanticTopicIndex:
    def __init__(self, docs_dir):
        self.docs = []
        self.df = Counter()
        self.avgdl = 0.0
        self._build_index(docs_dir)

    def _build_index(self, docs_dir):
        for root, _, files in os.walk(docs_dir):
            for f in sorted(files):
                if not f.endswith(".md") or f in ("index.md", "README.md"):
                    continue
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(full_path, BASE_DIR).replace("\\", "/")
                parts = rel_path.split("/")
                disc_folder = parts[2] if len(parts) > 3 else ""

                try:
                    with open(full_path, "r", encoding="utf-8") as fp:
                        content = fp.read()
                except Exception:
                    continue

                h1_m = re.search(r"^#\s+(.+)$", content, re.M)
                h1_title = h1_m.group(1).strip() if h1_m else f.replace(".md", "")
                h2_list = re.findall(r"^##\s+(.+)$", content, re.M)
                h2_clean = [
                    h.strip()
                    for h in h2_list
                    if not re.search(r"quest[õo]es|exerc[íi]cios|refer[êe]ncias|resumo", h, re.I)
                ]
                target_section = h2_clean[0] if h2_clean else h1_title

                title_tokens = tokenize_pt(h1_title + " " + " ".join(h2_clean) + " " + f.replace("-", " "))
                body_tokens = tokenize_pt(content[:25000])
                all_tokens = title_tokens * 4 + body_tokens
                tf = Counter(all_tokens)
                dl = len(all_tokens)

                for term in tf.keys():
                    self.df[term] += 1

                self.docs.append(
                    {
                        "rel_path": rel_path,
                        "disc_folder": disc_folder,
                        "target_section": f"## {target_section}" if not target_section.startswith("#") else target_section,
                        "tf": tf,
                        "dl": dl,
                    }
                )

        if self.docs:
            self.avgdl = sum(d["dl"] for d in self.docs) / len(self.docs)

    def match(self, question_text):
        q_tokens = tokenize_pt(question_text)
        if not q_tokens or not self.docs:
            return "docs/geral/conhecimentos-gerais/lingua-portuguesa/1-compreensao-e-interpretacao.md", "## 1. Compreensão e Interpretação de Textos", 1.0

        boosted_folders = set()
        boost_factor = 1.0
        for pattern, folders, factor in DISCIPLINE_HINT_RULES:
            if re.search(pattern, question_text, re.I):
                boosted_folders.update(folders)
                boost_factor = max(boost_factor, factor)

        N = len(self.docs)
        k1 = 1.5
        b = 0.75
        best_doc = self.docs[0]
        best_score = -1.0

        for doc in self.docs:
            score = 0.0
            dl = doc["dl"]
            tf_map = doc["tf"]
            for qt in q_tokens:
                f_val = tf_map.get(qt, 0)
                if f_val == 0:
                    continue
                df_val = self.df.get(qt, 0)
                idf = math.log(1.0 + (N - df_val + 0.5) / (df_val + 0.5))
                denom = f_val + k1 * (1.0 - b + b * (dl / max(self.avgdl, 1.0)))
                score += idf * ((f_val * (k1 + 1.0)) / denom)

            if doc["disc_folder"] in boosted_folders:
                score *= boost_factor

            if score > best_score:
                best_score = score
                best_doc = doc

        return best_doc["rel_path"], best_doc["target_section"], round(best_score, 2)


# ==============================================================================
# EXTRAÇÃO DE METADADOS DA PROVA A PARTIR DO NOME DO ARQUIVO
# ==============================================================================
def extract_metadata_from_slug(pv_filename):
    slug = pv_filename.split("___")[0] if "___" in pv_filename else pv_filename.replace(".pdf", "")
    slug_norm = slug.lower().replace("_", "-")

    # Ano
    m_year = re.search(r"\b(20\d{2})\b", slug_norm)
    ano = int(m_year.group(1)) if m_year else 2024

    # Banca
    if "cebraspe" in slug_norm or "cespe" in slug_norm:
        banca = "CEBRASPE"
    elif "fgv" in slug_norm:
        banca = "FGV"
    elif "fcc" in slug_norm:
        banca = "FCC"
    elif "vunesp" in slug_norm:
        banca = "VUNESP"
    elif "ibfc" in slug_norm:
        banca = "IBFC"
    elif "consulplan" in slug_norm:
        banca = "CONSULPLAN"
    elif "fumarc" in slug_norm:
        banca = "FUMARC"
    elif "faperp" in slug_norm:
        banca = "FAPERP"
    else:
        banca = "OUTRA"

    # Órgão
    orgao = "ÓRGÃO PÚBLICO"
    m_org = re.search(
        r"\b(tce-[a-z]{2}|tcu|tj-[a-z]{2,3}|tjm-[a-z]{2}|trf-(?:da-\d+-regiao|\d+)|trt-(?:da-\d+-regiao|\d+)|stf|stj|cnj|mpu|cgu)\b",
        slug_norm,
    )
    if m_org:
        raw_org = m_org.group(1).upper()
        raw_org = re.sub(r"^(TRF|TRT)-DA-(\d+)-REGIAO$", r"\1-\2", raw_org)
        orgao = raw_org

    # Cargo limpo
    cargo_part = slug_norm
    cargo_part = re.sub(r"-(?:fgv|fcc|cebraspe|cespe|ibfc|fumarc|faperp|instituto-consulplan|vunesp)-20\d{2}.*$", "", cargo_part)
    cargo_part = re.sub(r"-(?:tce-[a-z]{2}|tcu|tj-[a-z]{2,3}|tjm-[a-z]{2}|trf-(?:da-\d+-regiao|\d+)|trt-(?:da-\d+-regiao|\d+)|stf|stj|cnj|mpu|cgu)$", "", cargo_part)
    cargo_title = cargo_part.replace("-", " ").strip().title()
    cargo_title = re.sub(r"\bTi\b", "TI", cargo_title)
    cargo_title = re.sub(r"\bDe\b", "de", cargo_title)
    cargo_title = re.sub(r"\bDa\b", "da", cargo_title)
    cargo_title = re.sub(r"\bDo\b", "do", cargo_title)
    cargo_title = re.sub(r"\bE\b", "e", cargo_title)

    return {
        "banca": banca,
        "ano": ano,
        "orgao": orgao,
        "cargo": cargo_title or "Analista / Auditor",
        "prova_slug": slug,
    }


def extract_cargo_tokens_from_slug(pv_filename):
    slug = pv_filename.split("___")[0] if "___" in pv_filename else pv_filename.replace(".pdf", "")
    slug_l = slug.lower().replace("_", "-")
    slug_l = re.sub(r"-(?:fgv|fcc|cebraspe|cespe|ibfc|fumarc|faperp|instituto-consulplan|vunesp)-20\d{2}.*$", "", slug_l)
    slug_l = re.sub(r"-(?:tce-[a-z]{2}|tj-[a-z]{2,3}|tjm-[a-z]{2}|trf-(?:da-\d+-regiao|\d+)|trt-(?:da-\d+-regiao|\d+)|stf|stj)$", "", slug_l)
    stop = {"de", "da", "do", "das", "dos", "e", "em", "area", "apoio", "especializado", "especialidade", "grupo", "classe", "c"}
    return [t for t in slug_l.split("-") if t and t not in stop]


# ==============================================================================
# PAREAMENTO E EXTRAÇÃO DE GABARITOS (MULTI-CARGO E MULTI-CADERNO AWARE)
# ==============================================================================
def pair_files(provas_dir):
    files = [f for f in sorted(os.listdir(provas_dir)) if f.endswith(".pdf") and not f.startswith("edital")]
    provas = []
    gabaritos = []
    for f in files:
        f_l = f.lower()
        if "copy" in f_l or "padraoresposta" in f_l or "discursiva" in f_l:
            continue
        if "gab" in f_l:
            gabaritos.append(f)
        else:
            provas.append(f)

    pairs = []
    for pv in provas:
        pv_clean = pv.replace(".pdf", "")
        matched_gab = None
        if "___" in pv:
            slug, pv_rest = pv.split("___", 1)
            cand_gabs = [g for g in gabaritos if g.startswith(slug + "___")]
            if len(cand_gabs) == 1:
                matched_gab = cand_gabs[0]
            elif len(cand_gabs) > 1:
                pv_rest_l = pv_rest.lower()
                for g in cand_gabs:
                    g_rest_l = g.split("___", 1)[1].lower()
                    if ("basic" in pv_rest_l and "basic" in g_rest_l) or ("espec" in pv_rest_l and "espec" in g_rest_l):
                        matched_gab = g
                        break
                    codes = re.findall(r"\d+_\d+", pv_rest_l)
                    if codes and any(c in g_rest_l for c in codes):
                        matched_gab = g
                        break
                if not matched_gab:
                    matched_gab = cand_gabs[0]
        else:
            for g in gabaritos:
                if "___" not in g and g.startswith(pv_clean) and "gab" in g:
                    matched_gab = g
                    break
        if matched_gab:
            pairs.append((pv, matched_gab))
    return pairs


def parse_answers_from_blocks(blocks, raw_text=""):
    res = {}
    if not raw_text:
        raw_text = "\n".join(b[4] for b in blocks if "pcimarkpci" not in b[4] and "pciconcursos" not in b[4])

    # 1. Padrão FCC: "001 - B" ou "1 - B"
    p_fcc = re.findall(r"(?m)^\s*0*([1-9]\d{0,2})\s*[-–—\.]\s*([A-E]|ANULAD[AO]|X|N|\*|\#)\b", raw_text, re.I)
    if len(p_fcc) >= 15:
        for q, g in p_fcc:
            q_num = int(q)
            g_val = g.upper()
            res[q_num] = "ANULADA" if (g_val in ("X", "N", "*", "#") or g_val.startswith("ANUL")) else g_val
        return res

    tokens = []
    source_lines = (
        raw_text.split("\n")
        if not blocks
        else [l for b in blocks if "pcimarkpci" not in b[4] and "pciconcursos" not in b[4] for l in b[4].split("\n")]
    )
    for line in source_lines:
        ls = line.strip()
        if not ls:
            continue
        if re.search(
            r"(?:EDITAL|CONCURSO|TRIBUNAL|P[ÁA]GINA|APLICA[ÇC][ÃA]O|CARGO\s+\d|CADERNO\s+\d|IBFC_\d|TIPO\s+\d|PROVA\s*[–-]\s*TIPO|\d{2}/\d{2}/\d{4}|CARGO/ESPECIALIDADE)",
            ls,
            re.I,
        ):
            continue
        for tok in ls.split():
            t_clean = tok.strip(".,:;()[]")
            if t_clean == "0":
                continue
            tokens.append(t_clean)

    VALID_ANS = {"A", "B", "C", "D", "E", "X", "*", "#", "N", "ANULADA", "ANULADO"}
    i = 0
    while i < len(tokens):
        if tokens[i].isdigit() and 1 <= int(tokens[i]) <= 150:
            nums = [int(tokens[i])]
            j = i + 1
            while j < len(tokens) and tokens[j].isdigit() and int(tokens[j]) == nums[-1] + 1:
                nums.append(int(tokens[j]))
                j += 1
            if len(nums) >= 2:
                k = len(nums)
                ans_list = []
                m = j
                while m < len(tokens) and len(ans_list) < k:
                    tu = tokens[m].upper()
                    if tu in VALID_ANS:
                        ans_list.append(tu)
                    elif tu.isdigit() and int(tu) == nums[-1] + 1:
                        break
                    m += 1
                if len(ans_list) == k:
                    for n_val, a_val in zip(nums, ans_list):
                        res[n_val] = "ANULADA" if (a_val in ("X", "*", "#", "N") or a_val.startswith("ANUL")) else a_val
                    i = m
                    continue
        i += 1

    if len(res) >= 15:
        return res

    # Pares alternados ("01 B 13 D 25 C...")
    i = 0
    while i < len(tokens) - 1:
        if tokens[i].isdigit() and 1 <= int(tokens[i]) <= 150:
            q_num = int(tokens[i])
            tu = tokens[i + 1].upper()
            if tu in VALID_ANS:
                res[q_num] = "ANULADA" if (tu in ("X", "*", "#", "N") or tu.startswith("ANUL")) else tu
                i += 2
                continue
        i += 1

    return res


def cebra_cg_matches_cargo(header_norm, cargo_num):
    if not cargo_num:
        return True
    nums_in_header = set()
    for m in re.finditer(r"\b(\d{1,2})\s+a\s+(\d{1,2})\b", header_norm):
        a, b = int(m.group(1)), int(m.group(2))
        if 1 <= a <= b <= 50:
            nums_in_header.update(range(a, b + 1))
    for m in re.finditer(r"\b(\d{1,2})\b", header_norm):
        n = int(m.group(1))
        if 1 <= n <= 50:
            nums_in_header.add(n)
    return cargo_num in nums_in_header


def get_answer_key_for_pair(pv_path, gab_path):
    pv_name = os.path.basename(pv_path)
    doc_pv = open_pdf_fitz(pv_path)
    doc_gab = open_pdf_fitz(gab_path)

    pv_head_text = "\n".join(doc_pv[i].get_text("text") for i in range(min(3, len(doc_pv))))
    cebra_code = None
    m_cb = re.search(r"\|\|([A-Za-z0-9_]+?)N\d+\|\|", pv_head_text)
    if m_cb:
        cebra_code = m_cb.group(1)

    ibfc_code = None
    m_ibfc = re.search(r"\b(IBFC_\d+)\b", pv_head_text)
    if m_ibfc:
        ibfc_code = m_ibfc.group(1)

    fcc_code = None
    m_fcc = re.search(r"prova_([a-z]\d{2})_tipo", pv_name.lower())
    if m_fcc:
        fcc_code = m_fcc.group(1).upper()
    else:
        m_fcc2 = re.search(r"Caderno de Prova\s*['’]([A-Z0-9]{2,3})['’]", pv_head_text)
        if m_fcc2:
            fcc_code = m_fcc2.group(1).upper()

    cargo_tokens = extract_cargo_tokens_from_slug(pv_name)

    sorted_page_texts = []
    for p in doc_gab:
        bks = sorted(p.get_text("blocks"), key=lambda b: (round(b[1] / 5), b[0]))
        sorted_page_texts.append("\n".join(b[4] for b in bks if "pcimarkpci" not in b[4] and "pciconcursos" not in b[4]))
    full_gab_text = "\n".join(sorted_page_texts)

    # 1. FCC multi-section gabarito ("Cargo ou opção")
    if re.search(r"Cargo ou op[çc][ãa]o", full_gab_text, re.I):
        sections = re.split(r"(?=Cargo ou op[çc][ãa]o)", full_gab_text, flags=re.I)
        best_sec = None
        best_score = -999
        for sec in sections:
            if not re.search(r"Cargo ou op", sec, re.I):
                continue
            ans_cand = parse_answers_from_blocks([], sec)
            if len(ans_cand) < 15:
                continue
            first_lines = "\n".join(sec.split("\n")[:8])
            fl_norm = normalize_text(first_lines)
            score = 0
            if re.search(r"Tipo gabarito\s*[2345]", first_lines, re.I):
                score -= 500
            if fcc_code and re.search(r"\b" + re.escape(fcc_code.lower()) + r"\b", fl_norm):
                score += 1000
            for ct in cargo_tokens:
                if ct in fl_norm or ct[:5] in fl_norm:
                    score += 20
            if score > best_score:
                best_score = score
                best_sec = sec
        if best_sec:
            return parse_answers_from_blocks([], best_sec)

    # 2. Consulplan multi-section gabarito ("CARGO/ESPECIALIDADE:")
    if "CARGO/ESPECIALIDADE:" in full_gab_text:
        sections = re.split(r"(?=CARGO/ESPECIALIDADE:)", full_gab_text)
        best_sec = None
        best_score = -999
        for sec in sections:
            if "CARGO/ESPECIALIDADE:" not in sec:
                continue
            first_lines = "\n".join(sec.split("\n")[:5])
            fl_norm = normalize_text(first_lines)
            score = 0
            if "tipo 1" in fl_norm or "branca" in fl_norm:
                score += 50
            elif any(x in fl_norm for x in ["tipo 2", "tipo 3", "tipo 4", "verde", "amarela", "azul"]):
                score -= 500
            for ct in cargo_tokens:
                if ct in fl_norm:
                    score += 20
            if score > best_score:
                best_score = score
                best_sec = sec
        if best_sec:
            return parse_answers_from_blocks([], best_sec)

    # 3. Page-by-page scoring (FGV, Cebraspe, IBFC, FUMARC, FAPERP)
    best_page_idx = 0
    best_score = -9999
    page_infos = []

    for p_idx, page in enumerate(doc_gab):
        blocks = sorted(page.get_text("blocks"), key=lambda b: (round(b[1] / 5), b[0]))
        p_text = "\n".join(b[4] for b in blocks if "pcimarkpci" not in b[4] and "pciconcursos" not in b[4])
        header_lines = []
        for l in p_text.split("\n"):
            ls = l.strip()
            if not ls or ls == "0":
                continue
            if re.match(r"^\d+\s+\d+\s+\d+", ls) or re.match(r"^0*[1-9]\d?\s+[A-EX\*\#]$", ls):
                break
            header_lines.append(ls)
        header_str = " ".join(header_lines[:12])
        h_norm = normalize_text(header_str)
        p_norm = normalize_text(p_text)

        ans_map = parse_answers_from_blocks(blocks, p_text)
        page_infos.append((p_idx, h_norm, p_norm, ans_map, header_str))

        if len(ans_map) < 10:
            continue

        score = 0
        if "discursiva" in h_norm or "padrao de resposta" in h_norm:
            score -= 2000
        if re.search(r"\btipo\s*[2345]\b|\btipo\s*(?:verde|amarela|azul)\b|\bprova\s*[bcde]\b", h_norm):
            score -= 1000
        if re.search(r"\btipo\s*0?1\b|\btipo\s*branca\b|\btipo\s*a\b", h_norm):
            score += 30

        if cebra_code and cebra_code.lower() in p_norm:
            score += 2000
        if ibfc_code and ibfc_code.lower() in p_norm:
            score += 2000

        matched_tokens = sum(1 for ct in cargo_tokens if re.search(r"\b" + re.escape(ct) + r"\b", h_norm))
        score += matched_tokens * 25

        distractor_words = [
            "contabeis", "contabilidade", "direito", "juridica", "engenharia", "civil", "eletrica", "mecanica",
            "sanitaria", "economia", "atuariais", "estatistica", "enfermagem", "medicina", "odontologia",
            "psicologia", "servico", "social", "arquitetura", "arquivologia", "biblioteconomia", "policia",
            "telecomunicacoes", "telecomunicacao", "banco", "desenvolvimento", "seguranca", "suporte",
            "infraestrutura", "governanca", "negocios", "projetos", "dados",
        ]
        for dw in distractor_words:
            if dw not in cargo_tokens and re.search(r"\b" + dw + r"\b", h_norm):
                score -= 40

        if "analista" in cargo_tokens and "tecnico judiciario" in h_norm and "analista" not in h_norm:
            score -= 200
        if "tecnico" in cargo_tokens and "analista judiciario" in h_norm and "tecnico" not in h_norm:
            score -= 200

        if score > best_score:
            best_score = score
            best_page_idx = p_idx

    chosen_idx, chosen_h, chosen_p, chosen_ans, _ = page_infos[best_page_idx]
    final_ans = dict(chosen_ans)

    # Fallback para pdfplumber.extract_tables() caso o mapa da página esteja vazio
    if not final_ans:
        try:
            with open_pdf_plumber(gab_path) as pl_pdf:
                pl_page = pl_pdf.pages[best_page_idx]
                tables = pl_page.extract_tables() or []
                table_text = "\n".join(
                    " ".join(str(cell or "").strip() for cell in row)
                    for tbl in tables
                    for row in tbl
                )
                final_ans = parse_answers_from_blocks([], table_text)
        except Exception:
            pass

    # Cebraspe: se a página escolhida só possui Conhecimentos Específicos (ex: itens 51..120),
    # complementar com a página de Conhecimentos Básicos/Gerais (itens 1..50) do respectivo cargo.
    if final_ans and min(final_ans.keys()) > 15:
        need_max = min(final_ans.keys()) - 1
        m_cnum = re.search(r"\bcargo\s*(\d{1,2})\b", chosen_h)
        cargo_num = int(m_cnum.group(1)) if m_cnum else None
        best_cg = None
        for _, h_norm, p_norm, ans_map, _ in page_infos:
            if ans_map and min(ans_map.keys()) == 1 and max(ans_map.keys()) == need_max:
                if "conhecimentos" in p_norm or cebra_cg_matches_cargo(h_norm, cargo_num):
                    if cebra_cg_matches_cargo(h_norm, cargo_num):
                        best_cg = ans_map
                        break
                    elif best_cg is None:
                        best_cg = ans_map
        if best_cg:
            for k, v in best_cg.items():
                final_ans.setdefault(k, v)

    return final_ans


# ==============================================================================
# FILTROS ANTI-LIXO, LEITURA CIENTE DE COLUNAS E SANITIZAÇÃO NATIVA
# ==============================================================================
HEADER_FOOTER_LINE_RE = re.compile(
    r"(?:"
    r"^pcimarkpci\b|"
    r"www\.pciconcursos\.com\.br|"
    r"^\|\|.*\|\|$|"
    r"^CESPE\s*\|?\s*CEBRASPE\s*[–\-]|"
    r"^CEBRASPE\s*[–\|]\s*.*Edital:|"
    r"^UnB/CESPE\s*[–\-]|"
    r"^Caderno de Prova\b|"
    r"^\s*P[áa]gina\s+\d+\s+de\s+\d+\s*$|"
    r"\bTIPO\s+(?:BRANCA|VERDE|AMARELA|AZUL|001|01|1)\s*[–\-]\s*P[ÁA]GINA\s*\d+|"
    r"^IBFC_\d+\s*$|"
    r"^FAPERP\s*$|"
    r"^--\s*(?:PROVAS?\s+OBJETIVAS?|CONHECIMENTOS\s+(?:GERAIS|ESPEC[ÍI]FICOS|B[ÁA]SICOS)|PROVA\s+DISCURSIVA)\s*--$"
    r")",
    re.I,
)

SECTION_HEADER_BLOCK_RE = re.compile(
    r"^\s*(?:"
    r"CONHECIMENTOS\s+(?:GERAIS|ESPEC[ÍI]FICOS|B[ÁA]SICOS)(?:\s+[I123V]+)?|"
    r"L[ÍI]NGUA\s+PORTUGUESA|"
    r"RACIOC[ÍI]NIO\s+L[ÓO]GICO(?:\s*[-E]\s*MATEM[ÁA]TICO)?|"
    r"NO[ÇC][ÕO]ES\s+DE\s+(?:INFORM[ÁA]TICA|DIREITO|ESTAT[ÍI]STICA|ADMINISTRA[ÇC][ÃA]O|SUSTENTABILIDADE|DIREITOS\s+DAS\s+PESSOAS\s+COM\s+DEFICI[ÊE]NCIA)|"
    r"DIREITO\s+(?:CONSTITUCIONAL|ADMINISTRATIVO|CIVIL|PENAL|PROCESSUAL|TRIBUT[ÁA]RIO|PREVIDENCI[ÁA]RIO|EMPRESARIAL|DO\s+TRABALHO)|"
    r"TECNOLOGIA\s+DA\s+INFORMA[ÇC][ÃA]O|"
    r"ENGENHARIA\s+DE\s+SOFTWARE|"
    r"BANCO\s+DE\s+DADOS|"
    r"SEGURAN[ÇC]A\s+DA\s+INFORMA[ÇC][ÃA]O|"
    r"REDES\s+DE\s+COMPUTADORES|"
    r"GOVERNAN[ÇC]A\s+DE\s+TI|"
    r"CONTROLE\s+EXTERNO|"
    r"AUDITORIA\s+GOVERNAMENTAL|"
    r"ADMINISTRA[ÇC][ÃA]O\s+(?:P[ÚU]BLICA|GERAL|FINANCEIRA\s+E\s+OR[ÇC]AMENT[ÁA]RIA)|"
    r"MATEM[ÁA]TICA\s+FINANCEIRA|"
    r"ESTAT[ÍI]STICA|"
    r"CI[ÊE]NCIA\s+DE\s+DADOS|"
    r"CONTABILIDADE\s+(?:GERAL|P[ÚU]BLICA)|"
    r"ECONOMIA|"
    r"ATOS\s+NORMATIVOS|"
    r"M[ÓO]DULO\s+[I123V]+|"
    r"BLOCO\s+[I123V]+|"
    r"PARTE\s+[I123V]+|"
    r"ESPA[ÇC]O\s+LIVRE|"
    r"RASCUNHO"
    r")\s*$",
    re.I,
)

BASE_TEXT_START_RE = re.compile(
    r"(?:"
    r"^\s*Aten[çc][ãa]o\s*:\s*(?:As\s+quest[õo]es|Para\s+responder)|"
    r"^\s*(?:Considere|Leia|Analise)\s+(?:o\s+texto|os\s+textos)\s+(?:I+|1|2|3|a\s+seguir|abaixo)\s+para\s+responder|"
    r"^\s*Texto\s+(?:I+|1|2|3|4|CG\d+[A-Z0-9\-]*|CB\d+[A-Z0-9\-]*)\b|"
    r"^\s*O\s+texto\s+seguinte\s+servir[áa]\s+de\s+base\s+para\s+responder|"
    r"^\s*As\s+quest[õo]es\s+de\s+n[úu]meros?\s+\d+\s+a\s+\d+\s+referem-se|"
    r"^\s*Instru[çc][ãa]o:\s*As\s+quest[õo]es\s+de\s+n[úu]meros?|"
    r"^\s*\(Dispon[íi]vel\s+em:\s*https?://|"
    r"^\s*Internet:\s*<|"
    r"^\s*Fonte:\s*https?://"
    r")",
    re.I,
)

CEBRASPE_GROUP_CMD_RE = re.compile(
    r"(?:"
    r"julgue\s+os\s+(?:seguintes\s+|pr[óo]ximos\s+)?itens(?:\s+a\s+seguir|\s+que\s+se\s+seguem|\s+subsecutivos|\s+subsequentes)?|"
    r"julgue\s+o\s+(?:seguinte\s+|pr[óo]ximo\s+)?item(?:\s+a\s+seguir|\s+que\s+se\s+segue)?|"
    r"assinale\s+a\s+op[çc][ãa]o\s+correta\s+nos\s+itens\s+a\s+seguir"
    r")\s*[\.\:]?\s*$",
    re.I,
)

REVOKED_LAWS_RE = re.compile(
    r"\b(?:"
    r"Lei\s*(?:Federal\s*)?(?:n[ºo°\.\s]*)?8\.666(?:\/1993|\/93)?|"
    r"Lei\s*(?:Federal\s*)?(?:n[ºo°\.\s]*)?10\.520(?:\/2002|\/02)?|"
    r"Regime\s*Diferenciado\s*de\s*Contrata[çc][õo]es|"
    r"Lei\s*(?:n[ºo°\.\s]*)?12\.462(?:\/2011|\/11)?|"
    r"Decreto\s*(?:n[ºo°\.\s]*)?5\.450(?:\/2005|\/05)?|"
    r"Decreto\s*(?:n[ºo°\.\s]*)?3\.555(?:\/2000|\/00)?"
    r")\b",
    re.I,
)

VISUAL_DEPENDENCY_RE = re.compile(
    r"\b(?:"
    r"conforme\s+(?:a\s+)?(?:figura|imagem|tabela|planilha|gr[áa]fico|diagrama|fluxograma|quadro|circuito|topologia)\s+(?:abaixo|acima|a\s+seguir|ilustrad[oa]|apresentad[oa])|"
    r"observ(?:e|ando)\s+(?:a\s+|o\s+|uma?\s+)?(?:figura|imagem|tabela|planilha|gr[áa]fico|diagrama|fluxograma|quadro|tela|janela|mapa|foto|fotografia|ilustra[çc][ãa]o|rede\s+pert|pe[çc]a\s+de\s+campanha)\b|"
    r"(?:analise|considere|veja)\s+(?:a\s+|o\s+|uma?\s+)?(?:figura|imagem|gr[áa]fico|diagrama|fluxograma|organograma|mapa|foto|fotografia|ilustra[çc][ãa]o)\s+(?:[A-Z0-9\-]+\s+)?(?:acima|abaixo|a\s+seguir|ilustrad[oa]|apresentad[oa]|mostrad[oa])|"
    r"(?:na|da|pela)\s+(?:figura|imagem|tabela|planilha|gr[áa]fico|diagrama|fluxograma|quadro|tela|janela|[áa]rvore|grafo)\s+(?:acima|abaixo|a\s+seguir|ilustrad[oa]|apresentad[oa]|mostrad[oa])|"
    r"(?:as\s+figuras|a\s+foto|o\s+mapa|o\s+diagrama|a\s+figura(?:\s+plana)?|gr[áa]fico|fluxograma|tabela|planilha|quadro|circuito|topologia|modelo\s+entidade-relacionamento)\s+(?:a\s+seguir|abaixo|acima|apresentad[oa]s?)\b|"
    r"cuja\s+inst[âa]ncia\s+[ée]\s+mostrada\s+(?:a\s+seguir|abaixo|acima)|"
    r"tirinha|tira\s+c[ôo]mica|charge|cartum|hist[óo]ria\s+em\s+quadrinhos|infogr[áa]fico|pe[çc]a\s+(?:de\s+campanha|publicit[áa]ria)|elementos?\s+(?:verbais\s+e\s+)?n[ãa]o\s+verbais|linguagem\s+n[ãa]o\s+verbal"
    r")\b",
    re.I,
)

OUT_OF_SCOPE_PATTERNS = [
    # 1. Ciências Atuariais
    r"\b(?:nota[çc][ãa]o|passivo|avalia[çc][ãa]o|nota\s+t[ée]cnica|c[áa]lculo)\s+atuarial\b",
    r"\bhans-ulrich\s+gerber\b",
    r"\b(?:t[áa]buas?|hip[óo]teses?|premissas?)\s+biom[ée]tricas?\b",
    r"\bcomuta[çc](?:[ãa]o|[õo]es)\s+(?:atuaria(?:l|is)|tabuladas)\b",
    r"\bprovis[õo]es?\s+matem[áa]ticas?\b",
    r"\banuidade\s+vital[íi]cia\b",
    r"\bprobabilidade\s+kpx\b",
    r"\bseguro\s+dotal\s+puro\b",
    r"\bfun[çc][ãa]o\s+heritor\b",
    # 2. Engenharia Civil, Rodoviária, Saneamento, Estruturas, Hidráulica e Solos
    r"\bviga\s+(?:biapoiada|biengastada|cont[íi]nua|met[áa]lica|possui\s+se[çc][ãa]o)\b",
    r"\bmomento\s+(?:fletor|de\s+in[ée]rcia)\b",
    r"\besfor[çc]o\s+cortante\b",
    r"\btreli[çc]a\b",
    r"\bconcreto\s+(?:armado|asf[áa]ltico|fresco|protendido)\b",
    r"\bensaio\s+spt\b",
    r"\bestacas?\s+(?:raiz|h[ée]lice|frank|escavada|pr[ée]-moldada|cravadas?)\b",
    r"\bfunda[çc](?:[ãa]o|[õo]es)\s+(?:rasa|profunda|direta|indireta|de\s+uma\s+obra)\b",
    r"\bsapatas?\s+(?:isolada|corrida|associada)\b",
    r"\btubul(?:[ãa]o|[õo]es)\s+(?:a\s+c[ée]u\s+aberto|a\s+ar\s+comprimido)\b",
    r"\b(?:mec[âa]nica|prospec[çc][ãa]o|grau\s+de\s+satura[çc][ãa]o)\s+d[eo]s?\s+solos?\b",
    r"\bnivelamento\s+geom[ée]trico\b",
    r"\btop[óo]grafo\b",
    r"\blagoas?\s+de\s+estabiliz[aá][çc][ãa]o\b",
    r"\b(?:tratamento|sistemas?)\s+de\s+esgotos?\b",
    r"\bautodepura[çc][ãa]o\s+dos\s+corpos\s+d['’][áa]gua\b",
    r"\bpintura\s+de\s+edifica[çc][õo]es\b",
    r"\balvenaria\s+estrutural\b",
    r"\barmaduras?\s+de\s+flex[ãa]o\b",
    r"\blajes?\s+maci[çc]as?\s+de\s+concreto\b",
    r"\bescoramento\s+de\s+formas\b",
    r"\b(?:drenagem|terraplenagem|pavimento)\s+de\s+(?:uma\s+)?(?:rodovia|estrada|via)\b",
    r"\baltura\s+manom[ée]trica\b",
    r"\bdimensionar\s+uma\s+adutora\b",
    r"\b(?:CA-50|CA-60|NBR\s+7190|NBR\s+6118)\b",
    # 3. Engenharia Mecânica / Termodinâmica / Elétrica
    r"\b(?:primeira|segunda)\s+lei\s+da\s+termodin[âa]mica\b",
    r"\bciclos?\s+(?:termodin[âa]micos?|de\s+carnot|rankine|otto|diesel)\b",
    r"\bm[áa]quinas?\s+t[ée]rmicas?\b",
    r"\bentalpia\b",
    r"\bescoamento\s+(?:laminar|turbulento|permanente\s+uniforme)\b",
    r"\bn[úu]mero\s+de\s+reynolds\b",
    r"\bcaldeiras?\s+aquatubular\b",
    r"\bcompressores?\s+alternativos?\b",
    r"\bmotor(?:es)?\s+(?:el[ée]trico\s+trif[áa]sico|de\s+indu[çc][ãa]o)\b",
    r"\bsistema\s+el[ée]trico\s+de\s+pot[êe]ncia\b",
    r"\bconvers[ãa]o\s+eletromec[âa]nica\s+de\s+energia\b",
    # 4. Saúde / Odontologia / Medicina clínica
    r"\bcl[íi]nica\s+odontol[óo]gica\b",
    r"\bsa[úu]de\s+bucal\b",
    r"\bc[áa]rie\s+dent[áa]ria\b",
    r"\bperiodontite\b",
    r"\bposologia\s+do\s+medicamento\b",
    r"\bdiagn[óo]stico\s+cl[íi]nico\s+de\s+patologia\b",
    r"\bleitos?\s+de\s+uti\b",
    r"\bcuidados\s+de\s+enfermagem\b",
    # 5. Legislação local estrita de outros tribunais/estados
    r"\bLei\s+Complementar\s+(?:Estadual\s+)?n[ºo°]?\s*0?66/1993\b",
    r"\bRegimento\s+Interno\s+do\s+Tribunal\s+de\s+Justi[çc]a\s+do\s+Estado\s+d[eo]\s+(?:Amap[áa]|Roraima|Mato\s+Grosso)\b",
    r"\bC[óo]digo\s+de\s+Organiza[çc][ãa]o\s+Judici[áa]ria\s+do\s+Estado\s+do\s+Amap[áa]\b",
    r"\bRegimento\s+Interno\s+do\s+TJ-?(?:AP|RR|MT)\b",
]
OUT_OF_SCOPE_RE = re.compile("|".join(OUT_OF_SCOPE_PATTERNS), re.I)


def is_header_or_footer_block(b, w, h):
    x0, y0, x1, y1, txt, bno, btype = b
    if btype != 0:
        return False
    s = txt.strip()
    if not s:
        return True
    if y1 <= h * 0.052 or y0 >= h * 0.932:
        return True
    if y0 < h * 0.088:
        if (x1 - x0) > w * 0.52 and re.search(
            r"(?:TRIBUNAL|CONCURSO|FGV|CEBRASPE|CESPE|CADERNO|EDITAL|TIPO\s+0?1|PROVA|ORGANIZADORA)", s, re.I
        ):
            return True
        if re.search(
            r"(?:Caderno de Prova|CEBRASPE\s*[–\|]|CESPE\s*\|?\s*CEBRASPE|\|\|.*\|\||CONCURSO P[ÚU]BLICO)", s, re.I
        ):
            return True
    if y1 > h * 0.895:
        if re.search(
            r"(?:pciconcursos|P[ÁA]GINA\s*\d+|TIPO\s+BRANCA|TIPO\s+\d|Conhecimentos\s+Gerais\d|Conhecimentos\s+Espec[íi]ficos\d|IBFC_\d+|FAPERP|ANALISTA\s+JUDICI[ÁA]RIO.*TIPO)",
            s,
            re.I,
        ):
            return True
    return False


def is_cover_or_instructions_page(page, pno):
    if pno > 2:
        return False
    txt = page.get_text("text")
    if re.search(r"(?m)(?:^\s*QUEST[ÃA]O\s+0*[1-9]\b|^\s*0*1\s*[\.\)]\s+[A-ZÁÉÍÓÚ])", txt, re.I):
        return False
    if re.search(
        r"(?:ASSINATURA DO CANDIDATO|FOLHA DE TEXTO DEFINITIVO DA PROVA DISCURSIVA|Leia,\s*atentamente,\s*as\s*instru[çc][õo]es|SUA PROVA\s+Al[ée]m deste caderno)",
        txt,
        re.I,
    ):
        return True
    return False


def extract_column_aware_blocks_from_page(page):
    """
    Extrai blocos visuais da página respeitando diagramação em 1 ou 2 colunas.
    Blocos que cruzam o eixo central (full-width) dividem a página em bandas;
    dentro de cada banda de 2 colunas, lê toda a coluna da esquerda de cima a baixo
    e depois toda a coluna da direita de cima a baixo.
    """
    w, h = page.rect.width, page.rect.height
    mid_x = w / 2.0
    raw_blocks = page.get_text("blocks")

    filtered = []
    for b in raw_blocks:
        x0, y0, x1, y1, txt, bno, btype = b
        if btype == 1:
            bw, bh = x1 - x0, y1 - y0
            if y0 > h * 0.075 and y1 < h * 0.915 and bw >= 28 and bh >= 20:
                filtered.append((x0, y0, x1, y1, "[[IMAGE_BLOCK]]", bno, 1))
            continue
        if is_header_or_footer_block(b, w, h):
            continue
        cleaned_lines = []
        for l in txt.split("\n"):
            ls = l.strip()
            if not ls:
                continue
            if HEADER_FOOTER_LINE_RE.search(ls):
                continue
            if re.match(r"^_{5,}\s*$", ls):
                cleaned_lines.append("<<BLOCK>>\n[[SECTION_BREAK]]\n<<BLOCK>>")
                continue
            cleaned_lines.append(ls)
        if not cleaned_lines:
            continue
        clean_txt = "\n".join(cleaned_lines)
        if SECTION_HEADER_BLOCK_RE.match(clean_txt) or BASE_TEXT_START_RE.search(clean_txt):
            filtered.append((x0, y0, x1, y1, "[[SECTION_BREAK]]\n" + clean_txt, bno, 0))
            continue
        filtered.append((x0, y0, x1, y1, clean_txt, bno, 0))

    bands = []
    curr_left = []
    curr_right = []

    for b in sorted(filtered, key=lambda item: (round(item[1] / 4.0), item[0])):
        x0, y0, x1, y1, txt, bno, btype = b
        is_full_width = (x0 < mid_x - 35) and (x1 > mid_x + 35)
        if is_full_width:
            if curr_left or curr_right:
                curr_left.sort(key=lambda item: (round(item[1] / 4.0), item[0]))
                curr_right.sort(key=lambda item: (round(item[1] / 4.0), item[0]))
                bands.extend(curr_left)
                bands.extend(curr_right)
                curr_left = []
                curr_right = []
            bands.append(b)
        else:
            cx = (x0 + x1) / 2.0
            if x0 < mid_x - 12 and cx < mid_x + 8:
                curr_left.append(b)
            else:
                curr_right.append(b)

    if curr_left or curr_right:
        curr_left.sort(key=lambda item: (round(item[1] / 4.0), item[0]))
        curr_right.sort(key=lambda item: (round(item[1] / 4.0), item[0]))
        bands.extend(curr_left)
        bands.extend(curr_right)

    return bands


def clean_inline_text(s):
    s = s.replace("<<BLOCK>>", "\n").replace("[[SECTION_BREAK]]", "\n")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"([a-záéíóúâêôãõç])-\s*\n\s*([a-záéíóúâêôãõç])", r"\1\2", s)
    s = re.sub(r"\s*\n\s*", " ", s)
    return s.strip()


def truncate_trailing_noise_from_text(text, is_cebraspe_ce=False):
    parts = [p.strip() for p in text.split("<<BLOCK>>") if p.strip()]
    if not parts:
        return ""

    kept = []
    for part in parts:
        if "[[SECTION_BREAK]]" in part:
            before_sb = part.split("[[SECTION_BREAK]]")[0].strip()
            if before_sb:
                kept.append(before_sb)
            break

        if SECTION_HEADER_BLOCK_RE.match(part) or BASE_TEXT_START_RE.search(part):
            break

        if CEBRASPE_GROUP_CMD_RE.search(part):
            break

        if not kept:
            kept.append(part)
        else:
            prev_joined = " ".join(kept).strip()
            if re.search(r"[\.\?\!\"”\;]\s*$", prev_joined):
                if not is_cebraspe_ce:
                    break
                else:
                    if not re.search(
                        r"(?:a\s+seguir|abaixo|seguinte|argumento|di[áa]logo|texto|trecho)[\.\:]\s*$",
                        prev_joined,
                        re.I,
                    ):
                        break
            if len(part) > 400:
                break
            kept.append(part)

    res = "\n".join(kept).strip()
    lines = res.split("\n")
    while lines:
        last_l = lines[-1].strip()
        if (
            not last_l
            or SECTION_HEADER_BLOCK_RE.match(last_l)
            or BASE_TEXT_START_RE.search(last_l)
            or CEBRASPE_GROUP_CMD_RE.search(last_l)
        ):
            lines.pop()
        elif re.search(
            r"^(?:Texto\s+[I1234V]+|Dispon[íi]vel\s+em:|Fonte:|Adaptado\s+de\b|Internet:\s*<)", last_l, re.I
        ):
            lines.pop()
        else:
            break
    return clean_inline_text("\n".join(lines))


def parse_alternatives_from_block(block_text):
    patterns = [
        r"(?m)(?:^\s*|\s+)\(([A-E])\)(?:\s+|\s*\n\s*)",
        r"(?m)^\s*([A-Ea-e])\)(?:\s+|\s*\n\s*)",
        r"(?m)^\s*([A-E])(?:\s*\n\s*(?:<<BLOCK>>\s*\n\s*)?|\s+)(?=[A-ZÁÉÍÓÚÂÊÔÃÕÇa-záéíóúâêôãõç0-9\"“‘'(\-\/])",
    ]

    for pat in patterns:
        matches = list(re.finditer(pat, block_text))
        if len(matches) < 4:
            continue
        seq = []
        for m in matches:
            let = m.group(1).upper()
            if let == "A":
                if len(seq) < 4:
                    seq = [m]
            elif seq and ord(let) == ord(seq[-1].group(1).upper()) + 1:
                seq.append(m)

        if len(seq) in (4, 5):
            enun_raw = block_text[: seq[0].start()]
            alts = {}
            for i, m in enumerate(seq):
                let = m.group(1).upper()
                a_start = m.end()
                a_end = seq[i + 1].start() if i + 1 < len(seq) else len(block_text)
                alt_slice = block_text[a_start:a_end]
                if i + 1 == len(seq):
                    alts[let] = truncate_trailing_noise_from_text(alt_slice, is_cebraspe_ce=False)
                else:
                    alts[let] = clean_inline_text(alt_slice)
            return clean_inline_text(enun_raw), alts

    return None, None


def select_optimal_question_sequence(candidates, min_expected, max_expected):
    """
    Usa programação dinâmica (Longest Increasing Subsequence ponderada) para
    selecionar os cabeçalhos reais de questões em ordem estritamente crescente,
    ignorando números espúrios dentro de enunciados ou alternativas matemáticas.
    """
    filtered = [c for c in candidates if min_expected <= c[0] <= max_expected]
    if not filtered:
        return []

    n = len(filtered)
    dp = [0.0] * n
    parent = [-1] * n

    for i in range(n):
        q_i, s_i, _, w_i = filtered[i]
        # Bônus se começar próximo a min_expected ou 1
        start_penalty = 0.0 if (q_i - min_expected) <= 5 else -float(q_i - min_expected) * 0.5
        dp[i] = 10.0 + w_i + start_penalty

        for j in range(max(0, i - 45), i):
            q_j, s_j, _, _ = filtered[j]
            if q_i <= q_j:
                continue
            gap = q_i - q_j
            if gap > 25:
                continue
            # Evitar matches quase na mesma posição de caractere (ex: dentro da mesma alternativa)
            if s_i - s_j < 35:
                continue

            step_score = 15.0 if gap == 1 else max(2.0, 11.0 - gap * 1.2)
            cand_score = dp[j] + step_score + w_i
            if cand_score > dp[i]:
                dp[i] = cand_score
                parent[i] = j

    best_end = max(range(n), key=lambda idx: dp[idx])
    seq = []
    curr = best_end
    while curr != -1:
        q_num, s_pos, e_pos, _ = filtered[curr]
        seq.append((q_num, s_pos, e_pos))
        curr = parent[curr]
    seq.reverse()
    return seq


def extract_questions_from_proof(pv_path, ans_map):
    doc = open_pdf_fitz(pv_path)
    all_blocks = []
    for pno, page in enumerate(doc):
        if is_cover_or_instructions_page(page, pno):
            continue
        page_bks = extract_column_aware_blocks_from_page(page)
        for b in page_bks:
            all_blocks.append(b[4])

    full_text = "\n<<BLOCK>>\n".join(all_blocks)

    has_ce_answers = any(v in ("C", "E") for v in ans_map.values()) and not any(
        v in ("A", "B", "D") for v in ans_map.values()
    )
    if has_ce_answers:
        q_pat = re.compile(
            r"(?m)(?:"
            r"^\s*QUEST[ÃA]O\s+0*([1-9]\d{0,2})\b|"
            r"(?:^|<<BLOCK>>\n)\s*0*([1-9]\d{0,2})\s+(?=[A-ZÁÉÍÓÚÂÊÔÃÕÇ\"“‘'(\[])"
            r")",
            re.I,
        )
    else:
        q_pat = re.compile(
            r"(?m)(?:"
            r"^\s*QUEST[ÃA]O\s+0*([1-9]\d{0,2})\b|"
            r"(?:^|<<BLOCK>>\n)\s*0*([1-9]\d{0,2})\s*\n<<BLOCK>>|"
            r"^\s*0*([1-9]\d{0,2})\s*[\.\)]\s*(?:\n\s*)?(?=[A-ZÁÉÍÓÚÂÊÔÃÕÇ\"“‘'(\[])"
            r")",
            re.I,
        )

    candidates = []
    for m in q_pat.finditer(full_text):
        q_str = next(g for g in m.groups() if g is not None)
        q_num = int(q_str)
        # Peso maior para cabeçalhos explícitos ("QUESTÃO X" ou número isolado em bloco FGV)
        w_bonus = 6.0 if (m.group(1) is not None or m.group(2) is not None) else 2.0
        candidates.append((q_num, m.start(), m.end(), w_bonus))

    min_expected = min(ans_map.keys()) if ans_map else 1
    max_expected = max(ans_map.keys()) if ans_map else 120
    valid_q = select_optimal_question_sequence(candidates, min_expected, max_expected)

    pv_slug_l = os.path.basename(pv_path).lower()
    is_non_ti_eng_or_actuarial = any(
        w in pv_slug_l
        for w in (
            "engenharia-civil",
            "engenharia-mecanica",
            "engenharia-eletrica",
            "engenharia-sanitaria",
            "ciencias-atuariais",
            "controle-externo-engenharia",
        )
    )

    questions = []
    for idx, (q_num, s_pos, h_end) in enumerate(valid_q):
        e_pos = valid_q[idx + 1][1] if idx + 1 < len(valid_q) else len(full_text)
        raw_slice = full_text[h_end:e_pos]

        gab = ans_map.get(q_num)
        if not gab or gab == "ANULADA":
            continue

        if is_non_ti_eng_or_actuarial and q_num >= 61:
            if not re.search(
                r"\b(?:Lei\s+n[ºo°]?\s*14\.133|Constitui[çc][ãa]o\s+Federal|Tribunal\s+de\s+Contas|Controle\s+Externo|Licita[çc][ãa]o|Auditoria\s+Governamental|Or[çc]amento\s+P[úu]blico|Lei\s+Complementar\s+n[ºo°]?\s*101)\b",
                raw_slice,
                re.I,
            ):
                continue

        enun, alts = parse_alternatives_from_block(raw_slice)
        if enun and alts:
            full_q = enun + " " + " ".join(alts.values())
            if "[[IMAGE_BLOCK]]" in raw_slice or "[[IMAGE_BLOCK]]" in full_q:
                continue
            if REVOKED_LAWS_RE.search(full_q) or VISUAL_DEPENDENCY_RE.search(full_q) or OUT_OF_SCOPE_RE.search(full_q):
                continue
            if len(enun) < 20 or len(enun) > 3500:
                continue

            bad_alt = False
            for _, v in alts.items():
                if not v or len(v) > 1500 or not re.search(r"[a-zA-Z0-9]", v):
                    bad_alt = True
                    break
                # Descarta alternativas que sejam apenas hifens ou caracteres de fonte privada corrompida
                if re.match(r"^[\-\–\—\.\,\;\:\s]+$", v) or re.search(r"[\uf000-\uf8ff\ufffd]", v):
                    bad_alt = True
                    break
            if bad_alt or re.search(r"[\uf000-\uf8ff\ufffd]", enun):
                continue

            formato = "MULTIPLA_ESCOLHA_5" if len(alts) == 5 else "MULTIPLA_ESCOLHA_4"
            questions.append(
                {
                    "num_questao": q_num,
                    "formato": formato,
                    "enunciado": enun,
                    "alternativas": alts,
                    "gabarito": gab,
                }
            )
        elif gab in ("C", "E"):
            if "[[IMAGE_BLOCK]]" in raw_slice:
                continue
            enun_ce = truncate_trailing_noise_from_text(raw_slice, is_cebraspe_ce=True)
            if not enun_ce or len(enun_ce) < 30 or len(enun_ce) > 2000:
                continue
            if (
                REVOKED_LAWS_RE.search(enun_ce)
                or VISUAL_DEPENDENCY_RE.search(enun_ce)
                or OUT_OF_SCOPE_RE.search(enun_ce)
            ):
                continue
            if re.search(r"[\uf000-\uf8ff\ufffd]", enun_ce):
                continue
            questions.append(
                {
                    "num_questao": q_num,
                    "formato": "CERTO_ERRADO",
                    "enunciado": enun_ce,
                    "alternativas": {},
                    "gabarito": gab,
                }
            )

    return questions


def run_smart_extraction():
    print("Inicializando indexador semântico BM25 sobre docs/...")
    topic_index = SemanticTopicIndex(DOCS_DIR)
    print(f"Indexados {len(topic_index.docs)} guias de estudo em docs/.")

    pairs = pair_files(PROVAS_DIR)
    print(f"Total de pares Prova/Gabarito localizados em raw_provas/: {len(pairs)}")

    all_clean_questions = []
    seen_enunciados = set()

    for idx, (pv_file, gab_file) in enumerate(pairs, 1):
        pv_path = os.path.join(PROVAS_DIR, pv_file)
        gab_path = os.path.join(PROVAS_DIR, gab_file)
        meta = extract_metadata_from_slug(pv_file)

        try:
            ans_map = get_answer_key_for_pair(pv_path, gab_path)
            if not ans_map:
                continue
            extracted = extract_questions_from_proof(pv_path, ans_map)
        except Exception as exc:
            print(f"[AVISO] Falha ao processar {pv_file}: {exc}")
            continue

        added_from_proof = 0
        for q in extracted:
            norm_key = normalize_text(q["enunciado"])
            if len(norm_key) < 15 or norm_key in seen_enunciados:
                continue
            seen_enunciados.add(norm_key)

            full_q_text = q["enunciado"] + " " + " ".join(q["alternativas"].values())
            target_file, target_section, rel_score = topic_index.match(full_q_text)

            q_id = f"{meta['banca'].lower()}-{meta['ano']}-{meta['orgao'].lower()}-q{q['num_questao']:03d}-{len(all_clean_questions)+1:05d}"
            all_clean_questions.append(
                {
                    "id": q_id,
                    "banca": meta["banca"],
                    "ano": meta["ano"],
                    "orgao": meta["orgao"],
                    "cargo": meta["cargo"],
                    "prova_slug": meta["prova_slug"],
                    "num_questao": q["num_questao"],
                    "formato": q["formato"],
                    "enunciado": q["enunciado"],
                    "alternativas": q["alternativas"],
                    "gabarito": q["gabarito"],
                    "target_file": target_file,
                    "target_section": target_section,
                    "relevance_score": rel_score,
                }
            )
            added_from_proof += 1

        print(
            f"[{idx:02d}/{len(pairs):02d}] {meta['banca']:10s} | {meta['orgao']:7s} ({meta['ano']}) | "
            f"+{added_from_proof:3d} questões limpas | {pv_file[:55]}"
        )

    os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)
    payload = {
        "versao": "2.0",
        "extrator": "smart_extractor_v2_column_aware",
        "total_questoes": len(all_clean_questions),
        "questoes": all_clean_questions,
    }
    with open(OUTPUT_JSON, "w", encoding="utf-8") as fp:
        json.dump(payload, fp, ensure_ascii=False, indent=2)

    print(f"\n[EXTRAÇÃO V2 CONCLUÍDA] Total de Questões Limpas: {len(all_clean_questions)}")


if __name__ == "__main__":
    run_smart_extraction()

