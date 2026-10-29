# -*- coding: utf-8 -*-
import json
import re

# Carregar banco de questoes
with open('banco_questoes_extraidas.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

questoes_dict = {q['id']: q for q in db['questoes']}

# Texto de apoio da prova TRT-1 2014 FCC
TEXTO_TRT1_2014 = """*Atenção: As questões a seguir referem-se ao texto abaixo:*

> **Os direitos “nossos” e os “deles”**  
>  
> Não é incomum que julguemos o que chamamos “nossos” direitos superiores aos direitos do “outro”. Tanto no nível mais pessoal das relações como nos fatos sociais costuma ocorrer essa discrepância, com as consequências de sempre: soluções injustas.  
> Durante um júri, em que defendia um escravo que havia matado o seu senhor, Luís Gama (1830 - 1882), advogado, jornalista e escritor mestiço, abolicionista que chegou a ser escravo por alguns anos, proferiu uma frase que se tornou célebre, numa sessão de julgamento: "O escravo que mata o senhor, seja em que circunstância for, mata sempre em legítima defesa". A frase causou tumulto e acabou por suspender a sessão do júri, despertando tremenda polêmica à época. Na verdade, continua provocando.  
> Dissesse alguém isso hoje, em alguma circunstância análoga, seria aplaudido por uns e acusado por outros de demonizar o “proprietário”. Como se vê, também a demonização tem duas mãos: os partidários de quem subjuga acabam por demonizar a reação do subjugado. Tais fatos e tais polêmicas, sobre tais direitos, nem deveriam existir, mas existem; será que terão fim?  
> O grande pensador e militante italiano Antonio Gramsci (1891-1937), que passou muitos anos na prisão por conta de suas ideias socialistas, propunha, em algum lugar de sua obra, que diante do dilema de uma escolha nossa conduta subsequente deve se reger pela avaliação objetiva das circunstâncias para então responder à seguinte pergunta: “Quem sofre?” Para Gramsci, o sofrimento humano é um parâmetro que não se pode perder de vista na avaliação das decisões pessoais ou políticas.  
> *(Abelardo Trancoso, inédito)*"""

# Mapeamento dos 11 testes
replacement_data = [
    {
        "test_num": "001",
        "qid": "TRT1-2014-FCC-Q01",
        "header": "**(FCC – TRT-1 – Analista Judiciário (TI) – 2014)**",
        "prefix_text": TEXTO_TRT1_2014 + "\n\n",
        "comments": {
            "A": "Incorreta. O item III está incorreto, pois Gramsci não propõe um apego cego e formalista ao 'cumprimento rigoroso da lei', mas sim a avaliação do 'sofrimento humano' diante das circunstâncias objetivas.",
            "B": "Correta. O item I é verdadeiro: o 1º parágrafo apresenta a tese da discrepância entre 'nossos' direitos e os direitos do 'outro', ilustrada no 2º parágrafo com o episódio histórico de Luís Gama. O item II também é verdadeiro: a contundência da frase de Luís Gama em pleno regime escravocrata explica o tumulto e a polêmica gerados.",
            "C": "Incorreta. O item I está plenamente correto na estruturação do texto, não podendo ser descartado.",
            "D": "Incorreta. O item III é falso (Gramsci prioriza o sofrimento humano, não o rigor legalista) e o item I é verdadeiro.",
            "E": "Incorreta. O item II está correto e o item III é incorreto."
        }
    },
    {
        "test_num": "002",
        "qid": "TRT1-2014-FCC-Q02",
        "header": "**(FCC – TRT-1 – Analista Judiciário (TI) – 2014)**",
        "prefix_text": "",
        "comments": {
            "A": "Incorreta. A expressão não se refere à desproporção da reação, mas ao fato de que ambos os lados se acusam mutuamente de injustiça.",
            "B": "Incorreta. Não se trata da violência aproveitando-se da fragilidade, mas da dinâmica de julgamento moral recíproco.",
            "C": "Incorreta. O texto não absolve de culpa ambas as partes; trata da demonização mútua que ocorre no debate ideológico e social.",
            "D": "Correta. 'A demonização tem duas mãos' sintetiza o raciocínio explicitado na sequência: 'os partidários de quem subjuga acabam por demonizar a reação do subjugado', isto é, tanto o subjugado quanto quem subjuga são censurados e julgados por atos considerados intoleráveis pelo outro polo.",
            "E": "Incorreta. A alternativa insere o juízo 'ainda que não tenham razão para fazê-lo', o que extrapola a análise textual do autor."
        }
    },
    {
        "test_num": "003",
        "qid": "TRT-2024-FCC-Q05",
        "header": "**(FCC – TRT – Analista Judiciário (TI) – 2024)**",
        "prefix_text": "",
        "comments": {
            "A": "Incorreta. As frases não partem todas de um elemento idêntico e repetido estaticamente sem progressão temático-conceitual.",
            "B": "Incorreta. O texto não cria um encadeamento linear em que o rema da frase anterior vira o tema único da seguinte (progressão linear em cadeia).",
            "C": "Correta. A primeira frase estabelece o hipertema geral: a postura conservadora da Corte Suprema em relação aos direitos individuais. As frases seguintes desdobram esse tema decompondo-o em múltiplos elementos ilustrativos (direitos dos prisioneiros, pena de morte, apoio ao governo Reagan em liberdades civis). Trata-se da progressão temática com tema derivado/decomposto.",
            "D": "Incorreta. Não há dois temas contrastantes em análise paralela, mas a desagregação de uma decisão geral da Suprema Corte.",
            "E": "Incorreta. Não existem dois polos temáticos iniciais combinados progressivamente."
        }
    },
    {
        "test_num": "004",
        "qid": "TRT1-2014-FCC-Q03",
        "header": "**(FCC – TRT-1 – Analista Judiciário (TI) – 2014)**",
        "prefix_text": "",
        "comments": {
            "A": "Incorreta. O sofrimento para Gramsci é um parâmetro ético e orientador da conduta, e não um obstáculo impeditivo da ação.",
            "B": "Incorreta. Gramsci não defende abster-se da ação moral, mas agir considerando quem sofre.",
            "C": "Incorreta. A consideração pelo sofrimento alheio é a própria base da escolha ética em Gramsci, e não uma distorção.",
            "D": "Correta. No último parágrafo, o autor ressalta que para Gramsci a avaliação das circunstâncias objetivas e a pergunta 'Quem sofre?' devem orientar as escolhas políticas e pessoais, estabelecendo o sofrimento humano como parâmetro ético intransigente.",
            "E": "Incorreta. O texto não associa Gramsci à indiferença pragmática nem à renúncia dos princípios em favor de interesses imediatos."
        }
    },
    {
        "test_num": "005",
        "qid": "TRT14-2016-FCC-Q03",
        "header": "**(FCC – TRT-14 – Analista Judiciário (TI) – 2016)**",
        "prefix_text": "",
        "comments": {
            "A": "Incorreta. O excerto não estabelece relação de causa e efeito determinística entre a hipocrisia e os tabus.",
            "B": "Correta. Ao afirmar que 'a hipocrisia existe, mas o aparente exagero tem a ver com a luta da mulher americana para mudar um quadro de pressupostos e tabus tão machistas', o autor pressupõe que as atitudes das mulheres, embora possam soar exageradas aos olhos superficiais, são respostas legítimas a uma estrutura social prévia opressora.",
            "C": "Incorreta. O autor não desqualifica a luta das mulheres como hipócrita; a conjunção adversativa 'mas' contrapõe a existência da hipocrisia geral à legitimidade da luta.",
            "D": "Incorreta. A alternativa restringe indevidamente o escopo da afirmação, ignorando a contextualização cultural apresentada.",
            "E": "Incorreta. Trata-se de extrapolação conceitual que não encontra respaldo no excerto original."
        }
    },
    {
        "test_num": "006",
        "qid": "TRTDA24REGIO-2025-FGV-Q06",
        "header": "**(FGV – TRT-24 – Analista Judiciário (TI) – 2025)**",
        "prefix_text": "",
        "comments": {
            "A": "Correta. O trecho utiliza uma analogia figurada (linguagem conotativa) entre a criação literária do romancista e a navegação do capitão de navio que parte com ordens seladas. A metáfora ilustra o processo criativo no qual o plano inicial do autor pode ser transformado pelo próprio desenrolar da narrativa.",
            "B": "Incorreta. Não se trata de uma afirmação denotativa ou literal sobre náutica ou táticas navais.",
            "C": "Incorreta. A comparação não expressa descontentamento ou censura à conduta militar, mas uma figura ilustrativa da escrita de ficção.",
            "D": "Incorreta. A analogia não nega o planejamento da escrita, mas salienta a maleabilidade da criação literária diante dos rumos do texto.",
            "E": "Incorreta. O foco não é a imprevisibilidade meteorológica, mas a liberdade e descobertas do escritor ao longo de sua criação."
        }
    },
    {
        "test_num": "007",
        "qid": "TRT3-2015-FCC-Q10",
        "header": "**(FCC – TRT-3 – Analista Judiciário (TI) – 2015)**",
        "prefix_text": "*Considere o seguinte trecho para análise:*  \n*\"A primeira pessoa que me falou foi a vizinha: — Agora sim sabemos que o Antônio rompeu o noivado! Chegara ao meu ouvido o rumor daquela fofoca que tinha de ouvir todos os dias.\"*\n\n",
        "comments": {
            "A": "Incorreta. 'Tinha de ouvir' expressa obrigação/necessidade no passado, enquanto 'ouvia' traduz mera habitualidade temporal (pretérito imperfeito simples).",
            "B": "Incorreta. A forma 'chegara' está no pretérito mais-que-perfeito, indicando ação anterior (e não simultânea) ao fato expresso por 'tinha de ouvir'.",
            "C": "Incorreta. Na transposição adequada para o discurso indireto, o tempo verbal deve sofrer a correlação: o presente 'sabemos' transpassa para o imperfeito 'sabiam', e o perfeito 'rompeu' para o mais-que-perfeito 'rompera' (ou 'havia rompido').",
            "D": "Correta. Na variedade padrão e culta da língua prescrita para concursos, vocábulos de registro marcadamente coloquial/informal como 'fofoca' devem ser evitados em redações e análises formais, ainda que o autor os utilize em contexto de narrativa ficcional.",
            "E": "Incorreta. Com a locução 'Uma das primeiras', o verbo pode concordar tanto no singular (enfatizando o núcleo 'uma') quanto no plural (concordando com o termo partitivo no plural)."
        }
    },
    {
        "test_num": "008",
        "qid": "TRT-2025-FGV-Q07",
        "header": "**(FGV – TRT – Analista Judiciário (TI) – 2025)**",
        "prefix_text": "",
        "comments": {
            "A": "Incorreta. No discurso indireto iniciado por verbo no passado ('Ele disse que...'), o advérbio 'amanhã' deve ser transposto para 'no dia seguinte' ou 'no dia posterior', e o futuro do presente deve converter-se em futuro do pretérito.",
            "B": "Incorreta. Mantém incorretamente o advérbio temporal 'amanhã', sem a devida transposição dêitica.",
            "C": "Incorreta. Mantém 'amanhã' e altera a locução verbal para o pretérito imperfeito 'estava saindo', descaracterizando o futuro do pretérito.",
            "D": "Correta. A transposição perfeita do discurso direto para o indireto exige a concordância de todos os dêiticos: o tempo verbal do futuro perifrástico 'estarei saindo' passa ao futuro do pretérito 'estaria saindo'; o advérbio de lugar 'daqui' converte-se em 'de lá'; o advérbio de tempo 'amanhã' transita para 'no dia seguinte'; e o pronome possessivo de 1ª pessoa 'minha irmã' passa para 'sua irmã'.",
            "E": "Incorreta. A introdução desnecessária do pronome reto 'ele' e a troca por 'a irmã dele' criam prolixidade desnecessária diante da forma canônica de transposição com pronome possessivo de terceira pessoa."
        }
    },
    {
        "test_num": "009",
        "qid": "TRT24-2017-FCC-Q04",
        "header": "**(FCC – TRT-24 – Analista Judiciário (TI) – 2017)**",
        "prefix_text": "",
        "comments": {
            "A": "Incorreta. A regência 'impelido de me reportar à quem quer que fosse' comete crase indevida antes de pronome indefinido ('quem').",
            "B": "Incorreta. 'Continuo a sentir-me incomodado ao testemunhar' não preserva com exatidão a nuance estilística de 'ainda sinto desconforto em ver'.",
            "C": "Correta. A substituição proposta mantém plenamente a conformidade com o padrão culto e as relações de sentido originais do texto, operando paráfrase irretocável dos termos essenciais.",
            "D": "Incorreta. 'Porquanto' exprime causa/explicação, ao passo que 'contudo' é conectivo adversativo de oposição, alterando radicalmente o sentido.",
            "E": "Incorreta. Há erro crasso de próclise/ênclise ('já tornamo-nos', pois 'já' atrai próclise: 'já nos tornamos') e omissão indevida da preposição exigida pelo substantivo 'impressão'."
        }
    },
    {
        "test_num": "010",
        "qid": "TRTDA24REGIO-2025-FGV-Q10",
        "header": "**(FGV – TRT-24 – Analista Judiciário (TI) – 2025)**",
        "prefix_text": "",
        "comments": {
            "A": "Incorreta. Trata-se de um texto puramente dissertativo-argumentativo, que discute e teoriza sobre o papel do olhar e da imagem na cultura contemporânea.",
            "B": "Incorreta. Texto de tipologia dissertativa, no qual se defende a tese de que a manifestação pública é basilar para a democracia.",
            "C": "Incorreta. Apresenta caráter informativo/expositivo e noticioso sobre o adiamento de uma reunião, sem estrutura narrativa com progressão de ações e personagens.",
            "D": "Correta. O fragmento estrutura-se com elementos típicos da narração: marco temporal preciso ('Em 1501'), personagem com ação sucessiva no tempo ('Michelangelo volta de viagem a Florença e concentra seu trabalho artístico em um grande bloco de mármore abandonado'), narrando um episódio concreto com transformação de estado.",
            "E": "Incorreta. Frase puramente aforística/dissertativa com juízo de valor sobre o conceito de solidariedade."
        }
    },
    {
        "test_num": "011",
        "qid": "TRT3-2015-FCC-Q02",
        "header": "**(FCC – TRT-3 – Analista Judiciário (TI) – 2015)**",
        "prefix_text": "*Considere o trecho:*  \n*\"A imprensa frequentemente anuncia que o leitor pode apreciar duas opiniões diferentes sobre um mesmo tema polêmico, colocando lado a lado análises que divergem apenas em pormenores cosméticos, mas convergem no alinhamento ideológico com o status quo.\"*\n\n",
        "comments": {
            "A": "Incorreta. As aspas marcam uma citação irônica ou distanciamento crítico, e não o nome da seção do jornal.",
            "B": "Correta. A análise contextual do autor demonstra a ironia na promessa de pluralismo ('o leitor pode apreciar duas opiniões diferentes'), revelando que o arranjo editorial força uma falsa polarização que mascara uma base ideológica idêntica.",
            "C": "Incorreta. A frase em si não denuncia o falso pluralismo diretamente; ela é o mote convencional que o autor ironiza para depois construir sua crítica.",
            "D": "Incorreta. O autor critica esse modelo cosmético, logo ele não o toma como objetivo ideal a ser perseguido por uma linha editorial séria.",
            "E": "Incorreta. O autor não afirma a impossibilidade do pluralismo no Brasil, mas desmascara o pseudopluralismo das análises binárias na imprensa."
        }
    }
]

print("Script de mapeamento preparado com sucesso!")

