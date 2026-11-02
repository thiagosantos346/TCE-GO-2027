# 03 - Conteinerização com Docker e Docker Compose

> **Matéria:** DevOps, Plataforma de Desenvolvimento e Engenharia de Entrega  
> **Cargo:** B02 – Técnico de Controle Externo – Especialidade: Tecnologia da Informação  
> **Arquivo:** `03_conteinerizacao_docker_e_docker_compose.md`  



---


## 📌 Ementa / Itens do Edital
- Conceitos de conteinerização vs. virtualização tradicional
- Arquitetura e componentes do Docker (Daemon, Client, Images, Containers, Registries)
- Construção de imagens e instruções do Dockerfile
- Otimização com builds de múltiplos estágios (Multi-Stage Builds)
- Gestão de dados (Volumes, Bind Mounts e tmpfs) e Redes no Docker
- Orquestração de múltiplos contêineres com Docker Compose

---

## 🧭 Sumário

1. [Fundamentos de Conteinerização vs. Virtualização Tradicional](#1-fundamentos-de-conteinerizacao-vs-virtualizacao-tradicional)
    1. [Máquinas Virtuais (Hypervisors) vs. Contêineres (Kernel Compartilhado)](#11-maquinas-virtuais-hypervisors-vs-conteineres-kernel-compartilhado)
    2. [Primitivas Essenciais do Kernel Linux: Namespaces e Control Groups (cgroups)](#12-primitivas-essenciais-do-kernel-linux-namespaces-e-control-groups-cgroups)
    3. [Arquitetura do Docker Engine: Client, Daemon, containerd, runc e Registries](#13-arquitetura-do-docker-engine-client-daemon-containerd-runc-e-registries)
    4. [Sistema de Arquivos em Camadas (Overlay2 UnionFS) e Copy-on-Write (CoW)](#14-sistema-de-arquivos-em-camadas-overlay2-unionfs-e-copy-on-write-cow)
    5. [Teste 192](#Teste-192)
    6. [Teste 193](#Teste-193)
    7. [Teste 194](#Teste-194)
2. [Construção de Imagens e Anatomia do Dockerfile](#2-construcao-de-imagens-e-anatomia-do-dockerfile)
    1. [Instruções Canônicas: FROM, WORKDIR, COPY vs. ADD, RUN, ENV vs. ARG](#21-instrucoes-canonicas-from-workdir-copy-vs-add-run-env-vs-arg)
    2. [Execução de Processos: ENTRYPOINT vs. CMD (Exec Form vs. Shell Form)](#22-execucao-de-processos-entrypoint-vs-cmd-exec-form-vs-shell-form)
    3. [Exposição de Portas e Segurança: EXPOSE vs. Publicação no Host e Diretiva USER](#23-exposicao-de-portas-e-seguranca-expose-vs-publicacao-no-host-e-diretiva-user)
    4. [Otimização com Builds de Múltiplos Estágios (Multi-Stage Builds) e Cache de Camadas](#24-otimizacao-com-builds-de-multiplos-estagios-multi-stage-builds-e-cache-de-camadas)
    5. [Teste 195](#Teste-195)
    6. [Teste 196](#Teste-196)
    7. [Teste 197](#Teste-197)
    8. [Teste 198](#Teste-198)
3. [Persistência de Dados e Gerenciamento de Armazenamento](#3-persistencia-de-dados-e-gerenciamento-de-armazenamento)
    1. [Efemeridade da Camada de Leitura e Escrita do Contêiner](#31-efemeridade-da-camada-de-leitura-e-escrita-do-conteiner)
    2. [Comparativo: Named Volumes vs. Bind Mounts vs. tmpfs Mounts](#32-comparativo-named-volumes-vs-bind-mounts-vs-tmpfs-mounts)
    3. [Teste 199](#Teste-199)
4. [Redes no Docker: Drivers e Resolução de Nomes](#4-redes-no-docker-drivers-e-resolucao-de-nomes)
    1. [Drivers de Rede: bridge, host, none, overlay e macvlan](#41-drivers-de-rede-bridge-host-none-overlay-e-macvlan)
    2. [Resolução de Nomes por DNS Integrado em Redes Customizadas](#42-resolucao-de-nomes-por-dns-integrado-em-redes-customizadas)
    3. [Teste 200](#Teste-200)
    4. [Teste 201](#Teste-201)
5. [Orquestração Multi-Contêiner com Docker Compose](#5-orquestracao-multi-conteiner-com-docker-compose)
    1. [Estrutura do Manifesto Compose: Services, Networks, Volumes e depends_on](#51-estrutura-do-manifesto-compose-services-networks-volumes-e-dependson)
    2. [Ciclo de Vida e Comandos Operacionais da CLI](#52-ciclo-de-vida-e-comandos-operacionais-da-cli)
    3. [Teste 202](#Teste-202)
6. [🌐 Fontes Oficiais e Referências Bibliográficas](#fontes-oficiais-e-referencias-bibliograficas)

---

## 1. Fundamentos de Conteinerização vs. Virtualização Tradicional

A compreensão da barreira arquitetural entre Máquinas Virtuais (VMs) e Contêineres de software constitui um dos temas mais recorrentes em concursos públicos da FCC na área de infraestrutura, arquitetura de sistemas e DevOps.

```mermaid
flowchart TD
    subgraph VM_Arch["Virtualização Tradicional (VMs)"]
        direction TB
        APP_VM1["App A"]
        BIN_VM1["Libs / Binários"]
        GUEST_OS1["Guest OS Completo<br/>(Kernel próprio, Drivers, SO)"]
        APP_VM2["App B"]
        BIN_VM2["Libs / Binários"]
        GUEST_OS2["Guest OS Completo<br/>(Kernel próprio, Drivers, SO)"]
        HYPERVISOR["Hipervisor (Type 1 Bare-Metal ou Type 2 Hosted)"]
        HOST_OS_HW1["Hardware Físico / Host OS"]
        
        APP_VM1 --- BIN_VM1 --- GUEST_OS1 --- HYPERVISOR
        APP_VM2 --- BIN_VM2 --- GUEST_OS2 --- HYPERVISOR
        HYPERVISOR --- HOST_OS_HW1
    end

    subgraph Container_Arch["Conteinerização (Docker)"]
        direction TB
        APP_C1["App A"]
        BIN_C1["Libs / Dependências"]
        CONT1["Contêiner A (Processo Isolado)"]
        APP_C2["App B"]
        BIN_C2["Libs / Dependências"]
        CONT2["Contêiner B (Processo Isolado)"]
        DOCKER_ENG["Docker Engine (dockerd / containerd / runc)"]
        HOST_KERNEL["Kernel Compartilhado do Linux Host<br/>(Namespaces + Control Groups)"]
        HW["Hardware Físico"]
        
        APP_C1 --- BIN_C1 --- CONT1 --- DOCKER_ENG
        APP_C2 --- BIN_C2 --- CONT2 --- DOCKER_ENG
        DOCKER_ENG --- HOST_KERNEL --- HW
    end
```

### 1.1 Máquinas Virtuais (Hypervisors) vs. Contêineres (Kernel Compartilhado)

A distinção basilar assenta-se no **nível de abstração** e na **existência ou não de um núcleo de sistema operacional independente**:

- **Máquinas Virtuais (VMs):**
    - Operam sob a abstração em **nível de hardware**.
    - O **Hipervisor** (*Hypervisor* Type 1 bare-metal como VMware ESXi/KVM, ou Type 2 hospedado como VirtualBox) emula componentes físicos virtuais (CPU, memória RAM, interfaces de rede, controladoras de disco).
    - Cada máquina virtual instala e executa um **Sistema Operacional convidado (*Guest OS*) completo e autônomo**, contendo seu próprio Kernel, drivers e daemons de inicialização.
    - **Sobrecarga (*Overhead*):** Elevado consumo de espaço em disco e memória RAM apenas para manter as instâncias de SO convidado rodando; tempo de inicialização lento (de dezenas de segundos a vários minutos para executar o boot completo).
- **Contêineres (Docker / OCI):**
    - Operam sob a abstração em **nível de sistema operacional**.
    - Os contêineres **NÃO possuem kernel próprio nem executam um Guest OS completo**. Todos os contêineres em execução em um mesmo host compartilham diretamente o **mesmo Kernel do sistema operacional hospedeiro**.
    - Um contêiner nada mais é do que um **processo padrão do Linux encapsulado e isolado** do restante do sistema através de recursos nativos do núcleo.
    - **Eficiência e Densidade:** Inicialização em milissegundos (o tempo de iniciar um processo simples); consumo mínimo de RAM e CPU; densidade operacional altíssima (dezenas ou centenas de contêineres em um mesmo nó físico).

| Parâmetro de Comparação | Máquinas Virtuais (VMs) | Contêineres (Docker) |
| :--- | :--- | :--- |
| **Nível de Abstração** | Abstração da camada de **Hardware**. | Abstração em nível de **Processos do Sistema Operacional**. |
| **Núcleo de SO (Kernel)** | **SIM**. Cada VM possui seu próprio kernel independente (*Guest OS*). | **NÃO**. Compartilham o **mesmo Kernel do host**. |
| **Mecanismo Central** | Hipervisor (*Hypervisor Type 1 ou Type 2*). | Primitivas do Kernel Linux: *Namespaces* e *cgroups*. |
| **Tempo de Inicialização** | Dezenas de segundos a minutos (boot de SO completo). | Milissegundos a poucos segundos (inicialização de processo comum). |
| **Consumo de Recursos** | Alto (gigabytes alocados para o SO convidado). | Mínimo (apenas o espaço estritamente consumido pela aplicação). |
| **Nível de Isolamento** | Muito alto (isolamento por hardware via instruções de CPU VT-x/AMD-V). | Alto (isolamento em espaço de usuário do Linux via kernel). |

### 1.2 Primitivas Essenciais do Kernel Linux: Namespaces e Control Groups (cgroups)

A segurança e o isolamento de um contêiner Docker não decorrem de mágica, mas do acoplamento de duas tecnologias maduras do Kernel Linux:

#### 1. Linux Namespaces (Isolamento de Visibilidade)
Determinam **o que um contêiner consegue enxergar**. Cada contêiner recebe seu próprio conjunto isolado de namespaces:

- **`pid` (Process ID):** Isola a árvore de processos. Dentro do contêiner, o processo principal da aplicação visualiza a si mesmo como `PID 1`, sendo totalmente cego aos processos em execução no host e em outros contêineres.
- **`net` (Network):** Isola interfaces de rede, portas TCP/UDP, tabelas de roteamento e regras de firewall (iptables/nftables).
- **`mnt` (Mount):** Isola os pontos de montagem do sistema de arquivos, garantindo que o contêiner enxergue apenas a sua raiz (`/`) privativa.
- **`ipc` (Inter-Process Communication):** Isola mecanismos de comunicação interprocessos, como memória compartilhada e semáforos POSIX.
- **`uts` (UNIX Timesharing System):** Permite que cada contêiner possua seu próprio *hostname* e nome de domínio independente.
- **`user` (User IDs):** Mapeia UIDs e GIDs entre o contêiner e o host, viabilizando que um processo execute como `root` (UID 0) dentro do contêiner, mas seja mapeado para um usuário não privilegiado comum (ex.: UID 10001) no sistema hospedeiro.

#### 2. Control Groups - `cgroups` (Limitação e Governança de Recursos)
Determinam **quanto de recursos computacionais um contêiner pode consumir**:

- Permitem estabelecer quotas estritas e limites máximos de consumo de **memória RAM** (evitando ataques de exaustão de memória e acionamento descontrolado do *OOM Killer* no host).
- Limitam a fração de **tempo de CPU** (ex.: reservar 1.5 núcleos para um serviço).
- Controlam a largura de banda de tráfego de rede e taxas de leitura/gravação em disco (*Block I/O limits*).

### 1.3 Arquitetura do Docker Engine: Client, Daemon, containerd, runc e Registries

A arquitetura do Docker é cliente-servidor distribuída e baseada em componentes modulares padronizados pela *Open Container Initiative* (OCI):

- **Docker Client (CLI):** O binário de linha de comando `docker` utilizado pelos operadores e desenvolvedores. Comunica-se com o daemon local ou remoto através de chamadas REST em um socket Unix (`/var/run/docker.sock`) ou conexão TCP com TLS.
- **Docker Daemon (`dockerd`):** Serviço persistente de segundo plano que processa requisições da API, orquestra contêineres, compila imagens e gerencia volumes e redes virtuais.
- **containerd:** Daemon de gerenciamento de contêineres de alto nível (desacoplado do Docker e doado à CNCF). Supervisiona o ciclo de vida completo: download de imagens de repositórios remotos, provisionamento de armazenamento e monitoramento de execução.
- **runc:** Runtime de baixo nível compatível com a especificação OCI. É o componente final responsável por interagir diretamente com as chamadas de sistema (*syscalls*) do Kernel Linux para criar os *namespaces* e *cgroups* e despachar o processo do contêiner.
- **Registries de Imagens:** Servidores centralizados de catalogação e armazenamento de imagens Docker (como Docker Hub público, AWS Elastic Container Registry - ECR, Harbor corporativo ou GitHub Packages).

### 1.4 Sistema de Arquivos em Camadas (Overlay2 UnionFS) e Copy-on-Write (CoW)

Uma imagem Docker é uma coleção imutável de **camadas de somente leitura (*Read-Only Layers*)** empilhadas hierarquicamente.

- **UnionFS / Overlay2:** Driver de armazenamento padrão que sobrepõe as múltiplas camadas de diretórios, apresentando-as ao contêiner como um sistema de arquivos unificado e coeso.
- **Copy-on-Write (CoW):** Quando um contêiner é instanciado a partir de uma imagem, o Docker cria uma camada muito fina e descartável de **leitura e escrita (*Container Read-Write Layer*)** no topo da pilha. Se o contêiner precisa alterar um arquivo que pertence a uma camada inferior de somente leitura, o driver copia esse arquivo para a camada superior gravável e aplica a alteração ali. As camadas da imagem base permanecem intactas e compartilhadas por todos os outros contêineres que utilizam a mesma imagem.

---

### Teste 192
**(FGV – TJ-DFT – Analista Judiciario Suporte Em Tecnologia da Informacao – 2022)**
A analista Sara modificou alguns arquivos do container Docker TJSiteContainer que se encontra em execução. Para criar uma imagem Docker a partir do estado atual de TJSiteContainer, a fim de persistirem as modificações efetuadas em seus arquivos, Sara deve utilizar o comando:

* **A)** docker create
* **B)** docker diff
* **C)** docker export
* **D)** docker image save
* **E)** docker commit

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "docker create". De acordo com a teoria estudada em *4.2 Resolução de Nomes por DNS Integrado em Redes Customizadas*, redes Customizadas pelo Usuário (*User-Defined Networks*): Ao criar uma rede com `docker network create minha-rede`, o Docker ativa um servidor DNS interno embutido.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "docker diff". De acordo com a teoria estudada em *2.3 Exposição de Portas e Segurança: EXPOSE vs. Publicação no Host e Diretiva USER*, para que o contêiner fique acessível pelo tráfego de fora do host, o operador deve compulsoriamente mapear a porta via `docker run -p <porta_host>:<porta_container>` ou pela diretiva `ports` no Docker Compose.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "docker export". De acordo com a teoria estudada em *1.4 Sistema de Arquivos em Camadas (Overlay2 UnionFS) e Copy-on-Write (CoW)*, uma imagem Docker é uma coleção imutável de camadas de somente leitura (*Read-Only Layers*) empilhadas hierarquicamente.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "docker image save". De acordo com a teoria estudada em *5.1 Estrutura do Manifesto Compose: Services, Networks, Volumes e depends_on*, `services`: Declara cada um dos contêineres da aplicação. Define a imagem pronta (`image:`) ou o contexto de construção local (`build:`), portas mapeadas (`ports:`), variáveis (`environment:`) e volumes acoplados.
> - **E)** **Correta.** Conforme fundamentado na seção *1.4 Sistema de Arquivos em Camadas (Overlay2 UnionFS) e Copy-on-Write (CoW)* deste guia, copy-on-Write (CoW): Quando um contêiner é instanciado a partir de uma imagem, o Docker cria uma camada muito fina e descartável de leitura e escrita (*Container Read-Write Layer*) no topo da pilha. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ-DFT/2022) ao estabelecer que "docker commit".
>
> **Gabarito: E**

---

### Teste 193
**(CEBRASPE – TJ-RJ – Analista Judiciario Grupo Tecnologia da Informacao Analista de Infraestrutura de Tic – 2021)**
Por meio de determinada camada de software localizada entre o hardware e o sistema operacional, diversas máquinas virtuais podem ter acesso aos recursos de hardware, como CPU, memória, rede, armazenamento, entre outros. Essa camada de software é denominada

* **A)** hosted.
* **B)** hypervisor.
* **C)** processo virtualizado.
* **D)** abstração de interface.
* **E)** BIOS.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "hosted". De acordo com a teoria estudada em *1.1 Máquinas Virtuais (Hypervisors) vs. Contêineres (Kernel Compartilhado)*, mecanismo Central: Hipervisor (*Hypervisor Type 1 ou Type 2*). — Primitivas do Kernel Linux: *Namespaces* e *cgroups*.
> - **B)** **Correta.** Conforme fundamentado na seção *1.1 Máquinas Virtuais (Hypervisors) vs. Contêineres (Kernel Compartilhado)* deste guia, o Hipervisor (*Hypervisor* Type 1 bare-metal como VMware ESXi/KVM, ou Type 2 hospedado como VirtualBox) emula componentes físicos virtuais (CPU, memória RAM, interfaces de rede, controladoras de disco). Dessa forma, está plenamente correta a assertiva da banca (CEBRASPE – TJ-RJ/2021) ao estabelecer que "hypervisor".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "processo virtualizado". De acordo com a teoria estudada em *1.1 Máquinas Virtuais (Hypervisors) vs. Contêineres (Kernel Compartilhado)*, eficiência e Densidade: Inicialização em milissegundos (o tempo de iniciar um processo simples); consumo mínimo de RAM e CPU; densidade operacional altíssima (dezenas ou centenas de contêineres em um mesmo nó físico).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "abstração de interface". De acordo com a teoria estudada em *1.1 Máquinas Virtuais (Hypervisors) vs. Contêineres (Kernel Compartilhado)*, nível de Abstração: Abstração da camada de Hardware. — Abstração em nível de Processos do Sistema Operacional.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "BIOS". De acordo com a teoria estudada em *1.1 Máquinas Virtuais (Hypervisors) vs. Contêineres (Kernel Compartilhado)*, nível de Isolamento: Muito alto (isolamento por hardware via instruções de CPU VT-x/AMD-V). — Alto (isolamento em espaço de usuário do Linux via kernel).
>
> **Gabarito: B**

---

### Teste 194
**(FCC – TRT-6 – Analista Judiciario Apoio Especializado Tecnologia da Informacao – 2012)**
Filesystem Hierarchy Standard (FHS) é a padronização da organização do sistema de arquivos do sistemas Linux à qual aderem as principais distribuições. De acordo com a FHS, arquivos executáveis que precisam estar disponíveis em single user mode, arquivos cujo conteúdo varia ao longo da operação do sistema e arquivos de configuração do sistema devem localizar-se, respectivamente, em

* **A)** /boot, /tmp e /usr/share.
* **B)** /usr/bin, /tmp e /usr/local.
* **C)** /bin, /opt e /usr/local.
* **D)** /boot, /usr e /etc.
* **E)** /bin, /var e /etc.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "/boot, /tmp e /usr/share". De acordo com a teoria estudada em *1.1 Máquinas Virtuais (Hypervisors) vs. Contêineres (Kernel Compartilhado)*, sobrecarga (*Overhead*): Elevado consumo de espaço em disco e memória RAM apenas para manter as instâncias de SO convidado rodando; tempo de inicialização lento (de dezenas de segundos a vários minutos para executar o boot completo).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "/usr/bin, /tmp e /usr/local". De acordo com a teoria estudada em *2.2 Execução de Processos: ENTRYPOINT vs. CMD (Exec Form vs. Shell Form)*, shell Form (Desaconselhado): Notação em string simples: `ENTRYPOINT nginx -g "daemon off;"`. O Docker invoca internamente `/bin/sh -c`, tornando o shell o `PID 1` e impedindo o repasse adequado de sinais de encerramento gracioso para a aplicação.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "/bin, /opt e /usr/local". De acordo com a teoria estudada em *3.2 Comparativo: Named Volumes vs. Bind Mounts vs. tmpfs Mounts*, bind Mounts: Qualquer caminho arbitrário absoluto do host (ex.: `/opt/app` ou `C:\projetos`) — NÃO (depende da estrutura física e de permissões do host) — Desenvolvimento local.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "/boot, /usr e /etc". De acordo com a teoria estudada em *1.1 Máquinas Virtuais (Hypervisors) vs. Contêineres (Kernel Compartilhado)*, tempo de Inicialização: Dezenas de segundos a minutos (boot de SO completo). — Milissegundos a poucos segundos (inicialização de processo comum).
> - **E)** **Correta.** Conforme fundamentado na seção *1.3 Arquitetura do Docker Engine: Client, Daemon, containerd, runc e Registries* deste guia, docker Client (CLI): O binário de linha de comando `docker` utilizado pelos operadores e desenvolvedores. Comunica-se com o daemon local ou remoto através de chamadas REST em um socket Unix (`/var/run/docker.sock`) ou conexão TCP com TLS. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT-6/2012) ao estabelecer que "/bin, /var e /etc".
>
> **Gabarito: E**

---

## 2. Construção de Imagens e Anatomia do Dockerfile

O `Dockerfile` é o manifesto declarativo em formato de texto simples que estabelece o passo a passo automatizado para compilar uma imagem de contêiner.

### 2.1 Instruções Canônicas: FROM, WORKDIR, COPY vs. ADD, RUN, ENV vs. ARG

- **`FROM <imagem>:<tag>`:** Especifica a imagem base que fundamenta a construção. Toda compilação deve iniciar por um comando `FROM` (ou `FROM scratch` para construir uma imagem vazia de 0 bytes para binários estáticos).
- **`WORKDIR /caminho`:** Define o diretório de trabalho padrão para as instruções subsequentes (`RUN`, `CMD`, `ENTRYPOINT`, `COPY`). Se a pasta não existir no sistema de arquivos da imagem, o Docker a cria automaticamente. É uma boa prática usar `WORKDIR` em vez de comandos imperativos `RUN cd /caminho`.
- **`COPY` vs. `ADD` (Ponto Forte em Provas):**
    - **`COPY <origem> <destino>`:** Realiza a cópia direta, simples e estrita de arquivos e pastas da máquina local (contexto de build) para o interior da imagem. **É a instrução oficialmente recomendada pelas boas práticas para cópias locais.**
    - **`ADD <origem> <destino>`:** Possui recursos extras automáticos: permite baixar arquivos remotos via URLs HTTP/HTTPS e descompacta compulsoriamente arquivos tar/gzip (`.tar`, `.tar.gz`) diretamente no destino. Por apresentar comportamentos implícitos que podem introduzir vulnerabilidades ou aumentar o tamanho da imagem, seu uso indiscriminado é desaconselhado pela comunidade técnica.
- **`RUN <comando>`:** Executa comandos durante a fase de construção (*build-time*), como instalação de pacotes (`apt-get install`, `npm install`). Cada comando `RUN` gera uma **nova camada imutável** no sistema de arquivos da imagem.
- **`ENV` vs. `ARG`:**
    - **`ARG`:** Define variáveis disponíveis **exclusivamente durante a compilação da imagem** (`docker build --build-arg CHAVE=VALOR`). Não persiste nos metadados nem no ambiente do contêiner em runtime.
    - **`ENV`:** Define variáveis de ambiente que são gravadas permanentemente na imagem e permanecem **ativas durante a execução do contêiner em produção (runtime)**.

### 2.2 Execução de Processos: ENTRYPOINT vs. CMD (Exec Form vs. Shell Form)

A definição de qual processo será executado ao instanciar o contêiner é regulada pela combinação de `ENTRYPOINT` e `CMD`:

- **`ENTRYPOINT`:** Define o **executável imutável principal** do contêiner. Ele transforma o contêiner em um comando executável dedicado. Não é sobrescrito facilmente por parâmetros informados ao final do comando `docker run`.
- **`CMD`:** Define os **argumentos padrão** ou o comando de fallback. Se utilizado em conjunto com `ENTRYPOINT`, os valores declarados no `CMD` atuam como parâmetros padrão que podem ser facilmente substituídos pelo usuário na linha de comando.
- **Regra de Sobrescrita Prática:** Ao executar `docker run minha-imagem arg1 arg2`, os argumentos `arg1 arg2` substituem integralmente o conteúdo da diretiva `CMD`, mas são repassados como parâmetros para o executável fixado no `ENTRYPOINT`.

**Formatos de Notação (Exec Form vs. Shell Form):**

- **Exec Form (Recomendado):** Notação em vetor JSON com aspas duplas: `ENTRYPOINT ["nginx", "-g", "daemon off;"]`. Executa o processo diretamente sem passar por interpretadores de terminal, permitindo que o processo receba os sinais de término do sistema operacional (`SIGTERM`, `SIGKILL`) como `PID 1`.
- **Shell Form (Desaconselhado):** Notação em string simples: `ENTRYPOINT nginx -g "daemon off;"`. O Docker invoca internamente `/bin/sh -c`, tornando o shell o `PID 1` e impedindo o repasse adequado de sinais de encerramento gracioso para a aplicação.

### 2.3 Exposição de Portas e Segurança: EXPOSE vs. Publicação no Host e Diretiva USER

- **`EXPOSE <porta>`:** Instrução **meramente informativa e documental**. Ela sinaliza ao desenvolvedor ou orquestrador em qual porta o serviço interno escuta por padrão, mas **NÃO abre portas no firewall da máquina host nem publica a porta externamente**. Para que o contêiner fique acessível pelo tráfego de fora do host, o operador deve compulsoriamente mapear a porta via `docker run -p <porta_host>:<porta_container>` ou pela diretiva `ports` no Docker Compose.
- **Diretiva `USER` e Segurança (Princípio do Menor Privilégio):** Por padrão, os processos dentro de um contêiner rodam como o usuário `root` (UID 0). Caso a aplicação sofra um ataque de *container breakout*, o invasor pode comprometer o host. A diretiva `USER <usuario_sem_privilegio>` altera o contexto de execução para um usuário comum do sistema, mitigando severamente riscos de escalada de privilégios.

### 2.4 Otimização com Builds de Múltiplos Estágios (Multi-Stage Builds) e Cache de Camadas

```mermaid
flowchart TD
    subgraph MultiStage["Padrão Multi-Stage Build"]
        direction TB
        S1["Estágio 1 (Builder): maven:3.9-eclipse-temurin-17<br/>- Baixa 800 MB de SDK e dependências<br/>- Compila o código com 'mvn package'<br/>- Gera o binário final 'app.jar'"]
        S2["Estágio 2 (Runtime): eclipse-temurin:17-jre-alpine<br/>- Imagem mínima de apenas 150 MB<br/>- Sem compiladores ou código-fonte"]
        COPY["COPY --from=builder /app/app.jar /app/app.jar"]
        IMG_FINAL["Imagem Final Gerada (Produção):<br/>- Apenas 160 MB<br/>- Mínima superfície de ataque e sem ferramentas de build"]
        
        S1 -.-> COPY
        S2 --> COPY --> IMG_FINAL
    end
```

#### O Padrão Multi-Stage Build
Em pipelines corporativos de CI/CD, compilar software exige SDKs volumosos, compiladores C/C++, ferramentas de empacotamento e código-fonte bruto. Se esses artefatos forem mantidos na imagem final que vai para produção, a imagem terá gigabytes de tamanho e conterá dezenas de vulnerabilidades conhecidas (CVEs).

A funcionalidade de **Multi-Stage Builds** resolve esse problema declarando múltiplos comandos `FROM` no mesmo `Dockerfile`:

1. **Estágio de Construção (*Builder*):** `FROM maven:3.9-eclipse-temurin-17 AS builder`. Utiliza o ambiente pesado de build para compilar e empacotar a aplicação, gerando o artefato final (`app.jar`).
2. **Estágio de Execução (*Runtime*):** `FROM eclipse-temurin:17-jre-alpine`. Utiliza uma imagem base mínima que contém apenas o ambiente estrito de execução (JRE ou Alpine/Distroless).
3. **Cópia Seletiva:** Através do comando `COPY --from=builder /app/target/app.jar /app/app.jar`, extrai-se apenas o binário compilado. Todo o SDK do Maven, código-fonte original e arquivos temporários são descartados.
4. **Benefícios:** Redução drástica do tamanho da imagem (de centenas de megabytes para dezenas), agilidade no download pelos nós do Kubernetes e minimização radical da superfície de ataque cibernético.

---

### Teste 195
**(FCC – TRT-4 – Analista Judiciario Tecnologia da Informacao – 2015)**
A possibilidade de compartilhar arquivos entre diferentes sistemas operacionais é fundamental para aumentar a produtividade computacional. A montagem automática de uma partição com sistema de arquivos CIFS, durante o boot do servidor com sistema operacional Linux, deve ser configurada no arquivo

* **A)** /etc/fstab.
* **B)** /boot/mount.
* **C)** /etc/mount.
* **D)** /boot/inittab.
* **E)** /etc/initd.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *1. Linux Namespaces (Isolamento de Visibilidade)* deste guia, `mnt` (Mount): Isola os pontos de montagem do sistema de arquivos, garantindo que o contêiner enxergue apenas a sua raiz (`/`) privativa. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT-4/2015) ao estabelecer que "/etc/fstab".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "/boot/mount". De acordo com a teoria estudada em *1.1 Máquinas Virtuais (Hypervisors) vs. Contêineres (Kernel Compartilhado)*, sobrecarga (*Overhead*): Elevado consumo de espaço em disco e memória RAM apenas para manter as instâncias de SO convidado rodando; tempo de inicialização lento (de dezenas de segundos a vários minutos para executar o boot completo).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "/etc/mount". De acordo com a teoria estudada em *2.1 Instruções Canônicas: FROM, WORKDIR, COPY vs. ADD, RUN, ENV vs. ARG*, `RUN <comando>`: Executa comandos durante a fase de construção (*build-time*), como instalação de pacotes (`apt-get install`, `npm install`). Cada comando `RUN` gera uma nova camada imutável no sistema de arquivos da imagem.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "/boot/inittab". De acordo com a teoria estudada em *1.1 Máquinas Virtuais (Hypervisors) vs. Contêineres (Kernel Compartilhado)*, tempo de Inicialização: Dezenas de segundos a minutos (boot de SO completo). — Milissegundos a poucos segundos (inicialização de processo comum).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "/etc/initd". De acordo com a teoria estudada em *1.4 Sistema de Arquivos em Camadas (Overlay2 UnionFS) e Copy-on-Write (CoW)*, se o contêiner precisa alterar um arquivo que pertence a uma camada inferior de somente leitura, o driver copia esse arquivo para a camada superior gravável e aplica a alteração ali.
>
> **Gabarito: A**

---

### Teste 196
**(FCC – TRT-15 – Analista Judiciario Tecnologia da Informacao – 2015)**
O sistema operacional Linux, em suas diferentes distribuições, utiliza uma estrutura de arquivos padronizada e que se baseia na estrutura do Unix. Na estrutura de arquivos do Linux SuSE, o diretório /opt é utilizado

* **A)** pelo sistema operacional como área de memória secundária quando a memória principal se esgota.
* **B)** para o armazenamento de logs e eventos gerados pelo sistema operacional.
* **C)** como a pasta Arquivos de Programas do Windows e é reservado para a instalação de programas adicionais.
* **D)** para a montagem de dispositivos externos de leitura de mídia óptica.
* **E)** pelo sistema operacional para o armazenamento de arquivos temporários de gerenciamento de processos.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "pelo sistema operacional como área de memória secundária quando a memória principal se esgota". De acordo com a teoria estudada em *2.1 Instruções Canônicas: FROM, WORKDIR, COPY vs. ADD, RUN, ENV vs. ARG*, `RUN <comando>`: Executa comandos durante a fase de construção (*build-time*), como instalação de pacotes (`apt-get install`, `npm install`). Cada comando `RUN` gera uma nova camada imutável no sistema de arquivos da imagem.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "para o armazenamento de logs e eventos gerados pelo sistema operacional". De acordo com a teoria estudada em *1.4 Sistema de Arquivos em Camadas (Overlay2 UnionFS) e Copy-on-Write (CoW)*, unionFS / Overlay2: Driver de armazenamento padrão que sobrepõe as múltiplas camadas de diretórios, apresentando-as ao contêiner como um sistema de arquivos unificado e coeso.
> - **C)** **Correta.** Conforme fundamentado na seção *2.1 Instruções Canônicas: FROM, WORKDIR, COPY vs. ADD, RUN, ENV vs. ARG* deste guia, `WORKDIR /caminho`: Define o diretório de trabalho padrão para as instruções subsequentes (`RUN`, `CMD`, `ENTRYPOINT`, `COPY`). Se a pasta não existir no sistema de arquivos da imagem, o Docker a cria automaticamente. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT-15/2015) ao estabelecer que "como a pasta Arquivos de Programas do Windows e é reservado para a instalação de programas adicionais".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "para a montagem de dispositivos externos de leitura de mídia óptica". De acordo com a teoria estudada em *1. Linux Namespaces (Isolamento de Visibilidade)*, `mnt` (Mount): Isola os pontos de montagem do sistema de arquivos, garantindo que o contêiner enxergue apenas a sua raiz (`/`) privativa.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "pelo sistema operacional para o armazenamento de arquivos temporários de gerenciamento de processos". De acordo com a teoria estudada em *3. Persistência de Dados e Gerenciamento de Armazenamento*, por definição arquitetural, os contêineres Docker são efêmeros e sem estado (*stateless*). Compreender as opções de persistência é requisito obrigatório para a sustentação de bancos de dados relacionais e sistemas de arquivos corporativos.
>
> **Gabarito: C**

