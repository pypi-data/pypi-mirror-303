import numpy as np  

# (x -xi)² + (y - yi)² = di²
#  x² - 2xix + x²i² + y² - 2yiy + y²i² = di²
# -2xix - 2yiy + x² + y² = di² - (xi² - yi²)
# -2xix -2yiy + di = di² - (xi² - yi²)

# x1 = (x - 2,8)^2 + (y - 10,2)^2 = (5,2)^2
# x2 = (x - 14)^2 + (y - 13)^2 = 7^2
# x3 = (x - 4)^2 + (y - 15)^2 = (3,5)^2

x = np.array([2.8, 14, 4])
y = np.array([10.2, 13, 15])
d = np.array([5.2, 7, 3.5])

X = np.array([[x], [y], [d**2]])

A = np.array([[-2*x[0], -2*y[0], 1],
              [-2*x[1], -2*y[1], 1],
              [-2*x[2], -2*y[2], 1]])

B = np.array([
    d[0]**2 - x[0]**2 - y[0]**2,
    d[1]**2 - x[1]**2 - y[1]**2,
    d[2]**2 - x[2]**2 - y[2]**2
])

def gauss(A, B):
    """
    Applique la méthode de Gauss pour triangulariser le système AX = B.
    A: Matrice des coefficients (de taille n x n)
    B: Vecteur des constantes (de taille n x 1)
    """
    n = len(B)
    
    # Combiner A et B dans une matrice augmentée
    Ab = np.hstack([A, B.reshape(-1, 1)])

    # Triangularisation (Réduction échelonnée)
    for i in range(n):
        # Trouver le pivot
        if Ab[i, i] == 0:
            raise ValueError("La méthode de Gauss ne peut pas être appliquée (pivot nul détecté).")
        
        # Elimination de Gauss
        for j in range(i + 1, n):
            facteur = Ab[j, i] / Ab[i, i]
            Ab[j, i:] = Ab[j, i:] - facteur * Ab[i, i:]
    
    # Substitution arrière pour obtenir les solutions
    X = np.zeros(n)
    for i in range(n - 1, -1, -1):
        X[i] = (Ab[i, -1] - np.dot(Ab[i, i+1:n], X[i+1:])) / Ab[i, i]
    return X

def tripolation():

    X = gauss(A, B)
    x, y = X[0], X[1]
    print(f"Position du telephone portable : (x, y) = ({x}, {y})")

tripolation()

# def gauss(A, B):
#     n = len(B)
#     Ab = np.hstack([A, B.reshape(-1, 1)])

#     for i in range (n):
#         if(Ab[i,i] == 0 ):
#             raise ValueError("POPOOSIBLE")

#         for j in range (i+1,n):
#             facteur = Ab[j,i]/Ab[i,i]
#             Ab[j,i:] = Ab[j,i:] - facteur * Ab[i,i:]

#     X = np.zeros(n)
#     for i in range (n-1, -1, -1):
#         X[i] = (Ab)