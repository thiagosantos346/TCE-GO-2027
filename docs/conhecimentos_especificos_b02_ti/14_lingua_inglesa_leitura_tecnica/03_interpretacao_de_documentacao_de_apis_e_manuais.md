# 03 - Interpretação de Documentação de APIs, Manuais e Artigos

> **Matéria:** Língua Inglesa (Leitura Técnica)  
> **Cargo:** B02 – Técnico de Controle Externo – Especialidade: Tecnologia da Informação  
> **Arquivo:** `03_interpretacao_de_documentacao_de_apis_e_manuais.md`  



---


## 📌 Ementa / Itens do Edital
- Interpretação e leitura de documentações técnicas de APIs (REST, GraphQL)
- Interpretação de manuais de instalação, configuração e guias de software
- Leitura crítica de artigos científicos e papers de tecnologia da informação
- Linguagem prescritiva e advertências técnicas (RFC 2119: MUST, SHOULD, MAY)

---

## 🧭 Sumário

1. [Linguagem Normativa e Prescritiva de Engenharia (RFC 2119 / RFC 8174)](#1-linguagem-normativa-e-prescritiva-de-engenharia-rfc-2119-rfc-8174)
    1. [Os Níveis Normativos Canônicos](#11-os-niveis-normativos-canonicos)
    2. [Matriz de Conformidade Técnica da RFC 2119](#12-matriz-de-conformidade-tecnica-da-rfc-2119)
    3. [Teste 585](#Teste-585)
    4. [Teste 586](#Teste-586)
    5. [Teste 587](#Teste-587)
2. [Interpretação de Documentação de APIs (REST, OpenAPI, Swagger e GraphQL)](#2-interpretacao-de-documentacao-de-apis-rest-openapi-swagger-e-graphql)
    1. [Estrutura de Rotas, Métodos HTTP e Idempotência](#21-estrutura-de-rotas-metodos-http-e-idempotencia)
    2. [Parâmetros de Requisição e Schemas de Dados JSON](#22-parametros-de-requisicao-e-schemas-de-dados-json)
    3. [Códigos de Status HTTP Críticos e Cabeçalhos de Resposta](#23-codigos-de-status-http-criticos-e-cabecalhos-de-resposta)
    4. [Documentação de APIs GraphQL (Queries, Mutations e Types)](#24-documentacao-de-apis-graphql-queries-mutations-e-types)
    5. [Teste 588](#Teste-588)
    6. [Teste 589](#Teste-589)
    7. [Teste 590](#Teste-590)
    8. [Teste 591](#Teste-591)
3. [Interpretação de Manuais Técnicos e Guias de Configuração de Sistemas](#3-interpretacao-de-manuais-tecnicos-e-guias-de-configuracao-de-sistemas)
    1. [Verbos Operacionais no Modo Imperativo](#31-verbos-operacionais-no-modo-imperativo)
    2. [Seções Estruturantes de um Manual de Implantação](#32-secoes-estruturantes-de-um-manual-de-implantacao)
    3. [Categorização e Gravidade das Advertências Técnicas](#33-categorizacao-e-gravidade-das-advertencias-tecnicas)
    4. [Ciclo de Vida: Deprecated vs. Decommissioned](#34-ciclo-de-vida-deprecated-vs-decommissioned)
    5. [Teste 592](#Teste-592)
4. [Leitura Crítica de Artigos Científicos e Papers de TI (IEEE / ACM / ArXiv)](#4-leitura-critica-de-artigos-cientificos-e-papers-de-ti-ieee-acm-arxiv)
    1. [Anatomia Estrutural de um Artigo de Vanguarda](#41-anatomia-estrutural-de-um-artigo-de-vanguarda)
    2. [A Metodologia Three-Pass sob Pressão de Tempo de Prova](#42-a-metodologia-three-pass-sob-pressao-de-tempo-de-prova)
    3. [Léxico de Validação Experimental e Evidências Empíricas](#43-lexico-de-validacao-experimental-e-evidencias-empiricas)
    4. [Teste 593](#Teste-593)
    5. [Teste 594](#Teste-594)
6. [Fontes Recomendadas na Internet](#6-fontes-recomendadas-na-internet)

---

## 1. Linguagem Normativa e Prescritiva de Engenharia (RFC 2119 / RFC 8174)

Nas áreas de engenharia de software, redes de comunicação e governança de tecnologia avaliadas pela Fundação Carlos Chagas (FCC), a leitura de especificações técnicas formais (padrões da IETF, W3C, ISO/IEC e NIST) exige a compreensão rigorosa dos **termos normativos prescritivos grafados em letras maiúsculas**, disciplinados pela clássica **RFC 2119** (e reafirmados pela RFC 8174).

Esses vocábulos não exercem função decorativa ou meramente estilística; constituem **imposições contratuais e técnicas de conformidade estrita**.

```mermaid
flowchart TD
    RFC["Níveis Normativos de Exigência (RFC 2119)"]
    
    RFC --> L1["Nível 1: Exigência Absoluta<br/>MUST / SHALL / REQUIRED"]
    RFC --> L2["Nível 2: Proibição Absoluta<br/>MUST NOT / SHALL NOT"]
    RFC --> L3["Nível 3: Recomendação Firme<br/>SHOULD / RECOMMENDED"]
    RFC --> L4["Nível 4: Desaconselhamento Firme<br/>SHOULD NOT / NOT RECOMMENDED"]
    RFC --> L5["Nível 5: Opcionalidade Pura<br/>MAY / OPTIONAL"]
    
    L1 --> E1["Violação = Não-Conformidade / Rejeição"]
    L2 --> E1
    L3 --> E2["Exceção Demanda Justificativa Técnica Documentada"]
    L4 --> E2
    L5 --> E3["Escolha Discricionária do Implementador"]
```

### 1.1 Os Níveis Normativos Canônicos

1. **MUST / SHALL / REQUIRED (Obrigatório / Mandatório):** Designam uma exigência absoluta da especificação (*absolute requirement*). O sistema, serviço ou cliente que não implementar ou violar este item é classificado como em **não-conformidade** (*non-compliant*).
2. **MUST NOT / SHALL NOT (Terminantemente Proibido):** Expressam um veto categórico (*absolute prohibition*). A inclusão do comportamento vedado invalida a conformidade da solução perante o padrão internacional.
3. **SHOULD / RECOMMENDED (Fortemente Recomendado):** Indicam que o comportamento prescrito representa a boa prática recomendada. Podem existir razões válidas em circunstâncias particulares para ignorar a diretriz, mas as implicações técnicas de tal desvio devem ser plenamente compreendidas, avaliadas e formalmente documentadas.
4. **SHOULD NOT / NOT RECOMMENDED (Fortemente Desaconselhado):** Expressam que determinada conduta técnica deve ser evitada sob condições normais de operação. Desvios somente são tolerados em situações excepcionais de contorno devidamente motivadas.
5. **MAY / OPTIONAL (Opcional / Facultativo):** Indicam um recurso verdadeiramente opcional (*truly optional*). O implementador detém a faculdade discricionária de incluir ou omitir o atributo sem comprometer a interoperabilidade com outros sistemas que seguem o padrão.

### 1.2 Matriz de Conformidade Técnica da RFC 2119

| Termo em Maiúsculas | Definição Oficial IETF | Significado Prático em Auditoria e TI | O que NÃO Significa (Pegadinha FCC) |
| :--- | :--- | :--- | :--- |
| **MUST** / **SHALL** / **REQUIRED** | Exigência absoluta da especificação. | Mandatório. Ausência implica rejeição e não-conformidade estrita. | NÃO é sugestão, boa prática ou opcionalidade. |
| **MUST NOT** / **SHALL NOT** | Proibição absoluta da especificação. | Proibição expressa. Qualquer execução viola o padrão. | NÃO é mera ressalva dispensável. |
| **SHOULD** / **RECOMMENDED** | Fortemente recomendado com abertura para exceções fundamentadas. | Padrão ouro a ser seguido; desvios exigem justificativa técnica formal. | NÃO é uma imposição cega inegociável, e NÃO é uma opção arbitrária sem critérios. |
| **SHOULD NOT** / **NOT RECOMMENDED** | Desaconselhamento enfático em operação padrão. | Conduta indesejada; implementação aceitável apenas em exceções marginais. | NÃO é um veto absoluto em 100% dos casos marginais. |
| **MAY** / **OPTIONAL** | Funcionalidade totalmente discricionária. | Facultativo. Não gera penalidades de conformidade. | NÃO é uma recomendação preferencial e NÃO é obrigatório. |

> 🚨 **ALERTA DE PROVA / PEGADINHA FCC:**  
> A FCC adora afirmar que o termo **"SHOULD"** impõe um mandamento inegociável sob qualquer pretexto. Trata-se de erro recorrente. A RFC 2119 expressamente ressalva que podem existir cenários peculiares que justifiquem a não observância do *SHOULD*, cabendo ao engenheiro mensurar os impactos (*the full implications must be understood and carefully weighed*).

---

### Teste 585
**(FCC – TRT 14ª – 2016 – Analista Judiciário - Apoio Especializado - Tecnologia da Informação)**
Dentre as categorias de controles gerais que devem ser consideradas em um processo de auditoria de sistemas estão os controles de

* **A)** eliminar o sistema que gerou o risco, visando reduzir o risco.
* **B)** atuar sobre os ativos que sofrem as consequências do risco, visando eliminar o risco.
* **C)** escolher apenas uma alternativa que seja economicamente viável, já que é impossível reter o risco.
* **D)** utilizar sempre medidas de caráter contingencial ou mitigatório, evitando-se as medidas preventivas.
* **E)** transferir o risco, por meio de seguros, cooperação ou outra ação adequada.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "eliminar o sistema que gerou o risco, visando reduzir o risco". De acordo com a teoria estudada em *1.1 Os Níveis Normativos Canônicos*, mUST / SHALL / REQUIRED (Obrigatório / Mandatório): Designam uma exigência absoluta da especificação (*absolute requirement*). O sistema, serviço ou cliente que não implementar ou violar este item é classificado como em não-conformidade (*non-compliant*).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "atuar sobre os ativos que sofrem as consequências do risco, visando eliminar o risco". De acordo com a teoria estudada em *3.3 Categorização e Gravidade das Advertências Técnicas*, as caixas de alerta dos manuais de engenharia são padronizadas por nível de risco.
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "escolher apenas uma alternativa que seja economicamente viável, já que é impossível reter o risco". De acordo com a teoria estudada em *3.3 Categorização e Gravidade das Advertências Técnicas*, caution (Cuidado): Risco de comportamento inesperado, degradação severa de desempenho ou instabilidade na topologia (ex.: formar clusters com número par de nós, arriscando *split-brain*).
> - **D)** **Correta.** Conforme fundamentado na seção *1.1 Os Níveis Normativos Canônicos* deste guia, podem existir razões válidas em circunstâncias particulares para ignorar a diretriz, mas as implicações técnicas de tal desvio devem ser plenamente compreendidas, avaliadas e formalmente documentadas. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 14ª/2016) ao estabelecer que "utilizar sempre medidas de caráter contingencial ou mitigatório, evitando-se as medidas preventivas".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "transferir o risco, por meio de seguros, cooperação ou outra ação adequada". De acordo com a teoria estudada em *2.1 Estrutura de Rotas, Métodos HTTP e Idempotência*, o design RESTful organiza as interações por meio de URIs de recursos e verbos padronizados pelo protocolo HTTP.
>
> **Gabarito: D**

---

### Teste 586
**(CEBRASPE – TRT/10 – 2013 – Analista Judiciario Tecnologia Da Informacao)**
O ciclo de vida de um software, entre outras características, está relacionado aos estágios de concepção, projeto, criação e implementação.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Correta.** O item está **Certo**. Conforme fundamentado na seção *3.4 Ciclo de Vida: Deprecated vs. Decommissioned* deste guia, a correta interpretação do ciclo de vida de componentes de software é essencial para a gestão e auditoria de TI. Dessa forma, está plenamente correta a proposição da banca (CEBRASPE – TRT/10/2013) ao afirmar que "O ciclo de vida de um software, entre outras características, está relacionado aos estágios de concepção...".
> - **E)** **Incorreta.** A marcação como **Errado** não procede, visto que a assertiva guarda integral conformidade com a teoria estudada em *3.4 Ciclo de Vida: Deprecated vs. Decommissioned*, segundo a qual deprecated (Descontinuado / Tornado Obsoleto): O método, protocolo ou versão continua plenamente funcional na versão em execução do software.
>
> **Gabarito: C**

---

### Teste 587
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
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "ativo intangível". De acordo com a teoria estudada em *1. Linguagem Normativa e Prescritiva de Engenharia (RFC 2119 / RFC 8174)*, esses vocábulos não exercem função decorativa ou meramente estilística; constituem imposições contratuais e técnicas de conformidade estrita.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Investimentos". De acordo com a teoria estudada em *3.3 Categorização e Gravidade das Advertências Técnicas*, as caixas de alerta dos manuais de engenharia são padronizadas por nível de risco.
> - **C)** **Correta.** Conforme fundamentado na seção *1. Linguagem Normativa e Prescritiva de Engenharia (RFC 2119 / RFC 8174)* deste guia, nas áreas de engenharia de software, redes de comunicação e governança de tecnologia avaliadas pela Fundação Carlos Chagas (FCC), a leitura de especificações técnicas formais (padrões da IETF, W3C, ISO/IEC e NIST) exige a compreensão rigorosa dos termos normativos prescritivos grafados em letras maiúsculas, disciplinados pela clássica RFC 2119 (e reafirmados pela RFC 8174). Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT da 24º Região/2025) ao estabelecer que "ativo Imobilizado".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "ativo circulante". De acordo com a teoria estudada em *1.1 Os Níveis Normativos Canônicos*, podem existir razões válidas em circunstâncias particulares para ignorar a diretriz, mas as implicações técnicas de tal desvio devem ser plenamente compreendidas, avaliadas e formalmente documentadas.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "ativo realizável a longo prazo". De acordo com a teoria estudada em *3.3 Categorização e Gravidade das Advertências Técnicas*, note / Tip (Nota / Dica): Informação complementar útil ou sugestão de atalho operacional.
>
> **Gabarito: C**

---

## 2. Interpretação de Documentação de APIs (REST, OpenAPI, Swagger e GraphQL)

A análise de contratos de interface entre sistemas constitui atividade primordial tanto no desenvolvimento quanto na auditoria de dados fiscais e orçamentários.

```mermaid
sequenceDiagram
    autonumber
    actor Client as "Cliente / Auditoria de TI"
    participant Gateway as "API Gateway"
    participant Backend as "Microsserviço de Negócio"
    
    Client->>Gateway: POST /v1/audits (Headers: Authorization, Content-Type) + JSON Body
    alt Token ausente ou expirado
        Gateway-->>Client: 401 Unauthorized (Header: WWW-Authenticate)
    else Usuário sem escopo 'audit:write'
        Gateway-->>Client: 403 Forbidden (Permissão insuficiente)
    else Cota de chamadas excedida
        Gateway-->>Client: 429 Too Many Requests (Header: Retry-After: 120)
    else Payload com erro semântico de regra de negócio
        Gateway->>Backend: Encaminha requisição
        Backend-->>Gateway: 422 Unprocessable Entity
        Gateway-->>Client: 422 Unprocessable Entity
    else Requisição válida e processada
        Gateway->>Backend: Encaminha requisição
        Backend-->>Gateway: 201 Created (JSON com ID do recurso)
        Gateway-->>Client: 201 Created
    end
```

### 2.1 Estrutura de Rotas, Métodos HTTP e Idempotência

O design RESTful organiza as interações por meio de URIs de recursos e verbos padronizados pelo protocolo HTTP:

- **GET:** Recupera a representação de um recurso. Operação **segura** (não altera o estado no servidor) e **idempotente** (múltiplas chamadas idênticas produzem o mesmo efeito de uma única chamada).
- **POST:** Submete dados para criação de novo recurso ou processamento interno. Operação **não-segura** e **não-idempotente** (cada envio gera uma nova entidade ou cobrança).
- **PUT:** Substitui integralmente o recurso existente na URI especificada. Operação **idempotente**.
- **PATCH:** Aplica modificações parciais a atributos pontuais do recurso.
- **DELETE:** Remove o recurso indicado. Operação **idempotente** (a exclusão de um recurso já excluído mantém o estado de recurso ausente).

### 2.2 Parâmetros de Requisição e Schemas de Dados JSON

Nas especificações OpenAPI 3.0 / Swagger, os parâmetros distribuem-se em quatro categorias fundamentais:

- **Path Parameters (`/taxpayers/{id}`):** Integram a hierarquia da URL e identificam instâncias unívocas de recursos. São invariavelmente obrigatórios.
- **Query Parameters (`?fiscal_year=2026&status=audited&limit=50&offset=100`):** Utilizados para filtragem, ordenação (*sorting*) e paginação de coleções.
- **Header Parameters:** Transportam metadados essenciais de rede e segurança:
    - `Authorization: Bearer <token_jwt>`: Credencial criptográfica de autenticação.
    - `Content-Type: application/json`: Informa a codificação do payload transmitido.
    - `Accept: application/json`: Comunica o formato que o cliente está apto a receber.
- **Request Body (Corpo da Requisição / Payload):** Estrutura hierárquica contendo os campos de dados:
    - `required: true`: Sinaliza que o bloco ou os campos listados no array `required:` são indispensáveis. A omissão acarreta rejeição da mensagem.
    - `properties`: Mapeia cada atributo com suas restrições de validação (`type: string`, `pattern: '^\d{14}$'`, `minimum: 0.0`).

### 2.3 Códigos de Status HTTP Críticos e Cabeçalhos de Resposta

A compreensão precisa das famílias de códigos de status HTTP é intensamente avaliada em provas:

- **Família 2xx (Success):**
    - `200 OK`: Requisição bem-sucedida com retorno de dados.
    - `201 Created`: Criação bem-sucedida de um novo recurso no servidor (resposta clássica a `POST`).
    - `204 No Content`: Ação processada com êxito, sem corpo textual de retorno (comum em `DELETE`).
- **Família 4xx (Client Error - Erros Originados no Cliente):**
    - `400 Bad Request`: Erro de sintaxe da requisição (JSON malformado, quebra de delimitadores, tipos primitivos ilegíveis).
    - `401 Unauthorized`: Falha de **autenticação**. O cliente não forneceu credenciais válidas ou o token expirou.
    - `403 Forbidden`: O cliente está autenticado com sucesso, mas suas permissões/papéis (*roles*) **não autorizam** o acesso à rota solicitada.
    - `404 Not Found`: A URI solicitada não corresponde a nenhum recurso existente.
    - `409 Conflict`: Conflito com o estado atual do recurso (ex.: tentativa de cadastrar registro com chave primária já existente).
    - `422 Unprocessable Entity`: A sintaxe do JSON está impecável, mas os dados contêm **erros semânticos ou violações de regras de negócio** (ex.: valor negativo em receita declarada, CPF com dígitos verificadores inválidos).
    - `429 Too Many Requests`: Limite de taxa de requisições excedido (*rate limiting / throttling*). Vem associado ao cabeçalho `Retry-After: <segundos>`, que estipula o tempo de espera obrigatório antes de nova tentativa.
- **Família 5xx (Server Error - Falhas Internas do Provedor):**
    - `500 Internal Server Error`: Exceção inesperada não tratada pela aplicação.
    - `502 Bad Gateway`: O proxy reverso ou gateway recebeu resposta corrompida do microsserviço de backend.
    - `503 Service Unavailable`: Servidor temporariamente incapacitado por sobrecarga ou manutenção programada.
    - `504 Gateway Timeout`: O gateway expirou aguardando a resposta do serviço interno.

> 💡 **Diferença Crítica FCC (401 vs. 403):**  
>
> - **401 Unauthorized** $\rightarrow$ *Quem é você?* (Problema de Identidade / Autenticação).  
> - **403 Forbidden** $\rightarrow$ *Eu sei quem você é, mas você não tem permissão para entrar aqui.* (Problema de Privilégio / Autorização).

### 2.4 Documentação de APIs GraphQL (Queries, Mutations e Types)

Diferentemente do padrão REST, no qual cada recurso ocupa uma URI distinta, o padrão GraphQL opera via endpoint único (`POST /graphql`). A documentação orienta-se por esquemas de tipagem estrita (*Schema Definition Language - SDL*):

- **Query:** Operação de consulta somente-leitura.
- **Mutation:** Operação de escrita que gera efeitos colaterais de criação, atualização ou remoção.
- **Modifiers de Obrigatoriedade:** O caractere de exclamação `!` ao final do tipo indica campo não-nulo e mandatório (ex.: `id: ID!`, `revenue: Float!`).

---

### Teste 588
**(FCC – TRT 13ª – 2014 – Analista Judiciário - Tecnologia da Informação)**
O OSPF − Open Shortest Path First é um dos protocolos de roteamento, do tipo IGP − Interior Gateway Protocol, mais utilizados em redes de grande dimensão. Se, comparado com o OSPF, o BGP

* **A)** é baseado no estado do link e o OSPF, no vetor de distâncias.
* **B)** é utilizado como IGP em redes locais pequenas e o OSPF, para redes grandes.
* **C)** faz uso do protocolo de transporte e o OSPF não faz uso do protocolo de transporte.
* **D)** é mais simples que o OSPF, sendo assim, menos eficiente como IGP.
* **E)** opera dentro de uma única rede local e o OSPF opera sobre várias.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "é baseado no estado do link e o OSPF, no vetor de distâncias". De acordo com a teoria estudada em *3.4 Ciclo de Vida: Deprecated vs. Decommissioned*, deprecated (Descontinuado / Tornado Obsoleto): O método, protocolo ou versão continua plenamente funcional na versão em execução do software.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "é utilizado como IGP em redes locais pequenas e o OSPF, para redes grandes". De acordo com a teoria estudada em *1. Linguagem Normativa e Prescritiva de Engenharia (RFC 2119 / RFC 8174)*, nas áreas de engenharia de software, redes de comunicação e governança de tecnologia avaliadas pela Fundação Carlos Chagas (FCC), a leitura de especificações técnicas formais (padrões da IETF, W3C, ISO/IEC e NIST) exige a compreensão rigorosa dos termos normativos prescritivos grafados em letras maiúsculas, disciplinados pela clássica RFC 2119 (e reafirmados pela RFC 8174).
> - **C)** **Correta.** Conforme fundamentado na seção *2.1 Estrutura de Rotas, Métodos HTTP e Idempotência* deste guia, o design RESTful organiza as interações por meio de URIs de recursos e verbos padronizados pelo protocolo HTTP. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 13ª/2014) ao estabelecer que "faz uso do protocolo de transporte e o OSPF não faz uso do protocolo de transporte".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "é mais simples que o OSPF, sendo assim, menos eficiente como IGP". De acordo com a teoria estudada em *4.3 Léxico de Validação Experimental e Evidências Empíricas*, tail Latency (Latência de Cauda - P99 / P99.9): O tempo de resposta experimentado pelos percentis mais lentos das requisições; indicador crítico em sistemas de tempo real.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "opera dentro de uma única rede local e o OSPF opera sobre várias". De acordo com a teoria estudada em *2.1 Estrutura de Rotas, Métodos HTTP e Idempotência*, gET: Recupera a representação de um recurso. Operação segura (não altera o estado no servidor) e idempotente (múltiplas chamadas idênticas produzem o mesmo efeito de uma única chamada).
>
> **Gabarito: C**

---

### Teste 589
**(FGV – TRT/DA – 2025 – Tecnico Judiciario Area Administrativa Agente Da Policia Judicial)**
Para que a vigilância de áreas internas e externas seja efetiva, é necessário seguir o seguinte roteiro: identificação de riscos, mitigação de riscos e elaboração de plano de contingência. Assinale a opção que apresenta duas ações que contribuem com a identificação de riscos.

* **A)** Avaliação da edificação e vulnerabilidade do acervo.
* **B)** Guarda do acervo com critérios de seguranças e identificação de serviços de emergência.
* **C)** Vulnerabilidade do acervo e treinamento de equipes.
* **D)** Métodos de recuperação dos acervos e avaliação do sistema de combate a incêndio.
* **E)** Utilização de diário de ocorrências e manutenção da edificação.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *2.3 Códigos de Status HTTP Críticos e Cabeçalhos de Resposta* deste guia, família 5xx (Server Error - Falhas Internas do Provedor). Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT/DA/2025) ao estabelecer que "Avaliação da edificação e vulnerabilidade do acervo".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Guarda do acervo com critérios de seguranças e identificação de serviços de emergência". De acordo com a teoria estudada em *1.2 Matriz de Conformidade Técnica da RFC 2119*, sHOULD / RECOMMENDED: Fortemente recomendado com abertura para exceções fundamentadas. — Padrão ouro a ser seguido; desvios exigem justificativa técnica formal. — NÃO é uma imposição cega inegociável, e NÃO é uma opção arbitrária sem critérios.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Vulnerabilidade do acervo e treinamento de equipes". De acordo com a teoria estudada em *1. Linguagem Normativa e Prescritiva de Engenharia (RFC 2119 / RFC 8174)*, nas áreas de engenharia de software, redes de comunicação e governança de tecnologia avaliadas pela Fundação Carlos Chagas (FCC), a leitura de especificações técnicas formais (padrões da IETF, W3C, ISO/IEC e NIST) exige a compreensão rigorosa dos termos normativos prescritivos grafados em letras maiúsculas, disciplinados pela clássica RFC 2119 (e reafirmados pela RFC 8174).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Métodos de recuperação dos acervos e avaliação do sistema de combate a incêndio". De acordo com a teoria estudada em *1.1 Os Níveis Normativos Canônicos*, mUST / SHALL / REQUIRED (Obrigatório / Mandatório): Designam uma exigência absoluta da especificação (*absolute requirement*). O sistema, serviço ou cliente que não implementar ou violar este item é classificado como em não-conformidade (*non-compliant*).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Utilização de diário de ocorrências e manutenção da edificação". De acordo com a teoria estudada em *2.3 Códigos de Status HTTP Críticos e Cabeçalhos de Resposta*, `503 Service Unavailable`: Servidor temporariamente incapacitado por sobrecarga ou manutenção programada.
>
> **Gabarito: A**

---

### Teste 590
**(CEBRASPE – STJ – 2015 – Analista Judiciario Suporte Em Tecnologia Da Informacao)**
Um conjunto redundante de discos independentes (RAID) pode ser implementado tanto em software quanto em hardware.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Correta.** O item está **Certo**. Conforme fundamentado na seção *2. Interpretação de Documentação de APIs (REST, OpenAPI, Swagger e GraphQL)* deste guia, a análise de contratos de interface entre sistemas constitui atividade primordial tanto no desenvolvimento quanto na auditoria de dados fiscais e orçamentários. Dessa forma, está plenamente correta a proposição da banca (CEBRASPE – STJ/2015) ao afirmar que "Um conjunto redundante de discos independentes (RAID) pode ser implementado tanto em software quanto em...".
> - **E)** **Incorreta.** A marcação como **Errado** não procede, visto que a assertiva guarda integral conformidade com a teoria estudada em *4. Leitura Crítica de Artigos Científicos e Papers de TI (IEEE / ACM / ArXiv)*, segundo a qual em certames da FCC para cargos de alta remuneração de Tecnologia da Informação, os textos de prova costumam ser extraídos de publicações acadêmicas e anais de conferências de renome mundial (como *IEEE Transactions on Software Engineering, ACM SIGMOD, USENIX OSDI*).
>
> **Gabarito: C**

---

### Teste 591
**(FGV – TJ/AP – 2023 – Analista Judiciario Apoio Especializado Tecnologia Da Informacao Seguranca Da Informacao)**
Gilberto trabalha no setor de segurança do Tribunal de Justiça do Amapá (TJAP) e está fazendo a modelagem de possíveis ameaças aos seus sistemas, aplicativos, redes e serviços. Após pesquisar alguns modelos, decidiu realizar a modelagem seguindo o STRIDE (Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege). O modelo relaciona as ameaças do acrônimo STRIDE com as propriedades de segurança. Inicialmente, Gilberto trabalhará na propriedade de integridade. Logo, dentro do acrônimo STRIDE, a ameaça a ser trabalhada por Gilberto será:

* **A)** spoofing;
* **B)** tampering;
* **C)** repudiation;
* **D)** information disclosure;
* **E)** denial of service.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "spoofing". De acordo com a teoria estudada em *2.2 Parâmetros de Requisição e Schemas de Dados JSON*, header Parameters: Transportam metadados essenciais de rede e segurança.
> - **B)** **Correta.** Conforme fundamentado na seção *2.3 Códigos de Status HTTP Críticos e Cabeçalhos de Resposta* deste guia, `503 Service Unavailable`: Servidor temporariamente incapacitado por sobrecarga ou manutenção programada. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/AP/2023) ao estabelecer que "tampering".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "repudiation". De acordo com a teoria estudada em *2. Interpretação de Documentação de APIs (REST, OpenAPI, Swagger e GraphQL)*, a análise de contratos de interface entre sistemas constitui atividade primordial tanto no desenvolvimento quanto na auditoria de dados fiscais e orçamentários.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "information disclosure". De acordo com a teoria estudada em *1. Linguagem Normativa e Prescritiva de Engenharia (RFC 2119 / RFC 8174)*, nas áreas de engenharia de software, redes de comunicação e governança de tecnologia avaliadas pela Fundação Carlos Chagas (FCC), a leitura de especificações técnicas formais (padrões da IETF, W3C, ISO/IEC e NIST) exige a compreensão rigorosa dos termos normativos prescritivos grafados em letras maiúsculas, disciplinados pela clássica RFC 2119 (e reafirmados pela RFC 8174).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "denial of service". De acordo com a teoria estudada em *3.1 Verbos Operacionais no Modo Imperativo*, enforce: *"Enforce least-privilege IAM policies"* $\rightarrow$ *Imponha / faça cumprir* políticas de menor privilégio.
>
> **Gabarito: B**

