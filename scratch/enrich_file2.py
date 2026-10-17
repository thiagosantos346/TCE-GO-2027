import os, re

FILE_2 = r"fontes_de_estudo/conhecimentos_gerais/01_lingua_portuguesa/02_ortografia_acentuacao_e_formacao_de_palavras.md"

q06_text = """
### Questão 06
**(FCC – TRT – Analista Judiciário)**  
Considere as seguintes palavras retiradas de um relatório de fiscalização contábil:  
*relatório* – *órgão* – *auditoria* – *público* – *responsável*

Quanto às regras de acentuação gráfica previstas no sistema ortográfico vigente e cobradas pela banca FCC, assinale a afirmação correta:

* **A)** O vocábulo *relatório* recebe acento gráfico pela mesma regra que justifica o acento no vocábulo *público*, haja vista serem ambos proparoxítonos clássicos.
* **B)** A palavra *auditoria* deveria receber acento gráfico na penúltima sílaba, por ser paroxítona terminada em ditongo crescente, constituindo sua grafia sem acento uma exceção arbitrária.
* **C)** Os vocábulos *relatório* e *órgão* são acentuados por pertencerem à regra geral das paroxítonas (terminada em ditongo crescente e terminada em -ão, respectivamente), ao passo que a FCC também admite classificar *relatório* como proparoxítona aparente ou eventual.
* **D)** A palavra *responsável* é acentuada por ser oxítona terminada na consoante -l.
* **E)** Todos os vocábulos citados são acentuados em razão da regra dos hiatos tônicos.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. *Público* é proparoxítona real/estrita (antepenúltima sílaba tônica: *pú-bli-co*). *Relatório* é paroxítona terminada em ditongo oral (*re-la-tó-rio*), admitida pela tradição gramatical e pela FCC como proparoxítona eventual/relativa, mas não uma proparoxítona estrita originária.
> - **B)** Incorreta. Em *auditoria*, a sílaba tônica é *ri* (*au-di-to-ri-a*), tratando-se de hiato átono final, sem acento gráfico; não há ditongo crescente tônico nem qualquer irregularidade na grafia.
> - **C)** Correta. A regra geral das paroxítonas acentua as palavras com tonicidade na penúltima sílaba terminadas em ditongo oral crescente/decrescente (*re-la-tó-rio*) e terminadas em *-ão* (*ór-gão*). A FCC reconhece a dupla classificação fonética de *relatório* (paroxítona terminada em ditongo ou proparoxítona eventual), o que é tema recorrente da banca.
> - **D)** Incorreta. *Responsável* é paroxítona (*res-pon-sá-vel*), e não oxítona; acentua-se por terminar na consoante *-l*.
> - **E)** Incorreta. Nenhum dos vocábulos acentuados recai na regra dos hiatos tônicos (*I* ou *U* tônicos isolados na sílaba).
>
> **Gabarito: C**
"""

q07_text = """
### Questão 07
**(FCC – TCE-GO – Analista de Controle Externo)**  
Avalie os seguintes grupos de vocábulos quanto à aplicação das regras especiais de acentuação gráfica do Acordo Ortográfico vigente:  

I. *juízes*, *saúde*, *baú*, *balaústre*  
II. *ideia*, *heroico*, *jiboia*, *coreia*  
III. *eles têm*, *eles vêm*, *ele mantém*, *eles mantêm*  

Está em total conformidade com as regras gramaticais o que se afirma em:

* **A)** No grupo I, as palavras perdem o acento gráfico quando seguidas de consoante na mesma sílaba.
* **B)** No grupo II, os vocábulos perderam o acento gráfico porque o Novo Acordo extinguiu a acentuação dos ditongos abertos (*éi*, *ói*) nas palavras paroxítonas, mantendo-o apenas nas oxítonas e monossílabos tônicos (*herói*, *pastéis*, *dói*).
* **C)** No grupo III, as formas verbais *têm* e *vêm* recebem acento circunflexo na 3ª pessoa do singular e perdem o acento no plural.
* **D)** O acento diferencial foi completamente abolido pelo Acordo Ortográfico em todas as palavras da língua portuguesa, sem nenhuma exceção.
* **E)** Em *saúde* e *baú*, o acento gráfico justifica-se por serem paroxítonas terminadas em vogal temática.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. No grupo I, os hiatos tônicos em *i* e *u* são acentuados quando sozinhos na sílaba ou seguidos de *-s* (*ju-í-zes*, *sa-ú-de*, *ba-ú*, *ba-la-ús-tre*). Se fossem seguidos de outras consoantes (como *-z* em *juiz*), não levariam acento.
> - **B)** Correta. O Acordo Ortográfico aboliu expressamente o acento nos ditongos abertos *éi* e *ói* das palavras **paroxítonas** (*i-dei-a*, *he-roi-co*, *ji-boi-a*). Todavia, preservou rigorosamente o acento nas oxítonas (*he-rói*, *pa-péis*, *tro-féu*) e nos monossílabos tônicos (*dói*, *céu*, *réis*).
> - **C)** Incorreta. É o oposto: na 3ª pessoa do singular não há acento (*ele tem*, *ele vem*); na 3ª pessoa do plural o acento circunflexo diferencial é obrigatório (*eles têm*, *eles vêm*). Já nos derivados (*manter*), o singular leva agudo (*ele mantém*) e o plural circunflexo (*eles mantêm*).
> - **D)** Incorreta. O acento diferencial obrigatório foi expressamente mantido em *pôde* (pretérito) / *pode* (presente) e no verbo *pôr* / preposição *por*, além de facultativo em *fôrma* / *forma*.
> - **E)** Incorreta. Trata-se da regra especial dos hiatos tônicos (*I* e *U*), e não da regra geral das paroxítonas.
>
> **Gabarito: B**
"""

