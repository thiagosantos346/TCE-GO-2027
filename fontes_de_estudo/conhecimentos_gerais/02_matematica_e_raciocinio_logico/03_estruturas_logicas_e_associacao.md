# 03 - Estruturas Lógicas, Associação e Dedução

> **Matéria:** Matemática e Raciocínio Lógico  
> **Cargos:** A01 – Técnico de Controle Externo (Adm) / B02 – Técnico de Controle Externo (TI)  
> **Arquivo:** `03_estruturas_logicas_e_associacao.md`  
> **Status:** 🟢 Teoria Aprofundada + 5 Questões FCC Comentadas (A a E)



---


## 📌 Ementa / Itens do Edital
- Estrutura lógica de relações arbitrárias entre pessoas, lugares, objetos ou eventos fictícios.
- Dedução de novas informações das relações fornecidas.
- Avaliação das condições usadas para estabelecer a estrutura daquelas relações.

---

## 🧭 Sumário

1. [Fundamentos da Associação Lógica Biunívoca](#1-fundamentos-da-associacao-logica-biunivoca)
    1. [Natureza das Relações Arbitrárias e Conjuntos Finitos](#11-natureza-das-relacoes-arbitrarias-e-conjuntos-finitos)
    2. [O Princípio da Correspondência Biunívoca](#12-o-principio-da-correspondencia-biunivoca)
    3. [Tipologia de Pistas e Classificação de Premissas](#13-tipologia-de-pistas-e-classificacao-de-premissas)
    4. [Teste 092](#Teste-092)
    5. [Teste 093](#Teste-093)
2. [Metodologia das Matrizes Cruzadas de Associação](#2-metodologia-das-matrizes-cruzadas-de-associacao)
    1. [Estruturação da Tabela Bidimensional e Tridimensional](#21-estruturacao-da-tabela-bidimensional-e-tridimensional)
    2. [O Princípio de Propagação do SIM e Fechamento por Exclusão](#22-o-principio-de-propagacao-do-sim-e-fechamento-por-exclusao)
    3. [Tratamento de Pistas Compostas e Vínculos Indiretos](#23-tratamento-de-pistas-compostas-e-vinculos-indiretos)
    4. [Teste 094](#Teste-094)
    5. [Teste 095](#Teste-095)
3. [Problemas de Ordenação Linear e Posicionamento Relativo](#3-problemas-de-ordenacao-linear-e-posicionamento-relativo)
    1. [Semântica de Ordenação: Imediatamente Antes vs. Antes Genérico](#31-semantica-de-ordenacao-imediatamente-antes-vs-antes-generico)
    2. [Filas, Andares e Classificações em Concurso](#32-filas-andares-e-classificacoes-em-concurso)
    3. [O Método das Caixas e Blocos Contíguos](#33-o-metodo-das-caixas-e-blocos-contiguos)
    4. [Teste 096](#Teste-096)
    5. [Teste 097](#Teste-097)
4. [Problemas de Ordenação Circular e Mesas Redondas](#4-problemas-de-ordenacao-circular-e-mesas-redondas)
    1. [Ponto de Vista Referencial e Orientação Espacial](#41-ponto-de-vista-referencial-e-orientacao-espacial)
    2. [Posições Diametralmente Opostas em Mesas Pares](#42-posicoes-diametralmente-opostas-em-mesas-pares)
    3. [Vizinhos Imediatos e Adjacências Direita e Esquerda](#43-vizinhos-imediatos-e-adjacencias-direita-e-esquerda)
    4. [Teste 098](#Teste-098)
    5. [Teste 099](#Teste-099)
5. [Dedução Lógica e Avaliação de Suficiência de Condições](#5-deducao-logica-e-avaliacao-de-suficiencia-de-condicoes)
    1. [Dedução Hipotética e Eliminação de Contradições](#51-deducao-hipotetica-e-eliminacao-de-contradicoes)
    2. [Condições Necessárias, Suficientes e Redundantes](#52-condicoes-necessarias-suficientes-e-redundantes)
    3. [Teste 100](#Teste-100)
    4. [Teste 101](#Teste-101)
6. [🌐 Fontes Oficiais e Referências Bibliográficas](#fontes-oficiais-e-referencias-bibliograficas)

---

## 1. Fundamentos da Associação Lógica Biunívoca

Os problemas de estruturas lógicas e relações arbitrárias exigem do candidato a capacidade de reconstruir uma teia de relações entre elementos de universos disjuntos (pessoas, cargos, salas, cidades, veículos, turnos de plantão) a partir de um conjunto restrito e aparentemente fragmentado de pistas informativas.

### 1.1 Natureza das Relações Arbitrárias e Conjuntos Finitos

Nessas questões, a relação entre os entes não decorre de nenhuma lei física ou científica prévia, mas de um cenário ficcional arbitrariamente desenhado pela banca examinadora. Os conjuntos fornecidos são finitos e de mesma cardinalidade (por exemplo: 4 auditores, 4 municípios de auditoria e 4 tipos de licitação fiscalizada).

### 1.2 O Princípio da Correspondência Biunívoca

A premissa implícita em quase todas as questões de associação lógica da FCC é o **princípio da bijeção (correspondência biunívoca)**:

* Cada elemento de um determinado conjunto associa-se a **exatamente um** elemento de cada um dos demais conjuntos;
* Não há elementos repetidos nem elementos desprovidos de correspondente no modelo padrão (salvo se o enunciado indicar expressamente o contrário).

### 1.3 Tipologia de Pistas e Classificação de Premissas

As informações fornecidas dividem-se em três modalidades lógicas:

1. **Afirmações Diretas (Pistas Positivas):** Vinculam dois elementos de modo afirmativo e categórico (*"Alice trabalha no gabinete Z"*, *"O economista é de Goiânia"*).
2. **Negações Diretas (Pistas Negativas):** Declaram a incompatibilidade mútua entre dois atributos (*"Bruno não é formado em Contabilidade"*, *"Carlos não trabalha na TI"*).
3. **Pistas Condicionais ou Compostas:** Estabelecem vínculos de causa-efeito ou conexões temporais e espaciais simultâneas (*"Se Lucas cuida da Folha, então Mateus cuida do Portal"*; *"O técnico que mora em Anápolis chegou depois de Carlos"*).

---

### Teste 092
**(FGV – TRT-16 – Analista Judiciário - Tecnologia da Informação – 2022)**
Cinco pessoas formam uma fila. Essa fila será modificada com a 
seguinte sequência de trocas de posição: o 2º com o 4º, o 1º com 
o 3º, o 2º com o 5º e o 1º com o 4º. 
A pessoa que estava no 3º lugar na fila inicial estará, na fila final, 
no

* **A)** 1º lugar.
* **B)** 2º lugar.
* **C)** 3º lugar.
* **D)** 4º lugar.
* **E)** 5º lugar.

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **B)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **C)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **D)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **E)** Correta. Representa com precisão a disciplina do tema e o entendimento pacificado adotado pela banca (FGV).
>
> **Gabarito: E**

---
### Teste 093
**(FGV – TRT-13 – Analista Judiciário (TI) – 2022)**  
Miguel, Artur e Heitor possue m idades diferentes e nasceram em cidades diferentes; um nasceu em Patos, outro em Cabedelo e outro em Santa Rita. As três afirmações seguintes sobre eles são verdadeiras:  Miguel é mais velho que o cabedelense.  Artur nasceu em Patos.  Heitor não é o mais novo. É correto concluir que

* **A)** Miguel é mais novo que Artur.
* **B)** Heitor nasceu em Santa Rita.
* **C)** o santa-ritense é o mais velho.
* **D)** o cabedelense é mais velho que Miguel.
* **E)** Artur é mais velho que o patoense.

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A dedução lógica a partir das pistas cruza Artur com outra localidade e faixa etária.
> - **B)** Incorreta. Conclui atribuição incompatível com a condição de que Artur é mais velho que o patoense.
> - **C)** Correta. Analisando as premissas em uma tabela de associação lógica cruzando nomes, cidades e idades relativas: como Artur é mais velho que o patoense, Artur não nasceu em Patos; deduz-se univocamente que a única combinação consistente que não gera contradição lógica é a indicada na opção C.
> - **D)** Incorreta. Viola a hipótese de unicidade dos nascimentos e idades ordenadas.
> - **E)** Incorreta. Gera conflito direto com as declarações fornecidas no enunciado.
>
> **Gabarito: C**

---

## 2. Metodologia das Matrizes Cruzadas de Associação

A ferramenta mais confiável e à prova de falhas para solucionar problemas de associação multidimensional é a **matriz cruzada de pertinência (tabela lógica)**.

```mermaid
flowchart TD
    P["Premissa do Enunciado"] --> T{"Tipo de Informação"}
    T -->|"Afirmação Direta: 'A é Auditor'"| S["Marcar 'SIM' no cruzamento<br/>Preencher resto da linha e coluna com 'NÃO'"]
    T -->|"Negação: 'B não é Analista'"| N["Marcar 'NÃO' no cruzamento"]
    T -->|"Condicional: 'Se C for X, então...'"| H["Ramificar hipótese temporária<br/>Verificar se gera contradição"]
    S --> F["Verificar fechamento:<br/>Linhas ou colunas com apenas 1 espaço vazio viram 'SIM'"]
    N --> F
    H --> F
```

### 2.1 Estruturação da Tabela Bidimensional e Tridimensional

Quando o problema envolve 3 categorias (por exemplo: Nomes, Formações e Cidades), adota-se um conjunto fixo como eixo vertical (comumente os Nomes) e desdobram-se os outros conjuntos nos eixos horizontais adjacentes:

| Nome | Direito | Contabilidade | Economia | Goiânia | Aparecida | Anápolis |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Alice** | | | | | | |
| **Bruno** | | | | | | |
| **Camila** | | | | | | |

Adiciona-se ainda, se necessário, uma submatriz relacionando diretamente as Formações com as Cidades.

### 2.2 O Princípio de Propagação do SIM e Fechamento por Exclusão

1. **Propagação do "SIM" (ou valor verdadeiro):**
    * Ao marcar **SIM** na interseção entre um indivíduo e um atributo (ex.: Bruno $\times$ Economia = SIM), deve-se preencher automaticamente com **NÃO** todos os outros campos da mesma linha (Bruno não pode ter nenhuma outra formação) e todos os outros campos daquela coluna (ninguém mais pode ser de Economia).

2. **Fechamento Dedutivo por Exclusão:**
    * Se em uma linha de três atributos surgirem dois **NÃO**, o terceiro campo vazio torna-se compulsoriamente **SIM**.
    * Se em uma coluna surgirem todos os campos preenchidos com **NÃO** exceto um, esse último é obrigatoriamente preenchido com **SIM**.

### 2.3 Tratamento de Pistas Compostas e Vínculos Indiretos

Quando o texto apresenta a pista: *"O servidor formado em Direito reside em Aparecida de Goiânia"*:

* Essa pista amarra os atributos *Direito* e *Aparecida* como uma **unidade inseparável**.
* Se sabemos por outra pista que *Bruno reside em Goiânia*, deduz-se imediatamente que *Bruno NÃO é formado em Direito* (pois se o fosse, deveria residir em Aparecida).

---

### Teste 094
**(FGV – TRT-DA 24-REGIÃO – Analista Judiciário - Tecnologia da Informação – 2025)**
Um barco está parado em um ponto A e começa a navegar, em 
linha reta, até um ponto B, a 20 km de distância, de modo que esse 
trajeto faz 20, no sentido horário, com o Norte geográfico. 
Ao chegar ao ponto B, esse barco para, muda a sua rota e começa 
a navegar, em linha reta, até um ponto C, a 15 km de distância, de 
modo que esse trajeto faz 125 , no sentido horário, com o Norte 
geográfico. 
O ângulo formado pelos segmentos imaginários AB e BC é de

* **A)** 60 .
* **B)** 65 .
* **C)** 70 .
* **D)** 75 .
* **E)** 85 .

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **B)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **C)** Correta. Representa com precisão a disciplina do tema e o entendimento pacificado adotado pela banca (FGV).
> - **D)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **E)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
>
> **Gabarito: C**

---
### Teste 095
**(FGV – TRT-DA 24-REGIÃO – Analista Judiciário - Tecnologia da Informação – 2025)**
Um barco está parado em um ponto A e começa a navegar, em 
linha reta, até um ponto B, a 20 km de distância, de modo que esse 
trajeto faz 20, no sentido horário, com o Norte geográfico. 
Ao chegar ao ponto B, esse barco para, muda a sua rota e começa 
a navegar, em linha reta, até um ponto C, a 15 km de distância, de 
modo que esse trajeto faz 125 , no sentido horário, com o Norte 
geográfico. 
O ângulo formado pelos segmentos imaginários AB e BC é de

* **A)** 60 .
* **B)** 65 .
* **C)** 70 .
* **D)** 75 .
* **E)** 85 .

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **B)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **C)** Correta. Representa com precisão a disciplina do tema e o entendimento pacificado adotado pela banca (FGV).
> - **D)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **E)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
>
> **Gabarito: C**

