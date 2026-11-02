# 04 - Protocolos de Aplicação, Segurança de Rede e Redes Sem Fio

> **Matéria:** Sistemas Operacionais, Redes e Computação em Nuvem  
> **Cargo:** B02 – Técnico de Controle Externo – Especialidade: Tecnologia da Informação  
> **Arquivo:** `04_protocolos_de_aplicacao_redes_sem_fio_e_seguranca_de_rede.md`  

---

## 📌 Ementa / Itens do Edital
- Protocolos da camada de aplicação e transporte:
    - Evolução da Web: HTTP/1.1, HTTP/2, HTTP/3 e HTTPS
    - Gerenciamento e transferência: SSH, FTP/SFTP
    - Correio eletrônico: SMTP, IMAP e POP3
- Tecnologias de interconexão e segurança perimetral: VPN, Balanceamento de Carga, Proxies e Firewalls
- Noções de redes sem fio (Padrões IEEE 802.11 e segurança Wi-Fi)

---

## 🧭 Sumário

1. [Evolução dos Protocolos Web: HTTP/1.1, HTTP/2, HTTP/3 e HTTPS](#1-evolucao-dos-protocolos-web-http11-http2-http3-e-https)
    1. [HTTP/1.1 e o Bloqueio de Início de Fila (Head-of-Line Blocking) na Aplicação](#11-http11-e-o-bloqueio-de-inicio-de-fila-head-of-line-blocking-na-aplicacao)
    2. [HTTP/2: Formato Binário, Multiplexação de Streams e Compressão HPACK](#12-http2-formato-binario-multiplexacao-de-streams-e-compressao-hpack)
    3. [HTTP/3 e o Protocolo QUIC sobre UDP](#13-http3-e-o-protocolo-quic-sobre-udp)
    4. [HTTPS e TLS 1.3 Integrado](#14-https-e-tls-13-integrado)
    5. [Teste 443](#Teste-443)
    6. [Teste 444](#Teste-444)
    7. [Teste 445](#Teste-445)
2. [Protocolos Utilitários, Transferência de Arquivos e Correio Eletrônico](#2-protocolos-utilitarios-transferencia-de-arquivos-e-correio-eletronico)
    1. [SSH (Secure Shell) e Redirecionamento de Portas](#21-ssh-secure-shell-e-redirecionamento-de-portas)
    2. [Transferência de Arquivos: FTP vs. FTPS vs. SFTP](#22-transferencia-de-arquivos-ftp-vs-ftps-vs-sftp)
    3. [Correio Eletrônico: SMTP vs. POP3 vs. IMAP](#23-correio-eletronico-smtp-vs-pop3-vs-imap)
    4. [Teste 446](#Teste-446)
    5. [Teste 447](#Teste-447)
3. [Elementos de Borda e Segurança de Rede: VPN, IPsec, Balanceadores e Proxies](#3-elementos-de-borda-e-seguranca-de-rede-vpn-ipsec-balanceadores-e-proxies)
    1. [Arquitetura IPsec: Cabeçalhos AH vs. ESP e Modos Transporte vs. Túnel](#31-arquitetura-ipsec-cabecalhos-ah-vs-esp-e-modos-transporte-vs-tunel)
    2. [Balanceadores de Carga: Camada 4 (L4) vs. Camada 7 (L7)](#32-balanceadores-de-carga-camada-4-l4-vs-camada-7-l7)
    3. [Servidores Proxy: Forward Proxy vs. Reverse Proxy](#33-servidores-proxy-forward-proxy-vs-reverse-proxy)
    4. [Teste 448](#Teste-448)
    5. [Teste 449](#Teste-449)
    6. [Teste 450](#Teste-450)
4. [Redes Sem Fio (IEEE 802.11 - Wi-Fi)](#4-redes-sem-fio-ieee-80211-wi-fi)
    1. [Evolução dos Padrões 802.11 (Wi-Fi 4, Wi-Fi 5 e Wi-Fi 6/6E)](#41-evolucao-dos-padroes-80211-wi-fi-4-wi-fi-5-e-wi-fi-66e)
    2. [Frequências de Operação: 2.4 GHz vs. 5 GHz](#42-frequencias-de-operacao-24-ghz-vs-5-ghz)
    3. [Mecanismo de Acesso ao Meio: CSMA/CA e o Problema do Nó Oculto (RTS/CTS)](#43-mecanismo-de-acesso-ao-meio-csmaca-e-o-problema-do-no-oculto-rtscts)
    4. [Evolução da Segurança Sem Fio: WEP, WPA, WPA2 e WPA3 (Personal vs. Enterprise)](#44-evolucao-da-seguranca-sem-fio-wep-wpa-wpa2-e-wpa3-personal-vs-enterprise)
    5. [Teste 451](#Teste-451)
    6. [Teste 452](#Teste-452)
    7. [Teste 453](#Teste-453)
6. [Fontes Recomendadas na Internet](#6-fontes-recomendadas-na-internet)

---

## 1. Evolução dos Protocolos Web: HTTP/1.1, HTTP/2, HTTP/3 e HTTPS

### 1.1 HTTP/1.1 e o Bloqueio de Início de Fila (Head-of-Line Blocking) na Aplicação

O protocolo **HTTP/1.1** (RFC 2616) estruturou a comunicação na web durante duas décadas. Ele trouxe como avanço o suporte a **conexões persistentes (*Keep-Alive*)**, permitindo que uma mesma conexão TCP fosse reaproveitada para transferir múltiplos recursos sem a necessidade de reabrir o handshake a cada arquivo.

Contudo, o HTTP/1.1 padece de uma limitação arquitetural grave:

- As mensagens trafegam em formato **estritamente textual e sequencial** no modelo requisição-resposta.
- Se uma página web demanda dezenas de imagens, folhas de estilo CSS e scripts JavaScript, o cliente envia uma requisição e precisa aguardar o servidor responder integralmente antes de enviar a próxima.
- Esse fenômeno é denominado **Bloqueio de Início de Fila na Aplicação (*Head-of-Line Blocking / HoL Blocking*)**: se a primeira requisição for lenta ou complexa para o backend processar, todos os demais recursos da página ficam bloqueados na fila do navegador. Para mitigar o problema, os navegadores passaram a abrir de 6 a 8 conexões TCP concorrentes com o mesmo domínio, sobrecarregando os servidores.

### 1.2 HTTP/2: Formato Binário, Multiplexação de Streams e Compressão HPACK

Padronizado pela RFC 7540, o **HTTP/2** reformulou a camada de aplicação sem alterar a semântica básica (métodos GET/POST, cabeçalhos e códigos de status HTTP continuam os mesmos):

1. **Protocolo Estritamente Binário:** Substituiu o texto ASCII puro por uma camada de enquadramento binário estruturada em **Quadros (*Frames*)** e **Fluxos (*Streams*)**.
2. **Multiplexação Verdadeira:** Múltiplas requisições e respostas podem trafegar de forma intercalada, bidirecional e simultânea sobre uma **única conexão TCP aberta**. Um arquivo CSS pesado não bloqueia mais o tráfego de imagens leves.
3. **Compressão de Cabeçalhos (HPACK):** Utiliza tabelas estáticas e dinâmicas associadas à codificação Huffman para eliminar a repetição redundante de cabeçalhos volumosos (como cookies e user-agents).
4. **Server Push:** O servidor pode enviar antecipadamente recursos essenciais ao cliente (como uma folha de estilo `style.css`) antes mesmo de o navegador interpretá-la e requisitá-la explicitamente.

#### O Gargalo Restante do HTTP/2: HoL Blocking no Transporte TCP
Embora o HTTP/2 tenha solucionado o bloqueio de início de fila na aplicação, ele transferiu o problema para a **Camada de Transporte (TCP)**:

- Como todos os streams do site compartilham a mesma e única conexão TCP, se um único pacote TCP for corrompido ou perdido na rede, o mecanismo de confiabilidade do TCP obriga o receptor a paralisar **a entrega de todos os outros streams da conexão** até que o pacote faltante seja retransmitido (*TCP Head-of-Line Blocking*).

### 1.3 HTTP/3 e o Protocolo QUIC sobre UDP

Para eliminar em definitivo qualquer forma de bloqueio em redes móveis e de alta latência, a IETF padronizou o **HTTP/3** (RFC 9114), substituindo o TCP pelo protocolo de transporte **QUIC (*Quick UDP Internet Connections* - RFC 9000)**, que opera sobre datagramas **UDP (Porta UDP 443)**:

```mermaid
flowchart TD
    subgraph HTTP2_Transporte["HTTP/2 sobre TCP (Problema do Head-of-Line Blocking no Transporte)"]
        StreamA["Stream 1 (HTML)"]
        StreamB["Stream 2 (CSS)"]
        StreamC["Stream 3 (IMG)"]
        StreamA & StreamB & StreamC --> TCP_Pipe["Conexão Única TCP"]
        TCP_Pipe --> PacotePerdido["Pacote TCP da Imagem Perdido!"]
        PacotePerdido --> Travamento["Toda a conexão é paralisada até a retransmissão pelo TCP!"]
    end

    subgraph HTTP3_Transporte["HTTP/3 sobre QUIC/UDP (Isolamento Total de Streams)"]
        QStreamA["Stream 1 (HTML)"]
        QStreamB["Stream 2 (CSS)"]
        QStreamC["Stream 3 (IMG)"]
        QStreamA & QStreamB & QStreamC --> QUIC_UDP["Datagramas QUIC/UDP"]
        QUIC_UDP --> QPacotePerdido["Pacote UDP da Imagem Perdido!"]
        QPacotePerdido --> QIsolamento["Apenas o Stream 3 aguarda; Stream 1 e 2 continuam fluindo!"]
    end
```

#### Inovações Tecnológicas do HTTP/3 (QUIC):
- **Eliminação Total do HoL Blocking:** Os streams dentro do QUIC são verdadeiramente isolados. A perda de um pacote no fluxo da imagem congela apenas o processamento da imagem, enquanto o código HTML e o script JavaScript continuam sendo entregues imediatamente ao navegador.
- **Handshake Acelerado (0-RTT e 1-RTT):** Como o controle de transporte e a criptografia TLS 1.3 são integrados no mesmo protocolo, a conexão segura é estabelecida em apenas 1 RTT (ou 0-RTT se o host já for conhecido), contra 2 a 3 RTTs exigidos pelo par TCP + TLS 1.2.
- **Migração de Conexão Resiliente (*Connection Migration*):** A conexão QUIC não é identificada pela 4-tupla tradicional (IP de origem, IP de destino, porta de origem, porta de destino), mas por um identificador exclusivo de 64 bits chamado **Connection ID**. Se o usuário sair da rede Wi-Fi de casa e entrar na rede móvel 5G (mudando completamente o endereço IP do smartphone), **a sessão de download, streaming ou chamada de vídeo NÃO cai nem reinicia**, migrando de forma totalmente transparente.
- **Compressão QPACK:** Evolução do algoritmo HPACK adaptada para lidar com pacotes que chegam fora de ordem sobre o transporte UDP.

### 1.4 HTTPS e TLS 1.3 Integrado

O **HTTPS** nada mais é do que o tráfego HTTP executado sobre uma camada de segurança de transporte criptográfica:

- **TLS 1.3 (RFC 8446):** Padrão moderno obrigatório que aboliu cifras antigas fracas ou suscetíveis a ataques (eliminou suporte a RC4, 3DES, CBC, MD5 e trocas estáticas de chave RSA).
- **Forward Secrecy Mandatório:** O TLS 1.3 exige o uso de algoritmos de troca de chave efêmera (como ECDHE), garantindo que, mesmo que a chave privada do servidor web seja roubada no futuro, o tráfego gravado no passado não poderá ser decifrado.
- No HTTP/3, o **TLS 1.3 é embutido nativamente no QUIC**, não existindo HTTP/3 em texto claro na especificação padrão.

---

## 2. Protocolos Utilitários, Transferência de Arquivos e Correio Eletrônico

### 2.1 SSH (Secure Shell) e Redirecionamento de Portas

O protocolo **SSH** opera na **porta TCP 22** e provê comunicação criptografada segura para administração remota de servidores, transferência de arquivos e execução remota de comandos, substituindo protocolos inseguros legados (Telnet, rlogin):

- **Autenticação:** Baseada em senhas ou pares de chaves criptográficas assimétricas (RSA, Ed25519), onde a chave pública fica registrada no arquivo `~/.ssh/authorized_keys` do servidor remoto e a chave privada permanece protegida sob custódia do usuário.
- **Túneis e Redirecionamento de Portas (*Port Forwarding*):**
    - *Local Port Forwarding (`ssh -L local_port:target_host:target_port user@server`):* Encaminha o tráfego de uma porta local da estação do administrador através do túnel criptografado SSH para um serviço interno na rede remota (ex.: acessar uma base de dados inacessível pela Internet).
    - *Remote Port Forwarding (`ssh -R remote_port:target_host:target_port user@server`):* Encaminha tráfego recebido em uma porta do servidor remoto de volta para um serviço rodando na máquina local do administrador.
    - *Dynamic Port Forwarding (`ssh -D local_port user@server`):* Transforma a sessão SSH em um servidor proxy local do tipo SOCKS4/SOCKS5.

### 2.2 Transferência de Arquivos: FTP vs. FTPS vs. SFTP

| Protocolo | Portas de Transporte Utilizadas | Criptografia / Segurança | Arquitetura e Relação com FTP |
|---|---|---|---|
| **FTP** (*File Transfer Protocol*) | **TCP 21** (Controle) e **TCP 20** (Dados no modo ativo) | **NENHUMA.** Usuário, senha e conteúdo dos arquivos transitam em texto claro puro. | Protocolo legado original. Opera com duas conexões distintas (modo Ativo vs. modo Passivo/PASV). |
| **FTPS** (*FTP over SSL/TLS*) | TCP 21 (Controle) + Portas de Dados dinâmicas protegidas | Criptografia via TLS/SSL aplicada sobre as conexões de controle e dados do FTP. | É o protocolo FTP clássico encapsulado em uma sessão TLS. Requer abertura de faixas complexas de portas no firewall. |
| **SFTP** (*SSH File Transfer Protocol*) | **Apenas a porta TCP 22** | Criptografia forte de ponta a ponta e autenticação por chaves SSH. | **NÃO tem nenhuma relação com o FTP!** É um subsistema de extensão que opera inteiramente dentro de uma sessão SSH estabelecida. |

### 2.3 Correio Eletrônico: SMTP vs. POP3 vs. IMAP

O tráfego de correio eletrônico na Internet divide-se claramente entre envio/retransmissão e acesso/leitura:

```mermaid
flowchart LR
    MUA_Envio["Cliente Remetente (MUA)"] -->|"SMTP (Porta 587 STARTTLS)"| MTA_Origem["Servidor de Correio Origem (MTA)"]
    MTA_Origem -->|"SMTP (Porta 25)"| MTA_Destino["Servidor de Correio Destino (MTA)"]
    MTA_Destino -->|"IMAP (Porta 993) ou POP3 (Porta 995)"| MUA_Destino["Cliente Destinatário (MUA)"]
```

#### Protocolos em Detalhes:
1. **SMTP (*Simple Mail Transfer Protocol* - Portas TCP 25 e TCP 587):**
    - É um protocolo do tipo **Push (Envio)**.
    - Utilizado pelo cliente para submeter e-mails ao seu servidor (porta 587 com autenticação e STARTTLS) e utilizado para retransmitir e-mails entre servidores de correio na Internet (porta 25).

2. **POP3 (*Post Office Protocol v3* - Portas TCP 110 e TCP 995 com SSL):**
    - É um protocolo do tipo **Pull (Recuperação)**.
    - Baixa as mensagens do servidor para a máquina local do usuário e, por padrão histórico, **remove as mensagens da caixa postal do servidor**. Não suporta criação nem sincronização de pastas remotas.

3. **IMAP (*Internet Message Access Protocol* - Portas TCP 143 e TCP 993 com SSL):**
    - É um protocolo do tipo **Pull (Acesso e Sincronização)**.
    - Mantém as mensagens, pastas customizadas, marcações de lido/não-lido e rascunhos **armazenados permanentemente no servidor central**. Permite que o usuário consulte sua caixa de correio através de múltiplos dispositivos (smartphone, webmail, notebook) com sincronização em tempo real.

---

### Teste 001
**(FGV – TCE/GO – 2024 – Analista de Controle Externo - Tecnologia da Informação)**
O Sistema de Nomes de Domínios (DNS) é uma aplicação cliente/servidor que associa cada host na Internet com um nome de domínio exclusivo facilmente identificável. Sobre DNS, é correto afirmar que

* **A)** existem dois tipos de registros DNS: registros de consultas e registros de respostas.
* **B)** na resolução iterativa, o cliente transmite sua solicitação a um servidor que, no final do processo, retorna uma resposta.
* **C)** um FQDN é um nome de domínio que não inclui todos os níveis existentes entre o host e o nó raiz.
* **D)** o DNS usa os serviços de UDP para mensagens menores que 1024 bytes, caso contrário é usado o TCP.
* **E)** o DNS pode ser representado por uma estrutura hierárquica de árvore invertida, com o nó raiz na parte superior e um máximo de 128 níveis. Segurança da Informação

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "existem dois tipos de registros DNS: registros de consultas e registros de respostas". De acordo com a teoria estudada em *6. Fontes Recomendadas na Internet*, kUROSE, James F.; ROSS, Keith W. Redes de Computadores e a Internet: Uma Abordagem Top Down. 7. ed. São Paulo: Pearson Education do Brasil, 2017. (Cap. 2 Camada de Aplicação: HTTP, SMTP, DNS; Cap. 6 Redes Sem Fio e Móveis; Cap. 8 Segurança em Redes).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "na resolução iterativa, o cliente transmite sua solicitação a um servidor que, no final do processo, retorna uma...". De acordo com a teoria estudada em *1.2 HTTP/2: Formato Binário, Multiplexação de Streams e Compressão HPACK*, server Push: O servidor pode enviar antecipadamente recursos essenciais ao cliente (como uma folha de estilo style.css ) antes mesmo de o navegador interpretá la e requisitá la explicitamente.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "um FQDN é um nome de domínio que não inclui todos os níveis existentes entre o host e o nó raiz". De acordo com a teoria estudada em *1.1 HTTP/1.1 e o Bloqueio de Início de Fila (Head-of-Line Blocking) na Aplicação*, esse fenômeno é denominado Bloqueio de Início de Fila na Aplicação ( Head of Line Blocking / HoL Blocking ): se a primeira requisição for lenta ou complexa para o backend processar, todos os demais recursos da página ficam bloqueados na fila do navegador. Para mitigar o problema, os navegadores passaram a abrir de 6 a 8 conexões TCP concorrentes com o mesmo domínio, sobrecarregando os servidores.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "o DNS usa os serviços de UDP para mensagens menores que 1024 bytes, caso contrário é usado o TCP". De acordo com a teoria estudada em *4.4 Evolução da Segurança Sem Fio: WEP, WPA, WPA2 e WPA3 (Personal vs. Enterprise)*, wPA3: AES 128 (modo Personal) ou CNSA de 192 bits (modo Enterprise) — Galois/Counter Mode (GCMP) — Padrão de Excelência Atual. Elimina ataques de dicionário offline através da troca autenticada simultânea de iguais (SAE / Dragonfly) e garante sigilo futuro ( Forward Secrecy ).
> - **E)** **Correta.** Conforme fundamentado na seção *4.4 Evolução da Segurança Sem Fio: WEP, WPA, WPA2 e WPA3 (Personal vs. Enterprise)* deste guia, wEP: Cifra de fluxo RC4 (chave de 40 ou 104 bits + IV estático de 24 bits) — CRC 32 (fraco) — Totalmente Quebrado e Obsoleto. Pode ser decifrado em poucos minutos devido ao reúso de vetores de inicialização (IVs curtos). Banido pelas normas de segurança. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/GO/2024) ao estabelecer que "o DNS pode ser representado por uma estrutura hierárquica de árvore invertida, com o nó raiz na parte superior e...".
>
> **Gabarito: E**

---

### Teste 002
**(FGV – TJ/AP – 2023 – Analista Judiciario Apoio Especializado Tecnologia Da Informacao Seguranca Da Informacao)**
Os protocolos DNS, HTTPS, DHCP e SSH utilizam, respectivamente, as portas:

* **A)** 22, 80, 53 e 21;
* **B)** 67, 80, 22 e 443;
* **C)** 53, 443, 67 e 22;
* **D)** 443, 53, 143 e 67;
* **E)** 79, 80, 67 e 21.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "22, 80, 53 e 21". De acordo com a teoria estudada em *2.1 SSH (Secure Shell) e Redirecionamento de Portas*, o protocolo SSH opera na porta TCP 22 e provê comunicação criptografada segura para administração remota de servidores, transferência de arquivos e execução remota de comandos, substituindo protocolos inseguros legados (Telnet, rlogin).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "67, 80, 22 e 443". De acordo com a teoria estudada em *3.2 Balanceadores de Carga: Camada 4 (L4) vs. Camada 7 (L7)*, compreende a semântica dos protocolos de aplicação (HTTP/HTTPS, gRPC).
> - **C)** **Correta.** Conforme fundamentado na seção *1.3 HTTP/3 e o Protocolo QUIC sobre UDP* deste guia, para eliminar em definitivo qualquer forma de bloqueio em redes móveis e de alta latência, a IETF padronizou o HTTP/3 (RFC 9114), substituindo o TCP pelo protocolo de transporte QUIC ( Quick UDP Internet Connections RFC 9000), que opera sobre datagramas UDP (Porta UDP 443). Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/AP/2023) ao estabelecer que "53, 443, 67 e 22".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "443, 53, 143 e 67". De acordo com a teoria estudada em *Protocolos em Detalhes:*, iMAP ( Internet Message Access Protocol Portas TCP 143 e TCP 993 com SSL).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "79, 80, 67 e 21". De acordo com a teoria estudada em *2.1 SSH (Secure Shell) e Redirecionamento de Portas*, autenticação: Baseada em senhas ou pares de chaves criptográficas assimétricas (RSA, Ed25519), onde a chave pública fica registrada no arquivo ~/.ssh/authorized keys do servidor remoto e a chave privada permanece protegida sob custódia do usuário.
>
> **Gabarito: C**

---

### Teste 003
**(FGV – TJ/AP – 2023 – Analista Judiciario Apoio Especializado Tecnologia Da Informacao Telecomunicacoes)**
Com relação ao sistema de nomes de domínio (Domain Name System ̶ DNS), analise as afirmativas a seguir, considerando V para a(s) verdadeira(s) e F para a(s) falsa(s). ( ) DNS é um protocolo localizado na camada 6 do modelo OSI (Open Systems Interconnection), pois resolve endereços de aplicações do tipo http. ( ) O domínio .com.br é um domínio de primeiro nível. ( ) A capacidade de um determinado domínio em aceitar correio eletrônico deve estar indicado nos registros de recursos do domínio. A sequência correta é:

* **A)** F, F e F;
* **B)** F, F e V;
* **C)** V, F e F;
* **D)** V, F e V;
* **E)** V, V e F.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "F, F e F". De acordo com a teoria estudada em *1.1 HTTP/1.1 e o Bloqueio de Início de Fila (Head-of-Line Blocking) na Aplicação*, esse fenômeno é denominado Bloqueio de Início de Fila na Aplicação ( Head of Line Blocking / HoL Blocking ): se a primeira requisição for lenta ou complexa para o backend processar, todos os demais recursos da página ficam bloqueados na fila do navegador. Para mitigar o problema, os navegadores passaram a abrir de 6 a 8 conexões TCP concorrentes com o mesmo domínio, sobrecarregando os servidores.
> - **B)** **Correta.** Conforme fundamentado na seção *3.1 Arquitetura IPsec: Cabeçalhos AH vs. ESP e Modos Transporte vs. Túnel* deste guia, o conjunto de protocolos IPsec opera na Camada de Rede (Camada 3 do modelo OSI), sendo agnóstico em relação às aplicações de camadas superiores. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/AP/2023) ao estabelecer que "F, F e V".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "V, F e F". De acordo com a teoria estudada em *6. Fontes Recomendadas na Internet*, kUROSE, James F.; ROSS, Keith W. Redes de Computadores e a Internet: Uma Abordagem Top Down. 7. ed. São Paulo: Pearson Education do Brasil, 2017. (Cap. 2 Camada de Aplicação: HTTP, SMTP, DNS; Cap. 6 Redes Sem Fio e Móveis; Cap. 8 Segurança em Redes).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "V, F e V". De acordo com a teoria estudada em *2.3 Correio Eletrônico: SMTP vs. POP3 vs. IMAP*, o tráfego de correio eletrônico na Internet divide se claramente entre envio/retransmissão e acesso/leitura.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "V, V e F". De acordo com a teoria estudada em *2.3 Correio Eletrônico: SMTP vs. POP3 vs. IMAP*, mUA Envio["Cliente Remetente (MUA)"] |"SMTP (Porta 587 STARTTLS)"| MTA Origem["Servidor de Correio Origem (MTA)"].
>
> **Gabarito: B**

---

### Teste 004
**(FCC – TRT 6ª – 2012 – Analista Judiciário - Apoio Especializado/Tecnologia da Informação)**
O Domain Name System pode ser visto como uma base de dados onde é possível consultar, entre outras coisas,

* **A)** a lista dos serviços disponíveis em um certo domínio.
* **B)** os servidores HTTP responsáveis por servir as páginas WWW de um certo domínio.
* **C)** os servidores NTP responsáveis por manter o sincronismo de um certo domínio.
* **D)** os servidores DHCP responsáveis por atribuir números IP às máquinas que se conectam dinamicamente a um certo domínio.
* **E)** os servidores de e-mail responsáveis por receber as mensagens endereçadas a um certo domínio.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "a lista dos serviços disponíveis em um certo domínio". De acordo com a teoria estudada em *Protocolos em Detalhes:*, sMTP ( Simple Mail Transfer Protocol Portas TCP 25 e TCP 587).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "os servidores HTTP responsáveis por servir as páginas WWW de um certo domínio". De acordo com a teoria estudada em *3.3 Servidores Proxy: Forward Proxy vs. Reverse Proxy*, forward Proxy (Proxy Direto): Fica posicionado em frente aos computadores clientes internos da organização. É utilizado para controlar e registrar a navegação dos funcionários na Internet, aplicar políticas de filtragem de conteúdo corporativo, fazer cache de páginas externas e mascarar os endereços IP das estações de trabalho perante os servidores web do mundo exterior.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "os servidores NTP responsáveis por manter o sincronismo de um certo domínio". De acordo com a teoria estudada em *3.3 Servidores Proxy: Forward Proxy vs. Reverse Proxy*, reverse Proxy (Proxy Reverso): Fica posicionado em frente aos servidores internos de aplicação e bancos de dados da instituição (ex.: Nginx, HAProxy, Envoy). Atua como a vitrine pública de entrada: recebe as requisições dos usuários da Internet, faz terminação SSL, aplica balanceamento de carga, acelera a entrega por meio de cache de conteúdo estático e oculta a topologia interna e a quantidade de servidores do datacenter contra invasores externos.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "os servidores DHCP responsáveis por atribuir números IP às máquinas que se conectam dinamicamente a um certo...". De acordo com a teoria estudada em *Modos de Operação: Personal vs. Enterprise*, uma chave criptográfica de sessão exclusiva é gerada dinamicamente para cada dispositivo individualmente.
> - **E)** **Correta.** Conforme fundamentado na seção *1.1 HTTP/1.1 e o Bloqueio de Início de Fila (Head-of-Line Blocking) na Aplicação* deste guia, esse fenômeno é denominado Bloqueio de Início de Fila na Aplicação ( Head of Line Blocking / HoL Blocking ): se a primeira requisição for lenta ou complexa para o backend processar, todos os demais recursos da página ficam bloqueados na fila do navegador. Para mitigar o problema, os navegadores passaram a abrir de 6 a 8 conexões TCP concorrentes com o mesmo domínio, sobrecarregando os servidores. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 6ª/2012) ao estabelecer que "os servidores de e mail responsáveis por receber as mensagens endereçadas a um certo domínio".
>
> **Gabarito: E**

---

### Teste 005
**(FGV – TRT 16ª – 2022 – Analista Judiciário (Área Administrativa - Tecnologia da Informação))**
O ESG surgiu no mercado financeiro como uma forma de medir o impacto que as ações de sustentabilidade geram nos resultados das empresas. A sigla surgiu a primeira vez em 2004, dentro de um grupo de trabalho do Principles for Responsible Investment (PRI), rede ligada à ONU que tem como objetivo atrair investimentos sustentáveis. James Gifford, economista que liderava o PRI, resumiu assim o significado de ESG: “O ESG é apenas um subgrupo inserido no contexto maior do investimento sustentável. O termo foi criado, especificamente, para focar em questões materiais. A ideia foi inverter a lógica do que, na época, era chamado de investimento ético, para se concentrar em fatores relevantes para os investidores. Se você tem uma responsabilidade fiduciária, como no caso de um fundo de pensão, não deveria estar pensando num horizonte de nove meses, mas sim de nove anos, ou de 20 anos. E quando se considera esse horizonte, temas como mudanças climáticas, riscos sociopolíticos etc., se tornam relevantes. Algumas pessoas usam o termo de maneira mais ampla, mas o ponto central é a incorporação de fatores socioambientais nos investimentos para gerenciar riscos. Não é mais sobre ética.” (https://exame.com/esg/) A sigla em inglês ESG significa

* **A)** meio ambiente, social e governança.
* **B)** economia, social e gestão.
* **C)** energia, sustentabilidade e gestão.
* **D)** ética, natureza e economia.
* **E)** eficiência, sustentação e ação global.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *Inovações Tecnológicas do HTTP/3 (QUIC):* deste guia, migração de Conexão Resiliente ( Connection Migration ): A conexão QUIC não é identificada pela 4 tupla tradicional (IP de origem, IP de destino, porta de origem, porta de destino), mas por um identificador exclusivo de 64 bits chamado Connection ID. Se o usuário sair da rede Wi Fi de casa e entrar na rede móvel 5G (mudando completamente o endereço IP do smartphone), a sessão de download, streaming ou chamada de vídeo NÃO cai nem reinicia, migrando de forma totalmente transparente. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT 16ª/2022) ao estabelecer que "meio ambiente, social e governança".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "economia, social e gestão". De acordo com a teoria estudada em *Modos de Operação: Personal vs. Enterprise*, modo Personal (WPA PSK): Emprega uma chave pré compartilhada única ( Pre Shared Key ) configurada no ponto de acesso e digitada por todos os usuários da rede. Típico de ambientes residenciais ou pequenas empresas.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "energia, sustentabilidade e gestão". De acordo com a teoria estudada em *4.3 Mecanismo de Acesso ao Meio: CSMA/CA e o Problema do Nó Oculto (RTS/CTS)*, participant AP as "Ponto de Acesso (AP)".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "ética, natureza e economia". De acordo com a teoria estudada em *6. Fontes Recomendadas na Internet*, tANENBAUM, Andrew S.; WETHERALL, David. Redes de Computadores. 5. ed. São Paulo: Pearson, 2011. (Cap. 4 A Subcamada de Controle de Acesso ao Meio: Padrões IEEE 802.11; Cap. 8 Segurança de Rede).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "eficiência, sustentação e ação global". De acordo com a teoria estudada em *6. Fontes Recomendadas na Internet*, iETF RFC 9110 HTTP Semantics Norma de referência global da IETF com as semânticas, códigos de status e métodos do protocolo HTTP.
>
> **Gabarito: A**

