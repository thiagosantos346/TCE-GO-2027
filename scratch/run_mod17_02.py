# -*- coding: utf-8 -*-
import os
import re

BASE_DIR = "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/17_nocoes_de_direito_constitucional"
f02_path = f"{BASE_DIR}/02_direitos_e_garantias_fundamentais_e_politicos.md"
with open(f02_path, "r", encoding="utf-8") as f:
    t02 = f.read()

assert "### Questão 01" in t02
assert "### Questão 02" in t02
assert "### Questão 03" in t02
assert "### Questão 04" in t02
assert "### Questão 05" in t02

q06_02 = """### Questão 06 (FCC - Analista Judiciário - Área Judiciária)
A Constituição Federal de 1988 consagra, em seu art. 5º, XI, que 'a casa é asilo inviolável do indivíduo, ninguém nela podendo penetrar sem consentimento do morador, salvo em caso de flagrante delito ou desastre, ou para prestar socorro, ou, durante o dia, por determinação judicial'.

Sobre a interpretação dada a essa garantia fundamental pelo Supremo Tribunal Federal (Tema 280 de Repercussão Geral), assinale a afirmativa correta.

* **A)** A entrada forçada em domicílio sem mandado judicial é lícita em qualquer horário quando amparada em fundada suspeita, justificada a posteriori mediante a apreensão efetiva de entorpecentes no local.
* **B)** A entrada forçada em domicílio sem mandado judicial, mesmo em caso de crime permanente, só é lícita quando amparada em fundadas razões, devidamente justificadas pelas circunstâncias do caso concreto que indiquem a ocorrência de flagrante delito no interior da residência.
* **C)** O conceito constitucional de 'casa' abrange unicamente residências habitadas de forma definitiva por famílias, excluindo quartos de hotel ocupados e escritórios profissionais.
* **D)** A determinação judicial autoriza a invasão domiciliar por agentes policiais a qualquer hora da noite sem consentimento do morador.
* **E)** Fiscais tributários e auditores de controle externo podem ingressar em domicílio privado durante o dia com base em seu poder de polícia, independentemente de autorização judicial.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A ilicitude da invasão não é convalidada pelo encontro fortuito posterior de drogas. A justa causa deve existir e ser demonstrável **antes** do ingresso forçado.
> - **B)** Correta. Tese fixada pelo STF no **Tema 280 de Repercussão Geral** (RE 603.616): *"A entrada forçada em domicílio sem mandado judicial só é lícita, mesmo em período noturno, quando amparada em fundadas razões, devidamente justificadas a posteriori, que indiquem que dentro da casa ocorre situação de flagrante delito, sob pena de responsabilidade disciplinar, civil e penal do agente ou da autoridade e de nulidade dos atos praticados"*.
> - **C)** Incorreta. O conceito de casa no direito constitucional é amplo: abrange residência, quarto de hotel ocupado, trailers, consultórios e escritórios profissionais fechados ao público (art. 150, § 4º, do Código Penal).
> - **D)** Incorreta. O mandado judicial autoriza ingresso **estritamente durante o dia** (critério cronológico ou físico-astronômico do nascer ao pôr do sol).
> - **E)** Incorreta. Fiscais e auditores administrativos não possuem poder para ingressar contra a vontade do morador sem mandado judicial.
>
> **Gabarito: B**"""

