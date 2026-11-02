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

### Teste 001
**(FGV – TCE/GO – 2024 – Analista de Controle Externo - Tecnologia da Informação)**
Considere um banco de dados relacional de um tribunal, na qual nenhum usuário, a menos do DBA, possua algum privilégio sobre. O DBA concedeu direito de criação de tabelas ao usuário USR_0010, que, por sua vez, criou as tabelas DADOS_PROCESSO e DADOS_PARTE. Logo após a criação, o usuário USR_0010 executou os seguintes comandos da DCL (Data Control Language) da linguagem SQL no sistema gerenciador de banco de dados, referentes aos usuários USR_0011 e USR_0100: GRANT SELECT, UPDATE ON DADO_PARTE TO USR_0011; GRANT SELECT ON DADOS_PARTE TO USR_0100; GRANT SELECT, INSERT, DELETE, UPDATE ON DADOS_PROCESSO TO USR_0011; GRANT SELECT, UPDATE ON DADOS_PROCESSO TO USR_0100 WITH GRANT OPTION; Na sequência, o usuário USR_0100 executou o seguinte comando: GRANT UPDATE ON DADOS_PROCESSO TO USR_00101; Por fim, o DBA executou o comando: REVOKE UPDATE ON DADOS_PROCESSO FROM USR_0100; Considerando esse cenário, qual situação é válida para as permissões referentes às tabelas DADOS_PROCESSO e DADOS_PARTE?

* **A)** O usuário USR_0011 tem direito de inserção na tabela DADOS_PARTE.
* **B)** O usuário USR_0100 tem direito de atualização na tabela DADOS_PROCESSO, mas sem direito de propagação.
* **C)** O usuário USR_0100 tem direito de consulta na tabela DADOS_PROCESSO, com direito de propagação.
* **D)** O usuário USR_0101 tem direito de atualização na tabela DADOS_PROCESSO.
* **E)** O usuário USR_0101 tem direito de consulta na tabela DADOS_PROCESSO.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O usuário USR 0011 tem direito de inserção na tabela DADOS PARTE". De acordo com a teoria estudada em *1.1 Classificação ANSI: DDL, DML, DQL, DCL e TCL*, dML: Data Manipulation Language — INSERT , UPDATE , DELETE , MERGE — Inserção, alteração e remoção de registros/tuplas dentro de tabelas existentes.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O usuário USR 0100 tem direito de atualização na tabela DADOS PROCESSO, mas sem direito de propagação". De acordo com a teoria estudada em *1.1 Classificação ANSI: DDL, DML, DQL, DCL e TCL*, dQL: Data Query Language — SELECT — Consulta e recuperação de dados estruturados (frequentemente agrupada como subconjunto da DML).
> - **C)** **Correta.** Conforme fundamentado na seção *1.1 Classificação ANSI: DDL, DML, DQL, DCL e TCL* deste guia, dCL: Data Control Language — GRANT , REVOKE — Gestão de privilégios de acesso, concessão e revogação de permissões a usuários e papéis ( roles ). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/GO/2024) ao estabelecer que "O usuário USR 0100 tem direito de consulta na tabela DADOS PROCESSO, com direito de propagação".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O usuário USR 0101 tem direito de atualização na tabela DADOS PROCESSO". De acordo com a teoria estudada em *1.1 Classificação ANSI: DDL, DML, DQL, DCL e TCL*, dDL: Data Definition Language — CREATE , ALTER , DROP , TRUNCATE , RENAME — Criação, modificação estrutural e exclusão física de objetos no catálogo de dados (tabelas, esquemas, índices, visões).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O usuário USR 0101 tem direito de consulta na tabela DADOS PROCESSO". De acordo com a teoria estudada em *1. Subconjuntos da Linguagem SQL*, sQL DCL["DCL (Controle)<br/ GRANT, REVOKE"].
>
> **Gabarito: C**

---

### Teste 002
**(FGV – TCE/GO – 2024 – Analista de Controle Externo - Tecnologia da Informação)**
A integração de dados desempenha um papel crucial na gestão da informação em organizações. No contexto dos processos de ETL (Extract, Transform, Load), cada etapa desempenha funções específicas. Assinale a opção que descreve corretamente o processo de Transformação (T) no ETL.

* **A)** Etapa em que os dados são carregados em um data warehouse para armazenamento.
* **B)** Fase em que os dados são extraídos de diferentes fontes de dados.
* **C)** Momento em que os dados são preparados para serem apresentados aos usuários finais.
* **D)** Parte do processo em que os dados são indexados espacialmente para otimizar consultas futuras.
* **E)** Passo no qual os dados são limpos, filtrados, agregados ou modificados de acordo com os requisitos de negócios.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Etapa em que os dados são carregados em um data warehouse para armazenamento". De acordo com a teoria estudada em *1.2 O Duelo Clássico: DROP vs. TRUNCATE vs. DELETE*, "O comando TRUNCATE é uma operação DML porque manipula dados de linhas." $\rightarrow$ ERRADO! O TRUNCATE é formalmente classificado como DDL, pois opera desalocando páginas físicas de armazenamento no catálogo de dados.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Fase em que os dados são extraídos de diferentes fontes de dados". De acordo com a teoria estudada em *4. Funções Analíticas de Janela (Window Functions)*, diferente da cláusula GROUP BY (que colapsa múltiplas linhas em um único registro agregado por partição), as funções de janela ( Window Functions ) realizam cálculos agregados e analíticos sem colapsar as tuplas, preservando a identidade e o detalhe de cada linha individual.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Momento em que os dados são preparados para serem apresentados aos usuários finais". De acordo com a teoria estudada em *1.1 Classificação ANSI: DDL, DML, DQL, DCL e TCL*, dCL: Data Control Language — GRANT , REVOKE — Gestão de privilégios de acesso, concessão e revogação de permissões a usuários e papéis ( roles ).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Parte do processo em que os dados são indexados espacialmente para otimizar consultas futuras". De acordo com a teoria estudada em *3.4 Common Table Expressions (CTEs) e Recursividade (WITH RECURSIVE)*, wITH RECURSIVE : Permite que a CTE faça referência a si mesma, viabilizando consultas em estruturas hierárquicas e em grafos (como organogramas empresariais ou árvores de dependência de processos).
> - **E)** **Correta.** Conforme fundamentado na seção *2.2 O Conflito WHERE vs. HAVING e a Ilegalidade de Aliases* deste guia, o HAVING filtra grupos agregados já sumarizados pelo GROUP BY e aceita funções agregadas (ex.: HAVING SUM(valor) 100 ). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/GO/2024) ao estabelecer que "Passo no qual os dados são limpos, filtrados, agregados ou modificados de acordo com os requisitos de negócios".
>
> **Gabarito: E**

---

### Teste 003
**(CEBRASPE – STJ – 2024 – Analista Judiciário - Apoio Especializado - Suporte em Tecnologia da Informação)**
Os bancos de dados dimensionais que atendem ao data warehouse nas fontes transacionais, sem que haja acréscimo de informações devem ser implementados de forma normalizada. transcreva o texto para a FOLHA DE TEXTO DEFINITIVO DA PROVA DISCURSIVA, no local apropriado, pois não será avaliado fragmento de texto escrito em local indevido. • Qualquer fragmento de texto além da extensão máxima de linhas disponibilizadas será desconsiderado. • Na Folha de Texto Definitivo, a presença de qualquer marca identificadora no espaço destinado à transcrição do texto definitivo acarretará a anulação da sua prova discursiva. • Ao domínio do conteúdo serão atribuídos até 40,00 pontos, dos quais até 2,00 pontos serão atribuídos ao quesito apresentação (legibilidade, respeito às margens e indicação de parágrafos) e estrutura textual (organização das ideias em texto estruturado). -- PROVA DISCURSIVA -- A criptografia é um método de segurança que usa algoritmos para proteger informações, transformando-as em um código secreto que só pode ser desbloqueado com uma chave digital. A respeito da criptografia no âmbito da segurança da informação, redija um texto dissertativo atendendo ao que se pede a seguir.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Incorreta.** A proposição promove generalização excessiva que desconsidera as condições técnicas e normativas ao afirmar que "Os bancos de dados dimensionais que atendem ao data warehouse nas fontes transacionais, sem que haja...". De acordo com a teoria em *1.2 O Duelo Clássico: DROP vs. TRUNCATE vs. DELETE*, escopo de Remoção: Linhas filtradas ( WHERE ) ou todas as linhas da tabela. — Todas as linhas da tabela incondicionalmente. — A tabela inteira (estrutura, dados e metadados no catálogo).
> - **E)** **Correta.** O item está **Errado** (gabarito oficial: **E**), pois contraria a disciplina teórica aplicável.
>
> **Gabarito: E**

---

### Teste 004
**(FGV – TJ/AP – 2023 – Analista Judiciario Apoio Especializado Tecnologia Da Informacao Banco De Dados)**
O componente arquitetural de um ambiente de Data Warehouse usado para armazenar temporariamente os dados durante a sua transformação é o(a):

