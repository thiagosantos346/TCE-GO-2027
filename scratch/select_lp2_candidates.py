import json

data = json.load(open('banco_questoes_extraidas.json', 'r', encoding='utf-8'))
questoes_dict = {q['id']: q for q in data['questoes']}

# Lista de IDs candidatos
ids = [
    'TJRR-2024-FGV-Q06',          # Teste 012: Bechara / Novo Acordo Ortografico / Acentuacao e Grafia
    'TRTDA24REGIO-2025-FGV-Q06',  # Teste 013: Acento indicativo e regras de acentuacao
    'TJAP-2023-FGV-Q01',          # Teste 014: Houaiss / Formação de Palavras / Elementos de Composição
    'TJAP-2023-FGV-Q04',          # Teste 015: Termo preposicionado vs Vocábulo único / Derivação
    'TRT-2024-FGV-Q01',           # Teste 016: Expressões impróprias / Semântica e Vocabulário
    'TRT-2024-FGV-Q03',           # Teste 017: Emprego e concisão vocabular / Redundância
    'TRT-2024-FGV-Q10',           # Teste 018: Locuções adjetivas substituídas por adjetivos / Morfologia
    'TRT-2009-FCC-Q16',           # Teste 019: Substituição vocabular e correção semântica
    'TRT-2009-FCC-Q17',           # Teste 020: Correção no emprego do elemento / Homônimos e Parônimos
    'TRT14-2016-FCC-Q13'          # Teste 021: Adequação e grafia de elementos sublinhados
]

for qid in ids:
    q = questoes_dict.get(qid)
    if not q:
        print(f"NOT FOUND: {qid}")
        continue
    print("=" * 60)
    print(f"ID: {qid} | {q['banca']} - {q['orgao']} - {q['cargo']} - {q['ano']}")
    print(f"ENUNCIADO: {q['enunciado'][:200].replace(chr(10), ' ')}")
    print(f"GABARITO: {q['gabarito_oficial']}")

