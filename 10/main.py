from os import system

system("cls")

def zad1():
    print("Zadanie 1")

    t1 = (1, 2, 10, 5)
    t2 = (10.5, 22, 351)

    l = list(t1)

    del t1
    del l[0]

    t1 = tuple(l)
    print(t1)

def zad2():
    print("\nZadanie 2")

    sl = {'Imie': 'Anna', 'Wiek': 30, 5: 'Cośtam', (6,2): 32}

    sl['dodatki'] = 'Costam znowu'

    slow = {}
    l1 = [1, 3, 5, 7, 9]
    l2 = [2, 4, 6, 8, 10]

    for i in range(len(l1)):
        slow[l1[i]] = l2[i]

    print(slow)

def bezpowt(sl):
    l = list(sl.values())
    count = 0

    for i in l:
        for j in l:
            if i == j:
                count += 1

        if count > 1: return 0
        count = 0

    return 1

def zad3():
    print("\nZadanie 3")

    sl = {1: 3, 3: 4, 5: 6}
    sl2 = {1: 2, 2: 10, 10: 2}

    wyn1 = bezpowt(sl)
    wyn2 = bezpowt(sl2)

    if wyn1 == 1: print("Pierwszy słownik jest bez powtorzeń.")
    else: print("Pierwszy słownik posiada powtórzenia.")

    if wyn2 == 1: print("Drugi słownik jest bez powtorzeń.")
    else: print("Drugi słownik posiada powtórzenia.") 

def odwr(sl):
    l = list(sl.values())
    l2 = list(sl.keys())

    count = bezpowt(sl)

    if count == 0:
        return "Słownik posiada powtórzenia!"

    sl2 = {}

    for i in range(len(l)):
        sl2[l[i]] = l2[i]

    return sl2

def zad4():
    print("\nZadanie 4")

    sl = {1: 4, 3: 4, 5: 6, 7: 8}
    sl2 = odwr(sl)
    print(sl2)

    sl3 = {'slonce': 'sun', 'ksiezyc': 'moon', 'gwiazda': 'star'}
    sl4 = odwr(sl3)
    print(sl4)

def zad5():
    print("\nZadanie 5")

    f = open('plik.txt', 'a')

    sl = {'slonce': 'sun', 'ksiezyc': 'moon', 'gwiazda': 'star'}
    l1 = list(sl.keys())
    l2 = list(sl.values())

    for i in range(len(l1)):
        f.write(f"{l1[i]}:{l2[i]};")

    f.close()

def zad6():
    print("\nZadanie 6")

    f = open('plik.txt', 'r')

    sl = {}
    l1 = []
    l2 = []
    plik = str(f.read())
    splitted = plik.split(";")

    for i in splitted:
        tekst = ''
        flag = False

        for j in range(len(i)):
            if i[j] == ":":
                l1.append(tekst)
                tekst = ''
                continue
            
            if j == len(i)-1:
                l2.append(tekst+i[j])
                tekst = ''
                continue

            tekst += i[j]

    for i in range(len(l1)):
        sl[l1[i]] = l2[i]

    print(sl)

    f.close()

if __name__ == '__main__':
    zad1()
    zad2()
    zad3()
    zad4()
    zad5()
    zad6()