* **A)** log;
* **B)** data mining;
* **C)** stage area;
* **D)** repositório de metadados;
* **E)** cubo de dados.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "log". De acordo com a teoria estudada em *1.2 O Duelo Clássico: DROP vs. TRUNCATE vs. DELETE*, sobrecarga de Log (WAL/Redo): Alto overhead: Registra cada linha excluída individualmente no log de transações. — Mínimo overhead: Registra apenas a desalocação das páginas/extensões no disco. — Mínimo overhead: Registra a remoção do objeto do catálogo de dados.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "data mining". De acordo com a teoria estudada em *1.1 Classificação ANSI: DDL, DML, DQL, DCL e TCL*, dQL: Data Query Language — SELECT — Consulta e recuperação de dados estruturados (frequentemente agrupada como subconjunto da DML).
> - **C)** **Correta.** Conforme fundamentado na seção *1.1 Classificação ANSI: DDL, DML, DQL, DCL e TCL* deste guia, dDL: Data Definition Language — CREATE , ALTER , DROP , TRUNCATE , RENAME — Criação, modificação estrutural e exclusão física de objetos no catálogo de dados (tabelas, esquemas, índices, visões). Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/AP/2023) ao estabelecer que "stage area".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "repositório de metadados". De acordo com a teoria estudada em *1.2 O Duelo Clássico: DROP vs. TRUNCATE vs. DELETE*, escopo de Remoção: Linhas filtradas ( WHERE ) ou todas as linhas da tabela. — Todas as linhas da tabela incondicionalmente. — A tabela inteira (estrutura, dados e metadados no catálogo).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "cubo de dados". De acordo com a teoria estudada em *1.2 O Duelo Clássico: DROP vs. TRUNCATE vs. DELETE*, velocidade de Execução: Lento em grandes volumes de dados (milhões de linhas). — Extremamente rápido (quase instantâneo). — Instantâneo.
>
> **Gabarito: C**

---

### Teste 005
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
> - **A)** **Correta.** Conforme fundamentado na seção *5.3 Gatilhos (Triggers): Eventos, Momentos (BEFORE, AFTER, INSTEAD OF) e Pseudorregistros OLD/NEW* deste guia, gatilhos ( Triggers ) são blocos de código procedurais executados automaticamente pelo motor de banco de dados quando eventos DML específicos ocorrem em uma tabela. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/AP/2023) ao estabelecer que "retornará o nome do usuário com o CPF 99988877766 da tabela “tbl usuario” do banco de dados “prd processo”".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "retornará o nome do usuário com o CPF 99988877766 da tabela “tbl usuario” do banco de dados “prd processo”, se o...". De acordo com a teoria estudada em *1.3 Restrições de Integridade (Constraints) e Ações de Chave Estrangeira*, as restrições de integridade garantem a consistência lógica dos dados no banco.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "retornará o nome do usuário com o CPF 99988877766 da tabela “tbl usuario” do banco de dados “prd processo”, se...". De acordo com a teoria estudada em *5.1 Visões: View Padrão vs. View Materializada (Materialized View)*, trade off: Os dados ficam estáticos/defasados até que um comando de atualização explícito seja disparado: REFRESH MATERIALIZED VIEW nome da view;.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "não retornará o nome do usuário com o CPF 99988877766 da tabela “tbl usuario” do banco de dados “prd processo”...". De acordo com a teoria estudada em *5.2 Stored Procedures vs. User-Defined Functions (UDF)*, efeitos Colaterais: Permite alterar esquemas e dados via DDL e DML livremente. — Deve evitar efeitos colaterais para manter a integridade referencial.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "não retornará o nome do usuário com o CPF 99988877766 da tabela “tbl usuario” do banco de dados “prd processo”...". De acordo com a teoria estudada em *3.3 Lógica Ternária (Three-Valued Logic) e a Armadilha do NOT IN com NULL*, considere a consulta: SELECT nome FROM cliente WHERE id NOT IN (SELECT id cliente FROM divida).
>
> **Gabarito: A**

---

### Teste 006
**(FGV – TJ/AP – 2023 – Analista Judiciario Apoio Especializado Tecnologia Da Informacao Banco De Dados)**
João, administrador de banco de dados MySQL, deverá realizar, periodicamente, o backup lógico completo do banco de dados "tjap_db". Para isso, João deverá utilizar o comando:

* **A)** backup -u root -p tjap_db > backup.sql;
* **B)** mydump -u root -p tjap_db > backup.sql;
* **C)** mybackup -u root -p tjap_db > backup.sql;
* **D)** mysqldump -u root -p tjap_db > backup.sql;
* **E)** select * from tjap_db into outfile backup.sql;

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "backup u root p tjap db backup.sql". De acordo com a teoria estudada em *5.1 Visões: View Padrão vs. View Materializada (Materialized View)*, não armazena dados físicos em disco; representa apenas uma consulta SQL gravada no dicionário de dados do SGBD.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "mydump u root p tjap db backup.sql". De acordo com a teoria estudada em *1.3 Restrições de Integridade (Constraints) e Ações de Chave Estrangeira*, as restrições de integridade garantem a consistência lógica dos dados no banco.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "mybackup u root p tjap db backup.sql". De acordo com a teoria estudada em *5.3 Gatilhos (Triggers): Eventos, Momentos (BEFORE, AFTER, INSTEAD OF) e Pseudorregistros OLD/NEW*, gatilhos ( Triggers ) são blocos de código procedurais executados automaticamente pelo motor de banco de dados quando eventos DML específicos ocorrem em uma tabela.
> - **D)** **Correta.** Conforme fundamentado na seção *5.2 Stored Procedures vs. User-Defined Functions (UDF)* deste guia, invocação: Comando explícito CALL procedure name(args); — Invocada inline em comandos SQL: SELECT func(x) FROM tab. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/AP/2023) ao estabelecer que "mysqldump u root p tjap db backup.sql".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "select from tjap db into outfile backup.sql". De acordo com a teoria estudada em *2.2 O Conflito WHERE vs. HAVING e a Ilegalidade de Aliases*, código Inválido: SELECT salario 1.1 AS novo salario FROM servidor WHERE novo salario 5000; (Gera erro de coluna inexistente!).
>
> **Gabarito: D**

---

### Teste 007
**(FGV – TJ/AP – 2023 – Analista Judiciario Apoio Especializado Tecnologia Da Informacao Banco De Dados)**
Observe a estrutura da tabela “Cliente” abaixo: CREATE TABLE cliente ( cliente_ID NUMBER(12) PRIMARY KEY, cidade VARCHAR2(50) NOT NULL, limite_credito NUMBER(13,2) DEFAULT 0 ); Com o objetivo de gerar um relatório que mostre o limite de crédito médio para clientes em “Sao Paulo” e “Belo Horizonte”, a consulta a ser executada é:

* **A)** SELECT cidade, AVG(NVL(limite_credito,0)) FROM cliente WHERE cidade IN ('SAO PAULO','BELO HORIZONTE');
* **B)** SELECT cidade, AVG(limite_credito) FROM cliente WHERE cidade IN ('SAO PAULO','BELO HORIZONTE') GROUP BY cidade;
* **C)** SELECT cidade, AVG(limite_credito) FROM cliente WHERE cidade IN ('SAO PAULO','BELO HORIZONTE') GROUP BY cliente_ID;
* **D)** SELECT cidade, AVG(limite_credito) FROM cliente WHERE cidade IN ('SAO PAULO','BELO HORIZONTE') GROUP BY cidade, limite_credito;
* **E)** SELECT cidade, AVG(limite_credito) FROM cliente WHERE cidade IN ('SAO PAULO','BELO HORIZONTE') GROUP BY limite_credito, cidade;

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "SELECT cidade, AVG(NVL(limite credito,0)) FROM cliente WHERE cidade IN ('SAO PAULO','BELO HORIZONTE')". De acordo com a teoria estudada em *2.2 O Conflito WHERE vs. HAVING e a Ilegalidade de Aliases*, código Inválido: SELECT salario 1.1 AS novo salario FROM servidor WHERE novo salario 5000; (Gera erro de coluna inexistente!).
> - **B)** **Correta.** Conforme fundamentado na seção *3.3 Lógica Ternária (Three-Valued Logic) e a Armadilha do NOT IN com NULL* deste guia, considere a consulta: SELECT nome FROM cliente WHERE id NOT IN (SELECT id cliente FROM divida). Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/AP/2023) ao estabelecer que "SELECT cidade, AVG(limite credito) FROM cliente WHERE cidade IN ('SAO PAULO','BELO HORIZONTE') GROUP BY cidade".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "SELECT cidade, AVG(limite credito) FROM cliente WHERE cidade IN ('SAO PAULO','BELO HORIZONTE') GROUP BY cliente ID". De acordo com a teoria estudada em *3.3 Lógica Ternária (Three-Valued Logic) e a Armadilha do NOT IN com NULL*, se a tabela divida contiver ao menos UM único registro cujo id cliente seja NULL , a subconsulta retornará o valor NULL.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "SELECT cidade, AVG(limite credito) FROM cliente WHERE cidade IN ('SAO PAULO','BELO HORIZONTE') GROUP BY cidade...". De acordo com a teoria estudada em *2. Ordem Lógica de Execução da Consulta SQL (DQL)*, p1["1. FROM / JOIN / ON<br/ (Identifica tabelas e computa junções)"] P2["2. WHERE<br/ (Filtra tuplas brutas linha a linha)"].
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "SELECT cidade, AVG(limite credito) FROM cliente WHERE cidade IN ('SAO PAULO','BELO HORIZONTE') GROUP BY limite...". De acordo com a teoria estudada em *2.2 O Conflito WHERE vs. HAVING e a Ilegalidade de Aliases*, o HAVING filtra grupos agregados já sumarizados pelo GROUP BY e aceita funções agregadas (ex.: HAVING SUM(valor) 100 ).
>
> **Gabarito: B**

