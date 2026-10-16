# -*- coding: utf-8 -*-
"""
PASSO 4: Script de Auditoria Final de Fontes Oficiais, Deep Linking e Estrutura (verify_sources.py)
Percorre todos os arquivos .md das 3 pastas:
  1. fontes_de_estudo/conhecimentos_gerais
  2. fontes_de_estudo/conhecimentos_especificos_b02_ti
  3. fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo

Verifica:
  - Presença da seção de Fontes Oficiais e Referências Bibliográficas;
  - Entre 4 e 7 Deep Links web verificados por arquivo .md + referências bibliográficas clássicas em ABNT (texto puro);
  - Proibição absoluta de URLs apontando apenas para a raiz/homepage de um domínio;
  - Proibição de domínios de baixa credibilidade ou links genéricos de editoras;
  - Validação HTTP (200 OK) de todas as URLs;
  - Preservação de emoticons e estrutura original (Ementa, Sumário, Questões).
"""

import pathlib
import re
import ssl
import sys
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

FOLDERS = [
    "fontes_de_estudo/conhecimentos_gerais",
    "fontes_de_estudo/conhecimentos_especificos_b02_ti",
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo",
]

BANNED_DOMAINS = {
    "somatematica.com.br",
    "www.somatematica.com.br",
    "soportugues.com.br",
    "www.soportugues.com.br",
    "todamateria.com.br",
    "www.todamateria.com.br",
    "brasilescola.uol.com.br",
    "mundoeducacao.uol.com.br",
    "infoescola.com",
    "www.infoescola.com",
    "normaculta.com.br",
    "www.normaculta.com.br",
    "portugues.com.br",
    "www.portugues.com.br",
    "guiadacarreira.com.br",
    "significados.com.br",
    "www.significados.com.br",
    "blog.cleancoder.com",
    "devmedia.com.br",
    "www.devmedia.com.br",
    "w3schools.com",
    "www.w3schools.com",
    "geeksforgeeks.org",
    "www.geeksforgeeks.org",
    "javatpoint.com",
    "www.javatpoint.com",
    "tutorialspoint.com",
    "www.tutorialspoint.com",
    # Editoras comerciais genéricas (livros físicos devem ficar em ABNT puro sem link falso)
    "grupogen.com.br",
    "www.grupogen.com.br",
    "pearson.com",
    "www.pearson.com",
    "wiley.com",
    "www.wiley.com",
    "altabooks.com.br",
    "www.altabooks.com.br",
    "vozes.com.br",
    "www.vozes.com.br",
    "record.com.br",
    "www.record.com.br",
    "sextante.com.br",
    "www.sextante.com.br",
    "mheducation.com",
    "www.mheducation.com",
    "harpercollins.com",
    "www.harpercollins.com",
    "manole.com.br",
    "www.manole.com.br",
    "grupoa.com.br",
    "www.grupoa.com.br",
    "editorajuspodivm.com.br",
    "www.editorajuspodivm.com.br",
    "editorasenacsp.com.br",
    "www.editorasenacsp.com.br",
    "us.sagepub.com",
}

GENERIC_ROOT_PATHS = {
    "",
    "index.html",
    "index.php",
    "index.htm",
    "home",
    "pt",
    "pt-br",
    "en",
    "en-us",
    "br",
    "tesouronacional/pt-br",
    "governodigital/pt-br",
    "anpd/pt-br",
    "compras/pt-br",
}


def is_root_or_generic_url(url: str) -> bool:
    parsed = urllib.parse.urlparse(url)
    path = parsed.path.strip("/").lower()
    if path in GENERIC_ROOT_PATHS and not parsed.query and not parsed.fragment:
        return True
    return False


