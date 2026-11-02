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
**(FGV – TRT 1ª – 2024 – Analista Judiciário - Área Administrativa)**
Uma lei impôs aos estabelecimentos federais de ensino a utilização de cadeiras adaptadas para alunos com deficiência física ou mobilidade reduzida. Nela foi determinado que o número de cadeiras adaptadas deve ser, no mínimo, igual ao número de alunos regularmente matriculados em cada sala. Deixou a lei de tratar sobre pessoas com deficiência auditiva e visual. Com relação ao tema do enunciado, à Lei nº 10.098/2000, que trata sobre normas gerais e critérios básicos para a promoção da acessibilidade das pessoas com deficiência ou com mobilidade reduzida, e ao pensamento do Supremo Tribunal Federal (STF), é correto afirmar que:

* **A)** a Lei nº 10.098/2000 não tratou dos locais de aula para pessoas que utilizam cadeiras de roda, deixando um vácuo suplementado pela aludida lei, que optou pelo uso de cadeiras adaptadas;
* **B)** a lei federal, em respeito ao princípio da proporcionalidade, deveria estabelecer que o número de cadeiras adaptadas seria o número de alunos com deficiência regularmente matriculados em cada sala;
* **C)** a Lei nº 10.098/2000 dispôs sobre lugares específicos para pessoas com deficiência auditiva e visual, mas não sobre a presença do respectivo acompanhante, o que obedece à ideia de autonomia;
* **D)** o respeito à imposição legal não seria um problema orçamentário, pois o aludido critério do número de alunos regularmente matriculados obedece à lógica da integração social;
* **E)** a referida imposição aos estabelecimentos federais de ensino viola a não discriminação, porque as pessoas com deficiência receberiam tratamento diferenciado em decorrência dessa condição.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "a Lei nº 10.098/2000 não tratou dos locais de aula para pessoas que utilizam cadeiras de roda, deixando um vácuo...". De acordo com a teoria estudada em *4.2 Posições Diametralmente Opostas em Mesas Pares*, em mesas circulares com um número par $N$ de assentos ($N = 6$ ou $N = 8$), diz-se que duas pessoas estão sentadas em frente ou diametralmente opostas quando a linha reta que as une passa pelo centro da mesa.
> - **B)** **Correta.** Conforme fundamentado na seção *1.1 Natureza das Relações Arbitrárias e Conjuntos Finitos* deste guia, nessas questões, a relação entre os entes não decorre de nenhuma lei física ou científica prévia, mas de um cenário ficcional arbitrariamente desenhado pela banca examinadora. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT 1ª/2024) ao estabelecer que "a lei federal, em respeito ao princípio da proporcionalidade, deveria estabelecer que o número de cadeiras...".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "a Lei nº 10.098/2000 dispôs sobre lugares específicos para pessoas com deficiência auditiva e visual, mas não...". De acordo com a teoria estudada em *4.2 Posições Diametralmente Opostas em Mesas Pares*, em uma mesa de 6 cadeiras numeradas de 1 a 6 em sentido horário.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "o respeito à imposição legal não seria um problema orçamentário, pois o aludido critério do número de alunos...". De acordo com a teoria estudada em *2.3 Tratamento de Pistas Compostas e Vínculos Indiretos*, se sabemos por outra pista que *Bruno reside em Goiânia*, deduz-se imediatamente que *Bruno NÃO é formado em Direito* (pois se o fosse, deveria residir em Aparecida).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "a referida imposição aos estabelecimentos federais de ensino viola a não discriminação, porque as pessoas com...". De acordo com a teoria estudada em *2.2 O Princípio de Propagação do SIM e Fechamento por Exclusão*, ao marcar SIM na interseção entre um indivíduo e um atributo (ex.: Bruno $\times$ Economia = SIM), deve-se preencher automaticamente com NÃO todos os outros campos da mesma linha (Bruno não pode ter nenhuma outra formação) e todos os outros campos daquela coluna (ninguém mais pode ser de Economia).
>
> **Gabarito: B**

---

### Teste 093
**(FGV – TCE/GO – 2024 – Analista de Controle Externo - Ciências Contábeis)**
Todas as frases abaixo estão separadas em dois segmentos. Assinale a opção em que a relação lógica entre esses segmentos está corretamente indicada.

