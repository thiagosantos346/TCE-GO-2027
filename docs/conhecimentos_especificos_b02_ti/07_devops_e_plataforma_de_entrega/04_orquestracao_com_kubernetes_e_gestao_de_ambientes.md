# 04 - Orquestração com Kubernetes e Gestão de Ambientes

> **Matéria:** DevOps, Plataforma de Desenvolvimento e Engenharia de Entrega  
> **Cargo:** B02 – Técnico de Controle Externo – Especialidade: Tecnologia da Informação  
> **Arquivo:** `04_orquestracao_com_kubernetes_e_gestao_de_ambientes.md`  

---

## 📌 Ementa / Itens do Edital

- Orquestração de contêineres com Kubernetes (K8s)
- Arquitetura de clusters Kubernetes (Plano de Controle / Control Plane e Nós de Trabalho / Worker Nodes)
- Objetos fundamentais: Pods, Deployments, ReplicaSets, StatefulSets, DaemonSets, Services e Ingress
- Mecanismos de configuração, persistência e governança: ConfigMaps, Secrets, Namespaces, PV e PVC
- Probes de integridade e ciclo de vida: Liveness, Readiness e Startup Probes
- Estratégias de implantação (Rolling Update, Recreate, Blue-Green, Canary)
- Gestão e segregação de ambientes: Desenvolvimento, Homologação e Produção (Paridade Dev/Prod)

---

## 🧭 Sumário

