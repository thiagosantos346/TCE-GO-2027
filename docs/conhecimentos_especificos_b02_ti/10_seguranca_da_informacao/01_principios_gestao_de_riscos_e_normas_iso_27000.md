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

### Teste 355
**(FGV – TRF/1 – 2024 – Analista Judiciario Area Apoio Especializado Especialidade Suporte Em Tecnologia Da Informacao)**
O uso de criptografia na armazenagem ou tráfego de dados visa a garantir os pilares da segurança da informação. As ações a seguir podem ser garantidas com o uso da criptografia: I. proteção das informações armazenadas ou transmitidas; II. comprovação da ocorrência ou não ocorrência de um evento ou ação; III. verificação da correção da informação; IV. validação de usuários nos sistemas. Assinale a alternativa que identifica, respectivamente, os pilares da segurança da informação associados a cada uma das ações acima:

* **A)** confidencialidade, não repúdio, integridade e autenticação;
* **B)** não repúdio, confidencialidade, autenticidade e integridade;
* **C)** integridade, autenticidade, autenticação e disponibilidade;
* **D)** autenticidade, integridade, disponibilidade e não repúdio;
* **E)** disponibilidade, integridade, autenticidade e confidencialidade.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade* deste guia, *Mecanismos técnicos:* Funções criptográficas de espalhamento (*hashing* criptográfico como SHA-256 e SHA-512), códigos de autenticação de mensagem (HMAC), assinaturas digitais, somas de verificação (*checksums*) e trilhas de auditoria imutáveis. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRF/1/2024) ao estabelecer que "confidencialidade, não repúdio, integridade e autenticação".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "não repúdio, confidencialidade, autenticidade e integridade". De acordo com a teoria estudada em *1. Princípios Básicos da Segurança da Informação (CIDAN)*, a segurança da informação é definida pela norma ABNT NBR ISO/IEC 27000 como a preservação da confidencialidade, integridade e disponibilidade da informação, admitindo-se adicionalmente propriedades vitais para transações formais como a autenticidade e o não repúdio.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "integridade, autenticidade, autenticação e disponibilidade". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, garantia de que a informação, os sistemas computacionais e os ativos de telecomunicações associados estejam acessíveis e utilizáveis sob demanda pelos usuários autorizados sempre que necessário.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "autenticidade, integridade, disponibilidade e não repúdio". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, *Mecanismos técnicos:* Criptografia em trânsito (TLS) e em repouso (TDE), controle de acesso lógico baseado em papéis (RBAC), mascaramento dinâmico de dados e soluções de Prevenção contra Perda de Dados (*DLP - Data Loss Prevention*).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "disponibilidade, integridade, autenticidade e confidencialidade". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, *Mecanismos técnicos:* Redundância de hardware e fontes de alimentação, clusters de alta disponibilidade (HA ativo-ativo ou ativo-passivo), sistemas anti-DDoS, geradores e nobreaks comutáveis, planos de continuidade de negócios (PCN/DRP) e rotinas estruturadas de backup.
>
> **Gabarito: A**

---

### Teste 356
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Ciência de Dados)**
A segurança da informação é fundamentada em três pilares principais: 1. Confidencialidade: Garantir que a informação seja acessível apenas a indivíduos autorizados. 2. Integridade: Assegurar que a informação seja precisa e completa, não sofrendo alterações não autorizadas. 3. Disponibilidade: Garantir que a informação e os recursos estejam disponíveis para uso quando necessário. Esses conceitos são frequentemente referidos como a Tríade CIA (Confidentiality, Integrity, Availability). A equipe de TI do TCE-PA está desenvolvendo um plano de segurança da informação. Eles precisam garantir que informações sensíveis estejam protegidas contra acessos não autorizados, que os dados das transações permaneçam inalterados e corretos, e que os sistemas estejam sempre disponíveis para realizarem suas operações. Assinale a opção que melhor representa a implementação dos três pilares da segurança da informação (confidencialidade, integridade e disponibilidade) no cenário descrito.

