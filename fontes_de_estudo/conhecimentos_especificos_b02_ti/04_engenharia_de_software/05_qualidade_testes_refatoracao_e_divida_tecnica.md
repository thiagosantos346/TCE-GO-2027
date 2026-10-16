# 05 - Qualidade, Testes, Refatoração e Dívida Técnica

> **Matéria:** Engenharia de Software  
> **Cargo:** B02 – Técnico de Controle Externo – Especialidade: Tecnologia da Informação  
> **Arquivo:** `05_qualidade_testes_refatoracao_e_divida_tecnica.md`  

---

## 📌 Ementa / Itens do Edital
- Qualidade de software: desempenho, escalabilidade, disponibilidade, confiabilidade e manutenibilidade
- Testes de software: unitários, de integração, funcionais, de regressão, de carga e de estresse
- Testes automatizados
- Revisão de código (code review)
- Refatoração de código (refactoring)
- Dívida técnica (technical debt)

---

## 🧭 Sumário
- [1. Atributos e Métricas de Qualidade de Software (ISO/IEC 25010)](#1-atributos-e-metricas-de-qualidade-de-software-isoiec-25010)
    - [1.1 Desempenho e Eficiência de Recursos](#11-desempenho-e-eficiencia-de-recursos)
    - [1.2 Escalabilidade Vertical (Scale Up) vs. Escalabilidade Horizontal (Scale Out)](#12-escalabilidade-vertical-scale-up-vs-escalabilidade-horizontal-scale-out)
    - [1.3 Confiabilidade, Disponibilidade e Métricas de Manutenção (MTBF e MTTR)](#13-confiabilidade-disponibilidade-e-metricas-de-manutencao-mtbf-e-mttr)
    - [1.4 Manutenibilidade e Facilidade de Mudança](#14-manutenibilidade-e-facilidade-de-mudanca)
- [2. Níveis e Estratégias de Testes de Software](#2-niveis-e-estrategias-de-testes-de-software)
    - [2.1 A Pirâmide de Testes de Mike Cohn](#21-a-piramide-de-testes-de-mike-cohn)
    - [2.2 Dublês de Teste (Test Doubles de Gerard Meszaros)](#22-dubles-de-teste-test-doubles-de-gerard-meszaros)
    - [2.3 Testes de Caixa-Preta (Funcionais) vs. Testes de Caixa-Branca (Estruturais)](#23-testes-de-caixa-preta-funcionais-vs-testes-de-caixa-branca-estruturais)
    - [2.4 Complexidade Ciclomática de Thomas McCabe e Grafo de Fluxo](#24-complexidade-ciclomatica-de-thomas-mccabe-e-grafo-de-fluxo)
- [3. Tipos Especializados de Testes e Automação](#3-tipos-especializados-de-testes-e-automacao)
    - [3.1 Testes de Regressão e Automação Contínua](#31-testes-de-regressao-e-automacao-continua)
    - [3.2 Testes de Desempenho: Carga vs. Estresse vs. Pico vs. Resistência](#32-testes-de-desempenho-carga-vs-estresse-vs-pico-vs-resistencia)
    - [3.3 Práticas de TDD (Test-Driven Development) e BDD (Behavior-Driven Development)](#33-praticas-de-tdd-test-driven-development-e-bdd-behavior-driven-development)
- [4. Revisão de Código, Refatoração e Dívida Técnica](#4-revisao-de-codigo-refatoracao-e-divida-tecnica)
    - [4.1 Técnicas Modernas de Revisão de Código (Code Review)](#41-tecnicas-modernas-de-revisao-de-codigo-code-review)
    - [4.2 Refatoração de Código e os "Maus Cheiros" (Code Smells) de Fowler](#42-refatoracao-de-codigo-e-os-maus-cheiros-code-smells-de-fowler)
    - [4.3 Dívida Técnica e o Quadrante de Martin Fowler](#43-divida-tecnica-e-o-quadrante-de-martin-fowler)
- [5. Fontes Oficiais e Referências Bibliográficas](#5-fontes-oficiais-e-referencias-bibliograficas)
- [6. Questões de Concurso FCC Comentadas](#6-questoes-de-concurso-fcc-comentadas)

---

## 1. Atributos e Métricas de Qualidade de Software (ISO/IEC 25010)

A norma internacional **ISO/IEC 25010** (evolução da ISO 9126) define o modelo de qualidade de produto de software, estruturado em oito características fundamentais: adequação funcional, eficiência de desempenho, compatibilidade, usabilidade, confiabilidade, segurança, manutenibilidade e portabilidade.

### 1.1 Desempenho e Eficiência de Recursos
Mede o comportamento do sistema em termos de velocidade de resposta e utilização racional dos recursos computacionais sob condições especificadas:

- **Tempo de Resposta (*Response Time*):** Intervalo de tempo transcorrido entre a emissão de uma requisição pelo usuário e a exibição completa da resposta processada;
- **Latência:** Tempo de trânsito que uma mensagem ou pacote leva para viajar da origem ao destino na rede;
- **Vazão (*Throughput*):** Quantidade de transações, requisições ou volume de dados processados com sucesso por unidade de tempo (ex.: 5.000 requisições por segundo - RPS);
- **Utilização de Recursos:** Percentual de ocupação de CPU, consumo de memória RAM, largura de banda e operações de entrada/saída em disco (I/O).

---

### 1.2 Escalabilidade Vertical (Scale Up) vs. Escalabilidade Horizontal (Scale Out)
- **Escalabilidade Vertical (*Scale Up*):** Expansão da capacidade computacional através do acréscimo de recursos físicos à máquina servidora existente (mais núcleos de processador, mais memória RAM ou discos SSD mais rápidos).  
  *Limitações:* Possui teto físico máximo de hardware, custo exponencialmente elevado nas faixas superiores e exige paradas no sistema para upgrade;
- **Escalabilidade Horizontal (*Scale Out*):** Expansão da capacidade mediante a adição de novas instâncias e nós servidores operando em paralelo sob um balanceador de carga (*Load Balancer*).  
  *Vantagens:* Altamente flexível, alinhada a ambientes em nuvem e contêineres elásticos, permitindo provisionamento dinâmico sem interrupção de serviços.

---

### 1.3 Confiabilidade, Disponibilidade e Métricas de Manutenção (MTBF e MTTR)
- **Confiabilidade:** Grau em que o software desempenha suas funções requeridas sob condições estabelecidas por um período especificado de tempo. Avalia a maturidade, a tolerância a falhas e a capacidade de recuperação de desastres;
- **Disponibilidade:** Proporção de tempo em que o sistema está operacional e plenamente acessível para uso quando demandado. Expressa-se habitualmente pelo número de "noves" em acordos de nível de serviço (SLA - *Service Level Agreement*):
    - *99% ("dois noves"):* Tolera até 3,65 dias de indisponibilidade por ano;
    - *99,9% ("três noves"):* Tolera até 8,76 horas de indisponibilidade por ano;
    - *99,99% ("quatro noves"):* Tolera até 52,56 minutos de indisponibilidade por ano.
- **Métricas Clássicas de Sustentação de Sistemas:**
    - **MTBF (*Mean Time Between Failures* - Tempo Médio Entre Falhas):** Métrica de confiabilidade que calcula o tempo médio em que o sistema opera perfeitamente entre duas panes consecutivas;
    - **MTTR (*Mean Time to Repair* - Tempo Médio para Reparo):** Métrica de manutenibilidade que mede o tempo médio gasto pela equipe de suporte para diagnosticar, corrigir a falha e restaurar o sistema à plena operação;
    - **Cálculo da Disponibilidade Teórica:**
    $$\text{Disponibilidade} = \frac{\text{MTBF}}{\text{MTBF} + \text{MTTR}}$$

---

### 1.4 Manutenibilidade e Facilidade de Mudança
A manutenibilidade reflete a facilidade e a eficiência com que o software pode ser modificado pelos desenvolvedores para corrigir defeitos, melhorar o desempenho ou adaptar o sistema a mudanças no ambiente de negócio. Subdivide-se em:

- **Modularidade:** Grau em que o sistema é composto por componentes discretos, isolando o impacto de alterações;
- **Reusabilidade:** Capacidade de um ativo ser utilizado em mais de um sistema ou módulo;
- **Analisabilidade:** Facilidade com que se pode diagnosticar deficiências, causas raízes de falhas ou identificar partes a serem alteradas;
- **Modificabilidade:** Facilidade com que o software pode ser modificado sem introduzir novos defeitos ou degradar a qualidade existente;
- **Testabilidade:** Grau em que critérios e testes eficazes podem ser estabelecidos e executados para validar as alterações realizadas.

---

## 2. Níveis e Estratégias de Testes de Software

### 2.1 A Pirâmide de Testes de Mike Cohn
A Pirâmide de Testes é o modelo canônico de engenharia de software para construir suítes de testes automatizados equilibradas e sustentáveis:

```mermaid
flowchart TD
    E2E["Testes de Ponta a Ponta (E2E / Interface / UI)<br/>Topo: Menor quantidade • Lentos • Caros • Frágeis"]
    INT["Testes de Integração / Serviços<br/>Meio: Volume intermediário • Validação entre módulos, bancos e APIs"]
    UNI["Testes Unitários / Componentes<br/>Base: Maior volume • Milissegundos • Baixo custo • Alta precisão"]
    E2E --> INT --> UNI
```

| Nível de Teste | Velocidade de Execução | Custo de Construção/Manutenção | Foco do Diagnóstico de Falha | Escopo de Isolamento |
| :--- | :--- | :--- | :--- | :--- |
| **Unitário** | Milissegundos | Muito baixo | Linha exata do código / método | Total (isola com Stubs/Mocks) |
| **Integração** | Segundos | Moderado | Comunicação entre componentes | Parcial (integra com BD ou filas) |
| **Ponta a Ponta (E2E)** | Minutos / Horas | Extremamente alto | Fluxo completo do usuário | Nulo (sistema real completo) |

> 🚨 **ALERTA DE PROVA / PEGADINHA FCC:** A inversão da pirâmide (chamada de antipadrão "Casquinha de Sorvete" ou *Ice Cream Cone*) ocorre quando a organização possui poucos testes unitários e concentra quase todo o esforço em testes manuais ou E2E de interface. O resultado são suítes de testes lentas, que demoram horas para rodar no CI/CD e quebram frequentemente por pequenas alterações visuais (*testes frágeis / flaky tests*).

---

### 2.2 Dublês de Teste (*Test Doubles* de Gerard Meszaros)
Nos testes unitários, para isolar a unidade sob teste (*System Under Test - SUT*) de dependências pesadas, instáveis ou lentas (bancos de dados, serviços web externos, sistemas de arquivos), empregam-se **Dublês de Teste**:

```mermaid
graph TD
    TD["DUBLÊS DE TESTE (Test Doubles)"]
    
    TD --> Dummy["Dummy<br/>Objeto preenchedor que nunca é chamado; satisfaz parâmetros"]
    TD --> Stub["Stub<br/>Fornece respostas enlatadas e pré-fabricadas a chamadas"]
    TD --> Spy["Spy<br/>Stub que também registra métricas e parâmetros das chamadas recebidas"]
    TD --> Mock["Mock<br/>Programado com expectativas estritas de chamadas; falha o teste se não ocorrerem"]
    TD --> Fake["Fake<br/>Implementação funcional real simplificada (ex.: banco de dados em memória)"]
```

1. **Dummy:** Objeto passado apenas para preencher parâmetros de assinatura de métodos obrigatórios, nunca sendo invocado durante a execução do teste;
2. **Stub:** Objeto que fornece respostas prontas e pré-programadas para as chamadas recebidas durante o teste (ex.: método `consultarSaldo()` retorna sempre o valor fixo de `1000.00`);
3. **Spy (Espião):** Um Stub enriquecido que intercepta e grava o histórico das chamadas (armazena quantas vezes o método foi invocado e quais parâmetros foram passados para checagem posterior);
4. **Mock:** Objeto pré-programado com **expectativas formais de comportamento**. O desenvolvedor configura explicitamente quais métodos devem ser chamados, com quais argumentos específicos e em que ordem. Se o método não for invocado conforme a expectativa estabelecida, o teste falha compulsoriamente;
5. **Fake:** Objeto que possui uma implementação funcional real simplificada, mas utiliza atalhos que a tornam imprópria para produção (ex.: um banco de dados relacional em memória H2 substituindo um servidor Oracle corporativo nos testes).

---

### 2.3 Testes de Caixa-Preta (Funcionais) vs. Testes de Caixa-Branca (Estruturais)
- **Testes de Caixa-Preta (Funcionais):** Avaliam o comportamento do software sem conhecimento da estrutura interna ou do código-fonte. O foco reside nas entradas e saídas esperadas:
    - *Partição de Equivalência:* Divide os dados de entrada em classes válidas e inválidas, partindo do princípio de que qualquer dado dentro da mesma partição receberá o mesmo tratamento;
    - *Análise do Valor Limite (BVA):* Testa valores situados exatamente nas fronteiras e adjacências das partições (ex.: se o intervalo aceito é de 18 a 65 anos, testa-se 17, 18, 19, 64, 65 e 66 anos).
- **Testes de Caixa-Branca (Estruturais):** Avaliam os caminhos de controle, estruturas lógicas e condições internas do código-fonte:
    - *Critérios de Cobertura:* Cobertura de comandos (*Statement Coverage*), cobertura de decisões/desvios (*Branch Coverage*) e cobertura de caminhos independentes.

---

### 2.4 Complexidade Ciclomática de Thomas McCabe e Grafo de Fluxo
Proposta por Thomas McCabe em 1976, a **Complexidade Ciclomática ($V(G)$)** mede quantitativamente a complexidade lógica de um programa através da contagem do número de caminhos linearmente independentes no seu grafo de fluxo de controle.

**Fórmulas de Cálculo Clássicas:**

1. Pela contagem de arestas ($E$), nós ($N$) e componentes conexos ($P=1$ para método único):
   $$V(G) = E - N + 2$$
2. Pela contagem direta de pontos de decisão/predicados ($P$):
   $$V(G) = P + 1$$
   *(onde $P$ é o total de comandos condicionais e de laço: `if`, `while`, `for`, `case`)*.

> ⭐ **IMPORTANTE / APLICAÇÃO EM TESTES:** O valor da complexidade ciclomática de McCabe define o **número mínimo exato de casos de teste** necessários para garantir que todas as instruções e caminhos lógicos do método sejam executados ao menos uma vez!

---

## 3. Tipos Especializados de Testes e Automação

### 3.1 Testes de Regressão e Automação Contínua
- **Conceito de Teste de Regressão:** Bateria sistemática de testes executada após qualquer manutenção no software (correção de bugs, refatoração ou acréscimo de novas funcionalidades) para certificar que as alterações introduzidas **não causaram efeitos colaterais adversos nem reintroduziram defeitos antigos em módulos que funcionavam perfeitamente**;
- **Automação no Pipeline de CI/CD:** A suíte de testes de regressão deve ser integralmente automatizada e disparada a cada *commit* ou *Pull Request*, impedindo que código quebrado atinja o repositório principal.

---

### 3.2 Testes de Desempenho: Carga vs. Estresse vs. Pico vs. Resistência
A engenharia de testes de desempenho categoriza os testes de acordo com o padrão e a intensidade de tráfego injetado no sistema:

| Modalidade de Teste | Volume de Tráfego / Carga Injetada | Objetivo Específico da Avaliação |
| :--- | :--- | :--- |
| **Teste de Carga (*Load Testing*)** | Carga operacional esperada (normal e pico previsto em projeto). | Avaliar o comportamento do sistema, tempos de resposta e uso de hardware sob o volume regular de usuários acordado no SLA. |
| **Teste de Estresse (*Stress Testing*)** | Carga extrema que ultrapassa intencionalmente o limite de capacidade máxima do sistema. | Identificar o **ponto de quebra (*breaking point*)**, testar como o sistema falha (degradação graciosa) e como ele se recupera após o término da sobrecarga extrema. |
| **Teste de Pico (*Spike Testing*)** | Variações abruptas, repentinas e massivas de tráfego em intervalos de segundos. | Avaliar se a infraestrutura elástica e os balanceadores reagem com agilidade suficiente a picos súbitos de acesso. |
| **Teste de Resistência (*Soak / Endurance*)** | Carga moderada a alta mantida de forma ininterrupta por períodos prolongados (dias/semanas). | Detectar **vazamentos de memória (*memory leaks*)**, esgotamento de pools de conexões e saturação progressiva de disco. |

> 🚨 **ALERTA DE PROVA / PEGADINHA FCC:** Fique atento: Teste de **Carga** avalia o sistema *dentro* da capacidade contratual. Teste de **Estresse** empurra o sistema *além* do limite máximo com a finalidade expressa de quebrar o ambiente e avaliar a resiliência e recuperação.

---

### 3.3 Práticas de TDD (Test-Driven Development) e BDD (Behavior-Driven Development)
- **TDD (Desenvolvimento Guiado por Testes):** Técnica de engenharia de software fundamentada no ciclo rápido e iterativo de três fases: **Red $\rightarrow$ Green $\rightarrow$ Refactor**:
    1. *Red:* Escrever um teste automatizado que falha antes de escrever o código de produção;
    2. *Green:* Escrever o código mais simples possível apenas para fazer o teste passar com sucesso;
    3. *Refactor:* Limpar o código-fonte, eliminar duplicações e aperfeiçoar o design, garantindo que a suíte de testes continue verde.

- **BDD (Desenvolvimento Guiado por Comportamento):** Evolução colaborativa do TDD focada na linguagem ubíqua e no comportamento do sistema sob a ótica do negócio. Expressa cenários no formato **Given-When-Then** (*Dado que... Quando... Então...* - sintaxe Gherkin).

---

## 4. Revisão de Código, Refatoração e Dívida Técnica

### 4.1 Técnicas Modernas de Revisão de Código (Code Review)
A revisão de código é uma prática colaborativa indispensável de garantia da qualidade:

- **Inspeções Formais (Fagan):** Processo tradicional rígido com papéis formais (moderador, autor, leitor e inspetor) e reuniões presenciais de leitura de código;
- **Revisão Baseada em Pull Requests (Moderna / Ágil):** Conduzida de forma assíncrona em plataformas como GitHub/GitLab. Antes de realizar o *merge* para a branch principal, outros desenvolvedores inspecionam o diff, verificam aderência a padrões arquiteturais, segurança e ausência de code smells;
- **Pair Programming:** Revisão contínua em tempo real executada pelo copiloto (*Navigator*) enquanto o piloto (*Driver*) digita o código.

---

### 4.2 Refatoração de Código e os "Maus Cheiros" (Code Smells) de Fowler
- **Definição Canônica (Martin Fowler):** Refatoração (*Refactoring*) é o processo de **modificar a estrutura interna de um software sem alterar o seu comportamento observável externo**, visando melhorar a legibilidade, reduzir a complexidade e facilitar futuras manutenções.  
  > 🚨 **PEGADINHA FCC:** Refatoração **NÃO adiciona novas funcionalidades** e **NÃO corrige bugs de negócio**! Se o comportamento funcional externo mudou, houve evolução de software ou correção, e não pura refatoração.
- **Maus Cheiros de Código (*Code Smells*) Recorrentes:**
    - *Método Longo (*Long Method*):* Métodos com centenas de linhas de código. Técnica de correção: **Extract Method** (extrair trecho para novo método nomeado);
    - *Classe Grande / Objeto Deus (*Large Class / God Class*):* Classe que acumula responsabilidades demais. Correção: **Extract Class**;
    - *Código Duplicado (*Duplicated Code*):* Mesma estrutura lógica em múltiplos locais. Viola o princípio DRY;
    - *Cirurgia com Espingarda (*Shotgun Surgery*):* Cada pequena alteração em uma regra exige dezenas de pequenas modificações espalhadas em classes diferentes. Indica alto acoplamento e baixa coesão.

---

### 4.3 Dívida Técnica e o Quadrante de Martin Fowler
Cunhada por Ward Cunningham, a metáfora da **Dívida Técnica (*Technical Debt*)** compara o desenvolvimento acelerado e descuidado de software a um empréstimo financeiro bancário: você consegue entregar o produto mais rápido hoje, mas contrai uma dívida de código mal estruturado. Se a dívida não for quitada (por meio de refatoração), o sistema acumula "juros compostos" que tornam qualquer nova manutenção futura proibitivamente lenta e cara.

```mermaid
flowchart TD
    subgraph EixoPrudente["POSTURA PRUDENTE"]
        P_DEL["<b>Deliberada & Prudente:</b><br/>'Precisamos lançar o MVP agora pelo prazo legal,<br/>mas quitaremos a dívida na próxima sprint.'"]
        P_INA["<b>Inadvertida & Prudente:</b><br/>'Agora que o sistema está em produção,<br/>compreendemos qual é a arquitetura ideal.'"]
    end
    subgraph EixoImprudente["POSTURA IMPRUDENTE"]
        I_DEL["<b>Deliberada & Imprudente:</b><br/>'Não temos tempo para design nem testes,<br/>basta fazer funcionar rápido de qualquer jeito.'"]
        I_INA["<b>Inadvertida & Imprudente:</b><br/>'O que são padrões de projeto?<br/>Não sabemos como estruturar código.'"]
    end
    EixoPrudente ~~~ EixoImprudente
```

- **Deliberada e Prudente:** A equipe sabe exatamente como fazer da melhor forma, mas opta conscientemente por um atalho temporário para atingir uma janela crítica de mercado ou prazo legal, agendando formalmente a refatoração subsequente;
- **Inadvertida e Prudente:** Decorrente do aprendizado natural do time: após colocar o sistema em produção e observar o uso real, os arquitetos percebem qual deveria ter sido o melhor design;
- **Deliberada e Imprudente:** A equipe sabe que está gerando código de péssima qualidade e sem testes, mas adota atalhos por puro desleixo e negligência;
- **Inadvertida e Imprudente:** A equipe desconhece princípios básicos de engenharia de software e padrões de design, gerando código macarrônico por pura incompetência técnica.

---

## 5. Fontes Oficiais e Referências Bibliográficas

* [ISO/IEC 25010: Systems and software engineering - Systems and software Quality Requirements and Evaluation (SQuaRE)](https://iso25000.com/index.php/en/iso-25000-standards/iso-25010) - Padrão internacional de qualidade de produto de software.
* [Refactoring: Improving the Design of Existing Code (Martin Fowler)](https://refactoring.com/) - Catálogo de code smells e refatorações canônicas.
* [xUnit Test Patterns: Refactoring Test Code (Gerard Meszaros)](http://xunitpatterns.com/) - Classificação formal dos Dublês de Teste (*Test Doubles*).
* [The Practical Test Pyramid (Ham Vocke / Martin Fowler)](https://martinfowler.com/articles/practical-test-pyramid.html) - Distribuição e níveis da pirâmide de testes.
* [A Complexity Measure (Thomas J. McCabe - IEEE Transactions on Software Engineering)](https://ieeexplore.ieee.org/) - Artigo original da métrica de complexidade ciclomática.

---

## 6. Questões de Concurso FCC Comentadas

### Questão 01
**(FCC – TCE-GO – Analista de Controle Externo / TI)**  
Uma equipe de desenvolvimento de software do Tribunal de Contas concluiu a correção de uma vulnerabilidade de segurança e a implementação de uma nova funcionalidade na rotina de cadastro de credores. Antes de disponibilizar a nova versão em produção, o líder técnico determinou a execução imediata de um conjunto de testes automatizados com o objetivo específico de verificar se as alterações recentes introduzidas no código-fonte não afetaram adversamente ou causaram falhas em partes do sistema que funcionavam perfeitamente antes da alteração. O tipo de teste determinado pelo líder é o:

* **A)** Teste de estresse.
* **B)** Teste de regressão.
* **C)** Teste de carga.
* **D)** Teste de usabilidade.
* **E)** Teste de caixa-transparente destrutivo.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** O teste de estresse avalia o sistema sob sobrecarga extrema de infraestrutura além dos limites operacionais, sem foco em efeitos colaterais de novas linhas de código em funcionalidades estáveis.
> - **B) CORRETA.** O **Teste de Regressão** tem a finalidade precípua e específica de assegurar que novas alterações no código-fonte (sejam correções de defeitos, refatorações ou implementação de novos recursos) não causaram "regressão", isto é, não introduziram novos defeitos em funcionalidades que anteriormente se encontravam íntegras e funcionando de forma estável.
> - **C) Incorreta.** O teste de carga avalia o comportamento sob volume de requisições normais ou de pico contratual.
> - **D) Incorreta.** O teste de usabilidade verifica a ergonomia e facilidade de interação do usuário com a interface gráfica.
> - **E) Incorreta.** Nomenclatura fictícia sem amparo na literatura técnica de engenharia de software.
> 
> **Gabarito: B**

---

### Questão 02
**(FCC – TCE-GO – Técnico de Controle Externo / TI)**  
A respeito do conceito de refatoração (*refactoring*) de código em engenharia de software e da metáfora de dívida técnica, assinale a afirmativa correta:

* **A)** A refatoração consiste em alterar a lógica de negócio do software para adicionar novos recursos solicitados pelo cliente na sprint atual.
* **B)** A refatoração tem como objetivo aperfeiçoar a estrutura interna do código, tornando-o mais limpo, legível e manutenível, sem alterar o seu comportamento observável externo.
* **C)** A dívida técnica é um conceito que se aplica exclusivamente aos débitos financeiros de contratos de licitação em atraso.
* **D)** A prática do desenvolvimento guiado por testes (TDD) proíbe a realização de refatoração após os testes unitários passarem.
* **E)** Métodos longos com dezenas de parâmetros são considerados boas práticas de modularidade no padrão Clean Code.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** A adição de novas funcionalidades ou alterações no comportamento do software para o usuário constituem evolução ou manutenção adaptativa, contrariando a premissa de refatoração.
> - **B) CORRETA.** Conforme a definição clássica estabelecida por Martin Fowler, a **refatoração (*refactoring*)** é o processo de alterar e aprimorar a estrutura interna do código-fonte (eliminar duplicações, melhorar modularidade e legibilidade) **sem alterar o seu comportamento observável externo**.
> - **C) Incorreta.** A dívida técnica (*technical debt*) é uma célebre metáfora criada por Ward Cunningham no contexto do desenvolvimento de software para representar o custo cumulativo futuro gerado por atalhos arquiteturais e código mal projetado.
> - **D) Incorreta.** O TDD preconiza obrigatoriamente a refatoração como a sua terceira fase cíclica (*Red $\rightarrow$ Green $\rightarrow$ Refactor*).
> - **E) Incorreta.** Métodos longos (*Long Method*) constituem um dos mais graves "maus cheiros" (*code smells*), devendo ser eliminados via extração de métodos.
> 
> **Gabarito: B**

---

### Questão 03
**(FCC – TRF – Analista Judiciário / TI)**  
Considere um método Java que contém a seguinte estrutura lógica de decisões condicionais: três comandos `if` simples, um laço `while` e uma estrutura `switch-case` com quatro cláusulas `case` e uma cláusula `default`. Aplicando a técnica de teste de caixa-branca fundamentada na Complexidade Ciclomática de Thomas McCabe ($V(G)$), o número de caminhos linearmente independentes e, consequentemente, a quantidade mínima de casos de teste necessários para cobrir todos os fluxos de execução desse método é:

* **A)** 8.
* **B)** 9.
* **C)** 10.
* **D)** 12.
* **E)** 7.

> **Comentário Detalhado:**
>
> - A fórmula de cálculo da Complexidade Ciclomática de McCabe por pontos de decisão (predicados) é expressa por:
>   $$V(G) = P + 1$$
> - Mapeando os predicados de decisão do código:
>     - Três instruções `if` simples: $3$ predicados;
>     - Um laço de repetição `while`: $1$ predicado;
>     - Um comando `switch-case` com $4$ cláusulas `case`: $4$ predicados (a cláusula `default` é a rota padrão de escape e não pontua como predicado adicional).
> - Total de predicados: $P = 3 + 1 + 4 = 8$.
> - Aplicando a fórmula:
>   $$V(G) = 8 + 1 = 9$$
> - O número de caminhos linearmente independentes e a quantidade mínima de casos de teste para cobertura estrutural completa é **9**.
> 
> **Gabarito: B**

---

### Questão 04
**(FCC – TCE – Auditor de Controle Externo / TI)**  
No desenvolvimento guiado por testes (*Test-Driven Development* - TDD) e na criação de suítes de testes unitários isolados, utilizam-se diferentes tipos de dublês de teste (*Test Doubles*). O dublê que é configurado especificamente com expectativas prévias sobre quais métodos devem ser chamados, com quais argumentos e quantas vezes, fazendo com que o teste falhe caso essas interações não ocorram conforme esperado, é denominado:

* **A)** Dummy.
* **B)** Stub.
* **C)** Mock.
* **D)** Fake.
* **E)** Driver.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** O Dummy é um objeto utilizado unicamente para preencher argumentos exigidos por assinaturas de construtores ou métodos, sem jamais ser executado na lógica.
> - **B) Incorreta.** O Stub fornece respostas fixas pré-programadas para chamadas feitas durante o teste, mas não verifica expectativas de quantas vezes ou com quais argumentos foi chamado.
> - **C) CORRETA.** Conforme a classificação formal de Gerard Meszaros e Martin Fowler, o **Mock** é um dublê de teste orientado à verificação de comportamento. Ele é configurado previamente com expectativas estritas de chamadas e parâmetros; ao final da execução do teste, o mock valida se os métodos esperados foram acionados na quantidade e ordem programadas, reprovando o teste caso haja desvio.
> - **D) Incorreta.** O Fake é uma implementação funcional real, porém simplificada e inadequada para produção (ex.: repositório em memória).
> - **E) Incorreta.** Driver é o componente que aciona o módulo sob teste em abordagens ascendentes de integração (*bottom-up*).
> 
> **Gabarito: C**

