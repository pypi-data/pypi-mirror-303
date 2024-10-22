import numpy as np

# Generalisation de la methode de Newton-Raphson pour un systeme de n equations
X = np.array([1.2, 0.9])
x, y = X[0], X[1]

def g1(x, y):
    return 2*x + 4*y - 2

def g2(x, y):
    return -2 * y + 4*x

for i in range(10):
    Jg = np.array([[2, 4], [4,-2]])     # Jacobienne de g

    G = np.array([g1(x,y), g2(x,y)])

    X -= np.linalg.inv(Jg).dot(G)       # X = X - Jg^-1 * G

    x, y = X[0], X[1]

print("x,y :", X)