* **A)** Utilizar funções de hash para garantir que os dados estão ´- íntegros, criptografia para assegurar a confidencialidade e redundância de servidores para garantir a disponibilidade.
* **B)** Utilizar criptografia para proteger a integridade dos dados, backups regulares para assegurar a confiabilidade e redundância de servidores para garantir a disponibilidade.
* **C)** Implementar redundância de servidores para proteger a confiabilidade, criptografia para assegurar a integridade e backups regulares para garantir a disponibilidade
* **D)** Utilizar criptografia para proteger a disponibilidade dos dados, backups regulares para assegurar a integridade e redundância de servidores para garantir a confiabilidade.
* **E)** Implementar redundância de servidores para proteger a disponibilidade, criptografia para assegurar a confiabilidade e backups regulares para garantir a confidencialidade

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade* deste guia, *Mecanismos técnicos:* Criptografia em trânsito (TLS) e em repouso (TDE), controle de acesso lógico baseado em papéis (RBAC), mascaramento dinâmico de dados e soluções de Prevenção contra Perda de Dados (*DLP - Data Loss Prevention*). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "Utilizar funções de hash para garantir que os dados estão ´- íntegros, criptografia para assegurar a...".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Utilizar criptografia para proteger a integridade dos dados, backups regulares para assegurar a confiabilidade e...". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, garantia de que a informação, os sistemas computacionais e os ativos de telecomunicações associados estejam acessíveis e utilizáveis sob demanda pelos usuários autorizados sempre que necessário.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Implementar redundância de servidores para proteger a confiabilidade, criptografia para assegurar a integridade e...". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, *Ameaças clássicas:* Escuta clandestina de rede (*sniffing/eavesdropping*), roubo de dispositivos físicos, engenharia social, vazamento inadvertido de dados fiscais protegidos por sigilo e acessos não autorizados.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Utilizar criptografia para proteger a disponibilidade dos dados, backups regulares para assegurar a integridade e...". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, *Mecanismos técnicos:* Redundância de hardware e fontes de alimentação, clusters de alta disponibilidade (HA ativo-ativo ou ativo-passivo), sistemas anti-DDoS, geradores e nobreaks comutáveis, planos de continuidade de negócios (PCN/DRP) e rotinas estruturadas de backup.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Implementar redundância de servidores para proteger a disponibilidade, criptografia para assegurar a...". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, *Ameaças clássicas:* Adulteração maliciosa de tabelas contábeis ou salariais em bancos de dados (*tampering*), infecção por malware, ataques man-in-the-middle e erros de transmissão de rede sem checagem de paridade.
>
> **Gabarito: A**

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

### Teste 357
**(FGV – TRT 1ª – 2024 – Analista Judiciário - Área Administrativa)**
De acordo com a Lei nº 12.527/2011, cabe aos órgãos e entidades do Poder Público, observados os procedimentos específicos aplicáveis e as normas, assegurar a proteção da informação sigilosa. É correto afirmar acerca desse tema, à luz do mencionado diploma legal, que:

* **A)** o prazo máximo de restrição de acesso para informação classificada como secreta é de vinte e cinco anos, vigorando a partir da data de sua produção;
* **B)** as informações cuja divulgação ou acesso irrestrito possam prejudicar ou causar risco a projetos de pesquisa e desenvolvimento científico ou tecnológico não podem ser consideradas como imprescindíveis à segurança da sociedade e do Estado e, portanto, passíveis de classificação de sigilo;
* **C)** a classificação do sigilo de informações no âmbito da Administração Pública federal no grau reservado é de competência de todos os servidores públicos federais que tenham sido regularmente investidos em cargos efetivos;
* **D)** o requerente deverá ser informado sobre a possibilidade de recurso, prazos e condições para sua interposição, quando não for autorizado o acesso por se tratar de informação total ou parcialmente sigilosa, devendo, ainda, ser-lhe indicada a autoridade competente para sua apreciação;
* **E)** o disposto na aludida norma abarca as situações previstas nas demais hipóteses legais de sigilo e de segredo de justiça, além de hipóteses de segredo industrial decorrentes da exploração direta de atividade econômica pelo Estado, afastando, por conseguinte, a aplicação das respectivas normas.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "o prazo máximo de restrição de acesso para informação classificada como secreta é de vinte e cinco anos, vigorando...". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, além disso, lembre-se: informações relativas à intimidade, vida privada, honra e imagem das pessoas têm restrição de acesso máxima de até 100 anos a contar da data de sua produção (Art. 31 da LAI), não se confundindo com prazos de segurança de Estado!.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "as informações cuja divulgação ou acesso irrestrito possam prejudicar ou causar risco a projetos de pesquisa e...". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam-se em três graus solenes.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "a classificação do sigilo de informações no âmbito da Administração Pública federal no grau reservado é de...". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, grau de Sigilo: Prazo Máximo de Restrição — Competência Originária Típica para Classificar — Regime de Prorrogação.
> - **D)** **Correta.** Conforme fundamentado na seção *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)* deste guia, decore rigorosamente os prazos decrescentes: 25 anos $\rightarrow$ 15 anos $\rightarrow$ 5 anos. A FCC inventa prazos alternativos inexistentes (como 10 ou 20 anos) ou inverte Secreta e Reservada. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT 1ª/2024) ao estabelecer que "o requerente deverá ser informado sobre a possibilidade de recurso, prazos e condições para sua interposição...".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "o disposto na aludida norma abarca as situações previstas nas demais hipóteses legais de sigilo e de segredo de...". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, secreta: 15 anos — Titulares de autarquias, fundações e órgãos públicos sob mesma alçada legal — Não admite prorrogação. O prazo cessa impreterivelmente aos 15 anos.
>
> **Gabarito: D**

---

### Teste 358
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Ciências da Computação, Sistemas de Informação...)**
Durante uma auditoria de conformidade em Segurança da Informação, um Auditor analisa os procedimentos de backup e os mecanismos de redundância de hardware de um órgão público. Essas salvaguardas são implementadas para garantir que, mesmo diante de falhas técnicas ou desastres, os dados possam ser acessados pelos usuários autorizados e que seu conteúdo não tenha sofrido modificações indesejadas durante o incidente. De acordo com a norma ISO/IEC 27002, os princípios da segurança da informação que visam assegurar, respectivamente, o acesso oportuno à informação e a preservação da exatidão dos dados são os de

* **A)** confidencialidade e autenticidade.
* **B)** disponibilidade e integridade.
* **C)** não repúdio e irretratabilidade.
* **D)** elasticidade e escalabilidade.
* **E)** governança e compliance.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "confidencialidade e autenticidade". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, *Mecanismos técnicos:* Redundância de hardware e fontes de alimentação, clusters de alta disponibilidade (HA ativo-ativo ou ativo-passivo), sistemas anti-DDoS, geradores e nobreaks comutáveis, planos de continuidade de negócios (PCN/DRP) e rotinas estruturadas de backup.
> - **B)** **Correta.** Conforme fundamentado na seção *1. Princípios Básicos da Segurança da Informação (CIDAN)* deste guia, a segurança da informação é definida pela norma ABNT NBR ISO/IEC 27000 como a preservação da confidencialidade, integridade e disponibilidade da informação, admitindo-se adicionalmente propriedades vitais para transações formais como a autenticidade e o não repúdio. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "disponibilidade e integridade".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "não repúdio e irretratabilidade". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, *Ameaças clássicas:* Ataques de negação de serviço (DoS e DDoS), falhas físicas de hardware em servidores e storages, interrupção no fornecimento de energia elétrica, panes nos links de internet e desastres ambientais (enchentes, incêndios em datacenters).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "elasticidade e escalabilidade". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, garantia de que a informação, os sistemas computacionais e os ativos de telecomunicações associados estejam acessíveis e utilizáveis sob demanda pelos usuários autorizados sempre que necessário.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "governança e compliance". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, *Mecanismos técnicos:* Criptografia em trânsito (TLS) e em repouso (TDE), controle de acesso lógico baseado em papéis (RBAC), mascaramento dinâmico de dados e soluções de Prevenção contra Perda de Dados (*DLP - Data Loss Prevention*).
>
> **Gabarito: B**

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

