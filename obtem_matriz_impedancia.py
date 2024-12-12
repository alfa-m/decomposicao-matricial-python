import pandas as pd

matriz_a = pd.DataFrame({"V1": [1, 2, 3], "V2": [4, 5, 6], "V3": [7, 8, 9]})
matriz_b = pd.DataFrame({"V1": [-1, -2, -3], "V2": [-4, -5, -6], "V3": [-7, -8, -9]})
matriz_c = pd.DataFrame({"V1": [10, 20, 30], "V2": [40, 50, 60], "V3": [70, 80, 90]})

matriz_freq_1 = pd.DataFrame()
matriz_freq_1["a"] = matriz_a.iloc[0]
matriz_freq_1["b"] = matriz_b.iloc[0]
matriz_freq_1["c"] = matriz_c.iloc[0]
print(matriz_freq_1)

matriz_freq_2 = pd.DataFrame()
matriz_freq_2["a"] = matriz_a.iloc[1]
matriz_freq_2["b"] = matriz_b.iloc[1]
matriz_freq_2["c"] = matriz_c.iloc[1]
print(matriz_freq_2)

matriz_freq_3 = pd.DataFrame()
matriz_freq_3["a"] = matriz_a.iloc[2]
matriz_freq_3["b"] = matriz_b.iloc[2]
matriz_freq_3["c"] = matriz_c.iloc[2]
print(matriz_freq_3)
