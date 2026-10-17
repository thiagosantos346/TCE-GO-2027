import os

file_path = "fontes_de_estudo/conhecimentos_especificos_b02_ti/13_legislacao_aplicada_a_ti/03_seguranca_em_contratacoes_e_certificacao_digital.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

q06 = """
---

### Questão 06 (FCC - Auditor de Controle Externo / TI - Adaptada)
**Enunciado:** O planejamento de contratações de TIC na Administração Pública exige a incorporação de requisitos de segurança da informação desde os primeiros estudos preliminares, em consonância com a Lei nº 14.133/2021 e a norma ABNT NBR ISO/IEC 27001. A respeito da segurança da informação na fase preparatória, assinale a afirmativa correta:  

* **A)** A definição de requisitos de segurança cibernética deve ocorrer exclusivamente após a homologação final do software em produção, vedada a inserção de exigências no Estudo Técnico Preliminar (ETP).
* **B)** O Mapa de Gerenciamento de Riscos deve contemplar ameaças de vazamento de dados pessoais, indisponibilidade de serviços essenciais e estratégias para evitar o aprisionamento tecnológico (*vendor lock-in*).
* **C)** É obrigatório que o órgão público dispense a exigência de testes estáticos (SAST) e dinâmicos (DAST) de vulnerabilidades para desonerar financeiramente a licitante vencedora.
* **D)** A Política de Segurança da Informação (PSI) do órgão contratante não possui força cogente para balizar as cláusulas do Termo de Referência de TIC.
* **E)** Requisitos de soberania e residência de dados em território nacional para sistemas críticos são ilegais por violarem a liberdade de mercado das multinacionais de nuvem.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Segurança é um requisito não funcional estruturante que deve ser mapeado desde a concepção inicial no ETP (*Security by Design*).
> - **B)** **Correta.** O gerenciamento de riscos na fase de planejamento de TIC identifica proativamente ameaças à integridade, confidencialidade e disponibilidade, inclusive riscos de perda de controle dos dados e aprisionamento tecnológico (*vendor lock-in*), estabelecendo salvaguardas contratuais.
> - **C)** Incorreta. A exigência de varreduras SAST/DAST e correção de vulnerabilidades sem ônus adicional é boa prática mandatória de fiscalização técnica.
> - **D)** Incorreta. A contratação de TIC deve estar estritamente alinhada à PSI institucional.
> - **E)** Incorreta. A exigência de residência e soberania de dados para informações estatais estratégicas é plenamente respaldada pela legislação nacional de segurança cibernética.
> 
> **Gabarito: B**
"""

q07 = """
---

### Questão 07 (FCC - Analista Judiciário - Tecnologia da Informação - Adaptada)
**Enunciado:** A Infraestrutura de Chaves Públicas Brasileira (ICP-Brasil), instituída pela MP nº 2.200-2/2001, é estruturada de forma hierárquica. Acerca dos atores e papéis que compõem a ICP-Brasil, assinale a afirmativa correta:  

* **A)** A Autoridade Certificadora Raiz (AC-Raiz) da ICP-Brasil é operada privativamente pelo Instituto Nacional de Tecnologia da Informação (ITI).
* **B)** As Autoridades de Registro (ARs) têm como competência exclusiva a emissão e a assinatura de certificados digitais de primeiro nível na cadeia de confiança.
* **C)** O Comitê Gestor da ICP-Brasil é um órgão composto unicamente por empresas multinacionais de software sem qualquer participação do Estado brasileiro.
* **D)** As Autoridades de Carimbo do Tempo (ACTs) são proibidas de sincronizar seus relógios com a hora legal brasileira do Observatório Nacional.
* **E)** Qualquer pessoa física pode atuar autonomamente como Autoridade Certificadora de primeiro nível sem necessidade de credenciamento perante o ITI.

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme a MP nº 2.200-2/2001, a AC-Raiz é operada pelo ITI (Instituto Nacional de Tecnologia da Informação), autarquia federal vinculada à Casa Civil da Presidência da República.
> - **B)** Incorreta. As Autoridades de Registro (AR) realizam a identificação presencial/biométrica e confirmação documental do titular, mas quem emite e assina criptograficamente o certificado é a Autoridade Certificadora (AC).
> - **C)** Incorreta. O Comitê Gestor da ICP-Brasil é instância colegiada pública que conta com representantes do governo federal, sociedade civil e setor acadêmico/empresarial.
> - **D)** Incorreta. As ACTs devem obrigatoriamente referenciar-se ao Padrão de Hora Legal Brasileira fornecido pelo Observatório Nacional (ON).
> - **E)** Incorreta. O credenciamento de ACs perante a AC-Raiz/ITI é obrigatório e envolve rigorosos requisitos de infraestrutura física, salas-cofre e auditorias de segurança.
> 
> **Gabarito: A**
"""

