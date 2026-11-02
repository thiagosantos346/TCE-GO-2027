import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DOCS_DIR = BASE_DIR / "docs"

BLACKLIST = [
    "06_engenharia_software_ia_e_sistemas_agentivos",
    "04_lei_complementar_estadual_205_2025.md",
    "06_politicas_institucionais_e_resolucoes_normativas.md"
]

def clean_markdowns():
    arquivos_limpos = 0
    for md_file in DOCS_DIR.rglob("*.md"):
        if any(b in str(md_file) for b in BLACKLIST):
            continue

        texto = md_file.read_text(encoding="utf-8")
        # Remove do ### Teste até o próximo ## ou fim do arquivo
        novo_texto = re.sub(r'### Teste.*?(?=\n## |\Z)', '', texto, flags=re.DOTALL)

        if texto != novo_texto:
            # Remove quebras de linha excessivas no final
            novo_texto = re.sub(r'\n{3,}', '\n\n', novo_texto).strip() + '\n'
            md_file.write_text(novo_texto, encoding="utf-8")
            arquivos_limpos += 1
            
    print(f"Limpeza concluída. {arquivos_limpos} arquivos higienizados.")

if __name__ == "__main__":
    clean_markdowns()