---

### Teste 197
**(FCC – TRT-14 – Analista Judiciario Apoio Especializado Tecnologia da Informacao – 2016)**
Como uma instância de JBoss é uma configuração em execução, ao ser instalado, ele vem com diferentes configurações e cada uma delas é localizada no diretório JBOSS_DIST/jboss-as/server. Em linha de comando no Linux, para iniciar o JBoss com o conjunto de arquivo de configuração mínimo utiliza-se o comando

* **A)** run.sh -x compact
* **B)** run.sh -c minimal
* **C)** start.sh -a compact
* **D)** start.sh -x 0
* **E)** run.sh -a minimal

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "run.sh -x compact". De acordo com a teoria estudada em *2.1 Instruções Canônicas: FROM, WORKDIR, COPY vs. ADD, RUN, ENV vs. ARG*, `FROM <imagem>:<tag>`: Especifica a imagem base que fundamenta a construção. Toda compilação deve iniciar por um comando `FROM` (ou `FROM scratch` para construir uma imagem vazia de 0 bytes para binários estáticos).
> - **B)** **Correta.** Conforme fundamentado na seção *2.2 Execução de Processos: ENTRYPOINT vs. CMD (Exec Form vs. Shell Form)* deste guia, `CMD`: Define os argumentos padrão ou o comando de fallback. Se utilizado em conjunto com `ENTRYPOINT`, os valores declarados no `CMD` atuam como parâmetros padrão que podem ser facilmente substituídos pelo usuário na linha de comando. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT-14/2016) ao estabelecer que "run.sh -c minimal".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "start.sh -a compact". De acordo com a teoria estudada em *3.1 Efemeridade da Camada de Leitura e Escrita do Contêiner*, se o contêiner for parado (`docker stop`) e reiniciado (`docker start`), esses dados são preservados.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "start.sh -x 0". De acordo com a teoria estudada em *1.3 Arquitetura do Docker Engine: Client, Daemon, containerd, runc e Registries*, docker Client (CLI): O binário de linha de comando `docker` utilizado pelos operadores e desenvolvedores. Comunica-se com o daemon local ou remoto através de chamadas REST em um socket Unix (`/var/run/docker.sock`) ou conexão TCP com TLS.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "run.sh -a minimal". De acordo com a teoria estudada em *2.1 Instruções Canônicas: FROM, WORKDIR, COPY vs. ADD, RUN, ENV vs. ARG*, `WORKDIR /caminho`: Define o diretório de trabalho padrão para as instruções subsequentes (`RUN`, `CMD`, `ENTRYPOINT`, `COPY`). Se a pasta não existir no sistema de arquivos da imagem, o Docker a cria automaticamente.
>
> **Gabarito: B**

