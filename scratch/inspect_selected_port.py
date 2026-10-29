import json

with open('banco_questoes_extraidas.json', 'r', encoding='utf-8') as f:
    questoes = json.load(f).get('questoes', [])

selected_ids = [
    'TJAP-2023-FGV-Q07', # Teste 001 (Argumentação / Método de Resolução)
    'TRT1-2014-FCC-Q16', # Teste 002 (Contexto / Posicionamento do autor - FCC)
    'TRT16-2022-FGV-Q10', # Teste 003 (Exposição e Crítica de Imprensa)
    'TRT6-2012-FCC-Q08',  # Teste 004 (Sentido / Pressupostos - FCC)
    'TJAP-2023-FGV-Q06', # Teste 006 (Linguagem Conotativa / Sentido de palavra)
    'TJAP-2023-FGV-Q23', # Teste 007 (Discurso e Narrativa / Discurso Indireto)
    'TRT-2024-FGV-Q13',  # Teste 008 (Transposição / Forma Negativa e Positiva)
    'TRT16-2022-FGV-Q04', # Teste 009 (Citação e Alusão)
    'TRT-2024-FGV-Q11'   # Teste 010 (Sentido Figurado / Figuras de Linguagem)
]

found = {}
for q in questoes:
    qid = q.get('id')
    if qid in selected_ids and qid not in found:
        found[qid] = q

print(f"Total encontradas: {len(found)} de {len(selected_ids)}")
for qid in selected_ids:
    q = found.get(qid)
    if q:
        print(f"\n==================== {qid} ====================")
        print(f"Banca: {q.get('banca')} | Órgão: {q.get('orgao')} | Cargo: {q.get('cargo')} | Ano: {q.get('ano')}")
        print("Enunciado:\n" + q.get('enunciado').strip())
        print("Alternativas:")
        for l, txt in sorted(q.get('alternativas', {}).items()):
            print(f"  * **{l})** {txt.strip().replace(chr(10), ' ')}")
        print(f"Gabarito: {q.get('gabarito_oficial')}")

