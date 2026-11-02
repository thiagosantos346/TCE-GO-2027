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
**(FGV – TJ/SC – 2026 – Analista Administrativo)**
Na empresa ABC, a área tradicionalmente denominada "Recursos Humanos" passa por ampla reformulação, refletindo o novo contexto organizacional marcado por mudanças vertiginosas, dinâmicas exponenciais e pela confluência de fatores econômicos, tecnológicos, sociais, culturais, legais, políticos, demográficos e ecológicos. A Diretoria avalia a substituição da nomenclatura por termos que melhor expressem os novos espaços, configurações e propósitos assumidos pela área. Considerando as transformações contemporâneas que afetam a Gestão de Pessoas, assinale a opção que apresenta uma terminologia compatível com essa reformulação.

* **A)** Gestão do Capital Intelectual.
* **B)** Gestão de Suprimentos.
* **C)** Gestão Patrimonial.
* **D)** Gestão de Compliance.
* **E)** Gestão Tributária.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *3. Gestão e Análise de Riscos de Segurança da Informação* deste guia, a gestão de riscos estabelece um processo contínuo e estruturado para identificar incertezas, avaliar a probabilidade de falhas e selecionar salvaguardas economicamente proporcionais. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/SC/2026) ao estabelecer que "Gestão do Capital Intelectual".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Gestão de Suprimentos". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, a norma ABNT NBR ISO/IEC 27001 estabelece os requisitos formais para estabelecer, implementar, manter e melhorar continuamente um Sistema de Gestão de Segurança da Informação (SGSI).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Gestão Patrimonial". De acordo com a teoria estudada em *5.2 A Nova ISO/IEC 27002 (Edição 2022: 4 Temas e 93 Controles)*, cONTROLES ORGANIZACIONAIS (37 controles) ──► Políticas, gestão de ativos,.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Gestão de Compliance". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, nIST SP 800 30 Rev. 1 Guide for Conducting Risk Assessments Guia metodológico oficial para condução de processos de avaliação e gestão de riscos em segurança da informação.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Gestão Tributária". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, governo Digital Programa de Privacidade e Segurança da Informação (PPSI 2.0) Diretrizes, requisitos de maturidade e gestão de riscos cibernéticos para a administração pública.
>
> **Gabarito: A**

---


### Teste 002
**(FGV – TJ/SC – 2026 – Analista Administrativo)**
No Brasil, o planejamento governamental estrutura-se em instrumentos articulados que operam em diferentes horizontes temporais e níveis de detalhamento, traduzindo as estratégias de médio prazo em metas anuais e em programas finalísticos voltados à entrega de resultados à sociedade. O instrumento de planejamento de médio prazo, com vigência de quatro anos, no qual são definidos os eixos, os objetivos estratégicos e os programas finalísticos da Administração Pública para o período, servindo de referência para a elaboração dos orçamentos anuais subsequentes, denomina-se

* **A)** Orçamento Anual.
* **B)** Diretrizes Orçamentárias.
* **C)** Plano Plurianual.
* **D)** Plano de Contingência Orçamentária.
* **E)** Plano de Aplicação Financeira.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Orçamento Anual". De acordo com a teoria estudada em *3.2 Análise Qualitativa vs. Análise Quantitativa (SLE, ARO e ALE)*, aLE ( Annualized Loss Expectancy Expectativa de Perda Anual).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Diretrizes Orçamentárias". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, governo Digital Programa de Privacidade e Segurança da Informação (PPSI 2.0) Diretrizes, requisitos de maturidade e gestão de riscos cibernéticos para a administração pública.
> - **C)** **Correta.** Conforme fundamentado na seção *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL* deste guia, cláusula 6: Planejamento (Tratamento de riscos e objetivos de segurança). Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/SC/2026) ao estabelecer que "Plano Plurianual".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Plano de Contingência Orçamentária". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, aceitar / Reter ( Risk Acceptance / Retention ): Manter o risco no nível atual sem novos controles, mediante aprovação formal fundamentada da alta administração, quando o custo da salvaguarda técnica for superior à perda monetária potencial estimada.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Plano de Aplicação Financeira". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, transferir / Compartilhar ( Risk Transfer / Sharing ): Compartilhar a carga financeira ou operacional das perdas com terceiros (ex.: contratação de apólice de seguro contra incidentes cibernéticos ou terceirização da infraestrutura de datacenter para provedores de nuvem sob contratos de SLA estritos).
>
> **Gabarito: C**

---


### Teste 003
**(FGV – TJ/SC – 2026 – Analista Administrativo)**
A Lei nº 13.019/2014, denominada Marco Regulatório das Organizações da Sociedade Civil (MROSC), estabelece o regime jurídico das parcerias entre a Administração Pública e as organizações da sociedade civil, instituindo três instrumentos jurídicos distintos para a formalização dessas parcerias. Relacione os instrumentos jurídicos previstos no MROSC às respectivas características. Instrumento Característica 1. Termo de ( ) Adotado em parcerias que envolvem colaboração transferência de recursos financeiros e cujo plano de trabalho é proposto pela Administração Pública 2. Termo de ( ) Adotado em parcerias que não fomento envolvem transferência de recursos financeiros entre os parceiros 3. Acordo de ( ) Adotado em parcerias que envolvem cooperação transferência de recursos financeiros e cujo plano de trabalho é proposto pela organização da sociedade civil Assinale a opção que indica a relação correta, na ordem apresentada.

* **A)** 1 – 2 – 3.
* **B)** 2 – 3 – 1.
* **C)** 1 – 3 – 2.
* **D)** 3 – 1 – 2.
* **E)** 2 – 1 – 3.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "1 – 2 – 3". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, grau de Sigilo: Prazo Máximo de Restrição — Competência Originária Típica para Classificar — Regime de Prorrogação.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "2 – 3 – 1". De acordo com a teoria estudada em *5.2 A Nova ISO/IEC 27002 (Edição 2022: 4 Temas e 93 Controles)*, cONTROLES DE PESSOAS ( 8 controles) ──► Recrutamento, trabalho remoto,.
> - **C)** **Correta.** Conforme fundamentado na seção *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)* deste guia, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/SC/2026) ao estabelecer que "1 – 3 – 2".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "3 – 1 – 2". De acordo com a teoria estudada em *5.3 A Declaração de Aplicabilidade (SoA) e a ISO/IEC 27005*, a justificativa formal obrigatória para a exclusão de qualquer controle que não tenha sido adotado.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "2 – 1 – 3". De acordo com a teoria estudada em *3. Gestão e Análise de Riscos de Segurança da Informação*, a gestão de riscos estabelece um processo contínuo e estruturado para identificar incertezas, avaliar a probabilidade de falhas e selecionar salvaguardas economicamente proporcionais.
>
> **Gabarito: C**

---


### Teste 004
**(FGV – TJ/SC – 2026 – Analista Administrativo)**
Durante a execução orçamentária federal, verificou-se a utilização de emendas do relator para alocação de recursos públicos sem identificação clara dos parlamentares beneficiários nem transparência quanto à destinação final das verbas. À luz da Constituição Federal e da jurisprudência do Supremo Tribunal Federal, é correto afirmar que tal prática, denominada de “orçamento secreto”, é

* **A)** válida, pois decorre da discricionariedade parlamentar na alocação de recursos orçamentários.
* **B)** legítima, desde que haja previsão genérica na lei orçamentária anual.
* **C)** inconstitucional, pois as emendas do relator violam os princípios da unidade e da anualidade.
* **D)** regular, desde que os recursos sejam aplicados em políticas públicas de interesse social.
* **E)** incompatível com os princípios da transparência, publicidade e planejamento orçamentário.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "válida, pois decorre da discricionariedade parlamentar na alocação de recursos orçamentários". De acordo com a teoria estudada em *4.1 Métricas do CVSS v3.1 (Common Vulnerability Scoring System)*, scope (S): Escopo Inalterado ( Unchanged ) ou Alterado ( Changed , quando a falha compromete recursos fora de sua camada de autorização).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "legítima, desde que haja previsão genérica na lei orçamentária anual". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "inconstitucional, pois as emendas do relator violam os princípios da unidade e da anualidade". De acordo com a teoria estudada em *1. Princípios Básicos da Segurança da Informação (CIDAN)*, a segurança da informação é definida pela norma ABNT NBR ISO/IEC 27000 como a preservação da confidencialidade, integridade e disponibilidade da informação, admitindo se adicionalmente propriedades vitais para transações formais como a autenticidade e o não repúdio. O mnemônico padronizado em concursos da FCC é CIDAN.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "regular, desde que os recursos sejam aplicados em políticas públicas de interesse social". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, cláusula 7: Apoio (Recursos, capacitação, conscientização e comunicação).
> - **E)** **Correta.** Conforme fundamentado na seção *2.2 Classificação Corporativa Geral de Ativos* deste guia, pública: Informação destinada à divulgação irrestrita (editais de licitação, acórdãos públicos, portal da transparência); o vazamento gera dano nulo. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/SC/2026) ao estabelecer que "incompatível com os princípios da transparência, publicidade e planejamento orçamentário".
>
> **Gabarito: E**

---


### Teste 005
**(FGV – TJ/SC – 2026 – Analista Administrativo)**
Em audiência pública promovida por determinada Secretaria Estadual, o Secretário afirmou aos presentes que a divulgação ampla de dados sobre execução orçamentária, contratos e despesas correntes não constitui mera formalidade administrativa, mas pressuposto para que a comunidade exerça efetivo acompanhamento sobre os gastos públicos. Acrescentou que o desenvolvimento de condições e arranjos institucionais voltados a aproximar a Administração Pública do cidadão é expediente necessário ao combate à corrupção. A manifestação do Secretário guarda correspondência com a noção de transparência pública, na medida em que se assenta, fundamentalmente, na

* **A)** exigência de participação da comunidade no controle dos gastos públicos, mediante o desenvolvimento de condições institucionais que permitam o acompanhamento da atuação administrativa pela sociedade.
* **B)** atribuição da fiscalização dos atos do administrador público à estrutura interna de controle do próprio ente federativo, no exercício de suas competências institucionais ordinárias.
* **C)** consolidação de sigilo amplo sobre informações financeiras e orçamentárias, de modo a preservar a estabilidade institucional da Administração Pública.
* **D)** restrição do acesso a informações administrativas aos cidadãos previamente cadastrados em sistemas de identificação biométrica.
* **E)** atuação técnico-fiscalizatória dos Tribunais de Contas, cujo aparato especializado supre, em sede de controle externo, as exigências do princípio republicano, cabendo à divulgação à sociedade função meramente subsidiária.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *2.2 Classificação Corporativa Geral de Ativos* deste guia, pública: Informação destinada à divulgação irrestrita (editais de licitação, acórdãos públicos, portal da transparência); o vazamento gera dano nulo. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/SC/2026) ao estabelecer que "exigência de participação da comunidade no controle dos gastos públicos, mediante o desenvolvimento de condições...".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "atribuição da fiscalização dos atos do administrador público à estrutura interna de controle do próprio ente...". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, aceitar / Reter ( Risk Acceptance / Retention ): Manter o risco no nível atual sem novos controles, mediante aprovação formal fundamentada da alta administração, quando o custo da salvaguarda técnica for superior à perda monetária potencial estimada.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "consolidação de sigilo amplo sobre informações financeiras e orçamentárias, de modo a preservar a estabilidade...". De acordo com a teoria estudada em *2.2 Classificação Corporativa Geral de Ativos*, confidencial: Informações estratégicas, relatórios preliminares de auditoria em instrução ou dados cadastrais sob sigilo fiscal; vazamento gera dano financeiro ou institucional grave.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "restrição do acesso a informações administrativas aos cidadãos previamente cadastrados em sistemas de...". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "atuação técnico fiscalizatória dos Tribunais de Contas, cujo aparato especializado supre, em sede de controle...". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, secreta: 15 anos — Titulares de autarquias, fundações e órgãos públicos sob mesma alçada legal — Não admite prorrogação. O prazo cessa impreterivelmente aos 15 anos.
>
> **Gabarito: A**

---


### Teste 006
**(FGV – TCE/GO – 2024 – Analista de Controle Externo - Ciências Contábeis)**
Em 2022, uma sociedade empresária reconheceu lucro de R$600.000. Na Demonstração das Mutações do Patrimônio Líquido de 31/12/2022, reconheceu distribuição de dividendos de R$150.000, que foram pagos aos sócios em 2023. Já em 2023, a sociedade empresária reconheceu lucro de R$800.000. Na Demonstração das Mutações do Patrimônio Líquido de 31/12/2023, reconheceu a distribuição de dividendos relativas ao ano no montante de R$200.000. Também em 2023, reconheceu a distribuição de dividendos adicionais, relativos ao lucro auferido em 2022, de R$70.000. Os dois valores foram pagos em 2024. Na Demonstração do Valor Adicionado de 31/12/2023, o seguinte montante foi reconhecido como distribuição do valor adicionado, em dividendos

* **A)** R$70.000.
* **B)** R$150.000.
* **C)** R$200.000.
* **D)** R$220.000.
* **E)** R$270.000. Contabilidade Pública

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "R$70.000". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, decore rigorosamente os prazos decrescentes: 25 anos $\rightarrow$ 15 anos $\rightarrow$ 5 anos. A FCC inventa prazos alternativos inexistentes (como 10 ou 20 anos) ou inverte Secreta e Reservada. Além disso, lembre se: informações relativas à intimidade, vida privada, honra e imagem das pessoas têm restrição de acesso máxima de até 100 anos a contar da data de sua produção (Art. 31 da LAI), não se confundindo com prazos de segurança de Estado!.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "R$150.000". De acordo com a teoria estudada em *3.2 Análise Qualitativa vs. Análise Quantitativa (SLE, ARO e ALE)*, mensura as perdas e investimentos em valores monetários concretos (R$).
> - **C)** **Correta.** Conforme fundamentado na seção *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)* deste guia, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/GO/2024) ao estabelecer que "R$200.000".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "R$220.000". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, aSSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. ABNT NBR ISO/IEC 27005:2023: Segurança da informação, segurança cibernética e proteção da privacidade — Gestão de riscos de segurança da informação. Rio de Janeiro: ABNT, 2023.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "R$270.000. Contabilidade Pública". De acordo com a teoria estudada em *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade*, (O que tem valor econômico ou funcional.
>
> **Gabarito: C**

---


### Teste 007
**(FGV – TCE/GO – 2024 – Analista de Controle Externo - Ciências Contábeis)**
O Relatório Resumido da Execução Orçamentária (RREO) é divulgado mensalmente pela União. De acordo com o Manual de Demonstrativos Fiscais, o objetivo dessa periodicidade é

* **A)** oferecer segurança à sociedade, de modo a aumentar a arrecadação.
* **B)** assegurar que as informações são livres de fraude e de erro e que a transparência é valorizada.
* **C)** mostrar à sociedade que o Governo Federal cumpre com as suas responsabilidades perante ela.
* **D)** servir de exemplo e estimular que outras entidades públicas divulguem os seus relatórios com regularidade.
* **E)** permitir que a sociedade conheça, acompanhe e analise o desempenho da execução orçamentária do Governo Federal.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "oferecer segurança à sociedade, de modo a aumentar a arrecadação". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, cláusula 8: Operação (Execução do tratamento de riscos de segurança).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "assegurar que as informações são livres de fraude e de erro e que a transparência é valorizada". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "mostrar à sociedade que o Governo Federal cumpre com as suas responsabilidades perante ela". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, cláusula 9: Avaliação de Desempenho (Auditorias internas e análise pela direção).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "servir de exemplo e estimular que outras entidades públicas divulguem os seus relatórios com regularidade". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, garantia de que o acesso à informação é restrito estrita e exclusivamente a pessoas, entidades ou processos formalmente autorizados.
> - **E)** **Correta.** Conforme fundamentado na seção *3.2 Análise Qualitativa vs. Análise Quantitativa (SLE, ARO e ALE)* deste guia, vantagem: Rápida execução, baixo custo analítico e de fácil compreensão gerencial. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/GO/2024) ao estabelecer que "permitir que a sociedade conheça, acompanhe e analise o desempenho da execução orçamentária do Governo Federal".
>
> **Gabarito: E**

---


### Teste 008
**(FGV – TCE/GO – 2024 – Analista de Controle Externo - Ciências Contábeis)**
Uma empresa de auditoria apresentava os seguintes saldos em seus ativos e passivos, em 31/12/2023: Fornecedores (120 dias): R$30.000; Salários a pagar (30 dias): 40.000; Adiantamento a sócio (60 dias): R$50.000; Contas a pagar (180 dias): R$50.000; Receitas antecipadas (210 dias): R$80.000; Empréstimo bancário (420 dias): R$120.000; Clientes (360 dias): R$190.000; Caixa: R$300.000. A empresa calculou o índice de composição das exigibilidades em 31/12/2023, de modo a verificar a participação das obrigações com terceiros de curto prazo em relação ao total de suas obrigações com terceiros. Assinale a opção que indica o indicador obtido.

* **A)** 0,37
* **B)** 0,50
* **C)** 0,59
* **D)** 0,63
* **E)** 0,68

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "0,37". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, mecanismos técnicos: Funções criptográficas de espalhamento ( hashing criptográfico como SHA 256 e SHA 512), códigos de autenticação de mensagem (HMAC), assinaturas digitais, somas de verificação ( checksums ) e trilhas de auditoria imutáveis.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "0,50". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, transferir / Compartilhar ( Risk Transfer / Sharing ): Compartilhar a carga financeira ou operacional das perdas com terceiros (ex.: contratação de apólice de seguro contra incidentes cibernéticos ou terceirização da infraestrutura de datacenter para provedores de nuvem sob contratos de SLA estritos).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "0,59". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, aSSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. ABNT NBR ISO/IEC 27005:2023: Segurança da informação, segurança cibernética e proteção da privacidade — Gestão de riscos de segurança da informação. Rio de Janeiro: ABNT, 2023.
> - **D)** **Correta.** Conforme fundamentado na seção *2.2 Classificação Corporativa Geral de Ativos* deste guia, confidencial: Informações estratégicas, relatórios preliminares de auditoria em instrução ou dados cadastrais sob sigilo fiscal; vazamento gera dano financeiro ou institucional grave. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/GO/2024) ao estabelecer que "0,63".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "0,68". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, garantia de que a informação, os sistemas computacionais e os ativos de telecomunicações associados estejam acessíveis e utilizáveis sob demanda pelos usuários autorizados sempre que necessário.
>
> **Gabarito: D**

---


### Teste 009
**(FGV – TCE/GO – 2024 – Analista de Controle Externo - Ciências Contábeis)**
Uma sociedade empresária apresentava os seguintes saldos em seu balanço patrimonial, em 31/12/2023: Caixa: R$4.000; Conta corrente no banco: R$8.000; Aplicação financeira com resgate em 80 dias: R$10.000; Contas a pagar em 60 dias: R$13.000; Empréstimos com vencimento em 540 dias: R$29.000; Patrimônio Líquido: R$80.000; Terrenos para valorização: R$100.000. Assinale a opção que indica a liquidez imediata da sociedade empresária em 31/12/2023.

* **A)** 0,10
* **B)** 0,31
* **C)** 0,52
* **D)** 0,92
* **E)** 1,69

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "0,10". De acordo com a teoria estudada em *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade*, ex.: banco de dados tributário do TCE GO).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "0,31". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, transferir / Compartilhar ( Risk Transfer / Sharing ): Compartilhar a carga financeira ou operacional das perdas com terceiros (ex.: contratação de apólice de seguro contra incidentes cibernéticos ou terceirização da infraestrutura de datacenter para provedores de nuvem sob contratos de SLA estritos).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "0,52". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, nIST SP 800 37 Rev. 2 Risk Management Framework Diretrizes para aplicação do Risk Management Framework (RMF) aos sistemas e organizações.
> - **D)** **Correta.** Conforme fundamentado na seção *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)* deste guia, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/GO/2024) ao estabelecer que "0,92".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "1,69". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, aSSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. ABNT NBR ISO/IEC 27005:2023: Segurança da informação, segurança cibernética e proteção da privacidade — Gestão de riscos de segurança da informação. Rio de Janeiro: ABNT, 2023.
>
> **Gabarito: D**

---


### Teste 010
**(FGV – TCE/GO – 2024 – Analista de Controle Externo - Controle Externo)**
O planejamento nas organizações públicas é uma pedra angular para garantir a eficiência e a eficácia na entrega de serviços à sociedade. No entanto, é imperativo reconhecer que esse processo está passando por uma redefinição e realinhamento devido às transformações significativas na realidade contemporânea. Tais mudanças são impulsionadas pela globalização, avanços tecnológicos e evolução das expectativas dos cidadãos. Assim, o planejamento público está se adaptando dinamicamente para abraçar essas mudanças, garantindo que os serviços oferecidos estejam alinhados com as necessidades emergentes da comunidade e sejam entregues de maneira efetiva e oportuna. Assinale, dentre as opções a seguir, a que apresenta uma mudança da função de planejamento.

* **A)** O enfoque no potencial é substituído pela ênfase na previsão, direcionando a atenção para a elaboração de cenários futuros.
* **B)** As fronteiras entre o planejamento estratégico e o planejamento tático se mesclam de forma dissociável.
* **C)** A transição de uma estrutura organizacional horizontal e aberta para um processo flexível, no qual as relações que facilitam a troca de informações predominam.
* **D)** A base do novo planejamento muda de uma estrutura organizacional vertical e hierárquica para um processo fluido, horizontal e livre.
* **E)** O conteúdo estratégico tem maior importância do que o processo estratégico.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O enfoque no potencial é substituído pela ênfase na previsão, direcionando a atenção para a elaboração de cenários...". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, evitar / Eliminar ( Risk Avoidance ): Descontinuar a atividade, processo ou serviço gerador do risco (ex.: desligar e desativar em definitivo um sistema legado vulnerável sem suporte do fabricante).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "As fronteiras entre o planejamento estratégico e o planejamento tático se mesclam de forma dissociável". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, cláusula 6: Planejamento (Tratamento de riscos e objetivos de segurança).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A transição de uma estrutura organizacional horizontal e aberta para um processo flexível, no qual as relações que...". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A base do novo planejamento muda de uma estrutura organizacional vertical e hierárquica para um processo fluido...". De acordo com a teoria estudada em *5.3 A Declaração de Aplicabilidade (SoA) e a ISO/IEC 27005*, iSO/IEC 27005: Norma que fornece diretrizes especializadas para o processo de avaliação e tratamento de riscos de segurança da informação no suporte ao SGSI.
> - **E)** **Correta.** Conforme fundamentado na seção *3. Gestão e Análise de Riscos de Segurança da Informação* deste guia, a gestão de riscos estabelece um processo contínuo e estruturado para identificar incertezas, avaliar a probabilidade de falhas e selecionar salvaguardas economicamente proporcionais. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/GO/2024) ao estabelecer que "O conteúdo estratégico tem maior importância do que o processo estratégico".
>
> **Gabarito: E**

---


### Teste 011
**(FGV – TCE/GO – 2024 – Analista de Controle Externo - Engenharia)**
Orçamento de uma obra compõe-se pela identificação, descrição, quantificação e valoração da mão de obra, equipamentos e materiais utilizados na obra, custos financeiros, impostos, riscos e margem de lucro desejada, para a adequada previsão do preço final. A elaboração do orçamento requer o conhecimento de conceitos, que são fundamentais para a utilização das referências dos Sistemas de Custo disponíveis. Associe os conceitos listados a seguir com as respectivas descrições: 1. Bonificação 2. Despesa Fixa 3. Despesa Variável 4. Custo Indireto 5. Custo Direto ( ) Mobilização e desmobilização; ( ) Tributação sobre faturamento; ( ) Manutenção da sede da empresa; ( ) Materiais usados na obra; ( ) Remuneração da empresa pelo desenvolvimento de sua atividade econômica A sequência correta da numeração, na ordem apresentada é

* **A)** 5 – 1 – 4 – 3 – 2.
* **B)** 4 – 3 – 2 – 5 – 1.
* **C)** 3 – 4 – 2 – 5 – 1.
* **D)** 3 – 4 – 1 – 5 – 2.
* **E)** 5 – 3 – 2 – 4 – 1.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "5 – 1 – 4 – 3 – 2". De acordo com a teoria estudada em *3.2 Análise Qualitativa vs. Análise Quantitativa (SLE, ARO e ALE)*, onde $\text{ACS}$ ( Annualized Cost of Safeguard ) é o custo anual de manutenção do controle. Se o saldo for positivo, o controle de segurança é economicamente viável.
> - **B)** **Correta.** Conforme fundamentado na seção *🌐 Fontes Oficiais e Referências Bibliográficas* deste guia, nIST Cybersecurity Framework (CSF 2.0) Estrutura de referência global do NIST para identificação, proteção, detecção, resposta e recuperação de riscos cibernéticos. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/GO/2024) ao estabelecer que "4 – 3 – 2 – 5 – 1".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "3 – 4 – 2 – 5 – 1". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, garantia de que a informação, os sistemas computacionais e os ativos de telecomunicações associados estejam acessíveis e utilizáveis sob demanda pelos usuários autorizados sempre que necessário.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "3 – 4 – 1 – 5 – 2". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, mecanismos técnicos: Redundância de hardware e fontes de alimentação, clusters de alta disponibilidade (HA ativo ativo ou ativo passivo), sistemas anti DDoS, geradores e nobreaks comutáveis, planos de continuidade de negócios (PCN/DRP) e rotinas estruturadas de backup.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "5 – 3 – 2 – 4 – 1". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, nIST SP 800 37 Rev. 2 Risk Management Framework Diretrizes para aplicação do Risk Management Framework (RMF) aos sistemas e organizações.
>
> **Gabarito: B**

---


### Teste 012
**(FGV – TCE/GO – 2024 – Analista de Controle Externo - Jurídica)**
O Presidente da República editou o Decreto nº X, o qual dispôs sobre o seguinte: I. extinção dos órgãos públicos Alfa e Beta, com realocação dos respectivos ocupantes, o que decorria da exponencial diminuição de suas atividades, fruto de alterações no ambiente social; II. extinção dos cargos em comissão de simbologia W, na medida em que vagassem; III. disciplina da organização da Administração Pública federal. Por discordar das medidas adotadas, o Partido Político Alfa, com representação no Congresso Nacional, consultou sua assessoria jurídica em relação à conformidade constitucional das medidas adotadas. A assessoria informou que é constitucional o que consta em

* **A)** I, II e III.
* **B)** I, apenas.
* **C)** III, apenas.
* **D)** I e II, apenas.
* **E)** II e III, apenas.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I, II e III". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, decreto Federal nº 9.637/2018 (Política Nacional de Segurança da Informação) Institui a PNSI, dispondo sobre governança, gestão de riscos e tratamento de incidentes de segurança da informação.
> - **B)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I, apenas". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, secreta: 15 anos — Titulares de autarquias, fundações e órgãos públicos sob mesma alçada legal — Não admite prorrogação. O prazo cessa impreterivelmente aos 15 anos.
> - **C)** **Correta.** Conforme fundamentado na seção *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)* deste guia, ultrassecreta: 25 anos — Presidente da República, Vice Presidente, Ministros de Estado, Comandantes das Forças Armadas — Prorrogável uma única vez, por igual período (totalizando até 50 anos), exclusivamente pela CMRI ( Comissão Mista de Reavaliação de Informações ). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/GO/2024) ao estabelecer que "III, apenas".
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e II, apenas". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Escuta clandestina de rede ( sniffing/eavesdropping ), roubo de dispositivos físicos, engenharia social, vazamento inadvertido de dados fiscais protegidos por sigilo e acessos não autorizados.
> - **E)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II e III, apenas". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, propriedade de salvaguardar a exatidão, originalidade e completude da informação e de seus métodos de processamento, impedindo alterações, corrupções ou supressões indevidas ou não autorizadas.
>
> **Gabarito: C**

---


### Teste 013
**(FGV – TCE/GO – 2024 – Analista de Controle Externo - Jurídica)**
Em julgamento ocorrido no final do ano de 2022, em sede de controle concentrado de constitucionalidade, o STF analisou o denominado “orçamento secreto”. Com relação ao tema e considerando o julgamento do STF, assinale a afirmativa correta.

* **A)** O orçamento secreto observa os postulados da publicidade e transparência através da disponibilização nos sites oficiais do Governo Federal das informações sobre a execução orçamentaria das emendas do relator.
* **B)** Trata-se de um regime em que vincula o autor da emenda ao beneficiário da despesa, tornando verificáveis a origem e destinação do dinheiro gasto por meio do cruzamento das informações publicadas, sendo, portanto, constitucional.
* **C)** O orçamento secreto oculta os efetivos requerentes da despesa, por meio da utilização de rubrica orçamentária única, na qual todas as despesas previstas são atribuídas à pessoa do relator-geral do orçamento.
* **D)** O orçamento secreto deve destinar obrigatoriamente as despesas para ações e serviços públicos de saúde e de assistência social, e oculta os valores individualizados das emendas do relator.
* **E)** As emendas parlamentares ao orçamento secreto possuem autorização constitucional e objetivam viabilizar a participação ativa dos Deputados Federais e Senadores na elaboração da peça orçamentária.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O orçamento secreto observa os postulados da publicidade e transparência através da disponibilização nos sites...". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Trata se de um regime em que vincula o autor da emenda ao beneficiário da despesa, tornando verificáveis a origem...". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, ultrassecreta: 25 anos — Presidente da República, Vice Presidente, Ministros de Estado, Comandantes das Forças Armadas — Prorrogável uma única vez, por igual período (totalizando até 50 anos), exclusivamente pela CMRI ( Comissão Mista de Reavaliação de Informações ).
> - **C)** **Correta.** Conforme fundamentado na seção *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)* deste guia, uLTRASSECRETA ──► Prazo Máximo: 25 ANOS (Prorrogável 1 única vez por igual período). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/GO/2024) ao estabelecer que "O orçamento secreto oculta os efetivos requerentes da despesa, por meio da utilização de rubrica orçamentária...".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O orçamento secreto deve destinar obrigatoriamente as despesas para ações e serviços públicos de saúde e de...". De acordo com a teoria estudada em *2.2 Classificação Corporativa Geral de Ativos*, pública: Informação destinada à divulgação irrestrita (editais de licitação, acórdãos públicos, portal da transparência); o vazamento gera dano nulo.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "As emendas parlamentares ao orçamento secreto possuem autorização constitucional e objetivam viabilizar a...". De acordo com a teoria estudada em *4.1 Métricas do CVSS v3.1 (Common Vulnerability Scoring System)*, scope (S): Escopo Inalterado ( Unchanged ) ou Alterado ( Changed , quando a falha compromete recursos fora de sua camada de autorização).
>
> **Gabarito: C**

---


### Teste 014
**(FGV – TJ/AP – 2023 – Analista Judiciario Apoio Especializado Tecnologia Da Informacao Banco De Dados)**
A analista Joana implementou o sistema de autorização da aplicação TJApp utilizando o protocolo OAuth2. Joana decidiu por implementar o fluxo do OAuth2 de concessão por código de autorização. A fim de indicar ao servidor de autorização o fluxo de concessão escolhido, Joana atribuiu ao parâmetro response_type da requisição de autorização de TJApp o valor associado ao fluxo implementado, conforme a especificação do OAuth2. Joana atribuiu ao response_type o valor:

* **A)** code;
* **B)** token;
* **C)** auth-code;
* **D)** access-token;
* **E)** client-credentials. Realização

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL* deste guia, a norma ABNT NBR ISO/IEC 27001 estabelece os requisitos formais para estabelecer, implementar, manter e melhorar continuamente um Sistema de Gestão de Segurança da Informação (SGSI). Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/AP/2023) ao estabelecer que "code".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "token". De acordo com a teoria estudada em *4.1 Métricas do CVSS v3.1 (Common Vulnerability Scoring System)*, scope (S): Escopo Inalterado ( Unchanged ) ou Alterado ( Changed , quando a falha compromete recursos fora de sua camada de autorização).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "auth code". De acordo com a teoria estudada em *4.2 As Quatro Fases do Ciclo de Resposta a Incidentes (NIST SP 800-61)*, recuperação: Restaurar sistemas para operação produtiva plena utilizando cópias seguras de backup, testando sua estabilidade.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "access token". De acordo com a teoria estudada em *5.2 A Nova ISO/IEC 27002 (Edição 2022: 4 Temas e 93 Controles)*, a norma ISO/IEC 27002 constitui um Código de Práticas que detalha diretrizes para implementação dos controles de segurança do Anexo A da ISO 27001. Não é passível de certificação independente.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "client credentials. Realização". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, nIST SP 800 37 Rev. 2 Risk Management Framework Diretrizes para aplicação do Risk Management Framework (RMF) aos sistemas e organizações.
>
> **Gabarito: A**

---