q07_02 = """### Questão 07 (FGV - Auditor Fiscal da Receita Estadual)
O art. 5º, XII, da Constituição Federal estabelece que 'é inviolável o sigilo da correspondência e das comunicações telegráficas, de dados e das comunicações telefônicas, salvo, no último caso, por ordem judicial, nas hipóteses e na forma que a lei estabelecer para fins de investigação criminal ou instrução processual penal'.

À luz do texto constitucional e da jurisprudência do STF, assinale a afirmativa correta.

* **A)** A interceptação de comunicações telefônicas pode ser decretada pelo juiz competente em processo administrativo disciplinar ou em ação civil pública patrimonial.
* **B)** A interceptação telefônica depende de ordem judicial fundamentada e destina-se exclusivamente à investigação criminal ou instrução processual penal, não se admitindo em processos de natureza cível ou administrativa originária.
* **C)** O sigilo fiscal e bancário é absoluto, sendo vedado à Receita Federal e ao Tribunal de Contas ter acesso a dados financeiros mesmo nos termos da Lei Complementar nº 105/2001.
* **D)** A gravação clandestina realizada por um dos interlocutores sem o conhecimento do outro é considerada prova ilícita em qualquer circunstância.
* **E)** A interceptação telefônica pode ser autorizada sem prazo fixado, perdurando por tempo indeterminado a critério do delegado de polícia.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A Constituição é taxativa: interceptação telefônica somente é autorizada para fins de **investigação criminal ou instrução processual penal** (art. 5º, XII c/c Lei nº 9.296/1996). O que se admite, após produzida no processo penal, é o empréstimo da prova (prova emprestada) para o PAD.
> - **B)** Correta. A quebra do sigilo das comunicações telefônicas (interceptação da conversa em tempo real) submete-se à estrita reserva de jurisdição e restringe-se materialmente à seara criminal/penal.
> - **C)** Incorreta. O sigilo bancário não é absoluto; o STF (ADI 2.390 e RE 601.314/Tema 225) declarou a constitucionalidade do acesso direto da Receita Federal a dados bancários nos termos da LC nº 105/2001.
> - **D)** Incorreta. Conforme firme jurisprudência do STF (Tema 98 de Repercussão Geral), a gravação ambiental ou telefônica realizada por um dos interlocutores (gravação clandestina) é **lícita**, inclusive sem o conhecimento do outro, em legítima defesa de direitos.
> - **E)** Incorreta. O prazo legal é de 15 dias, prorrogável justificadamente (art. 5º da Lei nº 9.296/1996).
>
> **Gabarito: B**"""

q08_02 = """### Questão 08 (FCC - Procurador do Estado / Adaptada)
A respeito dos remédios constitucionais, compare a disciplina do Mandado de Injunção (art. 5º, LXXI, e Lei nº 13.300/2016) e do Habeas Data (art. 5º, LXXII, e Lei nº 9.507/1997).

Assinale a afirmativa correta.

* **A)** O mandado de injunção é a ação constitucional cabível para obter a retificação de dados pessoais em registros de entidades governamentais.
* **B)** O habeas data prescinde de prévia recusa da via administrativa, podendo ser impetrado diretamente em juízo mesmo sem consulta ao órgão detentor dos dados.
* **C)** Conceder-se-á mandado de injunção sempre que a falta de norma regulamentadora torne inviável o exercício dos direitos e liberdades constitucionais e das prerrogativas inerentes à nacionalidade, à soberania e à cidadania.
* **D)** A impetração de habeas data está sujeita ao pagamento prévio de custas processuais fixadas pelo regimento interno do tribunal.
* **E)** O mandado de injunção não admite a modalidade coletiva, sendo ação personalíssima e de titularidade estritamente individual.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A retificação de dados pessoais é objeto precípuo do **Habeas Data** (art. 5º, LXXII, 'b').
> - **B)** Incorreta. O STJ e o STF pacificaram (Súmula 2 do STJ): *"Não cabe o habeas data (HD) se não houve recusa de informações por parte da autoridade administrativa"*. Exige-se interesse de agir demonstrado pela recusa expressa ou mora administrativa injustificada.
> - **C)** Correta. O art. 5º, LXXI, da CF/88 estatui literalmente: *"conceder-se-á mandado de injunção sempre que a falta de norma regulamentadora torne inviável o exercício dos direitos e liberdades constitucionais e das prerrogativas inerentes à nacionalidade, à soberania e à cidadania"*.
> - **D)** Incorreta. O art. 5º, LXXIII, da CF/88 prevê a **gratuidade das ações de habeas corpus e habeas data**.
> - **E)** Incorreta. O mandado de injunção coletivo é expressamente disciplinado nos arts. 12 e 13 da Lei nº 13.300/2016.
>
> **Gabarito: C**"""