q08_text = """
### Questão 08
**(FCC – DPE-RS – Analista Jurídico)**  
Assinale a opção em que todas as palavras estão grafadas em perfeita conformidade com as normas de emprego do hífen estabelecidas pelo Acordo Ortográfico:

* **A)** auto-escola, anti-social, micro-ondas, semi-aberto.
* **B)** autoescola, antissocial, micro-ondas, semiaberto.
* **C)** autoescola, anti-social, microondas, semi-aberto.
* **D)** auto-escola, antissocial, microondas, semiaberto.
* **E)** autoescola, anti-social, micro-ondas, semiaberto.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Diante de vogal diferente, não se usa hífen (*autoescola*, *semiaberto*); diante de *s*, duplica-se a consoante (*antissocial*).
> - **B)** Correta. Aplicação perfeita das três regras básicas: 1) Vogais diferentes se juntam sem hífen (*autoescola*, *semiaberto*); 2) Prefixo terminado em vogal seguido de *r* ou *s* exige duplicação da consoante (*antissocial*, *minissaia*, *autorretrato*); 3) Letras iguais se repelem com hífen (*micro-ondas*, *anti-inflamatório*).
> - **C)** Incorreta. Falhou em *anti-social* (o correto é *antissocial*), em *microondas* (o correto é *micro-ondas*) e em *semi-aberto* (*semiaberto*).
> - **D)** Incorreta. Falhou em *auto-escola* (o correto é *autoescola*) e em *microondas* (o correto é *micro-ondas*).
> - **E)** Incorreta. Falhou em *anti-social* (deve-se dobrar o 's': *antissocial*).
>
> **Gabarito: B**
"""

q09_text = """
### Questão 09
**(FCC – METRÔ-SP – Advogado)**  
Considere as lacunas no seguinte texto administrativo:  
*"O Tribunal Pleno realizou extraordinária __________ para deliberar sobre a __________ de uso de bem público imóvel aos servidores. O parecer técnico apontou risco __________ de desmoronamento estrutural na ala sul do edifício."*

As palavras que preenchem correta e respectivamente as lacunas da frase são:

* **A)** sessão – cessão – iminente
* **B)** seção – cessão – eminente
* **C)** cessão – sessão – iminente
* **D)** sessão – seção – eminente
* **E)** seção – sessão – iminente

> **Comentário Detalhado:**
>
> - **1ª lacuna:** Refere-se à reunião de um colegiado ou intervalo de tempo de trabalho. O termo correto é **sessão** (com dois esses, derivado do latim *sessio*, ato de sentar-se).
> - **2ª lacuna:** Refere-se ao ato de ceder, transferir posse, uso ou direito. O termo correto é **cessão** (com c inicial e dois esses, derivado do verbo *ceder*). Seção (com ç) significa divisão, subdivisão departamental ou repartição.
> - **3ª lacuna:** Refere-se a algo prestes a acontecer ou que ameaça ocorrer a qualquer instante. O termo correto é **iminente** (com i). *Eminente* (com e) significa ilustre, notável, elevado ou superior.
> - **Análise das alternativas:** A alternativa **A** é a única que traz a sequência correta: *sessão – cessão – iminente*.
>
> **Gabarito: A**
"""

