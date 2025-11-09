import requests

def consulta_cambio(moeda: str) -> tuple[str]:

    moeda = moeda.strip().upper()
    url = f'https://economia.awesomeapi.com.br/json/last/{moeda}-BRL'
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        chave = f'{moeda}BRL'
        
        # A API não fornece o preço atual (o último preço onde ocorreu bid = ask), 
        # então tomamos ask para essa finalidade
        maxima = dados[chave]['high']
        minima = dados[chave]['low']
        atual = dados[chave]['ask']
        data, hora = dados[chave]['create_date'].split(' ')

        return maxima, minima, atual, data, hora
    
    else:
        print(f'Erro {resposta.status_code}. Tente novamente.\ncny')

if __name__ == '__main__':

    moeda = input('Digite o código da moeda: ')
    
    maxima, minima, atual, data, hora = consulta_cambio(moeda)

    print(
        f'Atual: {atual}',
        f'Máxima: {maxima}',
        f'Mínima: {minima}',
        f'Data: {data}',
        f'Hora: {hora}',
        sep='\n'
    )
