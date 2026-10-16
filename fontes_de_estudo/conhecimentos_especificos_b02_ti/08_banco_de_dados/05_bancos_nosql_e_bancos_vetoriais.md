# 05 - Bancos de Dados NoSQL e Bancos Vetoriais (IA)
**Última Atualização:** 2026-03-31  
**Banca Foco:** FCC (Fundação Carlos Chagas)  
**Cargo:** Auditor de Controle Externo - Tecnologia da Informação  
**Status do Mapeamento:** 100% aderente ao edital TCE-GO

---

## 📌 Ementa / Itens do Edital
1. **Teorema CAP e Modelo BASE:** Teorema CAP de Eric Brewer (Consistência, Disponibilidade e Tolerância a Partições), trade-offs fundamentais (CP vs. AP), Teorema PACELC e Modelo BASE (*Basically Available*, *Soft state*, *Eventual consistency*) vs. Modelo ACID.
2. **As Quatro Famílias de Bancos NoSQL:**
    - **Documentos:** Modelagem semiestruturada (JSON/BSON), coleções, identificador único `_id`, pipeline de agregação e arquitetura MongoDB (*Replica Sets* e *Sharding*).
    - **Chave-Valor (*Key-Value*):** Estruturas nativas em memória RAM, persistência (RDB e AOF), TTL e arquitetura Redis.
    - **Famílias de Colunas (*Wide-Column*):** Tabelas esparsas multidimensionais, arquitetura descentralizada sem nó mestre (*masterless*), Cassandra e HBase.
    - **Grafos:** Vértices, arestas direcionadas tipadas, propriedades, linguagem Cypher e adjacência livre de índice (*Index-free Adjacency*) no Neo4j.

3. **Casos de Uso e Escalabilidade:** Trade-offs arquiteturais, escalabilidade horizontal (*sharding*) e adequação a cenários de Big Data e auditoria de controle externo.
4. **Bancos de Dados Vetoriais Aplicados à Inteligência Artificial:** Representação vetorial contínua (*embeddings*), métricas de distância e similaridade (Cosseno, Euclidiana $L_2$ e Produto Escalar), algoritmos de busca aproximada por vizinhos mais próximos (ANN: HNSW e IVF), ecossistema vetorial (`pgvector` no PostgreSQL e SGBDs vetoriais dedicados como Qdrant, Milvus e Pinecone) e aplicação em RAG (*Retrieval-Augmented Generation*).

---

