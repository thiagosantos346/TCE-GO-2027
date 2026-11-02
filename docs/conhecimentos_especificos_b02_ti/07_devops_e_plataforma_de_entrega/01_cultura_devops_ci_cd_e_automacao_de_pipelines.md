# 01 - CI/CD, Pipelines e Automação de Entrega

> **Matéria:** DevOps, Plataforma de Desenvolvimento e Engenharia de Entrega  
> **Cargo:** B02 – Técnico de Controle Externo – Especialidade: Tecnologia da Informação  
> **Arquivo:** `01_cultura_devops_ci_cd_e_automacao_de_pipelines.md`  



---


## 📌 Ementa / Itens do Edital
- Conceitos e fundamentos da cultura DevOps
- Integração Contínua (CI - Continuous Integration)
- Entrega Contínua (Continuous Delivery) vs. Implantação Contínua (Continuous Deployment)
- Estrutura e estágios de pipelines de desenvolvimento
- Automação de compilação (build) e de testes
- Estratégias modernas de publicação (Blue-Green, Canary, Rolling Update)
- Ferramentas de automação: GitHub Actions, GitLab CI/CD e Jenkins

---

## 🧭 Sumário

1. [Fundamentos da Cultura DevOps](#1-fundamentos-da-cultura-devops)
    1. [Eliminação do Muro da Confusão e Responsabilidade Compartilhada](#11-eliminacao-do-muro-da-confusao-e-responsabilidade-compartilhada)
    2. [O Framework C.A.L.M.S.](#12-o-framework-calms)
    3. [As Três Vias do DevOps](#13-as-tres-vias-do-devops)
    4. [As Quatro Métricas DORA (DevOps Research and Assessment)](#14-as-quatro-metricas-dora-devops-research-and-assessment)
    5. [Teste 171](#Teste-171)
    6. [Teste 172](#Teste-172)
    7. [Teste 173](#Teste-173)
2. [O Espectro de Automação: CI vs. CD (Delivery vs. Deployment)](#2-o-espectro-de-automacao-ci-vs-cd-delivery-vs-deployment)
    1. [Integração Contínua (CI): Boas Práticas, Trunk-Based e Princípio Stop the Line](#21-integracao-continua-ci-boas-praticas-trunk-based-e-principio-stop-the-line)
    2. [Entrega Contínua (Continuous Delivery): O Release Candidate Permanente](#22-entrega-continua-continuous-delivery-o-release-candidate-permanente)
    3. [Implantação Contínua (Continuous Deployment): Promoção Automática para Produção](#23-implantacao-continua-continuous-deployment-promocao-automatica-para-producao)
    4. [Tabela Comparativa Detalhada: CI vs. Continuous Delivery vs. Continuous Deployment](#24-tabela-comparativa-detalhada-ci-vs-continuous-delivery-vs-continuous-deployment)
    5. [Teste 174](#Teste-174)
    6. [Teste 175](#Teste-175)
3. [Estratégias Modernas de Publicação (Deployment Strategies)](#3-estrategias-modernas-de-publicacao-deployment-strategies)
    1. [Recreate (Recriação)](#31-recreate-recriacao)
    2. [Rolling Update (Atualização Progressiva)](#32-rolling-update-atualizacao-progressiva)
    3. [Blue-Green Deployment (Azul-Verde)](#33-blue-green-deployment-azul-verde)
    4. [Canary Deployment (Canário)](#34-canary-deployment-canario)
    5. [Feature Flags / Feature Toggles e Dark Launching](#35-feature-flags-feature-toggles-e-dark-launching)
    6. [Teste 176](#Teste-176)
    7. [Teste 177](#Teste-177)
    8. [Teste 178](#Teste-178)
4. [Estrutura, Estágios e Segurança de Pipelines (DevSecOps)](#4-estrutura-estagios-e-seguranca-de-pipelines-devsecops)
    1. [Estágios Canônicos: Lint, Análise Estática (SAST/SCA), Build, Testes e Registry](#41-estagios-canonicos-lint-analise-estatica-sastsca-build-testes-e-registry)
    2. [Pirâmide de Testes Automatizados no Pipeline](#42-piramide-de-testes-automatizados-no-pipeline)
    3. [Teste 179](#Teste-179)
5. [Ferramentas de Automação: Sintaxe, Arquitetura e Manifestos](#5-ferramentas-de-automacao-sintaxe-arquitetura-e-manifestos)
    1. [GitHub Actions: Workflows, Events, Jobs, Steps, Runners e Secrets](#51-github-actions-workflows-events-jobs-steps-runners-e-secrets)
    2. [GitLab CI/CD: Stages, Jobs, Artifacts, Cache, Rules e Runners](#52-gitlab-cicd-stages-jobs-artifacts-cache-rules-e-runners)
    3. [Jenkins: Arquitetura Controller-Agent, Declarative Pipeline e Scripted Pipeline](#53-jenkins-arquitetura-controller-agent-declarative-pipeline-e-scripted-pipeline)
    4. [Teste 180](#Teste-180)
    5. [Teste 181](#Teste-181)
6. [🌐 Fontes Oficiais e Referências Bibliográficas](#fontes-oficiais-e-referencias-bibliograficas)

---

## 1. Fundamentos da Cultura DevOps

A cultura DevOps surgiu como uma resposta essencial à ineficiência e aos conflitos crônicos entre os modelos tradicionais de desenvolvimento de software e de operação de infraestrutura. Em organizações convencionais com silos funcionais estanques, as equipes operam com incentivos conflitantes:

- A equipe de **Desenvolvimento (Dev)** é cobrada por velocidade de entrega, lançamento contínuo de novas funcionalidades e mudanças dinâmicas no sistema.
- A equipe de **Operações (Ops)** é cobrada por estabilidade operacional, resiliência, disponibilidade ininterrupta (uptime) e contenção de riscos, vendo qualquer alteração no ambiente produtivo como uma ameaça potencial à estabilidade.

Esse choque histórico consolidou o chamado **"Muro da Confusão" (*Wall of Confusion*)**: desenvolvedores empacotavam binários em suas máquinas locais e os "jogavam por cima do muro" para que a equipe de infraestrutura os instalasse manualmente em produção, gerando o clássico empasse *"Na minha máquina funciona, o problema é na infraestrutura"*.

```mermaid
flowchart LR
    subgraph Silos_Tradicionais["Abordagem Tradicional em Silos"]
        DEV["Desenvolvimento<br/>Foco: Mudança e Velocidade"]
        WALL["⛔ Muro da Confusão<br/>(Passagem de bastão 'Jogar por cima do muro')"]
        OPS["Operações<br/>Foco: Estabilidade e Resiliência"]
        DEV --> WALL --> OPS
    end
```

```mermaid
flowchart LR
    subgraph DevOps_Integrado["Cultura DevOps Integrada"]
        DEV_OPS["Responsabilidade Compartilhada de Ponta a Ponta<br/>(You build it, you run it - Werner Vogels)"]
        CALMS["CALMS: Cultura | Automação | Lean | Medição | Compartilhamento"]
        DEV_OPS --- CALMS
    end
```

### 1.1 Eliminação do Muro da Confusão e Responsabilidade Compartilhada

O DevOps quebra essa barreira através da fusão de processos, práticas colaborativas e ferramentas automatizadas, estabelecendo o princípio da **responsabilidade compartilhada de ponta a ponta** (*"You build it, you run it"*, sintetizado por Werner Vogels, CTO da Amazon). Sob essa ótica:

- Desenvolvedores assumem a corresponsabilidade pelo comportamento da aplicação em produção, projetando sistemas já preparados para observabilidade, diagnóstico e tolerância a falhas.
- Engenheiros de operações e infraestrutura fornecem plataformas automatizadas (*Platform Engineering*) como autosserviço (*Self-Service*), permitindo que os desenvolvedores criem ambientes, executem pipelines e realizem deploys seguros de forma autônoma.
- Adota-se a cultura de post-mortems isentos de culpa (*Blameless Post-Mortems*), tratando falhas de produção não como erros individuais de programadores, mas como deficiências no sistema e nos processos que exigem automação de barreiras de proteção (*guardrails*).

### 1.2 O Framework C.A.L.M.S.

Sistematizado pioneiramente por Damon Edwards e John Willis (e posteriormente complementado por Jez Humble), o modelo conceitual **CALMS** define os cinco pilares essenciais para avaliar e evoluir a maturidade DevOps:

1. **C (Culture - Cultura):** Transformação comportamental centrada em pessoas, confiança mútua, colaboração multidisciplinar e eliminação de silos. Prioriza a segurança psicológica da equipe para experimentar e inovar.
2. **A (Automation - Automação):** Substituição de intervenções manuais propensas a erros por pipelines automatizados de build, testes, segurança, provisionamento de infraestrutura (IaC) e deploy. A automação elimina o trabalho repetitivo e sem valor agregado (*toil*).
3. **L (Lean - Princípios Enxutos):** Aplicação dos princípios da manufatura enxuta (Sistema Toyota de Produção) ao ciclo de software: redução drástica de desperdícios, entregas frequentes em lotes pequenos (*small batch sizes*), redução do tempo de fila e limitação estrita do trabalho em progresso (*WIP - Work in Progress*).
4. **M (Measurement - Medição):** Coleta contínua e visibilidade de telemetria, abrangendo métricas de negócio (conversões, faturamento), métricas técnicas de estabilidade (tempo de resposta, taxa de erros) e métricas de processo de entrega (como o framework DORA).
5. **S (Sharing - Compartilhamento):** Disseminação aberta de conhecimento, ferramentas, erros, padrões arquiteturais e vitórias entre todos os setores da instituição, prevenindo a criação de novos "feudos" tecnológicos.

### 1.3 As Três Vias do DevOps

Formalizadas por Gene Kim, Kevin Behr e George Spafford nas obras seminais *The Phoenix Project* e *The DevOps Handbook*, as Três Vias estruturam as práticas dinâmicas da entrega contínua:

1. **A Primeira Via (O Princípio do Fluxo):** Tem por objetivo acelerar a velocidade com que o valor transita da esquerda (Desenvolvimento e Requisitos) para a direita (Operações e Produção). Exige tornar o fluxo de trabalho visível (via quadros Kanban), limitar o trabalho em andamento (WIP), reduzir o tamanho dos lotes e criar barreiras que impeçam terminantemente a propagação de defeitos para etapas posteriores (*downstream*).
2. **A Segunda Via (O Princípio do Feedback):** Busca encurtar e amplificar continuamente os ciclos de retorno da direita (Operações e Clientes em Produção) para a esquerda (Desenvolvimento). Isso significa que, se um bug surge em produção ou um teste falha no pipeline, os desenvolvedores recebem alarmes e telemetria em tempo real, permitindo identificar a causa raiz e corrigir o problema imediatamente antes que ele escale.
3. **A Terceira Via (O Princípio do Aprendizado Contínuo e Experimentação):** Fomenta uma cultura organizacional de alta confiança que estimula a experimentação deliberada, a tomada de riscos calculados e o domínio da resiliência através da repetição e da prática. O conhecimento gerado a partir de sucessos e falhas locais é sistematicamente compartilhado e incorporado às práticas institucionais de toda a organização.

### 1.4 As Quatro Métricas DORA (DevOps Research and Assessment)

As métricas DORA resultam de quase uma década de pesquisas empíricas e rigor estatístico conduzidas pelo grupo fundado por Nicole Forsgren, Jez Humble e Gene Kim (posteriormente incorporado ao Google Cloud). A FCC cobra sistematicamente a classificação e os impactos dessas métricas:

| Métrica DORA | Dimensão Operacional | Definição Precisa | Nível de Elite / Alta Performance | Nível Baixo |
| :--- | :--- | :--- | :--- | :--- |
| **Deployment Frequency (DF)** | **Throughput (Velocidade)** | Frequência com que a organização implanta com sucesso código no ambiente de produção. | **Múltiplos deploys por dia** (sob demanda contínua). | Menos de 1 deploy a cada 6 meses. |
| **Lead Time for Changes (LTTC)** | **Throughput (Velocidade)** | Intervalo de tempo transcorrido desde o primeiro commit no controle de versão até a entrada efetiva em produção. | **Menos de 1 hora** (do commit ao deploy produtivo). | Entre 1 mês e 6 meses. |
| **Change Failure Rate (CFR)** | **Stability (Estabilidade)** | Percentual de alterações enviadas para produção que resultam em falha operacional imediata (exigindo rollback, hotfix ou intervenção emergencial). | **0% a 15%** de taxa de falhas. | Mais de 45% a 60% de falhas. |
| **Time to Restore Service (MTTR)** | **Stability (Estabilidade)** | Tempo médio necessário para restabelecer a operação normal do serviço quando ocorre um incidente de indisponibilidade em produção. | **Menos de 1 hora** (recuperação ágil via rollback ou fix-forward). | Mais de 1 semana a 1 mês. |

> 🚨 **ALERTA DE PROVA / PEGADINHA FCC:**  
> A FCC adora elaborar afirmativas que tentam classificar incorretamente as dimensões das métricas DORA:
>
> - **Throughput / Velocidade de Entrega:** *Deployment Frequency (DF)* e *Lead Time for Changes (LTTC)*.
> - **Estabilidade / Confiabilidade do Sistema:** *Change Failure Rate (CFR)* e *Time to Restore Service (MTTR)*.
> - **A GRANDE CONCLUSÃO CIENTÍFICA DORA:** Empresas de alta performance **NÃO sacrificam estabilidade em troca de velocidade**. Elas atingem alto throughput E alta estabilidade simultaneamente, quebrando o mito antiquado de que "entregar mais rápido produz mais erros".

---

### Teste 171
**(FCC – TRT-6 – Analista Judiciario Apoio Especializado Tecnologia da Informacao – 2012)**
Com relação ao ciclo de vida do produto, segundo o PMBOK, considere: I. Geralmente o ciclo de vida de um projeto está contido em um ou mais ciclos de vida do produto. O ciclo de vida do produto consiste em fases do produto, geralmente sequenciais e não sobrepostas, determinadas pela necessidade de produção e controle da organização, sendo que a última fase do ciclo de vida de um produto é a entrega para o cliente final. II. Vários aspectos do ciclo de vida do produto prestam-se à execução como projetos, por exemplo, a realização de um estudo de viabilidade, a condução de pesquisas de mercado, a execução de campanhas publicitárias, a instalação de um produto, realização de dinâmicas de grupo e de avaliações de produtos em mercados de teste. Em cada um destes exemplos, o ciclo de vida do projeto difere do ciclo de vida do produto. III. Quando a saída do projeto está relacionada a um produto, existem muitas relações possíveis. Por exemplo, o desenvolvimento de um novo produto pode ser um projeto em si. Ao mesmo tempo, um produto existente pode se beneficiar de um projeto para o acréscimo de novas funções ou características. Está correto o que se afirma em

* **A)** II e III, apenas.
* **B)** I, II e III.
* **C)** I e III, apenas.
* **D)** I, apenas.
* **E)** III, apenas.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *3.5 Feature Flags / Feature Toggles e Dark Launching* deste guia, um código pode estar rodando em produção com a funcionalidade desligada no servidor de configuração remota, sendo ativada sob demanda sem a necessidade de novo pipeline de deploy. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT-6/2012) ao estabelecer que "II e III, apenas".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I, II e III". De acordo com a teoria estudada em *1. Fundamentos da Cultura DevOps*, a equipe de Desenvolvimento (Dev) é cobrada por velocidade de entrega, lançamento contínuo de novas funcionalidades e mudanças dinâmicas no sistema.
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e III, apenas". De acordo com a teoria estudada em *1.4 As Quatro Métricas DORA (DevOps Research and Assessment)*, as métricas DORA resultam de quase uma década de pesquisas empíricas e rigor estatístico conduzidas pelo grupo fundado por Nicole Forsgren, Jez Humble e Gene Kim (posteriormente incorporado ao Google Cloud).
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I, apenas". De acordo com a teoria estudada em *1.2 O Framework C.A.L.M.S.*, l (Lean - Princípios Enxutos): Aplicação dos princípios da manufatura enxuta (Sistema Toyota de Produção) ao ciclo de software: redução drástica de desperdícios, entregas frequentes em lotes pequenos (*small batch sizes*), redução do tempo de fila e limitação estrita do trabalho em progresso (*WIP - Work in Progress*).
> - **E)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "III, apenas". De acordo com a teoria estudada em *1.3 As Três Vias do DevOps*, a Segunda Via (O Princípio do Feedback): Busca encurtar e amplificar continuamente os ciclos de retorno da direita (Operações e Clientes em Produção) para a esquerda (Desenvolvimento).
>
> **Gabarito: A**

---

### Teste 172
**(IBFC – TJ-MG – Analista Judiciario Classe C Analista de Tecnologia da Informacao – 2022)**
Dado os três conceitos básicos sobre o ITIL v4 abaixo, assinale a alternativa que corresponda respectivamente a denominação referente a cada um desses conceitos: 1. Acréscimo, modificação ou remoção de qualquer elemento que possa afetar direta ou indiretamente os serviços. 2. É uma interrupção não planejada de um serviço de TI ou uma redução da qualidade de um serviço de TI. 3. Trata-se de uma chamada para a ação de serviço que tenha sido acordada como parte normal da entrega de serviço.

* **A)** 1.INCIDENTE - 2.MUDANÇA - 3.REQUISIÇÃO de SERVIÇO
* **B)** 1.MUDANÇA - 2.INCIDENTE - 3.REQUISIÇÃO de SERVIÇO
* **C)** 1.INCIDENTE - 2.REQUISIÇÃO de SERVIÇO - 3.MUDANÇA
* **D)** 1.MUDANÇA - 2.REQUISIÇÃO de SERVIÇO - 3.INCIDENTE
* **E)** 1.REQUISIÇÃO de SERVIÇO - 2.INCIDENTE - 3.MUDANÇA

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "1.INCIDENTE - 2.MUDANÇA - 3.REQUISIÇÃO de SERVIÇO". De acordo com a teoria estudada em *3.5 Feature Flags / Feature Toggles e Dark Launching*, dark Launching: O código novo é implantado em produção e passa a ser executado em segundo plano de forma invisível aos usuários (ex.: para cada requisição recebida, o sistema envia uma chamada assíncrona ao novo algoritmo fiscal em paralelo, comparando os resultados e medindo o impacto em banco de dados sem exibir as saídas na interface do usuário).
> - **B)** **Correta.** Conforme fundamentado na seção *1.4 As Quatro Métricas DORA (DevOps Research and Assessment)* deste guia, time to Restore Service (MTTR): Stability (Estabilidade) — Tempo médio necessário para restabelecer a operação normal do serviço quando ocorre um incidente de indisponibilidade em produção. — Menos de 1 hora (recuperação ágil via rollback ou fix-forward). — Mais de 1 semana a 1 mês. Dessa forma, está plenamente correta a assertiva da banca (IBFC – TJ-MG/2022) ao estabelecer que "1.MUDANÇA - 2.INCIDENTE - 3.REQUISIÇÃO de SERVIÇO".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "1.INCIDENTE - 2.REQUISIÇÃO de SERVIÇO - 3.MUDANÇA". De acordo com a teoria estudada em *2.3 Implantação Contínua (Continuous Deployment): Promoção Automática para Produção*, toda modificação que passa com sucesso em 100% dos estágios automatizados do pipeline (CI + Staging + Gates de Segurança e Qualidade) é promovida de forma instantânea e automática para os servidores de produção.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "1.MUDANÇA - 2.REQUISIÇÃO de SERVIÇO - 3.INCIDENTE". De acordo com a teoria estudada em *1.3 As Três Vias do DevOps*, formalizadas por Gene Kim, Kevin Behr e George Spafford nas obras seminais *The Phoenix Project* e *The DevOps Handbook*, as Três Vias estruturam as práticas dinâmicas da entrega contínua.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "1.REQUISIÇÃO de SERVIÇO - 2.INCIDENTE - 3.MUDANÇA". De acordo com a teoria estudada em *1.2 O Framework C.A.L.M.S.*, l (Lean - Princípios Enxutos): Aplicação dos princípios da manufatura enxuta (Sistema Toyota de Produção) ao ciclo de software: redução drástica de desperdícios, entregas frequentes em lotes pequenos (*small batch sizes*), redução do tempo de fila e limitação estrita do trabalho em progresso (*WIP - Work in Progress*).
>
> **Gabarito: B**

---

### Teste 173
**(FCC – TRT-13 – Analista Judiciario Tecnologia da Informacao – 2014)**
Considere: I. Aceitar mudanças de requisitos, mesmo no fim do desenvolvimento. Processos ágeis se adequam a mudanças, para que o cliente possa tirar vantagens competitivas. II. Pessoas relacionadas a negócios e desenvolvedores devem trabalhar separadamente durante todo o curso do projeto. III. O método mais eficiente e eficaz de transmitir informações para e por dentro de um time de desenvolvimento, é por meio do correio eletrônico. IV. A maior prioridade é satisfazer o cliente através da entrega adiantada e contínua de software de valor. É coerente com os princípios que embasam o manifesto ágil (desenvolvimento ágil de software) o que consta APENAS em

* **A)** I, II e III.
* **B)** I e III.
* **C)** I e IV.
* **D)** II e IV.
* **E)** III e IV.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I, II e III". De acordo com a teoria estudada em *1.4 As Quatro Métricas DORA (DevOps Research and Assessment)*, time to Restore Service (MTTR): Stability (Estabilidade) — Tempo médio necessário para restabelecer a operação normal do serviço quando ocorre um incidente de indisponibilidade em produção. — Menos de 1 hora (recuperação ágil via rollback ou fix-forward). — Mais de 1 semana a 1 mês.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I e III". De acordo com a teoria estudada em *1. Fundamentos da Cultura DevOps*, a equipe de Desenvolvimento (Dev) é cobrada por velocidade de entrega, lançamento contínuo de novas funcionalidades e mudanças dinâmicas no sistema.
> - **C)** **Correta.** Conforme fundamentado na seção *1.3 As Três Vias do DevOps* deste guia, a Primeira Via (O Princípio do Fluxo): Tem por objetivo acelerar a velocidade com que o valor transita da esquerda (Desenvolvimento e Requisitos) para a direita (Operações e Produção). Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT-13/2014) ao estabelecer que "I e IV".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "II e IV". De acordo com a teoria estudada em *2.2 Entrega Contínua (Continuous Delivery): O Release Candidate Permanente*, característica Definitiva: O software é mantido em um estado permanentemente pronto para entrar em produção (*deployable at any time*).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "III e IV". De acordo com a teoria estudada em *1.1 Eliminação do Muro da Confusão e Responsabilidade Compartilhada*, o DevOps quebra essa barreira através da fusão de processos, práticas colaborativas e ferramentas automatizadas, estabelecendo o princípio da responsabilidade compartilhada de ponta a ponta (*"You build it, you run it"*, sintetizado por Werner Vogels, CTO da Amazon).
>
> **Gabarito: C**

---

## 2. O Espectro de Automação: CI vs. CD (Delivery vs. Deployment)

A automação da esteira de publicação de software é composta por três patamares progressivos de maturidade. Compreender o limite exato de escopo e responsabilidade entre eles é matéria clássica em provas da FCC.

```mermaid
flowchart TD
    subgraph CI["Integração Contínua (CI)"]
        A["Commit / Push no Git"] --> B["Build Automatizado"]
        B --> C["Testes de Unidade e Lint"]
    end
    
    subgraph CD_Delivery["Entrega Contínua (Continuous Delivery)"]
        C --> D["Empacotamento e Testes de Integração / Aceite"]
        D --> E["Deploy Automatizado em Staging / Homologação"]
        E --> F{"Aprovação Manual<br/>(Gate de Negócio)"}
    end
    
    subgraph CD_Deployment["Implantação Contínua (Continuous Deployment)"]
        E -.->|Se Continuous Deployment: SEM GATILHO MANUAL| G["Deploy Automático em Produção"]
    end
    
    F -->|Aprovado por Humano| G
```

### 2.1 Integração Contínua (CI): Boas Práticas, Trunk-Based e Princípio Stop the Line

Conforme consagrado por Martin Fowler, a **Integração Contínua (*Continuous Integration*)** é a prática de engenharia na qual os membros de um time integram suas alterações de código-fonte ao branch principal do repositório com alta frequência — preferencialmente **ao menos uma vez por dia**.

**Práticas Fundamentais de CI:**

1. **Repositório Central Único:** Todo o código, configurações e scripts de build residem em um repositório centralizado versionado.
2. **Desenvolvimento em Tronco (*Trunk-Based Development*) ou Feature Branches Curtas:** Evita-se a criação de branches de desenvolvimento isoladas de longa duração. Branches que duram semanas acumulam conflitos de mesclagem complexos (*merge hell*). No modelo trunk-based, merges acontecem em ciclos diários.
3. **Build Automatizado Autocontido:** A compilação da aplicação deve ser disparada automaticamente a cada push ou commit, operando a partir de um único comando de script (ex.: `mvn clean package`, `npm run build`), sem intervenção manual de ambiente.
4. **Execução Obrigatória de Testes de Unidade e Linting:** A esteira de CI roda linters de código e baterias de testes unitários rápidos. A meta é que a validação de CI execute em menos de 10 minutos para não bloquear o fluxo do desenvolvedor.
5. **O Princípio *Stop the Line* (Corda de Andon):** Inspirado no modelo de produção enxuta, se um commit quebra o build no branch principal, a equipe inteira deve suspender novas tarefas e priorizar a resolução imediata da quebra antes de efetuar novos merges. Manter o branch principal permanentemente verde (*always green*) é mandatório.

### 2.2 Entrega Contínua (Continuous Delivery): O Release Candidate Permanente

A **Entrega Contínua (*Continuous Delivery*)** expande o escopo da Integração Contínua para além dos testes unitários e da compilação:

- Ela automatiza toda a preparação da aplicação até o limiar de produção. Cada alteração que passa pelos testes é empacotada em uma imagem ou binário e implantada automaticamente em ambientes de homologação (*staging*, *pre-prod*) estritamente idênticos à produção.
- Nesse ambiente, o sistema é submetido a baterias automatizadas de testes de integração, testes de aceitação de negócio, testes de segurança estática e dinâmica, e testes de estresse/carga.
- **Característica Definitiva:** O software é mantido em um estado **permanentemente pronto para entrar em produção (*deployable at any time*)**. Contudo, a efetiva promoção para o ambiente produtivo real depende de um **gatilho manual** (*Manual Gate* / decisão de negócio, liberação por diretoria ou janela de release programada).

### 2.3 Implantação Contínua (Continuous Deployment): Promoção Automática para Produção

A **Implantação Contínua (*Continuous Deployment*)** representa o nível máximo de maturidade na automação da esteira de entrega:

- Elimina-se completamente qualquer intervenção humana, aprovação de comitê ou gatilho manual.
- Toda modificação que passa com sucesso em 100% dos estágios automatizados do pipeline (CI + Staging + Gates de Segurança e Qualidade) é **promovida de forma instantânea e automática para os servidores de produção**.
- **Pré-requisitos Mandatórios:** Exige cobertura massiva de testes automatizados, esteiras de análise estática sem falso-positivo, arquitetura resiliente com rollback automático disparado por telemetria e estratégias avançadas de liberação (como Canary ou Blue-Green).

### 2.4 Tabela Comparativa Detalhada: CI vs. Continuous Delivery vs. Continuous Deployment

| Característica | Integração Contínua (CI) | Entrega Contínua (Continuous Delivery) | Implantação Contínua (Continuous Deployment) |
| :--- | :--- | :--- | :--- |
| **Objetivo Primário** | Validar que o código de múltiplos desenvolvedores compila e se integra sem quebrar funcionalidades existentes. | Assegurar que o software está em **estado permanente de prontidão para deploy produtivo** a qualquer momento. | Disponibilizar novas alterações para os usuários finais em produção de maneira imediata e ininterrupta. |
| **Frequência de Integração** | Diária ou múltiplas vezes ao dia no branch principal (`main`/`trunk`). | Contínua (cada lote de commits aprovados gera um novo *release candidate*). | Contínua (fluxo contínuo do commit até o servidor de produção). |
| **Escopo dos Testes** | Análise sintática (linters), tipos estáticos e testes de unidade rápidos. | Testes de integração, de contrato, ponta a ponta (E2E), segurança (SAST/DAST) e carga. | Idem ao Delivery, acrescido de monitoramento ativo de telemetria e testes de saúde em produção. |
| **Ambientes Envolvidos** | Runners de CI efêmeros (contêineres de build). | Runners de CI + Ambientes de Teste, QA e Staging/Homologação idênticos à produção. | Toda a cadeia de ambientes estendendo-se até o cluster de **Produção Real**. |
| **Gatilho de Produção** | Não contempla publicação em produção. | **GATILHO MANUAL** (Decisão humana, clique em painel, aprovação de negócio). | **100% AUTOMÁTICO** (Nenhuma intervenção humana; commit aprovado nos testes vai direto para produção). |
| **Fator Crítico de Sucesso** | Testes rápidos (< 10 min); disciplina estrita de resolução imediata de builds quebrados. | Automação total de provisionamento de staging; paridade estrita de infraestrutura dev/prod. | Monitoramento e observabilidade em tempo real com mecanismo de **rollback automatizado** sem intervenção humana. |

> ⭐ **IMPORTANTE / REGRA DE OURO:**  
> A fronteira conceitual cobrada em concursos entre **Continuous Delivery** e **Continuous Deployment** reside **exclusivamente no gatilho para o ambiente de Produção**:
>
> - **Continuous Delivery:** A publicação em produção requer acionamento por **aprovação manual humana**.
> - **Continuous Deployment:** A publicação em produção é **totalmente automatizada via software**, sem cliques ou autorizações manuais.

---

### Teste 174
**(FCC – TRT-6 – Analista Judiciario Apoio Especializado Tecnologia da Informacao – 2012)**
Existem diversos modelos CMMI disponíveis, gerados a partir do CMMI Framework. Em consequência disso, é preciso estar preparado para decidir qual modelo CMMI melhor atende às necessidades de melhoria de processos de uma organização específica. É possível selecionar uma representação, contínua ou em estágios, e determinar as áreas de conhecimento que serão incluídas no modelo que essa organização irá utilizar. Sobre essas representações, considere: I. Oferecerá uma sequência comprovada de melhorias, começando com práticas básicas de gerenciamento e progredindo por um caminho pré-definido e comprovado de níveis sucessivos, cada um servindo como base para o próximo. II. Oferecerá uma classificação única que resume os resultados de avaliações e permite comparações entre organizações. III. Possibilitará comparações dentro e entre organizações em uma área de processo em termos de área de processo ou pela comparação de resultados através do uso de estágios equivalentes. IV. Permitirá comparação dentro da organização e entre organizações pelo uso de níveis de maturidade. V. Permitirá selecionar a sequência de melhorias que melhor atende aos objetivos de negócios e reduz as áreas de risco da organização. Os itens apresentados referem-se, respectivamente, às representações

* **A)** contínua, contínua, em estágios, contínua, em estágios.
* **B)** em estágios, em estágios, contínua, em estágios, contínua.
* **C)** contínua, em estágios, em estágios, contínua, em estágios.
* **D)** em estágios, contínua, em estágios, contínua, em estágios.
* **E)** contínua, em estágios, contínua, em estágios, contínua.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "contínua, contínua, em estágios, contínua, em estágios". De acordo com a teoria estudada em *4. Estrutura, Estágios e Segurança de Pipelines (DevSecOps)*, a construção de um pipeline de entrega contínua robusto organiza as atividades em estágios lógicos estritamente encadeados, impedindo o avanço de artefatos defeituosos ou inseguros.
> - **B)** **Correta.** Conforme fundamentado na seção *2.3 Implantação Contínua (Continuous Deployment): Promoção Automática para Produção* deste guia, toda modificação que passa com sucesso em 100% dos estágios automatizados do pipeline (CI + Staging + Gates de Segurança e Qualidade) é promovida de forma instantânea e automática para os servidores de produção. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT-6/2012) ao estabelecer que "em estágios, em estágios, contínua, em estágios, contínua".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "contínua, em estágios, em estágios, contínua, em estágios". De acordo com a teoria estudada em *2.1 Integração Contínua (CI): Boas Práticas, Trunk-Based e Princípio Stop the Line*, build Automatizado Autocontido: A compilação da aplicação deve ser disparada automaticamente a cada push ou commit, operando a partir de um único comando de script (ex.: `mvn clean package`, `npm run build`), sem intervenção manual de ambiente.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "em estágios, contínua, em estágios, contínua, em estágios". De acordo com a teoria estudada em *1.3 As Três Vias do DevOps*, o conhecimento gerado a partir de sucessos e falhas locais é sistematicamente compartilhado e incorporado às práticas institucionais de toda a organização.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "contínua, em estágios, contínua, em estágios, contínua". De acordo com a teoria estudada em *2.1 Integração Contínua (CI): Boas Práticas, Trunk-Based e Princípio Stop the Line*, no modelo trunk-based, merges acontecem em ciclos diários.
>
> **Gabarito: B**

---

### Teste 175
**(FGV – TCE-GO – Analista de Controle Externo Tecnologia da Informacao – 2024)**
Avalie as seguintes afirmativas no contexto de práticas e metodologias de deploy em desenvolvimento mobile: I. A aplicação de Continuous Integration (CI) em aplicativos mobile responsivos é uma prática que visa a fusão e teste do código apenas ao final de cada sprint; II. Continuous Delivery (CD) é parte da filosofia "Mobile First" e permite que toda mudança de código seja automaticamente disponibilizada para os usuários finais, sem a necessidade de aprovação das equipes de operações; III. DevSecOps é a integração da segurança no processo de desenvolvimento de software desde o início sem comprometer a velocidade de entrega. Está correto o que se afirma em

* **A)** I, apenas.
* **B)** II e III, apenas.
* **C)** III, apenas.
* **D)** I, II e III.
* **E)** I e II, apenas. Redes de Computadores e Sistemas Operacionais Redes de Computadores

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I, apenas". De acordo com a teoria estudada em *2.1 Integração Contínua (CI): Boas Práticas, Trunk-Based e Princípio Stop the Line*, conforme consagrado por Martin Fowler, a Integração Contínua (*Continuous Integration*) é a prática de engenharia na qual os membros de um time integram suas alterações de código-fonte ao branch principal do repositório com alta frequência — preferencialmente ao menos uma vez por dia.
> - **B)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II e III, apenas". De acordo com a teoria estudada em *2.2 Entrega Contínua (Continuous Delivery): O Release Candidate Permanente*, ela automatiza toda a preparação da aplicação até o limiar de produção.
> - **C)** **Correta.** Conforme fundamentado na seção *2.4 Tabela Comparativa Detalhada: CI vs. Continuous Delivery vs. Continuous Deployment* deste guia, objetivo Primário: Validar que o código de múltiplos desenvolvedores compila e se integra sem quebrar funcionalidades existentes. — Assegurar que o software está em estado permanente de prontidão para deploy produtivo a qualquer momento. — Disponibilizar novas alterações para os usuários finais em produção de maneira imediata e ininterrupta. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE-GO/2024) ao estabelecer que "III, apenas".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I, II e III". De acordo com a teoria estudada em *2.1 Integração Contínua (CI): Boas Práticas, Trunk-Based e Princípio Stop the Line*, build Automatizado Autocontido: A compilação da aplicação deve ser disparada automaticamente a cada push ou commit, operando a partir de um único comando de script (ex.: `mvn clean package`, `npm run build`), sem intervenção manual de ambiente.
> - **E)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e II, apenas. Redes de Computadores e Sistemas Operacionais Redes de Computadores". De acordo com a teoria estudada em *1.1 Eliminação do Muro da Confusão e Responsabilidade Compartilhada*, desenvolvedores assumem a corresponsabilidade pelo comportamento da aplicação em produção, projetando sistemas já preparados para observabilidade, diagnóstico e tolerância a falhas.
>
> **Gabarito: C**

