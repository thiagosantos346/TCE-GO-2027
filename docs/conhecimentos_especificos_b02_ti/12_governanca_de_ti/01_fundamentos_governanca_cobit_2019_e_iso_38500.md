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
**(FCC – TRT-13 – Analista Judiciario Tecnologia da Informacao – 2014)**
Observe as seguintes considerações do modelo de maturidade do processo Cobit 4.1, Definir um Plano Estratégico de TI: I. O planejamento estratégico de TI é uma prática padrão cujas exceções são detectadas pela Direção. É uma função da Direção com nível sênior de responsabilidade. A Direção é capaz de monitorar o processo de planejamento estratégico de TI, tomar decisões baseadas nesse processo e medir sua efetividade. Os planejamentos de TI, de curto e longo prazos, são cascateados de cima para baixo na organização, com atualizações quando necessário. A estratégia de TI e a estratégia global da organização estão se tornando gradativamente mais coordenadas por abordar processos de negócio, capacidades de valor agregado e alavancar o uso de aplicativos e tecnologias na reengenharia dos processos de negócios. Há um processo bem definido para determinar o uso dos recursos internos e externos no desenvolvimento de sistema e operações. II. O planejamento estratégico de TI é compartilhado com a Direção do Negócio conforme a necessidade. A atualização dos planos de TI acontece em resposta aos pedidos da Direção. As decisões estratégicas são tomadas projeto a projeto, sem consistência com uma estratégia corporativa. Os riscos e benefícios do usuário nas principais decisões estratégicas são determinados de forma intuitiva. As considerações I e II referem-se, respectivamente, aos níveis

* **A)** Gerenciado e Mensurável - Inicial/ Ad hoc
* **B)** Otimizado - Processo Definido
* **C)** Gerenciado e Mensurável - Repetível, porém Intuitivo
* **D)** Processo Definido - Inicial/ Ad hoc
* **E)** Inicial/ Ad hoc - Inexistente

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Gerenciado e Mensurável - Inicial/ Ad hoc". De acordo com a teoria estudada em *1.2 Alinhamento Estratégico e Criação de Valor Público*, isso significa garantir que os recursos aplicados em tecnologia resultem em fiscalizações mais ágeis, auditorias digitais baseadas em cruzamento massivo de dados, transparência ativa ao cidadão e prestação jurisdicional de excelência.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Otimizado - Processo Definido". De acordo com a teoria estudada em *Níveis de Capacidade de Processo (CPM / CMMI: 0 a 5)*, 3: Definido (*Defined*) — O processo é bem caracterizado, compreendido e executado com base em procedimentos padronizados em toda a organização (*organizational standards*).
> - **C)** **Correta.** Conforme fundamentado na seção *Tabela Comparativa dos Princípios do COBIT 2019* deste guia, 1. Prover valor aos stakeholders: O sistema deve gerar valor a partir do uso de I&T balanceando benefícios, riscos e uso otimizado de recursos.: 1. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT-13/2014) ao estabelecer que "Gerenciado e Mensurável - Repetível, porém Intuitivo".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Processo Definido - Inicial/ Ad hoc". De acordo com a teoria estudada em *Níveis de Capacidade de Processo (CPM / CMMI: 0 a 5)*, 2: Gerenciado (*Managed*) — O processo é planejado, executado, monitorado e ajustado para atingir objetivos específicos. Os produtos de trabalho são controlados e mantidos adequadamente.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Inicial/ Ad hoc - Inexistente". De acordo com a teoria estudada em *Níveis de Capacidade de Processo (CPM / CMMI: 0 a 5)*, 4: Quantitativamente Gerenciado (*Quantitatively Managed*) — O processo é controlado quantitativamente por meio de métricas estatísticas e técnicas de controle de qualidade, sendo altamente previsível.
>
> **Gabarito: C**

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
**(FGV – TCE-PA – Auditor de Controle Externo Administrativa Ciencia de Dados – 2024)**
A Governança Corporativa de TI busca fazer o alinhamento entre a área de Tecnologia da Informação (TI) em uma organização com os objetivos estratégicos e operacionais da empresa. Para isso, algumas normas buscam caminhos para alcançar tal alinhamento. O principal objetivo da norma ABNT NBR ISO/IEC 38500 em Governança Corporativa de TI é

