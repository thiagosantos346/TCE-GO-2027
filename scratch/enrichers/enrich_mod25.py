# -*- coding: utf-8 -*-
"""
Enriquecedor Módulo 25 - Gestão de Pessoas
Arquivos: 01, 02, 03, 04
Adiciona de 5 a 6 questões por arquivo (Questões 06 a 10/11) no padrão rigoroso FCC / Anti-spoiler.
No arquivo 04 (Lei 20.756/2020), inclui questões no formato: (FCC - Inédita - Padrão TCE-GO).
"""

import os

BASE_DIR = "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/25_gestao_de_pessoas"

def enrich_file_01():
    filepath = os.path.join(BASE_DIR, "01_processos_de_gp_recrutamento_selecao_e_integracao.md")
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    if "### Questão 06" in text:
        print("File 01 already enriched.")
        return

    q06 = """### Questão 06 (FCC - Adaptada / Analista de Gestão Pública)
Idalberto Chiavenato estrutura a moderna Gestão de Pessoas em seis processos básicos interdependentes: Agregar, Aplicar, Recompensar, Desenvolver, Manter e Monitorar pessoas.

O processo de **Aplicar Pessoas** compreende precipuamente as atividades de:

* **A)** Desenho organizacional de cargos, análise e descrição de funções, orientação e socialização das pessoas e avaliação do desempenho humano.
* **B)** Recrutamento interno, recrutamento externo e seleção de candidatos por provas e títulos.
* **C)** Concessão de remuneração fixa, incentivos salariais, benefícios e serviços sociais.
* **D)** Treinamento e desenvolvimento de competências, gestão do conhecimento e programas de mudança.
* **E)** Higiene, segurança e qualidade de vida no trabalho e relações com sindicatos.

> **Comentário Detalhado:**
>
> - **A)** Correta. Os seis processos de Chiavenato: (1) *Agregar Pessoas*: recrutamento e seleção; (2) **Aplicar Pessoas**: desenho de cargos, descrição de atribuições, orientação (*onboarding*) e avaliação de desempenho; (3) *Recompensar Pessoas*: remuneração, benefícios e incentivos; (4) *Desenvolver Pessoas*: treinamento, capacitação e aprendizagem; (5) *Manter Pessoas*: higiene, segurança, relações sindicais e QVT; (6) *Monitorar Pessoas*: banco de dados e sistemas de informação de RH.
> - **B)** Incorreta. Refere-se ao processo de *Agregar Pessoas*.
> - **C)** Incorreta. Refere-se ao processo de *Recompensar Pessoas*.
> - **D)** Incorreta. Refere-se ao processo de *Desenvolver Pessoas*.
> - **E)** Incorreta. Refere-se ao processo de *Manter Pessoas*.
> 
> **Gabarito: A**

---

"""

    q07 = """### Questão 07 (FCC - Adaptada / Auditor de Controle Externo)
No tocante às rotinas de recrutamento de pessoal, o **Recrutamento Interno** contrapõe-se ao **Recrutamento Externo** ao privilegiar a movimentação de servidores da própria organização.

Constitui uma típica **vantagem** do Recrutamento Interno:

* **A)** Maior rapidez no preenchimento da vaga, menor custo financeiro do processo e estímulo à motivação e à lealdade dos servidores atuais por meio de oportunidades concretas de plano de carreira.
* **B)** A introdução massiva de novas ideias, talentos externos e inovação de ponta na cultura corporativa.
* **C)** A renovação completa do quadro de pessoal e oxigenação da estrutura burocrática.
* **D)** A dispensa absoluta de avaliação de desempenho funcional e conformidade disciplinar.
* **E)** A eliminação do sentimento de frustração entre os servidores que não foram contemplados na promoção.

> **Comentário Detalhado:**
>
> - **A)** Correta. O **Recrutamento Interno** é mais econômico, mais rápido, apresenta maior índice de validade e segurança (o candidato já é conhecido) e atua como poderoso incentivo à motivação e retenção de talentos da casa.
> - **B), C)** Incorretas. Vantagens exclusivas do **Recrutamento Externo** (traz "sangue novo" e novas perspectivas).
> - **D)** Incorreta. A movimentação interna baseia-se exatamente no histórico e avaliação de desempenho.
> - **E)** Incorreta. O recrutamento interno frequentemente gera frustração nos candidatos não selecionados (efeito Peter e conflito de interesse).
> 
> **Gabarito: A**

---

"""

    q08 = """### Questão 08 (FCC - Adaptada / Analista de Planejamento e Gestão)
No processo de socialização organizacional (*onboarding*) dos novos servidores públicos ingressantes, John Van Maanen e Edgar Schein categorizam as táticas institucionais de socialização empregadas pela organização.

A tática de socialização caracterizada por integrar os novatos em grupos que passam pelas mesmas experiências e trilhas formativas conjuntas, com um cronograma predeterminado de etapas de acolhimento e mentoria, é classificada como:

* **A)** Coletiva, Formal e Sequencial.
* **B)** Individual, Informal e Aleatória.
* **C)** Desjuntiva, Isolada e Punitiva.
* **D)** Reativa, Transitória e Descentralizada.
* **E)** Cartorária, Regressiva e Desestruturada.

> **Comentário Detalhado:**
>
> - **A)** Correta. Táticas de socialização de Van Maanen e Schein: **Coletiva** (novatos acolhidos em turma/grupo, comum em cursos de formação de concursos públicos); **Formal** (atividades estruturadas de integração fora do posto de trabalho imediato); e **Sequencial** (etapas ordenadas e progressivas de aprendizado até a plena assunção do cargo).
> - **B), C), D), E)** Incorretas. Representam táticas individualizadas, informais ou termos desconexos da taxonomia clássica.
> 
> **Gabarito: A**

---

"""

    q09_10 = """### Questão 09 (FCC - Adaptada / TCE-PI - Auditor de Controle Externo)
Na Administração Pública brasileira, o concurso público de provas ou de provas e títulos constitui o instrumento constitucional republicano por excelência para a investidura em cargo ou emprego público (art. 37, II da CF/88).

A respeito das regras constitucionais do concurso público, é correto afirmar:

* **A)** O prazo de validade do concurso público será de até dois anos, prorrogável uma vez, por igual período, e a convocação do aprovado durante a validade obedecerá estritamente à ordem de classificação.
* **B)** A aprovação em concurso público gera sempre e em qualquer hipótese mera expectativa de direito, não assistindo ao candidato direito à nomeação mesmo quando aprovado dentro do número de vagas do edital.
* **C)** É lícito ao Poder Público abrir novo concurso público para o mesmo cargo e prover todas as novas vagas antes de convocar os candidatos remanescentes aprovados no concurso anterior com prazo de validade ainda em vigor.
* **D)** A fixação de limite de idade em edital independe de previsão em lei formal, bastando a conveniência discricionária do órgão.
* **E)** A realização de concurso público é dispensável para a contratação de pessoal docente permanente em universidades públicas estaduais.

> **Comentário Detalhado:**
>
> - **A)** Correta. Literalidade do art. 37, incisos III e IV da CF/88: prazo de validade de até 2 anos, prorrogável uma vez por igual período; a ordem classificatória é inafastável.
> - **B)** Incorreta. O STF já fixou tese vinculante (Tema 161 - RE 598.099) de que o candidato aprovado **dentro do número de vagas** do edital possui **direito subjetivo à nomeação** durante o prazo de validade.
> - **C)** Incorreta. O art. 37, IV veda expressamente a preterição de candidatos de concurso válido.
> - **D)** Incorreta. Súmula Vinculante nº 44 do STF: exigência de limite de idade só é válida se prevista expressamente em lei e justificada pela natureza das atribuições do cargo.
> - **E)** Incorreta. Cargos efetivos em universidades exigem compulsoriamente concurso público.
> 
> **Gabarito: A**

---

### Questão 10 (FCC - Adaptada / TCE-GO - Analista de Controle Externo)
No processo seletivo de pessoas, as técnicas de seleção devem apresentar dois requisitos psicométricos e metodológicos indispensáveis: **Validade** e **Confiabilidade (Fidedignidade)**.

Diz-se que uma técnica ou teste de seleção possui alta **Validade** quando:

* **A)** Mede com precisão exata aquilo que se propõe a medir e possui alto poder preditivo de prognosticar o desempenho futuro real do candidato no exercício do cargo.
* **B)** Produz sempre as mesmas notas numéricas quando aplicada repetidas vezes à mesma pessoa em dias consecutivos.
* **C)** Apresenta o menor custo financeiro de aplicação em relação ao orçamento disponível do departamento de recursos humanos.
* **D)** É aplicada exclusivamente por meio de questionários digitais anônimos na internet.
* **E)** Elimina mais de 90% dos candidatos na primeira etapa eliminatória.

> **Comentário Detalhado:**
>
> - **A)** Correta. Em psicometria e seleção de pessoal: **Validade** é o grau em que o instrumento mede realmente o traço ou competência que pretende medir e a sua capacidade preditiva de antecipar o sucesso do candidato no cargo; já a **Confiabilidade (ou Fidedignidade)** é a consistência e reprodutibilidade dos resultados (aplicado várias vezes à mesma pessoa, gera pontuações semelhantes).
> - **B)** Incorreta. Conceito referente à **Confiabilidade / Fidedignidade**.
> - **C)** Incorreta. Refere-se à economicidade do processo seletivo.
> - **D), E)** Incorretas. Distorções procedimentais sem relação com o conceito psicométrico de validade.
> 
> **Gabarito: A**

---

"""

    anchor_3 = "### 3. Rotinas Administrativas do Departamento de Pessoal no Setor Público"
    anchor_5 = "### 5. O Concurso Público como Instrumento Republicano (CF/88, art. 37)"
    anchor_6 = "### 6. Processo de Socialização e Integração Organizacional (*Onboarding*)"
    anchor_fontes = "### 7. Fontes Oficiais e Referências Bibliográficas"

    text = text.replace(anchor_3, q06 + "\n" + anchor_3)
    text = text.replace(anchor_5, q07 + "\n" + anchor_5)
    text = text.replace(anchor_6, q08 + "\n" + anchor_6)
    text = text.replace(anchor_fontes, q09_10 + "\n" + anchor_fontes)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    print("Enriched File 25/01 successfully! Total: 10 questions.")


