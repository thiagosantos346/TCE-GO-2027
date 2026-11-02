# 02 - Linguagem SQL e Objetos de Banco

> **Matéria:** Banco de Dados  
> **Cargo:** B02 – Técnico de Controle Externo – Especialidade: Tecnologia da Informação  
> **Arquivo:** `02_linguagem_sql_ddl_dml_dql_tcl_e_dcl.md`  



---


## 📌 Ementa / Itens do Edital
- Linguagem SQL (ANSI e extensões procedurais)
- Subconjuntos da SQL: DDL, DML, DQL, DCL e TCL
- Consultas avançadas: Junções (Joins), Agrupamentos, Subconsultas, CTEs e Funções de Janela
- Objetos de banco de dados: Views (padrão e materializadas), Procedures, Functions e Triggers

---

## 🧭 Sumário

1. [Subconjuntos da Linguagem SQL](#1-subconjuntos-da-linguagem-sql)
    1. [Classificação ANSI: DDL, DML, DQL, DCL e TCL](#11-classificacao-ansi-ddl-dml-dql-dcl-e-tcl)
    2. [O Duelo Clássico: DROP vs. TRUNCATE vs. DELETE](#12-o-duelo-classico-drop-vs-truncate-vs-delete)
    3. [Restrições de Integridade (Constraints) e Ações de Chave Estrangeira](#13-restricoes-de-integridade-constraints-e-acoes-de-chave-estrangeira)
    4. [Teste 245](#Teste-245)
    5. [Teste 246](#Teste-246)
    6. [Teste 247](#Teste-247)
2. [Ordem Lógica de Execução da Consulta SQL (DQL)](#2-ordem-logica-de-execucao-da-consulta-sql-dql)
    1. [Ordem Léxica (Escrita) vs. Ordem Lógica (Processamento)](#21-ordem-lexica-escrita-vs-ordem-logica-processamento)
    2. [O Conflito WHERE vs. HAVING e a Ilegalidade de Aliases](#22-o-conflito-where-vs-having-e-a-ilegalidade-de-aliases)
    3. [Teste 248](#Teste-248)
3. [Consultas Avançadas: Junções, Operadores de Conjunto e Subconsultas](#3-consultas-avancadas-juncoes-operadores-de-conjunto-e-subconsultas)
    1. [Junções (INNER, LEFT, RIGHT, FULL OUTER e CROSS JOIN)](#31-juncoes-inner-left-right-full-outer-e-cross-join)
    2. [Operadores de Conjunto (UNION vs. UNION ALL, INTERSECT, EXCEPT)](#32-operadores-de-conjunto-union-vs-union-all-intersect-except)
    3. [Lógica Ternária (Three-Valued Logic) e a Armadilha do NOT IN com NULL](#33-logica-ternaria-three-valued-logic-e-a-armadilha-do-not-in-com-null)
    4. [Common Table Expressions (CTEs) e Recursividade (WITH RECURSIVE)](#34-common-table-expressions-ctes-e-recursividade-with-recursive)
    5. [Teste 249](#Teste-249)
    6. [Teste 250](#Teste-250)
    7. [Teste 251](#Teste-251)
    8. [Teste 252](#Teste-252)
4. [Funções Analíticas de Janela (Window Functions)](#4-funcoes-analiticas-de-janela-window-functions)
    1. [Sintaxe Geral e Cláusula OVER (PARTITION BY .. ORDER BY ..)](#41-sintaxe-geral-e-clausula-over-partition-by-order-by)
    2. [Funções de Ranking: ROW_NUMBER(), RANK() e DENSE_RANK()](#42-funcoes-de-ranking-rownumber-rank-e-denserank)
    3. [Funções de Deslocamento: LEAD() e LAG()](#43-funcoes-de-deslocamento-lead-e-lag)
    4. [Teste 253](#Teste-253)
    5. [Teste 254](#Teste-254)
5. [Objetos Programáveis de Banco de Dados](#5-objetos-programaveis-de-banco-de-dados)
    1. [Visões: View Padrão vs. View Materializada (Materialized View)](#51-visoes-view-padrao-vs-view-materializada-materialized-view)
    2. [Stored Procedures vs. User-Defined Functions (UDF)](#52-stored-procedures-vs-user-defined-functions-udf)
    3. [Gatilhos (Triggers): Eventos, Momentos (BEFORE, AFTER, INSTEAD OF) e Pseudorregistros OLD/NEW](#53-gatilhos-triggers-eventos-momentos-before-after-instead-of-e-pseudorregistros-oldnew)
    4. [Teste 255](#Teste-255)
6. [🌐 Fontes Oficiais e Referências Bibliográficas](#fontes-oficiais-e-referencias-bibliograficas)

---

## 1. Subconjuntos da Linguagem SQL

A linguagem SQL (*Structured Query Language*), padronizada internacionalmente pela norma ISO/IEC 9075, é subdividida em conjuntos de comandos com finalidades operacionais distintas:

```mermaid
flowchart TD
    SQL["Linguagem SQL"]
    SQL --> DDL["DDL (Definição)<br/>CREATE, ALTER, DROP, TRUNCATE"]
    SQL --> DML["DML (Manipulação)<br/>INSERT, UPDATE, DELETE"]
    SQL --> DQL["DQL (Consulta)<br/>SELECT"]
    SQL --> DCL["DCL (Controle)<br/>GRANT, REVOKE"]
    SQL --> TCL["TCL (Transação)<br/>COMMIT, ROLLBACK, SAVEPOINT"]
```

### 1.1 Classificação ANSI: DDL, DML, DQL, DCL e TCL

| Subconjunto | Denominação | Comandos Primários | Finalidade Operacional |
| :--- | :--- | :--- | :--- |
| **DDL** | *Data Definition Language* | `CREATE`, `ALTER`, `DROP`, `TRUNCATE`, `RENAME` | Criação, modificação estrutural e exclusão física de objetos no catálogo de dados (tabelas, esquemas, índices, visões). |
| **DML** | *Data Manipulation Language* | `INSERT`, `UPDATE`, `DELETE`, `MERGE` | Inserção, alteração e remoção de registros/tuplas dentro de tabelas existentes. |
| **DQL** | *Data Query Language* | `SELECT` | Consulta e recuperação de dados estruturados (frequentemente agrupada como subconjunto da DML). |
| **DCL** | *Data Control Language* | `GRANT`, `REVOKE` | Gestão de privilégios de acesso, concessão e revogação de permissões a usuários e papéis (*roles*). |
| **TCL** | *Transaction Control Language* | `COMMIT`, `ROLLBACK`, `SAVEPOINT` | Gerenciamento de blocos de transações atômicas, garantindo as propriedades ACID. |

### 1.2 O Duelo Clássico: DROP vs. TRUNCATE vs. DELETE

Um dos tópicos de maior incidência em provas da FCC para cargos de Tecnologia da Informação envolve a comparação detalhada entre as operações de remoção:

| Dimensão de Análise | `DELETE` | `TRUNCATE TABLE` | `DROP TABLE` |
| :--- | :--- | :--- | :--- |
| **Classificação Formal** | **DML** (*Manipulação*) | **DDL** (*Definição*) | **DDL** (*Definição*) |
| **Escopo de Remoção** | Linhas filtradas (`WHERE`) ou todas as linhas da tabela. | **Todas as linhas da tabela** incondicionalmente. | A **tabela inteira** (estrutura, dados e metadados no catálogo). |
| **Sobrecarga de Log (WAL/Redo)** | **Alto overhead:** Registra cada linha excluída individualmente no log de transações. | **Mínimo overhead:** Registra apenas a desalocação das páginas/extensões no disco. | **Mínimo overhead:** Registra a remoção do objeto do catálogo de dados. |
| **Velocidade de Execução** | Lento em grandes volumes de dados (milhões de linhas). | **Extremamente rápido** (quase instantâneo). | Instantâneo. |
| **Disparo de Triggers** | Dispara triggers de `DELETE` (`FOR EACH ROW` e `STATEMENT`). | **NÃO dispara** triggers de linha (`FOR EACH ROW`). | Não dispara triggers DML. |
| **Comportamento Transacional** | Suporta `ROLLBACK` em qualquer SGBD compatível com ACID. | Reversível no PostgreSQL/SQL Server; no Oracle efetua **COMMIT implícito**. | Reversível no PostgreSQL; no Oracle efetua **COMMIT implícito**. |
| **Reinício de Sequences (Identity)**| **Não reinicia** contadores de auto-incremento. | **Reinicia** os contadores de identidade para o valor inicial padrão. | A tabela deixa de existir fisicamente. |

> 🚨 **ALERTA DE PROVA / PEGADINHA FCC:**  
> A FCC adora elaborar enunciados afirmando que:
>
> 1. *"O comando TRUNCATE é uma operação DML porque manipula dados de linhas."* $\rightarrow$ **ERRADO!** O `TRUNCATE` é formalmente classificado como **DDL**, pois opera desalocando páginas físicas de armazenamento no catálogo de dados.
> 2. *"O comando TRUNCATE aciona gatilhos de auditoria FOR EACH ROW para registrar quem apagou cada linha."* $\rightarrow$ **ERRADO!** O `TRUNCATE` ignora completamente gatilhos de nível de linha!

### 1.3 Restrições de Integridade (Constraints) e Ações de Chave Estrangeira

As restrições de integridade garantem a consistência lógica dos dados no banco:

- **`PRIMARY KEY`:** Garante unicidade e impede valores nulos (`UNIQUE` + `NOT NULL`). Cada tabela pode conter apenas uma chave primária.
- **`FOREIGN KEY` (Integridade Referencial):** Impõe que o valor da coluna exista previamente na chave primária da tabela referenciada.
    - **Ações Referenciais em Deleção/Atualização (`ON DELETE` / `ON UPDATE`):**
    - `RESTRICT` / `NO ACTION`: Bloqueia e rejeita a operação no pai caso existam registros filhos dependentes (comportamento padrão).
    - `CASCADE`: Propaga a alteração/exclusão automaticamente aos filhos (se o contrato for apagado, todos os seus aditivos são apagados).
    - `SET NULL`: Atualiza o campo da chave estrangeira dos filhos para `NULL` quando o pai é excluído (exige que a coluna aceite nulos).
    - `SET DEFAULT`: Preenche a chave estrangeira dos filhos com o valor padrão configurado.
- **`UNIQUE`:** Impede valores duplicados, mas permite a inserção de valores nulos (`NULL`), exceto se combinado com `NOT NULL`.
- **`CHECK`:** Valida predicados booleanos customizados antes de persistir a tupla (ex.: `CHECK (valor_empenho > 0)`).

---

### Teste 245
**(FGV – TRT-16 – Analista Judiciario Area Administrativa Tecnologia da Informacao – 2022)**
Observe os dois comandos de atribuição do JavaScript. let X = -100; X <<= 5; Assinale o valor de X após a execução desses comandos.

* **A)** 0
* **B)** 3
* **C)** -100
* **D)** -200
* **E)** -3200 ATENÇÂO: Nas próximas três questões, considere o esquema relacional de um banco de dados numa instalação SQL Server na qual os nulos são tratados como valores desconhecidos (unknow). create table X(A int not null primary key, B int) create table Y(A int not null UNIQUE, constraint fk foreign key (A) references X(A) on delete cascade) Para todos os efeitos, suponha que o número de linhas em cada tabela é diferente de zero.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "0". De acordo com a teoria estudada em *1.3 Restrições de Integridade (Constraints) e Ações de Chave Estrangeira*, `UNIQUE`: Impede valores duplicados, mas permite a inserção de valores nulos (`NULL`), exceto se combinado com `NOT NULL`.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "3". De acordo com a teoria estudada em *1.3 Restrições de Integridade (Constraints) e Ações de Chave Estrangeira*, `FOREIGN KEY` (Integridade Referencial): Impõe que o valor da coluna exista previamente na chave primária da tabela referenciada.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "-100". De acordo com a teoria estudada em *3.3 Lógica Ternária (Three-Valued Logic) e a Armadilha do NOT IN com NULL*, em SQL, qualquer comparação direta com valor nulo (`coluna = NULL` ou `coluna != NULL`) avalia como `UNKNOWN` (*Desconhecido*), e não como `TRUE` nem `FALSE`. Para testar nulos, deve-se usar estritamente `IS NULL` ou `IS NOT NULL`.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "-200". De acordo com a teoria estudada em *3.3 Lógica Ternária (Three-Valued Logic) e a Armadilha do NOT IN com NULL*, resultado Catastrófico: A consulta retornará ZERO LINHAS (conjunto vazio)!.
> - **E)** **Correta.** Conforme fundamentado na seção *1.3 Restrições de Integridade (Constraints) e Ações de Chave Estrangeira* deste guia, `PRIMARY KEY`: Garante unicidade e impede valores nulos (`UNIQUE` + `NOT NULL`). Cada tabela pode conter apenas uma chave primária. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT-16/2022) ao estabelecer que "-3200 ATENÇÂO: Nas próximas três questões, considere o esquema relacional de um banco de dados numa instalação SQL...".
>
> **Gabarito: E**

---

### Teste 246
**(FGV – TCE-GO – Analista de Controle Externo Tecnologia da Informacao – 2024)**
Considere um banco de dados relacional de um tribunal, na qual nenhum usuário, a menos do DBA, possua algum privilégio sobre. O DBA concedeu direito de criação de tabelas ao usuário USR_0010, que, por sua vez, criou as tabelas DADOS_PROCESSO e DADOS_PARTE. Logo após a criação, o usuário USR_0010 executou os seguintes comandos da DCL (Data Control Language) da linguagem SQL no sistema gerenciador de banco de dados, referentes aos usuários USR_0011 e USR_0100: GRANT SELECT, UPDATE ON DADO_PARTE TO USR_0011; GRANT SELECT ON DADOS_PARTE TO USR_0100; GRANT SELECT, INSERT, DELETE, UPDATE ON DADOS_PROCESSO TO USR_0011; GRANT SELECT, UPDATE ON DADOS_PROCESSO TO USR_0100 WITH GRANT OPTION; Na sequência, o usuário USR_0100 executou o seguinte comando: GRANT UPDATE ON DADOS_PROCESSO TO USR_00101; Por fim, o DBA executou o comando: REVOKE UPDATE ON DADOS_PROCESSO FROM USR_0100; Considerando esse cenário, qual situação é válida para as permissões referentes às tabelas DADOS_PROCESSO e DADOS_PARTE?

* **A)** O usuário USR_0011 tem direito de inserção na tabela DADOS_PARTE.
* **B)** O usuário USR_0100 tem direito de atualização na tabela DADOS_PROCESSO, mas sem direito de propagação.
* **C)** O usuário USR_0100 tem direito de consulta na tabela DADOS_PROCESSO, com direito de propagação.
* **D)** O usuário USR_0101 tem direito de atualização na tabela DADOS_PROCESSO.
* **E)** O usuário USR_0101 tem direito de consulta na tabela DADOS_PROCESSO.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O usuário USR_0011 tem direito de inserção na tabela DADOS_PARTE". De acordo com a teoria estudada em *1.1 Classificação ANSI: DDL, DML, DQL, DCL e TCL*, dML: *Data Manipulation Language* — `INSERT`, `UPDATE`, `DELETE`, `MERGE` — Inserção, alteração e remoção de registros/tuplas dentro de tabelas existentes.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O usuário USR_0100 tem direito de atualização na tabela DADOS_PROCESSO, mas sem direito de propagação". De acordo com a teoria estudada em *1.1 Classificação ANSI: DDL, DML, DQL, DCL e TCL*, dQL: *Data Query Language* — `SELECT` — Consulta e recuperação de dados estruturados (frequentemente agrupada como subconjunto da DML).
> - **C)** **Correta.** Conforme fundamentado na seção *1.1 Classificação ANSI: DDL, DML, DQL, DCL e TCL* deste guia, dCL: *Data Control Language* — `GRANT`, `REVOKE` — Gestão de privilégios de acesso, concessão e revogação de permissões a usuários e papéis (*roles*). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE-GO/2024) ao estabelecer que "O usuário USR_0100 tem direito de consulta na tabela DADOS_PROCESSO, com direito de propagação".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O usuário USR_0101 tem direito de atualização na tabela DADOS_PROCESSO". De acordo com a teoria estudada em *1.1 Classificação ANSI: DDL, DML, DQL, DCL e TCL*, dDL: *Data Definition Language* — `CREATE`, `ALTER`, `DROP`, `TRUNCATE`, `RENAME` — Criação, modificação estrutural e exclusão física de objetos no catálogo de dados (tabelas, esquemas, índices, visões).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O usuário USR_0101 tem direito de consulta na tabela DADOS_PROCESSO". De acordo com a teoria estudada em *5.1 Visões: View Padrão vs. View Materializada (Materialized View)*, não armazena dados físicos em disco; representa apenas uma consulta SQL gravada no dicionário de dados do SGBD.
>
> **Gabarito: C**

---

### Teste 247
**(FGV – TRT-13 – Analista Judiciario Tecnologia da Informacao – 2022)**
Considere uma tabela relacional X com uma única coluna A, cuja instância contém uma linha apenas, e os comandos SQL a seguir. ------------- 1. delete from X where exists (select * from X x2 where x2.A = X.A) 2. delete from X where not exists (select * from X x2 where x2.A = X.A) ------------- Nesse contexto, analise as afirmativas sobre os efeitos desses comandos. I. Nenhuma linha seria deletada na execução do comando 1. II. Uma linha seria deletada na execução do comando 1. III. Nenhuma linha seria deletada na execução do comando 2. IV. Uma linha seria deletada na execução do comando 2. V. Os dois comandos gerariam erros de execução. Está correto o que se afirma em

* **A)** I e III, apenas.
* **B)** I e IV, apenas.
* **C)** II e III, apenas.
* **D)** II e IV, apenas.
* **E)** V, apenas.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e III, apenas". De acordo com a teoria estudada em *3.3 Lógica Ternária (Three-Valued Logic) e a Armadilha do NOT IN com NULL*, considere a consulta: `SELECT nome FROM cliente WHERE id NOT IN (SELECT id_cliente FROM divida);`.
> - **B)** **Correta.** Conforme fundamentado na seção *5.2 Stored Procedures vs. User-Defined Functions (UDF)* deste guia, invocação: Comando explícito `CALL procedure_name(args);` — Invocada inline em comandos SQL: `SELECT func(x) FROM tab;`. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT-13/2022) ao estabelecer que "I e IV, apenas".
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II e III, apenas". De acordo com a teoria estudada em *2.2 O Conflito WHERE vs. HAVING e a Ilegalidade de Aliases*, *Código Inválido:* `SELECT salario * 1.1 AS novo_salario FROM servidor WHERE novo_salario > 5000;` *(Gera erro de coluna inexistente!)*.
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II e IV, apenas". De acordo com a teoria estudada em *Pseudorregistros de Contexto:*, no `DELETE`: Contém os valores da linha que está sendo removida.
> - **E)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "V, apenas". De acordo com a teoria estudada em *2. Ordem Lógica de Execução da Consulta SQL (DQL)*, ao escrever uma consulta com a cláusula `SELECT`, a ordem sintática da escrita (ordem léxica) é muito diferente da ordem lógica de processamento adotada pelo otimizador de consultas do SGBD.
>
> **Gabarito: B**

---

## 2. Ordem Lógica de Execução da Consulta SQL (DQL)

Ao escrever uma consulta com a cláusula `SELECT`, a ordem sintática da escrita (ordem léxica) é muito diferente da **ordem lógica de processamento** adotada pelo otimizador de consultas do SGBD:

```mermaid
flowchart TD
    P1["1. FROM / JOIN / ON<br/>(Identifica tabelas e computa junções)"] --> P2["2. WHERE<br/>(Filtra tuplas brutas linha a linha)"]
    P2 --> P3["3. GROUP BY<br/>(Agrupa os registros restantes)"]
    P3 --> P4["4. HAVING<br/>(Filtra grupos agregados)"]
    P4 --> P5["5. WINDOW FUNCTIONS<br/>(Aplica OVER: ROW_NUMBER, RANK)"]
    P5 --> P6["6. SELECT<br/>(Calcula expressões e aliases de colunas)"]
    P6 --> P7["7. DISTINCT<br/>(Elimina tuplas duplicadas)"]
    P7 --> P8["8. UNION / INTERSECT / EXCEPT<br/>(Aplica operações de conjunto)"]
    P8 --> P9["9. ORDER BY<br/>(Ordena o resultado final)"]
    P9 --> P10["10. LIMIT / OFFSET<br/>(Paginador / fatia final do resultado)"]
```

### 2.1 Ordem Léxica (Escrita) vs. Ordem Lógica (Processamento)

A ordem lógica executada pelo motor relacional é rigorosamente:

1. **`FROM` e `JOIN / ON`:** Identifica as relações de entrada e calcula produtos cartesianos e junções;
2. **`WHERE`:** Aplica filtros booleanos linha a linha antes de qualquer agregação;
3. **`GROUP BY`:** Agrupa as linhas restantes em blocos lógicos baseados nas chaves de agrupamento;
4. **`HAVING`:** Aplica filtros booleanos sobre os grupos agregados gerados;
5. **`WINDOW` (Funções de Janela):** Computa partições e ordenações analíticas (`OVER`);
6. **`SELECT`:** Avalia as expressões da lista de projeção e atribui apelidos de colunas (*aliases*);
7. **`DISTINCT`:** Elimina tuplas que apresentem valores rigorosamente idênticos na projeção;
8. **`UNION / INTERSECT / EXCEPT`:** Executa operações de conjuntos de linhas;
9. **`ORDER BY`:** Ordena as tuplas resultantes para exibição;
10. **`LIMIT / OFFSET`:** Extrai a fatia dimensional delimitada para paginação.

### 2.2 O Conflito WHERE vs. HAVING e a Ilegalidade de Aliases

Compreender essa cronologia lógica resolve duas das questões mais frequentes da FCC:

1. **Ilegalidade de Aliases no `WHERE`:**  
   Como a cláusula `WHERE` (etapa 2) é processada **muito antes da cláusula `SELECT`** (etapa 6), qualquer apelido de coluna (*alias*) criado no `SELECT` ainda não existe no catálogo de símbolos durante a avaliação do `WHERE`.  
   *Código Inválido:* `SELECT salario * 1.1 AS novo_salario FROM servidor WHERE novo_salario > 5000;` *(Gera erro de coluna inexistente!)*.
2. **`WHERE` vs. `HAVING`:**  
    - O **`WHERE`** filtra registros **individuais** antes da formação dos grupos e **rejeita terminantemente funções agregadas** (ex.: `WHERE SUM(valor) > 100` é sintaticamente inválido).
    - O **`HAVING`** filtra **grupos agregados** já sumarizados pelo `GROUP BY` e aceita funções agregadas (ex.: `HAVING SUM(valor) > 100`).

---

### Teste 248
**(FGV – TRT-24 – Analista Judiciario Area Apoio Especializado Tecnologia da Informacao – 2025)**
O PostgreSQL é um SGBD gratuito de código aberto que suporta consultas relacionais em linguagem SQL. Com relação ao SQL do PostgreSQL, analise as afirmativas a seguir. I. A cláusula GROUP BY agrupa linhas com os mesmos valores em linhas de resumo, sendo frequentemente usada com funções de agregação como, por exemplo, COUNT( ), MAX( ), MIN( ), SUM( ) e AVG( ), para agrupar um conjunto de resultados de uma ou mais colunas. II. O operador HAVING foi adicionado ao SQL porque o WHERE não pode ser usado com funções de agregação, as quais são frequentemente usadas com a cláusula GROUP BY. Ao adicionar o HAVING é possível escrever condições similares às das cláusulas WHERE. III. A expressão CASE testa condições e retorna um valor quando a primeira condição é atendida (como uma instrução if-thenelse); quando a condição seja verdadeira, ele parará a leitura e retornará o resultado, mas, se nenhuma condição for verdadeira, ele retornará o valor da cláusula ELSE. Caso não houver nenhum ELSE e nenhuma condição for verdadeira, ele retornará o valor NULL. Está correto o que se afirma em

* **A)** I e II, apenas.
* **B)** I e III, apenas.
* **C)** II e III, apenas.
* **D)** I e IV, apenas.
* **E)** III e IV, apenas.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e II, apenas". De acordo com a teoria estudada em *2. Ordem Lógica de Execução da Consulta SQL (DQL)*, ao escrever uma consulta com a cláusula `SELECT`, a ordem sintática da escrita (ordem léxica) é muito diferente da ordem lógica de processamento adotada pelo otimizador de consultas do SGBD.
> - **B)** **Correta.** Conforme fundamentado na seção *2.2 O Conflito WHERE vs. HAVING e a Ilegalidade de Aliases* deste guia, o `HAVING` filtra grupos agregados já sumarizados pelo `GROUP BY` e aceita funções agregadas (ex.: `HAVING SUM(valor) > 100`). Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT-24/2025) ao estabelecer que "I e III, apenas".
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II e III, apenas". De acordo com a teoria estudada em *2.2 O Conflito WHERE vs. HAVING e a Ilegalidade de Aliases*, o `WHERE` filtra registros individuais antes da formação dos grupos e rejeita terminantemente funções agregadas (ex.: `WHERE SUM(valor) > 100` é sintaticamente inválido).
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e IV, apenas". De acordo com a teoria estudada em *1.2 O Duelo Clássico: DROP vs. TRUNCATE vs. DELETE*, comportamento Transacional: Suporta `ROLLBACK` em qualquer SGBD compatível com ACID. — Reversível no PostgreSQL/SQL Server; no Oracle efetua COMMIT implícito. — Reversível no PostgreSQL; no Oracle efetua COMMIT implícito.
> - **E)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "III e IV, apenas". De acordo com a teoria estudada em *3.3 Lógica Ternária (Three-Valued Logic) e a Armadilha do NOT IN com NULL*, resultado Catastrófico: A consulta retornará ZERO LINHAS (conjunto vazio)!.
>
> **Gabarito: B**

---

## 3. Consultas Avançadas: Junções, Operadores de Conjunto e Subconsultas

### 3.1 Junções (INNER, LEFT, RIGHT, FULL OUTER e CROSS JOIN)

- **`INNER JOIN`:** Retorna exclusivamente as tuplas que possuem correspondência em ambas as tabelas com base na condição de junção (`ON`). Linhas sem correspondência são sumariamente descartadas.
- **`LEFT OUTER JOIN` (ou `LEFT JOIN`):** Retorna todas as tuplas da tabela à esquerda (`FROM`), combinando com as tuplas da tabela à direita. Caso não haja correspondência na tabela da direita, os atributos da direita são preenchidos com valores nulos (`NULL`).
- **`RIGHT OUTER JOIN` (ou `RIGHT JOIN`):** Comportamento inverso do LEFT JOIN: preserva todas as tuplas da tabela da direita, preenchendo com `NULL` as ausências da tabela da esquerda.
- **`FULL OUTER JOIN`:** Preserva todas as tuplas de ambas as tabelas. Quando não há correspondência mútua, preenche com `NULL` os atributos correspondentes.
- **`CROSS JOIN`:** Produz o produto cartesiano irrestrito entre as tabelas (cada linha da primeira tabela é combinada com todas as linhas da segunda).

### 3.2 Operadores de Conjunto (UNION vs. UNION ALL, INTERSECT, EXCEPT)

- **`UNION` vs. `UNION ALL`:**
    - **`UNION`:** Combina os resultados de duas consultas com compatibilidade de esquema e executa um algoritmo interno de ordenação/hashing para **eliminar compulsoriamente linhas duplicadas**.
    - **`UNION ALL`:** Apenas concatena as duas listas de tuplas, **preservando todas as duplicatas intactas**. Possui desempenho computacional dramaticamente superior ao `UNION`.
- **`INTERSECT`:** Retorna apenas as tuplas que constam simultaneamente em ambas as consultas, eliminando duplicatas.
- **`EXCEPT` (ou `MINUS` no Oracle):** Retorna as tuplas da primeira consulta que não estão presentes na segunda consulta.

### 3.3 Lógica Ternária (Three-Valued Logic) e a Armadilha do NOT IN com NULL

Em SQL, qualquer comparação direta com valor nulo (`coluna = NULL` ou `coluna != NULL`) avalia como **`UNKNOWN`** (*Desconhecido*), e não como `TRUE` nem `FALSE`. Para testar nulos, deve-se usar estritamente `IS NULL` ou `IS NOT NULL`.

> 🚨 **ALERTA DE PROVA / PEGADINHA FCC:**  
> A armadilha clássica da FCC em subconsultas:  
> Considere a consulta: `SELECT nome FROM cliente WHERE id NOT IN (SELECT id_cliente FROM divida);`  
>
> - Se a tabela `divida` contiver **ao menos UM único registro cujo `id_cliente` seja `NULL`**, a subconsulta retornará o valor `NULL`.  
> - Como o predicado desdobra-se em: `id != 1 AND id != 2 AND id != NULL`, e qualquer comparação com `NULL` resulta em `UNKNOWN`, a expressão inteira avaliará como `UNKNOWN` para todas as linhas!  
> - **Resultado Catastrófico:** A consulta retornará **ZERO LINHAS (conjunto vazio)**!  
> - **Solução Recomendada:** Utilizar sempre a construção com **`NOT EXISTS`** correlacionado, imune a valores nulos.

### 3.4 Common Table Expressions (CTEs) e Recursividade (WITH RECURSIVE)

As Expressões de Tabela Comuns (*CTEs*) são conjuntos de resultados temporários nomeados declarados através da cláusula `WITH`:

```sql
WITH AuditoriasRecentes AS (
    SELECT auditor_id, COUNT(*) AS total
    FROM fiscalizacao
    WHERE data_inspecao >= '2026-01-01'
    GROUP BY auditor_id
)
SELECT a.nome, ar.total
FROM auditor a
JOIN AuditoriasRecentes ar ON a.id = ar.auditor_id;
```

- **`WITH RECURSIVE`:** Permite que a CTE faça referência a si mesma, viabilizando consultas em estruturas hierárquicas e em grafos (como organogramas empresariais ou árvores de dependência de processos).

---

### Teste 249
**(FGV – TJ-AP – Analista Judiciario Apoio Especializado Tecnologia da Informacao Banco de Dados – 2023)**
Considerando as tabelas Competidor e Disputa, descritas anteriormente, analise o comando SQL a seguir. select nome from Competidor C where not exists (select * from Disputa D where D.azul = C.nome) or not exists (select * from Disputa D where D.verde = C.nome) A execução do comando acima produziria somente a lista completa dos competidores que:

* **A)** participaram em disputas com camisas das duas cores;
* **B)** nunca participaram em disputas com camisa verde;
* **C)** nunca participaram em disputas com camisa azul;
* **D)** nas disputas em que participaram, usaram sempre camisas da mesma cor;
* **E)** nunca participaram em disputas.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "participaram em disputas com camisas das duas cores". De acordo com a teoria estudada em *3.3 Lógica Ternária (Three-Valued Logic) e a Armadilha do NOT IN com NULL*, considere a consulta: `SELECT nome FROM cliente WHERE id NOT IN (SELECT id_cliente FROM divida);`.
> - **B)** **Incorreta.** A opção apresenta vedação ou negativa absoluta incompatível com a regra aplicável ao afirmar que "nunca participaram em disputas com camisa verde". De acordo com a teoria estudada em *5.2 Stored Procedures vs. User-Defined Functions (UDF)*, invocação: Comando explícito `CALL procedure_name(args);` — Invocada inline em comandos SQL: `SELECT func(x) FROM tab;`.
> - **C)** **Incorreta.** A opção apresenta vedação ou negativa absoluta incompatível com a regra aplicável ao afirmar que "nunca participaram em disputas com camisa azul". De acordo com a teoria estudada em *5.1 Visões: View Padrão vs. View Materializada (Materialized View)*, vantagens: Dados sempre 100% atualizados; atua como camada de segurança e abstração (ocultando colunas confidenciais).
> - **D)** **Correta.** Conforme fundamentado na seção *3.3 Lógica Ternária (Three-Valued Logic) e a Armadilha do NOT IN com NULL* deste guia, solução Recomendada: Utilizar sempre a construção com `NOT EXISTS` correlacionado, imune a valores nulos. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ-AP/2023) ao estabelecer que "nas disputas em que participaram, usaram sempre camisas da mesma cor".
> - **E)** **Incorreta.** A opção apresenta vedação ou negativa absoluta incompatível com a regra aplicável ao afirmar que "nunca participaram em disputas". De acordo com a teoria estudada em *3.4 Common Table Expressions (CTEs) e Recursividade (WITH RECURSIVE)*, `WITH RECURSIVE`: Permite que a CTE faça referência a si mesma, viabilizando consultas em estruturas hierárquicas e em grafos (como organogramas empresariais ou árvores de dependência de processos).
>
> **Gabarito: D**

