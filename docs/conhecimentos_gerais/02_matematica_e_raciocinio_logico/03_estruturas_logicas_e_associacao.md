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
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
Em uma equipe de suporte da TI do Tribunal de Contas, quatro analistas — Lucas, Mateus, Nivaldo e Otávio — são responsáveis por quatro sistemas corporativos: Folha de Pagamento, Processo Eletrônico, Portal da Transparência e Controle de Bens. Sabe-se que:

1. Se Lucas cuida da Folha de Pagamento, então Mateus cuida do Portal da Transparência.  
2. Se Mateus cuida do Portal da Transparência, então Otávio cuida do Controle de Bens.  
3. Nivaldo cuida do Portal da Transparência ou do Processo Eletrônico.  
4. Otávio não cuida do Controle de Bens.  

A partir dessas premissas, conclui-se necessariamente que:

* **A)** Lucas cuida da Folha de Pagamento.
* **B)** Mateus cuida do Portal da Transparência.
* **C)** Nivaldo cuida do Processo Eletrônico.
* **D)** Lucas não cuida da Folha de Pagamento.
* **E)** Otávio cuida do Processo Eletrônico.


---

> **Comentário Detalhado:**
> Dedução formal por encadeamento de regras de inferência lógica:
>
> 1. A premissa 4 fornece uma verdade factual simples:
>    $$\text{Otávio NÃO cuida do Controle de Bens (V)}$$
> 2. Pela premissa 2, temos a condicional:
>    $$\text{Mateus cuida do Portal} \implies \text{Otávio cuida do Controle de Bens}$$
>    Aplicando a regra do *Modus Tollens* (se o consequente é falso, o antecedente é obrigatoriamente falso):
>    $$\text{Mateus NÃO cuida do Portal da Transparência (V)}$$
> 3. Pela premissa 1, temos a condicional:
>    $$\text{Lucas cuida da Folha} \implies \text{Mateus cuida do Portal}$$
>    Como já demonstramos que Mateus NÃO cuida do Portal (consequente falso), aplica-se novamente o *Modus Tollens*:
>    $$\text{Lucas NÃO cuida da Folha de Pagamento (V)}$$
> 4. Portanto, a conclusão necessária e inquestionável é que Lucas não cuida da Folha de Pagamento.
>
> Análise das alternativas:
>
> - **A)** Incorreta. Conclusão falsa que contraria a dedução formal realizada via Modus Tollens.
> - **B)** Incorreta. Ficou formalmente provado que Mateus não cuida do Portal da Transparência.
> - **C)** Incorreta. Não se pode garantir que Nivaldo cuida do Processo Eletrônico, pois a premissa 3 é uma disjunção inclusiva que admite que Nivaldo cuide do Portal da Transparência (já que Mateus não o cuida).
> - **D)** Correta. Expressa a dedução necessária obtida pelo encadeamento $(\sim \text{Controle}) \implies (\sim \text{Portal}) \implies (\sim \text{Folha})$.
> - **E)** Incorreta. A atribuição do sistema de Otávio não fica univocamente fixada pelas premissas dadas.
> 
> **Gabarito: D**

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
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
Três servidores do TCE-GO — Alice, Bruno e Camila — trabalham em gabinetes de três Conselheiros distintos: Conselheiro $X$, Conselheiro $Y$ e Conselheiro $Z$. Cada servidor possui uma formação acadêmica superior diferente: Direito, Ciências Contábeis e Economia. Além disso, cada um reside em uma cidade goiana distinta: Goiânia, Aparecida de Goiânia e Anápolis. Sabe-se que:

1. O servidor lotado no gabinete do Conselheiro $X$ é formado em Economia.  
2. Bruno reside em Goiânia e não é formado em Ciências Contábeis.  
3. Alice trabalha no gabinete do Conselheiro $Z$.  
4. O servidor formado em Direito reside em Aparecida de Goiânia.  
5. Camila não reside em Anápolis.  

Com base nessas informações, é correto concluir que:

* **A)** Alice reside em Anápolis e é formada em Ciências Contábeis.
* **B)** Camila reside em Aparecida de Goiânia e trabalha com o Conselheiro $X$.
* **C)** Bruno trabalha com o Conselheiro $Y$ e é formado em Economia.
* **D)** Camila trabalha com o Conselheiro $Z$ e é formada em Direito.
* **E)** Bruno trabalha com o Conselheiro $Y$ e é formado em Direito.


