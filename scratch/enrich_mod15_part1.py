# -*- coding: utf-8 -*-
import os
import re

BASE_DIR = "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/15_nocoes_de_direito_administrativo"

# ==============================================================================
# FILE 01: 01_regime_juridico_principios_e_lindb.md
# ==============================================================================
f01_path = f"{BASE_DIR}/01_regime_juridico_principios_e_lindb.md"
with open(f01_path, "r", encoding="utf-8") as f:
    c01 = f.read()

# Verificações de segurança
assert "### Questão 01" in c01
assert "### Questão 02" in c01
assert "### Questão 03" in c01
assert "### Questão 04" in c01
assert "### Questão 05" in c01

q06_01 = """### Questão 06 (FCC - Analista Judiciário - Área Judiciária)
Acerca do conceito e dos sentidos de Administração Pública no ordenamento jurídico brasileiro, considere a situação em que determinado doutrinador analisa os órgãos, os agentes e as pessoas jurídicas incumbidos de desempenhar a atividade estatal, contrapondo-os à própria atividade concreta, contínua e direta voltada ao atendimento das necessidades coletivas.

Sob a perspectiva técnico-doutrinária consagrada pelo Direito Administrativo e pela jurisprudência:

* **A)** Em sentido objetivo, material ou funcional, a Administração Pública compreende o conjunto de órgãos, agentes e pessoas jurídicas instituídos pelo Estado para a execução de suas finalidades.
* **B)** Em sentido subjetivo, formal ou orgânico, a Administração Pública designa a própria função administrativa do Estado, abrangendo os serviços públicos, o poder de polícia, o fomento e a intervenção.
* **C)** No Brasil, adotou-se prioritariamente o critério formal, de modo que somente integram a Administração Pública, em sentido estrito e subjetivo, as entidades e órgãos reconhecidos como tais pela ordem jurídica, independentemente da atividade desempenhada.
* **D)** A atividade política de comando superior e fixação de diretrizes governamentais (função política ou de governo) confunde-se integralmente com a função administrativa em sentido material.
* **E)** As concessionárias e permissionárias de serviços públicos, por prestarem serviços essenciais à coletividade, passam a integrar a Administração Pública em sentido subjetivo ou orgânico.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O conceito descrito (órgãos, agentes e pessoas jurídicas) corresponde à Administração Pública em sentido **subjetivo, formal ou orgânico**, e não em sentido objetivo/material.
> - **B)** Incorreta. O enunciado inverteu os conceitos: a função administrativa, compreendendo as atividades de polícia, serviço público, fomento e intervenção, consubstancia a Administração Pública em sentido **objetivo, material ou funcional**.
> - **C)** Correta. O ordenamento jurídico pátrio consagrou o critério formal (subjetivo/orgânico): apenas integram formalmente a Administração Pública os entes e órgãos que a legislação expressamente qualifica como tais (Administração Direta e Indireta, art. 37 da CF/88 e Decreto-Lei nº 200/1967).
> - **D)** Incorreta. A doutrina clássica distingue nitidamente a função de governo/política (elaboração de diretrizes políticas amplas, atos com discricionariedade ampla e base constitucional direta) da função administrativa (execução subordinada e técnica das leis e políticas públicas).
> - **E)** Incorreta. Concessionárias e permissionárias são particulares em colaboração com o Poder Público; exercem função administrativa delegada (sentido material), mas **jamais integram** a Administração Pública em sentido subjetivo/orgânico.
>
> **Gabarito: C**"""

