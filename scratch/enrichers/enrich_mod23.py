# -*- coding: utf-8 -*-
"""
Enriquecedor Módulo 23 - Administração Estratégica
Arquivos: 01, 02, 03
Adiciona de 5 a 6 questões por arquivo (Questões 06 a 10/11) no padrão rigoroso FCC / Anti-spoiler.
"""

import os

BASE_DIR = "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/23_administracao_estrategica"

def enrich_file_01():
    filepath = os.path.join(BASE_DIR, "01_planejamento_estrategico_missao_visao_valores_e_escolas.md")
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    if "### Questão 06" in text:
        print("File 01 already enriched.")
        return

    q06 = """### Questão 06 (FCC - Adaptada / Analista de Planejamento e Gestão)
Na definição da identidade corporativa e do referencial estratégico de um órgão de controle externo, a **Visão de Futuro** diferencia-se da **Missão Institucional** por:

* **A)** Descrever a imagem mental do estado futuro desejado que a instituição almeja alcançar em determinado horizonte temporal (onde queremos chegar), enquanto a Missão define a razão de existir fundamental e o propósito perene de atuação presente do órgão (quem somos e para que servimos).
* **B)** Estabelecer os princípios éticos inegociáveis que regem a conduta disciplinar dos servidores concursados.
* **C)** Consistir em documento sigiloso e restrito à apreciação do Presidente do Tribunal.
* **D)** Ter validade perpétua e imutável que não admite revisão nem mesmo em novos ciclos plurianuais de planejamento.
* **E)** Focar exclusivamente na redução percentual dos gastos de custeio com passagens aéreas e combustíveis.

> **Comentário Detalhado:**
>
> - **A)** Correta. Conceituação clássica: **Missão** é a razão de ser fundamental da instituição, sua vocação e propósito permanente de existir perante a sociedade; **Visão** é o estado futuro almejado, a aspiração ambiciosa de longo prazo, aquilo que a organização pretende ser e como deseja ser reconhecida no futuro.
> - **B)** Incorreta. Refere-se aos **Valores** organizacionais.
> - **C)** Incorreta. A identidade estratégica deve ser amplamente divulgada e compartilhada.
> - **D)** Incorreta. A Visão tem horizonte temporal determinado (ex.: "ser referência nacional até 2030") e é renovada a cada ciclo.
> - **E)** Incorreta. Meta operacional pontual, não visão estratégica.
> 
> **Gabarito: A**

---

"""

    q07 = """### Questão 07 (FCC - Adaptada / Auditor de Controle Externo)
Henry Mintzberg, ao analisar a formação das estratégias organizacionais, contrapôs o modelo puramente racional e deliberado ao surgimento de estratégias não previstas.

Segundo Mintzberg, a **Estratégia Emergente** caracteriza-se por:

* **A)** Surgir a partir de padrões consistentes de ação que emergem espontaneamente ao longo do tempo, em resposta a contingências, oportunidades e desafios imprevistos do ambiente, sem terem sido formalmente intencionadas no plano estratégico original.
* **B)** Ser minuciosamente calculada pela alta administração em planos operacionais plurianuais de dez anos.
* **C)** Exigir autorização prévia em emenda parlamentar na Lei de Diretrizes Orçamentárias.
* **D)** Representar a parte do plano estratégico formal que foi integralmente abandonada e descartada pela equipe (*estratégia não realizada*).
* **E)** Constituir violação do princípio da legalidade administrativa suscetível de anulação sumária.

> **Comentário Detalhado:**
>
> - **A)** Correta. Para Mintzberg, a estratégia realizada é uma combinação de **estratégias deliberadas** (intenções originais que foram formalmente planejadas e executadas) e **estratégias emergentes** (padrões de ação que não foram planejados de antemão, mas surgiram na prática em resposta à dinâmica ambiental e acabaram sendo adotados com sucesso pela organização).
> - **B)** Incorreta. Isso caracteriza a estratégia puramente planejada/deliberada.
> - **C)** Incorreta. Conceito de administração estratégica, não de formalismo financeiro.
> - **D)** Incorreta. O que é descartado chama-se *estratégia não realizada*.
> - **E)** Incorreta. Estratégias emergentes expressam capacidade de adaptação e resiliência.
> 
> **Gabarito: A**

---

"""

    q08 = """### Questão 08 (FCC - Adaptada / Analista de Planejamento e Controle)
Na clássica obra *Safári de Estratégia*, Henry Mintzberg, Bruce Ahlstrand e Joseph Lampel classificam o pensamento estratégico em dez escolas, agrupadas em **Prescritivas** e **Descritivas**.

Constitui uma escola de natureza tipicamente **Prescritiva** (normativa), voltada para prescrever *como a estratégia deve ser idealmente formulada*:

* **A)** A Escola do Planejamento (que concebe a formação estratégica como um processo formal, decomposto em etapas sequenciais analíticas e detalhadas).
* **B)** A Escola do Aprendizado (que vê a estratégia como um processo emergente e contínuo de experimentação).
* **C)** A Escola do Poder (que compreende a estratégia como um processo de negociação e disputas políticas entre grupos).
* **D)** A Escola Cultural (que enxerga a formação da estratégia como um processo coletivo enraizado em valores e crenças).
* **E)** A Escola Ambiental (que trata a estratégia como uma resposta passiva e reativa às pressões ecológicas do contexto externo).

> **Comentário Detalhado:**
>
> - **A)** Correta. As três escolas **Prescritivas** (normativas - como deve ser formulada a estratégia) são: **Design** (estratégia como processo de concepção/ajuste SWOT), **Planejamento** (processo formal e sistemático de passos analíticos) e **Posicionamento** (processo analítico focado na indústria e concorrência - Porter). As demais escolas (Empreendedora, Cognitiva, Aprendizado, Poder, Cultural, Ambiental e Configuração) são **Descritivas** ou Integrativas (focam em como a estratégia realmente se desenvolve na prática).
> - **B), C), D), E)** Incorretas. São todas escolas **Descritivas**.
> 
> **Gabarito: A**

---

"""

    q09_10 = """### Questão 09 (FCC - Adaptada / TCE-PI - Auditor de Controle Externo)
Na elaboração do planejamento estratégico, a formulação dos **Valores Organizacionais** representa:

* **A)** O conjunto de princípios, crenças fundamentais e padrões éticos de conduta compartilhados que orientam as decisões institucionais e definem as relações da organização com seus membros, parceiros e com a sociedade.
* **B)** A estimativa do saldo orçamentário líquido da conta de capital no final de cada quadrimestre fiscal.
* **C)** O cálculo do retorno econômico sobre os investimentos em obras rodoviárias estaduais.
* **D)** A lista taxativa das penalidades disciplinares de demissão constantes do estatuto funcional.
* **E)** O montante financeiro total de multas imputadas aos jurisdicionados pelo Tribunal de Contas.

> **Comentário Detalhado:**
>
> - **A)** Correta. Os **Valores** compõem o núcleo axiológico e ético da cultura organizacional: estabelecem os limites morais, princípios de conduta, responsabilidade socioambiental, transparência e retidão que direcionam o comportamento de todos os integrantes da instituição na busca da missão e visão.
> - **B), C), D), E)** Incorretas. Distorções que confundem "valores" axiológicos/éticos com conceitos puramente financeiros ou punitivos.
> 
> **Gabarito: A**

---

### Questão 10 (FCC - Adaptada / TCE-GO - Analista de Controle Externo)
O ciclo integrado de gestão estratégica nas organizações públicas envolve etapas encadeadas para garantir que as decisões não se restrinjam a documentos formais engavetados.

A etapa do ciclo em que a alta direção e os comitês de governança comparam periodicamente o avanço real dos indicadores frente às metas estipuladas, promovendo os ajustes necessários no plano, denomina-se:

* **A)** Monitoramento e Avaliação Estratégica.
* **B)** Diagnóstico Ambiental Macro.
* **C)** Formulação da Missão Corporativa.
* **D)** Lançamento Tributário Vinculado.
* **E)** Homologação de Parecer Prévio Orçamentário.

> **Comentário Detalhado:**
>
> - **A)** Correta. O ciclo da gestão estratégica compreende: (1) Diagnóstico Estratégico; (2) Formulação da Estratégia (missão, visão, objetivos); (3) Implementação/Execução; e (4) **Monitoramento e Avaliação** (acompanhamento contínuo dos indicadores de desempenho, análise de desvios e adoção de ações corretivas tempestivas).
> - **B), C)** Incorretas. Fases preliminares de diagnóstico e concepção.
> - **D), E)** Incorretas. Atos de direito financeiro e controle externo que não se confundem com as fases do ciclo de gestão estratégica.
> 
> **Gabarito: A**

---

"""

    anchor_2 = "### 2. O Ciclo da Gestão Estratégica Integrada"
    anchor_3 = "### 3. Estratégias Deliberadas vs. Estratégias Emergentes (Henry Mintzberg)"
    anchor_4 = "### 4. As Dez Escolas do Pensamento Estratégico (*Safári de Estratégia*)"
    anchor_fontes = "### 5. Fontes Oficiais e Referências Bibliográficas"

    text = text.replace(anchor_2, q06 + "\n" + anchor_2)
    text = text.replace(anchor_3, q07 + "\n" + anchor_3)
    text = text.replace(anchor_4, q08 + "\n" + anchor_4)
    text = text.replace(anchor_fontes, q09_10 + "\n" + anchor_fontes)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    print("Enriched File 23/01 successfully! Total: 10 questions.")


