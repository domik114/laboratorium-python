from os import system

system("cls")

def zad1():
    from random import randint

    f = open('liczby.txt', 'a')

    for i in range(20):
        f.write(str(randint(1, 100)) + " ")
    
    f.close()

def zad2():
    print("Zadanie 2")

    l = []

    f = open('liczby.txt', 'r')
    s = ''
    liczby = f.read()
    i = 0

    while 1:
        if liczby[i] != " ":
            s = s + str(liczby[i])
        else:
            s = int(s)
            l.append(s)
            s = ''

        if i == len(liczby)-1:
            break

        i += 1

    print(l)

    f.close()

def zad3():
    from random import randint

    f = open('gwiazdki.txt', 'a')

    for i in range(50):
        for j in range(50):
            rand = randint(1, 5)

            if rand == 1:
                f.write("*")
            else:
                f.write(" ")

        f.write("\n")

    f.close()

def zad4():
    f = open('pierwsze.txt', 'a')

    for j in range(200):
        counter = 0
    
        for i in range(1, j+1):
            if j%i == 0:
                counter += 1

        if counter == 2:    
            f.write(str(j) + " ")

    f.close()

def zad5():
    print("Zadanie 5")

    f = open('pierwsze.txt', 'r')

    l = []
    liczby = f.read()
    s = ""

    for i in range(len(liczby)):
        if liczby[i] != " ":
            s = s + liczby[i]
        else:
            s = int(s)
            l.append(s)
            s = ""

    print(l[-1])

    f.close()

#zad1()
#zad2()
#zad3()
#zad4()
zad5()