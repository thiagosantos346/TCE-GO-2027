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

1. [Teorema CAP, Teorema PACELC e o Modelo BASE](#1-teorema-cap-teorema-pacelc-e-o-modelo-base)
    1. [Teorema CAP (Eric Brewer / Gilbert & Lynch)](#11-teorema-cap-eric-brewer-gilbert-lynch)
    2. [O Teorema PACELC](#12-o-teorema-pacelc)
    3. [Modelo BASE vs. Propriedades ACID](#13-modelo-base-vs-propriedades-acid)
    4. [Teste 278](#Teste-278)
    5. [Teste 279](#Teste-279)
    6. [Teste 280](#Teste-280)
2. [As Quatro Famílias de Bancos de Dados NoSQL](#2-as-quatro-familias-de-bancos-de-dados-nosql)
    1. [Bancos Orientados a Documentos (MongoDB)](#21-bancos-orientados-a-documentos-mongodb)
    2. [Bancos Chave-Valor (Redis)](#22-bancos-chave-valor-redis)
    3. [Bancos de Famílias de Colunas (Wide-Column / Cassandra / HBase)](#23-bancos-de-familias-de-colunas-wide-column-cassandra-hbase)
    4. [Bancos Orientados a Grafos (Neo4j e Cypher)](#24-bancos-orientados-a-grafos-neo4j-e-cypher)
    5. [Matriz Comparativa e Casos de Uso no Controle Externo](#25-matriz-comparativa-e-casos-de-uso-no-controle-externo)
    6. [Teste 281](#Teste-281)
    7. [Teste 282](#Teste-282)
    8. [Teste 283](#Teste-283)
    9. [Teste 284](#Teste-284)
    10. [Teste 285](#Teste-285)
3. [Bancos de Dados Vetoriais e Inteligência Artificial](#3-bancos-de-dados-vetoriais-e-inteligencia-artificial)
    1. [Embeddings: Do Texto Não-Estruturado ao Espaço Vetorial](#31-embeddings-do-texto-nao-estruturado-ao-espaco-vetorial)
    2. [Métricas Matemáticas de Distância e Similaridade](#32-metricas-matematicas-de-distancia-e-similaridade)
    3. [Algoritmos de Busca Aproximada por Vizinhos Mais Próximos (ANN)](#33-algoritmos-de-busca-aproximada-por-vizinhos-mais-proximos-ann)
    4. [Ecossistema Tecnológico: Extensão pgvector e Bancos Nativos](#34-ecossistema-tecnologico-extensao-pgvector-e-bancos-nativos)
    5. [Teste 286](#Teste-286)
    6. [Teste 287](#Teste-287)
    7. [Teste 288](#Teste-288)
4. [🌐 Fontes Oficiais e Referências Bibliográficas](#fontes-oficiais-e-referencias-bibliograficas)

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

### Teste 278
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Ciências da Computação, Sistemas de Informação...)**
Um Auditor de Controle Externo precisa processar grandes volumes de dados de georreferenciação de obras públicas em Santa Catarina. Para otimizar o tempo, ele utiliza o paradigma MapReduce. Na fase de MAP desse paradigma, a ação principal executada nos blocos de dados distribuídos é

* **A)** consolidar todos os resultados parciais num único servidor central.
* **B)** filtrar e ordenar os dados por meio de funções de agregação final.
* **C)** transformar os dados de entrada em pares de chave-valor.
* **D)** eliminar permanentemente os dados duplicados na base de origem.
* **E)** realizar o backup dos dados em nós de redundância.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "consolidar todos os resultados parciais num único servidor central". De acordo com a teoria estudada em *2.2 Bancos Chave-Valor (Redis)*, arquitetura em Memória RAM: O Redis (*Remote Dictionary Server*) opera primariamente na memória principal do servidor, propiciando tempos de resposta na escala de dezenas de microssegundos.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "filtrar e ordenar os dados por meio de funções de agregação final". De acordo com a teoria estudada em *2.2 Bancos Chave-Valor (Redis)*, `Hashes`: Mapas associativos de pares campo-valor internos (`HSET`, `HGET`), ideais para armazenar perfis de usuários e entidades com múltiplos atributos.
> - **C)** **Correta.** Conforme fundamentado na seção *2.2 Bancos Chave-Valor (Redis)* deste guia, o modelo mais simples, minimalista e veloz. Armazena pares formados por uma chave única (string) mapeada para um valor (escalar primitivo, objeto binário ou estrutura complexa). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "transformar os dados de entrada em pares de chave-valor".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "eliminar permanentemente os dados duplicados na base de origem". De acordo com a teoria estudada em *1.3 Modelo BASE vs. Propriedades ACID*, d - Durabilidade: Os dados comitados persistem permanentemente em disco, resistindo a falhas elétricas.: Propagação de Réplicas: Replicação assíncrona tolerante a latência, utilizando protocolos como *Gossip Protocol* e algoritmos de quórum configuráveis ($R + W > N$).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "realizar o backup dos dados em nós de redundância". De acordo com a teoria estudada em *2.2 Bancos Chave-Valor (Redis)*, *RDB (Redis Database Snapshot):* Cria instantâneos binários compactos de toda a base de dados em intervalos pré-programados de tempo ou volume de escritas. Rápido para restaurar, mas pode perder dados gerados entre o último snapshot e o momento da falha.
>
> **Gabarito: C**

---

### Teste 279
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Ciência de Dados)**
Considere o Sistema de Concursos de uma empresa hipotética que adota um Sistema de Gerenciamento de Banco de Dados (SGDB) relacional. A primeira tabela construída no banco foi Tabela_Candidato, que possui os seguintes campos: candidato_ID; candidato_Nome; candidato_CPF. A segunda tabela construída foi a Tabela_Concurso, que possui os seguintes campos: concurso_ID; candidato_ID; concurso_Nome; concurso_Cargo. No contexto dos bancos de dados relacionais, é correto afirmar que

* **A)** o campo candidato_ID é uma chave estrangeira na Tabela_Candidato.
* **B)** o campo candidato_ID é uma chave primária na Tabela_Concurso.
* **C)** a Tabela_Candidato está incompleta, haja vista que não possui informação do concurso que o candidato pode fazer.
* **D)** dá forma como o banco de dados foi concebido, só é possível lançar um concurso por candidado.
* **E)** a inserção da chave estrangeira candidato_ID na tabela Tabela_Concurso, permite o lançamento de um candidato em vários concursos. Realização

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "o campo candidato_ID é uma chave estrangeira na Tabela_Candidato". De acordo com a teoria estudada em *3.4 Ecossistema Tecnológico: Extensão pgvector e Bancos Nativos*, permite que uma tabela relacional clássica armazene o texto bruto, metadados de auditoria e a representação vetorial juntos.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "o campo candidato_ID é uma chave primária na Tabela_Concurso". De acordo com a teoria estudada em *2.2 Bancos Chave-Valor (Redis)*, `Lists`: Listas encadeadas de strings ordenadas por inserção (`LPUSH`, `RPUSH`, `LPOP`, `RPOP`), ideais para filas FIFO/LIFO de mensagens.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "a Tabela_Candidato está incompleta, haja vista que não possui informação do concurso que o candidato pode fazer". De acordo com a teoria estudada em *2.3 Bancos de Famílias de Colunas (Wide-Column / Cassandra / HBase)*, modelo de Dados Bidimensional Esparso: Os dados são organizados em linhas, onde cada linha possui uma chave de linha (*Row Key* ou *Partition Key*).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "dá forma como o banco de dados foi concebido, só é possível lançar um concurso por candidado". De acordo com a teoria estudada em *2.1 Bancos Orientados a Documentos (MongoDB)*, armazenam dados na forma de documentos semiestruturados, geralmente serializados em formatos como JSON, BSON (*Binary JSON*) ou XML.
> - **E)** **Correta.** Conforme fundamentado na seção *2.4 Bancos Orientados a Grafos (Neo4j e Cypher)* deste guia, é o diferencial técnico mais cobrado em concursos. Em bancos relacionais, para relacionar tabelas, o motor precisa realizar operações de `JOIN` via índices secundários ou varreduras com custo que escala de acordo com o tamanho total da tabela. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "a inserção da chave estrangeira candidato_ID na tabela Tabela_Concurso, permite o lançamento de um candidato em...".
>
> **Gabarito: E**

---

### Teste 280
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Ciência de Dados)**
Com relação aos bancos de dados NoSQL orientados a documentos, avalie se as afirmativas a seguir são verdadeiras (V) ou falsas (F). ( ) Utilizam um modelo de dados flexível, e permitem o armazenado de dados em formatos como JSON e BSON. ( ) São comumente mais escaláveis verticalmente do que bancos de dados relacionais, permitindo dessa forma a distribuição de dados entre múltiplos servidores. ( ) Nesse tipo de banco de dados, a normalização dos dados é frequentemente utilizada para melhorar a consistência dos dados e evitar redundância. As afirmativas são, respectivamente,

* **A)** V – V – F.
* **B)** V – V – V.
* **C)** V – F – F.
* **D)** F – F – V.
* **E)** F – V – F

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "V – V – F". De acordo com a teoria estudada em *1.3 Modelo BASE vs. Propriedades ACID*, enquanto os bancos relacionais transacionais regem-se pelo rigor determinístico do modelo ACID, os sistemas NoSQL distribuídos apoiam-se no paradigma flexível do modelo BASE.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "V – V – V". De acordo com a teoria estudada em *2.1 Bancos Orientados a Documentos (MongoDB)*, *Sharding:* Distribuição horizontal física dos documentos entre múltiplos servidores (*shards*) guiada por uma Chave de Partição (*Shard Key*).
> - **C)** **Correta.** Conforme fundamentado na seção *2.1 Bancos Orientados a Documentos (MongoDB)* deste guia, armazenam dados na forma de documentos semiestruturados, geralmente serializados em formatos como JSON, BSON (*Binary JSON*) ou XML. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "V – F – F".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "F – F – V". De acordo com a teoria estudada em *2.1 Bancos Orientados a Documentos (MongoDB)*, bSON (Binary JSON): Extensão binária do JSON que viabiliza tipos primitivos adicionais não suportados pelo JSON textual puro, como tipos `Date` nativos, inteiros de 64 bits (`long`), decimais de alta precisão e dados binários brutos, otimizando a velocidade de parseamento e travessia.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "F – V – F". De acordo com a teoria estudada em *1. Teorema CAP, Teorema PACELC e o Modelo BASE*, o movimento NoSQL (*Not Only SQL*) surgiu para contornar as restrições físicas de escalabilidade vertical de bancos relacionais monolíticos em cenários de processamento massivo de dados (*Big Data*), viabilizando esquemas dinâmicos (*schemaless*) e particionamento horizontal maciço (*sharding*).
>
> **Gabarito: C**

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

### Teste 281
**(FGV – TJ/MT – 2024 – Analista Judiciario Tecnologia Da Informacao)**
Os bancos de dados NoSQL são uma categoria de sistemas de gerenciamento de banco de dados (SGBD) projetados para lidar com dados não estruturados ou semiestruturados, ou seja, dados que não seguem um modelo de esquema rígido como o relacional (SQL). O termo NoSQL (que originalmente significava “sem SQL”) evoluiu para se referir a “Not Only SQL”, destacando a flexibilidade dessas bases de dados em relação aos modelos tradicionais. No contexto dos bancos de dados NoSQL, bancos de dados do tipo documento

* **A)** armazenam dados em tabelas estruturadas, com linhas e colunas, semelhantes aos bancos de dados relacionais.
* **B)** utilizam um modelo de grafos para representar e armazenar dados complexos, como relações entre entidades.
* **C)** são projetados para garantir transações ACID em todos os casos, oferecendo suporte a operações complexas de leitura e escrita.
* **D)** armazenam dados em um modelo de chave-valor, onde cada chave corresponde a um valor específico.
* **E)** armazenam dados em formato JSON, BSON ou XML, permitindo flexibilidade para armazenar diferentes tipos de informações em um único documento.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "armazenam dados em tabelas estruturadas, com linhas e colunas, semelhantes aos bancos de dados relacionais". De acordo com a teoria estudada em *2.1 Bancos Orientados a Documentos (MongoDB)*, bSON (Binary JSON): Extensão binária do JSON que viabiliza tipos primitivos adicionais não suportados pelo JSON textual puro, como tipos `Date` nativos, inteiros de 64 bits (`long`), decimais de alta precisão e dados binários brutos, otimizando a velocidade de parseamento e travessia.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "utilizam um modelo de grafos para representar e armazenar dados complexos, como relações entre entidades". De acordo com a teoria estudada em *1. Teorema CAP, Teorema PACELC e o Modelo BASE*, o movimento NoSQL (*Not Only SQL*) surgiu para contornar as restrições físicas de escalabilidade vertical de bancos relacionais monolíticos em cenários de processamento massivo de dados (*Big Data*), viabilizando esquemas dinâmicos (*schemaless*) e particionamento horizontal maciço (*sharding*).
> - **C)** **Incorreta.** A opção promove generalização excessiva que desconsidera as condições técnicas e normativas ao afirmar que "são projetados para garantir transações ACID em todos os casos, oferecendo suporte a operações complexas de...". De acordo com a teoria estudada em *2.5 Matriz Comparativa e Casos de Uso no Controle Externo*, família NoSQL: Tecnologia Típica — Complexidade de Escrita / Leitura — Modelo CAP — Aplicação Prática no Tribunal de Contas (TCE-GO).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "armazenam dados em um modelo de chave-valor, onde cada chave corresponde a um valor específico". De acordo com a teoria estudada em *2.3 Bancos de Famílias de Colunas (Wide-Column / Cassandra / HBase)*, modelo de Dados Bidimensional Esparso: Os dados são organizados em linhas, onde cada linha possui uma chave de linha (*Row Key* ou *Partition Key*).
> - **E)** **Correta.** Conforme fundamentado na seção *2.1 Bancos Orientados a Documentos (MongoDB)* deste guia, armazenam dados na forma de documentos semiestruturados, geralmente serializados em formatos como JSON, BSON (*Binary JSON*) ou XML. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/MT/2024) ao estabelecer que "armazenam dados em formato JSON, BSON ou XML, permitindo flexibilidade para armazenar diferentes tipos de...".
>
> **Gabarito: E**

