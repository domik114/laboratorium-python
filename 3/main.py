import os

os.system("cls")



print("Zadanie 3")

for i in range(10):
    for j in range(10):
        print("* ", end="")

    print()



print("Zadanie 4")

for i in range(0, 10):
    for j in range(0, 10):
        if i == 0 or j == 0 or j == 9 or i == 9:
            print("* ", end="")
        else:
            print("  ", end="")

    print()



print("Zadanie 5")

for i in range(0, 10):
    for j in range(0, 10):
        if i == 0 or j == 0 or j == 9 or i == 9 or i == j or i + j == 9:
            print("* ", end="")
        else:
            print("  ", end="")

    print() 



print("Zadanie 6")

for i in range(1, 11):
    for j in range(1, 11):
        if i == 1 or j == 1 or j == 10 or i == 10 or i % 2 == 0 and j % 2 == 1 or i%2 == 1 and j%2 == 0:
            print("* ", end="")
        else:
            print("  ", end="")

    print()



print("Zadanie 7")

for i in range(1, 11):
    print(f"\t{i}", end="")

print(end="\n")

for i in range(1, 11):
    print(f"{i}\t", end="")

    for j in range(1, 11):
        if i * j > 9:
            print(i*j, "\t", end="")
        else:
            print(i*j, " \t", end="")

    print()



print("Zadanie 8")

for i in range(0, 10):
    for j in range(0, 10):
        if i == 0 or j == 0 or j == 9 or i == 9 or i == j or i + j == 9:
            print("* ", end="")
        else:
            print("  ", end="")

    print()



print("Zadanie 9")

for i in range(1, 11):
    print(f"\t{i}", end="")

print(end="\n")

for i in range(1, 11):
    print(f"{i}\t", end="")

    for j in range(1, 11):
        if i ** j > j ** i:
            print(">", "\t", end="")
        elif i ** j < j ** i:
            print("<", " \t", end="")
        elif i ** j == j ** i:
            print("=", "\t", end="")

    print()



print("Zadanie 10")

for i in range(10):
    for j in range(10):
        if ((i == 0) or (i == 9)) and ((j < 3) or (j > 6)):
            print(f"  ", end="")
        elif ((i == 1) or (i == 8)) and ((j < 2) or (j > 7)):
            print(f"  ", end="")
        elif ((i == 2) or (i == 7)) and ((j < 1) or (j > 8)):
            print(f"  ", end="")
        elif ((i == 3) or (i == 6)) and ((j < 0) or (j > 9)):
            print(f"  ", end="")
        else:
            print(f"* ", end="")
            
    print()

print()

for i in range(10):
    for j in range(10):
        if ((i == 0) or (i == 9)) and ((j < 3) or (j > 6)):
            print(f"  ", end="")
        elif ((i == 1) or (i == 8)) and ((j < 2) or (j > 7) or (j > 2) and (j < 7)):
            print(f"  ", end="")
        elif ((i == 2) or (i == 7)) and ((j < 1) or (j > 8) or (j > 1) and (j < 8)):
            print(f"  ", end="")
        elif ((i == 3) or (i == 4) or (i == 5) or (i == 6)) and ((j < 0) or (j > 9) or (j > 0) and (j < 9)):
            print(f"  ", end="")
        else:
            print(f"* ", end="")
            
    print()