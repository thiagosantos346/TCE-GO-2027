import os

file_path = "fontes_de_estudo/conhecimentos_especificos_b02_ti/13_legislacao_aplicada_a_ti/01_lgpd_aplicada_ao_desenvolvimento_e_sistemas.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

q06 = """
---

### Questão 06 (FGV - TJ-RR - Analista Judiciário - Governança e Gestão de TI - Adaptada)
**Enunciado:** No contexto da Lei Geral de Proteção de Dados Pessoais (LGPD - Lei nº 13.709/2018), a definição dos papéis dos agentes de tratamento e do encarregado é essencial para estabelecer responsabilidades jurídicas e arquiteturais em sistemas informatizados. Acerca do Controlador, do Operador e do Encarregado (DPO), assinale a afirmativa correta:  

* **A)** O Controlador é a pessoa natural ou jurídica responsável por executar o tratamento estritamente sob as ordens do Operador, sem qualquer poder deliberativo sobre a finalidade dos dados.
* **B)** O Operador decide monocraticamente as bases legais e as finalidades institucionais do tratamento, atuando como o titular patrimonial dos dados.
* **C)** O Encarregado (DPO) tem a responsabilidade exclusiva de indenizar os titulares em caso de vazamento ilícito de dados perpetrado por hackers.
* **D)** O Controlador compete as decisões referentes ao tratamento de dados pessoais; o Operador realiza o tratamento em nome do controlador e segundo suas diretrizes; e o Encarregado atua como canal de comunicação entre o controlador, os titulares dos dados e a ANPD.
* **E)** O papel de Encarregado pelo tratamento de dados pessoais só pode ser desempenhado por servidores públicos federais da carreira policial, vedada a indicação de terceirizados ou pessoas jurídicas.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O Controlador é quem toma as decisões sobre o tratamento (finalidades e meios essenciais); o Operador é quem executa as ordens.
> - **B)** Incorreta. O Operador apenas processa os dados em nome do Controlador e conforme suas instruções contratuais.
> - **C)** Incorreta. A responsabilidade civil de indenização recai sobre os agentes de tratamento (Controlador e Operador), não pessoalmente sobre o DPO no exercício regular de suas funções orientadoras.
> - **D)** **Correta.** Definição literal da LGPD (Art. 5º, incisos VI, VII e VIII): Controlador: a quem competem as decisões; Operador: quem realiza o tratamento em nome do controlador; Encarregado: pessoa indicada para atuar como canal de comunicação entre controlador, titulares e ANPD.
> - **E)** Incorreta. O DPO pode ser pessoa natural ou jurídica, integrante do quadro próprio ou contratado externo (*DPO as a Service*).
> 
> **Gabarito: D**
"""

q07 = """
---

### Questão 07 (FCC - Analista de Sistemas / Engenharia de Software - Adaptada)
**Enunciado:** O Artigo 6º da LGPD estabelece dez princípios fundamentais que regem as atividades de tratamento de dados pessoais. Sob a ótica da Engenharia de Software e da Arquitetura de Dados, o princípio da **Necessidade** (também denominado princípio da **Minimização de Dados**) impõe que os sistemas corporativos:  

* **A)** Devem coletar a maior quantidade possível de dados pessoais e biometrias em formulários públicos, mesmo sem utilidade atual, prevendo eventuais demandas futuras de machine learning.
* **B)** Devem limitar o tratamento ao mínimo necessário para a realização de suas finalidades específicas, abrangendo apenas dados pertinentes, proporcionais e não excessivos em relação aos objetivos do serviço.
* **C)** Estão autorizados a manter permanentemente em tabelas de log o histórico de senhas em texto puro de todos os usuários cadastrados.
* **D)** Devem conceder privilégios irrestritos de administrador de banco de dados (DBA) a todos os desenvolvedores juniores e fornecedores terceirizados.
* **E)** Devem publicar automaticamente no Portal de Transparência os dados bancários e exames de saúde privados dos servidores públicos.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A coleta especulativa de dados sem utilidade imediata viola frontalmente o princípio da necessidade/minimização e da finalidade.
> - **B)** **Correta.** Conforme o Art. 6º, III, da LGPD, o princípio da necessidade determina a limitação do tratamento ao mínimo necessário para a realização de suas finalidades, com abrangência dos dados pertinentes, proporcionais e não excessivos em relação aos objetivos do tratamento.
> - **C)** Incorreta. Gravar senhas em texto puro viola gravemente os princípios de segurança e prevenção (Art. 6º, VII e VIII).
> - **D)** Incorreta. A concessão excessiva de privilégios contraria o princípio do privilégio mínimo (*least privilege*) e da segurança.
> - **E)** Incorreta. Dados de saúde são dados pessoais sensíveis e sigilosos, cuja exposição indevida acarreta ilicitude severa.
> 
> **Gabarito: B**
"""