---

### Teste 006
**(FGV – TRF/1 – 2024 – Analista Judiciario Area Apoio Especializado Especialidade Tecnologia Da Informacao)**
A equipe de TI de uma empresa está conduzindo uma investigação minuciosa dos registros de recursos DNS. Enquanto revisavam esses registros, eles se depararam com um registro de recurso com o campo type = A. Nesse registro, o campo:

* **A)** Name é um nome de domínio e Value é o endereço IP para o nome de domínio;
* **B)** Name é um nome de hospedeiro e Value é o endereço IP para o nome de hospedeiro;
* **C)** Name é um nome de domínio e Value é o endereço IP para o nome de um servidor DNS recursivo;
* **D)** Name é um nome de domínio e Value é o endereço IP para o nome de um servidor DNS autoritativo;
* **E)** Name é um nome de hospedeiro e Value é o endereço IP para o nome de um servidor DNS recursivo.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Name é um nome de domínio e Value é o endereço IP para o nome de domínio". De acordo com a teoria estudada em *1.1 HTTP/1.1 e o Bloqueio de Início de Fila (Head-of-Line Blocking) na Aplicação*, esse fenômeno é denominado Bloqueio de Início de Fila na Aplicação ( Head of Line Blocking / HoL Blocking ): se a primeira requisição for lenta ou complexa para o backend processar, todos os demais recursos da página ficam bloqueados na fila do navegador. Para mitigar o problema, os navegadores passaram a abrir de 6 a 8 conexões TCP concorrentes com o mesmo domínio, sobrecarregando os servidores.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Name é um nome de hospedeiro e Value é o endereço IP para o nome de hospedeiro". De acordo com a teoria estudada em *Inovações Tecnológicas do HTTP/3 (QUIC):*, migração de Conexão Resiliente ( Connection Migration ): A conexão QUIC não é identificada pela 4 tupla tradicional (IP de origem, IP de destino, porta de origem, porta de destino), mas por um identificador exclusivo de 64 bits chamado Connection ID. Se o usuário sair da rede Wi Fi de casa e entrar na rede móvel 5G (mudando completamente o endereço IP do smartphone), a sessão de download, streaming ou chamada de vídeo NÃO cai nem reinicia, migrando de forma totalmente transparente.
> - **C)** **Correta.** Conforme fundamentado na seção *6. Fontes Recomendadas na Internet* deste guia, kUROSE, James F.; ROSS, Keith W. Redes de Computadores e a Internet: Uma Abordagem Top Down. 7. ed. São Paulo: Pearson Education do Brasil, 2017. (Cap. 2 Camada de Aplicação: HTTP, SMTP, DNS; Cap. 6 Redes Sem Fio e Móveis; Cap. 8 Segurança em Redes). Dessa forma, está plenamente correta a assertiva da banca (FGV – TRF/1/2024) ao estabelecer que "Name é um nome de domínio e Value é o endereço IP para o nome de um servidor DNS recursivo".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Name é um nome de domínio e Value é o endereço IP para o nome de um servidor DNS autoritativo". De acordo com a teoria estudada em *3.2 Balanceadores de Carga: Camada 4 (L4) vs. Camada 7 (L7)*, toma decisões de chaveamento baseando se unicamente em informações das camadas de rede e transporte: Endereço IP de origem/destino e Portas TCP/UDP.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Name é um nome de hospedeiro e Value é o endereço IP para o nome de um servidor DNS recursivo". De acordo com a teoria estudada em *1.2 HTTP/2: Formato Binário, Multiplexação de Streams e Compressão HPACK*, server Push: O servidor pode enviar antecipadamente recursos essenciais ao cliente (como uma folha de estilo style.css ) antes mesmo de o navegador interpretá la e requisitá la explicitamente.
>
> **Gabarito: C**

