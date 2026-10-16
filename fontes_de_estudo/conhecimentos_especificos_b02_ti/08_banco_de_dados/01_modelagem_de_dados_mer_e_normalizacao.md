# 01 - Modelagem de Dados, MER e Normalização

> **Matéria:** Banco de Dados  
> **Cargo:** B02 – Técnico de Controle Externo – Especialidade: Tecnologia da Informação  
> **Arquivo:** `01_modelagem_de_dados_mer_e_normalizacao.md`  

---

## 📌 Ementa / Itens do Edital
- Modelagem conceitual, lógica e física de dados
- Modelo Entidade-Relacionamento (MER) e Diagrama Entidade-Relacionamento (DER)
- Álgebra Relacional (operações fundamentais e derivadas)
- Dependências funcionais e Formas Normais (1ª FN, 2ª FN, 3ª FN e BCNF)
- Processo de Desnormalização de dados

---

## 🧭 Sumário
- [1. As Três Fases do Projeto de Banco de Dados](#1-as-três-fases-do-projeto-de-banco-de-dados)
    - [1.1 Modelo Conceitual: Semântica e Independência de Tecnologia](#11-modelo-conceitual-semântica-e-independência-de-tecnologia)
    - [1.2 Modelo Lógico: Dependência do Paradigma Relacional](#12-modelo-lógico-dependência-do-paradigma-relacional)
    - [1.3 Modelo Físico: Implementação e Otimização no SGBD](#13-modelo-físico-implementação-e-otimização-no-sgbd)
    - [1.4 Tabela Comparativa dos Níveis de Abstração](#14-tabela-comparativa-dos-níveis-de-abstração)
- [2. Modelo Entidade-Relacionamento (MER / DER de Peter Chen)](#2-modelo-entidade-relacionamento-mer--der-de-peter-chen)
    - [2.1 Entidades Fortes (Regulares) vs. Entidades Fracas](#21-entidades-fortes-regulares-vs-entidades-fracas)
    - [2.2 Tipologia e Representação Gráfica dos Atributos](#22-tipologia-e-representação-gráfica-dos-atributos)
    - [2.3 Relacionamentos, Cardinalidade e Participação (Total vs. Parcial)](#23-relacionamentos-cardinalidade-e-participação-total-vs-parcial)
- [3. Álgebra Relacional: Operações Formais e Consultas](#3-álgebra-relacional-operações-formais-e-consultas)
    - [3.1 As Seis Operações Fundamentais (Seleção, Projeção, Produto Cartesiano, União, Diferença e Renomeação)](#31-as-seis-operações-fundamentais-seleção-projeção-produto-cartesiano-união-diferença-e-renomeação)
    - [3.2 Operações Derivadas: Junção Natural, Theta Join, Equijunção, Interseção e Divisão Relacional](#32-operações-derivadas-junção-natural-theta-join-equijunção-interseção-e-divisão-relacional)
- [4. Teoria da Normalização e Formas Normais (Codd)](#4-teoria-da-normalização-e-formas-normais-codd)
    - [4.1 Dependências Funcionais: Total, Parcial e Transitiva](#41-dependências-funcionais-total-parcial-e-transitiva)
    - [4.2 A Escada da Normalização: 1ª FN, 2ª FN e 3ª FN](#42-a-escada-da-normalização-1ª-fn-2ª-fn-e-3ª-fn)
    - [4.3 Forma Normal de Boyce-Codd (FNBC / BCNF) vs. 3ª FN](#43-forma-normal-de-boyce-codd-fnbc--bcnf-vs-3ª-fn)
- [5. Processo de Desnormalização de Dados](#5-processo-de-desnormalização-de-dados)
    - [5.1 Motivações e Trade-offs: OLTP vs. OLAP / Data Warehouses](#51-motivações-e-trade-offs-oltp-vs-olap--data-warehouses)
    - [5.2 Técnicas Comuns e Riscos de Integridade](#52-técnicas-comuns-e-riscos-de-integridade)
- [6. Questões Comentadas & Prática Padrão FCC](#6-questões-comentadas--prática-padrão-fcc)

---

## 1. As Três Fases do Projeto de Banco de Dados

O projeto e a modelagem de dados para sistemas de gestão pública e auditoria fiscal evoluem ao longo de **três níveis sucessivos de abstração**, garantindo que a semântica das regras de negócio do Estado seja preservada independentemente dos detalhes físicos de armazenamento em disco.

```mermaid
flowchart LR
    A["Requisitos do Negócio"] --> B["1. Modelo Conceitual<br/>(Independente de SGBD e Paradigma)<br/>Ex.: DER Peter Chen"]
    B --> C["2. Modelo Lógico<br/>(Dependente do Paradigma Relacional)<br/>Ex.: Esquema Relacional, Tabelas, PK/FK"]
    C --> D["3. Modelo Físico<br/>(Dependente do SGBD Específico)<br/>Ex.: DDL Postgres/Oracle, Índices, Tablespaces"]
```

### 1.1 Modelo Conceitual: Semântica e Independência de Tecnologia
- **Escopo e Foco:** É o modelo de mais alto nível de abstração. Captura as entidades do mundo real, seus atributos fundamentais e como elas se relacionam, espelhando fielmente os requisitos do negócio sem qualquer preocupação tecnológica.
- **Independência Absoluta:** É **totalmente independente do software de SGBD** (PostgreSQL, Oracle) e até mesmo do paradigma lógico adotado (Relacional, Documentos, Grafos).
- **Notação Canônica:** O Diagrama Entidade-Relacionamento (DER) clássico de Peter Chen ou modelagens conceituais equivalentes.
- **Restrição Crítica:** O modelo conceitual **NÃO possui chaves estrangeiras (FKs)**, não define índices e não estipula tipos de dados de implementação (como `VARCHAR`, `INTEGER` ou `BLOB`).

### 1.2 Modelo Lógico: Dependência do Paradigma Relacional
- **Escopo e Foco:** Traduz o modelo conceitual para as estruturas do paradigma de banco de dados escolhido (quase universalmente o **Modelo Relacional** de Edgar F. Codd).
- **Mapeamento de Abstrações:** Entidades tornam-se **tabelas (relações)**, atributos tornam-se **colunas (atributos relacionais)**, instâncias tornam-se **tuplas (linhas)** e relacionamentos tornam-se **chaves estrangeiras (Foreign Keys - FK)** ou novas tabelas associativas (no caso de relacionamentos $N:M$).
- **Aplicação da Normalização:** É no modelo lógico que se aplicam formalmente as regras de normalização (1ª FN, 2ª FN, 3ª FN e FNBC) para expurgar anomalias de atualização e redundâncias desnecessárias.
- **Independência de Software:** Permanece independente de um SGBD específico (o mesmo modelo lógico atende ao PostgreSQL, Oracle Database ou SQL Server).

### 1.3 Modelo Físico: Implementação e Otimização no SGBD
- **Escopo e Foco:** Representa a implementação concreta e de mais baixo nível, altamente dependente dos recursos internos, dialeto SQL e mecanismos de armazenamento do SGBD corporativo contratado.
- **Elementos Físicos:** Scripts DDL (`CREATE TABLE`), definição precisa dos tipos de dados de baixo nível (`NUMERIC(15,2)`, `TIMESTAMPTZ`, `VARCHAR2`), definição de métodos de acesso e estruturas de **índices** (`B-Tree`, `Hash`, `GIN`, `GiST`, `BRIN`), estratégias de **particionamento de tabelas** (por lista, alcance ou hash), alocação de **tablespaces** e parâmetros de blocos de disco.
- **Decisões de Engenharia:** Avaliação de desnormalização deliberada para acelerar relatórios de grande porte e definição de restrições de integridade física (*constraints*).

### 1.4 Tabela Comparativa dos Níveis de Abstração

| Dimensão de Comparação | Modelo Conceitual | Modelo Lógico | Modelo Físico |
| :--- | :--- | :--- | :--- |
| **Público-Alvo Principal** | Analistas de negócio, auditores e usuários | Arquitetos de software e Administradores de Dados (DA) | Administradores de Banco de Dados (DBAs) e Engenheiros de Infra |
| **Independência de SGBD** | **Total** (independe de SGBD e de paradigma) | **Independente do SGBD**, dependente do paradigma relacional | **Totalmente dependente** do SGBD específico (PostgreSQL, Oracle) |
| **Estruturas Centrais** | Entidades, Atributos, Relacionamentos, Cardinalidade | Tabelas, Colunas, Chaves Primárias (PK), Chaves Estrangeiras (FK) | DDL SQL, Índices físicos, Tablespaces, Particionamento, Storage |
| **Momento da Normalização** | Não se aplica formalmente (define semântica) | **Etapa central de normalização** (1ª FN até Boyce-Codd) | Otimizações e eventual desnormalização controlada |

> 🚨 **ALERTA DE PROVA / FCC:**  
> A FCC adora cobrar a fronteira entre os modelos:
>
> - O **Modelo Conceitual** NÃO possui chaves estrangeiras nem tipos de dados de sistema operacional.
> - A introdução formal de **chaves estrangeiras (FKs)** ocorre estritamente na transição para o **Modelo Lógico**.
> - Estruturas de aceleração física como **índices B-Tree, particionamento e tablespaces** pertencem com exclusividade ao **Modelo Físico**.

---

## 2. Modelo Entidade-Relacionamento (MER / DER de Peter Chen)

Publicado em 1976 por Peter Pin-Shan Chen, o Modelo Entidade-Relacionamento tornou-se a ferramenta semântica universal para representação conceitual de esquemas de dados.

### 2.1 Entidades Fortes (Regulares) vs. Entidades Fracas

- **Entidade Forte (Regular):**
    - Possui existência autônoma e independente no mundo real.
    - Possui ao menos um atributo identificador próprio (chave primária) que distingue univocamente cada uma de suas instâncias.
    - Representação gráfica de Chen: **Retângulo de linha simples**.
- **Entidade Fraca:**
    - Sua existência depende obrigatoriamente da existência de outra entidade (denominada entidade proprietária ou dominante). Se a entidade proprietária for removida, a entidade fraca deixa de fazer sentido.
    - Não possui chave primária completa própria; possui apenas um **discriminador** ou **chave parcial**, que identifica a ocorrência apenas no escopo da sua entidade dominante.
    - Sua identificação plena é formada pela junção: $\text{Chave da Entidade Forte} + \text{Chave Parcial}$.
    - Representação gráfica de Chen: **Retângulo de linha dupla**.
- **Relacionamento Identificador:**
    - É o relacionamento formal que vincula a entidade fraca à sua entidade forte proprietária.
    - Representação gráfica de Chen: **Losango de linha dupla**.

```mermaid
flowchart LR
    subgraph Dominio_Funcional["Exemplo de Entidade Fraca"]
        D["PROCESSO_FISCAL<br/>(Entidade Forte - Linha Simples)"] --- RelId{{"CONTÉM<br/>(Relac. Identificador - Linha Dupla)"}}
        RelId --- Dep["TERMO_AUDITORIA<br/>(Entidade Fraca - Linha Dupla)"]
    end
```

### 2.2 Tipologia e Representação Gráfica dos Atributos

No modelo clássico de Chen, os atributos são expressos por elipses conectadas às entidades:

| Tipo de Atributo | Definição Teórica Rigorosa | Representação Gráfica (Chen) | Exemplo Prático |
| :--- | :--- | :--- | :--- |
| **Simples (Atômico)** | Não divisível em partes menores dotadas de significado próprio. | Elipse com linha simples | `CPF`, `Matrícula`, `Idade` |
| **Composto** | Pode ser desmembrado em múltiplos subatributos autônomos. | Elipse ramificada em subelipses | `Endereço` (`Logradouro`, `Número`, `CEP`) |
| **Monovalorado** | Armazena exatamente um valor para cada instância da entidade. | Elipse padrão de linha simples | `Data_Nascimento`, `Data_Emissao` |
| **Multivalorado** | Pode assumir múltiplos valores simultâneos para a mesma entidade. | Elipse com **linha dupla** | `Telefones`, `E-mails`, `CNAEs_Secundarios` |
| **Determinante (Identificador)**| Identifica univocamente a instância da entidade forte. | Elipse com texto **sublinhado contínuo** | `<u>NumContrato</u>`, `<u>IdProcesso</u>` |
| **Discriminador (Chave Parcial)**| Identifica a entidade fraca apenas dentro do escopo da forte. | Elipse com texto **sublinhado tracejado** | `Num_Sequencial_Termo` |
| **Derivado** | Valor calculado dinamicamente a partir de outros atributos persistidos. | Elipse com **borda tracejada/pontilhada** | `Idade` (calculada de `Data_Nasc`) |

### 2.3 Relacionamentos, Cardinalidade e Participação (Total vs. Parcial)

- **Grau do Relacionamento:** Quantidade de entidades participantes (Binário = 2 entidades; Ternário = 3 entidades; Unário / Auto-relacionamento = a mesma entidade se relaciona consigo mesma, como `FUNCIONARIO gerencia FUNCIONARIO`).
- **Razão de Cardinalidade:** Especifica o número máximo de ocorrências de relacionamento nas quais uma entidade pode participar:
    - $1:1$ (Um para Um);
    - $1:N$ (Um para Muitos);
    - $N:M$ (Muitos para Muitos - na conversão lógica, exige compulsoriamente a criação de uma tabela associativa intermediária).
- **Participação Total (Dependência de Existência):** Toda entidade do conjunto de entidades **obrigatoriamente deve participar** de ao menos uma instância do relacionamento. É representada graficamente por uma **linha dupla** que liga a entidade ao losango. Na notação $(mín, máx)$, expressa-se com $mín \ge 1$.
- **Participação Parcial:** A participação é opcional (algumas instâncias podem não participar do relacionamento). Representada por uma **linha simples**. Na notação $(mín, máx)$, expressa-se com $mín = 0$.

> 🚨 **ALERTA DE PROVA / PEGADINHA FCC:**  
> Cuidado com a notação de cardinalidade:
>
> - Na notação clássica de Chen com cardinalidade nas pontas ($1$ e $N$), o valor representa a cardinalidade máxima permitida.
> - Na notação de pares de limites $(mín, máx)$, se $mín = 0$, a participação é **parcial**; se $mín = 1$, a participação é **total**. Além disso, na notação $(min, max)$, os limites ficam posicionados **adjacentes à entidade que possui aquela restrição**!

---

## 3. Álgebra Relacional: Operações Formais e Consultas

A Álgebra Relacional é uma linguagem de consulta formal procedimental concebida por Edgar F. Codd. Suas operações manipulam uma ou duas relações como entrada e produzem uma nova relação como saída (propriedade de **fechamento da álgebra relacional**).

```mermaid
flowchart TD
    subgraph Operacoes_Algebricas["Álgebra Relacional"]
        A["Operações Fundamentais"] --> A1["Seleção: &sigma;_cond(R)<br/>(Filtra Tuplas/Linhas)"]
        A --> A2["Projeção: &pi;_cols(R)<br/>(Filtra Atributos/Colunas)"]
        A --> A3["Produto Cartesiano: R &times; S<br/>(Todas as Combinações)"]
        A --> A4["União: R &cup; S<br/>(Compatibilidade de Esquema)"]
        A --> A5["Diferença: R - S<br/>(Presentes em R, ausentes em S)"]
        A --> A6["Renomeação: &rho;_S(R)<br/>(Muda Rótulos)"]
        B["Operações Derivadas"] --> B1["Junção Natural: R &#x22C8; S"]
        B --> B2["Theta Join: R &#x22C8;_&theta; S"]
        B --> B3["Interseção: R &cap; S = R - (R - S)"]
        B --> B4["Divisão: R &divide; S (Universal)"]
    end
```

### 3.1 As Seis Operações Fundamentais

Qualquer consulta relacional teórica pode ser expressa combinando as seis operações primitivas:

1. **Seleção ($\sigma_{\text{condição}}(R)$):** Filtra linhas (tuplas) que satisfazem a um predicado lógico booleano. É um operador unário que atua no eixo **horizontal**. Corresponde à cláusula `WHERE` do SQL.
2. **Projeção ($\pi_{\text{lista\_atributos}}(R)$):** Filtra colunas (atributos) selecionadas, descartando as demais. É um operador unário que atua no eixo **vertical**. **Propriedade Mandatória:** A projeção matemática **elimina compulsoriamente tuplas duplicadas** do resultado final (dado que relações são conjuntos puros). Corresponde a `SELECT DISTINCT` no SQL.
3. **Produto Cartesiano ($R \times S$):** Operador binário que combina cada tupla da relação $R$ com todas as tuplas da relação $S$. Se $R$ possui $n_1$ tuplas e grau $k_1$, e $S$ possui $n_2$ tuplas e grau $k_2$, o produto $R \times S$ terá exatamente $n_1 \cdot n_2$ tuplas e grau $k_1 + k_2$.
4. **União ($R \cup S$):** Combina todas as tuplas de $R$ e $S$. Exige compulsoriamente **compatibilidade de união**: $R$ e $S$ devem ter o mesmo grau (mesmo número de atributos) e os tipos dos atributos correspondentes devem pertencer a domínios compatíveis.
5. **Diferença de Conjuntos ($R - S$):** Retorna as tuplas que existem na relação $R$, mas que **não estão presentes** na relação $S$. Também exige compatibilidade de união.
6. **Renomeação ($\rho_{S}(R)$ ou $\rho_{S(A_1, A_2, \dots)}(R)$):** Altera o nome da relação resultante ou rebatiza seus atributos, permitindo desambiguar colunas em junções recursivas.

### 3.2 Operações Derivadas: Junção Natural, Theta Join, Equijunção, Interseção e Divisão Relacional

São operações construídas a partir da composição das primitivas fundamentais:

- **Theta Join ($R \bowtie_{\theta} S$):** Combina o produto cartesiano com uma condição de seleção: $\sigma_{\theta}(R \times S)$. Se a condição $\theta$ envolver apenas testes de igualdade ($=$), denomina-se **Equijunção**.
- **Junção Natural ($R \bowtie S$):** Executa uma equijunção automática baseada em todos os atributos que compartilham o mesmo nome e tipo em $R$ e $S$, projetando as colunas comuns uma única vez no resultado:
  $$R \bowtie S = \pi_{\text{esquema\_unificado}}(\sigma_{R.A_1 = S.A_1 \land \dots \land R.A_m = S.A_m}(R \times S))$$
- **Interseção ($R \cap S$):** Retorna as tuplas presentes simultaneamente em $R$ e $S$. Derivável pela diferença: $R \cap S = R - (R - S)$.
- **Divisão Relacional ($R \div S$):** Operação fundamental para responder a consultas que envolvem o **quantificador universal "para todos" ($\forall$)** — por exemplo, *"encontrar os auditores que fiscalizaram TODOS os municípios do estado de Goiás"*.
    - Se $R$ possui esquema $(A, B)$ e $S$ possui esquema $(B)$, a divisão $R \div S$ produz uma relação de esquema $(A)$ contendo as tuplas $t$ tais que, para toda tupla $s \in S$, o par ordenado $(t, s)$ existe na relação $R$.

---

## 4. Teoria da Normalização e Formas Normais (Codd)

A teoria da normalização, concebida por Edgar F. Codd, consiste em uma técnica formal de análise de esquemas relacionais com base em suas **Dependências Funcionais (DF)** e chaves primárias. Seu objetivo é minimizar a redundância de dados e erradicar as anomalias de inserção, exclusão e alteração.

```mermaid
flowchart TD
    subgraph Fluxo_Normalizacao["Escada da Normalização"]
        A["Tabela Bruta Não Normalizada"] -->|Eliminar Grupos Repetitivos e Atributos Multivalorados| B["1ª Forma Normal (1ª FN)"]
        B -->|Eliminar Dependências Parciais de Chaves Compostas| C["2ª Forma Normal (2ª FN)"]
        C -->|Eliminar Dependências Transitivas| D["3ª Forma Normal (3ª FN)"]
        D -->|Eliminar Anomalias com Múltiplas Chaves Candidatas Sobrepostas| E["Forma Normal de Boyce-Codd (FNBC / BCNF)"]
    end
```

### 4.1 Dependências Funcionais: Total, Parcial e Transitiva

Dada uma relação $R$, diz-se que o conjunto de atributos $X$ determina funcionalmente o atributo $Y$ ($X \rightarrow Y$) se, e somente se, para quaisquer duas tuplas $t_1, t_2 \in R$, sempre que $t_1[X] = t_2[X]$, obrigatoriamente $t_1[Y] = t_2[Y]$. O lado esquerdo ($X$) é chamado de **determinante** e o direito ($Y$) de **dependente**.

- **Dependência Funcional Total:** Ocorre quando $Y$ depende funcionalmente de $X$ e não depende de nenhum subconjunto próprio de $X$.
- **Dependência Funcional Parcial:** Ocorre quando um atributo não-chave depende de apenas uma parte de uma chave primária composta (isto é, existe $A \subset X$ tal que $A \rightarrow Y$).
- **Dependência Funcional Transitiva:** Ocorre quando $X \rightarrow Y$ e $Y \rightarrow Z$, onde $Y$ não é superchave e $Y \not\rightarrow X$. Consequentemente, $X$ determina $Z$ indiretamente através de $Y$.

### 4.2 A Escada da Normalização: 1ª FN, 2ª FN e 3ª FN

1. **Primeira Forma Normal (1ª FN):**
    - **Regra:** Todos os domínios de atributos devem conter **apenas valores atômicos e indivisíveis**. Proíbe-se a presença de atributos multivalorados, atributos compostos e grupos repetitivos (como campos contendo listas separadas por vírgula ou tabelas aninhadas).
2. **Segunda Forma Normal (2ª FN):**
    - **Regra:** A relação deve estar na **1ª FN** e todo atributo não-chave deve depender **totalmente da chave primária**, eliminando qualquer dependência funcional parcial.
    - **Regra de Ouro em Provas:** A violação da 2ª FN só pode ocorrer se a chave primária for **composta** (possuir 2 ou mais atributos). Se a chave primária for simples (apenas 1 atributo), estando na 1ª FN ela estará **automaticamente na 2ª FN**!
3. **Terceira Forma Normal (3ª FN):**
    - **Regra:** A relação deve estar na **2ª FN** e nenhum atributo não-chave pode depender transitivamente da chave primária.
    - **Definição Formal de Codd:** Para toda dependência funcional não-trivial $X \rightarrow A$:
    1. $X$ é uma superchave; **OU**
    2. $A$ é um atributo primo (faz parte de ao menos uma chave candidata).

### 4.3 Forma Normal de Boyce-Codd (FNBC / BCNF) vs. 3ª FN

A **Forma Normal de Boyce-Codd (FNBC)** é uma versão mais estrita da 3ª FN criada por Raymond F. Boyce e Edgar F. Codd para lidar com anomalias sutis que surgem quando uma tabela possui **múltiplas chaves candidatas compostas que se sobrepõem** (compartilham atributos entre si):

- **Regra Inflexível da FNBC:** Uma relação $R$ está na FNBC se, e somente se, para **toda** dependência funcional não-trivial $X \rightarrow A$, **$X$ for obrigatoriamente uma superchave**.
- **Diferença Crucial:** Na FNBC, **elimina-se a condição de escape do atributo primo da 3ª FN**. Mesmo que $A$ faça parte de uma chave candidata, se o determinante $X$ não for superchave, a relação viola a FNBC.
- Toda relação que está na FNBC está automaticamente na 3ª FN. A recíproca não é verdadeira.

---

## 5. Processo de Desnormalização de Dados

A **desnormalização** consiste na introdução deliberada, planejada e controlada de redundância em um esquema de banco de dados físico previamente normalizado.

```mermaid
flowchart TD
    subgraph TradeOff["Trade-off de Desnormalização"]
        N["Banco Totalmente Normalizado (3ª FN / FNBC)"]
        N -->|Vantagem| NV1["Zero redundância<br/>Integridade garantida<br/>Escritas/Updates rápidos"]
        N -->|Desvantagem| ND1["Múltiplos JOINs complexos<br/>Lentidão em consultas analíticas OLAP"]
        
        D["Banco Desnormalizado"]
        D -->|Vantagem| DV1["Leituras ultrarrápidas<br/>Consultas simples sem JOINs<br/>Ideal para Data Warehouses"]
        D -->|Desvantagem| DD1["Redundância severa<br/>Risco de anomalias de atualização<br/>Maior consumo de disco"]
    end
```

### 5.1 Motivações e Trade-offs: OLTP vs. OLAP / Data Warehouses

- **Sistemas Transacionais (OLTP - Online Transaction Processing):** Exigem alta normalização (3ª FN / FNBC) para garantir escrita rápida, bloqueio granular de linhas e integridade referencial sem risco de anomalias.
- **Sistemas Analíticos (OLAP - Online Analytical Processing / Data Warehouses):** Priorizam o desempenho em **leitura massiva** e agregação de dados. Em esquemas como o *Star Schema* (Esquema em Estrela), desnormalizam-se as tabelas de dimensões para eliminar junções caras (`JOINs`) de centenas de milhões de linhas.

### 5.2 Técnicas Comuns e Riscos de Integridade

- **Técnicas de Desnormalização:**
    1. *Junção Pré-calculada:* Mesclar duas tabelas $1:N$ em uma única tabela para evitar consultas com `JOIN`.
    2. *Campos Totalizadores / Derivados Persistidos:* Adicionar uma coluna `ValorTotalNota` na tabela mestre para evitar calcular `SUM()` de itens a cada requisição.
    3. *Replicação de Colunas de Consulta Frequente:* Armazenar o `NomeFornecedor` diretamente na tabela de `Empenho`.
- **Riscos e Trade-offs:**
    - Redundância severa e aumento do consumo de armazenamento em disco;
    - **Risco Crítico de Inconsistência:** Atualizar o nome do fornecedor exige atualizar milhões de registros duplicados; se uma atualização falhar pela metade, o banco de dados entra em estado inconsistente.

---

## 6. Questões Comentadas & Prática Padrão FCC

### Questão 1 (FCC - Adaptada / TI - Teoria da Normalização)
Considere uma relação não normalizada de um sistema de compras públicas representada pelo esquema:  
`CONTRATO (NumContrato, NumItem, CodFornecedor, NomeFornecedor, DescricaoItem, Quantidade, ValorUnitario)`  
Onde a chave primária composta da relação é `(NumContrato, NumItem)`. Sabe-se ainda que existem as seguintes dependências funcionais:

- `(NumContrato, NumItem) -> Quantidade, ValorUnitario`
- `NumItem -> DescricaoItem`
- `NumContrato -> CodFornecedor, NomeFornecedor`
- `CodFornecedor -> NomeFornecedor`

Para que o esquema atinja estritamente a **Segunda Forma Normal (2ª FN)**, deve-se:  

* **A)** Eliminar os grupos repetitivos e garantir a atomicidade dos campos, mantendo todos os atributos na mesma tabela.
* **B)** Eliminar as dependências funcionais parciais, decompondo a relação de modo que nenhum atributo não-chave dependa de apenas parte da chave primária composta.
* **C)** Eliminar as dependências transitivas, garantindo que o `NomeFornecedor` não dependa de `CodFornecedor`.
* **D)** Converter todas as chaves primárias em chaves substitutas (*surrogate keys*) UUID geradas pelo SGBD.
* **E)** Desnormalizar a relação unificando `Quantidade` e `ValorUnitario` em um atributo multivalorado.

> **Comentário Detalhado:**
> - **A)** Incorreta. A atomicidade de domínios e a eliminação de grupos repetitivos constituem a regra da **Primeira Forma Normal (1ª FN)**.
> - **B)** Correta. A **Segunda Forma Normal (2ª FN)** exige que a relação esteja na 1ª FN e que todo atributo não-chave dependa *totalmente* da chave primária. Como a chave primária é composta por `(NumContrato, NumItem)`, atributos como `DescricaoItem` (que depende apenas de `NumItem`) e `CodFornecedor` (que depende apenas de `NumContrato`) configuram **dependências funcionais parciais**, devendo ser isolados em tabelas próprias para atingir a 2ª FN.
> - **C)** Incorreta. A eliminação de dependências transitivas (`CodFornecedor -> NomeFornecedor`) é o requisito exclusivo para a **Terceira Forma Normal (3ª FN)**.
> - **D)** Incorreta. A adoção de chaves substitutas (*surrogate keys*) é escolha de modelagem física, sem relação formal com os postulados de Edgar F. Codd.
> - **E)** Incorreta. Introduzir atributos multivalorados violaria a 1ª FN, degradando o esquema para o estado não normalizado.
> 
> **Gabarito: B**

---

### Questão 2 (FCC - Adaptada / TI - Álgebra Relacional)
Na Álgebra Relacional, uma consulta sobre duas relações $R(A, B, C)$ e $S(C, D, E)$ tem por objetivo filtrar as tuplas de $R$ onde o atributo $A = 10$, concatenar com as tuplas correspondentes de $S$ onde $R.C = S.C$, e projetar apenas as colunas $B$ e $D$.

A expressão formal algébrica que representa essa operação com precisão é:  

* **A)** $\pi_{B, D} (\sigma_{A = 10} (R \bowtie S))$
* **B)** $\sigma_{B, D} (\pi_{A = 10} (R \times S))$
* **C)** $\pi_{B, D} (\sigma_{A = 10} (R) \cup \sigma_{A = 10} (S))$
* **D)** $\rho_{B, D} (\sigma_{A = 10} (R - S))$
* **E)** $\pi_{A = 10} (\sigma_{B, D} (R \div S))$

> **Comentário Detalhado:**
> - **A)** Correta. A junção natural $R \bowtie S$ realiza a equijunção pelo atributo comum $C$ ($R.C = S.C$). Em seguida, a seleção $\sigma_{A=10}$ filtra apenas as tuplas onde $A$ vale $10$. Por fim, a projeção $\pi_{B, D}$ descarta as demais colunas e projeta unicamente os atributos solicitados $B$ e $D$, eliminando eventuais duplicatas.
> - **B)** Incorreta. Inverte a sintaxe dos operadores: $\sigma$ recebe uma condição booleana (e não uma lista de atributos como $B, D$) e $\pi$ recebe atributos.
> - **C)** Incorreta. O operador de união ($\cup$) concatena tuplas verticalmente e exige que as relações sejam compatíveis quanto à união (mesmo grau e domínios equivalentes), o que não ocorre entre $R$ e $S$.
> - **D)** Incorreta. O operador $\rho$ representa a operação de renomeação.
> - **E)** Incorreta. O operador $\div$ expressa a divisão relacional, inadequada para consultas com junção condicional e projeção.
> 
> **Gabarito: A**