1. [Arquitetura do Kubernetes: Control Plane vs. Worker Nodes](#1-arquitetura-do-kubernetes-control-plane-vs-worker-nodes)
    1. [Componentes do Plano de Controle (Control Plane)](#11-componentes-do-plano-de-controle-control-plane)
    1. [Componentes dos Nós de Execução (Worker Nodes)](#12-componentes-dos-nós-de-execução-worker-nodes)
    1. [O Loop de Reconciliação Contínua e o Estado Desejado](#13-o-loop-de-reconciliação-contínua-e-o-estado-desejado)
    1. [Teste 203](#teste-203)
    1. [Teste 204](#teste-204)
    1. [Teste 205](#teste-205)
2. [Workloads e Controladores: Qual Objeto Escolher?](#2-workloads-e-controladores-qual-objeto-escolher)
    1. [Pods: A Menor Unidade Implantável](#21-pods-a-menor-unidade-implantável)
    1. [Deployment e ReplicaSet: Gerenciamento Declarativo para Aplicações Stateless](#22-deployment-e-replicaset-gerenciamento-declarativo-para-aplicações-stateless)
    1. [StatefulSet: Identidade Estável e Volumes para Cargas Stateful](#23-statefulset-identidade-estável-e-volumes-para-cargas-stateful)
    1. [DaemonSet: Instância Única por Nó de Infraestrutura](#24-daemonset-instância-única-por-nó-de-infraestrutura)
    1. [Job e CronJob: Tarefas em Lote e Rotinas Agendadas](#25-job-e-cronjob-tarefas-em-lote-e-rotinas-agendadas)
    1. [Teste 206](#teste-206)
    1. [Teste 207](#teste-207)
    1. [Teste 208](#teste-208)
3. [Serviços de Rede (Services) e Roteamento de Borda (Ingress)](#3-serviços-de-rede-services-e-roteamento-de-borda-ingress)
    1. [Tipos de Services: ClusterIP, NodePort, LoadBalancer e ExternalName](#31-tipos-de-services-clusterip-nodeport-loadbalancer-e-externalname)
    1. [O Objeto Ingress e Controladores de Roteamento de Camada 7](#32-o-objeto-ingress-e-controladores-de-roteamento-de-camada-7)
    1. [Teste 209](#teste-209)
    1. [Teste 210](#teste-210)
4. [Ciclo de Vida, Resiliência e Probes de Integridade](#4-ciclo-de-vida-resiliência-e-probes-de-integridade)
    1. [Liveness Probe vs. Readiness Probe vs. Startup Probe](#41-liveness-probe-vs-readiness-probe-vs-startup-probe)
    1. [Tabela Comparativa de Comportamento em Caso de Falha](#42-tabela-comparativa-de-comportamento-em-caso-de-falha)
    1. [Teste 211](#teste-211)
5. [Governança, Armazenamento e Segregação de Ambientes](#5-governança-armazenamento-e-segregação-de-ambientes)
    1. [ConfigMaps e Secrets: Injeção Desacoplada de Configurações](#51-configmaps-e-secrets-injeção-desacoplada-de-configurações)
    1. [Persistência: PersistentVolume (PV), PersistentVolumeClaim (PVC) e StorageClass](#52-persistência-persistentvolume-pv-persistentvolumeclaim-pvc-e-storageclass)
    1. [Segregação de Ambientes e Paridade Dev/Prod (Twelve-Factor App)](#53-segregação-de-ambientes-e-paridade-devprod-twelve-factor-app)
    1. [Teste 212](#teste-212)
    1. [Teste 213](#teste-213)
6. [Fontes Oficiais e Referências Bibliográficas](#-fontes-oficiais-e-referências-bibliográficas)

---

## 1. Arquitetura do Kubernetes: Control Plane vs. Worker Nodes

O Kubernetes (K8s) é a plataforma líder da indústria para orquestração declarativa de contêineres em ambientes distribuídos e elásticos. Concebido a partir da experiência do Google com seus sistemas internos (Borg e Omega) e posteriormente doado à *Cloud Native Computing Foundation* (CNCF), o Kubernetes opera sob o paradigma do **estado desejado (*declarative reconciliation*)**: o operador define as metas do cluster em manifestos YAML e a plataforma atua ininterruptamente para assegurar que o **estado real** coincida com o **estado declarado**.

```mermaid
flowchart TD
    subgraph Control_Plane["Plano de Controle (Control Plane / Master)"]
        API["kube-apiserver<br/>(Ponto de entrada REST, porta 6443)"]
        ETCD[("etcd<br/>(Banco Chave-Valor Distribuído / Raft)")]
        SCHED["kube-scheduler<br/>(Agendador de Nós)"]
        CTRL["kube-controller-manager<br/>(Loops de Reconciliação)"]
  
        API <--> ETCD
        API <--> SCHED
        API <--> CTRL
    end

    subgraph Worker_Node_1["Nó de Trabalho 1 (Worker)"]
        KUBELET1["kubelet (Agente do Nó)"]
        KPROXY1["kube-proxy (Regras de Rede)"]
        RUNTIME1["Container Runtime (containerd)"]
        POD1["Pod A (Contêineres)"]
  
        KUBELET1 <--> RUNTIME1
        RUNTIME1 --- POD1
    end

    subgraph Worker_Node_2["Nó de Trabalho 2 (Worker)"]
        KUBELET2["kubelet (Agente do Nó)"]
        KPROXY2["kube-proxy (Regras de Rede)"]
        RUNTIME2["Container Runtime (containerd)"]
        POD2["Pod B (Contêineres)"]
  
        KUBELET2 <--> RUNTIME2
        RUNTIME2 --- POD2
    end

    API <===>|Comunicação Segura TLS| KUBELET1
    API <===>|Comunicação Segura TLS| KUBELET2
    API <===>|Atualização de Serviços| KPROXY1
    API <===>|Atualização de Serviços| KPROXY2
```

### 1.1 Componentes do Plano de Controle (Control Plane)

O Plano de Controle é responsável por tomar decisões globais sobre o cluster (como agendamento de recursos), detectar e responder a eventos (como inicializar um novo Pod quando as réplicas de um Deployment não são atendidas):

1. **`kube-apiserver`:** É o coração e a porta de entrada de todo o cluster. Expõe a API REST do Kubernetes em HTTPS (porta padrão 6443). Todos os clientes externos (como a CLI `kubectl` ou esteiras de CI/CD) e todos os nós internos comunicam-se **exclusivamente com ele**. É o único componente autorizado a realizar operações diretas de leitura e gravação no banco de dados distribuído `etcd`.
2. **`etcd`:** Armazena o estado completo de configuração, segredos, metadados e objetos do cluster. Trata-se de um banco de dados relacional distribuído chave-valor altamente consistente que utiliza o algoritmo de consenso Raft. Fazer backup regular do `etcd` equivale a garantir a recuperação completa de desastres (*Disaster Recovery*) de todo o cluster K8s.
3. **`kube-scheduler`:** Responsável por analisar Pods recém-criados que ainda não possuem um nó atribuído e selecionar o nó de trabalho ideal para executá-los. Considera restrições de hardware (CPU e RAM solicitadas), regras de afinidade e anti-afinidade (*nodeAffinity*, *podAntiAffinity*), tolerâncias a manchas (*taints & tolerations*) e disponibilidade de portas.
4. **`kube-controller-manager`:** Executa os controladores internos em processos de segundo plano. Cada controlador é um loop contínuo de reconciliação que compara o estado real observado via API Server com o estado desejado (ex.: *Node Controller* para nós que falham, *Deployment Controller* para substituição de versões, *EndpointSlice Controller* para roteamento de rede).
5. **`cloud-controller-manager`:** Módulo opcional que integra a lógica do Kubernetes com as APIs dos provedores de nuvem pública (AWS, Azure, Google Cloud), provisionando dinamicamente balanceadores de carga, rotas e discos gerenciados.

### 1.2 Componentes dos Nós de Execução (Worker Nodes)

Os Nós de Trabalho (*Worker Nodes*) são os servidores físicos ou máquinas virtuais encarregados de executar as cargas de trabalho reais da organização:

1. **`kubelet`:** O agente de gerenciamento instalado em cada nó do cluster. Ele consome as especificações do Pod (*PodSpecs*) enviadas pelo `kube-apiserver` e interage com o runtime local de contêineres via *Container Runtime Interface* (CRI) para garantir que os contêineres descritos sejam criados, permaneçam em execução e estejam saudáveis. Ele também supervisiona o resultado das *probes* de integridade e reporta o status do nó ao Control Plane.
2. **`kube-proxy`:** Componente de rede distribuído executado em cada nó de trabalho. Mantém as regras de rede (usando tabelas `iptables` ou módulos `IPVS` do Linux), viabilizando a abstração de *Service* e implementando o balanceamento de conexões TCP/UDP entre as réplicas ativas dos Pods.
3. **Container Runtime:** O software responsável pela execução física dos contêineres (como `containerd` ou `CRI-O`). Opera em conformidade com os padrões da OCI (*Open Container Initiative*).

> ⭐ **IMPORTANTE / REGRA DE OURO:**  
> Nenhum componente do cluster comunica-se diretamente com o `etcd`, com exceção do **`kube-apiserver`**. O `kube-scheduler`, o `controller-manager` e os agentes `kubelet` consultam e atualizam o estado do cluster **sempre e obrigatoriamente através do `kube-apiserver`**.

### 1.3 O Loop de Reconciliação Contínua e o Estado Desejado

O ciclo de vida do Kubernetes baseia-se em um mecanismo ininterrupto:
$$\text{Observar Estado Real} \longrightarrow \text{Comparar com Estado Desejado} \longrightarrow \text{Executar Ação Corretiva}$$
Se um desenvolvedor define `replicas: 4` em um manifesto e um nó físico desliga subitamente (derrubando 2 Pods), o *Controller Manager* detecta que o estado real caiu para 2 réplicas e comanda o *kube-scheduler* a despachar 2 novos Pods em nós sadios remanescentes, restaurando a capacidade desejada sem qualquer intervenção humana (*Self-Healing*).

---

### Teste 203

**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
A arquitetura do Kubernetes é dividida entre o Plano de Controle (*Control Plane*) e os Nós de Execução (*Worker Nodes*). O componente central do *Control Plane* que atua como o único banco de dados de armazenamento consistente e altamente disponível, guardando todo o estado do cluster, suas configurações e especificações de objetos no modelo chave-valor, é o:

- **A)** `kube-scheduler`
- **B)** `etcd`
- **C)** `kube-apiserver`
- **D)** `kubelet`
- **E)** `kube-proxy`

---

> **Comentário Detalhado:**
>
> - **A) Incorreta.** O `kube-scheduler` analisa os nós e decide em qual nó cada Pod deve ser executado.
> - **B) Correta.** O **`etcd`** é um banco de dados distribuído de chave-valor consistente e de alta disponibilidade (baseado no algoritmo de consenso Raft) que armazena todos os dados do cluster Kubernetes como a fonte única da verdade.
> - **C) Incorreta.** O `kube-apiserver` é a porta de entrada da API que se comunica com o etcd.
> - **D) Incorreta.** O `kubelet` é o agente que executa nos nós de trabalho (*Worker Nodes*).
> - **E) Incorreta.** O `kube-proxy` gerencia as regras de rede nos nós de trabalho.
>
> **Gabarito: B**

---

### Teste 204

**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**
Durante o planejamento de alta disponibilidade para a infraestrutura de computação em nuvem de um Tribunal de Contas, a equipe de operações analisou a distribuição de responsabilidades entre os componentes do Plano de Controle (*Control Plane*) e dos Nós de Execução (*Worker Nodes*) do Kubernetes.

A respeito das funções e interações entre esses componentes, assinale a afirmativa correta:  

- **A)** O `etcd` atua como servidor de proxy reverso e balanceador de carga HTTP para receber diretamente as requisições dos usuários da internet.
- **B)** O `kube-scheduler` é o único componente autorizado a realizar operações de gravação e leitura no banco de dados distribuído `etcd`.
- **C)** O `kubelet` é o agente executado em cada nó de trabalho (*Worker Node*) responsável por receber as especificações dos Pods (*PodSpecs*) a partir do `kube-apiserver` e assegurar que os contêineres descritos estejam em execução e saudáveis no nó.
- **D)** O `kube-controller-manager` tem como responsabilidade exclusiva alocar endereços IP públicos nas placas de rede físicas dos servidores blade da instituição.
- **E)** O `kube-proxy` roda unicamente no nó Master e impede que contêineres dentro do mesmo Pod consigam se comunicar via `localhost`.

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O `etcd` é o banco de dados chave-valor distribuído que preserva o estado completo e as configurações do cluster K8s, operando em rede privada e sem qualquer exposição para o tráfego de usuários finais da internet.
> - **B)** Incorreta. O **único** componente do cluster que possui autorização e capacidade de interagir diretamente com o banco de dados `etcd` é o **`kube-apiserver`**. Todos os outros componentes (incluindo o scheduler e os controllers) comunicam-se via API Server.
> - **C)** Correta. O **`kubelet`** é o agente primário de cada nó de trabalho (*Worker Node*). Ele estabelece comunicação contínua com o `kube-apiserver`, recebe as especificações dos Pods (*PodSpecs*), comanda o runtime de contêineres via CRI para instanciar as cargas de trabalho e supervisiona a saúde das instâncias através das sondas (*probes*).
> - **D)** Incorreta. O `kube-controller-manager` executa múltiplos loops de reconciliação contínua (como Node Controller e Deployment Controller) para manter o estado desejado do cluster, não gerenciando alocação física de IPs em blades.
> - **E)** Incorreta. O `kube-proxy` opera em cada nó de trabalho gerenciando regras de rede de serviços, e contêineres do mesmo Pod comunicam-se nativamente via `localhost`.
>
> **Gabarito: C**

---

### Teste 205

**(FGV – TJ/RR – 2024 – Analista Judiciário - Infraestrutura de TI)**  
No Kubernetes, há duas formas de aplicar mudanças na configuração de uma aplicação: imperativa e declarativa. Considere os dois comandos a seguir:

1: `kubectl create -f exemplo.yaml`  
2: `kubectl apply -f exemplo-deployment.yaml`  

Nesse caso, é correto afirmar que:

- **A)** 1 é um exemplo de comando declarativo, em que o kubectl especifica a operação que se deseja aplicar.
- **B)** 2 é um exemplo de comando imperativo, em que o kubectl especifica a operação que se deseja aplicar.
- **C)** 2 é um exemplo de comando imperativo, em que o usuário não define que operações serão executadas.
- **D)** 1 é um exemplo de comando declarativo, em que o sistema do Kubernetes decidirá a melhor forma de aplicá-lo.
- **E)** 2 é um exemplo de comando declarativo, em que o sistema do Kubernetes decidirá a melhor forma de aplicá-lo.

---

> **Comentário Detalhado:**
>
> - **A, B, C e D) Incorretas.** O comando `kubectl create` é imperativo (instrui o cluster a criar o recurso explicitamente; falha se o recurso já existir). Já o comando `kubectl apply` é a abordagem declarativa padrão da gerência de configuração no Kubernetes: opera sobre o arquivo de configuração e reconcilia o estado do cluster com base na especificação declarada, cabendo ao Kubernetes determinar as operações necessárias para convergir o estado atual ao estado desejado.
> - **E) Correta.** O comando 2 (`kubectl apply`) exemplifica o gerenciamento declarativo de objetos. O usuário fornece o manifesto com o estado final pretendido e o Kubernetes infere as alterações necessárias (criação, patch ou atualização de campos) para alcançar esse estado.
>
> **Gabarito: E**

---

> **Comentário Detalhado:**
>
> - **A) Incorreta.** O processo é 100% autônomo e contínuo.
> - **B) Correta.** É o cerne da automação do Kubernetes: o usuário declara o estado desejado (ex: "desejo 5 réplicas do Pod X"). O controlador monitora a realidade: se um nó cai e sobram apenas 4 pods, o controlador detecta a discrepância e dispara a criação de um novo Pod imediatamente para restabelecer as 5 réplicas (*self-healing* declarativo).
> - **C) Incorreta.** Kubernetes provê resiliência e alta disponibilidade.
> - **D) Incorreta.** Comportamento inexistente.
> - **E) Incorreta.** Afirmação absurda.
>
> **Gabarito: B**

---

## 2. Workloads e Controladores: Qual Objeto Escolher?

O Kubernetes não executa contêineres diretamente de forma isolada; ele os encapsula em abstrações funcionais denominadas *Workloads*.

```mermaid
flowchart TD
    subgraph Deployment_Hierarchy["Hierarquia do Deployment"]
        DEP["Deployment (Gerencia versões e Rollouts)"]
        RS1["ReplicaSet (Versão Atual V1 - 3 réplicas)"]
        RS2["ReplicaSet (Versão Nova V2 - 0 réplicas)"]
        P1["Pod 1"]
        P2["Pod 2"]
        P3["Pod 3"]
  
        DEP --> RS1
        DEP -.-> RS2
        RS1 --> P1
        RS1 --> P2
        RS1 --> P3
    end
```

### 2.1 Pods: A Menor Unidade Implantável

O **Pod** é a menor e mais básica unidade gerenciável do modelo de objetos do Kubernetes:

- Um Pod encapsula **um ou mais contêineres estreitamente acoplados** que compartilham recursos de baixo nível:
    1. **Network Namespace Compartilhado:** Todos os contêineres do mesmo Pod compartilham o mesmo endereço IP e a mesma tabela de portas. Eles podem se comunicar internamente via `localhost` com altíssima performance.
    2. **Volumes Compartilhados:** Podem montar os mesmos diretórios de dados locais.

- **Padrão Sidecar:** Um contêiner primário executa a lógica de negócio (ex.: API Node.js), enquanto contêineres secundários (*sidecars*) realizam tarefas de apoio (ex.: agente Envoy de Service Mesh ou agente de envio de logs).
- **Efemeridade Crítica:** Pods são descartáveis e mortais. Eles nunca devem ser instanciados de forma avulsa em produção; devem ser sempre gerenciados por controladores de carga de trabalho.

### 2.2 Deployment e ReplicaSet: Gerenciamento Declarativo para Aplicações Stateless

- **`ReplicaSet`:** Controlador encarregado de manter um número fixo e estável de réplicas de Pods rodando a qualquer momento, utilizando seletores de rótulos (*Labels and Selectors*).
- **`Deployment`:** Abstração de nível superior que gerencia os `ReplicaSets` de forma declarativa:
  - Permite realizar atualizações sem tempo de inatividade (*RollingUpdate*);
  - Controla o ritmo de rollout através das diretivas `maxSurge` (quantos Pods extras podem ser criados acima da meta) e `maxUnavailable` (quantos Pods podem ficar indisponíveis durante a transição);
  - Possibilita pausar, retomar e reverter versões instantaneamente (`kubectl rollout undo deployment/<nome>`).
  - **Uso ideal:** Aplicações web sem estado (*stateless*), microsserviços REST, APIs de processamento assíncrono.

### 2.3 StatefulSet: Identidade Estável e Volumes para Cargas Stateful

Projetado para aplicações que demandam persistência de dados e ordenação estrita:

- **Identidade de Rede Estável:** Cada Pod recebe um nome ordinal determinístico que persiste mesmo se o Pod for recriado (ex.: `postgres-0`, `postgres-1`, `postgres-2`).
- **Volumes Dedicados via `volumeClaimTemplates`:** Cada réplica recebe seu próprio disco persistente individual; se o `postgres-1` morrer e renascer em outro nó, o Kubernetes reanexa exatamente o mesmo disco à nova réplica.
- **Inicialização e Parada Ordenada:** Pods sobem sequencialmente (0, depois 1, depois 2) e são encerrados na ordem inversa (2, depois 1, depois 0).
- **Uso ideal:** Bancos de dados distribuídos (PostgreSQL com replicação, MongoDB, Cassandra), sistemas de mensageria (Apache Kafka, RabbitMQ).

### 2.4 DaemonSet: Instância Única por Nó de Infraestrutura

- Garante que **exatamente uma cópia de um determinado Pod seja executada em todos os nós de trabalho** do cluster.
- Se novos nós forem adicionados ao cluster (por autoscaling de infraestrutura), o *DaemonSet* automaticamente agenda uma réplica do Pod no nó recém-adicionado. Se um nó for removido, o Pod é destruído.
- **Uso ideal:** Daemons de infraestrutura, coletores de logs (Fluentd, Logstash), agentes de monitoramento de métricas (Prometheus Node Exporter) e plugins de rede CNI (Calico, Flannel).

### 2.5 Job e CronJob: Tarefas em Lote e Rotinas Agendadas

- **`Job`:** Cria um ou mais Pods e assegura que eles executem até o término bem-sucedido (código de saída zero). Ao concluir a tarefa, o Pod é encerrado e não é reiniciado pelo kubelet. Indicado para migrações de schema de banco de dados e relatórios pontuais.
- **`CronJob`:** Gerencia a execução periódica de `Jobs` com base em uma tabela temporal padrão (sintaxe cron de 5 campos, ex.: `0 2 * * *` para rodar diariamente às 02h). Indicado para rotinas de backup noturno e limpezas de cache.

---

### Teste 206

**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
Para implantar e gerenciar aplicações sem estado (*stateless*) em clusters Kubernetes, o controlador de carga de trabalho recomendado como padrão na arquitetura é o **Deployment**. A relação estrutural entre um objeto *Deployment* e os objetos *ReplicaSets* e *Pods* sob sua gestão estabelece que:

- **A)** O Deployment gerencia diretamente contêineres individuais sem a existência de Pods.
- **B)** O Deployment gerencia versões de ReplicaSets (criando novos ReplicaSets durante atualizações de versão e mantendo os antigos para viabilizar *rollbacks* rápidos), e os ReplicaSets garantem a quantidade declarada de réplicas ativas dos Pods em execução.
- **C)** O ReplicaSet comanda o Deployment em uma hierarquia invertida.
- **D)** Cada Deployment só pode conter um único Pod no cluster inteiro.
- **E)** O Deployment exige que a aplicação utilize armazenamento físico em disquetes de alta densidade. em conformidade com as diretrizes e padrões de arquitetura corporativa.

