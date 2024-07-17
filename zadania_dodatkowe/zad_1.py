class Circle:
    def __init__(self, promien, liczba_probek):
        self.promien = promien
        self.liczba_probek = liczba_probek

    def __str__(self):
        return 'Promień koła: ' + str(self.promien) + ', Liczba próbek: ' + str(self.liczba_probek)
    
    def pole(self):
        from math import pi, pow
        wynik = pi * pow(self.promien, 2)

        return wynik

    def poleMC(self):
        from random import random
        from math import sqrt

        x = None
        y = None
        srodek = 0

        for i in range(self.liczba_probek):
            x = random() * 2
            y = random() * 2

            if (sqrt((x - 1) * (x - 1) + (y - 1) * (y - 1)) <= 1):
                srodek += 1

        pole = (4 * srodek / self.liczba_probek) * 100

        return pole



if __name__ == '__main__':
    kolo1 = Circle(10, 10)
    kolo2 = Circle(10, 1000)
    kolo3 = Circle(10, 1000000)

    print(kolo1)
    print(kolo2)
    print(kolo3)

    print(kolo1.pole(), kolo1.poleMC())
    print(kolo2.pole(), kolo2.poleMC())
    print(kolo3.pole(), kolo3.poleMC())