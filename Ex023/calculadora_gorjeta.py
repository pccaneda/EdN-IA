def calcula_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    gorjeta: float = porcentagem_gorjeta * valor_conta

    return gorjeta

try:
    valor_conta = input('Valor da conta: ')
    valor_conta = float(valor_conta)
except ValueError as e:
    e.add_note('\nO valor da conta deve ser um número.\n')
    raise

try:
    porcentagem_gorjeta = input('Porcentagem da gorjeta (valor entre 0 e 1, inclusive): ')
    porcentagem_gorjeta = float(porcentagem_gorjeta)
except ValueError as e:
    e.add_note('\nA porcentagem da gorjeta deve ser um número.\n')
    raise

if __name__ == '__main__':

    gorjeta = calcula_gorjeta(valor_conta, porcentagem_gorjeta)
    print(f'A gorjeta é: {gorjeta}')