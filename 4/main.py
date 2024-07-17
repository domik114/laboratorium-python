import os

os.system("cls")

def zad1():
    print("Zadanie 1")

    n = str(input("Podaj zdanie: "))
    count = 0

    for i in n:
        print(i, end=" ")
        count += 1

    print(f"\nIlość znaków w zdaniu: {count}")

def zad2():
    print("\nZadanie 2")

    n = str(input("Podaj zdanie: "))
    count = 0

    for i in n:
        print(i, end=" ")
        if i == 'a' and i.islower():
            count += 1

    print(f"\nIlość małych liter a: {count}")

def zad3():
    print("\nZadanie 3")

    n = str(input("Podaj zdanie: "))
    count = 0

    for i in n:
        if i != " ":
            print(i, end=" ")

        else:
            print("\n")
            count += 1

    print(f"\n\nIlość słow w zdaniu: {count+1}")

def zad4():
    print("\nZadanie 4")

    ln_2 = 0
    pi = 0
    bool = False

    for i in range(1, 100001):
        if i % 2 == 0:
            ln_2 -= 1/i
        else:
            ln_2 += 1/i

    for j in range(1, 1000001, 2):
        if bool:
            pi -= 1/j
            bool = False
        else:
            pi += 1/j
            bool = True

    pi = pi * 4

    print(ln_2)
    print(pi)

def zad5():
    print("\nZadanie 5")

    n = int(input("Z ilu liczb ma być wyliczona średnia?: "))
    liczby = []
    wynik = 0

    for i in range(0, n):
        liczby.append(float(input("Podaj liczbę: ")))

    for i in liczby:
        wynik += i

    wynik /= n

    print("Średnia wynosi:", wynik)

def zad6():
    print("\nZadanie 6")

    from math import sqrt, sin

    for i in range(1, 21):
        print("%.2f" % sqrt(i), end=", ")

    print("\n", end="")

    for i in range(1, 21):
        print("%.2f" % sin(i), end=", ")
    
    print()

def zad7():
    print("\nZadanie 7")

    from math import sqrt, pow

    s = 0

    for i in range(1, 10001):
        s += 1/pow(i, 2)

    print(s)
    print(sqrt(s*6))

def zad8():
    print("\nZadanie 8")

    t = str(input("Podaj zdanie: "))

    a = t[::-1]

    print(a)

def zad9():
    print("\nZadanie 9")

    a = -1
    b = 0
    c = (a+b)/2

    print(c)

    for i in range(1, 1001):
        c = (a+b)/2

        if c ** 5 + c + 1 > 0 and a ** 5 + a + 1 > 0:
            a = c
        else:
            b = c

    print(c)

    print(c**5+c+1)

zad1()
zad2()
zad3()
zad4()
zad5()
zad6()
zad7()
zad8()
zad9()