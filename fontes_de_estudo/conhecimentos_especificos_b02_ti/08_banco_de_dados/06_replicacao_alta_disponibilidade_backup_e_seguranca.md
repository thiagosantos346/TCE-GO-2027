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
- [1. Replicação de Dados e Topologias Distribuídas](#1-replicacao-de-dados-e-topologias-distribuidas)
    - [1.1 Replicação Síncrona vs. Assíncrona](#11-replicacao-sincrona-vs-assincrona)
    - [1.2 Topologias de Replicação: Leader-Follower vs. Multi-Master](#12-topologias-de-replicacao-leader-follower-vs-multi-master)
    - [1.3 Replicação Física vs. Replicação Lógica](#13-replicacao-fisica-vs-replicacao-logica)
- [2. Alta Disponibilidade (HA), Failover e Mitigação de Split-Brain](#2-alta-disponibilidade-ha-failover-e-mitigacao-de-split-brain)
    - [2.1 Switchover vs. Failover: Transições Planejadas e Emergenciais](#21-switchover-vs-failover-transicoes-planejadas-e-emergenciais)
    - [2.2 O Fenômeno Crítico do Split-Brain](#22-o-fenomeno-critico-do-split-brain)
    - [2.3 Estratégias de Quórum Distribuído, Árbitros e STONITH](#23-estrategias-de-quorum-distribuido-arbitros-e-stonith)
    - [2.4 Soluções de HA Corporativas: Patroni, Oracle Data Guard e RAC](#24-solucoes-de-ha-corporativas-patroni-oracle-data-guard-e-rac)
- [3. Estratégias de Backup, PITR e Métricas de Continuidade de Negócios](#3-estrategias-de-backup-pitr-e-metricas-de-continuidade-de-negocios)
    - [3.1 Backup Lógico vs. Backup Físico](#31-backup-logico-vs-backup-fisico)
    - [3.2 Tipos de Backup: Completo (Full), Diferencial e Incremental](#32-tipos-de-backup-completo-full-diferencial-e-incremental)
    - [3.3 Point-in-Time Recovery (PITR)](#33-point-in-time-recovery-pitr)
    - [3.4 Métricas Críticas: RPO vs. RTO](#34-metricas-criticas-rpo-vs-rto)
- [4. Segurança, Criptografia, Privacidade e Governança de Dados](#4-seguranca-criptografia-privacidade-e-governanca-de-dados)
    - [4.1 Criptografia em Repouso: Transparent Data Encryption (TDE)](#41-criptografia-em-repouso-transparent-data-encryption-tde)
    - [4.2 Mascaramento Dinâmico de Dados (DDM) e Privacidade (LGPD)](#42-mascaramento-dinamico-de-dados-ddm-e-privacidade-lgpd)
    - [4.3 Trilhas de Auditoria e Controle de Acesso Baseado em Papéis (RBAC)](#43-trilhas-de-auditoria-e-controle-de-acesso-baseado-em-papeis-rbac)
- [Fontes Oficiais e Referências Bibliográficas](#fontes-oficiais-e-referencias-bibliograficas)

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

---

### Questão 01
**(FCC - TRF-3ª Região - Analista Judiciário - Informática)**
Em clusters de alta disponibilidade operando com réplicas distribuídas em datacenters geograficamente separados, a ruptura física dos canais de comunicação de rede entre os nós pode ocasionar uma partição de rede. A respeito dos mecanismos de consenso utilizados para prevenir a corrupção de dados e a ocorrência de *Split-Brain*, é correto afirmar:

* **A)** O fenômeno de *Split-Brain* é naturalmente impossível em clusters compostos por exatamente 2 nós de pesos idênticos.
* **B)** Os algoritmos de consenso baseados em quórum de maioria (como Raft e Paxos) exigem que um nó ou subconjunto de nós obtenha a maioria absoluta de votos ($\lfloor N/2 \rfloor + 1$) para prosseguir com operações de escrita, forçando os nós isolados na partição minoritária a suspender gravações.
* **C)** A técnica de STONITH (*Shoot The Other Node In The Head*) consiste em promover simultaneamente todos os nós isolados a servidores mestres com o objetivo de multiplicar a capacidade de escrita.
* **D)** A ocorrência de dois nós primários concorrentes não acarreta danos à integridade do banco de dados, pois sistemas relacionais conciliam divergências automaticamente por união natural.
* **E)** Para garantir a mitigação de falhas em partições de rede, os clusters distribuídos devem ser projetados prioritariamente com um número par de servidores.

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

---

### Questão 02
**(FCC - TRT-15ª Região - Analista Judiciário - Tecnologia da Informação)**
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

---

### Questão 03
**(FCC - DPE-RS - Analista de Tecnologia da Informação)**
Às 14h35 de uma terça-feira, durante a realização de uma rotina emergencial no banco de dados de produção de um tribunal, um operador executou inadvertidamente o comando `DROP TABLE CADASTRO_SERVIDORES`. A organização adota uma política com Backup Físico Completo (*Full*) todos os domingos às 00h00, backups incrementais diários às 23h00 e mantém o arquivamento contínuo ininterrupto de todos os logs de transação (*WAL / Archived Redo Logs*).
Para reverter o banco de dados exatamente ao estado em que se encontrava às 14h34m59s (um segundo antes do comando destrutivo), minimizando a perda de transações legítimas, a estratégia técnica apropriada é:

* **A)** Restaurar o backup completo de domingo, aceitando a perda das transações confirmadas na segunda e terça-feira.
* **B)** Utilizar o mecanismo de *Point-in-Time Recovery* (PITR), restaurando a cópia física base e reaplicando sequencialmente os arquivos de log transacional arquivados até o carimbo de data e hora especificado anterior à falha.
* **C)** Executar uma rotina de Backup Lógico Frio para exportar os metadados da tabela a partir da memória do sistema operacional.
* **D)** Emitir um comando de `ROLLBACK` na sessão do usuário que executou o comando destrutivo para anular a exclusão dos dados.
* **E)** Restaurar unicamente o arquivo de backup incremental de segunda-feira, sendo tecnicamente impossível recuperar dados transacionados entre as 23h00 de segunda e as 14h35 de terça.

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

### Questão 04
**(FCC - TCE-PI - Auditor de Controle Externo - Tecnologia da Informação)**
O Plano de Continuidade de Negócios e Recuperação de Desastres de um Tribunal de Contas estabeleceu duas diretrizes mandatórias para os sistemas corporativos de auditoria:

1. Em caso de desastre físico no datacenter principal, a tolerância para descarte de dados fiscais é de **zero transações confirmadas**.
2. O tempo máximo aceitável para que a infraestrutura secundária assuma a operação e o sistema esteja plenamente restabelecido aos auditores é de **15 minutos**.

A respeito das métricas de resiliência e dos modelos de replicação envolvidos, é correto afirmar:

* **A)** A primeira diretriz define o RTO, podendo ser atendida exclusivamente por backups em fitas magnéticas semanais.
* **B)** A primeira diretriz define um RPO igual a zero, exigindo replicação síncrona de dados para o nó secundário; enquanto a segunda diretriz define um RTO de 15 minutos, demandando infraestrutura com detecção ágil e failover automatizado.
* **C)** O fenômeno de *Split-Brain* é definido formalmente como o estado no qual o RTO de um cluster supera 48 horas ininterruptas.
* **D)** A replicação puramente assíncrona garante perda zero de dados em caso de destruição repentina do nó primário, pois os dados comitados ficam congelados na rede até a confirmação da réplica.
* **E)** RPO e RTO são conceitos financeiros atrelados ao custo de licenças de software, sem relação com tempos de contingência operacional.

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

---

### Questão 05
**(FCC - TCE-RS - Auditor Público Externo - Tecnologia da Informação)**
Em conformidade com as exigências de privacidade da Lei Geral de Proteção de Dados (LGPD) e as boas práticas de segurança corporativa em órgãos públicos, a equipe de administração de banco de dados implementou duas medidas técnicas:

1. Criptografia dos blocos de dados físicos em repouso (*data-at-rest*) no disco rígido e nas fitas de backup de maneira imperceptível para as instruções SQL e aplicações conectadas.
2. Ofuscação de colunas com dados sensíveis (como números de CPF e remunerações) em tempo de execução para operadores sem permissões especiais, mantendo os registros originais intactos e inalterados no subsistema de armazenamento.

As duas abordagens de segurança correspondem, respectivamente, a:

* **A)** *Dynamic Data Masking* (DDM); e *Transparent Data Encryption* (TDE).
* **B)** *Transparent Data Encryption* (TDE); e *Dynamic Data Masking* (DDM).
* **C)** *Point-in-Time Recovery* (PITR); e Anonimização definitiva em repouso.
* **D)** Autenticação multifator por biometria; e exclusão lógica com `DELETE CASCADE`.
* **E)** *Role-Based Access Control* (RBAC); e cálculo de hash MD5 na cláusula `WHERE`.

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

