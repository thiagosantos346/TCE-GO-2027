# 01 - LGPD Aplicada ao Desenvolvimento e Operação de Sistemas

> **Matéria:** Legislação Aplicada à Tecnologia da Informação  
> **Cargo:** B02 – Técnico de Controle Externo – Especialidade: Tecnologia da Informação  
> **Arquivo:** `01_lgpd_aplicada_ao_desenvolvimento_e_sistemas.md`  
> **Ato Normativo:** Lei Federal nº 13.709, de 14 de agosto de 2018 (Lei Geral de Proteção de Dados Pessoais - LGPD)



---


## 📌 Ementa / Itens do Edital
- Aplicação técnica da LGPD (Lei nº 13.709/2018) no ciclo de desenvolvimento de software e operação de sistemas
- Conceitos essenciais: Dado pessoal, Dado sensível, Dado anonimizado, Titular, Controlador, Operador e Encarregado (DPO)
- Princípios da LGPD aplicados à engenharia de software (com foco em Minimização e Finalidade)
- Metodologias: Privacy by Design e Privacy by Default (Ann Cavoukian)
- Técnicas de desidentificação: Anonimização vs. Pseudonimização
- Implementação de direitos dos titulares em sistemas de informação e segurança de dados



---


## 🧭 Sumário

