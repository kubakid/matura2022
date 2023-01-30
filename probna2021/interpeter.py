import string
def a():
    with open('napisy.txt', 'r') as file:
        napisy = file.readlines()
    for i in range(len(napisy)):
        napisy[i] = napisy[i].rstrip()
    suma = 0
    cyfry = list("0123456789")
    for i in napisy:
        a = list(i)
        for j in a:
            if j in cyfry:
                suma += 1
    print(suma)

a()


def b():
    with open('napisy.txt', 'r') as file:
        napisy = file.readlines()
    for i in range(len(napisy)):
        napisy[i] = napisy[i].rstrip()
    haslo = ""
    pozycja = 0
    for i in range(19, len(napisy),20):
        haslo += napisy[i][pozycja]
        pozycja += 1
    print(haslo)


b()


def c():
    with open('napisy.txt', 'r') as file:
        napisy = file.readlines()
    for i in range(len(napisy)):
        napisy[i] = napisy[i].rstrip()
    haslo = ''
    for i in napisy:
        palindrom = True
        first = i[0]
        last = i[-1]
        a = list(last + i)
        b = list(i+ first)
        a1 = a
        b1 = b
        for j in range(26):
            if a[0] == a[-1]:
                a = a[1:-1]
            else:
                palindrom = False
                break
        suma = 0
        if palindrom:
            haslo += a1[25]
            continue
        else:
            for j in range(26):
                if b[0] == b[-1]:
                    b = b[1:-1]
                    suma += 1
                else:
                    break
        if suma == 26:
            haslo += b1[25]
    print(haslo)


c()


def d():
    with open('napisy.txt', 'r') as file:
        napisy = file.readlines()
    for i in range(len(napisy)):
        napisy[i] = napisy[i].rstrip()
    koniec = ""
    haslo = list()
    licznikx = 0
    slownik = {}
    litery = list(string.ascii_uppercase)
    wartosc = 65
    for i in litery:
        slownik[wartosc] = i
        wartosc += 1
    for i in napisy:
        aktualnecyfry = ''
        for j in range(len(i)):
            if 47 < ord(i[j]) < 58:
                aktualnecyfry += i[j]
        if len(aktualnecyfry) % 2 == 1:
            aktualnecyfry = aktualnecyfry[0:-1]
        haslo += aktualnecyfry
    while licznikx != 3:
        a = int(haslo[0] + haslo[1])
        haslo = haslo[2:]
        if 64 < a < 91:
            koniec += slownik[a]
        if a == 88:
            licznikx += 1
        else:
            licznikx = 0
    print(koniec)




d()

