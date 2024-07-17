print("\tZadanie 1:")
 
a = 2
b = 5
c = 5.0
d = 4.2

print(f"\t{a}, {b}, {c}, {d}")
print("\ta + b = ", a + b)
print("\ta + c = ", a + c)
print("\ta + d = ", a + d)
print("\ta * b = ", a * b)
print("\ta * c = ", a * c)
print("\ta * d = ", a * d)
print("\ta / b = ", a / b)
print("\ta / c = ", a / c)
print("\ta / d = ", a / d)

print("\tZadanie 2")
 
s = "kot"
t = "pies"
 
print("\ts + t = ", s + t)
print("\tt + s = ", t + s)
print("\t2 * s = ", 2 * s)

print("\tZadanie 3")
 
i = input("\tPodaj i: ")
j = input("\tPodaj j: ")
 
print("\ti + j = ", i + j)

 
print("\tZadanie 4")
 
i = input("\tPodaj i: ")
j = input("\tPodaj j: ")
 
i = str(i)
j = str(j)
print("\tstring: i + j = ", i + j)
 
i = int(i)
j = int(j)
print("\tint: i + j = ", i + j)
 
i = float(i)
j = float(j)
print("\tfloat: i + j = ", i + j)
 
 
print("\tZadanie 5")
 
a = int(input("\tPodaj pierwszą liczbe całkowitą: "))
b = int(input("\tPodaj drugą liczbę całkowita: "))
 
print("\ta % b = ", a % b)
print("\ta // b = ", a // b)

print("\tZadanie 6")
 
a = int(input("\tPodaj pierwszą liczbę całkowitą: "))
b = int(input("\tPodaj drugą liczbę całkowitą: "))
c = int(input("\tPodaj trzecią liczbę całkowitą: "))
 
if a >= 10:
    print("\n\tPierwsza liczba jest większa od 10: ", a)
if b >= 10:
    print("\tDruga liczba jest większa od 10: ", b)
if c >= 10:
    print("\tTrzecia liczba jest większa od 10: ", c)

print("\tZadanie 7")
 
a = int(input("\tPodaj liczbę całkowitą parzystą: "))
 
if (a % 2) == 0:
    print("\n\tLiczba jest liczbą parzystą.")
else:
    print("\n\tLiczba nie jest liczbą parzystą.")

 
print("\tZadanie 8")
 
rok = int(input("\tPodaj rok przestępny: "))
 
if rok % 4 and rok % 100 != 0 or rok % 400 == 0:
    print("\n\tRok jest przestępny.")
else:
    print("\n\tRok nie jest przestępny.")

 
print("\tZadanie 9")
 
import math
 
f = float(input("\tPodaj liczbę zmiennoprzecinkową: "))
 
a = math.floor(f % 10)
b = math.floor(f % 1*10)
 
print("\tPrzed przecinkiem: {}, i po przecinku: {}.".format(a, b))


print("\tZadanie 10")
 
f = float(input("\tPodaj pierwszą liczbę zmiennoprzecinkową: "))
g = float(input("\tPodaj drugą liczbę zmiennoprzecinkową: "))
 
pom1 = ""
pom2 = ""
a = ""
b = ""
 
f = str(f)
g = str(g)
 
for i in range(0, len(f)):
    if f[i] == ".":
        pom1 = f[i+1:]
        break
 
for i in range(0, len(g)):
    if g[i] == ".":
        pom2 = g[i+1:]
        a = g[:i+1] + pom1
        break
 
for i in range(0, len(f)):
    if f[i] == ".":
        b = f[:i+1] + pom2
 

print("\t", float(b), sep="")
print("\t", float(a), sep="")


print("\tZadanie 11")

i = int(input("\tPodaj podstawę potęgi: "))
j = int(input("\tPodaj wykładnik potęgi: "))

wynik_i = i ** j
wynik_j = j ** i

if wynik_i > wynik_j:
    print(f"\t{i} do {j} równe {wynik_i} jest większe od {j} do {i} równe {wynik_j}")
else:
    print(f"\t{j} do {i} równe {wynik_j} jest większe od {i} do {j} równe {wynik_i}")

print("\tZadanie 12")

pierwiastek_2 = 2 ** (1/2)
pierwiastek_3 = 3 ** (1/3)
pierwiastek_5 = 5 ** (1/5)

if pierwiastek_2 == max(pierwiastek_2, pierwiastek_3, pierwiastek_5):
    print(f"\tPierwiastek z liczby {2}^({1}/{2}) jest największy.")
elif pierwiastek_3 == max(pierwiastek_2, pierwiastek_3, pierwiastek_5):
    print(f"\tPierwiastek z liczby {3}^({1}/{3}) jest największy.")
else:
    print(f"\tPierwiastek z liczby {5}^({1}/{5}) jest największy.")

if pierwiastek_2 == min(pierwiastek_2, pierwiastek_3, pierwiastek_5):
    print(f"\tPierwiastek z liczby {2}^({1}/{2}) jest najmniejszy.")
elif pierwiastek_3 == min(pierwiastek_2, pierwiastek_3, pierwiastek_5):
    print(f"\tPierwiastek z liczby {3}^({1}/{3}) jest najmniejszy.")
else:
    print(f"\tPierwiastek z liczby {5}^({1}/{5}) jest najmniejszy.")
