# Plano de Estudos & Fontes Teóricas: Conhecimentos Específicos TI

> **Cargo:** B02 – Técnico de Controle Externo – Especialidade: Tecnologia da Informação  
> **Matéria:** DevOps, Plataforma de Desenvolvimento e Engenharia de Entrega  
> **Banca Referência:** Fundação Carlos Chagas (FCC)  
> **Status Geral:** 🟡 Em mapeamento de fontes teóricas

---

## 📋 Visão Geral da Ementa Oficial

> *"Integração, entrega e implantação contínuas (CI/CD); pipelines de desenvolvimento; automação de build e de testes. Infraestrutura como código e gerenciamento de configuração. Observabilidade e monitoramento de sistemas: métricas, logs e traces; telemetria, instrumentação, correlação de eventos, alertas e acompanhamento de indicadores técnicos de aplicações e infraestrutura. Controle de versão distribuído com Git; plataformas de hospedagem, colaboração e automação baseadas em Git, incluindo GitHub e GitLab; estratégias de branching, incluindo Git Flow e trunk-based development; pull requests/merge requests e revisão de código. Conteinerização: Docker e Docker Compose; orquestração de containers com Kubernetes. Ambientes de desenvolvimento, homologação e produção. Automação de pipelines: GitHub Actions, GitLab CI/CD, Jenkins e ferramentas correlatas."*

---

## 🗂️ Estrutura Hierárquica dos Tópicos

A matéria foi dividida em 6 módulos temáticos modulares que cobrem todo o ciclo de vida moderno de entrega de software:

| # | Módulo / Tópico Principal | Arquivo Markdown | Itens Cobertos do Edital | Status |
|---|---------------------------|------------------|--------------------------|:------:|
| 01 | [CI/CD, Pipelines e Automação de Entrega](./01_cultura_devops_ci_cd_e_automacao_de_pipelines.md) | `01_cultura_devops_ci_cd_e_automacao_de_pipelines.md` | Integração/Entrega Contínua (CI/CD); Pipelines; GitHub Actions, GitLab CI/CD, Jenkins | ⚪ Aguardando Fontes |
| 02 | [Estratégias de Branching e Plataformas Git](./02_git_estrategias_de_branching_e_plataformas_colaborativas.md) | `02_git_estrategias_de_branching_e_plataformas_colaborativas.md` | GitHub e GitLab; Git Flow vs. Trunk-Based; Pull/Merge Requests e governança de código | ⚪ Aguardando Fontes |
| 03 | [Conteinerização com Docker e Docker Compose](./03_conteinerizacao_docker_e_docker_compose.md) | `03_conteinerizacao_docker_e_docker_compose.md` | Docker (imagens, Dockerfile, redes, volumes, multi-stage) e Docker Compose | ⚪ Aguardando Fontes |
| 04 | [Orquestração com Kubernetes e Gestão de Ambientes](./04_orquestracao_com_kubernetes_e_gestao_de_ambientes.md) | `04_orquestracao_com_kubernetes_e_gestao_de_ambientes.md` | Kubernetes (Pods, Deployments, Services, Ingress); Deploys (Blue-Green, Canary); Ambientes | ⚪ Aguardando Fontes |
| 05 | [Infraestrutura como Código (IaC) e Configuração](./05_infraestrutura_como_codigo_iac_e_gerenciamento_de_configuracao.md) | `05_infraestrutura_como_codigo_iac_e_gerenciamento_de_configuracao.md` | IaC declarativa vs. imperativa; Terraform/OpenTofu; Ansible e gerenciamento de configuração | ⚪ Aguardando Fontes |
| 06 | [Observabilidade, Monitoramento e Telemetria](./06_observabilidade_monitoramento_e_telemetria.md) | `06_observabilidade_monitoramento_e_telemetria.md` | Três pilares (Métricas, Logs, Traces); OpenTelemetry, Prometheus, Grafana, ELK; DORA Metrics | ⚪ Aguardando Fontes |

---

## 🎯 Próximos Passos
1. Consolidar manifestos de pipelines reais (exemplos de `.github/workflows` e `.gitlab-ci.yml`).
2. Mapear comandos e manifestos essenciais do Dockerfile e Kubernetes (`kubectl`).
3. Reunir questões recentes da FCC sobre DevOps, Kubernetes e monitoramento de sistemas.