---

## 3. Estratégias Modernas de Publicação (Deployment Strategies)

Em infraestruturas modernas baseadas em contêineres e microsserviços, a substituição de versões deve buscar a eliminação de indisponibilidade (*zero downtime*), a mitigação do raio de impacto (*blast radius*) e a rapidez de reversão (*rollback*).

### 3.1 Recreate (Recriação)

- **Mecanismo:** Todas as instâncias da versão antiga ($V1$) são terminadas simultaneamente antes que qualquer instância da nova versão ($V2$) seja inicializada.
- **Vantagens:** É a abordagem mais simples de configurar; não exige retrocompatibilidade de banco de dados, pois nunca coexistem versões diferentes executando simultaneamente.
- **Desvantagens:** Gera **indisponibilidade obrigatória (*downtime*)** para os usuários durante o intervalo de desligamento da $V1$ e inicialização completa da $V2$. Inadmissível para sistemas críticos de fiscalização e arrecadação fiscal.

### 3.2 Rolling Update (Atualização Progressiva)

- **Mecanismo:** A substituição ocorre de forma gradual e incremental. Em um cluster com 4 réplicas de contêineres, uma instância antiga é terminada e substituída por uma nova réplica $V2$. Uma vez que a $V2$ passa nos testes de integridade (*readiness probes*), a próxima instância antiga é substituída, até que 100% dos nós estejam executando a versão $V2$.
- **Vantagens:** Garante **zero downtime** sem a necessidade de alocar o dobro de recursos de infraestrutura. É a estratégia nativa padrão em orquestradores como o Kubernetes (`strategy: RollingUpdate`).
- **Desvantagens:** Durante o processo de transição, instâncias da $V1$ e da $V2$ respondem concomitantemente às requisições dos usuários, exigindo que o banco de dados e as APIs sejam rigorosamente retrocompatíveis. Em caso de falha no meio do processo, o rollback demanda tempo para reverter progressivamente os nós alterados.

