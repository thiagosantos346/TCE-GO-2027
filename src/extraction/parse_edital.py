#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
src/extraction/parse_edital.py

Fase 1: Parser do Edital (Geração do JSON Estruturado).
Lê o arquivo data/ANEXO II.md e extrai:
- Áreas (Conhecimentos Gerais, Específicos A01, Específicos B02)
- Matérias dentro das áreas
- Tópicos (quebrando os parágrafos das matérias por ponto ou ponto e vírgula, preservando números de leis e versões)
Salva a saída estruturada em data/edital_estruturado.json.
"""

import json
import os
import re

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
INPUT_MD = os.path.join(BASE_DIR, "data", "ANEXO II.md")
OUTPUT_JSON = os.path.join(BASE_DIR, "data", "edital_estruturado.json")

MATERIAS_CONHECIDAS = {
    "Língua Portuguesa",
    "Matemática e Raciocínio Lógico",
    "Legislação Institucional",
    "Noções de Direito Administrativo",
    "Licitações e Contratos Administrativos",
    "Noções de Direito Constitucional",
    "Noções de Controle Externo",
    "Noções de Administração Financeira e Orçamentária",
    "Contabilidade aplicada ao Setor Público",
    "Noções de Administração Pública",
    "Administração Geral",
    "Administração Estratégica",
    "Comportamento Organizacional",
    "Gestão de Pessoas",
    "Engenharia de Software",
    "Desenvolvimento de Sistemas",
    "Engenharia de Software Assistida por Inteligência Artificial e Sistemas Agentivos",
    "DevOps, Plataforma de Desenvolvimento e Engenharia de Entrega",
    "Banco de Dados",
    "Inteligência Artificial, Ciência de Dados e Automação",
    "Segurança da Informação",
    "Sistemas Operacionais, Redes e Computação em Nuvem",
    "Governança de Tecnologia da Informação",
    "Legislação Aplicada à Tecnologia da Informação",
    "Língua Inglesa (Leitura Técnica)",
}


def mapear_nome_area(titulo_original: str) -> str:
    upper = titulo_original.upper()
    if "CONHECIMENTOS GERAIS" in upper:
        return "CONHECIMENTOS GERAIS (A01 E B02)"
    if "CARGO A01" in upper:
        return "CONHECIMENTOS ESPECÍFICOS A01 - TÉCNICO ADMINISTRATIVO"
    if "CARGO B02" in upper:
        return "CONHECIMENTOS ESPECÍFICOS B02 - TI"
    return titulo_original


def quebrar_topicos(texto_materia: str) -> list[str]:
    """
    Divide o parágrafo de uma matéria em tópicos por ponto (.) ou ponto e vírgula (;),
    protegendo pontos dentro de números de leis (ex: 14.133), versões (ex: 2.0, 1.0)
    e tecnologias (ex: Node.js).
    """
    texto = re.sub(r"\s+", " ", texto_materia).strip()

    # Protege pontos entre dígitos (ex: 14.133, 2.0) e Node.js
    texto_protegido = re.sub(r"(?<=\d)\.(?=\d)", "<DOT_NUM>", texto)
    texto_protegido = re.sub(r"Node\.js", "Node<DOT_JS>js", texto_protegido, flags=re.IGNORECASE)

    partes = re.split(r"[.;]\s*", texto_protegido)

    topicos = []
    for p in partes:
        item = p.replace("<DOT_NUM>", ".").replace("<DOT_JS>", ".").strip()
        # Remove pontuação residual no final se houver
        item = item.rstrip(".; ")
        if item and len(item) > 2:
            topicos.append(item)
    return topicos


def parse_edital(md_path: str) -> dict:
    with open(md_path, "r", encoding="utf-8") as f:
        raw_lines = [line.strip() for line in f.readlines()]

    # Filtra linhas vazias e números de página isolados (ex: "22", "23", "24")
    lines = []
    for line in raw_lines:
        if not line:
            continue
        if re.fullmatch(r"\d+", line):
            continue
        lines.append(line)

    # Une cabeçalhos de Áreas que estão quebrados em 2 linhas no ANEXO II.md
    merged_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("CONHECIMENTOS GERAIS") or line.startswith("CONHECIMENTOS ESPECÍFICOS"):
            combined = line
            while i + 1 < len(lines) and (
                lines[i + 1].isupper()
                and lines[i + 1] not in MATERIAS_CONHECIDAS
                and not lines[i + 1].startswith("CONHECIMENTOS ")
            ):
                combined += " " + lines[i + 1]
                i += 1
            merged_lines.append(combined)
        else:
            merged_lines.append(line)
        i += 1

    areas = []
    current_area = None
    current_materia = None
    buffer_texto = []

    def flush_materia():
        nonlocal current_materia, buffer_texto
        if current_area is not None and current_materia is not None and buffer_texto:
            texto_completo = " ".join(buffer_texto)
            topicos = quebrar_topicos(texto_completo)
            current_area["materias"].append(
                {
                    "nome_materia": current_materia,
                    "topicos": topicos,
                }
            )
        current_materia = None
        buffer_texto = []

    for line in merged_lines:
        if line.startswith("CONHECIMENTOS GERAIS") or line.startswith("CONHECIMENTOS ESPECÍFICOS"):
            flush_materia()
            current_area = {
                "nome_area": mapear_nome_area(line),
                "titulo_original": line,
                "materias": [],
            }
            areas.append(current_area)
        elif line in MATERIAS_CONHECIDAS:
            flush_materia()
            current_materia = line
        else:
            if current_materia is not None:
                buffer_texto.append(line)

    flush_materia()

    return {
        "concurso": "TCE-GO 2027",
        "areas": areas,
    }


def main():
    if not os.path.exists(INPUT_MD):
        raise FileNotFoundError(f"Arquivo não encontrado: {INPUT_MD}")

    dados = parse_edital(INPUT_MD)
    os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

    total_areas = len(dados["areas"])
    total_materias = sum(len(a["materias"]) for a in dados["areas"])
    total_topicos = sum(len(m["topicos"]) for a in dados["areas"] for m in a["materias"])
    print(f"[FASE 1 CONCLUÍDA] Edital estruturado salvo em: {OUTPUT_JSON}")
    print(f" -> Áreas: {total_areas} | Matérias: {total_materias} | Tópicos: {total_topicos}")


if __name__ == "__main__":
    main()

