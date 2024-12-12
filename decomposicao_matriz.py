import numpy as np

matriz_original = np.array([[-5, 2, 7], [2, -2, 3], [1, 4, 7]])
autovalores, autovetores = np.linalg.eig(matriz_original)
matriz_diagonal = np.diag(autovalores)

print("Matriz original:\n", matriz_original)
print("Matriz decomposta:\n", matriz_diagonal)
print("Autovetores:\n", autovetores)