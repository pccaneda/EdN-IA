notas = []

while True:

    print('Digite uma nota. Digite "fim" para encerrar.\n')
    nota = input()

    if nota.lower() == 'fim':
        break

    try:
        nota = float(nota)
        notas.append(float(nota))
    except:
        pass

media_turma = sum(notas) / len(notas)

print(f'Média da turma = {media_turma:.2f}')