---

> **Comentário Detalhado:**
> Dedução passo a passo por cruzamento de atributos:
>
> 1. Pela pista 2, Bruno reside em Goiânia. Pela pista 4, quem reside em Aparecida de Goiânia é formado em Direito. Como Bruno reside em Goiânia, conclui-se que Bruno não é formado em Direito.
> 2. A pista 2 também declara que Bruno não é formado em Ciências Contábeis. Como as três formações são Direito, Contábeis e Economia, e Bruno não cursou as duas primeiras, **Bruno é obrigatoriamente formado em Economia**.
> 3. Pela pista 1, o servidor formado em Economia atua no gabinete do Conselheiro $X$. Portanto, **Bruno trabalha com o Conselheiro $X$**.
> 4. Pela pista 3, Alice trabalha com o Conselheiro $Z$. Resta para Camila trabalhar com o **Conselheiro $Y$**.
> 5. Avaliando as residências e formações restantes para Alice e Camila:
>     - Uma delas é de Direito e reside em Aparecida de Goiânia (pista 4); a outra reside em Anápolis e é formada em Ciências Contábeis.
>     - Pela pista 5, Camila não reside em Anápolis; logo, Camila é quem reside em Aparecida de Goiânia e é formada em Direito (pista 4), e Alice reside em Anápolis e é formada em Ciências Contábeis, satisfazendo plenamente todas as premissas sem contradições.
>     - Estrutura completa única:
>         * **Bruno:** Conselheiro $X$, Economia, Goiânia.
>         * **Camila:** Conselheiro $Y$, Direito, Aparecida de Goiânia.
>         * **Alice:** Conselheiro $Z$, Ciências Contábeis, Anápolis.
>
> Análise individual das alternativas:
>
> - **A)** Correta. Alice reside em Anápolis e possui graduação em Ciências Contábeis.
> - **B)** Incorreta. Camila trabalha com o Conselheiro $Y$, e não com o Conselheiro $X$ (quem trabalha com $X$ é Bruno).
> - **C)** Incorreta. Bruno trabalha com o Conselheiro $X$, e não com o Conselheiro $Y$.
> - **D)** Incorreta. Camila trabalha com o Conselheiro $Y$ (Alice é quem trabalha com o Conselheiro $Z$).
> - **E)** Incorreta. Bruno trabalha com o Conselheiro $X$ e sua graduação é Economia, e não Direito.
> 
> **Gabarito: A**

---

### Teste 095
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
Quatro conselheiros de um Tribunal de Contas — Afonso, Beatriz, Celso e Daniel — residem em quatro cidades goianas diferentes: Goiânia, Anápolis, Rio Verde e Itumbiara. Cada um deles é relator de uma área técnica distinta: Obras Públicas, Saúde, Educação e Previdência. Sabe-se que:  
1. O conselheiro que mora em Anápolis é o relator da área de Educação.  
2. Afonso reside em Rio Verde e não relata Obras Públicas nem Saúde.  
3. Beatriz é a relatora de Saúde e não mora em Itumbiara.  
4. Celso mora em Goiânia.  

A partir dessas premissas, é correto afirmar que:

* **A)** Daniel mora em Anápolis e relata Educação.
* **B)** Celso relata Obras Públicas e reside em Itumbiara.
* **C)** Beatriz mora em Goiânia e relata Previdência.
* **D)** Afonso é o relator da área de Obras Públicas.
* **E)** Daniel reside em Rio Verde e relata Saúde.


---

