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
- [1. Princípios Básicos da Segurança da Informação (CIDAN)](#1-principios-basicos-da-seguranca-da-informacao-cidan)
    - [1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade](#11-os-pilares-fundamentais-confidencialidade-integridade-e-disponibilidade)
    - [1.2 Autenticidade, Não Repúdio e Atributos Complementares](#12-autenticidade-nao-repudio-e-atributos-complementares)
- [2. Classificação e Rotulagem da Informação](#2-classificacao-e-rotulagem-da-informacao)
    - [2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)](#21-graus-de-sigilo-no-setor-publico-lei-de-acesso-a-informacao-lei-no-125272011)
    - [2.2 Classificação Corporativa Geral de Ativos](#22-classificacao-corporativa-geral-de-ativos)
- [3. Gestão e Análise de Riscos de Segurança da Informação](#3-gestao-e-analise-de-riscos-de-seguranca-da-informacao)
    - [3.1 A Tríade Ativo, Ameaça e Vulnerabilidade](#31-a-triade-ativo-ameaca-e-vulnerabilidade)
    - [3.2 Análise Qualitativa vs. Análise Quantitativa (SLE, ARO e ALE)](#32-analise-qualitativa-vs-analise-quantitativa-sle-aro-e-ale)
    - [3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)](#33-as-quatro-estrategias-de-tratamento-do-risco-isoiec-27005)
- [4. Gestão de Vulnerabilidades e Resposta a Incidentes](#4-gestao-de-vulnerabilidades-e-resposta-a-incidentes)
    - [4.1 Métricas do CVSS v3.1 (Common Vulnerability Scoring System)](#41-metricas-do-cvss-v31-common-vulnerability-scoring-system)
    - [4.2 As Quatro Fases do Ciclo de Resposta a Incidentes (NIST SP 800-61)](#42-as-quatro-fases-do-ciclo-de-resposta-a-incidentes-nist-sp-800-61)
- [5. Família de Normas ISO/IEC 27000 (SGSI)](#5-familia-de-normas-isoiec-27000-sgsi)
    - [5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL](#51-a-norma-certificavel-isoiec-27001-e-o-anexo-sl)
    - [5.2 A Nova ISO/IEC 27002 (Edição 2022: 4 Temas e 93 Controles)](#52-a-nova-isoiec-27002-edicao-2022-4-temas-e-93-controles)
    - [5.3 A Declaração de Aplicabilidade (SoA) e a ISO/IEC 27005](#53-a-declaracao-de-aplicabilidade-soa-e-a-isoiec-27005)
- [6. Questões Comentadas (FCC)](#6-questoes-comentadas-fcc)

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

## 6. Questões Comentadas (FCC)

### Questão 01
**(FCC - DPE-RS - Analista de Tecnologia da Informação)**
Durante uma auditoria de conformidade em um sistema eletrônico de protocolo processual do Tribunal de Contas, os auditores avaliaram a eficácia de diferentes mecanismos de segurança da informação.
Relacione as situações práticas descritas a seguir com o princípio fundamental de segurança correspondente (CIDAN):

1. Garantir que um documento processual contábil emitido por um conselheiro não tenha seu conteúdo adulterado ou corrompido durante a transmissão na rede.
2. Garantir que dados fiscais sigilosos de contribuintes sob sigilo legal não sejam visualizados por servidores públicos não autorizados.
3. Garantir que o remetente de um ofício eletrônico assinado com certificado digital ICP-Brasil não possa negar falsamente, perante a administração e a justiça, a autoria do envio daquele documento.

As situações 1, 2 e 3 correspondem, respectivamente, aos princípios de:

* **A)** Autenticidade; Disponibilidade; e Confidencialidade.
* **B)** Integridade; Confidencialidade; e Não Repúdio (Irretratabilidade).
* **C)** Confidencialidade; Integridade; e Autenticidade.
* **D)** Disponibilidade; Legalidade; e Não Repúdio.
* **E)** Integridade; Autenticidade; e Disponibilidade.

> **Comentário Detalhado:**
>
> - **Situação 1:** Trata da garantia contra adulterações ou corrupções de conteúdo, correspondendo estritamente ao princípio da **Integridade**.
> - **Situação 2:** Trata do barramento de visualização e leitura por terceiros não autorizados, salvaguardando o sigilo, o que define a **Confidencialidade**.
> - **Situação 3:** Trata da impossibilidade jurídica de o autor contestar ou negar falsamente ter praticado o ato, o que define formalmente o princípio do **Não Repúdio** (ou Irretratabilidade).
> - **A)** Incorreta. A situação 1 trata de integridade e a 2 de confidencialidade.
> - **B)** **Correta.** Mapeia rigorosamente: 1 = Integridade, 2 = Confidencialidade e 3 = Não Repúdio.
> - **C)** Incorreta. Inverteu as situações 1 e 2.
> - **D)** Incorreta. Aponta disponibilidade para a situação 1.
> - **E)** Incorreta. Erra as correspondências dos itens 2 e 3.
> 
> **Gabarito: B**

---

### Questão 02
**(FCC - SEFAZ-PE - Auditoria Fiscal - Gestão de Riscos e Normas ISO/IEC 27000)**
A respeito dos conceitos de gestão de riscos e da família de normas ABNT NBR ISO/IEC 27000, assinale a afirmativa correta:

* **A)** Uma vulnerabilidade é o agente externo causador do dano (como um invasor ou uma tempestade), enquanto a ameaça é a falha ou brecha interna de um sistema.
* **B)** A norma ABNT NBR ISO/IEC 27001 é um padrão certificável que define os requisitos para estabelecer, implementar, manter e melhorar continuamente um Sistema de Gestão de Segurança da Informação (SGSI), estruturado nas cláusulas de alto nível harmonizadas e no ciclo PDCA.
* **C)** A edição atualizada da norma ISO/IEC 27002 organiza seus controles em 14 domínios tecnológicos idênticos aos da versão de 2005, proibindo expressamente o tratamento de controles organizacionais e de pessoas.
* **D)** O cálculo do risco quantitativo Annualized Loss Expectancy (ALE) é obtido somando-se a taxa anual de ocorrência (ARO) com a metade do patrimônio líquido da organização.
* **E)** A opção de tratamento de risco denominada "Aceitação" consiste em instalar firewalls redundantes e sistemas IPS para zerar o risco residual.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Os conceitos foram invertidos: **Vulnerabilidade** é a fraqueza interna do ativo; **Ameaça** é o agente ou evento externo causador do dano potencial.
> - **B)** **Correta.** A **ABNT NBR ISO/IEC 27001** prescreve formalmente os **requisitos do SGSI**, sendo a única norma da família 27000 passível de certificação institucional para organizações.
> - **C)** Incorreta. A ISO/IEC 27002:2022 consolidou os antigos 14 domínios em **4 temas integrados**: Organizacionais, Pessoas, Físicos e Tecnológicos, somando 93 controles.
> - **D)** Incorreta. A fórmula quantitativa correta é a multiplicação: $\text{ALE} = \text{SLE} \times \text{ARO}$, sem relação com somas de patrimônio líquido.
> - **E)** Incorreta. A Aceitação do risco (*Risk Acceptance*) não adiciona controles técnicos; consiste em assumir formalmente o risco residual sem novas salvaguardas quando o custo de mitigação não for justificável.
> 
> **Gabarito: B**