---

### Teste 198
**(FGV – TRF-1 – Analista Judiciario Area Apoio Especializado Especialidade Tecnologia da Informacao – 2024)**
O analista Carlos está configurando o modo rootless do Docker em um servidor Linux. Carlos sabe que, para operar no modo rootless, o Docker exige a presença de determinados utilitários do sistema operacional que possibilitam o uso de múltiplos identificadores de usuário e de grupo no namespace de um usuário. Logo, antes de configurar o modo rootless do Docker no servidor Linux, Carlos verificou a presença dos utilitários:

* **A)** subuid e subgid;
* **B)** subuid e newgidmap;
* **C)** newuidmap e subgid;
* **D)** newuidmap e subuid;
* **E)** newuidmap e newgidmap.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "subuid e subgid". De acordo com a teoria estudada em *1. Linux Namespaces (Isolamento de Visibilidade)*, `user` (User IDs): Mapeia UIDs e GIDs entre o contêiner e o host, viabilizando que um processo execute como `root` (UID 0) dentro do contêiner, mas seja mapeado para um usuário não privilegiado comum (ex.: UID 10001) no sistema hospedeiro.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "subuid e newgidmap". De acordo com a teoria estudada em *2.3 Exposição de Portas e Segurança: EXPOSE vs. Publicação no Host e Diretiva USER*, a diretiva `USER <usuario_sem_privilegio>` altera o contexto de execução para um usuário comum do sistema, mitigando severamente riscos de escalada de privilégios.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "newuidmap e subgid". De acordo com a teoria estudada em *O Padrão Multi-Stage Build*, em pipelines corporativos de CI/CD, compilar software exige SDKs volumosos, compiladores C/C++, ferramentas de empacotamento e código-fonte bruto.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "newuidmap e subuid". De acordo com a teoria estudada em *2.2 Execução de Processos: ENTRYPOINT vs. CMD (Exec Form vs. Shell Form)*, executa o processo diretamente sem passar por interpretadores de terminal, permitindo que o processo receba os sinais de término do sistema operacional (`SIGTERM`, `SIGKILL`) como `PID 1`.
> - **E)** **Correta.** Conforme fundamentado na seção *4.2 Resolução de Nomes por DNS Integrado em Redes Customizadas* deste guia, redes Customizadas pelo Usuário (*User-Defined Networks*): Ao criar uma rede com `docker network create minha-rede`, o Docker ativa um servidor DNS interno embutido. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRF-1/2024) ao estabelecer que "newuidmap e newgidmap".
>
> **Gabarito: E**

