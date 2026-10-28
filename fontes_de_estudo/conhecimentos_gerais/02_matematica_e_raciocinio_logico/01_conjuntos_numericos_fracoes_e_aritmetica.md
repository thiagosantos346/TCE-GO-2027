# 01 - Aritmética e Conjuntos Numéricos

> **Matéria:** Matemática e Raciocínio Lógico  
> **Cargos:** A01 – Técnico de Controle Externo (Adm) / B02 – Técnico de Controle Externo (TI)  
> **Arquivo:** `01_conjuntos_numericos_fracoes_e_aritmetica.md`  
> **Status:** 🟢 Teoria Aprofundada + 5 Questões FCC Comentadas (A a E)



---


## 📌 Ementa / Itens do Edital
- Números inteiros e racionais: operações (adição, subtração, multiplicação, divisão, potenciação).
- Expressões numéricas.
- Múltiplos e divisores de números naturais.
- Problemas envolvendo números inteiros e racionais.
- Frações e operações com frações.

---

## 🧭 Sumário

1. [Conjuntos Numéricos Fundamentais e Propriedades Estruturais](#1-conjuntos-numericos-fundamentais-e-propriedades-estruturais)
    1. [Conjunto dos Números Naturais e Inteiros](#11-conjunto-dos-numeros-naturais-e-inteiros)
    2. [Conjunto dos Números Racionais: Decimais Finitos e Dízimas Periódicas](#12-conjunto-dos-numeros-racionais-decimais-finitos-e-dizimas-periodicas)
    3. [Algoritmo da Divisão Euclidiana e Aritmética dos Restos](#13-algoritmo-da-divisao-euclidiana-e-aritmetica-dos-restos)
    4. [Teste 072](#Teste-072)
    5. [Teste 073](#Teste-073)
2. [Operações Aritméticas e Expressões Numéricas](#2-operacoes-aritmeticas-e-expressoes-numericas)
    1. [Ordem de Precedência das Operações e Delimitadores](#21-ordem-de-precedencia-das-operacoes-e-delimitadores)
    2. [Potenciação: Propriedades Operatórias e Notação Científica](#22-potenciacao-propriedades-operatorias-e-notacao-cientifica)
    3. [Teste 074](#Teste-074)
3. [Teoria dos Números: Divisibilidade, Primos, MMC e MDC](#3-teoria-dos-numeros-divisibilidade-primos-mmc-e-mdc)
    1. [Critérios de Divisibilidade Aplicados](#31-criterios-de-divisibilidade-aplicados)
    2. [Decomposição em Fatores Primos e Contagem de Divisores Positivos](#32-decomposicao-em-fatores-primos-e-contagem-de-divisores-positivos)
    3. [Mínimo Múltiplo Comum: Ciclos, Coincidências e Periodicidade](#33-minimo-multiplo-comum-ciclos-coincidencias-e-periodicidade)
    4. [Máximo Divisor Comum: Partições Equitativas e Lotes Máximos](#34-maximo-divisor-comum-particoes-equitativas-e-lotes-maximos)
    5. [Relação Fundamental entre MMC e MDC](#35-relacao-fundamental-entre-mmc-e-mdc)
    6. [Teste 075](#Teste-075)
    7. [Teste 076](#Teste-076)
    8. [Teste 077](#Teste-077)
4. [Álgebra Fracionária e Operações com Frações](#4-algebra-fracionaria-e-operacoes-com-fracoes)
    1. [Conceito, Tipologias e Equivalência de Frações](#41-conceito-tipologias-e-equivalencia-de-fracoes)
    2. [Operações Aritméticas com Frações](#42-operacoes-aritmeticas-com-fracoes)
    3. [Teste 078](#Teste-078)
5. [Modelagem e Resolução de Problemas no Padrão FCC](#5-modelagem-e-resolucao-de-problemas-no-padrao-fcc)
    1. [Problemas de Fração de Resto ou Cadeia Regressiva](#51-problemas-de-fracao-de-resto-ou-cadeia-regressiva)
    2. [Problemas de Trabalho Conjunto e Torneiras](#52-problemas-de-trabalho-conjunto-e-torneiras)
    3. [Problemas de Ciclos Periódicos e Padrões Sequenciais](#53-problemas-de-ciclos-periodicos-e-padroes-sequenciais)
    4. [Teste 079](#Teste-079)
    5. [Teste 080](#Teste-080)
    6. [Teste 081](#Teste-081)
6. [🌐 Fontes Oficiais e Referências Bibliográficas](#fontes-oficiais-e-referencias-bibliograficas)

---

## 1. Conjuntos Numéricos Fundamentais e Propriedades Estruturais

O estudo dos conjuntos numéricos estabelece as bases conceituais sobre as quais repousa toda a aritmética e o raciocínio quantitativo exigido nos concursos da área fiscal e de controle. A estruturação desses conjuntos desenvolveu-se historicamente para sanar impossibilidades operatórias verificadas em conjuntos mais restritos.

```mermaid
flowchart TD
    N["Naturais (N)<br/>0, 1, 2, 3..."] --> Z["Inteiros (Z)<br/>... -2, -1, 0, 1, 2..."]
    Z --> Q["Racionais (Q)<br/>a/b com b ≠ 0"]
    Q --> R["Reais (R)<br/>Q união Irracionais"]
```

### 1.1 Conjunto dos Números Naturais e Inteiros

* **Conjunto dos Números Naturais ($\mathbb{N}$):**
  $$\mathbb{N} = \{0, 1, 2, 3, 4, 5, \dots\}$$
  Representa o conjunto de contagem primitiva e ordenação de elementos discretos. É fechado sob as operações de adição e multiplicação (a soma ou produto de dois naturais é sempre um natural), mas falha no fechamento da subtração quando o minuendo é menor que o subtraendo ($3 - 8 \notin \mathbb{N}$).
* **Conjunto dos Números Inteiros ($\mathbb{Z}$):**
  $$\mathbb{Z} = \{\dots, -3, -2, -1, 0, 1, 2, 3, \dots\}$$
  Incorpora os opostos simétricos (negativos) aos números naturais, viabilizando o fechamento irrestrito da subtração. Na reta numérica, os inteiros organizam-se ordenadamente em torno da origem zero.
    * *Regra de Sinais na Multiplicação e Divisão:* Sinais iguais geram resultado positivo ($+ \cdot + = +$; $- \cdot - = +$); sinais contrários geram resultado negativo ($+ \cdot - = -$; $- \cdot + = -$).
    * *Adição de Inteiros com Sinais Opostos:* Conserva-se o sinal do termo de maior valor absoluto (módulo) e subtraem-se os valores: $(-15) + (+9) = -(15 - 9) = -6$.

### 1.2 Conjunto dos Números Racionais: Decimais Finitos e Dízimas Periódicas

O **Conjunto dos Números Racionais ($\mathbb{Q}$)** reúne todos os números suscetíveis de representação sob a forma de uma razão ou fração de dois números inteiros com denominador não nulo:
$$\mathbb{Q} = \left\{ x = \frac{a}{b} \ \middle| \ a \in \mathbb{Z}, \ b \in \mathbb{Z}, \ b \neq 0 \right\}$$

Todo número racional pode ser transcrito sob representação decimal, dividindo-se o numerador pelo denominador, resultando em apenas duas possibilidades formais:

1. **Decimais Exatos (ou Finitos):** Apresentam um número finito de casas decimais após a vírgula. Isso ocorre quando a fração irredutível $\frac{a}{b}$ possui um denominador $b$ decomposto exclusivamente em fatores primos iguais a $2$ e/ou $5$:
   $$0,75 = \frac{75}{100} = \frac{3}{4} \quad (4 = 2^2); \qquad 0,35 = \frac{35}{100} = \frac{7}{20} \quad (20 = 2^2 \times 5)$$
2. **Dízimas Periódicas:** Apresentam infinitas casas decimais que se repetem de maneira cíclica a partir de um bloco repetitivo denominado **período**:
    * **Dízima Periódica Simples:** O período principia imediatamente após a vírgula:
     $$0,\overline{4} = 0,444\dots = \frac{4}{9}; \qquad 0,\overline{27} = 0,2727\dots = \frac{27}{99} = \frac{3}{11}$$
    * **Dízima Periódica Composta:** Existe um segmento decimal que não se repete (o antiperíodo) posicionado entre a vírgula e o início do período:
     $$0,1\overline{6} = 0,1666\dots$$
    * **Regra Prática da Fração Geratriz para Dízimas Compostas:**
     $$\text{Fração Geratriz} = \frac{(\text{Antiperíodo seguido do Período}) - (\text{Antiperíodo})}{(\text{tantos 9 quantos forem os dígitos do período}) \times 10^{(\text{dígitos do antiperíodo})}}$$
     Exemplo para $0,1\overline{6}$:
     $$0,1\overline{6} = \frac{16 - 1}{90} = \frac{15}{90} = \frac{1}{6}$$

### 1.3 Algoritmo da Divisão Euclidiana e Aritmética dos Restos

Para quaisquer dois números inteiros $D$ (dividendo) e $d$ (divisor não nulo), existem inteiros únicos $q$ (quociente) e $r$ (resto) tais que:
$$D = d \cdot q + r, \quad \text{onde } 0 \le r < |d|$$

Propriedades críticas da divisão inteira:

* O resto $r$ é **estritamente não negativo** e **menor que o divisor** ($0 \le r \le d - 1$).
* O **resto máximo possível** na divisão por um divisor $d$ é sempre igual a $d - 1$. Se um problema indagar o resto máximo obtido na divisão por $15$, esse valor é inequivocamente $15 - 1 = 14$.

> 🚨 **ALERTA DE PROVA / PEGADINHA FCC:** Em problemas que envolvem ciclos e restos de divisão (dias da semana, rodízio de equipes, posições de algarismos), o divisor corresponde ao tamanho do ciclo. Se o resto for zero, significa que a divisão foi exata e que a posição procurada corresponde rigorosamente ao **último elemento** do ciclo periódico, e não ao primeiro!

---

### Teste 072
**(FCC – TRT-23 – Analista Judiciário)**  
Considere a expressão numérica $E = 0{,}333... + \frac{1}{6} - 0{,}25$. O valor exato de $E$ expresso sob a forma de fração irredutível é igual a:

* **A)** $\frac{1}{4}$
* **B)** $\frac{1}{3}$
* **C)** $\frac{1}{2}$
* **D)** $\frac{5}{12}$
* **E)** $\frac{7}{12}$


---

> **Comentário Detalhado:**
>
> - **1º Passo:** Converter os números decimais e a dízima periódica em frações ordinárias:  
>   - A dízima periódica simples $0{,}333...$ tem como fração geratriz $\frac{3}{9} = \frac{1}{3}$.  
>   - O decimal exato $0{,}25$ corresponde a $\frac{25}{100} = \frac{1}{4}$.  
> - **2º Passo:** Substituir os valores na expressão:  
>   $$E = \frac{1}{3} + \frac{1}{6} - \frac{1}{4}$$  
> - **3º Passo:** Obter o MMC dos denominadores $3, 6, 4$:  
>   $MMC(3, 6, 4) = 12$.  
> - **4º Passo:** Reduzir ao mesmo denominador e efetuar as operações:  
>   $$E = \frac{4}{12} + \frac{2}{12} - \frac{3}{12} = \frac{4 + 2 - 3}{12} = \frac{3}{12}$$  
> - **5º Passo:** Simplificar a fração obtida:  
>   $$\frac{3}{12} = \frac{1}{4}$$  
> - **Conclusão:** O resultado é $\frac{1}{4}$ (Alternativa A).
>
> **Gabarito: A**

---

### Teste 073
**(FCC – TCE-GO – Auditor de Controle Externo)**  
Considere a sequência infinita de números formados pela repetição cíclica dos algarismos do número 74582:
$$7, 4, 5, 8, 2, 7, 4, 5, 8, 2, 7, 4, 5, 8, 2, \dots$$
O algarismo que ocupa a 2027ª posição nessa sequência e o resto da divisão de 2027 por 5 são, respectivamente:

* **A)** 5 e 2
* **B)** 4 e 2
* **C)** 7 e 1
* **D)** 5 e 3
* **E)** 8 e 4


---

> **Comentário Detalhado:**
> Análise do padrão de periodicidade cíclica:
>
> 1. O ciclo básico é composto por 5 algarismos ordenados:
>     - 1º elemento: 7 (posições que deixam resto 1 na divisão por 5)
>     - 2º elemento: 4 (posições que deixam resto 2 na divisão por 5)
>     - 3º elemento: 5 (posições que deixam resto 3 na divisão por 5)
>     - 4º elemento: 8 (posições que deixam resto 4 na divisão por 5)
>     - 5º elemento: 2 (posições que deixam resto 0 na divisão por 5, múltiplos exatos de 5)
>
> 2. Pelo algoritmo da divisão euclidiana, dividimos a posição 2027 pelo comprimento do período (5):
>    $$2027 = 5 \times 405 + 2$$
>     - O quociente 405 indica que o ciclo completo de 5 algarismos é repetido integralmente 405 vezes.
>     - O **resto é 2**.
>
> 3. Como o resto da divisão é 2, o algarismo que ocupa a 2027ª posição corresponde ao segundo elemento do bloco cíclico padrão $(7, \mathbf{4}, 5, 8, 2)$, que é o algarismo **4**.
> 4. Logo, o algarismo é **4** e o resto é **2**.
>
> Análise das alternativas:
>
> - **A)** Incorreta. Indica o algarismo 5, que corresponderia a resto 3.
> - **B)** Correta. O algarismo na posição 2027 é o 2º elemento do ciclo (**4**) e o resto da divisão euclidiana de 2027 por 5 é **2**.
> - **C)** Incorreta. Aponta resto 1 e algarismo 7.
> - **D)** Incorreta. Afirma erroneamente que o resto de 2027 por 5 é 3.
> - **E)** Incorreta. Aponta o algarismo 8 e resto 4.
> 
> **Gabarito: B**

---

## 2. Operações Aritméticas e Expressões Numéricas

### 2.1 Ordem de Precedência das Operações e Delimitadores

A avaliação de expressões aritméticas complexas exige obediência à ordem universal de precedência matemática (mnemônico PEMDAS / PDMAS):

1. **Ordem dos Delimitadores de Escopo (de dentro para fora):**
   1º) Parênteses $( \ )$;
   2º) Colchetes $[ \ ]$;
   3º) Chaves $\{ \ \}$.
2. **Ordem Hierárquica das Operações:**
   1º) **Potenciações e Radiciações** (na ordem em que aparecem da esquerda para a direita);
   2º) **Multiplicações e Divisões** (com estrita igualdade de precedência, calculando-se o que vier primeiro da esquerda para a direita);
   3º) **Adições e Subtrações** (igualmente da esquerda para a direita).

> 📌 **NOTA EXPLICATIVA / ERRO COMUM DE DIVISÃO E MULTIPLICAÇÃO:** Na expressão $12 \div 3 \times 2$, a multiplicação **não** tem prioridade sobre a divisão! Ambas possuem a mesma hierarquia; resolve-se da esquerda para a direita: $12 \div 3 = 4$, e $4 \times 2 = 8$ (o cálculo incorreto $12 \div 6 = 2$ é uma armadilha frequente).

### 2.2 Potenciação: Propriedades Operatórias e Notação Científica

A potenciação traduz o produto de fatores idênticos repetidos ($a^n = \underbrace{a \cdot a \cdots a}_{n \text{ vezes}}$). Suas propriedades fundamentais incluem:

* Produto de potências de mesma base: $a^m \cdot a^n = a^{m+n}$
* Divisão de potências de mesma base: $\frac{a^m}{a^n} = a^{m-n} \quad (a \neq 0)$
* Potência de potência: $(a^m)^n = a^{m \cdot n}$
* Potência de produto: $(a \cdot b)^n = a^n \cdot b^n$
* Expoente nulo: $a^0 = 1 \quad (a \neq 0)$
* Expoente negativo: $a^{-n} = \frac{1}{a^n} = \left(\frac{1}{a}\right)^n \quad (a \neq 0)$
* Expoente fracionário (Radiciação): $a^{\frac{m}{n}} = \sqrt[n]{a^m}$

---

### Teste 074
**(FCC – TCE-GO – Analista de Controle Externo)**  
O valor numérico da expressão aritmética $K = \frac{2^{20} + 2^{18}}{2^{19} - 2^{17}}$ é igual a:

* **A)** $\frac{5}{3}$
* **B)** $\frac{10}{3}$
* **C)** $2$
* **D)** $4$
* **E)** $\frac{5}{6}$


---

> **Comentário Detalhado:**
>
> - **Método de Resolução (Fatoração por Colocação em Evidência):** Em expressões com potências de mesma base com expoentes elevados, a estratégia padrão da FCC consiste em colocar em evidência a potência de menor expoente no numerador e no denominador.  
> - **No numerador:** $2^{20} + 2^{18} = 2^{18} \cdot (2^2 + 1) = 2^{18} \cdot (4 + 1) = 2^{18} \cdot 5$.  
> - **No denominador:** $2^{19} - 2^{17} = 2^{17} \cdot (2^2 - 1) = 2^{17} \cdot (4 - 1) = 2^{17} \cdot 3$.  
> - **Dividindo numerador por denominador:**  
>   $$K = \frac{2^{18} \cdot 5}{2^{17} \cdot 3} = \frac{2^{18}}{2^{17}} \cdot \frac{5}{3} = 2^{18-17} \cdot \frac{5}{3} = 2^1 \cdot \frac{5}{3} = \frac{10}{3}$$  
> - **Conclusão:** O valor numérico de $K$ é exatamente $\frac{10}{3}$ (Alternativa B).
>
> **Gabarito: B**

---

## 3. Teoria dos Números: Divisibilidade, Primos, MMC e MDC

A teoria dos números fornece o ferramental algébrico para lidar com divisões inteiras, periodicidade de escalas e otimização de lotes em logística e auditoria.

### 3.1 Critérios de Divisibilidade Aplicados

Permitem verificar se um número inteiro $N$ é divisível por outro sem executar a divisão longa:

* **Por 2:** O último algarismo da direita é par ($0, 2, 4, 6, 8$).
* **Por 3:** A soma dos valores absolutos dos seus algarismos é um múltiplo de 3 (ex.: $7.458 \rightarrow 7 + 4 + 5 + 8 = 24$, que é divisível por 3).
* **Por 4:** O número formado pelos dois últimos algarismos é divisível por 4 ou termina em $00$.
* **Por 5:** O último algarismo é $0$ ou $5$.
* **Por 6:** É simultaneamente divisível por 2 (par) e por 3 (soma dos algarismos múltipla de 3).
* **Por 8:** O número formado pelos três últimos algarismos é divisível por 8 ou termina em $000$.
* **Por 9:** A soma dos seus algarismos resulta em um múltiplo de 9.
* **Por 10:** O último algarismo é obrigatoriamente $0$.
* **Por 11:** A diferença entre a soma dos algarismos de ordem ímpar e a soma dos algarismos de ordem par é múltipla de 11 (incluindo o zero).

### 3.2 Decomposição em Fatores Primos e Contagem de Divisores Positivos

Pelo Teorema Fundamental da Aritmética, qualquer número natural maior que 1 pode ser decomposto de forma única (a menos da ordem dos fatores) em um produto de potências de números primos:
$$N = p_1^{\alpha} \cdot p_2^{\beta} \cdot p_3^{\gamma} \cdots p_k^{\omega}$$

#### Quantidade Total de Divisores Positivos:
O número total de divisores inteiros positivos de $N$ é obtido somando-se uma unidade a cada expoente da fatoração canônica e multiplicando-se os resultados:
$$Q(N) = (\alpha + 1)(\beta + 1)(\gamma + 1)\cdots(\omega + 1)$$
*Exemplo:* Para encontrar quantos divisores possui o número 360:
$$360 = 2^3 \cdot 3^2 \cdot 5^1 \implies Q(360) = (3 + 1)(2 + 1)(1 + 1) = 4 \times 3 \times 2 = 24 \text{ divisores}$$

### 3.3 Mínimo Múltiplo Comum: Ciclos, Coincidências e Periodicidade

O **Mínimo Múltiplo Comum (MMC)** entre dois ou mais inteiros é o menor número natural não nulo que é divisível simultaneamente por todos eles.

* **Cálculo Prático:** Decompõem-se os números em fatores primos; o MMC é o produto de **todos os fatores primos comuns e não comuns, elevados aos seus maiores expoentes**.

```mermaid
flowchart LR
    A["Identificação do Problema"] --> B{"Qual é a ideia do enunciado?"}
    B -->|"Tempo / Encontro / Ciclos"| C["Calcular MMC<br/>Fatores comuns e não comuns<br/>Maiores expoentes"]
    B -->|"Repartir / Cortar / Maior lote"| D["Calcular MDC<br/>Fatores comuns<br/>Menores expoentes"]
```

> 💡 **DICA DE IDENTIFICAÇÃO (MMC NA FCC):** O problema exige MMC sempre que veicular ideias de **coincidência temporal futura**, **reencontro de eventos periódicos**, **ciclos de rondas/inspeções** ou questões que indaguem: *"quando voltarão a se encontrar simultaneamente?"*.

### 3.4 Máximo Divisor Comum: Partições Equitativas e Lotes Máximos

O **Máximo Divisor Comum (MDC)** é o maior número inteiro capaz de dividir exatamente todos os números dados, sem deixar resto.

* **Cálculo Prático:** É o produto **apenas dos fatores primos comuns a todos os números, elevados aos seus menores expoentes**.

| Característica | Mínimo Múltiplo Comum (MMC) | Máximo Divisor Comum (MDC) |
|---|---|---|
| **Ideia central** | Coincidência, repetição, sincronia periódica | Divisão, partição equitativa, corte em partes iguais |
| **Palavras-chave** | "Quando voltarão a se encontrar?", "periodicidade", "ciclos", "simultaneamente" | "Maior tamanho possível", "sem sobras", "dividir igualmente", "menor número de caixas" |
| **Fatoração em primos** | Fatores comuns e não comuns com os **maiores expoentes** | Apenas fatores **comuns** com os **menores expoentes** |

> 🚨 **ALERTA DE PROVA / PEGADINHA CLÁSSICA DO MDC:** Em problemas de particionamento (como arquivar pastas em caixas de maior tamanho possível), o cálculo do MDC fornece a **capacidade de cada caixa**, e **não a quantidade total de caixas**! Para achar a quantidade de caixas, deve-se somar a divisão de cada lote pelo valor do MDC encontrado.

### 3.5 Relação Fundamental entre MMC e MDC

Para quaisquer dois números inteiros positivos $a$ e $b$, o produto entre o seu MMC e o seu MDC é rigorosamente igual ao produto entre os próprios números:
$$\text{MMC}(a, b) \times \text{MDC}(a, b) = a \times b$$

---

### Teste 075
**(FCC – METRÔ-SP – Analista)**  
O número de divisores naturais positivos do número inteiro $N = 360$ é igual a:

* **A)** $18$
* **B)** $24$
* **C)** $20$
* **D)** $30$
* **E)** $12$


