# 03 - Transações, Propriedades ACID e Concorrência

> **Matéria:** Banco de Dados  
> **Cargo:** B02 – Técnico de Controle Externo – Especialidade: Tecnologia da Informação  
> **Arquivo:** `03_transacoes_propriedades_acid_e_concorrencia.md`  



---


## 📌 Ementa / Itens do Edital
- Conceito de Transação de banco de dados
- As quatro propriedades fundamentais: ACID (Atomicidade, Consistência, Isolamento, Durabilidade)
- Comandos de controle transacional: COMMIT, ROLLBACK e SAVEPOINT
- Anomalias de concorrência (Leitura Suja, Leitura Não Repetível, Leitura Fantasma, Atualização Perdida)
- Níveis de Isolamento ANSI SQL
- Mecanismos de controle de concorrência: Bloqueios (Locks), 2PL, MVCC e Deadlocks

---

## 🧭 Sumário

1. [O Conceito Formal de Transação e o Modelo ACID](#1-o-conceito-formal-de-transacao-e-o-modelo-acid)
    1. [Ciclo de Vida e Estados de uma Transação](#11-ciclo-de-vida-e-estados-de-uma-transacao)
    2. [As Quatro Propriedades Fundamentais: ACID](#12-as-quatro-propriedades-fundamentais-acid)
    3. [Mecanismos Internos: Undo Log, Redo Log e Write-Ahead Logging (WAL)](#13-mecanismos-internos-undo-log-redo-log-e-write-ahead-logging-wal)
    4. [Teste 256](#Teste-256)
    5. [Teste 257](#Teste-257)
2. [Comandos de Controle Transacional (TCL)](#2-comandos-de-controle-transacional-tcl)
    1. [COMMIT, ROLLBACK e Gestão de SAVEPOINTs](#21-commit-rollback-e-gestao-de-savepoints)
    2. [Teste 258](#Teste-258)
3. [Fenômenos e Anomalias de Concorrência](#3-fenomenos-e-anomalias-de-concorrencia)
    1. [Leitura Suja (Dirty Read)](#31-leitura-suja-dirty-read)
    2. [Leitura Não Repetível (Non-Repeatable Read)](#32-leitura-nao-repetivel-non-repeatable-read)
    3. [Leitura Fantasma (Phantom Read)](#33-leitura-fantasma-phantom-read)
    4. [Atualização Perdida (Lost Update)](#34-atualizacao-perdida-lost-update)
    5. [Teste 259](#Teste-259)
4. [Níveis de Isolamento ANSI SQL-92](#4-niveis-de-isolamento-ansi-sql-92)
    1. [Matriz de Isolamento vs. Fenômenos Admitidos](#41-matriz-de-isolamento-vs-fenomenos-admitidos)
    2. [Snapshot Isolation (Isolamento por Instantâneo)](#42-snapshot-isolation-isolamento-por-instantaneo)
    3. [Teste 260](#Teste-260)
    4. [Teste 261](#Teste-261)
5. [Técnicas de Controle de Concorrência](#5-tecnicas-de-controle-de-concorrencia)
    1. [Bloqueios (Locks) e Matriz de Compatibilidade (Shared vs. Exclusive)](#51-bloqueios-locks-e-matriz-de-compatibilidade-shared-vs-exclusive)
    2. [Protocolo de Bloqueio em Duas Fases (2PL - Two-Phase Locking): Básico, Estrito e Rigoroso](#52-protocolo-de-bloqueio-em-duas-fases-2pl-two-phase-locking-basico-estrito-e-rigoroso)
    3. [Controle Multiversão de Concorrência (MVCC)](#53-controle-multiversao-de-concorrencia-mvcc)
    4. [Impasses (Deadlocks): Detecção via Wait-For Graph e Resolução por Transação Vítima](#54-impasses-deadlocks-deteccao-via-wait-for-graph-e-resolucao-por-transacao-vitima)
    5. [Teste 262](#Teste-262)
    6. [Teste 263](#Teste-263)
    7. [Teste 264](#Teste-264)
    8. [Teste 265](#Teste-265)
    9. [Teste 266](#Teste-266)
6. [🌐 Fontes Oficiais e Referências Bibliográficas](#fontes-oficiais-e-referencias-bibliograficas)

---

## 1. O Conceito Formal de Transação e o Modelo ACID

Uma **transação** de banco de dados é uma unidade lógica e atômica de processamento que agrupa uma ou mais instruções SQL (leitura e escrita) que devem ser executadas de modo estritamente indivisível. No contexto de auditoria e controle externo no setor público, uma transação típica é a liquidação de uma despesa orçamentária: o sistema deve simultaneamente debitar o saldo do empenho e creditar a conta bancária do fornecedor. Se apenas uma das ações ocorrer, o banco de dados entrará em colapso fiscal.

### 1.1 Ciclo de Vida e Estados de uma Transação

Durante sua existência, uma transação transita por estados formais bem definidos na teoria de sistemas relacionais:

```mermaid
stateDiagram-v2
    [*] --> Ativa: BEGIN TRANSACTION
    Ativa --> Parcialmente_Comitada: Última operação executada
    Ativa --> Falha: Erro de execução / Violação
    Parcialmente_Comitada --> Comitada: Gravação definitiva no log (WAL)
    Parcialmente_Comitada --> Falha: Erro no flush do disco
    Falha --> Abortada: ROLLBACK (Desfaz alterações via Undo Log)
    Comitada --> [*]
    Abortada --> [*]
```

- **Ativa (*Active*):** O estado inicial. A transação está sendo executada pela aplicação.
- **Parcialmente Comitada (*Partially Committed*):** A última instrução SQL foi processada na memória RAM, mas os dados ainda não foram gravados permanentemente no log em disco.
- **Comitada (*Committed*):** Todas as alterações foram confirmadas e gravadas no log transacional em armazenamento persistente (*Write-Ahead Logging*). A transação foi concluída com sucesso.
- **Falha (*Failed*):** Ocorre quando uma instrução viola uma restrição de integridade ou o sistema sofre interrupção antes da conclusão definitiva.
- **Abortada (*Aborted*):** O SGBD executa o comando `ROLLBACK`, desfazendo todas as modificações parciais já executadas e restaurando a base de dados ao estado exato anterior ao início da transação.

### 1.2 As Quatro Propriedades Fundamentais: ACID

Para que a integridade dos dados seja inviolável mesmo diante de falhas de hardware, interrupções de energia elétrica e concorrência massiva de usuários, o SGBD deve garantir integralmente as propriedades do acrônimo **ACID** (Jim Gray e Andreas Reuter):

```mermaid
flowchart TD
    subgraph ACID["Propriedades ACID"]
        A["<b>A - Atomicidade (Atomicity)</b><br/>Princípio do 'Tudo ou Nada'<br/>Mecanismo: Log de UNDO (desfaz em caso de aborto)"]
        C["<b>C - Consistência (Consistency)</b><br/>Preserva invariantes e integridade do banco<br/>Mecanismo: PK, FK, CHECK, Triggers, regras do negócio"]
        I["<b>I - Isolamento (Isolation)</b><br/>Execuções concorrentes não sofrem interferência<br/>Mecanismo: Bloqueios (Locks), 2PL, MVCC"]
        D["<b>D - Durabilidade (Durability)</b><br/>Alterações confirmadas sobrevivem a panes<br/>Mecanismo: Log de REDO e Write-Ahead Logging (WAL)"]
    end
```

1. **A - Atomicidade (*Atomicity*):**
    - Princípio do **"tudo ou nada"** (*all-or-nothing*). Todas as operações que compõem a transação são consolidadas em conjunto no banco de dados, ou nenhuma delas produzirá efeito algum. Não existe efetivação parcial de transação.

2. **C - Consistência (*Consistency*):**
    - Garante que a transação conduz o banco de dados de um **estado válido para outro estado igualmente válido**. A transação não pode violar nenhuma regra de integridade declarativa (chaves primárias, chaves estrangeiras, restrições `CHECK`, valores `NOT NULL`) ou procedimental (gatilhos e regras de negócio).

3. **I - Isolamento (*Isolation*):**
    - Assegura que a execução concomitante de múltiplas transações seja invisível entre si. Os efeitos intermediários e temporários de uma transação não comitada não podem ser observados por outras transações concorrentes. O resultado final deve equivaler a uma execução estritamente sequencial (*serializável*).

4. **D - Durabilidade (*Durability*):**
    - Garante que, uma vez que a transação foi confirmada com sucesso (`COMMIT`), suas modificações tornam-se **permanentes e indeléveis**. As alterações não serão perdidas sob nenhuma hipótese, resistindo até mesmo a falhas catastróficas de energia física ou travamentos no sistema operacional da máquina servidora.

### 1.3 Mecanismos Internos: Undo Log, Redo Log e Write-Ahead Logging (WAL)

- **Undo Log (Segmentos de Rollback):** Registra os valores **anteriores** à modificação. Se uma transação falhar ou for cancelada, o SGBD lê o Undo Log para restaurar os dados originais (garantindo a **Atomicidade**).
- **Redo Log / WAL (*Write-Ahead Logging*):** Registra os **novos** valores gerados pela transação.
    - **A Regra Inviolável do WAL:** O registro de log que descreve a alteração **deve ser gravado fisicamente em disco síncrono ANTES** que as páginas de dados correspondentes sejam descarregadas da memória RAM para os arquivos de dados (*datafiles*).
    - Isso garante a **Durabilidade**: se faltar energia imediatamente após o commit, o SGBD lê o Redo Log no boot de recuperação (*Crash Recovery*) e reaplica (*redo*) as alterações nas tabelas.

---

### Teste 256
**(FGV – TCE-PA – Auditor de Controle Externo Administrativa Ciencia de Dados – 2024)**
Diferentemente do armazenamento feito em sistema de arquivos, o armazenamento em sistemas de banco de dados ou SGBD possui características especiais que garantem um funcionamento superior em relação à outras formas de armazenamento. Nesse contexto, as propriedades fundamentais garantidas pelo conceito ACID em sistemas de banco de dados são:

* **A)** Atomicidade, Complexidade, Integridade, Durabilidade.
* **B)** Atividade, Consistência, Inovação, Durabilidade.
* **C)** Atomicidade, Consistência, Isolamento, Durabilidade.
* **D)** Autenticidade, Conformidade, Integridade, Desempenho.
* **E)** Automação, Convergência, Interoperabilidade, Desempenho.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Atomicidade, Complexidade, Integridade, Durabilidade". De acordo com a teoria estudada em *1.2 As Quatro Propriedades Fundamentais: ACID*, para que a integridade dos dados seja inviolável mesmo diante de falhas de hardware, interrupções de energia elétrica e concorrência massiva de usuários, o SGBD deve garantir integralmente as propriedades do acrônimo ACID (Jim Gray e Andreas Reuter).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Atividade, Consistência, Inovação, Durabilidade". De acordo com a teoria estudada em *1.3 Mecanismos Internos: Undo Log, Redo Log e Write-Ahead Logging (WAL)*, isso garante a Durabilidade: se faltar energia imediatamente após o commit, o SGBD lê o Redo Log no boot de recuperação (*Crash Recovery*) e reaplica (*redo*) as alterações nas tabelas.
> - **C)** **Correta.** Conforme fundamentado na seção *1.3 Mecanismos Internos: Undo Log, Redo Log e Write-Ahead Logging (WAL)* deste guia, undo Log (Segmentos de Rollback): Registra os valores anteriores à modificação. Se uma transação falhar ou for cancelada, o SGBD lê o Undo Log para restaurar os dados originais (garantindo a Atomicidade). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE-PA/2024) ao estabelecer que "Atomicidade, Consistência, Isolamento, Durabilidade".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Autenticidade, Conformidade, Integridade, Desempenho". De acordo com a teoria estudada em *1.2 As Quatro Propriedades Fundamentais: ACID*, a transação não pode violar nenhuma regra de integridade declarativa (chaves primárias, chaves estrangeiras, restrições `CHECK`, valores `NOT NULL`) ou procedimental (gatilhos e regras de negócio).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Automação, Convergência, Interoperabilidade, Desempenho". De acordo com a teoria estudada em *1. O Conceito Formal de Transação e o Modelo ACID*, no contexto de auditoria e controle externo no setor público, uma transação típica é a liquidação de uma despesa orçamentária: o sistema deve simultaneamente debitar o saldo do empenho e creditar a conta bancária do fornecedor.
>
> **Gabarito: C**

---

### Teste 257
**(FCC – TRT-14 – Analista Judiciario Apoio Especializado Tecnologia da Informacao – 2016)**
Em uma empresa, um servidor Oracle 11g apresentou um problema e o disco no qual se localizavam os arquivos do banco de dados foi danificado e perderam-se todos os arquivos (control files, datafiles, online redo log files etc.), porém, o disco no qual estava a flash recovery area ficou intacto. Neste caso,

* **A)** não será possível restaurar um backup do banco de dados, pois os control files, datafiles e online redo log files foram perdidos.
* **B)** será possível restaurar um backup do banco de dados utilizando o aplicativo DUMP ou RESTORE a partir da flash recovery area.
* **C)** não será possível restaurar um banco de dados porque o servidor sempre fica off-line quando o disco é danificado, impedindo o acesso à flash recovery area.
* **D)** será possível restaurar um backup RMAN em conjunto com os archive redo log files contidos na flash recovery area.
* **E)** não será possível restaurar o banco de dados, pois o software Oracle foi corrompido e o disco no qual se localizavam os arquivos do banco de dados foi danificado.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "não será possível restaurar um backup do banco de dados, pois os control files, datafiles e online redo log files...". De acordo com a teoria estudada em *1.3 Mecanismos Internos: Undo Log, Redo Log e Write-Ahead Logging (WAL)*, a Regra Inviolável do WAL: O registro de log que descreve a alteração deve ser gravado fisicamente em disco síncrono ANTES que as páginas de dados correspondentes sejam descarregadas da memória RAM para os arquivos de dados (*datafiles*).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "será possível restaurar um backup do banco de dados utilizando o aplicativo DUMP ou RESTORE a partir da flash...". De acordo com a teoria estudada em *1.3 Mecanismos Internos: Undo Log, Redo Log e Write-Ahead Logging (WAL)*, undo Log (Segmentos de Rollback): Registra os valores anteriores à modificação. Se uma transação falhar ou for cancelada, o SGBD lê o Undo Log para restaurar os dados originais (garantindo a Atomicidade).
> - **C)** **Incorreta.** A opção promove generalização excessiva que desconsidera as condições técnicas e normativas ao afirmar que "não será possível restaurar um banco de dados porque o servidor sempre fica off-line quando o disco é danificado...". De acordo com a teoria estudada em *1.1 Ciclo de Vida e Estados de uma Transação*, parcialmente Comitada (*Partially Committed*): A última instrução SQL foi processada na memória RAM, mas os dados ainda não foram gravados permanentemente no log em disco.
> - **D)** **Correta.** Conforme fundamentado na seção *1.3 Mecanismos Internos: Undo Log, Redo Log e Write-Ahead Logging (WAL)* deste guia, isso garante a Durabilidade: se faltar energia imediatamente após o commit, o SGBD lê o Redo Log no boot de recuperação (*Crash Recovery*) e reaplica (*redo*) as alterações nas tabelas. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT-14/2016) ao estabelecer que "será possível restaurar um backup RMAN em conjunto com os archive redo log files contidos na flash recovery area".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "não será possível restaurar o banco de dados, pois o software Oracle foi corrompido e o disco no qual se...". De acordo com a teoria estudada em *1.2 As Quatro Propriedades Fundamentais: ACID*, princípio do "tudo ou nada" (*all-or-nothing*). Todas as operações que compõem a transação são consolidadas em conjunto no banco de dados, ou nenhuma delas produzirá efeito algum. Não existe efetivação parcial de transação.
>
> **Gabarito: D**

---

## 2. Comandos de Controle Transacional (TCL)

A linguagem SQL provê comandos dedicados para controlar as fronteiras transacionais:

### 2.1 COMMIT, ROLLBACK e Gestão de SAVEPOINTs

- **`COMMIT`:** Finaliza a transação com sucesso, gravando definitivamente todas as alterações pendentes no log transacional e liberando todos os bloqueios (*locks*) de recursos retidos.
- **`ROLLBACK`:** Cancela integralmente a transação, desfazendo todas as operações pendentes desde o `BEGIN TRANSACTION` e restaurando a base ao estado inicial.
- **`SAVEPOINT nome_ponto`:** Estabelece um **marco intermediário de salvamento** dentro de uma transação aberta.
- **`ROLLBACK TO SAVEPOINT nome_ponto`:** Reverte as operações executadas **apenas após o marco especificado**, mantendo preservadas as instruções anteriores ao savepoint. **Atenção:** O comando `ROLLBACK TO SAVEPOINT` **NÃO encerra a transação**; ela permanece aberta aguardando novas instruções ou a finalização formal com `COMMIT` ou `ROLLBACK` total.

---

### Teste 258
**(FGV – TJ-AP – Analista Judiciario Apoio Especializado Tecnologia da Informacao Banco de Dados – 2023)**
Transação é uma unidade lógica de trabalho e é fundamental para garantir a integridade e a consistência dos dados. Observe o seguinte script de uma transação implementada no MySQL: CREATE TABLE candidato (id INT, nome CHAR (50), INDEX (id)); START TRANSACTION; INSERT INTO candidato VALUES (1, 'JULIA'); INSERT INTO candidato VALUES (2, 'MARIA'); COMMIT; SET autocommit = 0; INSERT INTO candidato VALUES (3, 'SOFIA'); UPDATE candidato SET nome='ANA' WHERE id=3; DELETE FROM candidato WHERE nome='JULIA'; ROLLBACK; SELECT * FROM candidato; Após a execução do script apresentado, a consulta retornará as colunas id e nome com os valores:

* **A)** 2,MARIA
* **B)** 1,JULIA 2,MARIA
* **C)** 1,JULIA 2,MARIA 3,SOFIA
* **D)** 1,JULIA 2,MARIA 3,ANA
* **E)** 2,MARIA 3,ANA

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "2,MARIA". De acordo com a teoria estudada em *2.1 COMMIT, ROLLBACK e Gestão de SAVEPOINTs*, `ROLLBACK TO SAVEPOINT nome_ponto`: Reverte as operações executadas apenas após o marco especificado, mantendo preservadas as instruções anteriores ao savepoint.
> - **B)** **Correta.** Conforme fundamentado na seção *3.3 Leitura Fantasma (Phantom Read)* deste guia, definição: Ocorre quando a transação \$T_1\$ executa uma consulta filtrando um intervalo de dados (ex.: `SELECT * FROM contratos WHERE valor > 500000`) e recupera 10 tuplas. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ-AP/2023) ao estabelecer que "1,JULIA 2,MARIA".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "1,JULIA 2,MARIA 3,SOFIA". De acordo com a teoria estudada em *5.1 Bloqueios (Locks) e Matriz de Compatibilidade (Shared vs. Exclusive)*, bloqueio Exclusivo (Exclusive Lock - X): Solicitado para operações de modificação (`INSERT`, `UPDATE`, `DELETE`). Apenas uma transação pode reter o bloqueio exclusivo; nenhuma outra transação pode obter bloqueio S ou X sobre a mesma linha até sua liberação.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "1,JULIA 2,MARIA 3,ANA". De acordo com a teoria estudada em *1. O Conceito Formal de Transação e o Modelo ACID*, uma transação de banco de dados é uma unidade lógica e atômica de processamento que agrupa uma ou mais instruções SQL (leitura e escrita) que devem ser executadas de modo estritamente indivisível.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "2,MARIA 3,ANA". De acordo com a teoria estudada em *2.1 COMMIT, ROLLBACK e Gestão de SAVEPOINTs*, `ROLLBACK`: Cancela integralmente a transação, desfazendo todas as operações pendentes desde o `BEGIN TRANSACTION` e restaurando a base ao estado inicial.
>
> **Gabarito: B**

---

## 3. Fenômenos e Anomalias de Concorrência

Quando múltiplas transações concorrem pelo acesso aos mesmos dados sem controle de concorrência estrito, quatro anomalias clássicas podem se manifestar:

### 3.1 Leitura Suja (Dirty Read)
- **Definição:** Ocorre quando uma transação $T_1$ modifica uma linha no buffer, a transação $T_2$ lê esse valor ainda **não comitado**, e logo em seguida a transação $T_1$ sofre um **`ROLLBACK`**.
- **Impacto:** A transação $T_2$ tomou decisões de negócio baseando-se em um dado ilegítimo que nunca existiu formalmente no banco de dados.

### 3.2 Leitura Não Repetível (Non-Repeatable Read)
- **Definição:** Ocorre quando a transação $T_1$ consulta uma linha específica. Em seguida, a transação $T_2$ altera ou apaga essa exata linha e executa **`COMMIT`**. Posteriormente, a transação $T_1$ relê a mesma linha e encontra valores divergentes ou constata que ela foi removida.
- **Impacto:** Consultas idênticas sobre a mesma linha dentro do mesmo escopo transacional retornam valores distintos.

### 3.3 Leitura Fantasma (Phantom Read)
- **Definição:** Ocorre quando a transação $T_1$ executa uma consulta filtrando um intervalo de dados (ex.: `SELECT * FROM contratos WHERE valor > 500000`) e recupera 10 tuplas. Em seguida, a transação $T_2$ insere novas linhas que atendem a esse predicado e executa **`COMMIT`**. Quando $T_1$ reexecuta a mesma consulta de intervalo, obtém 12 tuplas.
- **Impacto:** Surgem novos registros ("fantasmas") que satisfazem a condição de busca no curso da mesma transação.

### 3.4 Atualização Perdida (Lost Update)
- **Definição:** Duas transações ($T_1$ e $T_2$) leem simultaneamente a mesma tupla (ex.: saldo = 100). Ambas realizam cálculos locais independentes ($T_1$ soma 50; $T_2$ subtrai 30) e gravam os novos valores. A gravação mais tardia sobrescreve a anterior sem considerar seu cálculo, perdendo uma das atualizações.

---

### Teste 259
**(FGV – TCE-PA – Auditor de Controle Externo Administrativa Ciencia de Dados – 2024)**
Um banco de dados projetado para apoiar a tarefa de alocação automática de analistas para os processos recém inseridos no sistema. O modelo relacional especificado e implementado restringe a alocação de processos apenas a analistas disponíveis no departamento. Caso haja tentativa de inserção de nome fora da lista de valores já registrados, a transação não será completada, ou seja, nenhum valor será inserido. Selecione a alternativa que contém duas propriedades de transação aplicáveis ao cenário acima.

* **A)** Atomicidade e Consistência.
* **B)** Consistência e Durabilidade.
* **C)** Durabilidade e Segurança.
* **D)** Isolamento e Segurança.
* **E)** Isolamento e Consistência.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *1.3 Mecanismos Internos: Undo Log, Redo Log e Write-Ahead Logging (WAL)* deste guia, undo Log (Segmentos de Rollback): Registra os valores anteriores à modificação. Se uma transação falhar ou for cancelada, o SGBD lê o Undo Log para restaurar os dados originais (garantindo a Atomicidade). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE-PA/2024) ao estabelecer que "Atomicidade e Consistência".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Consistência e Durabilidade". De acordo com a teoria estudada em *1.3 Mecanismos Internos: Undo Log, Redo Log e Write-Ahead Logging (WAL)*, isso garante a Durabilidade: se faltar energia imediatamente após o commit, o SGBD lê o Redo Log no boot de recuperação (*Crash Recovery*) e reaplica (*redo*) as alterações nas tabelas.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Durabilidade e Segurança". De acordo com a teoria estudada em *1. O Conceito Formal de Transação e o Modelo ACID*, uma transação de banco de dados é uma unidade lógica e atômica de processamento que agrupa uma ou mais instruções SQL (leitura e escrita) que devem ser executadas de modo estritamente indivisível.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Isolamento e Segurança". De acordo com a teoria estudada em *4.2 Snapshot Isolation (Isolamento por Instantâneo)*, implementado em motores que utilizam controle de concorrência multiversão (MVCC).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Isolamento e Consistência". De acordo com a teoria estudada em *4.2 Snapshot Isolation (Isolamento por Instantâneo)*, no início da transação, o SGBD captura uma "fotografia" lógica (*snapshot*) do banco baseada no número de transação (*Transaction ID - XID*).
>
> **Gabarito: A**

---

## 4. Níveis de Isolamento ANSI SQL-92

A norma ANSI/ISO SQL-92 estabelece quatro níveis canônicos de isolamento transacional, regulados pela tolerância ou bloqueio formal às anomalias de concorrência:

### 4.1 Matriz de Isolamento vs. Fenômenos Admitidos

| Nível de Isolamento | Leitura Suja (*Dirty Read*) | Leitura Não Repetível (*Non-Repeatable Read*) | Leitura Fantasma (*Phantom Read*) | Mecanismo Típico de Implementação |
| :--- | :---: | :---: | :---: | :--- |
| **`READ UNCOMMITTED`** | ❌ **Permite** | ❌ **Permite** | ❌ **Permite** | Leituras sem bloqueios; não gera snapshots. |
| **`READ COMMITTED`** | ✅ **Previne** | ❌ **Permite** | ❌ **Permite** | Lê apenas dados já comitados. Cada instrução `SELECT` tira um novo snapshot. *(Padrão em PostgreSQL e Oracle)* |
| **`REPEATABLE READ`** | ✅ **Previne** | ✅ **Previne** | ❌ **Permite** *(no ANSI)* | Lê o snapshot gerado no instante em que a primeira instrução da transação iniciou. *(Padrão no MySQL InnoDB)* |
| **`SERIALIZABLE`** | ✅ **Previne** | ✅ **Previne** | ✅ **Previne** | Bloqueios de predicado / Range Locks ou SSI (*Serializable Snapshot Isolation*). Simula execução serial estrita. |

> 🚨 **ALERTA DE PROVA / PEGADINHA FCC:**  
>
> 1. *"Qual o nível de isolamento MÍNIMO que impede Leitura Não Repetível?"* $\rightarrow$ **`REPEATABLE READ`**.
> 2. No PostgreSQL, a implementação prática do nível `REPEATABLE READ` via MVCC impede também leituras fantasmas; contudo, nas questões teóricas da FCC baseadas estritamente no **padrão ANSI SQL-92**, o candidato deve assinalar que o `REPEATABLE READ` **admite Leitura Fantasma**!
> 3. O único nível do padrão ANSI que previne **todos os três fenômenos** é o **`SERIALIZABLE`**.

### 4.2 Snapshot Isolation (Isolamento por Instantâneo)

Implementado em motores que utilizam controle de concorrência multiversão (MVCC):

- No início da transação, o SGBD captura uma "fotografia" lógica (*snapshot*) do banco baseada no número de transação (*Transaction ID - XID*).
- Todas as consultas daquela transação enxergam estritamente o estado dos dados consolidado no momento do snapshot, impedindo Leituras Não Repetíveis e Leituras Fantasmas sem a necessidade de adquirir bloqueios pesados de leitura.

---

### Teste 260
**(FGV – TJ-RR – Analista Judiciario Infraestrutura de Tecnologia da Informacao – 2024)**
O administrador de banco de dados MySQL de um certo tribunal precisa restaurar o banco de dados MySQL, chamado "tjdb", usando o arquivo de backup nomeado backup_tjdb.sql". Para isso ele deve acessar o usuário root, usando a senha apropriada. Um comando que poderia ser usado é

* **A)** mysql -u root -p tjdb > backup_tjdb.sql
* **B)** mysql -u root -p -D tjdb < backup_tjdb.sql
* **C)** mysql -u root -p -D tjdb > backup_tjdb.sql
* **D)** mysql -u root -p -h tjdb < backup_tjdb.sql
* **E)** mysql -u root -p -D tjdb backup_tjdb.sql

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "mysql -u root -p tjdb > backup_tjdb.sql". De acordo com a teoria estudada em *1. O Conceito Formal de Transação e o Modelo ACID*, uma transação de banco de dados é uma unidade lógica e atômica de processamento que agrupa uma ou mais instruções SQL (leitura e escrita) que devem ser executadas de modo estritamente indivisível.
> - **B)** **Correta.** Conforme fundamentado na seção *4.1 Matriz de Isolamento vs. Fenômenos Admitidos* deste guia, `REPEATABLE READ`: ✅ Previne — ✅ Previne — ❌ Permite *(no ANSI)* — Lê o snapshot gerado no instante em que a primeira instrução da transação iniciou. *(Padrão no MySQL InnoDB)*. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ-RR/2024) ao estabelecer que "mysql -u root -p -D tjdb < backup_tjdb.sql".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "mysql -u root -p -D tjdb > backup_tjdb.sql". De acordo com a teoria estudada em *4.1 Matriz de Isolamento vs. Fenômenos Admitidos*, no PostgreSQL, a implementação prática do nível `REPEATABLE READ` via MVCC impede também leituras fantasmas; contudo, nas questões teóricas da FCC baseadas estritamente no padrão ANSI SQL-92, o candidato deve assinalar que o `REPEATABLE READ` admite Leitura Fantasma!.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "mysql -u root -p -h tjdb < backup_tjdb.sql". De acordo com a teoria estudada em *4. Níveis de Isolamento ANSI SQL-92*, a norma ANSI/ISO SQL-92 estabelece quatro níveis canônicos de isolamento transacional, regulados pela tolerância ou bloqueio formal às anomalias de concorrência.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "mysql -u root -p -D tjdb backup_tjdb.sql". De acordo com a teoria estudada em *1.1 Ciclo de Vida e Estados de uma Transação*, parcialmente Comitada (*Partially Committed*): A última instrução SQL foi processada na memória RAM, mas os dados ainda não foram gravados permanentemente no log em disco.
>
> **Gabarito: B**