### Teste 015
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
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Screened Host". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Escuta clandestina de rede ( sniffing/eavesdropping ), roubo de dispositivos físicos, engenharia social, vazamento inadvertido de dados fiscais protegidos por sigilo e acessos não autorizados.
> - **C)** **Correta.** Conforme fundamentado na seção *4.2 As Quatro Fases do Ciclo de Resposta a Incidentes (NIST SP 800-61)* deste guia, contenção: Ação emergencial prioritária voltada a estancar a disseminação do ataque e limitar o raio de destruição ( blast radius ), tal como isolar a máquina da rede, desconectar cabos ou bloquear portas de switches. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/AP/2023) ao estabelecer que "Screened Subnet".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Dual Homed Host". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Adulteração maliciosa de tabelas contábeis ou salariais em bancos de dados ( tampering ), infecção por malware, ataques man in the middle e erros de transmissão de rede sem checagem de paridade.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Stateful Inspection". De acordo com a teoria estudada em *3.2 Análise Qualitativa vs. Análise Quantitativa (SLE, ARO e ALE)*, utiliza escalas ordinais descritivas (ex.: Baixo, Médio, Alto, Crítico) distribuídas em uma Matriz de Probabilidade vs. Impacto.
>
> **Gabarito: C**

---


### Teste 016
**(FGV – TJ/AP – 2023 – Analista Judiciario Apoio Especializado Tecnologia Da Informacao Seguranca Da Informacao)**
Como parte da Governança e Gestão de Tecnologia da Informação (TI), um Tribunal de Justiça desenvolveu novos serviços digitais para a sociedade. Após a entrega dos serviços digitais, foram criados meios para o monitoramento da qualidade com o intuito de capturar a percepção de benefícios pela sociedade e atender a melhoria contínua dos serviços. O monitoramento da qualidade dos serviços digitais disponibilizados à sociedade representa uma ação estratégica de:

* **A)** implantação dos serviços;
* **B)** sustentação dos serviços;
* **C)** otimização do processo do serviço;
* **D)** priorização de serviços;
* **E)** abrangência dos resultados dos serviços.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "implantação dos serviços". De acordo com a teoria estudada em *4.2 As Quatro Fases do Ciclo de Resposta a Incidentes (NIST SP 800-61)*, preparação ( Preparation ): Estabelecimento e capacitação da equipe técnica de resposta (CSIRT / CERT), aquisição de ferramentas de investigação forense, implantação de políticas e planos de comunicação.
> - **B)** **Correta.** Conforme fundamentado na seção *🌐 Fontes Oficiais e Referências Bibliográficas* deste guia, decreto Federal nº 9.637/2018 (Política Nacional de Segurança da Informação) Institui a PNSI, dispondo sobre governança, gestão de riscos e tratamento de incidentes de segurança da informação. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/AP/2023) ao estabelecer que "sustentação dos serviços".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "otimização do processo do serviço". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, evitar / Eliminar ( Risk Avoidance ): Descontinuar a atividade, processo ou serviço gerador do risco (ex.: desligar e desativar em definitivo um sistema legado vulnerável sem suporte do fabricante).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "priorização de serviços". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, aSSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. ABNT NBR ISO/IEC 27001:2022: Tecnologia da informação — Técnicas de segurança — Sistemas de gestão da segurança da informação — Requisitos. Rio de Janeiro: ABNT, 2022.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "abrangência dos resultados dos serviços". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, melhoria Contínua: Opera tradicionalmente alicerçada no ciclo PDCA ( Plan, Do, Check, Act ).
>
> **Gabarito: B**

---


### Teste 017
**(FGV – TJ/AP – 2023 – Analista Judiciario Apoio Especializado Tecnologia Da Informacao Seguranca Da Informacao)**
A Governança de Tecnologia da Informação (TI) deverá ser implantada com base no(a):

* **A)** área focal tecnológica;
* **B)** gestão por projetos;
* **C)** ativo operacional;
* **D)** colaboração da sociedade;
* **E)** transparência e prestação de contas.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "área focal tecnológica". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, decreto Federal nº 9.637/2018 (Política Nacional de Segurança da Informação) Institui a PNSI, dispondo sobre governança, gestão de riscos e tratamento de incidentes de segurança da informação.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "gestão por projetos". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, aSSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. ABNT NBR ISO/IEC 27001:2022: Tecnologia da informação — Técnicas de segurança — Sistemas de gestão da segurança da informação — Requisitos. Rio de Janeiro: ABNT, 2022.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "ativo operacional". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, transferir / Compartilhar ( Risk Transfer / Sharing ): Compartilhar a carga financeira ou operacional das perdas com terceiros (ex.: contratação de apólice de seguro contra incidentes cibernéticos ou terceirização da infraestrutura de datacenter para provedores de nuvem sob contratos de SLA estritos).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "colaboração da sociedade". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes.
> - **E)** **Correta.** Conforme fundamentado na seção *2.2 Classificação Corporativa Geral de Ativos* deste guia, pública: Informação destinada à divulgação irrestrita (editais de licitação, acórdãos públicos, portal da transparência); o vazamento gera dano nulo. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/AP/2023) ao estabelecer que "transparência e prestação de contas".
>
> **Gabarito: E**

---


### Teste 018
**(CEBRASPE – TRF/6 – 2025 – Analista Judiciario Apoio Especializado Tecnologia Da Informacao)**
Em decorrência da recente experiência do Estado na prestação de serviços públicos digitais, associada tanto a características do setor público quanto a entraves legislativos, a administração pública substituiu a lógica de prestação de serviços digitais centrada no usuário, consagrada no setor privado, pela lógica burocrática do serviço público voltada essencialmente à efetividade junto aos cidadãos. De acordo com o CIS Controls, julgue os próximos itens.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Incorreta.** A proposição apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Em decorrência da recente experiência do Estado na prestação de serviços públicos digitais, associada tanto a...". De acordo com a teoria em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, secreta: 15 anos — Titulares de autarquias, fundações e órgãos públicos sob mesma alçada legal — Não admite prorrogação. O prazo cessa impreterivelmente aos 15 anos.
> - **E)** **Correta.** O item está **Errado** (gabarito oficial: **E**), pois contraria a disciplina teórica aplicável.
>
> **Gabarito: E**

---


### Teste 019
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


### Teste 020
**(FCC – TRT 9ª – 2015 – Analista Judiciário - Apoio Especializado - Tecnologia da Informação)**
Nos termos da Constituição Federal, é direito social a

* **A)** despoluição dos rios.
* **B)** proteção à maternidade.
* **C)** ao Superior Tribunal de Justiça, privativamente.
* **D)** ao Superior Tribunal de Justiça e aos Tribunais de
* **E)** aos Tribunais de Justiça, privativamente.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "despoluição dos rios". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, nIST Cybersecurity Framework (CSF 2.0) Estrutura de referência global do NIST para identificação, proteção, detecção, resposta e recuperação de riscos cibernéticos.
> - **B)** **Correta.** Conforme fundamentado na seção *2. Classificação e Rotulagem da Informação* deste guia, a classificação atribui rótulos de sensibilidade aos ativos de informação da organização, ditando os níveis de proteção lógica e física a serem aplicados de forma proporcional ao dano decorrente de divulgação ou modificação indevida. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 9ª/2015) ao estabelecer que "proteção à maternidade".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "ao Superior Tribunal de Justiça, privativamente". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, aceitar / Reter ( Risk Acceptance / Retention ): Manter o risco no nível atual sem novos controles, mediante aprovação formal fundamentada da alta administração, quando o custo da salvaguarda técnica for superior à perda monetária potencial estimada.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "ao Superior Tribunal de Justiça e aos Tribunais de". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, aSSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. ABNT NBR ISO/IEC 27005:2023: Segurança da informação, segurança cibernética e proteção da privacidade — Gestão de riscos de segurança da informação. Rio de Janeiro: ABNT, 2023.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "aos Tribunais de Justiça, privativamente". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Escuta clandestina de rede ( sniffing/eavesdropping ), roubo de dispositivos físicos, engenharia social, vazamento inadvertido de dados fiscais protegidos por sigilo e acessos não autorizados.
>
> **Gabarito: B**

---


### Teste 021
**(FGV – TRT da 24º Região – 2025 – Analista Judiciário - Área Administrativa - Contabilidade)**
Em dezembro de 2024, uma sociedade empresária recomprou suas próprias ações, que estavam com terceiros, para mantê-las em tesouraria. A contrapartida da diminuição em Disponibilidades é reconhecida como um(a)

* **A)** aumento no patrimônio líquido.
* **B)** aumento em investimentos.
* **C)** diminuição no patrimônio líquido.
* **D)** diminuição em investimentos.
* **E)** diminuição em financiamentos.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "aumento no patrimônio líquido". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, transferir / Compartilhar ( Risk Transfer / Sharing ): Compartilhar a carga financeira ou operacional das perdas com terceiros (ex.: contratação de apólice de seguro contra incidentes cibernéticos ou terceirização da infraestrutura de datacenter para provedores de nuvem sob contratos de SLA estritos).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "aumento em investimentos". De acordo com a teoria estudada em *3.2 Análise Qualitativa vs. Análise Quantitativa (SLE, ARO e ALE)*, mensura as perdas e investimentos em valores monetários concretos (R$).
> - **C)** **Correta.** Conforme fundamentado na seção *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)* deste guia, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT da 24º Região/2025) ao estabelecer que "diminuição no patrimônio líquido".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "diminuição em investimentos". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, cláusula 10: Melhoria (Não conformidades, ações corretivas e ciclo contínuo).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "diminuição em financiamentos". De acordo com a teoria estudada em *1. Princípios Básicos da Segurança da Informação (CIDAN)*, a segurança da informação é definida pela norma ABNT NBR ISO/IEC 27000 como a preservação da confidencialidade, integridade e disponibilidade da informação, admitindo se adicionalmente propriedades vitais para transações formais como a autenticidade e o não repúdio. O mnemônico padronizado em concursos da FCC é CIDAN.
>
> **Gabarito: C**

---


### Teste 022
**(FGV – TRT da 24º Região – 2025 – Analista Judiciário - Área Administrativa - Contabilidade)**
Uma sociedade empresária do setor de engenharia tem uma biblioteca, que é utilizada por seus empregados para obter informações técnicas. Os livros da biblioteca são classificados no balanço patrimonial da sociedade empresária como

* **A)** ativo intangível.
* **B)** Investimentos.
* **C)** ativo Imobilizado.
* **D)** ativo circulante.
* **E)** ativo realizável a longo prazo.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "ativo intangível". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, mecanismos técnicos: Redundância de hardware e fontes de alimentação, clusters de alta disponibilidade (HA ativo ativo ou ativo passivo), sistemas anti DDoS, geradores e nobreaks comutáveis, planos de continuidade de negócios (PCN/DRP) e rotinas estruturadas de backup.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Investimentos". De acordo com a teoria estudada em *3.2 Análise Qualitativa vs. Análise Quantitativa (SLE, ARO e ALE)*, mensura as perdas e investimentos em valores monetários concretos (R$).
> - **C)** **Correta.** Conforme fundamentado na seção *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)* deste guia, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT da 24º Região/2025) ao estabelecer que "ativo Imobilizado".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "ativo circulante". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Escuta clandestina de rede ( sniffing/eavesdropping ), roubo de dispositivos físicos, engenharia social, vazamento inadvertido de dados fiscais protegidos por sigilo e acessos não autorizados.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "ativo realizável a longo prazo". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, uLTRASSECRETA ──► Prazo Máximo: 25 ANOS (Prorrogável 1 única vez por igual período).
>
> **Gabarito: C**

---


### Teste 023
**(FGV – TRT da 24º Região – 2025 – Analista Judiciário - Área Administrativa - Contabilidade)**
Em 2024, uma sociedade empresária programou um treinamento para a sua equipe com o intuito de implementar as normas de sustentabilidade em sua estrutura. Em 2024 foram realizados treinamentos no valor de R$ 50.000, cujo pagamento estava previsto para 31/01/2025. Além disso, foram programados novos treinamentos a serem oferecidos em 2025, que custarão R$ 80.000. Assinale a opção que indica o saldo na conta “Provisão para Treinamento” no balanço patrimonial da sociedade empresária em 31/12/2024.

* **A)** Zero.
* **B)** R$ 30.000.
* **C)** R$ 50.000.
* **D)** R$ 80.000.
* **E)** R$ 130.000.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)* deste guia, decore rigorosamente os prazos decrescentes: 25 anos $\rightarrow$ 15 anos $\rightarrow$ 5 anos. A FCC inventa prazos alternativos inexistentes (como 10 ou 20 anos) ou inverte Secreta e Reservada. Além disso, lembre se: informações relativas à intimidade, vida privada, honra e imagem das pessoas têm restrição de acesso máxima de até 100 anos a contar da data de sua produção (Art. 31 da LAI), não se confundindo com prazos de segurança de Estado!. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT da 24º Região/2025) ao estabelecer que "Zero".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "R$ 30.000". De acordo com a teoria estudada em *2. Classificação e Rotulagem da Informação*, a classificação atribui rótulos de sensibilidade aos ativos de informação da organização, ditando os níveis de proteção lógica e física a serem aplicados de forma proporcional ao dano decorrente de divulgação ou modificação indevida.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "R$ 50.000". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "R$ 80.000". De acordo com a teoria estudada em *3.2 Análise Qualitativa vs. Análise Quantitativa (SLE, ARO e ALE)*, onde $\text{ACS}$ ( Annualized Cost of Safeguard ) é o custo anual de manutenção do controle. Se o saldo for positivo, o controle de segurança é economicamente viável.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "R$ 130.000". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, aceitar / Reter ( Risk Acceptance / Retention ): Manter o risco no nível atual sem novos controles, mediante aprovação formal fundamentada da alta administração, quando o custo da salvaguarda técnica for superior à perda monetária potencial estimada.
>
> **Gabarito: A**

---


### Teste 024
**(FGV – TRT da 24º Região – 2025 – Analista Judiciário - Área Administrativa - Contabilidade)**
Em 31/12/2024, uma sociedade empresária do setor de venda de alimentos apresentou os seguintes saldos em sua demonstração do resultado:  Receita de vendas: R$ 500.000;  Custo das mercadorias vendidas: R$ 300.000;  Receita com a venda de ativo imobilizado: R$ 45.000;  Baixa do ativo imobilizado: R$ 40.000;  Receita com equivalência patrimonial: R$ 35.000;  Receita de aluguel de imóveis a terceiros: R$ 12.000. Com base nas informações, assinale a opção que indica o saldo apresentado em “Valor adicionado recebido em transferência” na Demonstração do Valor Adicionado da sociedade empresária, em 31/12/2024.

* **A)** R$ 12.000.
* **B)** R$ 35.000.
* **C)** R$ 47.000.
* **D)** R$ 52.000.
* **E)** R$ 92.000.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "R$ 12.000". De acordo com a teoria estudada em *3.2 Análise Qualitativa vs. Análise Quantitativa (SLE, ARO e ALE)*, onde $\text{ACS}$ ( Annualized Cost of Safeguard ) é o custo anual de manutenção do controle. Se o saldo for positivo, o controle de segurança é economicamente viável.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "R$ 35.000". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, ultrassecreta: 25 anos — Presidente da República, Vice Presidente, Ministros de Estado, Comandantes das Forças Armadas — Prorrogável uma única vez, por igual período (totalizando até 50 anos), exclusivamente pela CMRI ( Comissão Mista de Reavaliação de Informações ).
> - **C)** **Correta.** Conforme fundamentado na seção *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)* deste guia, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT da 24º Região/2025) ao estabelecer que "R$ 47.000".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "R$ 52.000". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, decore rigorosamente os prazos decrescentes: 25 anos $\rightarrow$ 15 anos $\rightarrow$ 5 anos. A FCC inventa prazos alternativos inexistentes (como 10 ou 20 anos) ou inverte Secreta e Reservada. Além disso, lembre se: informações relativas à intimidade, vida privada, honra e imagem das pessoas têm restrição de acesso máxima de até 100 anos a contar da data de sua produção (Art. 31 da LAI), não se confundindo com prazos de segurança de Estado!.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "R$ 92.000". De acordo com a teoria estudada em *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade*, (O que tem valor econômico ou funcional.
>
> **Gabarito: C**

---


### Teste 025
**(FGV – TRT da 24º Região – 2025 – Analista Judiciário - Área Administrativa - Sem Especialidade)**
A Administração Pública, guiada por princípios constitucionais, busca uma gestão ética, transparente e eficaz, voltada ao interesse da sociedade. Assinale a opção que apresenta corretamente o princípio que é requisito de eficácia dos atos administrativos.

* **A)** Eficiência.
* **B)** Legalidade.
* **C)** Moralidade.
* **D)** Publicidade.
* **E)** Impessoalidade.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Eficiência". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, governo Digital Programa de Privacidade e Segurança da Informação (PPSI 2.0) Diretrizes, requisitos de maturidade e gestão de riscos cibernéticos para a administração pública.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Legalidade". De acordo com a teoria estudada em *1. Princípios Básicos da Segurança da Informação (CIDAN)*, a segurança da informação é definida pela norma ABNT NBR ISO/IEC 27000 como a preservação da confidencialidade, integridade e disponibilidade da informação, admitindo se adicionalmente propriedades vitais para transações formais como a autenticidade e o não repúdio. O mnemônico padronizado em concursos da FCC é CIDAN.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Moralidade". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, mitigar / Reduzir ( Risk Mitigation / Reduction ): Implementar controles de segurança (técnicos, administrativos ou físicos) para reduzir a probabilidade e/ou o impacto do risco até patamares aceitáveis (ex.: instalar firewalls, adotar MFA e criptografia).
> - **D)** **Correta.** Conforme fundamentado na seção *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)* deste guia, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT da 24º Região/2025) ao estabelecer que "Publicidade".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Impessoalidade". De acordo com a teoria estudada em *4.2 As Quatro Fases do Ciclo de Resposta a Incidentes (NIST SP 800-61)*, contenção: Ação emergencial prioritária voltada a estancar a disseminação do ataque e limitar o raio de destruição ( blast radius ), tal como isolar a máquina da rede, desconectar cabos ou bloquear portas de switches.
>
> **Gabarito: D**

---


### Teste 026
**(FGV – TRT da 24º Região – 2025 – Analista Judiciário - Área Administrativa - Sem Especialidade)**
O planejamento estratégico no setor público orienta a gestão por resultados, promovendo ações alinhadas a metas e indicadores que garantem maior eficiência, transparência e foco nas demandas da sociedade. Assinale a opção que apresenta corretamente uma característica do planejamento estratégico no setor público.

* **A)** O planejamento estratégico é voltado principalmente para a resolução imediata de problemas operacionais, com foco no curto prazo.
* **B)** O planejamento estratégico é um processo limitado a algumas áreas da organização, buscando melhorias isoladas e específicas.
* **C)** O planejamento estratégico ignora o ambiente externo, concentrando-se apenas nos recursos internos da organização.
* **D)** O planejamento estratégico é um processo centrado exclusivamente na alta administração, sem necessidade de envolvimento de outros atores.
* **E)** O planejamento estratégico é orientado para o futuro, envolvendo toda a organização, busca consenso entre os atores e promove o aprendizado organizacional.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O planejamento estratégico é voltado principalmente para a resolução imediata de problemas operacionais, com foco...". De acordo com a teoria estudada em *Fundamentos Teóricos*, banca Foco: FCC (Fundação Carlos Chagas).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O planejamento estratégico é um processo limitado a algumas áreas da organização, buscando melhorias isoladas e...". De acordo com a teoria estudada em *3. Gestão e Análise de Riscos de Segurança da Informação*, a gestão de riscos estabelece um processo contínuo e estruturado para identificar incertezas, avaliar a probabilidade de falhas e selecionar salvaguardas economicamente proporcionais.
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "O planejamento estratégico ignora o ambiente externo, concentrando se apenas nos recursos internos da organização". De acordo com a teoria estudada em *4.1 Métricas do CVSS v3.1 (Common Vulnerability Scoring System)*, scope (S): Escopo Inalterado ( Unchanged ) ou Alterado ( Changed , quando a falha compromete recursos fora de sua camada de autorização).
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "O planejamento estratégico é um processo centrado exclusivamente na alta administração, sem necessidade de...". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, aceitar / Reter ( Risk Acceptance / Retention ): Manter o risco no nível atual sem novos controles, mediante aprovação formal fundamentada da alta administração, quando o custo da salvaguarda técnica for superior à perda monetária potencial estimada.
> - **E)** **Correta.** Conforme fundamentado na seção *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL* deste guia, cláusula 6: Planejamento (Tratamento de riscos e objetivos de segurança). Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT da 24º Região/2025) ao estabelecer que "O planejamento estratégico é orientado para o futuro, envolvendo toda a organização, busca consenso entre os...".
>
> **Gabarito: E**

---


### Teste 027
**(FGV – TRT da 24º Região – 2025 – Analista Judiciário - Área Administrativa - Sem Especialidade)**
A Qualidade de Vida no Trabalho (QVT) no setor público visa promover um ambiente organizacional saudável, equilibrado e motivador, que valorize o servidor, melhore o desempenho institucional e fortaleça o compromisso com o serviço à sociedade. Assinale a opção que apresenta corretamente um fator-chave da QVT no setor público, relacionado à satisfação de clientes internos e externos.

* **A)** Compensação: associada à inovação, variedade e ritmo de trabalho.
* **B)** Moral: envolve bonificações, benefícios sociais e participação nos lucros.
* **C)** Organização do trabalho: relaciona-se à saúde ocupacional e à educação preventiva.
* **D)** Participação: refere-se à criatividade, à expressão pessoal e aos programas de capacitação.
* **E)** Comunicação: está ligada ao apoio psicossocial, à orientação técnica e ao gerenciamento pelo exemplo.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Compensação: associada à inovação, variedade e ritmo de trabalho". De acordo com a teoria estudada em *5.2 A Nova ISO/IEC 27002 (Edição 2022: 4 Temas e 93 Controles)*, cONTROLES DE PESSOAS ( 8 controles) ──► Recrutamento, trabalho remoto,.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Moral: envolve bonificações, benefícios sociais e participação nos lucros". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, cláusula 7: Apoio (Recursos, capacitação, conscientização e comunicação).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Organização do trabalho: relaciona se à saúde ocupacional e à educação preventiva". De acordo com a teoria estudada em *2. Classificação e Rotulagem da Informação*, a classificação atribui rótulos de sensibilidade aos ativos de informação da organização, ditando os níveis de proteção lógica e física a serem aplicados de forma proporcional ao dano decorrente de divulgação ou modificação indevida.
> - **D)** **Correta.** Conforme fundamentado na seção *4.2 As Quatro Fases do Ciclo de Resposta a Incidentes (NIST SP 800-61)* deste guia, preparação ( Preparation ): Estabelecimento e capacitação da equipe técnica de resposta (CSIRT / CERT), aquisição de ferramentas de investigação forense, implantação de políticas e planos de comunicação. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT da 24º Região/2025) ao estabelecer que "Participação: refere se à criatividade, à expressão pessoal e aos programas de capacitação".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Comunicação: está ligada ao apoio psicossocial, à orientação técnica e ao gerenciamento pelo exemplo". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, aceitar / Reter ( Risk Acceptance / Retention ): Manter o risco no nível atual sem novos controles, mediante aprovação formal fundamentada da alta administração, quando o custo da salvaguarda técnica for superior à perda monetária potencial estimada.
>
> **Gabarito: D**

---


### Teste 028
**(FGV – TRT da 24º Região – 2025 – Analista Judiciário - Área Administrativa - Sem Especialidade)**
A gestão eficiente das receitas públicas é essencial para garantir recursos que impulsionam investimentos estratégicos e a implementação de políticas sociais. Assinale a opção que apresenta corretamente as origens das receitas públicas.

* **A)** Derivam unicamente do patrimônio estatal e do patrimônio do particular.
* **B)** Originam-se exclusivamente do patrimônio do particular e dos ingressos temporários.
* **C)** Têm origem somente nas transferências intergovernamentais e nos ingressos temporários.
* **D)** São provenientes apenas do patrimônio estatal e das transferências intergovernamentais.
* **E)** São oriundas do patrimônio estatal; do patrimônio do particular; das transferências intergovernamentais; e dos ingressos temporários.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "Derivam unicamente do patrimônio estatal e do patrimônio do particular". De acordo com a teoria estudada em *3.2 Análise Qualitativa vs. Análise Quantitativa (SLE, ARO e ALE)*, mensura as perdas e investimentos em valores monetários concretos (R$).
> - **B)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "Originam se exclusivamente do patrimônio do particular e dos ingressos temporários". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, garantia de que o acesso à informação é restrito estrita e exclusivamente a pessoas, entidades ou processos formalmente autorizados.
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "Têm origem somente nas transferências intergovernamentais e nos ingressos temporários". De acordo com a teoria estudada em *4.1 Métricas do CVSS v3.1 (Common Vulnerability Scoring System)*, scope (S): Escopo Inalterado ( Unchanged ) ou Alterado ( Changed , quando a falha compromete recursos fora de sua camada de autorização).
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "São provenientes apenas do patrimônio estatal e das transferências intergovernamentais". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, cláusula 7: Apoio (Recursos, capacitação, conscientização e comunicação).
> - **E)** **Correta.** Conforme fundamentado na seção *5.2 A Nova ISO/IEC 27002 (Edição 2022: 4 Temas e 93 Controles)* deste guia, cONTROLES ORGANIZACIONAIS (37 controles) ──► Políticas, gestão de ativos,. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT da 24º Região/2025) ao estabelecer que "São oriundas do patrimônio estatal; do patrimônio do particular; das transferências intergovernamentais; e dos...".
>
> **Gabarito: E**

---


### Teste 029
**(FGV – TRT da 24º Região – 2025 – Analista Judiciário - Área Administrativa - Sem Especialidade)**
Programas de integridade e mecanismos de prevenção à corrupção são fundamentais para promover a ética, a transparência e a accountability na Administração Pública, fortalecendo a confiança da sociedade nas instituições e garantindo a correta aplicação dos recursos públicos. Assinale a opção que apresenta corretamente o conceito de accountability.

* **A)** Diz respeito à obrigação de pessoas ou entidades que recebem recursos públicos de prestar contas e assumir responsabilidades fiscais, gerenciais e programáticas.
* **B)** É o dever exclusivo dos cidadãos de fiscalizar os atos da Administração Pública.
* **C)** Refere-se à obrigação do Estado de manter o sigilo sobre todas as informações estratégicas.
* **D)** Trata-se da exigência de cumprimento de metas financeiras impostas apenas as empresas privadas.
* **E)** Refere-se à transparência apenas nos processos eleitorais, sem relação com a gestão pública.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade* deste guia, garantia de que o acesso à informação é restrito estrita e exclusivamente a pessoas, entidades ou processos formalmente autorizados. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT da 24º Região/2025) ao estabelecer que "Diz respeito à obrigação de pessoas ou entidades que recebem recursos públicos de prestar contas e assumir...".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "É o dever exclusivo dos cidadãos de fiscalizar os atos da Administração Pública". De acordo com a teoria estudada em *2.2 Classificação Corporativa Geral de Ativos*, pública: Informação destinada à divulgação irrestrita (editais de licitação, acórdãos públicos, portal da transparência); o vazamento gera dano nulo.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Refere se à obrigação do Estado de manter o sigilo sobre todas as informações estratégicas". De acordo com a teoria estudada em *2.2 Classificação Corporativa Geral de Ativos*, confidencial: Informações estratégicas, relatórios preliminares de auditoria em instrução ou dados cadastrais sob sigilo fiscal; vazamento gera dano financeiro ou institucional grave.
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "Trata se da exigência de cumprimento de metas financeiras impostas apenas as empresas privadas". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Escuta clandestina de rede ( sniffing/eavesdropping ), roubo de dispositivos físicos, engenharia social, vazamento inadvertido de dados fiscais protegidos por sigilo e acessos não autorizados.
> - **E)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "Refere se à transparência apenas nos processos eleitorais, sem relação com a gestão pública". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, nIST SP 800 30 Rev. 1 Guide for Conducting Risk Assessments Guia metodológico oficial para condução de processos de avaliação e gestão de riscos em segurança da informação.
>
> **Gabarito: A**

---


### Teste 030
**(FGV – TRT da 24º Região – 2025 – Analista Judiciário - Área Administrativa - Sem Especialidade)**
Uma entidade do setor público incorreu em despesas com a aquisição de passagens aéreas e pagamento de taxas de embarque para funcionários que mudaram o seu domicílio por conta de demandas internas da administração da entidade. Ao verificar o grupo de natureza da despesa orçamentária, é correto classificar esses gastos como

* **A)** investimentos.
* **B)** inversões financeiras.
* **C)** amortização da dívida.
* **D)** pessoal e encargos sociais.
* **E)** outras despesas correntes.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *3.2 Análise Qualitativa vs. Análise Quantitativa (SLE, ARO e ALE)* deste guia, mensura as perdas e investimentos em valores monetários concretos (R$). Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT da 24º Região/2025) ao estabelecer que "investimentos".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "inversões financeiras". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, grau de Sigilo: Prazo Máximo de Restrição — Competência Originária Típica para Classificar — Regime de Prorrogação.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "amortização da dívida". De acordo com a teoria estudada em *4.2 As Quatro Fases do Ciclo de Resposta a Incidentes (NIST SP 800-61)*, preparação ( Preparation ): Estabelecimento e capacitação da equipe técnica de resposta (CSIRT / CERT), aquisição de ferramentas de investigação forense, implantação de políticas e planos de comunicação.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "pessoal e encargos sociais". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, cláusula 9: Avaliação de Desempenho (Auditorias internas e análise pela direção).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "outras despesas correntes". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, aceitar / Reter ( Risk Acceptance / Retention ): Manter o risco no nível atual sem novos controles, mediante aprovação formal fundamentada da alta administração, quando o custo da salvaguarda técnica for superior à perda monetária potencial estimada.
>
> **Gabarito: A**

---


### Teste 031
**(FGV – TRT 16ª – 2022 – Analista Judiciário (Área Administrativa - Tecnologia da Informação))**
Christo e Jeanne-Claude foi um casal de artistas plásticos que se notabilizou por um trabalho muito próximo à arquitetura e com forte componente social, que aparecia na execução de seus projetos, que sempre envolviam a comunidade onde as obras eram instaladas. Alguns aspectos presentes em sua obra, evidenciados nas fotos, são apresentados nas opções a seguir, à exceção de um. Assinale-o.

* **A)** A escala de suas obras.
* **B)** A intervenção em ambientes naturais.
* **C)** A repetição de elementos.
* **D)** O caráter arquitetônico de sua linguagem.
* **E)** O fazer performático.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A escala de suas obras". De acordo com a teoria estudada em *4.1 Métricas do CVSS v3.1 (Common Vulnerability Scoring System)*, o padrão CVSS (mantido pelo FIRST) quantifica a gravidade técnica de vulnerabilidades de software e hardware em uma escala contínua de 0,0 a 10,0.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A intervenção em ambientes naturais". De acordo com a teoria estudada em *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade*, ameaça ( Threat ): Evento ou agente com potencial de causar dano (hackers, desastres naturais, erros acidentais de operadores).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A repetição de elementos". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, garantia de que a informação, os sistemas computacionais e os ativos de telecomunicações associados estejam acessíveis e utilizáveis sob demanda pelos usuários autorizados sempre que necessário.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O caráter arquitetônico de sua linguagem". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes.
> - **E)** **Correta.** Conforme fundamentado na seção *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade* deste guia, ameaças clássicas: Escuta clandestina de rede ( sniffing/eavesdropping ), roubo de dispositivos físicos, engenharia social, vazamento inadvertido de dados fiscais protegidos por sigilo e acessos não autorizados. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT 16ª/2022) ao estabelecer que "O fazer performático".
>
> **Gabarito: E**

---


