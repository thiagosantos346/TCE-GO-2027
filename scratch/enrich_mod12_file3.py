import os

file_path = "fontes_de_estudo/conhecimentos_especificos_b02_ti/12_governanca_de_ti/03_gestao_de_projetos_pmbok_8_edicao_e_metodos_ageis.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

q06 = """
---

### Questão 06 (FCC - Analista Judiciário - Tecnologia da Informação - Adaptada)
**Enunciado:** O Guia PMBOK estabelece distinções fundamentais entre as características de um projeto e as rotinas de uma operação contínua dentro de uma organização de TI. Acerca dessa comparação, assinale a alternativa correta:  

* **A)** Projetos são contínuos e repetitivos, visando unicamente manter os sistemas legados funcionando sem qualquer alteração de infraestrutura.
* **B)** As operações são caracterizadas pela temporariedade estrita, tendo data formal de início e término com dissolução imediata da equipe ao término de cada chamado.
* **C)** Um projeto é um esforço temporário empreendido para criar um produto, serviço ou resultado exclusivo, enquanto as operações sustentam a execução contínua do negócio.
* **D)** A elaboração progressiva é uma característica exclusiva das operações financeiras, sendo expressamente vedada na gestão de projetos de tecnologia da informação.
* **E)** Projetos de desenvolvimento de software prescindem de objetivos ou escopo delimitado, devendo prolongar-se indefinidamente pela vida útil da instituição.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Atividades contínuas e repetitivas de manutenção definem as Operações, não os projetos.
> - **B)** Incorreta. Quem possui marco temporal determinado de início e término é o Projeto. Operações são permanentes e contínuas.
> - **C)** **Correta.** Definição clássica e canônica do PMI: Projetos são iniciativas temporárias que geram entregas exclusivas (únicas); operações são contínuas e mantêm a organização funcionando.
> - **D)** Incorreta. A elaboração progressiva (desenvolver em etapas, com detalhes refinados à medida que o projeto avança) é característica marcante dos projetos.
> - **E)** Incorreta. Projetos têm objetivos específicos e encerram-se ao concluir suas entregas ou quando se tornam inviáveis.
> 
> **Gabarito: C**
"""

q07 = """
---

### Questão 07 (FGV - TRT - Analista Judiciário - Tecnologia da Informação - Adaptada)
**Enunciado:** Nas diretrizes contemporâneas do Guia PMBOK (7ª e 8ª edições), a gestão de projetos é articulada dentro de um 'Sistema de Entrega de Valor' (*System for Value Delivery*), superando o modelo puramente prescritivo de processos mecânicos. A respeito dos princípios e desse sistema de entrega de valor, assinale a alternativa correta:  

* **A)** O sistema de entrega de valor preconiza que o único objetivo do gestor de projetos é a geração burocrática de documentos e artefatos em papel, desconsiderando se o produto gerou valor ao negócio.
* **B)** O foco da gestão contemporânea de projetos desloca-se da mera entrega física de produtos (*deliverables*) para a realização efetiva de benefícios e resultados estratégicos (*outcomes and business value*).
* **C)** O PMBOK estabelece que a liderança em projetos deve ser autoritária e centralizadora, sendo proibida a adoção de posturas de liderança servidora em equipes ágeis.
* **D)** O sistema de entrega de valor é restrito a empresas privadas com fins lucrativos, sendo inaplicável a órgãos públicos ou tribunais de contas.
* **E)** O Guia PMBOK aboliu totalmente a gestão de riscos e a preocupação com a qualidade técnica das entregas de software.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O foco em entregáveis documentais burocráticos foi expressamente substituído pelo foco em valor e benefícios reais.
> - **B)** **Correta.** A evolução do PMBOK foca no Sistema de Entrega de Valor: o valor reside na capacidade do resultado final (*outcome*) resolver problemas reais e viabilizar os objetivos estratégicos da organização.
> - **C)** Incorreta. Os princípios do PMBOK enfatizam a liderança colaborativa, servidora e a capacitação contínua da equipe.
> - **D)** Incorreta. O sistema de entrega de valor aplica-se plenamente ao setor público, orientando a geração de valor público, eficiência de gastos e transparência social.
> - **E)** Incorreta. Riscos (Domínio da Incerteza) e Qualidade continuam sendo pilares centrais de avaliação de projetos.
> 
> **Gabarito: B**
"""