---

### Teste 250
**(FUMARC – TRT-3 – Analista Judiciario Apoio Especializado Tecnologia da Informacao – 2022)**
21 Escolha a sentença SQL que MELHOR responda à consulta “Listar o nome de todos os empregadores da tabela EMPREGADOR e o total de contratos cadastrados na tabela CONTRATO para cada um. Empregadores sem contratos cadastrados devem aparecer com total igual a zero.”:

* **A)** SELECT e.nome_empregador, COUNT(*) as total FROM EMPREGADOR as e LEFT JOIN CONTRATO as c ON e.id = c.id GROUP BY e.nome_empregador;
* **B)** SELECT e.nome_empregador, COUNT(c.id) as total FROM EMPREGADOR as e LEFT JOIN CONTRATO as c ON e.id = c.id_empregador WHERE c.id_empregador <> NULL GROUP BY e.nome_empregador;
* **C)** SELECT e.nome_empregador, COUNT(c.id) as total FROM EMPREGADOR as e LEFT JOIN CONTRATO as c ON e.id = c.id_empregador GROUP BY e.nome_empregador;
* **D)** SELECT e.nome_empregador, COUNT(c.id) as total FROM EMPREGADOR as e RIGHT JOIN CONTRATO as c ON e.id = c.id_empregador GROUP BY e.nome_empregador;
* **E)** SELECT e.nome_empregador, COUNT(c.id) as total FROM EMPREGA- DOR as e INNER JOIN CONTRATO as c ON e.id = c.id_empregador GROUP BY e.nome_empregador;

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "SELECT e.nome_empregador, COUNT(*) as total FROM EMPREGADOR as e LEFT JOIN CONTRATO as c ON e.id = c.id GROUP BY...". De acordo com a teoria estudada em *3.1 Junções (INNER, LEFT, RIGHT, FULL OUTER e CROSS JOIN)*, `LEFT OUTER JOIN` (ou `LEFT JOIN`): Retorna todas as tuplas da tabela à esquerda (`FROM`), combinando com as tuplas da tabela à direita. Caso não haja correspondência na tabela da direita, os atributos da direita são preenchidos com valores nulos (`NULL`).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "SELECT e.nome_empregador, COUNT(c.id) as total FROM EMPREGADOR as e LEFT JOIN CONTRATO as c ON e.id =...". De acordo com a teoria estudada em *3.1 Junções (INNER, LEFT, RIGHT, FULL OUTER e CROSS JOIN)*, `RIGHT OUTER JOIN` (ou `RIGHT JOIN`): Comportamento inverso do LEFT JOIN: preserva todas as tuplas da tabela da direita, preenchendo com `NULL` as ausências da tabela da esquerda.
> - **C)** **Correta.** Conforme fundamentado na seção *3.3 Lógica Ternária (Three-Valued Logic) e a Armadilha do NOT IN com NULL* deste guia, considere a consulta: `SELECT nome FROM cliente WHERE id NOT IN (SELECT id_cliente FROM divida);`. Dessa forma, está plenamente correta a assertiva da banca (FUMARC – TRT-3/2022) ao estabelecer que "SELECT e.nome_empregador, COUNT(c.id) as total FROM EMPREGADOR as e LEFT JOIN CONTRATO as c ON e.id =...".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "SELECT e.nome_empregador, COUNT(c.id) as total FROM EMPREGADOR as e RIGHT JOIN CONTRATO as c ON e.id =...". De acordo com a teoria estudada em *3.1 Junções (INNER, LEFT, RIGHT, FULL OUTER e CROSS JOIN)*, `CROSS JOIN`: Produz o produto cartesiano irrestrito entre as tabelas (cada linha da primeira tabela é combinada com todas as linhas da segunda).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "SELECT e.nome_empregador, COUNT(c.id) as total FROM EMPREGA- DOR as e INNER JOIN CONTRATO as c ON e.id =...". De acordo com a teoria estudada em *3.1 Junções (INNER, LEFT, RIGHT, FULL OUTER e CROSS JOIN)*, `INNER JOIN`: Retorna exclusivamente as tuplas que possuem correspondência em ambas as tabelas com base na condição de junção (`ON`). Linhas sem correspondência são sumariamente descartadas.
>
> **Gabarito: C**

