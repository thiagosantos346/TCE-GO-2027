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
**(FGV – TCE-SC – Auditor Fiscal de Controle Externo Administracao – 2026)**
Gabriel fez um sorteio dos seis primeiros números naturais e obteve a sequência: 6 3 5 1 4 2 Essa sequência poderá ser alterada mediante uma sucessão de movimentos. Realizar um movimento significa escolher um dos números da sequência e fazê-lo pular o número que está imediatamente à sua direita. A partir da sequência dada, após 𝑛 movimentos, Gabriel obteve esta sequência natural: 1 2 3 4 5 6. O menor valor possível de 𝑛 é

* **A)** 10.
* **B)** 11.
* **C)** 12.
* **D)** 13.
* **E)** 14.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "10". De acordo com a teoria estudada em *1.2 Conjunto dos Números Racionais: Decimais Finitos e Dízimas Periódicas*, dízima Periódica Simples: O período principia imediatamente após a vírgula.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "11". De acordo com a teoria estudada em *3.2 Decomposição em Fatores Primos e Contagem de Divisores Positivos*, pelo Teorema Fundamental da Aritmética, qualquer número natural maior que 1 pode ser decomposto de forma única (a menos da ordem dos fatores) em um produto de potências de números primos.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "12". De acordo com a teoria estudada em *1.2 Conjunto dos Números Racionais: Decimais Finitos e Dízimas Periódicas*, decimais Exatos (ou Finitos): Apresentam um número finito de casas decimais após a vírgula. Isso ocorre quando a fração irredutível \$\frac{a}{b}\$ possui um denominador \$b\$ decomposto exclusivamente em fatores primos iguais a \$2\$ e/ou \$5\$.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "13". De acordo com a teoria estudada em *3.3 Mínimo Múltiplo Comum: Ciclos, Coincidências e Periodicidade*, o Mínimo Múltiplo Comum (MMC) entre dois ou mais inteiros é o menor número natural não nulo que é divisível simultaneamente por todos eles.
> - **E)** **Correta.** Conforme fundamentado na seção *1.1 Conjunto dos Números Naturais e Inteiros* deste guia, é fechado sob as operações de adição e multiplicação (a soma ou produto de dois naturais é sempre um natural), mas falha no fechamento da subtração quando o minuendo é menor que o subtraendo (\$3 - 8 \notin \mathbb{N}\$). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE-SC/2026) ao estabelecer que "14".
>
> **Gabarito: E**

---

### Teste 073
**(FGV – TJ-MT – Analista Judiciario Tecnologia da Informacao – 2024)**
A linguagem de programação Python é uma linguagem de alto nível, de tipagem dinâmica e interpretada, conhecida pela sua simplicidade, legibilidade e versatilidade. Criada por Guido van Rossum e lançada pela primeira vez em 1991, Python tem se tornado uma das linguagens mais populares do mundo, devido à sua capacidade de ser usada em diversos tipos de projetos, como desenvolvimento web, automação, análise de dados, inteligência artificial, aprendizado de máquina, automação de tarefas, entre outros. Em Python, o operador //