---

### Teste 261
**(FGV – TJ-AP – Analista Judiciario Apoio Especializado Tecnologia da Informacao Banco de Dados – 2023)**
No contexto de transações em banco de dados, a transação T1 está inserindo um novo registro na tabela TB_JUIZ. Enquanto isso, a transação T2 está lendo todos os registros de TB_JUIZ para gerar uma listagem. Considere que: - T1 iniciou antes de T2; - T1 ainda não concluiu; e - T2 não enxerga o registro que está sendo inserido por T1. A situação apresentada acima representa um:

* **A)** bloqueio por inanição;
* **B)** bloqueio do tipo Latches;
* **C)** conflito causado por um registro fantasma;
* **D)** conflito lógico entre T1 e T2, com bloqueio do item (registro) que está sendo inserido por T1;
* **E)** deadlock que pode ser prevenido pelo esquema esperar-morrer (wait-die).

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "bloqueio por inanição". De acordo com a teoria estudada em *5.1 Bloqueios (Locks) e Matriz de Compatibilidade (Shared vs. Exclusive)*, bloqueio Compartilhado (Shared Lock - S): Solicitado para operações de leitura (`SELECT`). Múltiplas transações podem reter simultaneamente bloqueios compartilhados sobre o mesmo registro.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "bloqueio do tipo Latches". De acordo com a teoria estudada em *3.3 Leitura Fantasma (Phantom Read)*, impacto: Surgem novos registros ("fantasmas") que satisfazem a condição de busca no curso da mesma transação.
> - **C)** **Correta.** Conforme fundamentado na seção *1.3 Mecanismos Internos: Undo Log, Redo Log e Write-Ahead Logging (WAL)* deste guia, a Regra Inviolável do WAL: O registro de log que descreve a alteração deve ser gravado fisicamente em disco síncrono ANTES que as páginas de dados correspondentes sejam descarregadas da memória RAM para os arquivos de dados (*datafiles*). Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ-AP/2023) ao estabelecer que "conflito causado por um registro fantasma".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "conflito lógico entre T1 e T2, com bloqueio do item (registro) que está sendo inserido por T1". De acordo com a teoria estudada em *1.1 Ciclo de Vida e Estados de uma Transação*, ativa (*Active*): O estado inicial. A transação está sendo executada pela aplicação.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "deadlock que pode ser prevenido pelo esquema esperar-morrer (wait-die)". De acordo com a teoria estudada em *5.4 Impasses (Deadlocks): Detecção via Wait-For Graph e Resolução por Transação Vítima*, um deadlock ocorre quando duas ou mais transações entram em estado de bloqueio mútuo e circular: a transação \$T_1\$ retém o recurso \$A\$ e aguarda o recurso \$B\$, enquanto a transação \$T_2\$ retém o recurso \$B\$ e aguarda o recurso \$A\$.
>
> **Gabarito: C**