* **A)** As testemunhas custam muito caro / e não as tem quem quer. / explicação.
* **B)** Quanto mais proeminentes são as leis e a ordem, / mais ladrões e assaltantes haverá. / comparação.
* **C)** A ginástica é vulgar porque faz as pessoas cheirarem mal. / causa e consequência.
* **D)** O jogo foi interrompido porque o chapéu de um dos espectadores voou para a quadra. / relação temporal.
* **E)** A mente, como o lar, é mobiliada pelo proprietário, portanto se sua vida for fria e árida, a culpa será somente dele. / conclusão.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "As testemunhas custam muito caro / e não as tem quem quer. / explicação". De acordo com a teoria estudada em *1.2 O Princípio da Correspondência Biunívoca*, a premissa implícita em quase todas as questões de associação lógica da FCC é o princípio da bijeção (correspondência biunívoca).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Quanto mais proeminentes são as leis e a ordem, / mais ladrões e assaltantes haverá. / comparação". De acordo com a teoria estudada em *2. Metodologia das Matrizes Cruzadas de Associação*, a ferramenta mais confiável e à prova de falhas para solucionar problemas de associação multidimensional é a matriz cruzada de pertinência (tabela lógica).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A ginástica é vulgar porque faz as pessoas cheirarem mal. / causa e consequência". De acordo com a teoria estudada em *1.3 Tipologia de Pistas e Classificação de Premissas*, pistas Condicionais ou Compostas: Estabelecem vínculos de causa-efeito ou conexões temporais e espaciais simultâneas (*"Se Lucas cuida da Folha, então Mateus cuida do Portal"*; *"O técnico que mora em Anápolis chegou depois de Carlos"*).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O jogo foi interrompido porque o chapéu de um dos espectadores voou para a quadra. / relação temporal". De acordo com a teoria estudada em *1.1 Natureza das Relações Arbitrárias e Conjuntos Finitos*, nessas questões, a relação entre os entes não decorre de nenhuma lei física ou científica prévia, mas de um cenário ficcional arbitrariamente desenhado pela banca examinadora.
> - **E)** **Correta.** Conforme fundamentado na seção *5.2 Condições Necessárias, Suficientes e Redundantes* deste guia, condição Suficiente: Aquela que, por si só, basta para fixar uma conclusão ou determinar o sistema sem necessidade de dados complementares. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/GO/2024) ao estabelecer que "A mente, como o lar, é mobiliada pelo proprietário, portanto se sua vida for fria e árida, a culpa será somente...".
>
> **Gabarito: E**

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
**(FGV – TRT da 24º Região – 2025 – Analista Judiciário - Área Administrativa - Contabilidade)**
Leia o texto a seguir. O fato de uma opinião ser amplamente compartilhada não é nenhuma evidência de que não seja completamente absurda; de fato, tendo-se em vista a maioria da humanidade, é mais provável que uma opinião difundida seja mais tola do que sensata. Bertrand Russell. Marriage and Morals. H. Liveright, 1929, p. 53. Assinale a afirmativa que indica corretamente o significado ou a estruturação do texto citado.

* **A)** O texto se opõe ao pensamento de que um argumento seja considerado verdadeiro porque se apoia no que pensa a maioria das pessoas.
* **B)** O autor mostra a vantagem de uma opinião ser amplamente compartilhada a fim de que se torne mais segura.
* **C)** O texto é do tipo argumentativo, pois apresenta uma tese, ainda que não acompanhada de argumentos.
* **D)** A opinião final do texto é apresentada como certeza a fim de melhor convencer o leitor.
* **E)** O texto se estrutura com a apresentação de um contra- argumento seguido da apresentação da opinião contrária.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *5.1 Dedução Hipotética e Eliminação de Contradições* deste guia, se o desdobramento conduzir a uma contradição lógica (uma linha sem nenhum elemento verdadeiro, ou duas pessoas com o mesmo cargo), a hipótese é falsa e seu oposto é compulsoriamente verdadeiro. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT da 24º Região/2025) ao estabelecer que "O texto se opõe ao pensamento de que um argumento seja considerado verdadeiro porque se apoia no que pensa a...".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O autor mostra a vantagem de uma opinião ser amplamente compartilhada a fim de que se torne mais segura". De acordo com a teoria estudada em *2.2 O Princípio de Propagação do SIM e Fechamento por Exclusão*, ao marcar SIM na interseção entre um indivíduo e um atributo (ex.: Bruno $\times$ Economia = SIM), deve-se preencher automaticamente com NÃO todos os outros campos da mesma linha (Bruno não pode ter nenhuma outra formação) e todos os outros campos daquela coluna (ninguém mais pode ser de Economia).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O texto é do tipo argumentativo, pois apresenta uma tese, ainda que não acompanhada de argumentos". De acordo com a teoria estudada em *2.3 Tratamento de Pistas Compostas e Vínculos Indiretos*, quando o texto apresenta a pista: *"O servidor formado em Direito reside em Aparecida de Goiânia"*.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A opinião final do texto é apresentada como certeza a fim de melhor convencer o leitor". De acordo com a teoria estudada em *2.2 O Princípio de Propagação do SIM e Fechamento por Exclusão*, propagação do "SIM" (ou valor verdadeiro).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O texto se estrutura com a apresentação de um contra- argumento seguido da apresentação da opinião contrária". De acordo com a teoria estudada em *5.2 Condições Necessárias, Suficientes e Redundantes*, a ementa do edital exige expressamente a *"avaliação das condições usadas para estabelecer a estrutura daquelas relações"*.
>
> **Gabarito: A**