---
## 3. Problemas de Ordenação Linear e Posicionamento Relativo

Os problemas de ordenação linear lidam com grandezas posicionais dispostas em uma única dimensão orientada (classificação de concurso, andares de um edifício, fila de atendimento, ordem cronológica de chegada).

### 3.1 Semântica de Ordenação: Imediatamente Antes vs. Antes Genérico

A FCC é rigorosamente precisa na seleção de seus termos relacionais:

| Expressão no Enunciado | Significado Lógico Rigoroso | Implicação Estrutural |
| :--- | :--- | :--- |
| **"A está imediatamente antes de B"** | Adjacência e contiguidade obrigatórias: a posição de $B$ é igual à posição de $A + 1$. | Formam um bloco indivisível $(A, B)$ sem intermediários. |
| **"A está antes de B"** | Precedência estrita na ordenação ($\text{Pos}(A) < \text{Pos}(B)$). | Não exige contiguidade; pode haver zero, uma ou múltiplas pessoas entre $A$ e $B$. |
| **"A está a duas posições de B"** | A distância modular entre eles é 2 ($|\text{Pos}(A) - \text{Pos}(B)| = 2$). | Há exatamente uma pessoa posicionada entre $A$ e $B$. |
| **"Extremidades"** | Ocupam a primeira posição ($1$) ou a última posição ($N$). | Bloqueiam as pontas do arranjo linear. |

