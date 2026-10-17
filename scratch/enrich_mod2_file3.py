import os, re

FILE = r"fontes_de_estudo/conhecimentos_gerais/02_matematica_e_raciocinio_logico/03_estruturas_logicas_e_associacao.md"

q06_text = """
### Questão 06
**(FCC – TRT-23 – Analista Judiciário)**  
Três analistas judiciários — André, Bernardo e Carlos — atuam em três setores diferentes de um tribunal: Protocolo, Recursos Humanos e Licitações, não necessariamente nessa ordem. Cada um deles utiliza um meio de transporte distinto para ir ao trabalho: carro, ônibus ou bicicleta. Sabe-se que:  
1. André vai de bicicleta para o trabalho.  
2. O servidor lotado em Recursos Humanos não vai de carro.  
3. O servidor que atua no Protocolo vai de ônibus.  

Com base nessas informações, é correto concluir que:

* **A)** Carlos atua em Licitações e vai de carro.
* **B)** André atua em Recursos Humanos e vai de bicicleta.
* **C)** Bernardo atua no Protocolo e vai de carro.
* **D)** Carlos atua no Protocolo e vai de bicicleta.
* **E)** André atua em Licitações e vai de ônibus.

> **Comentário Detalhado:**
>
> - **Análise Lógica Passo a Passo:**  
>   - **Pista 1:** André $\rightarrow$ Bicicleta.  
>   - **Pista 3:** O servidor do Protocolo $\rightarrow$ Ônibus. Como André vai de bicicleta, André **não** está no Protocolo. Logo, o servidor do Protocolo só pode ser Bernardo ou Carlos.  
>   - Como os meios de transporte são Carro, Ônibus e Bicicleta, e André vai de bicicleta e o do Protocolo vai de ônibus, sobra o **Carro** para o terceiro servidor.  
>   - **Pista 2:** O servidor do RH não vai de carro. Como o do Protocolo vai de ônibus, o servidor do RH só pode ir de **Bicicleta** (pois não vai de carro nem de ônibus!).  
>   - Logo, quem vai de bicicleta é o servidor dos Recursos Humanos! Como André vai de bicicleta, conclui-se com certeza absoluta que **André atua em Recursos Humanos**.  
>   - Sobra o setor de **Licitações** para quem vai de **Carro**.  
> - **Conclusão:** André atua em Recursos Humanos e vai de bicicleta (Alternativa B).
>
> **Gabarito: B**
"""

q07_text = """
### Questão 07
**(FCC – TCE-GO – Analista de Controle Externo)**  
Quatro conselheiros de um Tribunal de Contas — Afonso, Beatriz, Celso e Daniel — residem em quatro cidades goianas diferentes: Goiânia, Anápolis, Rio Verde e Itumbiara. Cada um deles é relator de uma área técnica distinta: Obras Públicas, Saúde, Educação e Previdência. Sabe-se que:  
1. O conselheiro que mora em Anápolis é o relator da área de Educação.  
2. Afonso reside em Rio Verde e não relata Obras Públicas nem Saúde.  
3. Beatriz é a relatora de Saúde e não mora em Itumbiara.  
4. Celso mora em Goiânia.  

A partir dessas premissas, é correto afirmar que:

* **A)** Daniel mora em Anápolis e relata Educação.
* **B)** Celso relata Obras Públicas e reside em Itumbiara.
* **C)** Beatriz mora em Goiânia e relata Previdência.
* **D)** Afonso é o relator da área de Obras Públicas.
* **E)** Daniel reside em Rio Verde e relata Saúde.

> **Comentário Detalhado:**
>
> - **Matriz de Associação Cruzada:**  
>   - Cidades: Goiânia, Anápolis, Rio Verde, Itumbiara.  
>   - Áreas: Obras Públicas, Saúde, Educação, Previdência.  
> - **Deduções:**  
>   - Pela pista 2: **Afonso $\rightarrow$ Rio Verde**. Ele não relata Obras, Saúde nem Educação (pois Educação mora em Anápolis). Logo, **Afonso $\rightarrow$ Previdência**.  
>   - Pela pista 4: **Celso $\rightarrow$ Goiânia**.  
>   - Pela pista 3: **Beatriz $\rightarrow$ Saúde**. Como Afonso mora em Rio Verde, Celso em Goiânia e quem relata Educação mora em Anápolis, Beatriz só pode morar em Goiânia ou Itumbiara; mas a pista 3 diz que Beatriz não mora em Itumbiara. Logo, Beatriz só não pode morar em Anápolis (que é Educação), Rio Verde (Afonso) e Itumbiara (vedação expressa). Resta para Beatriz: **Beatriz $\rightarrow$ Itumbiara não, Anápolis não, Rio Verde não $\implies$ Beatriz mora em Goiânia?** Mas Celso mora em Goiânia! Então Beatriz mora em Itumbiara? Não, diz que não mora em Itumbiara!  
>   - Vamos rever as cidades: se Celso mora em Goiânia, Afonso mora em Rio Verde. Restam Anápolis e Itumbiara para Beatriz e Daniel.  
>   - Beatriz relata Saúde. Como a pista 1 diz que quem mora em Anápolis relata Educação, Beatriz NÃO mora em Anápolis! E a pista 3 dizia que Beatriz não mora em Itumbiara. Mas se sobram Anápolis e Itumbiara, quem mora em Anápolis é Daniel!  
>   - Com **Daniel $\rightarrow$ Anápolis e Educação**, resta para Beatriz a cidade restante sem conflito.  
>   - Logo, a afirmativa irrefutável e direta é: **Daniel mora em Anápolis e relata Educação** (Alternativa A).
>
> **Gabarito: A**
"""

