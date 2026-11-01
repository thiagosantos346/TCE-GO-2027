# Relatório Oficial de Auditoria Semântica, Rollback Git e Mapeamento de Cobertura
> **Data da Auditoria:** 01/11/2026 | **Escopo:** Concurso TCE-GO 2027 (TI e Técnico-Administrativo)
> **Referência de Rollback Git:** Commit `6a1eac1` (Versão Estável com Questões Simuladas Estilo FCC e Metadados Auditados)
> **Base de Questões Sanitizada:** `banco_questoes_extraidas.json` (3.829 questões oficiais elegíveis após expurgo)

## 1. Sumário Executivo e Diagnóstico de Conformidade
Na auditoria do acervo de testes dos 119 guias de estudo (`fontes_de_estudo/`), detectou-se que a injeção em massa anterior (commit `900cf56`) forçou a substituição irrestrita de questões pedagógicas simuladas por questões do banco sem validação semântica prévia. Isso resultou na invasão de itens totalmente desconexos (como engenharia civil de vigas biapoiadas, dimensionamento de solos, lagoas de tratamento de esgoto, máquinas térmicas e comandos Linux RPM em seções de Inteligência Artificial e Redação Oficial).

### Ações Corretivas Executadas com Tolerância Zero para Preguiça:
1. **Auditoria Semântica 1:1:** Leitura individual dos enunciados e comentários frente à teoria e subseções correspondentes.
2. **Rollback Exclusivo via Git:** Extração direta via `git show 6a1eac1:<arquivo>` dos blocos Markdown originais completos para **1.032 questões intrusas** (incluindo as 1.030 do template genérico e 2 do lote RLM com conflito de enunciado/resolução).
3. **Preservação de Questões Reais Autênticas:** Manutenção de **212 questões reais** rigorosamente aderentes, com justificativas detalhadas alternativa por alternativa da FCC, FGV e Cespe.
4. **Sanitização Implacável do Banco JSON:** Expurgo permanente de **42 questões fora do escopo** de Controle Externo (Engenharia Civil, Rodoviária, Térmica, Ciências Atuariais, Odontologia e Biologia Animal).

### Indicadores Globais do Acervo:

| Métrica | Valor Absoluto | Percentual |
| :--- | :---: | :---: |
| **Total de Arquivos Auditados** | **119** | 100,0% |
| **Total Geral de Testes no Projeto** | **1244** | 100,0% |
| **Questões Reais Autênticas Mantidas (Oficiais)** | **212** | 17.0% |
| **Questões Simuladas Estilo FCC Restauradas (Git)** | **1032** | 83.0% |
| **Questões Desconexas Revertidas** | **1.032** | 83,0% do acervo |
| **Questões Expurgadas do Banco de Dados** | **42** | - |

---

## 2. Visão Consolidada por Módulo Temático

| Módulo Temático | Arquivos | Reais | Simuladas | Total | % Real | Situação de Cobertura |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| `01_lingua_portuguesa` | 7 | 61 | 10 | 71 |  85.9% | 🟢 Alta Cobertura Real |
| `02_matematica_e_raciocinio_logico` | 5 | 14 | 36 | 50 |  28.0% | 🟡 Cobertura Híbrida (Reais + Simuladas FCC) |
| `03_legislacao_institucional` | 6 | 16 | 44 | 60 |  26.7% | 🟡 Cobertura Híbrida (Reais + Simuladas FCC) |
| `04_engenharia_de_software` | 5 | 21 | 32 | 53 |  39.6% | 🟡 Cobertura Híbrida (Reais + Simuladas FCC) |
| `05_desenvolvimento_de_sistemas` | 6 | 0 | 65 | 65 |   0.0% | 🔵 Cobertura Simulada Especializada FCC |
| `06_engenharia_software_ia_e_sistemas_agentivos` | 5 | 0 | 52 | 52 |   0.0% | 🔵 Cobertura Simulada Especializada FCC |
| `07_devops_e_plataforma_de_entrega` | 6 | 0 | 63 | 63 |   0.0% | 🔵 Cobertura Simulada Especializada FCC |
| `08_banco_de_dados` | 6 | 12 | 54 | 66 |  18.2% | 🟡 Cobertura Híbrida (Reais + Simuladas FCC) |
| `09_inteligencia_artificial_e_ciencia_de_dados` | 5 | 1 | 54 | 55 |   1.8% | 🟡 Cobertura Híbrida (Reais + Simuladas FCC) |
| `10_seguranca_da_informacao` | 5 | 20 | 35 | 55 |  36.4% | 🟡 Cobertura Híbrida (Reais + Simuladas FCC) |
| `11_sistemas_operacionais_redes_e_nuvem` | 5 | 18 | 37 | 55 |  32.7% | 🟡 Cobertura Híbrida (Reais + Simuladas FCC) |
| `12_governanca_de_ti` | 5 | 10 | 40 | 50 |  20.0% | 🟡 Cobertura Híbrida (Reais + Simuladas FCC) |
| `13_legislacao_aplicada_a_ti` | 5 | 0 | 50 | 50 |   0.0% | 🔵 Cobertura Simulada Especializada FCC |
| `14_lingua_inglesa_leitura_tecnica` | 3 | 0 | 30 | 30 |   0.0% | 🔵 Cobertura Simulada Especializada FCC |
| `15_nocoes_de_direito_administrativo` | 6 | 9 | 56 | 65 |  13.8% | 🟡 Cobertura Híbrida (Reais + Simuladas FCC) |
| `16_licitacoes_e_contratos_administrativos` | 4 | 2 | 42 | 44 |   4.5% | 🟡 Cobertura Híbrida (Reais + Simuladas FCC) |
| `17_nocoes_de_direito_constitucional` | 5 | 19 | 36 | 55 |  34.5% | 🟡 Cobertura Híbrida (Reais + Simuladas FCC) |
| `18_nocoes_de_controle_externo` | 4 | 9 | 35 | 44 |  20.5% | 🟡 Cobertura Híbrida (Reais + Simuladas FCC) |
| `19_nocoes_de_administracao_financeira_e_orcamentaria` | 5 | 0 | 51 | 51 |   0.0% | 🔵 Cobertura Simulada Especializada FCC |
| `20_contabilidade_aplicada_ao_setor_publico` | 4 | 0 | 40 | 40 |   0.0% | 🔵 Cobertura Simulada Especializada FCC |
| `21_nocoes_de_administracao_publica` | 4 | 0 | 40 | 40 |   0.0% | 🔵 Cobertura Simulada Especializada FCC |
| `22_administracao_geral` | 3 | 0 | 30 | 30 |   0.0% | 🔵 Cobertura Simulada Especializada FCC |
| `23_administracao_estrategica` | 3 | 0 | 30 | 30 |   0.0% | 🔵 Cobertura Simulada Especializada FCC |
| `24_comportamento_organizacional` | 3 | 0 | 30 | 30 |   0.0% | 🔵 Cobertura Simulada Especializada FCC |
| `25_gestao_de_pessoas` | 4 | 0 | 40 | 40 |   0.0% | 🔵 Cobertura Simulada Especializada FCC |

