# 04 - APIs RESTful, GraphQL, WebSockets e Documentação

> **Matéria:** Desenvolvimento de Sistemas  
> **Cargo:** B02 – Técnico de Controle Externo – Especialidade: Tecnologia da Informação  
> **Arquivo:** `04_apis_restful_graphql_websockets_documentacao.md`  



---


## 📌 Ementa / Itens do Edital
- Desenvolvimento de APIs RESTful
- Conceitos de GraphQL e WebSockets
- Formatos de representação de dados: JSON e XML
- Documentação de APIs com OpenAPI e Swagger

---

## 🧭 Sumário

1. [APIs RESTful e Protocolo HTTP](#1-apis-restful-e-protocolo-http)
    1. [Princípios Arquiteturais do REST (Roy Fielding)](#11-principios-arquiteturais-do-rest-roy-fielding)
    2. [O Modelo de Maturidade de Richardson](#12-o-modelo-de-maturidade-de-richardson)
    3. [Métodos HTTP: Semântica, Segurança e Idempotência](#13-metodos-http-semantica-seguranca-e-idempotencia)
    4. [Códigos de Status HTTP Essenciais em Provas](#14-codigos-de-status-http-essenciais-em-provas)
    5. [Boas Práticas no Design de URIs e Recursos RESTful](#15-boas-praticas-no-design-de-uris-e-recursos-restful)
    6. [Teste 087](#Teste-087)
    7. [Teste 088](#Teste-088)
    8. [Teste 089](#Teste-089)
    9. [Teste 090](#Teste-090)
    10. [Teste 091](#Teste-091)
2. [GraphQL: Arquitetura e Consultas Declarativas](#2-graphql-arquitetura-e-consultas-declarativas)
    1. [Motivação: Resolução de Over-fetching e Under-fetching](#21-motivacao-resolucao-de-over-fetching-e-under-fetching)
    2. [Modelo Operacional e a Schema Definition Language (SDL)](#22-modelo-operacional-e-a-schema-definition-language-sdl)
    3. [Operações Centrais: Queries, Mutations, Subscriptions e Resolvers](#23-operacoes-centrais-queries-mutations-subscriptions-e-resolvers)
    4. [Teste 092](#Teste-092)
    5. [Teste 093](#Teste-093)
3. [Protocolo WebSocket e Comunicação em Tempo Real](#3-protocolo-websocket-e-comunicacao-em-tempo-real)
    1. [Arquitetura Full-Duplex e a RFC 6455](#31-arquitetura-full-duplex-e-a-rfc-6455)
    2. [O Handshake HTTP Upgrade e os Esquemas `ws://` e `wss://`](#32-o-handshake-http-upgrade-e-os-esquemas-ws-e-wss)
    3. [Comparativo: Polling, Long-Polling, Server-Sent Events (SSE) e WebSocket](#33-comparativo-polling-long-polling-server-sent-events-sse-e-websocket)
    4. [Teste 094](#Teste-094)
    5. [Teste 095](#Teste-095)
4. [Formatos de Representação de Dados: JSON vs. XML](#4-formatos-de-representacao-de-dados-json-vs-xml)
    1. [JSON: Tipagem, Sintaxe Estrita e Validação com JSON Schema](#41-json-tipagem-sintaxe-estrita-e-validacao-com-json-schema)
    2. [XML: Estrutura, Validação (DTD/XSD) e Consultas com XPath](#42-xml-estrutura-validacao-dtdxsd-e-consultas-com-xpath)
    3. [Comparativo Prático entre JSON e XML](#43-comparativo-pratico-entre-json-e-xml)
    4. [Teste 096](#Teste-096)
5. [Documentação de APIs com OpenAPI e o Ecossistema Swagger](#5-documentacao-de-apis-com-openapi-e-o-ecossistema-swagger)
    1. [A Especificação OpenAPI (OAS 3.0 / 3.1)](#51-a-especificacao-openapi-oas-30-31)
    2. [Estrutura Canônica do Documento OpenAPI (YAML / JSON)](#52-estrutura-canonica-do-documento-openapi-yaml-json)
    3. [Ferramental Swagger: Swagger UI, Editor e Codegen](#53-ferramental-swagger-swagger-ui-editor-e-codegen)
    4. [Teste 097](#Teste-097)
6. [Fontes Recomendadas na Internet](#6-fontes-recomendadas-na-internet)

---

## 1. APIs RESTful e Protocolo HTTP

### 1.1 Princípios Arquiteturais do REST (Roy Fielding)
O estilo arquitetural **REST** (*Representational State Transfer*) foi formalizado por Roy Fielding em sua tese de doutorado no ano 2000. Trata-se de um conjunto de **restrições arquiteturais** coordenadas que, quando seguidas, conferem à web propriedades desejáveis de desempenho, escalabilidade, simplicidade, modificabilidade e visibilidade:

1. **Cliente-Servidor (*Client-Server*):** Separação estrita de responsabilidades. O cliente cuida da apresentação visual e experiência do usuário; o servidor encarrega-se do armazenamento de dados e das regras de negócio. Essa dissociação permite que ambas as camadas evoluam de forma independente.
2. **Sem Estado (*Statelessness*):** Cada requisição do cliente para o servidor deve conter **todas as informações contextuais necessárias** para que o servidor a interprete e execute. O servidor não armazena nenhuma sessão em memória entre requisições. O estado da sessão reside exclusivamente no lado cliente (ex.: tokens JWT).
3. **Cacheabilidade (*Cacheable*):** As respostas devem explicitar claramente se podem ou não ser retidas em cache pelo cliente ou por nós intermediários (via cabeçalhos `Cache-Control`, `ETag`, `Last-Modified`), reduzindo a latência e o consumo de banda.
4. **Interface Uniforme (*Uniform Interface*):** É o princípio distintivo do REST, subdividido em 4 pilares:
    - *Identificação de Recursos:* Recursos são identificados unicamente por URIs estáveis (ex.: `/processos/10`).
    - *Manipulação por Representações:* O cliente manipula o recurso através de sua representação textual (JSON, XML), e não do objeto bruto no banco de dados.
    - *Mensagens Autodescritivas:* Cada mensagem inclui metadados suficientes para indicar como deve ser processada (cabeçalho `Content-Type: application/json`).
    - *HATEOAS (Hypermedia As The Engine Of Application State):* A resposta traz links navegáveis que orientam o cliente sobre quais são os próximos passos e estados possíveis na aplicação.

5. **Sistema em Camadas (*Layered System*):** A arquitetura pode incluir intermediários transparentes para o cliente (balanceadores de carga, firewalls de aplicação - WAF, proxies reversos e gateways de API), sem que o cliente precise saber se está falando com o servidor final.
6. **Código sob Demanda (*Code on Demand* - Única Opcional):** Permite ao servidor estender a funcionalidade do cliente transmitindo código executável (ex.: scripts JavaScript).

### 1.2 O Modelo de Maturidade de Richardson
Leonard Richardson concebeu um modelo para classificar a aderência de serviços web aos preceitos REST:

```mermaid
flowchart TD
    subgraph Richardson["Níveis de Maturidade de Richardson"]
        N0["Nível 0: The Swamp of POX (Endpoint único RPC via POST)"]
        N1["Nível 1: Recursos Individuais (Múltiplas URIs bem estruturadas)"]
        N2["Nível 2: Verbos HTTP e Códigos de Status Padronizados"]
        N3["Nível 3: HATEOAS (Controles Hipermídia nas Respostas) - Glória do REST"]
    end
    N0 --> N1 --> N2 --> N3
```

- **Nível 0 (The Swamp of POX):** Utiliza HTTP apenas como protocolo de transporte para chamadas RPC remotas sobre um único endpoint (ex.: SOAP ou XML-RPC, onde todas as operações são enviadas via `POST /servico`).
- **Nível 1 (Recursos):** A API introduz URIs específicas para identificar recursos distintos (ex.: `/processos`, `/processos/12`), mas ainda utiliza métodos HTTP de forma genérica (frequentemente apenas POST ou GET).
- **Nível 2 (Verbos HTTP & Status Codes):** Emprega os verbos HTTP de acordo com sua semântica oficial (`GET` para leitura, `POST` para criação, `PUT` para substituição, `DELETE` para exclusão) e responde com códigos de status padronizados (`200`, `201`, `404`). A grande maioria das APIs comerciais atuais opera neste nível.
- **Nível 3 (Controles Hipermídia - HATEOAS):** O patamar máximo da maturidade REST. As respostas trazem links hipermídia (`_links` ou `rel`) que informam dinamicamente ao cliente quais ações subsequentes ele pode executar (ex.: aprovar processo, anexar documento).

### 1.3 Métodos HTTP: Semântica, Segurança e Idempotência
A RFC 7231 da IETF define com rigor a semântica e as propriedades dos métodos HTTP:

| Método | Seguro (*Safe*)? | Idempotente? | Semântica Principal | Códigos de Sucesso Comuns |
|---|:---:|:---:|---|---|
| **`GET`** | **Sim** | **Sim** | Recuperar a representação de um recurso (somente leitura). | `200 OK` |
| **`HEAD`** | **Sim** | **Sim** | Idêntico ao GET, mas retorna **apenas cabeçalhos** (sem corpo). | `200 OK` |
| **`OPTIONS`**| **Sim** | **Sim** | Consulta quais métodos e parâmetros o servidor aceita naquela URI. | `200 OK`, `204 No Content` |
| **`POST`** | **Não** | **Não** | Criação de recurso subordinado ou processamento arbitrário. | `201 Created`, `200 OK` |
| **`PUT`** | **Não** | **Sim** | **Substituição completa** do recurso especificado na URI. | `200 OK`, `204 No Content` |
| **`PATCH`**| **Não** | **Não**\* | **Modificação parcial** de campos de um recurso existente. | `200 OK`, `204 No Content` |
| **`DELETE`**| **Não** | **Sim** | Exclusão do recurso indicado na URI. | `200 OK`, `204 No Content` |

*\*Nota: Pela RFC 5789, PATCH não é intrinsecamente idempotente, embora possa ser implementado de forma idempotente em certos casos.*

> 🚨 **ALERTA DE PROVA / FCC:**  
>
> - **Método Seguro (*Safe*):** A execução da requisição **NÃO altera o estado dos recursos no servidor** (leitura pura). `GET`, `HEAD` e `OPTIONS` são seguros.
> - **Método Idempotente (*Idempotent*):** Executar a mesma requisição uma vez ou $N$ vezes consecutivas com os mesmos dados produz **exatamente o mesmo efeito final no estado do servidor**.
>     - O `PUT` é idempotente: substituir integralmente um registro 10 vezes resulta no mesmo estado final no banco de dados.
>     - O `DELETE` é idempotente: após o primeiro comando, o recurso foi apagado; chamá-lo novamente mantém o recurso inexistente. O fato de responder `404` na segunda chamada não altera a idempotência!
>     - O `POST` **NÃO é idempotente**: disparar 5 vezes cria 5 novos registros no banco.

### 1.4 Códigos de Status HTTP Essenciais em Provas

```mermaid
flowchart LR
    S2["2xx: Sucesso"]
    S3["3xx: Redirecionamento"]
    S4["4xx: Erro do Cliente"]
    S5["5xx: Erro do Servidor"]
    S2 -->|"200, 201, 204"| R2["Atendido com Êxito"]
    S3 -->|"301, 304"| R3["Cache ou Nova Localização"]
    S4 -->|"400, 401, 403, 404, 409, 422"| R4["Falha na Requisição do Cliente"]
    S5 -->|"500, 502, 503, 504"| R5["Falha na Infraestrutura do Servidor"]
```

#### Faixa 2xx (Sucesso)
- **`200 OK`:** A requisição foi atendida com sucesso e o corpo contém a resposta solicitada.
- **`201 Created`:** Um novo recurso foi criado com sucesso. O cabeçalho `Location` deve conter a URI do recurso recém-criado.
- **`204 No Content`:** A requisição foi processada com êxito, mas o servidor **não envia nenhum corpo de resposta** (comum após operações `DELETE` ou `PUT`).

#### Faixa 3xx (Redirecionamento)
- **`301 Moved Permanently`:** O recurso mudou de endereço definitivamente.
- **`304 Not Modified`:** Validação condicional de cache bem-sucedida (via `ETag` ou `If-Modified-Since`). O cliente deve reutilizar os dados já armazenados em seu cache local sem trafegar o corpo do arquivo.

#### Faixa 4xx (Erro do Cliente)
- **`400 Bad Request`:** Requisição sintaticamente malformada (ex.: JSON inválido, sintaxe corrompida).
- **`401 Unauthorized`:** Na realidade técnica, significa **Não Autenticado** (*Unauthenticated*). Faltam credenciais no cabeçalho `Authorization` ou o token expirou/está inválido (*"Eu não sei quem você é"*).
- **`403 Forbidden`:** O cliente foi **validado e autenticado com sucesso**, mas **não possui permissão/autorização** suficiente para acessar o recurso pretendido (*"Eu sei quem você é, mas você não tem autorização"*).
- **`404 Not Found`:** O servidor não encontrou nenhum recurso na URI solicitada.
- **`409 Conflict`:** Conflito de estado do recurso (ex.: tentativa de cadastrar um processo com número de protocolo que já existe).
- **`422 Unprocessable Entity`:** A sintaxe do payload é válida, mas há violação de regras semânticas de negócio (ex.: enviar campo "idade" com valor negativo).

### 1.5 Boas Práticas no Design de URIs e Recursos RESTful
- **Utilizar substantivos no plural:** `/processos`, `/auditores`, `/orgaos` (em vez de verbos como `/buscarProcessos` ou `/criarAuditor`).
- **Hierarquias para recursos aninhados:** `/processos/105/anexos/2` indica o anexo de código 2 subordinado ao processo 105.
- **Versionamento explícito na URI:** `/api/v1/processos` ou por cabeçalhos customizados (`Accept: application/vnd.tce.v1+json`).
- **Parâmetros de consulta (*Query Strings*):** Utilizados estritamente para filtragem, paginação e ordenação:
  `/processos?status=julgado&page=2&limit=20&sort=-dataCriacao`.

---

### Teste 087
**(CEBRASPE – TRT-8 – Analista Judiciario Area Apoio Especializado Tecnologia da Informacao – 2022)**
Em uma API RESTful, cada solicitação deve conter todos os dados necessários ao seu atendimento para não depender de informações armazenadas em outras sessões, o que caracteriza uma restrição de

* **A)** cache.
* **B)** arquitetura cliente-servidor.
* **C)** interface uniforme.
* **D)** sistema de camadas.
* **E)** comunicação stateless.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "cache". De acordo com a teoria estudada em *Faixa 3xx (Redirecionamento)*, `304 Not Modified`: Validação condicional de cache bem-sucedida (via `ETag` ou `If-Modified-Since`). O cliente deve reutilizar os dados já armazenados em seu cache local sem trafegar o corpo do arquivo.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "arquitetura cliente-servidor". De acordo com a teoria estudada em *3.1 Arquitetura Full-Duplex e a RFC 6455*, o protocolo HTTP tradicional baseia-se no modelo *Request-Response* *half-duplex*, no qual toda comunicação precisa ser iniciada pelo cliente.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "interface uniforme". De acordo com a teoria estudada em *1.1 Princípios Arquiteturais do REST (Roy Fielding)*, interface Uniforme (*Uniform Interface*): É o princípio distintivo do REST, subdividido em 4 pilares.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "sistema de camadas". De acordo com a teoria estudada em *1.1 Princípios Arquiteturais do REST (Roy Fielding)*, sistema em Camadas (*Layered System*): A arquitetura pode incluir intermediários transparentes para o cliente (balanceadores de carga, firewalls de aplicação - WAF, proxies reversos e gateways de API), sem que o cliente precise saber se está falando com o servidor final.
> - **E)** **Correta.** Conforme fundamentado na seção *1.1 Princípios Arquiteturais do REST (Roy Fielding)* deste guia, sem Estado (*Statelessness*): Cada requisição do cliente para o servidor deve conter todas as informações contextuais necessárias para que o servidor a interprete e execute. O servidor não armazena nenhuma sessão em memória entre requisições. Dessa forma, está plenamente correta a assertiva da banca (CEBRASPE – TRT-8/2022) ao estabelecer que "comunicação stateless".
>
> **Gabarito: E**

---

### Teste 088
**(FGV – TJ-RR – Analista Judiciario Infraestrutura de Tecnologia da Informacao – 2024)**
Uma API REST (Representational State Transfer) é uma interface que permite a comunicação entre sistemas utilizando um determinado protocolo, em que os recursos são acessados e manipulados por meio de requisições padrão como GET, POST, PUT e DELETE, seguindo princípios de simplicidade, escalabilidade e independência de plataforma. Isso posto, assinale a afirmativa correta sobre API REST.

* **A)** Normalmente, uma solicitação PUT cria um novo registro.
* **B)** Nenhum dado do cliente é armazenado no servidor entre as solicitações e toda solicitação é separada e desconectada.
* **C)** Não há a possibilidade de utilização de cache.
* **D)** Utiliza WSDL como linguagem de descrição de serviços web.
* **E)** É um protocolo com requisitos específicos, como a mensageria XML.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Normalmente, uma solicitação PUT cria um novo registro". De acordo com a teoria estudada em *1.3 Métodos HTTP: Semântica, Segurança e Idempotência*, o `PUT` é idempotente: substituir integralmente um registro 10 vezes resulta no mesmo estado final no banco de dados.
> - **B)** **Correta.** Conforme fundamentado na seção *Faixa 2xx (Sucesso)* deste guia, `204 No Content`: A requisição foi processada com êxito, mas o servidor não envia nenhum corpo de resposta (comum após operações `DELETE` ou `PUT`). Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ-RR/2024) ao estabelecer que "Nenhum dado do cliente é armazenado no servidor entre as solicitações e toda solicitação é separada e desconectada".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Não há a possibilidade de utilização de cache". De acordo com a teoria estudada em *3.1 Arquitetura Full-Duplex e a RFC 6455*, o protocolo HTTP tradicional baseia-se no modelo *Request-Response* *half-duplex*, no qual toda comunicação precisa ser iniciada pelo cliente.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Utiliza WSDL como linguagem de descrição de serviços web". De acordo com a teoria estudada em *1.2 O Modelo de Maturidade de Richardson*, nível 1 (Recursos): A API introduz URIs específicas para identificar recursos distintos (ex.: `/processos`, `/processos/12`), mas ainda utiliza métodos HTTP de forma genérica (frequentemente apenas POST ou GET).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "É um protocolo com requisitos específicos, como a mensageria XML". De acordo com a teoria estudada em *Faixa 4xx (Erro do Cliente)*, `404 Not Found`: O servidor não encontrou nenhum recurso na URI solicitada.
>
> **Gabarito: B**

---

### Teste 089
**(FGV – TRT-16 – Analista Judiciario Area Administrativa Tecnologia da Informacao – 2022)**
O Swagger é uma plataforma que possui diversas ferramentas, entre as quais o SwaggerHub. Em relação ao SwaggerHub, analise os itens a seguir: I. Permite que os desenvolvedores definam suas APIs no formato OpenAPI ou AsyncAPI. II. É uma plataforma colaborativa capaz de hospedar todas as definições de APIs em um único local. III. Para o AsyncAPI, gera códigos de servidor e cliente e envia-os por push para as plataformas GitHub, GitLab, Bitbucket ou Azure DevOps Services. Está correto apenas o que se afirma em

* **A)** I.
* **B)** I e II.
* **C)** II e III.
* **D)** I e III.
* **E)** III.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I". De acordo com a teoria estudada em *1.2 O Modelo de Maturidade de Richardson*, nível 0 (The Swamp of POX): Utiliza HTTP apenas como protocolo de transporte para chamadas RPC remotas sobre um único endpoint (ex.: SOAP ou XML-RPC, onde todas as operações são enviadas via `POST /servico`).
> - **B)** **Correta.** Conforme fundamentado na seção *5.3 Ferramental Swagger: Swagger UI, Editor e Codegen* deste guia, swagger UI: Converte o contrato OpenAPI em uma interface visual web interativa, onde desenvolvedores e analistas podem inspecionar a documentação e realizar disparos de testes reais diretamente pelo navegador (*Try it out*). Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT-16/2022) ao estabelecer que "I e II".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "II e III". De acordo com a teoria estudada em *1.1 Princípios Arquiteturais do REST (Roy Fielding)*, sem Estado (*Statelessness*): Cada requisição do cliente para o servidor deve conter todas as informações contextuais necessárias para que o servidor a interprete e execute. O servidor não armazena nenhuma sessão em memória entre requisições.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I e III". De acordo com a teoria estudada em *1.1 Princípios Arquiteturais do REST (Roy Fielding)*, código sob Demanda (*Code on Demand* - Única Opcional): Permite ao servidor estender a funcionalidade do cliente transmitindo código executável (ex.: scripts JavaScript).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "III". De acordo com a teoria estudada em *2.1 Motivação: Resolução de Over-fetching e Under-fetching*, solução do GraphQL: O cliente envia uma consulta declarativa especificando exatamente quais campos e relacionamentos deseja.
>
> **Gabarito: B**

---

### Teste 090
**(FGV – TRT-13 – Analista Judiciario Tecnologia da Informacao – 2022)**
Uma aplicação mobile enviou a um gateway de APIs REST várias solicitações idênticas em sequência utilizando o método HTTP PUT. Essas solicitações idênticas resultaram em nenhuma alteração de estado do sistema de backend, a exceção da primeira solicitação que atualizou um registro no banco de dados. Nesse contexto, é correto afirmar que essa solicitação HTTP é

* **A)** acoplada.
* **B)** balanceada.
* **C)** full-duplex.
* **D)** idempotente.
* **E)** segura.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *1.3 Métodos HTTP: Semântica, Segurança e Idempotência* deste guia, o `PUT` é idempotente: substituir integralmente um registro 10 vezes resulta no mesmo estado final no banco de dados. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT-13/2022) ao estabelecer que "acoplada".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "balanceada". De acordo com a teoria estudada em *1.1 Princípios Arquiteturais do REST (Roy Fielding)*, sistema em Camadas (*Layered System*): A arquitetura pode incluir intermediários transparentes para o cliente (balanceadores de carga, firewalls de aplicação - WAF, proxies reversos e gateways de API), sem que o cliente precise saber se está falando com o servidor final.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "full-duplex". De acordo com a teoria estudada em *3.1 Arquitetura Full-Duplex e a RFC 6455*, mensageria Push Nativa: O servidor pode enviar dados ativamente ao cliente a qualquer momento sem que o cliente precise solicitar (*server push* instantâneo).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "idempotente". De acordo com a teoria estudada em *1.3 Métodos HTTP: Semântica, Segurança e Idempotência*, método Idempotente (*Idempotent*): Executar a mesma requisição uma vez ou \$N\$ vezes consecutivas com os mesmos dados produz exatamente o mesmo efeito final no estado do servidor.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "segura". De acordo com a teoria estudada em *3.3 Comparativo: Polling, Long-Polling, Server-Sent Events (SSE) e WebSocket*, long Polling: Unidirecional (Servidor segura requisição) — HTTP com conexão mantida aberta até haver dado — Alto (reabre conexão HTTP a cada resposta) — Cenários legados sem suporte a WebSockets.
>
> **Gabarito: A**

---

#### Faixa 5xx (Erro do Servidor)
- **`500 Internal Server Error`:** Erro genérico e inesperado de execução no servidor (exceção não tratada no código).
- **`502 Bad Gateway`:** Um servidor intermediário (proxy reverso, gateway de API) recebeu uma resposta inválida ou falha do servidor *upstream* (backend).
- **`503 Service Unavailable`:** O servidor está temporariamente incapaz de atender requisições por sobrecarga pontual ou manutenção programada.
- **`504 Gateway Timeout`:** O servidor intermediário esgotou o tempo limite de espera (*timeout*) aguardando uma resposta do servidor backend.

---

### Teste 091
**(FGV – TJ-AP – Analista Judiciario Apoio Especializado Tecnologia da Informacao Desenvolvimento de Sistemas – 2023)**
Observe a seguinte requisição em Hypertext Transfer Protocol (HTTP) feita a uma Application Programming Interface (API) RESTful: PUT http://webservice.tjapp/recursos/1 A respectiva resposta HTTP da API RESTful apresentou o código de status 204. Os dados apresentados acima indicam que a API RESTful processou a solicitação de:

* **A)** obtenção de um recurso de forma bem-sucedida;
* **B)** atualização de um recurso de forma malsucedida;
* **C)** criação de um novo recurso de forma malsucedida;
* **D)** atualização de um recurso de forma bem-sucedida;
* **E)** criação de um novo recurso de forma bem-sucedida.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "obtenção de um recurso de forma bem-sucedida". De acordo com a teoria estudada em *1.2 O Modelo de Maturidade de Richardson*, nível 1 (Recursos): A API introduz URIs específicas para identificar recursos distintos (ex.: `/processos`, `/processos/12`), mas ainda utiliza métodos HTTP de forma genérica (frequentemente apenas POST ou GET).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "atualização de um recurso de forma malsucedida". De acordo com a teoria estudada em *1.3 Métodos HTTP: Semântica, Segurança e Idempotência*, `PUT`: Não — Sim — Substituição completa do recurso especificado na URI. — `200 OK`, `204 No Content`.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "criação de um novo recurso de forma malsucedida". De acordo com a teoria estudada em *1.3 Métodos HTTP: Semântica, Segurança e Idempotência*, `POST`: Não — Não — Criação de recurso subordinado ou processamento arbitrário. — `201 Created`, `200 OK`.
> - **D)** **Correta.** Conforme fundamentado na seção *Faixa 3xx (Redirecionamento)* deste guia, `304 Not Modified`: Validação condicional de cache bem-sucedida (via `ETag` ou `If-Modified-Since`). O cliente deve reutilizar os dados já armazenados em seu cache local sem trafegar o corpo do arquivo. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ-AP/2023) ao estabelecer que "atualização de um recurso de forma bem-sucedida".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "criação de um novo recurso de forma bem-sucedida". De acordo com a teoria estudada em *1.2 O Modelo de Maturidade de Richardson*, nível 2 (Verbos HTTP & Status Codes): Emprega os verbos HTTP de acordo com sua semântica oficial (`GET` para leitura, `POST` para criação, `PUT` para substituição, `DELETE` para exclusão) e responde com códigos de status padronizados (`200`, `201`, `404`).
>
> **Gabarito: D**

---

## 2. GraphQL: Arquitetura e Consultas Declarativas

### 2.1 Motivação: Resolução de Over-fetching e Under-fetching
Desenvolvido pelo Facebook (Meta) em 2012 e tornado código aberto em 2015, o **GraphQL** é uma linguagem de consulta para APIs e um ambiente de execução para cumprir essas consultas com dados existentes.

```mermaid
flowchart LR
    subgraph REST_Problem["Problemas no REST Tradicional"]
        R1["GET /processos/1"] --> T1["Payload com 60 campos desnecessários (Over-fetching)"]
        R2["GET /processos/1/relatores"] --> T2["Segunda chamada em cascata (Under-fetching)"]
        R3["GET /processos/1/prazos"] --> T3["Terceira chamada (Gargalo N+1)"]
    end
    subgraph GraphQL_Sol["Solução com GraphQL"]
        G1["POST /graphql"] --> Res["Payload sob medida com apenas os dados solicitados"]
    end
```

- **Over-fetching (Excesso de Dados):** Ocorre no REST quando um endpoint fixo retorna dezenas de campos complexos, embora a interface do cliente só precise de dois (ex.: renderizar apenas o nome do relator em uma lista móvel consumindo centenas de kilobytes de dados irrelevantes).
- **Under-fetching (Carência de Dados):** Ocorre no REST quando um endpoint não traz dados relacionados suficientes, forçando o cliente a disparar sucessivas requisições em cascata para montar uma única tela (ex.: `GET /processos`, depois $N$ requisições para `GET /processos/{id}/partes` — o clássico problema $N+1$).
- **Solução do GraphQL:** O cliente envia uma consulta declarativa especificando **exatamente quais campos e relacionamentos deseja**. O backend responde com um JSON espelhado na estrutura exata do pedido, através de um **endpoint único** (geralmente `/graphql`), operando via requisições HTTP `POST`.

### 2.2 Modelo Operacional e a Schema Definition Language (SDL)
O contrato entre cliente e servidor no GraphQL é expresso na linguagem **SDL** (*Schema Definition Language*):

```graphql
type Processo {
  id: ID!
  numeroProtocolo: String!
  valorGlosa: Float
  julgado: Boolean!
  relator: Auditor!
}

type Auditor {
  id: ID!
  nome: String!
  matricula: String!
}
```

- **Tipos Escalares Nativos:** `Int` (inteiro 32 bits), `Float` (ponto flutuante com sinal), `String` (UTF-8), `Boolean` (`true`/`false`) e `ID` (identificador único serializado como string).
- **Modificador de Não-Nulo (`!`):** Garante que o campo jamais retornará nulo (ex.: `String!`). Se ausente, o campo é considerado anulável (*nullable*).
- **Tipos de Lista (`[]`):** `[String]` indica uma lista de strings. `[String!]!` indica uma lista não nula contendo itens obrigatoriamente não nulos.

### 2.3 Operações Centrais: Queries, Mutations, Subscriptions e Resolvers

1. **`Query`:** Operações de consulta e leitura de dados. Não devem provocar efeitos colaterais no backend (análogas ao método `GET` do REST).

```graphql
query BuscarProcesso {
  processo(id: "100") {
    numeroProtocolo
    relator {
      nome
    }
  }
}
```

2. **`Mutation`:** Operações que provocam modificações no servidor (criação, edição, exclusão de dados — análogas ao `POST`, `PUT`, `DELETE`).

```graphql
mutation CriarProcesso($dados: NovoProcessoInput!) {
  cadastrarProcesso(input: $dados) {
    id
    numeroProtocolo
  }
}
```

3. **`Subscription`:** Mecanismo de subscrição para receber eventos e atualizações em tempo real disparadas pelo servidor (mantidas tipicamente sobre conexões WebSocket).
4. **`Resolvers`:** Funções no backend associadas a cada campo do Schema. Quando uma query é executada, o motor do GraphQL invoca os *resolvers* correspondentes para extrair os dados de bancos SQL, bancos NoSQL ou de outras APIs REST.

---

### Teste 092
**(CEBRASPE – TRT-8 – Analista Judiciario Apoio Especializado Tecnologia da Informacao – 2016)**
Assinale a opção que apresenta o método HTTP que envia dados, colocando-os no corpo da mensagem, e deixa a URI separada dos dados que serão enviados.

* **A)** HEAD
* **B)** PUT
* **C)** CONNECT
* **D)** GET
* **E)** POST

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "HEAD". De acordo com a teoria estudada em *1.3 Métodos HTTP: Semântica, Segurança e Idempotência*, método Seguro (*Safe*): A execução da requisição NÃO altera o estado dos recursos no servidor (leitura pura). `GET`, `HEAD` e `OPTIONS` são seguros.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "PUT". De acordo com a teoria estudada em *1.2 O Modelo de Maturidade de Richardson*, nível 2 (Verbos HTTP & Status Codes): Emprega os verbos HTTP de acordo com sua semântica oficial (`GET` para leitura, `POST` para criação, `PUT` para substituição, `DELETE` para exclusão) e responde com códigos de status padronizados (`200`, `201`, `404`).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "CONNECT". De acordo com a teoria estudada em *2.1 Motivação: Resolução de Over-fetching e Under-fetching*, o backend responde com um JSON espelhado na estrutura exata do pedido, através de um endpoint único (geralmente `/graphql`), operando via requisições HTTP `POST`.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "GET". De acordo com a teoria estudada em *1.2 O Modelo de Maturidade de Richardson*, nível 1 (Recursos): A API introduz URIs específicas para identificar recursos distintos (ex.: `/processos`, `/processos/12`), mas ainda utiliza métodos HTTP de forma genérica (frequentemente apenas POST ou GET).
> - **E)** **Correta.** Conforme fundamentado na seção *2.3 Operações Centrais: Queries, Mutations, Subscriptions e Resolvers* deste guia, `Mutation`: Operações que provocam modificações no servidor (criação, edição, exclusão de dados — análogas ao `POST`, `PUT`, `DELETE`). Dessa forma, está plenamente correta a assertiva da banca (CEBRASPE – TRT-8/2016) ao estabelecer que "POST".
>
> **Gabarito: E**

