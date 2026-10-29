import json
from collections import Counter

data = json.load(open('banco_questoes_extraidas.json', 'r', encoding='utf-8'))
questoes = [q for q in data['questoes'] if q.get('status_integracao') == 'pendente' and q.get('numero_original', 0) > 20]

ti_cats = {
    'banco_de_dados': ['sql', 'tabela', 'select', 'join', 'sgbd', 'relacional', 'nosql', 'chave primária', 'forma normal', 'ddl', 'dml'],
    'redes_infra': ['tcp', 'ip', 'udp', 'ipv6', 'ipv4', 'dns', 'dhcp', 'roteador', 'switch', 'vlan', 'snmp', 'camada de rede', 'enlace'],
    'seguranca': ['criptografia', 'rsa', 'aes', 'hash', 'firewall', 'iso 27001', 'certificado digital', 'icp-brasil', 'assinatura digital', 'ataque'],
    'eng_software': ['scrum', 'sprint', 'uml', 'caso de uso', 'requisitos', 'rup', 'teste de unidade', 'diagrama de classes', 'microsserviços', 'padrão de projeto'],
    'governanca_ti': ['itil', 'cobit', 'gerenciamento de incidentes', 'slm', 'acordo de nível de serviço', 'mudança', 'governança'],
    'sistemas_operacionais': ['linux', 'windows', 'processo', 'thread', 'deadlock', 'memória virtual', 'raid', 'ext4', 'sistema de arquivos']
}

for cat, kws in ti_cats.items():
    cnt = 0
    fcc_cnt = 0
    fgv_cnt = 0
    for q in questoes:
        text = (q['enunciado'] + ' ' + ' '.join(q['alternativas'].values())).lower()
        if any(w in text for w in kws):
            cnt += 1
            if q['banca'] == 'FCC': fcc_cnt += 1
            elif q['banca'] == 'FGV': fgv_cnt += 1
    print(f"{cat}: {cnt} questões reais (FCC: {fcc_cnt}, FGV: {fgv_cnt})")

