# 03 - Ciclo de Vida Assistido: Geração, Testes e Depuração

> **Matéria:** Engenharia de Software Assistida por IA e Sistemas Agentivos  
> **Cargo:** B02 – Técnico de Controle Externo – Especialidade: Tecnologia da Informação  
> **Arquivo:** `03_ciclo_de_vida_assistido_geracao_testes_e_depuracao.md`  



---


## 📌 Ementa / Itens do Edital
- Geração de código assistida por IA
- Revisão automatizada de código (AI Code Review)
- Documentação técnica e geração de contratos assistidos por IA
- Depuração (debugging) assistida por IA
- Geração automatizada de testes de software

---

## 🧭 Sumário

1. [Geração de Código Assistida por Inteligência Artificial](#1-geracao-de-codigo-assistida-por-inteligencia-artificial)
    1. [Scaffolding, Código Repetitivo (Boilerplate) e CRUDs Estruturais](#11-scaffolding-codigo-repetitivo-boilerplate-e-cruds-estruturais)
    2. [Síntese de Algoritmos Complexos e Regras de Negócio](#12-sintese-de-algoritmos-complexos-e-regras-de-negocio)
    3. [Modernização e Tradução de Sistemas Legados: Riscos Aritméticos](#13-modernizacao-e-traducao-de-sistemas-legados-riscos-aritmeticos)
    4. [Completamento Inteligente de Código: Ghost Text e AST Local](#14-completamento-inteligente-de-codigo-ghost-text-e-ast-local)
    5. [Teste 139](#Teste-139)
    6. [Teste 140](#Teste-140)
2. [Revisão Automatizada de Código (AI Code Review)](#2-revisao-automatizada-de-codigo-ai-code-review)
    1. [Linters Estáticos Tradicionais (AST/SAST) vs. Agentes de AI Code Review](#21-linters-estaticos-tradicionais-astsast-vs-agentes-de-ai-code-review)
    2. [Identificação de Code Smells, Débito Técnico e Violações de SOLID](#22-identificacao-de-code-smells-debito-tecnico-e-violacoes-de-solid)
    3. [Varredura Automática de Vulnerabilidades e Vazamento de Segredos](#23-varredura-automatica-de-vulnerabilidades-e-vazamento-de-segredos)
    4. [Síntese de Pull Requests e Notas de Lançamento (Release Notes)](#24-sintese-de-pull-requests-e-notas-de-lancamento-release-notes)
    5. [Teste 141](#Teste-141)
    6. [Teste 142](#Teste-142)
    7. [Teste 143](#Teste-143)
3. [Documentação Técnica e Geração de Contratos](#3-documentacao-tecnica-e-geracao-de-contratos)
    1. [Docstrings, Javadoc e Comentários Semânticos](#31-docstrings-javadoc-e-comentarios-semanticos)
    2. [Engenharia Reversa de Contratos de API (OpenAPI 3.0 / Swagger)](#32-engenharia-reversa-de-contratos-de-api-openapi-30-swagger)
    3. [Diagramação Arquitetural Declarativa com Mermaid.js e PlantUML](#33-diagramacao-arquitetural-declarativa-com-mermaidjs-e-plantuml)
    4. [Teste 144](#Teste-144)
4. [Depuração (Debugging) e Diagnóstico de Erros Assistidos por IA](#4-depuracao-debugging-e-diagnostico-de-erros-assistidos-por-ia)
    1. [Análise de Stack Traces e Decodificação de Erros Críticos](#41-analise-de-stack-traces-e-decodificacao-de-erros-criticos)
    2. [Análise Forense de Logs de Produção e Vazamentos de Recursos](#42-analise-forense-de-logs-de-producao-e-vazamentos-de-recursos)
    3. [Análise de Causa-Raiz (Root Cause Analysis - RCA) e Patches Mínimos](#43-analise-de-causa-raiz-root-cause-analysis-rca-e-patches-minimos)
    4. [Teste 145](#Teste-145)
    5. [Teste 146](#Teste-146)
5. [Geração Automatizada de Testes de Software](#5-geracao-automatizada-de-testes-de-software)
    1. [A Grande Armadilha: Testar a Implementação Defeituosa vs. o Comportamento](#51-a-grande-armadilha-testar-a-implementacao-defeituosa-vs-o-comportamento)
    2. [Cobertura Sistemática de Casos de Borda (Edge Cases)](#52-cobertura-sistematica-de-casos-de-borda-edge-cases)
    3. [Geração de Cenários BDD Executáveis (Gherkin)](#53-geracao-de-cenarios-bdd-executaveis-gherkin)
    4. [Testes de Mutação (Mutation Testing): Avaliando a Real Eficácia dos Testes](#54-testes-de-mutacao-mutation-testing-avaliando-a-real-eficacia-dos-testes)
    5. [Teste 147](#Teste-147)
    6. [Teste 148](#Teste-148)
    7. [Teste 149](#Teste-149)
6. [Fontes Recomendadas na Internet](#6-fontes-recomendadas-na-internet)

---

## 1. Geração de Código Assistida por Inteligência Artificial

### 1.1 Scaffolding, Código Repetitivo (Boilerplate) e CRUDs Estruturais
A automação de código por meio de modelos generativos impacta profundamente a velocidade de entrega nas fases inaugurais de projetos:

- **Redução do Esforço em Boilerplate:** Tarefas repetitivas e mecânicas — como a criação de classes de entidade (*JPA/Hibernate*), objetos de transferência de dados (*DTOs*), mapeadores (*Mappers/MapStruct*), repositórios (*Spring Data JPA*) e controladores REST — são geradas em segundos a partir de especificações de esquema relacional (DDL) ou contratos de interface.
- **Anotações de Validação:** A IA infere e aplica automaticamente regras de validação padronizadas (`@NotNull`, `@Size`, `@NotBlank`, `@Email`, `@PositiveOrZero`), diminuindo falhas de integridade na camada de borda da API.
- **Foco no Domínio:** Ao transferir a codificação mecânica de infraestrutura para a IA, os engenheiros de software concentram-se no núcleo das regras de negócio fiscais, auditoria orçamentária e conformidade jurídica.

### 1.2 Síntese de Algoritmos Complexos e Regras de Negócio
A partir de especificações funcionais ricas redigidas em linguagem natural, modelos de linguagem avançados deduzem a lógica algorítmica imperativa correspondente:

- **Cálculos Fiscais e Previdenciários:** Implementação de tabelas progressivas de alíquotas, regras de transição de benefícios e apuração de juros moratórios.
- **Algoritmos em Grafos e Otimização:** Algoritmos de ordenação topológica para detecção de dependências cíclicas em fluxos de processos administrativos.
- **Pré-requisito Vital:** A qualidade e corretude do algoritmo gerado dependem estritamente da clareza com que o desenvolvedor estabelece as **pré-condições, pós-condições e invariantes lógicas** na especificação enviada.

### 1.3 Modernização e Tradução de Sistemas Legados: Riscos Aritméticos
A migração de sistemas governamentais legados (especialmente rotinas tributárias e de arrecadação em COBOL ou PL/SQL para microsserviços modernos em Java 21, Kotlin ou Python) é uma das aplicações mais estratégicas de IA no setor público.

```mermaid
flowchart LR
    COB["Código Legado: COBOL / PL-SQL
    - Aritmética Packed Decimal (COMP-3)
    - Variáveis Globais de Trabalho"] --> AG["Agente de Migração de Código (LLM)"]
    AG --> CODE["Novo Código: Java 21 / Python 3"]
    CODE --> CHECK{"Validação de Paridade Aritmética"}
    CHECK -->|Utilizou double / float IEEE 754| ERR["❌ Erro Crítico: Perda de precisão e centavos"]
    CHECK -->|Utilizou BigDecimal / Decimal| OK["✅ Paridade Aritmética Garantida"]
```

> 🚨 **ALERTA DE PROVA / FCC:**  
> **A Armadilha do Ponto Flutuante Binário:**  
>
> - Em sistemas contábeis e fiscais legados (COBOL), a representação numérica decimal de ponto fixo (`COMP-3`) assegura precisão absoluta de centavos.  
> - Ao traduzir esse código para Java ou Python, modelos de IA frequentemente sugerem tipos primitivos de ponto flutuante binário (`float` ou `double`), por serem mais concisos.  
> - Contudo, os tipos `float` e `double` (norma IEEE 754) introduzem **imprecisões binárias de arredondamento cumulativo** em cálculos de moedas e alíquotas (ex.: `0.1 + 0.2 != 0.3`).  
> - Em código fiscal de órgãos de controle externo, é **mandatório o uso de classes de precisão arbitrária exata (`java.math.BigDecimal` em Java ou o módulo `decimal` em Python)** com estratégias explícitas de arredondamento (`RoundingMode.HALF_EVEN`).

### 1.4 Completamento Inteligente de Código: Ghost Text e AST Local
Assistentes de desenvolvimento integrados à IDE operam combinando predição estatística de tokens com inspeção estrutural estática:

- **Ghost Text:** Exibição em cinza de blocos inteiros de código sugerido antes da digitação.
- **Contexto da AST (Abstract Syntax Tree):** O assistente inspeciona a árvore sintática do arquivo em edição, classes importadas, tipos retornados por métodos e abas adjacentes recentemente abertas, assegurando coerência tipográfica e semântica com o restante da solução.

---

### Teste 139
**(FCC – TRT-13 – Analista Judiciario Tecnologia da Informacao – 2014)**
Considere o código abaixo, digitado em Python. a, b = 0, 1 while b < 10: print b a, b = b, a+b No final da execução do código, o último valor armazenado nas variáveis a e b serão, respectivamente,

* **A)** 13 e 21.
* **B)** 8 e 13.
* **C)** 5 e 10.
* **D)** 13 e 20.
* **E)** 8 e 10.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "13 e 21". De acordo com a teoria estudada em *1.3 Modernização e Tradução de Sistemas Legados: Riscos Aritméticos*, ao traduzir esse código para Java ou Python, modelos de IA frequentemente sugerem tipos primitivos de ponto flutuante binário (`float` ou `double`), por serem mais concisos.
> - **B)** **Correta.** Conforme fundamentado na seção *3.1 Docstrings, Javadoc e Comentários Semânticos* deste guia, python (PEP 257): Docstrings estruturadas explicando o comportamento de funções, tipos de argumentos e invariantes de execução. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT-13/2014) ao estabelecer que "8 e 13".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "5 e 10". De acordo com a teoria estudada em *1.3 Modernização e Tradução de Sistemas Legados: Riscos Aritméticos*, em código fiscal de órgãos de controle externo, é mandatório o uso de classes de precisão arbitrária exata (`java.math.BigDecimal` em Java ou o módulo `decimal` em Python) com estratégias explícitas de arredondamento (`RoundingMode.HALF_EVEN`).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "13 e 20". De acordo com a teoria estudada em *1.3 Modernização e Tradução de Sistemas Legados: Riscos Aritméticos*, a migração de sistemas governamentais legados (especialmente rotinas tributárias e de arrecadação em COBOL ou PL/SQL para microsserviços modernos em Java 21, Kotlin ou Python) é uma das aplicações mais estratégicas de IA no setor público.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "8 e 10". De acordo com a teoria estudada em *4.1 Análise de Stack Traces e Decodificação de Erros Críticos*, traduz mensagens herméticas para linguagem natural, explicando a condição de contorno que causou a falha (ex.: violação de chave estrangeira por registro órfão ou valor nulo não tratado).
>
> **Gabarito: B**

---

### Teste 140
**(FGV – TJ-MT – Analista Judiciario Tecnologia da Informacao – 2024)**
Em uma cidade inteligente, diversos dispositivos conectados, como sensores de trânsito, câmeras de segurança e medidores de energia, trocam informações entre si para otimizar o uso de recursos e melhorar a qualidade de vida dos cidadãos. Esse conceito é conhecido como

* **A)** Computação em Nuvem.
* **B)** Big Data.
* **C)** Inteligência Artificial.
* **D)** Internet das Coisas (IoT).
* **E)** Realidade Aumentada.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Computação em Nuvem". De acordo com a teoria estudada em *1.2 Síntese de Algoritmos Complexos e Regras de Negócio*, pré-requisito Vital: A qualidade e corretude do algoritmo gerado dependem estritamente da clareza com que o desenvolvedor estabelece as pré-condições, pós-condições e invariantes lógicas na especificação enviada.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Big Data". De acordo com a teoria estudada em *1.1 Scaffolding, Código Repetitivo (Boilerplate) e CRUDs Estruturais*, redução do Esforço em Boilerplate: Tarefas repetitivas e mecânicas — como a criação de classes de entidade (*JPA/Hibernate*), objetos de transferência de dados (*DTOs*), mapeadores (*Mappers/MapStruct*), repositórios (*Spring Data JPA*) e controladores REST — são geradas em segundos a partir de especificações de esquema relacional (DDL) ou contratos de interface.
> - **C)** **Correta.** Conforme fundamentado na seção *1.3 Modernização e Tradução de Sistemas Legados: Riscos Aritméticos* deste guia, em código fiscal de órgãos de controle externo, é mandatório o uso de classes de precisão arbitrária exata (`java.math.BigDecimal` em Java ou o módulo `decimal` em Python) com estratégias explícitas de arredondamento (`RoundingMode.HALF_EVEN`). Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ-MT/2024) ao estabelecer que "Inteligência Artificial".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Internet das Coisas (IoT)". De acordo com a teoria estudada em *2.1 Linters Estáticos Tradicionais (AST/SAST) vs. Agentes de AI Code Review*, custo Computacional: Praticamente nulo; execução local instantânea sem dependência de internet ou APIs externas. — Moderado a alto; demanda chamadas de rede para inferência em aceleradores (GPUs/TPUs).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Realidade Aumentada". De acordo com a teoria estudada em *1.4 Completamento Inteligente de Código: Ghost Text e AST Local*, assistentes de desenvolvimento integrados à IDE operam combinando predição estatística de tokens com inspeção estrutural estática.
>
> **Gabarito: C**

---

## 2. Revisão Automatizada de Código (AI Code Review)

### 2.1 Linters Estáticos Tradicionais (AST/SAST) vs. Agentes de AI Code Review
A integração de agentes de IA generativa em esteiras de CI/CD para inspeção de *Pull Requests* não substitui, mas complementa as ferramentas de análise estática convencionais:

```mermaid
flowchart TD
    subgraph Pipeline["Esteira de CI/CD no Pull Request"]
        PR["Desenvolvedor abre Pull Request"] --> LINT["Linters Determinísticos (SonarQube / ESLint / Checkstyle)"]
        PR --> AI["Agente de AI Code Review (LLM Especializado)"]
        
        LINT -->|Relatório Sintático e Métricas de Cobertura| REL["Painel do Pull Request"]
        AI -->|Análise Semântica, Lógica de Negócio e Resumo| REL
        
        REL --> HUM["Revisão por Pares Humana (Tech Lead / Auditor)"]
        HUM -->|Aprovação Conclusiva| MERGE["Merge na Branch Principal"]
    end
```

| Critério de Comparação | Analisadores Estáticos Determinísticos (Linters / SAST) | Agentes de AI Code Review (Baseados em LLMs) |
|---|---|---|
| **Exemplos de Mercado** | SonarQube, Checkstyle, ESLint, FindBugs. | CodeRabbit, PR-Agent, GitHub Copilot PR Reviewer. |
| **Mecanismo Operacional** | Regras determinísticas imutáveis sobre AST, expressões regulares e grafos formais de fluxo de controle. | Inferência semântica probabilística e contextual sobre a intenção do desenvolvedor e o domínio do problema. |
| **Custo Computacional** | Praticamente nulo; execução local instantânea sem dependência de internet ou APIs externas. | Moderado a alto; demanda chamadas de rede para inferência em aceleradores (GPUs/TPUs). |
| **Compreensão de Negócio** | **Nula**. Incapaz de identificar se um cálculo tributário inverteu uma regra fiscal (ex.: aplicou desconto no lugar de acréscimo legal). | **Alta**. Consegue correlacionar a descrição textual da *issue* com o código implementado, detectando desvios semânticos. |
| **Papel na Governança** | Base obrigatória e inegociável de conformidade de estilo, cobertura e padrões de código. | Camada inteligente de triagem, síntese de alterações e detecção de falhas lógicas sutis para apoiar a revisão humana. |

### 2.2 Identificação de Code Smells, Débito Técnico e Violações de SOLID
Os modelos de revisão atuam ativamente na prevenção de débito técnico em PRs:

- **Classes Deus (*God Classes*):** Alerta quando uma classe acumula dezenas de responsabilidades distintas, violando o Princípio da Responsabilidade Única (SRP).
- **Complexidade Ciclomática Excessiva:** Identificação de encadeamentos profundos de estruturas condicionais (`if`/`else` aninhados) e proposição de refatoração para o padrão *Strategy* ou *Polimorfismo*.
- **Código Duplicado e Obsolescência:** Identificação de reimplementações de funções utilitárias que já existem no ecossistema da biblioteca padrão.

### 2.3 Varredura Automática de Vulnerabilidades e Vazamento de Segredos
Durante o ciclo de revisão, os agentes aplicam filtros baseados nas diretrizes OWASP Top 10 e CWE:

- **Injeção de SQL (SQL Injection):** Identificação de interpolação direta de parâmetros de usuário em consultas HQL/JPQL ou SQL puro, recomendando consultas parametrizadas (*Prepared Statements*).
- **Vazamento de Credenciais (*Hardcoded Secrets*):** Detecção de chaves privadas, senhas de banco de dados, tokens de APIs e certificados digitais inseridos inadvertidamente em arquivos rastreados pelo Git.
- **Cross-Site Scripting (XSS) e Desserialização Insegura:** Alerta sobre a renderização direta de payloads HTML sem sanitização prévia.

### 2.4 Síntese de Pull Requests e Notas de Lançamento (Release Notes)
A IA lê o conjunto completo de alterações (*diffs*) entre branches e sintetiza automaticamente:

- Um resumo executivo claro das mudanças para os revisores humanos;
- Lista de arquivos alterados agrupados por domínio de impacto;
- Minuta preliminar das notas de versão (*Release Notes*) em conformidade com o padrão *Keep a Changelog*.

---

### Teste 141
**(FGV – TRT-24 – Analista Judiciario Area Apoio Especializado Tecnologia da Informacao – 2025)**
A biblioteca Python de código aberto que utiliza tensores de forma otimizada para aplicações de aprendizado profundo usando GPUs ou CPUs se chama

* **A)** pytensorflow.
* **B)** pymatrix.
* **C)** pytorch.
* **D)** pynum.
* **E)** pyxpu.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "pytensorflow". De acordo com a teoria estudada em *1.3 Modernização e Tradução de Sistemas Legados: Riscos Aritméticos*, a migração de sistemas governamentais legados (especialmente rotinas tributárias e de arrecadação em COBOL ou PL/SQL para microsserviços modernos em Java 21, Kotlin ou Python) é uma das aplicações mais estratégicas de IA no setor público.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "pymatrix". De acordo com a teoria estudada em *2.1 Linters Estáticos Tradicionais (AST/SAST) vs. Agentes de AI Code Review*, custo Computacional: Praticamente nulo; execução local instantânea sem dependência de internet ou APIs externas. — Moderado a alto; demanda chamadas de rede para inferência em aceleradores (GPUs/TPUs).
> - **C)** **Correta.** Conforme fundamentado na seção *2.2 Identificação de Code Smells, Débito Técnico e Violações de SOLID* deste guia, código Duplicado e Obsolescência: Identificação de reimplementações de funções utilitárias que já existem no ecossistema da biblioteca padrão. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT-24/2025) ao estabelecer que "pytorch".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "pynum". De acordo com a teoria estudada em *1.3 Modernização e Tradução de Sistemas Legados: Riscos Aritméticos*, ao traduzir esse código para Java ou Python, modelos de IA frequentemente sugerem tipos primitivos de ponto flutuante binário (`float` ou `double`), por serem mais concisos.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "pyxpu". De acordo com a teoria estudada em *1.3 Modernização e Tradução de Sistemas Legados: Riscos Aritméticos*, em código fiscal de órgãos de controle externo, é mandatório o uso de classes de precisão arbitrária exata (`java.math.BigDecimal` em Java ou o módulo `decimal` em Python) com estratégias explícitas de arredondamento (`RoundingMode.HALF_EVEN`).
>
> **Gabarito: C**

---

### Teste 142
**(FGV – TRT-16 – Analista Judiciario Area Administrativa Tecnologia da Informacao – 2022)**
Analise o código a seguir, que descreve a entidade Carro: A anotação JPA, versão 2.0, a ser incluída na linha 9 para indicar que as cores da entidade Carro devem ser armazenadas em uma tabela separada da tabela carros, é

* **A)** @CollectionAttribute
* **B)** @ElementCollection
* **C)** @Embeddable
* **D)** @Embedded
* **E)** @InnerTable

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "@CollectionAttribute". De acordo com a teoria estudada em *4.1 Análise de Stack Traces e Decodificação de Erros Críticos*, localiza cirurgicamente o método corporativo na linha exata onde a exceção foi lançada.
> - **B)** **Correta.** Conforme fundamentado na seção *1.1 Scaffolding, Código Repetitivo (Boilerplate) e CRUDs Estruturais* deste guia, redução do Esforço em Boilerplate: Tarefas repetitivas e mecânicas — como a criação de classes de entidade (*JPA/Hibernate*), objetos de transferência de dados (*DTOs*), mapeadores (*Mappers/MapStruct*), repositórios (*Spring Data JPA*) e controladores REST — são geradas em segundos a partir de especificações de esquema relacional (DDL) ou contratos de interface. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT-16/2022) ao estabelecer que "@ElementCollection".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "@Embeddable". De acordo com a teoria estudada em *4.3 Análise de Causa-Raiz (Root Cause Analysis - RCA) e Patches Mínimos*, devem-se evitar refatorações cosméticas em massa durante a aplicação de correções críticas (*hotfixes*), minimizando o risco de efeitos colaterais indesejados no ambiente de produção.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "@Embedded". De acordo com a teoria estudada em *2.4 Síntese de Pull Requests e Notas de Lançamento (Release Notes)*, minuta preliminar das notas de versão (*Release Notes*) em conformidade com o padrão *Keep a Changelog*.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "@InnerTable". De acordo com a teoria estudada em *3.3 Diagramação Arquitetural Declarativa com Mermaid.js e PlantUML*, diagramas de Classes e Entidade-Relacionamento: Representação visual do modelo relacional a partir do código das entidades.
>
> **Gabarito: B**

---

### Teste 143
**(FGV – TJ-AP – Analista Judiciario Apoio Especializado Tecnologia da Informacao Desenvolvimento de Sistemas – 2023)**
A analista Joelma está desenvolvendo o web service tjapRest utilizando o Spring Boot. Determinadas operações de tjapRest devem ser executadas assincronamente. Para implementar as operações assíncronas de forma simples e direta, Joelma recorreu a duas anotações padrões do Spring. A primeira anotação habilita o suporte do Spring à execução de métodos assíncronos. A segunda anotação marca determinado método como um candidato à execução assíncrona. Joelma recorreu às anotações do Spring:

* **A)** @EnableAsync e @Async;
* **B)** @AsyncConfigurer e @Async;
* **C)** @EnableAsync e @Asynchronous;
* **D)** @AsyncConfigurer e @EnableAsync;
* **E)** @AsyncConfigurer e @Asynchronous.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *2.1 Linters Estáticos Tradicionais (AST/SAST) vs. Agentes de AI Code Review* deste guia, custo Computacional: Praticamente nulo; execução local instantânea sem dependência de internet ou APIs externas. — Moderado a alto; demanda chamadas de rede para inferência em aceleradores (GPUs/TPUs). Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ-AP/2023) ao estabelecer que "@EnableAsync e @Async".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "@AsyncConfigurer e @Async". De acordo com a teoria estudada em *2.1 Linters Estáticos Tradicionais (AST/SAST) vs. Agentes de AI Code Review*, papel na Governança: Base obrigatória e inegociável de conformidade de estilo, cobertura e padrões de código. — Camada inteligente de triagem, síntese de alterações e detecção de falhas lógicas sutis para apoiar a revisão humana.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "@EnableAsync e @Asynchronous". De acordo com a teoria estudada em *2.3 Varredura Automática de Vulnerabilidades e Vazamento de Segredos*, injeção de SQL (SQL Injection): Identificação de interpolação direta de parâmetros de usuário em consultas HQL/JPQL ou SQL puro, recomendando consultas parametrizadas (*Prepared Statements*).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "@AsyncConfigurer e @EnableAsync". De acordo com a teoria estudada em *2.3 Varredura Automática de Vulnerabilidades e Vazamento de Segredos*, cross-Site Scripting (XSS) e Desserialização Insegura: Alerta sobre a renderização direta de payloads HTML sem sanitização prévia.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "@AsyncConfigurer e @Asynchronous". De acordo com a teoria estudada em *1.1 Scaffolding, Código Repetitivo (Boilerplate) e CRUDs Estruturais*, anotações de Validação: A IA infere e aplica automaticamente regras de validação padronizadas (`@NotNull`, `@Size`, `@NotBlank`, `@Email`, `@PositiveOrZero`), diminuindo falhas de integridade na camada de borda da API.
>
> **Gabarito: A**

---

## 3. Documentação Técnica e Geração de Contratos

### 3.1 Docstrings, Javadoc e Comentários Semânticos
A documentação no nível do código-fonte é sintetizada de acordo com os padrões da linguagem:

- **Java (Javadoc):** Descrição formal de classes, métodos, parâmetros (`@param`), valores de retorno (`@return`) e exceções disparadas (`@throws`).
- **Python (PEP 257):** Docstrings estruturadas explicando o comportamento de funções, tipos de argumentos e invariantes de execução.
- **Regra de Ouro:** A documentação gerada deve focar no **"PORQUÊ"** daquela decisão arquitetural, e não apenas na descrição óbvia do código que qualquer programador conseguiria ler diretamente.

### 3.2 Engenharia Reversa de Contratos de API (OpenAPI 3.0 / Swagger)
Ao inspecionar classes controladoras (*controllers*) e modelos de dados DTO, a IA é capaz de gerar o contrato formal de API em sintaxe YAML/JSON:

- Mapeamento de rotas, verbos HTTP e códigos de resposta (`200 OK`, `201 Created`, `400 Bad Request`, `404 Not Found`);
- Descrição de esquemas de segurança no bloco `components/securitySchemes` (Bearer JWT, OAuth2);
- Exemplos de payloads válidos de requisição e resposta.

### 3.3 Diagramação Arquitetural Declarativa com Mermaid.js e PlantUML
Em vez de diagramas estáticos desenhados em ferramentas gráficas externas (que ficam rapidamente desatualizados), o agente de IA sintetiza diagramas baseados em texto dentro da própria documentação Markdown:

- **Diagramas de Classes e Entidade-Relacionamento:** Representação visual do modelo relacional a partir do código das entidades;
- **Diagramas de Sequência:** Mapeamento visual das trocas de mensagens assíncronas entre microsserviços via filas Kafka ou chamadas HTTP REST.

---

### Teste 144
**(FGV – TRT-16 – Analista Judiciario Area Administrativa Tecnologia da Informacao – 2022)**
Michael coleciona moedas brasileiras, americanas e francesas. Para cada 3 moedas americanas Michael tem 7 moedas brasileiras e para cada 5 moedas brasileiras, ele tem 2 francesas. Com relação às moedas de Michael, a razão entre a quantidade de moedas brasileiras e a quantidade de moedas não brasileiras é igual a 7

* **A)** 5. 12
* **B)** 7 . 25
* **C)** 19. 30
* **D)** 23. 35
* **E)** 29.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "5. 12". De acordo com a teoria estudada em *3.1 Docstrings, Javadoc e Comentários Semânticos*, a documentação no nível do código-fonte é sintetizada de acordo com os padrões da linguagem.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "7 . 25". De acordo com a teoria estudada em *3.1 Docstrings, Javadoc e Comentários Semânticos*, java (Javadoc): Descrição formal de classes, métodos, parâmetros (`@param`), valores de retorno (`@return`) e exceções disparadas (`@throws`).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "19. 30". De acordo com a teoria estudada em *3.1 Docstrings, Javadoc e Comentários Semânticos*, python (PEP 257): Docstrings estruturadas explicando o comportamento de funções, tipos de argumentos e invariantes de execução.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "23. 35". De acordo com a teoria estudada em *3.1 Docstrings, Javadoc e Comentários Semânticos*, regra de Ouro: A documentação gerada deve focar no "PORQUÊ" daquela decisão arquitetural, e não apenas na descrição óbvia do código que qualquer programador conseguiria ler diretamente.
> - **E)** **Correta.** Conforme fundamentado na seção *1.3 Modernização e Tradução de Sistemas Legados: Riscos Aritméticos* deste guia, contudo, os tipos `float` e `double` (norma IEEE 754) introduzem imprecisões binárias de arredondamento cumulativo em cálculos de moedas e alíquotas (ex.: `0.1 + 0.2 != 0.3`). Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT-16/2022) ao estabelecer que "29".
>
> **Gabarito: E**

