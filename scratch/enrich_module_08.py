# -*- coding: utf-8 -*-
"""
Script to enrich Module 08 (Banco de Dados) with Questions 06 to 11 in each of the 6 files.
Preserves existing questions 01-05 and all formatting/mermaid diagrams.
"""

import os
import re

BASE_DIR = "fontes_de_estudo/conhecimentos_especificos_b02_ti/08_banco_de_dados"

# File 01: 01_modelagem_de_dados_mer_e_normalizacao.md
f01_path = os.path.join(BASE_DIR, "01_modelagem_de_dados_mer_e_normalizacao.md")

q06_f01 = """### Questão 06 (FGV - TRT / Analista Judiciário - TI - Fases do Projeto e Níveis de Abstração)
No ciclo de vida do projeto de bancos de dados relacionais, a modelagem é classicamente particionada em três níveis conceituais progressivos: Modelo Conceitual, Modelo Lógico e Modelo Físico. 

A respeito desses modelos e de suas respectivas características arquiteturais, assinale a afirmativa correta:

* **A)** O modelo físico independe do Sistema Gerenciador de Banco de Dados (SGBD) adotado, concentrando-se na especificação pura das regras de negócio e diagramas de classes sem tipos primitivos.
* **B)** O modelo conceitual possui dependência direta do paradigma de dados escolhido (relacional, hierárquico ou grafos), determinando a alocação de chaves primárias e tipos de dados de armazenamento como `VARCHAR` e `INT`.
* **C)** O modelo lógico é uma representação de alto nível voltada à comunicação com o usuário final de negócio, na qual não constam tabelas, chaves primárias ou chaves estrangeiras.
* **D)** O modelo conceitual captura os requisitos de negócio e a semântica dos dados independentemente de tecnologia ou SGBD; o modelo lógico mapeia essas entidades para o paradigma relacional (tabelas, chaves); e o modelo físico define o armazenamento, estruturas de partição, índices e parâmetros de desempenho específicos do SGBD.
* **E)** A desnormalização é uma decisão estritamente tomada durante o modelo conceitual com o intuito de facilitar a validação dos diagramas pelos gestores de negócio.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O modelo físico é 100% dependente do SGBD específico (Oracle, PostgreSQL, MySQL), definindo scripts DDL, tablespaces, alocação de blocos e tipos nativos de armazenamento.
> - **B)** Incorreta. O modelo conceitual é completamente independente de paradigma de banco de dados e de tecnologia de SGBD.
> - **C)** Incorreta. O modelo lógico já adota o paradigma relacional, definindo rigorosamente tabelas, atributos, chaves primárias (PK), chaves estrangeiras (FK) e normalização.
> - **D)** **CORRETA.** Descreve com exatidão a clássica divisão de três esquemas proposta pela arquitetura ANSI/SPARC: Modelo Conceitual (independente de SGBD e de modelo de dados lógico), Modelo Lógico (dependente do modelo relacional, independente do software SGBD específico) e Modelo Físico (implementação concreta no SGBD).
> - **E)** Incorreta. A desnormalização ocorre nas fases lógica/física para otimização de leitura e desempenho transacional/analítico, jamais no modelo conceitual.
> 
> **Gabarito: D**

---
"""

