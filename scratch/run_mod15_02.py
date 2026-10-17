# -*- coding: utf-8 -*-
import os
import re

BASE_DIR = "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/15_nocoes_de_direito_administrativo"
f02_path = f"{BASE_DIR}/02_organizacao_administrativa_e_poderes.md"

with open(f02_path, "r", encoding="utf-8") as f:
    text = f.read()

assert "### Questão 01" in text
assert "### Questão 02" in text
assert "### Questão 03" in text
assert "### Questão 04" in text
assert "### Questão 05" in text

q06_02 = """### Questão 06 (FCC - Auditor Fiscal da Receita Estadual)
No que tange às técnicas de organização e estruturação da Administração Pública, a doutrina e a jurisprudência estabelecem distinções fundamentais entre os institutos da centralização, descentralização, concentração e desconcentração.

A respeito desses conceitos, é correto afirmar:

* **A)** A descentralização consiste na distribuição interna de competências decisórias dentro de uma mesma pessoa jurídica, resultando na criação de órgãos públicos desprovidos de personalidade jurídica própria.
* **B)** A desconcentração pressupõe a transferência da titularidade e/ou da execução de serviços públicos para uma pessoa jurídica distinta, seja ela integrante da Administração Indireta ou um particular colaborador.
* **C)** Na descentralização por serviços, funcional ou outorga, o Poder Público cria, por meio de lei formal, uma entidade com personalidade jurídica própria (autarquia), transferindo-lhe a titularidade e a execução do serviço.
* **D)** A criação de ministérios, secretarias estaduais e diretorias setoriais constitui típica hipótese de descentralização política e territorial.
* **E)** Entre a Administração Direta e os órgãos criados por desconcentração inexiste qualquer vínculo de hierarquia ou subordinação funcional.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A distribuição interna de competências no âmbito da mesma pessoa jurídica com criação de órgãos denomina-se **desconcentração** (mnemônico: desCOncentração = COm criação de Órgãos), e não descentralização.
> - **B)** Incorreta. A transferência de competências para outra pessoa jurídica (distinta do ente matriz) consubstancia a **descentralização** (mnemônico: desCENtralização = criação de ENtidades), e não desconcentração.
> - **C)** Correta. A descentralização por serviços, funcional, técnica ou por outorga ocorre quando o Estado transfere, mediante previsão legal expressa, tanto a titularidade quanto a execução de determinado serviço para uma entidade de direito público da Administração Indireta (ex.: autarquias).
> - **D)** Incorreta. Ministérios e secretarias são órgãos públicos criados por **desconcentração** administrativa interna no âmbito da União e dos Estados, respectivamente.
> - **E)** Incorreta. Na desconcentração há forte e plena relação de **hierarquia e subordinação** entre o órgão superior e os órgãos inferiores dele derivados.
>
> **Gabarito: C**"""

q07_02 = """### Questão 07 (FGV - Analista de Controle Externo / TCE)
As autarquias constituem pessoas jurídicas de direito público integrantes da Administração Indireta, criadas por lei específica para o desempenho de atividades típicas de Estado. Sobre o regime jurídico aplicável às autarquias comuns e às autarquias em regime especial (agências reguladoras), assinale a afirmativa correta.

* **A)** As autarquias adquirem personalidade jurídica a partir do registro de seus atos constitutivos no Cartório de Registro Civil de Pessoas Jurídicas ou na Junta Comercial.
* **B)** Os bens das autarquias ostentam a natureza de bens públicos, gozando de inalienabilidade relativa, impenhorabilidade, imprescritibilidade (não sujeição a usucapião) e não oneração.
* **C)** Os dirigentes de agências reguladoras podem ser exonerados ad nutum e sem justa causa pelo Chefe do Poder Executivo a qualquer momento de seu mandato.
* **D)** As decisões técnicas finais proferidas pelas agências reguladoras no exercício de suas competências normativas submetem-se a recurso hierárquico impróprio ordinário perante os Ministérios de Estado supervisores.
* **E)** As autarquias subordinam-se hierarquicamente aos órgãos centrais do Poder Executivo, cabendo a estes avocar e revogar seus atos a juízo de conveniência política.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. As autarquias são pessoas jurídicas de direito público; sua existência e personalidade jurídica iniciam-se com a vigência da própria **lei específica criadora** (art. 37, XIX, CF/88), independentemente de registro cartorário.
> - **B)** Correta. Por integrarem o patrimônio de pessoas jurídicas de direito público, os bens autárquicos são legalmente qualificados como bens públicos (art. 98 do Código Civil), sendo impenhoráveis, imprescritíveis (não passíveis de usucapião, Súmula 340/STF) e gravados por inalienabilidade relativa.
> - **C)** Incorreta. Os dirigentes das agências reguladoras possuem estabilidade durante mandato fixo estabelecido em lei (quarentena e processo de destituição estrito), vedada a exoneração ad nutum para resguardar a autonomia técnica e decisória (Lei nº 13.848/2019).
> - **D)** Incorreta. Em regra, não cabe recurso hierárquico ao Ministério supervisor contra decisão de mérito técnico da agência (recurso hierárquico impróprio só é cabível em hipóteses excepcionais expressamente previstas em lei ou desvio de finalidade/usurpação de competência).
> - **E)** Incorreta. Não existe relação de subordinação hierárquica entre a Administração Direta e as autarquias, mas tão somente controle finalístico (tutela administrativa ou supervisão ministerial) nos limites estritos da lei.
>
> **Gabarito: B**"""

