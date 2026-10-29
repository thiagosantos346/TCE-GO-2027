import os, re

target_file = 'fontes_de_estudo/conhecimentos_especificos_b02_ti/04_engenharia_de_software/05_qualidade_testes_refatoracao_e_divida_tecnica.md'

with open(target_file, 'r', encoding='utf-8') as f:
    content = f.read()

rewrites = {}

rewrites['Teste 043'] = '''### Teste 043
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
Durante uma auditoria operacional de infraestrutura e acordos de nível de serviço (SLA) de TI em um Tribunal de Contas, a equipe de fiscalização analisou as métricas de confiabilidade e disponibilidade do portal de serviços ao jurisdicionado. No cálculo formal preconizado pela literatura de engenharia de software e normas ISO/IEC de qualidade de produto, utilizam-se o MTBF (*Mean Time Between Failures* - Tempo Médio Entre Falhas) e o MTTR (*Mean Time To Repair* - Tempo Médio Para Reparo). A fórmula clássica que expressa a Disponibilidade Operacional ($D$) de um sistema computacional é:

* **A)** $D = \\frac{MTBF}{MTBF + MTTR}$
* **B)** $D = \\frac{MTTR}{MTBF + MTTR}$
* **C)** $D = MTBF - MTTR$
* **D)** $D = \\frac{MTBF \\times MTTR}{100}$
* **E)** $D = \\frac{MTTR}{MTBF}$


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** A **Disponibilidade Operacional ($D$)** representa a fração de tempo em que o sistema está operacional e apto para uso. O tempo total de ciclo é a soma do tempo de operação estável ($MTBF$) com o tempo de indisponibilidade para reparo ($MTTR$). Logo, a disponibilidade é a razão entre o tempo produtivo e o tempo total: $D = \\frac{MTBF}{MTBF + MTTR}$.
> - **B) Incorreta.** Essa equação calcula a taxa de **indisponibilidade fracionária** (*unavailability*).
> - **C) Incorreta.** Subtração dimensionalmente desprovida de sentido estatístico para cálculo de disponibilidade percentual.
> - **D) Incorreta.** Produto desprovido de base teórica no cálculo de confiabilidade de sistemas.
> - **E) Incorreta.** A razão de MTTR por MTBF não representa percentual de disponibilidade.
>
> **Gabarito: A**'''

rewrites['Teste 044'] = '''### Teste 044
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
A Pirâmide de Testes, conceito consolidado na engenharia de software moderna por Mike Cohn e Martin Fowler, estabelece a proporção e distribuição ideal entre diferentes categorias de testes automatizados em um pipeline de integração contínua (CI/CD). Em conformidade com as diretrizes desse modelo, é correto afirmar:

* **A)** a base da pirâmide deve concentrar o maior volume de testes automatizados da aplicação, sendo constituída por Testes de Unidade, caracterizados por alta velocidade de execução, isolamento rigoroso de dependências externas e baixo custo de manutenção.
* **B)** o topo da pirâmide deve concentrar mais de 80% do esforço de testes por meio de testes manuais exaustivos de ponta a ponta na interface gráfica de usuário.
* **C)** a camada intermediária de testes de integração deve ser suprimida em arquiteturas de microsserviços, transferindo toda a validação de rede para os testes de unidade.
* **D)** a pirâmide recomenda a inversão de sua geometria (formato cone de sorvete) quando o sistema opera sob infraestrutura de nuvem pública.
* **E)** os testes de unidade demandam maior tempo de execução computacional do que os testes ponta a ponta em virtude da complexidade de mocks e stubs.


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** A **Pirâmide de Testes** prescreve:
>     - **Base (maior volume):** Testes de **Unidade** (rápidos, baratos, isolados, executam em milissegundos sem I/O pesado);
>     - **Meio (volume moderado):** Testes de **Integração / Serviços** (validam comunicação entre componentes, banco de dados e APIs);
>     - **Topo (menor volume):** Testes de **Ponta a Ponta (E2E / UI)** (lentos, caros, frágeis e suscetíveis a falsos positivos).
> - **B) Incorreta.** Concentrar o esforço no topo configura o anti-padrão do "cone de sorvete" (*ice-cream cone anti-pattern*), que torna a suíte lenta e instável.
> - **C) Incorreta.** Testes de integração são indispensáveis para validar comunicação entre módulos, bancos e contratos de rede.
> - **D) Incorreta.** O modelo em cone de sorvete é um anti-padrão nocivo a ser evitado em qualquer ambiente tecnológico.
> - **E) Incorreta.** Inversão completa: testes unitários são ordens de grandeza mais rápidos e leves que testes ponta a ponta.
>
> **Gabarito: A**'''