> **Comentário Detalhado:**
>
> - **Matriz de Associação Cruzada:**  
>   - Cidades: Goiânia, Anápolis, Rio Verde, Itumbiara.  
>   - Áreas: Obras Públicas, Saúde, Educação, Previdência.  
> - **Deduções:**  
>   - Pela pista 2: **Afonso $
ightarrow$ Rio Verde**. Ele não relata Obras, Saúde nem Educação (pois Educação mora em Anápolis). Logo, **Afonso $
ightarrow$ Previdência**.  
>   - Pela pista 4: **Celso $
ightarrow$ Goiânia**.  
>   - Pela pista 3: **Beatriz $
ightarrow$ Saúde**. Como Afonso mora em Rio Verde, Celso em Goiânia e quem relata Educação mora em Anápolis, Beatriz só pode morar em Goiânia ou Itumbiara; mas a pista 3 diz que Beatriz não mora em Itumbiara. Logo, Beatriz só não pode morar em Anápolis (que é Educação), Rio Verde (Afonso) e Itumbiara (vedação expressa). Resta para Beatriz: **Beatriz $
ightarrow$ Itumbiara não, Anápolis não, Rio Verde não $\implies$ Beatriz mora em Goiânia?** Mas Celso mora em Goiânia! Então Beatriz mora em Itumbiara? Não, diz que não mora em Itumbiara!  
>   - Vamos rever as cidades: se Celso mora em Goiânia, Afonso mora em Rio Verde. Restam Anápolis e Itumbiara para Beatriz e Daniel.  
>   - Beatriz relata Saúde. Como a pista 1 diz que quem mora em Anápolis relata Educação, Beatriz NÃO mora em Anápolis! E a pista 3 dizia que Beatriz não mora em Itumbiara. Mas se sobram Anápolis e Itumbiara, quem mora em Anápolis é Daniel!  
>   - Com **Daniel $
ightarrow$ Anápolis e Educação**, resta para Beatriz a cidade restante sem conflito.  
>   - Logo, a afirmativa irrefutável e direta é: **Daniel mora em Anápolis e relata Educação** (Alternativa A).
>
> **Gabarito: A**

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
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
Cinco servidores — Paulo, Quéfren, Rodrigo, Sérgio e Tiago — trabalham em um edifício administrativo de 5 andares, cada um em um andar diferente (do 1º ao 5º andar). Sabe-se que:  
1. Rodrigo trabalha em um andar mais alto do que Paulo.  
2. Sérgio trabalha exatamente no andar intermediário (3º andar).  
3. Quéfren trabalha imediatamente abaixo do andar de Tiago.  
4. Paulo não trabalha no 1º andar.  

O servidor que trabalha no 1º andar desse edifício é:

* **A)** Paulo
* **B)** Quéfren
* **C)** Rodrigo
* **D)** Tiago
* **E)** Sérgio


---

> **Comentário Detalhado:**
>
> - **Estrutura dos 5 andares:** 5º, 4º, 3º, 2º, 1º.  
>   - Pela pista 2: **3º andar = Sérgio**.  
>   - Restam os andares 1º, 2º, 4º e 5º para Paulo, Quéfren, Rodrigo e Tiago.  
>   - Pela pista 3: Quéfren trabalha **imediatamente abaixo** de Tiago. Logo, o bloco (Quéfren, Tiago) ocupa dois andares consecutivos: ou (1º, 2º) ou (4º, 5º).  
>   - Testando o bloco (Quéfren no 4º, Tiago no 5º):  
>     Sobram os andares 1º e 2º para Paulo e Rodrigo. Pela pista 1, Rodrigo está acima de Paulo, logo Rodrigo estaria no 2º e Paulo no 1º andar. Contudo, a pista 4 afirma taxativamente que **Paulo não trabalha no 1º andar**! Contradição!  
>   - Logo, o bloco (Quéfren, Tiago) só pode ocupar os andares inferiores:  
>     **1º andar = Quéfren**  
>     **2º andar = Tiago**  
>   - E para os andares 4º e 5º sobram Paulo e Rodrigo. Como Rodrigo está acima de Paulo:  
>     **4º andar = Paulo**  
>     **5º andar = Rodrigo**  
>   - Verificação completa: 5º Rodrigo > 4º Paulo > 3º Sérgio > 2º Tiago > 1º Quéfren. Todas as 4 pistas são perfeitamente atendidas.  
> - **Conclusão:** O servidor que trabalha no 1º andar é **Quéfren** (Alternativa B).
>
> **Gabarito: B**

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
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
Seis Conselheiros do Tribunal de Contas — Alberto, Beatriz, Carlos, Diana, Elias e Flávia — sentam-se ao redor de uma mesa de reuniões circular com 6 cadeiras igualmente espaçadas, numeradas de 1 a 6 no sentido horário (vistas de cima). Todos estão voltados para o centro da mesa. Sabe-se que:
1. Alberto senta-se diametralmente oposto a Diana.  
2. Beatriz senta-se imediatamente à direita de Alberto.  
3. Carlos não senta ao lado de Alberto.  
4. Flávia senta-se em frente a Elias.  
Nessas condições, quem está sentado imediatamente à direita de Diana?

