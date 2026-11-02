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
**(CEBRASPE – TRF/6 – 2025 – Analista Judiciario Apoio Especializado Tecnologia Da Informacao)**
As várias disciplinas do CMMI são relativas à engenharia de software e visam oferecer uma solução eficaz para a melhoria dos processos da organização.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Incorreta.** A marcação como **Certo** não procede, pois o enunciado apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "As várias disciplinas do CMMI são relativas à engenharia de software e visam oferecer uma solução eficaz para...". De acordo com a teoria estudada em *1.3 Modelos de Maturidade de Processo (CMMI e MPS.BR)*, *Nível 5 (Em Otimização):* Foco na melhoria contínua e inovação sistemática de processos.
> - **E)** **Correta.** O item está **Errado** (gabarito oficial: **E**). Conforme fundamentado na seção *1.3 Modelos de Maturidade de Processo (CMMI e MPS.BR)* deste guia, *Nível 3 (Definido):* Processos corporativos padronizados e integrados em toda a organização. Portanto, a assertiva examinada pela banca (CEBRASPE – TRF/6/2025) viola os preceitos técnicos do tópico.
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

### Teste 002
**(FCC – TRT 2ª – 2014 – Analista Judiciário - Tecnologia da Informação)**
O modelo de ciclo de vida incremental e iterativo foi proposto como uma resposta aos problemas encontrados no modelo em cascata. Em relação a este tipo de modelo de processo, é INCORRETO afirmar que

* **A)** sequência − um método − na classe − objetos e atores.
* **B)** atividades − um procedimento − no método − classes e objetos.
* **C)** objetos − uma mensagem − no método − objetos e métodos.
* **D)** sequência − um método − no método construtor − classes e métodos.
* **E)** atividades − uma classe − na superclasse − objetos e atores.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "sequência − um método − na classe − objetos e atores". De acordo com a teoria estudada em *2.1 Abordagem Preditiva: Modelo Cascata (Waterfall) e Modelo V*, modelo Cascata (Royce, 1970): Caracteriza-se por uma progressão linear, estritamente sequencial entre as fases do ciclo de vida.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "atividades − um procedimento − no método − classes e objetos". De acordo com a teoria estudada em *1.2 Atividades Genéricas de Processo de Software*, independentemente do ciclo de vida adotado (preditivo, iterativo ou ágil), a literatura clássica de engenharia de software (Pressman e Sommerville) mapeia cinco atividades genéricas de processo.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "objetos − uma mensagem − no método − objetos e métodos". De acordo com a teoria estudada em *4.1 Princípios e Práticas Gerais do Kanban*, concebido por David J. Anderson com base no Sistema Toyota de Produção, o método Kanban é uma abordagem evolucionária e não prescritiva para gestão de fluxos de trabalho do conhecimento.
> - **D)** **Correta.** Conforme fundamentado na seção *5.1 Extreme Programming: Valores e Práticas de Engenharia* deste guia, design Simples: O código atende a todos os testes, expressa com clareza a intenção, não possui duplicações (DRY - *Don't Repeat Yourself*) e contém o menor número possível de classes e métodos (YAGNI - *You Aren't Gonna Need It*). Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 2ª/2014) ao estabelecer que "sequência − um método − no método construtor − classes e métodos".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "atividades − uma classe − na superclasse − objetos e atores". De acordo com a teoria estudada em *1.1 Escopo da Engenharia de Software e a Crise do Software*, a Engenharia de Software é a disciplina de engenharia dedicada ao estabelecimento e uso de sólidos princípios e métodos sistemáticos, disciplinados e quantificáveis para o desenvolvimento, operação e manutenção de software de alta qualidade dentro de custos e prazos previsíveis.
>
> **Gabarito: D**

---

### Teste 003
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Administração)**
Em 2024, Belém completou 408 anos. Sua arquitetura e sua urbanização, entretanto, conservam ainda o que foi realizado durante o ciclo da borracha, dando origem à cultura da Belle Époque paraense (1870-1910). As afirmativas a seguir descrevem corretamente a Belle Époque paraense, à exceção de uma. Assinale-a.

