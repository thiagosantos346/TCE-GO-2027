# -*- coding: utf-8 -*-
with open("templates/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace:
# /* Sumário de Tópico e Listas de Alternativas (Sem Bolinhas Duplicadas) */
# ul.sumario-list, ul.sumario-list ul {
#     list-style: none !important;
# }
# 
# ul.sumario-list {
#     padding-left: 0 !important;
# }
# 
# ul.sumario-list ul {
#     padding-left: 24px !important;
# }

old = '''/* Sumário de Tópico e Listas de Alternativas (Sem Bolinhas Duplicadas) */
ul.sumario-list, ul.sumario-list ul {
    list-style: none !important;
}

ul.sumario-list {
    padding-left: 0 !important;
}

ul.sumario-list ul {
    padding-left: 24px !important;
}'''

new = '''/* Sumário de Tópico Hierárquico Ordenado */
ol.sumario-list {
    padding-left: 24px !important;
    margin-top: 10px;
    margin-bottom: 20px;
}

ol.sumario-list > li {
    font-weight: 700;
    margin-top: 8px;
    margin-bottom: 4px;
    color: var(--text-heading);
}

ol.sumario-list ol {
    padding-left: 24px !important;
    margin-top: 4px;
    margin-bottom: 6px;
}

ol.sumario-list ol > li {
    font-weight: 400;
    margin-top: 2px;
    margin-bottom: 2px;
    color: var(--text-main);
}

ul.sumario-list, ul.sumario-list ul {
    list-style: none !important;
    padding-left: 0 !important;
}

ul.sumario-list ul {
    padding-left: 24px !important;
}'''

if old in css:
    css = css.replace(old, new, 1)
    with open("templates/style.css", "w", encoding="utf-8") as f:
        f.write(css)
    print("SUCCESS: Updated style.css with ordered sumario styles!")
else:
    print("Old CSS block not found!")