## 🧭 Sumário
- [1. Teorema CAP, Teorema PACELC e o Modelo BASE](#1-teorema-cap-teorema-pacelc-e-o-modelo-base)
    - [1.1 Teorema CAP (Eric Brewer / Gilbert & Lynch)](#11-teorema-cap-eric-brewer-gilbert-lynch)
    - [1.2 O Teorema PACELC](#12-o-teorema-pacelc)
    - [1.3 Modelo BASE vs. Propriedades ACID](#13-modelo-base-vs-propriedades-acid)
- [2. As Quatro Famílias de Bancos de Dados NoSQL](#2-as-quatro-familias-de-bancos-de-dados-nosql)
    - [2.1 Bancos Orientados a Documentos (MongoDB)](#21-bancos-orientados-a-documentos-mongodb)
    - [2.2 Bancos Chave-Valor (Redis)](#22-bancos-chave-valor-redis)
    - [2.3 Bancos de Famílias de Colunas (Wide-Column / Cassandra / HBase)](#23-bancos-de-familias-de-colunas-wide-column-cassandra-hbase)
    - [2.4 Bancos Orientados a Grafos (Neo4j e Cypher)](#24-bancos-orientados-a-grafos-neo4j-e-cypher)
    - [2.5 Matriz Comparativa e Casos de Uso no Controle Externo](#25-matriz-comparativa-e-casos-de-uso-no-controle-externo)
- [3. Bancos de Dados Vetoriais e Inteligência Artificial](#3-bancos-de-dados-vetoriais-e-inteligencia-artificial)
    - [3.1 Embeddings: Do Texto Não-Estruturado ao Espaço Vetorial](#31-embeddings-do-texto-nao-estruturado-ao-espaco-vetorial)
    - [3.2 Métricas Matemáticas de Distância e Similaridade](#32-metricas-matematicas-de-distancia-e-similaridade)
    - [3.3 Algoritmos de Busca Aproximada por Vizinhos Mais Próximos (ANN)](#33-algoritmos-de-busca-aproximada-por-vizinhos-mais-proximos-ann)
    - [3.4 Ecossistema Tecnológico: Extensão pgvector e Bancos Nativos](#34-ecossistema-tecnologico-extensao-pgvector-e-bancos-nativos)
- [4. Questões Comentadas (FCC)](#4-questoes-comentadas-fcc)

---

## 1. Teorema CAP, Teorema PACELC e o Modelo BASE

O movimento NoSQL (*Not Only SQL*) surgiu para contornar as restrições físicas de escalabilidade vertical de bancos relacionais monolíticos em cenários de processamento massivo de dados (*Big Data*), viabilizando esquemas dinâmicos (*schemaless*) e particionamento horizontal maciço (*sharding*).

### 1.1 Teorema CAP (Eric Brewer / Gilbert & Lynch)

O Teorema CAP afirma que em qualquer sistema distribuído de armazenamento de dados sujeito a comunicação em rede, é **matematicamente impossível** fornecer simultaneamente as três garantias abaixo:

```
                      [C] Consistência Forte
                          (Linearizabilidade)
                                /     \
                               /       \
                              /  TRADE  \
                             /   -OFFS   \
                            /             \
    [A] Disponibilidade ───────────────────── [P] Tolerância a Partições
  (Todo nó responde com sucesso)               (Rede sujeita a quedas e atrasos)
```

1. **C (Consistency - Consistência Forte / Linearizabilidade):** Todos os clientes leem exatamente a versão mais recente e idêntica dos dados no mesmo instante, independentemente do nó consultado.
2. **A (Availability - Disponibilidade):** Todo nó não-falho que recebe uma requisição emite obrigatoriamente uma resposta com sucesso (sem exceções, erros internos de partição ou timeouts), embora não haja garantia estrita de que o dado seja o mais recente.
3. **P (Partition Tolerance - Tolerância a Partições de Rede):** O cluster distribuído continua processando dados mesmo se ocorrerem interrupções de links de comunicação, partições físicas de rede ou atrasos arbitrários no tráfego de pacotes entre os nós.

> ⚠️ **Alerta de Prova (FCC):**
> A banca FCC costuma colocar como pegadinha que "um arquiteto pode escolher um sistema CA (Consistência + Disponibilidade sem Tolerância a Partições)". Lembre-se: em redes de computadores físicas do mundo real, quedas de links de rede e atrasos são contingências inevitáveis; portanto, **P é compulsório**. A decisão prática resume-se a escolher entre:
>
> - **Sistemas CP:** Priorizam Consistência. Em caso de quebra de partição, os nós isolados rejeitam requisições para evitar leituras defasadas ou escritas conflitantes (sacrificam a Disponibilidade). Exemplos: MongoDB, Redis Cluster, HBase, CockroachDB.
> - **Sistemas AP:** Priorizam Disponibilidade. Em caso de quebra de rede, todos os nós continuam respondendo a leituras e escritas, tolerando que réplicas fiquem temporariamente desatualizadas e sincronizem depois via Consistência Eventual (sacrificam a Consistência imediata). Exemplos: Apache Cassandra, CouchDB, DynamoDB (em configuração padrão).

### 1.2 O Teorema PACELC

Formulado pelo professor Daniel Abadi, o Teorema PACELC expande o Teorema CAP para descrever o comportamento do sistema não apenas durante desastres de rede, mas também em condições de operação normal:

- **Se houver Partição (P):** Escolha entre **Disponibilidade (A)** e **Consistência (C)**;
- **Senão (*Else - E*):** Operando em regime de normalidade sem partições ativas, o sistema precisa arbitrar entre **Latência (L)** e **Consistência (C)**.

Ou seja, para entregar dados estritamente consistentes mesmo em tempos normais, os nós do cluster precisam trocar mensagens de confirmação síncronas entre si, o que eleva a latência percebida pelos clientes. Se o objetivo for latência ultrabaixa, o sistema deve relaxar a consistência imediata de leitura.

### 1.3 Modelo BASE vs. Propriedades ACID

Enquanto os bancos relacionais transacionais regem-se pelo rigor determinístico do modelo ACID, os sistemas NoSQL distribuídos apoiam-se no paradigma flexível do **modelo BASE**:

| Propriedades ACID (Bancos Relacionais) | Pilares do Modelo BASE (Sistemas NoSQL Distribuídos) |
| :--- | :--- |
| **A - Atomicidade:** A transação é indivisível (tudo ou nada). | **BA - Basically Available (Disponibilidade Básica):** O sistema garante disponibilidade contínua dos serviços essenciais, tolerando falhas parciais ou degradação seletiva de recursos secundários. |
| **C - Consistência:** Preservação estrita das regras de integridade e esquemas rígidos antes e após a transação. | **S - Soft State (Estado Maleável/Fluido):** O estado do sistema pode sofrer alterações ao longo do tempo por sincronização interna de réplicas em segundo plano, mesmo sem que nenhuma nova escrita tenha ocorrido. |
| **I - Isolamento:** Transações simultâneas não interferem entre si, produzindo resultado idêntico a uma execução serial. | **E - Eventual Consistency (Consistência Eventual):** Se nenhuma nova atualização for submetida ao sistema, após decorrido um intervalo de tempo razoável todas as réplicas convergentes propagarão suas atualizações e alcançarão o mesmo estado consolidado. |
| **D - Durabilidade:** Os dados comitados persistem permanentemente em disco, resistindo a falhas elétricas. | **Propagação de Réplicas:** Replicação assíncrona tolerante a latência, utilizando protocolos como *Gossip Protocol* e algoritmos de quórum configuráveis ($R + W > N$). |

---

## 2. As Quatro Famílias de Bancos de Dados NoSQL

Os bancos de dados NoSQL agrupam-se em quatro categorias fundamentais de acordo com seus modelos conceituais de dados subjacentes:

```
┌────────────────────────────────────────────────────────────────────────┐
│                   AS QUATRO FAMÍLIAS DO PARADIGMA NoSQL                │
└────────────────────────────────────────────────────────────────────────┘
          │                   │                     │                  │
          ▼                   ▼                     ▼                  ▼
   [ DOCUMENTOS ]      [ CHAVE-VALOR ]      [ WIDE-COLUMN ]       [ GRAFOS ]
   MongoDB, CouchDB    Redis, DynamoDB      Cassandra, HBase      Neo4j, Neptune
   - Docs JSON/BSON    - Chave -> Valor     - Tabelas esparsas    - Nós, arestas,
   - Pipeline agreg.   - RAM ultra-rápida   - Escala massiva        propriedades
   - Esquema dinâmico  - TTL e persistência - Masterless P2P      - Index-free adj.
```

### 2.1 Bancos Orientados a Documentos (MongoDB)

Armazenam dados na forma de documentos semiestruturados, geralmente serializados em formatos como JSON, BSON (*Binary JSON*) ou XML.

- **Coleções e Documentos:** Os dados são agrupados em Coleções (*Collections*), que equivalem conceitualmente às tabelas relacionais. No entanto, cada Documento (*Document*) individual dentro de uma mesma coleção pode possuir campos, tipos e estruturas inteiramente distintas (esquema dinâmico / *schema-flexible*).
- **Identificador Canônico (`_id`):** Todo documento possui obrigatoriamente um identificador exclusivo mapeado pelo campo `_id`, instanciado por padrão como um `ObjectId` de 12 bytes (composto por timestamp Unix de 4 bytes, identificador do host/processo de 5 bytes e contador incremental aleatório de 3 bytes).
- **BSON (Binary JSON):** Extensão binária do JSON que viabiliza tipos primitivos adicionais não suportados pelo JSON textual puro, como tipos `Date` nativos, inteiros de 64 bits (`long`), decimais de alta precisão e dados binários brutos, otimizando a velocidade de parseamento e travessia.
- **Aggregation Pipeline:** Framework de análise de dados no MongoDB estruturado em etapas sequenciais compostas por operadores:
    - `$match`: Filtra os documentos com base em predicados lógicos (equivalente ao `WHERE` / `HAVING`).
    - `$project`: Modifica a projeção estrutural dos campos, renomeando ou incluindo campos calculados (equivalente ao `SELECT`).
    - `$group`: Agrupa documentos por uma chave específica e calcula métricas agregadas como `$sum`, `$avg`, `$min`, `$max` (equivalente ao `GROUP BY`).
    - `$sort`: Ordena os documentos processados pelo pipeline (equivalente ao `ORDER BY`).
    - `$unwind`: Desconstrói um campo contendo array, emitindo um documento individual para cada elemento do array.
- **Alta Disponibilidade e Particionamento:**
    - *Replica Sets:* Conjuntos de nós configurados para replicação automática com eleição de um nó Primário (*Primary*, que processa todas as escritas) e múltiplos nós Secundários (*Secondary*, que replicam os logs de operação `oplog` de forma assíncrona). Se o nó Primário cair, os Secundários realizam uma eleição baseada no algoritmo Raft/Paxos para eleger um novo líder sem intervenção humana.
    - *Sharding:* Distribuição horizontal física dos documentos entre múltiplos servidores (*shards*) guiada por uma Chave de Partição (*Shard Key*). O balanceamento e roteamento de requisições é transparente, intermediado por roteadores `mongos` e servidores de configuração (*Config Servers*).

### 2.2 Bancos Chave-Valor (Redis)

O modelo mais simples, minimalista e veloz. Armazena pares formados por uma chave única (string) mapeada para um valor (escalar primitivo, objeto binário ou estrutura complexa).

- **Arquitetura em Memória RAM:** O **Redis (*Remote Dictionary Server*)** opera primariamente na memória principal do servidor, propiciando tempos de resposta na escala de dezenas de microssegundos.
- **Estruturas de Dados Nativas do Redis:**
    - `Strings`: O tipo básico fundamental (suporta texto, blobs de até 512 MB ou inteiros/floats com manipulação atômica via `INCR`, `DECR`, `INCRBY`).
    - `Hashes`: Mapas associativos de pares campo-valor internos (`HSET`, `HGET`), ideais para armazenar perfis de usuários e entidades com múltiplos atributos.
    - `Lists`: Listas encadeadas de strings ordenadas por inserção (`LPUSH`, `RPUSH`, `LPOP`, `RPOP`), ideais para filas FIFO/LIFO de mensagens.
    - `Sets`: Conjuntos matemáticos não-ordenados de strings únicas (`SADD`, `SREM`), com suporte a operações de interseção (`SINTER`), união (`SUNION`) e diferença (`SDIFF`).
    - `Sorted Sets (ZSET)`: Coleção de strings únicas onde cada membro é associado a um valor numérico de ponto flutuante denominado **score**. Os elementos são mantidos rigorosamente ordenados pelo seu score interno, viabilizando consultas rápidas por faixa de pontuação (`ZRANGE`, `ZREVRANGEBYSCORE`). Ideal para **rankings (*leaderboards*) em tempo real**.
    - `Bitmaps` e `HyperLogLog`: Estruturas compactas de alta precisão para rastreamento de bits (ex.: usuários ativos) e estimativa de cardinalidade com erro de 0,81% ocupando meros 12 KB de RAM (`PFADD`, `PFCOUNT`).
- **Mecanismos de Persistência em Disco:**
    - *RDB (Redis Database Snapshot):* Cria instantâneos binários compactos de toda a base de dados em intervalos pré-programados de tempo ou volume de escritas. Rápido para restaurar, mas pode perder dados gerados entre o último snapshot e o momento da falha.
    - *AOF (Append Only File):* Registra em disco todas as instruções de escrita recebidas pelo servidor à medida que acontecem em um log sequencial. Proporciona durabilidade máxima com impacto mínimo via `fsync` configurável, suportando compactação automática (*AOF rewrite*).
- **Recursos Chave:** Suporte nativo a tempo de expiração de chaves (**TTL - *Time-To-Live*** via `EXPIRE`), arquitetura Pub/Sub e algoritmos de bloqueios distribuídos (*Redlock*).

> ⚠️ **Alerta de Prova (FCC):**
> Atenção às questões da FCC sobre persistência no Redis: a banca costuma inverter RDB e AOF! Grave bem: **RDB faz snapshots pontuais de tempos em tempos** (ideal para backups compactos, mas com risco de perda recente); **AOF grava log de comandos de escrita continuamente** (durabilidade superior, análogo ao WAL de bancos relacionais).

### 2.3 Bancos de Famílias de Colunas (Wide-Column / Cassandra / HBase)

Projetados para armazenar volumes gigantescos de dados em clusters massivos com distribuição totalmente horizontal:

- **Modelo de Dados Bidimensional Esparso:** Os dados são organizados em linhas, onde cada linha possui uma chave de linha (*Row Key* ou *Partition Key*). Cada linha pode conter uma quantidade variável de colunas associadas a uma Família de Colunas (*Column Family*), e cada coluna contém um nome, um valor e um carimbo de tempo (*Timestamp*). Linhas diferentes na mesma tabela não precisam ter as mesmas colunas (espaço não alocado para colunas vazias, eliminando o custo de atributos nulos).
- **Arquitetura Descentralizada (*Masterless* / P2P no Apache Cassandra):**
    - Não existe um nó mestre ou coordenador fixo (*Single Point of Failure - SPOF*). Todos os nós do anel (*ring*) desempenham papéis idênticos.
    - Qualquer nó pode receber requisições de clientes, atuando como Coordenador pontual para aquela transação.
    - A comunicação interna entre nós do cluster opera por meio do **Gossip Protocol** para monitoramento contínuo do estado e saúde do sistema.
    - A persistência no disco utiliza estruturas de **LSM-Tree (*Log-Structured Merge-Tree*)**: as escritas vão primeiro para a memória RAM (*MemTable*) e para um log sequencial (*CommitLog*); quando a MemTable enche, é descarregada no disco em arquivos imutáveis chamados **SSTables (*Sorted String Tables*)**, periodicamente unificados por compactação.
- **Consultas e Casos de Uso:** O Cassandra adota a linguagem **CQL (*Cassandra Query Language*)**, que lembra a sintaxe do SQL, mas restringe severamente consultas que não utilizem a chave de partição (não há suporte para `JOIN` relacional arbitrário). É a solução perfeita para dados de séries temporais, registros massivos de telemetria IoT, histórico contábil imutável e logs de auditoria contínua.

### 2.4 Bancos Orientados a Grafos (Neo4j e Cypher)

Modelam os dados utilizando os conceitos formais da teoria dos grafos: **Vértices (Nós)**, **Arestas (Relacionamentos)** e **Propriedades**:

- **Labeled Property Graph (LPG):**
    - *Nós (Nodes):* Entidades do domínio (ex.: `:Pessoa`, `:Empresa`, `:Contrato`).
    - *Relacionamentos (Relationships):* Conexões direcionadas entre nós, obrigatoriamente tipadas (ex.: `-[:SOCIO_DE]->`, `-[:RECEBEU_REPASSE]->`).
    - *Propriedades (Properties):* Atributos em formato chave-valor atribuídos tanto aos nós quanto aos relacionamentos (ex.: `percentual_societario: 49.5`, `data_inicio: '2025-01-10'`).
- **Adjacência Livre de Índice (*Index-free Adjacency*):**
    - É o diferencial técnico mais cobrado em concursos. Em bancos relacionais, para relacionar tabelas, o motor precisa realizar operações de `JOIN` via índices secundários ou varreduras com custo que escala de acordo com o tamanho total da tabela.
    - No modelo de grafos nativo, cada nó armazena ponteiros físicos de memória diretos para todos os seus nós adjacentes.
    - **Vantagem de Performance:** A travessia de relacionamentos possui custo computacional em tempo constante $\mathcal{O}(1)$ por aresta percorrida. O tempo de execução da consulta depende exclusivamente do subgrafo visitado na vizinhança, e não do volume global de bilhões de registros armazenados no banco.
- **Linguagem Declarativa Cypher:**
    - Linguagem de consulta padrão de mercado para grafos que utiliza representação visual de arte ASCII:

```cypher
MATCH (auditor:Auditor {matricula: 'A123'})-[:FISCALIZA]->(contrato:Contrato)
MATCH (contrato)-[:EXECUTADO_POR]->(empresa:Empresa)
MATCH (socio:Pessoa)-[:SOCIO_DE]->(empresa)
WHERE contrato.valor > 1000000.00
RETURN auditor.nome, contrato.numero, empresa.razao_social, socio.nome
```

### 2.5 Matriz Comparativa e Casos de Uso no Controle Externo

| Família NoSQL | Tecnologia Típica | Complexidade de Escrita / Leitura | Modelo CAP | Aplicação Prática no Tribunal de Contas (TCE-GO) |
| :--- | :--- | :--- | :--- | :--- |
| **Documentos** | MongoDB | $\mathcal{O}(1)$ / $\mathcal{O}(\log N)$ | CP (geralmente) | Gestão de peças processuais digitalizadas, acórdãos e formulários dinâmicos de prestação de contas dos jurisdicionados. |
| **Chave-Valor** | Redis | $\mathcal{O}(1)$ em memória RAM | CP / AP | Cache de consultas analíticas pesadas, barramento de autenticação/sessões de usuários do Portal do Cidadão e contadores em tempo real. |
| **Wide-Column** | Cassandra | $\mathcal{O}(1)$ escrita LSM / $\mathcal{O}(\log N)$ | AP | Armazenamento de trilhas de auditoria contínua (*audit trails*), logs de transações orçamentárias de prefeituras e séries temporais de despesas públicas. |
| **Grafos** | Neo4j | $\mathcal{O}(1)$ por salto adjacente | CP | Mapeamento de redes societárias suspeitas, teias de empresas de fachada, identificação de laranjas e cartéis em processos licitatórios. |

---

## 3. Bancos de Dados Vetoriais e Inteligência Artificial

A revolução dos Modelos de Linguagem Grande (*Large Language Models - LLMs*) baseados na arquitetura *Transformer* impulsionou a necessidade de gerenciar, armazenar e consultar representações semânticas densas em alta dimensionalidade.

### 3.1 Embeddings: Do Texto Não-Estruturado ao Espaço Vetorial

Um **embedding** é a conversão algorítmica de um dado arbitrário não estruturado (documentos jurídicos, relatórios fiscais, imagens de obras públicas ou fragmentos de código) em um **vetor numérico denso contínuo** em um espaço multidimensional (tipicamente com 768, 1.536 ou 3.072 dimensões de números de ponto flutuante `float32`).

- **Propriedade Semântica Fundamental:** Redes neurais de embedding posicionam conceitos correlacionados em regiões geometricamente vizinhas no hiperespaço contínuo.
- Duas sentenças que expressem a mesma ideia semântica, ainda que com vocabulário formal e palavras inteiramente distintas (ex.: *"sobrepreço em pavimentação asfáltica"* e *"desvio orçamentário na compra de asfalto municipal"*), geram vetores densos com altíssima proximidade geométrica e angular.

```
Texto Bruto: "Edital com sobrepreço" ──► [Modelo Transformer] ──► Vetor: [0.15, -0.42, 0.88, ..., 0.05]
                                                                        (1.536 dimensões)
```

### 3.2 Métricas Matemáticas de Distância e Similaridade

Para determinar o grau de afinidade entre dois vetores $\mathbf{u}$ e $\mathbf{v}$ de dimensão $D$, utilizam-se métricas de distância ou similaridade no espaço vetorial:

1. **Similaridade de Cosseno (*Cosine Similarity*):**
    - Mede o cosseno do ângulo $\theta$ formado entre dois vetores densos:
     $$\text{Sim}_{\cos}(\mathbf{u}, \mathbf{v}) = \cos(\theta) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\| \|\mathbf{v}\|} = \frac{\sum_{i=1}^{D} u_i v_i}{\sqrt{\sum_{i=1}^{D} u_i^2} \sqrt{\sum_{i=1}^{D} v_i^2}}$$
    - **Variação:** Varia no intervalo de $[-1, +1]$:
    - $+1$: Vetores apontam para a exata mesma direção (máxima similaridade semântica).
    - $0$: Vetores ortogonais (independência semântica total).
    - $-1$: Vetores diametralmente opostos.
    - **Propriedade Crítica:** **Independe da magnitude (comprimento) dos vetores**. Isso a torna a métrica prioritária para comparação de textos em tarefas de busca semântica e sistemas de RAG, compensando variações no tamanho dos documentos de entrada.
    - A **Distância de Cosseno** é dada pelo complemento: $\text{Dist}_{\cos} = 1 - \text{Sim}_{\cos}$.

2. **Distância Euclidiana ($L_2$ Distance):**
    - Mede o comprimento do segmento de reta geométrico que une os dois pontos no espaço euclidiano:
     $$\|\mathbf{u} - \mathbf{v}\|_2 = \sqrt{\sum_{i=1}^{D} (u_i - v_i)^2}$$
    - Valores menores denotam maior proximidade física entre os vetores. É fortemente influenciada pela magnitude dos vetores.

3. **Produto Escalar (*Dot Product* / *Inner Product*):**
    - Soma ponderada dos produtos dos componentes:
     $$\mathbf{u} \cdot \mathbf{v} = \sum_{i=1}^{D} u_i v_i$$
    - Se os vetores estiverem **normalizados** para terem norma unitária ($\|\mathbf{u}\| = \|\mathbf{v}\| = 1$), o produto escalar coincide exatamente com a similaridade de cosseno, sendo computado com máxima aceleração por instruções vetoriais SIMD e tensores de GPUs.

### 3.3 Algoritmos de Busca Aproximada por Vizinhos Mais Próximos (ANN)

Em bases vetoriais de auditoria contendo centenas de milhares ou milhões de documentos, encontrar os $k$ vizinhos mais próximos através da comparação exaustiva de força bruta ($k$-NN exato) exige complexidade computacional $\mathcal{O}(N \times D)$, gerando lentidão inaceitável.

Para solucionar esse problema, empregam-se algoritmos de **ANN (*Approximate Nearest Neighbors*)**, que abrem mão de uma fração mínima de precisão absoluta (*recall*) em troca de redução de latência para a escala de milissegundos:

* **HNSW (Hierarchical Navigable Small World):**
    - Constrói uma estrutura em grafo multicamadas onde a camada superior possui arestas longas (permitindo saltos gigantescos pelo hiperespaço para localização aproximada da região), enquanto as camadas inferiores possuem conexões locais cada vez mais densas para refinamento fino da busca.
    - **Desempenho:** Complexidade de busca com escala logarítmica $\mathcal{O}(\log N)$, apresentando o melhor balanço da indústria entre taxa de acerto (*recall*) e velocidade de resposta.
* **IVF (Inverted File Index):**
    - Utiliza o algoritmo $K$-Means durante a fase de treinamento para particionar o espaço vetorial contínuo em centenas de centróides (células de Voronoi).
    - Cada centróide mantém uma lista invertida contendo os identificadores dos vetores que caíram em seu domínio. Durante a consulta, o algoritmo compara a consulta apenas com os centróides mais próximos e varre exclusivamente as listas associadas (*probe lists*).

### 3.4 Ecossistema Tecnológico: Extensão pgvector e Bancos Nativos

A indexação e recuperação de embeddings pode ser implementada por duas abordagens arquiteturais:

1. **Abordagem Integrada / Multimodelo (`pgvector` no PostgreSQL):**
    - Extensão de código aberto que acrescenta nativamente o tipo de dados `vector(dimensoes)` ao PostgreSQL.
    - Permite que uma tabela relacional clássica armazene o texto bruto, metadados de auditoria e a representação vetorial juntos:

```sql
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE acordaos_tce (
    id BIGSERIAL PRIMARY KEY,
    numero_processo VARCHAR(50) NOT NULL,
    data_julgamento DATE,
    conteudo_ementa TEXT,
    vetor_embedding vector(1536) -- Embedding gerado pelo modelo
);

-- Criação de índice vetorial de alta performance HNSW
CREATE INDEX idx_acordaos_hnsw ON acordaos_tce 
USING hnsw (vetor_embedding vector_cosine_ops);

-- Consulta por similaridade semântica (operador <=> calcula a distância de cosseno)
SELECT numero_processo, conteudo_ementa, 
       1 - (vetor_embedding <=> '[0.012, -0.045, ...]'::vector) AS similaridade
FROM acordaos_tce
ORDER BY vetor_embedding <=> '[0.012, -0.045, ...]'::vector
LIMIT 5;
```

    - Operadores de distância do `pgvector`:
    - `<->`: Distância Euclidiana ($L_2$).
    - `<=>`: Distância de Cosseno ($1 - \text{Similaridade de Cosseno}$).
    - `<#>`: Produto Escalar Negativo.

2. **Bancos de Dados Vetoriais Nativos Especializados:**
    - Softwares projetados exclusivamente para o ciclo de vida vetorial distribuído: **Pinecone** (SaaS nativo de nuvem), **Milvus** (banco distribuído de alta escala em Go/C++), **Qdrant** (motor em Rust de altíssima eficiência de memória) e **Chroma** (banco leve voltado ao ecossistema Python).
    - Oferecem recursos de particionamento dinâmico em memória e filtragem por metadados pré e pós-busca vetorial (*payload-based filtering*).

---

## 4. Questões Comentadas (FCC)

### Questão 01
**(FCC - DPE-RS - Analista de Tecnologia da Informação)**
Um arquiteto de software de um tribunal público avalia a infraestrutura de dados para dois projetos de modernização institucional:

1. Uma plataforma analítica de combate à corrupção encarregada de mapear redes de parentesco, cruzamento de quadros societários e rastreamento de laranjas em contratações de órgãos jurisdicionados.
2. Um serviço de autenticação e controle de tráfego de alta concorrência que demanda armazenamento em memória de tokens transitórios de acesso e sessões de usuários com tempo de vida definido (TTL).

Considerando as famílias NoSQL mais eficientes para os casos e as regras de sistemas distribuídos do Teorema CAP, é correto afirmar:

* **A)** O Projeto 1 deve utilizar Banco Chave-Valor; o Projeto 2 deve utilizar Banco de Grafos; e sistemas distribuídos sob partição de rede garantem Consistência e Disponibilidade plenas simultaneamente.
* **B)** O Projeto 1 deve utilizar Banco de Grafos (ex.: Neo4j); o Projeto 2 deve utilizar Banco Chave-Valor em memória (ex.: Redis); e, em sistemas distribuídos sob partição de rede (P), é compulsório optar entre Consistência estrita (C) ou Disponibilidade (A).
* **C)** O Projeto 1 deve utilizar Banco de Famílias de Colunas; o Projeto 2 deve utilizar Banco de Documentos; e o Teorema CAP não se aplica a arquiteturas NoSQL com persistência em disco.
* **D)** O Projeto 1 deve utilizar Banco de Documentos; o Projeto 2 deve utilizar Banco Relacional Monolítico; e o modelo BASE substitui integralmente a necessidade de tolerância a partições físicas.
* **E)** O Projeto 1 deve utilizar Banco de Séries Temporais; o Projeto 2 deve utilizar Banco Orientado a Objetos; e transações ACID distribuídas mantêm disponibilidade total mesmo com isolamento físico de rede entre datacenters.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Houve inversão completa das soluções tecnológicas indicadas, além da afirmação errônea de que é possível garantir C e A simultaneamente na vigência de partições de rede.
> - **B)** **Correta.** 
>     - No Projeto 1, a análise de redes societárias e parentescos exige travessia profunda e multidirecional de arestas; o modelo de **Grafos** (como o Neo4j) é a solução sob medida, viabilizando navegação com custo $\mathcal{O}(1)$ por nó explorado (*Index-free Adjacency*).
>     - No Projeto 2, o gerenciamento de sessões com expiração automática (TTL) requer armazenamento ultrarrápido em RAM; o modelo **Chave-Valor** (como o Redis) é o padrão da indústria.
>     - Pelo **Teorema CAP**, como falhas de comunicação em rede física (**P**) são contingências inevitáveis em sistemas distribuídos, o arquiteto é obrigado a arbitrar entre **Consistência (C)** ou **Disponibilidade (A)** durante o evento de partição.
> - **C)** Incorreta. Bancos de famílias de colunas são otimizados para ingestão massiva e séries temporais, sendo inadequados para travessia de grafos de relacionamentos em teia; ademais, o Teorema CAP aplica-se formalmente a qualquer sistema distribuído em rede.
> - **D)** Incorreta. O modelo de documentos lida com coleções semiestruturadas em árvore, sendo ineficiente para detectar conexões de grafos em anel ou cíclicas sem múltiplos loops de aplicação.
> - **E)** Incorreta. Sistemas distribuídos com particionamento de rede não conseguem sustentar ACID clássico pleno sem degradar totalmente a disponibilidade do sistema perante os clientes dos nós isolados.
> 
> **Gabarito: B**

---

### Questão 02
**(FCC - TCE-PI - Auditor de Controle Externo - Tecnologia da Informação)**
A implementação de sistemas de Inteligência Artificial Generativa e Arquiteturas de Recuperação Aumentada por Geração (RAG) em órgãos de controle externo demanda a utilização de bancos de dados vetoriais para indexação semântica de peças processuais e relatórios de auditoria. Sobre os conceitos matemáticos e a operação de bancos de dados vetoriais, assinale a alternativa correta:

* **A)** Os embeddings transformam textos em hashes criptográficos MD5, permitindo que a busca vetorial localize documentos exclusivamente quando houver correspondência exata de todos os caracteres alfanuméricos.
* **B)** A similaridade de cosseno avalia o cosseno do ângulo formado entre dois vetores densos em um hiperespaço multidimensional, medindo a orientação semântica relativa de forma independente da magnitude do comprimento dos textos.
* **C)** Os algoritmos de busca aproximada por vizinhos mais próximos (ANN), como o HNSW, utilizam exclusivamente a varredura linear exaustiva de força bruta em 100% da base vetorial, garantindo complexidade $\mathcal{O}(N)$.
* **D)** O PostgreSQL não possui extensões de código aberto para tratamento de dados vetoriais, sendo mandatória a contratação de ferramentas proprietárias externas em nuvem para execução de buscas por similaridade.
* **E)** Em espaços vetoriais densos, um valor de similaridade de cosseno igual a zero indica que os conceitos representados possuem máxima correlação e equivalência semântica absoluta.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Hashes criptográficos (como MD5 ou SHA-256) possuem o chamado *efeito avalanche*: qualquer alteração mínima gera um hash completamente diferente. Já os embeddings gerados por LLMs realizam mapeamento contínuo onde vetores espacialmente próximos representam textos semanticamente afins.
> - **B)** **Correta.** A métrica de **Similaridade de Cosseno** calcula $\cos(\theta) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\| \|\mathbf{v}\|}$, mensurando a orientação angular dos vetores sem sofrer distorções causadas pela variação no comprimento bruto dos textos analisados, constituindo a métrica padrão para busca textual em RAG.
> - **C)** Incorreta. A varredura linear completa em todos os vetores é a definição da busca exata por força bruta ($k$-NN exato). Algoritmos **ANN** (como o **HNSW**) utilizam grafos de mundo pequeno navegáveis multicamadas para navegar no espaço vetorial em tempo logarítmico $\mathcal{O}(\log N)$.
> - **D)** Incorreta. O PostgreSQL possui a consagrada extensão aberta **`pgvector`**, que viabiliza o armazenamento nativo do tipo `vector`, criação de índices `hnsw` e cálculo de distância de cosseno via operador `<=>`.
> - **E)** Incorreta. Similaridade de cosseno igual a zero denota vetores ortogonais ($\theta = 90^\circ$), o que significa **independência semântica total**, e não máxima equivalência (que seria indicada pelo valor $+1$).
> 
> **Gabarito: B**