* **A)** O então gestor da cidade, o intendente Antônio Lemos, desejava reproduzir na América uma configuração urbana europeizada, por isso favoreceu a construção de ruas largas, chamadas boulevards, e de áreas verdes como o Bosque Rodrigues Alves, inspirado no Bois de Boulogne parisiense.
* **B)** A urbanização e a cultura da Belle Époque inspiravam-se sobretudo na cultura francesa, de modo que políticos e elites locais buscavam transpor para Belém o modo de vida e as manifestações artísticas da Paris da época, mediante a construção de teatros líricos, como o Theatro da Paz, por exemplo.
* **C)** A construção de um espaço urbano considerado civilizado levou à formulação de um paisagismo tropical moderno, marcado por canteiros curvos e fluidos e pela valorização da vegetação nativa, como se experimentava em Paris e Londres no mesmo período.
* **D)** O poder público implantou em Belém serviços pautados em tecnologia avançada, como o bonde elétrico, a iluminação pública e um modelo sanitarista pautado na construção de redes de esgoto, de abastecimento de água e de tratamento do lixo.
* **E)** O conceito de modernidade aplicado às reformas de Belém estava ligado à ideia de progresso, materializada pela construção de símbolos modernos como as ferrovias, associadas à intensificação das redes comerciais no último quarto do século XIX.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O então gestor da cidade, o intendente Antônio Lemos, desejava reproduzir na América uma configuração urbana...". De acordo com a teoria estudada em *3.4 Artefatos Oficiais e seus Três Compromissos Formais*, a DoD é a descrição formal dos critérios de qualidade exigidos para que o item seja considerado pronto para uso.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A urbanização e a cultura da Belle Époque inspiravam-se sobretudo na cultura francesa, de modo que políticos e...". De acordo com a teoria estudada em *2.1 Abordagem Preditiva: Modelo Cascata (Waterfall) e Modelo V*, modelo Cascata (Royce, 1970): Caracteriza-se por uma progressão linear, estritamente sequencial entre as fases do ciclo de vida.
> - **C)** **Correta.** Conforme fundamentado na seção *1.2 Atividades Genéricas de Processo de Software* deste guia, construção: Atividades conjugadas de codificação (programação) e testes automatizados/manuais de software. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "A construção de um espaço urbano considerado civilizado levou à formulação de um paisagismo tropical moderno...".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O poder público implantou em Belém serviços pautados em tecnologia avançada, como o bonde elétrico, a iluminação...". De acordo com a teoria estudada em *1.1 Escopo da Engenharia de Software e a Crise do Software*, *Complexidade Acidental:* Relacionada às limitações transitórias da tecnologia utilizada (compiladores rudimentares, falta de ferramentas de integração ou linguagens de baixo nível).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O conceito de modernidade aplicado às reformas de Belém estava ligado à ideia de progresso, materializada pela...". De acordo com a teoria estudada em *3.1 Pilares do Empirismo e Valores Fundamentais*, *Inspeção:* O progresso rumo aos objetivos deve ser examinado com frequência diligente para identificar anomalias.
>
> **Gabarito: C**

---

### Teste 004
**(FCC – TRT 14ª – 2016 – Analista Judiciário - Apoio Especializado - Tecnologia da Informação)**
De acordo com a ITIL v3, atualizada em 2011, o Catálogo de Serviços é