---

### Teste 251
**(FGV – TJ-AP – Analista Judiciario Apoio Especializado Tecnologia da Informacao Banco de Dados – 2023)**
Considerando as tabelas Competidor e Disputa, descritas anteriormente, analise os três comandos SQL a seguir. I. select C.nome from Competidor C where exists (select * from Disputa D where D.azul = C.nome) and exists (select * from Disputa D where D.verde = C.nome) II. select C.nome from Competidor C where exists (select * from Disputa D where D.azul = C.nome or D.verde = C.nome) III. select C.nome from Competidor C where (select count(*) from Disputa D where D.azul = C.nome) + (select count(*) from Disputa D where D.verde = C.nome) > 1 O resultado Nome A B é obtido somente no(s) comando(s):

* **A)** I;
* **B)** II;
* **C)** III;
* **D)** I e II;
* **E)** II e III.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *5.2 Stored Procedures vs. User-Defined Functions (UDF)* deste guia, invocação: Comando explícito `CALL procedure_name(args);` — Invocada inline em comandos SQL: `SELECT func(x) FROM tab;`. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ-AP/2023) ao estabelecer que "I".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "II". De acordo com a teoria estudada em *3.3 Lógica Ternária (Three-Valued Logic) e a Armadilha do NOT IN com NULL*, considere a consulta: `SELECT nome FROM cliente WHERE id NOT IN (SELECT id_cliente FROM divida);`.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "III". De acordo com a teoria estudada em *2.2 O Conflito WHERE vs. HAVING e a Ilegalidade de Aliases*, *Código Inválido:* `SELECT salario * 1.1 AS novo_salario FROM servidor WHERE novo_salario > 5000;` *(Gera erro de coluna inexistente!)*.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I e II". De acordo com a teoria estudada em *5.1 Visões: View Padrão vs. View Materializada (Materialized View)*, trade-off: Os dados ficam estáticos/defasados até que um comando de atualização explícito seja disparado: `REFRESH MATERIALIZED VIEW nome_da_view;`.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "II e III". De acordo com a teoria estudada em *1. Subconjuntos da Linguagem SQL*, a linguagem SQL (*Structured Query Language*), padronizada internacionalmente pela norma ISO/IEC 9075, é subdividida em conjuntos de comandos com finalidades operacionais distintas.
>
> **Gabarito: A**