---

### Teste 093
**(FGV – TJ-AP – Analista Judiciario Apoio Especializado Tecnologia da Informacao Desenvolvimento de Sistemas – 2023)**
Breno está criando um serviço REST, que será disponibilizado por meio de um aplicativo Spring Boot. Como ele já conhece o padrão do REST, criou um método de inclusão no controlador, tendo como parâmetro uma entidade do tipo gerenciado pelo serviço. Para que o parâmetro receba corretamente os dados fornecidos pela requisição, no formato JSON, Breno irá utilizar nesse parâmetro a anotação:

* **A)** PostMapping;
* **B)** RestController;
* **C)** GetMapping;
* **D)** RequestBody;
* **E)** PathParam.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "PostMapping". De acordo com a teoria estudada em *4.1 JSON: Tipagem, Sintaxe Estrita e Validação com JSON Schema*, o JSON (*JavaScript Object Notation*, padronizado pela RFC 8259) é o formato dominante no intercâmbio de dados em APIs REST modernas.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "RestController". De acordo com a teoria estudada em *2.3 Operações Centrais: Queries, Mutations, Subscriptions e Resolvers*, `Query`: Operações de consulta e leitura de dados. Não devem provocar efeitos colaterais no backend (análogas ao método `GET` do REST).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "GetMapping". De acordo com a teoria estudada em *1.3 Métodos HTTP: Semântica, Segurança e Idempotência*, método Idempotente (*Idempotent*): Executar a mesma requisição uma vez ou \$N\$ vezes consecutivas com os mesmos dados produz exatamente o mesmo efeito final no estado do servidor.
> - **D)** **Correta.** Conforme fundamentado na seção *5.2 Estrutura Canônica do Documento OpenAPI (YAML / JSON)* deste guia, `paths`: Mapeia os endpoints (URIs), métodos HTTP suportados, parâmetros (path, query, header), corpo de requisição (`requestBody`) e respostas (`responses`). Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ-AP/2023) ao estabelecer que "RequestBody".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "PathParam". De acordo com a teoria estudada em *1.3 Métodos HTTP: Semântica, Segurança e Idempotência*, método Seguro (*Safe*): A execução da requisição NÃO altera o estado dos recursos no servidor (leitura pura). `GET`, `HEAD` e `OPTIONS` são seguros.
>
> **Gabarito: D**