* **A)** parte do Portfólio de Serviço e contém informações sobre serviços de TI: 1. voltados para o cliente, que são visíveis para o negócio e 2. de suporte, requeridos pelo provedor de serviço para entregar serviços voltados para o cliente.
* **B)** estruturado por um banco de dados com informações sobre todos os serviços de TI já implantados, em produção e obsoletos, sem incluir serviços disponíveis para implantação.
* **C)** o responsável por fornecer e manter o Portfólio de Serviços e por garantir que esteja disponível àqueles autorizados.
* **D)** um documento que contém detalhes de um serviço novo ou modificado recentemente.
* **E)** usado para gerenciar o ciclo de vida completo de todos os serviços de TI, incluindo duas categorias: 1. Funil de Serviço (proposto ou em desenvolvimento) e 2. Portfólio de Serviço (em produção ou disponível para implantação).

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *2.1 Abordagem Preditiva: Modelo Cascata (Waterfall) e Modelo V* deste guia, requisitos de Negócio $\longleftrightarrow$ Testes de Aceitação. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 14ª/2016) ao estabelecer que "parte do Portfólio de Serviço e contém informações sobre serviços de TI: 1. voltados para o cliente, que são...".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "estruturado por um banco de dados com informações sobre todos os serviços de TI já implantados, em produção e...". De acordo com a teoria estudada em *1.2 Atividades Genéricas de Processo de Software*, implantação (Deployment): Disponibilização do software em ambiente operacional, homologação pelo usuário final, suporte técnico e coleta de feedback.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "o responsável por fornecer e manter o Portfólio de Serviços e por garantir que esteja disponível àqueles...". De acordo com a teoria estudada em *3.4 Artefatos Oficiais e seus Três Compromissos Formais*, cada um dos três artefatos do Scrum contém um compromisso formal associado (introduzido formalmente no Guia 2020) para fornecer transparência e foco.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "um documento que contém detalhes de um serviço novo ou modificado recentemente". De acordo com a teoria estudada em *2.3 Abordagem Adaptativa / Ágil: O Manifesto Ágil de 2001*, colaboração com o cliente: Negociação de contratos.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "usado para gerenciar o ciclo de vida completo de todos os serviços de TI, incluindo duas categorias: 1. Funil de...". De acordo com a teoria estudada em *2.1 Abordagem Preditiva: Modelo Cascata (Waterfall) e Modelo V*, modelo Cascata (Royce, 1970): Caracteriza-se por uma progressão linear, estritamente sequencial entre as fases do ciclo de vida.
>
> **Gabarito: A**

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

### Teste 005
**(FGV – TRT 16ª – 2022 – Analista Judiciário (Área Administrativa - Tecnologia da Informação))**
Observe o seguinte texto: “’Há muita gente atrapalhando a vida do governador, inclusive o próprio governador’, costuma dizer um deputado muito conhecido. Trata-se de um comentário muito comum na Assembleia Legislativa”. A introdução utilizada nesse texto pode ser identificada como

* **A)** uma alusão histórica.
* **B)** uma interrogação.
* **C)** uma citação.
* **D)** uma definição.
* **E)** uma divisão de temas.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "uma alusão histórica". De acordo com a teoria estudada em *3.3 Eventos Formais do Scrum e Regras de Time-box*, uma Sprint só pode ser cancelada prematuramente pelo Product Owner, caso a Meta da Sprint (*Sprint Goal*) se torne obsoleta!.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "uma interrogação". De acordo com a teoria estudada em *3.1 Pilares do Empirismo e Valores Fundamentais*, *Transparência:* Processos e artefatos devem ser visíveis para todos os responsáveis pelos resultados.
> - **C)** **Correta.** Conforme fundamentado na seção *3.3 Eventos Formais do Scrum e Regras de Time-box* deste guia, sprint Planning: Define o plano de trabalho da Sprint abordando: 1) *Por que a Sprint é valiosa?* 2) *O que pode ser feito?* 3) *Como o trabalho será realizado?* — Máximo de 8 horas. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT 16ª/2022) ao estabelecer que "uma citação".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "uma definição". De acordo com a teoria estudada em *3.2 Estrutura do Scrum Team e Responsabilidades*, adaptam o plano diariamente na Daily Scrum e responsabilizam-se pela qualidade aplicando a Definição de Pronto (*DoD*).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "uma divisão de temas". De acordo com a teoria estudada em *3.1 Pilares do Empirismo e Valores Fundamentais*, *Inspeção:* O progresso rumo aos objetivos deve ser examinado com frequência diligente para identificar anomalias.
>
> **Gabarito: C**