---

> **Comentário Detalhado:**
>
> - **A) Incorreta.** A menor unidade gerenciável no Kubernetes é o Pod, nunca contêineres soltos.
> - **B) Correta.** A hierarquia canônica de workloads *stateless*: **Deployment $\rightarrow$ ReplicaSet $\rightarrow$ Pods**. Ao atualizar a imagem de um Deployment, ele cria um novo ReplicaSet e migra as réplicas progressivamente (*RollingUpdate*), permitindo voltar à versão anterior (*rollback*) instantaneamente apenas reativando o ReplicaSet anterior.
> - **C) Incorreta.** O Deployment situa-se acima do ReplicaSet.
> - **D) Incorreta.** Suporta dezenas ou centenas de réplicas escaladas horizontalmente.
> - **E) Incorreta.** Afirmação absurda.
>
> **Gabarito: B**

---

### Teste 207

**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**
Uma equipe de desenvolvimento da Secretaria da Fazenda precisa implantar três soluções distintas no cluster Kubernetes institucional:

1. Uma API de consulta tributária sem estado (*stateless*), que deve permitir atualizações de versão sem parada de serviço (*rolling updates*) e escalabilidade horizontal automática.
2. Um cluster de banco de dados distribuído que exige armazenamento persistente com discos dedicados e nomes de rede fixos e ordenados para cada réplica.
3. Um agente de segurança e coleta de logs que deve ser executado obrigatoriamente com exatamente uma cópia em cada nó de trabalho do cluster.

