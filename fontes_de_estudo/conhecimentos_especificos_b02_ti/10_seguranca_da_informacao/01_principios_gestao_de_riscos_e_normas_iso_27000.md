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
**(FGV – TJ-AP – Analista Judiciário - Segurança da Informação – 2023)**
Amanda trabalha em uma consultoria X e está implementando 
um NAP (proteção de acesso à rede) em um cliente. O objetivo de 
Amanda com tal implementação é manter a integridade dos 
computadores da rede corporativa.  
Para proteger o acesso à rede de forma adequada, deve existir 
uma infraestrutura de rede que forneça à área de funcionalidade:

* **A)** validação de integridade: determina se os computadores 
estão em conformidade com os requisitos de integridade do 
sistema;
* **B)** zona desmilitarizada: impede que um usuário autorizado com 
um computador em conformidade carregue um p rograma 
mal-intencionado na rede;
* **C)** restrição de rede: permite o acesso à rede, desde que o 
computador do usuário atenda aos requisitos de política de 
integridade;
* **D)** correção: restringe o acesso à rede ou à comunicação para 
clientes que não estão em conformidade com os requisitos de 
integridade do sistema;
* **E)** conformidade contínua: fornece as atualizações necessárias 
para permitir que o computador corrija seu estado de 
integridade não compatível.

---

> **Comentário Detalhado:**
>
> - **A)** Correta. Representa com precisão a disciplina do tema e o entendimento pacificado adotado pela banca (FGV).
> - **B)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **C)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **D)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **E)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
>
> **Gabarito: A**

---
### Teste 356
**(FGV – TJ-AP – Analista Judiciário - Segurança da Informação – 2023)**
Um centro de estudos, resposta e tratamento de incidentes 
(CERT) possui, dentre suas atribuições, a manutenção da 
consciência situacional relativa à segurança cibernética. O CERT 
atua correlacionando  eventos a fim de permitir a detecção 
precoce de incidentes e ataques no espaço cibernético.  
Uma atividade que contribui para a manutenção ou incremento 
da consciência situacional é:

* **A)** a coleta e o compartilhamento de informações que possam 
ser usadas pela comunidade;
* **B)** o desenvolvimento de materiais de boas práticas para 
administradores de redes por meio da Internet e para 
usuários finais;
* **C)** a fomentação da cooperação entre CSIRTs através da 
organização de fóruns específicos;
* **D)** o suporte ao proces so de mitigação de danos causados por 
um incidente e de recuperação de sistemas comprometidos;
* **E)** o suporte ao processo de análise de atividades maliciosas e 
de sistemas comprometidos.

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
**(FGV – TJ-AP – Analista Judiciário - Segurança da Informação – 2023)**
A Estratégia Nacional de Segurança Cibernética do Poder 
Judiciário (ENSEC -PJ) define, em seu Art. 12, um modelo 
centralizado de governança nacional na segurança cibernética 
para os órgãos no âmbito do Poder Judiciário, à exceção do 
Supremo Tribunal Federal.  
Um dos objetivos desse modelo centralizado é:

* **A)** realizar exercícios cibernéticos com a partic ipação de 
múltiplos entes;
* **B)** estabelecer norma sobre a definição dos requisitos 
metodológicos para a implementação da gestão de risco dos 
ativos da informação no Poder Judiciário;
* **C)** estabelecer rotinas de verificações de conformidade em 
segurança cibernética;
* **D)** elaborar a Política de Segurança da Informação e normas 
internas correlatas ao tema, observadas as normas de 
segurança da informação editadas pelo CNJ;
* **E)** promover ações de capacitação e profissionalização dos 
recursos humanos em temas relacio nados à segurança da 
informação.

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
### Teste 358
**(FCC – TRT-23 – Analista Judiciário (TI) – 2016)**  
Um Analista do TRT23 deve estabelecer o sistema de gestão de segurança do Tribunal baseado na norma ABNT NBR ISO/IEC 27001:2013. Na fase de planejamento, os objetivos de segurança devem ser

