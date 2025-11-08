from datetime import datetime

def calcula_idade_em_dias(data_nascimento: str) -> int:
    
    ano_atual = datetime.today()
    idade_dias = (ano_atual - data_nascimento).days

    return idade_dias

if __name__ == '__main__':

    try:
        data_nascimento = input('Data de nascimento: ')
        data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
    except ValueError as e:
        e.add_note('\nA data de nascimento deve possuir o formato dd/mm/aaaa.\n')
        raise

    idade_dias = calcula_idade_em_dias(data_nascimento=data_nascimento)

    print(f'Idade em dias: {idade_dias}')
