import os

file_path = "fontes_de_estudo/conhecimentos_especificos_b02_ti/13_legislacao_aplicada_a_ti/02_marco_civil_da_internet_lei_12965_2014.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

q06 = """
---

### Questão 06 (FCC - Analista de Sistemas - Redes e Telecomunicações - Adaptada)
**Enunciado:** O Artigo 5º da Lei nº 12.965/2014 (Marco Civil da Internet) estabelece definições técnicas canônicas para a disciplina do uso da internet no Brasil. Com base nessas definições legais e no Decreto nº 8.771/2016, assinale a afirmativa correta:  

* **A)** O endereço IP é definido como o computador físico ou qualquer dispositivo móvel que se conecte diretamente a uma tomada de energia.
* **B)** A porta lógica de origem é um elemento descartável e sem relevância probatória, sendo expressamente proibido seu registro sob a arquitetura de Carrier-Grade NAT (CGNAT).
* **C)** Provedor de Conexão à Internet é a pessoa jurídica que fornece unicamente serviços de correio eletrônico e streaming de vídeo sob demanda.
* **D)** Conexão à Internet é a habilitação de um terminal para envio e recebimento de pacotes de dados na Internet, mediante a atribuição ou autenticação de um endereço IP.
* **E)** Aplicações de Internet limitam-se exclusivamente aos navegadores web instalados em computadores desktop de repartições públicas.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Computador ou dispositivo que se conecta à internet é o **Terminal** (Art. 5º, II). O **Endereço IP** é o código atribuído a um terminal para permitir sua identificação lógica (Art. 5º, III).
> - **B)** Incorreta. A porta lógica de origem é essencial para identificar o usuário específico sob CGNAT, no qual dezenas de conexões compartilham o mesmo endereço IPv4 público.
> - **C)** Incorreta. Quem fornece streaming e e-mail é o **Provedor de Aplicações de Internet** (Art. 5º, VII). O Provedor de Conexão habilita o terminal na rede (ISP).
> - **D)** **Correta.** Definição literal do Art. 5º, inciso V do Marco Civil: Conexão à Internet é a habilitação de um terminal para envio e recebimento de pacotes de dados na Internet, mediante a atribuição ou autenticação de um endereço IP.
> - **E)** Incorreta. Aplicações de Internet abrangem qualquer conjunto de funcionalidades acessíveis por terminal conectado à rede (redes sociais, sites, APIs, nuvem).
> 
> **Gabarito: D**
"""

q07 = """
---

### Questão 07 (FCC - Analista Judiciário - Tecnologia da Informação - Adaptada)
**Enunciado:** Em conformidade com o Art. 7º do Marco Civil da Internet (Lei nº 12.965/2014), o acesso à internet é essencial ao exercício da cidadania, sendo assegurados aos usuários diversos direitos fundamentais. A respeito desses direitos, assinale a afirmativa correta:  

* **A)** O sigilo das comunicações privadas armazenadas e do fluxo de comunicações na internet é inviolável, salvo por expressa e fundamentada ordem judicial nas hipóteses legais.
* **B)** As operadoras de telecomunicações podem suspender unilateralmente a conexão do usuário caso ele publique críticas políticas a autoridades públicas locais.
* **C)** É permitido aos provedores de internet comercializar os dados cadastrais e o histórico de navegação dos usuários sem o seu consentimento livre e informado.
* **D)** A navegação na internet implica renúncia tácita e perpétua a qualquer indenização por dano moral decorrente de violação da intimidade.
* **E)** O usuário não tem direito à exclusão definitiva dos dados pessoais que forneceu a uma aplicação de internet ao término da relação jurídica entre as partes.

> **Comentário Detalhado:**
>
> - **A)** **Correta.** O Art. 7º, incisos II e III da Lei nº 12.965/2014 estabelece a inviolabilidade e o sigilo do fluxo de comunicações e das comunicações privadas armazenadas, admitindo-se a quebra de sigilo exclusivamente por ordem judicial.
> - **B)** Incorreta. A suspensão da conexão só é permitida em decorrência de débito financeiro diretamente decorrente da utilização do serviço (Art. 7º, IV).
> - **C)** Incorreta. A cessão a terceiros de dados requer consentimento expresso, destacado e informado (Art. 7º, VII).
> - **D)** Incorreta. A inviolabilidade da intimidade e o direito à indenização plena por danos materiais e morais são garantias expressas (Art. 7º, I).
> - **E)** Incorreta. O titular tem direito expresso à exclusão definitiva dos seus dados ao término da relação, ressalvadas as hipóteses legais de guarda (Art. 7º, X).
> 
> **Gabarito: A**
"""