### Teste 032
**(FGV – TRT 16ª – 2022 – Analista Judiciário (Área Administrativa - Tecnologia da Informação))**
O ESG surgiu no mercado financeiro como uma forma de medir o impacto que as ações de sustentabilidade geram nos resultados das empresas. A sigla surgiu a primeira vez em 2004, dentro de um grupo de trabalho do Principles for Responsible Investment (PRI), rede ligada à ONU que tem como objetivo atrair investimentos sustentáveis. James Gifford, economista que liderava o PRI, resumiu assim o significado de ESG: “O ESG é apenas um subgrupo inserido no contexto maior do investimento sustentável. O termo foi criado, especificamente, para focar em questões materiais. A ideia foi inverter a lógica do que, na época, era chamado de investimento ético, para se concentrar em fatores relevantes para os investidores. Se você tem uma responsabilidade fiduciária, como no caso de um fundo de pensão, não deveria estar pensando num horizonte de nove meses, mas sim de nove anos, ou de 20 anos. E quando se considera esse horizonte, temas como mudanças climáticas, riscos sociopolíticos etc., se tornam relevantes. Algumas pessoas usam o termo de maneira mais ampla, mas o ponto central é a incorporação de fatores socioambientais nos investimentos para gerenciar riscos. Não é mais sobre ética.” (https://exame.com/esg/) A sigla em inglês ESG significa

* **A)** meio ambiente, social e governança.
* **B)** economia, social e gestão.
* **C)** energia, sustentabilidade e gestão.
* **D)** ética, natureza e economia.
* **E)** eficiência, sustentação e ação global.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade* deste guia, ameaças clássicas: Escuta clandestina de rede ( sniffing/eavesdropping ), roubo de dispositivos físicos, engenharia social, vazamento inadvertido de dados fiscais protegidos por sigilo e acessos não autorizados. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT 16ª/2022) ao estabelecer que "meio ambiente, social e governança".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "economia, social e gestão". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, decreto Federal nº 9.637/2018 (Política Nacional de Segurança da Informação) Institui a PNSI, dispondo sobre governança, gestão de riscos e tratamento de incidentes de segurança da informação.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "energia, sustentabilidade e gestão". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Ataques de negação de serviço (DoS e DDoS), falhas físicas de hardware em servidores e storages, interrupção no fornecimento de energia elétrica, panes nos links de internet e desastres ambientais (enchentes, incêndios em datacenters).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "ética, natureza e economia". De acordo com a teoria estudada em *5.2 A Nova ISO/IEC 27002 (Edição 2022: 4 Temas e 93 Controles)*, cONTROLES DE PESSOAS ( 8 controles) ──► Recrutamento, trabalho remoto,.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "eficiência, sustentação e ação global". De acordo com a teoria estudada em *4.2 As Quatro Fases do Ciclo de Resposta a Incidentes (NIST SP 800-61)*, contenção: Ação emergencial prioritária voltada a estancar a disseminação do ataque e limitar o raio de destruição ( blast radius ), tal como isolar a máquina da rede, desconectar cabos ou bloquear portas de switches.
>
> **Gabarito: A**

---


### Teste 033
**(FGV – TRT 16ª – 2022 – Analista Judiciário (Área Administrativa - Tecnologia da Informação))**
Observe a declaração abaixo no contexto de páginas Web. <div class="jumbotron"> <h1>Teste</h1> <p>Frase inicial...</p> </div> Assinale o framework usualmente associado à classe utilizada.

* **A)** Angular Material.
* **B)** Bootstrap.
* **C)** CSS.
* **D)** JSON.
* **E)** SpringBoot.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Angular Material". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, nIST Cybersecurity Framework (CSF 2.0) Estrutura de referência global do NIST para identificação, proteção, detecção, resposta e recuperação de riscos cibernéticos.
> - **B)** **Correta.** Conforme fundamentado na seção *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL* deste guia, cláusula 4: Contexto da Organização (partes interessadas e escopo do SGSI). Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT 16ª/2022) ao estabelecer que "Bootstrap".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "CSS". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, nIST SP 800 37 Rev. 2 Risk Management Framework Diretrizes para aplicação do Risk Management Framework (RMF) aos sistemas e organizações.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "JSON". De acordo com a teoria estudada em *5.3 A Declaração de Aplicabilidade (SoA) e a ISO/IEC 27005*, declaração de Aplicabilidade (SoA Statement of Applicability ).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "SpringBoot". De acordo com a teoria estudada em *5.3 A Declaração de Aplicabilidade (SoA) e a ISO/IEC 27005*, documento formal obrigatório exigido pela ISO/IEC 27001 no qual a organização lista todos os controles de segurança do Anexo A, declarando.
>
> **Gabarito: B**

---


### Teste 034
**(FGV – TRT 1ª – 2024 – Analista Judiciário - Área Administrativa)**
Uma lei impôs aos estabelecimentos federais de ensino a utilização de cadeiras adaptadas para alunos com deficiência física ou mobilidade reduzida. Nela foi determinado que o número de cadeiras adaptadas deve ser, no mínimo, igual ao número de alunos regularmente matriculados em cada sala. Deixou a lei de tratar sobre pessoas com deficiência auditiva e visual. Com relação ao tema do enunciado, à Lei nº 10.098/2000, que trata sobre normas gerais e critérios básicos para a promoção da acessibilidade das pessoas com deficiência ou com mobilidade reduzida, e ao pensamento do Supremo Tribunal Federal (STF), é correto afirmar que:

* **A)** a Lei nº 10.098/2000 não tratou dos locais de aula para pessoas que utilizam cadeiras de roda, deixando um vácuo suplementado pela aludida lei, que optou pelo uso de cadeiras adaptadas;
* **B)** a lei federal, em respeito ao princípio da proporcionalidade, deveria estabelecer que o número de cadeiras adaptadas seria o número de alunos com deficiência regularmente matriculados em cada sala;
* **C)** a Lei nº 10.098/2000 dispôs sobre lugares específicos para pessoas com deficiência auditiva e visual, mas não sobre a presença do respectivo acompanhante, o que obedece à ideia de autonomia;
* **D)** o respeito à imposição legal não seria um problema orçamentário, pois o aludido critério do número de alunos regularmente matriculados obedece à lógica da integração social;
* **E)** a referida imposição aos estabelecimentos federais de ensino viola a não discriminação, porque as pessoas com deficiência receberiam tratamento diferenciado em decorrência dessa condição.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "a Lei nº 10.098/2000 não tratou dos locais de aula para pessoas que utilizam cadeiras de roda, deixando um vácuo...". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, decore rigorosamente os prazos decrescentes: 25 anos $\rightarrow$ 15 anos $\rightarrow$ 5 anos. A FCC inventa prazos alternativos inexistentes (como 10 ou 20 anos) ou inverte Secreta e Reservada. Além disso, lembre se: informações relativas à intimidade, vida privada, honra e imagem das pessoas têm restrição de acesso máxima de até 100 anos a contar da data de sua produção (Art. 31 da LAI), não se confundindo com prazos de segurança de Estado!.
> - **B)** **Correta.** Conforme fundamentado na seção *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade* deste guia, vulnerabilidade ( Vulnerability ): Ponto fraco, falha de projeto, brecha de configuração ou deficiência de controle em um ativo que pode ser explorado por uma ameaça. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT 1ª/2024) ao estabelecer que "a lei federal, em respeito ao princípio da proporcionalidade, deveria estabelecer que o número de cadeiras...".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "a Lei nº 10.098/2000 dispôs sobre lugares específicos para pessoas com deficiência auditiva e visual, mas não...". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, garantia de que o acesso à informação é restrito estrita e exclusivamente a pessoas, entidades ou processos formalmente autorizados.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "o respeito à imposição legal não seria um problema orçamentário, pois o aludido critério do número de alunos...". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, secreta: 15 anos — Titulares de autarquias, fundações e órgãos públicos sob mesma alçada legal — Não admite prorrogação. O prazo cessa impreterivelmente aos 15 anos.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "a referida imposição aos estabelecimentos federais de ensino viola a não discriminação, porque as pessoas com...". De acordo com a teoria estudada em *5.2 A Nova ISO/IEC 27002 (Edição 2022: 4 Temas e 93 Controles)*, cONTROLES DE PESSOAS ( 8 controles) ──► Recrutamento, trabalho remoto,.
>
> **Gabarito: B**

---


### Teste 035
**(FGV – TRT 1ª – 2024 – Analista Judiciário - Área Administrativa)**
Um servidor foi designado para analisar as informações a serem apresentadas no Demonstrativo da Execução das Despesas por Função e Subfunção. Ao analisar despesas da Câmara dos Deputados, o servidor verificou que a Ação nº 2010 – Assistência Pré-escolar aos Dependentes dos Servidores do Órgão foi incluída na subfunção 365 – Educação Infantil. Quanto à função, o referido gasto deve constar como:

* **A)** Educação;
* **B)** Legislativa;
* **C)** Administração;
* **D)** Assistência Social;
* **E)** Encargos Especiais.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Educação". De acordo com a teoria estudada em *2. Classificação e Rotulagem da Informação*, a classificação atribui rótulos de sensibilidade aos ativos de informação da organização, ditando os níveis de proteção lógica e física a serem aplicados de forma proporcional ao dano decorrente de divulgação ou modificação indevida.
> - **B)** **Correta.** Conforme fundamentado na seção *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade* deste guia, ameaças clássicas: Ataques de negação de serviço (DoS e DDoS), falhas físicas de hardware em servidores e storages, interrupção no fornecimento de energia elétrica, panes nos links de internet e desastres ambientais (enchentes, incêndios em datacenters). Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT 1ª/2024) ao estabelecer que "Legislativa".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Administração". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, aceitar / Reter ( Risk Acceptance / Retention ): Manter o risco no nível atual sem novos controles, mediante aprovação formal fundamentada da alta administração, quando o custo da salvaguarda técnica for superior à perda monetária potencial estimada.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Assistência Social". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Escuta clandestina de rede ( sniffing/eavesdropping ), roubo de dispositivos físicos, engenharia social, vazamento inadvertido de dados fiscais protegidos por sigilo e acessos não autorizados.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Encargos Especiais". De acordo com a teoria estudada em *4.2 As Quatro Fases do Ciclo de Resposta a Incidentes (NIST SP 800-61)*, contenção: Ação emergencial prioritária voltada a estancar a disseminação do ataque e limitar o raio de destruição ( blast radius ), tal como isolar a máquina da rede, desconectar cabos ou bloquear portas de switches.
>
> **Gabarito: B**

---


### Teste 036
**(FGV – TRF/1 – 2024 – Analista Judiciario Area Apoio Especializado Especialidade Suporte Em Tecnologia Da Informacao)**
Acerca das normas atinentes ao sigilo das informações, da comunicação, da publicidade dos atos e das informações, bem como da imprensa oficial, nos termos em que dispõe o Código de Conduta dos servidores da Justiça Federal – Resolução nº 147/2011, do Conselho da Justiça Federal, é correto afirmar que:

* **A)** os servidores e gestores do Conselho e da Justiça Federal são proibidos de receber presentes, incluindo os brindes atribuídos por entidades a título de cortesia, por ocasião de eventos especiais ou datas comemorativas;
* **B)** o servidor ou gestor do Conselho e da Justiça Federal que, por força de seu cargo ou de suas responsabilidades, tiverem acesso a informações do órgão em que atuam ainda não divulgadas não são obrigados a manter sigilo quanto ao seu conteúdo;
* **C)** a comunicação entre os destinatários do Código ou entre esses e os órgãos governamentais, os clientes, os fornecedores e a sociedade deve ser indiscutivelmente clara, simples, objetiva e acessível a todos os legitimamente interessados;
* **D)** os contatos com os órgãos de imprensa serão promovidos por quaisquer servidores e gestores do Conselho e da Justiça Federal, tribunais regionais federais e seções judiciárias;
* **E)** é vedado aos servidores e gestores do Conselho e da Justiça Federal garantir a publicidade de seus atos e a disponibilidade de informações corretas e atualizadas que permitam o conhecimento dos aspectos relevantes da atividade sob sua responsabilidade.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "os servidores e gestores do Conselho e da Justiça Federal são proibidos de receber presentes, incluindo os brindes...". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, secreta: 15 anos — Titulares de autarquias, fundações e órgãos públicos sob mesma alçada legal — Não admite prorrogação. O prazo cessa impreterivelmente aos 15 anos.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "o servidor ou gestor do Conselho e da Justiça Federal que, por força de seu cargo ou de suas responsabilidades...". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, ultrassecreta: 25 anos — Presidente da República, Vice Presidente, Ministros de Estado, Comandantes das Forças Armadas — Prorrogável uma única vez, por igual período (totalizando até 50 anos), exclusivamente pela CMRI ( Comissão Mista de Reavaliação de Informações ).
> - **C)** **Correta.** Conforme fundamentado na seção *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)* deste guia, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRF/1/2024) ao estabelecer que "a comunicação entre os destinatários do Código ou entre esses e os órgãos governamentais, os clientes, os...".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "os contatos com os órgãos de imprensa serão promovidos por quaisquer servidores e gestores do Conselho e da...". De acordo com a teoria estudada em *5.2 A Nova ISO/IEC 27002 (Edição 2022: 4 Temas e 93 Controles)*, a norma ISO/IEC 27002 constitui um Código de Práticas que detalha diretrizes para implementação dos controles de segurança do Anexo A da ISO 27001. Não é passível de certificação independente.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "é vedado aos servidores e gestores do Conselho e da Justiça Federal garantir a publicidade de seus atos e a...". De acordo com a teoria estudada em *2.2 Classificação Corporativa Geral de Ativos*, confidencial: Informações estratégicas, relatórios preliminares de auditoria em instrução ou dados cadastrais sob sigilo fiscal; vazamento gera dano financeiro ou institucional grave.
>
> **Gabarito: C**

---


### Teste 037
**(FGV – TRF/1 – 2024 – Analista Judiciario Area Apoio Especializado Especialidade Suporte Em Tecnologia Da Informacao)**
A equipe de tecnologia da informação (TI) de um órgão está enfrentando dificuldades de disponibilidade de seu site de Internet após a divulgação de novos serviços com prazos rígidos para seus clientes. O site de Internet não está suportando o volume de acessos simultâneos. Para incrementar a disponibilidade do site, a equipe de TI replicou os servidores web e contratou uma solução que instalou um equipamento na frente das várias réplicas do site. Esse equipamento recebe as solicitações dos usuários da Internet, direcionando-as para os diversos servidores web internos, balanceando a carga entre eles. O certificado digital foi instalado nele para reduzir o processamento dos servidores web interno. O equipamento da solução contratada é um Proxy:

* **A)** de encaminhamento;
* **B)** transparente;
* **C)** anônimo;
* **D)** reverso;
* **E)** de distorção.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "de encaminhamento". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, propriedade de salvaguardar a exatidão, originalidade e completude da informação e de seus métodos de processamento, impedindo alterações, corrupções ou supressões indevidas ou não autorizadas.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "transparente". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, garantia de que a informação, os sistemas computacionais e os ativos de telecomunicações associados estejam acessíveis e utilizáveis sob demanda pelos usuários autorizados sempre que necessário.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "anônimo". De acordo com a teoria estudada em *2.2 Classificação Corporativa Geral de Ativos*, interna: Informação para circulação interna restrita aos servidores e colaboradores; divulgação indevida acarreta transtorno administrativo leve.
> - **D)** **Correta.** Conforme fundamentado na seção *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade* deste guia, ameaças clássicas: Ataques de negação de serviço (DoS e DDoS), falhas físicas de hardware em servidores e storages, interrupção no fornecimento de energia elétrica, panes nos links de internet e desastres ambientais (enchentes, incêndios em datacenters). Dessa forma, está plenamente correta a assertiva da banca (FGV – TRF/1/2024) ao estabelecer que "reverso".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "de distorção". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Escuta clandestina de rede ( sniffing/eavesdropping ), roubo de dispositivos físicos, engenharia social, vazamento inadvertido de dados fiscais protegidos por sigilo e acessos não autorizados.
>
> **Gabarito: D**

---


### Teste 038
**(FGV – TRF/1 – 2024 – Analista Judiciario Area Apoio Especializado Especialidade Tecnologia Da Informacao)**
Ao analisar uma conexão HTTP não persistente, constatou-se o acesso ao endereço http://www.highschool.edu/departamentos/home.index. Uma das etapas da transferência dessa página do servidor para o cliente está corretamente descrita na seguinte alternativa:

* **A)** cliente HTTP envia uma mensagem de download HTTP ao servidor por meio do socket do servidor. Essa mensagem inclui o nome de caminho /departamentos/home.index;
* **B)** processo servidor HTTP ordena ao TCP que encerre a conexão TCP. Mas, na realidade, o TCP só a encerrará quando tiver certeza de que o cliente recebeu a mensagem de resposta intacta;
* **C)** processo cliente HTTP inicia uma conexão TCP para o servidor www.highschool.edu na porta número 90, que é o número de porta default para o HTTP. Associados à conexão UDP, haverá um socket no cliente e um socket no servidor;
* **D)** cliente TCP recebe a mensagem de resposta e a conexão TCP é encerrada. A mensagem indica que o objeto encapsulado é um arquivo HTTP. O cliente extrai o arquivo da mensagem de resposta, analisa o arquivo HTML e encontra referências aos objetos JPEG;
* **E)** processo servidor HTML solicita a mensagem de requisição por meio de seu socket, extrai o objeto /departamentos/home.index de seu armazenamento (RAM ou disco), encapsula-o em uma mensagem de resposta HTML e a envia ao cliente HTTP.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "cliente HTTP envia uma mensagem de download HTTP ao servidor por meio do socket do servidor. Essa mensagem inclui...". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, nIST Cybersecurity Framework (CSF 2.0) Estrutura de referência global do NIST para identificação, proteção, detecção, resposta e recuperação de riscos cibernéticos.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "processo servidor HTTP ordena ao TCP que encerre a conexão TCP. Mas, na realidade, o TCP só a encerrará quando...". De acordo com a teoria estudada em *3. Gestão e Análise de Riscos de Segurança da Informação*, a gestão de riscos estabelece um processo contínuo e estruturado para identificar incertezas, avaliar a probabilidade de falhas e selecionar salvaguardas economicamente proporcionais.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "processo cliente HTTP inicia uma conexão TCP para o servidor www.highschool.edu na porta número 90, que é o número...". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, garantia de que a informação, os sistemas computacionais e os ativos de telecomunicações associados estejam acessíveis e utilizáveis sob demanda pelos usuários autorizados sempre que necessário.
> - **D)** **Correta.** Conforme fundamentado na seção *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade* deste guia, mecanismos técnicos: Funções criptográficas de espalhamento ( hashing criptográfico como SHA 256 e SHA 512), códigos de autenticação de mensagem (HMAC), assinaturas digitais, somas de verificação ( checksums ) e trilhas de auditoria imutáveis. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRF/1/2024) ao estabelecer que "cliente TCP recebe a mensagem de resposta e a conexão TCP é encerrada. A mensagem indica que o objeto encapsulado...".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "processo servidor HTML solicita a mensagem de requisição por meio de seu socket, extrai o objeto...". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, evitar / Eliminar ( Risk Avoidance ): Descontinuar a atividade, processo ou serviço gerador do risco (ex.: desligar e desativar em definitivo um sistema legado vulnerável sem suporte do fabricante).
>
> **Gabarito: D**

---


### Teste 039
**(FGV – TRF/1 – 2024 – Analista Judiciario Area Apoio Especializado Especialidade Tecnologia Da Informacao)**
Uma empresa está desenvolvendo um aplicativo para comunicação interna entre seus funcionários. Para estabelecer uma conexão, o cliente TCP envia um segmento de requisição de estabelecimento de conexão com as linhas: clientSocket = socket(AF_INET, SOCK_STREAM) clientSocket.connect((serverName,12000)) Nas linhas acima, "12000" refere-se ao(à):

* **A)** porta de origem;
* **B)** porta de destino;
* **C)** tempo limite para a conexão permanecer ativa;
* **D)** tempo limite (timeout) para a conexão ser estabelecida;
* **E)** número de conexões simultâneas permitidas pelo servidor.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade* deste guia, ex.: invasor, tempestade, malware) ex.: porta aberta, ausência de patch). Dessa forma, está plenamente correta a assertiva da banca (FGV – TRF/1/2024) ao estabelecer que "porta de origem".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "porta de destino". De acordo com a teoria estudada em *4.2 As Quatro Fases do Ciclo de Resposta a Incidentes (NIST SP 800-61)*, preparação ( Preparation ): Estabelecimento e capacitação da equipe técnica de resposta (CSIRT / CERT), aquisição de ferramentas de investigação forense, implantação de políticas e planos de comunicação.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "tempo limite para a conexão permanecer ativa". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, a norma ABNT NBR ISO/IEC 27001 estabelece os requisitos formais para estabelecer, implementar, manter e melhorar continuamente um Sistema de Gestão de Segurança da Informação (SGSI).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "tempo limite (timeout) para a conexão ser estabelecida". De acordo com a teoria estudada em *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade*, vulnerabilidade ( Vulnerability ): Ponto fraco, falha de projeto, brecha de configuração ou deficiência de controle em um ativo que pode ser explorado por uma ameaça.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "número de conexões simultâneas permitidas pelo servidor". De acordo com a teoria estudada em *2.2 Classificação Corporativa Geral de Ativos*, interna: Informação para circulação interna restrita aos servidores e colaboradores; divulgação indevida acarreta transtorno administrativo leve.
>
> **Gabarito: A**

---


### Teste 040
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


### Teste 041
**(FGV – TJ/RR – 2024 – Analista Judiciario Gestao E Governanca De Tecnologia Da Informacao)**
Mais do que uma simples abordagem operacional, a gestão de processos é uma ferramenta importante para líderes de variados níveis hierárquicos, fornecendo subsídios para a tomada de decisão e na implantação de melhorias impactantes em diversos setores das instituições e na geração de valor público. Nesse contexto, assinale a afirmativa correta acerca de gestão de processos.

* **A)** Cadeia de valor encontra-se em um nível intermediário na estratégia de uma organização.
* **B)** Uma tarefa é um conjunto de atividades e comportamentos executados por pessoas ou máquinas cujo objetivo é alcançar um ou mais resultados organizacionais.
* **C)** O Ciclo BPM possui etapas como: planejar, analisar, desenhar, implantar e monitorar os processos.
* **D)** Processos de suporte são associados às atividades-fim da organização ou diretamente envolvidos no atendimento às necessidades dos seus usuários finais.
* **E)** Um processo é uma agregação de tarefas necessárias para entregar uma parte específica e definível de um produto ou serviço.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Cadeia de valor encontra se em um nível intermediário na estratégia de uma organização". De acordo com a teoria estudada em *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade*, ativo ( Asset ): Qualquer recurso humano, físico, tecnológico ou de informação que possui valor intrínseco para o cumprimento da missão da instituição.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Uma tarefa é um conjunto de atividades e comportamentos executados por pessoas ou máquinas cujo objetivo é...". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, garantia de que o acesso à informação é restrito estrita e exclusivamente a pessoas, entidades ou processos formalmente autorizados.
> - **C)** **Correta.** Conforme fundamentado na seção *🌐 Fontes Oficiais e Referências Bibliográficas* deste guia, nIST SP 800 30 Rev. 1 Guide for Conducting Risk Assessments Guia metodológico oficial para condução de processos de avaliação e gestão de riscos em segurança da informação. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/RR/2024) ao estabelecer que "O Ciclo BPM possui etapas como: planejar, analisar, desenhar, implantar e monitorar os processos".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Processos de suporte são associados às atividades fim da organização ou diretamente envolvidos no atendimento às...". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, garantia de que a informação, os sistemas computacionais e os ativos de telecomunicações associados estejam acessíveis e utilizáveis sob demanda pelos usuários autorizados sempre que necessário.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Um processo é uma agregação de tarefas necessárias para entregar uma parte específica e definível de um produto ou...". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, evitar / Eliminar ( Risk Avoidance ): Descontinuar a atividade, processo ou serviço gerador do risco (ex.: desligar e desativar em definitivo um sistema legado vulnerável sem suporte do fabricante).
>
> **Gabarito: C**

---


### Teste 042
**(CEBRASPE – STF – 2008 – Analista Judiciario Suporte Em Tecnologia Da Informacao)**
Dado um conjunto de relacionamentos R binário entre os conjuntos de entidades A e B, é correto afirmar que, em um mapeamento de cardinalidade muitos para muitos, uma entidade A está associada a qualquer número de entidades em B e uma entidade em B está associada a um número qualquer de entidades em A.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Correta.** O item está **Certo**. Conforme fundamentado na seção *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, garantia de que o acesso à informação é restrito estrita e exclusivamente a pessoas, entidades ou processos formalmente autorizados. Dessa forma, está plenamente correta a assertiva da banca (CEBRASPE – STF/2008) ao afirmar que "Dado um conjunto de relacionamentos R binário entre os conjuntos de entidades A e B, é correto afirmar que...".
> - **E)** **Incorreta.** A assertiva não incorre em erro conceitual, guardando conformidade com a teoria estudada.
>
> **Gabarito: C**

---


### Teste 043
**(CEBRASPE – STJ – 2015 – Analista Judiciario Suporte Em Tecnologia Da Informacao)**
A garantia do mínimo existencial, que decorre da proteção constitucional à dignidade da pessoa humana, restringe a invocação da reserva do possível como óbice à concretização do acesso aos direitos sociais.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Correta.** O item está **Certo**. Conforme fundamentado na seção *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, garantia de que o acesso à informação é restrito estrita e exclusivamente a pessoas, entidades ou processos formalmente autorizados. Dessa forma, está plenamente correta a assertiva da banca (CEBRASPE – STJ/2015) ao afirmar que "A garantia do mínimo existencial, que decorre da proteção constitucional à dignidade da pessoa humana...".
> - **E)** **Incorreta.** A assertiva não incorre em erro conceitual, guardando conformidade com a teoria estudada.
>
> **Gabarito: C**

---


### Teste 044
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


### Teste 045
**(CEBRASPE – TJ/DFT – 2015 – Analista Judiciario Suporte Em Tecnologia Da Informacao)**
O objetivo do direito é a paz. A luta é o meio de 1 O Programa de Responsabilidade consegui-la. Enquanto o direito tiver de repelir o ataque Socioambiental Viver Direito do TJDFT foi instituído por meio causado pela injustiça — e isso durará enquanto o mundo da Portaria GPR n.º 1.313/2012. As bases do Programa Viver 4 estiver de pé —, ele não será poupado. Direito, seus objetivos e sua meta permanente são 4 A vida do direito é a luta: a luta de povos, de apresentados, respectivamente, nos artigos 1.º, 2.º e 3.º da governos, de classes, de indivíduos. Todo o direito do mundo referida portaria, os quais são transcritos abaixo: 7 foi assim conquistado. Todo ordenamento jurídico que se lhe Art. 1.º Reeditar o Programa de Responsabilidade 7 contrapôs teve de ser eliminado e todo direito, o direito de um Socioambiental do TJDFT Viver Direito, cuja base é a Agenda povo ou o de um indivíduo, teve de ser conquistado com luta. Socioambiental do TJDFT que, em permanente revisão,

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Correta.** O item está **Certo**. Conforme fundamentado na seção *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, decore rigorosamente os prazos decrescentes: 25 anos $\rightarrow$ 15 anos $\rightarrow$ 5 anos. A FCC inventa prazos alternativos inexistentes (como 10 ou 20 anos) ou inverte Secreta e Reservada. Além disso, lembre se: informações relativas à intimidade, vida privada, honra e imagem das pessoas têm restrição de acesso máxima de até 100 anos a contar da data de sua produção (Art. 31 da LAI), não se confundindo com prazos de segurança de Estado!. Dessa forma, está plenamente correta a assertiva da banca (CEBRASPE – TJ/DFT/2015) ao afirmar que "O objetivo do direito é a paz. A luta é o meio de 1 O Programa de Responsabilidade consegui la. Enquanto o...".
> - **E)** **Incorreta.** A assertiva não incorre em erro conceitual, guardando conformidade com a teoria estudada.
>
> **Gabarito: C**

---


### Teste 046
**(CEBRASPE – TJ/DFT – 2015 – Analista Judiciario Suporte Em Tecnologia Da Informacao)**
A espada sem a balança é a força bruta, a balança sem a espada 13 ambiente, por meio de ações sociais sustentáveis, a fim de é a fraqueza do direito. Ambas se completam e o verdadeiro torná-lo e mantê-lo ambientalmente correto, socialmente justo estado de direito só existe onde a força, com a qual a justiça e economicamente viável. 16 empunha a espada, é usada com a mesma destreza com que a 16 Art. 2.º O Programa de Responsabilidade justiça maneja a balança. Socioambiental Viver Direito objetiva indicar e programar O direito é um labor contínuo, não apenas dos ações bem como sensibilizar os públicos interno e externo 19 governantes, mas de todo o povo. Cada um que se encontra na 19 quanto ao exercício dos direitos sociais, à gestão adequada dos situação de precisar defender seu direito participa desse resíduos gerados pelo órgão, ao combate a todas as formas de trabalho, levando sua contribuição para a concretização da desperdício dos recursos naturais e à inclusão de critérios 22 ideia de direito sobre a Terra. 22 socioambientais nos investimentos, nas construções, nas Rudolf von Ihering. A luta pelo direito. Tradução de J. Cretella Jr. compras e nas contratações de serviços da instituição. e Agnes Cretella. 5.ª ed. revista da tradução. São Paulo: Art. 3.º Define-se como meta permanente do Viver Editora Revista dos Tribunais, 2008, p. 31 (com adaptações).

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Incorreta.** A proposição incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "A espada sem a balança é a força bruta, a balança sem a espada 13 ambiente, por meio de ações sociais...". De acordo com a teoria em *3.2 Análise Qualitativa vs. Análise Quantitativa (SLE, ARO e ALE)*, onde $\text{ACS}$ ( Annualized Cost of Safeguard ) é o custo anual de manutenção do controle. Se o saldo for positivo, o controle de segurança é economicamente viável.
> - **E)** **Correta.** O item está **Errado** (gabarito oficial: **E**), pois contraria a disciplina teórica aplicável.
>
> **Gabarito: E**

---


### Teste 047
**(CEBRASPE – TJ/DFT – 2015 – Analista Judiciario Suporte Em Tecnologia Da Informacao)**
A forma verbal “defende” (R.12) está flexionada na terceira 28 social, com base no desenvolvimento do ser humano e na pessoa do singular por concordar com seu sujeito, cujo preservação da vida. referente é “a justiça” (R.11).

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Correta.** O item está **Certo**. Conforme fundamentado na seção *1. Princípios Básicos da Segurança da Informação (CIDAN)*, a segurança da informação é definida pela norma ABNT NBR ISO/IEC 27000 como a preservação da confidencialidade, integridade e disponibilidade da informação, admitindo se adicionalmente propriedades vitais para transações formais como a autenticidade e o não repúdio. O mnemônico padronizado em concursos da FCC é CIDAN. Dessa forma, está plenamente correta a assertiva da banca (CEBRASPE – TJ/DFT/2015) ao afirmar que "A forma verbal “defende” (R.12) está flexionada na terceira 28 social, com base no desenvolvimento do ser...".
> - **E)** **Incorreta.** A assertiva não incorre em erro conceitual, guardando conformidade com a teoria estudada.
>
> **Gabarito: C**

---


### Teste 048
**(CEBRASPE – TJ/DFT – 2015 – Analista Judiciario Suporte Em Tecnologia Da Informacao)**
A correção gramatical e o sentido original do texto seriam 12 O termo “ambientalmente correto, socialmente justo e preservados caso a oração “que se lhe contrapôs” (R. 7 e 8) economicamente viável” (R. 14 e 15) exerce a função de fosse reescrita como que foi contraposto a ele. predicativo. Texto para os itens de 13 a 21

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Incorreta.** A proposição apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A correção gramatical e o sentido original do texto seriam 12 O termo “ambientalmente correto, socialmente...". De acordo com a teoria em *3.2 Análise Qualitativa vs. Análise Quantitativa (SLE, ARO e ALE)*, onde $\text{ACS}$ ( Annualized Cost of Safeguard ) é o custo anual de manutenção do controle. Se o saldo for positivo, o controle de segurança é economicamente viável.
> - **E)** **Correta.** O item está **Errado** (gabarito oficial: **E**), pois contraria a disciplina teórica aplicável.
>
> **Gabarito: E**

---


### Teste 049
**(CEBRASPE – TJ/DFT – 2015 – Analista Judiciario Suporte Em Tecnologia Da Informacao)**
A política de acesso à justiça deve mobilizar todos os segmentos sociais contra a violência que emerge no cotidiano, dentro e fora do Estado. Para além das múltiplas portas que o 49 sistema de justiça deve abrir, é necessária a adoção de espaços livres de coerção para a construção de uma justiça acessível, mas, sobretudo, realizada por todos. Glaúcia Falsarella Foley. Nova política de acesso à justiça é possível. In: Correio Braziliense, 22/12/2014 (com adaptações).

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Incorreta.** A proposição apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A política de acesso à justiça deve mobilizar todos os segmentos sociais contra a violência que emerge no...". De acordo com a teoria em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, mecanismos técnicos: Criptografia em trânsito (TLS) e em repouso (TDE), controle de acesso lógico baseado em papéis (RBAC), mascaramento dinâmico de dados e soluções de Prevenção contra Perda de Dados ( DLP Data Loss Prevention ).
> - **E)** **Correta.** O item está **Errado** (gabarito oficial: **E**), pois contraria a disciplina teórica aplicável.
>
> **Gabarito: E**

---


