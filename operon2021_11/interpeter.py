import math
def sumkwcyfr(n):
    suma = 0
    while n != 0:
        suma += (n % 10)**2
        n //= 10
    return suma

def czypierwsza(n):
    for i in range(2,math.ceil(math.sqrt(int(n)))+1):
        if int(n) % i == 0:
            return False
    return True


def a():
    maks = 1
    wyjscie = []
    for i in range(1,1001):
        lista = [i]
        b = True
        a = sumkwcyfr(i)
        while a != 0:
            lista.append(a)
            a = sumkwcyfr(a)
            if a in lista:
                if a != 1:
                    b = False
                break
        if len(lista) > maks and b == True:
            maks = len(lista)
        if len(lista) == 7:
            print(i, end=" ")
    print()
    print(maks)


a()


def b():
    with open('liczby.txt', 'r') as file:
        liczby = file.readlines()
    for i in range(len(liczby)):
        liczby[i] = liczby[i].rstrip()
    licznik = 0
    for i in liczby:
        lista = [i]
        b = True
        a = sumkwcyfr(int(i))
        while a != 1:
            lista.append(a)
            a = sumkwcyfr(a)
            if a in lista:
                b = False
                break
        if b:
            licznik += 1
    print(licznik)

b()


def c():
    with open('liczby.txt', 'r') as file:
        liczby = file.readlines()
    for i in range(len(liczby)):
        liczby[i] = liczby[i].rstrip()
    maks = 0
    licznik = 0
    listaakt = []
    makslista = []
    for i in range(len(liczby)):
        lista = [i]
        b = True
        a = sumkwcyfr(int(i))
        while a != 1:
            lista.append(a)
            a = sumkwcyfr(a)
            if a in lista:
                b = False
                break
        if b:
            licznik += 1
            listaakt.append(liczby[i])
        if not b:
            if licznik > maks:
                maks = licznik
                makslista = listaakt
            licznik = 0
            listaakt = []
    print(maks)
    print(makslista)


c()


def d():
    with open('liczby.txt', 'r') as file:
        liczby = file.readlines()
    for i in range(len(liczby)):
        liczby[i] = liczby[i].rstrip()
    licznik = 0
    for i in liczby:
        lista = [i]
        b = True
        a = sumkwcyfr(int(i))
        while a != 1:
            lista.append(a)
            a = sumkwcyfr(a)
            if a in lista:
                b = False
                break
        if b and czypierwsza(i):
            licznik += 1
    print(licznik)


d()

