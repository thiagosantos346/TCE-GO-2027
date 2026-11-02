# 04 - Índices, Otimização de Consultas e Administração (PostgreSQL e Oracle)
**Última Atualização:** 2026-03-31  
**Banca Foco:** FCC (Fundação Carlos Chagas)  
**Cargo:** Auditor de Controle Externo - Tecnologia da Informação  
**Status do Mapeamento:** 100% aderente ao edital TCE-GO



---


## 📌 Ementa / Itens do Edital
1. **Estruturas de Indexação:** B-Tree, B+Tree, Hash, Bitmap, Índices Espaciais (R-Tree/GiST), GIN (Generalized Inverted Index), BRIN (Block Range Index), Índices Clusterizados vs. Não-Clusterizados, Índices Parciais e Baseados em Expressões. Trade-offs de escrita vs. leitura.
2. **Otimização de Consultas (Query Tuning):** Otimizador Baseado em Custo (CBO), Estatísticas de Catálogo e Histogramas, Planos de Execução (`EXPLAIN` e `EXPLAIN ANALYZE`).
3. **Métodos de Acesso e Operações de Junção (Joins):** Sequential Scan vs. Index Scan vs. Index Only Scan vs. Bitmap Scan; Nested Loop, Hash Join e Merge Join (critérios de escolha, memória e ordenação).
4. **Administração e Arquitetura do PostgreSQL:** Processo mestre (`postmaster`) e arquitetura multiprocesso; Parâmetros de Memória (`shared_buffers`, `work_mem`, `maintenance_work_mem`, `effective_cache_size`); MVCC e Limpeza (`VACUUM`, `VACUUM FULL`, `autovacuum`); Write-Ahead Logging (`WAL`) e Checkpoints.
5. **Administração e Arquitetura do Oracle Database:** Instância vs. Banco de Dados; Estruturas de Memória SGA (`Database Buffer Cache`, `Shared Pool`, `Redo Log Buffer`) e PGA; Processos de Background Essenciais (`DBWn`, `LGWR`, `CKPT`, `SMON`, `PMON`, `ARCn`); Estrutura Física (`Datafiles`, `Control Files`, `Redo Log Files`) e Estrutura Lógica (`Tablespaces`, Segmentos, Extensões, Blocos de Dados).

---

## 🧭 Sumário