---

### Teste 282
**(FGV – TJ/AP – 2023 – Analista Judiciario Apoio Especializado Tecnologia Da Informacao Desenvolvimento De Sistemas)**
A equipe de sistemas do TJAP precisa analisar o papel das camadas de persistência em bancos de dados e como elas contribuem para o desenvolvimento dos sistemas. Para tanto, com a intenção de ajudar nesse processo de análise, as camadas de persistência:

* **A)** são exclusivas para bancos de dados NoSQL, utilizando bibliotecas como HBase e Cassandra;
* **B)** proporcionam interfaces que permitem a leitura, gravação e manipulação dos dados armazenados, como JDBC e ADO.NET;
* **C)** são responsáveis pela interface gráfica dos sistemas de bancos de dados, usando bibliotecas como Hibernate e Entity Framework;
* **D)** gerenciam a persistência de dados no armazenamento e as bibliotecas SQLite e MongoDB são exemplos dessa abordagem;
* **E)** focam exclusivamente a otimização de consultas SQL, e bibliotecas como LINQ e Django ORM são amplamente utilizadas nesse contexto.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "são exclusivas para bancos de dados NoSQL, utilizando bibliotecas como HBase e Cassandra". De acordo com a teoria estudada em *2.3 Bancos de Famílias de Colunas (Wide-Column / Cassandra / HBase)*, projetados para armazenar volumes gigantescos de dados em clusters massivos com distribuição totalmente horizontal.
> - **B)** **Correta.** Conforme fundamentado na seção *2.2 Bancos Chave-Valor (Redis)* deste guia, `Strings`: O tipo básico fundamental (suporta texto, blobs de até 512 MB ou inteiros/floats com manipulação atômica via `INCR`, `DECR`, `INCRBY`). Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/AP/2023) ao estabelecer que "proporcionam interfaces que permitem a leitura, gravação e manipulação dos dados armazenados, como JDBC e ADO.NET".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "são responsáveis pela interface gráfica dos sistemas de bancos de dados, usando bibliotecas como Hibernate e...". De acordo com a teoria estudada em *2.1 Bancos Orientados a Documentos (MongoDB)*, aggregation Pipeline: Framework de análise de dados no MongoDB estruturado em etapas sequenciais compostas por operadores.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "gerenciam a persistência de dados no armazenamento e as bibliotecas SQLite e MongoDB são exemplos dessa abordagem". De acordo com a teoria estudada em *1.1 Teorema CAP (Eric Brewer / Gilbert & Lynch)*, sistemas CP: Priorizam Consistência. Em caso de quebra de partição, os nós isolados rejeitam requisições para evitar leituras defasadas ou escritas conflitantes (sacrificam a Disponibilidade). Exemplos: MongoDB, Redis Cluster, HBase, CockroachDB.
> - **E)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "focam exclusivamente a otimização de consultas SQL, e bibliotecas como LINQ e Django ORM são amplamente utilizadas...". De acordo com a teoria estudada em *2.4 Bancos Orientados a Grafos (Neo4j e Cypher)*, o tempo de execução da consulta depende exclusivamente do subgrafo visitado na vizinhança, e não do volume global de bilhões de registros armazenados no banco.
>
> **Gabarito: B**

