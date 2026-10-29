import os, re

target_file = 'fontes_de_estudo/conhecimentos_especificos_b02_ti/04_engenharia_de_software/01_ciclo_de_vida_e_metodologias_ageis.md'

with open(target_file, 'r', encoding='utf-8') as f:
    content = f.read()

rewrites = {}

rewrites['Teste 001'] = '''### Teste 001
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
Durante uma auditoria de conformidade em contratações de soluções de tecnologia da informação em um órgão estadual, a equipe de fiscalização analisou a exigência editalícia de comprovação de maturidade em processos de software com base nos modelos CMMI (*Capability Maturity Model Integration*) e MPS.BR (*Melhoria de Processo do Software Brasileiro*). A respeito da estrutura de avaliação e dos níveis formais desses referenciais, é correto afirmar:

* **A)** No CMMI em sua representação por estágios, a organização atinge níveis de maturidade escalonados de 1 a 5, ao passo que o modelo de referência do MPS.BR (MR-MPS-SW) estrutura-se em 7 níveis de maturidade denominados de G (mais elementar) a A (mais avançado/otimizado).
* **B)** O MPS.BR adota 5 níveis de maturidade classificados alfabeticamente de A a E, enquanto o CMMI estabelece 7 níveis de maturidade representados em algarismos romanos.
* **C)** O CMMI restringe-se exclusivamente à representação contínua por áreas de processo, sendo vedada a avaliação por estágios organizacionais de maturidade.
* **D)** O MPS.BR foi concebido como um padrão proprietário incompatível com as normas técnicas internacionais ISO/IEC 12207 e ISO/IEC 15504 (SPICE).
* **E)** Ambos os modelos de maturidade vedam a utilização de metodologias e práticas ágeis (como Scrum e XP) em organizações que pleiteiem certificação nos seus níveis mais elevados.


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** Exatamente a distinção normativa frequentemente cobrada pela FCC: no CMMI por estágios (*staged representation*), existem 5 níveis de maturidade numerados de 1 (Inicial) a 5 (Otimizado). Por sua vez, o MPS.BR (MR-MPS-SW) adota 7 níveis alfabéticos em escala inversa de maturidade: G (Parcialmente Gerenciado), F (Gerenciado), E (Parcialmente Definido), D (Definido), C (Totalmente Definido), B (Gerenciado Quantitativamente) e A (Em Otimização).
> - **B) Incorreta.** Inversão quantitativa e conceitual: o MPS.BR possui 7 níveis (G a A) e o CMMI possui 5 níveis por estágios (1 a 5).
> - **C) Incorreta.** O CMMI oferece duas representações oficiais: a representação por Estágios (níveis de maturidade de 1 a 5) e a representação Contínua (níveis de capacidade de 0 a 3 aplicados a cada área de prática/processo).
> - **D) Incorreta.** O MPS.BR foi arquitetado expressamente em estrita conformidade com os referenciais internacionais ISO/IEC 12207 (Ciclos de Vida de Software) e ISO/IEC 15504 / 33000 (Avaliação de Processos de Software).
> - **E) Incorreta.** Não há vedação; as versões recentes tanto do CMMI quanto do MPS.BR incorporam formalmente práticas ágeis e híbridas em seus guias de avaliação.
>
> **Gabarito: A**'''

