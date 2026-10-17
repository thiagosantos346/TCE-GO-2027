# -*- coding: utf-8 -*-
import os
import re

BASE_DIR = "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/16_licitacoes_e_contratos_administrativos"
f03_path = f"{BASE_DIR}/03_procedimentos_auxiliares_e_contratacao_direta.md"
with open(f03_path, "r", encoding="utf-8") as f:
    t03 = f.read()

assert "### Questão 01" in t03
assert "### Questão 02" in t03
assert "### Questão 03" in t03
assert "### Questão 04" in t03
assert "### Questão 05" in t03

q06_03 = """### Questão 06 (FCC - Analista Judiciário - Área Administrativa)
No âmbito das contratações públicas regidas pela Lei nº 14.133/2021, a contratação direta subdivide-se nas figuras jurídicas da inexigibilidade de licitação e da dispensa de licitação.

A respeito da distinção conceitual e dogmática entre esses dois institutos, assinale a afirmativa correta.

* **A)** A inexigibilidade de licitação ocorre quando a competição é perfeitamente viável do ponto de vista fático e jurídico, mas a lei autoriza a contratação direta por conveniência e oportunidade do administrador.
* **B)** A dispensa de licitação fundamenta-se na inviabilidade fática ou jurídica de competição, possuindo rol meramente exemplificativo na legislação de regência.
* **C)** Na inexigibilidade de licitação há inviabilidade de competição decorrente da exclusividade de fornecedor, da notoriedade técnica profissional ou da natureza singular do objeto, configurando o art. 74 um rol meramente exemplificativo; já na dispensa de licitação (art. 75), a competição seria viável em tese, mas o legislador optou por dispensá-la em rol estrito e taxativo.
* **D)** A dispensa de licitação dispensa a instauração de qualquer processo administrativo formal, bastando a emissão de nota de empenho imediata.
* **E)** Em ambos os casos, inexigibilidade e dispensa, a Administração Pública fica desobrigada de justificar a razoabilidade do preço contratado.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Onde a competição é viável, não cabe inexigibilidade; cabe licitação ou, excepcionalmente, dispensa de licitação se houver enquadramento taxativo em lei.
> - **B)** Incorreta. A inviabilidade de competição é a essência da **inexigibilidade**, cujo rol é exemplificativo. A dispensa pressupõe viabilidade teórica de concorrência com rol **taxativo (numerus clausus)**.
> - **C)** Correta. Dogmática clássica e unânime: na **inexigibilidade** (art. 74) a competição é impossível (fornecedor exclusivo, artista consagrado, serviço técnico especializado com profissional de notória especialização), tendo o legislador apresentado hipóteses exemplificativas ("em especial"); na **dispensa** (art. 75), a disputa seria em tese viável, mas a lei autoriza a não realização da licitação (licitação dispensável) por razões de modicidade do valor, urgência, ou desinteresse de mercado, em rol estritamente taxativo.
> - **D)** Incorreta. A contratação direta exige rigoroso processo administrativo prévio (art. 72 da Lei nº 14.133/2021).
> - **E)** Incorreta. A justificativa do preço é requisito obrigatório em toda contratação direta (art. 72, VII), para coibir superfaturamento.
>
> **Gabarito: C**"""

q07_03 = """### Questão 07 (FGV - Auditor de Controle Externo / TCE-GO)
O credenciamento constitui procedimento auxiliar expressamente disciplinado no art. 79 da Lei nº 14.133/2021, vocacionado ao cadastramento prévio de interessados para eventual contratação pela Administração Pública.

Sobre as hipóteses e regras aplicáveis ao credenciamento, assinale a afirmativa correta.

* **A)** O credenciamento é admitido exclusivamente para a contratação de fornecedores exclusivos de medicamentos raros importados.
* **B)** A Administração Pública deve manter edital de credenciamento permanentemente aberto para o ingresso de novos interessados ao longo de toda a sua vigência, garantindo igualdade de condições a todos os que preencham os requisitos de habilitação.
* **C)** No credenciamento com contratações paralelas e não excludentes, a Administração Pública pode selecionar arbitrariamente qual dos credenciados executará o serviço a cada demanda.
* **D)** O valor a ser pago aos credenciados deve ser negociado individualmente com cada contratado no momento da emissão da ordem de serviço.
* **E)** O procedimento de credenciamento elimina a necessidade de comprovação de regularidade fiscal e trabalhista pelos interessados.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Fornecedor exclusivo é caso clássico de inexigibilidade comum (art. 74, I), e não de credenciamento.
> - **B)** Correta. O art. 79, parágrafo único, I, da Lei nº 14.133/2021 estabelece expressamente que a Administração deverá manter **edital de credenciamento permanentemente aberto** para a inscrição de eventuais interessados, garantindo a publicidade, a isonomia e a entrada contínua de novos profissionais ou empresas aptas.
> - **C)** Incorreta. Quando o objeto admitir contratações simultâneas mas demandar distribuição, a seleção deve basear-se em critérios objetivos prévios (como sorteio público, rodízio ou preferência do usuário do serviço público), vedada qualquer escolha subjetiva pelo gestor.
> - **D)** Incorreta. O preço do credenciamento é previamente tabelado e fixado de forma uniforme e pública pela própria Administração no edital convocatório (art. 79, parágrafo único, II).
> - **E)** Incorreta. A habilitação jurídica, fiscal, social e trabalhista é requisito indispensável para credenciamento.
>
> **Gabarito: B**"""

