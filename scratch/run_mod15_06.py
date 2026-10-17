# -*- coding: utf-8 -*-
import os
import re

BASE_DIR = "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/15_nocoes_de_direito_administrativo"
f06_path = f"{BASE_DIR}/06_acesso_a_informacao_e_contratos_publicidade.md"
with open(f06_path, "r", encoding="utf-8") as f:
    t06 = f.read()

assert "### Questão 01" in t06
assert "### Questão 02" in t06
assert "### Questão 03" in t06
assert "### Questão 04" in t06
assert "### Questão 05" in t06

q06_06 = """### Questão 06 (FCC - Auditor de Controle Externo / TCE-GO)
A Lei de Acesso à Informação (Lei Federal nº 12.527/2011) regulamenta o direito constitucional fundamental de obter informações dos órgãos públicos (art. 5º, XXXIII, CF/88).

A respeito das diretrizes estruturantes da LAI e do regime de publicidade na Administração Pública, assinale a afirmativa correta.

* **A)** O sigilo é a regra geral na Administração Pública, devendo a publicidade ser deferida excepcionalmente apenas aos cidadãos que comprovem interesse jurídico direto e pessoal na informação pleiteada.
* **B)** A publicidade é o preceito geral e o sigilo a exceção, sendo dever do Estado garantir o acesso a informações públicas mediante utilização de meios de comunicação viabilizados pela tecnologia da informação e fomento à cultura de transparência.
* **C)** A divulgação em sítios eletrônicos oficiais de dados orçamentários, repasses financeiros e contratos administrativos configura transparência passiva.
* **D)** As entidades privadas sem fins lucrativos que recebam recursos públicos para realização de ações de interesse público estão totalmente dispensadas de prestar contas ou conferir publicidade a esses recursos.
* **E)** O fornecimento de informação pública está condicionado ao prévio pagamento de taxa remuneratória correspondente ao custo da busca e do trabalho intelectual do servidor público.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A regra geral republicana e constitucional é a **publicidade máxima**; o sigilo é estrita e fundamentada exceção legal. Ademais, a LAI proíbe expressamente a exigência de motivação ou comprovação de interesse jurídico do requerente.
> - **B)** Correta. O art. 3º da Lei nº 12.527/2011 consagra as diretrizes fundamentais da LAI: I - publicidade como preceito geral e do sigilo como exceção; II - divulgação de informações de interesse público, independentemente de solicitações; III - utilização de meios de comunicação viabilizados pela tecnologia da informação; IV - fomento ao desenvolvimento da cultura de transparência; V - desenvolvimento do controle social da administração pública.
> - **C)** Incorreta. A divulgação prévia, obrigatória e espontânea nos portais da transparência sem necessidade de provocação do cidadão denomina-se **transparência ativa**. Transparência passiva é a resposta a pedidos específicos formulados pelos cidadãos.
> - **D)** Incorreta. O art. 2º da LAI submete as entidades privadas que recebam recursos públicos (subvenções, convênios, contratos de gestão) ao dever de dar publicidade aos valores públicos geridos.
> - **E)** Incorreta. O art. 10 da LAI estabelece que o serviço de busca e fornecimento da informação é **gratuito**, salvo nos casos de reprodução de documentos pelo órgão, situação em que poderá ser cobrado exclusivamente o valor do custo dos serviços e dos materiais utilizados.
>
> **Gabarito: B**"""

