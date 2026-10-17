# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from enricher_base import inject_questions_into_file

# ==========================================
# FILE 1: 01_ciclo_de_vida_e_metodologias_ageis.md
# ==========================================
file_1 = "fontes_de_estudo/conhecimentos_especificos_b02_ti/04_engenharia_de_software/01_ciclo_de_vida_e_metodologias_ageis.md"
injections_1 = [
    {
        "target_sec": "### 1.3 Modelos de Maturidade de Processo (CMMI e MPS.BR)",
        "question_text": """### Questão 06
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
No âmbito dos modelos de qualidade e melhoria de processos de software, o CMMI (Capability Maturity Model Integration) e o MPS.BR (Melhoria de Processo do Software Brasileiro) apresentam estruturas formais de avaliação. A respeito das características comparativas entre ambos, é correto afirmar que:

* **A)** o MPS.BR estabelece 5 níveis de maturidade organizados alfabeticamente de A a E, enquanto o CMMI possui 7 níveis de maturidade.
* **B)** no CMMI em sua representação por estágios, a organização atinge níveis de maturidade numerados de 1 a 5, ao passo que o modelo de maturidade do MPS.BR possui 7 níveis de maturidade denominados de G (mais básico) a A (mais avançado/otimizado).
* **C)** o CMMI não contempla representação contínua por níveis de capacidade, restringindo-se estritamente à avaliação por estágios organizacionais.
* **D)** o MPS.BR é incompatível com as normas internacionais ISO/IEC 12207 e ISO/IEC 15504, tendo sido criado para substituir integralmente esses referenciais no Brasil.
* **E)** ambos os modelos exigem que a organização abandone práticas ágeis como Scrum e XP para obter a certificação no nível mais alto de maturidade.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** O MPS.BR possui 7 níveis de maturidade (de G até A), e o CMMI possui 5 níveis de maturidade na representação por estágios (1 a 5).
> - **B) Correta.** Exatamente a distinção cobrada pela FCC: CMMI por estágios vai do nível 1 (Inicial) ao 5 (Otimizado), enquanto o MPS.BR estrutura-se em 7 níveis: G (Parcialmente Gerenciado), F (Gerenciado), E (Parcialmente Definido), D (Definido), C (Totalmente Definido), B (Gerenciado Quantitativamente) e A (Em Otimização).
> - **C) Incorreta.** O CMMI oferece duas representações: por Estágios (níveis de maturidade de 1 a 5) e Contínua (níveis de capacidade de 0 a 3 nas áreas de processo).
> - **D) Incorreta.** O MPS.BR foi desenvolvido expressamente em conformidade com as normas ISO/IEC 12207 e ISO/IEC 15504 (SPICE) / ISO/IEC 33000.
> - **E) Incorreta.** Nenhum dos modelos proíbe metodologias ágeis; ao contrário, versões recentes do CMMI e do MPS.BR incorporam formalmente práticas ágeis.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 2.2 Abordagem Iterativa e Incremental: Modelo Espiral e RUP",
        "question_text": """### Questão 07
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
O Processo Unificado (*Rational Unified Process* - RUP) é um modelo de ciclo de vida de software iterativo e incremental estruturado em quatro fases sequenciais ao longo do tempo. A fase do RUP cuja meta precípua é estabelecer uma arquitetura executável estável, mitigar os riscos técnicos mais severos e validar a viabilidade da solução técnica é a fase de:

* **A)** Iniciação (*Inception*).
* **B)** Elaboração (*Elaboration*).
* **C)** Construção (*Construction*).
* **D)** Transição (*Transition*).
* **E)** Homologação (*Acceptance*).