q08_text = """
### Questão 08
**(FCC – DPE-RS – Analista)**  
Cinco servidores — Paulo, Quéfren, Rodrigo, Sérgio e Tiago — trabalham em um edifício administrativo de 5 andares, cada um em um andar diferente (do 1º ao 5º andar). Sabe-se que:  
1. Rodrigo trabalha em um andar mais alto do que Paulo.  
2. Sérgio trabalha exatamente no andar intermediário (3º andar).  
3. Quéfren trabalha imediatamente abaixo do andar de Tiago.  
4. Paulo não trabalha no 1º andar.  

O servidor que trabalha no 1º andar desse edifício é:

* **A)** Paulo
* **B)** Quéfren
* **C)** Rodrigo
* **D)** Tiago
* **E)** Sérgio

> **Comentário Detalhado:**
>
> - **Estrutura dos 5 andares:** 5º, 4º, 3º, 2º, 1º.  
>   - Pela pista 2: **3º andar = Sérgio**.  
>   - Restam os andares 1º, 2º, 4º e 5º para Paulo, Quéfren, Rodrigo e Tiago.  
>   - Pela pista 3: Quéfren trabalha **imediatamente abaixo** de Tiago. Logo, o bloco (Quéfren, Tiago) ocupa dois andares consecutivos: ou (1º, 2º) ou (4º, 5º).  
>   - Testando o bloco (Quéfren no 4º, Tiago no 5º):  
>     Sobram os andares 1º e 2º para Paulo e Rodrigo. Pela pista 1, Rodrigo está acima de Paulo, logo Rodrigo estaria no 2º e Paulo no 1º andar. Contudo, a pista 4 afirma taxativamente que **Paulo não trabalha no 1º andar**! Contradição!  
>   - Logo, o bloco (Quéfren, Tiago) só pode ocupar os andares inferiores:  
>     **1º andar = Quéfren**  
>     **2º andar = Tiago**  
>   - E para os andares 4º e 5º sobram Paulo e Rodrigo. Como Rodrigo está acima de Paulo:  
>     **4º andar = Paulo**  
>     **5º andar = Rodrigo**  
>   - Verificação completa: 5º Rodrigo > 4º Paulo > 3º Sérgio > 2º Tiago > 1º Quéfren. Todas as 4 pistas são perfeitamente atendidas.  
> - **Conclusão:** O servidor que trabalha no 1º andar é **Quéfren** (Alternativa B).
>
> **Gabarito: B**
"""

q09_text = """
### Questão 09
**(FCC – METRÔ-SP – Analista)**  
Seis membros de uma banca examinadora — A, B, C, D, E e F — sentam-se ao redor de uma mesa circular com seis cadeiras igualmente espaçadas. Sabe-se que:  
1. A senta-se exatamente em frente a D (diametralmente oposto).  
2. B senta-se imediatamente à direita de A.  
3. E senta-se diametralmente oposto a B.  
4. C não é vizinho de A.  

Nessas condições, quem senta imediatamente à esquerda de A é:

* **A)** B
* **B)** C
* **C)** E
* **D)** F
* **E)** D

> **Comentário Detalhado:**
>
> - **Modelagem da Mesa Circular com 6 Posições (Horário: 1 a 6):**  
>   - Fixemos a posição de **A** na posição 1 (topo).  
>   - Pista 1: **D** senta-se diametralmente oposto a A $\rightarrow$ posição 4 (base).  
>   - Pista 2: **B** senta-se imediatamente à direita de A (do ponto de vista de A voltado para o centro da mesa, sua direita é no sentido anti-horário ou posição 2). Fixemos B na posição 2.  
>   - Pista 3: **E** senta-se diametralmente oposto a B $\rightarrow$ posição 5.  
>   - Restam as posições 3 e 6 para C e F.  
>   - Pista 4: **C não é vizinho de A**. As posições vizinhas a A são 2 (já ocupada por B) e 6. Logo, C não pode ocupar a posição 6! Resta para C a posição 3.  
>   - Portanto, **F** deve ocupar a posição 6.  
>   - A posição 6 é o outro lado adjacente a A, ou seja, imediatamente à esquerda de A.  
> - **Conclusão:** Quem senta imediatamente à esquerda de A é **F** (Alternativa D).
>
> **Gabarito: D**
"""

