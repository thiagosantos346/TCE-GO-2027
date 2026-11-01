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
    2. [Componentes dos Nós de Execução (Worker Nodes)](#12-componentes-dos-nos-de-execucao-worker-nodes)
    3. [O Loop de Reconciliação Contínua e o Estado Desejado](#13-o-loop-de-reconciliacao-continua-e-o-estado-desejado)
    4. [Teste 203](#Teste-203)
    5. [Teste 204](#Teste-204)
    6. [Teste 205](#Teste-205)
2. [Workloads e Controladores: Qual Objeto Escolher?](#2-workloads-e-controladores-qual-objeto-escolher)
    1. [Pods: A Menor Unidade Implantável](#21-pods-a-menor-unidade-implantavel)
    2. [Deployment e ReplicaSet: Gerenciamento Declarativo para Aplicações Stateless](#22-deployment-e-replicaset-gerenciamento-declarativo-para-aplicacoes-stateless)
    3. [StatefulSet: Identidade Estável e Volumes para Cargas Stateful](#23-statefulset-identidade-estavel-e-volumes-para-cargas-stateful)
    4. [DaemonSet: Instância Única por Nó de Infraestrutura](#24-daemonset-instancia-unica-por-no-de-infraestrutura)
    5. [Job e CronJob: Tarefas em Lote e Rotinas Agendadas](#25-job-e-cronjob-tarefas-em-lote-e-rotinas-agendadas)
    6. [Teste 206](#Teste-206)
    7. [Teste 207](#Teste-207)
    8. [Teste 208](#Teste-208)
3. [Serviços de Rede (Services) e Roteamento de Borda (Ingress)](#3-servicos-de-rede-services-e-roteamento-de-borda-ingress)
    1. [Tipos de Services: ClusterIP, NodePort, LoadBalancer e ExternalName](#31-tipos-de-services-clusterip-nodeport-loadbalancer-e-externalname)
    2. [O Objeto Ingress e Controladores de Roteamento de Camada 7](#32-o-objeto-ingress-e-controladores-de-roteamento-de-camada-7)
    3. [Teste 209](#Teste-209)
    4. [Teste 210](#Teste-210)
4. [Ciclo de Vida, Resiliência e Probes de Integridade](#4-ciclo-de-vida-resiliencia-e-probes-de-integridade)
    1. [Liveness Probe vs. Readiness Probe vs. Startup Probe](#41-liveness-probe-vs-readiness-probe-vs-startup-probe)
    2. [Tabela Comparativa de Comportamento em Caso de Falha](#42-tabela-comparativa-de-comportamento-em-caso-de-falha)
    3. [Teste 211](#Teste-211)
5. [Governança, Armazenamento e Segregação de Ambientes](#5-governanca-armazenamento-e-segregacao-de-ambientes)
    1. [ConfigMaps e Secrets: Injeção Desacoplada de Configurações](#51-configmaps-e-secrets-injecao-desacoplada-de-configuracoes)
    2. [Persistência: PersistentVolume (PV), PersistentVolumeClaim (PVC) e StorageClass](#52-persistencia-persistentvolume-pv-persistentvolumeclaim-pvc-e-storageclass)
    3. [Segregação de Ambientes e Paridade Dev/Prod (Twelve-Factor App)](#53-segregacao-de-ambientes-e-paridade-devprod-twelve-factor-app)
    4. [Teste 212](#Teste-212)
    5. [Teste 213](#Teste-213)
6. [🌐 Fontes Oficiais e Referências Bibliográficas](#fontes-oficiais-e-referencias-bibliograficas)

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
**(FCC – TRT-15 – Analista Judiciário - Tecnologia da Informação – 2015)**
A partir do caminho $JBOSS_HOME/bin, considere: 

 I. ./standalone.sh --server-config=standalone-ha.xml  
 II. ./startserver.sh --domain-config=default.xml  
 III. ./domain.sh --domain-config=domain-osgi-only.xml  
 IV. ./jbserver.sh --config=defaul-ha.xml 

 As instruções que podem ser utilizadas para iniciar o JBoss Application Server 7 com configurações alternativas em um arquivo 
de configuração são as que constam APENAS em

* **A)** I e II.
* **B)** III e IV.
* **C)** II e IV.
* **D)** I e III.
* **E)** II e III. 
Caderno de Prova ’B02’, Tipo 001

10 TRT15-An.Jud.-Téc. Informação-B02

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **B)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **C)** Correta. Representa com precisão a disciplina do tema e o entendimento pacificado adotado pela banca (FCC).
> - **D)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **E)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
>
> **Gabarito: C**

---
### Teste 204
**(FGV – TRT-13 – Analista Judiciário - Tecnologia da Informação – 2022)**
A infraestrutura recomendada para instalar o Rancher em um 
cluster Kubernetes K3 de alta disponibilidade é

* **A)** dois nós Linux, normalmente máquina virtual,  e um banco de 
dados externo do tipo NoSQL.
* **B)** um cluster com Linux com menos dois nós ou quatro nós se 
Windows Server normalmente máquinas virtuais;  com pelos 
menos 64 GB de memória RAM no provedor de infraestrutura 
e um banco de dados externo do tipo NoSQL.
* **C)** um cluster com Linux de dois nós normalmente máquinas 
virtuais; com pelos menos 48 GB de memória RAM no 
provedor de infraestrutura.
* **D)** dois nós Linux, normalmente máquinas virtuais; um banco de 
dados externo do tipo relacional, um balanceador de carga e 
um registro DNS.
* **E)** quatro nós Windows Server, normalmente máquinas virtuais; 
um banco de dados externo do tipo relacional, um 
balanceador de carga entre os  quatro nós e dois registros 
DNS como redundância.

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **B)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **C)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **D)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **E)** Correta. Representa com precisão a disciplina do tema e o entendimento pacificado adotado pela banca (FGV).
>
> **Gabarito: E**

---
### Teste 205
**(FCC – TRT-11 – Analista Judiciário - Tecnologia da Informação – 2017)**
Considere a imagem abaixo, que mostra uma arquitetura de armazenamento baseada em informações. 



 Nessa arquitetura, as lacunas I e II são preenchidas, correta e respectivamente, com

* **A)** NFS/CIFS e NAS.
* **B)** LAN/WAN e SAN.
* **C)** MAN/WAN e NAS.
* **D)** LAN/SAN e VPN.
* **E)** VPN/NAS e SAN. 
Caderno de Prova ’K11’, Tipo 005

12 TRT11-An.Jud.-Tec.Informação-K11

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **B)** Correta. Representa com precisão a disciplina do tema e o entendimento pacificado adotado pela banca (FCC).
> - **C)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **D)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **E)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
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
**(FCC – TRT-11 – Analista Judiciário - Tecnologia da Informação – 2017)**
A arquitetura de portais corporativos construídos usando a tecnologia Java EE se baseia em três componentes fundamentais:
o portal, o portlet e o portlet container.  O container da Apache que fornece a implementação de referência do Java Portlet 
Specification é chamado de

* **A)** Maia.
* **B)** Jetty.
* **C)** Pluto.
* **D)** Gerônimo.
* **E)** Inca. 
Caderno de Prova ’K11’, Tipo 005

