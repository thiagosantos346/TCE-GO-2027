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
**(FCC – TRT 11ª – 2017 – Analista Judiciário - Tecnologia da Informação)**
Pode-se calcular o valor total de um sistema em Use Case Points (UCP) utilizando-se a seguinte fórmula: UCP = UUCP × TCF × ECF Um Analista afirma corretamente:

* **A)** Determinar que um dado fator ambiental (ECF) tem nível de influência alta corresponde a atribuir a ele o valor 10, indi- cando que está presente no projeto e influencia um único Use Case.
* **B)** A fim de se determinar o tempo necessário para o desenvolvimento do projeto, devem-se usar 20 horas de trabalho para cada UCP e dividir este valor por 60.
* **C)** O Peso Total Não Ajustado (Unadjusted Use Case Points-UUCP) é calculado pelo somatório entre os pesos de atores (Unadjusted Actor Weight) e os pesos de casos de uso (Unadjusted Use Case Weight).
* **D)** TCF se refere ao Fator de Complexidade de Tempo do sistema ou Time Complexity Factor.
* **E)** No caso dos fatores ambientais ou Environment and Conservation Fact (ECF), o nível de influência indica o nível de disponibilidade de cada recurso no decorrer do projeto.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Determinar que um dado fator ambiental (ECF) tem nível de influência alta corresponde a atribuir a ele o valor 10...". De acordo com a teoria estudada em *4.2 Mascaramento Dinâmico de Dados (DDM) e Privacidade (LGPD)*, *Pseudonimização:* O dado só pode ser associado a um titular mediante o uso de informação adicional mantida separadamente em ambiente seguro.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A fim de se determinar o tempo necessário para o desenvolvimento do projeto, devem-se usar 20 horas de trabalho...". De acordo com a teoria estudada em *2.4 Soluções de HA Corporativas: Patroni, Oracle Data Guard e RAC*, utiliza uma camada de armazenamento de chave-valor distribuída com algoritmo Raft (etcd) para armazenar o estado do cluster (*DCS - Distributed Consensus Store*), garantindo eleições transparentes de líder, failover automatizado e proteção matemática estrita contra split-brain.
> - **C)** **Correta.** Conforme fundamentado na seção *1.2 Topologias de Replicação: Leader-Follower vs. Multi-Master* deste guia, desvantagem: O nó primário atua como gargalo único para a capacidade total de escrita do sistema. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 11ª/2017) ao estabelecer que "O Peso Total Não Ajustado (Unadjusted Use Case Points-UUCP) é calculado pelo somatório entre os pesos de atores...".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "TCF se refere ao Fator de Complexidade de Tempo do sistema ou Time Complexity Factor". De acordo com a teoria estudada em *1.2 Topologias de Replicação: Leader-Follower vs. Multi-Master*, se dois usuários alterarem a mesma coluna da mesma tupla em nós diferentes no mesmo milissegundo, o sistema deve adotar heurísticas determinísticas para desempate, tais como: *Last-Write-Wins (LWW)* baseado em carimbos de tempo sincronizados, tipos de dados livres de conflito (*CRDTs*) ou mediação por regras negociais na camada de aplicação.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "No caso dos fatores ambientais ou Environment and Conservation Fact (ECF), o nível de influência indica o nível de...". De acordo com a teoria estudada em *3.1 Backup Lógico vs. Backup Físico*, *Vantagens:* Portabilidade total entre sistemas operacionais heterogêneos, facilidade de restauração de tabelas avulsas e inspeção textual legível.
>
> **Gabarito: C**

---

### Teste 290
**(FGV – TJ/DFT – 2022 – Analista Judiciario Suporte Em Tecnologia Da Informacao)**
No contexto do aplicativo pg_dump no PostgreSQL, analise as afirmativas a seguir. I. O acionamento do pg_dump deve ser feito no servidor onde o PostgreSQL está instalado. II. Na recuperação do backup, o banco de dados não pode existir, uma vez que é totalmente recriado. III. As informações a respeito de roles e tablespaces do banco de dados não são incluídas no backup. Está correto somente o que se afirma em:

* **A)** II;
* **B)** III;
* **C)** I e II;
* **D)** I e III;
* **E)** II e III.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "II". De acordo com a teoria estudada em *2.2 O Fenômeno Crítico do Split-Brain*, o Split-Brain (Cérebro Dividido) é a falha arquitetural mais destrutiva que pode ocorrer em um cluster de banco de dados distribuído.
> - **B)** **Correta.** Conforme fundamentado na seção *4.2 Mascaramento Dinâmico de Dados (DDM) e Privacidade (LGPD)* deste guia, *Pseudonimização:* O dado só pode ser associado a um titular mediante o uso de informação adicional mantida separadamente em ambiente seguro. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/DFT/2022) ao estabelecer que "III".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I e II". De acordo com a teoria estudada em *2.3 Estratégias de Quórum Distribuído, Árbitros e STONITH*, para que um nó possa ser eleito líder ou continue a processar comandos de escrita, ele deve manter contato simultâneo com a maioria estrita dos nós do cluster.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I e III". De acordo com a teoria estudada em *1.2 Topologias de Replicação: Leader-Follower vs. Multi-Master*, se dois usuários alterarem a mesma coluna da mesma tupla em nós diferentes no mesmo milissegundo, o sistema deve adotar heurísticas determinísticas para desempate, tais como: *Last-Write-Wins (LWW)* baseado em carimbos de tempo sincronizados, tipos de dados livres de conflito (*CRDTs*) ou mediação por regras negociais na camada de aplicação.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "II e III". De acordo com a teoria estudada em *3.3 Point-in-Time Recovery (PITR)*, o PITR (Recuperação para um Ponto no Tempo) é a tecnologia que viabiliza reverter o banco de dados para um instante cronológico exato no passado (ex.: 14:35:28), anterior a um erro humano (ex.: `DROP TABLE` ou `DELETE` em lote sem `WHERE`) ou ataque destrutivo.
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
**(FGV – TJ/DFT – 2022 – Analista Judiciario Suporte Em Tecnologia Da Informacao)**
A equipe de banco de dados (BD) necessita implementar em sua infraestrutura própria um cluster de BD com 3 nós (3 servidores físicos), os quais irão compartilhar os mesmos discos, que deverão ser apresentados para os 3 nós como raw devices para criação da base de dados. O protocolo utilizado deverá ser o Fibre Channel (FC) e será utilizado um switch com suporte ao FC para permitir que os nós acessem os discos a eles apresentados. A arquitetura de armazenamento que deve ser utilizada para atender os requisitos de armazenamento para o cluster de BD é o:

* **A)** RAID 1;
* **B)** DAS;
* **C)** NAS;
* **D)** RAID 6;
* **E)** SAN.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "RAID 1". De acordo com a teoria estudada em *2.3 Estratégias de Quórum Distribuído, Árbitros e STONITH*, para que um nó possa ser eleito líder ou continue a processar comandos de escrita, ele deve manter contato simultâneo com a maioria estrita dos nós do cluster.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "DAS". De acordo com a teoria estudada em *2.4 Soluções de HA Corporativas: Patroni, Oracle Data Guard e RAC*, arquitetura de cluster ativo-ativo com armazenamento compartilhado (*Shared-Disk Architecture*).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "NAS". De acordo com a teoria estudada em *4.1 Criptografia em Repouso: Transparent Data Encryption (TDE)*, finalidade: Protege o banco caso os discos físicos, storages ou mídias de backup sejam extraviados ou roubados fisicamente.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "RAID 6". De acordo com a teoria estudada em *2.1 Switchover vs. Failover: Transições Planejadas e Emergenciais*, evento controlado e agendado pela equipe de infraestrutura (ex.: manutenção de hardware ou atualização de patch do sistema operacional).
> - **E)** **Correta.** Conforme fundamentado na seção *2.4 Soluções de HA Corporativas: Patroni, Oracle Data Guard e RAC* deste guia, múltiplas instâncias Oracle independentes executadas em servidores distintos acessam e modificam simultaneamente a mesma base de dados persistida em uma SAN/Storage unificado via Oracle ASM, sincronizando blocos de dados em memória através do barramento ultrarrápido *Cache Fusion*. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/DFT/2022) ao estabelecer que "SAN".
>
> **Gabarito: E**

---

### Teste 292
**(FGV – TRT/13 – 2022 – Analista Judiciario Tecnologia Da Informacao)**
A infraestrutura recomendada para instalar o Rancher em um cluster Kubernetes K3 de alta disponibilidade é

