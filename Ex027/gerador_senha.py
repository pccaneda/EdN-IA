import random
import string

caracteres_validos = string.ascii_letters + string.digits + string.punctuation

def gera_senha(k: int) -> str:
    senha = ''.join(random.choices(caracteres_validos, k=k))
    return senha

while True:
    k = input('Informe o tamanho da senha: ')

    try:
        k = int(k)
        senha = gera_senha(k=k)
        print(senha)
        break
    except ValueError:
        print('O tamanho da senha deve ser um número inteiro\n')