Os objetos e controladores do Kubernetes mais indicados para atender aos cenários 1, 2 e 3 são, respectivamente:  

- **A)** `Deployment`; `StatefulSet`; e `DaemonSet`.
- **B)** `StatefulSet`; `Deployment`; e `CronJob`.
- **C)** `Job`; `ReplicaSet`; e `ConfigMap`.
- **D)** `DaemonSet`; `Job`; e `StatefulSet`.
- **E)** `Deployment`; `CronJob`; e `Ingress`.

---

> **Comentário Detalhado:**
>
> - **A)** Correta. As três opções correspondem perfeitamente às definições da arquitetura K8s:
>   - Cenário 1: Aplicações sem estado (*stateless*) com atualização sem parada (*RollingUpdate*) e escalabilidade horizontal são gerenciadas canonicamente por **`Deployments`**.
>   - Cenário 2: Bancos de dados e sistemas com estado (*stateful*) que exigem discos persistentes dedicados e nomes estáveis com ordenação determinística (`pod-0`, `pod-1`) exigem o uso de **`StatefulSets`**.
>   - Cenário 3: Agentes de coleta de logs, telemetria e segurança que precisam rodar com exatamente uma cópia em cada nó do cluster são orquestrados por **`DaemonSets`**.
> - **B)** Incorreta. O StatefulSet é para o cenário 2 e o CronJob é para tarefas periódicas.
> - **C)** Incorreta. Job é para tarefas pontuais de lote e ConfigMap é para injeção de configurações.
> - **D)** Incorreta. A ordem dos controladores está incorreta para os cenários descritos.
> - **E)** Incorreta. O Ingress é um recurso de rede/borda de Camada 7, não um controlador de execução de agentes em nós.
>
> **Gabarito: A**

