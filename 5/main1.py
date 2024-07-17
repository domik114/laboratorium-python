import os

os.system("cls")

def zad1():
    print("Zadanie 1")

    l = [3, 'alfa', 2.71, 'kot']

    print(l[2])
    print(l[-3])

    l[0] = 4
    l[-1] = 'pies'

    l2 = l

    print(l, end=" ")
    print(l2)

    l2[0] = 'zmodyfikowano'

    print(l, end=" ")
    print(l2)

    l3 = l.copy()

    l3[0] = 'mod22'

    print(l, end="")
    print(l3)

def zad2():
    print("\nZadanie 2")

    l = []

    for i in range(1, 11):
        l.append(i**2)

    print(l)

    for i in range(len(l)):
        if l[i] % 2 == 0:
            l[i] = -1 * l[i]

    print(l)

def zad3():
    print("\nZadanie 3")

    n = int(input("Podaj n: "))

    l = []

    for i in range(n):
        l.append(int(input("Podaj liczbę: ")))

    print("\nMinimalny element:", min(l), "\nMaksymalny element:", max(l))

def zad4():
    print("\nZadanie 4")

    from math import sin
    n = int(input("Podaj n: "))

    l = []

    for i in range(1, n + 1):
        l.append(sin(i))

    print(l)
    print("Minimalny element:", min(l), "\nMaksymalny element:", max(l))

def zad5():
    print("\nZadanie 5")

    l = []

    for i in range(100, 151):
        l.append(i)

    print(f"lista przed usunięciem: {l}")

    del l[5:-1:5]

    print(f"\nLista po usunięciu: {l}")

def zad6():
    print("\nZadanie 6")

    l = [5, 1, 7, 3, 10, 3, 111, -34, 15, -25]

    l2 = l[1::]
    l2.append(l[0])

    print("l", l)
    print("l2", l2)

    l3 = l[::]
    del l3[9]
    l3.insert(0, l[9])
    print("l3", l3)

    l4 = l[::-1]
    print("l4", l4)

    l5 = []
    for i in range(len(l)):
        if l[i] % 2 == 0:
            l5.append(l[i])

    print("l5", l5)

    l6 = []

    for i in range(len(l)):
        if i % 2 == 0 and l[i] % 2 == 1:
            l6.append(l[i])

    print("l6", l6)

def zad7():
    print("\nZadanie 7")

    from math import pi
    from random import randint

    l = []
    p = str(pi)

    for i in range(len(p)):
        if p[i] != ".":
            l.append(p[i])

    for i in range(len(l)):
        l[i] = int(l[i])

    for i in range(33):
        l.append(randint(0, 9))

    print(l)

#zad1()
#zad2()
#zad3()
#zad4()
#zad5()
#zad6()
zad7()