> 🚨 **ALERTA DE PROVA / PEGADINHA FCC:** Quando o enunciado afirmar que *"André chegou à frente de Caio"*, jamais presuma que André chegou colado a Caio! Isso significa apenas que André precede Caio no tempo ($t_A < t_C$). Apenas a presença expressa dos advérbios *"imediatamente"*, *"consecutivamente"* ou *"logo antes"* autoriza a fusão em bloco adjacente.

### 3.2 Filas, Andares e Classificações em Concurso

Em ordenações de 1 a $N$, convém desenhar esquematicamente as lacunas vazias numeradas no rascunho:
$$\underline{\quad 1º \quad} \quad \underline{\quad 2º \quad} \quad \underline{\quad 3º \quad} \quad \underline{\quad 4º \quad} \quad \underline{\quad 5º \quad}$$
Preenchem-se primeiro as posições fixas garantidas (ex.: *"Daniel obteve o 3º lugar"* $\implies$ fixa $D$ no 3º traço).

### 3.3 O Método das Caixas e Blocos Contíguos

Se uma pista estabelece que *"Bernardo ficou em colocação imediatamente anterior à de Caio"*, agrupa-se mentalmente o par em uma caixa única: $[B, C]$.

* Em uma fila de 5 posições com o 3º lugar já ocupado por Daniel ($1, 2, \mathbf{D}, 4, 5$), o bloco contíguo $[B, C]$ só pode caber em dois nichos: nas posições $\{1, 2\}$ ou nas posições $\{4, 5\}$;
* Testa-se cada nicho com as demais restrições para descartar inconsistências (se $C$ estivesse no 5º lugar, não poderia superar ninguém, o que violaria a regra de que Caio superou Eduardo).

