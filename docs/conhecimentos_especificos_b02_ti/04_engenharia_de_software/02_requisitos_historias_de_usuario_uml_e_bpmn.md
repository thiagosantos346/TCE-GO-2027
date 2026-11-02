# 02 - Requisitos, Histórias de Usuário, UML e BPMN

> **Matéria:** Engenharia de Software  
> **Cargo:** B02 – Técnico de Controle Externo – Especialidade: Tecnologia da Informação  
> **Arquivo:** `02_requisitos_historias_de_usuario_uml_e_bpmn.md`  



---


## 📌 Ementa / Itens do Edital
- Levantamento, especificação, análise, validação e gerenciamento de requisitos funcionais e não funcionais
- Histórias de usuário, casos de uso e critérios de aceite
- Modelagem de sistemas com UML (Unified Modeling Language)
- Modelagem de processos de negócio com BPMN (Business Process Model and Notation)

---

## 🧭 Sumário

1. [Engenharia de Requisitos de Software](#1-engenharia-de-requisitos-de-software)
    1. [Ciclo de Vida da Engenharia de Requisitos](#11-ciclo-de-vida-da-engenharia-de-requisitos)
    2. [Técnicas de Elicitação de Requisitos](#12-tecnicas-de-elicitacao-de-requisitos)
    3. [Requisitos Funcionais vs. Requisitos Não Funcionais (Taxonomia de Sommerville)](#13-requisitos-funcionais-vs-requisitos-nao-funcionais-taxonomia-de-sommerville)
    4. [Gerenciamento, Rastreabilidade e Mudança de Requisitos](#14-gerenciamento-rastreabilidade-e-mudanca-de-requisitos)
    5. [Teste 012](#Teste-012)
    6. [Teste 013](#Teste-013)
2. [Modelagem por Casos de Uso e Histórias de Usuário](#2-modelagem-por-casos-de-uso-e-historias-de-usuario)
    1. [Modelagem de Casos de Uso: Elementos e Relacionamentos («include» vs. «extend»)](#21-modelagem-de-casos-de-uso-elementos-e-relacionamentos-include-vs-extend)
    2. [Histórias de Usuário (User Stories) e os 3 Cs de Ron Jeffries](#22-historias-de-usuario-user-stories-e-os-3-cs-de-ron-jeffries)
    3. [Critérios de Aceite e o Padrão INVEST](#23-criterios-de-aceite-e-o-padrao-invest)
    4. [Teste 014](#Teste-014)
    5. [Teste 015](#Teste-015)
    6. [Teste 016](#Teste-016)
3. [Modelagem de Sistemas com UML (versão 2.5)](#3-modelagem-de-sistemas-com-uml-versao-25)
    1. [Taxonomia dos Diagramas UML: Estruturais vs. Comportamentais](#31-taxonomia-dos-diagramas-uml-estruturais-vs-comportamentais)
    2. [Diagrama de Classes: Visibilidade, Multiplicidade, Agregação e Composição](#32-diagrama-de-classes-visibilidade-multiplicidade-agregacao-e-composicao)
    3. [Diagramas de Sequência, Atividades e Máquina de Estados](#33-diagramas-de-sequencia-atividades-e-maquina-de-estados)
    4. [Teste 017](#Teste-017)
    5. [Teste 018](#Teste-018)
    6. [Teste 019](#Teste-019)
4. [Modelagem de Processos de Negócio com BPMN 2.0](#4-modelagem-de-processos-de-negocio-com-bpmn-20)
    1. [Elementos de Fluxo: Eventos, Atividades e Tipos de Tarefas](#41-elementos-de-fluxo-eventos-atividades-e-tipos-de-tarefas)
    2. [Gateways Decisórios no BPMN 2.0 (XOR, AND, OR e Event-based)](#42-gateways-decisorios-no-bpmn-20-xor-and-or-e-event-based)
    3. [Estruturas de Separação (Pools e Lanes) e Conectores de Sequência vs. Mensagem](#43-estruturas-de-separacao-pools-e-lanes-e-conectores-de-sequencia-vs-mensagem)
    4. [Teste 020](#Teste-020)
    5. [Teste 021](#Teste-021)
    6. [Teste 022](#Teste-022)
5. [Fontes Oficiais e Referências Bibliográficas](#5-fontes-oficiais-e-referencias-bibliograficas)

---

## 1. Engenharia de Requisitos de Software

### 1.1 Ciclo de Vida da Engenharia de Requisitos
A Engenharia de Requisitos é o processo disciplinado de descobrir, analisar, documentar e verificar os serviços fornecidos pelo sistema e suas restrições operacionais (Ian Sommerville). Divide-se em etapas interligadas:

1. **Concepção / Estudo de Viabilidade:** Avalia se o sistema contribui para os objetivos da organização e se é técnica e economicamente viável;
2. **Elicitação (Levantamento):** Identificação e descoberta dos requisitos junto aos clientes, usuários e demais partes interessadas (*stakeholders*);
3. **Análise e Negociação:** Detecção de conflitos entre requisitos de diferentes fontes, análise de completude, consistência e priorização de demandas;
4. **Especificação:** Documentação formal dos requisitos levantados por meio de documentos formais (Documento de Requisitos de Software - DRS), Casos de Uso ou Histórias de Usuário;
5. **Validação:** Verificação se os requisitos especificados refletem fielmente as reais necessidades do cliente (revisões técnicas, testes de protótipos e geração de casos de teste);
6. **Gerenciamento de Requisitos:** Processo contínuo de controle de versões, rastreabilidade e acomodação de mudanças ao longo do ciclo de vida.

### 1.2 Técnicas de Elicitação de Requisitos
A escolha das técnicas de elicitação depende da maturidade do domínio de negócio e do perfil dos usuários:

- **Entrevistas:** Técnicas estruturadas (fechadas) ou abertas. Excelentes para explorar detalhes e obter uma visão aprofundada dos processos de negócio;
- **Questionários e Pesquisas:** Eficientes para coletar impressões de uma base ampla de usuários geograficamente dispersa, com baixo custo, embora sujeita a respostas superficiais;
- **Workshops / JAD (Joint Application Design):** Sessões estruturadas e colaborativas que reúnem desenvolvedores, gerentes e clientes no mesmo espaço físico para alinhar requisitos divergentes e acelerar consensos;
- **Etnografia e Observação Direta:** O analista acompanha presencialmente a rotina operacional do usuário em seu ambiente real de trabalho. Revela requisitos implícitos e regras tácitas que os usuários costumam esquecer de relatar nas entrevistas;
- **Prototipação Rápida:** Construção de maquetes visuais ou versões interativas preliminares do sistema para permitir a validação antecipada de fluxos de navegação e layouts.

### 1.3 Requisitos Funcionais vs. Requisitos Não Funcionais (Taxonomia de Sommerville)
A distinção entre o que o sistema realiza e como ele realiza constitui o pilar conceitual da engenharia de requisitos:

```mermaid
flowchart TD
    REQ["Requisitos de Software"] --> RF["Requisitos Funcionais (RF)<br/>O QUE o sistema faz (serviços, cálculos, regras de negócio)"]
    REQ --> RNF["Requisitos Não Funcionais (RNF)<br/>COMO o sistema opera (qualidades globais e restrições)"]
    
    RNF --> RNF_PROD["Requisitos de Produto<br/>(Desempenho, Usabilidade, Confiabilidade, Portabilidade, Segurança)"]
    RNF --> RNF_ORG["Requisitos Organizacionais<br/>(Padrões de projeto, Linguagem de programação, Metodologia de entrega)"]
    RNF --> RNF_EXT["Requisitos Externos<br/>(Legislação, LGPD, Ética, Conformidade contábil/fiscal)"]
```

1. **Requisitos Funcionais (RF):** Descrevem as funções e comportamentos que o software deve executar. Especificam o que o sistema deve fazer em resposta a determinadas entradas, como reagir a situações específicas e quais cálculos realizar (ex.: *"O sistema deve calcular a alíquota previdenciária com base na remuneração bruta"*).
2. **Requisitos Não Funcionais (RNF):** Estabelecem propriedades de qualidade e restrições impostas aos serviços oferecidos pelo sistema. A taxonomia de Sommerville classifica os RNFs em:
    - *Requisitos de Produto:* Especificam o comportamento do produto em tempo de execução (desempenho, tempo de resposta, taxa de ocupação de memória, confiabilidade e disponibilidade mínima de 99,9%);
    - *Requisitos Organizacionais:* Decorrem das políticas e procedimentos da empresa cliente ou desenvolvedora (ex.: uso obrigatório de Java 21, versionamento no Git corporativo ou adoção da metodologia Scrum);
    - *Requisitos Externos:* Derivam de fatores externos ao sistema e à organização (ex.: aderência à Lei Geral de Proteção de Dados - LGPD, normas de interoperabilidade e regulamentações do Banco Central).

### 1.4 Gerenciamento, Rastreabilidade e Mudança de Requisitos
- **Rastreabilidade de Requisitos:** Capacidade de acompanhar o ciclo de vida de um requisito em ambas as direções:
    - *Rastreabilidade para trás (Backward traceability):* Liga o requisito à sua fonte originária (norma legal, entrevista ou necessidade de negócio);
    - *Rastreabilidade para frente (Forward traceability):* Liga o requisito aos módulos arquiteturais, classes, componentes e casos de teste que o implementam e validam;
- **Matriz de Rastreabilidade:** Tabela que mapeia a correlação bidirecional entre requisitos de usuário, requisitos de sistema, diagramas de arquitetura e casos de testes unitários.

---

### Teste 012
**(FCC – TRT-23 – Analista Judiciario Apoio Especializado Tecnologia da Informacao – 2016)**
Considere: I. Uma Especificação de Requisitos que reflete todas as decisões que foram tomadas e não contém cláusulas de pendências. Desta forma, contém todos os requisitos significativos relativos a funcionalidade, desempenho, restrições de desenho, atributos e interfaces externas, além de definir as respostas do software para todas as entradas possíveis, válidas e inválidas, em todas as situações possíveis. II. Uma Especificação de Requisitos em que todo requisito presente possui apenas uma única interpretação, aceita tanto pelos desenvolvedores quanto pelos usuários chaves. Em particular, ela é compreensível para todo o seu público alvo e é suficiente para a especificação dos testes de aceitação do produto. Os itens I e II descrevem especificações cujos requisitos contemplam, respectivamente, as qualidades

* **A)** rastreabilidade e consistência.
* **B)** completeza e precisão.
* **C)** correção e completeza.
* **D)** consistência e priorização.
* **E)** verificabilidade e precisão.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "rastreabilidade e consistência". De acordo com a teoria estudada em *1.1 Ciclo de Vida da Engenharia de Requisitos*, análise e Negociação: Detecção de conflitos entre requisitos de diferentes fontes, análise de completude, consistência e priorização de demandas.
> - **B)** **Correta.** Conforme fundamentado na seção *1.3 Requisitos Funcionais vs. Requisitos Não Funcionais (Taxonomia de Sommerville)* deste guia, especificam o que o sistema deve fazer em resposta a determinadas entradas, como reagir a situações específicas e quais cálculos realizar (ex.: *"O sistema deve calcular a alíquota previdenciária com base na remuneração bruta"*). Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT-23/2016) ao estabelecer que "completeza e precisão".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "correção e completeza". De acordo com a teoria estudada em *1.3 Requisitos Funcionais vs. Requisitos Não Funcionais (Taxonomia de Sommerville)*, *Requisitos de Produto:* Especificam o comportamento do produto em tempo de execução (desempenho, tempo de resposta, taxa de ocupação de memória, confiabilidade e disponibilidade mínima de 99,9%).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "consistência e priorização". De acordo com a teoria estudada em *1.2 Técnicas de Elicitação de Requisitos*, questionários e Pesquisas: Eficientes para coletar impressões de uma base ampla de usuários geograficamente dispersa, com baixo custo, embora sujeita a respostas superficiais.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "verificabilidade e precisão". De acordo com a teoria estudada em *1.1 Ciclo de Vida da Engenharia de Requisitos*, especificação: Documentação formal dos requisitos levantados por meio de documentos formais (Documento de Requisitos de Software - DRS), Casos de Uso ou Histórias de Usuário.
>
> **Gabarito: B**

---

### Teste 013
**(FGV – TJ-RR – Analista Judiciario Infraestrutura de Tecnologia da Informacao – 2024)**
De acordo com a norma ISO/IEC 27001, a organização precisa definir a aplicabilidade e os limites do sistema de gestão da segurança da informação para estabelecer o seu escopo. Nesse contexto, no que se refere ao que a organização deve considerar para a determinação do escopo descrito acima avalie as afirmativas a seguir e marque (V) para a verdadeira e (F) para a falsa. ( ) Questões internas e externas importantes para o seu propósito e que afetam sua capacidade para atingir os resultados desejados do seu sistema de gestão da segurança da informação. ( ) Requisitos das partes interessadas relevantes para a segurança da informação, os quais podem incluir requisitos legais e regulamentares, bem como obrigações contratuais. ( ) Interfaces e dependências entre as atividades desempenhadas pela organização e aquelas que são executadas por outras instituições. As afirmativas são, respectivamente,

* **A)** V – V – F.
* **B)** F – F – V.
* **C)** V – V – V.
* **D)** F – V – V.
* **E)** V – F – F.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "V – V – F". De acordo com a teoria estudada em *1.3 Requisitos Funcionais vs. Requisitos Não Funcionais (Taxonomia de Sommerville)*, especificam o que o sistema deve fazer em resposta a determinadas entradas, como reagir a situações específicas e quais cálculos realizar (ex.: *"O sistema deve calcular a alíquota previdenciária com base na remuneração bruta"*).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "F – F – V". De acordo com a teoria estudada em *1.1 Ciclo de Vida da Engenharia de Requisitos*, elicitação (Levantamento): Identificação e descoberta dos requisitos junto aos clientes, usuários e demais partes interessadas (*stakeholders*).
> - **C)** **Correta.** Conforme fundamentado na seção *2.1 Modelagem de Casos de Uso: Elementos e Relacionamentos («include» vs. «extend»)* deste guia, atores: Papéis desempenhados por entidades externas em relação ao sistema. Podem ser *Atores Primários* (iniciam o caso de uso para atingir um objetivo) ou *Atores Secundários* (fornecem serviços de apoio ao sistema, como um serviço externo de pagamento). Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ-RR/2024) ao estabelecer que "V – V – V".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "F – V – V". De acordo com a teoria estudada em *1.1 Ciclo de Vida da Engenharia de Requisitos*, concepção / Estudo de Viabilidade: Avalia se o sistema contribui para os objetivos da organização e se é técnica e economicamente viável.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "V – F – F". De acordo com a teoria estudada em *1.3 Requisitos Funcionais vs. Requisitos Não Funcionais (Taxonomia de Sommerville)*, *Requisitos Externos:* Derivam de fatores externos ao sistema e à organização (ex.: aderência à Lei Geral de Proteção de Dados - LGPD, normas de interoperabilidade e regulamentações do Banco Central).
>
> **Gabarito: C**

---

## 2. Modelagem por Casos de Uso e Histórias de Usuário

### 2.1 Modelagem de Casos de Uso: Elementos e Relacionamentos («include» vs. «extend»)
Um Caso de Uso descreve uma sequência de interações entre um ator externo (humano ou outro sistema) e o software para atingir um objetivo específico que entregue valor mensurável:

- **Atores:** Papéis desempenhados por entidades externas em relação ao sistema. Podem ser *Atores Primários* (iniciam o caso de uso para atingir um objetivo) ou *Atores Secundários* (fornecem serviços de apoio ao sistema, como um serviço externo de pagamento);
- **Cenários:** Compõe-se de um *Cenário Principal* (fluxo básico ou "caminho feliz" onde tudo ocorre com sucesso) e *Cenários Alternativos/Exceção* (desvios de rota, validações de erro ou falhas).

**Relacionamentos no Diagrama de Casos de Uso (Cobrança Clássica da FCC):**

1. **Associação:** Linha contínua que conecta um ator a um caso de uso, denotando comunicação direta.
2. **Estereótipo `«include»` (Inclusão Obrigatória):**
    - O caso de uso base **depende obrigatoriamente** do caso de uso incluído para completar sua execução com sucesso;
    - Evita duplicação de comportamentos comuns compartilhados por múltiplos casos de uso (ex.: *Emitir Relatório* inclui compulsoriamente *Autenticar Usuário*);
    - **Direção da Seta:** Seta tracejada apontando **do Caso Base para o Caso Incluído** ($\text{Base} \xrightarrow{\ll\text{include}\gg} \text{Incluído}$).

3. **Estereótipo `«extend»` (Extensão Condicional / Opcional):**
    - Modela comportamento acessório, opcional ou excepcional que somente é acionado se determinada condição pré-definida for satisfeita em um **ponto de extensão (*extension point*)**;
    - O caso base executa e conclui com sucesso mesmo se a extensão jamais ocorrer (ex.: *Emitir Notificação Especial* estende o caso base *Processar Pedido* quando o valor for superior a cem mil reais);
    - **Direção da Seta:** Seta tracejada apontando **do Caso Extensor para o Caso Base** ($\text{Extensão} \xrightarrow{\ll\text{extend}\gg} \text{Base}$).

4. **Generalização / Especialização:** Relação de herança representada por uma seta com triângulo vazado na ponta. Pode ocorrer entre casos de uso ou entre atores (ex.: *Auditor de TI* especializa *Auditor Geral*).

> 🚨 **ALERTA DE PROVA / PEGADINHA FCC:**  
> A banca FCC frequentemente inverte a direção das setas e os conceitos:
>
> - No `<<include>>`: A seta aponta do caso base para o incluído ($\text{Base} \rightarrow \text{Incluído}$) e a execução é **obrigatória/incondicional**.
> - No `<<extend>>`: A seta aponta do caso que estende para o caso base ($\text{Extensor} \rightarrow \text{Base}$) e a execução é **opcional/condicional** vinculada a um ponto de extensão.

### 2.2 Histórias de Usuário (User Stories) e os 3 Cs de Ron Jeffries
Em ambientes ágeis, as necessidades de software são expressas através de **Histórias de Usuário**:
$$\text{"Como [papel de usuário], eu quero [funcionalidade/ação], para que [benefício de negócio percebido]"}$$

- **Os 3 Cs de Ron Jeffries:**
    1. **Card (Cartão):** A história é escrita de forma sucinta em um cartão físico ou digital, servindo como lembrete visual de uma funcionalidade a ser construída;
    2. **Conversation (Conversa):** O detalhamento do requisito não é fixado em documentos estáticos, mas refinado por meio de diálogo contínuo entre desenvolvedores, Product Owner e usuários;
    3. **Confirmation (Confirmação):** Critérios de aceite formais e testes que estabelecem a validação inequívoca de que a história foi concluída com sucesso.

### 2.3 Critérios de Aceite e o Padrão INVEST
- **Critérios de Aceite (Formato BDD / Gherkin):** Estruturam-se tipicamente no padrão:  
  *Dado que [contexto inicial], Quando [evento ou ação executada], Então [resultado esperado observável].*
- **Critérios INVEST de Qualidade de Histórias (Bill Wake e Mike Cohn):**

| Letra | Critério INVEST | Significado Técnico na Prática Ágil |
| :---: | :--- | :--- |
| **I** | **Independent** (Independente) | As histórias devem ser desacopladas entre si, permitindo que sejam priorizadas, desenvolvidas e implantadas em qualquer ordem. |
| **N** | **Negotiable** (Negociável) | A história não é um contrato pétreo. Seu escopo de detalhe deve permanecer aberto para negociações e ajustes durante a Sprint. |
| **V** | **Valuable** (Valiosa) | Deve entregar valor tangível e perceptível para o cliente ou usuário final (evitam-se histórias puramente técnicas desvinculadas de valor). |
| **E** | **Estimable** (Estimável) | A equipe deve compreender a complexidade técnica para estimar seu esforço de desenvolvimento em *Story Points* ou horas. |
| **S** | **Small** (Pequena) | A história deve ser dimensionada adequadamente para ser concluída com folga dentro de uma única iteração/sprint. |
| **T** | **Testable** (Testável) | A história deve possuir critérios de aceite objetivos e claros que permitam a validação automatizada ou manual de aprovação. |

---

### Teste 014
**(FCC – TRT-1 – Analista Judiciario Tecnologia da Informacao – 2014)**
Diagramas de casos de uso constituem-se em um tipo de diagrama definido na UML. Segundo a UML 2.4.1, em um diagrama de casos de uso,

* **A)** um ator pode ser representado apenas pelo símbolo do “stick man”.
* **B)** só pode haver representado um único ator.
* **C)** o número de atores e de casos de uso sempre deve ser o mesmo.
* **D)** só pode haver representado um único caso de uso.
* **E)** um ator pode ser representado pelo “stick man” ou por um retângulo com a expressão <`<actor>`>.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "um ator pode ser representado apenas pelo símbolo do “stick man”". De acordo com a teoria estudada em *2.1 Modelagem de Casos de Uso: Elementos e Relacionamentos («include» vs. «extend»)*, associação: Linha contínua que conecta um ator a um caso de uso, denotando comunicação direta.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "só pode haver representado um único ator". De acordo com a teoria estudada em *2.1 Modelagem de Casos de Uso: Elementos e Relacionamentos («include» vs. «extend»)*, generalização / Especialização: Relação de herança representada por uma seta com triângulo vazado na ponta. Pode ocorrer entre casos de uso ou entre atores (ex.: *Auditor de TI* especializa *Auditor Geral*).
> - **C)** **Incorreta.** A opção promove generalização excessiva que desconsidera as condições técnicas e normativas ao afirmar que "o número de atores e de casos de uso sempre deve ser o mesmo". De acordo com a teoria estudada em *2.1 Modelagem de Casos de Uso: Elementos e Relacionamentos («include» vs. «extend»)*, atores: Papéis desempenhados por entidades externas em relação ao sistema. Podem ser *Atores Primários* (iniciam o caso de uso para atingir um objetivo) ou *Atores Secundários* (fornecem serviços de apoio ao sistema, como um serviço externo de pagamento).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "só pode haver representado um único caso de uso". De acordo com a teoria estudada em *2.1 Modelagem de Casos de Uso: Elementos e Relacionamentos («include» vs. «extend»)*, o caso de uso base depende obrigatoriamente do caso de uso incluído para completar sua execução com sucesso.
> - **E)** **Correta.** Conforme fundamentado na seção *2.1 Modelagem de Casos de Uso: Elementos e Relacionamentos («include» vs. «extend»)* deste guia, um Caso de Uso descreve uma sequência de interações entre um ator externo (humano ou outro sistema) e o software para atingir um objetivo específico que entregue valor mensurável. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT-1/2014) ao estabelecer que "um ator pode ser representado pelo “stick man” ou por um retângulo com a expressão <`<actor>`>".
>
> **Gabarito: E**

---

### Teste 015
**(FGV – TJ-RR – Analista Judiciario Gestao e Governanca de Tecnologia da Informacao – 2024)**
Um bom diagrama pode ajudar a comunicar ideias sobre um sistema, principalmente quando deseja-se evitar muitos detalhes. Na UML, uma ferramenta recomendada para esse fim é o Caso de Uso. Acerca dos diagramas de casos de uso, avalie as afirmativas a seguir e assinale (V) para a verdadeira e (F) para a falsa. ( ) Casos de uso são uma técnica para capturar os requisitos não funcionais de um software. ( ) Casos de uso representam uma visão externa do sistema, logo não deve haver correlação com as classes internas do sistema. ( ) Raias, atores e transições são elementos comuns em casos de uso. As afirmativas são, respectivamente,

* **A)** F – V – F.
* **B)** V – V – F.
* **C)** F – V – V.
* **D)** F – F – V.
* **E)** V – F – F.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *2.1 Modelagem de Casos de Uso: Elementos e Relacionamentos («include» vs. «extend»)* deste guia, atores: Papéis desempenhados por entidades externas em relação ao sistema. Podem ser *Atores Primários* (iniciam o caso de uso para atingir um objetivo) ou *Atores Secundários* (fornecem serviços de apoio ao sistema, como um serviço externo de pagamento). Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ-RR/2024) ao estabelecer que "F – V – F".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "V – V – F". De acordo com a teoria estudada em *2.1 Modelagem de Casos de Uso: Elementos e Relacionamentos («include» vs. «extend»)*, um Caso de Uso descreve uma sequência de interações entre um ator externo (humano ou outro sistema) e o software para atingir um objetivo específico que entregue valor mensurável.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "F – V – V". De acordo com a teoria estudada em *2.1 Modelagem de Casos de Uso: Elementos e Relacionamentos («include» vs. «extend»)*, generalização / Especialização: Relação de herança representada por uma seta com triângulo vazado na ponta. Pode ocorrer entre casos de uso ou entre atores (ex.: *Auditor de TI* especializa *Auditor Geral*).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "F – F – V". De acordo com a teoria estudada em *3.1 Taxonomia dos Diagramas UML: Estruturais vs. Comportamentais*, diagrama de Casos de Uso (interações de atores com funcionalidades).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "V – F – F". De acordo com a teoria estudada em *1.4 Gerenciamento, Rastreabilidade e Mudança de Requisitos*, matriz de Rastreabilidade: Tabela que mapeia a correlação bidirecional entre requisitos de usuário, requisitos de sistema, diagramas de arquitetura e casos de testes unitários.
>
> **Gabarito: A**

---

### Teste 016
**(FCC – TRT-2 – Analista Judiciario Tecnologia da Informacao – 2014)**
No Gerenciamento de Liberação e Implantação da ITIL v3, é proposto o Modelo V de Serviço para o planejamento da construção e teste dos serviços. Critério de Revisão de Serviço I Critério de Aceite II Critério Operacional III Critério de Teste de Liberação Desenhar Liberação do Serviço Desenvolver Liberação do Serviço Construir e Testar Serviço Validar Serviços, Pacotes, Ofertas e Contratos Teste de Aceite de Serviço Teste de Aceite Operacional Teste de Pacote de Liberação Teste de Componente No Modelo V, acima, as lacunas I, II e III são preenchidas, correta e respectivamente, com:

* **A)** Definir Escopo da Liberação, Planejar Liberação, Definir Requisitos da Liberação.
* **B)** Definir Escopo da Liberação, Definir Requisitos da Liberação, Definir Requisitos do Serviço.
* **C)** Definir Requisitos da Liberação, Definir Requisitos do Negócio, Definir Requisitos do Serviço.
* **D)** Definir Requisitos do Negócio, Definir Requisitos do Serviço, Definir Solução do Serviço.
* **E)** Definir Requisitos do Negócio, Definir Requisitos do Sistema, Definir Requisitos do Serviço.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Definir Escopo da Liberação, Planejar Liberação, Definir Requisitos da Liberação". De acordo com a teoria estudada em *2.3 Critérios de Aceite e o Padrão INVEST*, n: Negotiable (Negociável) — A história não é um contrato pétreo. Seu escopo de detalhe deve permanecer aberto para negociações e ajustes durante a Sprint.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Definir Escopo da Liberação, Definir Requisitos da Liberação, Definir Requisitos do Serviço". De acordo com a teoria estudada em *1.4 Gerenciamento, Rastreabilidade e Mudança de Requisitos*, *Rastreabilidade para trás (Backward traceability):* Liga o requisito à sua fonte originária (norma legal, entrevista ou necessidade de negócio).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Definir Requisitos da Liberação, Definir Requisitos do Negócio, Definir Requisitos do Serviço". De acordo com a teoria estudada em *4.1 Elementos de Fluxo: Eventos, Atividades e Tipos de Tarefas*, *Tarefas (Atômicas):* Tarefa de Usuário (*User Task* - mão humana), Tarefa de Serviço (*Service Task* - engrenagem, executada por software automatizado), Tarefa Manual (*Manual Task*) e Tarefa de Script (*Script Task*).
> - **D)** **Correta.** Conforme fundamentado na seção *2.1 Modelagem de Casos de Uso: Elementos e Relacionamentos («include» vs. «extend»)* deste guia, atores: Papéis desempenhados por entidades externas em relação ao sistema. Podem ser *Atores Primários* (iniciam o caso de uso para atingir um objetivo) ou *Atores Secundários* (fornecem serviços de apoio ao sistema, como um serviço externo de pagamento). Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT-2/2014) ao estabelecer que "Definir Requisitos do Negócio, Definir Requisitos do Serviço, Definir Solução do Serviço".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Definir Requisitos do Negócio, Definir Requisitos do Sistema, Definir Requisitos do Serviço". De acordo com a teoria estudada em *1.2 Técnicas de Elicitação de Requisitos*, prototipação Rápida: Construção de maquetes visuais ou versões interativas preliminares do sistema para permitir a validação antecipada de fluxos de navegação e layouts.
>
> **Gabarito: D**