---

### Teste 007
**(FGV – TJ/RR – 2024 – Analista Judiciario Gestao E Governanca De Tecnologia Da Informacao)**
O gerenciamento de redes envolve diversas práticas e protocolos que permitem monitorar e gerenciar a operação de dispositivos em uma infraestrutura de rede. Assinale o protocolo amplamente utilizado para o gerenciamento e monitoramento de dispositivos de rede.

* **A)** HTTP.
* **B)** FTP.
* **C)** SNMP.
* **D)** SMTP.
* **E)** DNS.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "HTTP". De acordo com a teoria estudada em *1.3 HTTP/3 e o Protocolo QUIC sobre UDP*, para eliminar em definitivo qualquer forma de bloqueio em redes móveis e de alta latência, a IETF padronizou o HTTP/3 (RFC 9114), substituindo o TCP pelo protocolo de transporte QUIC ( Quick UDP Internet Connections RFC 9000), que opera sobre datagramas UDP (Porta UDP 443).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "FTP". De acordo com a teoria estudada em *2.2 Transferência de Arquivos: FTP vs. FTPS vs. SFTP*, protocolo: Portas de Transporte Utilizadas — Criptografia / Segurança — Arquitetura e Relação com FTP.
> - **C)** **Correta.** Conforme fundamentado na seção *Modos de Operação do IPsec:* deste guia, modo Túnel: Utilizado em conexões de borda VPN Site to Site interligando redes inteiras (Matriz e Filial) através de roteadores ou firewalls. O pacote IP original inteiro (cabeçalho IP privado + carga útil) é completamente criptografado, e um novo cabeçalho IP externo contendo os endereços públicos dos gateways de borda é adicionado por fora. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/RR/2024) ao estabelecer que "SNMP".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "SMTP". De acordo com a teoria estudada em *6. Fontes Recomendadas na Internet*, kUROSE, James F.; ROSS, Keith W. Redes de Computadores e a Internet: Uma Abordagem Top Down. 7. ed. São Paulo: Pearson Education do Brasil, 2017. (Cap. 2 Camada de Aplicação: HTTP, SMTP, DNS; Cap. 6 Redes Sem Fio e Móveis; Cap. 8 Segurança em Redes).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "DNS". De acordo com a teoria estudada em *Modos de Operação do IPsec:*, modo Transporte: Utilizado em comunicações ponto a ponto entre dois hosts finais ( Host to Host ). Criptografa apenas o payload de transporte (dados TCP/UDP), mantendo o cabeçalho IP original legível. Os IPs privados de origem e destino ficam visíveis na rede pública.
>
> **Gabarito: C**

