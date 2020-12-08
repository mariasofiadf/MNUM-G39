"""
x é o valor inicial e xf o valor final
n é o número de iterações
df é a derivada da função
"""
def rk4(x, xf, n, df):
    h = (xf-x)/n
    y = 1
    for i in range(0,n):
        d1 = h * df(x,y)
        d2 = h * df(x + h/2, y + d1/2)
        d3 = h * df(x + h/2, y + d2/2)
        d4 = h * df(x + h, y + d3)
        dy = d1/6 + d2/3 + d3/3 + d4/6
        x += h
        y += dy
        print("x: ", x, " y: ", y)