from os import system

system("cls")

def zad1():
    print("Zadanie 1")
 
    a = 5
    b = 10
 
    print(f"a = {a}")
    print(f"b = {b}")
 
    c = a
    a = b
    b = c
 
    print(f"a = {a}")
    print(f"b = {b}")
 
def zmien(a, b):
    c = a
    a = b
    b = c
 
    print("W funkcji:")
    print(f"a = {a}")
    print(f"b = {b}")
 
def zad2():
    print("\nZadanie 2")
 
    a = 5
    b = 10
 
    zmien(a, b)
 
    print("Poza funkcją:")
    print(f"a = {a}")
    print(f"b = {b}")
 
def zamien(l):
    a = l[0]
    l[0] = l[1]
    l[1] = a
 
    print("W funkcji:")
    print(l)
 
def zad3():
    print("\nZadanie 3")
 
    l = [10, 50]
 
    zamien(l)
 
    print("Po zastosowaniu funkcji:")
    print(l)
 
def odwroc(l):
    l = l[::-1]
 
    print("W funkcji:")
    print(l)
 
def zad4():
    print("\nZadanie 4")
 
    l = [1, 5, 4, 3]
 
    odwroc(l)
 
    print("Po zastosowaniu funkcji:")
    print(l)
 
def sortuj(l):
    n = len(l)
 
    while n > 1:
        flag = False
 
        for i in range(0, n-1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                flag = True
 
        n -= 1
        if flag == False:
            break
 
    print("W funkcji:")
    print(l)
 
def zad5():
    print("\nZadanie 5")
 
    from random import randint
 
    l = []
 
    for i in range(randint(1, 100)):
        l.append(randint(0, 100))
 
    sortuj(l)

    li = ["przykladowe", "zdanie", "dla", "testu"]
    odwroc(li)
 
    print("Po zastosowaniu funkcji:")
    print(l)
    print(li)
    print(li[1] > li[2])

def sortuj_zad_6(l):
    n = len(l)
 
    while n > 1:
        flag = False
 
        for i in range(n-1):
            pom1, pom2 = str(l[i]), str(l[i+1])
            pom1 = pom1.lower()
            pom2 = pom2.lower()

            if pom1 > pom2:
                l[i], l[i+1] = l[i+1], l[i]
                flag = True
 
        n -= 1
        if flag == False:
            break
    
    print(l)

    n = len(l)

    while n > 1:
        flag = False

        for i in range(n-1):
            if len(l[i]) > len(l[i+1]):
                l[i], l[i+1] = l[i+1], l[i]
                flag = True
 
        n -= 1
        if flag == False:
            break
    
    print(l)

def zad6():
    print("\nZadanie 6")
 
    zdanie = str(input("Podaj zdanie: "))
    l = []
    count = 0
    zd = ""
 
    for i in range(len(zdanie)):
        if zdanie[i] == " ":
            l.append(zd)
            zd = ""
            count = 0
        else: zd = zd + zdanie[i]
 
        if i == len(zdanie)-1:
            l.append(zd)

        count += 1
 
    print(l)

    sortuj_zad_6(l)
 
def zad7():
    print("\nZadanie 7")

    from random import randint, choice

    lista = []
    lista_int = []
    samogloski = ['a', 'e', 'i', 'o', 'u', 'y']
    tekst = ""

    for i in range(100):
        ran = randint(3, 8)
        
        for j in range(ran):   
            if j % 3 == 0:
                sam = choice(samogloski)
                sam = str(sam)
                tekst += sam
                lista_int.append(ord(sam))
                continue

            ran_int = randint(97, 122)
            lista_int.append(ran_int)

            if len(lista_int) == 1:
                tekst += chr(ran_int)            
            elif lista_int[-1] == ran_int:
                if ran_int == 122:
                    lista_int.append(ran_int-2)
                    tekst += chr(ran_int-2)
                else:
                    lista_int.append(ran_int+1)
                    tekst += chr(ran_int+1)

        lista.append(tekst)
        tekst = ""

    n = len(lista)

    while n > 1:
        flag = False
 
        for i in range(n-1):
            pom1, pom2 = str(lista[i]), str(lista[i+1])
            pom1 = pom1.lower()
            pom2 = pom2.lower()

            if pom1 > pom2:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                flag = True
 
        n -= 1
        if flag == False:
            break

    print(lista)
 
#zad1()
#zad2()
#zad3()
#zad4()
#zad5()
#zad6()
zad7()