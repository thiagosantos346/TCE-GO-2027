# 01 - Ciclo de Vida e Metodologias Ágeis

> **Matéria:** Engenharia de Software  
> **Cargo:** B02 – Técnico de Controle Externo – Especialidade: Tecnologia da Informação  
> **Arquivo:** `01_ciclo_de_vida_e_metodologias_ageis.md`  

---

## 📌 Ementa / Itens do Edital
- Fundamentos da engenharia de software
- Ciclo de vida de software
- Abordagens de ciclo de vida preditiva, iterativa, incremental e adaptativa/ágil (e abordagens híbridas)
- Abordagens, métodos e frameworks ágeis: Scrum, Kanban, Lean Software Development e Extreme Programming (XP)

---

## 🧭 Sumário

1. [Fundamentos de Engenharia de Software e Processos](#1-fundamentos-de-engenharia-de-software-e-processos)
    1. [Escopo da Engenharia de Software e a Crise do Software](#11-escopo-da-engenharia-de-software-e-a-crise-do-software)
    2. [Atividades Genéricas de Processo de Software](#12-atividades-genericas-de-processo-de-software)
    3. [Modelos de Maturidade de Processo (CMMI e MPS.BR)](#13-modelos-de-maturidade-de-processo-cmmi-e-mpsbr)
    4. [Teste 001](#Teste-001)
2. [Modelos de Ciclo de Vida de Software](#2-modelos-de-ciclo-de-vida-de-software)
    1. [Abordagem Preditiva: Modelo Cascata (Waterfall) e Modelo V](#21-abordagem-preditiva-modelo-cascata-waterfall-e-modelo-v)
    2. [Abordagem Iterativa e Incremental: Modelo Espiral e RUP](#22-abordagem-iterativa-e-incremental-modelo-espiral-e-rup)
    3. [Abordagem Adaptativa / Ágil: O Manifesto Ágil de 2001](#23-abordagem-adaptativa-agil-o-manifesto-agil-de-2001)
    4. [Abordagens Híbridas de Desenvolvimento](#24-abordagens-hibridas-de-desenvolvimento)
    5. [Teste 002](#Teste-002)
    6. [Teste 003](#Teste-003)
    7. [Teste 004](#Teste-004)
3. [O Framework Scrum (Guia Scrum 2020)](#3-o-framework-scrum-guia-scrum-2020)
    1. [Pilares do Empirismo e Valores Fundamentais](#31-pilares-do-empirismo-e-valores-fundamentais)
    2. [Estrutura do Scrum Team e Responsabilidades](#32-estrutura-do-scrum-team-e-responsabilidades)
    3. [Eventos Formais do Scrum e Regras de Time-box](#33-eventos-formais-do-scrum-e-regras-de-time-box)
    4. [Artefatos Oficiais e seus Três Compromissos Formais](#34-artefatos-oficiais-e-seus-tres-compromissos-formais)
    5. [Métricas e Gráficos de Acompanhamento (Burndown e Burnup)](#35-metricas-e-graficos-de-acompanhamento-burndown-e-burnup)
    6. [Teste 005](#Teste-005)
    7. [Teste 006](#Teste-006)
    8. [Teste 007](#Teste-007)
    9. [Teste 008](#Teste-008)
4. [Método Kanban e Gestão do Fluxo de Valor](#4-metodo-kanban-e-gestao-do-fluxo-de-valor)
    1. [Princípios e Práticas Gerais do Kanban](#41-principios-e-praticas-gerais-do-kanban)
    2. [Limites de Trabalho em Progresso (WIP) e Gargalos](#42-limites-de-trabalho-em-progresso-wip-e-gargalos)
    3. [Métricas de Fluxo: Lead Time, Cycle Time, Throughput e CFD](#43-metricas-de-fluxo-lead-time-cycle-time-throughput-e-cfd)
    4. [Teste 009](#Teste-009)
    5. [Teste 010](#Teste-010)
5. [Extreme Programming (XP) e Lean Software Development](#5-extreme-programming-xp-e-lean-software-development)
    1. [Extreme Programming: Valores e Práticas de Engenharia](#51-extreme-programming-valores-e-praticas-de-engenharia)
    2. [Lean Software Development e Eliminação dos 7 Desperdícios](#52-lean-software-development-e-eliminacao-dos-7-desperdicios)
    3. [Teste 011](#Teste-011)
6. [Fontes Oficiais e Referências Bibliográficas](#6-fontes-oficiais-e-referencias-bibliograficas)

---

## 1. Fundamentos de Engenharia de Software e Processos

### 1.1 Escopo da Engenharia de Software e a Crise do Software
A Engenharia de Software é a disciplina de engenharia dedicada ao estabelecimento e uso de sólidos princípios e métodos sistemáticos, disciplinados e quantificáveis para o desenvolvimento, operação e manutenção de software de alta qualidade dentro de custos e prazos previsíveis.

- **A Crise do Software:** O termo emergiu formalmente na Conferência da OTAN (NATO Conference) em 1968, em Garmisch, motivado pela incapacidade sistemática da indústria de entregar sistemas confiáveis dentro do orçamento e cronograma. Os projetos sofriam rotineiramente com estouros orçamentários astronômicos, atrasos severos, código repleto de defeitos e sistemas que não atendiam às necessidades reais dos usuários.
- **Fatores da Complexidade do Software (Frederick Brooks - *No Silver Bullet*):** Brooks dividiu a complexidade em duas dimensões:
    - *Complexidade Essencial:* Intrínseca à natureza do software (conformidade legal mutável, invisibilidade, complexidade inerente ao domínio do negócio);
    - *Complexidade Acidental:* Relacionada às limitações transitórias da tecnologia utilizada (compiladores rudimentares, falta de ferramentas de integração ou linguagens de baixo nível). Não há "bala de prata" tecnológica capaz de quadruplicar a produtividade por si só.

### 1.2 Atividades Genéricas de Processo de Software
Independentemente do ciclo de vida adotado (preditivo, iterativo ou ágil), a literatura clássica de engenharia de software (Pressman e Sommerville) mapeia cinco atividades genéricas de processo:

1. **Comunicação:** Cooperação contínua e levantamento de requisitos junto a clientes e partes interessadas (*stakeholders*);
2. **Planejamento:** Estimativas de esforço, alocação de recursos, definição de entregáveis, cronograma e análise de riscos;
3. **Modelagem:** Elaboração de arquitetura de software, diagramação de modelos conceituais, fluxos de dados e especificações detalhadas de design;
4. **Construção:** Atividades conjugadas de codificação (programação) e testes automatizados/manuais de software;
5. **Implantação (Deployment):** Disponibilização do software em ambiente operacional, homologação pelo usuário final, suporte técnico e coleta de feedback.

### 1.3 Modelos de Maturidade de Processo (CMMI e MPS.BR)
- **CMMI (Capability Maturity Model Integration):** Desenvolvido pelo SEI (Software Engineering Institute), estrutura a capacidade e maturidade de organizações em 5 níveis escalonados:
    - *Nível 1 (Inicial):* Processos imprevisíveis, reativos e caóticos; o sucesso depende do esforço heróico individual;
    - *Nível 2 (Gerenciado):* Projetos planejados, medidos e controlados em nível de projeto;
    - *Nível 3 (Definido):* Processos corporativos padronizados e integrados em toda a organização;
    - *Nível 4 (Quantitativamente Gerenciado):* Processos controlados estatisticamente mediante métricas rigorosas de desempenho;
    - *Nível 5 (Em Otimização):* Foco na melhoria contínua e inovação sistemática de processos.
- **MPS.BR (Melhoria de Processo do Software Brasileiro):** Modelo nacional alinhado às normas ISO/IEC 12207 e 15504, subdividido em 7 níveis de maturidade decrescentes em letras (do nível G - Parcialmente Gerenciado até o nível A - Em Otimização).

---

### Teste 001
**(FGV – TJ/RR – 2024 – Analista Judiciario Gestao E Governanca De Tecnologia Da Informacao)**
Considerando a aplicação de metodologias ágeis a projetos de desenvolvimento de software, analise as seguintes afirmativas: I. Mais do que software em funcionamento, documentação abrangente é um dos valores propostos pelo manifesto ágil. II. A limitação do número de tarefas em execução, conhecida como WIP (Work In Progress), favorece um ritmo sustentável para a equipe de desenvolvimento sem impedir o fluxo de trabalho. III. O tempo transcorrido desde o momento em que uma tarefa entra em um quadro Kanban até ser finalizada é conhecido como lead time. Está correto o que se afirma em

* **A)** I, apenas.
* **B)** II, apenas.
* **C)** III, apenas.
* **D)** I e II, apenas.
* **E)** II e III, apenas.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I, apenas". De acordo com a teoria estudada em *2.3 Abordagem Adaptativa / Ágil: O Manifesto Ágil de 2001*, software em funcionamento: Documentação abrangente.
> - **B)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II, apenas". De acordo com a teoria estudada em *4.2 Limites de Trabalho em Progresso (WIP) e Gargalos*, limite de WIP (Work In Progress): Cada coluna do quadro possui um teto máximo de itens permitidos simultaneamente (ex.: a coluna "Testes" com WIP = 3).
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "III, apenas". De acordo com a teoria estudada em *6. Fontes Oficiais e Referências Bibliográficas*, o Guia Oficial do Kanban (Kanban Guides — Português do Brasil) Definição formal do método Kanban, práticas de limitação de WIP e métricas de fluxo (Lead Time, Cycle Time e Throughput).
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e II, apenas". De acordo com a teoria estudada em *4.3 Métricas de Fluxo: Lead Time, Cycle Time, Throughput e CFD*, diagrama de Fluxo Cumulativo (CFD Cumulative Flow Diagram): Gráfico de áreas empilhadas que ilustra o número cumulativo de itens em cada fase do processo ao longo do tempo.
> - **E)** **Correta.** Conforme fundamentado na seção *4.3 Métricas de Fluxo: Lead Time, Cycle Time, Throughput e CFD* deste guia, cycle Time: É o tempo em que a equipe técnica esteve ativamente trabalhando no desenvolvimento do item (desde que o cartão foi puxado para a primeira coluna de execução até a conclusão da tarefa). Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/RR/2024) ao estabelecer que "II e III, apenas".
>
> **Gabarito: E**

---



## 2. Modelos de Ciclo de Vida de Software

```mermaid
flowchart TD
    subgraph Preditivo["Abordagem Preditiva (Plano Dirigido)"]
        W1["Requisitos Congelados"] --> W2["Projeto / Arquitetura"]
        W2 --> W3["Implementação (Código)"]
        W3 --> W4["Testes de Aceitação"]
        W4 --> W5["Entrega Única Final"]
    end

    subgraph Adaptativo["Abordagem Adaptativa / Ágil"]
        A1["Visão do Produto"] --> A2["Ciclos Curtos / Iterações (1 a 4 semanas)"]
        A2 --> A3["Incremento Utilizável 'Pronto'"]
        A3 --> A4["Inspeção e Feedback do Usuário"]
        A4 -->|Adaptação e Repriorização| A2
    end
```

### 2.1 Abordagem Preditiva: Modelo Cascata (Waterfall) e Modelo V
- **Modelo Cascata (Royce, 1970):** Caracteriza-se por uma progressão linear, estritamente sequencial entre as fases do ciclo de vida. Uma fase subsequente somente é iniciada quando todos os artefatos da fase anterior estiverem totalmente concluídos, documentados e formalmente aprovados (*gates* de transição).
    - *Vantagens:* Estrutura rígida de fácil controle gerencial para projetos com requisitos absolutamente estáveis, bem compreendidos e sem previsão de mudanças tecnológicas.
    - *Desvantagens:* Inflexibilidade severa para absorver mudanças; o software só ganha forma executável nas fases finais do projeto, postergando a percepção de valor e a identificação de defeitos críticos para o encerramento do cronograma.
- **Modelo V (Verificação e Validação):** Variação direta do modelo cascata que explicita o pareamento simétrico entre cada fase de especificação/desenvolvimento e a sua correspondente fase de testes:
    - Requisitos de Negócio $\longleftrightarrow$ Testes de Aceitação;
    - Requisitos de Sistema $\longleftrightarrow$ Testes de Sistema;
    - Design Arquitetural $\longleftrightarrow$ Testes de Integração;
    - Design Detalhado de Módulos $\longleftrightarrow$ Testes Unitários.

### 2.2 Abordagem Iterativa e Incremental: Modelo Espiral e RUP
- **Conceito de Iteração vs. Incremento:**
    - *Iterativo:* O software é desenvolvido por meio de repetições sucessivas de ciclos de desenvolvimento, refinando progressivamente a solução.
    - *Incremental:* A cada ciclo concluído, uma porção utilizável e funcional do software é acrescida à versão anterior.
- **Modelo Espiral (Barry Boehm, 1988):** Modelo orientado a riscos (*risk-driven*), no qual o desenvolvimento progride em ciclos espirais contínuos compostos por quatro quadrantes obrigatórios:
    1. *Determinação de objetivos, alternativas e restrições;*
    2. *Identificação e resolução de riscos* (análise de risco, prototipação e simulações);
    3. *Desenvolvimento e validação do produto do nível atual;*
    4. *Planejamento da próxima fase.*

- **Processo Unificado (RUP - Rational Unified Process):** Metodologia iterativa e incremental orientada por Casos de Uso e centrada na Arquitetura de Software. Estrutura-se em quatro fases temporais sequenciais:
    1. *Iniciação (Inception):* Estabelecimento do escopo de negócio e viabilidade;
    2. *Elaboração (Elaboration):* Mapeamento profundo dos requisitos, mitigação de riscos maiores e estabilização da arquitetura executável básica;
    3. *Construção (Construction):* Desenvolvimento em larga escala e codificação de todos os componentes;
    4. *Transição (Transition):* Implantação, homologação, treinamento dos usuários e passagem para operação.

> 🚨 **ALERTA DE PROVA / PEGADINHA FCC:** A característica mais cobrada pela FCC a respeito do Modelo Espiral de Boehm é a **gestão explícita e sistemática de riscos** (*risk analysis*) em cada espira. Se a questão mencionar "modelo direcionado pela mitigação contínua de riscos através de prototipação em cada volta do ciclo", marque com segurança o **Modelo Espiral**.

### 2.3 Abordagem Adaptativa / Ágil: O Manifesto Ágil de 2001
Em fevereiro de 2001, em Snowbird (Utah), dezessete líderes de desenvolvimento de software redigiram o **Manifesto para o Desenvolvimento Ágil de Software**, fundamentado em 4 Valores e 12 Princípios:

| Nós valorizamos mais: | Do que: |
| :--- | :--- |
| **Indivíduos e interações** | Processos e ferramentas |
| **Software em funcionamento** | Documentação abrangente |
| **Colaboração com o cliente** | Negociação de contratos |
| **Responder a mudanças** | Seguir um plano pré-estabelecido |

*A premissa não é eliminar processos, documentação, contratos ou planos, mas reconhecer que os itens à esquerda entregam valor direto superior e adaptabilidade num ambiente de incerteza.*

### 2.4 Abordagens Híbridas de Desenvolvimento
Reconhecem que o mundo corporativo raramente opera em extremos absolutos. Um projeto híbrido pode adotar:

- Abordagem preditiva no planejamento macro de escopo, contratação pública e cronograma de alto nível (governança tradicional);
- Abordagem adaptativa/ágil na execução das iterações técnicas pelas equipes de desenvolvimento (com Sprints Scrum, gestão visual Kanban e testes contínuos).

---

## 3. O Framework Scrum (Guia Scrum 2020)

```mermaid
graph LR
    PB["Product Backlog<br/>(Compromisso: Meta do Produto)"] --> SP["Sprint Planning"]
    SP --> SB["Sprint Backlog<br/>(Compromisso: Meta da Sprint)"]
    SB --> DS["Daily Scrum (15 min)"]
    DS --> INC["Incremento Utilizável<br/>(Compromisso: Definição de Pronto - DoD)"]
    INC --> SR["Sprint Review (Inspeção do Produto)"]
    SR --> RET["Sprint Retrospective (Melhoria Contínua)"]
    RET --> PB
```

### 3.1 Pilares do Empirismo e Valores Fundamentais
O Scrum é um framework leve que ajuda pessoas, times e organizações a gerar valor por meio de soluções adaptativas para problemas complexos. Alicerça-se no **Empirismo** e no pensamento **Lean**:

- **Três Pilares Empíricos:**
    1. *Transparência:* Processos e artefatos devem ser visíveis para todos os responsáveis pelos resultados;
    2. *Inspeção:* O progresso rumo aos objetivos deve ser examinado com frequência diligente para identificar anomalias;
    3. *Adaptação:* Havendo desvios inaceitáveis, os ajustes operacionais devem ser implementados no menor tempo viável.

- **Cinco Valores do Scrum:** Compromisso (*Commitment*), Foco (*Focus*), Abertura (*Openness*), Respeito (*Respect*) e Coragem (*Courage*).

### 3.2 Estrutura do Scrum Team e Responsabilidades
No Guia Scrum oficial de 2020, o **Scrum Team** é a unidade fundamental de trabalho, caracterizado por ser **multifuncional** (possui todas as habilidades necessárias para entregar o incremento) e **autogerenciado** (*self-managing* - a equipe decide internamente *quem*, *o que* e *como* fazer). O time compõe-se de três papéis/responsabilidades:

1. **Product Owner (PO):**
    - Responsável por **maximizar o valor do produto** resultante do trabalho do time;
    - Única pessoa responsável pela gestão eficaz do **Product Backlog** (criação, ordenação, clareza e comunicação dos itens de backlog);
    - Representa os interesses dos stakeholders; suas decisões devem ser respeitadas por toda a organização.

2. **Scrum Master (SM):**
    - Responsável por promover e apoiar o Scrum conforme definido no Guia;
    - Atua como um **líder que serve** (*true leader who serves*);
    - Remove impedimentos externos que bloqueiam o avanço dos Desenvolvedores;
    - Facilita os eventos do Scrum e garante a eficácia e a melhoria dos processos do time.

3. **Desenvolvedores (Developers):**
    - Pessoas do Scrum Team comprometidas em criar qualquer aspecto de um **Incremento utilizável a cada Sprint**;
    - Criam o plano para a Sprint (Sprint Backlog);
    - Adaptam o plano diariamente na Daily Scrum e responsabilizam-se pela qualidade aplicando a Definição de Pronto (*DoD*).

> 🚨 **ALERTA DE PROVA / PEGADINHA FCC:**  
>
> 1. No Guia 2020 **NÃO existe mais o papel "Time de Desenvolvimento" (Development Team)**. Existe apenas o *Scrum Team*, formado por PO, Scrum Master e Desenvolvedores. Não há subtimes nem hierarquias internas!  
> 2. O Scrum Master **NÃO é um gerente funcional**, não distribui tarefas individualmente e não cobra relatórios de horas.

### 3.3 Eventos Formais do Scrum e Regras de Time-box
Todos os eventos no Scrum possuem duração máxima pré-fixada (**time-box**):

| Evento Scrum | Finalidade Central e Participantes | Duração Máxima (Sprint de 1 mês) |
| :--- | :--- | :--- |
| **A Sprint** | Contêiner maior para todos os demais eventos. É o ciclo no qual o trabalho é executado para criar o incremento. | Até **um (1) mês** de duração fixa. |
| **Sprint Planning** | Define o plano de trabalho da Sprint abordando: 1) *Por que a Sprint é valiosa?* 2) *O que pode ser feito?* 3) *Como o trabalho será realizado?* | Máximo de **8 horas**. |
| **Daily Scrum** | Evento de alinhamento diário exclusivo dos **Desenvolvedores** para inspecionar o progresso rumo à Meta da Sprint e adaptar o plano para as próximas 24h. | Exatamente **15 minutos** (fixo, independentemente do tamanho da Sprint). |
| **Sprint Review** | Inspeção do Incremento produzido com os *stakeholders* para adaptar o Product Backlog com base no feedback real. | Máximo de **4 horas**. |
| **Sprint Retrospective** | Planejamento de melhorias na eficácia do time (pessoas, processos, ferramentas e Definição de Pronto). | Máximo de **3 horas**. |

> ⭐ **IMPORTANTE / REGRAS DA SPRINT:** Uma Sprint **nunca é prorrogada**. Se os itens planejados não forem concluídos dentro do time-box, a Sprint encerra-se normalmente; os itens não finalizados voltam para o Product Backlog. Uma Sprint só pode ser **cancelada prematuramente pelo Product Owner**, caso a Meta da Sprint (*Sprint Goal*) se torne obsoleta!

### 3.4 Artefatos Oficiais e seus Três Compromissos Formais
Cada um dos três artefatos do Scrum contém um **compromisso formal** associado (introduzido formalmente no Guia 2020) para fornecer transparência e foco:

1. **Product Backlog** $\longrightarrow$ Compromisso: **Meta do Produto (*Product Goal*)**  
    - O Product Backlog é a lista ordenada e emergente de tudo o que é necessário para melhorar o produto. A Meta do Produto descreve o estado futuro que serve como alvo de longo prazo para o Scrum Team.

2. **Sprint Backlog** $\longrightarrow$ Compromisso: **Meta da Sprint (*Sprint Goal*)**  
    - O Sprint Backlog é composto pela Meta da Sprint (o porquê), o conjunto de itens selecionados do Product Backlog (o quê) e o plano de ação detalhado (o como). A Meta da Sprint é o objetivo único acordado para a iteração, que não muda durante a sua execução.

3. **Incremento** $\longrightarrow$ Compromisso: **Definição de Pronto (*Definition of Done - DoD*)**  
    - O Incremento é um degrau concreto rumo à Meta do Produto. No momento em que um item do Product Backlog atende à Definição de Pronto, um novo Incremento nasce. A DoD é a descrição formal dos critérios de qualidade exigidos para que o item seja considerado pronto para uso.

### 3.5 Métricas e Gráficos de Acompanhamento (Burndown e Burnup)
- **Sprint Burndown Chart:** Gráfico que exibe a quantidade de **trabalho restante** (geralmente em pontos de história ou horas) em relação ao tempo da Sprint. A inclinação da linha decrescente indica se a equipe concluirá as tarefas no prazo;
- **Burnup Chart:** Gráfico com duas linhas: uma demonstrando o crescimento do escopo total ao longo do tempo e outra demonstrando o trabalho efetivamente concluído (*done*). Excelente para detectar expansão de escopo (*scope creep*).

---

### Teste 002
**(FGV – TCE/GO – 2024 – Analista de Controle Externo - Tecnologia da Informação)**
Avalie as seguintes afirmativas no contexto de práticas e metodologias de deploy em desenvolvimento mobile: I. A aplicação de Continuous Integration (CI) em aplicativos mobile responsivos é uma prática que visa a fusão e teste do código apenas ao final de cada sprint; II. Continuous Delivery (CD) é parte da filosofia "Mobile First" e permite que toda mudança de código seja automaticamente disponibilizada para os usuários finais, sem a necessidade de aprovação das equipes de operações; III. DevSecOps é a integração da segurança no processo de desenvolvimento de software desde o início sem comprometer a velocidade de entrega. Está correto o que se afirma em

* **A)** I, apenas.
* **B)** II e III, apenas.
* **C)** III, apenas.
* **D)** I, II e III.
* **E)** I e II, apenas. Redes de Computadores e Sistemas Operacionais Redes de Computadores

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I, apenas". De acordo com a teoria estudada em *6. Fontes Oficiais e Referências Bibliográficas*, continuous Integration (Martin Fowler — Práticas de Engenharia Ágil e XP) Fundamentos de integração contínua, automação de builds e práticas técnicas do Extreme Programming (XP).
> - **B)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II e III, apenas". De acordo com a teoria estudada em *5.2 Lean Software Development e Eliminação dos 7 Desperdícios*, 1. Trabalho Parcialmente Feito: Código desenvolvido que permanece semanas em branch aguardando testes ou aprovação de deploy.
> - **C)** **Correta.** Conforme fundamentado na seção *5.1 Extreme Programming: Valores e Práticas de Engenharia* deste guia, integração Contínua ( Continuous Integration ): Código integrado e testado no repositório compartilhado várias vezes ao dia. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/GO/2024) ao estabelecer que "III, apenas".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I, II e III". De acordo com a teoria estudada em *1.1 Escopo da Engenharia de Software e a Crise do Software*, a Crise do Software: O termo emergiu formalmente na Conferência da OTAN (NATO Conference) em 1968, em Garmisch, motivado pela incapacidade sistemática da indústria de entregar sistemas confiáveis dentro do orçamento e cronograma. Os projetos sofriam rotineiramente com estouros orçamentários astronômicos, atrasos severos, código repleto de defeitos e sistemas que não atendiam às necessidades reais dos usuários.
> - **E)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e II, apenas. Redes de Computadores e Sistemas Operacionais Redes de Computadores". De acordo com a teoria estudada em *5.2 Lean Software Development e Eliminação dos 7 Desperdícios*, desperdício no Lean Software: Manifestação Prática no Desenvolvimento de Sistemas.
>
> **Gabarito: C**

---


### Teste 003
**(CEBRASPE – TRF 6ª – 2025 – Analista Judiciário - Apoio Especializado - Governança e Gestão de Tecnologia da Informação)**
Na teoria do Scrum, o Lean Thinking é uma abordagem em que o conhecimento aplicado aos projetos e a tomada de decisão são oriundos da experiência das equipes.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Incorreta.** A proposição apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Na teoria do Scrum, o Lean Thinking é uma abordagem em que o conhecimento aplicado aos projetos e a tomada de...". De acordo com a teoria em *2.4 Abordagens Híbridas de Desenvolvimento*, abordagem adaptativa/ágil na execução das iterações técnicas pelas equipes de desenvolvimento (com Sprints Scrum, gestão visual Kanban e testes contínuos).
> - **E)** **Correta.** O item está **Errado** (gabarito oficial: **E**), pois contraria a disciplina teórica aplicável.
>
> **Gabarito: E**

---


### Teste 004
**(CEBRASPE – TRF 6ª – 2025 – Analista Judiciário - Apoio Especializado - Governança e Gestão de Tecnologia da Informação)**
O Scrum diário, ou daily standup, é uma reunião de equipe de projeto, na qual é feita uma análise do progresso do dia anterior e são definidas ações para o dia em que ocorre referida reunião. Em relação aos modelos e às referências de governança da tecnologia da informação, julgue os seguintes itens.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Correta.** O item está **Certo**. Conforme fundamentado na seção *3.3 Eventos Formais do Scrum e Regras de Time-box*, daily Scrum: Evento de alinhamento diário exclusivo dos Desenvolvedores para inspecionar o progresso rumo à Meta da Sprint e adaptar o plano para as próximas 24h. — Exatamente 15 minutos (fixo, independentemente do tamanho da Sprint). Dessa forma, está plenamente correta a assertiva da banca (CEBRASPE – TRF 6ª/2025) ao afirmar que "O Scrum diário, ou daily standup, é uma reunião de equipe de projeto, na qual é feita uma análise do...".
> - **E)** **Incorreta.** A assertiva não incorre em erro conceitual, guardando conformidade com a teoria estudada.
>
> **Gabarito: C**

---


### Teste 005
**(FGV – TJ/AP – 2023 – Analista Judiciario Apoio Especializado Tecnologia Da Informacao Seguranca Da Informacao)**
A metodologia Scrum é um framework que apoia o desenvolvimento de soluções adaptativas para problemas complexos utilizando diversos artefatos. O artefato do Scrum composto pela Meta da Sprint (por que), o conjunto de itens do Product Backlog selecionados para a Sprint (o que), bem como um plano de ação para entregar o Incremento (como) é o:

* **A)** kanban;
* **B)** incremento;
* **C)** sprint backlog;
* **D)** product owner;
* **E)** meta do produto.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "kanban". De acordo com a teoria estudada em *3. O Framework Scrum (Guia Scrum 2020)*, pB["Product Backlog<br/ (Compromisso: Meta do Produto)"] SP["Sprint Planning"].
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "incremento". De acordo com a teoria estudada em *3.3 Eventos Formais do Scrum e Regras de Time-box*, sprint Review: Inspeção do Incremento produzido com os stakeholders para adaptar o Product Backlog com base no feedback real. — Máximo de 4 horas.
> - **C)** **Correta.** Conforme fundamentado na seção *3.4 Artefatos Oficiais e seus Três Compromissos Formais* deste guia, o Sprint Backlog é composto pela Meta da Sprint (o porquê), o conjunto de itens selecionados do Product Backlog (o quê) e o plano de ação detalhado (o como). A Meta da Sprint é o objetivo único acordado para a iteração, que não muda durante a sua execução. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/AP/2023) ao estabelecer que "sprint backlog".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "product owner". De acordo com a teoria estudada em *3.3 Eventos Formais do Scrum e Regras de Time-box*, uma Sprint nunca é prorrogada. Se os itens planejados não forem concluídos dentro do time box, a Sprint encerra se normalmente; os itens não finalizados voltam para o Product Backlog. Uma Sprint só pode ser cancelada prematuramente pelo Product Owner, caso a Meta da Sprint ( Sprint Goal ) se torne obsoleta!.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "meta do produto". De acordo com a teoria estudada em *3.4 Artefatos Oficiais e seus Três Compromissos Formais*, o Incremento é um degrau concreto rumo à Meta do Produto. No momento em que um item do Product Backlog atende à Definição de Pronto, um novo Incremento nasce. A DoD é a descrição formal dos critérios de qualidade exigidos para que o item seja considerado pronto para uso.
>
> **Gabarito: C**

---


### Teste 006
**(FCC – TRT 14ª – 2016 – Analista Judiciário - Apoio Especializado - Tecnologia da Informação)**
Um aspecto comum entre o desenvolvimento baseado no UP e no Scrum é que ambos

* **A)** estão sendo representados os 3 processos básicos da metodologia FDD.
* **B)** os testes estão sendo realizados com o JUnit e o Netbeans.
* **C)** são etapas do FDD, que tem em comum com o XP o fato de que o desenvolvedor é o único responsável pelo código que ele desenvolve.
* **D)** refatorar é uma prática comum em XP e também utilizada no TDD.
* **E)** estas etapas são utilizadas quando se deseja assegurar que um código sempre lance uma exceção.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "estão sendo representados os 3 processos básicos da metodologia FDD". De acordo com a teoria estudada em *5.1 Extreme Programming: Valores e Práticas de Engenharia*, criado por Kent Beck, o Extreme Programming (XP) é uma metodologia ágil voltada à excelência técnica e engenharia de software para times pequenos e médios submetidos a requisitos vagos e altamente dinâmicos.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "os testes estão sendo realizados com o JUnit e o Netbeans". De acordo com a teoria estudada em *5.1 Extreme Programming: Valores e Práticas de Engenharia*, refactor: Limpar e aprimorar o código fonte (eliminando duplicações), garantindo que todos os testes continuem passando.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "são etapas do FDD, que tem em comum com o XP o fato de que o desenvolvedor é o único responsável pelo código que...". De acordo com a teoria estudada em *5.1 Extreme Programming: Valores e Práticas de Engenharia*, propriedade Coletiva do Código ( Collective Ownership ): Qualquer desenvolvedor do time tem liberdade e responsabilidade para alterar qualquer módulo do sistema para corrigir defeitos ou implementar melhorias.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "refatorar é uma prática comum em XP e também utilizada no TDD". De acordo com a teoria estudada em *5.1 Extreme Programming: Valores e Práticas de Engenharia*, test Driven Development (TDD): Desenvolvimento guiado por testes mediante o ciclo contínuo Red Green Refactor.
> - **E)** **Correta.** Conforme fundamentado na seção *5.2 Lean Software Development e Eliminação dos 7 Desperdícios* deste guia, 2. Recursos Extras (Gold Plating): Funcionalidades desenvolvidas que nunca serão utilizadas pelo usuário final (excesso de especificação). Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 14ª/2016) ao estabelecer que "estas etapas são utilizadas quando se deseja assegurar que um código sempre lance uma exceção".
>
> **Gabarito: E**

