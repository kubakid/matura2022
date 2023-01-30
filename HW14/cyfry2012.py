def a():
    with open("cyfry.txt", "r") as file:
        cyfry = file.readlines()
    for i in range(len(cyfry)):
        cyfry[i] = cyfry[i].rstrip()
    parzyste = 0
    for j in cyfry:
        if int(j) % 2 == 0:
            parzyste += 1
    print("Ilosc parzystych: ", str(parzyste))


def suma_liczb(n):
    wynik = 0
    while n != 0:
        wynik += int(n) % 10
        n = int(n) // 10
    return wynik


def b():
    with open("cyfry.txt", "r") as file:
        cyfry = file.readlines()
    for i in range(len(cyfry)):
        cyfry[i] = cyfry[i].rstrip()
    maks = 6
    min = 100
    liczba_maks = ""
    liczba_min = ""
    for i in cyfry:
        suma = suma_liczb(i)

        if suma > maks:
            liczba_maks = i
            maks = suma
        if suma < min:
            min = suma
            liczba_min = i
    print("Liczba z maks suma cyfr: ", liczba_maks)
    print("Liczba z min suma cyfr: ", liczba_min)

def czy_cr(n):
    liczba = 10
    tak = False
    while n != 0:
        liczb_koniec = int(n) % 10
        n = int(n) // 10
        if liczb_koniec < liczba:
            tak = True
            liczba = liczb_koniec
        else:
            tak = False
            break
    return tak





def c():
    with open("cyfry.txt", "r") as file:
        cyfry = file.readlines()
    for i in range(len(cyfry)):
        cyfry[i] = cyfry[i].rstrip()
    for i in cyfry:
        if czy_cr(i):
            print(i)







a()



b()

c()


