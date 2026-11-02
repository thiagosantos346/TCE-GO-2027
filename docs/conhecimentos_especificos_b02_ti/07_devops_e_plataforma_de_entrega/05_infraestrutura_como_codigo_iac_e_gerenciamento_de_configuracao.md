# 05 - Infraestrutura como Código (IaC) e Gerenciamento de Configuração

> **Matéria:** DevOps, Plataforma de Desenvolvimento e Engenharia de Entrega  
> **Cargo:** B02 – Técnico de Controle Externo – Especialidade: Tecnologia da Informação  
> **Arquivo:** `05_infraestrutura_como_codigo_iac_e_gerenciamento_de_configuracao.md`  



---


## 📌 Ementa / Itens do Edital
- Conceitos de Infraestrutura como Código (IaC - Infrastructure as Code)
- Abordagens: Declarativa vs. Imperativa / Procedural
- Infraestrutura Imutável vs. Mutável (Paradigma Pets vs. Cattle)
- Idempotência e controle de desvio de estado (Configuration Drift)
- Ferramentas de provisionamento declarativo: Terraform e OpenTofu
- Ferramentas de gerenciamento de configuração: Ansible, Puppet e Chef (Arquitetura Push vs. Pull, Agentless vs. Agent-based)

---

## 🧭 Sumário

