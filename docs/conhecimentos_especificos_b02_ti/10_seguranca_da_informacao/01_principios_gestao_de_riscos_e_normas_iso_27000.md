# 01 - Princípios, Gestão de Riscos e Normas ISO/IEC 27000
**Última Atualização:** 2026-03-31  
**Banca Foco:** FCC (Fundação Carlos Chagas)  
**Cargo:** Auditor de Controle Externo - Tecnologia da Informação  
**Status do Mapeamento:** 100% aderente ao edital TCE-GO

---

## 📌 Ementa / Itens do Edital
1. **Princípios Fundamentais da Segurança da Informação:** Confidencialidade, Integridade, Disponibilidade, Autenticidade e Não Repúdio / Irretratabilidade (CIDAN); Atributos complementares (Conformidade/Legalidade, Auditorabilidade/*Accountability* e Privacidade).
2. **Classificação e Rotulagem da Informação:** Critérios de sensibilidade e criticidade de ativos; Graus de sigilo na Administração Pública conforme a Lei de Acesso à Informação (LAI - Lei nº 12.527/2011: Reservada com 5 anos, Secreta com 15 anos e Ultrassecreta com 25 anos; prazos de prorrogação e dados pessoais até 100 anos); e Classificação corporativa geral (Pública, Interna, Confidencial e Restrita).
3. **Gestão de Riscos de Segurança da Informação:** Ativo (*Asset*), Ameaça (*Threat*), Vulnerabilidade (*Vulnerability*) e Impacto; Risco Inerente vs. Risco Residual e Apetite ao Risco; Análise Qualitativa (matrizes de probabilidade vs. impacto) vs. Análise Quantitativa ($SLE = AV \times EF$, $ALE = SLE \times ARO$ e CBA); e Opções de Tratamento do Risco (Mitigar/Reduzir, Aceitar/Reter, Transferir/Compartilhar e Evitar/Eliminar).
4. **Gestão de Vulnerabilidades e Resposta a Incidentes:** Sistema CVSS v3.1 (métricas de base, temporais, ambientais e faixas de severidade); Ciclo de Resposta a Incidentes (NIST SP 800-61 Rev. 2 e ISO/IEC 27035: Preparação, Detecção e Análise, Contenção/Erradicação/Recuperação e Atividades Pós-Incidente/Lições Aprendidas); e Equipes CSIRT/CERT.
5. **Família de Normas ABNT NBR ISO/IEC 27000:** ISO/IEC 27000 (vocabulário); ISO/IEC 27001 (Requisitos auditáveis e certificáveis do SGSI, estrutura de alto nível do Anexo SL e ciclo PDCA); ISO/IEC 27002 (Código de Práticas, estrutura moderna em 4 temas: Organizacionais, Pessoas, Físicos e Tecnológicos, totalizando 93 controles; e a Declaração de Aplicabilidade - SoA); e ISO/IEC 27005 (Diretrizes para Gestão de Riscos de Segurança da Informação).

---

## 🧭 Sumário

1. [Princípios Básicos da Segurança da Informação (CIDAN)](#1-principios-basicos-da-seguranca-da-informacao-cidan)
    1. [Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade](#11-os-pilares-fundamentais-confidencialidade-integridade-e-disponibilidade)
    2. [Autenticidade, Não Repúdio e Atributos Complementares](#12-autenticidade-nao-repudio-e-atributos-complementares)
    3. [Teste 355](#Teste-355)
    4. [Teste 356](#Teste-356)
2. [Classificação e Rotulagem da Informação](#2-classificacao-e-rotulagem-da-informacao)
    1. [Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)](#21-graus-de-sigilo-no-setor-publico-lei-de-acesso-a-informacao-lei-no-125272011)
    2. [Classificação Corporativa Geral de Ativos](#22-classificacao-corporativa-geral-de-ativos)
    3. [Teste 357](#Teste-357)
    4. [Teste 358](#Teste-358)
3. [Gestão e Análise de Riscos de Segurança da Informação](#3-gestao-e-analise-de-riscos-de-seguranca-da-informacao)
    1. [A Tríade Ativo, Ameaça e Vulnerabilidade](#31-a-triade-ativo-ameaca-e-vulnerabilidade)
    2. [Análise Qualitativa vs. Análise Quantitativa (SLE, ARO e ALE)](#32-analise-qualitativa-vs-analise-quantitativa-sle-aro-e-ale)
    3. [As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)](#33-as-quatro-estrategias-de-tratamento-do-risco-isoiec-27005)
    4. [Teste 359](#Teste-359)
    5. [Teste 360](#Teste-360)
    6. [Teste 361](#Teste-361)
4. [Gestão de Vulnerabilidades e Resposta a Incidentes](#4-gestao-de-vulnerabilidades-e-resposta-a-incidentes)
    1. [Métricas do CVSS v3.1 (Common Vulnerability Scoring System)](#41-metricas-do-cvss-v31-common-vulnerability-scoring-system)
    2. [As Quatro Fases do Ciclo de Resposta a Incidentes (NIST SP 800-61)](#42-as-quatro-fases-do-ciclo-de-resposta-a-incidentes-nist-sp-800-61)
    3. [Teste 362](#Teste-362)
    4. [Teste 363](#Teste-363)
5. [Família de Normas ISO/IEC 27000 (SGSI)](#5-familia-de-normas-isoiec-27000-sgsi)
    1. [A Norma Certificável ISO/IEC 27001 e o Anexo SL](#51-a-norma-certificavel-isoiec-27001-e-o-anexo-sl)
    2. [A Nova ISO/IEC 27002 (Edição 2022: 4 Temas e 93 Controles)](#52-a-nova-isoiec-27002-edicao-2022-4-temas-e-93-controles)
    3. [A Declaração de Aplicabilidade (SoA) e a ISO/IEC 27005](#53-a-declaracao-de-aplicabilidade-soa-e-a-isoiec-27005)
    4. [Teste 364](#Teste-364)
    5. [Teste 365](#Teste-365)
6. [🌐 Fontes Oficiais e Referências Bibliográficas](#fontes-oficiais-e-referencias-bibliograficas)

---

## 1. Princípios Básicos da Segurança da Informação (CIDAN)

A segurança da informação é definida pela norma ABNT NBR ISO/IEC 27000 como a preservação da confidencialidade, integridade e disponibilidade da informação, admitindo-se adicionalmente propriedades vitais para transações formais como a autenticidade e o não repúdio. O mnemônico padronizado em concursos da FCC é **CIDAN**.

### 1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade

1. **Confidencialidade (*Confidentiality*):**
    - Garantia de que o acesso à informação é restrito estrita e exclusivamente a pessoas, entidades ou processos formalmente autorizados.
    - *Ameaças clássicas:* Escuta clandestina de rede (*sniffing/eavesdropping*), roubo de dispositivos físicos, engenharia social, vazamento inadvertido de dados fiscais protegidos por sigilo e acessos não autorizados.
    - *Mecanismos técnicos:* Criptografia em trânsito (TLS) e em repouso (TDE), controle de acesso lógico baseado em papéis (RBAC), mascaramento dinâmico de dados e soluções de Prevenção contra Perda de Dados (*DLP - Data Loss Prevention*).

2. **Integridade (*Integrity*):**
    - Propriedade de salvaguardar a exatidão, originalidade e completude da informação e de seus métodos de processamento, impedindo alterações, corrupções ou supressões indevidas ou não autorizadas.
    - *Ameaças clássicas:* Adulteração maliciosa de tabelas contábeis ou salariais em bancos de dados (*tampering*), infecção por malware, ataques man-in-the-middle e erros de transmissão de rede sem checagem de paridade.
    - *Mecanismos técnicos:* Funções criptográficas de espalhamento (*hashing* criptográfico como SHA-256 e SHA-512), códigos de autenticação de mensagem (HMAC), assinaturas digitais, somas de verificação (*checksums*) e trilhas de auditoria imutáveis.

3. **Disponibilidade (*Availability*):**
    - Garantia de que a informação, os sistemas computacionais e os ativos de telecomunicações associados estejam acessíveis e utilizáveis sob demanda pelos usuários autorizados sempre que necessário.
    - *Ameaças clássicas:* Ataques de negação de serviço (DoS e DDoS), falhas físicas de hardware em servidores e storages, interrupção no fornecimento de energia elétrica, panes nos links de internet e desastres ambientais (enchentes, incêndios em datacenters).
    - *Mecanismos técnicos:* Redundância de hardware e fontes de alimentação, clusters de alta disponibilidade (HA ativo-ativo ou ativo-passivo), sistemas anti-DDoS, geradores e nobreaks comutáveis, planos de continuidade de negócios (PCN/DRP) e rotinas estruturadas de backup.

### 1.2 Autenticidade, Não Repúdio e Atributos Complementares

* **Autenticidade (*Authenticity*):**
    - Garantia da veracidade da identidade alegada da fonte emissora ou do autor da informação. Assegura que o documento ou mensagem procede de fato da pessoa ou sistema que afirma ser seu originador.
    - *Mecanismos:* Certificados digitais de chave pública padrão X.509, autenticação multifator (MFA) e assinaturas eletrônicas qualificadas.
* **Não Repúdio / Irretratabilidade (*Non-Repudiation*):**
    - Capacidade de comprovar a autoria e a realização inequívoca de um ato, transação ou envio de mensagem de tal modo que o autor **não possa negar formal ou judicialmente perante terceiros ter praticado a ação**.
    - *Mecanismos:* Assinatura digital padrão ICP-Brasil (com posse e custódia da chave privada) associada a carimbos do tempo (*timestamps*) emitidos por Autoridades de Carimbo do Tempo (ACT).

| Princípio | Pergunta Central de Verificação | Violação Típica | Mecanismo Primário de Defesa |
| :--- | :--- | :--- | :--- |
| **Confidencialidade** | *Quem tem autorização para visualizar?* | Espionagem, vazamento de dados | Criptografia, ACLs, TDE, DLP |
| **Integridade** | *O dado permanece exato e sem alterações?* | Adulteração, injeção de malware | Hashes criptográficos (SHA-256), HMAC |
| **Disponibilidade** | *O serviço está no ar quando requisitado?* | Ataques DDoS, quebra de storage | Clusters HA, Redundância, Backups |
| **Autenticidade** | *A identidade alegada é genuína?* | Falsificação de remetente (*spoofing*) | Certificados Digitais X.509, MFA |
| **Não Repúdio** | *O remetente pode negar juridicamente o envio?* | Alegação de repúdio posterior | Assinatura ICP-Brasil + Carimbo do Tempo |

> ⚠️ **Alerta de Prova (FCC):**
> A banca FCC costuma colocar como pegadinha a confusão entre **Autenticidade** e **Não Repúdio**:
>
> - *Autenticidade* foca na **certeza técnica de quem produziu** o dado;
> - *Não Repúdio* assegura a **impossibilidade jurídica de o emissor negar a autoria**, exigindo prova probatória cabal que blinda a transação contra contestações judiciais.

* **Atributos Complementares Modernos:**
    - **Conformidade / Legalidade:** Observância estrita às normas regulatórias e marcos legais (LGPD, LAI, Marco Civil da Internet).
    - **Auditorabilidade / Responsabilização (*Accountability*):** Capacidade de rastrear inequivocamente quem realizou determinada intervenção através de logs cronológicos protegidos contra exclusão.
    - **Privacidade:** Garantia de que dados pessoais sejam tratados em conformidade com o princípio da finalidade e autodeterminação informativa.

---

### Teste 001
**(FGV – TJ/AP – 2023 – Analista Judiciario Apoio Especializado Tecnologia Da Informacao Seguranca Da Informacao)**
A arquitetura de firewall da empresa APP.TI utiliza uma sub-rede para isolar a rede interna e a internet. Essa é uma arquitetura de firewall do tipo:

* **A)** Packet Filter;
* **B)** Screened Host;
* **C)** Screened Subnet;
* **D)** Dual-Homed Host;
* **E)** Stateful Inspection.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Packet Filter". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Ataques de negação de serviço (DoS e DDoS), falhas físicas de hardware em servidores e storages, interrupção no fornecimento de energia elétrica, panes nos links de internet e desastres ambientais (enchentes, incêndios em datacenters).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Screened Host". De acordo com a teoria estudada em *3.2 Análise Qualitativa vs. Análise Quantitativa (SLE, ARO e ALE)*, utiliza escalas ordinais descritivas (ex.: Baixo, Médio, Alto, Crítico) distribuídas em uma Matriz de Probabilidade vs. Impacto.
> - **C)** **Correta.** Conforme fundamentado na seção *4.2 As Quatro Fases do Ciclo de Resposta a Incidentes (NIST SP 800-61)* deste guia, contenção: Ação emergencial prioritária voltada a estancar a disseminação do ataque e limitar o raio de destruição ( blast radius ), tal como isolar a máquina da rede, desconectar cabos ou bloquear portas de switches. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/AP/2023) ao estabelecer que "Screened Subnet".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Dual Homed Host". De acordo com a teoria estudada em *2.2 Classificação Corporativa Geral de Ativos*, interna: Informação para circulação interna restrita aos servidores e colaboradores; divulgação indevida acarreta transtorno administrativo leve.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Stateful Inspection". De acordo com a teoria estudada em *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade*, (Causa potencial externa indesejada: (Fraqueza ou brecha interna explorável.
>
> **Gabarito: C**

---

### Teste 002
**(FCC – TRT 14ª – 2016 – Analista Judiciário - Apoio Especializado - Tecnologia da Informação)**
Um Analista sugeriu corretamente instalar, como mecanismo de segurança da informação, um

* **A)** Servidor firewall à frente do VPN. O servidor firewall seria conectado à intranet e o VPN seria posicionado entre o servidor firewall e a internet para bloquear totalmente os acessos indevidos.
* **B)** Filtro de conteúdo, para analisar todo o tráfego que circula entre a rede local e a internet, impedindo o acesso a sites utilizando bloqueio por palavra-chave, por URL ou por horário.
* **C)** Sistema de Prevenção de Intrusão − IDS, um sistema passivo que examina o tráfego e informa sobre ameaças, após o firewall.
* **D)** Sistema de Detecção de Intrusão − IPS antes do firewall, para analisar ativamente o fluxo de tráfego que entra na rede e realizar ações de bloqueio automaticamente.
* **E)** Roteador IP com recurso de NAT no ponto de conexão entre a VPN e a internet, para converter endereços IPv6 de com- putadores da VPN em endereços IPv4 da internet.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Servidor firewall à frente do VPN. O servidor firewall seria conectado à intranet e o VPN seria posicionado entre...". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Escuta clandestina de rede ( sniffing/eavesdropping ), roubo de dispositivos físicos, engenharia social, vazamento inadvertido de dados fiscais protegidos por sigilo e acessos não autorizados.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Filtro de conteúdo, para analisar todo o tráfego que circula entre a rede local e a internet, impedindo o acesso a...". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Ataques de negação de serviço (DoS e DDoS), falhas físicas de hardware em servidores e storages, interrupção no fornecimento de energia elétrica, panes nos links de internet e desastres ambientais (enchentes, incêndios em datacenters).
> - **C)** **Correta.** Conforme fundamentado na seção *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade* deste guia, risco Residual: Risco que subsiste e permanece após o projeto e a entrada em operação dos controles de segurança mitigadores. Deve situar se estritamente abaixo do Apetite ao Risco fixado pela diretoria do tribunal. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 14ª/2016) ao estabelecer que "Sistema de Prevenção de Intrusão − IDS, um sistema passivo que examina o tráfego e informa sobre ameaças, após o...".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Sistema de Detecção de Intrusão − IPS antes do firewall, para analisar ativamente o fluxo de tráfego que entra na...". De acordo com a teoria estudada em *4.2 As Quatro Fases do Ciclo de Resposta a Incidentes (NIST SP 800-61)*, detecção e Análise ( Detection and Analysis ): Monitoramento contínuo de alertas de IDS/IPS, antivírus/EDR e correlação de logs em SIEM para constatar indícios de comprometimento ( IoCs ) e dimensionar o alcance do ataque.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Roteador IP com recurso de NAT no ponto de conexão entre a VPN e a internet, para converter endereços IPv6 de com...". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, a norma ABNT NBR ISO/IEC 27001 estabelece os requisitos formais para estabelecer, implementar, manter e melhorar continuamente um Sistema de Gestão de Segurança da Informação (SGSI).
>
> **Gabarito: C**

---

### Teste 003
**(FGV – TRT 16ª – 2022 – Analista Judiciário (Área Administrativa - Tecnologia da Informação))**
Os firewalls podem ser um meio eficaz de proteger sistemas e redes contra ameaças de segurança. Com relação às suas limitações, analise os itens a seguir. I. Não são capazes de proteger contra os ataques que contornam o firewall. II. Não protegem contra ameaças internas, como funcionários insatisfeitos ou que cooperam com um atacante externo. III. Não protegem contra a transferência de programas ou arquivos infectados com vírus. Está correto o que se afirma em

* **A)** I, apenas.
* **B)** II, apenas.
* **C)** III, apenas.
* **D)** I, II e III.
* **E)** II e III, apenas.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I, apenas". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Ataques de negação de serviço (DoS e DDoS), falhas físicas de hardware em servidores e storages, interrupção no fornecimento de energia elétrica, panes nos links de internet e desastres ambientais (enchentes, incêndios em datacenters).
> - **B)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II, apenas". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, cláusula 9: Avaliação de Desempenho (Auditorias internas e análise pela direção).
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "III, apenas". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, mitigar / Reduzir ( Risk Mitigation / Reduction ): Implementar controles de segurança (técnicos, administrativos ou físicos) para reduzir a probabilidade e/ou o impacto do risco até patamares aceitáveis (ex.: instalar firewalls, adotar MFA e criptografia).
> - **D)** **Correta.** Conforme fundamentado na seção *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade* deste guia, ameaças clássicas: Adulteração maliciosa de tabelas contábeis ou salariais em bancos de dados ( tampering ), infecção por malware, ataques man in the middle e erros de transmissão de rede sem checagem de paridade. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT 16ª/2022) ao estabelecer que "I, II e III".
> - **E)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II e III, apenas". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, sTALLINGS, William. Criptografia e Segurança de Redes: Princípios e Práticas. 7. ed. São Paulo: Pearson Education do Brasil, 2018. (Cap. 1 Visão Geral de Segurança da Informação).
>
> **Gabarito: D**

---

### Teste 004
**(FGV – TRF/1 – 2024 – Analista Judiciario Area Apoio Especializado Especialidade Suporte Em Tecnologia Da Informacao)**
Um estagiário recebeu a tarefa de documentar a topologia de uma rede atualmente em operação. Durante essa análise, identificou-se a presença de um único dispositivo de firewall localizado entre um roteador interno e um roteador externo. Esse firewall tem a capacidade de implementar filtros com estado e/ou proxies de aplicação. A configuração descrita é chamada de bastião:

* **A)** em sdrop;
* **B)** duplo em T;
* **C)** único em T;
* **D)** duplo em linha;
* **E)** único em linha.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "em sdrop". De acordo com a teoria estudada em *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade*, vulnerabilidade ( Vulnerability ): Ponto fraco, falha de projeto, brecha de configuração ou deficiência de controle em um ativo que pode ser explorado por uma ameaça.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "duplo em T". De acordo com a teoria estudada em *4.2 As Quatro Fases do Ciclo de Resposta a Incidentes (NIST SP 800-61)*, atividades Pós Incidente ( Post Incident Activity / Lessons Learned ): Reunião formal de Lições Aprendidas para documentar como o incidente foi tratado, registrar métricas temporais e aprimorar as salvaguardas da fase de preparação.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "único em T". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, nIST SP 800 37 Rev. 2 Risk Management Framework Diretrizes para aplicação do Risk Management Framework (RMF) aos sistemas e organizações.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "duplo em linha". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, mitigar / Reduzir ( Risk Mitigation / Reduction ): Implementar controles de segurança (técnicos, administrativos ou físicos) para reduzir a probabilidade e/ou o impacto do risco até patamares aceitáveis (ex.: instalar firewalls, adotar MFA e criptografia).
> - **E)** **Correta.** Conforme fundamentado na seção *3.2 Análise Qualitativa vs. Análise Quantitativa (SLE, ARO e ALE)* deste guia, onde $\text{AV}$ ( Asset Value ) é o valor financeiro do ativo e $\text{EF}$ ( Exposure Factor ) é a fração percentual do valor do ativo perdida em um único incidente (0% a 100%). Dessa forma, está plenamente correta a assertiva da banca (FGV – TRF/1/2024) ao estabelecer que "único em linha".
>
> **Gabarito: E**

---

### Teste 005
**(FGV – TRF/1 – 2024 – Analista Judiciario Area Apoio Especializado Especialidade Suporte Em Tecnologia Da Informacao)**
João não sabe fazer consultas em banco de dados e buscou a literatura para fazer uma junção interna otimizada. Um dos pontos observados por João foi que suas relações não tinham seus registros fisicamente organizados, necessitando de uma ordenação externa. Os atributos de junção são atributos chave. Pares de blocos de arquivo são copiados para buffers de memória na ordem, e os registros de cada arquivo são varridos apenas uma vez cada um, para combinar com o outro arquivo. O método de implementação da junção utilizado por João foi o(a):

* **A)** loop alinhado;
* **B)** bloco alinhado;
* **C)** ordenação - intercalação;
* **D)** único loop;
* **E)** partição - hash.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "loop alinhado". De acordo com a teoria estudada em *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade*, ex.: banco de dados tributário do TCE GO).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "bloco alinhado". De acordo com a teoria estudada em *2.2 Classificação Corporativa Geral de Ativos*, interna: Informação para circulação interna restrita aos servidores e colaboradores; divulgação indevida acarreta transtorno administrativo leve.
> - **C)** **Correta.** Conforme fundamentado na seção *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade* deste guia, (Causa potencial externa indesejada: (Fraqueza ou brecha interna explorável. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRF/1/2024) ao estabelecer que "ordenação intercalação".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "único loop". De acordo com a teoria estudada em *3.2 Análise Qualitativa vs. Análise Quantitativa (SLE, ARO e ALE)*, onde $\text{AV}$ ( Asset Value ) é o valor financeiro do ativo e $\text{EF}$ ( Exposure Factor ) é a fração percentual do valor do ativo perdida em um único incidente (0% a 100%).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "partição hash". De acordo com a teoria estudada em *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade*, risco Inerente: Risco existente em seu estado natural bruto, antes da implementação de qualquer controle protetivo.
>
> **Gabarito: C**

---

### Teste 006
**(FGV – TRT/DA – 2025 – Analista Judiciario Area Apoio Especializado Tecnologia Da Informacao)**
Um modelo de índice é uma maneira de informar ao Elasticsearch como configurar um índice quando ele for criado. Os tipos de modelos de índice disponíveis no Elasticsearch são

* **A)** file e directory.
* **B)** index e component.
* **C)** log, metric e profiler.
* **D)** file, volume e dataset.
* **E)** blob, hash e collection.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "file e directory". De acordo com a teoria estudada em *Fundamentos Teóricos*, banca Foco: FCC (Fundação Carlos Chagas).
> - **B)** **Correta.** Conforme fundamentado na seção *Fundamentos Teóricos* deste guia, última Atualização: 2026 03 31. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT/DA/2025) ao estabelecer que "index e component".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "log, metric e profiler". De acordo com a teoria estudada em *Fundamentos Teóricos*, status do Mapeamento: 100% aderente ao edital TCE GO.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "file, volume e dataset". De acordo com a teoria estudada em *1. Princípios Básicos da Segurança da Informação (CIDAN)*, a segurança da informação é definida pela norma ABNT NBR ISO/IEC 27000 como a preservação da confidencialidade, integridade e disponibilidade da informação, admitindo se adicionalmente propriedades vitais para transações formais como a autenticidade e o não repúdio. O mnemônico padronizado em concursos da FCC é CIDAN.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "blob, hash e collection". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, confidencialidade ( Confidentiality ).
>
> **Gabarito: B**

---

### Teste 007
**(FGV – TJ/RR – 2024 – Analista Judiciario Infraestrutura De Tecnologia Da Informacao)**
Você, como analista de segurança ou de infraestrutura do TJ-RR, pode ser incumbido de instalar e configurar servidores para resoluções de nomes de domínio da Internet. Uma das soluções mais robustas para esse fim é o BIND, do Internet Systems Consortium (ISC). Em relação ao tema, avalie se cada afirmativa a seguir, referente a boas práticas recomendadas pelo ISC para administração do BIND, é verdadeira (V) ou falsa (F) . ( ) Assegurar que a infraestrutura utilizada suporte EDNS0 e pacotes UDP de tamanhos reduzidos. ( ) Não combinar funções de servidor de nomes autoritativas e recursivas no mesmo servidor. ( ) Empregar firewalls/filtros de pacotes com estado em seus servidores para tráfego de consulta de saída. As afirmativas são, respectivamente,

* **A)** V – F – V.
* **B)** V – V – V.
* **C)** V – F – F.
* **D)** F – V – V.
* **E)** F – V – F.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "V – F – V". De acordo com a teoria estudada em *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade*, vulnerabilidade ( Vulnerability ): Ponto fraco, falha de projeto, brecha de configuração ou deficiência de controle em um ativo que pode ser explorado por uma ameaça.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "V – V – V". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Ataques de negação de serviço (DoS e DDoS), falhas físicas de hardware em servidores e storages, interrupção no fornecimento de energia elétrica, panes nos links de internet e desastres ambientais (enchentes, incêndios em datacenters).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "V – F – F". De acordo com a teoria estudada em *5.2 A Nova ISO/IEC 27002 (Edição 2022: 4 Temas e 93 Controles)*, a norma ISO/IEC 27002 constitui um Código de Práticas que detalha diretrizes para implementação dos controles de segurança do Anexo A da ISO 27001. Não é passível de certificação independente.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "F – V – V". De acordo com a teoria estudada em *5.3 A Declaração de Aplicabilidade (SoA) e a ISO/IEC 27005*, iSO/IEC 27005: Norma que fornece diretrizes especializadas para o processo de avaliação e tratamento de riscos de segurança da informação no suporte ao SGSI.
> - **E)** **Correta.** Conforme fundamentado na seção *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)* deste guia, mitigar / Reduzir ( Risk Mitigation / Reduction ): Implementar controles de segurança (técnicos, administrativos ou físicos) para reduzir a probabilidade e/ou o impacto do risco até patamares aceitáveis (ex.: instalar firewalls, adotar MFA e criptografia). Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/RR/2024) ao estabelecer que "F – V – F".
>
> **Gabarito: E**

---

### Teste 008
**(CEBRASPE – STF – 2008 – Analista Judiciario Suporte Em Tecnologia Da Informacao)**
Se K for uma chave simétrica conhecida apenas pelas entidades X e Y, pode-se garantir a confidencialidade dos dados D e a autenticidade da origem com o seguinte procedimento: 1) X concatena K a D, produzindo M1, e calcula um código de autenticação MAC1 para M1 via função de dispersão (hash); 2) X concatena MAC1 a D e envia-os para Y; 3) Y concatena K a D, produzindo M2; 4) Y calcula o código de autenticação MAC2 para M2, usando a função de dispersão; 5) Y compara MAC1 a MAC2.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Incorreta.** A proposição incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "Se K for uma chave simétrica conhecida apenas pelas entidades X e Y, pode se garantir a confidencialidade dos...". De acordo com a teoria em *1. Princípios Básicos da Segurança da Informação (CIDAN)*, a segurança da informação é definida pela norma ABNT NBR ISO/IEC 27000 como a preservação da confidencialidade, integridade e disponibilidade da informação, admitindo se adicionalmente propriedades vitais para transações formais como a autenticidade e o não repúdio. O mnemônico padronizado em concursos da FCC é CIDAN.
> - **E)** **Correta.** O item está **Errado** (gabarito oficial: **E**), pois contraria a disciplina teórica aplicável.
>
> **Gabarito: E**

---

### Teste 009
**(CEBRASPE – STF – 2008 – Analista Judiciario Suporte Em Tecnologia Da Informacao)**
Osfirewalls baseados em proxies interceptam mensagens de protocolos de aplicação que trafegam entre a rede não- protegida e a protegida. Em uma rede privada conectada à Internet via um firewall baseado em proxies, um dos endereços IP do firewall pode ser visível na Internet.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Correta.** O item está **Certo**. Conforme fundamentado na seção *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade*, vulnerabilidade ( Vulnerability ): Ponto fraco, falha de projeto, brecha de configuração ou deficiência de controle em um ativo que pode ser explorado por uma ameaça. Dessa forma, está plenamente correta a assertiva da banca (CEBRASPE – STF/2008) ao afirmar que "Osfirewalls baseados em proxies interceptam mensagens de protocolos de aplicação que trafegam entre a rede...".
> - **E)** **Incorreta.** A assertiva não incorre em erro conceitual, guardando conformidade com a teoria estudada.
>
> **Gabarito: C**

---

### Teste 010
**(CEBRASPE – STF – 2013 – Analista Judiciario Suporte Em Tecnologia Da Informacao)**
Ataques de negação de serviço distribuído com base em HTTP devem ser mitigados em firewall de camada de aplicação. Nesse caso, se for utilizado o protocolo HTTPS, a mitigação não será possível porque os dados trafegados são cifrados.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Incorreta.** A proposição apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Ataques de negação de serviço distribuído com base em HTTP devem ser mitigados em firewall de camada de...". De acordo com a teoria em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Ataques de negação de serviço (DoS e DDoS), falhas físicas de hardware em servidores e storages, interrupção no fornecimento de energia elétrica, panes nos links de internet e desastres ambientais (enchentes, incêndios em datacenters).
> - **E)** **Correta.** O item está **Errado** (gabarito oficial: **E**), pois contraria a disciplina teórica aplicável.
>
> **Gabarito: E**

---

### Teste 011
**(CEBRASPE – STJ – 2015 – Analista Judiciario Suporte Em Tecnologia Da Informacao)**
Firewalls que utilizam filtros de pacotes sem estados não verificam a parte útil de dados dos pacotes e não guardam o estado das conexões, o que pode impedir que sejam totalmente eficazes.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Correta.** O item está **Certo**. Conforme fundamentado na seção *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade*, vulnerabilidade ( Vulnerability ): Ponto fraco, falha de projeto, brecha de configuração ou deficiência de controle em um ativo que pode ser explorado por uma ameaça. Dessa forma, está plenamente correta a assertiva da banca (CEBRASPE – STJ/2015) ao afirmar que "Firewalls que utilizam filtros de pacotes sem estados não verificam a parte útil de dados dos pacotes e não...".
> - **E)** **Incorreta.** A assertiva não incorre em erro conceitual, guardando conformidade com a teoria estudada.
>
> **Gabarito: C**

---

### Teste 012
**(CEBRASPE – STJ – 2015 – Analista Judiciario Suporte Em Tecnologia Da Informacao)**
Uma vez que a varredura simples de portas é facilmente detectada por firewalls, outros tipos de mensagens passaram a ser utilizadas para mapeamento de serviços de redes, como por exemplo, as de RESET e as de SYN-ACK, que sinalizariam tentativa legítima de conexão, e, ainda, pacotes de resposta DNS (domain name system), que são respostas a mensagens geradas internamente.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Correta.** O item está **Certo**. Conforme fundamentado na seção *4.2 As Quatro Fases do Ciclo de Resposta a Incidentes (NIST SP 800-61)*, ├── Contenção: Isolar nós infectados e bloquear portas (frear o avanço). Dessa forma, está plenamente correta a assertiva da banca (CEBRASPE – STJ/2015) ao afirmar que "Uma vez que a varredura simples de portas é facilmente detectada por firewalls, outros tipos de mensagens...".
> - **E)** **Incorreta.** A assertiva não incorre em erro conceitual, guardando conformidade com a teoria estudada.
>
> **Gabarito: C**

---

### Teste 013
**(CEBRASPE – TJ/DFT – 2015 – Analista Judiciario Suporte Em Tecnologia Da Informacao)**
O acesso direto a registros será eficiente ao se usar funções hash, visto que essas funções garantem uma relação unívoca entre o registro e a sua localização física.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Incorreta.** A proposição apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O acesso direto a registros será eficiente ao se usar funções hash, visto que essas funções garantem uma...". De acordo com a teoria em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, reservada: 5 anos — Autoridades que exerçam funções formais de direção, comando ou chefia — Não admite prorrogação. O prazo cessa impreterivelmente aos 5 anos.
> - **E)** **Correta.** O item está **Errado** (gabarito oficial: **E**), pois contraria a disciplina teórica aplicável.
>
> **Gabarito: E**

---

### Teste 014
**(CEBRASPE – TJ/DFT – 2015 – Analista Judiciario Suporte Em Tecnologia Da Informacao)**
As vantagens dos arquivos hash incluem a otimização no uso do espaço físico em disco.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Incorreta.** A proposição apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "As vantagens dos arquivos hash incluem a otimização no uso do espaço físico em disco". De acordo com a teoria em *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade*, ativo ( Asset ): Qualquer recurso humano, físico, tecnológico ou de informação que possui valor intrínseco para o cumprimento da missão da instituição.
> - **E)** **Correta.** O item está **Errado** (gabarito oficial: **E**), pois contraria a disciplina teórica aplicável.
>
> **Gabarito: E**

---

### Teste 015
**(FCC – TRT 13ª – 2014 – Analista Judiciário - Tecnologia da Informação)**
Atualmente, os firewalls desempenham papel fundamental na proteção da rede local de computadores contra invasões. O analista de tecnologia da informação do TRT da 13a Região deve escolher o tipo de firewall a ser utilizado no Tribunal para que o firewall verifique os pacotes recebidos em busca das informações da camada de rede e da camada de transporte. Esse tipo de firewall é conhecido como de

* **A)** Implementar e Operar o SGSI.
* **B)** Estabelecer o SGSI.
* **C)** Gerenciar o SGSI.
* **D)** Monitorar e Analisar o SGSI.
* **E)** Manter e Melhorar o SGSI.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Implementar e Operar o SGSI". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, mitigar / Reduzir ( Risk Mitigation / Reduction ): Implementar controles de segurança (técnicos, administrativos ou físicos) para reduzir a probabilidade e/ou o impacto do risco até patamares aceitáveis (ex.: instalar firewalls, adotar MFA e criptografia).
> - **B)** **Correta.** Conforme fundamentado na seção *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL* deste guia, a norma ABNT NBR ISO/IEC 27001 estabelece os requisitos formais para estabelecer, implementar, manter e melhorar continuamente um Sistema de Gestão de Segurança da Informação (SGSI). Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 13ª/2014) ao estabelecer que "Estabelecer o SGSI".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Gerenciar o SGSI". De acordo com a teoria estudada em *5.3 A Declaração de Aplicabilidade (SoA) e a ISO/IEC 27005*, iSO/IEC 27005: Norma que fornece diretrizes especializadas para o processo de avaliação e tratamento de riscos de segurança da informação no suporte ao SGSI.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Monitorar e Analisar o SGSI". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, cláusula 4: Contexto da Organização (partes interessadas e escopo do SGSI).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Manter e Melhorar o SGSI". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, aceitar / Reter ( Risk Acceptance / Retention ): Manter o risco no nível atual sem novos controles, mediante aprovação formal fundamentada da alta administração, quando o custo da salvaguarda técnica for superior à perda monetária potencial estimada.
>
> **Gabarito: B**

---

### Teste 016
**(FCC – TRT 15ª – 2015 – Analista Judiciário - Tecnologia da Informação)**
Em uma rede sem fio de computadores (WLAN), as funções de gerenciamento da WLAN são desempenhadas pelo dispositivo comercialmente chamado de Roteador Wireless. Dentre as funções do Roteador está a de designar um endereço IP válido para as mensagens que saem da LAN para a WAN, uma vez que, na LAN, é utilizado um endereço IP virtual. No Roteador, essa função é desempenhada pelo

* **A)** DNS.
* **B)** Gateway.
* **C)** DHCP.
* **D)** Firewall.
* **E)** NAT.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "DNS". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, reservada: 5 anos — Autoridades que exerçam funções formais de direção, comando ou chefia — Não admite prorrogação. O prazo cessa impreterivelmente aos 5 anos.
> - **B)** **Correta.** Conforme fundamentado na seção *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade* deste guia, mecanismos técnicos: Funções criptográficas de espalhamento ( hashing criptográfico como SHA 256 e SHA 512), códigos de autenticação de mensagem (HMAC), assinaturas digitais, somas de verificação ( checksums ) e trilhas de auditoria imutáveis. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 15ª/2015) ao estabelecer que "Gateway".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "DHCP". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Escuta clandestina de rede ( sniffing/eavesdropping ), roubo de dispositivos físicos, engenharia social, vazamento inadvertido de dados fiscais protegidos por sigilo e acessos não autorizados.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Firewall". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Adulteração maliciosa de tabelas contábeis ou salariais em bancos de dados ( tampering ), infecção por malware, ataques man in the middle e erros de transmissão de rede sem checagem de paridade.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "NAT". De acordo com a teoria estudada em *4.1 Métricas do CVSS v3.1 (Common Vulnerability Scoring System)*, exploitability: Vetor de Ataque (AV: Rede, Adjacente, Local, Físico), Complexidade do Ataque (AC: Baixa, Alta), Privilégios Requeridos (PR: Nenhum, Baixo, Alto) e Interação do Usuário (UI: Nenhuma, Requerida).
>
> **Gabarito: B**

---

### Teste 017
**(FCC – TRT 24ª – 2017 – Analista Judiciário - Tecnologia da Informação)**
Desenvolvimento seguro é um requisito para construir um serviço, uma arquitetura, um software e um sistema que respeitem normas de segurança. Dentro de uma política de desenvolvimento seguro, a norma ABNT NBR ISO/IEC 27002:2013 recomenda

* **A)** No SNMP o item a ser monitorado ou gerenciado é um agente. Quem consulta (GET) ou solicita modificações (SET) é um gerente. O agente também tem a função de gerar alertas (TRAP).
* **B)** Dentre as regras do IPTables para configurar o firewall pode-se utilizar o parâmetro "-s ALL", que se aplica simul- taneamente aos três protocolos (SSH, HTTP e HTTPS), sem que seja necessário incluir uma regra separada para cada um.
* **C)** O Zabbix é uma ferramenta de monitoramento de redes, servidores e serviços que não permite monitoramento agentless (sem agentes).
* **D)** Como o servidor Zabbix é obrigatoriamente instalado em sistemas Unix ou Linux, não há agentes Zabbix disponíveis para ambientes Windows e OS.
* **E)** O ICMP, assim como o TCP e o UDP, é um protocolo de controle também usado para a transmissão de dados, que desempenha diversas funções exclusivas para Linux como o ping, para verificar se uma determinada máquina está online.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "No SNMP o item a ser monitorado ou gerenciado é um agente. Quem consulta (GET) ou solicita modificações (SET) é um...". De acordo com a teoria estudada em *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade*, vulnerabilidade ( Vulnerability ): Ponto fraco, falha de projeto, brecha de configuração ou deficiência de controle em um ativo que pode ser explorado por uma ameaça.
> - **B)** **Correta.** Conforme fundamentado na seção *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)* deste guia, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 24ª/2017) ao estabelecer que "Dentre as regras do IPTables para configurar o firewall pode se utilizar o parâmetro " s ALL", que se aplica simul...".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O Zabbix é uma ferramenta de monitoramento de redes, servidores e serviços que não permite monitoramento agentless...". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, a norma ABNT NBR ISO/IEC 27001 estabelece os requisitos formais para estabelecer, implementar, manter e melhorar continuamente um Sistema de Gestão de Segurança da Informação (SGSI).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Como o servidor Zabbix é obrigatoriamente instalado em sistemas Unix ou Linux, não há agentes Zabbix disponíveis...". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, aSSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. ABNT NBR ISO/IEC 27001:2022: Tecnologia da informação — Técnicas de segurança — Sistemas de gestão da segurança da informação — Requisitos. Rio de Janeiro: ABNT, 2022.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O ICMP, assim como o TCP e o UDP, é um protocolo de controle também usado para a transmissão de dados, que...". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Adulteração maliciosa de tabelas contábeis ou salariais em bancos de dados ( tampering ), infecção por malware, ataques man in the middle e erros de transmissão de rede sem checagem de paridade.
>
> **Gabarito: B**

---

### Teste 018
**(FCC – TRT 3ª – 2015 – Analista Judiciário - Tecnologia da Informação)**
Na ITIL v3 atualizada em 2011, o processo responsável por garantir que os serviços de TI atendam às necessidades atuais e futuras de disponibilidade do negócio de uma maneira mais efetiva em custo e mais oportuna é o gerenciamento de disponibilidade que define, analisa, planeja, mede e melhora todos os aspectos da disponibilidade de serviços de TI e garante que todos os processos, infraestruturas, ferramentas, papéis, etc. de TI sejam adequados para as metas de nível de serviço acordadas para disponibilidade. Ele é estabelecido em

* **A)** simétrica, pois apresenta maior velocidade de processamento se comparado ao de chave assimétrica.
* **B)** assimétrica, pois utiliza um algoritmo eficiente e de maior desempenho de processamento se comparado ao de chave simétrica.
* **C)** simétrica devido à facilidade que este apresenta para enviar a chave pela internet de forma segura.
* **D)** assimétrica, pois requer a utilização de duas chaves para criptografar e descriptografar a informação, o que o torna mais seguro que o de chave simétrica.
* **E)** simétrica devido à facilidade que este apresenta para gerenciar grande quantidade de chaves se comparado ao de chave assimétrica.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade* deste guia, propriedade de salvaguardar a exatidão, originalidade e completude da informação e de seus métodos de processamento, impedindo alterações, corrupções ou supressões indevidas ou não autorizadas. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 3ª/2015) ao estabelecer que "simétrica, pois apresenta maior velocidade de processamento se comparado ao de chave assimétrica".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "assimétrica, pois utiliza um algoritmo eficiente e de maior desempenho de processamento se comparado ao de chave...". De acordo com a teoria estudada em *3.2 Análise Qualitativa vs. Análise Quantitativa (SLE, ARO e ALE)*, utiliza escalas ordinais descritivas (ex.: Baixo, Médio, Alto, Crítico) distribuídas em uma Matriz de Probabilidade vs. Impacto.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "simétrica devido à facilidade que este apresenta para enviar a chave pela internet de forma segura". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Ataques de negação de serviço (DoS e DDoS), falhas físicas de hardware em servidores e storages, interrupção no fornecimento de energia elétrica, panes nos links de internet e desastres ambientais (enchentes, incêndios em datacenters).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "assimétrica, pois requer a utilização de duas chaves para criptografar e descriptografar a informação, o que o...". De acordo com a teoria estudada em *2.2 Classificação Corporativa Geral de Ativos*, restrita / Secreta: Nível máximo corporativo (chaves criptográficas mestras de certificados de segurança, senhas de administradores de domínios centrais); divulgação gera dano catastrófico e imediato.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "simétrica devido à facilidade que este apresenta para gerenciar grande quantidade de chaves se comparado ao de...". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, evitar / Eliminar ( Risk Avoidance ): Descontinuar a atividade, processo ou serviço gerador do risco (ex.: desligar e desativar em definitivo um sistema legado vulnerável sem suporte do fabricante).
>
> **Gabarito: A**

---

### Teste 019
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Ciências da Computação, Sistemas de Informação...)**
Um pipeline de dados do TCE-SC processa bilhões de registros de notas fiscais usando Spark SQL. O Auditor nota um problema de desbalanceamento de dados no qual um único executor demora muito mais que os outros para completar uma operação de Join, pois uma chave específica possui muito mais registros que as demais. A seguinte técnica avançada de otimização no Spark 3.x permite ao motor de execução identificar esse desequilíbrio em tempo de execução e dividir a partição sobrecarregada em subtarefas menores:

* **A)** Broadcast Hash Join.
* **B)** Adaptive Query Execution com Skew Join Optimization.
* **C)** Predicate Pushdown.
* **D)** Bucketing com 1024 partições fixas.
* **E)** Cache In-Memory em nível de cluster.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Broadcast Hash Join". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, cláusula 8: Operação (Execução do tratamento de riscos de segurança).
> - **B)** **Correta.** Conforme fundamentado na seção *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade* deste guia, ameaças clássicas: Escuta clandestina de rede ( sniffing/eavesdropping ), roubo de dispositivos físicos, engenharia social, vazamento inadvertido de dados fiscais protegidos por sigilo e acessos não autorizados. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "Adaptive Query Execution com Skew Join Optimization".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Predicate Pushdown". De acordo com a teoria estudada em *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade*, ex.: banco de dados tributário do TCE GO).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Bucketing com 1024 partições fixas". De acordo com a teoria estudada em *3. Gestão e Análise de Riscos de Segurança da Informação*, a gestão de riscos estabelece um processo contínuo e estruturado para identificar incertezas, avaliar a probabilidade de falhas e selecionar salvaguardas economicamente proporcionais.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Cache In Memory em nível de cluster". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, aceitar / Reter ( Risk Acceptance / Retention ): Manter o risco no nível atual sem novos controles, mediante aprovação formal fundamentada da alta administração, quando o custo da salvaguarda técnica for superior à perda monetária potencial estimada.
>
> **Gabarito: B**

---

### Teste 020
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Ciências da Computação, Sistemas de Informação...)**
Um Auditor de TI suspeita que um executável utilizado para cálculos tributários em uma prefeitura possui um backdoor (porta dos fundos). Ele não possui acesso ao código-fonte original. A técnica de auditoria que envolve a análise do código em linguagem Assembly para entender o comportamento do software sem executá-lo, visando identificar trechos maliciosos escondidos, é a(o)

* **A)** Análise Dinâmica com Sandboxing.
* **B)** Fuzzing de interface.
* **C)** Disassembly.
* **D)** Teste de Intrusão (Pentest) Caixa Preta.
* **E)** Verificação de Hash MD5.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Análise Dinâmica com Sandboxing". De acordo com a teoria estudada em *3. Gestão e Análise de Riscos de Segurança da Informação*, a gestão de riscos estabelece um processo contínuo e estruturado para identificar incertezas, avaliar a probabilidade de falhas e selecionar salvaguardas economicamente proporcionais.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Fuzzing de interface". De acordo com a teoria estudada em *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade*, ex.: invasor, tempestade, malware) ex.: porta aberta, ausência de patch).
> - **C)** **Correta.** Conforme fundamentado na seção *4.1 Métricas do CVSS v3.1 (Common Vulnerability Scoring System)* deste guia, o padrão CVSS (mantido pelo FIRST) quantifica a gravidade técnica de vulnerabilidades de software e hardware em uma escala contínua de 0,0 a 10,0. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "Disassembly".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Teste de Intrusão (Pentest) Caixa Preta". De acordo com a teoria estudada em *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade*, ativo ( Asset ): Qualquer recurso humano, físico, tecnológico ou de informação que possui valor intrínseco para o cumprimento da missão da instituição.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Verificação de Hash MD5". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, mecanismos técnicos: Funções criptográficas de espalhamento ( hashing criptográfico como SHA 256 e SHA 512), códigos de autenticação de mensagem (HMAC), assinaturas digitais, somas de verificação ( checksums ) e trilhas de auditoria imutáveis.
>
> **Gabarito: C**

---

## 2. Classificação e Rotulagem da Informação

A classificação atribui rótulos de sensibilidade aos ativos de informação da organização, ditando os níveis de proteção lógica e física a serem aplicados de forma proporcional ao dano decorrente de divulgação ou modificação indevida.

### 2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)

No setor público brasileiro, **a publicidade é a regra geral** e o sigilo é a **exceção expressa** (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam-se em três graus solenes:

```
┌────────────────────────────────────────────────────────────────────────┐
│             GRAUS DE SIGILO E PRAZOS MÁXIMOS DA LAI (LEI 12.527/2011)  │
└────────────────────────────────────────────────────────────────────────┘
  1. ULTRASSECRETA ──► Prazo Máximo: 25 ANOS (Prorrogável 1 única vez por igual período)
  2. SECRETA       ──► Prazo Máximo: 15 ANOS (Não prorrogável além de 15 anos)
  3. RESERVADA     ──► Prazo Máximo:  5 ANOS (Não prorrogável além de 5 anos)
```

| Grau de Sigilo | Prazo Máximo de Restrição | Competência Originária Típica para Classificar | Regime de Prorrogação |
| :--- | :--- | :--- | :--- |
| **Ultrassecreta** | **25 anos** | Presidente da República, Vice-Presidente, Ministros de Estado, Comandantes das Forças Armadas | Prorrogável **uma única vez**, por igual período (totalizando até 50 anos), exclusivamente pela CMRI (*Comissão Mista de Reavaliação de Informações*). |
| **Secreta** | **15 anos** | Titulares de autarquias, fundações e órgãos públicos sob mesma alçada legal | **Não admite prorrogação**. O prazo cessa impreterivelmente aos 15 anos. |
| **Reservada** | **5 anos** | Autoridades que exerçam funções formais de direção, comando ou chefia | **Não admite prorrogação**. O prazo cessa impreterivelmente aos 5 anos. |

> ⚠️ **Alerta de Prova (FCC):**
> Decore rigorosamente os prazos decrescentes: **25 anos $\rightarrow$ 15 anos $\rightarrow$ 5 anos**. A FCC inventa prazos alternativos inexistentes (como 10 ou 20 anos) ou inverte Secreta e Reservada. Além disso, lembre-se: informações relativas à intimidade, vida privada, honra e imagem das pessoas têm restrição de acesso máxima de **até 100 anos** a contar da data de sua produção (Art. 31 da LAI), não se confundindo com prazos de segurança de Estado!

### 2.2 Classificação Corporativa Geral de Ativos

No âmbito corporativo preconizado pela ISO/IEC 27002:

- **Pública:** Informação destinada à divulgação irrestrita (editais de licitação, acórdãos públicos, portal da transparência); o vazamento gera dano nulo.
- **Interna:** Informação para circulação interna restrita aos servidores e colaboradores; divulgação indevida acarreta transtorno administrativo leve.
- **Confidencial:** Informações estratégicas, relatórios preliminares de auditoria em instrução ou dados cadastrais sob sigilo fiscal; vazamento gera dano financeiro ou institucional grave.
- **Restrita / Secreta:** Nível máximo corporativo (chaves criptográficas mestras de certificados de segurança, senhas de administradores de domínios centrais); divulgação gera dano catastrófico e imediato.

---

## 3. Gestão e Análise de Riscos de Segurança da Informação

A gestão de riscos estabelece um processo contínuo e estruturado para identificar incertezas, avaliar a probabilidade de falhas e selecionar salvaguardas economicamente proporcionais.

### 3.1 A Tríade Ativo, Ameaça e Vulnerabilidade

```
      AMEAÇA (Threat)                     VULNERABILIDADE (Vulnerability)
(Causa potencial externa indesejada:    (Fraqueza ou brecha interna explorável:
 ex.: invasor, tempestade, malware)      ex.: porta aberta, ausência de patch)
           │                                             │
           └──────────────────────┬──────────────────────┘
                                  │
                                  ▼
               A Ameaça EXPLORA a Vulnerabilidade
                                  │
                                  ▼
                        ATIVO (Asset) IMPACTADO
              (O que tem valor econômico ou funcional:
               ex.: banco de dados tributário do TCE-GO)
                                  │
                                  ▼
              RISCO = f(PROBABILIDADE, IMPACTO)
```

- **Ativo (*Asset*):** Qualquer recurso humano, físico, tecnológico ou de informação que possui valor intrínseco para o cumprimento da missão da instituição.
- **Ameaça (*Threat*):** Evento ou agente com potencial de causar dano (hackers, desastres naturais, erros acidentais de operadores).
- **Vulnerabilidade (*Vulnerability*):** Ponto fraco, falha de projeto, brecha de configuração ou deficiência de controle em um ativo que pode ser explorado por uma ameaça.
- **Risco Inerente vs. Risco Residual:**
    - *Risco Inerente:* Risco existente em seu estado natural bruto, antes da implementação de qualquer controle protetivo.
    - *Risco Residual:* Risco que subsiste e permanece após o projeto e a entrada em operação dos controles de segurança mitigadores. Deve situar-se estritamente abaixo do **Apetite ao Risco** fixado pela diretoria do tribunal.

### 3.2 Análise Qualitativa vs. Análise Quantitativa (SLE, ARO e ALE)

* **Análise Qualitativa:**
    - Utiliza escalas ordinais descritivas (ex.: Baixo, Médio, Alto, Crítico) distribuídas em uma **Matriz de Probabilidade vs. Impacto**.
    - *Vantagem:* Rápida execução, baixo custo analítico e de fácil compreensão gerencial.
* **Análise Quantitativa:**
    - Mensura as perdas e investimentos em **valores monetários concretos** (R$).
    - **Fórmulas Canônicas Obrigatórias:**
        1. **SLE (*Single Loss Expectancy* - Expectativa de Perda Única):**
           $$\text{SLE} = \text{AV} \times \text{EF}$$
           onde $\text{AV}$ (*Asset Value*) é o valor financeiro do ativo e $\text{EF}$ (*Exposure Factor*) é a fração percentual do valor do ativo perdida em um único incidente (0% a 100%).
        2. **ALE (*Annualized Loss Expectancy* - Expectativa de Perda Anual):**
           $$\text{ALE} = \text{SLE} \times \text{ARO}$$
           onde $\text{ARO}$ (*Annualized Rate of Occurrence*) é a frequência estimada do evento por ano (ex.: 1 incidente a cada 4 anos equivale a $\text{ARO} = 0{,}25$; 2 incidentes por ano equivale a $\text{ARO} = 2$).
        3. **Análise de Custo-Benefício do Controle (CBA):**
           $$\text{Valor do Controle} = (\text{ALE}_{\text{antes}} - \text{ALE}_{\text{depois}}) - \text{ACS}$$
           onde $\text{ACS}$ (*Annualized Cost of Safeguard*) é o custo anual de manutenção do controle. Se o saldo for positivo, o controle de segurança é economicamente viável.

### 3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)

Concluída a avaliação do risco, a organização deve optar formalmente por uma das quatro respostas estratégicas:

1. **Mitigar / Reduzir (*Risk Mitigation / Reduction*):** Implementar controles de segurança (técnicos, administrativos ou físicos) para reduzir a probabilidade e/ou o impacto do risco até patamares aceitáveis (ex.: instalar firewalls, adotar MFA e criptografia).
2. **Aceitar / Reter (*Risk Acceptance / Retention*):** Manter o risco no nível atual sem novos controles, mediante aprovação formal fundamentada da alta administração, quando o custo da salvaguarda técnica for superior à perda monetária potencial estimada.
3. **Transferir / Compartilhar (*Risk Transfer / Sharing*):** Compartilhar a carga financeira ou operacional das perdas com terceiros (ex.: contratação de apólice de seguro contra incidentes cibernéticos ou terceirização da infraestrutura de datacenter para provedores de nuvem sob contratos de SLA estritos).
4. **Evitar / Eliminar (*Risk Avoidance*):** Descontinuar a atividade, processo ou serviço gerador do risco (ex.: desligar e desativar em definitivo um sistema legado vulnerável sem suporte do fabricante).

---

### Teste 021
**(FGV – TCE/GO – 2024 – Analista de Controle Externo - Tecnologia da Informação)**
A ABNT NBR ISO/IEC 27001:2022, NBR ISO/IEC 27002:2022, os CIS v8, SIEM, e a Lei nº 13.709(LGPD) são algumas das diversas normas e leis que trabalham conjuntamente para assegurar a integridade, confidencialidade e disponibilidade dos dados no contexto da segurança da informação. Assinale a opção que descreve corretamente uma contribuição combinada dessas leis e normas.

* **A)** Apenas a implementação da LGPD é suficiente para garantir a conformidade legal e a segurança da informação, tornando as outras normas e controles redundantes.
* **B)** O ponto chave dos Sistemas de Gerenciamento de Informações e Eventos de Segurança (SIEM) oferecer somente práticas de segurança pessoal em tempo real que deve ser combinado as demais normas e leis.
* **C)** As normas ABNT NBR ISO/IEC estabelecem os requisitos gerais de segurança, a LGPD foca na proteção de dados pessoais, e os SIEM proporcionam a visão e controle operacionais necessários.
* **D)** A adoção dos CIS Critical Security Controls v8 cobre os requisitos de segurança e as normas ABNT NBR ISO/IEC fornecem o complemento no que se refere a proteção de dados pessoais.
* **E)** A ABNT NBR ISO/IEC 27001:2022 e a 27002:2022 são as únicas que fornecem uma abordagem baseada em risco que utilizará os outros mecanismos para organizar e controlar os sistemas de segurança.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "Apenas a implementação da LGPD é suficiente para garantir a conformidade legal e a segurança da informação...". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, aSSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. ABNT NBR ISO/IEC 27005:2023: Segurança da informação, segurança cibernética e proteção da privacidade — Gestão de riscos de segurança da informação. Rio de Janeiro: ABNT, 2023.
> - **B)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "O ponto chave dos Sistemas de Gerenciamento de Informações e Eventos de Segurança (SIEM) oferecer somente práticas...". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, a norma ABNT NBR ISO/IEC 27001 estabelece os requisitos formais para estabelecer, implementar, manter e melhorar continuamente um Sistema de Gestão de Segurança da Informação (SGSI).
> - **C)** **Correta.** Conforme fundamentado na seção *🌐 Fontes Oficiais e Referências Bibliográficas* deste guia, aSSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. ABNT NBR ISO/IEC 27001:2022: Tecnologia da informação — Técnicas de segurança — Sistemas de gestão da segurança da informação — Requisitos. Rio de Janeiro: ABNT, 2022. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/GO/2024) ao estabelecer que "As normas ABNT NBR ISO/IEC estabelecem os requisitos gerais de segurança, a LGPD foca na proteção de dados...".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A adoção dos CIS Critical Security Controls v8 cobre os requisitos de segurança e as normas ABNT NBR ISO/IEC...". De acordo com a teoria estudada em *1. Princípios Básicos da Segurança da Informação (CIDAN)*, a segurança da informação é definida pela norma ABNT NBR ISO/IEC 27000 como a preservação da confidencialidade, integridade e disponibilidade da informação, admitindo se adicionalmente propriedades vitais para transações formais como a autenticidade e o não repúdio. O mnemônico padronizado em concursos da FCC é CIDAN.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A ABNT NBR ISO/IEC 27001:2022 e a 27002:2022 são as únicas que fornecem uma abordagem baseada em risco que...". De acordo com a teoria estudada em *5.2 A Nova ISO/IEC 27002 (Edição 2022: 4 Temas e 93 Controles)*, a norma ISO/IEC 27002 constitui um Código de Práticas que detalha diretrizes para implementação dos controles de segurança do Anexo A da ISO 27001. Não é passível de certificação independente.
>
> **Gabarito: C**

---

### Teste 022
**(FGV – TJ/AP – 2023 – Analista Judiciario Apoio Especializado Tecnologia Da Informacao Banco De Dados)**
Fábio pertence ao departamento de segurança da empresa K e está verificando os controles existentes para a Gestão de Riscos de Segurança da Informação. Ele faz uso da norma ABNT NBR ISO/IEC 27005:2011 para efetuar sua verificação. Fábio está examinando o correto funcionamento dos controles existentes. Ele identificou alguns controles obsoletos, que foram descartados, e outros que foram substituídos por controles melhores ou mais modernos. Nesse momento, Fábio está fazendo uso da tarefa dentro de identificação de riscos:

* **A)** dos ativos;
* **B)** das ameaças;
* **C)** de controles existentes;
* **D)** das vulnerabilidades;
* **E)** de consequências.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "dos ativos". De acordo com a teoria estudada em *5.2 A Nova ISO/IEC 27002 (Edição 2022: 4 Temas e 93 Controles)*, cONTROLES ORGANIZACIONAIS (37 controles) ──► Políticas, gestão de ativos,.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "das ameaças". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, a norma ABNT NBR ISO/IEC 27001 estabelece os requisitos formais para estabelecer, implementar, manter e melhorar continuamente um Sistema de Gestão de Segurança da Informação (SGSI).
> - **C)** **Correta.** Conforme fundamentado na seção *🌐 Fontes Oficiais e Referências Bibliográficas* deste guia, aSSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. ABNT NBR ISO/IEC 27005:2023: Segurança da informação, segurança cibernética e proteção da privacidade — Gestão de riscos de segurança da informação. Rio de Janeiro: ABNT, 2023. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/AP/2023) ao estabelecer que "de controles existentes".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "das vulnerabilidades". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, aSSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. ABNT NBR ISO/IEC 27001:2022: Tecnologia da informação — Técnicas de segurança — Sistemas de gestão da segurança da informação — Requisitos. Rio de Janeiro: ABNT, 2022.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "de consequências". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, mitigar / Reduzir ( Risk Mitigation / Reduction ): Implementar controles de segurança (técnicos, administrativos ou físicos) para reduzir a probabilidade e/ou o impacto do risco até patamares aceitáveis (ex.: instalar firewalls, adotar MFA e criptografia).
>
> **Gabarito: C**

---

### Teste 023
**(FCC – TRT 6ª – 2012 – Analista Judiciário - Apoio Especializado/Tecnologia da Informação)**
Segundo a ISO/IEC 27001, em relação à Provisão de Recursos, a organização deve determinar e prover os recursos necessários para

* **A)** avaliar a necessidade de ações para assegurar que as não conformidades não ocorram.
* **B)** identificar os impactos que as perdas de confidencialidade, integridade e disponibilidade podem causar aos ativos.
* **C)** transferir os riscos associados ao negócio a outras partes, por exemplo, seguradoras e fornecedores.
* **D)** estabelecer, implementar, operar, monitorar, analisar criticamente, manter e melhorar um SGSI.
* **E)** desenvolver critérios para a aceitação de riscos e identificar níveis aceitáveis de risco.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "avaliar a necessidade de ações para assegurar que as não conformidades não ocorram". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, cláusula 10: Melhoria (Não conformidades, ações corretivas e ciclo contínuo).
> - **B)** **Correta.** Conforme fundamentado na seção *4.1 Métricas do CVSS v3.1 (Common Vulnerability Scoring System)* deste guia, impact: Impactos na Confidencialidade (C), Integridade (I) e Disponibilidade (A). Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 6ª/2012) ao estabelecer que "identificar os impactos que as perdas de confidencialidade, integridade e disponibilidade podem causar aos ativos".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "transferir os riscos associados ao negócio a outras partes, por exemplo, seguradoras e fornecedores". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, garantia de que a informação, os sistemas computacionais e os ativos de telecomunicações associados estejam acessíveis e utilizáveis sob demanda pelos usuários autorizados sempre que necessário.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "estabelecer, implementar, operar, monitorar, analisar criticamente, manter e melhorar um SGSI". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, a norma ABNT NBR ISO/IEC 27001 estabelece os requisitos formais para estabelecer, implementar, manter e melhorar continuamente um Sistema de Gestão de Segurança da Informação (SGSI).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "desenvolver critérios para a aceitação de riscos e identificar níveis aceitáveis de risco". De acordo com a teoria estudada em *2. Classificação e Rotulagem da Informação*, a classificação atribui rótulos de sensibilidade aos ativos de informação da organização, ditando os níveis de proteção lógica e física a serem aplicados de forma proporcional ao dano decorrente de divulgação ou modificação indevida.
>
> **Gabarito: B**

---

### Teste 024
**(CEBRASPE – STJ – 2015 – Analista Judiciario Suporte Em Tecnologia Da Informacao)**
De acordo com a norma ISO 27005, na estimativa de riscos, podem ser aplicadas metodologias qualitativas para a identificação de riscos.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Correta.** O item está **Certo**. Conforme fundamentado na seção *5.3 A Declaração de Aplicabilidade (SoA) e a ISO/IEC 27005*, iSO/IEC 27005: Norma que fornece diretrizes especializadas para o processo de avaliação e tratamento de riscos de segurança da informação no suporte ao SGSI. Dessa forma, está plenamente correta a assertiva da banca (CEBRASPE – STJ/2015) ao afirmar que "De acordo com a norma ISO 27005, na estimativa de riscos, podem ser aplicadas metodologias qualitativas para...".
> - **E)** **Incorreta.** A assertiva não incorre em erro conceitual, guardando conformidade com a teoria estudada.
>
> **Gabarito: C**

---

### Teste 025
**(CEBRASPE – TJ/DFT – 2015 – Analista Judiciario Suporte Em Tecnologia Da Informacao)**
De acordo com a IN n.º 4 MPOG/SLTI, a gestão de processos de TI, que inclui a gestão de segurança da informação, não poderá ser objeto de contratação, salvo se aprovado pela autoridade máxima do órgão ou entidade, e desde que esteja Julgue o item a seguir com relação à norma ISO 27005.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Incorreta.** A proposição apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "De acordo com a IN n.º 4 MPOG/SLTI, a gestão de processos de TI, que inclui a gestão de segurança da...". De acordo com a teoria em *🌐 Fontes Oficiais e Referências Bibliográficas*, nIST SP 800 30 Rev. 1 Guide for Conducting Risk Assessments Guia metodológico oficial para condução de processos de avaliação e gestão de riscos em segurança da informação.
> - **E)** **Correta.** O item está **Errado** (gabarito oficial: **E**), pois contraria a disciplina teórica aplicável.
>
> **Gabarito: E**

---

### Teste 026
**(FCC – TRT 24ª – 2017 – Analista Judiciário - Tecnologia da Informação)**
Considere os processos abaixo. Processos do SGSI Processos de GRSI − Planejar. − Definição do contexto. − Executar. − Avaliação de riscos. − Verificar. − Definição do plano de tratamento do risco. − Agir. − Aceitação do risco. − Implementação do plano de tratamento do risco. − Monitoramento contínuo e análise crítica de riscos. − Manter e melhorar o processo de GRSI. A norma ABNT NBR ISO/IEC 27005:2011 apresenta o alinhamento do processo do Sistema de Gestão da Segurança da In- formação – SGSI e do processo de Gestão de Riscos de Segurança da Informação – GRSI. Segundo a Norma, o processo de GRSI denominado

* **A)** no JBoss EAP 6 a fonte de dados é configurada no arquivo de configuração do servidor. Caso a instância do JBoss EAP estiver sendo executada como servidor autônomo, a fonte de dados é configurada no arquivo standalone/ configuration/standalone.xml.
* **B)** o JBoss Messaging passou a ser incluído no JBoss EAP 6, já que o JBoss EAP 5 usava o HornetQ como provedor messaging.
* **C)** no JBoss EAP 5 a arquitetura de carregamento de classe era baseado nos JBoss Modules, mas no JBoss EAP6, o carregamento de classe é hierárquico, ocultando as classes de implementação do servidor e carregando apenas as classes que o aplicativo necessita.
* **D)** no JBoss EAP 5, o servidor podia ser executado em um managed domain, mas no JBoss EAP 6 executa como um servidor autônomo, permitindo configurar todos os grupos dos servidores de uma só vez, mantendo as configurações sincronizadas por toda a rede de servidores.
* **E)** o JBoss EAP 5 usava perfis baseados na configuração de implantação, localizados no diretório EAP_HOME/ configuration/. No JBoss EAP 6, a configuração da implantação é feita usando um arquivo e um servidor autônomo, que é configurado usando o arquivo EAP_HOME/domain/server/domain.xml.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "no JBoss EAP 6 a fonte de dados é configurada no arquivo de configuração do servidor. Caso a instância do JBoss...". De acordo com a teoria estudada em *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade*, vulnerabilidade ( Vulnerability ): Ponto fraco, falha de projeto, brecha de configuração ou deficiência de controle em um ativo que pode ser explorado por uma ameaça.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "o JBoss Messaging passou a ser incluído no JBoss EAP 6, já que o JBoss EAP 5 usava o HornetQ como provedor...". De acordo com a teoria estudada em *5.3 A Declaração de Aplicabilidade (SoA) e a ISO/IEC 27005*, iSO/IEC 27005: Norma que fornece diretrizes especializadas para o processo de avaliação e tratamento de riscos de segurança da informação no suporte ao SGSI.
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "no JBoss EAP 5 a arquitetura de carregamento de classe era baseado nos JBoss Modules, mas no JBoss EAP6, o...". De acordo com a teoria estudada em *5.2 A Nova ISO/IEC 27002 (Edição 2022: 4 Temas e 93 Controles)*, a norma ISO/IEC 27002 constitui um Código de Práticas que detalha diretrizes para implementação dos controles de segurança do Anexo A da ISO 27001. Não é passível de certificação independente.
> - **D)** **Correta.** Conforme fundamentado na seção *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL* deste guia, a norma ABNT NBR ISO/IEC 27001 estabelece os requisitos formais para estabelecer, implementar, manter e melhorar continuamente um Sistema de Gestão de Segurança da Informação (SGSI). Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 24ª/2017) ao estabelecer que "no JBoss EAP 5, o servidor podia ser executado em um managed domain, mas no JBoss EAP 6 executa como um servidor...".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "o JBoss EAP 5 usava perfis baseados na configuração de implantação, localizados no diretório EAP HOME/...". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, aSSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. ABNT NBR ISO/IEC 27005:2023: Segurança da informação, segurança cibernética e proteção da privacidade — Gestão de riscos de segurança da informação. Rio de Janeiro: ABNT, 2023.
>
> **Gabarito: D**

---

### Teste 027
**(FCC – TRT 3ª – 2015 – Analista Judiciário - Tecnologia da Informação)**
Um analista de TI está utilizando as recomendações da norma ABNT NBR ISO/IEC 27005:2011 para realizar o tratamento de riscos dentro do processo de gestão de riscos de segurança da informação. Nesse contexto, a norma recomenda que

* **A)** as opções de tratamento do risco sejam selecionadas apenas com base no resultado do processo de avaliação de riscos e no custo esperado para implementações dessas opções.
* **B)** as quatro opções para tratamento do risco sejam aplicadas de forma mutuamente exclusiva, ou seja, não combinadas.
* **C)** as opções de tratamento do risco sejam consideradas levando-se em conta como o risco é percebido pelas partes afeta- das e as formas mais apropriadas de comunicação com estas partes.
* **D)** as consequências adversas do risco sejam reduzidas ao mínimo possível de acordo com critérios absolutos, como a proba- bilidade do risco, pois riscos mais prováveis devem ser os primeiros a serem considerados.
* **E)** um plano de tratamento de riscos seja definido identificando os riscos mais prováveis, as formas de tratar estes riscos, independente das prioridades, e os prazos de execução das ações de tratamento de risco indicadas.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "as opções de tratamento do risco sejam selecionadas apenas com base no resultado do processo de avaliação de...". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, evitar / Eliminar ( Risk Avoidance ): Descontinuar a atividade, processo ou serviço gerador do risco (ex.: desligar e desativar em definitivo um sistema legado vulnerável sem suporte do fabricante).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "as quatro opções para tratamento do risco sejam aplicadas de forma mutuamente exclusiva, ou seja, não combinadas". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, mitigar / Reduzir ( Risk Mitigation / Reduction ): Implementar controles de segurança (técnicos, administrativos ou físicos) para reduzir a probabilidade e/ou o impacto do risco até patamares aceitáveis (ex.: instalar firewalls, adotar MFA e criptografia).
> - **C)** **Correta.** Conforme fundamentado na seção *5.3 A Declaração de Aplicabilidade (SoA) e a ISO/IEC 27005* deste guia, iSO/IEC 27005: Norma que fornece diretrizes especializadas para o processo de avaliação e tratamento de riscos de segurança da informação no suporte ao SGSI. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 3ª/2015) ao estabelecer que "as opções de tratamento do risco sejam consideradas levando se em conta como o risco é percebido pelas partes...".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "as consequências adversas do risco sejam reduzidas ao mínimo possível de acordo com critérios absolutos, como a...". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, aSSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. ABNT NBR ISO/IEC 27005:2023: Segurança da informação, segurança cibernética e proteção da privacidade — Gestão de riscos de segurança da informação. Rio de Janeiro: ABNT, 2023.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "um plano de tratamento de riscos seja definido identificando os riscos mais prováveis, as formas de tratar estes...". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, cláusula 8: Operação (Execução do tratamento de riscos de segurança).
>
> **Gabarito: C**

---

## 4. Gestão de Vulnerabilidades e Resposta a Incidentes

### 4.1 Métricas do CVSS v3.1 (Common Vulnerability Scoring System)

O padrão CVSS (mantido pelo FIRST) quantifica a gravidade técnica de vulnerabilidades de software e hardware em uma escala contínua de **0,0 a 10,0**:

- **Métricas de Base (*Base Metrics*):** Qualidades intrínsecas e imutáveis da falha:
    - *Exploitability:* Vetor de Ataque (AV: Rede, Adjacente, Local, Físico), Complexidade do Ataque (AC: Baixa, Alta), Privilégios Requeridos (PR: Nenhum, Baixo, Alto) e Interação do Usuário (UI: Nenhuma, Requerida).
    - *Impact:* Impactos na Confidencialidade (C), Integridade (I) e Disponibilidade (A).
    - *Scope (S):* Escopo Inalterado (*Unchanged*) ou Alterado (*Changed*, quando a falha compromete recursos fora de sua camada de autorização).
- **Faixas de Gravidade CVSS v3.1:**
    - `0.0`: Nenhuma (*None*)
    - `0.1` a `3.9`: Baixa (*Low*)
    - `4.0` a `6.9`: Média (*Medium*)
    - `7.0` a `8.9`: Alta (*High*)
    - `9.0` a `10.0`: Crítica (*Critical*)

### 4.2 As Quatro Fases do Ciclo de Resposta a Incidentes (NIST SP 800-61)

O tratamento de incidentes cibernéticos adota o ciclo formalizado no guia NIST SP 800-61 Rev. 2:

```
┌────────────────────────────────────────────────────────────────────────┐
│             CICLO DE RESPOSTA A INCIDENTES (NIST SP 800-61 REV. 2)     │
└────────────────────────────────────────────────────────────────────────┘
  [1. PREPARAÇÃO] ──► Treinamento do CSIRT, ferramentas forenses e políticas
         │
         ▼
  [2. DETECÇÃO E ANÁLISE] ──► Análise de logs do SIEM, alertas e confirmação do ataque
         │
         ▼
  [3. CONTENÇÃO, ERRADICAÇÃO E RECUPERAÇÃO]
         ├── Contenção: Isolar nós infectados e bloquear portas (frear o avanço)
         ├── Erradicação: Eliminar malwares e sanear senhas violadas
         └── Recuperação: Restaurar backups íntegros e retornar à operação normal
         │
         ▼
  [4. ATIVIDADES PÓS-INCIDENTE] ──► Reunião de Lições Aprendidas e melhorias
         │
         └───────────► Realimenta a Fase 1 (Preparação Contínua)
```

1. **Preparação (*Preparation*):** Estabelecimento e capacitação da equipe técnica de resposta (CSIRT / CERT), aquisição de ferramentas de investigação forense, implantação de políticas e planos de comunicação.
2. **Detecção e Análise (*Detection and Analysis*):** Monitoramento contínuo de alertas de IDS/IPS, antivírus/EDR e correlação de logs em SIEM para constatar indícios de comprometimento (*IoCs*) e dimensionar o alcance do ataque.
3. **Contenção, Erradicação e Recuperação (*Containment, Eradication and Recovery*):**
    - *Contenção:* Ação emergencial prioritária voltada a **estancar a disseminação do ataque e limitar o raio de destruição** (*blast radius*), tal como isolar a máquina da rede, desconectar cabos ou bloquear portas de switches.
    - *Erradicação:* Expurgar o agente agressor (remover malwares, fechar brechas de software e alterar credenciais comprometidas).
    - *Recuperação:* Restaurar sistemas para operação produtiva plena utilizando cópias seguras de backup, testando sua estabilidade.

4. **Atividades Pós-Incidente (*Post-Incident Activity / Lessons Learned*):** Reunião formal de **Lições Aprendidas** para documentar como o incidente foi tratado, registrar métricas temporais e aprimorar as salvaguardas da fase de preparação.

---

### Teste 028
**(FGV – TCE/GO – 2024 – Analista de Controle Externo - Tecnologia da Informação)**
Assinale a opção correta sobre a segurança de redes de computadores.

* **A)** Os sistemas de detecção de intrusão (IDS) e os sistemas de prevenção de intrusão (IPS) são ferramentas com a mesma função
* **B)** Gestão de vulnerabilidades é um processo para correção de vulnerabilidades em softwares, não tendo relação direta com o firewall.
* **C)** Um sistema de detecção de intrusão (IDS) não funciona numa DMZ (Demilitarized Zone), pois ela necessita de visibilidade completa da rede.
* **D)** O uso de NAC (Network Access Control) não contribui para a gestão de vulnerabilidades.
* **E)** Os Sistemas de detecção de intrusão (IDS) são projetados para monitorar e alertar sobre possíveis intrusões, enquanto sistemas de prevenção de intrusão (IPS) atuam ativamente para bloquear ataques detectados.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Os sistemas de detecção de intrusão (IDS) e os sistemas de prevenção de intrusão (IPS) são ferramentas com a mesma...". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, mecanismos técnicos: Criptografia em trânsito (TLS) e em repouso (TDE), controle de acesso lógico baseado em papéis (RBAC), mascaramento dinâmico de dados e soluções de Prevenção contra Perda de Dados ( DLP Data Loss Prevention ).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Gestão de vulnerabilidades é um processo para correção de vulnerabilidades em softwares, não tendo relação direta...". De acordo com a teoria estudada em *3. Gestão e Análise de Riscos de Segurança da Informação*, a gestão de riscos estabelece um processo contínuo e estruturado para identificar incertezas, avaliar a probabilidade de falhas e selecionar salvaguardas economicamente proporcionais.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Um sistema de detecção de intrusão (IDS) não funciona numa DMZ (Demilitarized Zone), pois ela necessita de...". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Adulteração maliciosa de tabelas contábeis ou salariais em bancos de dados ( tampering ), infecção por malware, ataques man in the middle e erros de transmissão de rede sem checagem de paridade.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O uso de NAC (Network Access Control) não contribui para a gestão de vulnerabilidades". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, aSSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. ABNT NBR ISO/IEC 27001:2022: Tecnologia da informação — Técnicas de segurança — Sistemas de gestão da segurança da informação — Requisitos. Rio de Janeiro: ABNT, 2022.
> - **E)** **Correta.** Conforme fundamentado na seção *4.2 As Quatro Fases do Ciclo de Resposta a Incidentes (NIST SP 800-61)* deste guia, detecção e Análise ( Detection and Analysis ): Monitoramento contínuo de alertas de IDS/IPS, antivírus/EDR e correlação de logs em SIEM para constatar indícios de comprometimento ( IoCs ) e dimensionar o alcance do ataque. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/GO/2024) ao estabelecer que "Os Sistemas de detecção de intrusão (IDS) são projetados para monitorar e alertar sobre possíveis intrusões...".
>
> **Gabarito: E**

---

### Teste 029
**(FGV – TRF/1 – 2024 – Analista Judiciario Area Apoio Especializado Especialidade Tecnologia Da Informacao)**
Fabrício, delegado de polícia, solicitou a intervenção de um especialista em informática para investigar um incidente ocorrido em uma empresa, no qual João, um ex-funcionário, acessou indevidamente o sistema da empresa, que continha dados confidenciais. Durante essa invasão, João procedeu à modificação dos preços dos produtos, reduzindo-os a valores insignificantes, e distribuiu essas informações para milhares de indivíduos, ocasionando uma interrupção temporária no funcionamento do sistema. Após uma minuciosa análise da situação, o perito elaborou um relatório abrangente para o delegado Fabrício, no qual apontou os objetivos fundamentais de segurança que foram violados. A alternativa que lista os objetivos fundamentais de segurança que foram violados, na ordem em que as respectivas violações aparecem no texto acima, é:

* **A)** não repúdio, integridade e disponibilidade;
* **B)** disponibilidade, integridade e confidencialidade;
* **C)** confidencialidade, Integridade e disponibilidade;
* **D)** não repúdio, disponibilidade e confidencialidade;
* **E)** confidencialidade, disponibilidade e não repúdio.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "não repúdio, integridade e disponibilidade". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Ataques de negação de serviço (DoS e DDoS), falhas físicas de hardware em servidores e storages, interrupção no fornecimento de energia elétrica, panes nos links de internet e desastres ambientais (enchentes, incêndios em datacenters).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "disponibilidade, integridade e confidencialidade". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Escuta clandestina de rede ( sniffing/eavesdropping ), roubo de dispositivos físicos, engenharia social, vazamento inadvertido de dados fiscais protegidos por sigilo e acessos não autorizados.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "confidencialidade, Integridade e disponibilidade". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, mecanismos técnicos: Criptografia em trânsito (TLS) e em repouso (TDE), controle de acesso lógico baseado em papéis (RBAC), mascaramento dinâmico de dados e soluções de Prevenção contra Perda de Dados ( DLP Data Loss Prevention ).
> - **D)** **Correta.** Conforme fundamentado na seção *1. Princípios Básicos da Segurança da Informação (CIDAN)* deste guia, a segurança da informação é definida pela norma ABNT NBR ISO/IEC 27000 como a preservação da confidencialidade, integridade e disponibilidade da informação, admitindo se adicionalmente propriedades vitais para transações formais como a autenticidade e o não repúdio. O mnemônico padronizado em concursos da FCC é CIDAN. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRF/1/2024) ao estabelecer que "não repúdio, disponibilidade e confidencialidade".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "confidencialidade, disponibilidade e não repúdio". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Adulteração maliciosa de tabelas contábeis ou salariais em bancos de dados ( tampering ), infecção por malware, ataques man in the middle e erros de transmissão de rede sem checagem de paridade.
>
> **Gabarito: D**

---

### Teste 030
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Ciência de Dados)**
O TCE-PA deseja fortalecer (hardening) a segurança de suas estações de trabalho para proteger contra diversas ameaças. As ações que devem ser tomadas pelo tribunal incluem

* **A)** implementar hardening e ignorar a aplicação de patches.
* **B)** usar apenas antivírus e firewall.
* **C)** aplicar políticas de senhas fortes e monitorar vulnerabilidades em serviços.
* **D)** desativar o IPS e focar apenas em hardening.
* **E)** evitar a implementação de políticas de senhas e confiar somente em firewalls.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "implementar hardening e ignorar a aplicação de patches". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, mitigar / Reduzir ( Risk Mitigation / Reduction ): Implementar controles de segurança (técnicos, administrativos ou físicos) para reduzir a probabilidade e/ou o impacto do risco até patamares aceitáveis (ex.: instalar firewalls, adotar MFA e criptografia).
> - **B)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "usar apenas antivírus e firewall". De acordo com a teoria estudada em *4.1 Métricas do CVSS v3.1 (Common Vulnerability Scoring System)*, o padrão CVSS (mantido pelo FIRST) quantifica a gravidade técnica de vulnerabilidades de software e hardware em uma escala contínua de 0,0 a 10,0.
> - **C)** **Correta.** Conforme fundamentado na seção *2.2 Classificação Corporativa Geral de Ativos* deste guia, restrita / Secreta: Nível máximo corporativo (chaves criptográficas mestras de certificados de segurança, senhas de administradores de domínios centrais); divulgação gera dano catastrófico e imediato. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "aplicar políticas de senhas fortes e monitorar vulnerabilidades em serviços".
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "desativar o IPS e focar apenas em hardening". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, evitar / Eliminar ( Risk Avoidance ): Descontinuar a atividade, processo ou serviço gerador do risco (ex.: desligar e desativar em definitivo um sistema legado vulnerável sem suporte do fabricante).
> - **E)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "evitar a implementação de políticas de senhas e confiar somente em firewalls". De acordo com a teoria estudada em *5.2 A Nova ISO/IEC 27002 (Edição 2022: 4 Temas e 93 Controles)*, a norma ISO/IEC 27002 constitui um Código de Práticas que detalha diretrizes para implementação dos controles de segurança do Anexo A da ISO 27001. Não é passível de certificação independente.
>
> **Gabarito: C**

---

## 5. Família de Normas ISO/IEC 27000 (SGSI)

### 5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL

A norma **ABNT NBR ISO/IEC 27001** estabelece os requisitos formais para estabelecer, implementar, manter e melhorar continuamente um Sistema de Gestão de Segurança da Informação (SGSI).

- **Certificação:** É a **única norma auditável e formalmente certificável** da família para organizações.
- **Estrutura Harmonizada (Anexo SL - Cláusulas 4 a 10):**
    - *Cláusula 4:* Contexto da Organização (partes interessadas e escopo do SGSI)
    - *Cláusula 5:* Liderança e Comprometimento da Alta Direção
    - *Cláusula 6:* Planejamento (Tratamento de riscos e objetivos de segurança)
    - *Cláusula 7:* Apoio (Recursos, capacitação, conscientização e comunicação)
    - *Cláusula 8:* Operação (Execução do tratamento de riscos de segurança)
    - *Cláusula 9:* Avaliação de Desempenho (Auditorias internas e análise pela direção)
    - *Cláusula 10:* Melhoria (Não conformidades, ações corretivas e ciclo contínuo)
- **Melhoria Contínua:** Opera tradicionalmente alicerçada no ciclo **PDCA** (*Plan, Do, Check, Act*).

### 5.2 A Nova ISO/IEC 27002 (Edição 2022: 4 Temas e 93 Controles)

A norma **ISO/IEC 27002** constitui um Código de Práticas que detalha diretrizes para implementação dos controles de segurança do Anexo A da ISO 27001. **Não é passível de certificação independente**.
A edição atualizada (ISO/IEC 27002:2022) simplificou os antigos 14 domínios da versão 2013, reorganizando os controles em **4 grandes temas integrados, totalizando 93 controles**:

```
┌────────────────────────────────────────────────────────────────────────┐
│             ESTRUTURA DOS CONTROLES DA ISO/IEC 27002:2022              │
└────────────────────────────────────────────────────────────────────────┘
  1. CONTROLES ORGANIZACIONAIS (37 controles) ──► Políticas, gestão de ativos,
                                                  classificação, governança
  2. CONTROLES DE PESSOAS     ( 8 controles) ──► Recrutamento, trabalho remoto,
                                                  termos de sigilo, treinamento
  3. CONTROLES FÍSICOS        (14 controles) ──► Perímetro, salas seguras,
                                                  cabeamento, descarte de mídias
  4. CONTROLES TECNOLÓGICOS   (34 controles) ──► Autenticação, controle de acesso,
                                                  criptografia, logs e redes
```

### 5.3 A Declaração de Aplicabilidade (SoA) e a ISO/IEC 27005

- **Declaração de Aplicabilidade (SoA - *Statement of Applicability*):**
  Documento formal obrigatório exigido pela ISO/IEC 27001 no qual a organização lista todos os controles de segurança do Anexo A, declarando:

    1. Se cada controle foi considerado aplicável ou não ao escopo do SGSI;
    2. A justificativa técnica para inclusão de cada controle aplicável;
    3. O estado atual de implementação dos controles;
    4. A **justificativa formal obrigatória para a exclusão** de qualquer controle que não tenha sido adotado.

- **ISO/IEC 27005:** Norma que fornece diretrizes especializadas para o processo de avaliação e tratamento de riscos de segurança da informação no suporte ao SGSI.

---

### Teste 031
**(CEBRASPE – STJ – 2015 – Analista Judiciario Suporte Em Tecnologia Da Informacao)**
De acordo com a norma ISO 27001, o sistema de gerenciamento da segurança da informação deve ser revisado regularmente, considerando-se as sugestões e os feedbacks das partes interessadas.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Correta.** O item está **Certo**. Conforme fundamentado na seção *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, cláusula 4: Contexto da Organização (partes interessadas e escopo do SGSI). Dessa forma, está plenamente correta a assertiva da banca (CEBRASPE – STJ/2015) ao afirmar que "De acordo com a norma ISO 27001, o sistema de gerenciamento da segurança da informação deve ser revisado...".
> - **E)** **Incorreta.** A assertiva não incorre em erro conceitual, guardando conformidade com a teoria estudada.
>
> **Gabarito: C**

---

### Teste 032
**(FCC – TRT 15ª – 2015 – Analista Judiciário - Tecnologia da Informação)**
Segundo a norma ISO 27001 de 2006, a Segurança da Informação é um conjunto de medidas que visam proteger e preservar informações e sistemas de informações, assegurando-lhes algumas qualidades, EXCETO a

* **A)** autenticidade.
* **B)** disponibilidade.
* **C)** irretratabilidade.
* **D)** compatibilidade.
* **E)** integridade.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "autenticidade". De acordo com a teoria estudada em *1. Princípios Básicos da Segurança da Informação (CIDAN)*, a segurança da informação é definida pela norma ABNT NBR ISO/IEC 27000 como a preservação da confidencialidade, integridade e disponibilidade da informação, admitindo se adicionalmente propriedades vitais para transações formais como a autenticidade e o não repúdio. O mnemônico padronizado em concursos da FCC é CIDAN.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "disponibilidade". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, garantia de que a informação, os sistemas computacionais e os ativos de telecomunicações associados estejam acessíveis e utilizáveis sob demanda pelos usuários autorizados sempre que necessário.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "irretratabilidade". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, a norma ABNT NBR ISO/IEC 27001 estabelece os requisitos formais para estabelecer, implementar, manter e melhorar continuamente um Sistema de Gestão de Segurança da Informação (SGSI).
> - **D)** **Correta.** Conforme fundamentado na seção *🌐 Fontes Oficiais e Referências Bibliográficas* deste guia, aSSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. ABNT NBR ISO/IEC 27001:2022: Tecnologia da informação — Técnicas de segurança — Sistemas de gestão da segurança da informação — Requisitos. Rio de Janeiro: ABNT, 2022. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 15ª/2015) ao estabelecer que "compatibilidade".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "integridade". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, mecanismos técnicos: Redundância de hardware e fontes de alimentação, clusters de alta disponibilidade (HA ativo ativo ou ativo passivo), sistemas anti DDoS, geradores e nobreaks comutáveis, planos de continuidade de negócios (PCN/DRP) e rotinas estruturadas de backup.
>
> **Gabarito: D**

---

## 🌐 Fontes Oficiais e Referências Bibliográficas

* [NIST Cybersecurity Framework (CSF 2.0)](https://www.nist.gov/cyberframework) - Estrutura de referência global do NIST para identificação, proteção, detecção, resposta e recuperação de riscos cibernéticos.
* [NIST SP 800-30 Rev. 1 - Guide for Conducting Risk Assessments](https://csrc.nist.gov/pubs/sp/800/30/r1/final) - Guia metodológico oficial para condução de processos de avaliação e gestão de riscos em segurança da informação.
* [NIST SP 800-37 Rev. 2 - Risk Management Framework](https://csrc.nist.gov/pubs/sp/800/37/r2/final) - Diretrizes para aplicação do Risk Management Framework (RMF) aos sistemas e organizações.
* [Governo Digital - Programa de Privacidade e Segurança da Informação (PPSI 2.0)](https://www.gov.br/governodigital/pt-br/privacidade-e-seguranca/ppsi-2.0) - Diretrizes, requisitos de maturidade e gestão de riscos cibernéticos para a administração pública.
* [Decreto Federal nº 9.637/2018 (Política Nacional de Segurança da Informação)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/decreto/d9637.htm) - Institui a PNSI, dispondo sobre governança, gestão de riscos e tratamento de incidentes de segurança da informação.
* ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **ABNT NBR ISO/IEC 27001:2022**: Tecnologia da informação — Técnicas de segurança — Sistemas de gestão da segurança da informação — Requisitos. Rio de Janeiro: ABNT, 2022.
* ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **ABNT NBR ISO/IEC 27005:2023**: Segurança da informação, segurança cibernética e proteção da privacidade — Gestão de riscos de segurança da informação. Rio de Janeiro: ABNT, 2023.
* STALLINGS, William. **Criptografia e Segurança de Redes: Princípios e Práticas**. 7. ed. São Paulo: Pearson Education do Brasil, 2018. (Cap. 1 - Visão Geral de Segurança da Informação).
