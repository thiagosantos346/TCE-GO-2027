import os

file_path = "fontes_de_estudo/conhecimentos_especificos_b02_ti/12_governanca_de_ti/05_governo_digital_lei_14129_e_engd_2024_2027.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

q06 = """
---

### Questão 06 (FCC - Auditor Estadual de Controle Externo / TI - Adaptada)
**Enunciado:** A Lei Federal nº 14.129/2021 estabelece princípios, regras e instrumentos para o Governo Digital e o aumento da eficiência pública. Em relação ao âmbito de aplicação subjetivo e institucional da referida lei, assinale a afirmativa correta:  

* **A)** A Lei do Governo Digital aplica-se com exclusividade ao Poder Executivo Federal, sendo expressamente vedada sua aplicação aos Estados, Distrito Federal e Municípios.
* **B)** A norma aplica-se aos órgãos da administração direta e indireta da União, dos Estados, do DF e dos Municípios, abrangendo expressamente os Poderes Executivo, Judiciário e Legislativo, bem como os Tribunais de Contas e o Ministério Público.
* **C)** Os Tribunais de Contas e as empresas estatais que prestam serviços públicos foram formalmente excluídos da incidência da Lei nº 14.129/2021 por emenda parlamentar.
* **D)** A aplicação da lei é facultativa para os municípios que não possuam data center próprio com servidores locais de alta densidade.
* **E)** Apenas os cartórios de registro civil privados com delegação notarial estão obrigados a cumprir as metas da Lei nº 14.129/2021.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A lei possui alcance federativo amplo e obrigatório em âmbito nacional.
> - **B)** **Correta.** De acordo com o Art. 2º da Lei nº 14.129/2021, a norma aplica-se aos órgãos da administração direta e indireta de todos os entes federados (União, Estados, DF e Municípios), abarcando os Poderes Executivo, Legislativo (incluídos os Tribunais de Contas), Judiciário e Ministério Público.
> - **C)** Incorreta. Os Tribunais de Contas estão expressamente subordinados às diretrizes de governo digital, transparência e interoperabilidade da lei.
> - **D)** Incorreta. A obrigatoriedade independe de infraestrutura própria prévia; incentiva-se o compartilhamento de recursos em nuvem e plataformas comuns.
> - **E)** Incorreta. A lei disciplina a atuação dos órgãos e entidades da Administração Pública.
> 
> **Gabarito: B**
"""

q07 = """
---

### Questão 07 (FCC - Analista de TI / Sistemas - Adaptada)
**Enunciado:** A plataforma digital única GOV.BR disponibiliza mecanismos de autenticação com três níveis progressivos de segurança e confiabilidade cadastral: Bronze, Prata e Ouro. A respeito dos requisitos para obtenção desses níveis e seus respectivos graus de privilégio, assinale a alternativa correta:  

* **A)** A conta de nível Bronze exige compulsoriamente a validação biométrica facial do usuário cruzada com a base de dados da Justiça Eleitoral (TSE/CIN).
* **B)** O nível Prata pode ser obtido mediante validação biométrica facial na base da CNH (Senatran) ou validação de credenciais bancárias de instituições financeiras credenciadas via Open Finance.
* **C)** O nível Ouro restringe-se unicamente ao envio de SMS para telefone celular pré-pago sem necessidade de confirmação cadastral prévia.
* **D)** A obtenção de qualquer nível de conta no GOV.BR exige a presença física obrigatória do cidadão em Brasília com pagamento de taxa consular.
* **E)** O nível Bronze é o único que autoriza a realização de transações fiscais sigilosas críticas e a assinatura eletrônica avançada de contratos administrativos.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A biometria facial com o TSE/CIN confere o nível Ouro, e não Bronze. O nível Bronze baseia-se em cadastro online básico ou cruzamento simples com INSS/Receita.
> - **B)** **Correta.** O nível Prata (nível intermediário com alta confiabilidade) é concedido via validação biométrica com a base da Carteira Nacional de Habilitação (Senatran) ou por autenticação através de internet banking/Open Finance de bancos credenciados.
> - **C)** Incorreta. O nível Ouro (nível avançado de segurança máxima) requer validação biométrica na base da Justiça Eleitoral / Carteira de Identidade Nacional (CIN) ou certificado digital ICP-Brasil.
> - **D)** Incorreta. A criação e elevação de níveis das contas GOV.BR é totalmente digital, remota e gratuita pelo aplicativo ou portal oficial.
> - **E)** Incorreta. A assinatura eletrônica avançada e serviços críticos exigem no mínimo nível Prata ou Ouro.
> 
> **Gabarito: B**
"""

