import os, fnmatch
import pandas as pd
from pandas import read_csv

lista_de_harmonicos_reduzido = pd.read_csv("./arquivos_csv_base/espectro_harmonico_reduzido.csv", header=None)[0]
lista_de_nos = pd.read_csv("./arquivos_csv_base/lista_de_nos.csv", index_col=0).drop([0,1,2])["0"]

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(name)
    return result

arquivos_vmag = find('vmagpu_node*.csv', './arquivos_csv_base/')

indice = 0
for harmonico in lista_de_harmonicos_reduzido:
    harmonico_df = pd.DataFrame()
    for i in range(len(lista_de_nos)):
        node = lista_de_nos.iloc[i]

        for arquivo in arquivos_vmag:
            nome_arquivo_dividido = arquivo.rsplit("_")
            final_nome_arquivo = nome_arquivo_dividido[-1]
            final_nome_arquivo_sem_extensao = final_nome_arquivo.rsplit(".csv")[0]

            if final_nome_arquivo_sem_extensao == node:
                # print("Match!")
                caminho = "./arquivos_csv_base/{}".format(arquivo)
                arquivo_df = pd.read_csv(caminho, index_col=0).drop([0,1,2])
                harmonico_df[node] = arquivo_df.iloc[:,indice]
                break
            else:
                # print("Sem match!")
                continue

    harmonico_df.index = lista_de_nos
    harmonico_df.to_csv("Z_pu_harmonico_{}.csv".format(harmonico))
    indice = indice + 1

print("Matrizes Z em pu criadas")