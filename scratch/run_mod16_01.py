# -*- coding: utf-8 -*-
import os
import re

BASE_DIR = "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/16_licitacoes_e_contratos_administrativos"

# ==============================================================================
# FILE 01: 01_governanca_planejamento_etp_tr_e_matriz_riscos.md
# ==============================================================================
f01_path = f"{BASE_DIR}/01_governanca_planejamento_etp_tr_e_matriz_riscos.md"
with open(f01_path, "r", encoding="utf-8") as f:
    t01 = f.read()

assert "### Questão 01" in t01
assert "### Questão 02" in t01
assert "### Questão 03" in t01
assert "### Questão 04" in t01
assert "### Questão 05" in t01

q06_01 = """### Questão 06 (FGV - Auditor de Controle Externo / TCE-GO)
A Lei nº 14.133/2021 (Nova Lei de Licitações e Contratos Administrativos) estabeleceu em seu art. 11 os objetivos precípuos do processo licitatório.

A esse respeito, assinale a opção que indica corretamente um dos objetivos expressamente positivados no referido dispositivo legal.

* **A)** Assegurar tratamento favorecido e diferenciado obrigatório às grandes multinacionais detentoras de patentes tecnológicas exclusivas.
* **B)** Garantir a seleção da proposta apta a gerar o resultado de contratação mais vantajoso para a Administração Pública, inclusive no que se refere ao ciclo de vida do objeto.
* **C)** Priorizar a escolha da proposta de menor valor nominal imediato de aquisição, desconsiderando custos futuros de manutenção e descarte do bem.
* **D)** Assegurar que a disputa ocorra sob absoluto sigilo até o término da fase recursal para evitar conluio entre os licitantes.
* **E)** Fomentar exclusivamente a contratação de empresas com sede no mesmo município onde o serviço público for executado.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O art. 11, II, impõe justamente assegurar tratamento isonômico e justa competição, sem privilégios arbitrários.
> - **B)** Correta. O art. 11, I, da Lei nº 14.133/2021 estatui como objetivo basilar: *"assegurar a seleção da proposta apta a gerar o resultado de contratação mais vantajoso para a Administração Pública, inclusive no que se refere ao ciclo de vida do objeto"*. Introduziu-se formalmente o conceito de custo global do ciclo de vida (custo de aquisição + custos de operação, manutenção e destinação final).
> - **C)** Incorreta. O critério moderno superou a visão míope do menor desembolso inicial estático; bens baratos que exigem manutenção caríssima ou poluem o meio ambiente violam o princípio do ciclo de vida.
> - **D)** Incorreta. A publicidade dos atos e das propostas é diretriz mestra (art. 11, IV, e art. 13 da NLLC).
> - **E)** Incorreta. É vedado estabelecer preferências fundadas na naturalidade, sede ou domicílio das licitantes (art. 9º, I, 'a', da Lei 14.133/2021).
>
> **Gabarito: B**"""

q07_01 = """### Questão 07 (FCC - Analista de Gestão Pública / Contratações)
Em consonância com as diretrizes de governança pública insculpidas no art. 11, parágrafo único, da Lei nº 14.133/2021, a alta administração do órgão ou entidade é responsável pela implementação de processos e estruturas de governança nas contratações.

Nesse contexto, assinale a afirmativa que apresenta um instrumento essencial de governança e planejamento das contratações públicas.

* **A)** O Plano de Contratações Anual (PCA), que visa a racionalizar as contratações dos órgãos sob sua competência, garantir o alinhamento com o planejamento estratégico e subsidiar as leis orçamentárias.
* **B)** A dispensa de elaboração de estudos técnicos para todas as compras rotineiras realizadas pelo órgão no decorrer do exercício financeiro.
* **C)** A concentração de todas as fases da contratação (planejamento, julgamento, fiscalização e pagamento) na pessoa de um único servidor de confiança da chefia.
* **D)** A criação de comissões secretas para seleção prévia de fornecedores antes da publicação do edital no Portal Nacional de Contratações Públicas.
* **E)** A delegação integral da competência de fiscalização orçamentária para a própria empresa contratada.

> **Comentário Detalhado:**
>
> - **A)** Correta. O art. 12, VII, da Lei nº 14.133/2021 estabelece que a autoridade competente deve providenciar a elaboração do **Plano de Contratações Anual (PCA)**, com o objetivo de racionalizar as compras públicas, evitar contratações fragmentadas, conferir previsibilidade ao mercado fornecedor e garantir o alinhamento entre as compras e o planejamento estratégico governamental.
> - **B)** Incorreta. O Estudo Técnico Preliminar (ETP) é peça basilar de governança, sendo dispensável apenas em hipóteses estritas e taxativas previstas em regulamento ou na lei (art. 72).
> - **C)** Incorreta. A concentração de funções afronta diretamente o **princípio da segregação de funções** (art. 5º e art. 7º, § 1º, da NLLC).
> - **D)** Incorreta. Procedimentos secretos são manifestamente nulos por violarem a transparência e a isonomia.
> - **E)** Incorreta. A fiscalização contratual é dever irrenunciável do Poder Público (art. 117 da Lei nº 14.133/2021).
>
> **Gabarito: A**"""

