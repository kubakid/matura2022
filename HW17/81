import math
def a():
    with open('wspolrzedne.txt', 'r') as file:
        wspolrzedne = file.readlines()
    for i in range(len(wspolrzedne)):
        wspolrzedne[i] = wspolrzedne[i].rstrip()
    ilosc = 0
    for i in wspolrzedne:
        dane = list(map(int, i.split()))
        xa, ya, xb, yb, xc, yc = dane
        if xa > 0 and xb > 0 and xc > 0 and ya >0 and yb >0 and yc > 0:
            ilosc += 1
    print(ilosc)


a()


def b():
    with open('wspolrzedne.txt', 'r') as file:
        wspolrzedne = file.readlines()
    for i in range(len(wspolrzedne)):
        wspolrzedne[i] = wspolrzedne[i].rstrip()
    ilosc = 0
    for i in wspolrzedne:
        dane = list(map(int, i.split()))
        xa, ya, xb, yb, xc, yc = dane
        if xb - xa == 0 and xc - xb == 0:
            ilosc += 1
        if yb - ya == 0 and yc - yb ==0:
            ilosc += 1
        if xb - xa == 0 or xc - xb == 0 or yb - ya == 0 or yc - yb == 0:
            continue
        a1 = (yb-ya)/(xb-xa)
        a2 = (yc - yb) / (xc - xb)
        if a1 == a2:
            ilosc += 1

    print(ilosc)



b()

def c():
    with open('wspolrzedneTR.txt', 'r') as file:
        wspolrzedne = file.readlines()
    for i in range(len(wspolrzedne)):
        wspolrzedne[i] = wspolrzedne[i].rstrip()
    obw = 0
    a = []
    b = []
    c = []
    for i in wspolrzedne:
        dane = list(map(int, i.split()))
        xa, ya, xb, yb, xc, yc = dane
        ab = math.sqrt((xb-xa)**2 + (yb - ya)**2)
        bc = math.sqrt((xc-xb)**2 +(yc-yb)**2)
        ac = math.sqrt((xc-xa)**2+(yc-ya)**2)
        if ab + bc + ac > obw:
            obw = ab + bc + ac
            a = [xa, ya]
            b = [xb, yb]
            c = [xc, yc]
    print(round(obw,2))
    print(a)
    print(b)
    print(c)


c()


def d():
    with open('wspolrzedneTR.txt', 'r') as file:
        wspolrzedne = file.readlines()
    for i in range(len(wspolrzedne)):
        wspolrzedne[i] = wspolrzedne[i].rstrip()
    ilosc = 0
    for i in wspolrzedne:
        dane = list(map(int, i.split()))
        xa, ya, xb, yb, xc, yc = dane
        ab = (xb-xa)**2 + (yb - ya)**2
        bc = (xc-xb)**2 +(yc-yb)**2
        ac = (xc-xa)**2+(yc-ya)**2
        if ab + bc == ac or ac + bc == ab or ab + ac == bc:
            ilosc += 1
    print(ilosc)


d()


def e():
    with open('wspolrzedneTR.txt', 'r') as file:
        wspolrzedne = file.readlines()
    for i in range(len(wspolrzedne)):
        wspolrzedne[i] = wspolrzedne[i].rstrip()
    lista = []
    for i in wspolrzedne:
        dane = list(map(int, i.split()))
        xa, ya, xb, yb, xc, yc = dane
        wektorx = xc - xb
        wektory = yc - yb
        xd = wektorx + xa
        yd = wektory + ya
        if xd == yd:
            lista.append(f'A[{xa}, {ya}], B[{xb}, {yb},], C[{xc}, {yc}], D[{xd}, {yd}]')
    for i in lista:
        print(i)


e()