def enrich_file_02():
    filepath = os.path.join(BASE_DIR, "02_treinamento_desenvolvimento_aprendizagem_e_gestao_do_conhecimento.md")
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    if "### Questão 06" in text:
        print("File 02 already enriched.")
        return

    q06 = """### Questão 06 (FCC - Adaptada / Analista de Gestão Pública)
Na gestão de pessoas, **Treinamento** e **Desenvolvimento de Pessoas (T&D)** são processos distintos, embora complementares.

A distinção conceitual precisa entre Treinamento e Desenvolvimento reside em:

* **A)** O treinamento tem foco no curto prazo e visa capacitar o indivíduo para o desempenho eficaz de suas funções e tarefas no cargo atual; enquanto o desenvolvimento foca o médio e longo prazo, visando ao crescimento integral do potencial humano e à preparação do servidor para desafios, papéis e cargos futuros.
* **B)** O treinamento é privativo de cargos comissionados e o desenvolvimento é restrito a servidores estagiários.
* **C)** O treinamento não pode utilizar tecnologias digitais e o desenvolvimento é sempre presencial em sala de aula.
* **D)** O treinamento extingue a necessidade de avaliação de desempenho funcional posterior.
* **E)** O desenvolvimento visa unicamente à redução salarial em situações de limite prudencial da LRF.

> **Comentário Detalhado:**
>
> - **A)** Correta. Diferenciação clássica: **Treinamento**: curto prazo, focado nas exigências técnicas imediatas do cargo atual, adaptando o servidor às rotinas de hoje; **Desenvolvimento**: longo prazo, visa à ampliação de competências globais, liderança, visão holística e crescimento pessoal para carreiras e posições futuras.
> - **B), C), D), E)** Incorretas. Distorções sem embasamento na literatura de gestão de pessoas.
> 
> **Gabarito: A**

---

"""

    q07 = """### Questão 07 (FCC - Adaptada / Auditor de Controle Externo)
Donald Kirkpatrick concebeu o modelo mais utilizado internacionalmente para avaliação da eficácia de programas de capacitação, estruturado em quatro níveis sucessivos de impacto.

O **Nível 3 (Comportamento no Cargo / Aplicação)** do modelo de Kirkpatrick avalia:

* **A)** O grau em que os participantes efetivamente transferiram e aplicaram os novos conhecimentos, habilidades e atitudes no seu dia a dia profissional real após o retorno ao local de trabalho.
* **B)** A satisfação imediata dos participantes com as instalações físicas, a pontualidade e o coffee-break do evento.
* **C)** O aumento formal de retenção de conceitos verificado por meio de prova teórica aplicada ao final da aula.
* **D)** O cálculo monetário estrito do retorno financeiro sobre o investimento (*ROI*) obtido pelo Tesouro Estadual.
* **E)** A pontualidade da entrega do diploma de conclusão emitido pelo órgão realizador.

> **Comentário Detalhado:**
>
> - **A)** Correta. Os 4 níveis de Kirkpatrick: (1) **Reação**: satisfação e percepção imediata dos alunos com o curso; (2) **Aprendizado**: retenção teórica e assimilação de conhecimentos (testes no fim do curso); (3) **Comportamento (Aplicação/Transferência)**: se os novos conhecimentos são efetivamente aplicados na prática do trabalho real; (4) **Resultados**: impacto final produzido nos indicadores e objetivos estratégicos da organização. Jack Phillips adicionou o 5º nível: ROI.
> - **B)** Incorreta. Refere-se ao Nível 1 (Reação).
> - **C)** Incorreta. Refere-se ao Nível 2 (Aprendizado).
> - **D)** Incorreta. Refere-se ao Nível 5 (ROI de Phillips) ou Nível 4 (Resultados).
> - **E)** Incorreta. Trâmite meramente burocrático de certificação.
> 
> **Gabarito: A**

---

"""

    q08 = """### Questão 08 (FCC - Adaptada / Analista de Tecnologia e Controle)
Ikujiro Nonaka e Hirotaka Takeuchi desenvolveram o consagrado modelo **SECI** para explicar a criação e a conversão do conhecimento organizacional através da interação entre o conhecimento tácito e o conhecimento explícito.

A modalidade de conversão do conhecimento que consiste em transformar o **conhecimento tácito em conhecimento explícito** (por exemplo, quando um auditor experiente redige um manual detalhado de auditoria de obras sistematizando seus anos de intuição e prática para toda a equipe) é a:

* **A)** Externalização.
* **B)** Socialização.
* **C)** Combinação.
* **D)** Internalização.
* **E)** Desintermediação.

> **Comentário Detalhado:**
>
> - **A)** Correta. As quatro formas de conversão do modelo SECI: (1) **Socialização** (Tácito para Tácito): compartilhamento de experiências e observação direta; (2) **Externalização** (Tácito para Explícito): articulação do saber tácito em conceitos, modelos, manuais e regras escritas; (3) **Combinação** (Explícito para Explícito): junção, edição e sistematização de diferentes bases de dados e documentos; (4) **Internalização** (Explícito para Tácito): assimilação do conhecimento documentado na rotina mental prática (*learning by doing*).
> - **B), C), D)** Incorretas. Representam as outras etapas de conversão do modelo SECI.
> - **E)** Incorreta. Conceito econômico de exclusão de intermediários.
> 
> **Gabarito: A**

---

"""

    q09_10 = """### Questão 09 (FCC - Adaptada / TCE-PI - Auditor de Controle Externo)
Na obra clássica *A Quinta Disciplina*, Peter Senge apresenta os fundamentos necessários para a construção de organizações que aprendem (*learning organizations*).

A disciplina que Senge considera a "pedra angular" e a mais integradora de todas, por permitir que os gestores enxerguem as inter-relações e os padrões de mudança sistêmicos em vez de eventos estáticos e isolados, é o:

* **A)** Pensamento Sistêmico.
* **B)** Domínio Pessoal.
* **C)** Modelos Mentais.
* **D)** Visão Compartilhada.
* **E)** Aprendizado em Equipe.

> **Comentário Detalhado:**
>
> - **A)** Correta. Peter Senge formulou cinco disciplinas: Domínio Pessoal, Modelos Mentais, Visão Compartilhada, Aprendizagem em Equipe e **Pensamento Sistêmico**. O Pensamento Sistêmico é a quinta disciplina que integra todas as outras, permitindo enxergar as causas profundas e as estruturas interdependentes em vez de sintomas superficiais de problemas.
> - **B), C), D), E)** Incorretas. São as outras quatro disciplinas que são potencializadas pelo pensamento sistêmico.
> 
> **Gabarito: A**

---

### Questão 10 (FCC - Adaptada / TCE-GO - Analista de Controle Externo)
No modelo de aprendizagem organizacional de Chris Argyris e Donald Schön, a **Aprendizagem de Circuito Duplo** (*Double-Loop Learning*) ocorre quando a organização:

* **A)** Questiona e modifica os valores, premissas fundamentais, normas e políticas subjacentes que definem as metas da instituição, em vez de apenas corrigir erros superficiais mantendo as regras inalteradas.
* **B)** Repete as mesmas tarefas rotineiras duas vezes para garantir conformidade contábil.
* **C)** Exige que dois auditores assinem conjuntamente o mesmo relatório preliminar.
* **D)** Mantém os procedimentos tradicionais inalterados independentemente de variações no ambiente externo.
* **E)** Contrata duas consultorias externas concorrentes para emitir pareceres conflitantes.

> **Comentário Detalhado:**
>
> - **A)** Correta. Distinção essencial: **Circuito Simples (*Single-Loop*)**: a organização detecta o erro e o corrige sem alterar as regras e objetivos vigentes (adaptação mecânica); **Circuito Duplo (*Double-Loop*)**: a instituição vai à raiz do problema e questiona as próprias premissas, normas, valores e paradigmas que balizam o plano de ação, reestruturando a lógica operacional.
> - **B), C), D), E)** Incorretas. Interpretações literais errôneas da expressão "circuito duplo".
> 
> **Gabarito: A**

---

"""

    anchor_2 = "### 2. O Ciclo de Treinamento em Quatro Etapas e a Avaliação de Kirkpatrick"
    anchor_3 = "### 3. Gestão do Conhecimento Organizacional e o Modelo SECI"
    anchor_4 = "### 4. Aprendizagem Organizacional e as Cinco Disciplinas de Peter Senge"
    anchor_fontes = "### 6. Fontes Oficiais e Referências Bibliográficas"

    text = text.replace(anchor_2, q06 + "\n" + anchor_2)
    text = text.replace(anchor_3, q07 + "\n" + anchor_3)
    text = text.replace(anchor_4, q08 + "\n" + anchor_4)
    text = text.replace(anchor_fontes, q09_10 + "\n" + anchor_fontes)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    print("Enriched File 25/02 successfully! Total: 10 questions.")


