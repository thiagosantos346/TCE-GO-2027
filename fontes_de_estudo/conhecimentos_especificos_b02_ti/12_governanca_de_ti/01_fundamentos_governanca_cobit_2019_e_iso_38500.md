# 01 - Fundamentos de Governança, COBIT 2019 e ISO/IEC 38500:2024

> **Matéria:** Governança de Tecnologia da Informação  
> **Cargo:** B02 – Técnico de Controle Externo – Especialidade: Tecnologia da Informação  
> **Arquivo:** `01_fundamentos_governanca_cobit_2019_e_iso_38500.md`  



---


## 📌 Ementa / Itens do Edital
- Governança de TI vs. Gestão de TI: conceitos e alinhamento estratégico institucional
- Norma ABNT NBR ISO/IEC 38500:2024 (Governança Corporativa de Tecnologia da Informação)
- Framework COBIT 2019 (ISACA):
    - Princípios de Governança e do Framework
    - Componentes do Sistema de Governança e Fatores de Design (Design Factors)
    - Áreas de Foco (Focus Areas) e Cascatamento de Objetivos (Goals Cascade)
    - Os 40 Objetivos de Governança e Gestão (5 Domínios: EDM, APO, BAI, DSS, MEA)
    - Gestão de Desempenho do COBIT (CPM) e Níveis de Capacidade CMMI

---

## 🧭 Sumário