> **Comentário Detalhado:**
>
> - **A) Incorreta.** A Iniciação foca no escopo do negócio, estimativas macro de viabilidade e limites do sistema.
> - **B) Correta.** A fase de Elaboração tem como objetivo central detalhar os requisitos, mitigar os maiores riscos arquiteturais e estabelecer uma baseline arquitetural executável estável.
> - **C) Incorreta.** A Construção foca no desenvolvimento em larga escala de todos os componentes e funcionalidades restantes.
> - **D) Incorreta.** A Transição foca na implantação, entrega aos usuários, correção de defeitos em produção e treinamento.
> - **E) Incorreta.** Homologação não é uma das quatro fases canônicas do RUP.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 2.3 Abordagem Adaptativa / Ágil: O Manifesto Ágil de 2001",
        "question_text": """### Questão 08
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
O Manifesto para o Desenvolvimento Ágil de Software, firmado em 2001, estabeleceu 4 valores fundamentais e 12 princípios norteadores. Entre os 12 princípios formais expressos no documento oficial, encontra-se:

* **A)** Aceitar mudanças de requisitos, mesmo em fases tardias do desenvolvimento, pois processos ágeis tiram vantagem das mudanças em benefício da vantagem competitiva do cliente.
* **B)** Priorizar a documentação técnica exaustiva antes do início de qualquer codificação, garantindo a rastreabilidade contratual.
* **C)** Realizar entregas de software funcional apenas ao final do contrato, assegurando que o produto seja entregue sem pendências aos usuários.
* **D)** Proibir a alteração de requisitos após a homologação da arquitetura básica pelo cliente.
* **E)** Concentrar a comunicação exclusivamente por meio de relatórios formais de status report escritos pela gerência.

> **Comentário Detalhado:**
>
> - **A) Correta.** É a literalidade do segundo princípio do Manifesto Ágil: "Aceitar mudanças de requisitos, mesmo no fim do desenvolvimento. Processos ágeis se adequam a mudanças, para que o cliente possa tirar vantagens competitivas".
> - **B) Incorreta.** O Manifesto valoriza software em funcionamento mais do que documentação abrangente.
> - **C) Incorreta.** O princípio ágil preconiza "entregar software funcionando com frequência, na escala de semanas a meses, com preferência aos períodos mais curtos".
> - **D) Incorreta.** A adaptabilidade é a espinha dorsal do desenvolvimento ágil; mudanças são bem-vindas.
> - **E) Incorreta.** O método mais eficiente e eficaz de transmitir informações para e dentro de uma equipe de desenvolvimento é a conversa face a face.
>
> **Gabarito: A**"""
    },
    {
        "target_sec": "### 3.2 Estrutura do Scrum Team e Responsabilidades",
        "question_text": """### Questão 09
**(FGV – TJ-RR – Analista Judiciário / Tecnologia da Informação)**  
Em relação às características do Scrum Team estabelecidas no Guia Scrum (versão 2020), analise as afirmativas a seguir:  

I. O Scrum Team é uma unidade coesa de profissionais que engloba um Product Owner, um Scrum Master e os Desenvolvedores, caracterizando-se por ser autogerenciado e multifuncional.  
II. O Product Owner é o único responsável pela gestão do Product Backlog e por maximizar o valor do produto entregue, não havendo subordinação hierárquica entre ele e os demais membros do time.  
III. O Scrum Master é o superior hierárquico do time e detém a prerrogativa formal de atribuir tarefas diárias nominais e individuais aos desenvolvedores.  

Está correto o que se afirma em:

* **A)** I, apenas.
* **B)** III, apenas.
* **C)** I e II, apenas.
* **D)** II e III, apenas.
* **E)** I, II e III.

> **Comentário Detalhado:**
>
> - **I. Correta.** O time Scrum é autogerenciado (decide quem faz o que, quando e como) e multifuncional (possui todas as habilidades para gerar um incremento).
> - **II. Correta.** O PO é o responsável exclusivo pela gestão eficaz do Product Backlog e maximização de valor; não há hierarquia dentro do Scrum Team.
> - **III. Incorreta.** O Scrum Master é um "líder que serve" (*servant leader*), não um gerente tradicional; ele não atribui tarefas nominais e os Desenvolvedores autogerenciam seu trabalho.
>
> **Gabarito: C**"""
    },
    {
        "target_sec": "### 3.5 Métricas e Gráficos de Acompanhamento (Burndown e Burnup)",
        "question_text": """### Questão 10
**(FCC – TCE – Auditor de Controle Externo / Tecnologia da Informação)**  
No acompanhamento visual do progresso de equipes ágeis, dois gráficos amplamente utilizados são o *Sprint Burndown* e o *Release Burnup*. A correta caracterização e interpretação desses gráficos estabelece que:

* **A)** o gráfico de Burndown exibe a quantidade acumulada de funcionalidades já concluídas subindo progressivamente até atingir o teto de escopo planejado.
* **B)** no gráfico de *Sprint Burndown*, o eixo vertical quantifica o trabalho restante a ser concluído e o eixo horizontal representa o tempo; quando a linha real situa-se abaixo da linha ideal planejada, isso indica que a equipe está adiantada em relação ao planejado.
* **C)** o gráfico de *Burnup* mede exclusivamente os impedimentos técnicos do time, não tendo relação com escopo ou entregas de software.
* **D)** no gráfico de Burndown, uma linha real ascendente ou situada acima da linha ideal indica que a equipe está entregando o trabalho mais rapidamente do que o estimado originalmente.
* **E)** o gráfico de Burnup é incapaz de demonstrar alterações de escopo ocorridas durante o projeto, revelando apenas as tarefas finalizadas.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** O Burndown mede o trabalho *restante* ("queimando" para baixo em direção a zero). O gráfico que sobe progressivamente é o *Burnup*.
> - **B) Correta.** No Burndown, o eixo Y mostra o trabalho restante (horas ou story points). Se a linha real está abaixo da linha guia ideal, restam menos tarefas do que o previsto, indicando que a equipe está trabalhando mais rápido/adiantada.
> - **C) Incorreta.** O Burnup rastreia o progresso acumulado em direção à meta e mostra a linha de escopo total.
> - **D) Incorreta.** Se a linha real está acima da linha ideal, resta mais trabalho do que o esperado, denotando atraso ou acréscimo de escopo.
> - **E) Incorreta.** A principal vantagem do Burnup sobre o Burndown é justamente a capacidade de exibir explicitamente a variação da linha de escopo total ao longo do tempo.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 4.2 Limites de Trabalho em Progresso (WIP) e Gargalos",
        "question_text": """### Questão 11
**(FGV – TJ-MT – Analista Judiciário / Tecnologia da Informação)**  
No método Kanban aplicado ao fluxo de desenvolvimento de software, a imposição de limites explícitos de Trabalho em Progresso (*Work in Progress* - WIP) nas colunas do quadro de tarefas tem como objetivo primordial e fundamentação técnica:

* **A)** forçar a equipe a realizar horas extras para desocupar postos de trabalho travados.
* **B)** impedir alterações no código-fonte sem homologação prévia do comitê de governança.
* **C)** evidenciar gargalos e bloqueios no fluxo, reduzindo o tempo de ciclo (*Cycle Time*) e prevenindo o desperdício decorrente da troca constante de contexto, em consonância com a Lei de Little.
* **D)** eliminar a necessidade de testes de integração, transferindo a validação diretamente para o usuário final.
* **E)** nivelar a capacidade produtiva fixando rigidamente o tamanho de todas as tarefas em exatamente um dia de trabalho.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** O Kanban busca ritmo sustentável de trabalho, não exploração com horas extras.
> - **B) Incorreta.** Limites de WIP não atuam como barreiras burocráticas de homologação, mas como restrição de concorrência operacional.
> - **C) Correta.** Segundo a Lei de Little ($Lead\\ Time = WIP / Throughput$), limitar o WIP reduz diretamente o tempo de ciclo total, expõe gargalos operacionais no fluxo e combate o desperdício de *multitasking*.
> - **D) Incorreta.** Limitar o WIP eleva a qualidade e não elimina qualquer etapa de testes.
> - **E) Incorreta.** Os itens no Kanban podem ter tamanhos variáveis; o limite aplica-se à quantidade simultânea de itens na coluna, não ao tamanho da tarefa.
>
> **Gabarito: C**"""
    }
]

# ==========================================
# FILE 2: 02_requisitos_historias_de_usuario_uml_e_bpmn.md
# ==========================================
file_2 = "fontes_de_estudo/conhecimentos_especificos_b02_ti/04_engenharia_de_software/02_requisitos_historias_de_usuario_uml_e_bpmn.md"
injections_2 = [
    {
        "target_sec": "### 1.1 Ciclo de Vida da Engenharia de Requisitos",
        "question_text": """### Questão 06
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
O processo de Engenharia de Requisitos compreende um conjunto de atividades estruturadas destinadas a descobrir, analisar, documentar e manter os requisitos de um sistema de software. A atividade desse processo cuja finalidade precípua é demonstrar formalmente que a especificação de requisitos define com precisão o sistema que os clientes realmente desejam e necessitam, identificando ambiguidades, omissões e inconsistências antes da codificação, denomina-se:

* **A)** Elicitação de requisitos.
* **B)** Validação de requisitos.
* **C)** Rastreabilidade de requisitos.
* **D)** Gerenciamento de mudanças.
* **E)** Modelagem de domínio.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** A Elicitação é a atividade inicial de descoberta e levantamento dos requisitos junto aos stakeholders.
> - **B) Correta.** A Validação de Requisitos verifica se o documento de especificação reflete as reais necessidades dos clientes e usuários (*construir o sistema certo*), detectando erros, omissões e conflitos antes do desenvolvimento.
> - **C) Incorreta.** A Rastreabilidade mantém os vínculos históricos entre requisitos, código, testes e artefatos de negócio.
> - **D) Incorreta.** O Gerenciamento de Mudanças lida com o controle e impacto das solicitações de alteração ao longo do ciclo de vida.
> - **E) Incorreta.** A Modelagem de Domínio foca na representação das entidades conceituais e regras do negócio.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 1.3 Requisitos Funcionais vs. Requisitos Não Funcionais (Taxonomia de Sommerville)",
        "question_text": """### Questão 07
**(FCC – SEFAZ – Auditor Fiscal da Receita Estadual)**  
Na especificação de requisitos de software segundo a taxonomia clássica de Ian Sommerville, os requisitos são categorizados em Requisitos Funcionais (RF) e Requisitos Não Funcionais (RNF). Considere os seguintes requisitos elicitados para um sistema corporativo:  

I. O sistema deve emitir o relatório de arrecadação diária consolidado por região fiscal às 18h de cada dia útil.  
II. A comunicação entre o cliente web e a API de backend deve utilizar criptografia TLS versão 1.3 com certificados digitais padrão ICP-Brasil.  
III. O tempo de resposta para a consulta de certidões fiscais não deve exceder 2 segundos para 95% das requisições sob carga de 1.000 usuários simultâneos.  

A correta classificação dos itens I, II e III é, respectivamente:

* **A)** RF, RF e RNF.
* **B)** RNF, RF e RNF.
* **C)** RF, RNF e RNF.
* **D)** RNF, RNF e RF.
* **E)** RF, RNF e RF.

> **Comentário Detalhado:**
>
> - **I. Requisito Funcional (RF):** Descreve uma função/serviço que o sistema deve executar (emitir relatório específico em determinado horário).
> - **II. Requisito Não Funcional (RNF):** Estabelece uma restrição técnica de segurança e protocolo de comunicação (segurança / conformidade).
> - **III. Requisito Não Funcional (RNF):** Trata-se de uma restrição e atributo de qualidade relativo ao desempenho/tempo de resposta e escalabilidade sob carga.
>
> **Gabarito: C**"""
    },
    {
        "target_sec": "### 2.2 Histórias de Usuário (User Stories) e os 3 Cs de Ron Jeffries",
        "question_text": """### Questão 08
**(FCC – DPE – Analista de Sistemas)**  
No contexto do desenvolvimento ágil, Ron Jeffries sintetizou os componentes essenciais de uma História de Usuário (*User Story*) por meio da abordagem dos "Três Cs": *Card*, *Conversation* e *Confirmation*. O papel correspondente ao "Confirmation" estabelece que:

* **A)** o gerente de projetos deve assinar formalmente uma ordem de serviço em cartório antes do início do Sprint.
* **B)** a História de Usuário deve conter critérios de aceite explícitos e verificáveis que permitam ao Product Owner e ao time comprovar que a funcionalidade foi entregue conforme o esperado.
* **C)** deve ser realizada uma reunião de confirmação diária de 2 horas entre todos os diretores da organização.
* **D)** a história deve ser impressa em três cartões coloridos fixados no quadro Kanban.
* **E)** o código-fonte deve ser compilado e confirmado em três ambientes de nuvem distintos antes do commit.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** Prática burocrática alheia ao desenvolvimento ágil.
> - **B) Correta.** O "Confirmation" (Confirmação) representa os critérios de aceite (*acceptance criteria*) que formalizam os testes e condições que devem ser satisfeitos para que a história seja considerada aceita pelo Product Owner.
> - **C) Incorreta.** Não existe tal reunião de 2 horas na definição dos Três Cs.
> - **D) Incorreta.** O "Card" (Cartão) é apenas o suporte inicial resumido da história; o "Confirmation" não é a impressão física de três cartões.
> - **E) Incorreta.** Descrição técnica desprovida de conexão com o framework de histórias de usuário de Jeffries.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 3.1 Taxonomia dos Diagramas UML: Estruturais vs. Comportamentais",
        "question_text": """### Questão 09
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
A linguagem UML (Unified Modeling Language, versão 2.5) define 14 diagramas oficiais divididos em duas grandes categorias: Diagramas Estruturais e Diagramas Comportamentais (com o subgrupo de Interação). Dentre os diagramas listados a seguir, pertencem exclusivamente à categoria dos **Diagramas Estruturais**:

* **A)** Diagrama de Classes, Diagrama de Sequência e Diagrama de Atividades.
* **B)** Diagrama de Casos de Uso, Diagrama de Máquina de Estados e Diagrama de Comunicação.
* **C)** Diagrama de Classes, Diagrama de Componentes e Diagrama de Implantação (*Deployment Diagram*).
* **D)** Diagrama de Objetos, Diagrama de Atividades e Diagrama de Pacotes.
* **E)** Diagrama de Sequência, Diagrama de Interação Geral e Diagrama de Tempo.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** Sequência e Atividades são comportamentais.
> - **B) Incorreta.** Todos os três listados são comportamentais.
> - **C) Correta.** Classes, Componentes e Implantação (*Deployment*) são todos diagramas estáticos/estruturais da UML 2.5.
> - **D) Incorreta.** O Diagrama de Atividades é comportamental.
> - **E) Incorreta.** São diagramas de interação, que constituem uma subclasse dos comportamentais.
>
> **Gabarito: C**"""
    },
    {
        "target_sec": "### 3.3 Diagramas de Sequência, Atividades e Máquina de Estados",
        "question_text": """### Questão 10
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
No Diagrama de Sequência da UML 2.5, utilizado para modelar a dinâmica de interação temporal entre objetos, a notação gráfica para representar uma mensagem assíncrona (na qual o remetente envia o estímulo e prossegue imediatamente com seu processamento sem aguardar a conclusão do receptor) é:

* **A)** Uma linha contínua com uma seta preenchida sólida ($\blacktriangleright$).
* **B)** Uma linha contínua terminada por uma seta aberta em forma de ponta de flecha ($\rightarrow$).
* **C)** Uma linha tracejada terminada por um círculo preenchido.
* **D)** Um losango preenchido na extremidade do emissor.
* **E)** Uma linha dupla contínua sem extremidades direcionais.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** A seta preenchida e sólida com linha contínua representa uma chamada de procedimento síncrona (*synchronous call*).
> - **B) Correta.** Mensagens assíncronas (*asynchronous signals/messages*) são representadas na UML por uma linha contínua finalizada por uma seta aberta em forma de ponta de flecha ($\rightarrow$).
> - **C) Incorreta.** Linha tracejada com seta aberta representa mensagens de retorno (*reply/return messages*).
> - **D) Incorreta.** O losango preenchido denota composição no Diagrama de Classes.
> - **E) Incorreta.** Inexiste essa notação para mensagens em diagramas de sequência UML.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 4.1 Elementos de Fluxo: Eventos, Atividades e Tipos de Tarefas",
        "question_text": """### Questão 11
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
Na notação BPMN 2.0 (*Business Process Model and Notation*), as tarefas são atividades atômicas que compõem o fluxo do processo. A tarefa que representa um trabalho executado por um serviço automatizado (como um Web Service, API externa ou rotina de backend) sem qualquer intervenção humana direta é denominada:

* **A)** *User Task* (Tarefa de Usuário).
* **B)** *Manual Task* (Tarefa Manual).
* **C)** *Service Task* (Tarefa de Serviço).
* **D)** *Business Rule Task* (Tarefa de Regra de Negócio).
* **E)** *Script Task* (Tarefa de Script executada pelo próprio motor BPMN).

> **Comentário Detalhado:**
>
> - **A) Incorreta.** A *User Task* é realizada por um ser humano com o auxílio de uma interface de software.
> - **B) Incorreta.** A *Manual Task* é executada fisicamente por um ser humano sem assistência de qualquer sistema ou motor de processo.
> - **C) Correta.** A *Service Task* (representada pelo ícone de engrenagens no canto superior esquerdo da atividade) representa a invocação de um serviço externo automatizado, como uma chamada de API REST ou Web Service SOAP.
> - **D) Incorreta.** A *Business Rule Task* é específica para execução de regras corporativas via motor de decisão (DMN/BRMS).
> - **E) Incorreta.** A *Script Task* executa scripts diretamente interpretados pelo próprio motor BPMN, diferindo da invocação de serviços externos via *Service Task*.
>
> **Gabarito: C**"""
    }
]

# ==========================================
# FILE 3: 03_arquitetura_de_software_e_principios_solid.md
# ==========================================
file_3 = "fontes_de_estudo/conhecimentos_especificos_b02_ti/04_engenharia_de_software/03_arquitetura_de_software_e_principios_solid.md"
injections_3 = [
    {
        "target_sec": "### 1.2 O Modelo 4+1 Visões de Philippe Kruchten",
        "question_text": """### Questão 06
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
O modelo arquitetural "4+1 Visões", concebido por Philippe Kruchten, organiza a descrição de uma arquitetura de software sob diferentes perspectivas de múltiplos *stakeholders*. A visão do modelo que se destina primordialmente aos programadores e gerentes de software, descrevendo a organização estática do código-fonte em módulos, pacotes, camadas e subsistemas, denomina-se Visão:

* **A)** Lógica (*Logical View*).
* **B)** de Processo (*Process View*).
* **C)** de Desenvolvimento ou de Implementação (*Development/Implementation View*).
* **D)** Física ou de Implantação (*Physical/Deployment View*).
* **E)** de Casos de Uso ou Cenários (*Scenarios / +1 View*).

> **Comentário Detalhado:**
>
> - **A) Incorreta.** A Visão Lógica descreve a modelagem orientada a objetos (classes e entidades de negócio) sob a perspectiva dos analistas e usuários finais.
> - **B) Incorreta.** A Visão de Processo foca no comportamento dinâmico, concorrência, threads e desempenho.
> - **C) Correta.** A Visão de Desenvolvimento (ou de Implementação) concentra-se na organização estrutural do código-fonte, módulos, bibliotecas e pacotes de software gerenciados no ambiente de desenvolvimento.
> - **D) Incorreta.** A Visão Física (ou de Implantação) descreve o mapeamento dos componentes sobre a topologia de hardware e nós de rede.
> - **E) Incorreta.** Os Cenários (+1) integram e validam as quatro visões anteriores a partir dos casos de uso críticos do negócio.
>
> **Gabarito: C**"""
    },
    {
        "target_sec": "### 1.3 Coesão e Acoplamento: A Busca pela Alta Coesão e Baixo Acoplamento",
        "question_text": """### Questão 07
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
Na engenharia de software modular e orientada a objetos, dois conceitos fundamentais que determinam a manutenibilidade, testabilidade e elegância do código são a Coesão e o Acoplamento. A respeito desses conceitos, assinale a afirmativa tecnicamente correta:

* **A)** O projeto ideal busca módulos com baixo acoplamento e baixa coesão, para que cada classe compartilhe o maior número possível de variáveis globais.
* **B)** A alta coesão indica que os elementos e responsabilidades de um mesmo módulo estão intimamente relacionados a um único propósito conceitual claro e bem delimitado.
* **C)** O acoplamento mede a força de relacionamento interno entre as linhas de código de uma mesma função privada.
* **D)** O alto acoplamento é altamente recomendável em sistemas críticos, pois assegura que qualquer alteração em um módulo propague seus efeitos diretamente em todos os demais componentes.
* **E)** Módulos altamente coesos dependem obrigatoriamente de conexões diretas com detalhes de implementação do banco de dados relacional.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** A meta de design de software é sempre **Alta Coesão e Baixo Acoplamento**; variáveis globais elevam perigosamente o acoplamento.
> - **B) Correta.** Alta coesão significa que os métodos e atributos de um componente convergem para uma responsabilidade única e coesa, facilitando manutenção e reuso.
> - **C) Incorreta.** A força interna dos elementos do mesmo módulo é a *coesão*; o *acoplamento* mede a dependência externa entre módulos distintos.
> - **D) Incorreta.** O alto acoplamento gera código frágil e rígido (*efeito cascata* de quebras diante de mudanças).
> - **E) Incorreta.** Módulos coesos seguem a inversão de dependência e devem desacoplar-se de detalhes de infraestrutura e persistência.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 2.1 Arquitetura em Camadas (Layered / N-Tier Architecture) e Variações Hexagonais",
        "question_text": """### Questão 08
**(FCC – TCE – Auditor de Controle Externo / Tecnologia da Informação)**  
A Arquitetura Hexagonal (*Ports and Adapters*), idealizada por Alistair Cockburn, consolidou-se como um dos padrões arquiteturais fundamentais para sistemas modernos que buscam isolar as regras de negócio de frameworks e detalhes tecnológicos externos. Em relação a essa arquitetura, é correto afirmar que:

* **A)** as regras de negócio residem no centro do hexágono e comunicam-se com o mundo externo exclusivamente por meio de Portas (*Ports* - interfaces abstratas), cujas implementações concretas são fornecidas pelos Adaptadores (*Adapters*).
* **B)** o banco de dados e a interface gráfica do usuário devem obrigatoriamente ser acoplados diretamente ao domínio central do sistema.
* **C)** o padrão proíbe o uso de testes unitários automatizados no domínio interno sem a presença de um servidor de aplicação web ativo.
* **D)** a arquitetura hexagonal exige a utilização de seis camadas físicas de hardware redundantes para operar em produção.
* **E)** portas e adaptadores só podem ser implementados se a aplicação utilizar banco de dados relacional baseado em linguagem SQL padrão ANSI.