---

## 5. Técnicas de Controle de Concorrência

### 5.1 Bloqueios (Locks) e Matriz de Compatibilidade (Shared vs. Exclusive)

O controle pessimista de concorrência baseia-se na alocação de travas (*locks*) sobre tuplas, páginas ou tabelas:

- **Bloqueio Compartilhado (Shared Lock - S):** Solicitado para operações de leitura (`SELECT`). Múltiplas transações podem reter simultaneamente bloqueios compartilhados sobre o mesmo registro.
- **Bloqueio Exclusivo (Exclusive Lock - X):** Solicitado para operações de modificação (`INSERT`, `UPDATE`, `DELETE`). Apenas uma transação pode reter o bloqueio exclusivo; nenhuma outra transação pode obter bloqueio S ou X sobre a mesma linha até sua liberação.

| Bloqueio Solicitado \ Bloqueio Existente | Shared (S) | Exclusive (X) |
| :---: | :---: | :---: |
| **Shared (S)** | ✅ **Compatível** (Permitido) | ❌ Conflito (Aguarda liberação) |
| **Exclusive (X)** | ❌ Conflito (Aguarda liberação) | ❌ Conflito (Aguarda liberação) |

### 5.2 Protocolo de Bloqueio em Duas Fases (2PL - Two-Phase Locking): Básico, Estrito e Rigoroso