---

## 3. Interpretação de Manuais Técnicos e Guias de Configuração de Sistemas

Manuais operacionais de infraestrutura (Linux manpages, guias do Kubernetes, PostgreSQL, Docker) empregam linguagem estritamente procedimental e estruturada.

### 3.1 Verbos Operacionais no Modo Imperativo

No manual técnico, instruções diretas abrem as sentenças com o verbo no infinitivo sem "to", expressando comando executivo:

- **Ensure:** *"Ensure that NTP synchronization is active before joining nodes"* $\rightarrow$ *Garanta que* a sincronização de relógio esteja ativa.
- **Provision:** *"Provision persistent storage classes with dynamic allocation"* $\rightarrow$ *Aloque / provisione* classes de armazenamento.
- **Purge / Prune:** *"Prune unreferenced objects to recover disk blocks"* $\rightarrow$ *Expurgue / limpe* objetos não referenciados.
- **Enforce:** *"Enforce least-privilege IAM policies"* $\rightarrow$ *Imponha / faça cumprir* políticas de menor privilégio.
- **Bypass:** *"Do not attempt to bypass input sanitation filters"* $\rightarrow$ *Não tente burlar / contornar* filtros de sanitização.

### 3.2 Seções Estruturantes de um Manual de Implantação

1. **Overview / Architecture:** Visão conceitual e topologia do sistema.
2. **Prerequisites (Pré-requisitos):** Condições mandatórias que devem ser atendidas antes da instalação (versão de kernel, bibliotecas, portas de firewall abertas). O descumprimento impede a instalação.
3. **Installation & Configuration:** Procedimentos passo a passo de implantação.
4. **Troubleshooting (Resolução de Problemas):** Procedimentos de diagnóstico e mitigação de erros comuns.