---

### Questão 3 (FCC - Adaptada / TI - Modelo Entidade-Relacionamento de Peter Chen)
No contexto do Diagrama Entidade-Relacionamento (DER) segundo a notação original proposta por Peter Chen, analise a seguinte situação de negócio:  
*"Em um órgão de fiscalização fazendária, cada PROCESSO_FISCAL possui um número de processo que o identifica unicamente. Cada processo pode conter múltiplos TERMOS_FISCAIS. Um termo fiscal possui apenas uma numeração sequencial interna (ex.: 1, 2, 3), só faz sentido existir vinculado ao seu respectivo processo fiscal e sua identificação plena depende da chave primária do processo."*

Conforme a teoria canônica do DER, a entidade `TERMO_FISCAL`, a numeração sequencial interna e o relacionamento entre `PROCESSO_FISCAL` e `TERMO_FISCAL` são classificados, respectivamente, como:  

* **A)** Entidade Associativa, Atributo Composto e Auto-relacionamento.
* **B)** Entidade Fraca, Chave Parcial (discriminador) e Relacionamento Identificador.
* **C)** Entidade Regular, Atributo Multivalorado e Relacionamento Não-identificador.
* **D)** Entidade Fraca, Atributo Derivado e Agregação.
* **E)** Superclasse, Atributo Atômico e Relacionamento Ternário.