---

## 3. Modelagem de Sistemas com UML (versão 2.5)

### 3.1 Taxonomia dos Diagramas UML: Estruturais vs. Comportamentais
A UML 2.5 divide seus diagramas em duas categorias fundamentais cobradas rigorosamente pela FCC:

1. **Diagramas Estruturais (Aspectos Estáticos do Sistema):**
    - **Diagrama de Classes** (estruturas de classes, atributos, operações e relações);
    - **Diagrama de Objetos** (instâncias de classes em um dado momento temporal);
    - **Diagrama de Componentes** (módulos executáveis e interfaces de software);
    - **Diagrama de Implantação (*Deployment*)** (arquitetura de hardware, nós de rede e distribuição de artefatos);
    - **Diagrama de Pacotes** (organização lógica de subsistemas);
    - **Diagrama de Estrutura Composta** e **Diagrama de Perfis**.

2. **Diagramas Comportamentais (Aspectos Dinâmicos e Fluxos de Controle):**
    - **Diagrama de Casos de Uso** (interações de atores com funcionalidades);
    - **Diagrama de Atividades** (fluxos de trabalho procedimentais e concorrência);
    - **Diagrama de Máquina de Estados** (estados e transições de ciclo de vida de objetos);
    - **Diagramas de Interação:**
        - **Diagrama de Sequência** (mensagens ordenadas cronologicamente ao longo do tempo);
        - **Diagrama de Comunicação** (interações enfatizando a estrutura dos objetos);
        - **Diagrama de Visão Geral de Interação** e **Diagrama de Tempo (*Timing*)**.

