# -*- coding: utf-8 -*-
import os
import re

BASE_DIR = "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/15_nocoes_de_direito_administrativo"

# ==============================================================================
# FILE 04: 04_servicos_publicos_bens_e_responsabilidade_civil.md
# ==============================================================================
f04_path = f"{BASE_DIR}/04_servicos_publicos_bens_e_responsabilidade_civil.md"
with open(f04_path, "r", encoding="utf-8") as f:
    t04 = f.read()

assert "### Questão 01" in t04
assert "### Questão 02" in t04
assert "### Questão 03" in t04
assert "### Questão 04" in t04
assert "### Questão 05" in t04

q06_04 = """### Questão 06 (FCC - Analista Judiciário - Área Judiciária)
Motorista de ambulância pertencente à Secretaria de Saúde de determinado Estado da Federação, ao conduzir o veículo oficial em velocidade excessiva e com a sirene desligada durante o retorno de uma oficina mecânica, colidiu com veículo particular parado regularmente no semáforo, causando graves danos materiais ao proprietário.

Considerando o regramento constitucional sobre a responsabilidade civil do Estado (art. 37, § 6º, da CF/88) e a jurisprudência dominante, o proprietário do veículo lesado:

* **A)** Deve ajuizar a ação indenizatória diretamente e com exclusividade contra o motorista da ambulância, demonstrando sua culpa grave.
* **B)** Tem direito a ser indenizado pelo Estado com base na responsabilidade civil objetiva, fundada na Teoria do Risco Administrativo, prescindindo de comprovação de dolo ou culpa do agente público condutor.
* **C)** Só poderá obter indenização do Estado se comprovar dolo ou desvio de poder por parte da Secretaria de Saúde.
* **D)** Terá seu pleito sumariamente indeferido caso o Estado demonstre que o motorista agiu em estrito desvio de suas funções institucionais no momento do abalroamento.
* **E)** Submete-se à teoria da responsabilidade civil subjetiva comum do Código Civil, incumbindo-lhe o ônus de provar a culpa do motorista e a falha de manutenção da via.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A teor do Tema 940 de Repercussão Geral do STF, a ação indenizatória por danos causados por agente público no exercício de suas funções deve ser ajuizada **diretamente em face do Estado** ou da pessoa jurídica de direito privado prestadora de serviço público, sendo vedada a inclusão originária do servidor público no polo passivo (Teoria da Dupla Garantia).
> - **B)** Correta. O art. 37, § 6º, da CF/88 consagra a **responsabilidade civil objetiva** do Estado na modalidade do Risco Administrativo para condutas comissivas de seus agentes. Para a procedência do pedido indenizatório, a vítima precisa provar apenas: (1) a conduta oficial comissiva; (2) o dano patrimonial sofrido; e (3) o nexo de causalidade direto entre ambos, sendo dispensável perquirir dolo ou culpa do motorista.
> - **C)** Incorreta. A responsabilidade objetiva independe de dolo ou culpa da Administração.
> - **D)** Incorreta. O Estado responde objetivamente pelos atos de seus agentes públicos que atuem nessa qualidade, mesmo que excedam ou desviem formalmente suas atribuições funcionais.
> - **E)** Incorreta. A teoria subjetiva é exceção aplicável ao servidor na eventual ação regressiva de regresso, e não à pretensão da vítima frente à Fazenda Pública.
>
> **Gabarito: B**"""

q07_04 = """### Questão 07 (FGV - Auditor de Controle Externo / TCE-SC)
A Teoria do Risco Integral diferencia-se substancialmente da Teoria do Risco Administrativo no que concerne à admissão de excludentes de responsabilidade civil estatal. A respeito das hipóteses excepcionais em que o ordenamento constitucional e legal pátrio adota o Risco Integral, assinale a afirmativa correta.

* **A)** Na Teoria do Risco Integral, o Estado responde pelo dano mesmo que haja culpa exclusiva da vítima, fato de terceiro ou caso fortuito/força maior, sendo vedada a alegação de qualquer causa excludente do nexo causal.
* **B)** O ordenamento jurídico brasileiro aplica a Teoria do Risco Integral como regra geral para todos os acidentes de trânsito envolvendo veículos da polícia militar.
* **C)** A responsabilidade civil do Estado por danos nucleares admite expressamente a excludente de caso fortuito e de culpa concorrente da vítima para mitigar o dever estatal de indenizar.
* **D)** Em caso de assalto à mão armada ocorrido dentro de agência bancária privada, incide a Teoria do Risco Integral contra a Fazenda Pública Estadual por deficiência de segurança pública.
* **E)** Danos decorrentes de atos de terrorismo contra aeronaves de matrícula brasileira operando no exterior são regidos pela Teoria da Falta do Serviço (faute du service), não cabendo assunção integral de risco pela União.

> **Comentário Detalhado:**
>
> - **A)** Correta. A Teoria do Risco Integral impõe ao Poder Público a obrigação de indenizar sem qualquer possibilidade de invocação de excludentes de nexo de causalidade (culpa exclusiva da vítima, caso fortuito, força maior ou fato de terceiro). O Estado atua como garantidor universal e irrestrito do risco consumado.
> - **B)** Incorreta. Acidentes de trânsito com viaturas policiais submetem-se à Teoria do Risco Administrativo comum (art. 37, § 6º, CF), admitindo a prova de excludentes como culpa exclusiva da vítima.
> - **C)** Incorreta. O art. 21, XXIII, 'd', da CF/88 consagra a responsabilidade civil por danos nucleares de forma objetiva pura e integral, sem admissão de excludentes.
> - **D)** Incorreta. A responsabilidade por segurança pública em espaços privados decorre de suposta omissão estatal genérica, exigindo a teoria subjetiva da falta do serviço (culpa anônima), e não risco integral.
> - **E)** Incorreta. A Lei Federal nº 10.744/2003 estabelece que a União assume a responsabilidade civil por danos a terceiros provocados por atentados terroristas contra aeronaves brasileiras, aplicando-se a teoria do risco integral.
>
> **Gabarito: A**"""

