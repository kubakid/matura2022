def sumacyfr(n):
    suma = 0
    a = int(n)
    while a != 0:
        suma += a % 10
        a //= 10
    return suma



def pierwsza(n):
    tak = True
    for i in range(2, int(n) - 1):
        if int(n) % i == 0:
            tak = False
            break
    return tak


def a():
    with open('liczby2019.txt', 'r') as file:
        liczby = file.readlines()
    for i in range(len(liczby)):
        liczby[i] = liczby[i].rstrip()
    for i in liczby:
        if pierwsza(i) and 100 < int(i) < 5000:
            print(i, end = " ")
    print()


a()


def b():
    with open('pierwsze.txt', 'r') as file:
        liczby = file.readlines()
    for i in range(len(liczby)):
        liczby[i] = liczby[i].rstrip()
    for i in liczby:
        a = i[::-1]
        if pierwsza(a):
            print(i, end=" ")
    print()



b()



def c():
    with open('pierwsze.txt', 'r') as file:
        liczby = file.readlines()
    for i in range(len(liczby)):
        liczby[i] = liczby[i].rstrip()
    licznik = 0
    for i in liczby:
        while int(i) > 9:
            i = sumacyfr(i)
        if i == 1:
            licznik += 1
    print(licznik)


c()