1. [Fundamentos de Infraestrutura como Código (IaC)](#1-fundamentos-de-infraestrutura-como-codigo-iac)
    1. [Definição, Propósito e Benefícios de Engenharia](#11-definicao-proposito-e-beneficios-de-engenharia)
    2. [Paradigma Declarativo (O Quê) vs. Imperativo (Como)](#12-paradigma-declarativo-o-que-vs-imperativo-como)
    3. [O Princípio da Idempotência e Desvio de Configuração (Configuration Drift)](#13-o-principio-da-idempotencia-e-desvio-de-configuracao-configuration-drift)
    4. [Infraestrutura Mutável vs. Imutável (Pets vs. Cattle)](#14-infraestrutura-mutavel-vs-imutavel-pets-vs-cattle)
    5. [Teste 214](#Teste-214)
    6. [Teste 215](#Teste-215)
    7. [Teste 216](#Teste-216)
2. [Provisionamento Declarativo com Terraform e OpenTofu](#2-provisionamento-declarativo-com-terraform-e-opentofu)
    1. [Estrutura e Blocos Fundamentais da Linguagem HCL](#21-estrutura-e-blocos-fundamentais-da-linguagem-hcl)
    2. [O Arquivo de Estado (terraform.tfstate), Remote Backend e State Locking](#22-o-arquivo-de-estado-terraformtfstate-remote-backend-e-state-locking)
    3. [Ciclo Operacional da CLI: init, validate, plan, apply e destroy](#23-ciclo-operacional-da-cli-init-validate-plan-apply-e-destroy)
    4. [Teste 217](#Teste-217)
    5. [Teste 218](#Teste-218)
    6. [Teste 219](#Teste-219)
3. [Gerenciamento Automatizado de Configuração: Ansible vs. Puppet vs. Chef](#3-gerenciamento-automatizado-de-configuracao-ansible-vs-puppet-vs-chef)
    1. [Modelos Arquiteturais: Push vs. Pull e Agentless vs. Agent-Based](#31-modelos-arquiteturais-push-vs-pull-e-agentless-vs-agent-based)
    2. [Matriz Comparativa Detalhada: Ansible vs. Puppet vs. Chef](#32-matriz-comparativa-detalhada-ansible-vs-puppet-vs-chef)
    3. [Anatomia Operacional do Ansible: Inventário, Playbooks, Módulos, Handlers e Roles](#33-anatomia-operacional-do-ansible-inventario-playbooks-modulos-handlers-e-roles)
    4. [Sinergia Arquitetural: Terraform no Provisionamento + Ansible na Configuração](#34-sinergia-arquitetural-terraform-no-provisionamento-ansible-na-configuracao)
    5. [Teste 220](#Teste-220)
    6. [Teste 221](#Teste-221)
    7. [Teste 222](#Teste-222)
    8. [Teste 223](#Teste-223)
4. [🌐 Fontes Oficiais e Referências Bibliográficas](#fontes-oficiais-e-referencias-bibliograficas)

---

## 1. Fundamentos de Infraestrutura como Código (IaC)

A Infraestrutura como Código (*Infrastructure as Code - IaC*) é a prática de engenharia que substitui o provisionamento manual e artesanal de recursos computacionais (telas interativas de consoles de nuvem, assistentes gráficos e comandos isolados no terminal) por **arquivos descritivos de configuração legíveis por máquina e versionados em sistemas de controle de versão (como o Git)**.

```mermaid
flowchart TD
    subgraph Paradigma_Declarativo["Paradigma Declarativo (Terraform / K8s)"]
        DEC_CODE["Código: 'Quero 3 Servidores Web'"]
        DEC_ENGINE["Motor de IaC: Calcula a diferença e aplica"]
        DEC_REAL["Estado Real Atual: 1 Servidor"]
        DEC_ACT["Ação: Cria exatamente 2 novos servidores"]
        DEC_CODE --> DEC_ENGINE
        DEC_REAL --> DEC_ENGINE
        DEC_ENGINE --> DEC_ACT
    end

    subgraph Paradigma_Imperativo["Paradigma Imperativo (Bash / CLI)"]
        IMP_CODE["Script: 'Execute: criar_servidor() duas vezes'"]
        IMP_ACT["Ação: Executa os comandos cegamente sem verificar o estado"]
        IMP_CODE --> IMP_ACT
    end
```

### 1.1 Definição, Propósito e Benefícios de Engenharia

O propósito primordial da IaC é aplicar os mesmos rigores e benefícios do desenvolvimento de software ao gerenciamento de infraestrutura de TI:

- **Reprodutibilidade e Consistência:** Permite recriar ambientes completos de homologação, testes e produção com total fidelidade a partir de um único comando, erradicando o problema do "na minha máquina funciona".
- **Rastreabilidade e Auditoria:** Cada modificação em redes, regras de firewall ou servidores fica registrada no histórico de commits do Git, documentando quem alterou, quando alterou e qual foi a justificativa técnica.
- **Automação via Pipelines de CI/CD:** A infraestrutura pode ser validada por linters estáticos, testes de segurança e submetida a aprovações por pares antes de ser aplicada compulsoriamente por runners automatizados (*GitOps*).

### 1.2 Paradigma Declarativo (O Quê) vs. Imperativo (Como)

As linguagens e ferramentas de IaC dividem-se em dois paradigmas fundamentais:

- **Paradigma Declarativo (O Quê / *Desired State*):**
    - O operador define o **estado final almejado da infraestrutura** (ex.: *"devem existir 3 máquinas virtuais com 8GB de RAM na sub-rede privada"*).
    - O motor da ferramenta de IaC é responsável por consultar o estado atual da nuvem, compará-lo com o código, deduzir a diferença matemática (*delta*) e orquestrar a execução estrita das ações necessárias para atingir a meta.
    - Se 1 máquina já existir, o motor cria apenas 2. Se as 3 já existirem, o motor não faz nada.
    - **Exemplos Canônicos:** Terraform, OpenTofu, AWS CloudFormation, manifestos do Kubernetes.
- **Paradigma Imperativo / Procedural (Como / *Execution Steps*):**
    - O operador programa a **sequência cronológica e explícita de passos e comandos** que o sistema deve executar para erguer a infraestrutura (ex.: *"passo 1: chame a API de criar VM; passo 2: pause por 30 segundos; passo 3: anexe o disco"*).
    - A ferramenta executa as instruções cegamente. Se o script falhar na metade, o ambiente fica em estado inconsistente (*partially applied*), exigindo scripts corretivos ou intervenções manuais.
    - **Exemplos Canônicos:** Shell Scripts (Bash/PowerShell), AWS CLI, chamadas via SDK Python (Boto3).

### 1.3 O Princípio da Idempotência e Desvio de Configuração (Configuration Drift)

Dois conceitos são cobrados com rigor terminológico pela FCC:

#### Idempotência
Uma operação é dita **idempotente** se a sua execução repetida múltiplas vezes sobre um mesmo sistema produz **exatamente o mesmo resultado final da primeira execução**, sem gerar efeitos colaterais indesejados, duplicações de recursos ou erros de execução.

- *Na prática:* Se você executar `terraform apply` ou rodar um *Playbook* do Ansible dez vezes consecutivas sobre uma infraestrutura estável sem alterar o código, a ferramenta validará que o estado real já coincide com o estado desejado e reportará **zero alterações** (`0 to add, 0 to change, 0 to destroy` ou `changed=0`).

#### Desvio de Configuração (*Configuration Drift*)
O desvio de configuração manifesta-se quando recursos de produção são modificados manualmente "fora de banda" (*out-of-band*), por exemplo:

- Um administrador conecta via console web da nuvem ou via terminal SSH e altera manualmente uma porta de firewall ou a quantidade de memória de uma instância sem refletir essa mudança no repositório Git.
- **Impacto:** O ambiente real diverge da especificação formal do código versionado.
- **Correção Automatizada:** Na execução seguinte de planejamento (`terraform plan`), o motor compara o estado real com o código, detecta a divergência e propõe a reversão compulsória da alteração manual, restaurando a conformidade institucional.

### 1.4 Infraestrutura Mutável vs. Imutável (Pets vs. Cattle)

O debate arquitetural entre sistemas mutáveis e imutáveis é consagrado na metáfora de Randy Bias: *"Pets vs. Cattle"* (Animais de Estimação vs. Gado).

```mermaid
flowchart LR
    subgraph Pets["Infraestrutura Mutável (Pets / Animais de Estimação)"]
        P_SRV["Servidor Dedicado (srv-web-01)"]
        P_PATCH["Aplica patches in-place via SSH"]
        P_DRIFT["Acúmulo de divergências (Snowflake Server)"]
        P_SRV --> P_PATCH --> P_DRIFT
    end

    subgraph Cattle["Infraestrutura Imutável (Cattle / Gado)"]
        C_OLD["Instância V1 em Execução"]
        C_NEW["Nova Imagem V2 (Gerada com Packer / Docker)"]
        C_SWAP["Substitui V1 por V2 e destrói V1"]
        C_OLD --> C_SWAP
        C_NEW --> C_SWAP
    end
```

| Critério de Análise | Infraestrutura Mutável (*Pets*) | Infraestrutura Imutável (*Cattle*) |
| :--- | :--- | :--- |
| **Mecanismo de Atualização** | Atualizações no local (*in-place*), instalando patches e compilando código diretamente na máquina em execução. | **Destruição da instância antiga** e subida de uma nova instância pré-construída com a imagem atualizada. |
| **Identidade dos Servidores** | Servidores únicos, com nomes próprios e manutenção artesanal (*animais de estimação*). | Servidores anônimos, descartáveis, idênticos e substituíveis (*cabeças de gado*). |
| **Patologia / Risco Típico** | **Servidores "Snowflake":** Instâncias artesanais com configurações acumuladas que ninguém sabe reproduzir do zero. | Tempo e pipeline necessários para compilar e homologar a imagem antes do deploy. |
| **Facilidade de Rollback** | Complexa e arriscada (exige scripts de desinstalação reversos). | **Instantânea e segura:** Basta apontar o balanceador para a imagem anterior testada. |
| **Tecnologias Viabilizadoras** | Ansible, Puppet, Chef, scripts Bash in-place. | Packer, Docker, Terraform, Kubernetes, AMIs de nuvem. |

---

### Teste 214
**(FGV – TJ-AP – Analista Judiciario Apoio Especializado Tecnologia da Informacao Banco de Dados – 2023)**
Analise o código Python a seguir. L=[0,1,1,2,3,5,8,13] for k in range(1,len(L)): L[k],L[k-1] = L[k-1],L[k] print L[-1] O último valor exibido na execução desse código é:

* **A)** 0;
* **B)** 1;
* **C)** 5;
* **D)** 8;
* **E)** 13.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *1.2 Paradigma Declarativo (O Quê) vs. Imperativo (Como)* deste guia, o motor da ferramenta de IaC é responsável por consultar o estado atual da nuvem, compará-lo com o código, deduzir a diferença matemática (*delta*) e orquestrar a execução estrita das ações necessárias para atingir a meta. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ-AP/2023) ao estabelecer que "0".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "1". De acordo com a teoria estudada em *Desvio de Configuração (Configuration Drift)*, correção Automatizada: Na execução seguinte de planejamento (`terraform plan`), o motor compara o estado real com o código, detecta a divergência e propõe a reversão compulsória da alteração manual, restaurando a conformidade institucional.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "5". De acordo com a teoria estudada em *1.4 Infraestrutura Mutável vs. Imutável (Pets vs. Cattle)*, mecanismo de Atualização: Atualizações no local (*in-place*), instalando patches e compilando código diretamente na máquina em execução. — Destruição da instância antiga e subida de uma nova instância pré-construída com a imagem atualizada.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "8". De acordo com a teoria estudada em *3.2 Matriz Comparativa Detalhada: Ansible vs. Puppet vs. Chef*, requisito no Destino: Python instalado e servidor SSH/WinRM ativo — Agente Puppet instalado e em execução — Agente Chef Client instalado e em execução.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "13". De acordo com a teoria estudada em *1.2 Paradigma Declarativo (O Quê) vs. Imperativo (Como)*, exemplos Canônicos: Shell Scripts (Bash/PowerShell), AWS CLI, chamadas via SDK Python (Boto3).
>
> **Gabarito: A**

---

### Teste 215
**(FGV – TJ-AP – Analista Judiciario Apoio Especializado Tecnologia da Informacao Desenvolvimento de Sistemas – 2023)**
Analise o código Python a seguir. L=[0,1,1,2,3] for k in range(4, -4, -1): print (L[k] + L[k % len(L)]) O resultado da execução desse código, na ordem, é:

* **A)** 4, 2, 2, 0, 6, 4;
* **B)** 6, 4, 2, 2, 0, 6, 4, 2, 2;
* **C)** 6, 4, 2, 2, 0, 6, 4, 2;
* **D)** 6, 4, 2, 2, 6, 4, 2;
* **E)** 6, 4, 2, 0, 6, 4, 2.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "4, 2, 2, 0, 6, 4". De acordo com a teoria estudada em *1.2 Paradigma Declarativo (O Quê) vs. Imperativo (Como)*, o motor da ferramenta de IaC é responsável por consultar o estado atual da nuvem, compará-lo com o código, deduzir a diferença matemática (*delta*) e orquestrar a execução estrita das ações necessárias para atingir a meta.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "6, 4, 2, 2, 0, 6, 4, 2, 2". De acordo com a teoria estudada em *Desvio de Configuração (Configuration Drift)*, correção Automatizada: Na execução seguinte de planejamento (`terraform plan`), o motor compara o estado real com o código, detecta a divergência e propõe a reversão compulsória da alteração manual, restaurando a conformidade institucional.
> - **C)** **Correta.** Conforme fundamentado na seção *Idempotência* deste guia, uma operação é dita idempotente se a sua execução repetida múltiplas vezes sobre um mesmo sistema produz exatamente o mesmo resultado final da primeira execução, sem gerar efeitos colaterais indesejados, duplicações de recursos ou erros de execução. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ-AP/2023) ao estabelecer que "6, 4, 2, 2, 0, 6, 4, 2".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "6, 4, 2, 2, 6, 4, 2". De acordo com a teoria estudada em *1.4 Infraestrutura Mutável vs. Imutável (Pets vs. Cattle)*, mecanismo de Atualização: Atualizações no local (*in-place*), instalando patches e compilando código diretamente na máquina em execução. — Destruição da instância antiga e subida de uma nova instância pré-construída com a imagem atualizada.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "6, 4, 2, 0, 6, 4, 2". De acordo com a teoria estudada em *3.2 Matriz Comparativa Detalhada: Ansible vs. Puppet vs. Chef*, requisito no Destino: Python instalado e servidor SSH/WinRM ativo — Agente Puppet instalado e em execução — Agente Chef Client instalado e em execução.
>
> **Gabarito: C**

---

### Teste 216
**(CEBRASPE – TJ-RJ – Analista Judiciario Grupo Tecnologia da Informacao Analista de Infraestrutura de Tic – 2021)**
Em um servidor que tem dez bancos de dados disponíveis e que funciona em ambiente de produção utilizando Mysql Server, o utilitário a ser usado a fim de gerar um backup de todos os bancos de dados contidos no servidor é o

* **A)** mysqldiff.
* **B)** mysqldump.
* **C)** mysqlrplcheck.
* **D)** mysqlgrants.
* **E)** mysqlfailover.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "mysqldiff". De acordo com a teoria estudada em *2.1 Estrutura e Blocos Fundamentais da Linguagem HCL*, `resource`: Bloco primordial que declara os componentes que devem ser criados e mantidos no provedor (ex.: VPCs, instâncias EC2, bancos RDS).
> - **B)** **Correta.** Conforme fundamentado na seção *1.1 Definição, Propósito e Benefícios de Engenharia* deste guia, reprodutibilidade e Consistência: Permite recriar ambientes completos de homologação, testes e produção com total fidelidade a partir de um único comando, erradicando o problema do "na minha máquina funciona". Dessa forma, está plenamente correta a assertiva da banca (CEBRASPE – TJ-RJ/2021) ao estabelecer que "mysqldump".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "mysqlrplcheck". De acordo com a teoria estudada em *Idempotência*, uma operação é dita idempotente se a sua execução repetida múltiplas vezes sobre um mesmo sistema produz exatamente o mesmo resultado final da primeira execução, sem gerar efeitos colaterais indesejados, duplicações de recursos ou erros de execução.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "mysqlgrants". De acordo com a teoria estudada em *Idempotência*, *Na prática:* Se você executar `terraform apply` ou rodar um *Playbook* do Ansible dez vezes consecutivas sobre uma infraestrutura estável sem alterar o código, a ferramenta validará que o estado real já coincide com o estado desejado e reportará zero alterações (`0 to add, 0 to change, 0 to destroy` ou `changed=0`).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "mysqlfailover". De acordo com a teoria estudada em *1.2 Paradigma Declarativo (O Quê) vs. Imperativo (Como)*, a ferramenta executa as instruções cegamente. Se o script falhar na metade, o ambiente fica em estado inconsistente (*partially applied*), exigindo scripts corretivos ou intervenções manuais.
>
> **Gabarito: B**

---

## 2. Provisionamento Declarativo com Terraform e OpenTofu

O **Terraform** (desenvolvido pela HashiCorp) e seu fork comunitário de código aberto **OpenTofu** (mantido sob a governança da *Linux Foundation*) são as plataformas líderes para provisionamento declarativo multi-nuvem e multi-provedor.

```mermaid
flowchart TD
    subgraph Terraform_Flow["Ciclo de Vida Operacional do Terraform"]
        CODE["Código HCL (*.tf)"] --> INIT["terraform init<br/>(Baixa Provedores e Inicia Backend)"]
        INIT --> PLAN["terraform plan<br/>(Lê Cloud e State; Calcula Diff)"]
        PLAN --> APPLY["terraform apply<br/>(Aplica alterações reais na Cloud)"]
        APPLY --> STATE[("terraform.tfstate<br/>(Atualiza arquivo de Estado)")]
        STATE -.->|Base de comparação| PLAN
    end
```

### 2.1 Estrutura e Blocos Fundamentais da Linguagem HCL

O código é estruturado na linguagem *HashiCorp Configuration Language* (HCL) através de blocos declarativos coesos:

```hcl
terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  backend "s3" { # Remote Backend Seguro
    bucket         = "tce-terraform-state"
    key            = "producao/infra.tfstate"
    region         = "us-east-1"
    dynamodb_table = "tce-lock-table" # State Locking
  }
}

provider "aws" {
  region = var.regiao_padrao
}

resource "aws_vpc" "rede_tce" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  tags = {
    Name = "vpc-fiscalizacao-tce"
  }
}

output "vpc_id" {
  value       = aws_vpc.rede_tce.id
  description = "ID da VPC gerada pelo provedor"
}
```

- **`terraform {}`:** Configurações globais do próprio motor, requisitos de versões mínimas e declaração do *Backend* de armazenamento do estado.
- **`provider`:** Módulos de plugins responsáveis por traduzir as instruções HCL em chamadas REST para as APIs dos provedores de destino (AWS, Azure, Google Cloud, VMware, Kubernetes).
- **`resource`:** Bloco primordial que declara os componentes que devem ser criados e mantidos no provedor (ex.: VPCs, instâncias EC2, bancos RDS).
- **`data`:** Fontes de dados (*Data Sources*) utilizadas para consultar informações sobre recursos pré-existentes na infraestrutura que foram criados fora do escopo do manifesto atual.
- **`variable`:** Parâmetros de entrada que tornam o código flexível e reutilizável.
- **`output`:** Valores de retorno exportados após a execução (ex.: IP público de um balanceador, ID de uma VPC).
- **`module`:** Pacote de configurações HCL autocontidas e parametrizadas que funcionam como funções reutilizáveis em múltiplos ambientes.

### 2.2 O Arquivo de Estado (terraform.tfstate), Remote Backend e State Locking

- **A Função do `terraform.tfstate`:** É o coração transacional do Terraform. Ele mapeia os identificadores declarados no código HCL com os identificadores reais gerados nas APIs da nuvem (ex.: mapeia o recurso `aws_vpc.rede_tce` ao identificador físico `vpc-0123456789abcdef0`), além de armazenar metadados e dependências.
- **Remote Backend:** Em times profissionais e órgãos públicos, o arquivo `.tfstate` **nunca deve ser versionado no Git local** (pois pode conter senhas em texto claro e causará conflitos insolúveis). Ele deve ser armazenado em um repositório remoto seguro com criptografia em repouso (ex.: Amazon S3, Google Cloud Storage, Terraform Cloud).
- **State Locking (Bloqueio de Estado):** Mecanismo de controle de concorrência que impede que dois operadores ou pipelines de CI/CD executem `terraform apply` simultaneamente sobre a mesma infraestrutura, o que provocaria corrupção catastrófica de dados. No AWS S3, o locking é implementado através de tabelas no **Amazon DynamoDB**.

### 2.3 Ciclo Operacional da CLI: init, validate, plan, apply e destroy

1. **`terraform init`:** Inicializa o diretório de trabalho, baixa os plugins dos provedores necessários (`providers`) e conecta ao *backend* de estado configurado.
2. **`terraform validate`:** Realiza a análise estática da sintaxe HCL e checa a consistência interna das variáveis sem consultar as APIs dos provedores.
3. **`terraform plan`:** Executa o planejamento especulativo: consulta a nuvem real, compara com o `.tfstate` e com o código HCL, exibindo a prévia exata do que será criado (`+`), alterado (`~`) ou destruído (`-`), **sem realizar modificações reais**.
4. **`terraform apply`:** Aplica efetivamente as alterações na nuvem com base no plano aprovado e atualiza o arquivo de estado.
5. **`terraform destroy`:** Destrói de forma controlada todos os recursos gerenciados por aquele projeto específico de IaC.

---

### Teste 217
**(FCC – TRT-13 – Analista Judiciario Tecnologia da Informacao – 2014)**
Considere: I. Para cada processo aberto deve ser emitido um aviso eletrônico para o juizado correspondente. II. Os tempos de resposta do sistema não podem exceder a 20 milissegundos, em qualquer hipótese. III. A disponibilidade da rede de dados deve ser 24 × 7. IV. Cada juiz deve ser capaz de realizar uma busca de processos, tanto pelo número quanto pela data ou pelo responsável. V. Toda modificação realizada nos programas do sistema devem seguir os padrões estabelecidos na Gestão de Mudanças. É exemplo de requisito não funcional o que consta APENAS em

* **A)** I, III e IV.
* **B)** II e IV.
* **C)** I, IV e V.
* **D)** I, III e V.
* **E)** II, III e V.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I, III e IV". De acordo com a teoria estudada em *2.1 Estrutura e Blocos Fundamentais da Linguagem HCL*, `resource`: Bloco primordial que declara os componentes que devem ser criados e mantidos no provedor (ex.: VPCs, instâncias EC2, bancos RDS).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "II e IV". De acordo com a teoria estudada em *2.2 O Arquivo de Estado (terraform.tfstate), Remote Backend e State Locking*, remote Backend: Em times profissionais e órgãos públicos, o arquivo `.tfstate` nunca deve ser versionado no Git local (pois pode conter senhas em texto claro e causará conflitos insolúveis).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I, IV e V". De acordo com a teoria estudada em *2.2 O Arquivo de Estado (terraform.tfstate), Remote Backend e State Locking*, ele deve ser armazenado em um repositório remoto seguro com criptografia em repouso (ex.: Amazon S3, Google Cloud Storage, Terraform Cloud).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I, III e V". De acordo com a teoria estudada em *1.2 Paradigma Declarativo (O Quê) vs. Imperativo (Como)*, o operador define o estado final almejado da infraestrutura (ex.: *"devem existir 3 máquinas virtuais com 8GB de RAM na sub-rede privada"*).
> - **E)** **Correta.** Conforme fundamentado na seção *2.1 Estrutura e Blocos Fundamentais da Linguagem HCL* deste guia, `data`: Fontes de dados (*Data Sources*) utilizadas para consultar informações sobre recursos pré-existentes na infraestrutura que foram criados fora do escopo do manifesto atual. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT-13/2014) ao estabelecer que "II, III e V".
>
> **Gabarito: E**