---

### Teste 008
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
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "CREATE TABLE notas aluno (aluno ID NUMBER(12), media notas NUMBER(4,3), CONSTRAINT aluno ID fk REFERENCES...". De acordo com a teoria estudada em *1.3 Restrições de Integridade (Constraints) e Ações de Chave Estrangeira*, pRIMARY KEY : Garante unicidade e impede valores nulos ( UNIQUE + NOT NULL ). Cada tabela pode conter apenas uma chave primária.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "CREATE TABLE notas aluno (aluno ID NUMBER(12), media notas NUMBER(4,3), CONSTRAINT FOREIGN KEY (aluno ID)...". De acordo com a teoria estudada em *1.1 Classificação ANSI: DDL, DML, DQL, DCL e TCL*, dDL: Data Definition Language — CREATE , ALTER , DROP , TRUNCATE , RENAME — Criação, modificação estrutural e exclusão física de objetos no catálogo de dados (tabelas, esquemas, índices, visões).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "CREATE TABLE notas aluno (aluno ID NUMBER(12), media notas NUMBER(4,3), aluno ID fk FOREIGN KEY (aluno ID)...". De acordo com a teoria estudada em *1. Subconjuntos da Linguagem SQL*, sQL DDL["DDL (Definição)<br/ CREATE, ALTER, DROP, TRUNCATE"].
> - **D)** **Correta.** Conforme fundamentado na seção *1.3 Restrições de Integridade (Constraints) e Ações de Chave Estrangeira* deste guia, fOREIGN KEY (Integridade Referencial): Impõe que o valor da coluna exista previamente na chave primária da tabela referenciada. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/AP/2023) ao estabelecer que "CREATE TABLE notas aluno (aluno ID NUMBER(12), media notas NUMBER(4,3), CONSTRAINT aluno ID fk FOREIGN KEY (aluno...".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "CREATE TABLE notas aluno (aluno ID NUMBER(12), media notas NUMBER(4,3), CONSTRAINT aluno ID fk REFERENCES (aluno...". De acordo com a teoria estudada em *1.3 Restrições de Integridade (Constraints) e Ações de Chave Estrangeira*, as restrições de integridade garantem a consistência lógica dos dados no banco.
>
> **Gabarito: D**

---

### Teste 009
**(CEBRASPE – TRF/6 – 2025 – Analista Judiciario Apoio Especializado Tecnologia Da Informacao)**
A arquitetura de bancos de dados cliente-servidor é caracterizada pela divisão do processamento entre sistemas, e sua implementação requer soluções de software que possibilitem confirmar transações, desfazer transações e disponibilizar linguagens de consultas. SELECT * FROM Produtos WHERE Preco > 0.00;

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Correta.** O item está **Certo**. Conforme fundamentado na seção *2.2 O Conflito WHERE vs. HAVING e a Ilegalidade de Aliases*, código Inválido: SELECT salario 1.1 AS novo salario FROM servidor WHERE novo salario 5000; (Gera erro de coluna inexistente!). Dessa forma, está plenamente correta a assertiva da banca (CEBRASPE – TRF/6/2025) ao afirmar que "A arquitetura de bancos de dados cliente servidor é caracterizada pela divisão do processamento entre...".
> - **E)** **Incorreta.** A assertiva não incorre em erro conceitual, guardando conformidade com a teoria estudada.
>
> **Gabarito: C**

---

### Teste 010
**(FCC – TRT 14ª – 2016 – Analista Judiciário - Apoio Especializado - Tecnologia da Informação)**
Uma tabela de um banco de dados Oracle chamada funcionarios possui os campos id, nome e salario. Um Analista deseja realizar uma consulta nesta tabela, que exiba o id, o nome dos funcionários, o salário e o salário acrescido de 12,5%. O salário com o acréscimo deverá ser mostrado como um número inteiro e a coluna deverá ser nomeada Salário Reajustado. A instrução SQL que deverá ser digitada pelo Analista é

* **A)** SELECT id, nome, salario, TO_INT(salario * 1.125,0) AS "Salário Reajustado" FROM funcionarios;
* **B)** SELECT id, nome, salario, ARRED(salario * 1.125) AS "Salário Reajustado" FROM funcionarios;
* **C)** SELECT id, nome, salario, ROUND(salario * 1.125, 0) "Salário Reajustado" FROM funcionarios;
* **D)** SELECT id, nome, salario, TRUNC(salario * 1.125) 'Salário Reajustado' FROM funcionarios;
* **E)** SELECT id, nome, salario, TO_INTEGER(salario * 1.125) AS "Salário Reajustado" FROM funcionarios;

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *3.3 Lógica Ternária (Three-Valued Logic) e a Armadilha do NOT IN com NULL* deste guia, considere a consulta: SELECT nome FROM cliente WHERE id NOT IN (SELECT id cliente FROM divida). Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 14ª/2016) ao estabelecer que "SELECT id, nome, salario, TO INT(salario 1.125,0) AS "Salário Reajustado" FROM funcionarios".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "SELECT id, nome, salario, ARRED(salario 1.125) AS "Salário Reajustado" FROM funcionarios". De acordo com a teoria estudada em *2.2 O Conflito WHERE vs. HAVING e a Ilegalidade de Aliases*, código Inválido: SELECT salario 1.1 AS novo salario FROM servidor WHERE novo salario 5000; (Gera erro de coluna inexistente!).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "SELECT id, nome, salario, ROUND(salario 1.125, 0) "Salário Reajustado" FROM funcionarios". De acordo com a teoria estudada em *5.1 Visões: View Padrão vs. View Materializada (Materialized View)*, trade off: Os dados ficam estáticos/defasados até que um comando de atualização explícito seja disparado: REFRESH MATERIALIZED VIEW nome da view;.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "SELECT id, nome, salario, TRUNC(salario 1.125) 'Salário Reajustado' FROM funcionarios". De acordo com a teoria estudada em *5.2 Stored Procedures vs. User-Defined Functions (UDF)*, invocação: Comando explícito CALL procedure name(args); — Invocada inline em comandos SQL: SELECT func(x) FROM tab.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "SELECT id, nome, salario, TO INTEGER(salario 1.125) AS "Salário Reajustado" FROM funcionarios". De acordo com a teoria estudada em *4.2 Funções de Ranking: ROW_NUMBER(), RANK() e DENSE_RANK()*, considere quatro servidores avaliados por salário dentro de uma partição: Ana (10.000), Carlos (10.000), Beatriz (10.000) e Daniel (8.000).
>
> **Gabarito: A**

---

### Teste 011
**(FCC – TRT 14ª – 2016 – Analista Judiciário - Apoio Especializado - Tecnologia da Informação)**
No Oracle 11g há uma instrução que permite atualizar, inserir ou remover linhas condicionalmente em uma tabela, evitando o uso de várias instruções DML. Esta instrução é especialmente útil nas aplicações em ambientes de Data Warehouse, nas quais é preciso trabalhar com dados provenientes de várias origens. Trata-se da instrução

* **A)** SWITCH.
* **B)** TRUNCATE.
* **C)** MERGE.
* **D)** IFCOMMAND.
* **E)** EXEC.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "SWITCH". De acordo com a teoria estudada em *1.1 Classificação ANSI: DDL, DML, DQL, DCL e TCL*, dDL: Data Definition Language — CREATE , ALTER , DROP , TRUNCATE , RENAME — Criação, modificação estrutural e exclusão física de objetos no catálogo de dados (tabelas, esquemas, índices, visões).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "TRUNCATE". De acordo com a teoria estudada em *1.2 O Duelo Clássico: DROP vs. TRUNCATE vs. DELETE*, escopo de Remoção: Linhas filtradas ( WHERE ) ou todas as linhas da tabela. — Todas as linhas da tabela incondicionalmente. — A tabela inteira (estrutura, dados e metadados no catálogo).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "MERGE". De acordo com a teoria estudada em *1.1 Classificação ANSI: DDL, DML, DQL, DCL e TCL*, dML: Data Manipulation Language — INSERT , UPDATE , DELETE , MERGE — Inserção, alteração e remoção de registros/tuplas dentro de tabelas existentes.
> - **D)** **Correta.** Conforme fundamentado na seção *5.2 Stored Procedures vs. User-Defined Functions (UDF)* deste guia, efeitos Colaterais: Permite alterar esquemas e dados via DDL e DML livremente. — Deve evitar efeitos colaterais para manter a integridade referencial. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 14ª/2016) ao estabelecer que "IFCOMMAND".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "EXEC". De acordo com a teoria estudada em *1.1 Classificação ANSI: DDL, DML, DQL, DCL e TCL*, dQL: Data Query Language — SELECT — Consulta e recuperação de dados estruturados (frequentemente agrupada como subconjunto da DML).
>
> **Gabarito: D**