### 3.2 Diagrama de Classes: Visibilidade, Multiplicidade, Agregação e Composição
O Diagrama de Classes é o pilar estrutural da modelagem orientada a objetos:

```mermaid
classDiagram
    direction LR
    class ProcessoTCE {
        -String numeroAutos
        #Date dataAbertura
        +iniciarInstrucao() void
    }
    class ItemProcesso {
        -String descricaoFato
        +validarItem() Boolean
    }
    class ServidorRelator {
        +String matricula
        +emitirVoto() void
    }
    ProcessoTCE "1" *-- "1..*" ItemProcesso : Composição (Todo-Parte Forte)
    ProcessoTCE "0..*" o-- "1" ServidorRelator : Agregação (Todo-Parte Fraca)
```

- **Notação de Visibilidade dos Membros:**
    - `+` **Público (Public):** Acessível por qualquer classe do sistema;
    - `-` **Privado (Private):** Acessível estritamente dentro da própria classe definidora;
    - `#` **Protegido (Protected):** Acessível pela classe definidora e suas subclasses herdadas;
    - `~` **Pacote (Package):** Acessível por qualquer classe que pertença ao mesmo pacote.
- **Diferença Crucial: Agregação vs. Composição (Questão Garantida):**
    - **Agregação (Todo-Parte Fraca - Losango Branco/Vazio):** A existência da parte é independente do todo. O objeto todo agrega referências a objetos que podem existir isoladamente e pertencer a outros agregados (ex.: *Universidade e Professores*).
    - **Composição (Todo-Parte Forte - Losango Preto/Preenchido):** A existência da parte depende compulsoriamente do todo. A parte tem ciclo de vida estritamente atrelado ao todo: se o todo for destruído, todas as suas partes constitutivas são destruídas em cascata (ex.: *Processo e Peças dos Autos*; *Nota Fiscal e Itens da Nota*). A multiplicidade do lado do todo na composição é no máximo 1.