1. [Teoria Aprofundada & Fundamentos de Engenharia](#teoria-aprofundada-fundamentos-de-engenharia)
2. [Taxonomia de Dados e Papéis sob a LGPD](#1-taxonomia-de-dados-e-papeis-sob-a-lgpd)
    1. [Classificação Legal e Técnica dos Dados](#11-classificacao-legal-e-tecnica-dos-dados)
    2. [Teste 515](#Teste-515)
    3. [Agentes de Tratamento e o Encarregado (DPO)](#12-agentes-de-tratamento-e-o-encarregado-dpo)
    4. [Teste 516](#Teste-516)
3. [Princípios do Art. 6º sob a Ótica da Arquitetura e Engenharia de Software](#2-principios-do-art-6o-sob-a-otica-da-arquitetura-e-engenharia-de-software)
    1. [Teste 517](#Teste-517)
4. [Privacy by Design e Privacy by Default (Ann Cavoukian)](#3-privacy-by-design-e-privacy-by-default-ann-cavoukian)
    1. [Os 7 Princípios Fundamentais do Privacy by Design](#31-os-7-principios-fundamentais-do-privacy-by-design)
    2. [Teste 518](#Teste-518)
    3. [Comparativo: Privacy by Design vs. Privacy by Default](#32-comparativo-privacy-by-design-vs-privacy-by-default)
    4. [Teste 519](#Teste-519)
5. [Engenharia de Desidentificação: Anonimização vs. Pseudonimização](#4-engenharia-de-desidentificacao-anonimizacao-vs-pseudonimizacao)
    1. [Técnicas Criptográficas de Pseudonimização](#41-tecnicas-criptograficas-de-pseudonimizacao)
    2. [Teste 520](#Teste-520)
    3. [Métricas Formais de Anonimização (k-Anonymity, l-Diversity, t-Closeness e DP)](#42-metricas-formais-de-anonimizacao-k-anonymity-l-diversity-t-closeness-e-dp)
    4. [Teste 521](#Teste-521)
6. [Implementação Técnica dos Direitos dos Titulares (Art. 18 da LGPD)](#5-implementacao-tecnica-dos-direitos-dos-titulares-art-18-da-lgpd)
    1. [Mapeamento dos Direitos e Requisitos Técnicos](#51-mapeamento-dos-direitos-e-requisitos-tecnicos)
    2. [Teste 522](#Teste-522)
    3. [Comunicação de Incidentes de Segurança à ANPD e Titulares (Art. 48)](#52-comunicacao-de-incidentes-de-seguranca-a-anpd-e-titulares-art-48)
    4. [Teste 523](#Teste-523)
    5. [Teste 524](#Teste-524)
7. [Fontes Recomendadas na Internet](#6-fontes-recomendadas-na-internet)

---


## 📖 Teoria Aprofundada & Fundamentos de Engenharia


---


## 1. Taxonomia de Dados e Papéis sob a LGPD

A aplicação da **Lei Geral de Proteção de Dados Pessoais (Lei nº 13.709/2018 - LGPD)** na Engenharia de Software, Arquitetura de Sistemas e Operações de TI (DevSecOps) impõe uma reformulação estrutural nos modelos conceituais de dados, esquemas relacionais e NoSQL, esteiras de mensageria, contratos de APIs e controles de acesso.

### 1.1 Classificação Legal e Técnica dos Dados

```mermaid
flowchart TD
    DADO["Dado Bruto em Sistema"] --> DP{"Refere-se a Pessoa Natural Identificada ou Identificável?"}
    DP -- "Não" --> D_NAO_PESSOAL["Dado Não Pessoal / Corporativo / Estatístico"]
    DP -- "Sim" --> D_PESSOAL["DADO PESSOAL (Escopo LGPD)"]
    
    D_PESSOAL --> SENSIVEL{"Enquadra-se no rol taxativo do Art. 5º, II (saúde, biometria, religião, etc.)?"}
    SENSIVEL -- "Sim" --> DPS["DADO PESSOAL SENSÍVEL (Art. 11: Requisitos Rígidos, Sem Legítimo Interesse)"]
    SENSIVEL -- "Não" --> DPC["DADO PESSOAL COMUM (Art. 7º: 10 Bases Legais)"]
    
    D_PESSOAL --> DESID{"Submetido a Processo de Desidentificação?"}
    DESID -- "Reversível mediante informação adicional mantida à parte" --> PSEUDO["DADO PSEUDONIMIZADO (Art. 13, §4º: CONTINUA SENDO DADO PESSOAL)"]
    DESID -- "Irreversível por meios técnicos razoáveis e disponíveis" --> ANON["DADO ANONIMIZADO (Art. 12: NÃO É MAIS DADO PESSOAL)"]
```

| Categoria | Definição Legal (LGPD) | Exemplos Técnicos em Banco de Dados / APIs | Regime Jurídico de Proteção |
|---|---|---|---|
| **Dado Pessoal Comum** (Art. 5º, I) | Informação relacionada a pessoa natural identificada ou identificável. | Nome, CPF, e-mail pessoal, endereço IP de log, User-Agent, cookie identifier, geolocalização GPS. | Sujeito integralmente à LGPD. Pode ser tratado via 10 bases legais (Art. 7º), incluindo execução de contrato, cumprimento de obrigação legal e legítimo interesse. |
| **Dado Pessoal Sensível** (Art. 5º, II) | Origem racial/étnica, convicção religiosa, opinião política, filiação a sindicato/organização religiosa/política, dado referente à saúde ou à vida sexual, dado genético ou biométrico. | Template biométrico facial/digital, prontuário médico eletrônico, CID em atestados, exames toxicológicos. | Regime altamente restritivo (Art. 11). **NÃO admite a base legal do Legítimo Interesse**. Exige consentimento específico e destacado ou hipóteses legais estritas. |
| **Dado Pseudonimizado** (Art. 13, § 4º) | Dado que perde a possibilidade de associação direta a um indivíduo, senão pelo uso de informação adicional mantida separadamente pelo controlador. | IDs com Hashing salgado (`SHA-256(CPF + Salt)`), tokens UUID opacos cujas tabelas de de-para residem em base isolada com KMS. | **CONTINUA SENDO DADO PESSOAL**. É uma salvaguarda técnica e de segurança, não uma isenção da lei. |
| **Dado Anonimizado** (Art. 12) | Dado relativo a titular que não possa ser identificado, considerando meios técnicos razoáveis e disponíveis na ocasião do tratamento. | Conjuntos agregados com k-anonymity alto, microdados com injeção de ruído laplaciano (Differential Privacy). | **NÃO é considerado dado pessoal**, saindo do escopo da LGPD, **salvo se o processo for revertido** ou reversível por esforço razoável. |

> 🚨 **ALERTA DE PROVA / PEGADINHA FCC:**  
> A FCC tenta induzir o candidato ao erro afirmando que a **pseudonimização** retira o dado da incidência da LGPD. Isso é **FALSO**! O dado pseudonimizado permanece sob a tutela da LGPD porque o próprio controlador ou terceiro autorizado detém a chave reversora (informação adicional). Somente a **anonimização real e irreversível** afasta a aplicação da lei (Art. 12).

---

### Teste 515
**(FCC - Auditor de Controle Externo / Tecnologia da Informação)**
**Enunciado:** Um arquiteto de software da Diretoria de Tecnologia da Informação de um órgão de controle externo está projetando a nova arquitetura do sistema de protocolo e tramitação processual eletrônica. Durante o levantamento de requisitos, a equipe propôs três medidas de segurança e tratamento de dados:  

I. Substituir o CPF dos cidadãos denunciantes por um hash criptográfico com salt aleatório gerado pelo servidor corporativo, cuja tabela de correspondência fica protegida em repositório seguro acessível unicamente pelos auditores responsáveis pela instrução da denúncia.  

II. Disponibilizar os dados de contratações públicas para consulta de terceiros somente após a aplicação de algoritmos de k-anonimato e injeção de ruído laplaciano, de tal forma que, por nenhum meio técnico razoável e disponível na ocasião do tratamento, seja possível identificar as pessoas naturais associadas.  

III. Ativar, por padrão, em todos os novos formulários públicos web, caixas de diálogo pré-marcadas autorizando o compartilhamento irrestrito de contatos telefônicos de cidadãos com órgãos de publicidade privada.  

À luz das disposições da Lei Federal nº 13.709/2018 (LGPD) e das metodologias de *Privacy by Design* e *Privacy by Default*, é correto afirmar que:  

* **A)** As medidas I e II configuram anonimização perfeita, excluindo ambos os conjuntos de dados da incidência da LGPD.
* **B)** A medida I configura pseudonimização, razão pela qual os dados tratados continuam sendo considerados dados pessoais sob a égide da LGPD; a medida II configura anonimização, excluindo os dados da lei (salvo reversão por meios razoáveis); e a medida III viola flagrantemente o princípio do *Privacy by Default*.
* **C)** A medida I descaracteriza os dados como pessoais, pois o hash criptográfico com salt impede a leitura direta por parte dos atacantes externos, afastando a fiscalização da ANPD.
* **D)** A medida II configura pseudonimização imperfeita, uma vez que algoritmos de ruído matemático nunca possuem validade perante as diretrizes da LGPD.
* **E)** A medida III é juridicamente válida e recomendável pelo *Privacy by Default*, tendo em vista que desonera o usuário da tarefa manual de consentir explicitamente.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A medida I não é anonimização, e sim pseudonimização. Na pseudonimização, a associação com a pessoa física continua existindo por meio da chave/tabela que os auditores mantêm no repositório seguro. O dado continua sob o regime da LGPD.
> - **B)** **Correta.** A medida I descreve com exatidão a pseudonimização (Art. 13, § 4º), na qual o dado perde a associação direta senão pelo uso de informação adicional mantida em ambiente controlado, continuando a ser considerado dado pessoal. A medida II atende aos critérios do Art. 12 da LGPD para anonimização (não identificável por meios técnicos razoáveis e disponíveis), deixando de ser dado pessoal. A medida III viola frontalmente o *Privacy by Default*, que proíbe caixas pré-marcadas (*opt-in* forçado) e compartilhamentos indiscriminados.
> - **C)** Incorreta. O hash criptográfico, mesmo com salt, não descaracteriza o dado pessoal de forma absoluta perante a LGPD, pois o controlador detém a chave para reverter ou associar os registros. Trata-se de pseudonimização.
> - **D)** Incorreta. A injeção de ruído laplaciano (Privacidade Diferencial) e o k-anonimato são métodos formais robustos e internacionalmente reconhecidos de anonimização matemática aceitos pela doutrina e pelos órgãos reguladores.
> - **E)** Incorreta. A inclusão de checkboxes pré-marcados (*pre-ticked boxes*) é o oposto do *Privacy by Default*. A regra mandatória é que as opções mais restritivas de privacidade venham ativadas por padrão, exigindo ação positiva e consciente do usuário para qualquer flexibilização.
> 
> **Gabarito: B**

---



### 1.2 Agentes de Tratamento e o Encarregado (DPO)

1. **Titular:** A pessoa natural (física) viva a quem se referem os dados pessoais que são objeto de tratamento. Pessoas jurídicas **não** são titulares de dados sob a LGPD.
2. **Controlador (Art. 5º, VI):** Pessoa natural ou jurídica, de direito público ou privado, a quem competem as **decisões** essenciais referentes ao tratamento de dados pessoais (ex.: Tribunal de Contas, Secretaria de Fazenda, empresa pública).
3. **Operador (Art. 5º, VII):** Pessoa natural ou jurídica, de direito público ou privado, que realiza o tratamento de dados pessoais **em nome do controlador** (ex.: empresa contratada de hospedagem em nuvem, fábrica de software terceirizada, consultoria de sustentação de banco de dados). O operador deve agir estritamente conforme as instruções lícitas do controlador.
4. **Encarregado / Data Protection Officer - DPO (Art. 5º, VIII):** Pessoa indicada pelo controlador e operador para atuar como canal de comunicação entre o controlador, os titulares dos dados e a Autoridade Nacional de Proteção de Dados (ANPD).
    - Suas atividades incluem: receber reclamações e comunicações dos titulares, prestar esclarecimentos, receber notificações da ANPD e orientar os colaboradores da entidade sobre as práticas de proteção de dados.
    - A identidade e as informações de contato do encarregado devem ser divulgadas publicamente, de forma clara e objetiva, preferencialmente no sítio eletrônico do controlador (Art. 41, § 1º).

> 🚨 **ALERTA DE PROVA / PEGADINHA FCC:**  
> O Operador não toma decisões sobre as finalidades do tratamento. Se um provedor de nuvem contratado como Operador resolver utilizar os dados do órgão público para treinar seus próprios modelos comerciais de IA sem autorização, ele comete desvio de finalidade e passa a responder como **Controlador** em relação a esse tratamento ilícito.

---

### Teste 516
**(FGV - TJ-RR - Analista Judiciário - Governança e Gestão de TI - Adaptada)**
**Enunciado:** No contexto da Lei Geral de Proteção de Dados Pessoais (LGPD - Lei nº 13.709/2018), a definição dos papéis dos agentes de tratamento e do encarregado é essencial para estabelecer responsabilidades jurídicas e arquiteturais em sistemas informatizados. Acerca do Controlador, do Operador e do Encarregado (DPO), assinale a afirmativa correta:  

* **A)** O Controlador é a pessoa natural ou jurídica responsável por executar o tratamento estritamente sob as ordens do Operador, sem qualquer poder deliberativo sobre a finalidade dos dados.
* **B)** O Operador decide monocraticamente as bases legais e as finalidades institucionais do tratamento, atuando como o titular patrimonial dos dados.
* **C)** O Encarregado (DPO) tem a responsabilidade exclusiva de indenizar os titulares em caso de vazamento ilícito de dados perpetrado por hackers.
* **D)** O Controlador compete as decisões referentes ao tratamento de dados pessoais; o Operador realiza o tratamento em nome do controlador e segundo suas diretrizes; e o Encarregado atua como canal de comunicação entre o controlador, os titulares dos dados e a ANPD.
* **E)** O papel de Encarregado pelo tratamento de dados pessoais só pode ser desempenhado por servidores públicos federais da carreira policial, vedada a indicação de terceirizados ou pessoas jurídicas.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O Controlador é quem toma as decisões sobre o tratamento (finalidades e meios essenciais); o Operador é quem executa as ordens.
> - **B)** Incorreta. O Operador apenas processa os dados em nome do Controlador e conforme suas instruções contratuais.
> - **C)** Incorreta. A responsabilidade civil de indenização recai sobre os agentes de tratamento (Controlador e Operador), não pessoalmente sobre o DPO no exercício regular de suas funções orientadoras.
> - **D)** **Correta.** Definição literal da LGPD (Art. 5º, incisos VI, VII e VIII): Controlador: a quem competem as decisões; Operador: quem realiza o tratamento em nome do controlador; Encarregado: pessoa indicada para atuar como canal de comunicação entre controlador, titulares e ANPD.
> - **E)** Incorreta. O DPO pode ser pessoa natural ou jurídica, integrante do quadro próprio ou contratado externo (*DPO as a Service*).
> 
> **Gabarito: D**




---


## 2. Princípios do Art. 6º sob a Ótica da Arquitetura e Engenharia de Software

O Art. 6º da LGPD elenca dez princípios fundamentais que regem as atividades de tratamento. Para desenvolvedores, arquitetos e DBAs, esses princípios se traduzem em requisitos não funcionais diretos:

1. **Finalidade:** Realização do tratamento para propósitos legítimos, específicos, explícitos e informados ao titular, sem possibilidade de tratamento posterior de forma incompatível.
    - *Impacto em TI:* Cada campo persistido na tabela do banco de dados deve ter uma justificativa funcional rastreável. Não é permitido criar rotinas de coleta de dados genéricos sob a premissa de "podemos precisar disso no futuro".

2. **Adequação:** Compatibilidade do tratamento com as finalidades informadas ao titular.
    - *Impacto em TI:* Se o cadastro foi feito para emissão de certidão negativa de débitos fiscais, o sistema não pode enviar newsletters promocionais ou compartilhar dados com empresas privadas sem base legal.

3. **Necessidade (Minimização de Dados):** Limitação do tratamento ao mínimo necessário para a realização de suas finalidades, com abrangência dos dados pertinentes, proporcionais e não excessivos.
    - *Impacto em TI:* Se uma API precisa apenas validar a maioridade do usuário, ela deve receber um booleano `maior_de_idade: true/false` ou a idade calculada, e não o RG completo, filiação e certidão de nascimento digitalizada.

4. **Livre Acesso:** Garantia aos titulares de consulta facilitada e gratuita sobre a forma e a duração do tratamento, bem como sobre a integralidade de seus dados pessoais.
    - *Impacto em TI:* Criação de painéis de autoatendimento (*self-service privacy portals*) e endpoints de leitura de perfil.

5. **Qualidade dos Dados:** Garantia de exatidão, clareza, relevância e atualização dos dados.
    - *Impacto em TI:* Implementação de rotinas de validação de esquemas (JSON Schema, constraints de integridade), deduplicação de registros e mecanismos para retificação de dados incorretos pelo próprio titular.

6. **Transparência:** Garantia de informações claras, precisas e facilmente acessíveis sobre a realização do tratamento e os respectivos agentes de tratamento.
    - *Impacto em TI:* Políticas de privacidade com redação clara em microcopy nos formulários, registros de consentimento (*consent logs*) e termos versionados.

7. **Segurança:** Utilização de medidas técnicas e administrativas aptas a proteger os dados pessoais de acessos não autorizados e de situações acidentais ou ilícitas.
    - *Impacto em TI:* Criptografia de dados em trânsito (TLS 1.3) e em repouso (AES-256 com chaves gerenciadas por HSM/KMS), RBAC/ABAC, mTLS em microserviços e proteção contra injeções (OWASP Top 10).

8. **Prevenção:** Adoção de medidas prévias para evitar a ocorrência de danos em virtude do tratamento de dados pessoais.
    - *Impacto em TI:* Auditorias contínuas de código (SAST/DAST), modelagem de ameaças e esteiras DevSecOps com bloqueio de deploy em caso de vazamento de segredos em repositórios.

9. **Não Discriminação:** Impossibilidade de realização do tratamento para fins discriminatórios ilícitos ou abusivos.
    - *Impacto em TI:* Validação ética e técnica de modelos de Machine Learning para evitar viés algorítmico (*bias*) em sistemas de concessão de créditos tributários ou triagens fiscais.

10. **Responsabilização e Prestação de Contas (Accountability):** Demonstração da eficácia das medidas adotadas pelo agente.
    - *Impacto em TI:* Trilhas de auditoria imutáveis (*audit trails* / logs assinados digitalmente), relatórios de impacto à proteção de dados (RIPD/DPIA) e documentação de arquitetura de dados.

> 🚨 **ALERTA DE PROVA / PEGADINHA FCC:**  
> No setor público (Art. 23), para desempenhar competências legais e executar políticas públicas, **não se exige consentimento** do titular. A FCC adora afirmar que órgãos de fiscalização precisam de autorização do cidadão auditado para processar seus dados cadastrais. **ERRADO!** O tratamento funda-se no cumprimento de obrigação legal (Art. 7º, II) e exercício regular de direitos (Art. 7º, VI).

---

### Teste 517
**(FCC - Analista de Sistemas / Engenharia de Software - Adaptada)**
**Enunciado:** O Artigo 6º da LGPD estabelece dez princípios fundamentais que regem as atividades de tratamento de dados pessoais. Sob a ótica da Engenharia de Software e da Arquitetura de Dados, o princípio da **Necessidade** (também denominado princípio da **Minimização de Dados**) impõe que os sistemas corporativos:  

* **A)** Devem coletar a maior quantidade possível de dados pessoais e biometrias em formulários públicos, mesmo sem utilidade atual, prevendo eventuais demandas futuras de machine learning.
* **B)** Devem limitar o tratamento ao mínimo necessário para a realização de suas finalidades específicas, abrangendo apenas dados pertinentes, proporcionais e não excessivos em relação aos objetivos do serviço.
* **C)** Estão autorizados a manter permanentemente em tabelas de log o histórico de senhas em texto puro de todos os usuários cadastrados.
* **D)** Devem conceder privilégios irrestritos de administrador de banco de dados (DBA) a todos os desenvolvedores juniores e fornecedores terceirizados.
* **E)** Devem publicar automaticamente no Portal de Transparência os dados bancários e exames de saúde privados dos servidores públicos.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A coleta especulativa de dados sem utilidade imediata viola frontalmente o princípio da necessidade/minimização e da finalidade.
> - **B)** **Correta.** Conforme o Art. 6º, III, da LGPD, o princípio da necessidade determina a limitação do tratamento ao mínimo necessário para a realização de suas finalidades, com abrangência dos dados pertinentes, proporcionais e não excessivos em relação aos objetivos do tratamento.
> - **C)** Incorreta. Gravar senhas em texto puro viola gravemente os princípios de segurança e prevenção (Art. 6º, VII e VIII).
> - **D)** Incorreta. A concessão excessiva de privilégios contraria o princípio do privilégio mínimo (*least privilege*) e da segurança.
> - **E)** Incorreta. Dados de saúde são dados pessoais sensíveis e sigilosos, cuja exposição indevida acarreta ilicitude severa.
> 
> **Gabarito: B**