---

> **Comentário Detalhado:**
>
> - **Regra da Quantidade de Divisores Positivos:** Para determinar o número de divisores positivos de um inteiro $N$, realiza-se a decomposição canônica em fatores primos:  
>   $$N = p_1^{\alpha_1} \cdot p_2^{\alpha_2} \cdot ... \cdot p_k^{\alpha_k}$$  
>   A quantidade total de divisores positivos é dada pelo produto dos expoentes acrescidos de uma unidade:  
>   $$D(N) = (\alpha_1 + 1) \cdot (\alpha_2 + 1) \cdot ... \cdot (\alpha_k + 1)$$  
> - **Fatoração de 360:**  
>   $360 = 36 \times 10 = (2^2 \cdot 3^2) \cdot (2 \cdot 5) = 2^3 \cdot 3^2 \cdot 5^1$.  
> - **Cálculo dos divisores:**  
>   - Expoente da base 2: $\alpha_1 = 3 \rightarrow (3 + 1) = 4$  
>   - Expoente da base 3: $\alpha_2 = 2 \rightarrow (2 + 1) = 3$  
>   - Expoente da base 5: $\alpha_3 = 1 \rightarrow (1 + 1) = 2$  
>   $$D(360) = 4 \times 3 \times 2 = 24$$  
> - **Conclusão:** O número 360 possui exatamente 24 divisores naturais positivos (Alternativa B).
>
> **Gabarito: B**