---

### Teste 208

**(FGV – TJ/DFT – 2022 – Analista Judiciário - Suporte em TI)**  
A analista Ana precisa implantar o pod `LogPod` no cluster de Kubernetes `KCluster` do TJDFT de forma que todos os nós elegíveis do `KCluster` executem uma cópia do `LogPod`.

Para que o `KCluster` apresente uma cópia do `LogPod` em cada nó elegível, de forma automática, Ana deve implantar o `LogPod` utilizando o recurso do Kubernetes:

- **A)** ReplicationController;
- **B)** ReplicaSet;
- **C)** StatefulSet;
- **D)** DaemonSet;
- **E)** EndpointSlice.

---

> **Comentário Detalhado:**
>
> - **A e B) Incorretas.** `ReplicationController` e `ReplicaSet` gerenciam uma quantidade determinada de réplicas e as distribuem pelo cluster conforme os algoritmos de escalonamento do scheduler, sem garantir que haja uma réplica em cada nó físico/trabalhador.
> - **C) Incorreta.** O `StatefulSet` gerencia aplicações com estado que exigem identidade de rede e volumes persistentes exclusivos e ordenados.
> - **D) Correta.** O **`DaemonSet`** assegura que todos (ou um subconjunto selecionado de) nós executem uma cópia de um Pod. Conforme novos nós são adicionados ao cluster, Pods são criados automaticamente neles. Esse é o padrão arquitetural ideal para coletores de logs (ex: Fluentd, Logstash), agentes de monitoramento e plugins de storage/rede.
> - **E) Incorreta.** `EndpointSlice` é um recurso de rede para agrupar endpoints de rede do Kubernetes de forma escalável.
>
> **Gabarito: D**

---

> **Comentário Detalhado:**
>
> - **A) Incorreta.** *Job* executa tarefas em lote que finalizam após a conclusão com sucesso.
> - **B) Incorreta.** *StatefulSet* gerencia cargas com estado e identificadores ordinais fixos.
> - **C) Correta.** O **`DaemonSet`** garante que todos (ou alguns nós específicos) executem exatamente uma réplica do Pod. Quando novos nós entram no cluster, o DaemonSet aloca o Pod neles automaticamente; se um nó é removido, o Pod é destruído (padrão ideal para agentes de log, métricas e storage da infraestrutura).
> - **D) Incorreta.** *ReplicaSet* distribui réplicas arbitrariamente pelo cluster conforme capacidade.
> - **E) Incorreta.** *CronJob* executa Jobs periodicamente com base em agendamentos cron.
>
> **Gabarito: C**

---

## 3. Serviços de Rede (Services) e Roteamento de Borda (Ingress)

Como os Pods são efêmeros e seus IPs são dinâmicos e voláteis, sistemas corporativos exigem pontos de acesso estáveis para comunicação.

```mermaid
flowchart LR
    subgraph Internet_Traffic["Tráfego Externo"]
        USER["Clientes Externos"] --> ING["Ingress Controller (Nginx / HAProxy)<br/>Roteia por Host/Path e Termina TLS"]
    end
  
    subgraph K8s_Services["Serviços Kubernetes"]
        ING -->|"portal.fazenda.gov.br"| SVC_WEB["Service Web (ClusterIP)"]
        ING -->|"api.fazenda.gov.br/tributos"| SVC_API["Service API (ClusterIP)"]
  
        SVC_WEB --> P1["Pod Web 1"]
        SVC_WEB --> P2["Pod Web 2"]
        SVC_API --> P3["Pod API 1"]
        SVC_API --> P4["Pod API 2"]
    end
```

### 3.1 Tipos de Services: ClusterIP, NodePort, LoadBalancer e ExternalName

O objeto **`Service`** provê um endereço IP virtual fixo (*VIP*) e um registro DNS imutável para um conjunto de Pods selecionados via *labels*:

1. **`ClusterIP` (Padrão):**
    - Cria um IP virtual acessível **estritamente de dentro do cluster**.
    - É o padrão ouro para comunicação interna entre microsserviços (comunicação leste-oeste).

2. **`NodePort`:**
    - Abre uma porta estática de alto nível (por padrão entre as faixas **30000 e 32767**) em todas as interfaces de rede de **todos os nós do cluster**.
    - Qualquer cliente que enviar tráfego para `<IP_Qualquer_No>:<NodePort>` é balanceado e direcionado aos Pods do serviço.

3. **`LoadBalancer`:**
    - Estende o tipo `NodePort` ao solicitar automaticamente a criação de um balanceador de carga externo gerenciado no provedor de nuvem pública (AWS NLB, Azure Load Balancer).
    - O balanceador da nuvem recebe o tráfego externo e o despacha para os nós do Kubernetes.

4. **`ExternalName`:**
    - Não utiliza seletores nem endereços IP virtuais; atua como um redirecionamento interno de DNS mapeando o serviço para um nome externo (registro CNAME), como `database.orgao.gov.br`.

### 3.2 O Objeto Ingress e Controladores de Roteamento de Camada 7

Enquanto criar múltiplos serviços do tipo `LoadBalancer` gera custos financeiros elevados e aloca dezenas de IPs públicos, o **`Ingress`** atua como um roteador de borda consolidado na Camada 7 (HTTP/HTTPS):

- **Funcionalidades:** Roteamento baseado em nomes de domínio (*Virtual Hosting* baseado em SNI, ex.: `portal.tce.go.gov.br` vs `auditoria.tce.go.gov.br`), roteamento baseado em caminhos de URL (ex.: `/api/v1/auth` vs `/api/v1/certidoes`) e **terminação centralizada de criptografia TLS/SSL**.
- **Ingress Controller:** O objeto `Ingress` é apenas um manifesto declarativo de regras. Ele exige a presença de um **Ingress Controller** ativo no cluster (como NGINX Ingress Controller, Traefik, HAProxy ou Kong) para interceptar o tráfego e aplicar o roteamento.

---

### Teste 209