---

## 3. Persistência de Dados e Gerenciamento de Armazenamento

Por definição arquitetural, os contêineres Docker são **efêmeros e sem estado (*stateless*)**. Compreender as opções de persistência é requisito obrigatório para a sustentação de bancos de dados relacionais e sistemas de arquivos corporativos.

```mermaid
flowchart TD
    subgraph Storage["Tipos de Armazenamento no Docker"]
        direction TB
        CONT["Contêiner Docker (Espaço Isolado)"]
        VOL["Named Volume (/var/lib/docker/volumes/)<br/>- Gerenciado pelo Docker<br/>- Alta performance e seguro<br/>- Padrão recomendado em produção"]
        BIND["Bind Mount (/home/user/meu-codigo/)<br/>- Vinculado a qualquer pasta do Host<br/>- Ideal para desenvolvimento local"]
        TMP["tmpfs Mount (Memória RAM do Host)<br/>- Não grava em disco<br/>- Dados ultra-rápidos e sensíveis"]
        
        CONT <--> VOL
        CONT <--> BIND
        CONT <--> TMP
    end
```

### 3.1 Efemeridade da Camada de Leitura e Escrita do Contêiner

Todas as modificações, gravações de logs e escritas em tabelas realizadas por uma aplicação em execução dentro de um contêiner são salvas na camada fina de leitura e escrita (*Container Read-Write Layer*).