* **A)** realiza a divisão entre dois números e retorna o resultado com a maior precisão possível.
* **B)** realiza a divisão entre dois números e sempre retorna um número com ponto decimal, mesmo que o resultado seja inteiro.
* **C)** eleva o primeiro número ao segundo número, funcionando como um operador de potência.
* **D)** realiza a divisão inteira entre dois números, retornando apenas a parte inteira do resultado e descartando o resto.
* **E)** realiza a divisão entre dois números e retorna o resto da divisão, semelhante ao operador %.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *3.4 Máximo Divisor Comum: Partições Equitativas e Lotes Máximos* deste guia, em problemas de particionamento (como arquivar pastas em caixas de maior tamanho possível), o cálculo do MDC fornece a capacidade de cada caixa, e não a quantidade total de caixas! Para achar a quantidade de caixas, deve-se somar a divisão de cada lote pelo valor do MDC encontrado. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ-MT/2024) ao estabelecer que "realiza a divisão entre dois números e retorna o resultado com a maior precisão possível".
> - **B)** **Incorreta.** A opção promove generalização excessiva que desconsidera as condições técnicas e normativas ao afirmar que "realiza a divisão entre dois números e sempre retorna um número com ponto decimal, mesmo que o resultado seja...". De acordo com a teoria estudada em *3.4 Máximo Divisor Comum: Partições Equitativas e Lotes Máximos*, o Máximo Divisor Comum (MDC) é o maior número inteiro capaz de dividir exatamente todos os números dados, sem deixar resto.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "eleva o primeiro número ao segundo número, funcionando como um operador de potência". De acordo com a teoria estudada em *3.4 Máximo Divisor Comum: Partições Equitativas e Lotes Máximos*, palavras-chave: "Quando voltarão a se encontrar?", "periodicidade", "ciclos", "simultaneamente" — "Maior tamanho possível", "sem sobras", "dividir igualmente", "menor número de caixas".
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "realiza a divisão inteira entre dois números, retornando apenas a parte inteira do resultado e descartando o resto". De acordo com a teoria estudada em *5.2 Problemas de Trabalho Conjunto e Torneiras*, *Atenção à Conversão de Tempo:* Se o resultado da divisão em horas for decimal, como \$2,4\text{ horas}\$, a parte inteira corresponde a \$2\text{ horas}\$ e a parte decimal \$0,4\$ deve ser multiplicada por \$60\text{ minutos}\$ (\$0,4 \times 60 = 24\text{ minutos}\$).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "realiza a divisão entre dois números e retorna o resto da divisão, semelhante ao operador %". De acordo com a teoria estudada em *1.3 Algoritmo da Divisão Euclidiana e Aritmética dos Restos*, para quaisquer dois números inteiros \$D\$ (dividendo) e \$d\$ (divisor não nulo), existem inteiros únicos \$q\$ (quociente) e \$r\$ (resto) tais que.
>
> **Gabarito: A**

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
**(FGV – TCE-GO – Analista de Controle Externo Ciencias Contabeis – 2024)**
Tanto a auditoria interna quanto a auditoria externa são essenciais para garantir a integridade, transparência e eficácia das operações de uma organização. Assinale a opção que indica o Princípio Orçamentário que evita múltiplos orçamentos paralelos dentro da mesma pessoa política.

* **A)** Profundidade dos trabalhos maior e periodicidade dos testes menor.
* **B)** Grau de independência menor e periodicidade dos testes maior.
* **C)** Profundidade dos trabalhos menor e periodicidade dos testes maior.
* **D)** Grau de independência maior e periodicidade dos testes menor.
* **E)** Profundidade dos trabalhos maior e periodicidade dos testes maior.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *3.4 Máximo Divisor Comum: Partições Equitativas e Lotes Máximos* deste guia, palavras-chave: "Quando voltarão a se encontrar?", "periodicidade", "ciclos", "simultaneamente" — "Maior tamanho possível", "sem sobras", "dividir igualmente", "menor número de caixas". Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE-GO/2024) ao estabelecer que "Profundidade dos trabalhos maior e periodicidade dos testes menor".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Grau de independência menor e periodicidade dos testes maior". De acordo com a teoria estudada em *3.3 Mínimo Múltiplo Comum: Ciclos, Coincidências e Periodicidade*, o Mínimo Múltiplo Comum (MMC) entre dois ou mais inteiros é o menor número natural não nulo que é divisível simultaneamente por todos eles.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Profundidade dos trabalhos menor e periodicidade dos testes maior". De acordo com a teoria estudada em *3. Teoria dos Números: Divisibilidade, Primos, MMC e MDC*, a teoria dos números fornece o ferramental algébrico para lidar com divisões inteiras, periodicidade de escalas e otimização de lotes em logística e auditoria.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Grau de independência maior e periodicidade dos testes menor". De acordo com a teoria estudada em *1.1 Conjunto dos Números Naturais e Inteiros*, é fechado sob as operações de adição e multiplicação (a soma ou produto de dois naturais é sempre um natural), mas falha no fechamento da subtração quando o minuendo é menor que o subtraendo (\$3 - 8 \notin \mathbb{N}\$).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Profundidade dos trabalhos maior e periodicidade dos testes maior". De acordo com a teoria estudada em *1.3 Algoritmo da Divisão Euclidiana e Aritmética dos Restos*, o resto \$r\$ é estritamente não negativo e menor que o divisor (\$0 \le r \le d - 1\$).
>
> **Gabarito: A**

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
**(FGV – TRT-13 – Analista Judiciario Tecnologia da Informacao – 2022)**
A soma de 2 números naturais é 22253. Um dos números é divisível por 10 e se retirarmos o algarismo das unidades desse número obtém-se o outro número. A diferença entre o maior e o menor número é

