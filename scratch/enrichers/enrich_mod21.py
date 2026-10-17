# -*- coding: utf-8 -*-
"""
Enriquecedor Módulo 21 - Noções de Administração Pública
Arquivos: 01, 02, 03, 04
Adiciona de 5 a 6 questões por arquivo (Questões 06 a 10/11) com âncoras exatas.
"""

import os

BASE_DIR = "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/21_nocoes_de_administracao_publica"

def enrich_file_01():
    filepath = os.path.join(BASE_DIR, "01_organizacoes_formais_estruturas_e_processo_organizacional.md")
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    if "### Questão 06" in text:
        print("File 01 already enriched.")
        return

    q06 = """### Questão 06 (FCC - Adaptada / Analista de Gestão Pública)
No estudo das organizações formais e do processo administrativo clássico (PODC - Planejar, Organizar, Dirigir e Controlar), a função **Organização** compreende precipuamente:

* **A)** A distribuição de tarefas, a alocação criteriosa de recursos humanos e materiais entre os órgãos e a definição da estrutura de autoridade, responsabilidade e linhas de comunicação formal da instituição.
* **B)** A fixação dos objetivos corporativos de longo prazo e a escolha das estratégias mestras para alcançá-los.
* **C)** A motivação, orientação, liderança e coordenação interpessoal direta das equipes de trabalho no cotidiano operacional.
* **D)** A comparação sistemática entre os resultados obtidos e os padrões preestabelecidos, com aplicação de eventuais correções corretivas.
* **E)** A realização de auditorias financeiras externas de conformidade legal sobre os balanços patrimoniais.

> **Comentário Detalhado:**
>
> - **A)** Correta. A função **Organizar** diz respeito à modelagem da estrutura organizacional: divisão do trabalho, departamentalização, distribuição de recursos, delegação de autoridade e atribuição de responsabilidades.
> - **B)** Incorreta. Conceito referente à função de **Planejamento**.
> - **C)** Incorreta. Conceito referente à função de **Direção** (liderança, motivação e comunicação interpessoal).
> - **D)** Incorreta. Conceito referente à função de **Controle** (monitoramento e correção).
> - **E)** Incorreta. Procedimento de controle externo, e não da função gerencial interna de organização.
> 
> **Gabarito: A**

---

"""

    q07 = """### Questão 07 (FCC - Adaptada / Auditor de Controle Externo)
A respeito da amplitude administrativa (ou amplitude de controle) e dos níveis hierárquicos nas organizações formais, assinale a afirmativa correta:

* **A)** Uma amplitude de controle estreita (poucos subordinados por chefe) tende a produzir uma estrutura organizacional verticalizada (alongada), com múltiplos níveis hierárquicos e maior custo administrativo de supervisão.
* **B)** Uma estrutura organizacional achatada (plana) decorre necessariamente de amplitudes de controle muito reduzidas.
* **C)** Quanto maior o número de níveis hierárquicos em uma repartição pública, mais ágil e desprovida de distorções e ruídos torna-se a comunicação vertical ascendente.
* **D)** A amplitude de controle refere-se unicamente ao limite territorial de competência jurisdicional de uma corte de contas.
* **E)** A descentralização administrativa exige compulsoriamente a eliminação de qualquer amplitude de supervisão nos órgãos setoriais.

> **Comentário Detalhado:**
>
> - **A)** Correta. A **amplitude de controle** é o número de subordinados que um gestor pode supervisionar diretamente. Amplitude estreita gera estrutura verticalizada (*tall structure*), com mais níveis de comando e comunicação mais lenta.
> - **B)** Incorreta. Estrutura achatada decorre de amplitude **ampla/larga**.
> - **C)** Incorreta. Excesso de níveis alonga a cadeia de comando e amplifica ruídos.
> - **D)** Incorreta. Trata-se de variável da teoria da organização.
> - **E)** Incorreta. Descentralização delega decisões, mantendo supervisão.
> 
> **Gabarito: A**

---

"""

    q08 = """### Questão 08 (FCC - Adaptada / Analista de Planejamento e Gestão)
Em relação aos modelos de departamentalização das organizações formais, a estrutura **Matricial** diferencia-se dos modelos clássicos por:

* **A)** Sobrepor uma coordenação horizontal orientada a projetos ou produtos a uma estrutura vertical departamentalizada por funções, gerando dupla subordinação hierárquica para os membros das equipes.
* **B)** Basear-se exclusivamente no critério geográfico ou territorial, alocando todos os servidores em unidades regionais autônomas.
* **C)** Extinguir totalmente a especialização técnica dos servidores para transformá-los em operadores generalistas.
* **D)** Proibir a formação de equipes multidisciplinares temporárias em qualquer setor da Administração Pública.
* **E)** Impor rigidez funcional extrema que impede o compartilhamento de especialistas entre diferentes áreas do órgão.

> **Comentário Detalhado:**
>
> - **A)** Correta. A **estrutura matricial** combina departamentalização funcional com departamentalização por projetos/produtos, gerando a **dupla subordinação** (o servidor responde ao gerente funcional e ao gerente do projeto).
> - **B)** Incorreta. Refere-se à departamentalização geográfica.
> - **C)** Incorreta. Preserva especialização funcional com flexibilidade de projetos.
> - **D)** Incorreta. Essência da matriz é formar equipes multifuncionais.
> - **E)** Incorreta. Proporciona alto compartilhamento dinâmico de recursos.
> 
> **Gabarito: A**

---

"""

    q09_10 = """### Questão 09 (FCC - Adaptada / TCE-SC - Auditor de Controle Externo)
Na Administração Pública contemporânea, a distinção entre **Concentração/Desconcentração** e **Centralização/Descentralização** é basilar para a compreensão da estrutura estatal.

Sobre esses conceitos fundamentais, assinale a alternativa correta:

* **A)** A desconcentração envolve a distribuição interna de competências decisórias dentro de uma mesma pessoa jurídica (órgão público), mantendo-se a relação de subordinação hierárquica; já a descentralização consiste na transferência de competências para outra pessoa jurídica distinta (da Administração Indireta ou particular).
* **B)** A criação de uma autarquia estadual constitui típico exemplo de desconcentração administrativa sem personalidade jurídica própria.
* **C)** A criação de delegacias de polícia ou postos de atendimento ao cidadão em municípios do interior configura típica descentralização por outorga legal.
* **D)** A descentralização preserva a hierarquia direta e a subordinação disciplinar entre o Chefe do Executivo e os dirigentes das entidades privadas contratadas.
* **E)** A desconcentração enseja a extinção imediata do poder regulamentar do ente estatal matriz.

> **Comentário Detalhado:**
>
> - **A)** Correta. **Desconcentração** é interna (mesma pessoa jurídica, com hierarquia); **Descentralização** é externa (outra pessoa jurídica, sem hierarquia, apenas tutela/vinculação).
> - **B)** Incorreta. Criação de autarquia é descentralização administrativa.
> - **C)** Incorreta. Postos e delegacias são desconcentração.
> - **D)** Incorreta. Na descentralização inexiste subordinação hierárquica.
> - **E)** Incorreta. A desconcentração não afeta poderes estatais.
> 
> **Gabarito: A**

---

### Questão 10 (FCC - Adaptada / TCE-GO - Analista de Controle Externo)
No exercício da função administrativa de **Controle**, a literatura e a jurisprudência consagraram a classificação do controle governamental quanto ao momento de sua efetivação em: prévio (preventivo), concomitante e a posteriori (corretivo).

Constitui exemplo de controle governamental **prévio** (ou preventivo):

* **A)** O exame e homologação prévia de editais de licitação de grande vulto ou a concessão de tutela de urgência cautelar para suspender a assinatura de contrato com indícios de sobrepreço.
* **B)** A auditoria contábil operacional realizada pelo Tribunal de Contas após o encerramento do exercício sobre as despesas de Restos a Pagar.
* **C)** A instauração de Tomada de Contas Especial cinco anos após a execução irregular de um convênio de repasse.
* **D)** O julgamento formal das contas dos ordenadores de despesas referente ao ano financeiro pretérito.
* **E)** A cobrança judicial via execução fiscal dos valores de multas imputadas pelo Tribunal de Contas.

> **Comentário Detalhado:**
>
> - **A)** Correta. O **controle prévio/preventivo** atua antes da consumação ou produção de efeitos do ato (ex.: exame cautelar de editais licitatórios, vistorias preliminares, suspensão de assinatura de contratos).
> - **B)** Incorreta. Auditoria após encerramento do exercício é controle *a posteriori*.
> - **C)** Incorreta. TCE é procedimento corretivo/repressivo posterior.
> - **D)** Incorreta. Julgamento de contas é a posteriori.
> - **E)** Incorreta. Execução fiscal é coercitiva final.
> 
> **Gabarito: A**

---

"""

    anchor_2 = "### 2. Modelos de Estrutura Organizacional"
    anchor_3 = "### 3. Critérios de Departamentalização"
    anchor_4 = "### 4. O Processo Organizacional e as Funções Administrativas (PODC)"
    anchor_fontes = "## 🌐 Fontes Oficiais & Referências Bibliográficas"

    text = text.replace(anchor_2, q06 + "\n" + anchor_2)
    text = text.replace(anchor_3, q07 + "\n" + anchor_3)
    text = text.replace(anchor_4, q08 + "\n" + anchor_4)
    text = text.replace(anchor_fontes, q09_10 + "\n" + anchor_fontes)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    print("Enriched File 21/01 successfully! Total: 10 questions.")


