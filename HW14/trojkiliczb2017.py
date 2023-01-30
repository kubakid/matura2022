def a():
    with open("liczby.txt", "r") as file:
        liczby = file.readlines()
    for i in range(len(liczby)):
        liczby[i] = liczby[i].rstrip()
    rosnaco = 0
    for i in liczby:
        przerwa_a = i.index(" ")
        pierwsza = i[:przerwa_a]
        i = i[przerwa_a:].lstrip()
        przerwa_b = i.index(" ")
        druga = i[:przerwa_b]
        trzecia = i[przerwa_b+1:]
        if int(pierwsza) < int(druga) < int(trzecia):
             rosnaco += 1
    print(rosnaco)

def nwd(a, b):
    if b > 0:
        return nwd(b, a % b)
    return a

def b():
    with open("liczby.txt", "r") as file:
        liczby = file.readlines()
    for i in range(len(liczby)):
        liczby[i] = liczby[i].rstrip()
    sumanwd = 0
    for i in liczby:
        przerwa_a = i.index(" ")
        pierwsza = int(i[:przerwa_a])
        i = i[przerwa_a:].lstrip()
        przerwa_b = i.index(" ")
        druga = int(i[:przerwa_b])
        trzecia = int(i[przerwa_b + 1:])
        pierwszynwd = nwd(pierwsza, druga)
        druginwd = nwd(pierwszynwd, trzecia)
        sumanwd += druginwd
    print(sumanwd)

def suma_cyfr(n):
    wynik = 0
    while n != 0:
        wynik = wynik + int(n) % 10
        n = n // 10
    return wynik


def c():
    with open("liczby.txt", "r") as file:
        liczby = file.readlines()
    for i in range(len(liczby)):
        liczby[i] = liczby[i].rstrip()
    trzypiec = 0
    maks = 0
    iloscmaks = 0
    for i in liczby:
        przerwa_a = i.index(" ")
        pierwsza = int(i[:przerwa_a])
        i = i[przerwa_a:].lstrip()
        przerwa_b = i.index(" ")
        druga = int(i[:przerwa_b])
        trzecia = int(i[przerwa_b + 1:])
        if suma_cyfr(pierwsza) + suma_cyfr(druga) + suma_cyfr(trzecia) == 35:
            trzypiec += 1
        if suma_cyfr(pierwsza) + suma_cyfr(druga) + suma_cyfr(trzecia) > maks:
            maks = suma_cyfr(pierwsza) + suma_cyfr(druga) + suma_cyfr(trzecia)
    for i in liczby:
        przerwa_a = i.index(" ")
        pierwsza = int(i[:przerwa_a])
        i = i[przerwa_a:].lstrip()
        przerwa_b = i.index(" ")
        druga = int(i[:przerwa_b])
        trzecia = int(i[przerwa_b + 1:])
        if suma_cyfr(pierwsza) + suma_cyfr(druga) + suma_cyfr(trzecia) == maks:
            iloscmaks +=1

    print("ilosc wystapien sumy cyfr rownej 35: ", str(trzypiec))
    print("maksymalna suma cyfr rowna:", (maks))
    print("wystapila", str(iloscmaks), "razy")




a()
print(" ")
print(" ")
print(" ")
b()
print(" ")
print(" ")
print(" ")
c()