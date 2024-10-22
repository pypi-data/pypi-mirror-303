import numpy as np
def f(x):
    return x**3-x-1
def fprime(x):
    return 3*(x**2)-1
def func(x):
    return np.exp(x)-2*np.cos(x)
def funcprime(x):
    return np.exp(x)+2*np.sin(x)

def deuxvar(x,y):
    return x**3+y**2+2*x*y-x


def binarysearch(func,epsilon,intervalle):

    start, finish = intervalle[0],intervalle[1]

    while finish-start >= epsilon:
        mid = (start+finish)/2

        if func(start)*func(mid)<0:
            finish=mid
        else :
            start = mid

    return mid

def newtonrhapson(func,funcprime,xinit,epsilon):
    x=xinit
    while abs(func(x))>epsilon:
        x = x-(func(x)/funcprime(x))
    return x


print(newtonrhapson(func,funcprime,1.5,0.0001))