q09_02 = """### Questão 09 (FGV - Analista de Controle Externo / TCE-GO)
Os Direitos Sociais encontram-se insculpidos no art. 6º da Constituição da República de 1988, integrando o núcleo dos direitos fundamentais de segunda dimensão (prestações positivas do Estado).

Sobre a disciplina jurídica dos direitos sociais e a jurisprudência constitucional, assinale a afirmativa correta.

* **A)** O rol dos direitos sociais do art. 6º da CF/88 é taxativo, sendo vedada a inclusão de novos direitos por meio de emendas constitucionais.
* **B)** São direitos sociais previstos expressamente no art. 6º da CF/88 a educação, a saúde, a alimentação, o trabalho, a moradia, o transporte, o lazer, a segurança, a previdência social, a proteção à maternidade e à infância e a assistência aos desamparados.
* **C)** O princípio da reserva do possível autoriza o gestor público a descumprir o mínimo existencial de saúde e educação sem qualquer justificativa orçamentária ou técnica.
* **D)** O direito de greve dos servidores públicos civis (art. 37, VII) é autoaplicável e prescinde de qualquer integração legislativa ou analogia.
* **E)** Os direitos trabalhistas previstos no art. 7º da CF/88 não admitem qualquer flexibilização por negociação coletiva de trabalho.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O rol é exemplificativo e tem sido ampliado pelo constituinte derivado (foram incluídos moradia pela EC 26/00, alimentação pela EC 64/10 e transporte pela EC 90/15).
> - **B)** Correta. O art. 6º da CF/88 enumera: *"São direitos sociais a educação, a saúde, a alimentação, o trabalho, a moradia, o transporte, o lazer, a segurança, a previdência social, a proteção à maternidade e à infância, a assistência aos desamparados, na forma desta Constituição"*.
> - **C)** Incorreta. Conforme jurisprudência do STF (ADPF 45 e Tema 698/STF), a cláusula da reserva do possível não pode ser invocada de modo genérico para esvaziar o núcleo do mínimo existencial (como leitos hospitalares e medicamentos vitais).
> - **D)** Incorreta. O STF (MI 670, MI 708 e MI 712) determinou a aplicação analógica da lei de greve do setor privado (Lei nº 7.783/1989) aos servidores públicos civis ante a mora legislativa.
> - **E)** Incorreta. Diversos direitos trabalhistas admitem redução e compensação por convenção ou acordo coletivo (art. 7º, VI, XIII e XIV da CF/88 c/c Tema 1.046/STF).
>
> **Gabarito: B**"""

q10_02 = """### Questão 10 (FCC - Analista de Controle Externo / Adaptada)
A Emenda Constitucional nº 131/2023 alterou substancialmente a disciplina da perda da nacionalidade brasileira constante no art. 12, § 4º, da Constituição Federal.

De acordo com o texto constitucional vigente com a redação dada pela EC nº 131/2023, será declarada a perda da nacionalidade do brasileiro que:

* **A)** Adquirir outra nacionalidade por naturalização voluntária, perdendo automaticamente a nacionalidade brasileira no dia da concessão do passaporte estrangeiro.
* **B)** Tiver cancelada sua naturalização, por sentença judicial, em virtude de fraude relacionada ao processo de naturalização ou de atentado contra a ordem constitucional e o Estado Democrático; ou fizer pedido expresso de perda da nacionalidade brasileira perante autoridade brasileira competente, ressalvadas situações que acarretem apatridia.
* **C)** Residir no exterior por mais de cinco anos ininterruptos sem comparecer ao consulado brasileiro.
* **D)** Casar-se com cidadão estrangeiro em país que não reconheça a dupla cidadania.
* **E)** Aceitar emprego remunerado em empresa privada sediada em país estrangeiro sem autorização do Presidente da República.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A EC nº 131/2023 **revogou a perda automática** da nacionalidade brasileira pela aquisição voluntária de outra nacionalidade. Hoje o brasileiro pode ter dupla ou múltipla cidadania sem perder a brasileira.
> - **B)** Correta. O art. 12, § 4º, da CF/88 (redação da EC nº 131/2023) estabelece que será declarada a perda da nacionalidade do brasileiro que: I - tiver cancelada sua naturalização, por sentença judicial, em virtude de fraude relacionada ao processo de naturalização ou de atentado contra a ordem constitucional e o Estado Democrático; II - fizer **pedido expresso de perda da nacionalidade brasileira** perante autoridade brasileira competente, ressalvadas situações que acarretem apatridia (ninguém pode se tornar apátrida). Ademais, a renúncia não impede a readquisição posterior.
> - **C)** Incorreta. A residência no exterior não acarreta perda da nacionalidade.
> - **D)** Incorreta. O casamento com estrangeiro jamais gerou perda de nacionalidade brasileira.
> - **E)** Incorreta. Não existe restrição constitucional para trabalho de brasileiros em empresas privadas no exterior.
>
> **Gabarito: B**"""