- Se o contêiner for parado (`docker stop`) e reiniciado (`docker start`), esses dados são preservados.
- Contudo, **se o contêiner for removido (`docker rm`)**, essa camada é destruída imediata e irremediavelmente, ocasionando a perda total de todos os dados que não foram explicitamente montados em volumes persistentes.

### 3.2 Comparativo: Named Volumes vs. Bind Mounts vs. tmpfs Mounts

| Tipo de Montagem | Localização no Disco do Host | Gerenciado pelo Docker Engine? | Caso de Uso Principal e Boas Práticas |
| :--- | :--- | :--- | :--- |
| **Named Volumes** | `/var/lib/docker/volumes/<nome>/_data` | **SIM** (via comandos `docker volume create/ls/rm`) | **Padrão ouro para produção e bancos de dados (PostgreSQL, MySQL, MongoDB)**. Independe do SO hospedeiro, permite backups simples e oferece alto rendimento de I/O. |
| **Bind Mounts** | Qualquer caminho arbitrário absoluto do host (ex.: `/opt/app` ou `C:\projetos`) | **NÃO** (depende da estrutura física e de permissões do host) | **Desenvolvimento local**. Permite montar o código-fonte da máquina do desenvolvedor dentro do contêiner para viabilizar *hot-reloading* imediato. |
| **tmpfs Mounts** | Alocado diretamente na **Memória RAM** volátil do hospedeiro | **SIM** (via Docker Engine) | **Armazenamento de segredos, senhas e operações temporárias intensivas**. Não grava dados no disco físico; os dados somem ao desligar o contêiner. |