---


### Teste 007
**(FCC – TRT 6ª – 2012 – Analista Judiciário - Apoio Especializado/Tecnologia da Informação)**
Na metodologia Scrum, NÃO faz parte de uma revisão do sprint (sprint review) o seguinte procedimento:

* **A)** Todo o time colabora no que deve ser feito em seguida, de modo que esta revisão contribua para reuniões de planejamento subsequentes.
* **B)** O proprietário do produto identifica o que está pronto e o que ainda está por fazer.
* **C)** O time de desenvolvimento discute quais fatores positivos e negativos ocorreram durante o sprint e como os problemas foram resolvidos.
* **D)** O time de desenvolvimento apresenta o trabalho que foi desenvolvido e responde questões sobre o incremento.
* **E)** Todo o time cria um plano para implementar melhorias no modo como o time efetua seu trabalho.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *3.3 Eventos Formais do Scrum e Regras de Time-box* deste guia, sprint Planning: Define o plano de trabalho da Sprint abordando: 1) Por que a Sprint é valiosa? 2) O que pode ser feito? 3) Como o trabalho será realizado? — Máximo de 8 horas. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 6ª/2012) ao estabelecer que "Todo o time colabora no que deve ser feito em seguida, de modo que esta revisão contribua para reuniões de...".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O proprietário do produto identifica o que está pronto e o que ainda está por fazer". De acordo com a teoria estudada em *3.3 Eventos Formais do Scrum e Regras de Time-box*, sprint Retrospective: Planejamento de melhorias na eficácia do time (pessoas, processos, ferramentas e Definição de Pronto). — Máximo de 3 horas.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O time de desenvolvimento discute quais fatores positivos e negativos ocorreram durante o sprint e como os...". De acordo com a teoria estudada em *3.3 Eventos Formais do Scrum e Regras de Time-box*, uma Sprint nunca é prorrogada. Se os itens planejados não forem concluídos dentro do time box, a Sprint encerra se normalmente; os itens não finalizados voltam para o Product Backlog. Uma Sprint só pode ser cancelada prematuramente pelo Product Owner, caso a Meta da Sprint ( Sprint Goal ) se torne obsoleta!.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O time de desenvolvimento apresenta o trabalho que foi desenvolvido e responde questões sobre o incremento". De acordo com a teoria estudada em *3.2 Estrutura do Scrum Team e Responsabilidades*, no Guia Scrum oficial de 2020, o Scrum Team é a unidade fundamental de trabalho, caracterizado por ser multifuncional (possui todas as habilidades necessárias para entregar o incremento) e autogerenciado ( self managing a equipe decide internamente quem , o que e como fazer). O time compõe se de três papéis/responsabilidades.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Todo o time cria um plano para implementar melhorias no modo como o time efetua seu trabalho". De acordo com a teoria estudada em *5.1 Extreme Programming: Valores e Práticas de Engenharia*, propriedade Coletiva do Código ( Collective Ownership ): Qualquer desenvolvedor do time tem liberdade e responsabilidade para alterar qualquer módulo do sistema para corrigir defeitos ou implementar melhorias.
>
> **Gabarito: A**

