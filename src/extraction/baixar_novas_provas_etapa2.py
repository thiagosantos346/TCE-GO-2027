import os
import json
import requests
import re

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DEST_DIR = os.path.join(BASE_DIR, "raw_provas")
WHITELIST_FILE = os.path.join(BASE_DIR, "provas_recomendadas_whitelist.json")

def sanitize_slug(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text[:70]

def main():
    with open(WHITELIST_FILE, "r", encoding="utf-8") as f:
        provas = json.load(f)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    print(f"=== ETAPA 2: AQUISIÇÃO E DOWNLOAD DE NOVAS PROVAS ===")
    print(f"Total de provas qualificadas a baixar: {len(provas)}")

    baixadas = 0
    erros = 0

    for idx, p in enumerate(provas, 1):
        orgao = p.get("orgao", "orgao")
        ano = p.get("ano", "ano")
        banca = p.get("banca", "banca")
        cargo = p.get("cargo", "cargo")
        prio = p.get("prio", 2)
        
        slug_base = sanitize_slug(f"{cargo}-{orgao}-{banca}-{ano}")
        
        prova_url = p.get("prova_link")
        gabarito_url = p.get("gabarito_link")
        
        # Download Prova
        if prova_url:
            nome_prova = prova_url.rstrip("/").split("/")[-1]
            dest_prova = os.path.join(DEST_DIR, f"{slug_base}___{nome_prova}")
            if not os.path.exists(dest_prova):
                try:
                    r = requests.get(prova_url, headers=headers, timeout=15)
                    if r.status_code == 200 and r.content.startswith(b"%PDF"):
                        with open(dest_prova, "wb") as fp:
                            fp.write(r.content)
                        print(f"[{idx}/{len(provas)}] [Prio {prio}] Prova baixada: {slug_base}___{nome_prova} ({len(r.content)} bytes)")
                        baixadas += 1
                    else:
                        print(f"[{idx}/{len(provas)}] Prova não retornou PDF válido ({r.status_code}): {prova_url}")
                        erros += 1
                except Exception as e:
                    print(f"[{idx}/{len(provas)}] Erro ao baixar prova {prova_url}: {e}")
                    erros += 1
            else:
                print(f"[{idx}/{len(provas)}] Prova já existente: {nome_prova}")

        # Download Gabarito
        if gabarito_url:
            nome_gab = gabarito_url.rstrip("/").split("/")[-1]
            dest_gab = os.path.join(DEST_DIR, f"{slug_base}___{nome_gab}")
            if not os.path.exists(dest_gab):
                try:
                    r = requests.get(gabarito_url, headers=headers, timeout=15)
                    if r.status_code == 200 and r.content.startswith(b"%PDF"):
                        with open(dest_gab, "wb") as fp:
                            fp.write(r.content)
                        print(f"[{idx}/{len(provas)}] [Prio {prio}] Gabarito baixado: {slug_base}___{nome_gab}")
                        baixadas += 1
                    else:
                        print(f"[{idx}/{len(provas)}] Gabarito não retornou PDF válido ({r.status_code}): {gabarito_url}")
                        erros += 1
                except Exception as e:
                    print(f"[{idx}/{len(provas)}] Erro ao baixar gabarito {gabarito_url}: {e}")
                    erros += 1
            else:
                print(f"[{idx}/{len(provas)}] Gabarito já existente: {nome_gab}")

    print(f"\n--- RESUMO DO DOWNLOAD DA ETAPA 2 ---")
    print(f"Arquivos baixados com sucesso: {baixadas}")
    print(f"Erros de download: {erros}")

if __name__ == "__main__":
    main()

