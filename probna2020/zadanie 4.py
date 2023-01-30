import math

def czypierwsza(n):
    for i in range(2, math.ceil(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
def a():
    with open('pary.txt','r') as file:
        pary = file.readlines()
    for i in range(len(pary)):
        pary[i]=pary[i].rstrip()
    lista = []
    for i in pary:
        a, b = i.split()
        if int(a) % 2 == 0:
            lista.append(a)

    for i in lista:
        pierwsze = []
        for j in range(2, int(i)):
            if czypierwsza(j):
                pierwsze.append(j)
        ok = []
        for k in pierwsze:
            for l in pierwsze:
                if int(k) + int(l) == int(i):
                    ok.append([k,l])
        maks = abs(ok[0][0] - ok[0][1])
        a = ok[0][0]
        b = ok [0][1]
        for i in ok:
            if abs(i[0] - i[1]) >maks:
                maks = abs(i[0]-i[1])
                c = i[0]
                d = i[1]
                if c > d:
                    b = c
                    a = d
                else:
                    b = a
                    a = c
        print(a+b ,a,b)





def b():
    with open('pary.txt','r') as file:
        pary = file.readlines()
    for i in range(len(pary)):
        pary[i]=pary[i].rstrip()
    slowa = []
    for i in pary:
        a,b = i.split()
        slowa.append(b)
    for i in slowa:
        maks = 1
        akt = 1
        litera = i[0]
        aktlitera = i[0]
        for j in range(len(i)-1):
            aktlitera = i[j]
            if i[j] == i[j+1]:
               akt += 1

            else:
                if akt > maks:
                    maks = akt
                    litera = i[j-1]
                akt = 1

        j = len(i)
        if akt > maks:
            maks = akt
            litera = i[j - 1]
            akt = 1
        print(litera * maks,maks)





def c():
    with open('pary.txt','r') as file:
        pary = file.readlines()
    for i in range(len(pary)):
        pary[i]=pary[i].rstrip()
    ok = []
    for i in pary:
        a, b = i.split()
        if int(a) == len(b):
            ok.append([a,b])
    min = 3
    min = ok[0][1]
    for i in ok:
        if i[1] < min:
            min = i[1]
    print('3', min)

a()
b()
c()