q08 = """
---

### Questão 08 (FCC - Auditor de Controle Externo / TI - Adaptada)
**Enunciado:** Durante a fiscalização de segurança e conformidade da infraestrutura de telecomunicações de um órgão estadual, os auditores analisaram o cumprimento das obrigações impostas aos provedores de conexão à internet. Nos termos do Art. 14 da Lei nº 12.965/2014 (Marco Civil da Internet), na provisão de conexão à internet:  

* **A)** É obrigatória a gravação em disco e indexação dos títulos de todos os vídeos e páginas web acessados por cada usuário, pelo prazo de cinco anos.
* **B)** É expressamente vedada a guarda dos registros de acesso a aplicações de internet.
* **C)** O provedor de conexão deve compartilhar os logs de navegação dos cidadãos com agências de publicidade mediante pagamento de taxa de administração.
* **D)** O administrador de sistema autônomo é obrigado a monitorar e interceptar o tráfego criptografado HTTPS sem necessidade de autorização judicial.
* **E)** A guarda dos registros de conexão é facultativa, podendo ser excluída a critério de conveniência da operadora de telecomunicações.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. É expressamente proibido aos provedores de conexão vigiar e registrar o histórico de navegação e as páginas que o usuário consome.
> - **B)** **Correta.** O Art. 14 da Lei nº 12.965/2014 veda expressamente a guarda dos registros de acesso a aplicações de internet na provisão de conexão à internet. O ISP guarda unicamente os registros de conexão (endereço IP, data/hora de início e fim da conexão), sem registrar quais sites ou aplicações foram acessados.
> - **C)** Incorreta. A comercialização de registros de navegação é manifestamente ilegal.
> - **D)** Incorreta. O provedor de conexão não pode interceptar nem inspecionar o fluxo de dados dos usuários sem ordem judicial.
> - **E)** Incorreta. A guarda dos registros de conexão é obrigação legal cogente pelo prazo de 1 ano (Art. 13).
> 
> **Gabarito: B**
"""

q09 = """
---

### Questão 09 (FCC - Auditor Estadual de Controle Externo / TI - Adaptada)
**Enunciado:** A requisição de dados perante provedores de internet é regulada pelo Marco Civil da Internet sob rigoroso regime de garantias. Em relação à requisição de dados cadastrais e de registros de conexão e de aplicações (Arts. 10 e 22), assinale a afirmativa correta:  

* **A)** Registros de conexão (IP, data, hora, porta lógica) podem ser requisitados diretamente por qualquer autoridade administrativa sem mandado judicial.
* **B)** A quebra de sigilo de registros de conexão ou de registros de acesso a aplicações de internet exige sempre expressa e motivada ordem judicial, sob pena de nulidade probatória.
* **C)** O juiz pode expedir ordem genérica e indeterminada para que um provedor entregue todos os registros de acessos de todos os cidadãos de um estado durante dez anos, sem indício de ilícito.
* **D)** Dados cadastrais de qualificação pessoal (como nome, filiação e endereço) possuem o mesmo tratamento probatório estrito dos conteúdos de mensagens sigilosas.
* **E)** Os provedores de internet estrangeiros que prestam serviços no Brasil estão dispensados de cumprir a legislação brasileira e ordens judiciais emitidas por juízes nacionais.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O fornecimento de registros de conexão e de acesso submete-se à cláusula de reserva de jurisdição (exige ordem judicial). Apenas dados cadastrais básicos podem ser solicitados por autoridades legalmente autorizadas.
> - **B)** **Correta.** Conforme os Arts. 10, § 1º e 22 do Marco Civil, os registros de conexão e de acesso a aplicações só podem ser disponibilizados mediante ordem judicial fundamentada que aponte fundados indícios de ilícito, justificativa da utilidade e período determinado.
> - **C)** Incorreta. Ordens genéricas (*fishing expeditions*) são expressamente vedadas pelo Art. 22, parágrafo único (exige período determinado e indícios de crime).
> - **D)** Incorreta. A jurisprudência e a lei diferenciam dados cadastrais (acessíveis com menor formalidade) de registros de conexão e conteúdo de comunicações (protegidos por reserva judicial estrita).
> - **E)** Incorreta. Conforme o Art. 11, aplica-se a lei brasileira a qualquer empresa que preste serviços ao público brasileiro ou que tenha filial no país.
> 
> **Gabarito: B**
"""