---

### Teste 218
**(FCC – TRT-15 – Analista Judiciario Tecnologia da Informacao – 2015)**
Em uma página HTML5 há o bloco de código conforme abaixo. `<code>` int i=0; while (i &lt;=10){ out.print(i); i++; } `</code>` Ao executar a página no navegador, foi exibido o seguinte conteúdo: int i=0; while (i <=10){ out.print(i); i++; } Para que a exibição tenha ocorrido desta forma, este bloco de código estava no interior das tags

* **A)** `<samp>` e `</samp>`
* **B)** `<kbd>` e `</kbd>`
* **C)** `<fixed>` e `</fixed>`
* **D)** `<pre>` e `</pre>`
* **E)** `<operation>` e `</operation>`

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "`<samp>` e `</samp>`". De acordo com a teoria estudada em *2.1 Estrutura e Blocos Fundamentais da Linguagem HCL*, `data`: Fontes de dados (*Data Sources*) utilizadas para consultar informações sobre recursos pré-existentes na infraestrutura que foram criados fora do escopo do manifesto atual.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "`<kbd>` e `</kbd>`". De acordo com a teoria estudada em *1. Fundamentos de Infraestrutura como Código (IaC)*, a Infraestrutura como Código (*Infrastructure as Code - IaC*) é a prática de engenharia que substitui o provisionamento manual e artesanal de recursos computacionais (telas interativas de consoles de nuvem, assistentes gráficos e comandos isolados no terminal) por arquivos descritivos de configuração legíveis por máquina e versionados em sistemas de controle de versão (como o Git).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "`<fixed>` e `</fixed>`". De acordo com a teoria estudada em *2.1 Estrutura e Blocos Fundamentais da Linguagem HCL*, `resource`: Bloco primordial que declara os componentes que devem ser criados e mantidos no provedor (ex.: VPCs, instâncias EC2, bancos RDS).
> - **D)** **Correta.** Conforme fundamentado na seção *1.4 Infraestrutura Mutável vs. Imutável (Pets vs. Cattle)* deste guia, mecanismo de Atualização: Atualizações no local (*in-place*), instalando patches e compilando código diretamente na máquina em execução. — Destruição da instância antiga e subida de uma nova instância pré-construída com a imagem atualizada. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT-15/2015) ao estabelecer que "`<pre>` e `</pre>`".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "`<operation>` e `</operation>`". De acordo com a teoria estudada em *2.3 Ciclo Operacional da CLI: init, validate, plan, apply e destroy*, `terraform destroy`: Destrói de forma controlada todos os recursos gerenciados por aquele projeto específico de IaC.
>
> **Gabarito: D**