---

### Teste 076
**(FCC – Auditor Fiscal da Receita – Adaptada)**  
Três equipes de fiscalização do Tribunal de Contas realizam auditorias periódicas em municípios do interior goiano. A equipe Alfa realiza auditorias a cada 12 dias; a equipe Beta, a cada 18 dias; e a equipe Gama, a cada 20 dias. No dia 1º de março de determinado ano não bissexto, as três equipes iniciaram suas inspeções simultaneamente.

O número de dias que decorrerão até que as três equipes voltem a iniciar suas auditorias no mesmo dia é:

* **A)** 60 dias
* **B)** 120 dias
* **C)** 180 dias
* **D)** 240 dias
* **E)** 360 dias


---

> **Comentário Detalhado:**
> O problema demanda o cálculo do menor intervalo de tempo em que eventos com frequências periódicas distintas coincidem simultaneamente no futuro, o que se resolve determinando o **Mínimo Múltiplo Comum (MMC)** entre 12, 18 e 20.
> Decompondo os números em fatores primos simultâneos:
>
> - $12 = 2^2 \times 3$
> - $18 = 2 \times 3^2$
> - $20 = 2^2 \times 5$
> 
> O MMC reúne todos os fatores primos presentes (2, 3 e 5), elevados aos seus maiores expoentes:
> $$\text{MMC}(12, 18, 20) = 2^2 \times 3^2 \times 5 = 4 \times 9 \times 5 = 180 \text{ dias}$$
> 
> Análise individual das alternativas:
>
> - **A)** Incorreta. 60 é múltiplo comum de 12 e 20, mas não é divisível por 18 ($60 \div 18 \approx 3,33$).
> - **B)** Incorreta. 120 é divisível por 12 e por 20, mas não divide exatamente por 18 ($120 \div 18 \approx 6,66$).
> - **C)** Correta. 180 é o menor número natural simultaneamente divisível por 12 ($180/12 = 15$), 18 ($180/18 = 10$) e 20 ($180/20 = 9$).
> - **D)** Incorreta. 240 não é divisível por 18 ($240 \div 18 \approx 13,33$).
> - **E)** Incorreta. 360 é um múltiplo comum posterior, mas a questão indaga expressamente quando voltarão a coincidir (primeiro reencontro após 1º de março).
> 
> **Gabarito: C**

