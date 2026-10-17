import os, re

FILE = r"fontes_de_estudo/conhecimentos_gerais/02_matematica_e_raciocinio_logico/04_raciocinio_sequencial_temporal_espacial_e_verbal.md"

q06_text = """
### Questão 06
**(FCC – TRT-23 – Analista Judiciário)**  
Considere a sucessão lógica de letras:  
$$U, D, T, Q, C, S, S, O, N, ...$$  
A próxima letra que dá continuidade lógica e consistente a essa sequência é:

* **A)** D
* **B)** V
* **C)** O
* **D)** T
* **E)** Q

> **Comentário Detalhado:**
>
> - **Identificação do Padrão Semântico Oculto:**  
>   - Em sequências literais da FCC que não seguem ordem alfabética aritmética evidente, a banca comumente recorre à **inicial semântica dos números cardinais ou ordinais**:  
>     - **U** $\rightarrow$ Um  
>     - **D** $\rightarrow$ Dois  
>     - **T** $\rightarrow$ Três  
>     - **Q** $\rightarrow$ Quatro  
>     - **C** $\rightarrow$ Cinco  
>     - **S** $\rightarrow$ Seis  
>     - **S** $\rightarrow$ Sete  
>     - **O** $\rightarrow$ Oito  
>     - **N** $\rightarrow$ Nove  
>   - O próximo número da contagem natural é o número **Dez**.  
>   - A letra inicial da palavra "Dez" é a letra **D**.  
> - **Conclusão:** A próxima letra é **D** (Alternativa A).
>
> **Gabarito: A**
"""

q07_text = """
### Questão 07
**(FCC – TCE-GO – Analista de Controle Externo)**  
Um relógio analógico convencional de ponteiros marca exatamente $3$ horas e $40$ minutos. A medida do menor ângulo formado entre o ponteiro das horas e o ponteiro dos minutos nesse instante é igual a:

* **A)** $120^\\circ$
* **B)** $130^\\circ$
* **C)** $140^\\circ$
* **D)** $150^\\circ$
* **E)** $115^\\circ$

> **Comentário Detalhado:**
>
> - **Método da Cinemática Angular dos Relógios:**  
>   - O círculo completo tem $360^\\circ$, dividido em 12 intervalos de horas ($30^\\circ$ por hora).  
>   - O ponteiro dos minutos desloca-se a uma velocidade de $6^\\circ$ por minuto ($360^\\circ / 60\\text{ min}$).  
>   - O ponteiro das horas desloca-se a uma velocidade de $0{,}5^\\circ$ por minuto ($30^\\circ / 60\\text{ min}$).  
> - **Fórmula Direta do Ângulo entre Ponteiros (FCC):**  
>   $$\\theta = \\left| \\frac{60H - 11M}{2} \\right|$$  
>   onde $H = 3$ horas e $M = 40$ minutos.  
> - **Substituindo os valores:**  
>   $$\\theta = \\left| \\frac{60 \\times 3 - 11 \\times 40}{2} \\right| = \\left| \\frac{180 - 440}{2} \\right| = \\left| \\frac{-260}{2} \\right| = |-130^\\circ| = 130^\\circ$$  
> - Como $130^\\circ \\le 180^\\circ$, este já é o menor ângulo formado entre eles.  
> - **Conclusão:** O menor ângulo mede exatamente $130^\\circ$ (Alternativa B).
>
> **Gabarito: B**
"""