---

### Teste 006
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
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "kanban". De acordo com a teoria estudada em *3.3 Eventos Formais do Scrum e Regras de Time-box*, sprint Review: Inspeção do Incremento produzido com os *stakeholders* para adaptar o Product Backlog com base no feedback real. — Máximo de 4 horas.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "incremento". De acordo com a teoria estudada em *3.4 Artefatos Oficiais e seus Três Compromissos Formais*, o Incremento é um degrau concreto rumo à Meta do Produto. No momento em que um item do Product Backlog atende à Definição de Pronto, um novo Incremento nasce.
> - **C)** **Correta.** Conforme fundamentado na seção *3.4 Artefatos Oficiais e seus Três Compromissos Formais* deste guia, o Sprint Backlog é composto pela Meta da Sprint (o porquê), o conjunto de itens selecionados do Product Backlog (o quê) e o plano de ação detalhado (o como). A Meta da Sprint é o objetivo único acordado para a iteração, que não muda durante a sua execução. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/AP/2023) ao estabelecer que "sprint backlog".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "product owner". De acordo com a teoria estudada em *3.3 Eventos Formais do Scrum e Regras de Time-box*, uma Sprint só pode ser cancelada prematuramente pelo Product Owner, caso a Meta da Sprint (*Sprint Goal*) se torne obsoleta!.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "meta do produto". De acordo com a teoria estudada em *3.4 Artefatos Oficiais e seus Três Compromissos Formais*, o Product Backlog é a lista ordenada e emergente de tudo o que é necessário para melhorar o produto. A Meta do Produto descreve o estado futuro que serve como alvo de longo prazo para o Scrum Team.
>
> **Gabarito: C**

---

### Teste 007
**(FCC – TRT 9ª – 2015 – Analista Judiciário - Apoio Especializado - Tecnologia da Informação)**
Um Analista da área de TI construiu a classe Vectors e a classe de teste VectorsTest utilizando o JUnit. package sample; public final class Vectors { private Vectors() {} public static int scalarMultiplication(int[] a, int[] b) { if ((a == null) || (b == null)) { throw new IllegalArgumentException("Argumento nulo"); } if (a.length != b.length) { throw new IllegalArgumentException("Vetores com tuplas diferentes"); } int sum = 0; for (int i = 0; i < a.length; i++) { sum += a[i] * b[i]; } return sum; } } package sample; import junit.framework.TestCase; public class VectorsTest extends TestCase { public VectorsTest(String testName) { super(testName); } public void testScalarMultiplication() { I  } } I Ao executar a classe VectorsTest, o teste será reprovado se a lacuna  estiver preenchida com a instrução

* **A)** Scrum.
* **B)** Dynamic Systems Development Method.
* **C)** Crystal Clear.
* **D)** Extreme Programming.
* **E)** Feature Driven Development.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Scrum". De acordo com a teoria estudada em *3.2 Estrutura do Scrum Team e Responsabilidades*, no Guia 2020 NÃO existe mais o papel "Time de Desenvolvimento" (Development Team). Existe apenas o *Scrum Team*, formado por PO, Scrum Master e Desenvolvedores. Não há subtimes nem hierarquias internas!.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Dynamic Systems Development Method". De acordo com a teoria estudada em *5.2 Lean Software Development e Eliminação dos 7 Desperdícios*, 2. Recursos Extras (Gold Plating): Funcionalidades desenvolvidas que nunca serão utilizadas pelo usuário final (excesso de especificação).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Crystal Clear". De acordo com a teoria estudada em *5.2 Lean Software Development e Eliminação dos 7 Desperdícios*, adaptado do Sistema Toyota de Produção por Mary e Tom Poppendieck, o desenvolvimento Lean foca na entrega rápida de valor mediante a eliminação sistemática de desperdícios (*Muda*).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Extreme Programming". De acordo com a teoria estudada em *5.1 Extreme Programming: Valores e Práticas de Engenharia*, o Driver (Piloto) assume o teclado e digita o código com foco no detalhe imediato; o Navigator (Copiloto) analisa estrategicamente a solução, checa erros de sintaxe, avalia impactos arquiteturais e elabora casos de teste adicionais.
> - **E)** **Correta.** Conforme fundamentado na seção *5.1 Extreme Programming: Valores e Práticas de Engenharia* deste guia, test-Driven Development (TDD): Desenvolvimento guiado por testes mediante o ciclo contínuo Red-Green-Refactor. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 9ª/2015) ao estabelecer que "Feature Driven Development".
>
> **Gabarito: E**

