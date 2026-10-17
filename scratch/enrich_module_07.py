# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from enricher_base import inject_questions_into_file

# ==========================================
# FILE 1: 01_cultura_devops_ci_cd_e_automacao_de_pipelines.md
# ==========================================
file_1 = "fontes_de_estudo/conhecimentos_especificos_b02_ti/07_devops_e_plataforma_de_entrega/01_cultura_devops_ci_cd_e_automacao_de_pipelines.md"
injections_1 = [
    {
        "target_sec": "### 1.2 O Framework C.A.L.M.S.",
        "question_text": """### Questão 06
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
O framework C.A.L.M.S., concebido por Damon Edwards e John Willis, resume os cinco pilares fundacionais da cultura DevOps em organizações de alto desempenho. Os cinco pilares representados pelo acrônimo C.A.L.M.S. são:

* **A)** *Control, Architecture, Legacy, Monitoring, Speed*
* **B)** *Culture, Automation, Lean, Measurement, Sharing*
* **C)** *Containers, Agility, Linux, Microservices, Security*
* **D)** *Communication, Accuracy, Leadership, Management, Software*
* **E)** *Continuous, Alignment, Licensing, Maintenance, Scalability*

> **Comentário Detalhado:**
>
> - **A) Incorreta.** Termos arbitrários não correspondentes ao modelo.
> - **B) Correta.** O acrônimo C.A.L.M.S. traduz os cinco pilares essenciais de DevOps:
>   - **Culture (Cultura):** colaboração, empatia e quebra de silos entre Desenvolvimento e Operações;
>   - **Automation (Automação):** eliminação de tarefas manuais repetitivas via pipelines e IaC;
>   - **Lean (Pensamento Enxuto):** fluxo contínuo, lotes pequenos e eliminação de desperdícios;
>   - **Measurement (Mensuração):** telemetria, métricas de negócio e dados orientando decisões;
>   - **Sharing (Compartilhamento):** disseminação aberta de aprendizados, ferramentas e responsabilidade mútua.
> - **C) Incorreta.** Mistura ferramentas técnicas com termos ágeis.
> - **D) Incorreta.** Não reflete a definição oficial de DevOps.
> - **E) Incorreta.** Definição incorreta.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 1.3 As Três Vias do DevOps",
        "question_text": """### Questão 07
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
Na obra de referência *The DevOps Handbook* (Gene Kim, Jez Humble et al.), as práticas e princípios que norteiam a transformação DevOps são organizados nas "Três Vias" (*The Three Ways*). A Segunda Via (*The Second Way*) tem como objetivo primordial:

* **A)** Acelerar o fluxo unidirecional de valor de Desenvolvimento para Operações, aumentando o tamanho dos lotes de entrega.
* **B)** Amplificar e encurtar os ciclos de feedback da direita para a esquerda (de Operações/Produção de volta para Desenvolvimento), permitindo detectar, resolver e prevenir problemas no menor tempo possível.
* **C)** Estabelecer uma cultura de culpa (*blame culture*) onde cada incidente gera punição imediata ao engenheiro responsável.
* **D)** Terceirizar integralmente a responsabilidade da infraestrutura para servidores públicos em regime de comodato.
* **E)** Impedir a execução de testes automatizados no ambiente de desenvolvimento local.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** A Primeira Via (*The First Way*) foca nos Princípios de Fluxo (da esquerda para a direita, com lotes pequenos).
> - **B) Correta.** A Segunda Via (*The Second Way*) foca nos Princípios de Feedback: criar ciclos de retorno rápidos e contínuos de Operações/Produção para Desenvolvimento (*shift-left* do feedback, telemetria em tempo real), evitando que defeitos se propaguem e permitindo correção imediata.
> - **C) Incorreta.** A cultura DevOps baseia-se em post-mortems sem culpa (*blameless post-mortems*).
> - **D) Incorreta.** DevOps prega a colaboração integrada, não terceirização burocrática.
> - **E) Incorreta.** Testes contínuos são a base da automação DevOps.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 2.1 Integração Contínua (CI): Boas Práticas, Trunk-Based e Princípio Stop the Line",
        "question_text": """### Questão 08
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
Na esteira de Integração Contínua (CI), uma prática consagrada originária do Sistema Toyota de Produção (metáfora do *Andon Cord*) é o princípio do *"Stop the Line"* (Parar a Linha de Montagem). No contexto do desenvolvimento de software em equipe, esse princípio determina que:

* **A)** Sempre que o build quebrar ou um teste automatizado falhar no pipeline da branch principal, a equipe deve priorizar imediatamente a correção do problema antes de comitar qualquer novo código, impedindo o acúmulo de erros sobre uma base instável.
* **B)** Todos os desenvolvedores devem desligar seus computadores e sair do escritório por tempo indeterminado.
* **C)** O pipeline deve desabilitar os testes que falharam para que o deploy possa prosseguir normalmente para produção.
* **D)** O código da branch principal deve ser revertido para a versão original do ano anterior.
* **E)** A gerência deve transferir o projeto para uma consultoria externa sem aviso prévio.

> **Comentário Detalhado:**
>
> - **A) Correta.** O princípio "Stop the Line" estabelece disciplina inegociável de qualidade: um build quebrado é um sinal de emergência máxima para a equipe. Enquanto a branch principal estiver vermelha, novas funcionalidades não devem ser mescladas até que o problema seja diagnosticado e reparado.
> - **B) Incorreta.** A equipe deve agir rapidamente para restabelecer a integridade do build.
> - **C) Incorreta.** Desativar testes com falha é um anti-padrão gravíssimo que mascara falhas críticas em produção.
> - **D) Incorreta.** Ação desproporcional e descabida.
> - **E) Incorreta.** Afirmação absurda.
>
> **Gabarito: A**"""
    },
    {
        "target_sec": "### 3.4 Canary Deployment (Canário)",
        "question_text": """### Questão 09
**(FCC – TCE – Auditor de Controle Externo / Tecnologia da Informação)**  
Dentre as estratégias modernas de implantação contínua (*Deployment Strategies*), o *Canary Deployment* (Implantação Canário) diferencia-se da estratégia *Blue-Green* pelo fato de:

* **A)** Exigir a substituição imediata e simultânea de 100% dos servidores em produção em uma fração de segundo.
* **B)** Encaminhar gradualmente uma pequena fração controlada do tráfego real de usuários (por exemplo, 2% a 5%) para a nova versão da aplicação, monitorando métricas de erro e telemetria antes de expandir progressivamente o tráfego para a totalidade dos usuários.
* **C)** Manter dois ambientes idênticos em produção alternando o roteador de borda de forma binária de um para o outro.
* **D)** Impedir que o sistema opere durante os finais de semana.
* **E)** Funcionar exclusivamente em aplicações desktop monousuário desconectadas da rede.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** Essa é a estratégia de *Recreate* com parada de serviço (*downtime*).
> - **B) Correta.** O *Canary Deployment* (inspirado no canário nas minas de carvão) direciona uma pequena parcela do tráfego para a nova versão. Se a telemetria revelar anomalias (aumento de erros HTTP 500 ou latência), o tráfego é revertido instantaneamente sem afetar a maioria dos usuários; se os sinais forem saudáveis, a versão é expandida progressivamente até 100%.
> - **C) Incorreta.** Alternância total entre dois ambientes isolados (ativo e inativo) descreve a estratégia *Blue-Green Deployment*.
> - **D) Incorreta.** Práticas modernas operam com alta disponibilidade ininterrupta (24x7).
> - **E) Incorreta.** Aplica-se a sistemas web e distribuídos de alta escala.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 3.5 Feature Flags / Feature Toggles e Dark Launching",
        "question_text": """### Questão 10
**(FGV – TJ – Analista Judiciário / Tecnologia da Informação)**  
A utilização de *Feature Flags* (ou *Feature Toggles*) é uma técnica de engenharia de software indispensável para viabilizar entregas contínuas com Trunk-Based Development. A principal vantagem arquitetural proporcionada pelo uso de Feature Flags reside em:

* **A)** Acelerar a velocidade de clock do banco de dados relacional.
* **B)** Desacoplar formalmente a implantação física do código (*deployment*) da ativação comercial da funcionalidade para os usuários (*release*), permitindo que código em desenvolvimento seja mesclado na branch principal e enviado a produção em estado desligado.
* **C)** Excluir automaticamente o código-fonte da aplicação após 30 dias de uso em produção.
* **D)** Impedir que desenvolvedores utilizem branches locais no Git.
* **E)** Substituir os testes de segurança automatizados (SAST/DAST) por questionários manuais.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** Flags operam na camada de código/lógica da aplicação.
> - **B) Correta.** O conceito nuclear de Feature Flags é **Deploy != Release**: o código é implantado continuamente em produção, mas permanece invisível ou inativo para os usuários finais até que uma chave lógica de configuração seja ativada (permitindo testes A/B, liberação por usuário VIP ou *rollback* instantâneo sem necessidade de novo deploy).
> - **C) Incorreta.** Flags velhas devem ser removidas por manutenção, não deleção cega automática.
> - **D) Incorreta.** Não restringe branches locais.
> - **E) Incorreta.** Feature flags não substituem testes de segurança.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 4.1 Estágios Canônicos: Lint, Análise Estática (SAST/SCA), Build, Testes e Registry",
        "question_text": """### Questão 11
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
Na cultura DevSecOps, a integração da segurança ao longo de todo o ciclo de vida do software (*Shift-Left Security*) apoia-se em duas ferramentas automatizadas centrais no pipeline: SAST (*Static Application Security Testing*) e SCA (*Software Composition Analysis*). A correta distinção entre SAST e SCA estabelece que:

* **A)** SAST audita o código-fonte proprietário da organização em repouso em busca de vulnerabilidades e falhas de codificação (como injeção SQL e XSS), enquanto SCA analisa as dependências de terceiros e bibliotecas de código aberto para identificar vulnerabilidades conhecidas (CVEs) e riscos de licenciamento.
* **B)** SCA só pode ser executado em sistemas com servidores de banco de dados Oracle.
* **C)** SAST testa a aplicação em tempo de execução contra ataques de negação de serviço (DDoS).
* **D)** Ambos os termos são sinônimos perfeitos de testes manuais de caixa-preta realizados por estagiários.
* **E)** SAST destina-se exclusivamente a validar o layout gráfico de páginas em CSS3.

> **Comentário Detalhado:**
>
> - **A) Correta.** Distinção clássica cobrada em provas:
>   - **SAST (Static Application Security Testing):** varre o código proprietário da equipe (*white-box*, em repouso), detectando vulnerabilidades como SQL Injection, Buffer Overflow e segredos expostos;
>   - **SCA (Software Composition Analysis):** inspeciona o grafo de dependências externas (pacotes npm, Maven, pip), apontando CVEs cadastradas no NVD e problemas de licenças (como contaminação por GPLv3).
> - **B) Incorreta.** SCA é agnóstico ao banco de dados.
> - **C) Incorreta.** O teste de segurança em tempo de execução é o DAST (*Dynamic Application Security Testing*).
> - **D) Incorreta.** São ferramentas automatizadas de análise de segurança em pipelines.
> - **E) Incorreta.** SAST é focado em segurança de código.
>
> **Gabarito: A**"""
    }
]

