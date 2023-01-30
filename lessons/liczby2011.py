def a():
    with open("liczby.txt", "r") as file:
        liczby = file.readlines()
    for i in range(len(liczby)):
        liczby[i] = liczby[i].rstrip()
    parzyste = 0
    for i in liczby:
        dwa = int(i, 2)
        dziesiec = int(str(dwa), 10)
        if dziesiec % 2 == 0:
            parzyste += 1
    print("ilosc liczb parzystych: ", str(parzyste))

def b():
    with open("liczby.txt", "r") as file:
        liczby = file.readlines()
    for i in range(len(liczby)):
        liczby[i] = liczby[i].rstrip()
    maks = 0
    for i in liczby:
        dwa = int(i, 2)
        dziesiec = int(str(dwa), 10)
        if dziesiec > maks:
            maks = dziesiec
    maksdwa = bin(maks)[2:]
    print("Liczba maks w systemie dwujkowym:", str(maksdwa))
    print("Liczba maks w systemie dziesiatkowym:", str(maks))

def c():
    with open("liczby.txt", "r") as file:
        liczby = file.readlines()
    for i in range(len(liczby)):
        liczby[i] = liczby[i].rstrip()
    suma = 0
    ile = 0
    for i in liczby:
        dwa = int(i, 2)
        dziesiec = int(str(dwa), 10)
        if len(i) == 9:
            suma += dziesiec
            ile += 1
    print(ile)
    print(bin(suma)[2:])





a()
print()
b()
print()
c()