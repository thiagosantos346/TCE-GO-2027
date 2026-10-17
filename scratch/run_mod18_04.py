# -*- coding: utf-8 -*-
import os
import re

BASE_DIR = "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/18_nocoes_de_controle_externo"
f04_path = f"{BASE_DIR}/04_relatorios_processo_de_controle_externo_e_sancoes.md"
with open(f04_path, "r", encoding="utf-8") as f:
    t04 = f.read()

assert "### Questão 01" in t04
assert "### Questão 02" in t04
assert "### Questão 03" in t04
assert "### Questão 04" in t04
assert "### Questão 05" in t04

q06_04 = """### Questão 06 (FCC - Analista de Controle Externo / TCE-GO)
A respeito da comunicação dos resultados das fiscalizações e dos instrumentos deliberativos do Tribunal de Contas, assinale a afirmativa correta.

* **A)** O acórdão constitui deliberação monocrática tomada exclusivamente pelo Conselheiro-Presidente em matéria administrativa interna.
* **B)** O acórdão é a deliberação colegiada do Tribunal de Contas (tomada pelo Plenário ou pelas Câmaras), formalizada por escrito e publicada no Diário Oficial de Contas, que decide o mérito de processos submetidos a julgamento ou apreciação da Corte.
* **C)** As decisões monocráticas dos Conselheiros-Relatores são irrecorríveis e imunes a qualquer insurgência recursal pelo gestor público.
* **D)** O relatório de auditoria elaborado pela equipe técnica tem força executiva imediata de título extrajudicial antes de qualquer manifestação do colegiado do Tribunal.
* **E)** O Ministério Público de Contas tem a prerrogativa de emitir sentenças vinculantes que anulam os acórdãos do Pleno do Tribunal de Contas.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Acórdão é ato **colegiado**, resultante da deliberação de órgãos fracionários (Câmaras) ou do Plenário da Corte.
> - **B)** Correta. O **acórdão** consubstancia a deliberação colegiada formal do Tribunal de Contas (Pleno ou Câmaras), contendo relatório, fundamentação/voto do Relator e dispositivo decisório, com publicação oficial para produzir efeitos erga omnes ou inter partes.
> - **C)** Incorreta. As decisões monocráticas do Relator admitem recurso de **agravo** para o órgão colegiado respectivo no prazo regimental.
> - **D)** Incorreta. O relatório técnico é peça instrutória e opinativa; apenas a decisão final colegiada do Tribunal com imputação de débito ou multa tem eficácia de título executivo (art. 71, § 3º, CF).
> - **E)** Incorreta. O Ministério Público de Contas atua como fiscal da ordem jurídica (custos legis), emitindo pareceres, sem exercer função judicante do Plenário.
>
> **Gabarito: B**"""

q07_04 = """### Questão 07 (FGV - Auditor de Controle Externo / TCE-SC)
A Tomada de Contas Especial (TCE) é um processo administrativo de controle de rito próprio instaurado para apurar responsabilidade por dano causado ao erário.

Sobre os pressupostos de instauração e o desenvolvimento da Tomada de Contas Especial, assinale a afirmativa correta.

* **A)** A Tomada de Contas Especial deve ser instaurada de forma compulsória e imediata pela autoridade administrativa competente diante da omissão no dever de prestar contas, de desfalque, desvio de bens ou de prática de qualquer ato ilegal, ilegítimo ou antieconômico de que resulte dano ao erário, após o esgotamento das medidas administrativas internas de cobrança.
* **B)** A TCE pode ser instaurada para apurar danos ao erário de valor insignificante, independentemente do custo de tramitação do processo de cobrança.
* **C)** A autoridade administrativa do órgão lesado fica dispensada de instaurar a TCE se o dano tiver sido praticado por servidor efetivo com mais de vinte anos de serviço.
* **D)** A instauração da Tomada de Contas Especial é prerrogativa exclusiva e originária do Poder Judiciário.
* **E)** A Tomada de Contas Especial não admite a condenação solidária de pessoas jurídicas de direito privado contratadas pelo órgão público.

> **Comentário Detalhado:**
>
> - **A)** Correta. O art. 71, II, da CF/88 c/c leis orgânicas dos Tribunais de Contas (art. 8º da Lei nº 8.443/1992 e LOTCE-GO) dispõe que, diante da omissão no dever de prestar contas, da não comprovação da aplicação dos recursos, de desfalque ou de qualquer ato ilegal de que resulte dano ao erário, a autoridade administrativa competente, **sob pena de responsabilidade solidária**, deverá adotar providências para a instauração da **Tomada de Contas Especial (TCE)** para apurar os fatos, identificar os responsáveis e quantificar o dano, após esgotadas as medidas internas.
> - **B)** Incorreta. Em homenagem ao princípio da economicidade processual, os Tribunais de Contas fixam valor de alçada (teto mínimo de dano); abaixo desse valor, adota-se cobrança administrativa sem deflagração de onerosa TCE.
> - **C)** Incorreta. O dever de prestar contas e apurar o dano atinge qualquer agente público, independentemente do tempo de carreira.
> - **D)** Incorreta. A TCE é processo administrativo instaurado pelo próprio órgão lesado (fase interna) e julgado pelo Tribunal de Contas (fase externa).
> - **E)** Incorreta. O particular e a pessoa jurídica privada que concorrerem para o dano respondem solidariamente com o agente público perante o TC (art. 71, II, CF).
>
> **Gabarito: A**"""