> **Comentário Detalhado:**
> - **A)** Incorreta. Entidades associativas resolvem relacionamentos $N:M$ com atributos próprios, e auto-relacionamento ocorre quando uma entidade se relaciona consigo mesma.
> - **B)** Correta. Classificação impecável segundo a teoria de Chen:
>   1. `TERMO_FISCAL` depende existencialmente de `PROCESSO_FISCAL` e não possui chave primária global própria; logo, é uma **Entidade Fraca** (representada por retângulo de linha dupla);
>   2. A numeração sequencial interna (1, 2, 3) identifica o termo apenas dentro de cada processo; logo, é uma **Chave Parcial** ou **Discriminador** (representada por elipse com sublinhado tracejado);
>   3. O relacionamento que conecta a entidade fraca à sua proprietária é um **Relacionamento Identificador** (representado por losango de linha dupla).
> - **C)** Incorreta. `TERMO_FISCAL` não é uma entidade regular (forte), pois depende da proprietária para sua identificação plena.
> - **D)** Incorreta. A numeração sequencial não é atributo derivado (calculado dinamicamente).
> - **E)** Incorreta. Conceitos de especialização/generalização e relacionamentos ternários não se aplicam ao cenário.
> 
> **Gabarito: B**

---

### Questão 4 (FCC - Adaptada / TI - Forma Normal de Boyce-Codd vs. 3ª FN)
Considere uma relação $R(A, B, C)$ com o seguinte conjunto de dependências funcionais:  
$F = \{ (A, B) \rightarrow C, \quad C \rightarrow B \}$  
Sabe-se que as chaves candidatas dessa relação são $(A, B)$ e $(A, C)$.