> **Comentário Detalhado:**
>
> - **A) Correta.** No padrão Ports and Adapters, a lógica de domínio reside no núcleo isolado; ela define *Portas* (interfaces de entrada/saída) e o mundo externo (REST, filas, bancos, CLI) conecta-se a essas portas através de *Adaptadores*.
> - **B) Incorreta.** O princípio central da arquitetura hexagonal é justamente desacoplar o banco de dados e a UI da lógica de negócio.
> - **C) Incorreta.** A maior vantagem da arquitetura hexagonal é permitir testar 100% da lógica de negócio em isolamento absoluto, sem necessidade de banco, web ou infraestrutura externa.
> - **D) Incorreta.** O nome "hexagonal" é meramente uma metáfora visual gráfica; não se refere a nós de hardware.
> - **E) Incorreta.** A arquitetura é agnóstica em relação a mecanismos de persistência (relacional, NoSQL, arquivos em memória, etc.).
>
> **Gabarito: A**"""
    },
    {
        "target_sec": "### 2.2 Arquitetura Orientada a Serviços (SOA) e o Papel do Barramento Corporativo (ESB)",
        "question_text": """### Questão 09
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
No modelo de Arquitetura Orientada a Serviços (SOA), o Barramento Corporativo de Serviços (*Enterprise Service Bus* - ESB) desempenha um papel de integração centralizada na infraestrutura organizacional. Dentre as responsabilidades e capacidades fundamentais desempenhadas por um ESB clássico, destaca-se:

* **A)** A compilação em tempo de execução de todo o código-fonte Java e Python existente nos clientes web.
* **B)** O roteamento inteligente de mensagens, a transformação entre formatos e protocolos de comunicação heterogêneos e a mediação de serviços corporativos.
* **C)** A substituição permanente de qualquer banco de dados relacional pelo armazenamento de dados diretamente no buffer da memória RAM do barramento.
* **D)** A imposição de que todos os serviços legados da empresa sejam reescritos obrigatoriamente na mesma linguagem de programação.
* **E)** A execução de algoritmos de inteligência artificial generativa para criação autônoma de novos produtos bancários.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** O ESB não é compilador de linguagens.
> - **B) Correta.** As funções essenciais do ESB são roteamento, mediação, mensageria, segurança e transformação de formatos e protocolos (por exemplo, converter chamadas SOAP/XML em REST/JSON ou conectores JMS).
> - **C) Incorreta.** O ESB é uma plataforma de transporte e integração de mensagens, não um banco de dados transacional substituto.
> - **D) Incorreta.** SOA e ESB promovem a interoperabilidade entre linguagens e plataformas heterogêneas, sem exigir reescrita na mesma linguagem.
> - **E) Incorreta.** Atividade fictícia e alheia ao escopo clássico de integração via ESB.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 2.4 Arquitetura Orientada a Eventos (EDA - Event-Driven Architecture)",
        "question_text": """### Questão 10
**(FGV – TJ – Analista Judiciário / Tecnologia da Informação)**  
A Arquitetura Orientada a Eventos (*Event-Driven Architecture* - EDA) é caracterizada pela comunicação assíncrona desacoplada baseada na produção, detecção e consumo de eventos de negócio. Nesse paradigma, quando associado ao padrão CQRS (*Command Query Responsibility Segregation*), tem-se que:

* **A)** as operações de alteração de estado (*Commands*) e as operações de consulta (*Queries*) utilizam modelos conceituais distintos, permitindo otimizar a escrita e a leitura de forma independente.
* **B)** toda e qualquer requisição de leitura deve travar o banco de dados em modo monousuário até que as mensagens pendentes na fila sejam totalmente apagadas.
* **C)** os produtores de eventos precisam conhecer o endereço de rede IP e a tecnologia interna de cada um dos consumidores para que o evento seja entregue.
* **D)** o padrão exige o descarte de mecanismos de mensageria assíncrona em favor de chamadas HTTP síncronas bloqueantes ponto a ponto.
* **E)** as consultas nunca podem retornar dados desatualizados, mesmo que o sistema utilize consistência eventual (*eventual consistency*).

> **Comentário Detalhado:**
>
> - **A) Correta.** O CQRS separa formalmente as operações de escrita (*Commands*, que modificam o estado) das operações de leitura (*Queries*, que apenas consultam dados), permitindo que cada lado tenha esquemas de dados e estratégias de escalabilidade customizadas.
> - **B) Incorreta.** EDA e CQRS promovem concorrência de alto desempenho e assincronismo, jamais travamento monousuário.
> - **C) Incorreta.** Em EDA, o produtor emite o evento para um broker de mensageria sem conhecer a identidade ou localização dos consumidores (desacoplamento espacial).
> - **D) Incorreta.** EDA fundamenta-se primordialmente em brokers de mensageria assíncrona (como Kafka e RabbitMQ), e não em HTTP síncrono bloqueante.
> - **E) Incorreta.** Em sistemas distribuídos com CQRS e projeções assíncronas, o modelo de leitura opera frequentemente sob consistência eventual.
>
> **Gabarito: A**"""
    }
]