---

### Questão 03
**(FCC - TRT-2ª Região - Analista Judiciário - Tecnologia da Informação)**
No banco de dados NoSQL Redis, o gerenciamento eficiente da memória RAM e as opções de salvaguarda dos dados em disco baseiam-se em estruturas e parâmetros bem definidos. Sobre o funcionamento do Redis, é correto afirmar:

* **A)** O tipo de dados *Sorted Set (ZSET)* armazena elementos duplicados sequenciados exclusivamente pelo horário de inserção na fila.
* **B)** O mecanismo de persistência RDB (*Redis Database*) realiza a gravação síncrona de cada instrução individual de escrita em um arquivo sequencial contínuo imediatamente após a execução do comando.
* **C)** O mecanismo de persistência AOF (*Append Only File*) atua como um log transacional sequencial, registrando em disco os comandos executados que modificam os dados, viabilizando a restauração fiel do estado do banco após falhas.
* **D)** O comando de expiração temporal TTL (*Time-To-Live*) não existe no Redis, demandando rotinas em scripts externos para varredura e exclusão manual de chaves obsoletas.
* **E)** A estrutura de dados *Hash* permite o armazenamento de apenas uma chave simples atrelada a uma string escalar, não suportando subcampos internos.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O *Sorted Set (ZSET)* armazena exclusivamente elementos **únicos** (sem duplicatas), cada um obrigatoriamente associado a um valor numérico de ponto flutuante denominado **score**, sendo ordenados por esse score (e não pela ordem de inserção cronológica).
> - **B)** Incorreta. A gravação síncrona de cada instrução em arquivo contínuo de log é responsabilidade do mecanismo **AOF**. O **RDB** gera instantâneos compactos pontuais (*point-in-time snapshots*) em intervalos de tempo configuráveis.
> - **C)** **Correta.** O mecanismo **AOF (*Append Only File*)** atua de forma contínua registrando cada operação de mutação da base em um arquivo de log, de modo análogo ao Write-Ahead Logging (WAL) dos bancos relacionais, possibilitando a recomposição precisa da base em memória durante o reinício do serviço.
> - **D)** Incorreta. O Redis fornece suporte nativo completo ao **TTL (*Time-To-Live*)** por meio de comandos consagrados como `EXPIRE`, `PEXPIRE` e `SETEX`.
> - **E)** Incorreta. A estrutura `Hash` no Redis implementa um mapa associativo que aceita múltiplos pares de campo-valor internos associados a uma mesma chave principal.
> 
> **Gabarito: C**