### Teste 359
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
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "no JBoss EAP 6 a fonte de dados é configurada no arquivo de configuração do servidor. Caso a instância do JBoss...". De acordo com a teoria estudada em *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade*, vulnerabilidade (*Vulnerability*): Ponto fraco, falha de projeto, brecha de configuração ou deficiência de controle em um ativo que pode ser explorado por uma ameaça.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "o JBoss Messaging passou a ser incluído no JBoss EAP 6, já que o JBoss EAP 5 usava o HornetQ como provedor...". De acordo com a teoria estudada em *5.3 A Declaração de Aplicabilidade (SoA) e a ISO/IEC 27005*, iSO/IEC 27005: Norma que fornece diretrizes especializadas para o processo de avaliação e tratamento de riscos de segurança da informação no suporte ao SGSI.
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "no JBoss EAP 5 a arquitetura de carregamento de classe era baseado nos JBoss Modules, mas no JBoss EAP6, o...". De acordo com a teoria estudada em *3. Gestão e Análise de Riscos de Segurança da Informação*, a gestão de riscos estabelece um processo contínuo e estruturado para identificar incertezas, avaliar a probabilidade de falhas e selecionar salvaguardas economicamente proporcionais.
> - **D)** **Correta.** Conforme fundamentado na seção *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL* deste guia, a norma ABNT NBR ISO/IEC 27001 estabelece os requisitos formais para estabelecer, implementar, manter e melhorar continuamente um Sistema de Gestão de Segurança da Informação (SGSI). Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 24ª/2017) ao estabelecer que "no JBoss EAP 5, o servidor podia ser executado em um managed domain, mas no JBoss EAP 6 executa como um servidor...".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "o JBoss EAP 5 usava perfis baseados na configuração de implantação, localizados no diretório EAP_HOME/...". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, evitar / Eliminar (*Risk Avoidance*): Descontinuar a atividade, processo ou serviço gerador do risco (ex.: desligar e desativar em definitivo um sistema legado vulnerável sem suporte do fabricante).
>
> **Gabarito: D**

---

### Teste 360
**(FGV – TJ/AP – 2023 – Analista Judiciario Apoio Especializado Tecnologia Da Informacao Banco De Dados)**
Uma empresa de consultoria X foi contratada para verificar os riscos quanto à segurança da informação no Tribunal de Justiça do Amapá (TJAP). Para atender ao requisito licitatório, a consultoria fez uso da norma ABNT NBR ISO/IEC 27005:2011. Em seu relatório de segurança, a consultoria identificou riscos causados por fenômenos naturais, de forma que a melhor alternativa era mover fisicamente as instalações para um local onde tal risco não exista ou esteja sob controle. A empresa de consultoria X se baseou no tópico de tratamento de riscos de:

* **A)** reter o risco;
* **B)** modificar o risco;
* **C)** evitar o risco;
* **D)** compartilhar o risco;
* **E)** aceitar o risco.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "reter o risco". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, aceitar / Reter (*Risk Acceptance / Retention*): Manter o risco no nível atual sem novos controles, mediante aprovação formal fundamentada da alta administração, quando o custo da salvaguarda técnica for superior à perda monetária potencial estimada.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "modificar o risco". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, transferir / Compartilhar (*Risk Transfer / Sharing*): Compartilhar a carga financeira ou operacional das perdas com terceiros (ex.: contratação de apólice de seguro contra incidentes cibernéticos ou terceirização da infraestrutura de datacenter para provedores de nuvem sob contratos de SLA estritos).
> - **C)** **Correta.** Conforme fundamentado na seção *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)* deste guia, evitar / Eliminar (*Risk Avoidance*): Descontinuar a atividade, processo ou serviço gerador do risco (ex.: desligar e desativar em definitivo um sistema legado vulnerável sem suporte do fabricante). Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/AP/2023) ao estabelecer que "evitar o risco".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "compartilhar o risco". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, mitigar / Reduzir (*Risk Mitigation / Reduction*): Implementar controles de segurança (técnicos, administrativos ou físicos) para reduzir a probabilidade e/ou o impacto do risco até patamares aceitáveis (ex.: instalar firewalls, adotar MFA e criptografia).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "aceitar o risco". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, concluída a avaliação do risco, a organização deve optar formalmente por uma das quatro respostas estratégicas.
>
> **Gabarito: C**