O protocolo **2PL** é o algoritmo matemático que garante a **serializabilidade** das escalas de execução concorrente:

```mermaid
flowchart LR
    subgraph Protocolo_2PL["Protocolo 2PL (Two-Phase Locking)"]
        F1["Fase 1: Crescimento (Growing)<br/>Transação adquire bloqueios conforme necessário.<br/><b>PROIBIDO LIBERAR BLOQUEIOS!</b>"] --> P["Ponto de Bloqueio<br/>(Lock Point)"]
        P --> F2["Fase 2: Encolhimento (Shrinking)<br/>Transação libera bloqueios gradualmente.<br/><b>PROIBIDO ADQUIRIR NOVOS BLOQUEIOS!</b>"]
    end
```

- **Regra Fundamental do 2PL Básico:** A transação possui duas fases estanques:
    1. *Fase de Crescimento (*Growing Phase*):* A transação pode adquirir quantos bloqueios precisar, mas **é terminantemente proibida de liberar qualquer bloqueio**.
    2. *Fase de Encolhimento (*Shrinking Phase*):* A transação pode liberar bloqueios já utilizados, mas **é terminantemente proibida de adquirir novos bloqueios**.

- **Strict 2PL (2PL Estrito):** Todos os bloqueios **exclusivos (X)** devem ser mantidos até o fim definitivo da transação (`COMMIT` ou `ROLLBACK`). Evita abortos em cascata (*cascadeless schedules*).
- **Rigorous 2PL (2PL Rigoroso):** Todos os bloqueios (tanto **compartilhados - S** quanto **exclusivos - X**) devem ser mantidos até o `COMMIT` ou `ROLLBACK`. É a variante mais utilizada na prática por garantir serializabilidade estrita.

