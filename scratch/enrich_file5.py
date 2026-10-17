import os, re

FILE_5 = r"fontes_de_estudo/conhecimentos_gerais/01_lingua_portuguesa/05_concordancia_regencia_e_crase.md"

q06_text = """
### Questão 06
**(FCC – TRT-23 – Analista Judiciário)**  
Considere as frases a seguir quanto à concordância verbal segundo a norma culta:  

I. *A maioria dos auditores de controle externo **rejeitou** a proposta de acordo.*  
II. *Cerca de vinte por cento do orçamento municipal **foram destinados** à saúde básica.*  
III. *Faltavam, naquele momento crítico, **coragem e determinação** ao gestor público.*  
IV. *Mais de um fiscal **cumprimentaram-se** cordialmente na entrada do plenário.*  

A concordância verbal está inteiramente correta em:

* **A)** I e II, apenas.
* **B)** I, II, III e IV.
* **C)** II e III, apenas.
* **D)** I, III e IV, apenas.
* **E)** III e IV, apenas.

> **Comentário Detalhado:**
>
> - **Item I:** Correto. Diante de sujeito formado por expressão partitiva (*A maioria de*) seguida de adjunto no plural (*dos auditores*), a concordância é facultativa: o verbo pode concordar no singular com o núcleo partitivo (*rejeitou*) ou ir para o plural concordando com o especificador (*rejeitaram*).
> - **Item II:** Correto. Com expressões percentuais seguidas de substantivo (*vinte por cento do orçamento*), o verbo pode concordar com o número percentual (*vinte* $\rightarrow$ plural: *foram destinados*) ou com o termo partitivo singular (*orçamento* $\rightarrow$ singular: *foi destinado*). Logo, o plural é plenamente lícito.
> - **Item III:** Correto. Estando o sujeito composto posposto ao verbo (*coragem e determinação*), o verbo pode concordar no plural com a totalidade dos núcleos (*faltavam*) ou concordar atrativamente no singular com o núcleo mais próximo (*faltava*).
> - **Item IV:** Correto. Com a expressão *"mais de um"*, a regra geral impõe o verbo no singular; todavia, quando o verbo exprime **reciprocidade** de ação (indicada pelo pronome reflexivo/recíproco *se*), o verbo vai **obrigatoriamente para o plural**: *"cumprimentaram-se"* (um cumprimentou o outro reciprocamente).
> - **Conclusão:** Todos os quatro itens (I, II, III e IV) estão em perfeita conformidade gramatical.
>
> **Gabarito: B**
"""

q07_text = """
### Questão 07
**(FCC – TCE-GO – Analista de Controle Externo)**  
Assinale a alternativa em que a concordância nominal atende integralmente às exigências da norma culta:

* **A)** Seguem anexos as certidões negativas e os comprovantes de quitação eleitoral dos candidatos.
* **B)** A procuradora declarou que estava meia preocupada com o resultado do julgamento dos embargos.
* **C)** É proibido a entrada de pessoas não autorizadas na sala de deliberações secretas dos conselheiros.
* **D)** As auditoras mesmas elaboraram os relatórios circunstanciados, demonstrando que haviam bastantes motivos para impugnar o edital.
* **E)** Havia menas divergências entre os membros da corte técnica durante a última sessão plenária.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O adjetivo *anexo* concorda em gênero e número com o substantivo a que se refere: como os substantivos são *certidões* (feminino) e *comprovantes* (masculino), o adjetivo anteposto deve concordar com o mais próximo (*"Seguem anexas as certidões..."*) ou ir para o masculino plural caso posposto. Além disso, a locução invariável é *"em anexo"*.
> - **B)** Incorreta. *Meio*, com valor de advérbio de intensidade modificando o adjetivo *preocupada*, é **invariável**: *"estava meio preocupada"* (e nunca "meia").
> - **C)** Incorreta. Nas expressões do tipo *é proibido*, havendo artigo determinado anteposto ao substantivo (*"a entrada"*), a concordância é obrigatória: *"É proibida a entrada..."*. Apenas se não houvesse artigo seria correto o masculino neutro (*"É proibido entrada"*).
> - **D)** Correta. O pronome demonstrativo reforçador *mesmo* flexiona-se normalmente concordando com o sujeito (*"As auditoras mesmas"* = elas próprias). A palavra *bastantes*, funcionando como pronome adjetivo indefinido que acompanha e quantifica substantivo no plural (*motivos*), flexiona-se obrigatoriamente no plural (*"bastantes motivos"* = muitos motivos).
> - **E)** Incorreta. A palavra *menos* é estritamente invariável na língua culta; a forma "menas" não existe no vocabulário padrão.
>
> **Gabarito: D**
"""