---

### Teste 283
**(FGV – TRT/DA – 2025 – Analista Judiciario Area Apoio Especializado Tecnologia Da Informacao)**
O Sistema Gerenciador de Bancos de Dados (SGBD) Oracle 21c oferece diversos tipos de índices. Índices são estruturas opcionais, associadas a uma tabela ou cluster de tabelas que podem acelerar o acesso aos dados. Com relação aos índices desse SGBD, analise as afirmativas a seguir. I. Índices podem ser exclusivos ou não exclusivos. Índices exclusivos garantem que nenhuma das duas linhas de uma tabela tenha valores duplicados na coluna ou mais colunas- chave. Já Índices não exclusivos permitem valores duplicados na coluna ou nas colunas indexadas. II. Índices de árvores B são o tipo de índice padrão do Oracle. Esse tipo possui diversos subtipos, por exemplo, índices de chave inversa, índices descendentes e índices de junção de clusteres de tabelas. III. Existem índices que não usam estruturas de árvore B, por exemplo, índices de junção de bitmap e bitmap, índices baseados em funções e índices de domínio de aplicação. Está correto o que se afirma em

* **A)** I, apenas.
* **B)** II, apenas.
* **C)** III, apenas.
* **D)** I e II, apenas.
* **E)** I e III, apenas.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I, apenas". De acordo com a teoria estudada em *2.3 Bancos de Famílias de Colunas (Wide-Column / Cassandra / HBase)*, modelo de Dados Bidimensional Esparso: Os dados são organizados em linhas, onde cada linha possui uma chave de linha (*Row Key* ou *Partition Key*).
> - **B)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II, apenas". De acordo com a teoria estudada em *2.3 Bancos de Famílias de Colunas (Wide-Column / Cassandra / HBase)*, cada linha pode conter uma quantidade variável de colunas associadas a uma Família de Colunas (*Column Family*), e cada coluna contém um nome, um valor e um carimbo de tempo (*Timestamp*).
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "III, apenas". De acordo com a teoria estudada em *2.3 Bancos de Famílias de Colunas (Wide-Column / Cassandra / HBase)*, linhas diferentes na mesma tabela não precisam ter as mesmas colunas (espaço não alocado para colunas vazias, eliminando o custo de atributos nulos).
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e II, apenas". De acordo com a teoria estudada em *2.3 Bancos de Famílias de Colunas (Wide-Column / Cassandra / HBase)*, a comunicação interna entre nós do cluster opera por meio do Gossip Protocol para monitoramento contínuo do estado e saúde do sistema.
> - **E)** **Correta.** Conforme fundamentado na seção *2.4 Bancos Orientados a Grafos (Neo4j e Cypher)* deste guia, é o diferencial técnico mais cobrado em concursos. Em bancos relacionais, para relacionar tabelas, o motor precisa realizar operações de `JOIN` via índices secundários ou varreduras com custo que escala de acordo com o tamanho total da tabela. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT/DA/2025) ao estabelecer que "I e III, apenas".
>
> **Gabarito: E**