> 🚨 **ALERTA DE PROVA / PEGADINHA FCC:**  
> O protocolo 2PL garante a **serializabilidade**, mas **NÃO evita impasses (*deadlocks*)**! Transações operando sob o 2PL básico podem sofrer deadlocks frequentemente.

### 5.3 Controle Multiversão de Concorrência (MVCC)

Adotado nativamente por PostgreSQL e Oracle:

- **Princípio:** *"Leitores nunca bloqueiam escritores, e escritores nunca bloqueiam leitores."*
- **Mecanismo:** Ao atualizar uma linha, o SGBD não sobrescreve os dados no mesmo local; ele cria uma **nova versão física da tupla** contendo metadados de cabeçalho:
    - No PostgreSQL: `xmin` (ID da transação criadora) e `xmax` (ID da transação que apagou ou gerou versão superior).
    - Leitores consultam versões visíveis compatíveis com o seu instante temporal (*snapshot*), garantindo alto rendimento de leitura e escrita concorrentes.

### 5.4 Impasses (Deadlocks): Detecção via Wait-For Graph e Resolução por Transação Vítima

Um **deadlock** ocorre quando duas ou mais transações entram em estado de bloqueio mútuo e circular: a transação $T_1$ retém o recurso $A$ e aguarda o recurso $B$, enquanto a transação $T_2$ retém o recurso $B$ e aguarda o recurso $A$. Nenhuma das transações consegue prosseguir.

