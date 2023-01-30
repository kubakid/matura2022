def a():
    with open("hasla.txt", "r") as file:
        hasla = file.readlines()
    for i in range(len(hasla)):
        hasla[i] = hasla[i].rstrip()
    parzyste = 0
    n_parzyste = 0
    for i in hasla:

        if len(i) % 2 == 0:
            parzyste += 1
        else:
            n_parzyste += 1
    print(parzyste)
    print(n_parzyste)

def b():
    with open("hasla.txt", "r") as file:
        hasla = file.readlines()
    for i in range(len(hasla)):
        hasla[i] = hasla[i].rstrip()
    for i in hasla:
        if i == i[::-1]:
            print(i)


def c():
    with open("hasla.txt", "r") as file:
        hasla = file.readlines()
    for i in range(len(hasla)):
        hasla[i] = hasla[i].rstrip()
    for i in hasla:
        for j in range(len(i)-1):
            if ord(i[j])+ord(i[j+1])== 220:
                print(i)
                break









# print(ord("a"))
# print(ord("A"))
# print(ord("0"))
# print(chr(97))
# print(chr(33))

a()


b()


c()