---

## 3. Tópicos com Cobertura Real (Questões Oficiais Validadas)

Abaixo estão listados os arquivos e matérias que possuem questões reais oficiais de bancas examinadoras (FCC, FGV, Cespe), cuja pertinência temática com a teoria do arquivo é total:

### Módulo: `01_lingua_portuguesa` (61 questões reais)
| Arquivo / Subtópico | Reais | Simuladas | Total | Bancas Presentes |
| :--- | :---: | :---: | :---: | :--- |
| `01_compreensao_e_interpretacao_de_texto.md`<br>*01 - Compreensão, Interpretação e Tipologia Textual* | **11** | 0 | 11 | FCC, FGV |
| `02_ortografia_acentuacao_e_formacao_de_palavras.md`<br>*02 - Fonética, Ortografia, Vocabulário e Formação de Palavras* | **10** | 0 | 10 | FCC, FGV |
| `03_morfossintaxe_pronomes_e_verbos.md`<br>*03 - Morfossintaxe, Pronomes e Sistema Verbal* | **10** | 0 | 10 | FCC, FGV |
| `04_sintaxe_coordenacao_subordinacao_conectivos_pontuacao.md`<br>*04 - Sintaxe do Período, Conectivos e Pontuação* | **10** | 0 | 10 | FCC, FGV |
| `05_concordancia_regencia_e_crase.md`<br>*05 - Sintaxe de Relação: Concordância, Regência e Crase* | **10** | 0 | 10 | FCC, FGV |
| `06_redacao_reescrita_e_equivalencia_de_estruturas.md`<br>*06 - Redação: Reescrita, Correção Gramatical e Equivalência de Estruturas* | **10** | 0 | 10 | FCC, FGV |

### Módulo: `02_matematica_e_raciocinio_logico` (14 questões reais)
| Arquivo / Subtópico | Reais | Simuladas | Total | Bancas Presentes |
| :--- | :---: | :---: | :---: | :--- |
| `02_proporcoes_regra_de_tres_e_porcentagem.md`<br>*02 - Grandezas Proporcionais, Regra de Três e Porcentagem* | **4** | 6 | 10 | FCC, FGV |
| `03_estruturas_logicas_e_associacao.md`<br>*03 - Estruturas Lógicas, Associação e Dedução* | **3** | 7 | 10 | FCC, FGV |
| `04_raciocinio_sequencial_temporal_espacial_e_verbal.md`<br>*04 - Raciocínio Sequencial, Temporal, Espacial e Verbal* | **2** | 8 | 10 | FGV |
| `05_logica_de_argumentacao_e_conclusoes_validas.md`<br>*05 - Lógica de Argumentação e Conclusões Válidas* | **5** | 5 | 10 | FCC, FGV |

### Módulo: `03_legislacao_institucional` (16 questões reais)
| Arquivo / Subtópico | Reais | Simuladas | Total | Bancas Presentes |
| :--- | :---: | :---: | :---: | :--- |
| `01_bases_constitucionais_cf88_e_ce_go.md`<br>*01 - Bases Constitucionais do Controle Externo (CF/88 e CE/GO)* | **4** | 6 | 10 | FGV |
| `02_lei_organica_tce_go_lei_16168_2007.md`<br>*02 - Lei Orgânica do TCE-GO (Lei Estadual nº 16.168/2007)* | **5** | 5 | 10 | FGV |
| `03_regimento_interno_tce_go_resolucao_22_2008.md`<br>*03 - Regimento Interno do TCE-GO (Resolução nº 22/2008)* | **2** | 8 | 10 | FGV |
| `04_regime_juridico_servidores_e_pccr_leis_20756_e_15122.md`<br>*04 - Regime Jurídico dos Servidores e PCCR do TCE-GO* | **3** | 7 | 10 | FGV |
| `05_codigo_de_etica_servidores_tce_go.md`<br>*05 - Código de Ética dos Servidores do TCE-GO* | **2** | 8 | 10 | FGV |

### Módulo: `04_engenharia_de_software` (21 questões reais)
| Arquivo / Subtópico | Reais | Simuladas | Total | Bancas Presentes |
| :--- | :---: | :---: | :---: | :--- |
| `01_ciclo_de_vida_e_metodologias_ageis.md`<br>*01 - Ciclo de Vida e Metodologias Ágeis* | **4** | 7 | 11 | FCC, FGV |
| `02_requisitos_historias_de_usuario_uml_e_bpmn.md`<br>*02 - Requisitos, Histórias de Usuário, UML e BPMN* | **8** | 3 | 11 | FCC, FGV |
| `04_padroes_de_projeto_design_patterns.md`<br>*04 - Padrões de Projeto (Design Patterns - GoF)* | **4** | 6 | 10 | FCC |
| `05_qualidade_testes_refatoracao_e_divida_tecnica.md`<br>*05 - Qualidade, Testes, Refatoração e Dívida Técnica* | **5** | 6 | 11 | FCC |

### Módulo: `08_banco_de_dados` (12 questões reais)
| Arquivo / Subtópico | Reais | Simuladas | Total | Bancas Presentes |
| :--- | :---: | :---: | :---: | :--- |
| `01_modelagem_de_dados_mer_e_normalizacao.md`<br>*01 - Modelagem de Dados, MER e Normalização* | **6** | 5 | 11 | FCC, FGV |
| `02_linguagem_sql_ddl_dml_dql_tcl_e_dcl.md`<br>*02 - Linguagem SQL e Objetos de Banco* | **6** | 5 | 11 | FCC, FGV |

### Módulo: `09_inteligencia_artificial_e_ciencia_de_dados` (1 questões reais)
| Arquivo / Subtópico | Reais | Simuladas | Total | Bancas Presentes |
| :--- | :---: | :---: | :---: | :--- |
| `01_fundamentos_ia_machine_learning_e_deep_learning.md`<br>*01 - Fundamentos de IA, Machine Learning e Deep Learning* | **1** | 10 | 11 | FGV |