# ==========================================
# FILE 2: 02_git_estrategias_de_branching_e_plataformas_colaborativas.md
# ==========================================
file_2 = "fontes_de_estudo/conhecimentos_especificos_b02_ti/07_devops_e_plataforma_de_entrega/02_git_estrategias_de_branching_e_plataformas_colaborativas.md"
injections_2 = [
    {
        "target_sec": "### 1.3 O Modelo GitHub Flow",
        "question_text": """### Questão 06
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
O modelo de ramificação *GitHub Flow* destaca-se por sua simplicidade e alinhamento estreito com práticas de Implantação Contínua. Diferentemente do complexo modelo *Git Flow*, a premissa central de governança do *GitHub Flow* estabelece que:

* **A)** Devem existir permanentemente cinco branches perenes no repositório com releases a cada dois anos.
* **B)** Há apenas uma branch de vida longa (`main` ou `master`), a qual deve estar permanentemente em estado de produção (testada e estável); novas funcionalidades são criadas a partir dela em branches descritivas de curta duração, integradas rapidamente via *Pull Request* e implantadas imediatamente em produção.
* **C)** Desenvolvedores são expressamente proibidos de abrir *Pull Requests* para revisão por pares.
* **D)** O código da branch principal nunca pode ser enviado para servidores de produção.
* **E)** As mesclagens devem ser realizadas exclusivamente por comando de voz do diretor de TI.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** O *Git Flow* possui múltiplas branches perenes (`main`, `develop`); o *GitHub Flow* foca em extrema simplicidade.
> - **B) Correta.** O *GitHub Flow* apoia-se em 6 regras canônicas: 1) qualquer coisa na branch `main` está pronta para deploy; 2) para trabalhar em algo novo, crie uma branch com nome descritivo a partir da `main`; 3) faça commits nessa branch local e remota; 4) abra um Pull Request para feedback; 5) revise e aprove; 6) faça merge na `main` e implante imediatamente em produção.
> - **C) Incorreta.** O Pull Request é o coração colaborativo do GitHub Flow.
> - **D) Incorreta.** A branch `main` é a própria base de produção.
> - **E) Incorreta.** Afirmação cômica e absurda.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 2.1 Create a Merge Commit (`git merge --no-ff`)",
        "question_text": """### Questão 07
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
No Git, ao integrar duas ramificações cuja branch de destino não sofreu alterações desde o ponto de bifurcação, o comportamento padrão é a execução de um *Fast-Forward* (avanço rápido do ponteiro). Entretanto, quando o desenvolvedor utiliza explicitamente o comando `git merge --no-ff`, o efeito técnico resultante é:

* **A)** A destruição de todos os arquivos modificados na branch de origem.
* **B)** A criação forçada de um commit de mescla (*merge commit*) com múltiplos pais, preservando formalmente no histórico gráfico a evidência histórica de que aqueles commits pertenceram a uma branch de desenvolvimento independente.
* **C)** A conversão do repositório Git local em um repositório centralizado Apache Subversion (SVN).
* **D)** O rebaseamento automático de todos os commits diretamente na memória ROM da placa-mãe.
* **E)** A execução de uma checagem de tipos estáticos sem criação de novos nós na árvore de commits.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** Não há perda de dados.
> - **B) Correta.** A flag `--no-ff` (*no fast-forward*) força a criação de um nó explícito de *merge commit* mesmo quando o Git poderia simplesmente avançar o ponteiro. Essa prática é valiosa para governança corporativa, pois demarca claramente o ciclo de vida e fechamento de cada funcionalidade no grafo de commits.
> - **C) Incorreta.** Não altera a natureza distribuída do Git.
> - **D) Incorreta.** Totalmente descabida.
> - **E) Incorreta.** A operação gera obrigatoriamente um novo commit no histórico.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 2.3 Rebase and Merge (`git rebase`)",
        "question_text": """### Questão 08
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
Em plataformas modernas de desenvolvimento colaborativo (como GitHub e GitLab), uma das opções de fechamento de Pull Requests é o *Rebase and Merge*. A principal consequência dessa estratégia na topologia do histórico da branch principal é:

* **A)** A geração de múltiplos commits de mescla entrelaçados em formato de teia de aranha.
* **B)** A geração de um histórico de commits estritamente linear e limpo, uma vez que os commits da feature branch são reaplicados um a um sobre a ponta da branch principal com novos hashes SHA, dispensando a criação de um commit de merge adicional.
* **C)** A descompactação de todos os arquivos em um servidor FTP legado.
* **D)** A impossibilidade de compilar o software após o merge.
* **E)** O travamento permanente de todas as demais branches do projeto.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** Essa topologia desorganizada ocorre com múltiplos merges bidirecionais sem rebase.
> - **B) Correta.** O *Rebase and Merge* reescreve os commits da branch individual sobre o topo da branch base (`main`), criando novos identificadores SHA-1/256 e produzindo uma linha do tempo perfeitamente linear e contínua, facilitando auditoria via `git log --oneline` e bissecção de bugs (`git bisect`).
> - **C) Incorreta.** Não há conexão com FTP.
> - **D) Incorreta.** A compilação opera normalmente.
> - **E) Incorreta.** Não trava o repositório.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 3.2 O Arquivo `CODEOWNERS` e Revisões Bloqueantes",
        "question_text": """### Questão 09
