import os, re

FILE = r"fontes_de_estudo/conhecimentos_gerais/03_legislacao_institucional/04_regime_juridico_servidores_e_pccr_leis_20756_e_15122.md"

q06_text = """
### Questão 06
**(FCC – Inédita – Padrão TCE-GO)**  
Nos termos do Estatuto dos Servidores Públicos Civis do Estado de Goiás (Lei Estadual nº 20.756/2020), a vacância do cargo público decorre taxativamente de:

* **A)** Promoção, readaptação, aposentadoria, exoneração, demissão, destituição de cargo em comissão, posse em outro cargo inacumulável e falecimento.
* **B)** Transferência, remoção compulsória, licença para tratar de interesses particulares e disponibilidade remunerada.
* **C)** Exoneração voluntária e demissão por justa causa apenas, permanecendo as demais hipóteses regidas pelo direito civil.
* **D)** Ascensão funcional, readmissão graciosa e aproveitamento em cargo comissionado.
* **E)** Licença-maternidade, afastamento para mandato classista e cessão de servidores entre órgãos.

> **Comentário Detalhado:**
>
> - **A)** Correta. O art. 44 da Lei Estadual nº 20.756/2020 prevê o rol taxativo das hipóteses de vacância de cargo público no Estado de Goiás: I - exoneração; II - demissão; III - destituição de cargo em comissão; IV - aposentadoria; V - posse em outro cargo inacumulável; VI - promoção; VII - readaptação; VIII - falecimento. Nota-se que tanto a promoção quanto a readaptação operam simultaneamente como forma de provimento (em um cargo) e forma de vacância (no cargo anterior).
> - **B)** Incorreta. Remoção e transferência interna não geram vacância de cargo, pois o servidor permanece ocupando o mesmo cargo efetivo, apenas alterando sua lotação ou unidade de exercício.
> - **C)** Incorreta. Há várias outras hipóteses legais além de exoneração e demissão (aposentadoria, promoção, posse em cargo inacumulável etc.).
> - **D)** Incorreta. Ascensão e transferência como formas de investidura foram banidas do ordenamento jurídico por inconstitucionalidade (Súmula Vinculante 43 do STF).
> - **E)** Incorreta. Licenças e afastamentos temporários mantêm o cargo provido pelo titular.
>
> **Gabarito: A**
"""

q07_text = """
### Questão 07
**(FCC – Inédita – Padrão TCE-GO)**  
A respeito das licenças, afastamentos e concessões funcionais reguladas pela Lei Estadual nº 20.756/2020 (Estatuto dos Servidores de Goiás):

* **A)** A antiga licença-prêmio por assiduidade foi expressamente extinta pelo novel estatuto goiano, sendo substituída pela licença para capacitação profissional pelo prazo de até 3 meses a cada quinquênio de efetivo exercício, sem prejuízo da remuneração.
* **B)** A licença por motivo de doença em pessoa da família é sempre concedida com remuneração integral, independentemente do prazo de duração do afastamento.
* **C)** É garantida a conversão em pecúnia de todos os períodos de licença-capacitação não usufruídos pelo servidor em atividade a qualquer tempo.
* **D)** O servidor em estágio probatório pode usufruir de licença para tratar de interesses particulares pelo prazo de até 3 anos consecutivos.
* **E)** O servidor afastado para exercício de mandato classista em sindicato perceberá gratificação extraordinária de função paga pelo erário estadual.

> **Comentário Detalhado:**
>
> - **A)** Correta. Uma das inovações mais relevantes da Lei Estadual nº 20.756/2020 (art. 138) foi a extinção da antiga licença-prêmio assiduidade (preservados os direitos adquiridos sob a égide da lei anterior) e a instituição da **Licença para Capacitação Profissional**, que faculta ao servidor afastar-se do cargo por até 3 meses, com remuneração integral, a cada período de 5 anos de efetivo exercício, desde que comprovada a participação em curso de aperfeiçoamento correlato às atribuições do cargo.
> - **B)** Incorreta. A licença por motivo de doença em pessoa da família (art. 130) é remunerada nos primeiros meses e torna-se sem remuneração caso ultrapasse os limites temporais previstos na lei.
> - **C)** Incorreta. A conversão em pecúnia da licença-capacitação é expressamente vedada durante a atividade funcional.
> - **D)** Incorreta. A licença para tratar de interesses particulares é privativa de servidores estáveis (após o término do estágio probatório).
> - **E)** Incorreta. O afastamento classista não gera direito a acréscimos pecuniários extraordinários custeados pelos cofres públicos.
>
> **Gabarito: A**
"""

