#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
extract_pci_questions.py
========================
Script automatizado para processamento, extração, pareamento e classificação temática
de provas e gabaritos em PDF da pasta ./provas_pci.

Etapas:
1. Sincronização com o estado atual do projeto (mapa_topicos.json + leitura dos 119 .md)
2. Pareamento automático de Prova + Gabarito
3. Extração, limpeza e filtros de qualidade (leis revogadas, anulações, imagens)
4. Mapeamento semântico (BM25) para target_file e target_section
5. Geração de banco_questoes_extraidas.json e lacunas_edital.json
"""

import os
import sys
import re
import json
import math
import unicodedata
import pypdf

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PROVAS_DIR = os.path.join(ROOT_DIR, "provas_pci")
MAPA_TOPICOS_PATH = os.path.join(ROOT_DIR, "mapa_topicos.json")
BANCO_EXTRAIDO_PATH = os.path.join(ROOT_DIR, "banco_questoes_extraidas.json")
LACUNAS_PATH = os.path.join(ROOT_DIR, "lacunas_edital.json")

STOPWORDS = set("""
de da do das dos a o as os e em um uma uns umas para por com sem sob sobre entre ate que se ao aos na no nas nos
ou ser sao foi eh como mais menos mas seu sua seus suas esta este isso essa esse num numa pelo pela pelos pelas lhe ja nao
sim todo toda todos todas cada qual quais quando onde quem tambem apenas ainda pois entao assim porque seguinte correta
incorreta alternativa questao gabarito comentario detalhado afirmativa assertiva fcc fgv cespe cebraspe ibfc analista tecnico
judiciario tribunal prova considerando assinale termos acerca item itens correto incorreto respeito acordo texto
""".split())

def normalize_text(s):
    if not s:
        return ""
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r'[^a-zA-Z0-9]+', ' ', s).lower().strip()
    return s

def tokenize(s):
    return [t for t in normalize_text(s).split() if len(t) > 2 and t not in STOPWORDS]

# ==============================================================================
# 1. SINCRONIZAÇÃO E ÍNDICE SEMÂNTICO (BM25) DOS TÓPICOS DO EDITAL
# ==============================================================================

class SemanticTopicIndex:
    def __init__(self, root_dir, mapa_path):
        self.root_dir = root_dir
        self.mapa_path = mapa_path
        self.sections = [] # lista de dicts com info de cada seção
        self.load_index()

    def load_index(self):
        # 1. Ler mapa_topicos.json se existir
        mapa_data = {}
        if os.path.exists(self.mapa_path):
            with open(self.mapa_path, 'r', encoding='utf-8') as f:
                mapa_data = json.load(f)

        # 2. Ler todos os 119 arquivos Markdown para obter cabeçalhos e textos completos
        dirs = [
            "fontes_de_estudo/conhecimentos_gerais",
            "fontes_de_estudo/conhecimentos_especificos_b02_ti",
            "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo"
        ]

        doc_list = []
        for d in dirs:
            base = os.path.join(self.root_dir, d)
            if not os.path.exists(base):
                continue
            for dp, _, fns in os.walk(base):
                for fn in sorted(fns):
                    if fn.endswith('.md') and fn.lower() != 'readme.md':
                        p = os.path.join(dp, fn)
                        rel = os.path.relpath(p, self.root_dir).replace('\\', '/')
                        self.index_file(p, rel)

        # Preparar BM25
        self.N = len(self.sections)
        self.df = {}
        for sec in self.sections:
            for t in set(sec['tokens']):
                self.df[t] = self.df.get(t, 0) + 1
        self.avg_dl = sum(len(sec['tokens']) for sec in self.sections) / max(self.N, 1)

    def index_file(self, full_path, rel_path):
        with open(full_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # Identificar H1 (título do arquivo)
        h1_title = ""
        for l in lines:
            if l.startswith("# "):
                h1_title = l[2:].strip()
                break

        # Identificar seções teóricas (H2 e H3 entre Sumário e Fontes)
        in_theory = False
        current_sec = None
        current_body = []

        skip_pat = re.compile(r'Ementa|Sum[aá]rio|Fontes|Refer[êe]ncias', re.I)

        for l in lines:
            if re.search(r'##\s*🧭?\s*Sum[aá]rio', l, re.I):
                in_theory = False
                continue
            if re.search(r'##\s*🌐?\s*Fontes', l, re.I):
                # Fim da teoria
                if current_sec:
                    current_sec['body'] = '\n'.join(current_body)
                    current_sec['tokens'] = tokenize(current_sec['heading']) * 4 + tokenize(current_sec['body'])
                    self.sections.append(current_sec)
                    current_sec = None
                break

            m_h = re.match(r'^(#{2,3})\s+(.*?)\s*$', l)
            if m_h:
                level = len(m_h.group(1))
                htext = m_h.group(2).strip()
                if skip_pat.search(htext):
                    continue
                if re.match(r'^(?:\*\*)?Quest[ãa]o\s+\d+', htext, re.I):
                    continue

                in_theory = True
                if current_sec:
                    current_sec['body'] = '\n'.join(current_body)
                    current_sec['tokens'] = tokenize(current_sec['heading']) * 4 + tokenize(current_sec['body'])
                    self.sections.append(current_sec)

                current_sec = {
                    'rel_path': rel_path,
                    'file_title': h1_title,
                    'heading': ('## ' if level == 2 else '### ') + htext,
                    'level': level,
                    'body': '',
                    'tokens': []
                }
                current_body = []
            elif in_theory and current_sec:
                # Não acumular o texto de questões inline dentro do body da seção para não distorcer o vocabulário teórico
                if not l.startswith('>') and not re.search(r'^\s*[-*]\s+\*\*[A-E]\)', l):
                    current_body.append(l)

        if current_sec:
            current_sec['body'] = '\n'.join(current_body)
            current_sec['tokens'] = tokenize(current_sec['heading']) * 4 + tokenize(current_sec['body'])
            self.sections.append(current_sec)

    def match(self, text, top_k=3):
        q_tokens = tokenize(text)
        if not q_tokens:
            return self.sections[0]['rel_path'], self.sections[0]['heading']

        # Frequência dos termos da query
        q_tf = {}
        for t in q_tokens:
            q_tf[t] = q_tf.get(t, 0) + 1

        k1 = 1.5
        b = 0.75
        scores = []
        for idx, sec in enumerate(self.sections):
            score = 0.0
            dl = len(sec['tokens'])
            sec_tf = {}
            for t in sec['tokens']:
                sec_tf[t] = sec_tf.get(t, 0) + 1

            for t, weight in q_tf.items():
                f = sec_tf.get(t, 0)
                if not f:
                    continue
                doc_freq = self.df.get(t, 1)
                idf = math.log(1 + (self.N - doc_freq + 0.5) / (doc_freq + 0.5))
                score += weight * idf * (f * (k1 + 1)) / (f + k1 * (1 - b + b * (dl / self.avg_dl)))
            scores.append((score, idx))

        scores.sort(key=lambda x: x[0], reverse=True)
        best_idx = scores[0][1]
        best_sec = self.sections[best_idx]
        return best_sec['rel_path'], best_sec['heading']

# ==============================================================================
# 2. METADADOS E PAREAMENTO AUTOMÁTICO PROVA + GABARITO
# ==============================================================================

def extract_metadata_from_slug(slug, filename=""):
    slug_l = slug.lower().replace('_', '-')
    
    # Banca
    banca = "FCC"
    if "fgv" in slug_l:
        banca = "FGV"
    elif "cebraspe" in slug_l or "cespe" in slug_l:
        banca = "Cebraspe"
    elif "ibfc" in slug_l:
        banca = "IBFC"
    elif "consulplan" in slug_l:
        banca = "Instituto Consulplan"
    elif "fumarc" in slug_l:
        banca = "FUMARC"
    elif "faperp" in slug_l:
        banca = "FAPERP"
    elif "vunesp" in slug_l:
        banca = "Vunesp"

    # Ano
    ano = 2024
    m_ano = re.search(r'\b(200[89]|201[0-9]|202[0-6])\b', slug_l)
    if m_ano:
        ano = int(m_ano.group(1))

    # Orgao
    orgao = "TRT"
    m_org = re.search(r'\b(trt[\-\s]da[\-\s]\d+[\-\s]regiao|trt[\-\s]\d+|trf[\-\s]da[\-\s]\d+[\-\s]regiao|trf[\-\s]\d+|tj[\-\s][a-z]{2}|tjm[\-\s][a-z]{2}|stf|stj)\b', slug_l)
    if m_org:
        orgao = m_org.group(1).upper().replace('DA-', 'DA ').replace('REGIAO', 'REGIÃO')
    
    # Cargo
    cargo = "Analista Judiciário - Tecnologia da Informação"
    if "governanca" in slug_l:
        cargo = "Analista Judiciário - Governança e Gestão de TI"
    elif "suporte" in slug_l or "infraestrutura" in slug_l:
        cargo = "Analista Judiciário - Suporte e Infraestrutura de TI"
    elif "banco-de-dados" in slug_l:
        cargo = "Analista Judiciário - Banco de Dados"
    elif "desenvolvimento" in slug_l:
        cargo = "Analista Judiciário - Desenvolvimento de Sistemas"
    elif "seguranca" in slug_l:
        cargo = "Analista Judiciário - Segurança da Informação"
    elif "negocios" in slug_l:
        cargo = "Analista Judiciário - Análise de Negócios"
    elif "projetos" in slug_l:
        cargo = "Analista Judiciário - Gestão de Projetos"

    return banca, orgao, ano, cargo

def pair_proofs_and_answer_keys(provas_dir):
    files = [f for f in sorted(os.listdir(provas_dir)) if f.endswith('.pdf') and not f.startswith('edital')]
    
    provas = []
    gabaritos = []
    for f in files:
        f_l = f.lower()
        if 'copy' in f_l or 'padraoresposta' in f_l or 'discursiva' in f_l:
            continue
        if 'gab' in f_l:
            gabaritos.append(f)
        else:
            provas.append(f)

    pairs = []
    for pv in provas:
        pv_clean = pv.replace('.pdf', '')
        matched_gab = None
        if '___' in pv:
            slug, pv_rest = pv.split('___', 1)
            cand_gabs = [g for g in gabaritos if g.startswith(slug + '___')]
            if len(cand_gabs) == 1:
                matched_gab = cand_gabs[0]
            elif len(cand_gabs) > 1:
                pv_rest_l = pv_rest.lower()
                for g in cand_gabs:
                    g_rest_l = g.split('___', 1)[1].lower()
                    if ('basic' in pv_rest_l and 'basic' in g_rest_l) or ('espec' in pv_rest_l and 'espec' in g_rest_l):
                        matched_gab = g
                        break
                    codes = re.findall(r'\d+_\d+', pv_rest_l)
                    if codes and any(c in g_rest_l for c in codes):
                        matched_gab = g
                        break
                if not matched_gab:
                    matched_gab = cand_gabs[0]
        else:
            for g in gabaritos:
                if '___' not in g and g.startswith(pv_clean) and 'gab' in g:
                    matched_gab = g
                    break

        if matched_gab:
            pairs.append((pv, matched_gab))

    return pairs

# ==============================================================================
# 3. EXTRAÇÃO DE GABARITOS OFICIAIS
# ==============================================================================

def extract_answer_key_map(gabarito_path):
    try:
        reader = pypdf.PdfReader(gabarito_path)
    except Exception:
        return {}

    full_text = ""
    # Ler até 25 páginas
    for page in reader.pages[:25]:
        txt = page.extract_text() or ""
        full_text += txt + "\n"

    res = {}

    # 1. Padrão FCC: "001 - B" ou "1 - B"
    p1 = re.findall(r'(?m)^\s*0*([1-9]\d{0,2})\s*[-–—\.]\s*([A-E]|ANULAD[AO]|X|N)\b', full_text, re.I)
    if len(p1) >= 15:
        for q, g in p1:
            q_num = int(q)
            g_val = g.upper()
            res[q_num] = g_val if g_val not in ('X', 'N') and not g_val.startswith('ANUL') else 'ANULADA'
        return res

    # 2. Padrão FGV / Cebraspe: linhas alternadas (números seguidos de letras)
    lines = [l.strip() for l in full_text.split('\n') if l.strip()]
    for i in range(len(lines) - 1):
        num_toks = lines[i].split()
        ans_toks = lines[i+1].split()
        if len(num_toks) >= 4 and len(num_toks) == len(ans_toks):
            try:
                nums = [int(x) for x in num_toks]
                if all(1 <= n <= 150 for n in nums) and sorted(nums) == nums:
                    if all((len(a) == 1 and a.upper() in 'ABCDE') or a.upper() in ('X', 'N', '*', 'ANULADA') for a in ans_toks):
                        for n, a in zip(nums, ans_toks):
                            ans = a.upper()
                            res[n] = ans if ans not in ('X', 'N', '*', 'ANULADA') else 'ANULADA'
            except ValueError:
                pass

    if len(res) >= 15:
        return res

    # 3. Padrão Cebraspe C/E: números seguidos de C ou E
    p_ce = re.findall(r'\b0*([1-9]\d{0,2})\s*[:\-=]\s*([CE]|ANULAD[AO]|X|N)\b', full_text, re.I)
    if len(p_ce) >= 15:
        for q, g in p_ce:
            q_num = int(q)
            g_val = g.upper()
            res[q_num] = g_val if g_val not in ('X', 'N') and not g_val.startswith('ANUL') else 'ANULADA'
        return res

    # 4. Padrão inline "1-A 2-B 3-C"
    p4 = re.findall(r'\b0*([1-9]\d{0,2})\s*[:\-=]\s*([A-E]|ANULAD[AO]|X|N)\b', full_text, re.I)
    if len(p4) >= 15:
        for q, g in p4:
            q_num = int(q)
            g_val = g.upper()
            res[q_num] = g_val if g_val not in ('X', 'N') and not g_val.startswith('ANUL') else 'ANULADA'
        return res

    return res

# ==============================================================================
# 4. EXTRAÇÃO, LIMPEZA E FILTROS DE QUESTÕES DE CADA PROVA
# ==============================================================================

REVOKED_LAWS_PATTERN = re.compile(
    r'\b(?:Lei\s*(?:Federal\s*)?(?:n[ºo\.\s]*)?8\.666(?:\/1993|\/93)?|'
    r'Lei\s*(?:Federal\s*)?(?:n[ºo\.\s]*)?10\.520(?:\/2002|\/02)?|'
    r'Regime\s*Diferenciado\s*de\s*Contrata[çc][õo]es|'
    r'\bRDC\b|'
    r'Lei\s*(?:n[ºo\.\s]*)?12\.462(?:\/2011|\/11)?)\b',
    re.I
)

IMAGE_DEPENDENCY_PATTERN = re.compile(
    r'\b(?:conforme\s+(?:a\s+)?figura\s+(?:abaixo|acima|a\s+seguir)|'
    r'observando\s+(?:a\s+)?imagem\s+(?:ao\s+lado|acima|abaixo)|'
    r'no\s+gr[áa]fico\s+(?:acima|abaixo|ilustrado)|'
    r'diagrama\s+apresentado\s+na\s+figura|'
    r'quadro\s+ilustrativo\s+abaixo|'
    r'imagem\s+a\s+seguir)\b',
    re.I
)

def clean_proof_page_text(txt):
    lines = txt.split('\n')
    cleaned = []
    for l in lines:
        s = l.strip()
        if not s:
            cleaned.append('')
            continue
        if s.startswith('pcimarkpci') or 'www.pciconcursos.com.br' in s:
            continue
        if re.search(r'P[aá]gina\s+\d+\s+de\s+\d+', s, re.I):
            continue
        if re.search(r'^(?:TRIBUNAL|CONCURSO P[UÚ]BLICO|ANALISTA JUDICI[AÁ]RIO|PODER JUDICI[AÁ]RIO).*TIPO', s, re.I):
            continue
        cleaned.append(l)
    return '\n'.join(cleaned)

def extract_questions_from_proof(proof_path, answer_key_map, banca, orgao, ano, cargo):
    try:
        reader = pypdf.PdfReader(proof_path)
    except Exception:
        return []

    full_text = ""
    for p in reader.pages:
        txt = p.extract_text() or ""
        full_text += clean_proof_page_text(txt) + "\n"

    # Segmentação das questões
    # Procura marcadores de início de questão:
    # "QUESTÃO 01", "Questão 1", "\n1. ", "\n01. ", ou "\n1\n", "\n01\n"
    q_matches = list(re.finditer(
        r'(?m)(?:^\s*QUEST[ÃA]O\s+0*([1-9]\d{0,2})\b|^\s*0*([1-9]\d{0,2})\s*[\.\-]\s+|^\s*0*([1-9]\d{0,2})\s*$)',
        full_text
    ))

    # Filtrar matches para garantir que a sequência seja progressiva e plausível
    valid_blocks = []
    last_num = 0
    for m in q_matches:
        q_str = m.group(1) or m.group(2) or m.group(3)
        q_num = int(q_str)
        # Sequência plausível de questões de concurso (1 a 120)
        if 1 <= q_num <= 120 and (q_num > last_num or q_num == 1):
            valid_blocks.append((q_num, m.start(), m.end()))
            last_num = q_num

    extracted = []
    for idx, (q_num, start_pos, header_end) in enumerate(valid_blocks):
        end_pos = valid_blocks[idx + 1][1] if idx + 1 < len(valid_blocks) else len(full_text)
        block_text = full_text[header_end:end_pos].strip()

        # 1. Filtro: Se não tem gabarito pareado ou foi anulada
        gab = answer_key_map.get(q_num)
        if not gab or gab == 'ANULADA':
            continue

        # 2. Filtro: Leis expressamente revogadas (Lei 8.666/1993, Lei 10.520/2002, RDC)
        if REVOKED_LAWS_PATTERN.search(block_text):
            continue

        # 3. Filtro: Dependência irrecuperável de imagens/figuras não textuais
        if IMAGE_DEPENDENCY_PATTERN.search(block_text):
            continue

        # 4. Extração de alternativas A a E
        # Padrão: (A) ... (B) ... (C) ... (D) ... (E) ...
        alt_matches = list(re.finditer(r'(?m)(?:^\s*|\s+)\(([A-E])\)\s+', block_text))
        if not alt_matches:
            alt_matches = list(re.finditer(r'(?m)^\s*([A-E])\)\s+', block_text))

        if len(alt_matches) >= 4:
            # Questão de Múltipla Escolha (4 ou 5 opções)
            enunciado = block_text[:alt_matches[0].start()].strip()
            alternativas = {}
            for a_idx, am in enumerate(alt_matches):
                letter = am.group(1).upper()
                a_start = am.end()
                a_end = alt_matches[a_idx + 1].start() if a_idx + 1 < len(alt_matches) else len(block_text)
                alternativas[letter] = block_text[a_start:a_end].strip()

            formato = "MULTIPLA_ESCOLHA_5" if len(alternativas) == 5 else "MULTIPLA_ESCOLHA_4"

            # Validação mínima de qualidade de texto
            if len(enunciado) < 25 or any(len(v) < 1 for v in alternativas.values()):
                continue

            extracted.append({
                'q_num': q_num,
                'enunciado': enunciado,
                'alternativas': alternativas,
                'gabarito': gab,
                'formato': formato,
                'raw_text': block_text
            })
        elif gab in ('C', 'E') and len(block_text) >= 40:
            # Questão Cebraspe Certo/Errado
            # Limpar comandos iniciais genéricos se presentes
            enunciado = block_text
            enunciado = re.sub(r'^(?:Julgue os itens a seguir|Com base no texto|Considerando).*?:\s*', '', enunciado, flags=re.I)

            extracted.append({
                'q_num': q_num,
                'enunciado': enunciado.strip(),
                'alternativas': {},
                'gabarito': gab,
                'formato': "CERTO_ERRADO",
                'raw_text': block_text
            })

    return extracted

# ==============================================================================
# 5. EXECUÇÃO PRINCIPAL E GERAÇÃO DOS ARTEFATOS
# ==============================================================================

def main():
    print("="*75)
    print(" EXTRAÇÃO, LIMPEZA E CLASSIFICAÇÃO DE QUESTÕES PCI CONCURSOS")
    print("="*75)

    # 1. Carregar índice semântico dos tópicos
    print("\n[Etapa 1] Indexando árvore de tópicos e ementas dos 119 arquivos .md...")
    topic_index = SemanticTopicIndex(ROOT_DIR, MAPA_TOPICOS_PATH)
    print(f"Sucesso: {len(topic_index.sections)} seções/subtópicos indexados via BM25.")

    # 2. Parear Provas e Gabaritos
    print("\n[Etapa 2] Pareando cadernos de prova e gabaritos em ./provas_pci...")
    pairs = pair_proofs_and_answer_keys(PROVAS_DIR)
    print(f"Sucesso: {len(pairs)} pares de Prova + Gabarito identificados.")

    # 3. Processar cada prova
    print("\n[Etapa 3] Extraindo questões com gabarito oficial e aplicando filtros...")
    all_extracted_questions = []
    proofs_processed = 0

    # Contagem de questões por target_file para mapa de lacunas
    coverage_counts = {}
    for sec in topic_index.sections:
        coverage_counts.setdefault(sec['rel_path'], 0)

    for idx, (pv_file, gab_file) in enumerate(pairs):
        pv_path = os.path.join(PROVAS_DIR, pv_file)
        gab_path = os.path.join(PROVAS_DIR, gab_file)

        slug = pv_file.split('___')[0] if '___' in pv_file else pv_file.replace('.pdf', '')
        banca, orgao, ano, cargo = extract_metadata_from_slug(slug, pv_file)

        # Extrair gabarito oficial
        ans_map = extract_answer_key_map(gab_path)
        if not ans_map:
            continue

        # Extrair questões
        q_list = extract_questions_from_proof(pv_path, ans_map, banca, orgao, ano, cargo)
        if not q_list:
            continue

        proofs_processed += 1
        org_clean = re.sub(r'[^a-zA-Z0-9]+', '', orgao)

        for q in q_list:
            q_id = f"{org_clean}-{ano}-{banca}-Q{q['q_num']:02d}"
            # Classificação semântica do tópico alvo
            full_q_text = q['enunciado'] + " " + " ".join(q['alternativas'].values())
            target_file, target_section = topic_index.match(full_q_text)

            coverage_counts[target_file] = coverage_counts.get(target_file, 0) + 1

            all_extracted_questions.append({
                "id": q_id,
                "banca": banca,
                "orgao": orgao,
                "ano": ano,
                "cargo": cargo,
                "numero_original": q['q_num'],
                "enunciado": q['enunciado'],
                "alternativas": q['alternativas'],
                "gabarito_oficial": q['gabarito'],
                "formato": q['formato'],
                "target_file": target_file,
                "target_section": target_section,
                "status_integracao": "pendente"
            })

    print(f"Sucesso: {proofs_processed} provas lidas, {len(all_extracted_questions)} questões válidas extraídas com gabarito oficial.")

    # 4. Gravar banco_questoes_extraidas.json
    print(f"\n[Etapa 4] Gravando banco em {os.path.basename(BANCO_EXTRAIDO_PATH)}...")
    banco_payload = {
        "metadata": {
            "total_provas_processadas": proofs_processed,
            "total_questoes_extraidas": len(all_extracted_questions),
            "status_geral": "pendente",
            "filtros_aplicados": [
                "Descarte de questoes anuladas no gabarito oficial",
                "Descarte de legislacoes revogadas (ex: Lei 8.666/1993, Lei 10.520/2002, RDC)",
                "Descarte de questoes com imagens ou figuras graficas nao extraiveis em texto"
            ]
        },
        "questoes": all_extracted_questions
    }

    with open(BANCO_EXTRAIDO_PATH, 'w', encoding='utf-8') as f:
        json.dump(banco_payload, f, ensure_ascii=False, indent=2)

    # 5. Gerar lacunas_edital.json
    print(f"Mapeando lacunas temáticas em {os.path.basename(LACUNAS_PATH)}...")
    
    # Classificar arquivos com poucas questões extraídas (< 3 questões extraídas)
    lacunas = {
        "metadata": {
            "criterio_lacuna": "Arquivos do edital com menos de 3 questões adicionais no lote extraído de TI",
            "total_arquivos_com_lacuna": 0,
            "total_arquivos_edital": len(coverage_counts)
        },
        "modulos_com_lacunas": {}
    }

    lacunas_count = 0
    for rel_path, count in sorted(coverage_counts.items()):
        if count < 3:
            lacunas_count += 1
            parts = rel_path.split('/')
            mod = parts[2] if len(parts) > 2 else "geral"
            lacunas["modulos_com_lacunas"].setdefault(mod, []).append({
                "arquivo": rel_path,
                "questoes_extraidas_lote": count,
                "situacao": "CRÍTICA (0 questões)" if count == 0 else "BAIXA COBERTURA"
            })

    lacunas["metadata"]["total_arquivos_com_lacuna"] = lacunas_count

    with open(LACUNAS_PATH, 'w', encoding='utf-8') as f:
        json.dump(lacunas, f, ensure_ascii=False, indent=2)

    # 6. Relatório final no terminal
    print("\n" + "="*75)
    print(" RELATÓRIO DE PROCESSAMENTO E MAPA DE LACUNAS")
    print("="*75)
    print(f"Total de Cadernos de Prova Processados: {proofs_processed}")
    print(f"Total de Questões Extraídas e Validadas: {len(all_extracted_questions)}")
    print(f"Total de Arquivos do Edital Mapeados: {len(coverage_counts)}")
    print(f"Arquivos com Necessidade de Injeção Complementar (Lacunas): {lacunas_count}")
    print("\nPrincipais Módulos com Lacunas Identificadas no Acervo PCI:")
    for mod, flist in sorted(lacunas["modulos_com_lacunas"].items()):
        crit = sum(1 for item in flist if "CRÍTICA" in item["situacao"])
        print(f"  • {mod}: {len(flist)} arquivos com lacuna ({crit} com 0 questões extraídas)")
    print("="*75)
    print(f"Arquivos gerados na raiz: {os.path.basename(BANCO_EXTRAIDO_PATH)} e {os.path.basename(LACUNAS_PATH)}")

if __name__ == '__main__':
    main()

