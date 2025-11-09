import requests

def gera_usuario() -> tuple[str]:
    url = 'https://randomuser.me/api/'
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        usuario = dados['results'][0]
        
        nome = f'{usuario["name"]["title"]} {usuario["name"]["first"]} {usuario["name"]["last"]}'
        email = usuario['email']
        pais = usuario['location']['country']

        return nome, email, pais

    else:
        print(f'Erro {resposta.status_code}. Tente novamente.')

if __name__ == '__main__':

    nome, email, pais = gera_usuario()

    print(
        f'Nome: {nome}', 
        f'Email: {email}', 
        f'País: {pais}', 
        sep='\n'
    )