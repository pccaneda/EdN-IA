valor_real = 100
cambio_real_para_dolar = 5.60
cambio_real_para_euro = 6.60

valor_dolar = valor_real / cambio_real_para_dolar
valor_euro = valor_real / cambio_real_para_euro

print(
    f'Valor em dólar = ${valor_dolar:.2f}', 
    f'Valor em euro = \u20AC{valor_euro:.2f} ', 
    sep='\n'
)