---

### Questão 03
**(FCC - TCE-RS - Auditor Público Externo - Tecnologia da Informação)**
Durante o processo de avaliação quantitativa de riscos de um banco de dados do Tribunal de Contas avaliado em R$ 400.000,00, a equipe de segurança apurou que um ataque cibernético de ransomware causaria uma perda direta de 40% sobre o valor desse ativo. O histórico de segurança do órgão e os relatórios de inteligência de ameaças apontam que a taxa anual estimada de ocorrência desse tipo de incidente para órgãos do mesmo porte é de 0,25 vezes por ano (isto é, 1 incidente a cada 4 anos).
Com base nas métricas clássicas de análise quantitativa de risco ($\text{SLE}$, $\text{ARO}$ e $\text{ALE}$), assinale a opção que apresenta, respectivamente, o valor da Expectativa de Perda Única ($\text{SLE}$) e da Expectativa de Perda Anual ($\text{ALE}$):

* **A)** R$ 160.000,00 e R$ 40.000,00.
* **B)** R$ 40.000,00 e R$ 160.000,00.
* **C)** R$ 240.000,00 e R$ 60.000,00.
* **D)** R$ 100.000,00 e R$ 25.000,00.
* **E)** R$ 160.000,00 e R$ 80.000,00.

> **Comentário Detalhado:**
>
> - **1. Dados fornecidos:**
>     - $\text{AV}$ (*Asset Value*) = R$ 400.000,00
>     - $\text{EF}$ (*Exposure Factor*) = $40\% = 0{,}40$
>     - $\text{ARO}$ (*Annualized Rate of Occurrence*) = $0{,}25$
> - **2. Cálculo da Expectativa de Perda Única (SLE):**
>   $$\text{SLE} = \text{AV} \times \text{EF} = 400.000 \times 0{,}40 = \text{R\$}~160.000,00$$
> - **3. Cálculo da Expectativa de Perda Anual (ALE):**
>   $$\text{ALE} = \text{SLE} \times \text{ARO} = 160.000 \times 0{,}25 = \text{R\$}~40.000,00$$
> - **A)** **Correta.** Apresenta exatamente $\text{SLE} = \text{R\$}~160.000,00$ e $\text{ALE} = \text{R\$}~40.000,00$.
> - **B)** Incorreta. Inverteu a posição de SLE e ALE.
> - **C)** Incorreta. Calculou o valor residual do ativo pós-incidente (60% = R$ 240.000,00).
> - **D)** Incorreta. Utilizou incorretamente 25% para o cálculo do SLE.
> - **E)** Incorreta. Errou o cálculo do ALE ao utilizar um ARO fictício de 0,50.
> 
> **Gabarito: A**

