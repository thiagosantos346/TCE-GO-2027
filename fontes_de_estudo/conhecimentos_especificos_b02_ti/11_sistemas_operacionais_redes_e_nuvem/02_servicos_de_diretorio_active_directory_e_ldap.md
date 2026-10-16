# 02 - Serviços de Diretório: Active Directory e LDAP

> **Matéria:** Sistemas Operacionais, Redes e Computação em Nuvem  
> **Cargo:** B02 – Técnico de Controle Externo – Especialidade: Tecnologia da Informação  
> **Arquivo:** `02_servicos_de_diretorio_active_directory_e_ldap.md`  

---

## 📌 Ementa / Itens do Edital
- Conceitos e fundamentos de Serviços de Diretório
- Protocolo LDAP (Lightweight Directory Access Protocol)
- Arquitetura do Microsoft Active Directory Domain Services (AD DS)
- Estrutura lógica e física do Active Directory
- Objetos, Contas de Usuário, Grupos e Unidades Organizacionais (OUs)
- Políticas de Grupo (GPO - Group Policy Objects)
- Autenticação Kerberos e funções FSMO

---

## 🧭 Sumário
- [1. Fundamentos de Serviços de Diretório e Protocolo LDAP](#1-fundamentos-de-servicos-de-diretorio-e-protocolo-ldap)
    - [1.1 Conceito: Diretório Hierárquico vs. Banco de Dados Relacional (RDBMS)](#11-conceito-diretorio-hierarquico-vs-banco-de-dados-relacional-rdbms)
    - [1.2 O Protocolo LDAP: Portas Padrão e Arquitetura TCP/IP](#12-o-protocolo-ldap-portas-padrao-e-arquitetura-tcpip)
    - [1.3 Formato de Nomenclatura X.500: DN, RDN, CN, OU e DC](#13-formato-de-nomenclatura-x500-dn-rdn-cn-ou-e-dc)
    - [1.4 Operações LDAP Fundamentais e Filtros de Busca](#14-operacoes-ldap-fundamentais-e-filtros-de-busca)
- [2. Arquitetura Lógica do Microsoft Active Directory (AD DS)](#2-arquitetura-logica-do-microsoft-active-directory-ad-ds)
    - [2.1 Níveis Hierárquicos: OUs, Domínios, Árvores e Floresta](#21-niveis-hierarquicos-ous-dominios-arvores-e-floresta)
    - [2.2 Tipos e Escopos de Grupos no AD DS](#22-tipos-e-escopos-de-grupos-no-ad-ds)
    - [2.3 A Estratégia Canônica de Permissões: AGDLP e AGUDLP](#23-a-estrategia-canonica-de-permissoes-agdlp-e-agudlp)
- [3. Estrutura Física e Serviços de Infraestrutura do AD DS](#3-estrutura-fisica-e-servicos-de-infraestrutura-do-ad-ds)
    - [3.1 Controladores de Domínio (DCs), ntds.dit e SYSVOL](#31-controladores-de-dominio-dcs-ntdsdit-e-sysvol)
    - [3.2 Sites, Sub-redes e Otimização de Replicação Física](#32-sites-sub-redes-e-otimizacao-de-replicacao-fisica)
    - [3.3 Catálogo Global (Global Catalog - GC)](#33-catalogo-global-global-catalog-gc)
    - [3.4 As 5 Funções Mestres de Operação Única (FSMO)](#34-as-5-funcoes-mestres-de-operacao-unica-fsmo)
- [4. Políticas de Grupo (GPO) e Autenticação Kerberos v5](#4-politicas-de-grupo-gpo-e-autenticacao-kerberos-v5)
    - [4.1 Precedência e Ordem de Processamento de GPOs (LSDOU)](#41-precedencia-e-ordem-de-processamento-de-gpos-lsdou)
    - [4.2 Bloqueio de Herança (Block Inheritance) vs. Imposição (Enforced)](#42-bloqueio-de-heranca-block-inheritance-vs-imposicao-enforced)
    - [4.3 Mecânica do Kerberos v5: KDC, AS, TGS, TGT e Bilhetes de Serviço](#43-mecanica-do-kerberos-v5-kdc-as-tgs-tgt-e-bilhetes-de-servico)
    - [4.4 Tolerância Temporal (Clock Skew) e o Papel do PDC Emulator](#44-tolerancia-temporal-clock-skew-e-o-papel-do-pdc-emulator)
- [5. Fontes Recomendadas na Internet](#5-fontes-recomendadas-na-internet)
- [6. Questões Comentadas & Exemplos Práticos](#6-questoes-comentadas-exemplos-praticos)

---

## 1. Fundamentos de Serviços de Diretório e Protocolo LDAP

### 1.1 Conceito: Diretório Hierárquico vs. Banco de Dados Relacional (RDBMS)

Um **Serviço de Diretório** é uma base de dados especializada, estruturada hierarquicamente em formato de árvore invertida (**DIT** - *Directory Information Tree*), concebida para gerenciar, pesquisar e localizar recursos de rede (usuários, grupos funcionais, computadores, servidores, políticas de segurança e certificados).

A principal distinção da arquitetura de diretórios frente aos bancos de dados relacionais convencionais (RDBMS) reside no seu perfil de carga de trabalho:

- Enquanto bancos relacionais são desenhados para suportar operações transacionais equilibradas e escritas frequentes (garantindo ACID rígido com travas complexas), os **Serviços de Diretório são otimizados para uma proporção esmagadora de LEITURAS (cerca de 95% ou mais das operações)** e poucas atualizações ou inserções.
- As buscas no diretório são extremamente rápidas e os dados são replicados entre múltiplos servidores sob o modelo de **consistência eventual** (*Multi-Master Replication*).

| Característica | Serviço de Diretório (LDAP / AD DS) | Banco de Dados Relacional (RDBMS / SQL) |
|---|---|---|
| **Proporção Leitura / Escrita** | **Altíssima leitura (95%+)** e baixa escrita. Otimizado para buscas e logons quase instantâneos. | Equilibrado entre leituras e escritas frequentes (transações OLTP complexas). |
| **Estrutura de Dados** | Hierárquica em árvore (DIT - *Directory Information Tree*). | Tabelas bidimensionais relacionais normalizadas com chaves primárias e estrangeiras. |
| **Mecanismo de Consulta** | Protocolo LDAP com filtros de busca estruturados (ex.: `(&(objectCategory=person)(sAMAccountName=jsilva))`). | Linguagem declarativa SQL com junções relacionais complexas (`JOIN`). |
| **Transacionalidade / ACID** | Suporte transacional limitado; prioriza alta disponibilidade e replicação eventual. | Suporte rigoroso às propriedades ACID (Atomicidade, Consistência, Isolamento, Durabilidade). |
| **Padrão Normativo** | Baseado nas normas ITU-T X.500 e RFCs IETF (RFC 4511). | Padrão ANSI/ISO SQL. |

---

### 1.2 O Protocolo LDAP: Portas Padrão e Arquitetura TCP/IP

O **LDAP (*Lightweight Directory Access Protocol*)** foi desenvolvido para simplificar o pesado e complexo protocolo DAP (*Directory Access Protocol*) do padrão OSI X.500, eliminando a dependência das camadas superiores da pilha OSI e rodando diretamente sobre a pilha de transporte **TCP/IP**.

#### Portas de Rede Mandatórias para Concursos:
- **Porta TCP/UDP 389:** Porta padrão para tráfego LDAP em texto plano ou com elevação de segurança em canal aberto através do comando `StartTLS`.
- **Porta TCP 636:** Porta padrão para **LDAPS** (*LDAP over SSL/TLS*), onde toda a sessão de rede é encapsulada em criptografia TLS desde o aperto de mão inicial.
- **Porta TCP 3268:** Porta de consulta LDAP direcionada ao **Catálogo Global (*Global Catalog - GC*)** do Active Directory (consultas em nível de floresta).
- **Porta TCP 3269:** Porta de consulta LDAPS segura direcionada ao **Catálogo Global (GC)** com criptografia TLS.

---

### 1.3 Formato de Nomenclatura X.500: DN, RDN, CN, OU e DC

Cada objeto registrado no diretório possui uma identificação globalmente exclusiva na árvore denominada **Nome Distinto (*Distinguished Name* - DN)**. O DN é formado por uma cadeia encadeada de **Nomes Distintos Relativos (*Relative Distinguished Names* - RDNs)** separados por **vírgulas**:

```text
CN=Thiago Ramos,OU=Auditores,OU=Fiscalizacao,DC=tce,DC=go,DC=gov,DC=br
```

#### Atributos Fundamentais de Composição:
- **`CN` (*Common Name*):** Identificador relativo do objeto folha no nó atual (ex.: `CN=Thiago Ramos` ou `CN=Grupo_Auditores`).
- **`OU` (*Organizational Unit*):** Unidade Organizacional contêiner à qual o objeto pertence. A leitura do DN é feita da **folha para a raiz** (ou seja, `OU=Auditores` está contida no interior da `OU=Fiscalizacao`).
- **`DC` (*Domain Component*):** Cada um dos fragmentos de texto separados por ponto que integram o nome de domínio DNS corporativo (`DC=tce`, `DC=go`, `DC=gov`, `DC=br` para o domínio `tce.go.gov.br`).

> 🚨 **ALERTA DE PROVA / PEGADINHA FCC:**  
> A banca FCC costuma colocar opções invertidas (iniciando pelos `DC`s da raiz em direção ao `CN` folha) ou utilizando barras (`/`) e pontos (`.`) como delimitadores. A sintaxe canônica da RFC 4511 **inicia obrigatoriamente no objeto folha mais específico à esquerda** e utiliza **vírgulas** para separar cada atributo RDN.

---

### 1.4 Operações LDAP Fundamentais e Filtros de Busca

O protocolo LDAP define um conjunto de operações primitivas:

- **Bind:** Autentica a sessão do cliente perante o servidor de diretório (logon anônimo ou autenticado por credenciais).
- **Search:** Realiza consultas e extração de dados com filtros booleanos prefixados e três escopos de busca:
    - *Base:* Consulta restrita estritamente ao objeto indicado pelo DN base;
    - *One-Level:* Consulta todos os filhos imediatos localizados no primeiro nível abaixo da base;
    - *Subtree:* Consulta exaustiva em toda a subárvore hierárquica abaixo do nó base.
- **Add / Modify / Delete / ModifyDN:** Inserção, edição, exclusão e renomeação de objetos.
- **Unbind:** Encerramento formal da sessão LDAP.

---

## 2. Arquitetura Lógica do Microsoft Active Directory (AD DS)

### 2.1 Níveis Hierárquicos: OUs, Domínios, Árvores e Floresta

A estrutura lógica do **Active Directory Domain Services (AD DS)** organiza os objetos corporativos de forma desvinculada da disposição física dos cabos e prédios:

```mermaid
flowchart TD
    subgraph Floresta["FLORESTA (Fronteira Máxima de Segurança - Schema e Config Compartilhados)"]
        GC["Catálogo Global (GC)"]
        subgraph Arvore1["Árvore de Domínios 1: tce.go.gov.br"]
            D1["Domínio Raiz: tce.go.gov.br"]
            D2["Subdomínio: sistemas.tce.go.gov.br"]
            D1 <-->|"Confiança Bidirecional Transitiva Kerberos"| D2
        end
        subgraph Arvore2["Árvore de Domínios 2: orgaoexterno.gov.br"]
            D3["Domínio: orgaoexterno.gov.br"]
        end
        D1 <-->|"Confiança de Floresta Transitiva"| D3
        subgraph Estrutura_OU["Estrutura Interna de Domínio (ex: tce.go.gov.br)"]
            OU_Sede["OU Sede"]
            OU_TI["OU Tecnologia da Informação"]
            OU_Audit["OU Auditoria Fiscal"]
            OU_Sede --> OU_TI
            OU_Sede --> OU_Audit
            User1["Usuário: Carlos Silva"]
            GPO1["GPO Segurança de Senhas"]
            OU_Audit --> User1
            GPO1 -.->|"Vinculada a"| OU_Sede
        end
    end
```

#### Hierarquia Lógica Detalhada:
1. **Unidade Organizacional (OU - *Organizational Unit*):**
    - É o menor elemento da hierarquia do AD DS no qual se pode:
    - **Vincular diretamente uma Política de Grupo (GPO)**;
    - **Delegar poderes de administração** (ex.: conceder ao suporte técnico de Goiânia autorização para redefinir senhas exclusivamente dos servidores daquela OU).

2. **Domínio (*Domain*):**
    - É a unidade lógica central de segurança, replicação e gerenciamento de contas. Todos os Controladores de Domínio (DCs) do mesmo domínio replicam 100% dos objetos locais.

3. **Árvore de Domínios (*Domain Tree*):**
    - Coleção de um ou mais domínios que compartilham um **namespace DNS contíguo** (ex.: `tce.go.gov.br` e o filho `sistemas.tce.go.gov.br`). Estabelecem relações de confiança automáticas bidirecionais e transitivas entre pai e filho.

4. **Floresta (*Forest*):**
    - É a **fronteira máxima de segurança (*Security Boundary*)** de toda a arquitetura Active Directory.
    - Compreende uma ou mais árvores de domínios que obrigatoriamente compartilham:
    - Uma única partição de **Esquema (*Schema*)**;
    - Uma única partição de **Configuração (*Configuration*)**;
    - O **Catálogo Global (*Global Catalog*)**.

> 🚨 **ALERTA DE PROVA / PEGADINHA FCC:**  
> A FCC já elaborou questões afirmando que o *Domínio* é a fronteira máxima de segurança da arquitetura Windows. **A AFIRMATIVA É ERRADA!** O Domínio é uma *fronteira administrativa*. A **Floresta** é formalmente a **fronteira máxima de segurança**, haja vista que um administrador do domínio raiz da floresta (*Enterprise Admins*) possui privilégios de controle irrestrito que alcançam qualquer domínio subordinado da floresta.

---

### 2.2 Tipos e Escopos de Grupos no AD DS

Os grupos no Active Directory desempenham papéis fundamentais de organização e controle de acesso:

#### Tipos de Grupo:
- **Grupos de Segurança (*Security Groups*):** Possuem um identificador de segurança único (**SID** - *Security Identifier*). São os únicos que podem ser inseridos em Listas de Controle de Acesso (ACLs) para concessão de permissões em pastas, bancos e impressoras.
- **Grupos de Distribuição (*Distribution Groups*):** Não possuem SID e destinam-se exclusivamente ao envio em massa de e-mails corporativos (ex.: Exchange Server). Não podem receber permissões em recursos de TI.

#### Escopos de Grupos:
- **Global (G):** Agrupa usuários e computadores **do mesmo domínio**. Pode ser utilizado para atribuir permissões em qualquer domínio da floresta.
- **Local de Domínio (DL - *Domain Local*):** Pode conter membros (usuários, grupos globais) de **qualquer domínio confiável da floresta**, mas só pode ser utilizado para conceder permissões em recursos localizados **no mesmo domínio** onde o grupo reside.
- **Universal (U):** Pode conter membros de qualquer domínio da floresta e receber permissões em recursos de qualquer domínio da floresta. Suas alterações são replicadas para o Catálogo Global.

---

### 2.3 A Estratégia Canônica de Permissões: AGDLP e AGUDLP

A recomendação oficial de arquitetura da Microsoft para gestão segura e escalável de permissões adota a estratégia mnemônica **AGDLP**:

```mermaid
flowchart LR
    A["1. Accounts (Contas)<br>Usuários e computadores"] --> G["2. Global Groups<br>Agrupam Funções (ex: GG_Auditores)"]
    G --> DL["3. Domain Local Groups<br>Representam Direitos (ex: DL_PastaProcessos_Modificar)"]
    DL --> P["4. Permissions (ACLs)<br>Permissões NTFS no Servidor"]
```

1. **A**ccounts: As contas de usuário individuais são criadas e inseridas em...
2. **G**lobal Groups: Grupos Globais que representam uma função de trabalho corporativa (ex.: `GG_AuditoresFiscais`), que são adicionados a...
3. **D**omain **L**ocal Groups: Grupos Locais de Domínio criados especificamente para representar o nível de permissão sobre determinado recurso (ex.: `DL_ProcessosEletronicos_Leitura`), onde finalmente se aplicam as...
4. **P**ermissions: Permissões de controle de acesso (ACLs NTFS) na pasta do servidor de arquivos.

*(Em florestas multinacionais ou corporações complexas com múltiplos domínios, insere-se a camada de Grupos Universais, formando o padrão **AGUDLP**).*

---

## 3. Estrutura Física e Serviços de Infraestrutura do AD DS

### 3.1 Controladores de Domínio (DCs), ntds.dit e SYSVOL

- **Controlador de Domínio (DC - *Domain Controller*):** Servidor Windows que executa a função de AD DS, responsável por autenticar usuários, processar logon Kerberos e manter a base de dados.
- **`ntds.dit`:** O arquivo de banco de dados do Active Directory propriamente dito (baseado no mecanismo ESE / JET Blue).
- **Compartilhamento SYSVOL:** Pasta de rede replicada automaticamente entre todos os DCs que armazena os scripts de logon e os arquivos de configuração das Políticas de Grupo (GPOs).
- **RODC (*Read-Only Domain Controller*):** Controlador de Domínio somente leitura projetado para filiais ou escritórios remotos que não possuem segurança física adequada (sem sala cofre). Não armazena senhas em cache por padrão, resguardando o domínio central caso o hardware da filial seja furtado.

---

### 3.2 Sites, Sub-redes e Otimização de Replicação Física

Enquanto a estrutura lógica organiza os objetos em Domínios e OUs, a **Estrutura Física** modela a topologia real da rede:

- **Sub-redes (*Subnets*):** Mapeamento dos blocos de endereços IP de cada unidade (ex.: `10.1.0.0/24`).
- **Sites:** Agrupamento de sub-redes interligadas por links de rede de alta velocidade e baixa latência (LAN local).
- **Utilidade dos Sites:**
    1. *Direcionamento de Logon:* Garante que uma estação de trabalho em Goiânia autentique-se no DC local de Goiânia, sem atravessar links WAN lentos até Brasília.
    2. *Controle de Replicação:* A replicação intra-site (mesmo local) ocorre quase instantaneamente sem compressão; a replicação inter-site (entre filiais) é agendada para horários de menor tráfego e compactada via protocolo RPC sobre IP.

---

### 3.3 Catálogo Global (Global Catalog - GC)

O **Catálogo Global (GC)** é uma função especializada desempenhada por um ou mais Controladores de Domínio da floresta:

- Armazena uma réplica completa de todos os objetos do seu próprio domínio e uma **réplica parcial (somente leitura com os atributos mais consultados, como nome, e-mail e UPN) de todos os objetos de todos os outros domínios da floresta**.
- É indispensável para permitir que usuários façam login utilizando o seu *User Principal Name* (UPN: `usuario@orgao.gov.br`) e para a resolução de associações de Grupos Universais durante o processo de geração do token de logon.

---

### 3.4 As 5 Funções Mestres de Operação Única (FSMO)

Embora o Active Directory opere predominantemente sob o regime de replicação multimesmo (*multi-master*), determinadas tarefas críticas não admitem escritas concorrentes descentralizadas. Para essas operações, o AD DS define as **5 Funções FSMO (*Flexible Single Master Operations*)**:

| Escopo da Função | Função FSMO | Responsabilidade e Missão Crítica | Consequência da Falha Prolongada |
|---|---|---|---|
| **Nível de Floresta** *(Apenas 1 por Floresta)* | **Schema Master** *(Mestre de Esquema)* | Controla todas as modificações e extensões no Esquema do AD DS (criação de novas classes e atributos de objetos). | Não impacta logons de usuários; impede unicamente a instalação de softwares que alteram o schema (ex.: Exchange, SCCM). |
| **Nível de Floresta** *(Apenas 1 por Floresta)* | **Domain Naming Master** *(Mestre de Nomenclatura)* | Autoriza a criação, exclusão ou renomeação de domínios e partições de diretório em toda a floresta. | Impede unicamente criar novos domínios ou excluir domínios existentes. |
| **Nível de Domínio** *(1 em cada Domínio)* | **PDC Emulator** *(Emulador de PDC)* | **A função mais ativa e crítica:** atua como servidor de sincronização de relógio mestre (servidor NTP raiz), reconcilia alterações e falhas de senha com prioridade, e processa bloqueios de conta. | Causa atrasos na propagação de novas senhas, falhas de logon em contas recém-alteradas e erros de dessincronização no protocolo Kerberos. |
| **Nível de Domínio** *(1 em cada Domínio)* | **RID Master** *(Mestre de Identificadores Relativos)* | Distribui blocos (*pools*) de RIDs para todos os outros DCs do domínio. Cada objeto criado recebe um SID composto pelo SID do Domínio + um RID exclusivo. | Se o pool de RIDs de um DC se esgotar com o RID Master fora do ar, aquele DC fica impossibilitado de criar novos usuários, grupos ou máquinas. |
| **Nível de Domínio** *(1 em cada Domínio)* | **Infrastructure Master** *(Mestre de Infraestrutura)* | Atualiza referências cruzadas quando um objeto de outro domínio pertencente a um grupo local é modificado. | Em domínio único não tem efeito prático. Em multi-domínio sem GC conjunto, nomes de usuários externos podem demorar a se resolver nas ACLs. |

---

## 4. Políticas de Grupo (GPO) e Autenticação Kerberos v5

### 4.1 Precedência e Ordem de Processamento de GPOs (LSDOU)

Os **Objetos de Política de Grupo (GPOs - *Group Policy Objects*)** aplicam configurações centralizadas de segurança, registros, mapeamentos de impressoras e restrições a usuários e computadores.

O processamento das GPOs segue a ordem cronológica estrita representada pelo mnemônico **LSDOU**:

$$\text{1. Local} \longrightarrow \text{2. Site} \longrightarrow \text{3. Domain} \longrightarrow \text{4. Organizational Unit (OU)}$$

```mermaid
flowchart TD
    L["1. GPO Local (Máquina do Usuário)"] --> S["2. GPO vinculada ao Site"]
    S --> D["3. GPO vinculada ao Domínio"]
    D --> OUP["4. GPO vinculada à OU Pai"]
    OUP --> OUF["5. GPO vinculada à OU Filha (Maior Precedência Ordinária)"]
    
    style OUF fill:#bbf,stroke:#333,stroke-width:2px
```

- **Regra de Ouro da Resolução de Conflitos:** Em caso de políticas com parâmetros contraditórios, **a última diretiva processada é a que prevalece!**
- Como a OU filha é processada por último na cadeia ordinária, as configurações da **OU mais próxima do objeto possuem maior precedência** sobre as diretivas de Domínio, Site ou Local.

---

### 4.2 Bloqueio de Herança (Block Inheritance) vs. Imposição (Enforced)

O comportamento padrão de herança pode ser alterado por dois modificadores:

1. **Bloquear Herança (*Block Inheritance*):** Aplicado a uma Unidade Organizacional (OU) específica. Impede que a OU receba diretivas herdadas de níveis superiores (Site, Domínio e OUs pai).
2. **Imposição / Não Substituir (*Enforced*):** Aplicado diretamente a uma GPO vinculada a um nível superior (como o Domínio).  
   > 🚨 **REGRA DE PREVALÊNCIA ABSOLUTA FCC:**  
   > A opção **Enforced SOBREPÕE QUALQUER BLOQUEIO DE HERANÇA!** Uma GPO de domínio configurada como *Enforced* será obrigatoriamente aplicada a todas as estações e OUs subordinadas, mesmo que estas tenham o *Block Inheritance* explicitamente ativado.

---

### 4.3 Mecânica do Kerberos v5: KDC, AS, TGS, TGT e Bilhetes de Serviço

O protocolo **Kerberos v5** (RFC 4120) é o alicerce de autenticação e *Single Sign-On* (SSO) do Active Directory:

```mermaid
sequenceDiagram
    autonumber
    participant C as "Cliente (Estação de Trabalho)"
    participant AS as "Authentication Server (AS / KDC no DC)"
    participant TGS as "Ticket Granting Server (TGS / KDC)"
    participant S as "Servidor de Arquivos / Aplicação"

    C->>AS: 1. KRB_AS_REQ (Solicitação com carimbo de tempo cifrado pela senha do usuário)
    AS-->>C: 2. KRB_AS_REP (Retorna TGT cifrado pela chave do KDC + Sessão KDC)
    Note over C: Usuário agora possui um TGT (Ticket Granting Ticket)
    C->>TGS: 3. KRB_TGS_REQ (Apresenta TGT solicitando acesso ao serviço CIFS/HTTP)
    TGS-->>C: 4. KRB_TGS_REP (Retorna Ticket de Serviço cifrado com a chave do servidor)
    C->>S: 5. KRB_AP_REQ (Apresenta o Ticket de Serviço diretamente ao servidor de recursos)
    S-->>C: 6. KRB_AP_REP (Autenticação mútua confirmada; acesso liberado)
```

1. **`KRB_AS_REQ` / `KRB_AS_REP`:** O cliente envia uma requisição ao serviço de autenticação (**AS**). O AS valida a identidade e devolve uma chave de sessão e o **TGT (*Ticket Granting Ticket*)**, um bilhete cifrado com a chave secreta exclusiva do KDC (a conta `krbtgt`).
2. **`KRB_TGS_REQ` / `KRB_TGS_REP`:** De posse do TGT, quando o usuário precisa acessar um servidor de arquivos ou intranet, ele solicita um bilhete ao serviço concessor de bilhetes (**TGS**). O TGS valida o TGT e emite um **Ticket de Serviço (*Service Ticket*)** cifrado com a chave do servidor de destino.
3. **`KRB_AP_REQ`:** O cliente entrega o Ticket de Serviço diretamente ao servidor final, obtendo acesso imediato sem jamais trafegar sua senha pela rede.

---

### 4.4 Tolerância Temporal (Clock Skew) e o Papel do PDC Emulator

Para impedir que invasores capturem pacotes de autenticação na rede e os reenviem maliciosamente (**ataques de repetição / *replay attacks***), as mensagens do Kerberos incluem carimbos temporais (*timestamps*):

- O KDC exige que a diferença entre o relógio da estação cliente e o relógio do servidor de autenticação não ultrapasse um limite máximo, denominado **Desvio de Relógio (*Clock Skew*)**, configurado por padrão em **5 minutos**.
- Se a divergência for superior a 5 minutos, a autenticação Kerberos falha sumariamente.
- Por esse motivo, a função FSMO **PDC Emulator** atua compulsoriamente como a fonte oficial de sincronização horária (**NTP Master**) de toda a floresta do Active Directory.

---

## 5. Fontes Recomendadas na Internet

- [Microsoft Learn - Visão Geral do Active Directory Domain Services (AD DS)](https://learn.microsoft.com/pt-br/windows-server/identity/ad-ds/active-directory-domain-services): Documentação arquitetural oficial cobrindo florestas, domínios, OUs, catálogo global e replicação multimesmo.
- [IETF RFC 4511 - Lightweight Directory Access Protocol (LDAPv3)](https://datatracker.ietf.org/doc/html/rfc4511): Especificação padrão do IETF que formaliza a sintaxe de buscas, filtros booleanos e operações de protocolo LDAP.
- [Microsoft Learn - Ordem de Processamento e Precedência de Políticas de Grupo (GPO)](https://learn.microsoft.com/pt-br/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn789197(v=ws.11)): Guia técnico descrevendo a regra LSDOU, resolução de conflitos, herança de diretivas e comportamentos de *Enforced* e *Block Inheritance*.
- [Microsoft Learn - Funções Mestres de Operação Única (FSMO) no AD](https://learn.microsoft.com/pt-br/troubleshoot/windows-server/active-directory/fsmo-roles): Documentação canônica que detalha as cinco funções FSMO, suas regras de transferência e impactos de indisponibilidade.
- [IETF RFC 4120 - The Kerberos Network Authentication Service (V5)](https://datatracker.ietf.org/doc/html/rfc4120): Padrão oficial do protocolo Kerberos v5, detalhando as mensagens de troca de bilhetes (AS, TGS, TGT) e criptografia simétrica.

---

## 6. Questões Comentadas & Exemplos Práticos

### Questão 1 (FCC - Adaptada / Analista de TI - Infraestrutura e Redes)
Considere uma floresta corporativa do Microsoft Active Directory Domain Services (AD DS) composta por um único domínio denominado `tce.go.gov.br`. Um computador do setor de compras está localizado na Unidade Organizacional (OU) `Licitacoes`, que por sua vez é uma subunidade contida no interior da OU `Administrativo`. 

Existem quatro Políticas de Grupo (GPOs) com configurações conflitantes vinculadas aos seguintes níveis:

1. GPO "Diretiva-Local" configurada nas políticas da máquina local;
2. GPO "Diretiva-Site" vinculada ao Site físico do Active Directory;
3. GPO "Diretiva-Dominio" vinculada à raiz do Domínio `tce.go.gov.br`;
4. GPO "Diretiva-Admin" vinculada à OU pai `Administrativo`;
5. GPO "Diretiva-Licitacoes" vinculada à OU folha `Licitacoes`.

Sabendo que a OU `Licitacoes` possui a opção de "Bloquear Herança" (*Block Inheritance*) explicitamente habilitada, mas a GPO "Diretiva-Dominio" foi configurada pelo Administrador Corporativo com a opção de "Imposição" (*Enforced* / Não Substituir), assinale a alternativa que indica a política que terá a maior precedência final para definir o parâmetro conflitante na referida estação de trabalho:

* **A)** GPO "Diretiva-Local", em razão de as configurações físicas na estação de trabalho sempre prevalecerem sobre diretivas de rede.
* **B)** GPO "Diretiva-Site", pois diretivas de site físico são imunes a bloqueios de herança configurados em OUs.
* **C)** GPO "Diretiva-Admin", que é herdada compulsoriamente por ser a Unidade Organizacional hierarquicamente superior direta.
* **D)** GPO "Diretiva-Licitacoes", pois o bloqueio de herança impede a aplicação de qualquer diretiva originada fora da referida OU.
* **E)** GPO "Diretiva-Dominio", pois a opção de Imposição (*Enforced*) ignora e sobrepõe qualquer bloqueio de herança definido nas Unidades Organizacionais descendentes.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A diretiva Local é a primeira a ser processada na cadeia e possui a menor precedência em relação às diretivas de domínio.
> - **B)** Incorreta. As diretivas de Site são ordinariamente bloqueadas pelo Bloqueio de Herança caso não estejam marcadas como Enforced.
> - **C)** Incorreta. A GPO da OU Administrativo foi devidamente bloqueada pelo Block Inheritance da OU filha e não possui a flag Enforced.
> - **D)** Incorreta. O Bloqueio de Herança bloqueia diretivas comuns, mas é expressamente sobreposto pela configuração de Imposição (*Enforced*) da Diretiva de Domínio.
> - **E)** Correta. A opção *Enforced* (Imposição) foi desenhada pela Microsoft exatamente para garantir a prevalência inegociável de diretivas centrais de governança e segurança, sobrepondo qualquer bloqueio de herança definido em OUs subordinadas.
> 
> **Gabarito: E**

---

### Questão 2 (FCC - Adaptada / Tribunal de Contas - Especialidade Tecnologia da Informação)
No contexto de serviços de diretório baseados nas normas X.500 e no protocolo LDAP (RFC 4511), a localização precisa de um objeto no interior da Árvore de Informações de Diretório (DIT) é expressa por meio de seu Nome Distinto (*Distinguished Name* - DN).

Considere que um analista precisa cadastrar a conta de usuário do servidor "Julio Cesar", lotado no setor de "AuditoriaTributaria", pertencente à subunidade de "Fiscalizacao", dentro do domínio governamental `sefaz.go.gov.br`. 

De acordo com o padrão LDAP, assinale a alternativa que apresenta a sintaxe canônica e estruturalmente válida para o *Distinguished Name* (DN) desse objeto:

* **A)** `CN=Julio Cesar,OU=AuditoriaTributaria,OU=Fiscalizacao,DC=sefaz,DC=go,DC=gov,DC=br`
* **B)** `DN=Julio Cesar/OU=Fiscalizacao/OU=AuditoriaTributaria/DC=sefaz.go.gov.br`
* **C)** `USER=Julio Cesar,DEPT=AuditoriaTributaria,SECTOR=Fiscalizacao,DOMAIN=sefaz.go.gov.br`
* **D)** `DC=br,DC=gov,DC=go,DC=sefaz,OU=Fiscalizacao,OU=AuditoriaTributaria,CN=Julio Cesar`
* **E)** `CN=Julio Cesar.OU=AuditoriaTributaria.OU=Fiscalizacao.DC=sefaz.go.gov.br`

> **Comentário Detalhado:**
>
> - **A)** Correta. Segue com perfeição a regra de construção de DN da RFC 4511: inicia pelo nó folha mais específico (`CN=Julio Cesar`), seguido das OUs em ordem ascendente (`OU=AuditoriaTributaria`, `OU=Fiscalizacao`) e finaliza com os componentes de domínio DNS individualizados (`DC=sefaz,DC=go,DC=gov,DC=br`), todos separados por vírgulas.
> - **B)** Incorreta. Utiliza barras como delimitadores e agrupa o domínio com pontos, violando a norma de atributos individuais DC.
> - **C)** Incorreta. Emprega identificadores inexistentes no esquema padrão LDAP (`USER`, `DEPT`, `SECTOR`, `DOMAIN`).
> - **D)** Incorreta. Inverte a ordem exigida: o DN deve iniciar na folha mais específica à esquerda, e não na raiz.
> - **E)** Incorreta. Utiliza pontos como delimitadores entre os atributos RDN no lugar de vírgulas.
> 
> **Gabarito: A**

---

### Questão 3 (FCC - Adaptada / Analista de Sistemas - Suporte a Servidores)
Em uma floresta multi-domínio do Microsoft Active Directory Domain Services (AD DS), a arquitetura do sistema delega certas operações a servidores específicos por meio das funções Mestres de Operação Única Flexível (*Flexible Single Master Operations* - FSMO). 

Sobre as atribuições e o escopo dessas funções, é correto afirmar:

* **A)** A função de *Schema Master* possui escopo restrito a cada domínio individual da floresta, permitindo que cada domínio configure seus próprios atributos de usuário de maneira independente e isolada.
* **B)** A função de *PDC Emulator* (Emulador de Controlador de Domínio Primário) atua no nível de domínio e é a principal responsável por atuar como autoridade de referência de sincronização de horário (servidor NTP), além de processar com prioridade as alterações e bloqueios de senhas de usuários.
* **C)** A função de *RID Master* opera no nível de floresta e atua exclusivamente na validação de nomes de novos domínios que solicitam ingresso na estrutura hierárquica do AD.
* **D)** As cinco funções FSMO operam compulsoriamente no mesmo e único Controlador de Domínio raiz, sendo tecnicamente impossível transferi-las individualmente entre diferentes servidores da rede.
* **E)** A função de *Domain Naming Master* tem escopo de domínio e é responsável por atribuir identificadores relativos (RIDs) a cada novo objeto criado pelos controladores de domínio locais.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O Schema Master possui escopo de floresta (apenas 1 por floresta); o esquema do AD DS é único e universal para todos os domínios da floresta.
> - **B)** Correta. O PDC Emulator opera no nível de domínio e é a função FSMO de maior atividade, sendo responsável pela sincronização de tempo NTP (vital para o Kerberos) e processamento imediato de alterações de senha.
> - **C)** Incorreta. O RID Master opera no nível de domínio e distribui blocos de identificadores relativos para criação de novos SIDs.
> - **D)** Incorreta. As funções FSMO são flexíveis e podem ser livremente distribuídas e transferidas entre diferentes Controladores de Domínio.
> - **E)** Incorreta. O Domain Naming Master tem escopo de floresta e cuida da nomenclatura e criação de domínios, e não da alocação de RIDs.
> 
> **Gabarito: B**

