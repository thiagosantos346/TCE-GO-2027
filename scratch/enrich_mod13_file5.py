import os

file_path = "fontes_de_estudo/conhecimentos_especificos_b02_ti/13_legislacao_aplicada_a_ti/05_normativos_e_planejamento_de_ti_tce_go.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

q06 = """
---

### Questão 06 (FCC – Inédita – Padrão TCE-GO - Auditor Estadual de Controle Externo / TI)
**Enunciado:** O Comitê Estratégico de Tecnologia da Informação (CETI) do Tribunal de Contas do Estado de Goiás, instituído pela Resolução Normativa nº 13/2016, é a instância máxima colegiada de governança de TI. Acerca da composição e das competências privativas do CETI, assinale a afirmativa correta:  

* **A)** O CETI é composto exclusivamente por técnicos terceirizados contratados por empresas de suporte, sendo vedada a presença de membros da alta cúpula do Tribunal.
* **B)** Compete ao CETI aprovar formalmente o Plano Diretor de TI (PDTI) e suas revisões periódicas, além de estabelecer a priorização dos projetos e contratações de TIC de grande vulto e apreciar a Política de Segurança da Informação.
* **C)** O CETI tem como atribuição cotidiana o atendimento de chamados de formatação de computadores e a troca de toners de impressoras das secretarias.
* **D)** As decisões deliberadas pelo CETI têm caráter meramente folclórico e não vinculam o planejamento ou a execução orçamentária de tecnologia do Tribunal.
* **E)** O Presidente do Comitê é escolhido por sorteio público entre os jurisdicionados municipais fiscalizados pelo Tribunal de Contas.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O CETI é formado pela alta administração do TCE-GO: Conselheiro-Presidente (ou Conselheiro designado), Diretor-Geral, Secretários-Gerais (Controle Externo e Administração) e o Diretor de TI como relator técnico.
> - **B)** **Correta.** A Resolução Normativa nº 13/2016 confere ao CETI competência deliberativa estratégica: aprovar o PDTI, apreciar a PSI, priorizar grandes projetos e investimentos de TIC, monitorar indicadores de desempenho semestrais e dirimir conflitos institucionais de demandas.
> - **C)** Incorreta. Atividades operacionais de suporte de microinformática pertencem à Gerência de Atendimento e Suporte ao Usuário (DTI), e não à governança do CETI.
> - **D)** Incorreta. As deliberações do CETI possuem força normativa interna vinculante sobre os rumos de TIC no Tribunal.
> - **E)** Incorreta. A presidência do CETI é exercida por membro nato da alta direção do TCE-GO.
> 
> **Gabarito: B**
"""

q07 = """
---

### Questão 07 (FCC – Inédita – Padrão TCE-GO - Analista de Controle Externo / Governança)
**Enunciado:** A Resolução Administrativa nº 14/2024 estabeleceu a Política de Governança Organizacional do Tribunal de Contas do Estado de Goiás, adotando referenciais internacionais de controle e o consagrado Modelo das Três Linhas. No que se refere à estrutura de responsabilidades do Modelo das Três Linhas aplicado à gestão e controle no TCE-GO, assinale a afirmativa correta:  

* **A)** A 1ª Linha é exercida pela Auditoria Interna, sendo a única responsável por aplicar penalidades aos jurisdicionados municipais.
* **B)** A 2ª Linha é composta pelos fornecedores privados contratados, que fiscalizam os auditores fiscais concursados do Tribunal.
* **C)** A 1ª Linha é composta pelos gestores operacionais responsáveis pela entrega direta dos serviços e controles primários; a 2ª Linha atua no suporte, conformidade e gestão de riscos; e a 3ª Linha (Auditoria Interna) fornece avaliação objetiva e independente da eficácia dos controles e da governança.
* **D)** O Modelo das Três Linhas extinguiu qualquer dever de prestação de contas (*accountability*) da Diretoria de TI perante o Plenário do Tribunal.
* **E)** As três linhas operam em subordinação hierárquica direta à empresa vencedora da licitação de outsourcing de informática.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A Auditoria Interna ocupa privativamente a 3ª Linha (avaliação independente).
> - **B)** Incorreta. A 2ª Linha é interna ao Tribunal (unidades de integridade, conformidade e gestão de riscos).
> - **C)** **Correta.** Síntese exata do Modelo das Três Linhas do IIA (*Institute of Internal Auditors*) acolhido pela RA nº 14/2024: 1ª Linha (gestão operacional e controles diretos nas unidades executoras); 2ª Linha (monitoramento metodológico de conformidade, riscos e integridade); e 3ª Linha (auditoria interna independente).
> - **D)** Incorreta. A prestação de contas (*accountability*) é pilar estruturante e permanente da governança pública do Tribunal.
> - **E)** Incorreta. O modelo governa a estrutura institucional pública interna do Tribunal, sem subordinação a empresas privadas terceirizadas.
> 
> **Gabarito: C**
"""

