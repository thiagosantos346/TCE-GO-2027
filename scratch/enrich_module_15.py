# -*- coding: utf-8 -*-
"""
Script to enrich Module 15: Noções de Direito Administrativo (6 files).
Preserves existing questions 01-05 intact.
Adds Questão 06 to 11 (or 10 for file 06) after uncovered theoretical subtopics.
"""

import os
import re

BASE_DIR = "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/15_nocoes_de_direito_administrativo"

def inject_after_subtopic(content, subtopic_anchor, question_block):
    """
    Finds the end of the section identified by subtopic_anchor (before the next heading or ---)
    and inserts the question_block.
    """
    pattern = re.escape(subtopic_anchor)
    match = re.search(pattern, content)
    if not match:
        raise ValueError(f"Anchor not found: {subtopic_anchor}")
    
    start_pos = match.end()
    # Find next heading (### or ##) or horizontal rule (---) or EOF
    next_section = re.search(r"\n(?=###? |\Z)", content[start_pos:])
    if next_section:
        insert_idx = start_pos + next_section.start()
    else:
        insert_idx = len(content)
    
    # Ensure nice spacing
    new_content = content[:insert_idx].rstrip() + "\n\n" + question_block.strip() + "\n\n---\n\n" + content[insert_idx:].lstrip()
    return new_content

print("Helper defined.")