rewrites['Teste 002'] = '''### Teste 002
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
Ao examinar os artefatos de governança e ciclo de vida de desenvolvimento de software em um Tribunal de Contas, o Auditor de TI verificou a aplicação do Modelo em Espiral, concebido por Barry Boehm, para o desenvolvimento de um sistema analítico crítico de alta complexidade. A característica técnica que diferencia estruturalmente o Modelo em Espiral do modelo tradicional em Cascata (*Waterfall*) consiste em:

* **A)** adotar a análise e mitigação explícita e contínua de riscos técnicos e de negócio como o direcionador central de cada iteração da espiral.
* **B)** abolir totalmente a elaboração de especificações textuais de requisitos em prol de testes manuais em ambiente de produção.
* **C)** impor o congelamento rígido e imutável de todos os requisitos do sistema antes da elaboração do primeiro protótipo arquitetural.
* **D)** exigir a obrigatoriedade da programação em pares (*pair programming*) em todas as estações de trabalho do projeto.
* **E)** postergar os testes de integração e homologação de software para um momento posterior à entrada definitiva em operação assistida.


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** O diferencial marcante do **Modelo em Espiral de Barry Boehm** é ser um paradigma **orientado a riscos (*risk-driven*)**. Cada ciclo ("volta da espiral") contempla expressamente quatro quadrantes: determinação de objetivos, avaliação e mitigação de riscos, engenharia do produto e planejamento da próxima fase. Se os riscos não puderem ser mitigados a um nível aceitável, o projeto pode ser encerrado preventivamente.
> - **B) Incorreta.** O modelo em espiral não descarta documentação formal; a eliminação radical de documentos é distorção alheia ao modelo de Boehm.
> - **C) Incorreta.** O congelamento inicial e pétreo de requisitos é marca do modelo em Cascata tradicional, não do modelo em Espiral, cujos requisitos evoluem incrementalmente a cada volta da espiral.
> - **D) Incorreta.** A programação em pares é prática técnica originária da metodologia ágil Extreme Programming (XP).
> - **E) Incorreta.** Cada ciclo da espiral inclui testes, verificação e validação progressiva dos artefatos produzidos.
>
> **Gabarito: A**'''

rewrites['Teste 003'] = '''### Teste 003
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
O Processo Unificado (*Rational Unified Process* - RUP) é um modelo de ciclo de vida de desenvolvimento de software iterativo e incremental, caracterizado por ser centrado em arquitetura e dirigido por casos de uso. Ao auditar as fases cronológicas de um contrato estruturado sob o RUP, o auditor identifica que a fase cujo objetivo precíua e formalmente estabelecido é mitigar os riscos técnicos mais severos e validar a linha de base arquitetural executável (*executable architectural baseline*) denomina-se:

* **A)** Elaboração (*Elaboration*).
* **B)** Concepção / Iniciação (*Inception*).
* **C)** Construção (*Construction*).
* **D)** Transição (*Transition*).
* **E)** Homologação Operacional (*Acceptance*).


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** No RUP, a fase de **Elaboração (*Elaboration*)** destina-se a analisar o domínio do problema, estabelecer a baseline da arquitetura executável estável, mitigar os riscos técnicos de maior impacto e especificar detalhadamente a maioria dos casos de uso críticos.
> - **B) Incorreta.** A fase de Concepção (*Inception*) estabelece o escopo de negócio do projeto, a viabilidade econômica preliminar e a visão global da solução.
> - **C) Incorreta.** A fase de Construção (*Construction*) foca na codificação em larga escala, integração sistemática de módulos e desenvolvimento dos casos de uso restantes.
> - **D) Incorreta.** A fase de Transição (*Transition*) destina-se à implantação do sistema no ambiente dos usuários, testes beta, migração de dados e treinamento operacional.
> - **E) Incorreta.** "Homologação Operacional" não é uma das quatro fases canônicas estruturais do RUP.
>
> **Gabarito: A**'''

rewrites['Teste 004'] = '''### Teste 004
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
O Manifesto para o Desenvolvimento Ágil de Software, marco histórico do movimento ágil firmado em 2001, consagrou 4 valores fundamentais e 12 princípios norteadores. Entre as diretrizes expressamente consagradas nos 12 princípios formais do Manifesto Ágil, insere-se:

* **A)** aceitar alterações de requisitos, mesmo em fases adiantadas do projeto, aproveitando as mudanças para promover vantagem competitiva para o cliente.
* **B)** priorizar a formalização documental detalhada de todas as regras de negócio antes de iniciar a construção dos incrementos funcionais.
* **C)** realizar entregas de incrementos de software executável exclusivamente ao término de cada exercício financeiro da organização.
* **D)** condicionar o avanço do desenvolvimento à validação jurídica de termos de responsabilidade assinados por todas as partes envolvidas.
* **E)** canalizar a troca de informações entre desenvolvedores e gestores prioritariamente por meio de relatórios formais periódicos de status report.


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** Transcrição do segundo princípio do Manifesto Ágil: *"Aceitar mudanças de requisitos, mesmo no fim do desenvolvimento. Processos ágeis se adequam a mudanças, para que o cliente possa tirar vantagens competitivas"*.
> - **B) Incorreta.** O Manifesto valoriza *"software em funcionamento mais que documentação abrangente"*, repudiando documentações prévias exaustivas que retardem a entrega de valor.
> - **C) Incorreta.** O princípio prescreve *"entregar software funcionando com frequência, na escala de semanas a meses, com preferência aos períodos mais curtos"*, e não intervalos anuais burocráticos.
> - **D) Incorreta.** Falsa burocracia: o valor ágil preconiza *"colaboração com o cliente mais que negociação de contratos"*.
> - **E) Incorreta.** O Manifesto enfatiza que *"o método mais eficiente e eficaz de transmitir informações para e entre uma equipe de desenvolvimento é a conversa face a face"*.
>
> **Gabarito: A**'''