q08_text = """
### Questão 08
**(FCC – METRÔ-SP – Analista)**  
Uma pilha maciça de cubos idênticos de $1\\text{ cm}$ de aresta foi montada sobre uma mesa plana de modo que sua vista frontal e sua vista lateral direita são ambas formadas por uma grade quadrada de $3 \\times 3$ cubos completamente preenchida. O número MÍNIMO de cubinhos necessários para formar essa pilha é:

* **A)** $9$
* **B)** $12$
* **C)** $15$
* **D)** $18$
* **E)** $27$

> **Comentário Detalhado:**
>
> - **Análise das Vistas Ortogonais:**  
>   - A vista frontal mostra uma malha $3 \\times 3$ preenchida, o que significa que para cada uma das 3 colunas e cada um dos 3 níveis de altura (1, 2 e 3) deve haver pelo menos um cubo.  
>   - A vista lateral direita também mostra uma malha $3 \\times 3$ preenchida, o que significa que para cada uma das 3 linhas de profundidade e cada um dos 3 níveis de altura deve haver pelo menos um cubo.  
> - **Cálculo do Número Mínimo de Cubos:**  
>   - Em cada nível de altura (térreo, 2º andar e 3º andar), precisamos cobrir 3 posições em $x$ e 3 posições em $y$.  
>   - Para minimizar cubos em cada nível de altura $z$, basta posicionar os cubos ao longo da diagonal da base: $(1,1), (2,2), (3,3)$. Com apenas 3 cubos em cada nível, a projeção frontal projeta as 3 colunas e a projeção lateral projeta as 3 profundidades!  
>   - Como são 3 níveis de altura, o número mínimo total de cubos é:  
>     $$\\text{Mínimo} = 3 \\text{ níveis} \\times 3 \\text{ cubos por nível} = 9 \\text{ cubos}$$  
> - **Conclusão:** O número mínimo é 9 cubinhos (Alternativa A).
>
> **Gabarito: A**
"""

q09_text = """
### Questão 09
**(FCC – DPE-RS – Analista)**  
Considere o conjunto de cinco palavras a seguir:  
*Goiânia*, *Curitiba*, *Brasília*, *Teresina*, *Manaus*

Quatro dessas palavras guardam uma característica lógica comum que as reúne em uma mesma classe conceitual, enquanto uma delas é a intrusa. A palavra intrusa é:

* **A)** Goiânia
* **B)** Curitiba
* **C)** Brasília
* **D)** Teresina
* **E)** Manaus

> **Comentário Detalhado:**
>
> - **Critério de Classificação Geopolítica e Administrativa:**  
>   - *Goiânia* é a capital do Estado de Goiás.  
>   - *Curitiba* é a capital do Estado do Paraná.  
>   - *Teresina* é a capital do Estado do Piauí.  
>   - *Manaus* é a capital do Estado do Amazonas.  
>   - Todas essas quatro são **capitais de Estados-membros** da federação brasileira, municípios com autonomia municipal típica (prefeito e câmara de vereadores).  
>   - *Brasília*, por sua vez, é a **Capital Federal**, sediada no Distrito Federal, ente federativo anômalo que acumula competências estaduais e municipais e não é dividido em municípios.  
> - **Conclusão:** O elemento intruso é **Brasília** (Alternativa C).
>
> **Gabarito: C**
"""