1. [Estruturas de Indexação e Métodos de Acesso](#1-estruturas-de-indexacao-e-metodos-de-acesso)
    1. [Tipos de Índices: B+Tree, Hash, Bitmap, GIN, GiST e BRIN](#11-tipos-de-indices-btree-hash-bitmap-gin-gist-e-brin)
    2. [Índices Clusterizados vs. Não-Clusterizados, Parciais e Baseados em Expressão](#12-indices-clusterizados-vs-nao-clusterizados-parciais-e-baseados-em-expressao)
    3. [Trade-offs e Custos de Manutenção de Índices](#13-trade-offs-e-custos-de-manutencao-de-indices)
    4. [Teste 267](#Teste-267)
    5. [Teste 268](#Teste-268)
    6. [Teste 269](#Teste-269)
2. [Otimização de Consultas e Planos de Execução (Query Tuning)](#2-otimizacao-de-consultas-e-planos-de-execucao-query-tuning)
    1. [Otimizador Baseado em Custo (CBO), Estatísticas e Histogramas](#21-otimizador-baseado-em-custo-cbo-estatisticas-e-histogramas)
    2. [Análise de Planos: EXPLAIN vs. EXPLAIN ANALYZE](#22-analise-de-planos-explain-vs-explain-analyze)
    3. [Estratégias de Varredura: Seq Scan, Index Scan, Index Only Scan e Bitmap Scan](#23-estrategias-de-varredura-seq-scan-index-scan-index-only-scan-e-bitmap-scan)
    4. [Algoritmos de Junção: Nested Loop, Hash Join e Merge Join](#24-algoritmos-de-juncao-nested-loop-hash-join-e-merge-join)
    5. [Teste 270](#Teste-270)
    6. [Teste 271](#Teste-271)
    7. [Teste 272](#Teste-272)
3. [Arquitetura e Administração do PostgreSQL](#3-arquitetura-e-administracao-do-postgresql)
    1. [Modelo de Processos e Gerenciamento de Conexões](#31-modelo-de-processos-e-gerenciamento-de-conexoes)
    2. [Parâmetros Críticos de Memória](#32-parametros-criticos-de-memoria)
    3. [MVCC, Limpeza de Espaço e o Mecanismo VACUUM](#33-mvcc-limpeza-de-espaco-e-o-mecanismo-vacuum)
    4. [Write-Ahead Logging (WAL) e Checkpoints](#34-write-ahead-logging-wal-e-checkpoints)
    5. [Teste 273](#Teste-273)
    6. [Teste 274](#Teste-274)
4. [Arquitetura e Administração do Oracle Database](#4-arquitetura-e-administracao-do-oracle-database)
    1. [Instância vs. Banco de Dados e Estruturas de Memória (SGA e PGA)](#41-instancia-vs-banco-de-dados-e-estruturas-de-memoria-sga-e-pga)
    2. [Processos de Background Mandatórios (DBWn, LGWR, CKPT, SMON, PMON)](#42-processos-de-background-mandatorios-dbwn-lgwr-ckpt-smon-pmon)
    3. [Estrutura Física e Lógica de Armazenamento](#43-estrutura-fisica-e-logica-de-armazenamento)
    4. [Teste 275](#Teste-275)
    5. [Teste 276](#Teste-276)
    6. [Teste 277](#Teste-277)
5. [🌐 Fontes Oficiais e Referências Bibliográficas](#fontes-oficiais-e-referencias-bibliograficas)

---

## 1. Estruturas de Indexação e Métodos de Acesso

Os índices são estruturas auxiliares de acesso criadas fisicamente para acelerar a recuperação de tuplas em tabelas sem a necessidade de varrer sequencialmente todo o arquivo de dados (*full table scan*). Contudo, cada índice introduz sobrecarga operacional no subsistema de armazenamento e processamento durante operações DML (`INSERT`, `UPDATE`, `DELETE`).

### 1.1 Tipos de Índices: B+Tree, Hash, Bitmap, GIN, GiST e BRIN

A seleção da estrutura interna do índice determina diretamente a complexidade algorítmica e a aplicabilidade a determinados operadores relacionais (`=`, `<`, `>`, `BETWEEN`, `LIKE`, `IN`, operadores geométricos e de texto pleno):

1. **B-Tree e B+Tree (Árvores Balanceadas):**
    - **B+Tree:** É a estrutura padrão (*default*) na esmagadora maioria dos SGBDs relacionais (PostgreSQL, Oracle, MySQL/InnoDB, SQL Server).
    - **Características estruturais:** Todos os nós-folha encontram-se rigorosamente na mesma profundidade (balanceamento perfeito). Ao contrário da B-Tree clássica (onde registros/ponteiros de dados podem residir em nós intermediários), a **B+Tree armazena dados ou ponteiros para as linhas (`TID`/`ROWID`) exclusivamente nos nós-folha**. Além disso, todos os nós-folha são interligados horizontalmente por ponteiros em **lista duplamente encadeada**.
    - **Complexidade:** Busca pontual, inserção e remoção em tempo logarítmico $\mathcal{O}(\log N)$.
    - **Suporte a operadores:** Excelente para igualdade (`=`), intervalos (`<`, `<=`, `>`, `>=`, `BETWEEN`) e ordenação (`ORDER BY`).

2. **Índices Hash:**
    - Baseiam-se em uma função hash determinística que mapeia uma chave de busca a um *bucket* específico.
    - **Desempenho:** Busca pontual em complexidade média $\mathcal{O}(1)$.
    - **Limitações:** **Não suportam buscas por intervalo** (`<`, `>`, `BETWEEN`), ordenação ou busca por prefixo (`LIKE 'ABC%'`). Prestam-se estritamente a comparações de igualdade estrita (`=`). No PostgreSQL, antes da versão 10, não eram registrados no WAL (hoje são seguros para *crash recovery* e replicação).

3. **Índices Bitmap:**
    - Em vez de listas de identificadores de linha (`ROWID`), o índice cria uma matriz de bits para cada valor distinto existente na coluna indexada. Para cada linha física da tabela, atribui-se um bit `1` (se a linha possui aquele valor) ou `0` (se não possui).
    - **Cenário ideal:** Colunas com **baixa cardinalidade** (poucos valores distintos em relação ao volume total de linhas, como sexo, estado civil, status de pedido, unidade federativa).
    - **Vantagens analíticas (Data Warehousing/OLAP):** Operações lógicas complexas com múltiplos filtros (`WHERE sexo = 'F' AND status = 'ATIVO' AND uf = 'GO'`) são resolvidas com operações booleanas bit a bit (*bitwise* `AND`, `OR`, `NOT`) em memória ultrarrápida antes de qualquer acesso ao disco.
    - **Desvantagem crítica em OLTP:** **Péssimo para ambientes com alta concorrência de escrita/modificação**. A alteração de uma única linha bloqueia (*lock*) todo o segmento de bitmap correspondente ao bloco de dados, inviabilizando transações concorrentes simultâneas.

4. **GIN (Generalized Inverted Index - Índice Invertido Generalizado):**
    - Estrutura especializada no PostgreSQL para dados compostos onde um único valor de coluna contém múltiplos elementos internos: arrays, documentos semiestruturados `JSONB` e vetores de busca textual (`tsvector` para *Full-Text Search*).
    - O índice armazena entradas para cada elemento/palavra individual presente nos itens, apontando para a lista de tuplas que o contêm. A leitura é muito rápida, mas a inserção/atualização exige atualização de múltiplos nós (mitigada por `fastupdate`).

5. **GiST (Generalized Search Tree) e Índices Espaciais (R-Tree):**
    - Estrutura em árvore extensível que permite implementar métodos de indexação arbitrários balanceados.
    - É amplamente utilizada para tipos geométricos e espaciais (extensões PostGIS), intervalos (`daterange`, `tsrange`) e busca por proximidade geométrica / vizinho mais próximo (*k-Nearest Neighbors - kNN*).

6. **BRIN (Block Range Index):**
    - Projetado no PostgreSQL para tabelas com dezenas de milhões de linhas dispostas de forma fisicamente ordenada no disco (ex.: séries temporais, logs por data/hora).
    - Em vez de indexar cada linha, o BRIN armazena apenas os valores **mínimo e máximo** para um conjunto fixo de páginas físicas de disco (bloco de páginas).
    - **Vantagem:** Ocupa uma fração minúscula de memória/disco (kilobytes em vez de gigabytes) com custo de manutenção ínfimo.

### 1.2 Índices Clusterizados vs. Não-Clusterizados, Parciais e Baseados em Expressão

A relação entre a ordenação lógica do índice e a ordenação física dos blocos de dados no disco define a tipologia de agrupamento:

* **Índice Clusterizado (*Clustered Index* / *Index-Organized Table - IOT*):**
    - A própria tabela física é ordenada e armazenada de acordo com a chave do índice. As folhas da B+Tree contêm os próprios dados da linha, e não apenas ponteiros.
    - Como os dados físicos só podem seguir uma única ordem sequencial no disco, **uma tabela pode ter no máximo UM índice clusterizado** (frequentemente associado à Chave Primária).
    - Vantagem: Dispensa salto secundário aos blocos de dados (*table lookup*).
    - No PostgreSQL, o comando `CLUSTER tabela USING nome_indice` reorganiza as linhas fisicamente no disco com base no índice, mas **não mantém essa ordem automaticamente** em inserções futuras (exige nova execução manual de `CLUSTER`). No Oracle, as tabelas organizadas por índice são explicitamente criadas como `CREATE TABLE .. ORGANIZATION INDEX`.

* **Índice Não-Clusterizado (*Non-Clustered / Heap Table with Secondary Index*):**
    - Os dados da tabela residem em uma estrutura de *Heap* (pilha de blocos não ordenada). O índice secundário é uma estrutura separada cujos nós-folha armazenam a chave indexada e um ponteiro direto (`ROWID` ou `TID`) para a tupla física na tabela heap.

* **Índices Parciais (*Filtered Indexes*):**
    - Índices construídos sobre um subconjunto de dados da tabela definido por uma cláusula `WHERE`.
    - Exemplo: `CREATE INDEX idx_pedidos_pendentes ON pedidos(data_criacao) WHERE status = 'PENDENTE';`.
    - Economiza espaço em disco e memória cache, ignorando 99% das linhas arquivadas ou concluídas.

* **Índices Baseados em Expressões ou Funções (*Function-Based Indexes*):**
    - O índice é construído sobre o resultado de uma função ou cálculo escalar, e não sobre a coluna pura.
    - Exemplo: `CREATE INDEX idx_usuarios_email_lower ON usuarios(LOWER(email));`.
    - Permite que o otimizador utilize o índice em consultas do tipo `WHERE LOWER(email) = 'usuario@tce.go.gov.br'`. Sem esse índice funcional, o uso da função na coluna impede o uso de um índice B-Tree simples sobre `email`.

> ⚠️ **Alerta de Prova (FCC):**
> A banca FCC costuma afirmar categoricamente que o uso de funções em colunas na cláusula `WHERE` (ex.: `WHERE UPPER(nome) = 'SILVA'`) inviabiliza o uso de índices comuns do tipo B-Tree, forçando um *Full Table Scan*, a menos que exista expressamente um **Índice Baseado em Função** (*Function-Based Index*). Outro ponto favorito da banca é afirmar que índices Bitmap são ideais para OLTP; lembre-se: Bitmap é excelente para **baixa cardinalidade em OLAP/DW**, mas causa *locks* severos em ambientes OLTP concorrentes.

### 1.3 Trade-offs e Custos de Manutenção de Índices

A criação excessiva ou inadequada de índices acarreta degradação do sistema:

- **Sobrecarga de Escrita:** A cada `INSERT`, `UPDATE` (que altere coluna indexada) ou `DELETE`, todos os índices da tabela precisam ser sincronizados atomicamente.
- **Amplificação de I/O e Fragmentação:** Divisões de nós em árvores (*page splits*) provocam fragmentação física e lógica, exigindo manutenções periódicas (`REINDEX` no PostgreSQL ou `ALTER INDEX .. REBUILD` no Oracle).
- **Consumo de Memória de Buffer:** Índices volumosos competem com os blocos de dados por espaço na memória cache principal (`shared_buffers` no PostgreSQL / `Buffer Cache` no Oracle).

---

### Teste 267
**(FGV – TJ/AP – 2023 – Analista Judiciario Apoio Especializado Tecnologia Da Informacao Banco De Dados)**
João, administrador de Banco de Dados Oracle, deverá criar índices para melhorar o desempenho de consultas complexas sobre processos judiciais. Para isso, deverá escolher a estrutura que facilita a busca rápida de informações em operações de junção e intervalo, como: SELECT parte.nome, movimento.descricao, movimento.data FROM parte JOIN movimento ON parte.processoID = movimento.processoID WHERE parte.processoID BETWEEN 10 AND 20; Para tanto, João criou um índice específico na coluna “processoID” da tabela “movimento”: CREATE INDEX idx_movimento_processoID ON movimento(processoID); Após a execução do script apresentado, o tipo de índice criado por João é:

* **A)** bitmap;
* **B)** hashing;
* **C)** espacial;
* **D)** árvore B;
* **E)** sequencial.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "bitmap". De acordo com a teoria estudada em *1.1 Tipos de Índices: B+Tree, Hash, Bitmap, GIN, GiST e BRIN*, estrutura em árvore extensível que permite implementar métodos de indexação arbitrários balanceados.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "hashing". De acordo com a teoria estudada em *2.4 Algoritmos de Junção: Nested Loop, Hash Join e Merge Join*, consumo de Memória: Se a tabela hash exceder o espaço alocado de memória para ordenação/hashing (`work_mem` no PostgreSQL ou área de *hash* da PGA no Oracle), ocorre o *spill* para disco (armazenamento temporário em *batches*), degradando a performance.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "espacial". De acordo com a teoria estudada em *2. Otimização de Consultas e Planos de Execução (Query Tuning)*, o Query Tuning envolve a análise algorítmica e heurística empregada pelo SGBD para converter o comando declarativo SQL em uma árvore sequencial de operadores de acesso a dados de menor custo computacional.
> - **D)** **Correta.** Conforme fundamentado na seção *1.1 Tipos de Índices: B+Tree, Hash, Bitmap, GIN, GiST e BRIN* deste guia, vantagens analíticas (Data Warehousing/OLAP): Operações lógicas complexas com múltiplos filtros (`WHERE sexo = 'F' AND status = 'ATIVO' AND uf = 'GO'`) são resolvidas com operações booleanas bit a bit (*bitwise* `AND`, `OR`, `NOT`) em memória ultrarrápida antes de qualquer acesso ao disco. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/AP/2023) ao estabelecer que "árvore B".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "sequencial". De acordo com a teoria estudada em *1.2 Índices Clusterizados vs. Não-Clusterizados, Parciais e Baseados em Expressão*, como os dados físicos só podem seguir uma única ordem sequencial no disco, uma tabela pode ter no máximo UM índice clusterizado (frequentemente associado à Chave Primária).
>
> **Gabarito: D**

---

### Teste 268
**(FGV – TJ/DFT – 2022 – Analista Judiciario Suporte Em Tecnologia Da Informacao)**
No contexto do MySQL 8.x, analise as afirmativas a seguir a respeito da utilização de índices do tipo FULLTEXT . I. Índices FULLTEXT podem ser aplicados somente para tabelas InnoDB e MyISAM. II. Consultas baseadas em índices FULLTEXT devem usar a sintaxe SEARCH(col1, col2, ...) FOR(expressão [modificador]). III. O comando ALTER TABLE não pode ser utilizado para a criação de índices FULLTEXT. Está correto somente o que se afirma em:

* **A)** I;
* **B)** II;
* **C)** I e II;
* **D)** I e III;
* **E)** II e III.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *1.2 Índices Clusterizados vs. Não-Clusterizados, Parciais e Baseados em Expressão* deste guia, permite que o otimizador utilize o índice em consultas do tipo `WHERE LOWER(email) = 'usuario@tce.go.gov.br'`. Sem esse índice funcional, o uso da função na coluna impede o uso de um índice B-Tree simples sobre `email`. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/DFT/2022) ao estabelecer que "I".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "II". De acordo com a teoria estudada em *1.2 Índices Clusterizados vs. Não-Clusterizados, Parciais e Baseados em Expressão*, a banca FCC costuma afirmar categoricamente que o uso de funções em colunas na cláusula `WHERE` (ex.: `WHERE UPPER(nome) = 'SILVA'`) inviabiliza o uso de índices comuns do tipo B-Tree, forçando um *Full Table Scan*, a menos que exista expressamente um Índice Baseado em Função (*Function-Based Index*).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I e II". De acordo com a teoria estudada em *1.1 Tipos de Índices: B+Tree, Hash, Bitmap, GIN, GiST e BRIN*, b+Tree: É a estrutura padrão (*default*) na esmagadora maioria dos SGBDs relacionais (PostgreSQL, Oracle, MySQL/InnoDB, SQL Server).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I e III". De acordo com a teoria estudada em *1.2 Índices Clusterizados vs. Não-Clusterizados, Parciais e Baseados em Expressão*, como os dados físicos só podem seguir uma única ordem sequencial no disco, uma tabela pode ter no máximo UM índice clusterizado (frequentemente associado à Chave Primária).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "II e III". De acordo com a teoria estudada em *1.2 Índices Clusterizados vs. Não-Clusterizados, Parciais e Baseados em Expressão*, no Oracle, as tabelas organizadas por índice são explicitamente criadas como `CREATE TABLE .. ORGANIZATION INDEX`.
>
> **Gabarito: A**

---

### Teste 269
**(FGV – TJ/AP – 2023 – Analista Judiciario Apoio Especializado Tecnologia Da Informacao Banco De Dados)**
A tabela “Tbl_Financeiro” armazena milhares de registros de transações financeiras. Para lidar com consultas que envolvam agregações e cálculos complexos, o administrador de banco de dados poderá adotar a seguinte estratégia de otimização de consultas:

* **A)** aplicar “commits” aninhados;
* **B)** utilizar índices bitmap para colunas que envolvam dados calculados;
* **C)** reduzir a redundância dos dados aplicando técnicas de normalização;
* **D)** implementar particionamento horizontal para dividir a tabela em segmentos menores;
* **E)** armazenar previamente os resultados de consultas frequentes utilizando visões materializadas.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "aplicar “commits” aninhados". De acordo com a teoria estudada em *2. Otimização de Consultas e Planos de Execução (Query Tuning)*, o Query Tuning envolve a análise algorítmica e heurística empregada pelo SGBD para converter o comando declarativo SQL em uma árvore sequencial de operadores de acesso a dados de menor custo computacional.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "utilizar índices bitmap para colunas que envolvam dados calculados". De acordo com a teoria estudada em *2.3 Estratégias de Varredura: Seq Scan, Index Scan, Index Only Scan e Bitmap Scan*, o motor obtém a resposta sem tocar nos blocos de dados da tabela. — Consultas cujas colunas requeridas formam um índice cobridor (*covering index*). No PostgreSQL, requer consulta ao *Visibility Map* para garantir visibilidade MVCC.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "reduzir a redundância dos dados aplicando técnicas de normalização". De acordo com a teoria estudada em *3.2 Parâmetros Críticos de Memória*, define a quantidade de memória primária alocada pelo PostgreSQL para armazenar blocos de dados e índices em cache na memória compartilhada.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "implementar particionamento horizontal para dividir a tabela em segmentos menores". De acordo com a teoria estudada em *4.3 Estrutura Física e Lógica de Armazenamento*, segmento (Segment): Conjunto completo de extensões alocadas para uma estrutura de dados relacional específica. Tipos de segmentos: Segmento de Dados (Tabela), Segmento de Índice, Segmento Temporário e Segmento de Undo.
> - **E)** **Correta.** Conforme fundamentado na seção *3.2 Parâmetros Críticos de Memória* deste guia, trata-se de uma diretriz métrica informativa utilizada exclusivamente pelo planejador de consultas (CBO) para estimar a quantidade total de memória disponível para armazenar páginas em cache (somando `shared_buffers` e o cache de disco do sistema operacional). Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/AP/2023) ao estabelecer que "armazenar previamente os resultados de consultas frequentes utilizando visões materializadas".
>
> **Gabarito: E**

---

## 2. Otimização de Consultas e Planos de Execução (Query Tuning)

O Query Tuning envolve a análise algorítmica e heurística empregada pelo SGBD para converter o comando declarativo SQL em uma árvore sequencial de operadores de acesso a dados de menor custo computacional.

### 2.1 Otimizador Baseado em Custo (CBO), Estatísticas e Histogramas

Os SGBDs modernos operam com o **Cost-Based Optimizer (CBO)**, que calcula uma estimativa matemática abstrata de custo baseada no consumo previsto de I/O em disco, ciclos de CPU e memória para diversas permutações de planos de execução.

- **Estatísticas de Catálogo:** Para estimar os custos com precisão, o CBO depende de metadados atualizados coletados periodicamente pelos utilitários administrativos (`ANALYZE` no PostgreSQL ou `DBMS_STATS.GATHER_TABLE_STATS` no Oracle). As estatísticas incluem o número total de blocos da tabela, número de tuplas, largura média dos registros e número de valores distintos por coluna (*n_distinct*).
- **Histogramas:** Quando os dados de uma coluna sofrem de **distribuição assimétrica** (*data skew*), onde certos valores ocorrem com frequência desproporcional em relação a outros, o cálculo ingênuo de cardinalidade baseado na média ($1 / \text{n\_distinct}$) falha. O CBO constrói histogramas (frequência por faixas ou *Height-Balanced / Top-Frequency / Hybrid Histograms*) para estimar a seletividade real de filtros com valores literais.

### 2.2 Análise de Planos: EXPLAIN vs. EXPLAIN ANALYZE

Para inspecionar a decisão tomada pelo CBO, o desenvolvedor ou DBA utiliza ferramentas de introspecção:

* `EXPLAIN <consulta>`:
    - Gera e exibe o plano de execução teórico estimado pelo otimizador.
    - **A consulta NÃO é executada no banco de dados**. Os valores exibidos para `cost` (custo inicial e custo total de processamento), `rows` (cardinalidade estimada) e `width` (tamanho em bytes por linha) são puramente teóricos.
* `EXPLAIN ANALYZE <consulta>`:
    - **A consulta É REALMENTE EXECUTADA no motor do banco de dados**.
    - O comando exibe tanto os custos e cardinalidades estimados quanto os valores reais observados durante o processamento: tempo decorrido (*actual time* em milissegundos para a primeira e última linha), número real de linhas processadas (*actual rows*), número de loops executados e métricas de consumo de memória e I/O.
    - **Atenção:** Em comandos com efeitos colaterais (`UPDATE`, `DELETE`, `INSERT`), o `EXPLAIN ANALYZE` efetivamente altera os dados. Para evitar modificações permanentes em homologação/análise, deve ser executado dentro de uma transação com `ROLLBACK`.

```
QUERY PLAN
-------------------------------------------------------------------------------------------------------------------------
Hash Join  (cost=12.50.35.20 rows=150 width=64) (actual time=0.085.0.210 rows=145 loops=1)
  Hash Cond: (p.categoria_id = c.id)
  ->  Seq Scan on produtos p  (cost=0.00.18.00 rows=500 width=40) (actual time=0.012.0.080 rows=500 loops=1)
  ->  Hash  (cost=10.00.10.00 rows=20 width=28) (actual time=0.045.0.045 rows=20 loops=1)
        Buckets: 1024  Batches: 1  Memory Usage: 10kB
        ->  Seq Scan on categorias c  (cost=0.00.10.00 rows=20 width=28) (actual time=0.008.0.025 rows=20 loops=1)
Planning Time: 0.150 ms
Execution Time: 0.265 ms
```

### 2.3 Estratégias de Varredura: Seq Scan, Index Scan, Index Only Scan e Bitmap Scan

Ao acessar uma tabela individual, o motor pode empregar quatro métodos fundamentais:

| Método de Acesso | Mecanismo de Funcionamento | Cenário de Uso Favorável |
| :--- | :--- | :--- |
| **Sequential Scan / Full Table Scan** | Lê sequencialmente todos os blocos de dados alocados para a tabela, do primeiro ao último. | Recuperação de grande percentual das linhas (> 10-20% da tabela), tabelas minúsculas (onde carregar blocos de índice adiciona I/O desnecessário) ou filtros sem índices disponíveis. |
| **Index Scan** | Navega na B+Tree do índice até encontrar a chave desejada e, para cada nó-folha, lê o ponteiro físico (`ROWID`/`TID`) para buscar imediatamente a tupla no bloco de dados da tabela (operação de *random access* / I/O aleatório). | Filtros de alta seletividade que retornam um volume diminuto de linhas (ex.: busca por chave primária ou identificador único). |
| **Index Only Scan** | Todas as colunas requeridas na projeção (`SELECT`) e filtros (`WHERE`) já estão armazenadas nas folhas do próprio índice. O motor obtém a resposta **sem tocar nos blocos de dados da tabela**. | Consultas cujas colunas requeridas formam um índice cobridor (*covering index*). No PostgreSQL, requer consulta ao *Visibility Map* para garantir visibilidade MVCC. |
| **Bitmap Index Scan / Bitmap Heap Scan** | O índice B-Tree é varrido primeiro, montando um bitmap de endereços de blocos físicos em memória (`Bitmap Index Scan`). As páginas são ordenadas fisicamente e lidas sequencialmente no heap (`Bitmap Heap Scan`). | Consultas com seletividade moderada ou combinação de múltiplos índices com operadores `AND`/`OR`. Evita acessos aleatórios caóticos ao disco. |

### 2.4 Algoritmos de Junção: Nested Loop, Hash Join e Merge Join

A combinação de conjuntos de tuplas originários de duas tabelas (ou subconsultas) baseia-se em três estratégias centrais:

1. **Nested Loop Join:**
    - **Algoritmo:** Para cada tupla recuperada na tabela externa (*outer relation*), executa-se uma varredura (preferencialmente via índice) na tabela interna (*inner relation*).
    - **Complexidade:** Se a tabela interna for indexada, o custo é proporcional a $\mathcal{O}(N \times \log M)$, onde $N$ é o número de linhas da tabela externa e $M$ da interna.
    - **Uso ideal:** Uma tabela externa pequena combinada com uma tabela interna com índice de alta seletividade na coluna de junção.

2. **Hash Join:**
    - **Algoritmo:** O otimizador escolhe a menor das duas tabelas (relação de construção / *build phase*), lê suas tuplas e constrói uma **tabela hash em memória RAM** usando a chave de junção. Em seguida (fase de sondagem / *probe phase*), lê a tabela maior sequencialmente e busca correspondências na tabela hash.
    - **Restrições:** **Funciona exclusivamente com junções por igualdade (*equi-joins*, operador `=`)**. Não opera com desigualdades (`<`, `>`, `>=`).
    - **Consumo de Memória:** Se a tabela hash exceder o espaço alocado de memória para ordenação/hashing (`work_mem` no PostgreSQL ou área de *hash* da PGA no Oracle), ocorre o *spill* para disco (armazenamento temporário em *batches*), degradando a performance.

3. **Merge Join (ou Sort-Merge Join):**
    - **Algoritmo:** Ambas as tabelas de entrada precisam estar previamente **ordenadas** pela chave de junção. O algoritmo avança ponteiros simultaneamente pelas duas relações ordenadas, combinando tuplas equivalentes em uma única passada linear $\mathcal{O}(N + M)$.
    - **Uso ideal:** Tabelas volumosas onde os dados de ambas já vêm previamente ordenados (ex.: derivados de um índice B-Tree pré-existente) ou quando a consulta já exige ordenação explícita (`ORDER BY`) pela mesma chave de junção.

> ⚠️ **Alerta de Prova (FCC):**
> Atenção às pegadinhas clássicas da FCC sobre Joins:
>
> 1. O **Hash Join** é absolutamente inapto para processar junções baseadas em operadores de desigualdade (`t1.id < t2.id` ou `t1.valor BETWEEN t2.min AND t2.max`). O único algoritmo que lida nativamente com qualquer predicado arbitrário sem ordenação prévia é o **Nested Loop**.
> 2. No **Sort-Merge Join**, se os conjuntos não estiverem previamente ordenados, o custo preliminar de ordenação de ambas as fontes pode torná-lo inviável se comparado ao Hash Join.

---

### Teste 270
**(CEBRASPE – TJ/DFT – 2015 – Analista Judiciario Suporte Em Tecnologia Da Informacao)**
As vantagens dos arquivos hash incluem a otimização no uso do espaço físico em disco.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Incorreta.** A marcação como **Certo** não procede, pois o enunciado apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "As vantagens dos arquivos hash incluem a otimização no uso do espaço físico em disco". De acordo com a teoria estudada em *3.3 MVCC, Limpeza de Espaço e o Mecanismo VACUUM*, as tuplas antigas tornam-se tuplas mortas (*dead tuples*), consumindo espaço físico em disco (*bloat*).
> - **E)** **Correta.** O item está **Errado** (gabarito oficial: **E**). Conforme fundamentado na seção *1.1 Tipos de Índices: B+Tree, Hash, Bitmap, GIN, GiST e BRIN* deste guia, vantagens analíticas (Data Warehousing/OLAP): Operações lógicas complexas com múltiplos filtros (`WHERE sexo = 'F' AND status = 'ATIVO' AND uf = 'GO'`) são resolvidas com operações booleanas bit a bit (*bitwise* `AND`, `OR`, `NOT`) em memória ultrarrápida antes de qualquer acesso ao disco. Portanto, a assertiva examinada pela banca (CEBRASPE – TJ/DFT/2015) viola os preceitos técnicos do tópico.
>
> **Gabarito: E**

---

### Teste 271
**(FCC – TRT 13ª – 2014 – Analista Judiciário - Tecnologia da Informação)**
Um banco de dados Oracle possui uma tabela chamada processo com os seguintes campos: numero_processo number(5) sequencia_processo number(2) digito_processo number(2) ano_processo number(4) orgao_processo number(1) regiao_processo varchar2(5) vara_processo number(4) Após a tabela ter sido criada, observou-se um requisito informando que campo vara_processo deve permitir apenas valores entre 0 e 28. Para adicionar tal restrição na tabela deve-se digitar a instrução

* **A)** UPDATE TABLE processo ADD CONSTRAINT vara_processo BETWEEN 0 AND 28;
* **B)** INSERT CONSTRAINT processo ADD check_vara CHECK (vara_processo BETWEEN 0 AND 28);
* **C)** ALTER TABLE processo CONSTRAINT (vara_processo>0 AND vara_processo<28);
* **D)** ADD CONSTRAINT processo CHECK vara_processo BETWEEN 0 AND 28;
* **E)** ALTER TABLE processo ADD CONSTRAINT check_vara CHECK (vara_processo BETWEEN 0 AND 28);

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "UPDATE TABLE processo ADD CONSTRAINT vara_processo BETWEEN 0 AND 28". De acordo com a teoria estudada em *4.1 Instância vs. Banco de Dados e Estruturas de Memória (SGA e PGA)*, região de memória privada alocada exclusivamente para cada processo de servidor (*server process*).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "INSERT CONSTRAINT processo ADD check_vara CHECK (vara_processo BETWEEN 0 AND 28)". De acordo com a teoria estudada em *2.2 Análise de Planos: EXPLAIN vs. EXPLAIN ANALYZE*, atenção: Em comandos com efeitos colaterais (`UPDATE`, `DELETE`, `INSERT`), o `EXPLAIN ANALYZE` efetivamente altera os dados. Para evitar modificações permanentes em homologação/análise, deve ser executado dentro de uma transação com `ROLLBACK`.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "ALTER TABLE processo CONSTRAINT (vara_processo>0 AND vara_processo<28)". De acordo com a teoria estudada em *1.3 Trade-offs e Custos de Manutenção de Índices*, amplificação de I/O e Fragmentação: Divisões de nós em árvores (*page splits*) provocam fragmentação física e lógica, exigindo manutenções periódicas (`REINDEX` no PostgreSQL ou `ALTER INDEX .. REBUILD` no Oracle).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "ADD CONSTRAINT processo CHECK vara_processo BETWEEN 0 AND 28". De acordo com a teoria estudada em *3.1 Modelo de Processos e Gerenciamento de Conexões*, para cada nova conexão de cliente recebida, o `postmaster` invoca uma chamada de sistema `fork()` para gerar um processo de backend dedicado (*client backend process*).
> - **E)** **Correta.** Conforme fundamentado na seção *2.4 Algoritmos de Junção: Nested Loop, Hash Join e Merge Join* deste guia, o Hash Join é absolutamente inapto para processar junções baseadas em operadores de desigualdade (`t1.id < t2.id` ou `t1.valor BETWEEN t2.min AND t2.max`). Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 13ª/2014) ao estabelecer que "ALTER TABLE processo ADD CONSTRAINT check_vara CHECK (vara_processo BETWEEN 0 AND 28)".
>
> **Gabarito: E**

---

### Teste 272
**(FGV – TCE/GO – 2024 – Analista de Controle Externo - Tecnologia da Informação)**
O comando EXPLAIN no sistema PostgreSQL, versão 16, desempenha um papel crucial na análise e otimização do desempenho das consultas SQL. Compreender o funcionamento e a saída desse comando é essencial para otimizar o desempenho do sistema. Neste contexto, o comando EXPLAIN

* **A)** exibe informações sobre o histórico de execução de consultas no banco de dados, incluindo detalhes sobre transações anteriores.
* **B)** indica ao planejador que escolha como custo estimado de execução de consultas que utilizam a cláusula EXISTS o menor custo inicial em vez do menor custo total.
* **C)** modifica, em conjunto com a cláusula ANALYZE e WAL, a estrutura física dos arquivos de dados no disco para otimizar o desempenho das consultas.
* **D)** monitora o espaço em disco utilizado por tabelas e índices no banco de dados, permitindo a otimização do armazenamento e reconstrução de índices CLUSTERED.
* **E)** oferece uma interface gráfica para criar e modificar tabelas no banco de dados PostgreSQL escritas utilizando a sublinguagem DDL.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "exibe informações sobre o histórico de execução de consultas no banco de dados, incluindo detalhes sobre...". De acordo com a teoria estudada em *2.2 Análise de Planos: EXPLAIN vs. EXPLAIN ANALYZE*, a consulta NÃO é executada no banco de dados. Os valores exibidos para `cost` (custo inicial e custo total de processamento), `rows` (cardinalidade estimada) e `width` (tamanho em bytes por linha) são puramente teóricos.
> - **B)** **Correta.** Conforme fundamentado na seção *2. Otimização de Consultas e Planos de Execução (Query Tuning)* deste guia, o Query Tuning envolve a análise algorítmica e heurística empregada pelo SGBD para converter o comando declarativo SQL em uma árvore sequencial de operadores de acesso a dados de menor custo computacional. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/GO/2024) ao estabelecer que "indica ao planejador que escolha como custo estimado de execução de consultas que utilizam a cláusula EXISTS o...".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "modifica, em conjunto com a cláusula ANALYZE e WAL, a estrutura física dos arquivos de dados no disco para...". De acordo com a teoria estudada em *3.2 Parâmetros Críticos de Memória*, trata-se de uma diretriz métrica informativa utilizada exclusivamente pelo planejador de consultas (CBO) para estimar a quantidade total de memória disponível para armazenar páginas em cache (somando `shared_buffers` e o cache de disco do sistema operacional).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "monitora o espaço em disco utilizado por tabelas e índices no banco de dados, permitindo a otimização do...". De acordo com a teoria estudada em *2.2 Análise de Planos: EXPLAIN vs. EXPLAIN ANALYZE*, gera e exibe o plano de execução teórico estimado pelo otimizador.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "oferece uma interface gráfica para criar e modificar tabelas no banco de dados PostgreSQL escritas utilizando a...". De acordo com a teoria estudada em *2.3 Estratégias de Varredura: Seq Scan, Index Scan, Index Only Scan e Bitmap Scan*, o motor obtém a resposta sem tocar nos blocos de dados da tabela. — Consultas cujas colunas requeridas formam um índice cobridor (*covering index*). No PostgreSQL, requer consulta ao *Visibility Map* para garantir visibilidade MVCC.
>
> **Gabarito: B**