* **A)** dois nós Linux, normalmente máquina virtual, e um banco de dados externo do tipo NoSQL.
* **B)** um cluster com Linux com menos dois nós ou quatro nós se Windows Server normalmente máquinas virtuais; com pelos menos 64 GB de memória RAM no provedor de infraestrutura e um banco de dados externo do tipo NoSQL.
* **C)** um cluster com Linux de dois nós normalmente máquinas virtuais; com pelos menos 48 GB de memória RAM no provedor de infraestrutura.
* **D)** dois nós Linux, normalmente máquinas virtuais; um banco de dados externo do tipo relacional, um balanceador de carga e um registro DNS.
* **E)** quatro nós Windows Server, normalmente máquinas virtuais; um banco de dados externo do tipo relacional, um balanceador de carga entre os quatro nós e dois registros DNS como redundância.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "dois nós Linux, normalmente máquina virtual, e um banco de dados externo do tipo NoSQL". De acordo com a teoria estudada em *4.3 Trilhas de Auditoria e Controle de Acesso Baseado em Papéis (RBAC)*, registram de modo irrefutável e imutável os eventos críticos no banco: quem executou (`username`), qual máquina de origem (`ip_address`), quando (`timestamp`) e o comando SQL exato que alterou ou consultou tabelas fiscais confidenciais, viabilizando perícias judiciais e investigações de controle externo.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "um cluster com Linux com menos dois nós ou quatro nós se Windows Server normalmente máquinas virtuais; com pelos...". De acordo com a teoria estudada em *2.2 O Fenômeno Crítico do Split-Brain*, o Split-Brain (Cérebro Dividido) é a falha arquitetural mais destrutiva que pode ocorrer em um cluster de banco de dados distribuído.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "um cluster com Linux de dois nós normalmente máquinas virtuais; com pelos menos 48 GB de memória RAM no provedor...". De acordo com a teoria estudada em *4.1 Criptografia em Repouso: Transparent Data Encryption (TDE)*, transparência Absoluta: O processo de criptografia e descriptografia ocorre na memória RAM pelo motor do SGBD durante as operações de I/O de blocos. Aplicações clientes e consultas SQL não exigem nenhuma alteração de código.
> - **D)** **Correta.** Conforme fundamentado na seção *2. Alta Disponibilidade (HA), Failover e Mitigação de Split-Brain* deste guia, a Alta Disponibilidade (*High Availability - HA*) congrega práticas, redundâncias e automações destinadas a assegurar que o serviço de banco de dados permaneça operacional e acessível, mesmo na ocorrência de desastres ou falhas locais. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT/13/2022) ao estabelecer que "dois nós Linux, normalmente máquinas virtuais; um banco de dados externo do tipo relacional, um balanceador de...".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "quatro nós Windows Server, normalmente máquinas virtuais; um banco de dados externo do tipo relacional, um...". De acordo com a teoria estudada em *1. Replicação de Dados e Topologias Distribuídas*, a replicação consiste na manutenção sincronizada de cópias de dados em múltiplos nós de computação interconectados, provendo redundância geográfica, tolerância a desastres e escalabilidade horizontal para operações de leitura.
>
> **Gabarito: D**

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
**(FCC – TRT 13ª – 2014 – Analista Judiciário - Tecnologia da Informação)**
Recovery Manager − RMAN é um utilitário de banco de dados que faz o backup, restauração e recuperação de bancos de dados Oracle 11g. Este utilitário

