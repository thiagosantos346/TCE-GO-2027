# -*- coding: utf-8 -*-
"""
Script to enrich Module 11 (Sistemas Operacionais, Redes e Nuvem)
Files 01 to 05. Adds Questions 06 to 11 to each file (total 11 questions each).
Preserves existing questions 01-05 and all diagrams/formatting.
"""

import os
import re

BASE_DIR = "fontes_de_estudo/conhecimentos_especificos_b02_ti/11_sistemas_operacionais_redes_e_nuvem"

def check_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    qs = re.findall(r"### Questão \d+", content)
    return len(qs), content

# ==============================================================================
# FILE 01: 01_sistemas_operacionais_linux_e_windows.md
# ==============================================================================
def enrich_file_01():
    path = os.path.join(BASE_DIR, "01_sistemas_operacionais_linux_e_windows.md")
    count, content = check_file(path)
    if count >= 10:
        print(f"File 01 already has {count} questions, skipping.")
        return

    q06 = """### Questão 06 (FGV - TRT / Analista Judiciário - TI - Modos de Operação do Processador: User vs. Kernel)
A arquitetura de processadores modernos e sistemas operacionais de uso geral (como Linux e Windows) implementa anéis de proteção (*protection rings*) em hardware para segregar a execução de programas e garantir a estabilidade do sistema.

A respeito dos modos de operação do processador (**User Mode / Modo Usuário** e **Kernel Mode / Modo Núcleo**) e da transição entre eles, assinale a afirmativa correta:

* **A)** Softwares aplicativos de usuários comuns (como navegadores e suítes de escritório) rodam diretamente em Modo Núcleo (*Kernel Mode / Ring 0*), possuindo acesso irrestrito e direto a qualquer endereço físico de memória RAM e portas de I/O da máquina.
* **B)** A transição segura do Modo Usuário (*Ring 3*) para o Modo Núcleo (*Ring 0*) ocorre por meio de uma instrução especial de **Chamada de Sistema (*System Call / Trap*)**, na qual o hardware suspende a execução do processo, eleva o nível de privilégio e transfere o controle para um tratador específico (*Interrupt/Syscall Handler*) definido pelo kernel.
* **C)** No modo usuário, um programa tem autorização de hardware para desabilitar as interrupções de relógio da CPU e reconfigurar os registradores de controle de gerenciamento de memória.
* **D)** As chamadas de sistema dispensam qualquer troca de contexto de registradores na CPU, mantendo a pilha de execução inalterada.
* **E)** Sistemas operacionais modernos eliminaram o modo núcleo para rodar todo o código exclusivamente em máquinas virtuais JavaScript.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Aplicações de usuário rodam estritamente em **Modo Usuário (Ring 3)** com privilégios restritos; se tentarem executar instruções privilegiadas ou acessar memória do kernel diretamente, o processador dispara uma exceção de violação de proteção (*General Protection Fault* / *Segmentation Fault*).
> - **B)** **CORRETA.** Mecânica de isolamento e proteção de hardware:
>   - **Dual-Mode Operation:** Processadores x86/x64 implementam níveis de privilégio (sendo Ring 0 o mais privilegiado e Ring 3 o menos privilegiado).
>   - Para ler um arquivo, enviar um pacote de rede ou alocar memória física, o processo de usuário deve invocar uma **Chamada de Sistema (Syscall)**.
>   - O hardware aciona uma interrupção de software (*trap*), comuta o registrador de modo do processador de *User* para *Kernel*, salva o contexto da aplicação e salta para o endereço do despachante de chamadas de sistema na tabela do kernel, executando a operação com privilégios controlados antes de retornar o resultado ao modo usuário.
> - **C)** Incorreta. Instruções como `CLI` (desabilitar interrupções) são estritamente privilegiadas de Ring 0.
> - **D)** Incorreta. A transição exige salvar o contador de programa (PC), ponteiro de pilha (SP) e registradores na pilha do kernel.
> - **E)** Incorreta. O Kernel Mode permanece como pilar mandatório de qualquer arquitetura de computadores moderna.
> 
> **Gabarito: B**

---
"""

    q07 = """### Questão 07 (FCC - TRT / Analista Judiciário - TI - Processos vs. Threads)
No gerenciamento de processos e concorrência em sistemas operacionais multitarefa preemptivos, diferencia-se o conceito de **Processo Pesado** do conceito de **Thread** (*Processo Leve*).

A respeito do compartilhamento de recursos entre múltiplas threads pertencentes a um mesmo processo, assinale a afirmativa correta:

* **A)** Múltiplas threads do mesmo processo possuem, cada uma, um espaço de endereçamento de memória virtual totalmente isolado e tabelas de páginas exclusivas sem nenhum dado compartilhado.
* **B)** Todas as threads pertencentes a um mesmo processo compartilham o **espaço de endereçamento de memória**, as seções de código (*text*), os dados globais (*data/BSS*), a área de alocação dinâmica (*heap*) e os descritores de arquivos abertos; contudo, cada thread possui compulsoriamente sua própria **Pilha de Execução (*Stack*)**, seu próprio ponteiro de instrução (*Program Counter - PC*) e seu próprio conjunto individual de **Registradores da CPU**.
* **C)** A criação e a troca de contexto entre threads consomem mais tempo de CPU do que a criação e a troca de contexto entre processos pesados distintos.
* **D)** Se uma thread de um processo trava por erro de divisão por zero, as outras threads daquele mesmo processo continuam operando normalmente sem que o processo seja finalizado.
* **E)** Threads não podem ser executadas em núcleos de processadores diferentes (*multicore*), sendo restritas a um único clock de CPU compartilhado.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Esse isolamento total de memória é a característica definidora entre **processos diferentes**, e não entre threads do mesmo processo.
> - **B)** **CORRETA.** Modelo canônico de processos e threads (Silberschatz / Tanenbaum):
>   - **Recursos Compartilhados (Nível do Processo):** Espaço de endereçamento virtual completo, código executável, variáveis globais e estáticas, *Heap*, descritores de arquivos abertos e conexões de rede. Isso viabiliza comunicação ultrarrápida entre threads via memória compartilhada sem necessidade de IPC pesado.
>   - **Recursos Exclusivos (Nível da Thread):** Cada thread precisa de independência de fluxo de execução; logo, possui seu próprio **ID de Thread (TID)**, seu próprio conjunto de **registradores da CPU**, seu próprio **Program Counter (PC)** para saber qual instrução está executando, e sua própria **Stack (Pilha)** para gerenciar variáveis locais e chamadas de função.
> - **C)** Incorreta. Troca de contexto entre threads do mesmo processo é muito mais rápida porque **não exige a troca da tabela de páginas na MMU** nem invalidação do cache TLB.
> - **D)** Incorreta. Como compartilham o mesmo espaço de memória, se uma thread provocar corrupção fatal de memória (*Segmentation Fault*), o sistema operacional encerra o processo inteiro, derrubando todas as threads associadas.
> - **E)** Incorreta. Threads de kernel podem ser distribuídas concorrentemente em múltiplos núcleos e sockets de CPU.
> 
> **Gabarito: B**

---
"""

    q08 = """### Questão 08 (FGV - TRT / Analista Judiciário - TI - Sincronização e Exclusão Mútua: Mutex vs. Semáforos)
Em programação concorrente e em sistemas operacionais multithreaded, o acesso não coordenado a recursos compartilhados pode gerar **Condições de Corrida** (*Race Conditions*), corrompendo o estado da aplicação.

Para garantir a **Exclusão Mútua** na Região Crítica, utilizam-se primitivas de sincronização como **Mutex** (*Mutual Exclusion Lock*) e **Semáforos** (Dijkstra). A respeito da distinção conceitual e do funcionamento dessas primitivas, assinale a afirmativa correta:

* **A)** O Mutex é um mecanismo binário com conceito estrito de titularidade (*ownership*), no qual apenas a thread específica que adquiriu a trava (*Lock*) possui autorização para liberá-la (*Unlock*); ao passo que um **Semáforo Contador** gerencia um contador de recursos disponíveis, onde qualquer thread pode executar uma operação de sinalização (`signal` / `V()`) para incrementar o contador e desbloquear outra thread em espera, mesmo sem ter executado a operação de espera (`wait` / `P()`).
* **B)** Semáforos só podem assumir os valores 0 e 1, sendo proibido utilizá-los para controlar estoques de múltiplos recursos.
* **C)** O Mutex deve ser liberado compulsoriamente por qualquer thread da CPU que esteja ociosa no momento.
* **D)** A inversão de prioridades é um fenômeno que afeta exclusivamente semáforos contadores de números negativos.
* **E)** Bloqueios do tipo *Spinlock* colocam a thread para dormir no disco rígido enquanto o recurso estiver ocupado.

> **Comentário Detalhado:**
>
> - **A)** **CORRETA.** Distinção precisa entre Mutex e Semáforos:
>   - **Mutex (Mutual Exclusion Lock):** É um mecanismo de travamento com **propriedade (ownership)**. Se a Thread A executa `mutex.acquire()`, **somente a Thread A** tem autorização para executar `mutex.release()`. Se a Thread B tentar liberar o mutex, ocorrerá um erro. É ideal para proteger seções críticas exclusivas.
>   - **Semáforo (Counting Semaphore):** É um mecanismo de **sinalização** baseado em uma variável inteira protegida. A operação `P()` ou `wait()` decrementa o contador (bloqueando se o valor for $\le 0$); a operação `V()` ou `signal()` incrementa o contador. Não há conceito de titularidade: a Thread A pode aguardar a chegada de dados e a Thread B (produtora) pode emitir o sinal `signal()` para acordar a Thread A.
> - **B)** Incorreta. Semáforos contadores podem ser inicializados com qualquer valor inteiro positivo $N$ para disciplinar o acesso a um pool de $N$ recursos.
> - **C)** Incorreta. Mutex exige titularidade estrita da thread que o bloqueou.
> - **D)** Incorreta. A inversão de prioridades ocorre tipicamente com mutexes quando uma tarefa de baixa prioridade retém um recurso demandado por uma tarefa de alta prioridade.
> - **E)** Incorreta. *Spinlocks* realizam espera ocupada (*busy waiting*), consumindo 100% de CPU em loop contínuo testando o bit de trava, sem dormir.
> 
> **Gabarito: A**

---
"""

    q09 = """### Questão 09 (FCC - TRT / Analista Judiciário - TI - Memória Virtual e Hiperpaginação / Thrashing)
O subsistema de Memória Virtual permite que programas sejam executados mesmo quando seu espaço de endereçamento total excede a capacidade física de memória RAM instalada na máquina, transferindo blocos para a área de *Swap* em disco.

No entanto, quando a quantidade de memória RAM disponível torna-se criticamente insuficiente para acomodar o conjunto de trabalho (*Working Set*) de todos os processos ativos simultâneos, o sistema operacional pode entrar no colapso de desempenho denominado **Hiperpaginação (*Thrashing*)**.

A característica operacional que define formalmente o fenômeno do *Thrashing* consiste em:

* **A)** A CPU atinge 100% de utilização processando cálculos matemáticos puros sem nenhum acesso a disco.
* **B)** O sistema passa a maior parte do tempo transferindo páginas de memória de e para o disco rígido (alta taxa ininterrupta de *Page Faults* e saturação de I/O), enquanto a taxa de utilização útil da CPU cai drasticamente para níveis próximos de zero, travando a resposta aos usuários.
* **C)** A destruição física permanente dos módulos de memória RAM por superaquecimento.
* **D)** O fechamento imediato do sistema operacional sem emissão de qualquer log de evento.
* **E)** A conversão de todos os arquivos do disco para formato somente-leitura.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. No *Thrashing*, a CPU fica quase ociosa aguardando operações lentas de leitura e escrita no subsistema de armazenamento.
> - **B)** **CORRETA.** Mecânica do **Thrashing (Hiperpaginação)** (Tanenbaum / Silberschatz):
>   1. Quando a soma dos conjuntos de trabalho (*Working Sets*) dos processos ativos supera a memória RAM física, a taxa de faltas de página (*Page Faults*) explode.
>   2. Cada processo que tenta rodar precisa de páginas que foram descarregadas para o disco de *Swap*. O processo é suspenso aguardando o I/O de disco.
>   3. Como a maioria dos processos entra em estado de espera (*Waiting/Blocked*), o escalonador do SO erroneamente detecta baixa utilização da CPU e pode tentar aumentar o grau de multiprogramação, agravando ainda mais a contenção.
>   4. O sistema entra em parafuso: **quase 100% do tempo do subsistema de disco é consumido trocando páginas entre RAM e Swap**, enquanto a utilização da CPU desaba e o computador para de responder. Soluções: reduzir o grau de multiprogramação (suspender processos) ou adicionar memória RAM física.
> - **C)** Incorreta. Trata-se de um problema puramente lógico de contenção de recursos de software e gerência de memória.
> - **D)** Incorreta. O SO não desliga, fica congelado em sobrecarga de I/O.
> - **E)** Incorreta. O sistema de arquivos não é alterado para somente-leitura.
> 
> **Gabarito: B**

---
"""

    q10 = """### Questão 10 (FCC - TRT / Analista Judiciário - TI - Permissões Octais e Especiais no Linux: SUID, SGID e Sticky Bit)
Nos sistemas de arquivos de ambientes Linux/POSIX, a segurança de arquivos e diretórios é regida pela matriz de permissões associadas ao Proprietário (*User - u*), Grupo (*Group - g*) e Outros (*Others - o*), acrescida dos três bits de permissões especiais: **SUID**, **SGID** e **Sticky Bit**.

Considere um diretório compartilhado de auditoria `/var/auditoria_compartilhada` cujas permissões foram configuradas pelo administrador através do comando:

`chmod 1770 /var/auditoria_compartilhada`

A respeito do significado do primeiro dígito `1` (Sticky Bit) e dos efeitos práticos dessa configuração sobre o diretório, assinale a afirmativa correta:

* **A)** O bit 1 representa o SUID, permitindo que qualquer usuário execute o diretório como se fosse o usuário `root`.
* **B)** O bit 1 representa o **Sticky Bit** (representado pelo caractere `t` no final da string de permissões, ex.: `drwxrwx--t`); em um diretório com o Sticky Bit ativado, embora múltiplos usuários pertencentes ao grupo possam criar e editar arquivos no local, **apenas o proprietário de um arquivo específico (ou o superusuário root) tem permissão de renomear ou excluir o seu próprio arquivo**, impedindo que um usuário do grupo apague documentos criados por seus colegas.
* **C)** O bit 1 bloqueia o acesso de qualquer usuário ao diretório, tornando-o invisível no comando `ls`.
* **D)** O Sticky Bit força que todos os novos arquivos criados herdem compulsoriamente o grupo primário do diretório pai.
* **E)** As permissões 770 atribuem leitura, escrita e execução irrestrita para todos os usuários anônimos do mundo exterior (*others*).

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O valor octal do SUID é **4** (ex.: 4755), enquanto o valor octal do Sticky Bit é **1**.
> - **B)** **CORRETA.** Aplicação canônica das **Permissões Especiais no Linux**:
>   - **Sticky Bit (Bit 1000 em octal):** Quando aplicado a um diretório (como `/tmp` ou pastas compartilhadas de trabalho), restringe a **exclusão e renomeação de arquivos**. Mesmo que a pasta tenha permissão de escrita de grupo (`770`), um membro do grupo NÃO pode deletar arquivos de outro membro; apenas o **dono do arquivo** e o **root** podem remover o item. Representado por `t` (ou `T` se não houver permissão `x`).
>   - **SGID (Bit 2000 em octal):** Em arquivos executáveis, executa com os privilégios do grupo do arquivo; em diretórios, faz com que novos arquivos criados herdem o grupo do diretório pai.
>   - **SUID (Bit 4000 em octal):** Em arquivos executáveis binários (como `/usr/bin/passwd`), faz com que o executável rode com os privilégios do proprietário do arquivo (`root`).
> - **C)** Incorreta. O diretório continua visível e acessível aos usuários autorizados.
> - **D)** Incorreta. Essa é a função do **SGID em diretórios** (bit 2000), e não do Sticky Bit.
> - **E)** Incorreta. O último dígito `0` proíbe expressamente qualquer permissão para *others* (`---`).
> 
> **Gabarito: B**

---
"""

    q11 = """### Questão 11 (FGV - TRT / Analista Judiciário - TI - Gerenciamento de Serviços e Logs no Linux com systemd)
O `systemd` consolidou-se como o sistema de inicialização (*init system*) e gerenciador de serviços padrão na esmagadora maioria das distribuições Linux empresariais modernas (RHEL, Debian, Ubuntu, Rocky Linux).

Para administrar serviços de rede (como o servidor web Apache/Nginx ou PostgreSQL) e inspecionar logs centralizados de auditoria no terminal Linux, os utilitários de linha de comando padronizados do `systemd` e seus respectivos comandos são:

* **A)** `service start apache` e `cat /var/log/messages` exclusivamente.
* **B)** O comando `systemctl` para gerenciar unidades de serviço (ex.: `systemctl start`, `systemctl enable` para inicialização automática no boot, e `systemctl status`); e o comando `journalctl` para consultar e filtrar os registros do diário estruturado indexado do systemd (ex.: `journalctl -u nome_servico -f` para seguir logs em tempo real).
* **C)** O comando `killall -9 kernel` para atualizar os serviços em produção.
* **D)** O systemd foi descontinuado do Linux e substituído pelo MS-DOS em 2023.
* **E)** Todos os serviços do systemd rodam sem arquivos de configuração em disco, dependendo de comandos de áudio no microfone.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O comando `service` é um script legado mantido apenas por compatibilidade com o antigo System V init; o padrão arquitetural nativo é o `systemctl`.
> - **B)** **CORRETA.** Os dois comandos fundamentais do ecossistema **systemd**:
>   1. **systemctl:** Gerencia o ciclo de vida das *Units* (serviços `.service`, montagens `.mount`, sockets `.socket`).
>      - `systemctl start servico`: Inicia o serviço na sessão corrente.
>      - `systemctl enable servico`: Cria os links simbólicos necessários para que o serviço seja iniciado automaticamente no boot da máquina.
>      - `systemctl status servico`: Exibe o estado de execução (ativo, falho), PID e últimas linhas de log.
>   2. **journalctl:** Interface de consulta ao *systemd-journald*. Coleta logs estruturados de boot, kernel e serviços em formato binário indexado, permitindo buscas filtradas eficientes por unidade (`-u servico`), por severidade (`-p err`) e em tempo real (*follow* `-f`).
> - **C)** Incorreta. Matar o processo do kernel causaria *Kernel Panic* imediato na máquina.
> - **D)** Incorreta. O systemd é o padrão absoluto e ativo do Linux empresarial moderno.
> - **E)** Incorreta. O systemd utiliza arquivos declarativos de configuração de unidade (*unit files*) armazenados em `/etc/systemd/system/` e `/lib/systemd/system/`.
> 
> **Gabarito: B**

---
"""

    # Insert Q06 after 1.1 (before ### 1.2 Chamadas de Sistema)
    p1 = "### 1.2 Chamadas de Sistema (Syscalls: fork, execve, mmap, kill)"
    assert p1 in content
    content = content.replace(p1, q06 + "\n" + p1, 1)

    # Insert Q07 after 2.1 (before ### 2.2 Ciclo de Vida e Estados de um Processo)
    p2 = "### 2.2 Ciclo de Vida e Estados de um Processo"
    assert p2 in content
    content = content.replace(p2, q07 + "\n" + p2, 1)

    # Insert Q08 after 2.5 (before ## 3. Gerenciamento de Memória Virtual, Paginação e Swapping)
    p3 = "## 3. Gerenciamento de Memória Virtual, Paginação e Swapping"
    assert p3 in content
    content = content.replace(p3, q08 + "\n" + p3, 1)

    # Insert Q09 after 3.4 (before ## 4. Sistemas de Arquivos e Permissões no Linux e Windows)
    p4 = "## 4. Sistemas de Arquivos e Permissões no Linux e Windows"
    assert p4 in content
    content = content.replace(p4, q09 + "\n" + p4, 1)

    # Insert Q10 after 4.4 (before ## 5. Administração e Shell Scripting no Linux)
    p5 = "## 5. Administração e Shell Scripting no Linux"
    assert p5 in content
    content = content.replace(p5, q10 + "\n" + p5, 1)

    # Insert Q11 after 5.3 (before ## 6. Administração de Windows e Windows PowerShell)
    p6 = "## 6. Administração de Windows e Windows PowerShell"
    assert p6 in content
    content = content.replace(p6, q11 + "\n" + p6, 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("File 01 successfully enriched! Total questions:", len(re.findall(r"### Questão \d+", content)))

enrich_file_01()


# ==============================================================================
# FILE 02: 02_servicos_de_diretorio_active_directory_e_ldap.md
# ==============================================================================
def enrich_file_02():
    path = os.path.join(BASE_DIR, "02_servicos_de_diretorio_active_directory_e_ldap.md")
    count, content = check_file(path)
    if count >= 10:
        print(f"File 02 already has {count} questions, skipping.")
        return

    q06 = """### Questão 06 (FGV - TRT / Analista Judiciário - TI - Protocolo LDAP: Portas e Modelo Operacional)
O Lightweight Directory Access Protocol (LDAP) é o protocolo padrão da indústria utilizado para consulta e modificação de serviços de diretório hierárquicos em redes corporativas.

A respeito das características arquiteturais e das portas de comunicação padronizadas do LDAP, assinale a afirmativa correta:

* **A)** O LDAP opera exclusivamente sobre o protocolo UDP na porta 80 em texto claro sem suporte a autenticação.
* **B)** Por padrão IANA, o LDAP não seguro opera sobre o protocolo TCP na porta **389** (podendo ser protegido em tempo de execução via comando `StartTLS`), enquanto o LDAP seguro sobre SSL/TLS (**LDAPS**) opera tradicionalmente sobre a porta TCP **636**, utilizando certificados digitais X.509 para garantir a confidencialidade e integridade das credenciais transmitidas.
* **C)** No modelo de informação do LDAP, as operações de leitura são denominadas `DROP` e as de escrita `SELECT`.
* **D)** O LDAP substitui o protocolo IP na camada 3 do modelo OSI.
* **E)** As consultas LDAP são otimizadas para ambientes com altíssima taxa de gravação massiva e raríssimas leituras.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O LDAP utiliza transporte orientado a conexão TCP, suportando múltiplos métodos de autenticação (*Simple Bind*, SASL, Kerberos).
> - **B)** **CORRETA.** Especificação canônica do **LDAP (RFC 4511)**:
>   - **Porta TCP 389:** Porta padrão para tráfego LDAP tradicional. Admite a inicialização da sessão com negociação de segurança em tempo de execução via extensão `StartTLS` (RFC 4513) na mesma porta 389.
>   - **Porta TCP 636:** Porta padrão para **LDAPS (LDAP over SSL/TLS)**, onde o túnel criptográfico TLS é negociado logo na abertura da conexão antes de qualquer tráfego LDAP.
>   - **Catálogo Global (GC):** Em ambientes Active Directory, as portas do Global Catalog são TCP **3268** (claro) e TCP **3269** (seguro via SSL).
> - **C)** Incorreta. As operações centrais do LDAP são `Bind` (autenticação), `Search` (busca), `Compare`, `Add` (inserção), `Modify` (alteração) e `Delete` (exclusão).
> - **D)** Incorreta. O LDAP é um protocolo de **Camada de Aplicação (Camada 7)**.
> - **E)** Incorreta. Serviços de diretório são otimizados exatamente para uma **proporção muito alta de leituras/consultas em relação a modificações** (*read-heavy*).
> 
> **Gabarito: B**

---
"""

    q07 = """### Questão 07 (FCC - TRT / Analista de TI - Infraestrutura - Estrutura Física do Active Directory: Sites e Replicação)
No Microsoft Windows Server Active Directory Domain Services (AD DS), a topologia física é estritamente dissociada da estrutura lógica (florestas, árvores e domínios) para otimizar o tráfego de rede entre localidades remotas.

A respeito dos componentes da **Estrutura Física do Active Directory** e da replicação entre Controladores de Domínio (DCs), assinale a afirmativa correta:

* **A)** Um *Site* do Active Directory corresponde exatamente a uma Unidade Organizacional (OU) criada pelo administrador no painel de usuários.
* **B)** Um **Site** do Active Directory é uma construção física que mapeia uma ou mais sub-redes IP com conectividade de rede local (LAN) de alta velocidade e baixo custo; a replicação **Intra-Site** (dentro do mesmo site) ocorre de forma quase instantânea orientada por notificações RPC (*Change Notification*) e sem compactação de dados para economizar CPU; enquanto a replicação **Inter-Site** (entre sites distintos interligados por WANs lentas via Site Links) é agendada em intervalos controlados e comprime os dados transferidos para preservar a largura de banda da rede.
* **C)** Dois computadores pertencentes ao mesmo domínio são proibidos de residir em sites físicos distintos.
* **D)** A replicação do Active Directory é unidirecional e centralizada exclusivamente em fitas magnéticas transportadas por via postal.
* **E)** Todos os Controladores de Domínio de uma floresta devem ficar fisicamente no mesmo prédio para evitar falhas de replicação.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. *Site* é um conceito **físico** de conectividade de rede; *Unidade Organizacional (OU)* é um contêiner **lógico** administrativo.
> - **B)** **CORRETA.** Arquitetura física oficial do **Active Directory**:
>   - **Site:** Representa uma localidade geográfica bem conectada por links LAN rápidos (ex.: Sede em Goiânia, Subseção em Anápolis).
>   - **Replicação Intra-site (Dentro do Site):** Ocorre rapidamente (notificação disparada em média 15 segundos após a alteração). Como a largura de banda na LAN é abundante, os dados do diretório são replicados **sem compressão**, priorizando menor consumo de CPU dos DCs.
>   - **Replicação Inter-site (Entre Sites Distintos):** Ocorre através de links de site (*Site Links* usando RPC over IP ou SMTP). Como enlaces WAN são caros e concorrem com o tráfego de produção, a replicação é **agendada** (ex.: a cada 180 minutos ou durante a madrugada) e os dados são **altamente compactados** antes do envio.
> - **C)** Incorreta. Um mesmo domínio pode e costuma abranger dezenas de sites físicos interligados.
> - **D)** Incorreta. A replicação do AD é multimaster e baseada em protocolos de rede RPC/IP.
> - **E)** Incorreta. Distribuir DCs em sites geograficamente distintos é a melhor prática para resiliência e alta disponibilidade.
> 
> **Gabarito: B**

---
"""

    q08 = """### Questão 08 (FGV - TRT / Analista Judiciário - TI - O Mecanismo do Catálogo Global no Active Directory)
Em florestas corporativas do Active Directory compostas por múltiplos domínios (por exemplo, `tce.go.gov.br`, `sub1.tce.go.gov.br`, `sub2.tce.go.gov.br`), o **Catálogo Global (*Global Catalog - GC*)** desempenha um papel indispensável para a localização rápida de objetos e logon de usuários.

A respeito do conteúdo e das funções operacionais do Catálogo Global, assinale a afirmativa correta:

* **A)** O Catálogo Global armazena a cópia completa de todos os atributos de todos os objetos de todos os servidores do planeta.
* **B)** Um servidor configurado como Catálogo Global armazena uma réplica completa de todos os objetos de seu próprio domínio local e uma **réplica parcial de somente-leitura** de todos os objetos de todos os demais domínios da floresta (denominada *Partial Attribute Set - PAS*), permitindo buscas rápidas em toda a floresta sem sobrecarregar links WAN e viabilizando a resolução de associações a Grupos Universais durante o processo de logon.
* **C)** O Catálogo Global é um arquivo executável que deve ser instalado exclusivamente em estações de trabalho Windows 10 Home.
* **D)** O Catálogo Global é incompatível com o protocolo Kerberos v5.
* **E)** Cada floresta do Active Directory pode possuir no máximo um único servidor com a função de Catálogo Global ativada.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O GC não armazena todos os atributos de outros domínios; ele armazena apenas um subconjunto restrito de atributos frequentemente consultados (*Partial Attribute Set*).
> - **B)** **CORRETA.** Funções do **Catálogo Global (GC)**:
>   1. **Busca Florestal:** Permite que um usuário procure uma impressora, computador ou colega em qualquer domínio da floresta consultando o DC/GC local rapidamente, sem fazer requisições a DCs remotos.
>   2. **Conjunto Parcial de Atributos (PAS):** Contém atributos comuns como Nome, Sobrenome, E-mail, UPN e SID de todos os domínios.
>   3. **Logon e Grupos Universais:** Na autenticação Kerberos, o DC precisa consultar o GC para expandir a lista de associações a **Grupos Universais** do usuário e embutir os respectivos SIDs no token de acesso (*PAC - Privilege Attribute Certificate*). Se o GC estiver inacessível, o logon de usuários comuns pode falhar (salvo se o *Universal Group Membership Caching* estiver ativado).
> - **C)** Incorreta. O GC é uma função habilitada exclusivamente em Controladores de Domínio (DCs) do Windows Server.
> - **D)** Incorreta. O GC é parte integrante do fluxo de autenticação Kerberos.
> - **E)** Incorreta. Qualquer DC pode ser promovido a GC; a recomendação em domínios modernos é que a maioria dos DCs também atuem como Catálogo Global.
> 
> **Gabarito: B**

---
"""

    q09 = """### Questão 09 (FCC - TRT / Analista de Sistemas - Suporte a Servidores - Escopos de Grupos no Active Directory: Estratégia AGDLP)
O Active Directory classifica os grupos segundo dois tipos (**Segurança** e **Distribuição**) e três escopos principais: **Global**, **Domínio Local** (*Domain Local*) e **Universal**.

Para implementar o controle de acesso a pastas e recursos compartilhados em redes com múltiplos domínios conforme as melhores práticas recomendadas pela Microsoft, utiliza-se a consagrada estratégia de aninhamento **AGDLP** (ou AGUDLP).

A sequência correta de aninhamento e concessão de privilégios prescrita pela metodologia **AGDLP** é:

* **A)** Atribuir as permissões diretamente na Conta do Usuário e adicioná-la a um Grupo Universal.
* **B)** Inserir as **Contas de Usuários (A)** em **Grupos Globais (G)** (que representam funções corporativas de negócio); aninhar esses Grupos Globais dentro de **Grupos de Domínio Local (DL)** (que representam o recurso ou permissão específica); e, finalmente, conceder as **Permissões (P)** de acesso ao recurso (ex.: NTFS) diretamente ao Grupo de Domínio Local correspondente.
* **C)** Conceder Permissões (P) aos Grupos Globais e aninhá-los em Contas de Usuários (A).
* **D)** Criar exclusivamente Grupos de Distribuição sem senhas e vinculá-los ao registro do Windows.
* **E)** Aninhar todos os servidores em um único Grupo Global com permissão de Administrador do Domínio.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Conceder permissões diretamente a contas de usuários viola as melhores práticas de governança, tornando a auditoria impossível e gerando acúmulo residual de privilégios.
> - **B)** **CORRETA.** Metodologia canônica **AGDLP (Accounts $\\to$ Global $\\to$ Domain Local $\\to$ Permissions)**:
>   1. **A (Accounts):** As contas de usuários individuais.
>   2. **G (Global Groups):** Agrupam contas com base na sua função ou cargo de trabalho (ex.: `GG_Auditores_Fiscalizacao`).
>   3. **DL (Domain Local Groups):** Criados no domínio onde o recurso reside para definir o direito de acesso específico (ex.: `GDL_PastaProcessos_Modificar`).
>   4. **P (Permissions):** As listas de controle de acesso (ACLs/ACEs) do sistema de arquivos NTFS ou banco concedem as permissões de leitura/escrita **exclusivamente ao Grupo de Domínio Local**.
>   - Se a floresta tiver múltiplos domínios, expande-se para **AGUDLP**, onde Grupos Globais de diferentes domínios são agregados em um **Grupo Universal (U)** antes de serem aninhados no Grupo de Domínio Local (DL).
> - **C)** Incorreta. Inverteu o sentido do aninhamento e da governança.
> - **D)** Incorreta. Grupos de Distribuição servem exclusivamente para listas de e-mail (Exchange), não podendo receber permissões de segurança NTFS.
> - **E)** Incorreta. Violação grosseira do princípio do menor privilégio.
> 
> **Gabarito: B**

---
"""

    q10 = """### Questão 10 (FGV - TRT / Analista Judiciário - TI - Precedência de GPOs: O Princípio LSDOU)
No gerenciamento centralizado de estações de trabalho e servidores Windows através de Objetos de Diretiva de Grupo (*Group Policy Objects - GPOs*), um computador ou usuário pode estar sujeito a múltiplas políticas conflitantes configuradas em diferentes níveis da hierarquia.

A ordem padrão de processamento e precedência na aplicação de GPOs, expressa pela sigla **LSDOU**, estabelece que:

* **A)** As políticas vinculadas ao nível Local sobrescrevem compulsoriamente todas as políticas definidas na Unidade Organizacional (OU).
* **B)** O processamento ocorre na seguinte sequência temporal: 1º **Local** (política local da máquina), 2º **Site**, 3º **Domínio** e 4º **Unidade Organizacional (OU)** (processando das OUs superiores para as OUs filhas aninhadas); consequentemente, no caso de configurações conflitantes, **a última política processada (a vinculada à OU mais específica e profunda) é a que prevalece e sobrescreve as configurações anteriores**, salvo se houver imposição (*Enforced*).
* **C)** Políticas de Domínio são completamente ignoradas se o computador possuir antivírus instalado.
* **D)** A ordem LSDOU é definida aleatoriamente pela CPU a cada reinicialização do Windows.
* **E)** Uma GPO vinculada a um Site tem precedência superior sobre uma GPO vinculada com atributo *Enforced* em um Domínio.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A política Local é a primeira a ser aplicada e, portanto, é a mais fraca: qualquer política de Site, Domínio ou OU sobrescreve a política Local.
> - **B)** **CORRETA.** Regra canônica de herança e precedência de **GPOs (LSDOU)**:
>   - **Ordem de Aplicação:** 
>     1. **L**ocal Policy (mais antiga/mais fraca);
>     2. **S**ite;
>     3. **D**omain;
>     4. **O**rganizational **U**nit (processa da OU pai até a OU folha onde o objeto reside).
>   - **Regra de Conflito:** *"O último a ser aplicado vence"*. Logo, uma configuração na OU folha sobrescreve configurações divergentes vindas do Domínio ou do Site.
>   - **Exceção Maior:** A marcação **Enforced (Imposta)** em uma GPO de nível superior impede que suas diretivas sejam sobrescritas por OUs subordinadas e quebra bloqueios de herança (*Block Inheritance*).
> - **C)** Incorreta. Políticas de Domínio são aplicadas pelo serviço Group Policy Client do sistema operacional.
> - **D)** Incorreta. A ordem é estritamente determinística e previsível.
> - **E)** Incorreta. A flag *Enforced* confere prioridade absoluta àquela GPO contra qualquer outra política não imposta.
> 
> **Gabarito: B**

---
"""

    q11 = """### Questão 11 (FGV - TRT / Analista Judiciário - TI - Kerberos v5, Clock Skew e o Papel do PDC Emulator)
O protocolo de autenticação padrão no Active Directory é o **Kerberos v5** (RFC 4120), que opera com bilhetes criptográficos temporais (*tickets*) para assegurar autenticação mútua sem transmissão de senhas na rede.

A respeito da vulnerabilidade do Kerberos a ataques de repetição (*Replay Attacks*), do papel do mestre FSMO **PDC Emulator** e da tolerância temporal (*Clock Skew*), assinale a afirmativa correta:

* **A)** O Kerberos não utiliza carimbos de tempo, dependendo exclusivamente do endereço MAC da placa de rede para validar bilhetes.
* **B)** Os bilhetes e autenticadores do Kerberos contêm carimbos de data/hora (*timestamps*); para impedir que um invasor capture um pacote e o retransmita posteriormente (*Replay Attack*), o Active Directory impõe uma tolerância temporal máxima padrão de **5 minutos (*Clock Skew*)** entre o relógio da estação cliente e o Controlador de Domínio; para garantir essa sincronização em toda a floresta, o Controlador de Domínio detentor da função FSMO de **PDC Emulator** atua como a fonte oficial de tempo (servidor NTP raiz do domínio), sincronizando todas as estações e DCs subordinados.
* **C)** Se a diferença de relógio entre a estação de trabalho e o PDC Emulator for de 3 horas, a autenticação Kerberos prossegue normalmente sem emitir alertas.
* **D)** O PDC Emulator é uma placa aceleradora de vídeo 3D que deve ser instalada fisicamente em todas as estações do tribunal.
* **E)** O protocolo Kerberos foi substituído pelo NTLMv1 em todas as versões modernas do Windows Server devido à sua superioridade criptográfica.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O carimbo de data e hora (*timestamp*) é o mecanismo nuclear de segurança do Kerberos v5 para evitar ataques de repetição.
> - **B)** **CORRETA.** Funcionamento temporal do **Kerberos v5 no AD DS**:
>   - **Clock Skew (Tolerância de Relógio):** Por padrão nas Diretivas de Segurança do Domínio, a diferença máxima tolerada entre o relógio do cliente e o KDC (Controlador de Domínio) é de **5 minutos**. Se o relógio da máquina estiver desfasado em mais de 5 minutos, o KDC rejeita o bilhete com erro `KRB_AP_ERR_SKEW`, impedindo logons e acesso a compartilhamentos.
>   - **Papel do PDC Emulator (Mestre FSMO):** O DC que detém a função de emulador PDC no domínio raiz da floresta atua como o servidor de hora mestre (*Authoritative Time Server*) via protocolo W32Time/NTP, sincronizando-se com um relógio atômico externo confiável (como o `ntp.br`). Todos os demais DCs da floresta sincronizam seus relógios com ele, e as estações de trabalho sincronizam seus relógios com seu respectivo DC local, garantindo consistência cronológica em toda a rede.
> - **C)** Incorreta. Uma diferença de 3 horas causará rejeição sumária e imediata de qualquer autenticação Kerberos.
> - **D)** Incorreta. É uma função lógica de software FSMO do Active Directory.
> - **E)** Incorreta. O NTLMv1 é um protocolo inseguro e vulnerável, banido em favor do Kerberos.
> 
> **Gabarito: B**

---
"""

    # Insert Q06 after 1.1 (before ### 1.2 O Modelo de Informação e Árvore DIT)
    p1 = "### 1.2 O Protocolo LDAP: Portas Padrão e Arquitetura TCP/IP"
    assert p1 in content
    content = content.replace(p1, q06 + "\n" + p1, 1)

    # Insert Q07 after 2.3 (before ## 3. Componentes Estruturais e Operações de Diretório)
    p2 = "### 2.2 Tipos e Escopos de Grupos no AD DS"
    assert p2 in content
    content = content.replace(p2, q07 + "\n" + p2, 1)

    # Insert Q08 after 3.1 (before ### 3.2 Tipos de Grupos e seus Escopos)
    p3 = "### 3.2 Sites, Sub-redes e Otimização de Replicação Física"
    assert p3 in content
    content = content.replace(p3, q08 + "\n" + p3, 1)

    # Insert Q09 after 3.2 (before ### 3.3 Funções FSMO)
    p4 = "### 3.3 Catálogo Global (Global Catalog - GC)"
    assert p4 in content
    content = content.replace(p4, q09 + "\n" + p4, 1)

    # Insert Q10 after 4.1 (before ### 4.2 Bloqueio de Herança)
    p5 = "### 4.2 Bloqueio de Herança (Block Inheritance) vs. Imposição (Enforced)"
    assert p5 in content
    content = content.replace(p5, q10 + "\n" + p5, 1)

    # Insert Q11 after 4.4 (before ## 6. Fontes Recomendadas na Internet)
    p6 = "## 6. Fontes Recomendadas na Internet"
    assert p6 in content
    content = content.replace(p6, q11 + "\n" + p6, 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("File 02 successfully enriched! Total questions:", len(re.findall(r"### Questão \d+", content)))


# ==============================================================================
# FILE 03: 03_redes_tcp_ip_enderecamento_ipv4_ipv6_dns_dhcp.md
# ==============================================================================
def enrich_file_03():
    path = os.path.join(BASE_DIR, "03_redes_tcp_ip_enderecamento_ipv4_ipv6_dns_dhcp.md")
    count, content = check_file(path)
    if count >= 10:
        print(f"File 03 already has {count} questions, skipping.")
        return

    q06 = """### Questão 06 (FGV - TJ-AP / Analista Judiciário - TI - Unidades de Dados de Protocolo e Encapsulamento)
Na arquitetura em camadas dos modelos de redes de computadores (OSI e TCP/IP), o tráfego de saída sofre o processo progressivo de **Encapsulamento**, no qual cada camada empacota os dados da camada superior e anexa seus próprios cabeçalhos de controle.

A respeito das Unidades de Dados de Protocolo (**PDUs**) manipuladas em cada nível da pilha TCP/IP, assinale a opção que apresenta a correspondência correta de nomenclatura da PDU e seu respectivo dispositivo/protocolo de atuação:

* **A)** Camada de Transporte: Quadro (*Frame*), operado por switches de camada 2.
* **B)** Camada de Internet (Rede): Pacote ou Datagrama (endereçamento IP), processado por roteadores; e Camada de Enlace (Acesso à Rede): **Quadro ou Trama (*Frame*)**, delimitado por cabeçalhos que contêm endereços físicos MAC e sequências de checagem de erros (CRC/FCS), manipulado por switches Ethernet.
* **C)** Camada de Aplicação: Bit puro em pulsos elétricos no cabo de par trançado.
* **D)** Camada de Enlace: Mensagem HTTP em texto puro.
* **E)** Camada de Transporte: Rota estática em formato JSON.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A PDU da Camada de Transporte é o **Segmento** (no protocolo TCP) ou o **Datagrama de Usuário** (no protocolo UDP). Quadro é a PDU da Camada de Enlace.
> - **B)** **CORRETA.** Nomenclatura oficial das **PDUs (Protocol Data Units)** no modelo de redes:
>   1. **Camada de Aplicação:** Mensagem / Dados brutos da aplicação (HTTP, DNS, SSH).
>   2. **Camada de Transporte:** **Segmento** (TCP) ou **Datagrama** (UDP) — encapsula com portas de origem e destino e números de sequência.
>   3. **Camada de Rede / Internet:** **Pacote ou Datagrama IP** — adiciona cabeçalho com IP de origem e IP de destino (dispositivos de atuação: Roteadores e Switches L3).
>   4. **Camada de Enlace de Dados:** **Quadro ou Trama (Frame)** — adiciona cabeçalho com MAC de origem e MAC de destino e trailer de integridade FCS/CRC-32 (dispositivos: Switches L2, placas de rede/NICs).
>   5. **Camada Física:** **Bits** — sequência serial de bits codificada em pulsos elétricos, ópticos ou ondas de rádio (dispositivos: Hubs, transceivers ópticos, cabos UTP).
> - **C)** Incorreta. Bits pertencem à Camada Física (Camada 1).
> - **D)** Incorreta. Mensagens HTTP pertencem à Camada de Aplicação (Camada 7).
> - **E)** Incorreta. Rotas estáticas pertencem à Camada de Rede (tabelas de roteamento).
> 
> **Gabarito: B**

---
"""

    q07 = """### Questão 07 (FCC - TRT / Analista de Redes - Endereçamento Privado RFC 1918 e NAT/PAT)
Diante da iminência do esgotamento histórico de endereços IPv4 públicos globais, a IETF padronizou a separação entre blocos de endereços públicos roteáveis e blocos de endereçamento privado reservados para uso interno corporativo (**RFC 1918**), combinados com o mecanismo de **Tradução de Endereços de Rede (NAT/PAT)**.

A respeito das faixas de endereçamento privado da RFC 1918 e do funcionamento do **NAPT/PAT** (*Network Address Port Translation*), assinale a afirmativa correta:

* **A)** A faixa privada de Classe C é `192.168.0.0` com máscara `/16` (abrangendo de `192.168.0.0` até `192.168.255.255`), sendo esses endereços proibidos de serem roteados diretamente na internet pública global; para permitir que milhares de computadores dessa rede interna acessem a internet através de um único IP público contratado, o roteador de borda utiliza o **PAT**, mapeando as conexões internas privadas para diferentes **portas de transporte TCP/UDP** no endereço IP público externo.
* **B)** A faixa `10.0.0.0/8` é pública e atribuída exclusivamente a sites do governo federal americano.
* **C)** O NAT proíbe que qualquer pacote saia da rede local para a internet.
* **D)** O PAT exige que cada computador da rede interna possua seu próprio endereço IP público registrado no Registro.br.
* **E)** Endereços privados da RFC 1918 são roteados normalmente na internet sem necessidade de qualquer tradução por firewalls ou roteadores.

> **Comentário Detalhado:**
>
> - **A)** **CORRETA.** Fundamentos da **RFC 1918 e NAT/PAT**:
>   - **Três Faixas Privadas Oficiais (RFC 1918):**
>     1. `10.0.0.0/8` (`10.0.0.0` a `10.255.255.255` - 16.777.216 endereços).
>     2. `172.16.0.0/12` (`172.16.0.0` a `172.31.255.255` - 1.048.576 endereços).
>     3. `192.168.0.0/16` (`192.168.0.0` a `192.168.255.255` - 65.536 endereços).
>   - Esses blocos são descartados (*dropped*) pelos roteadores da internet pública (*não roteáveis na WAN*).
>   - **NAPT / PAT (NAT Overload):** Mapeia múltiplos IPs privados internos (muitos para um / $N:1$) para um único endereço IPv4 público válido. O roteador mantém uma tabela de estados de tradução na qual diferencia as conexões ativas variando as **portas de transporte de origem (Port Numbers TCP/UDP)** no cabeçalho externo.
> - **B)** Incorreta. O bloco `10.0.0.0/8` é a maior faixa privada reservada da RFC 1918.
> - **C)** Incorreta. O NAT foi concebido justamente para permitir a comunicação externa da rede interna.
> - **D)** Incorreta. Esse seria o modelo sem NAT; o PAT economiza IPs públicos compartilhando um único IP com toda a organização.
> - **E)** Incorreta. Provedores de internet (ISPs) bloqueiam e descartam pacotes com origem RFC 1918.
> 
> **Gabarito: A**

---
"""

    q08 = """### Questão 08 (FGV - TRT / Analista Judiciário - TI - Endereçamento IPv6 e Extinção do Broadcast)
O protocolo IPv6 resolve o esgotamento do IPv4 oferecendo um espaço de endereçamento de 128 bits ($2^{128} \\approx 3,4 \\times 10^{38}$ endereços), estruturado em 8 grupos de 4 dígitos hexadecimais separados por dois-pontos.

A respeito das regras formais de simplificação/compactação de endereços IPv6 (RFC 5952) e dos tipos de transmissão suportados, assinale a afirmativa correta:

* **A)** O IPv6 manteve o mecanismo de transmissão por *Broadcast*, ampliando a quantidade de pacotes de broadcast na rede para localizar dispositivos.
* **B)** Na simplificação de um endereço IPv6, pode-se omitir zeros à esquerda em qualquer bloco de 16 bits; e uma sequência contígua de um ou mais blocos formados exclusivamente por zeros pode ser substituída por dois-pontos duplos (`::`), sendo permitido aplicar essa substituição de dois-pontos duplos **uma única vez em todo o endereço**, para evitar ambiguidade na reconstituição dos 128 bits; além disso, o IPv6 **extinguiu completamente o tráfego de Broadcast**, substituindo-o pelo uso otimizado de transmissões **Multicast** e **Anycast**.
* **C)** O endereço de loopback do IPv6 é `127.0.0.1`.
* **D)** O símbolo `::` pode ser utilizado 5 vezes no mesmo endereço IPv6 sem qualquer problema de ambiguidade.
* **E)** Endereços IPv6 são obrigatoriamente convertidos para decimal antes de serem enviados pela placa de rede.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O IPv6 **aboliu expressamente o endereço de Broadcast**, eliminando tempestades de broadcast (*broadcast storms*) na rede local.
> - **B)** **CORRETA.** Regras oficiais da **RFC 5952 (Formatação e Compactação do IPv6)**:
>   1. **Omissão de zeros à esquerda:** Em cada hexteto (bloco de 16 bits), zeros à esquerda são descartados (ex.: `:0042:` vira `:42:`, `:0000:` vira `:0:`).
>   2. **Compressão com `::` (Dois-Pontos Duplos):** Uma única sequência de blocos de zeros contíguos mais longa pode ser colapsada para `::`. **Regra mandatória:** `::` só pode constar **exatamente uma vez** por endereço. Se houvesse dois `::`, seria algebricamente impossível determinar quantos blocos de zeros foram omitidos em cada ponto.
>   3. **Tipos de Endereçamento:** O IPv6 opera com **Unicast** (um-para-um), **Anycast** (um-para-o-mais-próximo de um grupo) e **Multicast** (um-para-muitos cadastrados). Todo o serviço que antes usava broadcast (como ARP e DHCP) agora opera sobre grupos de Multicast eficientes (como o *Solicited-Node Multicast* no protocolo NDP).
> - **C)** Incorreta. O endereço de loopback no IPv6 é `::1` (equivalente ao `127.0.0.1` do IPv4).
> - **D)** Incorreta. Usar `::` mais de uma vez torna a representação inválida e ambígua.
> - **E)** Incorreta. Os endereços são transmitidos como sequências binárias puras de 128 bits.
> 
> **Gabarito: B**

---
"""

    q09 = """### Questão 09 (FCC - TRT / Analista de Redes - Mecanismos de Transição para o IPv6)
A migração mundial da internet do IPv4 para o IPv6 ocorre de forma gradual e heterogênea. Como os cabeçalhos dos protocolos IPv4 e IPv6 são mutuamente incompatíveis entre si, a engenharia de redes desenvolveu técnicas formais de coexistência e transição.

As três categorias clássicas de mecanismos de transição padronizadas pela IETF são:

* **A)** Pilha Dupla (*Dual-Stack*), Tunelamento (*Tunneling*, como 6in4 e 6to4) e Tradução (*Translation*, como NAT64/DNS64).
* **B)** Cifragem Simétrica, Hash e Assinatura Digital.
* **C)** Sub-rede Classe A, Sub-rede Classe B e Sub-rede Classe C.
* **D)** Backup Full, Backup Incremental e Backup Diferencial.
* **E)** CSMA/CD, Token Ring e FDDI.

> **Comentário Detalhado:**
>
> - **A)** **CORRETA.** Os Três Mecanismos Canônicos de Transição IPv4/IPv6:
>   1. **Pilha Dupla (Dual-Stack):** A abordagem preferencial e recomendada. Os dispositivos (roteadores, firewalls e servidores) executam simultaneamente as duas pilhas de protocolos (IPv4 e IPv6) ativas nas mesmas interfaces de rede. Se o destino suporta IPv6 (registro DNS AAAA), conecta via IPv6; senão, conecta via IPv4 (registro DNS A).
>   2. **Tunelamento (Tunneling):** Permite encapsular pacotes IPv6 dentro de pacotes IPv4 para trafegar através de uma infraestrutura intermediária que só suporta IPv4 (ex.: 6in4, 6to4, GRE, Teredo).
>   3. **Tradução (Translation):** Permite a comunicação direta entre hosts que só possuem IPv6 e servidores legados que só possuem IPv4, utilizando **NAT64** no roteador de borda complementado por **DNS64** para síntese de registros de endereço sintéticos.
> - **B)** Incorreta. Primitivas de segurança criptográfica.
> - **C)** Incorreta. Classes obsoletas de endereçamento IPv4.
> - **D)** Incorreta. Tipos de cópias de segurança de dados.
> - **E)** Incorreta. Tecnologias de enlace de rede legadas.
> 
> **Gabarito: A**

---
"""

    q10 = """### Questão 10 (FGV - TRT / Analista Judiciário - TI - Consultas DNS: Recursivas vs. Iterativas)
O Domain Name System (DNS) é uma base de dados hierárquica e distribuída mundialmente, responsável por converter nomes amigáveis (FQDN, como `www.tce.go.gov.br`) em endereços IP numéricos.

A respeito do fluxo de resolução de nomes e da distinção entre **Consultas Recursivas** e **Consultas Iterativas**, assinale a afirmativa correta:

* **A)** Em uma consulta recursiva, o servidor DNS consultado apenas devolve uma indicação (*referral*) do melhor servidor seguinte que pode ter a resposta, sem se comprometer a buscar o endereço final.
* **B)** Na **Consulta Recursiva** (enviada tipicamente pela máquina cliente / *Stub Resolver* ao seu servidor DNS configurado localmente), o cliente exige que o servidor DNS faça todo o trabalho de resolução e devolva uma resposta definitiva (o IP resolvido com sucesso ou uma mensagem de erro de domínio inexistente `NXDOMAIN`); ao passo que na **Consulta Iterativa** (executada pelo servidor DNS recursivo aos Servidores Raiz, servidores de TLD `.br` e servidores autoritativos), o servidor consultado responde imediatamente com a melhor resposta que possui ou com uma referência (*referral*) apontando qual o próximo servidor autoritativo na hierarquia que deve ser consultado.
* **C)** Servidores DNS Raiz (*Root DNS Servers*) realizam obrigatoriamente consultas recursivas para todos os usuários domésticos do planeta.
* **D)** O protocolo DNS utiliza exclusivamente a porta TCP 8080 para resolver nomes de computadores.
* **E)** Consultas iterativas são proibidas na internet por violarem direitos autorais.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Devolver uma referência (*referral*) apontando outro servidor para o cliente consultar é a definição exata de **Consulta Iterativa**, não recursiva.
> - **B)** **CORRETA.** Mecânica canônica do **DNS (RFC 1034 / 1035)**:
>   - **Consulta Recursiva:** O cliente (*Resolver*) delega a responsabilidade total ao servidor DNS local (ex.: DNS do tribunal ou 1.1.1.1): *"Traga-me a resposta final completa, eu aguardo aqui"*.
>   - **Consulta Iterativa:** O servidor DNS recursivo assume a busca e faz perguntas iterativas pela cadeia de autoridade:
>     1. Pergunta aos **Servidores Raiz (Root Servers - ponto '.')**: o Root responde com indicação dos servidores do TLD `.br`.
>     2. Pergunta aos servidores de TLD `.br`: respondem com indicação dos servidores autoritativos de `gov.br`.
>     3. Pergunta aos servidores autoritativos de `tce.go.gov.br`: respondem com o registro A final (`IP: 200.x.x.x`).
>     4. O servidor recursivo salva o registro no seu **Cache DNS** local (respeitando o campo TTL) e devolve o IP definitivo ao cliente que fez a consulta recursiva.
> - **C)** Incorreta. Servidores Raiz e de TLD operam estritamente em modo **Iterativo**, rejeitando consultas recursivas para proteger sua disponibilidade e escalabilidade global.
> - **D)** Incorreta. O DNS utiliza as portas **UDP 53** (consultas normais rápidas) e **TCP 53** (transferências de zona / AXFR e respostas que excedem 512 bytes).
> - **E)** Incorreta. Consultas iterativas são o motor técnico da espinha dorsal de resolução de nomes da internet mundial.
> 
> **Gabarito: B**

---
"""

    q11 = """### Questão 11 (FCC - TRT / Analista de Tecnologia da Informação - DHCP: Timers T1/T2 e DHCP Relay Agent)
O protocolo DHCP (*Dynamic Host Configuration Protocol*) automatiza a concessão dinâmica de endereços IP, máscaras de rede, gateway padrão e servidores DNS em redes locais.

A respeito do ciclo de renovação de concessão (*Lease Time*) e do papel do **Agente de Retransmissão DHCP (*DHCP Relay Agent*)**, assinale a afirmativa correta:

* **A)** O cliente DHCP nunca renova seu endereço IP, abandonando a rede e desligando o computador após 1 hora de uso.
* **B)** A concessão do DHCP possui dois temporizadores fundamentais de renovação: o **Timer T1 (Renovação)**, acionado quando atinge **50% do tempo de concessão**, no qual o cliente envia um pacote `DHCPREQUEST` em Unicast diretamente ao servidor original que concedeu o IP; e o **Timer T2 (Revinculação)**, acionado se o servidor original não responder e a concessão atingir **87,5% (7/8) do tempo**, momento em que o cliente passa a transmitir em Broadcast para qualquer outro servidor DHCP da rede; além disso, como as mensagens iniciais do DHCP utilizam difusão por Broadcast (não roteável), o **DHCP Relay Agent** atua em roteadores para interceptar esses broadcasts locais e reencaminhá-los via Unicast até um servidor DHCP centralizado localizado em outra sub-rede.
* **C)** O DHCP Relay Agent converte pacotes IPv4 em sinais de rádio analógicos em amplitude modulada (AM).
* **D)** O Timer T1 é disparado exatamente no instante em que o tempo de concessão expira em 100%.
* **E)** O protocolo DHCP opera nas portas TCP 20 e 21.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O cliente busca renovar ativamente a concessão para manter o mesmo IP em uso ininterrupto.
> - **B)** **CORRETA.** Mecânica avançada do **DHCP (RFC 2131)**:
>   - **Timer T1 (Renewal Timer):** Disparado em $0,5 \\times \\text{Lease Time}$ (50%). O host envia `DHCPREQUEST` direcionado (Unicast) ao servidor que concedeu a licença. Se receber `DHCPACK`, o timer é resetado.
>   - **Timer T2 (Rebinding Timer):** Se o servidor original estiver fora do ar e não responder, quando o relógio atingir $0,875 \\times \\text{Lease Time}$ (87,5%), o host entra em modo de revinculação e envia `DHCPREQUEST` em **Broadcast**, aceitando confirmação de qualquer servidor DHCP ativo.
>   - Se expirar 100% sem resposta, o cliente abandona o IP e recomeça o ciclo `DHCPDISCOVER` (ou assume um IP APIPA `169.254.x.x`).
>   - **DHCP Relay Agent (RFC 3046 / IP Helper-Address):** Como o `DHCPDISCOVER` é emitido em broadcast de camada 2/3 (`255.255.255.255`), roteadores comuns descartam o pacote. O Relay Agent intercepta esse broadcast na sub-rede local, anexa as informações da interface de origem e envia o pacote empacotado em **Unicast via UDP porta 67** para o servidor DHCP central no datacenter, permitindo consolidar servidores DHCP corporativos.
> - **C)** Incorreta. Trata-se de reencaminhamento de pacotes IP entre sub-redes corporativas.
> - **D)** Incorreta. T1 dispara em 50% da concessão; em 100% ocorre a expiração da concessão (*Lease Expiration*).
> - **E)** Incorreta. O DHCP opera sobre **UDP portas 67** (servidor) e **68** (cliente). Portas TCP 20/21 são do FTP.
> 
> **Gabarito: B**

---
"""

    # Insert Q06 after 1.3 (before ## 2. Endereçamento e Sub-redes IPv4)
    p1 = "## 2. Endereçamento e Sub-redes IPv4"
    assert p1 in content
    content = content.replace(p1, q06 + "\n" + p1, 1)

    # Insert Q07 after 2.2 (before ### 2.3 Roteamento Interdomínio Sem Classe (CIDR) e VLSM)
    p2 = "### 2.3 Roteamento Interdomínio Sem Classe (CIDR) e VLSM"
    assert p2 in content
    content = content.replace(p2, q07 + "\n" + p2, 1)

    # Insert Q08 after 3.2 (before ### 3.3 Faixas Notáveis de Endereços IPv6)
    p3 = "### 3.3 Faixas Notáveis de Endereços IPv6 (Loopback, Link-Local, ULA, GUA)"
    assert p3 in content
    content = content.replace(p3, q08 + "\n" + p3, 1)

    # Insert Q09 after 3.4 (before ## 4. Protocolo DNS (Domain Name System))
    p4 = "## 4. Protocolo DNS (Domain Name System)"
    assert p4 in content
    content = content.replace(p4, q09 + "\n" + p4, 1)

    # Insert Q10 after 4.2 (before ### 4.3 Registros de Recursos)
    p5 = "### 4.3 Registros de Recursos (A, AAAA, CNAME, MX, NS, PTR, SOA, TXT)"
    assert p5 in content
    content = content.replace(p5, q10 + "\n" + p5, 1)

    # Insert Q11 after 5.4 (before ## 6. Fontes Recomendadas na Internet)
    p6 = "## 6. Fontes Recomendadas na Internet"
    assert p6 in content
    content = content.replace(p6, q11 + "\n" + p6, 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("File 03 successfully enriched! Total questions:", len(re.findall(r"### Questão \d+", content)))


# ==============================================================================
# FILE 04: 04_protocolos_de_aplicacao_redes_sem_fio_e_seguranca_de_rede.md
# ==============================================================================
def enrich_file_04():
    path = os.path.join(BASE_DIR, "04_protocolos_de_aplicacao_redes_sem_fio_e_seguranca_de_rede.md")
    count, content = check_file(path)
    if count >= 10:
        print(f"File 04 already has {count} questions, skipping.")
        return

    q06 = """### Questão 06 (FGV - TRT / Analista Judiciário - TI - Inovações do Protocolo HTTP/2)
O protocolo **HTTP/2** (RFC 7540) foi desenvolvido pelo IETF com o objetivo central de mitigar as graves restrições de latência e concorrência inerentes ao protocolo HTTP/1.1 clássico.

A respeito das inovações arquiteturais introduzidas pelo HTTP/2, assinale a afirmativa correta:

* **A)** O HTTP/2 aboliu o uso de cabeçalhos e passou a transferir mensagens exclusivamente em linguagem assembly.
* **B)** O HTTP/2 substituiu o formato textual do HTTP/1.1 por um **protocolo binário estruturado em quadros (*Frames*) e fluxos (*Streams*)**, permitindo a **Multiplexação Completa** de múltiplas requisições e respostas bidirecionais concorrentes trafegando simultaneamente sobre uma **única conexão TCP**, eliminando o bloqueio de início de fila (*Head-of-Line Blocking*) na camada de aplicação e introduzindo a compressão de cabeçalhos via algoritmo **HPACK**.
* **C)** O HTTP/2 exige a abertura de 50 conexões TCP paralelas para cada imagem carregada em uma página web.
* **D)** O HTTP/2 é incompatível com criptografia TLS, funcionando exclusivamente em conexões HTTP não seguras na porta 80.
* **E)** O algoritmo HPACK do HTTP/2 foi projetado exclusivamente para descompactar arquivos de vídeo em formato AVI.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Os cabeçalhos permanecem essenciais no HTTP/2, porém são comprimidos pelo HPACK.
> - **B)** **CORRETA.** Avanços técnicos canônicos do **HTTP/2 (RFC 7540)**:
>   1. **Formato Binário:** Mensagens são estruturadas em quadros binários (*Frames* de dados, cabeçalhos, prioridade, etc.), sendo muito mais fáceis e rápidas de parsear por computadores do que o texto plano do HTTP/1.1.
>   2. **Multiplexação (Uma Única Conexão TCP):** Múltiplas requisições independentes e assíncronas viajam intercaladas (*interleaved*) em uma única conexão TCP persistente. Resolve o HoL Blocking na aplicação (uma requisição lenta não trava as demais).
>   3. **Compressão HPACK (RFC 7541):** Comprime cabeçalhos HTTP por codificação de Huffman e tabelas de indexação de cabeçalhos estática e dinâmica, eliminando o envio repetitivo de cookies e user-agents idênticos.
>   4. **Server Push:** Capacidade de o servidor enviar recursos preventivos ao cache do navegador antes mesmo de serem explicitamente solicitados.
> - **C)** Incorreta. O objetivo do HTTP/2 é exatamente o inverso: concentrar tudo em **uma única conexão TCP**.
> - **D)** Incorreta. Na prática dos navegadores modernos, o HTTP/2 exige obrigatoriamente transporte seguro sobre TLS (h2).
> - **E)** Incorreta. O HPACK é um algoritmo de compressão específico para cabeçalhos HTTP.
> 
> **Gabarito: B**

---
"""

    q07 = """### Questão 07 (FCC - TRT / Analista de Redes - HTTP/3 e o Protocolo QUIC sobre UDP)
Embora o HTTP/2 tenha solucionado o bloqueio de início de fila (*Head-of-Line Blocking*) na camada de aplicação, ele continuou sofrendo com o *Head-of-Line Blocking* na **Camada de Transporte**, decorrente da garantia de entrega estritamente sequencial e ordenada do protocolo TCP subjacente (onde a perda de um único pacote TCP paralisa todos os fluxos multiplexados).

Para superar definitivamente essa barreira física, a IETF padronizou o **HTTP/3** (RFC 9114), cuja principal inovação reside na substituição do TCP pelo protocolo:

* **A)** ICMP com criptografia DES.
* **B)** **QUIC** (*Quick UDP Internet Connections*), executado sobre o protocolo de transporte **UDP**, no qual as perdas de pacotes em um fluxo (*stream*) individual não bloqueiam os demais fluxos independentes, incorporando criptografia **TLS 1.3 nativa** em seu núcleo e permitindo o estabelecimento de conexão ultrarrápido com handshake de zero tempo de ida e volta (**0-RTT**).
* **C)** FTP tradicional com autenticação anônima.
* **D)** AppleTalk em cabos coaxiais antigos.
* **E)** SMTP executado diretamente sobre conexões seriais RS-232.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O ICMP é um protocolo utilitário de controle e diagnóstico (ping/traceroute), não servindo para transporte de aplicações web.
> - **B)** **CORRETA.** Revolução arquitetural do **HTTP/3 e QUIC (RFC 9000 / RFC 9114)**:
>   - **Fundamento:** O HTTP/3 abandona o TCP e roda no espaço de usuário sobre **UDP (User Datagram Protocol)**.
>   - **Eliminação do HoL Blocking de Transporte:** No QUIC, os *streams* multiplexados são gerenciados no nível do próprio protocolo de transporte. Se um pacote correspondente ao Stream 2 for perdido na rede, apenas o Stream 2 aguarda a retransmissão; os Streams 1, 3 e 4 continuam sendo entregues imediatamente à aplicação sem qualquer bloqueio.
>   - **Criptografia Integrada (TLS 1.3):** A segurança não é uma camada sobreposta como no TCP; o handshake do QUIC funde a negociação de transporte com o handshake do TLS 1.3, reduzindo o tempo de estabelecimento de conexão de múltiplos RTTs para **1-RTT** (ou **0-RTT** em conexões recorrentes).
>   - **Migração de Conexão (*Connection Migration*):** Utiliza um ID de Conexão (*Connection ID*) independente do IP; se o usuário sai do Wi-Fi e entra no 4G/5G, a conexão não cai nem precisa reiniciar o handshake.
> - **C)** Incorreta. FTP é protocolo de transferência de arquivos.
> - **D)** Incorreta. Protocolo legado proprietário da Apple da década de 1980.
> - **E)** Incorreta. Protocolo de envio de e-mails.
> 
> **Gabarito: B**

---
"""

    q08 = """### Questão 08 (FGV - TRT / Analista Judiciário - TI - Transferência de Arquivos Segura: SFTP vs. FTPS)
Em auditorias de sistemas governamentais, é frequente a necessidade de transferir arquivos volumosos contendo bases de dados e folhas de pagamento de órgãos fiscalizados para os servidores do tribunal.

A respeito da distinção técnica fundamental entre os protocolos de transferência segura **SFTP** (*SSH File Transfer Protocol*) e **FTPS** (*FTP over SSL/TLS*), assinale a afirmativa correta:

* **A)** O SFTP é uma extensão direta do protocolo FTP tradicional que utiliza duas portas de conexão (portas 20 e 21) com certificados X.509.
* **B)** O **SFTP** é um protocolo completamente independente do FTP clássico, funcionando como um subsistema executado sobre um canal seguro do protocolo **SSH (*Secure Shell*)**, utilizando uma **única porta de rede (porta padrão TCP 22)** para comandos e transferência de dados com autenticação baseada em chaves públicas ou senhas; ao passo que o **FTPS** é o protocolo FTP tradicional legado encapsulado por uma camada de criptografia SSL/TLS, exigindo múltiplos canais de comunicação (porta de comando TCP 21 e uma faixa dinâmica de portas para os canais de dados em modo passivo), o que gera frequentes conflitos com firewalls corporativos.
* **C)** O FTPS é proibido em redes IPv4 por ser um protocolo exclusivo de satélites espaciais.
* **D)** Ambos os protocolos utilizam exclusivamente o protocolo UDP sem criptografia.
* **E)** O SFTP transmite dados em texto claro e foi decifrado em 1995.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O SFTP não tem nenhuma relação com o protocolo FTP nem com suas portas; ele roda integralmente dentro do protocolo SSH.
> - **B)** **CORRETA.** Confronto arquitetural canônico:
>   - **SFTP (SSH File Transfer Protocol):** É uma extensão do SSH (porta TCP 22). Utiliza **uma única conexão TCP** multiplexada para envio de comandos de controle, transferência de arquivos e manipulação remota de diretórios. É extremamente amigável para firewalls corporativos (basta liberar a porta 22) e herda toda a infraestrutura de segurança do SSH (chaves assimétricas RSA/Ed25519, `known_hosts`).
>   - **FTPS (FTP over TLS/SSL):** É o FTP antigo (RFC 959) envolvido por TLS. Mantém a problemática arquitetura de canal duplo do FTP (um canal de controle na porta TCP 21 e múltiplos canais de dados dinâmicos na faixa efêmera em modo passivo), exigindo regras complexas de *Connection Tracking / Application Layer Gateway (ALG)* nos firewalls para autorizar as portas dinâmicas de dados.
> - **C)** Incorreta. FTPS é amplamente suportado na internet padrão.
> - **D)** Incorreta. Ambos usam conexões TCP confiáveis e criptografia de ponta a ponta.
> - **E)** Incorreta. O SFTP cifra todo o tráfego de ponta a ponta através da criptografia robusta do túnel SSH.
> 
> **Gabarito: B**

---
"""

    q09 = """### Questão 09 (FCC - TRT / Analista de Infraestrutura - Balanceamento de Carga: Camada 4 vs. Camada 7)
Na infraestrutura de datacenters de tribunais de contas, o balanceamento de carga (*Load Balancing*) distribui o tráfego dos sistemas de processo eletrônico entre múltiplos servidores de aplicação em cluster, operando tipicamente na **Camada 4 (Transporte)** ou na **Camada 7 (Aplicação)**.

A respeito das características que diferenciam um balanceador **Layer 4 (L4)** de um balanceador **Layer 7 (L7)**, assinale a afirmativa correta:

* **A)** O balanceador L7 é incapaz de ler o conteúdo da requisição HTTP, roteando pacotes apenas pelo endereço IP de destino.
* **B)** O balanceador **Layer 4 (L4)** toma decisões de roteamento em alta velocidade baseando-se exclusivamente em informações das camadas de rede e transporte (endereço IP de origem/destino e porta TCP/UDP), sem inspecionar a carga útil da aplicação; ao passo que o balanceador **Layer 7 (L7)** atua na camada de aplicação, inspecionando o conteúdo semântico da mensagem (cabeçalhos HTTP, URIs solicitadas, métodos `GET`/`POST`, cookies de sessão e dados de formulário), permitindo roteamento inteligente baseado em caminhos (ex.: direcionar `/api/` para um cluster de microsserviços e `/estaticos/` para outro), além de permitir terminação SSL/TLS e persistência de sessão baseada em cookies (*Sticky Sessions*).
* **C)** O balanceador L4 é exclusivo de cabos de fibra óptica submarinos.
* **D)** O balanceador L7 consome menos ciclos de CPU e memória do que o L4 por não analisar o cabeçalho das mensagens.
* **E)** Ambos os tipos exigem que todos os servidores web de destino possuam o mesmo endereço IP físico.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O balanceador L7 inspeciona minuciosamente todo o tráfego da camada de aplicação HTTP/HTTPS.
> - **B)** **CORRETA.** Comparativo técnico clássico de **Load Balancers**:
>   - **Layer 4 (L4 - Transporte):** Roteamento em nível de fluxo TCP/UDP. Olha apenas a tupla de 5 elementos (*IP Origem, Porta Origem, IP Destino, Porta Destino, Protocolo*). Não decifra a mensagem nem conhece HTTP. É extremamente veloz, consome pouca CPU e lida com centenas de milhares de conexões por segundo sem interferir nos dados.
>   - **Layer 7 (L7 - Aplicação):** Roteamento consciente do conteúdo (*Content-Aware / Application Routing*). Atua como um proxy reverso completo: termina a conexão TCP do cliente, decifra o TLS, analisa o payload HTTP e decide o servidor backend com base na URL (ex.: `/relatorios` $\to$ Servidor A; `/pagamentos` $\to$ Servidor B), cookies ou cabeçalhos. Oferece inteligência máxima e recursos como WAF e *Sticky Sessions*, com maior custo computacional de CPU/RAM.
> - **C)** Incorreta. Dispositivos lógicos aplicados em qualquer infraestrutura corporativa.
> - **D)** Incorreta. O L7 consome **muito mais recursos de CPU e memória** do que o L4 justamente porque precisa remontar pacotes TCP, decifrar criptografia SSL e analisar texto HTTP.
> - **E)** Incorreta. Os servidores do pool de backend possuem endereços IPs privados distintos para os quais o balanceador despacha o tráfego.
> 
> **Gabarito: B**

---
"""

    q10 = """### Questão 10 (FGV - TRT / Analista Judiciário - TI - Servidores Proxy: Forward Proxy vs. Reverse Proxy)
Os servidores proxy são intermediários de rede amplamente empregados para segurança, controle de acesso, anonimização e aceleração de tráfego.

A respeito da distinção funcional entre um **Forward Proxy** e um **Reverse Proxy**, assinale a afirmativa correta:

* **A)** O Forward Proxy fica posicionado na frente dos servidores web do tribunal para protegê-los contra invasões externas vindas da internet.
* **B)** O **Forward Proxy** é posicionado à frente dos **clientes internos da rede corporativa**, atuando em nome dos colaboradores para intermediar o acesso à internet externa, sendo utilizado para filtragem de conteúdo web indesejado, aplicação de políticas de DLP, cache de navegação e auditoria de acessos de saída; ao passo que o **Reverse Proxy** é posicionado à frente dos **servidores internos da instituição**, interceptando as requisições de clientes externos da internet e repassando-as aos servidores de aplicação backend, atuando para balanceamento de carga, terminação SSL/TLS, aceleração de cache de páginas e proteção contra ataques externos (como DDoS).
* **C)** O Reverse Proxy impede que os servidores internos recebam energia elétrica da rede predial.
* **D)** Ambos os proxies realizam rigorosamente a mesma função e não possuem nenhuma diferença de posicionamento ou objetivo arquitetural.
* **E)** O Forward Proxy é exclusivo de conexões via satélite do padrão DVB-S2.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Quem fica na frente dos servidores para protegê-los é o **Reverse Proxy** (Proxy Reverso).
> - **B)** **CORRETA.** Distinção arquitetural clássica entre os tipos de proxy:
>   - **Forward Proxy (Proxy de Saída):** O cliente interno sabe que está usando o proxy (ou é interceptado de modo transparente). O proxy esconde os clientes da internet: o site externo enxerga apenas o IP do proxy. Finalidades: controle de navegação corporativa, bloqueio de sites impróprios, auditoria de compliance e economia de banda por cache.
>   - **Reverse Proxy (Proxy Reverso / de Entrada):** Os clientes da internet não sabem que estão falando com um proxy; eles pensam que estão acessando diretamente o portal oficial do tribunal. O proxy esconde e protege os servidores internos de aplicação. Finalidades: segurança perimetral, ocultação da topologia de backend, terminação SSL (descarrega a criptografia), compressão gzip e balanceamento de carga entre nós do cluster.
> - **C)** Incorreta. Trata-se de software/hardware de rede de dados.
> - **D)** Incorreta. Possuem papéis e direções de tráfego diametralmente opostos.
> - **E)** Incorreta. São conceitos universais da arquitetura TCP/IP.
> 
> **Gabarito: B**

---
"""

    q11 = """### Questão 11 (FCC - TRT / Analista de Telecomunicações - Redes Sem Fio IEEE 802.11 e Frequências 2.4 GHz vs. 5 GHz)
A implantação de redes locais sem fio corporativas (*WLAN / Wi-Fi*) baseadas na família de padrões IEEE 802.11 requer o planejamento criterioso de frequências e canais para evitar interferências de rádio e degradação de sinal.

A respeito da comparação técnica entre as bandas de frequência de **2.4 GHz** e **5 GHz**, assinale a afirmativa correta:

* **A)** A banda de 2.4 GHz oferece maiores taxas de transmissão de dados e mais canais sem sobreposição do que a banda de 5 GHz.
* **B)** A frequência de **2.4 GHz** possui maior alcance geográfico e maior capacidade de penetração de obstáculos físicos (paredes e divisórias) devido ao seu comprimento de onda maior, porém sofre de grande congestionamento e dispõe de apenas **3 canais sem sobreposição mútua** no espectro padrão (canais 1, 6 e 11); ao passo que a frequência de **5 GHz** oferece larguras de canal muito maiores, taxas de transmissão significativamente mais elevadas e dezenas de canais descorrelacionados, com o *trade-off* de apresentar menor alcance útil e maior atenuação ao atravessar obstáculos sólidos.
* **C)** A banda de 5 GHz é totalmente imune a qualquer atenuação provocada por paredes de concreto armado.
* **D)** O padrão IEEE 802.11b opera exclusivamente na faixa de 60 GHz com velocidade de 10 Gigabits por segundo.
* **E)** Fornos micro-ondas e telefones sem fio antigos operam exclusivamente na faixa de 5 GHz, deixando a faixa de 2.4 GHz livre de qualquer interferência.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A banda de 5 GHz oferece taxas de transferência ordens de grandeza superiores e muito mais canais não sobrepostos.
> - **B)** **CORRETA.** Propriedades físicas fundamentais da radiofrequência em redes Wi-Fi:
>   - **Banda de 2.4 GHz:** Comprimento de onda de cerca de 12,5 cm. **Vantagem:** Alcance mais longo e melhor propagação através de obstáculos sólidos. **Desvantagens:** Banda estreita, extremamente congestionada (Bluetooth, micro-ondas, telefones sem fio) e dispõe de apenas **três canais que não se sobrepõem: 1, 6 e 11** (canais adjacentes sofrem interferência de canal adjacente).
>   - **Banda de 5 GHz:** Comprimento de onda de cerca de 6 cm. **Vantagens:** Mais de 20 canais sem sobreposição, suporte a canais agregados de 40, 80 e 160 MHz (Wi-Fi 5 e 6), fornecendo taxas de múltiplos Gigabits/s com baixíssima interferência. **Desvantagem:** Maior absorção pelo ar e severa atenuação por obstáculos físicos (paredes grossas atenuam fortemente o sinal).
> - **C)** Incorreta. Sinais de frequências mais altas sofrem atenuação significativamente mais severa ao atravessar materiais densos.
> - **D)** Incorreta. O 802.11b é um padrão legado de 1999 que operava em 2.4 GHz com taxa máxima de 11 Mbps.
> - **E)** Incorreta. Fornos micro-ondas operam exatamente na faixa de **2.4 GHz** (frequência de ressonância da água), sendo a principal fonte de interferência eletromagnética não-Wi-Fi nessa banda.
> 
> **Gabarito: B**

---
"""

    # Insert Q06 after 1.2 (before ### 1.3 HTTP/3 e o Protocolo QUIC sobre UDP)
    p1 = "### 1.3 HTTP/3 e o Protocolo QUIC sobre UDP"
    assert p1 in content
    content = content.replace(p1, q06 + "\n" + p1, 1)

    # Insert Q07 after 1.3 (before ### 1.4 HTTPS e TLS 1.3 Integrado)
    p2 = "### 1.4 HTTPS e TLS 1.3 Integrado"
    assert p2 in content
    content = content.replace(p2, q07 + "\n" + p2, 1)

    # Insert Q08 after 2.2 (before ### 2.3 Correio Eletrônico: SMTP vs. POP3 vs. IMAP)
    p3 = "### 2.3 Correio Eletrônico: SMTP vs. POP3 vs. IMAP"
    assert p3 in content
    content = content.replace(p3, q08 + "\n" + p3, 1)

    # Insert Q09 after 3.2 (before ### 3.3 Servidores Proxy: Forward Proxy vs. Reverse Proxy)
    p4 = "### 3.3 Servidores Proxy: Forward Proxy vs. Reverse Proxy"
    assert p4 in content
    content = content.replace(p4, q09 + "\n" + p4, 1)

    # Insert Q10 after 3.3 (before ## 4. Redes Sem Fio (IEEE 802.11 - Wi-Fi))
    p5 = "## 4. Redes Sem Fio (IEEE 802.11 - Wi-Fi)"
    assert p5 in content
    content = content.replace(p5, q10 + "\n" + p5, 1)

    # Insert Q11 after 4.2 (before ### 4.3 Mecanismo de Acesso ao Meio: CSMA/CA e o Problema do Nó Oculto (RTS/CTS))
    p6 = "### 4.3 Mecanismo de Acesso ao Meio: CSMA/CA e o Problema do Nó Oculto (RTS/CTS)"
    assert p6 in content
    content = content.replace(p6, q11 + "\n" + p6, 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("File 04 successfully enriched! Total questions:", len(re.findall(r"### Questão \d+", content)))


# ==============================================================================
# FILE 05: 05_computacao_em_nuvem_modelos_serverless_e_hibridos.md
# ==============================================================================
def enrich_file_05():
    path = os.path.join(BASE_DIR, "05_computacao_em_nuvem_modelos_serverless_e_hibridos.md")
    count, content = check_file(path)
    if count >= 10:
        print(f"File 05 already has {count} questions, skipping.")
        return

    q06 = """### Questão 06 (FGV - TRT / Analista Judiciário - TI - As Cinco Características Essenciais da Nuvem pelo NIST)
A publicação especial NIST SP 800-145 estabelece a definição formal e canônica de Computação em Nuvem aceita internacionalmente por governos e indústrias de tecnologia.

O framework do NIST estrutura a computação em nuvem em **Cinco Características Essenciais**, Três Modelos de Serviço e Quatro Modelos de Implantação. Assinale a afirmativa que apresenta corretamente as Cinco Características Essenciais:

* **A)** Uso exclusivo de software proprietário, pagamento antecipado em moeda estrangeira, conexão física serial, ausência de virtualização e suporte telefônico presencial.
* **B)** **Autosserviço sob Demanda** (*On-Demand Self-Service*), **Amplo Acesso de Rede** (*Broad Network Access*), **Pool de Recursos Compartilhados** (*Resource Pooling*), **Elasticidade Rápida** (*Rapid Elasticity*) e **Serviço Mensurado** (*Measured Service*).
* **C)** Criptografia simétrica, assinatura em papel moeda, arquitetura cliente-servidor centralizada em mainframe, roteamento RIP e ausência de APIs.
* **D)** Tolerância a falhas manual, ausência de medição de consumo, dependência de fitas magnéticas, escaneamento de portas TCP e gerência por e-mail.
* **E)** As características essenciais proíbem que mais de uma organização compartilhe os servidores físicos de um mesmo provedor de nuvem.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Características falsas que contrariam a própria essência de nuvem.
> - **B)** **CORRETA.** As **Cinco Características Essenciais do NIST (SP 800-145)**:
>   1. **Autosserviço sob Demanda (On-Demand Self-Service):** O consumidor provisiona poder de computação, armazenamento e rede unilateralmente e automaticamente, sem interação humana com o provedor.
>   2. **Amplo Acesso de Rede (Broad Network Access):** Os recursos são disponibilizados na rede e acessíveis por mecanismos padronizados através de plataformas heterogêneas (celulares, tablets, notebooks).
>   3. **Pool de Recursos Compartilhados (Resource Pooling):** Recursos computacionais do provedor são agrupados para atender múltiplos consumidores sob um modelo multilocatário (*Multi-Tenant*), com alocação dinâmica e abstração de localização.
>   4. **Elasticidade Rápida (Rapid Elasticity):** Recursos podem ser provisionados e liberados elasticamente, em alguns casos automaticamente, escalando rapidamente para cima ou para baixo conforme a demanda.
>   5. **Serviço Mensurado (Measured Service):** O controle e a otimização de recursos ocorrem por meio de medição automática e transparente (*Pay-per-Use* / pague pelo que usar).
> - **C)** Incorreta. Não são características definidoras de computação em nuvem.
> - **D)** Incorreta. A nuvem exige medição estrita de consumo (*metering*) e orquestração automatizada.
> - **E)** Incorreta. O compartilhamento multilocatário (*Resource Pooling*) é um dos pilares centrais da economia de escala em nuvem.
> 
> **Gabarito: B**

---
"""

    q07 = """### Questão 07 (FCC - TRT / Analista de Tecnologia da Informação - Modelos de Implantação de Nuvem)
A definição do modelo de implantação de computação em nuvem determina o escopo de governança, compartilhamento de infraestrutura física e fronteiras de segurança entre organizações.

Considere um consórcio de Tribunais de Contas Estaduais que resolve implantar uma infraestrutura de nuvem conjunta para compartilhar ferramentas de auditoria e bases de jurisprudência, onde a infraestrutura é compartilhada estritamente entre instituições que possuem missões institucionais, requisitos de segurança e preocupações de conformidade comuns.

Segundo a taxonomia do NIST SP 800-145, esse modelo de implantação é classificado formalmente como:

* **A)** Nuvem Pública (*Public Cloud*).
* **B)** Nuvem Privada Monolítica (*Private Cloud*).
* **C)** Nuvem Comunitária (*Community Cloud*).
* **D)** Nuvem Descentralizada P2P (*Peer-to-Peer Cloud*).
* **E)** Nuvem Não Comercial Externa (*External Off-Grid Cloud*).

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Na *Nuvem Pública*, a infraestrutura é aberta ao público em geral e a qualquer empresa privada.
> - **B)** Incorreta. A *Nuvem Privada* é provisionada para uso exclusivo de **uma única organização** isoladamente.
> - **C)** **CORRETA.** A **Nuvem Comunitária (Community Cloud - NIST SP 800-145)**:
>   - É provisionada para uso exclusivo de uma **comunidade específica de organizações** que compartilham interesses, objetivos e requisitos regulatórios comuns (por exemplo: conformidade com a Lei de Responsabilidade Fiscal, auditoria governamental, interoperabilidade do controle externo ou segurança nacional).
>   - Pode ser gerenciada e operada pelas próprias organizações participantes, por uma terceira parte contratada ou por uma combinação mútua, e pode residir física e logicamente dentro ou fora das instalações dos órgãos (*on-premises* ou *off-premises*).
> - **D)** Incorreta. Modelo inexistente na taxonomia oficial do NIST.
> - **E)** Incorreta. Categoria inexistente na norma.
> 
> **Gabarito: C**

---
"""

    q08 = """### Questão 08 (FGV - TRT / Analista Judiciário - TI - Matriz de Responsabilidade Compartilhada na Nuvem)
O modelo de segurança na computação em nuvem baseia-se na **Matriz de Responsabilidade Compartilhada** (*Shared Responsibility Model*) entre o Provedor de Nuvem (*Cloud Service Provider - CSP*) e o Cliente (a organização governamental contratante).

A respeito da distribuição de responsabilidades de segurança da informação no modelo **IaaS** (*Infrastructure as a Service*), assinale a afirmativa correta:

* **A)** No modelo IaaS, o provedor de nuvem é integralmente responsável pela aplicação de correções de segurança (*patches*) do sistema operacional convidado, pelo controle de acesso aos bancos de dados do cliente e pela configuração do firewall do sistema operacional.
* **B)** No modelo **IaaS**, a responsabilidade é estritamente demarcada: o **Provedor de Nuvem** é responsável pela **segurança DA nuvem** (segurança física dos datacenters, hardware de servidores, subsistemas de armazenamento e camada de virtualização/hipervisor); ao passo que o **Cliente** é integralmente responsável pela **segurança NA nuvem** (instalação e aplicação de patches no Sistema Operacional Convidado da VM, configuração de firewalls lógicos de host / *Security Groups*, gestão de identidades e acessos - IAM, middleware, aplicações instaladas e proteção/criptografia dos seus próprios dados).
* **C)** O cliente de IaaS deve responsabilizar-se pela manutenção física do gerador a diesel do datacenter do provedor.
* **D)** Em modelos SaaS (Software as a Service), o cliente tem a obrigação técnica de atualizar o firmware dos roteadores do provedor.
* **E)** A responsabilidade pela classificação e conformidade dos dados transferidos para a nuvem recai sempre e exclusivamente sobre o fabricante dos processadores de hardware.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. No IaaS, o sistema operacional da máquina virtual (Linux/Windows) é de responsabilidade estrita e exclusiva do **cliente**. O provedor entrega a VM e não tem acesso às credenciais internas do SO do cliente.
> - **B)** **CORRETA.** Axioma da **Responsabilidade Compartilhada (AWS, Azure, Google Cloud e CSA)**:
>   - **Segurança DA Nuvem (*Security OF the Cloud* - Dever do Provedor):** Instalações físicas, climatização, energia, servidores físicos, hipervisores (KVM/Nitro/Hyper-V) e rede física.
>   - **Segurança NA Nuvem (*Security IN the Cloud* - Dever do Cliente em IaaS):** O cliente gerencia o Sistema Operacional (atualizações de patches de kernel), tabelas de roteamento e *Security Groups*, privilégios de usuários (IAM), serviços em execução, integridade das aplicações desenvolvidas e criptografia dos dados armazenados e em trânsito.
>   - À medida que se sobe na camada de abstração (PaaS e SaaS), o provedor assume camadas adicionais (em PaaS, o SO e middleware passam a ser mantidos pelo provedor; em SaaS, o provedor mantém até a aplicação inteira), mas **a governança e classificação dos dados pertencem sempre ao Cliente**.
> - **C)** Incorreta. Manutenção física de datacenter é responsabilidade absoluta do provedor em qualquer modelo.
> - **D)** Incorreta. No SaaS, o cliente gerencia apenas os dados e permissões dos usuários finais daquele software.
> - **E)** Incorreta. A custódia e governança legal dos dados é responsabilidade primária do cliente (*data controller*).
> 
> **Gabarito: B**

---
"""

    q09 = """### Questão 09 (FGV - TRT / Analista Judiciário - TI - Paradigma Serverless e o Fenômeno do Cold Start)
A computação sem servidor (*Serverless / Function-as-a-Service - FaaS*, como AWS Lambda, Azure Functions e Google Cloud Functions) oferece alta abstração de infraestrutura, escala automática orientada a eventos e cobrança por tempo de execução.

No entanto, uma das principais características operacionais a ser gerenciada por arquitetos de software em soluções FaaS é o **Cold Start** (*Inicialização a Frio*). O fenômeno do *Cold Start* é definido quando:

* **A)** O processador do servidor desliga permanentemente por congelamento criogênico na câmara frigorífica.
* **B)** Uma função Serverless é invocada após um período de inatividade (ou quando a demanda aumenta subitamente e exige novas réplicas paralelas), forçando a plataforma de nuvem a **alocar um novo contêiner de micro-máquina virtual, baixar a imagem de código, inicializar o ambiente de execução de runtime (ex.: JVM, Node.js ou Python) e carregar as bibliotecas na memória**, introduzindo uma latência perceptível no tempo de resposta da primeira requisição; sendo mitigado por técnicas como manter instâncias pré-aquecidas (**Provisioned Concurrency**) ou otimizar o tamanho do pacote de código.
* **C)** A função serverless rejeita comandos executados em dias de inverno.
* **D)** O código da função é deletado da nuvem caso a temperatura ambiente ultrapasse 25 graus Celsius.
* **E)** O sistema operacional trava e exige que o desenvolvedor reinicie manualmente a placa-mãe no datacenter.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Metáfora física descabida.
> - **B)** **CORRETA.** Mecânica do **Cold Start em Arquiteturas Serverless (FaaS)**:
>   - Em FaaS, quando não há requisições, o número de instâncias ativas reduz-se a zero (*Scale-to-Zero*), poupando custos de faturamento.
>   - Quando uma nova requisição chega e não há nenhuma instância previamente aquecida (*Warm Instance*) em memória, ocorre o **Cold Start**:
>     1. O orquestrador da nuvem instancia um microcontêiner isolado (ex.: Firecracker MicroVM).
>     2. Baixa o código da aplicação e dependências.
>     3. Inicializa o interpretador ou máquina virtual (linguagens com runtimes pesados como Java/JVM ou .NET sofrem *cold starts* mais longos do que Go, Rust, Node.js ou Python).
>     4. Executa os blocos estáticos de inicialização de código (como conexões com banco).
>     5. Finalmente processa o evento e responde.
>   - **Mitigação:** Uso de **Provisioned Concurrency (Concorrência Provisionada)**, que mantém um pool mínimo de instâncias sempre inicializadas e prontas para responder em milissegundos sem *cold start*.
> - **C)** Incorreta. Fatores climáticos não se aplicam à lógica de invocação de software.
> - **D)** Incorreta. O código fica persistido com segurança no repositório do provedor.
> - **E)** Incorreta. O desenvolvedor não gerencia hardware ou SO no paradigma serverless.
> 
> **Gabarito: B**

---
"""

    q10 = """### Questão 10 (FCC - TRT / Analista de Tecnologia da Informação - Padrões de Resiliência e Arquiteturas Multi-AZ)
No desenho de soluções corporativas de missão crítica em nuvens públicas, arquitetos de infraestrutura projetam sistemas para tolerar falhas físicas catastróficas sem interrupção de serviço.

A respeito das construções topológicas de **Regiões** e **Zonas de Disponibilidade (*Availability Zones - AZs*)**, assinale a afirmativa correta:

* **A)** Uma Região de nuvem é composta por apenas um único computador pessoal conectado a uma tomada comum.
* **B)** Uma Zona de Disponibilidade (AZ) é composta por um ou mais datacenters físicos discretos e independentes, dotados de infraestrutura autônoma de energia, refrigeração e segurança física; e uma **Região** é uma área geográfica que abriga **múltiplas AZs isoladas entre si contra desastres comuns, interconectadas por redes de fibra óptica privadas de altíssima largura de banda e ultrabaixa latência**, permitindo a implantação de bancos de dados e aplicações em arquitetura **Multi-AZ** para failover automático sem perda perceptível de dados.
* **C)** Duas Zonas de Disponibilidade da mesma região devem obrigatoriamente compartilhar o mesmo transformador de energia da concessionária e a mesma rede de água predial.
* **D)** O padrão Multi-AZ proíbe que existam servidores de aplicação espelhados em mais de uma localidade.
* **E)** Regiões de nuvem nunca podem ser interconectadas pela internet global.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Uma região abriga múltiplos datacenters de classe mundial com milhares de servidores.
> - **B)** **CORRETA.** Topologia de infraestrutura global dos grandes provedores de nuvem (AWS, GCP, Azure, Oracle):
>   - **Zona de Disponibilidade (Availability Zone - AZ):** Datacenter (ou grupo de datacenters) físico isolado contra inundações, falhas elétricas e desastres locais. Cada AZ tem seus próprios geradores a diesel, linhas elétricas redundantes e sistemas de refrigeração.
>   - **Região (Region):** Área geográfica delimitada (ex.: Região São Paulo `sa-east-1`, Região Virgínia do Norte `us-east-1`). É composta por no mínimo **três AZs distintas e distantes entre si** (para que uma inundação ou queda regional de energia não atinja as demais), porém próximas o bastante para serem unidas por enlaces ópticos de latência menor que 2 milissegundos.
>   - **Padrão Multi-AZ:** Ao distribuir instâncias e réplicas de banco de dados síncronas entre ao menos duas AZs diferentes, o sistema suporta a queda física total de um datacenter inteiro com *failover* automático e disponibilidade contínua dos serviços públicos.
> - **C)** Incorreta. A regra de ouro do isolamento de AZs é exatamente a **independência total de infraestrutura crítica** (redes elétricas e de telecomunicações distintas).
> - **D)** Incorreta. O Multi-AZ incentiva exatamente o espelhamento redundante ativo.
> - **E)** Incorreta. Regiões conectam-se através do backbone de fibra privado do provedor e da internet mundial.
> 
> **Gabarito: B**

---
"""

    q11 = """### Questão 11 (FGV - TRT / Analista Judiciário - Governança Cloud e FinOps - Da CapEx para OpEx e Rightsizing)
A governança financeira e orçamentária da computação em nuvem no setor público consolidou a disciplina de **FinOps** (*Cloud Financial Management*), unindo engenharia de software, operações de infraestrutura e gestão financeira.

No âmbito dos princípios de FinOps e planejamento econômico em nuvem, a transição contábil do modelo **CapEx para OpEx** e a técnica de **Rightsizing** caracterizam-se por:

* **A)** A substituição de despesas operacionais contínuas por compras maciças de hardware físico próprio a cada dez anos.
* **B)** A transição de despesas de capital (**CapEx - Capital Expenditure**, com vultosos investimentos iniciais em ativos físicos depreciáveis e superdimensionados) para despesas operacionais (**OpEx - Operational Expenditure**, com custos variáveis baseados no consumo real e sob demanda); e o **Rightsizing** como a prática contínua de analisar o consumo real de CPU, memória e armazenamento das cargas de trabalho para redimensionar instâncias excessivamente grandes para configurações de tamanho estritamente adequado às suas necessidades reais, eliminando o desperdício de dinheiro público.
* **C)** O Rightsizing consiste em aumentar indefinidamente o tamanho de todas as máquinas virtuais para a maior capacidade do catálogo do provedor sem verificar o consumo.
* **D)** O FinOps proíbe que órgãos públicos realizem qualquer tipo de controle de custos de computação em nuvem.
* **E)** CapEx e OpEx são índices de criptografia de ponta a ponta que dispensam aprovação orçamentária no Plano Plurianual (PPA).

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A nuvem promove exatamente a direção oposta: abandona a compra de hardware antecipado e adota serviços operacionais contínuos sob demanda.
> - **B)** **CORRETA.** Pilares econômicos do **FinOps na Nuvem**:
>   - **CapEx (Capital Expenditure):** Compra tradicional de datacenters locais: exige previsão orçamentária para 5 anos, aquisição de servidores superdimensionados para picos raros, contratos de garantia caros e depreciação patrimonial estática.
>   - **OpEx (Operational Expenditure):** A organização paga periodicamente apenas pelos recursos de computação que efetivamente consome mês a mês, adaptando a despesa ao ciclo orçamentário anual e à volatilidade da demanda.
>   - **Rightsizing (Dimensionamento Correto):** Técnica fundamental de otimização de custos em FinOps. Se um servidor virtual foi provisionado com 64 núcleos de CPU e 256 GB de RAM, mas a telemetria comprova que ele opera com média de 5% de uso nos últimos 90 dias, o *rightsizing* rebaixa a instância para 8 núcleos e 32 GB, reduzindo o custo daquela fatura em até 70% sem degradar a performance do sistema.
> - **C)** Incorreta. Superdimensionar desnecessariamente é a causa primária do desperdício de recursos públicos em nuvem que o FinOps combate.
> - **D)** Incorreta. FinOps é a própria prática de controle rigoroso e prestação de contas de custos.
> - **E)** Incorreta. São conceitos contábeis e financeiros clássicos de orçamento público e empresarial.
> 
> **Gabarito: B**

---
"""

    # Insert Q06 after 1.2 (before ### 1.3 Os Quatro Modelos de Implantação)
    p1 = "### 1.3 Os Quatro Modelos de Implantação (Pública, Privada, Comunitária, Híbrida)"
    assert p1 in content
    content = content.replace(p1, q06 + "\n" + p1, 1)

    # Insert Q07 after 1.3 (before ## 2. Modelos de Serviço e Matriz de Responsabilidade Compartilhada)
    p2 = "## 2. Modelos de Serviço e Matriz de Responsabilidade Compartilhada"
    assert p2 in content
    content = content.replace(p2, q07 + "\n" + p2, 1)

    # Insert Q08 after 2.2 (before ## 3. Computação Serverless (FaaS - Function as a Service))
    p3 = "## 3. Computação Serverless (FaaS - Function as a Service)"
    assert p3 in content
    content = content.replace(p3, q08 + "\n" + p3, 1)

    # Insert Q09 after 3.3 (before ## 4. Arquiteturas de Alta Disponibilidade e Escalabilidade em Nuvem)
    p4 = "## 4. Arquiteturas de Alta Disponibilidade e Escalabilidade em Nuvem"
    assert p4 in content
    content = content.replace(p4, q09 + "\n" + p4, 1)

    # Insert Q10 after 4.3 (before ## 5. Integração Híbrida e Governança Financeira (FinOps))
    p5 = "## 5. Integração Híbrida e Governança Financeira (FinOps)"
    assert p5 in content
    content = content.replace(p5, q10 + "\n" + p5, 1)

    # Insert Q11 after 5.3 (before ## 6. Fontes Recomendadas na Internet)
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