---

## 4. Depuração (Debugging) e Diagnóstico de Erros Assistidos por IA

### 4.1 Análise de Stack Traces e Decodificação de Erros Críticos
Frameworks corporativos modernos emitem rastreamentos de pilha (*stack traces*) extensos contendo centenas de linhas de chamadas internas da infraestrutura (Spring, Tomcat, Hibernate).

- O agente atua filtrando o ruído de bibliotecas de terceiros;
- Localiza cirurgicamente o método corporativo na linha exata onde a exceção foi lançada;
- Traduz mensagens herméticas para linguagem natural, explicando a condição de contorno que causou a falha (ex.: violação de chave estrangeira por registro órfão ou valor nulo não tratado).

### 4.2 Análise Forense de Logs de Produção e Vazamentos de Recursos
Ao processar logs em formato estruturado (JSON, Logstash, Log4j), a IA correlaciona eventos dispersos temporalmente:

- **Esgotamento de Pool de Conexões (*Connection Pool Exhaustion*):** Detecta que determinados endpoints demoram para liberar conexões com o banco de dados por ausência de blocos `try-with-resources` (`AutoCloseable`), culminando no travamento do serviço.
- **Condições de Corrida (*Race Conditions*):** Identifica acessos concorrentes desprotegidos a variáveis compartilhadas em memória entre múltiplas threads.

