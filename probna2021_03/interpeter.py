def a():
    with open('galerie.txt','r') as file:
        galerie = file.readlines()
    for i in range(len(galerie)):
        galerie[i]=galerie[i].rstrip()
    slownik = {}
    for i in range(len(galerie)):
        dane = galerie[i].split()
        if dane[0] not in slownik:
            slownik[dane[0]] = 1
        else:
            slownik[dane[0]] += 1
    for i in slownik:
        print(i, str(slownik[i]))



a()


def b():
    with open('galerie.txt','r') as file:
        galerie = file.readlines()
    for i in range(len(galerie)):
        galerie[i]=galerie[i].rstrip()
    miastomaks = ""
    maks = 0
    miastomin = ''
    min = 10000000000
    for i in galerie:
        dane = i.split()
        miasto = dane[1]
        c = 2
        d = 3
        a = dane[c]
        b = dane[d]
        indeks = 3
        suma = 0
        lokale = 70 - dane.count("0")//2
        while a != 0 and b != 0 and indeks + 2 < len(dane):
            suma += int(a) * int(b)
            c += 2
            d += 2
            a = dane[c]
            b = dane[d]
            indeks += 2
        if suma > maks:
            miastomaks = miasto
            maks = suma
        if suma < min:
            miastomin = miasto
            min = suma
        print(miasto, str(suma),str(lokale))

    print()
    print()
    print(miastomaks, str(maks))
    print(miastomin, str(min))

b()

def c():
    with open('galerie.txt','r') as file:
        galerie = file.readlines()
    for i in range(len(galerie)):
        galerie[i]=galerie[i].rstrip()
    miastomaks = ''
    maks = 0
    miastomin = ''
    min = 71
    for i in galerie:
        dane = i.split()
        miasto = dane[1]
        c = 2
        d = 3
        a = dane[c]
        b = dane[d]
        indeks = 3
        roznelokale = set()
        while a != 0 and b != 0 and indeks + 2 < len(dane):
            if int(a) * int(b) != 0:
                roznelokale.add(int(a)*int(b))
            c += 2
            d += 2
            a = dane[c]
            b = dane[d]
            indeks += 2
        if len(roznelokale) > maks:
            maks = len(roznelokale)
            miastomaks = miasto
        if len(roznelokale) < min:
            min = len(roznelokale)
            miastomin = miasto
    print()
    print(miastomaks, str(maks))
    print(miastomin, str(min))

c()