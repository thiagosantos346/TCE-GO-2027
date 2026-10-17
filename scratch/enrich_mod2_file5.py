import os, re

FILE = r"fontes_de_estudo/conhecimentos_gerais/02_matematica_e_raciocinio_logico/05_logica_de_argumentacao_e_conclusoes_validas.md"

q06_text = """
### Questão 06
**(FCC – TRT-23 – Analista Judiciário)**  
Considere as seguintes frases:  

I. *"O Tribunal de Contas fiscaliza a execução orçamentária dos municípios goianos."*  
II. *"Quem foi o responsável por autorizar a despesa sem prévio empenho?"*  
III. *"Encaminhe imediatamente a documentação comprobatória à comissão de auditoria!"*  
IV. *"Ele é um excelente auditor governamental."*  

De acordo com os princípios da lógica clássica proposicional, classifica-se como proposição lógica estrita APENAS a frase indicada em:

* **A)** I.
* **B)** I e IV.
* **C)** II e III.
* **D)** I e III.
* **E)** II e IV.

> **Comentário Detalhado:**
>
> - **Conceito de Proposição Lógica:** É toda sentença declarativa que exprime um pensamento de sentido completo e à qual se pode atribuir com certeza, e de forma exclusiva, um valor de verdade (Verdadeiro ou Falso), respeitando os princípios da Identidade, Não Contradição e Terceiro Excluído.  
> - **Análise dos itens:**  
>   - **Item I:** *"O Tribunal de Contas fiscaliza..."* é uma oração declarativa com sujeito, verbo e sentido completo, passível de julgamento objetivo como V ou F. É **proposição lógica**.  
>   - **Item II:** É uma **frase interrogativa**. Perguntas não possuem valor de verdade (não são V nem F). Não é proposição.  
>   - **Item III:** É uma **frase imperativa** (ordem expressa por verbo no imperativo). Ordens, desejos e exclamações não possuem valor de verdade. Não é proposição.  
>   - **Item IV:** *"Ele é um excelente auditor"* é uma **sentença aberta**. O pronome "Ele" é uma variável indeterminada; sem saber a quem se refere, não é possível atribuir valor de verdade. Logo, não é proposição lógica no sentido estrito.  
> - **Conclusão:** Apenas a frase I é proposição lógica (Alternativa A).
>
> **Gabarito: A**
"""

q07_text = """
### Questão 07
**(FCC – TCE-GO – Analista de Controle Externo)**  
A negação lógica da proposição composta:  
*"Se o auditor encontra irregularidades nas contas, então o gestor público é multado e a prestação de contas é reprovada"*  
é formulada corretamente por:

* **A)** O auditor encontra irregularidades nas contas, mas o gestor público não é multado ou a prestação de contas não é reprovada.
* **B)** Se o auditor não encontra irregularidades nas contas, então o gestor público não é multado ou a prestação de contas não é reprovada.
* **C)** O auditor não encontra irregularidades nas contas e o gestor público não é multado e a prestação de contas não é reprovada.
* **D)** Se o gestor público não é multado e a prestação de contas não é reprovada, então o auditor não encontrou irregularidades.
* **E)** O auditor encontra irregularidades nas contas e o gestor público não é multado e a prestação de contas é reprovada.

> **Comentário Detalhado:**
>
> - **Estrutura Proposicional:**  
>   Seja $P$: *"o auditor encontra irregularidades"*.  
>   Seja $Q$: *"o gestor público é multado"*.  
>   Seja $R$: *"a prestação de contas é reprovada"*.  
>   A proposição dada tem a forma:  
>   $$P \\rightarrow (Q \\land R)$$  
> - **Regra da Negação da Condicional (Regra do MANÉ - Mantém a primeira E Nega a segunda):**  
>   $$\\neg [P \\rightarrow (Q \\land R)] \\iff P \\land \\neg (Q \\land R)$$  
> - **Aplicação da Lei de De Morgan para negar a conjunção $(Q \\land R)$:**  
>   $$\\neg (Q \\land R) \\iff \\neg Q \\lor \\neg R$$  
> - **Substituindo na fórmula:**  
>   $$P \\land (\\neg Q \\lor \\neg R)$$  
> - **Tradução para a linguagem natural:**  
>   *"O auditor encontra irregularidades nas contas, e/mas o gestor público não é multado ou a prestação de contas não é reprovada"*.  
> - **Conclusão:** A alternativa **A** expressa exatamente essa negação.
>
> **Gabarito: A**
"""

