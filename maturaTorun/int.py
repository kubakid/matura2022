def a():
    with open('wykreslanka.txt','r') as file:
        wykreslanka = file.readlines()
    for i in range(len(wykreslanka)):
        wykreslanka[i] = wykreslanka[i].rstrip()
    for i in range(len(wykreslanka)):
        a = wykreslanka[i].find("matura")
        if a > -1:
            print(i,a)


a()


def b():
    with open('wykreslanka.txt','r') as file:
        wykreslanka = file.readlines()
    for i in range(len(wykreslanka)):
        wykreslanka[i] = wykreslanka[i].rstrip()
    slownik = {}
    for i in range(len(wykreslanka)):
        maks = 0
        akt = 1
        for j in range(len(wykreslanka[i])-1):
            if wykreslanka[i][j] == wykreslanka[i][j+1]:
                akt += 1
            else:
                if maks < akt:
                    maks = akt
                akt = 1
        if maks < akt:
            maks = akt
        slownik[i+1] = maks
    ogolnymaks = 0
    for i in slownik:
        if slownik[i] > ogolnymaks:
            ogolnymaks = slownik[i]
    print(ogolnymaks)
    for i in slownik:
        if slownik[i] == ogolnymaks:
            print(i)

b()


def c():
    with open('wykreslanka.txt','r') as file:
        wykreslanka = file.readlines()
    for i in range(len(wykreslanka)):
        wykreslanka[i] = wykreslanka[i].rstrip()


    # for i in range(100):
    #     koniec = False
    #     for j in range(200-26):
    #         lista = []
    #         for h in range(26):
    #             lista.append(wykreslanka[i][j+h])
    #         if len(set(lista)) == 26:
    #             koniec = True
    #             print("TAK")
    #             break
    # for i in range(99):
    #     koniec = False
    #     for j in range(200-13):
    #         lista = []
    #         for a in range(2):
    #             for b in range(13):
    #                 lista.append(wykreslanka[i+a][j+b])
    #         if len(set(lista)) == 26:
    #             print("TAK")
    #             koniec = True
    #             break
    # for i in range(100-26):
    #     koniec = False
    #     for j in range(200):
    #         lista = []
    #         for a in range(26):
    #             lista.append(wykreslanka[i+a][j])
    #         if len(set(lista)) == 26:
    #             koniec = True
    #             print("TAK")
    #             break
    lewygornyrog = [0,0]
    for i in range(100-13):
        koniec = False
        for j in range(200-1):
            lista = []
            for a in range(13):
                for b in range(2):
                    lista.append(wykreslanka[i+a][j+b])
            if len(set(lista)) == 26:
                print("TAK")
                print(i+1,j+1)
                koniec = True
        if koniec:
            break

    wys = 2
    szer = 13
    print(wys,szer)


c()


