# 05 - Autenticação, Identidade e Autorização: OAuth 2.0, OIDC e JWT

> **Matéria:** Desenvolvimento de Sistemas  
> **Cargo:** B02 – Técnico de Controle Externo – Especialidade: Tecnologia da Informação  
> **Arquivo:** `05_autenticacao_identidade_oauth2_oidc_jwt.md`  

---

## 📌 Ementa / Itens do Edital
- Autenticação, identidade e autorização
- Framework OAuth 2.0 (RFC 6749)
- Camada de Identidade OpenID Connect (OIDC 1.0)
- Tokens, claims e escopos
- JSON Web Token (JWT - RFC 7519)

---

## 🧭 Sumário

1. [Conceitos Fundamentais de Segurança de Acesso](#1-conceitos-fundamentais-de-seguranca-de-acesso)
    1. [Autenticação (AuthN) vs. Autorização (AuthZ)](#11-autenticacao-authn-vs-autorizacao-authz)
    2. [Fatores de Autenticação e MFA](#12-fatores-de-autenticacao-e-mfa)
    3. [Modelos de Controle de Acesso: RBAC e ABAC](#13-modelos-de-controle-de-acesso-rbac-e-abac)
    4. [Teste 098](#Teste-098)
    5. [Teste 099](#Teste-099)
2. [Framework de Autorização OAuth 2.0 (RFC 6749)](#2-framework-de-autorizacao-oauth-20-rfc-6749)
    1. [Os Quatro Papéis Fundamentais](#21-os-quatro-papeis-fundamentais)
    2. [Fluxos de Concessão (Grant Types) e Cenários de Aplicação](#22-fluxos-de-concessao-grant-types-e-cenarios-de-aplicacao)
    3. [A Extensão PKCE (RFC 7636) para Clientes Públicos](#23-a-extensao-pkce-rfc-7636-para-clientes-publicos)
    4. [Escopos (Scopes) e Autorização Granular](#24-escopos-scopes-e-autorizacao-granular)
    5. [Teste 100](#Teste-100)
    6. [Teste 101](#Teste-101)
    7. [Teste 102](#Teste-102)
    8. [Teste 103](#Teste-103)
3. [Camada de Identidade OpenID Connect (OIDC 1.0)](#3-camada-de-identidade-openid-connect-oidc-10)
    1. [Distinção Essencial: OAuth 2.0 vs. OpenID Connect](#31-distincao-essencial-oauth-20-vs-openid-connect)
    2. [Tríade de Tokens no OIDC: ID Token, Access Token e Refresh Token](#32-triade-de-tokens-no-oidc-id-token-access-token-e-refresh-token)
    3. [Endpoints Padronizados OIDC e Single Sign-On (SSO) Corporativo](#33-endpoints-padronizados-oidc-e-single-sign-on-sso-corporativo)
    4. [Teste 104](#Teste-104)
4. [JSON Web Token - JWT (RFC 7519)](#4-json-web-token-jwt-rfc-7519)
    1. [Anatomia Estrutural: Header, Payload e Signature](#41-anatomia-estrutural-header-payload-e-signature)
    2. [Claims Registradas, Públicas e Privadas](#42-claims-registradas-publicas-e-privadas)
    3. [Assinatura Digital: Algoritmos Simétricos (HS256) vs. Assimétricos (RS256)](#43-assinatura-digital-algoritmos-simetricos-hs256-vs-assimetricos-rs256)
    4. [Armazenamento Seguro de Tokens no Cliente e Mitigação de Ataques](#44-armazenamento-seguro-de-tokens-no-cliente-e-mitigacao-de-ataques)
    5. [Teste 105](#Teste-105)
    6. [Teste 106](#Teste-106)
    7. [Teste 107](#Teste-107)
5. [Quadro Comparativo Consolidado de Segurança de Acesso](#5-quadro-comparativo-consolidado-de-seguranca-de-acesso)
6. [Fontes Recomendadas na Internet](#6-fontes-recomendadas-na-internet)

---

## 1. Conceitos Fundamentais de Segurança de Acesso

### 1.1 Autenticação (AuthN) vs. Autorização (AuthZ)
A segurança em sistemas de informação modernos apoia-se na distinção categórica entre dois processos interdependentes:

```mermaid
flowchart LR
    subgraph AuthN_Flow["1. Autenticação (AuthN)"]
        A1["Usuário fornece credenciais"] --> A2["Sistema valida a identidade"]
        A2 --> A3["'Quem é você?' -> Identidade Confirmada"]
    end
    subgraph AuthZ_Flow["2. Autorização (AuthZ)"]
        B1["Usuário autenticado solicita ação"] --> B2["Sistema avalia políticas e privilégios"]
        B2 --> B3["'O que você pode fazer?' -> Acesso Concedido ou Negado"]
    end
    AuthN_Flow --> AuthZ_Flow
```

- **Autenticação (AuthN - *Authentication*):** Processo de validação e verificação inequívoca da identidade alegada por uma entidade (seja ela um usuário humano, um dispositivo ou um serviço autônomo). Responde à indagação fundamental: **"Quem é você?"**.
- **Autorização (AuthZ - *Authorization*):** Processo de determinar quais direitos, permissões e operações uma entidade **previamente autenticada** tem legitimidade para exercer sobre um recurso específico no sistema. Responde à pergunta: **"O que você tem permissão para fazer?"**.

### 1.2 Fatores de Autenticação e MFA
A robustez do processo de autenticação é medida pelo emprego de múltiplos fatores independentes (**MFA - *Multi-Factor Authentication***):

1. **Fator de Conhecimento (*Something you know*):** Informações secretas memorizadas pelo usuário (senhas alfanuméricas, códigos PIN, respostas a perguntas de segurança).
2. **Fator de Posse (*Something you have*):** Objetos físicos ou digitais sob custódia do usuário (smartcards com chip, tokens criptográficos USB/FIDO2, certificados digitais ICP-Brasil, aplicativos autenticadores geradores de senhas descartáveis baseadas em tempo — TOTP/Google Authenticator).
3. **Fator de Inerência (*Something you are*):** Características biológicas ou biométricas intrínsecas e exclusivas do indivíduo (impressão digital, reconhecimento facial 3D, geometria de íris/retina, padrão vascular).

> 🚨 **ALERTA DE PROVA / FCC:**  
> A banca costuma colocar pegadinhas afirmando que "utilizar senha e código PIN simultaneamente configura autenticação multifator". Isso é falso! Senha e PIN pertencem à **mesma categoria (conhecimento)**. O MFA exige o uso concorrente de pelo menos **duas categorias distintas de fatores** (ex.: senha + token TOTP ou biometria + certificado digital).

### 1.3 Modelos de Controle de Acesso: RBAC e ABAC
Uma vez autenticada a entidade, o subsistema de autorização aplica políticas para liberar ou vetar o acesso aos endpoints e bancos de dados:

```mermaid
flowchart TD
    subgraph ModelosAcesso["Modelos Principais de Controle de Acesso"]
        subgraph RBAC["RBAC (Role-Based Access Control)"]
            U["Usuário"] --> P["Papel / Função (Ex.: Auditor)"]
            P --> Perm["Permissões Estáticas (read:processos, sign:parecer)"]
        end
        subgraph ABAC["ABAC (Attribute-Based Access Control)"]
            Sujeito["Atributos do Sujeito (Cargo, Lotação, Vínculo)"]
            Recurso["Atributos do Recurso (Grau Sigilo, Unidade Orçamentária)"]
            Ambiente["Atributos Ambientais (IP de Origem, Horário, Geolocalização)"]
            Motor["Motor de Políticas ABAC (XACML / OPA)"]
            Sujeito --> Motor
            Recurso --> Motor
            Ambiente --> Motor
            Motor --> Decisao["Decisão Booleana em Tempo Real (Permitir / Bloquear)"]
        end
    end
```

| Critério de Comparação | RBAC (*Role-Based Access Control*) | ABAC (*Attribute-Based Access Control*) |
|---|---|---|
| **Fundamento Central** | Acesso concedido com base no **papel ou função estrutural** que o indivíduo exerce na organização (`Auditor`, `Gestor`, `Técnico`). | Acesso avaliado dinamicamente combinando múltiplos **atributos** do sujeito, do recurso, da ação pretendida e do ambiente contextual. |
| **Flexibilidade Contextual** | **Baixa**. O papel é estático e ignora variáveis temporais, geográficas ou de rede no momento da solicitação. | **Altíssima**. Permite regras condicionais refinadas (ex.: "Permitir acesso apenas se o auditor pertencer à 2ª Câmara, o processo for da sua relatoria e o acesso ocorrer em dia útil via VPN do TCE"). |
| **Complexidade de Gestão** | Sofre do problema de **explosão de papéis (*role explosion*)** quando a organização necessita de regras com granularidade muito fina. | Complexidade na escrita e no processamento computacional de políticas dinâmicas (frequentemente expressas em padrões como XACML ou OPA/Rego). |
| **Aplicação Típica** | Sistemas departamentais convencionais e portais corporativos simples. | Ambientes governamentais críticos, controle fiscal e sistemas orientados a microsserviços. |

---

## 2. Framework de Autorização OAuth 2.0 (RFC 6749)

### 2.1 Os Quatro Papéis Fundamentais
O framework OAuth 2.0 (padronizado pela IETF na **RFC 6749**) foi concebido para resolver o problema da concessão delegada de acesso, permitindo que uma aplicação terceira acesse recursos protegidos em nome do usuário **sem jamais exigir o compartilhamento de suas credenciais (login e senha)**.

1. **Resource Owner (Proprietário do Recurso):** A entidade (normalmente o usuário humano final) capaz de outorgar o acesso aos seus recursos protegidos.
2. **Client (Aplicação Cliente):** A aplicação que realiza requisições a recursos protegidos em nome do *Resource Owner*. Classifica-se em:
    - *Confidential Client (Cliente Confidencial):* Capaz de manter a confidencialidade de suas credenciais (`client_secret`), pois roda em servidores backend seguros controlados pela organização.
    - *Public Client (Cliente Público):* Incapaz de proteger um segredo criptográfico estático, pois roda no dispositivo do usuário final (SPAs em JavaScript no navegador, aplicativos móveis para Android/iOS).

3. **Authorization Server (Servidor de Autorização):** Servidor responsável por autenticar o *Resource Owner*, colher o seu consentimento expresso e emitir os tokens criptográficos de acesso (*Access Tokens*) após validação das credenciais e escopos.
4. **Resource Server (Servidor de Recursos):** O servidor que hospeda os recursos e APIs protegidos, capaz de receber, validar os tokens de acesso e responder às requisições do cliente.

### 2.2 Fluxos de Concessão (Grant Types) e Cenários de Aplicação
O OAuth 2.0 define fluxos distintos de acordo com a natureza da aplicação cliente e os requisitos de segurança:

```mermaid
flowchart TD
    subgraph EscolhaGrant["Árvore de Decisão de Fluxos OAuth 2.0 Modernos"]
        Q1{"Há usuário humano envolvido?"}
        Q1 -->|Não (Comunicação M2M / Batch)| CC["Client Credentials Grant"]
        Q1 -->|Sim| Q2{"O cliente consegue proteger um secret no backend?"}
        Q2 -->|Sim (Web App Tradicional)| AC["Authorization Code Grant"]
        Q2 -->|Não (SPA React ou App Mobile)| PKCE["Authorization Code Grant com PKCE"]
    end
```

| Fluxo (*Grant Type*) | Cenário Operacional | Nível de Segurança | Situação Normativa Atual |
|---|---|:---:|---|
| **Authorization Code** | Aplicações Web clássicas baseadas em servidor com backend seguro (*confidential clients*). | **Máximo** | Padrão recomendado pela IETF. |
| **Authorization Code com PKCE** | Clientes públicos: Single Page Applications (SPAs em React, Angular) e Apps Mobile nativos. | **Máximo** | **Obrigatório** pelas diretrizes contemporâneas (RFC 7636 e OAuth 2.1). |
| **Client Credentials** | Comunicação direta máquina-a-máquina (M2M), microsserviços internos, scripts batch e daemons sem usuário. | **Alto** | Padrão oficial para comunicação automatizada entre sistemas. |
| **Refresh Token Grant** | Renovação transparente de *Access Tokens* expirados sem requerer novo login do usuário. | **Alto** | Empregado como mecanismo complementar aos fluxos de código. |
| **Implicit Grant** | SPAs legadas nos primórdios da web, onde o token vinha diretamente exposto no fragmento da URL (`#access_token=..`). | **Vulnerável** | **DEPRECADO E PROIBIDO** no OAuth 2.1 devido a riscos de interceptação no histórico do navegador. |
| **Resource Owner Password Credentials (ROPC)** | O usuário digita suas credenciais corporativas diretamente na tela da aplicação cliente. | **Crítico** | **DEPRECADO E PROIBIDO** no OAuth 2.1 (viola a premissa central de não compartilhar senhas com clientes terceiros). |

### 2.3 A Extensão PKCE (RFC 7636) para Clientes Públicos
Em clientes públicos (como aplicações React ou apps móveis), um atacante pode registrar um esquema customizado de URI ou inspecionar o tráfego do sistema operacional para interceptar o código de autorização (`code`) retornado pelo servidor. Como o cliente público não possui um `client_secret` sigiloso, o atacante poderia trocar esse código interceptado por um *Access Token*.

A extensão **PKCE** (*Proof Key for Code Exchange*, RFC 7636) neutraliza essa ameaça através de segredos criptográficos efêmeros criados dinamicamente para cada autenticação:

```mermaid
sequenceDiagram
    autonumber
    actor Usuário
    participant Client as SPA React (Cliente Público)
    participant AS as Authorization Server
    participant API as Resource Server (API)

    Note over Client: 1. Gera code_verifier aleatório<br/>2. Calcula code_challenge = Base64URL(SHA256(verifier))
    Client->>AS: GET /authorize?response_type=code&code_challenge=..&code_challenge_method=S256
    Usuário->>AS: Autentica-se e autoriza o acesso
    AS-->>Client: Redireciona com Código Temporário (?code=AUTH_CODE)
    Client->>AS: POST /token (code=AUTH_CODE, code_verifier=SEGREDO_ORIGINAL)
    Note over AS: AS calcula SHA256(code_verifier) e compara com code_challenge registrado
    AS-->>Client: Retorna Access Token + ID Token (OIDC)
    Client->>API: GET /api/processos (Authorization: Bearer <Token>)
    API-->>Client: Dados Fiscais Protegidos
```

1. O cliente cria uma string secreta criptograficamente aleatória denominada **`code_verifier`**.
2. O cliente calcula o hash dessa string utilizando SHA-256 e o codifica em Base64URL, obtendo o **`code_challenge`**.
3. Na solicitação de autorização (`GET /authorize`), o cliente envia apenas o `code_challenge` e o método utilizado (`code_challenge_method=S256`).
4. Ao receber o código de autorização e solicitar o token (`POST /token`), o cliente envia o `code_verifier` original em texto claro.
5. O Servidor de Autorização calcula internamente o hash do `code_verifier` recebido e compara com o `code_challenge` guardado previamente. Se coincidirem, emite o token. Se um invasor tiver interceptado o `code`, não conseguirá trocá-lo por tokens porque não conhece o `code_verifier`.

### 2.4 Escopos (Scopes) e Autorização Granular
Os **escopos (*scopes*)** no OAuth 2.0 são identificadores textuais que expressam o conjunto delimitado de privilégios solicitados pela aplicação cliente ao concedente:

- Exemplos: `scope=read:processos write:processos openid email`.
- O *Resource Owner* pode consentir apenas com um subconjunto dos escopos solicitados.
- O Servidor de Recursos (API) analisa as claims de escopo presentes dentro do token de acesso para autorizar ou barrar endpoints específicos.

---

## 3. Camada de Identidade OpenID Connect (OIDC 1.0)

### 3.1 Distinção Essencial: OAuth 2.0 vs. OpenID Connect

> 🚨 **ALERTA DE PROVA / FCC:**  
> A afirmação *"OAuth 2.0 é um protocolo de autenticação"* é um dos maiores distratores em concursos públicos!
>
> - **OAuth 2.0 é exclusivamente um framework de autorização delegada.** Ele informa que uma aplicação tem autorização para consumir determinadas APIs, mas não padroniza quem é o usuário, qual o formato do token nem como consultar o perfil do usuário.
> - O **OpenID Connect (OIDC 1.0)** é uma camada de **identidade e autenticação** federada construída **sobre** o OAuth 2.0. Ele introduz o escopo obrigatório `openid` e define o padrão para emissão de um token de identidade padronizado: o **ID Token**.

```mermaid
flowchart TD
    subgraph OIDC_Stack["Camadas Arquiteturais OIDC / OAuth 2.0"]
        OIDC["<b>OpenID Connect 1.0 (Identidade / Autenticação)</b><br/>• Responde: 'Quem é o usuário logado?'<br/>• Emite: ID Token (formato obrigatório JWT)<br/>• Destinatário: Aplicação Cliente (Client)"]
        OAuth["<b>OAuth 2.0 (Autorização Delegada de APIs)</b><br/>• Responde: 'Quais permissões a aplicação possui?'<br/>• Emite: Access Token<br/>• Destinatário: Servidor de Recursos (API)"]
    end
    OIDC -->|Adiciona perfil, userInfo e ID Token sobre| OAuth
```

### 3.2 Tríade de Tokens no OIDC: ID Token, Access Token e Refresh Token

| Atributo / Dimensão | ID Token | Access Token | Refresh Token |
|---|---|---|---|
| **Norma de Origem** | OpenID Connect Core 1.0 | OAuth 2.0 (RFC 6749) | OAuth 2.0 (RFC 6749) |
| **Destinatário (*Audience*)** | A **Aplicação Cliente (*Client*)** | O **Servidor de Recursos (*Resource Server* / API)** | O **Servidor de Autorização (*Authorization Server*)** |
| **Formato Obrigatório** | **JWT (JSON Web Token)** assinado digitalmente | Não normatizado pelo OAuth 2.0 (na prática, JWT ou string opaca) | String opaca criptograficamente aleatória |
| **Finalidade Primária** | Provar que o usuário se autenticou com sucesso e fornecer seus atributos básicos de perfil (`sub`, `name`, `email`). | Credencial utilizada para autorizar chamadas às APIs e microsserviços nos cabeçalhos `Authorization: Bearer <token>`. | Credencial de longa duração utilizada para obter um novo *Access Token* quando o atual expirar, sem exigir novas credenciais do usuário. |
| **Tempo de Vida Médio** | Curto (minutos) | Curto (geralmente entre 5 e 60 minutos) | Longo (dias, semanas ou meses, com rotação de tokens) |

### 3.3 Endpoints Padronizados OIDC e Single Sign-On (SSO) Corporativo
O OpenID Connect padroniza os endpoints do Provedor de Identidade (*Identity Provider* - IdP):

- **`/.well-known/openid-configuration` (Discovery):** Endpoint público de autodescoberta que lista as capacidades do servidor, algoritmos suportados e as URLs de todos os endpoints.
- **`/authorize`:** Onde o usuário é redirecionado para realizar o login e conceder consentimento.
- **`/token`:** Onde o cliente troca o código de autorização pelos tokens de acesso e identidade.
- **`/userinfo`:** Endpoint protegido onde a aplicação cliente apresenta o *Access Token* para obter dados adicionais e detalhados do perfil do usuário autenticado.
- **Single Sign-On (SSO):** Arquitetura corporativa federada que permite ao usuário realizar login uma única vez no Provedor de Identidade (ex.: Keycloak, Microsoft Entra ID / Azure AD, Auth0) e acessar de forma transparente todos os sistemas governamentais integrados sem reinserir senhas.

---

### Teste 001
**(CEBRASPE – TRF 6ª – 2025 – Analista Judiciário - Apoio Especializado - Governança e Gestão de Tecnologia da Informação)**
A estrutura de autorização do OAuth 2.0 permite que uma aplicação obtenha acesso ilimitado a um serviço HTTP se houver token válido, mas não permite que uma aplicação de

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Incorreta.** A proposição apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A estrutura de autorização do OAuth 2.0 permite que uma aplicação obtenha acesso ilimitado a um serviço HTTP...". De acordo com a teoria em *3.1 Distinção Essencial: OAuth 2.0 vs. OpenID Connect*, oAuth 2.0 é exclusivamente um framework de autorização delegada. Ele informa que uma aplicação tem autorização para consumir determinadas APIs, mas não padroniza quem é o usuário, qual o formato do token nem como consultar o perfil do usuário.
> - **E)** **Correta.** O item está **Errado** (gabarito oficial: **E**), pois contraria a disciplina teórica aplicável.
>
> **Gabarito: E**

---

### Teste 002
**(CEBRASPE – TRF/6 – 2025 – Analista Judiciario Apoio Especializado Tecnologia Da Informacao)**
A estrutura de autorização do OAuth 2.0 permite que uma aplicação obtenha acesso ilimitado a um serviço HTTP se houver token válido, mas não permite que uma aplicação de terceiros obtenha acesso por conta própria.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Correta.** O item está **Certo**. Conforme fundamentado na seção *2.2 Fluxos de Concessão (Grant Types) e Cenários de Aplicação*, resource Owner Password Credentials (ROPC): O usuário digita suas credenciais corporativas diretamente na tela da aplicação cliente. — Crítico — DEPRECADO E PROIBIDO no OAuth 2.1 (viola a premissa central de não compartilhar senhas com clientes terceiros). Dessa forma, está plenamente correta a assertiva da banca (CEBRASPE – TRF/6/2025) ao afirmar que "A estrutura de autorização do OAuth 2.0 permite que uma aplicação obtenha acesso ilimitado a um serviço HTTP...".
> - **E)** **Incorreta.** A assertiva não incorre em erro conceitual, guardando conformidade com a teoria estudada.
>
> **Gabarito: C**

---

### Teste 003
**(FGV – TRT/13 – 2022 – Analista Judiciario Tecnologia Da Informacao)**
O protocolo de autorização OAuth 2.0 permite que aplicativos obtenham acesso limitado aos serviços HTTP. As quatro funções (roles) descritas na RFC 6749 para esse protocolo são

* **A)** protected resource, resource user, client e token server.
* **B)** access token, HTTP server, client credential e authorization broker.
* **C)** resource owner, resource server, client e authorization server.
* **D)** authorization resource, authorization code, client e token server.
* **E)** resource owner, password credential, access token e refresh token.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "protected resource, resource user, client e token server". De acordo com a teoria estudada em *3.2 Tríade de Tokens no OIDC: ID Token, Access Token e Refresh Token*, destinatário ( Audience ): A Aplicação Cliente ( Client ) — O Servidor de Recursos ( Resource Server / API) — O Servidor de Autorização ( Authorization Server ).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "access token, HTTP server, client credential e authorization broker". De acordo com a teoria estudada em *2.1 Os Quatro Papéis Fundamentais*, client (Aplicação Cliente): A aplicação que realiza requisições a recursos protegidos em nome do Resource Owner . Classifica se em.
> - **C)** **Correta.** Conforme fundamentado na seção *2.1 Os Quatro Papéis Fundamentais* deste guia, authorization Server (Servidor de Autorização): Servidor responsável por autenticar o Resource Owner , colher o seu consentimento expresso e emitir os tokens criptográficos de acesso ( Access Tokens ) após validação das credenciais e escopos. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT/13/2022) ao estabelecer que "resource owner, resource server, client e authorization server".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "authorization resource, authorization code, client e token server". De acordo com a teoria estudada em *6. Fontes Recomendadas na Internet*, iETF RFC 6749: The OAuth 2.0 Authorization Framework Papéis, fluxos de autorização (Authorization Code, Client Credentials, Refresh Token).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "resource owner, password credential, access token e refresh token". De acordo com a teoria estudada em *2.2 Fluxos de Concessão (Grant Types) e Cenários de Aplicação*, resource Owner Password Credentials (ROPC): O usuário digita suas credenciais corporativas diretamente na tela da aplicação cliente. — Crítico — DEPRECADO E PROIBIDO no OAuth 2.1 (viola a premissa central de não compartilhar senhas com clientes terceiros).
>
> **Gabarito: C**

---

## 4. JSON Web Token - JWT (RFC 7519)

### 4.1 Anatomia Estrutural: Header, Payload e Signature
O JWT (RFC 7519) é um padrão aberto compacto e autocontido (*stateless*) para transmitir com segurança informações entre partes na forma de um objeto JSON. No formato compacto serializado JWS (*JSON Web Signature*), é composto por **três seções separadas por pontos (`.`)**:

```text
[Header Base64URL] . [Payload Base64URL] . [Signature]
```

```mermaid
flowchart LR
    H["Header (JSON)<br/>{ 'alg': 'RS256', 'typ': 'JWT' }"] -->|"Base64URL"| H64["Parte 1: Header"]
    P["Payload (JSON)<br/>{ 'sub': '123', 'iss': 'tce', 'exp': .. }"] -->|"Base64URL"| P64["Parte 2: Payload"]
    H64 --> S["Assinatura Criptográfica:<br/>Hash(Header + '.' + Payload, Chave)"]
    P64 --> S
    S --> S64["Parte 3: Signature"]
```

1. **Cabeçalho (*Header*):** Especifica o tipo do token (`typ: "JWT"`) e o algoritmo de assinatura criptográfica empregado (`alg: "RS256"` ou `"HS256"`).
2. **Carga Útil (*Payload*):** Contém as **declarações (*claims*)**, que são afirmações sobre o sujeito e metadados adicionais.
3. **Assinatura (*Signature*):** Gerada pela aplicação da função criptográfica especificada no header sobre a concatenação do header codificado com o payload codificado, utilizando uma chave secreta ou privada.

> 🚨 **ALERTA DE PROVA / FCC:**  
> **Base64URL NÃO É CRIPTOGRAFIA!**  
> Um token JWS padrão garante **integridade** (o conteúdo não foi adulterado) e **autenticidade** (foi emitido por quem possui a chave), mas **NÃO fornece confidencialidade**. O Payload é meramente codificado em Base64URL; qualquer entidade que capture o token pode decodificá-lo instantaneamente e ler todos os seus campos em texto claro. Para manter o conteúdo em sigilo contra interceptadores, deve-se adotar o padrão **JWE (*JSON Web Encryption*)**.

### 4.2 Claims Registradas, Públicas e Privadas
As declarações contidas no payload classificam-se em três grupos segundo a RFC 7519:

#### Claims Registradas (*Registered Claims*)
Conjunto padronizado de chaves reservadas recomendadas para garantir interoperabilidade entre sistemas:

- **`sub` (*Subject*):** Identificador unívoco do sujeito/usuário a quem o token pertence (ex.: `"sub": "usr_9841"`).
- **`iss` (*Issuer*):** Entidade ou autoridade que emitiu o token (ex.: `"iss": "https://auth.tce.go.gov.br"`).
- **`aud` (*Audience*):** Destinatário ou aplicação para a qual o token foi emitido. Se o microsserviço receptor não constar no `aud`, deve rejeitar o token.
- **`exp` (*Expiration Time*):** Carimbo de data/hora no formato Unix Timestamp (segundos decorridos desde 01/01/1970 UTC) indicando o limite de validade do token. **Se `tempoAtual > exp`, o token é sumariamente inválido**.
- **`nbf` (*Not Before*):** Timestamp antes do qual o token não pode ser aceito para processamento.
- **`iat` (*Issued At*):** Timestamp indicando o instante exato em que o token foi criado e emitido.
- **`jti` (*JWT ID*):** Identificador exclusivo do token, frequentemente utilizado para prevenir ataques de repetição (*replay attacks*) e gerenciar revogações em listas negras (*blacklists*).

#### Claims Públicas e Privadas
- **Claims Públicas:** Nomes definidos e acordados em registros públicos da IANA ou nomes formatados como URIs para prevenir colisões de nomenclatura.
- **Claims Privadas:** Propriedades customizadas acordadas livremente entre os sistemas para tráfego de dados de negócio (ex.: `"roles": ["Auditor", "Administrador"]`, `"orgao": "TCE-GO"`).

### 4.3 Assinatura Digital: Algoritmos Simétricos (HS256) vs. Assimétricos (RS256)

```mermaid
flowchart TD
    subgraph Simetrico["1. Padrão Simétrico: HS256 (HMAC-SHA256)"]
        AS1["Servidor de Autorização"] -->|"Assina com Segredo K"| T1["JWT"]
        T1 --> RS1["Resource Server (API 1)"]
        T1 --> RS2["Resource Server (API 2)"]
        RS1 -->|"Valida com o MESMO Segredo K"| OK1["Válido"]
        RS2 -->|"Valida com o MESMO Segredo K"| OK2["Válido"]
    end
    subgraph Assimetrico["2. Padrão Assimétrico: RS256 (RSA-SHA256)"]
        AS2["Servidor de Autorização"] -->|"Assina com CHAVE PRIVADA"| T2["JWT"]
        T2 --> RS3["Resource Server (API 1)"]
        T2 --> RS4["Resource Server (API 2)"]
        AS2 -.->|"Distribui CHAVE PÚBLICA via JWKS"| RS3
        AS2 -.->|"Distribui CHAVE PÚBLICA via JWKS"| RS4
        RS3 -->|"Valida usando apenas a CHAVE PÚBLICA"| OK3["Válido"]
        RS4 -->|"Valida usando apenas a CHAVE PÚBLICA"| OK4["Válido"]
    end
```

- **HS256 (HMAC com SHA-256):** Algoritmo **simétrico**. Utiliza a mesmíssima chave secreta (*shared secret*) para assinar e para verificar a assinatura.
    - *Vulnerabilidade Arquitetural:* Todos os microsserviços que precisam validar tokens devem conhecer a chave secreta. Caso uma API periférica seja violada e a chave vaze, o invasor adquire o poder de **forjar tokens legítimos** para todo o ecossistema corporativo.
- **RS256 (RSA com SHA-256) / ES256 (ECDSA):** Algoritmo **assimétrico**.
    - O Servidor de Autorização assina o token com a sua **chave privada** (que nunca deixa seu cofre seguro de chaves).
    - Todos os servidores de recursos, APIs e clientes validam a assinatura utilizando unicamente a **chave pública**, obtida no endpoint padronizado **JWKS (*JSON Web Key Set* - `/.well-known/jwks.json`)**.
    - Mesmo que uma API receptora seja comprometida, o atacante jamais conseguirá forjar novos tokens, pois a chave pública apenas valida, não assina.

### 4.4 Armazenamento Seguro de Tokens no Cliente e Mitigação de Ataques

| Mecanismo no Navegador | Vulnerabilidade a XSS (*Cross-Site Scripting*) | Vulnerabilidade a CSRF (*Cross-Site Request Forgery*) | Recomendação de Segurança |
|---|:---:|:---:|---|
| **`localStorage` / `sessionStorage`** | **Totalmente Vulnerável**. Qualquer script malicioso injetado via XSS pode ler `localStorage.getItem("token")` e exfiltrá-lo. | Imune a CSRF (o navegador não anexa dados do localStorage automaticamente às requisições). | **Desaconselhado** para armazenamento de tokens com privilégios elevados. |
| **Cookies HTTP com Flags `HttpOnly` e `Secure`** | **Imune a roubo por XSS**. A flag `HttpOnly` bloqueia expressamente o acesso ao cookie via API JavaScript (`document.cookie`). | Suscetível a ataques de CSRF se não for configurado adequadamente. | **Altamente Recomendado**, desde que acompanhado do atributo **`SameSite=Strict`** (ou `Lax`) e tokens anti-CSRF para mitigar requisições forjadas entre sites. |

---

## 5. Quadro Comparativo Consolidado de Segurança de Acesso

| Dimensão | OAuth 2.0 | OpenID Connect (OIDC) | JWT (JWS) |
|---|---|---|---|
| **Propósito Central** | **Autorização Delegada** para APIs e microsserviços | **Identidade e Autenticação** federada de usuários | **Formato Estruturado de Token** assinado e compacto |
| **Token Principal** | *Access Token* (concede acesso aos endpoints) | *ID Token* (contém as informações do perfil do usuário) | É o formato adotado para o ID Token e geralmente para o Access Token |
| **Problema Solucionado** | Elimina a necessidade de repassar senhas para aplicações terceiras | Padroniza o Single Sign-On (SSO) e o intercâmbio de perfis | Elimina a necessidade de o backend consultar o banco de dados a cada requisição (*Stateless*) |
| **Norma Técnica** | RFC 6749 / RFC 7636 | OpenID Connect Core 1.0 | RFC 7519 / RFC 7515 |

---

---

## 6. Fontes Recomendadas na Internet

* [IETF - RFC 6749: The OAuth 2.0 Authorization Framework](https://datatracker.ietf.org/doc/html/rfc6749) - Papéis, fluxos de autorização (Authorization Code, Client Credentials, Refresh Token).
* [IETF - RFC 7636: Proof Key for Code Exchange (PKCE)](https://datatracker.ietf.org/doc/html/rfc7636) - Proteção contra interceptação de código de autorização em clientes públicos.
* [IETF - RFC 7519: JSON Web Token (JWT)](https://datatracker.ietf.org/doc/html/rfc7519) - Estrutura compacta base64url (Header, Payload, Signature) e claims registradas.
* [OpenID Connect Core 1.0 Specification](https://openid.net/specs/openid-connect-core-1_0.html) - Camada de identidade sobre OAuth 2.0 e ID Token assinado.
* [NIST SP 800-63B - Digital Identity Guidelines: Authentication](https://pages.nist.gov/800-63-3/sp800-63b.html) - Diretrizes oficiais do NIST para autenticação e gestão do ciclo de vida de tokens.
* HARDT, Dick (Ed.). **The OAuth 2.0 Authorization Protocol**. RFC 6749, Internet Engineering Task Force (IETF), 2012.
* STALLINGS, William. **Criptografia e Segurança de Redes: Princípios e Práticas**. 7. ed. São Paulo: Pearson, 2018. (Cap. 13 - Autenticação de Usuário e Protocolos de Identidade).
* CHESWICK, William R.; BELLOVIN, Steven M.; RUBIN, Aviel D. **Firewalls e Segurança na Internet**. 2. ed. Porto Alegre: Bookman, 2005. (Cap. 7 - Autenticação Distribuída e Tokens).