q08_text = """
### Questão 08
**(FCC – DPE-RS – Analista)**  
Dadas duas proposições simples $p$ e $q$, a proposição composta:  
$$[(p \\rightarrow q) \\land p] \\rightarrow q$$  
classifica-se logicamente como uma:

* **A)** Contingência, pois seu valor lógico depende dos valores atribuídos a $p$ e $q$.
* **B)** Contradição, pois seu valor lógico é sempre falso em qualquer circunstância.
* **C)** Tautologia, pois assume invariavelmente o valor verdadeiro para todas as combinações de valores lógicos de suas proposições componentes.
* **D)** Falácia da afirmação do consequente.
* **E)** Equivalência lógica bidirecional contingente.

> **Comentário Detalhado:**
>
> - **Construção da Tabela-Verdade:**  
>   | $p$ | $q$ | $p \\rightarrow q$ | $(p \\rightarrow q) \\land p$ | $[(p \\rightarrow q) \\land p] \\rightarrow q$ |
>   | :---: | :---: | :---: | :---: | :---: |
>   | V | V | V | V | **V** |
>   | V | F | F | F | **V** |
>   | F | V | V | F | **V** |
>   | F | F | V | F | **V** |
> - **Análise do Resultado:** A última coluna apresenta valor **Verdadeiro (V)** em todas as quatro linhas possíveis da tabela-verdade.  
> - Uma proposição composta cuja tabela-verdade resulta exclusivamente em valores verdadeiros é definida como **Tautologia** (trata-se da expressão formal da célebre regra de inferência válida do *Modus Ponens*).  
> - **Conclusão:** É uma Tautologia (Alternativa C).
>
> **Gabarito: C**
"""

q09_text = """
### Questão 09
**(FCC – METRÔ-SP – Analista)**  
Considere verdadeiras as seguintes premissas:  
1. *Se o certame é homologado, então os concursados são nomeados.*  
2. *Se os concursados são nomeados, então novas vagas no plenário são preenchidas.*  
3. *Novas vagas no plenário não foram preenchidas.*  

A partir dessas premissas, deduz-se corretamente que:

* **A)** O certame foi homologado e os concursados foram nomeados.
* **B)** Os concursados foram nomeados, mas o certame não foi homologado.
* **C)** O certame não foi homologado e os concursados não foram nomeados.
* **D)** O certame foi homologado, mas novas vagas não foram preenchidas.
* **E)** Nenhuma conclusão válida pode ser extraída a partir dessas premissas.

> **Comentário Detalhado:**
>
> - **Método do Encadeamento Lógico e Regras de Inferência (*Modus Tollens*):**  
>   - Premissa 3: *"Novas vagas no plenário não foram preenchidas"* = **VERDADE**.  
>   - Premissa 2: *"Se concursados são nomeados $\\rightarrow$ novas vagas são preenchidas"*.  
>     Como a premissa condicional é verdadeira e o consequente é FALSO (vagas não preenchidas), o antecedente obrigatoriamente tem de ser FALSO pelo *Modus Tollens*:  
>     $\\implies$ **"Os concursados NÃO foram nomeados"** é VERDADE.  
>   - Premissa 1: *"Se o certame é homologado $\\rightarrow$ concursados são nomeados"*.  
>     Como a condicional é verdadeira e o consequente é FALSO (concursados não foram nomeados), o antecedente tem de ser FALSO pelo *Modus Tollens*:  
>     $\\implies$ **"O certame NÃO foi homologado"** é VERDADE.  
> - **Conclusão Lógica Conjunta:** Conclui-se com certeza que *o certame não foi homologado e os concursados não foram nomeados* (Alternativa C).
>
> **Gabarito: C**
"""