```mermaid
flowchart LR
    subgraph RollingUpdate["Rolling Update (4 réplicas)"]
        direction TB
        T0["Instante 0: [V1] [V1] [V1] [V1] (100% V1)"]
        T1["Instante 1: [V1] [V1] [V1] [V2] (75% V1, 25% V2)"]
        T2["Instante 2: [V1] [V1] [V2] [V2] (50% V1, 50% V2)"]
        T3["Instante 3: [V2] [V2] [V2] [V2] (100% V2)"]
        T0 --> T1 --> T2 --> T3
    end
```

### 3.3 Blue-Green Deployment (Azul-Verde)

- **Mecanismo:** Mantêm-se dois ambientes de produção fisicamente idênticos e isolados: o ambiente **Blue** (que está ativo atendendo 100% das requisições reais dos usuários) e o ambiente **Green** (que permanece ocioso em modo de espera).
- **Fluxo Operacional:** A nova versão do software ($V2$) é instalada no ambiente Green. Nesse ambiente isolado, a equipe executa testes de fumaça (*smoke tests*), testes de carga e validações funcionais completas sem impactar os usuários reais.
- **Comutação e Rollback:** Quando a versão Green é plenamente aprovada, o balanceador de carga (*Load Balancer*) ou controlador de entrada (*Ingress*) chaveia 100% do tráfego para Green, tornando-o o ambiente ativo. O ambiente Blue passa a ser o novo ambiente inativo. Caso surja uma falha catastrófica imprevista, o **rollback é instantâneo**: basta reverter a rota do balanceador de carga de volta para Blue em questão de milissegundos.
- **Desvantagens:** Exige infraestrutura computacional duplicada, elevando os custos de nuvem ou de servidores locais.