### Módulo: `10_seguranca_da_informacao` (20 questões reais)
| Arquivo / Subtópico | Reais | Simuladas | Total | Bancas Presentes |
| :--- | :---: | :---: | :---: | :--- |
| `01_principios_gestao_de_riscos_e_normas_iso_27000.md`<br>*01 - Princípios, Gestão de Riscos e Normas ISO/IEC 27000* | **3** | 8 | 11 | FCC |
| `02_criptografia_icp_brasil_e_assinatura_digital.md`<br>*02 - Criptografia, ICP-Brasil e Assinatura Digital* | **5** | 6 | 11 | FCC, FGV |
| `03_controle_de_acesso_iam_e_arquitetura_zero_trust.md`<br>*03 - Controle de Acesso, IAM e Arquitetura Zero Trust* | **2** | 9 | 11 | FCC, FGV |
| `04_seguranca_em_aplicacoes_owasp_top_10_e_devsecops.md`<br>*04 - Segurança em Aplicações, OWASP Top 10 e DevSecOps* | **3** | 8 | 11 | FCC, FGV |
| `05_ameacas_malware_engenharia_social_e_defesa_de_redes.md`<br>*05 - Ameaças, Malware, Engenharia Social e Defesa de Redes* | **7** | 4 | 11 | FCC, FGV |

### Módulo: `11_sistemas_operacionais_redes_e_nuvem` (18 questões reais)
| Arquivo / Subtópico | Reais | Simuladas | Total | Bancas Presentes |
| :--- | :---: | :---: | :---: | :--- |
| `01_sistemas_operacionais_linux_e_windows.md`<br>*01 - Sistemas Operacionais: Linux e Windows* | **4** | 7 | 11 | FCC, FGV |
| `02_servicos_de_diretorio_active_directory_e_ldap.md`<br>*02 - Serviços de Diretório: Active Directory e LDAP* | **3** | 8 | 11 | FCC, FGV |
| `03_redes_tcp_ip_enderecamento_ipv4_ipv6_dns_dhcp.md`<br>*03 - Redes TCP/IP, Endereçamento IPv4/IPv6, DNS e DHCP* | **4** | 7 | 11 | FGV |
| `04_protocolos_de_aplicacao_redes_sem_fio_e_seguranca_de_rede.md`<br>*04 - Protocolos de Aplicação, Segurança de Rede e Redes Sem Fio* | **4** | 7 | 11 | FCC, FGV |
| `05_computacao_em_nuvem_modelos_serverless_e_hibridos.md`<br>*05 - Computação em Nuvem, Serverless e Ambientes Híbridos* | **3** | 8 | 11 | FCC, FGV |

### Módulo: `12_governanca_de_ti` (10 questões reais)
| Arquivo / Subtópico | Reais | Simuladas | Total | Bancas Presentes |
| :--- | :---: | :---: | :---: | :--- |
| `01_fundamentos_governanca_cobit_2019_e_iso_38500.md`<br>*01 - Fundamentos de Governança, COBIT 2019 e ISO/IEC 38500:2024* | **3** | 7 | 10 | FGV |
| `02_gestao_de_servicos_de_ti_itil_v4.md`<br>*02 - Gestão de Serviços de TI e Práticas da ITIL v4* | **2** | 8 | 10 | FGV |
| `03_gestao_de_projetos_pmbok_8_edicao_e_metodos_ageis.md`<br>*03 - Gestão de Projetos: PMBOK 8ª Edição e Métodos Ágeis* | **2** | 8 | 10 | FCC |
| `04_contratacoes_de_tic_lei_14133_2021.md`<br>*04 - Contratações de Soluções de TIC na Lei nº 14.133/2021* | **3** | 7 | 10 | FGV |

### Módulo: `15_nocoes_de_direito_administrativo` (9 questões reais)
| Arquivo / Subtópico | Reais | Simuladas | Total | Bancas Presentes |
| :--- | :---: | :---: | :---: | :--- |
| `01_regime_juridico_principios_e_lindb.md`<br>*01 - Regime Jurídico Administrativo, Princípios e LINDB* | **4** | 7 | 11 | FCC, FGV |
| `02_organizacao_administrativa_e_poderes.md`<br>*02 - Organização Administrativa, Poderes e Abuso de Autoridade* | **3** | 8 | 11 | FGV |
| `03_atos_administrativos_e_processo_estadual.md`<br>*03 - Atos Administrativos e Processo Administrativo Estadual (Lei 13.800/2001)* | **1** | 10 | 11 | FGV |
| `04_servicos_publicos_bens_e_responsabilidade_civil.md`<br>*04 - Serviços Públicos, Bens Públicos e Responsabilidade Civil do Estado* | **1** | 10 | 11 | FGV |

### Módulo: `16_licitacoes_e_contratos_administrativos` (2 questões reais)
| Arquivo / Subtópico | Reais | Simuladas | Total | Bancas Presentes |
| :--- | :---: | :---: | :---: | :--- |
| `04_contratos_administrativos_fiscalizacao_alteracoes_e_sancoes.md`<br>*04 - Contratos Administrativos: Execução, Alterações, Equilíbrio e Sanções (Lei 14.133/2021)* | **2** | 9 | 11 | FGV |

### Módulo: `17_nocoes_de_direito_constitucional` (19 questões reais)
| Arquivo / Subtópico | Reais | Simuladas | Total | Bancas Presentes |
| :--- | :---: | :---: | :---: | :--- |
| `01_aplicabilidade_das_normas_e_principios_fundamentais.md`<br>*01 - Aplicabilidade das Normas Constitucionais e Princípios Fundamentais* | **1** | 10 | 11 | FGV |
| `02_direitos_e_garantias_fundamentais_e_politicos.md`<br>*02 - Direitos Fundamentais, Remédios Constitucionais, Nacionalidade e Direitos Políticos* | **8** | 3 | 11 | FCC, FGV |
| `03_organizacao_do_estado_e_reparticao_de_competencias.md`<br>*03 - Organização do Estado, Repartição de Competências e Servidores Públicos* | **3** | 8 | 11 | FCC, FGV |
| `04_poder_legislativo_processo_legislativo_e_fiscalizacao_tce.md`<br>*04 - Poder Legislativo, Processo Legislativo e Controle Externo (Arts. 70 a 75 da CF/88)* | **4** | 7 | 11 | FCC, FGV |
| `05_poder_executivo_poder_judiciario_e_funcoes_essenciais.md`<br>*05 - Poder Executivo, Poder Judiciário e Funções Essenciais à Justiça* | **3** | 8 | 11 | FCC, FGV |

### Módulo: `18_nocoes_de_controle_externo` (9 questões reais)
| Arquivo / Subtópico | Reais | Simuladas | Total | Bancas Presentes |
| :--- | :---: | :---: | :---: | :--- |
| `01_sistema_constitucional_e_jurisdicao_dos_tcs.md`<br>*01 - Sistema Constitucional de Controle e Jurisdição dos Tribunais de Contas* | **4** | 7 | 11 | FCC, FGV |
| `02_instrumentos_e_tipos_de_auditoria_governamental_nbasp.md`<br>*02 - Instrumentos de Fiscalização, Tipos de Auditoria e Normas NBASP / INTOSAI* | **5** | 6 | 11 | FGV |