q08_04 = """### Questão 08 (FCC - Procurador do Estado / Adaptada)
Determinada autoridade administrativa, regularmente citada por edital em processo de tomada de contas especial perante o Tribunal de Contas em virtude de superfaturamento em pagamentos de obras, permaneceu inerte e não apresentou alegações de defesa nem recolheu o valor do débito no prazo fixado.

Diante do não comparecimento do responsável ao processo de controle externo, assinale a opção que expressa a consequência jurídica e a atuação correta do Tribunal de Contas.

* **A)** A revelia do responsável induz a presunção absoluta de veracidade de todas as imputações técnicas, ficando o Tribunal dispensado de examinar as provas materiais dos autos.
* **B)** O Tribunal de Contas deve declarar a revelia do responsável e dar prosseguimento ao processo, não operando a revelia a presunção automática de veracidade dos fatos, devendo a Corte de Contas pautar seu julgamento pelo princípio da verdade material com base nas provas efetivamente constantes nos autos.
* **C)** A decretação de revelia acarreta a prisão administrativa imediata do responsável pelo prazo de sessenta dias.
* **D)** O Tribunal deve extinguir o processo sem julgamento de mérito ante a ausência de manifestação voluntária da parte.
* **E)** A revelia impede que o responsável intervenha posteriormente nos autos ou constitua advogado antes do trânsito em julgado.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Ao contrário do processo civil comum onde a revelia pode gerar presunção relativa de veracidade fática dos fatos alegados pelo autor, no processo de controle externo vigora o postulado da **verdade material**: o Tribunal só condena se as provas documentais dos autos demonstrarem cabalmente o ilícito e o dano.
> - **B)** Correta. Regra processual pacífica nos Tribunais de Contas: o responsável que não atender à citação válida será considerado revel, dando-se prosseguimento ao feito. Todavia, a revelia não implica confissão ficta automática; a condenação exige lastro probatório fático idôneo apurado sob o princípio da **verdade material**. O responsável revel pode intervir no processo na fase em que ele se encontrar.
> - **C)** Incorreta. A prisão por dívida ou administrativa é vedada pela Constituição e pela Convenção Americana sobre Direitos Humanos (Súmula Vinculante 25/STF).
> - **D)** Incorreta. O processo prossegue à revelia até o julgamento de mérito com imputação de débito e multa.
> - **E)** Incorreta. O revel pode intervir em qualquer fase processual ulterior, recebendo o processo no estado em que se encontra.
>
> **Gabarito: B**"""