```mermaid
flowchart TD
    USERS["Usuários Finais"] --> ROUTER["Roteador / Load Balancer"]
    ROUTER -->|"100% do Tráfego Ativo"| BLUE["Ambiente Blue (V1 - Atual Ativo)"]
    ROUTER -.->|"0% de Tráfego (Testes de Homologação)"| GREEN["Ambiente Green (V2 - Novo Release)"]
    
    style BLUE fill:#bbdefb,stroke:#1976d2,stroke-width:2px
    style GREEN fill:#c8e6c9,stroke:#388e3c,stroke-width:2px
```

### 3.4 Canary Deployment (Canário)

- **Origem do Termo:** Alusão histórica aos canários utilizados nas minas de carvão britânicas para detectar vazamentos de gases tóxicos antes que afetassem os operários.
- **Mecanismo:** A nova versão ($V2$) é colocada no ar paralelamente à versão estável ($V1$), mas recebe apenas uma fração diminuta do tráfego real dos usuários (tipicamente entre 1% e 5%), enquanto a $V1$ continua atendendo os 95% restantes. O tráfego do canário pode ser roteado por amostragem percentual randômica, por localização geográfica ou por grupos de usuários específicos (ex.: servidores internos).
- **Monitoramento e Expansão:** Durante a exposição do canário, sistemas de telemetria analisam ativamente métricas como taxa de erros HTTP 5xx, consumo de memória e latência de resposta. Se o canário mantiver estabilidade perfeita, a proporção de tráfego é ampliada de forma progressiva (ex.: 5% $\rightarrow$ 25% $\rightarrow$ 50% $\rightarrow$ 100%).
- **Mitigação do Raio de Impacto (*Blast Radius*):** Se o canário apresentar anomalias ou falhas, o roteamento para ele é imediatamente interrompido, afetando apenas uma fração insignificante de requisições.

