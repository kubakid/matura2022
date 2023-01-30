
def a():
    with open("dane.txt", "r") as file:
        plik = file.readlines()
    for i in range(len(plik)):
        plik[i] = plik[i].rstrip()
    for i in plik:
        czy_palindrom = True
        for j in range(len(i)):
            if i[j] != i[-j-1]:
                czy_palindrom = False
        if czy_palindrom:
            print(i)








a()