q08_text = """
### Questão 08
**(FCC – Inédita – Padrão TCE-GO)**  
No âmbito do regime disciplinar instituído pela Lei Estadual nº 20.756/2020, as penalidades disciplinares aplicáveis aos servidores públicos estatutários de Goiás são:

* **A)** Advertência, censura ética, multa pecuniária descontada em folha e prisão administrativa.
* **B)** Advertência, suspensão de até 90 dias, demissão, cassação de aposentadoria ou disponibilidade e destituição de cargo em comissão.
* **C)** Repreensão verbal, suspensão por até 180 dias e perda compulsória dos direitos políticos.
* **D)** Advertência e demissão apenas, não se admitindo a penalidade de suspensão no serviço público estadual.
* **E)** Advertência, suspensão perpétua e banimento funcional.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A prisão administrativa é inconstitucional no direito brasileiro pós-CF/88, e censura ética é sanção deontológica de comissões de ética, não penalidade disciplinar estatutária direta.
> - **B)** Correta. O art. 196 da Lei Estadual nº 20.756/2020 enumera em rol taxativo as sanções disciplinares aplicáveis:  
>   I - advertência;  
>   II - suspensão (por prazo de até 90 dias);  
>   III - demissão;  
>   IV - cassação de aposentadoria ou disponibilidade;  
>   V - destituição de cargo em comissão ou função de confiança.
> - **C)** Incorreta. A suspensão é limitada a 90 dias, e perda de direitos políticos é sanção judicial privativa e não administrativa.
> - **D)** Incorreta. A suspensão é modalidade sancionatória expressamente positivada.
> - **E)** Incorreta. São vedadas penas perpétuas ou de banimento pela ordem constitucional.
>
> **Gabarito: B**
"""

q09_text = """
### Questão 09
**(FCC – Inédita – Padrão TCE-GO)**  
De acordo com o rito do Processo Administrativo Disciplinar (PAD) regulado pela Lei Estadual nº 20.756/2020:

* **A)** A comissão processante do PAD ordinário é composta por 3 servidores estáveis, designados pela autoridade instauradora, devendo o presidente ser ocupante de cargo efetivo superior ou de mesmo nível, ou ter escolaridade igual ou superior à do indiciado.
* **B)** A sindicância investigativa é fase obrigatória que precede necessariamente qualquer processo administrativo disciplinar, sob pena de nulidade absoluta.
* **C)** O indiciado não tem direito a constituir advogado para sua defesa técnica, sendo a autodefesa pessoal obrigatória e exclusiva.
* **D)** As testemunhas da comissão e da defesa devem depor conjuntamente na mesma sala de audiências para promover a imediata acareação.
* **E)** O relatório final da comissão processante vincula de forma absoluta o julgamento da autoridade competente, que não pode divergir de suas conclusões.

> **Comentário Detalhado:**
>
> - **A)** Correta. O art. 222 da Lei Estadual nº 20.756/2020 estabelece que o processo disciplinar será conduzido por comissão composta de **3 servidores estáveis**, exigindo-se que o presidente seja titular de cargo de escolaridade igual ou superior ou de nível hierárquico igual ou superior ao do servidor processado, garantindo imparcialidade e idoneidade formal.
> - **B)** Incorreta. Quando a autoria e a materialidade da infração disciplinar já estiverem previamente comprovadas por documentos ou relatórios de auditoria, o PAD pode ser instaurado diretamente, prescindindo de sindicância prévia.
> - **C)** Incorreta. A Súmula Vinculante 5 do STF preceitua que a falta de defesa técnica por advogado no PAD não ofende a Constituição, mas é evidente prerrogativa do servidor constituir advogado se assim desejar (faculdade assegurada pelo direito de ampla defesa).
> - **D)** Incorreta. As testemunhas são inquiridas separadamente e sucessivamente, para evitar que um depoimento contamine o outro.
> - **E)** Incorreta. A autoridade julgadora pode divergir motivadamente das conclusões do relatório da comissão quando este contrariar as provas dos autos.
>
> **Gabarito: A**
"""