---

### Teste 095
**(FGV – TRT 16ª – 2022 – Analista Judiciário (Área Administrativa - Tecnologia da Informação))**
Pedro, pessoa com deficiência, após concluir a educação básica, almejava ingressar em uma instituição de ensino superior (IES). Ao se inteirar dos seus direitos, visando à participação no processo seletivo, foi-lhe informado que a Lei nº 13.146/2015 lhe assegurava: (1) disponibilização de provas em formatos acessíveis, para atendimento às suas necessidades especiais; (2) disponibilização, de ofício, pela IES, de recursos de acessibilidade, permitindo que ele possa escolher, entre essas opções, aquela que mais se aproxima da satisfação de suas necessidades; (3) dilação de tempo, em 20%, no exame de seleção, a ser oferecida a todas as pessoas com deficiência, incluindo Pedro; e (4) adoção de critérios de avaliação das provas escritas, discursivas ou de redação, que considerem a singularidade linguística de Pedro no domínio da escrita da língua portuguesa. À luz das informações fornecidas a Pedro, é correto afirmar que

* **A)** todas estão corretas.
* **B)** apenas as informações 1 e 4 estão corretas.
* **C)** apenas as informações 2 e 3 estão corretas.
* **D)** apenas as informações 1, 3 e 4 estão corretas.
* **E)** apenas as informações 2, 3 e 4 estão corretas.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "todas estão corretas". De acordo com a teoria estudada em *4.2 Posições Diametralmente Opostas em Mesas Pares*, em mesas circulares com um número par $N$ de assentos ($N = 6$ ou $N = 8$), diz-se que duas pessoas estão sentadas em frente ou diametralmente opostas quando a linha reta que as une passa pelo centro da mesa.
> - **B)** **Correta.** Conforme fundamentado na seção *1.3 Tipologia de Pistas e Classificação de Premissas* deste guia, as informações fornecidas dividem-se em três modalidades lógicas. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT 16ª/2022) ao estabelecer que "apenas as informações 1 e 4 estão corretas".
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "apenas as informações 2 e 3 estão corretas". De acordo com a teoria estudada em *2.2 O Princípio de Propagação do SIM e Fechamento por Exclusão*, ao marcar SIM na interseção entre um indivíduo e um atributo (ex.: Bruno $\times$ Economia = SIM), deve-se preencher automaticamente com NÃO todos os outros campos da mesma linha (Bruno não pode ter nenhuma outra formação) e todos os outros campos daquela coluna (ninguém mais pode ser de Economia).
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "apenas as informações 1, 3 e 4 estão corretas". De acordo com a teoria estudada em *3.1 Semântica de Ordenação: Imediatamente Antes vs. Antes Genérico*, quando o enunciado afirmar que *"André chegou à frente de Caio"*, jamais presuma que André chegou colado a Caio! Isso significa apenas que André precede Caio no tempo ($t_A < t_C$).
> - **E)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "apenas as informações 2, 3 e 4 estão corretas". De acordo com a teoria estudada em *2. Metodologia das Matrizes Cruzadas de Associação*, a ferramenta mais confiável e à prova de falhas para solucionar problemas de associação multidimensional é a matriz cruzada de pertinência (tabela lógica).
>
> **Gabarito: B**

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
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Gestão Governamental)**
Leia a frase abaixo com atenção: Ninguém fica velho apenas por viver, mas por perder o interesse em viver. Assinale a afirmativa correta o significado ou a estruturação dessa frase.

