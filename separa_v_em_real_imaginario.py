import pandas as pd
from procura_arquivos import procura

arquivos_v = procura("v_*.csv", "./arquivos_csv_base/")
matrizVreal = pd.DataFrame()
matrizVimaginario = pd.DataFrame()

for arquivo in arquivos_v:
    arquivo_df = pd.read_csv("./arquivos_csv_base/{}".format(arquivo))
    matrizVreal = arquivo_df[arquivo_df.iloc[:,0] % 2 == 0]
    matrizVimaginario = arquivo_df[arquivo_df.iloc[:,0] % 2 == 1]
    matrizVreal = matrizVreal.iloc[:,1:]
    matrizVimaginario = matrizVimaginario.iloc[:,1:]
    matrizVreal.to_csv("./arquivos_csv_base/real_{}".format(arquivo))
    matrizVimaginario.to_csv("./arquivos_csv_base/imaginario_{}".format(arquivo))

print("Fim da criação das matrizes V real e V imaginário")