---


### Teste 008
**(FGV – TRF/1 – 2024 – Analista Judiciario Area Apoio Especializado Especialidade Suporte Em Tecnologia Da Informacao)**
A analista Paula foi designada como responsável por um projeto com as seguintes características: inovação, alto grau de incerteza, não ter sido realizado nenhum outro similar em seu órgão e provavelmente passar por muitas mudanças durante o processo. Considerando essas características do projeto, Paula decidiu pela abordagem ágil usando o framework Scrum. A atividade empregada pelo framework Scrum que Paula deve utilizar, para tratar a alta incerteza do projeto, é:

* **A)** realização de sprints;
* **B)** manutenção da declaração de escopo;
* **C)** confecção de documentação abrangente;
* **D)** revisões periódicas de processos e ferramentas;
* **E)** acompanhamento permanente da equipe de desenvolvimento.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *2.4 Abordagens Híbridas de Desenvolvimento* deste guia, abordagem adaptativa/ágil na execução das iterações técnicas pelas equipes de desenvolvimento (com Sprints Scrum, gestão visual Kanban e testes contínuos). Dessa forma, está plenamente correta a assertiva da banca (FGV – TRF/1/2024) ao estabelecer que "realização de sprints".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "manutenção da declaração de escopo". De acordo com a teoria estudada em *1.1 Escopo da Engenharia de Software e a Crise do Software*, a Engenharia de Software é a disciplina de engenharia dedicada ao estabelecimento e uso de sólidos princípios e métodos sistemáticos, disciplinados e quantificáveis para o desenvolvimento, operação e manutenção de software de alta qualidade dentro de custos e prazos previsíveis.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "confecção de documentação abrangente". De acordo com a teoria estudada em *2.3 Abordagem Adaptativa / Ágil: O Manifesto Ágil de 2001*, software em funcionamento: Documentação abrangente.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "revisões periódicas de processos e ferramentas". De acordo com a teoria estudada em *2.3 Abordagem Adaptativa / Ágil: O Manifesto Ágil de 2001*, indivíduos e interações: Processos e ferramentas.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "acompanhamento permanente da equipe de desenvolvimento". De acordo com a teoria estudada em *3.5 Métricas e Gráficos de Acompanhamento (Burndown e Burnup)*, sprint Burndown Chart: Gráfico que exibe a quantidade de trabalho restante (geralmente em pontos de história ou horas) em relação ao tempo da Sprint. A inclinação da linha decrescente indica se a equipe concluirá as tarefas no prazo.
>
> **Gabarito: A**