q07_f01 = """### Questão 07 (FCC - TRT-2 / Analista Judiciário - TI - Tipologia dos Atributos no MER)
Em alguns casos, dois ou mais valores de atributos em um modelo de Entidade-Relacionamento estão relacionados. Por exemplo, os atributos `Idade` e `Data_Nascimento` de um Auditor de Controle Externo. Para uma entidade `AUDITOR` em particular, o valor de `Idade` pode ser determinado pela data corrente do sistema e pelo valor de `Data_Nascimento` persistido. 

Portanto, segundo a teoria formal do MER concebida por Peter Chen, o atributo `Idade` é denominado atributo [ I ], ao passo que `Data_Nascimento` é denominado atributo [ II ].

As lacunas [ I ] e [ II ] são, correta e respectivamente, preenchidas por:

* **A)** armazenado — derivado.
* **B)** derivado — armazenado (ou básico).
* **C)** multivalorado — monovalorado.
* **D)** identificador — composto.
* **E)** determinante — discriminador.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A ordem está invertida: `Idade` é calculado, logo é derivado, não armazenado.
> - **B)** **CORRETA.** Na notação clássica de Peter Chen:
>   - **Atributo Derivado:** É aquele cujo valor não precisa ser persistido fisicamente na base, pois pode ser computado dinamicamente a partir de outro(s) atributo(s) ou do relógio do sistema. Graficamente é representado por uma elipse de contorno tracejado/pontilhado.
>   - **Atributo Armazenado (ou Base):** É o dado primitivo persistido no disco a partir do qual derivações são calculadas.
> - **C)** Incorreta. Ambos são atributos monovalorados (uma pessoa tem uma única data de nascimento e uma única idade em um dado momento).
> - **D)** Incorreta. Identificador é chave primária; `Idade` não identifica unicamente um servidor.
> - **E)** Incorreta. Determinante e discriminador referem-se a chaves primárias e parciais de entidades fortes e fracas.
> 
> **Gabarito: B**

---
"""

q08_f01 = """### Questão 08 (FCC - TRT-1 / Analista Judiciário - TI - Relacionamentos e Mapeamento N:M)
No Modelo Entidade-Relacionamento utilizado para projetar bancos de dados relacionais, quando se define que há um conjunto de relacionamentos de cardinalidade muitos para muitos ($N:M$) entre dois conjuntos de entidades $A$ e $B$, essa especificação significa e exige, do ponto de vista conceitual e de conversão lógica, que:

* **A)** uma entidade de $A$ está associada compulsoriamente a exatamente uma entidade de $B$, e cada entidade de $B$ está associada a no máximo duas entidades de $A$.
* **B)** uma entidade do conjunto $A$ pode estar associada a várias instâncias do conjunto $B$, e uma entidade do conjunto $B$ também pode estar associada a várias instâncias de $A$. Na conversão para o modelo relacional lógico, exige a criação de uma tabela associativa intermediária contendo as chaves primárias de $A$ e $B$ como chaves estrangeiras.
* **C)** os conjuntos de entidades $A$ e $B$ devem necessariamente possuir esquemas idênticos com o mesmo número e tipos de atributos primitivos.
* **D)** a chave primária de $A$ deve ser migrada diretamente como atributo simples e chave estrangeira na tabela $B$, tornando dispensável a criação de qualquer nova relação no banco de dados.
* **E)** uma entidade do conjunto $B$ associa-se a apenas uma entidade de $A$, configurando uma dependência existencial que transforma a entidade $B$ em entidade fraca.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A cardinalidade $N:M$ não restringe as associações a números fixos como "exatamente uma" ou "no máximo duas".
> - **B)** **CORRETA.** O relacionamento muitos-para-muitos ($N:M$) define que cada registro em $A$ pode relacionar-se com zero, um ou vários registros em $B$, e vice-versa. Na etapa de conversão lógica para o modelo relacional, um relacionamento $N:M$ não pode ser resolvido com inserção de chave estrangeira simples em nenhuma das tabelas originais sem violar a Primeira Forma Normal (1FN); logo, é mandatória a criação de uma **tabela associativa** (tabela de junção) cuja chave primária é tipicamente composta pelas chaves estrangeiras que referenciam $A$ e $B$.
> - **C)** Incorreta. Entidades relacionadas não precisam compartilhar os mesmos atributos.
> - **D)** Incorreta. A migração direta de FK resolve relacionamentos $1:N$ (migra-se a PK do lado 1 para a tabela do lado $N$), mas é inviável em $N:M$.
> - **E)** Incorreta. A assertiva descreve um relacionamento $1:N$ com dependência de existência, não uma relação $N:M$.
> 
> **Gabarito: B**

---
"""