---


## 3. Privacy by Design e Privacy by Default (Ann Cavoukian)

Concebida no final da década de 1990 pela Comissária de Informação e Privacidade de Ontário (Canadá), Dra. Ann Cavoukian, a metodologia de **Privacy by Design (PbD)** prescreve que a privacidade não pode ser um adendo tardio adicionado ao final do desenvolvimento; ela deve ser o alicerce desde a primeira linha de arquitetura.

### 3.1 Os 7 Princípios Fundamentais do Privacy by Design

```mermaid
flowchart LR
    subgraph PBD_7["Os 7 Princípios Fundamentais do Privacy by Design"]
        direction TB
        P1["1. Proativo, não reativo; preventivo, não corretivo"]
        P2["2. Privacidade como configuração padrão (Privacy by Default)"]
        P3["3. Privacidade incorporada ao design da arquitetura"]
        P4["4. Funcionalidade Total: Soma Positiva (Ganho-Ganho, sem trade-offs)"]
        P5["5. Segurança de Ponta a Ponta: Proteção em todo o Ciclo de Vida"]
        P6["6. Visibilidade e Transparência: Manter sistemas abertos e auditáveis"]
        P7["7. Respeito pela Privacidade do Usuário: Centrado no Titular"]
    end
```

1. **Proativo e não reativo; Preventivo e não corretivo:** O sistema antecipa os riscos de violação de privacidade antes que aconteçam, aplicando modelagem de ameaças à privacidade (LINDDUN) antes da codificação.
2. **Privacidade como Padrão (Privacy by Default):** Se o titular do dado não fizer nenhuma alteração nas configurações, o nível de privacidade permanece o mais restritivo possível.
    - Checkboxes de consentimento desmarcadas por padrão;
    - Coleta de dados estritamente necessária ativada; dados opcionais desativados;
    - Cookies de rastreamento de terceiros bloqueados por padrão.