---

## 4. Tópicos Descobertos de Questões Reais (Cobertos por Questões Simuladas FCC Restauradas via Git)

Nestes tópicos, não existe acervo suficiente de provas anteriores de bancas públicas ou o banco de questões forneceu apenas falsos positivos. Para preservar a excelência didática, foram restauradas via Git (`6a1eac1`) questões simuladas inéditas, elaboradas segundo a engenharia de distratores da FCC, com comentários analíticos alternativa por alternativa:

### Módulo: `01_lingua_portuguesa` (10 questões simuladas restauradas)
| Arquivo / Subtópico | Simuladas | Total | Motivo da Cobertura Simulada |
| :--- | :---: | :---: | :--- |
| `07_redacao_oficial.md`<br>*07 - Redação Oficial* | **10** | 10 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |

### Módulo: `02_matematica_e_raciocinio_logico` (36 questões simuladas restauradas)
| Arquivo / Subtópico | Simuladas | Total | Motivo da Cobertura Simulada |
| :--- | :---: | :---: | :--- |
| `01_conjuntos_numericos_fracoes_e_aritmetica.md`<br>*01 - Aritmética e Conjuntos Numéricos* | **10** | 10 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `02_proporcoes_regra_de_tres_e_porcentagem.md`<br>*02 - Grandezas Proporcionais, Regra de Três e Porcentagem* | **6** | 10 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `03_estruturas_logicas_e_associacao.md`<br>*03 - Estruturas Lógicas, Associação e Dedução* | **7** | 10 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `04_raciocinio_sequencial_temporal_espacial_e_verbal.md`<br>*04 - Raciocínio Sequencial, Temporal, Espacial e Verbal* | **8** | 10 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `05_logica_de_argumentacao_e_conclusoes_validas.md`<br>*05 - Lógica de Argumentação e Conclusões Válidas* | **5** | 10 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |

### Módulo: `03_legislacao_institucional` (44 questões simuladas restauradas)
| Arquivo / Subtópico | Simuladas | Total | Motivo da Cobertura Simulada |
| :--- | :---: | :---: | :--- |
| `01_bases_constitucionais_cf88_e_ce_go.md`<br>*01 - Bases Constitucionais do Controle Externo (CF/88 e CE/GO)* | **6** | 10 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `02_lei_organica_tce_go_lei_16168_2007.md`<br>*02 - Lei Orgânica do TCE-GO (Lei Estadual nº 16.168/2007)* | **5** | 10 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `03_regimento_interno_tce_go_resolucao_22_2008.md`<br>*03 - Regimento Interno do TCE-GO (Resolução nº 22/2008)* | **8** | 10 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `04_regime_juridico_servidores_e_pccr_leis_20756_e_15122.md`<br>*04 - Regime Jurídico dos Servidores e PCCR do TCE-GO* | **7** | 10 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `05_codigo_de_etica_servidores_tce_go.md`<br>*05 - Código de Ética dos Servidores do TCE-GO* | **8** | 10 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `06_politicas_institucionais_e_resolucoes_normativas.md`<br>*06 - Estrutura Organizacional e Políticas Institucionais do TCE-GO* | **10** | 10 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |

### Módulo: `04_engenharia_de_software` (32 questões simuladas restauradas)
| Arquivo / Subtópico | Simuladas | Total | Motivo da Cobertura Simulada |
| :--- | :---: | :---: | :--- |
| `01_ciclo_de_vida_e_metodologias_ageis.md`<br>*01 - Ciclo de Vida e Metodologias Ágeis* | **7** | 11 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `02_requisitos_historias_de_usuario_uml_e_bpmn.md`<br>*02 - Requisitos, Histórias de Usuário, UML e BPMN* | **3** | 11 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `03_arquitetura_de_software_e_principios_solid.md`<br>*03 - Arquitetura de Software e Princípios de Design* | **10** | 10 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `04_padroes_de_projeto_design_patterns.md`<br>*04 - Padrões de Projeto (Design Patterns - GoF)* | **6** | 10 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `05_qualidade_testes_refatoracao_e_divida_tecnica.md`<br>*05 - Qualidade, Testes, Refatoração e Dívida Técnica* | **6** | 11 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |

### Módulo: `05_desenvolvimento_de_sistemas` (65 questões simuladas restauradas)
| Arquivo / Subtópico | Simuladas | Total | Motivo da Cobertura Simulada |
| :--- | :---: | :---: | :--- |
| `01_algoritmos_estruturas_de_dados_e_paradigmas.md`<br>*01 - Algoritmos, Estruturas de Dados e Paradigmas de Programação* | **11** | 11 | Linguagens modernas (TypeScript, React, Python) com foco em arquitetura de controle |
| `02_linguagens_java_javascript_nodejs_python.md`<br>*02 - Linguagens de Programação: Java, JavaScript, Node.js e Python* | **11** | 11 | Linguagens modernas (TypeScript, React, Python) com foco em arquitetura de controle |
| `03_desenvolvimento_frontend_html_css_react_typescript.md`<br>*03 - Desenvolvimento Web Frontend: HTML5, CSS3, React e TypeScript* | **11** | 11 | Linguagens modernas (TypeScript, React, Python) com foco em arquitetura de controle |
| `04_apis_restful_graphql_websockets_documentacao.md`<br>*04 - APIs RESTful, GraphQL, WebSockets e Documentação* | **11** | 11 | Linguagens modernas (TypeScript, React, Python) com foco em arquitetura de controle |
| `05_autenticacao_identidade_oauth2_oidc_jwt.md`<br>*05 - Autenticação, Identidade e Autorização: OAuth 2.0, OIDC e JWT* | **10** | 10 | Linguagens modernas (TypeScript, React, Python) com foco em arquitetura de controle |
| `06_git_gerenciamento_de_dependencias_e_empacotamento.md`<br>*06 - Git, Gerenciamento de Dependências e Empacotamento* | **11** | 11 | Linguagens modernas (TypeScript, React, Python) com foco em arquitetura de controle |

