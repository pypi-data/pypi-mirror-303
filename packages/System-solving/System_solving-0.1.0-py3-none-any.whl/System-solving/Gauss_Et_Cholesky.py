import numpy as np

def gauss(A, B):
    """ Applique la méthode de Gauss pour triangulariser le système AX = B.
    A: Matrice des coefficients (de taille n x n)
    B: Vecteur des constantes (de taille n x 1) """

    # Combiner A et B dans une matrice augmentée
    n = len(B)
    Ab = np.hstack([A, B.reshape(-1, 1)])  # Ajout de B comme colonne à A

    # Triangularisation (Réduction échelonnée)
    for i in range(n):
        # Trouver le pivot
        if Ab[i, i] == 0:
            raise ValueError("La methode de Gauss ne peut pas etre appliquee (pivot nul detecte).")
        
        # Elimination de Gauss
        for j in range(i + 1, n):
            facteur = Ab[j, i] / Ab[i, i]
            Ab[j, i:] = Ab[j, i:] - facteur * Ab[i, i:]
    
    # Séparer à nouveau la matrice A et le vecteur B
    A_triangular = Ab[:, :-1]
    B_triangular = Ab[:, -1]

    return A_triangular, B_triangular

# Définir les matrices A et B
A = np.array([[1, 1, 1, 1],
              [1, 5, 5, 5],
              [1, 5, 14, 14],
              [1, 5, 14, 15]], dtype=float)

B = np.array([[1], [0], [0], [0]], dtype=float)

# Appeler la fonction de triangularisation
A_triangular, B_triangular = gauss(A, B)

# Afficher les résultats
print("Matrice triangulaire A:")
print(A_triangular)
print("\nVecteur B apres triangularisation:")
print(B_triangular)


def is_positive_definite(A):
    """Vérifie si la matrice est définie positive"""
    return np.all(np.linalg.eigvals(A) > 0)

# Vérifions la symétrie et si A est définie positive
if np.allclose(A, A.T) and is_positive_definite(A):
    print("La matrice A est symetrique et definie positive.")
else:
    print("La matrice A ne satisfait pas aux conditions pour Cholesky.")

def cholesky(A):
    n = A.shape[0]
    L = np.zeros_like(A)

    for i in range(n):
        for j in range(i+1):
            if i == j:
                L[i, j] = np.sqrt(A[i, i] - np.sum(L[i, :i]**2))
            else:
                L[i, j] = (A[i, j] - np.sum(L[i, :j] * L[j, :j])) / L[j, j]
    return L

def forward_substitution(L, B):
    """Résout LY = B où L est triangulaire inférieure."""
    n = L.shape[0]
    Y = np.zeros_like(B)

    for i in range(n):
        Y[i] = (B[i] - np.dot(L[i, :i], Y[:i])) / L[i, i]

    return Y

def backward_substitution(L_T, Y):
    """Résout L^T X = Y où L^T est triangulaire supérieure."""
    n = L_T.shape[0]
    X = np.zeros_like(Y)

    for i in range(n-1, -1, -1):
        X[i] = (Y[i] - np.dot(L_T[i, i+1:], X[i+1:])) / L_T[i, i]

    return X

# Si la matrice est définie positive, appliquez Cholesky
if np.allclose(A, A.T) and is_positive_definite(A):
    L = cholesky(A)
    print("Matrice L (Cholesky):")
    print(L)

    # Résoudre le système AX = B
    # Étape 1: Résoudre LY = B (substitution avant)
    Y = forward_substitution(L, B)

    # Étape 2: Résoudre L^T X = Y (substitution arrière)
    X = backward_substitution(L.T, Y)

    print("Solution X:")
    print(X)
else:
    print("La méthode de Cholesky ne peut pas être appliquée à cette matrice.")

# # Si la matrice est définie positive, appliquez Cholesky
# if np.allclose(A, A.T) and is_positive_definite(A):
#     L = cholesky(A)
#     print("Matrice L (Cholesky):")
#     print(L)
# else:
#     print("La methode de Cholesky ne peut pas être appliquee à cette matrice.")