q10_text = """
### Questão 10
**(FCC – Inédita – Padrão TCE-GO)**  
Em conformidade com a Lei Estadual nº 15.122/2005 (Plano de Cargos, Carreiras e Vencimentos dos Servidores do TCE-GO):

* **A)** O desenvolvimento na carreira opera-se exclusivamente por progressão funcional por tempo de serviço a cada 10 anos, inexistindo critério de merecimento ou avaliação de desempenho.
* **B)** A evolução funcional dos servidores do TCE-GO estrutura-se mediante **progressão horizontal** (passagem de um padrão para o subsequente dentro da mesma classe, por antiguidade e capacitação) e **promoção vertical** (passagem do último padrão de uma classe para o primeiro padrão da classe imediatamente superior, condicionada a interstício mínimo, avaliação de desempenho e qualificação técnica).
* **C)** Os cargos efetivos do TCE-GO admitem investidura derivada por reenquadramento automático de servidores terceirizados sem concurso público.
* **D)** O Adicional de Qualificação é parcela temporária concedida unicamente a servidores comissionados que não possuam vínculo efetivo com a Corte.
* **E)** As atribuições dos servidores de controle externo restringem-se ao atendimento ao público e arquivamento manual de certidões cartorárias.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O PCCR do TCE-GO adota sistemática moderna de desenvolvimento funcional baseada em avaliação periódica de desempenho, capacitação permanente e interstícios regulares.
> - **B)** Correta. Nos termos da Lei Estadual nº 15.122/2005, a carreira organiza-se em classes e padrões salariais sucessivos. A progressão (horizontal) consiste na movimentação entre padrões dentro da mesma classe, e a promoção (vertical) consiste na ascensão de classe funcional (por exemplo, da Classe A para a Classe B), exigindo o cumprimento de requisitos objetivos cumulativos de tempo (interstício), aproveitamento em cursos de pós-graduação/extensão e avaliação satisfatória no trabalho.
> - **C)** Incorreta. A exigência de concurso público específico de provas ou provas e títulos para provimento de cargos de provimento efetivo do Tribunal é mandamento constitucional inafastável (art. 37, II, da CF/88 e Súmula Vinculante 43).
> - **D)** Incorreta. O Adicional de Qualificação é vantagem funcional devida aos servidores do quadro efetivo portadores de títulos acadêmicos (especialização, mestrado, doutorado) correlatos às atividades de controle externo.
> - **E)** Incorreta. As atribuições legais dos cargos de controle externo compreendem o planejamento, a instrução e a execução de auditorias e fiscalizações de alta complexidade contábil, jurídica, orçamentária e financeira.
>
> **Gabarito: B**
"""

def enrich_mod3_file4():
    with open(FILE, "r", encoding="utf-8") as f:
        text = f.read()

    # Inserção da Questão 06: no fim da Seção 1.4 (antes de "### 1.5 Direitos, Vantagens Pecuniárias, Férias e Licenças")
    sec15 = "### 1.5 Direitos, Vantagens Pecuniárias, Férias e Licenças"
    idx15 = text.find(sec15)
    dash_idx = text.rfind("---", 0, idx15)
    text = text[:dash_idx] + q06_text + "\n---\n\n" + text[dash_idx:]

    # Inserção da Questão 07: no fim da Seção 1.5 (antes de "### 1.6 Regime Disciplinar: Deveres, Proibições e Penalidades")
    sec16 = "### 1.6 Regime Disciplinar: Deveres, Proibições e Penalidades"
    idx16 = text.find(sec16)
    dash_idx = text.rfind("---", 0, idx16)
    text = text[:dash_idx] + q07_text + "\n---\n\n" + text[dash_idx:]

    # Inserção da Questão 08: no fim da Seção 1.6 (antes de "### 1.7 Prescrição da Pretensão Punitiva Disciplinar")
    sec17 = "### 1.7 Prescrição da Pretensão Punitiva Disciplinar"
    idx17 = text.find(sec17)
    dash_idx = text.rfind("---", 0, idx17)
    text = text[:dash_idx] + q08_text + "\n---\n\n" + text[dash_idx:]

    # Inserção da Questão 09: no fim da Seção 1 (antes de "## 2. Plano de Cargos, Carreiras e Remuneração do TCE-GO")
    sec2 = "## 2. Plano de Cargos, Carreiras e Remuneração do TCE-GO (Lei nº 15.122/2005)"
    idx2 = text.find(sec2)
    dash_idx = text.rfind("---", 0, idx2)
    text = text[:dash_idx] + q09_text + "\n---\n\n" + text[dash_idx:]

    # Inserção da Questão 10: no fim da Seção 2 (antes de "## 3. Fontes Oficiais e Referências Bibliográficas")
    sec_fontes = "## 3. Fontes Oficiais e Referências Bibliográficas"
    idxf = text.find(sec_fontes)
    dash_idx = text.rfind("---", 0, idxf)
    text = text[:dash_idx] + q10_text + "\n---\n\n" + text[dash_idx:]

    with open(FILE, "w", encoding="utf-8") as f:
        f.write(text)

    print("Module 03 File 04 enriquecido com sucesso.")

enrich_mod3_file4()