q08_04 = """### Questão 08 (FCC - Procurador do Estado)
Sobre os princípios que regem a prestação de serviços públicos e o regime de corte de fornecimento por inadimplemento do usuário, à luz da Lei nº 8.987/1995 e da jurisprudência consolidada do Superior Tribunal de Justiça (STJ), assinale a afirmativa correta.

* **A)** O princípio da continuidade veda terminantemente a suspensão da prestação do serviço público sob qualquer pretexto, mesmo na hipótese de inadimplemento reiterado do usuário particular.
* **B)** É legítima a interrupção do fornecimento de serviço público essencial (como energia elétrica ou água) por inadimplemento do consumidor, desde que haja aviso prévio formal e que o débito seja atual, não se admitindo o corte por dívidas pretéritas consolidadas.
* **C)** O serviço público pode ser interrompido sem aviso prévio em virtude de inadimplemento de fatura vencida há mais de dois anos.
* **D)** O princípio da modicidade tarifária autoriza a concessionária a aumentar unilateralmente a tarifa básica sempre que julgar insatisfatória a sua margem de lucro operacional.
* **E)** As concessionárias de serviço público podem suspender o fornecimento de energia a hospitais públicos e unidades de pronto atendimento por inadimplemento de fatura sem qualquer restrição jurídica.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O art. 6º, § 3º, da Lei nº 8.987/1995 prescreve expressamente que **não se caracteriza descontinuidade do serviço** a sua interrupção em situação de emergência ou, após prévio aviso, por razões de ordem técnica/segurança ou por inadimplemento do usuário.
> - **B)** Correta. Jurisprudência sumulada e vinculante do STJ (Tema Repetitivo 699/STJ): é legítimo o corte no fornecimento de serviços essenciais por inadimplemento, condicionado a aviso prévio e adstrito a **contas atuais** (mês de consumo recente). Débitos pretéritos devem ser cobrados pelas vias ordinárias de cobrança judicial, sendo ilegal o corte coercitivo por dívida antiga.
> - **C)** Incorreta. É absolutamente obrigatório o prévio aviso e é vedado o corte para recuperação coativa de dívidas pretéritas (antigas).
> - **D)** Incorreta. O reajuste e a revisão tarifária subordinam-se estritamente aos índices e fórmulas pactuados no contrato de concessão e homologados pela agência reguladora, visando a preservar a modicidade para a população e o equilíbrio econômico-financeiro.
> - **E)** Incorreta. A interrupção de serviço essencial que atinja serviços públicos vitais e inadiáveis (como UTIs de hospitais públicos) é ilegítima por colocar em risco a vida e a dignidade humana.
>
> **Gabarito: B**"""