### 4.3 Análise de Causa-Raiz (Root Cause Analysis - RCA) e Patches Mínimos
Ao identificar a causa-raiz de um incidente, a boa prática da engenharia de software assistida por IA recomenda a formulação de **Patches Mínimos**:

- O modelo deve propor **alterações cirúrgicas restritas ao estritamente necessário** para neutralizar o defeito;
- Devem-se evitar refatorações cosméticas em massa durante a aplicação de correções críticas (*hotfixes*), minimizando o risco de efeitos colaterais indesejados no ambiente de produção.

---

### Teste 145
**(FGV – TRT-24 – Analista Judiciario Area Apoio Especializado Tecnologia da Informacao – 2025)**
Hibernate 7.0 representa um marco significativo na evolução do Hibernate ORM com foco especial na sua nova especificação para repositórios. O Hibernate Data Repositories é uma implementação baseado no

* **A)** Java EE8.
* **B)** JBoss 3.0.
* **C)** JQuery Data.
* **D)** Jakarta Data.
* **E)** Jakarta API 2.0.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Java EE8". De acordo com a teoria estudada em *1.3 Modernização e Tradução de Sistemas Legados: Riscos Aritméticos*, a migração de sistemas governamentais legados (especialmente rotinas tributárias e de arrecadação em COBOL ou PL/SQL para microsserviços modernos em Java 21, Kotlin ou Python) é uma das aplicações mais estratégicas de IA no setor público.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "JBoss 3.0". De acordo com a teoria estudada em *4.1 Análise de Stack Traces e Decodificação de Erros Críticos*, frameworks corporativos modernos emitem rastreamentos de pilha (*stack traces*) extensos contendo centenas de linhas de chamadas internas da infraestrutura (Spring, Tomcat, Hibernate).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "JQuery Data". De acordo com a teoria estudada em *1.1 Scaffolding, Código Repetitivo (Boilerplate) e CRUDs Estruturais*, foco no Domínio: Ao transferir a codificação mecânica de infraestrutura para a IA, os engenheiros de software concentram-se no núcleo das regras de negócio fiscais, auditoria orçamentária e conformidade jurídica.
> - **D)** **Correta.** Conforme fundamentado na seção *1.1 Scaffolding, Código Repetitivo (Boilerplate) e CRUDs Estruturais* deste guia, redução do Esforço em Boilerplate: Tarefas repetitivas e mecânicas — como a criação de classes de entidade (*JPA/Hibernate*), objetos de transferência de dados (*DTOs*), mapeadores (*Mappers/MapStruct*), repositórios (*Spring Data JPA*) e controladores REST — são geradas em segundos a partir de especificações de esquema relacional (DDL) ou contratos de interface. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT-24/2025) ao estabelecer que "Jakarta Data".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Jakarta API 2.0". De acordo com a teoria estudada em *1.1 Scaffolding, Código Repetitivo (Boilerplate) e CRUDs Estruturais*, anotações de Validação: A IA infere e aplica automaticamente regras de validação padronizadas (`@NotNull`, `@Size`, `@NotBlank`, `@Email`, `@PositiveOrZero`), diminuindo falhas de integridade na camada de borda da API.
>
> **Gabarito: D**

