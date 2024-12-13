import pandas as pd
import numpy as np
from procura_arquivos import procura

lista_de_matrizes_z = procura('Z_pu*.csv', './')

for matriz_z in lista_de_matrizes_z:
    nome_matriz_dividido = matriz_z.split("_",1)
    nome_matriz_redividido = nome_matriz_dividido[1].split("_", 1)
    inicio_nome_matriz = nome_matriz_dividido[0] + "_" + nome_matriz_redividido[0]
    final_nome_matriz = nome_matriz_redividido[1]
    #final_nome_matriz_sem_extensao = final_nome_matriz.rsplit(".csv")[0]
    caminho = "./{}".format(matriz_z)
    matriz_z_df = pd.read_csv(caminho, index_col=0)
    autovalores_matriz_z, autovetores_matriz_z = np.linalg.eig(matriz_z_df)
    matriz_z_diagonal = np.diag(autovalores_matriz_z)
    caminho_saida = inicio_nome_matriz + "_diagonal_" + final_nome_matriz
    matriz_z_diagonal_df = pd.DataFrame(matriz_z_diagonal)
    matriz_z_diagonal_df.to_csv(caminho_saida)
    autovetores_matriz_z_df = pd.DataFrame(autovetores_matriz_z)
    autovetores_matriz_z_df.to_csv("autovetores_{}".format(caminho_saida))

print("Matrizes Z em pu decompostas diagonalmente e matrizes de autovetores obtidas")