rewrites['Teste 045'] = '''### Teste 045
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
No desenvolvimento orientado por testes (*Test-Driven Development* - TDD) e na construção de testes unitários isolados para sistemas de auditoria corporativos, empregam-se diferentes categorias de dublês de teste (*Test Doubles*, conforme taxonomia de Gerard Meszaros). O dublê que é pré-configurado especificamente com expectativas formais sobre quais métodos devem ser chamados, com quais parâmetros exatos e em qual quantidade de invocações, fazendo com que o teste falhe automaticamente caso as interações não ocorram conforme o esperado, classifica-se como:

* **A)** Mock.
* **B)** Stub.
* **C)** Dummy.
* **D)** Fake.
* **E)** Spy.


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** Na taxonomia de Meszaros:
>     - **Mock:** É o dublê de **verificação de comportamento**. É pré-programado com *expectativas* (quais métodos devem ser chamados, parâmetros e contagem). O mock realiza verificação ativa e falha o teste caso o fluxo de chamadas divirja do esperado;
>     - **Stub:** Fornece respostas enlatadas (*canned answers*) pré-definidas para as chamadas feitas durante o teste, sem verificar comportamento;
>     - **Dummy:** Objeto passado apenas para preencher parâmetros de assinatura de método, nunca sendo invocado;
>     - **Fake:** Implementação simplificada funcionalmente funcional, mas inadequada para produção (ex.: banco em memória H2 ou repositório em HashMap);
>     - **Spy:** Registra passivamente informações sobre como foi chamado para verificação posterior (*asserts*).
> - **B) Incorreta.** O Stub retorna respostas fixas sem validar expectativas de chamadas.
> - **C) Incorreta.** O Dummy apenas preenche assinaturas sem uso ativo.
> - **D) Incorreta.** O Fake possui lógica funcional real simplificada.
> - **E) Incorreta.** O Spy registra chamadas, mas a verificação é feita a posteriori pelo teste, não por expectativas pré-programadas ativas como no Mock.
>
> **Gabarito: A**'''

rewrites['Teste 046'] = '''### Teste 046
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
No âmbito das técnicas funcionais de teste de software (Caixa-Preta), o Particionamento em Classes de Equivalência e a Análise de Valor Limite são métodos fundamentais para a seleção sistemática de casos de teste. A respeito dos fundamentos técnicos e das regras de aplicação dessas abordagens, é correto afirmar:

* **A)** No particionamento em classes de equivalência, divide-se o domínio de dados de entrada em partições válidas e inválidas, partindo da premissa de que qualquer dado representativo selecionado dentro de uma mesma partição revelará comportamento análogo do sistema.
* **B)** O particionamento em classes de equivalência requer a descompilação e análise do código-fonte para contabilizar o número de instruções condicionais `if-else`.
* **C)** A análise de valor limite assume que a probabilidade de ocorrência de erros no software é estatisticamente uniforme em todo o intervalo contínuo de entrada, dispensando testes nas fronteiras.
* **D)** As técnicas de teste funcional de caixa-preta baseiam-se primordialmente na complexidade ciclomática de McCabe e na cobertura de comandos do código compilado.
* **E)** A análise de valor limite restringe-se a testar exclusivamente o ponto médio aritmético de cada partição, ignorando os extremos superior e inferior.


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** O **Particionamento em Classes de Equivalência** divide o domínio de entrada em partições de dados equivalentes (válidas e inválidas). Assume-se que todos os membros de uma partição são tratados da mesma forma pela aplicação; logo, testar um único valor típico de cada classe é suficiente para inferir a conformidade dos demais.
> - **B) Incorreta.** Inspecionar código-fonte ou descompilar binários é característica de testes estruturais (**Caixa-Branca**), e não de técnicas funcionais de Caixa-Preta.
> - **C) Incorreta.** A premissa da **Análise de Valor Limite** é exatamente oposta: a vasta maioria dos defeitos de software concentra-se nas **fronteiras e limites** das classes de equivalência ($min$, $min-1$, $min+1$, $max$, $max-1$, $max+1$).
> - **D) Incorreta.** Complexidade ciclomática e cobertura de comandos são métricas de teste de Caixa-Branca.
> - **E) Incorreta.** O ponto médio aritmético é o valor típico testado no particionamento de equivalência; o valor limite foca estritamente nas fronteiras superior e inferior.
>
> **Gabarito: A**'''

