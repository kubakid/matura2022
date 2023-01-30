def a():
    with open('dane1.txt', 'r') as file:
        jeden = file.readlines()
    with open('dane2.txt', 'r') as file:
        dwa = file.readlines()
    for i in range(len(jeden)):
        jeden[i] = jeden[i].rstrip()
        dwa[i] = dwa[i].rstrip()
    licznik = 0
    for i in range(len(jeden)):
        a = list(jeden[i].split())
        b = list(dwa[i].split())
        if a[-1] == b[-1]:
            licznik += 1
    print(licznik)


a()


def b():
    with open('dane1.txt', 'r') as file:
        jeden = file.readlines()
    with open('dane2.txt', 'r') as file:
        dwa = file.readlines()
    for i in range(len(jeden)):
        jeden[i] = jeden[i].rstrip()
        dwa[i] = dwa[i].rstrip()
    licznik = 0
    for i in range(len(jeden)):
        a = list(map(int, jeden[i].split()))
        b = list(map(int, dwa[i].split()))
        p1 = 0
        p2 = 0
        for j in range(10):
            if a[j] % 2 == 0:
                p1 += 1
            if b[j] % 2 == 0:
                p2 += 1
        if p2 == p1 == 5:
            licznik += 1
    print(licznik)


b()

def c():
    with open('dane1.txt', 'r') as file:
        jeden = file.readlines()
    with open('dane2.txt', 'r') as file:
        dwa = file.readlines()
    for i in range(len(jeden)):
        jeden[i] = jeden[i].rstrip()
        dwa[i] = dwa[i].rstrip()
    licznik = 0
    lista = []
    for i in range(len(jeden)):
        a = sorted(set(jeden[i].split()))
        b = sorted(set(dwa[i].split()))
        if a == b:
            licznik += 1
            lista.append(i+1)
    print(licznik)
    for i in lista:
        print(i, end="")
    print()


c()


def d():
    with open('dane1.txt', 'r') as file:
        jeden = file.readlines()
    with open('dane2.txt', 'r') as file:
        dwa = file.readlines()
    for i in range(len(jeden)):
        jeden[i] = jeden[i].rstrip()
        dwa[i] = dwa[i].rstrip()
    lista = []
    for i in range(len(jeden)):
        a = list(map(int, jeden[i].split()))
        b = list(map(int, dwa[i].split()))
        suma = a + b
        suma = sorted(suma)
        for i in range(len(suma)):
            print(suma[i], end = ' ')
        print()



d()