---

### Questão 04
**(FCC - TCE-RS - Auditor Público Externo - Tecnologia da Informação)**
Em ambientes de computação distribuída e bancos de dados NoSQL projetados para suportar partições de rede com alta disponibilidade, a teoria de sistemas adota com frequência o modelo **BASE** em contraposição ao modelo **ACID** dos SGBDs relacionais clássicos. O pilar fundamental do modelo BASE que estabelece que, se nenhuma nova atualização for enviada ao sistema, ao longo do tempo todas as réplicas convergentes propagarão seus dados e alcançarão o mesmo estado consolidado é denominado:

* **A)** Soft State.
* **B)** Basically Available.
* **C)** Eventual Consistency.
* **D)** Strict Serializability.
* **E)** Atomic Broadcast.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. *Soft State* (Estado Maleável) estabelece que o estado dos nós do cluster pode mudar ou oscilar com o tempo por sincronização de réplicas em segundo plano, mesmo que não haja novas entradas externas.
> - **B)** Incorreta. *Basically Available* (Disponibilidade Básica) determina que o sistema continuará operando e respondendo aos clientes de maneira tolerante a falhas locais, admitindo degradação controlada.
> - **C)** **Correta.** O conceito de **Eventual Consistency (Consistência Eventual)** postula que, cessadas novas submissões de dados ao cluster, todas as réplicas do sistema distribuído trocarão mensagens de reconciliação (via quóruns, gossip protocol ou anti-entropy) e convergirão eventualmente para um estado idêntico e consistente.
> - **D)** Incorreta. *Strict Serializability* é a garantia mais rígida de consistência do modelo relacional/linearizável (ACID), sendo exatamente o oposto do modelo flexível BASE.
> - **E)** Incorreta. *Atomic Broadcast* é uma primitiva de comunicação de consenso distribuído, não um pilar conceituado no acrônimo BASE.
> 
> **Gabarito: C**