### Teste 050
**(FGV – TJ/BA – 2015 – Analista Judiciario Tecnologia Da Informacao)**
Em um ambiente Linux instalado em uma determinada empresa, as contas dos programadores que trabalham num dado projeto de desenvolvimento estão associadas ao mesmo grupo de usuários. Um deles cria um diretório que deverá ser visível aos demais membros do time de desenvolvimento. A ideia é que os colegas possam entrar no diretório, criar novos arquivos sob o diretório, bem como visualizar e modificar o conteúdo dos arquivos ali armazenados. Usuários externos à equipe de desenvolvimento não devem ter acesso ao diretório, nem aos seus descendentes. Supondo-se que o caminho para o diretório em questão seja /home/projeto e que a proteção de /home já esteja corretamente estabelecida, o comando que associa a proteção desejada ao diretório /home/projeto e aos seus descendentes é:

* **A)** chmod –R 0770 /home/projeto;
* **B)** chmod –R 0760 /home/projeto;
* **C)** chmod –R 0750 /home/projeto;
* **D)** chmod –R 0740 /home/projeto;
* **E)** chmod –R 0730 /home/projeto.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade* deste guia, vulnerabilidade ( Vulnerability ): Ponto fraco, falha de projeto, brecha de configuração ou deficiência de controle em um ativo que pode ser explorado por uma ameaça. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/BA/2015) ao estabelecer que "chmod –R 0770 /home/projeto".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "chmod –R 0760 /home/projeto". De acordo com a teoria estudada em *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade*, risco Residual: Risco que subsiste e permanece após o projeto e a entrada em operação dos controles de segurança mitigadores. Deve situar se estritamente abaixo do Apetite ao Risco fixado pela diretoria do tribunal.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "chmod –R 0750 /home/projeto". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, garantia de que a informação, os sistemas computacionais e os ativos de telecomunicações associados estejam acessíveis e utilizáveis sob demanda pelos usuários autorizados sempre que necessário.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "chmod –R 0740 /home/projeto". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, reservada: 5 anos — Autoridades que exerçam funções formais de direção, comando ou chefia — Não admite prorrogação. O prazo cessa impreterivelmente aos 5 anos.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "chmod –R 0730 /home/projeto". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, secreta: 15 anos — Titulares de autarquias, fundações e órgãos públicos sob mesma alçada legal — Não admite prorrogação. O prazo cessa impreterivelmente aos 15 anos.
>
> **Gabarito: A**

---


### Teste 051
**(FGV – TJ/MT – 2024 – Analista Judiciario Tecnologia Da Informacao)**
A ISO/IEC 27001 é uma norma internacional que estabelece diretrizes para um Sistema de Gestão da Segurança da Informação (SGSI). O principal objetivo da implementação de um SGSI, segundo a ISO/IEC 27001, é

* **A)** gerenciar exclusivamente os riscos financeiros da empresa.
* **B)** garantir que os dados estejam sempre disponíveis para todos os colaboradores.
* **C)** certificar que todos os processos da empresa sejam automatizados.
* **D)** proteger a confidencialidade, integridade e disponibilidade das informações.
* **E)** assegurar que apenas softwares certificados sejam utilizados na empresa.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "gerenciar exclusivamente os riscos financeiros da empresa". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, garantia de que o acesso à informação é restrito estrita e exclusivamente a pessoas, entidades ou processos formalmente autorizados.
> - **B)** **Incorreta.** A opção promove generalização excessiva que desconsidera as condições técnicas e normativas ao afirmar que "garantir que os dados estejam sempre disponíveis para todos os colaboradores". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, garantia de que a informação, os sistemas computacionais e os ativos de telecomunicações associados estejam acessíveis e utilizáveis sob demanda pelos usuários autorizados sempre que necessário.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "certificar que todos os processos da empresa sejam automatizados". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, a norma ABNT NBR ISO/IEC 27001 estabelece os requisitos formais para estabelecer, implementar, manter e melhorar continuamente um Sistema de Gestão de Segurança da Informação (SGSI).
> - **D)** **Correta.** Conforme fundamentado na seção *1. Princípios Básicos da Segurança da Informação (CIDAN)* deste guia, a segurança da informação é definida pela norma ABNT NBR ISO/IEC 27000 como a preservação da confidencialidade, integridade e disponibilidade da informação, admitindo se adicionalmente propriedades vitais para transações formais como a autenticidade e o não repúdio. O mnemônico padronizado em concursos da FCC é CIDAN. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/MT/2024) ao estabelecer que "proteger a confidencialidade, integridade e disponibilidade das informações".
> - **E)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "assegurar que apenas softwares certificados sejam utilizados na empresa". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, propriedade de salvaguardar a exatidão, originalidade e completude da informação e de seus métodos de processamento, impedindo alterações, corrupções ou supressões indevidas ou não autorizadas.
>
> **Gabarito: D**

---


### Teste 052
**(FCC – TRT 1ª – 2014 – Analista Judiciário - Tecnologia da Informação)**
Compete, privativamente à União, legislar sobre

* **A)** direito civil; direito do trabalho e direito agrário.
* **B)** produção e consumo; responsabilidade por dano ao meio ambiente e propaganda comercial.
* **C)** direito do trabalho; seguridade social e proteção à in- _________________________________________________________ fância e à juventude.
* **D)** direito civil; direito urbanístico e direito do trabalho.
* **E)** direito urbanístico; produção e consumo e segurida- de social. _________________________________________________________ Noções de Direito Administrativo

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *5.2 A Nova ISO/IEC 27002 (Edição 2022: 4 Temas e 93 Controles)* deste guia, cONTROLES DE PESSOAS ( 8 controles) ──► Recrutamento, trabalho remoto,. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 1ª/2014) ao estabelecer que "direito civil; direito do trabalho e direito agrário".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "produção e consumo; responsabilidade por dano ao meio ambiente e propaganda comercial". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, decore rigorosamente os prazos decrescentes: 25 anos $\rightarrow$ 15 anos $\rightarrow$ 5 anos. A FCC inventa prazos alternativos inexistentes (como 10 ou 20 anos) ou inverte Secreta e Reservada. Além disso, lembre se: informações relativas à intimidade, vida privada, honra e imagem das pessoas têm restrição de acesso máxima de até 100 anos a contar da data de sua produção (Art. 31 da LAI), não se confundindo com prazos de segurança de Estado!.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "direito do trabalho; seguridade social e proteção à in fância e à juventude". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Escuta clandestina de rede ( sniffing/eavesdropping ), roubo de dispositivos físicos, engenharia social, vazamento inadvertido de dados fiscais protegidos por sigilo e acessos não autorizados.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "direito civil; direito urbanístico e direito do trabalho". De acordo com a teoria estudada em *1. Princípios Básicos da Segurança da Informação (CIDAN)*, a segurança da informação é definida pela norma ABNT NBR ISO/IEC 27000 como a preservação da confidencialidade, integridade e disponibilidade da informação, admitindo se adicionalmente propriedades vitais para transações formais como a autenticidade e o não repúdio. O mnemônico padronizado em concursos da FCC é CIDAN.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "direito urbanístico; produção e consumo e segurida de social. Noções de Direito Administrativo". De acordo com a teoria estudada em *2.2 Classificação Corporativa Geral de Ativos*, interna: Informação para circulação interna restrita aos servidores e colaboradores; divulgação indevida acarreta transtorno administrativo leve.
>
> **Gabarito: A**

---


### Teste 053
**(CEBRASPE – TRT/10 – 2013 – Analista Judiciario Tecnologia Da Informacao)**
O certificado digital revogado deve constar da lista de certificados revogados, publicada na página de Internet da autoridade certificadora que o emitiu. (cid:129) Nesta prova, faça o que se pede, usando, caso deseje, o espaço para rascunho indicado no presente caderno. Em seguida, transcreva o texto para a FOLHA DE TEXTO DEFINITIVO DA PROVA DISCURSIVA, no local apropriado, pois não serão avaliados fragmentos de texto escritos em locais indevidos. (cid:129) Qualquer fragmento de texto que ultrapassar a extensão máxima de linhas disponibilizadas será desconsiderado. (cid:129) Na folha de texto definitivo, identifique-se apenas na primeira página, pois não será avaliado texto que tenha qualquer assinatura ou marca identificadora fora do local apropriado. (cid:129) Ao domínio do conteúdo serão atribuídos até 10,00 pontos, dos quais até 0,50 ponto será atribuído ao quesito apresentação e estrutura textual (legibilidade, respeito às margens e indicação de parágrafos). Essencial para a realização de qualquer atividade que requeira mudanças, o gerenciamento de projetos é uma área em constante expansão. Hoje, não há como planejar e executar um projeto sem referências bem definidas e internacionalmente aceitas. Um exemplo de documentação que atende a esses requisitos é o PMBOK, sigla em inglês para o Guia de Conhecimentos em Gerenciamento de Projetos, publicado pelo PMI (Project Management Institute).

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Correta.** O item está **Certo**. Conforme fundamentado na seção *🌐 Fontes Oficiais e Referências Bibliográficas*, governo Digital Programa de Privacidade e Segurança da Informação (PPSI 2.0) Diretrizes, requisitos de maturidade e gestão de riscos cibernéticos para a administração pública. Dessa forma, está plenamente correta a assertiva da banca (CEBRASPE – TRT/10/2013) ao afirmar que "O certificado digital revogado deve constar da lista de certificados revogados, publicada na página de...".
> - **E)** **Incorreta.** A assertiva não incorre em erro conceitual, guardando conformidade com a teoria estudada.
>
> **Gabarito: C**

---


### Teste 054
**(CEBRASPE – TRT/10 – 2013 – Analista Judiciario Tecnologia Da Informacao)**
Em “sua possibilidade de acesso” (R.10), o termo “sua” corresponde a da sociedade.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Incorreta.** A proposição apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Em “sua possibilidade de acesso” (R.10), o termo “sua” corresponde a da sociedade". De acordo com a teoria em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes.
> - **E)** **Correta.** O item está **Errado** (gabarito oficial: **E**), pois contraria a disciplina teórica aplicável.
>
> **Gabarito: E**

---


### Teste 055
**(CEBRASPE – TRT/10 – 2013 – Analista Judiciario Tecnologia Da Informacao)**
NASA e INPE, cada qual a seu modo e respeitadas as diferenças quanto à atuação de ambas, são exemplos de instituições identificadas com as necessidades e exigências do tempo atual, em que o conhecimento constitui a força motriz que impulsiona o desenvolvimento e serve de base para um sistema produtivo cada vez mais globalizado e tecnologicamente avançado. Primeiro vieram as ONGs. Depois, as unidades de polícia pacificadora. Agora é a hora de as agências de comunicação digital chegarem às favelas do Rio de Janeiro. E a primeira delas está funcionando a pleno vapor no Complexo da Maré. Fundada há dois anos, a agência emprega o conhecimento tecnológico e social dos jovens dos morros e ajuda na formação profissional deles. O Estado de S.Paulo, caderno Link, 7/1/2013, p. L6 (com adaptações). Tendo o fragmento de texto acima como referência inicial e considerando a amplitude do tema por ele focalizado, julgue os itens subsequentes.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Correta.** O item está **Certo**. Conforme fundamentado na seção *🌐 Fontes Oficiais e Referências Bibliográficas*, aSSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. ABNT NBR ISO/IEC 27001:2022: Tecnologia da informação — Técnicas de segurança — Sistemas de gestão da segurança da informação — Requisitos. Rio de Janeiro: ABNT, 2022. Dessa forma, está plenamente correta a assertiva da banca (CEBRASPE – TRT/10/2013) ao afirmar que "NASA e INPE, cada qual a seu modo e respeitadas as diferenças quanto à atuação de ambas, são exemplos de...".
> - **E)** **Incorreta.** A assertiva não incorre em erro conceitual, guardando conformidade com a teoria estudada.
>
> **Gabarito: C**

---


### Teste 056
**(FCC – TRT 11ª – 2017 – Analista Judiciário - Tecnologia da Informação)**
Alunos de um curso de Direito participaram de um evento organizado pelo Governo do Estado do Amazonas sobre os direitos das pessoas com deficiência. A primeira discussão tratou dos seguintes temas relacionados à Política Nacional para a Integração da Pessoa Portadora de Deficiência: I. O desenvolvimento de ação conjunta do Estado e da sociedade civil, de modo a assegurar a plena integração da pessoa portadora de deficiência no contexto socioeconômico e cultural. II. A adoção de estratégias de articulação com órgãos e entidades públicos e privados, bem assim com organismos inter- nacionais e estrangeiros para a implantação da Política Nacional para a Integração da Pessoa Portadora de Deficiência. III. O desenvolvimento de programas setoriais destinados ao atendimento das necessidades especiais da pessoa portadora de deficiência. IV. O fomento da tecnologia de bioengenharia voltada para a pessoa portadora de deficiência, bem como a facilitação da importação de equipamentos. V. A fiscalização do cumprimento da legislação pertinente à pessoa portadora de deficiência. Para a Política Nacional para a Integração da Pessoa Portadora de Deficiência e nos termos do Decreto no 3.298/1999, esses temas são conceituados, respectivamente, como:

* **A)** diretriz, princípio, instrumento, princípio e objetivo.
* **B)** objetivo, princípio, princípio, diretriz e diretriz.
* **C)** instrumento, princípio, diretriz, objetivo e instrumento.
* **D)** princípio, diretriz, objetivo, instrumento e instrumento.
* **E)** princípio, princípio, diretriz, instrumento e objetivo.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "diretriz, princípio, instrumento, princípio e objetivo". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, garantia de que o acesso à informação é restrito estrita e exclusivamente a pessoas, entidades ou processos formalmente autorizados.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "objetivo, princípio, princípio, diretriz e diretriz". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "instrumento, princípio, diretriz, objetivo e instrumento". De acordo com a teoria estudada em *4.2 As Quatro Fases do Ciclo de Resposta a Incidentes (NIST SP 800-61)*, contenção: Ação emergencial prioritária voltada a estancar a disseminação do ataque e limitar o raio de destruição ( blast radius ), tal como isolar a máquina da rede, desconectar cabos ou bloquear portas de switches.
> - **D)** **Correta.** Conforme fundamentado na seção *🌐 Fontes Oficiais e Referências Bibliográficas* deste guia, decreto Federal nº 9.637/2018 (Política Nacional de Segurança da Informação) Institui a PNSI, dispondo sobre governança, gestão de riscos e tratamento de incidentes de segurança da informação. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 11ª/2017) ao estabelecer que "princípio, diretriz, objetivo, instrumento e instrumento".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "princípio, princípio, diretriz, instrumento e objetivo". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, secreta: 15 anos — Titulares de autarquias, fundações e órgãos públicos sob mesma alçada legal — Não admite prorrogação. O prazo cessa impreterivelmente aos 15 anos.
>
> **Gabarito: D**

---


### Teste 057
**(FCC – TRT 11ª – 2017 – Analista Judiciário - Tecnologia da Informação)**
A Lei no 13.146/2015 instituiu a Lei Brasileira de Inclusão da Pessoa com Deficiência, também conhecida como o Estatuto da Pessoa com Deficiência. Entre os assuntos tratados por essa norma estão os entraves, obstáculos, atitudes ou comportamentos que limitem ou impeçam a participação social da pessoa, bem como o gozo, a fruição e o exercício de seus direitos à aces- sibilidade, à liberdade de movimento e de expressão, à comunicação, ao acesso à informação, à compreensão, à circulação com segurança, entre outros. Esses fatores são legal e tecnicamente denominados

* **A)** fatos de desagregação social.
* **B)** socioambientais de limitação.
* **C)** barreiras.
* **D)** limítrofes.
* **E)** impeditivos de fruição de direitos.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "fatos de desagregação social". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Escuta clandestina de rede ( sniffing/eavesdropping ), roubo de dispositivos físicos, engenharia social, vazamento inadvertido de dados fiscais protegidos por sigilo e acessos não autorizados.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "socioambientais de limitação". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes.
> - **C)** **Correta.** Conforme fundamentado na seção *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)* deste guia, secreta: 15 anos — Titulares de autarquias, fundações e órgãos públicos sob mesma alçada legal — Não admite prorrogação. O prazo cessa impreterivelmente aos 15 anos. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 11ª/2017) ao estabelecer que "barreiras".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "limítrofes". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, decore rigorosamente os prazos decrescentes: 25 anos $\rightarrow$ 15 anos $\rightarrow$ 5 anos. A FCC inventa prazos alternativos inexistentes (como 10 ou 20 anos) ou inverte Secreta e Reservada. Além disso, lembre se: informações relativas à intimidade, vida privada, honra e imagem das pessoas têm restrição de acesso máxima de até 100 anos a contar da data de sua produção (Art. 31 da LAI), não se confundindo com prazos de segurança de Estado!.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "impeditivos de fruição de direitos". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, aSSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. ABNT NBR ISO/IEC 27001:2022: Tecnologia da informação — Técnicas de segurança — Sistemas de gestão da segurança da informação — Requisitos. Rio de Janeiro: ABNT, 2022.
>
> **Gabarito: C**

---


### Teste 058
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


### Teste 059
**(FCC – TRT 13ª – 2014 – Analista Judiciário - Tecnologia da Informação)**
Considere as definições seguintes, cada qual em seu contexto específico, aplicáveis à gestão de negócios e de tecnologia da informação e comunicação. I. É embasado em quatro perspectivas (financeira, clientes, processos internos e aprendizado/crescimento), formando um conjunto coeso e interdependente, com seus objetivos e indicadores se inter-relacionando e formando um fluxo ou diagrama de causa e efeito que se inicia na perspectiva do aprendizado e crescimento e termina na perspectiva financeira. II. Seu objetivo é fornecer uma visão completa do ambiente atual de Tecnologia da Informação e Comunicação e ao mesmo tempo compará-lo a cenários alternativos que possam otimizar o retorno dos investimentos já feitos e dos ainda a serem realizados. Visa orientar a identificação das informações estratégicas, táticas e operacionais necessárias à instituição e também permitir a definição de projetos e prioridades, bem como o acompanhamento das ações e o controle dos investimentos. III. Gerenciar serviços terceirizados significa assegurar que os serviços prestados por fornecedores satisfaçam aos requisitos do negócio. Isso requer um processo efetivo de gestão da terceirização. Esse processo é realizado definindo-se claramente os papéis, responsabilidades e expectativas nos acordos de terceirização bem como revisando e monitorando tais acordos quanto à efetividade e à conformidade. A gestão eficaz dos serviços terceirizados minimiza os riscos de negócio associados aos fornecedores que não cumprem seu papel. As definições I, II e III correspondem, respectivamente, a

* **A)** ITIL - COBIT - BPMN
* **B)** COBIT - BSC - PDTIC
* **C)** BSC - ITIL - BPMN
* **D)** BPMN - PDTIC - BSC
* **E)** BSC - PDTIC - COBIT

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "ITIL COBIT BPMN". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, nIST SP 800 30 Rev. 1 Guide for Conducting Risk Assessments Guia metodológico oficial para condução de processos de avaliação e gestão de riscos em segurança da informação.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "COBIT BSC PDTIC". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, transferir / Compartilhar ( Risk Transfer / Sharing ): Compartilhar a carga financeira ou operacional das perdas com terceiros (ex.: contratação de apólice de seguro contra incidentes cibernéticos ou terceirização da infraestrutura de datacenter para provedores de nuvem sob contratos de SLA estritos).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "BSC ITIL BPMN". De acordo com a teoria estudada em *3. Gestão e Análise de Riscos de Segurança da Informação*, a gestão de riscos estabelece um processo contínuo e estruturado para identificar incertezas, avaliar a probabilidade de falhas e selecionar salvaguardas economicamente proporcionais.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "BPMN PDTIC BSC". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, governo Digital Programa de Privacidade e Segurança da Informação (PPSI 2.0) Diretrizes, requisitos de maturidade e gestão de riscos cibernéticos para a administração pública.
> - **E)** **Correta.** Conforme fundamentado na seção *🌐 Fontes Oficiais e Referências Bibliográficas* deste guia, aSSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. ABNT NBR ISO/IEC 27001:2022: Tecnologia da informação — Técnicas de segurança — Sistemas de gestão da segurança da informação — Requisitos. Rio de Janeiro: ABNT, 2022. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 13ª/2014) ao estabelecer que "BSC PDTIC COBIT".
>
> **Gabarito: E**

---


### Teste 060
**(FGV – TRT/13 – 2022 – Analista Judiciario Tecnologia Da Informacao)**
Conceito, surgido a partir do Protocolo de Kyoto em 1997, que visa à diminuição dos gases de efeito estufa, que provocam diversos problemas ambientais associados às mudanças climáticas. Eles fazem parte de um mecanismo de flexibilização que auxilia os países que possuem metas de redução da emissão de gases poluentes a alcançá-las. A cada tonelada não emitida, gera-se um crédito. Assim, quando um país consegue reduzir a emissão dessa tonelada, ele recebe uma certificação emitida pelo Mecanismo de Desenvolvimento Limpo (MDL), ou seja, recebe os créditos que estarão disponíveis para serem comercializados com os países que não alcançaram suas metas. A geração do crédito é realizada à medida que os países esforçam-se em projetos e ações que visam ao desenvolvimento sustentável, evitando, assim, o aumento do efeito estufa. Exemplos desses projetos são o empenho em reduzir os níveis de desmatamento, as campanhas para o consumo consciente, o uso de fontes de energia alternativas, entre outros. (mundoeducacao.uol.com.br. Adaptado) O texto refere-se aos créditos de

* **A)** Hidrogênio.
* **B)** Oxigênio.
* **C)** Carbono.
* **D)** Enxofre.
* **E)** Silício.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Hidrogênio". De acordo com a teoria estudada em *2. Classificação e Rotulagem da Informação*, a classificação atribui rótulos de sensibilidade aos ativos de informação da organização, ditando os níveis de proteção lógica e física a serem aplicados de forma proporcional ao dano decorrente de divulgação ou modificação indevida.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Oxigênio". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, garantia de que a informação, os sistemas computacionais e os ativos de telecomunicações associados estejam acessíveis e utilizáveis sob demanda pelos usuários autorizados sempre que necessário.
> - **C)** **Correta.** Conforme fundamentado na seção *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade* deste guia, ameaças clássicas: Ataques de negação de serviço (DoS e DDoS), falhas físicas de hardware em servidores e storages, interrupção no fornecimento de energia elétrica, panes nos links de internet e desastres ambientais (enchentes, incêndios em datacenters). Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT/13/2022) ao estabelecer que "Carbono".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Enxofre". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, mitigar / Reduzir ( Risk Mitigation / Reduction ): Implementar controles de segurança (técnicos, administrativos ou físicos) para reduzir a probabilidade e/ou o impacto do risco até patamares aceitáveis (ex.: instalar firewalls, adotar MFA e criptografia).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Silício". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, cláusula 10: Melhoria (Não conformidades, ações corretivas e ciclo contínuo).
>
> **Gabarito: C**

---


### Teste 061
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
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "DNS". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Escuta clandestina de rede ( sniffing/eavesdropping ), roubo de dispositivos físicos, engenharia social, vazamento inadvertido de dados fiscais protegidos por sigilo e acessos não autorizados.
> - **B)** **Correta.** Conforme fundamentado na seção *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade* deste guia, mecanismos técnicos: Funções criptográficas de espalhamento ( hashing criptográfico como SHA 256 e SHA 512), códigos de autenticação de mensagem (HMAC), assinaturas digitais, somas de verificação ( checksums ) e trilhas de auditoria imutáveis. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 15ª/2015) ao estabelecer que "Gateway".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "DHCP". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Adulteração maliciosa de tabelas contábeis ou salariais em bancos de dados ( tampering ), infecção por malware, ataques man in the middle e erros de transmissão de rede sem checagem de paridade.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Firewall". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, reservada: 5 anos — Autoridades que exerçam funções formais de direção, comando ou chefia — Não admite prorrogação. O prazo cessa impreterivelmente aos 5 anos.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "NAT". De acordo com a teoria estudada em *4.1 Métricas do CVSS v3.1 (Common Vulnerability Scoring System)*, exploitability: Vetor de Ataque (AV: Rede, Adjacente, Local, Físico), Complexidade do Ataque (AC: Baixa, Alta), Privilégios Requeridos (PR: Nenhum, Baixo, Alto) e Interação do Usuário (UI: Nenhuma, Requerida).
>
> **Gabarito: B**

---


### Teste 062
**(FCC – TRT 2ª – 2014 – Analista Judiciário - Tecnologia da Informação)**
Considere as seguintes afirmativas: I. Lei federal que condicione o exercício da profissão de músico à inscrição regular na Ordem dos Músicos do Brasil e ao pagamento das respectivas anuidades não ofende a Constituição, pois cabe ao legislador estabelecer qualificações profissionais a serem exigidas como condição ao exercício do direito fundamental à liberdade de profissão. II. É assegurada às entidades associativas, desde que expressamente autorizadas, legitimidade para representar seus filiados judicialmente, inclusive em sede de ação civil pública e de mandado de segurança coletivo. III. A inviolabilidade da intimidade, da honra e da imagem, bem como o direito à indenização por danos morais decorrentes de sua violação são constitucionalmente assegurados às pessoas naturais e não às pessoas jurídicas. Está correto o que consta em

* **A)** III, apenas.
* **B)** I e III, apenas.
* **C)** II, apenas.
* **D)** I, II e III.
* **E)** I, apenas. Noções de Direito Administrativo

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)* deste guia, decore rigorosamente os prazos decrescentes: 25 anos $\rightarrow$ 15 anos $\rightarrow$ 5 anos. A FCC inventa prazos alternativos inexistentes (como 10 ou 20 anos) ou inverte Secreta e Reservada. Além disso, lembre se: informações relativas à intimidade, vida privada, honra e imagem das pessoas têm restrição de acesso máxima de até 100 anos a contar da data de sua produção (Art. 31 da LAI), não se confundindo com prazos de segurança de Estado!. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 2ª/2014) ao estabelecer que "III, apenas".
> - **B)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e III, apenas". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, garantia de que o acesso à informação é restrito estrita e exclusivamente a pessoas, entidades ou processos formalmente autorizados.
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II, apenas". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, a norma ABNT NBR ISO/IEC 27001 estabelece os requisitos formais para estabelecer, implementar, manter e melhorar continuamente um Sistema de Gestão de Segurança da Informação (SGSI).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I, II e III". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, sTALLINGS, William. Criptografia e Segurança de Redes: Princípios e Práticas. 7. ed. São Paulo: Pearson Education do Brasil, 2018. (Cap. 1 Visão Geral de Segurança da Informação).
> - **E)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I, apenas. Noções de Direito Administrativo". De acordo com a teoria estudada em *2.2 Classificação Corporativa Geral de Ativos*, interna: Informação para circulação interna restrita aos servidores e colaboradores; divulgação indevida acarreta transtorno administrativo leve.
>
> **Gabarito: A**

---


### Teste 063
**(FCC – TRT 24ª – 2017 – Analista Judiciário - Tecnologia da Informação)**
Um Analista precisa escolher um Certificado de Assinatura Digital para ser utilizado na rede virtual privada da organização onde trabalha e na assinatura de documentos com verificação da integridade das informações. Optou corretamente por um certificado do tipo A2, cuja

* **A)** depicts the ITIL´s Release and Deployment Management process in which the account manager should try to handle that request on his own and explain the solution to the customer, then hand over the issue to a 2nd level support agent, who will hand over to upper level support, in a chain.
* **B)** shows the ITIL´s Service Portfolio Management process of a software manufacturer that is triggered by a customer requesting help from the account manager because of a well defined problem.
* **C)** isn’t useful to scope the process, get a basic understanding of the flow, and indicate the main steps, but it is relevant for discussing details of process improvements or even software driven support of the process.
* **D)** is simple because it assumes that a solution is always found to be explained to the customer. The model lacks all details of collaboration between the involved employees, that is important to the ITIL´s Incident Management process.
* **E)** shows the 2nd level support agent should figure out if the customer can fix the problem on her own, but if the agent is not sure about this he must deliver the responsability to a 3rd level agent or return to the 1st level, as recommended by ITIL.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "depicts the ITIL´s Release and Deployment Management process in which the account manager should try to handle...". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, nIST SP 800 37 Rev. 2 Risk Management Framework Diretrizes para aplicação do Risk Management Framework (RMF) aos sistemas e organizações.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "shows the ITIL´s Service Portfolio Management process of a software manufacturer that is triggered by a customer...". De acordo com a teoria estudada em *4.1 Métricas do CVSS v3.1 (Common Vulnerability Scoring System)*, o padrão CVSS (mantido pelo FIRST) quantifica a gravidade técnica de vulnerabilidades de software e hardware em uma escala contínua de 0,0 a 10,0.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "isn’t useful to scope the process, get a basic understanding of the flow, and indicate the main steps, but it is...". De acordo com a teoria estudada em *4.1 Métricas do CVSS v3.1 (Common Vulnerability Scoring System)*, scope (S): Escopo Inalterado ( Unchanged ) ou Alterado ( Changed , quando a falha compromete recursos fora de sua camada de autorização).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "is simple because it assumes that a solution is always found to be explained to the customer. The model lacks all...". De acordo com a teoria estudada em *4.2 As Quatro Fases do Ciclo de Resposta a Incidentes (NIST SP 800-61)*, atividades Pós Incidente ( Post Incident Activity / Lessons Learned ): Reunião formal de Lições Aprendidas para documentar como o incidente foi tratado, registrar métricas temporais e aprimorar as salvaguardas da fase de preparação.
> - **E)** **Correta.** Conforme fundamentado na seção *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade* deste guia, ameaças clássicas: Adulteração maliciosa de tabelas contábeis ou salariais em bancos de dados ( tampering ), infecção por malware, ataques man in the middle e erros de transmissão de rede sem checagem de paridade. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 24ª/2017) ao estabelecer que "shows the 2nd level support agent should figure out if the customer can fix the problem on her own, but if the...".
>
> **Gabarito: E**

---


### Teste 064
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Administração)**
Avalie se as seguintes afirmativas a seguir, contidas no Planejamento Estratégico do TCE-PA, correspondem a um valor institucional, à missão da organização ou à visão da organização. I. Ser instituição de referência no controle externo e contribuir para o aperfeiçoamento da administração pública. II. Primar pela divulgação clara e acessível dos seus atos e dos decorrentes de sua missão. III. Exercer o controle externo da gestão de recursos públicos estaduais em benefício da sociedade. IV. Atuar com liberdade, imparcialidade e autonomia. As afirmativas referem-se, respectivamente, a

* **A)** valor, visão, missão e valor.
* **B)** visão, missão, valor e valor.
* **C)** visão, visão, missão e missão.
* **D)** missão, visão, valor e visão.
* **E)** visão, valor, missão e valor.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "valor, visão, missão e valor". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, sTALLINGS, William. Criptografia e Segurança de Redes: Princípios e Práticas. 7. ed. São Paulo: Pearson Education do Brasil, 2018. (Cap. 1 Visão Geral de Segurança da Informação).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "visão, missão, valor e valor". De acordo com a teoria estudada em *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade*, (O que tem valor econômico ou funcional.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "visão, visão, missão e missão". De acordo com a teoria estudada em *3.2 Análise Qualitativa vs. Análise Quantitativa (SLE, ARO e ALE)*, onde $\text{AV}$ ( Asset Value ) é o valor financeiro do ativo e $\text{EF}$ ( Exposure Factor ) é a fração percentual do valor do ativo perdida em um único incidente (0% a 100%).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "missão, visão, valor e visão". De acordo com a teoria estudada em *3.2 Análise Qualitativa vs. Análise Quantitativa (SLE, ARO e ALE)*, $$\text{Valor do Controle} = (\text{ALE} {\text{antes}} \text{ALE} {\text{depois}}) \text{ACS}$$.
> - **E)** **Correta.** Conforme fundamentado na seção *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade* deste guia, ativo ( Asset ): Qualquer recurso humano, físico, tecnológico ou de informação que possui valor intrínseco para o cumprimento da missão da instituição. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "visão, valor, missão e valor".
>
> **Gabarito: E**

---


### Teste 065
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Administração)**
As opções a seguir apresentam objetivos do governo eletrônico, à exceção de uma. Assinale-a.

* **A)** Inclusão digital.
* **B)** Modernizar a máquina pública.
* **C)** Reduzir custos e melhorar a eficiência da administração pública no que se refere aos seus processos internos.
* **D)** Aumentar a transparência, o controle social e a accountability.
* **E)** Fomento econômico do setor de tecnologia da informação.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Inclusão digital". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, governo Digital Programa de Privacidade e Segurança da Informação (PPSI 2.0) Diretrizes, requisitos de maturidade e gestão de riscos cibernéticos para a administração pública.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Modernizar a máquina pública". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Reduzir custos e melhorar a eficiência da administração pública no que se refere aos seus processos internos". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, garantia de que o acesso à informação é restrito estrita e exclusivamente a pessoas, entidades ou processos formalmente autorizados.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Aumentar a transparência, o controle social e a accountability". De acordo com a teoria estudada em *2.2 Classificação Corporativa Geral de Ativos*, pública: Informação destinada à divulgação irrestrita (editais de licitação, acórdãos públicos, portal da transparência); o vazamento gera dano nulo.
> - **E)** **Correta.** Conforme fundamentado na seção *🌐 Fontes Oficiais e Referências Bibliográficas* deste guia, aSSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. ABNT NBR ISO/IEC 27001:2022: Tecnologia da informação — Técnicas de segurança — Sistemas de gestão da segurança da informação — Requisitos. Rio de Janeiro: ABNT, 2022. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "Fomento econômico do setor de tecnologia da informação".
>
> **Gabarito: E**