---

### Teste 284
**(FGV – TJ/AP – 2023 – Analista Judiciario Apoio Especializado Tecnologia Da Informacao Banco De Dados)**
João, administrador de banco de dados, deverá projetar um banco de dados Oracle de registro de alunos que contenha várias tabelas para armazenar informações acadêmicas:  A tabela “Aluno” armazena informações sobre alunos.  A tabela “Notas_Aluno” armazena informações sobre as notas do aluno.  Ambas as tabelas têm uma coluna chamada “Aluno_ID”.  A coluna “Aluno_ID” na tabela “Aluno” é uma chave primária. João deverá criar a chave estrangeira na coluna “aluno_ID” da tabela “Notas_Aluno” para relacionar-se com a coluna “aluno_ID” da tabela “Aluno”. Para isso, João deverá utilizar o seguinte comando:

* **A)** CREATE TABLE notas_aluno (aluno_ID NUMBER(12), media_notas NUMBER(4,3), CONSTRAINT aluno_ID_fk REFERENCES aluno(aluno_ID));
* **B)** CREATE TABLE notas_aluno (aluno_ID NUMBER(12), media_notas NUMBER(4,3), CONSTRAINT FOREIGN KEY (aluno_ID) REFERENCES aluno (aluno_ID));
* **C)** CREATE TABLE notas_aluno (aluno_ID NUMBER(12), media_notas NUMBER(4,3), aluno_ID_fk FOREIGN KEY (aluno_ID) REFERENCES aluno(aluno_ID));
* **D)** CREATE TABLE notas_aluno (aluno_ID NUMBER(12), media_notas NUMBER(4,3), CONSTRAINT aluno_ID_fk FOREIGN KEY (aluno_ID) REFERENCES aluno(aluno_ID));
* **E)** CREATE TABLE notas_aluno (aluno_ID NUMBER(12), media_notas NUMBER(4,3), CONSTRAINT aluno_ID_fk REFERENCES (aluno_ID) FOREIGN KEY aluno(aluno_ID));

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "CREATE TABLE notas_aluno (aluno_ID NUMBER(12), media_notas NUMBER(4,3), CONSTRAINT aluno_ID_fk REFERENCES...". De acordo com a teoria estudada em *2.1 Bancos Orientados a Documentos (MongoDB)*, *Sharding:* Distribuição horizontal física dos documentos entre múltiplos servidores (*shards*) guiada por uma Chave de Partição (*Shard Key*).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "CREATE TABLE notas_aluno (aluno_ID NUMBER(12), media_notas NUMBER(4,3), CONSTRAINT FOREIGN KEY (aluno_ID)...". De acordo com a teoria estudada em *2.4 Bancos Orientados a Grafos (Neo4j e Cypher)*, é o diferencial técnico mais cobrado em concursos. Em bancos relacionais, para relacionar tabelas, o motor precisa realizar operações de `JOIN` via índices secundários ou varreduras com custo que escala de acordo com o tamanho total da tabela.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "CREATE TABLE notas_aluno (aluno_ID NUMBER(12), media_notas NUMBER(4,3), aluno_ID_fk FOREIGN KEY (aluno_ID)...". De acordo com a teoria estudada em *2.1 Bancos Orientados a Documentos (MongoDB)*, coleções e Documentos: Os dados são agrupados em Coleções (*Collections*), que equivalem conceitualmente às tabelas relacionais.
> - **D)** **Correta.** Conforme fundamentado na seção *2.3 Bancos de Famílias de Colunas (Wide-Column / Cassandra / HBase)* deste guia, modelo de Dados Bidimensional Esparso: Os dados são organizados em linhas, onde cada linha possui uma chave de linha (*Row Key* ou *Partition Key*). Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/AP/2023) ao estabelecer que "CREATE TABLE notas_aluno (aluno_ID NUMBER(12), media_notas NUMBER(4,3), CONSTRAINT aluno_ID_fk FOREIGN KEY...".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "CREATE TABLE notas_aluno (aluno_ID NUMBER(12), media_notas NUMBER(4,3), CONSTRAINT aluno_ID_fk REFERENCES...". De acordo com a teoria estudada em *2.2 Bancos Chave-Valor (Redis)*, o modelo mais simples, minimalista e veloz. Armazena pares formados por uma chave única (string) mapeada para um valor (escalar primitivo, objeto binário ou estrutura complexa).
>
> **Gabarito: D**

