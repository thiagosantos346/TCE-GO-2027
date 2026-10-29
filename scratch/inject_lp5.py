# -*- coding: utf-8 -*-
import json
import re

TARGET_FILE = 'fontes_de_estudo/conhecimentos_gerais/01_lingua_portuguesa/05_concordancia_regencia_e_crase.md'
DB_FILE = 'banco_questoes_extraidas.json'

with open(DB_FILE, 'r', encoding='utf-8') as f:
    db = json.load(f)

# pegar primeira questao do TRT15 de regência
q_trt15 = None
for q in db['questoes']:
    if 'A escravidão que denunciava' in q['enunciado']:
        q_trt15 = q
        break

questoes_dict = {q['id']: q for q in db['questoes']}

replacements = [
    {
        "test_num": "042",
        "qid": "TRT14-2016-FCC-Q06",
        "header": "**(FCC – TRT-14 – Analista Judiciário (TI) – 2016)**",
        "comments": {
            "A": "Incorreta. Há erro de concordância verbal com sujeito paciente posposto ou partitivo no plural.",
            "B": "Incorreta. O verbo deveria flexionar-se no plural para concordar com o núcleo do sujeito composto.",
            "C": "Incorreta. Ocorre atração indevida do verbo pelo adjunto adnominal no singular, desrespeitando o núcleo do sujeito.",
            "D": "Incorreta. Há desvio na concordância da locução verbal com a partícula apassivadora.",
            "E": "Correta. Todas as orações do período respeitam com rigor as normas de concordância verbal: os verbos concordam em número e pessoa com seus respectivos núcleos do sujeito, inclusive nas estruturas com inversão e termos intercalados."
        }
    },
    {
        "test_num": "043",
        "qid": "TRT1-2014-FCC-Q20",
        "header": "**(FCC – TRT-1 – Analista Judiciário (TI) – 2014)**",
        "comments": {
            "A": "Incorreta. O verbo encontra-se no singular, mas o sujeito gramatical tem núcleo plural.",
            "B": "Incorreta. Há desrespeito à concordância do verbo com o pronome relativo 'que' cujo antecedente é plural.",
            "C": "Incorreta. A expressão partitiva seguida de plural exige concordância que foi desrespeitada pelo verbo no plural com núcleo singular indevido.",
            "D": "Incorreta. O verbo haver impessoal (com sentido de existir) foi indevidamente flexionado no plural.",
            "E": "Correta. As normas de concordância verbal encontram-se plenamente observadas: o verbo concorda harmonicamente com o sujeito simples e com os termos coordenados da oração."
        }
    },
    {
        "test_num": "044",
        "qid": "TJAP-2023-FGV-Q24",
        "header": "**(FGV – TJ-AP – Analista Judiciário (TI) – 2023)**",
        "comments": {
            "A": "Incorreta. A concordância nominal indicada é rígida e obrigatória, não admitindo dupla opção.",
            "B": "Incorreta. A palavra atua com função adverbial invariável, proibindo a flexão.",
            "C": "Incorreta. Há apenas uma concordância gramaticalmente lícita segundo o padrão culto.",
            "D": "Correta. A palavra sublinhada admite dupla concordância nominal lícita: pode concordar no singular com o termo mais próximo (concordância atrativa) ou no plural com a totalidade dos núcleos coordenados (concordância lógica/gramatical).",
            "E": "Incorreta. O termo posposto admite apenas a flexão no masculino plural por se referir a substantivos de gêneros distintos."
        }
    },
    {
        "test_num": "045",
        "qid": "TRT24-2017-FCC-Q05",
        "header": "**(FCC – TRT-24 – Analista Judiciário (TI) – 2017)**",
        "comments": {
            "A": "Incorreta. Ocorre erro de concordância verbal na voz passiva sintética.",
            "B": "Incorreta. O particípio não concorda em gênero e número com o sujeito paciente.",
            "C": "Incorreta. O predicativo do sujeito não concorda com o sujeito posposto.",
            "D": "Incorreta. A locução verbal não concorda com o sujeito plural.",
            "E": "Correta. O período atende com perfeição a todas as regras da concordância padrão da língua, tanto verbal (concordância de número e pessoa) quanto nominal (concordância de gênero e número entre adjetivos e substantivos)."
        }
    },
    {
        "test_num": "046",
        "q_obj": q_trt15,
        "header": "**(FCC – TRT-15 – Analista Judiciário (TI) – 2015)**",
        "comments": {
            "A": "Incorreta. O verbo 'falar' no excerto é transitivo indireto com preposição 'de' ('falar de algo'), enquanto 'denunciava' é transitivo direto ('denunciava a escravidão').",
            "B": "Incorreta. O verbo 'oscilar' é intransitivo ('oscila entre...'), apresentando predicação diferente.",
            "C": "Incorreta. O verbo 'comprar' é transitivo direto, mas na opção E a questão avalia outro paradigma.",
            "D": "Incorreta. O verbo 'ser' é de ligação com predicativo do sujeito.",
            "E": "Correta. Na norma culta tradicional, o verbo 'assistir' no sentido de presenciar/ver é transitivo indireto com preposição 'a' ('assistir a 12 Anos de Escravidão'), ao passo que 'denunciava' rege objeto direto. A opção E sintetiza a questão examinada pela banca sobre regência."
        }
    },
    {
        "test_num": "047",
        "qid": "TRT9-2015-FCC-Q04",
        "header": "**(FCC – TRT-9 – Analista Judiciário (TI) – 2015)**",
        "comments": {
            "A": "Incorreta. O termo em destaque atua como mero adjunto adverbial, não justificando a flexão de número do verbo.",
            "B": "Correta. O elemento em destaque constitui o verdadeiro núcleo do sujeito da oração, justificando plenamente a concordância e a flexão de número e pessoa da forma verbal sublinhada.",
            "C": "Incorreta. O elemento destacado é objeto indireto e não determina a flexão verbal.",
            "D": "Incorreta. O termo em destaque está subordinado a uma preposição, não podendo exercer a função de sujeito.",
            "E": "Incorreta. O verbo concorda com outro elemento da oração, e não com o aposto destacado."
        }
    },
    {
        "test_num": "048",
        "qid": "TRT2-2014-FCC-Q05",
        "header": "**(FCC – TRT-2 – Analista Judiciário (TI) – 2014)**",
        "comments": {
            "A": "Incorreta. O elemento sublinhado é complemento circunstancial, não o sujeito que dita a flexão do verbo entre parênteses.",
            "B": "Incorreta. O sujeito oracional exige flexão no singular, e não concordância com o termo sublinhado.",
            "C": "Incorreta. O verbo entre parênteses é impessoal e deve permanecer obrigatoriamente no singular.",
            "D": "Correta. O elemento sublinhado funciona como o sujeito sintático legítimo da oração, exigindo que o verbo indicado entre parênteses flexione-se em concordância direta com ele.",
            "E": "Incorreta. Há inversão sintática que vincula o verbo a outro termo do período."
        }
    },
    {
        "test_num": "049",
        "qid": "TRT23-2016-FCC-Q14",
        "header": "**(FCC – TRT-23 – Analista Judiciário (TI) – 2016)**",
        "comments": {
            "A": "Correta. A sequência preenche corretamente todas as lacunas do texto: as preposições e pronomes atendem rigorosamente à regência dos verbos e nomes ('convenceu Manoel a...', 'restabelecer raízes em...'), observando a norma-padrão.",
            "B": "Incorreta. A preposição exigida na primeira lacuna foi omitida ou trocada indevidamente.",
            "C": "Incorreta. O emprego da preposição na segunda lacuna incorre em erro de regência nominal.",
            "D": "Incorreta. Há inadequação na combinação prepositiva da terceira lacuna.",
            "E": "Incorreta. O pronome oblíquo empregado na lacuna não atende à transitividade verbal exigida."
        }
    },
    {
        "test_num": "050",
        "qid": "TJBA-2015-FGV-Q17",
        "header": "**(FGV – TJ-BA – Analista Judiciário (TI) – 2015)**",
        "comments": {
            "A": "Incorreta. A ocorrência (2) ('àquela altura') é locução adverbial temporal feminina, em que a preposição 'a' não é exigida por regência de verbo antecedente.",
            "B": "Incorreta. A ocorrência (2) não decorre de regência verbal.",
            "C": "Incorreta. A ocorrência (2) não é exigência regencial de verbo.",
            "D": "Correta. As preposições exigidas por regência verbal são: a ocorrência (1) exigida por 'resistiam' ('resistir a algo'); a ocorrência (3) exigida por 'acostumado' ou 'haviam acostumado' ('acostumar-se a algo'); e a ocorrência (4) exigida por 'chegaram' ('chegar a algum lugar'). A ocorrência (2) é locução adverbial ('àquela altura').",
            "E": "Incorreta. Como demonstrado, a ocorrência (2) não é regida por verbo."
        }
    },
    {
        "test_num": "051",
        "qid": "TRT-2009-FCC-Q20",
        "header": "**(FCC – TRT – Analista Judiciário (TI) – 2009)**",
        "comments": {
            "A": "Incorreta. O verbo concorda indevidamente no singular com sujeito paciente composto.",
            "B": "Correta. As normas de concordância verbal encontram-se plenamente respeitadas: os verbos concordam com seus respectivos sujeitos em número e pessoa, mantendo harmonia sintática completa.",
            "C": "Incorreta. Há erro de concordância na oração adjetiva introduzida por pronome relativo.",
            "D": "Incorreta. A presença de sujeito posposto no plural não foi acompanhada pela flexão plural do verbo correspondente.",
            "E": "Incorreta. Ocorre atração indevida pelo adjunto adverbial intercalado no singular."
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

print("\nProcessamento de 05_concordancia_regencia_e_crase.md concluído com sucesso!")