rewrites['Teste 005'] = '''### Teste 005
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
A respeito da composição estrutural e das responsabilidades do Scrum Team delineadas na versão oficial do Guia Scrum (2020), considere as seguintes afirmativas:

I. O Scrum Team é uma equipe coesa composta por um Product Owner, um Scrum Master e os Desenvolvedores, caracterizando-se essencialmente por ser multifuncional e autogerenciada.  
II. O Product Owner é o único responsável pela gestão eficaz do Product Backlog e pela maximização do valor decorrente do trabalho executado, não existindo relação de subordinação hierárquica entre ele e os demais integrantes do time.  
III. O Scrum Master atua como chefe executivo do time ágil, cabendo-lhe distribuir privativamente as tarefas diárias nominais e aprovar as horas registradas pelos desenvolvedores.  

Em relação às prescrições normativas do Guia Scrum, está correto o que se afirma em:

* **A)** I e II, apenas.
* **B)** I, apenas.
* **C)** III, apenas.
* **D)** II e III, apenas.
* **E)** I, II e III.


---

> **Comentário Detalhado:**
>
> - **I. Correta.** Conforme o Guia Scrum 2020, o Scrum Team não tem hierarquias internas nem subequipes; é uma unidade autogerenciada (a própria equipe decide quem faz o que, quando e como) e multifuncional (possui internamente todas as competências necessárias para gerar valor em cada Sprint).
> - **II. Correta.** O Product Owner é explicitamente a pessoa responsável por maximizar o valor do produto e gerenciar com transparência o Product Backlog. Ele atua como par colaborativo, inexistindo subordinação hierárquica com o time.
> - **III. Incorreta.** No Scrum, o Scrum Master é um verdadeiro líder que serve (*servant leader*), responsável pela eficácia do Scrum Team e por remover impedimentos organizacionais. Ele **não é chefe/gerente funcional** e não atribui tarefas nominais — os próprios desenvolvedores selecionam e distribuem as tarefas do Sprint Backlog.
>
> **Gabarito: A**'''

rewrites['Teste 006'] = '''### Teste 006
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
Em um projeto de modernização tecnológica de um Tribunal de Contas gerido por meio do framework Scrum, um auditor acompanhou a dinâmica dos eventos da equipe. A respeito do evento *Daily Scrum* (Reunião Diária), em estrita conformidade com o Guia Scrum (versão 2020), é correto afirmar:

* **A)** Trata-se de um evento com tempo limite (*timebox*) de 15 minutos destinado aos Desenvolvedores do Scrum Team para inspecionar o progresso em direção à Meta da Sprint e adaptar o planejamento do Sprint Backlog para as próximas 24 horas.
* **B)** Consiste em uma sessão formal de prestação de contas dos desenvolvedores para o Scrum Master e o Product Owner, que atuam avaliando metas individuais de produtividade.
* **C)** Possui duração proporcional ao tamanho da iteração, sendo estabelecido o tempo fixo de 45 minutos para Sprints com duração de quatro semanas.
* **D)** Exige compulsoriamente que cada integrante responda a três perguntas pré-determinadas sob pena de invalidação da ata do dia.
* **E)** Não pode ser realizada caso o Product Owner esteja ausente, exigindo a convocação de nova data e horário pela gerência do projeto.


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** Nos termos literais do Guia Scrum 2020: a Daily Scrum é um evento de **15 minutos** para os **Desenvolvedores** do Scrum Team inspecionarem o progresso em direção à **Meta da Sprint (*Sprint Goal*)** e adaptarem o Sprint Backlog conforme necessário, ajustando o plano de ação imediato para o próximo dia útil.
> - **B) Incorreta.** Inversão de papel: a Daily Scrum não é uma reunião gerencial de prestação de contas individual (*status report*), mas uma sessão técnica e colaborativa de planejamento e sincronização entre os desenvolvedores.
> - **C) Incorreta.** O timebox da Daily Scrum é fixo em **15 minutos**, independentemente de a Sprint durar uma, duas, três ou quatro semanas.
> - **D) Incorreta.** O Guia Scrum 2020 aboliu as três perguntas prescritivas fixas (o que fiz ontem, o que farei hoje, quais impedimentos), deixando o formato da conversa a critério autônomo dos desenvolvedores, desde que foquem na Meta da Sprint.
> - **E) Incorreta.** A Daily Scrum é um evento privativo dos Desenvolvedores; a ausência de papéis externos não impede sua execução regular.
>
> **Gabarito: A**'''

