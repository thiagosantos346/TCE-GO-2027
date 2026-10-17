# -*- coding: utf-8 -*-
"""
Enriquecedor Módulo 22 - Administração Geral
Arquivos: 01, 02, 03
Adiciona de 5 a 6 questões por arquivo (Questões 06 a 10/11) no padrão rigoroso FCC / Anti-spoiler.
"""

import os

BASE_DIR = "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/22_administracao_geral"

def enrich_file_01():
    filepath = os.path.join(BASE_DIR, "01_teorias_da_administracao_e_escolas_administrativas.md")
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    if "### Questão 06" in text:
        print("File 01 already enriched.")
        return

    # Q06: Após 3. Teoria das Relações Humanas (antes de ### 4.)
    q06 = """### Questão 06 (FCC - Adaptada / Analista de Gestão Pública)
A Teoria das Relações Humanas, impulsionada pelos estudos de Elton Mayo na fábrica de Hawthorne (Western Electric Company, 1927-1932), revolucionou a teoria administrativa ao demonstrar que:

* **A)** O nível de produção e a produtividade no trabalho são determinados primordialmente pela integração social e pelas normas informais do grupo, e não apenas pela capacidade física ou fisiológica do trabalhador.
* **B)** O operário é motivado exclusivamente por incentivos salariais materiais e materiais financeiros (*Homo economicus*).
* **C)** A divisão extrema do trabalho em tarefas microscópicas e cronometradas elimina qualquer necessidade de supervisão humana.
* **D)** A fadiga muscular é a única causa de acidentes e quebras de produtividade no ambiente industrial.
* **E)** As organizações formais funcionam como engrenagens mecânicas imunes a sentimentos, grupos informais e estados psicológicos.

> **Comentário Detalhado:**
>
> - **A)** Correta. A experiência de Hawthorne revelou que o trabalhador não atua isolado, mas como membro de um grupo social (*Homo socialis*). A produtividade é influenciada por fatores psicossociais, reconhecimento, moral do grupo e liderança informal.
> - **B)** Incorreta. O conceito de *Homo economicus* pertence à Administração Científica de Taylor.
> - **C)** Incorreta. Concepção taylorista de estudos de tempos e movimentos.
> - **D)** Incorreta. Elton Mayo provou que o efeito psicológico do grupo superava a fadiga física nas variações de produção.
> - **E)** Incorreta. Visão mecanicista da Escola Clássica que foi superada pela abordagem humanística.
> 
> **Gabarito: A**

---

"""

    # Q07: Após 5. Abordagem Comportamental (antes de ### 6.)
    q07 = """### Questão 07 (FCC - Adaptada / Auditor de Controle Externo)
Na Teoria Comportamental da Administração, Douglas McGregor concebeu duas visões antagônicas a respeito da natureza humana e da atitude dos indivíduos em relação ao trabalho: a **Teoria X** e a **Teoria Y**.

Segundo McGregor, a **Teoria Y** fundamenta-se na premissa de que:

* **A)** O dispêndio de esforço físico e mental no trabalho é tão natural quanto o lazer ou o repouso; o ser humano comum não tem aversão intrínseca ao trabalho e pode aprender não só a aceitar, mas a buscar responsabilidades sob condições favoráveis.
* **B)** O homem médio é indolente por natureza, evita o trabalho sempre que possível e precisa ser coagido, vigiado e controlado rigorosamente por meio de punições.
* **C)** As pessoas são desprovidas de ambição, preferem ser dirigidas e buscam prioritariamente a segurança acima de qualquer outro fator.
* **D)** A criatividade na solução de problemas organizacionais é privilégio raro e exclusivo dos ocupantes da alta direção.
* **E)** As recompensas financeiras estritas são a única força capaz de mobilizar a dedicação dos empregados.

> **Comentário Detalhado:**
>
> - **A)** Correta. A **Teoria Y** baseia-se em premissas humanistas, democráticas e participativas: o trabalho é visto como fonte de satisfação; os trabalhadores são automotivados, responsáveis e criativos quando engajados em metas organizacionais que atendem às suas necessidades de autorrealização.
> - **B)** Incorreta. Descrição clássica dos postulados autoritários da **Teoria X**.
> - **C)** Incorreta. Premissa da **Teoria X**.
> - **D)** Incorreta. Na Teoria Y, a criatividade e a engenhosidade são amplamente distribuídas na população.
> - **E)** Incorreta. Visão de incentivos materiais típica da Teoria X e da Administração Científica.
> 
> **Gabarito: A**

---

"""

    # Q08: Após 7. Teoria Contingencial (antes de ### 8.)
    q08 = """### Questão 08 (FCC - Adaptada / Analista de Planejamento e Gestão)
A Teoria Contingencial da Administração (desenvolvida a partir de pesquisas de Lawrence & Lorsch, Burns & Stalker e Joan Woodward) estabelece que não existe uma "única melhor maneira" (*the one best way*) de administrar e organizar, pois a estrutura e as práticas organizacionais dependem das variáveis ambientais e tecnológicas.

Segundo a tipologia de Tom Burns e G. M. Stalker, uma **estrutura orgânica** é mais adequada quando a organização opera em um ambiente:

* **A)** Dinâmico, instável e imprevisível, exigindo flexibilidade, descentralização decisória, baixa formalização e comunicações laterais/horizontais.
* **B)** Totalmente estável, estático e previsível, onde tarefas rotineiras repetitivas e centralização rígida produzem máxima eficiência.
* **C)** Fechado a qualquer influência externa e focado em controle legalista estrito de ponto eletrônico.
* **D)** Monopolista estatal sem qualquer interação com os cidadãos e a sociedade civil.
* **E)** Altamente regulado por normas que proíbam a adaptação a novas tecnologias digitais.

> **Comentário Detalhado:**
>
> - **A)** Correta. Burns e Stalker demonstraram que os **sistemas orgânicos** (flexíveis, descentralizados, baseados em redes e conhecimento especializado horizontal) ajustam-se a ambientes mutáveis e turbulentos; já os **sistemas mecanicistas** (burocráticos, verticais e rígidos) funcionam bem em ambientes estáveis e previsíveis.
> - **B)** Incorreta. Ambientes estáveis favorecem estruturas mecanicistas/burocráticas.
> - **C), D), E)** Incorretas. Distorções que contrariam a abertura e adaptabilidade dos modelos contingenciais.
> 
> **Gabarito: A**

---

"""

    # Q09 e Q10: Após 8. Metáforas Organizacionais antes de ### 9. Fontes Oficiais
    q09_10 = """### Questão 09 (FCC - Adaptada / TCE-PI - Auditor de Controle Externo)
Na obra clássica *Imagens da Organização*, Gareth Morgan analisa as organizações por meio de diferentes metáforas para explicar como gestores percebem e projetam as instituições.

A metáfora que visualiza a organização como um sistema adaptativo que necessita processar informações constantemente, aprender com os erros e reestruturar sua própria base de conhecimento e diretrizes (conceito de circuito duplo de aprendizagem) é a:

* **A)** Organização como Cérebro.
* **B)** Organização como Máquina.
* **C)** Organização como Prisão Psíquica.
* **D)** Organização como Instrumento de Dominação.
* **E)** Organização como Sistema Político de Coalizões.

> **Comentário Detalhado:**
>
> - **A)** Correta. A metáfora do **Cérebro** (Gareth Morgan) retrata a organização como um sistema de processamento de informações e aprendizagem contínua (*learning organization*), inspirando-se na cibernética e no holograma, onde as partes contêm o todo e a organização aprende a aprender (aprendizagem de circuito duplo).
> - **B)** Incorreta. A metáfora da Máquina retrata a burocracia clássica e mecanicista (Taylor e Weber).
> - **C)** Incorreta. A Prisão Psíquica aborda armadilhas inconscientes e ilusões partilhadas.
> - **D)** Incorreta. Instrumento de Dominação foca na exploração de empregados e comunidades.
> - **E)** Incorreta. Sistema Político foca em disputas de poder, interesses e coalizões.
> 
> **Gabarito: A**

---

### Questão 10 (FCC - Adaptada / TCE-GO - Analista de Controle Externo)
Em relação aos 14 princípios gerais da administração enunciados por Henri Fayol na Teoria Clássica, assinale a opção que define o princípio da **Unidade de Comando**:

* **A)** Cada colaborador ou servidor deve receber ordens e prestar contas exclusivamente a um único superior hierárquico direto.
* **B)** Todas as unidades do órgão devem possuir o mesmo quantitativo de servidores em exercício.
* **C)** O controle orçamentário deve ser unificado na presidência do Tribunal de Justiça.
* **D)** As decisões estratégicas devem ser tomadas sempre em comissões colegiadas deliberativas.
* **E)** Os servidores comissionados possuem autoridade irrestrita sobre os servidores estáveis.

> **Comentário Detalhado:**
>
> - **A)** Correta. O princípio da **Unidade de Comando** de Fayol postula que um subordinado deve reportar-se e receber ordens de apenas um único chefe imediato, evitando conflitos de autoridade, ambiguidade de papéis e instruções contraditórias.
> - **B), C), D), E)** Incorretas. Não guardam nenhuma relação com o princípio clássico da unidade de comando de Fayol.
> 
> **Gabarito: A**

---

"""

    anchor_4 = "### 4. Teoria da Burocracia (Max Weber) e as Disfunções Burocráticas (Robert Merton)"
    anchor_6 = "### 6. Teoria Geral dos Sistemas (TGS): A Organização como Sistema Aberto"
    anchor_8 = "### 8. Metáforas Organizacionais de Gareth Morgan"
    anchor_fontes = "### 9. Fontes Oficiais e Referências Bibliográficas"

    text = text.replace(anchor_4, q06 + "\n" + anchor_4)
    text = text.replace(anchor_6, q07 + "\n" + anchor_6)
    text = text.replace(anchor_8, q08 + "\n" + anchor_8)
    text = text.replace(anchor_fontes, q09_10 + "\n" + anchor_fontes)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    print("Enriched File 22/01 successfully! Total: 10 questions.")