q08 = """
---

### Questão 08 (FCC - TRT-6 - Analista Judiciário - Tecnologia da Informação - Adaptada)
**Enunciado:** No tocante à validade jurídica das assinaturas e documentos eletrônicos sob a égide da Medida Provisória nº 2.200-2/2001, assinale a afirmativa correta:  

* **A)** Os documentos eletrônicos assinados digitalmente com o uso de certificados emitidos no âmbito da ICP-Brasil presumem-se verdadeiros em relação aos signatários, na forma do Código Civil.
* **B)** A MP nº 2.200-2/2001 declarou expressamente nulo qualquer documento assinado eletronicamente por meio que não utilize certificado digital da ICP-Brasil.
* **C)** O certificado digital da ICP-Brasil não possui prazo de validade temporal, permanecendo ativo de forma perpétua mesmo após o falecimento do signatário.
* **D)** A assinatura digitalICP-Brasil substitui a necessidade de conexão física de cabos de fibra óptica nas redes de computadores.
* **E)** É proibido utilizar criptografia assimétrica na composição de assinaturas digitais brasileiras.

> **Comentário Detalhado:**
>
> - **A)** **Correta.** O Art. 10, § 1º da MP 2.200-2/2001 estipula que as declarações constantes dos documentos em forma eletrônica produzidos com a utilização de processo de certificação disponibilizado pela ICP-Brasil presumem-se verdadeiros em relação aos signatários (*presunção de veracidade juris tantum*).
> - **B)** Incorreta. O Art. 10, § 2º autoriza explicitamente outros meios de comprovação de autoria e integridade eletrônica, desde que aceito pelas partes.
> - **C)** Incorreta. Todo certificado digital possui período de validade determinado (ex.: 1 a 3 anos), findo o qual expira e não pode mais ser utilizado para novas assinaturas válidas.
> - **D)** Incorreta. Certificação digital é mecanismo criptográfico lógico de segurança, sem relação com meios físicos de transmissão de dados.
> - **E)** Incorreta. A assinatura digital baseia-se fundamentalmente em criptografia assimétrica de chave pública e privada.
> 
> **Gabarito: A**
"""

q09 = """
---

### Questão 09 (FGV - TRT - Analista Judiciário - Tecnologia da Informação - Adaptada)
**Enunciado:** Analise as afirmativas a seguir sobre criptografia assimétrica, funções de resumo (*hash*) e assinaturas digitais aplicadas a sistemas de controle e processo eletrônico:  

I. A criptografia assimétrica opera com um par de chaves matematicamente correlacionadas: a chave pública (que pode ser amplamente distribuída) e a chave privada (que deve ser mantida em sigilo absoluto pelo titular).  
II. O processo de criação de uma assinatura digital envolve a aplicação de uma função *hash* criptográfica unidirecional sobre o documento original e a subsequente cifração do resumo gerado utilizando-se a chave privada do signatário.  
III. A assinatura digital tem a propriedade de garantir a confidencialidade do conteúdo do documento assinado, tornando-o ilegível para qualquer pessoa que não possua a chave privada do autor.  

Está correto o que se afirma em:  

* **A)** I, apenas.
* **B)** II, apenas.
* **C)** I e II, apenas.
* **D)** II e III, apenas.
* **E)** I, II e III.

> **Comentário Detalhado:**
>
> - **I.** **Correta.** Na criptografia assimétrica, utiliza-se um par de chaves: a privada (exclusiva do titular) e a pública (divulgada no certificado digital).
> - **II.** **Correta.** A assinatura digital é obtida calculando o resumo criptográfico do documento (*hash*) e cifrando esse resumo com a chave privada do signatário. O destinatário decifra o resumo com a chave pública do autor e compara com o *hash* recalculado, atestando autenticidade, integridade e não repúdio.
> - **III.** Incorreta. A assinatura digital garante **autenticidade, integridade e não repúdio**, mas **não garante a confidencialidade** (o documento pode ser lido normalmente em texto claro a menos que também seja cifrado separadamente).
> 
> **Gabarito: C**
"""

