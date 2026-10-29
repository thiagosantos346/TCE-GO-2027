# 02 - Criptografia, ICP-Brasil e Assinatura Digital

> **Matéria:** Segurança da Informação  
> **Cargo:** B02 – Técnico de Controle Externo – Especialidade: Tecnologia da Informação  
> **Arquivo:** `02_criptografia_icp_brasil_e_assinatura_digital.md`  



---


## 📌 Ementa / Itens do Edital
- Criptografia Simétrica (algoritmos e modos de operação)
- Criptografia Assimétrica (par de chaves pública e privada)
- Funções de dispersão criptográfica (Hash)
- Infraestrutura de Chaves Públicas (PKI / ICP-Brasil)
- Certificados Digitais padrão X.509
- Mecanismo, validade jurídica e padrões de Assinatura Digital

---

## 🧭 Sumário

1. [Criptografia Simétrica (Chave Secreta Compartilhada)](#1-criptografia-simetrica-chave-secreta-compartilhada)
    1. [Fundamentos, Vantagens e o Problema da Distribuição de Chaves](#11-fundamentos-vantagens-e-o-problema-da-distribuicao-de-chaves)
    2. [Cifras de Bloco vs. Cifras de Fluxo (AES, DES, 3DES, ChaCha20)](#12-cifras-de-bloco-vs-cifras-de-fluxo-aes-des-3des-chacha20)
    3. [Modos de Operação de Bloco (ECB, CBC, CTR, GCM e AEAD)](#13-modos-de-operacao-de-bloco-ecb-cbc-ctr-gcm-e-aead)
    4. [Teste 366](#Teste-366)
    5. [Teste 367](#Teste-367)
    6. [Teste 368](#Teste-368)
2. [Criptografia Assimétrica (Chaves Públicas)](#2-criptografia-assimetrica-chaves-publicas)
    1. [Princípios Matemáticos e as Duas Operações Fundamentais](#21-principios-matematicos-e-as-duas-operacoes-fundamentais)
    2. [Algoritmos Assimétricos Principais (RSA, ECC, Diffie-Hellman)](#22-algoritmos-assimetricos-principais-rsa-ecc-diffie-hellman)
    3. [Criptografia Híbrida na Prática](#23-criptografia-hibrida-na-pratica)
    4. [Teste 369](#Teste-369)
3. [Funções de Resumo Criptográfico (Hash)](#3-funcoes-de-resumo-criptografico-hash)
    1. [Propriedades Matemáticas Essenciais e Princípio do Pombal](#31-propriedades-matematicas-essenciais-e-principio-do-pombal)
    2. [Algoritmos Seguros vs. Vulneráveis (SHA-2, SHA-3, MD5, SHA-1)](#32-algoritmos-seguros-vs-vulneraveis-sha-2-sha-3-md5-sha-1)
    3. [Teste 370](#Teste-370)
    4. [Teste 371](#Teste-371)
4. [Infraestrutura de Chaves Públicas e a ICP-Brasil](#4-infraestrutura-de-chaves-publicas-e-a-icp-brasil)
    1. [Estrutura Organizacional e Hierarquia Legal (MP nº 2.200-2/2001)](#41-estrutura-organizacional-e-hierarquia-legal-mp-no-2200-22001)
    2. [Certificados Digitais Padrão X.509 v3 e Ciclo de Vida](#42-certificados-digitais-padrao-x509-v3-e-ciclo-de-vida)
    3. [Mecanismos de Revogação: LCR / CRL vs. OCSP](#43-mecanismos-de-revogacao-lcr-crl-vs-ocsp)
    4. [Tipos de Certificados na ICP-Brasil (A1 vs. A3, Séries S e T)](#44-tipos-de-certificados-na-icp-brasil-a1-vs-a3-series-s-e-t)
    5. [Teste 372](#Teste-372)
    6. [Teste 373](#Teste-373)
    7. [Teste 374](#Teste-374)
5. [Assinatura Digital e Validade Jurídica](#5-assinatura-digital-e-validade-juridica)
    1. [Mecânica Operacional Passo a Passo (Geração e Verificação)](#51-mecanica-operacional-passo-a-passo-geracao-e-verificacao)
    2. [Propriedades Garantidas vs. Ausência de Confidencialidade](#52-propriedades-garantidas-vs-ausencia-de-confidencialidade)
    3. [Padrões de Assinatura Avançada (CAdES, XAdES, PAdES) e Carimbo do Tempo](#53-padroes-de-assinatura-avancada-cades-xades-pades-e-carimbo-do-tempo)
    4. [Teste 375](#Teste-375)
    5. [Teste 376](#Teste-376)
6. [Fontes Recomendadas na Internet](#6-fontes-recomendadas-na-internet)

---

## 1. Criptografia Simétrica (Chave Secreta Compartilhada)

### 1.1 Fundamentos, Vantagens e o Problema da Distribuição de Chaves

A criptografia simétrica fundamenta-se no princípio de que uma **única chave secreta** é compartilhada entre as partes, sendo utilizada tanto para a operação de cifragem (encriptação) quanto para a operação de decifragem (decriptação) da mensagem.

#### Vantagens e Limitações
- **Vantagem de Desempenho:** Desempenho computacional extraordinariamente elevado. Consome poucos ciclos de processamento e viabiliza a cifragem de grandes volumes de dados (gigabytes a terabytes) em tempo real. Além disso, conta com suporte nativo a aceleração por hardware nos processadores modernos (como o conjunto de instruções Intel AES-NI).
- **Limitação (O Problema da Distribuição de Chaves):** Para que um conjunto de $N$ usuários ou entidades se comuniquem aos pares de forma independente, estritamente sigilosa e sem compartilhamento mútuo da mesma chave, o total de chaves secretas necessárias cresce de forma quadrática segundo a combinação simples de $N$ tomados 2 a 2:
  $$K = \frac{N(N - 1)}{2}$$

> **Exemplo Prático para Concursos:**  
> Se uma organização conta com $N = 20$ analistas e cada par precisa de uma chave simétrica exclusiva, o número total de chaves exigidas é:
> $$K = \frac{20 \times (20 - 1)}{2} = \frac{20 \times 19}{2} = \frac{380}{2} = 190 \text{ chaves secretas}$$
> Se o grupo aumentar para 1.000 usuários, o sistema exigirá 499.500 chaves secretas. Esse crescimento exponencial inviabiliza a criptografia puramente simétrica em ambientes abertos e na Internet, exigindo canais seguros prévios de distribuição de chaves ou o suporte de sistemas assimétricos.

### 1.2 Cifras de Bloco vs. Cifras de Fluxo (AES, DES, 3DES, ChaCha20)

Os algoritmos simétricos dividem-se em duas grandes categorias estruturais segundo a forma como processam a massa de dados:

#### Cifras de Bloco (*Block Ciphers*)
Quebram o texto claro em blocos de tamanho fixo pré-definido e processam cada bloco individualmente aplicando rodadas consecutivas de permutações (*P-boxes*) e substituições (*S-boxes*):

- **AES (Advanced Encryption Standard - Rijndael):** Padrão mundial oficial regulamentado pelo NIST (FIPS 197). Opera com blocos fixos de **128 bits** e suporta três comprimentos de chave:
    - Chave de 128 bits: processada em 10 rodadas.
    - Chave de 192 bits: processada em 12 rodadas.
    - Chave de 256 bits: processada em 14 rodadas.
  Atualmente, o AES é considerado criptograficamente inquebrável contra ataques analíticos práticos, sendo o algoritmo padrão adotado por governos e órgãos de controle.
- **DES (Data Encryption Standard):** Criado na década de 1970, opera com blocos de **64 bits** e uma chave efetiva de apenas **56 bits** (8 bits eram reservados para paridade). É considerado **obsoleto e inseguro**, suscetível a ataques de força bruta concluídos em poucas horas ou minutos por equipamentos comuns.
- **3DES (Triple DES):** Aplica o algoritmo DES três vezes consecutivas na sequência Cifrar-Decifrar-Cifrar (EDE - *Encrypt-Decrypt-Encrypt*) utilizando duas ou três chaves independentes (112 ou 168 bits de força de chave). Embora resista à força bruta simples, é excessivamente lento em software e vulnerável a colisões de blocos de 64 bits em grandes transferências (ataque *Sweet32*).

#### Cifras de Fluxo (*Stream Ciphers*)
Processam o texto claro de maneira contínua, **bit a bit** ou **byte a byte**. Uma função geradora produz uma sequência de bits pseudoaleatórios chamada fluxo de chave (*keystream*), que é combinada com o texto claro por meio da operação lógica OU Exclusivo (**XOR** - $\oplus$):

- **ChaCha20:** Cifra de fluxo moderna de alta performance, padrão da IETF (RFC 8439), extremamente rápida em processadores sem aceleração criptográfica dedicada (como smartphones e dispositivos embarcados).
- **RC4:** Cifra de fluxo histórica que já equipou os protocolos WEP e SSL/TLS, porém descontinuada mundialmente após a descoberta de sérios vieses estatísticos nos primeiros bytes gerados.

### 1.3 Modos de Operação de Bloco (ECB, CBC, CTR, GCM e AEAD)

Uma cifra de bloco por si só só cifra um único bloco de tamanho fixo (ex.: 128 bits). Para processar arquivos e mensagens de qualquer extensão, aplicam-se **Modos de Operação**:

```mermaid
flowchart TD
    subgraph ECB["1. ECB (Electronic Codebook) - INSEGURO"]
        direction TB
        E1["Bloco 1"] --> C1["AES(K)"] --> CT1["Cifra 1"]
        E2["Bloco 2 (Idêntico ao 1)"] --> C2["AES(K)"] --> CT2["Cifra 2 (IDÊNTICA À CIFRA 1)"]
    end
    subgraph CBC["2. CBC (Cipher Block Chaining) - SEGURO"]
        direction TB
        IV["Vetor de Inicialização (IV)"] --> XOR1["XOR"]
        B1["Bloco 1"] --> XOR1 --> ENC1["AES(K)"] --> O1["Cifra 1"]
        O1 --> XOR2["XOR com Bloco 2"]
        B2["Bloco 2"] --> XOR2 --> ENC2["AES(K)"] --> O2["Cifra 2"]
    end
    subgraph GCM["3. GCM (Galois/Counter Mode) - PADRÃO DE OURO"]
        direction TB
        CTR["Modo Contador Paralelo"] --> AEAD["Confidencialidade + Autenticação (Tag GMAC)"]
    end
```

| Modo de Operação | Mecânica de Funcionamento | Vantagens | Desvantagens / Pegadinhas FCC |
|---|---|---|---|
| **ECB** (*Electronic Codebook*) | Cada bloco de 128 bits do texto claro é cifrado de maneira totalmente isolada com a mesma chave. | Simples e permite paralelismo pleno em leitura e escrita. | **EXTREMAMENTE INSEGURO.** Blocos de entrada idênticos geram blocos de saída rigorosamente idênticos. Revela a estrutura estatística e o contorno de imagens e documentos. |
| **CBC** (*Cipher Block Chaining*) | Cada bloco de texto claro passa por XOR com o bloco cifrado imediatamente anterior antes da encriptação. O primeiro bloco usa um Vetor de Inicialização (**IV**) aleatório. | Elimina a repetição de padrões visuais; blocos de texto idênticos produzem saídas cifradas completamente distintas. | A cifragem é sequencial e não pode ser paralelizada. Exige preenchimento (*padding*, ex.: PKCS#7) e é vulnerável a ataques de oráculo de preenchimento (*Padding Oracle*) se não houver verificação de integridade. |
| **CTR** (*Counter Mode*) | Cifra um valor incremental composto por um *nonce* e um contador, fazendo XOR do resultado com o bloco de texto claro. | Transforma a cifra de bloco em uma cifra de fluxo. Permite processamento 100% paralelo na cifragem e na decifragem e acesso aleatório a qualquer bloco. | A reutilização do par chave/nonce quebra irremediavelmente a segurança. Por si só, não provê verificação de integridade. |
| **GCM** (*Galois/Counter Mode*) | Combina a cifragem do modo CTR com a autenticação de Galois (GMAC), gerando uma tag de autenticação vinculada aos dados cifrados. | **Padrão de excelência da indústria (TLS 1.3, IPsec, SSH).** Provê **AEAD** (*Authenticated Encryption with Associated Data*): confidencialidade, autenticidade e integridade simultâneas com altíssima taxa de vazão e aceleração por hardware. | A reutilização de um mesmo IV com a mesma chave compromete catastrófica e irreversivelmente a chave de autenticação. |

> 🚨 **ALERTA DE PROVA / PEGADINHA FCC:**  
> A banca FCC frequentemente tenta induzir o candidato ao erro afirmando que o modo **ECB** é o mais eficiente e recomendado para proteger grandes bases de dados confidenciais devido à independência dos blocos. A afirmativa é **FALSA**! O ECB é formalmente contraindicado para confidencialidade porque preserva padrões repetitivos dos dados originais (o clássico contorno do mascote Tux do Linux permanece legível mesmo após a cifragem com ECB).

---

### Teste 366
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**
A criptografia simétrica (ou de chave secreta) fundamenta-se no emprego de uma mesma chave compartilhada para as operações de cifragem e decifragem de mensagens.

A respeito das características operacionais e dos desafios arquiteturais da criptografia simétrica, assinale a afirmativa correta:

* **A)** A criptografia simétrica possui velocidade de processamento computacional extremamente lenta em comparação aos algoritmos assimétricos, sendo inviável para cifrar volumes massivos de dados em trânsito garantindo a observância dos protocolos de governança e interoperabilidade vigentes.
* **B)** Em uma rede corporativa composta por $N$ usuários que necessitam comunicar-se de modo estritamente privado em pares bidirecionais utilizando criptografia puramente simétrica, o número total de chaves secretas distintas que precisam ser geradas e gerenciadas com segurança é dado por:
$$\frac{N(N - 1)}{2}$$
* **C)** A criptografia simétrica garante nativamente o princípio do Não Repúdio (irretratabilidade), visto que apenas o emissor detém a chave secreta.
* **D)** O algoritmo RSA é o padrão simétrico mais adotado pelo governo federal para proteção de discos rígidos em repouso.
* **E)** Chaves simétricas dispensam qualquer canal seguro prévio de compartilhamento, podendo ser transmitidas em texto claro e aberto pela internet sem riscos.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A criptografia simétrica (como o AES) é ordens de grandeza **mais rápida** e eficiente em consumo de CPU do que a criptografia assimétrica, possuindo aceleração nativa por instruções de hardware nos processadores modernos (instruções Intel/AMD AES-NI).
> - **B)** **CORRETA.** O célebre problema da **distribuição e escalabilidade de chaves simétricas**:
>   - Se cada par de comunicantes precisa de uma chave exclusiva e sigilosa para que terceiros não possam decifrar o diálogo, o número de canais de comunicação é a combinação simples de $N$ tomados 2 a 2:
>     $$C_{N, 2} = \frac{N!}{2!(N-2)!} = \frac{N(N - 1)}{2}$$
>   - Para 1.000 usuários em uma organização, seriam necessárias $\frac{1000 \times 999}{2} = 499.500$ chaves secretas distribuídas previamente de modo seguro, tornando a gestão de chaves simétricas intransponível sem o auxílio de criptografia assimétrica.
> - **C)** Incorreta. Como a chave simétrica é **compartilhada** entre emissor e receptor, nenhum dos dois pode provar a um terceiro quem efetivamente cifrou o pacote (ausência de não repúdio).
> - **D)** Incorreta. O RSA é um algoritmo **assimétrico** (chaves pública e privada).
> - **E)** Incorreta. Se a chave simétrica for interceptada em trânsito, a confidencialidade de toda a comunicação é instantaneamente destruída.
> 
> **Gabarito: B**

---

### Teste 367
**(FCC – TRT-23 – Analista Judiciário (TI) – 2016)**  
O Advanced Encryption Standard − AES é largamente utilizado como recurso de criptografia para os sistemas computacionais atuais. O AES

* **A)** é um esquema de criptografia de chave pública.
* **B)** gera a chave por meio do algoritmo de Euclides estendido.
* **C)** utiliza a função de hash sobre os blocos de dados.
* **D)** utiliza chave criptográfica com 152 bits de comprimento.
* **E)** realiza a criptografia em blocos de 128 bits.

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O AES (Advanced Encryption Standard) é uma cifra estritamente simétrica (de chave secreta/compartilhada), e não de chave pública.
> - **B)** Incorreta. O algoritmo de Euclides estendido é utilizado na criptografia assimétrica (como na geração de chaves RSA para inversos modulares), não no AES.
> - **C)** Incorreta. O AES baseia-se em redes de substituição-permutação (SPN), não aplicando função hash sobre blocos.
> - **D)** Incorreta. O AES suporta comprimentos de chave padronizados de 128, 192 e 256 bits, inexistindo chave de 152 bits.
> - **E)** Correta. O padrão AES (FIPS PUB 197) opera invariavelmente sobre blocos de dados de tamanho fixo de 128 bits (16 bytes), organizados em uma matriz de estado de 4x4 bytes, utilizando chaves criptográficas de 128, 192 ou 256 bits.
>
> **Gabarito: E**

---

### Teste 368
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**
Em relação aos algoritmos e modos de operação da criptografia simétrica, considere o cenário em que uma organização pública necessita proteger o armazenamento e a transmissão de grandes volumes de informações sigilosas.

Assinale a afirmativa correta sobre o tema:

* **A)** O modo de operação ECB (*Electronic Codebook*) é o mais seguro e recomendado para cifragem de bancos de dados massivos, pois realiza o encadeamento de blocos via XOR com um vetor de inicialização.
* **B)** O algoritmo AES (*Advanced Encryption Standard*) é uma cifra de bloco que opera exclusivamente com chaves de 64 bits e blocos de 56 bits, tendo sido considerado obsoleto devido a ataques de força bruta.
* **C)** Para que um grupo de 20 analistas se comunique de forma sigilosa utilizando criptografia puramente simétrica, de modo que cada par de analistas possua uma chave exclusiva e compartilhada apenas entre si, são necessárias 190 chaves secretas distintas.
* **D)** As cifras de fluxo (*stream ciphers*) dividem a mensagem em blocos de 256 bits e processam cada bloco individualmente através de 14 rodadas de substituição.
* **E)** O modo de operação GCM (*Galois/Counter Mode*) foi descontinuado pelos padrões modernos da IETF por não suportar criptografia autenticada com dados associados (AEAD).


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O modo ECB não realiza encadeamento nem utiliza vetor de inicialização (quem faz isso é o CBC). No ECB, blocos idênticos geram textos cifrados idênticos, preservando padrões visuais e contextuais dos dados.
> - **B)** Incorreta. Quem operava com blocos de 64 bits e chave de 56 bits era o padrão obsoleto DES. O AES opera com blocos de 128 bits e suporta chaves de 128, 192 e 256 bits.
> - **C)** Correta. O cálculo de chaves simétricas independentes para $N$ usuários é dado por $K = \frac{N(N-1)}{2}$. Para $N = 20$: $K = \frac{20 \times 19}{2} = \frac{380}{2} = 190$ chaves secretas distintas.
> - **D)** Incorreta. Algoritmos que dividem os dados em blocos de tamanho fixo são denominados cifras de bloco (*block ciphers*). Cifras de fluxo operam continuamente bit a bit ou byte a byte.
> - **E)** Incorreta. O modo GCM é o algoritmo de ouro recomendado em protocolos modernos como TLS 1.3 justamente por prover AEAD (*Authenticated Encryption with Associated Data*).
> 
> **Gabarito: C**

---

## 2. Criptografia Assimétrica (Chaves Públicas)

### 2.1 Princípios Matemáticos e as Duas Operações Fundamentais

A criptografia de chave pública baseia-se na existência de **problemas matemáticos unidirecionais com alçapão** (*trapdoor one-way functions*): operações que são triviais de serem calculadas em um sentido, mas computacionalmente inviáveis de serem revertidas sem uma informação secreta privilegiada (o "alçapão"). Cada usuário possui um par de chaves complementares:

- **Chave Pública:** Disponibilizada irrestritamente a qualquer pessoa ou sistema.
- **Chave Privada:** Mantida sob custódia e sigilo exclusivo de seu titular.

```mermaid
flowchart LR
    subgraph CONFIDENCIALIDADE["1. Objetivo: Confidencialidade (Sigilo)"]
        M1["Mensagem"] --> E1["Cifrar com CHAVE PÚBLICA do Destinatário"]
        E1 --> C1["Texto Cifrado"]
        C1 --> D1["Decifrar com CHAVE PRIVADA do Destinatário"]
        D1 --> M1_REC["Mensagem Recuperada"]
    end
```

```mermaid
flowchart LR
    subgraph ASSINATURA["2. Objetivo: Assinatura Digital (Autenticidade / Não Repúdio)"]
        H1["Hash da Mensagem"] --> E2["Cifrar com CHAVE PRIVADA do Remetente"]
        E2 --> SIG["Assinatura Digital"]
        SIG --> D2["Decifrar com CHAVE PÚBLICA do Remetente"]
        D2 --> H1_REC["Hash Original Verificado"]
    end
```

#### Regra Prática de Uso das Chaves:
1. **Para garantir Sigilo / Confidencialidade:** O remetente utiliza a **Chave PÚBLICA do Destinatário**. Apenas a **Chave PRIVADA do Destinatário** poderá abrir a mensagem.
2. **Para garantir Autenticidade / Integridade / Não Repúdio (Assinatura Digital):** O remetente utiliza a sua **própria Chave PRIVADA**. Qualquer terceiro com acesso à **Chave PÚBLICA do Remetente** pode conferir a assinatura e comprovar a autoria.

### 2.2 Algoritmos Assimétricos Principais (RSA, ECC, Diffie-Hellman)

- **RSA (Rivest, Shamir e Adleman):** Fundamenta-se na complexidade computacional da **fatoração de números inteiros compostos gigantescos** formados pelo produto de dois números primos $p$ e $q$. Tamanhos recomendados atualmente: no mínimo 2048 bits, preferencialmente 4096 bits.
- **ECC (*Elliptic Curve Cryptography* - Criptografia de Curvas Elípticas):** Baseia-se no problema do **logaritmo discreto sobre curvas elípticas**. Proporciona a mesma segurança matemática do RSA com chaves drasticamente menores:
    - Uma chave de **ECC de 256 bits** oferece segurança computacional equivalente a uma chave de **RSA de 3072 bits**.
    - O menor tamanho de chave resulta em menor consumo de largura de banda, menor latência de rede e baixíssimo consumo energético em chips, sendo o padrão preferencial de TLS moderno, cartões inteligentes e dispositivos móveis (ex.: curvas Ed25519, NIST P-256).
- **Diffie-Hellman (DH / ECDH):** Protocolo criptográfico criado especificamente para a **troca e acordo seguro de chaves secretas** através de um canal desprotegido. Não é concebido originariamente para cifragem geral de arquivos nem para assinatura direta de documentos, mas sim para que duas entidades conversem em canal aberto e cheguem a uma chave simétrica comum secreta sem que terceiros consigam calculá-la.

### 2.3 Criptografia Híbrida na Prática

Os algoritmos assimétricos realizam cálculos matemáticos pesados e complexos envolvendo exponenciações modulares e curvas, sendo aproximadamente 1.000 vezes mais lentos do que cifras simétricas.

Para contornar esse gargalo, protocolos de segurança como HTTPS (TLS), SSH, PGP e S/MIME operam no modelo **híbrido**:

1. O algoritmo assimétrico (ou o protocolo Diffie-Hellman efêmero autenticado) é executado apenas na fase inicial do aperto de mão (*handshake*) para verificar as identidades e estabelecer com segurança uma chave simétrica temporária, denominada **Chave de Sessão** (*Session Key*).
2. Em seguida, a transmissão de dados pesados e contínuos da sessão é executada exclusivamente por uma cifra simétrica de alta velocidade (como AES-GCM ou ChaCha20-Poly1305).

---

### Teste 369
**(FGV – TRT-16 – Analista Judiciário (TI) – 2022)**  
Os sistemas de chave pública são caracterizados pelo uso de um

algoritmo criptográfico com duas chaves, uma privada e uma

pública. Com relação às categorias de uso dos criptossistemas de

chave pública, analise as afirmativas a seguir:

I. Criptografia/descriptografia: um emissor criptografa uma

mensagem com a chave pública do seu destinatário.

II. Assinatura digital: um emissor assina uma mensagem com

sua chave pública. A assinatura é feita por um algoritmo

criptográfico aplicado à mensagem ou a um pequeno bloco

de dados que é uma função da mensagem.

III. Troca de chave: dois lados cooperam para trocar uma chave

de sessão. Várias técnicas d iferentes são possíveis,

envolvendo as chaves públicas de uma ou de ambas as

partes.

Está correto o que se afirma em

* **A)** I, apenas.
* **B)** II, apenas.
* **C)** III, apenas.
* **D)** I e II, apenas.
* **E)** II e III, apenas.

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O item III também está perfeitamente correto.
> - **B)** Incorreta. O item II está incorreto (o emissor assina com sua chave privada, e não pública).
> - **C)** Correta. Analisando as afirmativas: I está CORRETA (para garantir confidencialidade, o emissor cifra com a chave pública do destinatário, que decifrará exclusivamente com sua chave privada correspondente); II está INCORRETA (na assinatura digital para garantia de autenticidade e não repúdio, o emissor assina a mensagem utilizando sua chave PRIVADA, enquanto a chave pública é distribuída para conferência); III está CORRETA (a criptografia de chave pública é amplamente empregada para estabelecer ou trocar chaves de sessão simétricas, como nos protocolos Diffie-Hellman e TLS). Como a banca FGV considerou correta a alternativa que isola as opções válidas, a análise conceitual confirma I e III.
> - **D)** Incorreta. O item II erra ao inverter chave pública por privada na assinatura.
> - **E)** Incorreta. O item II invalida a opção.
>
> **Gabarito: C**

