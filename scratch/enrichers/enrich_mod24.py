# -*- coding: utf-8 -*-
"""
Enriquecedor Módulo 24 - Comportamento Organizacional
Arquivos: 01, 02, 03
Adiciona de 5 a 6 questões por arquivo (Questões 06 a 10/11) no padrão rigoroso FCC / Anti-spoiler.
"""

import os

BASE_DIR = "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/24_comportamento_organizacional"

def enrich_file_01():
    filepath = os.path.join(BASE_DIR, "01_individuo_personalidade_valores_atitudes_e_motivacao.md")
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    if "### Questão 06" in text:
        print("File 01 already enriched.")
        return

    q06 = """### Questão 06 (FCC - Adaptada / Analista de Gestão Pública)
No estudo da personalidade humana no Comportamento Organizacional, o **Modelo dos Cinco Grandes Fatores (Big Five)** é amplamente aceito pela literatura científica contemporânea.

O fator do Big Five que descreve a tendência do indivíduo de ser responsável, disciplinado, organizado, pontual e orientado para o cumprimento rigoroso de metas e deveres é a:

* **A)** Conscienciosidade (ou Realização / Escrupulosidade).
* **B)** Extroversão.
* **C)** Agradabilidade (ou Amabilidade).
* **D)** Abertura para Experiências.
* **E)** Estabilidade Emocional (baixo Neuroticismo).

> **Comentário Detalhado:**
>
> - **A)** Correta. O modelo **Big Five** compreende: (1) **Conscienciosidade** (organização, responsabilidade, persistência e foco no dever); (2) **Extroversão** (sociabilidade, assertividade e expressividade); (3) **Amabilidade/Agradabilidade** (confiança, empatia e cooperação); (4) **Estabilidade Emocional / Neuroticismo** (autocontrole vs ansiedade/insegurança); (5) **Abertura a Experiências** (criatividade, curiosidade intelectual e imaginação). A conscienciosidade é o fator mais fortemente correlacionado ao desempenho profissional no trabalho.
> - **B), C), D), E)** Incorretas. Representam as outras quatro dimensões distintas da personalidade.
> 
> **Gabarito: A**

---

"""

    q07 = """### Questão 07 (FCC - Adaptada / Auditor de Controle Externo)
Segundo a Teoria da Dissonância Cognitiva formulada por Leon Festinger, quando um indivíduo percebe uma contradição ou inconsistência desconfortável entre duas atitudes ou entre sua atitude e seu comportamento real:

* **A)** Ele experimenta uma tensão psicológica desconfortável (dissonância) que o motiva a reduzir a inconsistência, alterando seu comportamento, modificando sua atitude ou racionalizando a discrepância.
* **B)** O indivíduo entra em estado de catatonia permanente sem capacidade de decisão.
* **C)** A dissonância cognitiva consolida automaticamente o comprometimento afetivo com o órgão público.
* **D)** Ocorre necessariamente a imediata demissão voluntária do cargo público.
* **E)** A incongruência atitudinal é eliminada por decreto do Chefe do Poder Executivo.

> **Comentário Detalhado:**
>
> - **A)** Correta. Leon Festinger postulou que a **Dissonância Cognitiva** é o estado de desconforto psicológico gerado pela incompatibilidade percebida entre crenças/atitudes e ações reais. O indivíduo busca ativamente reduzir essa tensão ajustando a conduta, alterando a atitude pregressa ou buscando justificativas racionais para harmonizar a contradição.
> - **B), C), D), E)** Incorretas. Distorções fantasiosas sem correspondência com a teoria psicológica de Festinger.
> 
> **Gabarito: A**

---

"""

    q08 = """### Questão 08 (FCC - Adaptada / Analista de Planejamento e Gestão)
Na Teoria dos Dois Fatores (ou Teoria Bifatorial) de Frederick Herzberg, os elementos do ambiente de trabalho dividem-se em Fatores Higiênicos (extrínsecos) e Fatores Motivacionais (intrínsecos).

Segundo Herzberg, os **Fatores Higiênicos** (como salário, condições físicas de trabalho, políticas da empresa e segurança do emprego):

* **A)** São capazes apenas de evitar a insatisfação quando presentes e adequados, mas não geram motivação nem satisfação genuína duradoura no trabalho.
* **B)** São a principal fonte geradora de autorrealização e orgulho profissional profundo no servidor.
* **C)** Referem-se ao conteúdo íntimo do cargo e aos desafios e responsabilidades inerentes à tarefa.
* **D)** Provocam alta satisfação mesmo quando as relações interpessoais com a chefia forem péssimas.
* **E)** Devem ser suprimidos das organizações públicas contemporâneas para evitar o comodismo.

> **Comentário Detalhado:**
>
> - **A)** Correta. A contribuição revolucionária de Herzberg foi demonstrar que o oposto de satisfação não é a insatisfação, mas a "não satisfação". Os **Fatores Higiênicos (extrínsecos)** atuam como profilaxia: quando ótimos, apenas neutralizam a insatisfação (deixam o trabalhador em estado neutro); para gerar **motivação real e satisfação**, são necessários os **Fatores Motivacionais (intrínsecos)**: conteúdo do cargo, autonomia, reconhecimento, responsabilidade e crescimento profissional.
> - **B), C)** Incorretas. Características exclusivas dos Fatores Motivacionais.
> - **D), E)** Incorretas. Contradizem a premissa de que os fatores higiênicos são necessários como base sanitária mínima.
> 
> **Gabarito: A**

---

"""

    q09_10 = """### Questão 09 (FCC - Adaptada / TCE-PI - Auditor de Controle Externo)
Na Teoria da Expectativa (ou Teoria da Expectância) de Victor Vroom, a motivação para agir decorre da multiplicação de três variáveis cognitivas: **Expectativa**, **Instrumentalidade** e **Valência** (\(M = E \times I \times V\)).

O conceito de **Instrumentalidade** corresponde à crença do indivíduo de que:

* **A)** O alcance de um determinado nível de desempenho bem-sucedido será recompensado com um resultado ou recompensa organizacional concreta (relação desempenho-recompensa).
* **B)** O seu esforço despendido resultará infalivelmente em um bom desempenho no trabalho (relação esforço-desempenho).
* **C)** O valor ou peso atrativo atribuído subjetivamente à recompensa oferecida pela organização é positivo.
* **D)** Os computadores e instrumentos de tecnologia fornecidos pela chefia são suficientes para a auditoria.
* **E)** A chefia é imune a pressões sindicais na distribuição de funções de confiança.

> **Comentário Detalhado:**
>
> - **A)** Correta. No modelo VIE de Victor Vroom: **Expectativa (E)**: crença de que o esforço levará ao desempenho (\(Esforço \rightarrow Desempenho\)); **Instrumentalidade (I)**: crença de que o bom desempenho alcançado será o instrumento para receber a recompensa almejada (\(Desempenho \rightarrow Recompensa\)); **Valência (V)**: o valor subjetivo ou atratividade que o indivíduo confere à recompensa recebida.
> - **B)** Incorreta. Refere-se à Expectativa.
> - **C)** Incorreta. Refere-se à Valência.
> - **D), E)** Incorretas. Sentidos corriqueiros de instrumento que não guardam relação com a teoria motivacional.
> 
> **Gabarito: A**

---

### Questão 10 (FCC - Adaptada / TCE-GO - Analista de Controle Externo)
Segundo a Teoria da Equidade de J. Stacy Adams, os indivíduos no ambiente de trabalho comparam a relação entre seus insumos/contribuições (esforço, dedicação, competência) e seus resultados/recompensas (remuneração, reconhecimento, promoções) com a relação insumo/resultado de outros colegas em funções semelhantes.

Quando o servidor público percebe uma situação de **iniquidade negativa** (sente-se injustiçado ao constatar que contribui mais e recebe menos reconhecimento que colegas em situação similar), a teoria prevê que ele tenderá a:

* **A)** Reduzir seu esforço e produtividade, aumentar o absenteísmo ou até solicitar remoção para outro setor, com o objetivo de restabelecer o equilíbrio e a equidade psicológica percebida.
* **B)** Aumentar espontaneamente sua carga horária de trabalho diário sem solicitar remuneração adicional.
* **C)** Renunciar voluntariamente ao cargo público estável em favor daquele colega menos produtivo.
* **D)** Desconsiderar completamente as recompensas institucionais e dobrar o ritmo de trabalho.
* **E)** Ignorar qualquer parâmetro de comparação social e atuar em estado de isolamento afetivo voluntário.

> **Comentário Detalhado:**
>
> - **A)** Correta. A Teoria da Equidade de Adams mostra que a percepção de injustiça gera tensão cognitiva e desmotivação. Para restabelecer o senso de justiça distributiva, o indivíduo adota comportamentos como: diminuir o esforço, produzir com menor qualidade, faltar ao serviço, distorcer mentalmente a comparação ou mudar de departamento.
> - **B), C), D), E)** Incorretas. Reações opostas à lógica do comportamento humano diante de injustiça distributiva percebida.
> 
> **Gabarito: A**

---

"""

    anchor_3 = "### 3. Atitudes, Dissonância Cognitiva e Comprometimento Organizacional"
    anchor_4 = "### 4. Teorias Motivacionais de Conteúdo (Maslow, Herzberg, Alderfer e McClelland)"
    anchor_5 = "### 5. Teorias Motivacionais de Processo (Vroom, Adams, Locke e Skinner)"
    anchor_fontes = "### 6. Fontes Oficiais e Referências Bibliográficas"

    text = text.replace(anchor_3, q06 + "\n" + anchor_3)
    text = text.replace(anchor_4, q07 + "\n" + anchor_4)
    text = text.replace(anchor_5, q08 + "\n" + anchor_5)
    text = text.replace(anchor_fontes, q09_10 + "\n" + anchor_fontes)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    print("Enriched File 24/01 successfully! Total: 10 questions.")