---

### Teste 146
**(FGV – TJ-AP – Analista Judiciario Apoio Especializado Tecnologia da Informacao Desenvolvimento de Sistemas – 2023)**
Analise o código Python a seguir. L=[1,2] while len(L) < 10: L.append(L[-1] + L[-2]) print (L[-1]) O valor exibido na execução desse código é:

* **A)** -1;
* **B)** 1;
* **C)** 2;
* **D)** 89;
* **E)** 144.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "-1". De acordo com a teoria estudada em *3.1 Docstrings, Javadoc e Comentários Semânticos*, python (PEP 257): Docstrings estruturadas explicando o comportamento de funções, tipos de argumentos e invariantes de execução.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "1". De acordo com a teoria estudada em *1.3 Modernização e Tradução de Sistemas Legados: Riscos Aritméticos*, ao traduzir esse código para Java ou Python, modelos de IA frequentemente sugerem tipos primitivos de ponto flutuante binário (`float` ou `double`), por serem mais concisos.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "2". De acordo com a teoria estudada em *1.3 Modernização e Tradução de Sistemas Legados: Riscos Aritméticos*, em código fiscal de órgãos de controle externo, é mandatório o uso de classes de precisão arbitrária exata (`java.math.BigDecimal` em Java ou o módulo `decimal` em Python) com estratégias explícitas de arredondamento (`RoundingMode.HALF_EVEN`).
> - **D)** **Correta.** Conforme fundamentado na seção *4.1 Análise de Stack Traces e Decodificação de Erros Críticos* deste guia, traduz mensagens herméticas para linguagem natural, explicando a condição de contorno que causou a falha (ex.: violação de chave estrangeira por registro órfão ou valor nulo não tratado). Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ-AP/2023) ao estabelecer que "89".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "144". De acordo com a teoria estudada em *4.1 Análise de Stack Traces e Decodificação de Erros Críticos*, frameworks corporativos modernos emitem rastreamentos de pilha (*stack traces*) extensos contendo centenas de linhas de chamadas internas da infraestrutura (Spring, Tomcat, Hibernate).
>
> **Gabarito: D**