---

## 3. Protocolo WebSocket e Comunicação em Tempo Real

### 3.1 Arquitetura Full-Duplex e a RFC 6455
O protocolo HTTP tradicional baseia-se no modelo *Request-Response* *half-duplex*, no qual toda comunicação precisa ser iniciada pelo cliente. O protocolo **WebSocket** (padronizado pela IETF na **RFC 6455**) viabiliza comunicação **Full-Duplex** (bidirecional simultânea) e persistente sobre uma única conexão TCP de longa duração.

- **Baixa Latência e Mínimo Overhead:** Após a conexão ser aberta, os cabeçalhos HTTP volumosos não são mais transmitidos. As mensagens trafegam divididas em frames levíssimos contendo cabeçalhos de apenas 2 a 10 bytes.
- **Mensageria Push Nativa:** O servidor pode enviar dados ativamente ao cliente a qualquer momento sem que o cliente precise solicitar (*server push* instantâneo).

### 3.2 O Handshake HTTP Upgrade e os Esquemas `ws://` e `wss://`
A conexão WebSocket não inicia diretamente no protocolo WebSocket; ela nasce sobre o protocolo HTTP através de um procedimento de negociação denominado **HTTP Upgrade Handshake**:

```mermaid
sequenceDiagram
    autonumber
    actor Cliente as Navegador Web
    participant Servidor as Servidor WebSocket

    Note over Cliente,Servidor: 1. Negociação de Protocolo (HTTP Handshake)
    Cliente->>Servidor: GET /chat HTTP/1.1<br/>Host: api.tce.go.gov.br<br/>Upgrade: websocket<br/>Connection: Upgrade<br/>Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==<br/>Sec-WebSocket-Version: 13
    Servidor-->>Cliente: HTTP/1.1 101 Switching Protocols<br/>Upgrade: websocket<br/>Connection: Upgrade<br/>Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=

    Note over Cliente,Servidor: 2. Conexão TCP Aberta em Modo Full-Duplex
    Cliente->>Servidor: Frame de Texto / Binário
    Servidor-->>Cliente: Atualização Push Instantânea
    Cliente->>Servidor: Ping
    Servidor-->>Cliente: Pong (Heartbeat)
```

