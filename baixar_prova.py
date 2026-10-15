import os
import re
import time
import ssl
import urllib.request

DEST_DIR = "provas_pci"
os.makedirs(DEST_DIR, exist_ok=True)
LINKS_FILE = os.path.join(DEST_DIR, "links_diretos.txt")

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Referer": "https://www.pciconcursos.com.br/"
}

URLS = [
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-area-administrativa-tecnologia-da-informacao-trt-16-fgv-2022",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-apoio-especializado-governanca-e-gestao-de-tecnologia-da-informacao-trf-6-cebraspe-2025",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-apoio-especializado-suporte-em-tecnologia-da-informacao-stj-cebraspe-2024",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-apoio-especializado-tecnologia-da-informacao-trf-6-cebraspe-2025",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-apoio-especializado-tecnologia-da-informacao-trt-3-fumarc-2022",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-apoio-especializado-tecnologia-da-informacao-trt-8-cespe-2016",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-apoio-especializado-tecnologia-da-informacao-trt-14-fcc-2016",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-apoio-especializado-tecnologia-da-informacao-trt-23-fcc-2016",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-apoio-especializado-tecnologia-da-informacao-trt-9-fcc-2015",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-apoio-especializado-tecnologia-da-informacao-banco-de-dados-tj-ap-fgv-2023",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-apoio-especializado-tecnologia-da-informacao-desenvolvimento-de-sistemas-tj-ap-fgv-2023",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-apoio-especializado-tecnologia-da-informacao-seguranca-da-informacao-tj-ap-fgv-2023",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-apoio-especializado-tecnologia-da-informacao-telecomunicacoes-tj-ap-fgv-2023",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-apoio-especializado-tecnologia-da-informacao-trt-6-fcc-2012",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-area-apoio-especializado-especialidade-tecnologia-da-informacao-trt-7-cespe-2017",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-area-apoio-especializado-especialidade-suporte-em-tecnologia-da-informacao-trf-1-fgv-2024",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-area-apoio-especializado-especialidade-tecnologia-da-informacao-trf-1-fgv-2024",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-area-apoio-especializado-tecnologia-da-informacao-trt-da-24-regiao-fgv-2025",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-area-apoio-especializado-tecnologia-da-informacao-trt-da-8-regiao-cebraspe-2022",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-area-de-apoio-especializado-governanca-e-gestao-de-tecnologia-da-informacao-trf-da-5-regiao-ibfc-2024",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-classe-c-analista-de-tecnologia-da-informacao-tj-mg-ibfc-2022",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-especialidade-analista-de-tecnologia-da-informacao-tjm-mg-instituto-consulplan-2021",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-gestao-e-governanca-de-tecnologia-da-informacao-tj-rr-fgv-2024",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-grupo-tecnologia-da-informacao-analista-de-gestao-de-tic-tj-rj-cebraspe-2021",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-grupo-tecnologia-da-informacao-analista-de-infraestrutura-de-tic-tj-rj-cebraspe-2021",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-grupo-tecnologia-da-informacao-analista-de-negocios-tj-rj-cebraspe-2021",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-grupo-tecnologia-da-informacao-analista-de-projetos-tj-rj-cebraspe-2021",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-grupo-tecnologia-da-informacao-analista-de-seguranca-da-informacao-tj-rj-cebraspe-2021",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-grupo-tecnologia-da-informacao-analista-de-sistemas-tj-rj-cebraspe-2021",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-infraestrutura-de-tecnologia-da-informacao-tj-rr-fgv-2024",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-infraestrutura-de-tecnologia-da-informacao-tj-pb-faperp-2012",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-suporte-em-tecnologia-da-informacao-tj-dft-fgv-2022",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-suporte-em-tecnologia-da-informacao-tj-dft-cespe-2015",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-suporte-em-tecnologia-da-informacao-stj-cespe-2015",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-suporte-em-tecnologia-da-informacao-stf-cespe-2013",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-suporte-em-tecnologia-da-informacao-stf-cespe-2008",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-tecnologia-da-informacao-tj-mt-fgv-2024",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-tecnologia-da-informacao-trt-da-13-regiao-fgv-2022",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-tecnologia-da-informacao-trt-13-fgv-2022",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-tecnologia-da-informacao-trt-24-fcc-2017",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-tecnologia-da-informacao-trt-11-fcc-2017",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-tecnologia-da-informacao-tj-ba-fgv-2015",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-tecnologia-da-informacao-trt-15-fcc-2015",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-tecnologia-da-informacao-trt-3-fcc-2015",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-tecnologia-da-informacao-trt-4-fcc-2015",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-tecnologia-da-informacao-trt-13-fcc-2014",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-tecnologia-da-informacao-trt-16-fcc-2014",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-tecnologia-da-informacao-trt-1-fcc-2014",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-tecnologia-da-informacao-trt-2-fcc-2014",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-tecnologia-da-informacao-trt-10-cespe-2013"
]

with open(LINKS_FILE, "w", encoding="utf-8") as f_links:
    for i, page_url in enumerate(URLS, 1):
        slug = page_url.rstrip("/").split("/")[-1]
        print(f"[{i}/{len(URLS)}] Analisando: {slug}...")

        try:
            req = urllib.request.Request(page_url, headers=HEADERS)
            with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
                html = resp.read().decode("utf-8", errors="ignore")

            pdf_matches = set(re.findall(r'href=["\']([^"\']+\.pdf)["\']', html))

            for link in pdf_matches:
                if not link.startswith("http"):
                    link = f"https://www.pciconcursos.com.br{link}"

                f_links.write(link + "\n")
                f_links.flush()

                filename = f"{slug}___{os.path.basename(link)}"
                dest_path = os.path.join(DEST_DIR, filename)

                if os.path.exists(dest_path):
                    print(f"   -> [Ja existe] {filename}")
                else:
                    print(f"   -> [Baixando] {filename}")
                    req_pdf = urllib.request.Request(link, headers=HEADERS)
                    with urllib.request.urlopen(req_pdf, context=ctx, timeout=30) as pdf_resp, open(dest_path, "wb") as f_out:
                        f_out.write(pdf_resp.read())

        except Exception as e:
            print(f"   -> [Erro]: {e}")

        time.sleep(0.4)

print(f"\nFinalizado! Arquivos salvos em '{DEST_DIR}' e links em '{LINKS_FILE}'.")