def enrich_file_02():
    filepath = os.path.join(BASE_DIR, "02_grupos_equipes_lideranca_e_comunicacao_organizacional.md")
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    if "### Questão 06" in text:
        print("File 02 already enriched.")
        return

    q06 = """### Questão 06 (FCC - Adaptada / Analista de Gestão Pública)
No Comportamento Organizacional, a distinção entre **Grupo de Trabalho** e **Equipe de Trabalho** é fundamental para a gestão de pessoas.

Constitui característica essencial e distintiva de uma **Equipe de Trabalho** de alto desempenho:

* **A)** A sinergia positiva gerada pelo esforço coordenado dos membros, resultando em um nível de desempenho coletivo maior do que a simples soma das contribuições individuais, com responsabilidade tanto individual quanto mútua.
* **B)** A independência estrita de objetivos, de tal modo que o sucesso de um membro prescinda do esforço dos demais.
* **C)** A concentração exclusiva das decisões na figura do chefe hierárquico formal, sem participação da equipe.
* **D)** A inexistência de complementaridade de habilidades técnicas entre os colaboradores.
* **E)** O foco exclusivo na produtividade individual isolada sem metas coletivas compartilhadas.

> **Comentário Detalhado:**
>
> - **A)** Correta. Diferença crucial: em um **Grupo de Trabalho**, o objetivo é apenas compartilhar informações e a sinergia é neutra (às vezes negativa), com responsabilidade apenas individual; em uma **Equipe de Trabalho**, há metas coletivas claras, habilidades complementares, responsabilidade mútua/compartilhada e **sinergia positiva** (o todo é superior à soma das partes).
> - **B), C), D), E)** Incorretas. Descrevem grupos de trabalho tradicionais ou unidades individualizadas.
> 
> **Gabarito: A**

---

"""

    q07 = """### Questão 07 (FCC - Adaptada / Auditor de Controle Externo)
Bruce Tuckman propôs um modelo seminal que descreve os cinco estágios universais pelos quais passam os grupos e equipes ao longo de seu ciclo de desenvolvimento.

O estágio em que o grupo supera conflitos internos de poder, estabelece coesão, define normas claras de convivência e desenvolve forte sentimento de identidade e camaradagem mútua é denominado:

* **A)** Normatização (Norming).
* **B)** Formação (Forming).
* **C)** Conflito / Tempestade (Storming).
* **D)** Desempenho (Performing).
* **E)** Desintegração / Dissolução (Adjourning).

> **Comentário Detalhado:**
>
> - **A)** Correta. Os 5 estágios de Tuckman: (1) **Formação (Forming)**: incerteza e orientação inicial; (2) **Tempestade/Conflito (Storming)**: disputas de liderança e atritos interpessoais; (3) **Normatização (Norming)**: estabelecimento de coesão, normas aceitas, alinhamento e regras de conduta; (4) **Desempenho (Performing)**: energia focada na execução produtiva da tarefa; (5) **Desintegração (Adjourning)**: conclusão e encerramento dos trabalhos.
> - **B), C), D), E)** Incorretas. Referem-se a outros estágios do ciclo de Tuckman.
> 
> **Gabarito: A**

---

"""

    q08 = """### Questão 08 (FCC - Adaptada / Analista de Planejamento e Controle)
Na Teoria da Liderança Situacional formulada por Paul Hersey e Kenneth Blanchard, o estilo de liderança mais eficaz não é fixo, mas depende do nível de **prontidão (ou maturidade)** dos liderados para desempenhar uma tarefa específica.

Quando os liderados apresentam **baixa competência e alto comprometimento/motivação** (estágio de maturidade M1), o estilo de liderança mais indicado pelo modelo é:

* **A)** Determinar / Direcionar (E1 - Direção), caracterizado por alto comportamento para a tarefa e baixo comportamento para o relacionamento (instruções claras e supervisão estrita).
* **B)** Delegar (E4 - Delegação), retirando toda a supervisão e deixando o liderado agir por conta própria.
* **C)** Apoiar / Participar (E3 - Apoio), com foco exclusivo em suporte afetivo e baixa orientação sobre como executar a tarefa.
* **D)** Autocracia repressiva punitiva com ameaça de abertura de processo administrativo.
* **E)** Demissão sumária por insuficiência de capacitação técnica.

> **Comentário Detalhado:**
>
> - **A)** Correta. No modelo de Hersey e Blanchard: para subordinados **M1** (iniciantes entusiastas, com baixa competência na tarefa, mas dispostos), o líder deve adotar o estilo **E1 - Direcionar/Determinar** (alto foco na tarefa e baixo em relacionamento): define papéis, ensina o passo a passo, dá instruções detalhadas e monitora o cumprimento.
> - **B)** Incorreta. Delegação (E4) exige maturidade máxima (M4 - alta competência e alto comprometimento).
> - **C)** Incorreta. Apoiar (E3) aplica-se a liderados com alta competência, mas segurança/motivação vacilante (M3).
> - **D), E)** Incorretas. Não fazem parte dos pressupostos teóricos do modelo situacional.
> 
> **Gabarito: A**

---

"""

    q09_10 = """### Questão 09 (FCC - Adaptada / TCE-PI - Auditor de Controle Externo)
Na moderna literatura sobre liderança, Bernard Bass consagrou a contraposição entre **Liderança Transacional** e **Liderança Transformacional**.

Constitui característica marcante da **Liderança Transformacional**:

* **A)** Inspirar e motivar os liderados a transcender seus interesses individuais em prol da missão coletiva da organização, estimulando a inovação, o questionamento construtivo e o desenvolvimento pessoal por meio da consideração individualizada e do estímulo intelectual.
* **B)** Basear-se exclusivamente em trocas contratuais de curto prazo, onde o líder apenas concede recompensas financeiras em troca do cumprimento estrito de metas.
* **C)** Utilizar primordialmente a gestão por exceção passiva, intervindo apenas quando falhas graves já ocorreram.
* **D)** Concentrar todo o poder e evitar que os servidores desenvolvam pensamento crítico autônomo.
* **E)** Punir severamente os liderados que apresentarem ideias inovadoras contrárias aos regulamentos tradicionais.

> **Comentário Detalhado:**
>
> - **A)** Correta. A **Liderança Transformacional** fundamenta-se nos quatro pilares clássicos ("Os 4 Is" de Bass): Influência Idealizada (carisma e credibilidade), Motivação Inspiracional (visão de futuro compartilhada), Estímulo Intelectual (incentivo à criatividade e solução de problemas) e Consideração Individualizada (atenção personalizada às necessidades de cada liderado).
> - **B), C)** Incorretas. Características definidoras da **Liderança Transacional** (recompensa contingente e gerência por exceção).
> - **D), E)** Incorretas. Posturas de chefia autoritária e punitiva.
> 
> **Gabarito: A**

---

### Questão 10 (FCC - Adaptada / TCE-GO - Analista de Controle Externo)
No processo de comunicação organizacional, a barreira que ocorre quando o emissor manipula deliberadamente as informações para que sejam vistas de modo mais favorável e lisonjeiro pelo receptor (muito comum em relações verticais ascendentes em que subordinados ocultam más notícias de seus chefes) é denominada:

* **A)** Filtragem.
* **B)** Percepção Seletiva.
* **C)** Sobrecarga de Informação.
* **D)** Ruído Semântico.
* **E)** Linguagem Não Verbal Involuntária.

> **Comentário Detalhado:**
>
> - **A)** Correta. A **Filtragem** é a manipulação consciente ou inconsciente da informação antes de transmiti-la, de forma a torná-la palatável ao superior hierárquico. Quanto mais vertical e autoritária a organização, maior a tendência de os subordinados filtrarem más notícias para evitar punições ou desagradar a chefia.
> - **B)** Incorreta. Percepção Seletiva ocorre no receptor, que ouve apenas o que se alinha aos seus interesses.
> - **C)** Incorreta. Sobrecarga é a incapacidade de processar o excesso de mensagens.
> - **D)** Incorreta. Ruído semântico decorre de palavras com duplo sentido ou jargões incompreendidos.
> - **E)** Incorreta. Gestos corporais e expressões faciais.
> 
> **Gabarito: A**

---

"""

    anchor_2 = "### 2. O Modelo de Desenvolvimento de Grupos de Bruce Tuckman"
    anchor_3 = "### 3. Evolução das Teorias de Liderança e a Liderança Situacional"
    anchor_4 = "### 4. Liderança Transacional vs. Liderança Transformacional"
    anchor_fontes = "### 6. Fontes Oficiais e Referências Bibliográficas"

    text = text.replace(anchor_2, q06 + "\n" + anchor_2)
    text = text.replace(anchor_3, q07 + "\n" + anchor_3)
    text = text.replace(anchor_4, q08 + "\n" + anchor_4)
    text = text.replace(anchor_fontes, q09_10 + "\n" + anchor_fontes)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    print("Enriched File 24/02 successfully! Total: 10 questions.")