Com base nas definições formais das Formas Normais, afirma-se corretamente que a relação $R$:  

* **A)** Não está na 1ª FN, pois apresenta dependências funcionais sobrepostas.
* **B)** Está na 2ª FN, mas viola a 3ª FN porque $C$ determina um atributo não-chave.
* **C)** Está na 3ª FN, mas não está na Forma Normal de Boyce-Codd (FNBC).
* **D)** Está na Forma Normal de Boyce-Codd (FNBC), pois todas as dependências funcionais são triviais.
* **E)** Encontra-se na 4ª FN, pois não possui atributos multivalorados dependentes.

> **Comentário Detalhado:**
> - **A)** Incorreta. A relação está na 1ª FN (domínios atômicos).
> - **B)** Incorreta. A relação não viola a 3ª FN.
> - **C)** Correta. Análise detalhada:
>   1. Chaves candidatas: $(A, B)$ e $(A, C)$. Todos os atributos ($A, B, C$) são atributos primos (pertencem a ao menos uma chave).
>   2. 2ª FN: Como não existem atributos não-primos, a relação está na 2ª FN.
>   3. 3ª FN: Para $(A, B) \rightarrow C$, $(A, B)$ é superchave. Para $C \rightarrow B$, embora $C$ não seja superchave, $B$ é atributo primo. Logo, a relação **atende à 3ª FN**.
>   4. FNBC: A FNBC exige estritamente que, para toda dependência não-trivial $X \rightarrow Y$, o determinante $X$ seja superchave. Na dependência $C \rightarrow B$, o determinante $C$ **não é superchave**. Portanto, a relação **viola a FNBC**.
> - **D e E)** Incorretas. A relação viola a FNBC conforme demonstrado.
> 
> **Gabarito: C**

