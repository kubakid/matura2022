with open("instrukcje.txt", "r") as plik:
    dane = plik.readlines()

    for i in range(len(dane)):
        dane[i] = dane[i].rstrip().split()

    # Zadanie 4.

    wynik = ""
    for linijka in dane:
        if linijka[0] == "DOPISZ":
            wynik += linijka[-1]
        if linijka[0] == "ZMIEN":
            wynik = wynik[:len(wynik) - 1] + linijka[-1]
        if linijka[0] == "USUN":
            wynik = wynik[:len(wynik) - 1]
        if linijka[0] == "PRZESUN":
            if linijka[-1] != "Z":
                for litera in range(len(dane)):
                    if dane[litera] == linijka[-1]:
                        wynik = wynik[:litera-1] + chr(ord(linijka[1])+1)
            else:
                for litera in range(len(linijka)):
                    if linijka[litera] == linijka[-1]:
                        wynik = wynik[:litera-1] + "A"
    print(wynik)