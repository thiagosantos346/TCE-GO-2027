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
    2. [Teste 267](#Teste-267)
    3. [Índices Clusterizados vs. Não-Clusterizados, Parciais e Baseados em Expressão](#12-indices-clusterizados-vs-nao-clusterizados-parciais-e-baseados-em-expressao)
    4. [Teste 268](#Teste-268)
    5. [Trade-offs e Custos de Manutenção de Índices](#13-trade-offs-e-custos-de-manutencao-de-indices)
    6. [Teste 269](#Teste-269)
2. [Otimização de Consultas e Planos de Execução (Query Tuning)](#2-otimizacao-de-consultas-e-planos-de-execucao-query-tuning)
    1. [Otimizador Baseado em Custo (CBO), Estatísticas e Histogramas](#21-otimizador-baseado-em-custo-cbo-estatisticas-e-histogramas)
    2. [Teste 270](#Teste-270)
    3. [Análise de Planos: EXPLAIN vs. EXPLAIN ANALYZE](#22-analise-de-planos-explain-vs-explain-analyze)
    4. [Teste 271](#Teste-271)
    5. [Estratégias de Varredura: Seq Scan, Index Scan, Index Only Scan e Bitmap Scan](#23-estrategias-de-varredura-seq-scan-index-scan-index-only-scan-e-bitmap-scan)
    6. [Algoritmos de Junção: Nested Loop, Hash Join e Merge Join](#24-algoritmos-de-juncao-nested-loop-hash-join-e-merge-join)
    7. [Teste 272](#Teste-272)
3. [Arquitetura e Administração do PostgreSQL](#3-arquitetura-e-administracao-do-postgresql)
    1. [Modelo de Processos e Gerenciamento de Conexões](#31-modelo-de-processos-e-gerenciamento-de-conexoes)
    2. [Parâmetros Críticos de Memória](#32-parametros-criticos-de-memoria)
    3. [Teste 273](#Teste-273)
    4. [MVCC, Limpeza de Espaço e o Mecanismo VACUUM](#33-mvcc-limpeza-de-espaco-e-o-mecanismo-vacuum)
    5. [Teste 274](#Teste-274)
    6. [Write-Ahead Logging (WAL) e Checkpoints](#34-write-ahead-logging-wal-e-checkpoints)
4. [Arquitetura e Administração do Oracle Database](#4-arquitetura-e-administracao-do-oracle-database)
    1. [Instância vs. Banco de Dados e Estruturas de Memória (SGA e PGA)](#41-instancia-vs-banco-de-dados-e-estruturas-de-memoria-sga-e-pga)
    2. [Teste 275](#Teste-275)
    3. [Processos de Background Mandatórios (DBWn, LGWR, CKPT, SMON, PMON)](#42-processos-de-background-mandatorios-dbwn-lgwr-ckpt-smon-pmon)
    4. [Teste 276](#Teste-276)
    5. [Estrutura Física e Lógica de Armazenamento](#43-estrutura-fisica-e-logica-de-armazenamento)
    6. [Teste 277](#Teste-277)
5. [Fontes Oficiais e Referências Bibliográficas](#fontes-oficiais-e-referencias-bibliograficas)

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

---

### Teste 267
**(FCC - DPE-RS - Analista de Banco de Dados)**
O Administrador de Banco de Dados de um tribunal precisa otimizar uma consulta em uma tabela que contém 15 milhões de registros. A consulta utiliza uma cláusula `WHERE status = 'CONCLUIDO' AND uf = 'RS'`, sendo que o campo `status` possui apenas 3 valores possíveis ('PENDENTE', 'EM_ANDAMENTO', 'CONCLUIDO') e `uf` possui as 27 siglas das unidades federativas do Brasil. O ambiente é predominantemente de leitura analítica com baixíssima frequência de atualizações concorrentes. Para otimizar o tempo de resposta dessas operações combinadas, a estrutura de indexação mais indicada é:

* **A)** Índice B+Tree individual em cada uma das colunas.
* **B)** Índice Hash na coluna `uf` e B+Tree na coluna `status`.
* **C)** Índices Bitmap em ambas as colunas, permitindo operações lógicas booleanas diretas.
* **D)** Índice Clusterizado invertido na coluna `status`.
* **E)** Desativação total de índices para forçar um Full Table Scan paralelo em memória.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Índices B+Tree em colunas de baixíssima cardinalidade geram árvores rasas com listas gigantescas de ROWIDs nas folhas, além de não permitirem a combinação booleana ultrarrápida nativa de bitmaps.
> - **B)** Incorreta. O índice Hash só aceita comparações de igualdade estrita e não resolve de forma combinada o filtro composto com a coluna `status`.
> - **C)** **Correta.** Índices Bitmap são ideais para colunas com **baixa cardinalidade** (poucos valores distintos, como os 3 status e as 27 UFs) em ambientes predominantemente analíticos (OLAP) e com baixa concorrência de escritas DML. O otimizador pode combinar os bitmaps gerados para cada condição através de operações booleanas em nível de bits (`AND`, `OR`), reduzindo drasticamente o I/O de leitura.
> - **D)** Incorreta. Não existe a estrutura formal "índice clusterizado invertido" com essa finalidade; a baixa cardinalidade de `status` tornaria um agrupamento físico pouco seletivo.
> - **E)** Incorreta. Varrer 15 milhões de tuplas sequencialmente (Full Table Scan) consumirá I/O massivo sem necessidade diante da viabilidade técnica do uso de índices bitmap.
> 
> **Gabarito: C**

---


### 1.2 Índices Clusterizados vs. Não-Clusterizados, Parciais e Baseados em Expressão

A relação entre a ordenação lógica do índice e a ordenação física dos blocos de dados no disco define a tipologia de agrupamento:

* **Índice Clusterizado (*Clustered Index* / *Index-Organized Table - IOT*):**
    - A própria tabela física é ordenada e armazenada de acordo com a chave do índice. As folhas da B+Tree contêm os próprios dados da linha, e não apenas ponteiros.
    - Como os dados físicos só podem seguir uma única ordem sequencial no disco, **uma tabela pode ter no máximo UM índice clusterizado** (frequentemente associado à Chave Primária).
    - Vantagem: Dispensa salto secundário aos blocos de dados (*table lookup*).
    - No PostgreSQL, o comando `CLUSTER tabela USING nome_indice` reorganiza as linhas fisicamente no disco com base no índice, mas **não mantém essa ordem automaticamente** em inserções futuras (exige nova execução manual de `CLUSTER`). No Oracle, as tabelas organizadas por índice são explicitamente criadas como `CREATE TABLE ... ORGANIZATION INDEX`.

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

### Teste 268
**(FGV - TJ-AP / Analista Judiciário - Banco de Dados - Índices Parciais e Baseados em Expressões)**
Em um sistema de auditoria de compras públicas executado sobre PostgreSQL, a tabela `PROCESSO_LICITATORIO` armazena 5.000.000 de registros. Sabe-se que 98% dos processos possuem a coluna `situacao` igual a `'CONCLUIDO'`, e apenas 2% (100.000 registros) possuem `situacao` igual a `'EM_AUDITORIA'` ou `'SUSPEITO'`. As consultas investigativas mais críticas e frequentes filtram especificamente os processos com `situacao IN ('EM_AUDITORIA', 'SUSPEITO')`. Adicionalmente, consultas por nome do fornecedor realizam buscas ignorando maiúsculas e minúsculas (`LOWER(nome_fornecedor)`).

Para atender com máxima eficiência a esses dois padrões de consulta, minimizando o consumo de armazenamento em disco e a sobrecarga de cache na memória RAM, o DBA deve criar:

* **A)** Um índice B+Tree padrão sobre toda a tabela para `situacao` e outro índice padrão para `nome_fornecedor`.
* **B)** Um Índice Parcial (*Partial Index*) com predicado `WHERE situacao IN ('EM_AUDITORIA', 'SUSPEITO')` e um Índice Baseado em Expressão (*Expression Index*) sobre `LOWER(nome_fornecedor)`.
* **C)** Um índice Bitmap completo sobre todas as colunas da tabela e desabilitar o otimizador CBO.
* **D)** Dois índices Hash clusterizados obrigatórios sem cláusula de filtragem.
* **E)** Uma tabela intermediária física desnormalizada sem nenhum índice, pois índices parciais são proibidos no padrão SQL.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Um índice B+Tree completo sobre `situacao` indexaria 5 milhões de linhas (98% das quais são irrelevantes para as consultas críticas), desperdiçando centenas de megabytes de disco e memória sem oferecer seletividade eficaz para os 98% de `'CONCLUIDO'`.
> - **B)** **CORRETA.** Estratégias especializadas de indexação:
>   1. **Índice Parcial (Partial Index):** `CREATE INDEX idx_proc_suspeito ON PROCESSO_LICITATORIO(id_processo) WHERE situacao IN ('EM_AUDITORIA', 'SUSPEITO');`. Indexa apenas os 2% de tuplas de real interesse analítico. O índice ocupa uma fração minúscula de disco, cabe perfeitamente na memória RAM (*Buffer Cache*) e tem manutenção nula quando os 98% de processos concluídos são manipulados.
>   2. **Índice Baseado em Expressão (Expression/Function-Based Index):** `CREATE INDEX idx_fornec_lower ON PROCESSO_LICITATORIO(LOWER(nome_fornecedor));`. Permite que o otimizador utilize o índice em buscas que aplicam a função `WHERE LOWER(nome_fornecedor) = 'empresa x'`, evitando varredura sequencial (*Seq Scan*).
> - **C)** Incorreta. Índices bitmap são inadequados para ambientes OLTP concorrentes e o CBO jamais deve ser desabilitado.
> - **D)** Incorreta. Índices hash só atendem igualdade simples e não atendem predicados parciais ou buscas por intervalo.
> - **E)** Incorreta. Índices parciais são suportados nativamente pelo PostgreSQL e são amplamente recomendados para dados com distribuição altamente assimétrica (*skewed data*).
> 
> **Gabarito: B**

---

### 1.3 Trade-offs e Custos de Manutenção de Índices

A criação excessiva ou inadequada de índices acarreta degradação do sistema:

- **Sobrecarga de Escrita:** A cada `INSERT`, `UPDATE` (que altere coluna indexada) ou `DELETE`, todos os índices da tabela precisam ser sincronizados atomicamente.
- **Amplificação de I/O e Fragmentação:** Divisões de nós em árvores (*page splits*) provocam fragmentação física e lógica, exigindo manutenções periódicas (`REINDEX` no PostgreSQL ou `ALTER INDEX ... REBUILD` no Oracle).
- **Consumo de Memória de Buffer:** Índices volumosos competem com os blocos de dados por espaço na memória cache principal (`shared_buffers` no PostgreSQL / `Buffer Cache` no Oracle).

---

### Teste 269
**(FCC - TRT / Analista Judiciário - TI - Trade-offs e Custos de Manutenção de Índices)**
Um analista de infraestrutura de banco de dados constatou que determinada tabela transacional de protocolo processual possuía 18 índices B+Tree secundários criados para atender a diversas consultas históricas pontuais. Embora as consultas de leitura fossem velozes, os usuários começaram a relatar lentidão excessiva e travamentos intermitentes durante operações rotineiras de cadastro de novos processos e tramitação em lote.

A explicação técnica que justifica esse comportamento reside no fato de que:

* **A)** Índices B+Tree tornam-se somente-leitura após a inserção de 1.000 registros, forçando o SGBD a reiniciar a instância.
* **B)** A existência de múltiplos índices secundários impõe uma sobrecarga computacional de I/O e CPU em operações DML (`INSERT`, `UPDATE`, `DELETE`), pois cada nova tupla inserida ou alterada exige a atualização síncrona de todas as árvores B+Tree correspondentes, além de causar fragmentação e divisões de páginas (*page splits*).
* **C)** Os índices secundários bloqueiam compulsoriamente a tabela inteira em modo exclusivo toda vez que um comando `SELECT` é disparado.
* **D)** A criação de índices desativa automaticamente o subsistema de Write-Ahead Logging (WAL), forçando o SGBD a sincronizar blocos diretamente na área de dados em modo síncrono.
* **E)** Operações de `INSERT` não utilizam índices secundários, de modo que a lentidão relatada é necessariamente decorrente de falha física nos setores do disco rígido.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Índices B+Tree são estruturas dinâmicas que suportam inserções contínuas sem qualquer limite artificial de registros.
> - **B)** **CORRETA.** Há um *trade-off* estrutural e mandatório na criação de índices:
>   - **Benefício:** Acelera exponencialmente comandos de leitura (`SELECT` com predicados seletivos, junções e ordenações).
>   - **Custo/Sobrecarga:** Penaliza diretamente as operações de modificação de dados (`INSERT`, `DELETE` e `UPDATE` de colunas indexadas). Para cada tupla inserida, o SGBD é obrigado a atualizar a tabela base e navegar em cada uma das 18 árvores de índice, alocando novas entradas e potencialmente provocando **divisões de nós/páginas (page splits)**, o que multiplica o consumo de I/O de disco, gera contenção de *latches* na memória e fragmenta as estruturas.
> - **C)** Incorreta. Leituras adquirem bloqueios compartilhados de curta duração nas páginas do índice ou utilizam MVCC, sem travar a tabela em modo exclusivo.
> - **D)** Incorreta. Operações em índices são integralmente registradas no WAL para garantir durabilidade (ACID).
> - **E)** Incorreta. Cada `INSERT` afeta diretamente todos os índices secundários da tabela.
> 
> **Gabarito: B**



---


## 2. Otimização de Consultas e Planos de Execução (Query Tuning)

O Query Tuning envolve a análise algorítmica e heurística empregada pelo SGBD para converter o comando declarativo SQL em uma árvore sequencial de operadores de acesso a dados de menor custo computacional.

### 2.1 Otimizador Baseado em Custo (CBO), Estatísticas e Histogramas

Os SGBDs modernos operam com o **Cost-Based Optimizer (CBO)**, que calcula uma estimativa matemática abstrata de custo baseada no consumo previsto de I/O em disco, ciclos de CPU e memória para diversas permutações de planos de execução.

- **Estatísticas de Catálogo:** Para estimar os custos com precisão, o CBO depende de metadados atualizados coletados periodicamente pelos utilitários administrativos (`ANALYZE` no PostgreSQL ou `DBMS_STATS.GATHER_TABLE_STATS` no Oracle). As estatísticas incluem o número total de blocos da tabela, número de tuplas, largura média dos registros e número de valores distintos por coluna (*n_distinct*).
- **Histogramas:** Quando os dados de uma coluna sofrem de **distribuição assimétrica** (*data skew*), onde certos valores ocorrem com frequência desproporcional em relação a outros, o cálculo ingênuo de cardinalidade baseado na média ($1 / \text{n\_distinct}$) falha. O CBO constrói histogramas (frequência por faixas ou *Height-Balanced / Top-Frequency / Hybrid Histograms*) para estimar a seletividade real de filtros com valores literais.

### Teste 270
**(FGV - TRT / Analista Judiciário - TI - Otimizador Baseado em Custo e Coleta de Estatísticas)**
No PostgreSQL e em outros SGBDs modernos, o subsistema responsável por avaliar múltiplos caminhos de acesso alternativos e selecionar o plano de execução mais eficiente é o Otimizador Baseado em Custo (*Cost-Based Optimizer - CBO*).

Para que o CBO realize estimativas precisas de cardinalidade e escolha entre uma varredura sequencial (*Seq Scan*) e uma varredura por índice (*Index Scan*), é indispensável que o catálogo de metadados do banco (`pg_statistic` / `pg_stats`) mantenha informações atualizadas. O comando administrativo que coleta e recalcula essas estatísticas amostrais sem bloquear a tabela para leitura é:

* **A)** `REINDEX TABLE nome_tabela;`
* **B)** `ANALYZE nome_tabela;`
* **C)** `EXPLAIN OPTIMIZE nome_tabela;`
* **D)** `CHECK TABLE nome_tabela EXTENDED;`
* **E)** `FLUSH PRIVILEGES nome_tabela;`


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. `REINDEX` reconstrói fisicamente as árvores de índices existentes, mas não atualiza as estatísticas de distribuição de dados das colunas na `pg_statistic`.
> - **B)** **CORRETA.** O comando `ANALYZE` (ou a cláusula integrada no `VACUUM ANALYZE`) faz uma amostragem estatística das páginas da tabela e popula o catálogo `pg_statistic` (visível em `pg_stats`) com dados vitais para o CBO: fração de nulos (`null_frac`), largura média em bytes (`avg_width`), contagem de valores distintos (`n_distinct`), valores mais comuns (`most_common_vals` - MCV) e histogramas de limites de intervalos (`histogram_bounds`). Ele opera sem travar a tabela para leituras ou escritas.
> - **C)** Incorreta. `EXPLAIN` apenas exibe o plano de execução gerado pelo CBO para uma dada consulta; não existe a variante sintática `EXPLAIN OPTIMIZE` para calcular estatísticas.
> - **D)** Incorreta. Comando do MySQL para verificação de corrupção física de blocos, não usado no PostgreSQL.
> - **E)** Incorreta. Comando do MySQL para recarregar privilégios de acesso DCL da memória.
> 
> **Gabarito: B**