q08 = """
---

### Questão 08 (FCC – Inédita – Padrão TCE-GO - Analista de TI / Governança e Planejamento)
**Enunciado:** A Resolução Administrativa nº 14/2025 disciplinou a estrutura organizacional e as atribuições privativas da Diretoria de Tecnologia da Informação (DTI) do TCE-GO. Em face do princípio da segregação entre governança e gestão, assinale a opção que descreve uma atribuição genuinamente executiva da DTI:  

* **A)** Homologar em plenário as contas anuais prestadas pelo Governador do Estado de Goiás.
* **B)** Deliberar de forma autônoma sobre a extinção de cargos efetivos do quadro de controle externo do Tribunal.
* **C)** Planejar, gerenciar, executar e manter as soluções tecnológicas corporativas, elaborar Estudos Técnicos Preliminares (ETP) e Termos de Referência (TR) para aquisições de TIC e subsidiar tecnicamente o CETI.
* **D)** Substituir a Assembleia Legislativa do Estado na votação da Lei Orçamentária Anual.
* **E)** Julgar os recursos de apelação cível interpostos pelos contribuintes do ICMS perante o Tribunal de Justiça.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A emissão de parecer prévio sobre as contas do Governador é competência privativa do Plenário do TCE-GO.
> - **B)** Incorreta. Matéria reservada a processo legislativo de iniciativa privativa do Presidente do Tribunal.
> - **C)** **Correta.** A DTI exerce a gestão executiva técnica (nível tático-operacional): elabora os artefatos de planejamento de compras (ETP/TR), gerencia o ciclo de vida dos softwares, opera data centers e redes, e atua como braço técnico de suporte ao CETI.
> - **D)** Incorreta. Votação de leis é atribuição privativa do Poder Legislativo.
> - **E)** Incorreta. Matéria jurisdicional afeta ao Tribunal de Justiça de Goiás.
> 
> **Gabarito: C**
"""

q09 = """
---

### Questão 09 (FCC – Inédita – Padrão TCE-GO - Técnico de Controle Externo / TI)
**Enunciado:** De acordo com a Resolução Administrativa nº 14/2025 do TCE-GO, a Diretoria de Tecnologia da Informação (DTI) organiza suas competências funcionais em unidades gerenciais vinculadas. Assinale a alternativa que correlaciona corretamente a gerência às suas respectivas atribuições regulamentares:  

* **A)** Gerência de Infraestrutura e Redes: encarregada da gestão de RH e concessão de aposentadorias de servidores.
* **B)** Gerência de Atendimento e Suporte ao Usuário (*Service Desk*): atua como Ponto Único de Contato (SPOC) para atendimento a incidentes, requisições de serviço de TI e microinformática.
* **C)** Gerência de Banco de Dados e Informações Estratégicas: responsável privativa pela aquisição de veículos automotores e controle da frota do Tribunal.
* **D)** Gerência de Sistemas de Informação: responsável pela limpeza predial e segurança patrimonial armada do edifício-sede.
* **E)** Núcleo de Segurança da Informação: encarregado de proibir que o Tribunal utilize computadores em suas rotinas de trabalho.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Recursos humanos e previdência competem à Secretaria-Geral de Administração.
> - **B)** **Correta.** A Gerência de Atendimento e Suporte ao Usuário (Service Desk) constitui o SPOC (*Single Point of Contact*) da TI do TCE-GO, acolhendo incidentes de Nível 1 e 2, gerindo ativos de microinformática e provendo suporte técnico aos usuários internos e externos.
> - **C)** Incorreta. Gestão de frota é competência de serviços gerais administrativos. A Gerência de Dados cuida de SGBDs, Data Lake e IA (IAGO).
> - **D)** Incorreta. Sistemas de Informação cuida de desenvolvimento, arquitetura de microsserviços e sustentação de código-fonte.
> - **E)** Incorreta. O Núcleo de Segurança cuida da gestão de vulnerabilidades, conformidade com a PSI e monitoramento de SOC.
> 
> **Gabarito: B**
"""

