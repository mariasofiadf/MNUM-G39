import math

def f(x):
    return  x - 2*math.log(x) - 5
#temos 2 zeros
def f_der(x):
    return 1 - 2/x

a = 0.001
b = 0.5
crit = 10**-4

def bissecao(a,b,crit):
    eps = (b-a)/a
    while(eps > crit):
        med = (a+b)/2
        if (f(med)*f(a)<0):
            b=med
        else:
            a=med
        eps = (b-a)/a
    return (a+b)/2

print("\nMetodo da Bissecao\nzero1: ", bissecao(0.001,1,crit))
print("zero2: ", bissecao(8,10,crit))


