import math

with open("liczby.txt", "r") as plik:
    dane = plik.readlines()

    for i in range(len(dane)):
        dane[i] = int(dane[i].rstrip())

    nwd = dane[0]
    dlugoscCiagu = 0
    maksi = 0
    for i in range(len(dane)):
        nwd = math.gcd(nwd, dane[i])
        if nwd > 1:
            dlugoscCiagu += 1
            if dlugoscCiagu > maksi:
                maksi = dlugoscCiagu
        else:
            dlugoscCiagu = 0
            nwd = dane[i]

    print(maksi)