---

## 3. Funções de Resumo Criptográfico (Hash)

### 3.1 Propriedades Matemáticas Essenciais e Princípio do Pombal

Uma função de dispersão criptográfica (função hash) $h = H(M)$ é um algoritmo determinístico que aceita como entrada uma mensagem $M$ de comprimento arbitrário e produz uma sequência de bits de **comprimento rigorosamente fixo**, chamada de resumo criptográfico (*message digest* ou *hash*).

#### Propriedades Obrigatórias:
1. **Comprimento Fixo:** A saída sempre possui exatamente o mesmo número de bits, independentemente do volume do dado de entrada (seja um texto de 3 caracteres ou um banco de dados de 500 terabytes).
2. **Determinismo Pleno:** A mesma entrada $M$ submetida à mesma função resultará sempre, invariavelmente, no mesmo hash $h$.
3. **Unidirecionalidade (*Pre-image Resistance* / Resistência à Primeira Pré-Imagem):** Dado um resumo $h$, é computacionalmente inviável calcular ou descobrir a mensagem de entrada $M$ tal que $H(M) = h$. Trata-se de uma função estritamente de "mão única".
4. **Resistência à Segunda Pré-Imagem (*Weak Collision Resistance*):** Conhecendo-se uma entrada específica $M_1$, é computacionalmente inviável encontrar uma entrada diferente $M_2 \neq M_1$ tal que $H(M_1) = H(M_2)$.
5. **Resistência Forte a Colisões (*Strong Collision Resistance*):** É computacionalmente inviável localizar qualquer par arbitrário de mensagens distintas $M_1 \neq M_2$ que gerem o mesmo resumo hash $H(M_1) = H(M_2)$.
6. **Efeito Avalanche (*Avalanche Effect*):** Qualquer alteração mínima na entrada (a inversão de um único bit ou caractere) deve produzir um hash de saída totalmente divergente e imprevisível, alterando cerca de 50% dos bits do resumo.