---

### Teste 285
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Ciência de Dados)**
Sobre banco de dado NoSQL orientado a grafos, avalie se as afirmativas a seguir são falsas (F) ou verdadeiras (V). I. Se compararmos com um banco de dados relacional, os nós de um grafo correspondem às colunas de uma tabela. II. As operações de junção nesse tipo de banco são frequentemente mais eficientes do que em bancos de dados relacionais, pois utilizam chaves estrangeiras para realizar o relacionamento entre os nós. III. Diferentemente dos outros tipos de banco de dados NoSQL, bancos orientados a grafos não são próprios para se trabalhar com um grande volume de dados. As afirmativas são, respectivamente,

* **A)** V – F – F.
* **B)** F – V – F.
* **C)** F – F – V.
* **D)** V – F – V.
* **E)** F – F – F.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "V – F – F". De acordo com a teoria estudada em *2.4 Bancos Orientados a Grafos (Neo4j e Cypher)*, o tempo de execução da consulta depende exclusivamente do subgrafo visitado na vizinhança, e não do volume global de bilhões de registros armazenados no banco.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "F – V – F". De acordo com a teoria estudada em *2.1 Bancos Orientados a Documentos (MongoDB)*, bSON (Binary JSON): Extensão binária do JSON que viabiliza tipos primitivos adicionais não suportados pelo JSON textual puro, como tipos `Date` nativos, inteiros de 64 bits (`long`), decimais de alta precisão e dados binários brutos, otimizando a velocidade de parseamento e travessia.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "F – F – V". De acordo com a teoria estudada em *1. Teorema CAP, Teorema PACELC e o Modelo BASE*, o movimento NoSQL (*Not Only SQL*) surgiu para contornar as restrições físicas de escalabilidade vertical de bancos relacionais monolíticos em cenários de processamento massivo de dados (*Big Data*), viabilizando esquemas dinâmicos (*schemaless*) e particionamento horizontal maciço (*sharding*).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "V – F – V". De acordo com a teoria estudada em *2.1 Bancos Orientados a Documentos (MongoDB)*, coleções e Documentos: Os dados são agrupados em Coleções (*Collections*), que equivalem conceitualmente às tabelas relacionais.
> - **E)** **Correta.** Conforme fundamentado na seção *2.4 Bancos Orientados a Grafos (Neo4j e Cypher)* deste guia, é o diferencial técnico mais cobrado em concursos. Em bancos relacionais, para relacionar tabelas, o motor precisa realizar operações de `JOIN` via índices secundários ou varreduras com custo que escala de acordo com o tamanho total da tabela. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "F – F – F".
>
> **Gabarito: E**

