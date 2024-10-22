import numpy as np



SystemU = (np.array([[2,4,-6],[0,-1,1],[0,0,-2]]),np.array([2,3,-7]))
SystemL = (np.array([[2,0,0],[4,-1,0],[-6,1,-2]]),np.array([2,3,-7]))

def remontee(System):
    n = len(System[1])
    Sols = np.zeros(System[1].shape)
    for i in reversed(range(n)):

        Const = sum([System[0][i][j]*Sols[j] for j in range(i+1,n)])
        NRes = System[1][i]-Const
        Sols[i] = NRes/System[0][i][i]
    return Sols

def descente(System):
    n = len(System[1])
    Sols = np.zeros(System[1].shape)
    for i in range(n):
        Const = sum([System[0][i][j]*Sols[j] for j in range(i)])
        NRes = System[1][i]-Const
        Sols[i] = NRes/System[0][i][i]
    return Sols 

SystemD = (np.array([[1,1,1,1],[1,5,5,5],[1,5,14,14],[1,5,14,15]],dtype=np.float32),np.array([1,0,0,0],dtype=np.float32))
def triangularize(System):

    n = len(System[1])
    nSys = System
    for i in range(n-1):
        for j in range(i+1,n):
            facteur = - nSys[0][j][i]/nSys[0][i][i]
            nSys[1][j]=nSys[1][j]+ facteur*nSys[1][i]
            for k in range(i,n):
                nSys[0][j][k] = nSys[0][j][k] + facteur*nSys[0][i][k]
            nSys[0][j][i]=0
    return nSys


def CalcJacobi(Xnm1,T1,T2):
    return np.linalg.matmul(T1, Xnm1) + T2

def JacobiN(X,T1,T2,n):
    if n==0:
        return X
    Xnm1 = JacobiN(X,T1,T2,n-1)
    return CalcJacobi(Xnm1,T1,T2)


def JacobiRec(system,n):
    A = system[0]
    B = system[1]
    D = np.diag(np.diag(A))
    L = np.tril(A, k=-1)
    U = np.triu(A, k=1)
    invD = np.linalg.inv(D)
    T1 = np.linalg.matmul( invD, L + U)
    T2 = np.linalg.matmul(invD,B)
    X = np.zeros(len(B))
    return JacobiN(X,T1,T2,n)


def calcR(X,A,B):
    rk = B - np.linalg.matmul(A,X)
    return np.linalg.norm(rk)/np.linalg.norm(B)


def Jacobi(system,epsilon):
    A = system[0]
    B = system[1]
    D = np.diag(np.diag(A))
    print(D)
    L = -np.tril(A,k=-1)
    U = -np.triu(A,k=1)
    invD = np.linalg.inv(D)
    print(invD)
    T1 = np.linalg.matmul(invD, L + U)

    T2 = np.linalg.matmul(invD,B)
    X=np.zeros(len(B))
    while(calcR(X,A,B)>epsilon):
        X = np.linalg.matmul(T1,X)+T2

    return X

def Gaussiedel(system,epsilon):
    A = system[0]
    B = system[1]
    D = np.diag(np.diag(A))
    L = -np.tril(A,k=-1)
    U = -np.triu(A,k=1)
    invDML = np.linalg.inv(D-L)
    T1 = np.linalg.matmul(invDML, U)
    T2 = np.linalg.matmul(invDML, B)
    X=np.zeros(len(B))
    while(calcR(X,A,B)>epsilon):
        X = np.linalg.matmul(T1,X)+T2

    return X

def Relax(system,epsilon,omega):
    A = system[0]
    B = system[1]
    D = np.diag(np.diag(A))
    L = -np.tril(A,k=-1)
    U = -np.triu(A,k=1)
    invDML = np.linalg.inv(D-L)
    T1 = np.linalg.matmul(invDML, U)
    T2 = np.linalg.matmul(invDML, B)
    X=np.zeros(len(B))
    Xrel = np.zeros(len(B))
    while(calcR(Xrel,A,B)>epsilon):
        Xk = X
        X = np.linalg.matmul(T1,X)+T2
        Xrel = Xk - omega * (X-Xk)

    return Xrel

SystemJ = (np.array([[-6,1,-1,0],[1,4,0,1],[-1,0,-6,2],[0,1,2,6]]),np.array([-3,9,-2,0]))

# (x-x1)²-(x-x2)² + ... = d1²-d2²
# 2xx1+x1²+ 2xx2-x2²

atrianguler = (np.array([2.8,14,4]),np.array([10.2,13,15]),np.array([5.2,7,3.5]))

def linearise(system):

    B = np.array([system[2][i]**2-system[0][i]**2-system[1][i]**2 for i in range(3)])
    A = np.array([[-2*system[0][i],-2*system[1][i],1]for i in range(3)])

    return (A,B)

def tripolarise(system):
    linsys=linearise(system)

    trisys=triangularize(linsys)
    return remontee(trisys)

print(tripolarise(atrianguler))