---

### Teste 361
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
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "as opções de tratamento do risco sejam selecionadas apenas com base no resultado do processo de avaliação de...". De acordo com a teoria estudada em *5.3 A Declaração de Aplicabilidade (SoA) e a ISO/IEC 27005*, iSO/IEC 27005: Norma que fornece diretrizes especializadas para o processo de avaliação e tratamento de riscos de segurança da informação no suporte ao SGSI.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "as quatro opções para tratamento do risco sejam aplicadas de forma mutuamente exclusiva, ou seja, não combinadas". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, mitigar / Reduzir (*Risk Mitigation / Reduction*): Implementar controles de segurança (técnicos, administrativos ou físicos) para reduzir a probabilidade e/ou o impacto do risco até patamares aceitáveis (ex.: instalar firewalls, adotar MFA e criptografia).
> - **C)** **Correta.** Conforme fundamentado na seção *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)* deste guia, evitar / Eliminar (*Risk Avoidance*): Descontinuar a atividade, processo ou serviço gerador do risco (ex.: desligar e desativar em definitivo um sistema legado vulnerável sem suporte do fabricante). Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 3ª/2015) ao estabelecer que "as opções de tratamento do risco sejam consideradas levando-se em conta como o risco é percebido pelas partes...".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "as consequências adversas do risco sejam reduzidas ao mínimo possível de acordo com critérios absolutos, como a...". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, *Cláusula 6:* Planejamento (Tratamento de riscos e objetivos de segurança).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "um plano de tratamento de riscos seja definido identificando os riscos mais prováveis, as formas de tratar estes...". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, *Cláusula 8:* Operação (Execução do tratamento de riscos de segurança).
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

### Teste 362
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
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Os sistemas de detecção de intrusão (IDS) e os sistemas de prevenção de intrusão (IPS) são ferramentas com a mesma...". De acordo com a teoria estudada em *4.2 As Quatro Fases do Ciclo de Resposta a Incidentes (NIST SP 800-61)*, preparação (*Preparation*): Estabelecimento e capacitação da equipe técnica de resposta (CSIRT / CERT), aquisição de ferramentas de investigação forense, implantação de políticas e planos de comunicação.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Gestão de vulnerabilidades é um processo para correção de vulnerabilidades em softwares, não tendo relação direta...". De acordo com a teoria estudada em *3. Gestão e Análise de Riscos de Segurança da Informação*, a gestão de riscos estabelece um processo contínuo e estruturado para identificar incertezas, avaliar a probabilidade de falhas e selecionar salvaguardas economicamente proporcionais.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Um sistema de detecção de intrusão (IDS) não funciona numa DMZ (Demilitarized Zone), pois ela necessita de...". De acordo com a teoria estudada em *4.2 As Quatro Fases do Ciclo de Resposta a Incidentes (NIST SP 800-61)*, *Contenção:* Ação emergencial prioritária voltada a estancar a disseminação do ataque e limitar o raio de destruição (*blast radius*), tal como isolar a máquina da rede, desconectar cabos ou bloquear portas de switches.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O uso de NAC (Network Access Control) não contribui para a gestão de vulnerabilidades". De acordo com a teoria estudada em *4.1 Métricas do CVSS v3.1 (Common Vulnerability Scoring System)*, o padrão CVSS (mantido pelo FIRST) quantifica a gravidade técnica de vulnerabilidades de software e hardware em uma escala contínua de 0,0 a 10,0.
> - **E)** **Correta.** Conforme fundamentado na seção *4.2 As Quatro Fases do Ciclo de Resposta a Incidentes (NIST SP 800-61)* deste guia, detecção e Análise (*Detection and Analysis*): Monitoramento contínuo de alertas de IDS/IPS, antivírus/EDR e correlação de logs em SIEM para constatar indícios de comprometimento (*IoCs*) e dimensionar o alcance do ataque. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/GO/2024) ao estabelecer que "Os Sistemas de detecção de intrusão (IDS) são projetados para monitorar e alertar sobre possíveis intrusões...".
>
> **Gabarito: E**

---