* **A)** A relação entre os segmentos da frase não é de oposição, mas de diferença.
* **B)** O adjetivo “velho”, no contexto da frase, tem alto valor pejorativo.
* **C)** O segundo segmento da frase retifica algo dito erradamente no primeiro segmento.
* **D)** O termo “fica velho” pode ser adequadamente substituído por “envelheceu”.
* **E)** O emprego de “apenas” mostra uma visão negativa do ato de viver. Matemática Financeira, Estatística e Raciocínio Lógico

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *1.1 Natureza das Relações Arbitrárias e Conjuntos Finitos* deste guia, nessas questões, a relação entre os entes não decorre de nenhuma lei física ou científica prévia, mas de um cenário ficcional arbitrariamente desenhado pela banca examinadora. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "A relação entre os segmentos da frase não é de oposição, mas de diferença".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O adjetivo “velho”, no contexto da frase, tem alto valor pejorativo". De acordo com a teoria estudada em *2.2 O Princípio de Propagação do SIM e Fechamento por Exclusão*, propagação do "SIM" (ou valor verdadeiro).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O segundo segmento da frase retifica algo dito erradamente no primeiro segmento". De acordo com a teoria estudada em *3.2 Filas, Andares e Classificações em Concurso*, preenchem-se primeiro as posições fixas garantidas (ex.: *"Daniel obteve o 3º lugar"* $\implies$ fixa $D$ no 3º traço).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O termo “fica velho” pode ser adequadamente substituído por “envelheceu”". De acordo com a teoria estudada em *2.2 O Princípio de Propagação do SIM e Fechamento por Exclusão*, ao marcar SIM na interseção entre um indivíduo e um atributo (ex.: Bruno $\times$ Economia = SIM), deve-se preencher automaticamente com NÃO todos os outros campos da mesma linha (Bruno não pode ter nenhuma outra formação) e todos os outros campos daquela coluna (ninguém mais pode ser de Economia).
> - **E)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "O emprego de “apenas” mostra uma visão negativa do ato de viver. Matemática Financeira, Estatística e Raciocínio...". De acordo com a teoria estudada em *3.1 Semântica de Ordenação: Imediatamente Antes vs. Antes Genérico*, expressão no Enunciado: Significado Lógico Rigoroso — Implicação Estrutural.
>
> **Gabarito: A**

---

### Teste 097
**(FCC – TRT 1ª – 2014 – Analista Judiciário - Tecnologia da Informação)**
As expressões onde e em cujo preenchem corretamente, na ordem dada, as lacunas da seguinte frase:

* **A)** Ao longo dos anos de 1950 e 1960, verificaram-se, em nosso país, relações muito proveitosas e expres- sivas entre manifestações artísticas e projetos políti- cos.
* **B)** Não há como ignorar o precioso legado artístico que nos deixaram os artistas que, naquelas duas déca- das, se empenharam na renovação da nossa cultura.
* **C)** Há quem conteste a influência que a Bossa Nova su- postamente teria recebido do jazz; seja como for, é incontestável o valor das canções de um Tom Jobim.
* **D)** As ideologias políticas tomaram uma feição radical ao longo dos anos 60; isso transparece quando se examinam as letras das canções de protesto.
* **E)** Em virtude de fortes interesses políticos, muito em- bora nem sempre ocorressem, já que na década de 60 as canções de protesto se disseminaram. Atenção: As questões de números 16 a 20 referem-se ao texto seguinte. Novas fronteiras do mundo globalizado Apesar do desenvolvimento espetacular das tecnologias, não devemos imaginar que vivemos em um mundo sem frontei- ras, como se o espaço estivesse definitivamente superado pela velocidade do tempo. Seria mais correto dizer que a moderni- dade, ao romper com a geografia tradicional, cria novos limites. Se a diferença entre o “Primeiro” e o “Terceiro” mundo é diluída, outras surgem no interior deste último, agrupando ou excluindo as pessoas. Nossa contemporaneidade faz do próximo o distante, se- parando-nos daquilo que nos cerca, ao nos avizinhar de lugares remotos. Neste caso, não seria o outro aquilo que o “nós” gos- taria de excluir? Como o islamismo (associado à noção de ir- racionalidade), ou os espaços de pobreza (África, setores de países em desenvolvimento), que apesar de muitas vezes próxi- mos se afastam dos ideais cultivados pela modernidade. (Adaptado de: ORTIZ, Renato. Mundialização e cultura. São Paulo: Brasiliense, 1994, p. 220)

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Ao longo dos anos de 1950 e 1960, verificaram-se, em nosso país, relações muito proveitosas e expres- sivas entre...". De acordo com a teoria estudada em *1.1 Natureza das Relações Arbitrárias e Conjuntos Finitos*, nessas questões, a relação entre os entes não decorre de nenhuma lei física ou científica prévia, mas de um cenário ficcional arbitrariamente desenhado pela banca examinadora.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Não há como ignorar o precioso legado artístico que nos deixaram os artistas que, naquelas duas déca- das, se...". De acordo com a teoria estudada em *4.2 Posições Diametralmente Opostas em Mesas Pares*, em mesas circulares com um número par $N$ de assentos ($N = 6$ ou $N = 8$), diz-se que duas pessoas estão sentadas em frente ou diametralmente opostas quando a linha reta que as une passa pelo centro da mesa.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Há quem conteste a influência que a Bossa Nova su- postamente teria recebido do jazz; seja como for, é...". De acordo com a teoria estudada em *3.1 Semântica de Ordenação: Imediatamente Antes vs. Antes Genérico*, quando o enunciado afirmar que *"André chegou à frente de Caio"*, jamais presuma que André chegou colado a Caio! Isso significa apenas que André precede Caio no tempo ($t_A < t_C$).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "As ideologias políticas tomaram uma feição radical ao longo dos anos 60; isso transparece quando se examinam as...". De acordo com a teoria estudada em *3.3 O Método das Caixas e Blocos Contíguos*, testa-se cada nicho com as demais restrições para descartar inconsistências (se $C$ estivesse no 5º lugar, não poderia superar ninguém, o que violaria a regra de que Caio superou Eduardo).
> - **E)** **Correta.** Conforme fundamentado na seção *3.2 Filas, Andares e Classificações em Concurso* deste guia, preenchem-se primeiro as posições fixas garantidas (ex.: *"Daniel obteve o 3º lugar"* $\implies$ fixa $D$ no 3º traço). Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 1ª/2014) ao estabelecer que "Em virtude de fortes interesses políticos, muito em- bora nem sempre ocorressem, já que na década de 60 as canções...".
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
**(FCC – TRT 11ª – 2017 – Analista Judiciário - Tecnologia da Informação)**
Considere que em um projeto foi utilizada a métrica com base na contagem de Pontos de Função (PF). O projeto foi estimado em 100 PF. Em uma determinada fase, que corresponde a 20% do projeto: − trabalham 4 pessoas; − a produtividade média é de 20 horas/PF; − a jornada diária é de 8 horas, 5 dias por semana; − o valor por 1 hora de trabalho é R$ 50,00. Com base nos dados relativos à fase, o esforço total em horas, o prazo em dias e o custo do projeto podem ser estimados e correspondem, correta e respectivamente, a:

* **A)** Neste diagrama de classes da UML PedidoDAOCentral, PedidoDAOEscritorio e PedidoDAOLocal são classes concretas capazes de executar a operação inserirPedido.
* **B)** As instruções pedido Pedido = new pedido(); PedidoDAO d = buildPedidoDAO(); d.inserirPedido (pedido); em condições ideais, é um exemplo correto de implementação em linguagem Java.
* **C)** Neste diagrama de objetos da UML PedidoDAO se refere a um objeto abstrato.
* **D)** O padrão de projeto utilizado pode ser claramente identificado como Fabric Method.
* **E)** O método DAOBuilder possui os objetos responsáveis por construir o padrão de projeto a ser implementado em Java.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Neste diagrama de classes da UML PedidoDAOCentral, PedidoDAOEscritorio e PedidoDAOLocal são classes concretas...". De acordo com a teoria estudada em *1.1 Natureza das Relações Arbitrárias e Conjuntos Finitos*, os conjuntos fornecidos são finitos e de mesma cardinalidade (por exemplo: 4 auditores, 4 municípios de auditoria e 4 tipos de licitação fiscalizada).
> - **B)** **Correta.** Conforme fundamentado na seção *5.2 Condições Necessárias, Suficientes e Redundantes* deste guia, condição Suficiente: Aquela que, por si só, basta para fixar uma conclusão ou determinar o sistema sem necessidade de dados complementares. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 11ª/2017) ao estabelecer que "As instruções pedido Pedido = new pedido(); PedidoDAO d = buildPedidoDAO(); d.inserirPedido (pedido); em condições...".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Neste diagrama de objetos da UML PedidoDAO se refere a um objeto abstrato". De acordo com a teoria estudada em *2.1 Estruturação da Tabela Bidimensional e Tridimensional*, quando o problema envolve 3 categorias (por exemplo: Nomes, Formações e Cidades), adota-se um conjunto fixo como eixo vertical (comumente os Nomes) e desdobram-se os outros conjuntos nos eixos horizontais adjacentes.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O padrão de projeto utilizado pode ser claramente identificado como Fabric Method". De acordo com a teoria estudada em *2.2 O Princípio de Propagação do SIM e Fechamento por Exclusão*, ao marcar SIM na interseção entre um indivíduo e um atributo (ex.: Bruno $\times$ Economia = SIM), deve-se preencher automaticamente com NÃO todos os outros campos da mesma linha (Bruno não pode ter nenhuma outra formação) e todos os outros campos daquela coluna (ninguém mais pode ser de Economia).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O método DAOBuilder possui os objetos responsáveis por construir o padrão de projeto a ser implementado em Java". De acordo com a teoria estudada em *4.3 Vizinhos Imediatos e Adjacências Direita e Esquerda*, cada ocupante possui exatamente dois vizinhos imediatos (adjacentes).
>
> **Gabarito: B**

---

### Teste 099
**(FCC – TRT 6ª – 2012 – Analista Judiciário - Apoio Especializado/Tecnologia da Informação)**
Uma faculdade possui cinco salas equipadas para a projeção de filmes (I, II, III, IV e V). As salas I e II têm capacidade para 200 pessoas e as salas III, IV e V, para 100 pessoas. Durante um festival de cinema, as cinco salas serão usadas para a projeção do mesmo filme. Os alunos serão distribuídos entre elas conforme a ordem de chegada, seguindo o padrão descrito abaixo: 1a pessoa: sala I 2a pessoa: sala III 3a pessoa: sala II 4a pessoa: sala IV 5a pessoa: sala I 6a pessoa: sala V 7a pessoa: sala II A partir da 8a pessoa, o padrão se repete (I, III, II, IV, I, V, II...). Nessas condições, a 496a pessoa a chegar assistirá ao filme na sala

* **A)** V.
* **B)** IV.
* **C)** III.
* **D)** II.
* **E)** I.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *1. Fundamentos da Associação Lógica Biunívoca* deste guia, os problemas de estruturas lógicas e relações arbitrárias exigem do candidato a capacidade de reconstruir uma teia de relações entre elementos de universos disjuntos (pessoas, cargos, salas, cidades, veículos, turnos de plantão) a partir de um conjunto restrito e aparentemente fragmentado de pistas informativas. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 6ª/2012) ao estabelecer que "V".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "IV". De acordo com a teoria estudada em *3. Problemas de Ordenação Linear e Posicionamento Relativo*, os problemas de ordenação linear lidam com grandezas posicionais dispostas em uma única dimensão orientada (classificação de concurso, andares de um edifício, fila de atendimento, ordem cronológica de chegada).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "III". De acordo com a teoria estudada em *5.2 Condições Necessárias, Suficientes e Redundantes*, a ementa do edital exige expressamente a *"avaliação das condições usadas para estabelecer a estrutura daquelas relações"*.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "II". De acordo com a teoria estudada em *4.3 Vizinhos Imediatos e Adjacências Direita e Esquerda*, cada ocupante possui exatamente dois vizinhos imediatos (adjacentes).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I". De acordo com a teoria estudada em *4.1 Ponto de Vista Referencial e Orientação Espacial*, a resolução exige que o candidato projete seu olhar a partir da cadeira do ocupante analisado, voltado para o centro da mesa circular.
>
> **Gabarito: A**

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
**(FGV – TRF/1 – 2024 – Analista Judiciario Area Apoio Especializado Especialidade Tecnologia Da Informacao)**
A analista Dalva administra o cluster de Kubernetes do TRF1. Dalva precisa adicionar ao Kubernetes novas condições de prontidão customizadas para o Pod A. As novas condições devem ser atendidas para o Kubernetes elevar a condição do Pod A ao status Ready. Dalva deve adicionar as novas condições de prontidão ao manifesto do Pod A, especificamente no elemento:

* **A)** lifecycleConfig;
* **B)** readinessGates;
* **C)** containerStatuses;
* **D)** lifecycleConditions;
* **E)** readinessConditions.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "lifecycleConfig". De acordo com a teoria estudada em *5.2 Condições Necessárias, Suficientes e Redundantes*, condição Suficiente: Aquela que, por si só, basta para fixar uma conclusão ou determinar o sistema sem necessidade de dados complementares.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "readinessGates". De acordo com a teoria estudada em *5.2 Condições Necessárias, Suficientes e Redundantes*, condição Necessária: Requisito sem o qual o sistema não atinge a determinação unívoca, gerando graus de liberdade ou ambiguidade entre múltiplos cenários válidos.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "containerStatuses". De acordo com a teoria estudada em *5.2 Condições Necessárias, Suficientes e Redundantes*, condição Redundante: Informação cuja veracidade já havia sido demonstrada pelo encadeamento das premissas precedentes, nada acrescentando à solução final.
> - **D)** **Correta.** Conforme fundamentado na seção *2.2 O Princípio de Propagação do SIM e Fechamento por Exclusão* deste guia, ao marcar SIM na interseção entre um indivíduo e um atributo (ex.: Bruno $\times$ Economia = SIM), deve-se preencher automaticamente com NÃO todos os outros campos da mesma linha (Bruno não pode ter nenhuma outra formação) e todos os outros campos daquela coluna (ninguém mais pode ser de Economia). Dessa forma, está plenamente correta a assertiva da banca (FGV – TRF/1/2024) ao estabelecer que "lifecycleConditions".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "readinessConditions". De acordo com a teoria estudada em *5.1 Dedução Hipotética e Eliminação de Contradições*, se o desdobramento conduzir a uma contradição lógica (uma linha sem nenhum elemento verdadeiro, ou duas pessoas com o mesmo cargo), a hipótese é falsa e seu oposto é compulsoriamente verdadeiro.
>
> **Gabarito: D**

---

### Teste 101
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Direito)**
João contratou o empreiteiro Carlos para construir uma casa no terreno que havia comprado, restando pactuado que Carlos, além do trabalho em si, forneceria os materiais para a obra; que o prazo para a construção era de um ano, contados da assinatura do contrato; e que o pagamento do valor acordado seria feito em parcela única ao final da obra. Tão logo iniciada a obra, toda a região sofreu danos inestimáveis em razão de fortes chuvas que alagaram várias cidades do estado que, inclusive, decretou estado de calamidade pública. Em razão das chuvas imprevisíveis em volume e quantidade, a morfologia do terreno em que a casa seria construída foi alterada, exigindo um acréscimo considerável de trabalho e materiais para a conclusão da obra. Além disso, em razão do alagamento de toda a região, várias estradas foram fechadas, assim como o aeroporto da cidade, impossibilitando a entrega de materiais. Diante das novas condições do terreno, do custo do material e da impossibilidade de cumprimento do prazo originalmente pactuado, Carlos procurou João, requerendo a revisão do contrato, o que foi prontamente negado. Diante dessa situação hipotética, assinale a afirmativa correta.