---


### Teste 066
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Administração)**
A administração é o conjunto de práticas e processos voltados para a organização, planejamento, direção e controle de recursos com o objetivo de alcançar metas e resultados desejados. Seus principais conceitos incluem eficiência, eficácia e efetividade, que medem o uso adequado de recursos, o alcance dos objetivos e o impacto das ações, respectivamente. Os objetivos da administração abrangem a otimização de processos, a maximização de resultados e a sustentabilidade organizacional, visando atender tanto às necessidades internas quanto às demandas externas do ambiente em que a organização opera. Com relação aos conceitos e objetivos da Administração, analise as afirmativas a seguir: I. No novo milênio, as organizações estão se transformando em estruturas enxutas, flexíveis e ágeis, caracterizadas por uma comunicação intensa, trabalho em equipe, busca por mercados globais e foco nas necessidades dos clientes. II. No advento e consolidação da sociedade e economia do conhecimento, os trabalhadores do conhecimento representam uma parcela crescente da força de trabalho, e o componente intelectual das atividades organizacionais deverá aumentar significativamente. III. A economia do conhecimento exige um aprendizado contínuo e ininterrupto para o desenvolvimento de qualificações mais amplas e complexas. Está correto o que se afirma em

* **A)** I, apenas.
* **B)** I e II, apenas.
* **C)** I e III, apenas.
* **D)** II e III, apenas.
* **E)** I, II e III.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I, apenas". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, cláusula 9: Avaliação de Desempenho (Auditorias internas e análise pela direção).
> - **B)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e II, apenas". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, cláusula 6: Planejamento (Tratamento de riscos e objetivos de segurança).
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e III, apenas". De acordo com a teoria estudada em *4.2 As Quatro Fases do Ciclo de Resposta a Incidentes (NIST SP 800-61)*, preparação ( Preparation ): Estabelecimento e capacitação da equipe técnica de resposta (CSIRT / CERT), aquisição de ferramentas de investigação forense, implantação de políticas e planos de comunicação.
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II e III, apenas". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, cláusula 10: Melhoria (Não conformidades, ações corretivas e ciclo contínuo).
> - **E)** **Correta.** Conforme fundamentado na seção *4.2 As Quatro Fases do Ciclo de Resposta a Incidentes (NIST SP 800-61)* deste guia, detecção e Análise ( Detection and Analysis ): Monitoramento contínuo de alertas de IDS/IPS, antivírus/EDR e correlação de logs em SIEM para constatar indícios de comprometimento ( IoCs ) e dimensionar o alcance do ataque. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "I, II e III".
>
> **Gabarito: E**

---


### Teste 067
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Administração)**
O processo administrativo é o conjunto de funções desempenhadas por administradores em diversos níveis e áreas da organização, visando alcançar metas previamente definidas. Assinale a opção que está associada à função administrativa da direção.

* **A)** Ação corretiva.
* **B)** Divisão do trabalho.
* **C)** Produção de planos.
* **D)** Monitoramento das atividades.
* **E)** Motivação das pessoas.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Ação corretiva". De acordo com a teoria estudada em *4.2 As Quatro Fases do Ciclo de Resposta a Incidentes (NIST SP 800-61)*, contenção: Ação emergencial prioritária voltada a estancar a disseminação do ataque e limitar o raio de destruição ( blast radius ), tal como isolar a máquina da rede, desconectar cabos ou bloquear portas de switches.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Divisão do trabalho". De acordo com a teoria estudada em *5.2 A Nova ISO/IEC 27002 (Edição 2022: 4 Temas e 93 Controles)*, cONTROLES DE PESSOAS ( 8 controles) ──► Recrutamento, trabalho remoto,.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Produção de planos". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, decore rigorosamente os prazos decrescentes: 25 anos $\rightarrow$ 15 anos $\rightarrow$ 5 anos. A FCC inventa prazos alternativos inexistentes (como 10 ou 20 anos) ou inverte Secreta e Reservada. Além disso, lembre se: informações relativas à intimidade, vida privada, honra e imagem das pessoas têm restrição de acesso máxima de até 100 anos a contar da data de sua produção (Art. 31 da LAI), não se confundindo com prazos de segurança de Estado!.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Monitoramento das atividades". De acordo com a teoria estudada em *4.2 As Quatro Fases do Ciclo de Resposta a Incidentes (NIST SP 800-61)*, detecção e Análise ( Detection and Analysis ): Monitoramento contínuo de alertas de IDS/IPS, antivírus/EDR e correlação de logs em SIEM para constatar indícios de comprometimento ( IoCs ) e dimensionar o alcance do ataque.
> - **E)** **Correta.** Conforme fundamentado na seção *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade* deste guia, garantia de que o acesso à informação é restrito estrita e exclusivamente a pessoas, entidades ou processos formalmente autorizados. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "Motivação das pessoas".
>
> **Gabarito: E**

---


### Teste 068
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Administração)**
A qualidade de vida no trabalho (QVT) refere-se ao bem-estar geral dos colaboradores no ambiente organizacional. Isso inclui fatores como condições físicas de trabalho, equilíbrio entre vida pessoal e profissional, reconhecimento, oportunidades de desenvolvimento, e um ambiente de trabalho seguro e saudável. Com relação à QVT, avalie as afirmativas a seguir. I. Concilia duas posições opostas: as demandas dos colaboradores por bem-estar e satisfação e o interesse das organizações nos efeitos positivos sobre a produtividade e a qualidade. II. Representa um intenso movimento em direção ao profundo respeito pelo bem-estar das pessoas do ponto de vista biológico, psicológico e social. III. Almeja uma visão fragmentada do ser humano em seu relacionamento com as organizações. Está correto o que se afirma em

* **A)** I, apenas.
* **B)** I e II, apenas.
* **C)** I e III, apenas.
* **D)** II e III, apenas.
* **E)** I, II e III.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I, apenas". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, decore rigorosamente os prazos decrescentes: 25 anos $\rightarrow$ 15 anos $\rightarrow$ 5 anos. A FCC inventa prazos alternativos inexistentes (como 10 ou 20 anos) ou inverte Secreta e Reservada. Além disso, lembre se: informações relativas à intimidade, vida privada, honra e imagem das pessoas têm restrição de acesso máxima de até 100 anos a contar da data de sua produção (Art. 31 da LAI), não se confundindo com prazos de segurança de Estado!.
> - **B)** **Correta.** Conforme fundamentado na seção *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade* deste guia, vulnerabilidade ( Vulnerability ): Ponto fraco, falha de projeto, brecha de configuração ou deficiência de controle em um ativo que pode ser explorado por uma ameaça. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "I e II, apenas".
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e III, apenas". De acordo com a teoria estudada em *5.2 A Nova ISO/IEC 27002 (Edição 2022: 4 Temas e 93 Controles)*, cONTROLES DE PESSOAS ( 8 controles) ──► Recrutamento, trabalho remoto,.
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II e III, apenas". De acordo com a teoria estudada em *2.2 Classificação Corporativa Geral de Ativos*, interna: Informação para circulação interna restrita aos servidores e colaboradores; divulgação indevida acarreta transtorno administrativo leve.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I, II e III". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, sTALLINGS, William. Criptografia e Segurança de Redes: Princípios e Práticas. 7. ed. São Paulo: Pearson Education do Brasil, 2018. (Cap. 1 Visão Geral de Segurança da Informação).
>
> **Gabarito: B**

---


### Teste 069
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Administração)**
Alguns indicadores derivados dos modelos de qualidade de vida no trabalho (QVT) influenciam fortemente a satisfação dos colaboradores. Assinale a opção que apresenta o indicador que trata de um agradável ambiente de amizades e camaradagem.

* **A)** Integração social.
* **B)** Autonomia.
* **C)** Retroação recebida.
* **D)** Heteronomia.
* **E)** Compensação justa e adequada.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade* deste guia, ameaças clássicas: Escuta clandestina de rede ( sniffing/eavesdropping ), roubo de dispositivos físicos, engenharia social, vazamento inadvertido de dados fiscais protegidos por sigilo e acessos não autorizados. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "Integração social".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Autonomia". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, decore rigorosamente os prazos decrescentes: 25 anos $\rightarrow$ 15 anos $\rightarrow$ 5 anos. A FCC inventa prazos alternativos inexistentes (como 10 ou 20 anos) ou inverte Secreta e Reservada. Além disso, lembre se: informações relativas à intimidade, vida privada, honra e imagem das pessoas têm restrição de acesso máxima de até 100 anos a contar da data de sua produção (Art. 31 da LAI), não se confundindo com prazos de segurança de Estado!.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Retroação recebida". De acordo com a teoria estudada em *2.2 Classificação Corporativa Geral de Ativos*, interna: Informação para circulação interna restrita aos servidores e colaboradores; divulgação indevida acarreta transtorno administrativo leve.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Heteronomia". De acordo com a teoria estudada em *5.2 A Nova ISO/IEC 27002 (Edição 2022: 4 Temas e 93 Controles)*, cONTROLES DE PESSOAS ( 8 controles) ──► Recrutamento, trabalho remoto,.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Compensação justa e adequada". De acordo com a teoria estudada em *1. Princípios Básicos da Segurança da Informação (CIDAN)*, a segurança da informação é definida pela norma ABNT NBR ISO/IEC 27000 como a preservação da confidencialidade, integridade e disponibilidade da informação, admitindo se adicionalmente propriedades vitais para transações formais como a autenticidade e o não repúdio. O mnemônico padronizado em concursos da FCC é CIDAN.
>
> **Gabarito: A**

---


### Teste 070
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Administração)**
As primeiras experiências sobre liderança remontam à antiguidade, onde líderes eram frequentemente escolhidos com base em sua força, coragem e habilidade em batalha. Essas experiências iniciais lançaram as bases para os diversos estilos e teorias de liderança que se desenvolveriam nos séculos seguintes, à medida que as sociedades se tornavam mais complexas e organizadas. Assinale a opção que descreve a liderança democrática.

* **A)** O líder ajusta seu comportamento e estratégias de liderança com base na maturidade e motivação dos seguidores.
* **B)** O líder ajusta seu comportamento e estratégias de liderança com base nas exigências da tarefa.
* **C)** O líder dá ordens claras e espera obediência inquestionável, com pouca contribuição dos membros da equipe.
* **D)** O líder fornece pouca ou nenhuma orientação direta e permite que os membros do grupo tomem decisões.
* **E)** O líder é atuante, consultivo, define objetivos e orienta as decisões a serem tomadas em conjunto com os subordinados.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O líder ajusta seu comportamento e estratégias de liderança com base na maturidade e motivação dos seguidores". De acordo com a teoria estudada em *4.1 Métricas do CVSS v3.1 (Common Vulnerability Scoring System)*, métricas de Base ( Base Metrics ): Qualidades intrínsecas e imutáveis da falha.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O líder ajusta seu comportamento e estratégias de liderança com base nas exigências da tarefa". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, cláusula 5: Liderança e Comprometimento da Alta Direção.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O líder dá ordens claras e espera obediência inquestionável, com pouca contribuição dos membros da equipe". De acordo com a teoria estudada em *4.2 As Quatro Fases do Ciclo de Resposta a Incidentes (NIST SP 800-61)*, preparação ( Preparation ): Estabelecimento e capacitação da equipe técnica de resposta (CSIRT / CERT), aquisição de ferramentas de investigação forense, implantação de políticas e planos de comunicação.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O líder fornece pouca ou nenhuma orientação direta e permite que os membros do grupo tomem decisões". De acordo com a teoria estudada em *4.1 Métricas do CVSS v3.1 (Common Vulnerability Scoring System)*, exploitability: Vetor de Ataque (AV: Rede, Adjacente, Local, Físico), Complexidade do Ataque (AC: Baixa, Alta), Privilégios Requeridos (PR: Nenhum, Baixo, Alto) e Interação do Usuário (UI: Nenhuma, Requerida).
> - **E)** **Correta.** Conforme fundamentado na seção *2. Classificação e Rotulagem da Informação* deste guia, a classificação atribui rótulos de sensibilidade aos ativos de informação da organização, ditando os níveis de proteção lógica e física a serem aplicados de forma proporcional ao dano decorrente de divulgação ou modificação indevida. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "O líder é atuante, consultivo, define objetivos e orienta as decisões a serem tomadas em conjunto com os...".
>
> **Gabarito: E**

---


### Teste 071
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Administração)**
A função legislativa serve como um meio eficaz para realizar mudanças sociais de forma pacífica e em conformidade com o direito, por meio da revisão, modificação e sanção de leis. Com relação à elaboração de propostas orçamentárias, avalie as afirmativas a seguir. I. O Projeto de Lei Orçamentária Anual (PLOA) é encaminhado ao Congresso Nacional até 31 de agosto, devendo ser devolvido para sanção até o encerramento da sessão legislativa. II. A verificação da fidelidade funcional dos agentes da administração responsáveis por bens e valores públicos é parte integrante do controle da execução orçamentária. III. A análise da conformidade legal dos atos que geram a arrecadação de receitas é parte integrante do controle da execução orçamentária. Está correto o que se afirma em

* **A)** I, apenas.
* **B)** I e II, apenas.
* **C)** I e III, apenas.
* **D)** II e III, apenas.
* **E)** I, II e III.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I, apenas". De acordo com a teoria estudada em *2. Classificação e Rotulagem da Informação*, a classificação atribui rótulos de sensibilidade aos ativos de informação da organização, ditando os níveis de proteção lógica e física a serem aplicados de forma proporcional ao dano decorrente de divulgação ou modificação indevida.
> - **B)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e II, apenas". De acordo com a teoria estudada em *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade*, vulnerabilidade ( Vulnerability ): Ponto fraco, falha de projeto, brecha de configuração ou deficiência de controle em um ativo que pode ser explorado por uma ameaça.
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e III, apenas". De acordo com a teoria estudada em *3.2 Análise Qualitativa vs. Análise Quantitativa (SLE, ARO e ALE)*, mensura as perdas e investimentos em valores monetários concretos (R$).
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II e III, apenas". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, mecanismos técnicos: Funções criptográficas de espalhamento ( hashing criptográfico como SHA 256 e SHA 512), códigos de autenticação de mensagem (HMAC), assinaturas digitais, somas de verificação ( checksums ) e trilhas de auditoria imutáveis.
> - **E)** **Correta.** Conforme fundamentado na seção *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)* deste guia, secreta: 15 anos — Titulares de autarquias, fundações e órgãos públicos sob mesma alçada legal — Não admite prorrogação. O prazo cessa impreterivelmente aos 15 anos. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "I, II e III".
>
> **Gabarito: E**

---


### Teste 072
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Ciência de Dados)**
De acordo com Robert Kaplan e David Norton, o Balanced Scorecard (BSC) traduz a missão e a estratégia de uma organização em objetivos e medidas, organizados segundo as seguintes quatro perspectivas:

* **A)** Financeira; Clientes; Processos Internos; Governamental.
* **B)** Financeira; Clientes; Processos Externos; Aprendizado e Crescimento.
* **C)** Financeira; Responsabilidade Social; Processos Externos; Ambiental.
* **D)** Financeira; Clientes; Processos Internos; Aprendizado e Crescimento.
* **E)** Financeira; Clientes; Processos Internos; Processos Externos.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Financeira; Clientes; Processos Internos; Governamental". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, garantia de que o acesso à informação é restrito estrita e exclusivamente a pessoas, entidades ou processos formalmente autorizados.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Financeira; Clientes; Processos Externos; Aprendizado e Crescimento". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, nIST SP 800 30 Rev. 1 Guide for Conducting Risk Assessments Guia metodológico oficial para condução de processos de avaliação e gestão de riscos em segurança da informação.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Financeira; Responsabilidade Social; Processos Externos; Ambiental". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Escuta clandestina de rede ( sniffing/eavesdropping ), roubo de dispositivos físicos, engenharia social, vazamento inadvertido de dados fiscais protegidos por sigilo e acessos não autorizados.
> - **D)** **Correta.** Conforme fundamentado na seção *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)* deste guia, transferir / Compartilhar ( Risk Transfer / Sharing ): Compartilhar a carga financeira ou operacional das perdas com terceiros (ex.: contratação de apólice de seguro contra incidentes cibernéticos ou terceirização da infraestrutura de datacenter para provedores de nuvem sob contratos de SLA estritos). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "Financeira; Clientes; Processos Internos; Aprendizado e Crescimento".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Financeira; Clientes; Processos Internos; Processos Externos". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, concluída a avaliação do risco, a organização deve optar formalmente por uma das quatro respostas estratégicas.
>
> **Gabarito: D**

---


### Teste 073
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Contabilidade)**
Quando em uma combinação, uma das partes envolvidas obtiver o controle de uma ou mais operações, deve-se classificar a combinação como aquisição, exceto se a operação tiver essência econômica de fusão. Para que a operação tenha essência econômica de fusão, deve-se considerar os indicadores relacionados à contraprestação e ao processo de tomada de decisão. Entre esses indicadores estão os seguintes, à exceção de um. Assinale-o.

* **A)** Ocorre a combinação de entidades sob controle comum.
* **B)** A combinação está sujeita à aprovação dos cidadãos de cada uma das partes por meio de consultas à sociedade.
* **C)** A combinação é imposta por terceiro sem que qualquer das partes da combinação seja envolvida no processo de tomada de decisão.
* **D)** A contraprestação é paga àquele que detêm o direito aos ativos líquidos da operação transferida, que é identificado e contactado.
* **E)** A contraprestação é paga por outras razões que não a de compensar aqueles que detêm direito aos ativos líquidos da operação transferida em razão da renúncia a esse direito.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Ocorre a combinação de entidades sob controle comum". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, garantia de que a informação, os sistemas computacionais e os ativos de telecomunicações associados estejam acessíveis e utilizáveis sob demanda pelos usuários autorizados sempre que necessário.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A combinação está sujeita à aprovação dos cidadãos de cada uma das partes por meio de consultas à sociedade". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes.
> - **C)** **Incorreta.** A opção promove generalização excessiva que desconsidera as condições técnicas e normativas ao afirmar que "A combinação é imposta por terceiro sem que qualquer das partes da combinação seja envolvida no processo de tomada...". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, cláusula 4: Contexto da Organização (partes interessadas e escopo do SGSI).
> - **D)** **Correta.** Conforme fundamentado na seção *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade* deste guia, risco Residual: Risco que subsiste e permanece após o projeto e a entrada em operação dos controles de segurança mitigadores. Deve situar se estritamente abaixo do Apetite ao Risco fixado pela diretoria do tribunal. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "A contraprestação é paga àquele que detêm o direito aos ativos líquidos da operação transferida, que é...".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A contraprestação é paga por outras razões que não a de compensar aqueles que detêm direito aos ativos líquidos da...". De acordo com a teoria estudada em *4.2 As Quatro Fases do Ciclo de Resposta a Incidentes (NIST SP 800-61)*, └── Recuperação: Restaurar backups íntegros e retornar à operação normal.
>
> **Gabarito: D**

---


### Teste 074
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Contabilidade)**
Uma sociedade empresária precisa aumentar o seu saldo em caixa, para pagar as suas despesas operacionais. No entanto, a sociedade empresária não deseja aumentar as suas despesas, que já estão comprometidas, e nem o seu nível de endividamento. Assinale a opção que indica uma estratégia que atende aos objetivos da sociedade empresária.

* **A)** Pagamento das despesas antecipadas.
* **B)** Aumento do capital social em dinheiro.
* **C)** Desconto de duplicadas em instituição bancária.
* **D)** Solicitação de empréstimo bancário de curto prazo.
* **E)** Solicitação de empréstimo bancário de longo prazo.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Pagamento das despesas antecipadas". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes.
> - **B)** **Correta.** Conforme fundamentado na seção *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade* deste guia, ameaças clássicas: Escuta clandestina de rede ( sniffing/eavesdropping ), roubo de dispositivos físicos, engenharia social, vazamento inadvertido de dados fiscais protegidos por sigilo e acessos não autorizados. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "Aumento do capital social em dinheiro".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Desconto de duplicadas em instituição bancária". De acordo com a teoria estudada em *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade*, ativo ( Asset ): Qualquer recurso humano, físico, tecnológico ou de informação que possui valor intrínseco para o cumprimento da missão da instituição.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Solicitação de empréstimo bancário de curto prazo". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, uLTRASSECRETA ──► Prazo Máximo: 25 ANOS (Prorrogável 1 única vez por igual período).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Solicitação de empréstimo bancário de longo prazo". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, sECRETA ──► Prazo Máximo: 15 ANOS (Não prorrogável além de 15 anos).
>
> **Gabarito: B**

---


### Teste 075
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Contabilidade)**
No Balanço Patrimonial de uma sociedade empresária, os direitos derivados de vendas, adiantamentos ou empréstimos a sociedades coligadas ou controladas, diretores acionistas ou participantes no lucro da companhia não são classificados como ativo realizável a longo prazo quando

* **A)** envolvem valores considerados sem verificabilidade.
* **B)** constituem negócios usuais na exploração do objeto da companhia.
* **C)** apresentam prazo de realização de até um ano a partir da data final do balanço.
* **D)** apresentam prazo de realização no exercício social corrente ao da data final do balanço.
* **E)** têm por objeto bens corpóreos destinados à manutenção das atividades ou exercidos com essa finalidade.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "envolvem valores considerados sem verificabilidade". De acordo com a teoria estudada em *3.2 Análise Qualitativa vs. Análise Quantitativa (SLE, ARO e ALE)*, mensura as perdas e investimentos em valores monetários concretos (R$).
> - **B)** **Correta.** Conforme fundamentado na seção *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade* deste guia, mecanismos técnicos: Redundância de hardware e fontes de alimentação, clusters de alta disponibilidade (HA ativo ativo ou ativo passivo), sistemas anti DDoS, geradores e nobreaks comutáveis, planos de continuidade de negócios (PCN/DRP) e rotinas estruturadas de backup. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "constituem negócios usuais na exploração do objeto da companhia".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "apresentam prazo de realização de até um ano a partir da data final do balanço". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, mecanismos técnicos: Criptografia em trânsito (TLS) e em repouso (TDE), controle de acesso lógico baseado em papéis (RBAC), mascaramento dinâmico de dados e soluções de Prevenção contra Perda de Dados ( DLP Data Loss Prevention ).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "apresentam prazo de realização no exercício social corrente ao da data final do balanço". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Escuta clandestina de rede ( sniffing/eavesdropping ), roubo de dispositivos físicos, engenharia social, vazamento inadvertido de dados fiscais protegidos por sigilo e acessos não autorizados.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "têm por objeto bens corpóreos destinados à manutenção das atividades ou exercidos com essa finalidade". De acordo com a teoria estudada em *3.2 Análise Qualitativa vs. Análise Quantitativa (SLE, ARO e ALE)*, onde $\text{ACS}$ ( Annualized Cost of Safeguard ) é o custo anual de manutenção do controle. Se o saldo for positivo, o controle de segurança é economicamente viável.
>
> **Gabarito: B**

---


### Teste 076
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Direito)**
A empresa Gama Ltda adquiriu um terreno para ali construir um posto de combustível. O imóvel, segundo estudos preliminares, está localizado em uma Área de Preservação Permanente (APP), próximo a uma nascente subterrânea que alimenta um dos rios que cortam o município. Mesmo com essa informação, o Instituto Ambiental Estadual, autarquia estadual, concedeu a licença para a construção do posto sob o argumento de que a nascente está canalizada e não haveria impacto significativo no meio ambiente. Além disso, alegou a autarquia estadual que antes da instalação do posto de gasolina, já havia sido concedida licença ambiental para um outro empreendimento que funcionou e causou dano ambiental no local. O Ministério Público não concordou e ingressou com ação civil pública contra a empresa, o instituto ambiental e os sócios da pessoa jurídica argumentando que a instalação do posto de combustível em uma APP contraria as leis ambientais e comprovou novo dano ambiental causado pela empresa Gama Ltda. No entanto, o juiz julgou os pedidos improcedentes sob o argumento de que não foram produzidas provas da ilegalidade de localização e instalação da empresa, diante do fato de que a licença foi concedida antes da instalação do empreendimento. Além disso, o magistrado alegou que, antes da instalação do posto de gasolina, já havia sido concedida licença ambiental para um outro empreendimento que funcionou no local. Assim, o juízo entendeu que não foi o posto de gasolina não deve ser condenado, porque a área já estava degradada. A sentença foi mantida pelo Tribunal de 2ª instância, pelos mesmos fundamentos. Ainda inconformado, o Ministério Público interpôs recurso especial. Com base na narrativa, assinale a afirmativa correta.

* **A)** Entendeu corretamente o tribunal de origem no sentido de que o posto de gasolina não tem responsabilidade civil, pois não teria provocado danos ambientais considerando que a área já estava degradada.
* **B)** Eventual aplicação de penalidades administrativas, em razão da responsabilidade administrativa ambiental do posto de gasolina, não obedeceria à sistemática da teoria da culpabilidade, sendo desnecessária a demonstração de seu elemento subjetivo e demonstração do nexo causal entre a conduta e o dano.
* **C)** Conquanto houvesse a instalação do empreendimento em área de preservação permanente, não foram produzidas provas da ilegalidade de localização e instalação da empresa, diante do fato de que a licença foi concedida antes da instalação do empreendimento.
* **D)** A consolidação da intervenção na área de preservação permanente não justifica que seja mantida a situação lesiva ao meio ambiente.
* **E)** A violação das regras protetivas do meio ambiente atrai a responsabilidade civil objetiva, informada pela teoria do risco integral, nos termos do Art. 14, § 1º, da Lei nº 6.938/81, contra a empresa e os sócios da pessoa jurídica, exceto para a autarquia estadual, com presunção do prejuízo causado ao meio ambiente (dano in re ipsa), ensejando o dever de indenizar.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Entendeu corretamente o tribunal de origem no sentido de que o posto de gasolina não tem responsabilidade civil...". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Ataques de negação de serviço (DoS e DDoS), falhas físicas de hardware em servidores e storages, interrupção no fornecimento de energia elétrica, panes nos links de internet e desastres ambientais (enchentes, incêndios em datacenters).
> - **B)** **Incorreta.** A opção afasta requisito ou relação estrutural exigida pela matéria ao afirmar que "Eventual aplicação de penalidades administrativas, em razão da responsabilidade administrativa ambiental do posto...". De acordo com a teoria estudada em *2.2 Classificação Corporativa Geral de Ativos*, confidencial: Informações estratégicas, relatórios preliminares de auditoria em instrução ou dados cadastrais sob sigilo fiscal; vazamento gera dano financeiro ou institucional grave.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Conquanto houvesse a instalação do empreendimento em área de preservação permanente, não foram produzidas provas...". De acordo com a teoria estudada em *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade*, risco Inerente: Risco existente em seu estado natural bruto, antes da implementação de qualquer controle protetivo.
> - **D)** **Correta.** Conforme fundamentado na seção *1. Princípios Básicos da Segurança da Informação (CIDAN)* deste guia, a segurança da informação é definida pela norma ABNT NBR ISO/IEC 27000 como a preservação da confidencialidade, integridade e disponibilidade da informação, admitindo se adicionalmente propriedades vitais para transações formais como a autenticidade e o não repúdio. O mnemônico padronizado em concursos da FCC é CIDAN. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "A consolidação da intervenção na área de preservação permanente não justifica que seja mantida a situação lesiva...".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A violação das regras protetivas do meio ambiente atrai a responsabilidade civil objetiva, informada pela teoria...". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes.
>
> **Gabarito: D**

---


### Teste 077
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Direito)**
Considere a seguinte situação hipotética: Maria e José eram sócios-administradores da pessoa jurídica XYZ Ltda. Em 2022, Maria alienou regularmente a totalidade de suas quotas a João, e se retirou da administração da sociedade. João e José passaram a ser os únicos administradores da pessoa jurídica XYZ Ltda. desde então. Em 2023, a fazenda estadual ajuizou execução fiscal em face da pessoa jurídica XYZ Ltda., visando à cobrança de ICMS de 2021 a 2022, quando Maria e José eram administradores da empresa. Como o oficial de justiça não conseguiu citar a empresa executada, pois não estava mais funcionando no local de domicílio fiscal informado às autoridades públicas, foi deferida a inclusão no polo passivo da execução de Maria, José e João. Sobre o caso, a jurisprudência e a legislação em vigor atribuem a responsabilidade tributária a

* **A)** João, Maria e José.
* **B)** Maria e José, apenas.
* **C)** José, apenas.
* **D)** José e João, apenas.
* **E)** Maria e João, apenas.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "João, Maria e José". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes.
> - **B)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "Maria e José, apenas". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, reservada: 5 anos — Autoridades que exerçam funções formais de direção, comando ou chefia — Não admite prorrogação. O prazo cessa impreterivelmente aos 5 anos.
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "José, apenas". De acordo com a teoria estudada em *2.2 Classificação Corporativa Geral de Ativos*, confidencial: Informações estratégicas, relatórios preliminares de auditoria em instrução ou dados cadastrais sob sigilo fiscal; vazamento gera dano financeiro ou institucional grave.
> - **D)** **Correta.** Conforme fundamentado na seção *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade* deste guia, mecanismos técnicos: Redundância de hardware e fontes de alimentação, clusters de alta disponibilidade (HA ativo ativo ou ativo passivo), sistemas anti DDoS, geradores e nobreaks comutáveis, planos de continuidade de negócios (PCN/DRP) e rotinas estruturadas de backup. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "José e João, apenas".
> - **E)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "Maria e João, apenas". De acordo com a teoria estudada em *2.2 Classificação Corporativa Geral de Ativos*, restrita / Secreta: Nível máximo corporativo (chaves criptográficas mestras de certificados de segurança, senhas de administradores de domínios centrais); divulgação gera dano catastrófico e imediato.
>
> **Gabarito: D**

---


### Teste 078
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Direito)**
Avalie se as características-chave de entidade do setor público que reporta a informação contábil incluem: I. ser uma entidade que capta recursos da sociedade ou em nome desta e/ou utiliza recursos para realizar atividades em benefício dela; II. existirem usuários de serviços ou provedores de recursos dependentes de informações contidas nos relatórios contábeis de propósito geral das entidades do setor público para fins de prestação de contas e responsabilização e tomada de decisão; III. apresentar resultado superavitário em pelo menos dois exercícios sociais, mesmo não sendo essa a sua finalidade. De acordo com a NBC TSP Estrutura Conceitual – Estrutura Conceitual para Elaboração e Divulgação de Informação Contábil de Propósito Geral pelas Entidades do Setor Público, a entidade do setor público que reporta a informação contábil deve apresentar as seguintes características-chave:

* **A)** I, apenas.
* **B)** I e II, apenas.
* **C)** I e III, apenas.
* **D)** II e III, apenas.
* **E)** I, II e III.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I, apenas". De acordo com a teoria estudada em *2.2 Classificação Corporativa Geral de Ativos*, confidencial: Informações estratégicas, relatórios preliminares de auditoria em instrução ou dados cadastrais sob sigilo fiscal; vazamento gera dano financeiro ou institucional grave.
> - **B)** **Correta.** Conforme fundamentado na seção *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)* deste guia, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "I e II, apenas".
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e III, apenas". De acordo com a teoria estudada em *2.2 Classificação Corporativa Geral de Ativos*, pública: Informação destinada à divulgação irrestrita (editais de licitação, acórdãos públicos, portal da transparência); o vazamento gera dano nulo.
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II e III, apenas". De acordo com a teoria estudada em *2.2 Classificação Corporativa Geral de Ativos*, interna: Informação para circulação interna restrita aos servidores e colaboradores; divulgação indevida acarreta transtorno administrativo leve.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I, II e III". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, garantia de que o acesso à informação é restrito estrita e exclusivamente a pessoas, entidades ou processos formalmente autorizados.
>
> **Gabarito: B**

---


### Teste 079
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Gestão Governamental)**
Gisele é formada em Economia e vem estudando há alguns anos para concurso público, com vistas a concretizar seus planos de ser aprovada para cargo efetivo, que lhe assegure a garantia da estabilidade após o preenchimento dos respectivos requisitos. Diante dessa situação hipotética, é correto afirmar que Gisele colocará em prática o seu projeto pessoal caso venha a concorrer para

