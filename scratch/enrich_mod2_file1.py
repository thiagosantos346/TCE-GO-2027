import os, re

FILE = r"fontes_de_estudo/conhecimentos_gerais/02_matematica_e_raciocinio_logico/01_conjuntos_numericos_fracoes_e_aritmetica.md"

q06_text = """
### Questão 06
**(FCC – TRT-23 – Analista Judiciário)**  
Considere a expressão numérica $E = 0{,}333... + \\frac{1}{6} - 0{,}25$. O valor exato de $E$ expresso sob a forma de fração irredutível é igual a:

* **A)** $\\frac{1}{4}$
* **B)** $\\frac{1}{3}$
* **C)** $\\frac{1}{2}$
* **D)** $\\frac{5}{12}$
* **E)** $\\frac{7}{12}$

> **Comentário Detalhado:**
>
> - **1º Passo:** Converter os números decimais e a dízima periódica em frações ordinárias:  
>   - A dízima periódica simples $0{,}333...$ tem como fração geratriz $\\frac{3}{9} = \\frac{1}{3}$.  
>   - O decimal exato $0{,}25$ corresponde a $\\frac{25}{100} = \\frac{1}{4}$.  
> - **2º Passo:** Substituir os valores na expressão:  
>   $$E = \\frac{1}{3} + \\frac{1}{6} - \\frac{1}{4}$$  
> - **3º Passo:** Obter o MMC dos denominadores $3, 6, 4$:  
>   $MMC(3, 6, 4) = 12$.  
> - **4º Passo:** Reduzir ao mesmo denominador e efetuar as operações:  
>   $$E = \\frac{4}{12} + \\frac{2}{12} - \\frac{3}{12} = \\frac{4 + 2 - 3}{12} = \\frac{3}{12}$$  
> - **5º Passo:** Simplificar a fração obtida:  
>   $$\\frac{3}{12} = \\frac{1}{4}$$  
> - **Conclusão:** O resultado é $\\frac{1}{4}$ (Alternativa A).
>
> **Gabarito: A**
"""

q07_text = """
### Questão 07
**(FCC – TCE-GO – Analista de Controle Externo)**  
O valor numérico da expressão aritmética $K = \\frac{2^{20} + 2^{18}}{2^{19} - 2^{17}}$ é igual a:

* **A)** $\\frac{5}{3}$
* **B)** $\\frac{10}{3}$
* **C)** $2$
* **D)** $4$
* **E)** $\\frac{5}{6}$

> **Comentário Detalhado:**
>
> - **Método de Resolução (Fatoração por Colocação em Evidência):** Em expressões com potências de mesma base com expoentes elevados, a estratégia padrão da FCC consiste em colocar em evidência a potência de menor expoente no numerador e no denominador.  
> - **No numerador:** $2^{20} + 2^{18} = 2^{18} \\cdot (2^2 + 1) = 2^{18} \\cdot (4 + 1) = 2^{18} \\cdot 5$.  
> - **No denominador:** $2^{19} - 2^{17} = 2^{17} \\cdot (2^2 - 1) = 2^{17} \\cdot (4 - 1) = 2^{17} \\cdot 3$.  
> - **Dividindo numerador por denominador:**  
>   $$K = \\frac{2^{18} \\cdot 5}{2^{17} \\cdot 3} = \\frac{2^{18}}{2^{17}} \\cdot \\frac{5}{3} = 2^{18-17} \\cdot \\frac{5}{3} = 2^1 \\cdot \\frac{5}{3} = \\frac{10}{3}$$  
> - **Conclusão:** O valor numérico de $K$ é exatamente $\\frac{10}{3}$ (Alternativa B).
>
> **Gabarito: B**
"""

q08_text = """
### Questão 08
**(FCC – METRÔ-SP – Analista)**  
O número de divisores naturais positivos do número inteiro $N = 360$ é igual a:

* **A)** $18$
* **B)** $24$
* **C)** $20$
* **D)** $30$
* **E)** $12$

> **Comentário Detalhado:**
>
> - **Regra da Quantidade de Divisores Positivos:** Para determinar o número de divisores positivos de um inteiro $N$, realiza-se a decomposição canônica em fatores primos:  
>   $$N = p_1^{\\alpha_1} \\cdot p_2^{\\alpha_2} \\cdot ... \\cdot p_k^{\\alpha_k}$$  
>   A quantidade total de divisores positivos é dada pelo produto dos expoentes acrescidos de uma unidade:  
>   $$D(N) = (\\alpha_1 + 1) \\cdot (\\alpha_2 + 1) \\cdot ... \\cdot (\\alpha_k + 1)$$  
> - **Fatoração de 360:**  
>   $360 = 36 \\times 10 = (2^2 \\cdot 3^2) \\cdot (2 \\cdot 5) = 2^3 \\cdot 3^2 \\cdot 5^1$.  
> - **Cálculo dos divisores:**  
>   - Expoente da base 2: $\\alpha_1 = 3 \\rightarrow (3 + 1) = 4$  
>   - Expoente da base 3: $\\alpha_2 = 2 \\rightarrow (2 + 1) = 3$  
>   - Expoente da base 5: $\\alpha_3 = 1 \\rightarrow (1 + 1) = 2$  
>   $$D(360) = 4 \\times 3 \\times 2 = 24$$  
> - **Conclusão:** O número 360 possui exatamente 24 divisores naturais positivos (Alternativa B).
>
> **Gabarito: B**
"""