## 🌐 Fontes Oficiais e Referências Bibliográficas

* [PostgreSQL 17 Official Documentation - High Availability and Replication](https://www.postgresql.org/docs/current/high-availability.html) - Replicação física via streaming, replicação lógica e failover.
* [PostgreSQL 17 Official Documentation - Backup and Restore](https://www.postgresql.org/docs/current/backup.html) - Dumps lógicos (`pg_dump`), backups físicos de base (`pg_basebackup`) e recuperação ponto no tempo (PITR).
* [PostgreSQL 17 Official Documentation - Database Security and Roles](https://www.postgresql.org/docs/current/user-manag.html) - Autenticação (`pg_hba.conf`), concessão de privilégios (GRANT/REVOKE) e isolamento de esquemas.
* [PostgreSQL 17 Official Documentation - Row Security Policies](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - Controle de acesso multinível e segurança declarativa por perfil de usuário.
* SILBERSCHATZ, Abraham; KORTH, Henry F.; SUDARSHAN, S. **Sistema de Banco de Dados**. 7. ed. Rio de Janeiro: GEN LTC, 2020. (Cap. 19 - Recuperação de Falhas; Cap. 20 - Arquiteturas de Sistemas de Banco de Dados).
* ELMASRI, Ramez; NAVATHE, Shamkant B. **Sistemas de Banco de Dados**. 7. ed. São Paulo: Pearson, 2019. (Cap. 23 - Segurança e Autorização em Bancos de Dados).
* KLEPPMANN, Martin. **Projetando Aplicações Intensivas em Dados**. São Paulo: Novatec, 2018. (Cap. 5 - Replicação Líder-Seguidor e Multi-Líder; Cap. 6 - Particionamento de Dados).
