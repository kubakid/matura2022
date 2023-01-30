def a():
    with open("napisy.txt", "r") as file:
        napisy = file.readlines()
    for i in range(len(napisy)):
        napisy[i] = napisy[i].rstrip()
    parzyste = 0
    for i in napisy:
        if int(len(i)) % 2 == 0:
            parzyste += 1
    print("ilosc parzystych: ", str(parzyste))

def porownanie(n):
    jeden = 0
    zero = 0
    tyle_samo = True
    while len(n) != 0:
        if n[-1:] == "1":
            jeden += 1
        else:
            zero += 1
        n = n[:-1]
    if zero == jeden:
        tyle_samo = True
    else:
        tyle_samo = False
    return tyle_samo

def b():
    with open("napisy.txt", "r") as file:
        napisy = file.readlines()
    for i in range(len(napisy)):
        napisy[i]= napisy[i].rstrip()
    jed_rowne_zer = 0
    for i in napisy:
        if porownanie(i):
            jed_rowne_zer += 1
    print("Ilosc napisow z taka sama iloscia 1 i 0: ", jed_rowne_zer)




def c():
    with open("napisy.txt", "r") as file:
        napisy = file.readlines()
    for i in range(len(napisy)):
        napisy[i] = napisy[i].rstrip()
    jedynki = 0
    zera = 0
    for i in napisy:
        if i.strip("0") == "":
            zera += 1
        elif i.strip("1") == "":
            jedynki += 1
    print("ilosc napisow skladajacych sie z samych 1: ", jedynki)
    print("ilosc napisow skladajacych sie z samych 0: ", zera)


def d():
    with open("napisy.txt", "r") as file:
        napisy = file.readlines()
    for i in range(len(napisy)):
        napisy[i] = napisy[i].rstrip()
    for k in range(2, 17):
        ilosc = 0
        for i in napisy:
            if len(i) == k:
                ilosc += 1
        print("ilosc", str(k), "znakowych: ", ilosc)



a()

b()

c()

d()