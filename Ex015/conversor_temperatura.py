# Funções de conversão

def celsius_para_fahrenheit(temperatura):
    return temperatura * 1.8 + 32

def fahrenheit_para_celsius(temperatura):
    return (temperatura - 32) / 1.8

def celsius_para_kelvin(temperatura):
    return temperatura + 273.15

def kelvin_para_celsius(temperatura):
    return temperatura - 273.15


# Entrada

temperatura = float(input('Digite uma temperatura: '))
escala_origem = input('Digite a escala de origem: ')
escala_destino = input('Digite a escala de destino: ')


# Lógica

if escala_origem == 'Celsius':
    if escala_destino == 'Fahrenheit':
        temperatura_destino = celsius_para_fahrenheit(temperatura)
        print(f'Temperatura em Fahrenheit: {temperatura_destino} ºF')
    if escala_destino == 'Kelvin':
        temperatura_destino = celsius_para_kelvin(temperatura)
        print(f'Temperatura em Kelvin: {temperatura_destino} K')

if escala_origem == 'Fahrenheit':
    if escala_destino == 'Celsius':
        temperatura_destino = fahrenheit_para_celsius(temperatura)
        print(f'Temperatura em Celsius: {temperatura_destino} ºC')
    if escala_destino == 'Kelvin':
        temperatura_destino = celsius_para_kelvin(fahrenheit_para_celsius(temperatura))
        print(f'Temperatura em Kelvin: {temperatura_destino} K')

if escala_origem == 'Kelvin':
    if escala_destino == 'Celsius':
        temperatura_destino = kelvin_para_celsius(temperatura)
        print(f'Temperatura em Celsius: {temperatura_destino} ºC')
    if escala_destino == 'Fahrenheit':
        temperatura_destino = celsius_para_fahrenheit(kelvin_para_celsius(temperatura))
        print(f'Temperatura em Fahrenheit: {temperatura_destino} ºF')