### 3.3 Categorização e Gravidade das Advertências Técnicas

As caixas de alerta dos manuais de engenharia são padronizadas por nível de risco:

- **Note / Tip (Nota / Dica):** Informação complementar útil ou sugestão de atalho operacional.
- **Important (Importante):** Diretriz de conformidade essencial; sua inobservância causa mau funcionamento do serviço.
- **Caution (Cuidado):** Risco de comportamento inesperado, degradação severa de desempenho ou instabilidade na topologia (ex.: formar clusters com número par de nós, arriscando *split-brain*).
- **Warning (Advertência):** Alerta formal de perda iminente de compatibilidade ou quebra de fluxo operacional.
- **Danger / Fatal (Perigo / Fatalidade):** Risco crítico de perda irreversível de dados, danos físicos ao hardware ou colapso total de segurança cibernética.

### 3.4 Ciclo de Vida: Deprecated vs. Decommissioned

A correta interpretação do ciclo de vida de componentes de software é essencial para a gestão e auditoria de TI:

- **Deprecated (Descontinuado / Tornado Obsoleto):** O método, protocolo ou versão **continua plenamente funcional** na versão em execução do software. Contudo, o fabricante adverte formalmente que o recurso não receberá novas funcionalidades nem suporte futuro, estando com remoção agendada. Não deve ser empregado em novos projetos.
- **Decommissioned / Removed (Descomissionado / Removido):** O recurso foi definitivamente excluído da base de código. Qualquer invocação resultará em erro imediato de método inexistente (`404` ou `410 Gone`).