---

### Questão 05
**(FCC – SEFAZ – Auditor de Tecnologia da Informação)**  
Uma equipe de testes de software planeja a execução de testes não-funcionais de desempenho em um portal tributário que receberá declarações fiscais. Para verificar o comportamento do sistema quando submetido a uma carga que ultrapassa intencionalmente a capacidade operacional máxima para a qual foi projetado, com o objetivo de observar como o sistema se comporta sob falha, se degrada graciosamente e como se recupera após a remoção da sobrecarga extrema, deve ser planejado um:

* **A)** Teste de Carga (*Load Testing*).
* **B)** Teste de Estresse (*Stress Testing*).
* **C)** Teste de Aceitação de Usuário (*UAT*).
* **D)** Teste de Sanidade (*Sanity Testing*).
* **E)** Teste de Fumaça (*Smoke Testing*).

> **Comentário Detalhado:**
>
> - **A) Incorreta.** O Teste de Carga avalia o sistema dentro das condições esperadas normais e nos picos previstos de projeto, sem o objetivo proposital de colapsar o ambiente.
> - **B) CORRETA.** O **Teste de Estresse (*Stress Testing*)** submete deliberadamente o software a volumes de requisições e cargas que ultrapassam a sua capacidade física projetada. O objetivo fundamental é observar o modo como o sistema se comporta sob colapso (garantindo que ele degrade graciosamente sem corromper dados) e verificar se ele é capaz de se recuperar autonomamente após o término do estresse.
> - **C) Incorreta.** O UAT é o teste final de homologação pelos usuários para validar se os requisitos de negócio foram atendidos.
> - **D) Incorreta.** O Teste de Sanidade é um subconjunto rápido de testes funcionais focado em validar se uma correção pontual de bug surtiu efeito sem efeitos colaterais imediatos.
> - **E) Incorreta.** O Teste de Fumaça (*Smoke Test*) é uma execução preliminar e superficial para verificar se a compilação do software é minimamente estável para iniciar a rodada de testes.
> 
> **Gabarito: B**
