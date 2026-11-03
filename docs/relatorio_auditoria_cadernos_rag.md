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