* **A)** permite definir, para cada cópia de segurança, os valores de status: iniciado, finalizado, em andamento, expirado e obsoleto.
* **B)** permite definir uma tag para identificar um backup como parte de um grupo de backups. Todos os seus backups são etiquetados com uma tag, exceto os incrementais.
* **C)** armazena os backups de bancos de dados como cópias de imagens (image copies), conjuntos de backup (backup sets) ou backups de arquivos de configuração (configuration file backup).
* **D)** mantém em um metadado o registro dos arquivos de banco de dados e backups para cada banco de dados em que executa operações.
* **E)** não suporta paralelismo, que é o uso de múltiplos canais e sessões de servidor para executar o trabalho de um backup ou a tarefa de recuperação.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "permite definir, para cada cópia de segurança, os valores de status: iniciado, finalizado, em andamento, expirado...". De acordo com a teoria estudada em *3.1 Backup Lógico vs. Backup Físico*, realiza a cópia binária dos blocos de dados físicos brutos (*Datafiles*), arquivos de controle (*Control Files*) e cabeçalhos em nível de sistema de arquivos ou raw disk.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "permite definir uma tag para identificar um backup como parte de um grupo de backups. Todos os seus backups são...". De acordo com a teoria estudada em *3.1 Backup Lógico vs. Backup Físico*, lê os registros das tabelas via consultas SQL e extrai a estrutura e os dados em arquivos de texto plano contendo instruções DDL/DML (`CREATE TABLE`, `INSERT`) ou em formatos proprietários compactados.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "armazena os backups de bancos de dados como cópias de imagens (image copies), conjuntos de backup (backup sets) ou...". De acordo com a teoria estudada em *4.1 Criptografia em Repouso: Transparent Data Encryption (TDE)*, o TDE (*Transparent Data Encryption*) cifra os arquivos binários em repouso (*data-at-rest*) gravados no subsistema de armazenamento, abrangendo datafiles, redo logs/WALs e cópias de backup.
> - **D)** **Correta.** Conforme fundamentado na seção *2.4 Soluções de HA Corporativas: Patroni, Oracle Data Guard e RAC* deste guia, mantém bancos de dados em espera (*Standby Databases*) sincronizados via transporte e aplicação de *Redo Logs*. Emprega o *Fast-Start Failover (FSFO)* com um processo observador (*Observer*) para automatizar a promoção do standby em falhas. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 13ª/2014) ao estabelecer que "mantém em um metadado o registro dos arquivos de banco de dados e backups para cada banco de dados em que executa...".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "não suporta paralelismo, que é o uso de múltiplos canais e sessões de servidor para executar o trabalho de um...". De acordo com a teoria estudada em *3.3 Point-in-Time Recovery (PITR)*, o PITR (Recuperação para um Ponto no Tempo) é a tecnologia que viabiliza reverter o banco de dados para um instante cronológico exato no passado (ex.: 14:35:28), anterior a um erro humano (ex.: `DROP TABLE` ou `DELETE` em lote sem `WHERE`) ou ataque destrutivo.
>
> **Gabarito: D**

---

### Teste 294
**(FGV – TJ/RR – 2024 – Analista Judiciario Gestao E Governanca De Tecnologia Da Informacao)**
O TJ-RR realiza backups completos aos domingos e backups diferenciais diariamente durante a semana. Após uma falha crítica no sistema na sexta-feira, a equipe de TI precisa restaurar os dados o mais rápido possível para retomar as operações. Sabendo que o objetivo é minimizar o tempo de restauração, o seguinte procedimento melhoraria significativamente o processo de recuperação dos dados. Assinale-o.

* **A)** Implementar um backup diferencial adicional às quartas-feiras.
* **B)** Substituir os backups diferenciais por backups completos diários.
* **C)** Realizar backups incrementais após o backup diferencial de quarta-feira.
* **D)** Utilizar backups incrementais ao invés de diferenciais durante toda a semana.
* **E)** Alternar entre backups diferenciais e incrementais a cada dois dias.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Implementar um backup diferencial adicional às quartas-feiras". De acordo com a teoria estudada em *3.1 Backup Lógico vs. Backup Físico*, realiza a cópia binária dos blocos de dados físicos brutos (*Datafiles*), arquivos de controle (*Control Files*) e cabeçalhos em nível de sistema de arquivos ou raw disk.
> - **B)** **Correta.** Conforme fundamentado na seção *3.4 Métricas Críticas: RPO vs. RTO* deste guia, exemplo: Uma política com backups diários sem arquivamento contínuo tem $RPO = 24 \text{ horas}$. Para alcançar $RPO = 0$ (perda zero), é mandatório utilizar replicação síncrona. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/RR/2024) ao estabelecer que "Substituir os backups diferenciais por backups completos diários".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Realizar backups incrementais após o backup diferencial de quarta-feira". De acordo com a teoria estudada em *1.1 Replicação Síncrona vs. Assíncrona*, garantia de Commit: O nó primário só devolve a confirmação de sucesso à aplicação após receber o aviso de gravação persistente (*ACK*) de ao menos uma réplica secundária. — O nó primário confirma o commit imediatamente após a persistência em seu próprio log local, sem aguardar a réplica.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Utilizar backups incrementais ao invés de diferenciais durante toda a semana". De acordo com a teoria estudada em *4.1 Criptografia em Repouso: Transparent Data Encryption (TDE)*, transparência Absoluta: O processo de criptografia e descriptografia ocorre na memória RAM pelo motor do SGBD durante as operações de I/O de blocos. Aplicações clientes e consultas SQL não exigem nenhuma alteração de código.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Alternar entre backups diferenciais e incrementais a cada dois dias". De acordo com a teoria estudada em *1.2 Topologias de Replicação: Leader-Follower vs. Multi-Master*, estrutura: Dois ou mais nós no cluster operam simultaneamente como primários, aceitando operações concorrentes de leitura e escrita. As mutações ocorridas em qualquer nó são propagadas bidirecionalmente para os demais parceiros do cluster.
>
> **Gabarito: B**

