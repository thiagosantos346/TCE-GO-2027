#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
src/utils/scrubber.py

Fase 1: Limpeza Estrutural dos Arquivos Markdown.
Remove todos os blocos de questões (### Teste ...) dos arquivos em docs/,
preservando a teoria pura e respeitando a Blacklist estrita.
"""

import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DOCS_DIR = BASE_DIR / "docs"

# Blacklist de segurança (NÃO TOCAR)
BLACKLIST_PATHS = [
    "06_engenharia_software_ia_e_sistemas_agentivos",
    "04_lei_complementar_estadual_205_2025.md",
    "06_politicas_institucionais_e_resolucoes_normativas.md",
    "README.md",
    "relatorio_cobertura_questoes.md",
]


def is_blacklisted(path: Path) -> bool:
    path_str = path.as_posix()
    return any(b in path_str for b in BLACKLIST_PATHS)


def clean_markdown_file(path: Path) -> int:
    """Lê o arquivo, remove os blocos de teste via regex e salva.
    Retorna a quantidade de blocos removidos.
    """
    text = path.read_text(encoding="utf-8")
    matches = len(re.findall(r"### Teste", text))
    if matches == 0:
        return 0

    # Remove os blocos de questões iniciados por ### Teste até a próxima seção (## ) ou fim do arquivo
    cleaned = re.sub(r"### Teste.*?(?=\n## |\Z)", "", text, flags=re.DOTALL)
    # Higieniza delimitadores horizontais duplicados ou vazios antes de novas seções
    cleaned = re.sub(r"---\s*\n+(\n## )", r"---\n\1", cleaned)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)

    path.write_text(cleaned, encoding="utf-8")
    return matches


def main():
    print(f"[*] Iniciando Limpeza Estrutural em: {DOCS_DIR}")
    total_files = 0
    cleaned_files = 0
    total_tests_removed = 0
    skipped_files = 0

    for md_file in sorted(DOCS_DIR.rglob("*.md")):
        total_files += 1
        if is_blacklisted(md_file):
            skipped_files += 1
            continue

        removed = clean_markdown_file(md_file)
        if removed > 0:
            cleaned_files += 1
            total_tests_removed += removed
            print(f"  [LIMPO] {md_file.relative_to(DOCS_DIR)} (-{removed} testes)")

    print("\n[+] Relatório de Limpeza Estrutural:")
    print(f"  - Total de arquivos .md analisados: {total_files}")
    print(f"  - Arquivos higienizados: {cleaned_files}")
    print(f"  - Arquivos preservados na Blacklist: {skipped_files}")
    print(f"  - Total de blocos de questões apagados: {total_tests_removed}")


if __name__ == "__main__":
    main()

