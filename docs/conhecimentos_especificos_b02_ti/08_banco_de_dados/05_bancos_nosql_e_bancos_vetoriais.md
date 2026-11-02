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

### Teste 001
**(FGV – TCE/GO – 2024 – Analista de Controle Externo - Tecnologia da Informação)**
Dados abertos são informações digitais disponibilizadas ao público sem restrições de uso, geralmente sob formatos acessíveis e licenças que permitem sua livre utilização, redistribuição e modificação. O chamado Sistema de 5 Estrelas classifica por meio de estrelas o grau de abertura dos dados. O nível três estrelas é caracterizado por sua disponibilidade na internet

* **A)** em qualquer formato.
* **B)** em formato RDF.
* **C)** de maneira estruturada e formato não proprietário.
* **D)** em formato SPARQL.
* **E)** em formato RDF Conectado.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção promove generalização excessiva que desconsidera as condições técnicas e normativas ao afirmar que "em qualquer formato". De acordo com a teoria estudada em *1.1 Teorema CAP (Eric Brewer / Gilbert & Lynch)*, o Teorema CAP afirma que em qualquer sistema distribuído de armazenamento de dados sujeito a comunicação em rede, é matematicamente impossível fornecer simultaneamente as três garantias abaixo.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "em formato RDF". De acordo com a teoria estudada em *2.1 Bancos Orientados a Documentos (MongoDB)*, armazenam dados na forma de documentos semiestruturados, geralmente serializados em formatos como JSON, BSON ( Binary JSON ) ou XML.
> - **C)** **Correta.** Conforme fundamentado na seção *2.4 Bancos Orientados a Grafos (Neo4j e Cypher)* deste guia, propriedades (Properties): Atributos em formato chave valor atribuídos tanto aos nós quanto aos relacionamentos (ex.: percentual societario: 49.5 , data inicio: '2025 01 10' ). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/GO/2024) ao estabelecer que "de maneira estruturada e formato não proprietário".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "em formato SPARQL". De acordo com a teoria estudada em *2.3 Bancos de Famílias de Colunas (Wide-Column / Cassandra / HBase)*, a comunicação interna entre nós do cluster opera por meio do Gossip Protocol para monitoramento contínuo do estado e saúde do sistema.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "em formato RDF Conectado". De acordo com a teoria estudada em *2.5 Matriz Comparativa e Casos de Uso no Controle Externo*, documentos: MongoDB — $\mathcal{O}(1)$ / $\mathcal{O}(\log N)$ — CP (geralmente) — Gestão de peças processuais digitalizadas, acórdãos e formulários dinâmicos de prestação de contas dos jurisdicionados.
>
> **Gabarito: C**

---


### Teste 002
**(CEBRASPE – STJ – 2024 – Analista Judiciário - Apoio Especializado - Suporte em Tecnologia da Informação)**
O banco de dados H2 é uma solução de persistência de dados NoSQL do tipo chave-valor.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Incorreta.** A proposição apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O banco de dados H2 é uma solução de persistência de dados NoSQL do tipo chave valor". De acordo com a teoria em *2.3 Bancos de Famílias de Colunas (Wide-Column / Cassandra / HBase)*, consultas e Casos de Uso: O Cassandra adota a linguagem CQL ( Cassandra Query Language ), que lembra a sintaxe do SQL, mas restringe severamente consultas que não utilizem a chave de partição (não há suporte para JOIN relacional arbitrário). É a solução perfeita para dados de séries temporais, registros massivos de telemetria IoT, histórico contábil imutável e logs de auditoria contínua.
> - **E)** **Correta.** O item está **Errado** (gabarito oficial: **E**), pois contraria a disciplina teórica aplicável.
>
> **Gabarito: E**

---


### Teste 003
**(CEBRASPE – STJ – 2024 – Analista Judiciário - Apoio Especializado - Suporte em Tecnologia da Informação)**
Os sistemas de bancos de dados NoSQL baseados em documentos armazenam os dados por meio de esquemas do tipo XML.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Incorreta.** A proposição apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Os sistemas de bancos de dados NoSQL baseados em documentos armazenam os dados por meio de esquemas do tipo...". De acordo com a teoria em *2.1 Bancos Orientados a Documentos (MongoDB)*, armazenam dados na forma de documentos semiestruturados, geralmente serializados em formatos como JSON, BSON ( Binary JSON ) ou XML.
> - **E)** **Correta.** O item está **Errado** (gabarito oficial: **E**), pois contraria a disciplina teórica aplicável.
>
> **Gabarito: E**