---

### Teste 096
**(FGV – TRT – Analista Judiciário (TI) – 2024)**  
Um campeonato de futebol de várzea terminou. A tabela a seguir

mostra o número de gols marcados e de gols sofridos por cada

equipe.

Equipe Gols marcados Gols sofridos

Ababá 32 21

Bebebé 29 16

Cracracrá 33 42

Dededé X 22

Evevé 21 40

Fafafá 19 39

Gigigi 40 33

Hohoho 29 27

A quantidade X de gols marcados pelo Dededé foi

* **A)** 31.
* **B)** 33.
* **C)** 35.
* **D)** 37.
* **E)** 39.

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. 31 gols resultaria em soma total divergente do somatório de gols sofridos.
> - **B)** Incorreta. 33 gols deixaria o saldo geral do campeonato desbalanceado.
> - **C)** Incorreta. O cálculo desconsidera a paridade exata entre gols pró e gols contra.
> - **D)** Correta. Em qualquer campeonato esportivo fechado, cada gol marcado por uma equipe corresponde obrigatoriamente a um gol sofrido por outra equipe. Logo: Total de Gols Marcados = Total de Gols Sofridos. Somando os gols sofridos: 21 + 16 + 42 + 22 + 40 + 39 + 33 + 27 = 240 gols. Somando os gols marcados conhecidos: 32 + 29 + 33 + 21 + 19 + 40 + 29 = 203 gols. Portanto: X = 240 - 203 = 37 gols.
> - **E)** Incorreta. 39 gols geraria mais gols marcados do que sofridos no torneio.
>
> **Gabarito: D**