### 3.3 Diagramas de Sequência, Atividades e Máquina de Estados
- **Diagrama de Sequência:** Representa como os objetos colaboram em uma sequência temporal ordenada. Elementos chave:
    - *Linhas de Vida (*Lifelines*):* Linha vertical tracejada que representa a existência do objeto no tempo;
    - *Focos de Controle (*Activation bars*):* Retângulos estreitos que demonstram quando o objeto está executando operações ativas;
    - *Mensagens:* Síncronas (seta com ponta preenchida), Assíncronas (seta com ponta aberta), Retorno (linha tracejada com seta aberta);
    - *Fragmentos Combinados:* Blocos com operadores como `alt` (ramificações alternativas / *if-else*), `opt` (comportamento opcional / *if*) e `loop` (iterações / *for-while*).
- **Diagrama de Atividades:** Modela fluxos de controle e de dados entre atividades procedimentais:
    - Nós de bifurcação e junção (*Fork* e *Join*): barra preta horizontal ou vertical que modela **fluxos concorrentes/paralelos**;
    - Raias (*Swimlanes*): subdivisões verticais ou horizontais que delimitam os papéis organizacionais ou classes responsáveis pela execução de cada ação.
- **Diagrama de Máquina de Estados:** Modela os diferentes estados pelos quais um objeto singular transita durante sua vida útil em resposta a eventos (gatilhos), protegidos por guardas booleanas e disparando ações.