q10 = """
---

### Questão 10 (FCC - Analista Judiciário - Área Apoio Especializado / TI - Adaptada)
**Enunciado:** O regime de responsabilidade civil por danos decorrentes de conteúdo gerado por terceiros na internet foi disciplinado nos artigos 18 e 19 da Lei nº 12.965/2014. A respeito desse regime jurídico, assinale a afirmativa correta:  

* **A)** O provedor de conexão à internet responde solidariamente por todas as postagens caluniosas feitas pelos usuários que utilizam seus cabos de fibra óptica.
* **B)** O provedor de aplicações de internet (como uma rede social) responde civilmente de plano por injúrias publicadas por terceiros assim que recebe uma notificação extrajudicial enviada por e-mail pelo ofendido.
* **C)** O provedor de conexão à internet não responderá civilmente por danos decorrentes de conteúdo gerado por terceiros (Art. 18).
* **D)** A regra geral do Artigo 19 estabelece que o provedor de aplicações é proibido de cumprir ordens judiciais de remoção de conteúdos ilegais.
* **E)** As plataformas de internet são obrigadas a censurar previamente todo e qualquer texto ou comentário antes que ele seja publicado na rede.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Pelo Art. 18, o provedor de conexão goza de imunidade civil absoluta por danos causados por conteúdos veiculados por terceiros.
> - **B)** Incorreta. Na regra geral (Art. 19), a responsabilidade civil do provedor de aplicação depende de prévia ordem judicial específica; notificações extrajudiciais privadas não geram o dever de indenizar pela manutenção do conteúdo (salvo na exceção de nudez/sexo não consensual do Art. 21).
> - **C)** **Correta.** Redação expressa do Art. 18 da Lei nº 12.965/2014: "O provedor de conexão à internet não responderá civilmente por danos decorrentes de conteúdo gerado por terceiros."
> - **D)** Incorreta. O descumprimento da ordem judicial atrai a responsabilização civil subsidiária da plataforma.
> - **E)** Incorreta. A censura prévia é expressamente vedada pela Constituição Federal e pelo Marco Civil.
> 
> **Gabarito: C**
"""

# Insertions:
# 1. After Section 1.1 item 9 (line ~58)
p1 = "9. **Provedor de Aplicações de Internet:** Pessoa natural ou jurídica que disponibiliza serviços, plataformas e aplicações na Internet, explorados ou não comercialmente.\n"
assert p1 in content, "Pattern 1 not found"
content = content.replace(p1, p1 + q06 + "\n")

# 2. After Section 1.2 bullet 4 (line ~71)
p2 = "- Informações claras e completas sobre coleta, uso, armazenamento e tratamento de dados pessoais.\n"
assert p2 in content, "Pattern 2 not found"
content = content.replace(p2, p2 + q07 + "\n")

# 3. After Section 3.2 (line ~236)
p3 = "Isso significa que o provedor de banda larga (como Claro, Vivo, Oi ou provedores locais) **não pode bisbilhotar nem gravar quais sites, vídeos ou serviços o usuário navegou**. O provedor sabe apenas que o usuário estava conectado à internet e qual IP ele utilizou, mas não o que ele consumiu na web.\n"
assert p3 in content, "Pattern 3 not found"
content = content.replace(p3, p3 + q08 + "\n")

# 4. After Section 4 item 3 (line ~263)
p4 = "    - Período determinado ao qual se referem os registros (são vedadas ordens genéricas de devassa indeterminada).\n"
assert p4 in content, "Pattern 4 not found"
content = content.replace(p4, p4 + q09 + "\n")

# 5. After Section 5.2 (line ~307)
p5 = "- Notificações extrajudiciais privadas (cartas de advogados, e-mails de reclamação) **não** geram responsabilidade civil para a plataforma na regra geral!\n"
assert p5 in content, "Pattern 5 not found"
content = content.replace(p5, p5 + q10 + "\n")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("File 13_02 successfully updated!")
