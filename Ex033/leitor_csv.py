import csv
from pathlib import Path

# Mesmo arquivo escrito no Exercício 32
CAMINHO_PERFIS = Path('Ex033', 'perfis.csv')

with open(CAMINHO_PERFIS, newline='', encoding='utf-8') as f:
    leitor = csv.reader(f)
    
    for linha in leitor:
        print(','.join(linha))