---


### Teste 004
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
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "são exclusivas para bancos de dados NoSQL, utilizando bibliotecas como HBase e Cassandra". De acordo com a teoria estudada em *2. As Quatro Famílias de Bancos de Dados NoSQL*, mongoDB, CouchDB Redis, DynamoDB Cassandra, HBase Neo4j, Neptune.
> - **B)** **Correta.** Conforme fundamentado na seção *1.2 O Teorema PACELC* deste guia, ou seja, para entregar dados estritamente consistentes mesmo em tempos normais, os nós do cluster precisam trocar mensagens de confirmação síncronas entre si, o que eleva a latência percebida pelos clientes. Se o objetivo for latência ultrabaixa, o sistema deve relaxar a consistência imediata de leitura. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/AP/2023) ao estabelecer que "proporcionam interfaces que permitem a leitura, gravação e manipulação dos dados armazenados, como JDBC e ADO.NET".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "são responsáveis pela interface gráfica dos sistemas de bancos de dados, usando bibliotecas como Hibernate e...". De acordo com a teoria estudada em *2.1 Bancos Orientados a Documentos (MongoDB)*, aggregation Pipeline: Framework de análise de dados no MongoDB estruturado em etapas sequenciais compostas por operadores.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "gerenciam a persistência de dados no armazenamento e as bibliotecas SQLite e MongoDB são exemplos dessa abordagem". De acordo com a teoria estudada em *1.1 Teorema CAP (Eric Brewer / Gilbert & Lynch)*, sistemas CP: Priorizam Consistência. Em caso de quebra de partição, os nós isolados rejeitam requisições para evitar leituras defasadas ou escritas conflitantes (sacrificam a Disponibilidade). Exemplos: MongoDB, Redis Cluster, HBase, CockroachDB.
> - **E)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "focam exclusivamente a otimização de consultas SQL, e bibliotecas como LINQ e Django ORM são amplamente utilizadas...". De acordo com a teoria estudada em *2.3 Bancos de Famílias de Colunas (Wide-Column / Cassandra / HBase)*, consultas e Casos de Uso: O Cassandra adota a linguagem CQL ( Cassandra Query Language ), que lembra a sintaxe do SQL, mas restringe severamente consultas que não utilizem a chave de partição (não há suporte para JOIN relacional arbitrário). É a solução perfeita para dados de séries temporais, registros massivos de telemetria IoT, histórico contábil imutável e logs de auditoria contínua.
>
> **Gabarito: B**

---


### Teste 005
**(FCC – TRT 6ª – 2012 – Analista Judiciário - Apoio Especializado/Tecnologia da Informação)**
O estilo tradicional de direção (Teoria X) está apoiado numa concepção da natureza humana que enfatiza