q07_01 = """### Questão 07 (FGV - Auditor Fiscal da Receita Estadual)
O regime jurídico-administrativo fundamenta-se em uma bipolaridade basilar caracterizada pela coexistência de prerrogativas estatais e restrições impostas à atuação do Poder Público. A respeito dessa estrutura dogmática, assinale a afirmativa correta.

* **A)** A supremacia do interesse público sobre o privado é irrestrita, autorizando a Administração a sobrepor suas decisões à ordem constitucional em situações de conveniência política.
* **B)** O princípio da indisponibilidade do interesse público impõe que os bens e interesses coletivos pertençam à sociedade, atuando o administrador público como mero gestor fiduciário, carecedor de titularidade para deles dispor livremente.
* **C)** O interesse público secundário, consubstanciado nos interesses patrimoniais e fiscais imediatos do erário estatal, prevalece juridicamente sobre os direitos e garantias fundamentais dos cidadãos.
* **D)** As sujeições administrativas constituem privilégios concedidos aos órgãos estatais para sobrepujar a esfera de liberdade dos administrados sem necessidade de processo prévio.
* **E)** O princípio da indisponibilidade do interesse público inviabiliza que o Poder Público celebre transações, acordos judiciais ou termos de ajustamento de conduta, haja vista a vedação absoluta à autocomposição pelo Estado.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A supremacia do interesse público não é absoluta nem ilimitada; submete-se estritamente aos direitos fundamentais, à legalidade e aos princípios da proporcionalidade e razoabilidade.
> - **B)** Correta. Pelo princípio da indisponibilidade do interesse público, o administrador não é senhor nem proprietário dos interesses e bens coletivos, mas simples guardião e gestor fiduciário, cabendo-lhe atuar unicamente nos estritos limites traçados pela lei em prol da coletividade.
> - **C)** Incorreta. O interesse público primário (o bem comum coletivo) é o único dotado de supremacia jurídica. O interesse público secundário (o interesse patrimonial da Fazenda Pública como pessoa jurídica) só é legítimo quando coincide com o interesse primário ou com a ordem constitucional.
> - **D)** Incorreta. As sujeições administrativas representam limites, freios e restrições impostos à Administração (como o dever de licitar, realizar concurso público e motivar atos), e não prerrogativas ou privilégios de poder.
> - **E)** Incorreta. A indisponibilidade não impede a autocomposição ou celebração de acordos (como TACs ou mediações públicas), desde que tais medidas visem à melhor realização do interesse coletivo, conforme expressamente autorizado pelo art. 3º do CPC/2015 e pela LINDB (art. 26).
>
> **Gabarito: B**"""

q08_01 = """### Questão 08 (FCC - Analista Judiciário - Área Administrativa)
No âmbito do Direito Público brasileiro, o princípio da legalidade apresenta conformação substancialmente distinta daquela aplicável às relações jurídicas privadas. A esse propósito, assinale a afirmativa que expressa com exatidão a disciplina jurídica desse princípio.

* **A)** No âmbito privado vigora a autonomia da vontade (art. 5º, II, CF/88), sendo lícito fazer tudo o que a lei não proíbe; já para a Administração Pública impera o princípio da estrita legalidade, cabendo-lhe agir tão somente quando houver prévia e expressa autorização legal.
* **B)** A Administração Pública pode praticar atos inominados e criar obrigações para os cidadãos com base exclusiva em portarias e instruções normativas, independentemente de lei em sentido formal.
* **C)** O princípio da juridicidade restringe a atuação do administrador público à estrita literalidade da lei ordinária, excluindo o bloco de constitucionalidade e os princípios implícitos.
* **D)** Em matérias afetas à discricionariedade administrativa, o administrador público fica dispensado de observar a lei, prevalecendo seu juízo exclusivo de oportunidade e conveniência sem qualquer balizamento normativo.
* **E)** O princípio da legalidade administrativa impede terminantemente a edição de qualquer decreto regulamentar que disponha sobre o detalhamento da execução da lei.

> **Comentário Detalhado:**
>
> - **A)** Correta. Enquanto o particular goza do postulado da autonomia privada (não ser obrigado a fazer ou deixar de fazer algo senão em virtude de lei), a Administração Pública sujeita-se à vinculação positiva à lei (legalidade estrita), só podendo atuar onde, como e quando a norma legal autorizar ou determinar.
> - **B)** Incorreta. Atos infralegais (portarias, instruções, resoluções) não podem inovar na ordem jurídica originária nem criar obrigações sem fundamento direto em lei formal (art. 5º, II, e art. 84, IV, CF/88).
> - **C)** Incorreta. O princípio da juridicidade amplia a submissão administrativa para além da lei formal, abrangendo todo o ordenamento jurídico (a Constituição, os tratados internacionais, os princípios gerais de direito e os precedentes vinculantes).
> - **D)** Incorreta. A discricionariedade nunca autoriza agir fora ou contra a lei. O juízo de oportunidade e conveniência ocorre estritamente dentro da moldura conferida pelo legislador, subordinando-se à finalidade pública, razoabilidade e proporcionalidade.
> - **E)** Incorreta. O decreto regulamentar executivo (art. 84, IV, CF/88) é o instrumento clássico pelo qual o Chefe do Executivo detalha e viabiliza a fiel execução das leis, desde que não exorbite seus termos.
>
> **Gabarito: A**"""