```mermaid
flowchart TD
    USERS["Usuários Finais"] --> LB["Balanceador de Carga / Service Mesh"]
    LB -->|"95% do Tráfego"| STABLE["Versão Estável V1 (Produção)"]
    LB -->|"5% do Tráfego (Amostragem)"| CANARY["Versão Canário V2 (Monitorada)"]
    
    style STABLE fill:#e1f5fe,stroke:#0288d1
    style CANARY fill:#fff9c4,stroke:#fbc02d
```

### 3.5 Feature Flags / Feature Toggles e Dark Launching

- **Feature Flags (ou Toggles):** Mecanismo de controle em nível de código-fonte que permite encapsular novas funcionalidades em blocos condicionais (`if (featureManager.isEnabled("NOVO_MODULO_FISCAL")) { .. }`). Permite desacoplar a implantação do código (*deployment*) da ativação comercial do recurso (*release*). Um código pode estar rodando em produção com a funcionalidade desligada no servidor de configuração remota, sendo ativada sob demanda sem a necessidade de novo pipeline de deploy.
- **Dark Launching:** O código novo é implantado em produção e passa a ser executado em segundo plano de forma invisível aos usuários (ex.: para cada requisição recebida, o sistema envia uma chamada assíncrona ao novo algoritmo fiscal em paralelo, comparando os resultados e medindo o impacto em banco de dados sem exibir as saídas na interface do usuário).

> 🚨 **ALERTA DE PROVA / PEGADINHA FCC:**  
> A FCC adora comparar as características de risco e infraestrutura:
>
> - **Blue-Green:** Comutação total de 100% de uma vez; rollback **instantâneo** via balanceador; exige **duplicação integral de infraestrutura**.
> - **Canary:** Comutação **fracionada/percentual** (ex.: 5% inicial); focado em **reduzir o blast radius** e validar métricas de saúde com tráfego real.
> - **Rolling Update:** Substituição progressiva de instâncias/pods; **zero downtime** sem duplicação de infraestrutura, mas exige convivência temporária de versões.

---

### Teste 176
**(FCC – TRT-14 – Analista Judiciario Apoio Especializado Tecnologia da Informacao – 2016)**
A palavra latter, sublinhada no 3o parágrafo, refere-se a

* **A)** Dropbox.
* **B)** OneDrive.
* **C)** Google Drive.
* **D)** Docs.
* **E)** Sheets.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Dropbox". De acordo com a teoria estudada em *5.1 GitHub Actions: Workflows, Events, Jobs, Steps, Runners e Secrets*, para criar dependência sequencial ou construir um grafo acíclico direcionado (DAG), utiliza-se a palavra-chave `needs: [nome_do_job]`.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "OneDrive". De acordo com a teoria estudada em *3. Estratégias Modernas de Publicação (Deployment Strategies)*, em infraestruturas modernas baseadas em contêineres e microsserviços, a substituição de versões deve buscar a eliminação de indisponibilidade (*zero downtime*), a mitigação do raio de impacto (*blast radius*) e a rapidez de reversão (*rollback*).
> - **C)** **Correta.** Conforme fundamentado na seção *1.4 As Quatro Métricas DORA (DevOps Research and Assessment)* deste guia, as métricas DORA resultam de quase uma década de pesquisas empíricas e rigor estatístico conduzidas pelo grupo fundado por Nicole Forsgren, Jez Humble e Gene Kim (posteriormente incorporado ao Google Cloud). Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT-14/2016) ao estabelecer que "Google Drive".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Docs". De acordo com a teoria estudada em *3.1 Recreate (Recriação)*, mecanismo: Todas as instâncias da versão antiga (\$V1\$) são terminadas simultaneamente antes que qualquer instância da nova versão (\$V2\$) seja inicializada.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Sheets". De acordo com a teoria estudada em *3.1 Recreate (Recriação)*, vantagens: É a abordagem mais simples de configurar; não exige retrocompatibilidade de banco de dados, pois nunca coexistem versões diferentes executando simultaneamente.
>
> **Gabarito: C**

---

### Teste 177
**(FGV – TJ-SC – Analista Administrativo – 2026)**
A navegação segura na internet via protocolo HTTPS (Hypertext Transfer Protocol Secure) exige uma interação complexa entre hardware, software e protocolos de rede. Considerando o fluxo de processamento de uma requisição HTTPS em um sistema computacional moderno, é correto afirmar que