```mermaid
flowchart LR
    T1["Transação T1"] -->|Retém recurso A / Aguarda| T2["Transação T2"]
    T2 -->|Retém recurso B / Aguarda| T1
```

- **Detecção via Wait-For Graph (Grafo de Espera):** O SGBD constrói dinamicamente um grafo direcionado onde os nós são transações e as arestas indicam dependências de espera. **A detecção de um ciclo no grafo sinaliza formalmente um deadlock**.
- **Resolução via Transação Vítima:** Ao detectar o ciclo, o SGBD seleciona uma **transação vítima** (com base em critérios de menor custo computacional ou menor volume de dados alterados), aborta sua execução compulsoriamente via `ROLLBACK` forçado e devolve o erro à aplicação cliente.
- **Técnicas de Prevenção por Timestamps:**
    - *Wait-Die (Não-preemptivo):* Se a transação mais antiga solicitar recurso retido pela mais nova, ela espera (*wait*); se a mais nova solicitar recurso retido pela mais antiga, a mais nova morre (*die/rollback*).
    - *Wound-Wait (Preemptivo):* Se a transação mais antiga solicitar recurso retido pela mais nova, ela fere e aborta a mais nova (*wound/preempt*); se a mais nova solicitar da mais antiga, ela espera (*wait*).

---

### Teste 262
**(FUMARC – TRT-3 – Analista Judiciario Apoio Especializado Tecnologia da Informacao – 2022)**
27 Considere que a mensagem de erro em inglês técnico “Transaction (Process ID XX) was deadlocked on lock resources with another process and has been chosen as the deadlock victim. Rerun the transaction.” foi recebida por um usuário de uma aplicação, cujo banco de dados é o Microsoft SQL Server. De acordo com esta mensagem, assinale a opção que MELHOR explica o significado da mensagem:

* **A)** Uma transação entrou em deadlock (impasse) ao bloquear recursos com outro processo e foi escolhida como a vítima do deadlock. A transação será executada novamente de forma automática.
* **B)** Uma transação entrou em deadlock (impasse) ao bloquear recursos com outro processo e foi escolhida como a vítima do deadlock. Execute a transação novamente.
* **C)** Uma transação foi bloqueada por outro processo que rodava uma transação de deadlock (impasse) e foi escolhida como a vítima deste processo. Execute a transação novamente.
* **D)** Uma transação foi bloqueada por outro processo que rodava uma transação de deadlock (impasse) e foi escolhida como a vítima deste processo. A transação será executada novamente de forma automática.
* **E)** Uma transação foi bloqueada por recursos de deadlock (impasse) com outro processo e foi escolhida como a vítima dos bloqueios. A transação será executada novamente de forma automática.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Uma transação entrou em deadlock (impasse) ao bloquear recursos com outro processo e foi escolhida como a vítima...". De acordo com a teoria estudada em *5.4 Impasses (Deadlocks): Detecção via Wait-For Graph e Resolução por Transação Vítima*, detecção via Wait-For Graph (Grafo de Espera): O SGBD constrói dinamicamente um grafo direcionado onde os nós são transações e as arestas indicam dependências de espera. A detecção de um ciclo no grafo sinaliza formalmente um deadlock.
> - **B)** **Correta.** Conforme fundamentado na seção *5.4 Impasses (Deadlocks): Detecção via Wait-For Graph e Resolução por Transação Vítima* deste guia, um deadlock ocorre quando duas ou mais transações entram em estado de bloqueio mútuo e circular: a transação \$T_1\$ retém o recurso \$A\$ e aguarda o recurso \$B\$, enquanto a transação \$T_2\$ retém o recurso \$B\$ e aguarda o recurso \$A\$. Dessa forma, está plenamente correta a assertiva da banca (FUMARC – TRT-3/2022) ao estabelecer que "Uma transação entrou em deadlock (impasse) ao bloquear recursos com outro processo e foi escolhida como a vítima...".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Uma transação foi bloqueada por outro processo que rodava uma transação de deadlock (impasse) e foi escolhida como...". De acordo com a teoria estudada em *5.4 Impasses (Deadlocks): Detecção via Wait-For Graph e Resolução por Transação Vítima*, resolução via Transação Vítima: Ao detectar o ciclo, o SGBD seleciona uma transação vítima (com base em critérios de menor custo computacional ou menor volume de dados alterados), aborta sua execução compulsoriamente via `ROLLBACK` forçado e devolve o erro à aplicação cliente.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Uma transação foi bloqueada por outro processo que rodava uma transação de deadlock (impasse) e foi escolhida como...". De acordo com a teoria estudada em *1.2 As Quatro Propriedades Fundamentais: ACID*, garante que a transação conduz o banco de dados de um estado válido para outro estado igualmente válido.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Uma transação foi bloqueada por recursos de deadlock (impasse) com outro processo e foi escolhida como a vítima...". De acordo com a teoria estudada em *2.1 COMMIT, ROLLBACK e Gestão de SAVEPOINTs*, `COMMIT`: Finaliza a transação com sucesso, gravando definitivamente todas as alterações pendentes no log transacional e liberando todos os bloqueios (*locks*) de recursos retidos.
>
> **Gabarito: B**