def enrich_file_03():
    filepath = os.path.join(BASE_DIR, "03_avaliacao_de_desempenho_remuneracao_qvt_e_teletrabalho.md")
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    if "### Questão 06" in text:
        print("File 03 already enriched.")
        return

    q06 = """### Questão 06 (FCC - Adaptada / Analista de Gestão Pública)
Dentre as metodologias clássicas e modernas de Avaliação de Desempenho Humano nas organizações, a **Avaliação 360 Graus (ou Feedback Circular / Multirrequisital)** caracteriza-se por:

* **A)** Coletar avaliações estruturadas sobre o desempenho do colaborador provenientes de todas as direções de relacionamento: do superior hierárquico, dos pares de trabalho (colegas), dos subordinados, dos clientes/usuários externos e da autoavaliação do próprio servidor.
* **B)** Basear-se exclusivamente no julgamento autocrático e secreto do chefe imediato da repartição.
* **C)** Classificar os servidores por meio de uma curva forçada em que obrigatoriamente 20% são classificados como insuficientes.
* **D)** Avaliar apenas aspectos relacionados à pontualidade de registro do ponto biométrico eletrônico.
* **E)** Limitar-se à medição de força física e aptidão cardiorrespiratória dos novos contratados.

> **Comentário Detalhado:**
>
> - **A)** Correta. A **Avaliação 360 Graus** proporciona visão holística e rica do colaborador, coletando feedback de todos os agentes que interagem com ele: chefe imediato, subordinados diretos, pares de equipe, clientes internos/externos e a própria autoavaliação.
> - **B)** Incorreta. Refere-se à avaliação tradicional unilateral por superior hierárquico (90 graus).
> - **C)** Incorreta. Refere-se ao método da distribuição forçada (*forced distribution*).
> - **D), E)** Incorretas. Distorções que não representam o escopo da avaliação 360 graus.
> 
> **Gabarito: A**

---

"""

    q07 = """### Questão 07 (FCC - Adaptada / Auditor de Controle Externo)
No processo de Avaliação de Desempenho, o avaliador está sujeito a vieses cognitivos e distorções perceptivas involuntárias que podem comprometer a fidedignidade dos resultados.

A distorção conhecida como **Efeito de Halo (ou Halo Effect)** ocorre quando:

* **A)** O avaliador generaliza uma única característica marcante (positiva ou negativa) do avaliado para julgar de forma contaminada todos os demais fatores e competências de seu desempenho.
* **B)** O avaliador atribui notas medianas a todos os avaliados para evitar conflitos interpessoais (*tendência central*).
* **C)** O avaliador considera apenas os fatos ocorridos na última semana antes da avaliação, esquecendo o restante do ano (*efeito de recência*).
* **D)** O avaliador avalia melhor os indivíduos que possuem perfil, origens e opiniões semelhantes às suas (*erro de semelhança*).
* **E)** O avaliador é excessivamente rigoroso com todos os seus subordinados (*severidade excessiva*).

> **Comentário Detalhado:**
>
> - **A)** Correta. O **Efeito de Halo** (ou Efeito Horn, quando negativo) é a contaminação generalizada da avaliação por um único traço saliente: se o servidor é muito simpático ou pontual, o chefe presume precipitadamente que ele é ótimo em todas as demais competências (planejamento, rigor técnico, redação).
> - **B)** Incorreta. Refere-se ao vício de **Tendência Central**.
> - **C)** Incorreta. Refere-se ao erro de **Recência**.
> - **D)** Incorreta. Refere-se ao viés de **Semelhança** (*similar-to-me*).
> - **E)** Incorreta. Refere-se ao vício de **Severidade/Rigor excessivo**.
> 
> **Gabarito: A**

---

"""

    q08 = """### Questão 08 (FCC - Adaptada / Analista de Planejamento e Controle)
No estudo da Qualidade de Vida no Trabalho (QVT), o modelo conceitual mais abrangente e citado na literatura administrativa foi proposto por Richard Walton (1973), estruturado em oito dimensões clássicas.

Constitui uma das oito dimensões do modelo de QVT de **Richard Walton**:

* **A)** Constitucionalismo na Organização (respeito aos direitos dos trabalhadores, privacidade, liberdade de expressão e normas de equidade no trabalho).
* **B)** Remuneração salarial indexada exclusivamente à variação cambial do dólar americano.
* **C)** Proibição de concessão de férias e licenças no primeiro ano do mandato do governador.
* **D)** Instauração obrigatória de sindicância sumária em qualquer alteração de rotina.
* **E)** Exigência de cumprimento de horas extras diárias de forma compulsória sem descanso semanal.

> **Comentário Detalhado:**
>
> - **A)** Correta. As 8 dimensões de QVT de Walton: (1) Compensação justa e adequada; (2) Condições de trabalho seguras e saudáveis; (3) Uso e desenvolvimento de capacidades; (4) Oportunidade de crescimento contínuo e segurança; (5) Integração social na organização; (6) **Constitucionalismo na organização** (direitos, privacidade, contraditório); (7) Trabalho e o espaço total de vida (equilíbrio trabalho-família); (8) Relevância social do trabalho na sociedade.
> - **B), C), D), E)** Incorretas. Distorções que violam os preceitos de bem-estar e dignidade do trabalho.
> 
> **Gabarito: A**

---

"""

    q09_10 = """### Questão 09 (FCC - Adaptada / TCE-PI - Auditor de Controle Externo)
Com a regulamentação do teletrabalho e do trabalho híbrido no serviço público brasileiro (Decreto Federal nº 11.072/2022 - Programa de Gestão e Desempenho e normativos do TCE-GO), a dinâmica da gestão funcional passou por transformações estruturais.

No regime de teletrabalho regulamentado pelo poder público, a gestão do servidor público fundamenta-se prioritariamente:

* **A)** No acompanhamento de entregas, metas de produtividade pactuadas formalmente em plano de trabalho individual e resultados acordados, em substituição ao controle puramente físico e cronológico de frequência e assiduidade por ponto eletrônico.
* **B)** No monitoramento contínuo da imagem do servidor por câmera de vigilância durante oito horas ininterruptas.
* **C)** Na proibição total de comparecimento do servidor às dependências físicas do Tribunal de Contas sob pena de demissão.
* **D)** Na redução proporcional de 50% de seus vencimentos básicos em virtude da ausência no prédio público.
* **E)** Na transferência integral da responsabilidade fiscal do órgão para o servidor teletrabalhador.

> **Comentário Detalhado:**
>
> - **A)** Correta. A transição trazida pelos Programas de Gestão e Desempenho (PGD) e resoluções do setor público: o controle migra da lógica clássica de "presença e controle de horas no ponto" para a **gestão por resultados e cumprimento de metas de entregas mensuráveis**, expressas em Planos de Trabalho com prazos e padrões de qualidade definidos.
> - **B), C), D), E)** Incorretas. Posturas ilegais ou distorcidas que violam a regulamentação do teletrabalho no setor público.
> 
> **Gabarito: A**

---

### Questão 10 (FCC - Adaptada / TCE-GO - Analista de Controle Externo)
No tocante à estrutura do Sistema de Remuneração no Setor Público e aos Planos de Cargos, Carreiras e Vencimentos (PCCV), a contraprestação pecuniária mensal devida ao servidor pelo efetivo exercício do cargo público, fixada em lei, desprovida de quaisquer adicionais ou gratificações, denomina-se:

* **A)** Vencimento básico (ou padrão).
* **B)** Remuneração integral.
* **C)** Diária de deslocamento eventual.
* **D)** Ajuda de custo para transferência de domicílio.
* **E)** Indenização de transporte funcional.

> **Comentário Detalhado:**
>
> - **A)** Correta. Distinção essencial estatutária (Lei Estadual nº 20.756/2020 e Lei Federal nº 8.112/1990): **Vencimento básico** é a retribuição pecuniária básica fixada em lei devida pelo exercício do cargo; **Remuneração** é o vencimento básico acrescido das vantagens pecuniárias permanentes (adicionais e gratificações) estabelecidas em lei.
> - **B)** Incorreta. Remuneração inclui vencimento mais vantagens adicionais.
> - **C), D), E)** Incorretas. São parcelas de caráter puramente indenizatório, não salarial.
> 
> **Gabarito: A**

---

"""

    anchor_2 = "### 2. Erros, Vieses e Distorções Cognitivas do Avaliador"
    anchor_3 = "### 3. Remuneração e Planos de Carreira no Setor Público"
    anchor_4 = "### 4. Qualidade de Vida no Trabalho (QVT): Modelo de Richard Walton"
    anchor_fontes = "### 6. Fontes Oficiais e Referências Bibliográficas"

    text = text.replace(anchor_2, q06 + "\n" + anchor_2)
    text = text.replace(anchor_3, q07 + "\n" + anchor_3)
    text = text.replace(anchor_4, q08 + "\n" + anchor_4)
    text = text.replace(anchor_fontes, q09_10 + "\n" + anchor_fontes)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    print("Enriched File 25/03 successfully! Total: 10 questions.")