**(FCC – Inédita – Padrão TCE-GO)**  
No âmbito da governança de código e controle de acesso a repositórios de software corporativos, o arquivo especial `CODEOWNERS` (suportado por GitHub e GitLab) tem como função primordial:

* **A)** Definir senhas de acesso aos servidores de banco de dados de produção.
* **B)** Mapear padrões de arquivos e diretórios a pessoas ou equipes responsáveis (*owners*), associando-se a regras de proteção de branch para exigir a aprovação formal e obrigatória desses proprietários antes que Pull Requests que alterem esses caminhos específicos possam ser mesclados.
* **C)** Listar os salários dos funcionários que contribuem com o código-fonte.
* **D)** Proibir que desenvolvedores júnior leiam arquivos de teste.
* **E)** Substituir o compilador Java por um compilador de código proprietário.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** Segredos nunca devem ser colocados em arquivos de governança do repositório.
> - **B) Correta.** O arquivo `CODEOWNERS` (posicionado na raiz, em `.github/` ou `.gitlab/`) permite atribuir a custódia técnica de caminhos sensíveis (ex: `/segurança/`, `*.tf`, `/core/`) a especialistas ou times específicos. Quando integrado a regras de branch protection (*Require review from Code Owners*), nenhum PR nessas pastas pode ser mesclado sem o aval formal desses custodiantes.
> - **C) Incorreta.** Dado pessoal e corporativo alheio ao repositório.
> - **D) Incorreta.** Não restringe leitura em repositórios abertos à equipe.
> - **E) Incorreta.** Afirmação absurda.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 3.3 Comparativo Terminológico e Operacional: GitHub vs. GitLab",
        "question_text": """### Questão 10
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
As duas plataformas de desenvolvimento colaborativo e DevOps mais adotadas na administração pública são o GitHub e o GitLab. A respeito da correspondência terminológica e conceitual entre ambas as plataformas, é correto afirmar:

* **A)** A solicitação formal de revisão e mescla de código denomina-se *Pull Request* no GitHub e *Merge Request* no GitLab.
* **B)** O GitLab não suporta integração contínua (CI/CD), exigindo a contratação de ferramentas externas proprietárias.
* **C)** O GitHub proíbe a utilização de contêineres Docker em seus executores de pipeline (*Runners*).
* **D)** *Issues* existem apenas no GitHub, não havendo mecanismo de acompanhamento de demandas e chamados no GitLab.
* **E)** O GitLab exige que todo o código seja armazenado em fitas magnéticas analógicas.

> **Comentário Detalhado:**
>
> - **A) Correta.** É o clássico mapeamento terminológico: o que o GitHub chama de **Pull Request (PR)**, o GitLab denomina formalmente **Merge Request (MR)**. Da mesma forma, os executores de pipeline são *GitHub Actions Runners* e *GitLab Runners*.
> - **B) Incorreta.** O GitLab possui o *GitLab CI/CD* nativamente integrado ao repositório (via arquivo `.gitlab-ci.yml`).
> - **C) Incorreta.** GitHub Actions executa contêineres Docker tanto em steps quanto como ambiente de execução dos jobs.
> - **D) Incorreta.** Ambas as plataformas possuem módulos robustos de gestão de *Issues* e quadros Kanban.
> - **E) Incorreta.** Afirmação sem lógica técnica.
>
> **Gabarito: A**"""
    }
]

# ==========================================
# FILE 3: 03_conteinerizacao_docker_e_docker_compose.md
# ==========================================
file_3 = "fontes_de_estudo/conhecimentos_especificos_b02_ti/07_devops_e_plataforma_de_entrega/03_conteinerizacao_docker_e_docker_compose.md"
injections_3 = [
    {
        "target_sec": "### 1.2 Primitivas Essenciais do Kernel Linux: Namespaces e Control Groups (cgroups)",
        "question_text": """### Questão 06
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
A tecnologia de conteinerização no Linux fundamenta-se primordialmente em duas primitivas nativas do próprio Kernel do sistema operacional: os *Namespaces* e os *Control Groups* (*cgroups*). A respeito da responsabilidade técnica de cada uma dessas primitivas, é correto afirmar:

* **A)** Os *cgroups* isolam a visão dos processos sobre a rede e o sistema de arquivos, enquanto os *Namespaces* limitam o uso físico de memória RAM e CPU.
* **B)** Os *Namespaces* provêm o isolamento de visão dos recursos do sistema (como processos - PID, rede - NET, montagens - MNT e usuários - USER), enquanto os *cgroups* gerenciam, limitam e monitoram o consumo quantitativo de recursos de hardware (como cotas de CPU, limites de memória RAM e largura de banda de I/O de disco).
* **C)** Ambas as primitivas foram substituídas pelo uso de emuladores de BIOS de 16 bits.
* **D)** Os *Namespaces* só podem ser executados em servidores com placas gráficas de inteligência artificial.
* **E)** Os *cgroups* impedem que contêineres utilizem conexões de rede TCP/IP.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** As funções estão exatamente invertidas.
> - **B) Correta.** É a síntese arquitetural fundamental da conteinerização Linux:
>   - **Namespaces:** fornecem **isolamento** ("o que o processo pode enxergar"): cada contêiner ganha sua própria tabela de processos (PID), pilha de rede (NET), pontos de montagem (MNT), comunicação entre processos (IPC) e nomes de host (UTS);
>   - **cgroups (Control Groups):** fornecem **restrição e medição** ("quanto o processo pode consumir"): evitam que um contêiner monopolize a CPU, estoure a memória RAM da máquina host (disparando o OOM Killer) ou sature o subsistema de I/O.
> - **C) Incorreta.** Contêineres compartilham o kernel do host sem emulação de BIOS ou hipervisores.
> - **D) Incorreta.** São recursos nativos padrão do kernel Linux há décadas.
> - **E) Incorreta.** Rede é isolada por *Network Namespaces*.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 1.4 Sistema de Arquivos em Camadas (Overlay2 UnionFS) e Copy-on-Write (CoW)",
        "question_text": """### Questão 07
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
O sistema de arquivos em camadas do Docker (tipicamente implementado pelo driver de armazenamento `overlay2`) utiliza a estratégia *Copy-on-Write* (CoW). Esse mecanismo implica que:

* **A)** Todas as camadas que compõem a imagem base do Docker são estritamente somente-leitura (*read-only*) e imutáveis; quando um processo em execução dentro de um contêiner modifica um arquivo existente na imagem, o arquivo é copiado para a camada superior e efêmera de leitura e escrita (*read-write container layer*), onde a modificação é efetivada sem alterar a imagem original compartilhada.
* **B)** O disco rígido do servidor deve ser duplicado fisicamente a cada novo contêiner instanciado.
* **C)** Nenhuma modificação de arquivo pode ser realizada dentro de um contêiner Docker ativo.
* **D)** Todos os contêineres compartilham a mesma camada de leitura e escrita, gravando arquivos concorrentemente no mesmo bloco.
* **E)** As imagens Docker perdem todos os seus dados sempre que o contêiner é reiniciado.