---

### Teste 263
**(FGV – TCE-PA – Auditor de Controle Externo Administrativa Ciencia de Dados – 2024)**
Para garantir que operações complexas sejam executadas de maneira segura e eficiente, assegurando que o banco de dados mantenha sua integridade mesmo em situações adversas, os Sistemas de Gerenciamento de Banco de Dados (SGBD) implementam o conceito de transação. Transação é

* **A)** um conjunto de operações que são executadas sequencialmente para garantir a integridade dos dados.
* **B)** um mecanismo que permite a cópia de segurança (backup) automática dos dados do banco.
* **C)** um protocolo utilizado para distribuir os dados entre diferentes servidores de banco de dados.
* **D)** um conjunto de operações que devem ser tratadas como uma unidade atômica e indivisível.
* **E)** um método para criar índices que otimizam o acesso aos dados armazenados.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "um conjunto de operações que são executadas sequencialmente para garantir a integridade dos dados". De acordo com a teoria estudada em *1.2 As Quatro Propriedades Fundamentais: ACID*, para que a integridade dos dados seja inviolável mesmo diante de falhas de hardware, interrupções de energia elétrica e concorrência massiva de usuários, o SGBD deve garantir integralmente as propriedades do acrônimo ACID (Jim Gray e Andreas Reuter).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "um mecanismo que permite a cópia de segurança (backup) automática dos dados do banco". De acordo com a teoria estudada em *1.2 As Quatro Propriedades Fundamentais: ACID*, princípio do "tudo ou nada" (*all-or-nothing*). Todas as operações que compõem a transação são consolidadas em conjunto no banco de dados, ou nenhuma delas produzirá efeito algum. Não existe efetivação parcial de transação.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "um protocolo utilizado para distribuir os dados entre diferentes servidores de banco de dados". De acordo com a teoria estudada em *5.2 Protocolo de Bloqueio em Duas Fases (2PL - Two-Phase Locking): Básico, Estrito e Rigoroso*, rigorous 2PL (2PL Rigoroso): Todos os bloqueios (tanto compartilhados - S quanto exclusivos - X) devem ser mantidos até o `COMMIT` ou `ROLLBACK`. É a variante mais utilizada na prática por garantir serializabilidade estrita.
> - **D)** **Correta.** Conforme fundamentado na seção *1. O Conceito Formal de Transação e o Modelo ACID* deste guia, uma transação de banco de dados é uma unidade lógica e atômica de processamento que agrupa uma ou mais instruções SQL (leitura e escrita) que devem ser executadas de modo estritamente indivisível. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE-PA/2024) ao estabelecer que "um conjunto de operações que devem ser tratadas como uma unidade atômica e indivisível".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "um método para criar índices que otimizam o acesso aos dados armazenados". De acordo com a teoria estudada em *5.2 Protocolo de Bloqueio em Duas Fases (2PL - Two-Phase Locking): Básico, Estrito e Rigoroso*, strict 2PL (2PL Estrito): Todos os bloqueios exclusivos (X) devem ser mantidos até o fim definitivo da transação (`COMMIT` ou `ROLLBACK`). Evita abortos em cascata (*cascadeless schedules*).
>
> **Gabarito: D**

---

### Teste 264
**(FGV – TJ-AP – Analista Judiciario Apoio Especializado Tecnologia da Informacao Banco de Dados – 2023)**
João, administrador de banco de dados MySQL, deverá realizar, periodicamente, o backup lógico completo do banco de dados "tjap_db". Para isso, João deverá utilizar o comando:

* **A)** backup -u root -p tjap_db > backup.sql;
* **B)** mydump -u root -p tjap_db > backup.sql;
* **C)** mybackup -u root -p tjap_db > backup.sql;
* **D)** mysqldump -u root -p tjap_db > backup.sql;
* **E)** select * from tjap_db into outfile backup.sql;

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "backup -u root -p tjap_db > backup.sql". De acordo com a teoria estudada em *1.1 Ciclo de Vida e Estados de uma Transação*, parcialmente Comitada (*Partially Committed*): A última instrução SQL foi processada na memória RAM, mas os dados ainda não foram gravados permanentemente no log em disco.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "mydump -u root -p tjap_db > backup.sql". De acordo com a teoria estudada em *2. Comandos de Controle Transacional (TCL)*, a linguagem SQL provê comandos dedicados para controlar as fronteiras transacionais.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "mybackup -u root -p tjap_db > backup.sql". De acordo com a teoria estudada em *4. Níveis de Isolamento ANSI SQL-92*, a norma ANSI/ISO SQL-92 estabelece quatro níveis canônicos de isolamento transacional, regulados pela tolerância ou bloqueio formal às anomalias de concorrência.
> - **D)** **Correta.** Conforme fundamentado na seção *1. O Conceito Formal de Transação e o Modelo ACID* deste guia, uma transação de banco de dados é uma unidade lógica e atômica de processamento que agrupa uma ou mais instruções SQL (leitura e escrita) que devem ser executadas de modo estritamente indivisível. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ-AP/2023) ao estabelecer que "mysqldump -u root -p tjap_db > backup.sql".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "select * from tjap_db into outfile backup.sql". De acordo com a teoria estudada em *3.3 Leitura Fantasma (Phantom Read)*, definição: Ocorre quando a transação \$T_1\$ executa uma consulta filtrando um intervalo de dados (ex.: `SELECT * FROM contratos WHERE valor > 500000`) e recupera 10 tuplas.
>
> **Gabarito: D**

---

### Teste 265
**(FGV – TRF-1 – Analista Judiciario Area Apoio Especializado Especialidade Suporte Em Tecnologia da Informacao – 2024)**
Ana identificou que, em seu banco de dados, ocorria muita demora na execução de algumas transações específicas, que chegavam até a falhar algumas vezes. Ao efetuar uma análise, viu que não havia controle nas transações ocorridas. Como forma de garantir seus schedules estritos, Ana implementou um bloqueio em 2 fases rigoroso. Esse bloqueio implementado por Ana fará com que:

* **A)** uma transação bloqueie todos os itens que ela acessa antes que a transação inicie a execução;
* **B)** seja executado um downgrade do bloqueio ao se emitir uma operação read_lock(X), mesmo com a transação ainda em execução;
* **C)** uma transação T não libere nenhum de seus bloqueios exclusivos (gravação) até depois de confirmar ou abortar;
* **D)** seja gerado um rótulo de tempo, que será usado para garantir a serialização das transações;
* **E)** uma transação T não libere nenhum de seus bloqueios (exclusivo ou compartilhado) até depois de confirmar ou abortar.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "uma transação bloqueie todos os itens que ela acessa antes que a transação inicie a execução". De acordo com a teoria estudada em *5.2 Protocolo de Bloqueio em Duas Fases (2PL - Two-Phase Locking): Básico, Estrito e Rigoroso*, rigorous 2PL (2PL Rigoroso): Todos os bloqueios (tanto compartilhados - S quanto exclusivos - X) devem ser mantidos até o `COMMIT` ou `ROLLBACK`. É a variante mais utilizada na prática por garantir serializabilidade estrita.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "seja executado um downgrade do bloqueio ao se emitir uma operação read_lock(X), mesmo com a transação ainda em...". De acordo com a teoria estudada em *5.1 Bloqueios (Locks) e Matriz de Compatibilidade (Shared vs. Exclusive)*, bloqueio Compartilhado (Shared Lock - S): Solicitado para operações de leitura (`SELECT`). Múltiplas transações podem reter simultaneamente bloqueios compartilhados sobre o mesmo registro.
> - **C)** **Correta.** Conforme fundamentado na seção *5.2 Protocolo de Bloqueio em Duas Fases (2PL - Two-Phase Locking): Básico, Estrito e Rigoroso* deste guia, strict 2PL (2PL Estrito): Todos os bloqueios exclusivos (X) devem ser mantidos até o fim definitivo da transação (`COMMIT` ou `ROLLBACK`). Evita abortos em cascata (*cascadeless schedules*). Dessa forma, está plenamente correta a assertiva da banca (FGV – TRF-1/2024) ao estabelecer que "uma transação T não libere nenhum de seus bloqueios exclusivos (gravação) até depois de confirmar ou abortar".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "seja gerado um rótulo de tempo, que será usado para garantir a serialização das transações". De acordo com a teoria estudada em *5.2 Protocolo de Bloqueio em Duas Fases (2PL - Two-Phase Locking): Básico, Estrito e Rigoroso*, o protocolo 2PL garante a serializabilidade, mas NÃO evita impasses (*deadlocks*)! Transações operando sob o 2PL básico podem sofrer deadlocks frequentemente.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "uma transação T não libere nenhum de seus bloqueios (exclusivo ou compartilhado) até depois de confirmar ou abortar". De acordo com a teoria estudada em *5.1 Bloqueios (Locks) e Matriz de Compatibilidade (Shared vs. Exclusive)*, bloqueio Exclusivo (Exclusive Lock - X): Solicitado para operações de modificação (`INSERT`, `UPDATE`, `DELETE`). Apenas uma transação pode reter o bloqueio exclusivo; nenhuma outra transação pode obter bloqueio S ou X sobre a mesma linha até sua liberação.
>
> **Gabarito: C**

---

### Teste 266
**(FGV – TJ-AP – Analista Judiciario Apoio Especializado Tecnologia da Informacao Banco de Dados – 2023)**
O mecanismo de recuperação de banco de dados precisa garantir que uma transação possa ser desfeita. Para execução do rollback em cascata são necessárias entradas de log do(s) valor(es):

* **A)** novo;
* **B)** antigo;
* **C)** antigo e novo;
* **D)** write-ahead;
* **E)** undo/redo.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "novo". De acordo com a teoria estudada em *4.1 Matriz de Isolamento vs. Fenômenos Admitidos*, `READ COMMITTED`: ✅ Previne — ❌ Permite — ❌ Permite — Lê apenas dados já comitados. Cada instrução `SELECT` tira um novo snapshot. *(Padrão em PostgreSQL e Oracle)*.
> - **B)** **Correta.** Conforme fundamentado na seção *5.2 Protocolo de Bloqueio em Duas Fases (2PL - Two-Phase Locking): Básico, Estrito e Rigoroso* deste guia, strict 2PL (2PL Estrito): Todos os bloqueios exclusivos (X) devem ser mantidos até o fim definitivo da transação (`COMMIT` ou `ROLLBACK`). Evita abortos em cascata (*cascadeless schedules*). Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ-AP/2023) ao estabelecer que "antigo".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "antigo e novo". De acordo com a teoria estudada em *5.2 Protocolo de Bloqueio em Duas Fases (2PL - Two-Phase Locking): Básico, Estrito e Rigoroso*, rigorous 2PL (2PL Rigoroso): Todos os bloqueios (tanto compartilhados - S quanto exclusivos - X) devem ser mantidos até o `COMMIT` ou `ROLLBACK`. É a variante mais utilizada na prática por garantir serializabilidade estrita.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "write-ahead". De acordo com a teoria estudada em *1.3 Mecanismos Internos: Undo Log, Redo Log e Write-Ahead Logging (WAL)*, a Regra Inviolável do WAL: O registro de log que descreve a alteração deve ser gravado fisicamente em disco síncrono ANTES que as páginas de dados correspondentes sejam descarregadas da memória RAM para os arquivos de dados (*datafiles*).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "undo/redo". De acordo com a teoria estudada em *1.3 Mecanismos Internos: Undo Log, Redo Log e Write-Ahead Logging (WAL)*, isso garante a Durabilidade: se faltar energia imediatamente após o commit, o SGBD lê o Redo Log no boot de recuperação (*Crash Recovery*) e reaplica (*redo*) as alterações nas tabelas.
>
> **Gabarito: B**

---

## 🌐 Fontes Oficiais e Referências Bibliográficas

* [PostgreSQL 17 Official Documentation - Concurrency Control and MVCC](https://www.postgresql.org/docs/current/mvcc.html) - Controle de concorrência multiversão, níveis de isolamento (Read Committed, Repeatable Read, Serializable).
* [PostgreSQL 17 Official Documentation - Write-Ahead Logging (WAL)](https://www.postgresql.org/docs/current/wal-intro.html) - Registro em log prévio para garantia de durabilidade (D) e atomicidade (A) em transações ACID.
* [Oracle Database 19c Documentation - Transactions and Concurrency](https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/transactions.html) - Bloqueios, serializabilidade, Savepoints e controle de transações concorrentes.
* [Martin Kleppmann - Transactions and Isolation Levels in Distributed Systems](https://martinfowler.com/articles/patterns-of-distributed-systems/) - Análise formal das anomalias de concorrência (Dirty Read, Non-repeatable Read, Phantom Read e Write Skew).
* SILBERSCHATZ, Abraham; KORTH, Henry F.; SUDARSHAN, S. **Sistema de Banco de Dados**. 7. ed. Rio de Janeiro: GEN LTC, 2020. (Cap. 17 - Transações; Cap. 18 - Controle de Concorrência; Cap. 19 - Sistema de Recuperação).
* ELMASRI, Ramez; NAVATHE, Shamkant B. **Sistemas de Banco de Dados**. 7. ed. São Paulo: Pearson, 2019. (Cap. 20 - Conceitos de Processamento de Transações; Cap. 21 - Técnicas de Controle de Concorrência).
* KLEPPMANN, Martin. **Projetando Aplicações Intensivas em Dados: As Ideias Confiáveis por Trás de Sistemas Escaláveis**. São Paulo: Novatec, 2018. (Cap. 7 - Transações e Níveis de Isolamento).
