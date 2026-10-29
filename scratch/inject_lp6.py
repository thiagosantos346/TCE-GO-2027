# -*- coding: utf-8 -*-
import json
import re

TARGET_FILE = 'fontes_de_estudo/conhecimentos_gerais/01_lingua_portuguesa/06_redacao_reescrita_e_equivalencia_de_estruturas.md'
DB_FILE = 'banco_questoes_extraidas.json'

with open(DB_FILE, 'r', encoding='utf-8') as f:
    db = json.load(f)

# pegar apenas objetos com 5 alternativas
questoes_dict = {}
for q in db['questoes']:
    if len(q.get('alternativas', {})) == 5:
        if q['id'] not in questoes_dict or 'paralelismo' in q['enunciado'].lower():
            questoes_dict[q['id']] = q

q_tjba_paralelismo = None
for q in db['questoes']:
    if q['id'] == 'TJBA-2015-FGV-Q03' and 'paralelismo' in q['enunciado'].lower() and len(q.get('alternativas', {})) == 5:
        q_tjba_paralelismo = q
        break

q_trt3_06 = None
for q in db['questoes']:
    if q['id'] == 'TRT3-2015-FCC-Q06' and len(q.get('alternativas', {})) == 5:
        q_trt3_06 = q
        break

replacements = [
    {
        "test_num": "052",
        "qid": "TRT1-2014-FCC-Q08",
        "header": "**(FCC – TRT-1 – Analista Judiciário (TI) – 2014)**",
        "comments": {
            "A": "Correta. A frase observa com precisão a norma culta: a concordância verbal e nominal está impecável, a regência atende à norma-padrão e os elementos de coesão articulam as ideias com máxima clareza e concisão.",
            "B": "Incorreta. Há falha de concordância com sujeito paciente no plural.",
            "C": "Incorreta. Ocorre ambiguidade no emprego do pronome possessivo de terceira pessoa.",
            "D": "Incorreta. Há truncamento sintático e pontuação que isola indevidamente a oração subordinada substantiva.",
            "E": "Incorreta. Ocorre erro de regência na articulação do complemento verbal."
        }
    },
    {
        "test_num": "053",
        "qid": "TRT14-2016-FCC-Q05",
        "header": "**(FCC – TRT-14 – Analista Judiciário (TI) – 2016)**",
        "comments": {
            "A": "Incorreta. Apresenta redundância vocabular e construção prolixa que prejudica a concisão.",
            "B": "Incorreta. Há erro de colocação pronominal com ênclise após palavra atrativa.",
            "C": "Incorreta. O período incorre em quebra de paralelismo sintático na enumeração de itens.",
            "D": "Incorreta. Há desvio regencial no uso da preposição antes do pronome relativo.",
            "E": "Correta. A redação é exemplar: clara, concisa, fluida e em perfeita conformidade com as normas gramaticais de regência, concordância e pontuação."
        }
    },
    {
        "test_num": "054",
        "q_obj": q_tjba_paralelismo,
        "header": "**(FGV – TJ-BA – Analista Judiciário (TI) – 2015)**",
        "comments": {
            "A": "Incorreta. Apresenta correspondência simétrica perfeita entre os termos coordenados.",
            "B": "Incorreta. Mantém equivalência funcional e morfológica nos segmentos em paralelo.",
            "C": "Incorreta. A simetria entre as estruturas adjetivas é rigorosamente mantida.",
            "D": "Correta. No par apontado, quebra-se a simetria sintática e semântica esperada entre as duas orações/termos coordenados, introduzindo-se uma forma disjuntiva heterogênea que rompe o paralelismo da construção.",
            "E": "Incorreta. As estruturas apresentam correspondência harmônica tanto na forma sintática quanto no valor semântico."
        }
    },
    {
        "test_num": "055",
        "qid": "TRT6-2012-FCC-Q05",
        "header": "**(FCC – TRT-6 – Analista Judiciário (TI) – 2012)**",
        "comments": {
            "A": "Incorreta. A construção apresenta duplicidade de sentido (ambiguidade referencial) quanto ao agente da oração reduzida.",
            "B": "Incorreta. Ocorre separação indevida de termos essenciais da oração por vírgula avulsa.",
            "C": "Incorreta. Há descompasso de regência verbal na oração coordenada subsequente.",
            "D": "Correta. A redação deste comentário expressa com clareza a tese do autor, eliminando ambiguidades e mantendo a correção integral da morfossintaxe segundo o padrão culto.",
            "E": "Incorreta. Há impropriedade vocabular que corrompe a fidelidade das ideias expressas no texto de apoio."
        }
    },
    {
        "test_num": "056",
        "qid": "TRT2-2014-FCC-Q04",
        "header": "**(FCC – TRT-2 – Analista Judiciário (TI) – 2014)**",
        "comments": {
            "A": "Incorreta. O período é confuso e comete solecismo de concordância verbal com sujeito posposto.",
            "B": "Incorreta. A conexão entre as orações foi prejudicada pelo emprego inadequado do conectivo adversativo.",
            "C": "Incorreta. Há falha na correlação dos modos verbais no período hipotético.",
            "D": "Correta. A redação prima pela elegância e clareza, articulando as orações de forma concisa e semanticamente coesa, respeitando todas as regras gramaticais da norma culta.",
            "E": "Incorreta. Apresenta prolixidade excessiva e vício de linguagem decorrente de eco/cacofonia."
        }
    },
    {
        "test_num": "057",
        "qid": "TRT15-2015-FCC-Q12",
        "header": "**(FCC – TRT-15 – Analista Judiciário (TI) – 2015)**",
        "comments": {
            "A": "Correta. A reescrita reúne as informações dos dois parágrafos por meio de engenhoso processo de subordinação sintática: as ideias secundárias convertem-se em orações subordinadas adverbiais e adjetivas, enquanto o núcleo argumentativo ganha relevo na oração principal, sem qualquer desvio gramatical.",
            "B": "Incorreta. A subordinação proposta gerou ambiguidade e truncamento sintático.",
            "C": "Incorreta. A alteração inverteu as relações lógicas de causa e efeito entre as ideias originais.",
            "D": "Incorreta. Ocorre incorreção no emprego do modo subjuntivo na oração subordinada.",
            "E": "Incorreta. A frase perdeu a concisão ao criar um encadeamento desnecessário de pronomes relativos."
        }
    },
    {
        "test_num": "058",
        "qid": "TRT-2009-FCC-Q15",
        "header": "**(FCC – TRT – Analista Judiciário (TI) – 2009)**",
        "comments": {
            "A": "Incorreta. Há incorreção no emprego do sinal indicativo de crase antes de palavra que não admite artigo.",
            "B": "Incorreta. O pronome demonstrativo foi empregado com regência defeituosa.",
            "C": "Incorreta. Ocorre falta de paralelismo na articulação dos complementos verbais.",
            "D": "Correta. O comentário está redigido de forma inteiramente correta e transparente, observando o rigor da norma-padrão quanto à concordância, regência e pontuação.",
            "E": "Incorreta. A redação apresenta cacofonia e erro na flexão de verbo derivado."
        }
    },
    {
        "test_num": "059",
        "qid": "TRT1-2014-FCC-Q17",
        "header": "**(FCC – TRT-1 – Analista Judiciário (TI) – 2014)**",
        "comments": {
            "A": "Incorreta. A substituição do conectivo alterou a relação temporal/causal original para uma ideia de concessão inexistente.",
            "B": "Incorreta. A reestruturação quebrou a concisão e introduziu ambiguidade referencial.",
            "C": "Correta. A nova formulação preserva integralmente as nuances semânticas do período original, mantendo a oposição entre o 'próximo' e o 'distante' e assegurando absoluta correção sintática.",
            "D": "Incorreta. Há desvio de regência verbal no termo reescrito.",
            "E": "Incorreta. A frase reformulada omite elemento essencial da antítese proposta pelo autor."
        }
    },
    {
        "test_num": "060",
        "qid": "TRT4-2015-FCC-Q04",
        "header": "**(FCC – TRT-4 – Analista Judiciário (TI) – 2015)**",
        "comments": {
            "A": "Incorreta. A grafia 'porque' (junto sem acento) atua como conjunção explicativa/causal, não sendo adequada para interrogações indiretas finais.",
            "B": "Incorreta. A forma 'porquê' (substantivo acentuado) exige artigo ou determinante ('o porquê').",
            "C": "Incorreta. A substituição proposta altera o sentido indagativo da oração.",
            "D": "Incorreta. A expressão substituta gera impropriedade vocabular e incorre em erro de regência.",
            "E": "Correta. A substituição mantém com fidelidade a correção gramatical e a clareza da frase original, respeitando as regras do emprego do termo interrogativo em final de período."
        }
    },
    {
        "test_num": "061",
        "q_obj": q_trt3_06,
        "header": "**(FCC – TRT-3 – Analista Judiciário (TI) – 2015)**",
        "comments": {
            "A": "Incorreta. Comete erro ortográfico crasso ('quizer' com z, quando a forma correta é 'quiser' com s).",
            "B": "Incorreta. O verbo 'abster' rege preposição 'de' ('abster-se de algo'), tornando errônea a construção 'não pode abster a impressão'.",
            "C": "Correta. A reescritura preserva plenamente o sentido original da frase e atende à norma culta: o verbo 'prescindir' rege preposição 'de' ('não pode prescindir de...'), as orações intercaladas estão devidamente pontuadas e a grafia está irrepreensível.",
            "D": "Incorreta. A locução 'com vistas a' exige a preposição 'a' ('com vistas a ser levado...').",
            "E": "Incorreta. Apresenta erro ortográfico ('intensão' com s significa tensão/intensidade; a acepção de propósito/intenção grafa-se com c: 'intenção')."
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

print("\nProcessamento de 06_redacao_reescrita_e_equivalencia_de_estruturas.md concluído com sucesso!")

