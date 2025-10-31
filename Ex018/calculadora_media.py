n1 = float(input('N1 = '))
n2 = float(input('N2 = '))
n3 = float(input('N3 = '))
n4 = float(input('N4 = '))

p1 = 2
p2 = 3
p3 = 4
p4 = 1

media_ponderada = (p1*n1 + p2*n2 + p3*n3 + p4*n4) / (p1 + p2 + p3 + p4)

print('-'*30)

print(f'Média: {media_ponderada:.1f}')

if media_ponderada >= 7.0:
    print('Aluno aprovado.')
elif media_ponderada < 5.0:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')

    n_exame = float(input('Nota do exame = '))
    media_final = (media_ponderada + n_exame) / 2

    if media_final >= 5.0:
        print(
            'Aluno aprovado.', 
            f'Média final: {media_final:.1f}', 
            sep='\n'
        )
    else:
        print(
            'Aluno reprovado.',
            f'Média final: {media_final:.1f}',
            sep='\n'
        )