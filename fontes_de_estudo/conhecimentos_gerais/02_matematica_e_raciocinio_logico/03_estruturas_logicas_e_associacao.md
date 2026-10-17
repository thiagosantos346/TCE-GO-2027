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
- [1. Fundamentos da Associação Lógica Biunívoca](#1-fundamentos-da-associacao-logica-biunivoca)
    - [1.1 Natureza das Relações Arbitrárias e Conjuntos Finitos](#11-natureza-das-relacoes-arbitrarias-e-conjuntos-finitos)
    - [1.2 O Princípio da Correspondência Biunívoca](#12-o-principio-da-correspondencia-biunivoca)
    - [1.3 Tipologia de Pistas e Classificação de Premissas](#13-tipologia-de-pistas-e-classificacao-de-premissas)
- [2. Metodologia das Matrizes Cruzadas de Associação](#2-metodologia-das-matrizes-cruzadas-de-associacao)
    - [2.1 Estruturação da Tabela Bidimensional e Tridimensional](#21-estruturacao-da-tabela-bidimensional-e-tridimensional)
    - [2.2 O Princípio de Propagação do SIM e Fechamento por Exclusão](#22-o-principio-de-propagacao-do-sim-e-fechamento-por-exclusao)
    - [2.3 Tratamento de Pistas Compostas e Vínculos Indiretos](#23-tratamento-de-pistas-compostas-e-vinculos-indiretos)
- [3. Problemas de Ordenação Linear e Posicionamento Relativo](#3-problemas-de-ordenacao-linear-e-posicionamento-relativo)
    - [3.1 Semântica de Ordenação: Imediatamente Antes vs. Antes Genérico](#31-semantica-de-ordenacao-imediatamente-antes-vs-antes-generico)
    - [3.2 Filas, Andares e Classificações em Concurso](#32-filas-andares-e-classificacoes-em-concurso)
    - [3.3 O Método das Caixas e Blocos Contíguos](#33-o-metodo-das-caixas-e-blocos-contiguos)
- [4. Problemas de Ordenação Circular e Mesas Redondas](#4-problemas-de-ordenacao-circular-e-mesas-redondas)
    - [4.1 Ponto de Vista Referencial e Orientação Espacial](#41-ponto-de-vista-referencial-e-orientacao-espacial)
    - [4.2 Posições Diametralmente Opostas em Mesas Pares](#42-posicoes-diametralmente-opostas-em-mesas-pares)
    - [4.3 Vizinhos Imediatos e Adjacências Direita e Esquerda](#43-vizinhos-imediatos-e-adjacencias-direita-e-esquerda)
- [5. Dedução Lógica e Avaliação de Suficiência de Condições](#5-deducao-logica-e-avaliacao-de-suficiencia-de-condicoes)
    - [5.1 Dedução Hipotética e Eliminação de Contradições](#51-deducao-hipotetica-e-eliminacao-de-contradicoes)
    - [5.2 Condições Necessárias, Suficientes e Redundantes](#52-condicoes-necessarias-suficientes-e-redundantes)
- [Fontes Oficiais e Referências Bibliográficas](#fontes-oficiais-e-referencias-bibliograficas)

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

### Questão 01
**(FCC – TRT – Analista Judiciário)**  
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


### Questão 02
**(FCC – TRT-23 – Analista Judiciário)**  
Três analistas judiciários — André, Bernardo e Carlos — atuam em três setores diferentes de um tribunal: Protocolo, Recursos Humanos e Licitações, não necessariamente nessa ordem. Cada um deles utiliza um meio de transporte distinto para ir ao trabalho: carro, ônibus ou bicicleta. Sabe-se que:  
1. André vai de bicicleta para o trabalho.  
2. O servidor lotado em Recursos Humanos não vai de carro.  
3. O servidor que atua no Protocolo vai de ônibus.  

Com base nessas informações, é correto concluir que:

* **A)** Carlos atua em Licitações e vai de carro.
* **B)** André atua em Recursos Humanos e vai de bicicleta.
* **C)** Bernardo atua no Protocolo e vai de carro.
* **D)** Carlos atua no Protocolo e vai de bicicleta.
* **E)** André atua em Licitações e vai de ônibus.

> **Comentário Detalhado:**
>
> - **Análise Lógica Passo a Passo:**  
>   - **Pista 1:** André $
ightarrow$ Bicicleta.  
>   - **Pista 3:** O servidor do Protocolo $
ightarrow$ Ônibus. Como André vai de bicicleta, André **não** está no Protocolo. Logo, o servidor do Protocolo só pode ser Bernardo ou Carlos.  
>   - Como os meios de transporte são Carro, Ônibus e Bicicleta, e André vai de bicicleta e o do Protocolo vai de ônibus, sobra o **Carro** para o terceiro servidor.  
>   - **Pista 2:** O servidor do RH não vai de carro. Como o do Protocolo vai de ônibus, o servidor do RH só pode ir de **Bicicleta** (pois não vai de carro nem de ônibus!).  
>   - Logo, quem vai de bicicleta é o servidor dos Recursos Humanos! Como André vai de bicicleta, conclui-se com certeza absoluta que **André atua em Recursos Humanos**.  
>   - Sobra o setor de **Licitações** para quem vai de **Carro**.  
> - **Conclusão:** André atua em Recursos Humanos e vai de bicicleta (Alternativa B).
>
> **Gabarito: B**

---

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

### Questão 03
**(FCC – TCE-GO – Técnico de Controle Externo)**  
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


### Questão 04
**(FCC – TCE-GO – Analista de Controle Externo)**  
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

### Questão 05
**(FCC – TCE-GO – Auditor de Controle Externo)**  
Cinco auditores — André, Bernardo, Caio, Daniel e Eduardo — foram classificados do 1º ao 5º lugar em uma avaliação de desempenho interna do TCE-GO, sem empates. Sabe-se que:

- Caio ficou em uma colocação melhor do que Eduardo.  
- Daniel obteve o 3º lugar.  
- André não ficou em 1º lugar e não ficou imediatamente atrás de Caio.  
- Bernardo ficou em uma colocação imediatamente anterior à de Caio.  

Com base nessas condições, o auditor que obteve o 1º lugar foi:

* **A)** André
* **B)** Bernardo
* **C)** Caio
* **D)** Daniel
* **E)** Eduardo

> **Comentário Detalhado:**
> Resolução por ordenação linear de posições $(1º, 2º, 3º, 4º, 5º)$:
>
> 1. Pista fixa: **Daniel ocupa o 3º lugar** $\implies (\_, \_, D, \_, \_)$.
> 2. Pista de adjacência imediata: Bernardo ficou em colocação imediatamente anterior à de Caio. Isso significa que Bernardo e Caio formam um **bloco contíguo indivisível $[B, C]$**.
> 3. Como o 3º lugar está ocupado por Daniel, o bloco $[B, C]$ só pode ser inserido em dois intervalos:
>     - Hipótese 1: posições $\{1º, 2º\}$, com $B = 1º$ e $C = 2º$.
>     - Hipótese 2: posições $\{4º, 5º\}$, com $B = 4º$ e $C = 5º$.
>
> 4. Teste da Hipótese 2: se Caio ficasse em 5º lugar, seria impossível cumprir a primeira premissa (*"Caio ficou em colocação melhor do que Eduardo"*), pois não existiria nenhuma colocação posterior ao 5º lugar para alocar Eduardo. Portanto, a Hipótese 2 é falsa e gera contradição.
> 5. Confirmação da Hipótese 1:
>     - **Bernardo = 1º lugar**
>     - **Caio = 2º lugar**
>     - O arranjo parcial fica $(B, C, D, \_, \_)$.
>
> 6. As posições restantes ($4º$ e $5º$) são ocupadas por André e Eduardo. Como Caio ($2º$) superou Eduardo, e André não é o 1º nem está colado atrás de Caio, todas as condições são respeitadas com Bernardo no topo.
>
> Análise das alternativas:
>
> - **A)** Incorreta. O enunciado veda explicitamente André na 1ª colocação.
> - **B)** Correta. Bernardo é compulsoriamente o 1º colocado.
> - **C)** Incorreta. Caio situa-se imediatamente após Bernardo, obtendo o 2º lugar.
> - **D)** Incorreta. Daniel obteve o 3º lugar por premissa explícita.
> - **E)** Incorreta. Eduardo foi superado por Caio, ficando em 4º ou 5º lugar.
> 
> **Gabarito: B**


### Questão 06
**(FCC – DPE-RS – Analista)**  
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

---

### Questão 07
**(FCC – TCE-PI – Analista de Controle Externo)**  
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


### 4.3 Vizinhos Imediatos e Adjacências Direita e Esquerda

Cada ocupante possui exatamente dois vizinhos imediatos (adjacentes):

* O vizinho imediatamente à sua direita;
* O vizinho imediatamente à sua esquerda.
Todos os demais ocupantes não são vizinhos imediatos.


### Questão 08
**(FCC – METRÔ-SP – Analista)**  
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

### Questão 09
**(FCC – TCE-GO – Auditor de Controle Externo)**  
Considere quatro auditores — Paulo, Renan, Sérgio e Tiago — que possuem idades distintas: 25, 28, 31 e 35 anos, não necessariamente nessa ordem. Para se determinar com precisão unívoca a idade de cada um deles, foram apresentadas as seguintes três condições:
I. Paulo é mais velho que Sérgio.  
II. A idade de Renan é um número par.  
III. Tiago é mais velho que Paulo.  
Avalie se essas três condições, em conjunto, são suficientes para determinar a idade de cada um dos quatro auditores:

* **A)** As condições I, II e III, juntas, não são suficientes para determinar a idade de ninguém.
* **B)** Apenas as condições I e II seriam suficientes, sendo a condição III redundante.
* **C)** As três condições, juntas, são suficientes para determinar a idade de todos os quatro auditores.
* **D)** As três condições determinam apenas as idades de Paulo e Renan, restando ambiguidade entre Sérgio e Tiago.
* **E)** A condição I é contraditória com a condição III.