---

## 5. Geração Automatizada de Testes de Software

### 5.1 A Grande Armadilha: Testar a Implementação Defeituosa vs. o Comportamento

```mermaid
flowchart TD
    subgraph Armadilha["A Armadilha de Testar Código com Bug"]
        CODE_BUG["Código com Bug de Cálculo:<br/>aliquota = valor * 0.10 (Deveria ser 0.15)"] --> LLM["Agente de IA Gerador de Testes"]
        LLM --> TEST_BUG["Teste Unitário Gerado:<br/>assertEquals(10.0, calcularAliquota(100.0))"]
        TEST_BUG --> CI["Esteira de CI/CD Executa o Teste"]
        CI --> RES["✅ 100% de Sucesso nos Testes!<br/>(Falsa sensação de qualidade: o bug foi mascarado e promovido para produção)"]
    end
```

O risco mais crítico na geração de testes por modelos de IA é o **viés de ancoragem no código implementado**:

- Se o desenvolvedor fornecer um método que contém um bug e solicitar *"gere testes unitários para a função acima"*, a IA inferirá que o código fornecido representa o comportamento correto pretendido!
- Ela formulará asserções (`assert`) que confirmam o valor errado gerado pelo código. O teste passará com sucesso na esteira de CI/CD, conferindo uma falsa sensação de blindagem contra falhas.

