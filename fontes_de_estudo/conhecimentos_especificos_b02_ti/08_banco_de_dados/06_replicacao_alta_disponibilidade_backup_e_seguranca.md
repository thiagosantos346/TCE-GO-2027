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
**(FCC – TRT – Analista Judiciário - Tecnologia da Informação – 2024)**
Com relação aos tipos de backup suportados pelo  SQL Server 
2016, analise as afirmativas a seguir. 
I. Um backup incremental de transações inclui todos os 
registros de log dos quais não foi feito backup de dados 
anteriores. 
II. Um backup de logs registra apenas as extensões de dados 
que foram alteradas n os grupos de arquivos desde o último 
backup, conhecido como base para o backup diferencial. 
III. Os backups de banco de dados completos representam todo 
o banco de dados quando o backup foi concluído. 
Está correto o que se afirma em

* **A)** I, apenas.
* **B)** II, apenas.
* **C)** III, apenas.
* **D)** I e II, apenas.
* **E)** II e III, apenas.

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
### Teste 290
**(FCC – TRT-15 – Analista Judiciário - Tecnologia da Informação – 2015)**
Dentre os sistemas de armazenamento de dados, conhecidos pelas siglas SAN, NAS e DAS, as grandes empresas costumam 
adotar o SAN, pois

* **A)** utiliza o esquema de armazenamento em blocos, o que lhe confere maior desempenho se comparado com o NAS.
* **B)** permite o acesso múltiplo, ou seja, por vários usuários, uma vez que é implementado com um sistema operacional 
completo.
* **C)** utiliza o esquema de transferência de arquivo, o que lhe confere facilidade de operação com diversos sistemas 
operacionais.
* **D)** é conectado diretamente ao servidor, em racks com discos, o que lhe confere maior desempenho devido à proximidade 
com o servidor.
* **E)** incorpora o recurso de espelhamento de disco, implementado em seu sistema operacional, o que lhe confere maior 
confiabilidade. 
Caderno de Prova ’B02’, Tipo 001

TRT15-An.Jud.-Téc. Informação-B02 11

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
**(FCC – TRT-13 – Analista Judiciário - Tecnologia da Informação – 2014)**
Recovery Manager

−
 RMAN é um utilitário de banco de dados que faz o 
backup
, restauração e recuperação de bancos de dados 
Oracle 11g. Este utilitário

* **A)** permite definir, para cada cópia de segurança, os valores de 
status
: iniciado, finalizado, em andamento, expirado e 
obsoleto.
* **B)** permite definir uma 
tag
 para identificar um 
backup
 como parte de um grupo de 
backups
. Todos os seus 
backups
 são 
etiquetados com uma 
tag
, exceto os incrementais.
* **C)** armazena os 
backups
 de bancos de dados como cópias de imagens (
image copies
), conjuntos de 
backup
 (
backup sets
) ou 
backups
 de arquivos de configuração (
configuration file backup
).
* **D)** mantém em um metadado o registro dos arquivos de banco de dados e 
backups
 para cada banco de dados em que 
executa operações.
* **E)** não suporta paralelismo, que é o uso de múltiplos canais e sessões de servidor para executar o trabalho de um 
backup
 ou 
a tarefa de recuperação.

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **B)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **C)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **D)** Correta. Representa com precisão a disciplina do tema e o entendimento pacificado adotado pela banca (FCC).
> - **E)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
>
> **Gabarito: D**

---
### Teste 292
**(FGV – TJ-RR – Analista Judiciário - Suporte e Infraestrutura de TI – 2024)**
O administrador de banco de dados MySQL de um certo tribunal 
precisa restaurar o banco de dados MySQL, chamado "tjdb", usando 
o arquivo de backup nomeado backup_tjdb.sql".  
Para isso ele deve acessar o usuário root, usando a senha apropriada.  
Um comando que poderia ser usado é