1. [Fundamentos da Governança de TI e Alinhamento Estratégico](#1-fundamentos-da-governanca-de-ti-e-alinhamento-estrategico)
1. [Distinção Essencial entre Governança e Gestão](#1-1-distincao-essencial-entre-governanca-e-gestao)
1. [Alinhamento Estratégico e Criação de Valor Público](#1-2-alinhamento-estrategico-e-criacao-de-valor-publico)
    1. [Teste 465](#Teste-465)
2. [Norma ABNT NBR ISO/IEC 38500:2024](#2-norma-abnt-nbr-isoiec-385002024)
2. [Escopo e Modelo de Governança (Ciclo EDM)](#2-1-escopo-e-modelo-de-governanca-ciclo-edm)
    1. [Teste 466](#Teste-466)
2. [Os Seis Princípios da Boa Governança de TI](#2-2-os-seis-principios-da-boa-governanca-de-ti)
    1. [Teste 467](#Teste-467)
3. [Framework COBIT 2019 (ISACA)](#3-framework-cobit-2019-isaca)
3. [Princípios do Sistema e do Framework de Governança](#3-1-principios-do-sistema-e-do-framework-de-governanca)
    1. [Teste 468](#Teste-468)
3. [Componentes do Sistema de Governança (7 Componentes)](#3-2-componentes-do-sistema-de-governanca-7-componentes)
    1. [Teste 469](#Teste-469)
3. [Fatores de Design (11 Design Factors) e Áreas de Foco (Focus Areas)](#3-3-fatores-de-design-11-design-factors-e-areas-de-foco-focus-areas)
    1. [Teste 470](#Teste-470)
3. [Cascatamento de Objetivos (Goals Cascade)](#3-4-cascatamento-de-objetivos-goals-cascade)
    1. [Teste 471](#Teste-471)
3. [Os 40 Objetivos de Governança e Gestão nos 5 Domínios](#3-5-os-40-objetivos-de-governanca-e-gestao-nos-5-dominios)
    1. [Teste 472](#Teste-472)
3. [Gestão de Desempenho do COBIT (CPM) e Níveis de Capacidade CMMI](#3-6-gestao-de-desempenho-do-cobit-cpm-e-niveis-de-capacidade-cmmi)
    1. [Teste 473](#Teste-473)
    2. [Teste 474](#Teste-474)
6. [Fontes Recomendadas na Internet](#6-fontes-recomendadas-na-internet)

---

## 1. Fundamentos da Governança de TI e Alinhamento Estratégico

---

## 1.1 Distinção Essencial entre Governança e Gestão

A separação entre **Governança** e **Gestão** é o pilar estruturante de maior incidência em provas da Fundação Carlos Chagas (FCC) na disciplina de Governança de TI. Trata-se de responsabilidades, papéis e ciclos operacionais completamente distintos, embora fortemente integrados.

```mermaid
flowchart TD
    subgraph GOVERNANCA["GOVERNANÇA (Conselho / Alta Administração / Plenário do Tribunal)"]
        direction TB
        E["Avaliar (Evaluate)<br/>Necessidades, Condições e Opções"] --> D["Dirigir (Direct)<br/>Prioridades, Diretrizes e Políticas"]
        D --> M["Monitorar (Monitor)<br/>Desempenho, Conformidade e Riscos"]
        M --> E
    end

    subgraph GESTAO["GESTÃO (Diretoria Executiva / DTI / Gerência Operacional)"]
        direction LR
        P["Plan (Planejar)<br/>APO"] --> B["Build (Construir)<br/>BAI"]
        B --> R["Run (Executar)<br/>DSS"]
        R --> Mon["Monitor (Monitorar)<br/>MEA"]
        Mon --> P
    end

    D -- "Diretrizes, Políticas e Metas" --> P
    Mon -- "Relatórios de Desempenho e Evidências" --> M
```

#### Tabela Comparativa: Governança de TI versus Gestão de TI

| Dimensão de Análise | Governança de TI (*Governance*) | Gestão de TI (*Management*) |
| :--- | :--- | :--- |
| **Papel Primário** | Direcionamento estratégico, supervisão, liderança institucional e prestação de contas (*Accountability*). | Execução técnica, coordenação operacional, manutenção de rotinas e entrega diária de serviços. |
| **Responsável Típico** | Alta Administração, Conselho de Administração, Plenário e Comitês Estratégicos de Governança. | Diretoria Executiva de TI (CIO/DTI), gerentes de projetos, equipes de desenvolvimento e suporte. |
| **Atividades Centrais** | **EDM**: Avaliar (*Evaluate*), Dirigir (*Direct*) e Monitorar (*Monitor*). | **PBRM**: Planejar (*Plan*), Construir (*Build*), Executar (*Run*) e Monitorar (*Monitor*). |
| **Horizonte Temporal** | Longo prazo (visão plurianual, sustentabilidade e impacto institucional). | Curto e médio prazo (sprints de desenvolvimento, chamados operacionais, metas contratuais imediatas). |
| **Objetivo Maior** | **Criação de Valor**: Realização de benefícios com balanceamento e otimização de riscos e recursos. | Eficiência técnica, cumprimento estrito de SLAs, produtividade e estabilidade dos sistemas em produção. |
| **Ponto de Partida** | Necessidades das partes interessadas (*stakeholders*: cidadãos, magistrados, auditores, jurisdicionados). | Diretrizes, limites orçamentários, apetite a risco e prioridades deliberadas pela governança. |

> 🚨 **ALERTA DE PROVA / PEGADINHA FCC:**  
> A banca frequentemente tenta confundir o candidato atribuindo à Governança tarefas de execução (como configurar roteadores, gerenciar chamados de help desk ou planejar sprints). Lembre-se: a governança **define o que fazer e em qual direção ir**, avaliando, dirigindo e monitorando. A gestão cuida do **como fazer**, planejando, construindo, executando e monitorando o trabalho diário.

---

---

## 1.2 Alinhamento Estratégico e Criação de Valor Público

No setor público, e em especial nos órgãos de controle externo como o TCE-GO, o alinhamento estratégico da Tecnologia da Informação não tem como meta o lucro, mas sim a **criação de valor público**. Isso significa garantir que os recursos aplicados em tecnologia resultem em fiscalizações mais ágeis, auditorias digitais baseadas em cruzamento massivo de dados, transparência ativa ao cidadão e prestação jurisdicional de excelência.

O alinhamento estratégico é teorizado pelo clássico **Modelo de Alinhamento Estratégico (SAM - *Strategic Alignment Model*) de Henderson & Venkatraman**, que articula quatro domínios fundamentais:

1. **Estratégia do Negócio:** Escopo corporativo, competências distintivas e governança corporativa.
2. **Estratégia de TI:** Escopo de tecnologia, competências sistêmicas e governança de TI.
3. **Infraestrutura e Processos Organizacionais:** Estrutura administrativa, processos de trabalho corporativos e habilidades dos servidores.
4. **Infraestrutura e Processos de TI:** Arquitetura tecnológica, processos operacionais de TI e habilidades da equipe técnica.

A governança assegura a integração bidirecional contínua entre a estratégia institucional e a estratégia de TI, evitando que a área técnica formule objetivos isolados ou desconectados das reais prioridades de fiscalização e auditoria do Tribunal.

---

### Teste 465
**(FGV - TJ-MT - Analista Judiciário - Tecnologia da Informação - Adaptada)**
**Enunciado:** A governança de TI é fundamental para alinhar os recursos e investimentos de tecnologia aos objetivos estratégicos organizacionais, assegurando a geração de valor público e a mitigação de riscos. A respeito das diferenças estruturais e operacionais entre governança e gestão de tecnologia da informação, assinale a alternativa correta:  

* **A)** A governança de TI concentra-se precipuamente na execução de atividades operacionais rotineiras, como configuração de switches de rede, homologação de código e atendimento diário de chamados de suporte de primeiro nível.
* **B)** A governança de TI é responsável por avaliar as necessidades estratégicas, direcionar as prioridades institucionais por meio de políticas e monitorar o desempenho e a conformidade, cabendo à gestão planejar, construir, executar e monitorar as atividades técnicas em consonância com as diretrizes estabelecidas.
* **C)** A gestão de TI possui horizonte temporal plurianual e é exercida com exclusividade pelos membros do Plenário e da alta administração, não se subordinando às diretrizes dos comitês estratégicos institucionais.
* **D)** A governança e a gestão de tecnologia constituem funções idênticas e intercambiáveis, de modo que os frameworks internacionais (como COBIT 2019 e ISO/IEC 38500) não estabelecem segregação de papéis ou responsabilidades entre os dois domínios.
* **E)** A responsabilidade final pela governança corporativa de TI deve ser compulsoriamente transferida e delegada às empresas contratadas que fornecem infraestrutura de data center ou sustentação de sistemas.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Configuração de ativos, codificação e atendimento de chamados operacionais de suporte são atribuições típicas de gestão de serviços de TI (nível operacional/tático), e não de governança.
> - **B)** **Correta.** A governança define o direcionamento estratégico segundo o modelo EDM (Avaliar, Dirigir e Monitorar), enquanto a gestão implementa e executa planos diários segundo o ciclo PBRM (Planejar, Construir, Executar e Monitorar).
> - **C)** Incorreta. A gestão foca no curto e médio prazo (sprints, rotinas operacionais). Quem possui visão de longo prazo e é exercida pela alta administração é a governança corporativa.
> - **D)** Incorreta. Há estrita segregação de funções (*separation of duties*). COBIT 2019 e ISO/IEC 38500 enfatizam que governança e gestão possuem propósitos, estruturas, responsabilidades e horizontes temporais distintos.
> - **E)** Incorreta. Pelo princípio da Responsabilidade, a prestação de contas (*accountability*) da governança é indelegável e não pode ser transferida para fornecedores ou prestadores externos.
> 
> **Gabarito: B**

---

## 2. Norma ABNT NBR ISO/IEC 38500:2024

---

## 2.1 Escopo e Modelo de Governança (Ciclo EDM)

A norma **ABNT NBR ISO/IEC 38500:2024** fornece princípios e diretrizes para os órgãos deliberativos e membros da alta administração das organizações (públicas ou privadas, de qualquer porte ou setor) sobre a utilização aceitável, eficaz e eficiente da TI.

A governança atua segundo o modelo cíclico **EDM**:

- **Avaliar (*Evaluate*):** Examinar continuamente as circunstâncias presentes e futuras, considerando demandas dos stakeholders, tendências tecnológicas, requisitos legais e restrições financeiras.
- **Dirigir (*Direct*):** Atribuir responsabilidades e orientar a preparação e execução de estratégias, planos de TI e políticas institucionais.
- **Monitorar (*Monitor*):** Acompanhar periodicamente se a gestão está operando em conformidade com as diretrizes e se os objetivos de desempenho planejados estão sendo atingidos.

```mermaid
sequenceDiagram
    autonumber
    participant SH as Partes Interessadas (Cidadãos / Sociedade)
    participant GOV as Órgão de Governança (Alta Administração)
    participant MGT as Gestão da TI (DTI / Gestão Operacional)

    SH->>GOV: Demandas, expectativas e mandatos legais
    GOV->>GOV: Avaliar (Evaluate) necessidades, riscos e opções
    GOV->>MGT: Dirigir (Direct): Políticas, limites e planos estratégicos
    MGT->>MGT: Executar planos, operar sistemas e tratar incidentes
    MGT-->>GOV: Reportar dados de desempenho e relatórios de conformidade
    GOV->>GOV: Monitorar (Monitor) indicadores e conformidade
    GOV-->>SH: Prestação de contas e geração de valor público
```

---

### Teste 466
**(FCC - Tribunal de Contas - Auditor de TI - Adaptada)**
**Enunciado:** A norma ABNT NBR ISO/IEC 38500:2024 define que a governança de Tecnologia da Informação pela alta administração é exercida por meio de um ciclo contínuo de três tarefas fundamentais (modelo EDM). Acerca desse modelo e dos papéis desempenhados pelo órgão de governança, assinale a alternativa correta:  

* **A)** Na tarefa de Dirigir (*Direct*), o órgão de governança assume diretamente a programação de scripts e o deploy contínuo de aplicações em ambientes de produção.
* **B)** Na tarefa de Avaliar (*Evaluate*), o órgão de governança examina e julga o uso presente e futuro da TI, considerando as estratégias institucionais, propostas de projetos e demandas das partes interessadas (*stakeholders*).
* **C)** O modelo EDM determina que a tarefa de Monitorar (*Monitor*) é dispensável caso a organização possua certificação ISO 9001 e auditoria interna constituída.
* **D)** A governança corporativa de TI conforme a ISO/IEC 38500 limita-se a organizações privadas com fins lucrativos, sendo vedada sua aplicação em tribunais de contas ou autarquias públicas.
* **E)** A tarefa de Dirigir (*Direct*) consiste exclusivamente na realização de auditorias fiscais pós-fato, sem competência para emitir políticas ou planos de investimento.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O papel de *Direct* consiste em definir políticas institucionais, prioridades e direcionamentos estratégicos, jamais na programação direta ou intervenção operacional diária de TI.
> - **B)** **Correta.** A avaliação (*Evaluate*) examina continuamente as circunstâncias presentes e futuras, considerando demandas dos stakeholders, tendências tecnológicas, requisitos legais e restrições financeiras.
> - **C)** Incorreta. O monitoramento contínuo de conformidade e desempenho é tarefa indispensável e mandatória da governança.
> - **D)** Incorreta. A norma ABNT NBR ISO/IEC 38500 aplica-se universalmente a qualquer organização pública ou privada, independente de porte ou finalidade lucrativa.
> - **E)** Incorreta. Dirigir é atribuir responsabilidades, definir estratégias e planos de TI de forma proativa.
> 
> **Gabarito: B**

---

## 2.2 Os Seis Princípios da Boa Governança de TI

A ISO/IEC 38500 prescreve **seis princípios** fundamentais que orientam a tomada de decisão da alta administração:

| Nº | Princípio | Significado / Exigência Normativa | Foco de Cobrança FCC |
| :---: | :--- | :--- | :--- |
| **1** | **Responsabilidade** (*Responsibility*) | Indivíduos e comitês compreendem e aceitam suas responsabilidades relativas à oferta e demanda de TI. Autoridade delegada deve ser proporcional à responsabilidade. | Não pode haver ambiguidade de papéis; a responsabilidade de governança jamais pode ser transferida ou terceirizada a fornecedores externos. |
| **2** | **Estratégia** (*Strategy*) | A estratégia de TI deve estar perfeitamente alinhada e suportar as necessidades atuais e as aspirações futuras da estratégia corporativa. | TI não cria estratégia isolada; a TI viabiliza os objetivos institucionais e o plano de diretrizes do órgão. |
| **3** | **Aquisição** (*Acquisition*) | As aquisições de TI são feitas por razões válidas, com base em análise apropriada e contínua do Custo Total de Propriedade (TCO) e retorno esperado. | Veda compras impulsivas ou sem Estudo Técnico Preliminar (ETP) fundamentado. Exige análise de ciclo de vida completo. |
| **4** | **Desempenho** (*Performance*) | A TI atende às necessidades da organização, entregando serviços com os níveis de serviço e capacidade exigidos pelo negócio. | Monitoramento contínuo de disponibilidade, tempo de resposta e eficácia dos sistemas em produção. |
| **5** | **Conformidade** (*Conformance*) | A TI opera em estrita conformidade com toda a legislação, regulações e políticas internas aplicáveis (LGPD, Marco Civil, Lei 14.133/2021). | As práticas de governança devem assegurar aderência legal e auditoria formal periódica. |
| **6** | **Comportamento Humano** (*Human Behaviour*) | As políticas, práticas e decisões de TI respeitam os fatores humanos, culturais e as necessidades de todas as pessoas envolvidas. | Treinamento, usabilidade, ergonomia, acessibilidade e gestão de mudanças comportamentais no trabalho. |

> 🚨 **ALERTA DE PROVA / PEGADINHA FCC:**  
> A FCC adora cobrar a lista exata dos 6 princípios da ISO/IEC 38500 trocando palavras como "Comportamento Humano" por "Comportamento Financeiro", "Econômico" ou inventando termos como "Agilidade" e "Virtualização". Grave o mnemônico: **R-E-A-D-C-H** (*Responsibility, Strategy, Acquisition, Performance, Conformance, Human Behaviour*).

---

### Teste 467
**(FCC - Analista de TI / Governança - Adaptada)**
**Enunciado:** A norma ABNT NBR ISO/IEC 38500 fornece diretrizes para que dirigentes e órgãos de governança assegurem o uso eficaz, eficiente e aceitável da Tecnologia da Informação. Acerca dos princípios e do modelo de atuação prescritos por essa norma, assinale a alternativa correta:  

* **A)** O modelo da ISO/IEC 38500 estabelece que a atuação do órgão de governança ocorre por meio de três tarefas fundamentais: Avaliar (*Evaluate*), Dirigir (*Direct*) e Monitorar (*Monitor*).
* **B)** O princípio do Comportamento Humano exige que todos os colaboradores assinem termos de confidencialidade com renúncia a direitos trabalhistas antes de utilizar sistemas corporativos.
* **C)** O princípio da Aquisição determina que a organização deve sempre optar pela solução de menor preço nominal de compra imediata, sendo vedado o cômputo de custos futuros de manutenção e suporte.
* **D)** As diretrizes da norma ISO/IEC 38500 aplicam-se exclusivamente a instituições financeiras privadas e empresas de tecnologia listadas em bolsa de valores, sendo expressamente vedada sua aplicação a órgãos públicos.
* **E)** A responsabilidade pela prestação de contas do uso de TI na organização deve ser transferida compulsoriamente aos fornecedores externos e prestadores de suporte técnico terceirizados.


---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** A ISO/IEC 38500 estrutura a governança corporativa de TI em torno do ciclo EDM: Avaliar o uso atual e futuro da TI, Dirigir a preparação e implementação de planos e políticas, e Monitorar o cumprimento das políticas e o desempenho alcançado.
> - **B)** Incorreta. O princípio do Comportamento Humano estabelece que as políticas, práticas e decisões de TI devem respeitar os comportamentos humanos, as necessidades culturais e o bem-estar dos colaboradores e usuários, incluindo treinamento, usabilidade e transição adequada de rotinas.
> - **C)** Incorreta. O princípio da Aquisição exige justamente o oposto: os investimentos em TI devem ser fundamentados em análises criteriosas de custo-benefício de longo prazo, considerando o Custo Total de Propriedade (TCO) e riscos, e não apenas o custo de aquisição imediata.
> - **D)** Incorreta. A norma aplica-se a qualquer organização, pública ou privada, governamental ou não-governamental, independente de seu porte ou natureza jurídica.
> - **E)** Incorreta. Conforme o princípio da Responsabilidade, a governança e a *accountability* sobre as decisões de TI recaem sobre os dirigentes e a administração da própria organização; a responsabilidade final nunca pode ser terceirizada a prestadores de serviços externos.
> 
> **Gabarito: A**