rewrites['Teste 047'] = '''### Teste 047
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
Considere um método Java que implementa a regra de validação de elegibilidade de licitantes em um sistema de compras governamentais. A inspeção do grafo de fluxo de controle desse método identificou três comandos condicionais `if` simples independentes, uma estrutura de repetição `while` e um comando `switch-case` composto por quatro cláusulas `case` e uma cláusula `default`. Aplicando a técnica de teste estrutural de Caixa-Branca baseada na Complexidade Ciclomática de Thomas McCabe ($V(G)$), a quantidade de caminhos linearmente independentes e, consequentemente, o número mínimo de casos de teste necessários para assegurar cobertura integral de ramificações (*branch coverage*) é:

* **A)** 9.
* **B)** 8.
* **C)** 10.
* **D)** 12.
* **E)** 7.


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** Pela consagrada métrica de Complexidade Ciclomática de McCabe:
>     $$V(G) = P + 1$$
>     onde $P$ representa a quantidade de pontos de decisão (predicados binários no código):
>     - 3 comandos `if` simples = 3 pontos de decisão;
>     - 1 laço `while` = 1 ponto de decisão;
>     - 1 estrutura `switch` com 4 cláusulas `case` = 4 pontos de decisão (cada `case` atua como um desvio alternativo; o `default` é o caminho residual).
>     
>     Total de pontos de decisão: $P = 3 + 1 + 4 = 8$.  
>     Logo: $V(G) = 8 + 1 = 9$ caminhos linearmente independentes.
> - **B) Incorreta.** Equivale a calcular apenas $P$ sem somar o caminho linear básico ($+1$).
> - **C) Incorreta.** Contabilizou indevidamente o ramo `default` como predicado adicional.
> - **D) Incorreta.** Valor arbitrário inflacionado.
> - **E) Incorreta.** Subestimou as ramificações do laço de repetição ou dos desvios `case`.
>
> **Gabarito: A**'''

rewrites['Teste 048'] = '''### Teste 048
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
Uma equipe de desenvolvimento do Tribunal de Contas concluiu a refatoração e a correção de um defeito crítico no módulo de cálculo de prazos de processos administrativos. Antes de autorizar a implantação da nova versão no ambiente de homologação, o auditor líder de testes determinou a execução imediata de uma suíte de testes com a finalidade específica de assegurar que a alteração realizada ou o defeito corrigido não introduziram novos erros ou efeitos colaterais indesejados em partes do software que funcionavam perfeitamente antes da modificação. Essa categoria de teste classifica-se como:

* **A)** Teste de Regressão.
* **B)** Teste de Estresse.
* **C)** Teste de Carga.
* **D)** Teste de Usabilidade.
* **E)** Teste de Penetração (*Pentest*).


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** O **Teste de Regressão** consiste na reexecução seletiva ou total de suítes de testes previamente aprovadas após qualquer modificação de código (correção de bugs, refatoração, atualização de dependências ou acréscimo de novas features), visando certificar que as funcionalidades estáveis pré-existentes não sofreram "regressão" ou danos acidentais.
> - **B) Incorreta.** O Teste de Estresse avalia o comportamento do sistema sob sobrecargas extremas além de sua capacidade operacional máxima.
> - **C) Incorreta.** O Teste de Carga afere a performance e tempo de resposta sob volumes operacionais esperados em produção.
> - **D) Incorreta.** O Teste de Usabilidade avalia a facilidade de navegação, ergonomia e experiência do usuário na interface gráfica.
> - **E) Incorreta.** O Teste de Penetração avalia brechas de segurança cibernética e vetores de exploração de vulnerabilidades.
>
> **Gabarito: A**'''

