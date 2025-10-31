produto_nome = 'Camiseta'
produto_preco = 50.00
venda_desconto = 0.2

valor_descontado = produto_preco * venda_desconto
produto_preco_final = produto_preco - valor_descontado

print(
    f'Produto: {produto_nome}', 
    f'Preço Original: R$ {produto_preco}', 
    f'Desconto: R$ {valor_descontado}', 
    f'Preço final: R$ {produto_preco_final}', 
    sep='\n'
)