---

### Questão 4 (FCC - Adaptada / Analista de Tecnologia da Informação - Segurança da Informação)
No protocolo de autenticação Kerberos v5, implementado nativamente pelo Active Directory Domain Services para prover autenticação mútua e *Single Sign-On* (SSO) no ambiente de rede corporativo:

* **A)** As senhas dos usuários são transmitidas em texto claro durante a etapa inicial de negociação com o Authentication Server (AS), dependendo de túneis VPN para garantir a confidencialidade do tráfego.
* **B)** O serviço Ticket Granting Server (TGS) emite o bilhete inicial de concessão de bilhetes (*Ticket Granting Ticket* - TGT) imediatamente antes de validar as credenciais biométricas do usuário na máquina cliente.
* **C)** A tolerância temporal de dessincronização de relógio (*clock skew*) entre os clientes e o KDC é irrelevante para a segurança do protocolo, pois o Kerberos utiliza exclusivamente desafios e respostas baseados em números aleatórios (*nonces*).
* **D)** O cliente obtém inicialmente um TGT junto ao serviço de autenticação (AS) e posteriormente apresenta esse TGT ao servidor de concessão de bilhetes (TGS) para solicitar bilhetes de serviço específicos para acessar recursos de rede.
* **E)** O protocolo prescinde do uso de criptografia simétrica, utilizando certificados digitais de chave pública assimetricamente em todas as interações de solicitação de arquivos.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. No Kerberos, a senha do usuário jamais é transmitida pela rede em nenhuma circunstância.
> - **B)** Incorreta. Quem emite o TGT inicial durante o logon primário é o serviço Authentication Server (AS), e não o TGS.
> - **C)** Incorreta. A sincronia de relógio é indispensável para evitar ataques de repetição (*replay attack*). Se o desvio temporal exceder a tolerância padrão de 5 minutos, a autenticação falhará.
> - **D)** Correta. Sintetiza com exatidão a dinâmica operacional do Kerberos: obtenção inicial do TGT no AS e posterior apresentação ao TGS para emissão de tickets de serviço específicos.
> - **E)** Incorreta. O Kerberos é fundamentalmente alicerçado em criptografia simétrica rápida e segredos compartilhados.
> 
> **Gabarito: D**