---


### Teste 009
**(FGV – TJ/RR – 2024 – Analista Judiciario Gestao E Governanca De Tecnologia Da Informacao)**
Em relação às características do time Scrum, analise as afirmativas a seguir. I. O time Scrum é um pequeno grupo de pessoas em que o dono do produto é o superior hierárquico do Scrum Master e dos desenvolvedores. II. O Scrum Master é o responsável pela efetividade do time Scrum, permitindo que o time melhore suas práticas dentro do framework Scrum. III. Os desenvolvedores são as pessoas comprometidas a criar qualquer aspecto de um incremento utilizável em cada Sprint. Está correto o que se afirma em

* **A)** I, apenas.
* **B)** II, apenas.
* **C)** III, apenas.
* **D)** I e II, apenas.
* **E)** II e III, apenas.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I, apenas". De acordo com a teoria estudada em *3.3 Eventos Formais do Scrum e Regras de Time-box*, a Sprint: Contêiner maior para todos os demais eventos. É o ciclo no qual o trabalho é executado para criar o incremento. — Até um (1) mês de duração fixa.
> - **B)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II, apenas". De acordo com a teoria estudada em *3. O Framework Scrum (Guia Scrum 2020)*, dS INC["Incremento Utilizável<br/ (Compromisso: Definição de Pronto DoD)"].
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "III, apenas". De acordo com a teoria estudada em *3.2 Estrutura do Scrum Team e Responsabilidades*, no Guia 2020 NÃO existe mais o papel "Time de Desenvolvimento" (Development Team). Existe apenas o Scrum Team , formado por PO, Scrum Master e Desenvolvedores. Não há subtimes nem hierarquias internas!.
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e II, apenas". De acordo com a teoria estudada em *3.2 Estrutura do Scrum Team e Responsabilidades*, responsável por maximizar o valor do produto resultante do trabalho do time.
> - **E)** **Correta.** Conforme fundamentado na seção *3.2 Estrutura do Scrum Team e Responsabilidades* deste guia, pessoas do Scrum Team comprometidas em criar qualquer aspecto de um Incremento utilizável a cada Sprint. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/RR/2024) ao estabelecer que "II e III, apenas".
>
> **Gabarito: E**