---

## 3. Framework COBIT 2019 (ISACA)

O **COBIT 2019** (*Control Objectives for Information and Related Technologies*) é o framework líder mundial de governança e gestão corporativa de informação e tecnologia (I&T), publicado pela ISACA. O COBIT não é prescritivo em nível de codificação ou configuração de servidores; ele funciona como um **framework guarda-chuva** integrador, alinhando padrões técnicos (como ITIL, PMBOK, TOGAF e ISO 27001) às metas institucionais.

---

## 3.1 Princípios do Sistema e do Framework de Governança

Uma das maiores inovações do COBIT 2019 foi dividir formalmente os princípios em duas categorias:

1. **6 Princípios para o Sistema de Governança** (*Governance System Principles*).
2. **3 Princípios para o Framework de Governança** (*Governance Framework Principles*).

```mermaid
flowchart LR
    subgraph SISTEMA["6 Princípios do SISTEMA de Governança"]
        S1["1. Prover Valor aos Stakeholders"]
        S2["2. Abordagem Holística"]
        S3["3. Sistema Dinâmico"]
        S4["4. Governança Distinta da Gestão"]
        S5["5. Adaptado às Necessidades Corporativas"]
        S6["6. Sistema Ponta a Ponta"]
    end

    subgraph FRAMEWORK["3 Princípios do FRAMEWORK de Governança"]
        F1["1. Baseado em Modelo Conceitual"]
        F2["2. Aberto e Flexível"]
        F3["3. Alinhado aos Principais Padrões"]
    end
```