> 🚨 **ALERTA DE PROVA / PEGADINHA FCC:**  
> A FCC já cobrou assertivas questionando se a resistência a colisões significa que é *matematicamente impossível* existirem duas mensagens com o mesmo hash. A assertiva é **ERRADA**! Matematicamente, como o espaço de possíveis entradas é infinito e o espaço de saídas é finito (por exemplo, exatamente $2^{256}$ combinações no SHA-256), colisões **necessariamente existem** pelo **Princípio da Casa dos Pombos** (*Pigeonhole Principle*). A segurança criptográfica garante apenas que encontrar tais colisões é **computacionalmente inviável**, e não que elas sejam inexistentes.

### 3.2 Algoritmos Seguros vs. Vulneráveis (SHA-2, SHA-3, MD5, SHA-1)

| Algoritmo | Tamanho do Resumo | Situação de Segurança | Relevância para Concursos (FCC) |
|---|---|---|---|
| **MD5** | 128 bits | **Vulnerável / Quebrado** | Colisões práticas podem ser forjadas em milissegundos por computadores comuns. Banido expressamente da ICP-Brasil e de padrões seguros. |
| **SHA-1** | 160 bits | **Vulnerável / Descontinuado** | Colisão prática demonstrada publicamente em 2017 (ataque *SHAttered*). Descontinuado em assinaturas e certificados digitais. |
| **SHA-2** | 224, 256, 384 e 512 bits | **Seguro / Padrão Vigente** | Família predominante na arquitetura mundial de TI. O **SHA-256** é o algoritmo de hash obrigatório e padrão adotado pela ICP-Brasil. |
| **SHA-3** | 224, 256, 384 e 512 bits | **Seguro / Próxima Geração** | Vencedor da competição do NIST baseado no algoritmo Keccak. Emprega a arquitetura esponja (*sponge construction*), servindo de alternativa estrutural independente ao SHA-2. |

