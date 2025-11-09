import requests

def buscador_cep(cep: str) -> tuple[str]:

    cep = cep.strip().replace('-', '')
    url = f'https://viacep.com.br/ws/{cep}/json'
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        
        logradouro = dados['logradouro']
        bairro = dados['bairro']
        cidade = dados['localidade']
        estado = dados['estado']

        return logradouro, bairro, cidade, estado
    
    else:
        print(f'Erro {resposta.status_code}. Tente novamente.')

if __name__ == '__main__':

    cep = input('Digite um CEP: ')

    logradouro, bairro, cidade, estado = buscador_cep(cep)

    print(
        f'Logradouro: {logradouro}',
        f'Bairro: {bairro}',
        f'Cidade: {cidade}',
        f'Estado: {estado}',
        sep='\n'
    )