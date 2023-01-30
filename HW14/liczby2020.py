def a():
    with open("liczby2020.txt", "r") as file:
        liczby = file.readlines()
    for i in range(len(liczby)):
        liczby[i] = liczby[i].rstrip()
    nieparzyste = 0
    for i in liczby:
        if int(i) % 2 == 1:
            nieparzyste += 1
    print(nieparzyste)


def suma_cyfr(n):
    wynik = 0
    while n != 0:
        wynik += int(n) % 10
        n = int(n) // 10
    return wynik

def b():
    with open("liczby2020.txt", "r") as file:
        liczby = file.readlines()
    for i in range(len(liczby)):
        liczby[i] = liczby[i].rstrip()
    wartosc = 0
    for i in liczby:
        if suma_cyfr(i) == 11:
            wartosc += 1
            print(i)
def czy_pierwsza(n):
    jest = True
    for i in range(2,int(n)-1):
        if int(n) % i ==0:
            jest = False
            break
    return jest

def c():
    with open("liczby2020.txt", "r") as file:
        liczby = file.readlines()
    for i in range(len(liczby)):
        liczby[i] = liczby[i].rstrip()
    for i in liczby:
        if  4000 < int(i) < 5000:
            if czy_pierwsza(i):
                print(i)




a()
print("")
print("")
print("")
b()
print("")
print("")
print("")
c()