q07_06 = """### Questão 07 (FGV - Analista de Controle Externo / Auditoria)
Determinado cidadão protocolou requerimento de acesso à informação perante uma autarquia estadual, solicitando cópia integral de notas de empenho e medições de uma obra de pavimentação rodoviária.

De acordo com o rito procedimental estabelecido pela Lei Federal nº 12.527/2011 para a transparência passiva, a Administração Pública:

* **A)** Deve autorizar ou conceder o acesso imediato à informação disponível; não sendo possível o acesso imediato, tem o prazo de até vinte dias para responder, prorrogável justificadamente por mais dez dias.
* **B)** Dispõe do prazo improrrogável de sessenta dias úteis para deliberar sobre o requerimento de informações públicas.
* **C)** Pode condicionar a tramitação do pedido à declaração das razões determinantes da solicitação pelo cidadão interessado.
* **D)** Em caso de indeferimento de acesso a informações, não precisa fundamentar a negativa, haja vista a discricionariedade inerente à segurança dos arquivos públicos.
* **E)** Fica dispensada de prever instância recursal contra a decisão denegatória, sendo o Mandado de Segurança a única via admissível de insurgência.

> **Comentário Detalhado:**
>
> - **A)** Correta. O art. 11 da Lei nº 12.527/2011 estipula que o órgão público deve conceder o acesso imediato à informação disponível. Na impossibilidade de fazê-lo incontinente, deverá responder em prazo **não superior a 20 (vinte) dias**, admitida prorrogação por mais **10 (dez) dias** mediante justificativa expressa e motivada encaminhada ao requerente.
> - **B)** Incorreta. O prazo legal é de 20 dias (com prorrogação de 10 dias), e não 60 dias úteis.
> - **C)** Incorreta. O art. 10, § 3º, da LAI é peremptório: *"São vedadas quaisquer exigências relativas aos motivos determinantes da solicitação de informações de interesse público"*.
> - **D)** Incorreta. O indeferimento deve ser expressa e detalhadamente fundamentado, indicando as razões de sigilo ou a inexistência do documento, sob pena de responsabilidade funcional.
> - **E)** Incorreta. Negado o acesso, cabe recurso administrativo no prazo de 10 dias à autoridade hierarquicamente superior (art. 15 da LAI), não sendo o Judiciário a via exclusiva.
>
> **Gabarito: A**"""

q08_06 = """### Questão 08 (FCC - Técnico de Controle Externo / Adaptada TCE-GO)
No que concerne à classificação de informações sigilosas e à competência para a atribuição dos graus de sigilo no âmbito da Administração Pública do Estado de Goiás, conforme a Lei nº 12.527/2011 e o Decreto Estadual nº 7.904/2013, assinale a afirmativa correta.

* **A)** A competência para classificar informação no grau ultrassecreto (prazo máximo de restrição de 25 anos) é privativa do Governador e do Vice-Governador do Estado, no âmbito do Poder Executivo estadual.
* **B)** Qualquer servidor público ocupante de cargo efetivo possui competência legal para classificar documentos públicos como ultrassecretos a seu livre critério funcional.
* **C)** A autoridade que classifica um documento como secreto pode fixar discricionariamente prazo de sigilo de trinta anos, ante a soberania da gestão documental estadual.
* **D)** As informações de grau reservado possuem prazo de proteção sigilosa de até quinze anos, vedada a sua desclassificação antes do decurso do prazo.
* **E)** A classificação de sigilo não exige termo formal fundamentado de classificação, bastando o carimbo de confidencialidade aposto na capa dos autos.

> **Comentário Detalhado:**
>
> - **A)** Correta. A classificação de grau ultrassecreto (máximo de 25 anos) restringe-se às mais altas autoridades governamentais. No âmbito estadual goiano (Decreto Estadual nº 7.904/2013 c/c art. 27 da Lei nº 12.527/2011), a competência para classificação no grau **ultrassecreto** é exclusiva do Governador do Estado e do Vice-Governador; no grau **secreto** (máximo 15 anos), dos Secretários de Estado e autoridades equivalentes; e no grau **reservado** (máximo 5 anos), dos dirigentes máximos de autarquias, fundações e empresas públicas.
> - **B)** Incorreta. Servidores de escalão subalterno ou intermediário não detêm competência para classificar informações ultrassecretas ou secretas.
> - **C)** Incorreta. O teto legal da LAI (art. 24, § 1º) é taxativo: ultrassecreta = até 25 anos; secreta = até 15 anos; reservada = até 5 anos. Fixar 30 anos é ilegalidade manifesta.
> - **D)** Incorreta. O prazo de sigilo da informação reservada é de no máximo **5 (cinco) anos** (art. 24, § 1º, III, da LAI).
> - **E)** Incorreta. O art. 28 da LAI exige a formalização do Termo de Classificação de Informação (TCI), contendo a fundamentação da restrição, o assunto, o prazo e a indicação da autoridade competente.
>
> **Gabarito: A**"""

