# -*- coding: utf-8 -*-
import os
import re

BASE_DIR = "fontes_de_estudo/conhecimentos_especificos_b02_ti/08_banco_de_dados"

# ==============================================================================
# FILE 02: 02_linguagem_sql_ddl_dml_dql_tcl_e_dcl.md
# ==============================================================================
def enrich_file_02():
    path = os.path.join(BASE_DIR, "02_linguagem_sql_ddl_dml_dql_tcl_e_dcl.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    for q in ["### Questão 01", "### Questão 02", "### Questão 03", "### Questão 04", "### Questão 05"]:
        assert q in content, f"Missing {q} in {path}"

    q06 = """### Questão 06 (FGV - TRT / Analista Judiciário - TI - Comandos DCL e Gestão de Privilégios)
Em um banco de dados corporativo de um órgão público, o Administrador de Banco de Dados (DBA) necessita conceder privilégios de consulta e inserção na tabela `FOLHA_PAGAMENTO` para o usuário `auditor_fiscal`, permitindo adicionalmente que este usuário repasse exclusivamente o privilégio de consulta a outros analistas de sua equipe. Posteriormente, por motivos de conformidade, o DBA revogou o privilégio de consulta do `auditor_fiscal` de forma cascateada.

Considerando os comandos da Data Control Language (DCL) do padrão ANSI SQL, assinale a opção que indica as instruções corretas para conceder os privilégios solicitados e, em seguida, revogá-los com efeito em cascata:

* **A)** `GRANT SELECT, INSERT ON FOLHA_PAGAMENTO TO auditor_fiscal WITH GRANT OPTION;` e `REVOKE ALL PRIVILEGES ON FOLHA_PAGAMENTO FROM auditor_fiscal;`
* **B)** `GRANT SELECT ON FOLHA_PAGAMENTO TO auditor_fiscal WITH GRANT OPTION;` seguido de `GRANT INSERT ON FOLHA_PAGAMENTO TO auditor_fiscal;` e, para revogação, `REVOKE SELECT ON FOLHA_PAGAMENTO FROM auditor_fiscal CASCADE;`
* **C)** `PERMIT SELECT, INSERT ON FOLHA_PAGAMENTO FOR auditor_fiscal ADMIN OPTION;` e `DENY SELECT ON FOLHA_PAGAMENTO TO auditor_fiscal;`
* **D)** `GRANT READ, WRITE ON TABLE FOLHA_PAGAMENTO TO USER auditor_fiscal;` e `REVOKE SELECT CASCADE FROM auditor_fiscal;`
* **E)** `ALLOW SELECT ON FOLHA_PAGAMENTO TO auditor_fiscal WITH ADMIN OPTION;` e `REVOKE SELECT ON FOLHA_PAGAMENTO FROM auditor_fiscal RESTRICT;`

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Ao conceder `WITH GRANT OPTION` conjuntamente para `SELECT` e `INSERT`, o auditor poderia repassar também o privilégio de inserção, violando a regra de negócio que restringia o repasse exclusivamente à consulta (`SELECT`).
> - **B)** **CORRETA.** A cláusula `WITH GRANT OPTION` deve ser vinculada unicamente ao privilégio que pode ser repassado (`SELECT`). O privilégio `INSERT` é concedido sem essa cláusula. Para a revogação em cascata (removendo o privilégio de `auditor_fiscal` e simultaneamente de todos os terceiros a quem ele concedeu), a sintaxe padrão ANSI SQL exige `REVOKE SELECT ON FOLHA_PAGAMENTO FROM auditor_fiscal CASCADE;`.
> - **C)** Incorreta. `PERMIT` e `DENY` não são comandos padrão DCL do ANSI SQL (são dialetos proprietários).
> - **D)** Incorreta. No padrão SQL, os privilégios primitivos são `SELECT` e `INSERT`, não `READ` e `WRITE`.
> - **E)** Incorreta. `ALLOW` não é comando SQL; além disso, a cláusula `RESTRICT` abortaria a revogação caso existissem privilégios dependentes, enquanto o comando exigia revogação cascateada (`CASCADE`).
> 
> **Gabarito: B**

---
"""

    q07 = """### Questão 07 (FCC - TRT-14 / Analista Judiciário - TI - Comandos DDL vs. DML: DROP, TRUNCATE e DELETE)
Durante a manutenção emergencial de uma base de dados transacional com milhões de registros de log, o analista de banco de dados precisa esvaziar integralmente o conteúdo da tabela `LOG_ACESSO_TEMPORARIO`, liberando de imediato o espaço de armazenamento em disco e reinicializando os ponteiros de High Water Mark (HWM), com a máxima velocidade operacional possível e sem registrar cada tupla individualmente no log de transações.

Para atender estritamente a esses requisitos técnicos, o comando correto a ser executado é:

* **A)** `DELETE FROM LOG_ACESSO_TEMPORARIO;`
* **B)** `DROP TABLE LOG_ACESSO_TEMPORARIO;`
* **C)** `TRUNCATE TABLE LOG_ACESSO_TEMPORARIO;`
* **D)** `ALTER TABLE LOG_ACESSO_TEMPORARIO CLEAR DATA;`
* **E)** `REMOVE ALL FROM LOG_ACESSO_TEMPORARIO;`

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O `DELETE` é um comando DML que varre e remove linha por linha, gerando volume colossal de registros no Undo/Redo Log (WAL) para permitir `ROLLBACK`, além de disparar *triggers* do tipo `AFTER DELETE` e não resetar a High Water Mark (HWM), mantendo o espaço alocado.
> - **B)** Incorreta. O `DROP TABLE` é um comando DDL que destrói a própria definição da tabela no catálogo de metadados, eliminando suas colunas, restrições e índices, exigindo recriação do objeto caso ele continue a ser utilizado.
> - **C)** **CORRETA.** O `TRUNCATE TABLE` é um comando DDL (Data Definition Language) de desalocação rápida de páginas/extensões de dados. Ele desvincula os blocos de dados de uma só vez, gera registro mínimo no log transacional (apenas a desalocação das páginas), reinicializa a High Water Mark (HWM) e a contagem de sequências/identidades, não dispara *triggers* por linha e é ordens de grandeza mais veloz que o `DELETE`.
> - **D)** Incorreta. Sintaxe inexistente no padrão ANSI SQL.
> - **E)** Incorreta. Comando inexistente na sintaxe SQL.
> 
> **Gabarito: C**

---
"""

    q08 = """### Questão 08 (FGV - TJ-AP / Analista Judiciário - Banco de Dados - Junções SQL e Tratamento de Nulos)
Considere duas tabelas em um banco de dados relacional: `ORGAO` (com as colunas `id_orgao`, `nome_orgao`) contendo 10 registros, e `CONTRATO` (com as colunas `id_contrato`, `id_orgao`, `valor`) contendo 50 registros. Sabe-se que 2 órgãos da tabela `ORGAO` não possuem nenhum contrato cadastrado e que todos os 50 contratos da tabela `CONTRATO` possuem um `id_orgao` válido associado.

Um auditor executou a seguinte instrução SQL:

```sql
SELECT O.nome_orgao, C.id_contrato, C.valor
FROM ORGAO O
LEFT JOIN CONTRATO C ON O.id_orgao = C.id_orgao;
```

A quantidade exata de linhas retornadas por essa consulta e o conteúdo dos campos `C.id_contrato` e `C.valor` para os 2 órgãos que não possuem contratos são, respectivamente:

* **A)** 48 linhas, e as linhas dos órgãos sem contratos são omitidas do resultado.
* **B)** 50 linhas, e as linhas dos órgãos sem contratos exibem valor 0 nos campos numéricos.
* **C)** 52 linhas, e as linhas dos 2 órgãos sem contratos exibem o valor `NULL` nos campos `id_contrato` e `valor`.
* **D)** 60 linhas, correspondendo ao produto cartesiano das tabelas.
* **E)** 10 linhas, retornando apenas uma linha condensada para cada órgão existente.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A junção externa à esquerda (`LEFT JOIN`) preserva compulsoriamente todas as tuplas da relação esquerda (`ORGAO`), mesmo que não haja correspondência na direita.
> - **B)** Incorreta. O SQL preenche ausência de correspondência com o marcador `NULL`, jamais com o valor escalar 0.
> - **C)** **CORRETA.** A semântica do `LEFT OUTER JOIN` garante que todas as linhas da tabela à esquerda (`ORGAO`) estejam presentes no resultado:
>   1. Para os 8 órgãos que possuem contratos, cada contrato gera uma linha correspondente no resultado, totalizando 50 linhas.
>   2. Para os 2 órgãos que não possuem contratos vinculados, a tabela à esquerda gera exatamente uma linha para cada um deles, e todas as colunas originárias da tabela à direita (`C.id_contrato` e `C.valor`) são preenchidas com o marcador de ausência `NULL`.
>   3. Total de linhas: $50 + 2 = 52$ linhas.
> - **D)** Incorreta. O produto cartesiano ($10 \\times 50 = 500$ linhas) seria obtido com `CROSS JOIN`.
> - **E)** Incorreta. Para retornar apenas 10 linhas condensadas, seria necessária a cláusula `GROUP BY O.nome_orgao` com funções de agregação.
> 
> **Gabarito: C**

---
"""

    q09 = """### Questão 09 (FCC - TRT / Analista Judiciário - TI - Operadores de Conjunto: UNION vs. UNION ALL)
Em procedimentos analíticos de auditoria de dados, um auditor necessita consolidar em uma única lista todos os CPFs de fornecedores que receberam pagamentos no Exercício de 2024 (tabela `PAGAMENTOS_2024`, com 100.000 registros, contendo CPFs repetidos) e no Exercício de 2025 (tabela `PAGAMENTOS_2025`, com 80.000 registros, também com repetições). Sabe-se que 20.000 CPFs distintos aparecem em ambos os exercícios.

Considerando os operadores de conjunto da linguagem SQL padrão ANSI, avalie as afirmativas:

I. O operador `UNION` realiza a união das tuplas e executa uma etapa implícita de ordenação e descarte de duplicatas (`SORT UNIQUE`), retornando apenas CPFs distintos.  
II. O operador `UNION ALL` simplesmente concatena os resultados das duas consultas sem verificar duplicidades, resultando em menor custo computacional de CPU e memória em relação ao `UNION`.  
III. O operador `INTERSECT` retornaria apenas os CPFs dos fornecedores que figuram simultaneamente em ambas as tabelas (`PAGAMENTOS_2024` e `PAGAMENTOS_2025`), eliminando repetições.  

Está correto o que se afirma em:

* **A)** I, apenas.
* **B)** II, apenas.
* **C)** I e II, apenas.
* **D)** II e III, apenas.
* **E)** I, II e III.

> **Comentário Detalhado:**
>
> - **I.** **CORRETA.** O operador `UNION` exige compatibilidade de esquemas e, por padrão formal, elimina tuplas duplicadas do conjunto unificado. Para eliminar duplicatas, o motor do SGBD invoca um operador de ordenação em disco/memória (`Sort Unique`) ou uma tabela hash, aumentando o consumo de recursos.
> - **II.** **CORRETA.** O operador `UNION ALL` realiza a união multiconjunto (*multiset* ou *bag union*), preservando todas as linhas de ambos os lados sem qualquer deduplicação. Como dispensa a fase de ordenação/hashing, sua execução é ordens de grandeza mais rápida e consome menos memória.
> - **III.** **CORRETA.** O operador `INTERSECT` calcula a interseção dos dois conjuntos, retornando unicamente as linhas presentes simultaneamente no primeiro e no segundo comando `SELECT`, eliminando valores duplicados.
> 
> **Gabarito: E**

---
"""

    q10 = """### Questão 10 (FGV - TJ-AP / Analista Judiciário - Banco de Dados - Common Table Expressions e CTE Recursiva)
Em um sistema de auditoria governamental, a estrutura de subordinação hierárquica dos órgãos de controle é modelada na tabela `UNIDADE_ORGANIZACIONAL (id_unidade, nome_unidade, id_unidade_superior)`.

Para percorrer recursivamente todos os níveis descendentes a partir de uma unidade raiz (`id_unidade = 1`), o padrão ANSI SQL:1999 disponibiliza o recurso de Common Table Expressions (CTEs) recursivas. A respeito da construção sintática e do funcionamento operacional de uma `WITH RECURSIVE`, assinale a afirmativa correta:

* **A)** A cláusula `WITH RECURSIVE` é composta obrigatoriamente por dois membros unidos por `UNION` ou `UNION ALL`: o membro-âncora (termo inicial não-recursivo) e o membro recursivo (que faz referência ao próprio nome da CTE), cessando a execução quando o membro recursivo retorna um conjunto vazio.
* **B)** A consulta recursiva executa um loop infinito no SGBD a menos que seja incluída compulsoriamente uma cláusula `LIMIT 100` na definição da tabela âncora.
* **C)** Funções de agregação como `SUM()` e `AVG()` podem ser livremente empregadas dentro da subconsulta do membro recursivo sem restrições sintáticas pelo padrão ANSI.
* **D)** Uma CTE recursiva não pode ser utilizada com o comando `SELECT`, sendo um recurso exclusivo de instruções de modificação de dados (`UPDATE` e `DELETE`).
* **E)** O operador de junção entre o membro-âncora e o membro recursivo deve ser compulsoriamente um `CROSS JOIN`.

> **Comentário Detalhado:**
>
> - **A)** **CORRETA.** A arquitetura da CTE recursiva (`WITH RECURSIVE nome_cte AS (...)`) é rigorosamente estruturada em:
>   1. **Membro-Âncora (Anchor Member):** Executa uma única vez para gerar o conjunto de dados base (ex.: recuperar o órgão com `id_unidade = 1`).
>   2. **Operador de União:** `UNION ALL` (mais comum por performance) ou `UNION`.
>   3. **Membro Recursivo (Recursive Member):** Faz referência direta a `nome_cte` unida com a tabela física (`UNIDADE_ORGANIZACIONAL`) para descer/subir na árvore. O motor avalia iterativamente até que uma iteração retorne zero registros (conjunto vazio), momento em que a recursão atinge sua condição natural de parada.
> - **B)** Incorreta. O encerramento ocorre naturalmente quando a iteração atual não produz nenhuma nova linha.
> - **C)** Incorreta. O padrão ANSI SQL proíbe expressamente o uso de funções de agregação (`SUM`, `MAX`, `AVG`), cláusulas `GROUP BY` e `ORDER BY` dentro do membro recursivo que referencia a própria CTE recursiva.
> - **D)** Incorreta. CTEs recursivas são amplamente utilizadas com instruções `SELECT` para consultas em grafos e árvores hierárquicas.
> - **E)** Incorreta. O membro-âncora e o membro recursivo são unidos por operadores de conjunto (`UNION` ou `UNION ALL`), jamais por `CROSS JOIN`.
> 
> **Gabarito: A**

---
"""

    q11 = """### Questão 11 (FGV - TRT-DA 24-REGIÃO / Analista Judiciário - TI - Funções de Deslocamento: LEAD e LAG)
Em auditorias de contratações públicas, é comum comparar o valor pago a um prestador em um determinado mês com o valor pago no mês imediatamente anterior e no mês imediatamente posterior, a fim de detectar variações abruptas de faturamento.

Considere a tabela `PAGAMENTO_CONTRATO` com as colunas `id_contrato`, `mes_ano` e `valor_pago`. Assinale a instrução SQL que utiliza corretamente funções analíticas de deslocamento de janela para recuperar, em uma mesma linha de saída para cada contrato, o valor do pagamento corrente, o valor do mês imediatamente anterior e o valor do mês imediatamente subsequente:

* **A)**
```sql
SELECT id_contrato, mes_ano, valor_pago,
       LAG(valor_pago, 1) OVER (PARTITION BY id_contrato ORDER BY mes_ano) AS valor_anterior,
       LEAD(valor_pago, 1) OVER (PARTITION BY id_contrato ORDER BY mes_ano) AS valor_posterior
FROM PAGAMENTO_CONTRATO;
```
* **B)**
```sql
SELECT id_contrato, mes_ano, valor_pago,
       FIRST_VALUE(valor_pago) OVER (ORDER BY mes_ano) AS valor_anterior,
       LAST_VALUE(valor_pago) OVER (ORDER BY mes_ano) AS valor_posterior
FROM PAGAMENTO_CONTRATO;
```
* **C)**
```sql
SELECT id_contrato, mes_ano, valor_pago,
       PREVIOUS(valor_pago) WITHIN GROUP (ORDER BY mes_ano) AS valor_anterior,
       NEXT(valor_pago) WITHIN GROUP (ORDER BY mes_ano) AS valor_posterior
FROM PAGAMENTO_CONTRATO;
```
* **D)**
```sql
SELECT id_contrato, mes_ano, valor_pago,
       LEAD(valor_pago, -1) OVER (ORDER BY id_contrato) AS valor_anterior,
       LAG(valor_pago, +1) OVER (ORDER BY id_contrato) AS valor_posterior
FROM PAGAMENTO_CONTRATO;
```
* **E)**
```sql
SELECT id_contrato, mes_ano, valor_pago,
       OFFSET(valor_pago, -1) OVER (PARTITION BY id_contrato) AS valor_anterior,
       OFFSET(valor_pago, 1) OVER (PARTITION BY id_contrato) AS valor_posterior
FROM PAGAMENTO_CONTRATO;
```

> **Comentário Detalhado:**
>
> - **A)** **CORRETA.** As funções de deslocamento do padrão SQL funcionam com as seguintes propriedades:
>   - `LAG(expressao, offset, [default])`: Acessa dados de uma linha situada $N$ posições **anteriores** à linha corrente dentro da partição da janela.
>   - `LEAD(expressao, offset, [default])`: Acessa dados de uma linha situada $N$ posições **posteriores** (subsequentes) à linha corrente dentro da partição da janela.
>   - A cláusula `PARTITION BY id_contrato` garante que o histórico de pagamentos seja particionado isoladamente por contrato, e `ORDER BY mes_ano` define a sequência temporal cronológica mandatória para o cálculo do deslocamento.
> - **B)** Incorreta. `FIRST_VALUE` e `LAST_VALUE` retornam o primeiro e o último valor de todo o frame da janela, não os valores adjacentes anterior e posterior.
> - **C)** Incorreta. Funções `PREVIOUS` e `NEXT` não existem no padrão ANSI SQL.
> - **D)** Incorreta. Os papéis de `LEAD` e `LAG` foram invertidos e o deslocamento com offset negativo gera erro sintático em diversos dialetos.
> - **E)** Incorreta. Função `OFFSET` não é função analítica de janela no padrão SQL.
> 
> **Gabarito: A**

---
"""

    # Insert Q06 after 1.1 (before ### 1.2 O Duelo Clássico: DROP vs. TRUNCATE vs. DELETE)
    p1 = "### 1.2 O Duelo Clássico: DROP vs. TRUNCATE vs. DELETE"
    assert p1 in content
    content = content.replace(p1, q06 + "\n" + p1, 1)

    # Insert Q07 after 1.2 (before ### 1.3 Restrições de Integridade)
    p2 = "### 1.3 Restrições de Integridade (Constraints) e Ações de Chave Estrangeira"
    assert p2 in content
    content = content.replace(p2, q07 + "\n" + p2, 1)

    # Insert Q08 after 3.1 (before ### 3.2 Operadores de Conjunto)
    p3 = "### 3.2 Operadores de Conjunto (UNION vs. UNION ALL, INTERSECT, EXCEPT)"
    assert p3 in content
    content = content.replace(p3, q08 + "\n" + p3, 1)

    # Insert Q09 after 3.2 (before ### 3.3 Lógica Ternária)
    p4 = "### 3.3 Lógica Ternária (Three-Valued Logic) e a Armadilha do NOT IN com NULL"
    assert p4 in content
    content = content.replace(p4, q09 + "\n" + p4, 1)

    # Insert Q10 after 3.4 (before ## 4. Funções Analíticas de Janela)
    p5 = "## 4. Funções Analíticas de Janela (Window Functions)"
    assert p5 in content
    content = content.replace(p5, q10 + "\n" + p5, 1)

    # Insert Q11 after 4.3 (before ## 5. Objetos Programáveis de Banco de Dados)
    p6 = "## 5. Objetos Programáveis de Banco de Dados"
    assert p6 in content
    content = content.replace(p6, q11 + "\n" + p6, 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("File 02 successfully enriched! Total questions:", len(re.findall(r"### Questão \d+", content)))

# enrich_file_02()


# ==============================================================================
# FILE 03: 03_transacoes_propriedades_acid_e_concorrencia.md
# ==============================================================================
def enrich_file_03():
    path = os.path.join(BASE_DIR, "03_transacoes_propriedades_acid_e_concorrencia.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    for q in ["### Questão 01", "### Questão 02", "### Questão 03", "### Questão 04", "### Questão 05"]:
        assert q in content, f"Missing {q} in {path}"

    q06 = """### Questão 06 (FGV - TJ-AP / Analista Judiciário - Banco de Dados - Estados do Ciclo de Vida de uma Transação)
Segundo a teoria clássica de sistemas de bancos de dados relacionais formulada por Silberschatz, Korth e Sudarshan, uma transação deve atravessar uma máquina de estados finitos bem definida durante a sua execução.

A respeito dos estados possíveis de uma transação e das transições entre eles, assinale a afirmativa correta:

* **A)** Uma transação entra no estado *Committed* (Efetivada) imediatamente após a emissão da primeira instrução DML de escrita no buffer de memória.
* **B)** O estado *Partially Committed* (Parcialmente Efetivada) ocorre após a execução da última declaração SQL da transação, mas antes que as modificações e seus registros de log correspondentes tenham sido completamente gravados de forma persistente em disco (disco estável).
* **C)** Uma transação em estado *Failed* (Falha) transita compulsoriamente de volta para o estado *Active* (Ativa) para tentar novamente a operação a partir do ponto onde ocorreu a falha.
* **D)** O estado *Aborted* (Abortada) indica que a transação concluiu seu processamento com êxito e que seus resultados tornaram-se permanentes no banco de dados.
* **E)** Toda transação no estado *Active* pode transitar diretamente para o estado *Committed* sem necessidade de passar pelo estado *Partially Committed*.

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
"""

    q07 = """### Questão 07 (FGV - TJ-AP / Analista Judiciário - Banco de Dados - Anomalias e Fenômenos de Concorrência)
Em sistemas gerenciadores de bancos de dados com processamento transacional concorrente de alta intensidade, a ausência de mecanismos rigorosos de controle de concorrência expõe a base de dados a múltiplos fenômenos anômalos.

Analise as três situações de concorrência descritas a seguir entre duas transações $T_1$ e $T_2$:

1. $T_1$ lê um saldo bancário de R$ 10.000,00. Simultaneamente, $T_2$ altera esse saldo para R$ 15.000,00 e efetiva a operação com `COMMIT`. Em seguida, $T_1$ relê o mesmo registro na mesma transação e encontra o saldo de R$ 15.000,00.  
2. $T_1$ executa uma consulta que recupera todos os contratos com valor acima de R$ 1.000.000,00, obtendo 5 registros. Nesse intervalo, $T_2$ insere um novo contrato no valor de R$ 2.000.000,00 e efetiva com `COMMIT`. $T_1$ reexecuta a mesma consulta e agora obtém 6 registros.  
3. $T_1$ lê o valor de um empenho de R$ 50.000,00 e $T_2$ lê o mesmo valor. $T_1$ atualiza o valor para R$ 55.000,00 e efetiva. Logo depois, $T_2$, baseando-se no valor inicial lido, atualiza o valor para R$ 48.000,00 e efetiva, sobrescrevendo cegamente a alteração de $T_1$.  

Esses três fenômenos caracterizam, rigorosa e respectivamente:

* **A)** Leitura Suja (*Dirty Read*), Leitura Fantasma (*Phantom Read*) e Leitura Não Repetível (*Non-Repeatable Read*).
* **B)** Leitura Não Repetível (*Non-Repeatable Read*), Leitura Fantasma (*Phantom Read*) e Atualização Perdida (*Lost Update*).
* **C)** Leitura Fantasma (*Phantom Read*), Leitura Suja (*Dirty Read*) e Desvio de Gravação (*Write Skew*).
* **D)** Leitura Suja (*Dirty Read*), Atualização Perdida (*Lost Update*) e Leitura Não Repetível (*Non-Repeatable Read*).
* **E)** Leitura Não Repetível (*Non-Repeatable Read*), Atualização Perdida (*Lost Update*) e Leitura Suja (*Dirty Read*).

> **Comentário Detalhado:**
>
> - **Situação 1:** Trata-se de **Leitura Não Repetível (Non-Repeatable Read ou Fuzzy Read)**: ocorre quando uma transação relê a mesma linha e encontra valores de colunas alterados porque outra transação efetuou `UPDATE` e `COMMIT` no intervalo.
> - **Situação 2:** Trata-se de **Leitura Fantasma (Phantom Read)**: ocorre quando uma transação reexecuta uma consulta baseada em predicado/faixa e o conjunto de linhas resultante se altera devido a `INSERT` ou `DELETE` efetuado e confirmado por outra transação.
> - **Situação 3:** Trata-se de **Atualização Perdida (Lost Update)**: ocorre quando duas transações leem o mesmo registro e ambas tentam atualizá-lo em paralelo; a última gravação sobrescreve a primeira sem considerar a alteração anterior, perdendo-se os dados da primeira atualização.
> 
> **Gabarito: B**

---
"""

    q08 = """### Questão 08 (FCC - TRT / Analista Judiciário - TI - Snapshot Isolation e Anomalia de Write Skew)
O mecanismo de isolamento conhecido como *Snapshot Isolation* (Isolamento por Instantâneo) é amplamente empregado por SGBDs modernos baseados em MVCC (como PostgreSQL e Oracle). Sob esse nível, uma transação visualiza uma fotografia consistente dos dados correspondente ao instante em que iniciou.

Embora o *Snapshot Isolation* impeça Leitura Suja, Leitura Não Repetível e Leituras Fantasmas convencionais, a literatura de banco de dados comprova que ele **não é equivalente** ao nível de isolamento `SERIALIZABLE` clássico por admitir a anomalia denominada:

* **A)** Atualização Cega (*Blind Write*).
* **B)** Leitura Não Determinística (*Fuzzy Read*).
* **C)** Desvio de Gravação (*Write Skew*).
* **D)** Inconsistência de Checkpoint (*Torn Page*).
* **E)** Interbloqueio em Cascata (*Cascading Abort*).

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
"""

    q09 = """### Questão 09 (FGV - TJ-AP / Analista Judiciário - Banco de Dados - Bloqueios Compartilhados vs. Exclusivos)
Os SGBDs relacionais empregam bloqueios (*locks*) lógicos gerenciados pelo subsistema de Lock Manager para disciplinar o acesso concorrente aos dados. Dois modos fundamentais de bloqueio são o Compartilhado (*Shared Lock - S*) e o Exclusivo (*Exclusive Lock - X*).

A respeito da matriz de compatibilidade entre esses tipos de bloqueios e sua granularidade, assinale a afirmativa correta:

* **A)** Múltiplas transações concorrentes podem obter simultaneamente bloqueios compartilhados (*Shared Locks*) sobre o mesmo recurso de dados para fins de leitura.
* **B)** Uma transação pode obter com sucesso um bloqueio exclusivo (*Exclusive Lock*) sobre uma tabela mesmo que outra transação já mantenha ativo um bloqueio compartilhado sobre essa mesma tabela.
* **C)** O bloqueio de granularidade fina (no nível de linha/tupla) consome menos memória do Lock Manager do que o bloqueio de granularidade grossa (no nível de tabela inteira).
* **D)** Bloqueios de intenção (*Intent Locks*, como IS e IX) são utilizados apenas em operações DDL e não interferem na concorrência de instruções DML como `SELECT` e `UPDATE`.
* **E)** O bloqueio compartilhado impede que outras transações realizem leituras simultâneas no mesmo objeto, forçando o enfileiramento sequencial de todas as operações de consulta.

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
"""

    q10 = """### Questão 10 (FCC - TRT-6 / Analista Judiciário - TI - Controle Multiversão de Concorrência - MVCC)
O Controle Multiversão de Concorrência (*Multi-Version Concurrency Control - MVCC*) é o mecanismo arquitetural predominante em motores de banco de dados modernos, tais como o PostgreSQL e o Oracle Database.

A principal vantagem do MVCC sobre os mecanismos tradicionais de bloqueio pessimista bidirecional (2PL estrito) e o seu princípio fundamental de funcionamento residem no fato de que:

* **A)** As transações de leitura realizam bloqueios exclusivos de página, impedindo a escrita de novas tuplas até que a leitura seja confirmada por `COMMIT`.
* **B)** Leituras nunca bloqueiam escritas, e escritas nunca bloqueiam leituras; quando um registro é atualizado, o SGBD não sobrescreve o dado no local original, mas cria uma nova versão física da tupla com metadados de transação (`xmin` / `xmax`), mantendo a versão anterior visível para transações ativas mais antigas.
* **C)** O MVCC elimina completamente o uso de memória RAM e de discos rígidos, processando todas as transações em tabelas estritamente temporárias.
* **D)** O isolamento obtido com MVCC é sempre `READ UNCOMMITTED`, permitindo leituras de dados sujos sem qualquer validação de *snapshots*.
* **E)** O MVCC dispensa integralmente mecanismos de coleta de lixo (*garbage collection* / `VACUUM`), pois as tuplas obsoletas são destruídas instantaneamente pelo processador na saída do comando `UPDATE`.

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
"""

    q11 = """### Questão 11 (FGV - TRT / Analista Judiciário - TI - Impasses / Deadlocks e Grafo de Espera)
Em um ambiente de banco de dados de alto volume transacional, duas transações concorrentes entram em uma situação na qual a Transação $T_1$ detém o bloqueio exclusivo da linha $A$ e aguarda a liberação da linha $B$ (bloqueada por $T_2$), enquanto $T_2$ aguarda a liberação da linha $A$ (bloqueada por $T_1$).

A respeito desse cenário de impasse (*Deadlock*) e dos métodos empregados pelos SGBDs para seu tratamento, assinale a afirmativa correta:

* **A)** O impasse é automaticamente resolvido pelo SGBD permitindo que ambas as transações acessem e sobrescrevam simultaneamente as duas linhas em disputa.
* **B)** A ocorrência de um deadlock é detectada pelo SGBD por meio da construção periódica de um Grafo de Espera (*Wait-For Graph*); a existência de um ciclo direcionado nesse grafo indica formalmente a presença de um deadlock, exigindo que o SGBD selecione uma transação "vítima" para ser abortada e sofrer `ROLLBACK`.
* **C)** O protocolo 2PL básico garante matematicamente a imunidade total e absoluta contra a ocorrência de deadlocks.
* **D)** Em caso de deadlock, o SGBD encerra forçosamente todas as conexões ativas no banco de dados e reinicia o processo principal do servidor.
* **E)** Protocolos baseados em timestamps (como *Wait-Die* e *Wound-Wait*) detectam impasses somente após o bloqueio indefinido de todos os núcleos da CPU.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Permitir acesso simultâneo sem bloqueio violaria o isolamento e corromperia os dados da base.
> - **B)** **CORRETA.** A teoria de detecção de impasses modela as dependências ativas por um grafo direcionado $G = (V, E)$, denominado **Wait-For Graph (Grafo de Espera)**:
>   - Os vértices $V$ representam as transações ativas ($T_1, T_2, \\dots$).
>   - As arestas direcionadas $(T_i \\rightarrow T_j)$ indicam que a transação $T_i$ está aguardando a liberação de um recurso bloqueado por $T_j$.
>   - Um impasse (*deadlock*) ocorre **se, e somente se, o grafo contiver um ciclo direcionado** ($T_1 \\rightarrow T_2 \\rightarrow T_1$).
>   - Ao detectar o ciclo, o algoritmo de recuperação elege uma transação "vítima" (com base em critérios como tempo de execução, custo de *rollback* ou número de tuplas alteradas), aborta essa transação com `ROLLBACK` e libera seus bloqueios para que as demais transações possam prosseguir.
> - **C)** Incorreta. O protocolo 2PL garante serializabilidade, mas **não previne** deadlocks.
> - **D)** Incorreta. O SGBD aborta apenas a transação vítima selecionada, mantendo o restante da instância em operação ininterrupta.
> - **E)** Incorreta. *Wait-Die* e *Wound-Wait* são esquemas de **prevenção** preventiva de deadlocks baseados na idade/timestamp da transação, não atuando após travamento total da CPU.
> 
> **Gabarito: B**

---
"""

    # Insert Q06 after 1.1 (before ### 1.2 As Quatro Propriedades Fundamentais: ACID)
    p1 = "### 1.2 As Quatro Propriedades Fundamentais: ACID"
    assert p1 in content
    content = content.replace(p1, q06 + "\n" + p1, 1)

    # Insert Q07 after 3.4 (before ## 4. Níveis de Isolamento ANSI SQL-92)
    p2 = "## 4. Níveis de Isolamento ANSI SQL-92"
    assert p2 in content
    content = content.replace(p2, q07 + "\n" + p2, 1)

    # Insert Q08 after 4.2 (before ## 5. Técnicas de Controle de Concorrência)
    p3 = "## 5. Técnicas de Controle de Concorrência"
    assert p3 in content
    content = content.replace(p3, q08 + "\n" + p3, 1)

    # Insert Q09 after 5.1 (before ### 5.2 Protocolo de Bloqueio em Duas Fases)
    p4 = "### 5.2 Protocolo de Bloqueio em Duas Fases (2PL - Two-Phase Locking): Básico, Estrito e Rigoroso"
    assert p4 in content
    content = content.replace(p4, q09 + "\n" + p4, 1)

    # Insert Q10 after 5.3 (before ### 5.4 Impasses (Deadlocks))
    p5 = "### 5.4 Impasses (Deadlocks): Detecção via Wait-For Graph e Resolução por Transação Vítima"
    assert p5 in content
    content = content.replace(p5, q10 + "\n" + p5, 1)

    # Insert Q11 after 5.4 (before ## 🌐 Fontes Oficiais e Referências Bibliográficas)
    p6 = "## 🌐 Fontes Oficiais e Referências Bibliográficas"
    assert p6 in content
    content = content.replace(p6, q11 + "\n" + p6, 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("File 03 successfully enriched! Total questions:", len(re.findall(r"### Questão \d+", content)))

# enrich_file_03()