---

### Questão 5 (FCC - Adaptada / Analista de Redes e Sistemas)
Em uma organização pública que utiliza o Active Directory, um administrador necessita conceder permissões de leitura e modificação a uma pasta compartilhada no servidor de arquivos para os colaboradores do departamento financeiro. A organização segue rigorosamente a metodologia recomendada de desenho de segurança de identidades baseada na estratégia AGDLP.

Para cumprir esse padrão, a sequência correta de estruturação de contas, escopos de grupo e permissões de acesso é:

* **A)** As contas de usuários (**A**) são adicionadas diretamente à lista de controle de acesso (ACL) da pasta compartilhada, dispensando o uso de grupos intermediários.
* **B)** As contas de usuários (**A**) são inseridas em Grupos Locais de Domínio (**DL**), os quais são atribuídos a Grupos Globais (**G**), que por sua vez recebem as Permissões (**P**) na pasta.
* **C)** As contas de usuários (**A**) são inseridas em Grupos Globais (**G**), estes Grupos Globais são adicionados a Grupos Locais de Domínio (**DL**), e as Permissões (**P**) na pasta são atribuídas aos Grupos Locais de Domínio.
* **D)** As contas de usuários (**A**) são inseridas em Grupos de Distribuição, que são convertidos em Grupos de Segurança para receberem Permissões (**P**) no nível de Site.
* **E)** As contas de usuários (**A**) são associadas diretamente a uma Unidade Organizacional (**OU**), onde as permissões NTFS (**P**) de pastas são vinculadas via GPO.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Inserir usuários individuais em ACLs é uma péssima prática de governança que inviabiliza a auditoria e a escala administrativa.
> - **B)** Incorreta. Inverte a ordem do aninhamento estrutural: no AGDLP, os Grupos Globais entram nos Grupos Locais de Domínio.
> - **C)** Correta. Expressa a metodologia canônica AGDLP: Contas (**A**) entram em Grupos Globais (**G** que definem funções), estes entram em Grupos Locais de Domínio (**DL** que definem direitos), que finalmente recebem as Permissões (**P**) nas ACLs de pastas.
> - **D)** Incorreta. Grupos de Distribuição não possuem SID e não são utilizados para atribuir permissões de acesso em arquivos.
> - **E)** Incorreta. OUs não são entidades de segurança (*security principals*) e não podem receber permissões em ACLs de sistemas de arquivos.
> 
> **Gabarito: C**