q09_06 = """### Questão 09 (FGV - Analista de Controle Externo / TCE-GO)
Determinado cidadão requereu, com fundamento na LAI, acesso aos registros funcionais de servidores públicos estaduais que participaram, na condição de testemunhas e sindicantes, de apuração de graves violações a direitos humanos e atos de tortura ocorridos durante período de exceção política. O órgão responsável indeferiu o pedido, sob o argumento de que as informações envolveriam intimidade e vida privada, sujeitando-se ao sigilo legal de cem anos do art. 31 da LAI.

À luz da Lei Federal nº 12.527/2011 e da jurisprudência dos Tribunais Superiores, a decisão administrativa denegatória:

* **A)** É legítima, pois o direito à privacidade e à honra individual prevalece de forma absoluta sobre qualquer pretensão de apuração histórica ou controle social.
* **B)** É ilegítima, visto que a própria Lei de Acesso à Informação veda taxativamente a restrição de acesso a informações ou documentos que versem sobre condutas que impliquem violação dos direitos humanos praticada por agentes públicos ou a mando de autoridades públicas.
* **C)** Deveria ter condicionado a liberação dos documentos à autorização prévia e expressa de todos os servidores citados no relatório.
* **D)** Poderia conceder o acesso exclusivamente se o requerente firmasse termo de confidencialidade comprometendo-se a não divulgar os dados à imprensa.
* **E)** Ampara-se no princípio da supremacia do interesse público secundário de preservação da imagem funcional dos órgãos estatais.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O direito à verdade e à memória histórica sobre violações de direitos humanos não pode ser obstado sob o pretexto de proteção da intimidade de agentes públicos executores de ilícitos de Estado.
> - **B)** Correta. O art. 21, parágrafo único, da Lei nº 12.527/2011 prevê categoricamente: *"As informações ou documentos que versem sobre condutas que impliquem violação dos direitos humanos praticada por agentes públicos ou a mando de autoridades públicas não poderão ser objeto de restrição de acesso"*. O preceito afasta qualquer alegação de sigilo, inclusive o regime de informações pessoais do art. 31.
> - **C)** Incorreta. A consulta ou autorização dos servidores violadores de direitos humanos é expressamente dispensada pela lei.
> - **D)** Incorreta. O acesso nesse caso é público e amplo, não comportando imposição de cláusula de sigilo ou termo de confidencialidade individual.
> - **E)** Incorreta. O interesse público primário de preservação dos direitos humanos e transparência histórica sobrepuja eventuais interesses corporativos secundários da corporação.
>
> **Gabarito: B**"""

