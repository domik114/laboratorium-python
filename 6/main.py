from os import system

system("cls")

def zad1():
    print("Zadanie 1")

    s = 'Ala ma kota'
    lz = list(s)
    print(lz)

    print("\nPierwszy sposób:")

    for i in range(len(lz)):
        print(lz[i], end=" ")
    
    print("\nDrugi sposób:")

    for i in lz:
        print(i, end=" ")

    print()

    return lz

def zad2(lz):
    print("\nZadanie 2")

    ile = lz.count("a")

    print(f"Ilość literki a: {ile}")
    print("-----###-----")
    s = str(input("Podaj zdanie: "))

    ls = list(s)

    ile_a = ls.count("a")
    ile_w = ls.count("w")
    ile_s = ls.count("s")

    print(f"Ilość literek a: {ile_a}")
    print(f"Ilość literek w: {ile_w}")
    print(f"Ilość literek s: {ile_s}")

def zad3():
    print("\nZadanie 3")

    from math import factorial

    n = factorial(2000)

    s = str(n)
    lista = list(s)

    ile_0 = lista.count("0")
    ile_1 = lista.count("1")
    ile_2 = lista.count("2")
    ile_3 = lista.count("3")
    ile_4 = lista.count("4")
    ile_5 = lista.count("5")
    ile_6 = lista.count("6")
    ile_7 = lista.count("7")
    ile_8 = lista.count("8")
    ile_9 = lista.count("9")

    print(f"Ilość 0: {ile_0}")
    print(f"Ilość 1: {ile_1}")
    print(f"Ilość 2: {ile_2}")
    print(f"Ilość 3: {ile_3}")
    print(f"Ilość 4: {ile_4}")
    print(f"Ilość 5: {ile_5}")
    print(f"Ilość 6: {ile_6}")
    print(f"Ilość 7: {ile_7}")
    print(f"Ilość 8: {ile_8}")
    print(f"Ilość 9: {ile_9}")

def zad4():
    print("\nZadanie 4")
    
    l = []

    for i in range(30):
        l.append((3**i)-(2**i))

    for i in range(len(l)):
        if l[i] == 1161737179:
            print(f"N znajduje się na pozycji: {i}, dla liczby: {l[i]}")

    print(f"n = 19: {(3**19)-(2**19)}")

    return l

def zad5(l):
    print("\nZadanie 5")

    l2 = []

    for i in l:
        l2.append(i % 19)

    print(l2)
    print(f"Czy 10 jest w liście? {10 in l2}")
    print(f"Czy 11 jest w liście? {11 in l2}")

    n = int(input("\nPodaj n od 0 do 18: "))

    if n in l2:
        print(f"Ta liczba występuje w l2 {l2.count(n)} raz/y.")
    else:
        print("Nie ma tej liczby w l2")

def zad6():
    print("\nZadanie 6")

    from math import factorial

    l = []

    for i in range(1, 101):
        l.append(1/i)

    print(f"Suma: {sum(l)}\nMin: {min(l)}\nMax: {max(l)}")

    lz = []

    s = factorial(1000)
    s = str(s)

    lz = list(s)

    for i in range(len(lz)):
        lz[i] = int(lz[i])

    print(f"\nSuma cyfr 1000!: {sum(lz)}")

def zad7():
    print("\nZadanie 7")

    from math import factorial

    lista = []
    lista_pom = []

    s = factorial(1000)
    s = str(s)

    lista = list(s)

    for i in range(len(lista)-1):
        lista_pom.append(lista[i] + lista[i+1])

    for i in range(10):
        for j in range(10):
            print(f"{i}{j} występuje w liście", lista_pom.count(str(i) + str(j)))

lz = zad1()
zad2(lz)
zad3()
l = zad4()
zad5(l)
zad6()
zad7()