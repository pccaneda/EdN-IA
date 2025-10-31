from operator import add, mul, truediv, sub

operacoes_validas = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv
}

def entrada_numero(msg):

    while True:
        try:
            return float(input(msg))
        except ValueError:
            print('Informe um número inteiro ou de ponto flutuante.\n')

def entrada_operacao(msg):

    while True:
        try:
            operador = input(msg)

            if operador not in operacoes_validas:
                raise ValueError
            
            return operador, operacoes_validas[operador]
        except ValueError:
            print('Informe uma operação válida (+, -, *, /).\n')

print('Insira dois números e uma operação elementar (+, -, *, /):')
print('-'*30)

while True:
    try:
        n1 = entrada_numero('Número 1 = ')
        n2 = entrada_numero('Número 2 = ')
        operador, operacao = entrada_operacao('Operação: ')

        print(f'{n1} {operador} {n2} = {operacao(n1,n2)}')
        break
    except ZeroDivisionError:
        print('Divisão por zero não é permitida. Tente novamente.\n')