**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
Os objetos do tipo *Service* no Kubernetes fornecem abstração de rede estável e balanceamento de carga para conjuntos dinâmicos de Pods. O tipo de *Service* padrão, que atribui um endereço IP virtual interno alcançável exclusivamente dentro dos limites do cluster, denomina-se:

- **A)** `NodePort`
- **B)** `ClusterIP`
- **C)** `LoadBalancer`
- **D)** `ExternalName`
- **E)** `IngressController`

---

> **Comentário Detalhado:**
>
> - **A) Incorreta.** `NodePort` expõe o serviço em uma porta estática (faixa 30000-32767) em cada nó do cluster para acesso externo.
> - **B) Correta.** O **`ClusterIP`** é o tipo padrão (*default*): aloca um IP virtual estável roteável apenas internamente na rede do cluster, perfeito para comunicação interna entre microsserviços (ex: backend acessando o banco de dados).
> - **C) Incorreta.** `LoadBalancer` provisiona um balanceador de carga público externo gerenciado pelo provedor de nuvem (GCP, AWS, Azure).
> - **D) Incorreta.** `ExternalName` mapeia o Service para um registro CNAME DNS externo.
> - **E) Incorreta.** Ingress Controller é um controlador de roteamento de borda (L7), não um tipo de Service.
>
> **Gabarito: B**

---

### Teste 210

**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**
No Kubernetes, o mecanismo de abstração que permite agrupar um conjunto de Pods sob um mesmo endereço IP estável e balancear o tráfego de rede entre eles, bem como o componente responsável por receber tráfego HTTP/HTTPS externo e roteá-lo com base no nome do domínio e no caminho da URL para múltiplos serviços internos, são denominados, respectivamente:  

- **A)** `ConfigMap` e `kubelet`.
- **B)** `Service` e `Ingress`.
- **C)** `Namespace` e `etcd`.
- **D)** `PersistentVolumeClaim` e `kube-proxy`.
- **E)** `DaemonSet` e `ReplicaSet`.

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. `ConfigMap` provê injeção de parâmetros em texto claro e o `kubelet` gerencia contêineres nos nós.
> - **B)** Correta. O **`Service`** atua como uma abstração lógica que fornece um endereço IP estável e balanceia conexões entre réplicas de Pods selecionadas por labels. Já o **`Ingress`** opera na Camada 7 (HTTP/HTTPS), gerenciando o tráfego de borda externo, viabilizando roteamento por nomes de host (domínios virtuais), caminhos de requisição e terminação segura de certificados TLS/SSL.
> - **C)** Incorreta. `Namespace` é partição lógica interna e `etcd` é o armazenamento distribuído do cluster.
> - **D)** Incorreta. `PersistentVolumeClaim` lida com alocação de armazenamento em disco persistente.
> - **E)** Incorreta. Trata-se de controladores de cargas de trabalho, e não de componentes de rede e roteamento de borda.
>
> **Gabarito: B**

---

## 4. Ciclo de Vida, Resiliência e Probes de Integridade

O agente `kubelet` utiliza três sondas de monitoramento (*probes*) para acompanhar a integridade física e funcional dos contêineres:

```mermaid
flowchart TD
    START["Contêiner Iniciado"] --> S_PROBE{"Startup Probe configurada?"}
    S_PROBE -->|Sim| RUN_SP["Executa Startup Probe"]
    RUN_SP -->|Falhou| RESTART_SP["kubelet reinicia o contêiner"]
    RUN_SP -->|Sucesso| PASS_SP["Startup concluído com sucesso"]
    S_PROBE -->|Não| PASS_SP
  
    PASS_SP --> LOOP["Inicia loops paralelos: Liveness e Readiness"]
  
    LOOP --> RUN_LP["Liveness Probe periódica"]
    RUN_LP -->|Falhou| KILL_LP["Aplicação travada: kubelet REINICIA o contêiner"]
    RUN_LP -->|Sucesso| OK_LP["Mantém execução"]
  
    LOOP --> RUN_RP["Readiness Probe periódica"]
    RUN_RP -->|Falhou| UNREADY_RP["Sobrecarga/Indisponível: REMOVE Pod dos Endpoints do Service (Sem tráfego)"]
    RUN_RP -->|Sucesso| READY_RP["Adiciona Pod aos Endpoints (Recebe tráfego normal)"]
```

### 4.1 Liveness Probe vs. Readiness Probe vs. Startup Probe

1. **`livenessProbe` (Sonda de Sobrevivência):**
    - **Objetivo:** Detectar se a aplicação interna entrou em estado de falha fatal irrecuperável (ex.: *deadlock* de threads, vazamento catastrófico de memória ou loop infinito).
    - **Consequência da Falha:** O `kubelet` **encerra o contêiner imediatamente e o reinicia** de acordo com a política de reinício (*restartPolicy*).

2. **`readinessProbe` (Sonda de Prontidão):**
    - **Objetivo:** Detectar se a aplicação está **pronta para receber tráfego de rede** dos clientes.
    - **Consequência da Falha:** O contêiner **NÃO é reiniciado**! O Kubernetes apenas **remove temporariamente o endereço IP do Pod da lista de Endpoints do Service**, impedindo que requisições de usuários sejam enviadas a um Pod que está ocupado ou aquecendo caches.

3. **`startupProbe` (Sonda de Inicialização):**
    - **Objetivo:** Proteger aplicações legadas que demoram vários minutos para inicializar (ex.: monólitos corporativos em Java/Spring).
    - **Mecanismo:** Desativa as verificações de Liveness e Readiness até que a aplicação complete seu boot inicial, prevenindo que o kubelet mate prematuramente um contêiner que apenas estava inicializando seus módulos internos.

### 4.2 Tabela Comparativa de Comportamento em Caso de Falha

| Tipo de Sonda | Propósito Essencial | Ação do Kubernetes em Caso de Falha Contínua | Impacto no Tráfego de Rede |
| :--- | :--- | :--- | :--- |
| **`livenessProbe`** | Verificar se a aplicação está viva e operante. | **REINICIA o contêiner** (emite `SIGTERM` e `SIGKILL`). | O Pod fica temporariamente indisponível até o reinício. |
| **`readinessProbe`** | Verificar se a aplicação pode atender requisições agora. | **NÃO reinicia o contêiner**. | **Remove o Pod dos Endpoints do Service** (zero tráfego). |
| **`startupProbe`** | Proteger o tempo de boot inicial de sistemas lentos. | **REINICIA o contêiner** somente se o tempo limite de boot expirar. | O Pod não recebe tráfego até passar na sonda. |

> 🚨 **ALERTA DE PROVA / PEGADINHA FCC:**  
> A pegadinha clássica da FCC em questões sobre probes é inverter as consequências de falha:
>
> - Afirmar que a falha da **readinessProbe** causa a destruição ou reinicialização do contêiner (**FALSO!** A readiness apenas remove o Pod do balanceador do Service).
> - O reinício compulsório ocorre na falha contínua da **livenessProbe**!