q08_01 = """### Questão 08 (FGV - Analista de Controle Externo / TCE-SC)
A Lei nº 14.133/2021 inovou ao disciplinar a gestão por competências e a atuação do Agente de Contratação e da Comissão de Contratação (arts. 7º e 8º).

Sobre os requisitos legais para a designação do Agente de Contratação, assinale a afirmativa correta.

* **A)** O Agente de Contratação pode ser pessoa estranha aos quadros públicos contratada por empresa terceirizada para prestar consultoria ao órgão.
* **B)** A designação do Agente de Contratação deve recair, preferencialmente, sobre servidor efetivo ou empregado público dos quadros permanentes da Administração Pública, que possua atribuições relacionadas ou qualificação atestada por certificação profissional.
* **C)** O Agente de Contratação responde solidariamente por todos os atos praticados pela equipe de apoio, mesmo que tenha manifestado divergência expressa e formal em ata.
* **D)** O pregoeiro, nas licitações na modalidade pregão, deve ser obrigatoriamente um dirigente político do órgão investido em cargo de direção superior.
* **E)** É dispensável a observância do princípio da segregação de funções na designação dos agentes que atuam nas fases de planejamento e liquidação de despesa.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O art. 7º, I, da NLLC veda a designação de terceirizados; exige que os agentes sejam preferencialmente servidores públicos efetivos ou empregados públicos dos quadros permanentes da Administração.
> - **B)** Correta. O art. 7º da Lei nº 14.133/2021 estatui que a autoridade designará agentes públicos preferencialmente servidores efetivos ou empregados públicos permanentes, que tenham atribuições relacionadas a licitações e contratos ou possuam formação compatível ou qualificação atestada por escola de governo. O art. 8º define que o Agente de Contratação conduzirá a licitação e responderá individualmente pelas decisões.
> - **C)** Incorreta. A responsabilidade é individualizada; o agente que manifestar posição divergente e fundamentada registrada em ata não responde solidariamente pelas decisões do colegiado/equipe.
> - **D)** Incorreta. O pregoeiro é o próprio agente de contratação responsável pelo pregão, devendo cumprir os mesmos requisitos técnicos e preferência por vínculo efetivo.
> - **E)** Incorreta. A segregação de funções é vedação expressa à acumulação de atribuições suscetíveis a risco de conflito de interesses (art. 7º, § 1º).
>
> **Gabarito: B**"""

