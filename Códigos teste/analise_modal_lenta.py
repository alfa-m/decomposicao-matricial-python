import pandas as pd
import numpy as np

matriz_a = pd.DataFrame({"V1": [1, 2, 3], "V2": [4, 5, 6], "V3": [7, 8, 9]})
matriz_b = pd.DataFrame({"V1": [-1, -2, -3], "V2": [-4, -5, -6], "V3": [-7, -8, -9]})
matriz_c = pd.DataFrame({"V1": [10, 20, 30], "V2": [40, 50, 60], "V3": [70, 80, 90]})

matriz_freq_1 = pd.DataFrame()
matriz_freq_1["a"] = matriz_a.iloc[0]
matriz_freq_1["b"] = matriz_b.iloc[0]
matriz_freq_1["c"] = matriz_c.iloc[0]

matriz_freq_2 = pd.DataFrame()
matriz_freq_2["a"] = matriz_a.iloc[1]
matriz_freq_2["b"] = matriz_b.iloc[1]
matriz_freq_2["c"] = matriz_c.iloc[1]

matriz_freq_3 = pd.DataFrame()
matriz_freq_3["a"] = matriz_a.iloc[2]
matriz_freq_3["b"] = matriz_b.iloc[2]
matriz_freq_3["c"] = matriz_c.iloc[2]

matriz_freq_1_numpy = matriz_freq_1.to_numpy()
matriz_freq_2_numpy = matriz_freq_2.to_numpy()
matriz_freq_3_numpy = matriz_freq_3.to_numpy()

autovalores_matriz_freq_1_numpy, autovetores_matriz_freq_1_numpy = np.linalg.eig(matriz_freq_1_numpy)
matriz_freq_1_diagonal_numpy = np.diag(autovalores_matriz_freq_1_numpy)

autovalores_matriz_freq_2, autovetores_matriz_freq_2 = np.linalg.eig(matriz_freq_2_numpy)
matriz_freq_2_diagonal = np.diag(autovalores_matriz_freq_2)

autovalores_matriz_freq_3, autovetores_matriz_freq_3 = np.linalg.eig(matriz_freq_3_numpy)
matriz_freq_3_diagonal = np.diag(autovalores_matriz_freq_3)

autovalores_matriz_freq_1, autovetores_matriz_freq_1 = np.linalg.eig(matriz_freq_1_numpy)
matriz_freq_1_diagonal = np.diag(autovalores_matriz_freq_1)

print("Matriz Z com harmônico 1 com numpy:\n", matriz_freq_1_numpy)
print("Matriz Z diagonal:\n", matriz_freq_1_diagonal_numpy)
print("Autovetores da matriz Z:\n", autovetores_matriz_freq_1_numpy)

print("Matriz Z com harmônico 1 sem numpy:\n", matriz_freq_1)
print("Matriz Z diagonal:\n", matriz_freq_1_diagonal)
print("Autovetores da matriz Z:\n", autovetores_matriz_freq_1)