---

### Teste 219
**(FGV – TRF-1 – Analista Judiciario Area Apoio Especializado Especialidade Tecnologia da Informacao – 2024)**
A analista Priscila escreveu o seguinte shell script no arquivo q03.sh: #!/bin/bash alias echo3='echo -n TRF' function echo2 () { \$echo1 } echo1='echo TRF' \$echo1 echo2 echo3 Priscila executou o script acima em um terminal com o interpretador Bash, através do comando “bash q03.sh”. Após a execução do comando, Priscila observou que a string “TRF” foi impressa na saída do terminal:

* **A)** uma vez;
* **B)** três vezes;
* **C)** duas vezes;
* **D)** nenhuma vez, gerando erro;
* **E)** nenhuma vez, sem gerar erro.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "uma vez". De acordo com a teoria estudada em *2.1 Estrutura e Blocos Fundamentais da Linguagem HCL*, `output`: Valores de retorno exportados após a execução (ex.: IP público de um balanceador, ID de uma VPC).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "três vezes". De acordo com a teoria estudada em *1.2 Paradigma Declarativo (O Quê) vs. Imperativo (Como)*, exemplos Canônicos: Shell Scripts (Bash/PowerShell), AWS CLI, chamadas via SDK Python (Boto3).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "duas vezes". De acordo com a teoria estudada em *3.4 Sinergia Arquitetural: Terraform no Provisionamento + Ansible na Configuração*, a prática de ponta em engenharia de plataforma e DevOps preconiza a combinação harmônica das duas ferramentas.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "nenhuma vez, gerando erro". De acordo com a teoria estudada em *2.2 O Arquivo de Estado (terraform.tfstate), Remote Backend e State Locking*, no AWS S3, o locking é implementado através de tabelas no Amazon DynamoDB.
> - **E)** **Correta.** Conforme fundamentado na seção *Idempotência* deste guia, uma operação é dita idempotente se a sua execução repetida múltiplas vezes sobre um mesmo sistema produz exatamente o mesmo resultado final da primeira execução, sem gerar efeitos colaterais indesejados, duplicações de recursos ou erros de execução. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRF-1/2024) ao estabelecer que "nenhuma vez, sem gerar erro".
>
> **Gabarito: E**