---

### Teste 211

**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - TI)**  
O Tribunal está migrando seus serviços de auditoria contínua para um cluster Kubernetes (K8s). Durante um teste de carga, um Auditor de TI observa que, embora o Horizontal Pod Autoscaler (HPA) esteja criando novas réplicas dos Pods, o tempo de resposta continua alto porque o tráfego não está sendo distribuído eficientemente entre as novas instâncias.

Para garantir que o tráfego seja enviado apenas para Pods que já completaram sua rotina de inicialização e carregamento de cache, a seguinte configuração do Kubernetes deve ser rigorosamente auditada e ajustada:

- **A)** Liveness Probe.
- **B)** Resource Quotas.
- **C)** Readiness Probe.
- **D)** ConfigMaps.
- **E)** Node Selector.

---

> **Comentário Detalhado:**
>
> - **A) Incorreta.** A `Liveness Probe` verifica se o contêiner está vivo e em execução operacional saudável. Se ela falhar repetidamente, o `kubelet` reinicia o contêiner. Ela não serve primariamente para aguardar o aquecimento inicial ou segurar o tráfego de rede.
> - **B) Incorreta.** `Resource Quotas` estabelecem limites globais de consumo de CPU/Memória/Objetos por namespace.
> - **C) Correta.** A **`Readiness Probe`** indica se o contêiner está pronto para receber requisições de rede. Se a sonda de prontidão falhar, o Pod não é reiniciado, mas seu endereço IP é imediatamente removido dos Endpoints dos Services correspondentes, garantindo que o tráfego só seja roteado para Pods com inicialização e cache concluídos.
> - **D) Incorreta.** `ConfigMaps` desacoplam configurações do código de aplicação.
> - **E) Incorreta.** `Node Selector` restringe em quais nós de infraestrutura um Pod pode ser agendado.
>
> **Gabarito: C**

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O mecanismo de resiliência (*self-healing*) do Kubernetes não permite que o kubelet ignore falhas contínuas de sondas de sobrevivência.
> - **B)** Incorreta. Probes em contêineres individuais não acionam compras ou provisionamento financeiro de recursos em nuvem pública.
> - **C)** Correta. A finalidade precípua da **`livenessProbe`** é identificar se a aplicação travou irrecuperavelmente. Caso a sonda falhe pelo limite consecutivo configurado (*failureThreshold*), o agente `kubelet` encerra o contêiner (sinal `SIGTERM`/`SIGKILL`) e **reinicia-o compulsoriamente** com base na política de reinício do Pod (*restartPolicy*), restaurando o serviço.
> - **D)** Incorreta. A ação de apenas remover o Pod da lista de Endpoints do Service sem reiniciar o contêiner é a consequência exclusiva da falha na **`readinessProbe`**, e não na `livenessProbe`.
> - **E)** Incorreta. Ação absurda e destrutiva sem qualquer fundamento técnico.
>
> **Gabarito: C**

---

## 5. Governança, Armazenamento e Segregação de Ambientes

### 5.1 ConfigMaps e Secrets: Injeção Desacoplada de Configurações

Em cumprimento ao Fator III da metodologia *Twelve-Factor App* (*Store config in the environment*), parâmetros de configuração e credenciais nunca devem estar fixados (*hardcoded*) dentro do código-fonte ou da imagem Docker:

- **`ConfigMap`:** Armazena dados de configuração não sensíveis em texto claro (variáveis de ambiente, URLs de serviços externos, arquivos de configuração completos como `nginx.conf`). Podem ser injetados no contêiner como variáveis de ambiente ou montados como arquivos em volumes virtuais.
- **`Secret`:** Armazena dados estritamente sensíveis (senhas de banco de dados, chaves privadas SSH, tokens JWT, certificados digitais TLS). Por padrão no Kubernetes vanilla, os dados são armazenados no `etcd` e codificados em Base64 (exigindo a habilitação de criptografia em repouso no `etcd` para segurança corporativa plena).

### 5.2 Persistência: PersistentVolume (PV), PersistentVolumeClaim (PVC) e StorageClass

O Kubernetes implementa um padrão desacoplado entre administradores de infraestrutura e desenvolvedores para gerenciar armazenamento de dados:

```mermaid
flowchart LR
    ADMIN["Administrador / Cloud Provider"] -->|Provisiona storage físico| PV["PersistentVolume (PV)"]
    DEV["Desenvolvedor"] -->|Solicita 100Gi ReadWriteOnce| PVC["PersistentVolumeClaim (PVC)"]
    PVC -.->|Vinculação Automática (Binding)| PV
    POD["Pod (StatefulSet / Deployment)"] -->|Consome o storage| PVC
```

- **`PersistentVolume` (PV):** O recurso de armazenamento real provisionado no cluster (disco SAN, volume AWS EBS, export NFS). Representa a oferta de capacidade física.
- **`PersistentVolumeClaim` (PVC):** A solicitação formal de armazenamento feita por um desenvolvedor (especificando tamanho em gigabytes e modo de acesso, como `ReadWriteOnce` ou `ReadWriteMany`). O Kubernetes vincula automaticamente o PVC a um PV compatível.
- **`StorageClass`:** Permite o provisionamento dinâmico de volumes. Quando um PVC referencia uma StorageClass, o Kubernetes aciona a API do provedor de infraestrutura para criar o disco físico sob demanda, dispensando o provisionamento manual prévio de PVs.

### 5.3 Segregação de Ambientes e Paridade Dev/Prod (Twelve-Factor App)

A gestão profissional de múltiplos ambientes (Desenvolvimento, Homologação/Staging e Produção) exige conformidade com as boas práticas de governança:

1. **Paridade entre Ambientes (Fator X do Twelve-Factor App):** As ferramentas, bibliotecas e sistemas de retaguarda (bancos de dados, mensageria) devem ser estritamente idênticos em todos os estágios. Não se deve utilizar SQLite em desenvolvimento e PostgreSQL em produção; utilize o mesmo PostgreSQL conteinerizado em todos os ambientes.
2. **Modelos de Isolamento Multi-Ambiente:**
    - **Soft Multi-Tenancy (Namespaces Compartilhados no mesmo Cluster):** Ambientes separados logicamente por `Namespaces` dentro de um único cluster. Exige o uso obrigatório de **`ResourceQuota`** (para limitar o teto de CPU e RAM de desenvolvimento e evitar que testes sobrecarreguem a produção), **`LimitRange`** e **`NetworkPolicies`** (regras de firewall interno impedindo comunicação entre namespaces).
    - **Hard Multi-Tenancy (Clusters Físicos Dedicados):** Padrão recomendado para órgãos do setor público como o TCE-GO. Mantêm-se clusters fisicamente isolados para Produção e Não-Produção, eliminando qualquer risco de contaminação cruzada, vazamento de dados fiscais ou exaustão de plano de controle.