---

## 3. Arquitetura e Administração do PostgreSQL

O PostgreSQL é um Sistema Gerenciador de Banco de Dados Objeto-Relacional (SGBD-OR) de código aberto reconhecido por sua robustez, conformidade estrita com padrões SQL e arquitetura altamente modular e extensível.

### 3.1 Modelo de Processos e Gerenciamento de Conexões

Diferente de sistemas multithreaded (como MySQL ou SQL Server), o PostgreSQL adota uma arquitetura clássica baseada em **múltiplos processos independentes**:

* **Processo Mestre (`postmaster` / `postgres server process`):**
    - O daemon principal inicializa o servidor de banco de dados, aloca a memória compartilhada inicial e escuta em uma porta de rede (porta padrão `5432`).
    - Para cada nova conexão de cliente recebida, o `postmaster` invoca uma chamada de sistema `fork()` para gerar um processo de backend dedicado (*client backend process*).
    - Cada processo de backend gerencia uma única conexão de ponta a ponta e possui seu próprio espaço de memória privado (*process-private memory*).
    - **Implicação arquitetural:** A criação de centenas ou milhares de conexões diretas esgota a memória do sistema operacional devido à sobrecarga de processos. Por isso, ambientes de produção de alta escala exigem obrigatoriamente um gerenciador externo de *connection pooling* (ex.: **PgBouncer**).

