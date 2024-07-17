import os

os.system("cls")

'''

print("\tZadanie 1")

for i in range(5):
    print(f"\t{i}")

print("\n")

for i in range(4, 8):
    print(f"\t{i}")

print("\n")

for i in range(1, 20, 3):
    print(f"\t{i}")



print("\tZadanie 2")

for i in range(0, 20, 2):
    print(f"{i}", end=", ")

print("\n")

for i in range(19, 1, -2):
    print(f"\t{i}")

print("\n")

for i in range(1, 11):
    print(f"\t{i ** 2}")



print("Zadanie 3")

n = int(input("\nWprowadź liczbę n: "))
m = int(input("Wprowadź liczbę m: "))

if n < m:
    for i in range(m, n, -1):
        print(i)
elif n > m:
    for i in range(m, n+1):
        print(i)



print("Zadanie 4")

n = int(input("Podaj liczbę: "))

suma = 0

for i in range(0, n+1):
    suma += i

print(suma)



print("Zadanie 5")

n = 0
suma = 0

while suma < 1000000:
    n += 1
    suma += n

print(n)
print(suma)



print("Zadanie 6")

n = 0
suma = 0

while suma < 10:
    n += 1

    suma += (1/n)

print(suma)
print(n)



print("Zadanie 7")

n = int(input("Podaj n: "))

i = 1

while i < n:
    if i**2 == n:
        print(f"{i} ** 2 = {n}")

    i += 1



print("Zadanie 8")

n = int(input("Podaj n: "))

wynik = 1

i = 1

while i <= n:
    wynik *= i
    i += 1

print(wynik)



print("Zadanie 9")

n = int(input("Podaj n: "))
m = int(input("Podaj m: "))

wynik = 1

for i in range(m):
    wynik *= n

print(wynik)



print("Zadanie 10")

n = int(input("Podaj n: "))

i = 0

for k in range(1, n+1):
    if n%k == 0:
        print(k)
        i+=1

print("\n", i, sep="")



print("Zadanie 11")

n = int(input("Podaj n: "))

i = 0

for k in range(2, n):
    if n % k == 0:
        i += + 1
        print(k)

if n == 1 or n == 0:
    print(f"\n{n} nie jest ani liczbą pierwszą, ani złożoną.")
elif i > 0:
    print("\nLiczba złożona.")
    print(i)
else:
    print("\nLiczba pierwsza.")
    print(i)

'''
'''

print("Zadanie 12")

def generator(n):
    if n < 2:
        return False

    i = 2

    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    
    return True

print("Liczby pierwsze:")

for i in range(1, 201):
    if generator(i):
        print(i, end=", ")
    

'''

print("Zadanie 12")

for j in range(1, 201):
    counter = 0
    
    for i in range(1, j+1):
        if j%i == 0:
            counter += 1
    if counter == 2:

        print(j, end=" ")