---

### Teste 252
**(FCC – TRT-6 – Analista Judiciario Apoio Especializado Tecnologia da Informacao – 2012)**
Considere os seguintes comandos em PL/SQL: CREATE TABLE VALORES (ID INT NOT NULL PRIMARY KEY,VALOR INT); INSERT INTO VALORES VALUES (1,5); INSERT INTO VALORES VALUES (1,6); INSERT INTO VALORES VALUES (NULL,7); INSERT INTO VALORES VALUES (2,1); INSERT INTO VALORES VALUES (2,8); INSERT INTO VALORES VALUES (3,9); INSERT INTO VALORES VALUES (NULL,10); SELECT COUNT(VALOR) FROM VALORES WHERE VALOR >= 5; A consulta retornará o valor

* **A)** 2.
* **B)** 14.
* **C)** 6.
* **D)** 29.
* **E)** 5.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *3.3 Lógica Ternária (Three-Valued Logic) e a Armadilha do NOT IN com NULL* deste guia, considere a consulta: `SELECT nome FROM cliente WHERE id NOT IN (SELECT id_cliente FROM divida);`. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT-6/2012) ao estabelecer que "2".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "14". De acordo com a teoria estudada em *1.3 Restrições de Integridade (Constraints) e Ações de Chave Estrangeira*, `PRIMARY KEY`: Garante unicidade e impede valores nulos (`UNIQUE` + `NOT NULL`). Cada tabela pode conter apenas uma chave primária.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "6". De acordo com a teoria estudada em *3.3 Lógica Ternária (Three-Valued Logic) e a Armadilha do NOT IN com NULL*, resultado Catastrófico: A consulta retornará ZERO LINHAS (conjunto vazio)!.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "29". De acordo com a teoria estudada em *3.3 Lógica Ternária (Three-Valued Logic) e a Armadilha do NOT IN com NULL*, se a tabela `divida` contiver ao menos UM único registro cujo `id_cliente` seja `NULL`, a subconsulta retornará o valor `NULL`.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "5". De acordo com a teoria estudada em *5.2 Stored Procedures vs. User-Defined Functions (UDF)*, invocação: Comando explícito `CALL procedure_name(args);` — Invocada inline em comandos SQL: `SELECT func(x) FROM tab;`.
>
> **Gabarito: A**