* **A)** o caráter egocêntrico dos homens e a oposição entre os objetivos pessoais e os objetivos da organização.
* **B)** o caráter naturalmente empreendedor e ativo dos homens quando motivados por objetivos organizacionais ambiciosos.
* **C)** a natureza independente, a predisposição ao autocontrole e facilidade ao comportamento disciplinado.
* **D)** a capacidade de imaginação e de criatividade na solução de problemas como atributo comum à maioria dos homens.
* **E)** a responsabilidade da administração em proporcionar condições para que as pessoas reconheçam e desenvolvam suas potencialidades.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *2.1 Bancos Orientados a Documentos (MongoDB)* deste guia, replica Sets: Conjuntos de nós configurados para replicação automática com eleição de um nó Primário ( Primary , que processa todas as escritas) e múltiplos nós Secundários ( Secondary , que replicam os logs de operação oplog de forma assíncrona). Se o nó Primário cair, os Secundários realizam uma eleição baseada no algoritmo Raft/Paxos para eleger um novo líder sem intervenção humana. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 6ª/2012) ao estabelecer que "o caráter egocêntrico dos homens e a oposição entre os objetivos pessoais e os objetivos da organização".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "o caráter naturalmente empreendedor e ativo dos homens quando motivados por objetivos organizacionais ambiciosos". De acordo com a teoria estudada em *2.4 Bancos Orientados a Grafos (Neo4j e Cypher)*, modelam os dados utilizando os conceitos formais da teoria dos grafos: Vértices (Nós), Arestas (Relacionamentos) e Propriedades.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "a natureza independente, a predisposição ao autocontrole e facilidade ao comportamento disciplinado". De acordo com a teoria estudada em *1.2 O Teorema PACELC*, formulado pelo professor Daniel Abadi, o Teorema PACELC expande o Teorema CAP para descrever o comportamento do sistema não apenas durante desastres de rede, mas também em condições de operação normal.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "a capacidade de imaginação e de criatividade na solução de problemas como atributo comum à maioria dos homens". De acordo com a teoria estudada em *2.3 Bancos de Famílias de Colunas (Wide-Column / Cassandra / HBase)*, consultas e Casos de Uso: O Cassandra adota a linguagem CQL ( Cassandra Query Language ), que lembra a sintaxe do SQL, mas restringe severamente consultas que não utilizem a chave de partição (não há suporte para JOIN relacional arbitrário). É a solução perfeita para dados de séries temporais, registros massivos de telemetria IoT, histórico contábil imutável e logs de auditoria contínua.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "a responsabilidade da administração em proporcionar condições para que as pessoas reconheçam e desenvolvam suas...". De acordo com a teoria estudada em *3.2 Métricas Matemáticas de Distância e Similaridade*, $+1$: Vetores apontam para a exata mesma direção (máxima similaridade semântica).
>
> **Gabarito: A**

---


### Teste 006
**(FGV – TRF/1 – 2024 – Analista Judiciario Area Apoio Especializado Especialidade Suporte Em Tecnologia Da Informacao)**
Os sistemas de informação que automatizam os processos de negócio de uma organização requerem bancos de dados transacionais para realizar uma operação. Com o crescimento das fontes de dados, os bancos de dados evoluíram para permitir a ingestão de grandes volumes de dados gerados a cada instante. Com isso, uma das propriedades de transações que precisa estar presente em bancos de dados NoSQL é:

* **A)** durabilidade;
* **B)** atomicidade;
* **C)** estado inflexível;
* **D)** isolamento seletivo;
* **E)** eventualmente consistente.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "durabilidade". De acordo com a teoria estudada em *1.3 Modelo BASE vs. Propriedades ACID*, d Durabilidade: Os dados comitados persistem permanentemente em disco, resistindo a falhas elétricas.: Propagação de Réplicas: Replicação assíncrona tolerante a latência, utilizando protocolos como Gossip Protocol e algoritmos de quórum configuráveis ($R + W N$).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "atomicidade". De acordo com a teoria estudada em *1.3 Modelo BASE vs. Propriedades ACID*, a Atomicidade: A transação é indivisível (tudo ou nada).: BA Basically Available (Disponibilidade Básica): O sistema garante disponibilidade contínua dos serviços essenciais, tolerando falhas parciais ou degradação seletiva de recursos secundários.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "estado inflexível". De acordo com a teoria estudada em *2.4 Bancos Orientados a Grafos (Neo4j e Cypher)*, é o diferencial técnico mais cobrado em concursos. Em bancos relacionais, para relacionar tabelas, o motor precisa realizar operações de JOIN via índices secundários ou varreduras com custo que escala de acordo com o tamanho total da tabela.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "isolamento seletivo". De acordo com a teoria estudada em *1.3 Modelo BASE vs. Propriedades ACID*, i Isolamento: Transações simultâneas não interferem entre si, produzindo resultado idêntico a uma execução serial.: E Eventual Consistency (Consistência Eventual): Se nenhuma nova atualização for submetida ao sistema, após decorrido um intervalo de tempo razoável todas as réplicas convergentes propagarão suas atualizações e alcançarão o mesmo estado consolidado.
> - **E)** **Correta.** Conforme fundamentado na seção *1.3 Modelo BASE vs. Propriedades ACID* deste guia, enquanto os bancos relacionais transacionais regem se pelo rigor determinístico do modelo ACID, os sistemas NoSQL distribuídos apoiam se no paradigma flexível do modelo BASE. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRF/1/2024) ao estabelecer que "eventualmente consistente".
>
> **Gabarito: E**