---

### Teste 199
**(FCC – TRT-15 – Analista Judiciario Tecnologia da Informacao – 2015)**
Tipo de memória ROM que também permite a regravação de dados. No entanto, ao contrário do que acontece com as memórias EPROM, os processos para apagar e gravar dados são feitos por um método que faz com que não seja necessário mover o dispositivo de seu lugar para um aparelho especial para que a regravação ocorra. Trata-se de

* **A)** EVPROM − Electrically Virtual Programmable Read-Only Memory.
* **B)** EEPROM − Electrically Erasable Programmable Read-Only Memory.
* **C)** PEROM − Programmable Erasable Read-Only Memory.
* **D)** MROM − Magnetoresistive Read-Only Memory.
* **E)** PCROM − Programmable Computer Read-Only Memory.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "EVPROM − Electrically Virtual Programmable Read-Only Memory". De acordo com a teoria estudada em *3.1 Efemeridade da Camada de Leitura e Escrita do Contêiner*, todas as modificações, gravações de logs e escritas em tabelas realizadas por uma aplicação em execução dentro de um contêiner são salvas na camada fina de leitura e escrita (*Container Read-Write Layer*).
> - **B)** **Correta.** Conforme fundamentado na seção *1.4 Sistema de Arquivos em Camadas (Overlay2 UnionFS) e Copy-on-Write (CoW)* deste guia, uma imagem Docker é uma coleção imutável de camadas de somente leitura (*Read-Only Layers*) empilhadas hierarquicamente. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT-15/2015) ao estabelecer que "EEPROM − Electrically Erasable Programmable Read-Only Memory".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "PEROM − Programmable Erasable Read-Only Memory". De acordo com a teoria estudada em *1.4 Sistema de Arquivos em Camadas (Overlay2 UnionFS) e Copy-on-Write (CoW)*, copy-on-Write (CoW): Quando um contêiner é instanciado a partir de uma imagem, o Docker cria uma camada muito fina e descartável de leitura e escrita (*Container Read-Write Layer*) no topo da pilha.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "MROM − Magnetoresistive Read-Only Memory". De acordo com a teoria estudada em *3.2 Comparativo: Named Volumes vs. Bind Mounts vs. tmpfs Mounts*, tmpfs Mounts: Alocado diretamente na Memória RAM volátil do hospedeiro — SIM (via Docker Engine) — Armazenamento de segredos, senhas e operações temporárias intensivas. Não grava dados no disco físico; os dados somem ao desligar o contêiner.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "PCROM − Programmable Computer Read-Only Memory". De acordo com a teoria estudada em *3.2 Comparativo: Named Volumes vs. Bind Mounts vs. tmpfs Mounts*, tipo de Montagem: Localização no Disco do Host — Gerenciado pelo Docker Engine? — Caso de Uso Principal e Boas Práticas.
>
> **Gabarito: B**