q08_02 = """### Questão 08 (FGV - Analista Jurídico de Controle Externo / TCE-GO)
A Lei nº 13.303/2016 (Estatuto Jurídico das Empresas Públicas e Sociedades de Economia Mista) estabeleceu regras rigorosas de governança corporativa, compliance e transparência para as estatais. À luz dessa legislação e do regramento constitucional sobre estatais, assinale a afirmativa correta.

* **A)** A sociedade de economia mista pode adotar qualquer forma societária admitida em direito, desde que a totalidade de seu capital pertença a entes públicos.
* **B)** A empresa pública deve obrigatoriamente constituir-se sob a forma de sociedade anônima (S/A), admitindo-se a participação minoritária de capital privado com direito a voto.
* **C)** As empresas públicas e sociedades de economia mista exploradoras de atividade econômica em sentido estrito submetem-se ao regime jurídico próprio das empresas privadas, inclusive quanto aos direitos e obrigações civis, comerciais, trabalhistas e tributários.
* **D)** As empresas estatais prestadoras de serviços públicos próprios do Estado estão sujeitas à falência e insolvência civil de acordo com o regime concursal privado comum.
* **E)** As causas cíveis em que uma sociedade de economia mista federal for parte ou interveniente tramitam obrigatoriamente perante a Justiça Federal, a teor do art. 109, I, da CF/88.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A sociedade de economia mista deve constituir-se **obrigatoriamente sob a forma de sociedade por ações (S/A)**, com maioria do capital votante pertencente ao Poder Público, nos termos da Lei nº 13.303/2016 e do Decreto-Lei nº 200/1967.
> - **B)** Incorreta. A empresa pública admite **qualquer forma societária** admitida em direito (ex.: S/A, Ltda., empresa unipessoal) e seu capital deve ser **100% público** (União, Estados, DF, Municípios ou outras entidades da Administração Indireta).
> - **C)** Correta. O art. 173, § 1º, II, da CF/88 determina que a estatal exploradora de atividade econômica sujeita-se ao regime jurídico próprio das empresas privadas, inclusive quanto aos direitos e obrigações civis, comerciais, trabalhistas e tributários, para assegurar a livre concorrência e evitar vantagens concorrenciais indevidas.
> - **D)** Incorreta. O art. 2º, I, da Lei nº 11.101/2005 estatui que a lei de recuperação judicial e falência **não se aplica** a empresa pública e sociedade de economia mista.
> - **E)** Incorreta. A teor da Súmula 556 do STF e do art. 109, I, da CF/88, as ações em que figurem sociedades de economia mista federais (como o Banco do Brasil e a Petrobras) são julgadas na **Justiça Comum Estadual**, ressalvada a Justiça do Trabalho para lides trabalhistas.
>
> **Gabarito: C**"""

