from pathlib import Path

import pandas as pd

caminho_tempos_treinamento = Path('Ex031', 'tempos_treinamento.csv')

df_tempos_treinamento = pd.read_csv(caminho_tempos_treinamento)

media = df_tempos_treinamento['tempo_treinamento'].mean()
desvio_padrao = df_tempos_treinamento['tempo_treinamento'].std()

print(
    f'Tempo de Treinamento - Médio: {media:.4f}s',
    f'Tempo de Treinamento - Desvio Padrão: {desvio_padrao:.4f}s',
    sep='\n'
)