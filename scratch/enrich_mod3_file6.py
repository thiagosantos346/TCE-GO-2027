import os, re

FILE = r"fontes_de_estudo/conhecimentos_gerais/03_legislacao_institucional/06_politicas_institucionais_e_resolucoes_normativas.md"

q06_text = """
### Questão 06
**(FCC – Inédita – Padrão TCE-GO)**  
De acordo com a Estrutura Organizacional e Competências Técnicas do TCE-GO aprovada pela Resolução Administrativa nº 14/2025:

* **A)** A Secretaria-Geral de Controle Externo subordina-se hierarquicamente à Procuradoria-Geral do Estado para fins de definição das diretrizes de auditoria.
* **B)** A macroestrutura executiva do Tribunal de Contas do Estado de Goiás compreende unidades de assessoramento superior, a Secretaria de Controle Externo (responsável pela coordenação executiva e técnica das ações fiscalizatórias especializadas) e a Secretaria de Gestão Integrada, estruturadas para conferir celeridade, inovação e rigor metodológico ao controle governamental.
* **C)** A criação ou extinção de diretorias e secretarias operacionais dispensa qualquer aprovação do Tribunal Pleno.
* **D)** As equipes de auditoria técnica das gerências especializadas possuem competência para aplicar multas e emitir acórdãos terminativos de forma monocrática e independente do Tribunal Pleno.
* **E)** As decisões administrativas sobre recursos humanos da Secretaria de Controle Externo são julgadas exclusivamente pelo Ministério Público de Contas.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O Tribunal de Contas goza de autonomia administrativa, financeira e institucional garantida pela Constituição (art. 73 c/c art. 96 da CF/88), inexistindo qualquer subordinação à PGE.
> - **B)** Correta. A Resolução Administrativa nº 14/2025 estabeleceu o organograma moderno do TCE-GO, delineando a divisão das atribuições finalísticas de fiscalização contábil, financeira e operacional sob a coordenação técnica da Secretaria de Controle Externo, atuando em harmonia com as secretarias de governança e apoio corporativo.
> - **C)** Incorreta. A organização interna e a fixação de competências das unidades decorrem de deliberação normativa colegiada do Pleno.
> - **D)** Incorreta. As unidades técnicas de fiscalização emitem relatórios de auditoria, notas técnicas e pareceres instrutórios; a competência para julgar e aplicar penalidades é privativa dos colegiados (Pleno e Câmaras) e dos relatores, nos limites regimentais.
> - **E)** Incorreta. A gestão administrativa de pessoal compete à Presidência do Tribunal.
>
> **Gabarito: B**
"""

q07_text = """
### Questão 07
**(FCC – Inédita – Padrão TCE-GO)**  
A Política de Segurança da Informação (PSI) do TCE-GO, instituída pela Resolução Administrativa nº 17/2024, baseia-se nos pilares essenciais da segurança cibernética (CIDA+L). No tocante à classificação e ao tratamento da informação institucional:

* **A)** Toda informação produzida ou custodiada pelo Tribunal é classificada automaticamente como ultrassecreta por tempo indeterminado, sendo vedado o acesso aos cidadãos.
* **B)** As informações no âmbito do TCE-GO são classificadas quanto ao grau de confidencialidade (pública, interna, restrita e sigilosa), cabendo aos servidores e colaboradores zelar pela salvaguarda das credenciais de acesso, sendo proibido o compartilhamento de senhas individuais e a utilização de dispositivos particulares não autorizados para armazenamento de dados corporativos.
* **C)** O compartilhamento de senhas funcionais de acesso à rede interna entre colegas de uma mesma equipe de auditoria é estimulado pela PSI para garantir a continuidade dos serviços.
* **D)** O pilar da autenticidade assegura que a informação permaneça acessível aos usuários mesmo em situações de ataque de negação de serviço.
* **E)** Incidentes de quebra de sigilo ou vazamento cibernético de dados dispensam notificação à área de segurança da informação se resolvidos internamente no setor em 24 horas.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Pelo princípio constitucional da publicidade (art. 37 da CF/88 e Lei de Acesso à Informação), a publicidade é a regra geral e o sigilo é a exceção devidamente fundamentada.
> - **B)** Correta. A RA nº 17/2024 (PSI) estrutura a proteção de dados e ativos corporativos do TCE-GO em conformidade com as normas ABNT NBR ISO/IEC 27001 e 27002, estabelecendo a taxonomia formal de classificação da informação e impondo a responsabilidade individual e intransferível pelo uso de credenciais e senhas funcionais de acesso.
> - **C)** Incorreta. As credenciais de acesso são estritamente pessoais e intransferíveis; compartilhar senhas constitui grave infração de segurança da informação.
> - **D)** Incorreta. A garantia de disponibilidade contínua refere-se ao pilar da **Disponibilidade**; o pilar da **Autenticidade** assegura a identidade inequívoca do autor ou emissor da informação.
> - **E)** Incorreta. Qualquer incidente de segurança da informação deve ser imediatamente comunicado à equipe de resposta a incidentes (CSIRT/TI) da Corte.
>
> **Gabarito: B**
"""