---


### Teste 010
**(FGV – TJ/RR – 2024 – Analista Judiciario Gestao E Governanca De Tecnologia Da Informacao)**
Em relação aos eventos e aos artefatos do framework Scrum, analise as afirmativas a seguir. I. O backlog do produto é um documento preenchido antes do início do projeto e que não sofre alterações mesmo que os desejos do cliente mudem ao longo do tempo. II. A reunião diária, daily Scrum, é um evento de curta duração que permite identificar impedimentos, melhorar as comunicações, promover rápida tomada de decisões e reduzir a necessidade de outras reuniões ao longo do dia. III. A reunião de revisão da Sprint é um evento em que são definidas as histórias de usuário que serão trabalhadas naquela Sprint. Está correto o que se afirma em

* **A)** I, apenas.
* **B)** II, apenas.
* **C)** III, apenas.
* **D)** I e II, apenas.
* **E)** II e III, apenas.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I, apenas". De acordo com a teoria estudada em *3.3 Eventos Formais do Scrum e Regras de Time-box*, daily Scrum: Evento de alinhamento diário exclusivo dos Desenvolvedores para inspecionar o progresso rumo à Meta da Sprint e adaptar o plano para as próximas 24h. — Exatamente 15 minutos (fixo, independentemente do tamanho da Sprint).
> - **B)** **Correta.** Conforme fundamentado na seção *3.4 Artefatos Oficiais e seus Três Compromissos Formais* deste guia, o Product Backlog é a lista ordenada e emergente de tudo o que é necessário para melhorar o produto. A Meta do Produto descreve o estado futuro que serve como alvo de longo prazo para o Scrum Team. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/RR/2024) ao estabelecer que "II, apenas".
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "III, apenas". De acordo com a teoria estudada em *3.3 Eventos Formais do Scrum e Regras de Time-box*, evento Scrum: Finalidade Central e Participantes — Duração Máxima (Sprint de 1 mês).
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e II, apenas". De acordo com a teoria estudada em *3. O Framework Scrum (Guia Scrum 2020)*, pB["Product Backlog<br/ (Compromisso: Meta do Produto)"] SP["Sprint Planning"].
> - **E)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II e III, apenas". De acordo com a teoria estudada em *3.3 Eventos Formais do Scrum e Regras de Time-box*, a Sprint: Contêiner maior para todos os demais eventos. É o ciclo no qual o trabalho é executado para criar o incremento. — Até um (1) mês de duração fixa.
>
> **Gabarito: B**