> **Comentário Detalhado:**
>
> - **A) Correta.** No modelo UnionFS/Overlay2: as camadas da imagem são *read-only* e imutáveis, compartilhadas com segurança por centenas de contêineres na mesma máquina host. Ao subir um contêiner, o Docker anexa apenas uma fina camada *read-write* no topo. Pela mecânica *Copy-on-Write*, arquivos modificados sobem para essa camada superior, preservando a imagem intacta e economizando gigabytes de armazenamento.
> - **B) Incorreta.** A grande economia de espaço do Docker decorre justamente do compartilhamento de camadas de imagem.
> - **C) Incorreta.** A camada superior do contêiner aceita escrita normalmente.
> - **D) Incorreta.** Cada contêiner possui sua própria camada de escrita isolada.
> - **E) Incorreta.** A camada do contêiner persiste entre `stop` e `start` (perde-se apenas se o contêiner for removido com `docker rm`).
>
> **Gabarito: A**"""
    },
    {
        "target_sec": "### 2.1 Instruções Canônicas: FROM, WORKDIR, COPY vs. ADD, RUN, ENV vs. ARG",
        "question_text": """### Questão 08
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
Na elaboração de um arquivo `Dockerfile` para construção de imagens de software, duas instruções de cópia de arquivos frequentemente comparadas em concursos públicos são `COPY` e `ADD`. A boa prática recomendada de engenharia e a principal distinção técnica entre ambas estabelece que:

* **A)** A instrução `COPY` é mais simples e transparente, copiando arquivos e diretórios locais da máquina de build para o contêiner, devendo ser preferida na imensa maioria dos casos; a instrução `ADD`, além da cópia local, suporta o download de arquivos via URLs remotas e a extração automática de arquivos compactados (como `.tar.gz`) diretamente no destino.
* **B)** A instrução `ADD` é estritamente proibida em todas as distribuições Linux modernas.
* **C)** A instrução `COPY` só funciona para arquivos com extensão `.exe`.
* **D)** A instrução `ADD` compila o código-fonte Java automaticamente durante a cópia.
* **E)** Nenhuma das duas instruções permite copiar arquivos para diretórios internos do contêiner.

> **Comentário Detalhado:**
>
> - **A) Correta.** É a orientação oficial das melhores práticas de Dockerfile: prefira sempre `COPY` por ser previsível e direta (apenas copia arquivos locais). Use `ADD` somente quando você realmente necessitar da extração automática de pacotes compactados (*tar auto-extraction*) para o sistema de arquivos da imagem.
> - **B) Incorreta.** `ADD` é uma instrução padrão válida do Docker.
> - **C) Incorreta.** Opera sobre qualquer arquivo.
> - **D) Incorreta.** `ADD` apenas transfere e descompacta; quem compila são comandos executados via `RUN`.
> - **E) Incorreta.** Ambas copiam arquivos para o contêiner.
>
> **Gabarito: A**"""
    },
    {
        "target_sec": "### 2.3 Exposição de Portas e Segurança: EXPOSE vs. Publicação no Host e Diretiva USER",
        "question_text": """### Questão 09
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
Em relação às diretrizes de segurança da informação e redes na construção de contêineres Docker, analise as afirmativas a seguir:  

I. A instrução `EXPOSE 8080` em um Dockerfile funciona como documentação formal e intenção de rede entre quem cria e quem executa a imagem, mas não publica efetivamente a porta no sistema hospedeiro sem a utilização da flag `-p` ou `-P` no comando `docker run`.  
II. Por padrão, se a diretiva `USER` não for declarada no Dockerfile, os processos dentro do contêiner executam com privilégios de `root`, o que viola o princípio do privilégio mínimo e amplia a superfície de ataque em cenários de quebra de isolamento (*container breakout*).  
III. A diretiva `USER` impede que o contêiner acesse o hardware de memória RAM do servidor físico.  

Está correto o que se afirma em:

* **A)** I, apenas.
* **B)** III, apenas.
* **C)** I e II, apenas.
* **D)** II e III, apenas.
* **E)** I, II e III.

> **Comentário Detalhado:**
>
> - **I. Correta.** `EXPOSE` não mapeia portas no host; ela apenas documenta que o contêiner escuta naquela porta. A publicação real exige o bind explícito `-p 8080:8080` no `docker run`.
> - **II. Correta.** A execução padrão como usuário `root` dentro do contêiner é um risco clássico; a melhor prática é criar um usuário sem privilégios (ex: `RUN adduser -D appuser && USER appuser`).
> - **III. Incorreta.** `USER` afeta apenas permissões de segurança de usuário/UID, não o acesso a hardware de memória.
>
> **Gabarito: C**"""
    },
    {
        "target_sec": "### 4.1 Drivers de Rede: bridge, host, none, overlay e macvlan",
        "question_text": """### Questão 10
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
O subsistema de redes do Docker provê múltiplos *drivers* para atender a diferentes requisitos de isolamento e desempenho. O driver de rede padrão utilizado pelo Docker para comunicação entre contêineres executando na mesma máquina host isolada, criando uma ponte virtual de rede interna, é o driver:

* **A)** `host`
* **B)** `bridge`
* **C)** `none`
* **D)** `overlay`
* **E)** `macvlan`

> **Comentário Detalhado:**
>
> - **A) Incorreta.** O driver `host` remove o isolamento de rede entre o contêiner e o host, compartilhando a pilha de rede diretamente (sem NAT).
> - **B) Correta.** O driver `bridge` é o padrão para nós únicos: cria uma interface de rede virtual privada (como a `docker0`) e atribui endereços IP internos aos contêineres na sub-rede privada, com isolamento e encaminhamento via regras de iptables/NAT.
> - **C) Incorreta.** O driver `none` desabilita completamente a pilha de rede do contêiner (apenas interface de loopback `lo`).
> - **D) Incorreta.** O driver `overlay` é utilizado para comunicação multi-host entre diferentes nós de um cluster (Docker Swarm).
> - **E) Incorreta.** O `macvlan` atribui um endereço MAC físico direto ao contêiner na rede física corporativa.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 5.1 Estrutura do Manifesto Compose: Services, Networks, Volumes e depends_on",
        "question_text": """### Questão 11
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
O Docker Compose permite definir e executar aplicações multi-contêiner utilizando manifestos declarativos no formato YAML (como `compose.yaml` ou `docker-compose.yml`). Em relação aos elementos estruturais desse manifesto, é correto afirmar:

* **A)** A chave de nível superior `services` define o conjunto de contêineres que compõem a aplicação (como uma API web e um banco de dados), permitindo configurar imagens, portas expostas, variáveis de ambiente, volumes e redes associadas.
* **B)** O Docker Compose exige que todos os contêineres executem obrigatoriamente a mesma imagem com o mesmo nome.
* **C)** A diretiva `depends_on` aguarda que a aplicação interna do banco de dados conclua todas as suas migrações e consultas SQL antes de subir a API.
* **D)** Manifestos Compose não suportam a criação de redes virtuais isoladas entre serviços.
* **E)** O arquivo `docker-compose.yml` deve ser escrito obrigatoriamente em linguagem XML.

> **Comentário Detalhado:**
>
> - **A) Correta.** A seção `services` é o núcleo do arquivo Compose, onde cada serviço declara suas configurações operacionais (build/image, environment, ports, volumes, networks, restart).
> - **B) Incorreta.** Serviços podem executar imagens completamente distintas e heterogêneas.
> - **C) Incorreta.** `depends_on` controla apenas a ordem de inicialização dos contêineres (*container startup*), não garantindo que o serviço interno da aplicação esteja pronto para conexões sem um *healthcheck* associado.
> - **D) Incorreta.** Suporta a criação de redes personalizadas na seção `networks`.
> - **E) Incorreta.** O formato padrão e exclusivo é YAML.
>
> **Gabarito: A**"""
    }
]