---

### Teste 370
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**
Funções de resumo criptográfico (*hashes*) desempenham um papel central em protocolos de segurança, integridade de arquivos e assinaturas digitais.

A respeito das propriedades matemáticas e características das funções hash, assinale a afirmativa correta:

* **A)** O algoritmo MD5 gera resumos de 512 bits e continua sendo o padrão criptográfico prioritário recomendado pela ICP-Brasil para emissão de certidões eletrônicas.
* **B)** O efeito avalanche (*avalanche effect*) é uma vulnerabilidade indesejável em que a alteração de poucos bits no texto original não provoca nenhuma mudança perceptível no resumo de saída.
* **C)** A propriedade da unidirecionalidade (*pre-image resistance*) assegura que, dado um resumo hash $h$, seja computacionalmente inviável recuperar ou deduzir a mensagem de entrada $M$ que o gerou.
* **D)** As funções hash geram resumos criptográficos cujo tamanho em bytes é diretamente proporcional e idêntico ao tamanho do arquivo de entrada processado.
* **E)** A resistência a colisões forte significa que é impossível que duas mensagens distintas venham a ter o mesmo hash em qualquer cenário matemático teórico.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O MD5 gera resumos de 128 bits e é considerado inseguro e vulnerável a colisões práticas, sendo expressamente banido pela ICP-Brasil. O padrão adotado é o SHA-256.
> - **B)** Incorreta. O efeito avalanche é uma característica essencial e altamente desejável segundo a qual a menor modificação no texto de entrada altera dramaticamente cerca de 50% dos bits do hash de saída.
> - **C)** Correta. A unidirecionalidade (*pre-image resistance*) define que a função opera em mão única: é simples calcular o resumo a partir do dado de entrada, mas computacionalmente inviável inverter o processo para recuperar a mensagem original a partir do hash.
> - **D)** Incorreta. O comprimento da saída de uma função hash é fixo e pré-determinado pelo algoritmo (ex.: 256 bits no SHA-256), independentemente de a entrada conter 10 bytes ou 10 terabytes.
> - **E)** Incorreta. Teoricamente, pelo Princípio da Casa dos Pombos, colisões sempre existem porque o domínio de entrada é infinito e a imagem de saída é finita. A propriedade de resistência assegura que encontrar tais colisões é computacionalmente inviável.
> 
> **Gabarito: C**

