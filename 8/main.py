from os import system

system("cls")

def zad1():
    print("Zadanie 1")

    f = open("p.txt", 'w')

    f.write("To zostanie dodane do pliku!\nTo bedzie w nowej linijce\n")

    f.close()

def zad2():
    print("\nZadanie 2")

    f = open('p.txt', 'r')
    
    s = f.read()
    i = 0
    while 1:
        if i == len(s):
            break
        
        if i % 3 == 0 and i != 0:
            print(f"\n{s[i]}", end="")
        else:
            print(f"{s[i]}", end="")
        i += 1

    f.close()

def zad3():
    print("\nZadanie 3")

    f = open('p.txt', 'a')

    f.write(str(input("Podaj pierwsze zdanie do wpisania: ")) + "\n")
    f.write(str(input("Podaj drugie zdanie do wpisania: ")) + "\n")

    f.close()

def zad4():
    print("\nZadanie 4")

    f = open('p.txt', 'r')

    s = f.read()
    lista = [i.lower() for i in s]
    print(f"Ilość literek a: {lista.count('a')}")

    f.close()

def zad5():
    print("\nZadanie 5")

    f = open('p.txt', 'r')

    slowo = str(input("Podaj słowo by sprawdzić czy jest ono w pliku: "))

    l = f.readlines()
    flag = False

    for i in range(len(l)):
        if slowo in l[i]:
            print("\nSłowo znajduje się w pliku!")
            print(l[i])
            flag = True

    if flag == False:
        print("\nW pliku nie znajduję się takie słowo.")

    f.close()

def zad6():
    print("\nZadanie 6")

    f = open('p.txt', 'r')
    f2 = open('p2.txt', 'a')

    literki = f.read()
    literki = list(literki)

    for i in range(len(literki)):
        if literki[i] == " ":
            literki[i] = "*"
        
        f2.write(literki[i])

    f.close()
    f2.close()

def zad7():
    print("\nZadanie 7")

    f = open('p.txt', 'r')
    f2 = open('p2.txt', 'w')

    literki = f.read()
    literki = list(literki)

    for i in range(len(literki)):
        if literki[i] == " ":
            literki[i] = "*"
        
        f2.write(literki[i].upper())

    f.close()
    f2.close()

#zad1()
#zad2()
#zad3()
#zad4()
#zad5()
#zad6()
zad7()