---

### Teste 008
**(FCC – TRT 24ª – 2017 – Analista Judiciário - Tecnologia da Informação)**
Considere que uma equipe está trabalhando no desenvolvimento de um software com base em práticas e métricas ágeis e, em uma dada Sprint, a situação é apresentada pelo quadro abaixo. (http://www.devmedia.com.br/praticas-e-artefatos-comumente-utilizados-com-scrum/27911) Neste cenário é correto afirmar que

* **A)** <groupId>junit</groupId> <version>4.12</version> <exclusion>system</exclusion>
* **B)** <groupId>junit 4.12</groupId> <artifactId>junit</artifactId> <system>test</system> <scope>system</scope>
* **C)** <groupId>junit</groupId> <version>4.12</version> <test>compile</test>
* **D)** <groupId>junit</groupId> <artifactId>junit 4.12</artifactId> <compile>test</compile>
* **E)** <groupId>junit</groupId> <artifactId>junit</artifactId> <version>4.12</version> <scope>test</scope>

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "`<groupId>`junit`</groupId>` `<version>`4.12`</version>` `<exclusion>`system`</exclusion>`". De acordo com a teoria estudada em *5.1 Extreme Programming: Valores e Práticas de Engenharia*, test-Driven Development (TDD): Desenvolvimento guiado por testes mediante o ciclo contínuo Red-Green-Refactor.
> - **B)** **Correta.** Conforme fundamentado na seção *3.5 Métricas e Gráficos de Acompanhamento (Burndown e Burnup)* deste guia, burnup Chart: Gráfico com duas linhas: uma demonstrando o crescimento do escopo total ao longo do tempo e outra demonstrando o trabalho efetivamente concluído (*done*). Excelente para detectar expansão de escopo (*scope creep*). Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 24ª/2017) ao estabelecer que "`<groupId>`junit 4.12`</groupId>` `<artifactId>`junit`</artifactId>` `<system>`test`</system>`...".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "`<groupId>`junit`</groupId>` `<version>`4.12`</version>` `<test>`compile`</test>`". De acordo com a teoria estudada em *4.2 Limites de Trabalho em Progresso (WIP) e Gargalos*, o Kanban opera como um sistema puxado (*pull system*).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "`<groupId>`junit`</groupId>` `<artifactId>`junit 4.12`</artifactId>` `<compile>`test`</compile>`". De acordo com a teoria estudada em *4.3 Métricas de Fluxo: Lead Time, Cycle Time, Throughput e CFD*, cycle Time: É o tempo em que a equipe técnica esteve ativamente trabalhando no desenvolvimento do item (desde que o cartão foi puxado para a primeira coluna de execução até a conclusão da tarefa).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "`<groupId>`junit`</groupId>` `<artifactId>`junit`</artifactId>` `<version>`4.12`</version>` `<scope>`test`</scope>`". De acordo com a teoria estudada em *3.5 Métricas e Gráficos de Acompanhamento (Burndown e Burnup)*, sprint Burndown Chart: Gráfico que exibe a quantidade de trabalho restante (geralmente em pontos de história ou horas) em relação ao tempo da Sprint. A inclinação da linha decrescente indica se a equipe concluirá as tarefas no prazo.
>
> **Gabarito: B**

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

### Teste 009
**(FGV – TJ/DFT – 2022 – Analista Judiciario Suporte Em Tecnologia Da Informacao)**
“Também leio livros, muitos livros: mas com eles aprendo menos do que com a vida. Apenas um livro me ensinou muito: o dicionário. Oh, o dicionário, adoro-o. Mas também adoro a estrada, um dicionário muito mais maravilhoso.” Depreende-se desse pensamento que seu autor:

* **A)** nada aprende com os livros, com exceção do dicionário;
* **B)** deve tudo que conhece ao dicionário;
* **C)** adquire conhecimentos com as viagens que realiza;
* **D)** conhece o mundo por meio da experiência de vida;
* **E)** constatou que os dicionários registram o melhor da vida. LÍNGUA INGLESA Here’s why we’ll never be able to build a brain in a computer It’s easy to equate brains and computers – they’re both thinking machines, after all. But the comparison doesn’t really stand up to closer inspection, as Dr. Lisa Feldman Barrett reveals. People often describe the brain as a computer, as if neurons are like hardware and the mind is software. But this metaphor is deeply flawed. A computer is built from static parts, whereas your brain constantly rewires itself as you age and learn. A computer stores information in files that are retrieved exactly, but brains don’t store information in any literal sense. Your memory is a constant construction of electrical pulses and swirling chemicals, and the same remembrance can be reassembled in different ways at different times. Brains also do something critical that computers today can’t. A computer can be trained with thousands of photographs to recognise a dandelion as a plant with green leaves and yellow petals. You, however, can look at a dandelion and understand that in different situations it belongs to different categories. A dandelion in your vegetable garden is a weed, but in a bouquet from your child it’s a delightful flower. A dandelion in a salad is food, but people also consume dandelions as herbal medicine. In other words, your brain effortlessly categorises objects by their function, not just their physical form. Some scientists believe that this incredible ability of the brain, called ad hoc category construction, may be fundamental to the way brains work. Also, unlike a computer, your brain isn’t a bunch of parts in an empty case. Your brain inhabits a body, a complex web of systems that include over 600 muscles in motion, internal organs, a heart that pumps 7,500 litres of blood per day, and dozens of hormones and other chemicals, all of which must be coordinated, continually, to digest food, excrete waste, provide energy and fight illness.[…] If we want a computer that thinks, feels, sees or acts like us, it must regulate a body – or something like a body – with a complex collection of systems that it must keep in balance to continue operating, and with sensations to keep that regulation in check. Today’s computers don’t work this way, but perhaps some engineers can come up with something that’s enough like a body to provide this necessary ingredient. For now, ‘brain as computer’ remains just a metaphor. Metaphors can be wonderful for explaining complex topics in simple terms, but they fail when people treat the metaphor as an explanation. Metaphors provide the illusion of knowledge. (Adapted from https://www.sciencefocus.com/future-technology/can- we-build-brain-computer/ Published: 24th October, 2021, retrieved on February 9th, 2022)

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "nada aprende com os livros, com exceção do dicionário". De acordo com a teoria estudada em *1.2 Atividades Genéricas de Processo de Software*, independentemente do ciclo de vida adotado (preditivo, iterativo ou ágil), a literatura clássica de engenharia de software (Pressman e Sommerville) mapeia cinco atividades genéricas de processo.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "deve tudo que conhece ao dicionário". De acordo com a teoria estudada em *2.1 Abordagem Preditiva: Modelo Cascata (Waterfall) e Modelo V*, modelo Cascata (Royce, 1970): Caracteriza-se por uma progressão linear, estritamente sequencial entre as fases do ciclo de vida.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "adquire conhecimentos com as viagens que realiza". De acordo com a teoria estudada em *2.4 Abordagens Híbridas de Desenvolvimento*, reconhecem que o mundo corporativo raramente opera em extremos absolutos. Um projeto híbrido pode adotar.
> - **D)** **Correta.** Conforme fundamentado na seção *3.1 Pilares do Empirismo e Valores Fundamentais* deste guia, o Scrum é um framework leve que ajuda pessoas, times e organizações a gerar valor por meio de soluções adaptativas para problemas complexos. Alicerça-se no Empirismo e no pensamento Lean. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/DFT/2022) ao estabelecer que "conhece o mundo por meio da experiência de vida".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "constatou que os dicionários registram o melhor da vida. LÍNGUA INGLESA Here’s why we’ll never be able to build a...". De acordo com a teoria estudada em *5.1 Extreme Programming: Valores e Práticas de Engenharia*, design Simples: O código atende a todos os testes, expressa com clareza a intenção, não possui duplicações (DRY - *Don't Repeat Yourself*) e contém o menor número possível de classes e métodos (YAGNI - *You Aren't Gonna Need It*).
>
> **Gabarito: D**