* **A)** 13222.
* **B)** 14644.
* **C)** 15876.
* **D)** 17732.
* **E)** 18207.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *3.1 Critérios de Divisibilidade Aplicados* deste guia, permitem verificar se um número inteiro \$N\$ é divisível por outro sem executar a divisão longa. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT-13/2022) ao estabelecer que "13222".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "14644". De acordo com a teoria estudada em *1.1 Conjunto dos Números Naturais e Inteiros*, é fechado sob as operações de adição e multiplicação (a soma ou produto de dois naturais é sempre um natural), mas falha no fechamento da subtração quando o minuendo é menor que o subtraendo (\$3 - 8 \notin \mathbb{N}\$).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "15876". De acordo com a teoria estudada em *3.3 Mínimo Múltiplo Comum: Ciclos, Coincidências e Periodicidade*, o Mínimo Múltiplo Comum (MMC) entre dois ou mais inteiros é o menor número natural não nulo que é divisível simultaneamente por todos eles.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "17732". De acordo com a teoria estudada em *3.4 Máximo Divisor Comum: Partições Equitativas e Lotes Máximos*, palavras-chave: "Quando voltarão a se encontrar?", "periodicidade", "ciclos", "simultaneamente" — "Maior tamanho possível", "sem sobras", "dividir igualmente", "menor número de caixas".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "18207". De acordo com a teoria estudada em *3.1 Critérios de Divisibilidade Aplicados*, por 11: A diferença entre a soma dos algarismos de ordem ímpar e a soma dos algarismos de ordem par é múltipla de 11 (incluindo o zero).
>
> **Gabarito: A**

---

### Teste 076
**(FGV – TRT-13 – Analista Judiciario Tecnologia da Informacao – 2022)**
Um número inteiro positivo é chamado de “quadrado perfeito” quando ele é o quadrado de um número inteiro positivo. Por exemplo, 16 é um quadrado perfeito pois é igual a 42. O número de quadrados perfeitos maiores do que 100 e menores do que 2023 é

* **A)** 28.
* **B)** 34.
* **C)** 42.
* **D)** 44.
* **E)** 48.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "28". De acordo com a teoria estudada em *Quantidade Total de Divisores Positivos:*, *Exemplo:* Para encontrar quantos divisores possui o número 360.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "34". De acordo com a teoria estudada em *3.1 Critérios de Divisibilidade Aplicados*, permitem verificar se um número inteiro \$N\$ é divisível por outro sem executar a divisão longa.
> - **C)** **Correta.** Conforme fundamentado na seção *3.4 Máximo Divisor Comum: Partições Equitativas e Lotes Máximos* deste guia, fatoração em primos: Fatores comuns e não comuns com os maiores expoentes — Apenas fatores comuns com os menores expoentes. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT-13/2022) ao estabelecer que "42".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "44". De acordo com a teoria estudada em *3.4 Máximo Divisor Comum: Partições Equitativas e Lotes Máximos*, o Máximo Divisor Comum (MDC) é o maior número inteiro capaz de dividir exatamente todos os números dados, sem deixar resto.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "48". De acordo com a teoria estudada em *4.1 Conceito, Tipologias e Equivalência de Frações*, fração Aparente: O numerador é múltiplo exato do denominador, consubstanciando um número inteiro disfarçado (\$\frac{12}{3} = 4, \frac{35}{7} = 5\$).
>
> **Gabarito: C**