---

## 4. Redes no Docker: Drivers e Resolução de Nomes

O Docker abstrai a conectividade de contêineres através de subsistemas de rede modulares controlados por drivers específicos.

### 4.1 Drivers de Rede: bridge, host, none, overlay e macvlan

- **`bridge` (Ponte):** É o driver de rede padrão no Linux. Cria uma ponte de rede virtual interna na máquina hospedeira (tipicamente `docker0`). Cada contêiner recebe um endereço IP privativo (ex.: na faixa `172.17.0.0/16`).
- **`host`:** Elimina o isolamento de pilha de rede entre o contêiner e a máquina hospedeira. O contêiner compartilha as portas e a interface de rede física diretamente com o host. Não há overhead de tradução de endereços (NAT), mas dois contêineres não podem utilizar a mesma porta simultaneamente.
- **`none`:** Desativa compulsoriamente a conectividade de rede do contêiner. Mantém apenas a interface local de loopback (`127.0.0.1`), deixando o contêiner completamente isolado de acessos externos e de outros serviços.
- **`overlay`:** Driver de rede virtual distribuída para ambientes com múltiplos servidores físicos (*multi-host*). Criptografa e roteia o tráfego de contêineres entre diferentes nós, atuando como alicerce de orquestradores como o Docker Swarm.
- **`macvlan`:** Atribui um endereço MAC físico diretamente à interface virtual do contêiner, fazendo com que ele se apresente perante a rede corporativa (switch/roteador físico) como se fosse um servidor físico independente com IP próprio na sub-rede da LAN.

### 4.2 Resolução de Nomes por DNS Integrado em Redes Customizadas

Existe uma diferença crítica cobrada em concursos entre a rede bridge padrão e redes bridge criadas pelo usuário:

1. **Rede Bridge Padrão (`bridge` default):** Contêineres só conseguem se comunicar diretamente por endereços IP ou usando links legados desaconselhados (`--link`). **Não há suporte nativo à resolução automática de nomes por DNS.**
2. **Redes Customizadas pelo Usuário (*User-Defined Networks*):** Ao criar uma rede com `docker network create minha-rede`, o Docker ativa um **servidor DNS interno embutido**. Todos os contêineres vinculados a essa rede conseguem resolver e alcançar seus pares **utilizando diretamente o próprio nome do contêiner como endereço de rede (hostname)**.

---

### Teste 200
**(FCC – TRT-16 – Analista Judiciario Tecnologia da Informacao – 2014)**
A estrutura de diretórios do sistema operacional Linux possui uma organização padronizada e adotada por todas as distribuições. Considerando que um novo usuário de nome superior seja criado no Linux, o diretório do usuário será criado em:

* **A)** /root.
* **B)** /home.
* **C)** /usr/local.
* **D)** /tmp.
* **E)** /usr.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "/root". De acordo com a teoria estudada em *2.3 Exposição de Portas e Segurança: EXPOSE vs. Publicação no Host e Diretiva USER*, diretiva `USER` e Segurança (Princípio do Menor Privilégio): Por padrão, os processos dentro de um contêiner rodam como o usuário `root` (UID 0). Caso a aplicação sofra um ataque de *container breakout*, o invasor pode comprometer o host.
> - **B)** **Correta.** Conforme fundamentado na seção *1. Linux Namespaces (Isolamento de Visibilidade)* deste guia, `user` (User IDs): Mapeia UIDs e GIDs entre o contêiner e o host, viabilizando que um processo execute como `root` (UID 0) dentro do contêiner, mas seja mapeado para um usuário não privilegiado comum (ex.: UID 10001) no sistema hospedeiro. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT-16/2014) ao estabelecer que "/home".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "/usr/local". De acordo com a teoria estudada em *3.2 Comparativo: Named Volumes vs. Bind Mounts vs. tmpfs Mounts*, bind Mounts: Qualquer caminho arbitrário absoluto do host (ex.: `/opt/app` ou `C:\projetos`) — NÃO (depende da estrutura física e de permissões do host) — Desenvolvimento local.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "/tmp". De acordo com a teoria estudada em *1.4 Sistema de Arquivos em Camadas (Overlay2 UnionFS) e Copy-on-Write (CoW)*, unionFS / Overlay2: Driver de armazenamento padrão que sobrepõe as múltiplas camadas de diretórios, apresentando-as ao contêiner como um sistema de arquivos unificado e coeso.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "/usr". De acordo com a teoria estudada em *1.4 Sistema de Arquivos em Camadas (Overlay2 UnionFS) e Copy-on-Write (CoW)*, se o contêiner precisa alterar um arquivo que pertence a uma camada inferior de somente leitura, o driver copia esse arquivo para a camada superior gravável e aplica a alteração ali.
>
> **Gabarito: B**

---

### Teste 201
**(FGV – TRF-1 – Analista Judiciario Area Apoio Especializado Especialidade Tecnologia da Informacao – 2024)**
O analista Frederico configurou uma instalação personalizada do Red Hat Enterprise Linux (RHEL) para servidores Intel 64-bit baseados em BIOS. Frederico utilizou ainda o RHEL Kickstart para automatizar a instalação personalizada. A variante do Kickstart utilizada foi a que automatiza completamente o processo de instalação, a partir de um boot loader via rede adequadamente configurado. Para permitir o início automático da instalação Kickstart pelos servidores, Frederico configurou um servidor de boot:

* **A)** ISO;
* **B)** PXE;
* **C)** CDN;
* **D)** VNC;
* **E)** HTTP.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "ISO". De acordo com a teoria estudada em *4.1 Drivers de Rede: bridge, host, none, overlay e macvlan*, `overlay`: Driver de rede virtual distribuída para ambientes com múltiplos servidores físicos (*multi-host*). Criptografa e roteia o tráfego de contêineres entre diferentes nós, atuando como alicerce de orquestradores como o Docker Swarm.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "PXE". De acordo com a teoria estudada em *4.1 Drivers de Rede: bridge, host, none, overlay e macvlan*, `macvlan`: Atribui um endereço MAC físico diretamente à interface virtual do contêiner, fazendo com que ele se apresente perante a rede corporativa (switch/roteador físico) como se fosse um servidor físico independente com IP próprio na sub-rede da LAN.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "CDN". De acordo com a teoria estudada em *4.2 Resolução de Nomes por DNS Integrado em Redes Customizadas*, redes Customizadas pelo Usuário (*User-Defined Networks*): Ao criar uma rede com `docker network create minha-rede`, o Docker ativa um servidor DNS interno embutido.
> - **D)** **Correta.** Conforme fundamentado na seção *4.1 Drivers de Rede: bridge, host, none, overlay e macvlan* deste guia, `none`: Desativa compulsoriamente a conectividade de rede do contêiner. Mantém apenas a interface local de loopback (`127.0.0.1`), deixando o contêiner completamente isolado de acessos externos e de outros serviços. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRF-1/2024) ao estabelecer que "VNC".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "HTTP". De acordo com a teoria estudada em *2.1 Instruções Canônicas: FROM, WORKDIR, COPY vs. ADD, RUN, ENV vs. ARG*, `ADD <origem> <destino>`: Possui recursos extras automáticos: permite baixar arquivos remotos via URLs HTTP/HTTPS e descompacta compulsoriamente arquivos tar/gzip (`.tar`, `.tar.gz`) diretamente no destino.
>
> **Gabarito: D**