q10 = """
---

### Questão 10 (FCC – Inédita – Padrão TCE-GO - Auditor Estadual de Controle Externo / TI)
**Enunciado:** O Plano Diretor de TI (PDTI 2025–2026), aprovado pela Ordem de Serviço nº 001/2025-CETI, estruturou suas metas táticas a partir de um rigoroso Diagnóstico Estratégico fundamentado na Matriz SWOT. No contexto desse planejamento, assinale a afirmativa que apresenta uma Ameaça (*Threat*) externa e uma Oportunidade (*Opportunity*) externa identificadas para o ecossistema tecnológico do TCE-GO:  

* **A)** Ameaça: sofisticação crescente de ataques cibernéticos globais (*ransomware*) e forte concorrência do mercado privado na retenção de talentos de TIC; Oportunidade: expansão do uso de inteligência artificial preditiva no controle de despesas e adoção de soluções de nuvem híbrida elástica.
* **B)** Ameaça: posse de servidores concursados de alta qualificação técnica no órgão; Oportunidade: obsolescência forçada de todos os bancos de dados relacionais.
* **C)** Ameaça: realização de sessões plenárias ao vivo pela internet; Oportunidade: proibição do uso de fibra óptica em órgãos públicos goianos.
* **D)** Ameaça: aprovação da Lei Geral de Proteção de Dados Pessoais; Oportunidade: corte total do orçamento de TIC do Tribunal.
* **E)** Ameaça: extinção de todas as ameaças cibernéticas no mundo digital; Oportunidade: retorno definitivo aos processos judiciais em papel carbono.

> **Comentário Detalhado:**
>
> - **A)** **Correta.** A matriz SWOT do PDTI 2025–2026 identifica como Ameaças externas a proliferação de ataques cibernéticos sofisticados (*ransomware*) e a alta demanda e remuneração da iniciativa privada que dificulta a atração/retenção de talentos de TI. Como Oportunidades externas, aponta a revolução da IA (potencializada pela LC 205/2025) para auditorias contínuas massivas e a escalabilidade da nuvem híbrida.
> - **B)** Incorreta. Corpo técnico qualificado é Força (*Strength* interna), não Ameaça.
> - **C)** Incorreta. Transmissão de sessões é prática de transparência consolidada.
> - **D)** Incorreta. Redução orçamentária seria ameaça grave, jamais oportunidade.
> - **E)** Incorreta. Afirmativa sem qualquer nexo com a realidade tecnológica do controle externo.
> 
> **Gabarito: A**
"""

# Insertions:
# 1. After Section 1.2 item 5 (line ~135)
p1 = "5. **Resolução de Conflitos:** Dirimir impasses sobre demandas concorrentes entre a área de controle externo e a área administrativa.\n"
assert p1 in content, "Pattern 1 not found"
content = content.replace(p1, p1 + q06 + "\n")

# 2. After Section 2 item 3 (line ~150)
p2 = "3. **Conexão com a TIC:** A Governança de TI não é uma ilha isolada; os objetivos tecnológicos do PDTI são derivados diretamente dos objetivos estratégicos da RA nº 14/2024 para maximizar o valor público entregue pelo Tribunal à sociedade goiana.\n"
assert p2 in content, "Pattern 2 not found"
content = content.replace(p2, p2 + q07 + "\n")

# 3. After Section 4.1 bullet 5 (line ~255)
p3 = "- Garantir a alta disponibilidade da infraestrutura de servidores, data centers, redes e serviços em nuvem.\n"
assert p3 in content, "Pattern 3 not found"
content = content.replace(p3, p3 + q08 + "\n")

# 4. After Section 4.2 item 5 (line ~265)
p4 = "5. **Núcleo de Segurança da Informação e Conformidade:** Gestão contínua de vulnerabilidades, monitoramento de SOC (*Security Operations Center*), auditoria de logs e conformidade com a PSI e a LGPD.\n"
assert p4 in content, "Pattern 4 not found"
content = content.replace(p4, p4 + q09 + "\n")

# 5. After Section 5.1 bullet 4 (line ~291)
p5 = "- **Ameaças (Threats):** Sofisticação crescente de ataques cibernéticos globais (*ransomware*); retenção de talentos técnicos em face da concorrência do mercado privado global.\n"
assert p5 in content, "Pattern 5 not found"
content = content.replace(p5, p5 + q10 + "\n")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("File 13_05 successfully updated!")