rewrites['Teste 007'] = '''### Teste 007
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
A versão 2020 do Guia Scrum introduziu uma estrutura de transparência e responsabilização na qual cada um dos três artefatos do Scrum contém um compromisso formal associado para reforçar o foco e medir o progresso da equipe. De acordo com o Guia Scrum oficial, os compromissos vinculados, respectivamente, ao *Product Backlog*, ao *Sprint Backlog* e ao *Incremento* são:

* **A)** Meta do Produto (*Product Goal*), Meta da Sprint (*Sprint Goal*) e Definição de Pronto (*Definition of Done*).
* **B)** Definição de Pronto (*Definition of Done*), Meta da Sprint (*Sprint Goal*) e Meta do Produto (*Product Goal*).
* **C)** Visão Estratégica, Critérios de Aceite e Homologação Final de Produção.
* **D)** Termo de Abertura, Cronograma Físico-Financeiro e Matriz de Riscos.
* **E)** Velocidade do Time, Gráfico de Burndown e Diagrama de Fluxo Cumulativo.


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** O Guia Scrum oficial de 2020 estruturou formalmente a associação unívoca entre artefatos e compromissos:
>     - Para o **Product Backlog**, o compromisso é a **Meta do Produto (*Product Goal*)**;
>     - Para o **Sprint Backlog**, o compromisso é a **Meta da Sprint (*Sprint Goal*)**;
>     - Para o **Incremento**, o compromisso é a **Definição de Pronto (*Definition of Done - DoD*)**.
> - **B) Incorreta.** Apresenta inversão na correspondência dos compromissos formais com seus respectivos artefatos.
> - **C) Incorreta.** Mistura práticas gerenciais complementares que não constituem os três compromissos normativos do Scrum 2020.
> - **D) Incorreta.** Trata-se de artefatos clássicos e prescritivos de gestão preditiva de projetos (PMBOK tradicional), alheios aos compromissos do Scrum.
> - **E) Incorreta.** Velocidade, Burndown e CFD são métricas analíticas e ferramentas visuais de acompanhamento, não compromissos de artefatos.
>
> **Gabarito: A**'''

