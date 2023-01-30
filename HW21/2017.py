import math

def pierwsza(n):
    tak = True
    for i in range(2, int(n) - 1):
        if int(n) % i == 0:
            tak = False
            break
    return tak

def a():
    with open('punkty.txt', 'r') as file:
        xy = file.readlines()
    for i in range(len(xy)):
        xy[i] = xy[i].rstrip()
    licznik = 0
    for i in xy:
        a = list(map(int, i.split()))
        if pierwsza(a[0]) and pierwsza(a[1]):
            licznik += 1
    print(licznik)


a()


def b():
    with open('punkty.txt', 'r') as file:
        xy = file.readlines()
    for i in range(len(xy)):
        xy[i] = xy[i].rstrip()
    licznik = 0
    for i in xy:
        a = list(i.split())
        b = sorted(set(a[0]))
        c = sorted(set(a[1]))
        if b == c:
            licznik += 1
    print(licznik)


b()


def c():
    with open('punkty.txt', 'r') as file:
        xy = file.readlines()
    for i in range(len(xy)):
        xy[i] = xy[i].rstrip()
    a = ''
    b = ''
    maks = 0
    for i in xy:
        wsp = list(map(int, i.split()))
        for j in xy:
            wsp2 = list(map(int, j.split()))
            if i == j:
                continue
            else:
                d = round(math.sqrt((wsp[0] - wsp2[0])**2 + (wsp[1]-wsp2[1])**2))
                if d > maks:
                    a = i
                    b = j
                    maks = d
    print(a)
    print(b)
    print(maks)


c()


def d():
    with open('punkty.txt', 'r') as file:
        xy = file.readlines()
    for i in range(len(xy)):
        xy[i] = xy[i].rstrip()
    wew = 0
    na = 0
    zew = 0
    for i in xy:
        wsp = list(map(int, i.split()))
        x, y = wsp
        if abs(x) < 5000 and abs(y) < 5000:
            wew += 1
        elif abs(x) == 5000 or abs(y) == 5000:
            na += 1
        else:
            zew += 1
    print(wew)
    print(na)
    print(zew)

d()