def enrich_file_02():
    filepath = os.path.join(BASE_DIR, "02_modelos_de_administracao_publica_e_governanca.md")
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    if "### Questão 06" in text:
        print("File 02 already enriched.")
        return

    q06 = """### Questão 06 (FCC - Adaptada / Analista de Gestão Pública)
O modelo patrimonialista de Administração Pública prevaleceu no Brasil colonial e imperial, deixando traços na cultura organizacional do Estado.

Constitui traço característico definidor do **Patrimonialismo**:

* **A)** A incapacidade de distinção clara entre a *res publica* (o patrimônio público do Estado) e a *res principis* (o patrimônio pessoal e privado do soberano e dos governantes).
* **B)** A estrita impessoalidade nos processos de seleção e a instituição compulsória do mérito profissional aferido por concurso público aberto.
* **C)** O controle formal e rigoroso dos procedimentos operacionais estabelecido em manuais e regulamentos escritos padronizados.
* **D)** A ênfase na contratualização de resultados e no fornecimento de serviços orientados primordialmente ao cidadão-usuário.
* **E)** A transparência ativa sistemática proporcionada por portais de dados abertos na internet.

> **Comentário Detalhado:**
>
> - **A)** Correta. O **patrimonialismo** confunde o público e o privado: o soberano trata o Estado como extensão de seu patrimônio pessoal (nepotismo, clientelismo e prebendas).
> - **B)** Incorreta. Concurso e mérito são da burocracia weberiana.
> - **C)** Incorreta. Controle formal é o núcleo da burocracia.
> - **D)** Incorreta. Orientação ao cidadão-usuário é da administração gerencial (NPM).
> - **E)** Incorreta. Dados abertos são do Governo Digital contemporâneo.
> 
> **Gabarito: A**

---

"""

    q07 = """### Questão 07 (FCC - Adaptada / Auditor de Controle Externo)
Na teoria sociológica e administrativa, a Administração Pública Burocrática de Max Weber foi concebida para combater a corrupção e o nepotismo patrimonialista, baseando-se na legalidade, impessoalidade e formalismo. Todavia, a prática organizacional evidenciou as chamadas "disfunções da burocracia" (analisadas por Robert Merton).

Constitui uma típica **disfunção burocrática**:

* **A)** O apego exagerado às regras e aos procedimentos formais, fazendo com que as normas (que deveriam ser meios) se transformem nos próprios fins da ação administrativa (*internalização das regras*).
* **B)** A flexibilização excessiva de processos com delegação ampla de poderes decisórios aos funcionários da ponta.
* **C)** A priorização dos interesses estratégicos da sociedade em detrimento dos manuais internos de rotinas.
* **D)** A avaliação contínua da efetividade social das políticas públicas em substituição ao controle de conformidade legal.
* **E)** A descentralização territorial das decisões governamentais em prol de cooperativas locais.

> **Comentário Detalhado:**
>
> - **A)** Correta. Robert Merton identificou a **transposição de fins**, na qual regras e regulamentos (meios) tornam-se valores absolutos (fins em si mesmos), gerando lentidão e resistência a mudanças.
> - **B)** Incorreta. A burocracia clássica veda a flexibilização informal da ponta.
> - **C)** Incorreta. A disfunção faz esquecer a sociedade para focar só nas normas internas.
> - **D)** Incorreta. Foco em efetividade social é do gerencialismo.
> - **E)** Incorreta. A burocracia preza pela padronização centralizada.
> 
> **Gabarito: A**

---

"""

    q08 = """### Questão 08 (FCC - Adaptada / TCE-PI - Auditor de Controle Externo)
A Reforma do Aparelho do Estado de 1995 (Plano Diretor da Reforma do Aparelho do Estado - PDRAE), liderada pelo MARE, estruturou a atuação governamental em quatro setores estratégicos.

O setor do Estado que executa as funções exclusivas que envolvem o uso do poder extroverso e de polícia estatal (legislar, julgar, fiscalizar, arrecadar tributos e exercer o controle externo), sendo vedado à terceirização e à delegação a entidades privadas, é denominado pelo PDRAE:

* **A)** Núcleo Estratégico.
* **B)** Atividades Exclusivas de Estado.
* **C)** Serviços Não Exclusivos.
* **D)** Produção de Bens e Serviços para o Mercado.
* **E)** Setor Não Lucrativo de Fomento Societário.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O Núcleo Estratégico formula leis e políticas públicas (Cúpula).
> - **B)** Correta. O setor de **Atividades Exclusivas de Estado** engloba polícia, arrecadação, regulação e controle externo (Tribunais de Contas), indelegáveis a entidades particulares.
> - **C)** Incorreta. Serviços Não Exclusivos (saúde, educação) podem ser compartilhados com Organizações Sociais.
> - **D)** Incorreta. Produção para o mercado (estatais econômicas) opera sob concorrência.
> - **E)** Incorreta. Categoria inexistente no PDRAE.
> 
> **Gabarito: B**

---

"""

    q09_10 = """### Questão 09 (FCC - Adaptada / TCE-SC - Auditor de Controle Externo)
No campo da Nova Governança Pública e do combate à corrupção, o conceito de *Accountability* desdobra-se em diferentes dimensões fundamentais na relação entre governantes, sociedade e instituições fiscalizadoras.

Assinale a opção que define corretamente a **Accountability Horizontal**:

* **A)** É a mútua fiscalização e controle exercido entre os Poderes e órgãos públicos autônomos de mesmo patamar ou órgãos de controle especializado (como o controle exercido pelo Tribunal de Contas sobre o Poder Executivo ou pelo Ministério Público).
* **B)** É o controle direto exercido pelos cidadãos sobre os governantes exclusivamente por meio do voto periódico nas eleições democráticas.
* **C)** É a fiscalização informal exercida pela imprensa, meios de comunicação e movimentos sociais civis.
* **D)** É a subordinação hierárquica e disciplinar obrigatória de servidores subalternos perante suas chefias imediatas.
* **E)** É a transferência contratual de serviços de saúde para Organizações Sociais qualificadas pelo Executivo.

> **Comentário Detalhado:**
>
> - **A)** Correta. **Accountability Horizontal** (Guillermo O'Donnell): controle mútuo institucional entre poderes e órgãos de controle (Legislativo, Tribunais de Contas, Judiciário e MP - freios e contrapesos); **Vertical**: cidadãos sobre governantes via voto; **Social**: mídia e ONGs.
> - **B)** Incorreta. Refere-se à *Accountability Vertical*.
> - **C)** Incorreta. Refere-se à *Accountability Social*.
> - **D)** Incorreta. Trata-se de hierarquia administrativa.
> - **E)** Incorreta. Publicização de serviços públicos.
> 
> **Gabarito: A**

---

### Questão 10 (FCC - Adaptada / TCE-GO - Analista de Controle Externo)
O Decreto Federal nº 9.203/2017 dispõe sobre a política de governança da administração pública federal e define conceitos e diretrizes fundamentais também recepcionados pelos órgãos de controle estaduais (TCE-GO).

De acordo com as boas práticas de governança no setor público, a distinção entre **Governança** e **Gestão** reside essencialmente em:

* **A)** A governança compreende os mecanismos de liderança, estratégia e controle postos em prática para avaliar, direcionar e monitorar a gestão, visando à condução de políticas públicas e à prestação de serviços de interesse da sociedade; enquanto a gestão é responsável pelo planejamento, execução, operação e entrega cotidiana das ações e projetos definidos pela governança.
* **B)** A gestão é prerrogativa exclusiva do Poder Judiciário e a governança é função própria dos órgãos burocráticos municipais.
* **C)** A governança e a gestão são sinônimos perfeitos na teoria administrativa contemporânea, inexistindo distinção prática ou normativa entre os termos.
* **D)** A governança atua estritamente na fase de compra e liquidação contábil de bens e a gestão cuida da edição de medidas provisórias pelo Presidente da República.
* **E)** A governança afasta a necessidade de controles internos e auditorias para permitir total liberdade aos gestores operacionais.

> **Comentário Detalhado:**
>
> - **A)** Correta. Decreto nº 9.203/2017: **Governança** (*Avaliar, Direcionar e Monitorar* - liderança e estratégia da alta direção); **Gestão** (*Planejar, Executar e Controlar* - operação cotidiana dos gerentes e equipes).
> - **B), C), D), E)** Incorretas. Distorções conceituais dos papéis de governança e gestão.
> 
> **Gabarito: A**

---

"""

    anchor_2 = "### 2. As Disfunções da Burocracia (Robert Merton)"
    anchor_3 = "### 3. A Reforma Gerencial Brasileira de 1995 (PDRAE)"
    anchor_4 = "### 4. As Dimensões do Desempenho Público (Os 6Es da Gestão)"
    anchor_fontes = "## 🌐 Fontes Oficiais & Referências Bibliográficas"

    text = text.replace(anchor_2, q06 + "\n" + anchor_2)
    text = text.replace(anchor_3, q07 + "\n" + anchor_3)
    text = text.replace(anchor_4, q08 + "\n" + anchor_4)
    text = text.replace(anchor_fontes, q09_10 + "\n" + anchor_fontes)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    print("Enriched File 21/02 successfully! Total: 10 questions.")


