# 06 - Replicação, Alta Disponibilidade, Backup e Segurança
**Última Atualização:** 2026-03-31  
**Banca Foco:** FCC (Fundação Carlos Chagas)  
**Cargo:** Auditor de Controle Externo - Tecnologia da Informação  
**Status do Mapeamento:** 100% aderente ao edital TCE-GO



---


## 📌 Ementa / Itens do Edital
1. **Replicação de Dados:** Replicação síncrona vs. assíncrona (trade-offs de latência, vazão e consistência); Topologias Master-Replica (*Leader-Follower*) e Multi-Master; Replicação Física (*Streaming de WAL/Redo Logs*) vs. Replicação Lógica.
2. **Alta Disponibilidade (HA) e Resiliência:** Clusters ativo-passivo vs. ativo-ativo; Mecanismos de *Failover* e *Switchover*; Problema do *Split-Brain* e algoritmos de consenso e quórum (Raft, Paxos, nós testemunhas e *STONITH/Fencing*); Ferramentas de mercado (Patroni, Oracle Data Guard e RAC).
3. **Estratégias de Backup e Disaster Recovery:** Níveis de backup (Lógico vs. Físico); Tipos de backup (Completo/*Full*, Diferencial e Incremental); Complexidade de execução vs. restauração (*Restore*); *Point-in-Time Recovery* (PITR) e aplicação de logs arquivados.
4. **Métricas de Continuidade de Negócios:** RPO (*Recovery Point Objective*) e RTO (*Recovery Time Objective*).
5. **Segurança e Proteção de Dados:** Criptografia em repouso com TDE (*Transparent Data Encryption*); Criptografia em trânsito (TLS/SSL); Mascaramento Dinâmico de Dados (*Dynamic Data Masking - DDM*); Anonimização e Pseudonimização (LGPD); Trilhas de Auditoria (*Auditing*) e Controle de Acesso Baseado em Papéis (RBAC).

---

## 🧭 Sumário

1. [Replicação de Dados e Topologias Distribuídas](#1-replicacao-de-dados-e-topologias-distribuidas)
    1. [Replicação Síncrona vs. Assíncrona](#11-replicacao-sincrona-vs-assincrona)
    2. [Topologias de Replicação: Leader-Follower vs. Multi-Master](#12-topologias-de-replicacao-leader-follower-vs-multi-master)
    3. [Replicação Física vs. Replicação Lógica](#13-replicacao-fisica-vs-replicacao-logica)
    4. [Teste 289](#Teste-289)
    5. [Teste 290](#Teste-290)
2. [Alta Disponibilidade (HA), Failover e Mitigação de Split-Brain](#2-alta-disponibilidade-ha-failover-e-mitigacao-de-split-brain)
    1. [Switchover vs. Failover: Transições Planejadas e Emergenciais](#21-switchover-vs-failover-transicoes-planejadas-e-emergenciais)
    2. [O Fenômeno Crítico do Split-Brain](#22-o-fenomeno-critico-do-split-brain)
    3. [Estratégias de Quórum Distribuído, Árbitros e STONITH](#23-estrategias-de-quorum-distribuido-arbitros-e-stonith)
    4. [Soluções de HA Corporativas: Patroni, Oracle Data Guard e RAC](#24-solucoes-de-ha-corporativas-patroni-oracle-data-guard-e-rac)
    5. [Teste 291](#Teste-291)
    6. [Teste 292](#Teste-292)
3. [Estratégias de Backup, PITR e Métricas de Continuidade de Negócios](#3-estrategias-de-backup-pitr-e-metricas-de-continuidade-de-negocios)
    1. [Backup Lógico vs. Backup Físico](#31-backup-logico-vs-backup-fisico)
    2. [Tipos de Backup: Completo (Full), Diferencial e Incremental](#32-tipos-de-backup-completo-full-diferencial-e-incremental)
    3. [Point-in-Time Recovery (PITR)](#33-point-in-time-recovery-pitr)
    4. [Métricas Críticas: RPO vs. RTO](#34-metricas-criticas-rpo-vs-rto)
    5. [Teste 293](#Teste-293)
    6. [Teste 294](#Teste-294)
    7. [Teste 295](#Teste-295)
    8. [Teste 296](#Teste-296)
4. [Segurança, Criptografia, Privacidade e Governança de Dados](#4-seguranca-criptografia-privacidade-e-governanca-de-dados)
    1. [Criptografia em Repouso: Transparent Data Encryption (TDE)](#41-criptografia-em-repouso-transparent-data-encryption-tde)
    2. [Mascaramento Dinâmico de Dados (DDM) e Privacidade (LGPD)](#42-mascaramento-dinamico-de-dados-ddm-e-privacidade-lgpd)
    3. [Trilhas de Auditoria e Controle de Acesso Baseado em Papéis (RBAC)](#43-trilhas-de-auditoria-e-controle-de-acesso-baseado-em-papeis-rbac)
    4. [Teste 297](#Teste-297)
    5. [Teste 298](#Teste-298)
    6. [Teste 299](#Teste-299)
5. [🌐 Fontes Oficiais e Referências Bibliográficas](#fontes-oficiais-e-referencias-bibliograficas)

---

## 1. Replicação de Dados e Topologias Distribuídas

A replicação consiste na manutenção sincronizada de cópias de dados em múltiplos nós de computação interconectados, provendo redundância geográfica, tolerância a desastres e escalabilidade horizontal para operações de leitura.

### 1.1 Replicação Síncrona vs. Assíncrona

A sincronização entre o nó coordenador das gravações e seus nós secundários estabelece um compromisso formal entre **garantia de perda zero de dados** e **latência percebida pela aplicação**:

```
[Replicação Síncrona]
Cliente ──(1. COMMIT)──► Primário ──(2. Envia Log)──► Secundário
Cliente ◄──(4. SUCESSO)── Primário ◄──(3. ACK Log)─── Secundário
(Compromisso: RPO = 0 garantido, porém sujeito à latência de rede da réplica)

[Replicação Assíncrona]
Cliente ──(1. COMMIT)──► Primário ──(Grava Log Local)
Cliente ◄──(2. SUCESSO)── Primário
                         Primário ──(3. Envia Log em 2º plano)──► Secundário
(Compromisso: Latência mínima local, porém RPO > 0 em caso de desastre imediato)
```

| Dimensão de Análise | Replicação Síncrona (*Synchronous*) | Replicação Assíncrona (*Asynchronous*) |
| :--- | :--- | :--- |
| **Garantia de Commit** | O nó primário só devolve a confirmação de sucesso à aplicação após receber o aviso de gravação persistente (*ACK*) de ao menos uma réplica secundária. | O nó primário confirma o commit imediatamente após a persistência em seu próprio log local, sem aguardar a réplica. |
| **Perda de Dados (RPO)** | **RPO = 0** (Garantia matemática de perda zero de transações confirmadas). | **RPO > 0** (Risco de perda das transações mais recentes caso o primário sofra pane física antes da transmissão). |
| **Latência e Desempenho** | **Maior latência** por transação de escrita, diretamente dependente do tempo de ida e volta da rede (*Round-Trip Time - RTT*). | **Mínima latência** e máxima vazão de escrita local, idêntica à de um servidor autônomo. |
| **Impacto de Falhas na Rede** | Se o link de comunicação cair ou a réplica travar, as transações de escrita no nó primário podem ficar suspensas (*blocked*). | O nó primário continua processando escritas normalmente, acumulando logs para entrega posterior. |

### 1.2 Topologias de Replicação: Leader-Follower vs. Multi-Master

1. **Master-Replica / Leader-Follower (Primário-Secundário):**
    - **Estrutura:** Um único nó designado como **Primário (Líder)** tem autoridade para processar comandos de modificação DML (`INSERT`, `UPDATE`, `DELETE`) e DDL. Múltiplos nós **Secundários (Standbys / Read Replicas)** recebem o fluxo de replicação e atendem exclusivamente a consultas somente-leitura (`SELECT`).
    - **Vantagens:** Simplicidade de implementação, inexistência de conflitos de escrita concorrente e facilidade de manutenção de integridade referencial.
    - **Desvantagem:** O nó primário atua como gargalo único para a capacidade total de escrita do sistema.

2. **Multi-Master / Multi-Leader:**
    - **Estrutura:** Dois ou mais nós no cluster operam simultaneamente como primários, aceitando operações concorrentes de leitura e escrita. As mutações ocorridas em qualquer nó são propagadas bidirecionalmente para os demais parceiros do cluster.
    - **Desafio Crítico:** **Resolução de Conflitos de Escrita**. Se dois usuários alterarem a mesma coluna da mesma tupla em nós diferentes no mesmo milissegundo, o sistema deve adotar heurísticas determinísticas para desempate, tais como: *Last-Write-Wins (LWW)* baseado em carimbos de tempo sincronizados, tipos de dados livres de conflito (*CRDTs*) ou mediação por regras negociais na camada de aplicação.

### 1.3 Replicação Física vs. Replicação Lógica

* **Replicação Física (*Physical Streaming Replication*):**
    - Opera no nível mais baixo do subsistema de armazenamento, transmitindo o fluxo contínuo de registros binários dos logs transacionais (**WAL** no PostgreSQL / **Redo Logs** no Oracle).
    - A réplica secundária aplica esses blocos diretamente, constituindo um **clone exato byte a byte** do nó primário.
    - *Restrições:* Exige rigorosamente a mesma versão principal do SGBD, mesmo sistema operacional e mesma arquitetura de hardware entre os servidores. Não permite replicar tabelas selecionadas.
* **Replicação Lógica (*Logical Replication*):**
    - Utiliza o mecanismo de **decodificação lógica** para interceptar o fluxo transacional e convertê-lo em instruções lógicas discretas de manipulação de dados (eventos de inserção, alteração ou exclusão de tuplas com base na chave primária).
    - *Flexibilidade:* Permite arquiteturas do tipo *Publish/Subscribe*, replicação granular de tabelas específicas, consolidação de múltiplos bancos departamentais em um *Data Warehouse* central e replicação entre versões heterogêneas do SGBD.

---

### Teste 289
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**
Em projetos de alta disponibilidade de bancos de dados para órgãos de controle externo, a escolha entre replicação síncrona e assíncrona impacta diretamente os indicadores de continuidade de negócios e o desempenho das transações.

A respeito das características operacionais da **Replicação Síncrona**, assinale a afirmativa correta:

* **A)** A replicação síncrona garante que não haverá perda de dados em caso de desastre no nó primário ($RPO = 0$), ao custo de impor uma penalidade de latência de escrita (*write latency penalty*), visto que a transação no nó primário só recebe confirmação de `COMMIT` após os dados ou registros de log serem recebidos e confirmados por ao menos uma réplica em rede.
* **B)** A replicação síncrona reduz a latência de escrita para zero porque dispensa o envio de logs para os nós secundários.
* **C)** Em caso de lentidão severa na rede entre o nó primário e a réplica síncrona, a replicação síncrona aborta o cluster inteiro e converte o banco para somente-leitura.
* **D)** A replicação assíncrona é a única que consegue atingir matematicamente um Recovery Point Objective igual a zero ($RPO = 0$).
* **E)** O PostgreSQL não suporta replicação síncrona, operando exclusivamente em modo assíncrono não-transacional.


---

> **Comentário Detalhado:**
>
> - **A)** **CORRETA.** A **Replicação Síncrona** vincula a conclusão da transação à gravação remota:
>   - **Garantia de RPO Zero ($RPO = 0$):** Como o nó primário aguarda a confirmação de que os registros de WAL/Redo foram recebidos (e persistidos em disco, a depender do nível de sincronismo configurado) pela réplica antes de retornar sucesso ao cliente (`COMMIT`), nenhuma transação confirmada é perdida se o nó primário falhar subitamente.
>   - **Trade-off:** Cada transação de escrita sofre penalidade de latência (*Round-Trip Time - RTT* de rede entre primário e réplica), reduzindo o *throughput* de escrita caso a latência de rede seja significativa.
> - **B)** Incorreta. A replicação síncrona aumenta a latência de escrita, não a reduz.
> - **C)** Incorreta. O primário fica em espera (*wait state*) aguardando a confirmação da réplica ou pode degradar para assíncrono se configurado com *fallbacks*, mas não aborta o cluster inteiro.
> - **D)** Incorreta. A replicação assíncrona admite defasagem de replicação (*replication lag*), podendo acarretar perda de dados em falhas abruptas ($RPO > 0$).
> - **E)** Incorreta. O PostgreSQL suporta replicação síncrona nativa via parâmetro `synchronous_commit` e `synchronous_standby_names`.
> 
> **Gabarito: A**

---

### Teste 290
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**
No ecossistema PostgreSQL, administradores de banco de dados podem implementar tanto a Replicação Física por Fluxo (*Physical Streaming Replication*) quanto a Replicação Lógica (*Logical Replication*).

A respeito das distinções conceituais e operacionais entre essas duas abordagens de replicação, assinale a afirmativa correta:

* **A)** A replicação lógica exige versões idênticas do PostgreSQL e a mesma arquitetura de hardware em todos os nós, ao passo que a replicação física permite replicar dados entre sistemas operacionais e versões principais (*major versions*) diferentes.
* **B)** A replicação física transfere blocos exatos do Write-Ahead Log (WAL) byte a byte, replicando a instância inteira de modo homogêneo (todas as bases de dados e objetos), enquanto a replicação lógica opera no nível de publicação/assinatura (*publish/subscribe*), permitindo replicar seletivamente tabelas individuais e executar versões diferentes do SGBD nos nós de destino.
* **C)** A replicação física permite que as réplicas em modo *Standby* recebam operações concorrentes de escrita (`INSERT` e `UPDATE`) em tabelas de produção.
* **D)** A replicação lógica dispensa a existência de chaves primárias ou identificadores únicos nas tabelas replicadas.
* **E)** A replicação física é executada exclusivamente através de comandos DDL enviados em formato texto via protocolo HTTP.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A regra é o exato inverso: a replicação **física** exige idêntica versão principal do PostgreSQL e mesma arquitetura binária, enquanto a replicação **lógica** suporta versões diferentes e sistemas operacionais distintos (sendo excelente para atualizações sem *downtime*).
> - **B)** **CORRETA.** Distinção arquitetural rigorosa:
>   - **Replicação Física (Streaming Replication):** Opera no nível binário de baixo nível do WAL. É tudo-ou-nada: a réplica é um espelho físico exato de toda a instância do cluster (todos os databases, tabelas e catálogos). A réplica opera obrigatoriamente em modo *Hot Standby* (somente leitura).
>   - **Replicação Lógica:** Baseia-se na decodificação lógica do WAL em eventos de modificação de dados (DML). Opera sob o paradigma de Publicação e Assinatura (*Pub/Sub*), permitindo replicar tabelas específicas, filtrar linhas/colunas, integrar dados com data warehouses e manter tabelas locais adicionais com escrita no nó assinante.
> - **C)** Incorreta. Instâncias em replicação física operam em modo somente-leitura (*read-only*).
> - **D)** Incorreta. A replicação lógica requer que as tabelas possuam `REPLICA IDENTITY` (chave primária ou índice único) para aplicar operações de `UPDATE` e `DELETE` na réplica.
> - **E)** Incorreta. A replicação física transfere streams de registros WAL via conexão de streaming TCP proprietária do PostgreSQL.
> 
> **Gabarito: B**

---

## 2. Alta Disponibilidade (HA), Failover e Mitigação de Split-Brain

A Alta Disponibilidade (*High Availability - HA*) congrega práticas, redundâncias e automações destinadas a assegurar que o serviço de banco de dados permaneça operacional e acessível, mesmo na ocorrência de desastres ou falhas locais.

### 2.1 Switchover vs. Failover: Transições Planejadas e Emergenciais

* **Switchover (Transição Planejada):**
    - Evento controlado e agendado pela equipe de infraestrutura (ex.: manutenção de hardware ou atualização de patch do sistema operacional).
    - O nó primário transfere a liderança para o nó secundário de forma graciosa e sem nenhuma perda de dados: as transações ativas são finalizadas, os logs são drenados e as funções dos nós são invertidas de forma ordenada.
* **Failover (Transição Emergencial Não-Planejada):**
    - Evento emergencial disparado de forma automatizada ou sob intervenção humana quando o nó primário colapsa repentinamente (falha de energia, quebra de hardware ou travamento do sistema operacional).
    - Uma das réplicas secundárias é promovida (*promoted*) a nova líder e assume o tráfego de escritas.

### 2.2 O Fenômeno Crítico do Split-Brain

O **Split-Brain (Cérebro Dividido)** é a falha arquitetural mais destrutiva que pode ocorrer em um cluster de banco de dados distribuído:

- Ocorre quando uma falha ou partição no link de rede interrompe a comunicação entre dois datacenters ou servidores perfeitamente saudáveis.
- Como o canal de batimento cardíaco (*heartbeat*) cessa, o nó secundário deduz erroneamente que o nó primário faleceu e se autopromove a Primário.
- Enquanto isso, o nó primário original continua ativo e atendendo clientes locais.
- **Resultado Catastrófico:** O cluster passa a ter **dois nós primários simultâneos**. Clientes e microsserviços passam a gravar transações mutuamente exclusivas e conflitantes em cada um deles, provocando bifurcação divergente e corrupção irreversível da integridade dos dados (*data divergence*).

### 2.3 Estratégias de Quórum Distribuído, Árbitros e STONITH

Para erradicar a ocorrência de split-brain, os sistemas modernos de HA utilizam salvaguardas formais:

```
+────────────────────────────────────────────────────────────────────────────+
|                    CLUSTER DE 3 NÓS (QUÓRUM DE MAIORIA)                    |
|                                                                            |
|   Datacenter A (Partição Maioritária)       Datacenter B (Isolado)         |
|   ┌───────────────┐     ┌───────────────┐      X   ┌───────────────┐       |
|   │     Nó 1      │◄───►│     Nó 2      │  ◄───X──►│     Nó 3      │       |
|   │ (Líder Ativo) │     │   (Standby)   │      X   │  (Rejeitado)  │       |
|   └───────────────┘     └───────────────┘          └───────────────┘       |
|            \                   /                                           |
|             \                 /                                            |
|              ▼               ▼                                             |
|        [ Quórum = 2 de 3 votos (66%) ]            [ Apenas 1 voto (33%) ]  |
|           AUTORIZADO A PROCESSAR                    ENTRA EM MODO LEITURA  |
+────────────────────────────────────────────────────────────────────────────+
```

1. **Quórum Distribuído de Maioria Absoluta:**
    - Baseado em algoritmos de consenso formal como **Raft** ou **Paxos**.
    - Para que um nó possa ser eleito líder ou continue a processar comandos de escrita, ele deve manter contato simultâneo com a **maioria estrita** dos nós do cluster:
     $$\text{Quórum Mínimo} = \left\lfloor \frac{N}{2} \right\rfloor + 1$$
    - Em caso de partição binária de rede, o subconjunto de nós que mantiver a maioria prossegue operando; o nó isolado que ficar na minoria renuncia ao papel de líder e suspende as escritas.
    - **Regra de Ouro:** Clusters de alta disponibilidade devem ser configurados preferencialmente com um **número ímpar de nós** (3, 5, 7) para evitar cenários de empate em partições binárias (50%/50%).

2. **Nó Testemunha (*Witness / Arbiter*):**
    - Em arquiteturas com apenas dois servidores de dados, adiciona-se um terceiro nó leve (que não armazena dados de tabelas) cuja função exclusiva é emitir voto para desempatar eleições e garantir o quórum da maioria.

3. **STONITH (*Shoot The Other Node In The Head* / Fencing):**
    - Mecanismo agressivo de isolamento por hardware. Antes que um nó secundário tome a posse do armazenamento compartilhado e seja promovido a novo primário, ele aciona comandos remotos via interface de gerenciamento de hardware fora de banda (IPMI, iLO, BMC ou tomadas elétricas inteligentes) para **cortar compulsoriamente a energia física do antigo primário**, assegurando que ele jamais voltará a gravar dados simultaneamente.

### 2.4 Soluções de HA Corporativas: Patroni, Oracle Data Guard e RAC

* **Patroni (com etcd ou Consul):**
    - Solução de código aberto padrão de fato para gerenciamento de HA em **PostgreSQL**.
    - Utiliza uma camada de armazenamento de chave-valor distribuída com algoritmo Raft (**etcd**) para armazenar o estado do cluster (*DCS - Distributed Consensus Store*), garantindo eleições transparentes de líder, failover automatizado e proteção matemática estrita contra split-brain.
* **Oracle Data Guard:**
    - Solução corporativa de replicação e recuperação de desastres do Oracle Database.
    - Mantém bancos de dados em espera (*Standby Databases*) sincronizados via transporte e aplicação de *Redo Logs*. Emprega o *Fast-Start Failover (FSFO)* com um processo observador (*Observer*) para automatizar a promoção do standby em falhas.
* **Oracle RAC (Real Application Clusters):**
    - Arquitetura de cluster **ativo-ativo com armazenamento compartilhado (*Shared-Disk Architecture*)**.
    - Múltiplas instâncias Oracle independentes executadas em servidores distintos acessam e modificam simultaneamente a mesma base de dados persistida em uma SAN/Storage unificado via Oracle ASM, sincronizando blocos de dados em memória através do barramento ultrarrápido *Cache Fusion*.

---

### Teste 291
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**
Em ambientes de missão crítica de tribunais, a gestão de continuidade de serviços de tecnologia da informação diferencia com rigor os procedimentos de **Switchover** e **Failover**.

A respeito dessas duas operações de transição de papéis entre nós de banco de dados, assinale a afirmativa correta:

* **A)** O *Switchover* é uma transição planejada e controlada na qual o nó primário ativo transfere a liderança para uma réplica standby sincronizada sem qualquer perda de dados ($RPO = 0$).
* **B)** O *Failover* é realizado exclusivamente em janelas programadas durante os finais de semana e nunca envolve a promoção de réplicas.
* **C)** O *Switchover* acarreta necessariamente a perda irremediável de 1 hora de transações da base de dados.
* **D)** O *Failover* exige a aprovação física de três auditores em formulário impresso antes que qualquer software de monitoramento possa atuar.
* **E)** Ambos os termos são sinônimos perfeitos e referem-se à restauração de backups em fitas magnéticas.


---

> **Comentário Detalhado:**
>
> - **A)** **CORRETA.** Na engenharia de alta disponibilidade (HA):
>   - **Switchover:** É uma transição **planejada e preventiva**. O administrador coloca o nó primário em modo gracioso, garante a descarga de todos os logs para a réplica, inverte as funções (o primário torna-se secundário e a réplica é promovida a primário) com **perda zero de dados ($RPO = 0$)** e mínimo impacto na disponibilidade. É utilizado para aplicação de patches de SO, upgrades de hardware e manutenção periódica.
>   - **Failover:** É uma recuperação **emergencial não-planejada**, provocada por falha catastrófica (queda de energia, falha de hardware, pânico de kernel) no primário. A réplica é promovida para assumir o tráfego. Pode ocorrer de forma automática (via orquestradores como Patroni) ou manual, podendo incorrer em perda de dados caso a replicação fosse assíncrona.
> - **B)** Incorreta. Failover é uma ação emergencial em resposta a falhas.
> - **C)** Incorreta. Switchover é gracioso e planejado, garantindo $RPO = 0$.
> - **D)** Incorreta. Em clusters modernos de alta disponibilidade, o failover pode ser automatizado por consenso distribuído (etcd/Consul).
> - **E)** Incorreta. São conceitos de transição operacional em tempo de execução, completamente distintos de restauração de fitas.
> 
> **Gabarito: A**

---

### Teste 292
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**
Em clusters de alta disponibilidade operando com réplicas distribuídas em datacenters geograficamente separados, a ruptura física dos canais de comunicação de rede entre os nós pode ocasionar uma partição de rede. A respeito dos mecanismos de consenso utilizados para prevenir a corrupção de dados e a ocorrência de *Split-Brain*, é correto afirmar:

* **A)** O fenômeno de *Split-Brain* é naturalmente impossível em clusters compostos por exatamente 2 nós de pesos idênticos.
* **B)** Os algoritmos de consenso baseados em quórum de maioria (como Raft e Paxos) exigem que um nó ou subconjunto de nós obtenha a maioria absoluta de votos ($\lfloor N/2 \rfloor + 1$) para prosseguir com operações de escrita, forçando os nós isolados na partição minoritária a suspender gravações.
* **C)** A técnica de STONITH (*Shoot The Other Node In The Head*) consiste em promover simultaneamente todos os nós isolados a servidores mestres com o objetivo de multiplicar a capacidade de escrita.
* **D)** A ocorrência de dois nós primários concorrentes não acarreta danos à integridade do banco de dados, pois sistemas relacionais conciliam divergências automaticamente por união natural.
* **E)** Para garantir a mitigação de falhas em partições de rede, os clusters distribuídos devem ser projetados prioritariamente com um número par de servidores.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Clusters de 2 nós com pesos iguais são os mais suscetíveis ao *Split-Brain*, pois em caso de partição cada nó enxerga 50% dos votos (1 de 2), não atingindo a maioria estrita sem um árbitro externo (*witness*).
> - **B)** **Correta.** Os algoritmos de consenso e quórum (Raft, Paxos) exigem a conquista da **maioria absoluta estrita** ($\lfloor N/2 \rfloor + 1$). Se um cluster de 3 nós sofrer partição binária dividindo-se em [2 nós] e [1 nó], a partição maior detém o quórum ($2 > 1.5$) e continua processando gravações, enquanto o nó minoritário isolado suspende as alterações para resguardar a integridade global da base.
> - **C)** Incorreta. O STONITH é uma técnica drástica de isolamento (*fencing*) de hardware que desliga eletricamente pela força o nó suspeito via comandos de gerenciamento de rede (IPMI/iLO).
> - **D)** Incorreta. O *Split-Brain* é um evento gravíssimo que gera divergência irreparável de dados (*data divergence*), tornando impossível a reconciliação automática.
> - **E)** Incorreta. Recomenda-se projetar clusters de consenso com número **ímpar** de nós (3, 5, 7) para evitar cenários de empate em partições simétricas.
> 
> **Gabarito: B**

---

## 3. Estratégias de Backup, PITR e Métricas de Continuidade de Negócios

O plano de recuperação de desastres (*Disaster Recovery Plan*) constitui a última barreira de proteção do patrimônio informacional do Tribunal de Contas perante ataques de ransomware, corrupção lógica de dados ou danos físicos a datacenters.

### 3.1 Backup Lógico vs. Backup Físico

* **Backup Lógico (`pg_dump` / Oracle Data Pump `expdp`):**
    - Lê os registros das tabelas via consultas SQL e extrai a estrutura e os dados em arquivos de texto plano contendo instruções DDL/DML (`CREATE TABLE`, `INSERT`) ou em formatos proprietários compactados.
    - *Vantagens:* Portabilidade total entre sistemas operacionais heterogêneos, facilidade de restauração de tabelas avulsas e inspeção textual legível.
    - *Desvantagens:* Processamento computacional pesado de CPU e I/O, lentidão extrema em bases volumosas e incompatibilidade total com rotinas contínuas de recuperação pontual (PITR).
* **Backup Físico (`pg_basebackup` / Oracle RMAN):**
    - Realiza a cópia binária dos blocos de dados físicos brutos (*Datafiles*), arquivos de controle (*Control Files*) e cabeçalhos em nível de sistema de arquivos ou raw disk.
    - *Vantagens:* Altíssima velocidade de gravação e restauração, baixíssimo consumo de CPU e suporte integral a rotinas contínuas de Point-in-Time Recovery.

### 3.2 Tipos de Backup: Completo (Full), Diferencial e Incremental

A periodicidade e a combinação de técnicas definem o equilíbrio entre a **janela de execução do backup** e a **complexidade da restauração (*Restore*)**:

```
Domingo            Segunda             Terça               Quarta              Quinta (Desastre!)
  [FULL] ─────────► [INC Seg] ────────► [INC Ter] ────────► [INC Qua] ────────► 💥 FALHA!
    │                  ▲                   ▲                   ▲
    │                  │                   │                   │
    └──────────────────┴───────────────────┴───────────────────┴──► Restaurar: Full + Seg + Ter + Qua
    
  [FULL] ─────────────────────────────────────────────────────► [DIF Qua] ────► 💥 FALHA!
    │                                                              ▲
    └──────────────────────────────────────────────────────────────┴──► Restaurar: Full + DIF Qua
```

| Tipo de Backup | O que é copiado? | Janela de Backup (Tempo/Espaço) | Procedimento de Restauração (Restore) |
| :--- | :--- | :--- | :--- |
| **Completo (*Full*)** | 100% de todos os blocos de dados e estruturas do banco. | Lenta e consome o maior espaço de armazenamento. | Exige **apenas 1 arquivo**: restaura diretamente o arquivo do Full. |
| **Diferencial (*Differential*)** | Todos os blocos modificados **desde o ÚLTIMO BACKUP COMPLETO (*Full*)**. | Aumenta de tamanho a cada dia sucessivo ao longo da semana. | Exige **apenas 2 arquivos**: `Full (Dom) + Último Diferencial (Qua)`. |
| **Incremental (*Incremental*)** | Todos os blocos modificados **desde o ÚLTIMO BACKUP DE QUALQUER TIPO** (Full ou Incremental). | Extremamente rápida e consome o menor espaço diário. | Exige **toda a cadeia sequencial ininterrupta**: `Full (Dom) + Inc (Seg) + Inc (Ter) + Inc (Qua)`. |

> ⚠️ **Alerta de Prova (FCC):**
> A banca FCC explora sistematicamente os seguintes contrastes:
>
> 1. O **Backup Incremental** é o mais veloz para *fazer*, porém é o mais demorado e arriscado para *restaurar*, pois se um único arquivo intermediário da cadeia sequencial estiver corrompido, todo o processo a partir daquele dia é inviabilizado.
> 2. O **Backup Diferencial** simplifica o restore para apenas **dois passos** (`Full + Último Diferencial`), porém consome cada vez mais tempo e espaço de armazenamento à medida que os dias da semana avançam.

### 3.3 Point-in-Time Recovery (PITR)

O **PITR (Recuperação para um Ponto no Tempo)** é a tecnologia que viabiliza reverter o banco de dados para um instante cronológico exato no passado (ex.: 14:35:28), anterior a um erro humano (ex.: `DROP TABLE` ou `DELETE` em lote sem `WHERE`) ou ataque destrutivo.

A execução do PITR articula dois pilares:

1. **Restauração de um Backup Físico de Base (*Base Backup*):** Uma cópia física íntegra anterior ao evento.
2. **Reaplicação de Logs Transacionais (*Roll-Forward / Replay*):** O motor de recuperação lê sequencialmente os arquivos arquivados de log (**Archived WALs** no PostgreSQL ou **Archived Redo Logs** no Oracle) e reaplica todas as transações cronologicamente até parar **milissegundos antes** do timestamp ou número de alteração (*SCN*) do comando danoso.

### 3.4 Métricas Críticas: RPO vs. RTO

A elaboração de acordos de nível de serviço (SLA) para desastres baseia-se em duas métricas temporais consagradas:

```
[Último Ponto Válido] ◄────── RPO ──────► [MOMENTO DA FALHA] ◄────── RTO ──────► [SISTEMA RESTAURADO]
(Backup ou Réplica)                     (Pane / Desastre)                       (Disponível ao Usuário)
```

1. **RPO (Recovery Point Objective - Objetivo de Ponto de Recuperação):**
    - Mede a **tolerância máxima aceitável de perda de dados**, expressa em unidades de tempo.
    - Responde à indagação: *"Até que momento retroativo no tempo a instituição aceita perder transações comitadas?"*.
    - Exemplo: Uma política com backups diários sem arquivamento contínuo tem $RPO = 24 \text{ horas}$. Para alcançar **$RPO = 0$ (perda zero)**, é mandatório utilizar **replicação síncrona**.

2. **RTO (Recovery Time Objective - Objetivo de Tempo de Recuperação):**
    - Mede o **tempo máximo aceitável de paralisação** do sistema até que ele retorne à plena operacionalidade.
    - Responde à indagação: *"Por quanto tempo a instituição aguenta manter o sistema fora do ar até a recuperação?"*.
    - Exemplo: Um $RTO$ estrito de poucos segundos ou minutos exige infraestruturas de clustering de alta disponibilidade com *failover* automatizado.

---

### Teste 293
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**
A equipe de infraestrutura de dados de um tribunal adota a seguinte política semanal de cópias de segurança:

- **Domingo às 01h00:** Backup Físico Completo (*Full*).
- **Segunda a Sábado às 23h00:** Backups diários.

Na quinta-feira pela manhã, os discos do subsistema de armazenamento sofreram danos irreparáveis, exigindo a reconstrução total da base de dados.
Sobre os procedimentos técnicos de restauração (*Restore*) na quinta-feira, é correto afirmar:

* **A)** Caso a política utilize backups **diferenciais**, a restauração exigirá o backup *Full* de domingo e exclusivamente o arquivo de backup *Diferencial* de quarta-feira.
* **B)** Caso a política utilize backups **incrementais**, a restauração exigirá apenas o backup *Full* de domingo e o backup *Incremental* de quarta-feira, descartando os dias intermediários.
* **C)** O backup diferencial copia apenas os blocos modificados nas últimas 24 horas, exigindo mais passos na restauração do que o backup incremental.
* **D)** O backup incremental copia todos os dados alterados desde o último backup completo de domingo.
* **E)** A rotina noturna de backup incremental consome progressivamente mais tempo de execução e espaço em disco a cada dia sucessivo do que a rotina diferencial.


---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** O backup **Diferencial** armazena cumulativamente todos os blocos de dados alterados **desde o último backup COMPLETO (*Full*)**. Dessa forma, o arquivo diferencial gerado na noite de quarta-feira já consolida todas as modificações de segunda, terça e quarta. Para restaurar o banco na quinta-feira de manhã, são necessários exatamente **dois arquivos**: o *Full* de domingo + o *Diferencial* de quarta-feira.
> - **B)** Incorreta. O backup **Incremental** grava unicamente o delta ocorrido em relação ao backup anterior (seja full ou incremental). Para restaurar a base na quinta-feira via incremental, é mandatório aplicar **toda a cadeia sequencial**: `Full (Domingo) + Inc (Segunda) + Inc (Terça) + Inc (Quarta)`.
> - **C)** Incorreta. O backup diferencial consolida desde o último Full; sua restauração é mais ágil porque envolve apenas dois arquivos.
> - **D)** Incorreta. Quem copia desde o último backup completo de domingo é o backup **diferencial**, e não o incremental.
> - **E)** Incorreta. O backup incremental é compacto e lida apenas com o delta do último dia; quem cresce sucessivamente a cada dia da semana é o backup diferencial.
> 
> **Gabarito: A**

---

### Teste 294
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**
Para mitigar o risco de perda de dados e estabelecer janelas eficientes de cópia de segurança em uma instituição pública com 10 Terabytes de dados, a equipe de TI avaliou as estratégias de backup: Completo (*Full*), Diferencial e Incremental.

Considere a seguinte política semanal: no domingo à meia-noite é executado um Backup Full. De segunda a sábado à meia-noite, são executadas cópias auxiliares. Na quinta-feira às 10h da manhã ocorreu uma quebra física irreversível no subsistema de armazenamento primário.

A respeito do tempo de execução, consumo de armazenamento e processo de recuperação dessa base, assinale a afirmativa correta:

* **A)** Se a política adotada for de Backup Incremental, a restauração da base exigirá exclusivamente a aplicação do Backup Incremental de quarta-feira, sendo dispensável o Backup Full de domingo.
* **B)** Se a política adotada for de Backup Diferencial, a restauração da base até o estado da noite de quarta-feira exigirá apenas o Backup Full de domingo e o Backup Diferencial de quarta-feira.
* **C)** O Backup Incremental copia todas as modificações ocorridas desde o último Backup Full, tornando o seu tamanho crescente a cada dia da semana.
* **D)** O Backup Full é o mais rápido de todos para ser gerado diariamente, consumindo menos espaço em disco do que backups incrementais.
* **E)** O Backup Diferencial copia apenas as alterações ocorridas desde o último backup diferencial, exigindo a restauração de todos os arquivos diários da semana.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O Backup Incremental grava apenas as alterações ocorridas desde o backup anterior (seja ele full ou incremental). Para restaurar na quinta-feira, seriam necessários: Full de domingo + Incremental de segunda + Incremental de terça + Incremental de quarta.
> - **B)** **CORRETA.** A mecânica dos tipos de backup é canônica em concursos de TI:
>   - **Backup Full:** Cópia completa de todos os blocos/dados da base.
>   - **Backup Diferencial:** Copia todos os dados que foram modificados **desde o último Backup Full**. Consequentemente, o diferencial de quarta-feira já engloba todas as alterações de segunda, terça e quarta. O processo de restauração é mais simples e veloz: basta restaurar o **Full de domingo + o Diferencial mais recente (quarta-feira)**.
>   - **Trade-off:** O diferencial é mais lento para gerar ao longo da semana do que o incremental (pois seu tamanho cresce a cada dia), mas proporciona um tempo de recuperação (*RTO*) mais curto e menor risco de falha na cadeia de restauração.
> - **C)** Incorreta. Quem copia desde o último Full é o Diferencial; o Incremental copia desde o último backup qualquer.
> - **D)** Incorreta. O Backup Full é o mais demorado e o que consome maior volume de armazenamento.
> - **E)** Incorreta. A assertiva descreveu o funcionamento do Backup Incremental, não do Diferencial.
> 
> **Gabarito: B**

---

### Teste 295
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**
Às 14h35 de uma terça-feira, durante a realização de uma rotina emergencial no banco de dados de produção de um tribunal, um operador executou inadvertidamente o comando `DROP TABLE CADASTRO_SERVIDORES`. A organização adota uma política com Backup Físico Completo (*Full*) todos os domingos às 00h00, backups incrementais diários às 23h00 e mantém o arquivamento contínuo ininterrupto de todos os logs de transação (*WAL / Archived Redo Logs*).
Para reverter o banco de dados exatamente ao estado em que se encontrava às 14h34m59s (um segundo antes do comando destrutivo), minimizando a perda de transações legítimas, a estratégia técnica apropriada é:

* **A)** Restaurar o backup completo de domingo, aceitando a perda das transações confirmadas na segunda e terça-feira.
* **B)** Utilizar o mecanismo de *Point-in-Time Recovery* (PITR), restaurando a cópia física base e reaplicando sequencialmente os arquivos de log transacional arquivados até o carimbo de data e hora especificado anterior à falha.
* **C)** Executar uma rotina de Backup Lógico Frio para exportar os metadados da tabela a partir da memória do sistema operacional.
* **D)** Emitir um comando de `ROLLBACK` na sessão do usuário que executou o comando destrutivo para anular a exclusão dos dados.
* **E)** Restaurar unicamente o arquivo de backup incremental de segunda-feira, sendo tecnicamente impossível recuperar dados transacionados entre as 23h00 de segunda e as 14h35 de terça.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Restaurar unicamente o backup de domingo descartaria dois dias completos de transações legítimas comitadas, contrariando as boas práticas de recuperação de desastres.
> - **B)** **Correta.** O **Point-in-Time Recovery (PITR)** é a técnica padrão que combina a restauração de um backup físico de base com o reaproveitamento sequencial (*roll-forward*) dos arquivos arquivados de log de transação (WAL/Redo Logs) até atingir o timestamp exato (`14:34:59`), cessando a recuperação milissegundos antes da execução do comando destrutivo `DROP TABLE`.
> - **C)** Incorreta. Backups lógicos não interagem com fluxos temporais contínuos de logs transacionais para restauração de segundo em segundo.
> - **D)** Incorreta. Comandos DDL alteram diretamente os metadados do catálogo de dados e geram commits implícitos na imensa maioria dos SGBDs, não podendo ser revertidos por simples `ROLLBACK` de sessão.
> - **E)** Incorreta. O arquivamento ininterrupto de logs transacionais preserva todas as transações comitadas da terça-feira até o momento da falha.
> 
> **Gabarito: B**

---

### Teste 296
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**
O Plano de Continuidade de Negócios e Recuperação de Desastres de um Tribunal de Contas estabeleceu duas diretrizes mandatórias para os sistemas corporativos de auditoria:

1. Em caso de desastre físico no datacenter principal, a tolerância para descarte de dados fiscais é de **zero transações confirmadas**.
2. O tempo máximo aceitável para que a infraestrutura secundária assuma a operação e o sistema esteja plenamente restabelecido aos auditores é de **15 minutos**.

A respeito das métricas de resiliência e dos modelos de replicação envolvidos, é correto afirmar:

* **A)** A primeira diretriz define o RTO, podendo ser atendida exclusivamente por backups em fitas magnéticas semanais.
* **B)** A primeira diretriz define um RPO igual a zero, exigindo replicação síncrona de dados para o nó secundário; enquanto a segunda diretriz define um RTO de 15 minutos, demandando infraestrutura com detecção ágil e failover automatizado.
* **C)** O fenômeno de *Split-Brain* é definido formalmente como o estado no qual o RTO de um cluster supera 48 horas ininterruptas.
* **D)** A replicação puramente assíncrona garante perda zero de dados em caso de destruição repentina do nó primário, pois os dados comitados ficam congelados na rede até a confirmação da réplica.
* **E)** RPO e RTO são conceitos financeiros atrelados ao custo de licenças de software, sem relação com tempos de contingência operacional.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A primeira diretriz trata de limite de perda de dados no tempo (**RPO**), e não de tempo de restauração do serviço (**RTO**). Ademais, fitas semanais produzem perdas de vários dias.
> - **B)** **Correta.** 
>     - O **RPO (*Recovery Point Objective*)** define o volume aceitável de dados perdidos expresso em tempo retroativo. Exigir *zero transações confirmadas* significa **$RPO = 0$**, o que demanda compulsoriamente a **Replicação Síncrona**.
>     - O **RTO (*Recovery Time Objective*)** define o prazo máximo para colocar o sistema em operação após a ocorrência do desastre. O intervalo de 15 minutos demanda arquitetura de alta disponibilidade com monitoramento de batimento cardíaco (*heartbeat*) e rotinas de **failover** rápidas ou automatizadas.
> - **C)** Incorreta. *Split-Brain* é a anomalia grave em que dois nós do cluster assumem a função de nó primário simultaneamente em decorrência de quebra no link de comunicação; não se relaciona com uma métrica de 48 horas.
> - **D)** Incorreta. Na replicação assíncrona, o nó primário confirma o commit antes de transmitir o dado à réplica; em falha abrupta, transações em trânsito são irremediavelmente perdidas ($RPO > 0$).
> - **E)** Incorreta. RPO e RTO são métricas consagradas de engenharia de software e continuidade de negócios (*Disaster Recovery*).
> 
> **Gabarito: B**

---

## 4. Segurança, Criptografia, Privacidade e Governança de Dados

A proteção de ativos de informação em tribunais de controle externo exige mecanismos em camadas (*defense-in-depth*), combinando criptografia, controle de acesso e conformidade legal com a Lei Geral de Proteção de Dados (LGPD).

### 4.1 Criptografia em Repouso: Transparent Data Encryption (TDE)

O **TDE (*Transparent Data Encryption*)** cifra os arquivos binários em repouso (*data-at-rest*) gravados no subsistema de armazenamento, abrangendo datafiles, redo logs/WALs e cópias de backup:

- **Transparência Absoluta:** O processo de criptografia e descriptografia ocorre na memória RAM pelo motor do SGBD durante as operações de I/O de blocos. **Aplicações clientes e consultas SQL não exigem nenhuma alteração de código**.
- **Algoritmos e Chaves:** Utiliza algoritmos robustos da indústria (como AES-256 e 3DES) gerenciados por uma arquitetura hierárquica de chaves (*Master Encryption Key* armazenada externamente em *Oracle Wallet*, HSM ou KMS em nuvem).
- **Finalidade:** Protege o banco caso os discos físicos, storages ou mídias de backup sejam extraviados ou roubados fisicamente.

### 4.2 Mascaramento Dinâmico de Dados (DDM) e Privacidade (LGPD)

O **Dynamic Data Masking (DDM)** intercepta as consultas SQL no momento de sua emissão e ofusca dinamicamente campos sensíveis (CPF, dados bancários, prontuários de saúde):

- **Preservação do Dado Físico:** Os dados gravados fisicamente em disco permanecem **completamente intactos, originais e íntegros**.
- **Controle por Privilégio:** Um usuário privilegiado (ex.: Auditor Fiscal) executa `SELECT cpf FROM servidor` e visualiza `123.456.789-00`; um atendente ou estagiário sem privilégios emite o mesmo comando e visualiza `***.***.789-**`.
- **Anonimização vs. Pseudonimização:**
    - *Anonimização:* Processo irreversível no qual o dado perde a possibilidade de associação com o titular (dados anonimizados não são considerados dados pessoais sob a LGPD).
    - *Pseudonimização:* O dado só pode ser associado a um titular mediante o uso de informação adicional mantida separadamente em ambiente seguro.

### 4.3 Trilhas de Auditoria e Controle de Acesso Baseado em Papéis (RBAC)

1. **Role-Based Access Control (RBAC):**
    - Os privilégios de acesso a tabelas, visões e procedimentos armazenados não são concedidos a usuários individuais, mas sim a **Papéis (*Roles*)** institucionais (ex.: `role_auditor_ti`, `role_consultor_externo`), respeitando o Princípio do Menor Privilégio (*Least Privilege*).

2. **Trilhas de Auditoria (*Database Auditing*):**
    - Registram de modo irrefutável e imutável os eventos críticos no banco: quem executou (`username`), qual máquina de origem (`ip_address`), quando (`timestamp`) e o comando SQL exato que alterou ou consultou tabelas fiscais confidenciais, viabilizando perícias judiciais e investigações de controle externo.

---

### Teste 297
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**
Em conformidade com as exigências de privacidade da Lei Geral de Proteção de Dados (LGPD) e as boas práticas de segurança corporativa em órgãos públicos, a equipe de administração de banco de dados implementou duas medidas técnicas:

1. Criptografia dos blocos de dados físicos em repouso (*data-at-rest*) no disco rígido e nas fitas de backup de maneira imperceptível para as instruções SQL e aplicações conectadas.
2. Ofuscação de colunas com dados sensíveis (como números de CPF e remunerações) em tempo de execução para operadores sem permissões especiais, mantendo os registros originais intactos e inalterados no subsistema de armazenamento.

As duas abordagens de segurança correspondem, respectivamente, a:

* **A)** *Dynamic Data Masking* (DDM); e *Transparent Data Encryption* (TDE).
* **B)** *Transparent Data Encryption* (TDE); e *Dynamic Data Masking* (DDM).
* **C)** *Point-in-Time Recovery* (PITR); e Anonimização definitiva em repouso.
* **D)** Autenticação multifator por biometria; e exclusão lógica com `DELETE CASCADE`.
* **E)** *Role-Based Access Control* (RBAC); e cálculo de hash MD5 na cláusula `WHERE`.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Houve inversão da correspondência dos conceitos apresentados.
> - **B)** **Correta.** 
>     - O item 1 descreve com precisão o **TDE (*Transparent Data Encryption*)**, funcionalidade que cifra os arquivos de dados físicos (*datafiles*), logs e backups no armazenamento persistente de forma transparente para a aplicação cliente e sem alterações no código SQL.
>     - O item 2 retrata o **Dynamic Data Masking (DDM)** (Mascaramento Dinâmico de Dados), tecnologia que intercepta a consulta SQL em tempo de execução e ofusca o dado sensível para perfis não autorizados, mantendo o dado físico armazenado na tabela rigorosamente intacto.
> - **C)** Incorreta. O PITR é uma estratégia de restauração de desastres, e a anonimização definitiva altera permanentemente o registro original no disco.
> - **D)** Incorreta. Conceitos não guardam relação técnica com a descrição do enunciado.
> - **E)** Incorreta. RBAC gerencia autorizações por papéis de usuários, e cálculos de hash irreversíveis impediriam consultas de dados originais por usuários privilegiados.
> 
> **Gabarito: B**

---

### Teste 298
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**
Com o advento da Lei Geral de Proteção de Dados Pessoais (LGPD), órgãos de auditoria pública implementaram a técnica de Mascaramento Dinâmico de Dados (*Dynamic Data Masking - DDM*) em seus sistemas gerenciadores de banco de dados.

A respeito dos princípios de funcionamento e dos benefícios de segurança proporcionados pelo DDM, assinale a afirmativa correta:

* **A)** O DDM altera permanentemente os valores gravados nas páginas físicas do disco rígido, destruindo de forma irreversível os dados cadastrais originais da base.
* **B)** O DDM atua na camada de apresentação da consulta SQL em tempo real, ofuscando campos confidenciais (como CPF, números de cartão e remunerações) com base em privilégios e papéis do usuário conectado, mantendo os dados originais integralmente intactos e inalterados no armazenamento físico em disco.
* **C)** O DDM é uma tecnologia exclusiva de criptografia assimétrica de chaves públicas do padrão RSA de 4096 bits.
* **D)** O DDM impede que auditores realizem comandos `SELECT` nas tabelas mascaradas, retornando sempre uma mensagem de erro de compilação SQL.
* **E)** O mascaramento estático e o mascaramento dinâmico são sinônimos que dependem da exclusão física da tabela via comando `DROP TABLE`.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Modificar os dados fisicamente na base destruindo os originais caracteriza sanitização/anonimização estática irreversível, e não mascaramento dinâmico.
> - **B)** **CORRETA.** O **Dynamic Data Masking (DDM)**:
>   - Opera no momento em que a consulta é processada pelo SGBD (*on-the-fly*).
>   - Com base no contexto da sessão e nas permissões (RBAC) do usuário, regras de mascaramento pré-configuradas são aplicadas ao conjunto de resultados retornado (ex.: exibir um CPF como `XXX.XXX.123-XX` ou e-mail como `a***@orgao.gov.br` para analistas sem autorização explícita).
>   - **Propriedade fundamental:** Os dados reais persistidos nas páginas de disco e nos arquivos de log (WAL/Redo) permanecem **100% autênticos e intactos**, preservando a integridade referencial e o processamento de rotinas internas autorizadas.
> - **C)** Incorreta. DDM é uma técnica de ofuscação/política de visualização baseada em funções de formatação, e não um algoritmo de criptografia assimétrica.
> - **D)** Incorreta. O comando `SELECT` executa com sucesso normal, retornando os registros com os campos especificados mascarados.
> - **E)** Incorreta. No mascaramento estático (*Static Data Masking*), cria-se uma cópia duplicada da base com dados alterados (usada para homologação/testes); no dinâmico, os dados não são duplicados.
> 
> **Gabarito: B**

---

### Teste 299
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**
A segurança da informação em bancos de dados corporativos baseia-se em princípios de defesa em profundidade, destacando-se o Controle de Acesso Baseado em Papéis (*Role-Based Access Control - RBAC*) e a geração de Trilhas de Auditoria (*Audit Trails*).

Em relação às boas práticas de governança e implementação desses controles em SGBDs, assinale a afirmativa correta:

* **A)** O princípio do privilégio mínimo (*Least Privilege*) estabelece que privilégios administrativos irrestritos (`SUPERUSER` ou `DBA`) devem ser atribuídos preventivamente a todos os usuários corporativos para evitar abertura de chamados no suporte.
* **B)** A utilização de *Roles* (Papéis) permite agrupar privilégios de acesso a objetos do banco segundo funções de negócio (ex.: `role_auditor_externo`), associando os usuários aos papéis correspondentes, o que simplifica a governança e previne privilégios residuais decorrentes de transferências de pessoal.
* **C)** Trilhas de auditoria de banco de dados devem registrar exclusivamente operações de `SELECT`, sendo proibido registrar comandos DDL como `DROP` e `ALTER TABLE` por restrições constitucionais.
* **D)** O controle de acesso discricionário (DAC) impede que o proprietário de uma tabela conceda permissões de leitura a outros usuários.
* **E)** As trilhas de auditoria devem ser salvas na mesma tabela que sofreu auditoria com acesso de exclusão irrestrito para qualquer estagiário da organização.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O Princípio do Menor Privilégio (*Least Privilege*) dita que cada usuário ou processo deve possuir apenas os privilégios estritamente necessários para o desempenho de suas atribuições legítimas.
> - **B)** **CORRETA.** O modelo **RBAC (Role-Based Access Control)** desacopla usuários de permissões diretas:
>   1. Privilégios DDL/DML são concedidos a Papéis (*Roles*), estruturados conforme perfis funcionais da organização.
>   2. Usuários são vinculados a essas *Roles*.
>   3. Quando um colaborador muda de setor ou desliga-se do órgão, revoga-se apenas a associação de seu login com o papel correspondente, garantindo controle estrito, rastreabilidade e eliminação de privilégios excessivos (*privilege creep*).
> - **C)** Incorreta. A auditoria deve registrar prioritariamente comandos DDL críticos (`CREATE`, `ALTER`, `DROP`) e manipulações em tabelas sensíveis.
> - **D)** Incorreta. No DAC (Discretionary Access Control), o proprietário do objeto tem discricionariedade justamente para conceder privilégios a outros usuários via `GRANT`.
> - **E)** Incorreta. Trilhas de auditoria exigem proteção estrita contra modificação (*WORM - Write Once, Read Many*) e segregação de funções, jamais admitindo exclusão por usuários operacionais.
> 
> **Gabarito: B**

---

## 🌐 Fontes Oficiais e Referências Bibliográficas

* [PostgreSQL 17 Official Documentation - High Availability and Replication](https://www.postgresql.org/docs/current/high-availability.html) - Replicação física via streaming, replicação lógica e failover.
* [PostgreSQL 17 Official Documentation - Backup and Restore](https://www.postgresql.org/docs/current/backup.html) - Dumps lógicos (`pg_dump`), backups físicos de base (`pg_basebackup`) e recuperação ponto no tempo (PITR).
* [PostgreSQL 17 Official Documentation - Database Security and Roles](https://www.postgresql.org/docs/current/user-manag.html) - Autenticação (`pg_hba.conf`), concessão de privilégios (GRANT/REVOKE) e isolamento de esquemas.
* [PostgreSQL 17 Official Documentation - Row Security Policies](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - Controle de acesso multinível e segurança declarativa por perfil de usuário.
* SILBERSCHATZ, Abraham; KORTH, Henry F.; SUDARSHAN, S. **Sistema de Banco de Dados**. 7. ed. Rio de Janeiro: GEN LTC, 2020. (Cap. 19 - Recuperação de Falhas; Cap. 20 - Arquiteturas de Sistemas de Banco de Dados).
* ELMASRI, Ramez; NAVATHE, Shamkant B. **Sistemas de Banco de Dados**. 7. ed. São Paulo: Pearson, 2019. (Cap. 23 - Segurança e Autorização em Bancos de Dados).
* KLEPPMANN, Martin. **Projetando Aplicações Intensivas em Dados**. São Paulo: Novatec, 2018. (Cap. 5 - Replicação Líder-Seguidor e Multi-Líder; Cap. 6 - Particionamento de Dados).