* **A)** definir requisitos técnicos específicos para sistemas de TI.
* **B)** estabelecer diretrizes para a gestão eficaz da governança de TI.
* **C)** fornecer procedimentos detalhados para auditoria de segurança da informação.
* **D)** implementar práticas para desenvolvimento ágil de software.
* **E)** padronizar protocolos de rede para interoperabilidade entre sistemas.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "definir requisitos técnicos específicos para sistemas de TI". De acordo com a teoria estudada em *6. Fontes Recomendadas na Internet*, aSSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. ABNT NBR ISO/IEC 38500:2018: Governança corporativa de tecnologia da informação. Rio de Janeiro: ABNT, 2018.
> - **B)** **Correta.** Conforme fundamentado na seção *2.1 Escopo e Modelo de Governança (Ciclo EDM)* deste guia, a norma ABNT NBR ISO/IEC 38500:2024 fornece princípios e diretrizes para os órgãos deliberativos e membros da alta administração das organizações (públicas ou privadas, de qualquer porte ou setor) sobre a utilização aceitável, eficaz e eficiente da TI. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE-PA/2024) ao estabelecer que "estabelecer diretrizes para a gestão eficaz da governança de TI".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "fornecer procedimentos detalhados para auditoria de segurança da informação". De acordo com a teoria estudada em *3.2 Componentes do Sistema de Governança (7 Componentes)*, informação: Dados e fluxos informacionais consumidos e produzidos pela organização (relevância, segurança, precisão, completude).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "implementar práticas para desenvolvimento ágil de software". De acordo com a teoria estudada em *Tabela Comparativa: Governança de TI versus Gestão de TI*, responsável Típico: Alta Administração, Conselho de Administração, Plenário e Comitês Estratégicos de Governança. — Diretoria Executiva de TI (CIO/DTI), gerentes de projetos, equipes de desenvolvimento e suporte.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "padronizar protocolos de rede para interoperabilidade entre sistemas". De acordo com a teoria estudada em *Tabela Comparativa: Governança de TI versus Gestão de TI*, objetivo Maior: Criação de Valor: Realização de benefícios com balanceamento e otimização de riscos e recursos. — Eficiência técnica, cumprimento estrito de SLAs, produtividade e estabilidade dos sistemas em produção.
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
**(FCC – TRT-2 – Analista Judiciario Tecnologia da Informacao – 2014)**
Considere as afirmativas sobre a Norma NBR ISO/IEC 12207 e a Norma ISO/IEC 20968. I. A Norma NBR ISO/IEC 12207: 2009 possui duas seções principais para tratar os processos de software: Processos de Contexto de Sistema, para ser utilizado na implementação de um produto ou de um serviço de software que seja elemento de um sistema maior, e Processos Específicos de Software, para lidar com produto ou serviço de software ou um sistema de software independente. II. O método definido pela Norma ISO/IEC 20968: 2002 pode ser usado para medir o tamanho funcional de qualquer aplicação de software que possa ser descrita em termos de transações lógicas, cada uma composta por um componente de entrada, processo e saída. As regras de tamanho foram designadas para aplicações de software do domínio de sistemas de informação de negócios, nas quais o componente de processamento de cada transação tende a ser determinado por considerações de armazenamento ou recuperação de informação. III. Há duas categorias de processos de projeto, de acordo com a Norma NBR ISO/IEC 12207: 2009, Processos de Gestão de Projeto, utilizados para planejar, executar, avaliar e controlar o progresso de um projeto e Processos de Apoio ao Projeto, que fornecem um conjunto de tarefas específicas focadas na execução de um objetivo de gerenciamento especializado. Está correto o que consta APENAS em