#### Tabela Comparativa dos Princípios do COBIT 2019

| Princípios do **Sistema** de Governança (6) | Princípios do **Framework** de Governança (3) |
| :--- | :--- |
| **1. Prover valor aos stakeholders:** O sistema deve gerar valor a partir do uso de I&T balanceando benefícios, riscos e uso otimizado de recursos. | **1. Baseado em um modelo conceitual:** Deve identificar os principais componentes e relacionamentos para garantir consistência e automação. |
| **2. Abordagem holística:** O sistema é construído a partir de múltiplos tipos de componentes integrados entre si. | **2. Aberto e flexível:** Deve permitir a inclusão de novos conteúdos e tecnologias emergentes sem desestruturar o núcleo original. |
| **3. Sistema dinâmico:** Sempre que um ou mais fatores de design mudarem, o impacto sobre o sistema de governança deve ser reavaliado. | **3. Alinhado aos principais padrões:** Deve harmonizar-se com os padrões de referência (ISO, ITIL, TOGAF, PMBOK, NIST). |
| **4. Governança distinta da gestão:** O sistema mantém clara separação estrutural e conceitual entre governança e gestão. | — |
| **5. Adaptado às necessidades corporativas:** Deve ser customizado conforme o contexto organizacional por meio de fatores de design (*tailoring*). | — |
| **6. Sistema ponta a ponta:** Cobre todas as informações e tecnologias de toda a organização, e não apenas o departamento de TI. | — |

> 🚨 **ALERTA DE PROVA / PEGADINHA FCC:**  
> A banca FCC frequentemente afirma em enunciados que "Baseado em Modelo Conceitual" ou "Aberto e Flexível" são princípios do *Sistema de Governança*. **Errado!** Esses são princípios do **Framework de Governança**. Da mesma forma, "Sistema Dinâmico" e "Abordagem Holística" pertencem ao **Sistema**, e não ao framework!

---

### Teste 468
**(FCC - Analista de Controle Externo / Auditoria de TI - Adaptada)**
**Enunciado:** O framework COBIT 2019 estruturou seus fundamentos separando os princípios aplicáveis ao "Sistema de Governança" dos princípios aplicáveis ao "Framework de Governança". A respeito dessa classificação e dos componentes de governança do COBIT 2019, assinale a afirmativa correta:  

* **A)** "Baseado em um modelo conceitual", "Aberto e flexível" e "Alinhado aos principais padrões" constituem os 3 princípios do Framework de Governança.
* **B)** O princípio de "Prover valor aos stakeholders" pertence com exclusividade ao Framework de Governança, não tendo qualquer relação com o Sistema de Governança.
* **C)** O COBIT 2019 extinguiu os componentes organizacionais, considerando que processos de software são os únicos elementos necessários para garantir uma governança robusta.
* **D)** O princípio do "Sistema dinâmico" postula que o sistema de governança, uma vez implementado no órgão público, deve permanecer estático e imutável por no mínimo dez anos.
* **E)** A separação conceitual entre governança e gestão foi descontinuada na versão 2019, passando ambos a serem regidos pelo mesmo princípio unificado de desenvolvimento ágil.


---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** O COBIT 2019 estabelece exatamente 3 princípios para o Framework de Governança: 1. Baseado em um modelo conceitual; 2. Aberto e flexível; 3. Alinhado aos principais padrões e normas mundiais (ISO, ITIL, TOGAF, etc.).
> - **B)** Incorreta. "Prover valor aos stakeholders" é o primeiro e mais importante princípio do Sistema de Governança (e não do framework).
> - **C)** Incorreta. O COBIT 2019 define 7 componentes holísticos (Processos; Estruturas Organizacionais; Princípios, Políticas e Estruturas; Informação; Cultura, Ética e Comportamento; Pessoas, Habilidades e Competências; Serviços, Infraestrutura e Aplicações). Ele rejeita a visão míope de focar apenas em processos.
> - **D)** Incorreta. O princípio do "Sistema dinâmico" afirma exatamente o contrário: sempre que um ou mais fatores de design mudarem (ex.: nova legislação, alteração de diretoria, mudança tecnológica), o impacto sobre a governança de TI deve ser reavaliado dinamicamente.
> - **E)** Incorreta. A governança distinta da gestão é mantida explicitamente como o Princípio 4 do Sistema de Governança no COBIT 2019.
> 
> **Gabarito: A**

---

## 3.2 Componentes do Sistema de Governança (7 Componentes)

Para construir, operar e manter um sistema de governança funcional, o COBIT 2019 define **7 categorias de Componentes** (denominados "Habilitadores" no antigo COBIT 5):

1. **Processos:** Conjuntos estruturados de práticas e atividades concebidos para atingir determinados objetivos e produzir saídas úteis.
2. **Estruturas Organizacionais:** Entidades e comitês formais responsáveis pela tomada de decisão (Comitê de Governança Digital, Plenário, DTI).
3. **Princípios, Políticas e Estruturas:** Instrumentos normativos que traduzem comportamentos e diretrizes desejadas em orientações práticas cotidianas.
4. **Informação:** Dados e fluxos informacionais consumidos e produzidos pela organização (relevância, segurança, precisão, completude).
5. **Cultura, Ética e Comportamento:** Posturas éticas, hábitos e traços culturais dos servidores e da liderança corporativa.
6. **Pessoas, Habilidades e Competências:** Capital humano, competências técnicas e conhecimentos requeridos para a execução das práticas.
7. **Serviços, Infraestrutura e Aplicações:** A infraestrutura tecnológica, redes, data centers, ferramentas de software e aplicações corporativas.

