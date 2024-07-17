from graphics import *

def zad1():
    win = GraphWin('Zad 1', 800, 200)
    win.setBackground('cyan')

    x, y = 10, 50
    pt = Point(x, y)
    pt.setOutline('black')    
    pt.draw(win)
    win.getMouse()
    win.close()

def zad2():
    from random import randint, choice

    win = GraphWin('Zad 2', 800, 500)
    win.setBackground('black')
    colors = ['red', 'blue', 'yellow']

    for i in range(1000):
        x, y = randint(1, 799), randint(1, 499)
        pt = Point(x, y)
        color = choice(colors)
        pt.setOutline(color)    
        pt.draw(win)

    win.getMouse()
    win.close()

def zad3():
    from random import randint, choice
    from time import sleep

    win = GraphWin('Zad 3', 800, 500)
    win.setBackground('white')
    colors = ['green', 'blue', 'red', 'black']

    for i in range(50):
        c = Circle(Point(randint(30, 770), randint(30, 470)), randint(10, 30))
        color = choice(colors)
        c.setOutline(color)
        c.setFill(color)
        c.draw(win)
        sleep(0.1)

    win.getMouse()
    win.close()

def zad4():
    win = GraphWin('Zad 3', 800, 500)
    win.setBackground('white')

    o = Oval(Point(150, 150), Point(50, 50))
    o.draw(win)

    r = Rectangle(Point(200, 200), Point(300, 300))
    r.draw(win)

    win.getMouse()
    win.close()

def zad5():
    win = GraphWin('Zad 3', 800, 500)
    win.setBackground('white')

    l = Line(Point(100, 100), Point(200, 200))
    l2 = Line(Point(200, 200), Point(300, 150))

    l3 = Line(Point(300, 150), Point(400, 400))
    l4 = Line(Point(400, 400), Point(440, 440))

    l5 = Line(Point(440, 440), Point(440, 470))
    l6 = Line(Point(440, 470), Point(350, 470))

    l7 = Line(Point(350, 470), Point(350, 450))
    l8 = Line(Point(350, 450), Point(10, 450))

    l9 = Line(Point(10, 450), Point(100, 10))
    l10 = Line(Point(100, 10), Point(100, 100))
    
    l.draw(win)
    l2.draw(win)
    l3.draw(win)
    l4.draw(win)
    l5.draw(win)
    l6.draw(win)
    l7.draw(win)
    l8.draw(win)
    l9.draw(win)
    l10.draw(win)

    win.getMouse()
    win.close()

def zad6():
    from random import randint, choice
    from math import sin, cos, pi

    win = GraphWin('Zad 6', 800, 500)
    win.setBackground('white')

    n = int(input("Podaj n: "))
    tab = []

    for i in range(n):
        x = 400 + 400 * cos(2 * pi * i/n)
        y = 250 + 250 * sin(2 * pi * i/n)
        tab.append(Point(x, y))

    for i in range(n):
        l = Line(tab[i % n], tab[(i + 1) % n])
        l.draw(win)

    win.getMouse()
    win.close()

if __name__ == '__main__':
    #zad1()
    #zad2()
    #zad3()
    #zad4()
    #zad5()
    zad6()