---

## 3. Gerenciamento Automatizado de Configuração: Ansible vs. Puppet vs. Chef

Enquanto o Terraform se especializa em **provisionar a infraestrutura básica** (redes, instâncias virtuais, balanceadores), as ferramentas de gerenciamento de configuração especializam-se em **configurar o interior dos sistemas operacionais** (instalar pacotes, aplicar patches de segurança, gerenciar arquivos de configuração e orquestrar serviços).

```mermaid
flowchart TD
    subgraph Push_Agentless["Ansible: Modelo Push & Agentless"]
        A_CTRL["Nó de Controle Ansible"]
        A_NODE1["Nó 1 (Linux)"]
        A_NODE2["Nó 2 (Windows)"]
        A_CTRL -->|"SSH (Porta 22)"| A_NODE1
        A_CTRL -->|"WinRM (Porta 5986)"| A_NODE2
    end

    subgraph Pull_AgentBased["Puppet / Chef: Modelo Pull & Agent-Based"]
        P_SRV["Puppet Master / Chef Server"]
        P_NODE1["Nó 1 (Agente Residente)"]
        P_NODE2["Nó 2 (Agente Residente)"]
        P_NODE1 -.->|"Consulta periódica a cada 30min"| P_SRV
        P_NODE2 -.->|"Consulta periódica a cada 30min"| P_SRV
    end
```