---

### Teste 012
**(FCC – TRT 23ª – 2016 – Analista Judiciário - Apoio Especializado - Tecnologia da Informação)**
Na abordagem Star Schema, usada para modelar data warehouses, os fatos são representados na tabela de fatos, que normalmente

* **A)** o tempo decorrido entre as iterações de um processo recursivo.
* **B)** as interações entre as atividades, no tempo.
* **C)** os casos de uso de cada objeto.
* **D)** os períodos de ativação do objeto.
* **E)** as etapas em que o objeto estará inativo.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *5.1 Visões: View Padrão vs. View Materializada (Materialized View)* deste guia, a cada execução de um SELECT contra a View, o otimizador expande a consulta subjacente e varre as tabelas base em tempo real. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 23ª/2016) ao estabelecer que "o tempo decorrido entre as iterações de um processo recursivo".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "as interações entre as atividades, no tempo". De acordo com a teoria estudada em *1.1 Classificação ANSI: DDL, DML, DQL, DCL e TCL*, dDL: Data Definition Language — CREATE , ALTER , DROP , TRUNCATE , RENAME — Criação, modificação estrutural e exclusão física de objetos no catálogo de dados (tabelas, esquemas, índices, visões).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "os casos de uso de cada objeto". De acordo com a teoria estudada em *1.2 O Duelo Clássico: DROP vs. TRUNCATE vs. DELETE*, sobrecarga de Log (WAL/Redo): Alto overhead: Registra cada linha excluída individualmente no log de transações. — Mínimo overhead: Registra apenas a desalocação das páginas/extensões no disco. — Mínimo overhead: Registra a remoção do objeto do catálogo de dados.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "os períodos de ativação do objeto". De acordo com a teoria estudada em *1.1 Classificação ANSI: DDL, DML, DQL, DCL e TCL*, dML: Data Manipulation Language — INSERT , UPDATE , DELETE , MERGE — Inserção, alteração e remoção de registros/tuplas dentro de tabelas existentes.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "as etapas em que o objeto estará inativo". De acordo com a teoria estudada em *1.1 Classificação ANSI: DDL, DML, DQL, DCL e TCL*, dQL: Data Query Language — SELECT — Consulta e recuperação de dados estruturados (frequentemente agrupada como subconjunto da DML).
>
> **Gabarito: A**

---

### Teste 013
**(FCC – TRT 23ª – 2016 – Analista Judiciário - Apoio Especializado - Tecnologia da Informação)**
Para utilizar o OpenSource Selenium, um Analista deve conhecer suas atuais e principais ferramentas. Uma delas é a que permite distribuir os testes em múltiplas máquinas, reduzindo assim o tempo gasto na execução de uma suíte de testes. É ideal para escalonar suítes de testes grandes ou que devem ser executadas em múltiplos ambientes. Essa ferramenta é o Selenium

* **A)** SELECT.
* **B)** RC.
* **C)** IDE.
* **D)** TYPE.
* **E)** GRID.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *5.1 Visões: View Padrão vs. View Materializada (Materialized View)* deste guia, a cada execução de um SELECT contra a View, o otimizador expande a consulta subjacente e varre as tabelas base em tempo real. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 23ª/2016) ao estabelecer que "SELECT".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "RC". De acordo com a teoria estudada em *2. Ordem Lógica de Execução da Consulta SQL (DQL)*, ao escrever uma consulta com a cláusula SELECT , a ordem sintática da escrita (ordem léxica) é muito diferente da ordem lógica de processamento adotada pelo otimizador de consultas do SGBD.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "IDE". De acordo com a teoria estudada em *2. Ordem Lógica de Execução da Consulta SQL (DQL)*, p5 P6["6. SELECT<br/ (Calcula expressões e aliases de colunas)"].
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "TYPE". De acordo com a teoria estudada em *Momentos de Disparo (Timing):*, aFTER : Executado após a modificação ser gravada no disco. Ideal para gravação em tabelas de auditoria e disparos de notificações assíncronas.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "GRID". De acordo com a teoria estudada em *5.2 Stored Procedures vs. User-Defined Functions (UDF)*, efeitos Colaterais: Permite alterar esquemas e dados via DDL e DML livremente. — Deve evitar efeitos colaterais para manter a integridade referencial.
>
> **Gabarito: A**

---

### Teste 014
**(FGV – TRT 16ª – 2022 – Analista Judiciário (Área Administrativa - Tecnologia da Informação))**
O cmdlet do Powershell no Windows 10 capaz de exibir o modelo e o fabricante de uma máquina é o

* **A)** Get-CimInstance - ClassName Win32_QuickFixEngineering - Property HotFixID.
* **B)** Get-CimInstance - ClassName Win32_LogonSession.
* **C)** Get-CimInstance - ClassName Win32_ComputerSystem.
* **D)** Get-CimInstance - ClassName Win32_OperatingSystem | Select-Object - Property BuildNumber, BuildType, OSType, ServicePackMajorVersion, ServicePackMinorVersion.
* **E)** Get-CimInstance - ClassName Win32_BIOS.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Get CimInstance ClassName Win32 QuickFixEngineering Property HotFixID". De acordo com a teoria estudada em *1. Subconjuntos da Linguagem SQL*, sQL DDL["DDL (Definição)<br/ CREATE, ALTER, DROP, TRUNCATE"].
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Get CimInstance ClassName Win32 LogonSession". De acordo com a teoria estudada em *1. Subconjuntos da Linguagem SQL*, sQL DML["DML (Manipulação)<br/ INSERT, UPDATE, DELETE"].
> - **C)** **Correta.** Conforme fundamentado na seção *1. Subconjuntos da Linguagem SQL* deste guia, a linguagem SQL ( Structured Query Language ), padronizada internacionalmente pela norma ISO/IEC 9075, é subdividida em conjuntos de comandos com finalidades operacionais distintas. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT 16ª/2022) ao estabelecer que "Get CimInstance ClassName Win32 ComputerSystem".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Get CimInstance ClassName Win32 OperatingSystem | Select Object Property BuildNumber, BuildType, OSType...". De acordo com a teoria estudada em *1. Subconjuntos da Linguagem SQL*, sQL DQL["DQL (Consulta)<br/ SELECT"].
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Get CimInstance ClassName Win32 BIOS". De acordo com a teoria estudada em *1. Subconjuntos da Linguagem SQL*, sQL DCL["DCL (Controle)<br/ GRANT, REVOKE"].
>
> **Gabarito: C**

---

### Teste 015
**(CEBRASPE – STF – 2008 – Analista Judiciario Suporte Em Tecnologia Da Informacao)**
As características do atributo CEP — numérico, seqüencial e não repetido — permitem utilizá-lo como chave primária em um banco de dados destinado ao cadastro de clientes de uma loja.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Incorreta.** A proposição apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "As características do atributo CEP — numérico, seqüencial e não repetido — permitem utilizá lo como chave...". De acordo com a teoria em *1.3 Restrições de Integridade (Constraints) e Ações de Chave Estrangeira*, as restrições de integridade garantem a consistência lógica dos dados no banco.
> - **E)** **Correta.** O item está **Errado** (gabarito oficial: **E**), pois contraria a disciplina teórica aplicável.
>
> **Gabarito: E**

---

### Teste 016
**(CEBRASPE – STF – 2013 – Analista Judiciario Suporte Em Tecnologia Da Informacao)**
No modelo entidade/relacionamento, deve-se incluir a chave estrangeira (chave primária) de uma entidade como campo da outra para modelar o relacionamento entre elas.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Incorreta.** A proposição apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "No modelo entidade/relacionamento, deve se incluir a chave estrangeira (chave primária) de uma entidade como...". De acordo com a teoria em *1.3 Restrições de Integridade (Constraints) e Ações de Chave Estrangeira*, sET NULL : Atualiza o campo da chave estrangeira dos filhos para NULL quando o pai é excluído (exige que a coluna aceite nulos).
> - **E)** **Correta.** O item está **Errado** (gabarito oficial: **E**), pois contraria a disciplina teórica aplicável.
>
> **Gabarito: E**

---

### Teste 017
**(FGV – TJ/BA – 2015 – Analista Judiciario Tecnologia Da Informacao)**
O comando switch da linguagem de programação C é, na linguagem Visual Basic .NET, semelhante ao comando:

* **A)** Select Case;
* **B)** Exit;
* **C)** For Each;
* **D)** Goto;
* **E)** Continue.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *5.2 Stored Procedures vs. User-Defined Functions (UDF)* deste guia, invocação: Comando explícito CALL procedure name(args); — Invocada inline em comandos SQL: SELECT func(x) FROM tab. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/BA/2015) ao estabelecer que "Select Case".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Exit". De acordo com a teoria estudada em *1. Subconjuntos da Linguagem SQL*, sQL DQL["DQL (Consulta)<br/ SELECT"].
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "For Each". De acordo com a teoria estudada em *1.2 O Duelo Clássico: DROP vs. TRUNCATE vs. DELETE*, "O comando TRUNCATE aciona gatilhos de auditoria FOR EACH ROW para registrar quem apagou cada linha." $\rightarrow$ ERRADO! O TRUNCATE ignora completamente gatilhos de nível de linha!.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Goto". De acordo com a teoria estudada em *1.1 Classificação ANSI: DDL, DML, DQL, DCL e TCL*, dQL: Data Query Language — SELECT — Consulta e recuperação de dados estruturados (frequentemente agrupada como subconjunto da DML).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Continue". De acordo com a teoria estudada em *2. Ordem Lógica de Execução da Consulta SQL (DQL)*, ao escrever uma consulta com a cláusula SELECT , a ordem sintática da escrita (ordem léxica) é muito diferente da ordem lógica de processamento adotada pelo otimizador de consultas do SGBD.
>
> **Gabarito: A**

---

### Teste 018
**(FGV – TJ/BA – 2015 – Analista Judiciario Tecnologia Da Informacao)**
Analise o diagrama ER apresentado a seguir. Na implementação relacional desse modelo, é necessário que:

* **A)** o relacionamento entre T1 e T2 seja modificado, pois não é possível implementá-lo como descrito;
* **B)** o atributo C1 da tabela T1 seja declarado como uma chave estrangeira que referencia a tabela T2;
* **C)** o atributo C da tabela T2 seja declarado com a propriedade unique (com valores nulos ignorados);
* **D)** o atributo A2 da tabela T2 aceite valores nulos;
* **E)** o atributo C da tabela T2 seja declarado com a propriedade not null.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "o relacionamento entre T1 e T2 seja modificado, pois não é possível implementá lo como descrito". De acordo com a teoria estudada em *1.3 Restrições de Integridade (Constraints) e Ações de Chave Estrangeira*, uNIQUE : Impede valores duplicados, mas permite a inserção de valores nulos ( NULL ), exceto se combinado com NOT NULL.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "o atributo C1 da tabela T1 seja declarado como uma chave estrangeira que referencia a tabela T2". De acordo com a teoria estudada em *1.3 Restrições de Integridade (Constraints) e Ações de Chave Estrangeira*, sET NULL : Atualiza o campo da chave estrangeira dos filhos para NULL quando o pai é excluído (exige que a coluna aceite nulos).
> - **C)** **Correta.** Conforme fundamentado na seção *1.3 Restrições de Integridade (Constraints) e Ações de Chave Estrangeira* deste guia, pRIMARY KEY : Garante unicidade e impede valores nulos ( UNIQUE + NOT NULL ). Cada tabela pode conter apenas uma chave primária. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/BA/2015) ao estabelecer que "o atributo C da tabela T2 seja declarado com a propriedade unique (com valores nulos ignorados)".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "o atributo A2 da tabela T2 aceite valores nulos". De acordo com a teoria estudada em *3.1 Junções (INNER, LEFT, RIGHT, FULL OUTER e CROSS JOIN)*, lEFT OUTER JOIN (ou LEFT JOIN ): Retorna todas as tuplas da tabela à esquerda ( FROM ), combinando com as tuplas da tabela à direita. Caso não haja correspondência na tabela da direita, os atributos da direita são preenchidos com valores nulos ( NULL ).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "o atributo C da tabela T2 seja declarado com a propriedade not null". De acordo com a teoria estudada em *3.3 Lógica Ternária (Three-Valued Logic) e a Armadilha do NOT IN com NULL*, solução Recomendada: Utilizar sempre a construção com NOT EXISTS correlacionado, imune a valores nulos.
>
> **Gabarito: C**

---

### Teste 019
**(FGV – TJ/BA – 2015 – Analista Judiciario Tecnologia Da Informacao)**
Considere as seguintes dependências funcionais sobre os atributos A, B, C e D de uma tabela relacional, listadas a seguir. AB AC CD A dependência funcional que NÃO pode ser derivada das dependências acima é:

* **A)** BC
* **B)** AD
* **C)** AB,C
* **D)** A,B,CA,B
* **E)** C,BD,B

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *1.3 Restrições de Integridade (Constraints) e Ações de Chave Estrangeira* deste guia, pRIMARY KEY : Garante unicidade e impede valores nulos ( UNIQUE + NOT NULL ). Cada tabela pode conter apenas uma chave primária. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/BA/2015) ao estabelecer que "BC".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "AD". De acordo com a teoria estudada em *3.1 Junções (INNER, LEFT, RIGHT, FULL OUTER e CROSS JOIN)*, lEFT OUTER JOIN (ou LEFT JOIN ): Retorna todas as tuplas da tabela à esquerda ( FROM ), combinando com as tuplas da tabela à direita. Caso não haja correspondência na tabela da direita, os atributos da direita são preenchidos com valores nulos ( NULL ).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "AB,C". De acordo com a teoria estudada em *2.1 Ordem Léxica (Escrita) vs. Ordem Lógica (Processamento)*, a ordem lógica executada pelo motor relacional é rigorosamente.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A,B,CA,B". De acordo com a teoria estudada em *3.4 Common Table Expressions (CTEs) e Recursividade (WITH RECURSIVE)*, wITH RECURSIVE : Permite que a CTE faça referência a si mesma, viabilizando consultas em estruturas hierárquicas e em grafos (como organogramas empresariais ou árvores de dependência de processos).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "C,BD,B". De acordo com a teoria estudada em *3.1 Junções (INNER, LEFT, RIGHT, FULL OUTER e CROSS JOIN)*, fULL OUTER JOIN : Preserva todas as tuplas de ambas as tabelas. Quando não há correspondência mútua, preenche com NULL os atributos correspondentes.
>
> **Gabarito: A**

---

### Teste 020
**(FCC – TRT 11ª – 2017 – Analista Judiciário - Tecnologia da Informação)**
Considere a imagem abaixo, que mostra uma arquitetura de armazenamento baseada em informações. Nessa arquitetura, as lacunas I e II são preenchidas, correta e respectivamente, com

* **A)** será necessária a criação de uma tabela entre Advogado e Processo e o relacionamento N:N dará lugar a dois relacionamentos 1:N.
* **B)** a chave primária da tabela Processo deverá ser chave estrangeira na tabela Advogado.
* **C)** a chave primária da tabela Advogado deverá ser chave estrangeira na tabela Processo.
* **D)** ambas as tabelas (Processo e Advogado) deverão ter chave primária composta.
* **E)** a tabela Advogado deverá ter um campo para especificar o tipo de atuação do advogado em cada processo (defesa ou acusação).

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "será necessária a criação de uma tabela entre Advogado e Processo e o relacionamento N:N dará lugar a dois...". De acordo com a teoria estudada em *1.3 Restrições de Integridade (Constraints) e Ações de Chave Estrangeira*, fOREIGN KEY (Integridade Referencial): Impõe que o valor da coluna exista previamente na chave primária da tabela referenciada.
> - **B)** **Correta.** Conforme fundamentado na seção *1.3 Restrições de Integridade (Constraints) e Ações de Chave Estrangeira* deste guia, pRIMARY KEY : Garante unicidade e impede valores nulos ( UNIQUE + NOT NULL ). Cada tabela pode conter apenas uma chave primária. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 11ª/2017) ao estabelecer que "a chave primária da tabela Processo deverá ser chave estrangeira na tabela Advogado".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "a chave primária da tabela Advogado deverá ser chave estrangeira na tabela Processo". De acordo com a teoria estudada em *1.3 Restrições de Integridade (Constraints) e Ações de Chave Estrangeira*, as restrições de integridade garantem a consistência lógica dos dados no banco.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "ambas as tabelas (Processo e Advogado) deverão ter chave primária composta". De acordo com a teoria estudada em *Momentos de Disparo (Timing):*, aFTER : Executado após a modificação ser gravada no disco. Ideal para gravação em tabelas de auditoria e disparos de notificações assíncronas.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "a tabela Advogado deverá ter um campo para especificar o tipo de atuação do advogado em cada processo (defesa ou...". De acordo com a teoria estudada em *1.3 Restrições de Integridade (Constraints) e Ações de Chave Estrangeira*, sET NULL : Atualiza o campo da chave estrangeira dos filhos para NULL quando o pai é excluído (exige que a coluna aceite nulos).
>
> **Gabarito: B**

---

### Teste 021
**(FCC – TRT 15ª – 2015 – Analista Judiciário - Tecnologia da Informação)**
No contexto de Business Intelligence, os sistemas OLAP e OLTP se diferenciam em diversas características. Na tabela abaixo, no que diz respeito às características, está INCORRETO: Característica OLAP OLTP Alta velocidade na manipulação de dados operacio- Otimização para leitura e geração de análise e

