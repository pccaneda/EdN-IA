vendedor_nome = input('Nome do vendedor: ')
vendedor_salario = float(input('Salário do vendedor: '))
vendedor_vendas = float(input('Total em vendas fechadas pelo vendedor: '))
vendedor_comissao = 0.15

vendedor_pagamento = vendedor_salario + vendedor_comissao * vendedor_vendas

print(
    '-'*30,
    f'Vendedor: {vendedor_nome}',
    f'Pagamento: R$ {vendedor_pagamento:.2f}',
    sep='\n'
)