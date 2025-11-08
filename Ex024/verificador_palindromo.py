def verifica_palindromo(palavra: str) -> str:
    palavra  = palavra.lower()
    return 'Sim' if palavra[::-1] == palavra else 'Não'

if __name__ == '__main__':
    
    palavra = input('Digite uma palavra: ')

    print(
        f'{palavra.title()} é um palíndromo?', 
        verifica_palindromo(palavra), 
        sep='\n'
    )