q10_text = """
### Questão 10
**(FCC – TRT-14 – Analista Judiciário)**  
Três suspeitos de vazar um relatório confidencial de auditoria prestaram os seguintes depoimentos:  
- **Alberto:** *"Bruno é culpado."*  
- **Bruno:** *"Carlos é culpado."*  
- **Carlos:** *"O que Bruno disse é mentira."*  

Sabe-se que exatamente um dos três suspeitos disse a verdade e que apenas um deles é o culpado. O inocente que disse a verdade e o verdadeiro culpado são, respectivamente:

* **A)** Alberto e Bruno
* **B)** Carlos e Alberto
* **C)** Bruno e Carlos
* **D)** Carlos e Bruno
* **E)** Alberto e Carlos

> **Comentário Detalhado:**
>
> - **Identificação do Par Contraditório:**  
>   - Bruno afirma: *"Carlos é culpado"*.  
>   - Carlos afirma: *"O que Bruno disse é mentira"*.  
>   - As falas de Bruno e Carlos são **rigorosamente contraditórias**. Pelo Princípio da Não Contradição e do Terceiro Excluído, exatamente uma delas é verdadeira e a outra é falsa.  
> - **Dedução da Terceira Declaração:**  
>   - Como o enunciado informa que **apenas um dos três disse a verdade**, essa única verdade OBRIGATORIAMENTE está entre Bruno ou Carlos!  
>   - Portanto, a declaração de **Alberto é necessariamente FALSA**!  
> - **Análise da falsidade de Alberto:**  
>   - Alberto disse: *"Bruno é culpado"*. Como isso é falso, concluímos que **Bruno é INOCENTE**.  
> - **Análise de Bruno e Carlos:**  
>   - Agora suponha que Bruno tivesse dito a verdade. Se Bruno dissesse a verdade, Carlos seria o culpado. Mas Alberto disse que Bruno é culpado (falso, Bruno é inocente). E Carlos diria que Bruno mentiu (o que seria mentira, então Carlos mentiu). Isso daria Carlos culpado e mentiroso, e Bruno inocente que disse a verdade.  
>   - Mas se Alberto fosse o culpado? Se Alberto for o culpado, Carlos é inocente. Então o que Bruno disse ("Carlos é culpado") é FALSO!  
>   - Sendo a fala de Bruno falsa, a declaração de Carlos ("O que Bruno disse é mentira") torna-se **VERDADEIRA**!  
>   - Nesse caso: Alberto mentiu (F), Bruno mentiu (F) e Carlos disse a verdade (V) — exatamente 1 verdade!  
>   - E o culpado é **Alberto**, sendo Bruno e Carlos inocentes!  
> - **Conclusão:** Quem disse a verdade é **Carlos** (inocente), e o verdadeiro culpado é **Alberto** (Alternativa B).
>
> **Gabarito: B**
"""

def enrich_mod2_file4():
    with open(FILE, "r", encoding="utf-8") as f:
        text = f.read()

    # Inserção da Questão 06: no fim da Seção 1 (antes de "## 2. Orientação Temporal, Calendários e Relógios")
    sec2 = "## 2. Orientação Temporal, Calendários e Relógios"
    idx2 = text.find(sec2)
    dash_idx = text.rfind("---", 0, idx2)
    text = text[:dash_idx] + q06_text + "\n---\n\n" + text[dash_idx:]

    # Inserção da Questão 07: no fim da Seção 2 (antes de "## 3. Orientação Espacial, Transformações e Dobradura de Figuras")
    sec3 = "## 3. Orientação Espacial, Transformações e Dobradura de Figuras"
    idx3 = text.find(sec3)
    dash_idx = text.rfind("---", 0, idx3)
    text = text[:dash_idx] + q07_text + "\n---\n\n" + text[dash_idx:]

    # Inserção da Questão 08: no fim da Seção 3 (antes de "## 4. Formação de Conceitos e Discriminação de Elementos")
    sec4 = "## 4. Formação de Conceitos e Discriminação de Elementos"
    idx4 = text.find(sec4)
    dash_idx = text.rfind("---", 0, idx4)
    text = text[:dash_idx] + q08_text + "\n---\n\n" + text[dash_idx:]

    # Inserção da Questão 09: no fim da Seção 4 (antes de "## 5. Raciocínio Verbal e Problemas de Verdades e Mentiras")
    sec5 = "## 5. Raciocínio Verbal e Problemas de Verdades e Mentiras"
    idx5 = text.find(sec5)
    dash_idx = text.rfind("---", 0, idx5)
    text = text[:dash_idx] + q09_text + "\n---\n\n" + text[dash_idx:]

    # Inserção da Questão 10: no fim da Seção 5 (antes de "## 🌐 Fontes Oficiais e Referências Bibliográficas")
    sec_fontes = "## 🌐 Fontes Oficiais e Referências Bibliográficas"
    idxf = text.find(sec_fontes)
    dash_idx = text.rfind("---", 0, idxf)
    text = text[:dash_idx] + q10_text + "\n---\n\n" + text[dash_idx:]

    with open(FILE, "w", encoding="utf-8") as f:
        f.write(text)

    print("Module 02 File 04 enriquecido com sucesso.")

enrich_mod2_file4()