rewrites['Teste 049'] = '''### Teste 049
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
Durante a auditoria de desempenho de um sistema de transmissão eletrônica de folhas de pagamento dos municípios jurisdicionados ao Tribunal de Contas, a equipe técnica planejou a execução de testes não-funcionais. O objetivo é submeter intencionalmente o cluster computacional a um volume de requisições concorrentes e tráfego que extrapole significativamente a sua capacidade operacional de pico, visando observar se o sistema degrada graciosamente suas funções, se mantém a consistência dos dados sob pane e de que maneira se restabelece após o cessamento da sobrecarga extrema. Esse teste de desempenho classifica-se como:

* **A)** Teste de Estresse (*Stress Testing*).
* **B)** Teste de Carga (*Load Testing*).
* **C)** Teste de Aceitação de Usuário (*UAT*).
* **D)** Teste de Fumaça (*Smoke Testing*).
* **E)** Teste de Sanidade (*Sanity Testing*).


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** O **Teste de Estresse (*Stress Testing*)** tem como finalidade primordial avaliar a robustez, disponibilidade e resiliência de um sistema computacional quando submetido a condições operacionais que **extrapolam intencionalmente os limites máximos de projeto** (*breaking point*), verificando se ocorrem falhas catastróficas, vazamentos de memória ou corrupção de dados e como se dá sua capacidade de autorrecuperação.
> - **B) Incorreta.** O Teste de Carga (*Load Testing*) testa o sistema operando dentro dos limites operacionais máximos previstos em regime normal ou de pico para medir latência e vazão.
> - **C) Incorreta.** O UAT é o teste formal executado pelos usuários de negócio para validar se a aplicação atende às regras funcionais contratadas.
> - **D) Incorreta.** O Smoke Test é uma bateria superficial rápida para checar se a compilação inicial da versão é estável o suficiente para iniciar os testes aprofundados.
> - **E) Incorreta.** O Sanity Test é uma verificação pontual e rápida após uma correção isolada para garantir que a funcionalidade pontual alterada está respondendo.
>
> **Gabarito: A**'''

rewrites['Teste 050'] = '''### Teste 050
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
A disciplina do Desenvolvimento Orientado por Testes (*Test-Driven Development* - TDD), preconizada por Kent Beck na metodologia Extreme Programming, estrutura a atividade de programação em torno de microiterações sistemáticas e disciplinadas conhecidas como o ciclo *Red-Green-Refactor*. A correta sequência de ações que define esse ciclo canônico estabelece que o desenvolvedor deve:

* **A)** 1. Escrever um teste unitário automatizado que falha porque a funcionalidade ainda não foi implementada (Red); 2. Escrever o código mínimo necessário de produção para fazer o teste passar com sucesso (Green); 3. Aperfeiçoar o design e a legibilidade do código, eliminando duplicações, assegurando que todos os testes continuem passando (Refactor).
* **B)** 1. Escrever o código completo de produção em camada de controle (Green); 2. Analisar falhas de compilação em tempo de execução (Red); 3. Otimizar as tabelas do banco de dados relacional (Refactor).
* **C)** 1. Refatorar classes legadas sem cobertura de testes automatizados (Refactor); 2. Escrever testes exploratórios manuais na interface com o usuário (Red); 3. Publicar o incremento em produção assistida (Green).
* **D)** 1. Gerar relatórios automatizados de violação de cobertura com SonarQube (Red); 2. Submeter pull request para autorização do comitê diretivo (Green); 3. Reescrever a documentação funcional do sistema (Refactor).
* **E)** 1. Codificar os métodos de produção e as classes de teste de forma simultânea e acoplada no mesmo arquivo fonte (Green); 2. Aguardar a execução noturna da esteira CI/CD (Red); 3. Limpar variáveis de ambiente (Refactor).


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** O ciclo mestre do **TDD** é estruturado estritamente em três fases consecutivas:
>     1. **Red:** Escreve-se um teste unitário automatizado que expressa o comportamento desejado. O teste falha compulsoriamente (ficando vermelho), pois a funcionalidade ainda não existe;
>     2. **Green:** Escreve-se o código de produção estritamente mínimo e indispensável para fazer o teste passar (ficando verde);
>     3. **Refactor:** Aperfeiçoa-se a qualidade interna do código (eliminando duplicações, melhorando nomenclatura e arquitetura), mantendo a garantia de segurança de que a suíte de testes permanece verde.
> - **B) Incorreta.** Inverte a ordem lógica: no TDD o teste sempre nasce antes do código funcional.
> - **C) Incorreta.** Refatorar código sem a retaguarda de testes automatizados é violação das premissas de engenharia segura.
> - **D) Incorreta.** Distorção com burocracias e ferramentas periféricas que não representam o ciclo ágil de TDD.
> - **E) Incorreta.** Testes e código de produção residem em estruturas de diretórios segregadas (`src/main` e `src/test`), e a iteração do ciclo ocorre em questão de segundos a minutos.
>
> **Gabarito: A**'''