> ⭐ **IMPORTANTE / REGRA DE OURO:**  
> Ao solicitar a geração de testes para IA, **forneça sempre a especificação funcional ou regra de negócio independente do código**, ou adote a abordagem TDD (*Test-Driven Development*): gere os testes a partir dos requisitos e somente depois confronte os testes com o código desenvolvido.

### 5.2 Cobertura Sistemática de Casos de Borda (Edge Cases)
Enquanto desenvolvedores humanos frequentemente testam apenas o caminho feliz (*happy path*), modelos de linguagem são excelentes na exploração exaustiva de condições limites:

- **Nulidade e Strings:** Valores `null`, strings vazias (`""`), strings contendo apenas espaços em branco e caracteres especiais de injeção;
- **Limites Numéricos:** Limites extremos de tipos inteiros (`Integer.MAX_VALUE`, `Integer.MIN_VALUE`), números negativos em grandezas financeiras e divisão por zero;
- **Coleções:** Listas vazias, coleções com um único elemento e arrays com volumes massivos de dados;
- **Temporalidade:** Anos bissextos, viradas de século e discrepâncias de fusos horários (UTC vs. horário local).

### 5.3 Geração de Cenários BDD Executáveis (Gherkin)
Modelos de IA sintetizam com facilidade especificações executáveis em conformidade com o padrão BDD:

```gherkin
Funcionalidade: Validação de Prestação de Contas Municipal
  Cenário: Rejeição de despesa sem prévio empenho
    Dado que existe uma despesa protocolada no valor de R$ 45.000,00
    E não consta nota de empenho vinculada no sistema contábil
    Quando o auditor executar a validação de conformidade da despesa
    Então o sistema deve bloquear a liquidação do pagamento
    E emitir o alerta "IRREGULARIDADE_AUSENCIA_DE_EMPENHO_PREVIO"
```

### 5.4 Testes de Mutação (Mutation Testing): Avaliando a Real Eficácia dos Testes
Para auditar a qualidade técnica real de uma suíte de testes gerada por IA, aplica-se o **Teste de Mutação (*Mutation Testing*)** através de ferramentas como o Pitest (PIT) em Java:

```mermaid
flowchart LR
    SUT["Código de Produção sob Teste"] --> MUT["Motor de Mutação (Insere falhas intencionais)"]
    MUT --> M1["Mutante 1: Altera > para >="]
    MUT --> M2["Mutante 2: Inverte Booleano"]
    MUT --> M3["Mutante 3: Remove chamada de método"]
    
    M1 & M2 & M3 --> RUN["Executa Suíte de Testes Gerada por IA"]
    RUN --> R1["Teste Falhou -> Mutante MORTO (Teste Eficaz!)"]
    RUN --> R2["Teste Passou -> Mutante SOBREVIVEU (Teste Ineficaz / Asserção Fraca)"]
```

- **Mecânica dos Mutantes:** O motor de mutação introduz pequenas alterações deliberadas no código compilado (troca operadores relacionais, inverte expressões booleanas, altera valores de retorno).
- **Mutante Morto (*Killed Mutant*):** A suíte de testes detectou a anomalia e falhou. É o resultado esperado para testes robustos.
- **Mutante Sobrevivente (*Survived Mutant*):** O código foi sabotado pelo motor de mutação, mas a suíte de testes continuou passando com sucesso! Isso comprova que a suíte gerada pela IA possui asserções fracas ou testes superficiais que apenas percorrem as linhas sem checar a lógica do negócio.

> 🚨 **ALERTA DE PROVA / PEGADINHA FCC:**  
> A afirmação de que *"uma suíte de testes com 100% de cobertura de código (code coverage) garante que o sistema está livre de erros"* é uma das pegadinhas clássicas mais cobradas pela Fundação Carlos Chagas!  
>
> - **Cobertura de código mede apenas quais linhas foram executadas**, não avaliando se as asserções (`assert`) são corretas ou completas.  
> - É perfeitamente possível ter 100% de cobertura de código com testes que não possuem nenhuma asserção ou com testes que validam valores incorretos. A métrica definitiva de qualidade da suíte é o **Escore de Mutação (*Mutation Score*)**.

---

### Teste 147
**(FGV – TJ-AP – Analista Judiciario Apoio Especializado Tecnologia da Informacao Seguranca da Informacao – 2023)**
A Internet das Coisas, ou IoT (Internet of Things) como muitos conhecem, está dentro do tema casa inteligente, uma vez que faz com que “coisas” possam se comunicar, trocar informações e tomar decisões pré-programadas. Nesse contexto, o protocolo sem fio muito usado em dispositivos de casa inteligente, principalmente pela facilidade de transmitir pequenos pacotes de dados, com baixo consumo de energia e que não depende do Wi-Fi para funcionar, é o:

* **A)** zigbee;
* **B)** gateway;
* **C)** relé smart;
* **D)** 6lowPAN;
* **E)** tuya.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *1.4 Completamento Inteligente de Código: Ghost Text e AST Local* deste guia, contexto da AST (Abstract Syntax Tree): O assistente inspeciona a árvore sintática do arquivo em edição, classes importadas, tipos retornados por métodos e abas adjacentes recentemente abertas, assegurando coerência tipográfica e semântica com o restante da solução. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ-AP/2023) ao estabelecer que "zigbee".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "gateway". De acordo com a teoria estudada em *5.3 Geração de Cenários BDD Executáveis (Gherkin)*, modelos de IA sintetizam com facilidade especificações executáveis em conformidade com o padrão BDD.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "relé smart". De acordo com a teoria estudada em *5.2 Cobertura Sistemática de Casos de Borda (Edge Cases)*, coleções: Listas vazias, coleções com um único elemento e arrays com volumes massivos de dados.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "6lowPAN". De acordo com a teoria estudada em *1.2 Síntese de Algoritmos Complexos e Regras de Negócio*, pré-requisito Vital: A qualidade e corretude do algoritmo gerado dependem estritamente da clareza com que o desenvolvedor estabelece as pré-condições, pós-condições e invariantes lógicas na especificação enviada.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "tuya". De acordo com a teoria estudada em *3.3 Diagramação Arquitetural Declarativa com Mermaid.js e PlantUML*, em vez de diagramas estáticos desenhados em ferramentas gráficas externas (que ficam rapidamente desatualizados), o agente de IA sintetiza diagramas baseados em texto dentro da própria documentação Markdown.
>
> **Gabarito: A**

---

### Teste 148
**(IBFC – TJ-MG – Analista Judiciario Classe C Analista de Tecnologia da Informacao – 2022)**
Leia atentamente a frase abaixo: "O ______ é uma camada que descreve uma interface comum para frameworks ______ como o ______". Assinale a alternativa que preencha correta e respectivamente as lacunas.