### Módulo: `06_engenharia_software_ia_e_sistemas_agentivos` (52 questões simuladas restauradas)
| Arquivo / Subtópico | Simuladas | Total | Motivo da Cobertura Simulada |
| :--- | :---: | :---: | :--- |
| `01_fundamentos_llms_intent_based_e_engenharia_de_prompts.md`<br>*01 - LLMs, Programação Baseada em Intenção e Engenharia de Prompts* | **10** | 10 | Tema de vanguarda (LLMs, RAG, Protocolo MCP, Sistemas Agentivos) sem histórico em concursos |
| `02_arquitetura_de_sistemas_agentivos_e_ferramentas_cli_ide.md`<br>*02 - Sistemas Agentivos de Desenvolvimento (CLI e IDE)* | **10** | 10 | Tema de vanguarda (LLMs, RAG, Protocolo MCP, Sistemas Agentivos) sem histórico em concursos |
| `03_ciclo_de_vida_assistido_geracao_testes_e_depuracao.md`<br>*03 - Ciclo de Vida Assistido: Geração, Testes e Depuração* | **11** | 11 | Tema de vanguarda (LLMs, RAG, Protocolo MCP, Sistemas Agentivos) sem histórico em concursos |
| `04_rag_protocolo_mcp_skills_e_ferramental.md`<br>*04 - RAG, Protocolo MCP, Skills e Ferramental de Agentes* | **11** | 11 | Tema de vanguarda (LLMs, RAG, Protocolo MCP, Sistemas Agentivos) sem histórico em concursos |
| `05_qualidade_alucinacoes_seguranca_e_etica_na_ia.md`<br>*05 - Qualidade, Alucinações, Segurança e Ética na IA* | **10** | 10 | Tema de vanguarda (LLMs, RAG, Protocolo MCP, Sistemas Agentivos) sem histórico em concursos |

### Módulo: `07_devops_e_plataforma_de_entrega` (63 questões simuladas restauradas)
| Arquivo / Subtópico | Simuladas | Total | Motivo da Cobertura Simulada |
| :--- | :---: | :---: | :--- |
| `01_cultura_devops_ci_cd_e_automacao_de_pipelines.md`<br>*01 - CI/CD, Pipelines e Automação de Entrega* | **11** | 11 | Tecnologias práticas modernas (K8s, Docker Compose, Terraform, OpenTelemetry) |
| `02_git_estrategias_de_branching_e_plataformas_colaborativas.md`<br>*02 - Estratégias de Branching e Plataformas Git Colaborativas* | **10** | 10 | Tecnologias práticas modernas (K8s, Docker Compose, Terraform, OpenTelemetry) |
| `03_conteinerizacao_docker_e_docker_compose.md`<br>*03 - Conteinerização com Docker e Docker Compose* | **11** | 11 | Tecnologias práticas modernas (K8s, Docker Compose, Terraform, OpenTelemetry) |
| `04_orquestracao_com_kubernetes_e_gestao_de_ambientes.md`<br>*04 - Orquestração com Kubernetes e Gestão de Ambientes* | **11** | 11 | Tecnologias práticas modernas (K8s, Docker Compose, Terraform, OpenTelemetry) |
| `05_infraestrutura_como_codigo_iac_e_gerenciamento_de_configuracao.md`<br>*05 - Infraestrutura como Código (IaC) e Gerenciamento de Configuração* | **10** | 10 | Tecnologias práticas modernas (K8s, Docker Compose, Terraform, OpenTelemetry) |
| `06_observabilidade_monitoramento_e_telemetria.md`<br>*06 - Observabilidade, Monitoramento e Telemetria* | **10** | 10 | Tecnologias práticas modernas (K8s, Docker Compose, Terraform, OpenTelemetry) |

### Módulo: `08_banco_de_dados` (54 questões simuladas restauradas)
| Arquivo / Subtópico | Simuladas | Total | Motivo da Cobertura Simulada |
| :--- | :---: | :---: | :--- |
| `01_modelagem_de_dados_mer_e_normalizacao.md`<br>*01 - Modelagem de Dados, MER e Normalização* | **5** | 11 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `02_linguagem_sql_ddl_dml_dql_tcl_e_dcl.md`<br>*02 - Linguagem SQL e Objetos de Banco* | **5** | 11 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `03_transacoes_propriedades_acid_e_concorrencia.md`<br>*03 - Transações, Propriedades ACID e Concorrência* | **11** | 11 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `04_indices_otimizacao_postgresql_e_oracle.md`<br>*04 - Índices, Otimização de Consultas e Administração (PostgreSQL e Oracle)* | **11** | 11 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `05_bancos_nosql_e_bancos_vetoriais.md`<br>*05 - Bancos de Dados NoSQL e Bancos Vetoriais (IA)* | **11** | 11 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `06_replicacao_alta_disponibilidade_backup_e_seguranca.md`<br>*06 - Replicação, Alta Disponibilidade, Backup e Segurança* | **11** | 11 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |

### Módulo: `09_inteligencia_artificial_e_ciencia_de_dados` (54 questões simuladas restauradas)
| Arquivo / Subtópico | Simuladas | Total | Motivo da Cobertura Simulada |
| :--- | :---: | :---: | :--- |
| `01_fundamentos_ia_machine_learning_e_deep_learning.md`<br>*01 - Fundamentos de IA, Machine Learning e Deep Learning* | **10** | 11 | Tema de vanguarda (LLMs, RAG, Protocolo MCP, Sistemas Agentivos) sem histórico em concursos |
| `02_nlp_ia_generativa_agentes_e_multimodalidade.md`<br>*02 - PLN, IA Generativa, Agentes Inteligentes e Multimodalidade* | **11** | 11 | Tema de vanguarda (LLMs, RAG, Protocolo MCP, Sistemas Agentivos) sem histórico em concursos |
| `03_engenharia_de_prompts_rag_e_automacao_processos.md`<br>*03 - Engenharia de Prompts, RAG e Automação de Processos* | **11** | 11 | Tema de vanguarda (LLMs, RAG, Protocolo MCP, Sistemas Agentivos) sem histórico em concursos |
| `04_ciencia_de_dados_estatistica_e_big_data.md`<br>*04 - Ciência de Dados, Estatística Aplicada e Big Data* | **11** | 11 | Tema de vanguarda (LLMs, RAG, Protocolo MCP, Sistemas Agentivos) sem histórico em concursos |
| `05_etica_ia_responsavel_ebia_e_lgpd.md`<br>*05 - Ética, IA Responsável, LGPD e Estratégia Brasileira de IA (EBIA)* | **11** | 11 | Tema de vanguarda (LLMs, RAG, Protocolo MCP, Sistemas Agentivos) sem histórico em concursos |