rewrites['Teste 051'] = '''### Teste 051
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
Em equipes de desenvolvimento de alta maturidade em Tribunais de Contas, a Revisão de Código (*Code Review*) por pares via *Pull Requests* associada à Análise Estática de Código compõe uma política essencial de controle de qualidade e governança. Em relação aos fundamentos dessas práticas de engenharia de software, é correto afirmar:

* **A)** As ferramentas de análise estática de código examinam o código-fonte ou binários compilados sem executá-los dinamicamente, identificando potenciais falhas de segurança conhecidas, violações de diretrizes de codificação, duplicações de trechos e índices excessivos de complexidade ciclomática.
* **B)** A análise estática de código exige compulsoriamente que o software esteja em execução ativa em ambiente de produção sob carga real de requisições.
* **C)** A revisão de código por pares (*Code Review*) destina-se exclusivamente a medir o tempo e a quantidade nominal de linhas escritas por cada programador para subsidiar avaliações de desempenho individual.
* **D)** A adoção de ferramentas automatizadas de análise estática de qualidade dispensa inteiramente a necessidade de testes funcionais e de integração na esteira CI/CD.
* **E)** As análises de código devem ser executadas com periodicidade exclusivamente anual no encerramento de cada exercício contábil.


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** A **Análise Estática de Código** (executada por ferramentas como SonarQube, Checkstyle e linters) analisa o código sem executá-lo, detectando antecipadamente *code smells*, riscos de segurança (vulnerabilidades OWASP), código duplicado, violações de padrões arquiteturais e métricas de complexidade e acoplamento.
> - **B) Incorreta.** Inversão conceitual: o exame com o software em execução dinâmica sob carga caracteriza a **Análise Dinâmica de Código** (DAST / profiling), não a análise estática.
> - **C) Incorreta.** Code Review é uma prática colaborativa voltada a assegurar qualidade técnica, aderência a padrões arquiteturais e disseminação de conhecimento, não uma ferramenta punitiva de medição de linhas de código.
> - **D) Incorreta.** A análise estática identifica defeitos estruturais e estilísticos, mas é incapaz de testar a lógica dinâmica de execução de regras de negócio, que depende de testes funcionais.
> - **E) Incorreta.** Práticas modernas de DevOps incorporam a análise estática e o code review continuamente a cada *commit* ou *pull request*.
>
> **Gabarito: A**'''