rewrites['Teste 008'] = '''### Teste 008
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
No acompanhamento visual e na gestão quantitativa do progresso de equipes ágeis em um projeto de fiscalização de TI, utilizam-se com frequência os gráficos *Sprint Burndown* e *Release Burnup*. A respeito da interpretação técnica e das características comparativas desses gráficos, é correto afirmar:

* **A)** no gráfico de *Sprint Burndown*, o eixo vertical quantifica o trabalho restante planejado e o eixo horizontal representa o tempo; quando a linha real situa-se abaixo da linha ideal de tendência, indica que a equipe está com ritmo de entrega adiantado em relação ao cronograma previsto.
* **B)** no gráfico de *Sprint Burndown*, o traçado da linha real deve ascender continuamente até atingir o limite orçamentário previsto para o projeto.
* **C)** o gráfico de *Release Burnup* restringe-se a exibir a quantidade de impedimentos resolvidos, sendo incapaz de sinalizar expansões ou reduções no escopo global do projeto.
* **D)** no gráfico de *Sprint Burndown*, se a linha real mantiver trajetória acima da linha ideal planejada, conclui-se que o ritmo de entrega está superando as estimativas iniciais de vazão da equipe.
* **E)** o gráfico de *Release Burnup* monitora exclusivamente a performance computacional dos servidores de integração contínua durante a compilação do código.


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** No gráfico de **Burndown**, o objetivo é "queimar" o trabalho restante em direção a zero. O eixo vertical expressa o esforço restante (em pontos de história ou horas) e o horizontal expressa os dias da Sprint. Caso a linha de execução real esteja **abaixo da linha ideal guia**, resta menos trabalho do que o originalmente estimado para aquele dia, indicando que o time está **adiantado**.
> - **B) Incorreta.** O Burndown é descendente (mede trabalho restante decrescendo até zero); o gráfico que acumula entregas para cima de forma ascendente é o *Burnup*.
> - **C) Incorreta.** Uma das grandes vantagens analíticas do *Release Burnup* sobre o Burndown é justamente possuir duas linhas distintas (uma de escopo total e outra de trabalho realizado), tornando imediatamente transparentes acréscimos ou cortes de escopo ao longo da iteração.
> - **D) Incorreta.** Linha real acima da linha ideal em um Burndown indica atraso (resta mais trabalho pendente do que o previsto para aquele momento).
> - **E) Incorreta.** O Burnup é um gráfico de acompanhamento de entrega de escopo de negócio por iteração, não uma métrica de telemetria de infraestrutura.
>
> **Gabarito: A**'''

rewrites['Teste 009'] = '''### Teste 009
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
Ao auditar o fluxo contínuo de trabalho e os processos operacionais de desenvolvimento de uma entidade pública orientados pelo método Kanban, o auditor de controle externo verificou a instituição de limites explícitos de Trabalho em Progresso (*Work In Progress* - WIP) nas colunas do quadro. Na teoria e na prática do Kanban, o objetivo técnico central dessa restrição é:

* **A)** expor gargalos e bloqueios no fluxo operacional, reduzindo o tempo de ciclo total (*Cycle Time*) e prevenindo o desperdício decorrente da troca constante de contexto (*multitasking*).
* **B)** compelir os desenvolvedores a cumprirem horas extraordinárias sempre que o número de tarefas ultrapassar o limite pré-fixado na coluna.
* **C)** exigir a homologação formal de cada item por um comitê diretivo antes de autorizar sua passagem para a coluna seguinte.
* **D)** dispensar a execução de testes funcionais automatizados para acelerar a taxa de liberação de pacotes em produção.
* **E)** padronizar compulsoriamente para um tamanho idêntico o esforço e a complexidade de todas as demandas recebidas no fluxo.


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** O princípio orientador do método Kanban sintetiza-se no lema *"pare de começar e comece a terminar"*. A fixação de limites explícitos de WIP restringe o volume de tarefas concorrentes em cada etapa, expõe gargalos operacionais (impedindo que etapas a montante sobrecarreguem etapas a jusante), minimiza a perda de produtividade por troca de contexto e, por consequência direta da **Lei de Little** ($Lead\ Time = WIP / Throughput$), diminui o tempo de ciclo de entrega.
> - **B) Incorreta.** O limite de WIP busca promover ritmo sustentável e balanceamento de capacidade, e não impor sobrecarga ou horas extras artificiais.
> - **C) Incorreta.** Falsa burocracia: a transição entre colunas é orientada por políticas explícitas da equipe (*Definition of Workflow*), e não por atos comitiais formais.
> - **D) Incorreta.** A limitação de WIP foca na elevação da qualidade das entregas, não admitindo a supressão de testes ou controles de engenharia.
> - **E) Incorreta.** O Kanban lida pragmaticamente com itens de tamanhos e naturezas heterogêneas; o limite incide sobre a contagem simultânea de itens na raia/coluna, e não sobre o tamanho fixo da demanda.
>
> **Gabarito: A**'''