q09_01 = """### Questão 09 (FGV - Analista de Controle Externo / TCE)
Introduzido formalmente no caput do art. 37 da Constituição Federal pela Emenda Constitucional nº 19/1998, o princípio da eficiência impõe uma administração pública gerencial voltada a resultados. Sobre os desdobramentos normativos e práticos desse princípio, assinale a afirmativa correta.

* **A)** A busca pela eficiência econômica sobrepõe-se ao princípio da legalidade, permitindo ao gestor afastar regras procedimentais licitatórias sempre que verificar uma compra direta mais célere.
* **B)** O princípio da eficiência possui aplicação restrita à esfera de produtividade interna dos servidores, não gerando direitos subjetivos aos administrados quanto à qualidade dos serviços públicos prestados.
* **C)** Como corolário do princípio da eficiência, a CF/88 autorizou a perda de cargo do servidor público estável mediante procedimento de avaliação periódica de desempenho, na forma de lei complementar, assegurada ampla defesa.
* **D)** O princípio da eficiência impede a terceirização de atividades-meio na Administração Pública, por impor que todo e qualquer serviço estatal seja prestado diretamente por servidores concursados.
* **E)** A eficiência afasta o dever de motivação dos atos administrativos discricionários para conferir maior celeridade e desburocratização ao processo de tomada de decisão.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O princípio da eficiência jamais opera contra legem. A economicidade e a celeridade não autorizam o rompimento das regras constitucionais e legais que disciplinam a contratação pública.
> - **B)** Incorreta. A eficiência tem duas vertentes essenciais: a interna (atuação econômica e organizada do aparelho estatal) e a externa (prestação de serviços públicos céleres, adequados e de qualidade aos cidadãos administrados).
> - **C)** Correta. Nos termos do art. 41, § 1º, III, da CF/88 (incluído pela EC nº 19/1998), a avaliação periódica de desempenho constitui hipótese constitucional autônoma de perda do cargo do servidor estável, condicionada à edição de lei complementar e à garantia do contraditório e da ampla defesa.
> - **D)** Incorreta. O STF já fixou a tese de repercussão geral (Tema 725) no sentido de que é lícita a terceirização em todas as etapas da cadeia produtiva, inclusive em atividades-meio da Administração Pública, como instrumento de modernização gerencial.
> - **E)** Incorreta. A motivação é indispensável para verificar se o ato foi praticado com eficiência, finalidade pública e proporcionalidade; dispensar a motivação favoreceria o arbítrio e inviabilizaria o controle.
>
> **Gabarito: C**"""

q10_01 = """### Questão 10 (FCC - Procurador do Estado)
Determinada autoridade administrativa removeu ex officio um servidor público estável para localidade distante, fazendo constar formalmente na portaria que a medida visava atender a urgente déficit de pessoal e reestruturação do setor destinatário. Posteriormente, restou documentalmente comprovado em processo administrativo que o setor de destino possuía excedente de servidores e que a verdadeira intenção da chefia fora aplicar uma punição disfarçada em virtude de desavenças partidárias.

Diante da Teoria dos Motivos Determinantes, o ato de remoção descrito é:

* **A)** Válido, pois a remoção ex officio insere-se no poder discricionário da Administração, sendo irrelevante a veracidade dos motivos declarados pela autoridade.
* **B)** Nulo de pleno direito, uma vez que a validade do ato fica vinculada à veracidade e subsistência dos motivos explicitados pela autoridade, configurando a falsidade do motivo e o desvio de finalidade vício insanável.
* **C)** Convalidável, bastando que a autoridade edite novo ato retificador suprimindo a motivação pretérita e afirmando a discricionariedade pura.
* **D)** Válido quanto aos seus efeitos pretéritos e revogável unicamente com efeitos ex nunc por motivo de conveniência e oportunidade da chefia.
* **E)** Nulo apenas se comprovado prejuízo financeiro direto ao erário público, haja vista que a motivação constitui mero requisito acidental do ato administrativo.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Pela Teoria dos Motivos Determinantes, quando a autoridade explicita os motivos de fato e de direito para a prática do ato (mesmo em ato discricionário em que a motivação fosse dispensada em tese), o ato vincula-se indelevelmente a esses motivos. Se os fatos forem falsos ou inexistentes, o ato é nulo.
> - **B)** Correta. A Teoria dos Motivos Determinantes vincula o ato administrativo à veracidade dos motivos invocados. Comprovada a falsidade do déficit de pessoal e o desvio de finalidade (utilização de remoção como sanção disciplinar disfarçada), o ato padece de vício de nulidade insanável e afronta a moralidade e a impessoalidade.
> - **C)** Incorreta. Vícios no motivo e na finalidade são insanáveis e não admitem convalidação retroativa nem substituição extemporânea de motivos.
> - **D)** Incorreta. Trata-se de nulidade (vício de legalidade), ensejando declaração de invalidade (anulação) com efeitos retroativos (ex tunc), e não revogação discricionária ex nunc.
> - **E)** Incorreta. A motivação e o motivo são elementos de validade essenciais; a nulidade por falsidade do motivo independe de demonstração de dano patrimonial financeiro imediato ao erário.
>
> **Gabarito: B**"""

