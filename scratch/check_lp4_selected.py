import json

data = json.load(open('banco_questoes_extraidas.json', 'r', encoding='utf-8'))
questoes_dict = {q['id']: q for q in data['questoes']}

ids = [
    'TRT-2024-FGV-Q08',   # Teste 032: Conjunção OU / Relações Lógicas
    'TRT13-2014-FCC-Q08',  # Teste 033: Palavra QUE / Funções e Subordinação
    'TRT24-2017-FCC-Q03',  # Teste 034: Relação de Causa e Efeito
    'TRT-2024-FGV-Q09',   # Teste 035: Oração Adversativa / Relações Semânticas
    'TRT1-2014-FCC-Q12',  # Teste 036: Expressão de Causa e Consequência no contexto
    'TRT4-2015-FCC-Q03',  # Teste 037: Circunstância Restritiva
    'TRT-2024-FGV-Q10',   # Teste 038: Termo indicativo de Causa
    'TRT1-2014-FCC-Q13',  # Teste 039: Pontuação plenamente adequada
    'TRT24-2017-FCC-Q09', # Teste 040: Comentário sobre a Pontuação do texto
    'TRT1-2014-FCC-Q15'   # Teste 041: Falha estrutural de redação e pontuação
]

for qid in ids:
    q = questoes_dict.get(qid)
    print("=" * 60)
    print(f"ID: {qid} | {q['banca']} - {q['orgao']} - {q['cargo']} - {q['ano']}")
    print(q['enunciado'][:160].replace(chr(10), ' '))
    print(f"GAB: {q['gabarito_oficial']}")