---

### Teste 592
**(CEBRASPE – TRF/6 – 2025 – Analista Judiciario Apoio Especializado Tecnologia Da Informacao)**
A documentação técnica referente à API dos microsserviços desenvolvidos na PDPJ-Br deve seguir o padrão Swagger 2.0, a fim de garantir a compatibilidade com as Estratégia Nacional de Segurança Cibernética do Poder Judiciário (ENSEC-PJ), bem como na Portaria CNJ n.º 162/2021, que aprova protocolos e manuais criados pela referida Resolução, julgue os itens seguintes.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Incorreta.** A marcação como **Certo** não procede, pois o enunciado apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A documentação técnica referente à API dos microsserviços desenvolvidos na PDPJ-Br deve seguir o padrão...". De acordo com a teoria estudada em *2. Interpretação de Documentação de APIs (REST, OpenAPI, Swagger e GraphQL)*, a análise de contratos de interface entre sistemas constitui atividade primordial tanto no desenvolvimento quanto na auditoria de dados fiscais e orçamentários.
> - **E)** **Correta.** O item está **Errado** (gabarito oficial: **E**). Conforme fundamentado na seção *3.3 Categorização e Gravidade das Advertências Técnicas* deste guia, danger / Fatal (Perigo / Fatalidade): Risco crítico de perda irreversível de dados, danos físicos ao hardware ou colapso total de segurança cibernética. Portanto, a assertiva examinada pela banca (CEBRASPE – TRF/6/2025) viola os preceitos técnicos do tópico.
>
> **Gabarito: E**

