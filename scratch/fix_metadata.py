import json
import re

with open('banco_questoes_extraidas.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

tce_go_fixed = 0
tce_pa_fixed = 0
trt_fixed = 0

for q in data['questoes']:
    text = q['enunciado'] + ' ' + ' '.join(q['alternativas'].values())
    
    # Detecção de TCE-GO
    if 'TRIBUNAL DE CONTAS DO ESTADO DE GOIÁS' in text or 'TCE-GO' in text or 'TCE -GO' in text or 'Lei nº 16.168' in text:
        q['orgao'] = 'TCE-GO'
        if 'CIENCIAS CONTABEIS' in text:
            q['cargo'] = 'Analista de Controle Externo - Ciências Contábeis'
        elif 'TECNOLOGIA DA INFORMACAO' in text:
            q['cargo'] = 'Analista de Controle Externo - Tecnologia da Informação'
        elif 'CONTROLE EXTERNO' in text:
            q['cargo'] = 'Analista de Controle Externo - Controle Externo'
        else:
            q['cargo'] = 'Analista de Controle Externo'
        tce_go_fixed += 1

    # Detecção de TCE-PA
    elif 'TRIBUNAL DE CONTAS DO ESTADO DO PARÁ' in text or 'TCE-PA' in text:
        q['orgao'] = 'TCE-PA'
        q['cargo'] = 'Auditor de Controle Externo'
        tce_pa_fixed += 1

print(f"Metadados corrigidos:")
print(f"- TCE-GO: {tce_go_fixed} questões")
print(f"- TCE-PA: {tce_pa_fixed} questões")

with open('banco_questoes_extraidas.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("banco_questoes_extraidas.json atualizado com metadados reais de TCE-GO e TCE-PA!")