q09_04 = """### Questão 09 (FGV - Analista de Controle Externo / TCE-GO)
No julgamento das contas dos administradores públicos realizado pelo Tribunal de Contas, as contas podem ser julgadas regulares, regulares com ressalva ou irregulares (art. 71, II, CF/88 c/c LOTCE).

A respeito das consequências jurídicas do julgamento das contas, assinale a afirmativa correta.

* **A)** Quando julgar as contas regulares, o Tribunal dará quitação plena ao responsável, extinguindo sua responsabilidade sobre os atos de gestão examinados.
* **B)** O julgamento pela regularidade com ressalva acarreta a inabilitação temporária do gestor para o exercício de cargos em comissão pelo prazo de oito anos.
* **C)** As contas serão julgadas regulares com ressalva quando for comprovado desfalque financeiro ou dano irremediável ao patrimônio público.
* **D)** As contas julgadas irregulares que não envolvam dano ao erário dispensam a aplicação de qualquer sanção pecuniária pelo Tribunal.
* **E)** O acórdão que julga as contas regulares pode ser revisto ex officio a qualquer tempo pelo Presidente do Tribunal sem prazo decadencial.

> **Comentário Detalhado:**
>
> - **A)** Correta. Conforme previsto expressamente na Lei Orgânica do Tribunal de Contas, quando as contas forem julgadas **regulares** (expressando de forma clara e exata a exatidão dos demonstrativos e a legalidade dos atos de gestão), o Tribunal dará **quitação plena** ao responsável.
> - **B)** Incorreta. A regularidade com ressalva ocorre diante de impropriedades de natureza formal ou falhas sanáveis que não resultem em dano ao erário; o Tribunal emite quitação ao responsável e expede recomendações ou determinações corretivas, sem inabilitação.
> - **C)** Incorreta. Desfalque e dano impõem obrigatoriamente o julgamento pela **irregularidade das contas**, com condenação em débito e multa.
> - **D)** Incorreta. O art. 71, VIII, autoriza a aplicação de multa ao gestor por ato praticado com grave infração à norma legal ou regulamentar, mesmo sem dano patrimonial ao erário.
> - **E)** Incorreta. A revisão de ofício submete-se ao contraditório, aos prazos regimentais e à segurança jurídica.
>
> **Gabarito: A**"""

q10_04 = """### Questão 10 (FCC - Técnico de Controle Externo / TCE-GO)
Sobre o sistema recursal no processo de controle externo perante o Tribunal de Contas, assinale a afirmativa correta.

* **A)** O recurso de revisão possui efeito suspensivo automático sobre a execução do acórdão condenatório de débito emitido pelo Tribunal.
* **B)** Das deliberações proferidas pelo Tribunal de Contas em processos de prestação ou tomada de contas cabem embargos de declaração (para sanar obscuridade, omissão ou contradição) e recurso de reconsideração (dotado de efeito suspensivo ordinário).
* **C)** Os embargos de declaração no processo do Tribunal de Contas têm prazo de quinze dias úteis para interposição.
* **D)** O recurso de revisão pode ser interposto a qualquer tempo, mesmo após vinte anos do trânsito em julgado administrativo, sem necessidade de documento novo.
* **E)** É proibida a interposição de recursos administrativos por terceiros juridicamente interessados que comprovem prejuízo direto decorrente da decisão da Corte.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O recurso de revisão (ação rescisória no âmbito das Cortes de Contas) tem efeito **meramente devolutivo**, não suspendendo a eficácia da decisão condenatória nem impedindo a execução fiscal da dívida.
> - **B)** Correta. Disciplina processual consolidada das Cortes de Contas (Lei nº 8.443/1992 e Regimento Interno do TCE-GO): contra decisão definitiva de mérito em tomada ou prestação de contas cabe o **Recurso de Reconsideração** no prazo de 15 dias, dotado de efeito suspensivo e devolutivo; e cabem **Embargos de Declaração** para corrigir obscuridade, omissão ou contradição na deliberação colegiada.
> - **C)** Incorreta. O prazo dos embargos de declaração é de **5 (cinco) dias**, e não quinze.
> - **D)** Incorreta. O recurso de revisão sujeita-se a prazo decadencial estrito (normalmente 5 anos) e exige erro de cálculo, falsidade documental comprovada ou documento novo com eficácia sobre a prova.
> - **E)** Incorreta. Terceiros interessados e o Ministério Público de Contas detêm plena legitimidade recursal.
>
> **Gabarito: B**"""