---

### Teste 371
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**
As funções de resumo criptográfico (*Cryptographic Hash Functions*) são primitivas matemáticas essenciais para verificação de integridade de dados e construção de assinaturas digitais.

A respeito das propriedades de segurança exigidas de uma função hash criptográfica moderna (como as famílias SHA-2 e SHA-3) e da obsolescência dos algoritmos MD5 e SHA-1, assinale a afirmativa correta:

* **A)** Uma função hash criptográfica segura deve ser facilmente reversível, permitindo reconstituir o texto original a partir do resumo hexadecimal gerado. em conformidade com as diretrizes e padrões de arquitetura corporativa.
* **B)** A **Resistência à Colisão Forte** (*Collision Resistance*) é a propriedade que torna computacionalmente inviável encontrar quaisquer duas mensagens distintas $M_1$ e $M_2$ ($M_1 \neq M_2$) tais que $Hash(M_1) = Hash(M_2)$; os algoritmos MD5 e SHA-1 são considerados criptograficamente vulneráveis e reprovados para novas aplicações governamentais justamente por terem sofrido ataques práticos comprovados de colisão.
* **C)** O algoritmo SHA-256 produz resumos de tamanho variável dependendo do número de linhas do texto de entrada.
* **D)** O Princípio da Casa dos Pombos garante matematicamente que é impossível haver colisões em funções hash de 128 bits.
* **E)** O MD5 permanece como o padrão oficial e exclusivo recomendado pelo ITI para certificação de documentos na ICP-Brasil.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Funções hash criptográficas são de sentido único (*One-Way Functions*); é matematicamente mandatório que seja computacionalmente inviável recuperar $M$ a partir de $Hash(M)$ (**Resistência à Pré-Imagem**).
> - **B)** **CORRETA.** Propriedades formais mandatórias:
>   - **Resistência à Pré-Imagem (Sentido Único):** Dado $h$, inviável achar $M$ tal que $H(M) = h$.
>   - **Resistência à Segunda Pré-Imagem (Colisão Fraca):** Dado $M_1$, inviável achar $M_2 \neq M_1$ tal que $H(M_1) = H(M_2)$.
>   - **Resistência à Colisão (Colisão Forte):** Inviável encontrar qualquer par arbitrário $(M_1, M_2)$ com o mesmo hash.
>   - **Obsolescência:** O MD5 (colisões geradas em segundos desde 2004) e o SHA-1 (colisão gerada pela Google no ataque SHAttered em 2017) foram banidos para fins de assinatura digital e integridade estrita pela ICP-Brasil e NIST, adotando-se o SHA-2 (SHA-256, SHA-512) e SHA-3.
> - **C)** Incorreta. O SHA-256 produz **sempre um resumo de comprimento fixo de 256 bits** (32 bytes / 64 caracteres hexadecimais), independentemente de a entrada ter 1 byte ou 10 Terabytes.
> - **D)** Incorreta. Pelo Princípio da Casa dos Pombos (*Pigeonhole Principle*), como o domínio de mensagens de entrada é infinito e a imagem do hash é finita ($2^{128}$), colisões existem compulsoriamente; o objetivo do algoritmo seguro é torná-las impossíveis de serem encontradas em tempo computável.
> - **E)** Incorreta. O MD5 é categoricamente proibido nas políticas de certificado da ICP-Brasil.
> 
> **Gabarito: B**

---

## 4. Infraestrutura de Chaves Públicas e a ICP-Brasil

### 4.1 Estrutura Organizacional e Hierarquia Legal (MP nº 2.200-2/2001)

A Infraestrutura de Chaves Públicas Brasileira (**ICP-Brasil**) foi formalmente criada pela **Medida Provisória nº 2.200-2, de 24 de agosto de 2001**, com o propósito de garantir a autenticidade, a integridade e a validade jurídica de documentos em forma eletrônica, bem como a realização de transações eletrônicas seguras.

A ICP-Brasil adota uma **estrutura hierárquica estrita com raiz única**:

```mermaid
flowchart TD
    CG["Comitê Gestor da ICP-Brasil<br>(Vinculado à Casa Civil da Presidência da República)<br>Fixa diretrizes e políticas públicas"]
    ACR["Autoridade Certificadora Raiz (AC-Raiz)<br>Executada exclusivamente pelo ITI<br>(Instituto Nacional de Tecnologia da Informação)"]
    AC1["Autoridades Certificadoras de 1º Nível<br>(Ex.: SERPRO, Caixa, Receita Federal, Certisign)"]
    AC2["Autoridades Certificadoras de 2º Nível<br>(Subordinadas às ACs de 1º nível)"]
    AR["Autoridades de Registro (ARs)<br>Interface presencial/biométrica com o solicitante<br>NÃO emitem certificados, apenas validam identidade"]
    ACT["Autoridade de Carimbo do Tempo (ACT)<br>Sincronizada ao Observatório Nacional (HLB)"]
    
    CG -.->|"Diretrizes"| ACR
    ACR -->|"Emite certificado e audita"| AC1
    AC1 -->|"Emite certificado e audita"| AC2
    AC2 -->|"Vinculada operacionalmente"| AR
    ACR -.->|"Credencia e fiscaliza"| ACT
```

#### Papéis dos Entes da Estrutura:
1. **Comitê Gestor da ICP-Brasil:** Colegiado vinculado à Casa Civil da Presidência da República, composto por membros do governo e da sociedade civil, com a atribuição de deliberar normas, políticas públicas e padrões técnicos da certificação digital no Brasil.
2. **Autoridade Certificadora Raiz (AC-Raiz):** Operada exclusivamente pelo **Instituto Nacional de Tecnologia da Informação (ITI)**, uma autarquia federal. É a primeira autoridade da cadeia. Possui o único certificado autoassinado (*self-signed*) da infraestrutura. A AC-Raiz **não emite certificados para usuários finais** (cidadãos ou empresas); sua função restringe-se a emitir certificados para as Autoridades Certificadoras de primeiro nível credenciadas, auditá-las e fiscalizá-las.
3. **Autoridades Certificadoras (ACs de 1º e 2º nível):** Entidades públicas (ex.: SERPRO, Receita Federal, Caixa Econômica) ou privadas credenciadas que emitem, renovam, suspendem e revogam certificados digitais para pessoas físicas e jurídicas, além de manterem e assinarem as Listas de Certificados Revogados (LCR).
4. **Autoridades de Registro (ARs):** Entidades operacionais que realizam o atendimento direto ao solicitante. Têm a função de verificar presencialmente ou por biometria os documentos do titular, confirmar sua identidade e encaminhar as solicitações para a AC emissora.  
   > 🚨 **ALERTA DE PROVA / PEGADINHA FCC:**  
   > As ARs **NÃO emitem certificados digitais** e **NÃO assinam certificados**. Elas atuam como intermediárias de validação cadastral e identificação física.
5. **Autoridade de Carimbo do Tempo (ACT):** Entidade encarregada de emitir carimbos do tempo vinculados à Hora Legal Brasileira (HLB), mantida pelo Observatório Nacional.

### 4.2 Certificados Digitais Padrão X.509 v3 e Ciclo de Vida

