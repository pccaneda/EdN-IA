raio = float(input('Raio do círculo = '))

# Este valor foi exigido
pi = 3.14159265

# Dupla precisão no valor do raio
area = pi * ( round(raio, 2) ** 2 )

print(f'A={area:.4f}')