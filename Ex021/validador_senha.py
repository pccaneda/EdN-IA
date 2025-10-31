import getpass
import re

def validador_senha(senha):
    senha_valida = re.match(r'^(?=.*\d).{8,}$', senha)
    return senha_valida

print('Digite uma senha com ao menos 8 caracteres e 1 dígito. Digite "sair" para encerrar.')

while True:

    senha = getpass.getpass('')

    if senha.lower() == 'sair':
        break

    else:
        senha_validada = validador_senha(senha)

        if senha_validada:
            print('Senha válida.')
            break
        else:
            print('A senha deve conter ao menos 8 caracteres e 1 dígito.')