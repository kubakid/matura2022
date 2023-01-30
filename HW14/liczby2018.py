def a():
    with open("liczby2.txt", "r") as file:
        liczby = file.readlines()
    for i in range(len(liczby)):
        liczby[i] = liczby[i].rstrip()
    parzyste = []
    for i in liczby:
        if int(i) % 2 ==0:
            parzyste.append(int(i))
    print(max(parzyste))

a()
print(" ")

def b():
    with open("liczby2.txt", "r") as file:
        liczby = file.readlines()
    for i in range(len(liczby)):
        liczby[i] = liczby[i].rstrip()
    for i in liczby:
        if i == i[::-1]:
            print(i)

b()

def suma_cyfr(n):
    wynik = 0
    while n != 0:
        wynik += int(n) % 10
        n = int(n) // 10
    return wynik


def c():
    with open("liczby2.txt", "r") as file:
        liczby = file.readlines()
    for i in range(len(liczby)):
        liczby[i] = liczby[i].rstrip()
    calasuma = 0
    for i in liczby:
        calasuma += suma_cyfr(i)
        if suma_cyfr(i) > 30:
            print(i)
    print("Suma wszystkich cyfr wynosi", str(calasuma))

print(" ")
c()