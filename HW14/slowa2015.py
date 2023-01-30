def a():
    with open("slowa.txt", "r") as file:
        slowa = file.readlines()
    for i in range(len(slowa)):
        slowa[i] = slowa[i].rstrip()
    for k in range(1, 13):
        ilosc = 0
        for i in slowa:
            if len(i) == k:
                ilosc += 1
        print(str(k)+ ",  "+ str(ilosc))




def b():
    with open("slowa.txt", "r") as file:
        slowa = file.readlines()
    for i in range(len(slowa)):
        slowa[i] = slowa[i].rstrip()
    with open("nowe.txt", "r") as filei:
        nowe = filei.readlines()
    for j in range(len(nowe)):
        nowe[j]= nowe[j].rstrip()
    for j in nowe:
        ilosc = 0
        odbicie = 0
        for i in slowa:
            if j == i:
                ilosc +=1
            if j == i[::-1]:
                odbicie += 1
        print(str(j), str(ilosc), "", str(odbicie))



a()
print("")
print("")
print("")
b()