q08_03 = """### Questão 08 (FCC - Procurador do Estado / Adaptada)
No que se refere ao Sistema de Registro de Preços (SRP) e à utilização da ata de registro de preços por órgãos não participantes (figura do "carona"), em conformidade com o art. 86 da Lei nº 14.133/2021, assinale a afirmativa correta.

* **A)** Qualquer órgão público municipal pode aderir livremente como "carona" a atas de registro de preços geradas por outros municípios sem necessidade de consulta ou autorização do órgão gerenciador.
* **B)** As aquisições ou as contratações adicionais por órgãos não participantes ("caronas") não poderão exceder, por órgão ou entidade, a 50% (cinquenta por cento) dos quantitativos dos itens do instrumento convocatório registrados na ata para o órgão gerenciador.
* **C)** O quantitativo total decorrente de todas as adesões de órgãos não participantes a uma ata de registro de preços não possui limite global, admitindo adesões ilimitadas.
* **D)** É vedada em absoluto a realização de licitação sob o sistema de registro de preços para obras de engenharia padronizadas.
* **E)** A vigência da ata de registro de preços será de até cinco anos improrrogáveis.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A adesão de não participante depende de prévia consulta e autorização expressa do órgão gerenciador, além de demonstração da vantagem econômica e capacidade do fornecedor (art. 86, § 2º).
> - **B)** Correta. O art. 86, § 4º, da Lei nº 14.133/2021 estabelece que as aquisições ou contratações adicionais por órgão não participante não poderão exceder, por órgão ou entidade, a **50% (cinquenta por cento)** dos quantitativos dos itens registrados na ata de registro de preços para o órgão gerenciador e participantes.
> - **C)** Incorreta. Há teto global expresso: o quantitativo decorrente de todas as adesões não poderá exceder, na totalidade, ao **dobro (2x / 100%)** do quantitativo de cada item registrado (art. 86, § 5º).
> - **D)** Incorreta. A Lei nº 14.133/2021 (art. 85) autorizou expressamente o SRP para serviços de engenharia e obras padronizadas com projeto padrão.
> - **E)** Incorreta. O prazo de vigência da ata de registro de preços é de **1 (um) ano**, prorrogável por igual período, desde que comprovada a vantajosidade (art. 84).
>
> **Gabarito: B**"""

q09_03 = """### Questão 09 (FGV - Analista de Controle Externo / TCE-SC)
O art. 72 da Lei nº 14.133/2021 estabelece a instrução processual obrigatória para os processos administrativos de contratação direta (inexigibilidade e dispensa).

Dentre os elementos e documentos indispensáveis que devem instruir obrigatoriamente o processo de contratação direta, destaca-se:

* **A)** A realização prévia de audiência pública com a presença de todos os sindicatos de classe do Estado.
* **B)** A demonstração da compatibilidade da previsão de recursos orçamentários com o compromisso a ser assumido e a justificativa fundamentada de que o preço ofertado é condizente com os valores praticados no mercado.
* **C)** A autorização expressa do plenário do Tribunal de Contas previamente à assinatura de qualquer contrato por dispensa.
* **D)** A dispensa de elaboração de parecer jurídico quando a contratação direta envolver serviços de assessoria contábil.
* **E)** A certidão de inexistência de ações populares ajuizadas contra o gestor ordenador da despesa.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Audiência pública obrigatória aplica-se a licitações de grande vulto (art. 21), não sendo requisito genérico de contratação direta.
> - **B)** Correta. O art. 72, V e VII, da Lei nº 14.133/2021 exige categoricamente como elementos indispensáveis da contratação direta: a comprovação de que o contratado preenche os requisitos de habilitação, a demonstração da compatibilidade orçamentária e a **justificativa do preço**, mediante pesquisa de mercado ou comparação com contratações similares.
> - **C)** Incorreta. O controle do Tribunal de Contas é externo e exercido a posteriori ou concomitantemente, inexistindo chancela prévia de validade pelo plenário do TC.
> - **D)** Incorreta. O parecer jurídico do órgão de assessoramento legal da Administração é **obrigatório** em todo processo de contratação direta (art. 72, III), salvo hipóteses de baixo valor regulamentadas pelo órgão.
> - **E)** Incorreta. Ação popular contra gestor não impede contratações administrativas regulares respaldadas em lei.
>
> **Gabarito: B**"""