---

### Teste 469
**(FGV - TRT-13 - Analista Judiciário - TI - Adaptada)**
**Enunciado:** O COBIT 2019 estabelece que um sistema de governança requer fatores e recursos de diferentes naturezas trabalhando em conjunto, estruturados em 7 categorias de Componentes. A respeito desses componentes, assinale a alternativa correta:  

* **A)** O componente 'Processos' é o único obrigatório no COBIT 2019, sendo os demais 6 componentes considerados elementos puramente cosméticos e facultativos pela ISACA.
* **B)** As 'Estruturas Organizacionais' correspondem às entidades e comitês formais tomadores de decisão na organização, constituindo um dos 7 componentes do sistema de governança.
* **C)** O COBIT 2019 extinguiu o componente 'Pessoas, Habilidades e Competências', preconizando a automatização irrestrita de todas as práticas por inteligência artificial autônoma.
* **D)** O componente 'Cultura, Ética e Comportamento' aplica-se apenas a empresas privadas de capital aberto, não tendo relevância em órgãos públicos de controle externo.
* **E)** As ferramentas de software corporativo e data centers integram o componente de 'Estruturas Organizacionais' e não de 'Serviços, Infraestrutura e Aplicações'.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Todos os 7 componentes são essenciais e interdependentes para sustentar a eficácia do sistema de governança.
> - **B)** **Correta.** Estruturas organizacionais são os órgãos decisórios da governança e gestão (como o Plenário, comitês executivos de TI e a diretoria de tecnologia).
> - **C)** Incorreta. O capital humano (*People, Skills and Competencies*) continua sendo componente central do framework.
> - **D)** Incorreta. Cultura e ética corporativa são fundamentais em qualquer organização, sobretudo em tribunais de controle público.
> - **E)** Incorreta. Softwares e data centers integram a categoria 'Serviços, Infraestrutura e Aplicações'.
> 
> **Gabarito: B**

---

## 3.3 Fatores de Design (11 Design Factors) e Áreas de Foco (Focus Areas)

#### Os 11 Fatores de Design (*Design Factors*)
O COBIT 2019 não adota o modelo "tamanho único" (*one size fits all*). Para viabilizar a adaptação (*tailoring*) do sistema de governança à realidade de cada órgão ou empresa, são utilizados **11 Fatores de Design**:

1. **Estratégia corporativa (*Enterprise Strategy*):** Liderança em custos, diferenciação, inovação ou prestação de serviços essenciais.
2. **Objetivos corporativos (*Enterprise Goals*):** As prioridades desdobradas no Balanced Scorecard.
3. **Perfil de risco (*Risk Profile*):** O apetite e a tolerância a riscos de TI da instituição.
4. **Problemas relacionados a I&T (*I&T-Related Issues*):** Histórico de falhas, projetos com estouro de orçamento ou carência de competências.
5. **Cenário de ameaças (*Threat Landscape*):** Grau de exposição a ataques cibernéticos e espionagem de dados.
6. **Requisitos de conformidade (*Compliance Requirements*):** Rigidez regulatória externa (ex.: setor público sujeito à fiscalização do TCU/TCE vs. startups).
7. **Papel da TI (*Role of IT*):** Papel estratégico (TI como motor essencial da missão) vs. suporte (*back-office* básico).
8. **Modelo de fornecimento de TI (*Sourcing Model for IT*):** Terceirização (outsourcing), equipes próprias (insourcing), nuvem ou modelo híbrido.
9. **Métodos de implementação de TI (*IT Implementation Methods*):** Abordagens ágeis (DevOps, Scrum) vs. métodos tradicionais preditivos (cascata/waterfall).
10. **Estratégia de adoção de tecnologia (*Technology Adoption Strategy*):** Inovador pioneiro (*first mover*), seguidor rápido (*fast follower*) ou adotante conservador (*slow adopter*).
11. **Tamanho da organização (*Enterprise Size*):** Grande corporação / órgão público de grande porte vs. pequenas e médias organizações.

#### Áreas de Foco (*Focus Areas*)
Uma **Área de Foco** descreve um tópico, domínio de governança ou desafio tecnológico específico que requer a seleção e priorização de um conjunto direcionado de componentes e objetivos de governança do COBIT 2019. Exemplos de áreas de foco publicadas pela ISACA incluem: Segurança da Informação (*Information Security*), DevOps, Pequenas e Médias Empresas (PMEs) e Governança de Nuvem (*Cloud Governance*). As áreas de foco podem ser ilimitadas e são expandidas continuamente pela comunidade.

---

### Teste 470
**(FGV - TJ-RR - Analista Judiciário - Governança e Gestão de TI - Adaptada)**
**Enunciado:** No COBIT 2019, o sistema de governança deve ser moldado sob medida para cada organização, recusando a premissa de 'tamanho único' (*one size fits all*). Para essa personalização e adaptação (*tailoring*), o framework utiliza os Fatores de Design (*Design Factors*). Sobre os Fatores de Design e as Áreas de Foco no COBIT 2019, assinale a alternativa correta:  

* **A)** Os 11 Fatores de Design incluem aspectos como Estratégia corporativa, Perfil de risco, Cenário de ameaças, Requisitos de conformidade e Modelo de fornecimento de TI.
* **B)** As Áreas de Foco são rigidamente limitadas a exatamente 5 domínios fixos e imutáveis, sendo vedada pela ISACA a publicação de novos guias de foco temático.
* **C)** O Fator de Design 'Papel da TI' reconhece apenas a TI como área de apoio secundário, proibindo a classificação de TI como motor estratégico do negócio.
* **D)** Os Fatores de Design são aplicados exclusivamente após a conclusão integral de todos os 40 processos de gestão, atuando como ferramentas de auditoria punitiva.
* **E)** O tamanho da organização (*Enterprise Size*) não é considerado fator de design pelo COBIT 2019, aplicando-se exatamente o mesmo modelo e volume documental a qualquer porte institucional.


---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Os 11 fatores de design englobam estratégia institucional, objetivos, perfil de risco, problemas de I&T, cenário de ameaças, requisitos de conformidade, papel da TI, modelo de fornecimento, métodos de implementação, estratégia de adoção tecnológica e tamanho da organização.
> - **B)** Incorreta. Áreas de Foco podem ser ilimitadas e abertas, expandidas conforme o surgimento de novas demandas tecnológicas (ex.: Segurança, DevOps, Nuvem).
> - **C)** Incorreta. O papel da TI pode variar entre suporte, fábrica, transição e estratégico.
> - **D)** Incorreta. Fatores de design são utilizados no início, na concepção do sistema de governança (*design guide*), para selecionar e priorizar objetivos.
> - **E)** Incorreta. Tamanho da organização é expressamente o 11º Fator de Design.
> 
> **Gabarito: A**

