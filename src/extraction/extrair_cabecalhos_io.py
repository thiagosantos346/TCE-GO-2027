import os
import json
import fitz  # PyMuPDF

def extract_pdf_headers(target_dirs):
    """
    Script estrito de I/O:
    Lê os arquivos PDF de provas (excluindo gabaritos) e extrai o texto bruto
    das 2 primeiras páginas (cabeçalho/capa) sem aplicar qualquer lógica determinística,
    regex ou filtros de palavras-chave.
    """
    records = []
    
    for d in target_dirs:
        if not os.path.exists(d):
            continue
        for fname in sorted(os.listdir(d)):
            if not fname.lower().endswith(".pdf"):
                continue
            # Ignora gabaritos apenas para focar nos cadernos de prova
            if "gab" in fname.lower():
                continue
                
            fpath = os.path.join(d, fname)
            try:
                doc = fitz.open(fpath)
                num_pages = len(doc)
                # Extrai texto bruto das 2 primeiras páginas
                pages_text = []
                for p_num in range(min(2, num_pages)):
                    page = doc[p_num]
                    text = page.get_text("text")
                    if text.strip():
                        pages_text.append(f"--- PÁGINA {p_num + 1} ---\n" + text.strip())
                doc.close()
                
                raw_header = "\n\n".join(pages_text)
                records.append({
                    "diretorio": d,
                    "arquivo": fname,
                    "caminho_completo": os.path.abspath(fpath),
                    "total_paginas": num_pages,
                    "texto_bruto_cabecalho": raw_header[:3000] # Primeiros 3.000 caracteres representativos
                })
            except Exception as e:
                records.append({
                    "diretorio": d,
                    "arquivo": fname,
                    "caminho_completo": os.path.abspath(fpath),
                    "erro": str(e)
                })

    return records

if __name__ == "__main__":
    dirs = ["raw_provas", "raw_provas_v3"]
    extracted = extract_pdf_headers(dirs)
    os.makedirs("data", exist_ok=True)
    out_path = os.path.join("data", "inventario_textos_brutos.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(extracted, f, ensure_ascii=False, indent=2)
    print(f"I/O concluído com sucesso. {len(extracted)} cadernos de prova processados.")
    print(f"Arquivo gerado: {out_path}")