q09_f01 = """### Questão 09 (FGV - TJ-BA / Analista Judiciário - TI - Dependências Funcionais e Axiomas de Armstrong)
Considere uma relação $R(A, B, C, D)$ sobre a qual vigora o seguinte conjunto de dependências funcionais primitivas:

$$F = \\{ A \\rightarrow B, \\quad A \\rightarrow C, \\quad C \\rightarrow D \\}$$

Com base nos Axiomas de Armstrong (Reflexividade, Aumento e Transitividade) e em suas regras derivadas (União, Decomposição e Pseudotransitividade), assinale a dependência funcional que **NÃO** pode ser derivada logicamente de $F$:

* **A)** $B \\rightarrow C$
* **B)** $A \\rightarrow D$
* **C)** $A \\rightarrow B, C$
* **D)** $A, B, C \\rightarrow A, B$
* **E)** $C, B \\rightarrow D, B$

> **Comentário Detalhado:**
>
> - **A)** **CORRETA (não pode ser derivada).** Para verificar se $B \\rightarrow C$ é válida, calculamos o fechamento de atributos de $B$, denotado por $B^+$: como não há nenhuma regra em $F$ com $B$ no lado esquerdo determinante, temos $B^+ = \\{B\\}$. Como $C \\notin B^+$, a dependência $B \\rightarrow C$ é **falsa** e não pode ser inferida a partir de $F$.
> - **B)** Incorreta (pode ser derivada). Pela regra da Transitividade: como $A \\rightarrow C$ e $C \\rightarrow D$, então $A \\rightarrow D$ é válida ($A^+ = \\{A, B, C, D\\}$).
> - **C)** Incorreta (pode ser derivada). Pela regra da União: como $A \\rightarrow B$ e $A \\rightarrow C$, então $A \\rightarrow B, C$ é válida.
> - **D)** Incorreta (pode ser derivada). Pelo Axioma da Reflexividade: como $\\{A, B\\} \\subseteq \\{A, B, C\\}$, a dependência trivial $A, B, C \\rightarrow A, B$ é universalmente verdadeira.
> - **E)** Incorreta (pode ser derivada). Pelo Axioma do Aumento: dada a dependência $C \\rightarrow D$, adicionando o atributo $B$ a ambos os lados da implicação, obtém-se $C, B \\rightarrow D, B$.
> 
> **Gabarito: A**

---
"""

q10_f01 = """### Questão 10 (FGV - TRT / Analista Judiciário - TI - Normalização e Primeira Forma Normal)
O modelo de dados conceitual de um sistema de gestão de recursos humanos prevê a entidade `FUNCIONARIO`. Para fins de cálculo de benefícios e assistência médica, é necessário cadastrar os dados dos dependentes de cada funcionário (`NomeDependente`, `DataNascDependente`, `Parentesco`), sem limite superior de quantidade.

Para implementar esse modelo em um banco de dados relacional assegurando a conformidade rigorosa com a **Primeira Forma Normal (1FN)**, avalie as seguintes abordagens técnicas:

I. Armazenar no registro do funcionário um atributo estruturado do tipo vetor/array contendo os dados empacotados de todos os dependentes.  
II. Replicar a linha do funcionário na tabela principal tantas vezes quantos forem os dependentes cadastrados, variando apenas os dados do dependente.  
III. Criar uma tabela autônoma `DEPENDENTE` vinculada à tabela `FUNCIONARIO` por meio de uma chave estrangeira (`IdFuncionario`), com chave primária composta por `(IdFuncionario, NumSequencialDependente)`.  

Conforme a teoria da normalização relacional de Codd, está correto apenas o que se afirma em:

* **A)** I.
* **B)** II.
* **C)** III.
* **D)** I e II.
* **E)** II e III.

> **Comentário Detalhado:**
>
> - **I.** Incorreta. O uso de vetores, listas ou colunas multivaloradas viola explicitamente o requisito basilar da Primeira Forma Normal (1FN), segundo o qual todos os atributos de uma relação devem possuir domínios puramente **atômicos** (indivisíveis).
> - **II.** Incorreta. Replicar a tupla inteira do funcionário para cada dependente cria redundância massiva, anomalias graves de atualização/exclusão e viola a integridade de entidade caso a chave primária seja apenas o identificador do funcionário.
> - **III.** **CORRETA.** A técnica canônica para resolver atributos multivalorados ou grupos repetitivos e atender à 1FN consiste em decompor a estrutura: cria-se uma tabela separada (`DEPENDENTE`) que herda a chave da entidade principal como chave estrangeira (`FK`), garantindo atomicidade estrita em todas as colunas.
> 
> **Gabarito: C**

---
"""

