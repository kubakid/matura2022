import string
def a():
    with open('instrukcje.txt', 'r') as file:
        instrukcje = file.readlines()
    for i in range(len(instrukcje)):
        instrukcje[i] = instrukcje[i].rstrip()
    dlugosc = 0
    for i in instrukcje:
        if i[:-2] == "DOPISZ":
            dlugosc += 1
        elif i[:-2] == "USUN":
            dlugosc -= 1
    print(dlugosc)

a()


def b():
    with open('instrukcje.txt', 'r') as file:
        instrukcje = file.readlines()
    for i in range(len(instrukcje)):
        instrukcje[i] = instrukcje[i].rstrip()
    h = 0
    maks = 0
    rodzaj = ''
    for i in range(len(instrukcje)):
        if instrukcje[i-1][:-2] == instrukcje[i][:-2]:
            h += 1
            rodzaj = instrukcje[i][:-2]
        else:
            h = 1
        if h > maks:
            maks = h
    print(str(maks), rodzaj)

b()

def c():
    with open('instrukcje.txt', 'r') as file:
        instrukcje = file.readlines()
    for i in range(len(instrukcje)):
        instrukcje[i] = instrukcje[i].rstrip()
    litery = list(string.ascii_uppercase)
    lista = []
    for i in instrukcje:
        if i[-1] in litery and i[:-2] == "DOPISZ":
            lista.append(i[-1])
    maks = 0
    litera = ''
    for i in lista:
        wartosc = lista.count(i)
        if wartosc > maks:
            maks = wartosc
            litera = i
    print(maks)
    print(litera)


c()


def d():
    with open('instrukcje.txt', 'r') as file:
        instrukcje = file.readlines()
    for i in range(len(instrukcje)):
        instrukcje[i] = instrukcje[i].rstrip()
    alfabet = string.ascii_uppercase
    tekst = []
    for i in instrukcje:
        if i[:-2] == "DOPISZ":
            tekst.append(i[-1])
        elif i[:-2] == "ZMIEN":
            tekst[-1] = i[-1]
        elif i[:-2] == "USUN":
            tekst = tekst[:-1]
        elif i[:-2] == "PRZESUN":
            if i[-1] in tekst:
                if i[-1] == "Z":
                    miejsce = tekst.index("Z")
                    tekst[miejsce] = "A"
                else:
                    miejsce = tekst.index(i[-1])
                    indeks = alfabet.index(i[-1])
                    tekst[miejsce] = alfabet[indeks + 1]
    tekst = ''.join(tekst)
    print(tekst)




d()