* **A)** mysql -u root -p tjdb > backup_tjdb.sql
* **B)** mysql -u root -p -D tjdb < backup_tjdb.sql
* **C)** mysql -u root -p -D tjdb > backup_tjdb.sql
* **D)** mysql -u root -p -h tjdb < backup_tjdb.sql
* **E)** mysql -u root -p -D tjdb backup_tjdb.sql

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
**(FGV – TJ-RR – Analista Judiciário - Governança e Gestão de TI – 2024)**
O TJ -RR realiza backups completos aos domingos e backups 
diferenciais diariamente durante a semana. Após uma falha crítica 
no sistema na sexta-feira, a equipe de TI precisa restaurar os dados 
o mais rápido possível para retomar as operações.  
Sabendo que o objetivo é minimizar o tempo de restauração, o 
seguinte procedimento melhoraria significativamente o processo de 
recuperação dos dados. Assinale-o.

* **A)** Implementar um backup diferencial adicional às quartas-feiras.
* **B)** Substituir os backups diferenciais por backups completos diários.
* **C)** Realizar backups incrementais após o backup diferencial de 
quarta-feira.
* **D)** Utilizar backups incrementais ao invés de diferenciais durante 
toda a semana.
* **E)** Alternar entre backups diferenciais e incrementais a cada dois 
dias.

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
### Teste 294
**(FGV – TJ-RR – Analista Judiciário - Governança e Gestão de TI – 2024)**
Para garantir a continuidade dos negócios e a proteçã o adequada 
dos dados, uma organização deve definir claramente os objetivos de 
RTO ( Recovery Time Objective ) e RPO ( Recovery Point Objective ). 
Esses conceitos ajudam a estabelecer estratégias eficazes de 
recuperação e minimizam o impacto de incidentes. 
Considerando a importância dos objetivos de recuperação em um 
plano de continuidade de negócios, assinale a opção que apresenta 
corretas definições para RTO e RPO.

* **A)** RTO é o intervalo máximo aceitável entre o último backup 
realizado e o momento de um inc idente, enquanto RPO é o 
tempo máximo permitido para restaurar a operação após um 
incidente.
* **B)** RTO é o tempo máximo aceitável para restaurar a operação de 
um sistema após um incidente, enquanto RPO é a quantidade 
máxima de dados que podem ser perdidos se m causar danos 
significativos aos negócios.
* **C)** RTO é a quantidade máxima de dados que podem ser perdidos 
sem impactos negativos, enquanto RPO é o tempo máximo 
permitido para a execução de testes de recuperação de 
desastres.
* **D)** RTO é o intervalo de tempo entre o último backup realizado e a 
perda de dados, enquanto RPO é o tempo máximo necessário 
para restaurar a operação após uma interrupção.
* **E)** RTO é o tempo máximo permitido para o backup de dados em 
uma organização, enquanto RPO é o período durante o qu al a 
organização deve manter um backup de dados.

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
### Teste 295
**(FGV – TRT-16 – Analista Judiciário - Tecnologia da Informação – 2022)**
Com relação aos tipos de backup suportados pelo  SQL Server 
2016, analise as afirmativas a seguir. 
I. Um backup incremental de transações inclui todos os 
registros de log dos quais não foi feito backup de dados 
anteriores. 
II. Um backup de logs registra apenas as extensões de dados 
que foram alteradas n os grupos de arquivos desde o último 
backup, conhecido como base para o backup diferencial. 
III. Os backups de banco de dados completos representam todo 
o banco de dados quando o backup foi concluído. 
Está correto o que se afirma em

* **A)** I, apenas.
* **B)** II, apenas.
* **C)** III, apenas.
* **D)** I e II, apenas.
* **E)** II e III, apenas.

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **B)** Correta. Representa com precisão a disciplina do tema e o entendimento pacificado adotado pela banca (FGV).
> - **C)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **D)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **E)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
>
> **Gabarito: B**

---
### Teste 296
**(FCC – TRT-23 – Analista Judiciário - Tecnologia da Informação – 2016)**
Um Analista digitou as instruções abaixo em uma ferramenta de backup disponível para um determinado Sistema Gerenciador 
de Banco de Dados − SGBD. 

 CONFIGURE CONTROLFILE AUTOBACKUP ON; 
 CONFIGURE RETENTION POLICY TO RECOVERY WINDOW OF 2 DAYS; 
 BACKUP INCREMENTAL LEVEL 0 DATABASE; 
 DELETE NOPROMPT OBSOLETE; 

 Trata-se da ferramenta