---

## 3. Bancos de Dados Vetoriais e Inteligência Artificial

A revolução dos Modelos de Linguagem Grande (*Large Language Models - LLMs*) baseados na arquitetura *Transformer* impulsionou a necessidade de gerenciar, armazenar e consultar representações semânticas densas em alta dimensionalidade.

### 3.1 Embeddings: Do Texto Não-Estruturado ao Espaço Vetorial

Um **embedding** é a conversão algorítmica de um dado arbitrário não estruturado (documentos jurídicos, relatórios fiscais, imagens de obras públicas ou fragmentos de código) em um **vetor numérico denso contínuo** em um espaço multidimensional (tipicamente com 768, 1.536 ou 3.072 dimensões de números de ponto flutuante `float32`).

- **Propriedade Semântica Fundamental:** Redes neurais de embedding posicionam conceitos correlacionados em regiões geometricamente vizinhas no hiperespaço contínuo.
- Duas sentenças que expressem a mesma ideia semântica, ainda que com vocabulário formal e palavras inteiramente distintas (ex.: *"sobrepreço em pavimentação asfáltica"* e *"desvio orçamentário na compra de asfalto municipal"*), geram vetores densos com altíssima proximidade geométrica e angular.

```
Texto Bruto: "Edital com sobrepreço" ──► [Modelo Transformer] ──► Vetor: [0.15, -0.42, 0.88, .., 0.05]
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
       1 - (vetor_embedding <=> '[0.012, -0.045, ..]'::vector) AS similaridade
FROM acordaos_tce
ORDER BY vetor_embedding <=> '[0.012, -0.045, ..]'::vector
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

### Teste 286
**(FGV – TRT/DA – 2025 – Analista Judiciario Area Apoio Especializado Tecnologia Da Informacao)**
O banco de dados H2 é uma ferramenta muito útil para desenvolvedores Java. Ele foi projetado para ser leve e pode ser incorporado diretamente em aplicativos Java. Com relação aos modos de conexão do H2, analise as afirmativas a seguir. I. No modo incorporado (embedded), um aplicativo abre um banco de dados dentro da mesma máquina virtual Java (JVM) usando JDBC. Este é o modo de conexão mais rápido e fácil. A desvantagem é que um banco de dados só pode ser aberto em uma máquina virtual por vez. Não há limite para o número de bancos de dados abertos simultaneamente ou para o número de conexões abertas. II. O modo misto (mixed) é uma combinação dos modos incorporado e servidor. O primeiro aplicativo que se conecta ao banco usando o modo incorporado, mas também inicia um servidor para que outros aplicativos (executados em diferentes processos ou JVM) possam acessar simultaneamente os mesmos dados. As conexões locais são tão rápidas quanto se o banco fosse usado apenas no modo incorporado, mas as conexões remotas são um pouco mais lentas. III. O modo em memória (in memory) é uma especialização do modo incorporado exclusivo para aplicações que usam o H2 em exclusivamente em memória. Todos os clientes que desejam se conectar (não importa se é uma conexão local ou remota) utilizam a mesmo URL do banco de dados. Além do desempenho a vantagem é o mecanismo de persistência de dados baseada em logs de transações. Está correto o que se afirma em

* **A)** I, apenas.
* **B)** I e II, apenas
* **C)** II e III, apenas
* **D)** I e III, apenas
* **E)** I, II e III.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I, apenas". De acordo com a teoria estudada em *3.3 Algoritmos de Busca Aproximada por Vizinhos Mais Próximos (ANN)*, constrói uma estrutura em grafo multicamadas onde a camada superior possui arestas longas (permitindo saltos gigantescos pelo hiperespaço para localização aproximada da região), enquanto as camadas inferiores possuem conexões locais cada vez mais densas para refinamento fino da busca.
> - **B)** **Correta.** Conforme fundamentado na seção *3.4 Ecossistema Tecnológico: Extensão pgvector e Bancos Nativos* deste guia, softwares projetados exclusivamente para o ciclo de vida vetorial distribuído: Pinecone (SaaS nativo de nuvem), Milvus (banco distribuído de alta escala em Go/C++), Qdrant (motor em Rust de altíssima eficiência de memória) e Chroma (banco leve voltado ao ecossistema Python). Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT/DA/2025) ao estabelecer que "I e II, apenas".
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II e III, apenas". De acordo com a teoria estudada em *2.3 Bancos de Famílias de Colunas (Wide-Column / Cassandra / HBase)*, a persistência no disco utiliza estruturas de LSM-Tree (*Log-Structured Merge-Tree*): as escritas vão primeiro para a memória RAM (*MemTable*) e para um log sequencial (*CommitLog*); quando a MemTable enche, é descarregada no disco em arquivos imutáveis chamados SSTables (*Sorted String Tables*), periodicamente unificados por compactação.
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e III, apenas". De acordo com a teoria estudada em *2.1 Bancos Orientados a Documentos (MongoDB)*, no entanto, cada Documento (*Document*) individual dentro de uma mesma coleção pode possuir campos, tipos e estruturas inteiramente distintas (esquema dinâmico / *schema-flexible*).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I, II e III". De acordo com a teoria estudada em *1.1 Teorema CAP (Eric Brewer / Gilbert & Lynch)*, o Teorema CAP afirma que em qualquer sistema distribuído de armazenamento de dados sujeito a comunicação em rede, é matematicamente impossível fornecer simultaneamente as três garantias abaixo.
>
> **Gabarito: B**

---

### Teste 287
**(FCC – TRT 4ª – 2015 – Analista Judiciário - Tecnologia Da Informação)**
A plataforma Java EE define um padrão de arquitetura de três camadas para o desenvolvimento de aplicações web: Camada de Apresentação (Web Tier), Camada de Negócio (Business Tier) e Camada de Integração (EIS Tier). Na camada de Negócio são representados

* **A)** todos os componentes JSF (Java Server Faces).
* **B)** componentes de persistência de objetos utilizando Hibernate e JPA (Java Persistence API).
* **C)** os componentes EJB (Enterprise JavaBeans).
* **D)** todos os componentes JSP.
* **E)** os bancos de dados.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "todos os componentes JSF (Java Server Faces)". De acordo com a teoria estudada em *2.2 Bancos Chave-Valor (Redis)*, arquitetura em Memória RAM: O Redis (*Remote Dictionary Server*) opera primariamente na memória principal do servidor, propiciando tempos de resposta na escala de dezenas de microssegundos.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "componentes de persistência de objetos utilizando Hibernate e JPA (Java Persistence API)". De acordo com a teoria estudada em *1.3 Modelo BASE vs. Propriedades ACID*, d - Durabilidade: Os dados comitados persistem permanentemente em disco, resistindo a falhas elétricas.: Propagação de Réplicas: Replicação assíncrona tolerante a latência, utilizando protocolos como *Gossip Protocol* e algoritmos de quórum configuráveis ($R + W > N$).
> - **C)** **Correta.** Conforme fundamentado na seção *3.2 Métricas Matemáticas de Distância e Similaridade* deste guia, soma ponderada dos produtos dos componentes. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 4ª/2015) ao estabelecer que "os componentes EJB (Enterprise JavaBeans)".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "todos os componentes JSP". De acordo com a teoria estudada em *3.3 Algoritmos de Busca Aproximada por Vizinhos Mais Próximos (ANN)*, constrói uma estrutura em grafo multicamadas onde a camada superior possui arestas longas (permitindo saltos gigantescos pelo hiperespaço para localização aproximada da região), enquanto as camadas inferiores possuem conexões locais cada vez mais densas para refinamento fino da busca.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "os bancos de dados". De acordo com a teoria estudada em *3. Bancos de Dados Vetoriais e Inteligência Artificial*, a revolução dos Modelos de Linguagem Grande (*Large Language Models - LLMs*) baseados na arquitetura *Transformer* impulsionou a necessidade de gerenciar, armazenar e consultar representações semânticas densas em alta dimensionalidade.
>
> **Gabarito: C**

---

### Teste 288
**(CEBRASPE – STJ – 2024 – Analista Judiciário - Apoio Especializado - Suporte em Tecnologia da Informação)**
Os bancos de dados dimensionais que atendem ao data warehouse nas fontes transacionais, sem que haja acréscimo de informações devem ser implementados de forma normalizada. transcreva o texto para a FOLHA DE TEXTO DEFINITIVO DA PROVA DISCURSIVA, no local apropriado, pois não será avaliado fragmento de texto escrito em local indevido. • Qualquer fragmento de texto além da extensão máxima de linhas disponibilizadas será desconsiderado. • Na Folha de Texto Definitivo, a presença de qualquer marca identificadora no espaço destinado à transcrição do texto definitivo acarretará a anulação da sua prova discursiva. • Ao domínio do conteúdo serão atribuídos até 40,00 pontos, dos quais até 2,00 pontos serão atribuídos ao quesito apresentação (legibilidade, respeito às margens e indicação de parágrafos) e estrutura textual (organização das ideias em texto estruturado). -- PROVA DISCURSIVA -- A criptografia é um método de segurança que usa algoritmos para proteger informações, transformando-as em um código secreto que só pode ser desbloqueado com uma chave digital. A respeito da criptografia no âmbito da segurança da informação, redija um texto dissertativo atendendo ao que se pede a seguir.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Incorreta.** A marcação como **Certo** não procede, pois o enunciado promove generalização excessiva que desconsidera as condições técnicas e normativas ao afirmar que "Os bancos de dados dimensionais que atendem ao data warehouse nas fontes transacionais, sem que haja...". De acordo com a teoria estudada em *3.4 Ecossistema Tecnológico: Extensão pgvector e Bancos Nativos*, a indexação e recuperação de embeddings pode ser implementada por duas abordagens arquiteturais.
> - **E)** **Correta.** O item está **Errado** (gabarito oficial: **E**). Conforme fundamentado na seção *3.1 Embeddings: Do Texto Não-Estruturado ao Espaço Vetorial* deste guia, um embedding é a conversão algorítmica de um dado arbitrário não estruturado (documentos jurídicos, relatórios fiscais, imagens de obras públicas ou fragmentos de código) em um vetor numérico denso contínuo em um espaço multidimensional (tipicamente com 768, 1.536 ou 3.072 dimensões de números de ponto flutuante `float32`). Portanto, a assertiva examinada pela banca (CEBRASPE – STJ/2024) viola os preceitos técnicos do tópico.
>
> **Gabarito: E**

---

## 🌐 Fontes Oficiais e Referências Bibliográficas

* [MongoDB Official Documentation - Document Model and Aggregation](https://www.mongodb.com/docs/manual/core/data-modeling-introduction/) - Bancos orientados a documentos, BSON, pipeline de agregação e consistência distribuída.
* [Redis Official Documentation - Data Types and In-Memory Storage](https://redis.io/docs/latest/develop/data-types/) - Estrutura chave-valor em memória, strings, hashes, lists, sets, sorted sets e pub/sub.
* [PostgreSQL 17 Official Documentation - JSON Types and Functions](https://www.postgresql.org/docs/current/datatype-json.html) - Armazenamento de dados não estruturados com JSONB e indexação GIN no PostgreSQL.
* [ArXiv - Vector Search and Nearest Neighbor in Databases](https://arxiv.org/abs/2005.11401) - Indexação vetorial de embeddings (HNSW e IVFFlat) para busca semântica em bancos modernos.
* SADALAGE, Pramod J.; FOWLER, Martin. **NoSQL Essencial: Um Guia Conciso para o Mundo Emergente da Persistência Poliglota**. São Paulo: Novatec, 2013. (Cap. 2 a 5 - Modelos de Dados NoSQL e Teorema CAP).
* KLEPPMANN, Martin. **Projetando Aplicações Intensivas em Dados**. São Paulo: Novatec, 2018. (Cap. 3 - Mecanismos de Armazenamento e Recuperação; Cap. 5 - Replicação NoSQL).
* TANIAR, David et al. **Distributed Database Systems**. Nova York: Wiley-IEEE Press, 2008. (Cap. 4 - Fragmentação e Consistência Eventual).