---

### Teste 077
**(IBFC – TJ-MG – Analista Judiciario Classe C Analista de Tecnologia da Informacao – 2022)**
A negação da proposição “Existem números inteiros divisíveis por 5” corresponde a:

* **A)** Existem números inteiros não divisíveis por 5
* **B)** Não existem números inteiros divisíveis por 5
* **C)** Qualquer número inteiro é divisível por 5
* **D)** Qualquer número inteiro não é divisível por 5
* **E)** Nem todo número inteiro é divisível por 5

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Existem números inteiros não divisíveis por 5". De acordo com a teoria estudada em *1.3 Algoritmo da Divisão Euclidiana e Aritmética dos Restos*, para quaisquer dois números inteiros \$D\$ (dividendo) e \$d\$ (divisor não nulo), existem inteiros únicos \$q\$ (quociente) e \$r\$ (resto) tais que.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Não existem números inteiros divisíveis por 5". De acordo com a teoria estudada em *3.2 Decomposição em Fatores Primos e Contagem de Divisores Positivos*, pelo Teorema Fundamental da Aritmética, qualquer número natural maior que 1 pode ser decomposto de forma única (a menos da ordem dos fatores) em um produto de potências de números primos.
> - **C)** **Incorreta.** A opção promove generalização excessiva que desconsidera as condições técnicas e normativas ao afirmar que "Qualquer número inteiro é divisível por 5". De acordo com a teoria estudada em *3.4 Máximo Divisor Comum: Partições Equitativas e Lotes Máximos*, o Máximo Divisor Comum (MDC) é o maior número inteiro capaz de dividir exatamente todos os números dados, sem deixar resto.
> - **D)** **Correta.** Conforme fundamentado na seção *3.1 Critérios de Divisibilidade Aplicados* deste guia, permitem verificar se um número inteiro \$N\$ é divisível por outro sem executar a divisão longa. Dessa forma, está plenamente correta a assertiva da banca (IBFC – TJ-MG/2022) ao estabelecer que "Qualquer número inteiro não é divisível por 5".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Nem todo número inteiro é divisível por 5". De acordo com a teoria estudada em *3.3 Mínimo Múltiplo Comum: Ciclos, Coincidências e Periodicidade*, o Mínimo Múltiplo Comum (MMC) entre dois ou mais inteiros é o menor número natural não nulo que é divisível simultaneamente por todos eles.
>
> **Gabarito: D**

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
**(FGV – TRT-13 – Analista Judiciario Tecnologia da Informacao – 2022)**
Carlos considera que um número é agradável quando a soma dos seus algarismos é 7 ou múltiplo de 7. Por exemplo, o ano de 2005 foi agradável pois 2 + 0 + 0 + 5 = 7, e o de 2039 será também, pois 2 + 0 + 3 + 9 = 14. Por esse critério, o número de anos agradáveis do século XX foi igual a

