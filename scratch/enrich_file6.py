import os, re

FILE_6 = r"fontes_de_estudo/conhecimentos_gerais/01_lingua_portuguesa/06_redacao_reescrita_e_equivalencia_de_estruturas.md"

q06_text = """
### Questão 06
**(FCC – TRT-23 – Analista Judiciário)**  
As normas de concordância, regência e colocação pronominal estão plenamente respeitadas na frase:

* **A)** Devem haver outros motivos para que os conselheiros hajam recusado a prestação de contas que lhes enviou o prefeito.
* **B)** Deve haver outros motivos para que os conselheiros tenham recusado a prestação de contas que o prefeito lhes enviou.
* **C)** Devem existir outros motivos para que os conselheiros tenham recusado a prestação de contas que enviou-se pelo prefeito.
* **D)** Deve existir outros motivos para que os conselheiros hajam recusado a prestação de contas que o prefeito lhes enviou.
* **E)** Deve haver outros motivos para que os conselheiros tinham recusado a prestação de contas que lhes enviou o prefeito.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O verbo *haver* no sentido de existir é impessoal e transmite sua impessoalidade ao verbo auxiliar: *"Deve haver"* (e não "Devem haver").
> - **B)** Correta. 1) Locução com *haver* impessoal no singular (*"Deve haver outros motivos"*); 2) Subjuntivo perfeito correto (*"tenham recusado"*); 3) Próclise legítima motivada pelo pronome relativo *que* (*"que o prefeito lhes enviou"*). Frase irrepreensível no checklist FCC.
> - **C)** Incorreta. O verbo *existir* é pessoal; com sujeito no plural (*outros motivos*), o auxiliar deve ir para o plural (*"Devem existir"* - correto nesta parte), mas na oração adjetiva a ênclise com o pronome relativo *que* (*"que enviou-se"*) é erro grosseiro de colocação pronominal.
> - **D)** Incorreta. Com o verbo pessoal *existir*, a concordância no singular (*"Deve existir outros motivos"*) viola a regra de concordância verbal (o correto seria "Devem existir").
> - **E)** Incorreta. O tempo verbal *tinham recusado* (indicativo) quebra a correlação exigida pela locução conjuntiva final *"para que"*, a qual exige o modo subjuntivo (*tenham recusado*).
>
> **Gabarito: B**
"""

q07_text = """
### Questão 07
**(FCC – TCE-GO – Analista de Controle Externo)**  
Considere as seguintes frases elaboradas em redação administrativa:  

I. *O auditor entregou os documentos ao diretor da autarquia em seu gabinete.*  
II. *O processo licitatório foi arquivado pelo relator, o mesmo que havia instaurado a tomada de contas especial.*  
III. *Ao analisar as planilhas contábeis com cautela, os erros de cálculo foram descobertos pela equipe técnica.*  

Quanto à clareza, ambiguidade e conformidade com a norma-padrão:

* **A)** Em I, o pronome possessivo *seu* gera ambiguidade estrutural, pois não é possível determinar com certeza se o gabinete pertencia ao auditor ou ao diretor.
* **B)** Em II, o emprego da expressão *o mesmo* é recomendável pelas normas do padrão culto para evitar a repetição do substantivo anterior.
* **C)** Em III, a oração reduzida de gerúndio está perfeitamente vinculada ao sujeito gramatical da oração principal.
* **D)** Todas as frases estão redigidas com clareza exemplar e isentas de vícios sintáticos.
* **E)** Apenas a frase I apresenta problema de coesão referencial.

> **Comentário Detalhado:**
>
> - **A)** Correta. O emprego do pronome possessivo de terceira pessoa (*seu*) em contextos com dois referentes masculinos de 3ª pessoa cria **ambiguidade referencial viciosa**. Para dirimi-la no padrão culto, a FCC prescreve reformulações como *"no gabinete deste"*, *"no gabinete daquele"* ou *"no próprio gabinete"*.
> - **B)** Incorreta. O Manual de Redação e a banca FCC condenam terminantemente o uso de *"o mesmo"* / *"a mesma"* com função de pronome pessoal anafórico para substituir pessoas ou coisas. O correto seria *"relator, quem havia instaurado"* ou *"relator, o qual havia instaurado"*.
> - **C)** Incorreta. Há defeito clássico de oração reduzida solta (sujeito descompassado): quem analisou com cautela foram os técnicos, mas o sujeito gramatical da oração principal é *"os erros de cálculo"* (que não analisam nada!). Deveria ser: *"Ao analisar as planilhas contábeis com cautela, a equipe técnica descobriu os erros de cálculo"*.
> - **D) e E)** Incorretas. As três frases contêm vícios de redação e sintaxe reconhecidos na tipologia caça-erros da FCC.
>
> **Gabarito: A**
"""