- **Cabeçalhos do Handshake:**
    - O cliente envia `Upgrade: websocket` e `Connection: Upgrade`.
    - O servidor concorda respondendo com o código especial **`101 Switching Protocols`**.
- **Esquemas de Conexão:**
    - `ws://`: Conexão em texto claro sem criptografia (opera na porta 80 por padrão).
    - `wss://` (*WebSocket Secure*): Conexão protegida por criptografia TLS/HTTPS (opera na porta 443 por padrão), recomendada em ambientes de produção.

### 3.3 Comparativo: Polling, Long-Polling, Server-Sent Events (SSE) e WebSocket

| Tecnologia | Direção da Comunicação | Protocolo Subjacente | Overhead por Mensagem | Caso de Uso Ideal |
|---|:---:|:---:|:---:|---|
| **Short Polling** | Unidirecional (Cliente $\rightarrow$ Servidor) | HTTP repetitivo em intervalos fixos | **Altíssimo** (novo handshake e cabeçalhos a cada requisição) | Verificações esporádicas e simples. |
| **Long Polling** | Unidirecional (Servidor segura requisição) | HTTP com conexão mantida aberta até haver dado | Alto (reabre conexão HTTP a cada resposta) | Cenários legados sem suporte a WebSockets. |
| **Server-Sent Events (SSE)** | **Unidirecional** (Servidor $\rightarrow$ Cliente) | HTTP padrão (`text/event-stream`) | Baixo (conexão persistente HTTP única) | Painéis de monitoramento, cotações, feeds onde o cliente só recebe dados. |
| **WebSocket** | **Bidirecional Completo (*Full-Duplex*)** | Protocolo TCP customizado após handshake | **Mínimo** (frames de 2 a 10 bytes) | Chats, jogos interativos, colaboração simultânea em tempo real. |

