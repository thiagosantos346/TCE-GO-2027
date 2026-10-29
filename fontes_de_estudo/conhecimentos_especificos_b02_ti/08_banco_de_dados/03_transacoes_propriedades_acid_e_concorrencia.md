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
**(FGV - TJ-AP / Analista Judiciário - Banco de Dados - Estados do Ciclo de Vida de uma Transação)**
Segundo a teoria clássica de sistemas de bancos de dados relacionais formulada por Silberschatz, Korth e Sudarshan, uma transação deve atravessar uma máquina de estados finitos bem definida durante a sua execução.

A respeito dos estados possíveis de uma transação e das transições entre eles, assinale a afirmativa correta:

* **A)** Uma transação entra no estado *Committed* (Efetivada) imediatamente após a emissão da primeira instrução DML de escrita no buffer de memória.
* **B)** O estado *Partially Committed* (Parcialmente Efetivada) ocorre após a execução da última declaração SQL da transação, mas antes que as modificações e seus registros de log correspondentes tenham sido completamente gravados de forma persistente em disco (disco estável).
* **C)** Uma transação em estado *Failed* (Falha) transita compulsoriamente de volta para o estado *Active* (Ativa) para tentar novamente a operação a partir do ponto onde ocorreu a falha considerando os requisitos operacionais de segurança, escalabilidade, auditoria e desempenho corporativo.
* **D)** O estado *Aborted* (Abortada) indica que a transação concluiu seu processamento com êxito e que seus resultados tornaram-se permanentes no banco de dados.
* **E)** Toda transação no estado *Active* pode transitar diretamente para o estado *Committed* sem necessidade de passar pelo estado *Partially Committed*.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Uma transação no início de suas instruções está no estado *Active* (Ativa), jamais *Committed*.
> - **B)** **CORRETA.** No modelo formal de estados de transação:
>   1. **Active (Ativa):** O estado inicial enquanto as operações da transação estão em execução.
>   2. **Partially Committed (Parcialmente Efetivada):** Alcançado quando a última instrução da transação foi executada na memória, porém antes da garantia de que o log de transações (WAL) foi descarregado no armazenamento não-volátil (disco estável).
>   3. **Failed (Falha):** Se uma verificação normal de integridade falhar ou se houver pane de hardware/software durante a execução.
>   4. **Aborted (Abortada):** Ocorre após a transação em falha sofrer *rollback* e o banco de dados ser restaurado ao estado anterior.
>   5. **Committed (Efetivada):** Alcançado somente após a conclusão com sucesso de todas as gravações no disco estável.
> - **C)** Incorreta. Do estado *Failed*, a única transição válida é para o estado *Aborted*, após as operações de desfazimento (*undo*).
> - **D)** Incorreta. *Aborted* significa que a transação foi revertida e cancelada.
> - **E)** Incorreta. Pelo diagrama canônico, a transição para *Committed* passa obrigatoriamente por *Partially Committed*.
> 
> **Gabarito: B**

---

### Teste 257
**(FCC - Adaptada / TI - As Quatro Propriedades ACID e Logs)**
Em um SGBD corporativo, um desligamento repentino do fornecimento de energia elétrica interrompeu as operações enquanto dezenas de transações eram processadas. Durante a rotina de inicialização automática (Crash Recovery), o SGBD utilizou seus arquivos de log transacional para restaurar a consistência da base.

Sobre os mecanismos que asseguram as propriedades ACID nesse cenário, assinale a afirmativa correta:  

