import numpy as np

# def Jacobi(A, B, R, epsilon):
#     k = 1
#     X(:,k) = np.zeros(n,1)
#     R(k) = np.norm (B - A*X)
#     T1 = np.inv(D)*(L+U)
#     T2 = np.inv(D)*B
#     while R(k > epsilon):
#         X(:,k+1) = T1*X(:,k) + T2
#         R(k+1) = np.norm(B - A*X(:,k+1))
#         k = k + 1
#     X_Jacobi = X
#     Rjacobi = R
#     return X_Jacobi, Rjacobi

def Jacobi_moi(A, B, X0, epsilon, max_iter):
    
    D = np.diag(np.diag(A))      # Matrice diagonale de A
    L = -np.tril(A, -1)          # Partie strictement inférieure à la diagonale
    U = -np.triu(A, 1)           # Partie strictement supérieure à la diagonale

    if np.sum(D >= np.sum(np.abs(A - D), axis = 1)) == len(A):
        print("La matrice A est diagonalement dominante, donc la méthode de Jacobi converge.")
    else :
        print("La matrice A n'est pas diagonalement dominante, donc la methode de Jacobi pourrait ne pas converger.")

    D_inv = np.linalg.inv(D)    # Inverse de la matrice diagonale
    X = X0.copy()               # Initialisation de X
    norm_B = np.linalg.norm(B)  # Norme du vecteur B pour la condition d'arrêt
    k = 0                       # Compteur d'itérations

    while (k < max_iter):
        X_new = D_inv @ (L + U) @ X + D_inv @ B   # le @ signifie produit matriciel
        r = B - A @ X_new
        if np.linalg.norm(r) / norm_B < epsilon:
            break
        X = X_new
        k += 1
    
    return X, k


def is_diagonally_dominant(A):
    """Vérifie si la matrice A est diagonale dominante."""
    for i in range(A.shape[0]):
        diag = abs(A[i, i])
        off_diag_sum = np.sum(np.abs(A[i, :])) - diag
        if diag <= off_diag_sum:
            return False
    return True

def GaussSeidel(A, B, X0, epsilon, max_iter):
    D = np.diag(np.diag(A))
    L = -np.tril(A, -1)         # Partie strictement inférieure à la diagonale
    U = -np.triu(A, 1)          # Partie strictement supérieure à la diagonale
    X = X0.copy()               
    norm_B = np.linalg.norm(B)
    inv_DL = np.linalg.inv(D - L)
    k = 0
    while k < max_iter:
        x_new = inv_DL @ U @ X + inv_DL @ B
        r = B - A @ x_new
        while np.linalg.norm(r) / norm_B < epsilon:
            break
        X = x_new
        k += 1
    return X, k

# Version sans inversion de matrice :
# def GaussSeidel(A, B, X0, epsilon, max_iter):
#     n = A.shape[0]            # Taille de la matrice
#     X = X0.copy()              # Copie du vecteur initial X0
    
#     norm_B = np.linalg.norm(B)  # Norme de B pour le critère de convergence
    
#     k = 0                      # Compteur d'itérations
#     while k < max_iter:
#         X_new = X.copy()        # Copie de X pour l'itération k+1
        
#         for i in range(n):
#             # Calcul des sommes pour les parties inférieure et supérieure
#             sum1 = np.dot(A[i, :i], X_new[:i])   # Somme des éléments de L (partie inférieure)
#             sum2 = np.dot(A[i, i+1:], X[i+1:])   # Somme des éléments de U (partie supérieure)
            
#             # Mise à jour de l'élément X[i]
#             X_new[i] = (B[i] - sum1 - sum2) / A[i, i]
        
#         # Calcul du résidu
#         r = B - A @ X_new
        
#         # Vérification du critère de convergence
#         if np.linalg.norm(r) / norm_B < epsilon:
#             break
        
#         X = X_new    # Mise à jour de X pour la prochaine itération
#         k += 1       # Incrémentation du compteur d'itérations
#     return X, k

def relaxation(A, B, X0, omega, epsilon, max_iter):
    n = len(B)
    X = X0.copy()

    D = np.diag(np.diag(A))   # Diagonale de A
    L = np.tril(A, -1)        # Partie inférieure de A
    U = np.triu(A, 1)         # Partie supérieure de A

    norm_B = np.linalg.norm(B)
    inv_DL = np.linalg.inv(D - L)
    k = 0

    while k < max_iter:
        x_new = inv_DL @ (U @ X + B)
        r = B - A @ x_new
        if np.linalg.norm(r) / norm_B < epsilon:
            break
        X = (1-omega) * X + omega * x_new       # Application du facteur de relaxation
        k += 1

    return X, k



if __name__ == "__main__":

    A = np.array([[4, -1, 0, 0],
                [-1, 4, -1, 0],
                [0, -1, 4, -1],
                [0, 0, -1, 3]], dtype=float)
    
    B = np.array([15, 10, 10, 10], dtype=float)

    A2 = np.array([[-6, 1, -1, 0],
                   [1, 4, 0, 1],
                   [-1, 0, -6, 2],
                   [0, 1, 2, 6]], dtype=float)
    
    B2 = np.array([-3, 9, -2, 0], dtype=float)

    X0 = np.zeros_like(B)
    epsilon = 1e-6
    max_iter = 1000

    X, k = Jacobi_moi(A2, B2, X0, epsilon, max_iter)
    print("Solution du systeme AX = B:")
    print(X)
    print(f"Nombre d'iterations: {k}")

    if is_diagonally_dominant(A2):
        print("La matrice A est diagonalement dominante.")
        X, k = GaussSeidel(A, B, X0, epsilon, max_iter)
        print("Solution du systeme AX = B:")
        print(X)
        print(f"Nombre d'iterations: {k}")
    else:
        print("La matrice A n'est pas diagonalement dominante.")

    omega = 1.5
    X, k = relaxation(A, B, X0, omega, epsilon, max_iter)
    print("Solution du systeme AX = B:")
    print(X)
    print(f"Nombre d'iterations: {k}")