---

### Teste 017
**(FGV – TJ-AP – Analista Judiciario Apoio Especializado Tecnologia da Informacao Desenvolvimento de Sistemas – 2023)**
A análise orientada a objetos utiliza diagramas da UML para representar os diversos elementos de um projeto de software. Ana está modelando um sistema para Web, na arquitetura MVC, e agora precisa descrever o fluxo de mensagens entre os componentes View, Controller e DAO, segundo a cronologia com a qual ocorrem, para um processo de consulta aos dados na base e apresentação na interface de usuário. Para que possa desenhar corretamente o processo, Ana irá utilizar o diagrama de:

* **A)** classes;
* **B)** componentes;
* **C)** estados;
* **D)** implantação;
* **E)** sequência.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "classes". De acordo com a teoria estudada em *3.2 Diagrama de Classes: Visibilidade, Multiplicidade, Agregação e Composição*, o Diagrama de Classes é o pilar estrutural da modelagem orientada a objetos.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "componentes". De acordo com a teoria estudada em *3.1 Taxonomia dos Diagramas UML: Estruturais vs. Comportamentais*, diagrama de Componentes (módulos executáveis e interfaces de software).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "estados". De acordo com a teoria estudada em *3.3 Diagramas de Sequência, Atividades e Máquina de Estados*, diagrama de Sequência: Representa como os objetos colaboram em uma sequência temporal ordenada. Elementos chave.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "implantação". De acordo com a teoria estudada em *3.1 Taxonomia dos Diagramas UML: Estruturais vs. Comportamentais*, diagrama de Implantação (*Deployment*) (arquitetura de hardware, nós de rede e distribuição de artefatos).
> - **E)** **Correta.** Conforme fundamentado na seção *3.1 Taxonomia dos Diagramas UML: Estruturais vs. Comportamentais* deste guia, diagrama de Sequência (mensagens ordenadas cronologicamente ao longo do tempo). Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ-AP/2023) ao estabelecer que "sequência".
>
> **Gabarito: E**