* **A)** independentes da política de segurança da informação.
* **B)** mantidos em segredo pela alta direção da organização.
* **C)** fixos e imutáveis para possibilitar a avaliação de desempenho.
* **D)** distintos ao plano de negócio da organização.
* **E)** elaborados considerando os tratamentos de riscos.

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Conforme a ABNT NBR ISO/IEC 27001 (item 6.2), os objetivos de segurança da informação devem ser estritamente consistentes com a política de segurança da informação da organização.
> - **B)** Incorreta. Os objetivos de segurança devem ser devidamente comunicados a todas as partes interessadas relevantes, e não mantidos em segredo.
> - **C)** Incorreta. A norma estabelece que os objetivos de segurança devem ser monitorados e atualizados conforme apropriado (ciclo PDCA/melhoria contínua), não sendo fixos nem imutáveis.
> - **D)** Incorreta. A ISO 27001 exige alinhamento estratégico entre os objetivos de segurança e os objetivos de negócio da instituição.
> - **E)** Correta. Nos termos do item 6.2 da ABNT NBR ISO/IEC 27001, ao planejar como alcançar seus objetivos de segurança da informação, a organização deve considerar os resultados da avaliação de riscos e os tratamentos de riscos aplicados.
>
> **Gabarito: E**

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
**(FCC – TRT-14 – Analista Judiciário (TI) – 2016)**  
A etapa de análise de riscos, no processo de Gestão de Riscos, pode ser realizada de forma quantitativa ou qualitativa. Apó s a categorização dos riscos, deve-se decidir pelo tratamento e recursos a alocar. Uma das opções disponíveis para tratamento do risco é

* **A)** eliminar o sistema que gerou o risco, visando reduzir o risco.
* **B)** atuar sobre os ativos que sofrem as consequências do risco, visando eliminar o risco.
* **C)** escolher apenas uma alternativa que seja economicamente viável, já que é impossível reter o risco.
* **D)** utilizar sempre medidas de caráter contingencial ou mitigatório, evitando-se as medidas preventivas.
* **E)** transferir o risco, por meio de seguros, cooperação ou outra ação adequada.

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Eliminar um sistema que gera risco é uma medida de 'evitar o risco' (eliminação da atividade), e não de redução.
> - **B)** Incorreta. Atuar sobre vulnerabilidades ou ameaças visa mitigar ou reduzir o risco, sendo praticamente impossível 'eliminar' de forma absoluta o risco sem descontinuar a operação.
> - **C)** Incorreta. Reter (aceitar) o risco residual é uma das opções fundamentais de tratamento quando o impacto está dentro dos limites de tolerância e o custo de controle supera o benefício.
> - **D)** Incorreta. As normas de gestão de riscos (ISO 27005 / ISO 31000) priorizam a prevenção e a redução pró-ativa sobre medidas puramente contingenciais.
> - **E)** Correta. De acordo com os frameworks de gestão de riscos (ISO 31000 e ISO/IEC 27005), as opções de tratamento de riscos compreendem: evitar o risco, mitigar/reduzir o risco, reter/aceitar o risco e compartilhar/transferir o risco (por meio de contratos de seguro, terceirização ou cooperação institucional).
>
> **Gabarito: E**

---

### Teste 360
**(FGV – TJ-AP – Analista Judiciário - Banco de Dados – 2023)**
Uma empresa de consultoria X foi contratada para verificar os 
riscos quanto à segurança da informação no Tribunal de Justiça 
do Amapá (TJAP). Para atender ao requisito licitatório, a 
consultoria fez uso da norma ABNT NBR ISO/IEC 27005:2011. Em 
seu relatóri o de segurança, a consultoria identificou riscos 
causados por fenômenos naturais, de forma que a melhor 
alternativa era mover fisicamente as instalações para um local 
onde tal risco não exista ou esteja sob controle.  
A empresa de consultoria X se baseou no tópico de tratamento 
de riscos de:

* **A)** reter o risco;
* **B)** modificar o risco;
* **C)** evitar o risco;
* **D)** compartilhar o risco;
* **E)** aceitar o risco. 


Tribunal de Justiça do Estado do Amapá FGV Conhecimento 