q09_text = """
### Questão 09
**(FCC – TRT-14 – Analista Judiciário)**  
Um servidor do tribunal recebeu determinado lote de processos para instruir. No primeiro dia, analisou $\\frac{2}{5}$ do total de processos; no segundo dia, analisou $\\frac{1}{3}$ do que havia sobrado; e, no terceiro dia, concluiu os últimos $24$ processos restantes. O número total de processos contidos no lote original era igual a:

* **A)** $50$
* **B)** $60$
* **C)** $75$
* **D)** $80$
* **E)** $90$

> **Comentário Detalhado:**
>
> - **Método da Cadeia Regressiva (Fração de Resto):**  
>   - Seja $P$ o total original de processos.  
>   - **Dia 1:** O servidor instruiu $\\frac{2}{5}P$.  
>     Restante após o dia 1: $1 - \\frac{2}{5} = \\frac{3}{5}P$.  
>   - **Dia 2:** O servidor instruiu $\\frac{1}{3}$ do restante:  
>     $$\\frac{1}{3} \\times \\frac{3}{5}P = \\frac{1}{5}P$$  
>     Fração total instruída nos dois primeiros dias: $\\frac{2}{5}P + \\frac{1}{5}P = \\frac{3}{5}P$.  
>     Restante final para o dia 3: $1 - \\frac{3}{5} = \\frac{2}{5}P$.  
>   - **Dia 3:** Esse restante final corresponde a 24 processos:  
>     $$\\frac{2}{5}P = 24 \\implies 2P = 24 \\times 5 = 120 \\implies P = \\frac{120}{2} = 60$$  
> - **Conferência:** $60 \\times \\frac{2}{5} = 24$ no 1º dia (sobram 36); $\\frac{1}{3} \\times 36 = 12$ no 2º dia (sobram 24); $24$ no 3º dia. Perfeito.
>
> **Gabarito: B**
"""

q10_text = """
### Questão 10
**(FCC – TCE-PI – Auditor de Controle Externo)**  
Considere a sequência infinita de letras:  
$$T, C, E, G, O, I, A, S, T, C, E, G, O, I, A, S, T, C, E, ...$$  
formada pela repetição contínua do bloco de palavras *"TCEGOIAS"*. A letra que ocupa a 2027ª posição dessa sequência é:

* **A)** T
* **B)** C
* **C)** E
* **D)** G
* **E)** S

> **Comentário Detalhado:**
>
> - **Método dos Ciclos Periódicos e Aritmética dos Restos:**  
>   - O bloco padrão repetitivo é *"T, C, E, G, O, I, A, S"*.  
>   - Contagem do período: O bloco possui exatamente **8 letras**.  
>   - Para determinar o elemento na posição $N = 2027$, divide-se $2027$ pelo tamanho do ciclo ($8$) e analisa-se o resto:  
>     $$2027 = 8 \\times 253 + 3$$  
>     (pois $8 \\times 253 = 2024$, e $2027 - 2024 = 3$).  
>   - O quociente $253$ indica que o ciclo de 8 letras completou-se exatamente 253 vezes.  
>   - O resto $3$ indica que a letra procurada é a **3ª letra** do bloco padrão.  
> - **Localização no bloco:**  
>   1ª = T, 2ª = C, **3ª = E**.  
> - **Conclusão:** A letra na 2027ª posição é a letra **E** (Alternativa C).
>
> **Gabarito: C**
"""

def enrich_mod2_file1():
    with open(FILE, "r", encoding="utf-8") as f:
        text = f.read()

    # Inserção da Questão 06: na Seção 1.2 (antes de "### 1.3 Algoritmo da Divisão Euclidiana")
    sec13 = "### 1.3 Algoritmo da Divisão Euclidiana e Aritmética dos Restos"
    idx13 = text.find(sec13)
    text = text[:idx13] + "\n---\n" + q06_text + "\n---\n\n" + text[idx13:]

    # Inserção da Questão 07: no fim da Seção 2 (antes de "## 3. Teoria dos Números")
    sec3 = "## 3. Teoria dos Números: Divisibilidade, Primos, MMC e MDC"
    idx3 = text.find(sec3)
    dash_idx = text.rfind("---", 0, idx3)
    text = text[:dash_idx] + q07_text + "\n---\n\n" + text[dash_idx:]

    # Inserção da Questão 08: na Seção 3.2 (antes de "### 3.3 Mínimo Múltiplo Comum")
    sec33 = "### 3.3 Mínimo Múltiplo Comum: Ciclos, Coincidências e Periodicidade"
    idx33 = text.find(sec33)
    text = text[:idx33] + "\n---\n" + q08_text + "\n---\n\n" + text[idx33:]

    # Inserção da Questão 09: no fim da Seção 4 (antes de "## 5. Modelagem e Resolução de Problemas no Padrão FCC")
    sec5 = "## 5. Modelagem e Resolução de Problemas no Padrão FCC"
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

    print("Module 02 File 01 enriquecido com sucesso.")

enrich_mod2_file1()