q08 = """
---

### Questão 08 (FCC - TRT-14 - Analista Judiciário - Tecnologia da Informação - Adaptada)
**Enunciado:** O Guia PMBOK enfatiza o princípio da Adaptação Contextual (*Tailoring*), reconhecendo que abordagens de desenvolvimento (preditivas, ágeis ou híbridas) devem ser moldadas às características exclusivas de cada projeto e organização. Acerca do *Tailoring* e dos ciclos de vida de projetos, assinale a alternativa correta:  

* **A)** Em abordagens puramente preditivas (em cascata), o escopo, prazo e custo são definidos em detalhes nas fases iniciais, visando minimizar alterações ao longo do ciclo.
* **B)** A adaptação (*tailoring*) prescreve que todo projeto governamental de TI deve obrigatoriamente aplicar 100% de todas as ferramentas e modelos do PMBOK sem qualquer supressão ou customização.
* **C)** Métodos ágeis recusam qualquer planejamento inicial, proibindo a definição de visões de produto ou marcos de release.
* **D)** Em projetos com alto grau de incerteza de requisitos e tecnologias inovadoras, a abordagem mais indicada é o ciclo preditivo rígido com proibição de entregas incrementais.
* **E)** O princípio do *tailoring* impede que organizações públicas combinem elementos de governança preditiva contratual com frameworks ágeis (como Scrum) de desenvolvimento.

> **Comentário Detalhado:**
>
> - **A)** **Correta.** No ciclo de vida preditivo (*waterfall*), a ênfase inicial está no planejamento abrangente antecipado do escopo, cronograma e custo, controlando rigidamente qualquer alteração posterior.
> - **B)** Incorreta. O próprio conceito de *tailoring* determina a seleção criteriosa e personalização dos processos, métodos e artefatos adequados ao contexto específico de cada projeto.
> - **C)** Incorreta. Métodos ágeis planejam continuamente em múltiplos horizontes (visão, roadmap, release, sprint e dia a dia).
> - **D)** Incorreta. Alta incerteza e inovação exigem ciclos adaptativos/ágeis com iterações curtas e entregas frequentes.
> - **E)** Incorreta. Abordagens híbridas (muito comuns no setor público, unindo governança contratual formal da Lei 14.133/2021 à execução ágil interna) são expressamente incentivadas pelo *tailoring*.
> 
> **Gabarito: A**
> """

q09 = """
---

### Questão 09 (FCC - Auditor de Controle Externo / TI - Adaptada)
**Enunciado:** A Análise de Valor Agregado (EVM) fundamenta-se em três grandezas quantitativas centrais para aferir a saúde econômico-temporal de um projeto: Valor Planejado (VP), Custo Real (CR) e Valor Agregado (VA). Sobre essas variáveis, assinale a alternativa correta:  

* **A)** O Valor Agregado (VA) corresponde ao montante de recursos financeiros transferido compulsoriamente aos acionistas da empresa contratada a título de dividendos.
* **B)** O Custo Real (CR) representa o orçamento estimado ideal que deveria ter sido gasto na hipótese teórica de produtividade máxima.
* **C)** O Valor Planejado (VP) representa o orçamento autorizado e alocado para o trabalho que estava programado para ser executado até a data da medição.
* **D)** O Valor Agregado (VA) é calculado somando-se as notas fiscais emitidas pelo fornecedor independentemente de o serviço ter sido homologado ou entregue.
* **E)** As métricas de EVM podem ser calculadas apenas após o encerramento formal do projeto, sendo vedado seu uso durante a fase de execução.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O Valor Agregado é a medida do trabalho fisicamente concluído expresso em termos do orçamento aprovado para esse trabalho.
> - **B)** Incorreta. O Custo Real (CR) é o total dos custos efetivamente incorridos e contabilizados na realização do trabalho executado até a data base.
> - **C)** **Correta.** Definição exata de Valor Planejado (VP / PV): parcela do orçamento aprovado que deveria ter sido consumida conforme o cronograma planejado até o momento da aferição.
> - **D)** Incorreta. O VA só contabiliza o trabalho realmente executado e aceito segundo as regras de medição aprovadas.
> - **E)** Incorreta. O propósito primordial da EVM é o monitoramento contínuo concomitante durante a execução para permitir ações corretivas tempestivas.
> 
> **Gabarito: C**
"""

