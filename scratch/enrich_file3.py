import os, re

FILE_3 = r"fontes_de_estudo/conhecimentos_gerais/01_lingua_portuguesa/03_morfossintaxe_pronomes_e_verbos.md"

q06_text = """
### Questão 06
**(FCC – TRT-23 – Analista Judiciário)**  
Considere o seguinte período:  
*"A comissão de auditoria encaminhou aos diretores da autarquia o relatório conclusivo sobre os contratos de tecnologia."*

Em relação à morfossintaxe dos termos que compõem o período acima, assinale a opção correta:

* **A)** O segmento *"A comissão de auditoria"* exerce a função sintática de objeto direto da oração.
* **B)** O termo *"o relatório conclusivo sobre os contratos de tecnologia"* funciona como objeto direto do verbo transitivo direto e indireto *"encaminhou"*.
* **C)** A expressão *"aos diretores da autarquia"* atua como adjunto adnominal do substantivo *"comissão"*.
* **D)** O verbo *"encaminhou"* classifica-se como transitivo indireto puro, exigindo exclusivamente complemento preposicionado.
* **E)** O vocábulo *"conclusivo"* é um advérbio de modo que modifica o verbo *"encaminhou"*.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. *"A comissão de auditoria"* é o **sujeito simples** da oração (núcleo substantivo: *comissão*), praticante da ação verbal.
> - **B)** Correta. O verbo *encaminhar* é bitransitivo (Transitivo Direto e Indireto - VTDI): quem encaminha, encaminha algo (*o relatório conclusivo sobre os contratos de tecnologia* = Objeto Direto) a alguém (*aos diretores da autarquia* = Objeto Indireto).
> - **C)** Incorreta. *"Aos diretores da autarquia"* é **objeto indireto**, termo integrante regido pela preposição "a" exigida pela predicação de *encaminhou*.
> - **D)** Incorreta. O verbo é transitivo direto e indireto (VTDI), possuindo dois complementos de naturezas distintas.
> - **E)** Incorreta. *"Conclusivo"* é adjetivo que caracteriza o substantivo *"relatório"*, desempenhando função sintática de adjunto adnominal.
>
> **Gabarito: B**
"""

q07_text = """
### Questão 07
**(FCC – TCE-GO – Analista de Controle Externo)**  
Avalie a colocação pronominal nas frases a seguir, de acordo com o padrão culto da língua:  

I. *Não informaram-nos sobre o adiamento da sessão plenária.*  
II. *Em se tratando de controle de legalidade, o tribunal age com rigor.*  
III. *Os documentos que apresentaram-se na audiência foram periciados.*  
IV. *Dir-se-ia que os gestores agiram respaldados em parecer técnico.*  

A colocação dos pronomes oblíquos átonos está inteiramente correta APENAS em:

* **A)** I e III.
* **B)** II e IV.
* **C)** II e III.
* **D)** I e IV.
* **E)** I, II e IV.

> **Comentário Detalhado:**
>
> - **Item I:** Incorreto. O advérbio de negação *"Não"* é palavra atrativa de natureza absoluta, exigindo **próclise obrigatória**: *"Não nos informaram..."*. A ênclise é erro gramatical grave.
> - **Item II:** Correto. Na estrutura fixa constituída pela preposição *"Em"* seguida de gerúndio (*"Em se tratando de..."*), a **próclise é obrigatória** no padrão culto.
> - **Item III:** Incorreto. O pronome relativo *"que"* atrai obrigatoriamente o pronome oblíquo átono para antes do verbo: *"Os documentos que se apresentaram..."*.
> - **Item IV:** Correto. Estando o verbo no futuro do pretérito (*diria*) no início do período (ou sem elemento atrativo anterior), é obrigatório o emprego da **mesóclise**: *"Dir-se-ia..."*.
> - **Conclusão:** Estão corretos unicamente os itens II e IV.
>
> **Gabarito: B**
"""