10 TRT11-An.Jud.-Tec.Informação-K11

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **B)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **C)** Correta. Representa com precisão a disciplina do tema e o entendimento pacificado adotado pela banca (FCC).
> - **D)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **E)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
>
> **Gabarito: C**

---
### Teste 207
**(FCC – TRT-11 – Analista Judiciário - Tecnologia da Informação – 2017)**
José Souza, Paulo Almeida e Claudio Prinot são três funcionários que têm que realizar, no total para os três, 72 tarefas 
diariamente. Cada dia eles escolhem um critério diferente para repartir as tarefas. Por exemplo, no dia de ontem eles decidiram  
que as 72 tarefas seriam divididas entre eles diretamente proporcional às consoantes do sobrenome de cada um. Sendo assim, 
ontem Paulo Almeida teve que realizar o total de tarefas igual a

* **A)** 9.
* **B)** 24.
* **C)** 15.
* **D)** 12.
* **E)** 18.

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **B)** Correta. Representa com precisão a disciplina do tema e o entendimento pacificado adotado pela banca (FCC).
> - **C)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **D)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **E)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
>
> **Gabarito: B**

---
### Teste 208
**(FCC – TRT-1 – Analista Judiciário - Tecnologia da Informação – 2014)**
Sistemas de armazenamento de backup  são primordiais para assegurar a integridade dos dados em sistemas computacionais. 
O sistema de armazenamento caracterizado por ser disponibilizado na rede de computadores e passível de montagem para uso 
no computador, e um exemplo de tecnologia utilizada nesse sistema de armazenamento, são, respectivamente,