* **Processos Auxiliares de Background:**
    - `bgwriter` (Background Writer): Grava continuamente páginas de dados alteradas (*dirty buffers*) da memória compartilhada para o disco de forma assíncrona, liberando espaço nos buffers para novas leituras.
    - `checkpointer`: Executa periodicamente a operação de *checkpoint*, garantindo que todos os blocos sujos na memória até determinado ponto do log WAL sejam sincronizados fisicamente no disco.
    - `walwriter`: Descarrega os registros do buffer de WAL para o armazenamento de disco de forma contínua.
    - `autovacuum launcher` e `autovacuum workers`: Processos automáticos que orquestram a limpeza de registros mortos causados pelo modelo MVCC e atualizam as estatísticas de otimização.

### 3.2 Parâmetros Críticos de Memória

A memória no PostgreSQL é dividida categoricamente entre a Memória Compartilhada (*Shared Memory*) e a Memória Privada de Processo (*Process-Private Memory*):

```
+-----------------------------------------------------------------------------------+
|                        MEMÓRIA COMPARTILHADA (SHARED MEMORY)                      |
|                                                                                   |
|  +---------------------------------------------+  +----------------------------+  |
|  |             shared_buffers                  |  |         wal_buffers        |  |
|  | (Cache de Páginas de Tabelas e Índices)     |  | (Buffer de Logs de WAL)    |  |
|  +---------------------------------------------+  +----------------------------+  |
+-----------------------------------------------------------------------------------+
                                          ▲
                                          │ Comunicação via IPC
  +---------------------------------------+---------------------------------------+
  │                                                                               │
  ▼                                                                               ▼
+------------------------------------+          +------------------------------------+
|  BACKEND PROCESS 1 (Privado)       |          |  BACKEND PROCESS 2 (Privado)       |
|  - work_mem (por operação/ord/hash)|          |  - work_mem (por operação/ord/hash)|
|  - maintenance_work_mem            |          |  - maintenance_work_mem            |
+------------------------------------+          +------------------------------------+
```