---

## 4. Funções Analíticas de Janela (Window Functions)

Diferente da cláusula `GROUP BY` (que colapsa múltiplas linhas em um único registro agregado por partição), as **funções de janela (*Window Functions*)** realizam cálculos agregados e analíticos **sem colapsar as tuplas**, preservando a identidade e o detalhe de cada linha individual.

### 4.1 Sintaxe Geral e Cláusula OVER (PARTITION BY .. ORDER BY ..)

```sql
FUNCAO_ANALITICA() OVER (
    PARTITION BY coluna_agrupamento
    ORDER BY coluna_ordenacao DESC
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
)
```

- **`PARTITION BY`:** Divide o conjunto de resultados em janelas lógicas independentes (equivalente ao agrupamento, sem colapsar linhas).
- **`ORDER BY`:** Define a ordem de processamento das tuplas dentro de cada partição.
- **`Frame Specification` (`ROWS / RANGE`):** Delimita o subconjunto deslizante de linhas que compõem o cálculo da janela (ex.: médias móveis).

### 4.2 Funções de Ranking: ROW_NUMBER(), RANK() e DENSE_RANK()

Considere quatro servidores avaliados por salário dentro de uma partição: Ana (10.000), Carlos (10.000), Beatriz (10.000) e Daniel (8.000):