q10_06 = """### Questão 10 (FCC - Procurador do Estado / Adaptada)
A contratação de serviços de publicidade institucional prestados por intermédio de agências de propaganda pela Administração Pública rege-se pelas normas especiais da Lei nº 12.232/2010.

No que tange aos procedimentos e tipos de licitação admitidos para esses serviços, assinale a afirmativa correta.

* **A)** Os serviços de publicidade prestados por agências de propaganda podem ser licitados mediante pregão eletrônico, desde que os serviços sejam considerados comuns pela Administração.
* **B)** As licitações de publicidade disciplinadas pela Lei nº 12.232/2010 devem ser processadas obrigatoriamente pelos tipos 'melhor técnica' ou 'técnica e preço', sendo vedada a utilização do pregão.
* **C)** O julgamento das propostas técnicas é realizado privativamente pelo chefe da assessoria de comunicação do órgão, dispensada a criação de subcomissão técnica.
* **D)** Os membros da subcomissão técnica de julgamento devem ser todos servidores ocupantes de cargos de provimento efetivo do próprio órgão licitante.
* **E)** As propostas técnicas devem ser apresentadas com a ostensiva identificação da agência de publicidade em todas as páginas para conferir maior transparência à comissão avaliadora.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A Lei nº 12.232/2010 e a própria Lei nº 14.133/2021 (art. 29, parágrafo único) **vedam expressamente o uso do pregão** para a contratação de serviços de publicidade e propaganda, em face da sua natureza eminentemente intelectual, subjetiva e artística.
> - **B)** Correta. O art. 5º da Lei nº 12.232/2010 prescreve que as licitações para contratação de serviços de publicidade serão processadas obrigatoriamente pelos tipos **"melhor técnica"** ou **"técnica e preço"**, sendo terminantemente vedado o pregão ou o julgamento exclusivo por menor preço.
> - **C)** Incorreta. As propostas técnicas são julgadas obrigatoriamente por uma **subcomissão técnica** composta por no mínimo três membros (art. 10).
> - **D)** Incorreta. Pelo menos um terço (1/3) da subcomissão técnica deve ser composto por profissionais que **não mantenham qualquer vínculo funcional** ou contratual com o órgão público licitante (sorteados publicamente em sessão pública), visando a garantir a imparcialidade do julgamento.
> - **E)** Incorreta. A proposta técnica deve ser julgada **às cegas (proposta técnica desidentificada)**; a identificação da agência antes do julgamento da pontuação técnica é causa de desclassificação sumária da licitante (art. 6º da Lei nº 12.232/2010).
>
> **Gabarito: B**"""

# Inserções no arquivo 06
ancora_32 = "### 3.2 Tipos Licitatórios Obrigatórios"
pos_32 = t06.find(ancora_32)
pos_33 = t06.find("### 3.3 A Subcomissão Técnica de Julgamento", pos_32)
assert pos_32 != -1 and pos_33 != -1
t06 = t06[:pos_33] + "\n\n" + q10_06.strip() + "\n\n---\n\n" + t06[pos_33:]

ancora_23 = "### 2.3 Proteção de Informações Pessoais (100 Anos)"
pos_23 = t06.find(ancora_23)
pos_24 = t06.find("### 2.4 Vedação Absoluta de Sigilo: Violações a Direitos Humanos", pos_23)
pos_30 = t06.find("## 3. Licitações e Contratos de Serviços de Publicidade", pos_24)
assert pos_23 != -1 and pos_30 != -1
t06 = t06[:pos_30] + "\n\n" + q09_06.strip() + "\n\n---\n\n" + t06[pos_30:]

ancora_22 = "### 2.2 Competência Funcional para Classificação no Estado de Goiás"
pos_22 = t06.find(ancora_22)
pos_23_new = t06.find("### 2.3 Proteção de Informações Pessoais", pos_22)
assert pos_22 != -1 and pos_23_new != -1
t06 = t06[:pos_23_new] + "\n\n" + q08_06.strip() + "\n\n---\n\n" + t06[pos_23_new:]

ancora_14 = "### 1.4 Prazos Procedimentais e Regime Recursal"
pos_14 = t06.find(ancora_14)
pos_20 = t06.find("## 2. Classificação de Informações Sigilosas", pos_14)
assert pos_14 != -1 and pos_20 != -1
t06 = t06[:pos_20] + "\n\n" + q07_06.strip() + "\n\n---\n\n" + t06[pos_20:]

ancora_11 = "### 1.1 Diretrizes Fundamentais: A Publicidade como Regra Geral"
pos_11 = t06.find(ancora_11)
pos_12 = t06.find("### 1.2 Transparência Ativa", pos_11)
assert pos_11 != -1 and pos_12 != -1
t06 = t06[:pos_12] + "\n\n" + q06_06.strip() + "\n\n---\n\n" + t06[pos_12:]

qs_06 = re.findall(r"### Questão (\d+)", t06)
print("Questões no arquivo 06:", qs_06)
assert len(qs_06) == 10
assert sorted(qs_06) == ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']

with open(f06_path, "w", encoding="utf-8") as f:
    f.write(t06)

print("Arquivo 06 gravado com sucesso! Total: 10 questões.")