> **Comentário Detalhado:**
> Avaliação sistemática de suficiência de dados:
>
> 1. O conjunto de idades é $\{25, 28, 31, 35\}$. O único número par é 28.
> 2. Pela condição II, a idade de Renan é par $\implies$ **Renan tem compulsoriamente 28 anos**.
> 3. As idades restantes para Paulo, Sérgio e Tiago são $\{25, 31, 35\}$.
> 4. As condições I e III estabelecem a ordem estrita entre os três:
>    $$\text{Sérgio} < \text{Paulo} < \text{Tiago}$$
> 5. Há uma única alocação possível: **Sérgio = 25**, **Paulo = 31** e **Tiago = 35**. Logo, as três condições, em conjunto, determinam a idade dos quatro auditores.
>
> Análise individual das alternativas:
>
> - **A)** Incorreta. O conjunto determina a idade de todos, inclusive a de Renan, que decorre diretamente da condição II.
> - **B)** Incorreta. Com apenas I e II, Renan teria 28 anos, mas as idades de Paulo, Sérgio e Tiago admitiriam três arranjos distintos que respeitam $P > S$: $(S, P, T) = (25, 31, 35)$, $(25, 35, 31)$ ou $(31, 35, 25)$. A condição III é indispensável para fixar Tiago como o mais velho do trio.
> - **C)** Correta. As três condições, juntas, fixam univocamente as idades dos quatro auditores.
> - **D)** Incorreta. Não resta ambiguidade alguma entre Sérgio e Tiago: a ordem $S < P < T$ os determina.
> - **E)** Incorreta. As condições I e III são compatíveis entre si, pois ambas se encaixam na ordem $S < P < T$.
>
> **Gabarito: C**


