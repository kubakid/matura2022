def a():
    with open("anagram.txt", "r") as file:
        anagramy = file.readlines()
    for i in range(len(anagramy)):
        anagramy[i] = anagramy[i].rstrip()
    for i in anagramy:
        slowa = i.split()
        a = set()
        for j in slowa:
            a.add(len(j))
        if len(a) == 1:
            print(i)


# a()


def b():
    with open("anagram.txt", "r") as file:
        anagramy = file.readlines()
    for i in range(len(anagramy)):
        anagramy[i] = anagramy[i].rstrip()
    for i in anagramy:
        slowa = i.split()
        a = ""
        a = a + slowa[0]
        dlugosc = len(slowa[0])
        litery = set()
        for j in a:
            litery.add(j)
        reszta = slowa[1:]
        razy = 0
        for slowo in reszta:
            anagram = True
            wszystko = set()
            if len(slowo) != dlugosc:
                break
            for litera in slowo:
                wszystko.add(litera)
            if wszystko != set() and wszystko != litery:
                break
            if anagram:
                razy +=1
            if razy == 4:
                print(i)





        # anagram = True
        # for l in slowa[1:]:
        #     wszystkie.add(l)

        # for h in i:
        #     wszystkie.add(h)
        #     wszystkie.discard(" ")
        #     if wszystkie != litery:
        #         anagram = False
        #         break
        #     else:
        #         print(i)



b()