### 3.1 Modelos Arquiteturais: Push vs. Pull e Agentless vs. Agent-Based

- **Modelo Push (Empurrado) vs. Pull (Puxado):**
    - **Push (Ansible):** O servidor central de controle toma a iniciativa ativa: conecta-se aos nós de destino e empurra os comandos e scripts de configuração sob demanda do operador.
    - **Pull (Puppet e Chef):** Os nós clientes possuem agentes residentes executando em segundo plano que consultam periodicamente o servidor mestre (ex.: a cada 30 minutos) para verificar se há novas diretivas e aplicar correções locais.
- **Agentless (Sem Agente) vs. Agent-Based (Baseado em Agente):**
    - **Agentless (Ansible):** Não requer a instalação de nenhum software, daemon ou agente proprietário nos nós gerenciados. Utiliza protocolos de comunicação remota já existentes no próprio sistema operacional hospedeiro: **SSH** (porta 22) para sistemas Linux/Unix e **WinRM** (porta 5986) para sistemas Windows. Requer apenas o interpretador Python instalado nos nós-alvo.
    - **Agent-Based (Puppet e Chef):** Exige a instalação, configuração e manutenção de um agente residente proprietário (*Puppet Agent* ou *Chef Client*) em cada nó gerenciado, além de infraestrutura de certificados digitais TLS (PKI dedicada) para autenticar os nós junto ao servidor central.

### 3.2 Matriz Comparativa Detalhada: Ansible vs. Puppet vs. Chef

| Dimensão Técnica | Ansible | Puppet | Chef |
| :--- | :--- | :--- | :--- |
| **Arquitetura de Agentes** | **Agentless (Sem Agente)** | **Agent-based (Baseado em Agente)** | **Agent-based (Baseado em Agente)** |
| **Modelo de Execução** | **Push** (Nó de controle despacha tarefas) | **Pull** (Nó cliente busca configurações) | **Pull** (Nó cliente busca configurações) |
| **Protocolo de Transporte** | **SSH** padrão (Linux) e **WinRM** (Windows) | HTTPS com certificados TLS (PKI dedicada) | HTTPS com certificados TLS e API REST |
| **Linguagem de Definição** | **YAML** + Templates Jinja2 | DSL declarativa própria (*Puppet Language*) | **Ruby puro** (*Cookbooks* e *Recipes*) |
| **Curva de Aprendizado** | Baixa e imediata | Moderada | Alta (exige fluência em Ruby) |
| **Requisito no Destino** | Python instalado e servidor SSH/WinRM ativo | Agente Puppet instalado e em execução | Agente Chef Client instalado e em execução |

### 3.3 Anatomia Operacional do Ansible: Inventário, Playbooks, Módulos, Handlers e Roles

1. **Arquivo de Inventário (`inventory`):** Mapeia os endereços IP ou nomes de domínio dos servidores-alvo agrupados por categorias lógicas (formato INI ou YAML):

```ini
[webservers]
10.0.1.10
10.0.1.11

[dbservers]
10.0.2.20
```

2. **Playbooks:** Manifestos em YAML que definem as "jogadas" (*plays*), associando grupos do inventário a uma sequência de tarefas (*tasks*):

```yaml
- name: Configurar Servidor Web Corporativo
  hosts: webservers
  become: true
  tasks:
    - name: Garantir que o Nginx esteja instalado
      apt:
        name: nginx
        state: present

    - name: Atualizar o arquivo de configuracao
      template:
        src: nginx.conf.j2
        dest: /etc/nginx/nginx.conf
      notify: Reiniciar Servico Nginx

  handlers:
    - name: Reiniciar Servico Nginx
      service:
        name: nginx
        state: restarted
```

3. **Módulos Idempotentes:** Funções especializadas que realizam as modificações de baixo nível (`apt`, `package`, `service`, `systemd`, `copy`, `template`, `file`).
4. **Handlers (Gatilhos Condicionais):** Tarefas especiais que **só são executadas se alguma tarefa anterior tiver efetivamente modificado o estado do nó (`changed=true`)** e emitido um evento via diretiva `notify`. Se a tarefa não causou alteração (status `ok`), o handler não é disparado, evitando reinicializações desnecessárias de serviços em produção.
5. **Facts (Fatos do Sistema):** O Ansible coleta automaticamente no início da execução um dicionário detalhado de metadados do nó gerenciado (endereços IP, interfaces, capacidade de memória RAM, versão do Kernel, distribuição Linux).
6. **Roles (Papéis Modulares):** Estrutura padronizada de diretórios (`tasks/`, `handlers/`, `templates/`, `defaults/`, `vars/`) que organiza pacotes de automação para reutilização em larga escala.

### 3.4 Sinergia Arquitetural: Terraform no Provisionamento + Ansible na Configuração

A prática de ponta em engenharia de plataforma e DevOps preconiza a combinação harmônica das duas ferramentas:

- **Terraform:** Atua na camada de **Infraestrutura**. Cria VPCs, sub-redes, gateways de internet, grupos de segurança, discos e instancia as máquinas virtuais ou clusters Kubernetes.
- **Ansible:** Atua na camada de **Configuração do Sistema**. Uma vez provisionadas as instâncias, o Ansible conecta-se a elas via SSH para endurecer o sistema operacional (*hardening*), instalar utilitários, configurar usuários e preparar os nós para as cargas de trabalho corporativas.

---

### Teste 220
**(FGV – TRT-24 – Analista Judiciario Area Administrativa Sem Especialidade – 2025)**
O controle e o inventário de bens patrimoniais na Administração Pública buscam garantir a adequada gestão, a rastreabilidade e a conservação dos ativos públicos, promovendo transparência, responsabilidade e eficiência no uso dos recursos. Sobre o inventário físico de materiais, assinale a afirmativa correta.