def enrich_file_04():
    filepath = os.path.join(BASE_DIR, "04_estatuto_dos_servidores_do_estado_de_goias_lei_20756.md")
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    if "### Questão 06" in text:
        print("File 04 already enriched.")
        return

    q06 = """### Questão 06 (FCC – Inédita – Padrão TCE-GO)
De acordo com a Lei Estadual nº 20.756/2020 (Regime Jurídico dos Servidores Públicos Civis do Estado de Goiás), a respeito dos prazos legais do ciclo de investidura (posse e exercício), assinale a afirmativa correta:

* **A)** A posse dar-se-á no prazo improrrogável de 30 (trinta) dias contados da publicação oficial do ato de provimento (nomeação), e o servidor terá o prazo de 15 (quinze) dias, contados da data da posse, para entrar em efetivo exercício.
* **B)** A posse deve ocorrer em até 90 dias úteis e o exercício inicia-se compulsoriamente no mesmo dia da posse.
* **C)** Caso o nomeado não tome posse no prazo legal, ser-lhe-á concedida licença não remunerada automática de três meses.
* **D)** O servidor empossado que não entrar em exercício no prazo legal será sumariamente demitido a bem do serviço público mediante processo disciplinar.
* **E)** A posse é exigida para cargos efetivos, mas é expressamente dispensada para cargos em comissão e funções de confiança.

> **Comentário Detalhado:**
>
> - **A)** Correta. Prazos expressos da Lei Estadual nº 20.756/2020: **Posse**: 30 dias contados da publicação da nomeação (art. 21); **Exercício**: 15 dias contados da data da posse (art. 28). Se não tomar posse em 30 dias, o ato de nomeação torna-se **sem efeito**; se tomar posse mas não entrar em exercício em 15 dias, o servidor é **exonerado**.
> - **B)** Incorreta. Prazos em desacordo com o estatuto goiano.
> - **C)** Incorreta. Não há concessão de licença; a nomeação torna-se sem efeito.
> - **D)** Incorreta. Como o servidor já tomou posse mas não entrou em exercício, a consequência legal é a **exoneração**, e não demissão (demissão é sanção disciplinar punitiva).
> - **E)** Incorreta. Cargos em comissão também exigem formalização do termo de posse.
> 
> **Gabarito: A**

---

"""

    q07 = """### Questão 07 (FCC – Inédita – Padrão TCE-GO)
No regime estatutário do Estado de Goiás (Lei nº 20.756/2020), o servidor público estável que tiver sua demissão invalidada por decisão judicial ou administrativa irrecorrível terá direito ao instituto da:

* **A)** Reintegração, com o ressarcimento integral de todos os vencimentos, direitos e vantagens funcionais que deixou de auferir durante o período do afastamento ilegal.
* **B)** Recondução sumária sem pagamento de parcelas financeiras retroativas em atendimento à responsabilidade fiscal.
* **C)** Readaptação em cargo compatível com sua nova limitação física ou psíquica atestada em junta médica.
* **D)** Reversão compulsória no interesse exclusivo do serviço público da entidade autárquica.
* **E)** Aproveitamento prioritário em cargo de atribuições e remuneração inferiores.

> **Comentário Detalhado:**
>
> - **A)** Correta. A **Reintegração** (art. 41, § 2º da CF/88 e arts. 50 a 52 da Lei Estadual nº 20.756/2020) é o retorno do servidor público estável ao cargo anteriormente ocupado quando sua demissão for invalidada por sentença judicial ou decisão administrativa, assistindo-lhe direito ao **ressarcimento integral** de todas as vantagens pecuniárias e funcionais retroativas.
> - **B)** Incorreta. Recondução é o retorno do servidor estável ao cargo anterior em razão de inabilitação em estágio probatório ou reintegração do titular.
> - **C)** Incorreta. Readaptação decorre de limitação na capacidade física ou mental.
> - **D)** Incorreta. Reversão é o retorno do aposentado ao serviço ativo.
> - **E)** Incorreta. O aproveitamento deve ser em cargo de atribuições e vencimentos compatíveis.
> 
> **Gabarito: A**

---

"""

    q08 = """### Questão 08 (FCC – Inédita – Padrão TCE-GO)
Acerca do regime de férias remuneradas disciplinado pela Lei Estadual nº 20.756/2020 dos Servidores Públicos Civis de Goiás, é correto afirmar:

* **A)** As férias anuais de 30 (trinta) dias poderão ser parceladas em até 3 (três) períodos, por solicitação do servidor e interesse da administração, desde que nenhum deles seja inferior a 10 (dez) dias corridos.
* **B)** É obrigatória a conversão em dinheiro (venda) de pelo menos 50% do período de férias dos servidores de controle externo.
* **C)** O servidor tem direito a férias no seu primeiro ano de serviço sem a necessidade de cumprimento de qualquer período aquisitivo inicial.
* **D)** O adicional constitucional de férias no Estado de Goiás é pago à razão de metade (50%) da remuneração do mês de gozo.
* **E)** É proibida a acumulação de férias sob qualquer pretexto, extinguindo-se o direito caso o servidor não usufrua o descanso até o fim do ano civil.

> **Comentário Detalhado:**
>
> - **A)** Correta. Nos exatos termos do art. 132 da Lei nº 20.756/2020: as férias poderão ser parceladas em até **3 etapas**, a pedido do servidor e no interesse da Administração, sendo exigido que cada período tenha a duração mínima de **10 dias consecutivos**.
> - **B)** Incorreta. Não há obrigatoriedade de conversão pecuniária de férias.
> - **C)** Incorreta. O primeiro período aquisitivo exige 12 meses de efetivo exercício.
> - **D)** Incorreta. O adicional constitucional é de 1/3 (um terço) da remuneração, conforme art. 7º, XVII da CF/88.
> - **E)** Incorreta. É permitida a acumulação de até no máximo 2 períodos de férias no caso de imperiosa necessidade do serviço.
> 
> **Gabarito: A**

---

"""

    q09_10 = """### Questão 09 (FCC – Inédita – Padrão TCE-GO)
Em matéria de responsabilidade funcional e penalidades disciplinares no Estatuto dos Servidores Públicos Civis de Goiás (Lei nº 20.756/2020), considere a seguinte infração:

Determinado servidor efetivo do Estado de Goiás cometeu ato de incontinência pública ou conduta escandalosa na repartição que perturbou a ordem dos serviços e causou grave dano moral à imagem da instituição.

À luz da gradação disciplinar da Lei Estadual nº 20.756/2020, a referida conduta constitui falta punível originariamente com a penalidade de:

* **A)** Suspensão de até 90 (noventa) dias.
* **B)** Advertência verbal informal aplicada sem registro nos assentamentos funcionais.
* **C)** Cassação imediata de proventos de aposentadoria de parente consanguíneo.
* **D)** Perda definitiva dos direitos políticos por decisão da comissão processante de sindicância.
* **E)** Prisão administrativa em cela especial da polícia judiciária estadual.

> **Comentário Detalhado:**
>
> - **A)** Correta. Na disciplina dos arts. 192 e seguintes da Lei nº 20.756/2020: faltas mais graves que reincidência de advertência, incontinência pública ou conduta escandalosa no ambiente de trabalho sujeitam o servidor à pena de **Suspensão** por até 90 dias, cancelando a remuneração durante o afastamento.
> - **B)** Incorreta. A advertência é por escrito e registrada nos assentamentos funcionais, aplicável a infrações de menor gravidade.
> - **C), D), E)** Incorretas. Penas absurdas, ilegais ou manifestamente inconstitucionais (prisão administrativa foi abolida; perda de direitos políticos só ocorre em trânsito em julgado judicial).
> 
> **Gabarito: A**

---

### Questão 10 (FCC – Inédita – Padrão TCE-GO)
Quanto aos prazos de prescrição da pretensão punitiva disciplinar da Administração Pública estadual previstos na Lei Estadual nº 20.756/2020, a ação disciplinar prescreve em:

* **A)** 5 (cinco) anos, quanto às infrações puníveis com demissão, cassação de aposentadoria ou disponibilidade e destituição de cargo em comissão; 2 (dois) anos, quanto às puníveis com suspensão; e 180 (cento e oitenta) dias, quanto às puníveis com advertência.
* **B)** 10 anos para qualquer penalidade funcional, respeitada a prescrição civil do Código Civil.
* **C)** 30 dias para todas as penalidades, a contar da prática do ato faltoso.
* **D)** Prazo imprescritível em se tratando de infrações disciplinares cometidas por servidores de controle externo.
* **E)** 1 ano para demissão e 5 anos para advertência escrita.

> **Comentário Detalhado:**
>
> - **A)** Correta. É a disciplina clássica dos prazos prescricionais estatutários consolidados no art. 202 da Lei Estadual nº 20.756/2020: **5 anos**: faltas puníveis com demissão, cassação de aposentadoria/disponibilidade e destituição de cargo comissionado; **2 anos**: faltas puníveis com suspensão; **180 dias**: faltas puníveis com advertência. O prazo inicia-se na data em que o fato se tornou conhecido pela autoridade competente.
> - **B), C), D), E)** Incorretas. Prazos em total desconformidade com o regime legal dos servidores do Estado de Goiás.
> 
> **Gabarito: A**

---

"""

    anchor_3 = "## 3. Estágio Probatório e Estabilidade Constitucional"
    anchor_4 = "## 4. Provimento Derivado e Vacância de Cargos Públicos"
    anchor_5 = "## 5. Direitos, Vantagens Pecuniárias e Licenças Estatutárias"
    anchor_fontes = "## 7. Fontes Oficiais e Referências Bibliográficas"

    text = text.replace(anchor_3, q06 + "\n" + anchor_3)
    text = text.replace(anchor_4, q07 + "\n" + anchor_4)
    text = text.replace(anchor_5, q08 + "\n" + anchor_5)
    text = text.replace(anchor_fontes, q09_10 + "\n" + anchor_fontes)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    print("Enriched File 25/04 successfully! Total: 10 questions.")


if __name__ == "__main__":
    enrich_file_01()
    enrich_file_02()
    enrich_file_03()
    enrich_file_04()
    print("Module 25 fully processed!")