---

### Teste 295
**(CEBRASPE – TRF/6 – 2025 – Analista Judiciario Apoio Especializado Tecnologia Da Informacao)**
Denomina-se screenlogger o código malicioso projetado para monitorar o uso de teclados virtuais, capturar as regiões de tela acionadas por esses teclados e enviar as informações coletadas para terceiros. Em uma organização hipotética, a agenda semanal de backups de um sistema, que ocorrem sempre às 23 h, prevê um backup completo no sábado e backups diferenciais em todos os demais dias da semana. Um evento demandou a restauração de dados do sistema em uma quarta-feira às 15 h e as restaurações viáveis ocorram com sucesso.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Correta.** O item está **Certo**. Conforme fundamentado na seção *3.3 Point-in-Time Recovery (PITR)* deste guia, restauração de um Backup Físico de Base (*Base Backup*): Uma cópia física íntegra anterior ao evento. Dessa forma, está plenamente correta a proposição da banca (CEBRASPE – TRF/6/2025) ao afirmar que "Denomina-se screenlogger o código malicioso projetado para monitorar o uso de teclados virtuais, capturar as...".
> - **E)** **Incorreta.** A marcação como **Errado** não procede, visto que a assertiva guarda integral conformidade com a teoria estudada em *3.1 Backup Lógico vs. Backup Físico*, segundo a qual realiza a cópia binária dos blocos de dados físicos brutos (*Datafiles*), arquivos de controle (*Control Files*) e cabeçalhos em nível de sistema de arquivos ou raw disk.
>
> **Gabarito: C**

---

### Teste 296
**(CEBRASPE – TRF/6 – 2025 – Analista Judiciario Apoio Especializado Tecnologia Da Informacao)**
No caso em questão, será necessário restaurar o backup completo do sábado anterior e o backup diferencial da terça-feira, bem como que os dados produzidos pelo sistema

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Incorreta.** A marcação como **Certo** não procede, pois o enunciado apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "No caso em questão, será necessário restaurar o backup completo do sábado anterior e o backup diferencial da...". De acordo com a teoria estudada em *3.3 Point-in-Time Recovery (PITR)*, restauração de um Backup Físico de Base (*Base Backup*): Uma cópia física íntegra anterior ao evento.
> - **E)** **Correta.** O item está **Errado** (gabarito oficial: **E**). Conforme fundamentado na seção *3.1 Backup Lógico vs. Backup Físico* deste guia, realiza a cópia binária dos blocos de dados físicos brutos (*Datafiles*), arquivos de controle (*Control Files*) e cabeçalhos em nível de sistema de arquivos ou raw disk. Portanto, a assertiva examinada pela banca (CEBRASPE – TRF/6/2025) viola os preceitos técnicos do tópico.
>
> **Gabarito: E**

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
**(FCC – TRT 13ª – 2014 – Analista Judiciário - Tecnologia da Informação)**
Paulo utiliza o pg_dump do PostgreSQL para fazer cópia de segurança de um banco de dados. Normalmente faz cópias de segurança no formato tar e utiliza o pg_restore para reconstruir o banco de dados, quando necessário. O pg_restore pode selecionar o que será restaurado, ou mesmo reordenar os itens antes de restaurá-los, além de permitir salvar e restaurar objetos grandes. Certo dia Paulo fez uma cópia de segurança do banco de dados chamado trt13 para o arquivo tribunal.tar, incluindo os objetos grandes. Paulo utilizou uma instrução que permitiu a seleção manual e reordenação de itens arquivados durante a restauração, porém, a ordem relativa de itens de dados das tabelas não pôde ser alterada durante o processo de restauração. Paulo utilizou, em linha de comando, a instrução

