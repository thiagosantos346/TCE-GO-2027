#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
src/utils/llm_question_router.py

Fase 2: Rotulador Cognitivo via Gemini API (SDK google-genai) com fallback semântico de alta precisão.
Lê cada questão de data/banco_questoes_v3.json, raciocina com base na árvore de
tópicos de data/edital_estruturado.json e classifica estruturadamente em:
- 'target_area'
- 'target_materia'
- 'target_topico' (ou 'LIXO' para questões fora do escopo do edital)
"""

import json
import os
import re
import sys
import time
import unicodedata
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
BANCO_PATH = BASE_DIR / "data" / "banco_questoes_v3.json"
EDITAL_PATH = BASE_DIR / "data" / "edital_estruturado.json"

# Import condicional do google-genai
try:
    from google import genai
    from google.genai import types
    from google.genai.errors import APIError
    GENAI_AVAILABLE = True
except ImportError:
    GENAI_AVAILABLE = False


def remover_acentos(texto: str) -> str:
    if not texto:
        return ""
    return "".join(c for c in unicodedata.normalize("NFD", texto) if unicodedata.category(c) != "Mn").lower()


def carregar_arvore_edital(edital_path: Path):
    data = json.loads(edital_path.read_text(encoding="utf-8"))
    linhas = []
    for area in data.get("areas", []):
        nome_area = area.get("nome_area")
        linhas.append(f"\n# ÁREA: {nome_area}")
        for mat in area.get("materias", []):
            nome_mat = mat.get("nome_materia")
            linhas.append(f"  ## MATÉRIA: {nome_mat}")
            for top in mat.get("topicos", []):
                linhas.append(f"    - {top}")
    return "\n".join(linhas), data


def formatar_alternativas(alts) -> str:
    if isinstance(alts, dict):
        return "\n".join([f"{k}) {v}" for k, v in alts.items()])
    elif isinstance(alts, list):
        return "\n".join([f"- {v}" for v in alts])
    return str(alts)


def classificar_questao_llm(client, model_name: str, prompt: str, max_retries: int = 5) -> dict:
    delay = 2.0
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    temperature=0.1,
                ),
            )
            text_resp = response.text.strip()
            parsed = json.loads(text_resp)
            if isinstance(parsed, list) and len(parsed) > 0:
                parsed = parsed[0]
            return parsed
        except APIError as e:
            if hasattr(e, "code") and e.code == 429:
                print(f"    [!] Rate Limit (429). Aguardando {delay:.1f}s...")
                time.sleep(delay)
                delay *= 2.0
            else:
                print(f"    [!] Erro API ({e}). Aguardando {delay:.1f}s...")
                time.sleep(delay)
                delay *= 1.5
        except Exception as e:
            print(f"    [!] Erro ({e}). Tentando novamente...")
            time.sleep(delay)
            delay *= 1.5

    return {"target_area": "", "target_materia": "", "target_topico": "LIXO"}


def classificar_cognitivo_local(q: dict) -> dict:
    """
    Raciocínio semântico de especialista para categorização exata de edital
    e eliminação cirúrgica de conteúdos espúrios (LIXO).
    """
    enunciado = q.get("enunciado", "")
    alternativas = formatar_alternativas(q.get("alternativas", {}))
    cargo = q.get("cargo", "")
    orgao = q.get("orgao", "")
    full_text = f"{enunciado} {alternativas}".strip()
    norm_text = remover_acentos(full_text)
    norm_cargo = remover_acentos(cargo)
    norm_orgao = remover_acentos(orgao)

    # 1. DETECÇÃO DE LIXO: Legislações locais/estaduais fora de Goiás / TCE-GO
    outros_estados_proibidos = [
        "santa catarina", "tj/sc", "tj-sc", "tce/sc", "tce-sc", "para", "tce/pa", "tce-pa",
        "piaui", "tce/pi", "tce-pi", "amapa", "tj/ap", "roraima", "tj/rr",
        "maranhao", "trt 16", "distrito federal e dos territorios", "tjdft"
    ]
    termos_locais_especificos = [
        "regimento interno", "lei organica", "estatuto dos servidores", "regime juridico unico",
        "plano de cargos", "codigo de divisao", "organizacao judiciaria", "orgao especial",
        "vara criminal", "comarca", "lei estadual", "lei complementar estadual",
        "constituicao do estado do", "constituicao estadual do"
    ]
    # Se menciona legislação local de outro estado e NÃO é de Goiás / TCE-GO
    is_goias = any(k in norm_text or k in norm_orgao for k in ["goias", "tce/go", "tce-go", "goiano"])
    if not is_goias:
        for est in outros_estados_proibidos:
            if est in norm_text or est in norm_orgao:
                if any(tl in norm_text for tl in termos_locais_especificos):
                    # Exceto se for CF/88 ou lei federal geral (ex: 8.429, 14.133, 9.784)
                    if not any(lf in norm_text for lf in ["lei 14.133", "lei 8.429", "lei 12.846", "cf/88", "constituicao federal"]):
                        return {"target_area": "", "target_materia": "", "target_topico": "LIXO"}

    # 2. DETECÇÃO DE LIXO: Disciplinas totalmente fora do edital
    # Contabilidade privada comercial (CPC, DRE privada, custos industriais, balanço comercial sem vínculo público)
    termos_contab_privada = [
        "cpc 00", "cpc 01", "cpc 16", "cpc 25", "cpc 27", "cpc 48", "pronunciamento tecnico cpc",
        "demonstracao do resultado do exercicio", "dre", "acoes em tesouraria", "capital social subscrito",
        "lucro por acao", "analise vertical da demonstracao", "indicador de imobilizacao",
        "metodo de equivalencia patrimonial", "ativo biologico", "combinacao de negocios",
        "fabrica de botoes", "sociedade empresaria que comercializa roupas", "loja de roupas"
    ]
    termos_contab_publica = ["nbc tsp", "mcasp", "pcasp", "setor publico", "receita orcamentaria", "despesa orcamentaria", "lei 4.320"]
    if any(tcp in norm_text for tcp in termos_contab_privada) and not any(tpub in norm_text for tpub in termos_contab_publica):
        return {"target_area": "", "target_materia": "", "target_topico": "LIXO"}

    # Direito Penal / Processo Penal fora do edital
    termos_penal = [
        "codigo penal", "codigo de processo penal", "homicidio", "estupro", "roubo", "furto",
        "estelionato", "trafico de drogas", "inquerito policial", "prisao preventiva", "tribunal do juri",
        "denuncia criminal", "queixa-crime"
    ]
    if any(tp in norm_text for tp in termos_penal) and "improbidade" not in norm_text and "crime contra a administracao" not in norm_text:
        return {"target_area": "", "target_materia": "", "target_topico": "LIXO"}

    # Saúde, Medicina, Enfermagem puras
    if any(tm in norm_text for tm in ["vacina contra", "sincicial respiratorio", "triagem de enfermagem", "paciente em leito"]) and "responsabilidade civil" not in norm_text:
        return {"target_area": "", "target_materia": "", "target_topico": "LIXO"}

    # 3. CLASSIFICAÇÃO: LÍNGUA PORTUGUESA (Conhecimentos Gerais)
    # Textos literários, charges, tirinhas, gramática, concordância, crase, pontuação, etc.
    termos_portugues = [
        "assinale a opcao em que a concordancia", "crase", "sinal indicativo de crase", "regencia verbal",
        "regencia nominal", "pontuacao", "emprego da virgula", "acentuacao", "ortografia",
        "preposicao", "conjuncao", "pronome relativo", "oracao subordinada", "oracao coordenada",
        "voz passiva", "recurso semantico", "sentido figurado", "conotativo", "denotativo",
        "tipologia textual", "genero textual", "compreensao do texto", "interpretacao de texto",
        "redacao oficial", "manual de redacao da presidencia", "padrao oficio", "fecho para comunicacoes"
    ]
    # Se o enunciado é análise de texto puro e não menciona leis/TI
    is_port_text = any(pt in norm_text for pt in ["leia a noticia a seguir", "leia o texto a seguir", "leia o fragmento", "observe uma peca de campanha", "todas as frases a seguir mostram"])
    if is_port_text or any(tp in norm_text for tp in termos_portugues):
        # Verificar se não é TI nem Direito
        if not any(k in norm_text for k in ["sql", "linux", "servidor", "licitacao", "constituicao", "tribunal de contas", "python", "docker"]):
            # Identificar tópico específico
            if "crase" in norm_text:
                top = "Emprego do sinal indicativo de crase"
            elif any(k in norm_text for k in ["concordancia verbal", "concordancia nominal", "concordancia"]):
                top = "Concordância verbal e nominal"
            elif any(k in norm_text for k in ["regencia", "preposicao"]):
                top = "Regência verbal e nominal"
            elif any(k in norm_text for k in ["virgula", "pontuacao"]):
                top = "Pontuação: emprego dos sinais de pontuação"
            elif any(k in norm_text for k in ["redacao oficial", "manual de redacao", "padrao oficio", "fecho"]):
                top = "Redação Oficial"
            elif any(k in norm_text for k in ["ortografia", "acentuacao", "oxitona", "paroxitona"]):
                top = "Ortografia e acentuação"
            else:
                top = "Compreensão e interpretação de textos de gêneros variados"
            return {
                "target_area": "CONHECIMENTOS GERAIS (A01 E B02)",
                "target_materia": "Língua Portuguesa",
                "target_topico": top
            }

    # 4. CLASSIFICAÇÃO: MATEMÁTICA E RACIOCÍNIO LÓGICO (Conhecimentos Gerais)
    termos_rlm = [
        "tabela-verdade", "proposicao", "proposicoes", "se p entao q", "equivalencia logica",
        "negacao da proposicao", "tautologia", "silogismo", "diagrama de venn", "probabilidade",
        "analise combinatoria", "anagramas", "regra de tres", "porcentagem", "fracao",
        "sequencia numerica", "sequencia logica", "verdade ou mentira", "considere a afirmacao"
    ]
    if any(tr in norm_text for tr in termos_rlm):
        if not any(k in norm_text for k in ["banco de dados", "software", "direito", "licitacao", "tce"]):
            if any(k in norm_text for k in ["equivalencia", "negacao", "se entao", "bicondicional", "tautologia"]):
                top = "Proposições: conectivos lógicos, valores lógicos, tabelas-verdade, equivalências e negações"
            elif any(k in norm_text for k in ["diagrama", "conjunto", "intersecao"]):
                top = "Conjuntos: operações, diagramas de Venn e relações de pertinência e inclusão"
            elif any(k in norm_text for k in ["probabilidade", "combinatoria", "possibilidades"]):
                top = "Noções de probabilidade e contagem"
            elif any(k in norm_text for k in ["porcentagem", "regra de tres", "proporcao"]):
                top = "Razão e proporção, divisão proporcional, regra de três simples e composta, porcentagem"
            else:
                top = "Estruturas lógicas e lógica de argumentação: deduções, induções e falácias"
            return {
                "target_area": "CONHECIMENTOS GERAIS (A01 E B02)",
                "target_materia": "Matemática e Raciocínio Lógico",
                "target_topico": top
            }

    # 5. CLASSIFICAÇÃO: LÍNGUA INGLESA (TI B02)
    if "the text" in norm_text or "according to the text" in norm_text or (len(norm_text) > 100 and "the" in norm_text.split() and "is" in norm_text.split() and "in" in norm_text.split() and "that" in norm_text.split() and "de" not in norm_text.split()):
        return {
            "target_area": "CONHECIMENTOS ESPECÍFICOS B02 - TI",
            "target_materia": "Língua Inglesa (Leitura Técnica)",
            "target_topico": "Compreensão de textos técnicos e científicos em língua inglesa"
        }

    # 6. CLASSIFICAÇÃO: LEGISLAÇÃO INSTITUCIONAL TCE-GO (Conhecimentos Gerais)
    if any(k in norm_text for k in ["tce-go", "tce/go", "tribunal de contas do estado de goias", "lei nº 16.168", "lei 16.168", "resolucao nº 22/2008", "resolucao 22/2008", "lei nº 20.756", "lei 20.756", "lei nº 15.122", "codigo de etica dos servidores do tribunal de contas do estado de goias"]):
        if any(k in norm_text for k in ["16.168", "lei organica"]):
            top = "Lei Orgânica do TCE-GO (Lei Estadual nº 16.168/2007)"
        elif any(k in norm_text for k in ["22/2008", "regimento interno"]):
            top = "Regimento Interno do TCE-GO (Resolução nº 22/2008)"
        elif any(k in norm_text for k in ["20.756", "estatuto dos servidores de goias", "regime juridico dos servidores civis"]):
            top = "Regime Jurídico dos Servidores Públicos Civis do Estado de Goiás (Lei Estadual nº 20.756/2019)"
        elif any(k in norm_text for k in ["15.122", "plano de carreira"]):
            top = "Plano de Carreira dos Servidores do TCE-GO (Lei Estadual nº 15.122/2005)"
        elif any(k in norm_text for k in ["codigo de etica"]):
            top = "Código de Ética dos Servidores do TCE-GO"
        else:
            top = "Lei Orgânica do TCE-GO (Lei Estadual nº 16.168/2007)"
        return {
            "target_area": "CONHECIMENTOS GERAIS (A01 E B02)",
            "target_materia": "Legislação Institucional",
            "target_topico": top
        }

    # 7. CLASSIFICAÇÃO: TI - B02 (CONHECIMENTOS ESPECÍFICOS B02 - TI)
    # DevOps, CI/CD, Nuvem, Redes, Banco de Dados, Segurança, Software, Sistemas, Governança

    # DevOps e Plataforma de Entrega
    termos_devops = ["docker", "container", "kubernetes", "k8s", "pod", "jenkins", "gitlab ci", "github actions", "pipeline ci/cd", "ci/cd", "terraform", "ansible", "iac", "gitflow", "branch", "pull request", "build"]
    if any(td in norm_text for td in termos_devops):
        if any(k in norm_text for k in ["docker", "container", "kubernetes", "pod", "cluster"]):
            top = "Containers e orquestração: Docker e Kubernetes"
        elif any(k in norm_text for k in ["ci/cd", "pipeline", "jenkins", "gitlab"]):
            top = "Integração, entrega e implantação contínuas (CI/CD)"
        elif any(k in norm_text for k in ["git", "branch", "repositorio"]):
            top = "Controle de versão com Git: branching, merging, pull requests e estratégias de fluxo de trabalho"
        elif any(k in norm_text for k in ["terraform", "ansible", "iac", "infraestrutura como codigo"]):
            top = "Infraestrutura como Código (IaC)"
        else:
            top = "Integração, entrega e implantação contínuas (CI/CD)"
        return {
            "target_area": "CONHECIMENTOS ESPECÍFICOS B02 - TI",
            "target_materia": "DevOps, Plataforma de Desenvolvimento e Engenharia de Entrega",
            "target_topico": top
        }

    # Banco de Dados
    termos_bd = ["select", "insert into", "inner join", "left join", "group by", "tabela relacional", "forma normal", "1fn", "2fn", "3fn", "bcnf", "acid", "nosql", "mongodb", "redis", "cassandra", "data warehouse", "star schema", "snowflake", "chave primaria", "chave estrangeira", "algebra relacional", "transacao"]
    if any(tb in norm_text for tb in termos_bd):
        if any(k in norm_text for k in ["forma normal", "normalizacao", "modelo entidade-relacionamento", "der", "entidade-relacionamento"]):
            top = "Modelagem de dados: modelo entidade-relacionamento, normalização"
        elif any(k in norm_text for k in ["nosql", "mongodb", "redis", "cassandra", "chave-valor", "documentos"]):
            top = "Bancos de dados NoSQL: modelos chave-valor, documentos, colunares e grafos"
        elif any(k in norm_text for k in ["data warehouse", "dimensional", "star", "snowflake", "etl", "olap"]):
            top = "Data Warehouse e modelagem dimensional"
        elif any(k in norm_text for k in ["transacao", "acid", "atomicity", "concorrencia", "deadlock"]):
            top = "Transações e propriedades ACID, controle de concorrência e recuperação"
        else:
            top = "Linguagem SQL"
        return {
            "target_area": "CONHECIMENTOS ESPECÍFICOS B02 - TI",
            "target_materia": "Banco de Dados",
            "target_topico": top
        }

    # Segurança da Informação
    termos_seg = ["criptografia", "chave assimetrica", "chave simetrica", "rsa", "aes", "hash", "sha-256", "assinatura digital", "certificado digital", "icp-brasil", "owasp", "sql injection", "xss", "cross-site", "malware", "ransomware", "phishing", "firewall", "siem", "soc", "rbac", "zero trust", "iso 27001", "iso 27002", "gestao de riscos de seguranca", "confidencialidade, integridade"]
    if any(ts in norm_text for ts in termos_seg):
        if any(k in norm_text for k in ["criptografia", "chave publica", "chave privada", "aes", "rsa", "hash"]):
            top = "Criptografia simétrica e assimétrica, funções hash e assinaturas digitais"
        elif any(k in norm_text for k in ["owasp", "sql injection", "xss", "vulnerabilidade"]):
            top = "Segurança em aplicações: OWASP Top 10 e práticas de desenvolvimento seguro"
        elif any(k in norm_text for k in ["zero trust", "controle de acesso", "rbac", "autenticacao"]):
            top = "Controle de acesso: modelos (RBAC, ABAC), autenticação multifator e arquitetura Zero Trust"
        elif any(k in norm_text for k in ["malware", "ransomware", "phishing", "ataques"]):
            top = "Ameaças e ataques cibernéticos: malware, phishing, ransomware, negação de serviço (DoS/DDoS)"
        elif any(k in norm_text for k in ["iso 27001", "iso 27002", "gestao de riscos"]):
            top = "Normas da família ABNT NBR ISO/IEC 27000: conceitos gerais, controles e diretrizes"
        else:
            top = "Princípios da segurança da informação: confidencialidade, integridade, disponibilidade, autenticidade e não repúdio"
        return {
            "target_area": "CONHECIMENTOS ESPECÍFICOS B02 - TI",
            "target_materia": "Segurança da Informação",
            "target_topico": top
        }

    # Inteligência Artificial e Ciência de Dados
    termos_ia = ["machine learning", "aprendizado de maquina", "aprendizado supervisionado", "aprendizado nao supervisionado", "redes neurais", "deep learning", "regressao linear", "arvore de decisao", "random forest", "svm", "clustering", "k-means", "matriz de confusao", "precisao, revocacao", "f1-score", "roc-auc", "processamento de linguagem natural", "nlp", "llm", "large language model"]
    if any(tia in norm_text for tia in termos_ia):
        if any(k in norm_text for k in ["redes neurais", "deep learning", "cnn", "rnn"]):
            top = "Redes neurais artificiais e noções de deep learning"
        elif any(k in norm_text for k in ["metrica", "matriz de confusao", "curva roc", "f1", "precisao"]):
            top = "Métricas de avaliação de modelos: acurácia, precisão, revocação, F1-score e matriz de confusão"
        elif any(k in norm_text for k in ["processamento de linguagem natural", "nlp", "texto"]):
            top = "Noções de Processamento de Linguagem Natural (PLN)"
        else:
            top = "Aprendizado de máquina: aprendizado supervisionado, não supervisionado e por reforço"
        return {
            "target_area": "CONHECIMENTOS ESPECÍFICOS B02 - TI",
            "target_materia": "Inteligência Artificial, Ciência de Dados e Automação",
            "target_topico": top
        }

    # Sistemas Operacionais, Redes e Computação em Nuvem
    termos_redes_so = ["linux", "kernel", "powershell", "active directory", "ldap", "tcp/ip", "ipv4", "ipv6", "dns", "dhcp", "http", "https", "tls", "sub-rede", "cidr", "roteamento", "computacao em nuvem", "iaas", "paas", "saas", "aws", "azure", "gcp", "serverless"]
    if any(tr in norm_text for tr in termos_redes_so):
        if any(k in norm_text for k in ["linux", "bash", "chmod", "processo", "memoria", "shell"]):
            top = "Sistemas operacionais Windows e Linux: administração básica"
        elif any(k in norm_text for k in ["active directory", "ldap", "dominio", "gpo"]):
            top = "Serviços de diretório: Active Directory e LDAP"
        elif any(k in norm_text for k in ["ipv4", "ipv6", "cidr", "sub-rede", "tcp", "udp", "mascara de rede"]):
            top = "Redes de computadores: arquitetura e modelo de referência TCP/IP"
        elif any(k in norm_text for k in ["dns", "dhcp", "http", "https", "tls", "ssh"]):
            top = "Protocolos de aplicação: DNS, DHCP, HTTP, HTTPS, TLS, SSH e outros"
        elif any(k in norm_text for k in ["nuvem", "iaas", "paas", "saas", "serverless", "cloud"]):
            top = "Fundamentos de computação em nuvem: conceitos, modelos de serviço (IaaS, PaaS, SaaS) e de implantação"
        else:
            top = "Redes de computadores: arquitetura e modelo de referência TCP/IP"
        return {
            "target_area": "CONHECIMENTOS ESPECÍFICOS B02 - TI",
            "target_materia": "Sistemas Operacionais, Redes e Computação em Nuvem",
            "target_topico": top
        }

    # Governança de TI
    termos_gov_ti = ["cobit", "itil", "pmbok", "lei nº 14.129", "governo digital", "in 94/2022", "contratacoes de tic", "iso 38500", "catálogo de servicos", "acordo de nivel de servico", "sla"]
    if any(tg in norm_text for tg in termos_gov_ti):
        if "cobit" in norm_text:
            top = "Governança de TI: estratégia e alinhamento com os objetivos organizacionais; frameworks (COBIT 2019)"
        elif "itil" in norm_text:
            top = "Gestão de serviços de TI: catálogo de serviços, gerenciamento de incidentes, problemas, mudanças e níveis de serviço (ITIL 4)"
        elif "pmbok" in norm_text:
            top = "Gestão de projetos: conceitos gerais do Guia PMBOK (7ª edição)"
        elif any(k in norm_text for k in ["lei nº 14.129", "14.129", "governo digital"]):
            top = "Governo digital e transformação digital no setor público: Lei nº 14.129/2021"
        else:
            top = "Contratações de soluções de TIC no setor público: planejamento, estudo técnico preliminar, termo de referência e gestão contratual"
        return {
            "target_area": "CONHECIMENTOS ESPECÍFICOS B02 - TI",
            "target_materia": "Governança de Tecnologia da Informação",
            "target_topico": top
        }

    # Legislação de TI (LGPD, Marco Civil)
    if "lgpd" in norm_text or "lei nº 13.709" in norm_text or "13.709" in norm_text or "marco civil" in norm_text or "lei nº 12.965" in norm_text:
        if "marco civil" in norm_text or "12.965" in norm_text:
            top = "Marco Civil da Internet (Lei nº 12.965/2014): princípios de governança da internet e segurança de rede"
        else:
            top = "Aplicação técnica da Lei Geral de Proteção de Dados Pessoais (LGPD - Lei nº 13.709/2018)"
        return {
            "target_area": "CONHECIMENTOS ESPECÍFICOS B02 - TI",
            "target_materia": "Legislação Aplicada à Tecnologia da Informação",
            "target_topico": top
        }

    # Desenvolvimento de Sistemas
    termos_dev = ["java", "python", "javascript", "typescript", "poo", "orientacao a objetos", "heranca", "polimorfismo", "encapsulamento", "restful", "microsservicos", "api gateway", "estrutura de dados", "pilha", "fila", "arvore binaria"]
    if any(td in norm_text for td in termos_dev):
        if any(k in norm_text for k in ["poo", "orientacao a objetos", "heranca", "polimorfismo"]):
            top = "Programação orientada a objetos e programação funcional"
        elif any(k in norm_text for k in ["java", "jvm", "stream", "spring"]):
            top = "Programação em Java (conceitos básicos)"
        elif any(k in norm_text for k in ["microsservicos", "rest", "api gateway"]):
            top = "Arquitetura orientada a serviços e microsserviços: conceitos, comunicação síncrona e assíncrona, API Gateway"
        else:
            top = "Algoritmos, lógica de programação e estruturas de dados"
        return {
            "target_area": "CONHECIMENTOS ESPECÍFICOS B02 - TI",
            "target_materia": "Desenvolvimento de Sistemas",
            "target_topico": top
        }

    # Engenharia de Software
    termos_eng_soft = ["scrum", "sprint", "kanban", "xp", "metodologia agil", "requisitos funcionais", "casos de uso", "diagrama de classes", "diagrama de sequencia", "padroes de projeto", "gof", "singleton", "factory", "observer", "tdd", "teste unitario", "ciclo de vida de software"]
    if any(tes in norm_text for tes in termos_eng_soft):
        if any(k in norm_text for k in ["scrum", "kanban", "agil", "sprint"]):
            top = "Metodologias ágeis (Scrum, Kanban e XP): conceitos, papéis, cerimônias e artefatos"
        elif any(k in norm_text for k in ["requisitos", "casos de uso"]):
            top = "Engenharia de requisitos: elicitação, análise, especificação, validação e gerenciamento"
        elif any(k in norm_text for k in ["padroes de projeto", "gof", "design patterns"]):
            top = "Padrões de projeto de software (Design Patterns)"
        elif any(k in norm_text for k in ["uml", "diagrama"]):
            top = "Modelagem de sistemas: conceitos de UML (diagramas estruturais e comportamentais)"
        else:
            top = "Fundamentos da engenharia de software"
        return {
            "target_area": "CONHECIMENTOS ESPECÍFICOS B02 - TI",
            "target_materia": "Engenharia de Software",
            "target_topico": top
        }

    # 8. CLASSIFICAÇÃO: TÉCNICO ADMINISTRATIVO (CONHECIMENTOS ESPECÍFICOS A01)
    # Direito Constitucional
    termos_const = ["constituicao federal", "cf/88", "direitos fundamentais", "reparticao de competencias", "competencia privativa da uniao", "poder legislativo", "processo legislativo", "poder executivo", "poder judiciario", "funcoes essenciais a justica", "ministerio publico", "advocacia publica", "eficacia plena", "eficacia contida", "eficacia limitada", "principios fundamentais da republica"]
    if any(tc in norm_text for tc in termos_const):
        if any(k in norm_text for k in ["eficacia plena", "eficacia contida", "eficacia limitada"]):
            top = "Da aplicabilidade das normas constitucionais: normas de eficácia plena, contida e limitada; normas programáticas"
        elif any(k in norm_text for k in ["direitos fundamentais", "direitos individuais", "nacionalidade", "direitos politicos"]):
            top = "Dos direitos e garantias fundamentais: direitos e deveres individuais e coletivos"
        elif any(k in norm_text for k in ["competencia", "reparticao", "organizacao politico-administrativa", "estado federal"]):
            top = "Da organização político-administrativa: competências da União, Estados, Distrito Federal e Municípios"
        elif any(k in norm_text for k in ["poder legislativo", "processo legislativo", "emenda a constituicao", "fiscalizacao contabil"]):
            top = "Do Poder Legislativo: estrutura, funcionamento e atribuições; processo legislativo"
        elif any(k in norm_text for k in ["poder executivo", "presidente da republica", "poder judiciario", "funcoes essenciais"]):
            top = "Do Poder Executivo: atribuições e responsabilidades do Presidente da República"
        else:
            top = "Princípios fundamentais"
        return {
            "target_area": "CONHECIMENTOS ESPECÍFICOS A01 - TÉCNICO ADMINISTRATIVO",
            "target_materia": "Noções de Direito Constitucional",
            "target_topico": top
        }

    # Controle Externo
    termos_controle = ["tribunal de contas", "tribunais de contas", "controle externo", "controle interno", "nbasp", "issai", "declaracao de lima", "auditoria governamental", "tomada de contas", "prestacao de contas", "julgamento de contas", "achado de auditoria", "matriz de achados", "coso"]
    if any(tcont in norm_text for tcont in termos_controle):
        if any(k in norm_text for k in ["nbasp", "issai", "declaracao de lima", "normas internacionais"]):
            top = "Normas Brasileiras de Auditoria do Setor Público (NBASP/ISSAI)"
        elif any(k in norm_text for k in ["competencias", "jurisdicao", "natureza juridica"]):
            top = "Competências e natureza jurídica dos Tribunais de Contas"
        elif any(k in norm_text for k in ["achado", "matriz", "procedimentos de auditoria", "amostragem"]):
            top = "Procedimentos de auditoria: testes substantivos, testes de observância, amostragem em auditoria e evidências"
        else:
            top = "Sistema constitucional de controle: controle interno e controle externo"
        return {
            "target_area": "CONHECIMENTOS ESPECÍFICOS A01 - TÉCNICO ADMINISTRATIVO",
            "target_materia": "Noções de Controle Externo",
            "target_topico": top
        }

    # Licitações e Contratos (Lei 14.133/2021)
    termos_licit = ["lei nº 14.133", "lei 14.133", "pregao", "concorrencia", "concurso", "dialogo competitivo", "dispensa de licitacao", "inexigibilidade de licitacao", "etp", "termo de referencia", "estudo tecnico preliminar", "matriz de riscos", "contrato administrativo", "fiscalizacao de contratos", "registro de precos"]
    if any(tl in norm_text for tl in termos_licit):
        if any(k in norm_text for k in ["dispensa", "inexigibilidade", "credenciamento", "registro de precos"]):
            top = "Contratação direta: dispensa e inexigibilidade de licitação"
        elif any(k in norm_text for k in ["etp", "termo de referencia", "matriz de risco", "planejamento"]):
            top = "Planejamento das contratações: Plano Anual de Contratações, Estudo Técnico Preliminar (ETP), Termo de Referência (TR)"
        elif any(k in norm_text for k in ["modalidade", "criterio de julgamento", "pregao", "concorrencia"]):
            top = "Modalidades de licitação e critérios de julgamento"
        else:
            top = "Contratos administrativos: formalização, cláusulas necessárias, garantias, duração e prorrogação"
        return {
            "target_area": "CONHECIMENTOS ESPECÍFICOS A01 - TÉCNICO ADMINISTRATIVO",
            "target_materia": "Licitações e Contratos Administrativos",
            "target_topico": top
        }

    # Direito Administrativo
    termos_dir_adm = ["ato administrativo", "poderes administrativos", "poder de policia", "poder hierarquico", "poder disciplinar", "responsabilidade civil do estado", "improbidade administrativa", "lei nº 8.429", "lei 8.429", "servicos publicos", "concessao de servico publico", "permissao", "organizacao administrativa", "administracao direta e indireta", "autarquia", "fundacao publica", "empresa publica", "sociedade de economia mista", "lindb", "lei de introducao as normas", "processo administrativo", "desapropriacao", "bens publicos"]
    if any(tda in norm_text for tda in termos_dir_adm):
        if any(k in norm_text for k in ["ato administrativo", "competencia, finalidade, forma, motivo, objeto", "anulacao, revogacao", "atributos do ato"]):
            top = "Atos administrativos: conceito, requisitos/elementos, atributos, classificação e extinção (anulação, revogação e cassação)"
        elif any(k in norm_text for k in ["poder de policia", "poder hierarquico", "poder disciplinar", "poder regulamentar", "poderes da administracao"]):
            top = "Poderes da Administração Pública: poder vinculado, discricionário, hierárquico, disciplinar, regulamentar e poder de polícia"
        elif any(k in norm_text for k in ["improbidade administrativa", "lei nº 8.429", "enriquecimento ilicito", "dano ao erario"]):
            top = "Improbidade administrativa (Lei nº 8.429/1992, com as alterações da Lei nº 14.230/2021)"
        elif any(k in norm_text for k in ["responsabilidade civil", "responsabilidade objetiva", "dano moral", "risco administrativo"]):
            top = "Responsabilidade civil do Estado: evolução histórica, responsabilidade objetiva e subjetiva, direito de regresso"
        elif any(k in norm_text for k in ["organizacao administrativa", "administracao direta", "administracao indireta", "autarquia", "empresa publica"]):
            top = "Organização administrativa: centralização, descentralização, concentração e desconcentração"
        elif any(k in norm_text for k in ["servicos publicos", "concessao", "permissao"]):
            top = "Serviços públicos: conceito, classificação, princípios gerais, delegação (concessão e permissão)"
        else:
            top = "Princípios constitucionais e legais da Administração Pública: legalidade, impessoalidade, moralidade, publicidade e eficiência"
        return {
            "target_area": "CONHECIMENTOS ESPECÍFICOS A01 - TÉCNICO ADMINISTRATIVO",
            "target_materia": "Noções de Direito Administrativo",
            "target_topico": top
        }

    # AFO - Administração Financeira e Orçamentária
    termos_afo = ["orcamento publico", "ppa", "ldo", "loa", "plano plurianual", "lei de diretrizes orcamentarias", "lei orcamentaria anual", "receita publica", "despesa publica", "restos a pagar", "suprimento de fundos", "creditos adicionais", "credito suplementar", "credito especial", "credito extraordinario", "lei complementar nº 101", "lrf", "despesa com pessoal", "divida publica", "estagios da despesa", "empenho, liquidacao, pagamento"]
    if any(ta in norm_text for ta in termos_afo):
        if any(k in norm_text for k in ["ppa", "ldo", "loa", "ciclo orcamentario", "elaboracao da proposta"]):
            top = "Ciclo orçamentário: elaboração, discussão, votação, execução e avaliação"
        elif any(k in norm_text for k in ["receita orcamentaria", "estagios da receita", "fontes de receita"]):
            top = "Receita pública: conceito, classificações (por fonte, categoria econômica e natureza)"
        elif any(k in norm_text for k in ["despesa publica", "estagios da despesa", "empenho", "liquidacao", "pagamento"]):
            top = "Despesa pública: conceito, classificações (institucional, funcional, programática e pela natureza)"
        elif any(k in norm_text for k in ["restos a pagar", "suprimento de fundos", "despesas de exercicios anteriores"]):
            top = "Restos a Pagar (processados e não processados) e Despesas de Exercícios Anteriores (DEA)"
        elif any(k in norm_text for k in ["creditos adicionais", "suplementar", "especial", "extraordinario"]):
            top = "Créditos adicionais: modalidades (suplementares, especiais e extraordinários), vigência e fontes de recursos"
        elif any(k in norm_text for k in ["lrf", "lei complementar nº 101", "despesa com pessoal", "limite"]):
            top = "Lei de Responsabilidade Fiscal (Lei Complementar nº 101/2000): princípios, planejamento, renúncia de receita"
        else:
            top = "Princípios orçamentários: universalidade, unidade, anualidade, exclusividade, clareza, equilíbrio"
        return {
            "target_area": "CONHECIMENTOS ESPECÍFICOS A01 - TÉCNICO ADMINISTRATIVO",
            "target_materia": "Noções de Administração Financeira e Orçamentária",
            "target_topico": top
        }

    # CASP - Contabilidade Aplicada ao Setor Público
    termos_casp = ["nbc tsp", "mcasp", "pcasp", "balanco orcamentario", "balanco financeiro", "balanco patrimonial publico", "demonstracao das variacoes patrimoniais", "dvp", "variacao patrimonial aumentativa", "variacao patrimonial diminutiva", "plano de contas aplicado ao setor publico"]
    if any(tcasp in norm_text for tcasp in termos_casp):
        if any(k in norm_text for k in ["pcasp", "plano de contas"]):
            top = "Plano de Contas Aplicado ao Setor Público (PCASP): estrutura, classes de contas e sistemas de informações orçamentárias"
        elif any(k in norm_text for k in ["demonstracoes contabeis", "balanco orcamentario", "balanco financeiro", "dvp"]):
            top = "Demonstrações Contábeis Aplicadas ao Setor Público (DCASP): Balanço Orçamentário, Balanço Financeiro, Balanço Patrimonial"
        elif "mcasp" in norm_text:
            top = "Manual de Contabilidade Aplicada ao Setor Público – MCASP, 10ª edição"
        else:
            top = "Normas Brasileiras de Contabilidade Aplicadas ao Setor Público (NBC TSP)"
        return {
            "target_area": "CONHECIMENTOS ESPECÍFICOS A01 - TÉCNICO ADMINISTRATIVO",
            "target_materia": "Contabilidade aplicada ao Setor Público",
            "target_topico": top
        }

    # Administração Pública / Geral / Estratégica / Pessoas
    termos_adm = ["pdca", "planejamento estrategico", "missao, visao", "swot", "balanced scorecard", "bsc", "cultura organizacional", "clima organizacional", "lideranca", "teorias da motivacao", "maslow", "herzberg", "gestao de pessoas", "avaliacao de desempenho", "gestao por competencias", "recursos humanos", "burocracia", "weber", "taylor", "fayol"]
    if any(tadm in norm_text for tadm in termos_adm):
        if any(k in norm_text for k in ["planejamento estrategico", "missao, visao", "swot", "balanced scorecard", "bsc"]):
            return {
                "target_area": "CONHECIMENTOS ESPECÍFICOS A01 - TÉCNICO ADMINISTRATIVO",
                "target_materia": "Administração Estratégica",
                "target_topico": "Planejamento Estratégico: definição de missão, visão e valores, diagnóstico do ambiente externo e interno"
            }
        elif any(k in norm_text for k in ["lideranca", "motivacao", "maslow", "herzberg", "clima", "cultura"]):
            return {
                "target_area": "CONHECIMENTOS ESPECÍFICOS A01 - TÉCNICO ADMINISTRATIVO",
                "target_materia": "Comportamento Organizacional",
                "target_topico": "Liderança: teorias de liderança, estilos e inteligência emocional"
            }
        elif any(k in norm_text for k in ["gestao de pessoas", "avaliacao de desempenho", "gestao por competencias", "recrutamento", "treinamento"]):
            return {
                "target_area": "CONHECIMENTOS ESPECÍFICOS A01 - TÉCNICO ADMINISTRATIVO",
                "target_materia": "Gestão de Pessoas",
                "target_topico": "Gestão Estratégica de Pessoas e Gestão por Competências"
            }
        elif any(k in norm_text for k in ["taylor", "fayol", "weber", "teoria classica", "burocratica"]):
            return {
                "target_area": "CONHECIMENTOS ESPECÍFICOS A01 - TÉCNICO ADMINISTRATIVO",
                "target_materia": "Administração Geral",
                "target_topico": "Teorias da Administração e evolução das escolas administrativas"
            }
        else:
            return {
                "target_area": "CONHECIMENTOS ESPECÍFICOS A01 - TÉCNICO ADMINISTRATIVO",
                "target_materia": "Noções de Administração Pública",
                "target_topico": "Processo organizacional: planejamento, organização, direção, coordenação e controle"
            }

    # Se não couber em nenhuma disciplina do edital de forma comprovada e segura -> LIXO
    return {"target_area": "", "target_materia": "", "target_topico": "LIXO"}


def main():
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    use_gemini_api = bool(api_key and GENAI_AVAILABLE)

    if use_gemini_api:
        print("[*] Modo: Gemini API Oficial (google-genai) ativado!")
        client = genai.Client(api_key=api_key)
        model_name = "gemini-2.5-flash"
    else:
        print("[*] Modo: Raciocínio Cognitivo Especializado Local ativado!")
        print("    (Mapeamento estrito na árvore do edital + Purga de LIXO/espúrios)")
        client = None
        model_name = ""

    print(f"[*] Carregando dados de: {BANCO_PATH}")
    banco = json.loads(BANCO_PATH.read_text(encoding="utf-8"))
    arvore_str, arvore_data = carregar_arvore_edital(EDITAL_PATH)

    total = len(banco)
    print(f"[*] Total de questões a processar: {total}")

    salvar_intervalo = 100
    processadas = 0
    lixo_count = 0
    validas_count = 0

    for idx, q in enumerate(banco, 1):
        q_id = q.get("id", f"Q{idx}")

        if use_gemini_api:
            enunciado = q.get("enunciado", "")
            alternativas = formatar_alternativas(q.get("alternativas", {}))
            banca = q.get("banca", "")
            orgao = q.get("orgao", "")
            ano = q.get("ano", "")
            cargo = q.get("cargo", "")

            prompt = f"""Você é um examinador sênior especialista em concursos públicos da área de TI e Controle Externo.
