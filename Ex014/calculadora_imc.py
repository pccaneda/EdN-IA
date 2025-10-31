peso = float(input('Informe seu peso (kg): '))
altura = float(input('Informe sua altura (m): '))

imc = peso / altura ** 2

print(f'-'*30)
print(f'Seu IMC é {imc:.1f} km/m\u00B2')

if imc < 18.5:
    print('Classificação = Abaixo do peso')
elif imc < 25:
    print('Classificação = Peso normal')
elif imc < 30:
    print('Classificação = Sobrepeso')
else:
    print('Classificação = Obeso')