---

### Teste 008
**(FGV – TJ/RR – 2024 – Analista Judiciario Infraestrutura De Tecnologia Da Informacao)**
Com relação aos protocolos de redes de computadores, analise as afirmativas a seguir. I. O DHCP (Dynamic Host Configuration Protocol) é um protocolo cliente-servidor que permite que um host obtenha um endereço IP (Internet Protocol) automaticamente. II. Ao contrário do TCP (Transmission Control Protocol), o UDP (User Datagram Protocol) não é orientado a conexões. III. O SMTP (Simple Mail Transfer Protocol) permite que um servidor de correio eletrônico atue ora como cliente ora como servidor. Está correto o que se afirma em

* **A)** II, apenas.
* **B)** I e II, apenas.
* **C)** I e III, apenas.
* **D)** II e III, apenas.
* **E)** I, II e III.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II, apenas". De acordo com a teoria estudada em *2.3 Correio Eletrônico: SMTP vs. POP3 vs. IMAP*, mUA Envio["Cliente Remetente (MUA)"] |"SMTP (Porta 587 STARTTLS)"| MTA Origem["Servidor de Correio Origem (MTA)"].
> - **B)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e II, apenas". De acordo com a teoria estudada em *2.2 Transferência de Arquivos: FTP vs. FTPS vs. SFTP*, fTP ( File Transfer Protocol ): TCP 21 (Controle) e TCP 20 (Dados no modo ativo) — NENHUMA. Usuário, senha e conteúdo dos arquivos transitam em texto claro puro. — Protocolo legado original. Opera com duas conexões distintas (modo Ativo vs. modo Passivo/PASV).
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e III, apenas". De acordo com a teoria estudada em *Protocolos em Detalhes:*, utilizado pelo cliente para submeter e mails ao seu servidor (porta 587 com autenticação e STARTTLS) e utilizado para retransmitir e mails entre servidores de correio na Internet (porta 25).
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II e III, apenas". De acordo com a teoria estudada em *2.3 Correio Eletrônico: SMTP vs. POP3 vs. IMAP*, mTA Destino |"IMAP (Porta 993) ou POP3 (Porta 995)"| MUA Destino["Cliente Destinatário (MUA)"].
> - **E)** **Correta.** Conforme fundamentado na seção *Protocolos em Detalhes:* deste guia, sMTP ( Simple Mail Transfer Protocol Portas TCP 25 e TCP 587). Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/RR/2024) ao estabelecer que "I, II e III".
>
> **Gabarito: E**