q11_f01 = """### Questão 11 (FGV - TJ-AP / Analista Judiciário - Banco de Dados - Desnormalização e Trade-offs OLTP vs. OLAP)
No projeto de bancos de dados analíticos (Data Warehouses) e repositórios de dados para auditoria contínua, analistas de TI frequentemente ponderam entre o esquema puramente em estrela (*Star Schema*) e o esquema em flocos de neve (*Snowflake Schema*).

A respeito da técnica de modelagem multidimensional e de seus impactos arquiteturais sobre o desempenho das consultas analíticas, assinale a afirmativa correta:

* **A)** A normalização das tabelas de dimensão (esquema Snowflake) elimina redundâncias, mas impacta negativamente o tempo de resposta das consultas analíticas (OLAP) ao exigir uma maior quantidade de junções (*joins*) entre tabelas normalizadas.
* **B)** O esquema Star Schema é totalmente normalizado até a Boyce-Codd Normal Form (BCNF), o que minimiza o espaço de armazenamento consumido em disco e maximiza a quantidade de tabelas no data warehouse.
* **C)** A técnica de desnormalização é fortemente recomendada em sistemas puramente transacionais (OLTP) de alta concorrência para acelerar as operações concorrentes de `INSERT` e `UPDATE`.
* **D)** A criação de chaves substitutas (*surrogate keys*) nas tabelas dimensionais prejudica a governança e inviabiliza o rastreamento histórico de dimensões de alteração lenta (SCD).
* **E)** O Snowflake Schema é o padrão adotado em todos os data marts por dispensar completamente o uso de índices e por apresentar desempenho de leitura invariavelmente superior ao Star Schema.

> **Comentário Detalhado:**
>
> - **A)** **CORRETA.** O modelo *Snowflake* decompõe as tabelas de dimensão em múltiplas sub-tabelas normalizadas (ex.: normalizar `Cidade` e `Estado` para fora da dimensão `Cliente`). Embora reduza o consumo de armazenamento ao eliminar dados duplicados, ele degrada significativamente o desempenho de consultas OLAP complexas porque força o motor SQL a executar múltiplos *joins* pesados para reconstituir o contexto da dimensão. Já o *Star Schema* adota dimensões propositalmente desnormalizadas, favorecendo consultas simples e varreduras extremamente rápidas.
> - **B)** Incorreta. O *Star Schema* é intencionalmente **desnormalizado** em suas dimensões; quem busca normalização dimensional é o modelo Snowflake.
> - **C)** Incorreta. Em sistemas OLTP, a desnormalização introduz redundância de dados que encarece e desacelera operações de escrita (`INSERT`, `UPDATE`), além de gerar riscos de inconsistência transacional.
> - **D)** Incorreta. As chaves substitutas (*surrogate keys*) são essenciais justamente para permitir o gerenciamento de dimensões que mudam lentamente (Slowly Changing Dimensions - SCD Tipos 2 e 3).
> - **E)** Incorreta. O *Star Schema* é a estrutura dimensional predominante e recomendada por Ralph Kimball para data marts justamente por sua simplicidade e superior performance em leitura.
> 
> **Gabarito: A**

---
"""

print("Q06-Q11 for File 01 defined.")