* **A)** I e II.
* **B)** III.
* **C)** II e III.
* **D)** I e III.
* **E)** I.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I e II". De acordo com a teoria estudada em *Tabela Comparativa: Governança de TI versus Gestão de TI*, objetivo Maior: Criação de Valor: Realização de benefícios com balanceamento e otimização de riscos e recursos. — Eficiência técnica, cumprimento estrito de SLAs, produtividade e estabilidade dos sistemas em produção.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "III". De acordo com a teoria estudada em *Tabela Comparativa: Governança de TI versus Gestão de TI*, a banca frequentemente tenta confundir o candidato atribuindo à Governança tarefas de execução (como configurar roteadores, gerenciar chamados de help desk ou planejar sprints).
> - **C)** **Correta.** Conforme fundamentado na seção *2.1 Escopo e Modelo de Governança (Ciclo EDM)* deste guia, a norma ABNT NBR ISO/IEC 38500:2024 fornece princípios e diretrizes para os órgãos deliberativos e membros da alta administração das organizações (públicas ou privadas, de qualquer porte ou setor) sobre a utilização aceitável, eficaz e eficiente da TI. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT-2/2014) ao estabelecer que "II e III".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I e III". De acordo com a teoria estudada em *Tabela Comparativa: Governança de TI versus Gestão de TI*, atividades Centrais: EDM: Avaliar (*Evaluate*), Dirigir (*Direct*) e Monitorar (*Monitor*). — PBRM: Planejar (*Plan*), Construir (*Build*), Executar (*Run*) e Monitorar (*Monitor*).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I". De acordo com a teoria estudada em *6. Fontes Recomendadas na Internet*, aSSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. ABNT NBR ISO/IEC 38500:2018: Governança corporativa de tecnologia da informação. Rio de Janeiro: ABNT, 2018.
>
> **Gabarito: C**

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
**(FGV – TRF-1 – Analista Judiciario Area Apoio Especializado Especialidade Suporte Em Tecnologia da Informacao – 2024)**
Os princípios de governança do COBIT 2019® descrevem os principais requisitos de um sistema de governança para informações e tecnologia da organização. O princípio “sistema de governança dinâmico” determina que um sistema de governança deve:

* **A)** atender às necessidades das partes interessadas;
* **B)** distinguir claramente entre as atividades e estruturas de governança e gestão;
* **C)** ser construído a partir de vários componentes, que podem ser de diferentes tipos e que trabalham juntos;
* **D)** ser capaz de considerar os impactos da alteração de um ou mais fatores de desenho no sistema de governança;
* **E)** ser adaptado para as necessidades da organização usando um conjunto de fatores de desenho como parâmetros para adaptar e priorizar os componentes do sistema de governança.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "atender às necessidades das partes interessadas". De acordo com a teoria estudada em *3.4 Cascatamento de Objetivos (Goals Cascade)*, o mecanismo do COBIT 2019 traduz as necessidades das partes interessadas em ações e objetivos práticos de TI por meio de quatro níveis em cascata.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "distinguir claramente entre as atividades e estruturas de governança e gestão". De acordo com a teoria estudada em *Tabela Comparativa dos Princípios do COBIT 2019*, 3. Sistema dinâmico: Sempre que um ou mais fatores de design mudarem, o impacto sobre o sistema de governança deve ser reavaliado.: 3. Alinhado aos principais padrões: Deve harmonizar-se com os padrões de referência (ISO, ITIL, TOGAF, PMBOK, NIST).
> - **C)** **Correta.** Conforme fundamentado na seção *Tabela Comparativa dos Princípios do COBIT 2019* deste guia, 2. Abordagem holística: O sistema é construído a partir de múltiplos tipos de componentes integrados entre si.: 2. Aberto e flexível: Deve permitir a inclusão de novos conteúdos e tecnologias emergentes sem desestruturar o núcleo original. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRF-1/2024) ao estabelecer que "ser construído a partir de vários componentes, que podem ser de diferentes tipos e que trabalham juntos".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "ser capaz de considerar os impactos da alteração de um ou mais fatores de desenho no sistema de governança". De acordo com a teoria estudada em *Tabela Comparativa dos Princípios do COBIT 2019*, 1. Prover valor aos stakeholders: O sistema deve gerar valor a partir do uso de I&T balanceando benefícios, riscos e uso otimizado de recursos.: 1.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "ser adaptado para as necessidades da organização usando um conjunto de fatores de desenho como parâmetros para...". De acordo com a teoria estudada em *Tabela Comparativa dos Princípios do COBIT 2019*, 5. Adaptado às necessidades corporativas: Deve ser customizado conforme o contexto organizacional por meio de fatores de design (*tailoring*).: —.
>
> **Gabarito: C**

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
**(FGV – TRT-24 – Tecnico Judiciario Area Administrativa Sem Especialidade – 2025)**
A governança pública organizacional envolve a aplicação de práticas de liderança, estratégia e controle para que os gestores e as partes interessadas possam avaliar, direcionar e monitorar a atuação da organização pública, com o objetivo de melhorar os resultados entregues aos cidadãos, especialmente em serviços e políticas públicas. Assinale a opção que apresenta, corretamente, a diferença entre governança e gestão.