q08_text = """
### Questão 08
**(FCC – DPE-RS – Analista Jurídico)**  
Assinale a alternativa que propõe uma redação clara, coesa, concisa e inteiramente correta para as seguintes informações:  
*"O Tribunal de Contas julgou as contas do gestor. O julgamento ocorreu em sessão extraordinária. O Tribunal considerou as contas irregulares. O Tribunal aplicou ao gestor uma multa pecuniária proporcional ao dano."*

* **A)** O Tribunal de Contas, ao julgar as contas do gestor em sessão extraordinária, considerou-as irregulares e aplicou-lhe multa pecuniária proporcional ao dano.
* **B)** Em sessão extraordinária que foi julgada as contas do gestor pelo Tribunal de Contas, consideraram-se as mesmas irregulares, aplicando ao mesmo uma multa pelo dano proporcional.
* **C)** Julgou-se as contas do gestor pelo Tribunal de Contas em sessão extraordinária, onde considerou-as irregulares e lhe multou proporcionalmente ao dano.
* **D)** O Tribunal de Contas julgou irregular as contas do gestor cuja sessão extraordinária aplicou uma multa pecuniária e proporcional contra ele.
* **E)** Tendo sido julgadas as contas em sessão extraordinária, o Tribunal de Contas julgou elas irregulares, aplicando no gestor multa pecuniária.

> **Comentário Detalhado:**
>
> - **A)** Correta. Encadeia todas as informações originais com notável elegância sintática e concisão: oração reduzida de tempo (*"ao julgar..."*), adequada substituição pronominal enclítica com pronome direto (*"considerou-as irregulares"*), objeto indireto pronominal correto (*"aplicou-lhe"*) e coordenação harmoniosa, sem redundâncias ou repetições viciosas.
> - **B)** Incorreta. Erro crasso de concordância (*"foi julgada as contas"* em vez de "foram julgadas"), emprego reprovado de *"as mesmas"* e *"ao mesmo"*, e quebra de clareza.
> - **C)** Incorreta. Erro de concordância com partícula apassivadora (*"Julgou-se as contas"* em vez de "Julgaram-se as contas"), mau uso de *"onde"* para termo temporal (*sessão*) e erro de regência com o verbo multar (*"lhe multou"* em vez de "o multou").
> - **D)** Incorreta. Erro de concordância (*"julgou irregular as contas"* em vez de "irregulares"), e mau emprego do pronome relativo *cujo* (*"cuja sessão"* não indica posse legítima).
> - **E)** Incorreta. Uso vicioso de pronome reto como objeto direto (*"julgou elas"*) e erro de regência (*"aplicando no gestor"* em vez de "aplicando ao gestor").
>
> **Gabarito: A**
"""

q09_text = """
### Questão 09
**(FCC – TCE-PI – Auditor de Controle Externo)**  
Considere o seguinte período:  
*"Embora o relatório da comissão tenha apontado inconsistências formais nos procedimentos licitatórios, o pleno do tribunal optou por aprovar as contas com ressalvas."*

Mantendo-se estritamente o sentido original e a correção gramatical, o período pode ser parafraseado por:

* **A)** Como o relatório da comissão apontou inconsistências formais nos procedimentos licitatórios, o pleno do tribunal optou por aprovar as contas com ressalvas.
* **B)** Conquanto o relatório da comissão tenha apontado inconsistências formais nos procedimentos licitatórios, o pleno do tribunal optou por aprovar as contas com ressalvas.
* **C)** Porquanto o relatório da comissão tenha apontado inconsistências formais nos procedimentos licitatórios, o pleno do tribunal optou por aprovar as contas com ressalvas.
* **D)** À medida que o relatório da comissão apontava inconsistências formais nos procedimentos licitatórios, o pleno do tribunal optou por aprovar as contas com ressalvas.
* **E)** Desde que o relatório da comissão apontasse inconsistências formais nos procedimentos licitatórios, o pleno do tribunal optaria por aprovar as contas com ressalvas.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. *"Como"* é conjunção causal (motivo), alterando a relação semântica concessiva original (oposição/ressalva que não impede a ação principal).
> - **B)** Correta. *"Conquanto"* é conjunção subordinativa concessiva por excelência, perfeitamente sinônima de *"embora"*, mantendo o verbo no modo subjuntivo (*tenha apontado*) e preservando de forma idêntica a relação lógica de concessão e o sentido do texto original. Trata-se do clássico teste da FCC sobre o trio *conquanto* / *porquanto* / *portanto*.
> - **C)** Incorreta. *"Porquanto"* é conjunção explicativa ou causal (equivale a *porque*, *visto que*), distorcendo a lógica concessiva.
> - **D)** Incorreta. *"À medida que"* indica proporção e concomitância temporal progressiva, inexistente na oração concessiva original.
> - **E)** Incorreta. *"Desde que"* introduz valor condicional e alterou os tempos verbais, desfigurando o fato concretizado.
>
> **Gabarito: B**
"""