def enrich_file_03():
    filepath = os.path.join(BASE_DIR, "03_gestao_da_qualidade_processos_projetos_e_decreto_9094.md")
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    if "### Questão 06" in text:
        print("File 03 already enriched.")
        return

    q06 = """### Questão 06 (FCC - Adaptada / Analista de Planejamento e Gestão)
O Ciclo PDCA (desenvolvido por Walter Shewhart e amplamente disseminado por W. Edwards Deming) constitui metodologia clássica de melhoria contínua de processos organizacionais.

A etapa do ciclo em que a organização analisa e avalia sistematicamente as diferenças entre os resultados executados e as metas planejadas, identificando causas de variações para adoção de medidas saneadoras, denomina-se:

* **A)** Check (Verificar / Checar).
* **B)** Plan (Planejar).
* **C)** Do (Executar / Fazer).
* **D)** Act (Agir corretivamente / Padronizar).
* **E)** Decide (Decidir discricionariamente).

> **Comentário Detalhado:**
>
> - **A)** Correta. No ciclo **PDCA**: **Plan** (planejar metas); **Do** (executar); **Check** (checar/verificar resultados frente às metas e identificar desvios); **Act** (agir corretivamente e padronizar).
> - **B)** Incorreta. Planejar é fixação inicial.
> - **C)** Incorreta. Executar é implementação.
> - **D)** Incorreta. Agir é correção definitiva e padronização.
> - **E)** Incorreta. Fase inexistente no modelo.
> 
> **Gabarito: A**

---

"""

    q07 = """### Questão 07 (FCC - Adaptada / Auditor de Controle Externo)
Na Gestão de Processos de Negócio (BPM), a análise da situação corrente do processo para mapear seus gargalos, ineficiências e retrabalhos existentes é contraposta ao desenho da situação ideal futura pretendida.

Esses dois estágios do ciclo BPM são internacionalmente denominados, respectivamente:

* **A)** Mapeamento *AS-IS* (como o processo é executado atualmente) e Modelagem *TO-BE* (como o processo deverá ser executado no futuro após otimização).
* **B)** Planejamento *BOTTOM-UP* e Execução *TOP-DOWN*.
* **C)** Cadeia de Suprimentos *KANBAN* e Manufatura *JUST-IN-TIME*.
* **D)** Metodologia *SCRUM* e Painel de Controle *BALANCED SCORECARD*.
* **E)** Matriz *SWOT* e Matriz *BCG*.

> **Comentário Detalhado:**
>
> - **A)** Correta. Padrão BPM CBOK: **AS-IS** (diagnóstico da situação atual, gargalos e desperdícios); **TO-BE** (modelo do processo futuro otimizado).
> - **B)** Incorreta. Fluxos direcionais de planejamento.
> - **C)** Incorreta. Ferramentas de manufatura.
> - **D)** Incorreta. Scrum é ágil; BSC é estratégico.
> - **E)** Incorreta. Matrizes de diagnóstico e portfólio.
> 
> **Gabarito: A**

---

"""

    q08 = """### Questão 08 (FCC - Adaptada / Analista de Tecnologia e Controle)
No Gerenciamento de Projetos, as metodologias ágeis (como o Scrum) ganharam amplo espaço no setor público pela necessidade de entregas parciais e adaptação constante a mudanças.

No framework **Scrum**, a reunião diária, curta e estruturada (de cerca de 15 minutos), na qual a equipe alinha o andamento dos trabalhos e identifica impedimentos imediatos, é denominada:

* **A)** Daily Scrum (ou Daily Stand-up).
* **B)** Sprint Review.
* **C)** Sprint Retrospective.
* **D)** Sprint Planning.
* **E)** Product Backlog Refinement.

> **Comentário Detalhado:**
>
> - **A)** Correta. O **Daily Scrum** é a reunião diária da equipe (15 minutos) para alinhamento e identificação de impedimentos.
> - **B)** Incorreta. Sprint Review homologa o incremento da Sprint.
> - **C)** Incorreta. Sprint Retrospective avalia melhorias internas da equipe.
> - **D)** Incorreta. Sprint Planning planeja as tarefas da Sprint.
> - **E)** Incorreta. Refinamento de backlog detalha itens futuros.
> 
> **Gabarito: A**

---

"""

    q09_10 = """### Questão 09 (FCC - Adaptada / Analista Jurídico de Controle)
O Decreto Federal nº 9.094/2017 (que simplifica o atendimento aos usuários dos serviços públicos e institui a Carta de Serviços) e a Lei Federal nº 13.460/2017 trazem normas expressas para a desburocratização administrativa.

A respeito das exigências documentais dirigidas aos cidadãos e usuários do serviço público, de acordo com o Decreto nº 9.094/2017:

* **A)** É vedada a exigência de reconhecimento de firma e de cópia autenticada em cartório de documentos expedidos no País, devendo a autenticação ser feita pelo próprio agente público mediante confronto com o original, ressalvada expressa previsão legal em contrário.
* **B)** É obrigatória a apresentação mensal de certidões negativas de débito cível e criminal em todo requerimento administrativo individual de protocolo.
* **C)** A Administração Pública não pode admitir a autodeclaração de veracidade sob nenhuma hipótese, exigindo sempre laudos periciais cartorários.
* **D)** O cidadão tem o ônus exclusivo de obter certidões emitidas por outros órgãos do próprio Poder Executivo, sendo proibido o compartilhamento eletrônico de dados entre repartições estatais.
* **E)** A Carta de Serviços ao Cidadão possui caráter meramente facultativo e sigiloso, não devendo ser publicada na internet.

> **Comentário Detalhado:**
>
> - **A)** Correta. Decreto nº 9.094/2017 e Lei nº 13.726/2018 dispensam reconhecimento de firma e autenticação cartorária como regra geral, cabendo ao servidor atestar o confere com o original.
> - **B)** Incorreta. Vedado exigir certidões que o Estado já possui.
> - **C)** Incorreta. Admite-se autodeclaração de veracidade.
> - **D)** Incorreta. Órgãos devem compartilhar bases de dados entre si.
> - **E)** Incorreta. A Carta de Serviços é obrigatória e pública.
> 
> **Gabarito: A**

---

### Questão 10 (FCC - Adaptada / TCE-GO - Analista de Controle Externo)
Na elaboração do Termo de Abertura do Projeto (*Project Charter*) e no planejamento do escopo segundo as boas práticas do Guia PMBOK, a ferramenta estruturada que decompõe hierarquicamente o trabalho total do projeto em entregas menores e pacotes de trabalho gerenciáveis é a:

* **A)** Estrutura Analítica do Projeto (EAP) / *Work Breakdown Structure (WBS)*.
* **B)** Diagrama de Dispersão de Ishikawa.
* **C)** Curva ABC de Pareto.
* **D)** Matriz GUT de Gravidade, Urgência e Tendência.
* **E)** Análise de Regressão Linear Múltipla.

> **Comentário Detalhado:**
>
> - **A)** Correta. A **Estrutura Analítica do Projeto (EAP)** decompõe hierarquicamente o escopo total em entregas e pacotes de trabalho gerenciáveis.
> - **B)** Incorreta. Ishikawa analisa causas raízes.
> - **C)** Incorreta. Curva ABC/Pareto prioriza falhas/itens (80/20).
> - **D)** Incorreta. Matriz GUT prioriza problemas.
> - **E)** Incorreta. Ferramenta estatística.
> 
> **Gabarito: A**

---

"""

    anchor_2 = "### 2. Desburocratização e Atendimento ao Cidadão (Decreto nº 9.094/2017)"
    anchor_3 = "### 3. Gestão de Processos de Negócio (BPM)"
    anchor_4 = "### 4. Gestão de Projetos segundo o Guia PMBOK (PMI)"
    anchor_fontes = "## 🌐 Fontes Oficiais & Referências Bibliográficas"

    text = text.replace(anchor_2, q06 + "\n" + anchor_2)
    text = text.replace(anchor_3, q07 + "\n" + anchor_3)
    text = text.replace(anchor_4, q08 + "\n" + anchor_4)
    text = text.replace(anchor_fontes, q09_10 + "\n" + anchor_fontes)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    print("Enriched File 21/03 successfully! Total: 10 questions.")


