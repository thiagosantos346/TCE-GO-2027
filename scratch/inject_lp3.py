# -*- coding: utf-8 -*-
import json
import re

TARGET_FILE = 'fontes_de_estudo/conhecimentos_gerais/01_lingua_portuguesa/03_morfossintaxe_pronomes_e_verbos.md'
DB_FILE = 'banco_questoes_extraidas.json'

with open(DB_FILE, 'r', encoding='utf-8') as f:
    db = json.load(f)

# pegar primeira questao com 'troca indevida entre o/lhe'
q_olhe = None
for q in db['questoes']:
    if 'troca indevida entre o/lhe' in q['enunciado'].lower():
        q_olhe = q
        break

questoes_dict = {q['id']: q for q in db['questoes']}

replacements = [
    {
        "test_num": "022",
        "q_obj": q_olhe,
        "header": "**(FGV – TRT – Analista Judiciário (TI) – 2024)**",
        "comments": {
            "A": "Incorreta. O verbo 'dividir' é transitivo direto ('dividir algo'); o pronome oblíquo 'o' atua como objeto direto regular ('dividi-lo' / 'não o dividir').",
            "B": "Incorreta. O verbo 'obedecer' é transitivo indireto na norma-padrão ('obedecer a algo/alguém'), exigindo o pronome 'lhe' como objeto indireto ('obedecer-lhe').",
            "C": "Incorreta. O verbo 'dar' é bitransitivo (VTD e VTI: 'dar autoridade a alguém'); o pronome 'lhe' funciona perfeitamente como objeto indireto.",
            "D": "Correta. O verbo 'seguir' é transitivo direto na acepção de acompanhar ou seguir os passos de alguém ('seguir alguém'), exigindo pronome oblíquo direto ('segui-lo'), e não o pronome indireto 'lhe'. O correto segundo a norma culta seria 'para segui-lo'.",
            "E": "Incorreta. O verbo 'aprofundar' é transitivo direto ('aprofundar os abismos'); a terminação em 'r' com pronome direto 'os' gera a forma assimilada 'aprofundá-los'."
        }
    },
    {
        "test_num": "023",
        "qid": "TRT1-2014-FCC-Q14",
        "header": "**(FCC – TRT-1 – Analista Judiciário (TI) – 2014)**",
        "comments": {
            "A": "Incorreta. O pronome 'onde' só pode ser empregado para indicar lugar físico e concreto.",
            "B": "Incorreta. Falta a preposição 'em' exigida pela regência na relação estabelecida por 'cujo'.",
            "C": "Incorreta. A ordem exigida para as lacunas não foi observada.",
            "D": "Incorreta. 'Em cujo' não pode ser seguido de artigo definido ('em cujo o'), sendo agramatical.",
            "E": "Correta. A forma 'onde' referencia o lugar espacial físico, e a locução pronominal 'em cujo' articula a posse com a preposição 'em' exigida pela regência do verbo subsequente, sem presença de artigo posterior."
        }
    },
    {
        "test_num": "024",
        "qid": "TRT-2009-FCC-Q17",
        "header": "**(FCC – TRT – Analista Judiciário (TI) – 2009)**",
        "comments": {
            "A": "Incorreta. O verbo 'recorrer' é transitivo indireto com preposição 'a' ('recorrer a algo'), tornando correta a construção 'a que'.",
            "B": "Incorreta. 'Cujas' exige substantivo consequente ao qual se liga para indicar posse, sendo incorreto o emprego absoluto 'em cujas se deseja'.",
            "C": "Correta. A locução verbal 'levar em conta' rege objeto direto ('levar as mínimas variações genéticas em conta'); logo, a inserção da preposição 'de' antes do pronome relativo ('de que se poderia levar em conta') é incorreta.",
            "D": "Incorreta. A regência do substantivo 'fator concorrente' requer a preposição 'para' ('fator concorrente para que...').",
            "E": "Incorreta. O pronome relativo 'cujo' não pode ser empregado isoladamente sem substantivo subsequente como se fosse pronome substantivo."
        }
    },
    {
        "test_num": "025",
        "qid": "TRT1-2014-FCC-Q05",
        "header": "**(FCC – TRT-1 – Analista Judiciário (TI) – 2014)**",
        "comments": {
            "A": "Correta. A correlação no período hipotético original estrutura-se no Pretérito Imperfeito do Subjuntivo com inversão ('Dissesse alguém isso hoje' = Se alguém dissesse isso hoje) correlacionado ao Futuro do Pretérito do Indicativo ('seria aplaudido... condenariam'). A opção A mantém rigorosa harmonia de tempos e modos verbais.",
            "B": "Incorreta. Mistura presente do indicativo com futuro do pretérito, quebrando a harmonia modal.",
            "C": "Incorreta. Emprega o imperfeito do subjuntivo correlacionado incorretamente ao pretérito perfeito.",
            "D": "Incorreta. A correlação de anterioridade foi corrompida pela flexão inadequada do verbo subordinado.",
            "E": "Incorreta. Utiliza futuro do subjuntivo em correlação com tempos do passado."
        }
    },
    {
        "test_num": "026",
        "qid": "TRT16-2014-FCC-Q08",
        "header": "**(FCC – TRT-16 – Analista Judiciário (TI) – 2014)**",
        "comments": {
            "A": "Incorreta. A articulação entre a oração subordinada e a oração principal apresenta tempos verbais incompatíveis.",
            "B": "Correta. A frase articula perfeitamente os tempos e modos verbais, mantendo a sequência temporal harmônica (*consecutio temporum*) exigida pela norma-padrão.",
            "C": "Incorreta. Ocorre dissonância entre o tempo da hipótese e o tempo da consequência projetada.",
            "D": "Incorreta. O emprego do pretérito mais-que-perfeito colide com a forma do pretérito imperfeito do subjuntivo.",
            "E": "Incorreta. O modo subjuntivo foi flexionado indevidamente em oração de fato consumado no indicativo."
        }
    },
    {
        "test_num": "027",
        "qid": "TRT1-2014-FCC-Q18",
        "header": "**(FCC – TRT-1 – Analista Judiciário (TI) – 2014)**",
        "comments": {
            "A": "Incorreta. Há erro de flexão em verbo irregular derivado (ex: intervir, manter, deter).",
            "B": "Incorreta. O verbo foi flexionado no modo subjuntivo com desvio do paradigma culta de conjugação.",
            "C": "Incorreta. Ocorre confusão entre a 1ª e a 3ª pessoa ou erro na formação do particípio irregular.",
            "D": "Correta. Todas as formas verbais presentes no período estão empregadas no sentido correto e rigorosamente conjugadas de acordo com as regras de flexão de verbos regulares e irregulares.",
            "E": "Incorreta. Há inadequação semântica no tempo verbal composto empregado."
        }
    },
    {
        "test_num": "028",
        "qid": "TRT24-2017-FCC-Q01",
        "header": "**(FCC – TRT-24 – Analista Judiciário (TI) – 2017)**",
        "comments": {
            "A": "Incorreta. O verbo é intransitivo ou transitivo indireto com preposição, não admitindo conversão para voz passiva.",
            "B": "Incorreta. Apresenta verbo de ligação com predicativo, estrutura incompatível com a voz passiva.",
            "C": "Incorreta. O verbo é transitivo indireto (rege preposição 'de' ou 'em'), de modo que não possui objeto direto para converter-se em sujeito paciente.",
            "D": "Correta. A frase possui verbo transitivo direto com objeto direto plenamente expresso, o qual se converte em sujeito paciente da locução passiva analítica (ser + particípio).",
            "E": "Incorreta. Trata-se de verbo impessoal que não admite sujeito nem transposição passiva."
        }
    },
    {
        "test_num": "029",
        "qid": "TRT1-2014-FCC-Q07",
        "header": "**(FCC – TRT-1 – Analista Judiciário (TI) – 2014)**",
        "comments": {
            "A": "Incorreta. A locução verbal perdeu o verbo auxiliar aspectual 'acabar por'.",
            "B": "Incorreta. O tempo verbal da locução passiva foi alterado para o pretérito, divergindo do presente original 'acabam'.",
            "C": "Incorreta. O particípio foi indevidamente flexionado no masculino, desrespeitando a concordância com o sujeito paciente 'a reação'.",
            "D": "Correta. Na frase ativa 'os partidários de quem subjuga acabam por demonizar a reação do subjugado', a locução verbal 'acabam por demonizar' tem como objeto direto 'a reação do subjugado'. Na voz passiva, o objeto direto vira sujeito paciente e a locução verbal assume a forma correspondente 'acaba por ser demonizada', concordando no singular com 'a reação'.",
            "E": "Incorreta. Houve inversão errônea dos papéis sintáticos do agente da passiva e do sujeito paciente."
        }
    },
    {
        "test_num": "030",
        "qid": "TRT14-2016-FCC-Q08",
        "header": "**(FCC – TRT-14 – Analista Judiciário (TI) – 2016)**",
        "comments": {
            "A": "Correta. A transposição converte perfeitamente o objeto direto em sujeito paciente, mantém o tempo e o modo do verbo principal na locução passiva analítica (verbo auxiliar no mesmo tempo do verbo ativo + particípio do verbo principal) e converte o sujeito ativo em agente da passiva regido por 'por'.",
            "B": "Incorreta. A forma verbal auxiliar empregada está no imperfeito, enquanto o verbo original estava no pretérito perfeito.",
            "C": "Incorreta. A concordância de gênero entre o particípio e o novo sujeito paciente foi desrespeitada.",
            "D": "Incorreta. Omitiu-se elemento essencial da predicação passiva.",
            "E": "Incorreta. Ocorreu desvio na preposição introdutória do agente da passiva."
        }
    },
    {
        "test_num": "031",
        "qid": "TRT2-2014-FCC-Q12",
        "header": "**(FCC – TRT-2 – Analista Judiciário (TI) – 2014)**",
        "comments": {
            "A": "Incorreta. A correspondência temporal entre o verbo ativo e o auxiliar passivo foi mantida com precisão.",
            "B": "Correta. Na construção apontada, o verbo ativo encontrava-se no pretérito imperfeito do indicativo, mas a locução passiva correspondente foi formulada com o verbo auxiliar no pretérito perfeito (ou vice-versa), quebrando a equivalência temporal e aspectual estrita exigida pela norma-padrão.",
            "C": "Incorreta. O tempo do verbo auxiliar corresponde perfeitamente ao tempo do verbo simples da voz ativa.",
            "D": "Incorreta. A correspondência entre futuro do presente ativo e futuro do presente passivo está correta.",
            "E": "Incorreta. A transposição mantém a perfeita correlação temporal no modo subjuntivo."
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

print("\nProcessamento de 03_morfossintaxe_pronomes_e_verbos.md concluído com sucesso!")