---

## 4. Leitura Crítica de Artigos Científicos e Papers de TI (IEEE / ACM / ArXiv)

Em certames da FCC para cargos de alta remuneração de Tecnologia da Informação, os textos de prova costumam ser extraídos de publicações acadêmicas e anais de conferências de renome mundial (como *IEEE Transactions on Software Engineering, ACM SIGMOD, USENIX OSDI*).

### 4.1 Anatomia Estrutural de um Artigo de Vanguarda

```mermaid
flowchart TD
    P["Artigo Científico de TI (IEEE / ACM)"]
    
    P --> A1["1. Title & Abstract<br/>(Resumo de alto impacto: problema, método e ganhos quantitativos)"]
    P --> A2["2. Introduction<br/>(Contextualização da lacuna tecnológica e contribuições explícitas)"]
    P --> A3["3. Related Work<br/>(Comparação crítica com a literatura existente)"]
    P --> A4["4. Proposed Architecture / Model<br/>(Formalização matemática e engenharia da solução proposta)"]
    P --> A5["5. Experimental Evaluation<br/>(Datasets, benchmarks de carga, latência, throughput e overhead)"]
    P --> A6["6. Conclusion & Future Work<br/>(Síntese dos achados empíricos e trabalhos futuros)"]
```

1. **Title & Abstract:** O núcleo de maior densidade do paper. Sintetiza a motivação central, a fraqueza das abordagens tradicionais, a solução inovadora formulada e os ganhos numéricos consolidados (ex.: redução de latência em 42%).
2. **Introduction:** Expõe a relevância do problema e lista textualmente as contribuições primárias do trabalho (*"In this paper, our main contributions are.."*).
3. **Related Work:** Confronta a solução com trabalhos anteriores (*prior art*).
4. **Proposed Architecture / Algorithm:** Detalhamento da arquitetura técnica ou algoritmo implementado.
5. **Experimental Evaluation & Discussion:** Apresentação rigorosa das métricas de desempenho sob carga de trabalho corporativa real (*enterprise workloads*).
6. **Threats to Validity:** Reconhecimento das premissas e limitações do estudo.
7. **Conclusion:** Recapitulação das deduções finais.

