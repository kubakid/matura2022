def a():
    with open("PARY_LICZB.TXT", "r") as file:
        pary = file.readlines()
    for i in range(len(pary)):
        pary[i] = pary[i].rstrip()
    wielokrotnosc = 0
    for i in pary:
        przerwa = i.index(" ")
        pierwsza = i[:przerwa]
        druga = i[przerwa+1:]
        if int(pierwsza) % int(druga) == 0:
            wielokrotnosc += 1
        elif int(druga) % int(pierwsza) == 0:
            wielokrotnosc += 1
    print(wielokrotnosc)


def nwd(a, b):
    if b > 0:
        return nwd(b, a%b)
    return a


def b():
    with open("PARY_LICZB.TXT", "r") as file:
        pary = file.readlines()
    for i in range(len(pary)):
        pary[i] = pary[i].rstrip()
    spelniony_warunek = 0
    for i in pary:
        przerwa = i.index(" ")
        pierwsza = i[:przerwa]
        druga = i[przerwa+1:]
        if nwd(int(pierwsza), int(druga)) == 1:
            spelniony_warunek += 1
    print(spelniony_warunek)

def suma_cyfr(n):
    wynik = 0
    while n != 0:
        wynik += n % 10
        n = n // 10
    return wynik

def c():
    with open("PARY_LICZB.TXT", "r") as file:
        pary = file.readlines()
    for i in range(len(pary)):
        pary[i] = pary[i].rstrip()
    rowne = 0
    for i in pary:
        przerwa = i.index(" ")
        pierwsza = i[:przerwa]
        druga = i[przerwa+1:]
        if suma_cyfr(int(pierwsza)) == suma_cyfr(int(druga)):
            rowne += 1
    print(rowne)


a()

b()

c()