rewrites['Teste 010'] = '''### Teste 010
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
No âmbito da governança e gestão quantitativa de demandas de TI com o método Kanban, duas métricas temporais essenciais para diagnosticar a eficiência e a previsibilidade das entregas aos usuários são o *Lead Time* e o *Cycle Time*. A correta distinção conceitual entre essas grandezas estabelece que:

* **A)** o *Lead Time* compreende o tempo total decorrido desde a solicitação ou registro formal da demanda pelo usuário até sua entrega final em produção, ao passo que o *Cycle Time* mensura o intervalo em que a equipe esteve efetivamente trabalhando no desenvolvimento ativo do item.
* **B)** o *Lead Time* calcula exclusivamente o tempo durante o qual o item permaneceu bloqueado por impedimentos, enquanto o *Cycle Time* afere a duração das reuniões diárias da equipe.
* **C)** o *Cycle Time* abrange desde o momento da idealização pelo cliente até a homologação, enquanto o *Lead Time* tem início apenas com a primeira compilação do código-fonte.
* **D)** o *Lead Time* e o *Cycle Time* são métricas necessariamente coincidentes em qualquer ambiente Kanban que opere com fluxo puxado.
* **E)** o *Throughput* representa a grandeza temporal resultante da subtração matemática do *Cycle Time* pelo *Lead Time*.


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** No método Kanban:
>     - **Lead Time (Tempo de Atendimento):** Representa a perspectiva do **cliente/usuário**. É o tempo total transcorrido desde o registro formal da necessidade no sistema de chamados/backlog até a entrega do item pronto para uso em produção (engloba tempo de espera em fila + tempo de trabalho ativo);
>     - **Cycle Time (Tempo de Ciclo):** Representa a perspectiva da **equipe técnica**. É o intervalo transcorrido a partir do momento em que o item é puxado para o fluxo de execução ativa ("Em Andamento") até a sua conclusão.
> - **B) Incorreta.** Mistura tempos de fluxo com tempos de bloqueio e cerimônias ágeis.
> - **C) Incorreta.** Inverte diametralmente as definições consagradas das métricas.
> - **D) Incorreta.** São métricas distintas; o Lead Time sempre engloba o tempo de espera nas filas prévias de compromisso, sendo tipicamente superior ao Cycle Time.
> - **E) Incorreta.** *Throughput* (vazão) é uma métrica quantitativa (número de itens concluídos por unidade de tempo, ex.: 15 itens/semana), não o resultado de subtração de tempos.
>
> **Gabarito: A**'''

rewrites['Teste 011'] = '''### Teste 011
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
Em uma fiscalização de contratos de fábrica de software de um órgão público, o Auditor de Controle Externo analisou as práticas de engenharia de software preconizadas no Termo de Referência. Entre as práticas exigidas contratualmente, constavam a Programação em Par (*Pair Programming* — dois programadores atuando conjuntamente em uma mesma estação, com papéis de piloto e copiloto), o Desenvolvimento Orientado por Testes (*Test-Driven Development* - TDD, no ciclo Red-Green-Refactor) e a Refatoração Contínua. No rol das metodologias e frameworks ágeis, essas práticas de codificação são originárias e consagradas primariamente pelo:

* **A)** Extreme Programming (XP).
* **B)** Scrum.
* **C)** Rational Unified Process (RUP).
* **D)** Método em Cascata (*Waterfall*).
* **E)** CMMI Nível 5.


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** O **Extreme Programming (XP)**, formulado por Kent Beck, é a metodologia ágil estritamente focada em **excelência técnica de engenharia e programação**. É a fonte de práticas consagradas como *Pair Programming* (dois desenvolvedores compartilhando teclado/tela), *TDD* (escrever o teste unitário antes do código de produção), *Refactoring* sistemático, integração contínua, metáfora do sistema e propriedade coletiva do código.
> - **B) Incorreta.** O Scrum é um framework holístico de gestão e desenvolvimento de produtos centrado em papéis, eventos e artefatos, não prescrevendo práticas técnicas específicas de codificação como pair programming ou TDD.
> - **C) Incorreta.** O RUP é um processo pesado e prescritivo com 4 fases formais e modelagem intensiva em UML, não tendo como pilares mandatórios o TDD ou o pareamento.
> - **D) Incorreta.** O modelo em Cascata segrega estritamente as fases de especificação, codificação e testes, colidindo com a dinâmica contínua do TDD e da programação em pares.
> - **E) Incorreta.** O CMMI é um modelo conceitual corporativo de avaliação de maturidade e capacidade de processos, não uma metodologia de codificação ágil.
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

print('Arquivo 01_ciclo_de_vida_e_metodologias_ageis.md atualizado com sucesso!')