1. **`shared_buffers`:**
    - Define a quantidade de memória primária alocada pelo PostgreSQL para armazenar blocos de dados e índices em cache na memória compartilhada.
    - Em servidores dedicados Linux/Unix, a recomendação clássica de ajuste (*tuning*) gira em torno de **25% da memória RAM física total**. Valores excessivamente altos (acima de 40-50%) podem ser prejudiciais, pois o PostgreSQL depende em conjunto do *page cache* nativo do sistema operacional.

2. **`work_mem`:**
    - Define a quantidade máxima de memória privada que pode ser usada por **uma única operação interna de ordenação** (`ORDER BY`, `DISTINCT`) ou **tabela hash** (em `Hash Join` ou agregação por `GROUP BY`) antes de despejar dados para arquivos temporários no disco.
    - **Armadilha Crítica:** O valor de `work_mem` **NÃO é alocado por cliente ou por consulta**, mas sim **POR OPERAÇÃO dentro de uma consulta**. Uma consulta complexa que contenha 4 junções Hash e 2 ordenações simultâneas pode consumir até 6 vezes o valor de `work_mem` para uma única conexão ativa.

3. **`maintenance_work_mem`:**
    - Memória privada alocada para operações pontuais de manutenção, tais como execução de `VACUUM`, `CREATE INDEX`, `REINDEX` e adição de chaves estrangeiras. Como essas rotinas não rodam concorrentemente por centenas de usuários, pode ser dimensionada com valores muito mais generosos (ex.: 1 GB a 2 GB).

4. **`effective_cache_size`:**
    - Não aloca memória física real. Trata-se de uma diretriz métrica informativa utilizada exclusivamente pelo planejador de consultas (CBO) para estimar a quantidade total de memória disponível para armazenar páginas em cache (somando `shared_buffers` e o cache de disco do sistema operacional). Um valor padrão muito conservador faz o CBO preferir *Seq Scans* a *Index Scans*.

### 3.3 MVCC, Limpeza de Espaço e o Mecanismo VACUUM

O PostgreSQL implementa o controle de concorrência multiversão (MVCC) por meio de duplicação de versões de tuplas no próprio arquivo de dados:

- Um comando `UPDATE` não sobrescreve a tupla existente in-place; ele marca a tupla antiga como obsoleta (registrando o ID da transação no atributo oculto `xmax`) e insere uma tupla inteiramente nova no bloco com o novo valor (marcando `xmin`).
- Um comando `DELETE` apenas marca a linha com o identificador de transação `xmax`.
- As tuplas antigas tornam-se **tuplas mortas** (*dead tuples*), consumindo espaço físico em disco (*bloat*).

O utilitário `VACUUM` é o mecanismo responsável por recuperar esse espaço:

* **`VACUUM` (Padrão / Concorrente):**
    - Percorre as páginas, identifica as tuplas mortas que não são mais visíveis a nenhuma transação ativa e marca o espaço ocupado por elas como livre para reutilização interna por futuros `INSERT` ou `UPDATE` na mesma tabela.
    - **Não reduz o tamanho físico do arquivo no sistema operacional** (salvo no caso de páginas inteiramente vazias no final do arquivo físico).
    - Pode ser executado concorrentemente com operações normais de leitura e escrita (`SELECT`, `INSERT`, `UPDATE`, `DELETE`) sem bloquear a tabela com travas exclusivas.
* **`VACUUM FULL`:**
    - Reescreve completamente a tabela em um novo arquivo físico no disco, compactando os dados e eliminando integralmente todo o espaço morto (*bloat*), devolvendo o espaço livre ao sistema operacional.
    - **Desvantagem Crítica:** Exige um bloqueio exclusivo estrito (**ExclusiveLock**) sobre a tabela inteira, impedindo quaisquer operações concorrentes de leitura e escrita até o término do processo. Requer ainda espaço livre em disco suficiente para manter uma cópia temporária da tabela completa durante a execução.
* **`autovacuum`:**
    - Daemon residente que aciona automaticamente processos de limpeza e atualização de estatísticas (`ANALYZE`) com base em limites proporcionais de modificação de tuplas (`autovacuum_vacuum_threshold` e `autovacuum_vacuum_scale_factor`).

### 3.4 Write-Ahead Logging (WAL) e Checkpoints

Para assegurar a durabilidade (D do ACID) e a recuperação contra falhas (*crash recovery*), o PostgreSQL adota o princípio de **Write-Ahead Logging (WAL)**:

- Nenhuma alteração em página de dados pode ser gravada no armazenamento persistente principal antes que os registros correspondentes do log de transações (WAL) tenham sido gravados e sincronizados fisicamente em disco (`fsync`).
- **Checkpoints:** Evento de sincronização acionado por tempo (`checkpoint_timeout`) ou por volume de dados gerados no WAL (`max_wal_size`). O processo `checkpointer` força a gravação de todos os blocos alterados que residem nos `shared_buffers` para o disco e insere um registro demarcador no arquivo WAL. Na ocorrência de uma queda de energia ou travamento do sistema operacional (*crash*), a recuperação do banco só precisa reproduzir os registros do WAL a partir do último checkpoint consolidado, minimizando o tempo de recuperação.

---

### Teste 273
**(FCC – TRT 16ª – 2014 – Analista Judiciário - Tecnologia da Informação)**
Em um banco de dados Oracle, um usuário poderá conceder qualquer privilégio de objeto, sobre qualquer objeto de esquema que possua, para qualquer outro usuário ou função. Para conceder, por exemplo, a permissão de insert e select na tabela cliente para o usuário mac30, de forma que ele possa conceder estas permissões a outros usuários sobre esta tabela, utiliza- se a instrução

* **A)** GRANT insert, select ON cliente TO mac30 WITH GRANT OPTION;
* **B)** CREATE ROLE insert, select ON cliente TO mac30 WITH LICENCE ON;
* **C)** GRANT ADD insert, select FROM cliente TO mac30 WITH GRANT OPTION;
* **D)** GRANT insert, select FROM cliente TO mac30 WITH GRANT ON;
* **E)** GRANT insert, select FROM cliente TO mac30 WITH GRANT;

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *3.3 MVCC, Limpeza de Espaço e o Mecanismo VACUUM* deste guia, pode ser executado concorrentemente com operações normais de leitura e escrita (`SELECT`, `INSERT`, `UPDATE`, `DELETE`) sem bloquear a tabela com travas exclusivas. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 16ª/2014) ao estabelecer que "GRANT insert, select ON cliente TO mac30 WITH GRANT OPTION".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "CREATE ROLE insert, select ON cliente TO mac30 WITH LICENCE ON". De acordo com a teoria estudada em *4.2 Processos de Background Mandatórios (DBWn, LGWR, CKPT, SMON, PMON)*, processo Crítico de Commit: Quando uma transação executa um comando `COMMIT`, o processo LGWR sincroniza obrigatoriamente e de forma síncrona o registro de commit no Redo Log em disco antes de retornar a mensagem de confirmação de sucesso ao cliente.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "GRANT ADD insert, select FROM cliente TO mac30 WITH GRANT OPTION". De acordo com a teoria estudada em *3.3 MVCC, Limpeza de Espaço e o Mecanismo VACUUM*, percorre as páginas, identifica as tuplas mortas que não são mais visíveis a nenhuma transação ativa e marca o espaço ocupado por elas como livre para reutilização interna por futuros `INSERT` ou `UPDATE` na mesma tabela.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "GRANT insert, select FROM cliente TO mac30 WITH GRANT ON". De acordo com a teoria estudada em *3.1 Modelo de Processos e Gerenciamento de Conexões*, para cada nova conexão de cliente recebida, o `postmaster` invoca uma chamada de sistema `fork()` para gerar um processo de backend dedicado (*client backend process*).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "GRANT insert, select FROM cliente TO mac30 WITH GRANT". De acordo com a teoria estudada em *3.2 Parâmetros Críticos de Memória*, armadilha Crítica: O valor de `work_mem` NÃO é alocado por cliente ou por consulta, mas sim POR OPERAÇÃO dentro de uma consulta.
>
> **Gabarito: A**

---

### Teste 274
**(CEBRASPE – STJ – 2015 – Analista Judiciario Suporte Em Tecnologia Da Informacao)**
O ajuste de índices é um procedimento utilizado para aumentar o desempenho de um banco de dados. Esse ajuste é realizado removendo-se ou inserindo-se índices apropriados para as relações, visto que o gargalo de desempenho pode ser causado pelo excesso de atualizações ou de consultas no banco de dados. Analistas de TI do STJ desenvolveram um sistema para comunicação por meio de trocas de mensagens entre os funcionários do tribunal. A fim de garantir segurança nas comunicações, cada servidor do órgão configurou o sistema com um par de chaves digitais — uma pública e uma privada — e com um certificado digital. Assim, a comunicação segura funciona da seguinte forma: a mensagem do emissor é cifrada com a chave pública do receptor e enviada a um servidor; posteriormente, o receptor busca essa mensagem e a decifra utilizando sua chave privada. Após os servidores do STJ terem recebido instruções referentes à utilização desse sistema, André enviou mensagens para Maria; no entanto, Pedro teve acesso e revelou as mensagens destinadas à Maria antes que ela tivesse buscado as mensagens no servidor.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Correta.** O item está **Certo**. Conforme fundamentado na seção *3.2 Parâmetros Críticos de Memória* deste guia, define a quantidade máxima de memória privada que pode ser usada por uma única operação interna de ordenação (`ORDER BY`, `DISTINCT`) ou tabela hash (em `Hash Join` ou agregação por `GROUP BY`) antes de despejar dados para arquivos temporários no disco. Dessa forma, está plenamente correta a proposição da banca (CEBRASPE – STJ/2015) ao afirmar que "O ajuste de índices é um procedimento utilizado para aumentar o desempenho de um banco de dados. Esse ajuste...".
> - **E)** **Incorreta.** A marcação como **Errado** não procede, visto que a assertiva guarda integral conformidade com a teoria estudada em *4.2 Processos de Background Mandatórios (DBWn, LGWR, CKPT, SMON, PMON)*, segundo a qual processo Crítico de Commit: Quando uma transação executa um comando `COMMIT`, o processo LGWR sincroniza obrigatoriamente e de forma síncrona o registro de commit no Redo Log em disco antes de retornar a mensagem de confirmação de sucesso ao cliente.
>
> **Gabarito: C**

---

## 4. Arquitetura e Administração do Oracle Database

O Oracle Database adota uma separação rigorosa e altamente formalizada entre a entidade computacional em memória (Instância) e a estrutura física armazenada em disco (Banco de Dados).

### 4.1 Instância vs. Banco de Dados e Estruturas de Memória (SGA e PGA)

A terminologia oficial estabelece:

- **Banco de Dados (Database):** Conjunto de arquivos físicos residentes no subsistema de armazenamento (HDDs, SSDs ou arrays SAN via Oracle ASM).
- **Instância (Instance):** Conjunto composto pelas estruturas de memória compartilhada (**SGA**) e pelos processos de background associados. Uma instância pode existir sem abrir o banco de dados (estados de inicialização: `NOMOUNT`, `MOUNT` e `OPEN`).

```
+---------------------------------------------------------------------------------------------------------+
|                                    SISTEMA GERENCIADOR ORACLE DATABASE                                  |
|                                                                                                         |
|  +---------------------------------------------------------------------------------------------------+  |
|  |                                  SYSTEM GLOBAL AREA (SGA)                                         |  |
|  |  +---------------------------+  +-------------------------------+  +---------------------------+  |  |
|  |  |   Database Buffer Cache   |  |          Shared Pool          |  |      Redo Log Buffer      |  |  |
|  |  | (Armazena blocos de dados)|  |  - Library Cache (SQL/Planos) |  | (Registros de Redo em mem)|  |  |
|  |  |                           |  |  - Data Dictionary Cache      |  |                           |  |  |
|  |  +---------------------------+  +-------------------------------+  +---------------------------+  |  |
|  +---------------------------------------------------------------------------------------------------+  |
|                                                                                                         |
|  +---------------------------------------------------------------------------------------------------+  |
|  |                                  PROCESSOS DE BACKGROUND (INSTÂNCIA)                              |  |
|  |      [DBWn]                 [LGWR]               [CKPT]               [SMON]             [PMON]   |  |
|  +--------│----------------------│--------------------│--------------------│------------------│------+  |
+-----------│----------------------│--------------------│--------------------│------------------│---------+
            │                      │                    │                    │                  │
            ▼                      ▼                    ▼                    ▼                  ▼
+---------------------------------------------------------------------------------------------------------+
|                                       BANCO DE DADOS FÍSICO                                             |
|   +-----------------------+     +------------------------+      +-----------------------------------+   |
|   |   Datafiles (.dbf)    |     |    Redo Log Files      |      |        Control Files (.ctl)       |   |
|   |  (Tabelas e Índices)  |     |  (Garantia de ACID)    |      | (Metadados de integridade física) |   |
|   +-----------------------+     +------------------------+      +-----------------------------------+   |
+---------------------------------------------------------------------------------------------------------+
```

