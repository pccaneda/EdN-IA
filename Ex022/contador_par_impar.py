pares = []
impares = []

while True:

    entrada = input('Digite um número inteiro. Digite "fim" para encerrar: ')

    if entrada.lower() == 'fim':
        break

    try:
        numero = int(entrada)

        if numero % 2 == 0:
            pares.append(numero)
            print(f'{numero} é par\n')

        else:
            impares.append(numero)
            print(f'{numero} é ímpar\n')

    except ValueError:
        print(f'O valor digitado {entrada} não é um número inteiro\n')

print(
    f'Quantidade de números pares digitados: {len(pares)}', 
    f'Quantidade de números ímpares digitados: {len(impares)}', 
    sep='\n'
)