q11_04 = """### Questão 11 (FGV - Auditor de Controle Externo / TCE-GO)
A Lei Complementar nº 64/1990 (Lei das Inelegibilidades, com as alterações da Lei da Ficha Limpa - LC nº 135/2010) estabelece que são inelegíveis os que tiverem suas contas relativas ao exercício de cargos ou funções públicas rejeitadas por irregularidade insanável que configure ato doloso de improbidade administrativa.

Sobre a atuação do Tribunal de Contas na aplicação da Lei da Ficha Limpa e o envio de listagens à Justiça Eleitoral, assinale a afirmativa correta.

* **A)** O Tribunal de Contas declara diretamente e de forma privativa a inelegibilidade dos gestores punidos, cassando seus direitos políticos com efeitos imediatos.
* **B)** Compete ao Tribunal de Contas encaminhar à Justiça Eleitoral a relação dos responsáveis que tiveram suas contas rejeitadas por irregularidade insanável e por decisão irrecorrível do órgão competente, cabendo exclusivamente à Justiça Eleitoral declarar a inelegibilidade do candidato no processo de registro de candidatura.
* **C)** A inclusão do nome do gestor na lista do Tribunal de Contas enseja a cassação automática de seu diploma de eleito pela mesa da assembleia legislativa.
* **D)** Contas rejeitadas por mera culpa ou impropriedade formal leve atraem compulsoriamente a inelegibilidade decenal da Lei da Ficha Limpa.
* **E)** A obtenção de liminar judicial suspendendo os efeitos do acórdão do Tribunal de Contas é irrelevante para a Justiça Eleitoral, que deve manter o indeferimento da candidatura.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O Tribunal de Contas **não declara inelegibilidade nem cassa direitos políticos**; sua competência é administrativa e de julgamento técnico de contas.
> - **B)** Correta. O art. 11, § 5º, da Lei nº 9.504/1997 c/c art. 1º, I, 'g', da LC nº 64/1990 estatui categoricamente: até 15 de agosto do ano eleitoral, os Tribunais de Contas enviarão à Justiça Eleitoral a **relação dos agentes que tiveram suas contas rejeitadas** por irregularidade insanável e por decisão irrecorrível nos últimos 8 anos. A competência para julgar e declarar a **inelegibilidade** do cidadão é privativa da **Justiça Eleitoral** no momento da impugnação ao registro de candidatura.
> - **C)** Incorreta. O envio da lista subsidia o julgamento jurisdicional eleitoral, não gerando perda sumária de mandato prévio.
> - **D)** Incorreta. A inelegibilidade da alínea 'g' exige cumulativamente: irregularidade insanável + ato doloso de improbidade administrativa + decisão irrecorrível do órgão competente. Falhas formais ou culposas não geram inelegibilidade.
> - **E)** Incorreta. Se houver provimento judicial (tutela provisória ou anulatória) suspendendo o acórdão do TC, a inelegibilidade fica suspensa perante a Justiça Eleitoral (art. 1º, § 2º da LC 64/90).
>
> **Gabarito: B**"""

# Inserções no arquivo 04 de trás para frente
pos_q05 = t04.find("### Questão 05")
assert pos_q05 != -1
pos_fontes = t04.find("## 🌐 Fontes", pos_q05)
assert pos_fontes != -1
t04 = t04[:pos_fontes] + "\n\n" + q11_04.strip() + "\n\n---\n\n" + t04[pos_fontes:]

pos_q04 = t04.find("### Questão 04")
assert pos_q04 != -1
pos_end_q04 = t04.find("\n\n---\n\n", pos_q04)
assert pos_end_q04 != -1
t04 = t04[:pos_end_q04 + 7] + "\n\n" + q10_04.strip() + "\n\n---\n\n" + t04[pos_end_q04 + 7:]

pos_q03 = t04.find("### Questão 03")
assert pos_q03 != -1
pos_end_q03 = t04.find("\n\n---\n\n", pos_q03)
assert pos_end_q03 != -1
t04 = t04[:pos_end_q03 + 7] + "\n\n" + q09_04.strip() + "\n\n---\n\n" + t04[pos_end_q03 + 7:]

pos_q02 = t04.find("### Questão 02")
assert pos_q02 != -1
pos_end_q02 = t04.find("\n\n---\n\n", pos_q02)
assert pos_end_q02 != -1
t04 = t04[:pos_end_q02 + 7] + "\n\n" + q08_04.strip() + "\n\n---\n\n" + t04[pos_end_q02 + 7:]

pos_q01 = t04.find("### Questão 01")
assert pos_q01 != -1
t04 = t04[:pos_q01] + "\n\n" + q07_04.strip() + "\n\n---\n\n" + t04[pos_q01:]

ancora_1 = "### 1. Comunicação dos Resultados e Deliberações do Tribunal"
pos_1 = t04.find(ancora_1)
pos_2 = t04.find("### 2. Tomada de Contas Especial", pos_1)
assert pos_1 != -1 and pos_2 != -1
t04 = t04[:pos_2] + "\n\n" + q06_04.strip() + "\n\n---\n\n" + t04[pos_2:]

qs_04 = re.findall(r"### Questão (\d+)", t04)
print("Questões no arquivo 04 do Módulo 18:", qs_04)
assert len(qs_04) == 11
assert sorted(qs_04) == ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']

with open(f04_path, "w", encoding="utf-8") as f:
    f.write(t04)

print("Arquivo 04 do Módulo 18 gravado com sucesso! Total: 11 questões.")