1. **SGA (System Global Area):**
   Área de memória compartilhada acessível por todos os processos do servidor Oracle:

    - **Database Buffer Cache:** Mantém cópias em memória dos blocos de dados lidos dos arquivos de dados (`datafiles`). Quando uma consulta necessita de uma linha, busca primeiro o bloco neste cache; se não estiver presente, ocorre leitura física de disco.
    - **Shared Pool:** Estrutura fundamental dividida em subcomponentes essenciais:
    - *Library Cache:* Armazena comandos SQL executados, instruções PL/SQL compiladas e planos de execução gerados. Permite a reutilização de código e planos por meio de **Hard Parse** (análise sintática/semântica completa e geração de plano) e **Soft Parse** (reaproveitamento instantâneo de um plano já presente na Library Cache via *bind variables*).
    - *Data Dictionary Cache (Row Cache):* Armazena definições de tabelas, privilégios, colunas e restrições oriundas do catálogo interno de metadados.
    - **Redo Log Buffer:** Área circular de buffer em memória que captura alterações nos dados antes que estas sejam transferidas para os arquivos físicos de *Redo Log* no disco.
    - **Outras Pools:** *Large Pool* (para backup RMAN e buffers de I/O em grande escala), *Java Pool* e *Streams Pool*.

2. **PGA (Program Global Area / Process Global Area):**
    - Região de memória privada alocada exclusivamente para cada processo de servidor (*server process*).
    - Não é compartilhada. Contém áreas de trabalho privadas (*SQL Work Areas*) destinadas a operações de ordenação em memória (`Sort Area`), tabelas de junção Hash (`Hash Area`) e informações da sessão.

### 4.2 Processos de Background Mandatórios (DBWn, LGWR, CKPT, SMON, PMON)

Os processos de background realizam a ponte operacional entre a SGA e os arquivos de armazenamento em disco:

* **DBWn (Database Writer):**
    - Grava blocos de dados alterados (*dirty buffers*) do *Database Buffer Cache* nos arquivos de dados físicos (*Datafiles*).
    - É um processo assíncrono projetado para minimizar o I/O síncrono dos usuários. Grava em lotes sob gatilhos específicos (limiar de blocos sujos, ausência de buffers livres ou execução de checkpoints).
* **LGWR (Log Writer):**
    - Grava os dados do *Redo Log Buffer* da SGA nos arquivos de *Redo Log Files* no disco.
    - **Processo Crítico de Commit:** Quando uma transação executa um comando `COMMIT`, o processo LGWR sincroniza **obrigatoriamente e de forma síncrona** o registro de commit no Redo Log em disco antes de retornar a mensagem de confirmação de sucesso ao cliente.
* **CKPT (Checkpoint Process):**
    - Sinaliza ao DBWn para gravar os buffers sujos em disco e **atualiza os cabeçalhos de todos os arquivos de dados (*datafiles*) e dos arquivos de controle (*control files*)** com a numeração do System Change Number (SCN) mais recente.
* **SMON (System Monitor):**
    - Executa a **recuperação automática de falhas da instância (*instance recovery*)** durante a inicialização do banco de dados (reaplicando o Redo Log a partir do último checkpoint e revertendo transações não confirmadas). Realiza também a coalescência de extensões livres em tablespaces gerenciadas por dicionário.
* **PMON (Process Monitor):**
    - Monitora os processos dos clientes conectados. Se uma conexão ou processo de usuário falhar ou for abortado repentinamente, o PMON entra em ação para **limpar os recursos**: desfaz a transação pendente (*rollback*), libera bloqueios (*locks*) de tabela e linha que o usuário detinha e devolve a área de memória PGA ao sistema operacional.
* **ARCn (Archiver):**
    - Processo opcional (mas indispensável em produção empresarial), ativado quando o banco está configurado em modo `ARCHIVELOG`. Copia os arquivos de Redo Log que foram preenchidos para diretórios externos de arquivamento seguro (*Archive Logs*) antes que o LGWR os sobrescreva.

### 4.3 Estrutura Física e Lógica de Armazenamento

O Oracle estabelece uma hierarquia geométrica formal que desacopla a visualização relacional lógica da alocação de bytes física no sistema operacional:

```
[Visão Lógica]                                                 [Visão Física]
TABLESPACE ────────► SEGMENTO ────────► EXTENSÃO ────────► BLOCO ORACLE ────────► BLOCO SO / DISCO
(Ex: USERS)         (Ex: Tabela X)    (Conjunto de         (Unidade mínima       (Ex: 4 KB no FS)
                                       blocos contíguos)    de I/O, ex: 8 KB)
```

1. **Estrutura Física (Arquivos no Sistema Operacional / ASM):**
    - **Datafiles (.dbf):** Arquivos binários que contêm efetivamente os dados de tabelas, índices e metadados.
    - **Control Files (.ctl):** Arquivos essenciais de pequeno porte que descrevem a estrutura física do banco: nome do banco, caminho dos datafiles e redo logs, timestamp de criação e o número SCN atual. Sem o arquivo de controle íntegro, o Oracle não atinge o estado `MOUNT`. Devem ser multiplexados em discos físicos distintos.
    - **Redo Log Files:** Arquivos circulares organizados em grupos (mínimo de dois grupos) que registram todas as alterações cronológicas efetuadas no banco para fins de durabilidade e recuperação de desastres.
    - **Parameter Files (SPFILE / PFILE):** Parâmetros de inicialização e dimensionamento de memória.

2. **Estrutura Lógica:**
    - **Bloco de Dados Oracle (Data Block):** A menor unidade lógica de alocação de I/O de dados do Oracle (tipicamente 8 KB).
    - **Extensão (Extent):** Um número específico de blocos de dados Oracle logicamente e fisicamente contíguos alocados de uma só vez para acomodar o crescimento de um objeto.
    - **Segmento (Segment):** Conjunto completo de extensões alocadas para uma estrutura de dados relacional específica. Tipos de segmentos: Segmento de Dados (Tabela), Segmento de Índice, Segmento Temporário e Segmento de Undo.
    - **Tablespace:** A maior unidade lógica de armazenamento. Uma tablespace agrupa múltiplos segmentos e é mapeada fisicamente por **um ou mais Datafiles**. Um datafile pertence estrita e exclusivamente a uma única tablespace.

---

### Teste 275
**(FGV – TJ/AP – 2023 – Analista Judiciario Apoio Especializado Tecnologia Da Informacao Banco De Dados)**
No contexto de administração de conexões no Oracle, Database Link é um objeto do esquema que permite que usuários acessem objetos em bancos de dados diferentes. Observe o seguinte script: ---conexão no banco de dados staging CONNECT staging@staging CREATE PUBLIC DATABASE LINK "PRD_PROCESSO" CONNECT TO staging IDENTIFIED BY <PWD> USING 'PRD_PROCESSO'; SELECT nome FROM processo.tbl_usuario@prd_processo WHERE cpf = 99988877766; Após a execução do script acima, a instrução SELECT:

* **A)** retornará o nome do usuário com o CPF 99988877766 da tabela “tbl_usuario” do banco de dados “prd_processo”;
* **B)** retornará o nome do usuário com o CPF 99988877766 da tabela “tbl_usuario” do banco de dados “prd_processo”, se o usuário “processo” existir no banco de dados “staging”;
* **C)** retornará o nome do usuário com o CPF 99988877766 da tabela “tbl_usuario” do banco de dados “prd_processo”, se existir sinônimo público para a tabela “tbl_usuario” no banco de dados “prd_processo”;
* **D)** não retornará o nome do usuário com o CPF 99988877766 da tabela “tbl_usuario” do banco de dados “prd_processo”, porque o Database Link deve ser criado no banco de dados remoto especificado em USING 'PRD_PROCESSO';
* **E)** não retornará o nome do usuário com o CPF 99988877766 da tabela “tbl_usuario” do banco de dados “prd_processo”, porque a instrução deve ser executada com o usuário “staging” na cláusula FROM staging.tbl_usuario@prd_processo.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *4.2 Processos de Background Mandatórios (DBWn, LGWR, CKPT, SMON, PMON)* deste guia, se uma conexão ou processo de usuário falhar ou for abortado repentinamente, o PMON entra em ação para limpar os recursos: desfaz a transação pendente (*rollback*), libera bloqueios (*locks*) de tabela e linha que o usuário detinha e devolve a área de memória PGA ao sistema operacional. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/AP/2023) ao estabelecer que "retornará o nome do usuário com o CPF 99988877766 da tabela “tbl_usuario” do banco de dados “prd_processo”".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "retornará o nome do usuário com o CPF 99988877766 da tabela “tbl_usuario” do banco de dados “prd_processo”, se o...". De acordo com a teoria estudada em *1.2 Índices Clusterizados vs. Não-Clusterizados, Parciais e Baseados em Expressão*, no PostgreSQL, o comando `CLUSTER tabela USING nome_indice` reorganiza as linhas fisicamente no disco com base no índice, mas não mantém essa ordem automaticamente em inserções futuras (exige nova execução manual de `CLUSTER`).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "retornará o nome do usuário com o CPF 99988877766 da tabela “tbl_usuario” do banco de dados “prd_processo”, se...". De acordo com a teoria estudada em *4.1 Instância vs. Banco de Dados e Estruturas de Memória (SGA e PGA)*, instância (Instance): Conjunto composto pelas estruturas de memória compartilhada (SGA) e pelos processos de background associados. Uma instância pode existir sem abrir o banco de dados (estados de inicialização: `NOMOUNT`, `MOUNT` e `OPEN`).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "não retornará o nome do usuário com o CPF 99988877766 da tabela “tbl_usuario” do banco de dados “prd_processo”...". De acordo com a teoria estudada em *4. Arquitetura e Administração do Oracle Database*, o Oracle Database adota uma separação rigorosa e altamente formalizada entre a entidade computacional em memória (Instância) e a estrutura física armazenada em disco (Banco de Dados).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "não retornará o nome do usuário com o CPF 99988877766 da tabela “tbl_usuario” do banco de dados “prd_processo”...". De acordo com a teoria estudada em *1.2 Índices Clusterizados vs. Não-Clusterizados, Parciais e Baseados em Expressão*, a banca FCC costuma afirmar categoricamente que o uso de funções em colunas na cláusula `WHERE` (ex.: `WHERE UPPER(nome) = 'SILVA'`) inviabiliza o uso de índices comuns do tipo B-Tree, forçando um *Full Table Scan*, a menos que exista expressamente um Índice Baseado em Função (*Function-Based Index*).
>
> **Gabarito: A**

