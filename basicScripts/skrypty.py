import math
def silnia(n):
    a = 1
    for i in range(2,n+1):
        a *= i
    return a

def silniarek(n):
    if n == 0:
        return 1
    return silniarek(n-1) * n

def sumacyfr(n):
    suma = 0
    while n != 0:
        suma += n % 10
        n //= 10
    return suma

def sumcyfrrek(n):
    if n == 0:
        return 0
    return n % 10 + sumcyfrrek(n//10)

def czypierwsza(n):
    if n < 2:
        return "NIE"
    for i in range(2, math.ceil(math.sqrt(n))+1):
        if n % i == 0:
            return "NIE"
    return "TAK"

def nwd(a,b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def nwdrek(a,b):
    if b == 0:
        return a
    return nwdrek(b, a%b)

def nww(a,b):
    return(a*b//nwd(a,b))


def binarysearch(a, b):
    l = 0
    p = len(b)
    while l < p:
        s = (l + p) // 2
        if b[s] == a:
            return s
        elif b[s] < a:
            l = s + 1
        else:
            p = s
    return -1

print(binarysearch(5,[1,2,3,4,5,6,7,8]))