* **A)** A governança concentra-se em planejar e executar atividades, enquanto a gestão é voltada para avaliar e monitorar a eficácia organizacional.
* **B)** A governança foca em aspectos como eficácia e eficiência, enquanto a gestão ocupa-se da estratégia e do planejamento organizacional.
* **C)** A governança está relacionada à avaliação, à direção e ao monitoramento em prol da efetividade, enquanto a gestão envolve planejar, executar e controlar as atividades organizacionais visando à eficiência.
* **D)** A gestão é responsável por avaliar a eficácia econômica e monitorar as atividades, enquanto a governança trata de planejar e controlar os recursos.
* **E)** A governança e a gestão são processos idênticos, sem distinção clara entre suas funções dentro da organização.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A governança concentra-se em planejar e executar atividades, enquanto a gestão é voltada para avaliar e monitorar...". De acordo com a teoria estudada em *Tabela Comparativa: Governança de TI versus Gestão de TI*, atividades Centrais: EDM: Avaliar (*Evaluate*), Dirigir (*Direct*) e Monitorar (*Monitor*). — PBRM: Planejar (*Plan*), Construir (*Build*), Executar (*Run*) e Monitorar (*Monitor*).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A governança foca em aspectos como eficácia e eficiência, enquanto a gestão ocupa-se da estratégia e do...". De acordo com a teoria estudada em *2.2 Os Seis Princípios da Boa Governança de TI*, 4: Desempenho (*Performance*) — A TI atende às necessidades da organização, entregando serviços com os níveis de serviço e capacidade exigidos pelo negócio. — Monitoramento contínuo de disponibilidade, tempo de resposta e eficácia dos sistemas em produção.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A governança está relacionada à avaliação, à direção e ao monitoramento em prol da efetividade, enquanto a gestão...". De acordo com a teoria estudada em *Tabela Comparativa: Governança de TI versus Gestão de TI*, objetivo Maior: Criação de Valor: Realização de benefícios com balanceamento e otimização de riscos e recursos. — Eficiência técnica, cumprimento estrito de SLAs, produtividade e estabilidade dos sistemas em produção.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A gestão é responsável por avaliar a eficácia econômica e monitorar as atividades, enquanto a governança trata de...". De acordo com a teoria estudada em *1.1 Distinção Essencial entre Governança e Gestão*, trata-se de responsabilidades, papéis e ciclos operacionais completamente distintos, embora fortemente integrados.
> - **E)** **Correta.** Conforme fundamentado na seção *Tabela Comparativa dos Princípios do COBIT 2019* deste guia, 4. Governança distinta da gestão: O sistema mantém clara separação estrutural e conceitual entre governança e gestão.: —. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT-24/2025) ao estabelecer que "A governança e a gestão são processos idênticos, sem distinção clara entre suas funções dentro da organização".
>
> **Gabarito: E**

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
**(FGV – TJ-MT – Analista Judiciario Tecnologia da Informacao – 2024)**
A governança de dados é um conjunto de práticas, processos e políticas que garantem a disponibilidade, integridade, segurança e usabilidade dos dados dentro de uma organização. Ela envolve a criação de regras e a definição de responsabilidades para a gestão dos dados ao longo de seu ciclo de vida. Diferentes tipos de governança de dados podem ser implementados, dependendo dos objetivos da organização e dos requisitos regulatórios. No contexto de Governança de Dados, no modelo de governança de dados colegiado