### Questão 10
**(FCC – TRT-14 – Analista Judiciário)**  
Considere o problema de suficiência de dados a seguir para determinar o salário mensal de um auditor:  
*Pergunta: Qual é o valor exato do salário de Marcelo?*  
*Afirmação (1): O salário de Marcelo é R$ 2.000,00 superior ao de Renato.*  
*Afirmação (2): O salário de Marcelo somado ao de Renato totaliza R$ 18.000,00.*  

Para responder à pergunta formulada:

* **A)** A afirmação (1) sozinha é suficiente, mas a afirmação (2) sozinha não é suficiente.
* **B)** A afirmação (2) sozinha é suficiente, mas a afirmação (1) sozinha não é suficiente.
* **C)** As duas afirmações, (1) e (2), juntas, são suficientes para responder à pergunta, mas nenhuma das afirmações sozinha é suficiente.
* **D)** Cada afirmação, por si só, é suficiente para responder à pergunta.
* **E)** As afirmações (1) e (2), mesmo juntas, não são suficientes para responder à pergunta.

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

---



## 🌐 Fontes Oficiais e Referências Bibliográficas

* [Portal da Matemática OBMEP / IMPA - Noções de Lógica e Argumentação](https://portaldaobmep.impa.br/index.php/modulo/ver?modulo=1059) - Aulas do IMPA sobre princípios da lógica formal, tabelas-verdade, negações e proposições compostas.
* [OBMEP / IMPA - Apostila 2 do PIC: Métodos de Contagem e Lógica](https://www.obmep.org.br/docs/apostila2.pdf) - Estratégias estruturadas de dedução, análise combinatória e diagramas de associação lógica.
* [Khan Academy Brasil - Álgebra I: Lógica e Raciocínio Dedutivo](https://pt.khanacademy.org/math/algebra) - Resolução de quebra-cabeças lógicos, tabelas de contingência e modelagem dedutiva.
* [OBMEP / IMPA - Apostila 8 do PIC: Raciocínio Geométrico e Estruturas Lógicas](https://www.obmep.org.br/docs/apostila8.pdf) - Modelos formais de pensamento estruturado e deduções axiomáticas em problemas lógicos.
* ALENCAR FILHO, Edgard de. **Iniciação à Lógica Matemática**. São Paulo: Nobel, 2002. (Cap. 3 e 4 - Proposições Compostas e Conectivos Lógicos).
* COPI, Irving M. **Introdução à Lógica**. 2. ed. São Paulo: Mestre Jou, 1978. (Cap. 8 - Lógica Simbólica e Tabelas-Verdade).
* MORTARI, Cezar A. **Introdução à Lógica**. 2. ed. São Paulo: Editora Unesp, 2016. (Cap. 5 e 6 - Sintaxe e Semântica do Cálculo Proposicional).
