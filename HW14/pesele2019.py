def a():
    with open("dane.txt", "r") as file:
        pesele = file.readlines()
    for i in range(len(pesele)):
        pesele[i] = pesele[i].rstrip()
    kobiety = 0
    mezczyzni = 0
    for i in pesele:
        if int(i[-2]) % 2 == 0:
            kobiety += 1
        else:
            mezczyzni += 1
    print("Ilosc damskich peseli: "+str(kobiety))
    print("Ilosc meskich peseli: "+str(mezczyzni))

a()

def b():
    with open("dane.txt", "r") as file:
        pesele = file.readlines()
    for i in range(len(pesele)):
        pesele[i] = pesele[i].rstrip()
    listopadowicze = 0
    for i in pesele:
        if int(i[2:4]) == 11 or int(i[2:4]) == 31:
            listopadowicze += 1
    print("ilosc urodzonych w listopadzie wynosi: ", str(listopadowicze))

b()



def c():
    with open("dane.txt", "r") as file:
        pesele = file.readlines()
    for i in range(len(pesele)):
        pesele[i] = pesele[i].rstrip()
    print("niepoprawne numere pesel to: ")
    for i in pesele:
        wynik = int(i[0]) + int(i[1]) * 3 + int(i[2]) * 7 + int(i[3]) * 9 + int(i[4]) + int(i[5]) * 3 + int(i[6]) * 7 + int(i[7]) * 9 + int(i[8]) + int(i[9]) * 3 + int(i[10])
        if wynik % 10 != 0:
            print(i)

c()