* **A)** a seleção para certo emprego público em empresa pública estadual.
* **B)** o procedimento seletivo conduzido por entidade integrante do serviço social autônomo.
* **C)** o certame realizado para integrar o quadro de servidores de carreira de certa autarquia estadual.
* **D)** o preenchimento de determinado cargo exclusivamente em comissão junto a determinado Tribunal de Contas.
* **E)** a contratação temporária, para atender situação emergencial de relevante interesse público, por determinado Estado.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "a seleção para certo emprego público em empresa pública estadual". De acordo com a teoria estudada em *2.2 Classificação Corporativa Geral de Ativos*, interna: Informação para circulação interna restrita aos servidores e colaboradores; divulgação indevida acarreta transtorno administrativo leve.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "o procedimento seletivo conduzido por entidade integrante do serviço social autônomo". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Escuta clandestina de rede ( sniffing/eavesdropping ), roubo de dispositivos físicos, engenharia social, vazamento inadvertido de dados fiscais protegidos por sigilo e acessos não autorizados.
> - **C)** **Correta.** Conforme fundamentado na seção *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade* deste guia, ameaças clássicas: Ataques de negação de serviço (DoS e DDoS), falhas físicas de hardware em servidores e storages, interrupção no fornecimento de energia elétrica, panes nos links de internet e desastres ambientais (enchentes, incêndios em datacenters). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "o certame realizado para integrar o quadro de servidores de carreira de certa autarquia estadual".
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "o preenchimento de determinado cargo exclusivamente em comissão junto a determinado Tribunal de Contas". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, ultrassecreta: 25 anos — Presidente da República, Vice Presidente, Ministros de Estado, Comandantes das Forças Armadas — Prorrogável uma única vez, por igual período (totalizando até 50 anos), exclusivamente pela CMRI ( Comissão Mista de Reavaliação de Informações ).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "a contratação temporária, para atender situação emergencial de relevante interesse público, por determinado Estado". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, transferir / Compartilhar ( Risk Transfer / Sharing ): Compartilhar a carga financeira ou operacional das perdas com terceiros (ex.: contratação de apólice de seguro contra incidentes cibernéticos ou terceirização da infraestrutura de datacenter para provedores de nuvem sob contratos de SLA estritos).
>
> **Gabarito: C**

---


### Teste 080
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Gestão Governamental)**
Em 2021, visando enfrentar as consequências sociais e econômicas da pandemia da Covid-19, a Constituição Federal de 1988 foi alterada. Além de regras transitórias sobre redução de benefícios tributários, foi promovida a desvinculação parcial do superávit financeiro de fundos públicos, bem como suspensas condicionalidades para realização de despesas com concessão de auxílio emergencial residual. No contexto do dispositivo que promoveu tais alterações, destaca-se os a seguir elencados, à exceção de um. Assinale-o.

* **A)** A inclusão da obrigatoriedade aos entes públicos para disponibilizar suas informações e dados contábeis, orçamentários e fiscais, conforme periodicidade, formato e sistema estabelecidos pelo órgão central de contabilidade da União, de forma a garantir a rastreabilidade, a comparabilidade e a publicidade dos dados coletados.
* **B)** A disposição, em Lei Complementar, de indicadores para apuração da dívida pública, visando a aferição de sua sustentabilidade.
* **C)** A compatibilização dos resultados fiscais com a trajetória da dívida pública.
* **D)** A preocupação com a sustentabilidade fiscal do setor público, impondo uma trajetória de convergência do montante da dívida com os limites definidos em legislação.
* **E)** A possibilidade de planejamento de alienação de ativos com vistas à redução do montante da dívida pública.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)* deste guia, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "A inclusão da obrigatoriedade aos entes públicos para disponibilizar suas informações e dados contábeis...".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A disposição, em Lei Complementar, de indicadores para apuração da dívida pública, visando a aferição de sua...". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Escuta clandestina de rede ( sniffing/eavesdropping ), roubo de dispositivos físicos, engenharia social, vazamento inadvertido de dados fiscais protegidos por sigilo e acessos não autorizados.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A compatibilização dos resultados fiscais com a trajetória da dívida pública". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Adulteração maliciosa de tabelas contábeis ou salariais em bancos de dados ( tampering ), infecção por malware, ataques man in the middle e erros de transmissão de rede sem checagem de paridade.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A preocupação com a sustentabilidade fiscal do setor público, impondo uma trajetória de convergência do montante...". De acordo com a teoria estudada em *2.2 Classificação Corporativa Geral de Ativos*, confidencial: Informações estratégicas, relatórios preliminares de auditoria em instrução ou dados cadastrais sob sigilo fiscal; vazamento gera dano financeiro ou institucional grave.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A possibilidade de planejamento de alienação de ativos com vistas à redução do montante da dívida pública". De acordo com a teoria estudada em *2.2 Classificação Corporativa Geral de Ativos*, pública: Informação destinada à divulgação irrestrita (editais de licitação, acórdãos públicos, portal da transparência); o vazamento gera dano nulo.
>
> **Gabarito: A**

---


### Teste 081
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Gestão Governamental)**
Benjamin Zimler registra que o controle interno se caracteriza como gênero do qual se constituem espécies o controle administrativo e o sistema de controle interno estatuído no art. 74 da Constituição Federal. (ZIMLER, Benjamin. Direito Administrativo e Controle. Ed. Fórum, 2015, p. 165) O dispositivo constitucional citado pelo autor atribui ao sistema de controle interno a função de

* **A)** fiscalizar as contas nacionais das empresas supranacionais de cujo capital social a União participe, de forma direta ou indireta, nos termos do tratado constitutivo.
* **B)** fiscalizar a aplicação de quaisquer recursos repassados pela União mediante convênio, acordo, ajuste ou outros instrumentos congêneres, a Estado, ao Distrito Federal ou a Município.
* **C)** julgar as contas dos administradores e demais responsáveis por dinheiros, bens e valores públicos da administração direta e indireta.
* **D)** exercer o controle das operações de crédito, avais e garantias, bem como dos direitos e haveres da União.
* **E)** comprovar somente a legalidade da gestão orçamentária, financeira e patrimonial nos órgãos e entidades da administração federal.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "fiscalizar as contas nacionais das empresas supranacionais de cujo capital social a União participe, de forma...". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "fiscalizar a aplicação de quaisquer recursos repassados pela União mediante convênio, acordo, ajuste ou outros...". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, aceitar / Reter ( Risk Acceptance / Retention ): Manter o risco no nível atual sem novos controles, mediante aprovação formal fundamentada da alta administração, quando o custo da salvaguarda técnica for superior à perda monetária potencial estimada.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "julgar as contas dos administradores e demais responsáveis por dinheiros, bens e valores públicos da administração...". De acordo com a teoria estudada em *2.2 Classificação Corporativa Geral de Ativos*, restrita / Secreta: Nível máximo corporativo (chaves criptográficas mestras de certificados de segurança, senhas de administradores de domínios centrais); divulgação gera dano catastrófico e imediato.
> - **D)** **Correta.** Conforme fundamentado na seção *2. Classificação e Rotulagem da Informação* deste guia, a classificação atribui rótulos de sensibilidade aos ativos de informação da organização, ditando os níveis de proteção lógica e física a serem aplicados de forma proporcional ao dano decorrente de divulgação ou modificação indevida. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "exercer o controle das operações de crédito, avais e garantias, bem como dos direitos e haveres da União".
> - **E)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "comprovar somente a legalidade da gestão orçamentária, financeira e patrimonial nos órgãos e entidades da...". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, governo Digital Programa de Privacidade e Segurança da Informação (PPSI 2.0) Diretrizes, requisitos de maturidade e gestão de riscos cibernéticos para a administração pública.
>
> **Gabarito: D**

---


### Teste 082
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Gestão Governamental)**
Com relação aos crimes contra a ordem tributária, avalie se as afirmativas a seguir são verdadeiras (V) ou falsas (F). ( ) Para ser tipificado o crime de sonegação fiscal, caracterizado pela omissão de informação com o intuito de redução de tributo, é necessário o prévio lançamento definitivo do tributo. ( ) Ao tipificar como ilícito penal a conduta de deixar de recolher tributo ou contribuição social, descontado ou cobrado, no prazo legal, o legislador acabou por violar a CRFB/88, pois acabou por instituir prisão civil por dívida. ( ) A incidência do princípio da insignificância, nos crimes contra a ordem tributária, deve ser realizada considerando o montante total objeto da constituição definitiva do crédito tributária, excluindo juros e multa, sendo irrelevante o fato da conduta criminosa ter sido praticada em continuidade delitiva. A As afirmativas são, respectivamente,

* **A)** V – V – F.
* **B)** V – F – V.
* **C)** F – F – V.
* **D)** F – V – F.
* **E)** F – V – V.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "V – V – F". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, garantia de que a informação, os sistemas computacionais e os ativos de telecomunicações associados estejam acessíveis e utilizáveis sob demanda pelos usuários autorizados sempre que necessário.
> - **B)** **Correta.** Conforme fundamentado na seção *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)* deste guia, secreta: 15 anos — Titulares de autarquias, fundações e órgãos públicos sob mesma alçada legal — Não admite prorrogação. O prazo cessa impreterivelmente aos 15 anos. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "V – F – V".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "F – F – V". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Escuta clandestina de rede ( sniffing/eavesdropping ), roubo de dispositivos físicos, engenharia social, vazamento inadvertido de dados fiscais protegidos por sigilo e acessos não autorizados.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "F – V – F". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, mecanismos técnicos: Redundância de hardware e fontes de alimentação, clusters de alta disponibilidade (HA ativo ativo ou ativo passivo), sistemas anti DDoS, geradores e nobreaks comutáveis, planos de continuidade de negócios (PCN/DRP) e rotinas estruturadas de backup.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "F – V – V". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, mecanismos técnicos: Criptografia em trânsito (TLS) e em repouso (TDE), controle de acesso lógico baseado em papéis (RBAC), mascaramento dinâmico de dados e soluções de Prevenção contra Perda de Dados ( DLP Data Loss Prevention ).
>
> **Gabarito: B**

---


### Teste 083
**(FGV – TCE/PI – 2025 – Auditor de Controle Externo - Controle Externo - Específica de Área Comum)**
Os modelos de Administração Pública refletem a evolução das formas de gestão governamental, buscando equilibrar eficiência, transparência e participação cidadã para melhor atender às demandas da sociedade. O modelo em que a legitimidade se origina das leis e do direito e é pautada, a princípio, pela racionalidade e objetividade é o(a)

* **A)** carismático.
* **B)** tradicional.
* **C)** racional legal.
* **D)** nova gestão pública.
* **E)** nova governança pública.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "carismático". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, governo Digital Programa de Privacidade e Segurança da Informação (PPSI 2.0) Diretrizes, requisitos de maturidade e gestão de riscos cibernéticos para a administração pública.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "tradicional". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes.
> - **C)** **Correta.** Conforme fundamentado na seção *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)* deste guia, secreta: 15 anos — Titulares de autarquias, fundações e órgãos públicos sob mesma alçada legal — Não admite prorrogação. O prazo cessa impreterivelmente aos 15 anos. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PI/2025) ao estabelecer que "racional legal".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "nova gestão pública". De acordo com a teoria estudada em *5.2 A Nova ISO/IEC 27002 (Edição 2022: 4 Temas e 93 Controles)*, cONTROLES ORGANIZACIONAIS (37 controles) ──► Políticas, gestão de ativos,.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "nova governança pública". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, decreto Federal nº 9.637/2018 (Política Nacional de Segurança da Informação) Institui a PNSI, dispondo sobre governança, gestão de riscos e tratamento de incidentes de segurança da informação.
>
> **Gabarito: C**

---


### Teste 084
**(FGV – TCE/PI – 2025 – Auditor de Controle Externo - Controle Externo - Específica de Área Comum)**
A NBASP 400 - Auditoria de Conformidade assegura que o auditor execute seu trabalho de maneira objetiva, garantindo a transparência e a integridade da gestão pública. Ao promover a conformidade, a NBASP 400 reforça a responsabilidade e a prestação de contas, fortalecendo a confiança da sociedade nas instituições governamentais. Assinale a opção que indica o elemento que um Relatório de Auditoria de Conformidade deve incluir.

* **A)** Local da auditoria.
* **B)** Entidade revisora.
* **C)** Programas avaliados.
* **D)** Achados de auditoria.
* **E)** Planejamento da auditoria.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Local da auditoria". De acordo com a teoria estudada em *2.2 Classificação Corporativa Geral de Ativos*, confidencial: Informações estratégicas, relatórios preliminares de auditoria em instrução ou dados cadastrais sob sigilo fiscal; vazamento gera dano financeiro ou institucional grave.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Entidade revisora". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Programas avaliados". De acordo com a teoria estudada em *2.2 Classificação Corporativa Geral de Ativos*, pública: Informação destinada à divulgação irrestrita (editais de licitação, acórdãos públicos, portal da transparência); o vazamento gera dano nulo.
> - **D)** **Correta.** Conforme fundamentado na seção *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade* deste guia, mecanismos técnicos: Funções criptográficas de espalhamento ( hashing criptográfico como SHA 256 e SHA 512), códigos de autenticação de mensagem (HMAC), assinaturas digitais, somas de verificação ( checksums ) e trilhas de auditoria imutáveis. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PI/2025) ao estabelecer que "Achados de auditoria".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Planejamento da auditoria". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, cláusula 6: Planejamento (Tratamento de riscos e objetivos de segurança).
>
> **Gabarito: D**

---


### Teste 085
**(FGV – TCE/PI – 2025 – Auditor de Controle Externo - Controle Externo - Específica de Área Comum)**
Uma sociedade empresária localizada em Parnaíba/PI deixou de pagar por alguns meses a contribuição previdenciária de 2024 por falta de recurso financeiro. Ela foi então informada de que o Governo Federal havia lançado um programa permitindo a quitação da dívida com exclusão das penalidades. A sociedade empresária aderiu ao programa porque viu nele uma boa oportunidade de quitar sua obrigação. Assinale a opção que indica o fenômeno ocorrido.

* **A)** Anistia.
* **B)** Remição.
* **C)** Remissão.
* **D)** Imunidade.
* **E)** Dação em pagamento.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *🌐 Fontes Oficiais e Referências Bibliográficas* deste guia, governo Digital Programa de Privacidade e Segurança da Informação (PPSI 2.0) Diretrizes, requisitos de maturidade e gestão de riscos cibernéticos para a administração pública. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PI/2025) ao estabelecer que "Anistia".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Remição". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Remissão". De acordo com a teoria estudada em *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade*, ativo ( Asset ): Qualquer recurso humano, físico, tecnológico ou de informação que possui valor intrínseco para o cumprimento da missão da instituição.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Imunidade". De acordo com a teoria estudada em *5.3 A Declaração de Aplicabilidade (SoA) e a ISO/IEC 27005*, a justificativa formal obrigatória para a exclusão de qualquer controle que não tenha sido adotado.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Dação em pagamento". De acordo com a teoria estudada em *2.2 Classificação Corporativa Geral de Ativos*, confidencial: Informações estratégicas, relatórios preliminares de auditoria em instrução ou dados cadastrais sob sigilo fiscal; vazamento gera dano financeiro ou institucional grave.
>
> **Gabarito: A**

---


### Teste 086
**(FGV – TCE/PI – 2025 – Auditor de Controle Externo - Controle Externo - Específica de Área Comum)**
Godofredo está radiante porque foi aprovado no concurso público para o Tribunal de Contas do Estado do Piauí, em 2024. Agora Godofredo prepara-se para tomar posse e cumprir escorreitamente as suas atividades no serviço público. De acordo com a Lei de Regência, assinale a opção que indica a contribuição mensal de Godofredo para o plano de custeio do regime próprio de previdência social dos servidores públicos do Estado do Piauí.

* **A)** 10%.
* **B)** 12%.
* **C)** 11%.
* **D)** 14%.
* **E)** 13%.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "10%". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, grau de Sigilo: Prazo Máximo de Restrição — Competência Originária Típica para Classificar — Regime de Prorrogação.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "12%". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, secreta: 15 anos — Titulares de autarquias, fundações e órgãos públicos sob mesma alçada legal — Não admite prorrogação. O prazo cessa impreterivelmente aos 15 anos.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "11%". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Escuta clandestina de rede ( sniffing/eavesdropping ), roubo de dispositivos físicos, engenharia social, vazamento inadvertido de dados fiscais protegidos por sigilo e acessos não autorizados.
> - **D)** **Correta.** Conforme fundamentado na seção *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade* deste guia, ameaças clássicas: Ataques de negação de serviço (DoS e DDoS), falhas físicas de hardware em servidores e storages, interrupção no fornecimento de energia elétrica, panes nos links de internet e desastres ambientais (enchentes, incêndios em datacenters). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PI/2025) ao estabelecer que "14%".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "13%". De acordo com a teoria estudada em *2.2 Classificação Corporativa Geral de Ativos*, pública: Informação destinada à divulgação irrestrita (editais de licitação, acórdãos públicos, portal da transparência); o vazamento gera dano nulo.
>
> **Gabarito: D**

---


### Teste 087
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Fiscalização - Ciências Atuariais)**
Considerando os contornos da Administração Pública na Constituição de 1988, é correto afirmar que são entidades administrativas, integrantes da Administração Indireta, que são criadas por lei, diante de sua personalidade jurídica de direito público

* **A)** as entidades autárquicas.
* **B)** as sociedades de economia mista.
* **C)** as empresas públicas.
* **D)** os serviços sociais autônomos.
* **E)** as organizações da sociedade civil de interesse público.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade* deste guia, garantia de que o acesso à informação é restrito estrita e exclusivamente a pessoas, entidades ou processos formalmente autorizados. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "as entidades autárquicas".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "as sociedades de economia mista". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, ultrassecreta: 25 anos — Presidente da República, Vice Presidente, Ministros de Estado, Comandantes das Forças Armadas — Prorrogável uma única vez, por igual período (totalizando até 50 anos), exclusivamente pela CMRI ( Comissão Mista de Reavaliação de Informações ).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "as empresas públicas". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, aceitar / Reter ( Risk Acceptance / Retention ): Manter o risco no nível atual sem novos controles, mediante aprovação formal fundamentada da alta administração, quando o custo da salvaguarda técnica for superior à perda monetária potencial estimada.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "os serviços sociais autônomos". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, governo Digital Programa de Privacidade e Segurança da Informação (PPSI 2.0) Diretrizes, requisitos de maturidade e gestão de riscos cibernéticos para a administração pública.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "as organizações da sociedade civil de interesse público". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes.
>
> **Gabarito: A**

---


### Teste 088
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Fiscalização - Ciências Atuariais)**
A sociedade empresária “Conhecendo o Brasil”, especializada em turismo doméstico, regularmente constituída e com sede em Bonito (PA), conforme seu ato constitutivo, resolveu expandir os negócios e, para tal, constituiu três filiais. Assim, a diretoria permaneceu situada em Bonito (PA) e foram criadas filiais em Salvador (BA), Guarapari (ES) e Florianópolis (SC). Todas as unidades estão em funcionamento e são geridas como unidades de negócios. Recentemente, o gerente da filial de Guarapari foi questionado por um dos parceiros comerciais locais acerca da indicação do domicílio da “Conhecendo Brasil” no contrato com ele firmado. Segundo o parceiro comercial, a indicação de Bonito como domicílio está errada, pois o contrato foi celebrado em Guarapari. Sobre a situação narrada e em conformidade com a legislação vigente, é correto afirmar que

* **A)** não assiste razão ao parceiro comercial da filial de Guarapari, pois, de fato, o domicílio da “Conhecendo o Brasil” é, exclusivamente, Bonito (PA).
* **B)** não assiste razão ao parceiro comercial da filial de Guarapari, pois a sede e as filiais da “Conhecendo o Brasil” são consideradas como domicílio da pessoa jurídica para os atos nele praticados.
* **C)** assiste razão ao parceiro comercial da filial de Guarapari, pois o domicílio para o exercício dos direitos e obrigações da “Conhecendo o Brasil” deverá ser o local onde os contratos foram firmados, não sendo possível especificar domicílio diverso nos contratos escritos.
* **D)** não assiste razão ao parceiro comercial da filial de Guarapari, pois o domicílio da “Conhecendo o Brasil” é o local em que a sociedade empresária ficar sediada em ânimo definitivo.
* **E)** assiste razão ao parceiro comercial da filial de Guarapari, pois à pessoa jurídica que possui filiais, aplica-se o princípio da pluralidade domiciliar e, conjuntamente, a regra do domicílio necessário que será aquele onde os atos tiverem sido praticados.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "não assiste razão ao parceiro comercial da filial de Guarapari, pois, de fato, o domicílio da “Conhecendo o...". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, garantia de que o acesso à informação é restrito estrita e exclusivamente a pessoas, entidades ou processos formalmente autorizados.
> - **B)** **Correta.** Conforme fundamentado na seção *🌐 Fontes Oficiais e Referências Bibliográficas* deste guia, sTALLINGS, William. Criptografia e Segurança de Redes: Princípios e Práticas. 7. ed. São Paulo: Pearson Education do Brasil, 2018. (Cap. 1 Visão Geral de Segurança da Informação). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "não assiste razão ao parceiro comercial da filial de Guarapari, pois a sede e as filiais da “Conhecendo o Brasil”...".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "assiste razão ao parceiro comercial da filial de Guarapari, pois o domicílio para o exercício dos direitos e...". De acordo com a teoria estudada em *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade*, vulnerabilidade ( Vulnerability ): Ponto fraco, falha de projeto, brecha de configuração ou deficiência de controle em um ativo que pode ser explorado por uma ameaça.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "não assiste razão ao parceiro comercial da filial de Guarapari, pois o domicílio da “Conhecendo o Brasil” é o...". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "assiste razão ao parceiro comercial da filial de Guarapari, pois à pessoa jurídica que possui filiais, aplica se o...". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, garantia de que a informação, os sistemas computacionais e os ativos de telecomunicações associados estejam acessíveis e utilizáveis sob demanda pelos usuários autorizados sempre que necessário.
>
> **Gabarito: B**

---


### Teste 089
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Fiscalização - Ciências Atuariais)**
Em relação às Emendas Constitucionais que reformaram os regimes geral e próprios de previdência social, é incorreto afirmar que

* **A)** apenas com a Emenda Constitucional nº 20, de 15/12/1998, a Constituição Federal de 1988 passou a adotar o princípio do equilíbrio financeiro e atuarial, também posteriormente adotado com o artigo 69 da Lei de Responsabilidade Fiscal (Lei Complementar nº 101, de 04/05/2000).
* **B)** a Emenda Constitucional nº 41, de 19/12/2003 criou o princípio da solidariedade contributiva, o que permitiu a cobrança de contribuição de inativos e pensionistas.
* **C)** a Emenda Constitucional nº 47, de 05/07/2005 restabeleceu critérios condicionantes de paridade e integralidade na aposentadoria, anteriormente retirados pela Emenda Constitucional nº 41, de 19/12/2003.
* **D)** a Emenda Constitucional nº 70, de 29/03/2012 estabeleceu novos critérios para o cálculo da aposentadoria por invalidez se o servidor ingressou no serviço público antes da Emenda Constitucional nº 41, de 19/12/2003.
* **E)** a Emenda Constitucional nº 103, de 12/11/2019 instituiu a idade mínima para aposentadoria de 60 anos para mulheres e 65 anos para homens, tanto para o Regime Geral de Previdência Social (RGPS) quanto para o Regime Próprio de Previdência Social (RPPS).

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "apenas com a Emenda Constitucional nº 20, de 15/12/1998, a Constituição Federal de 1988 passou a adotar o...". De acordo com a teoria estudada em *2.2 Classificação Corporativa Geral de Ativos*, confidencial: Informações estratégicas, relatórios preliminares de auditoria em instrução ou dados cadastrais sob sigilo fiscal; vazamento gera dano financeiro ou institucional grave.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "a Emenda Constitucional nº 41, de 19/12/2003 criou o princípio da solidariedade contributiva, o que permitiu a...". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, grau de Sigilo: Prazo Máximo de Restrição — Competência Originária Típica para Classificar — Regime de Prorrogação.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "a Emenda Constitucional nº 47, de 05/07/2005 restabeleceu critérios condicionantes de paridade e integralidade na...". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Adulteração maliciosa de tabelas contábeis ou salariais em bancos de dados ( tampering ), infecção por malware, ataques man in the middle e erros de transmissão de rede sem checagem de paridade.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "a Emenda Constitucional nº 70, de 29/03/2012 estabeleceu novos critérios para o cálculo da aposentadoria por...". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Ataques de negação de serviço (DoS e DDoS), falhas físicas de hardware em servidores e storages, interrupção no fornecimento de energia elétrica, panes nos links de internet e desastres ambientais (enchentes, incêndios em datacenters).
> - **E)** **Correta.** Conforme fundamentado na seção *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade* deste guia, ameaças clássicas: Escuta clandestina de rede ( sniffing/eavesdropping ), roubo de dispositivos físicos, engenharia social, vazamento inadvertido de dados fiscais protegidos por sigilo e acessos não autorizados. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "a Emenda Constitucional nº 103, de 12/11/2019 instituiu a idade mínima para aposentadoria de 60 anos para mulheres...".
>
> **Gabarito: E**

---


### Teste 090
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Fiscalização - Contabilidade)**
Em 2023, uma sociedade empresária auferiu Receita com Equivalência Patrimonial de R$100.000. Em 31/12/2023, a sociedade empresária constituiu reserva de lucros a realizar, para não distribuir dividendos obrigatórios sobre a parcela de lucros ainda não realizada financeiramente. O montante será revertido quando ocorrer o primeiro entre

* **A)** alienação/baixa do investimento ou mudança do exercício social.
* **B)** aumento de participação no investimento ou recebimento dos dividendos.
* **C)** redução da participação societária no investimento ou mudança na administração da investida.
* **D)** mudança na estrutura societária do investimento ou mudança do exercício social.
* **E)** recebimento dos dividendos do investimento ou sua alienação/baixa.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "alienação/baixa do investimento ou mudança do exercício social". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Escuta clandestina de rede ( sniffing/eavesdropping ), roubo de dispositivos físicos, engenharia social, vazamento inadvertido de dados fiscais protegidos por sigilo e acessos não autorizados.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "aumento de participação no investimento ou recebimento dos dividendos". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "redução da participação societária no investimento ou mudança na administração da investida". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, aceitar / Reter ( Risk Acceptance / Retention ): Manter o risco no nível atual sem novos controles, mediante aprovação formal fundamentada da alta administração, quando o custo da salvaguarda técnica for superior à perda monetária potencial estimada.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "mudança na estrutura societária do investimento ou mudança do exercício social". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, estrutura Harmonizada (Anexo SL Cláusulas 4 a 10).
> - **E)** **Correta.** Conforme fundamentado na seção *4.1 Métricas do CVSS v3.1 (Common Vulnerability Scoring System)* deste guia, exploitability: Vetor de Ataque (AV: Rede, Adjacente, Local, Físico), Complexidade do Ataque (AC: Baixa, Alta), Privilégios Requeridos (PR: Nenhum, Baixo, Alto) e Interação do Usuário (UI: Nenhuma, Requerida). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "recebimento dos dividendos do investimento ou sua alienação/baixa".
>
> **Gabarito: E**

---


### Teste 091
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Administração)**
O Município Alfa, no Estado de Santa Catarina, publicou edital de licitação visando à celebração de vultoso contrato administrativo. As sociedades empresárias Beta, Charlie e Delta, interessadas em participar do certame público em consórcio, buscaram maiores informações sobre a temática. De acordo com a narrativa e considerando as disposições da Lei nº 14.133/2021, avalie as afirmativas a seguir. I. O edital deverá estabelecer para o consórcio acréscimo de dez por cento a trinta por cento sobre o valor exigido de licitante individual para a habilitação econômico-financeira, salvo justificação. II. O licitante vencedor é obrigado a promover, antes da celebração do contrato, a constituição e o registro do consórcio, nos termos da legislação de regência. III. É vedado a estipulação, no edital de licitação, de limite máximo para o número de empresas consorciadas. Nesse cenário, está correto o que se afirma em

* **A)** I, apenas.
* **B)** II, apenas.
* **C)** III, apenas.
* **D)** I e II, apenas.
* **E)** I, II e III.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I, apenas". De acordo com a teoria estudada em *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade*, (O que tem valor econômico ou funcional.
> - **B)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II, apenas". De acordo com a teoria estudada em *3.2 Análise Qualitativa vs. Análise Quantitativa (SLE, ARO e ALE)*, $$\text{Valor do Controle} = (\text{ALE} {\text{antes}} \text{ALE} {\text{depois}}) \text{ACS}$$.
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "III, apenas". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, ultrassecreta: 25 anos — Presidente da República, Vice Presidente, Ministros de Estado, Comandantes das Forças Armadas — Prorrogável uma única vez, por igual período (totalizando até 50 anos), exclusivamente pela CMRI ( Comissão Mista de Reavaliação de Informações ).
> - **D)** **Correta.** Conforme fundamentado na seção *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)* deste guia, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "I e II, apenas".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I, II e III". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, decore rigorosamente os prazos decrescentes: 25 anos $\rightarrow$ 15 anos $\rightarrow$ 5 anos. A FCC inventa prazos alternativos inexistentes (como 10 ou 20 anos) ou inverte Secreta e Reservada. Além disso, lembre se: informações relativas à intimidade, vida privada, honra e imagem das pessoas têm restrição de acesso máxima de até 100 anos a contar da data de sua produção (Art. 31 da LAI), não se confundindo com prazos de segurança de Estado!.
>
> **Gabarito: D**

---


### Teste 092
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Administração)**
O TCE-SC recebeu denúncias de uma entidade da sociedade civil e representações de autoridades administrativas que apontavam eventuais irregularidades na execução de um contrato firmado entre a empresa FazTudo Ltda. e um Município catarinense. Para apurar o objeto da denúncia e das representações e, ainda, para suprir omissões e lacunas nelas identificadas, a Diretoria Geral de Controle Externo do TCE-SC instaurou um instrumento de fiscalização e designou uma equipe para sua realização. Assinale a opção que identifica o instrumento de fiscalização instaurado pelo órgão de auditoria externa do TCE-SC.

* **A)** Levantamento.
* **B)** Auditoria governamental.
* **C)** Inspeção.
* **D)** Auditoria de Conformidade.
* **E)** Apuração.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Levantamento". De acordo com a teoria estudada em *2.2 Classificação Corporativa Geral de Ativos*, confidencial: Informações estratégicas, relatórios preliminares de auditoria em instrução ou dados cadastrais sob sigilo fiscal; vazamento gera dano financeiro ou institucional grave.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Auditoria governamental". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, mecanismos técnicos: Funções criptográficas de espalhamento ( hashing criptográfico como SHA 256 e SHA 512), códigos de autenticação de mensagem (HMAC), assinaturas digitais, somas de verificação ( checksums ) e trilhas de auditoria imutáveis.
> - **C)** **Correta.** Conforme fundamentado na seção *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)* deste guia, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "Inspeção".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Auditoria de Conformidade". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, reservada: 5 anos — Autoridades que exerçam funções formais de direção, comando ou chefia — Não admite prorrogação. O prazo cessa impreterivelmente aos 5 anos.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Apuração". De acordo com a teoria estudada em *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade*, (Causa potencial externa indesejada: (Fraqueza ou brecha interna explorável.
>
> **Gabarito: C**

---


### Teste 093
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Administração)**
Na era da informação, o uso responsável de redes sociais e de comunicação digital pelos servidores públicos é mandatório. Considerando as previsões expressas sobre a temática no Código de Conduta Ética dos Servidores do Tribunal de Contas do Estado de Santa Catarina (Resolução N. TC-252/2024) é correto afirmar que, ao utilizar as suas redes sociais e mídias digitais, o Auditor Fiscal de Controle Externo deve

* **A)** se abster de se identificar expressamente como servidor do Tribunal de Contas em seu perfil pessoal, o que afasta a possibilidade de penalização por eventuais manifestações fora do ambiente de trabalho.
* **B)** se abster de possuir perfis abertos ao público nas redes sociais, cautela que por si só já demonstra reserva e discrição suficientes para afastar eventuais violações de deveres funcionais.
* **C)** evitar, no seu perfil das redes sociais, pronunciamentos oficiais sobre casos decorrentes de sua atuação funcional, exceto o compartilhamento de publicações veiculadas nos perfis institucionais ou de notícias já publicadas oficialmente na página eletrônica do Tribunal de Contas.
* **D)** se abster de antecipar resultados de estudos, de projetos, de trabalhos ou de informações de caráter estratégico e funcional, antes de divulgação oficial, inclusive nos casos em que a divulgação esteja acordada com a Administração Superior, por imperativo de ética.
* **E)** evitar publicações em redes sociais que possam ser percebidas como discriminatórias em relação à raça, ao gênero, à orientação sexual, à religião e a outros valores ou direitos protegidos, e que possam comprometer os ideais defendidos pela instituição, salvo se publicadas em perfil fechado ao público e sem identificação da qualidade de servidor do TCE-SC.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "se abster de se identificar expressamente como servidor do Tribunal de Contas em seu perfil pessoal, o que afasta...". De acordo com a teoria estudada em *3. Gestão e Análise de Riscos de Segurança da Informação*, a gestão de riscos estabelece um processo contínuo e estruturado para identificar incertezas, avaliar a probabilidade de falhas e selecionar salvaguardas economicamente proporcionais.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "se abster de possuir perfis abertos ao público nas redes sociais, cautela que por si só já demonstra reserva e...". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, governo Digital Programa de Privacidade e Segurança da Informação (PPSI 2.0) Diretrizes, requisitos de maturidade e gestão de riscos cibernéticos para a administração pública.
> - **C)** **Correta.** Conforme fundamentado na seção *🌐 Fontes Oficiais e Referências Bibliográficas* deste guia, sTALLINGS, William. Criptografia e Segurança de Redes: Princípios e Práticas. 7. ed. São Paulo: Pearson Education do Brasil, 2018. (Cap. 1 Visão Geral de Segurança da Informação). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "evitar, no seu perfil das redes sociais, pronunciamentos oficiais sobre casos decorrentes de sua atuação...".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "se abster de antecipar resultados de estudos, de projetos, de trabalhos ou de informações de caráter estratégico e...". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, aceitar / Reter ( Risk Acceptance / Retention ): Manter o risco no nível atual sem novos controles, mediante aprovação formal fundamentada da alta administração, quando o custo da salvaguarda técnica for superior à perda monetária potencial estimada.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "evitar publicações em redes sociais que possam ser percebidas como discriminatórias em relação à raça, ao gênero...". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, nIST Cybersecurity Framework (CSF 2.0) Estrutura de referência global do NIST para identificação, proteção, detecção, resposta e recuperação de riscos cibernéticos.
>
> **Gabarito: C**