---


### Teste 007
**(FGV – TJ/RR – 2024 – Analista Judiciario Gestao E Governanca De Tecnologia Da Informacao)**
Dados são importantes elementos de apoio à tomada de decisão, sendo que algumas aplicações geram quantidade massiva e heterogênea de dados, com alta velocidade. Para lidar com esse cenário, foi desenvolvido o seguinte modelo de programação que consiste em dividir, processar e combinar os dados em paralelo, de forma a acelerar o processamento e garantir a confiabilidade dos resultados:

* **A)** Data Warehousing.
* **B)** Elastic Search.
* **C)** Hadoop.
* **D)** MapReduce.
* **E)** NoSQL.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Data Warehousing". De acordo com a teoria estudada em *1. Teorema CAP, Teorema PACELC e o Modelo BASE*, o movimento NoSQL ( Not Only SQL ) surgiu para contornar as restrições físicas de escalabilidade vertical de bancos relacionais monolíticos em cenários de processamento massivo de dados ( Big Data ), viabilizando esquemas dinâmicos ( schemaless ) e particionamento horizontal maciço ( sharding ).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Elastic Search". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, arXiv Vector Search and Nearest Neighbor in Databases Indexação vetorial de embeddings (HNSW e IVFFlat) para busca semântica em bancos modernos.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Hadoop". De acordo com a teoria estudada em *2.3 Bancos de Famílias de Colunas (Wide-Column / Cassandra / HBase)*, modelo de Dados Bidimensional Esparso: Os dados são organizados em linhas, onde cada linha possui uma chave de linha ( Row Key ou Partition Key ). Cada linha pode conter uma quantidade variável de colunas associadas a uma Família de Colunas ( Column Family ), e cada coluna contém um nome, um valor e um carimbo de tempo ( Timestamp ). Linhas diferentes na mesma tabela não precisam ter as mesmas colunas (espaço não alocado para colunas vazias, eliminando o custo de atributos nulos).
> - **D)** **Correta.** Conforme fundamentado na seção *2.1 Bancos Orientados a Documentos (MongoDB)* deste guia, bSON (Binary JSON): Extensão binária do JSON que viabiliza tipos primitivos adicionais não suportados pelo JSON textual puro, como tipos Date nativos, inteiros de 64 bits ( long ), decimais de alta precisão e dados binários brutos, otimizando a velocidade de parseamento e travessia. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/RR/2024) ao estabelecer que "MapReduce".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "NoSQL". De acordo com a teoria estudada em *2. As Quatro Famílias de Bancos de Dados NoSQL*, pipeline agreg. RAM ultra rápida Escala massiva propriedades.
>
> **Gabarito: D**

---


### Teste 008
**(CEBRASPE – TJ/DFT – 2015 – Analista Judiciario Suporte Em Tecnologia Da Informacao)**
Sistemas de bancos de dados classificados como NoSQL permitem a inserção de dados sem que haja um esquema predefinido.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Correta.** O item está **Certo**. Conforme fundamentado na seção *2. As Quatro Famílias de Bancos de Dados NoSQL*, esquema dinâmico TTL e persistência Masterless P2P Index free adj. Dessa forma, está plenamente correta a assertiva da banca (CEBRASPE – TJ/DFT/2015) ao afirmar que "Sistemas de bancos de dados classificados como NoSQL permitem a inserção de dados sem que haja um esquema...".
> - **E)** **Incorreta.** A assertiva não incorre em erro conceitual, guardando conformidade com a teoria estudada.
>
> **Gabarito: C**

---