### 4.2 A Metodologia Three-Pass sob Pressão de Tempo de Prova

Conforme preconizado pelo Prof. S. Keshav, a leitura de papers em ambientes de prova deve ser estratificada em camadas:

- **Passada 1 (Abordagem Panorâmica - 3 a 5 minutos):** Leitura concentrada do título, do *Abstract*, da introdução preliminar e da conclusão final. Essa varredura inicial responde com clareza:
    - Qual o problema central atacado pelo autor?
    - A tecnologia proposta substitui ou aprimora os modelos vigentes?
    - O tom é de refutação ou de proposição de nova técnica?
- **Passada 2 (Varredura Analítica para Itens Específicos):** Inspeção de figuras de arquitetura, gráficos de desempenho e tabelas comparativas.

### 4.3 Léxico de Validação Experimental e Evidências Empíricas

- **Benchmark / Workload:** Carga de trabalho de teste executada para aferir limites operacionais de um sistema.
- **Tail Latency (Latência de Cauda - P99 / P99.9):** O tempo de resposta experimentado pelos percentis mais lentos das requisições; indicador crítico em sistemas de tempo real.
- **Overhead:** Custo operacional computacional marginal incorrido em ciclos de CPU, memória RAM ou rede para suportar a nova ferramenta (ex.: menos de 3% de consumo extra de CPU).
- **Outperform:** Superar o desempenho de uma solução concorrente (*"Our model outperforms traditional heuristics"*).