# ==========================================
# FILE 4: 04_orquestracao_com_kubernetes_e_gestao_de_ambientes.md
# ==========================================
file_4 = "fontes_de_estudo/conhecimentos_especificos_b02_ti/07_devops_e_plataforma_de_entrega/04_orquestracao_com_kubernetes_e_gestao_de_ambientes.md"
injections_4 = [
    {
        "target_sec": "### 1.1 Componentes do Plano de Controle (Control Plane)",
        "question_text": """### Questão 06
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
A arquitetura do Kubernetes é dividida entre o Plano de Controle (*Control Plane*) e os Nós de Execução (*Worker Nodes*). O componente central do *Control Plane* que atua como o único banco de dados de armazenamento consistente e altamente disponível, guardando todo o estado do cluster, suas configurações e especificações de objetos no modelo chave-valor, é o:

* **A)** `kube-scheduler`
* **B)** `etcd`
* **C)** `kube-apiserver`
* **D)** `kubelet`
* **E)** `kube-proxy`

> **Comentário Detalhado:**
>
> - **A) Incorreta.** O `kube-scheduler` analisa os nós e decide em qual nó cada Pod deve ser executado.
> - **B) Correta.** O **`etcd`** é um banco de dados distribuído de chave-valor consistente e de alta disponibilidade (baseado no algoritmo de consenso Raft) que armazena todos os dados do cluster Kubernetes como a fonte única da verdade.
> - **C) Incorreta.** O `kube-apiserver` é a porta de entrada da API que se comunica com o etcd.
> - **D) Incorreta.** O `kubelet` é o agente que executa nos nós de trabalho (*Worker Nodes*).
> - **E) Incorreta.** O `kube-proxy` gerencia as regras de rede nos nós de trabalho.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 1.3 O Loop de Reconciliação Contínua e o Estado Desejado",
        "question_text": """### Questão 07
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
O modelo operacional do Kubernetes é fundamentado no princípio do Loop de Reconciliação Contínua (*Reconciliation Loop*). Esse mecanismo arquitetural opera continuamente por meio da seguinte dinâmica:

* **A)** O administrador digita comandos no terminal a cada dez segundos para manter os servidores ligados.
* **B)** Os controladores (*controllers*) observam o estado atual do cluster (*current state*), comparam-no com o estado desejado (*desired state*) declarado nos manifestos de configuração e executam ações automatizadas de convergência para fazer com que o estado atual se iguale ao estado desejado.
* **C)** O cluster apaga todos os bancos de dados caso a energia elétrica oscile.
* **D)** O sistema interrompe todo o tráfego de rede caso detecte um Pod com consumo de memória inferior a 50%.
* **E)** Os servidores são formatados diariamente para eliminar arquivos temporários.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** O processo é 100% autônomo e contínuo.
> - **B) Correta.** É o cerne da automação do Kubernetes: o usuário declara o estado desejado (ex: "desejo 5 réplicas do Pod X"). O controlador monitora a realidade: se um nó cai e sobram apenas 4 pods, o controlador detecta a discrepância e dispara a criação de um novo Pod imediatamente para restabelecer as 5 réplicas (*self-healing* declarativo).
> - **C) Incorreta.** Kubernetes provê resiliência e alta disponibilidade.
> - **D) Incorreta.** Comportamento inexistente.
> - **E) Incorreta.** Afirmação absurda.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 2.2 Deployment e ReplicaSet: Gerenciamento Declarativo para Aplicações Stateless",
        "question_text": """### Questão 08
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
Para implantar e gerenciar aplicações sem estado (*stateless*) em clusters Kubernetes, o controlador de carga de trabalho recomendado como padrão na arquitetura é o **Deployment**. A relação estrutural entre um objeto *Deployment* e os objetos *ReplicaSets* e *Pods* sob sua gestão estabelece que:

* **A)** O Deployment gerencia diretamente contêineres individuais sem a existência de Pods.
* **B)** O Deployment gerencia versões de ReplicaSets (criando novos ReplicaSets durante atualizações de versão e mantendo os antigos para viabilizar *rollbacks* rápidos), e os ReplicaSets garantem a quantidade declarada de réplicas ativas dos Pods em execução.
* **C)** O ReplicaSet comanda o Deployment em uma hierarquia invertida.
* **D)** Cada Deployment só pode conter um único Pod no cluster inteiro.
* **E)** O Deployment exige que a aplicação utilize armazenamento físico em disquetes de alta densidade.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** A menor unidade gerenciável no Kubernetes é o Pod, nunca contêineres soltos.
> - **B) Correta.** A hierarquia canônica de workloads *stateless*: **Deployment $\\rightarrow$ ReplicaSet $\\rightarrow$ Pods**. Ao atualizar a imagem de um Deployment, ele cria um novo ReplicaSet e migra as réplicas progressivamente (*RollingUpdate*), permitindo voltar à versão anterior (*rollback*) instantaneamente apenas reativando o ReplicaSet anterior.
> - **C) Incorreta.** O Deployment situa-se acima do ReplicaSet.
> - **D) Incorreta.** Suporta dezenas ou centenas de réplicas escaladas horizontalmente.
> - **E) Incorreta.** Afirmação absurda.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 2.4 DaemonSet: Instância Única por Nó de Infraestrutura",
        "question_text": """### Questão 09
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
Em um cluster Kubernetes corporativo, a equipe de operações necessita assegurar que exatamente uma cópia de um Pod de coleta de logs (como o Fluentd) e de um agente de monitoramento de infraestrutura execute em **todos** os nós de trabalho (*Worker Nodes*), inclusive sendo provisionado automaticamente em novos nós adicionados ao cluster. O objeto controlador do Kubernetes concebido especificamente para esse propósito é o:

* **A)** *Job*
* **B)** *StatefulSet*
* **C)** *DaemonSet*
* **D)** *ReplicaSet*
* **E)** *CronJob*

> **Comentário Detalhado:**
>
> - **A) Incorreta.** *Job* executa tarefas em lote que finalizam após a conclusão com sucesso.
> - **B) Incorreta.** *StatefulSet* gerencia cargas com estado e identificadores ordinais fixos.
> - **C) Correta.** O **`DaemonSet`** garante que todos (ou alguns nós específicos) executem exatamente uma réplica do Pod. Quando novos nós entram no cluster, o DaemonSet aloca o Pod neles automaticamente; se um nó é removido, o Pod é destruído (padrão ideal para agentes de log, métricas e storage da infraestrutura).
> - **D) Incorreta.** *ReplicaSet* distribui réplicas arbitrariamente pelo cluster conforme capacidade.
> - **E) Incorreta.** *CronJob* executa Jobs periodicamente com base em agendamentos cron.
>
> **Gabarito: C**"""
    },
    {
        "target_sec": "### 3.1 Tipos de Services: ClusterIP, NodePort, LoadBalancer e ExternalName",
        "question_text": """### Questão 10
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
Os objetos do tipo *Service* no Kubernetes fornecem abstração de rede estável e balanceamento de carga para conjuntos dinâmicos de Pods. O tipo de *Service* padrão, que atribui um endereço IP virtual interno alcançável exclusivamente dentro dos limites do cluster, denomina-se:

* **A)** `NodePort`
* **B)** `ClusterIP`
* **C)** `LoadBalancer`
* **D)** `ExternalName`
* **E)** `IngressController`

> **Comentário Detalhado:**
>
> - **A) Incorreta.** `NodePort` expõe o serviço em uma porta estática (faixa 30000-32767) em cada nó do cluster para acesso externo.
> - **B) Correta.** O **`ClusterIP`** é o tipo padrão (*default*): aloca um IP virtual estável roteável apenas internamente na rede do cluster, perfeito para comunicação interna entre microsserviços (ex: backend acessando o banco de dados).
> - **C) Incorreta.** `LoadBalancer` provisiona um balanceador de carga público externo gerenciado pelo provedor de nuvem (GCP, AWS, Azure).
> - **D) Incorreta.** `ExternalName` mapeia o Service para um registro CNAME DNS externo.
> - **E) Incorreta.** Ingress Controller é um controlador de roteamento de borda (L7), não um tipo de Service.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 5.1 ConfigMaps e Secrets: Injeção Desacoplada de Configurações",
        "question_text": """### Questão 11
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
Em conformidade com a metodologia dos Doze Fatores (*Twelve-Factor App*), a configuração de uma aplicação deve ser estritamente separada do código-fonte. No Kubernetes, essa segregação é implementada por meio de dois objetos nativos: *ConfigMaps* e *Secrets*. A diferença fundamental de propósito entre eles estabelece que:

* **A)** *ConfigMaps* armazenam dados confidenciais criptografados, enquanto *Secrets* guardam arquivos de imagem públicos sem restrição.
* **B)** *ConfigMaps* destinam-se a dados de configuração não confidenciais em texto claro (como URLs de endpoints, portas e flags de log), ao passo que *Secrets* são concebidos para armazenar dados confidenciais e credenciais sensíveis (como senhas, chaves de API, tokens e certificados TLS), codificados em Base64 ou protegidos por criptografia em repouso no `etcd`.
* **C)** *Secrets* não podem ser montados como variáveis de ambiente nos Pods.
* **D)** Ambos os objetos são deletados obrigatoriamente a cada 5 minutos pelo Kubernetes.
* **E)** *ConfigMaps* só aceitam configurações escritas em linguagem Pascal.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** Relação de confidencialidade invertida.
> - **B) Correta.** Definição arquitetural exata: **ConfigMaps** para configurações gerais legíveis; **Secrets** para credenciais sensíveis que demandam controle de acesso via RBAC, auditoria de acesso e encriptação no etcd. Ambos podem ser injetados em Pods como variáveis de ambiente ou montados como arquivos em volumes.
> - **C) Incorreta.** Secrets podem ser injetados perfeitamente como variáveis de ambiente via `secretKeyRef` ou `envFrom`.
> - **D) Incorreta.** São objetos persistentes estáveis.
> - **E) Incorreta.** Dados são armazenados como pares chave-valor universais.
>
> **Gabarito: B**"""
    }
]

# ==========================================
# FILE 5: 05_infraestrutura_como_codigo_iac_e_gerenciamento_de_configuracao.md
# ==========================================
file_5 = "fontes_de_estudo/conhecimentos_especificos_b02_ti/07_devops_e_plataforma_de_entrega/05_infraestrutura_como_codigo_iac_e_gerenciamento_de_configuracao.md"
injections_5 = [
    {
        "target_sec": "### 1.2 Paradigma Declarativo (O Quê) vs. Imperativo (Como)",
        "question_text": """### Questão 06
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
Na implementação de Infraestrutura como Código (IaC), as ferramentas podem adotar a abordagem declarativa ou a abordagem imperativa. A característica definidora do paradigma **declarativo** (adotado pelo Terraform e pelo Kubernetes) estabelece que o engenheiro:

* **A)** Descreve uma sequência detalhada e linear de comandos com laços e desvios condicionais que o sistema operacional deve executar passo a passo até a conclusão.
* **B)** Especifica o estado final desejado da infraestrutura ("o quê"), cabendo ao motor da ferramenta calcular automaticamente as diferenças e aplicar as ações necessárias de criação, modificação ou destruição para convergir a infraestrutura real ao estado declarado.
* **C)** Exige que a infraestrutura seja reconfigurada manualmente pela interface gráfica a cada novo deploy.
* **D)** Só permite o provisionamento de servidores desprovidos de conexão de rede.
* **E)** Proíbe o versionamento dos arquivos de código no Git.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** Descrever o passo a passo procedimental sequencial ("como") é a essência do paradigma **imperativo** (típico de scripts Bash/Python ou CLI pura).
> - **B) Correta.** No paradigma **declarativo**, o desenvolvedor declara a meta final (ex: "preciso de uma VPC com 3 sub-redes e 2 instâncias"). O Terraform calcula a diferença (*diff*) entre a realidade e o manifesto e descobre autonomamente a ordem de dependências e os comandos necessários para alcançar o resultado.
> - **C) Incorreta.** A premissa de IaC é eliminar a configuração manual (*ClickOps*).
> - **D) Incorreta.** Provisiona redes completas.
> - **E) Incorreta.** Manifestos declarativos devem ser versionados sob controle estrito no Git.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 2.1 Estrutura e Blocos Fundamentais da Linguagem HCL",
        "question_text": """### Questão 07
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
O Terraform utiliza a linguagem declarativa HCL (*HashiCorp Configuration Language*). No manifesto HCL, o bloco utilizado especificamente para consultar e extrair informações de recursos que já existem previamente na nuvem (sem gerenciá-los diretamente como novas criações do código corrente) é o bloco:

* **A)** `resource`
* **B)** `variable`
* **C)** `output`
* **D)** `data`
* **E)** `provider`

> **Comentário Detalhado:**
>
> - **A) Incorreta.** O bloco `resource` declara e gerencia a criação de um novo componente de infraestrutura sob custódia do Terraform.
> - **B) Incorreta.** `variable` define parâmetros de entrada customizáveis.
> - **C) Incorreta.** `output` expõe valores de saída calculados para outros módulos ou usuários.
> - **D) Correta.** O bloco **`data`** (*Data Source*) permite consultar e importar metadados de recursos pré-existentes na nuvem (ex: buscar o ID de uma imagem de VM oficial ou o IP de uma sub-rede corporativa existente) para uso dentro do manifesto Terraform.
> - **E) Incorreta.** `provider` configura o plugin de conexão com a plataforma alvo (ex: AWS, Google Cloud, Azure).
>
> **Gabarito: D**"""
    },
    {
        "target_sec": "### 2.2 O Arquivo de Estado (`terraform.tfstate`), Remote Backend e State Locking",
        "question_text": """### Questão 08
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
Em ambientes corporativos onde múltiplos engenheiros colaboram nos mesmos manifestos de infraestrutura Terraform, a configuração de um *Remote Backend* com suporte a *State Locking* (travamento de estado) é mandatória. A razão técnica precípua do *State Locking* consiste em:

* **A)** Impedir que o código-fonte Terraform seja lido por engenheiros que utilizam o sistema operacional Linux.
* **B)** Prevenir a corrupção do arquivo de estado (`terraform.tfstate`) decorrente de execuções concorrentes de comandos `terraform apply`, travando o estado com uma chave exclusiva enquanto uma operação de escrita estiver em andamento.
* **C)** Bloquear todas as portas de firewall da nuvem permanentemente.
* **D)** Acelerar a velocidade de download de imagens Docker em 500%.
* **E)** Excluir automaticamente os backups de dados após cada modificação.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** O Terraform é amplamente multiplataforma.
> - **B) Correta.** Se dois engenheiros (ou dois pipelines de CI/CD simultâneos) executarem `terraform apply` ao mesmo tempo sobre o mesmo arquivo de estado sem travamento, ocorreria condição de corrida (*race condition*), corrompendo o mapeamento de recursos do `terraform.tfstate`. Mecanismos como Cloud Storage / S3 com DynamoDB provêm *State Locking*, garantindo atomicidade e segurança transacional.
> - **C) Incorreta.** Não afeta as regras de firewall da nuvem.
> - **D) Incorreta.** Sem relação com imagens Docker.
> - **E) Incorreta.** O estado remoto mantém versionamento de backups.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 3.2 Matriz Comparativa Detalhada: Ansible vs. Puppet vs. Chef",
        "question_text": """### Questão 09
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
Entre as principais ferramentas de gerenciamento de configuração de servidores na cultura DevOps, o Ansible diferencia-se historicamente de ferramentas como Puppet e Chef por adotar uma arquitetura:

* **A)** Baseada em agentes locais pesados instalados em todos os servidores alvos operando em modelo *pull*.
* **B)** Sem agentes (*Agentless*), operando em modelo *push* no qual o nó de controle conecta-se aos nós gerenciados via protocolo SSH padrão (ou WinRM no Windows) e executa módulos descritos em manifestos YAML (*Playbooks*), dispensando a manutenção de daemons residentes nos nós alvos.
* **C)** Que só permite o gerenciamento de servidores baseados no sistema operacional MS-DOS.
* **D)** Totalmente dependente de conexão física com cabos seriais RS-232.
* **E)** Que exige a compilação do código em linguagem C++ antes de cada comando.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** Puppet e Chef tradicionalmente dependem de agentes residentes (*agent-based*) e arquitetura *pull*.
> - **B) Correta.** O grande diferencial do Ansible é ser **Agentless** e **Push-based**: não requer instalação, atualização ou monitoramento de software agente nos nós gerenciados; utiliza a infraestrutura de comunicação nativa (SSH/WinRM) para empurrar comandos declarativos a partir de playbooks YAML.
> - **C) Incorreta.** Suporta distribuições Linux corporativas e servidores Windows modernos.
> - **D) Incorreta.** Opera sobre redes TCP/IP padrão.
> - **E) Incorreta.** Playbooks são interpretados em tempo de execução via Python/YAML.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 3.4 Sinergia Arquitetural: Terraform no Provisionamento + Ansible na Configuração",
        "question_text": """### Questão 10
**(FCC – TCE – Auditor de Controle Externo / Tecnologia da Informação)**  
Na arquitetura de entrega contínua moderna de infraestrutura, a sinergia entre ferramentas de provisionamento e ferramentas de gerenciamento de configuração é amplamente recomendada pela divisão de papéis:

* **A)** O Ansible deve ser usado para criar switches físicos e o Terraform para formatar pen drives.
* **B)** O Terraform é a ferramenta ideal para o provisionamento e ciclo de vida da infraestrutura básica (redes VPC, sub-redes, instâncias de VM, clusters Kubernetes e storages gerenciados), ao passo que o Ansible atua na etapa subsequente para gerenciar a configuração interna dos servidores (instalação de pacotes, usuários, arquivos de configuração e serviços do sistema operacional).
* **C)** O uso combinado de Terraform e Ansible é estritamente proibido pelos padrões de arquitetura de nuvem pública.
* **D)** O Terraform só pode ser utilizado se todos os servidores forem mantidos em infraestrutura local própria (*on-premise*).
* **E)** Ambas as ferramentas devem ser substituídas permanentemente pela edição manual de arquivos no bloco de notas.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** Descrição fantasiosa.
> - **B) Correta.** Essa é a arquitetura de referência canônica da indústria DevOps: **Terraform para Provisionamento** (cria o hardware virtual e componentes em nuvem) e **Ansible para Configuração** (configura o sistema operacional e softwares no interior das máquinas instanciadas), aproveitando o melhor de cada ferramenta.
> - **C) Incorreta.** É uma das combinações mais celebradas do mercado.
> - **D) Incorreta.** O Terraform nasceu e domina o provisionamento em nuvem pública (AWS, GCP, Azure).
> - **E) Incorreta.** A edição manual viola todos os preceitos de IaC.
>
> **Gabarito: B**"""
    }
]

# ==========================================
# FILE 6: 06_observabilidade_monitoramento_e_telemetria.md
# ==========================================
file_6 = "fontes_de_estudo/conhecimentos_especificos_b02_ti/07_devops_e_plataforma_de_entrega/06_observabilidade_monitoramento_e_telemetria.md"
injections_6 = [
    {
        "target_sec": "### 1.1 Transição de Sintomas para Estados Internos",
        "question_text": """### Questão 06
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
Na engenharia de sistemas modernos, a distinção conceitual entre o Monitoramento Tradicional e a Observabilidade Moderna fundamenta-se na teoria do controle. A respeito dessa distinção, é correto afirmar:

* **A)** O monitoramento tradicional testa os sistemas internamente com inteligência artificial, enquanto a observabilidade analisa exclusivamente se o computador está ligado à tomada.
* **B)** O monitoramento tradicional foca em verificar sintomas e métricas pré-conhecidas de falha ("o sistema está funcionando?"), respondendo por problemas conhecidos (*known unknowns*); a observabilidade é a propriedade de inferir os estados internos de um sistema complexo exclusivamente a partir de suas saídas de telemetria externa, permitindo diagnosticar comportamentos inéditos e inesperados (*unknown unknowns*).
* **C)** Observabilidade e monitoramento são termos rigorosamente sinônimos, não havendo qualquer distinção técnica ou arquitetural entre ambos.
* **D)** A observabilidade exige o desligamento de todos os agentes de telemetria de produção.
* **E)** O monitoramento tradicional é capaz de isolar falhas de concorrência em sistemas distribuídos de microsserviços sem necessidade de logs ou traces.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** Relação invertida e simplória.
> - **B) Correta.** Definição clássica de Charity Majors e da literatura SRE: o monitoramento tradicional avisa quando algo quebrou baseado em limites pré-definidos (*thresholds* e alertas de sintomas conhecidos). A **Observabilidade** mede quão bem você consegue compreender o estado interno de um sistema complexo examinando apenas suas saídas de telemetria (métricas, logs, traces), sendo essencial para desvendar causas inéditas em sistemas distribuídos (*unknown unknowns*).
> - **C) Incorreta.** Há clara distinção de escopo e capacidade diagnóstica.
> - **D) Incorreta.** A observabilidade alimenta-se diretamente da telemetria.
> - **E) Incorreta.** Sistemas distribuídos demandam rastreamento distribuído e alta cardinalidade que o monitoramento tradicional não suporta.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 1.3 Metodologias Complementares: USE (Brendan Gregg) e RED (Tom Wilkie)",
        "question_text": """### Questão 07
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
No diagnóstico de desempenho de sistemas computacionais, duas metodologias de telemetria consagradas são o método **USE** (proposto por Brendan Gregg) e o método **RED** (proposto por Tom Wilkie). A correta caracterização dessas metodologias estabelece que:

* **A)** O método USE aplica-se a requisições de microsserviços e o método RED foca em memórias ROM analógicas.
* **B)** O método USE orienta-se a recursos físicos de infraestrutura e hardware, analisando a **Utilização** (% de tempo ocupado), a **Saturação** (filas de espera de trabalho reprimido) e os **Erros** de cada recurso; o método RED orienta-se a serviços e requisições de software, medindo a Taxa de Requisições (**Rate**), a Taxa de Falhas (**Errors**) e a Duração (**Duration** / tempo de resposta).
* **C)** O método RED mede exclusivamente o consumo de energia elétrica em watts dos servidores.
* **D)** Ambas as metodologias recomendam que a saturação dos discos seja mantida permanentemente em 100%.
* **E)** O método USE proíbe o registro de erros em sistemas de arquivos.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** A relação de foco está invertida.
> - **B) Correta.** É a divisão clássica da engenharia de observabilidade:
>   - **USE Method (Brendan Gregg):** foca em **recursos** (CPU, memória, disco, interfaces de rede): *Utilization, Saturation, Errors*;
>   - **RED Method (Tom Wilkie):** foca em **serviços e transações** (APIs e microsserviços): *Rate* (requisições por segundo), *Errors* (falhas por segundo) e *Duration* (latência/tempo gasto).
> - **C) Incorreta.** RED mede tráfego, erros e duração de requisições de software.
> - **D) Incorreta.** Saturação alta indica gargalo severo e filas reprimidas.
> - **E) Incorreta.** Erros são o terceiro elemento obrigatório do método USE.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 2.2 Logs Estruturados (Structured Logging) e Pilhas de Agregação (ELK, EFK, Loki)",
        "question_text": """### Questão 08
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
Em arquiteturas de microsserviços de grande escala, a substituição de logs em texto livre não estruturado por Logs Estruturados (*Structured Logging*, tipicamente formatados em JSON) é uma exigência essencial de observabilidade. A principal vantagem dos logs estruturados consiste em:

* **A)** Impedir que o arquivo de log seja aberto por editores de texto no sistema hospedeiro.
* **B)** Permitir a indexação eficiente de pares chave-valor (como `timestamp`, `level`, `user_id`, `trace_id` e `http_status`), viabilizando consultas analíticas rápidas, correlações precisas e agregações estatísticas por ferramentas de ingestão centralizada (como Elasticsearch, OpenSearch e Grafana Loki).
* **C)** Forçar que todos os logs sejam gravados exclusivamente em caixas de som de alta potência.
* **D)** Aumentar a quantidade de erros da aplicação para gerar mais alertas à gerência.
* **E)** Excluir automaticamente os rastros de auditoria fiscal a cada transação bancária.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** Arquivos JSON continuam sendo texto legível por humanos.
> - **B) Correta.** Logs estruturados padronizam as mensagens em JSON (`{"level": "ERROR", "trace_id": "abc-123", "duration_ms": 42}`). Isso transforma dados textuais caóticos em registros parseáveis e consultáveis instantaneamente por motores de busca e agregação, possibilitando correlações cruzadas e métricas em tempo real.
> - **C) Incorreta.** Afirmação absurda.
> - **D) Incorreta.** Não há geração forçada de erros.
> - **E) Incorreta.** Registros de auditoria devem ser preservados com integridade.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 3.1 Arquitetura Unificada: OTel API, OTel SDK e OTel Collector",
        "question_text": """### Questão 09
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
O OpenTelemetry (OTel), projeto incubado pela Cloud Native Computing Foundation (CNCF), consolidou-se como o padrão aberto da indústria para instrumentação e coleta de telemetria unificada (métricas, logs e traces). A arquitetura do OpenTelemetry estabelece uma separação clara entre:

* **A)** A API do OpenTelemetry (que fornece as interfaces e contratos de instrumentação agnósticos no código da aplicação, sem dependência de implementações concretas) e o SDK do OpenTelemetry (que implementa a API, gerenciando amostragem, buffers de memória e exportação de dados para coletores ou backends analíticos).
* **B)** O monitor de vídeo LCD e a memória cache do processador.
* **C)** O protocolo HTTP e os cabos de energia elétrica de corrente contínua.
* **D)** O sistema de arquivos Windows FAT32 e os discos de estado sólido NVMe.
* **E)** As linguagens de programação funcionais e os bancos de dados não relacionais NoSQL.

> **Comentário Detalhado:**
>
> - **A) Correta.** A separação formal entre **OpenTelemetry API** e **OpenTelemetry SDK** é uma das maiores elegâncias arquiteturais do projeto: as bibliotecas e frameworks de terceiros só precisam depender da API (contrato abstrato estável), sem amarrar a aplicação a nenhum fornecedor. A aplicação final acopla o SDK para configurar para onde e como os dados serão exportados.
> - **B) Incorreta.** Componentes de hardware.
> - **C) Incorreta.** Protocolos de rede vs eletricidade.
> - **D) Incorreta.** Sistemas de arquivos e storage.
> - **E) Incorreta.** Paradigmas conceituais genéricos.
>
> **Gabarito: A**"""
    },
    {
        "target_sec": "### 4.2 O Orçamento de Erro (Error Budget) como Equilíbrio entre Inovação e Confiabilidade",
        "question_text": """### Questão 10
**(FCC – TCE – Auditor de Controle Externo / Tecnologia da Informação)**  
Na Engenharia de Confiabilidade de Sites (*Site Reliability Engineering* - SRE), o conceito de Orçamento de Erro (*Error Budget*) é a métrica reguladora fundamental que equilibra o ritmo de inovação das equipes de produto com a estabilidade do sistema. Matematicamente e operacionalmente, o Orçamento de Erro é definido como:

* **A)** A quantia financeira em dólares destinada a pagar multas judiciais decorrentes de vazamento de senhas.
* **B)** A fração de indisponibilidade ou falhas toleradas pelo objetivo acordado de nível de serviço, calculada formalmente como $100\\% - SLO$; enquanto houver saldo positivo no Orçamento de Erro, a equipe pode realizar novos lançamentos arriscados em produção, mas caso o saldo seja consumido antes do fim da janela temporal, novos lançamentos são congelados e o esforço técnico é redirecionado para confiabilidade e correções.
* **C)** A quantidade máxima de linhas de código com defeito que um desenvolvedor pode comitar por hora de trabalho.
* **D)** A taxa de juros bancários cobrada por transações financeiras com cartão de crédito corporativo.
* **E)** O número total de computadores queimados em um ano de operação do data center.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** O Error Budget é uma métrica de engenharia de confiabilidade temporal, não um fundo financeiro de multas.
> - **B) Correta.** É a célebre definição do Google SRE: se o SLO (*Service Level Objective*) é de $99,9\\%$, o **Error Budget** é de $0,1\\%$ de falhas toleradas no período. Esse orçamento transforma a discussão política entre Produto (que quer velocidade) e Operações (que quer estabilidade) em uma regra matemática compartilhada: se há orçamento sobrando, libera-se a inovação; se o orçamento estourou, congelam-se novos deploys para focar em estabilização.
> - **C) Incorreta.** Métrica sem fundamento técnico.
> - **D) Incorreta.** Conceito financeiro bancário.
> - **E) Incorreta.** Perda de hardware físico.
>
> **Gabarito: B**"""
    }
]

print("Injecting into Module 07...")
inject_questions_into_file(file_1, injections_1)
inject_questions_into_file(file_2, injections_2)
inject_questions_into_file(file_3, injections_3)
inject_questions_into_file(file_4, injections_4)
inject_questions_into_file(file_5, injections_5)
inject_questions_into_file(file_6, injections_6)
print("\nModule 07 completed successfully!")