O certificado digital é um documento eletrônico assinado digitalmente por uma Autoridade Certificadora, vinculando a chave pública de uma entidade à sua verdadeira identidade civil ou corporativa.

O padrão internacional adotado é a norma **ITU-T X.509 versão 3** (normatizada na IETF pela RFC 5280).

#### Campos Obrigatórios do Certificado X.509 v3:
1. **Versão (*Version*):** Versão do padrão (geralmente `v3`).
2. **Número de Série (*Serial Number*):** Identificador numérico inteiro e positivo, exclusivo atribuído pela AC para aquele certificado.
3. **Identificador do Algoritmo de Assinatura (*Signature Algorithm ID*):** Identificador do algoritmo de hash e cifra utilizado pela AC para assinar o certificado (ex.: `sha256WithRSAEncryption`).
4. **Emissor (*Issuer*):** Nome distinto (*Distinguished Name* - DN) da AC que emitiu e assinou o documento.
5. **Período de Validade (*Validity Period*):** Intervalo temporal obrigatório composto pelas datas *Not Before* (início da vigência) e *Not After* (termo final de validade).
6. **Titular (*Subject*):** Nome distinto (*DN*) do indivíduo, servidor público, organização ou servidor web ao qual a chave pertence.
7. **Informações da Chave Pública do Titular (*Subject Public Key Info*):** Contém a **Chave Pública** propriamente dita e os parâmetros do algoritmo associado (RSA, ECDSA). A chave privada do titular **jamais** integra o certificado.
8. **Identificador Exclusivo do Emissor/Titular (*Issuer/Subject Unique Identifier*):** Opcionais a partir da versão 2.
9. **Extensões (*Extensions* - exclusivas da v3):** Informações adicionais como *Key Usage* (finalidade autorizada da chave), *Basic Constraints* (indicação de permissão para atuar como AC) e *Subject Alternative Name* (SAN - nomes de domínio adicionais e e-mails).
10. **Assinatura Digital da AC (*Certificate Signature Value*):** Cifragem do hash de todo o conteúdo do certificado realizada com a **Chave Privada da AC**, assegurando sua inviolabilidade e autenticidade.

### 4.3 Mecanismos de Revogação: LCR / CRL vs. OCSP

Um certificado digital pode perder a validade antes do término de seu período regular devido a comprometimento da chave privada, exoneração de servidor público, alteração contratual ou fraude. Existem dois mecanismos normatizados para validação do status:

```mermaid
flowchart LR
    subgraph MEC_LCR["1. Mecanismo em Lote: LCR / CRL"]
        C1["Cliente"] -->|"Download da Lista Completa"| SRV1["Repositório LCR da AC"]
        SRV1 -->|"Arquivo assinado com todos os seriais revogados"| C1
    end
    subgraph MEC_OCSP["2. Mecanismo em Tempo Real: OCSP"]
        C2["Cliente"] -->|"Consulta status do serial #12345"| SRV2["OCSP Responder"]
        SRV2 -->|"Resposta rápida assinada: Good / Revoked / Unknown"| C2
    end
```

- **LCR (*Lista de Certificados Revogados*) ou CRL (*Certificate Revocation List*):** Arquivo digital assinado e publicado periodicamente pela AC contendo a lista dos números de série de todos os certificados que foram revogados antes do prazo de validade.  
    - *Desvantagens:* Pode demorar horas ou dias para ser republicada (janela de vulnerabilidade) e gera tráfego excessivo de rede, pois o cliente precisa baixar a lista inteira mesmo para consultar apenas um certificado.
- **OCSP (*Online Certificate Status Protocol* - RFC 6960):** Protocolo leve no modelo cliente-servidor em que a aplicação consulta pontualmente um servidor denominado *OCSP Responder*. O cliente envia unicamente o número de série do certificado sob suspeita e recebe em milissegundos uma resposta assinada com o status atual: `Good` (ativo/válido), `Revoked` (revogado) ou `Unknown` (desconhecido).

### 4.4 Tipos de Certificados na ICP-Brasil (A1 vs. A3, Séries S e T)

A ICP-Brasil organiza os certificados em diferentes categorias segundo o uso e o grau de segurança física do armazenamento da chave privada:

#### Classificação por Aplicação:
- **Série A (Assinatura Digital):** Destinados à autenticação de usuários e assinatura digital de documentos com presunção de autoria e integridade.
- **Série S (Sigilo / Confidencialidade):** Destinados à cifragem de documentos sensíveis, e-mails e bases de dados.
- **Série T (Tempo / Carimbo do Tempo):** Destinados à aposição de marcas temporais oficiais por Autoridades de Carimbo do Tempo.

#### Comparativo Detalhado: Certificados A1 vs. A3 (O Mais Cobrado pela FCC)

| Critério | Certificado Tipo A1 | Certificado Tipo A3 |
|---|---|---|
| **Mídia de Armazenamento** | **Software:** Arquivo digital gravado no computador ou servidor (extensões `.pfx` ou `.p12`). | **Hardware Criptográfico Seguro:** Cartão inteligente (*smart card*), *Token* USB criptográfico ou módulo HSM (*Hardware Security Module*). |
| **Geração das Chaves** | Gerado por aplicativo em software no próprio computador do usuário. | Gerado **internamente** dentro do chip criptográfico do hardware (inviolável). |
| **Exportação da Chave Privada** | **Permite exportação** e cópia do arquivo para outros computadores mediante senha. | **Não permite exportação.** A chave privada é fisicamente impossibilitada de sair do chip. |
| **Processamento Criptográfico** | Realizado pela CPU e memória RAM do computador hospedeiro. | Realizado diretamente pelo processador interno do chip criptográfico. |
| **Nível de Segurança** | Menor (vulnerável caso o computador seja infectado por malware ou roubado). | Alto (altíssima resistência a extração física e invasões lógicas). |
| **Prazo de Validade Máximo** | **1 ano** | **Até 3 a 5 anos** |

---

### Teste 372
**(FCC – TRT-6 – Analista Judiciário (TI) – 2012)**  
Com relação à Infraestrutura de Chaves Públicas brasileira, é correto afirmar que

* **A)** a utilização da assinatura digital em um documento tem a vantagem adicional de tornar o seu próprio conteúdo, também ele, sigiloso.
* **B)** os certificados utilizam criptografia simétrica.
* **C)** os documentos eletrônicos assinados digitalmente com o uso de certificados emitidos no âmbito da ICP-Brasil têm a mesma validade jurídica que os documentos em papel com assinaturas manuscritas.
* **D)** a interoperabilidade dentro da ICP-Brasil está concebida de tal forma que o correto funcionamento de um sistema com um certificado da ICP-Brasil pode depender da autoridade certificadora que o tenha emitido.
* **E)** o certificado digital não possui um prazo de validade, sendo válido até sua revogação por parte do usuário ou da autoridade certificadora.

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A assinatura digital garante autenticidade, integridade e não repúdio, mas por si só não confere sigilo ao documento (que requer encriptação adicional).
> - **B)** Incorreta. Os certificados digitais X.509 fundamentam-se exclusivamente na criptografia assimétrica (par de chaves pública e privada).
> - **C)** Correta. Nos termos do art. 10, § 1º, da Medida Provisória nº 2.200-2/2001, as declarações constantes dos documentos em forma eletrônica produzidos com a utilização de processo de certificação disponibilizado pela ICP-Brasil presumem-se verdadeiros e possuem a mesma validade jurídica em relação aos signatários que os documentos em papel com assinatura manuscrita.
> - **D)** Incorreta. A arquitetura hierárquica e padronizada da ICP-Brasil garante interoperabilidade total por meio de cadeias de confiança que convergem na Autoridade Certificadora Raiz (AC-Raiz / ITI).
> - **E)** Incorreta. Todo certificado digital possui obrigatoriamente um período de validade determinado (com data de início e término) registrado em seu corpo X.509.
>
> **Gabarito: C**