* **A)** Performance. nais, porém ineficiente para geração de análises relatórios gerenciais. gerenciais. Tipo de permissões É permitido apenas inserção e leitura. Para o Podem ser feitas leitura, inserção, modificação e ex-
* **B)** nos dados. usuário está disponível apenas a leitura. clusão de dados. Armazenamento feito em Data Warehouse com Armazenamento feito em bancos de dados conven-
* **C)** Estrutura dos dados. otimização no desempenho em grandes volumes cionais pelos sistemas de informação da organização. de dados. Nível operacional da organização. Visa a exe- Nível estratégico da organização. Visa a análise
* **D)** Foco. cução operacional do negócio. empresarial e tomada de decisão. Dados históricos e não voláteis que praticamente
* **E)** Volatilidade. não sofrem alterações salvo em casos específi- Dados voláteis, passíveis de modificação e exclusão. Atenção: Conforme Edital do Concurso, Capítulo X, itens: “8. ... a Prova Estudo de Caso terá caráter eliminatório e classificatório. Cada uma das questões será avaliada na escala de 0 (zero) a 100 (cem) pontos, considerando-se habilitado o candidato que tiver obtido, no conjunto das duas questões, média igual ou superior a 50 (cinquenta).

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *Momentos de Disparo (Timing):* deste guia, aFTER : Executado após a modificação ser gravada no disco. Ideal para gravação em tabelas de auditoria e disparos de notificações assíncronas. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 15ª/2015) ao estabelecer que "Performance. nais, porém ineficiente para geração de análises relatórios gerenciais. gerenciais. Tipo de...".
> - **B)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "nos dados. usuário está disponível apenas a leitura. clusão de dados. Armazenamento feito em Data Warehouse com...". De acordo com a teoria estudada em *1.1 Classificação ANSI: DDL, DML, DQL, DCL e TCL*, dDL: Data Definition Language — CREATE , ALTER , DROP , TRUNCATE , RENAME — Criação, modificação estrutural e exclusão física de objetos no catálogo de dados (tabelas, esquemas, índices, visões).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Estrutura dos dados. otimização no desempenho em grandes volumes cionais pelos sistemas de informação da...". De acordo com a teoria estudada em *1.2 O Duelo Clássico: DROP vs. TRUNCATE vs. DELETE*, velocidade de Execução: Lento em grandes volumes de dados (milhões de linhas). — Extremamente rápido (quase instantâneo). — Instantâneo.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Foco. cução operacional do negócio. empresarial e tomada de decisão. Dados históricos e não voláteis que...". De acordo com a teoria estudada em *Momentos de Disparo (Timing):*, bEFORE : Executado antes que a modificação seja persistida no disco. Ideal para validação de dados, enriquecimento de campos e integridade de negócio. Permite alterar os valores de NEW antes da gravação.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Volatilidade. não sofrem alterações salvo em casos específi Dados voláteis, passíveis de modificação e exclusão...". De acordo com a teoria estudada em *3.2 Operadores de Conjunto (UNION vs. UNION ALL, INTERSECT, EXCEPT)*, uNION ALL : Apenas concatena as duas listas de tuplas, preservando todas as duplicatas intactas. Possui desempenho computacional dramaticamente superior ao UNION.
>
> **Gabarito: A**

---

### Teste 022
**(FCC – TRT 2ª – 2014 – Analista Judiciário - Tecnologia da Informação)**
No banco de dados MySQL, uma das maneiras de se efetuar uma consulta na qual uma determinada coluna de uma tabela seja igual ao valor máximo de uma coluna de outra tabela é

* **A)** SELECT * FROM t1 WHERE colunaX = (SELECT MAX(colunaY) FROM t2);
* **B)** SELECT * FROM t1 WHERE COALESCE(t1.colunaY, t2colunaY);
* **C)** SELECT colunaX from t1 IN MAX(SELECT colunaY from t2);
* **D)** SELECT CASE WHEN colunaX = (SELECT colunaY from t2) AS c WHERE c = colunaX;
* **E)** SELECT colunaX, colunaY from t1 WHER colunaX = colunaY;

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *2.2 O Conflito WHERE vs. HAVING e a Ilegalidade de Aliases* deste guia, código Inválido: SELECT salario 1.1 AS novo salario FROM servidor WHERE novo salario 5000; (Gera erro de coluna inexistente!). Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 2ª/2014) ao estabelecer que "SELECT FROM t1 WHERE colunaX = (SELECT MAX(colunaY) FROM t2)".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "SELECT FROM t1 WHERE COALESCE(t1.colunaY, t2colunaY)". De acordo com a teoria estudada em *3.3 Lógica Ternária (Three-Valued Logic) e a Armadilha do NOT IN com NULL*, considere a consulta: SELECT nome FROM cliente WHERE id NOT IN (SELECT id cliente FROM divida).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "SELECT colunaX from t1 IN MAX(SELECT colunaY from t2)". De acordo com a teoria estudada em *2. Ordem Lógica de Execução da Consulta SQL (DQL)*, p1["1. FROM / JOIN / ON<br/ (Identifica tabelas e computa junções)"] P2["2. WHERE<br/ (Filtra tuplas brutas linha a linha)"].
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "SELECT CASE WHEN colunaX = (SELECT colunaY from t2) AS c WHERE c = colunaX". De acordo com a teoria estudada em *2.2 O Conflito WHERE vs. HAVING e a Ilegalidade de Aliases*, como a cláusula WHERE (etapa 2) é processada muito antes da cláusula SELECT (etapa 6), qualquer apelido de coluna ( alias ) criado no SELECT ainda não existe no catálogo de símbolos durante a avaliação do WHERE.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "SELECT colunaX, colunaY from t1 WHER colunaX = colunaY". De acordo com a teoria estudada em *5.2 Stored Procedures vs. User-Defined Functions (UDF)*, invocação: Comando explícito CALL procedure name(args); — Invocada inline em comandos SQL: SELECT func(x) FROM tab.
>
> **Gabarito: A**

---

### Teste 023
**(FCC – TRT 24ª – 2017 – Analista Judiciário - Tecnologia da Informação)**
Uma das formas de apresentação de um banco de dados multidimensional é através do modelo estrela. No centro de um mode- lo estrela encontra-se a tabela de

* **A)** fatos, cuja chave primária deve ser simples.
* **B)** fatos e, ao seu redor, as tabelas de dimensões.
* **C)** dimensão e, ao seu redor, as tabelas de fatos.
* **D)** dimensão, cuja chave primária deve ser composta.
* **E)** núcleo e, ao seu redor, as tabelas de nível.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "fatos, cuja chave primária deve ser simples". De acordo com a teoria estudada em *1.3 Restrições de Integridade (Constraints) e Ações de Chave Estrangeira*, fOREIGN KEY (Integridade Referencial): Impõe que o valor da coluna exista previamente na chave primária da tabela referenciada.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "fatos e, ao seu redor, as tabelas de dimensões". De acordo com a teoria estudada em *Momentos de Disparo (Timing):*, aFTER : Executado após a modificação ser gravada no disco. Ideal para gravação em tabelas de auditoria e disparos de notificações assíncronas.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "dimensão e, ao seu redor, as tabelas de fatos". De acordo com a teoria estudada em *5.2 Stored Procedures vs. User-Defined Functions (UDF)*, efeitos Colaterais: Permite alterar esquemas e dados via DDL e DML livremente. — Deve evitar efeitos colaterais para manter a integridade referencial.
> - **D)** **Correta.** Conforme fundamentado na seção *1.3 Restrições de Integridade (Constraints) e Ações de Chave Estrangeira* deste guia, pRIMARY KEY : Garante unicidade e impede valores nulos ( UNIQUE + NOT NULL ). Cada tabela pode conter apenas uma chave primária. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 24ª/2017) ao estabelecer que "dimensão, cuja chave primária deve ser composta".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "núcleo e, ao seu redor, as tabelas de nível". De acordo com a teoria estudada em *1.3 Restrições de Integridade (Constraints) e Ações de Chave Estrangeira*, as restrições de integridade garantem a consistência lógica dos dados no banco.
>
> **Gabarito: D**

---

### Teste 024
**(FCC – TRT 3ª – 2015 – Analista Judiciário - Tecnologia da Informação)**
O Java EE pode ser organizado em três conjuntos de padrões de projeto, de acordo com as camadas da arquitetura JEE: Padrões da Camada de Apresentação (Web Tier Patterns), Padrões da Camada de Negócio (Business Tier Patterns) e Padrões da Camada de Integração (EIS Tier Patterns). São padrões de projeto da Camada de Apresentação:

* **A)** os dados de todos de todos os funcionários cujos nomes possuam a letra a como segundo caractere, utiliza-se a instrução SELECT * FROM emp WHERE nome LIKE '_a%';
* **B)** os dados dos funcionários cujo nome seja 'Pedro' ou 'Ana' utiliza-se a instrução SELECT * FROM emp WHERE nome LIKE ('Pedro','Ana');
* **C)** os dados de todos os funcionários cujo conteúdo do campo salario esteja entre 1000 e 2000 utiliza-se a instrução SELECT * FROM emp WHERE salario BETWEEN (1000,2000);
* **D)** os dados dos funcionários cujo conteúdo do campo nome tenha nos primeiros 4 caracteres a palavra 'Mari' utiliza-se a instrução SELECT * FROM emp WHERE SUBSTRING(nome,FIRST)= 'Mari';
* **E)** o nome e o salário do funcionário somado à comissão, considerando que o conteúdo de alguns campos comissao estão nulos, utiliza-se a instrução SELECT nome, salario+NIL(comissao) FROM emp;

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *3.3 Lógica Ternária (Three-Valued Logic) e a Armadilha do NOT IN com NULL* deste guia, considere a consulta: SELECT nome FROM cliente WHERE id NOT IN (SELECT id cliente FROM divida). Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 3ª/2015) ao estabelecer que "os dados de todos de todos os funcionários cujos nomes possuam a letra a como segundo caractere, utiliza se a...".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "os dados dos funcionários cujo nome seja 'Pedro' ou 'Ana' utiliza se a instrução SELECT FROM emp WHERE nome LIKE...". De acordo com a teoria estudada em *2.2 O Conflito WHERE vs. HAVING e a Ilegalidade de Aliases*, código Inválido: SELECT salario 1.1 AS novo salario FROM servidor WHERE novo salario 5000; (Gera erro de coluna inexistente!).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "os dados de todos os funcionários cujo conteúdo do campo salario esteja entre 1000 e 2000 utiliza se a instrução...". De acordo com a teoria estudada em *5.1 Visões: View Padrão vs. View Materializada (Materialized View)*, trade off: Os dados ficam estáticos/defasados até que um comando de atualização explícito seja disparado: REFRESH MATERIALIZED VIEW nome da view;.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "os dados dos funcionários cujo conteúdo do campo nome tenha nos primeiros 4 caracteres a palavra 'Mari' utiliza se...". De acordo com a teoria estudada em *2. Ordem Lógica de Execução da Consulta SQL (DQL)*, p1["1. FROM / JOIN / ON<br/ (Identifica tabelas e computa junções)"] P2["2. WHERE<br/ (Filtra tuplas brutas linha a linha)"].
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "o nome e o salário do funcionário somado à comissão, considerando que o conteúdo de alguns campos comissao estão...". De acordo com a teoria estudada em *Momentos de Disparo (Timing):*, bEFORE : Executado antes que a modificação seja persistida no disco. Ideal para validação de dados, enriquecimento de campos e integridade de negócio. Permite alterar os valores de NEW antes da gravação.
>
> **Gabarito: A**

---

### Teste 025
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Ciência de Dados)**
O DMBOK é estruturado em torno de onze (11) áreas de conhecimento do Framework de Gerenciamento de Dados DAMA-DMBOK. Essas áreas descrevem o escopo e o contexto de diversos conjuntos de atividades de gerenciamento de dados, e nelas estão incorporados os objetivos e princípios fundamentais do gerenciamento de dados. A área do conhecimento que inclui a reconciliação e a manutenção contínuas dos dados críticos, compartilhados e essenciais para permitir o uso consistente entre sistemas da versão mais precisa, oportuna e relevante da verdade sobre entidades empresariais essenciais é a

* **A)** Governança de Dados.
* **B)** Segurança de Dados.
* **C)** Referência e Dados Mestres.
* **D)** Integração e Interoperabilidade de Dados.
* **E)** Data Warehouse e Business Intelligence.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Governança de Dados". De acordo com a teoria estudada em *1.2 O Duelo Clássico: DROP vs. TRUNCATE vs. DELETE*, escopo de Remoção: Linhas filtradas ( WHERE ) ou todas as linhas da tabela. — Todas as linhas da tabela incondicionalmente. — A tabela inteira (estrutura, dados e metadados no catálogo).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Segurança de Dados". De acordo com a teoria estudada em *5.1 Visões: View Padrão vs. View Materializada (Materialized View)*, vantagens: Dados sempre 100% atualizados; atua como camada de segurança e abstração (ocultando colunas confidenciais).
> - **C)** **Correta.** Conforme fundamentado na seção *3.4 Common Table Expressions (CTEs) e Recursividade (WITH RECURSIVE)* deste guia, wITH RECURSIVE : Permite que a CTE faça referência a si mesma, viabilizando consultas em estruturas hierárquicas e em grafos (como organogramas empresariais ou árvores de dependência de processos). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "Referência e Dados Mestres".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Integração e Interoperabilidade de Dados". De acordo com a teoria estudada em *1.1 Classificação ANSI: DDL, DML, DQL, DCL e TCL*, dDL: Data Definition Language — CREATE , ALTER , DROP , TRUNCATE , RENAME — Criação, modificação estrutural e exclusão física de objetos no catálogo de dados (tabelas, esquemas, índices, visões).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Data Warehouse e Business Intelligence". De acordo com a teoria estudada em *1.1 Classificação ANSI: DDL, DML, DQL, DCL e TCL*, dQL: Data Query Language — SELECT — Consulta e recuperação de dados estruturados (frequentemente agrupada como subconjunto da DML).
>
> **Gabarito: C**

---

### Teste 026
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Ciência de Dados)**
Associe os conceitos a seguir às respectivas características. 1. Data Lake 2. Data Mart ( ) Surgiu como uma alternativa aos armazéns de dados tradicionais, permitindo o armazenamento de grandes volumes de dados de qualquer tipo e tamanho. ( ) São criados para tornar os dados mais facilmente acessíveis para geração de relatórios, além de fornecer um estágio adicional de transformação além das tubulações ETL iniciais. ( ) Tipo de armazenamento de dados frequentemente usado para suportar camadas de apresentação do ambiente de data warehouse. ( ) Fornece um local central de armazenamento para dados brutos, com o mínimo de transformação, se houver. A associação correta, na ordem dada, é:

* **A)** 1 – 2 – 2 – 1.
* **B)** 1 – 2 – 1 – 2.
* **C)** 2 – 2 – 1 – 1.
* **D)** 1 – 1 – 2 – 2.
* **E)** 2 – 1 – 1 – 2.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *1.2 O Duelo Clássico: DROP vs. TRUNCATE vs. DELETE* deste guia, velocidade de Execução: Lento em grandes volumes de dados (milhões de linhas). — Extremamente rápido (quase instantâneo). — Instantâneo. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "1 – 2 – 2 – 1".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "1 – 2 – 1 – 2". De acordo com a teoria estudada em *1.1 Classificação ANSI: DDL, DML, DQL, DCL e TCL*, dQL: Data Query Language — SELECT — Consulta e recuperação de dados estruturados (frequentemente agrupada como subconjunto da DML).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "2 – 2 – 1 – 1". De acordo com a teoria estudada em *1.2 O Duelo Clássico: DROP vs. TRUNCATE vs. DELETE*, sobrecarga de Log (WAL/Redo): Alto overhead: Registra cada linha excluída individualmente no log de transações. — Mínimo overhead: Registra apenas a desalocação das páginas/extensões no disco. — Mínimo overhead: Registra a remoção do objeto do catálogo de dados.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "1 – 1 – 2 – 2". De acordo com a teoria estudada em *1.2 O Duelo Clássico: DROP vs. TRUNCATE vs. DELETE*, "O comando TRUNCATE é uma operação DML porque manipula dados de linhas." $\rightarrow$ ERRADO! O TRUNCATE é formalmente classificado como DDL, pois opera desalocando páginas físicas de armazenamento no catálogo de dados.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "2 – 1 – 1 – 2". De acordo com a teoria estudada em *1.1 Classificação ANSI: DDL, DML, DQL, DCL e TCL*, dDL: Data Definition Language — CREATE , ALTER , DROP , TRUNCATE , RENAME — Criação, modificação estrutural e exclusão física de objetos no catálogo de dados (tabelas, esquemas, índices, visões).
>
> **Gabarito: A**

---

### Teste 027
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
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "o campo candidato ID é uma chave estrangeira na Tabela Candidato". De acordo com a teoria estudada em *1.3 Restrições de Integridade (Constraints) e Ações de Chave Estrangeira*, sET NULL : Atualiza o campo da chave estrangeira dos filhos para NULL quando o pai é excluído (exige que a coluna aceite nulos).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "o campo candidato ID é uma chave primária na Tabela Concurso". De acordo com a teoria estudada em *1.3 Restrições de Integridade (Constraints) e Ações de Chave Estrangeira*, pRIMARY KEY : Garante unicidade e impede valores nulos ( UNIQUE + NOT NULL ). Cada tabela pode conter apenas uma chave primária.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "a Tabela Candidato está incompleta, haja vista que não possui informação do concurso que o candidato pode fazer". De acordo com a teoria estudada em *5.2 Stored Procedures vs. User-Defined Functions (UDF)*, retorno Obrigatório: Não possui retorno obrigatório (utiliza parâmetros OUT / INOUT ). — Exige compulsoriamente a cláusula RETURNS (escalar ou tabela).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "dá forma como o banco de dados foi concebido, só é possível lançar um concurso por candidado". De acordo com a teoria estudada em *1.3 Restrições de Integridade (Constraints) e Ações de Chave Estrangeira*, as restrições de integridade garantem a consistência lógica dos dados no banco.
> - **E)** **Correta.** Conforme fundamentado na seção *1.3 Restrições de Integridade (Constraints) e Ações de Chave Estrangeira* deste guia, uNIQUE : Impede valores duplicados, mas permite a inserção de valores nulos ( NULL ), exceto se combinado com NOT NULL. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "a inserção da chave estrangeira candidato ID na tabela Tabela Concurso, permite o lançamento de um candidato em...".
>
> **Gabarito: E**

