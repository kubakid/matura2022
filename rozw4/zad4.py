def a():
    with open('dane4.txt', 'r') as file:
        dane = file.readlines()
    for i in range(len(dane)):
        dane[i] = dane[i].rstrip()
    maks = 0
    min = 10000000000
    for i in range(len(dane)-1):
        a = abs(int(dane[i])- int(dane[i+1]))
        if a > maks:
            maks = a
        if a < min:
            min = a
    print(maks)
    print(min)


a()


def b():
    with open('dane4.txt', 'r') as file:
        dane = file.readlines()
    for i in range(len(dane)):
        dane[i] = dane[i].rstrip()
    maksciag = []
    maks = 1
    akt = 1
    aktciag = []
    wartosc = abs(int(dane[0])- int(dane[1]))
    for i in range(1, len(dane)-1):
        a = abs(int(dane[i])- int(dane[i+1]))
        if wartosc == a:
            akt += 1
            aktciag.append(int(dane[i]))
        else:
            if akt > maks:
                aktciag.append(int(dane[i]))
                maks = akt
                maksciag = aktciag
            akt = 1
            aktciag = []
        wartosc = a
    print(maks)
    print(maksciag)



b()


def c():
    with open('dane4.txt', 'r') as file:
        dane = file.readlines()
    for i in range(len(dane)):
        dane[i] = dane[i].rstrip()
    slownik = {}
    for i in range(len(dane)-1):
        a = abs(int(dane[i])-int(dane[i+1]))
        if a in slownik:
            slownik[a] += 1
        else:
            slownik[a] = 1
    maks = 0
    for i in slownik:
        if slownik[i] > maks:
            maks = slownik[i]
    print(maks)
    for i in slownik:
        if slownik[i] == maks:
            print(i)



c()