q08 = """
---

### Questão 08 (FCC - Técnico de Controle Externo / TI - Adaptada)
**Enunciado:** Na implementação dos conceitos de Proteção de Dados desde a Concepção (*Privacy by Design*) e por Padrão (*Privacy by Default*), a equipe de desenvolvimento de software de um Tribunal de Contas deve adotar padrões arquiteturais restritivos nativos. A respeito da regra do *Privacy by Default*, assinale a afirmativa correta:  

* **A)** O sistema deve ser configurado para que, por padrão de fábrica (*out-of-the-box*), as configurações mais protetivas à privacidade sejam ativadas automaticamente, exigindo ação deliberada do usuário caso deseje compartilhar dados adicionais.
* **B)** O sistema deve vir de fábrica com todos os compartilhamentos de dados públicos e autorizações de cookies de rastreamento habilitados compulsoriamente.
* **C)** O *Privacy by Default* veda expressamente a implementação de qualquer mecanismo de criptografia em trânsito ou repouso.
* **D)** A privacidade por padrão aplica-se exclusivamente a jogos eletrônicos infantis, dispensando sua observância em sistemas governamentais ou portais do cidadão.
* **E)** O conceito determina que a documentação técnica do sistema seja destruída antes do deploy em ambiente de produção.

> **Comentário Detalhado:**
>
> - **A)** **Correta.** *Privacy by Default* (privacidade por padrão) estabelece que as configurações de fábrica e o comportamento padrão da aplicação devem ser automaticamente os mais estritos em proteção à privacidade (ex.: caixas de seleção desmarcadas, menor volume de coleta, tempo de retenção mínimo e compartilhamento restrito), sem que o titular precise alterar configurações manuais para se proteger.
> - **B)** Incorreta. Caixas pré-marcadas (*opt-out* compulsório) e abertura ampla de dados violam frontalmente o Privacy by Default.
> - **C)** Incorreta. A criptografia é uma das medidas essenciais recomendadas pelo Privacy by Design e by Default.
> - **D)** Incorreta. A regra aplica-se a qualquer aplicação e sistema de tratamento de dados pessoais, especialmente no setor público.
> - **E)** Incorreta. A documentação e rastreabilidade são fundamentais para o princípio da responsabilização e prestação de contas (*accountability*).
> 
> **Gabarito: A**
"""

q09 = """
---

### Questão 09 (FCC - Auditor Estadual de Controle Externo / TI - Adaptada)
**Enunciado:** A LGPD distingue formalmente os institutos da Anonimização e da Pseudonimização no ciclo de vida de desenvolvimento e análise de dados. Sob o ponto de vista criptográfico e de segurança da informação, assinale a afirmativa correta sobre a Pseudonimização:  

* **A)** O dado pseudonimizado é aquele que perdeu definitiva e irreversivelmente qualquer possibilidade de associação direta ou indireta a um indivíduo, deixando de ser considerado dado pessoal para todos os efeitos da LGPD.
* **B)** A pseudonimização é o tratamento por meio do qual um dado perde a possibilidade de associação, direta ou indireta, a um indivíduo, senão pelo uso de informação adicional mantida separadamente pelo controlador em ambiente seguro e controlado.
* **C)** A aplicação de algoritmo de hash MD5 simples sem *salt* em uma coluna de CPF garante a anonimização irreversível e absoluta da base de dados.
* **D)** Os dados pseudonimizados deixam de se sujeitar à LGPD, podendo ser vendidos livremente a empresas de telemarketing.
* **E)** A pseudonimização exige a destruição física dos discos rígidos e fitas de backup do data center a cada transação bancária.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Essa é a definição de dado **anonimizado** (Art. 12 da LGPD). O dado pseudonimizado continua sendo dado pessoal e sujeito integralmente à LGPD, pois pode ser reidentificado com a chave/informação adicional.
> - **B)** **Correta.** Definição legal do Art. 13, § 4º da LGPD: pseudonimização é o tratamento por meio do qual um dado perde a possibilidade de associação a um indivíduo, senão pelo uso de informação adicional mantida separadamente pelo controlador em ambiente seguro e controlado.
> - **C)** Incorreta. Hash sem *salt* em domínios finitos (como CPF) é vulnerável a ataques de tabela *rainbow* e quebra por força bruta trivial, não configurando anonimização robusta.
> - **D)** Incorreta. Dados pseudonimizados continuam sob o escopo pleno da LGPD e gozam de todas as garantias legais.
> - **E)** Incorreta. A pseudonimização é técnica criptográfica lógica (como tokenização e hashing com sal segregado), sem relação com destruição de hardware.
> 
> **Gabarito: B**
"""