q08_text = """
### Questão 08
**(FCC – METRÔ-SP – Advogado)**  
Considere as lacunas no período seguinte:  
*"A conduta do servidor público deve ser sempre compatível __________ a dignidade da função; suas manifestações técnicas não podem ser alheias __________ preceitos constitucionais, devendo o parecer mostrar-se atinente __________ matérias estritamente submetidas à sua apreciação."*

As preposições que preenchem correta e respectivamente as lacunas da frase são:

* **A)** a – de – em
* **B)** com – aos – às
* **C)** sobre – com – com as
* **D)** por – para os – nas
* **E)** com – dos – pelas

> **Comentário Detalhado:**
>
> - **1ª lacuna:** O adjetivo *compatível* rege legitimamente a preposição **com** (*compatível com a dignidade*).
> - **2ª lacuna:** O adjetivo *alheio* rege a preposição **a** (*alheio a algo*); diante do substantivo masculino plural *preceitos*, dá-se a contração **aos** (*alheias aos preceitos constitucionais*).
> - **3ª lacuna:** O adjetivo *atinente* rege a preposição **a** (*atinente a algo*); diante do substantivo feminino plural *matérias*, ocorre a crase obrigatória: preposição *a* + artigo *as* = **às** (*atinente às matérias*).
> - **Conclusão:** A alternativa **B** apresenta a sequência correta: *com – aos – às*.
>
> **Gabarito: B**
"""

q09_text = """
### Questão 09
**(FCC – DPE-RS – Analista Processual)**  
O sinal indicativo de crase está empregado em estrita observância à norma-padrão em:

* **A)** A comissão de licitação procedeu à abertura dos envelopes perante à uma plateia atenta.
* **B)** Os auditores compareceram à audiência pública dispostos à colaborar com o esclarecimento dos fatos.
* **C)** O presidente do tribunal comunicou o resultado à Vossa Excelência durante a reunião do conselho.
* **D)** À medida que os documentos contábeis eram analisados, as fraudes vinham à tona de forma irrefutável.
* **E)** O auditor entregou o parecer à um de seus assessores diretos logo após o almoço.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. É proibida a crase diante de artigo indefinido (*"uma plateia"*), pois não há artigo definido a fundir; além disso, a preposição *perante* já rege o termo sem preposição *a*.
> - **B)** Incorreta. É absolutamente proibido o emprego de crase antes de verbos (*"à colaborar"*), uma vez que verbos não admitem artigo feminino.
> - **C)** Incorreta. É proibida a crase diante de pronomes de tratamento em geral (*"Vossa Excelência"*), haja vista que não aceitam artigo definido feminino (exceções: *senhora*, *senhorita* e *dona*).
> - **D)** Correta. Em *"À medida que"*, trata-se de locução conjuntiva proporcional feminina de núcleo substantivo, na qual o acento grave indicativo de crase é rigorosamente **obrigatório**. Em *"à tona"*, temos locução adverbial de modo feminina, que também exige o sinal indicativo de crase na norma culta.
> - **E)** Incorreta. É proibido o uso de crase diante de palavras masculinas e de pronomes indefinidos (*"à um"*).
>
> **Gabarito: D**
"""

