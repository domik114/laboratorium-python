from graphics import *

def zad1():
    from time import sleep

    win = GraphWin('zad 1', 800, 500)
    win.setBackground('white')

    o = Oval(Point(250, 40), Point(300, 180))
    o.setFill("blue")

    c=Circle(Point(300, 300), 50)
    c.setFill('red')

    p = Rectangle(Point(200, 50),Point(350, 80))
    p.setFill('green')

    o.draw(win)
    c.draw(win)
    p.draw(win)

    for i in range(35):
        c.move(0, -6.2)
        sleep(1/10)

    win.getMouse()
    win.close()

def zad2():
    win = GraphWin('zad 2', 800, 500)
    win.setBackground('white')

    c = Circle(Point(300, 300), 50)
    c.setFill('red')

    c.draw(win)

    while True:
        k = win.getKey()

        if k == 'a': c.move(-20, 0)
        if k == 'd': c.move(20, 0)
        if k == 'w': c.move(0, -20)
        if k == 's': c.move(0, 20)
        if k == 'q': break

    win.close()

def zad3():
    from random import randint
    from time import sleep

    win = GraphWin('Zad 3', 800, 500)
    win.setBackground('white')

    c = Circle(Point(400, 250), 50)
    c.draw(win)

    while True:
        kierunek = randint(1, 4)

        if kierunek == 1: 
            c.move(-20, 0)
            sleep(1/5)
        if kierunek == 2: 
            c.move(20, 0)
            sleep(1/5)
        if kierunek == 3: 
            c.move(0, -20)
            sleep(1/5)
        if kierunek == 4: 
            c.move(0, 20)
            sleep(1/5)
    
    win.close()

def zad4():
    from random import uniform
    from time import sleep
    from math import cos, sin

    win = GraphWin('Zad 4', 800, 500)
    win.setBackground('white')
    c = Circle(Point(400, 250), 50)    

    alfa = 0

    while(True):
        c.draw(win)

        sleep(0.1)
        kat = uniform(-0.3, 0.3)
        alfa = alfa + kat

        x = 10 * cos(alfa)
        y = 10 * sin(alfa)
        
        c.move(x, y)
        c.undraw()

    win.getMouse()
    win.close()

def zad5():
    from random import uniform
    from time import sleep
    from math import cos, sin

    win = GraphWin('Zad 4', 800, 500)
    win.setBackground('white')
    c = Circle(Point(400, 250), 50)    

    alfa = 0
    xp = 400
    yp = 250

    while(True):
        c.draw(win)

        sleep(0.1)
        kat = uniform(-0.3, 0.3)
        alfa = alfa + kat

        x = 10 * cos(alfa)
        y = 10 * sin(alfa)
        
        c.move(x, y)

        xp = xp + x
        yp = yp + y

        if (xp < 50):
            alfa = 0
            c.move(15, 0)
            xp = xp + 15

        if (yp < 50):
            alfa = 90
            c.move(0, 15)
            yp = yp + 15

        if (xp > 750):
            alfa = 180
            c.move(-15, 0)
            xp = xp - 15

        if (yp > 450):
            alfa = 180
            c.move(0, 15)
            yp = yp - 15

        c.undraw()

    win.getMouse()
    win.close()

def zad6():
    from time import sleep
    from math import cos,sin

    win = GraphWin('Zad 6', 800, 500)
    win.setBackground('white')

    o = Circle(Point(400, 250), 30)
    o.setOutline('black')
    o.setWidth(1)
    o.setFill('blue')
    o.draw(win)

    o2 = Circle(Point(400, 150), 30)
    o2.setOutline('black')
    o2.setWidth(1)
    o2.draw(win)

    alfa = 0

    while(True):
        alfa += 0.1
        x = 10*cos(alfa)
        y = 10*sin(alfa)

        o2.move(x,y)

        time.sleep(1/30)

    win.getMouse()
    win.close()

def zad7():
    import random
    import time
    from math import cos,sin

    win = GraphWin('Mojeokno',1000,600)
    win.setBackground('black')
    okrag = Circle(Point(500,300),30)
    okrag.draw(win)
    okrag2 = Circle(Point(250,150),60)
    okrag.setFill('blue')
    okrag2.draw(win)
    alfa = 0

    while(True):
        alfa += 0.1
        x = 10*cos(alfa)
        y = 10*sin(alfa)
        okrag2.move(x,y)
        time.sleep(1/60) #60 FPS

if __name__ == '__main__':
    #zad1()
    #zad2()
    zad3()
    #zad4()
    #zad5()
    #ad6()
    #zad7()