---

### Teste 009
**(CEBRASPE – STF – 2008 – Analista Judiciario Suporte Em Tecnologia Da Informacao)**
A seqüência de caracteres http://www.google.com.br é um exemplo de endereço na Internet. Nesse endereço, os caracteres http identificam um protocolo.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Correta.** O item está **Certo**. Conforme fundamentado na seção *Inovações Tecnológicas do HTTP/3 (QUIC):*, migração de Conexão Resiliente ( Connection Migration ): A conexão QUIC não é identificada pela 4 tupla tradicional (IP de origem, IP de destino, porta de origem, porta de destino), mas por um identificador exclusivo de 64 bits chamado Connection ID. Se o usuário sair da rede Wi Fi de casa e entrar na rede móvel 5G (mudando completamente o endereço IP do smartphone), a sessão de download, streaming ou chamada de vídeo NÃO cai nem reinicia, migrando de forma totalmente transparente. Dessa forma, está plenamente correta a assertiva da banca (CEBRASPE – STF/2008) ao afirmar que "A seqüência de caracteres http://www.google.com.br é um exemplo de endereço na Internet. Nesse endereço, os...".
> - **E)** **Incorreta.** A assertiva não incorre em erro conceitual, guardando conformidade com a teoria estudada.
>
> **Gabarito: C**

---

### Teste 010
**(CEBRASPE – STJ – 2015 – Analista Judiciario Suporte Em Tecnologia Da Informacao)**
O uso de um servidor DNS de encaminhamento central para a resolução de nomes da Internet pode reduzir o desempenho da rede, tornando complexo o processo de solução de problemas, além de ser uma prática não recomendada em termos de segurança.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Incorreta.** A proposição apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O uso de um servidor DNS de encaminhamento central para a resolução de nomes da Internet pode reduzir o...". De acordo com a teoria em *1.4 HTTPS e TLS 1.3 Integrado*, forward Secrecy Mandatório: O TLS 1.3 exige o uso de algoritmos de troca de chave efêmera (como ECDHE), garantindo que, mesmo que a chave privada do servidor web seja roubada no futuro, o tráfego gravado no passado não poderá ser decifrado.
> - **E)** **Correta.** O item está **Errado** (gabarito oficial: **E**), pois contraria a disciplina teórica aplicável.
>
> **Gabarito: E**

---

### Teste 011
**(FGV – TJ/BA – 2015 – Analista Judiciario Tecnologia Da Informacao)**
Há suspeita de um loop de roteamento na rede. Tal suspeita pode ser reforçada se, ao se monitorar a rede, forem detectados:

* **A)** pacotes ICMP do tipo Time Exceeded;
* **B)** pacotes ARP originados de máquina externas;
* **C)** pacotes UDP contendo consultas recursivas para servidores DNS internos;
* **D)** pacotes TCP com endereços origem e destino iguais entre si;
* **E)** pacotes IGMP e multicast com pruning.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *Inovações Tecnológicas do HTTP/3 (QUIC):* deste guia, compressão QPACK: Evolução do algoritmo HPACK adaptada para lidar com pacotes que chegam fora de ordem sobre o transporte UDP. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/BA/2015) ao estabelecer que "pacotes ICMP do tipo Time Exceeded".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "pacotes ARP originados de máquina externas". De acordo com a teoria estudada em *3.3 Servidores Proxy: Forward Proxy vs. Reverse Proxy*, forward Proxy (Proxy Direto): Fica posicionado em frente aos computadores clientes internos da organização. É utilizado para controlar e registrar a navegação dos funcionários na Internet, aplicar políticas de filtragem de conteúdo corporativo, fazer cache de páginas externas e mascarar os endereços IP das estações de trabalho perante os servidores web do mundo exterior.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "pacotes UDP contendo consultas recursivas para servidores DNS internos". De acordo com a teoria estudada em *3.3 Servidores Proxy: Forward Proxy vs. Reverse Proxy*, reverse Proxy (Proxy Reverso): Fica posicionado em frente aos servidores internos de aplicação e bancos de dados da instituição (ex.: Nginx, HAProxy, Envoy). Atua como a vitrine pública de entrada: recebe as requisições dos usuários da Internet, faz terminação SSL, aplica balanceamento de carga, acelera a entrega por meio de cache de conteúdo estático e oculta a topologia interna e a quantidade de servidores do datacenter contra invasores externos.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "pacotes TCP com endereços origem e destino iguais entre si". De acordo com a teoria estudada em *Modos de Operação do IPsec:*, modo Transporte: Utilizado em comunicações ponto a ponto entre dois hosts finais ( Host to Host ). Criptografa apenas o payload de transporte (dados TCP/UDP), mantendo o cabeçalho IP original legível. Os IPs privados de origem e destino ficam visíveis na rede pública.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "pacotes IGMP e multicast com pruning". De acordo com a teoria estudada em *4.1 Evolução dos Padrões 802.11 (Wi-Fi 4, Wi-Fi 5 e Wi-Fi 6/6E)*, wi Fi 6 / 6E: 802.11ax — 2.4 GHz, 5 GHz e 6 GHz (no 6E) — Canais de até 160 MHz — OFDMA (subcanais RU), MU MIMO bidirecional, TWT ( Target Wake Time ) para IoT — Até 9.6 Gbps.
>
> **Gabarito: A**