def enrich_file_04():
    filepath = os.path.join(BASE_DIR, "04_planejamento_estrategico_indicadores_e_gestao_por_competencias.md")
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    if "### Questão 06" in text:
        print("File 04 already enriched.")
        return

    q06 = """### Questão 06 (FCC - Adaptada / Analista de Planejamento e Gestão)
O planejamento organizacional é estruturado em três níveis hierárquicos interligados: Estratégico, Tático e Operacional.

A respeito desses níveis, é correto afirmar:

* **A)** O planejamento estratégico tem horizonte temporal de longo prazo, abrange a organização como uma totalidade sistêmica e define a missão, visão e objetivos corporativos mestres; já o planejamento operacional foca o curto prazo e detalha tarefas e procedimentos diários de execução.
* **B)** O planejamento tático é formulado pelos operários da linha de frente para solucionar problemas de atendimento imediato.
* **C)** O planejamento operacional abrange o macroambiente externo e analisa as forças competitivas da economia internacional.
* **D)** O planejamento estratégico é privativo de empresas comerciais de mercado, inexistindo aplicação prática no âmbito dos Tribunais de Contas e órgãos públicos.
* **E)** O planejamento tático foca exclusivamente em investimentos com prazo superior a quinze anos.

> **Comentário Detalhado:**
>
> - **A)** Correta. **Estratégico** (longo prazo, diretoria/cúpula, visão holística); **Tático** (médio prazo, gerências/departamentos); **Operacional** (curto prazo, métodos e tarefas cotidianas).
> - **B)** Incorreta. Tático é gerencial intermediário.
> - **C)** Incorreta. Macroambiente é estratégico.
> - **D)** Incorreta. Tribunais de Contas utilizam planejamento estratégico sistematicamente.
> - **E)** Incorreta. Médio prazo (anual/bianual).
> 
> **Gabarito: A**

---

"""

    q07 = """### Questão 07 (FCC - Adaptada / Auditor de Controle Externo)
Na transposição do Balanced Scorecard (BSC - Kaplan e Norton) para as organizações públicas e entidades de controle governamental (como o TCE-GO), a adaptação mais relevante no mapa estratégico consiste em:

* **A)** Deslocar a perspectiva dos "Clientes / Cidadãos-Usuários e Sociedade" para o topo do mapa estratégico como objetivo final supremo, passando a perspectiva financeira a atuar como viabilizadora e restrição orçamentária dos serviços prestados.
* **B)** Eliminar completamente a perspectiva de Aprendizado e Crescimento, visto que servidores públicos estáveis não necessitam de capacitação continuada.
* **C)** Substituir os indicadores de eficácia social por índices de lucro líquido financeiro a ser distribuído aos cidadãos como dividendos monetários.
* **D)** Considerar a perspectiva de Processos Internos como a única relevante, descartando qualquer métrica voltada para a satisfação da sociedade.
* **E)** Proibir o estabelecimento de relações de causa e efeito entre os objetivos estratégicos institucionais.

> **Comentário Detalhado:**
>
> - **A)** Correta. No setor público, o ápice do mapa do BSC é a **Sociedade e os Cidadãos** (geração de valor público), atuando a perspectiva financeira como sustentabilidade orçamentária para a prestação de serviços.
> - **B)** Incorreta. Aprendizado e crescimento continuam sendo a base.
> - **C)** Incorreta. Órgãos públicos não visam lucro comercial.
> - **D)** Incorreta. O BSC integra equilibradamente as perspectivas.
> - **E)** Incorreta. O mapa baseia-se em relações de causa e efeito.
> 
> **Gabarito: A**

---

"""

    q08 = """### Questão 08 (FCC - Adaptada / Analista de Controle Externo)
Na formulação de planos de intervenção operacional decorrentes de achados de auditoria ou do planejamento setorial, a ferramenta **5W2H** é amplamente utilizada para operacionalizar as decisões em planos de ação objetivos.

O significado e escopo da letra **"H" (*How Much*)** na estrutura do 5W2H corresponde a responder:

* **A)** Quanto custará a execução da ação (estimativa orçamentária de custos e desembolsos financeiros envolvidos).
* **B)** Quem será o executor responsável pela atividade.
* **C)** Quando e em quais datas a ação será iniciada e finalizada.
* **D)** Por que a ação deve ser realizada e qual a sua justificativa estratégica.
* **E)** Onde a ação será implementada geograficamente.

> **Comentário Detalhado:**
>
> - **A)** Correta. **5W2H**: What (o que), Why (por que), Where (onde), When (quando), Who (quem), How (como) e **How Much (quanto custa)**.
> - **B)** Incorreta. Refere-se ao *Who*.
> - **C)** Incorreta. Refere-se ao *When*.
> - **D)** Incorreta. Refere-se ao *Why*.
> - **E)** Incorreta. Refere-se ao *Where*.
> 
> **Gabarito: A**

---

"""

    q09_10 = """### Questão 09 (FCC - Adaptada / TCE-PI - Auditor de Controle Externo)
A Gestão por Competências no setor público busca alinhar o desenvolvimento dos servidores aos objetivos estratégicos da organização. De acordo com o modelo amplamente consagrado na doutrina administrativa (Dutra, Zarifian, Fleury), a competência individual fundamenta-se no tripé conceitual **C.H.A.**.

As letras que compõem a sigla **CHA** representam:

* **A)** Conhecimento (o saber teórico), Habilidade (o saber fazer prático) e Atitude (o querer fazer / agir proativo).
* **B)** Controle fiscal, Hierarquia funcional e Autoridade delegada.
* **C)** Celeridade operacional, Honestidade profissional e Aptidão física.
* **D)** Criatividade técnica, Homogeneidade de tarefas e Assertividade comunicacional.
* **E)** Conformidade regulamentar, Homologação decisória e Atendimento cortês.

> **Comentário Detalhado:**
>
> - **A)** Correta. **CHA**: **Conhecimento** (saber teórico), **Habilidade** (saber fazer / capacidade prática) e **Atitude** (querer fazer / postura e proatividade).
> - **B), C), D), E)** Incorretas. Distorções que não correspondem ao modelo teórico.
> 
> **Gabarito: A**

---

### Questão 10 (FCC - Adaptada / TCE-GO - Analista de Controle Externo)
A respeito dos indicadores de desempenho da gestão pública e das dimensões clássicas dos **6 Es** (Eficácia, Eficiência, Efetividade, Economicidade, Excelência e Execução):

Um programa público de vacinação infantil que imunizou 98% do público-alvo planejado, gerando como reflexo a erradicação de determinada doença infectocontagiosa na população infantil do Estado no ano subsequente, demonstrou, com relação ao atingimento da meta quantitativa e ao impacto social transformador duradouro, respectivamente:

* **A)** Alta Eficácia (atingimento da meta física de vacinação de 98%) e Alta Efetividade (impacto real positivo na saúde pública com a erradicação da doença).
* **B)** Alta Economicidade e Baixa Eficiência orçamentária.
* **C)** Baixa Eficácia e Ausência de Efetividade social.
* **D)** Execução financeira passiva e Baixa Excelência de atendimento.
* **E)** Fato gerador contábil sem reflexo em indicadores de desempenho da gestão.

> **Comentário Detalhado:**
>
> - **A)** Correta. **Eficácia** mede o atingimento de metas planejadas (atingiu 98% de imunização); **Efetividade** mede o impacto real e mudança duradoura na sociedade (erradicação da doença infantil).
> - **B), C), D), E)** Incorretas. Não refletem as definições doutrinárias consagradas.
> 
> **Gabarito: A**

---

"""

    anchor_2 = "### 2. O Balanced Scorecard (BSC) no Setor Público"
    anchor_3 = "### 3. Matrizes SWOT (FOFA), GUT e Plano de Ação 5W2H"
    anchor_5 = "### 5. Gestão por Competências no Setor Público (Decreto 9.991/2019)"
    anchor_fontes = "### 8. Fontes Oficiais e Referências Bibliográficas"

    text = text.replace(anchor_2, q06 + "\n" + anchor_2)
    text = text.replace(anchor_3, q07 + "\n" + anchor_3)
    text = text.replace(anchor_5, q08 + "\n" + anchor_5)
    text = text.replace(anchor_fontes, q09_10 + "\n" + anchor_fontes)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    print("Enriched File 21/04 successfully! Total: 10 questions.")


if __name__ == "__main__":
    enrich_file_01()
    enrich_file_02()
    enrich_file_03()
    enrich_file_04()
    print("Module 21 fully processed!")