* **A)** 7.
* **B)** 10.
* **C)** 11.
* **D)** 13.
* **E)** 14.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "7". De acordo com a teoria estudada em *3.1 Critérios de Divisibilidade Aplicados*, por 9: A soma dos seus algarismos resulta em um múltiplo de 9.
> - **B)** **Correta.** Conforme fundamentado na seção *3.1 Critérios de Divisibilidade Aplicados* deste guia, por 3: A soma dos valores absolutos dos seus algarismos é um múltiplo de 3 (ex.: \$7.458 \rightarrow 7 + 4 + 5 + 8 = 24\$, que é divisível por 3). Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT-13/2022) ao estabelecer que "10".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "11". De acordo com a teoria estudada em *4.1 Conceito, Tipologias e Equivalência de Frações*, fração Aparente: O numerador é múltiplo exato do denominador, consubstanciando um número inteiro disfarçado (\$\frac{12}{3} = 4, \frac{35}{7} = 5\$).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "13". De acordo com a teoria estudada em *Quantidade Total de Divisores Positivos:*, *Exemplo:* Para encontrar quantos divisores possui o número 360.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "14". De acordo com a teoria estudada em *3.1 Critérios de Divisibilidade Aplicados*, por 6: É simultaneamente divisível por 2 (par) e por 3 (soma dos algarismos múltipla de 3).
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
**(FGV – TCE-SC – Auditor Fiscal de Controle Externo Administracao – 2026)**
Sejam 𝑋 e 𝑌 dois números inteiros maiores do que zero, tais que 2𝑋𝑌−𝑌= 36. A soma dos possíveis valores de 𝑋 é

* **A)** 8.
* **B)** 10.
* **C)** 12.
* **D)** 15.
* **E)** 21.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "8". De acordo com a teoria estudada em *1.1 Conjunto dos Números Naturais e Inteiros*, é fechado sob as operações de adição e multiplicação (a soma ou produto de dois naturais é sempre um natural), mas falha no fechamento da subtração quando o minuendo é menor que o subtraendo (\$3 - 8 \notin \mathbb{N}\$).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "10". De acordo com a teoria estudada em *1.1 Conjunto dos Números Naturais e Inteiros*, *Adição de Inteiros com Sinais Opostos:* Conserva-se o sinal do termo de maior valor absoluto (módulo) e subtraem-se os valores: \$(-15) + (+9) = -(15 - 9) = -6\$.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "12". De acordo com a teoria estudada em *3.1 Critérios de Divisibilidade Aplicados*, por 3: A soma dos valores absolutos dos seus algarismos é um múltiplo de 3 (ex.: \$7.458 \rightarrow 7 + 4 + 5 + 8 = 24\$, que é divisível por 3).
> - **D)** **Correta.** Conforme fundamentado na seção *1.3 Algoritmo da Divisão Euclidiana e Aritmética dos Restos* deste guia, para quaisquer dois números inteiros \$D\$ (dividendo) e \$d\$ (divisor não nulo), existem inteiros únicos \$q\$ (quociente) e \$r\$ (resto) tais que. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE-SC/2026) ao estabelecer que "15".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "21". De acordo com a teoria estudada em *1.1 Conjunto dos Números Naturais e Inteiros*, incorpora os opostos simétricos (negativos) aos números naturais, viabilizando o fechamento irrestrito da subtração. Na reta numérica, os inteiros organizam-se ordenadamente em torno da origem zero.
>
> **Gabarito: D**

---

### Teste 080
**(FCC – TRT-24 – Analista Judiciario Tecnologia da Informacao – 2017)**
Na sequência 1A3E; 5I7O; 9U11A; 13E15I; 17O19U; 21A23E; . . ., o 12o termo é formado por algarismos e pelas letras

* **A)** IO.
* **B)** AE.
* **C)** EI.
* **D)** UA.
* **E)** OA.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "IO". De acordo com a teoria estudada em *3.1 Critérios de Divisibilidade Aplicados*, por 8: O número formado pelos três últimos algarismos é divisível por 8 ou termina em \$000\$.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "AE". De acordo com a teoria estudada em *5.3 Problemas de Ciclos Periódicos e Padrões Sequenciais*, se o resto \$r > 0\$: O termo procurado é exatamente o \$r\$-ésimo elemento do ciclo padrão.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "EI". De acordo com a teoria estudada em *5.3 Problemas de Ciclos Periódicos e Padrões Sequenciais*, se o resto \$r = 0\$: O termo procurado é o último elemento do ciclo (o \$k\$-ésimo elemento).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "UA". De acordo com a teoria estudada em *1.1 Conjunto dos Números Naturais e Inteiros*, *Adição de Inteiros com Sinais Opostos:* Conserva-se o sinal do termo de maior valor absoluto (módulo) e subtraem-se os valores: \$(-15) + (+9) = -(15 - 9) = -6\$.
> - **E)** **Correta.** Conforme fundamentado na seção *3.1 Critérios de Divisibilidade Aplicados* deste guia, por 4: O número formado pelos dois últimos algarismos é divisível por 4 ou termina em \$00\$. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT-24/2017) ao estabelecer que "OA".
>
> **Gabarito: E**