3. **Privacidade Incorporada ao Design:** A proteção da privacidade é uma funcionalidade essencial do núcleo do software e da infraestrutura, não um remendo (*patch*) colocado sobre uma arquitetura insegura.
4. **Funcionalidade Total (Soma Positiva - *Positive-Sum, not Zero-Sum*):** Rejeita a falsa dicotomia de que "ou temos privacidade, ou temos segurança/desempenho". A arquitetura de software de excelência entrega alta performance, segurança robusta **e** respeito irrestrito à privacidade.
5. **Segurança de Ponta a Ponta (Proteção em Todo o Ciclo de Vida):** A segurança cobre a informação desde a coleta inicial, trânsito, processamento, armazenamento, backup até o expurgo definitivo e seguro (*crypto-shredding* ou destruição física da mídia).
6. **Visibilidade e Transparência:** Todas as partes operacionais e políticas devem permanecer transparentes e verificáveis, assegurando que o que foi prometido nos termos seja exatamente o que os algoritmos executam em produção.
7. **Respeito pela Privacidade do Usuário:** O sistema é centrado no usuário (*user-centric*). Oferece padrões de usabilidade claros, sem padrões obscuros (*dark patterns*) voltados a ludibriar o titular a compartilhar dados indesejados.

---

### Teste 518
**(FCC - Técnico de Controle Externo / Tecnologia da Informação)**
**Enunciado:** Durante o desenvolvimento de um aplicativo mobile para consulta de processos pelos cidadãos, o time de engenharia de software decide implementar as diretrizes de *Privacy by Design* formuladas por Ann Cavoukian. Ao tratar do princípio da "Funcionalidade Total" (*Full Functionality: Positive-Sum, not Zero-Sum*), a equipe deve adotar como premissa:  

* **A)** A privacidade dos titulares de dados deve ser sacrificada sempre que houver necessidade de aumentar o desempenho e a vazão de requisições por segundo na API do Tribunal.
* **B)** A segurança da informação e a privacidade dos dados pessoais devem ser acomodadas sem concessões mútuas, demonstrando que é perfeitamente viável atingir alto nível de proteção à privacidade juntamente com excelente desempenho e integridade funcional.
* **C)** O desenvolvimento deve adotar uma abordagem de jogo de soma zero, na qual a comodidade do usuário e a proteção de dados são objetivos necessariamente excludentes.
* **D)** As funcionalidades voltadas à segurança criptográfica devem ser desabilitadas em horários de pico operacional para garantir a responsividade da interface gráfica.
* **E)** Os princípios de privacidade devem ser implementados exclusivamente após a homologação final do software em ambiente de produção.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Contraria a essência da soma positiva, pois prega o sacrifício da privacidade em troca de ganho de desempenho (mentalidade de soma zero).
> - **B)** **Correta.** O princípio 4 do *Privacy by Design* (Funcionalidade Total: Soma Positiva) busca satisfazer todos os objetivos legítimos em um modelo "ganha-ganha" (*win-win*), rejeitando a falsa dicotomia de que a privacidade compete destrutivamente com a segurança, usabilidade ou desempenho.
> - **C)** Incorreta. O princípio prega explicitamente a superação do jogo de soma zero (*not Zero-Sum*). Não se admite a escolha de um em detrimento de outro.
> - **D)** Incorreta. Desabilitar a segurança criptográfica para reduzir latência viola tanto o princípio da funcionalidade total quanto o princípio da segurança de ponta a ponta.
> - **E)** Incorreta. Implementar privacidade apenas após a homologação viola o princípio fundante de que a privacidade deve ser proativa e incorporada desde o design arquitetural inicial (Princípios 1 e 3).
> 
> **Gabarito: B**