---

## 3.4 Cascatamento de Objetivos (Goals Cascade)

O mecanismo do COBIT 2019 traduz as necessidades das partes interessadas em ações e objetivos práticos de TI por meio de quatro níveis em cascata:

```mermaid
flowchart TD
    N["1. Necessidades dos Stakeholders<br/>(Cidadãos, Jurisdicionados, Gestores)"] --> EG["2. Objetivos Corporativos (Enterprise Goals)<br/>13 Objetivos estruturados pelas dimensões BSC"]
    EG --> AG["3. Objetivos de Alinhamento (Alignment Goals)<br/>13 Objetivos de TI alinhados ao negócio"]
    AG --> GG["4. Objetivos de Governança e Gestão<br/>40 Objetivos nos 5 Domínios (EDM, APO, BAI, DSS, MEA)"]
```

- **1. Necessidades dos Stakeholders:** Criam os direcionadores corporativos e estratégicos do órgão.
- **2. 13 Objetivos Corporativos (*Enterprise Goals*):** Classificados sob as 4 dimensões do *Balanced Scorecard* (Financeira, Clientes, Processos Internos, Aprendizado e Crescimento).
- **3. 13 Objetivos de Alinhamento (*Alignment Goals*):** Objetivos técnicos de TI alinhados diretamente aos objetivos corporativos (no COBIT 5 eram 17 objetivos de TI; no COBIT 2019 foram otimizados para 13).
- **4. 40 Objetivos de Governança e Gestão:** Cada um associado a um processo e aos componentes do sistema.

---

### Teste 471
**(FCC - Auditor Fiscal da Receita Estadual / TI - Adaptada)**
**Enunciado:** Em uma auditoria de governança de TI no setor público, a equipe avaliou como as metas institucionais do órgão são traduzidas em prioridades concretas de investimento tecnológico por meio do mecanismo de Cascatamento de Objetivos (*Goals Cascade*) e dos Fatores de Design (*Design Factors*) do COBIT 2019. A respeito desses instrumentos, assinale a alternativa correta:  

* **A)** O cascatamento de objetivos do COBIT 2019 estabelece que as necessidades dos stakeholders devem ser desdobradas primeiramente em 13 Objetivos Corporativos (*Enterprise Goals*), os quais se desdobram em 13 Objetivos de Alinhamento (*Alignment Goals*) e, finalmente, nos 40 Objetivos de Governança e Gestão.
* **B)** Os Fatores de Design foram concebidos com a finalidade exclusiva de impedir a customização do COBIT 2019, tornando sua adoção rígida e idêntica para qualquer entidade do planeta.
* **C)** O Perfil de Risco e o Cenário de Ameaças são classificados pelo COBIT 2019 como objetivos de alinhamento financeiro, não exercendo papel na definição dos fatores de design.
* **D)** O número de objetivos corporativos no COBIT 2019 foi ampliado para 114 itens, abolindo-se a correlação com as perspectivas clássicas do Balanced Scorecard (BSC).
* **E)** A estratégia corporativa da organização não exerce influência sobre o desenho do sistema de governança de TI, sendo este definido exclusivamente pelo fornecedor de hardware.


---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** No COBIT 2019, a Cascata de Objetivos (*Goals Cascade*) segue a sequência rigorosa: Necessidades dos Stakeholders $\rightarrow$ 13 Objetivos Corporativos (*Enterprise Goals* estruturados no BSC) $\rightarrow$ 13 Objetivos de Alinhamento (*Alignment Goals*) $\rightarrow$ 40 Objetivos de Governança e Gestão nos domínios EDM, APO, BAI, DSS e MEA.
> - **B)** Incorreta. Os 11 Fatores de Design têm como propósito justamente permitir o *tailoring* (adaptação personalizada) do sistema de governança às particularidades de porte, risco, estratégia e maturidade de cada organização.
> - **C)** Incorreta. O Perfil de Risco (Design Factor 3) e o Cenário de Ameaças (Design Factor 5) são explicitamente Fatores de Design (*Design Factors*), e não objetivos de alinhamento.
> - **D)** Incorreta. São exatamente 13 Objetivos Corporativos no COBIT 2019, organizados diretamente sob as quatro dimensões clássicas do BSC (Financeira, Clientes, Processos Internos, Aprendizado e Crescimento).
> - **E)** Incorreta. A Estratégia Corporativa é o Fator de Design número 1 (*Design Factor 1*), exercendo impacto primordial sobre as prioridades e o sistema de governança de I&T.
> 
> **Gabarito: A**

---

## 3.5 Os 40 Objetivos de Governança e Gestão nos 5 Domínios

O COBIT 2019 organiza seus 40 objetivos em **5 Domínios**. O primeiro pertence exclusivamente à **Governança**, enquanto os demais quatro integram a **Gestão**:

```mermaid
flowchart TB
    subgraph GOV["Domínio de Governança (Board / Alta Cúpula)"]
        EDM["EDM: Avaliar, Dirigir e Monitorar (5 objetivos: EDM01 a EDM05)"]
    end

    subgraph MGT["Domínios de Gestão (Diretoria Executiva / Operação de TI)"]
        APO["APO: Alinhar, Planejar e Organizar (14 objetivos: APO01 a APO14)"]
        BAI["BAI: Construir, Adquirir e Implementar (11 objetivos: BAI01 a BAI11)"]
        DSS["DSS: Entregar, Servir e Suportar (6 objetivos: DSS01 a DSS06)"]
        MEA["MEA: Monitorar, Avaliar e Medir (4 objetivos: MEA01 a MEA04)"]
    end

    EDM --> APO
    APO --> BAI
    BAI --> DSS
    DSS --> MEA
    MEA --> EDM
```

#### Relação Detalhada dos 40 Objetivos do COBIT 2019

##### Domínio de Governança: EDM (*Evaluate, Direct and Monitor*) - 5 Objetivos
1. **EDM01:** Garantir a Definição e Manutenção do Framework de Governança.
2. **EDM02:** Garantir a Realização de Benefícios.
3. **EDM03:** Garantir a Otimização de Riscos.
4. **EDM04:** Garantir a Otimização de Recursos.
5. **EDM05:** Garantir o Engajamento das Partes Interessadas (*Stakeholder Engagement*).

##### Domínio de Gestão 1: APO (*Align, Plan and Organize*) - 14 Objetivos
1. **APO01:** Gerenciar o Framework de Gestão de I&T.
2. **APO02:** Gerenciar a Estratégia.
3. **APO03:** Gerenciar a Arquitetura Corporativa.
4. **APO04:** Gerenciar a Inovação.
5. **APO05:** Gerenciar o Portfólio.
6. **APO06:** Gerenciar o Orçamento e os Custos.
7. **APO07:** Gerenciar os Recursos Humanos.
8. **APO08:** Gerenciar os Relacionamentos.
9. **APO09:** Gerenciar os Acordos de Serviços (SLAs).
10. **APO10:** Gerenciar os Fornecedores.
11. **APO11:** Gerenciar a Qualidade.
12. **APO12:** Gerenciar os Riscos.
13. **APO13:** Gerenciar a Segurança.
14. **APO14:** Gerenciar os Dados *(Objetivo introduzido expressamente no COBIT 2019)*.