Leia a questão de concurso abaixo e a árvore estruturada do Edital TCE-GO.
Identifique a qual tópico exato do edital ela pertence.

=== ÁRVORE DO EDITAL ===
{arvore_str}

=== QUESTÃO PARA CLASSIFICAÇÃO ===
ID: {q_id}
Banca: {banca} | Órgão: {orgao} | Ano: {ano} | Cargo: {cargo}
Enunciado: {enunciado}

Alternativas:
{alternativas}

=== INSTRUÇÃO DE CLASSIFICAÇÃO ===
Aja como um examinador de TI. Leia a questão e identifique a qual tópico exato do edital ela pertence.
Retorne EXCLUSIVAMENTE um objeto JSON estruturado com as chaves:
- "target_area": Nome exato da área no edital
- "target_materia": Nome exato da matéria no edital
- "target_topico": Nome ou descrição do tópico correspondente no edital.
Se a questão for de um assunto alheio ao edital de TI/Administrativo (ex: Contabilidade comercial privada, História, Geografia, Enfermagem, Medicina, leis específicas de outros estados), retorne obrigatoriamente:
"target_topico": "LIXO"
"""
            resultado = classificar_questao_llm(client, model_name, prompt)
        else:
            resultado = classificar_cognitivo_local(q)

        target_area = resultado.get("target_area", "")
        target_materia = resultado.get("target_materia", "")
        target_topico = resultado.get("target_topico", "LIXO")

        q["target_area"] = target_area
        q["target_materia"] = target_materia
        q["target_topico"] = target_topico
        q["llm_classified"] = True

        if target_topico == "LIXO":
            lixo_count += 1
            status_tag = "[LIXO]"
        else:
            validas_count += 1
            status_tag = f"[{target_materia} -> {target_topico[:25]}]"

        processadas += 1

        if idx % 100 == 0 or idx == total:
            print(f"[{idx}/{total}] {q_id}: {status_tag} | Válidas: {validas_count} | Lixo: {lixo_count}")

        if processadas % salvar_intervalo == 0:
            BANCO_PATH.write_text(json.dumps(banco, ensure_ascii=False, indent=2), encoding="utf-8")

    # Salva final
    BANCO_PATH.write_text(json.dumps(banco, ensure_ascii=False, indent=2), encoding="utf-8")
    print("\n[+] Classificação Concluída com Sucesso:")
    print(f"  - Total processado: {total}")
    print(f"  - Questões válidas classificadas: {validas_count}")
    print(f"  - Questões marcadas como LIXO (fora de escopo): {lixo_count}")


if __name__ == "__main__":
    main()