def enrich_file_02():
    filepath = os.path.join(BASE_DIR, "02_ferramentas_de_diagnostico_estrategico_swot_porter_rbv_canvas.md")
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    if "### Questão 06" in text:
        print("File 02 already enriched.")
        return

    q06 = """### Questão 06 (FCC - Adaptada / Analista de Planejamento e Gestão)
Na Análise SWOT Cruzada (Matriz FOFA), o confronto entre o ambiente interno (Forças e Fraquezas) e o ambiente externo (Oportunidades e Ameaças) permite delinear posturas estratégicas fundamentais para a organização.

A postura estratégica recomendada quando a organização diagnostica um cenário caracterizado predominantemente pelo cruzamento entre **Fraquezas Internas** e **Ameaças Externas** é a postura de:

* **A)** Sobrevivência (ou Defensiva), visando reduzir danos, conter prejuízos e desinvestir em áreas críticas inviabilizadas.
* **B)** Desenvolvimento (ou Alavancagem agressiva), priorizando a expansão maciça de novos serviços e instalações.
* **C)** Domínio Monopolista irrestrito de mercado.
* **D)** Crescimento acelerado por meio de fusões estatais corporativas.
* **E)** Terceirização integral das atividades exclusivas de Estado.

> **Comentário Detalhado:**
>
> - **A)** Correta. As quatro posturas da matriz SWOT cruzada: (1) **Forças + Oportunidades**: Desenvolvimento / Alavancagem; (2) **Forças + Ameaças**: Manutenção / Proteção; (3) **Fraquezas + Oportunidades**: Crescimento / Mudança de Rumo; (4) **Fraquezas + Ameaças**: **Sobrevivência** (situação de vulnerabilidade extrema, exigindo contenção de despesas, enxugamento de custos, alienação de ativos e redução de danos).
> - **B), C), D), E)** Incorretas. Incompatíveis com a combinação de fraquezas e ameaças.
> 
> **Gabarito: A**

---

"""

    q07 = """### Questão 07 (FCC - Adaptada / Auditor de Controle Externo)
Michael Porter formulou o célebre modelo das Cinco Forças Competitivas que determinam a atratividade e o nível de rentabilidade de uma indústria.

São forças competitivas integrantes do modelo original de Porter:

* **A)** Rivalidade entre os concorrentes existentes, Ameaça de novos entrantes, Poder de barganha dos compradores (clientes), Poder de barganha dos fornecedores e Ameaça de produtos ou serviços substitutos.
* **B)** Poder Judiciário, Poder Executivo, Poder Legislativo, Ministério Público e Tribunal de Contas.
* **C)** Gravidade, Urgência, Tendência, Capacidade Operacional e Risco Jurídico.
* **D)** Inflação, Taxa Selic, Produto Interno Bruto, Balança Comercial e Dívida Soberana.
* **E)** Hardware, Software, Peopleware, Sistemas de Redes e Dados na Nuvem.

> **Comentário Detalhado:**
>
> - **A)** Correta. As **Cinco Forças de Porter**: (1) Rivalidade entre concorrentes existentes; (2) Ameaça de novos concorrentes entrantes; (3) Poder de barganha dos clientes/compradores; (4) Poder de barganha dos fornecedores; (5) Ameaça de produtos/serviços substitutos.
> - **B)** Incorreta. Estrutura institucional dos Poderes estatais.
> - **C)** Incorreta. Elementos da Matriz GUT.
> - **D)** Incorreta. Indicadores macroeconômicos do ambiente geral.
> - **E)** Incorreta. Componentes de tecnologia da informação.
> 
> **Gabarito: A**

---

"""

    q08 = """### Questão 08 (FCC - Adaptada / Analista de Tecnologia e Controle)
Na Visão Baseada em Recursos (RBV - *Resource-Based View*) e no framework **VRIO** desenvolvido por Jay Barney, para que um recurso interno gere uma **Vantagem Competitiva Sustentável** de longo prazo para a organização, ele deve preencher cumulativamente os quatro requisitos:

* **A)** Ser Valioso (V), Raro (R), Difícil de Imitar/Inimitável (I) e a organização estar Organizada (O) para explorá-lo plenamente.
* **B)** Ser Volátil, Razoável, Imediato e Onipresente.
* **C)** Ser Vigoroso, Regular, Inflexível e Oneroso.
* **D)** Ter Vencimento anual, Restrição orçamentária, Isenção tributária e Opção de resgate.
* **E)** Ter Valor monetário alto, Rapidez de liquidação, Inscrição em dívida ativa e Ordem bancária emitida.

> **Comentário Detalhado:**
>
> - **A)** Correta. O modelo **VRIO** de Jay Barney estabelece que um recurso/capacidade gera vantagem sustentável quando é: **Valioso** (permite explorar oportunidades ou neutralizar ameaças); **Raro** (poucos concorrentes o possuem); **Inimitável / Imperfeitamente Imitável** (difícil e custoso de ser copiado ou substituído por concorrentes); e a instituição está **Organizada** (possui estrutura, governança e processos capazes de capturar esse potencial).
> - **B), C), D), E)** Incorretas. Distorções arbitrárias sem qualquer respaldo na RBV.
> 
> **Gabarito: A**

---

"""

    q09_10 = """### Questão 09 (FCC - Adaptada / TCE-PI - Auditor de Controle Externo)
Na modelagem inovadora de serviços e projetos públicos pelo *Business Model Canvas* (Alexander Osterwalder), o bloco que define como a instituição se comunica e entrega a sua proposta de valor aos diferentes segmentos de usuários e cidadãos é denominado:

* **A)** Canais (de Comunicação, Distribuição e Acesso).
* **B)** Estrutura de Custos.
* **C)** Fluxo de Receitas.
* **D)** Recursos Principais.
* **E)** Parcerias-Chave.

> **Comentário Detalhado:**
>
> - **A)** Correta. No **Canvas**: os **Canais** descrevem os pontos de contato e os meios pelos quais a organização se comunica com os usuários e entrega sua proposta de valor (ex.: atendimento presencial, portal eletrônico na internet, aplicativo móvel, ouvidoria, diário oficial).
> - **B)** Incorreta. Custos reúne as principais despesas de operação.
> - **C)** Incorreta. Fontes de receita descreve a monetização ou ingressos orçamentários.
> - **D)** Incorreta. Recursos principais são os ativos humanos, físicos e tecnológicos essenciais.
> - **E)** Incorreta. Parcerias-chave são a rede de colaboradores e fornecedores externos.
> 
> **Gabarito: A**

---

### Questão 10 (FCC - Adaptada / TCE-GO - Analista de Controle Externo)
Segundo as Estratégias Genéricas de Michael Porter, quando uma organização busca se destacar perante os usuários e a sociedade criando produtos ou serviços amplamente percebidos como únicos, de qualidade superior e com atributos exclusivos inigualáveis no setor, ela adota a estratégia de:

* **A)** Diferenciação.
* **B)** Liderança em Custo Total.
* **C)** Foco ou Enfoque em Custos Reduzidos.
* **D)** Desinvestimento em Ativos Intangíveis.
* **E)** Equalização Regressiva de Preços.

> **Comentário Detalhado:**
>
> - **A)** Correta. Michael Porter descreve três estratégias genéricas: (1) **Liderança em Custo**: eficiência operacional para produzir ao menor custo da indústria; (2) **Diferenciação**: oferta de serviços/produtos percebidos como únicos e diferenciados pela inovação, marca e qualidade; (3) **Foco/Enfoque**: concentração em um nicho específico de mercado (por custo ou diferenciação).
> - **B)** Incorreta. Liderança em custo foca no menor custo operacional possível.
> - **C)** Incorreta. Foco em custos atende um nicho restrito pelo menor preço.
> - **D), E)** Incorretas. Termos sem relação com o modelo porteriano.
> 
> **Gabarito: A**

---

"""

    anchor_2 = "### 2. O Modelo das Cinco Forças e as Estratégias Genéricas de Michael Porter"
    anchor_3 = "### 3. A Visão Baseada em Recursos (RBV) e o Framework VRIO (Jay Barney)"
    anchor_4 = "### 4. O Business Model Canvas (Alexander Osterwalder)"
    anchor_fontes = "### 5. Fontes Oficiais e Referências Bibliográficas"

    text = text.replace(anchor_2, q06 + "\n" + anchor_2)
    text = text.replace(anchor_3, q07 + "\n" + anchor_3)
    text = text.replace(anchor_4, q08 + "\n" + anchor_4)
    text = text.replace(anchor_fontes, q09_10 + "\n" + anchor_fontes)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    print("Enriched File 23/02 successfully! Total: 10 questions.")