rewrites['Teste 052'] = '''### Teste 052
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
A respeito da técnica de refatoração (*refactoring*) de código em engenharia de software e de sua aplicação na prevenção e pagamento de débitos estruturais, assinale a afirmativa tecnicamente correta:

* **A)** A refatoração consiste no processo de alterar a estrutura interna de um software para torná-lo mais compreensível e manutenível, reduzindo seu custo de evolução, sem que haja modificação no seu comportamento observável externo.
* **B)** A refatoração caracteriza-se compulsoriamente pela inclusão de novos requisitos de negócio demandados pelos usuários na iteração em andamento.
* **C)** O termo dívida técnica refere-se exclusivamente aos custos financeiros contratuais e contingências tributárias de licenciamento de software proprietário.
* **D)** A metodologia do desenvolvimento guiado por testes (TDD) proíbe a realização de refatorações de código após a aprovação da suíte de testes unitários.
* **E)** A presença de classes gigantes (*God Classes*) e métodos extensos repletos de responsabilidades dispersas é considerada um padrão arquitetural desejável em sistemas corporativos.


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** Definição formal cunhada por Martin Fowler: a **Refatoração (*Refactoring*)** é uma modificação na estrutura interna do software para torná-lo mais fácil de entender e mais barato de modificar, **sem alterar o seu comportamento observável externo** (as entradas produzem rigorosamente as mesmas saídas esperadas).
> - **B) Incorreta.** Se há alteração de comportamento observável ou inclusão de novos requisitos de negócio, não se trata de refatoração pura, mas de desenvolvimento evolutivo de novas funcionalidades.
> - **C) Incorreta.** Dívida Técnica (*Technical Debt*) é uma metáfora técnica de engenharia de software para custos ocultos de manutenção e retrabalho decorrentes de atalhos e código mal estruturado.
> - **D) Incorreta.** Pelo contrário: o passo *Refactor* é a terceira etapa obrigatória do ciclo canônico do TDD (*Red-Green-Refactor*).
> - **E) Incorreta.** God classes e métodos longos constituem graves *code smells* (sintomas de má qualidade) que violam o princípio da responsabilidade única.
>
> **Gabarito: A**'''

rewrites['Teste 053'] = '''### Teste 053
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
O conceito de Dívida Técnica (*Technical Debt*), cunhado originariamente por Ward Cunningham e categorizado no célebre "Quadrante da Dívida Técnica" por Martin Fowler, estabelece uma analogia entre decisões arquiteturais apressadas e empréstimos financeiros. No quadrante de Fowler, quando uma equipe técnica de desenvolvimento adota conscientemente uma solução temporária simplificada para atender a um prazo legal inadiável fixado pelo Tribunal de Contas, mantendo pleno conhecimento das deficiências técnicas da solução e planejando seu pagamento nas Sprints subsequentes de estabilização, essa dívida é classificada como:

* **A)** Prudente e Deliberada.
* **B)** Imprudente e Inadvertida.
* **C)** Imprudente e Deliberada.
* **D)** Prudente e Inadvertida.
* **E)** Acidental e Irreversível.


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** No **Quadrante da Dívida Técnica de Martin Fowler** (cruzando os eixos Prudente/Imprudente com Deliberada/Inadvertida):
>     - **Prudente e Deliberada:** A equipe possui alto conhecimento técnico, calcula conscientemente o custo-benefício de antecipar a entrega (*"precisamos lançar a solução agora para atender ao prazo legal; sabemos as limitações e pagaremos esse débito na próxima Sprint"*);
>     - **Imprudente e Deliberada:** A equipe ignora as boas práticas por preguiça ou desleixo (*"não temos tempo para arquitetura ou testes, entregue de qualquer jeito"*);
>     - **Imprudente e Inadvertida:** A equipe desconhece práticas básicas de engenharia (*"o que são princípios SOLID ou testes automatizados?"*);
>     - **Prudente e Inadvertida:** A equipe aplica as melhores práticas, mas, após a entrega, aprende novos aspectos sobre o domínio que revelam como o sistema poderia ter sido desenhado de forma melhor.
> - **B) Incorreta.** "Imprudente e Inadvertida" decorre da inexperiência e desconhecimento da equipe.
> - **C) Incorreta.** "Imprudente e Deliberada" ocorre quando atalhos de má qualidade são adotados por descaso, sem planos de pagamento.
> - **D) Incorreta.** "Prudente e Inadvertida" ocorre quando a percepção da dívida surge apenas a posteriori por evolução do conhecimento do time.
> - **E) Incorreta.** Classificação inexistente no quadrante conceitual de Fowler.
>
> **Gabarito: A**'''

for t_id, block in rewrites.items():
    full_pattern = rf'### {t_id}\s*\n+\*\*[^\n]+\*\*\s*\n+.*?>\s*\*\*Gabarito:\s*[A-E]\*\*'
    match = re.search(full_pattern, content, re.DOTALL)
    if not match:
        print(f'ERRO: Bloco {t_id} nao localizado com regex!')
    else:
        content = content[:match.start()] + block + content[match.end():]
        print(f'SUCESSO: Bloco {t_id} substituido perfeitamente.')

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(content)

print('Arquivo 05_qualidade_testes_refatoracao_e_divida_tecnica.md atualizado com sucesso!')