* **A)** JVM / ORM / Hibernate
* **B)** JPA / ORM / Hibernate
* **C)** JVM / ORM / OpenJDK
* **D)** JPA / DBA / OpenJDK
* **E)** JPA / DBA / Hibernate

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "JVM / ORM / Hibernate". De acordo com a teoria estudada em *4.1 Análise de Stack Traces e Decodificação de Erros Críticos*, frameworks corporativos modernos emitem rastreamentos de pilha (*stack traces*) extensos contendo centenas de linhas de chamadas internas da infraestrutura (Spring, Tomcat, Hibernate).
> - **B)** **Correta.** Conforme fundamentado na seção *1.1 Scaffolding, Código Repetitivo (Boilerplate) e CRUDs Estruturais* deste guia, redução do Esforço em Boilerplate: Tarefas repetitivas e mecânicas — como a criação de classes de entidade (*JPA/Hibernate*), objetos de transferência de dados (*DTOs*), mapeadores (*Mappers/MapStruct*), repositórios (*Spring Data JPA*) e controladores REST — são geradas em segundos a partir de especificações de esquema relacional (DDL) ou contratos de interface. Dessa forma, está plenamente correta a assertiva da banca (IBFC – TJ-MG/2022) ao estabelecer que "JPA / ORM / Hibernate".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "JVM / ORM / OpenJDK". De acordo com a teoria estudada em *1.1 Scaffolding, Código Repetitivo (Boilerplate) e CRUDs Estruturais*, anotações de Validação: A IA infere e aplica automaticamente regras de validação padronizadas (`@NotNull`, `@Size`, `@NotBlank`, `@Email`, `@PositiveOrZero`), diminuindo falhas de integridade na camada de borda da API.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "JPA / DBA / OpenJDK". De acordo com a teoria estudada em *2.1 Linters Estáticos Tradicionais (AST/SAST) vs. Agentes de AI Code Review*, papel na Governança: Base obrigatória e inegociável de conformidade de estilo, cobertura e padrões de código. — Camada inteligente de triagem, síntese de alterações e detecção de falhas lógicas sutis para apoiar a revisão humana.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "JPA / DBA / Hibernate". De acordo com a teoria estudada em *5.2 Cobertura Sistemática de Casos de Borda (Edge Cases)*, enquanto desenvolvedores humanos frequentemente testam apenas o caminho feliz (*happy path*), modelos de linguagem são excelentes na exploração exaustiva de condições limites.
>
> **Gabarito: B**

---

### Teste 149
**(IBFC – TJ-MG – Analista Judiciario Classe C Analista de Tecnologia da Informacao – 2022)**
Quanto à arquitetura distribuída de microsserviços temos o Spring Framework. Dentro desse ecossistema temos o Spring Boot que possui os seguintes componentes-base: (1) Spring Boot Actuator. (2) Spring Boot Finisher. (3) Spring Boot AutoConfigurator. (4) Spring Boot Starter. Da relação apresentada:

* **A)** somente são aplicados o 1, 2 e 3
* **B)** somente são aplicados o 1, 2 e 4
* **C)** somente são aplicados o 2, 3 e 4
* **D)** somente são aplicados o 1, 3 e 4
* **E)** todos podem ser aplicados

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "somente são aplicados o 1, 2 e 3". De acordo com a teoria estudada em *2.1 Linters Estáticos Tradicionais (AST/SAST) vs. Agentes de AI Code Review*, papel na Governança: Base obrigatória e inegociável de conformidade de estilo, cobertura e padrões de código. — Camada inteligente de triagem, síntese de alterações e detecção de falhas lógicas sutis para apoiar a revisão humana.
> - **B)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "somente são aplicados o 1, 2 e 4". De acordo com a teoria estudada em *2.2 Identificação de Code Smells, Débito Técnico e Violações de SOLID*, código Duplicado e Obsolescência: Identificação de reimplementações de funções utilitárias que já existem no ecossistema da biblioteca padrão.
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "somente são aplicados o 2, 3 e 4". De acordo com a teoria estudada em *3.3 Diagramação Arquitetural Declarativa com Mermaid.js e PlantUML*, em vez de diagramas estáticos desenhados em ferramentas gráficas externas (que ficam rapidamente desatualizados), o agente de IA sintetiza diagramas baseados em texto dentro da própria documentação Markdown.
> - **D)** **Correta.** Conforme fundamentado na seção *5.4 Testes de Mutação (Mutation Testing): Avaliando a Real Eficácia dos Testes* deste guia, mutante Sobrevivente (*Survived Mutant*): O código foi sabotado pelo motor de mutação, mas a suíte de testes continuou passando com sucesso! Isso comprova que a suíte gerada pela IA possui asserções fracas ou testes superficiais que apenas percorrem as linhas sem checar a lógica do negócio. Dessa forma, está plenamente correta a assertiva da banca (IBFC – TJ-MG/2022) ao estabelecer que "somente são aplicados o 1, 3 e 4".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "todos podem ser aplicados". De acordo com a teoria estudada em *1.1 Scaffolding, Código Repetitivo (Boilerplate) e CRUDs Estruturais*, redução do Esforço em Boilerplate: Tarefas repetitivas e mecânicas — como a criação de classes de entidade (*JPA/Hibernate*), objetos de transferência de dados (*DTOs*), mapeadores (*Mappers/MapStruct*), repositórios (*Spring Data JPA*) e controladores REST — são geradas em segundos a partir de especificações de esquema relacional (DDL) ou contratos de interface.
>
> **Gabarito: D**

---

## 6. Fontes Recomendadas na Internet

* [ArXiv - Evaluating Large Language Models Trained on Code / Codex & Pass@k (Chen et al.)](https://arxiv.org/abs/2107.03374) - Criação do benchmark HumanEval, definição formal da métrica pass@k e síntese funcional de código.
* [ArXiv - SWE-bench: Can Language Models Resolve Real-World GitHub Issues? (Jimenez et al.)](https://arxiv.org/abs/2310.06770) - Avaliação automatizada de agentes de software resolvendo bugs em repositórios reais.
* [Anthropic Documentation - Code Generation and Test Synthesis](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) - Melhores práticas para síntese de testes unitários, testes de mutação e análise de cobertura assistida.
* [Martin Fowler - Self-Testing Code and Continuous Delivery](https://martinfowler.com/bliki/SelfTestingCode.html) - Princípios fundamentais de código auto-testável e automação de testes em engenharia.
* SOMMERVILLE, Ian. **Engenharia de Software**. 10. ed. São Paulo: Pearson, 2019. (Cap. 8 - Teste de Software e Automação).
* PRESSMAN, Roger S.; MAXIM, Bruce R. **Engenharia de Software: Uma Abordagem Profissional**. 9. ed. Porto Alegre: AMGH, 2021. (Cap. 20 - Estratégias de Teste de Software).
* BECK, Kent. **Desenvolvimento Guiado por Testes (TDD)**. Porto Alegre: Bookman, 2010. (Cap. 1 a 3 - Ciclo Red-Green-Refactor).