---

### Teste 077
**(FCC – TCE-PI – Técnico de Controle Externo)**  
Uma coordenadoria administrativa do TCE-GO precisa arquivar 168 pastas de auditoria do tipo A, 216 pastas do tipo B e 264 pastas do tipo C em caixas organizadoras. Todas as caixas devem conter o mesmo número de pastas, sendo que cada caixa conterá pastas de um único tipo, e o número de pastas por caixa deve ser o **maior possível**, sem que sobre nenhuma pasta avulsa.

Nessas condições, o **número total de caixas organizadoras** necessárias para arquivar todas as pastas é:

* **A)** 24
* **B)** 27
* **C)** 32
* **D)** 36
* **E)** 48


---

> **Comentário Detalhado:**
> A resolução compõe-se de duas etapas lógicas:
>
> 1. Para que as caixas tenham capacidade idêntica, comportem apenas pastas do mesmo tipo e o número de pastas em cada caixa seja o **maior possível**, a capacidade de cada caixa deve corresponder ao **Máximo Divisor Comum (MDC)** entre 168, 216 e 264:
>     - $168 = 2^3 \times 3 \times 7$
>     - $216 = 2^3 \times 3^3$
>     - $264 = 2^3 \times 3 \times 11$
>     - $\text{MDC}(168, 216, 264) = 2^3 \times 3^1 = 8 \times 3 = 24 \text{ pastas por caixa}$.
>
> 2. O enunciado indaga expressamente o **número de caixas** demandado (e não a quantidade de pastas por caixa):
>     - Caixas para o lote A: $168 \div 24 = 7 \text{ caixas}$
>     - Caixas para o lote B: $216 \div 24 = 9 \text{ caixas}$
>     - Caixas para o lote C: $264 \div 24 = 11 \text{ caixas}$
>     - Total de caixas: $7 + 9 + 11 = 27 \text{ caixas}$.
>
> Análise das alternativas:
>
> - **A)** Incorreta. 24 é a capacidade unitária de pastas em cada caixa (o valor do MDC), armadilha clássica da FCC para o candidato desatento ao comando da questão.
> - **B)** Correta. 27 caixas no total ($7 + 9 + 11$).
> - **C)** Incorreta. Com 32 caixas, o total de 648 pastas ($168 + 216 + 264$) exigiria $648 \div 32 = 20{,}25$ pastas por caixa (valor não inteiro), o que é inviável.
> - **D)** Incorreta. Com 36 caixas, haveria $648 \div 36 = 18$ pastas por caixa; porém 18 não divide 168 ($168 \div 18 \approx 9{,}33$), o que deixaria pastas avulsas.
> - **E)** Incorreta. Com 48 caixas, haveria $648 \div 48 = 13{,}5$ pastas por caixa (valor não inteiro), o que é inviável.
> 
> **Gabarito: B**