q10 = """
---

### Questão 10 (FCC - Tribunal de Contas - Auditor de TI - Adaptada)
**Enunciado:** A Gestão de Portfólio de TI é o elo estratégico que alinha as decisões de investimento em tecnologia às prioridades institucionais de um Tribunal de Contas. A respeito das atribuições de governança e práticas de gestão de portfólio, assinale a afirmativa correta:  

* **A)** A gestão de portfólio visa garantir que a organização execute a combinação ideal de projetos e programas que maximize o valor institucional e respeite a capacidade orçamentária e operacional.
* **B)** O portfólio de TIC deve conter exclusivamente projetos de desenvolvimento de software em linguagem Java, sendo vedada a inclusão de projetos de aquisição de infraestrutura de nuvem.
* **C)** A priorização de projetos em um portfólio público deve basear-se exclusivamente na ordem cronológica de abertura de chamados no help desk, sem uso de modelos de pontuação estratégica.
* **D)** A governança de portfólio determina que, uma vez aprovado pelo Comitê Estratégico, um projeto jamais pode ser cancelado ou suspenso, ainda que perca sua viabilidade técnica ou legal.
* **E)** O gerenciamento de portfólio é atribuição privativa do estagiário de suporte técnico de primeiro nível, dispensando apreciação pelo Comitê de Governança de TI.

> **Comentário Detalhado:**
>
> - **A)** **Correta.** O objetivo primordial da Gestão de Portfólio é selecionar, priorizar, balancear e monitorar programas, projetos e iniciativas contínuas para assegurar o alinhamento com a estratégia corporativa e a otimização dos recursos disponíveis.
> - **B)** Incorreta. Portfólios de TIC integram iniciativas de diferentes naturezas: infraestrutura, segurança cibernética, sistemas analíticos, IA, modernização de redes, capacitação etc.
> - **C)** Incorreta. A seleção e priorização utilizam modelos formais de pontuação (*scoring models*) com base em alinhamento estratégico, valor público, riscos e retorno social.
> - **D)** Incorreta. A governança monitora continuamente o portfólio e tem o dever de cancelar, pausar ou replanejar projetos que deixem de demonstrar alinhamento ou viabilidade.
> - **E)** Incorreta. Gestão de portfólio é prática de governança estratégica ligada à alta administração e ao Comitê Estratégico de TI.
> 
> **Gabarito: A**
"""

# Insertions:
# 1. After Section 1.1 item 3 (line ~53)
p1 = "    - *Operações:* Sustentam o negócio existente, repetem processos padronizados contínuos (atendimento de chamados, manutenção de infraestrutura, rotinas de backup) e não têm data prevista para término.\n"
assert p1 in content, "Pattern 1 not found"
content = content.replace(p1, p1 + q06 + "\n")

# 2. After Section 1.3 bullet 4 (line ~117)
p2 = "- Fluxo de valor contínuo que transforma estratégias em benefícios tangíveis para os cidadãos e gestores públicos.\n"
assert p2 in content, "Pattern 2 not found"
content = content.replace(p2, p2 + q07 + "\n")

# 3. After Section 4.3 bullet 3 (line ~284)
p3 = "- *Cultura Organizacional:* Adequação dos ritos à maturidade do órgão e dos servidores envolvidos.\n"
assert p3 in content, "Pattern 3 not found"
content = content.replace(p3, p3 + q08 + "\n")

# 4. After Section 5.1 item 3 (line ~296)
p4 = "3. **Valor Agregado (VA ou EV - *Earned Value*):** A mensuração do trabalho **efetivamente executado**, avaliado em termos do orçamento originalmente aprovado para esse trabalho.\n"
assert p4 in content, "Pattern 4 not found"
content = content.replace(p4, p4 + q09 + "\n")

# 5. After Section 6 bullet 3 (line ~377)
p5 = "- **Balanceamento do Portfólio:** Equilíbrio equilibrado entre projetos de alta inovação (IA para auditoria), modernização de infraestrutura (migração para nuvem) e sustentação de sistemas legados essenciais.\n"
assert p5 in content, "Pattern 5 not found"
content = content.replace(p5, p5 + q10 + "\n")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("File 12_03 successfully updated!")