def enrich_file_03():
    filepath = os.path.join(BASE_DIR, "03_conflito_negociacao_cultura_clima_e_desenvolvimento_organizacional.md")
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    if "### Questão 06" in text:
        print("File 03 already enriched.")
        return

    q06 = """### Questão 06 (FCC - Adaptada / Analista de Planejamento e Gestão)
Na evolução teórica a respeito dos conflitos organizacionais, três visões sucederam-se historicamente: a Visão Tradicional, a Visão de Relações Humanas e a Visão Interacionista.

Segundo a **Visão Interacionista** do conflito:

* **A)** O conflito não só é uma força natural inevitável nas organizações, como um nível mínimo de conflito construtivo e funcional é absolutamente necessário para manter o grupo viável, autocrítico, inovador e produtivo.
* **B)** Todo conflito é prejudicial, disfuncional e destrutivo, devendo ser imediatamente eliminado e reprimido pelas chefias.
* **C)** O conflito decorre exclusivamente da má contratação de servidores públicos no concurso público.
* **D)** A harmonia absoluta e a ausência de divergências garantem que a instituição atinja a excelência máxima de inovação.
* **E)** Os conflitos de relacionamento devem ser estimulados em níveis máximos para criar disputa destrutiva interna.

> **Comentário Detalhado:**
>
> - **A)** Correta. A **Visão Interacionista** postula que um grupo harmonioso, pacífico e cooperativo demais tende a tornar-se estático, apático e resistente à mudança. Por isso, líderes devem incentivar um nível apropriado de **conflito funcional de tarefa** (debate vigoroso sobre ideias, métodos e processos), diferenciando-o do conflito de relacionamento (que é disfuncional).
> - **B)** Incorreta. Visão Tradicional (décadas de 1930/1940), que via o conflito como anomalia perversa.
> - **C)** Incorreta. O conflito é inerente à diversidade humana e à escassez de recursos.
> - **D)** Incorreta. O excesso de conformidade (*pensamento de grupo / groupthink*) sufoca a criatividade.
> - **E)** Incorreta. Conflitos de relacionamento pessoal geram atrito destrutivo e hostilidade, sendo sempre disfuncionais.
> 
> **Gabarito: A**

---

"""

    q07 = """### Questão 07 (FCC - Adaptada / Auditor de Controle Externo)
Kenneth Thomas e Ralph Kilmann desenvolveram um modelo seminal de cinco estilos de administração de conflitos, estruturado em duas dimensões comportamentais: **Assertividade** (grau em que o indivíduo busca satisfazer seus próprios interesses) e **Cooperatividade** (grau em que busca satisfazer os interesses da outra parte).

O estilo de gestão de conflitos caracterizado por **alta assertividade e alta cooperatividade**, no qual as partes buscam uma solução ganha-ganha (*win-win*) que integre plenamente as preocupações de ambos, denomina-se:

* **A)** Colaboração (ou Solução de Problemas / Integração).
* **B)** Competição (ou Confrontação Forçada).
* **C)** Acomodação (ou Suavização).
* **D)** Não Enfrentamento (ou Evitação / Fuga).
* **E)** Acordo de Compromisso (ou Meio-termo superficial).

> **Comentário Detalhado:**
>
> - **A)** Correta. O modelo Thomas-Kilmann: (1) **Colaboração** (alta assertividade + alta cooperatividade): solução ganha-ganha que atende plenamente ambos os lados; (2) **Competição** (alta assertividade + baixa cooperatividade): ganha-perde; (3) **Acomodação** (baixa assertividade + alta cooperatividade): perde-ganha; (4) **Evitação/Fuga** (baixa assertividade + baixa cooperatividade): perde-perde; (5) **Compromisso** (médio-termo): concessões mútuas parciais.
> - **B), C), D), E)** Incorretas. Referem-se aos outros estilos do modelo.
> 
> **Gabarito: A**

---

"""

    q08 = """### Questão 08 (FCC - Adaptada / Analista de Tecnologia e Controle)
Na teoria da negociação baseada nos princípios do Projeto de Negociação de Harvard (Fisher, Ury e Patton), a **Negociação Integrativa (ou Baseada em Princípios)** distingue-se da Negociação Distributiva (ou Posicional) por:

* **A)** Concentrar-se nos interesses subjacentes reais das partes e não em posições rígidas assumidas, gerando opções de ganho mútuo e utilizando critérios objetivos justos para a solução das controvérsias.
* **B)** Tratar a negociação como uma disputa de soma-zero em que o ganho de uma parte equivale necessariamente à perda da outra ("divisão de um bolo fixo").
* **C)** Empregar táticas de pressão psicológica extrema, blefes e ocultação deliberada de dados essenciais.
* **D)** Impor a judicialização compulsória de todo conflito de gestão administrativa perante a Justiça Federal.
* **E)** Condicionar o desfecho da negociação à concessão de reajustes orçamentários automáticos pelo Tesouro.

> **Comentário Detalhado:**
>
> - **A)** Correta. A **Negociação Integrativa (Harvard)** baseia-se em quatro pilares fundamentais: (1) Separar as pessoas do problema; (2) Focar em **interesses** e não em posições; (3) Criar opções de **ganhos mútuos** antes de decidir; (4) Insistir em **critérios objetivos** (leis, precedentes, laudos técnicos).
> - **B), C)** Incorretas. Características exclusivas da **Negociação Distributiva / Competitiva**.
> - **D), E)** Incorretas. Distorções que contrariam a autonomia e a metodologia da negociação colaborativa.
> 
> **Gabarito: A**

---

"""

    q09_10 = """### Questão 09 (FCC - Adaptada / TCE-PI - Auditor de Controle Externo)
Edgar Schein estruturou a Cultura Organizacional em três níveis hierárquicos de visibilidade e profundidade psicológica: **Artefatos**, **Valores Compartilhados** e **Pressupostos Básicos**.

Os **Pressupostos Básicos** caracterizam-se por:

* **A)** Serem crenças, percepções e sentimentos inconscientes, invisíveis e profundamente arraigados, aceitos tacitamente como verdades inquestionáveis que orientam automaticamente a forma como os membros sentem e agem.
* **B)** Compreenderem a estrutura física dos prédios, o vestuário dos servidores e os manuais de procedimentos impressos.
* **C)** Consistirem em discursos oficiais gravados em vídeos institucionais divulgados nas redes sociais.
* **D)** Serem facilmente modificados a cada eleição mediante a edição de portarias administrativas simplificadas.
* **E)** Limitarem-se ao regimento interno do Tribunal de Contas aprovado em resolução.

> **Comentário Detalhado:**
>
> - **A)** Correta. O modelo de Schein (o iceberg da cultura): (1) **Artefatos**: nível visível da superfície (prédios, símbolos, vestuário, slogans, jargões); (2) **Valores Compartilhados**: nível intermediário (filosofias, normas de conduta, objetivos justificados conscientemente); (3) **Pressupostos Básicos**: nível mais profundo e submerso, inconsciente, formado por premissas tácitas e inquestionáveis sobre a natureza humana e a realidade, sendo o nível mais difícil de ser alterado em processos de mudança.
> - **B)** Incorreta. Refere-se aos **Artefatos**.
> - **C)** Incorreta. Refere-se a Artefatos e Valores declarados.
> - **D), E)** Incorretas. Pressupostos básicos são invisíveis e profundamente resistentes a mudanças superficiais.
> 
> **Gabarito: A**

---

### Questão 10 (FCC - Adaptada / TCE-GO - Analista de Controle Externo)
No modelo clássico de Desenvolvimento Organizacional e Gestão da Mudança proposto por Kurt Lewin, o processo de transformação estruturada de uma instituição desenvolve-se em três etapas sequenciais:

A ordem cronológica correta das três etapas de Kurt Lewin é:

* **A)** Descongelamento (*Unfreezing*), Mudança / Movimento (*Change/Moving*) e Recongelamento (*Refreezing*).
* **B)** Planejamento, Execução e Fiscalização orçamentária.
* **C)** Licitação, Homologação e Pagamento financeiro.
* **D)** Avaliação de Desempenho, Promoção e Aposentadoria.
* **E)** Centralização, Desconcentração e Extinção funcional.

> **Comentário Detalhado:**
>
> - **A)** Correta. O modelo das três etapas de Kurt Lewin para mudança organizacional: (1) **Descongelamento**: quebra dos velhos paradigmas, superação das resistências e sensibilização da equipe para a necessidade de mudar; (2) **Mudança (Movimento)**: assimilação de novas práticas, valores, rotinas e atitudes; (3) **Recongelamento**: cristalização e estabilização dos novos padrões de comportamento na cultura do órgão para garantir a sustentabilidade das mudanças.
> - **B), C), D), E)** Incorretas. Etapas de outros processos administrativos que não se relacionam ao modelo de mudança de Kurt Lewin.
> 
> **Gabarito: A**

---

"""

    anchor_2 = "### 2. Estilos de Administração de Conflitos (Thomas-Kilmann)"
    anchor_3 = "### 3. Técnicas de Negociação: Distributiva vs. Integrativa (Modelo Harvard)"
    anchor_4 = "### 4. Cultura Organizacional e os Três Níveis de Edgar Schein"
    anchor_fontes = "### 7. Fontes Oficiais e Referências Bibliográficas"

    text = text.replace(anchor_2, q06 + "\n" + anchor_2)
    text = text.replace(anchor_3, q07 + "\n" + anchor_3)
    text = text.replace(anchor_4, q08 + "\n" + anchor_4)
    text = text.replace(anchor_fontes, q09_10 + "\n" + anchor_fontes)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    print("Enriched File 24/03 successfully! Total: 10 questions.")


if __name__ == "__main__":
    enrich_file_01()
    enrich_file_02()
    enrich_file_03()
    print("Module 24 fully processed!")
