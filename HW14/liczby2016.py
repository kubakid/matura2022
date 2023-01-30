

def a():
    with open("dane4.txt", "r") as file:
        liczby = file.readlines()
    for i in range(len(liczby)):
        liczby[i]= liczby[i].rstrip()
    pierwsze = 0
    for i in liczby:
        pierwsza = True
        for j in range(2, int(i)):
            if int(i) % int(j) == 0:
                pierwsza = False
                break
        if pierwsza:
            pierwsze += 1
    print("ilosc liczb pierwszych: ", str(pierwsze))


def b():
    with open("dane4.txt", "r") as file:
        liczby = file.readlines()
    for i in range(len(liczby)):
        liczby[i] = liczby[i].rstrip()
    pierwsze = []
    for i in liczby:
        pierwsza = True
        for j in range(2, int(i)):
            if int(i) % int(j) == 0:
                pierwsza = False
                break
        if pierwsza:
            pierwsze.append(int(i))
    print("Najwieksza: "+ str(max(pierwsze)))
    print("Najmniejsza: "+ str(min(pierwsze)))

def czy_pierwsza(n):
    tak = True
    for i in range(2, int(n)- 1):
        if int(n) % i == 0:
            tak = False
            break
    return tak



def c():
    with open("dane4.txt", "r") as file:
        liczby = file.readlines()
    for i in range(len(liczby)):
        liczby[i] = liczby[i].rstrip()
    iloscpar = 0
    for j in range(len(liczby)-1):
            if abs(int(liczby[j])-int(liczby[j+1])) == 2 and czy_pierwsza(liczby[j]) and czy_pierwsza(liczby[j+1]):
                iloscpar += 1
                print(liczby[j], liczby[j+1])
    print(iloscpar)


a()
print("")
print("")
print("")
b()
print("")
print("")
print("")
c()