def enrich_file_02():
    filepath = os.path.join(BASE_DIR, "02_organizacao_racional_do_trabalho_estruturas_e_ambientes.md")
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    if "### Questão 06" in text:
        print("File 02 already enriched.")
        return

    q06 = """### Questão 06 (FCC - Adaptada / Analista de Gestão Pública)
A Organização Racional do Trabalho (ORT), núcleo da Administração Científica de Frederick W. Taylor, estruturou-se em fundamentos técnicos para combater a "vadiagem sistemática" dos operários e elevar a produtividade.

Dentre os pilares da ORT, o **Estudo dos Tempos e Movimentos** (*Motion and Time Study*) visava essencialmente:

* **A)** Decompor cada tarefa fabril em seus movimentos elementares para eliminar movimentos inúteis, simplificar a execução e fixar o tempo-padrão de realização.
* **B)** Fixar os prazos de tramitação de processos administrativos no âmbito dos Tribunais de Contas.
* **C)** Estabelecer o horário fixo de entrada e saída dos servidores com tolerância de dez minutos.
* **D)** Organizar os intervalos de repouso conforme a vontade individual espontânea de cada trabalhador.
* **E)** Subordinar a chefia de fábrica à avaliação semestral de clima organizacional pelos empregados.

> **Comentário Detalhado:**
>
> - **A)** Correta. Taylor e Gilbreth desenvolveram a análise do trabalho mediante decomposição e cronometragem minuciosa dos movimentos: eliminavam-se movimentos desnecessários e ociosos, padronizavam-se ferramentas e fixava-se o tempo médio necessário para um operário médio desempenhar a tarefa (*tempo-padrão*).
> - **B), C), D), E)** Incorretas. Distorções que não representam o pilar da ORT taylorista.
> 
> **Gabarito: A**

---

"""

    q07 = """### Questão 07 (FCC - Adaptada / Auditor de Controle Externo)
No estudo da dinâmica organizacional, a **Organização Informal** coexiste paralelamente com a **Organização Formal** em toda repartição pública.

Constitui característica exclusiva da **Organização Informal**:

* **A)** O surgimento espontâneo a partir das interações sociais, simpatias, antipatias e afinidades interpessoais entre os servidores, não figurando nos organogramas e manuais oficiais.
* **B)** A formalização expressa em decretos de criação e estatutos jurídicos aprovados pelo Poder Legislativo.
* **C)** A definição prévia de níveis hierárquicos e competências funcionais taxativamente atribuídas por portaria.
* **D)** A obrigatoriedade de registro dos fluxos de comunicação em livros de ata públicos.
* **E)** A estabilidade jurídica vitalícia conferida por concurso público formal.

> **Comentário Detalhado:**
>
> - **A)** Correta. A **organização informal** emerge espontaneamente nas relações humanas diárias entre as pessoas: manifesta-se em padrões de liderança informal, canais de comunicação paralelos (a "rádio corredor"), grupos de amizade e normas de conduta tácitas que não constam de nenhum organograma formal.
> - **B), C), D), E)** Incorretas. Características exclusivas da organização **formal**.
> 
> **Gabarito: A**

---

"""

    q08 = """### Questão 08 (FCC - Adaptada / Analista de Planejamento e Controle)
Na teoria da administração, a delegação de autoridade é instrumento indispensável para a descentralização gerencial e agilização dos processos decisórios.

A respeito da delegação de autoridade, é uma regra fundamental da ciência da administração que:

* **A)** A autoridade pode ser delegada, mas a responsabilidade final pelo resultado alcançado permanece indelegável perante a autoridade superior que realizou a delegação.
* **B)** Tanto a autoridade quanto a responsabilidade integral são transferidas definitivamente ao subordinado, eximindo o superior de qualquer dever de supervisão.
* **C)** É obrigatória a delegação de atos normativos de caráter geral e a decisão de recursos administrativos ordinários.
* **D)** A delegação só é lícita quando envolver poderes irrevogáveis com prazo mínimo de dez anos.
* **E)** O subordinado que recebe autoridade delegada passa a responder diretamente ao Chefe do Poder Executivo.

> **Comentário Detalhado:**
>
> - **A)** Correta. Postulado clássico da teoria da delegação (também presente no Direito Administrativo - Lei nº 9.784/1999): a autoridade (o poder de agir e decidir) transfere-se ao subordinado delegado, mas a **responsabilidade final perante a alta administração permanece com o delegante** (*culpa in eligendo* e *culpa in vigilando*). O superior não se exime da responsabilidade final de controle.
> - **B)** Incorreta. A responsabilidade não se extingue com a delegação.
> - **C)** Incorreta. Atos normativos e recursos são legalmente indelegáveis (art. 13 da Lei nº 9.784/1999).
> - **D)** Incorreta. A delegação é ato discricionário e essencialmente revogável a qualquer tempo.
> - **E)** Incorreta. O delegado responde perante a autoridade que lhe conferiu a delegação.
> 
> **Gabarito: A**

---

"""

    q09_10 = """### Questão 09 (FCC - Adaptada / TCE-PI - Auditor de Controle Externo)
Na análise do ambiente organizacional, os teóricos contemporâneos distinguem o **Macroambiente (Ambiente Geral)** do **Microambiente (Ambiente de Tarefa ou Operacional)**.

Constitui elemento integrante do **Ambiente de Tarefa (Microambiente)** de uma organização pública:

* **A)** Os fornecedores de bens e serviços licitados, os cidadãos-usuários diretos dos serviços e os órgãos de controle externo fiscalizadores.
* **B)** As variáveis demográficas de longo prazo da população nacional.
* **C)** A conjuntura macroeconômica global e a taxa de câmbio internacional.
* **D)** O sistema jurídico-constitucional abstrato do país e as tendências climáticas planetárias.
* **E)** O conjunto de inovações científicas mundiais em física quântica.

> **Comentário Detalhado:**
>
> - **A)** Correta. O **Ambiente de Tarefa (Microambiente)** compreende o segmento do ambiente mais próximo e imediato com o qual a organização interage diretamente para atingir seus fins: clientes/usuários, fornecedores, concorrentes/parceiros e agências reguladoras/órgãos de controle. Já variáveis demográficas, econômicas, culturais e tecnológicas globais compõem o **Ambiente Geral (Macroambiente)**.
> - **B), C), D), E)** Incorretas. Elementos clássicos do Macroambiente geral.
> 
> **Gabarito: A**

---

### Questão 10 (FCC - Adaptada / TCE-GO - Analista de Controle Externo)
Em uma organização pública que busca aprimorar sua gestão, o diretor de departamento determinou que suas equipes eliminassem desperdícios de materiais e reduzissem os custos operacionais com papel e suprimentos de impressão em 30%, sem alterar a qualidade do serviço.

A ênfase conferida pelo diretor concentrou-se primordialmente na dimensão da:

* **A)** Eficiência (otimização do uso de insumos e recursos em relação aos produtos entregues / relação insumo-produto).
* **B)** Efetividade (grau de transformação e impacto social na comunidade de longo prazo).
* **C)** Eficácia pura (medida estrita do atingimento da meta final de atendimento).
* **D)** Descentralização operacional desverticalizada.
* **E)** Resiliência cibernética sistêmica.

> **Comentário Detalhado:**
>
> - **A)** Correta. A **Eficiência** diz respeito a "fazer certo as coisas" (ênfase nos meios, métodos, custos e economia de recursos): busca a melhor relação entre insumos (*inputs*) e resultados (*outputs*), reduzindo desperdícios e custos.
> - **B)** Incorreta. Efetividade mede impactos externos duradouros na sociedade.
> - **C)** Incorreta. Eficácia mede alcance do objetivo final independentemente dos custos.
> - **D), E)** Incorretas. Conceitos estranhos à questão de uso de recursos.
> 
> **Gabarito: A**

---

"""

    anchor_2 = "### 2. Dicotomia Conceitual: Eficiência vs. Eficácia vs. Efetividade"
    anchor_4 = "### 4. Centralização vs. Descentralização e a Regra Áurea da Delegação"
    anchor_5 = "### 5. Ambientes Organizacionais: Ambiente Geral (Macro) vs. Ambiente de Tarefa (Micro)"
    anchor_fontes = "### 6. Fontes Oficiais e Referências Bibliográficas"

    text = text.replace(anchor_2, q06 + "\n" + anchor_2)
    text = text.replace(anchor_4, q07 + "\n" + anchor_4)
    text = text.replace(anchor_5, q08 + "\n" + anchor_5)
    text = text.replace(anchor_fontes, q09_10 + "\n" + anchor_fontes)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    print("Enriched File 22/02 successfully! Total: 10 questions.")