---



### 3.2 Comparativo: Privacy by Design vs. Privacy by Default

| Dimensão | Privacy by Design (PbD) | Privacy by Default (PbDf) |
|---|---|---|
| **Escopo** | Holístico, arquitetural e metodológico. Abrange toda a esteira de engenharia de software e processos organizacionais. | Focado na experiência de usuário, parametrização padrão de interfaces, bancos e sistemas operacionais. |
| **Momento de Aplicação** | Desde a concepção dos requisitos de negócio e arquitetura de software (Fase 0). | No momento em que o sistema ou serviço é disponibilizado para uso pelo usuário final. |
| **Ação Exigida do Usuário** | Nenhuma (é interno à engenharia de software). | Zero esforço: a proteção máxima já está ativa sem que o usuário precise alterar nenhuma chave ou configuração. |
| **Exemplo Típico** | Armazenamento de dados pessoais em tabelas segregadas com criptografia em repouso e trilhas de log imutáveis. | Perfil público de novo usuário criado como "Privado" por padrão; geolocalização desativada inicialmente. |

---

### Teste 519
**(FCC - Técnico de Controle Externo / TI - Adaptada)**
**Enunciado:** Na implementação dos conceitos de Proteção de Dados desde a Concepção (*Privacy by Design*) e por Padrão (*Privacy by Default*), a equipe de desenvolvimento de software de um Tribunal de Contas deve adotar padrões arquiteturais restritivos nativos. A respeito da regra do *Privacy by Default*, assinale a afirmativa correta:  

* **A)** O sistema deve ser configurado para que, por padrão de fábrica (*out-of-the-box*), as configurações mais protetivas à privacidade sejam ativadas automaticamente, exigindo ação deliberada do usuário caso deseje compartilhar dados adicionais.
* **B)** O sistema deve vir de fábrica com todos os compartilhamentos de dados públicos e autorizações de cookies de rastreamento habilitados compulsoriamente.
* **C)** O *Privacy by Default* veda expressamente a implementação de qualquer mecanismo de criptografia em trânsito ou repouso.
* **D)** A privacidade por padrão aplica-se exclusivamente a jogos eletrônicos infantis, dispensando sua observância em sistemas governamentais ou portais do cidadão.
* **E)** O conceito determina que a documentação técnica do sistema seja destruída antes do deploy em ambiente de produção.


---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** *Privacy by Default* (privacidade por padrão) estabelece que as configurações de fábrica e o comportamento padrão da aplicação devem ser automaticamente os mais estritos em proteção à privacidade (ex.: caixas de seleção desmarcadas, menor volume de coleta, tempo de retenção mínimo e compartilhamento restrito), sem que o titular precise alterar configurações manuais para se proteger.
> - **B)** Incorreta. Caixas pré-marcadas (*opt-out* compulsório) e abertura ampla de dados violam frontalmente o Privacy by Default.
> - **C)** Incorreta. A criptografia é uma das medidas essenciais recomendadas pelo Privacy by Design e by Default.
> - **D)** Incorreta. A regra aplica-se a qualquer aplicação e sistema de tratamento de dados pessoais, especialmente no setor público.
> - **E)** Incorreta. A documentação e rastreabilidade são fundamentais para o princípio da responsabilização e prestação de contas (*accountability*).
> 
> **Gabarito: A**




---


## 4. Engenharia de Desidentificação: Anonimização vs. Pseudonimização

### 4.1 Técnicas Criptográficas de Pseudonimização

Na pseudonimização (Art. 13, § 4º da LGPD), o dado pessoal tem seu identificador direto substituído por um pseudônimo. O processo é reversível por quem possui a informação adicional mantida em ambiente segregado e seguro.

1. **Hashing Criptográfico com Salt Único:**
    - Hashing puro (`SHA-256(CPF)`) é vulnerável a ataques de dicionário e tabelas arco-íris (*rainbow tables*), pois o espaço amostral do CPF possui apenas $10^{11}$ possibilidades.
    - Deve-se utilizar Salt aleatório de alta entropia por registro e chaves secretas (HMAC):
     $$\text{Pseudônimo} = \text{HMAC-SHA256}(\text{ChaveSecreta}, \text{CPF} \parallel \text{Salt})$$
2. **Tokenização:** Substituição de dados sensíveis (ex.: número de cartão de crédito, CPF) por um identificador não algorítmico gerado aleatoriamente (Token UUID). O mapeamento (*token vault*) é protegido em banco de dados isolado com controle rigoroso de acesso e mTLS.
3. **Criptografia Reversível Preservadora de Formato (FPE - Format-Preserving Encryption):** Criptografa o dado mantendo o mesmo tamanho e tipo (ex.: CPF de 11 dígitos continua gerando uma string de 11 dígitos numéricos), viabilizando testes em sistemas legados sem quebrar restrições de esquema.

---

### Teste 520
**(FCC - Auditor Estadual de Controle Externo / TI - Adaptada)**
**Enunciado:** A LGPD distingue formalmente os institutos da Anonimização e da Pseudonimização no ciclo de vida de desenvolvimento e análise de dados. Sob o ponto de vista criptográfico e de segurança da informação, assinale a afirmativa correta sobre a Pseudonimização:  

* **A)** O dado pseudonimizado é aquele que perdeu definitiva e irreversivelmente qualquer possibilidade de associação direta ou indireta a um indivíduo, deixando de ser considerado dado pessoal para todos os efeitos da LGPD.
* **B)** A pseudonimização é o tratamento por meio do qual um dado perde a possibilidade de associação, direta ou indireta, a um indivíduo, senão pelo uso de informação adicional mantida separadamente pelo controlador em ambiente seguro e controlado.
* **C)** A aplicação de algoritmo de hash MD5 simples sem *salt* em uma coluna de CPF garante a anonimização irreversível e absoluta da base de dados.
* **D)** Os dados pseudonimizados deixam de se sujeitar à LGPD, podendo ser vendidos livremente a empresas de telemarketing.
* **E)** A pseudonimização exige a destruição física dos discos rígidos e fitas de backup do data center a cada transação bancária.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Essa é a definição de dado **anonimizado** (Art. 12 da LGPD). O dado pseudonimizado continua sendo dado pessoal e sujeito integralmente à LGPD, pois pode ser reidentificado com a chave/informação adicional.
> - **B)** **Correta.** Definição legal do Art. 13, § 4º da LGPD: pseudonimização é o tratamento por meio do qual um dado perde a possibilidade de associação a um indivíduo, senão pelo uso de informação adicional mantida separadamente pelo controlador em ambiente seguro e controlado.
> - **C)** Incorreta. Hash sem *salt* em domínios finitos (como CPF) é vulnerável a ataques de tabela *rainbow* e quebra por força bruta trivial, não configurando anonimização robusta.
> - **D)** Incorreta. Dados pseudonimizados continuam sob o escopo pleno da LGPD e gozam de todas as garantias legais.
> - **E)** Incorreta. A pseudonimização é técnica criptográfica lógica (como tokenização e hashing com sal segregado), sem relação com destruição de hardware.
> 
> **Gabarito: B**


