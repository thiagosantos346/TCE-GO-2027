# -*- coding: utf-8 -*-
"""
Script to cleanly enrich Files 02, 03, 04, 05, 06 of Module 08.
Guards each file to prevent duplicate insertions.
"""

import os
import re

BASE_DIR = "fontes_de_estudo/conhecimentos_especificos_b02_ti/08_banco_de_dados"

def check_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    qs = re.findall(r"### Questão \d+", content)
    return len(qs), content

# Import enrich_file_02 and enrich_file_03 definitions from enrich_mod08_files_2_to_6
import sys
sys.path.append("scratch")
from enrich_mod08_files_2_to_6 import enrich_file_02, enrich_file_03

# ==============================================================================
# FILE 04: 04_indices_otimizacao_postgresql_e_oracle.md
# ==============================================================================
def enrich_file_04():
    path = os.path.join(BASE_DIR, "04_indices_otimizacao_postgresql_e_oracle.md")
    count, content = check_file(path)
    if count >= 10:
        print(f"File 04 already has {count} questions, skipping.")
        return

    q06 = """### Questão 06 (FGV - TJ-AP / Analista Judiciário - Banco de Dados - Índices Parciais e Baseados em Expressões)
Em um sistema de auditoria de compras públicas executado sobre PostgreSQL, a tabela `PROCESSO_LICITATORIO` armazena 5.000.000 de registros. Sabe-se que 98% dos processos possuem a coluna `situacao` igual a `'CONCLUIDO'`, e apenas 2% (100.000 registros) possuem `situacao` igual a `'EM_AUDITORIA'` ou `'SUSPEITO'`. As consultas investigativas mais críticas e frequentes filtram especificamente os processos com `situacao IN ('EM_AUDITORIA', 'SUSPEITO')`. Adicionalmente, consultas por nome do fornecedor realizam buscas ignorando maiúsculas e minúsculas (`LOWER(nome_fornecedor)`).

Para atender com máxima eficiência a esses dois padrões de consulta, minimizando o consumo de armazenamento em disco e a sobrecarga de cache na memória RAM, o DBA deve criar:

* **A)** Um índice B+Tree padrão sobre toda a tabela para `situacao` e outro índice padrão para `nome_fornecedor`.
* **B)** Um Índice Parcial (*Partial Index*) com predicado `WHERE situacao IN ('EM_AUDITORIA', 'SUSPEITO')` e um Índice Baseado em Expressão (*Expression Index*) sobre `LOWER(nome_fornecedor)`.
* **C)** Um índice Bitmap completo sobre todas as colunas da tabela e desabilitar o otimizador CBO.
* **D)** Dois índices Hash clusterizados obrigatórios sem cláusula de filtragem.
* **E)** Uma tabela intermediária física desnormalizada sem nenhum índice, pois índices parciais são proibidos no padrão SQL.

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
"""

    q07 = """### Questão 07 (FCC - TRT / Analista Judiciário - TI - Trade-offs e Custos de Manutenção de Índices)
Um analista de infraestrutura de banco de dados constatou que determinada tabela transacional de protocolo processual possuía 18 índices B+Tree secundários criados para atender a diversas consultas históricas pontuais. Embora as consultas de leitura fossem velozes, os usuários começaram a relatar lentidão excessiva e travamentos intermitentes durante operações rotineiras de cadastro de novos processos e tramitação em lote.

A explicação técnica que justifica esse comportamento reside no fato de que:

* **A)** Índices B+Tree tornam-se somente-leitura após a inserção de 1.000 registros, forçando o SGBD a reiniciar a instância.
* **B)** A existência de múltiplos índices secundários impõe uma sobrecarga computacional de I/O e CPU em operações DML (`INSERT`, `UPDATE`, `DELETE`), pois cada nova tupla inserida ou alterada exige a atualização síncrona de todas as árvores B+Tree correspondentes, além de causar fragmentação e divisões de páginas (*page splits*).
* **C)** Os índices secundários bloqueiam compulsoriamente a tabela inteira em modo exclusivo toda vez que um comando `SELECT` é disparado.
* **D)** A criação de índices desativa automaticamente o subsistema de Write-Ahead Logging (WAL), forçando o SGBD a sincronizar blocos diretamente na área de dados em modo síncrono.
* **E)** Operações de `INSERT` não utilizam índices secundários, de modo que a lentidão relatada é necessariamente decorrente de falha física nos setores do disco rígido.

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
"""

    q08 = """### Questão 08 (FGV - TRT / Analista Judiciário - TI - Otimizador Baseado em Custo e Coleta de Estatísticas)
No PostgreSQL e em outros SGBDs modernos, o subsistema responsável por avaliar múltiplos caminhos de acesso alternativos e selecionar o plano de execução mais eficiente é o Otimizador Baseado em Custo (*Cost-Based Optimizer - CBO*).

Para que o CBO realize estimativas precisas de cardinalidade e escolha entre uma varredura sequencial (*Seq Scan*) e uma varredura por índice (*Index Scan*), é indispensável que o catálogo de metadados do banco (`pg_statistic` / `pg_stats`) mantenha informações atualizadas. O comando administrativo que coleta e recalcula essas estatísticas amostrais sem bloquear a tabela para leitura é:

* **A)** `REINDEX TABLE nome_tabela;`
* **B)** `ANALYZE nome_tabela;`
* **C)** `EXPLAIN OPTIMIZE nome_tabela;`
* **D)** `CHECK TABLE nome_tabela EXTENDED;`
* **E)** `FLUSH PRIVILEGES nome_tabela;`

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
"""

    q09 = """### Questão 09 (FCC - TRT / Analista Judiciário - TI - Algoritmos de Junção Física: Nested Loop, Hash Join e Merge Join)
O otimizador de consultas de um banco de dados relacional dispõe de três algoritmos fundamentais para processar a junção (*join*) física entre duas relações $R$ (externa/outer) e $S$ (interna/inner): *Nested Loop Join*, *Hash Join* e *Sort-Merge Join*.

Assinale a afirmativa que apresenta corretamente o cenário em que o CBO tipicamente elege o algoritmo **Hash Join**:

* **A)** Quando uma das relações possui apenas 2 registros e a outra possui índice exclusivo já ordenado.
* **B)** Quando as duas tabelas são volumosas, a condição de junção baseia-se em um teste de igualdade (equijunção, como $R.id = S.id$) e não existem índices prévios ordenados que viabilizem um Merge Join direto, sendo a menor das tabelas utilizada para construir uma tabela hash em memória.
* **C)** Quando a condição de junção utiliza predicados de desigualdade e faixas de valores, tais como $R.data \\ge S.data$.
* **D)** Exclusivamente quando a consulta contém a cláusula `ORDER BY` explícita em todas as colunas de ambas as tabelas.
* **E)** Quando o volume de memória alocado para `work_mem` for de apenas 4 kilobytes, tornando inviável qualquer estrutura em memória RAM.

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
"""

    q10 = """### Questão 10 (FGV - TRT / Analista Judiciário - TI - PostgreSQL: VACUUM, Bloat e Transaction ID Wraparound)
Em razão da arquitetura MVCC do PostgreSQL, comandos de `UPDATE` e `DELETE` não sobrescrevem tuplas fisicamente nem liberam o espaço em disco de imediato, gerando tuplas mortas (*dead tuples*) no interior das páginas de dados.

A respeito do mecanismo de limpeza e manutenção `VACUUM` no PostgreSQL, assinale a afirmativa correta:

* **A)** O comando `VACUUM` padrão (sem a opção `FULL`) bloqueia a tabela inteira para leituras até que todas as páginas de dados sejam reescritas no disco.
* **B)** O comando `VACUUM FULL` realiza a limpeza concorrente sem adquirir nenhum bloqueio exclusivo, liberando espaço diretamente para o sistema operacional sem mover dados.
* **C)** O `VACUUM` padrão marca o espaço ocupado por tuplas mortas como reutilizável para novas inserções dentro da mesma tabela sem devolver o espaço ao sistema operacional, ao passo que o `VACUUM FULL` reescreve a tabela inteira em novos blocos, devolve o espaço livre ao sistema operacional, mas exige bloqueio exclusivo total (`AccessExclusiveLock`).
* **D)** O mecanismo de *Autovacuum* deve ser permanentemente desativado em ambientes corporativos de produção para evitar concorrência com as conexões dos usuários.
* **E)** O PostgreSQL dispensa o congelamento de identificadores de transação (*Transaction ID Freeze*), pois seus identificadores de transação são inteiros de 128 bits imunes a esgotamento.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O `VACUUM` padrão roda em segundo plano e opera concorrentemente com leituras (`SELECT`) e escritas comuns (`INSERT`, `UPDATE`, `DELETE`), sem exigir bloqueio exclusivo.
> - **B)** Incorreta. O `VACUUM FULL` exige bloqueio exclusivo severo (`AccessExclusiveLock`), impedindo qualquer acesso concorrente (inclusive leitura) enquanto reconstrói a tabela.
> - **C)** **CORRETA.** No PostgreSQL:
>   - **VACUUM Padrão:** Varre as páginas, remove referências a tuplas mortas que não são mais visíveis por nenhuma transação ativa e atualiza o mapa de espaço livre (*Free Space Map - FSM*). O espaço liberado fica disponível para futuras inserções daquela mesma tabela, mas o arquivo físico no sistema operacional não diminui de tamanho.
>   - **VACUUM FULL:** Compacta e copia todas as tuplas vivas para um arquivo de dados totalmente novo, liberando o arquivo antigo e devolvendo o espaço em disco para o sistema operacional. Como contrapartida, adquire `AccessExclusiveLock` na tabela durante todo o processo.
> - **D)** Incorreta. Desativar o autovacuum causa degradação catastrófica de desempenho por inchaço (*bloat*) e paralisação do banco por *wraparound*.
> - **E)** Incorreta. Os Transaction IDs (XIDs) no PostgreSQL clássico são números inteiros de 32 bits ($2^{32} \\approx 4$ bilhões de valores). Para evitar que transações antigas pareçam estar no futuro (*Transaction ID Wraparound Failure*), o autovacuum executa compulsoriamente o **VACUUM FREEZE** para marcar transações consolidadas como `FrozenTransactionId`.
> 
> **Gabarito: C**

---
"""

    q11 = """### Questão 11 (FGV - TJ-AP / Analista Judiciário - Banco de Dados - Arquitetura Oracle: Estruturas de Memória SGA e PGA)
Na arquitetura do Oracle Database, a memória é estruturada em duas grandes áreas conceituais: a *System Global Area* (SGA) e a *Program Global Area* (PGA).

A respeito das funções e componentes dessas áreas de memória, assinale a afirmativa correta:

* **A)** A PGA é uma área de memória compartilhada acessível simultaneamente por todos os processos de background da instância Oracle para troca de blocos de dados.
* **B)** A SGA é uma área de memória compartilhada alocada na inicialização da instância, que contém estruturas vitais como o *Database Buffer Cache* (armazena cópias de blocos de dados lidos do disco), o *Redo Log Buffer* (armazena registros de alterações antes de serem gravados nos redo log files) e a *Shared Pool* (contém a Library Cache e o Data Dictionary Cache).
* **C)** O *Database Buffer Cache* armazena unicamente o código-fonte compilado de rotinas em PL/SQL e gatilhos, sendo proibido de armazenar dados de tabelas.
* **D)** A *Shared Pool* é alocada dentro da PGA privada de cada sessão de usuário e é destruída imediatamente após o encerramento do comando `SELECT`.
* **E)** O processo LGWR (*Log Writer*) lê dados diretamente da PGA dos clientes e grava nos datafiles de dados a cada 3 segundos.

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
"""

    # Insert Q06 after 1.2 (before ### 1.3 Trade-offs e Custos de Manutenção de Índices)
    p1 = "### 1.3 Trade-offs e Custos de Manutenção de Índices"
    assert p1 in content
    content = content.replace(p1, q06 + "\n" + p1, 1)

    # Insert Q07 after 1.3 (before ## 2. Otimização de Consultas e Planos de Execução)
    p2 = "## 2. Otimização de Consultas e Planos de Execução (Query Tuning)"
    assert p2 in content
    content = content.replace(p2, q07 + "\n" + p2, 1)

    # Insert Q08 after 2.1 (before ### 2.2 Análise de Planos: EXPLAIN vs. EXPLAIN ANALYZE)
    p3 = "### 2.2 Análise de Planos: EXPLAIN vs. EXPLAIN ANALYZE"
    assert p3 in content
    content = content.replace(p3, q08 + "\n" + p3, 1)

    # Insert Q09 after 2.4 (before ## 3. Arquitetura e Administração do PostgreSQL)
    p4 = "## 3. Arquitetura e Administração do PostgreSQL"
    assert p4 in content
    content = content.replace(p4, q09 + "\n" + p4, 1)

    # Insert Q10 after 3.3 (before ### 3.4 Write-Ahead Logging (WAL) e Checkpoints)
    p5 = "### 3.4 Write-Ahead Logging (WAL) e Checkpoints"
    assert p5 in content
    content = content.replace(p5, q10 + "\n" + p5, 1)

    # Insert Q11 after 4.1 (before ### 4.2 Processos de Background Mandatórios)
    p6 = "### 4.2 Processos de Background Mandatórios (DBWn, LGWR, CKPT, SMON, PMON)"
    assert p6 in content
    content = content.replace(p6, q11 + "\n" + p6, 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("File 04 successfully enriched! Total questions:", len(re.findall(r"### Questão \d+", content)))

enrich_file_04()


# ==============================================================================
# FILE 05: 05_bancos_nosql_e_bancos_vetoriais.md
# ==============================================================================
def enrich_file_05():
    path = os.path.join(BASE_DIR, "05_bancos_nosql_e_bancos_vetoriais.md")
    count, content = check_file(path)
    if count >= 10:
        print(f"File 05 already has {count} questions, skipping.")
        return

    q06 = """### Questão 06 (FGV - TJ-MT / Analista Judiciário - TI - O Teorema PACELC de Daniel Abadi)
O Teorema CAP (Brewer) postula que um sistema distribuído não pode garantir simultaneamente Consistência (C), Disponibilidade (A) e Tolerância a Particionamentos de Rede (P). No entanto, o Teorema CAP aborda apenas o comportamento do sistema durante partições de rede anormais. Para descrever o comportamento em operação de rede normal, Daniel Abadi formulou o Teorema PACELC.

A respeito dos postulados formais do Teorema PACELC, assinale a afirmativa correta:

* **A)** O Teorema PACELC estabelece que se houver Partição (P), deve-se escolher entre Disponibilidade (A) e Consistência (C); Senão (Else - E), deve-se escolher entre Latência (L) e Consistência (C).
* **B)** O Teorema PACELC afirma que bancos NoSQL podem garantir Consistência forte e Latência zero em 100% do tempo sem violar leis da física.
* **C)** No teorema PACELC, a letra 'E' significa Criptografia ponta a ponta (*End-to-end Encryption*) obrigatória em redes sem fio.
* **D)** Sistemas classificados como PC/EC priorizam sempre a disponibilidade operacional em detrimento de qualquer validação de integridade.
* **E)** O teorema PACELC aplica-se exclusivamente a bancos de dados centralizados legados em servidores *mainframe*.

> **Comentário Detalhado:**
>
> - **A)** **CORRETA.** O Teorema PACELC expande o Teorema CAP estruturando o seguinte raciocínio:
>   - **Se houver Partição de Rede (P):** O sistema deve escolher entre **Disponibilidade (A)** e **Consistência (C)** (como no Teorema CAP original).
>   - **Senão (Else - E - quando o sistema opera normalmente sem falhas de partição):** O sistema distribuído ainda assim enfrenta um *trade-off* inevitável entre **Latência (L)** e **Consistência (C)**.
>   - Para obter consistência estrita (leitura de dados sempre sincronizados entre réplicas), o sistema precisa coordenar mensagens e confirmações entre múltiplos nós antes de responder, o que introduz maior latência de resposta ($L$). Se quiser latência ultrabaixa ($L$), ele responde imediatamente com os dados locais do nó mais próximo, tolerando leituras temporariamente inconsistentes ($C$).
> - **B)** Incorreta. Consistência forte e latência zero em nós geograficamente distribuídos são mutuamente excludentes devido ao limite de propagação da velocidade da luz na rede.
> - **C)** Incorreta. 'E' significa *Else* (Senão / Operação normal da rede).
> - **D)** Incorreta. Sistemas PC/EC priorizam Consistência ($C$) tanto durante partições quanto no estado normal.
> - **E)** Incorreta. Aplica-se especificamente a arquiteturas de armazenamento distribuído (*Distributed Storage*).
> 
> **Gabarito: A**

---
"""

    q07 = """### Questão 07 (FGV - TRT / Analista Judiciário - TI - Bancos Orientados a Documentos: MongoDB e Modelagem)
Em um projeto de modernização de sistemas do tribunal, a equipe de desenvolvimento optou por utilizar o banco de dados orientado a documentos MongoDB para armazenar os autos e pareceres de auditoria.

A respeito das características arquiteturais e das técnicas de modelagem de dados no MongoDB, assinale a afirmativa correta:

* **A)** O MongoDB armazena dados em tabelas rígidas com colunas estáticas definidas em scripts DDL pré-compilados.
* **B)** Os documentos no MongoDB são serializados internamente no formato BSON (*Binary JSON*), o qual estende o JSON padrão suportando tipos de dados adicionais como datas, inteiros de 64 bits e identificadores binários (`ObjectId`).
* **C)** No MongoDB é terminantemente proibido embutir documentos dentro de outros documentos (*embedding*), sendo obrigatório o uso de referências via chave estrangeira com junções `INNER JOIN` em todas as coleções.
* **D)** O MongoDB não suporta nenhum tipo de índice, realizando varreduras completas em coleções para qualquer consulta.
* **E)** As transações multi-documento são fisicamente impossíveis de serem executadas no MongoDB, mesmo em clusters de réplicas modernas.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O MongoDB adota esquema flexível (*schemaless* / *schema-on-read*) organizado em coleções (*collections*) e documentos (*documents*), sem necessidade de DDL rígido prévio.
> - **B)** **CORRETA.** Os documentos do MongoDB são codificados e persistidos em formato **BSON (Binary JSON)**, uma representação binária do modelo JSON que agrega eficiência de parsing e suporte nativo a tipos primitivos indispensáveis em bancos de dados (como `Date`, `Timestamp`, `Int64`, `Decimal128` de alta precisão monetária e `ObjectId` de 12 bytes).
> - **C)** Incorreta. A técnica de embutir documentos e subdocumentos (*Embedded Documents*) é o padrão idiomático mais recomendado no MongoDB para dados acessados conjuntamente em uma única operação atômica de I/O, evitando junções.
> - **D)** Incorreta. O MongoDB suporta índices secundários B-Tree, índices geoespaciais, índices de texto e índices multikey (para vetores e arrays).
> - **E)** Incorreta. Desde a versão 4.0, o MongoDB implementa transações ACID multi-documento completas em *Replica Sets*.
> 
> **Gabarito: B**

---
"""

    q08 = """### Questão 08 (FCC - TRT / Analista Judiciário - TI - Apache Cassandra e Modelo Wide-Column)
O Apache Cassandra é um banco de dados NoSQL distribuído pertencente à família de colunas largas (*Wide-Column / Column Family*), projetado para suportar volumes massivos de dados com escrita de altíssima velocidade e sem ponto único de falha (*Single Point of Failure*).

Na definição de uma tabela no Cassandra via CQL (*Cassandra Query Language*), a chave primária (*Primary Key*) pode ser composta por dois tipos de componentes com funções operacionais distintas:

```cql
CREATE TABLE auditoria_acessos (
    sigla_orgao text,
    data_acesso timestamp,
    id_usuario uuid,
    acao text,
    PRIMARY KEY (sigla_orgao, data_acesso, id_usuario)
);
```

Nessa definição, assinale a afirmativa que expressa corretamente os papéis de `sigla_orgao` e `(data_acesso, id_usuario)`:

* **A)** `sigla_orgao` atua como Chave de Partição (*Partition Key*), determinando em qual nó do cluster os dados residirão via algoritmo de hash consistente; e `(data_acesso, id_usuario)` atuam como Chaves de Agrupamento (*Clustering Columns*), definindo a ordenação física dos registros gravados no disco (SSTables) dentro daquela partição.
* **B)** `sigla_orgao` é um índice secundário invertido, ao passo que `data_acesso` é uma chave estrangeira que aponta para um banco relacional externo.
* **C)** Todas as três colunas são Chaves de Partição independentes, distribuindo cada linha aleatoriamente em nós distintos sem qualquer relação entre si.
* **D)** O Cassandra não suporta ordenação em disco, sendo obrigatório ordenar todas as linhas na aplicação cliente via comandos em Python.
* **E)** A chave primária no Cassandra serve exclusivamente para exibição gráfica no terminal, sem qualquer influência na distribuição física de rede ou disco.

> **Comentário Detalhado:**
>
> - **A)** **CORRETA.** Na arquitetura do Apache Cassandra:
>   - **Partition Key (Chave de Partição - `sigla_orgao`):** O Cassandra aplica uma função hash criptográfica (ex.: Murmur3Partitioner) sobre este valor para determinar o token correspondente no anel (*ring*) do cluster e direcionar o registro para o nó responsável e suas réplicas.
>   - **Clustering Columns (Colunas de Agrupamento - `data_acesso, id_usuario`):** Dentro da partição alocada naquele nó, essas colunas determinam a **ordenação física dos dados nos arquivos SSTables em disco**, permitindo consultas por faixa (*range queries*) extremamente velozes na dimensão temporal.
> - **B)** Incorreta. Não são índices invertidos e o Cassandra não possui chaves estrangeiras.
> - **C)** Incorreta. Apenas a primeira coluna (ou as colunas entre parênteses aninhados) compõe a chave de partição; as demais são colunas de clustering.
> - **D)** Incorreta. A ordenação física em disco via *Clustering Columns* é justamente o grande trunfo do modelo de dados do Cassandra.
> - **E)** Incorreta. A Primary Key rege toda a topologia de particionamento de rede e armazenamento físico em disco.
> 
> **Gabarito: A**

---
"""

    q09 = """### Questão 09 (FCC - TRT / Analista Judiciário - TI - Escolha Arquitetural: NoSQL vs. RDBMS no Controle Externo)
Em um projeto de engenharia de dados do Tribunal de Contas, a equipe de TI deve definir a tecnologia de persistência para dois subsistemas com perfis de carga e requisitos funcionais completamente distintos:

- **Subsistema 1:** Módulo de Execução Financeira e Folha de Pagamento dos servidores, exigindo estrita conformidade com ACID, integridade referencial mandatória com chaves estrangeiras, ausência de redundâncias e processamento transacional com isolamento serializável.  
- **Subsistema 2:** Repositório de Ingestão Contínua de Logs de Auditoria e Telemetria de Redes (SIEM), com taxa de 100.000 eventos semiestruturados por segundo em formato JSON, consultas por chave primária simples e necessidade de escalabilidade horizontal linear (*scale-out*) com alta disponibilidade contínua sem interrupções.

Para atender com máxima aderência técnica a cada subsistema, o arquiteto de TI deve prescrever:

* **A)** Subsistema 1: Banco Orientado a Documentos NoSQL (MongoDB); Subsistema 2: Banco Relacional Tradicional (PostgreSQL centralizado em nó único).
* **B)** Subsistema 1: Banco Relacional com suporte completo a ACID (PostgreSQL / Oracle); Subsistema 2: Banco NoSQL escalável horizontalmente (Wide-Column Cassandra ou Banco Orientado a Documentos).
* **C)** Subsistema 1: Banco Chave-Valor puro sem persistência em disco (Redis); Subsistema 2: Banco Orientado a Grafos sem índices (Neo4j).
* **D)** Ambos os subsistemas devem ser obrigatoriamente implementados em arquivos de planilha eletrônica no formato CSV em disco compartilhado NFS.
* **E)** Ambos os subsistemas devem utilizar obrigatoriamente um banco de dados NoSQL baseado no Teorema CAP com consistência eventual sem durabilidade.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Inverteu a adequação das tecnologias aos requisitos dos subsistemas.
> - **B)** **CORRETA.** Aplicação canônica dos critérios arquiteturais de seleção:
>   - **Subsistema 1:** Requer integridade referencial forte, controle transacional ACID absoluto, isolamento serializável e modelo relacional normalizado para evitar inconsistências em pagamentos. Solução ideal: **RDBMS Relacional (PostgreSQL / Oracle)**.
>   - **Subsistema 2:** Requer ingestão de dados massivos semiestruturados em altíssima velocidade de escrita contínua, tolerância a falhas de nós e expansão horizontal barata (*scale-out*). Solução ideal: **NoSQL Wide-Column (Cassandra) ou Orientado a Documentos (MongoDB)**.
> - **C)** Incorreta. Redis sem persistência perderia todos os dados de folha de pagamento em caso de reinicialização.
> - **D)** Incorreta. Planilhas CSV não atendem requisitos de concorrência, integridade ou alto volume.
> - **E)** Incorreta. O Subsistema 1 exige garantias ACID estritas e durabilidade permanente.
> 
> **Gabarito: B**

---
"""

    q10 = """### Questão 10 (FGV - TRT / Analista Judiciário - TI - Embeddings Vetoriais em Inteligência Artificial)
Com o advento dos Modelos de Linguagem de Grande Porte (LLMs) e das arquiteturas de Geração Aumentada por Recuperação (RAG), o conceito de *Embeddings* tornou-se central para a busca semântica em repositórios de jurisprudência e relatórios de auditoria.

A respeito dos *embeddings* vetoriais e de suas propriedades matemáticas e computacionais, assinale a afirmativa correta:

* **A)** Um embedding vetorial é uma representação numérica contínua em que textos, imagens ou áudios são convertidos em vetores densos de números de ponto flutuante em um espaço euclidiano multidimensional (ex.: 768 ou 1536 dimensões), onde a proximidade geométrica entre vetores reflete sua similaridade semântica.
* **B)** Embeddings vetoriais utilizam representação *sparse* (esparsa) binária do tipo One-Hot Encoding, na qual o vetor possui o tamanho exato do dicionário e 99,9% dos elementos contêm o valor zero sem capturar contexto.
* **C)** Dois textos com palavras sinônimas distintas (como *"licitação fraudada"* e *"certame viciado"*) geram vetores ortogonais com similaridade cosseno igual a zero no espaço de embeddings.
* **D)** A dimensionalidade de um embedding pode ser livremente alterada após a geração do vetor sem necessidade de reprocessar os textos no modelo de aprendizado profundo.
* **E)** Bancos de dados vetoriais dispensam vetores numéricos, realizando buscas puramente por contagem léxica de caracteres ASCII.

> **Comentário Detalhado:**
>
> - **A)** **CORRETA.** Os **embeddings** são representações numéricas densas (*dense representations*) geradas por redes neurais profundas (como encoders do Transformer, BERT, text-embedding-3). Cada documento ou trecho de texto é mapeado para um vetor de $D$ dimensões reais (ex.: 768, 1536). A geometria desse espaço latente preserva relações semânticas complexas: conceitos com significados análogos ou contextualmente próximos convergem para regiões adjacentes no espaço multidimensional, viabilizando busca por significado (*semantic search*), clustering e classificação.
> - **B)** Incorreta. Essa é a descrição das representações clássicas esparsas e ingênuas (*Bag-of-Words* e *One-Hot Encoding*), que sofrem da maldição da dimensionalidade e não capturam semântica. Embeddings são densos (*dense*).
> - **C)** Incorreta. Como capturam o significado latente, sentenças semanticamente correlatas recebem vetores direcionados para quadrantes muito próximos, resultando em alta similaridade cosseno (próxima a 1,0).
> - **D)** Incorreta. A dimensionalidade é uma propriedade estrutural fixa da arquitetura da rede neural emissora; para mudar a dimensão, os dados devem ser reprocessados pelo novo modelo correspondente.
> - **E)** Incorreta. A busca vetorial calcula explicitamente distâncias matemáticas entre os vetores de ponto flutuante.
> 
> **Gabarito: A**

---
"""

    q11 = """### Questão 11 (FGV - TRT / Analista Judiciário - TI - Busca Vetorial Aproximada: IVFFlat vs. HNSW no pgvector)
A extensão `pgvector` viabiliza o armazenamento e a busca vetorial em bancos de dados PostgreSQL. Para acelerar a busca pelos $k$ vizinhos mais próximos ($k$-NN) em bases com milhões de vetores, utilizam-se algoritmos de Busca Aproximada por Vizinhos Mais Próximos (*Approximate Nearest Neighbor - ANN*).

No `pgvector`, os dois principais tipos de índices disponíveis para busca aproximada são o **IVFFlat** e o **HNSW**. A respeito da comparação técnica entre essas duas estruturas de indexação, assinale a afirmativa correta:

* **A)** O índice IVFFlat exige que a tabela já possua dados inseridos antes de sua criação para calcular os centroides via clustering $k$-means, ao passo que o HNSW (*Hierarchical Navigable Small World*) constrói grafos multicamadas que podem ser criados progressivamente com novas inserções, oferecendo desempenho de busca e taxa de recuperação (*recall*) superiores, com o *trade-off* de demandar maior consumo de memória RAM e maior tempo de construção.
* **B)** O índice HNSW só funciona com vetores de no máximo 3 dimensões, sendo proibido para aplicações de IA generativa.
* **C)** O índice IVFFlat oferece 100% de garantia matemática de encontrar os vizinhos exatos (*Exact Nearest Neighbor*) sem qualquer aproximação heurística.
* **D)** O índice HNSW é uma árvore B+Tree simples que ordena vetores apenas pela soma algébrica de suas coordenadas.
* **E)** Ambos os índices dispensam a definição de métricas de distância, calculando exclusivamente a distância de Manhattan sem suporte a Similaridade Cosseno ou Distância Euclidiana ($L_2$).

> **Comentário Detalhado:**
>
> - **A)** **CORRETA.** Comparativo arquitetural canônico entre os índices ANN no `pgvector`:
>   - **IVFFlat (Inverted File Flat):** Baseia-se em clustering $k$-means. Divide o espaço vetorial em $N$ listas (células Voronoi/centroides). **Exige dados já carregados na tabela** para realizar o treinamento e calcular centroides adequados. Possui construção rápida e consumo de memória modesto, porém menor *recall* e menor velocidade de busca em consultas concorrentes.
>   - **HNSW (Hierarchical Navigable Small World):** Estrutura vetorial de estado da arte baseada em grafos hierárquicos multicamadas (análoga a uma Skip List para grafos). Pode ser criado com a tabela vazia e atualizado incrementalmente. Proporciona excelente velocidade de consulta e elevadíssimo *recall*, mas exige significativamente **mais memória RAM** para reter o grafo e tem construção/atualização mais demorada e intensiva em CPU.
> - **B)** Incorreta. O HNSW suporta vetores de alta dimensionalidade (como 1536 e 3072 dimensões).
> - **C)** Incorreta. O IVFFlat é um algoritmo aproximado (*ANN*), não exato (*KNN exato faz busca sequencial / flat scan*).
> - **D)** Incorreta. HNSW é uma estrutura sofisticada de grafo de mundos pequenos navegáveis, e não uma árvore B+Tree.
> - **E)** Incorreta. O `pgvector` suporta distância Euclidiana ($L_2$ - `<->`), Similaridade Cosseno (`<=>`) e Produto Escelar / Inner Product (`<#>`).
> 
> **Gabarito: A**

---
"""

    # Insert Q06 after 1.2 (before ### 1.3 Modelo BASE vs. Propriedades ACID)
    p1 = "### 1.3 Modelo BASE vs. Propriedades ACID"
    assert p1 in content
    content = content.replace(p1, q06 + "\n" + p1, 1)

    # Insert Q07 after 2.1 (before ### 2.2 Bancos Chave-Valor (Redis))
    p2 = "### 2.2 Bancos Chave-Valor (Redis)"
    assert p2 in content
    content = content.replace(p2, q07 + "\n" + p2, 1)

    # Insert Q08 after 2.3 (before ### 2.4 Bancos Orientados a Grafos (Neo4j e Cypher))
    p3 = "### 2.4 Bancos Orientados a Grafos (Neo4j e Cypher)"
    assert p3 in content
    content = content.replace(p3, q08 + "\n" + p3, 1)

    # Insert Q09 after 2.5 (before ## 3. Bancos de Dados Vetoriais e Inteligência Artificial)
    p4 = "## 3. Bancos de Dados Vetoriais e Inteligência Artificial"
    assert p4 in content
    content = content.replace(p4, q09 + "\n" + p4, 1)

    # Insert Q10 after 3.1 (before ### 3.2 Métricas Matemáticas de Distância e Similaridade)
    p5 = "### 3.2 Métricas Matemáticas de Distância e Similaridade"
    assert p5 in content
    content = content.replace(p5, q10 + "\n" + p5, 1)

    # Insert Q11 after 3.4 (before ## 🌐 Fontes Oficiais e Referências Bibliográficas)
    p6 = "## 🌐 Fontes Oficiais e Referências Bibliográficas"
    assert p6 in content
    content = content.replace(p6, q11 + "\n" + p6, 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("File 05 successfully enriched! Total questions:", len(re.findall(r"### Questão \d+", content)))


# ==============================================================================
# FILE 06: 06_replicacao_alta_disponibilidade_backup_e_seguranca.md
# ==============================================================================
def enrich_file_06():
    path = os.path.join(BASE_DIR, "06_replicacao_alta_disponibilidade_backup_e_seguranca.md")
    count, content = check_file(path)
    if count >= 10:
        print(f"File 06 already has {count} questions, skipping.")
        return

    q06 = """### Questão 06 (FCC - TRT / Analista Judiciário - TI - Replicação Síncrona vs. Assíncrona e RPO)
Em projetos de alta disponibilidade de bancos de dados para órgãos de controle externo, a escolha entre replicação síncrona e assíncrona impacta diretamente os indicadores de continuidade de negócios e o desempenho das transações.

A respeito das características operacionais da **Replicação Síncrona**, assinale a afirmativa correta:

* **A)** A replicação síncrona garante que não haverá perda de dados em caso de desastre no nó primário ($RPO = 0$), ao custo de impor uma penalidade de latência de escrita (*write latency penalty*), visto que a transação no nó primário só recebe confirmação de `COMMIT` após os dados ou registros de log serem recebidos e confirmados por ao menos uma réplica em rede.
* **B)** A replicação síncrona reduz a latência de escrita para zero porque dispensa o envio de logs para os nós secundários.
* **C)** Em caso de lentidão severa na rede entre o nó primário e a réplica síncrona, a replicação síncrona aborta o cluster inteiro e converte o banco para somente-leitura.
* **D)** A replicação assíncrona é a única que consegue atingir matematicamente um Recovery Point Objective igual a zero ($RPO = 0$).
* **E)** O PostgreSQL não suporta replicação síncrona, operando exclusivamente em modo assíncrono não-transacional.

> **Comentário Detalhado:**
>
> - **A)** **CORRETA.** A **Replicação Síncrona** vincula a conclusão da transação à gravação remota:
>   - **Garantia de RPO Zero ($RPO = 0$):** Como o nó primário aguarda a confirmação de que os registros de WAL/Redo foram recebidos (e persistidos em disco, a depender do nível de sincronismo configurado) pela réplica antes de retornar sucesso ao cliente (`COMMIT`), nenhuma transação confirmada é perdida se o nó primário falhar subitamente.
>   - **Trade-off:** Cada transação de escrita sofre penalidade de latência (*Round-Trip Time - RTT* de rede entre primário e réplica), reduzindo o *throughput* de escrita caso a latência de rede seja significativa.
> - **B)** Incorreta. A replicação síncrona aumenta a latência de escrita, não a reduz.
> - **C)** Incorreta. O primário fica em espera (*wait state*) aguardando a confirmação da réplica ou pode degradar para assíncrono se configurado com *fallbacks*, mas não aborta o cluster inteiro.
> - **D)** Incorreta. A replicação assíncrona admite defasagem de replicação (*replication lag*), podendo acarretar perda de dados em falhas abruptas ($RPO > 0$).
> - **E)** Incorreta. O PostgreSQL suporta replicação síncrona nativa via parâmetro `synchronous_commit` e `synchronous_standby_names`.
> 
> **Gabarito: A**

---
"""

    q07 = """### Questão 07 (FGV - TJ-AP / Analista Judiciário - Banco de Dados - Replicação Física vs. Replicação Lógica)
No ecossistema PostgreSQL, administradores de banco de dados podem implementar tanto a Replicação Física por Fluxo (*Physical Streaming Replication*) quanto a Replicação Lógica (*Logical Replication*).

A respeito das distinções conceituais e operacionais entre essas duas abordagens de replicação, assinale a afirmativa correta:

* **A)** A replicação lógica exige versões idênticas do PostgreSQL e a mesma arquitetura de hardware em todos os nós, ao passo que a replicação física permite replicar dados entre sistemas operacionais e versões principais (*major versions*) diferentes.
* **B)** A replicação física transfere blocos exatos do Write-Ahead Log (WAL) byte a byte, replicando a instância inteira de modo homogêneo (todas as bases de dados e objetos), enquanto a replicação lógica opera no nível de publicação/assinatura (*publish/subscribe*), permitindo replicar seletivamente tabelas individuais e executar versões diferentes do SGBD nos nós de destino.
* **C)** A replicação física permite que as réplicas em modo *Standby* recebam operações concorrentes de escrita (`INSERT` e `UPDATE`) em tabelas de produção.
* **D)** A replicação lógica dispensa a existência de chaves primárias ou identificadores únicos nas tabelas replicadas.
* **E)** A replicação física é executada exclusivamente através de comandos DDL enviados em formato texto via protocolo HTTP.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A regra é o exato inverso: a replicação **física** exige idêntica versão principal do PostgreSQL e mesma arquitetura binária, enquanto a replicação **lógica** suporta versões diferentes e sistemas operacionais distintos (sendo excelente para atualizações sem *downtime*).
> - **B)** **CORRETA.** Distinção arquitetural rigorosa:
>   - **Replicação Física (Streaming Replication):** Opera no nível binário de baixo nível do WAL. É tudo-ou-nada: a réplica é um espelho físico exato de toda a instância do cluster (todos os databases, tabelas e catálogos). A réplica opera obrigatoriamente em modo *Hot Standby* (somente leitura).
>   - **Replicação Lógica:** Baseia-se na decodificação lógica do WAL em eventos de modificação de dados (DML). Opera sob o paradigma de Publicação e Assinatura (*Pub/Sub*), permitindo replicar tabelas específicas, filtrar linhas/colunas, integrar dados com data warehouses e manter tabelas locais adicionais com escrita no nó assinante.
> - **C)** Incorreta. Instâncias em replicação física operam em modo somente-leitura (*read-only*).
> - **D)** Incorreta. A replicação lógica requer que as tabelas possuam `REPLICA IDENTITY` (chave primária ou índice único) para aplicar operações de `UPDATE` e `DELETE` na réplica.
> - **E)** Incorreta. A replicação física transfere streams de registros WAL via conexão de streaming TCP proprietária do PostgreSQL.
> 
> **Gabarito: B**

---
"""

    q08 = """### Questão 08 (FGV - TJ-AP / Analista Judiciário - Banco de Dados - Switchover vs. Failover em Alta Disponibilidade)
Em ambientes de missão crítica de tribunais, a gestão de continuidade de serviços de tecnologia da informação diferencia com rigor os procedimentos de **Switchover** e **Failover**.

A respeito dessas duas operações de transição de papéis entre nós de banco de dados, assinale a afirmativa correta:

* **A)** O *Switchover* é uma transição planejada e controlada na qual o nó primário ativo transfere a liderança para uma réplica standby sincronizada sem qualquer perda de dados ($RPO = 0$), sendo utilizado em manutenções programadas de infraestrutura; já o *Failover* é uma promoção emergencial disparada em decorrência da falha não planejada do nó primário.
* **B)** O *Failover* é realizado exclusivamente em janelas programadas durante os finais de semana e nunca envolve a promoção de réplicas.
* **C)** O *Switchover* acarreta necessariamente a perda irremediável de 1 hora de transações da base de dados.
* **D)** O *Failover* exige a aprovação física de três auditores em formulário impresso antes que qualquer software de monitoramento possa atuar.
* **E)** Ambos os termos são sinônimos perfeitos e referem-se à restauração de backups em fitas magnéticas.

> **Comentário Detalhado:**
>
> - **A)** **CORRETA.** Na engenharia de alta disponibilidade (HA):
>   - **Switchover:** É uma transição **planejada e preventiva**. O administrador coloca o nó primário em modo gracioso, garante a descarga de todos os logs para a réplica, inverte as funções (o primário torna-se secundário e a réplica é promovida a primário) com **perda zero de dados ($RPO = 0$)** e mínimo impacto na disponibilidade. É utilizado para aplicação de patches de SO, upgrades de hardware e manutenção periódica.
>   - **Failover:** É uma recuperação **emergencial não-planejada**, provocada por falha catastrófica (queda de energia, falha de hardware, pânico de kernel) no primário. A réplica é promovida para assumir o tráfego. Pode ocorrer de forma automática (via orquestradores como Patroni) ou manual, podendo incorrer em perda de dados caso a replicação fosse assíncrona.
> - **B)** Incorreta. Failover é uma ação emergencial em resposta a falhas.
> - **C)** Incorreta. Switchover é gracioso e planejado, garantindo $RPO = 0$.
> - **D)** Incorreta. Em clusters modernos de alta disponibilidade, o failover pode ser automatizado por consenso distribuído (etcd/Consul).
> - **E)** Incorreta. São conceitos de transição operacional em tempo de execução, completamente distintos de restauração de fitas.
> 
> **Gabarito: A**

---
"""

    q09 = """### Questão 09 (FGV - TRT-16 / Analista Judiciário - TI - Estratégias de Backup: Full, Diferencial e Incremental)
Para mitigar o risco de perda de dados e estabelecer janelas eficientes de cópia de segurança em uma instituição pública com 10 Terabytes de dados, a equipe de TI avaliou as estratégias de backup: Completo (*Full*), Diferencial e Incremental.

Considere a seguinte política semanal: no domingo à meia-noite é executado um Backup Full. De segunda a sábado à meia-noite, são executadas cópias auxiliares. Na quinta-feira às 10h da manhã ocorreu uma quebra física irreversível no subsistema de armazenamento primário.

A respeito do tempo de execução, consumo de armazenamento e processo de recuperação dessa base, assinale a afirmativa correta:

* **A)** Se a política adotada for de Backup Incremental, a restauração da base exigirá exclusivamente a aplicação do Backup Incremental de quarta-feira, sendo dispensável o Backup Full de domingo.
* **B)** Se a política adotada for de Backup Diferencial, a restauração da base até o estado da noite de quarta-feira exigirá apenas o Backup Full de domingo e o Backup Diferencial de quarta-feira, pois cada backup diferencial copia todas as alterações ocorridas desde o último Backup Full.
* **C)** O Backup Incremental copia todas as modificações ocorridas desde o último Backup Full, tornando o seu tamanho crescente a cada dia da semana.
* **D)** O Backup Full é o mais rápido de todos para ser gerado diariamente, consumindo menos espaço em disco do que backups incrementais.
* **E)** O Backup Diferencial copia apenas as alterações ocorridas desde o último backup diferencial, exigindo a restauração de todos os arquivos diários da semana.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O Backup Incremental grava apenas as alterações ocorridas desde o backup anterior (seja ele full ou incremental). Para restaurar na quinta-feira, seriam necessários: Full de domingo + Incremental de segunda + Incremental de terça + Incremental de quarta.
> - **B)** **CORRETA.** A mecânica dos tipos de backup é canônica em concursos de TI:
>   - **Backup Full:** Cópia completa de todos os blocos/dados da base.
>   - **Backup Diferencial:** Copia todos os dados que foram modificados **desde o último Backup Full**. Consequentemente, o diferencial de quarta-feira já engloba todas as alterações de segunda, terça e quarta. O processo de restauração é mais simples e veloz: basta restaurar o **Full de domingo + o Diferencial mais recente (quarta-feira)**.
>   - **Trade-off:** O diferencial é mais lento para gerar ao longo da semana do que o incremental (pois seu tamanho cresce a cada dia), mas proporciona um tempo de recuperação (*RTO*) mais curto e menor risco de falha na cadeia de restauração.
> - **C)** Incorreta. Quem copia desde o último Full é o Diferencial; o Incremental copia desde o último backup qualquer.
> - **D)** Incorreta. O Backup Full é o mais demorado e o que consome maior volume de armazenamento.
> - **E)** Incorreta. A assertiva descreveu o funcionamento do Backup Incremental, não do Diferencial.
> 
> **Gabarito: B**

---
"""

    q10 = """### Questão 10 (FGV - TJ-AP / Analista Judiciário - Banco de Dados - Mascaramento Dinâmico de Dados - DDM e LGPD)
Com o advento da Lei Geral de Proteção de Dados Pessoais (LGPD), órgãos de auditoria pública implementaram a técnica de Mascaramento Dinâmico de Dados (*Dynamic Data Masking - DDM*) em seus sistemas gerenciadores de banco de dados.

A respeito dos princípios de funcionamento e dos benefícios de segurança proporcionados pelo DDM, assinale a afirmativa correta:

* **A)** O DDM altera permanentemente os valores gravados nas páginas físicas do disco rígido, destruindo de forma irreversível os dados cadastrais originais da base.
* **B)** O DDM atua na camada de apresentação da consulta SQL em tempo real, ofuscando campos confidenciais (como CPF, números de cartão e remunerações) com base em privilégios e papéis do usuário conectado, mantendo os dados originais integralmente intactos e inalterados no armazenamento físico em disco.
* **C)** O DDM é uma tecnologia exclusiva de criptografia assimétrica de chaves públicas do padrão RSA de 4096 bits.
* **D)** O DDM impede que auditores realizem comandos `SELECT` nas tabelas mascaradas, retornando sempre uma mensagem de erro de compilação SQL.
* **E)** O mascaramento estático e o mascaramento dinâmico são sinônimos que dependem da exclusão física da tabela via comando `DROP TABLE`.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Modificar os dados fisicamente na base destruindo os originais caracteriza sanitização/anonimização estática irreversível, e não mascaramento dinâmico.
> - **B)** **CORRETA.** O **Dynamic Data Masking (DDM)**:
>   - Opera no momento em que a consulta é processada pelo SGBD (*on-the-fly*).
>   - Com base no contexto da sessão e nas permissões (RBAC) do usuário, regras de mascaramento pré-configuradas são aplicadas ao conjunto de resultados retornado (ex.: exibir um CPF como `XXX.XXX.123-XX` ou e-mail como `a***@orgao.gov.br` para analistas sem autorização explícita).
>   - **Propriedade fundamental:** Os dados reais persistidos nas páginas de disco e nos arquivos de log (WAL/Redo) permanecem **100% autênticos e intactos**, preservando a integridade referencial e o processamento de rotinas internas autorizadas.
> - **C)** Incorreta. DDM é uma técnica de ofuscação/política de visualização baseada em funções de formatação, e não um algoritmo de criptografia assimétrica.
> - **D)** Incorreta. O comando `SELECT` executa com sucesso normal, retornando os registros com os campos especificados mascarados.
> - **E)** Incorreta. No mascaramento estático (*Static Data Masking*), cria-se uma cópia duplicada da base com dados alterados (usada para homologação/testes); no dinâmico, os dados não são duplicados.
> 
> **Gabarito: B**

---
"""

    q11 = """### Questão 11 (FGV - TJ-RR / Analista Judiciário - Governança de TI - Controle de Acesso RBAC e Trilhas de Auditoria)
A segurança da informação em bancos de dados corporativos baseia-se em princípios de defesa em profundidade, destacando-se o Controle de Acesso Baseado em Papéis (*Role-Based Access Control - RBAC*) e a geração de Trilhas de Auditoria (*Audit Trails*).

Em relação às boas práticas de governança e implementação desses controles em SGBDs, assinale a afirmativa correta:

* **A)** O princípio do privilégio mínimo (*Least Privilege*) estabelece que privilégios administrativos irrestritos (`SUPERUSER` ou `DBA`) devem ser atribuídos preventivamente a todos os usuários corporativos para evitar abertura de chamados no suporte.
* **B)** A utilização de *Roles* (Papéis) permite agrupar privilégios de acesso a objetos do banco segundo funções de negócio (ex.: `role_auditor_externo`), associando os usuários aos papéis correspondentes, o que simplifica a governança e previne privilégios residuais decorrentes de transferências de pessoal.
* **C)** Trilhas de auditoria de banco de dados devem registrar exclusivamente operações de `SELECT`, sendo proibido registrar comandos DDL como `DROP` e `ALTER TABLE` por restrições constitucionais.
* **D)** O controle de acesso discricionário (DAC) impede que o proprietário de uma tabela conceda permissões de leitura a outros usuários.
* **E)** As trilhas de auditoria devem ser salvas na mesma tabela que sofreu auditoria com acesso de exclusão irrestrito para qualquer estagiário da organização.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O Princípio do Menor Privilégio (*Least Privilege*) dita que cada usuário ou processo deve possuir apenas os privilégios estritamente necessários para o desempenho de suas atribuições legítimas.
> - **B)** **CORRETA.** O modelo **RBAC (Role-Based Access Control)** desacopla usuários de permissões diretas:
>   1. Privilégios DDL/DML são concedidos a Papéis (*Roles*), estruturados conforme perfis funcionais da organização.
>   2. Usuários são vinculados a essas *Roles*.
>   3. Quando um colaborador muda de setor ou desliga-se do órgão, revoga-se apenas a associação de seu login com o papel correspondente, garantindo controle estrito, rastreabilidade e eliminação de privilégios excessivos (*privilege creep*).
> - **C)** Incorreta. A auditoria deve registrar prioritariamente comandos DDL críticos (`CREATE`, `ALTER`, `DROP`) e manipulações em tabelas sensíveis.
> - **D)** Incorreta. No DAC (Discretionary Access Control), o proprietário do objeto tem discricionariedade justamente para conceder privilégios a outros usuários via `GRANT`.
> - **E)** Incorreta. Trilhas de auditoria exigem proteção estrita contra modificação (*WORM - Write Once, Read Many*) e segregação de funções, jamais admitindo exclusão por usuários operacionais.
> 
> **Gabarito: B**

---
"""

    # Insert Q06 after 1.1 (before ### 1.2 Topologias de Replicação: Leader-Follower vs. Multi-Master)
    p1 = "### 1.2 Topologias de Replicação: Leader-Follower vs. Multi-Master"
    assert p1 in content
    content = content.replace(p1, q06 + "\n" + p1, 1)

    # Insert Q07 after 1.3 (before ## 2. Alta Disponibilidade (HA), Failover e Mitigação de Split-Brain)
    p2 = "## 2. Alta Disponibilidade (HA), Failover e Mitigação de Split-Brain"
    assert p2 in content
    content = content.replace(p2, q07 + "\n" + p2, 1)

    # Insert Q08 after 2.1 (before ### 2.2 O Fenômeno Crítico do Split-Brain)
    p3 = "### 2.2 O Fenômeno Crítico do Split-Brain"
    assert p3 in content
    content = content.replace(p3, q08 + "\n" + p3, 1)

    # Insert Q09 after 3.2 (before ### 3.3 Point-in-Time Recovery (PITR))
    p4 = "### 3.3 Point-in-Time Recovery (PITR)"
    assert p4 in content
    content = content.replace(p4, q09 + "\n" + p4, 1)

    # Insert Q10 after 4.2 (before ### 4.3 Trilhas de Auditoria e Controle de Acesso Baseado em Papéis (RBAC))
    p5 = "### 4.3 Trilhas de Auditoria e Controle de Acesso Baseado em Papéis (RBAC)"
    assert p5 in content
    content = content.replace(p5, q10 + "\n" + p5, 1)

    # Insert Q11 after 4.3 (before ## 🌐 Fontes Oficiais e Referências Bibliográficas)
    p6 = "## 🌐 Fontes Oficiais e Referências Bibliográficas"
    assert p6 in content
    content = content.replace(p6, q11 + "\n" + p6, 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("File 06 successfully enriched! Total questions:", len(re.findall(r"### Questão \d+", content)))

if __name__ == "__main__":
    enrich_file_02()
    enrich_file_03()
    enrich_file_04()
    enrich_file_05()
    enrich_file_06()