* **A)** o protocolo HTTPS opera exclusivamente na camada de transporte do modelo OSI, substituindo o TCP para garantir que a criptografia seja processada diretamente pelo hardware da placa de rede (NIC).
* **B)** durante o handshake do TLS, o sistema operacional utiliza chamadas de sistema para acessar funções criptográficas e gerenciar sockets de rede, permitindo que o navegador estabeleça um canal seguro sobre a pilha TCP/IP.
* **C)** a criptografia assimétrica utilizada no HTTPS é uma função nativa do firmware do roteador, o que desonera a CPU do computador cliente de realizar cálculos matemáticos complexos.
* **D)** o endereçamento IP (camada de rede do modelo OSI) é o responsável por garantir a integridade dos certificados digitais, enquanto o protocolo HTTPS gerencia o endereçamento físico (MAC Address).
* **E)** ao utilizar HTTPS, o sistema operacional desativa a memória virtual para impedir que chaves criptográficas sejam gravadas em disco (swap), priorizando o processamento na Unidade de Controle.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "o protocolo HTTPS opera exclusivamente na camada de transporte do modelo OSI, substituindo o TCP para garantir que...". De acordo com a teoria estudada em *4.1 Estágios Canônicos: Lint, Análise Estática (SAST/SCA), Build, Testes e Registry*, deploy e *Smoke Tests*: Implantação nos servidores de destino e disparo de testes de fumaça rápidos para verificar a disponibilidade de portas de rede e rotas de saúde (`/healthz`).
> - **B)** **Correta.** Conforme fundamentado na seção *3.5 Feature Flags / Feature Toggles e Dark Launching* deste guia, dark Launching: O código novo é implantado em produção e passa a ser executado em segundo plano de forma invisível aos usuários (ex.: para cada requisição recebida, o sistema envia uma chamada assíncrona ao novo algoritmo fiscal em paralelo, comparando os resultados e medindo o impacto em banco de dados sem exibir as saídas na interface do usuário). Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ-SC/2026) ao estabelecer que "durante o handshake do TLS, o sistema operacional utiliza chamadas de sistema para acessar funções criptográficas...".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "a criptografia assimétrica utilizada no HTTPS é uma função nativa do firmware do roteador, o que desonera a CPU do...". De acordo com a teoria estudada em *3.3 Blue-Green Deployment (Azul-Verde)*, fluxo Operacional: A nova versão do software (\$V2\$) é instalada no ambiente Green. Nesse ambiente isolado, a equipe executa testes de fumaça (*smoke tests*), testes de carga e validações funcionais completas sem impactar os usuários reais.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "o endereçamento IP (camada de rede do modelo OSI) é o responsável por garantir a integridade dos certificados...". De acordo com a teoria estudada em *5.3 Jenkins: Arquitetura Controller-Agent, Declarative Pipeline e Scripted Pipeline*, declarative Pipeline (Estilo Moderno e Padronizado): Utiliza uma sintaxe declarativa estrita e de fácil leitura, iniciando obrigatoriamente pelo bloco raiz `pipeline { .. }`.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "ao utilizar HTTPS, o sistema operacional desativa a memória virtual para impedir que chaves criptográficas sejam...". De acordo com a teoria estudada em *3.4 Canary Deployment (Canário)*, monitoramento e Expansão: Durante a exposição do canário, sistemas de telemetria analisam ativamente métricas como taxa de erros HTTP 5xx, consumo de memória e latência de resposta.
>
> **Gabarito: B**

---

### Teste 178
**(FGV – TRF-1 – Analista Judiciario Area Apoio Especializado Especialidade Suporte Em Tecnologia da Informacao – 2024)**
Um usuário abriu um chamado questionando por que, ao realizar um download a partir do servidor de arquivos, o tráfego estava sendo encaminhado por dois caminhos distintos. Márcia, analista do TRF, explicou que o protocolo de roteamento utilizado é o OSPF, que identificou dois caminhos com custos iguais. Durante o encaminhamento dos pacotes, o tráfego é distribuído entre esses caminhos, promovendo o balanceamento de carga. A técnica mencionada por Márcia é chamada de:

* **A)** ICMP;
* **B)** ECMP;
* **C)** MOSPF;
* **D)** roteamento estático;
* **E)** roteamento dinâmico.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "ICMP". De acordo com a teoria estudada em *3.5 Feature Flags / Feature Toggles e Dark Launching*, dark Launching: O código novo é implantado em produção e passa a ser executado em segundo plano de forma invisível aos usuários (ex.: para cada requisição recebida, o sistema envia uma chamada assíncrona ao novo algoritmo fiscal em paralelo, comparando os resultados e medindo o impacto em banco de dados sem exibir as saídas na interface do usuário).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "ECMP". De acordo com a teoria estudada em *3.5 Feature Flags / Feature Toggles e Dark Launching*, um código pode estar rodando em produção com a funcionalidade desligada no servidor de configuração remota, sendo ativada sob demanda sem a necessidade de novo pipeline de deploy.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "MOSPF". De acordo com a teoria estudada em *3.3 Blue-Green Deployment (Azul-Verde)*, comutação e Rollback: Quando a versão Green é plenamente aprovada, o balanceador de carga (*Load Balancer*) ou controlador de entrada (*Ingress*) chaveia 100% do tráfego para Green, tornando-o o ambiente ativo.
> - **D)** **Correta.** Conforme fundamentado na seção *3.4 Canary Deployment (Canário)* deste guia, mitigação do Raio de Impacto (*Blast Radius*): Se o canário apresentar anomalias ou falhas, o roteamento para ele é imediatamente interrompido, afetando apenas uma fração insignificante de requisições. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRF-1/2024) ao estabelecer que "roteamento estático".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "roteamento dinâmico". De acordo com a teoria estudada em *3.3 Blue-Green Deployment (Azul-Verde)*, mecanismo: Mantêm-se dois ambientes de produção fisicamente idênticos e isolados: o ambiente Blue (que está ativo atendendo 100% das requisições reais dos usuários) e o ambiente Green (que permanece ocioso em modo de espera).
>
> **Gabarito: D**

---

## 4. Estrutura, Estágios e Segurança de Pipelines (DevSecOps)

A construção de um pipeline de entrega contínua robusto organiza as atividades em estágios lógicos estritamente encadeados, impedindo o avanço de artefatos defeituosos ou inseguros.

### 4.1 Estágios Canônicos: Lint, Análise Estática (SAST/SCA), Build, Testes e Registry

```mermaid
flowchart LR
    A["1. Code & Lint"] --> B["2. SAST & SCA<br/>(Segurança Estática)"]
    B --> C["3. Build & Compilação"]
    C --> D["4. Testes Automatizados<br/>(Unit, Int, Regressão)"]
    D --> E["5. Publicação de Imagem<br/>(Container Registry)"]
    E --> F["6. Deploy & Smoke Tests<br/>(Staging / Prod)"]
```

1. **Linting e Verificação de Estilo:** Análise léxica rápida para garantir uniformidade e detectar erros sintáticos elementares sem compilar o código (ex.: ESLint, SonarLint, flake8).
2. **DevSecOps - SAST (*Static Application Security Testing*) e SCA (*Software Composition Analysis*):**
    - **SAST:** Varredura estática no código-fonte em busca de falhas de segurança conhecidas (como SQL Injection, Cross-Site Scripting - XSS, uso de funções obsoletas). Ex.: SonarQube, Checkmarx.
    - **SCA:** Inspeção do grafo de dependências e bibliotecas externas de terceiros em busca de vulnerabilidades catalogadas na base CVE (*Common Vulnerabilities and Exposures*). Ex.: OWASP Dependency-Check, Snyk, Trivy.

3. **Build e Compilação:** Compilação do código-fonte em artefatos binários executáveis (`.jar`, `.war`, binários Go) ou construção de imagens de contêiner imutáveis via Dockerfile.
4. **Testes Automatizados:** Execução encadeada de suítes de testes automatizados organizados conforme a pirâmide de testes.
5. **Armazenamento em *Registry* de Artefatos:** Publicação segura do artefato aprovado em repositório centralizado de binários (como Docker Hub corporativo, GitHub Container Registry, Harbor ou Nexus).
6. **Deploy e *Smoke Tests*:** Implantação nos servidores de destino e disparo de testes de fumaça rápidos para verificar a disponibilidade de portas de rede e rotas de saúde (`/healthz`).

### 4.2 Pirâmide de Testes Automatizados no Pipeline

Proposta por Mike Cohn, a pirâmide de testes orienta a distribuição ótima dos testes automatizados na esteira de integração contínua:

1. **Base da Pirâmide - Testes de Unidade (Unitários):** Representam a esmagadora maioria dos testes (cerca de 70%). Testam classes e funções isoladas com uso de *mocks* e *stubs*. São extremamente rápidos de executar (milissegundos) e possuem baixo custo de manutenção.
2. **Meio da Pirâmide - Testes de Integração e de Contrato:** Testam a comunicação entre componentes integrados (como a camada de persistência com o banco de dados em contêiner de teste ou contratos de API REST via Pact). Mais lentos que os testes unitários, demandam inicialização de serviços.
3. **Topo da Pirâmide - Testes de Ponta a Ponta (E2E / Interface do Usuário):** Simulam a jornada completa do usuário final em navegadores ou clientes de API. São testes lentos, caros de manter e sujeitos a falhas intermitentes (*flaky tests*), devendo representar a menor fatia da suíte de automação (cerca de 10%).

---

