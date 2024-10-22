import numpy as np

## TP 1 Ex1
L = np.array([[2, 0, 0], [4, -1, 0], [-6, 1, -2]])
U = np.array([[2, 4, -6], [0, -1, 1], [0, 0, -2]])
B = np.array([[2], [3], [-7]])
def remontee(A, B):
    size = len(A)
    X = np.zeros([3,1])
    if A[size-1,size-1] != 0:
        X[size-1,0] = B[size-1,0] / A[size-1,size-1]
    for i in range(size-1, -1, -1):
        somme = 0
        for j in range(i+1, size):
            somme += A[i,j] * X[j,0]
        X[i, 0] = (B[i, 0] - somme)/A[i,i]
    print(X)

def descente(A, B):
    size = len(A)
    X = np.zeros([3,1])
    if A[0,0] != 0:
        X[0,0] = B[0,0] / A[0,0]
    for i in range(0, size):
        somme = 0
        for j in range(0, i):
            somme += A[i,j] * X[j,0]
        X[i, 0] = (B[i,0]-somme)/A[i,i]
    print(X)


#remontee(U, B)
#descente(L, B)


## TP 1 Ex 2
A = np.array([
    [1,1,1,1],
    [1,5,5,5],
    [1,5,14,14],
    [1,5,14,15]])
B = np.array([[1],[0],[0],[0]])

def gauss(A, B):
    n = len(B)
    A = A.astype(float)
    B = B.astype(float)
    for i in range(n):
        max_row = np.argmax(abs(A[i:, i])) + i
        if i != max_row:
            A[[i, max_row]] = A[[max_row, i]]
            B[[i, max_row]] = B[[max_row, i]]
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            B[j] -= factor * B[i]
    return A, B

def cholesky(A):
    size = len(A)
    for i in range(size):
        for j in range(size):
            if A[i,j] != A[j,i]:
                print("La matrice n'est pas symétrique")
                return A
    L = np.zeros_like(A)
    for i in range(size):
        somme_diagonale = sum(L[i, k] ** 2 for k in range(i))
        L[i, i] = np.sqrt(A[i, i] - somme_diagonale)

        for j in range(i + 1, size):
            somme_hors_diagonale = sum(L[j, k] * L[i, k] for k in range(i))
            L[j, i] = (A[j, i] - somme_hors_diagonale) / L[i, i]

    return L

#At, Bt = gauss(A, B)
# L = cholesky(A)
# print(L)

## TP 1 Ex 2

A = np.array([
    [-6, 1, -1, 0],
    [1, 4, 0, 1],
    [-1, 0, -6, 2],
    [0, 1, 2, 6]])
B = np.array([[-3], [9], [-2], [0]])

def jacobi(A, B):
    length = len(A)
    D = np.diag(np.diag(A))
    L = np.tril(A, -1)
    U = np.triu(A, 1)

    Xk = np.zeros([length, 1])

    R = np.linalg.norm(B - np.dot(A, Xk))
    T1 = np.dot(np.linalg.inv(D), (L + U))
    T2 = np.dot(np.linalg.inv(D), B)

    epsilon = 0.01
    while R > epsilon:
        Xk = np.dot(T1, Xk) + T2
        R = np.linalg.norm(B - np.dot(A, Xk))
    return Xk, R


# X, R = jacobi(A, B)
# print("X :", X)
# print("R :", R)

## Tp 1 Ex 3
Tab = np.array([
    [2.8, 14, 4],
    [10.2, 13, 15],
    [5.2, 7, 3.5]])


A = np.array([
    [-2*Tab[0,0], -2*Tab[1,0], 1],
    [-2*Tab[0,1], -2*Tab[1,1], 1],
    [-2*Tab[0,2], -2*Tab[1,2], 1]
])

B = np.array([
    [np.pow(Tab[2,0],2) - np.pow(Tab[0,0],2) - np.pow(Tab[1,0],2)],
    [np.pow(Tab[2,1],2) - np.pow(Tab[0,1],2) - np.pow(Tab[1,1],2)],
    [np.pow(Tab[2,2],2) - np.pow(Tab[0,2],2) - np.pow(Tab[1,2],2)]
])


A, B = gauss(A, B)
remontee(A, B)