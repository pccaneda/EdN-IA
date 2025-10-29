import locale

locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF8')

produto_nome = 'Cadeira Infantil'
produto_preco = 12.40
produto_qtd = 3

preco_total = produto_preco * produto_qtd

print(
    f'Produto: {produto_nome}', 
    f'Preço: {locale.currency(produto_preco)}', 
    f'Quantidade: {produto_qtd}', 
    '-'*30,
    f'Total: {locale.currency(preco_total)}',
    sep='\n'
)