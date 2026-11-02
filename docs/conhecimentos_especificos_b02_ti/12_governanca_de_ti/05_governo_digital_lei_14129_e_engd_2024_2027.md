# 05 - Governo Digital e a ENGD 2024–2027 (Decreto 12.069/2024)

> **Matéria:** Governança de Tecnologia da Informação  
> **Cargo:** B02 – Técnico de Controle Externo – Especialidade: Tecnologia da Informação  
> **Arquivo:** `05_governo_digital_lei_14129_e_engd_2024_2027.md`  
> **Atos Normativos Centrais:** Lei Federal nº 14.129, de 29 de março de 2021 (Lei do Governo Digital) e Decreto Federal nº 12.069, de 21 de junho de 2024 (Estratégia Nacional de Governo Digital – ENGD 2024–2027)

---

## 📌 Ementa / Itens do Edital
- Transformação digital, inovação e modernização administrativa no setor público
- Lei Federal nº 14.129/2021 (Lei do Governo Digital):
    - Princípios, diretrizes e instrumentos fundamentais
    - Princípio do "Digital por Padrão" (*Digital by Default*) e a vedação à exigência de documentos já existentes no Estado (*Once-Only Principle*)
    - Níveis de identificação e autenticação digital (Plataforma GOV.BR: Bronze, Prata e Ouro)
    - Tipos de assinatura eletrônica no setor público: Simples, Avançada e Qualificada (Lei 14.063/2020)
    - Governo Como Plataforma (*Government as a Platform* - GaaP) e Interoperabilidade de Dados
- Estratégia Nacional de Governo Digital – ENGD 2024–2027 (Decreto Federal nº 12.069/2024):
    - Visão estratégica, objetivos e princípios orientadores
    - Os 5 Eixos Estratégicos e diretrizes para a transformação federativa (União, Estados e Municípios)
    - Serviços Públicos Proativos e Infraestrutura Pública Digital (DPI)

---

## 🧭 Sumário

