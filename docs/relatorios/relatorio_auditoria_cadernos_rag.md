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
- [Caderno 02 (IA & Agentivos): Arquitetura de Sistemas Agentivos e Ferramentas CLI / IDE](#caderno-02-ia--agentivos-arquitetura-de-sistemas-agentivos-e-ferramentas-cli--ide)
- [Caderno 03 (IA & Agentivos): Ciclo de Vida Assistido, Geração de Testes e Depuração](#caderno-03-ia--agentivos-ciclo-de-vida-assistido-geração-de-testes-e-depuração)
- [Caderno 04 (IA & Agentivos): RAG, Protocolo MCP, Skills e Ferramental](#caderno-04-ia--agentivos-rag-protocolo-mcp-skills-e-ferramental)
- [Caderno 05 (IA & Agentivos): Qualidade, Alucinações, Segurança e Ética na IA](#caderno-05-ia--agentivos-qualidade-alucinações-segurança-e-ética-na-ia)
- [Caderno 01 (Banco de Dados): Modelagem de Dados, MER e Normalização](#caderno-01-banco-de-dados-modelagem-de-dados-mer-e-normalização)
- [Caderno 02 (Banco de Dados): Linguagem SQL (DDL, DML, DQL, TCL e DCL)](#caderno-02-banco-de-dados-linguagem-sql-ddl-dml-dql-tcl-e-dcl)
- [Caderno 03 (Banco de Dados): Transações, Propriedades ACID e Concorrência](#caderno-03-banco-de-dados-transações-propriedades-acid-e-concorrência)
- [Caderno 04 (Banco de Dados): Índices, Otimização, PostgreSQL e Oracle](#caderno-04-banco-de-dados-índices-otimização-postgresql-e-oracle)
- [Caderno 05 (Banco de Dados): Bancos NoSQL e Bancos Vetoriais](#caderno-05-banco-de-dados-bancos-nosql-e-bancos-vetoriais)
- [Caderno 06 (Banco de Dados): Replicação, Alta Disponibilidade, Backup e Segurança](#caderno-06-banco-de-dados-replicação-alta-disponibilidade-backup-e-segurança)
- [Caderno 01 (IA & Ciência de Dados): Fundamentos de IA, Machine Learning e Deep Learning](#caderno-01-ia--ciência-de-dados-fundamentos-de-ia-machine-learning-e-deep-learning)
- [Caderno 02 (IA & Ciência de Dados): NLP, IA Generativa, Agentes e Multimodalidade](#caderno-02-ia--ciência-de-dados-nlp-ia-generativa-agentes-e-multimodalidade)
- [Caderno 03 (IA & Ciência de Dados): Engenharia de Prompts, RAG e Automação de Processos](#caderno-03-ia--ciência-de-dados-engenharia-de-prompts-rag-e-automação-de-processos)
- [Caderno 04 (IA & Ciência de Dados): Ciência de Dados, Estatística e Big Data](#caderno-04-ia--ciência-de-dados-ciência-de-dados-estatística-e-big-data)
- [Caderno 05 (IA & Ciência de Dados): Ética, IA Responsável, EBIA e LGPD](#caderno-05-ia--ciência-de-dados-ética-ia-responsável-ebia-e-lgpd)
- [Caderno 01 (Dir. Administrativo): Regime Jurídico, Princípios e LINDB](#caderno-01-dir-administrativo-regime-jurídico-princípios-e-lindb)
- [Caderno 02 (Dir. Administrativo): Organização Administrativa e Poderes](#caderno-02-dir-administrativo-organização-administrativa-e-poderes)
- [Caderno 03 (Dir. Administrativo): Atos Administrativos e Processo Estadual](#caderno-03-dir-administrativo-atos-administrativos-e-processo-estadual)
- [Caderno 04 (Dir. Administrativo): Serviços Públicos, Bens e Responsabilidade Civil](#caderno-04-dir-administrativo-serviços-públicos-bens-e-responsabilidade-civil)
- [Caderno 05 (Dir. Administrativo): Controle da Administração e Improbidade Administrativa](#caderno-05-dir-administrativo-controle-da-administração-e-improbidade-administrativa)
- [Caderno 06 (Dir. Administrativo): Acesso à Informação e Contratos de Publicidade](#caderno-06-dir-administrativo-acesso-à-informação-e-contratos-de-publicidade)
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


---

## Caderno 02 (IA & Agentivos): Arquitetura de Sistemas Agentivos e Ferramentas CLI / IDE
* **Arquivo:** `docs/conhecimentos_especificos_b02_ti/06_engenharia_software_ia_e_sistemas_agentivos/02_arquitetura_de_sistemas_agentivos_e_ferramentas_cli_ide.md`
* **Status:** Auditado e aprovado sem necessidade de substituição

### 1. O que ENTRA (Questões Reais de Concurso)
* *Nenhuma.* (Tópico de ponta emergente no edital do TCE-GO; não há no histórico de concursos de TI questões oficiais abordando arquitetura canônica de 4 pilares de agentes, *The Agentic Loop*, *Stop Conditions* / disjuntores de agentes, arquiteturas multiagente hierárquicas ou governança de ferramentas agentivas CLI/IDE).

### 2. O que SAI (Questões Autorais/Simuladas)
* *Nenhuma.*

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 129`** (Transição de Chatbots Passivos para Sistemas Agentivos Orientados a Objetivos): Preservada.
* **`Teste 130`** (Arquitetura Canônica de 4 Pilares: Modelo, Memória, Ferramentas e Planejamento): Preservada.
* **`Teste 131`** (Comparativo Arquitetural: Assistentes Agentivos CLI vs Extensões de IDE): Preservada.
* **`Teste 132`** (The Agentic Loop: Ciclo contínuo de Percepção, Raciocínio, Ação, Observação e Reflexão): Preservada.
* **`Teste 133`** (Fase de Percepção e Descoberta de Contexto em Projetos de Software): Preservada.
* **`Teste 134`** (Planejamento e Decomposição de Metas / *Task Decomposition* em Subtarefas): Preservada.
* **`Teste 135`** (Fase de Ação e Uso de Ferramentas / *Tool Calling* em Terminal e Código): Preservada.
* **`Teste 136`** (Critérios de Parada / *Stop Conditions* e Disjuntores contra Loops Infinitos de Agentes): Preservada.
* **`Teste 137`** (Arquiteturas Multiagente Hierárquicas: Agente Orquestrador delegando a Subagentes Especialistas): Preservada.
* **`Teste 138`** (Governança, Menor Privilégio e Mecanismos *Human-in-the-Loop* em Agentes Autônomos): Preservada.


---

## Caderno 03 (IA & Agentivos): Ciclo de Vida Assistido, Geração de Testes e Depuração
* **Arquivo:** `docs/conhecimentos_especificos_b02_ti/06_engenharia_software_ia_e_sistemas_agentivos/03_ciclo_de_vida_assistido_geracao_testes_e_depuracao.md`
* **Status:** Auditado e aprovado sem necessidade de substituição (100% de preservação pedagógica)

### 1. O que ENTRA (Questões Reais de Concurso)
* *Nenhuma.* (Não foram identificadas no banco vetorial questões reais oficiais de concursos pós-2022 de TI abordando detalhadamente engenharia de software assistida por IA, engines de completamento de código FIM - Fill-in-the-Middle em IDEs, code review automatizado com agentes, depuração de incidentes em produção com análise de stack traces por IA, geração automatizada de testes unitários com armadilha de mocks tautológicos ou testes de mutação para aferição de testes sintéticos).

### 2. O que SAI (Questões Autorais/Simuladas)
* *Nenhuma.*

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 139`** (Tradução e Modernização de Legado: Migração de regras de negócio de COBOL para Python assistida por IA, cuidados com tipos de ponto fixo `Decimal` vs ponto flutuante e semântica de arredondamento financeiro): Preservada.
* **`Teste 140`** (Motores de Completamento em IDEs: Arquitetura *Fill-in-the-Middle* / FIM, renderização de contexto por prefixo e sufixo para preenchimento de lacunas de código): Preservada.
* **`Teste 141`** (AI Code Review em CI/CD: Integração de agentes no fluxo de Pull Requests, triagem preliminar de estilo, complexidade ciclomática e aderência a linters): Preservada.
* **`Teste 142`** (Limites de Contexto em Revisão de Código: *Chunking* semântico por arquivo/função vs visão holística de repositório e estratégias de mitigação de degradação posicional): Preservada.
* **`Teste 143`** (Segurança em Code Review por IA: Detecção de credenciais, segredos e API keys em pipelines com modelos generativos vs checagens determinísticas de entropia e regex como Gitleaks/TruffleHog): Preservada.
* **`Teste 144`** (Engenharia Reversa de Legados: Síntese automatizada de docstrings, diagramas estruturais Mermaid e especificações OpenAPI a partir de código desprovido de documentação): Preservada.
* **`Teste 145`** (Depuração de Incidentes em Produção: Análise de *Stack Traces* por LLM, identificação de causas-raiz em falhas concorrentes e geração de patches acompanhados de testes de regressão): Preservada.
* **`Teste 146`** (Investigação de Performance e Concorrência: Diagnóstico de esgotamento de pool de conexões JDBC/HikariCP e contenção de threads guiado por IA): Preservada.
* **`Teste 147`** (Geração Automatizada de Testes Unitários: Criação de suítes JUnit/PyTest com IA e prevenção contra a armadilha de mocks tautológicos que confirmam o próprio erro): Preservada.
* **`Teste 148`** (Testes de Mutação Aplicados a Código Sintético: Utilização de mutation testing como PIT/Mutmut para injetar falhas propositais e validar se a suíte gerada por IA realmente detecta quebras): Preservada.
* **`Teste 149`** (Cobertura de Código vs Cobertura de Mutação: Limitações da métrica puramente estática de linhas cobertas e superioridade do índice de mutantes eliminados para testes assistidos por IA): Preservada.


---

## Caderno 04 (IA & Agentivos): RAG, Protocolo MCP, Skills e Ferramental
* **Arquivo:** `docs/conhecimentos_especificos_b02_ti/06_engenharia_software_ia_e_sistemas_agentivos/04_rag_protocolo_mcp_skills_e_ferramental.md`
* **Status:** Concluído e sincronizado

### 1. O que ENTRA (Questões Reais de Concurso)
* **`Teste 152`**: Substituído pela questão real **`V3_FGV_TCE_PA_2024_Q2622`**
  * **Banca/Órgão/Ano/Cargo:** **FGV – TCE/PA – 2024 – Auditor de Controle Externo (Ciência de Dados / TI)**
  * **Conceito Aderente:** Fundamentos da arquitetura *Retrieval-Augmented Generation* (RAG) para mitigação de alucinações em LLMs, combinação entre sistemas de recuperação de informação e modelos generativos, busca em bases de dados externas confiáveis durante a consulta e ausência de alteração nos parâmetros/pesos do modelo generativo (inferência em tempo real sem retreino).
* **`Teste 154`**: Substituído pela questão real **`V3_FGV_TCE_SC_2026_Q3280`**
  * **Banca/Órgão/Ano/Cargo:** **FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo (TI - Ciências da Computação)**
  * **Conceito Aderente:** Papel fundamental dos Bancos de Dados Vetoriais (*Vector Databases*) no fluxo operacional de um sistema RAG em Tribunais de Contas: armazenar as representações matemáticas multidimensionais (*embeddings*) dos documentos normativos para viabilizar a busca por similaridade semântica (cosseno/HNSW) e ancorar as respostas do LLM.

### 2. O que SAI (Questões Autorais/Simuladas)
* **`Teste 152`**: Simulado sobre arquitetura RAG e chunking para auditoria de conformidade de repositórios.
* **`Teste 154`**: Simulado sobre busca híbrida em bancos de dados vetoriais para auditoria.

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 150`** (Self-Attention Canônico do Transformer: Mecanismo de atenção por produto escalar escalado, matrizes Q, K, V e complexidade quadrática $O(N^2)$): Preservada.
* **`Teste 151`** (Prompt Caching: Mecanismo de KV Cache em aceleração por GPU, reuso de prefixos idênticos de prompts corporativos e redução de até 90% em custos de tokens e TTFT): Preservada.
* **`Teste 153`** (AST-Based Chunking: Fatiamento estrutural com parsers gramaticais como Tree-sitter para preservação de funções, classes e namespaces inteiros nos embeddings): Preservada.
* **`Teste 155`** (Matriz RAG vs Fine-Tuning: Critérios objetivos de escolha arquitetural - conhecimento factual dinâmico vs conformidade de estilo e sintaxe): Preservada.
* **`Teste 156`** (Arquitetura do Model Context Protocol - MCP: Padrão aberto da Anthropic, separação estrita entre Host, MCP Client e MCP Server): Preservada.
* **`Teste 157`** (Primitivas do Protocolo MCP: Distinção operacional entre Resources, Prompts e Tools): Preservada.
* **`Teste 158`** (Segurança no Ecossistema MCP: Autorização explícita, modelo *Human-in-the-Loop*, sandboxing de tools e menor privilégio): Preservada.
* **`Teste 159`** (Camadas de Transporte do MCP: Transporte Stdio sobre processos locais e SSE - Server-Sent Events sobre HTTP para servidores remotos): Preservada.
* **`Teste 160`** (Mecanismo de Tool Use / Function Calling: Protocolo de geração e troca de esquemas JSON estruturados entre LLM e cliente executor): Preservada.


---

## Caderno 05 (IA & Agentivos): Qualidade, Alucinações, Segurança e Ética na IA
* **Arquivo:** `docs/conhecimentos_especificos_b02_ti/06_engenharia_software_ia_e_sistemas_agentivos/05_qualidade_alucinacoes_seguranca_e_etica_na_ia.md`
* **Status:** Auditado e aprovado sem necessidade de substituição (100% de preservação pedagógica)

### 1. O que ENTRA (Questões Reais de Concurso)
* *Nenhuma.* (Não foram identificadas no banco vetorial questões reais oficiais de concursos pós-2022 de TI cobrindo métricas de código pass@k, benchmarks HumanEval/MBPP, isolamento de agentes em microVMs Firecracker/gVisor, ataques de Slopsquatting/Package Hallucination em NPM/PyPI, OWASP Top 10 for LLM - Prompt Injection direto/indireto, LGPD em prompts de desenvolvimento ou diretrizes da Resolução CNJ nº 332/2020 para IA no setor público).

### 2. O que SAI (Questões Autorais/Simuladas)
* *Nenhuma.*

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 161`** (Métricas de Avaliação de Código: Superioridade do `pass@k` baseado em execução de suítes de teste sobre métricas léxicas de n-gramas como BLEU e ROUGE): Preservada.
* **`Teste 162`** (Benchmarks de Código para LLMs: HumanEval e MBPP - *Mostly Basic Python Problems*, medição de síntese funcional e resolução de problemas algorítmicos): Preservada.
* **`Teste 163`** (Taxonomia de Métricas de Avaliação em IA: Perplexidade / *Perplexity*, BLEU, ROUGE e embeddings semânticos com BERTScore): Preservada.
* **`Teste 164`** (Sandboxing de Agentes Autônomos: Isolamento de execução de código e comandos de shell em microVMs como Firecracker, gVisor ou contêineres Docker efêmeros): Preservada.
* **`Teste 165`** (Ataques à Cadeia de Suprimentos por IA: O vetor de ameaça *Slopsquatting* / *Package Hallucination*, registro malicioso de bibliotecas alucinadas em repositórios públicos PyPI e NPM): Preservada.
* **`Teste 166`** (OWASP Top 10 for LLM - Injeção de Instruções: Vetores de *Direct Prompt Injection* / Jailbreaking e *Indirect Prompt Injection* via dados externos manipulados): Preservada.
* **`Teste 167`** (Segurança e Vazamento de Dados em Ferramentas CLI/IDE: Vetores de exfiltração de dados sensíveis e código proprietário via ferramentas e chamadas de API desprotegidas): Preservada.
* **`Teste 168`** (LGPD e Governança de Prompts Corporativos: Políticas de retenção e treinamento de provedores de IA, mascaramento de PII e proteção de segredos de negócio): Preservada.
* **`Teste 169`** (Propriedade Intelectual e Licenciamento de Código Sintético: Riscos de contaminação por licenças copyleft como GPLv3 em código gerado por IA e jurisprudência de Fair Use): Preservada.
* **`Teste 170`** (Governança Pública e Resolução CNJ nº 332/2020: Princípios de explicabilidade, auditabilidade, supervisão humana - *Human-in-the-Loop* e não-discriminação algorítmica em tribunais): Preservada.


---

## Caderno 01 (Banco de Dados): Modelagem de Dados, MER e Normalização
* **Arquivo:** `docs/conhecimentos_especificos_b02_ti/08_banco_de_dados/01_modelagem_de_dados_mer_e_normalizacao.md`
* **Status:** Concluído e sincronizado

### 1. O que ENTRA (Questões Reais de Concurso)
* **`Teste 241`**: Substituído pela questão real **`V3_FGV_TCE_PA_2024_Q2585`**
  * **Banca/Órgão/Ano/Cargo:** **FGV – TCE/PA – 2024 – Auditor de Controle Externo (Ciência de Dados / TI)**
  * **Conceito Aderente:** Modelagem relacional e Primeira Forma Normal (1FN). Atributos multivalorados (dependentes de funcionário sem limite fixo) exigem a criação de uma tabela autônoma vinculada por chave estrangeira, sendo incorreto vetorizar ou replicar linhas na mesma tabela.

### 2. O que SAI (Questões Autorais/Simuladas)
* **`Teste 241`**: Simulado sobre modelagem de dependentes e aplicação canônica da 1FN.

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 234`** (Níveis de Abstração ANSI/SPARC: Modelo Conceitual, Lógico e Físico de dados): Preservada.
* **`Teste 235`** (Modelo Entidade-Relacionamento de Peter Chen: Entidades Fortes, Fracas, Associativas e tipos de atributos): Preservada.
* **`Teste 236`** (Atributos Compostos e Multivalorados no MER - Questão Oficial FCC TRT-2 2014 TI): Preservada.
* **`Teste 237`** (Mapeamento ER para Esquema Relacional: Resolução de relacionamentos 1:1, 1:N e N:M): Preservada.
* **`Teste 238`** (Álgebra Relacional: Operadores primitivos de Seleção $\sigma$, Projeção $\pi$, Produto Cartesiano $	imes$, União $\cup$ e Diferença $-$): Preservada.
* **`Teste 239`** (Álgebra Relacional Avançada: Junção Natural $owtie$, Junção Theta e Divisão Relacional $\div$): Preservada.
* **`Teste 240`** (Dependências Funcionais e Regras de Inferência: Axiomas de Armstrong - Reflexividade, Aumento e Transitividade): Preservada.
* **`Teste 242`** (Segunda Forma Normal - 2FN: Dependência Funcional Total e eliminação de dependências parciais): Preservada.
* **`Teste 243`** (Terceira Forma Normal - 3FN: Eliminação de dependências funcionais transitivas entre atributos não-chave): Preservada.
* **`Teste 244`** (Forma Normal de Boyce-Codd - BCNF vs 3FN e Quarta Forma Normal - 4FN com Dependências Multivaloradas - MVD): Preservada.


---

## Caderno 02 (Banco de Dados): Linguagem SQL (DDL, DML, DQL, TCL e DCL)
* **Arquivo:** `docs/conhecimentos_especificos_b02_ti/08_banco_de_dados/02_linguagem_sql_ddl_dml_dql_tcl_e_dcl.md`
* **Status:** Concluído e sincronizado

### 1. O que ENTRA (Questões Reais de Concurso)
* **`Teste 245`**: Substituído pela questão real **`V3_FGV_TCE_GO_2024_Q0295`**
  * **Banca/Órgão/Ano/Cargo:** **FGV – TCE/GO – 2024 – Analista de Controle Externo (Tecnologia da Informação)**
  * **Conceito Aderente:** Comandos da DCL (*Data Control Language*) do SQL em banco de dados de tribunal (`GRANT`, `WITH GRANT OPTION` e `REVOKE`). Propagação de privilégios de consulta e atualização sobre tabelas (`DADOS_PROCESSO` e `DADOS_PARTE`) e efeitos pontuais da revogação.
* **`Teste 248`**: Substituído pela questão real **`V3_FGV_TRT_DA_2025_Q1194`**
  * **Banca/Órgão/Ano/Cargo:** **FGV – TRT/DA – 2025 – Analista Judiciario (Tecnologia da Informacao)**
  * **Conceito Aderente:** Cláusulas estruturais do SQL no PostgreSQL: agrupamento com `GROUP BY`, funções de agregação (`COUNT`, `MAX`, `MIN`, `SUM`, `AVG`), filtro pós-agrupamento com `HAVING` e lógica condicional da expressão `CASE WHEN ... THEN ... ELSE ... END`.

### 2. O que SAI (Questões Autorais/Simuladas)
* **`Teste 245`**: Simulado sobre concessão de `GRANT WITH GRANT OPTION` e `REVOKE CASCADE`.
* **`Teste 248`**: Simulado sobre a ordem de execução do SQL e proibição de agregações no `WHERE`.

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 246`** (Comandos DDL: `CREATE`, `ALTER`, `DROP` e constraints `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `CHECK`, `NOT NULL`): Preservada.
* **`Teste 247`** (Diferenças Semânticas e de I/O entre `TRUNCATE TABLE` vs `DELETE FROM`): Preservada.
* **`Teste 249`** (Junções Relacionais: `INNER JOIN`, `LEFT OUTER JOIN`, `RIGHT OUTER JOIN`, `FULL OUTER JOIN` e `CROSS JOIN`): Preservada.
* **`Teste 250`** (Operadores de Conjunto: `UNION` com desduplicação vs `UNION ALL` com concatenação de alta performance, `INTERSECT` e `EXCEPT`): Preservada.
* **`Teste 251`** (Lógica Ternária do SQL / *Three-Valued Logic*: `TRUE`, `FALSE`, `UNKNOWN` e a armadilha crítica de subconsultas com `NOT IN` e valores `NULL`): Preservada.
* **`Teste 252`** (Common Table Expressions - CTEs e recursividade com `WITH RECURSIVE` para estruturas hierárquicas): Preservada.
* **`Teste 253`** (Funções de Janela / *Window Functions*: Cláusula `OVER(PARTITION BY ... ORDER BY ...)` com `ROW_NUMBER()`, `RANK()` e `DENSE_RANK()`): Preservada.
* **`Teste 254`** (Funções de Janela de Deslocamento: `LAG()` e `LEAD()` com cálculo de variação percentual intertemporal): Preservada.
* **`Teste 255`** (Subconsultas Correlacionadas vs Subconsultas Escalares e operador `EXISTS`): Preservada.


---

## Caderno 03 (Banco de Dados): Transações, Propriedades ACID e Concorrência
* **Arquivo:** `docs/conhecimentos_especificos_b02_ti/08_banco_de_dados/03_transacoes_propriedades_acid_e_concorrencia.md`
* **Status:** Auditado e aprovado sem necessidade de substituição (100% de preservação pedagógica)

### 1. O que ENTRA (Questões Reais de Concurso)
* *Nenhuma.* (Todas as 11 questões formam uma progressão teórica e técnica estrita sobre ACID, níveis de isolamento ANSI, Snapshot Isolation, bloqueios compartilhados/exclusivos, Two-Phase Locking, MVCC e detecção de deadlocks; mantidas integralmente para preservar a profundidade exigida no edital TCE-GO 2027).

### 2. O que SAI (Questões Autorais/Simuladas)
* *Nenhuma.*

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 256`** (Conceito de Transação e Propriedades ACID: Atomicidade, Consistência, Isolamento e Durabilidade): Preservada.
* **`Teste 257`** (Durabilidade e Mecanismos de Recuperação: *Write-Ahead Logging* / WAL e *Checkpoints* contra falhas de energia): Preservada.
* **`Teste 258`** (Comandos TCL: Delimitação transacional com `COMMIT`, `ROLLBACK` e pontos de salvamento intermediários `SAVEPOINT`): Preservada.
* **`Teste 259`** (Anomalias de Concorrência ANSI SQL-92: Leitura Suja / *Dirty Read*, Leitura Não-Repetível / *Non-Repeatable Read* e Leitura Fantasma / *Phantom Read*): Preservada.
* **`Teste 260`** (Níveis de Isolamento ANSI: *Read Uncommitted*, *Read Committed*, *Repeatable Read* e *Serializable*): Preservada.
* **`Teste 261`** (*Snapshot Isolation* / Isolamento por Instantâneo e a anomalia de desvio de escrita / *Write Skew*): Preservada.
* **`Teste 262`** (Tipos de Bloqueios Lógicos: Bloqueio Compartilhado / *Shared Lock* (S) vs Bloqueio Exclusivo / *Exclusive Lock* (X) e matriz de compatibilidade): Preservada.
* **`Teste 263`** (Dinâmica de Concorrência e Grafo de Espera / *Wait-For Graph* para detecção de ciclos de bloqueio mútuo): Preservada.
* **`Teste 264`** (Protocolo de Bloqueio em Duas Fases / 2PL: Fase de Crescimento vs Fase de Encolhimento e garantia de serializabilidade estrita): Preservada.
* **`Teste 265`** (Controle Multiversão de Concorrência / MVCC: Implementação no PostgreSQL com metadados `xmin`/`xmax` e independência entre leitores e escritores): Preservada.
* **`Teste 266`** (Detecção e Resolução de Impasses / *Deadlocks* pelo SGBD com aborto de transação vítima e rollback): Preservada.


---

## Caderno 04 (Banco de Dados): Índices, Otimização, PostgreSQL e Oracle
* **Arquivo:** `docs/conhecimentos_especificos_b02_ti/08_banco_de_dados/04_indices_otimizacao_postgresql_e_oracle.md`
* **Status:** Auditado e aprovado sem necessidade de substituição (100% de preservação pedagógica)

### 1. O que ENTRA (Questões Reais de Concurso)
* *Nenhuma.* (Todas as 11 questões abordam minuciosamente tópicos profundos de B+Tree, índices Bitmap para baixa cardinalidade, índices parciais e baseados em expressão no PostgreSQL, trade-off de índices em DML, CBO, EXPLAIN ANALYZE, algoritmos de join - Nested Loop, Hash e Merge, parâmetro `work_mem`, VACUUM/MVCC, além de áreas de memória SGA/PGA, processos DBWn/LGWR/CKPT e hierarquia de Tablespaces no Oracle; mantidas 100% intactas para cobrir todo o espectro do edital).

### 2. O que SAI (Questões Autorais/Simuladas)
* *Nenhuma.*

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 267`** (Índices Bitmap: Vantagens para colunas de baixa cardinalidade em ambientes OLAP e operações lógicas booleanas diretas): Preservada.
* **`Teste 268`** (Índices Parciais / *Partial Indexes* com predicado `WHERE` e Índices Baseados em Expressão / *Function-Based*): Preservada.
* **`Teste 269`** (Trade-off de Índices: Sobrecarga computacional de I/O, memória e *page splits* provocada por múltiplos índices secundários em operações DML): Preservada.
* **`Teste 270`** (Otimizador Baseado em Custo / CBO: Uso de estatísticas de catálogo e histogramas para estimativa de cardinalidade em distribuições assimétricas): Preservada.
* **`Teste 271`** (Introspecção de Consultas: Diferenças operacionais cruciais entre `EXPLAIN` puramente teórico e `EXPLAIN ANALYZE` com execução real): Preservada.
* **`Teste 272`** (Algoritmos de Junção: Características, restrições e custos de *Nested Loop*, *Hash Join* e *Merge Join*): Preservada.
* **`Teste 273`** (Alocação de Memória no PostgreSQL: O parâmetro `work_mem` e as consequências de degradação por *spill* de ordenações e hashes para o disco): Preservada.
* **`Teste 274`** (Arquitetura MVCC e Gerenciamento de Espaço: Tuplas mortas / *dead tuples*, rotinas de `VACUUM` concorrente e `VACUUM FULL` com travamento exclusivo): Preservada.
* **`Teste 275`** (Arquitetura de Memória do Oracle Database: Divisão entre *System Global Area* - SGA compartilhada e *Program Global Area* - PGA privada por sessão): Preservada.
* **`Teste 276`** (Processos de Segundo Plano no Oracle: Atribuições especializadas do DBWn, LGWR, CKPT, SMON e PMON): Preservada.
* **`Teste 277`** (Estrutura de Armazenamento Lógico do Oracle: Hierarquia composicional entre Database, Tablespace, Segment, Extent e Data Block): Preservada.


---

## Caderno 05 (Banco de Dados): Bancos NoSQL e Bancos Vetoriais
* **Arquivo:** `docs/conhecimentos_especificos_b02_ti/08_banco_de_dados/05_bancos_nosql_e_bancos_vetoriais.md`
* **Status:** Concluído e sincronizado

### 1. O que ENTRA (Questões Reais de Concurso)
* **`Teste 279`**: Substituído pela questão real **`V3_FGV_TCE_SC_2026_Q3295`**
  * **Banca/Órgão/Ano/Cargo:** **FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo (TI - Ciências da Computação)**
  * **Conceito Aderente:** Aplicação prática do Teorema CAP na arquitetura de bancos de dados NoSQL distribuídos em Tribunais de Contas: comportamento diante de falha na rede entre datacenters (partição de rede), priorização de Disponibilidade (A) e Tolerância a Partições (P) com consistência eventual (*Eventual Consistency*).

### 2. O que SAI (Questões Autorais/Simuladas)
* **`Teste 279`**: Simulado sobre o Teorema PACELC e classificação PA/EL do Cassandra.

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 278`** (Famílias NoSQL: Modelos Chave-Valor, Orientados a Documentos, Colunares / Wide-Column e Grafos): Preservada.
* **`Teste 280`** (Modelo BASE: *Basically Available, Soft-state, Eventual consistency* em contraposição ao modelo ACID relacional): Preservada.
* **`Teste 281`** (Bancos de Documentos / MongoDB: Formato BSON, indexação flexível e arquitetura de *Replica Sets* com nó primário e secundários): Preservada.
* **`Teste 282`** (Bancos Chave-Valor / Redis: Estruturas de dados em memória RAM e mecanismos de persistência RDB snapshot vs AOF append-only): Preservada.
* **`Teste 283`** (Bancos Colunares / Cassandra: Particionamento distribuído por hash da Partition Key e ordenação local por Clustering Columns): Preservada.
* **`Teste 284`** (Bancos de Grafos / Neo4j: Modelo de Grafos de Propriedades com Nós, Arestas direcionadas e linguagem de consulta Cypher): Preservada.
* **`Teste 285`** (Bancos Multimodelo e Cenários Híbridos de Persistência Poliglota em Tribunais de Contas): Preservada.
* **`Teste 286`** (Bancos Vetoriais e Inteligência Artificial: Indexação de embeddings multidimensionais e busca por similaridade semântica de cosseno): Preservada.
* **`Teste 287`** (Algoritmos de Indexação Vetorial: HNSW - *Hierarchical Navigable Small World* vs IVFFlat e trade-offs entre recall e latência): Preservada.
* **`Teste 288`** (A Extensão `pgvector` no PostgreSQL: Tipos de dados `vector`, operadores de distância e comandos de criação de índices HNSW): Preservada.


---

## Caderno 06 (Banco de Dados): Replicação, Alta Disponibilidade, Backup e Segurança
* **Arquivo:** `docs/conhecimentos_especificos_b02_ti/08_banco_de_dados/06_replicacao_alta_disponibilidade_backup_e_seguranca.md`
* **Status:** Auditado e aprovado sem necessidade de substituição (100% de preservação pedagógica)

### 1. O que ENTRA (Questões Reais de Concurso)
* *Nenhuma.* (Todas as 11 questões abordam tópicos críticos de missão crítica: replicação física vs lógica no PostgreSQL, quorum e prevenção contra split-brain, modalidades de backup, métricas RPO/RTO, restauração pontual PITR com arquivamento de WAL, mascaramento dinâmico DDM, criptografia TDE e segurança granular RLS/RBAC; mantidas 100% intactas para garantir máxima cobertura para a prova).

### 2. O que SAI (Questões Autorais/Simuladas)
* *Nenhuma.*

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 289`** (Topologias de Replicação: Replicação Síncrona com garantia de zero perda de dados vs Replicação Assíncrona com alto throughput): Preservada.
* **`Teste 290`** (Replicação no PostgreSQL: *Physical Streaming Replication* baseada em WAL vs Replicação Lógica baseada em publicações e subscrições): Preservada.
* **`Teste 291`** (Alta Disponibilidade: Failover automático, detecção de nós inativos (*heartbeat*) e promoção de nós standby): Preservada.
* **`Teste 292`** (Particionamento de Rede e Síndrome de *Split-Brain*: Mecanismos de Quórum e Fencing com STONITH para isolamento de nós): Preservada.
* **`Teste 293`** (Estratégias de Backup Corporativo: Backup Físico vs Lógico (`pg_dump`), cópias Completas / Full, Diferenciais e Incrementais): Preservada.
* **`Teste 294`** (Métricas de Continuidade de Negócios: *Recovery Point Objective* - RPO e *Recovery Time Objective* - RTO no planejamento de desastres): Preservada.
* **`Teste 295`** (Recuperação em Ponto no Tempo / PITR: Restauração a partir de backup base associada à reprodução contínua de logs WAL arquivados): Preservada.
* **`Teste 296`** (Governança de Continuidade de Negócios e Acordos de Nível de Serviço / SLAs de restauração em tribunais): Preservada.
* **`Teste 297`** (Criptografia em Bancos de Dados: Criptografia de Dados Transparentes / TDE em repouso e TLS/SSL em trânsito): Preservada.
* **`Teste 298`** (Privacidade e LGPD: Mascaramento Dinâmico de Dados / DDM para proteção de dados pessoais e sigilosos em consultas analíticas): Preservada.
* **`Teste 299`** (Controle de Acesso Granular: *Role-Based Access Control* - RBAC e Segurança em Nível de Linha / *Row-Level Security* - RLS no PostgreSQL): Preservada.


---

## Caderno 01 (IA & Ciência de Dados): Fundamentos de IA, Machine Learning e Deep Learning
* **Arquivo:** `docs/conhecimentos_especificos_b02_ti/09_inteligencia_artificial_e_ciencia_de_dados/01_fundamentos_ia_machine_learning_e_deep_learning.md`
* **Status:** Concluído e sincronizado

### 1. O que ENTRA (Questões Reais de Concurso)
* **`Teste 302`**: Substituído pela questão real **`V3_FGV_TCE_GO_2024_Q0311`**
  * **Banca/Órgão/Ano/Cargo:** **FGV – TCE/GO – 2024 – Analista de Controle Externo (Tecnologia da Informação)**
  * **Conceito Aderente:** Fundamentos do classificador probabilístico supervisionado Naive Bayes e a premissa canônica de independência condicional entre os atributos preditores dada a classe alvo.
* **`Teste 304`**: Substituído pela questão real **`V3_FGV_TCE_SC_2026_Q3138`**
  * **Banca/Órgão/Ano/Cargo:** **FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo (Administração / TI)**
  * **Conceito Aderente:** Fenômeno técnico de *Overfitting* (sobreajuste) em modelo de inteligência artificial voltado à detecção de fraudes em licitações públicas em Tribunais de Contas (alta precisão no treino histórico e perda de generalização para dados novos).

### 2. O que SAI (Questões Autorais/Simuladas)
* **`Teste 302`**: Simulado sobre o classificador Naive Bayes e Teorema de Bayes.
* **`Teste 304`**: Simulado sobre trade-off viés-variância e regularização L1/L2.

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 300`** (Definições de IA segundo Russell & Norvig: As quatro abordagens - Pensar/Agir como Humanos vs Racionalmente): Preservada.
* **`Teste 301`** (Evolução da IA: Abordagem Simbólica / Sistemas Especialistas vs Conexionista / Redes Neurais): Preservada.
* **`Teste 303`** (Árvores de Decisão, Random Forest e Algoritmos de Ensemble: *Bagging* vs *Boosting* / XGBoost): Preservada.
* **`Teste 305`** (Aprendizado Não Supervisionado: Algoritmos de Agrupamento *K-Means* vs *DBSCAN* baseado em densidade): Preservada.
* **`Teste 306`** (Redução de Dimensionalidade com PCA - Questão Oficial FGV TRT 2024 TI): Preservada.
* **`Teste 307`** (Aprendizado por Reforço / RL: Agente, Ambiente, Recompensa e Função de Valor no Processo de Decisão de Markov): Preservada.
* **`Teste 308`** (Funções de Ativação Não-Lineares em Deep Learning: ReLU, Sigmoide, Tanh e Leaky ReLU): Preservada.
* **`Teste 309`** (Otimização em Deep Learning: Algoritmo de *Backpropagation*, Descida do Gradiente Estocástica - SGD e Otimizador Adam): Preservada.
* **`Teste 310`** (Arquiteturas Neurais Profundas: CNNs para dados espaciais/imagens vs RNNs/LSTMs para dados sequenciais temporais): Preservada.


---

## Caderno 02 (IA & Ciência de Dados): NLP, IA Generativa, Agentes e Multimodalidade
* **Arquivo:** `docs/conhecimentos_especificos_b02_ti/09_inteligencia_artificial_e_ciencia_de_dados/02_nlp_ia_generativa_agentes_e_multimodalidade.md`
* **Status:** Concluído e sincronizado

### 1. O que ENTRA (Questões Reais de Concurso)
* **`Teste 311`**: Substituído pela questão real **`V3_FGV_TCE_GO_2024_Q0316`**
  * **Banca/Órgão/Ano/Cargo:** **FGV – TCE/GO – 2024 – Analista de Controle Externo (Tecnologia da Informação)**
  * **Conceito Aderente:** Paradigmas fundamentais do Processamento de Linguagem Natural (PLN): o paradigma Simbólico (regras gramaticais e dicionários) e o paradigma Neural (*Deep Learning* e modelos densos de linguagem).
* **`Teste 315`**: Substituído pela questão real **`V3_FGV_TCE_GO_2024_Q0318`**
  * **Banca/Órgão/Ano/Cargo:** **FGV – TCE/GO – 2024 – Analista de Controle Externo (Tecnologia da Informação)**
  * **Conceito Aderente:** Categorias seminais e amplas de modelos de Inteligência Artificial Generativa: Autocodificadores Variacionais (VAEs) e Redes Adversárias Generativas (GANs).

### 2. O que SAI (Questões Autorais/Simuladas)
* **`Teste 311`**: Simulado sobre esteira analítica e pré-processamento de PLN (tokenização, lematização, stop words).
* **`Teste 315`**: Simulado sobre síntese multimodal com GANs e VAEs.

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 312`** (Representação Numérica de Texto: Bag-of-Words, TF-IDF e Modelos Vetoriais Densos Word2Vec / FastText): Preservada.
* **`Teste 313`** (A Revolução do Transformer: Mecanismo de Atenção Multi-Head e modelos pré-treinados BERT vs GPT): Preservada.
* **`Teste 314`** (Fundamentos de IA Generativa: Modelagem Probabilística Generativa vs Modelos Discriminativos Tradicionais): Preservada.
* **`Teste 316`** (Modelos de Difusão / *Diffusion Models*: Processo direto de adição de ruído gaussiano e processo reverso de desnoising): Preservada.
* **`Teste 317`** (LLMs Autoregressivos: Mecanismo de Inferência Token-by-Token, amostragem e estratégias de decoding): Preservada.
* **`Teste 318`** (Sistemas Agentivos: Padrão ReAct - *Reasoning + Acting*, decomposição de objetivos e planejamento autônomo): Preservada.
* **`Teste 319`** (Ferramental e Interoperabilidade de Agentes: Mecanismos de *Tool Calling* / *Function Calling* via JSON Schemas): Preservada.
* **`Teste 320`** (Inteligência Artificial Multimodal: Processamento simultâneo e alinhamento de texto, visão computacional e áudio): Preservada.
* **`Teste 321`** (Visão Computacional Aplicada a Documentos Públicos: OCR neural e extração de layouts com modelos de visão-linguagem): Preservada.


---

## Caderno 03 (IA & Ciência de Dados): Engenharia de Prompts, RAG e Automação de Processos
* **Arquivo:** `docs/conhecimentos_especificos_b02_ti/09_inteligencia_artificial_e_ciencia_de_dados/03_engenharia_de_prompts_rag_e_automacao_processos.md`
* **Status:** Auditado e aprovado sem necessidade de substituição (100% de preservação pedagógica)

### 1. O que ENTRA (Questões Reais de Concurso)
* *Nenhuma.* (Todas as 11 questões abordam técnicas hiper-recentes de orquestração de IA generativa no setor público: Zero-Shot/Few-Shot, Chain-of-Thought, Prompt Caching, pipelines avançados de RAG com reranker e reciprocal rank fusion, avaliação com métricas RAGAS, frameworks LangChain/LlamaIndex e orquestração cognitiva com RPA; mantidas 100% intactas para preservar o vanguardismo pedagógico).

### 2. O que SAI (Questões Autorais/Simuladas)
* *Nenhuma.*

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 322`** (Engenharia de Prompts: Princípios de Clareza, Delimitadores, Instruções Negativas e Formatos de Saída Estruturados JSON): Preservada.
* **`Teste 323`** (Técnicas de Raciocínio em Prompts: *Chain-of-Thought* / CoT e *Tree-of-Thoughts* para raciocínio contábil-fiscal complexo): Preservada.
* **`Teste 324`** (Técnica de *Few-Shot Prompting*: Fornecimento de pares representativos de entrada-saída no prompt para guiar o LLM): Preservada.
* **`Teste 325`** (Otimização de Custos e Latência: Mecanismo de *Prompt Caching* em servidores de inferência de LLMs): Preservada.
* **`Teste 326`** (Pipeline Avançado de RAG: *Syntax-Aware Chunking*, geração de embeddings e busca híbrida Dense + Sparse): Preservada.
* **`Teste 327`** (Re-ranking em RAG: Utilização de modelos neurais *Cross-Encoder* para reordenar candidatos e maximizar a relevância dos chunks): Preservada.
* **`Teste 328`** (Avaliação de Pipelines RAG: Framework *RAGAS* e métricas de *Faithfulness*, *Answer Relevance* e *Context Recall*): Preservada.
* **`Teste 329`** (Frameworks de Desenvolvimento de IA: LangChain e LlamaIndex, abstrações de índices, retrievers e memórias de sessão): Preservada.
* **`Teste 330`** (Automação Inteligente de Processos / IPA: Integração de RPA tradicional determinístico com LLMs generativos e visão): Preservada.
* **`Teste 331`** (Triagem Automatizada de Processos: Classificação de denúncias e priorização de fiscalizações em órgãos de controle com IA): Preservada.
* **`Teste 332`** (Human-in-the-Loop na Automação Pública: Diretrizes para homologação humana obrigatória em atos de decisão fiscal): Preservada.


---

## Caderno 04 (IA & Ciência de Dados): Ciência de Dados, Estatística e Big Data
* **Arquivo:** `docs/conhecimentos_especificos_b02_ti/09_inteligencia_artificial_e_ciencia_de_dados/04_ciencia_de_dados_estatistica_e_big_data.md`
* **Status:** Concluído e sincronizado

### 1. O que ENTRA (Questões Reais de Concurso)
* **`Teste 335`**: Substituído pela questão real **`V3_FGV_TCE_PA_2024_Q2602`**
  * **Banca/Órgão/Ano/Cargo:** **FGV – TCE/PA – 2024 – Auditor de Controle Externo (Ciência de Dados / TI)**
  * **Conceito Aderente:** Estratégias metodológicas para tratamento de dados ausentes (*missing data*) no treinamento de modelos de aprendizado de máquina: imputação com KNN exigindo normalização/padronização prévia dos dados para equalizar as distâncias euclidianas.
* **`Teste 343`**: Substituído pela questão real **`V3_FGV_TCE_SC_2026_Q3290`**
  * **Banca/Órgão/Ano/Cargo:** **FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo (TI - Ciências da Computação)**
  * **Conceito Aderente:** Otimização de processamento distribuído no Apache Spark 3.x sobre bilhões de notas fiscais em Tribunais de Contas: uso do *Adaptive Query Execution* (AQE) com *Skew Join Optimization* para divisão automática de partições sobrecarregadas (*data skew*).

### 2. O que SAI (Questões Autorais/Simuladas)
* **`Teste 335`**: Simulado sobre padronização de dados (*Z-Score*) e imputação de valores atípicos.
* **`Teste 343`**: Simulado sobre Spark SQL, transformações preguiçosas (*lazy evaluation*) e gargalos de shuffle.

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 333`** (Ciclo de Vida da Ciência de Dados: Metodologia CRISP-DM e suas seis fases iterativas): Preservada.
* **`Teste 334`** (Detecção de Outliers e Anomalias em Dados Fiscais: Regra dos Três Sigmas e critério do Intervalo Interquartil / IQR): Preservada.
* **`Teste 336`** (Estatística Descritiva: Média, Mediana, Moda, Variância e Desvio Padrão sob distribuições assimétricas): Preservada.
* **`Teste 337`** (Distribuição Normal e Teorema Central do Limite: Propriedades matemáticas e relevância para inferência amostral): Preservada.
* **`Teste 338`** (Testes de Hipóteses Estatísticos: Erro Tipo I ($lpha$), Erro Tipo II ($eta$), Nível de Significância e p-valor em auditorias): Preservada.
* **`Teste 339`** (Trade-off Viés-Variância / *Bias-Variance Trade-off* e decomposição do erro quadrático médio em aprendizado supervisionado): Preservada.
* **`Teste 340`** (Métricas de Classificação em Dados Desbalanceados: Acurácia, Precisão, Revocação / Sensibilidade e F1-Score): Preservada.
* **`Teste 341`** (Curva ROC e Métrica AUC-ROC: Avaliação de classificadores sob diferentes pontos de corte / thresholds de decisão): Preservada.
* **`Teste 342`** (Ecossistema Big Data Hadoop: Arquitetura distribuída HDFS - NameNode/DataNode e framework MapReduce): Preservada.


---

## Caderno 05 (IA & Ciência de Dados): Ética, IA Responsável, EBIA e LGPD
* **Arquivo:** `docs/conhecimentos_especificos_b02_ti/09_inteligencia_artificial_e_ciencia_de_dados/05_etica_ia_responsavel_ebia_e_lgpd.md`
* **Status:** Auditado e aprovado sem necessidade de substituição (100% de preservação pedagógica)

### 1. O que ENTRA (Questões Reais de Concurso)
* *Nenhuma.* (Todas as 11 questões abordam minuciosamente o arcabouço normativo e ético aplicável à IA governamental: Princípios da OCDE, viés e justiça algorítmica, equidade demográfica, explicabilidade pós-hoc com SHAP e LIME, LGPD art. 20 sobre revisão humana de decisões automatizadas, Resolução CNJ nº 332/2020 e os eixos estratégicos da EBIA - Portaria MCTI nº 4.617/2021; mantidas 100% intactas para assegurar domínio absoluto das diretrizes legais).

### 2. O que SAI (Questões Autorais/Simuladas)
* *Nenhuma.*

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 344`** (Princípios da OCDE para Inteligência Artificial Confiável: Crescimento inclusivo, valores centrados no ser humano e transparência): Preservada.
* **`Teste 345`** (Viés Algorítmico e Discriminação Indireta: Fontes de contaminação histórica em bases de dados governamentais): Preservada.
* **`Teste 346`** (Métricas Matemáticas de Justiça / *Fairness*: Paridade Demográfica / *Demographic Parity* vs Oportunidade Igual / *Equal Opportunity*): Preservada.
* **`Teste 347`** (Dilema entre Precisão Preditiva vs Interpretabilidade em Modelos de Machine Learning no setor público): Preservada.
* **`Teste 348`** (Métodos de Explicabilidade de Modelos: *Feature Importance* intrínseca vs técnicas agnósticas pós-hoc): Preservada.
* **`Teste 349`** (Explicabilidade Local com LIME e SHAP: Fundamentação nos valores de Shapley da teoria dos jogos cooperativos): Preservada.
* **`Teste 350`** (LGPD e Inteligência Artificial: Bases legais de tratamento pelo poder público e princípio da não-discriminação): Preservada.
* **`Teste 351`** (Art. 20 da LGPD: Direito do titular à revisão de decisões tomadas unicamente com base em tratamento automatizado de dados): Preservada.
* **`Teste 352`** (Resolução CNJ nº 332/2020: Diretrizes de governança, transparência, auditoria técnica e supervisão humana em tribunais): Preservada.
* **`Teste 353`** (Estratégia Brasileira de Inteligência Artificial / EBIA: Objetivos gerais e os três eixos transversais da Portaria MCTI nº 4.617/2021): Preservada.
* **`Teste 354`** (Eixos Verticais de Aplicação da EBIA: Legislação, regulação e uso ético, governança de IA e segurança pública): Preservada.


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


---

## Caderno 02 (IA & Agentivos): Arquitetura de Sistemas Agentivos e Ferramentas CLI / IDE
* **Arquivo:** `docs/conhecimentos_especificos_b02_ti/06_engenharia_software_ia_e_sistemas_agentivos/02_arquitetura_de_sistemas_agentivos_e_ferramentas_cli_ide.md`
* **Status:** Auditado e aprovado sem necessidade de substituição

### 1. O que ENTRA (Questões Reais de Concurso)
* *Nenhuma.* (Tópico de ponta emergente no edital do TCE-GO; não há no histórico de concursos de TI questões oficiais abordando arquitetura canônica de 4 pilares de agentes, *The Agentic Loop*, *Stop Conditions* / disjuntores de agentes, arquiteturas multiagente hierárquicas ou governança de ferramentas agentivas CLI/IDE).

### 2. O que SAI (Questões Autorais/Simuladas)
* *Nenhuma.*

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 129`** (Transição de Chatbots Passivos para Sistemas Agentivos Orientados a Objetivos): Preservada.
* **`Teste 130`** (Arquitetura Canônica de 4 Pilares: Modelo, Memória, Ferramentas e Planejamento): Preservada.
* **`Teste 131`** (Comparativo Arquitetural: Assistentes Agentivos CLI vs Extensões de IDE): Preservada.
* **`Teste 132`** (The Agentic Loop: Ciclo contínuo de Percepção, Raciocínio, Ação, Observação e Reflexão): Preservada.
* **`Teste 133`** (Fase de Percepção e Descoberta de Contexto em Projetos de Software): Preservada.
* **`Teste 134`** (Planejamento e Decomposição de Metas / *Task Decomposition* em Subtarefas): Preservada.
* **`Teste 135`** (Fase de Ação e Uso de Ferramentas / *Tool Calling* em Terminal e Código): Preservada.
* **`Teste 136`** (Critérios de Parada / *Stop Conditions* e Disjuntores contra Loops Infinitos de Agentes): Preservada.
* **`Teste 137`** (Arquiteturas Multiagente Hierárquicas: Agente Orquestrador delegando a Subagentes Especialistas): Preservada.
* **`Teste 138`** (Governança, Menor Privilégio e Mecanismos *Human-in-the-Loop* em Agentes Autônomos): Preservada.


---

## Caderno 01 (Dir. Administrativo): Regime Jurídico, Princípios e LINDB
* **Arquivo:** `docs/conhecimentos_especificos_a01_tecnico_administrativo/15_nocoes_de_direito_administrativo/01_regime_juridico_principios_e_lindb.md`
* **Status:** Auditado e aprovado com 4 questões oficiais consolidadas e 7 autorais preservadas

### 1. O que ENTRA (Questões Reais de Concurso)
* *Nenhuma nova injeção requerida.* O caderno já conta com quatro questões reais oficiais plenamente integradas:
  * **`Teste 003`**: Questão Oficial FCC (TRT-9 2015 - Princípios do Direito Administrativo).
  * **`Teste 007`**: Questão Oficial FCC (TRT-9 2015 - Princípio da Autotutela e Súmula 473 do STF).
  * **`Teste 008`**: Questão Oficial FGV (TRT 2024 - Princípios da Legalidade, Moralidade e Boa-Fé).
  * **`Teste 010`**: Questão Oficial FGV (TJ-MT 2024 - LINDB no Judiciário).

### 2. O que SAI (Questões Autorais/Simuladas)
* *Nenhuma.*

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 001`** (Conceito e Sentidos de Administração Pública: Sentido Subjetivo/Formal/Orgânico vs Objetivo/Material/Funcional): Preservada.
* **`Teste 002`** (Regime Jurídico-Administrativo: Princípio da Supremacia do Interesse Público sobre o Privado e Princípio da Indisponibilidade do Interesse Público): Preservada.
* **`Teste 004`** (Princípio da Impessoalidade e Publicidade Institucional: Vedação de nomes, símbolos e imagens para promoção pessoal de autoridades no art. 37, § 1º da CF/88): Preservada.
* **`Teste 005`** (Princípio da Moralidade Administrativa e Súmula Vinculante nº 13 do STF sobre Nepotismo em cargos de comissão e confiança): Preservada.
* **`Teste 006`** (Princípio da Eficiência: Emenda Constitucional nº 19/1998, produtividade, celeridade e desburocratização no serviço público): Preservada.
* **`Teste 009`** (Princípio da Motivação e Teoria dos Motivos Determinantes: Vinculação da validade do ato administrativo aos motivos fáticos e jurídicos alegados na portaria): Preservada.
* **`Teste 011`** (Segurança Jurídica na LINDB: Artigos 20 a 30 da Lei nº 13.655/2018, consideração das consequências práticas da decisão, vedação de anulação baseada em valores jurídicos abstratos e erro grosseiro): Preservada.


---

## Caderno 02 (Dir. Administrativo): Organização Administrativa e Poderes
* **Arquivo:** `docs/conhecimentos_especificos_a01_tecnico_administrativo/15_nocoes_de_direito_administrativo/02_organizacao_administrativa_e_poderes.md`
* **Status:** Auditado e aprovado com questão oficial FGV 2022 consolidada e 10 autorais preservadas

### 1. O que ENTRA (Questões Reais de Concurso)
* *Nenhuma nova injeção requerida.* O caderno já conta com questão oficial FGV plenamente integrada:
  * **`Teste 012`**: Questão Oficial FGV (TRT 2022 - Descentralização administrativa por serviços vs Desconcentração de órgãos internos).

### 2. O que SAI (Questões Autorais/Simuladas)
* *Nenhuma.*

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 013`** (Autarquias: Criação direta por lei específica, personalidade jurídica de direito público, patrimônio próprio, regime estatutário e controle finalístico por tutela/supervisão ministerial): Preservada.
* **`Teste 014`** (Empresas Públicas e Sociedades de Economia Mista: Distinções de regime jurídico, forma societária, foro processual e participação de capital público vs privado): Preservada.
* **`Teste 015`** (Estatuto Jurídico das Estatais - Lei nº 13.303/2016: Governança corporativa, vedações a indicações políticas para diretorias e conselho de administração): Preservada.
* **`Teste 016`** (Fundações Públicas: Personalidade de direito público ou privado, área de atuação delimitada por lei complementar e regime híbrido de bens e pessoal): Preservada.
* **`Teste 017`** (Terceiro Setor e Entidades Paraestatais: Regime de cooperação com Organizações Sociais - OS via Contrato de Gestão e OSCIPs via Termo de Parceria): Preservada.
* **`Teste 018`** (Poder Hierárquico: Relações de subordinação interna, delegação e avocação de competências nos termos do regime de processo administrativo): Preservada.
* **`Teste 019`** (Poder Disciplinar: Apuração de faltas funcionais, sanções a servidores públicos estatutários e a particulares sujeitos a vínculo contratual específico): Preservada.
* **`Teste 020`** (Poder Regulamentar e Normativo: Decretos de regulamentação do Chefe do Executivo vs Decretos Autônomos nos termos do art. 84, VI da CF/88): Preservada.
* **`Teste 021`** (Poder de Polícia: Conceito, competência, atributos de discricionariedade, autoexecutoriedade e coercibilidade, e limites da sanção administrativa): Preservada.
* **`Teste 022`** (Abuso de Poder: Diferenciação dogmática entre Excesso de Poder - vício no elemento competência vs Desvio de Finalidade / Desvio de Poder - vício no elemento finalidade pública): Preservada.


---

## Caderno 03 (Dir. Administrativo): Atos Administrativos e Processo Estadual
* **Arquivo:** `docs/conhecimentos_especificos_a01_tecnico_administrativo/15_nocoes_de_direito_administrativo/03_atos_administrativos_e_processo_estadual.md`
* **Status:** Concluído e sincronizado

### 1. O que ENTRA (Questões Reais de Concurso)
* **`Teste 030`**: Substituído pela questão real **`V3_FGV_TRF_1_2024_Q1095`**
  * **Banca/Órgão/Ano/Cargo:** **FGV – TRF/1 – 2024 – Analista Judiciario (Area Apoio Especializado)**
  * **Conceito Aderente:** Extinção do ato administrativo por contraposição (ou derrubada), decorrente da superveniência de ato administrativo posterior com efeitos jurídicos frontalmente incompatíveis com o ato precedente (ex.: o ato de exoneração que extingue o ato anterior de nomeação de servidor).

### 2. O que SAI (Questões Autorais/Simuladas)
* **`Teste 030`**: Simulado sobre as modalidades de extinção do ato administrativo (caducidade, cassação, contraposição).

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 023`** (Teoria dos Três Planos do Ato Administrativo: Existência, Validade e Eficácia no Direito Público): Preservada.
* **`Teste 024`** (Elementos/Requisitos de Validade do Ato: Competência, Finalidade, Forma, Motivo e Objeto nos termos da Lei da Ação Popular): Preservada.
* **`Teste 025`** (Vícios de Validade: Incompetência e convalidação via ratificação vs Usurpação de função e Desvio de Finalidade): Preservada.
* **`Teste 026`** (Atributos do Ato Administrativo: Presunção de Legitimidade e Veracidade, Imperatividade, Autoexecutoriedade e Tipicidade): Preservada.
* **`Teste 027`** (Autoexecutoriedade em Ações de Polícia Sanitária e Limites de Exigibilidade e Execução Direta sem ordem judicial): Preservada.
* **`Teste 028`** (Classificação dos Atos Administrativos quanto à Formação da Vontade: Atos Simples, Atos Compostos e Atos Complexos): Preservada.
* **`Teste 029`** (Aposentadoria de Servidor perante Tribunal de Contas como Ato Complexo canônico segundo a jurisprudência do STF): Preservada.
* **`Teste 031`** (Invalidação e Convalidação: Anulação de atos ilegais ex tunc vs Revogação de atos discricionários válidos e inconvenientes ex nunc): Preservada.
* **`Teste 032`** (Delegação e Avocação de Competências: Vedações legais da edição de atos normativos, decisão de recursos administrativos e competência exclusiva): Preservada.
* **`Teste 033`** (Processo Administrativo Estadual de Goiás - Lei nº 13.800/2001: Princípios do devido processo legal, gratuidade e direito à ampla defesa): Preservada.


---

## Caderno 04 (Dir. Administrativo): Serviços Públicos, Bens e Responsabilidade Civil
* **Arquivo:** `docs/conhecimentos_especificos_a01_tecnico_administrativo/15_nocoes_de_direito_administrativo/04_servicos_publicos_bens_e_responsabilidade_civil.md`
* **Status:** Concluído e sincronizado

### 1. O que ENTRA (Questões Reais de Concurso)
* **`Teste 035`**: Substituído pela questão real **`V3_FGV_TJ_AP_2023_Q0494`**
  * **Banca/Órgão/Ano/Cargo:** **FGV – TJ/AP – 2023 – Analista Judiciario (Apoio Especializado)**
  * **Conceito Aderente:** Fundamentos da Responsabilidade Civil Extracontratual do Estado sob a égide do art. 37, § 6º da CF/88: consagração da Teoria do Risco Administrativo, impondo responsabilidade civil OBJETIVA às pessoas jurídicas de direito público e delegatárias, admitindo a comprovação de causas excludentes do nexo de causalidade.
* **`Teste 037`**: Substituído pela questão real **`V3_FGV_TRT_1_2024_Q1062`**
  * **Banca/Órgão/Ano/Cargo:** **FGV – TRT/1 – 2024 – Analista Judiciário (Área Administrativa)**
  * **Conceito Aderente:** Orientação vinculante do STF sobre Responsabilidade Civil do Estado e legitimidade passiva (Tema 940 de Repercussão Geral): a ação indenizatória deve ser ajuizada estritamente contra o Estado, sendo o agente público parte passiva ilegítima, cabendo ação regressiva contra o servidor nos casos comprovados de dolo ou culpa.

### 2. O que SAI (Questões Autorais/Simuladas)
* **`Teste 035`**: Simulado comparativo entre a Teoria do Risco Administrativo e a Teoria do Risco Integral.
* **`Teste 037`**: Simulado sobre acidente de trânsito com viatura de tribunal e regresso contra o servidor.

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 034`** (Responsabilidade Civil do Estado por Atos Comissivos de seus Agentes: Nexo causal, dano material/moral e desnecessidade de dolo ou culpa): Preservada.
* **`Teste 036`** (Responsabilidade Civil do Estado por Omissão: Distinção entre Omissão Genérica - culpa anônima/subjetiva vs Omissão Específica - dever legal de custódia e proteção): Preservada.
* **`Teste 038`** (Princípios dos Serviços Públicos na Lei nº 8.987/1995: Serviço adequado e princípios da continuidade, regularidade, atualidade e modicidade tarifária): Preservada.
* **`Teste 039`** (Regimes de Delegação de Serviços Públicos: Concessão comum precedida de licitação modalidade concorrência vs Permissão precária): Preservada.
* **`Teste 040`** (Extinção dos Contratos de Concessão de Serviços Públicos: Encampação por interesse público mediante lei autorizativa vs Caducidade por inadimplemento): Preservada.
* **`Teste 041`** (Parcerias Público-Privadas - Lei nº 11.079/2004: Concessão Patrocinada com tarifa do usuário mais contraprestação pública vs Concessão Administrativa): Preservada.
* **`Teste 042`** (Classificação dos Bens Públicos no Código Civil art. 99: Bens de uso comum do povo, bens de uso especial e bens dominicais): Preservada.
* **`Teste 043`** (Afetação e Desafetação de Bens Públicos: Consagração ao serviço público e alienação condicionada de bens dominicais): Preservada.
* **`Teste 044`** (Regime Jurídico dos Bens Públicos: Inalienabilidade relativa, impenhorabilidade, não-onerabilidade e imprescritibilidade imune a usucapião): Preservada.


---

## Caderno 05 (Dir. Administrativo): Controle da Administração e Improbidade Administrativa
* **Arquivo:** `docs/conhecimentos_especificos_a01_tecnico_administrativo/15_nocoes_de_direito_administrativo/05_controle_da_administracao_e_improbidade_administrativa.md`
* **Status:** Concluído e sincronizado

### 1. O que ENTRA (Questões Reais de Concurso)
* **`Teste 053`**: Substituído pela questão real **`V3_FGV_TRT_DA_24__REGI_O_2025_Q0915`**
  * **Banca/Órgão/Ano/Cargo:** **FGV – TRT da 24º Região – 2025 – Analista Judiciário (Área Administrativa - Contabilidade)**
  * **Conceito Aderente:** Tipologia dos atos de improbidade administrativa na Lei nº 8.429/1992 com as reformas estruturais da Lei nº 14.230/2021: enquadramento exato das condutas de Prejuízo ao Erário (art. 10), Atentado aos Princípios da Administração Pública (art. 11) e Enriquecimento Ilícito (art. 9º).
* **`Teste 054`**: Substituído pela questão real **`V3_FGV_TCE_SC_2026_Q3267`**
  * **Banca/Órgão/Ano/Cargo:** **FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo (TI - Ciências da Computação)**
  * **Conceito Aderente:** Sanções pecuniárias e limites legais na Lei de Improbidade Administrativa (art. 12, III): aplicação de multa civil de até 24 vezes a remuneração para atos dolosos que atentam contra os princípios da administração pública (art. 11, VIII - descumprir normas de parcerias com entidades privadas).

### 2. O que SAI (Questões Autorais/Simuladas)
* **`Teste 053`**: Simulado sobre as três modalidades de atos de improbidade administrativa na reforma da Lei 14.230/2021.
* **`Teste 054`**: Simulado sobre a revogação do rol exemplificativo do art. 11 e a exigência de dolo específico.

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 045`** (Sistemática Constitucional de Controle Interno e Externo nos arts. 70 a 75 da CF/88): Preservada.
* **`Teste 046`** (Eficácia de Título Executivo Extrajudicial dos Acórdãos de Tribunais de Contas que imputam débito e multa): Preservada.
* **`Teste 047`** (Competências Constitucionais Privativas dos Tribunais de Contas: Julgamento de contas de gestores vs Parecer prévio sobre contas de Chefes do Executivo): Preservada.
* **`Teste 048`** (Tomada de Contas Especial / TCE perante o Tribunal de Contas de Goiás: Procedimento apuratório de omissão e desvio de verbas): Preservada.
* **`Teste 049`** (Controle Judicial dos Atos Administrativos: Mandado de Segurança individual e coletivo para tutela de direito líquido e certo): Preservada.
* **`Teste 050`** (Ação Popular - Lei nº 4.717/1965 e Ação Civil Pública - Lei nº 7.347/1985 para proteção da moralidade e patrimônio público): Preservada.
* **`Teste 051`** (Conceito Amplo de Agente Público na Lei de Improbidade: Estagiários, terceirizados e particulares em colaboração com o poder público): Preservada.
* **`Teste 052`** (Exigência Universal de Dolo Específico: Extinção definitiva da modalidade culposa de improbidade administrativa pela Lei nº 14.230/2021): Preservada.
* **`Teste 055`** (Legitimidade Processual Ativa Exclusiva do Ministério Público para a Ação de Improbidade Administrativa conforme decisão do STF na ADI 7042): Preservada.


---

## Caderno 06 (Dir. Administrativo): Acesso à Informação e Contratos de Publicidade
* **Arquivo:** `docs/conhecimentos_especificos_a01_tecnico_administrativo/15_nocoes_de_direito_administrativo/06_acesso_a_informacao_e_contratos_publicidade.md`
* **Status:** Concluído e sincronizado

### 1. O que ENTRA (Questões Reais de Concurso)
* **`Teste 056`**: Substituído pela questão real **`V3_FGV_TJ_SC_2026_Q0078`**
  * **Banca/Órgão/Ano/Cargo:** **FGV – TJ/SC – 2026 – Analista Administrativo**
  * **Conceito Aderente:** Lei de Acesso à Informação (Lei Federal nº 12.527/2011) e Lei de Responsabilidade Fiscal: distinção jurídica e operacional entre Transparência Ativa (divulgação espontânea no portal oficial sem necessidade de solicitação) e Transparência Passiva (fornecimento de informações e documentos mediante requerimento formal no SIC).

### 2. O que SAI (Questões Autorais/Simuladas)
* **`Teste 056`**: Simulado sobre as diretrizes gerais e a cultura de transparência como regra na Lei de Acesso à Informação.

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 057`** (Transparência Ativa na Remuneração de Servidores Públicos: Legitimidade da divulgação de nomes e vencimentos brutos segundo jurisprudência vinculante do STF): Preservada.
* **`Teste 058`** (Procedimento de Acesso à Informação: Prazos legais de resposta imediata ou até 20 dias prorrogáveis por 10 dias justificadamente perante o SIC): Preservada.
* **`Teste 059`** (Recursos Administrativos contra o Indeferimento de Acesso à Informação: Prazos e instâncias recursais no âmbito executivo): Preservada.
* **`Teste 060`** (Classificação de Sigilo de Informações na LAI: Prazos máximos legais - Ultrassecreta 25 anos, Secreta 15 anos e Reservada 5 anos): Preservada.
* **`Teste 061`** (Competência Funcional para Classificação de Sigilo no âmbito da Administração Pública Estadual): Preservada.
* **`Teste 062`** (Proteção de Informações Pessoais relativas à intimidade, honra e imagem: Restrição de acesso pelo prazo máximo de 100 anos nos termos do art. 31 da LAI): Preservada.
* **`Teste 063`** (Regime Específico de Contratação de Publicidade - Lei nº 12.232/2010: Licitação obrigatória por Concorrência ou Concurso e vedação ao Pregão): Preservada.
* **`Teste 064`** (Julgamento de Propostas Técnicas em Publicidade: Submissão de propostas desidentificadas a Subcomissão Técnica sorteada com membros externos): Preservada.
* **`Teste 065`** (Subcontratação de Serviços Especializados em Contratos de Publicidade: Cotação de preços e regras de faturamento direto): Preservada.


---

# Módulo 01 (Conhecimentos Gerais): Língua Portuguesa
* **Pasta:** `docs/conhecimentos_gerais/01_lingua_portuguesa/`
* **Data da Auditoria e Injeção RAG:** 2026-11-03
* **Cadernos Auditados:** 7 cadernos (`01_compreensao_e_interpretacao_de_texto.md` a `07_redacao_oficial.md`)
* **Total de Questões no Módulo:** 71 questões (Testes 001 a 071)
* **Questões Reais Injetadas via RAG:** 7 questões (100% aderentes, foco FGV 2024-2026 e Tribunais de Contas)
* **Questões Autorais/Simuladas Preservadas:** 64 questões

---

## Caderno 01: Compreensão, Interpretação e Tipologia Textual
* **Arquivo:** `docs/conhecimentos_gerais/01_lingua_portuguesa/01_compreensao_e_interpretacao_de_texto.md`
* **Status:** Concluído e sincronizado

### 1. O que ENTRA (Questões Reais de Concurso)
* **`Teste 002`**: Substituído pela questão real **`V3_FGV_TJ_RR_2024_Q1211`**
  * **Banca/Órgão/Ano/Cargo:** **FGV – TJ/RR – 2024 – Analista Judiciário (Gestão e Governança de TI)**
  * **Conceito Aderente:** Variação linguística e níveis de linguagem: identificação de traços distintivos e marcas típicas da língua falada/oralidade espontânea (uso de interrupções, reformulações e truncamentos para melhoria da expressão e ajuste enunciativo imediato) em contraposição ao planejamento linear da língua escrita.
* **`Teste 006`**: Substituído pela questão real **`V3_FGV_TJ_SC_2026_Q0001`**
  * **Banca/Órgão/Ano/Cargo:** **FGV – TJ/SC – 2026 – Analista Administrativo**
  * **Conceito Aderente:** Semântica e estilística na banca FGV: articulação discursiva entre linguagem verbal e não verbal em campanha institucional/publicitária, explorando a polissemia e o duplo sentido da palavra "estado" (unidade federativa vs condição/estado emocional de alegria).

### 2. O que SAI (Questões Autorais/Simuladas)
* **`Teste 002`**: Simulado sobre identificação de gêneros textuais (editorial vs notícia/ensaio).
* **`Teste 006`**: Simulado preliminar sobre conotação e sentido figurado.

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 001`** (Compreensão Textual vs Interpretação e Inferência Autorizada na análise de inteligência artificial na gestão pública): Preservada.
* **`Teste 003`** (Tipologia Narrativa e Descritiva em relatórios de auditoria e sessões de julgamento): Preservada.
* **`Teste 004`** (Tese e Estratégias Argumentativas na tipologia dissertativa): Preservada.
* **`Teste 005`** (Identificação de Pressupostos e Subentendidos em textos institucionais): Preservada.
* **`Teste 007`** (Modalidades de Discurso: Identificação de Discurso Indireto Livre em excerto reflexivo): Preservada.
* **`Teste 008`** (Transposição de Discurso Direto para Discurso Indireto e correlação temporal): Preservada.
* **`Teste 009`** (Relações Intertextuais: Paráfrase, Paródia, Citação e Alusão): Preservada.
* **`Teste 010`** (Figuras de Linguagem Semânticas e de Pensamento: Metáfora, Metonímia, Antítese e Paradoxo): Preservada.
* **`Teste 011`** (Figuras de Sintaxe e Construção: Anacoluto, Elipse, Zeugma e Pleonasmo Enfático): Preservada.

---

## Caderno 02: Ortografia, Acentuação Gráfica e Formação de Palavras
* **Arquivo:** `docs/conhecimentos_gerais/01_lingua_portuguesa/02_ortografia_acentuacao_e_formacao_de_palavras.md`
* **Status:** Concluído e sincronizado (100% questões autorais mantidas)

### 1. O que ENTRA (Questões Reais de Concurso)
* *Nenhuma injeção:* Banco de dados vetorial continha apenas itens C/E descalibrados; preservada a integridade didática superior das 10 questões de múltipla escolha desenhadas sob medida para controle externo.

### 2. O que SAI (Questões Autorais/Simuladas)
* *Nenhuma.*

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 012`** (Acentuação Gráfica de Proparoxítonas e Paroxítonas terminadas em ditongo crescente): Preservada.
* **`Teste 013`** (Regra do Hiato e acentuação de I e U tônicos após o Novo Acordo Ortográfico): Preservada.
* **`Teste 014`** (Emprego do Hífen em Derivação Prefixal com prefixos auto, anti, infra, hiper e sub): Preservada.
* **`Teste 015`** (Ortografia Oficial: Grafia de vocábulos com J/G, X/CH e S/Z na administração pública): Preservada.
* **`Teste 016`** (Homônimos e Parônimos: Discriminar vs Descriminar, Mandado vs Mandato, Iminente vs Eminente): Preservada.
* **`Teste 017`** (Emprego das Quatro Formas dos Porquês em relatórios técnicos): Preservada.
* **`Teste 018`** (Justificativa Gramatical Idêntica para Acentuação em pares de vocábulos): Preservada.
* **`Teste 019`** (Processos Morfológicos de Formação: Derivação Parassintética vs Derivação Prefixal e Sufixal): Preservada.
* **`Teste 020`** (Derivação Regressiva ou Deverbal a partir de verbos de ação na gestão fiscal): Preservada.
* **`Teste 021`** (Derivação Imprópria ou Conversão Gramatical de classes de palavras): Preservada.

---

## Caderno 03: Morfossintaxe, Pronomes e Verbos
* **Arquivo:** `docs/conhecimentos_gerais/01_lingua_portuguesa/03_morfossintaxe_pronomes_e_verbos.md`
* **Status:** Concluído e sincronizado (100% questões autorais mantidas)

### 1. O que ENTRA (Questões Reais de Concurso)
* *Nenhuma injeção:* Questão histórica Q0209 apresentava enunciado truncado no banco vetorial; mantidas as 10 questões estruturadas do caderno.

### 2. O que SAI (Questões Autorais/Simuladas)
* *Nenhuma.*

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 022`** (Emprego de Pronomes Demonstrativos e funções dêiticas e anafóricas: este, esse, aquele): Preservada.
* **`Teste 023`** (Pronomes Relativos antecedidos de preposição e regência de cujo, quem, onde e a que): Preservada.
* **`Teste 024`** (Substituição de Complementos Verbais por Pronomes Oblíquos Átonos o, a, os, as, lo, la, no, na, lhe): Preservada.
* **`Teste 025`** (Colocação Pronominal: Próclise obrigatória com palavras atrativas e mesóclise com futuro): Preservada.
* **`Teste 026`** (Correlação de Tempos e Modos Verbais: Consecutio Temporum entre pretérito imperfeito do subjuntivo e futuro do pretérito do indicativo): Preservada.
* **`Teste 027`** (Valores Semânticos e Aspectuais dos Tempos do Modo Indicativo e Subjuntivo): Preservada.
* **`Teste 028`** (Condições Sintáticas para Transposição de Voz Ativa para Voz Passiva Analítica): Preservada.
* **`Teste 029`** (Transposição Rigorosa de Voz Verbal com locução auxiliar ser + particípio): Preservada.
* **`Teste 030`** (Funções da Partícula SE: Pronome Apassivador vs Índice de Indeterminação do Sujeito e reflexividade): Preservada.
* **`Teste 031`** (Verbos Anômalos, Defectivos e Irregulares na redação administrativa): Preservada.

---

## Caderno 04: Sintaxe, Coordenação, Subordinação, Conectivos e Pontuação
* **Arquivo:** `docs/conhecimentos_gerais/01_lingua_portuguesa/04_sintaxe_coordenacao_subordinacao_conectivos_pontuacao.md`
* **Status:** Concluído e sincronizado

### 1. O que ENTRA (Questões Reais de Concurso)
* **`Teste 040`**: Substituído pela questão real **`V3_FGV_TJ_SC_2026_Q0005`**
  * **Banca/Órgão/Ano/Cargo:** **FGV – TJ/SC – 2026 – Analista Administrativo**
  * **Conceito Aderente:** Emprego dos sinais de pontuação na banca FGV: papel sintático-estilístico dos dois-pontos ao introduzir explicações, especificações e enumerações que encadeiam o fluxo reflexivo de ideias do narrador (*Grande Sertão: Veredas* de Guimarães Rosa), além do uso de travessões parentéticos e ponto e vírgula coordenativo.

### 2. O que SAI (Questões Autorais/Simuladas)
* **`Teste 040`**: Simulado sobre o ponto e vírgula e conjunção adversativa deslocada na LRF.

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 032`** (Termos Essenciais e Integrantes da Oração: Sujeito, Objeto Direto, Objeto Indireto e Agente da Passiva): Preservada.
* **`Teste 033`** (Diferenciação Sintática entre Complemento Nominal e Adjunto Adnominal preposicionado): Preservada.
* **`Teste 034`** (Termos Acessórios da Oração: Adjunto Adverbial, Aposto Explicativo e Vocativo): Preservada.
* **`Teste 035`** (Classificação das Orações Coordenadas Sindéticas: Aditivas, Adversativas, Alternativas, Conclusivas e Explicativas): Preservada.
* **`Teste 036`** (Orações Subordinadas Substantivas e Função Sintática da Oração Subjetiva e Objetiva Direta): Preservada.
* **`Teste 037`** (Valores Semânticos das Conjunções Subordinativas Adverbiais: Concessivas como *Conquanto* vs Causais e Condicionais): Preservada.
* **`Teste 038`** (Polissemia Conjuntiva do Conectivo *COMO*: Causa, Comparação e Conformidade): Preservada.
* **`Teste 039`** (Regra de Ouro SVC e Proibição de Vírgula entre Sujeito e Predicado / Verbo e Complemento): Preservada.
* **`Teste 041`** (Distinção Semântica e Pontuação entre Oração Adjetiva Explicativa e Oração Adjetiva Restritiva): Preservada.

---

## Caderno 05: Concordância, Regência e Crase
* **Arquivo:** `docs/conhecimentos_gerais/01_lingua_portuguesa/05_concordancia_regencia_e_crase.md`
* **Status:** Concluído e sincronizado

### 1. O que ENTRA (Questões Reais de Concurso)
* **`Teste 047`**: Substituído pela questão real **`V3_FGV_TJ_MT_2024_Q1849`**
  * **Banca/Órgão/Ano/Cargo:** **FGV – TJ/MT – 2024 – Analista Judiciário**
  * **Conceito Aderente:** Regência verbal, complementos pronominais e crase: estruturação sintática e anáfora dos pronomes oblíquos átonos "la" (objeto direto de conhecer) e "lhe" (objeto indireto de virar as costas) remetendo ao mesmo antecedente (*à verdade*).
* **`Teste 050`**: Substituído pela questão real **`V3_FGV_TCE_SC_2026_Q3107`**
  * **Banca/Órgão/Ano/Cargo:** **FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo**
  * **Conceito Aderente:** Emprego do acento grave indicativo de crase em contexto institucional de controle externo: identificação de caso proibido por duplicidade prepositiva (*"para às novas funções"*, sobreposição indevida da preposição *para* com a contração *às*).

### 2. O que SAI (Questões Autorais/Simuladas)
* **`Teste 047`**: Simulado de lacunas sobre a regência de *referir-se* e *aspirar*.
* **`Teste 050`**: Simulado sobre casos gerais de proibição e obrigatoriedade de crase.

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 042`** (Concordância Verbal com Sujeito Composto anteposto e posposto e núcleos sinônimos): Preservada.
* **`Teste 043`** (Concordância Verbal com Expressões Partitivas e Percentuais seguidas de adjunto no plural): Preservada.
* **`Teste 044`** (Concordância Verbal com a partícula SE: Verbo Transitivo Direto no plural com Sujeito Paciente): Preservada.
* **`Teste 045`** (Concordância Nominal: Adjetivo anteposto e posposto a múltiplos substantivos): Preservada.
* **`Teste 046`** (Regência Verbal do verbo PREFERIR: Vedação a 'do que' e 'mais que', exigência de preposição 'a'): Preservada.
* **`Teste 048`** (Regência de Verbos Notáveis na Administração: Visar, Assistir, Implicar e Proceder): Preservada.
* **`Teste 049`** (Regência Nominal de Substantivos e Adjetivos que exigem preposições a, de, em e por): Preservada.
* **`Teste 051`** (Crase Diante de Nomes Geográficos, Locuções Femininas e Casos Facultativos): Preservada.

---

## Caderno 06: Redação, Reescrita e Equivalência de Estruturas
* **Arquivo:** `docs/conhecimentos_gerais/01_lingua_portuguesa/06_redacao_reescrita_e_equivalencia_de_estruturas.md`
* **Status:** Concluído e sincronizado (100% questões autorais mantidas)

### 1. O que ENTRA (Questões Reais de Concurso)
* *Nenhuma injeção:* Banco vetorial não apresentava itens de reescritura pura com aderência completa; preservadas integralmente as 10 questões originais elaboradas no rigoroso estilo FCC/FGV.

### 2. O que SAI (Questões Autorais/Simuladas)
* *Nenhuma.*

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 052`** (Reescrita com Manutenção do Sentido Original e Correção Gramatical): Preservada.
* **`Teste 053`** (Clareza e Concisão na Redação Oficial: Eliminação de prolixidade e preciosismos): Preservada.
* **`Teste 054`** (Paralelismo Sintático e Semântico em enumerações e orações coordenadas): Preservada.
* **`Teste 055`** (Substituição de Orações Subordinadas Adjetivas por Adjetivos ou Locuções Adjetivas Equivalentes): Preservada.
* **`Teste 056`** (Ambiguidade e Duplo Sentido na Redação de Relatórios de Auditoria): Preservada.
* **`Teste 057`** (Transposição de Oração Reduzida para Oração Desenvolvida com conectivo adequado): Preservada.
* **`Teste 058`** (Troca de Conectivos Coordenativos e Subordinativos com equivalência de valor semântico): Preservada.
* **`Teste 059`** (Economia Linguística e Combate a Pleonasmos Viciosos na gestão pública): Preservada.
* **`Teste 060`** (Reestruturação Sintática de Períodos Longos mantendo a coesão referencial): Preservada.
* **`Teste 061`** (Precisão Vocabular e Adequação Semântica na terminologia técnica do TCE-GO): Preservada.

---

## Caderno 07: Redação Oficial (Manual da Presidência da República 2018)
* **Arquivo:** `docs/conhecimentos_gerais/01_lingua_portuguesa/07_redacao_oficial.md`
* **Status:** Concluído e sincronizado

### 1. O que ENTRA (Questões Reais de Concurso)
* **`Teste 067`**: Substituído pela questão real **`V3_FGV_TCE_SC_2026_Q3173`**
  * **Banca/Órgão/Ano/Cargo:** **FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo**
  * **Conceito Aderente:** Manual de Redação da Presidência da República (3ª edição, 2018): padronização documental e unificação dos expedientes sob o Padrão Ofício, que passou a ser o documento único utilizado tanto para comunicações internas entre unidades do mesmo órgão quanto para comunicações externas com particulares e outros órgãos.
* **`Teste 068`**: Substituído pela questão real **`V3_FGV_TCE_SC_2026_Q3174`**
  * **Banca/Órgão/Ano/Cargo:** **FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo**
  * **Conceito Aderente:** Tramitação e controle de expedientes oficiais segundo o MRPR (2018): procedimentos que asseguram rastreabilidade, registro e controle das comunicações mediante identificação do signatário, número do expediente com o ano e registro claro do campo assunto.

### 2. O que SAI (Questões Autorais/Simuladas)
* **`Teste 067`**: Simulado prévio sobre a extinção de memorando e aviso.
* **`Teste 068`**: Simulado sobre diagramação física do ofício.

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 062`** (Atributos Fundamentais da Redação Oficial: Clareza, Precisão, Concisão, Objetividade, Impessoalidade e Padronização): Preservada.
* **`Teste 063`** (Princípio da Impessoalidade na Redação Oficial: Ausência de impressões individuais e uniformidade da linguagem): Preservada.
* **`Teste 064`** (Diagramação e Padrão Gráfico segundo o MRPR: Margens de 3,0 cm e 1,5 cm e tipografia Calibri/Carlito): Preservada.
* **`Teste 065`** (Pronomes de Tratamento: Emprego de Vossa Excelência para Chefes de Poder e Conselheiros vs Vossa Senhoria): Preservada.
* **`Teste 066`** (Vocativo Oficial em Expedientes: Vossa Excelência exige "Senhor [Cargo]" e fechos padronizados): Preservada.
* **`Teste 069`** (Fechos para Comunicações Oficiais: Bipartição estrita entre Respeitosamente para autoridade superior e Atenciosamente para mesma ou menor hierarquia): Preservada.
* **`Teste 070`** (Correio Eletrônico Institucional / E-mail: Valor documental, segurança da informação e parâmetros do MRPR): Preservada.
* **`Teste 071`** (Espécies Documentais no Controle Externo: Relatório de Auditoria, Instrução Técnica, Parecer Prévio e Acórdão): Preservada.


---

# Módulo 02 (Conhecimentos Gerais): Matemática e Raciocínio Lógico
* **Pasta:** `docs/conhecimentos_gerais/02_matematica_e_raciocinio_logico/`
* **Data da Auditoria e Injeção RAG:** 2026-11-03
* **Cadernos Auditados:** 5 cadernos (`01_conjuntos_numericos_fracoes_e_aritmetica.md` a `05_logica_de_argumentacao_e_conclusoes_validas.md`)
* **Total de Questões no Módulo:** 50 questões (Testes 072 a 121)
* **Decisão Metodológica RAG:** **Preservação Integral de 100% das Questões Autorais Simuladas (50 questões)**
  * **Motivação Técnica da Auditoria:** O banco de dados vetorial externo continha 28 registros rotulados como *Matemática e Raciocínio Lógico*. A inspeção semântica profunda revelou um vício de taxonomia na base importadora de concursos: a grande maioria dos registros tratava de *proposições legislativas* (Direito Constitucional, arts. 59 a 69 da CF/88), processos disciplinares, penalidades na Lei 14.133/2021 ou padrões de redes de dados (IPv6), indexados incorretamente pela palavra "proposição". As questões autorais existentes nos 5 cadernos foram rigorosamente estruturadas sob medida para cobrir 100% da ementa oficial do TCE-GO (Operações com Inteiros e Racionais, MDC/MMC, Razões e Proporções, Divisão Inversamente Proporcional, Regra de Três Simples e Composta, Porcentagem e Fatores de Aumento/Desconto, Lógica Proposicional, Tabelas-Verdade, Leis de De Morgan, Matrizes de Associação, Raciocínio Sequencial e Cíclico, Orientação Espacial e Temporal, e Lógica de Argumentação por Diagramas de Venn e Silogismos). Substituir esses testes por itens com desvio de matéria corromperia a integridade curricular do projeto.

---

## Caderno 01: Aritmética e Conjuntos Numéricos
* **Arquivo:** `docs/conhecimentos_gerais/02_matematica_e_raciocinio_logico/01_conjuntos_numericos_fracoes_e_aritmetica.md`
* **Status:** Concluído e auditado (100% questões autorais mantidas)

### 1. O que ENTRA (Questões Reais de Concurso)
* *Nenhuma injeção:* Banco vetorial sem correspondências conceituais exatas para aritmética e conjuntos numéricos.

### 2. O que SAI (Questões Autorais/Simuladas)
* *Nenhuma.*

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 072`** (Conjuntos Numéricos e Relações de Inclusão entre Naturais, Inteiros, Racionais e Reais): Preservada.
* **`Teste 073`** (Operações com Frações e Expressões Numéricas Fracionárias na divisão de recursos orçamentários): Preservada.
* **`Teste 074`** (Números Primos, Decomposição em Fatores Primos e Critérios de Divisibilidade): Preservada.
* **`Teste 075`** (Mínimo Múltiplo Comum / MMC aplicado a escalas periódicas de plantão e auditorias simultâneas): Preservada.
* **`Teste 076`** (Máximo Divisor Comum / MDC aplicado à divisão equitativa de lotes de processos e arquivos sem sobras): Preservada.
* **`Teste 077`** (Problemas Aritméticos Envolvendo Sistema Métrico Decimal e Conversão de Unidades de Medida): Preservada.
* **`Teste 078`** (Potenciação, Radiciação e Notação Científica no manuseio de grandezas financeiras): Preservada.
* **`Teste 079`** (Dízimas Periódicas Simples e Compostas e Conversão para Fração Geratriz): Preservada.
* **`Teste 080`** (Operações Aritméticas Fundamentais e Resolução de Problemas Algébricos de 1º Grau no setor público): Preservada.
* **`Teste 081`** (Princípio das Gavetas de Dirichlet / Princípio da Casa dos Pombos aplicado à triagem de relatórios): Preservada.

---

## Caderno 02: Grandezas Proporcionais, Regra de Três e Porcentagem
* **Arquivo:** `docs/conhecimentos_gerais/02_matematica_e_raciocinio_logico/02_proporcoes_regra_de_tres_e_porcentagem.md`
* **Status:** Concluído e auditado (100% questões autorais mantidas)

### 1. O que ENTRA (Questões Reais de Concurso)
* *Nenhuma injeção:* Preservadas as formulações matemáticas analíticas desenhadas sob medida para controle externo.

### 2. O que SAI (Questões Autorais/Simuladas)
* *Nenhuma.*

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 082`** (Razão e Proporção entre Grandezas e Propriedade Fundamental das Proporções): Preservada.
* **`Teste 083`** (Divisão em Partes Diretamente Proporcionais na partilha de gratificações por tempo de serviço): Preservada.
* **`Teste 084`** (Divisão em Partes Inversamente Proporcionais segundo o número de faltas e dias de atraso): Preservada.
* **`Teste 085`** (Divisão Proporcional Composta Direta e Inversa Simultânea): Preservada.
* **`Teste 086`** (Regra de Três Simples Direta e Inversa na produtividade de equipes de fiscalização): Preservada.
* **`Teste 087`** (Regra de Três Composta envolvendo operários/auditores, horas diárias, rendimento e extensão da obra): Preservada.
* **`Teste 088`** (Cálculo de Porcentagem Simples, Lucro, Prejuízo e Descontos sobre Valor Nominal): Preservada.
* **`Teste 089`** (Aumentos e Descontos Sucessivos e Cálculo do Fator Multiplicativo Acumulado Real): Preservada.
* **`Teste 090`** (Inversão da Base de Referência Percentual: Comparação entre Processos Físicos e Eletrônicos): Preservada.
* **`Teste 091`** (Variação Percentual Relativa vs Variação em Pontos Percentuais na alteração de alíquotas de tributos): Preservada.

---

## Caderno 03: Estruturas Lógicas, Associação e Dedução
* **Arquivo:** `docs/conhecimentos_gerais/02_matematica_e_raciocinio_logico/03_estruturas_logicas_e_associacao.md`
* **Status:** Concluído e auditado (100% questões autorais mantidas)

### 1. O que ENTRA (Questões Reais de Concurso)
* *Nenhuma injeção:* Banco vetorial continha registros de direito rotulados erroneamente como estruturas lógicas.

### 2. O que SAI (Questões Autorais/Simuladas)
* *Nenhuma.*

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 092`** (Conceito de Proposição Lógica, Princípios da Lógica Clássica e Sentenças Abertas): Preservada.
* **`Teste 093`** (Conectivos Lógicos: Conjunção, Disjunção Inclusiva, Disjunção Exclusiva, Condicional e Bicondicional): Preservada.
* **`Teste 094`** (Construção de Tabelas-Verdade e Determinação do Número de Linhas $2^n$): Preservada.
* **`Teste 095`** (Classificação de Fórmulas Proposicionais: Tautologia, Contradição e Contingência): Preservada.
* **`Teste 096`** (Equivalências Notáveis da Condicional: Contrapositiva $P \to Q \iff \neg Q \to \neg P$ e Equivalência Disjuntiva $\neg P \lor Q$): Preservada.
* **`Teste 097`** (Primeira e Segunda Leis de De Morgan: Negação de Conjunções e Disjunções): Preservada.
* **`Teste 098`** (Negação Lógica da Proposição Condicional: Regra 'Maném e Nega' $P \land \neg Q$): Preservada.
* **`Teste 099`** (Negação da Proposição Bicondicional e sua Equivalência com a Disjunção Exclusiva): Preservada.
* **`Teste 100`** (Problemas de Verdades e Mentiras com Afirmações Contraditórias entre Suspeitos): Preservada.
* **`Teste 101`** (Problemas de Associação Lógica por Matrizes de Eliminação Cruzada: Cargos, Salas e Cidades): Preservada.

---

## Caderno 04: Raciocínio Sequencial, Temporal, Espacial e Verbal
* **Arquivo:** `docs/conhecimentos_gerais/02_matematica_e_raciocinio_logico/04_raciocinio_sequencial_temporal_espacial_e_verbal.md`
* **Status:** Concluído e auditado (100% questões autorais mantidas)

### 1. O que ENTRA (Questões Reais de Concurso)
* *Nenhuma injeção:* Preservadas as 10 questões originais que cobrem perfeitamente os temas de progressões e raciocínio sequencial/temporal da banca.

### 2. O que SAI (Questões Autorais/Simuladas)
* *Nenhuma.*

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 102`** (Sequências Numéricas com Padrões Aritméticos de Segunda Ordem e Diferenças Sucessivas): Preservada.
* **`Teste 103`** (Sequência de Fibonacci e Variações Recursivas em Raciocínio Lógico): Preservada.
* **`Teste 104`** (Sequências Cíclicas e Periódicas: Determinação do n-ésimo termo pelo resto da divisão inteira): Preservada.
* **`Teste 105`** (Sequências Alfanuméricas e Correspondência de Posições no Alfabeto Oficial de 26 Letras): Preservada.
* **`Teste 106`** (Raciocínio Temporal e Problemas de Calendário: Anos Bissextos, Deslocamento de Dias da Semana e Módulos): Preservada.
* **`Teste 107`** (Raciocínio Temporal em Relógios: Ângulos entre Ponteiros de Horas e Minutos): Preservada.
* **`Teste 108`** (Orientação Espacial e Rotação de Figuras Geométricas Bidimensionais e Tridimensionais): Preservada.
* **`Teste 109`** (Planificação de Sólidos Geométricos e Determinação de Faces Opostas em Dados/Cubos): Preservada.
* **`Teste 110`** (Raciocínio Verbal e Analogias Semânticas entre Pares de Palavras): Preservada.
* **`Teste 111`** (Ordenação Linear e Posicional: Fila de Pessoas e Posições Relativas em Plenário): Preservada.

---

## Caderno 05: Lógica de Argumentação e Conclusões Válidas
* **Arquivo:** `docs/conhecimentos_gerais/02_matematica_e_raciocinio_logico/05_logica_de_argumentacao_e_conclusoes_validas.md`
* **Status:** Concluído e auditado (100% questões autorais mantidas)

### 1. O que ENTRA (Questões Reais de Concurso)
* *Nenhuma injeção:* Mantidas as questões didáticas de silogismo, dedução e falácias formais.

### 2. O que SAI (Questões Autorais/Simuladas)
* *Nenhuma.*

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 112`** (Conceito de Argumento Lógico: Premissas, Conclusão e Definição de Validade Formal): Preservada.
* **`Teste 113`** (Regras de Inferência Clássicas: Modus Ponens e Modus Tollens): Preservada.
* **`Teste 114`** (Falácias Formais da Lógica Condicional: Afirmação do Consequente e Negação do Antecedente): Preservada.
* **`Teste 115`** (Quantificadores Lógicos Universal e Existencial: Todo, Algum e Nenhum): Preservada.
* **`Teste 116`** (Negação de Proposições Categóricas com Quantificadores: A negação de 'Todo A é B' é 'Algum A não é B'): Preservada.
* **`Teste 117`** (Análise de Validade de Argumentos Silogísticos por Diagramas de Venn e Regiões de Inclusão): Preservada.
* **`Teste 118`** (Silogismo Categórico e Determinação de Conclusão Necessária a partir de Premissas Particulares e Universais): Preservada.
* **`Teste 119`** (Dedução Lógica a partir de Conjunto Complexo de Hipóteses com Premissas Verdadeiras): Preservada.
* **`Teste 120`** (Falácias Informais Comuns no Debate Público: Ad Hominem, Espantalho, Falsa Dicotomia e Apelo à Autoridade): Preservada.
* **`Teste 121`** (Paradoxos Lógicos Clássicos: Paradoxo do Mentiroso e Autoreferência na Epistemologia da Lógica): Preservada.


---

# Módulo 03 (Conhecimentos Gerais): Legislação Institucional
* **Pasta:** `docs/conhecimentos_gerais/03_legislacao_institucional/`
* **Data da Auditoria e Injeção RAG:** 2026-11-03
* **Cadernos Auditados:** 6 cadernos (`01_bases_constitucionais_cf88_e_ce_go.md` a `06_politicas_institucionais_e_resolucoes_normativas.md`)
* **Total de Questões no Módulo:** 60 questões (Testes 122 a 181)
* **Decisão Metodológica RAG:** **Preservação Integral de 100% das Questões Autorais Simuladas (60 questões)**
  * **Motivação Técnica da Auditoria:** Legislação Institucional versa estritamente sobre o ordenamento normativo específico do Estado de Goiás e do Tribunal de Contas goiano: Constituição Estadual de Goiás (arts. 26 a 33 e 77 a 82), Lei Orgânica do TCE-GO (Lei Estadual nº 16.168/2007), Regimento Interno do TCE-GO (Resolução nº 22/2008), Estatuto dos Servidores Públicos de Goiás (Lei Estadual nº 20.756/2020), Plano de Carreiras do TCE-GO (Lei Estadual nº 15.122/2005), Código de Ética do TCE-GO e Resoluções Normativas da Corte. O banco de dados externo continha 3 registros de concursos passados: 2 deles (FCC 2009) apresentavam enunciados/alternativas corrompidos e truncados no dump original (misturados com fragmentos desconexos), e o terceiro (FGV 2024) apresentava inconsistência doutrinária no gabarito arquivado. Em contrapartida, as 60 questões autorais dos 6 cadernos foram minuciosamente redigidas com fundamentação artigo por artigo da legislação estadual vigente em Goiás, conferindo máxima segurança jurídica e precisão didática aos candidatos aos cargos A01 e B02.

---

## Caderno 01: Bases Constitucionais do Controle Externo (CF/88 e CE/GO)
* **Arquivo:** `docs/conhecimentos_gerais/03_legislacao_institucional/01_bases_constitucionais_cf88_e_ce_go.md`
* **Status:** Concluído e auditado (100% questões autorais mantidas)

### 1. O que ENTRA (Questões Reais de Concurso)
* *Nenhuma injeção:* Preservadas as questões autorais ajustadas à Constituição do Estado de Goiás.

### 2. O que SAI (Questões Autorais/Simuladas)
* *Nenhuma.*

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 122`** (Regime Constitucional de Acumulação de Cargos Públicos: art. 37, XVI e XVII da CF/88 e reflexos no controle externo): Preservada.
* **`Teste 123`** (Estabilidade Constitucional e Processo de Avaliação Especial de Desempenho no Estado de Goiás): Preservada.
* **`Teste 124`** (Competências Constitucionais de Fiscalização Contábil, Financeira e Orçamentária na CE/GO, arts. 77 a 82): Preservada.
* **`Teste 125`** (Julgamento de Contas de Prefeitos vs Parecer Prévio e Tema 157 do STF): Preservada.
* **`Teste 126`** (Autonomia Funcional, Administrativa e Financeira do TCE-GO na Constituição Estadual): Preservada.
* **`Teste 127`** (Composição do Tribunal de Contas de Goiás: 7 Conselheiros, regras de escolha entre Assembleia e Governador): Preservada.
* **`Teste 128`** (Vagas Constitucionais Privativas de Auditores Substitutos e Procuradores de Contas no TCE-GO): Preservada.
* **`Teste 129`** (Garantias e Vedações Constitucionais dos Conselheiros do TCE-GO equiparadas aos Desembargadores do TJ-GO): Preservada.
* **`Teste 130`** (Poder Cautelar dos Tribunais de Contas e Afastamento Provisório de Responsáveis segundo STF e CE/GO): Preservada.
* **`Teste 131`** (Eficácia Executiva das Decisões do TCE-GO e Inscrição em Dívida Ativa Estadual): Preservada.

---

## Caderno 02: Lei Orgânica do TCE-GO (Lei Estadual nº 16.168/2007)
* **Arquivo:** `docs/conhecimentos_gerais/03_legislacao_institucional/02_lei_organica_tce_go_lei_16168_2007.md`
* **Status:** Concluído e auditado (100% questões autorais mantidas)

### 1. O que ENTRA (Questões Reais de Concurso)
* *Nenhuma injeção:* Questão histórica Q0176 apresentava inconsistência de gabarito e alternativas no dump externo; preservadas as questões autorais estritamente ancoradas na Lei nº 16.168/2007.

### 2. O que SAI (Questões Autorais/Simuladas)
* *Nenhuma.*

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 132`** (Jurisdição e Competência Territorial e Funcional do TCE-GO segundo a Lei Orgânica nº 16.168/2007): Preservada.
* **`Teste 133`** (Competência Originária do Plenário vs Competência das Câmaras na Lei Estadual nº 16.168/2007): Preservada.
* **`Teste 134`** (Classificação das Decisões do TCE-GO: Definitivas, Preliminares e Terminativas): Preservada.
* **`Teste 135`** (Natureza do Julgamento de Contas: Contas Regulares, Regulares com Ressalva e Irregulares com Imputação de Débito): Preservada.
* **`Teste 136`** (Sanções e Penalidades Administrativas aplicáveis pelo TCE-GO: Multas e Inabilitação para Função Pública): Preservada.
* **`Teste 137`** (Prazos Prescricionais na Lei Orgânica do TCE-GO e Jurisprudência Vinculante do STF - Tema 899): Preservada.
* **`Teste 138`** (Medidas Cautelares na Lei Orgânica: Requisitos do Fumus Boni Iuris e Periculum in Mora): Preservada.
* **`Teste 139`** (Tomada de Contas Especial / TCE Estadual: Pressupostos de Instauração e Responsabilidade da Autoridade Administrativa): Preservada.
* **`Teste 140`** (Sistema Recursal na Lei Orgânica do TCE-GO: Recursos de Reconsideração, Agravo e Embargos de Declaração): Preservada.
* **`Teste 141`** (Pedido de Rescisão de Julgado do TCE-GO: Prazos, Legitimidade e Hipóteses de Cabimento): Preservada.

---

## Caderno 03: Regimento Interno do TCE-GO (Resolução nº 22/2008)
* **Arquivo:** `docs/conhecimentos_gerais/03_legislacao_institucional/03_regimento_interno_tce_go_resolucao_22_2008.md`
* **Status:** Concluído e auditado (100% questões autorais mantidas)

### 1. O que ENTRA (Questões Reais de Concurso)
* *Nenhuma injeção:* Questões Q0230 e Q0231 do banco vetorial continham alternativas corrompidas no parsing; mantidas as 10 questões íntegras e completas.

### 2. O que SAI (Questões Autorais/Simuladas)
* *Nenhuma.*

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 142`** (Estrutura e Órgãos Deliberativos do TCE-GO: Plenário, Primeira e Segunda Câmaras e suas Competências): Preservada.
* **`Teste 143`** (Presidência e Corregedoria-Geral do TCE-GO: Eleição, Mandato e Atribuições Regimentais): Preservada.
* **`Teste 144`** (Ministério Público junto ao Tribunal de Contas de Goiás / MPC: Estrutura, Atribuições e Atuação Processual): Preservada.
* **`Teste 145`** (Corpo de Auditores Substitutos de Conselheiro / Auditores do art. 73 da CF no Regimento do TCE-GO): Preservada.
* **`Teste 146`** (Sessões Plenárias e de Câmaras: Quórum de Deliberação, Sessões Extraordinárias e Administrativas): Preservada.
* **`Teste 147`** (Distribuição, Relatoria e Sorteio de Processos no TCE-GO): Preservada.
* **`Teste 148`** (Prazos Regimentais e Contagem Processual segundo a Resolução nº 22/2008): Preservada.
* **`Teste 149`** (Incidentes de Uniformização de Jurisprudência e Súmulas Vinculantes do TCE-GO): Preservada.
* **`Teste 150`** (Sustentação Oral e Prerrogativas de Defesa perante o Plenário e as Câmaras): Preservada.
* **`Teste 151`** (Regime Disciplinar Aplicável a Conselheiros e Auditores Substitutos segundo o Regimento Interno): Preservada.

---

## Caderno 04: Regime Jurídico Único dos Servidores e PCCR do TCE-GO (Leis 20.756/2020 e 15.122/2005)
* **Arquivo:** `docs/conhecimentos_gerais/03_legislacao_institucional/04_regime_juridico_servidores_e_pccr_leis_20756_e_15122.md`
* **Status:** Concluído e auditado (100% questões autorais mantidas)

### 1. O que ENTRA (Questões Reais de Concurso)
* *Nenhuma injeção:* Banco vetorial sem questões específicas do Estatuto Goiano (Lei 20.756/2020).

### 2. O que SAI (Questões Autorais/Simuladas)
* *Nenhuma.*

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 152`** (Provimento e Vacância na Lei Estadual nº 20.756/2020: Nomeação, Posse, Exercício e Estágio Probatório em Goiás): Preservada.
* **`Teste 153`** (Formas Derivadas de Provimento no Estatuto de Goiás: Readaptação, Reversão, Reintegração e Recondução): Preservada.
* **`Teste 154`** (Direitos, Vantagens Pecuniárias e Remuneração dos Servidores Públicos Civis de Goiás): Preservada.
* **`Teste 155`** (Regime de Férias e Licenças na Lei nº 20.756/2020: Licença para Tratar de Interesses Particulares e Capacitação): Preservada.
* **`Teste 156`** (Deveres e Proibições do Servidor Público Estadual de Goiás): Preservada.
* **`Teste 157`** (Regime Disciplinar e Penalidades Administrativas na Lei Estadual nº 20.756/2020): Preservada.
* **`Teste 158`** (Processo Administrativo Disciplinar / PAD e Sindicância no Estado de Goiás): Preservada.
* **`Teste 159`** (Plano de Cargos, Carreiras e Vencimentos do TCE-GO - Lei Estadual nº 15.122/2005: Estrutura Funcional): Preservada.
* **`Teste 160`** (Progressão e Promoção Funcional na Carreira de Técnico e Analista de Controle Externo do TCE-GO): Preservada.
* **`Teste 161`** (Adicional de Qualificação e Incentivo à Capacitação dos Servidores do TCE-GO): Preservada.

---

## Caderno 05: Código de Ética e Conduta dos Servidores do TCE-GO
* **Arquivo:** `docs/conhecimentos_gerais/03_legislacao_institucional/05_codigo_de_etica_servidores_tce_go.md`
* **Status:** Concluído e auditado (100% questões autorais mantidas)

### 1. O que ENTRA (Questões Reais de Concurso)
* *Nenhuma injeção:* Preservadas as 10 questões construídas sob medida com base nas normas deontológicas do TCE-GO.

### 2. O que SAI (Questões Autorais/Simuladas)
* *Nenhuma.*

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 162`** (Princípios e Valores Deontológicos Fundamentais do Código de Ética dos Servidores do TCE-GO): Preservada.
* **`Teste 163`** (Conflito de Interesses e Impedimentos Éticos na Realização de Fiscalizações e Auditorias): Preservada.
* **`Teste 164`** (Recebimento de Presentes, Brindes, Vantagens e Hospitalidades por Servidores do Tribunal): Preservada.
* **`Teste 165`** (Uso de Informações Privilegiadas e Dever de Sigilo no Exercício das Funções do Controle Externo): Preservada.
* **`Teste 166`** (Relações Interpessoais, Assédio Moral e Sexual e Respeito à Diversidade no Ambiente do TCE-GO): Preservada.
* **`Teste 167`** (Comissão de Ética do TCE-GO: Composição, Competências e Procedimento Apuratório Ético): Preservada.
* **`Teste 168`** (Sanções Éticas Cabíveis: Censura Ética e Encaminhamento aos Órgãos Disciplinares Competentes): Preservada.
* **`Teste 169`** (Canal de Denúncias e Proteção ao Denunciante de Boa-Fé no Âmbito do TCE-GO): Preservada.
* **`Teste 170`** (Conduta Ética nas Redes Sociais e Manifestações Públicas de Opinião por Servidores de Controle): Preservada.
* **`Teste 171`** (Articulação entre Responsabilidade Ética, Disciplinar, Civil e Penal dos Servidores do Tribunal): Preservada.

---

## Caderno 06: Políticas Institucionais, Gestão e Resoluções Normativas do TCE-GO
* **Arquivo:** `docs/conhecimentos_gerais/03_legislacao_institucional/06_politicas_institucionais_e_resolucoes_normativas.md`
* **Status:** Concluído e auditado (100% questões autorais mantidas)

### 1. O que ENTRA (Questões Reais de Concurso)
* *Nenhuma injeção:* Mantidas as formulações originais orientadas às Resoluções Normativas da Corte de Contas goiana.

### 2. O que SAI (Questões Autorais/Simuladas)
* *Nenhuma.*

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 172`** (Estrutura Organizacional e Competências das Unidades Técnicas e Administrativas do TCE-GO): Preservada.
* **`Teste 173`** (Política de Segurança da Informação / PSI do TCE-GO: Classificação da Informação e Controles de Acesso): Preservada.
* **`Teste 174`** (Gestão de Riscos Corporativos e Controle Interno Institucional no Âmbito do TCE-GO): Preservada.
* **`Teste 175`** (Planejamento Estratégico Institucional e Indicadores de Desempenho do Tribunal de Contas de Goiás): Preservada.
* **`Teste 176`** (Governança de Tecnologia da Informação e Comunicação / TIC no TCE-GO: Alinhamento ao Plano Estratégico): Preservada.
* **`Teste 177`** (Processo Eletrônico de Controle Externo e Certificação Digital no TCE-GO): Preservada.
* **`Teste 178`** (Política de Sustentabilidade e Responsabilidade Socioambiental no Tribunal): Preservada.
* **`Teste 179`** (Ouvidoria do TCE-GO: Canal de Acesso ao Cidadão, Prazos de Resposta e Tratamento de Manifestações): Preservada.
* **`Teste 180`** (Escola Superior de Controle Externo / Escoex do TCE-GO: Capacitação e Aperfeiçoamento Profissional): Preservada.
* **`Teste 181`** (Resoluções Normativas Notáveis sobre Fiscalização de Obras Públicas, Saúde e Educação no TCE-GO): Preservada.


---

# Módulo 16 (Conhecimentos Específicos A01): Licitações e Contratos Administrativos (Lei nº 14.133/2021)
* **Pasta:** `docs/conhecimentos_especificos_a01_tecnico_administrativo/16_licitacoes_e_contratos_administrativos/`
* **Data da Auditoria e Injeção RAG:** 2026-11-03
* **Cadernos Auditados:** 4 cadernos (`01_governanca_planejamento_etp_tr_e_matriz_riscos.md` a `04_contratos_administrativos_fiscalizacao_alteracoes_e_sancoes.md`)
* **Total de Questões no Módulo:** 44 questões (Testes 066 a 109)
* **Questões Reais Injetadas via RAG:** 5 questões (100% aderentes, foco FGV de Tribunais de Contas: TCE-GO 2024, TCE-SC 2026, TCE-PI 2025, TCE-PA 2024)
* **Questões Autorais/Simuladas Preservadas:** 39 questões

---

## Caderno 01: Governança das Contratações, Planejamento, ETP, TR e Matriz de Riscos
* **Arquivo:** `docs/conhecimentos_especificos_a01_tecnico_administrativo/16_licitacoes_e_contratos_administrativos/01_governanca_planejamento_etp_tr_e_matriz_riscos.md`
* **Status:** Concluído e sincronizado (100% questões autorais mantidas)

### 1. O que ENTRA (Questões Reais de Concurso)
* *Nenhuma injeção:* Preservadas as 11 questões originais que cobrem com excelência didática as três linhas de defesa, governança, plano anual de contratações (PCA), estudo técnico preliminar (ETP), termo de referência (TR) e matriz de alocação de riscos da Lei nº 14.133/2021.

### 2. O que SAI (Questões Autorais/Simuladas)
* *Nenhuma.*

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 066`** (Governança das Contratações Públicas e Três Linhas de Defesa no art. 169 da Lei nº 14.133/2021): Preservada.
* **`Teste 067`** (Princípio da Segregação de Funções e Vedações à Designação Cumulativa de Agentes Públicos): Preservada.
* **`Teste 068`** (Gestão por Competências e Requisitos para Designação do Agente de Contratação e Equipe de Apoio): Preservada.
* **`Teste 069`** (Comissão de Contratação: Hipóteses de Obrigatoriedade e Composição Mínima de Três Membros): Preservada.
* **`Teste 070`** (Impedimentos e Suspeições dos Agentes Públicos que Atuam no Processo de Contratação): Preservada.
* **`Teste 071`** (Atuação da Assessoria Jurídica e Defesa Judicial de Agentes de Contratação pelo Órgão de Advocacia Pública): Preservada.
* **`Teste 072`** (Estudo Técnico Preliminar / ETP: Elementos Obrigatórios e Facultativos na Fase Preparatória): Preservada.
* **`Teste 073`** (Termo de Referência / TR e Projeto Básico: Distinções Estruturais e Requisitos Legais): Preservada.
* **`Teste 074`** (Pesquisa de Preços e Métodos de Composição do Preço Estimado segundo o art. 23 da NLLC): Preservada.
* **`Teste 075`** (Matriz de Alocação de Riscos: Riscos Contratuais, Cláusula de Eficiência e Equilíbrio Econômico-Financeiro): Preservada.
* **`Teste 076`** (Plano de Contratações Anual / PCA: Elaboração, Integração ao Orçamento e Publicidade no PNCP): Preservada.

---

## Caderno 02: Fases da Licitação, Modalidades e Critérios de Julgamento
* **Arquivo:** `docs/conhecimentos_especificos_a01_tecnico_administrativo/16_licitacoes_e_contratos_administrativos/02_fases_modalidades_e_criterios_de_julgamento.md`
* **Status:** Concluído e sincronizado

### 1. O que ENTRA (Questões Reais de Concurso)
* **`Teste 079`**: Substituído pela questão real **`V3_FGV_TCE_GO_2024_Q0174`**
  * **Banca/Órgão/Ano/Cargo:** **FGV – TCE/GO – 2024 – Analista de Controle Externo (Controle Externo)**
  * **Conceito Aderente:** Irresignação administrativa e recursos na Lei nº 14.133/2021: sistemática dos recursos e do pedido de reconsideração contra atos decisórios do certame e habilitação/inabilitação de licitantes.
* **`Teste 084`**: Substituído pela questão real **`V3_FGV_TCE_PI_2025_Q2984`**
  * **Banca/Órgão/Ano/Cargo:** **FGV – TCE/PI – 2025 – Auditor de Controle Externo**
  * **Conceito Aderente:** Articulação de instrumentos jurídicos na Lei nº 14.133/2021: emprego do Diálogo Competitivo para soluções complexas e software com inteligência artificial adaptada, Sistema de Registro de Preços (SRP) para notebooks e Credenciamento para técnicos em regime padronizado simultâneo.
* **`Teste 087`**: Substituído pela questão real **`V3_FGV_TCE_SC_2026_Q3127`**
  * **Banca/Órgão/Ano/Cargo:** **FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo (Administração)**
  * **Conceito Aderente:** Consórcio de empresas e habilitação na NLLC (art. 15): acréscimo editalício obrigatório de 10% a 30% na qualificação econômico-financeira de consórcios, dever de constituição e registro prévio do vencedor, e autorização justificada para fixação de limite de empresas consorciadas.

### 2. O que SAI (Questões Autorais/Simuladas)
* **`Teste 079`**: Simulado prévio sobre a fase recursal única da NLLC.
* **`Teste 084`**: Simulado introdutório sobre o conceito básico de diálogo competitivo.
* **`Teste 087`**: Simulado genérico sobre modos de disputa aberto e fechado.

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 077`** (Fases do Processo de Licitação: Inversão de Fases como Regra Geral e Excepcionalidade da Pré-Habilitação): Preservada.
* **`Teste 078`** (Publicidade do Edital e Prazos Mínimos de Apresentação de Propostas nas Modalidades da Lei nº 14.133/2021): Preservada.
* **`Teste 080`** (Modalidade Concorrência: Âmbito de Aplicação para Obras, Bens e Serviços Especiais): Preservada.
* **`Teste 081`** (Modalidade Pregão: Obrigatoriedade para Aquisição de Bens e Serviços Comuns): Preservada.
* **`Teste 082`** (Modalidade Concurso: Seleção de Trabalho Técnico, Científico ou Artístico e Prêmio/Remuneração): Preservada.
* **`Teste 083`** (Modalidade Leilão: Alienação de Bens Móveis Inservíveis e Imóveis sob Condução de Leiloeiro Oficial): Preservada.
* **`Teste 085`** (Critérios de Julgamento: Menor Preço, Maior Desconto, Melhor Técnica ou Conteúdo Artístico, Técnica e Preço, Maior Lance e Maior Retorno Econômico): Preservada.
* **`Teste 086`** (Critério de Maior Retorno Econômico em Contratos de Eficiência Energética e Redução de Custos Operacionais): Preservada.

---

## Caderno 03: Procedimentos Auxiliares e Contratação Direta
* **Arquivo:** `docs/conhecimentos_especificos_a01_tecnico_administrativo/16_licitacoes_e_contratos_administrativos/03_procedimentos_auxiliares_e_contratacao_direta.md`
* **Status:** Concluído e sincronizado (100% questões autorais mantidas)

### 1. O que ENTRA (Questões Reais de Concurso)
* *Nenhuma injeção:* Preservadas as 11 questões originais que cobrem com precisão o credenciamento, pré-qualificação, PMI, registro cadastral, SRP, dispensa (art. 75) e inexigibilidade (art. 74).

### 2. O que SAI (Questões Autorais/Simuladas)
* *Nenhuma.*

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 088`** (Rol Taxativo dos Cinco Procedimentos Auxiliares no art. 78 da Lei nº 14.133/2021): Preservada.
* **`Teste 089`** (Credenciamento: Hipóteses de Paralela e Não Excludente, Mercados com Preços Uniformes e Seleção a Critério de Terceiros): Preservada.
* **`Teste 090`** (Pré-Qualificação Permanente de Licitantes e Bens: Validade e Eficácia Procedimental): Preservada.
* **`Teste 091`** (Procedimento de Manifestação de Interesse / PMI: Proposição de Estudos e Projetos por Particulares sem Direito a Indenização): Preservada.
* **`Teste 092`** (Sistema de Registro de Preços / SRP: Ata de Registro de Preços, Órgão Gerenciador, Participantes e Caronas): Preservada.
* **`Teste 093`** (Processo de Contratação Direta: Requisitos Obrigatórios de Instrução do art. 72 da NLLC): Preservada.
* **`Teste 094`** (Inexigibilidade de Licitação para Serviços Técnicos Profissionais Especializados de Natureza Predominantemente Intelectual): Preservada.
* **`Teste 095`** (Inexigibilidade para Contratação de Profissional do Setor Artístico Consagrado pela Crítica): Preservada.
* **`Teste 096`** (Dispensa de Licitação em Razão do Valor: Limites Monetários dos incisos I e II do art. 75 e Fracionamento Indevido): Preservada.
* **`Teste 097`** (Dispensa de Licitação por Emergência ou Calamidade Pública: Prazo Máximo de 1 Ano e Vedação à Prorrogação): Preservada.
* **`Teste 098`** (Licitação Deserta e Licitação Fracassada: Requisitos Legais para Contratação Direta): Preservada.

---

## Caderno 04: Contratos Administrativos, Fiscalização, Alterações e Sanções
* **Arquivo:** `docs/conhecimentos_especificos_a01_tecnico_administrativo/16_licitacoes_e_contratos_administrativos/04_contratos_administrativos_fiscalizacao_alteracoes_e_sancoes.md`
* **Status:** Concluído e sincronizado

### 1. O que ENTRA (Questões Reais de Concurso)
* **`Teste 107`**: Substituído pela questão real **`V3_FGV_TCE_PA_2024_Q2511`**
  * **Banca/Órgão/Ano/Cargo:** **FGV – TCE/PA – 2024 – Auditor de Controle Externo**
  * **Conceito Aderente:** Processo de responsabilização administrativa na Lei nº 14.133/2021: condução por comissão de servidores estáveis para impedimento de licitar e declaração de inidoneidade, indeferimento motivado de provas ilícitas e prazo legal de 15 dias úteis para defesa.
* **`Teste 108`**: Substituído pela questão real **`V3_FGV_TCE_PA_2024_Q2879`**
  * **Banca/Órgão/Ano/Cargo:** **FGV – TCE/PA – 2024 – Auditor de Controle Externo (Gestão Governamental)**
  * **Conceito Aderente:** Sanção de Declaração de Inidoneidade para licitar ou contratar na Lei nº 14.133/2021: prazo legal mínimo de 3 anos e máximo de 6 anos (art. 156, § 5º), abrangência em âmbito nacional e competência exclusiva de autoridade superior.

### 2. O que SAI (Questões Autorais/Simuladas)
* **`Teste 107`**: Simulado prévio genérico sobre o rol de sanções do art. 156.
* **`Teste 108`**: Simulado sobre caso hipotético de fraude em ambulâncias.

### 3. O que FICA (Questões Autorais Preservadas)
* **`Teste 099`** (Cláusulas Exorbitantes nos Contratos Administrativos: Modificação Unilateral, Rescisão, Fiscalização e Ocupação Provisória - FGV TRF-1): Preservada.
* **`Teste 100`** (Garantias Contratuais na Lei nº 14.133/2021: Caução, Fiança Bancária e Seguro-Garantia com Cláusula de Retomada em Grande Vulto): Preservada.
* **`Teste 101`** (Duração dos Contratos Administrativos: Regra Geral de Até 5 Anos para Serviços Continuados, Prorrogáveis por Até 10 Anos): Preservada.
* **`Teste 102`** (Fiscalização Técnica, Administrativa e Setorial dos Contratos e Conta-Depósito Vinculada): Preservada.
* **`Teste 103`** (Responsabilidade Trabalhista e Previdenciária da Administração: Tema 246 do STF e Vedação à Transferência Automática de Inadimplência): Preservada.
* **`Teste 104`** (Alteração Unilateral dos Contratos Administrativos: Limites Legais de 25% para Acréscimos/Supressões e 50% para Reformas): Preservada.
* **`Teste 105`** (Equilíbrio Econômico-Financeiro: Reajuste em Sentido Estrito, Repactuação e Revisão/Recomposição por Fato Imprevisível): Preservada.
* **`Teste 106`** (Extinção dos Contratos Administrativos: Extinção Unilateral por Inadimplemento, Consensual e Judicial): Preservada.
* **`Teste 109`** (Reabilitação do Licitante ou Contratado Perante a Própria Autoridade que Aplicou a Sanção nos Termos do art. 163): Preservada.


---

# Auditoria e Injeção RAG Consolidada dos 14 Módulos Restantes
* **Data da Execução:** 2026-11-03
* **Escopo:** Conclusão de 100% dos cadernos do projeto TCE-GO 2027 (Trilhas B02 e A01)
* **Status:** 🟢 100% dos Módulos do Projeto Concluídos e Auditados

---

## Módulo 10 (B02 TI): Segurança da Informação
* **Pasta:** `docs/conhecimentos_especificos_b02_ti/10_seguranca_da_informacao/`
* **Cadernos Auditados:** 5 cadernos (Testes 355 a 409)
* **Injeção Real:**
  * **Caderno 02 — `Teste 370`**: Substituído pela questão real **`V3_FGV_TCE_SC_2026_Q3140`** (FGV TCE/SC 2026 Auditor de TI): Processo de geração de assinatura digital sob os padrões da ICP-Brasil (cifração do resumo criptográfico/hash com a chave privada do signatário, garantindo autenticidade, integridade e não repúdio).
* **Questões Autorais Preservadas:** 54 testes mantidos (ISO 27001/27002/27005, Gestão de Riscos, IAM, Zero Trust, OWASP Top 10, DevSecOps, Malware e Defesa em Profundidade).

---

## Módulo 11 (B02 TI): Sistemas Operacionais, Redes e Nuvem
* **Pasta:** `docs/conhecimentos_especificos_b02_ti/11_sistemas_operacionais_redes_e_nuvem/`
* **Cadernos Auditados:** 5 cadernos (Testes 410 a 464)
* **Injeções Reais:**
  * **Caderno 01 — `Teste 414`**: Substituído por **`V3_FGV_TRT_DA_2025_Q1195`** (FGV TRT/DA 2025 TI): Gerenciamento de pacotes RPM no Red Hat Enterprise Linux (`rpm -qa`, instalação e distinção do YUM/DNF na resolução de dependências).
  * **Caderno 03 — `Teste 434`**: Substituído por **`V3_FGV_TRT_DA_2025_Q1202`** (FGV TRT/DA 2025 TI): Arquitetura e endereçamento IP: quantidade de octetos em IPv4 (4 octetos / 32 bits) e IPv6 (16 octetos / 128 bits).
  * **Caderno 05 — `Teste 455`**: Substituído por **`V3_FGV_TCE_SC_2026_Q3279`** (FGV TCE/SC 2026 Auditor de TI): Modelos de computação em nuvem do NIST: migração para Microsoft Office 365 caracterizada como SaaS (Software as a Service).
* **Questões Autorais Preservadas:** 52 testes mantidos (Linux Kernel/CLI, Windows Server, Active Directory/LDAP, DNS/DHCP, protocolos de aplicação e nuvem híbrida/serverless).

---

## Módulo 12 (B02 TI): Governança de TI
* **Pasta:** `docs/conhecimentos_especificos_b02_ti/12_governanca_de_ti/`
* **Cadernos Auditados:** 5 cadernos (Testes 465 a 514)
* **Injeções Reais:**
  * **Caderno 02 — `Teste 478`**: Substituído por **`V3_FGV_TCE_SC_2026_Q3296`** (FGV TCE/SC 2026 Auditor de TI): Framework ITIL 4: Prática de Gerenciamento de Problemas (*Problem Management*) focada na identificação da causa raiz de incidentes repetitivos e mitigação de impactos.
  * **Caderno 04 — `Teste 499`**: Substituído por **`V3_FGV_TCE_SC_2026_Q3274`** (FGV TCE/SC 2026 Auditor de TI): Contratações de TIC e aplicação de sanções sob a Lei nº 14.133/2021 (condução por comissão de servidores estáveis e prazo de 15 dias úteis para defesa).
* **Questões Autorais Preservadas:** 48 testes mantidos (COBIT 2019, ISO 38500, PMBOK 8ª Edição, Métodos Ágeis Scrum/Kanban e Lei de Governo Digital nº 14.129).

---

## Módulo 13 (B02 TI): Legislação Aplicada à TI
* **Pasta:** `docs/conhecimentos_especificos_b02_ti/13_legislacao_aplicada_a_ti/`
* **Cadernos Auditados:** 5 cadernos (Testes 515 a 564)
* **Injeções Reais:**
  * **Caderno 01 — `Teste 516`**: Substituído por **`V3_FGV_TJ_AP_2023_Q0552`** (FGV TJ/AP 2023 TI): Conceito legal de Consentimento no art. 5º, XII da LGPD (manifestação livre, informada e inequívoca).
  * **Caderno 01 — `Teste 518`**: Substituído por **`V3_FGV_TJ_RR_2024_Q1260`** (FGV TJ/RR 2024 TI): Agentes de tratamento na LGPD: o Operador realiza o tratamento em nome e sob as diretrizes do Controlador.
  * **Caderno 01 — `Teste 520`**: Substituído por **`V3_FGV_TJ_RR_2024_Q1262`** (FGV TJ/RR 2024 TI): Instrumentos regulatórios da ANPD: determinação de elaboração do Relatório de Impacto à Proteção de Dados Pessoais (RIPD, art. 38).
* **Questões Autorais Preservadas:** 47 testes mantidos (Marco Civil da Internet, ICP-Brasil na TI, Lei Complementar Estadual nº 205/2025 de Goiás e Resoluções de Governança de TI do TCE-GO).

---

## Módulo 14 (B02 TI): Língua Inglesa (Leitura Técnica)
* **Pasta:** `docs/conhecimentos_especificos_b02_ti/14_lingua_inglesa_leitura_tecnica/`
* **Cadernos Auditados:** 3 cadernos (Testes 565 a 594)
* **Status:** Concluído e auditado (100% questões autorais mantidas com textos originais de documentação técnica, RFCs, manuais de cloud e APIs).

---

## Módulo 17 (A01): Noções de Direito Constitucional
* **Pasta:** `docs/conhecimentos_especificos_a01_tecnico_administrativo/17_nocoes_de_direito_constitucional/`
* **Cadernos Auditados:** 5 cadernos (Testes 110 a 164)
* **Injeção Real:**
  * **Caderno 02 — `Teste 122`**: Substituído por **`V3_FGV_TJ_SC_2026_Q0027`** (FGV TJ/SC 2026): Eficácia e regime dos direitos fundamentais: cláusula de não taxatividade / rol aberto do art. 5º, § 2º da CF/88.
* **Questões Autorais Preservadas:** 54 testes mantidos (Princípios Fundamentais, Organização do Estado, Processo Legislativo, Fiscalização Contábil/TCE e Poder Executivo/Judiciário).

---

## Módulo 18 (A01): Noções de Controle Externo
* **Pasta:** `docs/conhecimentos_especificos_a01_tecnico_administrativo/18_nocoes_de_controle_externo/`
* **Cadernos Auditados:** 4 cadernos (Testes 165 a 208)
* **Injeções Reais:**
  * **Caderno 01 — `Teste 166`**: Substituído por **`V3_FGV_TCE_SC_2026_Q3130`** (FGV TCE/SC 2026 Auditor): Sistema Constitucional de Controle e competência privativa para assinar prazo para exato cumprimento da lei em caso de ilegalidade (art. 71, IX CF/88).
  * **Caderno 03 — `Teste 188`**: Substituído por **`V3_FGV_TCE_SC_2026_Q3147`** (FGV TCE/SC 2026 Auditor): Normas de auditoria do setor público (NBASP/ISSAI): requisitos de suficiência, relevância e confiabilidade das evidências de auditoria.
* **Questões Autorais Preservadas:** 42 testes mantidos (Jurisdição dos TCs, Auditoria Operacional e de Conformidade, Matriz de Achados, Processo de Controle Externo e Sanções).

---

## Módulo 19 (A01): Administração Financeira e Orçamentária (AFO)
* **Pasta:** `docs/conhecimentos_especificos_a01_tecnico_administrativo/19_nocoes_de_administracao_financeira_e_orcamentaria/`
* **Cadernos Auditados:** 5 cadernos (Testes 209 a 259)
* **Injeções Reais:**
  * **Caderno 01 — `Teste 211`**: Substituído por **`V3_FGV_TCE_PI_2025_Q2962`** (FGV TCE/PI 2025 Auditor): Instrumentos do ciclo orçamentário: PPA (art. 165, § 1º), LDO (art. 165, § 2º) e LOA em seus três orçamentos (art. 165, § 5º da CF/88).
  * **Caderno 02 — `Teste 222`**: Substituído por **`V3_FGV_TRT_DA_2025_Q3516`** (FGV TRT/DA 2025): Princípio da universalidade e classificação econômica da receita pública (Receita de Serviços como Corrente vs Amortização de Empréstimos como Capital).
* **Questões Autorais Preservadas:** 49 testes mantidos (Estágios da receita e despesa, restos a pagar, créditos adicionais, LRF e limites com gastos de pessoal).

---

## Módulo 20 (A01): Contabilidade Aplicada ao Setor Público (CASP)
* **Pasta:** `docs/conhecimentos_especificos_a01_tecnico_administrativo/20_contabilidade_aplicada_ao_setor_publico/`
* **Cadernos Auditados:** 4 cadernos (Testes 260 a 299)
* **Injeção Real:**
  * **Caderno 01 — `Teste 262`**: Substituído por **`V3_FGV_TRT_DA_24__REGI_O_2025_Q0901`** (FGV TRT da 24ª Região 2025): NBC TSP Estrutura Conceitual: características qualitativas fundamentais da informação nos RCPGs (relevância, representação fidedigna, compreensibilidade, tempestividade, comparabilidade e verificabilidade).
* **Questões Autorais Preservadas:** 39 testes mantidos (Procedimentos MCASP, estrutura PCASP, subsistemas contábeis, variações patrimoniais e balanços orçamentário, financeiro e patrimonial).

---

## Módulo 21 (A01): Noções de Administração Pública
* **Pasta:** `docs/conhecimentos_especificos_a01_tecnico_administrativo/21_nocoes_de_administracao_publica/`
* **Cadernos Auditados:** 4 cadernos (Testes 300 a 339)
* **Status:** Concluído e auditado (100% das 40 questões autorais mantidas sobre modelos patrimonialista, burocrático e gerencial, governança, Decreto nº 9.094 e indicadores públicos).

---

## Módulo 22 (A01): Administração Geral
* **Pasta:** `docs/conhecimentos_especificos_a01_tecnico_administrativo/22_administracao_geral/`
* **Cadernos Auditados:** 3 cadernos (Testes 340 a 369)
* **Injeção Real:**
  * **Caderno 01 — `Teste 342`**: Substituído por **`V3_FGV_TCE_SC_2026_Q3171`** (FGV TCE/SC 2026 Auditor): Teoria Clássica da Administração: as cinco funções administrativas de Henri Fayol (prever, organizar, comandar, coordenar e controlar).
* **Questões Autorais Preservadas:** 29 testes mantidos (Teoria Científica, Burocracia de Weber, Relações Humanas, Estruturas Organizacionais e Processo Decisório).

---

## Módulo 23 (A01): Administração Estratégica
* **Pasta:** `docs/conhecimentos_especificos_a01_tecnico_administrativo/23_administracao_estrategica/`
* **Cadernos Auditados:** 3 cadernos (Testes 370 a 399)
* **Injeção Real:**
  * **Caderno 01 — `Teste 372`**: Substituído por **`V3_FGV_TRT_DA_2025_Q3510`** (FGV TRT/DA 2025): Níveis hierárquicos de planejamento: amplitude institucional de longo prazo do planejamento estratégico vs foco departamental e médio prazo do planejamento tático.
* **Questões Autorais Preservadas:** 29 testes mantidos (Matriz SWOT, Cinco Forças de Porter, RBV, Balanced Scorecard / BSC e Cadeia de Valor).

---

## Módulo 24 (A01): Comportamento Organizacional
* **Pasta:** `docs/conhecimentos_especificos_a01_tecnico_administrativo/24_comportamento_organizacional/`
* **Cadernos Auditados:** 3 cadernos (Testes 400 a 429)
* **Injeção Real:**
  * **Caderno 02 — `Teste 412`**: Substituído por **`V3_FGV_TJ_SC_2026_Q0031`** (FGV TJ/SC 2026): Estilos clássicos de liderança de White e Lippitt (autocrático, democrático e liberal/laissez-faire).
* **Questões Autorais Preservadas:** 29 testes mantidos (Teorias Motivacionais Maslow/Herzberg/Vroom, Dinâmica de Grupos e Equipes, Cultura e Clima Organizacional e Gestão de Conflitos).

---

## Módulo 25 (A01): Gestão de Pessoas
* **Pasta:** `docs/conhecimentos_especificos_a01_tecnico_administrativo/25_gestao_de_pessoas/`
* **Cadernos Auditados:** 4 cadernos (Testes 430 a 469)
* **Injeções Reais:**
  * **Caderno 01 — `Teste 432`**: Substituído por **`V3_FGV_TJ_SC_2026_Q0044`** (FGV TJ/SC 2026): Processos de atração: vantagens e desvantagens comparativas do recrutamento interno e recrutamento externo.
  * **Caderno 03 — `Teste 452`**: Substituído por **`V3_FGV_TJ_SC_2026_Q0045`** (FGV TJ/SC 2026): Metodologias de avaliação funcional: características da Avaliação de Desempenho 360 Graus com múltiplos avaliadores.
* **Questões Autorais Preservadas:** 38 testes mantidos (Gestão por Competências, Treinamento e Desenvolvimento, Clima e QVT e Estatuto dos Servidores de Goiás - Lei nº 20.756/2020).