---


### Teste 094
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Administração)**
Uma Secretaria Estadual de Educação iniciou um processo de planejamento estratégico. Na primeira reunião, a equipe responsável elaborou uma declaração descrevendo a razão de existir do órgão e o papel que ele desempenha perante a sociedade. Em seguida, definiu um conjunto de princípios éticos e comportamentais que deveriam orientar todas as decisões e ações dos servidores. Por fim, projetou uma situação futura desejada, indicando onde o órgão pretende chegar em um horizonte de dez anos. Conforme a literatura de planejamento estratégico aplicado às organizações públicas, os três elementos elaborados correspondem, respectivamente, a:

* **A)** visão, missão e valores.
* **B)** missão, visão e valores.
* **C)** valores, missão e visão.
* **D)** missão, valores e visão.
* **E)** visão, valores e missão.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "visão, missão e valores". De acordo com a teoria estudada em *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade*, ativo ( Asset ): Qualquer recurso humano, físico, tecnológico ou de informação que possui valor intrínseco para o cumprimento da missão da instituição.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "missão, visão e valores". De acordo com a teoria estudada em *3.2 Análise Qualitativa vs. Análise Quantitativa (SLE, ARO e ALE)*, mensura as perdas e investimentos em valores monetários concretos (R$).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "valores, missão e visão". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes.
> - **D)** **Correta.** Conforme fundamentado na seção *🌐 Fontes Oficiais e Referências Bibliográficas* deste guia, sTALLINGS, William. Criptografia e Segurança de Redes: Princípios e Práticas. 7. ed. São Paulo: Pearson Education do Brasil, 2018. (Cap. 1 Visão Geral de Segurança da Informação). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "missão, valores e visão".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "visão, valores e missão". De acordo com a teoria estudada em *5.3 A Declaração de Aplicabilidade (SoA) e a ISO/IEC 27005*, iSO/IEC 27005: Norma que fornece diretrizes especializadas para o processo de avaliação e tratamento de riscos de segurança da informação no suporte ao SGSI.
>
> **Gabarito: D**

---


### Teste 095
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Administração)**
O Tribunal de Contas da União (TCU), por meio do Referencial Básico de Governança Aplicável a Organizações Públicas (2020), consolidou um conjunto de conceitos e diretrizes sobre governança pública que orienta a atuação dos órgãos e entidades da Administração Pública brasileira. Com base no referencial do TCU sobre governança pública, assinale a afirmativa correta.

* **A)** Segundo o TCU, governança pública e gestão pública são conceitos equivalentes, pois ambos dizem respeito à execução das atividades finalísticas das organizações públicas com vistas ao atingimento de resultados.
* **B)** O referencial do TCU define governança pública como o conjunto de mecanismos de liderança, estratégia e controle postos em prática para avaliar, direcionar e monitorar a atuação da gestão, com vistas à condução de políticas públicas e à prestação de serviços de interesse da sociedade.
* **C)** Para o TCU, a governança pública tem como objetivo principal garantir a eficiência operacional dos processos internos das organizações, sendo sua aplicação restrita aos órgãos da Administração direta federal.
* **D)** O referencial do TCU estabelece que os mecanismos de governança compreendem exclusivamente as estruturas de controle interno, não abrangendo aspectos de liderança e definição estratégica das organizações públicas.
* **E)** Conforme o TCU, a boa governança pública dispensa a participação de partes interessadas externas à organização, pois a legitimidade das decisões decorre exclusivamente da competência técnica dos gestores públicos responsáveis pela condução institucional.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Segundo o TCU, governança pública e gestão pública são conceitos equivalentes, pois ambos dizem respeito à...". De acordo com a teoria estudada em *3. Gestão e Análise de Riscos de Segurança da Informação*, a gestão de riscos estabelece um processo contínuo e estruturado para identificar incertezas, avaliar a probabilidade de falhas e selecionar salvaguardas economicamente proporcionais.
> - **B)** **Correta.** Conforme fundamentado na seção *🌐 Fontes Oficiais e Referências Bibliográficas* deste guia, decreto Federal nº 9.637/2018 (Política Nacional de Segurança da Informação) Institui a PNSI, dispondo sobre governança, gestão de riscos e tratamento de incidentes de segurança da informação. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "O referencial do TCU define governança pública como o conjunto de mecanismos de liderança, estratégia e controle...".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Para o TCU, a governança pública tem como objetivo principal garantir a eficiência operacional dos processos...". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, nIST SP 800 30 Rev. 1 Guide for Conducting Risk Assessments Guia metodológico oficial para condução de processos de avaliação e gestão de riscos em segurança da informação.
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "O referencial do TCU estabelece que os mecanismos de governança compreendem exclusivamente as estruturas de...". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, a norma ABNT NBR ISO/IEC 27001 estabelece os requisitos formais para estabelecer, implementar, manter e melhorar continuamente um Sistema de Gestão de Segurança da Informação (SGSI).
> - **E)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "Conforme o TCU, a boa governança pública dispensa a participação de partes interessadas externas à organização...". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, cláusula 4: Contexto da Organização (partes interessadas e escopo do SGSI).
>
> **Gabarito: B**

---


### Teste 096
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Administração)**
A Lei Complementar nº 214/2025 regulamentou a reforma tributária aprovada pela Emenda Constitucional nº 132/2023, instituindo o Imposto sobre Bens e Serviços (IBS), a Contribuição Social sobre Bens e Serviços (CBS) e o Imposto Seletivo (IS), que substituirão progressivamente tributos atualmente vigentes. Com base na estrutura e nos objetivos da reforma tributária regulamentada pela Lei Complementar nº 214/2025, assinale a afirmativa correta.

* **A)** O IBS substituirá tributos federais, estaduais e municipais, sendo administrado exclusivamente pela Receita Federal do Brasil, a quem caberá a arrecadação e a distribuição das receitas aos entes subnacionais.
* **B)** A CBS é de competência da União e substituirá o PIS e a Cofins, ao passo que o IBS é de competência compartilhada entre Estados, Distrito Federal e Municípios, substituindo o ICMS e o ISS, sendo ambos administrados pelo Comitê Gestor do IBS.
* **C)** O IS tem como fato gerador a circulação de bens e a prestação de serviços em geral, incidindo de forma ampla sobre toda a cadeia produtiva com o objetivo de simplificar a arrecadação e eliminar a cumulatividade tributária.
* **D)** A reforma tributária instituída pela LC nº 214/2025 terá implementação imediata, com a extinção do ICMS, do ISS, do PIS, da Cofins e do IPI a partir do exercício financeiro seguinte à sua publicação, sem período de transição.
* **E)** O IBS e a CBS formam a chamada Contribuição sobre Bens e Serviços dual, mas incidem sobre bases de cálculo distintas: o IBS incide exclusivamente sobre bens, e a CBS incide exclusivamente sobre serviços, mantendo a separação tradicional entre o ICMS e o ISS.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "O IBS substituirá tributos federais, estaduais e municipais, sendo administrado exclusivamente pela Receita...". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, ultrassecreta: 25 anos — Presidente da República, Vice Presidente, Ministros de Estado, Comandantes das Forças Armadas — Prorrogável uma única vez, por igual período (totalizando até 50 anos), exclusivamente pela CMRI ( Comissão Mista de Reavaliação de Informações ).
> - **B)** **Correta.** Conforme fundamentado na seção *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)* deste guia, grau de Sigilo: Prazo Máximo de Restrição — Competência Originária Típica para Classificar — Regime de Prorrogação. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "A CBS é de competência da União e substituirá o PIS e a Cofins, ao passo que o IBS é de competência compartilhada...".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O IS tem como fato gerador a circulação de bens e a prestação de serviços em geral, incidindo de forma ampla sobre...". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, evitar / Eliminar ( Risk Avoidance ): Descontinuar a atividade, processo ou serviço gerador do risco (ex.: desligar e desativar em definitivo um sistema legado vulnerável sem suporte do fabricante).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A reforma tributária instituída pela LC nº 214/2025 terá implementação imediata, com a extinção do ICMS, do ISS...". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, uLTRASSECRETA ──► Prazo Máximo: 25 ANOS (Prorrogável 1 única vez por igual período).
> - **E)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "O IBS e a CBS formam a chamada Contribuição sobre Bens e Serviços dual, mas incidem sobre bases de cálculo...". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, garantia de que o acesso à informação é restrito estrita e exclusivamente a pessoas, entidades ou processos formalmente autorizados.
>
> **Gabarito: B**

---


### Teste 097
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Ciências Atuariais)**
Suponha um plano de previdência complementar fechada dos servidores públicos de um determinado Estado da Federação, estruturado na modalidade de contribuição definida, com os números (R$ milhares) apresentados na tabela a seguir. ATIVO 420.050 Exigível Operacional 1.500 Exigível Contingencial 500 PATRIMÔNIO SOCIAL 418.050 Fundo Previdencial 14.000 Fundo Administrativo 4.000 ATIVO REAL LÍQUIDO (PATRIMÔNIO DE COBERTURA) 400.050 PROVISÕES ATUARIAIS 400.050 Provisão Matemática de Benefícios a Conceder 385.000 Provisão Matemática de Benefícios Concedidos 15.050 O resultado atuarial do plano (superávit ou déficit) é

* **A)** nulo (equilíbrio atuarial).
* **B)** superávit de 2.000.
* **C)** superávit de 14.000.
* **D)** superávit de 18.000.
* **E)** superávit de 20.000.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "nulo (equilíbrio atuarial)". De acordo com a teoria estudada em *2.2 Classificação Corporativa Geral de Ativos*, pública: Informação destinada à divulgação irrestrita (editais de licitação, acórdãos públicos, portal da transparência); o vazamento gera dano nulo.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "superávit de 2.000". De acordo com a teoria estudada em *1. Princípios Básicos da Segurança da Informação (CIDAN)*, a segurança da informação é definida pela norma ABNT NBR ISO/IEC 27000 como a preservação da confidencialidade, integridade e disponibilidade da informação, admitindo se adicionalmente propriedades vitais para transações formais como a autenticidade e o não repúdio. O mnemônico padronizado em concursos da FCC é CIDAN.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "superávit de 14.000". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Escuta clandestina de rede ( sniffing/eavesdropping ), roubo de dispositivos físicos, engenharia social, vazamento inadvertido de dados fiscais protegidos por sigilo e acessos não autorizados.
> - **D)** **Correta.** Conforme fundamentado na seção *2.2 Classificação Corporativa Geral de Ativos* deste guia, interna: Informação para circulação interna restrita aos servidores e colaboradores; divulgação indevida acarreta transtorno administrativo leve. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "superávit de 18.000".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "superávit de 20.000". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Ataques de negação de serviço (DoS e DDoS), falhas físicas de hardware em servidores e storages, interrupção no fornecimento de energia elétrica, panes nos links de internet e desastres ambientais (enchentes, incêndios em datacenters).
>
> **Gabarito: D**

---


### Teste 098
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Ciências Atuariais)**
De acordo com a Portaria MTP nº 1.467/2022, assinale a situação a seguir em que a exigência do Certificado de Regularidade Previdenciária (CRP) é dispensada, constituindo uma exceção às regras gerais de comprovação.

* **A)** Celebração de contratos e convênios com a Administração direta e indireta da União.
* **B)** Liberação de empréstimos e financiamentos por instituições financeiras federais.
* **C)** Realização de transferências relativas a ações de educação, saúde e assistência social.
* **D)** Realização de transferências voluntárias de recursos pela União.
* **E)** Repasse de compensação financeira previdenciária.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Celebração de contratos e convênios com a Administração direta e indireta da União". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, decore rigorosamente os prazos decrescentes: 25 anos $\rightarrow$ 15 anos $\rightarrow$ 5 anos. A FCC inventa prazos alternativos inexistentes (como 10 ou 20 anos) ou inverte Secreta e Reservada. Além disso, lembre se: informações relativas à intimidade, vida privada, honra e imagem das pessoas têm restrição de acesso máxima de até 100 anos a contar da data de sua produção (Art. 31 da LAI), não se confundindo com prazos de segurança de Estado!.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Liberação de empréstimos e financiamentos por instituições financeiras federais". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, cláusula 10: Melhoria (Não conformidades, ações corretivas e ciclo contínuo).
> - **C)** **Correta.** Conforme fundamentado na seção *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade* deste guia, ameaças clássicas: Escuta clandestina de rede ( sniffing/eavesdropping ), roubo de dispositivos físicos, engenharia social, vazamento inadvertido de dados fiscais protegidos por sigilo e acessos não autorizados. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "Realização de transferências relativas a ações de educação, saúde e assistência social".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Realização de transferências voluntárias de recursos pela União". De acordo com a teoria estudada em *4.1 Métricas do CVSS v3.1 (Common Vulnerability Scoring System)*, scope (S): Escopo Inalterado ( Unchanged ) ou Alterado ( Changed , quando a falha compromete recursos fora de sua camada de autorização).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Repasse de compensação financeira previdenciária". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, transferir / Compartilhar ( Risk Transfer / Sharing ): Compartilhar a carga financeira ou operacional das perdas com terceiros (ex.: contratação de apólice de seguro contra incidentes cibernéticos ou terceirização da infraestrutura de datacenter para provedores de nuvem sob contratos de SLA estritos).
>
> **Gabarito: C**

---


### Teste 099
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Ciências Atuariais)**
A Resolução CMN nº 5.272/2025 consolidou o modelo de investimentos dos Regimes Próprios de Previdência Social (RPPS) baseado na maturidade da gestão, estabelecendo que o acesso a ativos de maior complexidade e risco é condicionado ao melhor nível de certificação institucional Pró-Gestão, baseada nos pilares de controle interno, governança corporativa e educação previdenciária. Diante desse novo regramento, a seguinte modalidade de investimento é vedada aos RPPS que não possuem nível máximo de governança com a certificação nível IV:

* **A)** cotas de fundos de investimento em participações (FIP), de “private equity” constituídas em regime fechado e qualificadas como entidade de investimento.
* **B)** cotas de fundos de investimento imobiliário (FII).
* **C)** cotas de Fundos de Investimento nas Cadeias Produtivas Agroindustriais (FIAGRO).
* **D)** cotas de Fundos de Investimento no Exterior (FIEX), com exposição a ativos estruturados e estratégias de gestão ativa sem proteção cambial (hedge).
* **E)** cotas de fundos de investimento tipificadas como multimercado (FM), constituídas em regime aberto.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "cotas de fundos de investimento em participações (FIP), de “private equity” constituídas em regime fechado e...". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, grau de Sigilo: Prazo Máximo de Restrição — Competência Originária Típica para Classificar — Regime de Prorrogação.
> - **B)** **Correta.** Conforme fundamentado na seção *2.2 Classificação Corporativa Geral de Ativos* deste guia, restrita / Secreta: Nível máximo corporativo (chaves criptográficas mestras de certificados de segurança, senhas de administradores de domínios centrais); divulgação gera dano catastrófico e imediato. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "cotas de fundos de investimento imobiliário (FII)".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "cotas de Fundos de Investimento nas Cadeias Produtivas Agroindustriais (FIAGRO)". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, mecanismos técnicos: Criptografia em trânsito (TLS) e em repouso (TDE), controle de acesso lógico baseado em papéis (RBAC), mascaramento dinâmico de dados e soluções de Prevenção contra Perda de Dados ( DLP Data Loss Prevention ).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "cotas de Fundos de Investimento no Exterior (FIEX), com exposição a ativos estruturados e estratégias de gestão...". De acordo com a teoria estudada em *5.2 A Nova ISO/IEC 27002 (Edição 2022: 4 Temas e 93 Controles)*, cONTROLES ORGANIZACIONAIS (37 controles) ──► Políticas, gestão de ativos,.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "cotas de fundos de investimento tipificadas como multimercado (FM), constituídas em regime aberto". De acordo com a teoria estudada em *2.2 Classificação Corporativa Geral de Ativos*, confidencial: Informações estratégicas, relatórios preliminares de auditoria em instrução ou dados cadastrais sob sigilo fiscal; vazamento gera dano financeiro ou institucional grave.
>
> **Gabarito: B**

---


### Teste 100
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Ciências Contábeis)**
Na era da informação, o uso responsável de redes sociais e de comunicação digital pelos servidores públicos é mandatória. Considerando as previsões expressas sobre a temática no Código de Conduta Ética dos Servidores do Tribunal de Contas do Estado de Santa Catarina (Resolução N. TC-252/2024) é correto afirmar que, ao utilizar as suas redes sociais e mídias digitais, o Auditor Fiscal de Controle Externo deve

* **A)** se abster de se identificar expressamente como servidor do Tribunal de Contas em seu perfil pessoal, o que afasta a possibilidade de penalização por eventuais manifestações fora do ambiente de trabalho.
* **B)** se abster de possuir perfis abertos ao público nas redes sociais, cautela que por si só já demonstra reserva e discrição suficientes para afastar eventuais violações de deveres funcionais.
* **C)** evitar, no seu perfil das redes sociais, pronunciamentos oficiais sobre casos decorrentes de sua atuação funcional, exceto o compartilhamento de publicações veiculadas nos perfis institucionais ou de notícias já publicadas oficialmente na página eletrônica do Tribunal de Contas.
* **D)** se abster de antecipar resultados de estudos, de projetos, de trabalhos ou de informações de caráter estratégico e funcional, antes de divulgação oficial, inclusive nos casos em que a divulgação esteja acordada com a Administração Superior, por imperativo de ética.
* **E)** evitar publicações em redes sociais que possam ser percebidas como discriminatórias em relação à raça, ao gênero, à orientação sexual, à religião e a outros valores ou direitos protegidos, e que possam comprometer os ideais defendidos pela instituição, salvo se publicadas em perfil fechado ao público e sem identificação da qualidade de servidor do TCE-SC.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "se abster de se identificar expressamente como servidor do Tribunal de Contas em seu perfil pessoal, o que afasta...". De acordo com a teoria estudada em *3. Gestão e Análise de Riscos de Segurança da Informação*, a gestão de riscos estabelece um processo contínuo e estruturado para identificar incertezas, avaliar a probabilidade de falhas e selecionar salvaguardas economicamente proporcionais.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "se abster de possuir perfis abertos ao público nas redes sociais, cautela que por si só já demonstra reserva e...". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, governo Digital Programa de Privacidade e Segurança da Informação (PPSI 2.0) Diretrizes, requisitos de maturidade e gestão de riscos cibernéticos para a administração pública.
> - **C)** **Correta.** Conforme fundamentado na seção *🌐 Fontes Oficiais e Referências Bibliográficas* deste guia, sTALLINGS, William. Criptografia e Segurança de Redes: Princípios e Práticas. 7. ed. São Paulo: Pearson Education do Brasil, 2018. (Cap. 1 Visão Geral de Segurança da Informação). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "evitar, no seu perfil das redes sociais, pronunciamentos oficiais sobre casos decorrentes de sua atuação...".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "se abster de antecipar resultados de estudos, de projetos, de trabalhos ou de informações de caráter estratégico e...". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, aceitar / Reter ( Risk Acceptance / Retention ): Manter o risco no nível atual sem novos controles, mediante aprovação formal fundamentada da alta administração, quando o custo da salvaguarda técnica for superior à perda monetária potencial estimada.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "evitar publicações em redes sociais que possam ser percebidas como discriminatórias em relação à raça, ao gênero...". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, nIST Cybersecurity Framework (CSF 2.0) Estrutura de referência global do NIST para identificação, proteção, detecção, resposta e recuperação de riscos cibernéticos.
>
> **Gabarito: C**

---


### Teste 101
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Ciências Contábeis)**
Um escritório de Contabilidade presta os seus serviços em imóvel alugado. O contrato de aluguel tem duração até 31/12/2030. Em 01/07/2025, o escritório adquiriu móveis planejados por R$ 11.000,00. O frete para a entrega foi de R$ 500,00 e a montagem dos móveis custou R$ 1.700,00. Os custos estimados para desmontagem e remoção eram estimados em R$ 1.980,00. No entanto, o sócio do escritório combinou com o proprietário do imóvel que usaria os móveis até o final do contrato e os venderia a ele por R$ 2.640,00, de modo a mantê-los no imóvel. Em 31/12/2025, o valor contábil dos móveis era de

* **A)** R$ 10.000,00.
* **B)** R$ 12.000,00.
* **C)** R$ 12.240,00.
* **D)** R$ 13.800,00.
* **E)** R$ 14.040,00.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "R$ 10.000,00". De acordo com a teoria estudada em *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade*, ativo ( Asset ): Qualquer recurso humano, físico, tecnológico ou de informação que possui valor intrínseco para o cumprimento da missão da instituição.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "R$ 12.000,00". De acordo com a teoria estudada em *3.2 Análise Qualitativa vs. Análise Quantitativa (SLE, ARO e ALE)*, onde $\text{AV}$ ( Asset Value ) é o valor financeiro do ativo e $\text{EF}$ ( Exposure Factor ) é a fração percentual do valor do ativo perdida em um único incidente (0% a 100%).
> - **C)** **Correta.** Conforme fundamentado na seção *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade* deste guia, (O que tem valor econômico ou funcional. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "R$ 12.240,00".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "R$ 13.800,00". De acordo com a teoria estudada em *4.2 As Quatro Fases do Ciclo de Resposta a Incidentes (NIST SP 800-61)*, o tratamento de incidentes cibernéticos adota o ciclo formalizado no guia NIST SP 800 61 Rev. 2.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "R$ 14.040,00". De acordo com a teoria estudada em *3.2 Análise Qualitativa vs. Análise Quantitativa (SLE, ARO e ALE)*, $$\text{Valor do Controle} = (\text{ALE} {\text{antes}} \text{ALE} {\text{depois}}) \text{ACS}$$.
>
> **Gabarito: C**

---


### Teste 102
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Ciências Contábeis)**
Em 30/11/2025, uma entidade apresentava os seguintes saldos em seu Balanço Patrimonial: • Disponibilidades: R$ 90.000,00; • Terrenos destinados ao uso: R$ 210.000,00; • Patrimônio Líquido: R$ 300.000,00. A entidade possuía 3 terrenos, sendo cada um avaliado por R$ 70.000,00. Em dezembro de 2025, a entidade decidiu concentrar as suas atividades em apenas um terreno. Desse modo, colocou os outros dois terrenos à venda, por R$ 72.000,00 cada. O nível hierárquico de gestão apropriado estava comprometido com o plano de venda dos terrenos, e iniciou um programa firme para localizar um comprador e concluir o plano assim que os terrenos estiverem desocupados, em fevereiro de 2027. A imobilização do patrimônio líquido da entidade, em 31/12/2025, foi de

* **A)** 23,33%.
* **B)** 24,00%.
* **C)** 70,00%.
* **D)** 71,33%.
* **E)** 72,00%.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "23,33%". De acordo com a teoria estudada em *2.2 Classificação Corporativa Geral de Ativos*, restrita / Secreta: Nível máximo corporativo (chaves criptográficas mestras de certificados de segurança, senhas de administradores de domínios centrais); divulgação gera dano catastrófico e imediato.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "24,00%". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, aceitar / Reter ( Risk Acceptance / Retention ): Manter o risco no nível atual sem novos controles, mediante aprovação formal fundamentada da alta administração, quando o custo da salvaguarda técnica for superior à perda monetária potencial estimada.
> - **C)** **Correta.** Conforme fundamentado na seção *🌐 Fontes Oficiais e Referências Bibliográficas* deste guia, governo Digital Programa de Privacidade e Segurança da Informação (PPSI 2.0) Diretrizes, requisitos de maturidade e gestão de riscos cibernéticos para a administração pública. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "70,00%".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "71,33%". De acordo com a teoria estudada em *4.2 As Quatro Fases do Ciclo de Resposta a Incidentes (NIST SP 800-61)*, [4. ATIVIDADES PÓS INCIDENTE] ──► Reunião de Lições Aprendidas e melhorias.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "72,00%". De acordo com a teoria estudada em *4.2 As Quatro Fases do Ciclo de Resposta a Incidentes (NIST SP 800-61)*, atividades Pós Incidente ( Post Incident Activity / Lessons Learned ): Reunião formal de Lições Aprendidas para documentar como o incidente foi tratado, registrar métricas temporais e aprimorar as salvaguardas da fase de preparação.
>
> **Gabarito: C**

---


### Teste 103
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Direito)**
Segundo a atual redação da Constituição Federal de 1988 (CF/1988), da parcela de arrecadação do Imposto sobre Bens e Serviços (IBS) que caberá aos Estados, 25% pertencem aos Municípios, a serem creditados a cada um deles de forma diferenciada, com base nos seguintes critérios: 1. indicadores de melhoria nos resultados de aprendizagem e de aumento da equidade, considerado o nível socioeconômico dos educandos, de acordo com o que dispuser lei estadual; 2. indicadores de preservação ambiental, de acordo com o que dispuser lei estadual; 3. proporção da população. Cada um desses critérios acima apresenta pesos distintos na fixação da parcela que pertence a cada Município. Diante disso, na determinação da repartição de tais receitas tributárias, a sequência indicadora do critério de maior peso para o de menor peso é

* **A)** 1 – 2 – 3.
* **B)** 1 – 3 – 2.
* **C)** 2 – 1 – 3.
* **D)** 3 – 1 – 2.
* **E)** 3 – 2 – 1.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *2. Classificação e Rotulagem da Informação* deste guia, a classificação atribui rótulos de sensibilidade aos ativos de informação da organização, ditando os níveis de proteção lógica e física a serem aplicados de forma proporcional ao dano decorrente de divulgação ou modificação indevida. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "1 – 2 – 3".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "1 – 3 – 2". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, aceitar / Reter ( Risk Acceptance / Retention ): Manter o risco no nível atual sem novos controles, mediante aprovação formal fundamentada da alta administração, quando o custo da salvaguarda técnica for superior à perda monetária potencial estimada.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "2 – 1 – 3". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, decore rigorosamente os prazos decrescentes: 25 anos $\rightarrow$ 15 anos $\rightarrow$ 5 anos. A FCC inventa prazos alternativos inexistentes (como 10 ou 20 anos) ou inverte Secreta e Reservada. Além disso, lembre se: informações relativas à intimidade, vida privada, honra e imagem das pessoas têm restrição de acesso máxima de até 100 anos a contar da data de sua produção (Art. 31 da LAI), não se confundindo com prazos de segurança de Estado!.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "3 – 1 – 2". De acordo com a teoria estudada em *1. Princípios Básicos da Segurança da Informação (CIDAN)*, a segurança da informação é definida pela norma ABNT NBR ISO/IEC 27000 como a preservação da confidencialidade, integridade e disponibilidade da informação, admitindo se adicionalmente propriedades vitais para transações formais como a autenticidade e o não repúdio. O mnemônico padronizado em concursos da FCC é CIDAN.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "3 – 2 – 1". De acordo com a teoria estudada em *4.1 Métricas do CVSS v3.1 (Common Vulnerability Scoring System)*, métricas de Base ( Base Metrics ): Qualidades intrínsecas e imutáveis da falha.
>
> **Gabarito: A**

---


### Teste 104
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Direito)**
A sociedade empresária Transporta 100% Ltda., com sede no Município Alfa, no ano de 2026, prestou serviço de transporte de 20 toneladas de feijão do Município Beta para o Município Gama. A mercadoria foi entregue sem avarias e integralmente ao destinatário constante no documento fiscal no Município Gama, a saber, a sociedade empresária Recebe 100% Ltda., que tem sua sede no Município Delta. Todos os quatro municípios se situam no mesmo estado da federação. Considerando as regras da Lei Complementar (LC) nº 214/2025 acerca do Imposto sobre Bens e Serviços (IBS), assinale a opção que indica corretamente o local onde se considera realizada essa operação de serviço de transporte de carga para efeitos de IBS:

* **A)** Município Alfa, por ser o local da sede de Transporta 100% Ltda.
* **B)** Município Beta, por ser o local de início do transporte.
* **C)** Município Gama, por ser o local da entrega do bem ao destinatário constante no documento fiscal.
* **D)** Município Delta, por ser o local da sede de Recebe 100% Ltda.
* **E)** Qualquer um dos quatro municípios, deixando a LC nº 214/2025 à escolha do sujeito passivo tributário.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Município Alfa, por ser o local da sede de Transporta 100% Ltda". De acordo com a teoria estudada em *3.2 Análise Qualitativa vs. Análise Quantitativa (SLE, ARO e ALE)*, onde $\text{AV}$ ( Asset Value ) é o valor financeiro do ativo e $\text{EF}$ ( Exposure Factor ) é a fração percentual do valor do ativo perdida em um único incidente (0% a 100%).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Município Beta, por ser o local de início do transporte". De acordo com a teoria estudada em *4.1 Métricas do CVSS v3.1 (Common Vulnerability Scoring System)*, exploitability: Vetor de Ataque (AV: Rede, Adjacente, Local, Físico), Complexidade do Ataque (AC: Baixa, Alta), Privilégios Requeridos (PR: Nenhum, Baixo, Alto) e Interação do Usuário (UI: Nenhuma, Requerida).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Município Gama, por ser o local da entrega do bem ao destinatário constante no documento fiscal". De acordo com a teoria estudada em *2.2 Classificação Corporativa Geral de Ativos*, confidencial: Informações estratégicas, relatórios preliminares de auditoria em instrução ou dados cadastrais sob sigilo fiscal; vazamento gera dano financeiro ou institucional grave.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Município Delta, por ser o local da sede de Recebe 100% Ltda". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, decore rigorosamente os prazos decrescentes: 25 anos $\rightarrow$ 15 anos $\rightarrow$ 5 anos. A FCC inventa prazos alternativos inexistentes (como 10 ou 20 anos) ou inverte Secreta e Reservada. Além disso, lembre se: informações relativas à intimidade, vida privada, honra e imagem das pessoas têm restrição de acesso máxima de até 100 anos a contar da data de sua produção (Art. 31 da LAI), não se confundindo com prazos de segurança de Estado!.
> - **E)** **Correta.** Conforme fundamentado na seção *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade* deste guia, mecanismos técnicos: Redundância de hardware e fontes de alimentação, clusters de alta disponibilidade (HA ativo ativo ou ativo passivo), sistemas anti DDoS, geradores e nobreaks comutáveis, planos de continuidade de negócios (PCN/DRP) e rotinas estruturadas de backup. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "Qualquer um dos quatro municípios, deixando a LC nº 214/2025 à escolha do sujeito passivo tributário".
>
> **Gabarito: E**

---


### Teste 105
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Direito)**
Maria Antônia, advogada privada em atividade autônoma no Estado de Santa Catarina, desempenha suas funções em favor de seus clientes, mediante remuneração contratualmente prevista, não possuindo qualquer outro vínculo laboral ou profissional. Diante da situação hipotética narrada, é correto afirmar que Maria é filiada, obrigatoriamente, ao

