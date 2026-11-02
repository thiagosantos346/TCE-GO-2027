#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
src/utils/chunk_semantic_router.py

Classificador Semântico Bottom-Up de Questões para o TCE-GO.
Processa os lotes em data/chunks_pendentes/, cruza os temas extraídos de enunciado
e alternativas com data/edital_estruturado.json, atribui a hierarquia exata
("target_area", "target_materia", "target_topico") ou define "target_topico": "DESCARTADA",
salva em data/chunks_processados/ e remove o lote da fila.
"""

import json
import os
import re
import sys
import unicodedata
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
EDITAL_PATH = BASE_DIR / "data" / "edital_estruturado.json"
PENDENTES_DIR = BASE_DIR / "data" / "chunks_pendentes"
PROCESSADOS_DIR = BASE_DIR / "data" / "chunks_processados"


def normalizar(texto: str) -> str:
    if not texto:
        return ""
    nfkd = unicodedata.normalize("NFKD", texto)
    sem_acento = "".join([c for c in nfkd if not unicodedata.combining(c)])
    return sem_acento.lower()


class PalavraInteira(str):
    """str cujo operador `in` casa termos como palavra inteira (plural s/es opcional).

    Evita falsos positivos de substring, ex.: 'pod' em 'podem', 'iac' em 'especialista'.
    """

    def __contains__(self, termo):
        padrao = r"(?<![a-z0-9])" + re.escape(termo) + r"(?:s|es)?(?![a-z0-9])"
        return re.search(padrao, str(self)) is not None


def carregar_edital():
    data = json.loads(EDITAL_PATH.read_text(encoding="utf-8"))
    catalogo = []
    
    for area in data.get("areas", []):
        nome_area = area["nome_area"]
        for mat in area.get("materias", []):
            nome_mat = mat["nome_materia"]
            for top in mat.get("topicos", []):
                catalogo.append({
                    "target_area": nome_area,
                    "target_materia": nome_mat,
                    "target_topico": top,
                    "norm_topico": normalizar(top)
                })
    return catalogo, data


def formatar_texto_questao(q: dict) -> str:
    enunciado = q.get("enunciado", "")
    alts = q.get("alternativas", {})
    if isinstance(alts, dict):
        alts_str = " ".join(f"{k}) {v}" for k, v in alts.items())
    elif isinstance(alts, list):
        alts_str = " ".join(alts)
    else:
        alts_str = str(alts)
    return f"{enunciado} {alts_str}"


def classificar_questao(q: dict, catalogo: list) -> dict:
    texto_completo = formatar_texto_questao(q)
    norm = PalavraInteira(normalizar(texto_completo))
    norm_cargo = normalizar(q.get("cargo", ""))
    norm_orgao = normalizar(q.get("orgao", ""))

    # -------------------------------------------------------------
    # 1. VERIFICAÇÃO DE DESCARTADA (Fora do Edital)
    # -------------------------------------------------------------

    # A) Legislações específicas de outros entes federativos / outros tribunais
    outros_tribunais_proibidos = [
        "santa catarina", "tj/sc", "tj-sc", "tce/sc", "tce-sc", "para", "tce/pa", "tce-pa",
        "piaui", "tce/pi", "tce-pi", "amapa", "tj/ap", "roraima", "tj/rr",
        "maranhao", "trt 16", "distrito federal e dos territorios", "tjdft"
    ]
    termos_estatutarios_locais = [
        "regimento interno", "lei organica", "estatuto dos servidores", "regime juridico unico",
        "plano de cargos", "codigo de divisao", "organizacao judiciaria", "orgao especial",
        "vara criminal", "comarca", "lei complementar estadual",
        "constituicao do estado do", "constituicao estadual do"
    ]
    is_goias = any(k in norm or k in norm_orgao for k in ["goias", "tce/go", "tce-go", "goiano"])
    if not is_goias:
        for est in outros_tribunais_proibidos:
            if est in norm or est in norm_orgao:
                if any(tl in norm for tl in termos_estatutarios_locais):
                    if not any(lf in norm for lf in ["14.133", "14133", "8.429", "8429", "12.846", "cf/88", "constituicao federal", "13.709", "lgpd"]):
                        return {"target_area": "", "target_materia": "", "target_topico": "DESCARTADA"}

    # B) Regimentos internos e códigos de ética específicos de outros tribunais federais/trts/stf
    if any(k in norm for k in ["comissao de etica do stf", "regimento interno do stf", "jurisprudencia do tribunal e para fixar a data da posse"]):
        return {"target_area": "", "target_materia": "", "target_topico": "DESCARTADA"}

    # C) Estatuto dos Servidores Federais (Lei 8.112/90) e penalidades/processo federal exclusivo
    if ("lei 8.112" in norm or "lei nº 8.112" in norm or "lei no 8.112" in norm or "lei 8112" in norm) and not any(k in norm for k in ["art. 37", "constituicao federal", "cf/88", "teto"]):
        return {"target_area": "", "target_materia": "", "target_topico": "DESCARTADA"}

    # D) Ramos jurídicos / técnicos não contemplados no edital
    # Meio ambiente
    if "servidao ambiental" in norm or "politica nacional do meio ambiente" in norm or "lei 6.938" in norm:
        return {"target_area": "", "target_materia": "", "target_topico": "DESCARTADA"}

    # Atuarial
    if "auditoria atuarial" in norm or "ciencias atuariais" in norm or "tabua de mortalidade" in norm or "deficit atuarial" in norm:
        return {"target_area": "", "target_materia": "", "target_topico": "DESCARTADA"}

    # Contabilidade privada comercial (CPCs de empresas privadas, balanço comercial privado sem CASP)
    termos_contab_privada = [
        "cpc 00", "cpc 01", "cpc 16", "cpc 25", "cpc 27", "cpc 48", "pronunciamento tecnico cpc",
        "demonstracao do resultado do exercicio", "dre", "acoes em tesouraria", "capital social subscrito",
        "lucro por acao", "analise vertical da demonstracao", "indicador de imobilizacao",
        "metodo de equivalencia patrimonial", "ativo biologico", "combinacao de negocios",
        "fabrica de botoes", "sociedade empresaria que comercializa roupas", "loja de roupas",
        "insumos quimicos", "alfa quimicas"
    ]
    termos_contab_publica = ["nbc tsp", "mcasp", "pcasp", "setor publico", "receita orcamentaria", "despesa orcamentaria", "lei 4.320"]
    if any(tcp in norm for tcp in termos_contab_privada) and not any(tpub in norm for tpub in termos_contab_publica):
        return {"target_area": "", "target_materia": "", "target_topico": "DESCARTADA"}

    # Direito Penal / Processo Penal fora do edital
    termos_penal = [
        "codigo penal", "codigo de processo penal", "homicidio", "estupro", "roubo", "furto",
        "estelionato", "trafico de drogas", "inquerito policial", "prisao preventiva", "tribunal do juri",
        "denuncia criminal", "queixa-crime"
    ]
    if any(tp in norm for tp in termos_penal) and "improbidade" not in norm and "crime contra a administracao" not in norm:
        return {"target_area": "", "target_materia": "", "target_topico": "DESCARTADA"}

    # Saúde e Medicina Clínica pura
    if any(tm in norm for tm in ["vacina contra", "sincicial respiratorio", "triagem de enfermagem", "paciente em leito"]) and "responsabilidade civil" not in norm:
        return {"target_area": "", "target_materia": "", "target_topico": "DESCARTADA"}

    # -------------------------------------------------------------
    # 2. CROSS-REFERENCE: MAPEAMENTO DIRETO NO EDITAL ESTRUTURADO
    # -------------------------------------------------------------

    # --- LÍNGUA INGLESA (TI B02) ---
    if "the text" in norm or "according to the text" in norm or (len(norm) > 80 and "the" in norm.split() and "is" in norm.split() and "in" in norm.split() and "that" in norm.split() and "de" not in norm.split()):
        return {
            "target_area": "CONHECIMENTOS ESPECÍFICOS B02 - TI",
            "target_materia": "Língua Inglesa (Leitura Técnica)",
            "target_topico": "Compreensão de textos técnicos e científicos em língua inglesa relacionados à tecnologia da informação"
        }

    # --- LÍNGUA PORTUGUESA (Conhecimentos Gerais) ---
    termos_portugues = [
        "assinale a opcao em que a concordancia", "crase", "sinal indicativo de crase", "regencia verbal",
        "regencia nominal", "pontuacao", "emprego da virgula", "acentuacao", "ortografia",
        "preposicao", "conjuncao", "pronome relativo", "oracao subordinada", "oracao coordenada",
        "voz passiva", "recurso semantico", "sentido figurado", "conotativo", "denotativo",
        "tipologia textual", "genero textual", "compreensao do texto", "interpretacao de texto",
        "redacao oficial", "manual de redacao da presidencia", "padrao oficio", "fecho para comunicacoes"
    ]
    is_port_text = any(pt in norm for pt in ["leia a noticia a seguir", "leia o texto a seguir", "leia o fragmento", "observe uma peca de campanha", "todas as frases a seguir mostram"])
    if is_port_text or any(tp in norm for tp in termos_portugues):
        if not any(k in norm for k in ["sql", "linux", "servidor", "licitacao", "constituicao", "tribunal de contas", "python", "docker", "pipeline", "rabbitmq", "kubernetes", "git"]):
            if any(k in norm for k in ["redacao oficial", "manual de redacao da presidencia", "padrao oficio", "fecho"]):
                top = "Redação Oficial"
            elif "crase" in norm:
                top = "Emprego do sinal indicativo de crase"
            elif any(k in norm for k in ["concordancia verbal", "concordancia nominal", "concordancia"]):
                top = "Concordância nominal e concordância verbal"
            elif any(k in norm for k in ["regencia", "preposicao"]):
                top = "Regência nominal e regência verbal"
            elif any(k in norm for k in ["virgula", "pontuacao"]):
                top = "Pontuação"
            elif any(k in norm for k in ["ortografia", "acentuacao"]):
                top = "Ortografia e acentuação"
            elif any(k in norm for k in ["pronome"]):
                top = "Pronomes"
            elif any(k in norm for k in ["coordenacao", "subordinacao", "oracao"]):
                top = "Coordenação e subordinação"
            elif any(k in norm for k in ["confronto e reconhecimento de frases", "reescrita", "equivalencia"]):
                top = "Redação (confronto e reconhecimento de frases corretas e incorretas"
            else:
                top = "Compreensão e interpretação de textos de gêneros variados"
            return {
                "target_area": "CONHECIMENTOS GERAIS (A01 E B02)",
                "target_materia": "Língua Portuguesa",
                "target_topico": top
            }

    # --- MATEMÁTICA E RACIOCÍNIO LÓGICO (Conhecimentos Gerais) ---
    termos_rlm = [
        "tabela-verdade", "proposicao", "proposicoes", "se p entao q", "equivalencia logica",
        "negacao da proposicao", "tautologia", "silogismo", "diagrama de venn", "probabilidade",
        "analise combinatoria", "regra de tres", "porcentagem", "fracao", "sequencia numerica",
        "sequencia logica", "verdade ou mentira", "considere a afirmacao"
    ]
    if any(tr in norm for tr in termos_rlm):
        if not any(k in norm for k in ["banco de dados", "software", "licitacao", "tce", "improbidade", "docker", "pipeline", "git"]):
            if any(k in norm for k in ["equivalencia", "negacao", "se entao", "bicondicional", "tautologia"]):
                top = "Raciocínio Lógico: Estrutura lógica de relações arbitrárias entre pessoas, lugares, objetos ou eventos fictícios"
            elif any(k in norm for k in ["porcentagem", "regra de tres", "proporcao", "razao"]):
                top = "porcentagem e problemas envolvendo regra de três simples, cálculos de porcentagem, acréscimos e descontos"
            elif any(k in norm for k in ["fracao", "fracoes", "numeros inteiros", "multiplos", "divisores"]):
                top = "Números inteiros e racionais: operações (adição, subtração, multiplicação, divisão, potenciação)"
            else:
                top = "Compreensão do processo lógico que, a partir de um conjunto de hipóteses, conduz, de forma válida, a conclusões determinadas"
            return {
                "target_area": "CONHECIMENTOS GERAIS (A01 E B02)",
                "target_materia": "Matemática e Raciocínio Lógico",
                "target_topico": top
            }

    # --- LEGISLAÇÃO INSTITUCIONAL TCE-GO (Conhecimentos Gerais) ---
    if any(k in norm for k in ["tce-go", "tce/go", "tribunal de contas do estado de goias", "16.168", "22/2008", "20.756", "15.122", "codigo de etica dos servidores do tribunal de contas do estado de goias"]):
        if "16.168" in norm or "lei organica" in norm:
            top = "Lei Orgânica do Tribunal de Contas do Estado de Goiás (Lei Estadual nº 16.168, de 11/12/2007)"
        elif "22/2008" in norm or "regimento interno" in norm:
            top = "Regimento Interno do Tribunal de Contas do Estado de Goiás (Resolução nº 22, de 04/09/2008, e alterações posteriores)"
        elif "20.756" in norm or "regime juridico dos servidores" in norm:
            top = "Regime Jurídico dos Servidores Públicos Civis do Estado de Goiás (Lei Estadual nº 20.756, de 28/01/2020)"
        elif "15.122" in norm or "plano de cargos" in norm:
            top = "Plano de Cargos, Carreiras e Remuneração dos Servidores do Tribunal de Contas do Estado de Goiás (Lei Estadual nº 15.122, de 04/02/2005)"
        elif "codigo de etica" in norm:
            top = "Código de Ética dos Servidores do Tribunal de Contas do Estado de Goiás"
        else:
            top = "Lei Orgânica do Tribunal de Contas do Estado de Goiás (Lei Estadual nº 16.168, de 11/12/2007)"
        return {
            "target_area": "CONHECIMENTOS GERAIS (A01 E B02)",
            "target_materia": "Legislação Institucional",
            "target_topico": top
        }

    # --- TI: DEVOPS, PLATAFORMA E ENTREGA (B02) ---
    termos_devops = [
        "docker", "container", "containers", "kubernetes", "k8s", "pod", "pods", "jenkins",
        "gitlab ci", "github actions", "pipeline ci/cd", "ci/cd", "continuous integration",
        "continuous delivery", "continuous deployment", "terraform", "ansible", "iac",
        "gitflow", "branching", "trunk-based", "git clone", "git branch", "git checkout",
        "git commit", "git push", "git pull", "repositorio git", "pull request", "merge request",
        "prometheus", "grafana", "observabilidade", "monitoramento de sistemas"
    ]
    if any(td in norm for td in termos_devops) or (re.search(r"\bgit\b", norm) and any(k in norm for k in ["comando", "branch", "repositorio", "clone", "commit"])):
        if any(k in norm for k in ["docker", "container", "containers", "kubernetes", "k8s", "pod", "pods", "cluster"]):
            top = "Conteinerização: Docker e Docker Compose"
        elif any(k in norm for k in ["ci/cd", "continuous integration", "continuous delivery", "continuous deployment", "jenkins", "gitlab ci", "github actions", "deploy"]):
            top = "Integração, entrega e implantação contínuas (CI/CD)"
        elif any(k in norm for k in ["terraform", "ansible", "iac", "infraestrutura como codigo"]):
            top = "Infraestrutura como código e gerenciamento de configuração"
        elif any(k in norm for k in ["git", "branch", "branching", "pull request", "merge request", "repositorio", "clone"]):
            top = "Controle de versão distribuído com Git"
        elif any(k in norm for k in ["prometheus", "grafana", "observabilidade", "metricas", "logs", "traces", "telemetria"]):
            top = "Observabilidade e monitoramento de sistemas: métricas, logs e traces"
        else:
            top = "Integração, entrega e implantação contínuas (CI/CD)"
        return {
            "target_area": "CONHECIMENTOS ESPECÍFICOS B02 - TI",
            "target_materia": "DevOps, Plataforma de Desenvolvimento e Engenharia de Entrega",
            "target_topico": top
        }

    # --- TI: BANCO DE DADOS (B02) ---
    termos_bd = [
        "select", "insert into", "inner join", "left join", "group by", "tabela relacional",
        "forma normal", "1fn", "2fn", "3fn", "bcnf", "acid", "nosql", "mongodb", "redis",
        "cassandra", "data warehouse", "star schema", "snowflake", "chave primaria",
        "chave estrangeira", "algebra relacional", "transacao", "procedimento armazenado", "trigger"
    ]
    if any(tb in norm for tb in termos_bd):
        if any(k in norm for k in ["forma normal", "normalizacao", "desnormalizacao", "modelo entidade-relacionamento", "der"]):
            top = "Modelagem de dados: modelo entidade-relacionamento, normalização e desnormalização"
        elif any(k in norm for k in ["nosql", "mongodb", "redis", "cassandra", "chave-valor", "documentos", "grafos", "colunas"]):
            top = "Bancos de dados NoSQL: modelos orientados a documentos, chave-valor, famílias de colunas (wide-column) e grafos"
        elif any(k in norm for k in ["transacao", "acid", "atomicidade", "concorrencia", "deadlock"]):
            top = "transações e propriedades ACID"
        elif any(k in norm for k in ["indice", "otimizacao de consulta", "plano de execucao"]):
            top = "Índices e otimização de consultas"
        elif any(k in norm for k in ["procedure", "trigger", "views"]):
            top = "Procedures, triggers e views"
        elif any(k in norm for k in ["postgresql", "oracle database"]):
            top = "Bancos relacionais: administração e otimização de PostgreSQL e Oracle Database"
        else:
            top = "Linguagem SQL"
        return {
            "target_area": "CONHECIMENTOS ESPECÍFICOS B02 - TI",
            "target_materia": "Banco de Dados",
            "target_topico": top
        }

    # --- TI: SEGURANÇA DA INFORMAÇÃO (B02) ---
    termos_seg = [
        "criptografia", "chave assimetrica", "chave simetrica", "rsa", "aes", "hash", "sha-256",
        "assinatura digital", "certificado digital", "icp-brasil", "owasp", "sql injection",
        "xss", "cross-site", "malware", "ransomware", "phishing", "firewall", "siem", "soc",
        "zero trust", "iso/iec 27000", "iso 27000", "iso 27001", "iso 27002", "iso/iec 27005", "27005",
        "confidencialidade, integridade", "autenticacao, autorizacao", "controle de acesso",
        "politica de controle de acesso", "gestao de riscos de seguranca"
    ]
    if any(ts in norm for ts in termos_seg):
        if any(k in norm for k in ["criptografia", "rsa", "aes", "chave publica", "chave privada", "funcao hash"]):
            top = "Criptografia simétrica e assimétrica"
        elif any(k in norm for k in ["owasp", "sql injection", "xss", "devsecops"]):
            top = "Segurança em aplicações: OWASP Top 10:2025"
        elif any(k in norm for k in ["zero trust"]):
            top = "Conceito de Zero Trust"
        elif any(k in norm for k in ["malware", "ransomware", "phishing", "engenharia social"]):
            top = "Malware, ransomware, phishing e engenharia social"
        elif any(k in norm for k in ["iso/iec 27000", "iso 27000", "iso 27001", "iso 27002"]):
            top = "Família de normas ABNT NBR ISO/IEC 27000 (gestão da segurança da informação)"
        elif any(k in norm for k in ["controle de acesso", "iam", "gestao de identidades", "politica de controle de acesso"]):
            top = "Controle de acesso: autenticação, autorização e gestão de identidades (IAM)"
        elif any(k in norm for k in ["certificado", "assinatura digital", "icp-brasil"]):
            top = "certificados e assinatura digital"
        elif any(k in norm for k in ["risco", "vulnerabilidade", "incidente", "27005", "gestao de riscos"]):
            top = "Gestão de riscos, de vulnerabilidades e de incidentes de segurança"
        else:
            top = "Princípios da segurança da informação: confidencialidade, integridade, disponibilidade, autenticidade e não repúdio"
        return {
            "target_area": "CONHECIMENTOS ESPECÍFICOS B02 - TI",
            "target_materia": "Segurança da Informação",
            "target_topico": top
        }

    # --- TI: INTELIGÊNCIA ARTIFICIAL E CIÊNCIA DE DADOS (B02) ---
    termos_ia = [
        "machine learning", "aprendizado de maquina", "aprendizado supervisionado",
        "aprendizado nao supervisionado", "redes neurais", "deep learning", "regressao linear",
        "arvore de decisao", "random forest", "svm", "clustering", "k-means", "matriz de confusao",
        "f1-score", "roc-auc", "processamento de linguagem natural", "nlp", "llm", "large language model",
        "rag", "inteligencia artificial generativa"
    ]
    if any(tia in norm for tia in termos_ia):
        if any(k in norm for k in ["redes neurais", "deep learning"]):
            top = "Redes neurais artificiais e noções de deep learning"
        elif any(k in norm for k in ["processamento de linguagem natural", "nlp"]):
            top = "Processamento de linguagem natural"
        elif any(k in norm for k in ["generativa", "llm", "large language"]):
            top = "Inteligência artificial generativa: conceitos e aplicações"
        elif any(k in norm for k in ["estatistica", "big data", "volume, velocidade"]):
            top = "fundamentos de Big Data, processamento distribuído e características de volume, velocidade e variedade dos dados"
        else:
            top = "Aprendizado de máquina: aprendizado supervisionado, não supervisionado e por reforço"
        return {
            "target_area": "CONHECIMENTOS ESPECÍFICOS B02 - TI",
            "target_materia": "Inteligência Artificial, Ciência de Dados e Automação",
            "target_topico": top
        }

    # --- TI: SISTEMAS OPERACIONAIS, REDES E NUVEM (B02) ---
    termos_so_redes = [
        "linux", "kernel", "powershell", "active directory", "ldap", "tcp/ip", "ipv4", "ipv6",
        "dns", "dhcp", "http/2", "http/3", "https", "sub-rede", "cidr", "computacao em nuvem",
        "iaas", "paas", "saas", "serverless", "ospf", "bgp", "vlan", "switch", "frame relay",
        "apache http server", "shell script", "endereco na internet", "caracteres http"
    ]
    if any(tr in norm for tr in termos_so_redes):
        if any(k in norm for k in ["linux", "bash", "processos", "memoria", "sistema de arquivos", "apache http server", "shell script"]):
            top = "Sistemas operacionais Windows e Linux: administração básica"
        elif any(k in norm for k in ["powershell", "shell"]):
            top = "Comandos básicos de shell (Linux) e do Windows PowerShell"
        elif any(k in norm for k in ["active directory", "ldap"]):
            top = "Serviços de diretório: Active Directory e LDAP"
        elif any(k in norm for k in ["ipv4", "ipv6", "cidr", "sub-rede", "tcp/ip", "ospf", "bgp", "vlan", "switch", "frame relay"]):
            top = "Redes de computadores: arquitetura TCP/IP, endereçamento IPv4 e IPv6, DNS e DHCP"
        elif any(k in norm for k in ["dns", "dhcp", "http", "https", "smtp", "ssh", "endereco na internet", "caracteres http"]):
            top = "protocolos HTTP/2, HTTP/3 e HTTPS, SMTP, FTP e SSH"
        elif any(k in norm for k in ["nuvem", "iaas", "paas", "saas", "serverless", "cloud"]):
            top = "Computação em nuvem: modelos IaaS, PaaS e SaaS"
        else:
            top = "Redes de computadores: arquitetura TCP/IP, endereçamento IPv4 e IPv6, DNS e DHCP"
        return {
            "target_area": "CONHECIMENTOS ESPECÍFICOS B02 - TI",
            "target_materia": "Sistemas Operacionais, Redes e Computação em Nuvem",
            "target_topico": top
        }

    # --- TI: GOVERNANÇA DE TI (B02) ---
    termos_gov = [
        "cobit", "itil", "pmbok", "lei nº 14.129", "lei no 14.129", "lei 14.129", "14129",
        "governo digital", "engd", "iso/iec 38500", "iso 38500", "38500", "catálogo de servicos",
        "gestao de incidentes, problemas"
    ]
    if any(tg in norm for tg in termos_gov):
        if any(k in norm for k in ["cobit", "itil", "38500"]):
            top = "Boas práticas e modelos de referência: COBIT 2019, ITIL v4 e ISO/IEC 38500:2024"
        elif "pmbok" in norm:
            top = "Gestão de projetos: fundamentos do PMBOK 8ª edição e de métodos ágeis aplicados a projetos de TI"
        elif any(k in norm for k in ["governo digital", "14.129", "14129", "engd"]):
            top = "Governo digital e transformação digital no setor público: Lei nº 14.129/2021 (Lei do Governo Digital)"
        elif any(k in norm for k in ["contratacao", "tic"]) and ("14.133" in norm or "14133" in norm):
            top = "Contratação de soluções de tecnologia da informação e comunicação (Lei nº 14.133/2021 aplicada às contratações de TIC)"
        else:
            top = "Governança de TI: estratégia e alinhamento com os objetivos institucionais"
        return {
            "target_area": "CONHECIMENTOS ESPECÍFICOS B02 - TI",
            "target_materia": "Governança de Tecnologia da Informação",
            "target_topico": top
        }

    # --- TI: LEGISLAÇÃO APLICADA À TI (B02) ---
    if "lgpd" in norm or "13.709" in norm or "13709" in norm or "marco civil" in norm or "12.965" in norm or "12965" in norm:
        if "marco civil" in norm or "12.965" in norm or "12965" in norm:
            top = "Marco Civil da Internet (Lei nº 12.965/2014): princípios de neutralidade de rede, proteção de dados e guarda de registros de conexão e de acesso"
        else:
            top = "Aplicação técnica da Lei Geral de Proteção de Dados Pessoais (Lei nº 13.709/2018) no desenvolvimento e na operação de sistemas: privacy by design e by default, minimização de dados, anonimização e pseudonimização"
        return {
            "target_area": "CONHECIMENTOS ESPECÍFICOS B02 - TI",
            "target_materia": "Legislação Aplicada à Tecnologia da Informação",
            "target_topico": top
        }

    # --- TI: DESENVOLVIMENTO DE SISTEMAS (B02) ---
    termos_dev = [
        "java", "python", "javascript", "react", "node.js", "poo", "orientada a objetos",
        "restful", "api rest", "apis rest", "metodo http", "idempotente", "microsservicos",
        "api gateway", "algoritmo", "estrutura de dados", "oauth", "jwt", "rabbitmq",
        "mensageria", "zuul", "front-end", "html5", "css3", "typescript", "encapsulamento", "polimorfismo"
    ]
    if any(td in norm for td in termos_dev):
        if any(k in norm for k in ["poo", "orientada a objetos", "heranca", "polimorfismo", "encapsulamento", "programacao funcional"]):
            top = "Programação orientada a objetos e programação funcional"
        elif "java" in norm and not any(k in norm for k in ["javascript"]):
            top = "Programação em Java (conceitos básicos)"
        elif "python" in norm:
            top = "Programação em Python para automação e desenvolvimento back-end"
        elif any(k in norm for k in ["javascript", "node.js"]):
            top = "Programação em JavaScript e no ambiente Node.js"
        elif any(k in norm for k in ["react", "front-end"]):
            top = "Desenvolvimento front-end com React"
        elif any(k in norm for k in ["rest", "api rest", "apis rest", "graphql", "websockets", "zuul", "rabbitmq", "api gateway", "idempotente"]):
            top = "Desenvolvimento de APIs RESTful"
        elif any(k in norm for k in ["oauth", "jwt", "oidc"]):
            top = "Autenticação, identidade e autorização: OAuth 2.0, OpenID Connect (OIDC) 1.0"
        else:
            top = "Algoritmos, lógica de programação e estruturas de dados"
        return {
            "target_area": "CONHECIMENTOS ESPECÍFICOS B02 - TI",
            "target_materia": "Desenvolvimento de Sistemas",
            "target_topico": top
        }

    # --- TI: ENGENHARIA DE SOFTWARE (B02) ---
    termos_eng = [
        "scrum", "kanban", "xp", "metodologia agil", "requisitos funcionais", "elicitacao de requisitos",
        "casos de uso", "historias de usuario", "padroes de projeto", "design patterns", "gof",
        "singleton", "solid", "teste unitario", "test-driven", "tdd", "ciclo de vida de software",
        "refatoracao", "arquitetura de software", "qualidade de software", "licenciamento de software"
    ]
    if any(te in norm for te in termos_eng):
        if any(k in norm for k in ["scrum", "kanban", "xp", "agil"]):
            top = "Abordagens, métodos e frameworks ágeis: Scrum, Kanban, Lean Software Development e Extreme Programming (XP)"
        elif any(k in norm for k in ["requisitos", "casos de uso", "historias de usuario", "elicitacao"]):
            top = "Levantamento, especificação, análise, validação e gerenciamento de requisitos funcionais e não funcionais"
        elif any(k in norm for k in ["padroes de projeto", "design patterns", "gof"]):
            top = "Padrões de projeto de software (Design Patterns), incluindo padrões criacionais, estruturais e comportamentais"
        elif any(k in norm for k in ["solid", "arquitetura de software", "camadas", "microsservicos", "coesao"]):
            top = "Arquitetura de software: padrões arquiteturais, arquitetura em camadas, orientada a serviços (SOA), microsserviços e orientada a eventos"
        elif any(k in norm for k in ["teste", "tdd", "test-driven", "testes"]):
            top = "Testes de software: unitários, de integração, funcionais, de regressão, de carga e de estresse"
        elif any(k in norm for k in ["uml", "bpmn"]):
            top = "Modelagem de sistemas e processos com UML e BPMN"
        else:
            top = "Fundamentos da engenharia de software"
        return {
            "target_area": "CONHECIMENTOS ESPECÍFICOS B02 - TI",
            "target_materia": "Engenharia de Software",
            "target_topico": top
        }

    # --- TÉCNICO ADMINISTRATIVO: DIREITO CONSTITUCIONAL (A01) ---
    termos_const = [
        "constituicao federal", "cf/88", "direitos fundamentais", "reparticao de competencias",
        "competencia privativa", "competencia concorrente", "poder legislativo", "processo legislativo",
        "poder executivo", "poder judiciario", "funcoes essenciais a justica", "ministerio publico",
        "advocacia publica", "eficacia plena", "eficacia contida", "eficacia limitada", "direitos politicos",
        "nacionalidade", "sigilo fiscal", "cnj", "conselho nacional de justica", "cargo, emprego e funcao publica",
        "teto remuneratorio", "subsidio"
    ]
    if any(tc in norm for tc in termos_const):
        if any(k in norm for k in ["eficacia plena", "eficacia contida", "eficacia limitada"]):
            top = "Da aplicabilidade das normas constitucionais: normas de eficácia plena, contida e limitada"
        elif any(k in norm for k in ["direitos e deveres individuais", "direitos sociais", "nacionalidade", "direitos politicos", "sigilo fiscal"]):
            top = "Dos direitos e garantias fundamentais: dos direitos e deveres individuais e coletivos"
        elif any(k in norm for k in ["competencias da uniao", "estados federados", "municipios", "competencia concorrente", "competencia legislativa"]):
            top = "Das competências da União, dos Estados e dos Municípios"
        elif any(k in norm for k in ["poder legislativo", "processo legislativo", "congresso nacional"]):
            top = "Do Poder Legislativo: do Congresso Nacional"
        elif any(k in norm for k in ["poder executivo", "presidente da republica"]):
            top = "Do Poder Executivo: do Presidente e do Vice-Presidente da República"
        elif any(k in norm for k in ["cnj", "conselho nacional de justica"]):
            top = "do Conselho Nacional de Justiça: organização e competência"
        elif any(k in norm for k in ["poder judiciario", "supremo tribunal", "stj"]):
            top = "Do Poder Judiciário: disposições gerais"
        elif any(k in norm for k in ["ministerio publico", "advocacia publica", "defensoria publica"]):
            top = "Das funções essenciais à Justiça: do Ministério Público"
        elif any(k in norm for k in ["servidores publicos", "subsidio", "teto remuneratorio"]):
            top = "dos servidores públicos"
        elif any(k in norm for k in ["cargo, emprego e funcao", "administracao publica"]):
            top = "Da Administração Pública: disposições gerais"
        else:
            top = "Princípios fundamentais"
        return {
            "target_area": "CONHECIMENTOS ESPECÍFICOS A01 - TÉCNICO ADMINISTRATIVO",
            "target_materia": "Noções de Direito Constitucional",
            "target_topico": top
        }

    # --- TÉCNICO ADMINISTRATIVO: CONTROLE EXTERNO (A01) ---
    termos_ctrl = [
        "tribunal de contas", "tribunais de contas", "controle externo", "controle interno e externo",
        "nbasp", "issai", "auditoria governamental", "tomada de contas", "prestacao de contas",
        "julgamento de contas", "achados de auditoria", "matriz de achados", "mecanismos de controle interno"
    ]
    if any(tct in norm for tct in termos_ctrl):
        if any(k in norm for k in ["nbasp", "issai", "normas da intosai"]):
            top = "Normas Brasileiras de Auditoria do Setor Público (NBASP 100, 200, 300 e 400)"
        elif any(k in norm for k in ["natureza juridica", "competencias", "jurisdicao"]):
            top = "Competências e natureza jurídica dos Tribunais de Contas"
        elif any(k in norm for k in ["amostragem", "planejamento de auditoria", "papeis de trabalho"]):
            top = "Planejamento de auditoria: determinação de escopo e amostragem estatística"
        elif any(k in norm for k in ["achado", "evidencias", "matriz de achados"]):
            top = "Evidências e caracterização de achados de auditoria"
        elif any(k in norm for k in ["relatorio de auditoria", "comunicacao dos resultados"]):
            top = "Comunicação dos resultados: relatórios de auditoria"
        elif any(k in norm for k in ["tomada de contas", "prestacao de contas", "contraditorio"]):
            top = "Prestações e tomadas de contas"
        else:
            top = "Sistema constitucional de controle: controle interno e controle externo"
        return {
            "target_area": "CONHECIMENTOS ESPECÍFICOS A01 - TÉCNICO ADMINISTRATIVO",
            "target_materia": "Noções de Controle Externo",
            "target_topico": top
        }

    # --- TÉCNICO ADMINISTRATIVO: LICITAÇÕES E CONTRATOS (A01) ---
    termos_licit = [
        "14.133", "14133", "pregao", "concorrencia", "dialogo competitivo", "dispensa de licitacao",
        "inexigibilidade de licitacao", "inexigivel", "licitacao e inexigivel", "etp",
        "termo de referencia", "estudo tecnico preliminar", "matriz de riscos", "contrato administrativo",
        "registro de precos", "atos da administracao decorrentes da aplicacao da lei"
    ]
    if any(tl in norm for tl in termos_licit):
        if any(k in norm for k in ["dispensa", "inexigibilidade", "inexigivel"]):
            top = "Contratação direta: dispensa e inexigibilidade"
        elif any(k in norm for k in ["etp", "termo de referencia", "matriz de risco", "planejamento"]):
            top = "Planejamento das contratações: Plano Anual de Contratações, Estudo Técnico Preliminar, Termo de Referência e matriz de riscos"
        elif any(k in norm for k in ["modalidade", "criterio de julgamento"]):
            top = "Modalidades de licitação e critérios de julgamento"
        elif any(k in norm for k in ["registro de precos", "credenciamento", "pre-qualificacao"]):
            top = "Sistema de registro de preços"
        elif any(k in norm for k in ["sancao", "sancoes administrativas", "inidoneidade", "recurso administrativo", "irresignacao"]):
            top = "Sanções administrativas e processo sancionador"
        else:
            top = "Contratos administrativos: formalização, execução, fiscalização e gestão contratual"
        return {
            "target_area": "CONHECIMENTOS ESPECÍFICOS A01 - TÉCNICO ADMINISTRATIVO",
            "target_materia": "Licitações e Contratos Administrativos",
            "target_topico": top
        }

    # --- TÉCNICO ADMINISTRATIVO: DIREITO ADMINISTRATIVO (A01) ---
    termos_dir_adm = [
        "ato administrativo", "atos administrativos", "poderes da administracao", "poder de policia",
        "poder hierarquico", "poder disciplinar", "responsabilidade civil do estado", "improbidade administrativa",
        "8.429", "8429", "14.230", "servicos publicos", "concessao de servico", "organizacao administrativa",
        "administracao direta e indireta", "autarquia", "empresa publica", "sociedade de economia mista",
        "lindb", "4.657", "processo administrativo", "bens publicos", "regime juridico administrativo",
        "ordenador de despesa", "diarias", "permuta de bem"
    ]
    if any(tda in norm for tda in termos_dir_adm):
        if any(k in norm for k in ["ato administrativo", "atos administrativos", "requisitos de validade", "revogacao", "anulacao", "convalidacao"]):
            top = "Ato administrativo"
        elif any(k in norm for k in ["poder de policia", "poder hierarquico", "poder disciplinar", "poderes da administracao"]):
            top = "Poderes da Administração Pública"
        elif any(k in norm for k in ["improbidade administrativa", "8.429", "8429", "14.230", "enriquecimento ilicito", "lesao ao erario"]):
            top = "Lei de Improbidade Administrativa (Lei nº 8.429/1992 com redação dada pela Lei nº 14.230/2021 e alterações)"
        elif any(k in norm for k in ["responsabilidade civil do estado", "responsabilidade objetiva"]):
            top = "Responsabilidade civil do Estado"
        elif any(k in norm for k in ["organizacao administrativa", "administracao direta", "administracao indireta", "descentralizacao"]):
            top = "Organização administrativa: administração direta e indireta"
        elif any(k in norm for k in ["servicos publicos", "concessao", "permissao"]):
            top = "Serviços públicos: concessão, permissão e autorização"
        elif any(k in norm for k in ["lindb", "lei de introducao", "4.657"]):
            top = "Lei de Introdução às normas do Direito Brasileiro (Decreto-Lei nº 4.657/1942 com redação dada pela Lei nº 12.376/2010 e alterações) e sua aplicação na Administração Pública"
        elif "bens publicos" in norm or "permuta de bem" in norm:
            top = "Bens públicos"
        elif "processo administrativo" in norm:
            top = "Processo administrativo"
        else:
            top = "Princípios constitucionais e legais da Administração Pública"
        return {
            "target_area": "CONHECIMENTOS ESPECÍFICOS A01 - TÉCNICO ADMINISTRATIVO",
            "target_materia": "Noções de Direito Administrativo",
            "target_topico": top
        }

    # --- TÉCNICO ADMINISTRATIVO: ADMINISTRAÇÃO FINANCEIRA E ORÇAMENTÁRIA - AFO (A01) ---
    termos_afo = [
        "orcamento publico", "ppa", "ldo", "loa", "plano plurianual", "lei de diretrizes orcamentarias",
        "lei orcamentaria anual", "receita orcamentaria", "despesa orcamentaria", "restos a pagar",
        "suprimento de fundos", "creditos orcamentarios", "creditos adicionais", "lei de responsabilidade fiscal",
        "lrf", "101/2000", "despesa com pessoal", "divida publica", "estagios da despesa", "estagios da receita",
        "rreo", "relatorio resumido"
    ]
    if any(ta in norm for ta in termos_afo):
        if any(k in norm for k in ["plano plurianual", "ppa"]):
            top = "Plano Plurianual"
        elif any(k in norm for k in ["lei de diretrizes orcamentarias", "ldo"]):
            top = "Lei de Diretrizes Orçamentárias"
        elif any(k in norm for k in ["lei orcamentaria anual", "loa"]):
            top = "Lei Orçamentária Anual"
        elif "ciclo orcamentario" in norm:
            top = "Ciclo orçamentário"
        elif "principios orcamentarios" in norm:
            top = "Princípios orçamentários"
        elif any(k in norm for k in ["receita orcamentaria", "estagios da receita", "fontes de receita"]):
            top = "Receita Orçamentária"
        elif any(k in norm for k in ["despesa orcamentaria", "estagios da despesa", "empenho"]):
            top = "Despesa Orçamentária"
        elif "restos a pagar" in norm:
            top = "Restos a pagar"
        elif "despesas de exercicios anteriores" in norm:
            top = "Despesas de exercícios anteriores"
        elif any(k in norm for k in ["creditos orcamentarios", "creditos adicionais"]):
            top = "Créditos orçamentários iniciais e adicionais"
        elif "suprimento de fundos" in norm:
            top = "Suprimento de fundos"
        elif any(k in norm for k in ["despesa com pessoal", "despesas com pessoal"]):
            top = "Despesas com pessoal: definições e limites"
        elif any(k in norm for k in ["lrf", "101/2000", "relatorio resumido", "rreo"]):
            top = "Lei de Responsabilidade Fiscal (Lei Complementar nº 101/2000 e alterações)"
        elif any(k in norm for k in ["divida publica", "endividamento"]):
            top = "Dívida e endividamento público: definições"
        else:
            top = "Orçamento público"
        return {
            "target_area": "CONHECIMENTOS ESPECÍFICOS A01 - TÉCNICO ADMINISTRATIVO",
            "target_materia": "Noções de Administração Financeira e Orçamentária",
            "target_topico": top
        }

    # --- TÉCNICO ADMINISTRATIVO: CONTABILIDADE APLICADA AO SETOR PÚBLICO - CASP (A01) ---
    termos_casp = [
        "nbc tsp", "mcasp", "pcasp", "balanco orcamentario", "balanco financeiro",
        "balanco patrimonial", "demonstracao das variacoes patrimoniais", "dvp",
        "variacao patrimonial aumentativa", "variacao patrimonial diminutiva", "escrituracao das contas publicas"
    ]
    if any(tcasp in norm for tcasp in termos_casp):
        if any(k in norm for k in ["pcasp", "plano de contas"]):
            top = "Plano de Contas Aplicado ao Setor Público"
        elif any(k in norm for k in ["balanco orcamentario", "balanco financeiro", "demonstracoes contabeis", "escrituracao"]):
            top = "Parte V – Demonstrações Contábeis Aplicadas ao Setor Público"
        elif "mcasp" in norm:
            top = "Manual de Contabilidade Aplicada ao Setor Público – MCASP, 11ª edição: Parte I – Procedimentos Contábeis Orçamentários"
        else:
            top = "Normas Brasileiras de Contabilidade Aplicadas ao Setor Público – NBC TSP: NBC TSP Estrutura Conceitual"
        return {
            "target_area": "CONHECIMENTOS ESPECÍFICOS A01 - TÉCNICO ADMINISTRATIVO",
            "target_materia": "Contabilidade aplicada ao Setor Público",
            "target_topico": top
        }

    # --- TÉCNICO ADMINISTRATIVO: ADMINISTRAÇÃO PÚBLICA, GERAL, ESTRATÉGICA E PESSOAS (A01) ---
    termos_adm = [
        "planejamento estrategico", "missao, visao", "swot", "balanced scorecard", "bsc",
        "cadeia de valor", "lideranca", "maslow", "herzberg", "motivacao", "recrutamento",
        "selecao", "avaliacao de desempenho", "gestao por competencias", "cultura organizacional",
        "clima organizacional", "fayol", "taylor", "weber", "burocracia", "indicadores de gestao de pessoas",
        "equipes interfuncionais", "gestao de pessoas", "formas organizacionais com base na"
    ]
    if any(ta in norm for ta in termos_adm):
        if any(k in norm for k in ["planejamento estrategico", "missao, visao"]):
            return {
                "target_area": "CONHECIMENTOS ESPECÍFICOS A01 - TÉCNICO ADMINISTRATIVO",
                "target_materia": "Administração Estratégica",
                "target_topico": "Planejamento Estratégico: definição de missão, visão e valores"
            }
        elif any(k in norm for k in ["swot", "forcas competitivas", "rbv"]):
            return {
                "target_area": "CONHECIMENTOS ESPECÍFICOS A01 - TÉCNICO ADMINISTRATIVO",
                "target_materia": "Administração Estratégica",
                "target_topico": "Ferramentas de diagnóstico: análise SWOT, cinco forças competitivas, Visão-Baseada em Recursos (RBV)"
            }
        elif any(k in norm for k in ["balanced scorecard", "bsc"]):
            return {
                "target_area": "CONHECIMENTOS ESPECÍFICOS A01 - TÉCNICO ADMINISTRATIVO",
                "target_materia": "Administração Estratégica",
                "target_topico": "Balanced Scorecard (BSC)"
            }
        elif "lideranca" in norm:
            return {
                "target_area": "CONHECIMENTOS ESPECÍFICOS A01 - TÉCNICO ADMINISTRATIVO",
                "target_materia": "Comportamento Organizacional",
                "target_topico": "Liderança"
            }
        elif any(k in norm for k in ["valores, atitudes", "satisfacao", "motivacao", "equipes interfuncionais"]):
            return {
                "target_area": "CONHECIMENTOS ESPECÍFICOS A01 - TÉCNICO ADMINISTRATIVO",
                "target_materia": "Comportamento Organizacional",
                "target_topico": "valores, atitudes e satisfação no trabalho, Personalidade, emoções e motivação, equipes de trabalho"
            }
        elif any(k in norm for k in ["recrutamento", "selecao"]):
            return {
                "target_area": "CONHECIMENTOS ESPECÍFICOS A01 - TÉCNICO ADMINISTRATIVO",
                "target_materia": "Gestão de Pessoas",
                "target_topico": "Recrutamento, seleção e integração"
            }
        elif any(k in norm for k in ["avaliacao de desempenho", "indicadores de gestao de pessoas"]):
            return {
                "target_area": "CONHECIMENTOS ESPECÍFICOS A01 - TÉCNICO ADMINISTRATIVO",
                "target_materia": "Gestão de Pessoas",
                "target_topico": "Gestão e Avaliação de Desempenho"
            }
        elif any(k in norm for k in ["gestao por competencias", "gestao de pessoas na atualidade"]):
            return {
                "target_area": "CONHECIMENTOS ESPECÍFICOS A01 - TÉCNICO ADMINISTRATIVO",
                "target_materia": "Gestão de Pessoas",
                "target_topico": "Gestão por Competências"
            }
        elif any(k in norm for k in ["escolas administrativas", "teorias da administracao", "fayol", "taylor"]):
            return {
                "target_area": "CONHECIMENTOS ESPECÍFICOS A01 - TÉCNICO ADMINISTRATIVO",
                "target_materia": "Administração Geral",
                "target_topico": "Teorias da Administração e evolução das escolas administrativas"
            }
        else:
            return {
                "target_area": "CONHECIMENTOS ESPECÍFICOS A01 - TÉCNICO ADMINISTRATIVO",
                "target_materia": "Noções de Administração Pública",
                "target_topico": "Processo organizacional: planejamento, organização, direção, coordenação, comunicação, controle e avaliação"
            }

    # Se não coube em nenhuma regra comprovada do edital, descarta
    return {"target_area": "", "target_materia": "", "target_topico": "DESCARTADA"}


def processar_lotes():
    catalogo, edital_data = carregar_edital()
    PROCESSADOS_DIR.mkdir(parents=True, exist_ok=True)
    
    arquivos_pendentes = sorted(PENDENTES_DIR.glob("lote_*.json"))
    total_arquivos = len(arquivos_pendentes)
    
    if total_arquivos == 0:
        print("[!] Nenhum arquivo encontrado em data/chunks_pendentes/.")
        return

    print(f"[*] Iniciando classificação semântica bottom-up de {total_arquivos} lotes...")

    total_questoes = 0
    total_classificadas = 0
    total_descartadas = 0

    for idx, arq_pendente in enumerate(arquivos_pendentes, 1):
        nome_arq = arq_pendente.name
        questoes = json.loads(arq_pendente.read_text(encoding="utf-8"))
        lote_classificadas = 0
        lote_descartadas = 0

        for q in questoes:
            res = classificar_questao(q, catalogo)
            q["target_area"] = res["target_area"]
            q["target_materia"] = res["target_materia"]
            q["target_topico"] = res["target_topico"]
            
            if res["target_topico"] == "DESCARTADA":
                lote_descartadas += 1
            else:
                lote_classificadas += 1

        # Salva no destino mantendo JSON e IDs intactos
        arq_destino = PROCESSADOS_DIR / nome_arq
        arq_destino.write_text(json.dumps(questoes, ensure_ascii=False, indent=2), encoding="utf-8")
        
        # Deleta da fila para limpar as pendências
        arq_pendente.unlink()

        total_questoes += len(questoes)
        total_classificadas += lote_classificadas
        total_descartadas += lote_descartadas

        print(f"[{idx:02d}/{total_arquivos:02d}] Processado {nome_arq}: {len(questoes)} questões (Classificadas: {lote_classificadas}, Descartadas: {lote_descartadas})")

    print("\n===================================================================")
    print("CLASSIFICAÇÃO SEMÂNTICA CONCLUÍDA COM SUCESSO!")
    print(f"  - Total de lotes processados: {total_arquivos}")
    print(f"  - Total de questões processadas: {total_questoes}")
    print(f"  - Questões válidas atribuídas ao Edital: {total_classificadas}")
    print(f"  - Questões descartadas (fora de escopo): {total_descartadas}")
    print(f"  - Diretório de saída: {PROCESSADOS_DIR}")
    print(f"  - Fila de pendências: {len(list(PENDENTES_DIR.glob('lote_*.json')))} arquivos restantes")
    print("===================================================================")


if __name__ == "__main__":
    processar_lotes()