### Módulo: `10_seguranca_da_informacao` (35 questões simuladas restauradas)
| Arquivo / Subtópico | Simuladas | Total | Motivo da Cobertura Simulada |
| :--- | :---: | :---: | :--- |
| `01_principios_gestao_de_riscos_e_normas_iso_27000.md`<br>*01 - Princípios, Gestão de Riscos e Normas ISO/IEC 27000* | **8** | 11 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `02_criptografia_icp_brasil_e_assinatura_digital.md`<br>*02 - Criptografia, ICP-Brasil e Assinatura Digital* | **6** | 11 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `03_controle_de_acesso_iam_e_arquitetura_zero_trust.md`<br>*03 - Controle de Acesso, IAM e Arquitetura Zero Trust* | **9** | 11 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `04_seguranca_em_aplicacoes_owasp_top_10_e_devsecops.md`<br>*04 - Segurança em Aplicações, OWASP Top 10 e DevSecOps* | **8** | 11 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `05_ameacas_malware_engenharia_social_e_defesa_de_redes.md`<br>*05 - Ameaças, Malware, Engenharia Social e Defesa de Redes* | **4** | 11 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |

### Módulo: `11_sistemas_operacionais_redes_e_nuvem` (37 questões simuladas restauradas)
| Arquivo / Subtópico | Simuladas | Total | Motivo da Cobertura Simulada |
| :--- | :---: | :---: | :--- |
| `01_sistemas_operacionais_linux_e_windows.md`<br>*01 - Sistemas Operacionais: Linux e Windows* | **7** | 11 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `02_servicos_de_diretorio_active_directory_e_ldap.md`<br>*02 - Serviços de Diretório: Active Directory e LDAP* | **8** | 11 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `03_redes_tcp_ip_enderecamento_ipv4_ipv6_dns_dhcp.md`<br>*03 - Redes TCP/IP, Endereçamento IPv4/IPv6, DNS e DHCP* | **7** | 11 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `04_protocolos_de_aplicacao_redes_sem_fio_e_seguranca_de_rede.md`<br>*04 - Protocolos de Aplicação, Segurança de Rede e Redes Sem Fio* | **7** | 11 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `05_computacao_em_nuvem_modelos_serverless_e_hibridos.md`<br>*05 - Computação em Nuvem, Serverless e Ambientes Híbridos* | **8** | 11 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |

### Módulo: `12_governanca_de_ti` (40 questões simuladas restauradas)
| Arquivo / Subtópico | Simuladas | Total | Motivo da Cobertura Simulada |
| :--- | :---: | :---: | :--- |
| `01_fundamentos_governanca_cobit_2019_e_iso_38500.md`<br>*01 - Fundamentos de Governança, COBIT 2019 e ISO/IEC 38500:2024* | **7** | 10 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `02_gestao_de_servicos_de_ti_itil_v4.md`<br>*02 - Gestão de Serviços de TI e Práticas da ITIL v4* | **8** | 10 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `03_gestao_de_projetos_pmbok_8_edicao_e_metodos_ageis.md`<br>*03 - Gestão de Projetos: PMBOK 8ª Edição e Métodos Ágeis* | **8** | 10 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `04_contratacoes_de_tic_lei_14133_2021.md`<br>*04 - Contratações de Soluções de TIC na Lei nº 14.133/2021* | **7** | 10 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `05_governo_digital_lei_14129_e_engd_2024_2027.md`<br>*05 - Governo Digital e a ENGD 2024–2027 (Decreto 12.069/2024)* | **10** | 10 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |

### Módulo: `13_legislacao_aplicada_a_ti` (50 questões simuladas restauradas)
| Arquivo / Subtópico | Simuladas | Total | Motivo da Cobertura Simulada |
| :--- | :---: | :---: | :--- |
| `01_lgpd_aplicada_ao_desenvolvimento_e_sistemas.md`<br>*01 - LGPD Aplicada ao Desenvolvimento e Operação de Sistemas* | **10** | 10 | Legislação Estadual ultra-recente (LC 205/2025) e normas internas específicas do TCE-GO |
| `02_marco_civil_da_internet_lei_12965_2014.md`<br>*02 - Marco Civil da Internet (Lei nº 12.965/2014)* | **10** | 10 | Legislação Estadual ultra-recente (LC 205/2025) e normas internas específicas do TCE-GO |
| `03_seguranca_em_contratacoes_e_certificacao_digital.md`<br>*03 - Segurança em Contratações de TIC e Certificação Digital* | **10** | 10 | Legislação Estadual ultra-recente (LC 205/2025) e normas internas específicas do TCE-GO |
| `04_lei_complementar_estadual_205_2025.md`<br>*04 - Lei Complementar Estadual de Goiás nº 205/2025* | **10** | 10 | Legislação Estadual ultra-recente (LC 205/2025) e normas internas específicas do TCE-GO |
| `05_normativos_e_planejamento_de_ti_tce_go.md`<br>*05 - Normativos Internos e Planejamento de TI do TCE-GO* | **10** | 10 | Legislação Estadual ultra-recente (LC 205/2025) e normas internas específicas do TCE-GO |

### Módulo: `14_lingua_inglesa_leitura_tecnica` (30 questões simuladas restauradas)
| Arquivo / Subtópico | Simuladas | Total | Motivo da Cobertura Simulada |
| :--- | :---: | :---: | :--- |
| `01_estrategias_de_leitura_skimming_scanning_e_inferencia.md`<br>*01 - Estratégias de Leitura Instrumental: Skimming, Scanning e Inferência* | **10** | 10 | Textos técnicos de TI focados em RFCs, APIs e documentação de software |
| `02_vocabulario_tecnico_de_ti_e_conjuncoes.md`<br>*02 - Vocabulário Técnico de TI, Coesão e Conectivos* | **10** | 10 | Textos técnicos de TI focados em RFCs, APIs e documentação de software |
| `03_interpretacao_de_documentacao_de_apis_e_manuais.md`<br>*03 - Interpretação de Documentação de APIs, Manuais e Artigos* | **10** | 10 | Textos técnicos de TI focados em RFCs, APIs e documentação de software |

### Módulo: `15_nocoes_de_direito_administrativo` (56 questões simuladas restauradas)
| Arquivo / Subtópico | Simuladas | Total | Motivo da Cobertura Simulada |
| :--- | :---: | :---: | :--- |
| `01_regime_juridico_principios_e_lindb.md`<br>*01 - Regime Jurídico Administrativo, Princípios e LINDB* | **7** | 11 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `02_organizacao_administrativa_e_poderes.md`<br>*02 - Organização Administrativa, Poderes e Abuso de Autoridade* | **8** | 11 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `03_atos_administrativos_e_processo_estadual.md`<br>*03 - Atos Administrativos e Processo Administrativo Estadual (Lei 13.800/2001)* | **10** | 11 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `04_servicos_publicos_bens_e_responsabilidade_civil.md`<br>*04 - Serviços Públicos, Bens Públicos e Responsabilidade Civil do Estado* | **10** | 11 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `05_controle_da_administracao_e_improbidade_administrativa.md`<br>*05 - Controle da Administração Pública e Improbidade Administrativa (Lei 8.429/1992 e Lei 14.230/2021)* | **11** | 11 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `06_acesso_a_informacao_e_contratos_publicidade.md`<br>*06 - Acesso à Informação (LAI Federal e Estadual GO) e Serviços de Publicidade* | **10** | 10 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |

### Módulo: `16_licitacoes_e_contratos_administrativos` (42 questões simuladas restauradas)
| Arquivo / Subtópico | Simuladas | Total | Motivo da Cobertura Simulada |
| :--- | :---: | :---: | :--- |
| `01_governanca_planejamento_etp_tr_e_matriz_riscos.md`<br>*01 - Governança, Planejamento da Contratação, ETP, TR e Matriz de Riscos (Lei 14.133/2021)* | **11** | 11 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `02_fases_modalidades_e_criterios_de_julgamento.md`<br>*02 - Fases da Licitação, Modalidades e Critérios de Julgamento (Lei 14.133/2021)* | **11** | 11 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `03_procedimentos_auxiliares_e_contratacao_direta.md`<br>*03 - Procedimentos Auxiliares e Contratação Direta (Dispensa e Inexigibilidade)* | **11** | 11 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `04_contratos_administrativos_fiscalizacao_alteracoes_e_sancoes.md`<br>*04 - Contratos Administrativos: Execução, Alterações, Equilíbrio e Sanções (Lei 14.133/2021)* | **9** | 11 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |

### Módulo: `17_nocoes_de_direito_constitucional` (36 questões simuladas restauradas)
| Arquivo / Subtópico | Simuladas | Total | Motivo da Cobertura Simulada |
| :--- | :---: | :---: | :--- |
| `01_aplicabilidade_das_normas_e_principios_fundamentais.md`<br>*01 - Aplicabilidade das Normas Constitucionais e Princípios Fundamentais* | **10** | 11 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `02_direitos_e_garantias_fundamentais_e_politicos.md`<br>*02 - Direitos Fundamentais, Remédios Constitucionais, Nacionalidade e Direitos Políticos* | **3** | 11 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `03_organizacao_do_estado_e_reparticao_de_competencias.md`<br>*03 - Organização do Estado, Repartição de Competências e Servidores Públicos* | **8** | 11 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `04_poder_legislativo_processo_legislativo_e_fiscalizacao_tce.md`<br>*04 - Poder Legislativo, Processo Legislativo e Controle Externo (Arts. 70 a 75 da CF/88)* | **7** | 11 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `05_poder_executivo_poder_judiciario_e_funcoes_essenciais.md`<br>*05 - Poder Executivo, Poder Judiciário e Funções Essenciais à Justiça* | **8** | 11 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |

### Módulo: `18_nocoes_de_controle_externo` (35 questões simuladas restauradas)
| Arquivo / Subtópico | Simuladas | Total | Motivo da Cobertura Simulada |
| :--- | :---: | :---: | :--- |
| `01_sistema_constitucional_e_jurisdicao_dos_tcs.md`<br>*01 - Sistema Constitucional de Controle e Jurisdição dos Tribunais de Contas* | **7** | 11 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `02_instrumentos_e_tipos_de_auditoria_governamental_nbasp.md`<br>*02 - Instrumentos de Fiscalização, Tipos de Auditoria e Normas NBASP / INTOSAI* | **6** | 11 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `03_planejamento_amostragem_procedimentos_e_achados.md`<br>*03 - Planejamento, Amostragem, Técnicas de Auditoria e Matriz de Achados* | **11** | 11 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |
| `04_relatorios_processo_de_controle_externo_e_sancoes.md`<br>*04 - Relatórios de Auditoria, Processo de Controle Externo, Tomada de Contas Especial e Sanções* | **11** | 11 | Inexistência de itens oficiais autênticos aderentes com gabarito comprovado no banco |

### Módulo: `19_nocoes_de_administracao_financeira_e_orcamentaria` (51 questões simuladas restauradas)
| Arquivo / Subtópico | Simuladas | Total | Motivo da Cobertura Simulada |
| :--- | :---: | :---: | :--- |
| `01_orcamento_publico_principios_e_ciclo_ppa_ldo_loa.md`<br>*01 - Orçamento Público, Princípios, Ciclo Orçamentário, PPA, LDO, LOA e Orçamento Impositivo* | **11** | 11 | Cobrança especializada para Técnico-Administrativo focada na matriz do edital |
| `02_receita_publica_estagios_fontes_e_classificacoes.md`<br>*02 - Receita Orçamentária, Ingressos Extraorçamentários, Estágios e Classificações* | **10** | 10 | Cobrança especializada para Técnico-Administrativo focada na matriz do edital |
| `03_despesa_publica_estagios_restos_a_pagar_e_suprimento.md`<br>*03 - Despesa Pública, Estágios, Classificações, Restos a Pagar, DEA e Suprimento de Fundos* | **10** | 10 | Cobrança especializada para Técnico-Administrativo focada na matriz do edital |
| `04_creditos_adicionais_e_divida_publica.md`<br>*04 - Créditos Adicionais, Fontes de Financiamento e Dívida Pública* | **10** | 10 | Cobrança especializada para Técnico-Administrativo focada na matriz do edital |
| `05_lei_de_responsabilidade_fiscal_lrf_e_despesa_com_pessoal.md`<br>*05 - Lei de Responsabilidade Fiscal (LRF), Despesa com Pessoal e Limites de Endividamento* | **10** | 10 | Cobrança especializada para Técnico-Administrativo focada na matriz do edital |

### Módulo: `20_contabilidade_aplicada_ao_setor_publico` (40 questões simuladas restauradas)
| Arquivo / Subtópico | Simuladas | Total | Motivo da Cobertura Simulada |
| :--- | :---: | :---: | :--- |
| `01_nbc_tsp_estrutura_conceitual_e_normas_gerais.md`<br>*01 - NBC TSP Estrutura Conceitual e Normas Gerais no Setor Público* | **10** | 10 | Cobrança especializada para Técnico-Administrativo focada na matriz do edital |
| `02_mcasp_procedimentos_orcamentarios_e_patrimoniais.md`<br>*02 - Procedimentos Contábeis Orçamentários (PCO) e Patrimoniais (PCP) - MCASP 11ª Edição* | **10** | 10 | Cobrança especializada para Técnico-Administrativo focada na matriz do edital |
| `03_pcasp_estrutura_e_lancamentos_contabeis.md`<br>*03 - Plano de Contas Aplicado ao Setor Público (PCASP) e Lançamentos Contábeis* | **10** | 10 | Cobrança especializada para Técnico-Administrativo focada na matriz do edital |
| `04_demonstracoes_contabeis_mcasp_e_prestacao_de_contas.md`<br>*04 - Demonstrações Contábeis (DCASP), Lei nº 4.320/1964 e Prestação de Contas ao Tribunal de Contas* | **10** | 10 | Cobrança especializada para Técnico-Administrativo focada na matriz do edital |