### Teste 009
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
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "armazenam dados em tabelas estruturadas, com linhas e colunas, semelhantes aos bancos de dados relacionais". De acordo com a teoria estudada em *2.1 Bancos Orientados a Documentos (MongoDB)*, coleções e Documentos: Os dados são agrupados em Coleções ( Collections ), que equivalem conceitualmente às tabelas relacionais. No entanto, cada Documento ( Document ) individual dentro de uma mesma coleção pode possuir campos, tipos e estruturas inteiramente distintas (esquema dinâmico / schema flexible ).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "utilizam um modelo de grafos para representar e armazenar dados complexos, como relações entre entidades". De acordo com a teoria estudada em *2.1 Bancos Orientados a Documentos (MongoDB)*, bSON (Binary JSON): Extensão binária do JSON que viabiliza tipos primitivos adicionais não suportados pelo JSON textual puro, como tipos Date nativos, inteiros de 64 bits ( long ), decimais de alta precisão e dados binários brutos, otimizando a velocidade de parseamento e travessia.
> - **C)** **Incorreta.** A opção promove generalização excessiva que desconsidera as condições técnicas e normativas ao afirmar que "são projetados para garantir transações ACID em todos os casos, oferecendo suporte a operações complexas de...". De acordo com a teoria estudada em *2.5 Matriz Comparativa e Casos de Uso no Controle Externo*, família NoSQL: Tecnologia Típica — Complexidade de Escrita / Leitura — Modelo CAP — Aplicação Prática no Tribunal de Contas (TCE GO).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "armazenam dados em um modelo de chave valor, onde cada chave corresponde a um valor específico". De acordo com a teoria estudada em *2.3 Bancos de Famílias de Colunas (Wide-Column / Cassandra / HBase)*, modelo de Dados Bidimensional Esparso: Os dados são organizados em linhas, onde cada linha possui uma chave de linha ( Row Key ou Partition Key ). Cada linha pode conter uma quantidade variável de colunas associadas a uma Família de Colunas ( Column Family ), e cada coluna contém um nome, um valor e um carimbo de tempo ( Timestamp ). Linhas diferentes na mesma tabela não precisam ter as mesmas colunas (espaço não alocado para colunas vazias, eliminando o custo de atributos nulos).
> - **E)** **Correta.** Conforme fundamentado na seção *2.1 Bancos Orientados a Documentos (MongoDB)* deste guia, armazenam dados na forma de documentos semiestruturados, geralmente serializados em formatos como JSON, BSON ( Binary JSON ) ou XML. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/MT/2024) ao estabelecer que "armazenam dados em formato JSON, BSON ou XML, permitindo flexibilidade para armazenar diferentes tipos de...".
>
> **Gabarito: E**

---


### Teste 010
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
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "V – F – F". De acordo com a teoria estudada em *2.4 Bancos Orientados a Grafos (Neo4j e Cypher)*, vantagem de Performance: A travessia de relacionamentos possui custo computacional em tempo constante $\mathcal{O}(1)$ por aresta percorrida. O tempo de execução da consulta depende exclusivamente do subgrafo visitado na vizinhança, e não do volume global de bilhões de registros armazenados no banco.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "F – V – F". De acordo com a teoria estudada em *2.1 Bancos Orientados a Documentos (MongoDB)*, coleções e Documentos: Os dados são agrupados em Coleções ( Collections ), que equivalem conceitualmente às tabelas relacionais. No entanto, cada Documento ( Document ) individual dentro de uma mesma coleção pode possuir campos, tipos e estruturas inteiramente distintas (esquema dinâmico / schema flexible ).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "F – F – V". De acordo com a teoria estudada em *2.3 Bancos de Famílias de Colunas (Wide-Column / Cassandra / HBase)*, consultas e Casos de Uso: O Cassandra adota a linguagem CQL ( Cassandra Query Language ), que lembra a sintaxe do SQL, mas restringe severamente consultas que não utilizem a chave de partição (não há suporte para JOIN relacional arbitrário). É a solução perfeita para dados de séries temporais, registros massivos de telemetria IoT, histórico contábil imutável e logs de auditoria contínua.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "V – F – V". De acordo com a teoria estudada em *2.3 Bancos de Famílias de Colunas (Wide-Column / Cassandra / HBase)*, modelo de Dados Bidimensional Esparso: Os dados são organizados em linhas, onde cada linha possui uma chave de linha ( Row Key ou Partition Key ). Cada linha pode conter uma quantidade variável de colunas associadas a uma Família de Colunas ( Column Family ), e cada coluna contém um nome, um valor e um carimbo de tempo ( Timestamp ). Linhas diferentes na mesma tabela não precisam ter as mesmas colunas (espaço não alocado para colunas vazias, eliminando o custo de atributos nulos).
> - **E)** **Correta.** Conforme fundamentado na seção *2.4 Bancos Orientados a Grafos (Neo4j e Cypher)* deste guia, é o diferencial técnico mais cobrado em concursos. Em bancos relacionais, para relacionar tabelas, o motor precisa realizar operações de JOIN via índices secundários ou varreduras com custo que escala de acordo com o tamanho total da tabela. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "F – F – F".
>
> **Gabarito: E**