* **A)** a governança de dados é centralizada em uma única equipe responsável por todas as decisões, garantindo padronização e controle rígido.
* **B)** múltiplas áreas da organização compartilham a responsabilidade pelas decisões de dados, com a liderança de um comitê ou grupo interdepartamental.
* **C)** todas as decisões são tomadas de forma independente por cada equipe de dados, sem coordenação centralizada.
* **D)** a governança de dados é mantida por um único setor que gerencia a coleta, o armazenamento e a análise dos dados de toda a organização.
* **E)** a responsabilidade de governança é atribuída exclusivamente aos usuários finais dos dados, garantindo maior autonomia para o uso.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "a governança de dados é centralizada em uma única equipe responsável por todas as decisões, garantindo...". De acordo com a teoria estudada em *2.2 Os Seis Princípios da Boa Governança de TI*, 6: Comportamento Humano (*Human Behaviour*) — As políticas, práticas e decisões de TI respeitam os fatores humanos, culturais e as necessidades de todas as pessoas envolvidas. — Treinamento, usabilidade, ergonomia, acessibilidade e gestão de mudanças comportamentais no trabalho.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "múltiplas áreas da organização compartilham a responsabilidade pelas decisões de dados, com a liderança de um...". De acordo com a teoria estudada em *Tabela Comparativa dos Princípios do COBIT 2019*, 6. Sistema ponta a ponta: Cobre todas as informações e tecnologias de toda a organização, e não apenas o departamento de TI.: —.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "todas as decisões são tomadas de forma independente por cada equipe de dados, sem coordenação centralizada". De acordo com a teoria estudada em *Níveis de Capacidade de Processo (CPM / CMMI: 0 a 5)*, 3: Definido (*Defined*) — O processo é bem caracterizado, compreendido e executado com base em procedimentos padronizados em toda a organização (*organizational standards*).
> - **D)** **Correta.** Conforme fundamentado na seção *3.2 Componentes do Sistema de Governança (7 Componentes)* deste guia, informação: Dados e fluxos informacionais consumidos e produzidos pela organização (relevância, segurança, precisão, completude). Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ-MT/2024) ao estabelecer que "a governança de dados é mantida por um único setor que gerencia a coleta, o armazenamento e a análise dos dados de...".
> - **E)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "a responsabilidade de governança é atribuída exclusivamente aos usuários finais dos dados, garantindo maior...". De acordo com a teoria estudada em *Os 11 Fatores de Design (Design Factors)*, o COBIT 2019 não adota o modelo "tamanho único" (*one size fits all*). Para viabilizar a adaptação (*tailoring*) do sistema de governança à realidade de cada órgão ou empresa, são utilizados 11 Fatores de Design.
>
> **Gabarito: D**

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
**(FCC – TRT-9 – Analista Judiciario Apoio Especializado Tecnologia da Informacao – 2015)**
Seguindo as boas práticas preconizadas pelo COBIT 5, um Analista da área de TI elencou as seguintes perguntas: − Como posso saber se as operações de um parceiro comercial são seguras e confiáveis? − Como posso saber se a organização cumpre as regras e regulamentos aplicáveis? − Como posso saber se a organização mantém um sistema eficiente de controle interno? − Os parceiros comerciais têm a cadeia de informações entre eles sob controle? De acordo com o COBIT 5, estas perguntas