---

### Teste 018
**(FCC – TRT-23 – Analista Judiciario Apoio Especializado Tecnologia da Informacao – 2016)**
Um Analista pretende desenvolver um projeto utilizando UML 2.0 e, em seus propósitos, verificou a possibilidade de uso de alguns diagramas. Um deles é o Diagrama de Sequência que representa a indicação do conjunto de objetos envolvidos em um cenário e a especificação das mensagens trocadas entre estes ao longo de linhas do tempo que são linhas tracejadas, traçadas verticalmente da base dos objetos até a parte inferior do diagrama. Retângulos colocados sobre as linhas de tempo indicam

* **A)** o tempo decorrido entre as iterações de um processo recursivo.
* **B)** as interações entre as atividades, no tempo.
* **C)** os casos de uso de cada objeto.
* **D)** os períodos de ativação do objeto.
* **E)** as etapas em que o objeto estará inativo.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "o tempo decorrido entre as iterações de um processo recursivo". De acordo com a teoria estudada em *3.1 Taxonomia dos Diagramas UML: Estruturais vs. Comportamentais*, diagrama de Sequência (mensagens ordenadas cronologicamente ao longo do tempo).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "as interações entre as atividades, no tempo". De acordo com a teoria estudada em *3.3 Diagramas de Sequência, Atividades e Máquina de Estados*, *Focos de Controle (*Activation bars*):* Retângulos estreitos que demonstram quando o objeto está executando operações ativas.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "os casos de uso de cada objeto". De acordo com a teoria estudada em *3.2 Diagrama de Classes: Visibilidade, Multiplicidade, Agregação e Composição*, agregação (Todo-Parte Fraca - Losango Branco/Vazio): A existência da parte é independente do todo. O objeto todo agrega referências a objetos que podem existir isoladamente e pertencer a outros agregados (ex.: *Universidade e Professores*).
> - **D)** **Correta.** Conforme fundamentado na seção *3.3 Diagramas de Sequência, Atividades e Máquina de Estados* deste guia, *Linhas de Vida (*Lifelines*):* Linha vertical tracejada que representa a existência do objeto no tempo. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT-23/2016) ao estabelecer que "os períodos de ativação do objeto".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "as etapas em que o objeto estará inativo". De acordo com a teoria estudada em *3.3 Diagramas de Sequência, Atividades e Máquina de Estados*, diagrama de Máquina de Estados: Modela os diferentes estados pelos quais um objeto singular transita durante sua vida útil em resposta a eventos (gatilhos), protegidos por guardas booleanas e disparando ações.
>
> **Gabarito: D**

---

### Teste 019
**(FCC – TRT-13 – Analista Judiciario Tecnologia da Informacao – 2014)**
Este diagrama da UML pode ser usado para modelar processos de negócio. Suporta comportamento paralelo e permite que, quem está seguindo o processo, escolha a ordem na qual fazer as coisas. Em outras palavras, ele simplesmente determina as regras essenciais de sequência que se deve seguir. São geralmente usados para mostrar o que acontece, mas não quem faz o que, já que faz sentido se concentrar no que é feito, em vez de em quem realiza quais partes do comportamento. O diagrama descrito é o diagrama de

* **A)** sequência.
* **B)** atividades.
* **C)** casos de uso.
* **D)** comunicação.
* **E)** distribuição.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "sequência". De acordo com a teoria estudada em *3.3 Diagramas de Sequência, Atividades e Máquina de Estados*, *Fragmentos Combinados:* Blocos com operadores como `alt` (ramificações alternativas / *if-else*), `opt` (comportamento opcional / *if*) e `loop` (iterações / *for-while*).
> - **B)** **Correta.** Conforme fundamentado na seção *3.3 Diagramas de Sequência, Atividades e Máquina de Estados* deste guia, diagrama de Máquina de Estados: Modela os diferentes estados pelos quais um objeto singular transita durante sua vida útil em resposta a eventos (gatilhos), protegidos por guardas booleanas e disparando ações. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT-13/2014) ao estabelecer que "atividades".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "casos de uso". De acordo com a teoria estudada em *3.1 Taxonomia dos Diagramas UML: Estruturais vs. Comportamentais*, diagrama de Casos de Uso (interações de atores com funcionalidades).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "comunicação". De acordo com a teoria estudada em *4.3 Estruturas de Separação (Pools e Lanes) e Conectores de Sequência vs. Mensagem*, fluxo de Mensagem (*Message Flow*): Representado por linha tracejada com um círculo vazado na origem e uma seta aberta no destino. Utilizado estritamente para modelar comunicação e troca de mensagens entre duas Pools distintas.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "distribuição". De acordo com a teoria estudada em *3.1 Taxonomia dos Diagramas UML: Estruturais vs. Comportamentais*, diagrama de Implantação (*Deployment*) (arquitetura de hardware, nós de rede e distribuição de artefatos).
>
> **Gabarito: B**

---

## 4. Modelagem de Processos de Negócio com BPMN 2.0

### 4.1 Elementos de Fluxo: Eventos, Atividades e Tipos de Tarefas
A notação **BPMN 2.0** (*Business Process Model and Notation*), mantida pelo consórcio OMG, é o padrão global para desenho de processos de negócio:

1. **Eventos (Círculos):** Representam algo que acontece no processo:
    - *Início (Start Event):* Linha de borda fina simples;
    - *Intermediário (Intermediate Event):* Linha de borda dupla;
    - *Fim (End Event):* Linha de borda grossa e preenchida.
    - *Gatilhos de Eventos:* Mensagem (ícone de envelope), Temporizador (ícone de relógio), Erro (ícone de raio) ou Condicional (ícone de documento).

2. **Atividades (Retângulos com Cantos Arredondados):** Trabalho realizado dentro do processo:
    - *Tarefas (Atômicas):* Tarefa de Usuário (*User Task* - mão humana), Tarefa de Serviço (*Service Task* - engrenagem, executada por software automatizado), Tarefa Manual (*Manual Task*) e Tarefa de Script (*Script Task*);
    - *Subprocessos:* Atividades compostas que podem ser visualizadas de forma colapsada (com marcador de cruz "+") ou expandida.

### 4.2 Gateways Decisórios no BPMN 2.0 (XOR, AND, OR e Event-based)
Os Gateways são representados por **Losangos** e controlam a convergência e divergência dos fluxos:

```mermaid
flowchart TD
    GW{"GATEWAYS NO BPMN 2.0"}
    
    GW --> XOR["Exclusivo (XOR - Marcador 'X' ou Vazio)<br/>• Desvia para EXATAMENTE UM caminho alternativo com base em dados"]
    GW --> AND["Paralelo (AND - Marcador '+')<br/>• Divide em TODOS os ramos concorrentes simultâneos (sem testar condições)<br/>• Na junção, AGUARDA a chegada de todos os fluxos para prosseguir"]
    GW --> OR["Inclusivo (OR - Marcador 'O')<br/>• Ativa UM OU MAIS caminhos que satisfaçam as condições booleanas"]
    GW --> EVENT["Baseado em Eventos (Marcador Pentágono)<br/>• A decisão aguarda a ocorrência do PRIMEIRO evento (mensagem ou timer)"]
```

- **Gateway Exclusivo (XOR - "X"):** Seleciona exclusivamente uma única rota entre as disponíveis;
- **Gateway Paralelo (AND - "+"):** Executa todos os caminhos de saída concorrentemente e sincroniza todos os caminhos na junção;
- **Gateway Inclusivo (OR - "O"):** Ativa múltiplos ramos condicionalmente e sincroniza apenas os ramos ativados;
- **Gateway Baseado em Eventos (Pentágono):** O desvio de fluxo depende de qual evento externo intermediário (recebimento de mensagem ou expiração de temporizador) ocorrer primeiro no tempo.

### 4.3 Estruturas de Separação (Pools e Lanes) e Conectores de Sequência vs. Mensagem
- **Piscina (*Pool*):** Representa um participante independente do processo (um ente externo, fornecedor, organização ou empresa). Cada processo de negócio autocontido executa dentro de uma Pool;
- **Raia (*Lane*):** Subdivisão interna de uma Pool, utilizada para alocar tarefas e agrupar responsabilidades por departamentos, funções, setores ou sistemas daquela mesma organização.

**Regras Fundamentais dos Conectores de Fluxo (Muito Cobrado em Prova):**

- **Fluxo de Sequência (*Sequence Flow*):** Representado por **linha sólida contínua com seta preenchida**. Conecta a sequência de atividades dentro da mesma Pool.  
  > 🚨 **REGRA DE OURO DO BPMN:** Um Fluxo de Sequência **NUNCA PODE CRUZAR A BORDA DE UMA POOL PARA OUTRA POOL!** Ele só pode cruzar linhas de Lanes dentro da mesma Pool!
- **Fluxo de Mensagem (*Message Flow*):** Representado por **linha tracejada com um círculo vazado na origem e uma seta aberta no destino**. Utilizado estritamente para modelar comunicação e troca de mensagens **entre duas Pools distintas**.
- **Associação:** Linha pontilhada simples, utilizada para associar dados, artefatos ou anotações de texto a objetos de fluxo.

---

### Teste 020
**(FCC – TRT-3 – Analista Judiciario Tecnologia da Informacao – 2015)**
O analista de TI Matheus, do TRT da 3a Região, durante o desenho de um processo utilizando a BPMN, deparou-se com a seguinte situação: em um ponto do processo em que a decisão seria tomada com base em um evento existiam dois possíveis eventos: (I) que o cliente entregasse os documentos no prazo estabelecido ou (II) que não os entregasse e o prazo de 5 dias expiraria. O primeiro evento que ocorresse determinaria o caminho do fluxo. No seu desenho ele utilizou, corretamente, o objeto BPMN Gataway

* **A)** Exclusivo baseado em Eventos.
* **B)** Paralelo.
* **C)** Exclusivo baseado em Dados.
* **D)** Inclusivo com Eventos.
* **E)** Exclusivo Paralelo.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *4.2 Gateways Decisórios no BPMN 2.0 (XOR, AND, OR e Event-based)* deste guia, gateway Baseado em Eventos (Pentágono): O desvio de fluxo depende de qual evento externo intermediário (recebimento de mensagem ou expiração de temporizador) ocorrer primeiro no tempo. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT-3/2015) ao estabelecer que "Exclusivo baseado em Eventos".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Paralelo". De acordo com a teoria estudada em *4.1 Elementos de Fluxo: Eventos, Atividades e Tipos de Tarefas*, a notação BPMN 2.0 (*Business Process Model and Notation*), mantida pelo consórcio OMG, é o padrão global para desenho de processos de negócio.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Exclusivo baseado em Dados". De acordo com a teoria estudada em *4.2 Gateways Decisórios no BPMN 2.0 (XOR, AND, OR e Event-based)*, gateway Exclusivo (XOR - "X"): Seleciona exclusivamente uma única rota entre as disponíveis.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Inclusivo com Eventos". De acordo com a teoria estudada em *4.2 Gateways Decisórios no BPMN 2.0 (XOR, AND, OR e Event-based)*, gateway Inclusivo (OR - "O"): Ativa múltiplos ramos condicionalmente e sincroniza apenas os ramos ativados.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Exclusivo Paralelo". De acordo com a teoria estudada em *4.2 Gateways Decisórios no BPMN 2.0 (XOR, AND, OR e Event-based)*, gateway Paralelo (AND - "+"): Executa todos os caminhos de saída concorrentemente e sincroniza todos os caminhos na junção.
>
> **Gabarito: A**

---

### Teste 021
**(FGV – TJ-SC – Analista Administrativo – 2026)**
A modelagem de processos pode ser realizada por meio de diferentes formatos, cada qual mais adequado a uma finalidade específica. A escolha do formato depende da situação organizacional, do público-alvo e do grau de formalidade exigido. Considere as situações a seguir, vivenciadas por gestores em uma organização. I. "Tenho 15 minutos para explicar o processo a quem nunca o viu." II. "Preciso mapear gargalos com o time de operação." III. "Preciso compreender oportunidades de melhorias, realizar automação, implantar IA ou conduzir projeto de transformação digital ou organizacional." Os formatos de modelagem mais adequados a cada uma dessas situações são, respectivamente,

