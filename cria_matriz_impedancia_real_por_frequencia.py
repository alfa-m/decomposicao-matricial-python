import pandas as pd
from procura_arquivos import procura

lista_de_harmonicos_reduzido = pd.read_csv("./arquivos_csv_base/espectro_harmonico_reduzido.csv", header=None)[0]
lista_de_nos = pd.read_csv("./arquivos_csv_base/lista_de_nos.csv", index_col=0).drop([0,1,2])["0"]
arquivos_v_real = procura("real_v_node*.csv", "./arquivos_csv_base/")

indice = 0
for harmonico in lista_de_harmonicos_reduzido:
    harmonico_df = pd.DataFrame()
    for i in range(len(lista_de_nos)):
        node = lista_de_nos.iloc[i]

        for arquivo in arquivos_v_real:
            nome_arquivo_dividido = arquivo.rsplit("_")
            final_nome_arquivo = nome_arquivo_dividido[-1]
            final_nome_arquivo_sem_extensao = final_nome_arquivo.rsplit(".csv")[0]

            if final_nome_arquivo_sem_extensao == node:
                # print("Match!")
                caminho = "./arquivos_csv_base/{}".format(arquivo)
                arquivo_df = pd.read_csv(caminho, index_col=0).drop([0,2,4])
                harmonico_df[node] = arquivo_df.iloc[:,indice]
                break
            else:
                # print("Sem match!")
                continue

    harmonico_df.index = lista_de_nos
    harmonico_df.to_csv("Z_real_harmonico_{}.csv".format(harmonico))
    indice = indice + 1

print("Matrizes Z real criadas")
