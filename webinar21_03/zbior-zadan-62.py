# Zadanie 62.2

plik = open("liczby1.txt")
osemkowy = plik.read().splitlines()
plik.close()

plik = open("liczby2.txt")
dziesiatkowy = plik.read().splitlines()
plik.close()


pierwszy = dziesiatkowy[0]
najdluzszy = 0
dlugosc = 0

for i in range(len(dziesiatkowy)):
    if i == len(dziesiatkowy) - 1:
        break
    if dziesiatkowy[i + 1] < dziesiatkowy[i]:
        if dlugosc > najdluzszy:
            najdluzszy = dlugosc
            pierwszy = dziesiatkowy[i + 1 - dlugosc]
        dlugosc = 0
    else:
        dlugosc += 1


print("DŁUGOSC NAJDLUZSZEGO CIAGU: ", najdluzszy)
print(pierwszy)