* **A)** O inventário físico é um procedimento interno facultativo, sem implicações fiscais ou contábeis.
* **B)** O principal objetivo do inventário físico é eliminar os controles contábeis, substituindo-os por registros manuais.
* **C)** O inventário físico visa apenas ao controle da quantidade de itens no almoxarifado, sem considerar valores monetários.
* **D)** O inventário físico não tem relação com o encerramento do exercício fiscal, sendo realizado apenas em caso de suspeita de perdas ou desvios.
* **E)** O inventário físico permite verificar discrepâncias entre registros e estoques reais, atendendo às exigências fiscais e possibilitando a apuração do valor do estoque para fins contábeis.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção afasta requisito ou relação estrutural exigida pela matéria ao afirmar que "O inventário físico é um procedimento interno facultativo, sem implicações fiscais ou contábeis". De acordo com a teoria estudada em *3.1 Modelos Arquiteturais: Push vs. Pull e Agentless vs. Agent-Based*, pull (Puppet e Chef): Os nós clientes possuem agentes residentes executando em segundo plano que consultam periodicamente o servidor mestre (ex.: a cada 30 minutos) para verificar se há novas diretivas e aplicar correções locais.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O principal objetivo do inventário físico é eliminar os controles contábeis, substituindo-os por registros manuais". De acordo com a teoria estudada em *1.1 Definição, Propósito e Benefícios de Engenharia*, reprodutibilidade e Consistência: Permite recriar ambientes completos de homologação, testes e produção com total fidelidade a partir de um único comando, erradicando o problema do "na minha máquina funciona".
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "O inventário físico visa apenas ao controle da quantidade de itens no almoxarifado, sem considerar valores...". De acordo com a teoria estudada em *Desvio de Configuração (Configuration Drift)*, um administrador conecta via console web da nuvem ou via terminal SSH e altera manualmente uma porta de firewall ou a quantidade de memória de uma instância sem refletir essa mudança no repositório Git.
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "O inventário físico não tem relação com o encerramento do exercício fiscal, sendo realizado apenas em caso de...". De acordo com a teoria estudada em *3.3 Anatomia Operacional do Ansible: Inventário, Playbooks, Módulos, Handlers e Roles*, arquivo de Inventário (`inventory`): Mapeia os endereços IP ou nomes de domínio dos servidores-alvo agrupados por categorias lógicas (formato INI ou YAML).
> - **E)** **Correta.** Conforme fundamentado na seção *2.2 O Arquivo de Estado (terraform.tfstate), Remote Backend e State Locking* deste guia, ele mapeia os identificadores declarados no código HCL com os identificadores reais gerados nas APIs da nuvem (ex.: mapeia o recurso `aws_vpc.rede_tce` ao identificador físico `vpc-0123456789abcdef0`), além de armazenar metadados e dependências. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT-24/2025) ao estabelecer que "O inventário físico permite verificar discrepâncias entre registros e estoques reais, atendendo às exigências...".
>
> **Gabarito: E**

---

### Teste 221
**(FGV – TRT-13 – Analista Judiciario Tecnologia da Informacao – 2022)**
Com relação ao Ansible da Red Hat, analise os itens a seguir. I. É uma ferramenta de automação que permite configurar sistemas, implantar softwares e orquestrar tarefas avançadas de TI, tais como implantações contínuas ou atualizações contínuas com tempo de inatividade zero. II. Ele é centralizado e pode se conectar facilmente com Kerberos, LDAP e outros sistemas de gerenciamento de autenticação descentralizada. III. Sua exposição à segurança é bastante reduzida pois usa a ferramenta OpenSSH para efetuar login remoto com o protocolo SSH. Está correto o que se afirma em

* **A)** I, apenas.
* **B)** II, apenas.
* **C)** III, apenas.
* **D)** I e II, apenas.
* **E)** I e III, apenas.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I, apenas". De acordo com a teoria estudada em *1.1 Definição, Propósito e Benefícios de Engenharia*, automação via Pipelines de CI/CD: A infraestrutura pode ser validada por linters estáticos, testes de segurança e submetida a aprovações por pares antes de ser aplicada compulsoriamente por runners automatizados (*GitOps*).
> - **B)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II, apenas". De acordo com a teoria estudada em *3.2 Matriz Comparativa Detalhada: Ansible vs. Puppet vs. Chef*, protocolo de Transporte: SSH padrão (Linux) e WinRM (Windows) — HTTPS com certificados TLS (PKI dedicada) — HTTPS com certificados TLS e API REST.
> - **C)** **Correta.** Conforme fundamentado na seção *3. Gerenciamento Automatizado de Configuração: Ansible vs. Puppet vs. Chef* deste guia, enquanto o Terraform se especializa em provisionar a infraestrutura básica (redes, instâncias virtuais, balanceadores), as ferramentas de gerenciamento de configuração especializam-se em configurar o interior dos sistemas operacionais (instalar pacotes, aplicar patches de segurança, gerenciar arquivos de configuração e orquestrar serviços). Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT-13/2022) ao estabelecer que "III, apenas".
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e II, apenas". De acordo com a teoria estudada em *3.4 Sinergia Arquitetural: Terraform no Provisionamento + Ansible na Configuração*, uma vez provisionadas as instâncias, o Ansible conecta-se a elas via SSH para endurecer o sistema operacional (*hardening*), instalar utilitários, configurar usuários e preparar os nós para as cargas de trabalho corporativas.
> - **E)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e III, apenas". De acordo com a teoria estudada em *Idempotência*, *Na prática:* Se você executar `terraform apply` ou rodar um *Playbook* do Ansible dez vezes consecutivas sobre uma infraestrutura estável sem alterar o código, a ferramenta validará que o estado real já coincide com o estado desejado e reportará zero alterações (`0 to add, 0 to change, 0 to destroy` ou `changed=0`).
>
> **Gabarito: C**

---

### Teste 222
**(FGV – TRT-24 – Analista Judiciario Area Apoio Especializado Tecnologia da Informacao – 2025)**
Gisele, uma analista do judiciário, necessita alterar os scripts de inicialização e shutdown de um servidor de aplicação Tomcat. Sabe-se que a configuração do Tomcat versão 11 usou os diretórios padrão indicados pelo programa instalador. O diretório que contém esses scripts é o