* **A)** são dirigidas às partes interessadas externas. Estão relacionadas aos objetivos corporativos, versam sobre governança e gestão de TI da organização e servem como entrada para a cascata de objetivos.
* **B)** visam unificar a criação de valor para as diversas partes interessadas de uma organização. Gestão de contratos é negociar e decidir entre os interesses de valor das diferentes partes interessadas externas.
* **C)** indicam que o sistema de governança de TI deve considerar apenas as partes interessadas externas ao tomar decisões sobre a avaliação dos recursos, benefícios e riscos.
* **D)** referem-se às necessidades das partes interessadas internas e norteiam a cascata de objetivos do COBIT 5, que é o mecanismo de tradução das necessidades dos stakeholders em objetivos corporativos amplos e gerais.
* **E)** refletem a cascata de objetivos, que deve ser seguida à risca, pois contém o mapeamento universal entre os objetivos corporativos e os objetivos de TI e entre os objetivos de TI e os habilitadores do COBIT 5.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *3.4 Cascatamento de Objetivos (Goals Cascade)* deste guia, o mecanismo do COBIT 2019 traduz as necessidades das partes interessadas em ações e objetivos práticos de TI por meio de quatro níveis em cascata. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT-9/2015) ao estabelecer que "são dirigidas às partes interessadas externas. Estão relacionadas aos objetivos corporativos, versam sobre...".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "visam unificar a criação de valor para as diversas partes interessadas de uma organização. Gestão de contratos é...". De acordo com a teoria estudada em *Tabela Comparativa: Governança de TI versus Gestão de TI*, ponto de Partida: Necessidades das partes interessadas (*stakeholders*: cidadãos, magistrados, auditores, jurisdicionados). — Diretrizes, limites orçamentários, apetite a risco e prioridades deliberadas pela governança.
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "indicam que o sistema de governança de TI deve considerar apenas as partes interessadas externas ao tomar decisões...". De acordo com a teoria estudada em *Tabela Comparativa dos Princípios do COBIT 2019*, 1. Prover valor aos stakeholders: O sistema deve gerar valor a partir do uso de I&T balanceando benefícios, riscos e uso otimizado de recursos.: 1.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "referem-se às necessidades das partes interessadas internas e norteiam a cascata de objetivos do COBIT 5, que é o...". De acordo com a teoria estudada em *3.4 Cascatamento de Objetivos (Goals Cascade)*, 1. Necessidades dos Stakeholders: Criam os direcionadores corporativos e estratégicos do órgão.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "refletem a cascata de objetivos, que deve ser seguida à risca, pois contém o mapeamento universal entre os...". De acordo com a teoria estudada em *Relação Detalhada dos 40 Objetivos do COBIT 2019*, eDM05: Garantir o Engajamento das Partes Interessadas (*Stakeholder Engagement*).
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
**(FGV – TJ-RR – Analista Judiciario Gestao e Governanca de Tecnologia da Informacao – 2024)**
O COBIT 2019 é um framework de governança e gestão de Tecnologia da Informação (TI) que fornece um conjunto de princípios, práticas e ferramentas para ajudar as organizações a alcançarem seus objetivos estratégicos por meio do gerenciamento eficaz da informação e tecnologia. Ele se concentra em garantir que a TI esteja alinhada com as metas da empresa, gerando valor e gerenciando riscos de forma eficiente. Entre os domínios que agrupam os objetivos da gestão no COBIT 2019 listados a seguir, assinale aquele que foca em como os objetivos estratégicos são traduzidos em planos táticos e operacionais, garantindo o alinhamento entre TI e os objetivos do negócio.