q08_text = """
### Questão 08
**(FCC – Inédita – Padrão TCE-GO)**  
Em relação à governança de privacidade e à proteção de dados pessoais no âmbito do TCE-GO (Resolução Normativa nº 5/2024, em sintonia com a Lei Geral de Proteção de Dados Pessoais - LGPD, Lei nº 13.709/2018):

* **A)** O tratamento de dados pessoais realizado pelo TCE-GO para o cumprimento de suas competências constitucionais de fiscalização e controle externo depende do prévio e expresso consentimento de cada gestor auditado.
* **B)** O Tribunal de Contas pode tratar dados pessoais de jurisdicionados, licitantes e servidores sem necessidade de consentimento do titular, com fundamento na base legal do cumprimento de obrigação legal e execução de políticas públicas previstas em lei (arts. 7º, II e III, e 23 da LGPD), devendo observar o princípio da minimização e adotar salvaguardas técnicas adequadas.
* **C)** O Encarregado pelo Tratamento de Dados Pessoais (DPO) do TCE-GO responde solidariamente com seu patrimônio pessoal por qualquer vazamento externo provocado por criminosos virtuais.
* **D)** O Relatório de Impacto à Proteção de Dados Pessoais (RIPD) é documento dispensável mesmo quando houver tratamento de dados sensíveis em larga escala.
* **E)** Os titulares de dados perdem qualquer direito de informação ou retificação de seus dados cadastrais perante o Tribunal de Contas.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Exigir consentimento prévio inviabilizaria a própria atividade de auditoria e repressão à corrupção. A LGPD expressamente afasta a exigência de consentimento para a atuação de órgãos estatais no cumprimento de deveres legais (art. 7º, II) e exercício regular de direitos em processos administrativos (art. 7º, VI).
> - **B)** Correta. A RN nº 5/2024 disciplina com precisão a incidência da LGPD no controle externo goiano: a atuação fiscalizatória apoia-se em hipóteses legais vinculadas (art. 23 da LGPD), dispensando consentimento, mas submetendo o TCE-GO aos princípios reitores da lei, em especial a **finalidade legítima**, a **adequação**, a **segurança da informação** e a **minimização** (coletar apenas os dados estritamente necessários ao objetivo da auditoria).
> - **C)** Incorreta. O Encarregado (DPO) atua como canal de comunicação entre o órgão, os titulares e a ANPD, não assumindo responsabilidade patrimonial automática por ações criminosas de terceiros.
> - **D)** Incorreta. O RIPD é obrigatório e fundamental quando o tratamento de dados envolver riscos relevantes aos direitos dos titulares ou dados sensíveis.
> - **E)** Incorreta. Os direitos básicos dos titulares assegurados pelo art. 18 da LGPD (confirmação de tratamento, acesso e correção) são garantidos no que for compatível com a tutela do sigilo legal das investigações.
>
> **Gabarito: B**
"""

q09_text = """
### Questão 09
**(FCC – Inédita – Padrão TCE-GO)**  
A Resolução Administrativa nº 24/2024 estabelece a Política de Governança e Uso de Inteligência Artificial no TCE-GO. Sobre as diretrizes éticas e operacionais de ferramentas de IA na Corte de Contas goiana, é correto afirmar:

* **A)** É permitida a delegação integral da tomada de decisão de mérito em processos de contas aos algoritmos de inteligência artificial generativa, dispensando a intervenção humana.
* **B)** É expressamente vedada a inserção de documentos sigilosos, dados pessoais não públicos ou peças de auditoria sob segredo de justiça em modelos públicos ou abertos de inteligência artificial generativa baseados em nuvem externa, subsistindo a supervisão humana obrigatória (*human-in-the-loop*) e a responsabilidade funcional indelegável do servidor que utilizar a ferramenta.
* **C)** A inteligência artificial pode ser utilizada para gerar automaticamente acórdãos condenatórios sem conferência técnica do relator.
* **D)** As ferramentas de IA utilizadas no Tribunal são dispensadas de observar princípios de explicabilidade e auditabilidade algorítmica.
* **E)** O servidor que assina relatório gerado com auxílio de IA fica isento de responsabilidade por erros materiais ou alucinações de conteúdo produzidas pela máquina.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A tomada de decisão jurisdicional e sancionatória é ato privativo e indelegável de agentes públicos humanos investidos de autoridade constitucional.
> - **B)** Correta. A RA nº 24/2024 do TCE-GO consagra balizas de vanguarda na governança de IA pública: 1) Vedação peremptória ao upload de dados sigilosos e informações sob segredo em plataformas públicas abertas (para evitar vazamentos e quebra da LGPD); 2) O princípio da supervisão humana compulsória (*human-in-the-loop*); 3) A responsabilidade pessoal e intransferível do servidor operador por todo e qualquer texto ou cálculo incorporado às minutas oficiais.
> - **C)** Incorreta. A decisão colegiada exige juízo crítico motivado do julgador humano.
> - **D)** Incorreta. A transparência, explicabilidade e auditabilidade dos sistemas inteligentes são exigências éticas fundamentais da norma.
> - **E)** Incorreta. O servidor responde plenamente por qualquer "alucinação", dado incorreto ou citação inexistente formulada pela IA que for submetida sem a devida validação humana.
>
> **Gabarito: B**
"""

