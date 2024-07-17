from os import system

system("cls")

def zad1():
    print("---Zadanie 1----")

    A = [[1, 2], [3, 4]]
    print(A)

    for i in range(len(A)):
        for j in range(len(A[i])):
            print(A[i][j], end = " ")
        
        print()

def zera(a, b):
    return [[0 for i in range(a)] for j in range(b)] 

def id(n):
    from numpy import eye
    
    l = [[0 for i in range(n)] for j in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i == j:
                l[i][j] = 1

    return l

def wyswietl(l):
    for i in range(len(l)):
        for j in range(len(l[i])):
            print(l[i][j], end = " ")
        print()
    print()

def zad2():
    print("\n---Zadanie 2----")   

    l = zera(2, 5)
    wyswietl(l)
    print()

    l2 = id(10)

    wyswietl(l2)

def losowa(a, b, n):
    from random import randint

    l = zera(a, b)

    for i in range(0, len(l)):
        for j in range(0,len(l[i])):
            l[i][j] = randint(1, n)

    return l

def dodaj(l, l2):
    suma = zera(len(l[0]), len(l))

    if len(l) != len(l2) or len(l[0]) != len(l2[0]):
        return []

    for i in range(len(suma)):
        for j in range(len(suma[i])):
            suma[i][j] = l[i][j] + l2[i][j]

    return suma

def zad3():
    print("\n---Zadanie 3----")

    l = losowa(2, 3, 10)
    l2 = losowa(2, 3, 10)
    l3 = losowa(3, 2, 10)

    wyswietl(l)
    wyswietl(l2)
    wyswietl(l3)

    print(f"Dodanie l + l2: {dodaj(l, l2)}")
    print(f"Dodanie l3 + l2: {dodaj(l3, l2)}")

def pomnoz(l, l2):
    mnozenie = zera(len(l[0]), len(l2))

    if len(l[0]) != len(l2) or len(l) != len(l2[0]):
        return []

    for i in range(len(l)):
        for j in range(len(l2[0])):
           for k in range(len(l2)):
               mnozenie[i][j] += l[i][k] * l2[k][j]

    return mnozenie

def zad4():
    print("\n---Zadanie 4----")

    l = losowa(2, 2, 10)
    l2 = losowa(2, 2, 10)
    l3 = losowa(2, 3, 10)

    wyswietl(l)
    wyswietl(l2)
    wyswietl(l3)

    print(f"Mnożenie l * l2: {pomnoz(l, l2)}")
    print(f"Mnożenie l3 * l2: {pomnoz(l3, l2)}")

def zamW(A, i, j):
    B = A[::]

    a = A[i-1]
    b = A[j-1]

    B[i-1] = b
    B[j-1] = a

    return B

def przemW(A, i, k):
    B = A.copy()

    a = B[i-1].copy()

    for j in range(len(a)):
        a[j] *= k

    B[i-1] = a

    return B

def dodajW(A, i, j, k):
    B = A[::]
    b = B[i-1].copy()
    c = B[j-1].copy()

    for x in range(len(c)):
        c[x] *= k

    for z in range(len(b)):
        b[z] += c[z]

    B[i-1] = b

    return B

def zad5():
    print("\n----Zadanie 5----")

    l = losowa(4, 4, 10)
    l2 = losowa(4, 4, 10)
    l3 = losowa(4, 4, 10)
    wyswietl(l)
    wyswietl(l2)
    wyswietl(l3)
    
    print("Funkcja zamW:")
    zam = zamW(l, 2, 1)
    wyswietl(zam)

    print("Funkcja przemW:")
    przem = przemW(l2, 2, 10)
    wyswietl(przem)

    print("Funkcja dodajW:")
    dodaj = dodajW(l3, 2, 3, 10)
    wyswietl(dodaj)
    #print(dodaj)

def zad6():
    print("\n---Zadanie 6----")

    
if __name__ == '__main__':
    zad1()
    zad2()
    zad3()
    zad4()
    zad5()
    #zad6()