* **A)** Alinhar, Planejar e Organizar (APO -Align, Plan, and Organize).
* **B)** Construir, Adquirir e Implantar (BAI -Buid, Acquire, and Implement).
* **C)** Entregar, Prestar Serviço e Dar e Suporte (DSS - Deliver, Service, and Support).
* **D)** Monitorar, Avaliar e Melhorar (MEA -Monitor, Evaluate, and Assess).
* **E)** Construir, Adquirir e Melhorar (BEA – Bild, Evaluate and Assess).

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *Tabela Comparativa: Governança de TI versus Gestão de TI* deste guia, atividades Centrais: EDM: Avaliar (*Evaluate*), Dirigir (*Direct*) e Monitorar (*Monitor*). — PBRM: Planejar (*Plan*), Construir (*Build*), Executar (*Run*) e Monitorar (*Monitor*). Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ-RR/2024) ao estabelecer que "Alinhar, Planejar e Organizar (APO -Align, Plan, and Organize)".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Construir, Adquirir e Implantar (BAI -Buid, Acquire, and Implement)". De acordo com a teoria estudada em *3. Framework COBIT 2019 (ISACA)*, o COBIT 2019 (*Control Objectives for Information and Related Technologies*) é o framework líder mundial de governança e gestão corporativa de informação e tecnologia (I&T), publicado pela ISACA.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Entregar, Prestar Serviço e Dar e Suporte (DSS - Deliver, Service, and Support)". De acordo com a teoria estudada em *2.1 Escopo e Modelo de Governança (Ciclo EDM)*, a norma ABNT NBR ISO/IEC 38500:2024 fornece princípios e diretrizes para os órgãos deliberativos e membros da alta administração das organizações (públicas ou privadas, de qualquer porte ou setor) sobre a utilização aceitável, eficaz e eficiente da TI.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Monitorar, Avaliar e Melhorar (MEA -Monitor, Evaluate, and Assess)". De acordo com a teoria estudada em *2.1 Escopo e Modelo de Governança (Ciclo EDM)*, monitorar (*Monitor*): Acompanhar periodicamente se a gestão está operando em conformidade com as diretrizes e se os objetivos de desempenho planejados estão sendo atingidos.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Construir, Adquirir e Melhorar (BEA – Bild, Evaluate and Assess)". De acordo com a teoria estudada em *6. Fontes Recomendadas na Internet*, iSACA. COBIT 2019 Framework: Introduction and Methodology. Schaumburg: ISACA, 2018. (Cap. 2 - Principles; Cap. 4 - Governance and Management Objectives).
>
> **Gabarito: A**

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
**(FCC – TRT-24 – Analista Judiciario Tecnologia da Informacao – 2017)**
O guia do COBIT 5 traz considerações acerca dos modelos de capacidade x maturidade, sobre os quais é correto afirmar que

* **A)** o modelo de maturidade do COBIT 5 visa produzir um perfil de maturidade da organização. Esta abordagem pode ser utilizada caso haja foco na melhoria em vez da necessidade de obter um número de maturidade para fins de relatório.
* **B)** uma organização que utilizava a abordagem dos atributos do modelo de maturidade do COBIT 4.1 poderá reutilizar os dados da sua avaliação e reclassificá-los segundo as avaliações de atributos do COBIT 5.
* **C)** os atributos de capacidade de processo do COBIT 4.1 e os atributos de maturidade do COBIT 5 não são idênticos.
* **D)** não há mais um modelo de capacidade específico por processo detalhado no COBIT 5, porque a abordagem da avaliação da maturidade de processo ISO/IEC 15505 não exige isso e ainda proíbe esta abordagem.
* **E)** no COBIT 5 o modelo de avaliação fornece uma escala de medição para cada atributo de maturidade e orientação sobre como aplicá-la, então para cada processo uma avaliação pode ser feita para cada um dos seis atributos de capacidade.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "o modelo de maturidade do COBIT 5 visa produzir um perfil de maturidade da organização. Esta abordagem pode ser...". De acordo com a teoria estudada em *Tabela Comparativa dos Princípios do COBIT 2019*, 3. Sistema dinâmico: Sempre que um ou mais fatores de design mudarem, o impacto sobre o sistema de governança deve ser reavaliado.: 3. Alinhado aos principais padrões: Deve harmonizar-se com os padrões de referência (ISO, ITIL, TOGAF, PMBOK, NIST).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "uma organização que utilizava a abordagem dos atributos do modelo de maturidade do COBIT 4.1 poderá reutilizar os...". De acordo com a teoria estudada em *Níveis de Capacidade de Processo (CPM / CMMI: 0 a 5)*, 3: Definido (*Defined*) — O processo é bem caracterizado, compreendido e executado com base em procedimentos padronizados em toda a organização (*organizational standards*).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "os atributos de capacidade de processo do COBIT 4.1 e os atributos de maturidade do COBIT 5 não são idênticos". De acordo com a teoria estudada em *2.1 Escopo e Modelo de Governança (Ciclo EDM)*, a norma ABNT NBR ISO/IEC 38500:2024 fornece princípios e diretrizes para os órgãos deliberativos e membros da alta administração das organizações (públicas ou privadas, de qualquer porte ou setor) sobre a utilização aceitável, eficaz e eficiente da TI.
> - **D)** **Correta.** Conforme fundamentado na seção *3.6 Gestão de Desempenho do COBIT (CPM) e Níveis de Capacidade CMMI* deste guia, no COBIT 2019, o modelo de medição de capacidade e maturidade migrou da ISO/IEC 33000 (usada no COBIT 5) para a escala alinhada ao CMMI (*Capability Maturity Model Integration*). Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT-24/2017) ao estabelecer que "não há mais um modelo de capacidade específico por processo detalhado no COBIT 5, porque a abordagem da avaliação...".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "no COBIT 5 o modelo de avaliação fornece uma escala de medição para cada atributo de maturidade e orientação sobre...". De acordo com a teoria estudada em *2.2 Os Seis Princípios da Boa Governança de TI*, autoridade delegada deve ser proporcional à responsabilidade. — Não pode haver ambiguidade de papéis; a responsabilidade de governança jamais pode ser transferida ou terceirizada a fornecedores externos.
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
**(FCC – TRT-23 – Analista Judiciario Apoio Especializado Tecnologia da Informacao – 2016)**
De acordo com a referência mundial em Gerenciamento de Processos de Negócio − BPM, durante a Análise de Processo o Analista deve observar diversas situações. Dentre elas: I. Fatores que impõem restrições e direcionam decisões que impactam a natureza e o desempenho do processo. Frequentemente esses fatores são criados sem suficiente compreensão dos cenários que a organização pode encontrar ou se tornam desconectados devido a mudanças não gerenciadas. II. Elementos que testam os limites de sustentação inferior e superior do processo e determinam se seus fatores de execução podem apropriadamente diminuir ou aumentar em escala para atender à demanda. III. Elementos que restringem a capacidade do processo e criam uma fila. Os itens I, II e III correspondem, correta e respectivamente, aos elementos