---

### Teste 094
**(CEBRASPE – TRT-8 – Analista Judiciario Area Apoio Especializado Tecnologia da Informacao – 2022)**
O cabeçalho do protocolo HTTP que contém o DNS do servidor é o

* **A)** host.
* **B)** authorization.
* **C)** referer.
* **D)** location.
* **E)** server.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *3.1 Arquitetura Full-Duplex e a RFC 6455* deste guia, o protocolo HTTP tradicional baseia-se no modelo *Request-Response* *half-duplex*, no qual toda comunicação precisa ser iniciada pelo cliente. Dessa forma, está plenamente correta a assertiva da banca (CEBRASPE – TRT-8/2022) ao estabelecer que "host".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "authorization". De acordo com a teoria estudada em *Faixa 4xx (Erro do Cliente)*, `401 Unauthorized`: Na realidade técnica, significa Não Autenticado (*Unauthenticated*). Faltam credenciais no cabeçalho `Authorization` ou o token expirou/está inválido (*"Eu não sei quem você é"*).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "referer". De acordo com a teoria estudada em *3.2 O Handshake HTTP Upgrade e os Esquemas `ws://` e `wss://`*, a conexão WebSocket não inicia diretamente no protocolo WebSocket; ela nasce sobre o protocolo HTTP através de um procedimento de negociação denominado HTTP Upgrade Handshake.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "location". De acordo com a teoria estudada em *Faixa 2xx (Sucesso)*, `201 Created`: Um novo recurso foi criado com sucesso. O cabeçalho `Location` deve conter a URI do recurso recém-criado.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "server". De acordo com a teoria estudada em *3.3 Comparativo: Polling, Long-Polling, Server-Sent Events (SSE) e WebSocket*, short Polling: Unidirecional (Cliente \$\rightarrow\$ Servidor) — HTTP repetitivo em intervalos fixos — Altíssimo (novo handshake e cabeçalhos a cada requisição) — Verificações esporádicas e simples.
>
> **Gabarito: A**