* **A)** A Atomicidade foi mantida pelo subsistema de recuperação que aplicou as operações de REDO para desfazer as alterações de transações que não haviam comitado no momento da queda.
* **B)** A Durabilidade assegura que todas as transações que receberam a confirmação de `COMMIT` antes da interrupção elétrica sejam reaplicadas a partir dos arquivos de log (REDO/WAL), caso suas páginas ainda estivessem apenas na memória RAM.
* **C)** A Consistência é a propriedade responsável por garantir que as transações concorrentes não interfiram entre si, mesmo que os dados não estejam totalmente gravados em disco.
* **D)** A Atomicidade autoriza que, em caso de pane catastrófica, parte das instruções de uma transação crítica permaneça gravada para evitar retrabalho da aplicação cliente.
* **E)** O mecanismo de Write-Ahead Logging (WAL) determina que as páginas de dados sejam obrigatoriamente persistidas nas tabelas físicas do disco antes que o registro transacional seja gravado no log no âmbito da administração pública direta e indireta.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Desfazer operações de transações não comitadas é responsabilidade do log de **UNDO**. O REDO reaplica transações comitadas.
> - **B)** Correta. A **Durabilidade** garante que transações comitadas persistam mesmo que os dados estivessem voláteis na memória RAM durante a queda. No processo de recuperação, o SGBD lê o Redo Log / WAL e reaplica as alterações comitadas na base de dados.
> - **C)** Incorreta. O impedimento de interferência entre transações concorrentes é atribuição da propriedade de **Isolamento** (I do ACID).
> - **D)** Incorreta. A Atomicidade obedece ao princípio estrito do "tudo ou nada", proibindo a persistência parcial de transações.
> - **E)** Incorreta. O princípio do WAL (*Write-Ahead Logging*) estipula exatamente o inverso: o registro de log deve ser gravado em disco **antes** que as páginas de dados modificadas sejam gravadas nas tabelas físicas.
> 
> **Gabarito: B**

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
**(FCC - Adaptada / TI - Controle de Transações: SAVEPOINT e ROLLBACK TO)**
Considere a sequência de comandos executada em uma única sessão transacional em um SGBD em conformidade com o padrão ANSI SQL:

```sql
BEGIN TRANSACTION;
  INSERT INTO fornecedores (id, nome) VALUES (1, 'Fornecedor Alfa');
  SAVEPOINT ponto_1;
  INSERT INTO fornecedores (id, nome) VALUES (2, 'Fornecedor Beta');
  SAVEPOINT ponto_2;
  INSERT INTO fornecedores (id, nome) VALUES (3, 'Fornecedor Gama');
  ROLLBACK TO SAVEPOINT ponto_1;
  INSERT INTO fornecedores (id, nome) VALUES (4, 'Fornecedor Delta');
COMMIT;
```

Considerando que a tabela `fornecedores` encontrava-se vazia antes do início do bloco transacional e que nenhuma instrução apresentou erro de restrição de integridade, quais registros constarão na tabela após o término da execução?  

* **A)** Fornecedor Alfa, Fornecedor Beta, Fornecedor Gama e Fornecedor Delta.
* **B)** Fornecedor Alfa e Fornecedor Delta apenas.
* **C)** Fornecedor Delta apenas.
* **D)** Fornecedor Alfa, Fornecedor Beta e Fornecedor Delta.
* **E)** Nenhum registro, pois o comando `ROLLBACK TO SAVEPOINT` desfaz a transação inteira e aborta o bloco.


---

> **Comentário Detalhado:**
>
> - **A) Incorreta.** Ignora o comando de reversão parcial `ROLLBACK TO SAVEPOINT ponto_1`, que cancelou as linhas 2 e 3.
> - **B) CORRETA.** O comando `ROLLBACK TO SAVEPOINT ponto_1` desfaz as operações executadas posteriormente a esse marco ('Fornecedor Beta' e 'Fornecedor Gama'), mantendo válido o 'Fornecedor Alfa'. Com a inserção subsequente de 'Fornecedor Delta' e o `COMMIT`, apenas Alfa e Delta são gravados.
> - **C) Incorreta.** O 'Fornecedor Alfa' foi inserido antes do `SAVEPOINT ponto_1` e não sofreu os efeitos do rollback.
> - **D) Incorreta.** O 'Fornecedor Beta' foi sumariamente revertido ao retornar ao ponto de salvamento 1.
> - **E) Incorreta.** O rollback para savepoint não aborta a transação e nem limpa os comandos executados antes do savepoint.
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
**(FGV - TJ-AP / Analista Judiciário - Banco de Dados - Anomalias e Fenômenos de Concorrência)**
Em sistemas gerenciadores de bancos de dados com processamento transacional concorrente de alta intensidade, a ausência de mecanismos rigorosos de controle de concorrência expõe a base de dados a múltiplos fenômenos anômalos.

Analise as três situações de concorrência descritas a seguir entre duas transações $T_1$ e $T_2$:

1. $T_1$ lê um saldo bancário de R$ 10.000,00. Simultaneamente, $T_2$ altera esse saldo para R$ 15.000,00 e efetiva a operação com `COMMIT`. Em seguida, $T_1$ relê o mesmo registro na mesma transação e encontra o saldo de R$ 15.000,00.  
2. $T_1$ executa uma consulta que recupera todos os contratos com valor acima de R$ 1.000.000,00, obtendo 5 registros. Nesse intervalo, $T_2$ insere um novo contrato no valor de R$ 2.000.000,00 e efetiva com `COMMIT`. $T_1$ reexecuta a mesma consulta e agora obtém 6 registros.  
3. $T_1$ lê o valor de um empenho de R$ 50.000,00 e $T_2$ lê o mesmo valor. $T_1$ atualiza o valor para R$ 55.000,00 e efetiva. Logo depois, $T_2$, baseando-se no valor inicial lido, atualiza o valor para R$ 48.000,00 e efetiva, sobrescrevendo cegamente a alteração de $T_1$.  

Esses três fenômenos caracterizam, rigorosa e respectivamente:

* **A)** Leitura Suja (*Dirty Read*), Leitura Fantasma (*Phantom Read*) e Leitura Não Repetível (*Non-Repeatable Read*).
* **B)** Leitura Não Repetível (*Non-Repeatable Read*), Leitura Fantasma (*Phantom Read*) e Atualização Perdida (*Lost Update*).
* **C)** Leitura Fantasma (*Phantom Read*), Leitura Suja (*Dirty Read*) e Desvio de Gravação (*Write Skew*).
* **D)** Leitura Suja (*Dirty Read*), Atualização Perdida (*Lost Update*) e Leitura Não Repetível (*Non-Repeatable Read*) no âmbito da administração pública direta e indireta.
* **E)** Leitura Não Repetível (*Non-Repeatable Read*), Atualização Perdida (*Lost Update*) e Leitura Suja (*Dirty Read*).


---

> **Comentário Detalhado:**
>
> - **Situação 1:** Trata-se de **Leitura Não Repetível (Non-Repeatable Read ou Fuzzy Read)**: ocorre quando uma transação relê a mesma linha e encontra valores de colunas alterados porque outra transação efetuou `UPDATE` e `COMMIT` no intervalo.
> - **Situação 2:** Trata-se de **Leitura Fantasma (Phantom Read)**: ocorre quando uma transação reexecuta uma consulta baseada em predicado/faixa e o conjunto de linhas resultante se altera devido a `INSERT` ou `DELETE` efetuado e confirmado por outra transação.
> - **Situação 3:** Trata-se de **Atualização Perdida (Lost Update)**: ocorre quando duas transações leem o mesmo registro e ambas tentam atualizá-lo em paralelo; a última gravação sobrescreve a primeira sem considerar a alteração anterior, perdendo-se os dados da primeira atualização.
> 
> **Gabarito: B**

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
**(FCC - Adaptada / TI - Níveis de Isolamento Transacional ANSI SQL)**
Em um sistema de arrecadação tributária estadual, duas transações concorrentes ($T_1$ e $T_2$) executam operações sobre a mesma tabela de contribuintes. A transação $T_1$ realiza a leitura de um registro de débitos fiscais. Em seguida, a transação $T_2$ altera o valor desse débito e efetiva a operação com `COMMIT`. Posteriormente, ainda dentro do seu escopo, a transação $T_1$ relê o mesmo registro e encontra o novo valor alterado e comitado por $T_2$.

Considerando os fenômenos de concorrência e os níveis de isolamento padronizados pela norma ANSI SQL:  

