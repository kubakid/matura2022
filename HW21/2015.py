def a():
    with open('kody.txt', 'r') as file:
        liczby = file.readlines()
    for i in range(len(liczby)):
        liczby[i] = liczby[i].rstrip()
    for i in liczby:
        p = 0
        np = 0
        for j in range(len(i)):
            if j % 2 == 0:
                np += int(i[j])
            else:
                p += int(i[j])
        print(str(p), str(np))


a()
print()
print()
print()


def b():
    with open('kody.txt', 'r') as file:
        kody = file.readlines()
    for i in range(len(kody)):
        kody[i] = kody[i].rstrip()
    with open('cyfra_kodkreskowy.txt', 'r') as file:
        zakodowane = file.readlines()
    for i in range(len(zakodowane)):
        zakodowane[i] = zakodowane[i].rstrip()
    zakodowane = zakodowane[1:]
    lista = []
    for i in zakodowane:
        a = list(i.split())
        lista.append(a)
    for i in kody:
        p = 0
        np = 0
        for j in range(len(i)):
            if j % 2 == 0:
                np += int(i[j])
            else:
                p += int(i[j])
        a = (10 - (p * 3 + np) % 10) % 10
        print(str(a), lista[a][1])





b()

def c():
    with open('kody.txt', 'r') as file:
        kody = file.readlines()
    for i in range(len(kody)):
        kody[i] = kody[i].rstrip()
    with open('cyfra_kodkreskowy.txt', 'r') as file:
        zakodowane = file.readlines()
    for i in range(len(zakodowane)):
        zakodowane[i] = zakodowane[i].rstrip()
    zakodowane = zakodowane[1:]
    lista = []
    for i in zakodowane:
        a = list(i.split())
        lista.append(a)
    for i in kody:
        napis = '11011010'
        p = 0
        np = 0
        for j in range(len(i)):
            napis += lista[int(i[j])][1]
            if j % 2 == 0:
                np += int(i[j])
            else:
                p += int(i[j])
        a = (10 - (p * 3 + np) % 10) % 10
        napis += lista[a][1]
        napis += '11010110'
        print(napis)

print()
print()
print()

c()