##### Domínio de Gestão 2: BAI (*Build, Acquire and Implement*) - 11 Objetivos
1. **BAI01:** Gerenciar Programas.
2. **BAI02:** Gerenciar a Definição de Requisitos.
3. **BAI03:** Gerenciar a Identificação e Construção de Soluções.
4. **BAI04:** Gerenciar a Disponibilidade e a Capacidade.
5. **BAI05:** Gerenciar a Mudança Organizacional.
6. **BAI06:** Gerenciar as Mudanças de TI (*IT Changes*).
7. **BAI07:** Gerenciar a Aceitação e Transição da Mudança de TI.
8. **BAI08:** Gerenciar o Conhecimento.
9. **BAI09:** Gerenciar os Ativos.
10. **BAI10:** Gerenciar a Configuração.
11. **BAI11:** Gerenciar Projetos *(Separado de Programas no COBIT 2019)*.

##### Domínio de Gestão 3: DSS (*Deliver, Service and Support*) - 6 Objetivos
1. **DSS01:** Gerenciar as Operações.
2. **DSS02:** Gerenciar as Requisições de Serviços e Incidentes.
3. **DSS03:** Gerenciar Problemas.
4. **DSS04:** Gerenciar a Continuidade.
5. **DSS05:** Gerenciar os Serviços de Segurança.
6. **DSS06:** Gerenciar os Controles de Processos de Negócio.

##### Domínio de Gestão 4: MEA (*Monitor, Evaluate and Assess*) - 4 Objetivos
1. **MEA01:** Monitorar, Avaliar e Medir o Desempenho e a Conformidade.
2. **MEA02:** Monitorar, Avaliar e Medir o Sistema de Controle Interno.
3. **MEA03:** Monitorar, Avaliar e Medir a Conformidade com Requisitos Externos.
4. **MEA04:** Monitorar, Avaliar e Medir a Garantia (*Assurance*).

---

### Teste 472
**(FCC - Auditor de Controle Externo / TI - Adaptada)**
**Enunciado:** O framework COBIT 2019 da ISACA estabelece uma distinção estrutural e operacional inequívoca entre Governança e Gestão de TI na organização. Com base nas definições dos domínios e competências organizacionais do COBIT 2019, assinale a alternativa correta:  

* **A)** A Governança tem como domínio executivo primário o APO (*Align, Plan and Organize*), sendo de sua competência a programação de sprints de desenvolvimento e a instalação de atualizações operacionais de sistemas.
* **B)** O domínio de Governança no COBIT 2019 é o EDM (*Evaluate, Direct and Monitor*), cabendo aos dirigentes máximos e comitês de governança avaliar necessidades, dirigir políticas e monitorar o alcance estratégico, enquanto a Gestão opera por meio de quatro domínios (APO, BAI, DSS e MEA).
* **C)** As atividades operacionais de atendimento a incidentes de suporte e requisições de serviço na Central de Serviços integram o domínio EDM, sob a responsabilidade direta dos membros do Conselho de Administração.
* **D)** O COBIT 2019 revogou o princípio da separação entre governança e gestão preconizado pelo COBIT 5, determinando que gerentes operacionais de redes acumulem privativamente as funções de deliberação estratégica e fixação de apetite a risco.
* **E)** O domínio BAI (*Build, Acquire and Implement*) é o único domínio classificado como de governança, destinando-se exclusivamente à fiscalização judicial de contratos públicos de TI.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O domínio APO pertence à Gestão, e não à Governança. Além disso, tarefas cotidianas como instalar atualizações operacionais pertencem à operação técnica (domínio DSS), e não ao planejamento tático ou à governança.
> - **B)** **Correta.** No COBIT 2019, o domínio exclusivo de governança é o EDM (*Evaluate, Direct and Monitor*), composto por 5 objetivos direcionados à Alta Administração (Board). Os domínios de Gestão são quatro: APO (*Align, Plan and Organize*), BAI (*Build, Acquire and Implement*), DSS (*Deliver, Service and Support*) e MEA (*Monitor, Evaluate and Assess*).
> - **C)** Incorreta. O atendimento a incidentes e requisições de serviço pertence ao domínio de gestão DSS (especificamente objetivo *DSS02 - Gerenciar Requisições de Serviços e Incidentes*), sendo executado pela Central de Serviços e equipes de suporte, jamais pelo Conselho de Administração.
> - **D)** Incorreta. O COBIT 2019 manteve inalterado o princípio basilar de que "Governança é distinta da gestão" (Princípio 4 do Sistema de Governança). A segregação de funções é imperativa para evitar conflitos de interesse e desvios de controle interno.
> - **E)** Incorreta. O domínio BAI é um domínio de Gestão (focado em construir, adquirir e implementar soluções, gerenciar projetos e mudanças), e não de governança, nem tem foco judicial exclusivo.
> 
> **Gabarito: B**

---

## 3.6 Gestão de Desempenho do COBIT (CPM) e Níveis de Capacidade CMMI

No COBIT 2019, o modelo de medição de capacidade e maturidade migrou da ISO/IEC 33000 (usada no COBIT 5) para a escala alinhada ao **CMMI** (*Capability Maturity Model Integration*).

```mermaid
flowchart LR
    N0["Nível 0<br/>Incompleto"] --> N1["Nível 1<br/>Executado<br/>(Initial / Performed)"]
    N1 --> N2["Nível 2<br/>Gerenciado<br/>(Managed)"]
    N2 --> N3["Nível 3<br/>Definido<br/>(Defined)"]
    N3 --> N4["Nível 4<br/>Quantitativamente<br/>Gerenciado"]
    N4 --> N5["Nível 5<br/>Em Otimização<br/>(Optimizing)"]
```

#### Níveis de Capacidade de Processo (CPM / CMMI: 0 a 5)

| Nível | Classificação | Descrição Prática do Desempenho do Processo |
| :---: | :--- | :--- |
| **0** | **Incompleto** (*Incomplete*) | O trabalho não atinge o propósito geral do processo. Poucas ou nenhuma atividade foram concluídas. |
| **1** | **Executado** (*Initial / Performed*) | O processo atinge seu propósito através de um conjunto incompleto de atividades; atua de forma intuitiva, sem padronização formal. |
| **2** | **Gerenciado** (*Managed*) | O processo é planejado, executado, monitorado e ajustado para atingir objetivos específicos. Os produtos de trabalho são controlados e mantidos adequadamente. |
| **3** | **Definido** (*Defined*) | O processo é bem caracterizado, compreendido e executado com base em procedimentos padronizados em toda a organização (*organizational standards*). |
| **4** | **Quantitativamente Gerenciado** (*Quantitatively Managed*) | O processo é controlado quantitativamente por meio de métricas estatísticas e técnicas de controle de qualidade, sendo altamente previsível. |
| **5** | **Em Otimização** (*Optimizing*) | O processo é continuamente aprimorado com base na compreensão quantitativa das causas de variações e na adoção de inovações tecnológicas. |

