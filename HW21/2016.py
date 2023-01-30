def a():
    with open('liczby.txt', 'r') as file:
        liczby = file.readlines()
    for i in range(len(liczby)):
        liczby[i] = liczby[i].rstrip()
    licznik = 0
    for i in liczby:
        if i[-1] == '8':
            licznik += 1
    print(licznik)

a()

def b():
    with open('liczby.txt', 'r') as file:
        liczby = file.readlines()
    for i in range(len(liczby)):
        liczby[i] = liczby[i].rstrip()
    licznik = 0
    for i in liczby:
        if i[-1] == '4':
            zbior = set(i)
            if '0' not in zbior:
                licznik += 1
    print(licznik)


b()


def c():
    with open('liczby.txt', 'r') as file:
        liczby = file.readlines()
    for i in range(len(liczby)):
        liczby[i] = liczby[i].rstrip()
    licznik = 0
    for i in liczby:
        if i[-1] == '2':
            if i[-2] == '0':
                licznik += 1
    print(licznik)


c()


def d():
    with open('liczby.txt', 'r') as file:
        liczby = file.readlines()
    for i in range(len(liczby)):
        liczby[i] = liczby[i].rstrip()
    suma = 0
    for i in liczby:
        if i[-1] == '8':
            liczba = i[:-1]
            a = int(liczba, 8)
            suma += a
    print(suma)


d()



def e():
    with open('liczby.txt', 'r') as file:
        liczby = file.readlines()
    for i in range(len(liczby)):
        liczby[i] = liczby[i].rstrip()
    kodmax = ''
    kodmin = ''
    maximum = 0
    minimum = 10000000
    for i in liczby:
        system = int(i[-1])
        liczba = i[:-1]
        a = int(liczba, system)
        if a > maximum:
            kodmax = i
            maximum = a
        if a < minimum:
            kodmin = i
            minimum = a
    print(kodmax)
    print(maximum)
    print(kodmin)
    print(minimum)



e()