q08 = """
---

### Questão 08 (FCC - Analista de Sistemas - Governança Digital - Adaptada)
**Enunciado:** O modelo conceitual de 'Governo Como Plataforma' (*Government as a Platform - GaaP*) e as diretrizes de interoperabilidade da Lei nº 14.129/2021 estabelecem uma nova arquitetura para a tecnologia no setor público. A respeito desse modelo, assinale a afirmativa correta:  

* **A)** Cada órgão público deve programar seus próprios sistemas em silos isolados, sendo proibida a utilização de APIs governamentais compartilhadas para troca de informações.
* **B)** O paradigma de Governo Como Plataforma promove a criação de componentes de software reutilizáveis, barramentos de interoperabilidade e APIs abertas que permitem a integração fluida entre múltiplos órgãos públicos e serviços digitais da sociedade.
* **C)** O GaaP exige que todas as soluções digitais governamentais sejam desenvolvidas exclusivamente em código binário assembly proprietário de uma única multinacional.
* **D)** A interoperabilidade de dados entre entes estatais visa impedir que os cidadãos acessem serviços pela internet, obrigando o retorno aos formulários manuais datilografados.
* **E)** A plataforma de interoperabilidade ConectaGov é exclusiva para entidades privadas e não pode ser integrada a sistemas de Tribunais de Contas.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O isolamento em silos de informação é exatamente o modelo obsoleto que a arquitetura GaaP busca erradicar.
> - **B)** **Correta.** No Governo Como Plataforma (GaaP), o Estado fornece blocos fundamentais de infraestrutura digital compartilhada (autenticação, pagamento, barramentos de mensageria e APIs padronizadas), permitindo a prestação integrada e contínua de serviços públicos sem duplicação de custos.
> - **C)** Incorreta. O modelo prioriza padrões abertos, interoperabilidade universal e formatos neutros legíveis por máquina.
> - **D)** Incorreta. O objetivo da interoperabilidade é facilitar a vida do cidadão, tornando os serviços rápidos e integrados.
> - **E)** Incorreta. O ConectaGov é o ecossistema federativo público para integração entre sistemas e bases de dados do Estado brasileiro.
> 
> **Gabarito: B**
"""

q09 = """
---

### Questão 09 (FCC - Auditor de Controle Externo / TI - Adaptada)
**Enunciado:** A Estratégia Nacional de Governo Digital (ENGD 2024–2027), instituída pelo Decreto nº 12.069/2024, consagra princípios de articulação federativa para a transformação digital do Estado. Sobre a abrangência e objetivos da ENGD 2024–2027, assinale a afirmativa correta:  

* **A)** A ENGD restringe suas metas à modernização dos gabinetes dos Ministérios da Esplanada em Brasília, vedando repasses de tecnologia aos Estados e Municípios.
* **B)** A nova estratégia adota abordagem estritamente federativa, buscando diminuir disparidades regionais e integrar serviços públicos digitais da União, dos Estados, do DF e dos Municípios em torno de padrões comuns de interoperabilidade e segurança.
* **C)** O Decreto nº 12.069/2024 determinou a extinção de todas as políticas de dados abertos e transparência ativa no Brasil.
* **D)** A ENGD estabelece que os serviços digitais governamentais devem ser inacessíveis a pessoas com deficiência física ou visual.
* **E)** A transformação digital preconizada pela ENGD visa terceirizar integralmente a gestão da política de segurança cibernética nacional para provedores internacionais sem regulação.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A ENGD 2024–2027 possui abrangência nacional e caráter expressamente federativo, alcançando os 26 estados, o DF e os mais de 5.500 municípios brasileiros.
> - **B)** **Correta.** O Decreto nº 12.069/2024 foi concebido para unificar a estratégia de transformação digital em nível federativo, superando fragmentações regionais através de padrões interoperáveis, segurança jurídica e inclusão social.
> - **C)** Incorreta. O Eixo 3 da ENGD é dedicado especificamente a 'Governo Aberto e Transparente'.
> - **D)** Incorreta. O Eixo 5 foca na acessibilidade, linguagem simples e multicanalidade para garantia de inclusão.
> - **E)** Incorreta. A soberania e a segurança cibernética (Eixo 2) são prioridades estratégicas nacionais e indelegáveis.
> 
> **Gabarito: B**
"""