* **A)** O fenômeno observado é classificado como *Leitura Suja* (*Dirty Read*), e ocorre quando o nível de isolamento está configurado como `SERIALIZABLE`.
* **B)** O fenômeno observado é classificado como *Leitura Não Repetível* (*Non-Repeatable Read*), e para impedi-lo o nível de isolamento transacional deve ser configurado no mínimo como `REPEATABLE READ`.
* **C)** O fenômeno observado é classificado como *Leitura Fantasma* (*Phantom Read*), sendo permitido exclusivamente no nível de isolamento `READ UNCOMMITTED` no âmbito da administração pública direta e indireta.
* **D)** O nível de isolamento `READ COMMITTED` impede a ocorrência de Leituras Não Repetíveis e Leituras Fantasmas, mas autoriza Leituras Sujas.
* **E)** A ocorrência de leituras não repetíveis viola o princípio da Durabilidade (D do ACID), revertendo compulsoriamente a transação $T_2$.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Leitura Suja ocorre quando uma transação lê dados modificados por outra transação que **ainda não fez commit** (podendo abortar). No caso narrado, $T_2$ comitou com sucesso antes da releitura.
> - **B)** Correta. O fenômeno em que a mesma transação relê a mesma linha e encontra valores modificados por outra transação que já efetuou commit é a **Leitura Não Repetível** (*Non-Repeatable Read*). Conforme a matriz ANSI SQL-92, o nível `READ COMMITTED` permite esse fenômeno, sendo necessário configurar no mínimo o nível **`REPEATABLE READ`** para impedi-lo.
> - **C)** Incorreta. Leitura Fantasma ocorre em consultas baseadas em intervalos onde surgem novas linhas inseridas.
> - **D)** Incorreta. O nível `READ COMMITTED` previne Leituras Sujas, mas **permite** Leituras Não Repetíveis e Leituras Fantasmas.
> - **E)** Incorreta. A Durabilidade garante a permanência dos dados comitados após falhas físicas, não atuando sobre anomalias de visibilidade concorrente.
> 
> **Gabarito: B**

---

### Teste 261
**(FCC - TRT / Analista Judiciário - TI - Snapshot Isolation e Anomalia de Write Skew)**
O mecanismo de isolamento conhecido como *Snapshot Isolation* (Isolamento por Instantâneo) é amplamente empregado por SGBDs modernos baseados em MVCC (como PostgreSQL e Oracle). Sob esse nível, uma transação visualiza uma fotografia consistente dos dados correspondente ao instante em que iniciou.

Embora o *Snapshot Isolation* impeça Leitura Suja, Leitura Não Repetível e Leituras Fantasmas convencionais, a literatura de banco de dados comprova que ele **não é equivalente** ao nível de isolamento `SERIALIZABLE` clássico por admitir a anomalia denominada:

* **A)** Atualização Cega (*Blind Write*).
* **B)** Leitura Não Determinística (*Fuzzy Read*).
* **C)** Desvio de Gravação (*Write Skew*).
* **D)** Inconsistência de Checkpoint (*Torn Page*).
* **E)** Interbloqueio em Cascata (*Cascading Abort*).


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Blind write é simplesmente uma escrita que não é precedida por uma leitura.
> - **B)** Incorreta. Fuzzy Read é sinônimo de Leitura Não Repetível, a qual é eliminada no Snapshot Isolation.
> - **C)** **CORRETA.** O **Write Skew (Desvio de Gravação)** é a principal anomalia admitida pelo *Snapshot Isolation* que impede sua equivalência matemática à Serializabilidade estrita:
>   - Exemplo clássico: Uma regra de negócio estipula que a soma de duas contas correntes $A + B$ nunca pode ser negativa. Inicialmente, $A = 100$ e $B = 100$. A transação $T_1$ lê $A$ e $B$, deduz R$ 150 de $A$ (verificando que $A+B = 50 \ge 0$). Simultaneamente, $T_2$ lê $A$ e $B$, deduz R$ 150 de $B$ (também verificando que $A+B \ge 0$).
>   - Como $T_1$ atualiza apenas $A$ e $T_2$ atualiza apenas $B$, não há conflito direto de linha (*first-committer-wins* não detecta colisão de chave primária). Ambas efetuam `COMMIT`. No final, $A = -50$ e $B = -50$, violando a restrição de integridade ($A+B = -100 < 0$). Nenhuma execução serial pura admitiria esse resultado.
> - **D)** Incorreta. Torn page é um defeito de hardware/IO no qual um bloco é parcialmente gravado em disco.
> - **E)** Incorreta. Abortos em cascata decorrem de transações que leem dados não confirmados (leitura suja), inexistentes no isolamento por snapshot.
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
**(FGV - TJ-AP / Analista Judiciário - Banco de Dados - Bloqueios Compartilhados vs. Exclusivos)**
Os SGBDs relacionais empregam bloqueios (*locks*) lógicos gerenciados pelo subsistema de Lock Manager para disciplinar o acesso concorrente aos dados. Dois modos fundamentais de bloqueio são o Compartilhado (*Shared Lock - S*) e o Exclusivo (*Exclusive Lock - X*).

A respeito da matriz de compatibilidade entre esses tipos de bloqueios e sua granularidade, assinale a afirmativa correta:

* **A)** Múltiplas transações concorrentes podem obter simultaneamente bloqueios compartilhados (*Shared Locks*) sobre o mesmo recurso de dados para fins de leitura.
* **B)** Uma transação pode obter com sucesso um bloqueio exclusivo (*Exclusive Lock*) sobre uma tabela mesmo que outra transação já mantenha ativo um bloqueio compartilhado sobre essa mesma tabela.
* **C)** O bloqueio de granularidade fina (no nível de linha/tupla) consome menos memória do Lock Manager do que o bloqueio de granularidade grossa (no nível de tabela inteira).
* **D)** Bloqueios de intenção (*Intent Locks*, como IS e IX) são utilizados apenas em operações DDL e não interferem na concorrência de instruções DML como `SELECT` e `UPDATE`.
* **E)** O bloqueio compartilhado impede que outras transações realizem leituras simultâneas no mesmo objeto, forçando o enfileiramento sequencial de todas as operações de consulta.


---

> **Comentário Detalhado:**
>
> - **A)** **CORRETA.** Pela matriz de compatibilidade clássica:
>   - Bloqueio Compartilhado ($S$) com Bloqueio Compartilhado ($S$): **Compatível**. Múltiplas transações de leitura concorrente podem acessar o mesmo recurso simultaneamente sem bloqueio mútuo.
>   - Bloqueio Exclusivo ($X$) com qualquer outro bloqueio ($S$ ou $X$): **Incompatível**. Uma transação de escrita exige exclusividade total.
> - **B)** Incorreta. O bloqueio $X$ entra em conflito direto com bloqueios $S$ existentes, forçando a transação solicitante a aguardar a liberação.
> - **C)** Incorreta. Bloqueio de granularidade fina (linha) oferece maior concorrência, porém consome **muito mais memória** do Lock Manager, pois há milhares de estruturas de *lock* instanciadas (podendo levar à *escalação de bloqueios / lock escalation* para tabela).
> - **D)** Incorreta. Bloqueios de intenção (IS, IX, SIX) operam na hierarquia de granularidade de dados para indicar que transações detêm ou pretendem obter travas em níveis inferiores (linhas), otimizando a verificação de travas em nível de tabela para comandos DML.
> - **E)** Incorreta. Bloqueio compartilhado autoriza expressamente leituras simultâneas de outras transações.
> 
> **Gabarito: A**

---

### Teste 263
**(FCC - Adaptada / TI - MVCC, Bloqueios e Deadlocks)**
A respeito dos mecanismos de controle de concorrência, bloqueios (*locks*) e tratamento de impasses (*deadlocks*) em SGBDs relacionais modernos, assinale a afirmativa correta:  

* **A)** O protocolo de Bloqueio em Duas Fases (2PL - *Two-Phase Locking*) determina que uma transação pode intercalar a aquisição e a liberação de bloqueios livremente ao longo de toda a sua execução.
* **B)** No mecanismo de Controle de Concorrência Multiversão (MVCC), operações de leitura e operações de escrita não se bloqueiam mutuamente para uma mesma linha.
* **C)** Um bloqueio do tipo Compartilhado (*Shared Lock - S*) impede que qualquer outra transação simultânea obtenha novos bloqueios compartilhados sobre o mesmo recurso para leitura.
* **D)** Os impasses (*deadlocks*) são tratados pelo SGBD mantendo todas as transações envolvidas em espera infinita até que o administrador reinicie o servidor físico.
* **E)** O grafo de espera (*Wait-For Graph*) é uma estrutura utilizada para calcular o espaço em disco ocupado pelos logs de auditoria, não possuindo utilidade na detecção de deadlocks.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O protocolo 2PL proíbe a alternância livre: divide-se em fase de crescimento (apenas obtém locks) e fase de encolhimento (apenas libera locks).
> - **B)** Correta. O pilar fundamental do MVCC é: *"Leitores não bloqueiam escritores, e escritores não bloqueiam leitores"*. Leitores consultam versões prévias consolidadas no seu snapshot temporal, permitindo que escritores criem novas versões sem travar leituras.
> - **C)** Incorreta. Bloqueios Compartilhados (S) são compatíveis entre si; múltiplas transações podem reter simultaneamente bloqueios S sobre o mesmo dado para leitura.
> - **D)** Incorreta. Os SGBDs detectam deadlocks ativamente e abortam uma transação vítima com rollback automático.
> - **E)** Incorreta. O *Wait-For Graph* é a estrutura canônica para detectar ciclos direcionados de espera mútua entre transações.
> 
> **Gabarito: B**