---

### Teste 095
**(CEBRASPE – TRT-8 – Analista Judiciario Apoio Especializado Tecnologia da Informacao – 2016)**
No que se refere à interoperabilidade de sistemas, assinale a opção correta.

* **A)** Mensagens SOAP possuem estrutura que descreve uma chamada de método, contendo alguma solicitação ou resposta. Considerando uma solicitação, o corpo da mensagem SOAP deve conter instruções para outra máquina executar determinada tarefa de forma remota.
* **B)** Os documentos formatados como XML contêm todas as instruções necessárias para a exibição de dados, razão pela qual dispensam aplicativos complementares para decidir como esses dados serão apresentados.
* **C)** Os diretórios UDDI são catálogos de web services que descrevem o negócio e os serviços disponíveis por meio das páginas amarelas, as quais definem as principais características da companhia, e das páginas brancas, as quais detalham a interface para o serviço.
* **D)** Os documentos WSDL disponibilizam a metodologia necessária para a integração entre os aplicativos e os web services, especificando informações de entrada e saída do serviço, sem indicar os formatos de solicitações e respostas.
* **E)** A arquitetura ePING consiste em um conjunto mínimo de informações técnicas que regulamentam os padrões de interoperabilidade de governo eletrônico, definindo as condições de interação dentro das diversas esferas do governo. As áreas cobertas pela ePING estão segmentadas em interconexão, segurança, planejamento, fiscalização e integração para governo eletrônico.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *1.1 Princípios Arquiteturais do REST (Roy Fielding)* deste guia, *Mensagens Autodescritivas:* Cada mensagem inclui metadados suficientes para indicar como deve ser processada (cabeçalho `Content-Type: application/json`). Dessa forma, está plenamente correta a assertiva da banca (CEBRASPE – TRT-8/2016) ao estabelecer que "Mensagens SOAP possuem estrutura que descreve uma chamada de método, contendo alguma solicitação ou resposta...".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Os documentos formatados como XML contêm todas as instruções necessárias para a exibição de dados, razão pela qual...". De acordo com a teoria estudada em *1.1 Princípios Arquiteturais do REST (Roy Fielding)*, sem Estado (*Statelessness*): Cada requisição do cliente para o servidor deve conter todas as informações contextuais necessárias para que o servidor a interprete e execute. O servidor não armazena nenhuma sessão em memória entre requisições.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Os diretórios UDDI são catálogos de web services que descrevem o negócio e os serviços disponíveis por meio das...". De acordo com a teoria estudada em *1.2 O Modelo de Maturidade de Richardson*, nível 0 (The Swamp of POX): Utiliza HTTP apenas como protocolo de transporte para chamadas RPC remotas sobre um único endpoint (ex.: SOAP ou XML-RPC, onde todas as operações são enviadas via `POST /servico`).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Os documentos WSDL disponibilizam a metodologia necessária para a integração entre os aplicativos e os web...". De acordo com a teoria estudada em *5.2 Estrutura Canônica do Documento OpenAPI (YAML / JSON)*, `paths`: Mapeia os endpoints (URIs), métodos HTTP suportados, parâmetros (path, query, header), corpo de requisição (`requestBody`) e respostas (`responses`).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A arquitetura ePING consiste em um conjunto mínimo de informações técnicas que regulamentam os padrões de...". De acordo com a teoria estudada em *3.1 Arquitetura Full-Duplex e a RFC 6455*, baixa Latência e Mínimo Overhead: Após a conexão ser aberta, os cabeçalhos HTTP volumosos não são mais transmitidos. As mensagens trafegam divididas em frames levíssimos contendo cabeçalhos de apenas 2 a 10 bytes.
>
> **Gabarito: A**

