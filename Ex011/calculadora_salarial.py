numero_funcionario = int(input('Número do funcionário: '))
horas_trabalhadas = int(input('Horas trabalhadas: '))
valor_por_hora = float(input('Valor por hora: '))

salario = valor_por_hora * horas_trabalhadas

print(
    f'Número do funcionário = {numero_funcionario}',
    f'Salário = R$ {salario:.2f}',
    sep='\n'
)