---


### Teste 011
**(FGV – TRT/13 – 2022 – Analista Judiciario Tecnologia Da Informacao)**
Relacione os tipos de Sprint do SCRUM com as definições dos seus objetivos. 1. Inspecionar o progresso em direção ao Sprint Goal e adaptar o Sprint Backlog conforme necessário, ajustando o próximo trabalho planejado, é um evento de até 15 minutos para os desenvolvedores. 2. Estabelecer o trabalho a ser executado no Sprint. O plano resultante é criado pelo trabalho colaborativo de todo o time. 3. Planejar maneiras de aumentar a qualidade e a eficácia. 4. Inspecionar o resultado do Sprint e determinar futuras adaptações. O time apresenta os resultados do seu trabalho para as principais partes interessadas, sendo discutido o progresso em direção ao Produto. ( ) Sprint de Planejamento ( ) Sprint de Retrospectiva ( ) Reunião Diária ( ) Sprint de Revisão Assinale a opção que indica a relação correta, na ordem apresentada.

* **A)** 1 – 2 – 4 – 3.
* **B)** 1 – 3 – 2 – 1.
* **C)** 2 – 3 – 1 – 4.
* **D)** 3 – 4 – 1 – 2.
* **E)** 4 – 1 – 3 – 2.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "1 – 2 – 4 – 3". De acordo com a teoria estudada em *3.3 Eventos Formais do Scrum e Regras de Time-box*, uma Sprint nunca é prorrogada. Se os itens planejados não forem concluídos dentro do time box, a Sprint encerra se normalmente; os itens não finalizados voltam para o Product Backlog. Uma Sprint só pode ser cancelada prematuramente pelo Product Owner, caso a Meta da Sprint ( Sprint Goal ) se torne obsoleta!.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "1 – 3 – 2 – 1". De acordo com a teoria estudada em *3.5 Métricas e Gráficos de Acompanhamento (Burndown e Burnup)*, sprint Burndown Chart: Gráfico que exibe a quantidade de trabalho restante (geralmente em pontos de história ou horas) em relação ao tempo da Sprint. A inclinação da linha decrescente indica se a equipe concluirá as tarefas no prazo.
> - **C)** **Correta.** Conforme fundamentado na seção *3.3 Eventos Formais do Scrum e Regras de Time-box* deste guia, daily Scrum: Evento de alinhamento diário exclusivo dos Desenvolvedores para inspecionar o progresso rumo à Meta da Sprint e adaptar o plano para as próximas 24h. — Exatamente 15 minutos (fixo, independentemente do tamanho da Sprint). Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT/13/2022) ao estabelecer que "2 – 3 – 1 – 4".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "3 – 4 – 1 – 2". De acordo com a teoria estudada em *3.3 Eventos Formais do Scrum e Regras de Time-box*, sprint Planning: Define o plano de trabalho da Sprint abordando: 1) Por que a Sprint é valiosa? 2) O que pode ser feito? 3) Como o trabalho será realizado? — Máximo de 8 horas.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "4 – 1 – 3 – 2". De acordo com a teoria estudada em *3.3 Eventos Formais do Scrum e Regras de Time-box*, sprint Retrospective: Planejamento de melhorias na eficácia do time (pessoas, processos, ferramentas e Definição de Pronto). — Máximo de 3 horas.
>
> **Gabarito: C**

---


### Teste 012
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Administração)**
Carolina é analista de controle externo de um Tribunal de Contas estadual. Em determinada semana, ela se depara com as seguintes demandas simultâneas: I. elaborar, até o fim do dia, o relatório de instrução de um processo com prazo regimental vencendo às 18h, sob pena de nulidade da autuação; II. responder a e-mails de colegas solicitando informações sobre procedimentos administrativos de rotina, sem prazo definido; III. desenvolver um plano de capacitação para a equipe, atividade estratégica alinhada ao planejamento anual do tribunal, sem data de entrega imediata; e IV. participar de uma reunião convocada com urgência por outro setor para discutir a pauta da confraternização de fim de ano. Para organizar essas demandas, Carolina as classifica segundo dois critérios (importância e urgência), identificando quais devem ser executadas imediatamente, quais devem ser agendadas, quais devem ser delegadas e quais devem ser eliminadas ou postergadas. Nesse caso, Carolina utiliza a seguinte técnica de gestão de tarefas:

* **A)** Método GTD (Getting Things Done).
* **B)** Técnica Pomodoro.
* **C)** Método Kanban.
* **D)** Matriz de Eisenhower.
* **E)** Método OKR (Objectives and Key Results).

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Método GTD (Getting Things Done)". De acordo com a teoria estudada em *4.1 Princípios e Práticas Gerais do Kanban*, concebido por David J. Anderson com base no Sistema Toyota de Produção, o método Kanban é uma abordagem evolucionária e não prescritiva para gestão de fluxos de trabalho do conhecimento.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Técnica Pomodoro". De acordo com a teoria estudada em *4.3 Métricas de Fluxo: Lead Time, Cycle Time, Throughput e CFD*, cycle Time: É o tempo em que a equipe técnica esteve ativamente trabalhando no desenvolvimento do item (desde que o cartão foi puxado para a primeira coluna de execução até a conclusão da tarefa).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Método Kanban". De acordo com a teoria estudada em *6. Fontes Oficiais e Referências Bibliográficas*, o Guia Oficial do Kanban (Kanban Guides — Português do Brasil) Definição formal do método Kanban, práticas de limitação de WIP e métricas de fluxo (Lead Time, Cycle Time e Throughput).
> - **D)** **Correta.** Conforme fundamentado na seção *3.5 Métricas e Gráficos de Acompanhamento (Burndown e Burnup)* deste guia, sprint Burndown Chart: Gráfico que exibe a quantidade de trabalho restante (geralmente em pontos de história ou horas) em relação ao tempo da Sprint. A inclinação da linha decrescente indica se a equipe concluirá as tarefas no prazo. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "Matriz de Eisenhower".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Método OKR (Objectives and Key Results)". De acordo com a teoria estudada em *6. Fontes Oficiais e Referências Bibliográficas*, bECK, Kent; ANDRES, Cynthia. Extreme Programming Explained: Embrace Change. 2. ed. Boston: Addison Wesley Professional, 2004. (Sec. 1 Values, Principles, and Practices).
>
> **Gabarito: D**

---


### Teste 013
**(FGV – TRT/DA – 2025 – Tecnico Judiciario Area Administrativa Sem Especialidade)**
Toda a literatura neoclássica se assenta no processo administrativo para explicar como as várias funções administrativas são desenvolvidas nas organizações. Assinale a opção que apresenta, corretamente, a função do planejamento.