q09_01 = """### Questão 09 (FCC - Procurador do Estado / Adaptada)
O art. 10 da Lei nº 14.133/2021 estabelece importante prerrogativa voltada à segurança jurídica dos agentes públicos que atuam nos processos de contratação.

Conforme esse dispositivo, se o agente público for demandado judicial ou administrativamente em razão de ato praticado com estrita observância de orientação constante em parecer jurídico emitido pela assessoria jurídica do órgão:

* **A)** Deverá ser imediatamente afastado cautelarmente de suas funções públicas sem direito a vencimentos até o trânsito em julgado.
* **B)** A advocacia pública que represente o órgão promoverá a sua defesa judicial ou extrajudicial, salvo se houver provas de prática de ato ilícito doloso ou praticado em desconformidade com o parecer.
* **C)** O agente público fica obrigado a contratar advogado particular com seus próprios recursos, sendo vedada qualquer assistência da Procuradoria do Estado.
* **D)** A responsabilidade civil, administrativa e penal do agente público é automaticamente extinta antes de qualquer apuração.
* **E)** O parecerista jurídico torna-se o único réu na ação judicial, sendo excluído sumariamente o agente público do processo.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O cumprimento de parecer jurídico emitido por órgão oficial não é falta funcional; afastar cautelarmente e sem remuneração configuraria grave ilegalidade e abuso.
> - **B)** Correta. O art. 10, caput, da Lei nº 14.133/2021 estabelece que, se o agente público for demandado administrativa ou judicialmente em decorrência de ato praticado em estrita consonância com parecer emitido pela assessoria jurídica, a **advocacia pública promoverá a sua representação judicial ou extrajudicial**. A assistência é afastada caso conste nos autos que o ato foi praticado com dolo ou fraude ou em flagrante desconformidade com o parecer (§ 2º).
> - **C)** Incorreta. A lei expressamente conferiu à advocacia pública o dever de patrocinar a defesa institucional do agente nessa hipótese.
> - **D)** Incorreta. A regra assegura assistência jurídica processual; não outorga imunidade material absoluta prévia nem anistia automática.
> - **E)** Incorreta. O parecerista não substitui o agente no polo passivo; sua responsabilização segue os parâmetros da LINDB (dolo ou erro grosseiro, art. 28).
>
> **Gabarito: B**"""

q10_01 = """### Questão 10 (FGV - Analista Judiciário de Controle Externo / TCE-GO)
O Estudo Técnico Preliminar (ETP), previsto no art. 18, § 1º, da Lei nº 14.133/2021, constitui o documento constitutivo da primeira etapa do planejamento de uma contratação.

Dentre os elementos previstos para o ETP, assinale a opção que apresenta um dos elementos obrigatórios (essenciais), cuja ausência torna imperfeito o estudo preparatório.

* **A)** A definição nominal e o CPF dos diretores de todas as empresas fornecedoras que atuam no mercado nacional.
* **B)** A descrição da necessidade da contratação considerado o problema a ser resolvido sob a perspectiva do interesse público.
* **C)** A indicação da modalidade de leilão como a única via jurídica admitida para a compra de bens comuns.
* **D)** A dispensa obrigatória de previsão de impactos ambientais em contratações de engenharia.
* **E)** A fixação de marca comercial específica como exigência inegociável para a participação no certame.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O ETP não investiga CPFs de diretores de empresas; visa a analisar a viabilidade técnica e econômica da contratação.
> - **B)** Correta. O art. 18, § 1º, I, c/c § 2º da Lei nº 14.133/2021 elenca como elemento **obrigatório e indispensável** do ETP a *"descrição da necessidade da contratação, considerado o problema a ser resolvido sob a perspectiva do interesse público"*. Juntamente com a estimativa das quantidades, a estimativa do valor, a justificativa da escolha da solução e a declaração de viabilidade, integra o núcleo obrigatório do ETP.
> - **C)** Incorreta. Leilão destina-se à alienação de bens (art. 28, IV), e não à aquisição de bens comuns.
> - **D)** Incorreta. Os requisitos de sustentabilidade ambiental integram o ETP (art. 18, § 1º, XII).
> - **E)** Incorreta. Em regra é vedada a indicação de marca, salvo hipóteses restritas de padronização justificada tecnicamente (art. 41, I).
>
> **Gabarito: B**"""