def enrich_file_03():
    filepath = os.path.join(BASE_DIR, "03_processo_decisorio_visao_sistemica_e_gerenciamento_de_projetos.md")
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    if "### Questão 06" in text:
        print("File 03 already enriched.")
        return

    q06 = """### Questão 06 (FCC - Adaptada / Analista de Planejamento e Gestão)
Herbert Simon, em sua obra clássica *O Comportamento Administrativo* (prêmio Nobel de Economia de 1978), formulou a Teoria da **Racionalidade Limitada** (*Bounded Rationality*) na tomada de decisões.

Segundo a teoria da racionalidade limitada de Simon:

* **A)** O tomador de decisões é incapaz de obter e processar todas as informações disponíveis e prever todas as consequências futuras possíveis; por isso, em vez de buscar a decisão ótima máxima, ele opta por uma decisão **satisfatória** que atenda aos padrões mínimos aceitáveis.
* **B)** O gestor público possui capacidade cognitiva infinita e recursos ilimitados para identificar a solução perfeita e maximizadora para cada problema.
* **C)** O processo decisório deve ser guiado exclusivamente pela intuição e pela sorte, visto que a análise racional é impossível na vida pública.
* **D)** As decisões programadas exigem a realização de assembleias públicas populares para cada ato administrativo rotineiro.
* **E)** A racionalidade limitada impede que a Administração Pública utilize computadores ou sistemas de dados no auxílio à decisão.

> **Comentário Detalhado:**
>
> - **A)** Correta. Herbert Simon derrubou o mito do tomador de decisão econômico onisciente e onipotente (*racionalidade absoluta*): o ser humano possui limitações cognitivas, tempo escasso e informações incompletas. Por isso, ele atua no modelo do **homem administrativo**, que busca soluções satisfatórias (*satisficing*), e não maximizadoras.
> - **B)** Incorreta. Visão do modelo da racionalidade absoluta que Simon refutou.
> - **C)** Incorreta. Simon defende a racionalidade, reconhecendo apenas seus limites inerentes.
> - **D), E)** Incorretas. Distorções que não representam o modelo de Simon.
> 
> **Gabarito: A**

---

"""

    q07 = """### Questão 07 (FCC - Adaptada / Auditor de Controle Externo)
Na tomada de decisão sob diferentes condições ambientais, a situação em que o tomador de decisão conhece os possíveis desfechos alternativos e dispõe de dados históricos ou cálculos matemáticos que lhe permitem atribuir **probabilidades estatísticas objetivas** à ocorrência de cada resultado denomina-se:

* **A)** Tomada de decisão em Condição de Risco.
* **B)** Tomada de decisão em Condição de Certeza Absoluta.
* **C)** Tomada de decisão em Condição de Incerteza Completa.
* **D)** Tomada de decisão por Anarquia Organizada (*Garbage Can*).
* **E)** Decisão de Consenso Heurístico Irrestrito.

> **Comentário Detalhado:**
>
> - **A)** Correta. Condições de tomada de decisão: **Certeza**: os resultados futuros de cada alternativa são perfeitamente previsíveis e conhecidos; **Risco**: os desfechos não são certos, mas é possível estimar a **probabilidade matemática/estatística** de cada alternativa ocorrer com base em dados; **Incerteza**: os desfechos são imprevisíveis e não se conhecem probabilidades estatísticas.
> - **B)** Incorreta. Na certeza, conhece-se com exatidão o resultado, sem risco de desvio.
> - **C)** Incorreta. Na incerteza, inexistem dados de probabilidade calculável.
> - **D)** Incorreta. Modelo da "lata de lixo" (Cohen, March e Olsen) para anarquias organizadas.
> - **E)** Incorreta. Expressão sem respaldo na tipologia ambiental de decisões.
> 
> **Gabarito: A**

---

"""

    q08 = """### Questão 08 (FCC - Adaptada / Analista de Tecnologia e Controle)
No Gerenciamento de Projetos e no controle do cronograma de atividades interdependentes, o método do **Caminho Crítico** (*Critical Path Method - CPM*) define-se como:

* **A)** A sequência mais longa de atividades dependentes no diagrama de rede do projeto que determina a duração total mínima necessária para a conclusão do projeto, caracterizando-se por ter folga total igual a zero.
* **B)** O conjunto de tarefas com menor custo financeiro que podem ser canceladas sem prejuízo do cronograma.
* **C)** A lista de atividades secundárias executadas simultaneamente por equipes de suporte terceirizadas.
* **D)** O gráfico de barras que demonstra a distribuição de competências funcionais dos membros da equipe.
* **E)** O caminho que concentra exclusivamente os riscos jurídicos e trabalhistas do contrato de engenharia.

> **Comentário Detalhado:**
>
> - **A)** Correta. O **Caminho Crítico (CPM)** é a trajetória mais longa através do diagrama de rede (com maior duração total). As atividades que integram o caminho crítico têm **folga zero** (*zero slack*): qualquer atraso em uma atividade crítica provocará automaticamente atraso idêntico na data final de entrega de todo o projeto.
> - **B)** Incorreta. Atividades críticas não podem ser suprimidas ou atrasadas.
> - **C)** Incorreta. Descreve tarefas não críticas ou paralelas com folga.
> - **D)** Incorreta. Gráfico de barras é o Gráfico de Gantt.
> - **E)** Incorreta. CPM é metodologia de gestão de tempo e sequenciamento de atividades.
> 
> **Gabarito: A**

---

"""

    q09_10 = """### Questão 09 (FCC - Adaptada / TCE-PI - Auditor de Controle Externo)
Na teoria das organizações e no pensamento sistêmico, o fenômeno patológico no qual departamentos e setores operam de forma isolada, defendendo interesses corporativos paroquiais e fechando canais de comunicação com as demais unidades da instituição é denominado:

* **A)** Silos Organizacionais (Mentalidade de Silo).
* **B)** Holacracia Sistêmica Integrada.
* **C)** Sinergia Coletiva Positiva.
* **D)** Homeostase Dinâmica Adaptativa.
* **E)** Entropia Negativa Expansiva.

> **Comentário Detalhado:**
>
> - **A)** Correta. A **mentalidade de silo (ou silos organizacionais)** ocorre quando divisões e gerências funcionam como redomas fechadas e impermeáveis ("feudos burocráticos"), bloqueando a troca de dados, gerando retrabalhos, desconfiança e inviabilizando a visão sistêmica e holística da instituição.
> - **B)** Incorreta. Holacracia é modelo de gestão sem hierarquia tradicional e de alta cooperação.
> - **C)** Incorreta. Sinergia positiva significa que o todo é maior que a soma das partes (cooperação produtiva).
> - **D)** Incorreta. Homeostase é a capacidade de autorregulação e equilíbrio do sistema aberto.
> - **E)** Incorreta. Entropia negativa (negentropia) é a importação de energia para evitar o perecimento do sistema.
> 
> **Gabarito: A**

---

### Questão 10 (FCC - Adaptada / TCE-GO - Analista de Controle Externo)
No gerenciamento de projetos, a técnica **PERT** (*Program Evaluation and Review Technique*) é particularmente recomendada quando as durações das atividades são incertas, utilizando uma média ponderada baseada em três estimativas de tempo:

As três estimativas temporais consideradas pelo modelo PERT são:

* **A)** Tempo Otimista (a), Tempo Mais Provável (m) e Tempo Pessimista (b).
* **B)** Tempo Mínimo legal, Tempo Médio da carreira e Tempo Máximo de estabilidade.
* **C)** Duração da licitação, Duração do contrato e Duração da garantia.
* **D)** Horário bancário de abertura, fechamento e compensação.
* **E)** Prazo prescricional, Prazo decadencial e Prazo preclusivo.

> **Comentário Detalhado:**
>
> - **A)** Correta. O modelo probabilístico do **PERT** calcula a duração esperada (*Expected Time - TE*) pela fórmula ponderada: \(TE = \frac{a + 4m + b}{6}\), onde: **a** = tempo otimista (tudo dá certo); **m** = tempo mais provável (condições normais de operação); **b** = tempo pessimista (cenário em que ocorrem adversidades e problemas).
> - **B), C), D), E)** Incorretas. Distorções sem respaldo técnico na metodologia PERT.
> 
> **Gabarito: A**

---

"""

    anchor_2 = "### 2. Condições Ambientais da Tomada de Decisão"
    anchor_3 = "### 3. Visão Sistêmica, Pensamento Holístico e Silos Organizacionais"
    anchor_4 = "### 4. Gerenciamento de Projetos: Restrição Tripla, Gantt, CPM e PERT"
    anchor_fontes = "### 5. Fontes Oficiais e Referências Bibliográficas"

    text = text.replace(anchor_2, q06 + "\n" + anchor_2)
    text = text.replace(anchor_3, q07 + "\n" + anchor_3)
    text = text.replace(anchor_4, q08 + "\n" + anchor_4)
    text = text.replace(anchor_fontes, q09_10 + "\n" + anchor_fontes)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    print("Enriched File 22/03 successfully! Total: 10 questions.")


if __name__ == "__main__":
    enrich_file_01()
    enrich_file_02()
    enrich_file_03()
    print("Module 22 fully processed!")