q10_text = """
### Questão 10
**(FCC – METRÔ-SP – Advogado)**  
Considere as frases a seguir quanto à precisão vocabular e semântica de suas locuções:  

I. *A decisão liminar do conselheiro veio **ao encontro dos** anseios da sociedade por transparência, prestigiando a fiscalização.*  
II. *A nova portaria administrativa veio **de encontro às** diretrizes do Plano Plurianual, gerando atritos com o planejamento.*  
III. *Os auditores reuniram-se **a fim de** debater a uniformização da jurisprudência sobre despesas previdenciárias.*  
IV. *O debate dos especialistas versou **acerca de** novas ferramentas de inteligência artificial aplicadas à auditoria pública.*  

Estão redigidas com absoluta propriedade lexical e sintática as frases:

* **A)** I, II, III e IV.
* **B)** I e III, apenas.
* **C)** II e IV, apenas.
* **D)** I, II e III, apenas.
* **E)** III e IV, apenas.

> **Comentário Detalhado:**
>
> - **Item I:** Correto. A locução *"ao encontro de"* exprime conformidade, concordância, harmonia ou convergência de vontades (*veio ao encontro dos anseios* = atendeu aos anseios).
> - **Item II:** Correto. A locução *"de encontro a"* exprime choque, oposição, colisão ou contrariedade (*veio de encontro às diretrizes* = colidiu com elas, contrariou-as, gerando atritos).
> - **Item III:** Correto. A locução *"a fim de"* (grafada separadamente) indica finalidade ou objetivo (*para debater*). O vocábulo *afim* (junto) é adjetivo que significa semelhante, análogo ou parente por afinidade.
> - **Item IV:** Correto. A locução prepositiva *"acerca de"* (junto) significa "a respeito de" ou "sobre". Não se confunde com *a cerca de* (distância aproximada) nem com *há cerca de* (tempo decorrido com verbo haver).
> - **Conclusão:** Todas as quatro frases (I, II, III e IV) estão inteiramente corretas.
>
> **Gabarito: A**
"""

def enrich_file_6():
    with open(FILE_6, "r", encoding="utf-8") as f:
        text = f.read()

    # Inserção da Questão 06: no fim da Seção 1 (antes de "## 2. Paralelismo Sintático e Semântico")
    sec2_marker = "## 2. Paralelismo Sintático e Semântico"
    insert_q06 = q06_text + "\n---\n\n"
    idx2 = text.find(sec2_marker)
    dash_idx = text.rfind("---", 0, idx2)
    text = text[:dash_idx] + insert_q06 + text[dash_idx:]

    # Inserção da Questão 07: no fim da Seção 3 (antes de "## 4. Organização e Reorganização de Orações e Períodos")
    sec4_marker = "## 4. Organização e Reorganização de Orações e Períodos"
    insert_q07 = q07_text + "\n---\n\n"
    idx4 = text.find(sec4_marker)
    dash_idx = text.rfind("---", 0, idx4)
    text = text[:dash_idx] + insert_q07 + text[dash_idx:]

    # Inserção da Questão 08: no fim da Seção 4 (antes de "## 5. Equivalência, Transformação de Estruturas e Paráfrase")
    sec5_marker = "## 5. Equivalência, Transformação de Estruturas e Paráfrase"
    insert_q08 = q08_text + "\n---\n\n"
    idx5 = text.find(sec5_marker)
    dash_idx = text.rfind("---", 0, idx5)
    text = text[:dash_idx] + insert_q08 + text[dash_idx:]

    # Inserção da Questão 09: na Seção 5.3 (antes de "### 5.4 Mecanismos de Nominalização e Concisão Textual")
    sec54_marker = "### 5.4 Mecanismos de Nominalização e Concisão Textual"
    insert_q09 = "\n---\n" + q09_text + "\n---\n\n"
    idx54 = text.find(sec54_marker)
    text = text[:idx54] + insert_q09 + text[idx54:]

    # Inserção da Questão 10: no fim da Seção 6 (antes de "## 🌐 Fontes Oficiais e Referências Bibliográficas")
    sec_fontes = "## 🌐 Fontes Oficiais e Referências Bibliográficas"
    insert_q10 = q10_text + "\n---\n\n"
    idxf = text.find(sec_fontes)
    dash_idx = text.rfind("---", 0, idxf)
    text = text[:dash_idx] + insert_q10 + text[dash_idx:]

    with open(FILE_6, "w", encoding="utf-8") as f:
        f.write(text)

    print("Arquivo 06 enriquecido com sucesso.")

enrich_file_6()
