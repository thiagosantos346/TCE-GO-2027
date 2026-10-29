# -*- coding: utf-8 -*-
import json
import re

TARGET_FILE = 'fontes_de_estudo/conhecimentos_especificos_b02_ti/04_engenharia_de_software/01_ciclo_de_vida_e_metodologias_ageis.md'
DB_FILE = 'banco_questoes_extraidas.json'

with open(DB_FILE, 'r', encoding='utf-8') as f:
    db = json.load(f)

# pegar os objetos certos com 5 alternativas
q_scrum_fgv = None
q_sprint_review = None
for q in db['questoes']:
    if 'A metodologia Scrum é um framework que apoi' in q['enunciado'] and len(q.get('alternativas', {})) == 5:
        q_scrum_fgv = q
    elif 'Inspecionar o resultado do Sprint e determinar futuras' in q['enunciado'] and len(q.get('alternativas', {})) == 5:
        q_sprint_review = q

questoes_dict = {q['id']: q for q in db['questoes']}

replacements = [
    {
        "test_num": "001",
        "qid": "TRT1-2014-FCC-Q35",
        "header": "**(FCC – TRT-1 – Analista Judiciário (TI) – 2014)**",
        "comments": {
            "A": "Incorreta. A fase de Transição não tem como foco principal definir a visão do produto ou o modelo de negócio.",
            "B": "Correta. No RUP (Rational Unified Process), a fase de Concepção (Iniciação) foca em estabelecer o escopo do negócio e a viabilidade do sistema; a fase de Elaboração estabelece a linha de base da arquitetura e gerencia os maiores riscos técnicos; a fase de Construção desenvolve o software de forma iterativa; e a fase de Transição entrega o produto aos usuários finais.",
            "C": "Incorreta. A fase de Elaboração não é dispensável nem foca apenas na codificação final.",
            "D": "Incorreta. O RUP é um processo iterativo e incremental, e não estritamente cascata sequencial.",
            "E": "Incorreta. Os fluxos de trabalho (disciplinas) ocorrem ao longo de todas as fases em intensidades variáveis."
        }
    },
    {
        "test_num": "002",
        "qid": "TRT23-2016-FCC-Q38",
        "header": "**(FCC – TRT-23 – Analista Judiciário (TI) – 2016)**",
        "comments": {
            "A": "Incorreta. Na fase de Construção, o maior esforço recai sobre Implementação e Testes.",
            "B": "Incorreta. Na fase de Transição, o foco é Implantação e Treinamento de usuários.",
            "C": "Incorreta. A Modelagem de Negócios tem seu ápice nas fases iniciais do ciclo.",
            "D": "Incorreta. O esforço de Requisitos decresce acentuadamente nas iterações finais da Construção.",
            "E": "Correta. No Processo Unificado, as maiores cargas de trabalho das disciplinas de Modelagem de Negócios e de Requisitos ocorrem predominantemente nas fases de Concepção (Iniciação) e Elaboração, visando estabilizar os objetivos do sistema e mitigar riscos antes da fase de Construção em larga escala."
        }
    },
    {
        "test_num": "006",
        "q_obj": q_scrum_fgv,
        "header": "**(FGV – TJ-AP – Analista Judiciário (TI) – 2023)**",
        "comments": {
            "A": "Correta. Segundo o Scrum Guide oficial, o Scrum baseia-se no empirismo (transparência, inspeção e adaptação) e no pensamento enxuto (lean), onde um time auto-organizável e multifuncional colabora em iterações de tamanho fixo (Sprints) para gerar valor contínuo e produtos utilizáveis a cada incremento.",
            "B": "Incorreta. O Scrum Master não gerencia pessoas de forma prescritiva nem atribui tarefas individualmente aos desenvolvedores.",
            "C": "Incorreta. O Product Owner não define a estimativa de esforço das tarefas, papel privativo dos Developers.",
            "D": "Incorreta. O Sprint Backlog não é imutável durante o Sprint se o time identificar necessidades de ajuste com o PO.",
            "E": "Incorreta. O Scrum não adota papéis gerenciais tradicionais como Gerente de Projetos dentro do Time Scrum."
        }
    },
    {
        "test_num": "007",
        "q_obj": q_sprint_review,
        "header": "**(FGV – TRT-13 – Analista Judiciário (TI) – 2022)**",
        "comments": {
            "A": "Incorreta. A Daily Scrum é uma reunião diária interna de alinhamento e sincronização dos Developers com duração de 15 minutos.",
            "B": "Incorreta. A Sprint Planning ocorre no início do Sprint para planejar o trabalho a ser realizado.",
            "C": "Correta. O evento do Scrum cujo objetivo precípuo é inspecionar o resultado do Sprint (o incremento de produto potencialmente utilizável) e determinar futuras adaptações, no qual o Time Scrum apresenta os resultados aos principais stakeholders, é a Revisão do Sprint (Sprint Review).",
            "D": "Incorreta. A Sprint Retrospective ocorre após a Sprint Review e foca na inspeção e melhoria dos processos, pessoas e relacionamentos da equipe, e não na demonstração do incremento aos stakeholders.",
            "E": "Incorreta. O Refinamento do Backlog é uma atividade contínua de detalhamento e estimativa de itens, não um evento formal com stakeholders."
        }
    }
]

with open(TARGET_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

for item in replacements:
    t_num = item["test_num"]
    q_data = item.get("q_obj") or questoes_dict[item["qid"]]
    
    enunciado_limpo = q_data['enunciado'].strip()
    lines = [l.strip() for l in enunciado_limpo.split('\n') if l.strip()]
    formatted_enunciado = '\n\n'.join(lines) if any(l.startswith('I.') or l.startswith('II.') or l.startswith('(') for l in lines) else ' '.join(lines)
    
    alts_text = []
    for letter in ['A', 'B', 'C', 'D', 'E']:
        alt_val = ' '.join(q_data['alternativas'][letter].strip().split())
        alts_text.append(f"* **{letter})** {alt_val}")
    alternativas_block = '\n'.join(alts_text)
    
    comms = item["comments"]
    comm_block = []
    for letter in ['A', 'B', 'C', 'D', 'E']:
        comm_block.append(f"> - **{letter})** {comms[letter]}")
    comentarios_text = '\n'.join(comm_block)
    
    gab = q_data['gabarito_oficial']
    
    novo_bloco = f"""### Teste {t_num}
{item['header']}  
{formatted_enunciado}

{alternativas_block}

---

> **Comentário Detalhado:**
>
{comentarios_text}
>
> **Gabarito: {gab}**

---"""

    pattern = rf"### Teste {t_num}[\s\S]*?(?=(?:### Teste \d+|## \d+|\Z))"
    match = re.search(pattern, content)
    if not match:
        print(f"ERRO: Bloco Teste {t_num} não encontrado!")
        continue
    
    content = content[:match.start()] + novo_bloco + "\n\n" + content[match.end():]
    q_data['status_integracao'] = 'injetada'
    print(f"[OK] Injetado Teste {t_num} <- {q_data['id']} ({item['header']})")

with open(TARGET_FILE, 'w', encoding='utf-8') as f:
    f.write(content)

with open(DB_FILE, 'w', encoding='utf-8') as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print("\nProcessamento de 01_ciclo_de_vida_e_metodologias_ageis.md concluído com sucesso!")