* **A)** BPMN simplificado, fluxograma tradicional e desenho lúdico.
* **B)** fluxograma tradicional, desenho lúdico e BPMN simplificado.
* **C)** desenho lúdico, BPMN simplificado e fluxograma tradicional.
* **D)** desenho lúdico, fluxograma tradicional e BPMN simplificado.
* **E)** BPMN simplificado, desenho lúdico e fluxograma tradicional.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "BPMN simplificado, fluxograma tradicional e desenho lúdico". De acordo com a teoria estudada em *4.2 Gateways Decisórios no BPMN 2.0 (XOR, AND, OR e Event-based)*, gateway Baseado em Eventos (Pentágono): O desvio de fluxo depende de qual evento externo intermediário (recebimento de mensagem ou expiração de temporizador) ocorrer primeiro no tempo.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "fluxograma tradicional, desenho lúdico e BPMN simplificado". De acordo com a teoria estudada em *4.2 Gateways Decisórios no BPMN 2.0 (XOR, AND, OR e Event-based)*, os Gateways são representados por Losangos e controlam a convergência e divergência dos fluxos.
> - **C)** **Correta.** Conforme fundamentado na seção *4.1 Elementos de Fluxo: Eventos, Atividades e Tipos de Tarefas* deste guia, a notação BPMN 2.0 (*Business Process Model and Notation*), mantida pelo consórcio OMG, é o padrão global para desenho de processos de negócio. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ-SC/2026) ao estabelecer que "desenho lúdico, BPMN simplificado e fluxograma tradicional".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "desenho lúdico, fluxograma tradicional e BPMN simplificado". De acordo com a teoria estudada em *4.2 Gateways Decisórios no BPMN 2.0 (XOR, AND, OR e Event-based)*, gateway Exclusivo (XOR - "X"): Seleciona exclusivamente uma única rota entre as disponíveis.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "BPMN simplificado, desenho lúdico e fluxograma tradicional". De acordo com a teoria estudada em *4.2 Gateways Decisórios no BPMN 2.0 (XOR, AND, OR e Event-based)*, gateway Paralelo (AND - "+"): Executa todos os caminhos de saída concorrentemente e sincroniza todos os caminhos na junção.
>
> **Gabarito: C**

---

### Teste 022
**(FGV – TCE-SC – Auditor Fiscal de Controle Externo Ciencias da Computacao Sistemas de Informacao – 2026)**
No mapeamento de um processo de auditoria externa, o Auditor desenha um fluxo onde, após a análise preliminar, duas atividades devem ocorrer simultaneamente, sendo elas: “Notificar o Gestor” e “Publicar Edital”. O elemento do padrão BPMN 2.0, que deve ser utilizado para dividir o fluxo em dois caminhos simultâneos que não dependem de condições lógicas para iniciar, é o

* **A)** Exclusive Gateway (X).
* **B)** Parallel Gateway (+).
* **C)** Inclusive Gateway (O).
* **D)** Event-based Gateway.
* **E)** Intermediate Timer Event.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Exclusive Gateway (X)". De acordo com a teoria estudada em *4.2 Gateways Decisórios no BPMN 2.0 (XOR, AND, OR e Event-based)*, gateway Paralelo (AND - "+"): Executa todos os caminhos de saída concorrentemente e sincroniza todos os caminhos na junção.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Parallel Gateway (+)". De acordo com a teoria estudada em *4.2 Gateways Decisórios no BPMN 2.0 (XOR, AND, OR e Event-based)*, gateway Exclusivo (XOR - "X"): Seleciona exclusivamente uma única rota entre as disponíveis.
> - **C)** **Correta.** Conforme fundamentado na seção *4.2 Gateways Decisórios no BPMN 2.0 (XOR, AND, OR e Event-based)* deste guia, gateway Baseado em Eventos (Pentágono): O desvio de fluxo depende de qual evento externo intermediário (recebimento de mensagem ou expiração de temporizador) ocorrer primeiro no tempo. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE-SC/2026) ao estabelecer que "Inclusive Gateway (O)".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Event-based Gateway". De acordo com a teoria estudada em *4.2 Gateways Decisórios no BPMN 2.0 (XOR, AND, OR e Event-based)*, gateway Inclusivo (OR - "O"): Ativa múltiplos ramos condicionalmente e sincroniza apenas os ramos ativados.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Intermediate Timer Event". De acordo com a teoria estudada em *4.1 Elementos de Fluxo: Eventos, Atividades e Tipos de Tarefas*, *Intermediário (Intermediate Event):* Linha de borda dupla.
>
> **Gabarito: C**

---

## 5. Fontes Oficiais e Referências Bibliográficas

* [OMG Unified Modeling Language (UML 2.5.1) — Especificação Oficial](https://www.omg.org/spec/UML/2.5.1/About-UML) - Especificação normativa da UML 2.5.1 mantida pelo Object Management Group (diagramas estruturais e comportamentais).
* [OMG Business Process Model and Notation (BPMN 2.0.2) — Especificação Oficial](https://www.omg.org/spec/BPMN/2.0.2/About-BPMN) - Especificação formal da notação BPMN 2.0 (eventos, atividades, gateways, pools, lanes e conectores).
* [User Stories and User Story Examples (Mike Cohn — Mountain Goat Software)](https://www.mountaingoatsoftware.com/agile/user-stories) - Guia de referência sobre escrita de Histórias de Usuário, padrão INVEST e os 3 Cs.
* [Bounded Context — Modelagem de Domínio e Requisitos (Martin Fowler)](https://martinfowler.com/bliki/BoundedContext.html) - Delimitação de contextos e linguagem ubíqua na análise e modelagem de sistemas.
* [Os 12 Princípios do Manifesto Ágil — Requisitos Evolutivos e Colaboração](https://agilemanifesto.org/iso/ptbr/principles.html) - Princípios ágeis aplicados ao gerenciamento adaptativo de requisitos e entregas de valor.
* SOMMERVILLE, Ian. **Engenharia de Software**. 10. ed. São Paulo: Pearson Education do Brasil, 2019. (Cap. 4 - Engenharia de Requisitos; Cap. 5 - Modelagem de Sistemas).
* PRESSMAN, Roger S.; MAXIM, Bruce R. **Engenharia de Software: Uma Abordagem Profissional**. 9. ed. Porto Alegre: AMGH, 2021. (Cap. 7 - Compreensão dos Requisitos; Cap. 8 - Modelagem de Requisitos).
* COHN, Mike. **User Stories Applied: For Agile Software Development**. Boston: Addison-Wesley Professional, 2004. (Cap. 2 - Writing Stories; Cap. 6 - Acceptance Testing).