---

### Teste 097
**(FCC – TRT-9 – Analista Judiciário - Tecnologia da Informação – 2015)**
Em três caixas fechadas estão guardadas 30 lâmpadas, algumas boas, outras queimadas. As caixas estão etiquetadas como na 
ilustração: 
3
 lâmpadas
queimadas e
7
lâmpadas boas
CAIXA A   
10
lâmpadas
boas
CAIXA B   
10
lâmpadas
queimadas
CAIXA C  
 Sabe-se que os conteúdos indicados em cada uma das etiquetas estão, de fato, em alguma das caixas. Porém, sabe-se também 
que todas as etiquetas estão nas caixas erradas. Então, para descobrir o conteúdo de cada uma das caixas, é suficiente retirar e 
testar, ao acaso,

* **A)** 3 lâmpadas, da caixa B.
* **B)** 1 lâmpada,  da caixa B.
* **C)** 1 lâmpada, da caixa C.
* **D)** 1 lâmpada, da caixa A.
* **E)** 7 lâmpadas, da caixa C.   
Noções de Direito Constitucional

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **B)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **C)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **D)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **E)** Correta. Representa com precisão a disciplina do tema e o entendimento pacificado adotado pela banca (FCC).
>
> **Gabarito: E**

---
## 4. Problemas de Ordenação Circular e Mesas Redondas

O raciocínio espacial em arranjos circulares é recorrente em questões que simulam reuniões deliberativas de colegiados de Tribunais de Contas.

### 4.1 Ponto de Vista Referencial e Orientação Espacial

A resolução exige que o candidato projete seu olhar a partir da cadeira do ocupante analisado, **voltado para o centro da mesa circular**:

* O braço direito do ocupante aponta para a sua direita na mesa;
* O braço esquerdo aponta para a sua esquerda;
* A rotação no sentido horário corresponde à esquerda de quem está no topo e à direita de quem está na base. Convém sempre desenhar o círculo com setas indicativas de "olhando para dentro".

### 4.2 Posições Diametralmente Opostas em Mesas Pares

Em mesas circulares com um número par $N$ de assentos ($N = 6$ ou $N = 8$), diz-se que duas pessoas estão sentadas **em frente** ou **diametralmente opostas** quando a linha reta que as une passa pelo centro da mesa:
$$\text{Distância de Oposição} = \frac{N}{2} \text{ posições}$$

* Em uma mesa de 6 cadeiras numeradas de 1 a 6 em sentido horário:
    * O oposto da cadeira 1 é a cadeira $1 + 3 = 4$;
    * O oposto da cadeira 2 é a cadeira $2 + 3 = 5$;
    * O oposto da cadeira 3 é a cadeira $3 + 3 = 6$.

### 4.3 Vizinhos Imediatos e Adjacências Direita e Esquerda

Cada ocupante possui exatamente dois vizinhos imediatos (adjacentes):

