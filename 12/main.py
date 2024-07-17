def zera(a, b):
    return [[0 for i in range(a)] for j in range(b)] 

def losowa(a, b, n):
    from random import randint

    l = zera(a, b)

    for i in range(0, len(l)):
        for j in range(0,len(l[i])):
            l[i][j] = randint(1, n)

    return l

def wyswietl1(l):
    for i in range(len(l)):
        for j in range(len(l[i])):
            print(l[i][j], end = " ")
        print()
    print()

def Gauss(macierz):
    from copy import deepcopy

    macierz_2 = deepcopy(macierz)

    for i in range(len(macierz[0])):
        for j in range(i+1, len(macierz)):
            if macierz_2[i][i] == 0:
                break

            macierz_3 = macierz_2[j][i] / macierz_2[i][i]

        for k in range(len(macierz) - 1):
             macierz_2[j][k] = macierz_2[j][k] - macierz_3 * macierz_2[i][k]

    return macierz_2

def zad1():
    print("----Zadanie 1----\n")

    macierz = losowa(3, 4, 5)
    wyswietl1(macierz)

    wynik = Gauss(macierz)
    wyswietl1(wynik)

def gauss(A):
    from copy import deepcopy
    B = deepcopy(A)
    for i in range(len(A[0])):
        for j in range(i+1, len(A)):
            if B[i][i] == 0:
                break
            C = B[j][i] / B[i][i]
            for k in range(len(A) - 1):
                B[j][k] = B[j][k] - C * B[i][k]
    return B

def wyswietl(A):
    alen = len(A)
    blen = len(A[0])
    for i in range(0, alen):
        string = ""
        for j in range(0, blen):
            string += str(A[i][j])
            string += " "
    print(string)

def losowa1():
    from random import randint

    a = 3
    b = 4
    n = 4

    M = [[0 for i in range(a)] for j in range(b)]

    for i in range(0, b):
        for j in range(0, a):
            M[i][j] = randint(1, n)

    return M

def rz(A):
    count = 0

    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] != 0:
                counter += 1
                break

    return count

def zad2():
    print("----Zadanie 2----\n")

    for i in range(0, 100):
        m1 = losowa1()
        m2 = gauss(m1)
        m3 = rz(m2)

        if m3 < 3:
            print("\nMacierz:")
            wyswietl(m1)

            print("Postac schodkowa:")
            wyswietl(m2)

            input("Press ANY key to continue...")

def wyswietl3(A):
    a = len(A)
    b = len(A[0])

    for i in range(0, a):
        string = ""

        for j in range(0, b):
            string += str(A[i][j])
            string += " "

        print(string)

def gauss2(A):
    B = gauss(A)

    for i in range(len(A)):
        for j in range(len(A[0])):
            if B[i][j] != 0:
                B[i][j] = 1

                for k in range(j+1, len(A[0])):
                    B[i][k] = 0

                continue
    for i in range(len(A)):
        for j in range(len(A[0])):
            B[i][j] = int(B[i][j])

    return B

def zad3():
    print("----Zadanie 2----\n")

    macierz = [
        [4,5,9],
        [10,9,1],
        [7,2,0],
        [3,5,6]]

    wyswietl3(macierz)
    A = gauss2(macierz)

    print("")
    wyswietl3(A)



def gauss3(a):
    for i in range(len(a)):
        if a[i][i] == 0:
            for j in range(i+1, len(a)):
                if a[i][j] != 0:
                    a[i], a[j] = a[j], a[i]
                    break
            else:
                raise ValueError("Matrix is not invertible")
        for j in range(i+1, len(a)):
            elim(a[i], a[j], i)
    for i in range(len(a)-1, -1, -1):
        for j in range(i-1, -1, -1):
            elim(a[i], a[j], i)
    for i in range(len(a)):
        elim(a[i], a[i], i, target=1)
    return a

def elim(a, b, col, target=0):
    c = (b[col]-target) / a[col]
    
    for i in range(len(b)):
        b[i] -= c * a[i]

def odwr(a):
    tmp = [[] for _ in a]

    for i,row in enumerate(a):
        assert len(row) == len(a)
        tmp[i].extend(row + [0]*i + [1] + [0]*(len(a)-i-1))
        
    gauss3(tmp)

    b = []

    for i in range(len(tmp)):
        b.append(tmp[i][len(tmp[i])//2:])

    return b

def zad4():
    print("----Zadanie 4----\n")
    import numpy

    macierz = [
        [4,5,9],
        [10,9,1],
        [7,2,0]]

    macierz2 = [
        [4,5,9],
        [10,9,1],
        [7,2,0]]

    wyswietl3(macierz)
    A = gauss2(macierz)

    B = odwr(macierz2)

    print()
    wyswietl3(B)
    print()

    print(numpy.linalg.inv(macierz))

if __name__ == '__main__':
    from os import system
    system("cls")

    #zad1()
    #zad2()
    #zad3()
    zad4()