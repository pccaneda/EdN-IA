from pathlib import Path
import time

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


X, y = load_iris(return_X_y=True)
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.8, random_state=42)

rf_clf = RandomForestClassifier()

tempos_treinamento = []

for i in range(30):

    tic = time.time()
    rf_clf.fit(X_treino, y_treino)
    tac = time.time()

    tempos_treinamento.append(tac - tic)

df_tempos_treinamento = pd.Series(tempos_treinamento)

caminho_tempos_treinamneto = Path('Ex031', 'tempos_treinamento.csv')
df_tempos_treinamento.to_csv(caminho_tempos_treinamneto, index=False, header=['tempo_treinamento'])