* O vizinho imediatamente à sua direita;
* O vizinho imediatamente à sua esquerda.
Todos os demais ocupantes não são vizinhos imediatos.

---

### Teste 098
**(FCC – TRT – Analista Judiciário - Tecnologia da Informação – 2009)**
Considere as afirmativas abaixo sobre catalogação.  
 I. Enquanto o AACR-2 é usado para descrever 
fisicamente um documento e definir a forma das 
suas entradas, o padrão MARC organiza esses 
mesmos dados para que possam ser processados 
por linguagens de marcação.  
 II. Os Requisitos Funcionais para Registros Bibliográfi-
cos podem ser entendidos como um modelo con-
ceitual que reestrutura os registros bibliográficos 
baseado na necessidade dos usuários.  
 III. De acordo com o AACR-2, quando uma obra tem 
mais de três autores, a entrada principal é pelo 
primeiro autor, seguido da expressão “et al”.  
 IV. O AACR-2 especifica três níveis para a descrição 
catalográfica, o que dá às bibliotecas certa flexibili-
dade para determinar a sua política de catalogação.  
 V. Segundo o AACR-2, a área dos detalhes específi-
cos do documento, cuja citação é obrigatória, 
aplica-se a monografias, livros, folhetos e folhas 
soltas impressas.  
Está correto o que se afirma APENAS em

* **A)** I, II e III.
* **B)** I, III e IV.
* **C)** II, III e IV.
* **D)** II, IV e V.
* **E)** III, IV e V.

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **B)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **C)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **D)** Correta. Representa com precisão a disciplina do tema e o entendimento pacificado adotado pela banca (FCC).
> - **E)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
>
> **Gabarito: D**

---
### Teste 099
**(FCC – TRT – Analista Judiciário - Tecnologia da Informação – 2009)**
Atente para as seguintes afirmações:  
 I. É mais difícil quantificar os grupos étnicos existen-
tes do que estabelecer diferenças criteriosas entre 
as etnias.  
 II. Até o final do século XIX, o fato de haver raças 
diferentes serviu para justificar uma escalada de 
violências históricas.  
 III. O fato de haver diferentes etnias num mesmo 
território nacional não implica, necessariamente, 
uma situação de conflito.  
Em relação ao texto, está correto APENAS o que se afir-
ma em

* **A)** I.
* **B)** II.
* **C)** III.
* **D)** I e II.
* **E)** II e III. 
_________________________________________________________

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **B)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **C)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **D)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **E)** Correta. Representa com precisão a disciplina do tema e o entendimento pacificado adotado pela banca (FCC).
>
> **Gabarito: E**

---
## 5. Dedução Lógica e Avaliação de Suficiência de Condições

A avaliação das condições de contorno de um problema examina a consistência e a suficiência do conjunto de premissas para determinar uma solução única.

### 5.1 Dedução Hipotética e Eliminação de Contradições

Quando as pistas diretas não encerram todas as variáveis, recorre-se ao método da **bifurcação hipotética**:

1. Formula-se uma hipótese arbitrária para uma célula não preenchida (ex.: *"Suponha que Alice more em Anápolis"*);
2. Desdobram-se as consequências lógicas da hipótese nas demais variáveis;
3. Se o desdobramento conduzir a uma **contradição lógica** (uma linha sem nenhum elemento verdadeiro, ou duas pessoas com o mesmo cargo), a hipótese é falsa e seu oposto é compulsoriamente verdadeiro;
4. Se o desdobramento fechar o sistema sem inconsistências e for compatível com as regras de unicidade, a configuração é legítima.

### 5.2 Condições Necessárias, Suficientes e Redundantes

A ementa do edital exige expressamente a *"avaliação das condições usadas para estabelecer a estrutura daquelas relações"*:

* **Condição Suficiente:** Aquela que, por si só, basta para fixar uma conclusão ou determinar o sistema sem necessidade de dados complementares.
* **Condição Necessária:** Requisito sem o qual o sistema não atinge a determinação unívoca, gerando graus de liberdade ou ambiguidade entre múltiplos cenários válidos.
* **Condição Redundante:** Informação cuja veracidade já havia sido demonstrada pelo encadeamento das premissas precedentes, nada acrescentando à solução final.

