import string
cyfry = [0,1,2,3,4,5,6,7,8,9,0]
def a():
    with open('identyfikator.txt', 'r') as file:
        dane = file.readlines()
    for i in range(len(dane)):
        dane[i] = dane[i].rstrip()
    maks = 0
    for i in dane:
        akt = 0
        tablica = list(i)
        for j in range(3,9):
            if int(tablica[j]) in cyfry:
                akt += int(tablica[j])
        if akt > maks:
            maks = akt
    for i in dane:
        akt = 0
        tablica = list(i)
        for j in range(3, 9):
            if int(tablica[j]) in cyfry:
                akt += int(tablica[j])
        if akt == maks:
            print(i)


a()
print()

def b():
    with open('identyfikator.txt', 'r') as file:
        dane = file.readlines()
    for i in range(len(dane)):
        dane[i] = dane[i].rstrip()
    for i in dane:
        lista = list(i)
        if lista[0] == lista[2]:
            print(i)
            continue
        if lista[3] == lista[8] and lista[4] == lista[7] and lista[5] == lista[6]:
            print(i)


b()
alfabet = list(string.ascii_uppercase)
slownik = {}
w = 10
for i in range(26):
    slownik[alfabet[w-10]] = w
    w += 1


print()
def c():
    with open('identyfikator.txt', 'r') as file:
        dane = file.readlines()
    for i in range(len(dane)):
        dane[i] = dane[i].rstrip()
    for i in dane:
        lista = list(i)
        jeden = slownik[lista[0]] * 7
        dwa = slownik[lista[1]] * 3
        trzy= slownik[lista[2]]
        piec= int(lista[4])*7
        szesc= int(lista[5])*3
        siedem= int(lista[6])
        osiem= int(lista[7])*7
        dziewiec= int(lista[8])*3
        suma = jeden + dwa + trzy + piec + szesc + siedem + osiem + dziewiec
        if suma % 10 != int(lista[3]):
            print(i)

c()



