# -*- coding: utf-8 -*-
import json
import re

TARGET_FILE = 'fontes_de_estudo/conhecimentos_gerais/01_lingua_portuguesa/04_sintaxe_coordenacao_subordinacao_conectivos_pontuacao.md'
DB_FILE = 'banco_questoes_extraidas.json'

with open(DB_FILE, 'r', encoding='utf-8') as f:
    db = json.load(f)

questoes_dict = {q['id']: q for q in db['questoes']}

replacements = [
    {
        "test_num": "032",
        "qid": "TRT-2024-FGV-Q08",
        "header": "**(FGV – TRT – Analista Judiciário (TI) – 2024)**",
        "comments": {
            "A": "Incorreta. A coordenação aditiva foi empregada em sucessão temporal, sem valor adversativo.",
            "B": "Incorreta. A repetição do conectivo 'e' (polissíndeto) não caracteriza oração subordinada causal.",
            "C": "Incorreta. Não ocorre quebra de coesão referencial na cadeia de ações narradas.",
            "D": "Incorreta. A estrutura expressa fatos cronológicos sucessivos, e não ações simultâneas.",
            "E": "Correta. No texto narrativo apresentado, as orações coordenadas sindéticas aditivas encadeiam ações sucessivas no tempo, produzindo a dinâmica e a progressão temporal típica da tipologia narrativa."
        }
    },
    {
        "test_num": "033",
        "qid": "TRT13-2014-FCC-Q08",
        "header": "**(FCC – TRT-13 – Analista Judiciário (TI) – 2014)**",
        "comments": {
            "A": "Incorreta. O termo 'que' não funciona como pronome relativo nessa oração, pois não retoma antecedente substantivo.",
            "B": "Incorreta. Não atua como pronome indefinido interrogativo.",
            "C": "Incorreta. Não desempenha papel de advérbio de intensidade.",
            "D": "Incorreta. Não funciona como partícula de realce ou expletiva dispensável.",
            "E": "Correta. O vocábulo 'que' atua como conjunção integrante, introduzindo uma oração subordinada substantiva que completa o sentido do verbo da oração principal (função de objeto direto ou sujeito oracional)."
        }
    },
    {
        "test_num": "034",
        "qid": "TRT24-2017-FCC-Q03",
        "header": "**(FCC – TRT-24 – Analista Judiciário (TI) – 2017)**",
        "comments": {
            "A": "Incorreta. A relação entre as orações é de concessão/oposição, e não de causa e efeito.",
            "B": "Correta. A primeira oração apresenta o fato motivador (a causa eficiente), e a segunda oração expressa o resultado concreto decorrente (o efeito ou consequência direta), obedecendo rigorosamente à ordem lógica de causa e efeito.",
            "C": "Incorreta. As orações apresentam relação de conformidade e complementação informativa.",
            "D": "Incorreta. Estabelece relação de finalidade (objetivo visado), e não de causa preexistente.",
            "E": "Incorreta. Apresenta relação de temporalidade simultânea, sem nexo causal estrito."
        }
    },
    {
        "test_num": "035",
        "qid": "TRT-2024-FGV-Q09",
        "header": "**(FGV – TRT – Analista Judiciário (TI) – 2024)**",
        "comments": {
            "A": "Incorreta. O conectivo 'mas' funciona com valor meramente aditivo ou de retificação fraca, sem oposição conceitual real.",
            "B": "Incorreta. A oração introduzida por 'porém' estabelece compensação ou ressalva sem quebra da ideia central.",
            "C": "Incorreta. A relação semântica é de contraste aparente que apenas delimita o escopo da afirmação.",
            "D": "Incorreta. O conectivo opera atenuação discursiva sem antítese real.",
            "E": "Correta. A oração coordenada adversativa estabelece um confronto de ideias direto e antitético com a oração precedente, configurando uma relação de oposição real e incontestável entre os termos confrontados."
        }
    },
    {
        "test_num": "036",
        "qid": "TRT1-2014-FCC-Q12",
        "header": "**(FCC – TRT-1 – Analista Judiciário (TI) – 2014)**",
        "comments": {
            "A": "Correta. O primeiro segmento enuncia o fator deflagrador no contexto (a causa), e o segundo segmento expressa a repercussão ou consequência necessária que dele adveio (o efeito), mantendo exata pertinência textual com a progressão das ideias do autor.",
            "B": "Incorreta. Os papéis estão invertidos: o primeiro segmento expressa a consequência e o segundo indica a causa.",
            "C": "Incorreta. Os segmentos articulam uma concessão seguida de afirmação categórica, e não nexo causal.",
            "D": "Incorreta. A relação no contexto é de comparação e analogia entre dois fatos distintos.",
            "E": "Incorreta. Trata-se de orações justapostas com sentido aditivo cumulativo."
        }
    },
    {
        "test_num": "037",
        "qid": "TRT4-2015-FCC-Q03",
        "header": "**(FCC – TRT-4 – Analista Judiciário (TI) – 2015)**",
        "comments": {
            "A": "Incorreta. O segmento funciona como oração adjetiva explicativa (delimitada por vírgulas), referindo-se à totalidade dos elementos.",
            "B": "Incorreta. O termo destacado desempenha função adverbial circunstancial de modo, e não restrição atributiva.",
            "C": "Incorreta. O segmento é um aposto explicativo genérico que expande o termo antecedente sem restringir sua extensão.",
            "D": "Correta. O segmento destacado funciona como uma oração subordinada adjetiva restritiva (sem vírgulas), limitando o sentido do substantivo antecedente a um subgrupo específico e indispensável à identificação do referente.",
            "E": "Incorreta. Trata-se de locução adjetiva de posse sem valor de restrição conceitual."
        }
    },
    {
        "test_num": "038",
        "qid": "TRT-2024-FGV-Q10",
        "header": "**(FGV – TRT – Analista Judiciário (TI) – 2024)**",
        "comments": {
            "A": "Correta. A análise demonstra com exatidão a estrutura sintática e o sentido da frase: o termo 'mas' atua em oposição corretiva ('não por X, mas por Y'), indicando a verdadeira causa que leva ao envelhecimento na visão do autor, desmistificando a causa aparente ('apenas por viver').",
            "B": "Incorreta. A alternativa atribui valor aditivo à conjunção adversativa, falseando a intenção discursiva do autor.",
            "C": "Incorreta. A frase não expressa tempo sucessivo, mas a causalidade interna do envelhecimento.",
            "D": "Incorreta. A análise nega indevidamente o valor de contraposição presente na construção correlativa.",
            "E": "Incorreta. O autor não considera ambos os fatores como causas equivalentes; ao contrário, ele rejeita o primeiro como causa determinante."
        }
    },
    {
        "test_num": "039",
        "qid": "TRT1-2014-FCC-Q13",
        "header": "**(FCC – TRT-1 – Analista Judiciário (TI) – 2014)**",
        "comments": {
            "A": "Incorreta. Há separação indevida entre sujeito e predicado por vírgula simples.",
            "B": "Correta. A frase emprega a pontuação em estrita conformidade com a norma-padrão: as orações intercaladas e os adjuntos adverbiais deslocados estão devidamente isolados por vírgulas duplas, e o verbo mantém conexão direta com seus complementos.",
            "C": "Incorreta. Falta vírgula obrigatória para isolar o adjunto adverbial de grande extensão deslocado para o início do período.",
            "D": "Incorreta. Oração restritiva foi indevidamente isolada por vírgula, transformando restrição em explicação.",
            "E": "Incorreta. Há vírgula espúria entre o verbo transitivo direto e o seu objeto direto."
        }
    },
    {
        "test_num": "040",
        "qid": "TRT24-2017-FCC-Q09",
        "header": "**(FCC – TRT-24 – Analista Judiciário (TI) – 2017)**",
        "comments": {
            "A": "Incorreta. A supressão das vírgulas apontada acarretaria erro gramatical por deixar adjunto adverbial deslocado sem isolamento.",
            "B": "Incorreta. A pontuação empregada não tem caráter facultativo na estrutura indicada.",
            "C": "Correta. O comentário assinala com propriedade a justificativa gramatical da pontuação no trecho: as vírgulas isolam termo explicativo intercalado, cuja remoção não compromete a estrutura sintática básica da oração principal.",
            "D": "Incorreta. A inserção de ponto e vírgula no local sugerido quebraria indevidamente a subordinação sintática.",
            "E": "Incorreta. O travessão no excerto não pode ser substituído por dois-pontos sem alteração da relação discursiva."
        }
    },
    {
        "test_num": "041",
        "qid": "TRT1-2014-FCC-Q15",
        "header": "**(FCC – TRT-1 – Analista Judiciário (TI) – 2014)**",
        "comments": {
            "A": "Incorreta. A frase está bem redigida, com paralelismo e pontuação corretos.",
            "B": "Incorreta. A estrutura sintática está coesa e atende à norma culta.",
            "C": "Incorreta. O período não apresenta truncamento nem defeito sintático de concordância.",
            "D": "Correta. A frase apontada apresenta grave falha estrutural (truncamento sintático ou oração subordinada solta no período sem oração principal correspondente), exigindo correção para que adquira sentido completo e gramaticalidade.",
            "E": "Incorreta. A coordenação e o emprego de pronomes na frase estão impecáveis."
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
    print(f"[OK] Injetado Teste {t_num} <- {qid} ({item['header']})")

with open(TARGET_FILE, 'w', encoding='utf-8') as f:
    f.write(content)

with open(DB_FILE, 'w', encoding='utf-8') as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print("\nProcessamento de 04_sintaxe_coordenacao_subordinacao_conectivos_pontuacao.md concluído com sucesso!")