q08_text = """
### Questão 08
**(FCC – TRT – Analista Judiciário)**  
Considere as formas verbais destacadas nas seguintes frases:  

I. *Se o auditor **intervir** tempestivamente no processo, os prejuízos serão contornados.*  
II. *Quando os conselheiros **propuserem** a nova diretriz, o regimento será atualizado.*  
III. *Caso a administração **mantesse** os controles diários, as fraudes não teriam ocorrido.*  
IV. *Os servidores **requereram** a revisão de seus adicionais por tempo de serviço.*  

A flexão verbal está em perfeita consonância com a norma-padrão em:

* **A)** I e III, apenas.
* **B)** II e IV, apenas.
* **C)** I, II e IV, apenas.
* **D)** II, III e IV, apenas.
* **E)** I, II, III e IV.

> **Comentário Detalhado:**
>
> - **Item I:** Incorreto. O verbo *intervir* é derivado de *vir* e conjuga-se exatamente como ele. O futuro do subjuntivo de *vir* é *vier*; logo, de *intervir* é **intervier** (*"Se o auditor intervier..."*), e não "intervir".
> - **Item II:** Correto. O verbo *propor* deriva de *pôr*. O futuro do subjuntivo de *pôr* é *puserem*; portanto, o derivado flexiona-se como **propuserem** (*"Quando os conselheiros propuserem..."*).
> - **Item III:** Incorreto. O verbo *manter* deriva de *ter*. O pretérito imperfeito do subjuntivo de *ter* é *tivesse*; portanto, a forma correta do derivado é **mantivesse** (*"Caso a administração mantivesse..."*), e jamais "mantesse".
> - **Item IV:** Correto. O verbo *requerer* não segue a conjugação de *querer* no pretérito perfeito do indicativo (que é *quis*). No pretérito perfeito, *requerer* é regular: *eu requeri, ele requereu, nós requeremos, eles requereram*.
> - **Conclusão:** Estão corretos apenas os itens II e IV.
>
> **Gabarito: B**
"""

q09_text = """
### Questão 09
**(FCC – TCE-PI – Auditor de Controle Externo)**  
Transpondo-se para a voz passiva analítica a oração:  
*"Os auditores de controle externo tinham elaborado relatórios minuciosos sobre os contratos"*  
obtém-se a forma verbal:

* **A)** foram elaborados.
* **B)** tinham sido elaborados.
* **C)** seriam elaborados.
* **D)** tinham elaborado-se.
* **E)** tinham estado sendo elaborados.

> **Comentário Detalhado:**
>
> - **Regra Geral de Transposição da FCC:** Na transposição da voz ativa para a passiva analítica, o tempo e modo verbais devem ser rigorosamente preservados. Na voz ativa, temos o tempo composto formado pelo verbo auxiliar *ter* no pretérito imperfeito do indicativo (*tinham*) + particípio (*elaborado*), configurando o Pretérito Mais-Que-Perfeito Composto do Indicativo.
> - **Mecanismo da Passiva:** A voz passiva desse tempo composto exige a inserção do verbo auxiliar *ser* no particípio (*sido*), mantendo-se o verbo auxiliar original e o particípio do verbo principal:  
>   *tinham elaborado* $\rightarrow$ **tinham sido elaborados**.
> - **Análise das alternativas:**  
>   - **A)** Incorreta. Reduziu ao pretérito perfeito simples (*foram elaborados*).  
>   - **B)** Correta. Preserva fielmente a estrutura temporal e aspectual do mais-que-perfeito composto, concordando com o sujeito paciente (*relatórios minuciosos*).  
>   - **C)** Incorreta. Transpôs para o futuro do pretérito (*seriam*).  
>   - **D)** Incorreta. Construção agramatical que mistura tempos sem auxiliar passivo legítimo.  
>   - **E)** Incorreta. Inserção espúria de particípio e gerúndio em perífrase inexistente no original.
>
> **Gabarito: B**
"""

