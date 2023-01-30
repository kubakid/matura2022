def iteracjanwd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def rekurencjanwd(a, b):
    while b != 0:
        return rekurencjanwd(b, a % b)
    else:
        return a


def fib(n):
    lista = [1,1]
    for i in range(2, n):
        lista.append(lista[i-2]+lista[i-1])
    return lista[n-1]


def rekfib(n):
    if n == 1:
        wartosc = 1
    elif n == 2:
        wartosc = 1
    else:
        wartosc = rekfib(n-1) + rekfib(n-2)
    return wartosc