q10_03 = """### Questão 10 (FCC - Técnico de Controle Externo / Administrativa)
Determinado Secretário Municipal de Obras realizou, no intervalo de quatro meses, cinco contratações diretas sucessivas de diferentes fornecedores para o mesmo serviço de reforma contínua de calçadas de uma única avenida, cada contratação orçada no valor de R$ 50.000,00, sob a justificativa formal de dispensa de licitação em razão do valor reduzido (art. 75, I, da Lei nº 14.133/2021).

Analisando a regularidade dessa conduta perante as regras da Nova Lei de Licitações e o controle exercido pelo Tribunal de Contas:

* **A)** A conduta é plenamente lícita, pois cada contrato individual permaneceu abaixo do limite financeiro estipulado em lei para a contratação direta.
* **B)** A conduta configura ilícito administrativo de fracionamento indevido de despesa, uma vez que o somatório das despesas de mesma natureza realizadas no exercício financeiro pela mesma unidade gestora ultrapassou o teto legal de dispensa por valor.
* **C)** O fracionamento de despesa só é ilícito se envolver a contratação de fornecedores sediados em outros entes da Federação.
* **D)** O gestor está isento de responsabilidade caso demonstre que os pagamentos foram liquidados em contas bancárias distintas.
* **E)** A Lei nº 14.133/2021 revogou a proibição ao fracionamento de despesa para permitir compras fragmentadas a critério exclusivo da autoridade local.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Avaliar o limite de dispensa contrato a contrato de forma isolada, ignorando a identidade de objeto e exercício financeiro, é a manobra clássica de burla denominada **fracionamento indevido**.
> - **B)** Correta. O art. 75, § 1º, da Lei nº 14.133/2021 prescreve expressamente que, para fins de aferição dos limites de dispensa de licitação em razão do valor, deverá ser considerado o **somatório do que for despendido no exercício financeiro pela respectiva unidade gestora com objetos de mesma natureza**, entendidos como tais aqueles relativos a contratações no mesmo ramo de atividade. A fragmentação artificial para fugir da concorrência constitui fraude à lei e ilegalidade punível pelo Tribunal de Contas.
> - **C)** Incorreta. O fracionamento é ilícito independentemente da localização geográfica das empresas contratadas.
> - **D)** Incorreta. A pluralidade de contas bancárias não elide a unicidade da despesa orçamentária e a burla à licitação.
> - **E)** Incorreta. A proibição do fracionamento de despesas foi expressa e severamente reforçada na Lei nº 14.133/2021.
>
> **Gabarito: B**"""