---

## 4. Formatos de Representação de Dados: JSON vs. XML

### 4.1 JSON: Tipagem, Sintaxe Estrita e Validação com JSON Schema
O JSON (*JavaScript Object Notation*, padronizado pela RFC 8259) é o formato dominante no intercâmbio de dados em APIs REST modernas.

- **Tipos de Dados Suportados:**
    - Primitivos: `string` (entre aspas duplas), `number` (inteiro ou flutuante), `boolean` (`true` ou `false`), `null`.
    - Estruturas de Dados: `object` (pares chave-valor `{}`) e `array` (listas ordenadas `[]`).
- **Regras Estritas de Sintaxe:**
    - **Chaves obrigatoriamente entre aspas duplas (`"chave": valor`)**. Usar aspas simples gera erro de parsing.
    - Proibida vírgula residual no último elemento (*trailing comma*): `{"id": 1,}` é inválido.
    - O padrão JSON puro **não suporta comentários** (`//` ou `/* */`).
- **JSON Schema:** Padrão para validar a estrutura, os tipos e os campos obrigatórios em payloads JSON de forma automatizada.

### 4.2 XML: Estrutura, Validação (DTD/XSD) e Consultas com XPath
O XML (*Extensible Markup Language*) é uma linguagem de marcação baseada em tags hierárquicas personalizáveis.

- **Estrutura:** Exige prólogo `<?xml version="1.0" encoding="UTF-8"?>`, raiz única (*root element*) e fechamento obrigatório de todas as tags (sensível a maiúsculas/minúsculas).
- **Validação de Documentos XML:**
    - **Well-formed (Bem-formado):** Cumpre as regras sintáticas fundamentais da linguagem XML.
    - **Valid (Válido):** Além de bem-formado, respeita rigorosamente um esquema formal de regras estruturais:
    - **DTD (*Document Type Definition*):** Mecanismo mais antigo com sintaxe própria.
    - **XSD (*XML Schema Definition*):** Esquema moderno escrito na própria sintaxe XML, com suporte a tipos de dados ricos e namespaces.
- **Consultas com XPath:** Linguagem de expressões de caminhos que permite navegar e selecionar nós específicos dentro da árvore XML (ex.: `/processos/processo[@status='julgado']/valor`).

### 4.3 Comparativo Prático entre JSON e XML

| Critério | JSON | XML |
|---|---|---|
| **Formato de Estrutura** | Pares chave-valor e listas (`{}`, `[]`) | Árvore de elementos com tags e atributos |
| **Complexidade de Parsing** | Leve e nativo para interpretadores JavaScript | Custoso computacionalmente (requer parsers DOM/SAX) |
| **Tamanho da Mensagem** | Compacto, sem redundância de tags | Verboso devido à duplicação de tags de fechamento |
| **Validação de Esquema** | JSON Schema | DTD e XML Schema (XSD) |
| **Linguagem de Consulta** | JSONPath | XPath e XQuery |

---

### Teste 096
**(FGV – TRT-24 – Analista Judiciario Area Apoio Especializado Tecnologia da Informacao – 2025)**
Paula e Maria estão avaliando as potencialidades dos usos de JSON e XML no desenvolvimento de aplicações Web para uma grande companhia estatal. As analistas sabem que JSON e XML são duas escolhas muito comuns quando se trata de formatos de dados na Web. A esse respeito, assinale a afirmativa correta.

* **A)** Com relação à legibilidade, Paula informa que ambos são legíveis por humanos, mas os documentos XML são mais detalhados.
* **B)** Com relação ao volume de dados, Maria informa que o JSON é maior e menos compacto que o XML devido aos elementos extra de marcação.
* **C)** Com relação as análises, Paula informa que as análises dos documentos JSON são mais complexas que os XML.
* **D)** Com relação ao apoio à gestão de dados, Maria informa que ambos possuem limitado suporte ao idioma português e que o XML está em desuso.
* **E)** Com relação aos casos de uso, Paula informa que o JSON é geralmente preterido para aplicações web devido ao seu código binário ser maior o que XML.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *4.2 XML: Estrutura, Validação (DTD/XSD) e Consultas com XPath* deste guia, dTD (*Document Type Definition*): Mecanismo mais antigo com sintaxe própria. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT-24/2025) ao estabelecer que "Com relação à legibilidade, Paula informa que ambos são legíveis por humanos, mas os documentos XML são mais...".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Com relação ao volume de dados, Maria informa que o JSON é maior e menos compacto que o XML devido aos elementos...". De acordo com a teoria estudada em *4.3 Comparativo Prático entre JSON e XML*, tamanho da Mensagem: Compacto, sem redundância de tags — Verboso devido à duplicação de tags de fechamento.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Com relação as análises, Paula informa que as análises dos documentos JSON são mais complexas que os XML". De acordo com a teoria estudada em *1.1 Princípios Arquiteturais do REST (Roy Fielding)*, *Manipulação por Representações:* O cliente manipula o recurso através de sua representação textual (JSON, XML), e não do objeto bruto no banco de dados.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Com relação ao apoio à gestão de dados, Maria informa que ambos possuem limitado suporte ao idioma português e que...". De acordo com a teoria estudada em *4.2 XML: Estrutura, Validação (DTD/XSD) e Consultas com XPath*, xSD (*XML Schema Definition*): Esquema moderno escrito na própria sintaxe XML, com suporte a tipos de dados ricos e namespaces.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Com relação aos casos de uso, Paula informa que o JSON é geralmente preterido para aplicações web devido ao seu...". De acordo com a teoria estudada em *1.3 Métodos HTTP: Semântica, Segurança e Idempotência*, *\*Nota: Pela RFC 5789, PATCH não é intrinsecamente idempotente, embora possa ser implementado de forma idempotente em certos casos.*.
>
> **Gabarito: A**