* **A)** gargalo, regras de negócio e capacidade.
* **B)** gargalo, capacidade e regras de negócio.
* **C)** capacidade, regras de negócio e gargalo.
* **D)** regras de negócio, capacidade e gargalo.
* **E)** regras de negócio, gargalo e capacidade.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "gargalo, regras de negócio e capacidade". De acordo com a teoria estudada em *Níveis de Capacidade de Processo (CPM / CMMI: 0 a 5)*, 5: Em Otimização (*Optimizing*) — O processo é continuamente aprimorado com base na compreensão quantitativa das causas de variações e na adoção de inovações tecnológicas.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "gargalo, capacidade e regras de negócio". De acordo com a teoria estudada em *3.6 Gestão de Desempenho do COBIT (CPM) e Níveis de Capacidade CMMI*, no COBIT 2019, o modelo de medição de capacidade e maturidade migrou da ISO/IEC 33000 (usada no COBIT 5) para a escala alinhada ao CMMI (*Capability Maturity Model Integration*).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "capacidade, regras de negócio e gargalo". De acordo com a teoria estudada em *Níveis de Capacidade de Processo (CPM / CMMI: 0 a 5)*, nível: Classificação — Descrição Prática do Desempenho do Processo.
> - **D)** **Correta.** Conforme fundamentado na seção *2.2 Os Seis Princípios da Boa Governança de TI* deste guia, 4: Desempenho (*Performance*) — A TI atende às necessidades da organização, entregando serviços com os níveis de serviço e capacidade exigidos pelo negócio. — Monitoramento contínuo de disponibilidade, tempo de resposta e eficácia dos sistemas em produção. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT-23/2016) ao estabelecer que "regras de negócio, capacidade e gargalo".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "regras de negócio, gargalo e capacidade". De acordo com a teoria estudada em *Níveis de Capacidade de Processo (CPM / CMMI: 0 a 5)*, 3: Definido (*Defined*) — O processo é bem caracterizado, compreendido e executado com base em procedimentos padronizados em toda a organização (*organizational standards*).
>
> **Gabarito: D**

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
