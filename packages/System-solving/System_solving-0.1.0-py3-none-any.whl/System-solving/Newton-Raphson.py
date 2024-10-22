import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - x - 1

def fprime(x):
    return 3*x**2 - 1

# # NEWTON-RAPHSON
# x = [3]
# epsilon = 0.00001
# it = 0
# erreur = []

# while abs(f(x[-1])) > epsilon:
#     it += 1
#     x_next = x[-1] - f(x[-1]) / fprime(x[-1])
#     x.append(x_next)
#     erreur.append(abs(f(x[-1])))

# xi = np.arange(it)
# print("Erreur : ", erreur)      # ERREUR
# print("Nbr iterations : ", it)  # NOMBRE D'ITERATIONS
# print(x[-1])                    # X[-1] PREND LA DERNIERE VALEUR DE LA LISTE X

# plt.plot(xi, erreur)
# plt.show()


#METHODE GRAPHIQUE
x = np.linspace(0,1,1000)       # 1000 points entre 0 et 1
y1 = np.exp(x)
y2 = 2*np.cos(x)

plt.plot(x, y1,'b')
plt.plot(x, y2,'r')
plt.title("METHODE GRAPHIQUE")
plt.show()

#METHODE DICHOTOMIE
def f2(x):
    return np.exp(x) - 2*np.cos(x)

def f2prime(x):
    return np.exp(x) + 2*np.sin(x)

def dichotomie(f2,a,b,epsilon):
    while b-a >= epsilon:
        x_mid = (a+b)/2
        if f2(a) * f2(x_mid) < 0:
            b = x_mid
        else:
            a = x_mid
    return x_mid

#METHODE NEWTON-RAPHSON
def newton_raphson(f2, f2prime, x0, epsilon):
    x = [x0]
    it = 0
    erreur = []
    while abs(f2(x[-1])) > epsilon:
        it += 1
        x_next = x[-1] - f2(x[-1]) / f2prime(x[-1]) # X[-1] PREND LA DERNIERE VALEUR DE LA LISTE X
        x.append(x_next)
        erreur.append(abs(f2(x[-1])))               # X[-1] PREND LA DERNIERE VALEUR DE LA LISTE X

    xi = np.arange(it)
    plt.plot(xi, erreur)
    plt.title('Courbe de convergence d erreur')
    plt.show()
    return x[-1]

print("\nQuestion b :")
print("dichotomie : ", dichotomie(f2, 0, 1, 0.0001))
print("\nQuestion c :")
print("newton-raphson : ", newton_raphson(f2, f2prime, 0, 0.0001))