---

## 5. Documentação de APIs com OpenAPI e o Ecossistema Swagger

### 5.1 A Especificação OpenAPI (OAS 3.0 / 3.1)
A especificação **OpenAPI** (gerenciada pela *OpenAPI Initiative* sob tutela da Linux Foundation) é uma descrição padronizada, legível por humanos e máquinas, para interfaces de APIs RESTful. Escrita em sintaxe **YAML** ou **JSON**, ela independe da linguagem de programação utilizada no backend.

### 5.2 Estrutura Canônica do Documento OpenAPI (YAML / JSON)
Um documento OpenAPI divide-se nas seguintes seções principais:

```yaml
openapi: 3.0.3
info:
  title: API de Processos do TCE-GO
  version: 1.0.0
  description: API REST para consulta e instrução de auditorias fiscais.
servers:
  - url: https://api.tce.go.gov.br/v1
    description: Servidor de Produção
paths:
  /processos/{id}:
    get:
      summary: Obter detalhes do processo
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
      responses:
        '200':
          description: Processo recuperado com sucesso
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Processo'
        '404':
          description: Processo não encontrado
components:
  schemas:
    Processo:
      type: object
      required:
        - id
        - numeroProtocolo
      properties:
        id:
          type: integer
        numeroProtocolo:
          type: string
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
```

- `openapi`: Versão da especificação OpenAPI empregada.
- `info`: Título, descrição, versão e termos da API.
- `servers`: URLs base dos ambientes (produção, homologação).
- `paths`: Mapeia os endpoints (URIs), métodos HTTP suportados, parâmetros (path, query, header), corpo de requisição (`requestBody`) e respostas (`responses`).
- `components`: Seção de **reutilização modular**. Evita redundância de código através do mecanismo de referências (`$ref`):
    - `schemas`: Modelos de entidades de dados.
    - `securitySchemes`: Definições de autenticação e autorização (Bearer JWT, OAuth2, API Key).

### 5.3 Ferramental Swagger: Swagger UI, Editor e Codegen
- **Swagger UI:** Converte o contrato OpenAPI em uma interface visual web interativa, onde desenvolvedores e analistas podem inspecionar a documentação e realizar disparos de testes reais diretamente pelo navegador (*Try it out*).
- **Swagger Editor:** Editor visual com validação sintática em tempo real para projetar contratos OpenAPI em YAML/JSON.
- **OpenAPI Generator / Swagger Codegen:** Utilitários que leem o arquivo OpenAPI e geram automaticamente o código boilerplate de clientes SDK (em Java, Python, TypeScript) ou esqueletos de servidores backend.

---

### Teste 097
**(FGV – TRT-16 – Analista Judiciario Area Administrativa Tecnologia da Informacao – 2022)**
O SwaggerEditor permite editar e documentar APIs. Em relação ao tema, assinale V para a afirmativa verdadeira e F para a falsa. I. O editor pode ser utilizado online como uma ferramenta web de código aberto ou ser instalada e executada localmente a partir de um servidor. II. A página inicial da versão online é composta por quatro elementos de interface: um toolbar, um painel de edição de API, um painel de visualização de documentos e um painel para testar os webhooks e chamadas da API. III. O editor, na versão online, salva os códigos da APIs nos formatos das especificações YAML, JSON e XML. As afirmativas são, respectivamente,

* **A)** V, F e F.
* **B)** V, V e F.
* **C)** V, F e V.
* **D)** F, V e V.
* **E)** F, F e V.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *5.2 Estrutura Canônica do Documento OpenAPI (YAML / JSON)* deste guia, `info`: Título, descrição, versão e termos da API. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT-16/2022) ao estabelecer que "V, F e F".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "V, V e F". De acordo com a teoria estudada em *5.3 Ferramental Swagger: Swagger UI, Editor e Codegen*, swagger UI: Converte o contrato OpenAPI em uma interface visual web interativa, onde desenvolvedores e analistas podem inspecionar a documentação e realizar disparos de testes reais diretamente pelo navegador (*Try it out*).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "V, F e V". De acordo com a teoria estudada em *2.1 Motivação: Resolução de Over-fetching e Under-fetching*, desenvolvido pelo Facebook (Meta) em 2012 e tornado código aberto em 2015, o GraphQL é uma linguagem de consulta para APIs e um ambiente de execução para cumprir essas consultas com dados existentes.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "F, V e V". De acordo com a teoria estudada em *5.2 Estrutura Canônica do Documento OpenAPI (YAML / JSON)*, `openapi`: Versão da especificação OpenAPI empregada.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "F, F e V". De acordo com a teoria estudada em *5.3 Ferramental Swagger: Swagger UI, Editor e Codegen*, swagger Editor: Editor visual com validação sintática em tempo real para projetar contratos OpenAPI em YAML/JSON.
>
> **Gabarito: A**

---

## 6. Fontes Recomendadas na Internet

* [IETF - RFC 9110: HTTP Semantics](https://datatracker.ietf.org/doc/html/rfc9110) - Métodos HTTP (GET, POST, PUT, DELETE, PATCH), idempotência, segurança e cabeçalhos.
* [OpenAPI Specification v3.1.0 (OAS)](https://spec.openapis.org/oas/latest.html) - Estrutura de especificação formal para documentação interoperável de APIs RESTful.
* [GraphQL Official Documentation - Learn GraphQL](https://graphql.org/learn/) - Schemas, tipos, queries, mutations, resolvers e prevenção de over-fetching e under-fetching.
* [MDN Web Docs - WebSockets API](https://developer.mozilla.org/pt-BR/docs/Web/API/WebSockets_API) - Comunicação full-duplex bidirecional sobre uma única conexão TCP persistente.
* [Martin Fowler - Richardson Maturity Model](https://martinfowler.com/articles/richardsonMaturityModel.html) - Os quatro níveis de maturidade de serviços REST (Nível 0 a 3 / HATEOAS).
* FIELDING, Roy Thomas. **Architectural Styles and the Design of Network-based Software Architectures**. Tese de Doutorado. University of California, Irvine, 2000. (Cap. 5 - Representational State Transfer - REST).
* ALLAMARAJU, Subbu. **Arquitetura de Web Services RESTful**. Rio de Janeiro: Alta Books, 2011. (Cap. 2 e 3 - O Protocolo HTTP e Recursos REST).
* PORCELLO, Eve; BANKS, Alex. **Aprendendo GraphQL: Declarativo, Orientado a Dados e Eficiente**. São Paulo: Novatec, 2019. (Cap. 3 e 4 - Esquemas e Resoluções de Consultas).