---

### Teste 276
**(FCC – TRT 4ª – 2015 – Analista Judiciário - Tecnologia Da Informação)**
O Sistema Gerenciador de Banco de Dados (SGBD)

* **A)** SQL Server 2014 possui várias tecnologias de BI, como o Integration Services, uma plataforma que inclui pacotes que fornecem processamento de extração, transformação e carregamento (ETL) para armazenamento de dados.
* **B)** PostegreSQL 9.4 utiliza um modelo cliente/servidor. Uma sessão PostgreSQL consiste de 2 processos cooperativos: o processo servidor que executa as operações no BD e o processo usuário-cliente que gerencia os arquivos do BD.
* **C)** Oracle 11g utiliza o seguinte comando para criar um novo BD, denominado meuBD: $createdatabase meuBD.
* **D)** PostegreSQL utiliza o pacote DBMS_CONNECTION_POOL para gerenciar o Database Resident Connection Pool, cujos procedimentos são usados pelo Administrador para configurar parâmetros pool como resize e trigger limit.
* **E)** Oracle 11g permite que o Analysis Services e o Reporting Services possam ser instalados como servidores autônomos em aplicativos de serviço compartilhado em um farm do SharePoint.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *3. Arquitetura e Administração do PostgreSQL* deste guia, o PostgreSQL é um Sistema Gerenciador de Banco de Dados Objeto-Relacional (SGBD-OR) de código aberto reconhecido por sua robustez, conformidade estrita com padrões SQL e arquitetura altamente modular e extensível. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 4ª/2015) ao estabelecer que "SQL Server 2014 possui várias tecnologias de BI, como o Integration Services, uma plataforma que inclui pacotes...".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "PostegreSQL 9.4 utiliza um modelo cliente/servidor. Uma sessão PostgreSQL consiste de 2 processos cooperativos: o...". De acordo com a teoria estudada em *3.1 Modelo de Processos e Gerenciamento de Conexões*, cada processo de backend gerencia uma única conexão de ponta a ponta e possui seu próprio espaço de memória privado (*process-private memory*).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Oracle 11g utiliza o seguinte comando para criar um novo BD, denominado meuBD: \$createdatabase meuBD". De acordo com a teoria estudada em *2. Otimização de Consultas e Planos de Execução (Query Tuning)*, o Query Tuning envolve a análise algorítmica e heurística empregada pelo SGBD para converter o comando declarativo SQL em uma árvore sequencial de operadores de acesso a dados de menor custo computacional.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "PostegreSQL utiliza o pacote DBMS_CONNECTION_POOL para gerenciar o Database Resident Connection Pool, cujos...". De acordo com a teoria estudada em *4.1 Instância vs. Banco de Dados e Estruturas de Memória (SGA e PGA)*, banco de Dados (Database): Conjunto de arquivos físicos residentes no subsistema de armazenamento (HDDs, SSDs ou arrays SAN via Oracle ASM).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Oracle 11g permite que o Analysis Services e o Reporting Services possam ser instalados como servidores autônomos...". De acordo com a teoria estudada em *1.1 Tipos de Índices: B+Tree, Hash, Bitmap, GIN, GiST e BRIN*, b+Tree: É a estrutura padrão (*default*) na esmagadora maioria dos SGBDs relacionais (PostgreSQL, Oracle, MySQL/InnoDB, SQL Server).
>
> **Gabarito: A**

---

### Teste 277
**(FCC – TRT 9ª – 2015 – Analista Judiciário - Apoio Especializado - Tecnologia da Informação)**
Considere o programa PL/SQL para o Oracle 11g: SQL> DECLARE 2 aumento NUMBER(8,2); 3 processo VARCHAR2(10) := '555/15'; 4 BEGIN 5 SELECT HonorPericiais * 0.20 INTO aumento 6 FROM DebTrab 7 WHERE processos = NroProcesso; 8 END; 9 / O programa acima

* **A)** Oracle 11g, utiliza o comando DBMS_CONNECTION_POOL para criar um pool denominado Database Resident Connection Pool que permite utilizar bibliotecas para armazenar imagens e metadados.
* **B)** Microsoft SQL Server não precisa configurar links para outros servidores na organização, nem definir uma estratégia de backup do banco de dados, pois tudo é feito automaticamente.
* **C)** PostgreSQL pode utilizar os seguintes comandos via linha de comando: pgdump, pgdumptotal, pgrestoreall, create_db, drop_db, create_role, drop_role, dentre outros.
* **D)** PostgreSQL pode utilizar a ferramenta PGAdmin para administrar banco de dados na plataforma Windows, pois trata-se de um aplicativo da Microsoft que oferece uma interface completa de administração.
* **E)** Microsoft SQL Server, não deve excluir ou mover o log de transações, pois se houver uma falha do sistema, será necessário que o log de transações retorne o banco de dados a um estado consistente.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *2.1 Otimizador Baseado em Custo (CBO), Estatísticas e Histogramas* deste guia, estatísticas de Catálogo: Para estimar os custos com precisão, o CBO depende de metadados atualizados coletados periodicamente pelos utilitários administrativos (`ANALYZE` no PostgreSQL ou `DBMS_STATS.GATHER_TABLE_STATS` no Oracle). Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 9ª/2015) ao estabelecer que "Oracle 11g, utiliza o comando DBMS_CONNECTION_POOL para criar um pool denominado Database Resident Connection Pool...".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Microsoft SQL Server não precisa configurar links para outros servidores na organização, nem definir uma...". De acordo com a teoria estudada em *4.1 Instância vs. Banco de Dados e Estruturas de Memória (SGA e PGA)*, outras Pools: *Large Pool* (para backup RMAN e buffers de I/O em grande escala), *Java Pool* e *Streams Pool*.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "PostgreSQL pode utilizar os seguintes comandos via linha de comando: pgdump, pgdumptotal, pgrestoreall, create_db...". De acordo com a teoria estudada em *4.1 Instância vs. Banco de Dados e Estruturas de Memória (SGA e PGA)*, banco de Dados (Database): Conjunto de arquivos físicos residentes no subsistema de armazenamento (HDDs, SSDs ou arrays SAN via Oracle ASM).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "PostgreSQL pode utilizar a ferramenta PGAdmin para administrar banco de dados na plataforma Windows, pois trata-se...". De acordo com a teoria estudada em *4. Arquitetura e Administração do Oracle Database*, o Oracle Database adota uma separação rigorosa e altamente formalizada entre a entidade computacional em memória (Instância) e a estrutura física armazenada em disco (Banco de Dados).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Microsoft SQL Server, não deve excluir ou mover o log de transações, pois se houver uma falha do sistema, será...". De acordo com a teoria estudada em *1.1 Tipos de Índices: B+Tree, Hash, Bitmap, GIN, GiST e BRIN*, b+Tree: É a estrutura padrão (*default*) na esmagadora maioria dos SGBDs relacionais (PostgreSQL, Oracle, MySQL/InnoDB, SQL Server).
>
> **Gabarito: A**

---

## 🌐 Fontes Oficiais e Referências Bibliográficas

* [PostgreSQL 17 Official Documentation - Indexes](https://www.postgresql.org/docs/current/indexes.html) - Tipos de índices: B-Tree, Hash, GiST, SP-GiST, GIN e BRIN e suas indicações de uso.
* [PostgreSQL 17 Official Documentation - Using EXPLAIN for Query Tuning](https://www.postgresql.org/docs/current/using-explain.html) - Análise de planos de execução (Seq Scan, Index Scan, Bitmap Index Scan, Nested Loop, Hash Join).
* [PostgreSQL 17 Official Documentation - Routine Vacuuming and Autovacuum](https://www.postgresql.org/docs/current/routine-vacuuming.html) - Limpeza de tuplas mortas (*dead tuples*), atualização de estatísticas do otimizador (ANALYZE).
* [Oracle Database 19c Documentation - Index Architecture](https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/indexes-and-index-organized-tables.html) - Índices B-Tree, índices Bitmap e tabelas organizadas por índice (IOT).
* SILBERSCHATZ, Abraham; KORTH, Henry F.; SUDARSHAN, S. **Sistema de Banco de Dados**. 7. ed. Rio de Janeiro: GEN LTC, 2020. (Cap. 14 - Indexação; Cap. 15 - Processamento e Otimização de Consultas).
* ELMASRI, Ramez; NAVATHE, Shamkant B. **Sistemas de Banco de Dados**. 7. ed. São Paulo: Pearson, 2019. (Cap. 16 - Estruturas de Indexação para Arquivos; Cap. 18 - Estratégias de Otimização).
* HEUSER, Carlos Alberto. **Projeto de Banco de Dados**. 6. ed. Porto Alegre: Bookman, 2009. (Cap. 7 - Projeto Físico e Otimização de Índices).