### Teste 363
**(FCC – TRT 3ª – 2015 – Analista Judiciário - Tecnologia da Informação)**
A fase “Definindo o SGSI” da norma ABNT NBR ISO/IEC 27003:2011 tem como objetivo completar o plano final de implantação do SGSI por meio da definição da segurança da organização com base nas opções de tratamento de risco selecionadas e nos requisitos de registros e documentação, definição dos controles pela integração com as provisões de segurança para TIC, infraestrutura e processos organizacionais, e definição dos requisitos específicos do SGSI. Nesta fase, na atividade de definição de uma estrutura para a documentação do SGSI, a saída é um documento

* **A)** resumindo os requisitos para os registros do SGSI e do controle da documentação, e repositórios e modelos para os registros necessários do SGSI.
* **B)** da Política da Segurança da Informação e do Plano de Continuidade de Negócios.
* **C)** que detalha um plano de implementação estruturado para os controles relacionados à segurança da organização como parte do plano final do projeto do SGSI.
* **D)** resumindo a estrutura da organização, papéis e responsabilidades para a segurança da informação alinhadas com o tratamento de risco.
* **E)** que resume o plano necessário para realizar uma análise crítica pela direção incluindo entradas e procedimentos exigidos avaliar a eficácia dos requisitos do SGSI para a gestão de controles de segurança da informação no projeto em que está trabalhando, o analista consultou a seção 7 da norma para descobrir as atividades sugeridas para serem estabelecidas e documentadas no desenvolvimento das medidas e medições. Nesse contexto, considere as atividades abaixo.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL* deste guia, a norma ABNT NBR ISO/IEC 27001 estabelece os requisitos formais para estabelecer, implementar, manter e melhorar continuamente um Sistema de Gestão de Segurança da Informação (SGSI). Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 3ª/2015) ao estabelecer que "resumindo os requisitos para os registros do SGSI e do controle da documentação, e repositórios e modelos para os...".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "da Política da Segurança da Informação e do Plano de Continuidade de Negócios". De acordo com a teoria estudada em *5.3 A Declaração de Aplicabilidade (SoA) e a ISO/IEC 27005*, iSO/IEC 27005: Norma que fornece diretrizes especializadas para o processo de avaliação e tratamento de riscos de segurança da informação no suporte ao SGSI.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "que detalha um plano de implementação estruturado para os controles relacionados à segurança da organização como...". De acordo com a teoria estudada em *5.2 A Nova ISO/IEC 27002 (Edição 2022: 4 Temas e 93 Controles)*, a norma ISO/IEC 27002 constitui um Código de Práticas que detalha diretrizes para implementação dos controles de segurança do Anexo A da ISO 27001. Não é passível de certificação independente.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "resumindo a estrutura da organização, papéis e responsabilidades para a segurança da informação alinhadas com o...". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, concluída a avaliação do risco, a organização deve optar formalmente por uma das quatro respostas estratégicas.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "que resume o plano necessário para realizar uma análise crítica pela direção incluindo entradas e procedimentos...". De acordo com a teoria estudada em *3. Gestão e Análise de Riscos de Segurança da Informação*, a gestão de riscos estabelece um processo contínuo e estruturado para identificar incertezas, avaliar a probabilidade de falhas e selecionar salvaguardas economicamente proporcionais.
>
> **Gabarito: A**

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

### Teste 364
**(FGV – TJ/RR – 2024 – Analista Judiciario Gestao E Governanca De Tecnologia Da Informacao)**
Com base nas normas ABNT referentes à segurança da informação, julgue as afirmativas a seguir. I. A Norma ABNT NBR ISO/IEC 27001:2022 estabelece requisitos genéricos e aplicáveis a todas as instituições, de qualquer tipo, tamanho ou natureza. II. A Norma ABNT NBR ISO/IEC 27002:2022 fornece orientações para ajudar as organizações a cumprirem os requisitos da ABNT NBR ISO/IEC 27005 em relação às ações para abordar riscos de segurança da informação. III. A Norma ABNT NBR ISO/IEC 27005:2022 determina os requisitos para estabelecer, implementar, manter e melhorar continuamente um sistema de gestão da segurança da informação dentro do contexto da organização. Está correto o que se afirma em