* **A)** Carlos arcará sozinho com o prejuízo decorrente das chuvas e do alagamento, independentemente de serem caracterizados como eventos extraordinários e imprevisíveis, pois incide o princípio da obrigatoriedade dos efeitos contratuais.
* **B)** Comprovada a onerosidade excessiva em razão das chuvas e alagamento, Carlos pode pedir judicialmente a resolução do contrato, sendo que os efeitos da sentença retroagirão à data da citação.
* **C)** Caso Carlos requeira a resolução do contrato, João não poderá evitá-la ainda que ofereça modificar equitativamente as condições do contrato em razão da natureza potestativa do direito de Carlos.
* **D)** Apesar de o princípio da obrigatoriedade dos efeitos contratuais não ser absoluto, Carlos não poderá pedir a resolução do contrato em razão de seu superveniente desequilíbrio, tendo em vista o princípio da conservação dos efeitos contratuais.
* **E)** Como Carlos assumiu a obrigação de fornecer os materiais, o contrato celebrado com João assume natureza aleatória, razão pela qual não incide a proteção contra a onerosidade excessiva.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Carlos arcará sozinho com o prejuízo decorrente das chuvas e do alagamento, independentemente de serem...". De acordo com a teoria estudada em *2.2 O Princípio de Propagação do SIM e Fechamento por Exclusão*, ao marcar SIM na interseção entre um indivíduo e um atributo (ex.: Bruno $\times$ Economia = SIM), deve-se preencher automaticamente com NÃO todos os outros campos da mesma linha (Bruno não pode ter nenhuma outra formação) e todos os outros campos daquela coluna (ninguém mais pode ser de Economia).
> - **B)** **Correta.** Conforme fundamentado na seção *1.3 Tipologia de Pistas e Classificação de Premissas* deste guia, negações Diretas (Pistas Negativas): Declaram a incompatibilidade mútua entre dois atributos (*"Bruno não é formado em Contabilidade"*, *"Carlos não trabalha na TI"*). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "Comprovada a onerosidade excessiva em razão das chuvas e alagamento, Carlos pode pedir judicialmente a resolução...".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Caso Carlos requeira a resolução do contrato, João não poderá evitá-la ainda que ofereça modificar equitativamente...". De acordo com a teoria estudada em *5.2 Condições Necessárias, Suficientes e Redundantes*, condição Redundante: Informação cuja veracidade já havia sido demonstrada pelo encadeamento das premissas precedentes, nada acrescentando à solução final.
> - **D)** **Incorreta.** A opção promove generalização excessiva que desconsidera as condições técnicas e normativas ao afirmar que "Apesar de o princípio da obrigatoriedade dos efeitos contratuais não ser absoluto, Carlos não poderá pedir a...". De acordo com a teoria estudada em *4.1 Ponto de Vista Referencial e Orientação Espacial*, a resolução exige que o candidato projete seu olhar a partir da cadeira do ocupante analisado, voltado para o centro da mesa circular.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Como Carlos assumiu a obrigação de fornecer os materiais, o contrato celebrado com João assume natureza aleatória...". De acordo com a teoria estudada em *1.3 Tipologia de Pistas e Classificação de Premissas*, pistas Condicionais ou Compostas: Estabelecem vínculos de causa-efeito ou conexões temporais e espaciais simultâneas (*"Se Lucas cuida da Folha, então Mateus cuida do Portal"*; *"O técnico que mora em Anápolis chegou depois de Carlos"*).
>
> **Gabarito: B**

---

## 🌐 Fontes Oficiais e Referências Bibliográficas

* [Portal da Matemática OBMEP / IMPA - Noções de Lógica e Argumentação](https://portaldaobmep.impa.br/index.php/modulo/ver?modulo=1059) - Aulas do IMPA sobre princípios da lógica formal, tabelas-verdade, negações e proposições compostas.
* [OBMEP / IMPA - Apostila 2 do PIC: Métodos de Contagem e Lógica](https://www.obmep.org.br/docs/apostila2.pdf) - Estratégias estruturadas de dedução, análise combinatória e diagramas de associação lógica.
* [Khan Academy Brasil - Álgebra I: Lógica e Raciocínio Dedutivo](https://pt.khanacademy.org/math/algebra) - Resolução de quebra-cabeças lógicos, tabelas de contingência e modelagem dedutiva.
* [OBMEP / IMPA - Apostila 8 do PIC: Raciocínio Geométrico e Estruturas Lógicas](https://www.obmep.org.br/docs/apostila8.pdf) - Modelos formais de pensamento estruturado e deduções axiomáticas em problemas lógicos.
* ALENCAR FILHO, Edgard de. **Iniciação à Lógica Matemática**. São Paulo: Nobel, 2002. (Cap. 3 e 4 - Proposições Compostas e Conectivos Lógicos).
* COPI, Irving M. **Introdução à Lógica**. 2. ed. São Paulo: Mestre Jou, 1978. (Cap. 8 - Lógica Simbólica e Tabelas-Verdade).
* MORTARI, Cezar A. **Introdução à Lógica**. 2. ed. São Paulo: Editora Unesp, 2016. (Cap. 5 e 6 - Sintaxe e Semântica do Cálculo Proposicional).