q09_02 = """### Questão 09 (FCC - Auditor de Controle Externo)
O controle finalístico, tutela administrativa ou supervisão ministerial exercido pela Administração Direta sobre as pessoas jurídicas integrantes da Administração Indireta caracteriza-se por:

* **A)** Relação de subordinação hierárquica plena, facultando ao ente criador revogar de ofício atos discricionários da entidade descentralizada por motivos de pura conveniência administrativa.
* **B)** Vinculação institucional estrita aos limites previstos em lei (princípio da especialidade), não se presumindo competências de controle que não estejam expressamente positivadas.
* **C)** Inexistência de qualquer poder fiscalizatório ou orçamentário sobre as estatais e autarquias, assegurando-lhes soberania político-administrativa absoluta.
* **D)** Poder disciplinar automático e direto da autoridade ministerial para demitir empregados celetistas de empresas públicas sem necessidade de procedimento motivado prévio.
* **E)** Substituição integral da competência fiscalizatória exercida pelo Tribunal de Contas, que fica dispensado de auditar as entidades supervisionadas.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Não há subordinação hierárquica entre a Administração Direta e os entes da Indireta, mas sim mera **vinculação legal**. A Administração Direta não pode revogar atos discricionários legítimos das autarquias sob critério de conveniência ou oportunidade própria.
> - **B)** Correta. A tutela administrativa (controle finalístico ou supervisão ministerial) submete-se ao princípio da especialidade e da legalidade estrita. Por inexistir hierarquia, o controle restringe-se às hipóteses, matérias e instrumentos expressamente autorizados em lei, não podendo ser presumido ou extrapolado.
> - **C)** Incorreta. A supervisão ministerial impõe acompanhamento orçamentário, metas de desempenho, conformidade com políticas públicas setoriais e prestação de contas, não havendo falar em "soberania absoluta".
> - **D)** Incorreta. A competência disciplinar sobre os empregados é da própria pessoa jurídica empregadora (a empresa estatal), e não do Ministério supervisor.
> - **E)** Incorreta. O controle interno/supervisão ministerial jamais substitui nem afasta a jurisdição constitucional e autônoma exercida pelas Cortes de Contas (art. 71, CF/88).
>
> **Gabarito: B**"""

q10_02 = """### Questão 10 (FGV - Analista de Controle Externo / Auditoria)
Determinada entidade privada sem fins lucrativos, criada por iniciativa de setor empresarial e instituída por lei para prestar serviços de assistência social e formação profissional aos trabalhadores da respectiva categoria (Serviço Social Autônomo - integrante do chamado "Sistema S"), foi objeto de representação perante o Tribunal de Contas.

A respeito da natureza jurídica e do controle público sobre as entidades do Sistema S, assinale a afirmativa correta.

* **A)** Integram a Administração Pública Indireta, ostentando natureza jurídica de autarquias corporativas especiais.
* **B)** Não se submetem à fiscalização do Tribunal de Contas, uma vez que sua personalidade jurídica é de direito privado e seus dirigentes não são servidores públicos.
* **C)** Submetem-se ao controle finalístico do Tribunal de Contas no que tange à aplicação dos recursos provenientes de contribuições parafiscais, embora não estejam obrigadas a seguir a Lei de Licitações comum, devendo editar e aplicar regulamentos próprios baseados nos princípios da impessoalidade e publicidade.
* **D)** Seus empregados são regidos pelo estatuto dos servidores públicos civis do Estado, com direito à estabilidade do art. 41 da CF/88.
* **E)** Estão obrigadas a realizar concurso público rigoroso nos moldes do art. 37, II, da CF/88 para a contratação de seu quadro de empregados.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. As entidades do Sistema S (SESI, SENAI, SESC, SENAC, etc.) são pessoas jurídicas de direito privado, paraestatais e pertencentes ao Terceiro Setor, não integrando a Administração Direta nem a Indireta.
> - **B)** Incorreta. Por arrecadarem e gerirem contribuições parafiscais (recursos públicos de natureza tributária), estão sujeitas à prestação de contas e à jurisdição fiscalizatória dos Tribunais de Contas (art. 70, parágrafo único, CF/88).
> - **C)** Correta. Jurisprudência pacífica do STF e do TCU (Súmula TCU nº 230 e ADI 1.864/STF): as entidades do Sistema S gerenciam recursos parafiscais e prestam contas às Cortes de Contas; contudo, não se sujeitam à lei geral de licitações, mas sim aos seus regulamentos próprios de licitações e contratos, balizados pelos princípios do art. 37 da CF/88.
> - **D)** Incorreta. Seus empregados são regidos pela CLT (Consolidação das Leis do Trabalho) e não possuem direito à estabilidade constitucional do art. 41 da CF/88.
> - **E)** Incorreta. Conforme jurisprudência consolidada do STF (ADI 3.026 e RE 789.874), o Sistema S não está obrigado a concurso público formal do art. 37, II, mas sim a processo seletivo público objetivo e simplificado.
>
> **Gabarito: C**"""

