import numpy as np
import matplotlib.pyplot as plt

# METHODE DE DICHOTOMIE :
def f(x):
    return x**3 - x - 1

a, b = 1, 2
epsilon = 0.0001

while b-a >= epsilon:
    x_mid = (b+a)/2  # Point milieu

    if f(a) * f(x_mid) < 0 :
        b = x_mid
    else:
        a = x_mid

print(f"Solution :  {x_mid}")


# METHODE GRAPHIQUE :
x = np.linspace(0, 2, 1000)

y1 = x**3
y2 = x+1

plt.plot(x,y1,'b', label='y = x^3')
plt.plot(x, y2, 'r', label='x+1')
plt.title('METHODE GRAPGIQUE')
plt.grid('true')
plt.show()