---


### Teste 011
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Ciências da Computação, Sistemas de Informação...)**
O Auditor fiscaliza a arquitetura de um novo banco de dados NoSQL distribuído para o TCE-SC. O sistema precisa garantir que, em caso de falha na rede entre dois data centers, o sistema continue aceitando gravações, mesmo que os dados fiquem temporariamente inconsistentes entre os nós. De acordo com o Teorema CAP, esse sistema prioriza as propriedades de

* **A)** e Tolerância a Partições (P).
* **B)** Consistência
* **C)** Disponibilidade
* **D)** Atomicidade e Durabilidade.
* **E)** Apenas Disponibilidade, ignorando partições.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "e Tolerância a Partições (P)". De acordo com a teoria estudada em *1.1 Teorema CAP (Eric Brewer / Gilbert & Lynch)*, a banca FCC costuma colocar como pegadinha que "um arquiteto pode escolher um sistema CA (Consistência + Disponibilidade sem Tolerância a Partições)". Lembre se: em redes de computadores físicas do mundo real, quedas de links de rede e atrasos são contingências inevitáveis; portanto, P é compulsório. A decisão prática resume se a escolher entre.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Consistência". De acordo com a teoria estudada em *1.1 Teorema CAP (Eric Brewer / Gilbert & Lynch)*, sistemas CP: Priorizam Consistência. Em caso de quebra de partição, os nós isolados rejeitam requisições para evitar leituras defasadas ou escritas conflitantes (sacrificam a Disponibilidade). Exemplos: MongoDB, Redis Cluster, HBase, CockroachDB.
> - **C)** **Correta.** Conforme fundamentado na seção *1.1 Teorema CAP (Eric Brewer / Gilbert & Lynch)* deste guia, sistemas AP: Priorizam Disponibilidade. Em caso de quebra de rede, todos os nós continuam respondendo a leituras e escritas, tolerando que réplicas fiquem temporariamente desatualizadas e sincronizem depois via Consistência Eventual (sacrificam a Consistência imediata). Exemplos: Apache Cassandra, CouchDB, DynamoDB (em configuração padrão). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "Disponibilidade".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Atomicidade e Durabilidade". De acordo com a teoria estudada em *1.3 Modelo BASE vs. Propriedades ACID*, a Atomicidade: A transação é indivisível (tudo ou nada).: BA Basically Available (Disponibilidade Básica): O sistema garante disponibilidade contínua dos serviços essenciais, tolerando falhas parciais ou degradação seletiva de recursos secundários.
> - **E)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "Apenas Disponibilidade, ignorando partições". De acordo com a teoria estudada em *1.1 Teorema CAP (Eric Brewer / Gilbert & Lynch)*, p (Partition Tolerance Tolerância a Partições de Rede): O cluster distribuído continua processando dados mesmo se ocorrerem interrupções de links de comunicação, partições físicas de rede ou atrasos arbitrários no tráfego de pacotes entre os nós.
>
> **Gabarito: C**

---


### Teste 012
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Engenharia Elétrica)**
Um sistema elétrico de potência é basicamente formado pela geração, transmissão, subtransmissão e distribuição. Sobre esses elementos, é correto afirmar que