q10_text = """
### Questão 10
**(FCC – Inédita – Padrão TCE-GO)**  
Quanto ao regime de teletrabalho disciplinado na Política de Gestão de Pessoas do TCE-GO (Resolução Administrativa nº 5/2024):

* **A)** O teletrabalho é direito subjetivo incondicionado de todo servidor recém-empossado, independentemente de avaliação do estágio probatório ou interesse da administração.
* **B)** A adesão ao teletrabalho vincula-se ao cumprimento de plano de trabalho com metas de desempenho superiores às da atividade presencial, sendo vedada a concessão do regime a servidores que estejam respondendo a processo administrativo disciplinar ou que tenham sofrido penalidade funcional recente.
* **C)** No regime de teletrabalho, o servidor fica desobrigado de manter canais de comunicação ativos durante o horário regular de funcionamento do Tribunal.
* **D)** O não atingimento imotivado das metas de desempenho fixadas no plano de trabalho acarreta a promoção automática do servidor por merecimento presumido.
* **E)** O teletrabalho impede a realização de auditorias presenciais mesmo quando expressamente requisitadas pelo relator dos autos.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O teletrabalho não constitui direito adquirido nem subjetivo incondicional; é ato discricionário deferido no estrito interesse e conveniência do serviço público.
> - **B)** Correta. De acordo com a RA nº 5/2024, a inclusão no regime de teletrabalho no TCE-GO exige pactuação formal de metas de produtividade e qualidade (geralmente fixadas em patamar superior ao presencial), observando-se vedações expressas, tais como a existência de penalidade disciplinar nos últimos anos ou tramitação de PAD por falta funcional grave.
> - **C)** Incorreta. O servidor em teletrabalho deve manter plena disponibilidade de comunicação (telefone, e-mail institucional, aplicativo corporativo) durante a jornada regular.
> - **D)** Incorreta. O descumprimento injustificado das metas resulta no imediato desligamento do regime de teletrabalho e na apuração de eventuais faltas funcionais.
> - **E)** Incorreta. O servidor em teletrabalho permanece obrigado a comparecer ao Tribunal ou a diligências externas sempre que convocado pela chefia ou pelo Relator.
>
> **Gabarito: B**
"""

def enrich_mod3_file6():
    with open(FILE, "r", encoding="utf-8") as f:
        text = f.read()

    # Inserção da Questão 06: no fim da Seção 1 (antes de "## 2. Política de Segurança da Informação - PSI")
    sec2 = "## 2. Política de Segurança da Informação - PSI (RA nº 17/2024)"
    idx2 = text.find(sec2)
    dash_idx = text.rfind("---", 0, idx2)
    text = text[:dash_idx] + q06_text + "\n---\n\n" + text[dash_idx:]

    # Inserção da Questão 07: no fim da Seção 2 (antes de "## 3. Tratamento e Proteção de Dados Pessoais - LGPD")
    sec3 = "## 3. Tratamento e Proteção de Dados Pessoais - LGPD (RN nº 5/2024)"
    idx3 = text.find(sec3)
    dash_idx = text.rfind("---", 0, idx3)
    text = text[:dash_idx] + q07_text + "\n---\n\n" + text[dash_idx:]

    # Inserção da Questão 08: no fim da Seção 3 (antes de "## 4. Governança e Uso de Inteligência Artificial")
    sec4 = "## 4. Governança e Uso de Inteligência Artificial no TCE-GO (RA nº 24/2024)"
    idx4 = text.find(sec4)
    dash_idx = text.rfind("---", 0, idx4)
    text = text[:dash_idx] + q08_text + "\n---\n\n" + text[dash_idx:]

    # Inserção da Questão 09: no fim da Seção 4 (antes de "## 5. Gestão de Pessoas, Comunicação e Planejamento Integrado")
    sec5 = "## 5. Gestão de Pessoas, Comunicação e Planejamento Integrado"
    idx5 = text.find(sec5)
    dash_idx = text.rfind("---", 0, idx5)
    text = text[:dash_idx] + q09_text + "\n---\n\n" + text[dash_idx:]

    # Inserção da Questão 10: no fim da Seção 5 (antes de "## 6. Fontes Oficiais e Referências Bibliográficas")
    sec_fontes = "## 6. Fontes Oficiais e Referências Bibliográficas"
    idxf = text.find(sec_fontes)
    dash_idx = text.rfind("---", 0, idxf)
    text = text[:dash_idx] + q10_text + "\n---\n\n" + text[dash_idx:]

    with open(FILE, "w", encoding="utf-8") as f:
        f.write(text)

    print("Module 03 File 06 enriquecido com sucesso.")

enrich_mod3_file6()
