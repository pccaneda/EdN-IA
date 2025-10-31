distancia = 300
combustivel_consumido = 25

consumo_medio = distancia / combustivel_consumido

print(
    f'Distância percorrida: {distancia} km',
    f'Combustível consumido: {combustivel_consumido} \u2113',
    f'Consumo médio: {consumo_medio:.2f} km/\u2113',
    sep='\n'
)