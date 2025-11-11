import json
from pathlib import Path

import requests


CAMINHO_PERFIS = Path('Ex034', 'perfis.json')


def gera_perfil(n: int) -> list[dict]:

    url = f'https://randomuser.me/api/?nat=br&inc=name,dob,location&results={n}'
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()

        return dados['results']

    else:
        print(f'Erro {resposta.status_code}. Tente novamente.')


if __name__ == '__main__':

    n = input('Digite quantos perfis gerar: ')

    try:
        n = int(n)
    except ValueError as e:
        e.add_note('O número de perfis deve ser um valor numérico inteiro e positivo.\n')
        raise

    perfis = gera_perfil(n)

    perfis_processados = [
        {
            'nome': perfil['name']['first'] + ' ' + perfil['name']['last'],
            'idade': perfil['dob']['age'],
            'cidade': perfil['location']['city']
        }
        for perfil in perfis
    ]

    with open(CAMINHO_PERFIS, 'w', encoding='utf-8') as f:
        json.dump(perfis_processados, f, ensure_ascii=False, indent=4)

    with open(CAMINHO_PERFIS, encoding='utf-8') as f:
        print(f.read())