q11_01 = """### Questão 11 (FCC - Auditor de Controle Externo)
Na fase preparatória das contratações regidas pela Lei nº 14.133/2021, o Termo de Referência (TR) e o Projeto Básico desempenham papéis definidores do objeto licitado.

Sobre as diretrizes legais aplicáveis a esses instrumentos, assinale a afirmativa correta.

* **A)** O Termo de Referência é o documento preparatório obrigatório utilizado exclusivamente nas licitações de obras e serviços especiais de engenharia de alta complexidade.
* **B)** O Termo de Referência é o documento necessário para a contratação de bens e serviços, contendo parâmetros objetivos de desempenho, requisitos da contratação, modelo de execução e critérios de medição e pagamento.
* **C)** No Projeto Básico de obras de engenharia, a elaboração da planilha orçamentária detalhada com quantitativos e custos unitários é facultativa para a Administração.
* **D)** O Termo de Referência pode conter especificações excessivas ou irrelevantes que direcionem o certame para fornecedor exclusivo local.
* **E)** É proibido prever no Termo de Referência matriz de riscos para contratos de grande vulto.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Para obras e serviços de engenharia o instrumento técnico principal é o **Projeto Básico** (art. 6º, XXV); o Termo de Referência é utilizado precipuamente para a aquisição de **bens e serviços comuns e em geral** (art. 6º, XXIII).
> - **B)** Correta. O art. 6º, XXIII, da Lei nº 14.133/2021 define o **Termo de Referência (TR)** como o documento necessário para a contratação de bens e serviços, que deve conter a definição do objeto, fundamentação da contratação, requisitos técnicos, modelo de gestão do contrato, critérios de medição, pagamento e estimativa do valor.
> - **C)** Incorreta. A planilha orçamentária detalhada com custos unitários é elemento estritamente obrigatório e vinculante no Projeto Básico (art. 6º, XXV).
> - **D)** Incorreta. É vedado inserir especificações restritivas ou desnecessárias que frustrem a competição (art. 9º, I).
> - **E)** Incorreta. A matriz de riscos é incentivada em geral e **obrigatória** nas contratações de grande vulto (art. 22, § 3º).
>
> **Gabarito: B**"""

# Inserções no arquivo 01 de trás para frente
ancora_33 = "### 3.3 Termo de Referência vs. Projeto Básico e Projeto Executivo"
pos_33 = t01.find(ancora_33)
pos_34 = t01.find("### 3.4 Matriz de Alocação de Riscos", pos_33)
assert pos_33 != -1 and pos_34 != -1
t01 = t01[:pos_34] + "\n\n" + q11_01.strip() + "\n\n---\n\n" + t01[pos_34:]

ancora_31 = "### 3.1 Plano de Contratações Anual (PCA) e Integração Orçamentária"
pos_31 = t01.find(ancora_31)
pos_32 = t01.find("### 3.2 Estudo Técnico Preliminar", pos_31)
assert pos_31 != -1 and pos_32 != -1
t01 = t01[:pos_32] + "\n\n" + q10_01.strip() + "\n\n---\n\n" + t01[pos_32:]

ancora_24 = "### 2.4 Defesa Jurídica Institucional dos Agentes (Art. 10)"
pos_24 = t01.find(ancora_24)
pos_30 = t01.find("## 3. Planejamento das Contratações", pos_24)
assert pos_24 != -1 and pos_30 != -1
t01 = t01[:pos_30] + "\n\n" + q09_01.strip() + "\n\n---\n\n" + t01[pos_30:]

ancora_21 = "### 2.1 O Agente de Contratação e o Pregoeiro"
pos_21 = t01.find(ancora_21)
pos_22 = t01.find("### 2.2 Comissão de Contratação", pos_21)
assert pos_21 != -1 and pos_22 != -1
t01 = t01[:pos_22] + "\n\n" + q08_01.strip() + "\n\n---\n\n" + t01[pos_22:]

ancora_13 = "### 1.3 Governança das Contratações e Gestão por Competências"
pos_13 = t01.find(ancora_13)
pos_20 = t01.find("## 2. Agentes Públicos da Contratação", pos_13)
assert pos_13 != -1 and pos_20 != -1
t01 = t01[:pos_20] + "\n\n" + q07_01.strip() + "\n\n---\n\n" + t01[pos_20:]

ancora_12 = "### 1.2 Os Objetivos Fundamentais do Processo Licitatório (Art. 11)"
pos_12 = t01.find(ancora_12)
pos_13_new = t01.find("### 1.3 Governança das Contratações", pos_12)
assert pos_12 != -1 and pos_13_new != -1
t01 = t01[:pos_13_new] + "\n\n" + q06_01.strip() + "\n\n---\n\n" + t01[pos_13_new:]

qs_01 = re.findall(r"### Questão (\d+)", t01)
print("Questões no arquivo 01 do Módulo 16:", qs_01)
assert len(qs_01) == 11
assert sorted(qs_01) == ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']

with open(f01_path, "w", encoding="utf-8") as f:
    f.write(t01)

print("Arquivo 01 do Módulo 16 gravado com sucesso! Total: 11 questões.")