---

### Teste 593
**(FCC – TRT 1ª – 2014 – Analista Judiciário - Tecnologia da Informação)**
No contexto do gerenciamento de memória de um computador, tem-se uma técnica muito utilizada que consiste na divisão da memória física do computador em partições de tamanhos menores, visando o uso mais eficiente dessa memória. O nome atribuído a essa técnica é

* **A)** alocação dinâmica.
* **B)** emulação.
* **C)** paginação.
* **D)** swapping.
* **E)** parametrização.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "alocação dinâmica". De acordo com a teoria estudada em *4.3 Léxico de Validação Experimental e Evidências Empíricas*, tail Latency (Latência de Cauda - P99 / P99.9): O tempo de resposta experimentado pelos percentis mais lentos das requisições; indicador crítico em sistemas de tempo real.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "emulação". De acordo com a teoria estudada em *4.3 Léxico de Validação Experimental e Evidências Empíricas*, overhead: Custo operacional computacional marginal incorrido em ciclos de CPU, memória RAM ou rede para suportar a nova ferramenta (ex.: menos de 3% de consumo extra de CPU).
> - **C)** **Correta.** Conforme fundamentado na seção *2.2 Parâmetros de Requisição e Schemas de Dados JSON* deste guia, query Parameters (`?fiscal_year=2026&status=audited&limit=50&offset=100`): Utilizados para filtragem, ordenação (*sorting*) e paginação de coleções. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 1ª/2014) ao estabelecer que "paginação".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "swapping". De acordo com a teoria estudada em *4.1 Anatomia Estrutural de um Artigo de Vanguarda*, proposed Architecture / Algorithm: Detalhamento da arquitetura técnica ou algoritmo implementado.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "parametrização". De acordo com a teoria estudada em *4.2 A Metodologia Three-Pass sob Pressão de Tempo de Prova*, o tom é de refutação ou de proposição de nova técnica?.
>
> **Gabarito: C**