---

### Questão 04
**(FCC - TRT-15ª Região - Analista Judiciário - Tecnologia da Informação)**
A Lei Federal nº 12.527/2011 (Lei de Acesso à Informação - LAI) dispõe sobre os procedimentos a serem observados pela União, Estados, DF e Municípios com o fim de garantir o acesso a informações públicas, estabelecendo regras para a classificação e proteção de dados que exijam restrição de acesso por motivos de segurança da sociedade ou do Estado.
Considere as seguintes assertivas sobre os graus de sigilo e prazos previstos na LAI:

I. A classificação de uma informação como reservada impõe restrição de acesso pelo prazo máximo de 5 anos.  

II. A informação classificada como secreta possui prazo máximo de restrição de 15 anos, sendo admitida prorrogação automática e ilimitada por sucessivos períodos de 10 anos.  

III. O prazo máximo de restrição de acesso à informação ultrassecreta é de 25 anos, podendo ser prorrogado uma única vez, por igual período, por decisão privativa da Comissão Mista de Reavaliação de Informações (CMRI).  

Está correto o que se afirma em:

* **A)** I, apenas.
* **B)** I e II, apenas.
* **C)** I e III, apenas.
* **D)** II e III, apenas.
* **E)** I, II e III.

> **Comentário Detalhado:**
>
> - **Item I (Correto):** Conforme o Art. 24, § 1º, III da LAI, o prazo de sigilo da informação **reservada** é de no máximo **5 anos**.
> - **Item II (Incorreto):** O prazo da informação **secreta** é de **15 anos**, mas a LAI **não admite prorrogações sucessivas ou ilimitadas**; o sigilo extingue-se impreterivelmente ao final dos 15 anos.
> - **Item III (Correto):** Conforme o Art. 24, § 1º, I c/c Art. 35, § 1º da LAI, a informação **ultrassecreta** possui prazo de **25 anos**, admitindo **uma única prorrogação por igual período** por decisão privativa da CMRI.
> - **A)** Incorreta, pois o item III também é verdadeiro.
> - **B)** Incorreta, pois o item II é falso.
> - **C)** **Correta.** Apenas as assertivas I e III estão corretas.
> - **D)** Incorreta, pois o item II é falso.
> - **E)** Incorreta, pois o item II está incorreto.
> 
> **Gabarito: C**

---

### Questão 05
**(FCC - TRF-3ª Região - Analista Judiciário - Informática)**
De acordo com o guia de boas práticas para tratamento de incidentes de segurança cibernética do NIST (NIST SP 800-61 Rev. 2) e as diretrizes da norma ISO/IEC 27035, um incidente cibernético confirmado deve ser processado segundo um ciclo estruturado de fases operacionais.
Ao detectar a proliferação acelerada de um malware em sua rede corporativa, a equipe de segurança da informação procedeu imediatamente com o isolamento físico dos servidores comprometidos através do desligamento das portas de switch correspondentes, com o intuito de conter a ameaça e evitar que outros nós fossem atingidos.
A referida ação operacional executada pela equipe insere-se formalmente na fase de:

* **A)** Preparação.
* **B)** Detecção e Análise.
* **C)** Contenção.
* **D)** Atividades Pós-Incidente (Lições Aprendidas).
* **E)** Classificação de Ativos.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Preparação é a etapa preventiva preliminar (treinamentos, políticas e criação do CSIRT).
> - **B)** Incorreta. Detecção e análise já ocorreram, pois o malware foi previamente identificado e analisado.
> - **C)** **Correta.** A ação de desconectar cabos, isolar máquinas da rede ou desativar portas de switch compõe a essência da **Contenção (*Containment*)**, cuja finalidade imediata é frear o avanço do ataque e limitar o dano aos ativos adjacentes.
> - **D)** Incorreta. Atividades pós-incidente (lições aprendidas) ocorrem após o restabelecimento produtivo dos sistemas.
> - **E)** Incorreta. Classificação de ativos é processo de governança, não sendo fase operacional de resposta a incidentes do NIST.
> 
> **Gabarito: C**