* **A)** o sistema de transmissão de uma rede interconectada é caracterizado por operar em malhas estritamente radiais para evitar a circulação de correntes de regime transitório.
* **B)** a subtransmissão é definida exclusivamente pelo seu nível de tensão intermediário, sendo funcionalmente idêntica à transmissão de longa distância, com a única diferença de que opera em anéis fechados.
* **C)** a subtransmissão atua como uma interface de "amortecimento" e capilaridade, recebendo energia do sistema de transmissão em altas tensões e redistribuindo-a para subestações de distribuição.
* **D)** o sistema de distribuição primária diferencia-se da subtransmissão por ser o único segmento do sistema que permite a conexão de cargas industriais de grande porte.
* **E)** no segmento de geração, o uso de transformadores elevadores nas subestações associadas às usinas tem como objetivo principal o isolamento galvânico entre o gerador e a rede.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "o sistema de transmissão de uma rede interconectada é caracterizado por operar em malhas estritamente radiais para...". De acordo com a teoria estudada em *1.2 O Teorema PACELC*, senão ( Else E ): Operando em regime de normalidade sem partições ativas, o sistema precisa arbitrar entre Latência (L) e Consistência (C).
> - **B)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "a subtransmissão é definida exclusivamente pelo seu nível de tensão intermediário, sendo funcionalmente idêntica à...". De acordo com a teoria estudada em *2.3 Bancos de Famílias de Colunas (Wide-Column / Cassandra / HBase)*, a comunicação interna entre nós do cluster opera por meio do Gossip Protocol para monitoramento contínuo do estado e saúde do sistema.
> - **C)** **Correta.** Conforme fundamentado na seção *2.1 Bancos Orientados a Documentos (MongoDB)* deste guia, sharding: Distribuição horizontal física dos documentos entre múltiplos servidores ( shards ) guiada por uma Chave de Partição ( Shard Key ). O balanceamento e roteamento de requisições é transparente, intermediado por roteadores mongos e servidores de configuração ( Config Servers ). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "a subtransmissão atua como uma interface de "amortecimento" e capilaridade, recebendo energia do sistema de...".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "o sistema de distribuição primária diferencia se da subtransmissão por ser o único segmento do sistema que permite...". De acordo com a teoria estudada em *2.3 Bancos de Famílias de Colunas (Wide-Column / Cassandra / HBase)*, projetados para armazenar volumes gigantescos de dados em clusters massivos com distribuição totalmente horizontal.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "no segmento de geração, o uso de transformadores elevadores nas subestações associadas às usinas tem como objetivo...". De acordo com a teoria estudada em *1.2 O Teorema PACELC*, ou seja, para entregar dados estritamente consistentes mesmo em tempos normais, os nós do cluster precisam trocar mensagens de confirmação síncronas entre si, o que eleva a latência percebida pelos clientes. Se o objetivo for latência ultrabaixa, o sistema deve relaxar a consistência imediata de leitura.
>
> **Gabarito: C**

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

## 🌐 Fontes Oficiais e Referências Bibliográficas

* [MongoDB Official Documentation - Document Model and Aggregation](https://www.mongodb.com/docs/manual/core/data-modeling-introduction/) - Bancos orientados a documentos, BSON, pipeline de agregação e consistência distribuída.
* [Redis Official Documentation - Data Types and In-Memory Storage](https://redis.io/docs/latest/develop/data-types/) - Estrutura chave-valor em memória, strings, hashes, lists, sets, sorted sets e pub/sub.
* [PostgreSQL 17 Official Documentation - JSON Types and Functions](https://www.postgresql.org/docs/current/datatype-json.html) - Armazenamento de dados não estruturados com JSONB e indexação GIN no PostgreSQL.
* [ArXiv - Vector Search and Nearest Neighbor in Databases](https://arxiv.org/abs/2005.11401) - Indexação vetorial de embeddings (HNSW e IVFFlat) para busca semântica em bancos modernos.
* SADALAGE, Pramod J.; FOWLER, Martin. **NoSQL Essencial: Um Guia Conciso para o Mundo Emergente da Persistência Poliglota**. São Paulo: Novatec, 2013. (Cap. 2 a 5 - Modelos de Dados NoSQL e Teorema CAP).
* KLEPPMANN, Martin. **Projetando Aplicações Intensivas em Dados**. São Paulo: Novatec, 2018. (Cap. 3 - Mecanismos de Armazenamento e Recuperação; Cap. 5 - Replicação NoSQL).
* TANIAR, David et al. **Distributed Database Systems**. Nova York: Wiley-IEEE Press, 2008. (Cap. 4 - Fragmentação e Consistência Eventual).