def enrich_file_03():
    filepath = os.path.join(BASE_DIR, "03_cadeia_de_valor_bsc_e_execucao_estrategica.md")
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    if "### Questão 06" in text:
        print("File 03 already enriched.")
        return

    q06 = """### Questão 06 (FCC - Adaptada / Analista de Gestão Pública)
Na Cadeia de Valor de Michael Porter, as atividades empresariais e organizacionais são rigorosamente classificadas em Atividades Primárias e Atividades de Apoio (ou Suporte).

Constitui típica **Atividade Primária** da Cadeia de Valor:

* **A)** Logística Interna (recebimento, armazenamento e distribuição de insumos e matérias-primas).
* **B)** Gestão de Recursos Humanos (recrutamento, seleção, treinamento e remuneração).
* **C)** Desenvolvimento de Tecnologia e Pesquisa (P&D).
* **D)** Infraestrutura da Empresa (planejamento, contabilidade, finanças e assessoria jurídica).
* **E)** Aquisição / Compras de suprimentos corporativos gerais.

> **Comentário Detalhado:**
>
> - **A)** Correta. A Cadeia de Valor de Porter divide-se em: **Atividades Primárias** (envolvidas diretamente na criação física, venda e entrega do produto/serviço): Logística Interna, Operações, Logística Externa, Marketing/Vendas e Serviços pós-venda. As **Atividades de Apoio/Suporte** (sustentam as atividades primárias fornecendo insumos, tecnologia e infraestrutura): Infraestrutura da empresa, Gestão de RH, Desenvolvimento de Tecnologia e Aquisição/Compras.
> - **B), C), D), E)** Incorretas. São todas Atividades de Apoio / Suporte.
> 
> **Gabarito: A**

---

"""

    q07 = """### Questão 07 (FCC - Adaptada / Auditor de Controle Externo)
No processo de desdobramento da estratégia corporativa pelo Balanced Scorecard, a técnica denominada **Cascading** (Estratégia em Cascata) tem por objetivo central:

* **A)** Desdobrar e traduzir os objetivos, metas e indicadores corporativos do nível estratégico para os níveis tático e operacional, alinhando as diretorias setoriais, gerências e equipes individuais à estratégia mestre da organização.
* **B)** Eliminar a remuneração variável e gratificações dos servidores públicos estaduais.
* **C)** Concentrar todas as decisões de compras na presidência da comissão permanente de licitação.
* **D)** Impor a demissão periódica de 10% dos servidores com pior produtividade mecânica.
* **E)** Substituir os sistemas de gestão eletrônica de processos por formulários impressos.

> **Comentário Detalhado:**
>
> - **A)** Correta. O desdobramento da estratégia (*cascading*) promove o alinhamento organizacional vertical: os objetivos macro do mapa estratégico institucional são sucessivamente traduzidos em objetivos departamentais e metas operacionais para equipes e indivíduos, assegurando que o trabalho diário contribua para a estratégia corporativa.
> - **B), C), D), E)** Incorretas. Distorções que nada têm a ver com a metodologia do BSC.
> 
> **Gabarito: A**

---

"""

    q08 = """### Questão 08 (FCC - Adaptada / Analista de Planejamento e Gestão)
Kaplan e Norton identificaram as quatro barreiras primordiais que impedem a execução eficaz das estratégias organizacionais nas instituições.

A barreira que ocorre quando a alta direção formula a estratégia, mas não a comunica nem a torna compreensível para os servidores e colaboradores que executam os serviços cotidianos na ponta da linha é denominada:

* **A)** Barreira da Visão.
* **B)** Barreira das Pessoas.
* **C)** Barreira da Gestão.
* **D)** Barreira dos Recursos.
* **E)** Barreira Orçamentária Externa.

> **Comentário Detalhado:**
>
> - **A)** Correta. As **quatro barreiras de Kaplan e Norton**: (1) **Barreira da Visão**: a equipe não compreende a estratégia nem a visão (apenas uma minoria conhece o plano); (2) **Barreira das Pessoas**: metas e incentivos individuais não estão ligados à estratégia; (3) **Barreira da Gestão**: a liderança dedica tempo excessivo a problemas operacionais e pouco à estratégia; (4) **Barreira dos Recursos**: orçamentos e investimentos não são alocados aos projetos estratégicos prioritários.
> - **B), C), D), E)** Incorretas. Outras barreiras ou terminologias distintas do conceito cobrado.
> 
> **Gabarito: A**

---

"""

    q09_10 = """### Questão 09 (FCC - Adaptada / TCE-PI - Auditor de Controle Externo)
Na governança estratégica moderna dos órgãos públicos (como no TCE-GO), as **Reuniões de Avaliação da Estratégia (RAE)** desempenham papel crucial na governança executiva.

O propósito primordial das RAEs é:

* **A)** Avaliar o andamento das iniciativas e indicadores estratégicos institucionais em periodicidade definida, debatendo causas de desvios e decidindo intervenções saneadoras e alocação de recursos em alto nível.
* **B)** Realizar a apuração de faltas funcionais disciplinares individuais dos servidores para abertura de PAD.
* **C)** Fiscalizar a conformidade fiscal das declarações de imposto de renda de pessoas físicas.
* **D)** Redigir pareceres jurídicos para aprovação de editais de concurso público.
* **E)** Conceder recesso administrativo remunerado aos membros dos comitês executivos.

> **Comentário Detalhado:**
>
> - **A)** Correta. As **Reuniões de Avaliação da Estratégia (RAE)** reúnem periodicamente a alta administração e os líderes de projetos para revisar o mapa estratégico, analisar se os indicadores estão atingindo as metas e tomar decisões corretivas para destravar projetos estratégicos prioritários.
> - **B), C), D), E)** Incorretas. Funções corriqueiras ou disciplinares estranhas ao escopo das RAEs.
> 
> **Gabarito: A**

---

### Questão 10 (FCC - Adaptada / TCE-GO - Analista de Controle Externo)
No âmbito dos Tribunais de Contas, o **Escritório de Gestão Estratégica (EGE)** atua como unidade técnica de apoio à governança corporativa.

Dentre as atribuições típicas do EGE em uma corte de contas, destaca-se:

* **A)** Facilitar o processo de planejamento estratégico institucional, apoiar as áreas na definição de indicadores e metas, consolidar relatórios de desempenho e secretariar as Reuniões de Avaliação da Estratégia.
* **B)** Emitir votos de julgamento de mérito com força jurisdicional nos processos de fiscalização contábil.
* **C)** Fiscalizar in loco as obras de construção civil e realizar medições de asfalto em rodovias estaduais.
* **D)** Gerenciar a segurança armada e o policiamento ostensivo das portarias do prédio sede.
* **E)** Substituir os Conselheiros titulares do Tribunal em caso de vacância definitiva do cargo.

> **Comentário Detalhado:**
>
> - **A)** Correta. O **Escritório de Gestão Estratégica (EGE / PMO Estratégico)** é o guardião metodológico da estratégia do órgão: auxilia a formulação, apoia os gestores setoriais na gestão de projetos e indicadores, padroniza ferramentas (BSC, 5W2H) e alimenta a alta direção com dados consolidados para subsidiar decisões de governança.
> - **B), C), D), E)** Incorretas. Atribuições institucionais próprias dos Conselheiros, auditores fiscais ou segurança predial.
> 
> **Gabarito: A**

---

"""

    anchor_2 = "### 2. O Desdobramento da Estratégia (*Cascading*) pelo BSC"
    anchor_3 = "### 3. As Quatro Barreiras à Execução da Estratégia (Kaplan e Norton)"
    anchor_4 = "### 4. Escritório de Gestão Estratégica (EGE) e Reuniões de Avaliação (RAE)"
    anchor_fontes = "### 5. Fontes Oficiais e Referências Bibliográficas"

    text = text.replace(anchor_2, q06 + "\n" + anchor_2)
    text = text.replace(anchor_3, q07 + "\n" + anchor_3)
    text = text.replace(anchor_4, q08 + "\n" + anchor_4)
    text = text.replace(anchor_fontes, q09_10 + "\n" + anchor_fontes)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    print("Enriched File 23/03 successfully! Total: 10 questions.")


if __name__ == "__main__":
    enrich_file_01()
    enrich_file_02()
    enrich_file_03()
    print("Module 23 fully processed!")