q09_04 = """### Questão 09 (FGV - Analista de Gestão / Auditoria)
A respeito dos regimes de delegação de serviços públicos previstos na Lei nº 8.987/1995, compare a concessão comum de serviço público e a permissão de serviço público.

Assinale a opção que apresenta a distinção jurídica correta entre esses institutos.

* **A)** A concessão comum prescinde de licitação prévia, ao passo que a permissão exige obrigatoriamente licitação na modalidade concurso.
* **B)** A concessão é celebrada mediante contrato administrativo bilateral, com prazo determinado e outorga a pessoa jurídica ou consórcio de empresas; a permissão formaliza-se mediante contrato de adesão, ostenta caráter precário e revogável unilateralmente pelo poder concedente, podendo ser outorgada a pessoa física ou jurídica.
* **C)** A permissão de serviço público é conferida por meio de ato administrativo unilateral discricionário imune a qualquer fiscalização do poder público.
* **D)** Tanto a concessão quanto a permissão admitem a outorga exclusiva a pessoas físicas, sendo vedada a participação de consórcios empresariais em ambas.
* **E)** Na concessão de serviço público, a extinção antecipada por razões de interesse público denomina-se caducidade, e independe de lei autorizativa específica ou de indenização prévia.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Ambas exigem prévia licitação (art. 175 da CF/88 e arts. 2º e 40 da Lei nº 8.987/1995).
> - **B)** Correta. Nos termos do art. 2º, II e IV, e art. 40 da Lei nº 8.987/1995: a **concessão** é a delegação contratual bilateral a pessoa jurídica ou consórcio de empresas, com prazo determinado; a **permissão** formaliza-se a título precário mediante **contrato de adesão**, podendo ser deferida tanto a pessoa física quanto a pessoa jurídica, sempre precedida de licitação.
> - **C)** Incorreta. Embora qualificada pela precariedade, a permissão de serviço público no Brasil formaliza-se sob a natureza de contrato de adesão (art. 40 da Lei nº 8.987/1995), plenamente submetida à fiscalização regulatória.
> - **D)** Incorreta. A concessão comum não pode ser delegada a pessoas físicas; exige pessoa jurídica ou consórcio de empresas.
> - **E)** Incorreta. A extinção da concessão por interesse público superveniente é a **encampação** (ou resgate), que exige obrigatoriamente lei autorizativa específica e prévio pagamento de indenização. Caducidade é a extinção por inexecução culposa da concessionária.
>
> **Gabarito: B**"""

q10_04 = """### Questão 10 (FCC - Técnico de Controle Externo)
O Código Civil brasileiro, em seu art. 99, classifica os bens públicos em três categorias fundamentais: bens de uso comum do povo, bens de uso especial e bens dominicais.

Em relação ao regime jurídico de alienação e fruição dessas categorias de bens, é correto afirmar:

* **A)** Os bens dominicais são inalienáveis em qualquer circunstância, tendo em vista que integram o patrimônio indisponível da pessoa jurídica de direito público.
* **B)** Os bens de uso comum do povo (como rios, mares, estradas e praças) e os de uso especial (como edifícios onde funcionam tribunais e escolas públicas) são inalienáveis enquanto conservarem a sua afetação ao interesse público.
* **C)** Os bens públicos dominicais podem ser adquiridos por particulares mediante usucapião ordinária após posse mansa e pacífica por mais de vinte anos.
* **D)** A utilização de bens de uso comum do povo é sempre gratuita, sendo inconstitucional a instituição de cobrança de pedágio em rodovias públicas.
* **E)** Os bens de uso especial desafetados passam automaticamente a pertencer à categoria de bens de uso comum do povo.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Os bens dominicais constituem o patrimônio disponível do Estado (art. 99, III, CC); eles **podem ser alienados**, desde que observadas as exigências legais (interesse público, avaliação prévia, autorização legislativa e licitação, art. 76 da Lei nº 14.133/2021 e art. 101 do CC).
> - **B)** Correta. O art. 100 do Código Civil prescreve expressamente que os bens públicos de uso comum do povo e os de uso especial são inalienáveis enquanto mantiverem a sua qualificação (afetação). Para que possam ser vendidos ou doados, precisam passar previamente pelo processo de desafetação, ingressando na classe dos bens dominicais.
> - **C)** Incorreta. Todos os bens públicos, indistintamente (sejam de uso comum, especial ou dominicais), são **imprescritíveis**, não podendo ser adquiridos por usucapião (art. 183, § 3º, e art. 191, parágrafo único, CF/88; Súmula 340/STF).
> - **D)** Incorreta. O art. 103 do Código Civil e o art. 150, V, da CF/88 autorizam que o uso de bens comuns seja gratuito ou retribuído (oneroso), como ocorre expressamente na cobrança legítima de pedágio.
> - **E)** Incorreta. Quando um bem de uso especial ou de uso comum perde sua destinação pública (desafetação), ele converte-se em **bem dominical**, e não em bem de uso comum.
>
> **Gabarito: B**"""

