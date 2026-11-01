#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/clean_database_artifacts.py

Limpeza de artefatos de cabeçalho e rodapé de página capturados na extração OCR/PDF
das provas oficiais (ex: 'TRIBUNAL DE CONTAS DO ESTADO DE GOIÁS FGV CONHECIMENTO', etc.).
Preserva o texto das questões estritamente ipsis litteris.
"""

import json
import re

DB_FILE = 'banco_questoes_extraidas.json'

PATTERNS = [
    r'\n\s*TRIBUNAL DE CONTAS[^\n]*',
    r'\n\s*ANALISTA JUDICIÁRIO[^\n]*',
    r'\n\s*ANALISTA DE CONTROLE[^\n]*',
    r'\n\s*TÉCNICO JUDICIÁRIO[^\n]*',
    r'\n\s*TÉCNICO DE CONTROLE[^\n]*',
    r'\n\s*CONHECIMENTOS ESPECÍFICOS[^\n]*',
    r'\n\s*CONHECIMENTOS GERAIS[^\n]*',
    r'\n\s*PROVA OBJETIVA[^\n]*',
    r'\n\s*FGV CONHECIMENTO[^\n]*',
    r'\n\s*TIPO BRANCA[^\n]*',
    r'\n\s*TIPO \d[^\n]*',
    r'\n\s*PÁGINA \d+[^\n]*'
]

def clean_text(text):
    if not text:
        return text
    cleaned = text
    for pat in PATTERNS:
        cleaned = re.sub(pat, '', cleaned, flags=re.IGNORECASE)
    return cleaned.strip()

def run():
    print(f"Carregando {DB_FILE}...")
    with open(DB_FILE, 'r', encoding='utf-8') as f:
        db = json.load(f)

    cleaned_alternatives = 0
    cleaned_enunciados = 0

    for q in db['questoes']:
        orig_enunciado = q.get('enunciado', '')
        new_enunciado = clean_text(orig_enunciado)
        if new_enunciado != orig_enunciado:
            q['enunciado'] = new_enunciado
            cleaned_enunciados += 1

        alts = q.get('alternativas', {})
        for k, v in alts.items():
            new_v = clean_text(v)
            if new_v != v:
                alts[k] = new_v
                cleaned_alternatives += 1

    print(f"Limpeza concluída:")
    print(f"  - Enunciados limpos: {cleaned_enunciados}")
    print(f"  - Alternativas limpas: {cleaned_alternatives}")

    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent=2)
    print(f"Arquivo {DB_FILE} salvo com sucesso.")

if __name__ == '__main__':
    run()