q10_text = """
### Questão 10
**(FCC – TRT – Técnico Judiciário)**  
Considere os vocábulos destacados nas frases abaixo:  

I. *"O **desembarque** da equipe de auditoria ocorreu nas primeiras horas da manhã."*  
II. *"Ouviram-se vários **comentários infundados** durante o almoço."*  
III. *"O **olhar** atento do relator detectou inconsistências no edital."*  

Quanto aos processos de formação das palavras destacadas, é correto afirmar que:

* **A)** O vocábulo *desembarque* formou-se por derivação parassintética, visto que o prefixo e o sufixo foram anexados simultaneamente ao radical.
* **B)** A palavra *desembarque* é fruto de derivação regressiva (deverbal), pois provém do verbo *desembarcar*, com perda do sufixo verbal e formação de substantivo abstrato que indica ação.
* **C)** No vocábulo *infundados*, constata-se processo de composição por aglutinação, com alteração fonética de seus elementos formadores.
* **D)** A palavra *olhar*, em III, constitui caso de derivação prefixal com acréscimo de desinência de modo-tempo.
* **E)** O vocábulo *olhar*, em III, exemplifica a derivação parassintética de base nominal.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Derivação parassintética exige acréscimo simultâneo e inseparável de prefixo e sufixo a um radical (ex.: *envernizar*, *esfriar*). *Desembarque* deriva de um verbo pré-existente por regressão.
> - **B)** Correta. Na derivação regressiva (ou deverbal), forma-se um substantivo abstrato indicador de ação a partir de um verbo, mediante a redução da terminação verbal e inserção de uma vogal temática nominal (*a*, *e*, *o*): *desembarcar* $\rightarrow$ *desembarque*; *atrasar* $\rightarrow$ *atraso*; *resgatar* $\rightarrow$ *resgate*. É um dos tópicos mais cobrados pela FCC.
> - **C)** Incorreta. *Infundados* forma-se por derivação prefixal e sufixal (prefixo de negação *in-* + radical *fund-* + sufixo *-ado*), e não por composição.
> - **D) e E)** Incorretas. Em III, a palavra *olhar* (originalmente verbo) é antecedida pelo artigo definido "O", mudando de classe gramatical para substantivo sem qualquer alteração mórfica na sua forma externa. Esse processo chama-se **derivação imprópria (ou conversão)**.
>
> **Gabarito: B**
"""

def enrich_file_2():
    with open(FILE_2, "r", encoding="utf-8") as f:
        text = f.read()

    # Inserção da Questão 06: no fim da Seção 1 (antes de "## 2. Regras Especiais de Acentuação")
    sec2_marker = "## 2. Regras Especiais de Acentuação"
    insert_q06 = q06_text + "\n---\n\n"
    idx2 = text.find(sec2_marker)
    dash_idx = text.rfind("---", 0, idx2)
    text = text[:dash_idx] + insert_q06 + text[dash_idx:]

    # Inserção da Questão 07: no fim da Seção 2 (antes de "## 3. Emprego do Hífen")
    sec3_marker = "## 3. Emprego do Hífen com Prefixos e Elementos de Composição"
    insert_q07 = q07_text + "\n---\n\n"
    idx3 = text.find(sec3_marker)
    dash_idx = text.rfind("---", 0, idx3)
    text = text[:dash_idx] + insert_q07 + text[dash_idx:]

    # Inserção da Questão 08: na Seção 3.4 (antes de "## 4. Semântica Lexical")
    sec4_marker = "## 4. Semântica Lexical: Relações de Sentido e Vocabulário"
    insert_q08 = q08_text + "\n---\n\n"
    idx4 = text.find(sec4_marker)
    dash_idx = text.rfind("---", 0, idx4)
    text = text[:dash_idx] + insert_q08 + text[dash_idx:]

    # Inserção da Questão 09: na Seção 4.4 (antes de "## 5. Morfologia: Elementos Estruturais da Palavra")
    # Atenção: Seção 4 já contém Questão 02. Vamos inserir a Questão 09 antes de "## 5. Morfologia"
    sec5_marker = "## 5. Morfologia: Elementos Estruturais da Palavra"
    insert_q09 = q09_text + "\n---\n\n"
    idx5 = text.find(sec5_marker)
    dash_idx = text.rfind("---", 0, idx5)
    text = text[:dash_idx] + insert_q09 + text[dash_idx:]

    # Inserção da Questão 10: no fim da Seção 6 (antes de "## 🌐 Fontes Oficiais e Referências Bibliográficas")
    sec_fontes = "## 🌐 Fontes Oficiais e Referências Bibliográficas"
    insert_q10 = q10_text + "\n---\n\n"
    idxf = text.find(sec_fontes)
    dash_idx = text.rfind("---", 0, idxf)
    text = text[:dash_idx] + insert_q10 + text[dash_idx:]

    with open(FILE_2, "w", encoding="utf-8") as f:
        f.write(text)

    print("Arquivo 02 enriquecido com sucesso.")

enrich_file_2()
