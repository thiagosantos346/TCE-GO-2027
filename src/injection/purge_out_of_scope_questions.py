#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/purge_out_of_scope_questions.py

FASE 2: Sanitização e expurgo implacável do banco de questões (banco_questoes_extraidas.json).
Remove permanentemente questões de áreas estranhas ao escopo de Controle Externo (TI e Técnico-Administrativo):
- Ciências Atuariais (tábuas biométricas, comutações, anuidades vitais, notação de Gerber)
- Engenharia Civil / Rodoviária / Estruturas / Solos / Saneamento (vigas, solos, concreto armado, drenagem rodoviária, estabilização)
- Engenharia Mecânica / Térmica (termodinâmica, Carnot, caldeiras, entalpia)
- Saúde / Odontologia / Medicina clínica
- Biologia pura / Zoologia
- Legislação institucional local restrita a outros tribunais estaduais (TJ-AP, TJ-RR, TJ-MT)
"""

import json
import os
import re

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
DB_FILE = os.path.join(BASE_DIR, 'data', 'banco_questoes_extraidas.json')

def should_purge(q):
    enunc = q.get('enunciado', '')
    alts = ' '.join(q.get('alternativas', {}).values())
    text = (enunc + ' ' + alts).lower()

    # 1. Ciências Atuariais
    atuarial_patterns = [
        r'\bnotação\s+atuarial\b',
        r'\bhans-ulrich\s+gerber\b',
        r'\btábuas?\s+biométrica\b',
        r'\bcomutaç(ão|ões)\s+atuaria(l|is)\b',
        r'\bprovisões?\s+matemática\b',
        r'\banuidade\s+vitalícia\b',
        r'\bcomutações\s+tabuladas\b',
        r'\bprobabilidade\s+kpx\b',
        r'\bavaliação\s+atuarial\b',
        r'\bseguro\s+dotal\s+puro\b'
    ]
    for p in atuarial_patterns:
        if re.search(p, text):
            return True, 'Ciências Atuariais'

    # 2. Engenharia Civil, Rodoviária, Saneamento, Estruturas e Solos
    civil_patterns = [
        r'\bviga\s+(biapoiada|biengastada|contínua|metálica)\b',
        r'\bviga\s+possui\s+seção\s+transversal\b',
        r'\bmomento\s+fletor\b',
        r'\besforço\s+cortante\b',
        r'\btreliça\b',
        r'\bconcreto\s+armado\b',
        r'\bensaio\s+spt\b',
        r'\bestaca\s+(raiz|hélice|frank|escavada|pré-moldada)\b',
        r'\bfundaç(ão|ões)\s+(rasa|profunda|direta|indireta)\b',
        r'\bsapatas?\s+(isolada|corrida|associada)\b',
        r'\btubul(ão|ões)\s+(a céu aberto|a ar comprimido)\b',
        r'\bclassificação\s+dos\s+solos\s+em\s+argila\b',
        r'\bmecânica\s+dos\s+solos\b',
        r'\btopografia\b',
        r'\blagoas?\s+de\s+estabiliz[aá]ção\b',
        r'\btratamento\s+de\s+esgoto\b',
        r'\bautodepuração\s+dos\s+corpos\s+d[\'’]água\b',
        r'\bpintura\s+de\s+edificações\b',
        r'\balvenaria\s+estrutural\b',
        r'\barmaduras?\s+de\s+flexão\b',
        r'\báguas\s+pluviais\b',
        r'\bcarga\s+uniformemente\s+distribuída\b.*?\bviga\b',
        r'\blajes?\s+maciças?\s+de\s+concreto\b',
        r'\bexecução\s+de\s+uma\s+estaca\b',
        r'\bescoramento\s+de\s+formas\b',
        r'\bprojetar\s+uma\s+rodovia.*?sistema\s+de\s+drenagem\b',
        r'\borçamento\s+de\s+uma\s+obra\s+compõe-se\b'
    ]
    for p in civil_patterns:
        if re.search(p, text):
            # Exceção para questões puramente de matemática (ex: conta de água com tabela tarifária)
            if 'tabela tarifária' in text and 'conta de água' in text:
                continue
            return True, 'Engenharia Civil/Sanitária/Rodoviária'

    # 3. Engenharia Mecânica / Termodinâmica / Térmica
    mecanica_patterns = [
        r'\bprimeira\s+lei\s+da\s+termodinâmica\b',
        r'\bsegunda\s+lei\s+da\s+termodinâmica\b',
        r'\bciclos?\s+termodinâmicos?\b',
        r'\bciclo\s+de\s+carnot\b',
        r'\bciclo\s+rankine\b',
        r'\bmáquinas?\s+térmicas?\b',
        r'\bdiagrama\s+temperatura\s*\(?t\)?\s*-\s*entropia\b',
        r'\bentalpia\b',
        r'\bescoamento\s+(laminar|turbulento)\b',
        r'\bnúmero\s+de\s+reynolds\b',
        r'\bcaldeiras?\s+aquatubular\b'
    ]
    for p in mecanica_patterns:
        if re.search(p, text):
            return True, 'Engenharia Mecânica/Térmica'

    # 4. Saúde / Odontologia / Medicina clínica
    saude_patterns = [
        r'\bclínica\s+odontológica\b',
        r'\bsaúde\s+bucal\b',
        r'\bcárie\s+dentária\b',
        r'\bperiodontite\b',
        r'\bposologia\s+do\s+medicamento\b',
        r'\bdiagnóstico\s+clínico\s+de\s+patologia\b',
        r'\bleitos?\s+de\s+uti\b',
        r'\bcuidados\s+de\s+enfermagem\b'
    ]
    for p in saude_patterns:
        if re.search(p, text):
            return True, 'Saúde/Medicina/Odontologia'

    # 5. Biologia / Animais
    bio_patterns = [
        r'\bcolibri\s+é\s+um\s+pequeno\s+exemplo\b',
        r'\bespécies\s+de\s+aves\s+migratórias\b',
        r'\btaxonomia\s+de\s+insetos\b'
    ]
    for p in bio_patterns:
        if re.search(p, text):
            return True, 'Biologia/Zoologia'

    # 6. Legislação local estrita de outros tribunais/estados
    legis_estranha_patterns = [
        r'\bLei\s+Complementar\s+(?:Estadual\s+)?n[ºo°]?\s*0?66/1993\b',
        r'\bRegimento\s+Interno\s+do\s+Tribunal\s+de\s+Justiça\s+do\s+Estado\s+do\s+Amapá\b',
        r'\bCódigo\s+de\s+Organização\s+Judiciária\s+do\s+Estado\s+do\s+Amapá\b',
        r'\bRegimento\s+Interno\s+do\s+Tribunal\s+de\s+Justiça\s+do\s+Estado\s+de\s+Roraima\b',
        r'\bRegimento\s+Interno\s+do\s+Tribunal\s+de\s+Justiça\s+do\s+Estado\s+de\s+Mato\s+Grosso\b',
        r'\bRegimento\s+Interno\s+do\s+TJ-?AP\b',
        r'\bRegimento\s+Interno\s+do\s+TJ-?RR\b',
        r'\bRegimento\s+Interno\s+do\s+TJ-?MT\b'
    ]
    for p in legis_estranha_patterns:
        if re.search(p, text):
            return True, 'Legislação Local Estranha'

    return False, None

def run_purge():
    print(f"Carregando {DB_FILE}...")
    with open(DB_FILE, 'r', encoding='utf-8') as f:
        db = json.load(f)

    questoes = db['questoes']
    total_antes = len(questoes)

    mantidas = []
    expurgadas = []

    for q in questoes:
        out, reason = should_purge(q)
        if out:
            expurgadas.append((q, reason))
        else:
            mantidas.append(q)

    print("=" * 70)
    print("RELATÓRIO DE EXPURGO DO BANCO DE DADOS:")
    print(f"Total antes: {total_antes}")
    print(f"Total expurgadas: {len(expurgadas)}")
    print(f"Total restantes no banco: {len(mantidas)}")
    print("=" * 70)

    # Detalhar categorias expurgadas
    from collections import Counter
    contagem_motivos = Counter(r for _, r in expurgadas)
    for mot, qtd in contagem_motivos.most_common():
        print(f" - {mot}: {qtd} questões")

    db['questoes'] = mantidas

    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

    print(f"\nBanco de dados salvo com sucesso com {len(mantidas)} questões legítimas.")

if __name__ == '__main__':
    run_purge()