* **A)** SQL Backup Manager − SBM para PostgreSQL.
* **B)** Recovery Manager − RMAN para Oracle.
* **C)** Server Manager Backup − SMB para SQL Server.
* **D)** Export Logical Backup − ELB para Oracle.
* **E)** Data Pump Export − EXPDP para Oracle.

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
**(FGV – TJ-AP – Analista Judiciário - Segurança da Informação – 2023)**
O setor de Tecnologia da Informação (TI) realiza as cópias de 
segurança (backup) de acordo com as políticas de backup 
definidas para cada sistema, conforme os requisitos 
estabelecidos pelos seus gestores. A fim de agilizar a có pia dos 
dados e diminuir o tempo da janela de backup diária, o setor de 
TI implementou um tipo de backup que copia nos dias úteis 
somente os dados modificados desde o último backup.  
Essa estratégia implementa um backup:

* **A)** híbrido;
* **B)** completo;
* **C)** diferencial;
* **D)** incremental;
* **E)** em disco.

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
### Teste 298
**(FGV – TJ-AP – Analista Judiciário - Banco de Dados – 2023)**
João, administrador de banco de dados MySQL, deverá realizar, 
periodicamente, o backup lógico completo do banco de dados 
"tjap_db".   
Para isso, João deverá utilizar o comando:

* **A)** backup -u root -p tjap_db > backup.sql;
* **B)** mydump -u root -p tjap_db > backup.sql;
* **C)** mybackup -u root -p tjap_db > backup.sql;
* **D)** mysqldump -u root -p tjap_db > backup.sql;
* **E)** select * from tjap_db into outfile backup.sql; 

Tribunal de Justiça do Estado do Amapá FGV Conhecimento 

Analista Jud - Apoio Especializado - Tecnologia da Informação - Banco de Dados  Tipo 1  ̶  Branca – Página 16

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **B)** Correta. Representa com precisão a disciplina do tema e o entendimento pacificado adotado pela banca (FGV).
> - **C)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **D)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **E)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
>
> **Gabarito: B**

---
### Teste 299
**(FGV – TJ-AP – Analista Judiciário - Banco de Dados – 2023)**
Em um ambiente de Data Warehouse, a operação OLAP que fatia 
o cubo de dados, gerando um subcubo, é:

* **A)** dice;
* **B)** roll-up;
* **C)** drill-across;
* **D)** drill-down;
* **E)** rotate. 


Tribunal de Justiça do Estado do Amapá FGV Conhecimento 

Analista Jud - Apoio Especializado - Tecnologia da Informação - Banco de Dados  Tipo 1  ̶  Branca – Página 14

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
## 🌐 Fontes Oficiais e Referências Bibliográficas

* [PostgreSQL 17 Official Documentation - High Availability and Replication](https://www.postgresql.org/docs/current/high-availability.html) - Replicação física via streaming, replicação lógica e failover.
* [PostgreSQL 17 Official Documentation - Backup and Restore](https://www.postgresql.org/docs/current/backup.html) - Dumps lógicos (`pg_dump`), backups físicos de base (`pg_basebackup`) e recuperação ponto no tempo (PITR).
* [PostgreSQL 17 Official Documentation - Database Security and Roles](https://www.postgresql.org/docs/current/user-manag.html) - Autenticação (`pg_hba.conf`), concessão de privilégios (GRANT/REVOKE) e isolamento de esquemas.
* [PostgreSQL 17 Official Documentation - Row Security Policies](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - Controle de acesso multinível e segurança declarativa por perfil de usuário.
* SILBERSCHATZ, Abraham; KORTH, Henry F.; SUDARSHAN, S. **Sistema de Banco de Dados**. 7. ed. Rio de Janeiro: GEN LTC, 2020. (Cap. 19 - Recuperação de Falhas; Cap. 20 - Arquiteturas de Sistemas de Banco de Dados).
* ELMASRI, Ramez; NAVATHE, Shamkant B. **Sistemas de Banco de Dados**. 7. ed. São Paulo: Pearson, 2019. (Cap. 23 - Segurança e Autorização em Bancos de Dados).
* KLEPPMANN, Martin. **Projetando Aplicações Intensivas em Dados**. São Paulo: Novatec, 2018. (Cap. 5 - Replicação Líder-Seguidor e Multi-Líder; Cap. 6 - Particionamento de Dados).