---

## 4. Álgebra Fracionária e Operações com Frações

Uma fração $\frac{a}{b}$ representa uma divisão indicada onde o denominador $b$ assinala em quantas partes iguais a unidade inteira foi particionada, e o numerador $a$ indica quantas dessas partes foram tomadas.

### 4.1 Conceito, Tipologias e Equivalência de Frações

* **Fração Própria:** O numerador é menor que o denominador ($a < b$). Representa um valor estritamente menor que a unidade inteira ($\frac{2}{5}, \frac{7}{9}$).
* **Fração Imprópria:** O numerador é maior ou igual ao denominador ($a \ge b$). Representa um valor maior ou igual à unidade inteira ($\frac{7}{4}, \frac{11}{3}$). Podem ser convertidas em **números mistos**: $\frac{7}{4} = 1 \frac{3}{4}$.
* **Fração Aparente:** O numerador é múltiplo exato do denominador, consubstanciando um número inteiro disfarçado ($\frac{12}{3} = 4, \frac{35}{7} = 5$).
* **Frações Equivalentes e Irredutibilidade:** Duas frações são equivalentes quando representam a mesma grandeza fracionária ($\frac{2}{3} = \frac{4}{6} = \frac{10}{15}$). Obtém-se a fração irredutível simplificando numerador e denominador pelo seu MDC.