* **A)** Regime Geral de Previdência Social, na qualidade de segurada obrigatória.
* **B)** Regime Geral de Previdência Social, na qualidade de segurada facultativa.
* **C)** Regime Próprio de Previdência do Estado de Santa Catarina.
* **D)** Regime Próprio de Previdência da União Federal.
* **E)** Regime Complementar de Previdência Complementar instituído pela OAB local.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Regime Geral de Previdência Social, na qualidade de segurada obrigatória". De acordo com a teoria estudada em *5.3 A Declaração de Aplicabilidade (SoA) e a ISO/IEC 27005*, a justificativa formal obrigatória para a exclusão de qualquer controle que não tenha sido adotado.
> - **B)** **Incorreta.** A opção afasta requisito ou relação estrutural exigida pela matéria ao afirmar que "Regime Geral de Previdência Social, na qualidade de segurada facultativa". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Escuta clandestina de rede ( sniffing/eavesdropping ), roubo de dispositivos físicos, engenharia social, vazamento inadvertido de dados fiscais protegidos por sigilo e acessos não autorizados.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Regime Próprio de Previdência do Estado de Santa Catarina". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, mecanismos técnicos: Funções criptográficas de espalhamento ( hashing criptográfico como SHA 256 e SHA 512), códigos de autenticação de mensagem (HMAC), assinaturas digitais, somas de verificação ( checksums ) e trilhas de auditoria imutáveis.
> - **D)** **Correta.** Conforme fundamentado na seção *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)* deste guia, grau de Sigilo: Prazo Máximo de Restrição — Competência Originária Típica para Classificar — Regime de Prorrogação. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "Regime Próprio de Previdência da União Federal".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Regime Complementar de Previdência Complementar instituído pela OAB local". De acordo com a teoria estudada em *4.1 Métricas do CVSS v3.1 (Common Vulnerability Scoring System)*, exploitability: Vetor de Ataque (AV: Rede, Adjacente, Local, Físico), Complexidade do Ataque (AC: Baixa, Alta), Privilégios Requeridos (PR: Nenhum, Baixo, Alto) e Interação do Usuário (UI: Nenhuma, Requerida).
>
> **Gabarito: D**

---


### Teste 106
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Direito)**
Jorge Ferraz, servidor público do Estado de Santa Catarina, dotado de cargo público de provimento efetivo, é regulamente filiado ao Regime de Previdência Estadual, vertendo suas contribuições normalmente. Jorge, todavia, decide realizar contribuição adicional ao Regime Geral de Previdência Social (RGPS), de forma a acumular aposentadorias de ambos os regimes. Diante da situação hipotética, é correto afirmar que a estratégia de Jorge é

* **A)** válida, desde que requeira inscrição previdenciária no RGPS como facultativo.
* **B)** inválida, pois não é possível a acumulação de aposentadorias após a EC nº 103/19.
* **C)** válida, desde que Jorge tenha outra atividade remunerada lícita que o vincule ao RGPS.
* **D)** inválida, pois a CF/88 impede a vinculação simultânea a dois ou mais regimes previdenciários.
* **E)** válida, desde que Jorge venha a aderir, também, ao regime de previdência complementar estadual. Realização

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção afasta requisito ou relação estrutural exigida pela matéria ao afirmar que "válida, desde que requeira inscrição previdenciária no RGPS como facultativo". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Escuta clandestina de rede ( sniffing/eavesdropping ), roubo de dispositivos físicos, engenharia social, vazamento inadvertido de dados fiscais protegidos por sigilo e acessos não autorizados.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "inválida, pois não é possível a acumulação de aposentadorias após a EC nº 103/19". De acordo com a teoria estudada em *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade*, risco Residual: Risco que subsiste e permanece após o projeto e a entrada em operação dos controles de segurança mitigadores. Deve situar se estritamente abaixo do Apetite ao Risco fixado pela diretoria do tribunal.
> - **C)** **Correta.** Conforme fundamentado na seção *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)* deste guia, evitar / Eliminar ( Risk Avoidance ): Descontinuar a atividade, processo ou serviço gerador do risco (ex.: desligar e desativar em definitivo um sistema legado vulnerável sem suporte do fabricante). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "válida, desde que Jorge tenha outra atividade remunerada lícita que o vincule ao RGPS".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "inválida, pois a CF/88 impede a vinculação simultânea a dois ou mais regimes previdenciários". De acordo com a teoria estudada em *2. Classificação e Rotulagem da Informação*, a classificação atribui rótulos de sensibilidade aos ativos de informação da organização, ditando os níveis de proteção lógica e física a serem aplicados de forma proporcional ao dano decorrente de divulgação ou modificação indevida.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "válida, desde que Jorge venha a aderir, também, ao regime de previdência complementar estadual. Realização". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, grau de Sigilo: Prazo Máximo de Restrição — Competência Originária Típica para Classificar — Regime de Prorrogação.
>
> **Gabarito: C**

---


### Teste 107
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Economia)**
Com base no Manual Técnico do Orçamento (MTO), avalie se as afirmativas a seguir sobre a classificação das receitas e despesas públicas são verdadeiras (V) ou falsas (F). ( ) A classificação da receita por natureza busca identificar a origem do recurso segundo seu fato gerador, ao passo que a fonte/destinação de recursos procura identificar a aplicação dos recursos arrecadados. ( ) Na classificação da despesa por natureza, o 1º dígito corresponde à categoria econômica, o 2º ao grupo de natureza da despesa, o 3º e o 4º à modalidade de aplicação, o 5º e o 6º ao elemento de despesa, e o 7º e o 8º ao subelemento. ( ) As receitas intraorçamentárias são ingressos oriundos de operações entre órgãos, fundos e entidades integrantes dos orçamentos fiscal e da seguridade social; por isso, sua contrapartida se relaciona à modalidade de aplicação 91, e sua identificação ajuda a evitar dupla contagem na consolidação das contas públicas. As afirmativas são, respectivamente,

* **A)** V – V – V.
* **B)** V – V – F.
* **C)** V – F – V.
* **D)** F – V – V.
* **E)** F – F – F.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "V – V – V". De acordo com a teoria estudada em *2.2 Classificação Corporativa Geral de Ativos*, confidencial: Informações estratégicas, relatórios preliminares de auditoria em instrução ou dados cadastrais sob sigilo fiscal; vazamento gera dano financeiro ou institucional grave.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "V – V – F". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, garantia de que o acesso à informação é restrito estrita e exclusivamente a pessoas, entidades ou processos formalmente autorizados.
> - **C)** **Correta.** Conforme fundamentado na seção *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)* deste guia, evitar / Eliminar ( Risk Avoidance ): Descontinuar a atividade, processo ou serviço gerador do risco (ex.: desligar e desativar em definitivo um sistema legado vulnerável sem suporte do fabricante). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "V – F – V".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "F – V – V". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Escuta clandestina de rede ( sniffing/eavesdropping ), roubo de dispositivos físicos, engenharia social, vazamento inadvertido de dados fiscais protegidos por sigilo e acessos não autorizados.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "F – F – F". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, secreta: 15 anos — Titulares de autarquias, fundações e órgãos públicos sob mesma alçada legal — Não admite prorrogação. O prazo cessa impreterivelmente aos 15 anos.
>
> **Gabarito: C**

---


### Teste 108
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Economia)**
Relacione os tipos de títulos financeiros com suas respectivas definições. 1. Letras e notas do Tesouro 2. Títulos privados de renda fixa 3. Ações ordinárias 4. Opções ( ) Conferem ao titular o direito, mas não a obrigação, de comprar ou vender um ativo por um preço previamente estabelecido, até o vencimento ou na data de vencimento. ( ) Representam participação no capital social da empresa, normalmente assegurando direito de voto nas assembleias. ( ) São títulos emitidos por empresas ou instituições financeiras, com remuneração previamente pactuada ou vinculada a algum indexador, sem conferir participação societária ao investidor. ( ) São títulos públicos emitidos pelo governo federal para captação de recursos e financiamento da dívida pública. Assinale a opção que indica a relação correta, na ordem apresentada.

* **A)** 4 – 3 – 2 – 1.
* **B)** 4 – 2 – 3 – 1.
* **C)** 3 – 4 – 2 – 1.
* **D)** 2 – 3 – 4 – 1.
* **E)** 1 – 3 – 2 – 4.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "4 – 3 – 2 – 1". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, mecanismos técnicos: Criptografia em trânsito (TLS) e em repouso (TDE), controle de acesso lógico baseado em papéis (RBAC), mascaramento dinâmico de dados e soluções de Prevenção contra Perda de Dados ( DLP Data Loss Prevention ).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "4 – 2 – 3 – 1". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, cláusula 10: Melhoria (Não conformidades, ações corretivas e ciclo contínuo).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "3 – 4 – 2 – 1". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, governo Digital Programa de Privacidade e Segurança da Informação (PPSI 2.0) Diretrizes, requisitos de maturidade e gestão de riscos cibernéticos para a administração pública.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "2 – 3 – 4 – 1". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, secreta: 15 anos — Titulares de autarquias, fundações e órgãos públicos sob mesma alçada legal — Não admite prorrogação. O prazo cessa impreterivelmente aos 15 anos.
> - **E)** **Correta.** Conforme fundamentado na seção *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade* deste guia, ameaças clássicas: Escuta clandestina de rede ( sniffing/eavesdropping ), roubo de dispositivos físicos, engenharia social, vazamento inadvertido de dados fiscais protegidos por sigilo e acessos não autorizados. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "1 – 3 – 2 – 4".
>
> **Gabarito: E**

---


### Teste 109
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Economia)**
Em uma pequena cidade, a prefeitura estuda financiar a iluminação das ruas por meio de contribuições voluntárias dos moradores. Como é difícil excluir do uso do sistema aqueles que não pagam, cada morador tem incentivo a contribuir menos do que contribuiria se pudesse ser cobrado individualmente pelo benefício recebido. Do ponto de vista microeconômico, a principal razão para a tendência à provisão ineficiente desse serviço é

* **A)** o problema do carona, associado à não exclusão característica dos bens públicos.
* **B)** a rivalidade no consumo do bem, que exige alocação por preços.
* **C)** a existência de economias de escala, que transforma o serviço em monopólio natural.
* **D)** a presença de externalidade positiva, decorrente do problema de não rivalidade no consumo.
* **E)** o fato de o bem ser de clube, permitindo exclusão sem custo relevante.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "o problema do carona, associado à não exclusão característica dos bens públicos". De acordo com a teoria estudada em *3.2 Análise Qualitativa vs. Análise Quantitativa (SLE, ARO e ALE)*, análise de Custo Benefício do Controle (CBA).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "a rivalidade no consumo do bem, que exige alocação por preços". De acordo com a teoria estudada em *5.3 A Declaração de Aplicabilidade (SoA) e a ISO/IEC 27005*, a justificativa formal obrigatória para a exclusão de qualquer controle que não tenha sido adotado.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "a existência de economias de escala, que transforma o serviço em monopólio natural". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, evitar / Eliminar ( Risk Avoidance ): Descontinuar a atividade, processo ou serviço gerador do risco (ex.: desligar e desativar em definitivo um sistema legado vulnerável sem suporte do fabricante).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "a presença de externalidade positiva, decorrente do problema de não rivalidade no consumo". De acordo com a teoria estudada em *2. Classificação e Rotulagem da Informação*, a classificação atribui rótulos de sensibilidade aos ativos de informação da organização, ditando os níveis de proteção lógica e física a serem aplicados de forma proporcional ao dano decorrente de divulgação ou modificação indevida.
> - **E)** **Correta.** Conforme fundamentado na seção *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade* deste guia, vulnerabilidade ( Vulnerability ): Ponto fraco, falha de projeto, brecha de configuração ou deficiência de controle em um ativo que pode ser explorado por uma ameaça. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "o fato de o bem ser de clube, permitindo exclusão sem custo relevante".
>
> **Gabarito: E**

---


### Teste 110
**(FGV – TCE/SC – 2026 – Auditor Fiscal De Controle Externo Engenharia Sanitaria)**
O instrumento de apoio à tomada de decisão que permite que a sociedade seja consultada previamente, por meio do envio de críticas, sugestões e contribuições por quaisquer interessados, sobre proposta de norma regulatória aplicável ao setor de saneamento básico, é denominado

* **A)** controle social.
* **B)** plano de gestão.
* **C)** consulta pública.
* **D)** audiência pública.
* **E)** agenda regulatória.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "controle social". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Escuta clandestina de rede ( sniffing/eavesdropping ), roubo de dispositivos físicos, engenharia social, vazamento inadvertido de dados fiscais protegidos por sigilo e acessos não autorizados.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "plano de gestão". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, a norma ABNT NBR ISO/IEC 27001 estabelece os requisitos formais para estabelecer, implementar, manter e melhorar continuamente um Sistema de Gestão de Segurança da Informação (SGSI).
> - **C)** **Correta.** Conforme fundamentado na seção *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)* deste guia, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "consulta pública".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "audiência pública". De acordo com a teoria estudada em *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL*, cláusula 7: Apoio (Recursos, capacitação, conscientização e comunicação).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "agenda regulatória". De acordo com a teoria estudada em *5.3 A Declaração de Aplicabilidade (SoA) e a ISO/IEC 27005*, se cada controle foi considerado aplicável ou não ao escopo do SGSI.
>
> **Gabarito: C**

---


### Teste 111
**(FGV – TRT/DA – 2025 – Tecnico Judiciario Area Administrativa Agente Da Policia Judicial)**
Maria, servidora pública federal ocupante de cargo de provimento efetivo, no pleno exercício de suas funções, foi convidada para integrar o conselho de administração de determinada sociedade empresária com personalidade jurídica de direito privado. Após analisar os balizamentos estabelecidos pela Lei nº 8.112/1990, com o objetivo de avaliar a possibilidade, ou não, de aceitar o convite, Maria concluiu corretamente que lhe é

* **A)** proibido participar do conselho de administração de qualquer sociedade empresária.
* **B)** permitido participar, apenas, do conselho de administração de sociedade de economia mista ou de empresa pública federal.
* **C)** permitido participar do conselho de administração de uma sociedade empresária caso seja autorizada por seu superior hierárquico.
* **D)** permitido participar, apenas, do conselho de administração de sociedade cooperativa constituída para prestar serviços a seus membros.
* **E)** permitido participar do conselho de administração de empresa ou entidade em que a União detenha, direta ou indiretamente, participação no capital social. Noções de Direito

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção promove generalização excessiva que desconsidera as condições técnicas e normativas ao afirmar que "proibido participar do conselho de administração de qualquer sociedade empresária". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes.
> - **B)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "permitido participar, apenas, do conselho de administração de sociedade de economia mista ou de empresa pública...". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, governo Digital Programa de Privacidade e Segurança da Informação (PPSI 2.0) Diretrizes, requisitos de maturidade e gestão de riscos cibernéticos para a administração pública.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "permitido participar do conselho de administração de uma sociedade empresária caso seja autorizada por seu...". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Escuta clandestina de rede ( sniffing/eavesdropping ), roubo de dispositivos físicos, engenharia social, vazamento inadvertido de dados fiscais protegidos por sigilo e acessos não autorizados.
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "permitido participar, apenas, do conselho de administração de sociedade cooperativa constituída para prestar...". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, reservada: 5 anos — Autoridades que exerçam funções formais de direção, comando ou chefia — Não admite prorrogação. O prazo cessa impreterivelmente aos 5 anos.
> - **E)** **Correta.** Conforme fundamentado na seção *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)* deste guia, aceitar / Reter ( Risk Acceptance / Retention ): Manter o risco no nível atual sem novos controles, mediante aprovação formal fundamentada da alta administração, quando o custo da salvaguarda técnica for superior à perda monetária potencial estimada. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT/DA/2025) ao estabelecer que "permitido participar do conselho de administração de empresa ou entidade em que a União detenha, direta ou...".
>
> **Gabarito: E**

---


### Teste 112
**(FGV – TRT/DA – 2025 – Tecnico Judiciario Area Administrativa Agente Da Policia Judicial)**
João, pessoa com deficiência, é ocupante de cargo de provimento efetivo no âmbito do Tribunal Regional do Trabalho da 24ª Região. Joana, por sua vez, é ocupante exclusiva de cargo em comissão no âmbito da mesma estrutura orgânica. Ambos, por serem muito amigos, decidiram analisar em conjunto a situação previdenciária de cada qual. Assinale a opção que apresenta, corretamente, a conclusão a que eles chegaram, ao fim de suas reflexões.

* **A)** A aposentadoria de ambos observará as regras do regime geral de previdência social.
* **B)** A aposentadoria de ambos observará as regras do regime próprio de previdência social.
* **C)** Tanto João como Joana estão sujeitos às regras de aposentadoria compulsória em razão da idade.
* **D)** Os períodos de férias não gozadas devem ser computados em dobro para fins de contagem do tempo de contribuição.
* **E)** Qualquer tratamento diferenciado em prol de João, quanto à idade e ao tempo de contribuição, deve ser estabelecido em lei complementar, não tendo sede constitucional.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A aposentadoria de ambos observará as regras do regime geral de previdência social". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, grau de Sigilo: Prazo Máximo de Restrição — Competência Originária Típica para Classificar — Regime de Prorrogação.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A aposentadoria de ambos observará as regras do regime próprio de previdência social". De acordo com a teoria estudada em *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade*, vulnerabilidade ( Vulnerability ): Ponto fraco, falha de projeto, brecha de configuração ou deficiência de controle em um ativo que pode ser explorado por uma ameaça.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Tanto João como Joana estão sujeitos às regras de aposentadoria compulsória em razão da idade". De acordo com a teoria estudada em *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade*, risco Residual: Risco que subsiste e permanece após o projeto e a entrada em operação dos controles de segurança mitigadores. Deve situar se estritamente abaixo do Apetite ao Risco fixado pela diretoria do tribunal.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Os períodos de férias não gozadas devem ser computados em dobro para fins de contagem do tempo de contribuição". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, ultrassecreta: 25 anos — Presidente da República, Vice Presidente, Ministros de Estado, Comandantes das Forças Armadas — Prorrogável uma única vez, por igual período (totalizando até 50 anos), exclusivamente pela CMRI ( Comissão Mista de Reavaliação de Informações ).
> - **E)** **Correta.** Conforme fundamentado na seção *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)* deste guia, concluída a avaliação do risco, a organização deve optar formalmente por uma das quatro respostas estratégicas. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT/DA/2025) ao estabelecer que "Qualquer tratamento diferenciado em prol de João, quanto à idade e ao tempo de contribuição, deve ser estabelecido...".
>
> **Gabarito: E**

---


### Teste 113
**(FGV – TRT/DA – 2025 – Tecnico Judiciario Area Administrativa Agente Da Policia Judicial)**
O Município Alfa, em observância às formalidades legais, celebrou contrato administrativo com determinada sociedade empresária, sem o prévio processo licitatório (contratação direta). Registre-se que o pacto envolveu a contratação do serviço técnico especializado, de natureza predominantemente intelectual, de treinamento e aperfeiçoamento de pessoal, sendo certo que a contratada é empresa de notória especialização. De acordo com a narrativa e considerando as disposições da Lei no 14.133/2021, analise as afirmativas a seguir. I. O Município Alfa celebrou contratação direta em razão da dispensa de licitação. II. No caso apresentado, é vedada a subcontratação de empresa distinta daquela que justificou a contratação direta. III. O ato que autorizou a contratação direta ou o extrato decorrente do contrato deverá ser mantido à disposição do público na sede física da repartição pública. Está correto o que se afirma em

* **A)** I, apenas.
* **B)** II, apenas.
* **C)** III, apenas.
* **D)** I e III, apenas.
* **E)** I, II e III.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I, apenas". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, evitar / Eliminar ( Risk Avoidance ): Descontinuar a atividade, processo ou serviço gerador do risco (ex.: desligar e desativar em definitivo um sistema legado vulnerável sem suporte do fabricante).
> - **B)** **Correta.** Conforme fundamentado na seção *2. Classificação e Rotulagem da Informação* deste guia, a classificação atribui rótulos de sensibilidade aos ativos de informação da organização, ditando os níveis de proteção lógica e física a serem aplicados de forma proporcional ao dano decorrente de divulgação ou modificação indevida. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT/DA/2025) ao estabelecer que "II, apenas".
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "III, apenas". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes.
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e III, apenas". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Ataques de negação de serviço (DoS e DDoS), falhas físicas de hardware em servidores e storages, interrupção no fornecimento de energia elétrica, panes nos links de internet e desastres ambientais (enchentes, incêndios em datacenters).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I, II e III". De acordo com a teoria estudada em *3. Gestão e Análise de Riscos de Segurança da Informação*, a gestão de riscos estabelece um processo contínuo e estruturado para identificar incertezas, avaliar a probabilidade de falhas e selecionar salvaguardas economicamente proporcionais.
>
> **Gabarito: B**

---


### Teste 114
**(FGV – TRT/DA – 2025 – Tecnico Judiciario Area Administrativa Agente Da Policia Judicial)**
Assinale a opção que apresenta, corretamente, o conceito de segurança institucional.

* **A)** Está relacionada à proteção de pessoas que estejam sob ameaça advinda de sua função em uma dada instituição.
* **B)** Tem a finalidade de manter a ordem pública e da paz social por meio da proteção do Estado.
* **C)** Compreende a segurança privada dos serviços públicos oferecidos pelo Estado.
* **D)** Tem por princípio de que o Estado tem que manter a proteção de pessoas e patrimônio.
* **E)** Atua na segurança prisional e nos deslocamentos de detentos de alta periculosidade.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade* deste guia, garantia de que a informação, os sistemas computacionais e os ativos de telecomunicações associados estejam acessíveis e utilizáveis sob demanda pelos usuários autorizados sempre que necessário. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT/DA/2025) ao estabelecer que "Está relacionada à proteção de pessoas que estejam sob ameaça advinda de sua função em uma dada instituição".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Tem a finalidade de manter a ordem pública e da paz social por meio da proteção do Estado". De acordo com a teoria estudada em *3.1 A Tríade Ativo, Ameaça e Vulnerabilidade*, ativo ( Asset ): Qualquer recurso humano, físico, tecnológico ou de informação que possui valor intrínseco para o cumprimento da missão da instituição.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Compreende a segurança privada dos serviços públicos oferecidos pelo Estado". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, decore rigorosamente os prazos decrescentes: 25 anos $\rightarrow$ 15 anos $\rightarrow$ 5 anos. A FCC inventa prazos alternativos inexistentes (como 10 ou 20 anos) ou inverte Secreta e Reservada. Além disso, lembre se: informações relativas à intimidade, vida privada, honra e imagem das pessoas têm restrição de acesso máxima de até 100 anos a contar da data de sua produção (Art. 31 da LAI), não se confundindo com prazos de segurança de Estado!.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Tem por princípio de que o Estado tem que manter a proteção de pessoas e patrimônio". De acordo com a teoria estudada em *2.2 Classificação Corporativa Geral de Ativos*, confidencial: Informações estratégicas, relatórios preliminares de auditoria em instrução ou dados cadastrais sob sigilo fiscal; vazamento gera dano financeiro ou institucional grave.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Atua na segurança prisional e nos deslocamentos de detentos de alta periculosidade". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, aSSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. ABNT NBR ISO/IEC 27005:2023: Segurança da informação, segurança cibernética e proteção da privacidade — Gestão de riscos de segurança da informação. Rio de Janeiro: ABNT, 2023.
>
> **Gabarito: A**

---


### Teste 115
**(FGV – TRT/DA – 2025 – Tecnico Judiciario Area Administrativa Sem Especialidade)**
A transparência na Administração Pública é um princípio fundamental que promove a confiança social, garantindo o acesso às informações, a accountability e a participação cidadã na gestão dos recursos e na tomada de decisões governamentais. Assinale a opção que apresenta, corretamente, o conceito que representa a qualidade da informação coletada na fonte, com o máximo de detalhamento possível, sem modificações.

* **A)** Autenticidade.
* **B)** Integridade.
* **C)** Tratamento.
* **D)** Primariedade.
* **E)** Disponibilidade.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Autenticidade". De acordo com a teoria estudada em *1. Princípios Básicos da Segurança da Informação (CIDAN)*, a segurança da informação é definida pela norma ABNT NBR ISO/IEC 27000 como a preservação da confidencialidade, integridade e disponibilidade da informação, admitindo se adicionalmente propriedades vitais para transações formais como a autenticidade e o não repúdio. O mnemônico padronizado em concursos da FCC é CIDAN.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Integridade". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, ameaças clássicas: Escuta clandestina de rede ( sniffing/eavesdropping ), roubo de dispositivos físicos, engenharia social, vazamento inadvertido de dados fiscais protegidos por sigilo e acessos não autorizados.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Tratamento". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, decreto Federal nº 9.637/2018 (Política Nacional de Segurança da Informação) Institui a PNSI, dispondo sobre governança, gestão de riscos e tratamento de incidentes de segurança da informação.
> - **D)** **Correta.** Conforme fundamentado na seção *🌐 Fontes Oficiais e Referências Bibliográficas* deste guia, governo Digital Programa de Privacidade e Segurança da Informação (PPSI 2.0) Diretrizes, requisitos de maturidade e gestão de riscos cibernéticos para a administração pública. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT/DA/2025) ao estabelecer que "Primariedade".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Disponibilidade". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, garantia de que o acesso à informação é restrito estrita e exclusivamente a pessoas, entidades ou processos formalmente autorizados.
>
> **Gabarito: D**

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

### Teste 116
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


### Teste 117
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
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "irretratabilidade". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, aSSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. ABNT NBR ISO/IEC 27001:2022: Tecnologia da informação — Técnicas de segurança — Sistemas de gestão da segurança da informação — Requisitos. Rio de Janeiro: ABNT, 2022.
> - **D)** **Correta.** Conforme fundamentado na seção *5.1 A Norma Certificável ISO/IEC 27001 e o Anexo SL* deste guia, a norma ABNT NBR ISO/IEC 27001 estabelece os requisitos formais para estabelecer, implementar, manter e melhorar continuamente um Sistema de Gestão de Segurança da Informação (SGSI). Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 15ª/2015) ao estabelecer que "compatibilidade".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "integridade". De acordo com a teoria estudada em *1.1 Os Pilares Fundamentais: Confidencialidade, Integridade e Disponibilidade*, mecanismos técnicos: Redundância de hardware e fontes de alimentação, clusters de alta disponibilidade (HA ativo ativo ou ativo passivo), sistemas anti DDoS, geradores e nobreaks comutáveis, planos de continuidade de negócios (PCN/DRP) e rotinas estruturadas de backup.
>
> **Gabarito: D**

---


### Teste 118
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Gestão Governamental)**
A Lei nº 14.133/2021 estabelece que as contratações públicas deverão submeter-se a práticas contínuas e permanentes de gestão de riscos e de controle preventivo, inclusive mediante adoção de recursos de tecnologia da informação, e, além de estar subordinadas ao controle social, sujeitar-se-ão às linhas de defesa nela delimitadas. Acerca do aludido tema, à luz do mencionado Diploma Legal, é correto afirmar que os Tribunal de Contas

* **A)** integram todas as linhas de defesa, em razão da relevância do controle por eles exercido.
* **B)** integram a primeira linha de defesa, juntamente com as autoridades que atuam na estrutura de governança do órgão ou entidade.
* **C)** integram a segunda linha de defesa, juntamente com as unidades de assessoramento jurídico.
* **D)** integram a terceira linha de defesa, juntamente o órgão central de controle interno da Administração.
* **E)** não integram tais linhas de defesa, que são compostas apenas pelos órgãos de controle interno.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "integram todas as linhas de defesa, em razão da relevância do controle por eles exercido". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, aceitar / Reter ( Risk Acceptance / Retention ): Manter o risco no nível atual sem novos controles, mediante aprovação formal fundamentada da alta administração, quando o custo da salvaguarda técnica for superior à perda monetária potencial estimada.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "integram a primeira linha de defesa, juntamente com as autoridades que atuam na estrutura de governança do órgão...". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, decreto Federal nº 9.637/2018 (Política Nacional de Segurança da Informação) Institui a PNSI, dispondo sobre governança, gestão de riscos e tratamento de incidentes de segurança da informação.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "integram a segunda linha de defesa, juntamente com as unidades de assessoramento jurídico". De acordo com a teoria estudada em *3. Gestão e Análise de Riscos de Segurança da Informação*, a gestão de riscos estabelece um processo contínuo e estruturado para identificar incertezas, avaliar a probabilidade de falhas e selecionar salvaguardas economicamente proporcionais.
> - **D)** **Correta.** Conforme fundamentado na seção *🌐 Fontes Oficiais e Referências Bibliográficas* deste guia, governo Digital Programa de Privacidade e Segurança da Informação (PPSI 2.0) Diretrizes, requisitos de maturidade e gestão de riscos cibernéticos para a administração pública. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "integram a terceira linha de defesa, juntamente o órgão central de controle interno da Administração".
> - **E)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "não integram tais linhas de defesa, que são compostas apenas pelos órgãos de controle interno". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, secreta: 15 anos — Titulares de autarquias, fundações e órgãos públicos sob mesma alçada legal — Não admite prorrogação. O prazo cessa impreterivelmente aos 15 anos.
>
> **Gabarito: D**

---


### Teste 119
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Ciências Atuariais)**
O Regime Próprio de Previdência Social (RPPS) de um determinado Estado da Federação possui uma carteira de investimentos com grande liquidez. O dirigente sugere que o instituto aplique esses recursos em Certificados de Depósito Bancário (CDB) do Banco de Desenvolvimento do próprio Estado, argumentando que os juros oferecidos são superiores aos do mercado, que o banco possui histórico de liquidez e solvência, e, ainda, que os recursos permaneceriam fomentando a economia regional. Com base na lógica de gestão de riscos da Resolução CMN nº 5.272/2025, assinale a opção que apresenta uma situação ou justificativa para a vedação desse tipo de operação.

* **A)** Ausência de aprovação, prévia, pelo conselho de administração e comitê de investimentos, assumindo expressamente a responsabilidade por eventuais perdas decorrentes do risco de crédito.
* **B)** Ausência de certificação Pró-Gestão Nível IV, visto que apenas esse nível máximo autoriza o investimento em qualquer instituição financeira nacional autorizada para funcionamento pelo Banco Central do Brasil.
* **C)** Caso o banco do Estado não apresente uma classificação de risco “grau de investimento”, por pelo menos duas das três agências “big three” de risco internacional.
* **D)** Proibição da aplicação de recursos em instituições financeiras cujo controle societário seja detido, direta ou indiretamente, pelo ente federativo.
* **E)** Proibição da aplicação de recursos superiores a 5% do patrimônio líquido do banco estatal, pela regra de concentração para ativos estruturados.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Ausência de aprovação, prévia, pelo conselho de administração e comitê de investimentos, assumindo expressamente a...". De acordo com a teoria estudada em *3.3 As Quatro Estratégias de Tratamento do Risco (ISO/IEC 27005)*, aceitar / Reter ( Risk Acceptance / Retention ): Manter o risco no nível atual sem novos controles, mediante aprovação formal fundamentada da alta administração, quando o custo da salvaguarda técnica for superior à perda monetária potencial estimada.
> - **B)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "Ausência de certificação Pró Gestão Nível IV, visto que apenas esse nível máximo autoriza o investimento em...". De acordo com a teoria estudada em *2.2 Classificação Corporativa Geral de Ativos*, restrita / Secreta: Nível máximo corporativo (chaves criptográficas mestras de certificados de segurança, senhas de administradores de domínios centrais); divulgação gera dano catastrófico e imediato.
> - **C)** **Correta.** Conforme fundamentado na seção *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)* deste guia, no setor público brasileiro, a publicidade é a regra geral e o sigilo é a exceção expressa (Art. 5º, XXXIII da CF/88). Nos termos do Artigo 24 da Lei nº 12.527/2011 (LAI), as informações passíveis de restrição por representarem risco à segurança da sociedade e do Estado classificam se em três graus solenes. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "Caso o banco do Estado não apresente uma classificação de risco “grau de investimento”, por pelo menos duas das...".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Proibição da aplicação de recursos em instituições financeiras cujo controle societário seja detido, direta ou...". De acordo com a teoria estudada em *2.1 Graus de Sigilo no Setor Público (Lei de Acesso à Informação - Lei nº 12.527/2011)*, grau de Sigilo: Prazo Máximo de Restrição — Competência Originária Típica para Classificar — Regime de Prorrogação.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Proibição da aplicação de recursos superiores a 5% do patrimônio líquido do banco estatal, pela regra de...". De acordo com a teoria estudada em *2. Classificação e Rotulagem da Informação*, a classificação atribui rótulos de sensibilidade aos ativos de informação da organização, ditando os níveis de proteção lógica e física a serem aplicados de forma proporcional ao dano decorrente de divulgação ou modificação indevida.
>
> **Gabarito: C**

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