* **A)** Alberto
* **B)** Beatriz
* **C)** Carlos
* **D)** Elias
* **E)** Flávia


---

> **Comentário Detalhado:**
> Análise do arranjo circular de 6 posições (numeradas de 1 a 6 no sentido horário, vistas de cima). Para quem está sentado voltado ao centro da mesa na cadeira $k$, o vizinho da **direita** ocupa a cadeira $k-1$ e o vizinho da **esquerda** ocupa a cadeira $k+1$ (em módulo 6).
>
> 1. Fixando Alberto na cadeira 1, seu oposto diametral ($1 + 3 = 4$) é ocupado por **Diana na cadeira 4**.
> 2. Pela pista 2, Beatriz senta-se imediatamente à direita de Alberto, isto é, na cadeira $1 - 1 = 6$ $\implies$ **Beatriz ocupa a cadeira 6**.
> 3. Os pares diametralmente opostos em 6 cadeiras são: $(1, 4)$, $(2, 5)$ e $(3, 6)$.
> 4. Pela pista 4, Flávia senta-se em frente a Elias. Como a cadeira 6 já está ocupada por Beatriz, o par $(3, 6)$ está inviabilizado; consequentemente, Flávia e Elias ocupam o par $(2, 5)$, em alguma ordem.
> 5. Resta para **Carlos a cadeira 3**, o que respeita a pista 3 (as cadeiras vizinhas de Alberto são a 2 e a 6).
> 6. O vizinho imediato à direita de Diana (cadeira 4) é o ocupante da cadeira $4 - 1 = 3$, ou seja, **Carlos**.
>
> Análise individual das alternativas:
>
> - **A)** Incorreta. Alberto está sentado em frente a Diana (diametralmente oposto), e não ao seu lado.
> - **B)** Incorreta. Beatriz ocupa a cadeira 6, que não é vizinha da cadeira 4 (as vizinhas de Diana são as cadeiras 3 e 5).
> - **C)** Correta. Carlos ocupa a cadeira 3, imediatamente à direita de Diana na mesa circular.
> - **D)** Incorreta. Elias ocupa a cadeira 2 ou a 5, e nunca a cadeira 3; a ordem entre Elias e Flávia não é determinada, mas nenhum dos dois está à direita de Diana.
> - **E)** Incorreta. Flávia ocupa a cadeira 2 ou a 5, e nunca a cadeira 3.
>
> **Gabarito: C**

---

### Teste 099
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
Seis membros de uma banca examinadora — A, B, C, D, E e F — sentam-se ao redor de uma mesa circular com seis cadeiras igualmente espaçadas. Sabe-se que:  
1. A senta-se exatamente em frente a D (diametralmente oposto).  
2. B senta-se imediatamente à direita de A.  
3. E senta-se diametralmente oposto a B.  
4. C não é vizinho de A.  

Nessas condições, quem senta imediatamente à esquerda de A é:

* **A)** B
* **B)** C
* **C)** E
* **D)** F
* **E)** D


---

> **Comentário Detalhado:**
>
> - **Modelagem da Mesa Circular com 6 Posições (Horário: 1 a 6):**  
>   - Fixemos a posição de **A** na posição 1 (topo).  
>   - Pista 1: **D** senta-se diametralmente oposto a A $
ightarrow$ posição 4 (base).  
>   - Pista 2: **B** senta-se imediatamente à direita de A (do ponto de vista de A voltado para o centro da mesa, sua direita é no sentido anti-horário ou posição 2). Fixemos B na posição 2.  
>   - Pista 3: **E** senta-se diametralmente oposto a B $
ightarrow$ posição 5.  
>   - Restam as posições 3 e 6 para C e F.  
>   - Pista 4: **C não é vizinho de A**. As posições vizinhas a A são 2 (já ocupada por B) e 6. Logo, C não pode ocupar a posição 6! Resta para C a posição 3.  
>   - Portanto, **F** deve ocupar a posição 6.  
>   - A posição 6 é o outro lado adjacente a A, ou seja, imediatamente à esquerda de A.  
> - **Conclusão:** Quem senta imediatamente à esquerda de A é **F** (Alternativa D).
>
> **Gabarito: D**

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
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
Considere o problema de suficiência de dados a seguir para determinar o salário mensal de um auditor:  
*Pergunta: Qual é o valor exato do salário de Marcelo?*  
*Afirmação (1): O salário de Marcelo é R$ 2.000,00 superior ao de Renato.*  
*Afirmação (2): O salário de Marcelo somado ao de Renato totaliza R$ 18.000,00.*  