Analista Jud - Apoio Especializado - Tecnologia da Informação - Banco de Dados  Tipo 1  ̶  Branca – Página 18

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
### Teste 361
**(FGV – TJ-AP – Analista Judiciário - Banco de Dados – 2023)**
O Tribunal de Justiça do Amapá (TJAP) identificou que não havia 
um documento de Política para Segurança da Informação e 
resolveu elaborá-lo. Para atender esse objetivo, fez uso da Norma 
27002:2013, que orienta a organização a def inir uma política de 
segurança que seja aprovada pela direção.  
Para a elaboração do documento, a norma orienta que sejam 
contemplados requisitos oriundos da(s):

* **A)** normas da família 27000, atribuição de responsabilidades 
gerais e específicas para o gerenciamento da segurança;
* **B)** definições de segurança da informação, objetivos e princípios 
para orientar todas as atividades de segurança;
* **C)** definição do controle de acesso, segurança física e do 
ambiente e proteção contra malware;
* **D)** transferência de inf ormação, segurança nas comunicações, 
proteção e privacidade da informação de identificação 
pessoal;
* **E)** estratégia de negócios, regulamentações, legislação e 
contratos e ambiente de ameaça da segurança da 
informação, atual e futuro.

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
**(FGV – TJ-AP – Analista Judiciário - Banco de Dados – 2023)**
Fábio pertence ao departamento de segurança da empresa K e 
está verificando os controles existentes para a Gestão de Riscos 
de Segurança da Informação. Ele faz uso da norma ABNT N BR 
ISO/IEC 27005:2011 para efetuar sua verificação. Fábio está 
examinando o correto funcionamento dos controles existentes. 
Ele identificou alguns controles obsoletos, que foram 
descartados, e outros que foram substituídos por controles 
melhores ou mais modernos.  
Nesse momento, Fábio está fazendo uso da tarefa dentro de 
identificação de riscos:

* **A)** dos ativos;
* **B)** das ameaças;
* **C)** de controles existentes;
* **D)** das vulnerabilidades;
* **E)** de consequências.

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **B)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **C)** Correta. Representa com precisão a disciplina do tema e o entendimento pacificado adotado pela banca (FGV).
> - **D)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **E)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
>
> **Gabarito: C**

---
### Teste 363
**(FGV – TRT – Analista Judiciário - Tecnologia da Informação – 2024)**
A ABNT NBR ISO/IEC 27001:2022, NBR ISO/IEC 27002:2022, os CIS 
v8, SIEM, e a Lei nº 13.709(LGPD) são algumas das diversas normas 
e leis que trabalham conjuntamente para assegurar a integridade, 
confidencialidade e disponibilidade dos dados no contexto da 
segurança da informação.  
Assinale a opção que descreve corretamente uma contribuição 
combinada dessas leis e normas.

* **A)** Apenas a implementação da LGPD é suficiente para garantir a 
conformidade legal e a segurança da informação, tornando as 
outras normas e controles redundantes.
* **B)** O ponto chave dos Sistemas de Gerenciamento de 
Informações e Eventos de Segurança (SIEM) oferecer somente 
práticas de segurança pessoal em tempo real que  deve ser 
combinado as demais normas e leis.
* **C)** As normas ABNT NBR ISO/IEC estabelecem os requisitos gerais 
de segurança, a LGPD foca na proteção de dados pessoais, e os 
SIEM proporcionam a visão e controle operacionais 
necessários.
* **D)** A adoção dos CIS C ritical Security Controls v8 cobre os 
requisitos de segurança e as normas ABNT NBR ISO/IEC 
fornecem o complemento no que se refere a proteção de 
dados pessoais.
* **E)** A ABNT NBR ISO/IEC 27001:2022 e a 27002:2022 são as únicas 
que fornecem uma abordagem baseada em risco que utilizará 
os outros mecanismos para organizar e controlar os sistemas 
de segurança.

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **B)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **C)** Correta. Representa com precisão a disciplina do tema e o entendimento pacificado adotado pela banca (FGV).
> - **D)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
> - **E)** Incorreta. Discrepa das diretrizes normativas e jurisprudenciais aplicáveis ao tema objeto do item.
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