* **A)** I, apenas.
* **B)** I e II, apenas.
* **C)** I e III, apenas.
* **D)** II e III, apenas.
* **E)** I, II e III.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL* deste guia, a norma ABNT NBR ISO/IEC 27001 estabelece os requisitos formais para estabelecer, implementar, manter e melhorar continuamente um Sistema de Gestão de Segurança da Informação (SGSI). Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/RR/2024) ao estabelecer que "I, apenas".
> - **B)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e II, apenas". De acordo com a teoria estudada em *5.3 A Declaração de Aplicabilidade (SoA) e a ISO/IEC 27005*, iSO/IEC 27005: Norma que fornece diretrizes especializadas para o processo de avaliação e tratamento de riscos de segurança da informação no suporte ao SGSI.
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e III, apenas". De acordo com a teoria estudada em *5.2 A Nova ISO/IEC 27002 (Edição 2022: 4 Temas e 93 Controles)*, a norma ISO/IEC 27002 constitui um Código de Práticas que detalha diretrizes para implementação dos controles de segurança do Anexo A da ISO 27001. Não é passível de certificação independente.
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II e III, apenas". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, *Cláusula 4:* Contexto da Organização (partes interessadas e escopo do SGSI).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I, II e III". De acordo com a teoria estudada em *1. Princípios Básicos da Segurança da Informação (CIDAN)*, a segurança da informação é definida pela norma ABNT NBR ISO/IEC 27000 como a preservação da confidencialidade, integridade e disponibilidade da informação, admitindo-se adicionalmente propriedades vitais para transações formais como a autenticidade e o não repúdio.
>
> **Gabarito: A**

---

### Teste 365
**(FGV – TJ/RR – 2024 – Analista Judiciario Infraestrutura De Tecnologia Da Informacao)**
Com base nas normas ABNT referentes à segurança da informação, avalie as afirmativas a seguir. I. A Norma ABNT NBR ISO/IEC 27001:2022 estabelece requisitos genéricos e aplicáveis a todas as instituições, de qualquer tipo, tamanho ou natureza. II. A Norma ABNT NBR ISO/IEC 27002:2022 fornece orientações para ajudar as organizações a cumprirem os requisitos da ABNT NBR ISO/IEC 27005 em relação às ações para abordar riscos de segurança da informação. III. A Norma ABNT NBR ISO/IEC 27005:2022 determina os requisitos para estabelecer, implementar, manter e melhorar continuamente um sistema de gestão da segurança da informação dentro do contexto da organização. Está correto o que se afirma em

* **A)** I, apenas.
* **B)** I e II, apenas.
* **C)** I e III, apenas.
* **D)** II e III, apenas.
* **E)** I, II e III.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL* deste guia, a norma ABNT NBR ISO/IEC 27001 estabelece os requisitos formais para estabelecer, implementar, manter e melhorar continuamente um Sistema de Gestão de Segurança da Informação (SGSI). Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/RR/2024) ao estabelecer que "I, apenas".
> - **B)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e II, apenas". De acordo com a teoria estudada em *5.3 A Declaração de Aplicabilidade (SoA) e a ISO/IEC 27005*, iSO/IEC 27005: Norma que fornece diretrizes especializadas para o processo de avaliação e tratamento de riscos de segurança da informação no suporte ao SGSI.
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e III, apenas". De acordo com a teoria estudada em *5.2 A Nova ISO/IEC 27002 (Edição 2022: 4 Temas e 93 Controles)*, a norma ISO/IEC 27002 constitui um Código de Práticas que detalha diretrizes para implementação dos controles de segurança do Anexo A da ISO 27001. Não é passível de certificação independente.
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II e III, apenas". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, *Cláusula 4:* Contexto da Organização (partes interessadas e escopo do SGSI).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I, II e III". De acordo com a teoria estudada em *1. Princípios Básicos da Segurança da Informação (CIDAN)*, a segurança da informação é definida pela norma ABNT NBR ISO/IEC 27000 como a preservação da confidencialidade, integridade e disponibilidade da informação, admitindo-se adicionalmente propriedades vitais para transações formais como a autenticidade e o não repúdio.
>
> **Gabarito: A**

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