q10 = """
---

### Questão 10 (FCC - Tribunal de Contas - Auditor de TI - Adaptada)
**Enunciado:** Em sistemas de processo eletrônico e repositórios digitais confiáveis de Tribunais de Contas, a preservação e a comprovação probatória de documentos a longo prazo exigem a adoção de padrões técnicos avançados. Acerca do Carimbo do Tempo (*Time Stamping*) e das políticas de assinatura digital de longo prazo, assinale a afirmativa correta:  

* **A)** O Carimbo do Tempo emitido por uma Autoridade de Carimbo do Tempo (ACT) atesta com fé pública eletrônica a data e a hora exatas em que um documento foi assinado, assegurando a validade probatória mesmo após a expiração temporal do certificado digital do signatário.
* **B)** O Carimbo do Tempo consiste unicamente no relógio interno do sistema operacional do computador do usuário, dispensando conexão com servidores oficiais.
* **C)** Políticas de assinatura de longo prazo (como PAdES-LTV) são proibidas em órgãos de controle externo em razão de incompatibilidade com o formato PDF.
* **D)** A expiração natural de um certificado digital anula retroativamente e torna ilícitos todos os acórdãos e relatórios emitidos legitimamente durante sua vigência.
* **E)** O carimbo do tempo pode ser gerado manualmente pelo próprio advogado mediante alteração das propriedades do arquivo no explorador de arquivos do Windows.

> **Comentário Detalhado:**
>
> - **A)** **Correta.** O Carimbo do Tempo (adicionado em formatos como PAdES/CAdES) vincula criptograficamente o documento à hora legal oficial emitida por uma ACT credenciada. Ele comprova que a assinatura foi aposta antes de qualquer expiração ou revogação futura do certificado, viabilizando a validação de longo prazo (*Long Term Validation* - LTV).
> - **B)** Incorreta. O relógio local da máquina do usuário não tem confiabilidade nem fé pública, podendo ser facilmente manipulado.
> - **C)** Incorreta. PAdES (*PDF Advanced Electronic Signatures*) com LTV é o padrão internacional dominante para processos judiciais e de controle externo eletrônicos.
> - **D)** Incorreta. A expiração da chave não invalida documentos legitimamente assinados no passado quando a validade temporal puder ser atestada por carimbo de tempo ou registros confiáveis.
> - **E)** Incorreta. Carimbo do tempo é emitido por entidade credenciada (ACT) mediante requisição criptográfica estruturada (RFC 3161).
> 
> **Gabarito: A**
"""

# Insertions:
# 1. After Section 1.1 item 4 (line ~61)
p1 = "4. **Termo de Referência (TR):** Especifica objetivamente os requisitos técnicos, indicadores do Instrumento de Medição de Resultado (IMR), níveis mínimos de serviço e cláusulas resolutivas.\n"
assert p1 in content, "Pattern 1 not found"
content = content.replace(p1, p1 + q06 + "\n")

# 2. After Section 2.1 item 5 (line ~135)
p2 = "5. **Autoridade de Carimbo do Tempo (ACT):** Entidade credenciada responsável por atestar, com base na hora legal brasileira emitida pelo Observatório Nacional, que determinado documento eletrônico existia em uma data e horário exatos.\n"
assert p2 in content, "Pattern 2 not found"
content = content.replace(p2, p2 + q07 + "\n")

# 3. After Section 2.3 alert box (line ~177)
p3 = "> A MP 2.200-2/2001 **não** proibiu nem tornou nulas as assinaturas eletrônicas fora da ICP-Brasil! O Art. 10, § 2º autoriza explicitamente assinaturas não-ICP se aceitas pelos participantes, o que forneceu a base jurídica para as assinaturas Gov.br e sistemas corporativos.\n"
assert p3 in content, "Pattern 3 not found"
content = content.replace(p3, p3 + q08 + "\n")

# 4. After Section 3.1 table (line ~205)
p4 = "| **Qualificada** (Art. 3º, III) | É **obrigatoriamente** aquela gerada mediante o uso de certificado digital emitido pela **ICP-Brasil** (MP 2.200-2/2001). | Assinatura com token A3 ou arquivo A1 ICP-Brasil em acórdãos de Tribunais, decisões judiciais e emissão de notas fiscais. | - **Exigência mandatória restrita:**<br>1. Atos assinados por Chefes de Poder, Ministros e titulares de Poder;<br>2. Emissão de Notas Fiscais Eletrônicas (salvo MEI);<br>3. Transferência e registro de bens imóveis. |\n"
assert p4 in content, "Pattern 4 not found"
content = content.replace(p4, p4 + q09 + "\n")

# 5. Before Section 6. Fontes
target = "## 6. Fontes Recomendadas na Internet"
assert target in content, "target not found"
idx = content.find(target)
content = content[:idx] + q10.strip() + "\n\n---\n\n" + content[idx:]

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("File 13_03 successfully updated!")