### Teste 179
**(FCC – TRT-9 – Analista Judiciario Apoio Especializado Tecnologia da Informacao – 2015)**
Usa-se um framework de testes iniciais automatizados para escrever os testes para uma nova funcionalidade antes que ela seja implementada, pois acredita-se que escrever o teste de unidade antes do código, que é escrito em pares, ajuda a escrever códigos com maior qualidade. Esta é uma regra de codificação recomendada pelo método

* **A)** Scrum.
* **B)** Dynamic Systems Development Method.
* **C)** Crystal Clear.
* **D)** Extreme Programming.
* **E)** Feature Driven Development.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Scrum". De acordo com a teoria estudada em *4.2 Pirâmide de Testes Automatizados no Pipeline*, meio da Pirâmide - Testes de Integração e de Contrato: Testam a comunicação entre componentes integrados (como a camada de persistência com o banco de dados em contêiner de teste ou contratos de API REST via Pact).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Dynamic Systems Development Method". De acordo com a teoria estudada em *2.1 Integração Contínua (CI): Boas Práticas, Trunk-Based e Princípio Stop the Line*, desenvolvimento em Tronco (*Trunk-Based Development*) ou Feature Branches Curtas: Evita-se a criação de branches de desenvolvimento isoladas de longa duração. Branches que duram semanas acumulam conflitos de mesclagem complexos (*merge hell*).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Crystal Clear". De acordo com a teoria estudada em *2.1 Integração Contínua (CI): Boas Práticas, Trunk-Based e Princípio Stop the Line*, execução Obrigatória de Testes de Unidade e Linting: A esteira de CI roda linters de código e baterias de testes unitários rápidos. A meta é que a validação de CI execute em menos de 10 minutos para não bloquear o fluxo do desenvolvedor.
> - **D)** **Correta.** Conforme fundamentado na seção *4.2 Pirâmide de Testes Automatizados no Pipeline* deste guia, base da Pirâmide - Testes de Unidade (Unitários): Representam a esmagadora maioria dos testes (cerca de 70%). Testam classes e funções isoladas com uso de *mocks* e *stubs*. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT-9/2015) ao estabelecer que "Extreme Programming".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Feature Driven Development". De acordo com a teoria estudada em *3.5 Feature Flags / Feature Toggles e Dark Launching*, um código pode estar rodando em produção com a funcionalidade desligada no servidor de configuração remota, sendo ativada sob demanda sem a necessidade de novo pipeline de deploy.
>
> **Gabarito: D**

---

## 5. Ferramentas de Automação: Sintaxe, Arquitetura e Manifestos

As bancas examinadoras de concursos de Tecnologia da Informação cobram com frequência a sintaxe de manifestos e os componentes arquiteturais das principais ferramentas de orquestração de CI/CD do mercado.

### 5.1 GitHub Actions: Workflows, Events, Jobs, Steps, Runners e Secrets

O GitHub Actions é uma plataforma de automação e orquestração de pipelines integrada nativamente ao GitHub.

- **Localização dos Arquivos:** Os manifestos são codificados no formato YAML e devem residir estritamente no diretório `.github/workflows/` na raiz do repositório.
- **Estrutura Hierárquica:**
    - **Workflows:** Processos automatizados configuráveis definidos por um arquivo YAML.
    - **Events (`on:`):** Eventos específicos que disparam o workflow. Exemplos: `push` em branches específicas, abertura de `pull_request`, execuções agendadas via cron (`schedule`) ou disparos manuais via interface web (`workflow_dispatch`).
    - **Jobs:** Conjunto de passos executados em um mesmo ambiente de runner. **Por padrão, múltiplos jobs definidos no mesmo workflow executam em paralelo**. Para criar dependência sequencial ou construir um grafo acíclico direcionado (DAG), utiliza-se a palavra-chave `needs: [nome_do_job]`.
    - **Steps:** Tarefas sequenciais executadas dentro de um job. Um step pode executar comandos de shell direto via `run:` ou invocar ações modulares reutilizáveis via `uses:` (como `uses: actions/checkout@v4`).
    - **Runners (`runs-on:`):** Máquinas virtuais ou contêineres que executam os jobs. Podem ser hospedados pela nuvem do GitHub (`ubuntu-latest`, `windows-latest`) ou auto-hospedados pela instituição (*self-hosted runners*). Cada job roda em uma instância de runner limpa e isolada.
    - **Secrets e Variáveis de Ambiente:** Credenciais e tokens sensíveis são armazenados criptografados e acessados nos workflows pela sintaxe `${{ secrets.NOME_DO_SEGREDO }}`.

Exemplo de manifesto completo do GitHub Actions:

```yaml
name: Pipeline CI-CD Institucional
on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Baixar Código-Fonte
        uses: actions/checkout@v4
      - name: Configurar Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
      - name: Instalar Dependências
        run: npm ci
      - name: Executar Bateria de Testes
        run: npm test

  security-scan:
    runs-on: ubuntu-latest
    steps:
      - name: Baixar Código-Fonte
        uses: actions/checkout@v4
      - name: Auditoria de Vulnerabilidades
        run: npm audit --audit-level=high

  deploy:
    needs: [test, security-scan] # Só roda se test E security-scan concluírem com sucesso
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main' # Só executa em pushes diretos ou merges na main
    steps:
      - name: Baixar Código-Fonte
        uses: actions/checkout@v4
      - name: Deploy em Produção
        env:
          CHAVE_PRODUCAO: ${{ secrets.PROD_API_KEY }}
        run: ./scripts/deploy-prod.sh
```

### 5.2 GitLab CI/CD: Stages, Jobs, Artifacts, Cache, Rules e Runners

O GitLab CI/CD baseia-se em um único arquivo de manifesto denominado obrigatoriamente `.gitlab-ci.yml`, posicionado na raiz do repositório.

- **Conceito de Stages:** A diretiva global `stages` define a ordem cronológica de execução das etapas do pipeline (ex.: `stages: [build, test, security, deploy]`). Todos os jobs associados ao mesmo stage executam **em paralelo**. O pipeline só avança para o stage subsequente se **todos os jobs do stage corrente** forem concluídos com êxito.
- **Artifacts vs. Cache (Diferença Crucial em Provas):**
    - **Artifacts:** São artefatos gerados pela execução de um job (como binários compilados `.jar`, pacotes `.zip` ou relatórios de cobertura) que são transferidos para os servidores do GitLab e repassados automaticamente aos estágios posteriores do **mesmo pipeline**.
    - **Cache:** Mecanismo de armazenamento temporário destinado unicamente a acelerar execuções futuras do pipeline, persistindo diretórios de bibliotecas externas (como `node_modules` ou `.m2/repository`) entre **diferentes execuções de pipelines**. O cache não deve ser utilizado para repassar binários finais.
- **GitLab Runners e Tags:** Os *runners* são os agentes que processam os trabalhos. Um job pode especificar quais runners têm permissão para executá-lo através de rótulos de identificação (*tags*).

Exemplo de manifesto `.gitlab-ci.yml`:

```yaml
stages:
  - build
  - test
  - deploy

variables:
  MAVEN_OPTS: "-Dmaven.repo.local=.m2/repository"

cache:
  paths:
    - .m2/repository/

build_job:
  stage: build
  image: maven:3.9-eclipse-temurin-17
  script:
    - mvn clean compile
  artifacts:
    paths:
      - target/classes/
    expire_in: 1 day

test_job:
  stage: test
  image: maven:3.9-eclipse-temurin-17
  script:
    - mvn test

deploy_staging:
  stage: deploy
  script:
    - ./scripts/deploy-staging.sh
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'
```

### 5.3 Jenkins: Arquitetura Controller-Agent, Declarative Pipeline e Scripted Pipeline

O Jenkins é um dos servidores de automação de código aberto mais tradicionais e disseminados na administração pública.

- **Arquitetura Controller-Agent:**
    - **Controller (antigo Master):** Servidor central que hospeda a interface web, gerencia as configurações dos projetos, agenda a fila de execução e supervisiona a distribuição de cargas de trabalho. O Controller **não deve executar compilações ou testes pesados diretamente**, a fim de preservar sua estabilidade.
    - **Agents (antigos Slaves):** Instâncias de computação (máquinas virtuais, nós físicos ou contêineres Docker efêmeros) que recebem comandos do Controller para executar fisicamente as etapas do pipeline.
- **Jenkinsfile e Estilos de Pipeline:** O pipeline é versionado dentro do projeto em um arquivo chamado `Jenkinsfile`:
    1. **Declarative Pipeline (Estilo Moderno e Padronizado):** Utiliza uma sintaxe declarativa estrita e de fácil leitura, iniciando obrigatoriamente pelo bloco raiz `pipeline { .. }`. Possui seções estruturadas para `agent`, `stages`, `stage`, `steps` e blocos de encerramento `post { success { .. } failure { .. } }`.
    2. **Scripted Pipeline (Estilo Tradicional em Groovy):** Sintaxe imperativa legada baseada diretamente na linguagem Groovy, iniciando por blocos `node { .. }`. Permite construções lógicas complexas e laços imperativos, mas apresenta curva de aprendizado mais íngreme e menor facilidade de manutenção.

Exemplo de Jenkinsfile Declarativo:

```groovy
pipeline {
    agent any
    stages {
        stage('Compilação e Lint') {
            steps {
                echo 'Compilando a aplicação..'
                sh 'mvn clean compile'
            }
        }
        stage('Testes Automatizados') {
            steps {
                echo 'Executando testes de unidade..'
                sh 'mvn test'
            }
        }
        stage('Homologação e Deploy') {
            steps {
                echo 'Implantando no cluster corporativo..'
                sh './scripts/deploy.sh'
            }
        }
    }
    post {
        always {
            echo 'Encerrando execução do pipeline e limpando workspace.'
            cleanWs()
        }
        failure {
            echo 'Alerta: Falha no pipeline. Notificando equipe de TI.'
        }
    }
}
```

> 🚨 **ALERTA DE PROVA / PEGADINHA FCC:**  
> A FCC adora cobrar as diferenças entre ferramentas de CI/CD:
>
> - **GitHub Actions:** Configurado em `.github/workflows/*.yml`; usa `needs:` para dependência de jobs (que rodam em paralelo por padrão); usa `runs-on:` para runners.
> - **GitLab CI/CD:** Arquivo `.gitlab-ci.yml`; organiza por `stages` (jobs de um mesmo stage rodam em paralelo; stages rodam em sequência); distingue `artifacts` (transferência no mesmo pipeline) de `cache` (reaproveitamento entre pipelines).
> - **Jenkins:** Arquitetura `Controller-Agent` (o Controller gerencia; os Agents executam); pipelines declarativos iniciam com `pipeline { agent any; stages { .. } }`.

---

### Teste 180
**(CEBRASPE – TRT-8 – Analista Judiciario Area Apoio Especializado Tecnologia da Informacao – 2022)**
Com relação às ferramentas CircleCI e Jenkins, assinale a opção correta.

* **A)** No que tange à segurança, o Jenkins possui camadas adicionais de segurança que protegem o código-fonte, variáveis ambientais e saídas.
* **B)** O Jenkins suporta maior quantidade de CPU e RAM para trabalhos mais complexos do que o CircleCI.
* **C)** O CircleCI implementa uma única camada de segurança em torno da frota de CI (integração contínua), com criação manual de segurança adicional.
* **D)** O Jenkins suporta adicionar usuários, por intermédio da autenticação VCS, utilizando diretamente a interface do usuário.
* **E)** O CircleCI utiliza-se de dependências do cache e camadas do Docker para melhorar o desempenho e acelerar o tempo de construção.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "No que tange à segurança, o Jenkins possui camadas adicionais de segurança que protegem o código-fonte, variáveis...". De acordo com a teoria estudada em *4.1 Estágios Canônicos: Lint, Análise Estática (SAST/SCA), Build, Testes e Registry*, build e Compilação: Compilação do código-fonte em artefatos binários executáveis (`.jar`, `.war`, binários Go) ou construção de imagens de contêiner imutáveis via Dockerfile.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O Jenkins suporta maior quantidade de CPU e RAM para trabalhos mais complexos do que o CircleCI". De acordo com a teoria estudada em *5.2 GitLab CI/CD: Stages, Jobs, Artifacts, Cache, Rules e Runners*, gitLab Runners e Tags: Os *runners* são os agentes que processam os trabalhos. Um job pode especificar quais runners têm permissão para executá-lo através de rótulos de identificação (*tags*).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O CircleCI implementa uma única camada de segurança em torno da frota de CI (integração contínua), com criação...". De acordo com a teoria estudada em *4. Estrutura, Estágios e Segurança de Pipelines (DevSecOps)*, a construção de um pipeline de entrega contínua robusto organiza as atividades em estágios lógicos estritamente encadeados, impedindo o avanço de artefatos defeituosos ou inseguros.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O Jenkins suporta adicionar usuários, por intermédio da autenticação VCS, utilizando diretamente a interface do...". De acordo com a teoria estudada em *3.5 Feature Flags / Feature Toggles e Dark Launching*, dark Launching: O código novo é implantado em produção e passa a ser executado em segundo plano de forma invisível aos usuários (ex.: para cada requisição recebida, o sistema envia uma chamada assíncrona ao novo algoritmo fiscal em paralelo, comparando os resultados e medindo o impacto em banco de dados sem exibir as saídas na interface do usuário).
> - **E)** **Correta.** Conforme fundamentado na seção *5.2 GitLab CI/CD: Stages, Jobs, Artifacts, Cache, Rules e Runners* deste guia, cache: Mecanismo de armazenamento temporário destinado unicamente a acelerar execuções futuras do pipeline, persistindo diretórios de bibliotecas externas (como `node_modules` ou `.m2/repository`) entre diferentes execuções de pipelines. Dessa forma, está plenamente correta a assertiva da banca (CEBRASPE – TRT-8/2022) ao estabelecer que "O CircleCI utiliza-se de dependências do cache e camadas do Docker para melhorar o desempenho e acelerar o tempo...".
>
> **Gabarito: E**

---

### Teste 181
**(FGV – TRF-1 – Analista Judiciario Area Apoio Especializado Especialidade Tecnologia da Informacao – 2024)**
O analista Maicon deve configurar um novo runner, chamado RunM, no GitLab CI/CD do TRF1. Os jobs executados no RunM devem ser capazes de interagir de forma plena com um dispositivo externo conectado fisicamente ao host do runner. O escalonamento do RunM pelo GitLab deve ser fixo, e não automático. Maicon deve escolher o executor de runner do GitLab que exige a menor quantidade de customização necessária para a execução de RunM. O executor de runner que Maicon deve escolher é:

* **A)** shell;
* **B)** docker;
* **C)** parallels;
* **D)** instance;
* **E)** virtualbox.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "shell". De acordo com a teoria estudada em *5.1 GitHub Actions: Workflows, Events, Jobs, Steps, Runners e Secrets*, steps: Tarefas sequenciais executadas dentro de um job. Um step pode executar comandos de shell direto via `run:` ou invocar ações modulares reutilizáveis via `uses:` (como `uses: actions/checkout@v4`).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "docker". De acordo com a teoria estudada em *5.3 Jenkins: Arquitetura Controller-Agent, Declarative Pipeline e Scripted Pipeline*, agents (antigos Slaves): Instâncias de computação (máquinas virtuais, nós físicos ou contêineres Docker efêmeros) que recebem comandos do Controller para executar fisicamente as etapas do pipeline.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "parallels". De acordo com a teoria estudada em *5.1 GitHub Actions: Workflows, Events, Jobs, Steps, Runners e Secrets*, jobs: Conjunto de passos executados em um mesmo ambiente de runner. Por padrão, múltiplos jobs definidos no mesmo workflow executam em paralelo.
> - **D)** **Correta.** Conforme fundamentado na seção *5.2 GitLab CI/CD: Stages, Jobs, Artifacts, Cache, Rules e Runners* deste guia, o cache não deve ser utilizado para repassar binários finais. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRF-1/2024) ao estabelecer que "instance".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "virtualbox". De acordo com a teoria estudada em *3.5 Feature Flags / Feature Toggles e Dark Launching*, dark Launching: O código novo é implantado em produção e passa a ser executado em segundo plano de forma invisível aos usuários (ex.: para cada requisição recebida, o sistema envia uma chamada assíncrona ao novo algoritmo fiscal em paralelo, comparando os resultados e medindo o impacto em banco de dados sem exibir as saídas na interface do usuário).
>
> **Gabarito: D**

---

## 🌐 Fontes Oficiais e Referências Bibliográficas

* [DORA (DevOps Research and Assessment) - The Four Keys Metrics](https://dora.dev/guides/dora-metrics-four-keys/) - Deployment Frequency, Lead Time for Changes, Time to Restore Service e Change Failure Rate.
* [Martin Fowler - Continuous Integration Guide](https://martinfowler.com/articles/continuousIntegration.html) - Fundamentos da integração frequente, build automatizado e práticas de branch principal.
* [Martin Fowler - Blue-Green Deployment](https://martinfowler.com/bliki/BlueGreenDeployment.html) - Estratégia de publicação com dois ambientes idênticos, comutação de tráfego e rollback instantâneo.
* [Martin Fowler - Canary Release Pattern](https://martinfowler.com/bliki/CanaryRelease.html) - Redução do raio de explosão (blast radius) através de rollout percentual progressivo.
* [GitHub Actions Official Documentation - Workflows and Triggers](https://docs.github.com/pt/actions/writing-workflows/about-workflows) - Sintaxe de manifestos YAML, eventos, jobs concorrentes, runners e secrets.
* [GitLab CI/CD Official Documentation - Keyword Reference](https://docs.gitlab.com/ci/yaml/) - Diretivas de pipeline: stages, jobs paralelos, artifacts e políticas de cache.
* KIM, Gene et al. **Manual de DevOps: Como Obter Agilidade, Confiabilidade e Segurança em Organizações Tecnológicas**. São Paulo: Alta Books, 2018. (Cap. 4 a 6 - As Três Vias e Práticas de Integração Contínua).
* HUMBLE, Jez; FARLEY, David. **Entrega Contínua: Como Entregar Software de Forma Rápida e Confiável**. Porto Alegre: Bookman, 2014. (Cap. 3 - Anatomia da Esteira de Implantação; Cap. 10 - Estratégias de Deploy).
* FORSGREN, Nicole; HUMBLE, Jez; KIM, Gene. **Accelerate: The Science of Lean Software and DevOps**. Portland: IT Revolution Press, 2018. (Cap. 2 - Mensurando Desempenho Organizacional com Métricas DORA).