| Servidor | Salário | `ROW_NUMBER()` | `RANK()` | `DENSE_RANK()` |
| :--- | :---: | :---: | :---: | :---: |
| Ana | 10.000 | **1** | **1** | **1** |
| Beatriz | 10.000 | **2** | **1** | **1** |
| Carlos | 10.000 | **3** | **1** | **1** |
| Daniel | 8.000 | **4** | **4** *(Pula 2 e 3)* | **2** *(Não pula números)* |

- **`ROW_NUMBER()`:** Atribui um número inteiro sequencial e estritamente exclusivo a cada linha da partição (1, 2, 3, 4..). Desconsidera empates.
- **`RANK()`:** Atribui a mesma posição a valores empatados, porém **pula números na sequência** proporcionalmente ao tamanho do empate (deixa lacunas no ranking).
- **`DENSE_RANK()`:** Atribui a mesma posição a valores empatados, porém **NÃO pula números na sequência**; a numeração subsequente continua estritamente consecutiva (ranking denso sem lacunas).

### 4.3 Funções de Deslocamento: LEAD() e LAG()

Permitem acessar dados de linhas vizinhas na mesma partição sem necessidade de efetuar auto-junções (*self-joins*) lentas:

- **`LAG(coluna, N, valor_padrao)`:** Retorna o valor da coluna correspondente a $N$ linhas **anteriores** à linha corrente.
- **`LEAD(coluna, N, valor_padrao)`:** Retorna o valor da coluna correspondente a $N$ linhas **posteriores** à linha corrente.