* **A)** O planejamento é orientado apenas para a alocação de recursos, sem considerar as prioridades ou o desempenho voltado para metas.
* **B)** O foco do planejamento é garantir que todas as atividades sejam realizadas, sem priorizar metas ou resultados específicos.
* **C)** A flexibilidade no planejamento implica em manter todos os processos rigidamente definidos, sem possibilidade de ajustes ou adaptações durante a execução.
* **D)** O planejamento orientado para mudanças permite antecipar problemas e aproveitar oportunidades, ajudando a organização a operar de forma ágil e dinâmica.
* **E)** O planejamento só é útil para organizações de grande porte, não beneficiando pequenas ou médias empresas.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "O planejamento é orientado apenas para a alocação de recursos, sem considerar as prioridades ou o desempenho...". De acordo com a teoria estudada em *1.2 Atividades Genéricas de Processo de Software*, planejamento: Estimativas de esforço, alocação de recursos, definição de entregáveis, cronograma e análise de riscos.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O foco do planejamento é garantir que todas as atividades sejam realizadas, sem priorizar metas ou resultados...". De acordo com a teoria estudada em *1.2 Atividades Genéricas de Processo de Software*, independentemente do ciclo de vida adotado (preditivo, iterativo ou ágil), a literatura clássica de engenharia de software (Pressman e Sommerville) mapeia cinco atividades genéricas de processo.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A flexibilidade no planejamento implica em manter todos os processos rigidamente definidos, sem possibilidade de...". De acordo com a teoria estudada em *3.4 Artefatos Oficiais e seus Três Compromissos Formais*, o Sprint Backlog é composto pela Meta da Sprint (o porquê), o conjunto de itens selecionados do Product Backlog (o quê) e o plano de ação detalhado (o como). A Meta da Sprint é o objetivo único acordado para a iteração, que não muda durante a sua execução.
> - **D)** **Correta.** Conforme fundamentado na seção *2.1 Abordagem Preditiva: Modelo Cascata (Waterfall) e Modelo V* deste guia, desvantagens: Inflexibilidade severa para absorver mudanças; o software só ganha forma executável nas fases finais do projeto, postergando a percepção de valor e a identificação de defeitos críticos para o encerramento do cronograma. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT/DA/2025) ao estabelecer que "O planejamento orientado para mudanças permite antecipar problemas e aproveitar oportunidades, ajudando a...".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O planejamento só é útil para organizações de grande porte, não beneficiando pequenas ou médias empresas". De acordo com a teoria estudada em *3.1 Pilares do Empirismo e Valores Fundamentais*, o Scrum é um framework leve que ajuda pessoas, times e organizações a gerar valor por meio de soluções adaptativas para problemas complexos. Alicerça se no Empirismo e no pensamento Lean.
>
> **Gabarito: D**

---



## 4. Método Kanban e Gestão do Fluxo de Valor

### 4.1 Princípios e Práticas Gerais do Kanban
Concebido por David J. Anderson com base no Sistema Toyota de Produção, o método Kanban é uma abordagem evolucionária e não prescritiva para gestão de fluxos de trabalho do conhecimento.

- **Princípios de Gestão de Mudança:** Comece com o que você faz hoje; busque mudança evolucionária e incremental; respeite os papéis, responsabilidades e títulos atuais; incentive liderança em todos os níveis.
- **Práticas Gerais do Kanban:**
    1. *Visualizar o fluxo de trabalho* (quadro Kanban com colunas de status);
    2. *Limitar o Trabalho em Progresso (WIP)*;
    3. *Gerenciar o fluxo*;
    4. *Tornar as políticas de processo explícitas*;
    5. *Implementar ciclos de feedback (cadências)*;
    6. *Melhorar colaborativamente e evoluir experimentalmente*.

### 4.2 Limites de Trabalho em Progresso (WIP) e Gargalos
O Kanban opera como um **sistema puxado (*pull system*)**:

- **Limite de WIP (Work In Progress):** Cada coluna do quadro possui um teto máximo de itens permitidos simultaneamente (ex.: a coluna "Testes" com WIP = 3).
- **Efeito Prático:** Impede a sobrecarga da equipe, reduz o desperdício de troca de contexto (*context switching*) e torna imediatamente visíveis os **gargalos** de produção. Se uma coluna atingir o limite de WIP, a etapa anterior é impedida de empurrar novos itens, forçando os membros da equipe a colaborar para destravar o gargalo (*"Pare de começar e comece a terminar!"*).

### 4.3 Métricas de Fluxo: Lead Time, Cycle Time, Throughput e CFD
- **Lead Time:** É o tempo total decorrido entre a solicitação inicial da demanda pelo cliente (registro no backlog) até a sua efetiva entrega em ambiente de produção;
- **Cycle Time:** É o tempo em que a equipe técnica esteve ativamente trabalhando no desenvolvimento do item (desde que o cartão foi puxado para a primeira coluna de execução até a conclusão da tarefa);
- **Throughput (Vazão):** Quantidade de itens entregues e concluídos por unidade de tempo (ex.: 12 tarefas por semana);
- **Diagrama de Fluxo Cumulativo (CFD - Cumulative Flow Diagram):** Gráfico de áreas empilhadas que ilustra o número cumulativo de itens em cada fase do processo ao longo do tempo:
    - *Distância Vertical:* Mostra a quantidade de Trabalho em Progresso (WIP) em um dado instante;
    - *Distância Horizontal:* Revela o Lead Time aproximado dos itens. Bandas com inclinação constante indicam fluxo estável e previsível.

---

### Teste 014
**(FGV – TJ/AP – 2023 – Analista Judiciario Apoio Especializado Tecnologia Da Informacao Desenvolvimento De Sistemas)**
Laura precisa modelar o processo de negócio do seu setor, explicitando o fluxo de trabalho (workflow), visando sua automatização via desenvolvimento de um Sistema de Informação. Para isso, o diagrama comportamental da UML que Laura deve usar é o(a):

* **A)** Use Case;
* **B)** Atividade;
* **C)** Comunicação;
* **D)** Sequência;
* **E)** Máquina de Estado.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Use Case". De acordo com a teoria estudada em *4.1 Princípios e Práticas Gerais do Kanban*, concebido por David J. Anderson com base no Sistema Toyota de Produção, o método Kanban é uma abordagem evolucionária e não prescritiva para gestão de fluxos de trabalho do conhecimento.
> - **B)** **Correta.** Conforme fundamentado na seção *4.3 Métricas de Fluxo: Lead Time, Cycle Time, Throughput e CFD* deste guia, diagrama de Fluxo Cumulativo (CFD Cumulative Flow Diagram): Gráfico de áreas empilhadas que ilustra o número cumulativo de itens em cada fase do processo ao longo do tempo. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/AP/2023) ao estabelecer que "Atividade".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Comunicação". De acordo com a teoria estudada em *1.2 Atividades Genéricas de Processo de Software*, comunicação: Cooperação contínua e levantamento de requisitos junto a clientes e partes interessadas ( stakeholders ).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Sequência". De acordo com a teoria estudada em *4.2 Limites de Trabalho em Progresso (WIP) e Gargalos*, o Kanban opera como um sistema puxado ( pull system ).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Máquina de Estado". De acordo com a teoria estudada em *4.3 Métricas de Fluxo: Lead Time, Cycle Time, Throughput e CFD*, cycle Time: É o tempo em que a equipe técnica esteve ativamente trabalhando no desenvolvimento do item (desde que o cartão foi puxado para a primeira coluna de execução até a conclusão da tarefa).
>
> **Gabarito: B**

---


### Teste 015
**(FGV – TJ/MT – 2024 – Analista Judiciario Tecnologia Da Informacao)**
No Scrum, um papel é responsável por maximizar o valor do produto e do trabalho da equipe, além de definir e ordenar o Product Backlog, papel esse exercido pelo

* **A)** Product Owner.
* **B)** Scrum Master.
* **C)** Desenvolvedor.
* **D)** Stakeholder.
* **E)** Gerente de Projetos.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *3.3 Eventos Formais do Scrum e Regras de Time-box* deste guia, uma Sprint nunca é prorrogada. Se os itens planejados não forem concluídos dentro do time box, a Sprint encerra se normalmente; os itens não finalizados voltam para o Product Backlog. Uma Sprint só pode ser cancelada prematuramente pelo Product Owner, caso a Meta da Sprint ( Sprint Goal ) se torne obsoleta!. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/MT/2024) ao estabelecer que "Product Owner".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Scrum Master". De acordo com a teoria estudada em *3.2 Estrutura do Scrum Team e Responsabilidades*, única pessoa responsável pela gestão eficaz do Product Backlog (criação, ordenação, clareza e comunicação dos itens de backlog).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Desenvolvedor". De acordo com a teoria estudada em *3.2 Estrutura do Scrum Team e Responsabilidades*, responsável por maximizar o valor do produto resultante do trabalho do time.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Stakeholder". De acordo com a teoria estudada em *3. O Framework Scrum (Guia Scrum 2020)*, pB["Product Backlog<br/ (Compromisso: Meta do Produto)"] SP["Sprint Planning"].
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Gerente de Projetos". De acordo com a teoria estudada em *3.4 Artefatos Oficiais e seus Três Compromissos Formais*, o Product Backlog é a lista ordenada e emergente de tudo o que é necessário para melhorar o produto. A Meta do Produto descreve o estado futuro que serve como alvo de longo prazo para o Scrum Team.
>
> **Gabarito: A**

