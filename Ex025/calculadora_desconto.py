def calcula_desconto(produto_preco: float, desconto_percentual: float) -> float:

    desconto_valor = desconto_percentual * produto_preco
    produto_preco_final = produto_preco - desconto_valor

    return desconto_valor, produto_preco_final

if __name__ == '__main__':

    try:
        produto_preco = input('Preço do produto: ')
        produto_preco = float(produto_preco)
    except ValueError as e:
        e.add_note('\nO preço do produto deve ser um valor numérico.\n')
        raise

    try:
        desconto_percentual = input('Desconto percentual: ')
        desconto_percentual = float(desconto_percentual)
    except ValueError as e:
        e.add_note('\nO desconto percentual deve ser um valor numérico.\n')
        raise

    if not 0 <= desconto_percentual <= 1:
        raise ValueError('O desconto percentual deve ser um valor entre 0 e 1, inclusives.')
    
    desconto_valor, preco_final = calcula_desconto(produto_preco=produto_preco, desconto_percentual=desconto_percentual)

    print(f'Preço final: R$ {preco_final:.2f}')