* **A)** NAS e CIFS.
* **B)** NAS e FibreChannel.
* **C)** DAS e NFS.
* **D)** SAN e NFS.
* **E)** SAN e FoE.

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **B)** Correta. Representa com precisão a disciplina do tema e o entendimento pacificado adotado pela banca (FCC).
> - **C)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **D)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **E)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
>
> **Gabarito: B**

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
**(FGV – TRT – Analista Judiciário - Suporte e Infraestrutura de TI – 2022)**
A analista Ana precisa implantar o pod LogPod no cluster de 
Kubernetes KCluster do TJDFT de forma que todos os nós 
elegíveis do KCluster executem uma cópia do LogPod.  
Para que o KCluster apresente uma cópia do Log Pod em cada nó 
elegível, de forma automática, Ana deve implantar o LogPod 
utilizando o recurso do Kubernetes:

* **A)** ReplicationController;
* **B)** ReplicaSet;
* **C)** StatefulSet;
* **D)** DaemonSet;
* **E)** EndpointSlice.

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **B)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **C)** Correta. Representa com precisão a disciplina do tema e o entendimento pacificado adotado pela banca (FGV).
> - **D)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **E)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
>
> **Gabarito: C**

---
### Teste 210
**(FGV – TRT – Analista Judiciário - Suporte e Infraestrutura de TI – 2022)**
A equipe de banco de dados (BD) necessita implementar  em sua 
infraestrutura própria um cluster de BD com 3 nós (3 servidores 
físicos), os quais irão compartilhar os mesmos discos, que 
deverão ser apresentados para os 3 nós como raw devices para 
criação da base de dados. O protocolo utilizado deverá ser o Fibre 
Channel (FC) e será utilizado um switch com suporte ao FC para 
permitir que os nós acessem os discos a eles apresentados.  
A arquitetura de armazenamento que deve ser utilizada para 
atender os requisitos de armazenamento para o cluster de BD é o:

* **A)** RAID 1;
* **B)** DAS;
* **C)** NAS;
* **D)** RAID 6;
* **E)** SAN.

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **B)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **C)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **D)** Correta. Representa com precisão a disciplina do tema e o entendimento pacificado adotado pela banca (FGV).
> - **E)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
>
> **Gabarito: D**

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
**(FGV – TJ-RR – Analista Judiciário - Suporte e Infraestrutura de TI – 2024)**
No Kubernetes, há duas formas de aplicar mudanças na configuração 
de uma aplicação: imperativa e declarativa.  
Considere os dois comandos a seguir: 
1:  
kubectl create -f exemplo.yaml 
2: 
kubectl apply -f exemplo-deployment.yaml 
Nesse caso, é correto afirmar que