---


### Teste 016
**(FGV – TJ/MT – 2024 – Analista Judiciario Tecnologia Da Informacao)**
No método Kanban, uma das práticas centrais ajuda a identificar gargalos e promover a eficiência ao limitar a quantidade de trabalho em progresso. O texto acima se refere à seguinte prática do Kanban:

* **A)** dividir o trabalho em iterações fixas.
* **B)** estabelecer metas rígidas de entrega.
* **C)** realizar reuniões diárias de acompanhamento.
* **D)** aumentar o número de colunas no quadro Kanban.
* **E)** limitar o WIP (Work in Progress).

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "dividir o trabalho em iterações fixas". De acordo com a teoria estudada em *4.1 Princípios e Práticas Gerais do Kanban*, limitar o Trabalho em Progresso (WIP).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "estabelecer metas rígidas de entrega". De acordo com a teoria estudada em *4.2 Limites de Trabalho em Progresso (WIP) e Gargalos*, o Kanban opera como um sistema puxado ( pull system ).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "realizar reuniões diárias de acompanhamento". De acordo com a teoria estudada em *4.2 Limites de Trabalho em Progresso (WIP) e Gargalos*, efeito Prático: Impede a sobrecarga da equipe, reduz o desperdício de troca de contexto ( context switching ) e torna imediatamente visíveis os gargalos de produção. Se uma coluna atingir o limite de WIP, a etapa anterior é impedida de empurrar novos itens, forçando os membros da equipe a colaborar para destravar o gargalo ( "Pare de começar e comece a terminar!" ).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "aumentar o número de colunas no quadro Kanban". De acordo com a teoria estudada em *4.1 Princípios e Práticas Gerais do Kanban*, visualizar o fluxo de trabalho (quadro Kanban com colunas de status).
> - **E)** **Correta.** Conforme fundamentado na seção *4.2 Limites de Trabalho em Progresso (WIP) e Gargalos* deste guia, limite de WIP (Work In Progress): Cada coluna do quadro possui um teto máximo de itens permitidos simultaneamente (ex.: a coluna "Testes" com WIP = 3). Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/MT/2024) ao estabelecer que "limitar o WIP (Work in Progress)".
>
> **Gabarito: E**

---



## 5. Extreme Programming (XP) e Lean Software Development

### 5.1 Extreme Programming: Valores e Práticas de Engenharia
Criado por Kent Beck, o Extreme Programming (XP) é uma metodologia ágil voltada à excelência técnica e engenharia de software para times pequenos e médios submetidos a requisitos vagos e altamente dinâmicos.

- **Cinco Valores do XP:** Comunicação, Simplicidade, Feedback, Coragem e Respeito.
- **Práticas de Engenharia Centrais (Cobrança Constante em Concursos):**
    1. **Programação em Par (*Pair Programming*):** Dois desenvolvedores trabalham simultaneamente em uma única estação de trabalho. O **Driver (Piloto)** assume o teclado e digita o código com foco no detalhe imediato; o **Navigator (Copiloto)** analisa estrategicamente a solução, checa erros de sintaxe, avalia impactos arquiteturais e elabora casos de teste adicionais;
    2. **Test-Driven Development (TDD):** Desenvolvimento guiado por testes mediante o ciclo contínuo **Red-Green-Refactor**:
        - *Red:* Escrever um teste automatizado que falha (pois a funcionalidade ainda não existe);
        - *Green:* Escrever o código mínimo de produção suficiente para fazer o teste passar;
        - *Refactor:* Limpar e aprimorar o código-fonte (eliminando duplicações), garantindo que todos os testes continuem passando;

    3. **Refatoração Contínua (*Refactoring*):** Melhoria da estrutura interna do código sem alterar seu comportamento observável externo;
    4. **Propriedade Coletiva do Código (*Collective Ownership*):** Qualquer desenvolvedor do time tem liberdade e responsabilidade para alterar qualquer módulo do sistema para corrigir defeitos ou implementar melhorias;
    5. **Integração Contínua (*Continuous Integration*):** Código integrado e testado no repositório compartilhado várias vezes ao dia;
    6. **Design Simples:** O código atende a todos os testes, expressa com clareza a intenção, não possui duplicações (DRY - *Don't Repeat Yourself*) e contém o menor número possível de classes e métodos (YAGNI - *You Aren't Gonna Need It*).

### 5.2 Lean Software Development e Eliminação dos 7 Desperdícios
Adaptado do Sistema Toyota de Produção por Mary e Tom Poppendieck, o desenvolvimento Lean foca na entrega rápida de valor mediante a **eliminação sistemática de desperdícios (*Muda*)**:

| Desperdício no Lean Software | Manifestação Prática no Desenvolvimento de Sistemas |
| :--- | :--- |
| **1. Trabalho Parcialmente Feito** | Código desenvolvido que permanece semanas em branch aguardando testes ou aprovação de deploy. |
| **2. Recursos Extras (Gold Plating)** | Funcionalidades desenvolvidas que nunca serão utilizadas pelo usuário final (excesso de especificação). |
| **3. Reaprendizado** | Redescoberta de soluções por falta de testes automatizados ou ausência de documentação de código limpo. |
| **4. Passagem de Tarefas (Hand-offs)** | Perda de conhecimento e ruídos de comunicação na transição entre silos (analista $\rightarrow$ arquiteto $\rightarrow$ dev $\rightarrow$ tester). |
| **5. Atrasos / Esperas (Delays)** | Desenvolvedores ociosos aguardando liberação de ambiente, homologação de acessos ou aprovação de comitês. |
| **6. Troca de Contexto (Task Switching)** | Alocar profissionais em múltiplos projetos paralelos, gerando perda massiva de produtividade cognitiva. |
| **7. Defeitos e Bugs** | Falhas que chegam a produção e demandam esforço emergencial de correção e retrabalho. |

- **Princípios Fundamentais do Lean:** Eliminar desperdícios; Amplificar o aprendizado; Decidir o mais tarde possível (manter opções em aberto); Entregar o mais rápido possível; Empoderar o time; Construir integridade intrínseca; e Enxergar o todo (*See the whole*).

---

## 6. Fontes Oficiais e Referências Bibliográficas

* [Guia do Scrum Oficial 2020 — Edição Online (Ken Schwaber & Jeff Sutherland)](https://scrumguides.org/scrum-guide.html) - Definição normativa do framework Scrum, pilares empíricos, Scrum Team, eventos e artefatos com seus compromissos.
* [Guia do Scrum 2020 — Documento Oficial em Português do Brasil (PDF)](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-PortugueseBR-3.0.pdf) - Tradução oficial completa da versão 2020 do Guia do Scrum.
* [Manifesto para o Desenvolvimento Ágil de Software (2001)](https://agilemanifesto.org/iso/ptbr/manifesto.html) - Declaração oficial dos quatro valores centrais do desenvolvimento ágil de software.
* [Os 12 Princípios do Software Ágil — Agile Manifesto Oficial](https://agilemanifesto.org/iso/ptbr/principles.html) - Diretrizes fundamentais de entregas contínuas, adaptação a mudanças e excelência técnica.
* [O Guia Oficial do Kanban (Kanban Guides — Português do Brasil)](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-PortugueseBR-3.0.pdf) - Definição formal do método Kanban, práticas de limitação de WIP e métricas de fluxo (Lead Time, Cycle Time e Throughput).
* [Continuous Integration (Martin Fowler — Práticas de Engenharia Ágil e XP)](https://martinfowler.com/articles/continuousIntegration.html) - Fundamentos de integração contínua, automação de builds e práticas técnicas do Extreme Programming (XP).
* SOMMERVILLE, Ian. **Engenharia de Software**. 10. ed. São Paulo: Pearson Education do Brasil, 2019. (Cap. 2 - Processos de Software; Cap. 3 - Desenvolvimento Ágil de Software).
* PRESSMAN, Roger S.; MAXIM, Bruce R. **Engenharia de Software: Uma Abordagem Profissional**. 9. ed. Porto Alegre: AMGH, 2021. (Cap. 2 - Modelos de Processo; Cap. 3 - Agilidade e Processo).
* BECK, Kent; ANDRES, Cynthia. **Extreme Programming Explained: Embrace Change**. 2. ed. Boston: Addison-Wesley Professional, 2004. (Sec. 1 - Values, Principles, and Practices).