q11_01 = """### Questão 11 (FGV - Auditor de Controle Externo / TCE)
A Lei de Introdução às Normas do Direito Brasileiro (LINDB), com a redação conferida pela Lei nº 13.655/2018, estabeleceu novas diretrizes para as esferas administrativa, controladora e judicial. A respeito do regramento previsto nos arts. 20 e 21 da LINDB, assinale a afirmativa correta.

* **A)** Nas esferas administrativa, controladora e judicial, não se decidirá com base em valores jurídicos abstratos sem que sejam consideradas as consequências práticas da decisão.
* **B)** A exigência de motivação fundada em consequências práticas aplica-se unicamente ao Poder Judiciário, não vinculando as Cortes de Contas no exercício de suas auditorias.
* **C)** A invalidação de ato ou contrato administrativo prescinde de indicação expressa sobre suas consequências jurídicas e administrativas, privilegiando a aplicação automática da legalidade estrita.
* **D)** Ao decidir sobre a regularidade de conduta de gestor público, o órgão julgador deve desconsiderar os obstáculos e dificuldades reais, exigindo padrão de conduta ideal e irrealizável.
* **E)** As decisões controladoras que invalidarem atos administrativos não podem estabelecer qualquer regime de transição para cumprimento da nova orientação.

> **Comentário Detalhado:**
>
> - **A)** Correta. O art. 20, caput, da LINDB estatui textualmente que nas esferas administrativa, controladora e judicial não se decidirá com base em valores jurídicos abstratos sem que sejam consideradas as consequências práticas da decisão, exigindo ainda que a motivação demonstre a necessidade e a adequação da medida (parágrafo único).
> - **B)** Incorreta. O art. 20 é explícito ao determinar sua aplicação nas "esferas administrativa, controladora e judicial", vinculando diretamente a atuação e as decisões dos Tribunais de Contas.
> - **C)** Incorreta. O art. 21 da LINDB determina que a decisão que decretar a invalidação de ato, contrato, ajuste, processo ou norma administrativa deverá indicar, de modo expresso, as suas consequências jurídicas e administrativas.
> - **D)** Incorreta. O art. 22 da LINDB impõe expressamente que, na interpretação de normas sobre gestão pública, serão considerados os obstáculos e as dificuldades reais do gestor e as exigências das políticas públicas a seu cargo.
> - **E)** Incorreta. O parágrafo único do art. 21 da LINDB prevê a fixação de regime de transição sempre que necessário para que a nova obrigação seja cumprida de modo proporcional e equânime e sem prejuízo aos interesses gerais.
>
> **Gabarito: A**"""

# Inserção no arquivo 01
# Vamos mapear as posições exatas
# Questão 06: após "### 1.2 Sentido Objetivo, Material ou Funcional"
# Questão 07: após "### 2.2 Princípio da Indisponibilidade do Interesse Público"
# Questão 08: após "### 3.1 Princípio da Legalidade Estrita"
# Questão 09: após "### 3.5 Princípio da Eficiência (Emenda Constitucional nº 19/1998)"
# Questão 10: após "### 4.4 Princípio da Motivação e a Teoria dos Motivos Determinantes"
# Questão 11: após "### 5.1 Consequencialismo Jurídico e Vedação de Valores Abstratos (Art. 20)"

print("Arquivo 01 preparado para injeção.")
