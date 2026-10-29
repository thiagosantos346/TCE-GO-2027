# -*- coding: utf-8 -*-
import json
import re

TARGET_FILE = 'fontes_de_estudo/conhecimentos_gerais/01_lingua_portuguesa/02_ortografia_acentuacao_e_formacao_de_palavras.md'
DB_FILE = 'banco_questoes_extraidas.json'

with open(DB_FILE, 'r', encoding='utf-8') as f:
    db = json.load(f)

questoes_dict = {q['id']: q for q in db['questoes']}

# Seleção de 10 questões reais com temas correlatos ao arquivo 02
replacements = [
    {
        "test_num": "012",
        "qid": "TJRR-2024-FGV-Q06",
        "header": "**(FGV – TJ-RR – Analista Judiciário (TI) – 2024)**",
        "prefix_text": "",
        "comments": {
            "A": "Incorreta. A obra explicita 'Mais de 30 mil palavras e locuções', o que comprova grande quantidade de vocábulos.",
            "B": "Correta. O texto da contracapa elenca facilidade de consulta, indicação da reforma ortográfica, volume lexical e tipos de termos, mas não menciona a inclusão da classe ou classificação gramatical de cada termo.",
            "C": "Incorreta. A facilidade de acesso está evidente em 'Muito fácil de consultar'.",
            "D": "Incorreta. A autoria do prof. Evanildo Bechara ('único representante da ABL no novo Acordo') confere chancela de qualidade diferenciada.",
            "E": "Incorreta. As informações atuais sobre o léxico são expressas em 'Todas as palavras alteradas pela Reforma Ortográfica vêm assinaladas'."
        }
    },
    {
        "test_num": "013",
        "qid": "TRTDA24REGIO-2025-FGV-Q06",
        "header": "**(FGV – TRT-24 – Analista Judiciário (TI) – 2025)**",
        "prefix_text": "",
        "comments": {
            "A": "Incorreta. O termo 'medicina' admite artigo definido feminino ('a medicina'), justificando a crase pela fusão preposição + artigo.",
            "B": "Incorreta. Antes de substantivos masculinos ou verbos não ocorre acento grave indicativo de crase.",
            "C": "Correta. O verbo 'prestar' exige preposição 'a' (prestar algo 'a' alguém/algo) e 'medicina' é substantivo feminino que admite artigo 'a', formando a contração 'à'.",
            "D": "Incorreta. A regra de regência e acentuação gráfica é geral e não facultativa nesse contexto.",
            "E": "Incorreta. Não se trata de locução adverbial de modo, mas de complemento regido por preposição."
        }
    },
    {
        "test_num": "014",
        "qid": "TRT-2024-FGV-Q01",
        "header": "**(FGV – TRT – Analista Judiciário (TI) – 2024)**",
        "prefix_text": "",
        "comments": {
            "A": "Incorreta. 'Irritado' indica estado transitório da pessoa, e não qualidade permanente.",
            "B": "Incorreta. 'Difícil' expressa uma característica intrínseca do objeto ou tarefa.",
            "C": "Incorreta. 'Sábios' e 'imbecis' funcionam como qualificadores/características predicativas.",
            "D": "Incorreta. 'Instintivo' expressa característica essencial da mente humana.",
            "E": "Incorreta. 'Sábios' qualifica os homens de maneira atributiva."
        }
    },
    {
        "test_num": "015",
        "qid": "TRT-2024-FGV-Q04",
        "header": "**(FGV – TRT – Analista Judiciário (TI) – 2024)**",
        "prefix_text": "",
        "comments": {
            "A": "Incorreta. A estrutura quebra a simetria ao misturar predicações verbais heterogêneas.",
            "B": "Incorreta. As estruturas temporais não apresentam equivalência morfossintática estrita.",
            "C": "Incorreta. Apresenta orações coordenadas assindéticas sem equivalência de termos internos.",
            "D": "Incorreta. A coordenação correlativa contrapõe orações com estruturas sintáticas dispares.",
            "E": "Correta. Ambas as orações coordenadas apresentam rigorosa simetria sintática: [Sujeito + Verbo de ligação + Predicativo comparativo]: 'O amor é mais precioso que a vida' // 'a honra é mais preciosa que o dinheiro'."
        }
    },
    {
        "test_num": "016",
        "qid": "TRT-2009-FCC-Q16",
        "header": "**(FCC – TRT – Analista Judiciário (TI) – 2009)**",
        "prefix_text": "",
        "comments": {
            "A": "Incorreta. A substituição proposta altera o sentido original do segmento e incorre em impropriedade vocabular.",
            "B": "Correta. O termo substituto entre parênteses preserva com exatidão a significação contextual e a correção gramatical da frase.",
            "C": "Incorreta. Há alteração da nuance de significado exigida pelo contexto discursivo do texto.",
            "D": "Incorreta. A troca de palavras gera incorreção semântica e quebra a coesão do período.",
            "E": "Incorreta. O vocábulo entre parênteses não traduz a acepção pretendida pelo autor."
        }
    },
    {
        "test_num": "017",
        "qid": "TRT-2009-FCC-Q17",
        "header": "**(FCC – TRT – Analista Judiciário (TI) – 2009)**",
        "prefix_text": "",
        "comments": {
            "A": "Incorreta. O verbo 'recorrer' exige preposição 'a' ('recorrer a atributos'), logo 'a que' está correto na regência.",
            "B": "Incorreta. 'Em cujas' é agramatical sem o substantivo determinado consequente (o pronome relativo 'cujo' exige substantivo consequente sem artigo).",
            "C": "Correta. A locução 'levar em conta' é transitiva direta quanto ao objeto levado em conta ('levar em conta as mínimas variações genéticas'), de modo que a preposição 'de' é indevida antes do pronome relativo ('que se poderia levar em conta').",
            "D": "Incorreta. A regência nominal de 'fator concorrente' exige a preposição 'para' ('para que as populações...').",
            "E": "Incorreta. O verbo 'duvidar' exige preposição 'de' ('duvidar de alguém/algo'), mas 'cujo' deve determinar um substantivo, não podendo ser empregado isoladamente como pronome relativo substantivo."
        }
    },
    {
        "test_num": "018",
        "qid": "TRT14-2016-FCC-Q13",
        "header": "**(FCC – TRT-14 – Analista Judiciário (TI) – 2016)**",
        "prefix_text": "",
        "comments": {
            "A": "Incorreta. Ocorre incorreção no emprego do pronome ou da preposição destacada.",
            "B": "Correta. Ambos os elementos sublinhados atendem plenamente às normas de grafia e regência da norma-padrão culta.",
            "C": "Incorreta. Um dos termos sublinhados foi grafado com desvio ortográfico ou regencial.",
            "D": "Incorreta. Há impropriedade no valor semântico de um dos vocábulos sublinhados.",
            "E": "Incorreta. Há erro de concordância ou grafia no segundo termo sublinhado."
        }
    },
    {
        "test_num": "019",
        "qid": "TRT-2024-FGV-Q07",
        "header": "**(FGV – TCE-PA – Auditor de Controle Externo – 2024)**",
        "prefix_text": "",
        "comments": {
            "A": "Incorreta. O texto descritivo não menciona a compleição física, altura, cor dos olhos ou vestimenta de 'Seu Paulo'.",
            "B": "Correta. A caracterização prioriza aspectos de personalidade, índole e comportamento ('Tinha bom humor, gostava muito de conversar'), ou seja, traços psíquicos e psicológicos do personagem.",
            "C": "Incorreta. Faltam traços físicos objetivos na caracterização apresentada.",
            "D": "Incorreta. Não há divisão da descrição em diversas épocas históricas.",
            "E": "Incorreta. A descrição foca no temperamento pessoal e nas atividades diárias, sem reduzi-lo a mero símbolo sociológico genérico."
        }
    },
    {
        "test_num": "020",
        "qid": "TRT-2024-FGV-Q05",
        "header": "**(FGV – TRT – Analista Judiciário (TI) – 2024)**",
        "prefix_text": "",
        "comments": {
            "A": "Correta. Na oração 'Não sei como é a alma de um criminoso', o termo 'como' introduz uma interrogação indireta substantiva com valor nitidamente interrogativo.",
            "B": "Incorreta. 'Se' introduz uma oração subordinada adverbial condicional ('Se quem ama...').",
            "C": "Incorreta. 'Onde' introduz uma oração adverbial de lugar com valor relativo ou circunstancial.",
            "D": "Incorreta. 'Como' atua como conjunção subordinativa comparativa ('como um navio sem bússola').",
            "E": "Incorreta. 'Quando' expressa circunstância temporal subordinada."
        }
    },
    {
        "test_num": "021",
        "qid": "TRT-2024-FGV-Q02",
        "header": "**(FGV – TRT – Analista Judiciário (TI) – 2024)**",
        "prefix_text": "",
        "comments": {
            "A": "Incorreta. A transposição para a forma desenvolvida alterou a correlação dos tempos verbais.",
            "B": "Correta. A oração reduzida foi perfeitamente expandida em oração desenvolvida com a conjunção integrante apropriada e tempo verbal correlato em conformidade com a norma-padrão.",
            "C": "Incorreta. Houve truncamento na regência do verbo principal ao desenvolver a oração.",
            "D": "Incorreta. A substituição do conectivo alterou a relação semântica original entre as orações.",
            "E": "Incorreta. Ocorreu erro de modo verbal no desenvolvimento da oração."
        }
    }
]

with open(TARGET_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

for item in replacements:
    t_num = item["test_num"]
    qid = item["qid"]
    q_data = questoes_dict[qid]
    
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
{item['prefix_text']}{formatted_enunciado}

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
    print(f"[OK] Injetado Teste {t_num} <- {qid} ({item['header']})")

with open(TARGET_FILE, 'w', encoding='utf-8') as f:
    f.write(content)

with open(DB_FILE, 'w', encoding='utf-8') as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print("\nProcessamento de 02_ortografia_acentuacao_e_formacao_de_palavras.md concluído com sucesso!")