### 4.2 Operações Aritméticas com Frações

1. **Adição e Subtração:**
    * Com denominadores iguais: conserva-se o denominador comum e operam-se os numeradores: $\frac{a}{c} \pm \frac{b}{c} = \frac{a \pm b}{c}$.
    * Com denominadores distintos: reduz-se ao mesmo denominador mediante o cálculo do MMC dos denominadores:
     $$\frac{a}{b} \pm \frac{c}{d} = \frac{\left(\frac{\text{MMC}}{b} \cdot a\right) \pm \left(\frac{\text{MMC}}{d} \cdot c\right)}{\text{MMC}(b, d)}$$
2. **Multiplicação:** Multiplicam-se os numeradores entre si e os denominadores entre si:
   $$\frac{a}{b} \times \frac{c}{d} = \frac{a \cdot c}{b \cdot d}$$
   A preposição "de" na matemática denota multiplicação: $\frac{2}{3}$ *de* $\frac{4}{5} = \frac{2}{3} \times \frac{4}{5} = \frac{8}{15}$.
3. **Divisão:** Conserva-se a primeira fração e multiplica-se pela fração inversa da segunda:
   $$\frac{a}{b} \div \frac{c}{d} = \frac{a}{b} \times \frac{d}{c} = \frac{a \cdot d}{b \cdot c} \quad (c, d \neq 0)$$

---

### Teste 078
**(FCC – TRT-14 – Analista Judiciário)**  
Um servidor do tribunal recebeu determinado lote de processos para instruir. No primeiro dia, analisou $\frac{2}{5}$ do total de processos; no segundo dia, analisou $\frac{1}{3}$ do que havia sobrado; e, no terceiro dia, concluiu os últimos $24$ processos restantes. O número total de processos contidos no lote original era igual a:

* **A)** $50$
* **B)** $60$
* **C)** $75$
* **D)** $80$
* **E)** $90$


---

> **Comentário Detalhado:**
>
> - **Método da Cadeia Regressiva (Fração de Resto):**  
>   - Seja $P$ o total original de processos.  
>   - **Dia 1:** O servidor instruiu $\frac{2}{5}P$.  
>     Restante após o dia 1: $1 - \frac{2}{5} = \frac{3}{5}P$.  
>   - **Dia 2:** O servidor instruiu $\frac{1}{3}$ do restante:  
>     $$\frac{1}{3} \times \frac{3}{5}P = \frac{1}{5}P$$  
>     Fração total instruída nos dois primeiros dias: $\frac{2}{5}P + \frac{1}{5}P = \frac{3}{5}P$.  
>     Restante final para o dia 3: $1 - \frac{3}{5} = \frac{2}{5}P$.  
>   - **Dia 3:** Esse restante final corresponde a 24 processos:  
>     $$\frac{2}{5}P = 24 \implies 2P = 24 \times 5 = 120 \implies P = \frac{120}{2} = 60$$  
> - **Conferência:** $60 \times \frac{2}{5} = 24$ no 1º dia (sobram 36); $\frac{1}{3} \times 36 = 12$ no 2º dia (sobram 24); $24$ no 3º dia. Perfeito.
>
> **Gabarito: B**

---

## 5. Modelagem e Resolução de Problemas no Padrão FCC

### 5.1 Problemas de Fração de Resto ou Cadeia Regressiva

Problemas clássicos da FCC narram um agente que consome uma fração de um montante total no primeiro dia, gasta uma fração **do restante** no segundo dia e encerra com uma quantia fixa final:

* Se no passo 1 gasta-se $\frac{1}{3}$ do total $T$, sobra:
  $$\text{Resto}_1 = 1 - \frac{1}{3} = \frac{2}{3}T$$
* Se no passo 2 gasta-se $\frac{3}{5}$ **do que sobrou**, o gasto é $\frac{3}{5} \times \frac{2}{3}T = \frac{6}{15}T = \frac{2}{5}T$.
* A parcela que resta ao final é o complementar de $\frac{3}{5}$ sobre o restante prévio:
  $$\text{Resto Final} = \left(1 - \frac{3}{5}\right) \times \frac{2}{3}T = \frac{2}{5} \times \frac{2}{3}T = \frac{4}{15}T$$
* Igualando essa fração ao valor numérico remanescente dado no enunciado, descobre-se o total $T$ por equação direta.

### 5.2 Problemas de Trabalho Conjunto e Torneiras

Quando dois agentes executam uma mesma tarefa de forma cooperativa em ritmos constantes, somam-se as suas taxas unitárias horárias de produtividade:
$$\text{Taxa Conjunta} = \frac{1}{T_{\text{junto}}} = \frac{1}{t_1} + \frac{1}{t_2} + \dots - \frac{1}{t_{\text{ralo}}}$$
Para o caso específico de dois agentes que levam tempos individuais $t_1$ e $t_2$:
$$T = \frac{t_1 \cdot t_2}{t_1 + t_2}$$

*Atenção à Conversão de Tempo:* Se o resultado da divisão em horas for decimal, como $2,4\text{ horas}$, a parte inteira corresponde a $2\text{ horas}$ e a parte decimal $0,4$ deve ser multiplicada por $60\text{ minutos}$ ($0,4 \times 60 = 24\text{ minutos}$). Logo, $2,4\text{ h} = 2\text{ horas e } 24\text{ minutos}$ (e nunca 2h40min!).

### 5.3 Problemas de Ciclos Periódicos e Padrões Sequenciais

Em problemas que constroem sequências infinitas repetindo ciclicamente um conjunto finito de $k$ elementos ($x_1, x_2, \dots, x_k$):

1. Toma-se o número da posição requerida $P$;
2. Divide-se $P$ pelo tamanho do ciclo $k$, obtendo o quociente $q$ e o resto $r$ ($P = k \cdot q + r$);
3. **Se o resto $r > 0$:** O termo procurado é exatamente o $r$-ésimo elemento do ciclo padrão;
4. **Se o resto $r = 0$:** O termo procurado é o último elemento do ciclo (o $k$-ésimo elemento).

---

### Teste 079
**(FCC – TCE-GO – Analista de Controle Externo)**  
Um auditor do TCE-GO foi designado para realizar a conferência documental de uma amostra de processos de licitação municipal. No primeiro dia de trabalho, o auditor analisou $\frac{1}{3}$ do total de processos da amostra. No segundo dia, analisou $\frac{3}{5}$ dos processos **restantes**. No terceiro dia, finalizou a conferência analisando os últimos 48 processos.

O número total de processos contidos originalmente nessa amostra era:

* **A)** 150
* **B)** 160
* **C)** 180
* **D)** 200
* **E)** 240


---

> **Comentário Detalhado:**
> Modelando o problema algebricamente:
>
> - Seja $T$ a quantidade total de processos da amostra.
> - **No Dia 1:** O auditor executou $\frac{1}{3}T$. A quantidade remanescente após o primeiro dia é:
>   $$\text{Resto}_1 = T - \frac{1}{3}T = \frac{2}{3}T$$
> - **No Dia 2:** O auditor analisou $\frac{3}{5}$ do que restava. Logo, sobrou $\frac{2}{5}$ daquele montante restante:
>   $$\text{Resto Final} = \left(1 - \frac{3}{5}\right) \times \text{Resto}_1 = \frac{2}{5} \times \left(\frac{2}{3}T\right) = \frac{4}{15}T$$
> - **No Dia 3:** O enunciado informa que o resto final totalizou 48 processos. Igualando os valores:
>   $$\frac{4}{15}T = 48 \implies 4T = 48 \times 15 \implies 4T = 720 \implies T = \frac{720}{4} = 180$$
>
> Análise individual das alternativas:
>
> - **A)** Incorreta. Se o total fosse 150, o resto final seria $\frac{4}{15} \times 150 = 40$ processos, divergindo dos 48 informados.
> - **B)** Incorreta. Com $T = 160$, o resto final seria $\frac{4}{15} \times 160 \approx 42{,}7$ processos (valor não inteiro), divergindo dos 48 informados.
> - **C)** Correta. Com $T = 180$: no dia 1 são analisados 60 processos (restando 120); no dia 2 são analisados $\frac{3}{5} \times 120 = 72$ processos (restando $120 - 72 = 48$); no dia 3 são analisados exatamente os 48 processos finais.
> - **D)** Incorreta. Com $T = 200$, o resto final seria $\frac{4}{15} \times 200 \approx 53{,}3$ processos (valor não inteiro), divergindo dos 48 informados. (Erro típico: aplicar $\frac{3}{5}$ sobre o total geral em vez de sobre o restante, o que daria $1 - \frac{1}{3} - \frac{3}{5} = \frac{1}{15}$ e $T = 720$, valor que nem figura entre as alternativas.)
> - **E)** Incorreta. Com $T = 240$, o resto final seria $\frac{4}{15} \times 240 = 64$ processos, divergindo dos 48 informados.
> 
> **Gabarito: C**

---

### Teste 080
**(FCC – TRT – Técnico Judiciário)**  
Dois técnicos de controle externo, Bruno e Camila, foram encarregados de digitalizar e indexar um acervo de processos arquivados. Trabalhando sozinho, Bruno realiza todo o serviço em 6 horas. Camila, trabalhando sozinha, executa o mesmo serviço em 4 horas. 