---

### Teste 012
**(FCC – TRT 11ª – 2017 – Analista Judiciário - Tecnologia da Informação)**
Considere a figura abaixo que descreve um sistema, denominado e-intimação, que utiliza web service. Foram omitidos da figura o protocolo (indicado por P) e o formato (indicado por F) de geração do documento de intimação que correspondem, correta e respectivamente, a

* **A)** HTTPS − XML.
* **B)** SOA − SOAP.
* **C)** SOAP − REST.
* **D)** REST − SOAP.
* **E)** SOAP − XML.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "HTTPS − XML". De acordo com a teoria estudada em *1.4 HTTPS e TLS 1.3 Integrado*, forward Secrecy Mandatório: O TLS 1.3 exige o uso de algoritmos de troca de chave efêmera (como ECDHE), garantindo que, mesmo que a chave privada do servidor web seja roubada no futuro, o tráfego gravado no passado não poderá ser decifrado.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "SOA − SOAP". De acordo com a teoria estudada em *Modos de Operação: Personal vs. Enterprise*, a comunicação é intermediada pelo ponto de acesso e validada por um servidor de autenticação corporativo baseado no protocolo RADIUS ( Remote Authentication Dial In User Service ).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "SOAP − REST". De acordo com a teoria estudada em *3.2 Balanceadores de Carga: Camada 4 (L4) vs. Camada 7 (L7)*, pode inspecionar URLs, caminhos de requisição ( /api vs. /imagens ), cabeçalhos HTTP, métodos REST e cookies de sessão.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "REST − SOAP". De acordo com a teoria estudada em *1.1 HTTP/1.1 e o Bloqueio de Início de Fila (Head-of-Line Blocking) na Aplicação*, o protocolo HTTP/1.1 (RFC 2616) estruturou a comunicação na web durante duas décadas. Ele trouxe como avanço o suporte a conexões persistentes ( Keep Alive ), permitindo que uma mesma conexão TCP fosse reaproveitada para transferir múltiplos recursos sem a necessidade de reabrir o handshake a cada arquivo.
> - **E)** **Correta.** Conforme fundamentado na seção *1.2 HTTP/2: Formato Binário, Multiplexação de Streams e Compressão HPACK* deste guia, compressão de Cabeçalhos (HPACK): Utiliza tabelas estáticas e dinâmicas associadas à codificação Huffman para eliminar a repetição redundante de cabeçalhos volumosos (como cookies e user agents). Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 11ª/2017) ao estabelecer que "SOAP − XML".
>
> **Gabarito: E**

---

### Teste 013
**(FCC – TRT 16ª – 2014 – Analista Judiciário - Tecnologia da Informação)**
O serviço de rede DNS possui uma arquitetura hierárquica que inclui clientes e servidores, com bases de dados distribuídos, que se comunicam por meio dos protocolos definidos para o DNS. Dentre os três tipos de mensagens definidas no protocolo, a mensagem utilizada para a troca de informações entre os servidores DNS é do tipo

* **A)** consulta.
* **B)** resposta.
* **C)** busca.
* **D)** atualização.
* **E)** sincronização.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "consulta". De acordo com a teoria estudada em *2.1 SSH (Secure Shell) e Redirecionamento de Portas*, local Port Forwarding ( ssh L local port:target host:target port user@server ): Encaminha o tráfego de uma porta local da estação do administrador através do túnel criptografado SSH para um serviço interno na rede remota (ex.: acessar uma base de dados inacessível pela Internet).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "resposta". De acordo com a teoria estudada em *1.1 HTTP/1.1 e o Bloqueio de Início de Fila (Head-of-Line Blocking) na Aplicação*, as mensagens trafegam em formato estritamente textual e sequencial no modelo requisição resposta.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "busca". De acordo com a teoria estudada em *3.3 Servidores Proxy: Forward Proxy vs. Reverse Proxy*, reverse Proxy (Proxy Reverso): Fica posicionado em frente aos servidores internos de aplicação e bancos de dados da instituição (ex.: Nginx, HAProxy, Envoy). Atua como a vitrine pública de entrada: recebe as requisições dos usuários da Internet, faz terminação SSL, aplica balanceamento de carga, acelera a entrega por meio de cache de conteúdo estático e oculta a topologia interna e a quantidade de servidores do datacenter contra invasores externos.
> - **D)** **Correta.** Conforme fundamentado na seção *Protocolos de Segurança do IPsec:* deste guia, o protocolo AH NÃO PROVÊ CONFIDENCIALIDADE (NÃO realiza criptografia de dados)! Além disso, é incompatível com NAT porque inclui o cabeçalho IP original no cálculo de integridade. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 16ª/2014) ao estabelecer que "atualização".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "sincronização". De acordo com a teoria estudada em *Protocolos em Detalhes:*, é um protocolo do tipo Pull (Acesso e Sincronização).
>
> **Gabarito: D**

---

### Teste 014
**(FCC – TRT 2ª – 2014 – Analista Judiciário - Tecnologia da Informação)**
Considere as seguintes figuras que apresentam o envio de um arquivo entre dois serviços: Figura 1 Figura 2 Com base nessas imagens e nas configurações padrão para os protocolos HTTP e HTTPS, é correto afirmar que o arquivo enviado na figura 1

* **A)** é recebido na porta 80 e o arquivo enviado na figura 2 é transportado por HTTPS.
* **B)** é transportado por HTTP e o arquivo enviado na figura 2 é recebido na porta 80.
* **C)** e o arquivo enviado na figura 2 são transportados na porta 80, porém o primeiro arquivo possui um header que garante sua segurança.
* **D)** é recebido na porta 443 e o arquivo enviado na figura 2 é transportado por HTTP.
* **E)** é transportado por HTTPS e o arquivo enviado na figura 2 é recebido na porta 443.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "é recebido na porta 80 e o arquivo enviado na figura 2 é transportado por HTTPS". De acordo com a teoria estudada em *1.2 HTTP/2: Formato Binário, Multiplexação de Streams e Compressão HPACK*, multiplexação Verdadeira: Múltiplas requisições e respostas podem trafegar de forma intercalada, bidirecional e simultânea sobre uma única conexão TCP aberta. Um arquivo CSS pesado não bloqueia mais o tráfego de imagens leves.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "é transportado por HTTP e o arquivo enviado na figura 2 é recebido na porta 80". De acordo com a teoria estudada em *2.1 SSH (Secure Shell) e Redirecionamento de Portas*, remote Port Forwarding ( ssh R remote port:target host:target port user@server ): Encaminha tráfego recebido em uma porta do servidor remoto de volta para um serviço rodando na máquina local do administrador.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "e o arquivo enviado na figura 2 são transportados na porta 80, porém o primeiro arquivo possui um header que...". De acordo com a teoria estudada em *4.4 Evolução da Segurança Sem Fio: WEP, WPA, WPA2 e WPA3 (Personal vs. Enterprise)*, wPA3: AES 128 (modo Personal) ou CNSA de 192 bits (modo Enterprise) — Galois/Counter Mode (GCMP) — Padrão de Excelência Atual. Elimina ataques de dicionário offline através da troca autenticada simultânea de iguais (SAE / Dragonfly) e garante sigilo futuro ( Forward Secrecy ).
> - **D)** **Correta.** Conforme fundamentado na seção *1.3 HTTP/3 e o Protocolo QUIC sobre UDP* deste guia, para eliminar em definitivo qualquer forma de bloqueio em redes móveis e de alta latência, a IETF padronizou o HTTP/3 (RFC 9114), substituindo o TCP pelo protocolo de transporte QUIC ( Quick UDP Internet Connections RFC 9000), que opera sobre datagramas UDP (Porta UDP 443). Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 2ª/2014) ao estabelecer que "é recebido na porta 443 e o arquivo enviado na figura 2 é transportado por HTTP".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "é transportado por HTTPS e o arquivo enviado na figura 2 é recebido na porta 443". De acordo com a teoria estudada em *1.4 HTTPS e TLS 1.3 Integrado*, no HTTP/3, o TLS 1.3 é embutido nativamente no QUIC, não existindo HTTP/3 em texto claro na especificação padrão.
>
> **Gabarito: D**

---

### Teste 015
**(FCC – TRT 3ª – 2015 – Analista Judiciário - Tecnologia da Informação)**
Para reduzir a vulnerabilidade dos acessos pelo protocolo HTTP, foi introduzido, acima desse protocolo, o SSL, originando assim o HTTPS. O HTTPS