q11_03 = """### Questão 11 (FGV - Analista de Controle Externo / TCE-GO)
A dispensa de licitação para contratação de obras e serviços em casos de emergência ou de calamidade pública, disciplinada pelo art. 75, VIII, da Lei nº 14.133/2021, destina-se a afastar o risco de dano a bens e pessoas.

A respeito dos limites e condicionamentos legais dessa hipótese de contratação direta emergencial, assinale a afirmativa correta.

* **A)** O contrato administrativo emergencial pode ter vigência de até cinco anos, permitida prorrogação sucessiva por conveniência do governante.
* **B)** A contratação emergencial fica restrita aos bens e serviços estritamente necessários ao atendimento da situação emergencial, com prazo máximo de um ano de vigência contratual, sendo expressamente vedada a prorrogação do contrato.
* **C)** A emergência fabricada decorrente de negligência continuada de gestores públicos convalida o contrato emergencial e extingue qualquer apuração disciplinar do servidor faltoso.
* **D)** Nas compras emergenciais por calamidade pública, a Administração está autorizada a recontratar a mesma empresa por dispensa emergencial consecutiva indefinidamente.
* **E)** A contratação direta por emergência dispensa a demonstração da adequação orçamentária prévia.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O teto legal da contratação emergencial na Lei nº 14.133/2021 é de **1 (um) ano**, sendo vedada qualquer prorrogação.
> - **B)** Correta. O art. 75, VIII, da Lei nº 14.133/2021 estatui que a dispensa de licitação nos casos de emergência ou calamidade pública aplica-se exclusivamente aos bens necessários ao atendimento da situação fática concreta, devendo a parcela de obras e serviços ser concluída no prazo máximo de **1 (um) ano**, contado da data de ocorrência da emergência, sendo **vedada a prorrogação dos respectivos contratos** e a recontratação de empresa já contratada com base no mesmo inciso.
> - **C)** Incorreta. O art. 75, § 6º, prevê que a caracterização de situação emergencial provocada pela inércia ou omissão de agentes públicos impõe a apuração de responsabilidade de quem deu causa à situação de desídia ("emergência fabricada").
> - **D)** Incorreta. A recontratação da mesma empresa sob o pálio da mesma emergência é expressamente proibida pela lei.
> - **E)** Incorreta. A regularidade orçamentária é requisito constitucional indeclinável de qualquer contratação pública (art. 167 da CF/88 e art. 72, V, da NLLC).
>
> **Gabarito: B**"""

# Inserções no arquivo 03 de trás para frente
ancora_5 = "### 5. Dispensa de Licitação (Art. 75 - Rol Taxativo)"
pos_5 = t03.find(ancora_5)
# Inserir Q11 antes da Questão 05 ou após a Questão 05
pos_q05 = t03.find("### Questão 05", pos_5)
pos_fontes = t03.find("## 🌐 Fontes Recomendadas", pos_q05)
assert pos_5 != -1 and pos_q05 != -1 and pos_fontes != -1
t03 = t03[:pos_fontes] + "\n\n" + q11_03.strip() + "\n\n---\n\n" + t03[pos_fontes:]

# Q10 inserida antes de Questão 05 na seção 5
t03 = t03[:pos_q05] + "\n\n" + q10_03.strip() + "\n\n---\n\n" + t03[pos_q05:]

ancora_3 = "### 3. Processo Administrativo de Contratação Direta (Art. 72)"
pos_3 = t03.find(ancora_3)
pos_4 = t03.find("### 4. Inexigibilidade de Licitação", pos_3)
assert pos_3 != -1 and pos_4 != -1
t03 = t03[:pos_4] + "\n\n" + q09_03.strip() + "\n\n---\n\n" + t03[pos_4:]

# Na seção 2 (Procedimentos Auxiliares), Q01 e Q02 já estão lá.
# Vamos inserir Q08 logo após a Questão 02, e Q07 antes da Questão 01
pos_q02 = t03.find("### Questão 02")
assert pos_q02 != -1
# Achar o final de Questão 02 (onde tem '---')
pos_end_q02 = t03.find("\n\n---\n\n", pos_q02)
assert pos_end_q02 != -1
t03 = t03[:pos_end_q02 + 7] + "\n\n" + q08_03.strip() + "\n\n---\n\n" + t03[pos_end_q02 + 7:]

pos_q01 = t03.find("### Questão 01")
assert pos_q01 != -1
t03 = t03[:pos_q01] + "\n\n" + q07_03.strip() + "\n\n---\n\n" + t03[pos_q01:]

ancora_1 = "### 1. Distinção Fundamental: Inexigibilidade x Dispensa de Licitação"
pos_1 = t03.find(ancora_1)
pos_2 = t03.find("### 2. Procedimentos Auxiliares", pos_1)
assert pos_1 != -1 and pos_2 != -1
t03 = t03[:pos_2] + "\n\n" + q06_03.strip() + "\n\n---\n\n" + t03[pos_2:]

qs_03 = re.findall(r"### Questão (\d+)", t03)
print("Questões no arquivo 03 do Módulo 16:", qs_03)
assert len(qs_03) == 11
assert sorted(qs_03) == ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']

with open(f03_path, "w", encoding="utf-8") as f:
    f.write(t03)

print("Arquivo 03 do Módulo 16 gravado com sucesso! Total: 11 questões.")