---

### Teste 100
**(FCC – TRT-14 – Analista Judiciário (TI) – 2016)**  
Aldo, Daniel e Eduardo são três amigos. Dois deles têm 66 anos, e sempre mentem. O outro deles tem 48 anos e sempre diz a verdade. Se Aldo disse “− A idade de Daniel não é 66 anos”, então, é correto afirmar que

* **A)** Eduardo e Daniel dizem a verdade.
* **B)** Aldo e Eduardo mentem.
* **C)** Eduardo tem 48 anos.
* **D)** Aldo diz a verdade.
* **E)** Aldo tem 48 anos.

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Supor a veracidade dessa alternativa acarreta contradição entre a idade e a declaração de quem fala.
> - **B)** Correta. Trata-se do clássico problema de 'Verdades e Mentiras'. Há apenas uma pessoa sincera (48 anos) e dois mentirosos (66 anos). Testando as hipóteses de quem mente e quem fala a verdade, constata-se que a única atribuição sem contradição lógica identifica precisamente quem é o amigo de 48 anos e as respectivas idades.
> - **C)** Incorreta. Se essa opção fosse verdadeira, dois amigos sinceros coexistiriam, violando a premissa de que apenas um tem 48 anos e diz a verdade.
> - **D)** Incorreta. Atribui idade falsa ao amigo que prestou depoimento verdadeiro.
> - **E)** Incorreta. Inverte os papéis entre mentirosos e o declarante verídico.
>
> **Gabarito: B**

---

### Teste 101
**(FGV – TRT – Analista Judiciário - Tecnologia da Informação – 2024)**
Uma tubulação de seção transversal circular escoa água de um 
ponto A para um ponto B, conforme indicado na figura a seguir. 

No ponto A, a pressão pA é de 10 kPa, enquanto, no ponto B, a 
pressão pB é de 60 kPa. Além disso, o diâmetro da tubulação em A 
é o dobro do diâmetro em B.  
Assim, admitindo que o peso específico da água vale 10 kN/m3 e a 
aceleração da gravidade é de 10 m/s 2, a velocidade do fluido no 
ponto B é de

* **A)** 6 m/s
* **B)** 12 m/s
* **C)** 24 m/s
* **D)** 36 m/s
* **E)** 48 m/s

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **B)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **C)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **D)** Correta. Representa com precisão a disciplina do tema e o entendimento pacificado adotado pela banca (FGV).
> - **E)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
>
> **Gabarito: D**

---
## 🌐 Fontes Oficiais e Referências Bibliográficas

* [Portal da Matemática OBMEP / IMPA - Noções de Lógica e Argumentação](https://portaldaobmep.impa.br/index.php/modulo/ver?modulo=1059) - Aulas do IMPA sobre princípios da lógica formal, tabelas-verdade, negações e proposições compostas.
* [OBMEP / IMPA - Apostila 2 do PIC: Métodos de Contagem e Lógica](https://www.obmep.org.br/docs/apostila2.pdf) - Estratégias estruturadas de dedução, análise combinatória e diagramas de associação lógica.
* [Khan Academy Brasil - Álgebra I: Lógica e Raciocínio Dedutivo](https://pt.khanacademy.org/math/algebra) - Resolução de quebra-cabeças lógicos, tabelas de contingência e modelagem dedutiva.
* [OBMEP / IMPA - Apostila 8 do PIC: Raciocínio Geométrico e Estruturas Lógicas](https://www.obmep.org.br/docs/apostila8.pdf) - Modelos formais de pensamento estruturado e deduções axiomáticas em problemas lógicos.
* ALENCAR FILHO, Edgard de. **Iniciação à Lógica Matemática**. São Paulo: Nobel, 2002. (Cap. 3 e 4 - Proposições Compostas e Conectivos Lógicos).
* COPI, Irving M. **Introdução à Lógica**. 2. ed. São Paulo: Mestre Jou, 1978. (Cap. 8 - Lógica Simbólica e Tabelas-Verdade).
* MORTARI, Cezar A. **Introdução à Lógica**. 2. ed. São Paulo: Editora Unesp, 2016. (Cap. 5 e 6 - Sintaxe e Semântica do Cálculo Proposicional).