---

### 4.2 Métricas Formais de Anonimização (k-Anonymity, l-Diversity, t-Closeness e DP)

Para que um conjunto de microdados seja considerado verdadeiramente **anonimizado**, a desidentificação deve resistir a três ataques clássicos:

- **Singling out (Isolamento):** Possibilidade de isolar um registro que pertença a um único indivíduo no conjunto.
- **Linkability (Vinculação):** Possibilidade de cruzar dois conjuntos de dados distintos e correlacionar registros referentes à mesma pessoa.
- **Inference (Inferência):** Possibilidade de deduzir, com alta probabilidade, o valor de um atributo sensível de um titular a partir de outros valores.

```mermaid
flowchart TD
    subgraph METRICAS["Métricas Formais de Privacidade em Bancos de Dados"]
        K["k-Anonymity"] -->|"Resolve ataque de Isolamento nos Quase-Identificadores"| L["l-Diversity"]
        L -->|"Resolve ataque de Homogeneidade nos Atributos Sensíveis"| T["t-Closeness"]
        T -->|"Resolve vazamento de distribuição de dados sensíveis"| DP["Differential Privacy (Privacidade Diferencial)"]
        DP -->|"Injeta ruído matemático balanceado nas consultas analíticas"| FIM["Anonimização Robusta e Formal"]
    end
```

1. **k-Anonymity (Sweeney, 2002):**
    - Um conjunto de dados possui $k$-anonimato se cada tupla de **quase-identificadores** (ex.: Idade, Gênero, CEP) for indistinguível de pelo menos outras $k-1$ tuplas no mesmo conjunto. Ou seja, cada grupo de equivalência contém no mínimo $k$ registros.
    - *Limitação:* Não protege contra o ataque de **homogeneidade**. Se em um grupo com $k=5$, todos os 5 indivíduos tiverem o atributo sensível "Tuberculose Pulmonar", qualquer pessoa que saiba que a vítima está naquele grupo descobrirá sua doença com 100% de certeza.

2. **l-Diversity (Machanavajjhala et al., 2007):**
    - Extensão do $k$-anonimato que exige que, dentro de cada grupo de equivalência de quase-identificadores, existam pelo menos $l$ valores "bem representados" para cada atributo sensível, superando o ataque de homogeneidade.

3. **t-Closeness (Li et al., 2007):**
    - Exige que a distribuição de probabilidade de um atributo sensível dentro de qualquer grupo de equivalência tenha uma distância estatística de no máximo $t$ em relação à distribuição desse mesmo atributo em todo o banco de dados global.

4. **Privacidade Diferencial ($\epsilon$-Differential Privacy - Dwork, 2006):**
    - Padrão-ouro na computação moderna. Garante matematicamente que a inclusão ou remoção de um único indivíduo no banco de dados não altera significativamente a probabilidade do resultado de uma consulta analítica agregada.
    - Injeta ruído aleatório calibrado (distribuição de Laplace ou Gaussiana) controlado pelo parâmetro de privacidade $\epsilon$ (*privacy budget*).

---

### Teste 521
**(FCC - Auditor Estadual de Controle Externo / Tecnologia da Informação)**
**Enunciado:** Em relação às técnicas computacionais de proteção à privacidade aplicadas à publicação de microdados e aos algoritmos de anonimização sob a ótica da segurança da informação, analise o seguinte cenário:  
Um analista aplicou generalização de atributos (faixas etárias e agrupamento de CEP) para garantir que cada registro em uma tabela médica publicada por uma Secretaria Estadual de Saúde seja indistinguível de pelo menos outros quatro registros em relação aos atributos quase-identificadores. No entanto, dentro de determinado grupo de equivalência contendo 5 registros idênticos nos quase-identificadores, todos os 5 registros possuem exatamente o mesmo valor sensível no diagnóstico médico: "Tuberculose Pulmonar".  
Com base nos conceitos teóricos de anonimização, esse conjunto de dados:  

* **A)** Satisfaz a métrica de 5-anonimato (k-anonymity com k=5), mas falha em relação à métrica de l-diversidade (l-diversity), ficando vulnerável ao ataque de homogeneidade.
* **B)** Falha tanto no k-anonimato quanto na privacidade diferencial, pois para k-anonimato ser satisfeito é obrigatório que haja diversidade em todos os campos do registro.
* **C)** Garante privacidade diferencial perfeita com epsilon igual a zero.
* **D)** Satisfaz plenamente a métrica de t-closeness, eliminando qualquer risco de reidentificação por inferência.
* **E)** Enquadra-se como dado pseudonimizado com chave simétrica AES-GCM.


---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** A propriedade de $k$-anonimato ($k=5$) exige apenas que cada combinação de quase-identificadores apareça em pelo menos $k$ tuplas (o que ocorreu, pois há 5 registros indistinguíveis). Porém, como todos os indivíduos do grupo têm exatamente o mesmo diagnóstico ("Tuberculose Pulmonar"), não há diversidade de valores sensíveis ($l=1$), o que permite a um atacante com conhecimento de que o alvo está no grupo descobrir sua doença sem incerteza (ataque de homogeneidade). A métrica de $l$-diversity foi violada.
> - **B)** Incorreta. O $k$-anonimato não falhou; ele foi satisfeito quanto aos quase-identificadores ($k=5$). O erro está em não prover $l$-diversidade no atributo sensível.
> - **C)** Incorreta. Privacidade diferencial com $\epsilon = 0$ exigiria ruído infinito (o resultado da consulta seria puramente ruído aleatório sem qualquer utilidade analítica). O cenário trata de generalização de quase-identificadores, não de diferencial privacy.
> - **D)** Incorreta. A métrica de $t$-closeness exige que a distribuição do atributo no bloco se aproxime da distribuição global. Se globalmente a incidência de tuberculose é 1% e no bloco é 100%, a distância $t$ é máxima, logo a $t$-closeness é violada.
> - **E)** Incorreta. O procedimento realizado foi generalização/supressão em microdados estatísticos para tentativa de anonimização, não criptografia simétrica de payload (AES-GCM).
> 
> **Gabarito: A**



---


## 5. Implementação Técnica dos Direitos dos Titulares (Art. 18 da LGPD)

### 5.1 Mapeamento dos Direitos e Requisitos Técnicos