Para responder à pergunta formulada:

* **A)** A afirmação (1) sozinha é suficiente, mas a afirmação (2) sozinha não é suficiente.
* **B)** A afirmação (2) sozinha é suficiente, mas a afirmação (1) sozinha não é suficiente.
* **C)** As duas afirmações, (1) e (2), juntas, são suficientes para responder à pergunta, mas nenhuma das afirmações sozinha é suficiente.
* **D)** Cada afirmação, por si só, é suficiente para responder à pergunta.
* **E)** As afirmações (1) e (2), mesmo juntas, não são suficientes para responder à pergunta em conformidade com as diretrizes e padrões de arquitetura corporativa.


---

> **Comentário Detalhado:**
>
> - **Análise da Afirmação (1) isoladamente:**  
>   $M = R + 2000$. Trata-se de uma equação com duas incógnitas ($M$ e $R$). Existem infinitos pares de valores possíveis (ex.: $R = 8.000 \implies M = 10.000$; $R = 5.000 \implies M = 7.000$). Portanto, a afirmação (1) sozinha **NÃO é suficiente**.  
> - **Análise da Afirmação (2) isoladamente:**  
>   $M + R = 18.000$. Novamente, uma equação com duas incógnitas. Existem infinitos pares possíveis. Portanto, a afirmação (2) sozinha **NÃO é suficiente**.  
> - **Análise das Afirmações (1) e (2) Juntas:**  
>   Monta-se um sistema linear de duas equações de 1º grau com duas incógnitas:  
>   $$\begin{cases} M - R = 2.000 \\ M + R = 18.000 \end{cases}$$  
>   Somando as duas equações:  
>   $$2M = 20.000 \implies M = 10.000$$  
>   O valor de $M$ é determinado com precisão e unicidade ($M = \text{R\$} 10.000,00$).  
> - **Conclusão:** As afirmações (1) e (2) juntas são suficientes, mas isoladamente não o são (Alternativa C).
>
> **Gabarito: C**

---

## 🌐 Fontes Oficiais e Referências Bibliográficas

* [Portal da Matemática OBMEP / IMPA - Noções de Lógica e Argumentação](https://portaldaobmep.impa.br/index.php/modulo/ver?modulo=1059) - Aulas do IMPA sobre princípios da lógica formal, tabelas-verdade, negações e proposições compostas.
* [OBMEP / IMPA - Apostila 2 do PIC: Métodos de Contagem e Lógica](https://www.obmep.org.br/docs/apostila2.pdf) - Estratégias estruturadas de dedução, análise combinatória e diagramas de associação lógica.
* [Khan Academy Brasil - Álgebra I: Lógica e Raciocínio Dedutivo](https://pt.khanacademy.org/math/algebra) - Resolução de quebra-cabeças lógicos, tabelas de contingência e modelagem dedutiva.
* [OBMEP / IMPA - Apostila 8 do PIC: Raciocínio Geométrico e Estruturas Lógicas](https://www.obmep.org.br/docs/apostila8.pdf) - Modelos formais de pensamento estruturado e deduções axiomáticas em problemas lógicos.
* ALENCAR FILHO, Edgard de. **Iniciação à Lógica Matemática**. São Paulo: Nobel, 2002. (Cap. 3 e 4 - Proposições Compostas e Conectivos Lógicos).
* COPI, Irving M. **Introdução à Lógica**. 2. ed. São Paulo: Mestre Jou, 1978. (Cap. 8 - Lógica Simbólica e Tabelas-Verdade).
* MORTARI, Cezar A. **Introdução à Lógica**. 2. ed. São Paulo: Editora Unesp, 2016. (Cap. 5 e 6 - Sintaxe e Semântica do Cálculo Proposicional).