q10 = """
---

### Questão 10 (FCC - Analista Judiciário - Segurança da Informação - Adaptada)
**Enunciado:** Em relação à gestão de riscos de privacidade e auditoria em sistemas públicos, a LGPD prevê o Relatório de Impacto à Proteção de Dados Pessoais (RIPD / DPIA). Acerca desse instrumento e das boas práticas de segurança, assinale a afirmativa correta:  

* **A)** O RIPD é um documento de preenchimento facultativo que deve ser mantido em segredo absoluto, sendo vedado à ANPD solicitar seu compartilhamento.
* **B)** O RIPD descreve os processos de tratamento de dados pessoais que podem gerar riscos às liberdades civis e aos direitos fundamentais, bem como medidas, salvaguardas e mecanismos de mitigação de risco adotados pela organização.
* **C)** A elaboração do RIPD exime o controlador de cumprir os princípios de segurança da informação e dispensa a comunicação de incidentes de segurança cibernética.
* **D)** O RIPD é obrigatório exclusivamente para operações que envolvam dados públicos abertos sem qualquer identificador pessoal.
* **E)** Compete privativamente ao estagiário de atendimento de suporte a emissão e homologação do RIPD, sendo dispensada a participação do Encarregado (DPO).

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A ANPD pode determinar a elaboração e apresentação do RIPD a qualquer tempo para operações de maior risco ou sensibilidade (Art. 38 da LGPD).
> - **B)** **Correta.** Conforme o Art. 5º, XVII e Art. 38 da LGPD, o RIPD é a documentação do controlador que contém a descrição dos processos de tratamento que podem gerar riscos às liberdades civis e aos direitos fundamentais, bem como medidas, salvaguardas e mecanismos de mitigação de risco.
> - **C)** Incorreta. O RIPD é uma ferramenta preventiva de conformidade; ele não afasta a obrigação contínua de segurança nem a obrigação de reportar incidentes relevantes à ANPD e aos titulares.
> - **D)** Incorreta. O RIPD foca justamente em operações que tratam dados pessoais com potencial de risco aos titulares (ex.: dados sensíveis, vigilância em massa, decisões automatizadas de IA).
> - **E)** Incorreta. A elaboração do RIPD envolve os gestores de negócio, arquitetos de TI, segurança da informação e conta com a orientação e parecer consultivo obrigatório do Encarregado (DPO).
> 
> **Gabarito: B**
"""

# Insertion 1: After Section 1.2
p1 = "> O Operador não toma decisões sobre as finalidades do tratamento. Se um provedor de nuvem contratado como Operador resolver utilizar os dados do órgão público para treinar seus próprios modelos comerciais de IA sem autorização, ele comete desvio de finalidade e passa a responder como **Controlador** em relação a esse tratamento ilícito.\n"
assert p1 in content, "Pattern 1 not found"
content = content.replace(p1, p1 + q06 + "\n")

# Insertion 2: After Section 2
p2 = "> No setor público (Art. 23), para desempenhar competências legais e executar políticas públicas, **não se exige consentimento** do titular. A FCC adora afirmar que órgãos de fiscalização precisam de autorização do cidadão auditado para processar seus dados cadastrais. **ERRADO!** O tratamento funda-se no cumprimento de obrigação legal (Art. 7º, II) e exercício regular de direitos (Art. 7º, VI).\n"
assert p2 in content, "Pattern 2 not found"
content = content.replace(p2, p2 + q07 + "\n")

# Insertion 3: After Section 3.2
p3 = '| **Exemplo Típico** | Armazenamento de dados pessoais em tabelas segregadas com criptografia em repouso e trilhas de log imutáveis. | Perfil público de novo usuário criado como "Privado" por padrão; geolocalização desativada inicialmente. |\n'
assert p3 in content, "Pattern 3 not found"
content = content.replace(p3, p3 + q08 + "\n")

# Insertion 4: After Section 4.1
p4 = "3. **Criptografia Reversível Preservadora de Formato (FPE - Format-Preserving Encryption):** Criptografa o dado mantendo o mesmo tamanho e tipo (ex.: CPF de 11 dígitos continua gerando uma string de 11 dígitos numéricos), viabilizando testes em sistemas legados sem quebrar restrições de esquema.\n"
assert p4 in content, "Pattern 4 not found"
content = content.replace(p4, p4 + q09 + "\n")

# Insertion 5: Before Section 6
target = "## 6. Fontes Recomendadas na Internet"
assert target in content, "target not found"
idx = content.find(target)
content = content[:idx] + q10.strip() + "\n\n---\n\n" + content[idx:]

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("File 13_01 successfully updated!")