q11_04 = """### Questão 11 (FGV - Analista de Controle Externo / TCE)
A afetação e a desafetação de bens públicos expressam a consagração ou a desvinculação de determinado bem a uma finalidade pública concreta. Sobre as formas de ocorrência e os efeitos jurídicos da afetação e desafetação, assinale a afirmativa correta.

* **A)** A afetação de um bem público somente pode ocorrer de forma tácita, sendo nula a afetação realizada por meio de lei formal.
* **B)** A desafetação decorrente de fato da natureza (como a destruição total e definitiva de um prédio público por incêndio incontrolável) torna o bem imprestável, extinguindo sua utilidade como bem de uso especial.
* **C)** A simples elaboração de projeto arquitetônico sem qualquer início de obra ou uso efetivo é suficiente para consumar a afetação fática material de um terreno público.
* **D)** O Poder Judiciário pode determinar de ofício a desafetação de um hospital público para fins de penhora judicial e pagamento de precatórios atrasados.
* **E)** Bens dominicais não admitem afetação superveniente, conservando para sempre seu caráter patrimonial disponível.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A afetação pode ser **expressa** (por lei ou ato administrativo) ou **tácita/fática** (decorrente da utilização material e direta do bem para a prestação do serviço público).
> - **B)** Correta. A desafetação pode decorrer de ato formal (lei ou decreto desafetando) ou de evento da natureza / fato material irreversível (como a ruína total ou destruição permanente de um edifício público de uso especial), cessando a afetação do imóvel à finalidade originária.
> - **C)** Incorreta. Meras expectativas, plantas ou projetos teóricos não afetam materialmente o imóvel; a afetação fática requer o início concreto da destinação pública ou uso efetivo pela coletividade.
> - **D)** Incorreta. O Judiciário não tem poder de desafetar bens públicos discricionariamente; ademais, incide a regra da impenhorabilidade absoluta dos bens públicos (art. 100 da CF/88), sujeitando-se as execuções contra a Fazenda exclusivamente ao regime de precatórios ou RPV.
> - **E)** Incorreta. Os bens dominicais podem a qualquer momento ser afetados, bastando que a Administração instale neles uma repartição pública ou praça, transmudando-os em bens de uso especial ou comum.
>
> **Gabarito: B**"""

# Inserções no arquivo 04
ancora_32 = "### 3.2 Fenômeno da Afetação e Desafetação"
pos_32 = t04.find(ancora_32)
pos_33 = t04.find("### 3.3 Prerrogativas do Regime", pos_32)
assert pos_32 != -1 and pos_33 != -1
t04 = t04[:pos_33] + "\n\n" + q11_04.strip() + "\n\n---\n\n" + t04[pos_33:]

ancora_31 = "### 3.1 Classificação Quanto à Destinação (Código Civil, art. 99)"
pos_31 = t04.find(ancora_31)
pos_32_new = t04.find("### 3.2 Fenômeno da Afetação", pos_31)
assert pos_31 != -1 and pos_32_new != -1
t04 = t04[:pos_32_new] + "\n\n" + q10_04.strip() + "\n\n---\n\n" + t04[pos_32_new:]

ancora_22 = "### 2.2 Concessão Comum e Permissão de Serviço Público (Lei nº 8.987/1995)"
pos_22 = t04.find(ancora_22)
pos_23 = t04.find("### 2.3 Formas de Extinção", pos_22)
assert pos_22 != -1 and pos_23 != -1
t04 = t04[:pos_23] + "\n\n" + q09_04.strip() + "\n\n---\n\n" + t04[pos_23:]

ancora_21 = "### 2.1 Princípios do Serviço Público Adequado"
pos_21 = t04.find(ancora_21)
pos_22_new = t04.find("### 2.2 Concessão Comum", pos_21)
assert pos_21 != -1 and pos_22_new != -1
t04 = t04[:pos_22_new] + "\n\n" + q08_04.strip() + "\n\n---\n\n" + t04[pos_22_new:]

ancora_14 = "### 1.4 Teoria do Risco Integral e suas Hipóteses Excepcionais"
pos_14 = t04.find(ancora_14)
pos_15 = t04.find("### 1.5 Responsabilidade por Omissão", pos_14)
assert pos_14 != -1 and pos_15 != -1
t04 = t04[:pos_15] + "\n\n" + q07_04.strip() + "\n\n---\n\n" + t04[pos_15:]

ancora_12 = "### 1.2 O Art. 37, § 6º da CF/88 e os Elementos da Responsabilidade Objetiva"
pos_12 = t04.find(ancora_12)
pos_13 = t04.find("### 1.3 Teoria do Risco Administrativo", pos_12)
assert pos_12 != -1 and pos_13 != -1
t04 = t04[:pos_13] + "\n\n" + q06_04.strip() + "\n\n---\n\n" + t04[pos_13:]

qs_04 = re.findall(r"### Questão (\d+)", t04)
print("Questões no arquivo 04:", qs_04)
assert len(qs_04) == 11
assert sorted(qs_04) == ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']

with open(f04_path, "w", encoding="utf-8") as f:
    f.write(t04)

print("Arquivo 04 gravado com sucesso! Total: 11 questões.")