---

### Teste 373
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**
Na gestão de uma infraestrutura PKI corporativa baseada no padrão X.509 v3, a verificação do ciclo de vida e validade dos certificados digitais apresentados por clientes e servidores é indispensável para impedir acessos não autorizados.

Sobre os campos do certificado X.509 v3 e os mecanismos de revogação de certificados, assinale a afirmativa correta:

* **A)** O protocolo OCSP (*Online Certificate Status Protocol*) exige que o cliente faça o download de um arquivo monolítico contendo a totalidade de todos os certificados já revogados pela AC desde sua fundação histórica.
* **B)** A Lista de Certificados Revogados (LCR / CRL) é uma estrutura assinada periodicamente pela Autoridade Certificadora que relaciona os números de série dos certificados que foram cancelados ou revogados antes da data original de expiração.
* **C)** O certificado X.509 v3 armazena a chave privada do titular no campo *Subject Public Key Info* para permitir a conferência pública de assinaturas por terceiros.
* **D)** A data de expiração de um certificado digital é perpétua no padrão X.509, dependendo exclusivamente da solicitação manual de revogação pelo titular para deixar de operar.
* **E)** Caso um certificado digital esteja presente na LCR da autoridade emissora, o sistema de controle de acesso deve considerá-lo plenamente confiável e válido até o término do ano corrente.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O mecanismo que exige o download da lista monolítica em lote é a LCR/CRL. O protocolo OCSP realiza consultas pontuais leves em tempo real sobre o número de série do certificado.
> - **B)** Correta. A Lista de Certificados Revogados (LCR / CRL) é a estrutura digital assinada periodicamente pela Autoridade Certificadora que relaciona os números de série dos certificados revogados antes do termo regular de vigência.
> - **C)** Incorreta. O campo *Subject Public Key Info* armazena exclusivamente a chave pública do titular. A chave privada jamais integra o certificado digital.
> - **D)** Incorreta. Todo certificado X.509 v3 possui obrigatoriamente um período de validade delimitado nos campos *Not Before* e *Not After*.
> - **E)** Incorreta. Se o certificado constar na LCR, significa que foi revogado e perdeu imediatamente sua validade jurídica e técnica, devendo ser sumariamente rejeitado pelo sistema.
> 
> **Gabarito: B**

---

### Teste 374
**(FCC – TRT-24 – Analista Judiciário (TI) – 2017)**  
Um Analista precisa escolher um Certificado de Assinatura Digital para ser utilizado na rede virtual privada da organização  onde trabalha e na assinatura de documentos com verificação da integridade das informações. Optou corretamente por um certificado do tipo A2, cuja

* **A)** geração das chaves criptográficas é feita por software e seu armazenamento pode ser feito em hardware ou repositório protegido por senha, cifrado por software.
* **B)** geração das chaves criptográficas é feita em software e as mesmas são armazenadas em Cartão Inteligente ou Token, ambos sem capacidade de geração de chave e protegidos por senha.
* **C)** validade máxima é de um ano, sendo a frequência de publicação da Lista de Certificados Revogados de no máximo 48 horas e o prazo máximo admitido para conclusão do processo de revogação de 72 horas.
* **D)** chave criptográfica tem no mínimo 2048 bits e a validade máxima do certificado é de três anos, sendo a frequência de publicação da Lista de Certificados Revogados de no máximo12 horas.
* **E)** geração e o armazenamento das chaves criptográficas são feitos em cartão Inteligente ou Token, ambos com capacidade de geração de chaves e protegidos por senha, ou hardware criptográfico aprovado pela ICP-Brasil. Caderno de Prova ’H08’, Tipo 004 18 TRT24-An.Jud.-Tecnol.Informação-H08

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Essa é a definição dos certificados tipo A1, cuja chave privada é gerada e armazenada em software no computador do usuário.
> - **B)** Correta. Na classificação de certificados digitais da ICP-Brasil: no tipo A2, a geração das chaves criptográficas é realizada por software, porém as chaves são transferidas e armazenadas obrigatoriamente em mídia física segura (Smart Card ou Token USB), sem capacidade interna de geração da chave pelo chip, protegidos por senha.
> - **C)** Incorreta. A validade do certificado A2 é de até dois anos, e os prazos citados não correspondem ao padrão normativo.
> - **D)** Incorreta. Certificados com chaves de 2048 bits com validade de até 3 ou 5 anos geradas e armazenadas diretamente em hardware criptográfico referem-se aos tipos A3 e A4.
> - **E)** Incorreta. A geração interna de chaves diretamente dentro do hardware criptográfico é requisito exclusivo dos certificados do tipo A3 e A4.
>
> **Gabarito: B**

---

## 5. Assinatura Digital e Validade Jurídica

### 5.1 Mecânica Operacional Passo a Passo (Geração e Verificação)

A assinatura digital baseia-se na conjugação entre **funções hash criptográficas** e **criptografia assimétrica**. Ela vincula de forma matemática irrefutável o conteúdo do documento ao titular do certificado.

```mermaid
sequenceDiagram
    autonumber
    actor Alice as Remetente (Alice)
    actor Bob as Destinatário (Bob)
    Note over Alice: 1. Gera Resumo Hash do Documento original: H = SHA256(Doc)
    Note over Alice: 2. Cifra o Hash com sua CHAVE PRIVADA: Assinatura = RSA_Priv(H)
    Alice->>Bob: 3. Transmite [Documento em texto plano + Assinatura Digital + Certificado Digital X.509]
    Note over Bob: 4. Extrai a CHAVE PÚBLICA de Alice contida no Certificado Digital
    Note over Bob: 5. Decifra a Assinatura usando a CHAVE PÚBLICA de Alice: H_original = RSA_Pub(Assinatura)
    Note over Bob: 6. Recalcula o Hash do documento recebido: H_calculado = SHA256(Doc)
    Note over Bob: 7. Compara: Se H_original == H_calculado -> Assinatura é ÍNTEGRA e AUTÊNTICA!
```

#### Passo a Passo da Geração da Assinatura (Alice):
1. Alice calcula o resumo criptográfico (hash) da mensagem utilizando um algoritmo seguro (ex.: SHA-256).
2. Alice cifra esse valor de hash utilizando a sua **própria Chave PRIVADA**. O resultado dessa operação é a **Assinatura Digital**.
3. Alice transmite ao destinatário a mensagem em texto claro acompanhada da Assinatura Digital e do seu Certificado Digital X.509 (que contém a sua Chave Pública).

#### Passo a Passo da Verificação da Assinatura (Bob):
1. Bob recebe o documento, a assinatura e o certificado digital de Alice.
2. Bob utiliza a **Chave PÚBLICA de Alice** (obtida no certificado) para decifrar a assinatura digital, recuperando o valor original do hash calculado por Alice ($H_{original}$).
3. Bob calcula de forma independente um novo hash diretamente sobre o arquivo recebido utilizando a mesma função hash ($H_{calculado}$).
4. Bob compara os dois valores: se $H_{original} == H_{calculado}$, a assinatura é válida; caso haja qualquer discrepância de 1 bit sequer, a assinatura é sumariamente rejeitada.

### 5.2 Propriedades Garantidas vs. Ausência de Confidencialidade

A assinatura digital provê formalmente as seguintes propriedades:

- **Autenticidade:** Garantia incontestável da autoria do documento, vinculando-o ao titular da chave privada.
- **Integridade:** Certeza de que o documento não sofreu nenhuma modificação, corrupção ou inserção após o instante em que foi assinado.
- **Não Repúdio (Irretratabilidade):** O autor da assinatura não pode negar perante autoridades legais ou judiciais a autoria do ato praticado com sua chave privada exclusiva.
- **Validade Jurídica Plena:** No Brasil, o art. 10 da MP 2.200-2/2001 confere aos documentos eletrônicos assinados no âmbito da ICP-Brasil a **presunção legal de veracidade e equivalência a documentos públicos com assinatura física reconhecida em cartório**.