---

### Teste 212

**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
Em conformidade com a metodologia dos Doze Fatores (*Twelve-Factor App*), a configuração de uma aplicação deve ser estritamente separada do código-fonte. No Kubernetes, essa segregação é implementada por meio de dois objetos nativos: *ConfigMaps* e *Secrets*. A diferença fundamental de propósito entre eles estabelece que:

- **A)** *ConfigMaps* armazenam dados confidenciais criptografados, enquanto *Secrets* guardam arquivos de imagem públicos sem restrição.
- **B)** *ConfigMaps* destinam-se a dados de configuração não confidenciais em texto claro (como URLs de endpoints, portas e flags de log), ao passo que *Secrets* são concebidos para armazenar dados confidenciais e credenciais sensíveis (como senhas, chaves de API, tokens e certificados TLS), codificados em Base64 ou protegidos por criptografia em repouso no `etcd`.
- **C)** *Secrets* não podem ser montados como variáveis de ambiente nos Pods.
- **D)** Ambos os objetos são deletados obrigatoriamente a cada 5 minutos pelo Kubernetes.
- **E)** *ConfigMaps* só aceitam configurações escritas em linguagem Pascal.

---

> **Comentário Detalhado:**
>
> - **A) Incorreta.** Relação de confidencialidade invertida.
> - **B) Correta.** Definição arquitetural exata: **ConfigMaps** para configurações gerais legíveis; **Secrets** para credenciais sensíveis que demandam controle de acesso via RBAC, auditoria de acesso e encriptação no etcd. Ambos podem ser injetados em Pods como variáveis de ambiente ou montados como arquivos em volumes.
> - **C) Incorreta.** Secrets podem ser injetados perfeitamente como variáveis de ambiente via `secretKeyRef` ou `envFrom`.
> - **D) Incorreta.** São objetos persistentes estáveis.
> - **E) Incorreta.** Dados são armazenados como pares chave-valor universais.
>
> **Gabarito: B**

---

### Teste 213

**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**
Em um órgão público, os ambientes de Desenvolvimento, Homologação e Produção compartilham a infraestrutura de computação. Para garantir a governança e o isolamento operacional desses ambientes de acordo com as boas práticas do Kubernetes e da metodologia dos Doze Fatores (*Twelve-Factor App*), a equipe técnica deve:  

- **A)** Utilizar `Namespaces` distintos combinados com `ResourceQuotas` para impor limites máximos de consumo de CPU e memória em cada ambiente, associando segredos e credenciais via objetos `Secret` e configurações não sensíveis via `ConfigMap`.
- **B)** Gravar senhas de bancos de dados diretamente em texto claro dentro do código-fonte da aplicação para evitar o overhead de processamento do K8s.
- **C)** Conceder permissões de administrador de cluster (*cluster-admin*) irrestritas a todos os estagiários nos ambientes de homologação e produção.
- **D)** Utilizar a estratégia de deploy *Recreate* em produção durante o horário de pico de atendimento ao cidadão para forçar o desligamento dos servidores.
- **E)** Armazenar os dados transacionais de bancos de dados exclusivamente na camada efêmera do Pod, proibindo o uso de `PersistentVolumes` (PV) e `PersistentVolumeClaims` (PVC).

---

> **Comentário Detalhado:**
>
> - **A)** Correta. O particionamento lógico em **`Namespaces`** associado a cotas estritas de recursos (**`ResourceQuota`**) impede que o ambiente de desenvolvimento monopolize os recursos de CPU e memória do cluster. Além disso, a segregação de configurações em **`ConfigMaps`** e credenciais confidenciais em **`Secrets`** materializa o Fator III (*Config*) do Twelve-Factor App, garantindo que a mesma imagem de contêiner imutável seja promovida entre os ambientes sem risco de exposição de dados.
> - **B)** Incorreta. Manter senhas no código-fonte viola os mais fundamentais princípios de segurança da informação e governança.
> - **C)** Incorreta. Distribuir privilégios irrestritos de *cluster-admin* contraria abertamente o Princípio do Menor Privilégio (*PoLP*) e as normas de controle de acesso RBAC.
> - **D)** Incorreta. A estratégia de publicação *Recreate* causa indisponibilidade forçada (*downtime*) e não deve ser utilizada em horários de pico operacional de produção.
> - **E)** Incorreta. Armazenar dados em camadas efêmeras provocaria perda catastrófica e definitiva de informações a cada reinicialização de Pods de banco de dados.
>
> **Gabarito: A**

---

## 🌐 Fontes Oficiais e Referências Bibliográficas

- [Kubernetes Official Documentation - Componentes da Arquitetura](https://kubernetes.io/pt-br/docs/concepts/overview/components/) - Control Plane (API Server, etcd, Scheduler, Controller Manager) e Node (kubelet, kube-proxy, runtime).
- [Kubernetes Official Documentation - Workloads e Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) - Gestão declarativa de Pods, ReplicaSets, Rolling Updates e Rollbacks.
- [Kubernetes Official Documentation - Services e Ingress](https://kubernetes.io/pt-br/docs/concepts/services-networking/service/) - Comunicação de rede (ClusterIP, NodePort, LoadBalancer) e roteamento HTTP/HTTPS via Ingress.
- [Kubernetes Official Documentation - Configure Liveness, Readiness and Startup Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/) - Monitoramento de integridade e prontidão operacional dos contêineres.
- [Kubernetes Official Documentation - Persistent Volumes](https://kubernetes.io/pt-br/docs/concepts/storage/persistent-volumes/) - Gestão de armazenamento persistente com PV, PVC e StorageClass.
- BURNS, Brendan; BEDA, Joe; HIGHTOWER, Kelsey. **Kubernetes: Up and Running: Dive into the Future of Infrastructure**. 3. ed. Sebastopol: O'Reilly Media, 2022. (Cap. 4 - Pods; Cap. 5 - Services; Cap. 9 - Deployments).
- SAYFAN, Gigi. **Mastering Kubernetes**. 4. ed. Birmingham: Packt Publishing, 2022. (Cap. 2 - Arquitetura de Alto Nível; Cap. 6 - Rede e Armazenamento).
- LUKSA, Marko. **Kubernetes em Ação**. Rio de Janeiro: Alta Books, 2019. (Cap. 6 e 7 - Volumes, ConfigMaps e Secrets).