q10 = """
---

### Questão 10 (FCC - Técnico de Controle Externo / TI - Adaptada)
**Enunciado:** A ENGD 2024–2027 (Decreto nº 12.069/2024) preconiza a transição de um modelo de serviços puramente reativo para a oferta de Serviços Públicos Proativos, alicerçados no conceito de Infraestrutura Pública Digital (DPI - *Digital Public Infrastructure*). A respeito desses conceitos, assinale a afirmativa correta:  

* **A)** Nos serviços públicos proativos, o Estado identifica automaticamente que o cidadão atingiu os requisitos previstos em lei e concede/oferece ativamente o serviço sem que o indivíduo precise solicitá-lo formalmente ou enfrentar burocracias de protocolo prévio.
* **B)** A Infraestrutura Pública Digital (DPI) baseia-se na volta do uso de fichas de papelão perfuradas para armazenamento de cadastros sociais.
* **C)** No modelo proativo, o cidadão é obrigado a contratar despachantes privados para intermediar eletronicamente o acesso aos benefícios sociais a que tem direito.
* **D)** A DPI é composta exclusivamente por impressoras matriciais de alta velocidade, excluindo componentes de identidade digital ou pagamentos instantâneos.
* **E)** O modelo proativo exige que o cidadão protocole petições físicas anuais perante o Tribunal de Contas para validar sua existência civil.

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Os serviços proativos representam uma quebra de paradigma na relação Estado-cidadão: graças à interoperabilidade de dados e inteligência analítica, o poder público reconhece o direito adquirido do usuário e o disponibiliza ativamente, notificando-o em seus canais digitais.
> - **B)** Incorreta. DPI (*Digital Public Infrastructure*) é o conjunto de trilhos digitais modernos (Identidade Digital, Pagamentos Digitais Instantâneos e Barramentos de Dados).
> - **C)** Incorreta. A proatividade visa eliminar a burocracia e custos de intermediação para o cidadão.
> - **D)** Incorreta. Os três pilares mundiais da DPI são Identidade Digital Unificada, Sistemas de Pagamentos Instantâneos (ex.: Pix/PagTesouro) e Troca Segura de Dados via APIs.
> - **E)** Incorreta. A validação é eletrônica, automática e sem fricção burocrática presencial.
> 
> **Gabarito: A**
"""

# Insertions:
# 1. After Section 1.1 item 3 (line ~53)
p1 = "3. Às empresas públicas e sociedades de economia mista que prestem serviços públicos.\n"
assert p1 in content, "Pattern 1 not found"
content = content.replace(p1, p1 + q06 + "\n")

# 2. After Section 1.3 table row Ouro (line ~160)
p2 = "| **Ouro** | Validação biométrica facial na base da Justiça Eleitoral (TSE / Carteira de Identidade Nacional - CIN); ou validação por Certificado Digital padrão ICP-Brasil (A1 ou A3). | Nível máximo de segurança: acesso irrestrito a todos os serviços críticos, sigilosos, declaração pré-preenchida do Imposto de Renda e assinaturas eletrônicas. |\n"
assert p2 in content, "Pattern 2 not found"
content = content.replace(p2, p2 + q07 + "\n")

# 3. After Section 1.5 bullet 3 (line ~219)
p3 = "- Racionalização de custos de TIC e eliminação de duplicação de dados entre a União, Estados e Municípios.\n"
assert p3 in content, "Pattern 3 not found"
content = content.replace(p3, p3 + q08 + "\n")

# 4. After Section 2.1 (line ~229)
p4 = "A ENGD 2024–2027 é uma política pública de **amplitude nacional federativa**, coordenada para articular a transformação digital integrada de todos os entes federativos (União, 26 Estados, DF e Municípios), promovendo a interoperabilidade e reduzindo disparidades regionais de infraestrutura e capacidade de atendimento digital.\n"
assert p4 in content, "Pattern 4 not found"
content = content.replace(p4, p4 + q09 + "\n")

# 5. After Section 2.3 item 3 (line ~317)
p5 = "3. **Barramento Seguro de Dados:** Troca segura de informações via APIs e ConectaGov, com rastreabilidade e controle estrito de acessos.\n"
assert p5 in content, "Pattern 5 not found"
content = content.replace(p5, p5 + q10 + "\n")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("File 12_05 successfully updated!")