* **A)** I e IV.
* **B)** I.
* **C)** II e IV.
* **D)** II e III.
* **E)** III.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I e IV". De acordo com a teoria estudada em *4.3 Trilhas de Auditoria e Controle de Acesso Baseado em Papéis (RBAC)*, registram de modo irrefutável e imutável os eventos críticos no banco: quem executou (`username`), qual máquina de origem (`ip_address`), quando (`timestamp`) e o comando SQL exato que alterou ou consultou tabelas fiscais confidenciais, viabilizando perícias judiciais e investigações de controle externo.
> - **B)** **Correta.** Conforme fundamentado na seção *3.3 Point-in-Time Recovery (PITR)* deste guia, reaplicação de Logs Transacionais (*Roll-Forward / Replay*): O motor de recuperação lê sequencialmente os arquivos arquivados de log (Archived WALs no PostgreSQL ou Archived Redo Logs no Oracle) e reaplica todas as transações cronologicamente até parar milissegundos antes do timestamp ou número de alteração (*SCN*) do comando danoso. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 13ª/2014) ao estabelecer que "I".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "II e IV". De acordo com a teoria estudada em *4.2 Mascaramento Dinâmico de Dados (DDM) e Privacidade (LGPD)*, *Pseudonimização:* O dado só pode ser associado a um titular mediante o uso de informação adicional mantida separadamente em ambiente seguro.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "II e III". De acordo com a teoria estudada em *4.1 Criptografia em Repouso: Transparent Data Encryption (TDE)*, transparência Absoluta: O processo de criptografia e descriptografia ocorre na memória RAM pelo motor do SGBD durante as operações de I/O de blocos. Aplicações clientes e consultas SQL não exigem nenhuma alteração de código.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "III". De acordo com a teoria estudada em *2.2 O Fenômeno Crítico do Split-Brain*, o Split-Brain (Cérebro Dividido) é a falha arquitetural mais destrutiva que pode ocorrer em um cluster de banco de dados distribuído.
>
> **Gabarito: B**

---

### Teste 298
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Ciência de Dados)**
Para garantir que operações complexas sejam executadas de maneira segura e eficiente, assegurando que o banco de dados mantenha sua integridade mesmo em situações adversas, os Sistemas de Gerenciamento de Banco de Dados (SGBD) implementam o conceito de transação. Transação é

* **A)** um conjunto de operações que são executadas sequencialmente para garantir a integridade dos dados.
* **B)** um mecanismo que permite a cópia de segurança (backup) automática dos dados do banco.
* **C)** um protocolo utilizado para distribuir os dados entre diferentes servidores de banco de dados.
* **D)** um conjunto de operações que devem ser tratadas como uma unidade atômica e indivisível.
* **E)** um método para criar índices que otimizam o acesso aos dados armazenados. Módulo III - Conhecimentos Específicos Avançados

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "um conjunto de operações que são executadas sequencialmente para garantir a integridade dos dados". De acordo com a teoria estudada em *2.3 Estratégias de Quórum Distribuído, Árbitros e STONITH*, em arquiteturas com apenas dois servidores de dados, adiciona-se um terceiro nó leve (que não armazena dados de tabelas) cuja função exclusiva é emitir voto para desempatar eleições e garantir o quórum da maioria.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "um mecanismo que permite a cópia de segurança (backup) automática dos dados do banco". De acordo com a teoria estudada em *3.1 Backup Lógico vs. Backup Físico*, realiza a cópia binária dos blocos de dados físicos brutos (*Datafiles*), arquivos de controle (*Control Files*) e cabeçalhos em nível de sistema de arquivos ou raw disk.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "um protocolo utilizado para distribuir os dados entre diferentes servidores de banco de dados". De acordo com a teoria estudada em *2.4 Soluções de HA Corporativas: Patroni, Oracle Data Guard e RAC*, múltiplas instâncias Oracle independentes executadas em servidores distintos acessam e modificam simultaneamente a mesma base de dados persistida em uma SAN/Storage unificado via Oracle ASM, sincronizando blocos de dados em memória através do barramento ultrarrápido *Cache Fusion*.
> - **D)** **Correta.** Conforme fundamentado na seção *2.3 Estratégias de Quórum Distribuído, Árbitros e STONITH* deste guia, regra de Ouro: Clusters de alta disponibilidade devem ser configurados preferencialmente com um número ímpar de nós (3, 5, 7) para evitar cenários de empate em partições binárias (50%/50%). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "um conjunto de operações que devem ser tratadas como uma unidade atômica e indivisível".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "um método para criar índices que otimizam o acesso aos dados armazenados. Módulo III - Conhecimentos Específicos...". De acordo com a teoria estudada em *4.3 Trilhas de Auditoria e Controle de Acesso Baseado em Papéis (RBAC)*, os privilégios de acesso a tabelas, visões e procedimentos armazenados não são concedidos a usuários individuais, mas sim a Papéis (*Roles*) institucionais (ex.: `role_auditor_ti`, `role_consultor_externo`), respeitando o Princípio do Menor Privilégio (*Least Privilege*).
>
> **Gabarito: D**