---

### Teste 473
**(FCC - Técnico de Controle Externo / TI - Adaptada)**
**Enunciado:** O modelo de Gestão de Desempenho do COBIT 2019 (CPM - *COBIT Performance Management*) utiliza a abordagem de Níveis de Capacidade de Processo (*Process Capability Levels*) alinhada ao CMMI, graduando a maturidade de execução de cada processo em uma escala de 0 a 5. Um processo que atinge o seu propósito por meio da aplicação de procedimentos formalmente padronizados, documentados e disseminados por toda a organização, classifica-se no:  

* **A)** Nível 0 - Incompleto (*Incomplete*).
* **B)** Nível 1 - Executado (*Initial / Performed*).
* **C)** Nível 2 - Gerenciado (*Managed*).
* **D)** Nível 3 - Definido (*Defined*).
* **E)** Nível 5 - Em Otimização (*Optimizing*).


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. No Nível 0 (Incompleto), o processo não atinge seu propósito; praticamente nenhuma atividade relevante foi executada.
> - **B)** Incorreta. No Nível 1 (Executado), o processo atinge seu propósito através de um conjunto incompleto de atividades, funcionando de forma ad-hoc, dependente do heroísmo individual e sem padrão.
> - **C)** Incorreta. No Nível 2 (Gerenciado), o processo é planejado, monitorado e controlado para um projeto ou unidade específica, gerando produtos de trabalho controlados, mas ainda não se tornou um padrão organizacional institucionalizado.
> - **D)** **Correta.** No Nível 3 (Definido), o processo é executado com base em um conjunto de procedimentos e normas documentadas e padronizadas em nível corporativo (*organizational standards*).
> - **E)** Incorreta. No Nível 5 (Em Otimização), o processo foca na melhoria contínua preditiva com base em inovações tecnológicas e controle estatístico de causas de variação (passando antes pelo Nível 4 - Quantitativamente Gerenciado).
> 
> **Gabarito: D**

---


#### Escala de Avaliação de Atividades e Práticas
Cada atividade é avaliada conforme a escala percentual de alcance:

- **N (Não Atingido / *Not Achieved*):** Evidência de alcance de $0\%$ a $15\%$.
- **P (Parcialmente Atingido / *Partially Achieved*):** Evidência de alcance de $> 15\%$ a $50\%$.
- **L (Praticamente Atingido / *Largely Achieved*):** Evidência de alcance de $> 50\%$ a $85\%$.
- **F (Totalmente Atingido / *Fully Achieved*):** Evidência de alcance de $> 85\%$ a $100\%$.

---

### Teste 474
**(FCC - TRT-14 - Analista Judiciário - Tecnologia da Informação - Adaptada)**
**Enunciado:** No modelo de Gestão de Desempenho do COBIT 2019 (CPM), para determinar o nível de capacidade de um processo, avalia-se o grau de alcance das práticas e atividades de governança e gestão por meio de uma escala percentual padrão dividida em quatro níveis (N, P, L e F). Assinale a alternativa que descreve corretamente essa escala:  

* **A)** Uma atividade com evidência de alcance entre maior que 15% e 50% é classificada como Parcialmente Atingida (*Partially Achieved* - P).
* **B)** Uma atividade com evidência de alcance de 0% a 15% é considerada Praticamente Atingida (*Largely Achieved* - L).
* **C)** Uma atividade é considerada Totalmente Atingida (*Fully Achieved* - F) apenas quando atinge 100% de conformidade formal sem qualquer margem de tolerância.
* **D)** A classificação 'Não Atingido' (*Not Achieved* - N) exige demonstração de fraude ou negligência dolosa comprovada por auditoria externa.
* **E)** A escala N-P-L-F foi descontinuada no COBIT 2019 e substituída exclusivamente pelo modelo binário de Sucesso ou Falha.


---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme a régua oficial do CPM/CMMI: N (Não Atingido: 0% a 15%), P (Parcialmente Atingido: > 15% a 50%), L (Praticamente Atingido: > 50% a 85%) e F (Totalmente Atingido: > 85% a 100%).
> - **B)** Incorreta. De 0% a 15% a classificação é Não Atingido (*Not Achieved* - N). Praticamente Atingido (L) situa-se na faixa de > 50% a 85%.
> - **C)** Incorreta. Totalmente Atingido (F) abrange a faixa superior de > 85% até 100%.
> - **D)** Incorreta. A classificação N reflete ausência ou nível incipiente de evidências de execução (0% a 15%), sem relação com fraude ou dolo.
> - **E)** Incorreta. A escala N-P-L-F permanece a métrica de avaliação contínua de atividades e práticas do COBIT 2019.
> 
> **Gabarito: A**

---

## 6. Fontes Recomendadas na Internet

* [ISACA - COBIT Framework Resources](https://www.isaca.org/resources/cobit) - Visão geral oficial do COBIT 2019, princípios de governança, objetivos de gestão e fatores de desenho.
* [TCU - Governança Pública e de TI no TCU](https://portal.tcu.gov.br/governanca/governanca-no-tcu/) - Referencial institucional do TCU para avaliação e controle da governança nas organizações públicas.
* [Decreto nº 12.198/2024 (Estratégia Nacional de Governo Digital)](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2024/decreto/d12198.htm) - Institui a Estratégia Nacional de Governo Digital para o ciclo 2024-2027.
* [Decreto Federal nº 9.203/2017 (Governança Pública)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2017/decreto/d9203.htm) - Dispõe sobre a política de governança da administração pública federal e mecanismos de liderança, estratégia e controle.
* [Governo Digital - Sistema de Administração dos Recursos de TIC (SISP)](https://www.gov.br/governodigital/pt-br/estrategias-e-governanca-digital/sisp/sobre-o-sisp) - Estrutura de governança e alinhamento estratégico de TI no setor público.
* FERNANDES, Aguinaldo Aragon; ABREU, Vladimir Ferraz de. **Implantando a Governança de TI: da Estratégia aos Processos**. 4. ed. Rio de Janeiro: Brasport, 2014. (Cap. 1 a 4 - Fundamentos de Governança, COBIT e ISO/IEC 38500).
* ISACA. **COBIT 2019 Framework: Introduction and Methodology**. Schaumburg: ISACA, 2018. (Cap. 2 - Principles; Cap. 4 - Governance and Management Objectives).
* ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **ABNT NBR ISO/IEC 38500:2018**: Governança corporativa de tecnologia da informação. Rio de Janeiro: ABNT, 2018.
