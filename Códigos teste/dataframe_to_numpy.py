import pandas as pd

matriz_df = pd.DataFrame({"V1": [-5, 2, 7], "V2": [2, -2, 3], "V3": [1, 4, 7]})
print(matriz_df)

matriz_numpy = matriz_df.to_numpy()
print(matriz_numpy)