---

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
Hash Join  (cost=12.50..35.20 rows=150 width=64) (actual time=0.085..0.210 rows=145 loops=1)
  Hash Cond: (p.categoria_id = c.id)
  ->  Seq Scan on produtos p  (cost=0.00..18.00 rows=500 width=40) (actual time=0.012..0.080 rows=500 loops=1)
  ->  Hash  (cost=10.00..10.00 rows=20 width=28) (actual time=0.045..0.045 rows=20 loops=1)
        Buckets: 1024  Batches: 1  Memory Usage: 10kB
        ->  Seq Scan on categorias c  (cost=0.00..10.00 rows=20 width=28) (actual time=0.008..0.025 rows=20 loops=1)
Planning Time: 0.150 ms
Execution Time: 0.265 ms
```

---

### Teste 271
**(FCC - SEFAZ-PE - Auditor Fiscal do Tesouro Estadual)**
No contexto de otimização de consultas e análise de planos de execução de banco de dados, avalie a seguinte instrução:
`EXPLAIN ANALYZE SELECT * FROM lancamentos WHERE valor > 50000;`
A respeito das características dos comandos `EXPLAIN` e `EXPLAIN ANALYZE`, é correto afirmar que:

* **A)** O comando `EXPLAIN` executa a consulta de forma assíncrona, coletando tempos reais de processamento de CPU.
* **B)** O comando `EXPLAIN ANALYZE` avalia as estimativas teóricas do otimizador CBO e efetivamente executa a instrução, medindo métricas e tempos reais de execução.
* **C)** Ambos os comandos apenas mostram estimativas estatísticas baseadas nos catálogos, sem jamais executar as consultas.
* **D)** O comando `EXPLAIN ANALYZE` é incapaz de apresentar os custos estimados, limitando-se a registrar o tempo total de relógio.
* **E)** O uso de `EXPLAIN ANALYZE` em consultas que realizam alterações de dados (`UPDATE` ou `DELETE`) apenas simula a modificação, sem alterar as linhas nas tabelas físicas.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O `EXPLAIN` puro não executa a consulta; seus tempos e custos exibidos são puramente derivados de estimativas estatísticas do catálogo.
> - **B)** **Correta.** O `EXPLAIN` apenas estima o plano sem processar a instrução, ao passo que o `EXPLAIN ANALYZE` gera a estimativa do CBO e **executa concretamente a consulta**, comparando o custo/linhas estimadas com o tempo real decorrido (*actual time*) e o número real de tuplas processadas (*actual rows*).
> - **C)** Incorreta. O `EXPLAIN ANALYZE` executa de fato a query.
> - **D)** Incorreta. O relatório de `EXPLAIN ANALYZE` exibe tanto a estimativa estatística prévia do planejador quanto os valores reais coletados durante o processamento.
> - **E)** Incorreta. Se aplicado a um comando DML (`UPDATE`, `DELETE`, `INSERT`), o `EXPLAIN ANALYZE` efetivamente altera os dados persistidos no banco de dados.
> 
> **Gabarito: B**

---


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

### Teste 272
**(FCC - TRT / Analista Judiciário - TI - Algoritmos de Junção Física: Nested Loop, Hash Join e Merge Join)**
O otimizador de consultas de um banco de dados relacional dispõe de três algoritmos fundamentais para processar a junção (*join*) física entre duas relações $R$ (externa/outer) e $S$ (interna/inner): *Nested Loop Join*, *Hash Join* e *Sort-Merge Join*.

Assinale a afirmativa que apresenta corretamente o cenário em que o CBO tipicamente elege o algoritmo **Hash Join**:

* **A)** Quando uma das relações possui apenas 2 registros e a outra possui índice exclusivo já ordenado.
* **B)** Quando as duas tabelas são volumosas, a condição de junção baseia-se em um teste de igualdade (equijunção, como $R.id = S.id$) e não existem índices prévios ordenados que viabilizem um Merge Join direto, sendo a menor das tabelas utilizada para construir uma tabela hash em memória.
* **C)** Quando a condição de junção utiliza predicados de desigualdade e faixas de valores, tais como $R.data \ge S.data$.
* **D)** Exclusivamente quando a consulta contém a cláusula `ORDER BY` explícita em todas as colunas de ambas as tabelas.
* **E)** Quando o volume de memória alocado para `work_mem` for de apenas 4 kilobytes, tornando inviável qualquer estrutura em memória RAM.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Com pouquíssimas linhas em uma relação e índice na outra, o CBO escolhe quase invariavelmente o **Nested Loop Join** com busca por índice na tabela interna.
> - **B)** **CORRETA.** O **Hash Join** é o algoritmo de escolha para equijunções ($=$) em conjuntos de dados médios a grandes sem ordenação prévia:
>   1. **Fase de Construção (Build Phase):** O SGBD lê a relação de menor tamanho (relação interna) e constrói uma tabela hash em memória RAM (delimitada pelo parâmetro `work_mem`), usando a chave de junção como chave de hash.
>   2. **Fase de Sondagem (Probe Phase):** O SGBD varre a relação maior (relação externa), aplica a função hash à chave de junção de cada linha e consulta a tabela hash em memória em tempo $O(1)$ para encontrar as correspondências.
> - **C)** Incorreta. O Hash Join requer predicados de equidade ($=$); para operadores de desigualdade ($>, <, \ge$), o CBO recorre a *Nested Loops* ou *Merge Joins*.
> - **D)** Incorreta. O Hash Join destrói a ordenação original dos dados; quando há `ORDER BY` coincidente com as chaves de junção, o algoritmo ideal é o **Sort-Merge Join**.
> - **E)** Incorreta. Se a memória for insuficiente para a tabela hash caber no `work_mem`, o SGBD é forçado a realizar *hash join em múltiplos lotes (multi-batch / grace hash join)* despejando partições no disco, o que degrada o desempenho.
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

---

### Teste 273
**(FCC - TRT-15ª Região - Analista Judiciário - Tecnologia da Informação)**
No Sistema Gerenciador de Banco de Dados PostgreSQL, o parâmetro de configuração `work_mem` desempenha papel vital no desempenho do sistema. Sobre esse parâmetro, é correto afirmar:

* **A)** Trata-se da área de memória global compartilhada responsável por armazenar os blocos de dados de tabelas e índices em cache para todas as conexões ativas.
* **B)** Define a quantidade máxima de memória estática alocada por cada transação, independentemente da quantidade de comandos executados no seu interior.
* **C)** É um parâmetro alocado dinamicamente por processo para operações internas como ordenações (`ORDER BY`) ou tabelas hash (`Hash Join`), podendo ser consumido múltiplas vezes em uma mesma consulta complexa.
* **D)** Especifica a quantidade de memória destinada exclusivamente ao processo `autovacuum` para compactação das tuplas mortas.
* **E)** Deve ser configurado obrigatoriamente com no mínimo 50% de toda a memória RAM física disponível no servidor de banco de dados.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A área global compartilhada de cache de blocos e índices é configurada pelo parâmetro `shared_buffers`.
> - **B)** Incorreta. O `work_mem` não é alocado por transação ou por sessão, e sim por operação relacional individual que demande ordenação ou hash.
> - **C)** **Correta.** O `work_mem` é uma área de memória privada de processo utilizada por nós do plano de execução que demandam ordenação em memória (`ORDER BY`, `DISTINCT`, Merge Join) ou tabelas hash (`Hash Join`, agregações por hash). Uma consulta contendo múltiplos joins e sorts pode alocar várias instâncias de `work_mem` simultaneamente.
> - **D)** Incorreta. A memória alocada para o processo de vacuum e criação de índices é o `maintenance_work_mem`.
> - **E)** Incorreta. Configurar `work_mem` com 50% da memória RAM física causaria rápido esgotamento de memória (*Out of Memory - OOM Kill*) pelo sistema operacional assim que houvesse conexões simultâneas executando queries concorrentes.
> 
> **Gabarito: C**

---


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

### Teste 274
**(FGV - TRT / Analista Judiciário - TI - PostgreSQL: VACUUM, Bloat e Transaction ID Wraparound)**
Em razão da arquitetura MVCC do PostgreSQL, comandos de `UPDATE` e `DELETE` não sobrescrevem tuplas fisicamente nem liberam o espaço em disco de imediato, gerando tuplas mortas (*dead tuples*) no interior das páginas de dados.

A respeito do mecanismo de limpeza e manutenção `VACUUM` no PostgreSQL, assinale a afirmativa correta:

* **A)** O comando `VACUUM` padrão (sem a opção `FULL`) bloqueia a tabela inteira para leituras até que todas as páginas de dados sejam reescritas no disco.
* **B)** O comando `VACUUM FULL` realiza a limpeza concorrente sem adquirir nenhum bloqueio exclusivo, liberando espaço diretamente para o sistema operacional sem mover dados.
* **C)** O `VACUUM` padrão marca o espaço ocupado por tuplas mortas como reutilizável para novas inserções dentro da mesma tabela sem devolver o espaço ao sistema operacional, ao passo que o `VACUUM FULL` reescreve a tabela inteira em novos blocos, devolve o espaço livre ao sistema operacional, mas exige bloqueio exclusivo total (`AccessExclusiveLock`).
* **D)** O mecanismo de *Autovacuum* deve ser permanentemente desativado em ambientes corporativos de produção para evitar concorrência com as conexões dos usuários.
* **E)** O PostgreSQL dispensa o congelamento de identificadores de transação (*Transaction ID Freeze*), pois seus identificadores de transação são inteiros de 128 bits imunes a esgotamento.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O `VACUUM` padrão roda em segundo plano e opera concorrentemente com leituras (`SELECT`) e escritas comuns (`INSERT`, `UPDATE`, `DELETE`), sem exigir bloqueio exclusivo.
> - **B)** Incorreta. O `VACUUM FULL` exige bloqueio exclusivo severo (`AccessExclusiveLock`), impedindo qualquer acesso concorrente (inclusive leitura) enquanto reconstrói a tabela.
> - **C)** **CORRETA.** No PostgreSQL:
>   - **VACUUM Padrão:** Varre as páginas, remove referências a tuplas mortas que não são mais visíveis por nenhuma transação ativa e atualiza o mapa de espaço livre (*Free Space Map - FSM*). O espaço liberado fica disponível para futuras inserções daquela mesma tabela, mas o arquivo físico no sistema operacional não diminui de tamanho.
>   - **VACUUM FULL:** Compacta e copia todas as tuplas vivas para um arquivo de dados totalmente novo, liberando o arquivo antigo e devolvendo o espaço em disco para o sistema operacional. Como contrapartida, adquire `AccessExclusiveLock` na tabela durante todo o processo.
> - **D)** Incorreta. Desativar o autovacuum causa degradação catastrófica de desempenho por inchaço (*bloat*) e paralisação do banco por *wraparound*.
> - **E)** Incorreta. Os Transaction IDs (XIDs) no PostgreSQL clássico são números inteiros de 32 bits ($2^{32} \approx 4$ bilhões de valores). Para evitar que transações antigas pareçam estar no futuro (*Transaction ID Wraparound Failure*), o autovacuum executa compulsoriamente o **VACUUM FREEZE** para marcar transações consolidadas como `FrozenTransactionId`.
> 
> **Gabarito: C**

---

### 3.4 Write-Ahead Logging (WAL) e Checkpoints

Para assegurar a durabilidade (D do ACID) e a recuperação contra falhas (*crash recovery*), o PostgreSQL adota o princípio de **Write-Ahead Logging (WAL)**:

- Nenhuma alteração em página de dados pode ser gravada no armazenamento persistente principal antes que os registros correspondentes do log de transações (WAL) tenham sido gravados e sincronizados fisicamente em disco (`fsync`).
- **Checkpoints:** Evento de sincronização acionado por tempo (`checkpoint_timeout`) ou por volume de dados gerados no WAL (`max_wal_size`). O processo `checkpointer` força a gravação de todos os blocos alterados que residem nos `shared_buffers` para o disco e insere um registro demarcador no arquivo WAL. Na ocorrência de uma queda de energia ou travamento do sistema operacional (*crash*), a recuperação do banco só precisa reproduzir os registros do WAL a partir do último checkpoint consolidado, minimizando o tempo de recuperação.



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

### Teste 275
**(FGV - TJ-AP / Analista Judiciário - Banco de Dados - Arquitetura Oracle: Estruturas de Memória SGA e PGA)**
Na arquitetura do Oracle Database, a memória é estruturada em duas grandes áreas conceituais: a *System Global Area* (SGA) e a *Program Global Area* (PGA).

A respeito das funções e componentes dessas áreas de memória, assinale a afirmativa correta:

* **A)** A PGA é uma área de memória compartilhada acessível simultaneamente por todos os processos de background da instância Oracle para troca de blocos de dados.
* **B)** A SGA é uma área de memória compartilhada alocada na inicialização da instância, que contém estruturas vitais como o *Database Buffer Cache* (armazena cópias de blocos de dados lidos do disco), o *Redo Log Buffer* (armazena registros de alterações antes de serem gravados nos redo log files) e a *Shared Pool* (contém a Library Cache e o Data Dictionary Cache).
* **C)** O *Database Buffer Cache* armazena unicamente o código-fonte compilado de rotinas em PL/SQL e gatilhos, sendo proibido de armazenar dados de tabelas.
* **D)** A *Shared Pool* é alocada dentro da PGA privada de cada sessão de usuário e é destruída imediatamente após o encerramento do comando `SELECT`.
* **E)** O processo LGWR (*Log Writer*) lê dados diretamente da PGA dos clientes e grava nos datafiles de dados a cada 3 segundos.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A PGA (*Program Global Area*) é estritamente **privada** para cada processo servidor de sessão, armazenando variáveis locais, área de ordenação (*sort area*) e informações de pilha.
> - **B)** **CORRETA.** Na arquitetura Oracle:
>   - **SGA (System Global Area):** Área de memória compartilhada alocada quando a instância inicia. Seus principais componentes são:
>     1. **Database Buffer Cache:** Mantém cópias em memória dos blocos de dados lidos dos datafiles.
>     2. **Redo Log Buffer:** Buffer circular que retém as informações de *redo* (mudanças feitas por DML/DDL) até que o processo LGWR as descarregue nos arquivos de *Redo Log* online.
>     3. **Shared Pool:** Armazena planos de execução SQL compilados e código PL/SQL (*Library Cache*) e metadados de tabelas/índices (*Data Dictionary Cache*).
>     4. **Large Pool / Java Pool / Streams Pool:** Áreas opcionais para operações pesadas de I/O de backup (RMAN), JVM e mensageria.
> - **C)** Incorreta. O *Database Buffer Cache* armazena blocos de tabelas e índices. Código compilado fica na *Library Cache* da *Shared Pool*.
> - **D)** Incorreta. A *Shared Pool* fica na SGA e é compartilhada por todas as conexões da instância.
> - **E)** Incorreta. O LGWR descarrega o *Redo Log Buffer* da SGA nos *Redo Log Files* em disco no momento do `COMMIT`, e não da PGA nos datafiles.
> 
> **Gabarito: B**

---

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

---

### Teste 276
**(FCC - TCE-RS - Auditor Público Externo - Tecnologia da Informação)**
No banco de dados Oracle, a comunicação entre as estruturas de memória da Instância e a gravação permanente no disco é realizada por processos de segundo plano (*background processes*). O processo responsável por efetuar a gravação síncrona das entradas do *Redo Log Buffer* nos arquivos físicos de *Redo Log* no momento exato em que uma transação emite o comando `COMMIT` é o:

* **A)** DBWn (Database Writer).
* **B)** LGWR (Log Writer).
* **C)** CKPT (Checkpoint).
* **D)** PMON (Process Monitor).
* **E)** SMON (System Monitor).


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O DBWn grava blocos de dados alterados (*dirty buffers*) do Buffer Cache nos *Datafiles*, de maneira assíncrona.
> - **B)** **Correta.** O processo LGWR (*Log Writer*) é o encarregado exclusivo de descarregar os registros de transação do *Redo Log Buffer* para os arquivos físicos de *Redo Log* em disco. No instante em que o cliente executa um `COMMIT`, a operação só é confirmada com sucesso após o LGWR gravar o registro de commit em disco.
> - **C)** Incorreta. O CKPT notifica o DBWn e atualiza os cabeçalhos dos datafiles e control files com o SCN atual.
> - **D)** Incorreta. O PMON limpa recursos órfãos de conexões que caíram inesperadamente (desfazendo transações pendentes e liberando locks).
> - **E)** Incorreta. O SMON executa a recuperação de falhas da instância (*instance recovery*) na inicialização do banco.
> 
> **Gabarito: B**

---


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

### Teste 277
**(FCC - TRF-3ª Região - Analista Judiciário - Informática)**
Na arquitetura do Oracle Database, a organização do armazenamento divide-se entre estruturas físicas e estruturas lógicas. Considere as seguintes assertivas:

I. Uma *Tablespace* é uma estrutura lógica que pode ser composta por um ou mais *Datafiles* físicos, mas um *Datafile* físico pode pertencer a apenas uma única *Tablespace*.  

II. Uma *Extensão* (*Extent*) lógica é formada por um conjunto contíguo de *Blocos de Dados* Oracle, e um conjunto de extensões alocadas para um objeto relacional forma um *Segmento*.  

III. Os arquivos de controle (*Control Files*) contêm o código compilado dos procedimentos PL/SQL armazenados e os blocos de dados de índices de alta performance.  

Está correto o que se afirma em:

* **A)** I e II, apenas.
* **B)** II e III, apenas.
* **C)** I e III, apenas.
* **D)** I, II e III.
* **E)** I, apenas.


---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** 
>     - **Item I:** Correto. A tablespace é a maior unidade lógica e mapeia um ou mais datafiles físicos, existindo uma relação estrita de 1:N (um datafile nunca pode pertencer a mais de uma tablespace).
>     - **Item II:** Correto. A hierarquia lógica fundamental do Oracle é: Bloco de Dados $\rightarrow$ Extensão (bloco contíguo) $\rightarrow$ Segmento (conjunto de extensões de um objeto) $\rightarrow$ Tablespace.
> - **B)** Incorreta, pois o item III é falso e o item I é verdadeiro.
> - **C)** Incorreta, pois o item III é flagrantemente falso.
> - **D)** Incorreta, pois o item III está incorreto.
> - **E)** Incorreta, pois o item II também está correto.
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