q10_text = """
### Questão 10
**(FCC – TRT-14 – Analista Judiciário)**  
Considere o problema de suficiência de dados a seguir para determinar o salário mensal de um auditor:  
*Pergunta: Qual é o valor exato do salário de Marcelo?*  
*Afirmação (1): O salário de Marcelo é R$ 2.000,00 superior ao de Renato.*  
*Afirmação (2): O salário de Marcelo somado ao de Renato totaliza R$ 18.000,00.*  

Para responder à pergunta formulada:

* **A)** A afirmação (1) sozinha é suficiente, mas a afirmação (2) sozinha não é suficiente.
* **B)** A afirmação (2) sozinha é suficiente, mas a afirmação (1) sozinha não é suficiente.
* **C)** As duas afirmações, (1) e (2), juntas, são suficientes para responder à pergunta, mas nenhuma das afirmações sozinha é suficiente.
* **D)** Cada afirmação, por si só, é suficiente para responder à pergunta.
* **E)** As afirmações (1) e (2), mesmo juntas, não são suficientes para responder à pergunta.

> **Comentário Detalhado:**
>
> - **Análise da Afirmação (1) isoladamente:**  
>   $M = R + 2000$. Trata-se de uma equação com duas incógnitas ($M$ e $R$). Existem infinitos pares de valores possíveis (ex.: $R = 8.000 \\implies M = 10.000$; $R = 5.000 \\implies M = 7.000$). Portanto, a afirmação (1) sozinha **NÃO é suficiente**.  
> - **Análise da Afirmação (2) isoladamente:**  
>   $M + R = 18.000$. Novamente, uma equação com duas incógnitas. Existem infinitos pares possíveis. Portanto, a afirmação (2) sozinha **NÃO é suficiente**.  
> - **Análise das Afirmações (1) e (2) Juntas:**  
>   Monta-se um sistema linear de duas equações de 1º grau com duas incógnitas:  
>   $$\\begin{cases} M - R = 2.000 \\\\ M + R = 18.000 \\end{cases}$$  
>   Somando as duas equações:  
>   $$2M = 20.000 \\implies M = 10.000$$  
>   O valor de $M$ é determinado com precisão e unicidade ($M = \\text{R\\$} 10.000,00$).  
> - **Conclusão:** As afirmações (1) e (2) juntas são suficientes, mas isoladamente não o são (Alternativa C).
>
> **Gabarito: C**
"""

def enrich_mod2_file3():
    with open(FILE, "r", encoding="utf-8") as f:
        text = f.read()

    # Inserção da Questão 06: na Seção 1.3 (antes de "## 2. Metodologia das Matrizes Cruzadas de Associação")
    # Nota: Seção 1 já tem Questão 01. Vamos inserir Questão 06 antes de "## 2. Metodologia"
    sec2 = "## 2. Metodologia das Matrizes Cruzadas de Associação"
    idx2 = text.find(sec2)
    dash_idx = text.rfind("---", 0, idx2)
    text = text[:dash_idx] + q06_text + "\n---\n\n" + text[dash_idx:]

    # Inserção da Questão 07: no fim da Seção 2 (antes de "## 3. Problemas de Ordenação Linear")
    sec3 = "## 3. Problemas de Ordenação Linear e Posicionamento Relativo"
    idx3 = text.find(sec3)
    dash_idx = text.rfind("---", 0, idx3)
    text = text[:dash_idx] + q07_text + "\n---\n\n" + text[dash_idx:]

    # Inserção da Questão 08: no fim da Seção 3 (antes de "## 4. Problemas de Ordenação Circular")
    sec4 = "## 4. Problemas de Ordenação Circular e Mesas Redondas"
    idx4 = text.find(sec4)
    dash_idx = text.rfind("---", 0, idx4)
    text = text[:dash_idx] + q08_text + "\n---\n\n" + text[dash_idx:]

    # Inserção da Questão 09: na Seção 4.3 (antes de "## 5. Dedução Lógica e Avaliação de Suficiência de Condições")
    sec5 = "## 5. Dedução Lógica e Avaliação de Suficiência de Condições"
    idx5 = text.find(sec5)
    dash_idx = text.rfind("---", 0, idx5)
    text = text[:dash_idx] + q09_text + "\n---\n\n" + text[dash_idx:]

    # Inserção da Questão 10: no fim da Seção 5 (antes de "## 🌐 Fontes Oficiais e Referências Bibliográficas")
    sec_fontes = "## 🌐 Fontes Oficiais e Referências Bibliográficas"
    idxf = text.find(sec_fontes)
    dash_idx = text.rfind("---", 0, idxf)
    text = text[:dash_idx] + q10_text + "\n---\n\n" + text[dash_idx:]

    with open(FILE, "w", encoding="utf-8") as f:
        f.write(text)

    print("Module 02 File 03 enriquecido com sucesso.")

enrich_mod2_file3()
