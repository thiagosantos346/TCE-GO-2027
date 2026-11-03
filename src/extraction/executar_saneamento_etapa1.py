import os
import json

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RAW_PROVAS_DIRS = [
    os.path.join(BASE_DIR, "raw_provas"),
    os.path.join(BASE_DIR, "raw_provas_v3")
]

# Mapeamento semântico gerado pelo LLM para todos os certames do inventário
# Cada tupla define: (identificador_slug, orgao, ano, banca, cargo, tipo_prova, dentro_escopo, motivo)
CLASSIFICACOES_NLP = [
    ("analista-administrativo-tj-sc-fgv-2026", "TJ-SC", 2026, "FGV", "Analista Administrativo", "ADM", True, "Whitelist: Analista Administrativo"),
    ("analista-de-controle-externo-ciencias-contabeis-tce-go-fgv-2024", "TCE-GO", 2024, "FGV", "Analista de Controle Externo - Ciências Contábeis", "Geral", False, "Fora do escopo: Contabilidade"),
    ("analista-de-controle-externo-controle-externo-tce-go-fgv-2024", "TCE-GO", 2024, "FGV", "Analista de Controle Externo - Controle Externo", "Geral", True, "Whitelist: Auditor/Controle Externo Geral"),
    ("analista-de-controle-externo-engenharia-tce-go-fgv-2024", "TCE-GO", 2024, "FGV", "Analista de Controle Externo - Engenharia", "Geral", False, "Fora do escopo: Engenharia"),
    ("analista-de-controle-externo-gestao-de-conhecimento-tce-go-fcc-2009", "TCE-GO", 2009, "FCC", "Analista de Controle Externo - Gestão do Conhecimento", "Geral", False, "Fora do escopo: Gestão do Conhecimento / 2009"),
    ("analista-de-controle-externo-juridica-tce-go-fgv-2024", "TCE-GO", 2024, "FGV", "Analista de Controle Externo - Jurídica", "Geral", False, "Fora do escopo: Área Jurídica/Direito"),
    ("analista-de-controle-externo-tecnologia-da-informacao-tce-go-fgv-2024", "TCE-GO", 2024, "FGV", "Analista de Controle Externo - Tecnologia da Informação", "TI", True, "Whitelist: Auditor/Analista de TI"),
    ("analista-judiciario-apoio-especializado-governanca-e-gestao-de-tecnologia-da-informacao-trf-6-cebraspe-2025", "TRF 6ª", 2025, "CEBRASPE", "Analista Judiciário - Governança e Gestão de TI", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-apoio-especializado-suporte-em-tecnologia-da-informacao-stj-cebraspe-2024", "STJ", 2024, "CEBRASPE", "Analista Judiciário - Suporte em TI", "TI", True, "Whitelist: Analista de TI / Suporte"),
    ("analista-judiciario-apoio-especializado-tecnologia-da-informacao-banco-de-dados-tj-ap-fgv-2023", "TJ-AP", 2023, "FGV", "Analista Judiciário - TI Banco de Dados", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-apoio-especializado-tecnologia-da-informacao-desenvolvimento-de-sistemas-tj-ap-fgv-2023", "TJ-AP", 2023, "FGV", "Analista Judiciário - TI Desenvolvimento de Sistemas", "TI", True, "Whitelist: Analista de TI / Sistemas"),
    ("analista-judiciario-apoio-especializado-tecnologia-da-informacao-seguranca-da-informacao-tj-ap-fgv-2023", "TJ-AP", 2023, "FGV", "Analista Judiciário - TI Segurança da Informação", "TI", True, "Whitelist: Analista de TI / Segurança"),
    ("analista-judiciario-apoio-especializado-tecnologia-da-informacao-telecomunicacoes-tj-ap-fgv-2023", "TJ-AP", 2023, "FGV", "Analista Judiciário - TI Telecomunicações", "TI", True, "Whitelist: Analista de TI / Telecomunicações"),
    ("analista-judiciario-apoio-especializado-tecnologia-da-informacao-trf-6-cebraspe-2025", "TRF 6ª", 2025, "CEBRASPE", "Analista Judiciário - Tecnologia da Informação", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-apoio-especializado-tecnologia-da-informacao-trt-14-fcc-2016", "TRT 14ª", 2016, "FCC", "Analista Judiciário - Tecnologia da Informação", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-apoio-especializado-tecnologia-da-informacao-trt-23-fcc-2016", "TRT 23ª", 2016, "FCC", "Analista Judiciário - Tecnologia da Informação", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-apoio-especializado-tecnologia-da-informacao-trt-3-fumarc-2022", "TRT 3ª", 2022, "FUMARC", "Analista Judiciário - Tecnologia da Informação", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-apoio-especializado-tecnologia-da-informacao-trt-6-fcc-2012", "TRT 6ª", 2012, "FCC", "Analista Judiciário - Tecnologia da Informação", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-apoio-especializado-tecnologia-da-informacao-trt-8-cespe-2016", "TRT 8ª", 2016, "CESPE", "Analista Judiciário - Tecnologia da Informação", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-apoio-especializado-tecnologia-da-informacao-trt-9-fcc-2015", "TRT 9ª", 2015, "FCC", "Analista Judiciário - Tecnologia da Informação", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-area-administrativa-contabilidade-trt-da-24-regiao-fgv-2025", "TRT 24ª", 2025, "FGV", "Analista Judiciário - Administrativa Contabilidade", "Geral", False, "Fora do escopo: Contabilidade"),
    ("analista-judiciario-area-administrativa-sem-especialidade-trt-da-24-regiao-fgv-2025", "TRT 24ª", 2025, "FGV", "Analista Judiciário - Área Administrativa", "ADM", True, "Whitelist: Analista Administrativo"),
    ("analista-judiciario-area-administrativa-tecnologia-da-informacao-trt-16-fgv-2022", "TRT 16ª", 2022, "FGV", "Analista Judiciário - TI Administrativa", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-area-administrativa-trt-1-fgv-2024", "TRF 1ª", 2024, "FGV", "Analista Judiciário - Área Administrativa", "ADM", True, "Whitelist: Analista Administrativo"),
    ("analista-judiciario-area-apoio-especializado-especialidade-suporte-em-tecnologia-da-informacao-trf-1-fgv-2024", "TRF 1ª", 2024, "FGV", "Analista Judiciário - Suporte em TI", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-area-apoio-especializado-especialidade-tecnologia-da-informacao-trf-1-fgv-2024", "TRF 1ª", 2024, "FGV", "Analista Judiciário - Tecnologia da Informação", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-area-apoio-especializado-especialidade-tecnologia-da-informacao-trt-7-cespe-2017", "TRT 7ª", 2017, "CESPE", "Analista Judiciário - Tecnologia da Informação", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-area-apoio-especializado-tecnologia-da-informacao-trt-da-24-regiao-fgv-2025", "TRT 24ª", 2025, "FGV", "Analista Judiciário - Tecnologia da Informação", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-area-apoio-especializado-tecnologia-da-informacao-trt-da-8-regiao-cebraspe-2022", "TRT 8ª", 2022, "CEBRASPE", "Analista Judiciário - Tecnologia da Informação", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-area-de-apoio-especializado-governanca-e-gestao-de-tecnologia-da-informacao-trf-da-5-regiao-ibfc-2024", "TRF 5ª", 2024, "IBFC", "Analista Judiciário - Governança e Gestão de TI", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-classe-c-analista-de-tecnologia-da-informacao-tj-mg-ibfc-2022", "TJ-MG", 2022, "IBFC", "Analista Judiciário - Analista de TI", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-especialidade-analista-de-tecnologia-da-informacao-tjm-mg-instituto-consulplan-2021", "TJM-MG", 2021, "Consulplan", "Analista Judiciário - Analista de TI", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-gestao-e-governanca-de-tecnologia-da-informacao-tj-rr-fgv-2024", "TJ-RR", 2024, "FGV", "Analista Judiciário - Gestão e Governança de TI", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-grupo-tecnologia-da-informacao-analista-de-gestao-de-tic-tj-rj-cebraspe-2021", "TJ-RJ", 2021, "CEBRASPE", "Analista Judiciário - Gestão de TIC", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-grupo-tecnologia-da-informacao-analista-de-infraestrutura-de-tic-tj-rj-cebraspe-2021", "TJ-RJ", 2021, "CEBRASPE", "Analista Judiciário - Infraestrutura de TIC", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-grupo-tecnologia-da-informacao-analista-de-negocios-tj-rj-cebraspe-2021", "TJ-RJ", 2021, "CEBRASPE", "Analista Judiciário - Analista de Negócios", "TI", True, "Whitelist: Analista de TI / Sistemas"),
    ("analista-judiciario-grupo-tecnologia-da-informacao-analista-de-projetos-tj-rj-cebraspe-2021", "TJ-RJ", 2021, "CEBRASPE", "Analista Judiciário - Analista de Projetos", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-grupo-tecnologia-da-informacao-analista-de-seguranca-da-informacao-tj-rj-cebraspe-2021", "TJ-RJ", 2021, "CEBRASPE", "Analista Judiciário - Segurança da Informação", "TI", True, "Whitelist: Analista de TI / Segurança"),
    ("analista-judiciario-grupo-tecnologia-da-informacao-analista-de-sistemas-tj-rj-cebraspe-2021", "TJ-RJ", 2021, "CEBRASPE", "Analista Judiciário - Analista de Sistemas", "TI", True, "Whitelist: Analista de Sistemas"),
    ("analista-judiciario-infraestrutura-de-tecnologia-da-informacao-tj-pb-faperp-2012", "TJ-PB", 2012, "FAPERP", "Analista Judiciário - Infraestrutura de TI", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-infraestrutura-de-tecnologia-da-informacao-tj-rr-fgv-2024", "TJ-RR", 2024, "FGV", "Analista Judiciário - Infraestrutura de TI", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-suporte-em-tecnologia-da-informacao-stf-cespe-2008", "STF", 2008, "CESPE", "Analista Judiciário - Suporte em TI", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-suporte-em-tecnologia-da-informacao-stf-cespe-2013", "STF", 2013, "CESPE", "Analista Judiciário - Suporte em TI", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-suporte-em-tecnologia-da-informacao-stj-cespe-2015", "STJ", 2015, "CESPE", "Analista Judiciário - Suporte em TI", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-suporte-em-tecnologia-da-informacao-tj-dft-cespe-2015", "TJDFT", 2015, "CESPE", "Analista Judiciário - Suporte em TI", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-suporte-em-tecnologia-da-informacao-tj-dft-fgv-2022", "TJDFT", 2022, "FGV", "Analista Judiciário - Suporte em TI", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-tecnologia-da-informacao-tj-ba-fgv-2015", "TJ-BA", 2015, "FGV", "Analista Judiciário - Tecnologia da Informação", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-tecnologia-da-informacao-tj-mt-fgv-2024", "TJ-MT", 2024, "FGV", "Analista Judiciário - Tecnologia da Informação", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-tecnologia-da-informacao-trt-1-fcc-2014", "TRT 1ª", 2014, "FCC", "Analista Judiciário - Tecnologia da Informação", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-tecnologia-da-informacao-trt-10-cespe-2013", "TRT 10ª", 2013, "CESPE", "Analista Judiciário - Tecnologia da Informação", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-tecnologia-da-informacao-trt-11-fcc-2017", "TRT 11ª", 2017, "FCC", "Analista Judiciário - Tecnologia da Informação", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-tecnologia-da-informacao-trt-13-fcc-2014", "TRT 13ª", 2014, "FCC", "Analista Judiciário - Tecnologia da Informação", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-tecnologia-da-informacao-trt-13-fgv-2022", "TRT 13ª", 2022, "FGV", "Analista Judiciário - Tecnologia da Informação", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-tecnologia-da-informacao-trt-15-fcc-2015", "TRT 15ª", 2015, "FCC", "Analista Judiciário - Tecnologia da Informação", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-tecnologia-da-informacao-trt-16-fcc-2014", "TRT 16ª", 2014, "FCC", "Analista Judiciário - Tecnologia da Informação", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-tecnologia-da-informacao-trt-2-fcc-2014", "TRT 2ª", 2014, "FCC", "Analista Judiciário - Tecnologia da Informação", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-tecnologia-da-informacao-trt-24-fcc-2017", "TRT 24ª", 2017, "FCC", "Analista Judiciário - Tecnologia da Informação", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-tecnologia-da-informacao-trt-3-fcc-2015", "TRT 3ª", 2015, "FCC", "Analista Judiciário - Tecnologia da Informação", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-tecnologia-da-informacao-trt-4-fcc-2015", "TRT 4ª", 2015, "FCC", "Analista Judiciário - Tecnologia da Informação", "TI", True, "Whitelist: Analista de TI"),
    ("analista-judiciario-tecnologia-da-informacao-trt-da-13-regiao-fgv-2022", "TRT 13ª", 2022, "FGV", "Analista Judiciário - Tecnologia da Informação", "TI", True, "Whitelist: Analista de TI"),
    ("analista_judiciario_apoio_especializado_governanca_e_gestao_de_tecnologia_da_informacao copy.pdf", "TRF 6ª", 2025, "CEBRASPE", "Duplicata Órfã", "TI", False, "Arquivo duplicado avulso"),
    ("analista_judiciario_apoio_especializado_governanca_e_gestao_de_tecnologia_da_informacao.pdf", "TRF 6ª", 2025, "CEBRASPE", "Analista Judiciário - Governança de TI", "TI", True, "Whitelist: Analista de TI"),
    ("analista_judiciario_apoio_especializado_suporte_em_tecnologia_da_informacao.pdf", "STJ", 2024, "CEBRASPE", "Analista Judiciário - Suporte em TI", "TI", True, "Whitelist: Analista de TI"),
    ("analista_judiciario_area_administrativa_tecnologia_da_informacao.pdf", "TRT 16ª", 2022, "FGV", "Analista Judiciário - TI", "TI", True, "Whitelist: Analista de TI"),
    ("auditor-de-controle-externo-administrativa-administracao-tce-pa-fgv-2024", "TCE-PA", 2024, "FGV", "Auditor de Controle Externo - Administração", "ADM", True, "Whitelist: Auditor / Administração"),
    ("auditor-de-controle-externo-administrativa-ciencia-de-dados-tce-pa-fgv-2024", "TCE-PA", 2024, "FGV", "Auditor de Controle Externo - Ciência de Dados", "TI", True, "Whitelist: Auditor / Ciência de Dados"),
    ("auditor-de-controle-externo-administrativa-contabilidade-tce-pa-fgv-2024", "TCE-PA", 2024, "FGV", "Auditor de Controle Externo - Contabilidade", "Geral", False, "Fora do escopo: Contabilidade"),
    ("auditor-de-controle-externo-administrativa-direito-tce-pa-fgv-2024", "TCE-PA", 2024, "FGV", "Auditor de Controle Externo - Direito", "Geral", False, "Fora do escopo: Direito/Jurídica"),
    ("auditor-de-controle-externo-administrativa-engenharia-civil-tce-pa-fgv-2024", "TCE-PA", 2024, "FGV", "Auditor de Controle Externo - Engenharia Civil", "Geral", False, "Fora do escopo: Engenharia Civil"),
    ("auditor-de-controle-externo-administrativa-engenharia-mecanica-tce-pa-fgv-2024", "TCE-PA", 2024, "FGV", "Auditor de Controle Externo - Engenharia Mecânica", "Geral", False, "Fora do escopo: Engenharia Mecânica"),
    ("auditor-de-controle-externo-administrativa-engenharia-telecomunicacao-tce-pa-fgv-2024", "TCE-PA", 2024, "FGV", "Auditor de Controle Externo - Engenharia Telecomunicações", "TI", True, "Whitelist: Auditor / Telecomunicações (TI)"),
    ("auditor-de-controle-externo-administrativa-gestao-governamental-tce-pa-fgv-2024", "TCE-PA", 2024, "FGV", "Auditor de Controle Externo - Gestão Governamental", "ADM", True, "Whitelist: Auditor / Gestão Pública"),
    ("auditor-de-controle-externo-controle-externo-especifica-de-area-comum-tce-pi-fgv-2025", "TCE-PI", 2025, "FGV", "Auditor de Controle Externo - Controle Externo / Área Comum", "Geral", True, "Whitelist: Auditor de Controle Externo Geral"),
    ("auditor-de-controle-externo-fiscalizacao-ciencias-atuariais-tce-pa-fgv-2024", "TCE-PA", 2024, "FGV", "Auditor de Controle Externo - Ciências Atuariais", "Geral", False, "Fora do escopo: Ciências Atuariais"),
    ("auditor-de-controle-externo-fiscalizacao-contabilidade-tce-pa-fgv-2024", "TCE-PA", 2024, "FGV", "Auditor de Controle Externo - Contabilidade", "Geral", False, "Fora do escopo: Contabilidade"),
    ("auditor-fiscal-de-controle-externo-administracao-tce-sc-fgv-2026", "TCE-SC", 2026, "FGV", "Auditor Fiscal de Controle Externo - Administração", "ADM", True, "Whitelist: Auditor / Administração"),
    ("auditor-fiscal-de-controle-externo-ciencias-atuariais-tce-sc-fgv-2026", "TCE-SC", 2026, "FGV", "Auditor Fiscal de Controle Externo - Ciências Atuariais", "Geral", False, "Fora do escopo: Ciências Atuariais"),
    ("auditor-fiscal-de-controle-externo-ciencias-contabeis-tce-sc-fgv-2026", "TCE-SC", 2026, "FGV", "Auditor Fiscal de Controle Externo - Ciências Contábeis", "Geral", False, "Fora do escopo: Contabilidade"),
    ("auditor-fiscal-de-controle-externo-ciencias-da-computacao-sistemas-de-informacao-tce-sc-fgv-2026", "TCE-SC", 2026, "FGV", "Auditor Fiscal de Controle Externo - Ciências da Computação", "TI", True, "Whitelist: Auditor / TI e Sistemas"),
    ("auditor-fiscal-de-controle-externo-direito-tce-sc-fgv-2026", "TCE-SC", 2026, "FGV", "Auditor Fiscal de Controle Externo - Direito", "Geral", False, "Fora do escopo: Direito/Jurídica"),
    ("auditor-fiscal-de-controle-externo-economia-tce-sc-fgv-2026", "TCE-SC", 2026, "FGV", "Auditor Fiscal de Controle Externo - Economia", "Geral", False, "Fora do escopo: Economia"),
    ("auditor-fiscal-de-controle-externo-engenharia-civil-tce-sc-fgv-2026", "TCE-SC", 2026, "FGV", "Auditor Fiscal de Controle Externo - Engenharia Civil", "Geral", False, "Fora do escopo: Engenharia Civil"),
    ("auditor-fiscal-de-controle-externo-engenharia-eletrica-tce-sc-fgv-2026", "TCE-SC", 2026, "FGV", "Auditor Fiscal de Controle Externo - Engenharia Elétrica", "Geral", False, "Fora do escopo: Engenharia Elétrica"),
    ("auditor-fiscal-de-controle-externo-engenharia-sanitaria-tce-sc-fgv-2026", "TCE-SC", 2026, "FGV", "Auditor Fiscal de Controle Externo - Engenharia Sanitária", "Geral", False, "Fora do escopo: Engenharia Sanitária"),
    ("edital_de_abertura_versaex771_o_15_09_2026_-_consolidado_com_retificacoes__1_.pdf", "TCE-GO", 2026, "FCC", "Edital de Abertura", "Geral", False, "Documento administrativo de edital, não é prova"),
    ("tecnico-judiciario-area-administrativa-agente-da-policia-judicial-trt-da-24-regiao-fgv-2025", "TRT 24ª", 2025, "FGV", "Técnico Judiciário - Polícia Judicial", "Geral", False, "Fora do escopo: Polícia Judicial"),
    ("tecnico-judiciario-area-administrativa-sem-especialidade-trt-da-24-regiao-fgv-2025", "TRT 24ª", 2025, "FGV", "Técnico Judiciário - Área Administrativa", "ADM", True, "Whitelist: Técnico Administrativo"),
]

def main():
    slug_map = {}
    for item in CLASSIFICACOES_NLP:
        slug_prefix = item[0][:75]
        slug_map[slug_prefix] = item
        # Also store original
        slug_map[item[0]] = item

    print("=== ETAPA 1: SANEAMENTO FÍSICO DO DIRETÓRIO ===")
    
    arquivos_deletados = []
    arquivos_mantidos = []
    catalogo_final = []

    for d in RAW_PROVAS_DIRS:
        if not os.path.exists(d):
            continue
        for fname in sorted(os.listdir(d)):
            if not fname.lower().endswith(".pdf"):
                continue
            fpath = os.path.join(d, fname)
            
            # Identifica o slug
            slug = fname.split("___")[0]
            
            # Procura no mapa
            classif = None
            for k, v in slug_map.items():
                if slug.startswith(k) or k.startswith(slug) or slug == k:
                    classif = v
                    break
            
            if not classif:
                # Se não encontrar por prefixo exato, faz match por similaridade semântica
                for k, v in slug_map.items():
                    if k in slug or slug in k:
                        classif = v
                        break
            
            if classif:
                _, orgao, ano, banca, cargo, tipo, dentro, motivo = classif
                record = {
                    "diretorio": os.path.basename(d),
                    "arquivo": fname,
                    "caminho_completo": fpath,
                    "orgao": orgao,
                    "ano": ano,
                    "banca": banca,
                    "cargo": cargo,
                    "tipo_de_prova": tipo,
                    "dentro_escopo": dentro,
                    "motivo_conformidade": motivo
                }
                catalogo_final.append(record)
                
                if not dentro:
                    try:
                        os.remove(fpath)
                        arquivos_deletados.append(fpath)
                        print(f"[DELETADO] {fname} -> Motivo: {motivo}")
                    except Exception as e:
                        print(f"[ERRO AO DELETAR] {fpath}: {e}")
                else:
                    arquivos_mantidos.append(fpath)
            else:
                print(f"[ALERTA: NÃO MAPEADO] {fname}")

    # Salva o catálogo consolidado
    catalogo_path = os.path.join(BASE_DIR, "data", "catalogo_provas_classificado.json")
    with open(catalogo_path, "w", encoding="utf-8") as f:
        json.dump(catalogo_final, f, ensure_ascii=False, indent=2)

    print("\n--- RESUMO DA EXECUÇÃO DO SANEAMENTO ---")
    print(f"Total de arquivos classificados: {len(catalogo_final)}")
    print(f"Total de arquivos DELETADOS fisicamente: {len(arquivos_deletados)}")
    print(f"Total de arquivos MANTIDOS na Whitelist: {len(arquivos_mantidos)}")
    print(f"Catálogo completo gravado em: {catalogo_path}")

if __name__ == "__main__":
    main()