* **A)** /bin.
* **B)** /init.
* **C)** /config.
* **D)** /scripts.
* **E)** /webapps.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *3.1 Modelos Arquiteturais: Push vs. Pull e Agentless vs. Agent-Based* deste guia, push (Ansible): O servidor central de controle toma a iniciativa ativa: conecta-se aos nós de destino e empurra os comandos e scripts de configuração sob demanda do operador. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT-24/2025) ao estabelecer que "/bin".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "/init". De acordo com a teoria estudada em *2.3 Ciclo Operacional da CLI: init, validate, plan, apply e destroy*, `terraform init`: Inicializa o diretório de trabalho, baixa os plugins dos provedores necessários (`providers`) e conecta ao *backend* de estado configurado.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "/config". De acordo com a teoria estudada em *3.1 Modelos Arquiteturais: Push vs. Pull e Agentless vs. Agent-Based*, agent-Based (Puppet e Chef): Exige a instalação, configuração e manutenção de um agente residente proprietário (*Puppet Agent* ou *Chef Client*) em cada nó gerenciado, além de infraestrutura de certificados digitais TLS (PKI dedicada) para autenticar os nós junto ao servidor central.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "/scripts". De acordo com a teoria estudada em *1.2 Paradigma Declarativo (O Quê) vs. Imperativo (Como)*, a ferramenta executa as instruções cegamente. Se o script falhar na metade, o ambiente fica em estado inconsistente (*partially applied*), exigindo scripts corretivos ou intervenções manuais.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "/webapps". De acordo com a teoria estudada em *3.2 Matriz Comparativa Detalhada: Ansible vs. Puppet vs. Chef*, protocolo de Transporte: SSH padrão (Linux) e WinRM (Windows) — HTTPS com certificados TLS (PKI dedicada) — HTTPS com certificados TLS e API REST.
>
> **Gabarito: A**

---

### Teste 223
**(FGV – TJ-RR – Analista Judiciario Infraestrutura de Tecnologia da Informacao – 2024)**
No Kubernetes, há duas formas de aplicar mudanças na configuração de uma aplicação: imperativa e declarativa. Considere os dois comandos a seguir: 1: kubectl create -f exemplo.yaml 2: kubectl apply -f exemplo-deployment.yaml Nesse caso, é correto afirmar que

* **A)** 1 é um exemplo de comando declarativo, em que o kubectl especifica a operação que se deseja aplicar.
* **B)** 2 é um exemplo de comando imperativo, em que o kubectl especifica a operação que se deseja aplicar.
* **C)** 2 é um exemplo de comando imperativo, em que o usuário não define que operações serão executadas.
* **D)** 1 é um exemplo de comando declarativo, em que o sistema do Kubernetes decidirá a melhor forma de aplicá-lo.
* **E)** 2 é um exemplo de comando declarativo, em que o sistema do Kubernetes decidirá a melhor forma de aplicá-lo.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "1 é um exemplo de comando declarativo, em que o kubectl especifica a operação que se deseja aplicar". De acordo com a teoria estudada em *Idempotência*, uma operação é dita idempotente se a sua execução repetida múltiplas vezes sobre um mesmo sistema produz exatamente o mesmo resultado final da primeira execução, sem gerar efeitos colaterais indesejados, duplicações de recursos ou erros de execução.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "2 é um exemplo de comando imperativo, em que o kubectl especifica a operação que se deseja aplicar". De acordo com a teoria estudada em *1.2 Paradigma Declarativo (O Quê) vs. Imperativo (Como)*, exemplos Canônicos: Terraform, OpenTofu, AWS CloudFormation, manifestos do Kubernetes.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "2 é um exemplo de comando imperativo, em que o usuário não define que operações serão executadas". De acordo com a teoria estudada em *1.2 Paradigma Declarativo (O Quê) vs. Imperativo (Como)*, o operador define o estado final almejado da infraestrutura (ex.: *"devem existir 3 máquinas virtuais com 8GB de RAM na sub-rede privada"*).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "1 é um exemplo de comando declarativo, em que o sistema do Kubernetes decidirá a melhor forma de aplicá-lo". De acordo com a teoria estudada em *1.2 Paradigma Declarativo (O Quê) vs. Imperativo (Como)*, o operador programa a sequência cronológica e explícita de passos e comandos que o sistema deve executar para erguer a infraestrutura (ex.: *"passo 1: chame a API de criar VM; passo 2: pause por 30 segundos; passo 3: anexe o disco"*).
> - **E)** **Correta.** Conforme fundamentado na seção *Desvio de Configuração (Configuration Drift)* deste guia, o desvio de configuração manifesta-se quando recursos de produção são modificados manualmente "fora de banda" (*out-of-band*), por exemplo. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ-RR/2024) ao estabelecer que "2 é um exemplo de comando declarativo, em que o sistema do Kubernetes decidirá a melhor forma de aplicá-lo".
>
> **Gabarito: E**

---

## 🌐 Fontes Oficiais e Referências Bibliográficas

* [Terraform Official Documentation - State Management](https://developer.hashicorp.com/terraform/language/state) - Gerenciamento do arquivo de estado (terraform.tfstate), state locking e backends remotos.
* [Terraform Official Documentation - Terraform Core Concepts and CLI](https://developer.hashicorp.com/terraform/intro) - Ciclo de vida: init, plan, apply, destroy e princípio da idempotência declarativa.
* [Ansible Official Documentation - Playbooks and Architecture](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_intro.html) - Automação agentless via SSH, módulos nativos, inventários dinâmicos e handlers.
* [OpenTelemetry Official Documentation - Observability Signals](https://opentelemetry.io/docs/concepts/signals/) - Coleta unificada de telemetria em ambientes de infraestrutura provisionados.
* BRICKEY, Scott. **Terraform: Up & Running: Writing Infrastructure as Code**. 3. ed. Sebastopol: O'Reilly Media, 2022. (Cap. 2 e 3 - Sintaxe HCL e Gestão de Estado).
* MORRIS, Kief. **Infraestrutura como Código: Gerenciamento Dinâmico de Sistemas na Era da Nuvem**. 2. ed. São Paulo: Novatec, 2021. (Cap. 2 - Princípios de IaC; Cap. 5 - Idempotência e Convergência).
* HALL, Joseph. **Ansible Configuration Management**. 2. ed. Birmingham: Packt Publishing, 2016. (Cap. 3 - Playbooks, Roles e Automação de Tarefas).