* **A)** 21 e 993.
* **B)** 110 e 443.
* **C)** 25 e 465.
* **D)** 143 e 993.
* **E)** 53 e 443.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "21 e 993". De acordo com a teoria estudada em *Protocolos em Detalhes:*, iMAP ( Internet Message Access Protocol Portas TCP 143 e TCP 993 com SSL).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "110 e 443". De acordo com a teoria estudada em *Protocolos em Detalhes:*, pOP3 ( Post Office Protocol v3 Portas TCP 110 e TCP 995 com SSL).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "25 e 465". De acordo com a teoria estudada em *2.2 Transferência de Arquivos: FTP vs. FTPS vs. SFTP*, fTPS ( FTP over SSL/TLS ): TCP 21 (Controle) + Portas de Dados dinâmicas protegidas — Criptografia via TLS/SSL aplicada sobre as conexões de controle e dados do FTP. — É o protocolo FTP clássico encapsulado em uma sessão TLS. Requer abertura de faixas complexas de portas no firewall.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "143 e 993". De acordo com a teoria estudada em *2.3 Correio Eletrônico: SMTP vs. POP3 vs. IMAP*, mTA Destino |"IMAP (Porta 993) ou POP3 (Porta 995)"| MUA Destino["Cliente Destinatário (MUA)"].
> - **E)** **Correta.** Conforme fundamentado na seção *1.3 HTTP/3 e o Protocolo QUIC sobre UDP* deste guia, para eliminar em definitivo qualquer forma de bloqueio em redes móveis e de alta latência, a IETF padronizou o HTTP/3 (RFC 9114), substituindo o TCP pelo protocolo de transporte QUIC ( Quick UDP Internet Connections RFC 9000), que opera sobre datagramas UDP (Porta UDP 443). Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 3ª/2015) ao estabelecer que "53 e 443".
>
> **Gabarito: E**

---

### Teste 016
**(FCC – TRT 4ª – 2015 – Analista Judiciário - Tecnologia Da Informação)**
Quando um novo computador é conectado e colocado em funcionamento em uma rede local de computadores, a primeira atividade desempenhada é a sua identificação, utilizando o endereço MAC, para a rede e o estabelecimento do relacionamento com um endereço IP. A mensagem inicial gerada pelo computador para a rede com esse propósito, utiliza o protocolo

* **A)** DHCP.
* **B)** ICMP.
* **C)** DNS.
* **D)** ARP.
* **E)** SNMP.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "DHCP". De acordo com a teoria estudada em *3.2 Balanceadores de Carga: Camada 4 (L4) vs. Camada 7 (L7)*, toma decisões de chaveamento baseando se unicamente em informações das camadas de rede e transporte: Endereço IP de origem/destino e Portas TCP/UDP.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "ICMP". De acordo com a teoria estudada em *6. Fontes Recomendadas na Internet*, tANENBAUM, Andrew S.; WETHERALL, David. Redes de Computadores. 5. ed. São Paulo: Pearson, 2011. (Cap. 4 A Subcamada de Controle de Acesso ao Meio: Padrões IEEE 802.11; Cap. 8 Segurança de Rede).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "DNS". De acordo com a teoria estudada em *6. Fontes Recomendadas na Internet*, kUROSE, James F.; ROSS, Keith W. Redes de Computadores e a Internet: Uma Abordagem Top Down. 7. ed. São Paulo: Pearson Education do Brasil, 2017. (Cap. 2 Camada de Aplicação: HTTP, SMTP, DNS; Cap. 6 Redes Sem Fio e Móveis; Cap. 8 Segurança em Redes).
> - **D)** **Correta.** Conforme fundamentado na seção *Inovações Tecnológicas do HTTP/3 (QUIC):* deste guia, migração de Conexão Resiliente ( Connection Migration ): A conexão QUIC não é identificada pela 4 tupla tradicional (IP de origem, IP de destino, porta de origem, porta de destino), mas por um identificador exclusivo de 64 bits chamado Connection ID. Se o usuário sair da rede Wi Fi de casa e entrar na rede móvel 5G (mudando completamente o endereço IP do smartphone), a sessão de download, streaming ou chamada de vídeo NÃO cai nem reinicia, migrando de forma totalmente transparente. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 4ª/2015) ao estabelecer que "ARP".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "SNMP". De acordo com a teoria estudada em *2.1 SSH (Secure Shell) e Redirecionamento de Portas*, local Port Forwarding ( ssh L local port:target host:target port user@server ): Encaminha o tráfego de uma porta local da estação do administrador através do túnel criptografado SSH para um serviço interno na rede remota (ex.: acessar uma base de dados inacessível pela Internet).
>
> **Gabarito: D**

---

## 3. Elementos de Borda e Segurança de Rede: VPN, IPsec, Balanceadores e Proxies

### 3.1 Arquitetura IPsec: Cabeçalhos AH vs. ESP e Modos Transporte vs. Túnel

O conjunto de protocolos **IPsec** opera na **Camada de Rede (Camada 3 do modelo OSI)**, sendo agnóstico em relação às aplicações de camadas superiores:

```mermaid
flowchart TD
    subgraph ModoTransporte["Modo Transporte (Host-a-Host)"]
        T1["Cabeçalho IP Original"] --> T2["Cabeçalho ESP / AH"] --> T3["Carga Útil Cifrada (Payload TCP/UDP)"]
    end
    subgraph ModoTunel["Modo Túnel (Site-to-Site / Filial-Sede)"]
        U1["NOVO Cabeçalho IP Externo (IPs Públicos dos Roteadores)"] --> U2["Cabeçalho ESP"] --> U3["Cabeçalho IP Original Privado CIFRADO"] --> U4["Carga Útil CIFRADA"]
    end
```

#### Protocolos de Segurança do IPsec:
- **AH (*Authentication Header* - Protocolo IP 51):** Provê autenticação da origem e integridade estrita dos dados via hash criptográfico.  
  > 🚨 **REGRA DE PROVA FCC:** O protocolo **AH NÃO PROVÊ CONFIDENCIALIDADE (NÃO realiza criptografia de dados)**! Além disso, é incompatível com NAT porque inclui o cabeçalho IP original no cálculo de integridade.
- **ESP (*Encapsulating Security Payload* - Protocolo IP 50):** Provê **confidencialidade (criptografia dos dados)**, além de autenticação de origem e integridade. É o protocolo primário utilizado para túneis VPN seguros.

#### Modos de Operação do IPsec:
- **Modo Transporte:** Utilizado em comunicações ponto a ponto entre dois hosts finais (*Host-to-Host*). Criptografa apenas o payload de transporte (dados TCP/UDP), mantendo o cabeçalho IP original legível. Os IPs privados de origem e destino ficam visíveis na rede pública.
- **Modo Túnel:** Utilizado em conexões de borda **VPN *Site-to-Site*** interligando redes inteiras (Matriz e Filial) através de roteadores ou firewalls. O **pacote IP original inteiro (cabeçalho IP privado + carga útil) é completamente criptografado**, e um novo cabeçalho IP externo contendo os endereços públicos dos gateways de borda é adicionado por fora.

### 3.2 Balanceadores de Carga: Camada 4 (L4) vs. Camada 7 (L7)

Os Balanceadores de Carga (*Load Balancers*) distribuem o fluxo de requisições entre múltiplos servidores de backend para garantir escalabilidade horizontal e alta disponibilidade:

- **Balanceador de Camada 4 (L4 - Transporte):**
    - Toma decisões de chaveamento baseando-se unicamente em informações das camadas de rede e transporte: **Endereço IP de origem/destino e Portas TCP/UDP**.
    - Não examina o conteúdo da aplicação. Apresenta rendimento extraordinário, baixa latência e consome poucos recursos computacionais.
- **Balanceador de Camada 7 (L7 - Aplicação):**
    - Compreende a semântica dos protocolos de aplicação (HTTP/HTTPS, gRPC).
    - Pode inspecionar URLs, caminhos de requisição (`/api` vs. `/imagens`), cabeçalhos HTTP, métodos REST e cookies de sessão.
    - Suporta roteamento contextual baseado em conteúdo, persistência de sessão (*Sticky Sessions* via cookies) e descarregamento de processamento criptográfico (**SSL Termination / Offloading**).

### 3.3 Servidores Proxy: Forward Proxy vs. Reverse Proxy

- **Forward Proxy (Proxy Direto):** Fica posicionado em frente aos **computadores clientes internos** da organização. É utilizado para controlar e registrar a navegação dos funcionários na Internet, aplicar políticas de filtragem de conteúdo corporativo, fazer cache de páginas externas e mascarar os endereços IP das estações de trabalho perante os servidores web do mundo exterior.
- **Reverse Proxy (Proxy Reverso):** Fica posicionado em frente aos **servidores internos de aplicação e bancos de dados** da instituição (ex.: Nginx, HAProxy, Envoy). Atua como a vitrine pública de entrada: recebe as requisições dos usuários da Internet, faz terminação SSL, aplica balanceamento de carga, acelera a entrega por meio de cache de conteúdo estático e oculta a topologia interna e a quantidade de servidores do datacenter contra invasores externos.