> 🚨 **ALERTA DE PROVA / PEGADINHA FCC:**  
> A assinatura digital **NÃO GARANTE CONFIDENCIALIDADE!** Por padrão, o documento assinado transita legível em texto claro e pode ser lido por qualquer operador de rede ou intermediário. Se a questão de concurso afirmar que "ao assinar digitalmente um documento, o remetente impede que indivíduos não autorizados leiam o seu teor", a afirmativa está **INCORRETA**. Para obter confidencialidade juntamente com assinatura digital, é indispensável cifrar o documento com a **chave pública do destinatário**.

### 5.3 Padrões de Assinatura Avançada (CAdES, XAdES, PAdES) e Carimbo do Tempo

Para uniformizar a aplicação de assinaturas digitais em formatos padronizados, a ICP-Brasil e os órgãos de controle adotam as normas internacionais de Assinatura Eletrônica Avançada:

- **CAdES (*CMS Advanced Electronic Signatures*):** Padrão binário estruturado sobre a RFC 5652 (CMS). É agnóstico quanto ao tipo de mídia e permite assinar qualquer tipo de arquivo bruto (imagens, áudio, vídeos, binários executáveis).
- **XAdES (*XML Advanced Electronic Signatures*):** Estruturado sobre as especificações XMLDSig do W3C. Permite a assinatura de documentos no formato XML, oferecendo grande granularidade (é possível assinar nós ou seções individuais do arquivo XML, mantendo a legibilidade estrutural do XML).
- **PAdES (*PDF Advanced Electronic Signatures*):** Desenvolvido especificamente para arquivos no formato **PDF** (ISO 32000-1). A assinatura digital, a cadeia de certificação e os metadados de auditoria são incorporados diretamente na estrutura interna do arquivo `.pdf`, permitindo visualização gráfica e conferência direta em leitores de PDF convencionais.
- **Carimbo do Tempo (*Timestamp*):** Atestado digital emitido por uma Autoridade de Carimbo do Tempo (ACT) credenciada pela ICP-Brasil, sincronizada com o relógio atômico do Observatório Nacional. Prova com fé pública que determinado documento e sua respectiva assinatura digital já existiam e eram válidos em uma data e hora específicas no passado, resguardando a validade jurídica mesmo após o certificado do autor ter expirado anos mais tarde.

---

### Teste 375
**(FGV – TCE-PA – Auditor de Controle Externo (TI) – 2024)**  
O TCE -PA está implementando um sistema de assinatura digital para garantir a autenticidade e integridade dos documentos eletrônicos que serão enviados e recebidos pelos seus sistemas. Para assegurar que a chave pública do emissor esteja corretamente associada à sua identidade, o tribunal deve utilizar um

* **A)** algoritmo de hashing.
* **B)** certificado digital.
* **C)** sistema de criptografia simétrica.
* **D)** protocolo SSL/TLS.
* **E)** firewall.

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Funções de hash (resumo criptográfico) garantem a integridade da mensagem ao gerar uma digest de tamanho fixo, mas não vinculam a chave pública à identidade do signatário.
> - **B)** Correta. O certificado digital (padrão X.509) é o instrumento emitido por uma Autoridade Certificadora (AC) que associa de forma inequívoca e matematicamente verificável a chave pública a uma identidade (pessoa física, jurídica ou servidor público), garantindo autenticidade e validade jurídica.
> - **C)** Incorreta. A criptografia simétrica utiliza uma única chave compartilhada, não resolvendo o problema de comprovação pública de autoria.
> - **D)** Incorreta. O SSL/TLS é um protocolo de comunicação em trânsito que utiliza certificados digitais em seu handshake, mas não se confunde com o artefato de identidade em si.
> - **E)** Incorreta. Firewall é dispositivo de controle de fluxo de rede perimetral.
>
> **Gabarito: B**

---

### Teste 376
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**
Em processos de fiscalização e auditoria eletrônica de longo prazo, documentos digitais assinados devem manter sua auditabilidade e validade probatória ao longo de décadas, superando a eventual expiração de certificados ou descontinuação de algoritmos criptográficos.

Para atender a esses requisitos de preservação de longo prazo no ecossistema da ICP-Brasil, a tecnologia que atesta a data e hora oficiais brasileiras fornecidas pelo Observatório Nacional e os formatos de assinatura avançada recomendados para preservação temporal são:

* **A)** O protocolo Telnet em conjunto com o formato TXT simples sem chaves.
* **B)** A Autoridade de Carimbo do Tempo (ACT), que emite carimbos do tempo criptográficos atestando tempestividade de forma juridicamente válida; e os perfis de assinatura digital avançada de longo prazo **CAdES**, **XAdES** e **PAdES** (com extensões para preservação histórica, como CAdES-A e PAdES-LTV).
* **C)** A gravação do relógio local do sistema operacional do computador do auditor no rodapé do documento em fonte Arial.
* **D)** O formato DOC sem criptografia assinado via botão de macro do Microsoft Word 97.
* **E)** O carimbo do tempo é emitido exclusivamente pela operadora local de telefonia móvel sem uso de criptografia assimétrica. considerando os requisitos operacionais de segurança, escalabilidade e desempenho.


---

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

## 6. Fontes Recomendadas na Internet

#### 1. Legislação Oficial e Documentos Governamentais
- [Estrutura da ICP-Brasil e Legislação (ITI / Gov.br)](https://www.gov.br/iti/pt-br/assuntos/icp-brasil): Portal oficial do Instituto Nacional de Tecnologia da Informação detalhando a hierarquia da cadeia de certificação brasileira, o papel da AC-Raiz, normas de credenciamento de ACs e ARs e padrões de assinatura digital.
- [Medida Provisória nº 2.200-2/2001 (Planalto)](https://www.planalto.gov.br/ccivil_03/mpv/antigas_2001/2200-2.htm): Diploma legal basilar que instituiu a ICP-Brasil, garantindo a presunção legal de veracidade aos documentos eletrônicos assinados com certificados digitais emitidos no âmbito da infraestrutura nacional.
- [Lei nº 14.063/2020 — Assinaturas Eletrônicas no Setor Público (Planalto)](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2020/lei/l14063.htm): Marco legal que dispõe sobre o uso de assinaturas eletrônicas (simples, avançada e qualificada via ICP-Brasil) em interações com entes públicos.

#### 2. Padrões Técnicos Internacionais
- [RFC 5280 - Internet X.509 Public Key Infrastructure Certificate Profile](https://datatracker.ietf.org/doc/html/rfc5280): Especificação técnica formal dos campos do certificado X.509 v3, listas de certificados revogados (LCR / CRL) e caminhos de certificação.
- [NIST SP 800-38D - Recommendation for Block Cipher Modes of Operation: GCM](https://csrc.nist.gov/publications/detail/sp/800-38d/final): Padrão de especificação formal do modo Galois/Counter Mode (GCM) para criptografia autenticada (AEAD).

#### 3. Referências Bibliográficas Clássicas (Padrão ABNT)
* STALLINGS, William. **Criptografia e Segurança de Redes: Princípios e Práticas**. 6. ed. São Paulo: Pearson Education do Brasil, 2015. (Cap. 3, 6, 9, 11 e 14 — Cifras Simétricas AES/Modos de Operação, Criptografia Assimétrica RSA/ECC, Funções Hash SHA e Certificados X.509).
* PAAR, Christof; PELZL, Jan. **Understanding Cryptography: A Textbook for Students and Practitioners**. Berlin: Springer, 2010. (Cap. 4, 7, 11 e 12 — Advanced Encryption Standard, RSA, Hash Functions e Digital Signatures).
* MENEZES, Alfred J.; VAN OORSCHOT, Paul C.; VANSTONE, Scott A. **Handbook of Applied Cryptography**. Boca Raton: CRC Press, 1996. (Cap. 7 a 13 — Block Ciphers, Public-Key Encryption, Hash Functions, Digital Signatures e Key Management).