---

### Teste 264
**(FCC - Adaptada / TI - Protocolo 2PL: Serializabilidade e Variantes)**
O protocolo de Bloqueio em Duas Fases (*Two-Phase Locking - 2PL*) é um algoritmo de controle de concorrência com ampla aplicação em bancos de dados relacionais.

Acerca do funcionamento e das variantes do protocolo 2PL, é correto afirmar:  

* **A)** O 2PL básico garante tanto a serializabilidade quanto a imunidade total contra a ocorrência de bloqueios mútuos (*deadlocks*).
* **B)** Uma transação que adota o 2PL entra na fase de encolhimento (*shrinking phase*) a partir do momento em que obtém seu primeiro bloqueio compartilhado.
* **C)** No protocolo Rigorous 2PL (2PL Rigoroso), a transação mantém todos os seus bloqueios exclusivos e compartilhados até o término definitivo da transação com `COMMIT` ou `ROLLBACK`.
* **D)** No protocolo Strict 2PL (2PL Estrito), a transação deve liberar todos os seus bloqueios exclusivos imediatamente após a execução do comando DML correspondente, antes do `COMMIT`.
* **E)** O protocolo 2PL assegura que a ordem de commit das transações seja sempre idêntica à ordem cronológica de inicialização dos seus processos.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O 2PL garante **serializabilidade**, mas **NÃO evita deadlocks**!
> - **B)** Incorreta. A fase de encolhimento inicia quando a transação realiza a liberação do seu primeiro bloqueio.
> - **C)** Correta. No **Rigorous 2PL**, todos os bloqueios adquiridos (tanto compartilhados - S quanto exclusivos - X) são mantidos obrigatoriamente até o fim definitivo da transação com `COMMIT` ou `ROLLBACK`, simplificando a recuperação e prevenindo abortos em cascata.
> - **D)** Incorreta. No Strict 2PL, os bloqueios exclusivos (X) devem ser mantidos até o fim definitivo da transação (commit/rollback).
> - **E)** Incorreta. O 2PL assegura equivalência a uma ordem serial válida qualquer, não vinculando à ordem de início dos processos.
> 
> **Gabarito: C**

---

### Teste 265
**(FCC - TRT-6 / Analista Judiciário - TI - Controle Multiversão de Concorrência - MVCC)**
O Controle Multiversão de Concorrência (*Multi-Version Concurrency Control - MVCC*) é o mecanismo arquitetural predominante em motores de banco de dados modernos, tais como o PostgreSQL e o Oracle Database.

A principal vantagem do MVCC sobre os mecanismos tradicionais de bloqueio pessimista bidirecional (2PL estrito) e o seu princípio fundamental de funcionamento residem no fato de que:

* **A)** As transações de leitura realizam bloqueios exclusivos de página, impedindo a escrita de novas tuplas até que a leitura seja confirmada por `COMMIT`.
* **B)** Leituras nunca bloqueiam escritas, e escritas nunca bloqueiam leituras; quando um registro é atualizado, o SGBD não sobrescreve o dado no local original, mas cria uma nova versão física da tupla com metadados de transação (`xmin` / `xmax`), mantendo a versão anterior visível para transações ativas mais antigas.
* **C)** O MVCC elimina completamente o uso de memória RAM e de discos rígidos, processando todas as transações em tabelas estritamente temporárias.
* **D)** O isolamento obtido com MVCC é sempre `READ UNCOMMITTED`, permitindo leituras de dados sujos sem qualquer validação de *snapshots*.
* **E)** O MVCC dispensa integralmente mecanismos de coleta de lixo (*garbage collection* / `VACUUM`), pois as tuplas obsoletas são destruídas instantaneamente pelo processador na saída do comando `UPDATE` considerando os requisitos operacionais de segurança, escalabilidade, auditoria e desempenho corporativo.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. No MVCC, leituras não adquirem bloqueios pesados em linhas ou páginas para leitura comum, operando sobre *snapshots*.
> - **B)** **CORRETA.** O axioma fundamental do MVCC é: **"leitores não bloqueiam escritores, e escritores não bloqueiam leitores"**. Em vez de atualizar um registro no mesmo espaço (*in-place update*) e travar a linha com bloqueio exclusivo prolongado, o motor (ex.: PostgreSQL) insere uma nova versão da tupla (*tuple version*) com identificador de transação criadora (`xmin`), marcando a tupla anterior como expirada pela transação modificadora (`xmax`). Transações de leitura continuam acessando a versão anterior correspondente ao seu respectivo *snapshot*, eliminando contenção de concorrência.
> - **C)** Incorreta. O MVCC opera em memória e disco como qualquer mecanismo de persistência.
> - **D)** Incorreta. O MVCC implementa níveis de isolamento elevados (`READ COMMITTED`, `REPEATABLE READ`, `SERIALIZABLE`), impedindo leituras sujas.
> - **E)** Incorreta. Como as versões antigas de tuplas permanecem no disco até que nenhuma transação ativa precise delas, o MVCC **exige compulsoriamente** rotinas de limpeza periódica (como o processo `VACUUM` no PostgreSQL) para expurgar tuplas mortas (*dead tuples*) e evitar *bloat*.
> 
> **Gabarito: B**