Se Bruno e Camila trabalharem juntos, no mesmo ritmo de produtividade constante, o tempo necessário para digitalizar e indexar todo o acervo será de:

* **A)** 2 horas e 12 minutos
* **B)** 2 horas e 24 minutos
* **C)** 2 horas e 30 minutos
* **D)** 2 horas e 40 minutos
* **E)** 5 horas


---

> **Comentário Detalhado:**
> Problema clássico de trabalho cooperativo e soma de taxas operatórias:
>
> 1. Taxa horária de Bruno: $v_B = \frac{1}{6}$ do serviço por hora.
> 2. Taxa horária de Camila: $v_C = \frac{1}{4}$ do serviço por hora.
> 3. Taxa conjunta trabalhando juntos:
>    $$v_{\text{juntos}} = \frac{1}{6} + \frac{1}{4} = \frac{2 + 3}{12} = \frac{5}{12} \text{ do serviço por hora}$$
> 4. Tempo total necessário ($T$):
>    $$T = \frac{1}{v_{\text{juntos}}} = \frac{12}{5} \text{ horas} = 2,4 \text{ horas}$$
> 5. Conversão da fração horária decimal:
>    A parte inteira é de 2 horas. A parte decimal corresponde a:
>    $$0,4 \text{ hora} = 0,4 \times 60 \text{ minutos} = 24 \text{ minutos}$$
>    Portanto, o tempo total é de **2 horas e 24 minutos**.
>
> Análise das alternativas:
>
> - **A)** Incorreta. Erra ao converter a parte decimal tomando $0,2$ em vez de $0,4$.
> - **B)** Correta. $2,4 \text{ horas} = 2 \text{ horas e } 24 \text{ minutos}$.
> - **C)** Incorreta. Resulta da confusão de achar que 2,4h equivale à média de tempo ou 2h30min.
> - **D)** Incorreta. Erro crasso de interpretar o dígito 4 do número decimal 2,4 como 40 minutos (a contagem do tempo é sexagesimal, base 60, e não decimal).
> - **E)** Incorreta. Média aritmética ingênua dos tempos individuais ($\frac{6 + 4}{2} = 5 \text{ horas}$), o que contraria o fato óbvio de que duas pessoas trabalhando juntas terminam a tarefa em tempo menor que o trabalhador mais rápido isoladamente.
> 
> **Gabarito: B**

---

### Teste 081
**(FCC – TCE-PI – Auditor de Controle Externo)**  
Considere a sequência infinita de letras:  
$$T, C, E, G, O, I, A, S, T, C, E, G, O, I, A, S, T, C, E, ...$$  
formada pela repetição contínua do bloco de palavras *"TCEGOIAS"*. A letra que ocupa a 2027ª posição dessa sequência é:

* **A)** T
* **B)** C
* **C)** E
* **D)** G
* **E)** S


---

> **Comentário Detalhado:**
>
> - **Método dos Ciclos Periódicos e Aritmética dos Restos:**  
>   - O bloco padrão repetitivo é *"T, C, E, G, O, I, A, S"*.  
>   - Contagem do período: O bloco possui exatamente **8 letras**.  
>   - Para determinar o elemento na posição $N = 2027$, divide-se $2027$ pelo tamanho do ciclo ($8$) e analisa-se o resto:  
>     $$2027 = 8 \times 253 + 3$$  
>     (pois $8 \times 253 = 2024$, e $2027 - 2024 = 3$).  
>   - O quociente $253$ indica que o ciclo de 8 letras completou-se exatamente 253 vezes.  
>   - O resto $3$ indica que a letra procurada é a **3ª letra** do bloco padrão.  
> - **Localização no bloco:**  
>   1ª = T, 2ª = C, **3ª = E**.  
> - **Conclusão:** A letra na 2027ª posição é a letra **E** (Alternativa C).
>
> **Gabarito: C**

---

## 🌐 Fontes Oficiais e Referências Bibliográficas

* [Khan Academy Brasil - Aritmética e Operações Fundamentais](https://pt.khanacademy.org/math/arithmetic) - Operações fundamentais com inteiros e números racionais, potenciação e expressões numéricas.
* [Khan Academy Brasil - Frações e Operações Fracionárias](https://pt.khanacademy.org/math/arithmetic/fraction-arithmetic) - Adição, subtração, multiplicação, divisão e simplificação de frações ordinárias.
* [Khan Academy Brasil - Pré-Álgebra: Fatores, Primos e Divisibilidade](https://pt.khanacademy.org/math/pre-algebra) - Critérios de divisibilidade, números primos, fatoração e cálculo de MMC e MDC.
* [OBMEP / IMPA - Apostila 1 do PIC: Iniciação à Aritmética](https://www.obmep.org.br/docs/apostila1.pdf) - Teoria elementar dos números, divisibilidade, algoritmo da divisão de Euclides e propriedades de restos (Prof. Abramo Hefez).
* [OBMEP / IMPA - Apostila Temática: Aritmética](https://www.obmep.org.br/docs/aritmetica.pdf) - Módulo aprofundado com demonstrações teóricas e problemas clássicos de aritmética e números inteiros.
* ALENCAR FILHO, Edgard de. **Iniciação à Lógica Matemática**. São Paulo: Nobel, 2002. (Cap. 1 e 2 - Fundamentos e Operações Básicas).
* HEFEZ, Abramo. **Elementos de Aritmética**. 2. ed. Rio de Janeiro: SBM, 2011. (Cap. 2 - Divisibilidade e Algoritmo de Euclides).
* IEZZI, Gelson; MURAKAMI, Carlos. **Fundamentos de Matemática Elementar, Volume 1: Conjuntos e Funções**. 9. ed. São Paulo: Atual, 2013. (Cap. 1 a 3 - Conjuntos Numéricos Fundamentais).