```mermaid
sequenceDiagram
    autonumber
    actor T as Titular dos Dados
    participant API as API Gateway / Portal de Privacidade
    participant IAM as Auth & Identity (Gov.br)
    participant SEC as Serviço de Direitos LGPD
    participant DB as Bancos Operacionais
    participant AUD as Trilha de Auditoria (Logs)

    T->>API: POST /api/v1/privacidade/direitos (Pedido de Eliminação)
    API->>IAM: Autenticação Segura (Nível Prata/Ouro)
    IAM-->>API: Token JWT Válido
    API->>SEC: Encaminha Requisição do Titular
    SEC->>SEC: Valida Base Legal (Art. 7º e Art. 16: há dever legal de guarda?)
    alt Há Obrigação Legal / Auditoria Fiscal (Art. 16, I)
        SEC-->>T: Rejeição Justificada da Eliminação (Retenção Mandatória de Contas)
    else Tratamento Baseado em Consentimento Revogado
        SEC->>DB: Executa Expurgo Seguro (Soft Delete + Crypto-shredding)
        SEC->>AUD: Registra Ação na Trilha de Auditoria com Hash
        SEC-->>T: Confirmação de Exclusão Definitiva dos Dados Pessoais
    end
```

1. **Confirmação e Acesso aos Dados (Art. 18, I e II):** Endpoint `GET /api/v1/titular/meus-dados` que consolida em uma única visão todos os dados cadastrais e transacionais associados ao titular.
2. **Correção de Dados Incompletos, Inexatos ou Desatualizados (Art. 18, III):** Endpoint `PUT /api/v1/titular/perfil` com replicação assíncrona para bases de réplica e filas de mensageria (Kafka/RabbitMQ).
3. **Anonimização, Bloqueio ou Eliminação de Dados Desnecessários (Art. 18, IV):** Rotinas de *Data Lifecycle Management* (DLM) em cron jobs de expurgo.
4. **Portabilidade dos Dados (Art. 18, V):** Geração assíncrona de arquivos em formato aberto e legível por máquina (JSON, CSV ou XML) disponibilizados via link pré-assinado temporário.
5. **Eliminação dos Dados Tratados com Consentimento (Art. 18, VI):**
    - *Soft Delete:* Marcação da flag `is_deleted = true`, acompanhada do mascaramento irreversível dos dados pessoais de identificação direta na linha do registro.
    - *Crypto-shredding:* Criptografar os dados pessoais de cada titular com uma chave individual e exclusiva ($K_{\text{titular}}$). Para executar a eliminação definitiva em todas as réplicas e backups frios (*WORM*), basta destruir a chave no KMS.
    - *Limites no Setor Público (Art. 16, I e Art. 23):* O direito de eliminação não é absoluto. O titular não pode exigir que o Tribunal de Contas apague dados fiscais e auditorias em que foi processado, pois a guarda decorre de dever legal.

---

### Teste 522
**(FCC - Analista Judiciário / Apoio Especializado / Análise de Sistemas)**
**Enunciado:** Determinado Tribunal de Justiça implementou uma solução corporativa para gerenciamento do ciclo de vida dos dados pessoais em conformidade com o Art. 18 da LGPD. Um cidadão que teve um procedimento administrativo disciplinar arquivado sem penalidades aciona o sistema solicitando a "eliminação definitiva de todos os seus dados pessoais e registros de movimentação processual dos bancos de dados do Tribunal". Diante desse cenário e das bases legais para o tratamento de dados no setor público, a conduta correta do órgão é:  

* **A)** Atender compulsoriamente à exclusão imediata e física de todos os dados do requerente, uma vez que o direito à eliminação previsto no Art. 18 é absoluto e incondicionado na esfera pública.
* **B)** Negar o pedido de eliminação quanto aos registros processuais e atos oficiais de arquivamento mantidos para cumprimento de obrigação legal ou regulatória e exercício regular de direitos em processo judicial ou administrativo, mantendo a guarda desses dados com fulcro no Art. 16 da LGPD.
* **C)** Excluir os dados apenas se o requerente pagar uma taxa de expurgo eletrônico estipulada em resolução interna do tribunal.
* **D)** Proceder à destruição física de todos os discos rígidos e backups magnéticos do Tribunal que contenham menção ao nome do titular.
* **E)** Transferir a guarda dos dados para uma empresa de tecnologia privada sediada no exterior a fim de eximir o Tribunal da responsabilidade civil.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O direito à eliminação (Art. 18, VI) não é absoluto. O Art. 16 da LGPD prevê expressamente as hipóteses em que os dados devem ou podem ser conservados mesmo após o término do tratamento ou a pedido do titular: cumprimento de obrigação legal ou regulatória pelo controlador (inciso I), estudo por órgão de pesquisa (inciso II), transferência a terceiro permitida pela lei (inciso III) ou uso exclusivo do controlador sob anonimização (inciso IV).
> - **B)** **Correta.** Os autos processuais e registros administrativos de órgãos públicos são protegidos por deveres de custódia documental (legislação arquivística e de controle externo) e pelo exercício regular de direitos. Portanto, a exclusão física solicitada pelo titular deve ser negada com a devida justificativa legal fundamentada no Art. 16, I da LGPD.
> - **C)** Incorreta. O Art. 18 estabelece que o exercício dos direitos pelo titular perante o controlador é gratuito (Art. 18, § 5º). É expressamente vedada a cobrança de taxas.
> - **D)** Incorreta. A destruição física indiscriminada de infraestrutura de hardware é absurda e violaria o princípio da continuidade do serviço público e da custódia do patrimônio documental.
> - **E)** Incorreta. Transferir dados para terceiros no exterior para burlar a lei é ilegal, contraria os princípios da boa-fé, segurança e responsabilização, além de violar as regras de transferência internacional de dados (Art. 33 da LGPD).
> 
> **Gabarito: B**

---



### 5.2 Comunicação de Incidentes de Segurança à ANPD e Titulares (Art. 48)

O Art. 48 da LGPD determina que o **Controlador** deve comunicar à Autoridade Nacional de Proteção de Dados (ANPD) e aos titulares a ocorrência de incidente de segurança que **possa acarretar risco ou dano relevante aos titulares**:

- A comunicação deve ocorrer em **prazo razoável** (definido pela Resolução CD/ANPD nº 15/2024 em **3 dias úteis** contados do conhecimento do fato).
- A notificação deve detalhar:
    1. A natureza e a categoria dos dados pessoais afetados;
    2. As informações sobre os titulares envolvidos;
    3. As medidas técnicas e de segurança utilizadas para proteção dos dados;
    4. Os riscos relacionados ao incidente;
    5. As medidas tomadas ou que serão adotadas para reverter ou mitigar os efeitos do prejuízo.

- A ANPD poderá determinar ao controlador a ampla divulgação do fato nos meios de comunicação caso considere relevante.

---