1. [A Lei do Governo Digital (Lei Federal nº 14.129/2021)](#1-a-lei-do-governo-digital-lei-federal-no-141292021)
1. [Âmbito de Aplicação Universal](#1-1-ambito-de-aplicacao-universal)
    1. [Teste 505](#Teste-505)
1. [Princípios e Diretrizes Marcantes](#1-2-principios-e-diretrizes-marcantes)
    1. [Teste 506](#Teste-506)
    2. [Teste 507](#Teste-507)
1. [Níveis de Autenticação na Plataforma GOV.BR (Bronze, Prata e Ouro)](#1-3-niveis-de-autenticacao-na-plataforma-govbr-bronze-prata-e-ouro)
    1. [Teste 508](#Teste-508)
1. [Classificação das Assinaturas Eletrônicas no Setor Público (Lei nº 14.063/2020)](#1-4-classificacao-das-assinaturas-eletronicas-no-setor-publico-lei-no-140632020)
    1. [Teste 509](#Teste-509)
1. [Governo Como Plataforma (GaaP) e Interoperabilidade](#1-5-governo-como-plataforma-gaap-e-interoperabilidade)
    1. [Teste 510](#Teste-510)
2. [A Estratégia Nacional de Governo Digital – ENGD 2024–2027 (Decreto nº 12.069/2024)](#2-a-estrategia-nacional-de-governo-digital-engd-20242027-decreto-no-120692024)
2. [Propósito e Abrangência Federativa](#2-1-proposito-e-abrangencia-federativa)
    1. [Teste 511](#Teste-511)
2. [Os 5 Eixos Estratégicos da ENGD 2024–2027](#2-2-os-5-eixos-estrategicos-da-engd-20242027)
    1. [Teste 512](#Teste-512)
    2. [Teste 513](#Teste-513)
2. [Serviços Públicos Proativos e Infraestrutura Pública Digital (DPI)](#2-3-servicos-publicos-proativos-e-infraestrutura-publica-digital-dpi)
    1. [Teste 514](#Teste-514)
6. [Fontes Recomendadas na Internet](#6-fontes-recomendadas-na-internet)

---

## 1. A Lei do Governo Digital (Lei Federal nº 14.129/2021)

A **Lei nº 14.129/2021** instituiu o marco regulatório para a prestação digital dos serviços públicos no Brasil, fixando princípios, regras e instrumentos para o aumento da eficiência pública e a desburocratização das relações entre o Estado e a sociedade.

---

## 1.1 Âmbito de Aplicação Universal

A Lei do Governo Digital aplica-se obrigatoriamente a todos os entes e Poderes da Federação:

1. À administração direta e indireta da **União, dos Estados, do Distrito Federal e dos Municípios**.
2. Aos Poderes **Executivo, Judiciário e Legislativo** (abrangendo expressamente os **Tribunais de Contas** e o Ministério Público).
3. Às empresas públicas e sociedades de economia mista que prestem serviços públicos.

---

## 1.2 Princípios e Diretrizes Marcantes

#### 1. Vedação Expressa à Exigência de Documento em Posse do Estado (*Once-Only Principle*)
O Art. 5º, inciso VI e o Art. 12 da Lei nº 14.129/2021 consagram expressamente a **vedação de exigir do cidadão informações, documentos ou certidões que já constem na posse da própria Administração Pública**:

- O órgão público não pode transferir para o usuário o ônus de buscar uma certidão emitida por outro órgão do mesmo ente ou da administração governamental.
- Os órgãos públicos são obrigados a estruturar mecanismos de **interoperabilidade de dados** para consultar diretamente as bases cadastrais governamentais.

> 🚨 **ALERTA DE PROVA / PEGADINHA FCC:**  
> A FCC adora cobrar a regra: Se o cidadão solicita um serviço em uma Secretaria Estadual, o órgão **não pode** exigir certidão de regularidade fiscal emitida pela própria Fazenda Estadual ou certidão de nascimento civil emitida pelo Estado; o órgão deve consumir esses dados eletronicamente via barramento de interoperabilidade.

---

## 1.3 Níveis de Autenticação na Plataforma GOV.BR (Bronze, Prata e Ouro)

O ecossistema GOV.BR classifica as contas de identificação dos cidadãos em **três níveis progressivos de confiabilidade cadastral**:

```mermaid
flowchart TD
    B["NÍVEL BRONZE (Básico)<br/>Cadastro online simples via INSS / Receita Federal"] --> P["NÍVEL PRATA (Intermediário)<br/>Biometria facial da CNH ou login bancário Open Finance"]
    P --> O["NÍVEL OURO (Avançado)<br/>Biometria Facial do TSE (CIN) ou Certificado Digital ICP-Brasil"]
```

| Nível da Conta | Métodos de Validação / Obtenção | Serviços Públicos Acessíveis |
| :---: | :--- | :--- |
| **Bronze** | Cadastro presencial simplificado ou validação de dados cadastrais básicos junto à base do INSS ou da Receita Federal (perguntas cadastrais simples). | Acesso a serviços digitais básicos de baixo risco e consultas cadastrais simples. |
| **Prata** | Validação biométrica facial contra a base da CNH (Senatran); login por meio de credenciais bancárias (Open Finance / Bancos Credenciados); ou validação via SIGEPE (servidores públicos). | Acesso à grande maioria dos serviços públicos digitais federais e estaduais, emissão de certidões e uso de assinatura eletrônica avançada. |
| **Ouro** | Validação biométrica facial na base da Justiça Eleitoral (TSE / Carteira de Identidade Nacional - CIN); ou validação por Certificado Digital padrão ICP-Brasil (A1 ou A3). | Nível máximo de segurança: acesso irrestrito a todos os serviços críticos, sigilosos, declaração pré-preenchida do Imposto de Renda e assinaturas eletrônicas. |

---

## 1.4 Classificação das Assinaturas Eletrônicas no Setor Público (Lei nº 14.063/2020)

A Lei nº 14.063/2020 padronizou os tipos de assinatura eletrônica no relacionamento com órgãos públicos em três modalidades:

```mermaid
flowchart LR
    S["1. Assinatura Eletrônica SIMPLES<br/>(Login básico, SMS, confirmação por e-mail)"] 
    A["2. Assinatura Eletrônica AVANÇADA<br/>(GOV.BR Prata/Ouro - Associação unívoca e integridade)"]
    Q["3. Assinatura Eletrônica QUALIFICADA<br/>(Exclusiva de Certificado Digital ICP-Brasil)"]
    
    S --> A --> Q
```

#### Tabela Comparativa: Assinaturas Eletrônicas na Administração Pública

| Categoria | Requisitos Técnicos de Segurança | Hipóteses de Aplicação Típicas |
| :--- | :--- | :--- |
| **Simples** | Permite identificar o signatário e anexa dados eletrônicos a outros dados (ex.: código SMS, confirmação de link por e-mail, login com senha comum). | Interações de baixo impacto financeiro ou operacional: agendamento de atendimentos, requerimentos de informações gerais, ouvidoria. |
| **Avançada** | Está associada unicamente ao signatário; dados para criação sob seu controle exclusivo; detecta qualquer alteração posterior no documento. Produzida tipicamente pelas contas **GOV.BR Prata e Ouro**. | Processos administrativos regulares, termos de posse, contratos administrativos ordinários, manifestações processuais em Tribunais de Contas e órgãos fiscais. |
| **Qualificada** | Utiliza **certificado digital emitido por Autoridade Certificadora credenciada na Infraestrutura de Chaves Públicas Brasileira (ICP-Brasil)**. É o nível mais alto. | Atos normativos de chefes de Poder (Presidente, Governadores, Prefeitos); transferência e registro de imóveis públicos; atos que impliquem sigilo fiscal/bancário gravíssimo onde a lei exigir expressamente. |

> 🚨 **ALERTA DE PROVA / PEGADINHA FCC:**  
> A FCC adora afirmar que qualquer manifestação ou processo eletrônico em órgão público "exige compulsoriamente a assinatura qualificada com certificado ICP-Brasil". **FALSO!** A legislação autorizou amplamente o uso da **Assinatura Eletrônica Avançada** (como a provida pelo GOV.BR Prata e Ouro) para a esmagadora maioria dos atos e processos administrativos cotidianos.

---

## 1.5 Governo Como Plataforma (GaaP) e Interoperabilidade

O paradigma de **Governo Como Plataforma** (*Government as a Platform - GaaP*) redefine o papel da tecnologia pública. Em vez de construir aplicações verticais monolíticas isoladas para cada órgão, o governo desenvolve blocos compartilhados de infraestrutura tecnológica aberta:

- Criação de APIs padronizadas e barramentos centrais (como a plataforma **ConectaGov** no Brasil);
- Disponibilização de serviços públicos digitais interoperáveis que conversam em tempo real;
- Racionalização de custos de TIC e eliminação de duplicação de dados entre a União, Estados e Municípios.

---

## 2. A Estratégia Nacional de Governo Digital – ENGD 2024–2027 (Decreto nº 12.069/2024)

O **Decreto Federal nº 12.069, de 21 de junho de 2024**, promulgou a nova **Estratégia Nacional de Governo Digital (ENGD)** para o quadriênio **2024 a 2027**.

---

## 2.1 Propósito e Abrangência Federativa

A ENGD 2024–2027 é uma política pública de **amplitude nacional federativa**, coordenada para articular a transformação digital integrada de todos os entes federativos (União, 26 Estados, DF e Municípios), promovendo a interoperabilidade e reduzindo disparidades regionais de infraestrutura e capacidade de atendimento digital.

---

## 2.2 Os 5 Eixos Estratégicos da ENGD 2024–2027

```mermaid
flowchart TD
    ENGD["ESTRATÉGIA NACIONAL DE GOVERNO DIGITAL 2024–2027<br/>(Decreto nº 12.069/2024)"]
    
    E1["Eixo 1: Governo Integrado e Eficiente<br/>Interoperabilidade federativa, ConectaGov e redução de redundâncias"]
    E2["Eixo 2: Governo Confiável e Seguro<br/>Segurança cibernética, conformidade com a LGPD e privacidade"]
    E3["Eixo 3: Governo Aberto e Transparente<br/>Abertura de dados, controle social e integridade"]
    E4["Eixo 4: Governo Inteligente e Inovador<br/>Uso ético de Inteligência Artificial e políticas orientadas por dados"]
    E5["Eixo 5: Governo Inclusivo e Centrado nas Pessoas<br/>Acessibilidade, linguagem simples, multicanalidade e Serviços Proativos"]
    
    ENGD --> E1
    ENGD --> E2
    ENGD --> E3
    ENGD --> E4
    ENGD --> E5
```

1. **Eixo 1 - Governo Integrado e Eficiente:** Fortalecimento da interoperabilidade federativa via ConectaGov, racionalização de custos de TIC e eliminação de cadastros redundantes.
2. **Eixo 2 - Governo Confiável e Seguro:** Resiliência cibernética de infraestruturas críticas, proteção de dados pessoais (LGPD) e segurança da informação governamental.
3. **Eixo 3 - Governo Aberto e Transparente:** Fomento à transparência ativa, ampliação do catálogo de dados abertos para pesquisa e controle social, e integridade pública.
4. **Eixo 4 - Governo Inteligente e Inovador:** Adoção ética e responsável de Inteligência Artificial (IA) e formulação de políticas públicas orientadas por evidências empíricas (*data-driven policy*).
5. **Eixo 5 - Governo Inclusivo e Centrado nas Pessoas:** Inclusão digital ampla, design universal, linguagem simples, multicanalidade e adoção do modelo de **Serviços Públicos Proativos**.

---

## 2.3 Serviços Públicos Proativos e Infraestrutura Pública Digital (DPI)

#### 1. Serviços Públicos Proativos
Consiste na mudança de paradigma do atendimento público:

- *Modelo Reativo Tradicional:* O cidadão descobre a existência do direito, preenche formulários, reúne certidões e protocola requerimento no órgão.
- *Modelo Proativo da ENGD:* O Estado cruza dados de suas bases interoperáveis, reconhece automaticamente que o cidadão preencheu os requisitos previstos em lei e **disponibiliza ou concede ativamente o serviço/benefício**, notificando o indivíduo de forma transparente, sem necessidade de provocação prévia.

#### 2. Infraestrutura Pública Digital (DPI - *Digital Public Infrastructure*)
A ENGD 2024–2027 estrutura a evolução digital do país em três pilares fundamentais:

1. **Identificação Digital Unificada:** Acesso único por meio do CPF e da plataforma GOV.BR.
2. **Sistema de Pagamentos Instantâneos:** Utilização do Pix e da plataforma PagTesouro para recebimento ágil de taxas e repasses sociais diretos.
3. **Barramento Seguro de Dados:** Troca segura de informações via APIs e ConectaGov, com rastreabilidade e controle estrito de acessos.

---

## 6. Fontes Recomendadas na Internet

* [Lei nº 14.129/2021 (Lei do Governo Digital)](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14129.htm) - Texto oficial que estabelece princípios, regras e instrumentos para o aumento da eficiência pública e desburocratização.
* [Decreto nº 12.198/2024 (Estratégia Nacional de Governo Digital)](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2024/decreto/d12198.htm) - Institui a Estratégia Nacional de Governo Digital para o ciclo 2024-2027.
* [Governo Digital - Estratégia Nacional de Governo Digital (ENGD)](https://www.gov.br/governodigital/pt-br/estrategias-e-governanca-digital/estrategianacional) - Pilares, metas e indicadores da transformação digital dos serviços públicos brasileiros.
* [Governo Digital - Estratégia Federal de Governo Digital (EFGD)](https://www.gov.br/governodigital/pt-br/estrategias-e-governanca-digital/EFGD) - Diretrizes estratégicas para interoperabilidade, dados abertos e serviços centrados no cidadão.
* [Governo Digital - Infraestrutura Nacional de Dados (IND)](https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados) - Governança, compartilhamento e segurança de bases de dados do setor público.
* DI PIETRO, Maria Sylvia Zanella. **Direito Administrativo**. 37. ed. Rio de Janeiro: Forense, 2024. (Cap. 3 - Princípios da Administração Pública e Eficiência Digital).
* NOHARA, Irene Patrícia. **Direito Administrativo**. 13. ed. São Paulo: Atlas, 2023. (Cap. 2 - A Transformação Digital da Administração Pública e a Lei 14.129/2021).
* BRESSER-PEREIRA, Luiz Carlos. **Reforma do Estado para a Cidadania: a Reforma Gerencial Brasileira na Perspectiva Internacional**. São Paulo: Editora 34, 1998. (Cap. 4 - Transparência, Governança e Serviços Públicos).
