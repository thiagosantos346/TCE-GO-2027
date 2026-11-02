#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
src/extraction/mcp_builder_v3.py

FASE 2 & FASE 3: Extrator Inteligente V3 Integrado ao MCP da PCI Concursos.
1. Carrega data/edital_estruturado.json.
2. Conecta-se via HTTP POST/SSE ao servidor MCP da PCI Concursos (https://mcp.pciconcursos.com.br/mcp),
   acionando a tool `pesquisar_provas` para cada tópico com a busca:
   "Prova FCC Analista Tribunal de Contas [PALAVRAS CHAVES DO TOPICO]" e fallback para FGV.
3. Baixa os PDFs das provas e gabaritos úteis para `raw_provas_v3/` (evitando downloads duplicados).
4. Extrai questões com `pdfplumber` ciente de layout (múltiplas colunas via bounding boxes `x0 < metade`,
   filtragem de 50px superiores/inferiores, suporte a Múltipla Escolha e Certo/Errado CEBRASPE).
5. Cruza com o PDF do gabarito oficial (tabelas e regex textual multi-cargo).
6. Aplica filtro semântico estrito contra os tópicos do edital e salva em `data/banco_questoes_v3.json`.
"""

import json
import os
import re
import shutil
import unicodedata
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed

import pdfplumber
import requests

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
EDITAL_JSON = os.path.join(BASE_DIR, "data", "edital_estruturado.json")
OUTPUT_V3_JSON = os.path.join(BASE_DIR, "data", "banco_questoes_v3.json")
RAW_PROVAS_V3_DIR = os.path.join(BASE_DIR, "raw_provas_v3")
LOCAL_CACHE_DIR = os.path.join(BASE_DIR, "raw_provas")
LINKS_DIRETOS_FILE = os.path.join(LOCAL_CACHE_DIR, "links_diretos.txt")

MCP_ENDPOINT = "https://mcp.pciconcursos.com.br/mcp"

STOPWORDS = {
    "a", "ao", "aos", "as", "ate", "com", "como", "da", "das", "de", "och", "do", "dos",
    "e", "em", "entre", "essa", "essas", "esse", "esses", "esta", "estas", "este", "estes",
    "na", "nas", "nao", "no", "nos", "num", "numa", "o", "os", "ou", "para", "pela",
    "pelas", "pelo", "pelos", "por", "qual", "quais", "quando", "que", "se", "sem", "seu",
    "seus", "sua", "suas", "sobre", "um", "uma", "umas", "uns", "uso", "conceito", "conceitos",
    "nocoes", "basicas", "basicos", "aplicada", "aplicado", "aplicadas", "aplicados", "gerais",
    "geral", "tipo", "tipos", "lei", "alteracoes", "posteriores", "disposicoes", "relativas",
    "estado", "goias", "federal", "estadual", "assinale", "alternativa", "correta", "incorreta",
    "opcao", "acordo", "conforme", "segundo", "abaixo", "acima", "seguinte", "seguintes",
}


def normalizar_texto(texto: str) -> str:
    if not texto:
        return ""
    nfkd = unicodedata.normalize("NFKD", texto)
    sem_acento = "".join(c for c in nfkd if not unicodedata.combining(c))
    return re.sub(r"[^a-zA-Z0-9\s]", " ", sem_acento).lower().strip()


def extrair_palavras_chave(texto: str, max_words: int = 4) -> list[str]:
    norm = normalizar_texto(texto)
    tokens = [
        t for t in norm.split()
        if len(t) > 2 and t not in STOPWORDS and not t.isdigit()
    ]
    seen = []
    for t in tokens:
        if t not in seen:
            seen.append(t)
    return seen[:max_words]


class PCIMCPClient:
    """Cliente HTTP/SSE JSON-RPC para o servidor MCP da PCI Concursos."""

    def __init__(self, endpoint: str = MCP_ENDPOINT):
        self.endpoint = endpoint
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/json, text/event-stream",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) TCE-GO-Extractor-V3/1.0",
        })
        self.cache_queries: dict[str, list[dict]] = {}
        self.req_id = 0

    def chamar_pesquisar_provas(self, termo_busca: str) -> list[dict]:
        termo_busca = re.sub(r"\s+", " ", termo_busca).strip()
        if termo_busca in self.cache_queries:
            return self.cache_queries[termo_busca]

        self.req_id += 1
        payload = {
            "jsonrpc": "2.0",
            "id": self.req_id,
            "method": "tools/call",
            "params": {
                "name": "pesquisar_provas",
                "arguments": {"termo": termo_busca},
            },
        }
        try:
            resp = requests.post(
                self.endpoint,
                json=payload,
                headers=dict(self.session.headers),
                timeout=12,
            )
            resp.raise_for_status()
            ctype = resp.headers.get("Content-Type", "")
            if "text/event-stream" in ctype:
                # Suporte SSE caso o servidor envie stream de eventos
                data_json = None
                for line in resp.text.splitlines():
                    if line.startswith("data:"):
                        data_json = json.loads(line[len("data:"):].strip())
                        break
            else:
                data_json = resp.json()

            if not data_json:
                self.cache_queries[termo_busca] = []
                return []

            content_list = data_json.get("result", {}).get("content", [])
            if not content_list:
                self.cache_queries[termo_busca] = []
                return []

            inner_text = content_list[0].get("text", "{}")
            parsed = json.loads(inner_text)
            provas = parsed.get("data", [])
            self.cache_queries[termo_busca] = provas
            return provas
        except Exception:
            self.cache_queries[termo_busca] = []
            return []

    def buscar_provas_por_topico(self, topico: str, materia: str = "") -> list[dict]:
        """
        Recebe um tópico do edital e aciona a tool `pesquisar_provas` no servidor MCP:
        1) Busca principal: "Prova FCC Analista Tribunal de Contas [PALAVRAS CHAVES DO TOPICO]"
        2) Fallback para FGV se FCC não retornar nada:
           "Prova FGV Analista Tribunal de Contas [PALAVRAS CHAVES DO TOPICO]"
        3) Como a busca booleana da PCI exige todas as palavras no título do cargo/órgão,
           realiza refinamento progressivo nas consultas MCP para retornar os links das provas.
        """
        kws = extrair_palavras_chave(topico, max_words=2)
        kw_str = " ".join(kws) if kws else extrair_palavras_chave(materia, max_words=1)[0]

        # 1. String exata exigida para FCC
        query_fcc_exata = f"Prova FCC Analista Tribunal de Contas {kw_str}".strip()
        resultados = self.chamar_pesquisar_provas(query_fcc_exata)

        # Fallback FGV exata se FCC exata retornar vazio
        if not resultados:
            query_fgv_exata = f"Prova FGV Analista Tribunal de Contas {kw_str}".strip()
            resultados = self.chamar_pesquisar_provas(query_fgv_exata)

        # Refinamento progressivo no MCP (pois a PCI filtra título de cargo/órgão)
        if not resultados:
            mat_norm = normalizar_texto(materia + " " + topico)
            consultas_refinadas = []
            if any(w in mat_norm for w in ["software", "sistemas", "dados", "redes", "seguranca", "ti", "tecnologia", "governanca", "ia", "devops"]):
                consultas_refinadas = [
                    "FCC Analista Tecnologia da Informacao",
                    "FGV Analista Tecnologia da Informacao",
                    "FCC TCE GO",
                    "FGV TCE GO",
                    "CEBRASPE Analista Tecnologia da Informacao",
                ]
            elif any(w in mat_norm for w in ["contabilidade", "orcamentaria", "financeira", "controle externo", "auditoria"]):
                consultas_refinadas = [
                    "FCC Analista Controle Externo",
                    "FGV Analista Controle Externo",
                    "FGV Auditor Controle Externo",
                    "FCC TCE GO",
                    "FGV TCE GO",
                ]
            else:
                consultas_refinadas = [
                    "FCC Analista Controle Externo Administrativa",
                    "FGV Analista Controle Externo",
                    "FCC Analista Judiciario Administrativa",
                    "FGV Analista Judiciario Administrativa",
                    "FGV TCE GO",
                ]

            for q_ref in consultas_refinadas:
                parciais = self.chamar_pesquisar_provas(q_ref)
                if parciais:
                    resultados.extend(parciais)

        return resultados


def carregar_mapa_links_diretos() -> dict[str, list[str]]:
    """Mapeia ID da prova PCI -> lista de URLs diretas de PDF quando disponíveis."""
    mapa: dict[str, list[str]] = {}
    if os.path.exists(LINKS_DIRETOS_FILE):
        with open(LINKS_DIRETOS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                url = line.strip()
                m = re.search(r"/provas/(\d+)/", url)
                if m:
                    pid = m.group(1)
                    if url not in mapa.setdefault(pid, []):
                        mapa[pid].append(url)
    return mapa


TURNSTILE_ATIVO = False


def montar_caminho_seguro(pasta: str, slug: str, nome_arq: str) -> str:
    """Garante que o caminho final no Windows não ultrapasse o limite MAX_PATH (260 caracteres)."""
    slug_curto = slug[:75]
    nome_curto = nome_arq if len(nome_arq) <= 65 else (nome_arq[:55] + "_" + nome_arq[-9:])
    dest_name = f"{slug_curto}___{nome_curto}"
    return os.path.join(pasta, dest_name)


def baixar_prova_e_gabarito(
    prova_info: dict,
    session: requests.Session,
    mapa_links: dict[str, list[str]],
    slugs_processados: set[str],
) -> tuple[list[str], list[str]]:
    """
    Baixa o PDF da prova e o PDF do gabarito para `raw_provas_v3/`,
    evitando baixar a mesma prova duas vezes verificando os nomes dos arquivos.
    """
    global TURNSTILE_ATIVO
    os.makedirs(RAW_PROVAS_V3_DIR, exist_ok=True)
    link_pagina = prova_info.get("link", "")
    prova_id = str(prova_info.get("id", ""))
    if not link_pagina:
        return [], []

    slug = link_pagina.rstrip("/").split("/")[-1]
    slug_prefix = slug[:75] + "___"
    if slug in slugs_processados:
        existentes = [
            os.path.join(RAW_PROVAS_V3_DIR, f)
            for f in os.listdir(RAW_PROVAS_V3_DIR)
            if f.startswith(slug_prefix) and f.endswith(".pdf")
        ]
        provas_pdf = [p for p in existentes if "gab" not in os.path.basename(p).lower()]
        gabs_pdf = [p for p in existentes if "gab" in os.path.basename(p).lower()]
        return provas_pdf, gabs_pdf

    # Verifica se já está salvo em raw_provas_v3/
    existentes = [
        os.path.join(RAW_PROVAS_V3_DIR, f)
        for f in os.listdir(RAW_PROVAS_V3_DIR)
        if f.startswith(slug_prefix) and f.endswith(".pdf")
    ]
    if existentes:
        slugs_processados.add(slug)
        provas_pdf = [p for p in existentes if "gab" not in os.path.basename(p).lower()]
        gabs_pdf = [p for p in existentes if "gab" in os.path.basename(p).lower()]
        return provas_pdf, gabs_pdf

    arquivos_salvos = []

    # 1. Tenta download HTTP direto caso o Turnstile ainda não tenha bloqueado a sessão
    if not TURNSTILE_ATIVO:
        urls_candidatas = list(mapa_links.get(prova_id, []))
        if not urls_candidatas:
            try:
                r_page = session.get(link_pagina, timeout=8)
                if r_page.status_code == 200:
                    for m in re.finditer(
                        r'data-code="([^"]+)"\s+data-arquivo="([^"]+)"', r_page.text
                    ):
                        code, arq = m.group(1), m.group(2)
                        u = f"https://www.pciconcursos.com.br/provas/{prova_id}/{code}/{arq}"
                        if u not in urls_candidatas:
                            urls_candidatas.append(u)
            except Exception:
                pass

        for pdf_url in urls_candidatas:
            nome_arq = pdf_url.rstrip("/").split("/")[-1]
            if "discursiva" in nome_arq.lower():
                continue
            dest_path = montar_caminho_seguro(RAW_PROVAS_V3_DIR, slug, nome_arq)
            try:
                r_pdf = session.get(pdf_url, timeout=8)
                if r_pdf.status_code == 200 and r_pdf.content.startswith(b"%PDF"):
                    with open(dest_path, "wb") as fp:
                        fp.write(r_pdf.content)
                    arquivos_salvos.append(dest_path)
                else:
                    # PCI retornou desafio HTML Turnstile em vez de %PDF
                    TURNSTILE_ATIVO = True
                    break
            except Exception:
                TURNSTILE_ATIVO = True
                break

    # 2. Fallback para os binários PDF já autenticados no cache local
    if not arquivos_salvos and os.path.exists(LOCAL_CACHE_DIR):
        cached_files = [
            f for f in os.listdir(LOCAL_CACHE_DIR)
            if f.startswith(slug + "___") and f.endswith(".pdf") and "discursiva" not in f.lower()
        ]
        for cf in cached_files:
            nome_arq = cf.split("___", 1)[1] if "___" in cf else cf
            src_p = "\\\\?\\" + os.path.abspath(os.path.join(LOCAL_CACHE_DIR, cf))
            dst_p = montar_caminho_seguro(RAW_PROVAS_V3_DIR, slug, nome_arq)
            if not os.path.exists(dst_p):
                with open(src_p, "rb") as f_in, open(dst_p, "wb") as f_out:
                    f_out.write(f_in.read())
            arquivos_salvos.append(dst_p)

    slugs_processados.add(slug)
    provas_pdf = [p for p in arquivos_salvos if "gab" not in os.path.basename(p).lower()]
    gabs_pdf = [p for p in arquivos_salvos if "gab" in os.path.basename(p).lower()]
    return provas_pdf, gabs_pdf


def agrupar_palavras_em_linhas(words: list[dict], y_tol: float = 3.0) -> list[str]:
    """Agrupa palavras (com bounding boxes) que estão na mesma linha horizontal."""
    if not words:
        return []
    sorted_w = sorted(words, key=lambda w: (round(w["top"] / y_tol) * y_tol, w["x0"]))
    lines = []
    cur_line = [sorted_w[0]]
    cur_top = sorted_w[0]["top"]
    for w in sorted_w[1:]:
        if abs(w["top"] - cur_top) <= y_tol:
            cur_line.append(w)
        else:
            cur_line.sort(key=lambda x: x["x0"])
            lines.append(" ".join(x["text"] for x in cur_line))
            cur_line = [w]
            cur_top = w["top"]
    if cur_line:
        cur_line.sort(key=lambda x: x["x0"])
        lines.append(" ".join(x["text"] for x in cur_line))
    return lines


def extrair_linhas_pdf_ciente_de_layout(pdf_path: str) -> list[str]:
    """
    Usa `pdfplumber` para abrir o PDF da prova:
    - Ignora Lixo: Filtra os 50 pixels superiores e inferiores de cada página (top > 50 e bottom < height - 50).
    - Múltiplas Colunas: Extrai palavras com suas caixas delimitadoras (bounding boxes),
      agrupa o texto da metade esquerda (x0 < metade da largura) e processa-o antes da metade direita.
    """
    all_lines: list[str] = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            largura = float(page.width)
            altura = float(page.height)
            metade_largura = largura / 2.0

            palavras_pagina = page.extract_words() or []
            palavras_limpas = []
            for wd in palavras_pagina:
                # Filtra os 50 pixels superiores e inferiores da página
                if wd["top"] <= 50.0 or wd["bottom"] >= (altura - 50.0):
                    continue
                txt_low = wd["text"].lower()
                if "pcimarkpci" in txt_low or "www.pciconcursos" in txt_low:
                    continue
                palavras_limpas.append(wd)

            if not palavras_limpas:
                continue

            # Verifica se a página está diagramada em 2 colunas (sem palavras atravessando o eixo central)
            atravessando_centro = [
                wd for wd in palavras_limpas
                if wd["x0"] < (metade_largura - 4.0) and wd["x1"] > (metade_largura + 4.0)
            ]

            if len(atravessando_centro) <= 2:
                # Múltiplas colunas: agrupa metade esquerda (x0 < metade) antes da metade direita
                col_esquerda = [wd for wd in palavras_limpas if wd["x0"] < metade_largura]
                col_direita = [wd for wd in palavras_limpas if wd["x0"] >= metade_largura]
                linhas_pagina = agrupar_palavras_em_linhas(col_esquerda) + agrupar_palavras_em_linhas(col_direita)
            else:
                # Coluna única (ex: cadernos FCC de largura total)
                linhas_pagina = agrupar_palavras_em_linhas(palavras_limpas)

            for ln in linhas_pagina:
                if re.search(
                    r"caderno de prova|página \d+|concursosfcc\.com|fgv conhecimento|direitos reservados",
                    ln,
                    re.IGNORECASE,
                ):
                    continue
                # Se houver múltiplas alternativas curtas na mesma linha (ex: "(A) 10 (B) 20"), separa-as
                partes_inline = re.split(r"\s+(?=\([A-E]\)\s)", ln)
                for p in partes_inline:
                    p_str = p.strip()
                    if p_str:
                        all_lines.append(p_str)

    return all_lines


def extrair_questoes_das_linhas(lines: list[str], banca: str) -> list[dict]:
    """
    Identifica questões por número (ex: `15.`, `Questão 15`, ou item numerado)
    e extrai alternativas `(A)`..`(E)` ou `A)`..`E)`, além de blocos Certo/Errado para CEBRASPE.
    """
    banca_up = banca.upper()
    questoes: list[dict] = []

    if "CEBRASPE" in banca_up or "CESPE" in banca_up:
        cur_q = None
        cur_text: list[str] = []
        for ln in lines:
            if re.match(r"^(?:QUESTÃO|Espaço livre|RASCUNHO|CONHECIMENTOS )", ln, re.IGNORECASE):
                continue
            m = re.match(r"^0*(\d{1,3})\s+([A-ZÁÉÍÓÚÂÊÔÃÕÇ\"“‘\(].*)$", ln)
            if m:
                qnum = int(m.group(1))
                if 1 <= qnum <= 150:
                    if cur_q is not None and cur_text:
                        enun = re.sub(r"\s+", " ", " ".join(cur_text)).strip()
                        if len(enun) >= 35:
                            questoes.append({
                                "num": cur_q,
                                "enunciado": enun,
                                "alternativas": {"C": "Certo", "E": "Errado"},
                                "formato": "CERTO_ERRADO",
                            })
                    cur_q = qnum
                    cur_text = [m.group(2).strip()]
                    continue
            if cur_q is not None:
                if re.match(
                    r"^(?:Com base n|Acerca d|Julgue os|A respeito d|Considerando |No que se refere|Quanto a|Tendo em vista)",
                    ln,
                ) and len(" ".join(cur_text)) > 75:
                    enun = re.sub(r"\s+", " ", " ".join(cur_text)).strip()
                    if len(enun) >= 35:
                        questoes.append({
                            "num": cur_q,
                            "enunciado": enun,
                            "alternativas": {"C": "Certo", "E": "Errado"},
                            "formato": "CERTO_ERRADO",
                        })
                    cur_q = None
                    cur_text = []
                else:
                    cur_text.append(ln)

        if cur_q is not None and cur_text:
            enun = re.sub(r"\s+", " ", " ".join(cur_text)).strip()
            if len(enun) >= 35:
                questoes.append({
                    "num": cur_q,
                    "enunciado": enun,
                    "alternativas": {"C": "Certo", "E": "Errado"},
                    "formato": "CERTO_ERRADO",
                })
        return questoes

    # Provas de Múltipla Escolha (FCC, FGV, etc.)
    cur_q = None
    cur_enun: list[str] = []
    cur_alts: dict[str, list[str]] = {}
    cur_alt_key = None

    def salvar_questao_mc():
        nonlocal cur_q, cur_enun, cur_alts, cur_alt_key
        if cur_q is not None and len(cur_alts) == 5:
            enun = re.sub(r"\s+", " ", " ".join(cur_enun)).strip()
            alts_dict = {
                k: re.sub(r"\s+", " ", " ".join(v)).strip()
                for k, v in cur_alts.items()
            }
            if len(enun) >= 25 and all(len(v) >= 1 for v in alts_dict.values()):
                questoes.append({
                    "num": cur_q,
                    "enunciado": enun,
                    "alternativas": alts_dict,
                    "formato": "MULTIPLA_ESCOLHA_5",
                })
        cur_q = None
        cur_enun = []
        cur_alts = {}
        cur_alt_key = None

    for ln in lines:
        # Regex de Alternativas: (A), (B), (C), (D), (E) ou A), B), C), D), E)
        m_alt = re.match(r"^(?:\(([A-E])\)|([A-E])\))\s*(.*)$", ln)
        if m_alt and cur_q is not None:
            letra = (m_alt.group(1) or m_alt.group(2)).upper()
            resto = m_alt.group(3).strip()
            cur_alt_key = letra
            cur_alts[letra] = [resto] if resto else []
            continue

        # Regex de Questão: "15. ...", "Questão 15 ...", ou linha isolada com número da questão
        m_q_dot = re.match(
            r"^(?:Quest[ãa]o\s+)?0*(\d{1,3})\s*[\.\-–]\s+([A-ZÁÉÍÓÚÂÊÔÃÕÇ0-9\"“‘\(].*)$",
            ln,
            re.IGNORECASE,
        )
        m_q_iso = re.match(r"^(?:Quest[ãa]o\s+)?0*(\d{1,3})$", ln, re.IGNORECASE)

        if m_q_dot:
            qnum = int(m_q_dot.group(1))
            if 1 <= qnum <= 120 and (cur_q is None or len(cur_alts) >= 4 or qnum == cur_q + 1):
                salvar_questao_mc()
                cur_q = qnum
                cur_enun = [m_q_dot.group(2).strip()]
                continue
        elif m_q_iso:
            qnum = int(m_q_iso.group(1))
            if 1 <= qnum <= 120 and (cur_q is None or len(cur_alts) >= 4 or qnum == cur_q + 1):
                salvar_questao_mc()
                cur_q = qnum
                cur_enun = []
                continue

        if cur_q is not None:
            if cur_alt_key is not None:
                cur_alts[cur_alt_key].append(ln)
            else:
                cur_enun.append(ln)

    salvar_questao_mc()
    return questoes


def extrair_gabarito_pdf(gab_paths: list[str], slug: str) -> dict[int, str]:
    """
    Lê o(s) PDF(s) de gabarito usando `pdfplumber.extract_tables()` e regex de texto
    para mapear o número da questão à letra correta.
    """
    if not gab_paths:
        return {}

    slug_tokens = set(re.findall(r"[a-z0-9]+", slug.lower())) - {
        "analista", "auditor", "tecnico", "judiciario", "de", "da", "do",
        "fgv", "fcc", "cebraspe", "cespe", "tce", "trt", "trf", "tj", "stj", "stf", "regiao",
    }

    gabarito_map: dict[int, str] = {}

    for gab_path in gab_paths:
        try:
            with pdfplumber.open(gab_path) as pdf:
                paginas_candidatas = []
                for page in pdf.pages:
                    txt = page.extract_text() or ""
                    txt_norm = normalizar_texto(txt)
                    score = sum(1 for t in slug_tokens if t in txt_norm)
                    if "tipo 1" in txt_norm or "gabarito 1" in txt_norm or "conhecimentos basicos" in txt_norm:
                        score += 0.5
                    paginas_candidatas.append((score, page, txt))

                if not paginas_candidatas:
                    continue

                max_score = max(p[0] for p in paginas_candidatas)
                paginas_selecionadas = [
                    (page, txt) for sc, page, txt in paginas_candidatas
                    if sc >= max(0.5, max_score - 0.5)
                ] or [(p[1], p[2]) for p in paginas_candidatas]

                for page, txt in paginas_selecionadas:
                    # 1. Tentativa via extract_tables()
                    try:
                        tables = page.extract_tables() or []
                        for tb in tables:
                            for r_idx in range(len(tb)):
                                row = [str(c or "").strip() for c in tb[r_idx]]
                                # Pareamento horizontal (célula "001 - E")
                                for cell in row:
                                    for m in re.finditer(r"\b0*(\d{1,3})\s*[-–:]\s*([A-ECEX*])\b", cell):
                                        qn = int(m.group(1))
                                        if 1 <= qn <= 150 and qn not in gabarito_map:
                                            gabarito_map[qn] = m.group(2).upper()
                                # Pareamento linha de números seguida de linha de letras
                                if r_idx + 1 < len(tb):
                                    next_row = [str(c or "").strip() for c in tb[r_idx + 1]]
                                    if len(row) == len(next_row) and len(row) >= 3:
                                        for c_num, c_let in zip(row, next_row):
                                            if re.fullmatch(r"0*\d{1,3}", c_num) and re.fullmatch(r"[A-ECEX*]", c_let.upper()):
                                                qn = int(c_num)
                                                if 1 <= qn <= 150 and qn not in gabarito_map:
                                                    gabarito_map[qn] = c_let.upper()
                    except Exception:
                        pass

                    # 2. Extração via Regex no texto da página (FCC: "001 - E", FGV/CEBRASPE: linhas num/letra)
                    for m in re.finditer(r"\b0*(\d{1,3})\s*[-–:]\s*([A-ECEX*])\b", txt):
                        qn = int(m.group(1))
                        if 1 <= qn <= 150 and qn not in gabarito_map:
                            gabarito_map[qn] = m.group(2).upper()

                    lines = [ln.strip() for ln in txt.splitlines() if ln.strip()]
                    for i in range(len(lines) - 1):
                        l_num = re.sub(r"^(?:Item|Quest[ãa]o|Itens)\s+", "", lines[i], flags=re.IGNORECASE).strip()
                        l_let = re.sub(r"^(?:Gabarito|Resposta|Respostas)\s+", "", lines[i + 1], flags=re.IGNORECASE).strip()
                        toks_num = l_num.split()
                        toks_let = l_let.split()
                        if len(toks_num) >= 5 and len(toks_num) == len(toks_let):
                            if all(re.fullmatch(r"\d{1,3}", x) for x in toks_num) and all(
                                re.fullmatch(r"[A-ECEX0*]", x.upper()) for x in toks_let
                            ):
                                for n_s, l_s in zip(toks_num, toks_let):
                                    qn = int(n_s)
                                    ans_char = l_s.upper()
                                    if 1 <= qn <= 150 and ans_char in ("A", "B", "C", "D", "E") and qn not in gabarito_map:
                                        gabarito_map[qn] = ans_char
        except Exception:
            continue

    return gabarito_map


def construir_indice_edital(edital_data: dict) -> list[dict]:
    """Prepara lista de tópicos do edital com seus conjuntos de palavras-chave para o Filtro Semântico."""
    indice = []
    for area in edital_data.get("areas", []):
        nome_area = area["nome_area"]
        for mat in area.get("materias", []):
            nome_materia = mat["nome_materia"]
            tokens_mat = set(extrair_palavras_chave(nome_materia, max_words=10))
            for topico in mat.get("topicos", []):
                tokens_top = set(extrair_palavras_chave(topico, max_words=20))
                all_tokens = tokens_top | tokens_mat
                if all_tokens:
                    indice.append({
                        "target_area": nome_area,
                        "target_materia": nome_materia,
                        "target_topico": topico,
                        "tokens_topico": tokens_top,
                        "tokens_combinados": all_tokens,
                    })
    return indice


def classificar_e_filtrar_questao(questao: dict, indice_edital: list[dict]) -> dict | None:
    """
    Filtro Semântico (A Trava de Segurança):
    Compara o texto da questão com as palavras do tópico do edital.
    Se não houver palavras em comum ou a similaridade for irrisória, descarta a questão
    (evitando capturar questões de Direito Penal, Direito do Trabalho ou Processo Civil).
    """
    texto_q = questao["enunciado"] + " " + " ".join(questao["alternativas"].values())
    norm_q = normalizar_texto(texto_q)

    # Trava explícita contra matérias fora do edital do TCE-GO
    termos_proibidos = [
        "consolidação das leis do trabalho", "reclamação trabalhista", "fgts", "aviso prévio",
        "código penal", "homicídio", "furto", "roubo", "estelionato", "habeas corpus",
        "inquérito policial", "pena de reclusão", "código de processo penal",
        "código de defesa do consumidor", "direito eleitoral", "partido político inelegibilidade",
    ]
    for proibido in termos_proibidos:
        if normalizar_texto(proibido) in norm_q:
            return None

    tokens_q = set(extrair_palavras_chave(texto_q, max_words=80))
    if len(tokens_q) < 4:
        return None

    melhor_item = None
    melhor_score = 0.0

    for item in indice_edital:
        inter_top = tokens_q & item["tokens_topico"]
        inter_all = tokens_q & item["tokens_combinados"]
        if not inter_top and len(inter_all) < 2:
            continue
        score = (len(inter_top) * 2.5) + (len(inter_all) * 1.0)
        if len(item["tokens_topico"]) > 0:
            score += len(inter_top) / len(item["tokens_topico"])
        if score > melhor_score:
            melhor_score = score
            melhor_item = item

    # Exige interseção semântica mínima real (pelo menos 1 palavra-chave forte do tópico + contexto ou >=2 termos)
    if melhor_item is None or melhor_score < 2.5:
        return None

    return {
        "target_area": melhor_item["target_area"],
        "target_materia": melhor_item["target_materia"],
        "target_topico": melhor_item["target_topico"],
        "score": round(melhor_score, 3),
    }


def inferir_metadados_do_slug(slug: str, meta_mcp: dict | None = None) -> tuple[str, str, int, str]:
    """Extrai (banca, orgao, ano, cargo) a partir do registro MCP ou do slug da prova."""
    if meta_mcp:
        banca = meta_mcp.get("organizadora") or "FCC"
        orgao = meta_mcp.get("orgao") or "TCE"
        ano = int(meta_mcp.get("ano") or 2024)
        cargo = meta_mcp.get("descricao") or "Analista de Controle Externo"
        return banca, orgao, ano, cargo

    partes = slug.split("-")
    ano = 2024
    if partes and re.fullmatch(r"20\d{2}", partes[-1]):
        ano = int(partes[-1])
        partes = partes[:-1]

    banca = "FGV"
    for b_cand in ["fcc", "fgv", "cebraspe", "cespe", "vunesp", "ibfc", "fumarc", "consulplan"]:
        if b_cand in partes:
            idx = partes.index(b_cand)
            banca = "CEBRASPE" if b_cand in ("cebraspe", "cespe") else b_cand.upper()
            partes_cargo_orgao = partes[:idx]
            break
    else:
        partes_cargo_orgao = partes

    orgao = "Tribunal"
    for org_prefix in ["tce", "trt", "trf", "tj", "stj", "stf", "tjm"]:
        if org_prefix in partes_cargo_orgao:
            o_idx = partes_cargo_orgao.index(org_prefix)
            orgao_tokens = partes_cargo_orgao[o_idx:]
            orgao = "/".join(t.upper() for t in orgao_tokens[:2])
            partes_cargo = partes_cargo_orgao[:o_idx]
            break
    else:
        partes_cargo = partes_cargo_orgao

    cargo = " ".join(partes_cargo).title() if partes_cargo else "Analista"
    return banca, orgao, ano, cargo


def main():
    print("=" * 75)
    print(" INICIANDO ESTEIRA DE EXTRAÇÃO V3 VIA INTEGRAÇÃO MCP (PCI CONCURSOS)")
    print("=" * 75)

    if not os.path.exists(EDITAL_JSON):
        raise FileNotFoundError(f"Arquivo {EDITAL_JSON} não encontrado. Execute parse_edital.py primeiro.")

    with open(EDITAL_JSON, "r", encoding="utf-8") as f:
        edital_data = json.load(f)

    indice_edital = construir_indice_edital(edital_data)
    print(f"[1/4] Edital carregado: {len(indice_edital)} tópicos estruturados prontos para busca MCP.")

    mcp_client = PCIMCPClient()
    mapa_links = carregar_mapa_links_diretos()
    provas_descobertas: dict[str, dict] = {}

    # Aciona a busca no MCP Server para os tópicos representativos de cada matéria em paralelo
    print("[2/4] Consultando servidor MCP (https://mcp.pciconcursos.com.br/mcp) tool `pesquisar_provas`...")
    topicos_busca = []
    materias_vistas = set()
    for item in indice_edital:
        mat = item["target_materia"]
        if mat not in materias_vistas:
            materias_vistas.add(mat)
            topicos_busca.append(item)

    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = [
            executor.submit(
                mcp_client.buscar_provas_por_topico,
                item["target_topico"],
                item["target_materia"],
            )
            for item in topicos_busca
        ]
        for fut in as_completed(futures):
            try:
                provas_mcp = fut.result()
                for p in provas_mcp:
                    link = p.get("link", "")
                    if link:
                        slug = link.rstrip("/").split("/")[-1]
                        provas_descobertas[slug] = p
            except Exception:
                pass

    # Também inclui no lote de descoberta os cadernos cujos links diretos constam no índice PCI da pasta local
    if os.path.exists(LOCAL_CACHE_DIR):
        for fname in sorted(os.listdir(LOCAL_CACHE_DIR)):
            if "___" in fname and fname.endswith(".pdf"):
                slug = fname.split("___")[0]
                if slug not in provas_descobertas:
                    banca, orgao, ano, cargo = inferir_metadados_do_slug(slug)
                    provas_descobertas[slug] = {
                        "id": "",
                        "descricao": cargo,
                        "orgao": orgao,
                        "ano": ano,
                        "organizadora": banca,
                        "link": f"https://www.pciconcursos.com.br/provas/download/{slug}",
                    }

    print(f" -> Provas identificadas via integração MCP: {len(provas_descobertas)} concursos/cadernos.")

    # Fase de Download e Extração Ciente de Layout
    print(f"[3/4] Baixando PDFs para `raw_provas_v3/` e extraindo questões com `pdfplumber` (2 colunas)...")
    slugs_processados: set[str] = set()
    questoes_validadas: list[dict] = []
    hashes_enunciado: set[str] = set()
    seq_id = 1

    for slug, info in sorted(provas_descobertas.items()):
        provas_pdf, gabs_pdf = baixar_prova_e_gabarito(
            prova_info=info,
            session=mcp_client.session,
            mapa_links=mapa_links,
            slugs_processados=slugs_processados,
        )
        if not provas_pdf or not gabs_pdf:
            continue

        banca, orgao, ano, cargo = inferir_metadados_do_slug(slug, info)
        gabarito_map = extrair_gabarito_pdf(gabs_pdf, slug)
        if not gabarito_map:
            continue

        for prova_pdf in provas_pdf:
            try:
                linhas = extrair_linhas_pdf_ciente_de_layout(prova_pdf)
                questoes_brutas = extrair_questoes_das_linhas(linhas, banca)
            except Exception:
                continue

            for qb in questoes_brutas:
                qnum = qb["num"]
                gab_oficial = gabarito_map.get(qnum)
                if not gab_oficial or gab_oficial in ("*", "X"):
                    continue
                if qb["formato"] == "MULTIPLA_ESCOLHA_5" and gab_oficial not in ("A", "B", "C", "D", "E"):
                    continue
                if qb["formato"] == "CERTO_ERRADO" and gab_oficial not in ("C", "E"):
                    continue

                # Deduplicação por enunciado normalizado
                chave_dedup = normalizar_texto(qb["enunciado"])[:180]
                if len(chave_dedup) < 25 or chave_dedup in hashes_enunciado:
                    continue

                # Filtro Semântico (A Trava de Segurança)
                classificacao = classificar_e_filtrar_questao(qb, indice_edital)
                if classificacao is None:
                    continue

                hashes_enunciado.add(chave_dedup)
                orgao_clean = re.sub(r"[^A-Z0-9]", "_", orgao.upper()).strip("_")
                q_id = f"V3_{banca.upper()}_{orgao_clean}_{ano}_Q{seq_id:04d}"
                seq_id += 1

                questoes_validadas.append({
                    "id": q_id,
                    "banca": banca,
                    "orgao": orgao,
                    "ano": int(ano),
                    "cargo": cargo,
                    "enunciado": qb["enunciado"],
                    "alternativas": qb["alternativas"],
                    "gabarito_oficial": gab_oficial,
                    "formato": qb["formato"],
                    "target_area": classificacao["target_area"],
                    "target_materia": classificacao["target_materia"],
                    "target_topico": classificacao["target_topico"],
                })

    # Salva em data/banco_questoes_v3.json
    os.makedirs(os.path.dirname(OUTPUT_V3_JSON), exist_ok=True)
    with open(OUTPUT_V3_JSON, "w", encoding="utf-8") as f:
        json.dump(questoes_validadas, f, ensure_ascii=False, indent=2)

    pdfs_baixados = len([f for f in os.listdir(RAW_PROVAS_V3_DIR) if f.endswith(".pdf")]) if os.path.exists(RAW_PROVAS_V3_DIR) else 0
    dist_bancas = Counter(q["banca"] for q in questoes_validadas)
    dist_areas = Counter(q["target_area"] for q in questoes_validadas)

    print("=" * 75)
    print(f"[4/4] BANCO V3 GERADO COM SUCESSO EM: {OUTPUT_V3_JSON}")
    print(f" -> Total de PDFs baixados em `raw_provas_v3/`: {pdfs_baixados}")
    print(f" -> Total de Questões Validadas salvas no Banco V3: {len(questoes_validadas)}")
    print(f" -> Distribuição por Banca: {dict(dist_bancas)}")
    print(f" -> Distribuição por Área:  {dict(dist_areas)}")
    print("=" * 75)


if __name__ == "__main__":
    main()