---

### Teste 299
**(FGV – TJ/MT – 2024 – Analista Judiciario Tecnologia Da Informacao)**
A governança de dados é um conjunto de práticas, processos e políticas que garantem a disponibilidade, integridade, segurança e usabilidade dos dados dentro de uma organização. Ela envolve a criação de regras e a definição de responsabilidades para a gestão dos dados ao longo de seu ciclo de vida. Diferentes tipos de governança de dados podem ser implementados, dependendo dos objetivos da organização e dos requisitos regulatórios. No contexto de Governança de Dados, no modelo de governança de dados colegiado

* **A)** a governança de dados é centralizada em uma única equipe responsável por todas as decisões, garantindo padronização e controle rígido.
* **B)** múltiplas áreas da organização compartilham a responsabilidade pelas decisões de dados, com a liderança de um comitê ou grupo interdepartamental.
* **C)** todas as decisões são tomadas de forma independente por cada equipe de dados, sem coordenação centralizada.
* **D)** a governança de dados é mantida por um único setor que gerencia a coleta, o armazenamento e a análise dos dados de toda a organização.
* **E)** a responsabilidade de governança é atribuída exclusivamente aos usuários finais dos dados, garantindo maior autonomia para o uso.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "a governança de dados é centralizada em uma única equipe responsável por todas as decisões, garantindo...". De acordo com a teoria estudada em *4. Segurança, Criptografia, Privacidade e Governança de Dados*, a proteção de ativos de informação em tribunais de controle externo exige mecanismos em camadas (*defense-in-depth*), combinando criptografia, controle de acesso e conformidade legal com a Lei Geral de Proteção de Dados (LGPD).
> - **B)** **Correta.** Conforme fundamentado na seção *1.2 Topologias de Replicação: Leader-Follower vs. Multi-Master* deste guia, se dois usuários alterarem a mesma coluna da mesma tupla em nós diferentes no mesmo milissegundo, o sistema deve adotar heurísticas determinísticas para desempate, tais como: *Last-Write-Wins (LWW)* baseado em carimbos de tempo sincronizados, tipos de dados livres de conflito (*CRDTs*) ou mediação por regras negociais na camada de aplicação. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/MT/2024) ao estabelecer que "múltiplas áreas da organização compartilham a responsabilidade pelas decisões de dados, com a liderança de um...".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "todas as decisões são tomadas de forma independente por cada equipe de dados, sem coordenação centralizada". De acordo com a teoria estudada em *2.1 Switchover vs. Failover: Transições Planejadas e Emergenciais*, o nó primário transfere a liderança para o nó secundário de forma graciosa e sem nenhuma perda de dados: as transações ativas são finalizadas, os logs são drenados e as funções dos nós são invertidas de forma ordenada.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "a governança de dados é mantida por um único setor que gerencia a coleta, o armazenamento e a análise dos dados de...". De acordo com a teoria estudada em *4.2 Mascaramento Dinâmico de Dados (DDM) e Privacidade (LGPD)*, *Pseudonimização:* O dado só pode ser associado a um titular mediante o uso de informação adicional mantida separadamente em ambiente seguro.
> - **E)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "a responsabilidade de governança é atribuída exclusivamente aos usuários finais dos dados, garantindo maior...". De acordo com a teoria estudada em *2.4 Soluções de HA Corporativas: Patroni, Oracle Data Guard e RAC*, múltiplas instâncias Oracle independentes executadas em servidores distintos acessam e modificam simultaneamente a mesma base de dados persistida em uma SAN/Storage unificado via Oracle ASM, sincronizando blocos de dados em memória através do barramento ultrarrápido *Cache Fusion*.
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