---

### Teste 028
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Administração)**
O Auditor está operando um banco de dados relacional que contém a tabela CONTRATOS. Ele precisa contar quantos contratos ativos existem para o município de ‘Florianópolis’. O comando SQL que executa essa tarefa corretamente é

* **A)** SELECT SUM(contratos) FROM Contratos WHERE municipio = ‘Florianópolis’;
* **B)** SELECT COUNT(*) FROM Contratos WHERE municipio = ‘Florianópolis’;
* **C)** SELECT DISTINCT(*) FROM Contratos WHERE municipio = ‘Florianópolis’;
* **D)** SELECT ALL FROM Contratos GROUP BY municipio;
* **E)** SELECT SEARCH contratos WHERE municipio = ‘Florianópolis’;

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "SELECT SUM(contratos) FROM Contratos WHERE municipio = ‘Florianópolis’". De acordo com a teoria estudada em *3.3 Lógica Ternária (Three-Valued Logic) e a Armadilha do NOT IN com NULL*, considere a consulta: SELECT nome FROM cliente WHERE id NOT IN (SELECT id cliente FROM divida).
> - **B)** **Correta.** Conforme fundamentado na seção *2.2 O Conflito WHERE vs. HAVING e a Ilegalidade de Aliases* deste guia, código Inválido: SELECT salario 1.1 AS novo salario FROM servidor WHERE novo salario 5000; (Gera erro de coluna inexistente!). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "SELECT COUNT( ) FROM Contratos WHERE municipio = ‘Florianópolis’".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "SELECT DISTINCT( ) FROM Contratos WHERE municipio = ‘Florianópolis’". De acordo com a teoria estudada em *5.2 Stored Procedures vs. User-Defined Functions (UDF)*, invocação: Comando explícito CALL procedure name(args); — Invocada inline em comandos SQL: SELECT func(x) FROM tab.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "SELECT ALL FROM Contratos GROUP BY municipio". De acordo com a teoria estudada em *3.4 Common Table Expressions (CTEs) e Recursividade (WITH RECURSIVE)*, sELECT auditor id, COUNT( ) AS total.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "SELECT SEARCH contratos WHERE municipio = ‘Florianópolis’". De acordo com a teoria estudada em *2. Ordem Lógica de Execução da Consulta SQL (DQL)*, p1["1. FROM / JOIN / ON<br/ (Identifica tabelas e computa junções)"] P2["2. WHERE<br/ (Filtra tuplas brutas linha a linha)"].
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

### Teste 029
**(CEBRASPE – STF – 2008 – Analista Judiciario Suporte Em Tecnologia Da Informacao)**
Regras de datalog podem ser classificadas como sendo um tipo de gatilho (trigger) utilizado, geralmente, para o tratamento na definição de visões no banco de dados. today looks at how emerging computer technologies will change

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Incorreta.** A proposição apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Regras de datalog podem ser classificadas como sendo um tipo de gatilho (trigger) utilizado, geralmente, para...". De acordo com a teoria em *Momentos de Disparo (Timing):*, iNSTEAD OF : Intercepta a instrução DML e executa a rotina do gatilho no lugar da operação original. É a solução canônica para permitir operações de INSERT , UPDATE e DELETE em visões (Views) complexas não atualizáveis.
> - **E)** **Correta.** O item está **Errado** (gabarito oficial: **E**), pois contraria a disciplina teórica aplicável.
>
> **Gabarito: E**

---

### Teste 030
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
> - **A)** **Correta.** Conforme fundamentado na seção *1.2 O Duelo Clássico: DROP vs. TRUNCATE vs. DELETE* deste guia, comportamento Transacional: Suporta ROLLBACK em qualquer SGBD compatível com ACID. — Reversível no PostgreSQL/SQL Server; no Oracle efetua COMMIT implícito. — Reversível no PostgreSQL; no Oracle efetua COMMIT implícito. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 4ª/2015) ao estabelecer que "SQL Server 2014 possui várias tecnologias de BI, como o Integration Services, uma plataforma que inclui pacotes...".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "PostegreSQL 9.4 utiliza um modelo cliente/servidor. Uma sessão PostgreSQL consiste de 2 processos cooperativos: o...". De acordo com a teoria estudada em *2.1 Ordem Léxica (Escrita) vs. Ordem Lógica (Processamento)*, uNION / INTERSECT / EXCEPT : Executa operações de conjuntos de linhas.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Oracle 11g utiliza o seguinte comando para criar um novo BD, denominado meuBD: $createdatabase meuBD". De acordo com a teoria estudada em *1.2 O Duelo Clássico: DROP vs. TRUNCATE vs. DELETE*, "O comando TRUNCATE é uma operação DML porque manipula dados de linhas." $\rightarrow$ ERRADO! O TRUNCATE é formalmente classificado como DDL, pois opera desalocando páginas físicas de armazenamento no catálogo de dados.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "PostegreSQL utiliza o pacote DBMS CONNECTION POOL para gerenciar o Database Resident Connection Pool, cujos...". De acordo com a teoria estudada em *5.2 Stored Procedures vs. User-Defined Functions (UDF)*, retorno Obrigatório: Não possui retorno obrigatório (utiliza parâmetros OUT / INOUT ). — Exige compulsoriamente a cláusula RETURNS (escalar ou tabela).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Oracle 11g permite que o Analysis Services e o Reporting Services possam ser instalados como servidores autônomos...". De acordo com a teoria estudada em *5.2 Stored Procedures vs. User-Defined Functions (UDF)*, efeitos Colaterais: Permite alterar esquemas e dados via DDL e DML livremente. — Deve evitar efeitos colaterais para manter a integridade referencial.
>
> **Gabarito: A**

---

### Teste 031
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Ciência de Dados)**
Em um Sistema de Gerenciamento de Banco de Dados (SGBD), recursos como Stored Procedures e Triggers são utilizados para dar maior flexibilidade para as aplicações a serem desenvolvidas, com o objetivo de regras e controles serem implementados na camada do banco. No contexto apresentado, assinale a opção que mostra a principal diferença entre Stored Procedures e Triggers.

* **A)** Stored Procedures são usadas para automatizar a execução de tarefas rotineiras, enquanto Triggers são usadas para armazenar procedimentos complexos.
* **B)** Stored Procedures são acionadas automaticamente em resposta a eventos específicos, enquanto Triggers são procedimentos armazenados que podem ser chamados explicitamente por comandos SQL.
* **C)** Stored Procedures são sempre escritas em linguagens de programação de alto nível, enquanto Triggers são escritas em SQL puro.
* **D)** Stored Procedures são armazenadas no disco junto com os dados do banco, enquanto Triggers são armazenadas apenas na memória principal do servidor.
* **E)** Stored Procedures são executadas apenas uma vez por evento, enquanto Triggers são executadas repetidamente até que o evento seja concluído.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Stored Procedures são usadas para automatizar a execução de tarefas rotineiras, enquanto Triggers são usadas para...". De acordo com a teoria estudada em *5.2 Stored Procedures vs. User-Defined Functions (UDF)*, invocação: Comando explícito CALL procedure name(args); — Invocada inline em comandos SQL: SELECT func(x) FROM tab.
> - **B)** **Correta.** Conforme fundamentado na seção *5.3 Gatilhos (Triggers): Eventos, Momentos (BEFORE, AFTER, INSTEAD OF) e Pseudorregistros OLD/NEW* deste guia, gatilhos ( Triggers ) são blocos de código procedurais executados automaticamente pelo motor de banco de dados quando eventos DML específicos ocorrem em uma tabela. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "Stored Procedures são acionadas automaticamente em resposta a eventos específicos, enquanto Triggers são...".
> - **C)** **Incorreta.** A opção promove generalização excessiva que desconsidera as condições técnicas e normativas ao afirmar que "Stored Procedures são sempre escritas em linguagens de programação de alto nível, enquanto Triggers são escritas...". De acordo com a teoria estudada em *5.2 Stored Procedures vs. User-Defined Functions (UDF)*, efeitos Colaterais: Permite alterar esquemas e dados via DDL e DML livremente. — Deve evitar efeitos colaterais para manter a integridade referencial.
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "Stored Procedures são armazenadas no disco junto com os dados do banco, enquanto Triggers são armazenadas apenas...". De acordo com a teoria estudada em *5.1 Visões: View Padrão vs. View Materializada (Materialized View)*, não armazena dados físicos em disco; representa apenas uma consulta SQL gravada no dicionário de dados do SGBD.
> - **E)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "Stored Procedures são executadas apenas uma vez por evento, enquanto Triggers são executadas repetidamente até que...". De acordo com a teoria estudada em *5.2 Stored Procedures vs. User-Defined Functions (UDF)*, dimensão Técnica: Stored Procedure — User Defined Function (UDF).
>
> **Gabarito: B**

---

