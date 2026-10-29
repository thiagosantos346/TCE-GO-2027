import json
import re

with open('banco_questoes_extraidas.json', 'r', encoding='utf-8') as f:
    questoes = json.load(f).get('questoes', [])

candidates = [q for q in questoes if q.get('target_file') == 'fontes_de_estudo/conhecimentos_gerais/01_lingua_portuguesa/01_compreensao_e_interpretacao_de_texto.md']

target_sections = [
    '### 1.4 Método Prático de Resolução',
    '### 2.3 Contexto Histórico, Cultural e Ideológico',
    '### 3.3 Exposição e Injunção',
    '### 4.4 Pressupostos e Subentendidos',
    '### 5.2 Linguagem Conotativa',
    '### 6.3 Discurso Indireto Livre',
    '### 7.2 Correlação Verbal e Armadilhas na Transposição',
    '### 8.3 Citação, Epígrafe e Alusão',
    '### 9.4 Figuras Sonoras ou Fonéticas'
]

def norm(t):
    return re.sub(r'\W+', '', (t or '').lower())[:60]

seen = set()
for sec in target_sections:
    print(f"\n==================== SEÇÃO: {sec} ====================")
    matched = [q for q in candidates if q.get('target_section') == sec]
    unique_matched = []
    for q in matched:
        k = norm(q.get('enunciado'))
        if k not in seen:
            seen.add(k)
            alts = q.get('alternativas', {})
            if isinstance(alts, dict) and len(alts) >= 4 and q.get('gabarito_oficial'):
                unique_matched.append(q)
    print(f"Encontradas {len(unique_matched)} questões únicas:")
    for q in unique_matched[:3]:
        print(f"  [{q['id']}] {q.get('banca')} {q.get('orgao')} {q.get('ano')}")
        print("    Enunc:", q.get('enunciado')[:110].strip().replace('\n', ' '))
        print("    Gabarito:", q.get('gabarito_oficial'))

