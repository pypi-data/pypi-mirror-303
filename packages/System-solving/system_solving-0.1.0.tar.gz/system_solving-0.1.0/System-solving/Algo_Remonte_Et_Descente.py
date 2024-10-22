import numpy as np

L = np.array([[2,0,0],
              [4,-1,0],
              [-6,1,-2]])

U = np.array([[2,4,-6],
              [0,-1,1],
              [0,0,-2]])

B = np.array([[2],
              [3],
              [-7]])

# A supposé inversible donc aucun des éléments diagonaux de L sont nul
# Algo de remonté : UX = B
def remontee():
    # Taille de la matrice
    n = U.shape[0]   
    X = np.zeros((n, 1))   
    # On commence par la dernière ligne et on remonte
    for i in range(n-1, -1, -1):
        X[i] = B[i]
        for j in range(i+1, n):
            X[i] -= U[i, j] * X[j]
        X[i] /= U[i, i]
    return X

def descente():
    # Taille de la matrice
    n = L.shape[0]   
    X = np.zeros((n, 1))   
    # On commence par la première ligne et on descend
    for i in range(n):   
        X[i] = B[i]
        for j in range(i):
            X[i] -= L[i, j] * X[j]
        X[i] /= L[i, i]
    return X

# X = remontee()
# X = descente()

# print("Solution X :")
# print(X)