# ==========================================
# FILE 4: 04_padroes_de_projeto_design_patterns.md
# ==========================================
file_4 = "fontes_de_estudo/conhecimentos_especificos_b02_ti/04_engenharia_de_software/04_padroes_de_projeto_design_patterns.md"
injections_4 = [
    {
        "target_sec": "### 1.3 A Matriz Canônica dos 23 Padrões GoF (Propósito vs. Escopo)",
        "question_text": """### Questão 06
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
O clássico catálogo de padrões de projeto do Gang of Four (GoF) classifica os 23 padrões canônicos sob duas dimensões fundamentais: o **Propósito** (Criacional, Estrutural ou Comportamental) e o **Escopo** (de Classe ou de Objeto). Quanto ao escopo de Classe (no qual os relacionamentos são estáticos e definidos em tempo de compilação principalmente por meio de herança), assinale o padrão de projeto GoF que pertence genuinamente ao escopo de **Classe**:

* **A)** *Abstract Factory*.
* **B)** *Singleton*.
* **C)** *Factory Method*.
* **D)** *Bridge*.
* **E)** *Strategy*.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** *Abstract Factory* tem escopo de Objeto (criação baseada em delegação/composição).
> - **B) Incorreta.** *Singleton* tem escopo de Objeto.
> - **C) Correta.** Na taxonomia formal do GoF, apenas 4 padrões operam sob escopo de **Classe**: *Factory Method* (Criação), *Adapter de Classe* (Estrutural), *Interpreter* (Comportamental) e *Template Method* (Comportamental). Todos os demais operam sob escopo de Objeto.
> - **D) Incorreta.** *Bridge* tem escopo de Objeto.
> - **E) Incorreta.** *Strategy* tem escopo de Objeto.
>
> **Gabarito: C**"""
    },
    {
        "target_sec": "### 2.2 Builder, Prototype e Singleton",
        "question_text": """### Questão 07
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
Considere uma situação em que um sistema corporativo necessita construir objetos complexos formados por múltiplas partes e configurações opcionais. A equipe deseja separar o algoritmo de montagem do objeto final da representação interna das suas partes constituintes, de modo que o mesmo processo de montagem possa criar representações diferentes com composições variadas. O padrão de projeto criacional do GoF que atende especificamente a esse requisito é o:

* **A)** *Prototype*.
* **B)** *Singleton*.
* **C)** *Builder*.
* **D)** *Decorator*.
* **E)** *Proxy*.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** O *Prototype* cria novos objetos clonando instâncias prototípicas existentes.
> - **B) Incorreta.** O *Singleton* assegura a unicidade de uma única instância global.
> - **C) Correta.** O padrão *Builder* tem como intenção explícita "separar a construção de um objeto complexo da sua representação, de modo que o mesmo processo de construção possa criar diferentes representações".
> - **D) Incorreta.** O *Decorator* é um padrão estrutural que adiciona responsabilidades a objetos dinamicamente.
> - **E) Incorreta.** O *Proxy* é um padrão estrutural que atua como substituto para controlar acesso a outro objeto.
>
> **Gabarito: C**"""
    },
    {
        "target_sec": "### 3.2 Composite, Decorator, Flyweight e Proxy",
        "question_text": """### Questão 08
**(FGV – TJ – Analista de Sistemas)**  
Analise os seguintes cenários de engenharia de software envolvendo padrões de projeto estruturais do GoF:  

Cenário 1: Um desenvolvedor necessita estender o comportamento de um objeto específico em tempo de execução, adicionando responsabilidades de forma transparente e flexível, como alternativa preferível à criação de subclasses estáticas por herança.  
Cenário 2: Uma aplicação requer o controle estrito de acesso a um objeto volumoso que demanda alto consumo de memória, instanciando-o apenas no momento exato em que algum cliente invocar sua execução pela primeira vez (*lazy loading*).  

Os padrões de projeto adequados para os Cenários 1 e 2 são, respectivamente:

* **A)** *Facade* e *Bridge*.
* **B)** *Decorator* e *Proxy* Virtual.
* **C)** *Composite* e *Adapter*.
* **D)** *Proxy* e *Decorator*.
* **E)** *Flyweight* e *Singleton*.

> **Comentário Detalhado:**
>
> - **Cenário 1:** O padrão *Decorator* adiciona responsabilidades a um objeto de maneira dinâmica e transparente sem usar herança profunda.
> - **Cenário 2:** O padrão *Proxy* Virtual atua como intermediário/substituto de um objeto real para adiar sua criação cara até o momento de uso (*lazy initialization*).
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 4.3 Command, Chain of Responsibility, Iterator, Mediator, Memento e Visitor",
        "question_text": """### Questão 09
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
No catálogo de padrões comportamentais do GoF, o padrão cuja intenção oficial é "evitar o acoplamento do remetente de uma requisição ao seu destinatário, dando a mais de um objeto a oportunidade de tratar a requisição, encadeando os objetos receptores e passando a requisição ao longo da cadeia até que um deles a trate" denomina-se:

* **A)** *Command*.
* **B)** *Chain of Responsibility*.
* **C)** *Mediator*.
* **D)** *Observer*.
* **E)** *Visitor*.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** O *Command* encapsula uma requisição como um objeto para parametrização e suporte a operações reversíveis (*undo*).
> - **B) Correta.** É a definição canônica e literal do padrão *Chain of Responsibility* do GoF (muito cobrada pela FCC).
> - **C) Incorreta.** O *Mediator* centraliza as interações complexas entre um conjunto de objetos colegas.
> - **D) Incorreta.** O *Observer* define dependência 1-para-muitos entre objetos com notificação automática de mudanças.
> - **E) Incorreta.** O *Visitor* representa uma operação a ser executada nos elementos de uma estrutura de objetos sem alterar suas classes.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 4.3 Command, Chain of Responsibility, Iterator, Mediator, Memento e Visitor",
        "question_text": """### Questão 10
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
O padrão de projeto comportamental GoF que permite capturar e externalizar o estado interno de um objeto, de modo que este possa ser restaurado a esse estado posteriormente, sem que o princípio fundamental de encapsulamento seja violado, é o:

* **A)** *Memento*.
* **B)** *State*.
* **C)** *Template Method*.
* **D)** *Prototype*.
* **E)** *Flyweight*.

> **Comentário Detalhado:**
>
> - **A) Correta.** O padrão *Memento* (composto pelos papéis *Originator*, *Memento* e *Caretaker*) armazena um snapshot do estado interno do objeto para viabilizar restauração (*undo/checkpoint*) preservando o encapsulamento.
> - **B) Incorreta.** O *State* permite a um objeto alterar seu comportamento quando seu estado interno muda.
> - **C) Incorreta.** O *Template Method* define o esqueleto de um algoritmo na superclasse, diferindo passos concretos para subclasses.
> - **D) Incorreta.** O *Prototype* é criacional e clona instâncias inteiras.
> - **E) Incorreta.** O *Flyweight* é estrutural e foca em compartilhamento de objetos de granularidade fina para economizar memória.
>
> **Gabarito: A**"""
    }
]