q10_text = """
### Questão 10
**(FCC – TRT-14 – Analista Judiciário)**  
Considere que as seguintes premissas são verdadeiras:  
1. *Todos os auditores de controle externo são servidores dedicados.*  
2. *Alguns servidores dedicados são especialistas em tecnologia da informação.*  

Com base estritamente nessas duas premissas, é necessariamente correto concluir que:

* **A)** Todos os auditores de controle externo são especialistas em tecnologia da informação.
* **B)** Nenhum auditor de controle externo é especialista em tecnologia da informação.
* **C)** Pelo menos um auditor de controle externo é especialista em tecnologia da informação.
* **D)** É possível que nenhum auditor de controle externo seja especialista em tecnologia da informação.
* **E)** Todos os especialistas em tecnologia da informação são auditores de controle externo.

> **Comentário Detalhado:**
>
> - **Análise via Diagramas de Euler-Venn:**  
>   - Seja $A$ o conjunto dos auditores, $D$ o conjunto dos servidores dedicados e $TI$ o conjunto dos especialistas em TI.  
>   - Premissa 1: *"Todos os auditores são dedicados"* $\implies A \\subseteq D$ (o círculo de $A$ está totalmente contido dentro do círculo de $D$).  
>   - Premissa 2: *"Alguns dedicados são especialistas em TI"* $\implies D \\cap TI \\neq \\emptyset$ (há intersecção entre o conjunto $D$ e o conjunto $TI$).  
> - **Posicionamento do conjunto $TI$ em relação a $A$:**  
>   - O conjunto $TI$ intercepta o círculo maior $D$. Essa intersecção pode ocorrer na região de $D$ fora de $A$, ou pode alcançar a região interna de $A$.  
>   - Como não há nenhuma premissa vinculando diretamente $A$ a $TI$, **não se pode garantir** que haja auditores em $TI$, nem se pode garantir que não haja.  
>   - Portanto, a única afirmação necessariamente verdadeira do ponto de vista da lógica dedutiva modal é que **é perfeitamente possível que nenhum auditor seja especialista em TI** (o círculo de $TI$ pode interceptar apenas os elementos de $D$ que não pertencem a $A$).  
> - **Conclusão:** É possível que nenhum auditor de controle externo seja especialista em TI (Alternativa D).
>
> **Gabarito: D**
"""

def enrich_mod2_file5():
    with open(FILE, "r", encoding="utf-8") as f:
        text = f.read()

    # Inserção da Questão 06: no fim da Seção 1 (antes de "## 2. Álgebra Proposicional")
    sec2 = "## 2. Álgebra Proposicional: Negações e Equivalências Clássicas"
    idx2 = text.find(sec2)
    dash_idx = text.rfind("---", 0, idx2)
    text = text[:dash_idx] + q06_text + "\n---\n\n" + text[dash_idx:]

    # Inserção da Questão 07: na Seção 2.2 (antes de "### 2.3 Equivalências Notáveis")
    sec23 = "### 2.3 Equivalências Notáveis da Condicional: Contrapositiva e Disjuntiva (NEYA)"
    idx23 = text.find(sec23)
    dash_idx = text.rfind("---", 0, idx23)
    text = text[:dash_idx] + q07_text + "\n---\n\n" + text[dash_idx:]

    # Inserção da Questão 08: no fim da Seção 2 (antes de "## 3. Validade de Argumentos Dedutivos")
    sec3 = "## 3. Validade de Argumentos Dedutivos e Regras de Inferência"
    idx3 = text.find(sec3)
    dash_idx = text.rfind("---", 0, idx3)
    text = text[:dash_idx] + q08_text + "\n---\n\n" + text[dash_idx:]

    # Inserção da Questão 09: no fim da Seção 3 (antes de "## 4. Lógica de Primeira Ordem")
    sec4 = "## 4. Lógica de Primeira Ordem: Quantificadores e Silogismos Categóricos"
    idx4 = text.find(sec4)
    dash_idx = text.rfind("---", 0, idx4)
    text = text[:dash_idx] + q09_text + "\n---\n\n" + text[dash_idx:]

    # Inserção da Questão 10: no fim da Seção 4 (antes de "## 🌐 Fontes Oficiais e Referências Bibliográficas")
    sec_fontes = "## 🌐 Fontes Oficiais e Referências Bibliográficas"
    idxf = text.find(sec_fontes)
    dash_idx = text.rfind("---", 0, idxf)
    text = text[:dash_idx] + q10_text + "\n---\n\n" + text[dash_idx:]

    with open(FILE, "w", encoding="utf-8") as f:
        f.write(text)

    print("Module 02 File 05 enriquecido com sucesso.")

enrich_mod2_file5()