---

## 5. Orquestração Multi-Contêiner com Docker Compose

O **Docker Compose** é a ferramenta oficial do ecossistema Docker voltada para definir, versionar e gerenciar a execução de múltiplos contêineres interconectados em uma única máquina hospedeira através de arquivos declarativos YAML (`compose.yaml` ou `docker-compose.yml`).

### 5.1 Estrutura do Manifesto Compose: Services, Networks, Volumes e depends_on

O arquivo Compose estrutura a topologia de microsserviços em seções padronizadas:

```yaml
services:
  web:
    build: .
    ports:
      - "8080:80"        # Mapeamento Porta Host : Porta Contêiner
    environment:
      - DB_HOST=db
      - DB_NAME=tce_fiscal
    depends_on:
      db:
        condition: service_healthy
    networks:
      - rede-corporativa

  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: tce_fiscal
      POSTGRES_PASSWORD: senha_segura_tce
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5
    networks:
      - rede-corporativa

volumes:
  pgdata:                # Volume persistente gerenciado nomeado

networks:
  rede-corporativa:      # Rede bridge customizada com DNS interno automático
```

- **`services`:** Declara cada um dos contêineres da aplicação. Define a imagem pronta (`image:`) ou o contexto de construção local (`build:`), portas mapeadas (`ports:`), variáveis (`environment:`) e volumes acoplados.
- **`depends_on`:** Especifica a ordem de inicialização das dependências. Em sua forma moderna, permite aguardar não apenas a subida do contêiner dependente, mas a validação de que ele está funcionalmente pronto através de regras de `condition: service_healthy`.
- **`networks`:** Define as redes virtuais privativas. Todos os serviços conectados à mesma rede conseguem se comunicar apontando o tráfego diretamente para o **nome do serviço** (ex.: a aplicação web acessa o banco via `db:5432`).
- **`volumes`:** Declara os volumes gerenciados que devem sobreviver à desmontagem dos contêineres.

### 5.2 Ciclo de Vida e Comandos Operacionais da CLI

- **`docker compose up -d`:** Compila imagens pendentes, cria redes, provisiona volumes e inicia todos os serviços em segundo plano (*detached mode*).
- **`docker compose down`:** Interrompe a execução dos contêineres e remove os contêineres e as redes criadas. **Atenção:** Os dados dos volumes persistentes NÃO são apagados pelo comando padrão. Para excluir também os volumes gerenciados, deve-se explicitar a flag `-v` (`docker compose down -v`).
- **`docker compose ps`:** Lista o estado operacional dos contêineres gerenciados pelo manifesto Compose.
- **`docker compose logs -f [servico]`:** Exibe o fluxo contínuo de logs consolidados de todos os contêineres ou de um serviço específico.
- **`docker compose exec [servico] [comando]`:** Dispara a execução de um comando interativo dentro de um contêiner em execução (ex.: `docker compose exec db psql -U postgres`).

---

### Teste 202
**(CEBRASPE – TJ-RJ – Analista Judiciario Grupo Tecnologia da Informacao Analista de Infraestrutura de Tic – 2021)**
Para a conteinerização de aplicações, são necessárias tecnologias que suportem esse tipo de operação; entre elas, há tecnologias consideradas como container runtime, que são responsáveis por executar os contêineres e gerenciar as imagens dos contêineres. Uma tecnologia que é capaz de prover a capacidade de container runtime é o

* **A)** Jboss.
* **B)** Tomcat.
* **C)** Active Directory.
* **D)** Docker.
* **E)** PostgreSQL.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Jboss". De acordo com a teoria estudada em *1.3 Arquitetura do Docker Engine: Client, Daemon, containerd, runc e Registries*, registries de Imagens: Servidores centralizados de catalogação e armazenamento de imagens Docker (como Docker Hub público, AWS Elastic Container Registry - ECR, Harbor corporativo ou GitHub Packages).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Tomcat". De acordo com a teoria estudada em *5.2 Ciclo de Vida e Comandos Operacionais da CLI*, `docker compose up -d`: Compila imagens pendentes, cria redes, provisiona volumes e inicia todos os serviços em segundo plano (*detached mode*).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Active Directory". De acordo com a teoria estudada em *1.2 Primitivas Essenciais do Kernel Linux: Namespaces e Control Groups (cgroups)*, a segurança e o isolamento de um contêiner Docker não decorrem de mágica, mas do acoplamento de duas tecnologias maduras do Kernel Linux.
> - **D)** **Correta.** Conforme fundamentado na seção *5. Orquestração Multi-Contêiner com Docker Compose* deste guia, o Docker Compose é a ferramenta oficial do ecossistema Docker voltada para definir, versionar e gerenciar a execução de múltiplos contêineres interconectados em uma única máquina hospedeira através de arquivos declarativos YAML (`compose.yaml` ou `docker-compose.yml`). Dessa forma, está plenamente correta a assertiva da banca (CEBRASPE – TJ-RJ/2021) ao estabelecer que "Docker".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "PostgreSQL". De acordo com a teoria estudada em *3.2 Comparativo: Named Volumes vs. Bind Mounts vs. tmpfs Mounts*, named Volumes: `/var/lib/docker/volumes/<nome>/_data` — SIM (via comandos `docker volume create/ls/rm`) — Padrão ouro para produção e bancos de dados (PostgreSQL, MySQL, MongoDB).
>
> **Gabarito: D**

---

## 🌐 Fontes Oficiais e Referências Bibliográficas

* [Docker Official Documentation - Dockerfile Reference](https://docs.docker.com/reference/dockerfile/) - Instruções canônicas: FROM, RUN, COPY, ADD, CMD, ENTRYPOINT, EXPOSE e USER.
* [Docker Official Documentation - Multi-stage Builds](https://docs.docker.com/build/building/multi-stage/) - Redução do tamanho de imagens, segregação de compilação e segurança de artefatos.
* [Docker Official Documentation - Storage and Volumes](https://docs.docker.com/engine/storage/volumes/) - Persistência de dados: Volumes nomeados, Bind Mounts e tmpfs.
* [Docker Official Documentation - Compose Application Model](https://docs.docker.com/compose/intro/compose-application-model/) - Orquestração de múltiplos contêineres locais, redes bridge e dependências de serviços.
* MOUAT, Adrian. **Usando Docker: Desenvolvendo e Implantando Software com Contêineres**. São Paulo: Novatec, 2016. (Cap. 3 a 5 - Construindo Imagens e Redes com Docker).
* TURNBULL, James. **The Docker Book: Containerization is the new virtualization**. 2. ed. James Turnbull, 2017. (Cap. 4 - Gerenciando Contêineres e Volumes).
* MORRIS, Kief. **Infraestrutura como Código: Gerenciamento Dinâmico de Sistemas na Era da Nuvem**. 2. ed. São Paulo: Novatec, 2021. (Cap. 8 - Imutabilidade e Contêineres).