---

### Teste 081
**(FGV – TCE-GO – Analista de Controle Externo Ciencias Contabeis – 2024)**
Assinale a opção em que a troca de posição realizada na frase é feita de forma a provocar modificação de sentido.

* **A)** Alguns me acham antipático porque minha cara não espelha minha alma / Porque minha cara não espelha minha alma, alguns me acham antipático.
* **B)** Os espíritos mais elevados são capazes das maiores faltas e das maiores virtudes / Os espíritos mais elevados são capazes das maiores virtudes e das maiores faltas.
* **C)** Diga “sim” sempre que possível e “não” sempre que necessário / Diga “não” sempre que necessário e “sim” sempre que possível.
* **D)** A sabedoria é a compreensão do eu e do mundo / A sabedoria é a compreensão do mundo e do eu.
* **E)** São as nossas escolhas e não as nossas habilidades que verdadeiramente mostram quem somos / São as nossas habilidades e não as nossas escolhas que verdadeiramente mostram quem somos.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Alguns me acham antipático porque minha cara não espelha minha alma / Porque minha cara não espelha minha alma...". De acordo com a teoria estudada em *1.1 Conjunto dos Números Naturais e Inteiros*, é fechado sob as operações de adição e multiplicação (a soma ou produto de dois naturais é sempre um natural), mas falha no fechamento da subtração quando o minuendo é menor que o subtraendo (\$3 - 8 \notin \mathbb{N}\$).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Os espíritos mais elevados são capazes das maiores faltas e das maiores virtudes / Os espíritos mais elevados são...". De acordo com a teoria estudada em *3.3 Mínimo Múltiplo Comum: Ciclos, Coincidências e Periodicidade*, cálculo Prático: Decompõem-se os números em fatores primos; o MMC é o produto de todos os fatores primos comuns e não comuns, elevados aos seus maiores expoentes.
> - **C)** **Correta.** Conforme fundamentado na seção *1.3 Algoritmo da Divisão Euclidiana e Aritmética dos Restos* deste guia, o resto máximo possível na divisão por um divisor \$d\$ é sempre igual a \$d - 1\$. Se um problema indagar o resto máximo obtido na divisão por \$15\$, esse valor é inequivocamente \$15 - 1 = 14\$. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE-GO/2024) ao estabelecer que "Diga “sim” sempre que possível e “não” sempre que necessário / Diga “não” sempre que necessário e “sim” sempre que...".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A sabedoria é a compreensão do eu e do mundo / A sabedoria é a compreensão do mundo e do eu". De acordo com a teoria estudada em *3.3 Mínimo Múltiplo Comum: Ciclos, Coincidências e Periodicidade*, o problema exige MMC sempre que veicular ideias de coincidência temporal futura, reencontro de eventos periódicos, ciclos de rondas/inspeções ou questões que indaguem: *"quando voltarão a se encontrar simultaneamente?"*.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "São as nossas escolhas e não as nossas habilidades que verdadeiramente mostram quem somos / São as nossas...". De acordo com a teoria estudada em *3.4 Máximo Divisor Comum: Partições Equitativas e Lotes Máximos*, palavras-chave: "Quando voltarão a se encontrar?", "periodicidade", "ciclos", "simultaneamente" — "Maior tamanho possível", "sem sobras", "dividir igualmente", "menor número de caixas".
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