---

### Teste 010
**(FGV – TRT da 24º Região – 2025 – Analista Judiciário - Área Administrativa - Contabilidade)**
Uma sociedade empresária do setor de engenharia tem uma biblioteca, que é utilizada por seus empregados para obter informações técnicas. Os livros da biblioteca são classificados no balanço patrimonial da sociedade empresária como

* **A)** ativo intangível.
* **B)** Investimentos.
* **C)** ativo Imobilizado.
* **D)** ativo circulante.
* **E)** ativo realizável a longo prazo.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "ativo intangível". De acordo com a teoria estudada em *2.4 Abordagens Híbridas de Desenvolvimento*, abordagem adaptativa/ágil na execução das iterações técnicas pelas equipes de desenvolvimento (com Sprints Scrum, gestão visual Kanban e testes contínuos).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Investimentos". De acordo com a teoria estudada em *1.1 Escopo da Engenharia de Software e a Crise do Software*, a Engenharia de Software é a disciplina de engenharia dedicada ao estabelecimento e uso de sólidos princípios e métodos sistemáticos, disciplinados e quantificáveis para o desenvolvimento, operação e manutenção de software de alta qualidade dentro de custos e prazos previsíveis.
> - **C)** **Correta.** Conforme fundamentado na seção *1.1 Escopo da Engenharia de Software e a Crise do Software* deste guia, *Complexidade Acidental:* Relacionada às limitações transitórias da tecnologia utilizada (compiladores rudimentares, falta de ferramentas de integração ou linguagens de baixo nível). Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT da 24º Região/2025) ao estabelecer que "ativo Imobilizado".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "ativo circulante". De acordo com a teoria estudada em *1.1 Escopo da Engenharia de Software e a Crise do Software*, a Crise do Software: O termo emergiu formalmente na Conferência da OTAN (NATO Conference) em 1968, em Garmisch, motivado pela incapacidade sistemática da indústria de entregar sistemas confiáveis dentro do orçamento e cronograma.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "ativo realizável a longo prazo". De acordo com a teoria estudada em *3.4 Artefatos Oficiais e seus Três Compromissos Formais*, o Product Backlog é a lista ordenada e emergente de tudo o que é necessário para melhorar o produto. A Meta do Produto descreve o estado futuro que serve como alvo de longo prazo para o Scrum Team.
>
> **Gabarito: C**

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

### Teste 011
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
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "III, apenas". De acordo com a teoria estudada em *4.3 Métricas de Fluxo: Lead Time, Cycle Time, Throughput e CFD*, diagrama de Fluxo Cumulativo (CFD - Cumulative Flow Diagram): Gráfico de áreas empilhadas que ilustra o número cumulativo de itens em cada fase do processo ao longo do tempo.
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e II, apenas". De acordo com a teoria estudada em *4.3 Métricas de Fluxo: Lead Time, Cycle Time, Throughput e CFD*, throughput (Vazão): Quantidade de itens entregues e concluídos por unidade de tempo (ex.: 12 tarefas por semana).
> - **E)** **Correta.** Conforme fundamentado na seção *4.3 Métricas de Fluxo: Lead Time, Cycle Time, Throughput e CFD* deste guia, cycle Time: É o tempo em que a equipe técnica esteve ativamente trabalhando no desenvolvimento do item (desde que o cartão foi puxado para a primeira coluna de execução até a conclusão da tarefa). Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/RR/2024) ao estabelecer que "II e III, apenas".
>
> **Gabarito: E**

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