---

## 4. Redes Sem Fio (IEEE 802.11 - Wi-Fi)

### 4.1 Evolução dos Padrões 802.11 (Wi-Fi 4, Wi-Fi 5 e Wi-Fi 6/6E)

| Geração Comercial | Padrão IEEE | Frequências de Operação | Larguras de Canal | Principais Tecnologias e Recursos | Taxas Teóricas Máximas |
|---|---|---|---|---|---|
| **Wi-Fi 4** | **802.11n** | 2.4 GHz e 5 GHz | 20 e 40 MHz | Introdução da tecnologia **MIMO** (*Multiple-Input Multiple-Output*) | Até 600 Mbps |
| **Wi-Fi 5** | **802.11ac** | **Exclusivo 5 GHz** | 20, 40, 80 e 160 MHz | **MU-MIMO** (*Multi-User MIMO*) para downlink, modulação 256-QAM | Até 6.9 Gbps |
| **Wi-Fi 6 / 6E** | **802.11ax** | 2.4 GHz, 5 GHz e 6 GHz (no 6E) | Canais de até 160 MHz | **OFDMA** (subcanais RU), MU-MIMO bidirecional, TWT (*Target Wake Time*) para IoT | Até 9.6 Gbps |

### 4.2 Frequências de Operação: 2.4 GHz vs. 5 GHz

- **Faixa de 2.4 GHz:**
    - *Vantagem:* Maior comprimento de onda, proporcionando **maior alcance físico** de cobertura e melhor penetração através de paredes e obstáculos sólidos.
    - *Desvantagem:* Menor largura de banda total e **altíssima interferência** (disputa espaço com Bluetooth, fornos micro-ondas e telefones sem fio). Possui apenas **3 canais não sobrepostos** na regulamentação padrão (canais 1, 6 e 11).
- **Faixa de 5 GHz:**
    - *Vantagem:* Menor índice de interferência, dezenas de canais não sobrepostos e capacidade para canais largos (80/160 MHz), oferecendo **altíssima vazão de dados**.
    - *Desvantagem:* Menor alcance de cobertura de sinal e maior atenuação ao atravessar obstáculos físicos.

### 4.3 Mecanismo de Acesso ao Meio: CSMA/CA e o Problema do Nó Oculto (RTS/CTS)

Diferente das redes cabeadas Ethernet (IEEE 802.3), que utilizam detecção de colisão (**CSMA/CD**), o meio sem fio via rádio impossibilita a detecção confiável de colisões elétricas na antena transmissora enquanto ela mesma emite sinal em alta potência. Por isso, o padrão IEEE 802.11 adota compulsoriamente a **Prevenção de Colisões (CSMA/CA - *Carrier Sense Multiple Access with Collision Avoidance*)**:

```mermaid
sequenceDiagram
    autonumber
    participant EstacaoA as "Estação A"
    participant AP as "Ponto de Acesso (AP)"
    participant EstacaoB as "Estação B (Nó Oculto de A)"

    Note over EstacaoA,EstacaoB: Estação A e B não se enxergam, mas ambas enxergam o AP!
    EstacaoA->>AP: Envia RTS (Request to Send - reserva de canal)
    AP-->>EstacaoA: Envia CTS (Clear to Send)
    AP-->>EstacaoB: Estação B ouve o CTS do AP e suspende transmissões (NAV)
    EstacaoA->>AP: Transmite Dados sem perigo de colisão com B
    AP-->>EstacaoA: Envia ACK (Reconhecimento de entrega)
```

#### O Problema do Nó Oculto (*Hidden Node Problem*):
Ocorre quando duas estações distantes (Estação A e Estação B) estão ambas dentro do raio de alcance do mesmo Ponto de Acesso (AP), mas encontram-se fora do alcance de escuta de rádio uma da outra. Se ambas escutarem o canal e acharem que ele está livre, transmitirão simultaneamente para o AP, provocando colisão destrutiva.

O problema é neutralizado pelo mecanismo opcional de reserva via quadros de controle **RTS/CTS**:

1. A Estação A transmite um quadro **RTS (*Request to Send*)** ao AP solicitando tempo de reserva;
2. O AP responde com um quadro **CTS (*Clear to Send*)** em broadcast;
3. A Estação B escuta o CTS emitido pelo AP e suspende suas transmissões (ajustando seu temporizador NAV - *Network Allocation Vector*), permitindo que a Estação A envie seus dados sem risco de colisão.

### 4.4 Evolução da Segurança Sem Fio: WEP, WPA, WPA2 e WPA3 (Personal vs. Enterprise)

| Padrão | Criptografia Adotada | Mecanismo de Integridade | Vulnerabilidades Críticas / Situação Atual |
|---|---|---|---|
| **WEP** | Cifra de fluxo **RC4** (chave de 40 ou 104 bits + IV estático de 24 bits) | CRC-32 (fraco) | **Totalmente Quebrado e Obsoleto.** Pode ser decifrado em poucos minutos devido ao reúso de vetores de inicialização (IVs curtos). Banido pelas normas de segurança. |
| **WPA** | Cifra **TKIP** (*Temporal Key Integrity Protocol*) sobre RC4 | Michael (MIC) | Padrão emergencial de transição para cobrir as falhas do WEP sem exigir troca de hardware; hoje também considerado obsoleto. |
| **WPA2** | **AES** (*Advanced Encryption Standard*) com protocolo **CCMP** | CBC-MAC | Padrão robusto da indústria. Vulnerável ao ataque de reinstalação de chave (**KRACK**) e ataques de força bruta/dicionário offline ao aperto de mão de 4 vias (modo PSK). |
| **WPA3** | **AES-128 (modo Personal) ou CNSA de 192 bits (modo Enterprise)** | Galois/Counter Mode (GCMP) | **Padrão de Excelência Atual.** Elimina ataques de dicionário offline através da troca autenticada simultânea de iguais (**SAE / Dragonfly**) e garante sigilo futuro (*Forward Secrecy*). |

#### Modos de Operação: Personal vs. Enterprise
- **Modo Personal (WPA-PSK):** Emprega uma **chave pré-compartilhada única (*Pre-Shared Key*)** configurada no ponto de acesso e digitada por todos os usuários da rede. Típico de ambientes residenciais ou pequenas empresas.
- **Modo Enterprise (WPA-Enterprise):** Não utiliza senha compartilhada única. Implementa a arquitetura de autenticação centralizada e individualizada baseada no padrão **IEEE 802.1X**:
    - Cada colaborador autentica-se com seu próprio login e senha do Active Directory ou com um certificado digital pessoal;
    - A comunicação é intermediada pelo ponto de acesso e validada por um servidor de autenticação corporativo baseado no protocolo **RADIUS** (*Remote Authentication Dial-In User Service*);
    - Uma chave criptográfica de sessão exclusiva é gerada dinamicamente para cada dispositivo individualmente.

---

## 6. Fontes Recomendadas na Internet

* [IETF RFC 9110 - HTTP Semantics](https://datatracker.ietf.org/doc/html/rfc9110) - Norma de referência global da IETF com as semânticas, códigos de status e métodos do protocolo HTTP.
* [IETF RFC 8446 - The Transport Layer Security (TLS) Protocol Version 1.3](https://datatracker.ietf.org/doc/html/rfc8446) - Especificação oficial do protocolo TLS 1.3 para canal seguro de comunicação na Internet.
* [IETF RFC 4253 - The Secure Shell (SSH) Transport Layer Protocol](https://datatracker.ietf.org/doc/html/rfc4253) - Especificação oficial da arquitetura de transporte e autenticação criptográfica do protocolo SSH.
* [Wi-Fi Alliance - Wi-Fi CERTIFIED WPA3 Security Highlights](https://www.wi-fi.org/discover-wi-fi/security) - Visão geral técnica oficial dos mecanismos do WPA3 e protocolo SAE (Simultaneous Authentication of Equals).
* [NIST SP 800-41 Rev. 1 - Guidelines on Firewalls and Firewall Policy](https://csrc.nist.gov/pubs/sp/800/41/r1/final) - Recomendações oficiais do NIST para arquitetura de firewalls e regras de segurança de rede.
* KUROSE, James F.; ROSS, Keith W. **Redes de Computadores e a Internet: Uma Abordagem Top-Down**. 7. ed. São Paulo: Pearson Education do Brasil, 2017. (Cap. 2 - Camada de Aplicação: HTTP, SMTP, DNS; Cap. 6 - Redes Sem Fio e Móveis; Cap. 8 - Segurança em Redes).
* TANENBAUM, Andrew S.; WETHERALL, David. **Redes de Computadores**. 5. ed. São Paulo: Pearson, 2011. (Cap. 4 - A Subcamada de Controle de Acesso ao Meio: Padrões IEEE 802.11; Cap. 8 - Segurança de Rede).
* STALLINGS, William. **Criptografia e Segurança de Redes: Princípios e Práticas**. 7. ed. São Paulo: Pearson Education do Brasil, 2018. (Cap. 17 - Segurança de Camada de Transporte: TLS; Cap. 20 - Firewalls).