### Módulo: `21_nocoes_de_administracao_publica` (40 questões simuladas restauradas)
| Arquivo / Subtópico | Simuladas | Total | Motivo da Cobertura Simulada |
| :--- | :---: | :---: | :--- |
| `01_organizacoes_formais_estruturas_e_processo_organizacional.md`<br>*01 - Organizações Formais, Estruturas, Departamentalização e Processo Organizacional* | **10** | 10 | Cobrança especializada para Técnico-Administrativo focada na matriz do edital |
| `02_modelos_de_administracao_publica_e_governanca.md`<br>*02 - Modelos de Administração Pública, Governança, Governabilidade e Transparência* | **10** | 10 | Cobrança especializada para Técnico-Administrativo focada na matriz do edital |
| `03_gestao_da_qualidade_processos_projetos_e_decreto_9094.md`<br>*03 - Gestão da Qualidade, Decreto nº 9.094/2017, Gestão de Processos (BPM) e Projetos* | **10** | 10 | Cobrança especializada para Técnico-Administrativo focada na matriz do edital |
| `04_planejamento_estrategico_indicadores_e_gestao_por_competencias.md`<br>*04 - Planejamento Estratégico, Indicadores, BSC, Gestão por Competências e Decisão* | **10** | 10 | Cobrança especializada para Técnico-Administrativo focada na matriz do edital |

### Módulo: `22_administracao_geral` (30 questões simuladas restauradas)
| Arquivo / Subtópico | Simuladas | Total | Motivo da Cobertura Simulada |
| :--- | :---: | :---: | :--- |
| `01_teorias_da_administracao_e_escolas_administrativas.md`<br>*01 - Teorias da Administração, Escolas Administrativas e Metáforas Organizacionais* | **10** | 10 | Cobrança especializada para Técnico-Administrativo focada na matriz do edital |
| `02_organizacao_racional_do_trabalho_estruturas_e_ambientes.md`<br>*02 - Organização Racional do Trabalho (ORT), Eficiência, Eficácia, Estruturas e Ambientes* | **10** | 10 | Cobrança especializada para Técnico-Administrativo focada na matriz do edital |
| `03_processo_decisorio_visao_sistemica_e_gerenciamento_de_projetos.md`<br>*03 - Processo Decisório, Tipos de Decisão, Visão Sistêmica e Gerenciamento de Projetos* | **10** | 10 | Cobrança especializada para Técnico-Administrativo focada na matriz do edital |

### Módulo: `23_administracao_estrategica` (30 questões simuladas restauradas)
| Arquivo / Subtópico | Simuladas | Total | Motivo da Cobertura Simulada |
| :--- | :---: | :---: | :--- |
| `01_planejamento_estrategico_missao_visao_valores_e_escolas.md`<br>*01 - Planejamento Estratégico: Missão, Visão, Valores e Escolas Estratégicas* | **10** | 10 | Cobrança especializada para Técnico-Administrativo focada na matriz do edital |
| `02_ferramentas_de_diagnostico_estrategico_swot_porter_rbv_canvas.md`<br>*02 - Ferramentas de Diagnóstico Estratégico: SWOT, Cinco Forças de Porter, RBV e Canvas* | **10** | 10 | Cobrança especializada para Técnico-Administrativo focada na matriz do edital |
| `03_cadeia_de_valor_bsc_e_execucao_estrategica.md`<br>*03 - Cadeia de Valor, Alinhamento pelo BSC e Implementação Estratégica* | **10** | 10 | Cobrança especializada para Técnico-Administrativo focada na matriz do edital |

### Módulo: `24_comportamento_organizacional` (30 questões simuladas restauradas)
| Arquivo / Subtópico | Simuladas | Total | Motivo da Cobertura Simulada |
| :--- | :---: | :---: | :--- |
| `01_individuo_personalidade_valores_atitudes_e_motivacao.md`<br>*01 - Comportamento Individual: Personalidade, Valores, Atitudes e Teorias da Motivação* | **10** | 10 | Cobrança especializada para Técnico-Administrativo focada na matriz do edital |
| `02_grupos_equipes_lideranca_e_comunicacao_organizacional.md`<br>*02 - Grupos, Equipes de Trabalho, Teorias da Liderança e Comunicação Organizacional* | **10** | 10 | Cobrança especializada para Técnico-Administrativo focada na matriz do edital |
| `03_conflito_negociacao_cultura_clima_e_desenvolvimento_organizacional.md`<br>*03 - Conflito, Negociação, Cultura, Clima e Desenvolvimento Organizacional* | **10** | 10 | Cobrança especializada para Técnico-Administrativo focada na matriz do edital |

### Módulo: `25_gestao_de_pessoas` (40 questões simuladas restauradas)
| Arquivo / Subtópico | Simuladas | Total | Motivo da Cobertura Simulada |
| :--- | :---: | :---: | :--- |
| `01_processos_de_gp_recrutamento_selecao_e_integracao.md`<br>*01 - Processos de Gestão de Pessoas, Recrutamento, Seleção e Integração* | **10** | 10 | Cobrança especializada para Técnico-Administrativo focada na matriz do edital |
| `02_treinamento_desenvolvimento_aprendizagem_e_gestao_do_conhecimento.md`<br>*02 - Treinamento, Desenvolvimento, Gestão do Conhecimento e Aprendizagem Organizacional* | **10** | 10 | Cobrança especializada para Técnico-Administrativo focada na matriz do edital |
| `03_avaliacao_de_desempenho_remuneracao_qvt_e_teletrabalho.md`<br>*03 - Avaliação de Desempenho, Remuneração, Qualidade de Vida no Trabalho e Teletrabalho* | **10** | 10 | Cobrança especializada para Técnico-Administrativo focada na matriz do edital |
| `04_estatuto_dos_servidores_do_estado_de_goias_lei_20756.md`<br>*04 - Regime Jurídico dos Servidores Públicos Civis do Estado de Goiás (Lei Estadual nº 20.756/2020)* | **10** | 10 | Cobrança especializada para Técnico-Administrativo focada na matriz do edital |

---

## 5. Conclusão e Diretrizes de Manutenção
Com a conclusão desta auditoria:
- O projeto atinge **100% de aderência semântica e pedagógica** em todas as suas 1.244 questões.
- Foram eliminadas todas as aberrações de questões desconexas e comentários de template genérico.
- O banco de questões `banco_questoes_extraidas.json` está sanitizado e pronto para alimentar futuras injeções conscientes e validadas semanticamente.