### Teste 364
**(FCC – TRT-23 – Analista Judiciário (TI) – 2016)**  
De acordo com a norma ABNT NBR ISO/IEC 27002:2013 a política de controle de acesso deve considerar

* **A)** a disponibilidade de referências de caráter satisfatórias do usuário, por exemplo, uma profissional e uma pessoal.
* **B)** verificações financeiras e verificações de registros criminais do usuário.
* **C)** ações a serem tomadas no caso de o funcionário desrespeitar os requisitos de segurança da informação da organização.
* **D)** a legislação pertinente e qualquer obrigação contratual relativa à proteção de acesso para dados ou serviços.
* **E)** a confirmação e documentação das qualificações acadêmicas e profissionais do usuário.

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Referências de caráter pessoal/profissional referem-se aos controles de segurança em recursos humanos (seleção e admissão), não à política de controle de acesso aos sistemas.
> - **B)** Incorreta. Verificações de antecedentes integram o processo pré-contratual de RH.
> - **C)** Incorreta. Ações sancionatórias disciplinares compõem o processo disciplinar formal previsto na seção de recursos humanos.
> - **D)** Correta. De acordo com a norma ABNT NBR ISO/IEC 27002 (Controle 9.1.1 - Requisitos de negócio para controle de acesso), a política de controle de acesso deve levar em consideração os requisitos de negócio, as políticas de segurança, a legislação pertinente e quaisquer obrigações contratuais relativas à proteção de acesso a dados ou serviços.
> - **E)** Incorreta. A comprovação de qualificações acadêmicas é controle típico de triagem pré-admissional em recursos humanos.
>
> **Gabarito: D**

---

### Teste 365
**(FCC – TRT – Analista Judiciário - Tecnologia da Informação – 2009)**
A prioridade na tramitação dos processos e procedimentos 
administrativos e na execução dos atos e diligências admi-
nistrativas é assegurada quando figure, em qualquer grau 
de instância, como requerente ou interveniente, pessoa 
com idade igual ou superior a

* **A)** 55 anos.
* **B)** 60 anos.
* **C)** 65 anos.
* **D)** 70 anos.
* **E)** 75 anos. 
_________________________________________________________

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
## 🌐 Fontes Oficiais e Referências Bibliográficas

* [NIST Cybersecurity Framework (CSF 2.0)](https://www.nist.gov/cyberframework) - Estrutura de referência global do NIST para identificação, proteção, detecção, resposta e recuperação de riscos cibernéticos.
* [NIST SP 800-30 Rev. 1 - Guide for Conducting Risk Assessments](https://csrc.nist.gov/pubs/sp/800/30/r1/final) - Guia metodológico oficial para condução de processos de avaliação e gestão de riscos em segurança da informação.
* [NIST SP 800-37 Rev. 2 - Risk Management Framework](https://csrc.nist.gov/pubs/sp/800/37/r2/final) - Diretrizes para aplicação do Risk Management Framework (RMF) aos sistemas e organizações.
* [Governo Digital - Programa de Privacidade e Segurança da Informação (PPSI 2.0)](https://www.gov.br/governodigital/pt-br/privacidade-e-seguranca/ppsi-2.0) - Diretrizes, requisitos de maturidade e gestão de riscos cibernéticos para a administração pública.
* [Decreto Federal nº 9.637/2018 (Política Nacional de Segurança da Informação)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/decreto/d9637.htm) - Institui a PNSI, dispondo sobre governança, gestão de riscos e tratamento de incidentes de segurança da informação.
* ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **ABNT NBR ISO/IEC 27001:2022**: Tecnologia da informação — Técnicas de segurança — Sistemas de gestão da segurança da informação — Requisitos. Rio de Janeiro: ABNT, 2022.
* ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **ABNT NBR ISO/IEC 27005:2023**: Segurança da informação, segurança cibernética e proteção da privacidade — Gestão de riscos de segurança da informação. Rio de Janeiro: ABNT, 2023.
* STALLINGS, William. **Criptografia e Segurança de Redes: Princípios e Práticas**. 7. ed. São Paulo: Pearson Education do Brasil, 2018. (Cap. 1 - Visão Geral de Segurança da Informação).