def check_url_http(url: str, retries: int = 2):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml,application/pdf;q=0.9,*/*;q=0.8",
        "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    }
    last_err = None
    for attempt in range(retries + 1):
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
                status = resp.getcode()
                return status, None
        except urllib.error.HTTPError as e:
            last_err = f"HTTP {e.code}"
            if e.code in (404, 403, 401, 410):
                return e.code, last_err
        except Exception as e:
            last_err = str(e)
        if attempt < retries:
            time.sleep(0.8)
    return 0, last_err


def extract_sources_section(text: str):
    # Match ## or ### heading that clearly starts the Sources/References section
    matches = list(
        re.finditer(
            r"(^#{2,3}\s+[^\n]*(?:Fontes\s+Oficiais|Fontes\s+Recomendadas|Referências\s+Bibliográficas)[^\n]*\n)(.*?)(?=^#{2,3}\s+|\Z)",
            text,
            flags=re.M | re.S | re.I,
        )
    )
    if matches:
        m = matches[-1]
        return m.group(1).strip(), m.group(2)
    return None, None


def main():
    targets = sys.argv[1:] if len(sys.argv) > 1 else FOLDERS
    topic_files = []
    for t in targets:
        p = pathlib.Path(t)
        if p.is_file() and p.suffix == ".md" and p.name != "README.md":
            topic_files.append(p)
        elif p.is_dir():
            for sub in sorted(p.rglob("*.md")):
                if sub.name != "README.md":
                    topic_files.append(sub)

    print("=" * 78)
    print(f" AUDITORIA DE FONTES OFICIAIS E DEEP LINKING ({len(topic_files)} arquivos .md)")
    print("=" * 78)

    file_errors = {}
    all_urls = set()
    file_urls = {}

    for p in topic_files:
        rel = p.as_posix()
        txt = p.read_text(encoding="utf-8")
        errs = []

        # 1. Check original structure & emojis
        if "📌" not in txt or "🧭" not in txt:
            errs.append("Emojis obrigatórios de estrutura (📌 Ementa / 🧭 Sumário) ausentes.")
        q_count = len(re.findall(r"^###\s+Questão\s+\d+", txt, flags=re.M | re.I))
        if q_count < 5:
            errs.append(f"Esperadas >= 5 questões comentadas, encontradas: {q_count}")

        # 2. Extract Fontes section
        heading, sec = extract_sources_section(txt)
        if not sec:
            errs.append("Seção de Fontes Oficiais e Referências Bibliográficas ausente.")
            file_urls[rel] = []
        else:
            # Extract markdown links [label](url) or raw urls inside the section
            urls = [u.rstrip(".,;:") for u in re.findall(r"https?://[^\s\)\>\]\"`]+", sec)]
            file_urls[rel] = urls
            if len(urls) < 4 or len(urls) > 7:
                errs.append(f"Quantidade de links web fora do intervalo [4, 7]: encontrados {len(urls)} links.")

            # Verify presence of at least 1 pure-text ABNT reference (bullet item without http:// or https://)
            bullet_lines = [
                line.strip()
                for line in sec.splitlines()
                if re.match(r"^\s*[-*]\s+", line) and "http://" not in line and "https://" not in line
            ]
            abnt_lines = [
                bl for bl in bullet_lines
                if re.search(r"[A-ZÁÉÍÓÚÂÊÔÃÕÇ]{2,},\s+[A-ZÁÉÍÓÚÂÊÔÃÕÇ]", bl)
            ]
            if not abnt_lines:
                errs.append("Ausência de referência bibliográfica clássica em padrão ABNT (texto puro sem link falso).")

            for u in urls:
                all_urls.add(u)
                parsed = urllib.parse.urlparse(u)
                domain = parsed.netloc.lower()
                if is_root_or_generic_url(u):
                    errs.append(f"Proibido link de homepage/raiz genérica: {u}")
                if domain in BANNED_DOMAINS or any(domain.endswith("." + bd) for bd in BANNED_DOMAINS):
                    errs.append(f"Domínio de baixa credibilidade ou editora genérica proibido: {u}")

        if errs:
            file_errors[rel] = errs

    print(f"Validando via HTTP {len(all_urls)} URLs únicas...")
    http_status = {}
    with ThreadPoolExecutor(max_workers=20) as ex:
        futs = {ex.submit(check_url_http, u): u for u in all_urls}
        for fut in as_completed(futs):
            u = futs[fut]
            http_status[u] = fut.result()

    for rel, urls in file_urls.items():
        for u in urls:
            st, err = http_status.get(u, (0, "Not checked"))
            if st != 200:
                file_errors.setdefault(rel, []).append(f"URL falhou na validação HTTP [{st} - {err}]: {u}")

    total_err_files = len(file_errors)
    if total_err_files == 0:
        print("\n" + "=" * 78)
        print(f" [SUCESSO ABSOLUTO] 100% dos {len(topic_files)} arquivos .md e {len(all_urls)} Deep Links aprovados!")
        print("=" * 78)
        sys.exit(0)
    else:
        print(f"\n[FALHOU] {total_err_files} de {len(topic_files)} arquivo(s) possuem pendências:")
        for rel, errs in sorted(file_errors.items()):
            print(f"\n  Arquivo: {rel}")
            for e in errs:
                print(f"    - {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