---

### Questão 5 (FCC - Adaptada / TI - Álgebra Relacional e Divisão Relacional)
Em sistemas de banco de dados relacionais, deseja-se elaborar uma consulta algébrica formal para responder à seguinte demanda de auditoria:  
*"Recuperar o código de todos os Auditores Fiscais que realizaram inspeções em TODOS os estabelecimentos cadastrados no estado."*

Considere os esquemas das relações:

- `INSPECAO (CodAuditor, CodEstabelecimento)`
- `ESTABELECIMENTO (CodEstabelecimento)`

A operação da Álgebra Relacional que expressa diretamente essa semântica de quantificação universal ("para todos"), sem a necessidade de aninhamentos complexos de operadores de diferença, é a:  

* **A)** Junção Externa Completa (`INSPECAO` $\mathbin{⟗}$ `ESTABELECIMENTO`)
* **B)** Equijunção (`INSPECAO` $\bowtie_{\text{CodEstabelecimento} = \text{CodEstabelecimento}}$ `ESTABELECIMENTO`)
* **C)** Divisão Relacional (`INSPECAO` $\div$ `ESTABELECIMENTO`)
* **D)** Produto Cartesiano (`INSPECAO` $\times$ `ESTABELECIMENTO`)
* **E)** Interseção (`INSPECAO` $\cap$ `ESTABELECIMENTO`)

> **Comentário Detalhado:**
> - **A)** Incorreta. O Full Outer Join preserva tuplas sem correspondência em ambos os lados preenchendo com nulos, sem filtrar por quantificação universal.
> - **B)** Incorreta. A Equijunção apenas relaciona inspeções a estabelecimentos existentes, retornando auditores que inspecionaram *ao menos um* estabelecimento.
> - **C)** Correta. A **Divisão Relacional ($R \div S$)** é o operador formal da álgebra relacional projetado para expressar o quantificador universal $\forall$ (*"para todos"*). A operação `INSPECAO` $\div$ `ESTABELECIMENTO` retorna unicamente as tuplas de `CodAuditor` que estão combinadas com **todas** as tuplas presentes na relação `ESTABELECIMENTO`.
> - **D)** Incorreta. O Produto Cartesiano gera todas as combinações possíveis entre auditores e estabelecimentos, multiplicando o número de tuplas.
> - **E)** Incorreta. A Interseção exige esquemas compatíveis quanto à união (mesmo número e tipos de atributos), o que não ocorre entre relações com graus diferentes.
> 
> **Gabarito: C**