# ==========================================
# FILE 5: 05_qualidade_testes_refatoracao_e_divida_tecnica.md
# ==========================================
file_5 = "fontes_de_estudo/conhecimentos_especificos_b02_ti/04_engenharia_de_software/05_qualidade_testes_refatoracao_e_divida_tecnica.md"
injections_5 = [
    {
        "target_sec": "### 1.3 Confiabilidade, Disponibilidade e Métricas de Manutenção (MTBF e MTTR)",
        "question_text": """### Questão 06
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
Na avaliação de confiabilidade e disponibilidade de sistemas computacionais em conformidade com as normas de qualidade de software, duas métricas temporais essenciais são o MTBF (*Mean Time Between Failures* - Tempo Médio Entre Falhas) e o MTTR (*Mean Time To Repair* - Tempo Médio Para Reparo). A disponibilidade global do sistema ($D$) é classicamente calculada pela fórmula:

* **A)** $D = \\frac{MTTR}{MTBF + MTTR}$
* **B)** $D = \\frac{MTBF}{MTBF + MTTR}$
* **C)** $D = MTBF - MTTR$
* **D)** $D = \\frac{MTBF \\times MTTR}{100}$
* **E)** $D = \\frac{MTTR}{MTBF}$

> **Comentário Detalhado:**
>
> - **A) Incorreta.** Essa razão representaria a taxa de indisponibilidade fracionária (*unavailability*).
> - **B) Correta.** A Disponibilidade ($A$ ou $D$) é a probabilidade do sistema estar operacional no instante considerado: $D = \\frac{MTBF}{MTBF + MTTR}$.
> - **C) Incorreta.** A disponibilidade é uma razão adimensional (frequentemente expressa em percentual, como 99,99%), não uma subtração temporal.
> - **D) Incorreta.** Fórmula incorreta.
> - **E) Incorreta.** Razão que não expressa a disponibilidade.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 2.1 A Pirâmide de Testes de Mike Cohn",
        "question_text": """### Questão 07
**(FGV – TJ – Analista Judiciário / Tecnologia da Informação)**  
A Pirâmide de Testes, conceito amplamente difundido por Mike Cohn na engenharia de software moderna, define a proporção ideal entre diferentes categorias de testes automatizados em uma suíte de entrega contínua. Em conformidade com esse modelo, tem-se que:

* **A)** a base da pirâmide deve conter o maior volume de testes e ser constituída por Testes de Unidade, caracterizados por alta velocidade de execução, isolamento e baixo custo de manutenção.
* **B)** o topo da pirâmide deve concentrar mais de 80% do esforço de testes na forma de testes ponta a ponta manuais na interface com o usuário.
* **C)** os testes de integração devem ser completamente extintos, visto que os testes de unidade cobrem todas as falhas de comunicação entre microsserviços.
* **D)** o modelo preconiza que suítes de testes automatizados devem assemelhar-se a um "cone de sorvete", priorizando testes de UI em detrimento de testes de baixo nível.
* **E)** os testes de unidade são os mais lentos e custosos da pirâmide devido à obrigatoriedade de instanciar contêineres Docker e bancos de dados em nuvem.

> **Comentário Detalhado:**
>
> - **A) Correta.** A base larga da pirâmide é formada por Testes de Unidade (rápidos, isolados, determinísticos e baratos). Na camada intermediária situam-se os Testes de Integração/Serviço, e no topo reduzido os Testes de Ponta a Ponta / UI.
> - **B) Incorreta.** O topo da pirâmide é pequeno e restrito; testes de UI são caros, lentos e frágeis (*flaky*).
> - **C) Incorreta.** Os testes de integração são indispensáveis para validar contratos, protocolos e comunicação de componentes.
> - **D) Incorreta.** O "cone de sorvete" (*ice cream cone anti-pattern*) é exatamente a anomalia que a Pirâmide de Testes combate.
> - **E) Incorreta.** Testes de unidade operam em memória com dublês de teste, sem rede ou banco real, sendo os mais velozes.
>
> **Gabarito: A**"""
    },
    {
        "target_sec": "### 2.3 Testes de Caixa-Preta (Funcionais) vs. Testes de Caixa-Branca (Estruturais)",
        "question_text": """### Questão 08
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
No âmbito das técnicas de teste funcional de software (Caixa-Preta), o Particionamento em Classes de Equivalência e a Análise de Valor Limite são métodos consagrados para seleção criteriosa de casos de teste. A respeito dessas técnicas, é correto afirmar:

* **A)** O particionamento em classes de equivalência exige que o desenvolvedor inspecione o código-fonte C++ para verificar o número de desvios condicionais `if-else`.
* **B)** A análise de valor limite assume que a probabilidade de ocorrência de erros no software é homogênea em todo o espaço de entrada, dispensando testes nas fronteiras.
* **C)** No particionamento de equivalência, divide-se o domínio de dados de entrada em partições válidas e inválidas, partindo do princípio de que qualquer dado representativo escolhido dentro de uma mesma partição gerará um comportamento análogo pelo sistema.
* **D)** As técnicas de caixa-preta analisam exclusivamente a complexidade ciclomática e a cobertura de comandos do código compilado.
* **E)** A análise de valor limite testa exclusivamente o ponto central aritmético de cada partição, ignorando os extremos superior e inferior.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** Inspecionar desvios e código-fonte é teste de Caixa-Branca (estrutural), não Caixa-Preta.
> - **B) Incorreta.** A análise de valor limite fundamenta-se na premissa comprovada de que a maioria dos erros ocorre justamente nas fronteiras e transições das partições.
> - **C) Correta.** É o princípio exato das classes de equivalência: os valores de uma classe são tratados como equivalentes pelo programa, permitindo testar um único representante por classe.
> - **D) Incorreta.** Complexidade ciclomática e cobertura de comandos são técnicas de Caixa-Branca.
> - **E) Incorreta.** A análise de valor limite testa exatamente os extremos (mínimo, logo abaixo do mínimo, máximo, logo acima do máximo).
>
> **Gabarito: C**"""
    },
    {
        "target_sec": "### 3.3 Práticas de TDD (Test-Driven Development) e BDD (Behavior-Driven Development)",
        "question_text": """### Questão 09
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
O Desenvolvimento Orientado por Testes (*Test-Driven Development* - TDD), preconizado por Kent Beck, estabelece um ciclo disciplinado de desenvolvimento guiado por iterações extremamente curtas, denominado ciclo *Red-Green-Refactor*. A ordem estrita e as ações correspondentes a esse ciclo são:

* **A)** 1. Escrever todo o código de produção funcional (Green); 2. Encontrar erros de compilação (Red); 3. Otimizar o banco de dados (Refactor).
* **B)** 1. Escrever um teste unitário automatizado que falha porque a funcionalidade ainda não existe (Red); 2. Escrever o código mínimo necessário para fazer o teste passar (Green); 3. Melhorar o design e a estrutura interna do código mantendo os testes passando (Refactor).
* **C)** 1. Refatorar o código legado sem testes (Refactor); 2. Executar testes de carga em produção (Green); 3. Corrigir bugs reportados pelos usuários (Red).
* **D)** 1. Gerar relatórios de cobertura SonarQube (Red); 2. Solicitar aprovação gerencial (Green); 3. Comitar na branch master (Refactor).
* **E)** 1. Escrever código e testes simultaneamente na mesma classe (Green); 2. Desabilitar testes que falharem (Refactor); 3. Marcar o build como concluído (Red).

> **Comentário Detalhado:**
>
> - **A) Incorreta.** No TDD o teste é escrito *antes* do código de produção.
> - **B) Correta.** É o mantra oficial do TDD: **Red** (escreva um teste para o novo comportamento e veja-o falhar), **Green** (escreva o código mais simples e rápido que faça o teste passar), e **Refactor** (limpe a duplicação e refine o design com a segurança de que a suíte continua verde).
> - **C) Incorreta.** Inversão completa da metodologia.
> - **D) Incorreta.** TDD é prática de engenharia de software em nível de código, não processo burocrático de aprovação.
> - **E) Incorreta.** Desabilitar testes que falham é um anti-padrão grave.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 4.1 Técnicas Modernas de Revisão de Código (Code Review)",
        "question_text": """### Questão 10
**(FCC – TCE – Auditor de Controle Externo / Tecnologia da Informação)**  
No ciclo de vida de desenvolvimento de software em equipes de alta maturidade, a prática de Revisão de Código (*Code Review*) por meio de *Pull Requests* / *Merge Requests* aliada à Análise Estática Automatizada compõe a primeira linha de defesa da qualidade do software. Em relação a essas práticas, é correto afirmar:

* **A)** A análise estática de código só pode ser executada com o software em pleno funcionamento no ambiente de produção sob tráfego real.
* **B)** As ferramentas de análise estática (como *linters* e analisadores de qualidade) examinam a estrutura do código-fonte sem executá-lo, detectando violações de estilo, vulnerabilidades de segurança conhecidas, duplicações de código e métricas de complexidade ciclomática.
* **C)** A revisão por pares de código deve ser reservada exclusivamente para código desenvolvido por estagiários, devendo o código de desenvolvedores seniores ser enviado direto para produção sem inspeção.
* **D)** O Code Review tem como finalidade primordial medir o tempo gasto por linha de código para fins de aplicação de penalidades trabalhistas.
* **E)** O uso de ferramentas automatizadas de análise de código elimina integralmente a necessidade da revisão humana em Pull Requests.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** A análise estática examina o código sem executá-lo. A análise que roda com a aplicação sob tráfego é a análise dinâmica (DAST / APM).
> - **B) Correta.** Ferramentas de análise estática (ex: SonarQube, ESLint, Checkstyle) inspecionam o código-fonte em repouso (*at rest*), apontando code smells, vulnerabilidades (SAST), duplicações e métricas de manutenibilidade.
> - **C) Incorreta.** Todos os membros da equipe submetem código a review (*peer review* universal para garantia de qualidade e disseminação de conhecimento).
> - **D) Incorreta.** Code review foca na qualidade técnica da solução e na melhoria contínua, jamais em controle punitivo.
> - **E) Incorreta.** Ferramentas automatizadas e revisões humanas são complementares; humanos avaliam arquitetura, legibilidade e intenção de negócio.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 4.3 Dívida Técnica e o Quadrante de Martin Fowler",
        "question_text": """### Questão 11
**(FCC – Inédita – Padrão TCE-GO)**  
O conceito de Dívida Técnica (*Technical Debt*), cunhado originariamente por Ward Cunningham e categorizado no célebre "Quadrante da Dívida Técnica" por Martin Fowler, compara decisões apressadas de desenvolvimento a dívidas financeiras. No quadrante de Fowler, quando uma equipe assume deliberadamente uma solução de arquitetura simplificada e incompleta para atingir um prazo de lançamento crucial do negócio, tendo plena consciência técnica do débito e planejando pagá-lo na Sprint seguinte, essa dívida é classificada como:

* **A)** Imprudente e Inadvertida.
* **B)** Prudente e Deliberada.
* **C)** Imprudente e Deliberada.
* **D)** Prudente e Inadvertida.
* **E)** Acidental e Irreversível.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** "Imprudente e Inadvertida" ocorre quando a equipe não conhece boas práticas de design e escreve código ruim sem saber que o está fazendo.
> - **B) Correta.** No Quadrante da Dívida Técnica de Fowler:
>   - **Prudente e Deliberada:** A equipe sabe o que está fazendo e decide assumir o débito conscientemente ("Temos que lançar agora; pagaremos o débito na próxima Sprint").
>   - **Imprudente e Deliberada:** A equipe decide ignorar boas práticas por pressa negligente ("Não temos tempo para design").
>   - **Prudente e Inadvertida:** A equipe fez o melhor trabalho possível, mas aprendeu uma abordagem melhor com o tempo ("Agora sabemos como deveríamos ter feito").
>   - **Imprudente e Inadvertida:** Falta de competência técnica básica ("O que é arquitetura em camadas?").
> - **C) Incorreta.** "Imprudente e Deliberada" é o atalho negligente.
> - **D) Incorreta.** "Prudente e Inadvertida" decorre do aprendizado natural pós-entrega.
> - **E) Incorreta.** Categorias que não fazem parte do quadrante de Fowler.
>
> **Gabarito: B**"""
    }
]

print("Injecting into Module 04...")
inject_questions_into_file(file_1, injections_1)
inject_questions_into_file(file_2, injections_2)
inject_questions_into_file(file_3, injections_3)
inject_questions_into_file(file_4, injections_4)
inject_questions_into_file(file_5, injections_5)
print("\nModule 04 completed successfully!")
