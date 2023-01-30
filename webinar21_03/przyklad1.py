def wypiszObrazek(obrazek):
    for i in range(21):
        print(obrazek[i])
    print("---------------------")

with open('dane_obrazki.txt', 'r') as plik:
    dane = plik.readlines()
    for i in range(len(dane)):
        dane[i] = dane[i].rstrip()

    obrazki = []
    for i in range(200):
        obrazek = []
        for j in range(21):
            obrazek.append(dane[i * 22 + j])
        obrazki.append(obrazek)

    # Test poprawnosci wczytania pliku:
    # for i in range(200):
    # 	wypiszObrazek(obrazki[i])

    # ----------------------------
    # Zadanie 1.
    print('Zadanie 1.')
    maks1 = 0
    ileobr = 0
    ilecz = 0
    for i in range(200):
        for j in range(20):
            for k in range(20):
                if obrazki[i][j][k] == '1':
                    ilecz += 1
            if ilecz > 200:
                ileobr += 1
                # wypiszObrazek(obrazki[i])
                if ilecz > maks1:
                    maks1 = ilecz
    print(ileobr)
    print(maks1)

    # ----------------------------
    # Zadanie 2.
    # Nie omawiane na webinarze

    # ----------------------------
    # Zadanie 3.
    print('Zadanie 3.')

    niepop = 0
    pop = 0
    nap = 0
    maks = 0
    for i in range(200):
        wiersz = 0
        kolumna = 0
        for j in range(20):
            ileczw = 0
            ileczk = 0
            for k in range(20):
                if obrazki[i][j][k] == 1:
                    ileczw += 1
                if obrazki[i][k][j] == 1:
                    ileczk += 1
            if ileczw % 2 != obrazki[i][j][20]:
                wiersz += 1
            if ileczk % 2 != obrazki[i][20][j]:
                kolumna += 1
        if wiersz > 1 or kolumna > 1:
            niepop += 1
        elif wiersz == 1 or kolumna == 1:
            nap += 1
        else:
            pop += 1
    print(pop, nap, niepop)