---

### Teste 253
**(FCC – TRT-13 – Analista Judiciario Tecnologia da Informacao – 2014)**
Um banco de dados Oracle possui uma tabela chamada processo com os seguintes campos: numero_processo number(5) sequencia_processo number(2) digito_processo number(2) ano_processo number(4) orgao_processo number(1) regiao_processo varchar2(5) vara_processo number(4) Após a tabela ter sido criada, observou-se um requisito informando que campo vara_processo deve permitir apenas valores entre 0 e 28. Para adicionar tal restrição na tabela deve-se digitar a instrução

* **A)** UPDATE TABLE processo ADD CONSTRAINT vara_processo BETWEEN 0 AND 28;
* **B)** INSERT CONSTRAINT processo ADD check_vara CHECK (vara_processo BETWEEN 0 AND 28);
* **C)** ALTER TABLE processo CONSTRAINT (vara_processo>0 AND vara_processo<28);
* **D)** ADD CONSTRAINT processo CHECK vara_processo BETWEEN 0 AND 28;
* **E)** ALTER TABLE processo ADD CONSTRAINT check_vara CHECK (vara_processo BETWEEN 0 AND 28);

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "UPDATE TABLE processo ADD CONSTRAINT vara_processo BETWEEN 0 AND 28". De acordo com a teoria estudada em *Momentos de Disparo (Timing):*, `INSTEAD OF`: Intercepta a instrução DML e executa a rotina do gatilho no lugar da operação original. É a solução canônica para permitir operações de `INSERT`, `UPDATE` e `DELETE` em visões (Views) complexas não-atualizáveis.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "INSERT CONSTRAINT processo ADD check_vara CHECK (vara_processo BETWEEN 0 AND 28)". De acordo com a teoria estudada em *1.3 Restrições de Integridade (Constraints) e Ações de Chave Estrangeira*, `CHECK`: Valida predicados booleanos customizados antes de persistir a tupla (ex.: `CHECK (valor_empenho > 0)`).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "ALTER TABLE processo CONSTRAINT (vara_processo>0 AND vara_processo<28)". De acordo com a teoria estudada em *3.3 Lógica Ternária (Three-Valued Logic) e a Armadilha do NOT IN com NULL*, como o predicado desdobra-se em: `id != 1 AND id != 2 AND id != NULL`, e qualquer comparação com `NULL` resulta em `UNKNOWN`, a expressão inteira avaliará como `UNKNOWN` para todas as linhas!.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "ADD CONSTRAINT processo CHECK vara_processo BETWEEN 0 AND 28". De acordo com a teoria estudada em *3.4 Common Table Expressions (CTEs) e Recursividade (WITH RECURSIVE)*, as Expressões de Tabela Comuns (*CTEs*) são conjuntos de resultados temporários nomeados declarados através da cláusula `WITH`.
> - **E)** **Correta.** Conforme fundamentado na seção *1.1 Classificação ANSI: DDL, DML, DQL, DCL e TCL* deste guia, dDL: *Data Definition Language* — `CREATE`, `ALTER`, `DROP`, `TRUNCATE`, `RENAME` — Criação, modificação estrutural e exclusão física de objetos no catálogo de dados (tabelas, esquemas, índices, visões). Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT-13/2014) ao estabelecer que "ALTER TABLE processo ADD CONSTRAINT check_vara CHECK (vara_processo BETWEEN 0 AND 28)".
>
> **Gabarito: E**

---

### Teste 254
**(FCC – TRT-14 – Analista Judiciario Apoio Especializado Tecnologia da Informacao – 2016)**
Uma tabela de um banco de dados Oracle chamada funcionarios possui os campos id, nome e salario. Um Analista deseja realizar uma consulta nesta tabela, que exiba o id, o nome dos funcionários, o salário e o salário acrescido de 12,5%. O salário com o acréscimo deverá ser mostrado como um número inteiro e a coluna deverá ser nomeada Salário Reajustado. A instrução SQL que deverá ser digitada pelo Analista é

* **A)** SELECT id, nome, salario, TO_INT(salario * 1.125,0) AS "Salário Reajustado" FROM funcionarios;
* **B)** SELECT id, nome, salario, ARRED(salario * 1.125) AS "Salário Reajustado" FROM funcionarios;
* **C)** SELECT id, nome, salario, ROUND(salario * 1.125, 0) "Salário Reajustado" FROM funcionarios;
* **D)** SELECT id, nome, salario, TRUNC(salario * 1.125) 'Salário Reajustado' FROM funcionarios;
* **E)** SELECT id, nome, salario, TO_INTEGER(salario * 1.125) AS "Salário Reajustado" FROM funcionarios;

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "SELECT id, nome, salario, TO_INT(salario * 1.125,0) AS "Salário Reajustado" FROM funcionarios". De acordo com a teoria estudada em *2.2 O Conflito WHERE vs. HAVING e a Ilegalidade de Aliases*, *Código Inválido:* `SELECT salario * 1.1 AS novo_salario FROM servidor WHERE novo_salario > 5000;` *(Gera erro de coluna inexistente!)*.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "SELECT id, nome, salario, ARRED(salario * 1.125) AS "Salário Reajustado" FROM funcionarios". De acordo com a teoria estudada em *5.2 Stored Procedures vs. User-Defined Functions (UDF)*, invocação: Comando explícito `CALL procedure_name(args);` — Invocada inline em comandos SQL: `SELECT func(x) FROM tab;`.
> - **C)** **Correta.** Conforme fundamentado na seção *3.3 Lógica Ternária (Three-Valued Logic) e a Armadilha do NOT IN com NULL* deste guia, considere a consulta: `SELECT nome FROM cliente WHERE id NOT IN (SELECT id_cliente FROM divida);`. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT-14/2016) ao estabelecer que "SELECT id, nome, salario, ROUND(salario * 1.125, 0) "Salário Reajustado" FROM funcionarios".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "SELECT id, nome, salario, TRUNC(salario * 1.125) 'Salário Reajustado' FROM funcionarios". De acordo com a teoria estudada em *5.1 Visões: View Padrão vs. View Materializada (Materialized View)*, trade-off: Os dados ficam estáticos/defasados até que um comando de atualização explícito seja disparado: `REFRESH MATERIALIZED VIEW nome_da_view;`.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "SELECT id, nome, salario, TO_INTEGER(salario * 1.125) AS "Salário Reajustado" FROM funcionarios". De acordo com a teoria estudada em *4.2 Funções de Ranking: ROW_NUMBER(), RANK() e DENSE_RANK()*, considere quatro servidores avaliados por salário dentro de uma partição: Ana (10.000), Carlos (10.000), Beatriz (10.000) e Daniel (8.000).
>
> **Gabarito: C**

