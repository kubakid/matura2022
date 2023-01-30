with open("przyklad-piksele.txt", "r") as plik:
    dane = plik.readlines()
    for i in range(len(dane)):
        dane[i] = dane[i].rstrip().split()

    # Zadanie 1.
    maksi = dane[0][0]
    mini = dane[0][0]
    for wiersz in range(200):
        for kolumna in range(320):
            if dane[wiersz][kolumna] > maksi:
                maksi = dane[wiersz][kolumna]
            if dane[wiersz][kolumna] < mini:
                mini = dane[wiersz][kolumna]
    print(maksi, mini)