q10_text = """
### Questão 10
**(FCC – TRT-14 – Analista Judiciário)**  
Considere as regras de correlação de tempos e modos verbais (*consecutio temporum*). Assinale a frase redigida em estrita conformidade com a norma culta:

* **A)** Se o plenário acolhesse a recomendação técnica, a prefeitura corrigirá os editais a tempo.
* **B)** Caso os gestores tivessem prestado contas no prazo regimental, o tribunal não lhes teria aplicado as multas previstas em lei.
* **C)** Quando o auditor ver as planilhas financeiras, identificaria de imediato as inconsistências.
* **D)** Embora o tribunal advertisse os responsáveis no ano passado, eles continuariam reincidindo na irregularidade atualmente.
* **E)** É imperativo que os fiscais mantenham a prudência para que não ocorreram prejuízos ao erário.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Falha na correlação: pretérito imperfeito do subjuntivo (*acolhesse*) exige futuro do pretérito do indicativo (*corrigiria*), e não futuro do presente (*corrigirá*).
> - **B)** Correta. Trata-se do clássico padrão condicional irreal no passado: pretérito mais-que-perfeito composto do subjuntivo na oração subordinada (*tivessem prestado*) correlacionado ao futuro do pretérito composto do indicativo na oração principal (*teria aplicado*).
> - **C)** Incorreta. O futuro do subjuntivo de *ver* é *vir* (*"Quando o auditor vir..."*); além disso, a correlação com a oração principal exigiria futuro do presente (*identificará*).
> - **D)** Incorreta. Mistura pretérito imperfeito (*advertisse*), futuro do pretérito (*continuariam*) com advérbio de tempo presente (*atualmente*), rompendo a harmonia cronológica do período.
> - **E)** Incorreta. A locução conjuntiva final *"para que"* rege obrigatoriamente o presente do subjuntivo (*"não ocorram"*), e não o pretérito perfeito do indicativo (*ocorreram*).
>
> **Gabarito: B**
"""

def enrich_file_3():
    with open(FILE_3, "r", encoding="utf-8") as f:
        text = f.read()

    # Inserção da Questão 06: no fim da Seção 1 (antes de "## 2. Teoria dos Pronomes e Relações Discursivas")
    sec2_marker = "## 2. Teoria dos Pronomes e Relações Discursivas"
    insert_q06 = q06_text + "\n---\n\n"
    idx2 = text.find(sec2_marker)
    dash_idx = text.rfind("---", 0, idx2)
    text = text[:dash_idx] + insert_q06 + text[dash_idx:]

    # Inserção da Questão 07: no fim da Seção 4 (antes de "## 5. Sistema Verbal: Paradigmas de Flexão e Formas Críticas")
    sec5_marker = "## 5. Sistema Verbal: Paradigmas de Flexão e Formas Críticas"
    insert_q07 = q07_text + "\n---\n\n"
    idx5 = text.find(sec5_marker)
    dash_idx = text.rfind("---", 0, idx5)
    text = text[:dash_idx] + insert_q07 + text[dash_idx:]

    # Inserção da Questão 08: no fim da Seção 5 (antes de "## 6. Vozes Verbais e Regras de Transposição")
    # Nota: Seção 5 já tem Questão 03. Vamos inserir Questão 08 antes de "## 6. Vozes Verbais"
    sec6_marker = "## 6. Vozes Verbais e Regras de Transposição"
    insert_q08 = q08_text + "\n---\n\n"
    idx6 = text.find(sec6_marker)
    dash_idx = text.rfind("---", 0, idx6)
    text = text[:dash_idx] + insert_q08 + text[dash_idx:]

    # Inserção da Questão 09: na Seção 6.2 (antes de "### 6.3 Voz Passiva Sintética")
    sec63_marker = "### 6.3 Voz Passiva Sintética ou Pronominal"
    insert_q09 = "\n---\n" + q09_text + "\n---\n\n"
    idx63 = text.find(sec63_marker)
    text = text[:idx63] + insert_q09 + text[idx63:]

    # Inserção da Questão 10: no fim da Seção 7 (antes de "## 🌐 Fontes Oficiais e Referências Bibliográficas")
    sec_fontes = "## 🌐 Fontes Oficiais e Referências Bibliográficas"
    insert_q10 = q10_text + "\n---\n\n"
    idxf = text.find(sec_fontes)
    dash_idx = text.rfind("---", 0, idxf)
    text = text[:dash_idx] + insert_q10 + text[dash_idx:]

    with open(FILE_3, "w", encoding="utf-8") as f:
        f.write(text)

    print("Arquivo 03 enriquecido com sucesso.")

enrich_file_3()