---

### Teste 594
**(CEBRASPE – TRF 6ª – 2025 – Analista Judiciário - Apoio Especializado - Governança e Gestão de Tecnologia da Informação)**
Os cilindros em BPMN, conhecidos como objetos de dados (data objects), representam informações utilizadas (data input) ou produzidas (data output) por atividades de processos.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Correta.** O item está **Certo**. Conforme fundamentado na seção *3.1 Verbos Operacionais no Modo Imperativo* deste guia, purge / Prune: *"Prune unreferenced objects to recover disk blocks"* $\rightarrow$ *Expurgue / limpe* objetos não referenciados. Dessa forma, está plenamente correta a proposição da banca (CEBRASPE – TRF 6ª/2025) ao afirmar que "Os cilindros em BPMN, conhecidos como objetos de dados (data objects), representam informações utilizadas...".
> - **E)** **Incorreta.** A marcação como **Errado** não procede, visto que a assertiva guarda integral conformidade com a teoria estudada em *3.1 Verbos Operacionais no Modo Imperativo*, segundo a qual bypass: *"Do not attempt to bypass input sanitation filters"* $\rightarrow$ *Não tente burlar / contornar* filtros de sanitização.
>
> **Gabarito: C**

---

## 6. Fontes Recomendadas na Internet

* [OpenAPI Specification 3.1.0 Official Documentation](https://spec.openapis.org/oas/v3.1.0) - Padrão de especificação formal em inglês para modelagem e consumo de interfaces RESTful.
* [IETF RFC 9110 - HTTP Semantics and Status Codes](https://datatracker.ietf.org/doc/html/rfc9110) - Norma de referência global em inglês para semântica de métodos, cabeçalhos e respostas de APIs na Web.
* [Docker Official Documentation - Dockerfile Reference (English)](https://docs.docker.com/reference/dockerfile/) - Manual técnico oficial para interpretação de comandos, sintaxe declarativa e boas práticas de containers.
* [Kubernetes Official Concepts - Pods and Workloads (English)](https://kubernetes.io/docs/concepts/workloads/pods/) - Documentação técnica primária em inglês para interpretação de especificações YAML e orquestração de microsserviços.
* [Google Technical Writing Courses - Organizing Complex Documents](https://developers.google.com/tech-writing/two) - Melhores práticas para leitura crítica e estruturação de manuais técnicos de arquitetura e APIs.
* SWALES, John M.; FEAK, Christine B. **Academic Writing for Graduate Students: Essential Tasks and Skills**. 3. ed. Ann Arbor: University of Michigan Press, 2012. (Unit 3 - Reading and Writing Technical Instructions).
* GLENDINNING, Eric H.; MCEWAN, John. **Oxford English for Information Technology**. 2. ed. Oxford: Oxford University Press, 2006. (Units 20 to 25 - Reading Technical Manuals and System Specifications).
* HEWINGS, Martin. **Advanced Grammar in Use**. 3. ed. Cambridge: Cambridge University Press, 2013. (Units 80 to 85 - Complex Sentences and Technical Documentation Structures).