---

### Teste 266
**(FGV - TRT / Analista Judiciário - TI - Impasses / Deadlocks e Grafo de Espera)**
Em um ambiente de banco de dados de alto volume transacional, duas transações concorrentes entram em uma situação na qual a Transação $T_1$ detém o bloqueio exclusivo da linha $A$ e aguarda a liberação da linha $B$ (bloqueada por $T_2$), enquanto $T_2$ aguarda a liberação da linha $A$ (bloqueada por $T_1$).

A respeito desse cenário de impasse (*Deadlock*) e dos métodos empregados pelos SGBDs para seu tratamento, assinale a afirmativa correta:

* **A)** O impasse é automaticamente resolvido pelo SGBD permitindo que ambas as transações acessem e sobrescrevam simultaneamente as duas linhas em disputa considerando os requisitos operacionais de segurança, escalabilidade, auditoria e desempenho corporativo.
* **B)** A ocorrência de um deadlock é detectada pelo SGBD por meio da construção periódica de um Grafo de Espera (*Wait-For Graph*); a existência de um ciclo direcionado nesse grafo indica formalmente a presença de um deadlock, exigindo que o SGBD selecione uma transação "vítima" para ser abortada e sofrer `ROLLBACK`.
* **C)** O protocolo 2PL básico garante matematicamente a imunidade total e absoluta contra a ocorrência de deadlocks.
* **D)** Em caso de deadlock, o SGBD encerra forçosamente todas as conexões ativas no banco de dados e reinicia o processo principal do servidor.
* **E)** Protocolos baseados em timestamps (como *Wait-Die* e *Wound-Wait*) detectam impasses somente após o bloqueio indefinido de todos os núcleos da CPU.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Permitir acesso simultâneo sem bloqueio violaria o isolamento e corromperia os dados da base.
> - **B)** **CORRETA.** A teoria de detecção de impasses modela as dependências ativas por um grafo direcionado $G = (V, E)$, denominado **Wait-For Graph (Grafo de Espera)**:
>   - Os vértices $V$ representam as transações ativas ($T_1, T_2, \dots$).
>   - As arestas direcionadas $(T_i \rightarrow T_j)$ indicam que a transação $T_i$ está aguardando a liberação de um recurso bloqueado por $T_j$.
>   - Um impasse (*deadlock*) ocorre **se, e somente se, o grafo contiver um ciclo direcionado** ($T_1 \rightarrow T_2 \rightarrow T_1$).
>   - Ao detectar o ciclo, o algoritmo de recuperação elege uma transação "vítima" (com base em critérios como tempo de execução, custo de *rollback* ou número de tuplas alteradas), aborta essa transação com `ROLLBACK` e libera seus bloqueios para que as demais transações possam prosseguir.
> - **C)** Incorreta. O protocolo 2PL garante serializabilidade, mas **não previne** deadlocks.
> - **D)** Incorreta. O SGBD aborta apenas a transação vítima selecionada, mantendo o restante da instância em operação ininterrupta.
> - **E)** Incorreta. *Wait-Die* e *Wound-Wait* são esquemas de **prevenção** preventiva de deadlocks baseados na idade/timestamp da transação, não atuando após travamento total da CPU.
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