### Teste 523
**(FCC - Analista de Gestão e Tecnologia / Segurança da Informação)**
**Enunciado:** Uma autarquia pública estadual sofreu um incidente de segurança cibernética consistente na exfiltração não autorizada da base de dados de seus servidores efetivos, contendo dados bancários, endereços residenciais e senhas criptografadas em hash MD5 sem salt. De acordo com o Art. 48 da Lei nº 13.709/2018 (LGPD) e a regulamentação expedida pela ANPD sobre a matéria:  

* **A)** O controlador deve comunicar à Autoridade Nacional de Proteção de Dados (ANPD) e aos titulares a ocorrência de qualquer incidente de segurança, ainda que insignificante e desprovido de qualquer risco aos direitos dos titulares.
* **B)** A comunicação de incidentes à ANPD e aos titulares é obrigatória quando o evento de segurança puder acarretar risco ou dano relevante aos titulares, devendo ser realizada em prazo razoável e descrever, entre outros pontos, a natureza dos dados afetados e as medidas de mitigação adotadas.
* **C)** A responsabilidade pela comunicação recai unicamente sobre o Operador contratado que hospedava o servidor, ficando o Controlador isento de qualquer obrigação perante a ANPD.
* **D)** A autarquia está dispensada de comunicar o fato se publicar uma nota genérica de desculpas em sua conta institucional em redes sociais em até 90 dias úteis.
* **E)** A ANPD não possui competência legal para determinar a divulgação do fato à imprensa caso o controlador decida manter o sigilo absoluto do vazamento.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O Art. 48 estabelece o dever de comunicação quando o incidente "possa acarretar risco ou dano relevante aos titulares". Incidentes triviais sem qualquer risco ou afetação a direitos não demandam comunicação formal obrigatória à ANPD e aos titulares.
> - **B)** **Correta.** O Art. 48 da LGPD determina: "O controlador deverá comunicar à autoridade nacional e ao titular a ocorrência de incidente de segurança que possa acarretar risco ou dano relevante aos titulares." A comunicação deve conter a natureza dos dados, informações sobre os titulares envolvidos, medidas técnicas adotadas para proteção e medidas para reverter ou mitigar os efeitos do prejuízo.
> - **C)** Incorreta. A obrigação legal de notificação à ANPD e aos titulares é do Controlador (Art. 48). O Operador tem o dever de notificar imediatamente o Controlador sobre a ocorrência do incidente, mas não assume o papel perante a ANPD e o público.
> - **D)** Incorreta. Publicar nota em rede social após 90 dias não atende à exigência legal de comunicação tempestiva em prazo razoável (estipulado pela Resolução CD/ANPD nº 15/2024 em 3 dias úteis a partir do conhecimento do incidente grave) e dirigida aos canais formais.
> - **E)** Incorreta. O Art. 48, § 2º da LGPD confere expressamente à ANPD o poder de determinar a ampla divulgação do fato em meios de comunicação e a adoção de medidas para mitigar seus efeitos caso constate a relevância do evento.
> 
> **Gabarito: B**

---



---

### Teste 524
**(FCC - Analista Judiciário - Segurança da Informação - Adaptada)**
**Enunciado:** Em relação à gestão de riscos de privacidade e auditoria em sistemas públicos, a LGPD prevê o Relatório de Impacto à Proteção de Dados Pessoais (RIPD / DPIA). Acerca desse instrumento e das boas práticas de segurança, assinale a afirmativa correta:  

* **A)** O RIPD é um documento de preenchimento facultativo que deve ser mantido em segredo absoluto, sendo vedado à ANPD solicitar seu compartilhamento.
* **B)** O RIPD descreve os processos de tratamento de dados pessoais que podem gerar riscos às liberdades civis e aos direitos fundamentais, bem como medidas, salvaguardas e mecanismos de mitigação de risco adotados pela organização.
* **C)** A elaboração do RIPD exime o controlador de cumprir os princípios de segurança da informação e dispensa a comunicação de incidentes de segurança cibernética.
* **D)** O RIPD é obrigatório exclusivamente para operações que envolvam dados públicos abertos sem qualquer identificador pessoal.
* **E)** Compete privativamente ao estagiário de atendimento de suporte a emissão e homologação do RIPD, sendo dispensada a participação do Encarregado (DPO).


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A ANPD pode determinar a elaboração e apresentação do RIPD a qualquer tempo para operações de maior risco ou sensibilidade (Art. 38 da LGPD).
> - **B)** **Correta.** Conforme o Art. 5º, XVII e Art. 38 da LGPD, o RIPD é a documentação do controlador que contém a descrição dos processos de tratamento que podem gerar riscos às liberdades civis e aos direitos fundamentais, bem como medidas, salvaguardas e mecanismos de mitigação de risco.
> - **C)** Incorreta. O RIPD é uma ferramenta preventiva de conformidade; ele não afasta a obrigação contínua de segurança nem a obrigação de reportar incidentes relevantes à ANPD e aos titulares.
> - **D)** Incorreta. O RIPD foca justamente em operações que tratam dados pessoais com potencial de risco aos titulares (ex.: dados sensíveis, vigilância em massa, decisões automatizadas de IA).
> - **E)** Incorreta. A elaboração do RIPD envolve os gestores de negócio, arquitetos de TI, segurança da informação e conta com a orientação e parecer consultivo obrigatório do Encarregado (DPO).
> 
> **Gabarito: B**



---


## 6. Fontes Recomendadas na Internet

* [Lei nº 13.709/2018 (Lei Geral de Proteção de Dados Pessoais - LGPD)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm) - Texto compilado da LGPD no Planalto com todas as bases legais, direitos dos titulares e deveres dos agentes de tratamento.
* [Decreto nº 9.637/2018 (Política Nacional de Segurança da Informação)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/decreto/d9637.htm) - Dispõe sobre governança de dados pessoais e segurança da informação na administração pública.
* [Governo Digital - Privacidade e Segurança da Informação](https://www.gov.br/governodigital/pt-br/privacidade-e-seguranca) - Diretrizes, guias operacionais e boas práticas de proteção de dados no setor público.
* [IETF RFC 7519 - JSON Web Token (JWT)](https://datatracker.ietf.org/doc/html/rfc7519) - Especificação técnica de tokens seguros para tráfego e proteção de dados entre sistemas.
* [OWASP Top 10 Privacy Risks Project](https://owasp.org/www-project-top-10-privacy-risks/) - Documentação oficial sobre vulnerabilidades de privacidade e controles recomendados em sistemas web.
* DONEDA, Danilo. **Da Privacidade à Proteção de Dados Pessoais: Elementos da Formação do seu Conceito**. 2. ed. São Paulo: Thomson Reuters Brasil, 2020. (Cap. 1 a 4 - Princípios Fundamentais da Proteção de Dados).
* BIONI, Bruno Ricardo. **Proteção de Dados Pessoais: A Função e os Limites do Consentimento**. 3. ed. Rio de Janeiro: Forense, 2021. (Cap. 2 - Bases Legais e Legitimo Interesse).
* PINHEIRO, Patricia Peck. **Direito Digital**. 7. ed. São Paulo: SaraivaJur, 2021. (Cap. 7 - Segurança da Informação e Compliance com a LGPD).