---

### Questão 05
**(FCC - TRF-3ª Região - Analista Judiciário - Informática)**
Ao planejar uma solução tecnológica para identificar fraudes tributárias sofisticadas caracterizadas por blindagem patrimonial em teias complexas de sócios cruzados, empresas coligadas e holdings familiares com 6 a 8 níveis de relacionamento hierárquico, uma equipe técnica optou pelo uso de um banco de dados orientado a grafos nativo (como o Neo4j).
A decisão técnica justifica-se primariamente porque:

* **A)** Os bancos de dados orientados a grafos convertem as instruções de consulta em planilhas tabulares CSV, eliminando a dependência de processadores multinúcleo.
* **B)** Os bancos de grafos nativos utilizam o princípio da Adjacência Livre de Índice (*Index-free Adjacency*), no qual cada nó armazena referências de ponteiros diretos para seus nós vizinhos, tornando o custo de navegação dependente apenas do subgrafo percorrido, evitando a explosão combinatória de múltiplos JOINs relacionais sucessivos.
* **C)** Os grafos de propriedades proíbem a inclusão de atributos descritivos nas arestas de relacionamento, simplificando os cálculos de álgebra booleana.
* **D)** Os bancos de dados relacionais tradicionais não admitem a execução de junções entre tabelas que possuam chaves primárias do tipo inteiro.
* **E)** A linguagem Cypher baseia-se exclusivamente em comandos imperativos procedurais em linguagem C, sendo compilada estaticamente durante a inicialização do cluster.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Bancos de grafos nativos utilizam armazenamento em arquivos binários contíguos estruturados de nós e arestas cacheados agressivamente na memória RAM.
> - **B)** **Correta.** O recurso técnico chave dos bancos de grafos é a **Adjacência Livre de Índice (*Index-free Adjacency*)**: cada nó armazena ponteiros físicos diretos de memória para os nós vizinhos interligados. Desse modo, o custo para saltar de uma entidade para outra é $\mathcal{O}(1)$ por nó explorado, eliminando os múltiplos `JOINs` sucessivos e pesados que provocam colapso de planos de execução em bancos relacionais em análises profundas.
> - **C)** Incorreta. No modelo *Labeled Property Graph*, tanto os nós quanto os relacionamentos (arestas) podem livremente armazenar atributos de propriedades (ex.: percentual de cotas, data de entrada na sociedade).
> - **D)** Incorreta. Bancos relacionais realizam plenamente junções sobre colunas inteiras; o problema reside na complexidade exponencial e no I/O excessivo ao realizar muitos joins em tabelas com milhões de linhas.
> - **E)** Incorreta. A linguagem **Cypher** é uma linguagem de consulta de alto nível puramente **declarativa** orientada a casamento de padrões visuais em arte ASCII (`MATCH (n)-[r]->(m)`).
> 
> **Gabarito: B**