q11_02 = """### Questão 11 (FGV - Analista Jurídico de Controle Externo / TCE-GO)
Sobre os direitos políticos e o regime de inelegibilidades positivado no art. 14 da Constituição Federal de 1988, assinale a afirmativa correta.

* **A)** O alistamento eleitoral e o voto são facultativos para os analfabetos, para os maiores de setenta anos e para os maiores de dezesseis e menores de dezoito anos.
* **B)** O estrangeiro e os conscritos, durante o período de serviço militar obrigatório, podem alistar-se livremente como eleitores desde que comprovem residência fixa.
* **C)** A idade mínima de trinta e cinco anos é condição constitucional de elegibilidade para os cargos de Governador e Vice-Governador de Estado e do Distrito Federal.
* **D)** São inelegíveis, no território de jurisdição do titular, o cônjuge e os parentes consanguíneos ou afins, até o terceiro grau, do Presidente da República, de Governador de Estado ou de Prefeito.
* **E)** O militar alistável é inelegível se contar com mais de dez anos de serviço na corporação.

> **Comentário Detalhado:**
>
> - **A)** Correta. O art. 14, § 1º, II, da CF/88 dispõe que o alistamento eleitoral e o voto são **facultativos**: 'a' - para os analfabetos; 'b' - para os maiores de setenta anos; 'c' - para os maiores de dezesseis e menores de dezoito anos. Para os maiores de 18 anos são obrigatórios.
> - **B)** Incorreta. O art. 14, § 2º, estabelece que os estrangeiros e, durante o período do serviço militar obrigatório, os conscritos **não podem alistar-se como eleitores** (são inalistáveis e, portanto, inelegíveis).
> - **C)** Incorreta. A idade mínima para Governador e Vice-Governador é de **30 (trinta) anos** (art. 14, § 3º, VI, 'b'); 35 anos aplica-se a Presidente, Vice-Presidente e Senador.
> - **D)** Incorreta. A inelegibilidade reflexa alcança parentes até o **segundo grau** (consanguíneos ou afins) ou por adoção (art. 14, § 7º da CF/88 e Súmula Vinculante 18), e não até o terceiro grau.
> - **E)** Incorreta. Se o militar tiver mais de 10 anos de serviço, será agregado pela autoridade e, se eleito, passará automaticamente, no ato da diplomação, para a inatividade (art. 14, § 8º, II).
>
> **Gabarito: A**"""

# Inserções no arquivo 02 de trás para frente
pos_q05 = t02.find("### Questão 05")
assert pos_q05 != -1
pos_fontes = t02.find("## 🌐 Fontes", pos_q05)
assert pos_fontes != -1
t02 = t02[:pos_fontes] + "\n\n" + q11_02.strip() + "\n\n---\n\n" + t02[pos_fontes:]

pos_q04 = t02.find("### Questão 04")
assert pos_q04 != -1
pos_end_q04 = t02.find("\n\n---\n\n", pos_q04)
assert pos_end_q04 != -1
t02 = t02[:pos_end_q04 + 7] + "\n\n" + q10_02.strip() + "\n\n---\n\n" + t02[pos_end_q04 + 7:]

ancora_3 = "### 3. Direitos Sociais (Arts. 6º a 11)"
pos_3 = t02.find(ancora_3)
pos_4 = t02.find("### 4. Teoria da Nacionalidade", pos_3)
assert pos_3 != -1 and pos_4 != -1
t02 = t02[:pos_4] + "\n\n" + q09_02.strip() + "\n\n---\n\n" + t02[pos_4:]

pos_q02 = t02.find("### Questão 02")
assert pos_q02 != -1
pos_end_q02 = t02.find("\n\n---\n\n", pos_q02)
assert pos_end_q02 != -1
t02 = t02[:pos_end_q02 + 7] + "\n\n" + q08_02.strip() + "\n\n---\n\n" + t02[pos_end_q02 + 7:]

pos_q01 = t02.find("### Questão 01")
assert pos_q01 != -1
pos_end_q01 = t02.find("\n\n---\n\n", pos_q01)
assert pos_end_q01 != -1
t02 = t02[:pos_end_q01 + 7] + "\n\n" + q07_02.strip() + "\n\n---\n\n" + t02[pos_end_q01 + 7:]
t02 = t02[:pos_q01] + "\n\n" + q06_02.strip() + "\n\n---\n\n" + t02[pos_q01:]

qs_02 = re.findall(r"### Questão (\d+)", t02)
print("Questões no arquivo 02 do Módulo 17:", qs_02)
assert len(qs_02) == 11
assert sorted(qs_02) == ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']

with open(f02_path, "w", encoding="utf-8") as f:
    f.write(t02)

print("Arquivo 02 do Módulo 17 gravado com sucesso! Total: 11 questões.")