* **A)** 1 é um exemplo de comando declarativo, em que o kubectl 
especifica a operação que se deseja aplicar.
* **B)** 2 é um exemplo de comando imperativo, em que o kubectl 
especifica a operação que se deseja aplicar.
* **C)** 2 é um exemplo de comando imperativo, em que o usuário não 
define que operações serão executadas.
* **D)** 1 é um exemplo de comando declara tivo, em que o sistema do 
Kubernetes decidirá a melhor forma de aplicá-lo.
* **E)** 2 é um exemplo de comando declarativo, em que o sistema do 
Kubernetes decidirá a melhor forma de aplicá-lo.

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **B)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **C)** Correta. Representa com precisão a disciplina do tema e o entendimento pacificado adotado pela banca (FGV).
> - **D)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **E)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
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
**(FGV – TRF-1 – Analista Judiciário - Tecnologia da Informação – 2024)**
A analista Dalva administra o cluster de Kubernetes do TRF1. 
Dalva precisa adicionar ao Kubernetes novas condições de 
prontidão customizadas para o Pod A. As novas condições devem 
ser atendidas para o Kubernetes elevar a condição do Pod A ao 
status Ready. 
Dalva deve adicionar as novas condições de prontidão ao 
manifesto do Pod A, especificamente no elemento:

* **A)** lifecycleConfig;
* **B)** readinessGates;
* **C)** containerStatuses;
* **D)** lifecycleConditions;
* **E)** readinessConditions. 

Tribunal Regional Federal da 1ª Região FGV Conhecimento 

Analista Jud - Áre Apoio Especializado - Especialidade Tecnologia da Informação  Tipo 1 – Branca – Página 14

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **B)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **C)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **D)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **E)** Correta. Representa com precisão a disciplina do tema e o entendimento pacificado adotado pela banca (FGV).
>
> **Gabarito: E**

---
### Teste 213
**(FCC – TRT-14 – Analista Judiciário - Tecnologia da Informação – 2016)**
Como uma instância de JBoss é uma configuração em execução, ao ser instalado, ele vem com diferentes configurações e cada 
uma delas é localizada no diretório JBOSS_DIST/jboss-as/server. Em linha de comando no Linux, para iniciar o JBoss com 
o conjunto de arquivo de configuração mínimo utiliza-se  o comando

* **A)** run.sh -x compact
* **B)** run.sh -c minimal
* **C)** start.sh -a compact
* **D)** start.sh -x 0
* **E)** run.sh -a minimal

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **B)** Correta. Representa com precisão a disciplina do tema e o entendimento pacificado adotado pela banca (FCC).
> - **C)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **D)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **E)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
>
> **Gabarito: B**

---
## 🌐 Fontes Oficiais e Referências Bibliográficas

* [Kubernetes Official Documentation - Componentes da Arquitetura](https://kubernetes.io/pt-br/docs/concepts/overview/components/) - Control Plane (API Server, etcd, Scheduler, Controller Manager) e Node (kubelet, kube-proxy, runtime).
* [Kubernetes Official Documentation - Workloads e Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) - Gestão declarativa de Pods, ReplicaSets, Rolling Updates e Rollbacks.
* [Kubernetes Official Documentation - Services e Ingress](https://kubernetes.io/pt-br/docs/concepts/services-networking/service/) - Comunicação de rede (ClusterIP, NodePort, LoadBalancer) e roteamento HTTP/HTTPS via Ingress.
* [Kubernetes Official Documentation - Configure Liveness, Readiness and Startup Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/) - Monitoramento de integridade e prontidão operacional dos contêineres.
* [Kubernetes Official Documentation - Persistent Volumes](https://kubernetes.io/pt-br/docs/concepts/storage/persistent-volumes/) - Gestão de armazenamento persistente com PV, PVC e StorageClass.
* BURNS, Brendan; BEDA, Joe; HIGHTOWER, Kelsey. **Kubernetes: Up and Running: Dive into the Future of Infrastructure**. 3. ed. Sebastopol: O'Reilly Media, 2022. (Cap. 4 - Pods; Cap. 5 - Services; Cap. 9 - Deployments).
* SAYFAN, Gigi. **Mastering Kubernetes**. 4. ed. Birmingham: Packt Publishing, 2022. (Cap. 2 - Arquitetura de Alto Nível; Cap. 6 - Rede e Armazenamento).
* LUKSA, Marko. **Kubernetes em Ação**. Rio de Janeiro: Alta Books, 2019. (Cap. 6 e 7 - Volumes, ConfigMaps e Secrets).