q10_text = """
### Questão 10
**(FCC – TRT-14 – Analista Judiciário)**  
Considere as frases a seguir no tocante ao emprego do acento indicativo de crase:  

I. *O assessor fez menção **àquela** portaria revogada pela presidência.*  
II. *O relatório referiu-se **à sua** atuação técnica de forma muito elogiosa.*  
III. *O procurador dedicou-se **à** elucidar os pontos controvertidos do edital.*  
IV. *A inspeção estendeu-se até **à** meia-noite sem interrupções.*  

O uso do sinal indicativo de crase é FACULTATIVO em:

* **A)** I e III.
* **B)** II e IV, apenas.
* **C)** I, II e IV.
* **D)** II, apenas.
* **E)** III e IV, apenas.

> **Comentário Detalhado:**
>
> - **Item I:** Incorreto para o enunciado. Quem faz menção, faz menção *a* algo (preposição obrigatória). O pronome demonstrativo *aquela* inicia-se pela letra *a*. A fusão da preposição com o *a* inicial de *aquela* resulta em crase **obrigatória** (*àquela*), e não facultativa.
> - **Item II:** Correto. Diante de **pronome possessivo feminino singular** (*sua*, *minha*, *tua*), o uso do artigo definido é facultativo na norma culta. Havendo preposição exigida pelo verbo (*referir-se a*), o acento grave de crase torna-se **facultativo** (*à sua* ou *a sua*).
> - **Item III:** Incorreto. Diante de verbo no infinitivo (*elucidar*), a crase é **proibida**.
> - **Item IV:** Correto. Após a preposição **até**, o emprego da preposição *a* é facultativo. Sendo a palavra subsequente feminina determinada (*meia-noite*), a crase é **facultativa** (*até à meia-noite* ou *até a meia-noite*).
> - **Conclusão:** O uso facultativo da crase ocorre nos itens II e IV.
>
> **Gabarito: B**
"""

def enrich_file_5():
    with open(FILE_5, "r", encoding="utf-8") as f:
        text = f.read()

    # Inserção da Questão 06: no fim da Seção 1 (antes de "## 2. Verbos Impessoais e a Dinâmica das Locuções Verbais")
    sec2_marker = "## 2. Verbos Impessoais e a Dinâmica das Locuções Verbais"
    insert_q06 = q06_text + "\n---\n\n"
    idx2 = text.find(sec2_marker)
    dash_idx = text.rfind("---", 0, idx2)
    text = text[:dash_idx] + insert_q06 + text[dash_idx:]

    # Inserção da Questão 07: na Seção 3.5 (antes de "## 4. Regência Verbal: Transitividade")
    sec4_marker = "## 4. Regência Verbal: Transitividade e Complementação dos Verbos Críticos"
    insert_q07 = q07_text + "\n---\n\n"
    idx4 = text.find(sec4_marker)
    dash_idx = text.rfind("---", 0, idx4)
    text = text[:dash_idx] + insert_q07 + text[dash_idx:]

    # Inserção da Questão 08: no fim da Seção 5 (antes de "## 6. Teoria Geral e Emprego do Sinal Indicativo de Crase")
    sec6_marker = "## 6. Teoria Geral e Emprego do Sinal Indicativo de Crase"
    insert_q08 = q08_text + "\n---\n\n"
    idx6 = text.find(sec6_marker)
    dash_idx = text.rfind("---", 0, idx6)
    text = text[:dash_idx] + insert_q08 + text[dash_idx:]

    # Inserção da Questão 09: na Seção 6.4 (antes de "### 6.5 Casos de Crase Facultativa")
    sec65_marker = "### 6.5 Casos de Crase Facultativa"
    insert_q09 = "\n---\n" + q09_text + "\n---\n\n"
    idx65 = text.find(sec65_marker)
    text = text[:idx65] + insert_q09 + text[idx65:]

    # Inserção da Questão 10: no fim da Seção 6 (antes de "## 🌐 Fontes Oficiais e Referências Bibliográficas")
    sec_fontes = "## 🌐 Fontes Oficiais e Referências Bibliográficas"
    insert_q10 = q10_text + "\n---\n\n"
    idxf = text.find(sec_fontes)
    dash_idx = text.rfind("---", 0, idxf)
    text = text[:dash_idx] + insert_q10 + text[dash_idx:]

    with open(FILE_5, "w", encoding="utf-8") as f:
        f.write(text)

    print("Arquivo 05 enriquecido com sucesso.")

enrich_file_5()
