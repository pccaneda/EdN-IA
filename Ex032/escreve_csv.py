import csv
from pathlib import Path

import requests

CAMINHO_PERFIS = Path('Ex032', 'perfis.csv')

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

    with open(CAMINHO_PERFIS, 'w', newline='', encoding='utf-8') as f:
        escritor = csv.DictWriter(f, fieldnames=['Nome', 'Idade', 'Cidade'])
        
        escritor.writeheader()
        
        for perfil in perfis:
            escritor.writerow({
                'Nome': perfil['name']['first'] + ' ' + perfil['name']['last'],
                'Idade': perfil['dob']['age'],
                'Cidade': perfil['location']['city'],
            })
