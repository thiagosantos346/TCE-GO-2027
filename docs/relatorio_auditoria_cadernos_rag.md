# Relatório de Auditoria e Injeção Semântica RAG (Etapa 5)

Este documento registra oficialmente a auditoria semântica 1:1 realizada caderno a caderno no projeto TCE-GO 2027. O objetivo deste procedimento é confrontar cada questão autoral simulada com o banco vetorial de questões reais de concursos anteriores, garantindo a substituição exclusiva por questões de **mesma matéria e mesmo tópico técnico em Tecnologia da Informação**, preservando intactas as questões simuladas quando não houver correspondente real com 100% de aderência conceitual.

---

## Sumário dos Cadernos Auditados

- [Caderno 05: Infraestrutura como Código (IaC) e Gerenciamento de Configuração](#caderno-05-infraestrutura-como-código-iac-e-gerenciamento-de-configuração)
- [Caderno 01: Cultura DevOps, CI/CD e Automação de Pipelines](#caderno-01-cultura-devops-cicd-e-automação-de-pipelines)
- [Caderno 02: Git, Estratégias de Branching e Plataformas Colaborativas](#caderno-02-git-estratégias-de-branching-e-plataformas-colaborativas)
- [Caderno 03: Conteinerização, Docker e Docker Compose](#caderno-03-conteinerização-docker-e-docker-compose)
- [Caderno 04: Orquestração com Kubernetes e Gestão de Ambientes](#caderno-04-orquestração-com-kubernetes-e-gestão-de-ambientes)
- [Caderno 06: Observabilidade, Monitoramento e Telemetria](#caderno-06-observabilidade-monitoramento-e-telemetria)
- [Caderno 01 (Eng. Software): Ciclo de Vida e Metodologias Ágeis](#caderno-01-eng-software-ciclo-de-vida-e-metodologias-ágeis)
- [Caderno 02 (Eng. Software): Requisitos, Histórias de Usuário, UML e BPMN](#caderno-02-eng-software-requisitos-histórias-de-usuário-uml-e-bpmn)
- [Caderno 03 (Eng. Software): Arquitetura de Software e Princípios SOLID](#caderno-03-eng-software-arquitetura-de-software-e-princípios-solid)
- [Caderno 04 (Eng. Software): Padrões de Projeto (Design Patterns - GoF)](#caderno-04-eng-software-padrões-de-projeto-design-patterns---gof)
- [Caderno 05 (Eng. Software): Qualidade, Testes, Refatoração e Dívida Técnica](#caderno-05-eng-software-qualidade-testes-refatoração-e-dívida-técnica)
- [Caderno 01 (Dev. Sistemas): Algoritmos, Estruturas de Dados e Paradigmas](#caderno-01-dev-sistemas-algoritmos-estruturas-de-dados-e-paradigmas)
- [Caderno 02 (Dev. Sistemas): Linguagens de Programação (Java, JavaScript, Node.js e Python)](#caderno-02-dev-sistemas-linguagens-de-programação-java-javascript-nodejs-e-python)
- [Caderno 03 (Dev. Sistemas): Desenvolvimento Frontend (HTML5, CSS3, React e TypeScript)](#caderno-03-dev-sistemas-desenvolvimento-frontend-html5-css3-react-e-typescript)
- [Caderno 04 (Dev. Sistemas): APIs RESTful, GraphQL, WebSockets e Documentação](#caderno-04-dev-sistemas-apis-restful-graphql-websockets-e-documentação)
- [Caderno 05 (Dev. Sistemas): Autenticação, Identidade, OAuth 2.0, OIDC e JWT](#caderno-05-dev-sistemas-autenticação-identidade-oauth-20-oidc-e-jwt)
- [Caderno 06 (Dev. Sistemas): Git, Gerenciamento de Dependências e Empacotamento](#caderno-06-dev-sistemas-git-gerenciamento-de-dependências-e-empacotamento)
- [Caderno 01 (IA & Agentivos): Fundamentos de LLMs, Intent-Based e Engenharia de Prompts](#caderno-01-ia--agentivos-fundamentos-de-llms-intent-based-e-engenharia-de-prompts)

---

## Caderno 05: Infraestrutura como Código (IaC) e Gerenciamento de Configuração
* **Arquivo:** `docs/conhecimentos_especificos_b02_ti/07_devops_e_plataforma_de_entrega/05_infraestrutura_como_codigo_iac_e_gerenciamento_de_configuracao.md`
* **Status:** Concluído e sincronizado (Commit `6673427`)

### 1. O que ENTRA (Questões Reais de Concurso)
* **`Teste 221`**: Substituído pela questão real **`V3_FGV_TRT_13_2022_Q2201`**
  * **Banca/Órgão/Ano/Cargo:** FGV – TRT/13 – 2022 – Analista Judiciário (Tecnologia da Informação)
  * **Conceito Aderente:** Arquitetura do Ansible, execução sem agentes (*agentless*), dependência do protocolo OpenSSH em nós Linux gerenciados e formato de playbooks YAML.

### 2. O que SAI (Questões Autorais/Simuladas)
* **`Teste 221`**: Simulado FCC anterior sobre conceitos agentless do Ansible.

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 214`** (Idempotência e Drift de Configuração em IaC): Sem questão real comparável de TI no banco.
* **`Teste 215`** (Declarativo vs Imperativo: Terraform vs Scripts shell/Ansible): Mantida.
* **`Teste 216`** (Ciclo de Vida do Terraform: `init`, `plan`, `apply`, `destroy`): Mantida.
* **`Teste 217`** (Terraform HCL - Bloco `data` vs `resource`): Mantida integralmente, rejeitando contaminação espúria de NBC TSP/Contabilidade.
* **`Teste 218`** (Gerenciamento do `terraform.tfstate` e State Locking remoto no S3/DynamoDB): Mantida.
* **`Teste 219`** (Módulos Terraform para reutilização corporativa de infraestrutura): Mantida.
* **`Teste 220`** (Ansible Playbooks, Plays e Tasks declarativas): Mantida.
* **`Teste 222`** (Ansible Roles e estrutura de pastas `tasks/`, `handlers/`, `templates/`): Mantida.
* **`Teste 223`** (Integração IaC no pipeline CI/CD com GitOps, `tflint` e OPA/Rego): Mantida.

---

## Caderno 01: Cultura DevOps, CI/CD e Automação de Pipelines
* **Arquivo:** `docs/conhecimentos_especificos_b02_ti/07_devops_e_plataforma_de_entrega/01_cultura_devops_ci_cd_e_automacao_de_pipelines.md`
* **Status:** Concluído e sincronizado (Commit `ccf7082`)

### 1. O que ENTRA (Questões Reais de Concurso)
* **`Teste 175`**: Substituído pela questão real **`V3_FGV_TCE_GO_2024_Q0297`**
  * **Banca/Órgão/Ano/Cargo:** **FGV – TCE/GO – 2024 – Analista de Controle Externo (Tecnologia da Informação)**
  * **Conceito Aderente:** Pipeline DevSecOps com SAST, DAST, teste de mutação e verificação contínua no tribunal.
* **`Teste 181`**: Substituído pela questão real **`V3_FGV_TRF_1_2024_Q1174`**
  * **Banca/Órgão/Ano/Cargo:** **FGV – TRF/1 – 2024 – Analista Judiciário (Tecnologia da Informação)**
  * **Conceito Aderente:** Tipos de executores do GitLab Runner (Shell, Docker, Kubernetes, VirtualBox) e isolamento de builds.

### 2. O que SAI (Questões Autorais/Simuladas)
* **`Teste 175`**: Questão autoral sobre pipeline de integração e entrega contínua.
* **`Teste 181`**: Questão autoral sobre GitLab CI e sintaxe `.gitlab-ci.yml`.

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 171`** (Modelo C.A.L.M.S. - Cultura, Automação, Lean, Medição, Compartilhamento): Preservada.
* **`Teste 172`** (As Três Vias do DevOps segundo Gene Kim): Preservada.
* **`Teste 173`** (Métricas DORA: Lead Time, Deployment Frequency, MTTR, Change Failure Rate): Preservada.
* **`Teste 174`** (Prática de *Stop the Line* e *Andon Cord* no fluxo contínuo de build): Preservada.
* **`Teste 176`** (Estratégia de Implantação Blue-Green e Chaveamento DNS/Router): Preservada.
* **`Teste 177`** (Estratégia Canary Release e análise estatística de erros com tráfego reduzido): Preservada.
* **`Teste 178`** (Feature Flags / Toggles e desacoplamento entre Deploy e Release): Preservada.
* **`Teste 179`** (Shift-Left Security: Análise SAST, DAST e SCA em pipelines DevSecOps): Preservada.
* **`Teste 180`** (GitHub Actions: Workflow, Jobs, Steps, Runners e eventos acionadores): Preservada.

---

## Caderno 02: Git, Estratégias de Branching e Plataformas Colaborativas
* **Arquivo:** `docs/conhecimentos_especificos_b02_ti/07_devops_e_plataforma_de_entrega/02_git_estrategias_de_branching_e_plataformas_colaborativas.md`
* **Status:** Concluído e auditado (Nenhuma substituição necessária)

### 1. O que ENTRA (Questões Reais de Concurso)
* *Nenhuma.* (Não há no banco vetorial questões reais oficiais de concursos pós-2022 de TI abordando detalhadamente Git Flow, Trunk-Based Development, squash/rebase merges corporativos ou governança por CODEOWNERS).

### 2. O que SAI (Questões Autorais/Simuladas)
* *Nenhuma.*

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 182`** (Modelo de Objetos do Git: Blobs, Trees, Commits e Tags): Preservada.
* **`Teste 183`** (As Três Áreas do Git: Working Directory, Staging/Index e Repository): Preservada.
* **`Teste 184`** (Merge Fast-Forward vs Three-Way Merge com nó de commit dedicado): Preservada.
* **`Teste 185`** (Git Rebase linear vs Git Merge não-destrutivo): Preservada.
* **`Teste 186`** (Git Flow: Branches de longa duração e efêmeras `feature/`, `release/`, `hotfix/`): Preservada.
* **`Teste 187`** (Trunk-Based Development para equipes ágeis de alta frequência): Preservada.
* **`Teste 188`** (Pull/Merge Request: Branch Protection Rules, code review obrigatório e CI verde): Preservada.
* **`Teste 189`** (Governança com arquivo `CODEOWNERS` no GitHub/GitLab): Preservada.
* **`Teste 190`** (Squash Merge para consolidação de commits intermediários na branch principal): Preservada.
* **`Teste 191`** (Git Hooks: Pre-commit, commit-msg e pre-push para linters e segurança): Preservada.

---

## Caderno 03: Conteinerização, Docker e Docker Compose
* **Arquivo:** `docs/conhecimentos_especificos_b02_ti/07_devops_e_plataforma_de_entrega/03_conteinerizacao_docker_e_docker_compose.md`
* **Status:** Concluído e sincronizado (Commit `c610f62`)

### 1. O que ENTRA (Questões Reais de Concurso)
* **`Teste 192`**: Substituído pela questão real **`V3_FGV_TJ_RR_2024_Q1300`**
  * **Banca/Órgão/Ano/Cargo:** FGV – TJ/RR – 2024 – Analista Judiciário (Tecnologia da Informação)
  * **Conceito Aderente:** Diferença arquitetural estruturante entre Máquinas Virtuais (Hypervisor e OS Guest completo) e Contêineres (compartilhamento do Kernel hospedeiro via Namespaces e Cgroups).
* **`Teste 194`**: Substituído pela questão real **`V3_FGV_TJ_DFT_2022_Q1777`**
  * **Banca/Órgão/Ano/Cargo:** FGV – TJ/DFT – 2022 – Analista Judiciário (Suporte em TI)
  * **Conceito Aderente:** Mecanismo Copy-on-Write (CoW), camada gravável de topo do contêiner e o comando `docker commit` para congelar alterações em uma nova imagem estática.

### 2. O que SAI (Questões Autorais/Simuladas)
* **`Teste 192`**: Questão autoral sobre Hypervisor Tipo 2 vs Namespaces do Kernel Linux.
* **`Teste 194`**: Questão autoral sobre camadas imutáveis (OverlayFS) e camada gravável efêmera.

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 193`** (Isolamento no Linux: Namespaces para segregação e Cgroups para limitação de CPU/RAM): Preservada.
* **`Teste 195`** (Anatomia do Dockerfile: Boas práticas de ordenação de instruções para cache de camadas): Preservada.
* **`Teste 196`** (Multi-Stage Builds para geração de imagens enxutas e eliminação de compiladores): Preservada.
* **`Teste 197`** (Redes Docker: `bridge`, `host`, `overlay` e `none`): Preservada.
* **`Teste 198`** (Armazenamento: Volumes gerenciados pelo Docker vs Bind Mounts acoplados ao host): Preservada.
* **`Teste 199`** (Diferença fundamental entre `CMD` e `ENTRYPOINT` no ciclo de inicialização): Preservada.
* **`Teste 200`** (Docker Compose: orquestração local declarativa multi-serviço em YAML): Preservada.
* **`Teste 201`** (Resolução interna de nomes DNS pelo engine do Docker Compose): Preservada.
* **`Teste 202`** (Segurança em contêineres: Usuário `non-root`, `read-only rootfs` e *Drop Capabilities*): Preservada.

---

## Caderno 04: Orquestração com Kubernetes e Gestão de Ambientes
* **Arquivo:** `docs/conhecimentos_especificos_b02_ti/07_devops_e_plataforma_de_entrega/04_orquestracao_com_kubernetes_e_gestao_de_ambientes.md`
* **Status:** Concluído e sincronizado

### 1. O que ENTRA (Questões Reais de Concurso)
* **`Teste 205`**: Substituído pela questão real **`V3_FGV_TJ_RR_2024_Q1301`**
  * **Banca/Órgão/Ano/Cargo:** FGV – TJ/RR – 2024 – Analista Judiciário (Infraestrutura de TI)
  * **Conceito Aderente:** Gerenciamento declarativo (`kubectl apply`) vs imperativo (`kubectl create`) e reconciliação do estado desejado no Kubernetes.
* **`Teste 208`**: Substituído pela questão real **`V3_FGV_TJ_DFT_2022_Q1775`**
  * **Banca/Órgão/Ano/Cargo:** FGV – TJ/DFT – 2022 – Analista Judiciário (Suporte em TI)
  * **Conceito Aderente:** Uso do objeto **`DaemonSet`** para garantir a execução de cópias automáticas de Pods de agentes/log em cada nó elegível do cluster.
* **`Teste 211`**: Substituído pela questão real **`V3_FGV_TCE_SC_2026_Q3289`**
  * **Banca/Órgão/Ano/Cargo:** **FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo (TI)**
  * **Conceito Aderente:** Sonda **`Readiness Probe`** para impedir o roteamento de tráfego de rede para Pods que ainda estão inicializando ou aquecendo cache.

### 2. O que SAI (Questões Autorais/Simuladas)
* **`Teste 205`**: Questão autoral sobre o mecanismo do *Reconciliation Loop*.
* **`Teste 208`**: Questão autoral sobre a escolha de workloads (*DaemonSet* para agentes de monitoramento e log).
* **`Teste 211`**: Questão autoral sobre `livenessProbe` vs `readinessProbe` em caso de falha de conexão.

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 203`** (Arquitetura do Control Plane: `kube-apiserver`, `etcd`, `kube-scheduler`, `controller-manager`): Preservada.
* **`Teste 204`** (Worker Nodes: `kubelet`, `kube-proxy` e Container Runtime): Preservada.
* **`Teste 206`** (Deployments e ReplicaSets: Estratégias RollingUpdate, maxSurge e maxUnavailable): Preservada.
* **`Teste 207`** (StatefulSets: Identidade de rede determinística e volumes ordinais): Preservada.
* **`Teste 209`** (Services no K8s: `ClusterIP`, `NodePort`, `LoadBalancer` e `ExternalName`): Preservada.
* **`Teste 210`** (Ingress Controller: Roteamento de Camada 7 HTTP/HTTPS por Host e Path): Preservada.
* **`Teste 212`** (ConfigMaps vs Secrets com encriptação e injeção por variáveis/volumes): Preservada.
* **`Teste 213`** (Persistência: `PersistentVolume` (PV), `PersistentVolumeClaim` (PVC) e `StorageClass`): Preservada.


---

## Caderno 06: Observabilidade, Monitoramento e Telemetria
* **Arquivo:** `docs/conhecimentos_especificos_b02_ti/07_devops_e_plataforma_de_entrega/06_observabilidade_monitoramento_e_telemetria.md`
* **Status:** Concluído e sincronizado

### 1. O que ENTRA (Questões Reais de Concurso)
* **`Teste 227`**: Substituir pela questão real **`V3_FGV_TRT_13_2022_Q2184`**
  * **Banca/Órgão/Ano/Cargo:** FGV – TRT/13 – 2022 – Analista Judiciário (Tecnologia da Informação)
  * **Conceito Aderente:** Arquitetura do Prometheus, armazenamento de dados como séries temporais (*time series*), linguagem de consulta PromQL e coleta de métricas via protocolo HTTP (método pull).

### 2. O que SAI (Questões Autorais/Simuladas)
* **`Teste 227`**: Questão autoral sobre os três pilares da observabilidade e métricas *Counter* vs *Gauge* no Prometheus.

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 224`** (Monitoramento Tradicional vs Observabilidade baseada na Teoria do Controle / Charity Majors): Preservada (sem questão real com profundidade equivalente no banco).
* **`Teste 225`** (Quatro Sinais Dourados / Four Golden Signals: Latência, Tráfego, Erros e Saturação do Google SRE): Preservada.
* **`Teste 226`** (Metodologias de Telemetria: Método USE de Brendan Gregg para recursos vs Método RED de Tom Wilkie para microsserviços): Preservada.
* **`Teste 228`** (Logs Estruturados em JSON, indexação de metadados e agregação em pilhas ELK/Loki): Preservada.
* **`Teste 229`** (Rastreamento Distribuído / Distributed Tracing: Relação entre Trace ponta a ponta e Spans atômicos): Preservada.
* **`Teste 230`** (OpenTelemetry / OTel: Desacoplamento entre OpenTelemetry API para instrumentação e OpenTelemetry SDK para coleta/exportação): Preservada.
* **`Teste 231`** (Confiabilidade SRE: Distinção hierárquica entre SLI, SLO interno e SLA contratual com clientes): Preservada.
* **`Teste 232`** (Engenharia de Confiabilidade / SRE: Cálculo matemático e papel regulador do Orçamento de Erro / *Error Budget* = 100% - SLO): Preservada.
* **`Teste 233`** (Pesquisas DORA: As quatro métricas fundamentais de performance de entrega de software): Preservada.


---

## Caderno 01 (Eng. Software): Ciclo de Vida e Metodologias Ágeis
* **Arquivo:** `docs/conhecimentos_especificos_b02_ti/04_engenharia_de_software/01_ciclo_de_vida_e_metodologias_ageis.md`
* **Status:** Concluído e sincronizado

### 1. O que ENTRA (Questões Reais de Concurso)
* **`Teste 004`**: Substituir pela questão real **`V3_FGV_TJ_RR_2024_Q1254`**
  * **Banca/Órgão/Ano/Cargo:** FGV – TJ/RR – 2024 – Analista Judiciário (Gestão e Governança de TI)
  * **Conceito Aderente:** Valores do Manifesto Ágil (*software em funcionamento mais que documentação abrangente*), limitação de WIP no Kanban e conceito de Lead Time.
* **`Teste 005`**: Substituir pela questão real **`V3_FGV_TJ_RR_2024_Q1251`**
  * **Banca/Órgão/Ano/Cargo:** FGV – TJ/RR – 2024 – Analista Judiciário (Gestão e Governança de TI)
  * **Conceito Aderente:** Composição do Scrum Team no Guia Scrum 2020 (inexistência de hierarquia entre PO, SM e Developers; responsabilidade do Scrum Master pela eficácia; papel dos Developers no incremento utilizável).
* **`Teste 006`**: Substituir pela questão real **`V3_FGV_TRT_13_2022_Q2199`**
  * **Banca/Órgão/Ano/Cargo:** FGV – TRT/13 – 2022 – Analista Judiciário (Tecnologia da Informação)
  * **Conceito Aderente:** Mapeamento conceitual e objetivos dos eventos do Scrum (Sprint Planning, Daily Scrum, Sprint Review e Sprint Retrospective).
* **`Teste 007`**: Substituir pela questão real **`V3_FGV_TCE_SC_2026_Q3297`**
  * **Banca/Órgão/Ano/Cargo:** **FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo (TI)**
  * **Conceito Aderente:** Governança ágil em órgãos de controle, compromisso do incremento com a *Definition of Done* (DoD) e consequências da geração de dívida técnica oculta quando a DoD é violada.
* **`Teste 009`**: Substituir pela questão real **`V3_FGV_TJ_MT_2024_Q1893`**
  * **Banca/Órgão/Ano/Cargo:** FGV – TJ/MT – 2024 – Analista Judiciário (Tecnologia da Informação)
  * **Conceito Aderente:** Práticas centrais do Kanban: limitação do trabalho em progresso (WIP - *Work in Progress*) para identificação de gargalos operacionais e fluidez do fluxo de entrega.

### 2. O que SAI (Questões Autorais/Simuladas)
* **`Teste 004`**: Simulado sobre os 4 valores do Manifesto Ágil.
* **`Teste 005`**: Simulado sobre estrutura do Scrum Team.
* **`Teste 006`**: Simulado sobre eventos e timeboxes do Scrum.
* **`Teste 007`**: Simulado sobre artefatos e metas (*commitments*) do Scrum 2020.
* **`Teste 009`**: Simulado sobre os princípios e limites de WIP do Kanban.

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 001`** (Modelo em Cascata vs Iterativo em auditoria de contratações de TI): Preservada (questão autoral contextualizada especificamente para auditoria de contratos de TI em Tribunal de Contas).
* **`Teste 002`** (Modelo Espiral de Boehm: Foco sistemático em avaliação e mitigação contínua de riscos): Preservada.
* **`Teste 003`** (RUP - Rational Unified Process: Fases de Concepção, Elaboração, Construção, Transição e arquitetura orientada a casos de uso): Preservada.
* **`Teste 008`** (Gráficos Burndown e Burnup para acompanhamento visual do escopo e esforço restante): Preservada.
* **`Teste 010`** (Métricas Kanban: Lead Time, Cycle Time e Lei de Little): Preservada.
* **`Teste 011`** (Práticas de Engenharia do Extreme Programming - XP: TDD, Pair Programming, Integração Contínua e Refatoração): Preservada.


---

## Caderno 01 (Eng. Software): Ciclo de Vida e Metodologias Ágeis
* **Arquivo:** `docs/conhecimentos_especificos_b02_ti/04_engenharia_de_software/01_ciclo_de_vida_e_metodologias_ageis.md`
* **Status:** Concluído e sincronizado

### 1. O que ENTRA (Questões Reais de Concurso)
* **`Teste 004`**: Substituir pela questão real **`V3_FGV_TJ_RR_2024_Q1254`**
  * **Banca/Órgão/Ano/Cargo:** FGV – TJ/RR – 2024 – Analista Judiciário (Gestão e Governança de TI)
  * **Conceito Aderente:** Valores do Manifesto Ágil (*software em funcionamento mais que documentação abrangente*), limitação de WIP no Kanban e conceito de Lead Time.
* **`Teste 005`**: Substituir pela questão real **`V3_FGV_TJ_RR_2024_Q1251`**
  * **Banca/Órgão/Ano/Cargo:** FGV – TJ/RR – 2024 – Analista Judiciário (Gestão e Governança de TI)
  * **Conceito Aderente:** Composição do Scrum Team no Guia Scrum 2020 (inexistência de hierarquia entre PO, SM e Developers; responsabilidade do Scrum Master pela eficácia; papel dos Developers no incremento utilizável).
* **`Teste 006`**: Substituir pela questão real **`V3_FGV_TRT_13_2022_Q2199`**
  * **Banca/Órgão/Ano/Cargo:** FGV – TRT/13 – 2022 – Analista Judiciário (Tecnologia da Informação)
  * **Conceito Aderente:** Mapeamento conceitual e objetivos dos eventos do Scrum (Sprint Planning, Daily Scrum, Sprint Review e Sprint Retrospective).
* **`Teste 007`**: Substituir pela questão real **`V3_FGV_TCE_SC_2026_Q3297`**
  * **Banca/Órgão/Ano/Cargo:** **FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo (TI)**
  * **Conceito Aderente:** Governança ágil em órgãos de controle, compromisso do incremento com a *Definition of Done* (DoD) e consequências da geração de dívida técnica oculta quando a DoD é violada.
* **`Teste 009`**: Substituir pela questão real **`V3_FGV_TJ_MT_2024_Q1893`**
  * **Banca/Órgão/Ano/Cargo:** FGV – TJ/MT – 2024 – Analista Judiciário (Tecnologia da Informação)
  * **Conceito Aderente:** Práticas centrais do Kanban: limitação do trabalho em progresso (WIP - *Work in Progress*) para identificação de gargalos operacionais e fluidez do fluxo de entrega.

### 2. O que SAI (Questões Autorais/Simuladas)
* **`Teste 004`**: Simulado sobre os 4 valores do Manifesto Ágil.
* **`Teste 005`**: Simulado sobre estrutura do Scrum Team.
* **`Teste 006`**: Simulado sobre eventos e timeboxes do Scrum.
* **`Teste 007`**: Simulado sobre artefatos e metas (*commitments*) do Scrum 2020.
* **`Teste 009`**: Simulado sobre os princípios e limites de WIP do Kanban.

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 001`** (Modelo em Cascata vs Iterativo em auditoria de contratações de TI): Preservada (questão autoral contextualizada especificamente para auditoria de contratos de TI em Tribunal de Contas).
* **`Teste 002`** (Modelo Espiral de Boehm: Foco sistemático em avaliação e mitigação contínua de riscos): Preservada.
* **`Teste 003`** (RUP - Rational Unified Process: Fases de Concepção, Elaboração, Construção, Transição e arquitetura orientada a casos de uso): Preservada.
* **`Teste 008`** (Gráficos Burndown e Burnup para acompanhamento visual do escopo e esforço restante): Preservada.
* **`Teste 010`** (Métricas Kanban: Lead Time, Cycle Time e Lei de Little): Preservada.
* **`Teste 011`** (Práticas de Engenharia do Extreme Programming - XP: TDD, Pair Programming, Integração Contínua e Refatoração): Preservada.


---

## Caderno 02 (Eng. Software): Requisitos, Histórias de Usuário, UML e BPMN
* **Arquivo:** `docs/conhecimentos_especificos_b02_ti/04_engenharia_de_software/02_requisitos_historias_de_usuario_uml_e_bpmn.md`
* **Status:** Concluído e sincronizado

### 1. O que ENTRA (Questões Reais de Concurso)
* **`Teste 014`**: Substituir pela questão real **`V3_FGV_TJ_RR_2024_Q1248`**
  * **Banca/Órgão/Ano/Cargo:** FGV – TJ/RR – 2024 – Analista Judiciário (Gestão e Governança de TI)
  * **Conceito Aderente:** Propósito e limites conceituais dos Diagramas de Casos de Uso na UML (captura de requisitos funcionais vs não funcionais, representação externa de caixa preta e distinção dos elementos gráficos).
* **`Teste 017`**: Substituir pela questão real **`V3_FGV_TJ_AP_2023_Q0550`**
  * **Banca/Órgão/Ano/Cargo:** FGV – TJ/AP – 2023 – Analista Judiciário (Desenvolvimento de Sistemas)
  * **Conceito Aderente:** Taxonomia dos diagramas comportamentais da UML (Diagrama de Atividades para modelagem de fluxos de trabalho/workflow frente a Use Case, Sequência e Máquina de Estados).

### 2. O que SAI (Questões Autorais/Simuladas)
* **`Teste 014`**: Simulado sobre relacionamentos de Caso de Uso (`include` e `extend`).
* **`Teste 017`**: Simulado sobre taxonomia estrutural vs comportamental na UML 2.5.

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 012`** (Requisitos Funcionais vs Não Funcionais / FURPS+ / ISO 25010): Preservada (desenhada especificamente para auditoria de processo eletrônico em Tribunal de Contas).
* **`Teste 013`** (Técnicas de Elicitação de Requisitos: JAD, Entrevistas, Questionários): Preservada.
* **`Teste 015`** (Histórias de Usuário e os 3 Cs de Ron Jeffries: Card, Conversation, Confirmation): Preservada.
* **`Teste 016`** (Critérios INVEST para Histórias de Usuário no Backlog Ágil): Preservada.
* **`Teste 018`** (Diagrama de Classes da UML: Agregação fraca vs Composição forte todo-parte e dependência de ciclo de vida): Preservada.
* **`Teste 019`** (Diagrama de Sequência da UML: Linhas de vida, mensagens síncronas/assíncronas e fragmentos combinados `alt`, `opt`, `loop`): Preservada.
* **`Teste 020`** (BPMN 2.0: Tipos canônicos de Tarefas - User Task, Service Task, Script Task, Manual Task): Preservada.
* **`Teste 021`** (BPMN 2.0: Gateways de Decisão - Exclusivo XOR, Paralelo AND, Inclusivo OR e Baseado em Eventos): Preservada.
* **`Teste 022`** (BPMN 2.0: Regras sintáticas de Pools, Lanes, Fluxo de Sequência e Fluxo de Mensagem): Preservada.


---

## Caderno 02 (Eng. Software): Requisitos, Histórias de Usuário, UML e BPMN
* **Arquivo:** `docs/conhecimentos_especificos_b02_ti/04_engenharia_de_software/02_requisitos_historias_de_usuario_uml_e_bpmn.md`
* **Status:** Concluído e sincronizado

### 1. O que ENTRA (Questões Reais de Concurso)
* **`Teste 014`**: Substituir pela questão real **`V3_FGV_TJ_RR_2024_Q1248`**
  * **Banca/Órgão/Ano/Cargo:** FGV – TJ/RR – 2024 – Analista Judiciário (Gestão e Governança de TI)
  * **Conceito Aderente:** Propósito e limites conceituais dos Diagramas de Casos de Uso na UML (captura de requisitos funcionais vs não funcionais, representação externa de caixa preta e distinção dos elementos gráficos).
* **`Teste 017`**: Substituir pela questão real **`V3_FGV_TJ_AP_2023_Q0550`**
  * **Banca/Órgão/Ano/Cargo:** FGV – TJ/AP – 2023 – Analista Judiciário (Desenvolvimento de Sistemas)
  * **Conceito Aderente:** Taxonomia dos diagramas comportamentais da UML (Diagrama de Atividades para modelagem de fluxos de trabalho/workflow frente a Use Case, Sequência e Máquina de Estados).

### 2. O que SAI (Questões Autorais/Simuladas)
* **`Teste 014`**: Simulado sobre relacionamentos de Caso de Uso (`include` e `extend`).
* **`Teste 017`**: Simulado sobre taxonomia estrutural vs comportamental na UML 2.5.

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 012`** (Requisitos Funcionais vs Não Funcionais / FURPS+ / ISO 25010): Preservada (desenhada especificamente para auditoria de processo eletrônico em Tribunal de Contas).
* **`Teste 013`** (Técnicas de Elicitação de Requisitos: JAD, Entrevistas, Questionários): Preservada.
* **`Teste 015`** (Histórias de Usuário e os 3 Cs de Ron Jeffries: Card, Conversation, Confirmation): Preservada.
* **`Teste 016`** (Critérios INVEST para Histórias de Usuário no Backlog Ágil): Preservada.
* **`Teste 018`** (Diagrama de Classes da UML: Agregação fraca vs Composição forte todo-parte e dependência de ciclo de vida): Preservada.
* **`Teste 019`** (Diagrama de Sequência da UML: Linhas de vida, mensagens síncronas/assíncronas e fragmentos combinados `alt`, `opt`, `loop`): Preservada.
* **`Teste 020`** (BPMN 2.0: Tipos canônicos de Tarefas - User Task, Service Task, Script Task, Manual Task): Preservada.
* **`Teste 021`** (BPMN 2.0: Gateways de Decisão - Exclusivo XOR, Paralelo AND, Inclusivo OR e Baseado em Eventos): Preservada.
* **`Teste 022`** (BPMN 2.0: Regras sintáticas de Pools, Lanes, Fluxo de Sequência e Fluxo de Mensagem): Preservada.


---

## Caderno 03 (Eng. Software): Arquitetura de Software e Princípios SOLID
* **Arquivo:** `docs/conhecimentos_especificos_b02_ti/04_engenharia_de_software/03_arquitetura_de_software_e_principios_solid.md`
* **Status:** Concluído e sincronizado

### 1. O que ENTRA (Questões Reais de Concurso)
* **`Teste 029`**: Substituir pela questão real **`V3_FGV_TJ_MT_2024_Q1887`**
  * **Banca/Órgão/Ano/Cargo:** FGV – TJ/MT – 2024 – Analista Judiciário (Tecnologia da Informação)
  * **Conceito Aderente:** Fundamentos da Arquitetura Orientada a Serviços (SOA), organização em serviços autônomos e comunicação por meio de protocolos padronizados abertos (como HTTP e SOAP).

### 2. O que SAI (Questões Autorais/Simuladas)
* **`Teste 029`**: Simulado sobre os princípios e características de SOA.

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 023`** (Modelo 4+1 Visões de Philippe Kruchten: Lógica, Processos, Desenvolvimento, Física e Cenários): Preservada (sem equivalente no banco).
* **`Teste 024`** (Acoplamento Fraco e Alta Coesão em design modular orientado a objetos): Preservada.
* **`Teste 025`** (Arquitetura Hexagonal / Ports and Adapters de Alistair Cockburn e Regra de Dependência): Preservada.
* **`Teste 026`** (Papel do Enterprise Service Bus - ESB na orquestração, mediação e roteamento de serviços): Preservada.
* **`Teste 027`** (Padrão Circuit Breaker para resiliência em microsserviços: Estados Closed, Open e Half-Open): Preservada.
* **`Teste 028`** (Arquitetura Orientada a Eventos - EDA: Outbox Pattern e consistência eventual com Kafka): Preservada.
* **`Teste 030`** (Princípios SOLID: Princípio da Segregação de Interfaces - ISP em Java): Preservada.
* **`Teste 031`** (Princípios SOLID: Princípio Aberto/Fechado - OCP e Responsabilidade Única - SRP): Preservada.
* **`Teste 032`** (Princípios de Design de Código: DRY, KISS e YAGNI): Preservada.


---

## Caderno 03 (Eng. Software): Arquitetura de Software e Princípios SOLID
* **Arquivo:** `docs/conhecimentos_especificos_b02_ti/04_engenharia_de_software/03_arquitetura_de_software_e_principios_solid.md`
* **Status:** Concluído e sincronizado

### 1. O que ENTRA (Questões Reais de Concurso)
* **`Teste 029`**: Substituir pela questão real **`V3_FGV_TJ_MT_2024_Q1887`**
  * **Banca/Órgão/Ano/Cargo:** FGV – TJ/MT – 2024 – Analista Judiciário (Tecnologia da Informação)
  * **Conceito Aderente:** Fundamentos da Arquitetura Orientada a Serviços (SOA), organização em serviços autônomos e comunicação por meio de protocolos padronizados abertos (como HTTP e SOAP).

### 2. O que SAI (Questões Autorais/Simuladas)
* **`Teste 029`**: Simulado sobre os princípios e características de SOA.

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 023`** (Modelo 4+1 Visões de Philippe Kruchten: Lógica, Processos, Desenvolvimento, Física e Cenários): Preservada (sem equivalente no banco).
* **`Teste 024`** (Acoplamento Fraco e Alta Coesão em design modular orientado a objetos): Preservada.
* **`Teste 025`** (Arquitetura Hexagonal / Ports and Adapters de Alistair Cockburn e Regra de Dependência): Preservada.
* **`Teste 026`** (Papel do Enterprise Service Bus - ESB na orquestração, mediação e roteamento de serviços): Preservada.
* **`Teste 027`** (Padrão Circuit Breaker para resiliência em microsserviços: Estados Closed, Open e Half-Open): Preservada.
* **`Teste 028`** (Arquitetura Orientada a Eventos - EDA: Outbox Pattern e consistência eventual com Kafka): Preservada.
* **`Teste 030`** (Princípios SOLID: Princípio da Segregação de Interfaces - ISP em Java): Preservada.
* **`Teste 031`** (Princípios SOLID: Princípio Aberto/Fechado - OCP e Responsabilidade Única - SRP): Preservada.
* **`Teste 032`** (Princípios de Design de Código: DRY, KISS e YAGNI): Preservada.


---

## Caderno 04 (Eng. Software): Padrões de Projeto (Design Patterns - GoF)
* **Arquivo:** `docs/conhecimentos_especificos_b02_ti/04_engenharia_de_software/04_padroes_de_projeto_design_patterns.md`
* **Status:** Concluído e sincronizado

### 1. O que ENTRA (Questões Reais de Concurso)
* **`Teste 033`**: Substituir pela questão real **`V3_FGV_TJ_BA_2015_Q1837`**
  * **Banca/Órgão/Ano/Cargo:** FGV – TJ/BA – 2015 – Analista Judiciário (Tecnologia da Informação)
  * **Conceito Aderente:** Classificação canônica dos 23 padrões GoF (*Gang of Four*) por família de propósito: Padrões Criacionais, Padrões Estruturais e Padrões Comportamentais (categorização de *Composite*, *Factory Method* e *Memento*).

### 2. O que SAI (Questões Autorais/Simuladas)
* **`Teste 033`**: Simulado sobre as matrizes de propósito e escopo do catálogo GoF.

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 034`** (Abstract Factory vs Factory Method: Criação desacoplada de famílias de produtos de interface gráfica): Preservada.
* **`Teste 035`** (Builder: Construção passo a passo e representações distintas de relatórios analíticos complexos): Preservada.
* **`Teste 036`** (Adapter: Compatibilização de interfaces incompatíveis com sistemas legados em Java): Preservada.
* **`Teste 037`** (Composite: Estrutura em árvore todo-parte tratando peças processuais e pastas uniformemente): Preservada.
* **`Teste 038`** (Decorator vs Proxy: Agregação dinâmica de comportamentos vs controle de acesso / surrogate): Preservada.
* **`Teste 039`** (Strategy: Família de algoritmos intercambiáveis para liquidação financeira de sanções): Preservada.
* **`Teste 040`** (Observer: Dependência um-para-muitos e notificação de eventos entre objetos): Preservada.
* **`Teste 041`** (Chain of Responsibility: Cadeia de objetos receptores para tratamento desacoplado de requisições): Preservada.
* **`Teste 042`** (Command e Memento: Encapsulamento de operações em objetos e captura de estado prévio para operação de *Undo*): Preservada.


---

## Caderno 04 (Eng. Software): Padrões de Projeto (Design Patterns - GoF)
* **Arquivo:** `docs/conhecimentos_especificos_b02_ti/04_engenharia_de_software/04_padroes_de_projeto_design_patterns.md`
* **Status:** Concluído e sincronizado

### 1. O que ENTRA (Questões Reais de Concurso)
* **`Teste 033`**: Substituir pela questão real **`V3_FGV_TJ_BA_2015_Q1837`**
  * **Banca/Órgão/Ano/Cargo:** FGV – TJ/BA – 2015 – Analista Judiciário (Tecnologia da Informação)
  * **Conceito Aderente:** Classificação canônica dos 23 padrões GoF (*Gang of Four*) por família de propósito: Padrões Criacionais, Padrões Estruturais e Padrões Comportamentais (categorização de *Composite*, *Factory Method* e *Memento*).

### 2. O que SAI (Questões Autorais/Simuladas)
* **`Teste 033`**: Simulado sobre as matrizes de propósito e escopo do catálogo GoF.

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 034`** (Abstract Factory vs Factory Method: Criação desacoplada de famílias de produtos de interface gráfica): Preservada.
* **`Teste 035`** (Builder: Construção passo a passo e representações distintas de relatórios analíticos complexos): Preservada.
* **`Teste 036`** (Adapter: Compatibilização de interfaces incompatíveis com sistemas legados em Java): Preservada.
* **`Teste 037`** (Composite: Estrutura em árvore todo-parte tratando peças processuais e pastas uniformemente): Preservada.
* **`Teste 038`** (Decorator vs Proxy: Agregação dinâmica de comportamentos vs controle de acesso / surrogate): Preservada.
* **`Teste 039`** (Strategy: Família de algoritmos intercambiáveis para liquidação financeira de sanções): Preservada.
* **`Teste 040`** (Observer: Dependência um-para-muitos e notificação de eventos entre objetos): Preservada.
* **`Teste 041`** (Chain of Responsibility: Cadeia de objetos receptores para tratamento desacoplado de requisições): Preservada.
* **`Teste 042`** (Command e Memento: Encapsulamento de operações em objetos e captura de estado prévio para operação de *Undo*): Preservada.


---

## Caderno 05 (Eng. Software): Qualidade, Testes, Refatoração e Dívida Técnica
* **Arquivo:** `docs/conhecimentos_especificos_b02_ti/04_engenharia_de_software/05_qualidade_testes_refatoracao_e_divida_tecnica.md`
* **Status:** Concluído e sincronizado

### 1. O que ENTRA (Questões Reais de Concurso)
* **`Teste 050`**: Substituir pela questão real **`V3_FGV_TCE_SC_2026_Q3284`**
  * **Banca/Órgão/Ano/Cargo:** **FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo (TI)**
  * **Conceito Aderente:** Ciclo canônico *Red-Green-Refactor* do TDD (*Test-Driven Development*) aplicado em sistemas de cálculo de pensões em Tribunal de Contas (escrever um teste que falha, escrever o código mínimo para fazê-lo passar e refatorar/melhorar o código).

### 2. O que SAI (Questões Autorais/Simuladas)
* **`Teste 050`**: Simulado sobre o ciclo Red-Green-Refactor do TDD.

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 043`** (Métricas de Confiabilidade: MTBF, MTTR, MTTF e cálculo de Disponibilidade): Preservada.
* **`Teste 044`** (Pirâmide de Testes de Mike Cohn e Martin Fowler: Unidade, Integração e Ponta a Ponta): Preservada.
* **`Teste 045`** (Taxonomia de Test Doubles de Gerard Meszaros: Mocks, Stubs, Dummies, Fakes e Spies): Preservada.
* **`Teste 046`** (Técnicas de Teste Caixa-Preta: Classes de Equivalência e Análise de Valor Limite): Preservada.
* **`Teste 047`** (Técnicas de Teste Caixa-Branca: Complexidade Ciclomática de McCabe e Cobertura de Código): Preservada.
* **`Teste 048`** (Testes de Regressão e Automação de Suítes em Pipelines CI/CD): Preservada.
* **`Teste 049`** (Testes Não Funcionais de Desempenho: Teste de Carga, Estresse, Pico e Resistência): Preservada.
* **`Teste 051`** (Revisão de Código / Code Review por pares e Análise Estática com SonarQube): Preservada.
* **`Teste 052`** (Refatoração segundo Martin Fowler e catálogo de *Code Smells*): Preservada.
* **`Teste 053`** (Dívida Técnica de Ward Cunningham e Quadrante da Dívida Técnica de Martin Fowler): Preservada.


---

## Caderno 01 (Dev. Sistemas): Algoritmos, Estruturas de Dados e Paradigmas
* **Arquivo:** `docs/conhecimentos_especificos_b02_ti/05_desenvolvimento_de_sistemas/01_algoritmos_estruturas_de_dados_e_paradigmas.md`
* **Status:** Auditado e aprovado sem necessidade de substituição

### 1. O que ENTRA (Questões Reais de Concurso)
* *Nenhuma.* (Não foram encontradas no banco vetorial questões reais oficiais recentes de TI abordando detalhadamente Árvores AVL, Tabelas Hash com fator de carga, Funções Puras / Imutabilidade funcional ou Notação Big-O com cenários comparativos de algoritmos).

### 2. O que SAI (Questões Autorais/Simuladas)
* *Nenhuma.*

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 054`** (Recursão: Caso Base, Caso Recursivo e Estouro de Pilha / Stack Overflow): Preservada.
* **`Teste 055`** (Complexidade de Algoritmos: Notação Big-O, limites assintóticos superior e temporal/espacial): Preservada.
* **`Teste 056`** (Estruturas de Dados Lineares: Pilha LIFO vs Fila FIFO): Preservada.
* **`Teste 057`** (Tabelas Hash: Função de dispersão, tratamento de colisões e Fator de Carga): Preservada.
* **`Teste 058`** (Árvore Binária de Busca - BST: Propriedade de ordenação e percurso Em-Ordem): Preservada.
* **`Teste 059`** (Árvore AVL: Fator de balanceamento e rotações simples/duplas para rebalanceamento): Preservada.
* **`Teste 060`** (POO: Encapsulamento de estado e modificadores de visibilidade): Preservada.
* **`Teste 061`** (POO: Polimorfismo, Sobrescrita de Método / Overriding e Sobrecarga / Overloading): Preservada.
* **`Teste 062`** (POO: Distinções conceituais e arquiteturais entre Classes Abstratas e Interfaces): Preservada.
* **`Teste 063`** (Programação Funcional: Funções Puras, ausência de efeitos colaterais e Transparência Referencial): Preservada.
* **`Teste 064`** (Programação Funcional: Funções de Alta Ordem - Map, Filter e Reduce): Preservada.


---

## Caderno 02 (Dev. Sistemas): Linguagens de Programação (Java, JavaScript, Node.js e Python)
* **Arquivo:** `docs/conhecimentos_especificos_b02_ti/05_desenvolvimento_de_sistemas/02_linguagens_java_javascript_nodejs_python.md`
* **Status:** Concluído e sincronizado

### 1. O que ENTRA (Questões Reais de Concurso)
* **`Teste 071`**: Substituir pela questão real **`V3_FGV_TJ_AP_2023_Q0539`**
  * **Banca/Órgão/Ano/Cargo:** FGV – TJ/AP – 2023 – Analista Judiciário (Desenvolvimento de Sistemas)
  * **Conceito Aderente:** Manipulação avançada de listas em Python 3, indexação positiva e negativa (`L[k]`), função `range()` reversa com passo negativo e operador de módulo (`%`) sobre o tamanho da lista.

### 2. O que SAI (Questões Autorais/Simuladas)
* **`Teste 071`**: Simulado sobre a sintaxe de fatiamento (*slicing*) em Python 3.

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 065`** (JVM: Gerenciamento de Memória Stack vs Heap e ciclo do Garbage Collector): Preservada.
* **`Teste 066`** (Linguagem Java: Modificadores `final`, `static`, `abstract` e encapsulamento): Preservada.
* **`Teste 067`** (Hierarquia de Exceções em Java: `Throwable`, Checked Exceptions vs Unchecked / `RuntimeException`): Preservada.
* **`Teste 068`** (Java Collections Framework: Distinções contratuais entre `List`, `Set` e `Map`): Preservada.
* **`Teste 069`** (JavaScript: Escopo de variáveis `var`, `let`, `const`, Hoisting e Closures em laços assíncronos): Preservada.
* **`Teste 070`** (JavaScript: Coerção implícita de tipos e diferença entre igualdade abstrata `==` e estrita `===`): Preservada.
* **`Teste 072`** (Node.js: Arquitetura do Event Loop, Call Stack, Microtask Queue e Macrotask Queue): Preservada.
* **`Teste 073`** (JavaScript/Node.js: Operações assíncronas com Promises, sintaxe `async/await` e tratamento de erros): Preservada.
* **`Teste 074`** (Python 3: Estruturas sequenciais, Listas mutáveis vs Tuplas imutáveis e Dicionários): Preservada.
* **`Teste 075`** (Python 3: Compreensão de Listas / *List Comprehensions*, filtragem e transformações funcionais): Preservada.


---

## Caderno 03 (Dev. Sistemas): Desenvolvimento Frontend (HTML5, CSS3, React e TypeScript)
* **Arquivo:** `docs/conhecimentos_especificos_b02_ti/05_desenvolvimento_de_sistemas/03_desenvolvimento_frontend_html_css_react_typescript.md`
* **Status:** Concluído e sincronizado

### 1. O que ENTRA (Questões Reais de Concurso)
* **`Teste 076`**: Substituir pela questão real **`V3_FGV_TRT_DA_2025_Q1177`**
  * **Banca/Órgão/Ano/Cargo:** FGV – TRT/DA – 2025 – Analista Judiciário (Tecnologia da Informação)
  * **Conceito Aderente:** Novos recursos e especificações introduzidos pelo HTML5 (Microdados para semântica personalizada de vocabulário, API de Geolocalização, Server-Sent Events e WebSockets).
* **`Teste 084`**: Substituir pela questão real **`V3_FGV_TCE_GO_2024_Q0296`**
  * **Banca/Órgão/Ano/Cargo:** **FGV – TCE/GO – 2024 – Analista de Controle Externo (Tecnologia da Informação)**
  * **Conceito Aderente:** Desenvolvimento de aplicações frontend em React, integração com bibliotecas de estilização CSS/Bootstrap e requisitos de importação/renderização de componentes.

### 2. O que SAI (Questões Autorais/Simuladas)
* **`Teste 076`**: Simulado sobre HTML5 semântico e tags estruturais.
* **`Teste 084`**: Simulado sobre virtual DOM e reconciliação com a propriedade `key` no React.

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 077`** (Acessibilidade Web: Diretrizes WCAG 2.1 e especificação semântica WAI-ARIA): Preservada.
* **`Teste 078`** (CSS3: Cálculo de especificidade de seletores e regras de cascata): Preservada.
* **`Teste 079`** (CSS3 Box Model: Propriedade `box-sizing: border-box` vs `content-box`): Preservada.
* **`Teste 080`** (CSS3 Flexbox: Eixo principal `justify-content` vs eixo transversal `align-items`): Preservada.
* **`Teste 081`** (TypeScript: Tipagem segura, distinção entre `any` e `unknown` e *type narrowing*): Preservada.
* **`Teste 082`** (TypeScript: `interface` vs `type alias` e o recurso exclusivo de *declaration merging*): Preservada.
* **`Teste 083`** (TypeScript: *Utility Types* `Partial`, `Readonly`, `Pick` e `Omit`): Preservada.
* **`Teste 085`** (React Hooks: Ciclo de vida com `useEffect`, array de dependências e função de cleanup): Preservada.
* **`Teste 086`** (React Hooks: Otimização de performance com `useMemo`, `useCallback` e referências com `useRef`): Preservada.


---

## Caderno 04 (Dev. Sistemas): APIs RESTful, GraphQL, WebSockets e Documentação
* **Arquivo:** `docs/conhecimentos_especificos_b02_ti/05_desenvolvimento_de_sistemas/04_apis_restful_graphql_websockets_documentacao.md`
* **Status:** Concluído e sincronizado

### 1. O que ENTRA (Questões Reais de Concurso)
* **`Teste 089`**: Substituir pela questão real **`V3_FGV_TRT_13_2022_Q2180`**
  * **Banca/Órgão/Ano/Cargo:** FGV – TRT/13 – 2022 – Analista Judiciário (Tecnologia da Informação)
  * **Conceito Aderente:** Propriedade de **Idempotência** em métodos HTTP (`PUT`), onde múltiplas requisições idênticas consecutivas produzem o mesmo estado final no servidor sem efeitos colaterais adicionais.
* **`Teste 090`**: Substituir pela questão real **`V3_FGV_TJ_AP_2023_Q0564`**
  * **Banca/Órgão/Ano/Cargo:** FGV – TJ/AP – 2023 – Analista Judiciário (Desenvolvimento de Sistemas)
  * **Conceito Aderente:** Semântica de verbos HTTP e códigos de status em APIs RESTful: requisição `PUT /recursos/1` com resposta `204 No Content` caracterizando atualização de recurso processada com sucesso.

### 2. O que SAI (Questões Autorais/Simuladas)
* **`Teste 089`**: Simulado sobre métodos HTTP e idempotência.
* **`Teste 090`**: Simulado sobre códigos de status HTTP 401 vs 403.

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 087`** (REST: As 6 restrições arquiteturais canônicas de Roy Fielding): Preservada.
* **`Teste 088`** (Modelo de Maturidade de Richardson: Do Nível 0 ao Nível 3 HATEOAS): Preservada.
* **`Teste 091`** (URI Design e Boas Práticas: Substantivos no plural e hierarquia de recursos): Preservada.
* **`Teste 092`** (GraphQL vs REST: Resolução de problemas de *Over-fetching* e *Under-fetching*): Preservada.
* **`Teste 093`** (GraphQL: Tipos de operações do esquema - `Query`, `Mutation` e `Subscription`): Preservada.
* **`Teste 094`** (WebSockets: Handshake via cabeçalho `Upgrade` e comunicação persistente full-duplex sobre TCP): Preservada.
* **`Teste 095`** (Server-Sent Events - SSE vs WebSockets: Transmissão unidirecional em tempo real sobre HTTP): Preservada.
* **`Teste 096`** (Formato JSON: Tipos de dados suportados, serialização e deserialização): Preservada.
* **`Teste 097`** (OpenAPI / Swagger: Especificação padronizada declarativa de endpoints, parâmetros e schemas): Preservada.


---

## Caderno 05 (Dev. Sistemas): Autenticação, Identidade, OAuth 2.0, OIDC e JWT
* **Arquivo:** `docs/conhecimentos_especificos_b02_ti/05_desenvolvimento_de_sistemas/05_autenticacao_identidade_oauth2_oidc_jwt.md`
* **Status:** Concluído e sincronizado

### 1. O que ENTRA (Questões Reais de Concurso)
* **`Teste 100`**: Substituir pela questão real **`V3_FGV_TRT_13_2022_Q2200`**
  * **Banca/Órgão/Ano/Cargo:** FGV – TRT/13 – 2022 – Analista Judiciário (Tecnologia da Informação)
  * **Conceito Aderente:** As quatro funções operacionais canônicas (*roles*) padronizadas na RFC 6749 do protocolo OAuth 2.0: *resource owner*, *resource server*, *client* e *authorization server*.
* **`Teste 101`**: Substituir pela questão real **`V3_FGV_TJ_AP_2023_Q0534`**
  * **Banca/Órgão/Ano/Cargo:** FGV – TJ/AP – 2023 – Analista Judiciário (Tecnologia da Informação)
  * **Conceito Aderente:** Fluxo de concessão por código de autorização (*Authorization Code Grant*) no OAuth 2.0 e o valor obrigatório atribuído ao parâmetro `response_type=code` na requisição de autorização.
* **`Teste 102`**: Substituir pela questão real **`V3_FGV_TJ_AP_2023_Q0566`**
  * **Banca/Órgão/Ano/Cargo:** FGV – TJ/AP – 2023 – Analista Judiciário (Desenvolvimento de Sistemas)
  * **Conceito Aderente:** Autenticação máquina-para-máquina (M2M) autônoma em clientes OpenID Connect/OAuth 2.0 no Keycloak, com habilitação de contas de serviço (*service accounts*) sem envolvimento de usuário final.

### 2. O que SAI (Questões Autorais/Simuladas)
* **`Teste 100`**: Simulado sobre os 4 papéis do OAuth 2.0.
* **`Teste 101`**: Simulado sobre Authorization Code Grant e PKCE.
* **`Teste 102`**: Simulado sobre Client Credentials Grant para rotinas batch.

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 098`** (Fundamentos de Segurança: Autenticação AuthN vs Autorização AuthZ): Preservada.
* **`Teste 099`** (Autenticação Multifator - MFA: Fatores de Conhecimento, Posse e Inerência): Preservada.
* **`Teste 103`** (OAuth 2.0 PKCE: Prevenção de roubo de código de autorização com `code_verifier` e `code_challenge` S256): Preservada.
* **`Teste 104`** (OpenID Connect - OIDC 1.0: Camada de identidade sobre OAuth 2.0 e o artefato `ID Token`): Preservada.
* **`Teste 105`** (JSON Web Token - JWT: Estrutura em três partes codificadas em Base64URL - Header, Payload e Signature): Preservada.
* **`Teste 106`** (Validação de JWT: Verificação de integridade criptográfica e auditoria de claims temporais): Preservada.
* **`Teste 107`** (Armazenamento Seguro de Tokens: Cookies `HttpOnly`, `Secure` e `SameSite` vs `localStorage`, e modelos RBAC/ABAC): Preservada.


---

## Caderno 06 (Dev. Sistemas): Git, Gerenciamento de Dependências e Empacotamento
* **Arquivo:** `docs/conhecimentos_especificos_b02_ti/05_desenvolvimento_de_sistemas/06_git_gerenciamento_de_dependencias_e_empacotamento.md`
* **Status:** Auditado e aprovado sem necessidade de substituição

### 1. O que ENTRA (Questões Reais de Concurso)
* *Nenhuma.* (Não foram identificadas no banco vetorial questões reais oficiais de concursos pós-2022 de TI abordando detalhadamente objetos internos do Git, `git stash`, `git reset --soft/--mixed/--hard`, versionamento SemVer, `npm ci`, ciclo de vida do Maven ou *Tree Shaking* com Vite/Webpack).

### 2. O que SAI (Questões Autorais/Simuladas)
* *Nenhuma.*

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 108`** (Git Internals: Modelo de objetos *Content-Addressable*, Blobs, Trees, Commits e Tags): Preservada.
* **`Teste 109`** (As Três Áreas do Git: *Working Directory*, *Staging Area/Index* e *Repository*): Preservada.
* **`Teste 110`** (Estratégias de Integração: `git merge` não-destrutivo vs `git rebase` linear): Preservada.
* **`Teste 111`** (Manipulação de Histórico com `git reset`: Modos `--soft`, `--mixed` e `--hard`): Preservada.
* **`Teste 112`** (Salvamento Temporário de Trabalho com `git stash` e seus subcomandos): Preservada.
* **`Teste 113`** (Gerenciamento de Dependências: Dependências Transitivas e resolução de conflitos de versão): Preservada.
* **`Teste 114`** (Versionamento Semântico / SemVer: Regras normativas de alteração de `MAJOR.MINOR.PATCH`): Preservada.
* **`Teste 115`** (Gerenciadores de Pacotes: O comando `npm ci` e a garantia de builds reprodutíveis via `package-lock.json`): Preservada.
* **`Teste 116`** (Apache Maven: O arquivo `pom.xml` e as fases canônicas do *Build Lifecycle*): Preservada.
* **`Teste 117`** (Ferramentas de Empacotamento Web: A inovação arquitetural do Vite com ES Modules nativos via esbuild): Preservada.
* **`Teste 118`** (Otimização de Bundling: Técnica de *Tree Shaking* para eliminação de código morto baseada na sintaxe estática de ES Modules): Preservada.


---

## Caderno 01 (IA & Agentivos): Fundamentos de LLMs, Intent-Based e Engenharia de Prompts
* **Arquivo:** `docs/conhecimentos_especificos_b02_ti/06_engenharia_software_ia_e_sistemas_agentivos/01_fundamentos_llms_intent_based_e_engenharia_de_prompts.md`
* **Status:** Concluído e sincronizado

### 1. O que ENTRA (Questões Reais de Concurso)
* **`Teste 120`**: Substituir pela questão real **`V3_FGV_TCE_PA_2024_Q2621`**
  * **Banca/Órgão/Ano/Cargo:** **FGV – TCE/PA – 2024 – Auditor de Controle Externo (Ciência de Dados / TI)**
  * **Conceito Aderente:** As três famílias arquiteturais originárias do modelo *Transformer* para LLMs: modelos *Decoder-only* (GPT) para geração textual autoregressiva; modelos *Encoder-only* (BERT) para compreensão contextual e classificação; e modelos *Encoder-Decoder* (T5) para transformação e síntese de sequências.

### 2. O que SAI (Questões Autorais/Simuladas)
* **`Teste 120`**: Simulado sobre as três famílias de Transformers (Encoder, Decoder e Seq2Seq).

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 119`** (Arquitetura Transformer: Mecanismo de Autoatenção / *Self-Attention*, matrizes Q, K, V e projeções escaladas): Preservada.
* **`Teste 121`** (Pipeline de Treinamento de LLMs: Pré-treinamento auto-supervisionado, Fine-Tuning Supervisionado - SFT e Alinhamento por RLHF/DPO): Preservada.
* **`Teste 122`** (Hiperparâmetros de Inferência: Temperatura, *Top-p* / *Nucleus Sampling* e *Top-k* para balanceamento de determinismo e criatividade): Preservada.
* **`Teste 123`** (Evolução de Paradigmas: Programação Imperativa Clássica vs Assistida por IA vs Programação Baseada em Intenção): Preservada.
* **`Teste 124`** (Programação Baseada em Intenção / *Intent-Based Programming*: Especificação declarativa em linguagem natural e síntese de código): Preservada.
* **`Teste 125`** (Engenharia de Prompts: Estrutura e precedência de mensagens - *System Prompt*, *User Prompt* e *Assistant Context*): Preservada.
* **`Teste 126`** (Técnicas Avançadas de Prompting: *Zero-Shot*, *Few-Shot*, *Chain-of-Thought* / CoT e *Self-Consistency*): Preservada.
* **`Teste 127`** (Limites de Contexto e Atenção: O fenômeno empírico *Lost in the Middle* em janelas longas de contexto): Preservada.
* **`Teste 128`** (Segurança e Vulnerabilidades em LLMs: Injeção de Prompt / *Prompt Injection* direta e indireta, vazamento de contexto e *Jailbreaks*): Preservada.