---

## 5. Objetos Programáveis de Banco de Dados

### 5.1 Visões: View Padrão vs. View Materializada (Materialized View)

- **View Padrão (Virtual View):**
    - Não armazena dados físicos em disco; representa apenas uma consulta SQL gravada no dicionário de dados do SGBD.
    - A cada execução de um `SELECT` contra a View, o otimizador expande a consulta subjacente e varre as tabelas base em tempo real.
    - Vantagens: Dados sempre 100% atualizados; atua como camada de segurança e abstração (ocultando colunas confidenciais).
- **View Materializada (*Materialized View*):**
    - O resultado da consulta é **gravado e persistido fisicamente em disco** como uma tabela real.
    - Proporciona leituras de altíssima velocidade em consultas analíticas pesadas com múltiplos `JOINs` e agregações complexas.
    - **Trade-off:** Os dados ficam estáticos/defasados até que um comando de atualização explícito seja disparado: `REFRESH MATERIALIZED VIEW nome_da_view;`.

### 5.2 Stored Procedures vs. User-Defined Functions (UDF)

| Dimensão Técnica | Stored Procedure | User-Defined Function (UDF) |
| :--- | :--- | :--- |
| **Invocação** | Comando explícito `CALL procedure_name(args);` | Invocada inline em comandos SQL: `SELECT func(x) FROM tab;` |
| **Retorno Obrigatório** | **Não possui retorno obrigatório** (utiliza parâmetros `OUT`/`INOUT`). | **Exige compulsoriamente a cláusula `RETURNS`** (escalar ou tabela). |
| **Controle Transacional** | **Pode executar `COMMIT` e `ROLLBACK` internamente.** | **Proibido gerenciar transações** dentro da função. |
| **Efeitos Colaterais** | Permite alterar esquemas e dados via DDL e DML livremente. | Deve evitar efeitos colaterais para manter a integridade referencial. |

### 5.3 Gatilhos (Triggers): Eventos, Momentos (BEFORE, AFTER, INSTEAD OF) e Pseudorregistros OLD/NEW

Gatilhos (*Triggers*) são blocos de código procedurais executados automaticamente pelo motor de banco de dados quando eventos DML específicos ocorrem em uma tabela:

#### Pseudorregistros de Contexto:
- **`OLD`:** Representa o estado da linha **antes** da modificação.
    - No `INSERT`: É nulo/indefinido (não existia linha prévia).
    - No `UPDATE`: Contém os valores originais da linha.
    - No `DELETE`: Contém os valores da linha que está sendo removida.
- **`NEW`:** Representa o estado da linha **após** a modificação proposta.
    - No `INSERT`: Contém os valores da nova linha a ser inserida.
    - No `UPDATE`: Contém os novos valores propostos.
    - No `DELETE`: É nulo/indefinido (a linha deixará de existir).

#### Momentos de Disparo (*Timing*):
- **`BEFORE`:** Executado antes que a modificação seja persistida no disco. Ideal para **validação de dados**, enriquecimento de campos e integridade de negócio. Permite alterar os valores de `NEW` antes da gravação.
- **`AFTER`:** Executado após a modificação ser gravada no disco. Ideal para **gravação em tabelas de auditoria** e disparos de notificações assíncronas.
- **`INSTEAD OF`:** Intercepta a instrução DML e executa a rotina do gatilho no lugar da operação original. É a solução canônica para permitir operações de `INSERT`, `UPDATE` e `DELETE` em **visões (Views) complexas não-atualizáveis**.

---

### Teste 255
**(FCC – TRT-13 – Analista Judiciario Tecnologia da Informacao – 2014)**
Em um ambiente de banco de dados Oracle 11g ideal, foram criadas duas tabelas por meio das instruções PL/SQL a seguir: CREATE TABLE orders (order_id NUMBER PRIMARY KEY, line_items_count NUMBER DEFAULT 0 ); CREATE TABLE lineitems (order_id REFERENCES orders, seq_no NUMBER, CONSTRAINT lineitems PRIMARY KEY(order_id,seq_no) ); Foi criada, relacionada às tabelas, a seguinte trigger, colocada em execução: CREATE OR REPLACE TRIGGER lineitems_trigger AFTER INSERT OR UPDATE OR DELETE ON lineitems FOR EACH ROW BEGIN IF (INSERTING OR UPDATING) THEN UPDATE orders SET line_items_count = NVL(line_items_count,0)+1 WHERE order_id = :new.order_id; END IF; IF (DELETING OR UPDATING) THEN UPDATE orders SET line_items_count = NVL(line_items_count,0)-1 WHERE order_id = :old.order_id; END IF; END; / Em seguida, foram executadas as instruções abaixo, nesta ordem: INSERT INTO orders (order_id) VALUES (78); INSERT INTO orders(order_id) VALUES (92); INSERT INTO lineitems (order_id, seq_no) VALUES (78,1); INSERT INTO lineitems (order_id, seq_no) VALUES (78,2); SELECT * FROM orders; Considere: I. Ao executar a instrução INSERT INTO orders (order_id) VALUES (78); a trigger incrementou o valor contido no campo line_items_count passando de 0 para 1. II. Ao executar a instrução INSERT INTO lineitems (order_id, seq_no) VALUES (78,1); a trigger incrementou o valor contido no campo line_items_count da tabela orders passando de 0 para 1. III. Ao executar a instrução INSERT INTO lineitems (order_id, seq_no) VALUES (78,2); a trigger incrementou o valor contido no campo line_items_count da tabela orders passando de 1 para 2. IV. A instrução SELECT * FROM orders; mostrará no campo line_items_count da linha cujo order_id é 78 o valor 3. Está correto o que consta APENAS em

* **A)** I e IV.
* **B)** I.
* **C)** II e IV.
* **D)** II e III.
* **E)** III.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I e IV". De acordo com a teoria estudada em *Momentos de Disparo (Timing):*, `INSTEAD OF`: Intercepta a instrução DML e executa a rotina do gatilho no lugar da operação original. É a solução canônica para permitir operações de `INSERT`, `UPDATE` e `DELETE` em visões (Views) complexas não-atualizáveis.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I". De acordo com a teoria estudada em *Momentos de Disparo (Timing):*, `AFTER`: Executado após a modificação ser gravada no disco. Ideal para gravação em tabelas de auditoria e disparos de notificações assíncronas.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "II e IV". De acordo com a teoria estudada em *3.3 Lógica Ternária (Three-Valued Logic) e a Armadilha do NOT IN com NULL*, considere a consulta: `SELECT nome FROM cliente WHERE id NOT IN (SELECT id_cliente FROM divida);`.
> - **D)** **Correta.** Conforme fundamentado na seção *5.3 Gatilhos (Triggers): Eventos, Momentos (BEFORE, AFTER, INSTEAD OF) e Pseudorregistros OLD/NEW* deste guia, gatilhos (*Triggers*) são blocos de código procedurais executados automaticamente pelo motor de banco de dados quando eventos DML específicos ocorrem em uma tabela. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT-13/2014) ao estabelecer que "II e III".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "III". De acordo com a teoria estudada em *Momentos de Disparo (Timing):*, `BEFORE`: Executado antes que a modificação seja persistida no disco. Ideal para validação de dados, enriquecimento de campos e integridade de negócio. Permite alterar os valores de `NEW` antes da gravação.
>
> **Gabarito: D**

---