q11_02 = """### Questão 11 (FCC - Técnico de Controle Externo)
Sobre o poder disciplinar e a sua articulação com o poder hierárquico na Administração Pública, considere a seguinte hipótese: servidor público estável cometeu falta funcional grave devidamente apurada em processo administrativo disciplinar (PAD) com observância do contraditório e da ampla defesa, cuja tipificação legal comina com exclusividade a penalidade de demissão.

Diante da constatação inequívoca da infração legal grave, a autoridade julgadora competente:

* **A)** Pode, por juízo discricionário de conveniência e oportunidade, deixar de aplicar a penalidade de demissão se considerar o servidor eficiente em suas rotinas de trabalho.
* **B)** Tem o dever de aplicar a penalidade de demissão prevista em lei, haja vista que o poder disciplinar vincula a autoridade julgadora quanto à aplicação da sanção legalmente estipulada diante de conduta ilícita comprovada.
* **C)** Deve converter a demissão em advertência verbal, em atenção exclusiva ao princípio da insignificância administrativa.
* **D)** Exerce poder discricionário absoluto na fixação da sanção, independentemente das hipóteses taxativas cominadas no estatuto funcional aplicável.
* **E)** Fica impedida de punir o servidor caso o ato ilícito também configure crime comum que ainda não tenha transitado em julgado no juízo penal.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Comprovada a falta funcional punível com demissão, a autoridade competente não possui discricionariedade para perdoar a infração ou deixar de punir com base em mérito de conveniência. Trata-se de poder-dever vinculado.
> - **B)** Correta. Embora a tipificação de infrações disciplinares muitas vezes envolva termos indeterminados, uma vez tipificada de forma incontroversa a conduta cominada com demissão, o ato de aplicação da sanção torna-se **vinculado**, não restando margem de escolha à autoridade julgadora senão demitir o servidor faltoso (art. 128 e 132 da Lei nº 8.112/1990 e legislação correlata de Goiás).
> - **C)** Incorreta. A autoridade não pode comutar ou atenuar a pena para advertência fora das hipóteses e limites estritamente traçados em lei.
> - **D)** Incorreta. As penalidades administrativas sujeitam-se ao princípio da legalidade estrita e da proporcionalidade; a fixação da pena não é arbitrária nem goza de discricionariedade absoluta.
> - **E)** Incorreta. Vigora a independência das instâncias administrativa e penal, de modo que a Administração Pública pode punir disciplinarmente o servidor antes mesmo de qualquer desfecho do processo criminal, ressalvada a hipótese de absolvição penal categórica fundada em negativa de autoria ou inexistência material do fato.
>
> **Gabarito: B**"""

# Inserções no arquivo 02
ancora_41 = "### 4.3 Poder Disciplinar e Sanções Funcionais"
pos_41 = text.find(ancora_41)
pos_44 = text.find("### 4.4 Poder Regulamentar", pos_41)
assert pos_41 != -1 and pos_44 != -1
text = text[:pos_44] + "\n\n" + q11_02.strip() + "\n\n---\n\n" + text[pos_44:]

ancora_31 = "### 3.1 Serviços Sociais Autônomos (Sistema S)"
pos_31 = text.find(ancora_31)
pos_32 = text.find("### 3.2 Organizações Sociais", pos_31)
assert pos_31 != -1 and pos_32 != -1
text = text[:pos_32] + "\n\n" + q10_02.strip() + "\n\n---\n\n" + text[pos_32:]

ancora_25 = "### 2.5 Controle Finalístico, Tutela e Supervisão Ministerial"
pos_25 = text.find(ancora_25)
pos_30 = text.find("## 3. O Terceiro Setor", pos_25)
assert pos_25 != -1 and pos_30 != -1
text = text[:pos_30] + "\n\n" + q09_02.strip() + "\n\n---\n\n" + text[pos_30:]

ancora_24 = "### 2.4 O Estatuto Jurídico das Estatais (Lei nº 13.303/2016)"
pos_24 = text.find(ancora_24)
pos_25_new = text.find("### 2.5 Controle Finalístico", pos_24)
assert pos_24 != -1 and pos_25_new != -1
text = text[:pos_25_new] + "\n\n" + q08_02.strip() + "\n\n---\n\n" + text[pos_25_new:]

ancora_21 = "### 2.1 Autarquias e Autarquias de Regime Especial"
pos_21 = text.find(ancora_21)
pos_22 = text.find("### 2.2 Fundações Públicas", pos_21)
assert pos_21 != -1 and pos_22 != -1
text = text[:pos_22] + "\n\n" + q07_02.strip() + "\n\n---\n\n" + text[pos_22:]

ancora_12 = "### 1.2 Desconcentração e a Criação de Órgãos Públicos"
pos_12 = text.find(ancora_12)
pos_13 = text.find("### 1.3 Quadro Distintivo", pos_12)
assert pos_12 != -1 and pos_13 != -1
text = text[:pos_13] + "\n\n" + q06_02.strip() + "\n\n---\n\n" + text[pos_13:]

final_qs = re.findall(r"### Questão (\d+)", text)
print("Questões no arquivo 02:", final_qs)
assert len(final_qs) == 11
assert sorted(final_qs) == ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']

with open(f02_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Arquivo 02 gravado com sucesso! Total: 11 questões.")
