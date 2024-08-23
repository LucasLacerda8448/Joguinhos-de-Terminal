import turtle
import time

def andar(x, y):
    extra.goto(x, y)
    extra.pd()
    extra.fd(46)
    extra.pu()

def andar2(x, y):
    ponto.goto(x, y-15)
    if texto.pencolor() == 'blue':
        ponto.color("red")
    else:
        ponto.color("blue")
    ponto.write("P", False, "center", fonte2)
    ponto.forward(50)

def especifica_y(x2, y2):
    if 0 < y2 < 60:
        andar(x2, 24)
    elif 60 < y2 < 120:
        andar(x2, 84)
    elif 120 < y2 < 180:
        andar(x2, 144)
    elif 180 < y2 < 240:
        andar(x2, 204)
    elif 240 < y2 < 300:
        andar(x2, 264)
    elif 300 < y2 < 360:
        andar(x2, 324)
    elif 360 < y2 < 420:
        andar(x2, 384)
    elif 420 < y2 < 480:
        andar(x2, 444)
    elif 480 < y2 < 540:
        andar(x2, 504)
    elif 540 < y2 < 600:
        andar(x2, 560)
    else:
        return 0
    return 1

def especifica_x(x2, y2):
    if 0 < x2 < 60:
        andar(37, y2)
    elif 60 < x2 < 120:
        andar(97, y2)
    elif 120 < x2 < 180:
        andar(157, y2)
    elif 180 < x2 < 240:
        andar(217, y2)
    elif 240 < x2 < 300:
        andar(277, y2)
    elif 300 < x2 < 360:
        andar(337, y2)
    elif 360 < x2 < 420:
        andar(397, y2)
    elif 420 < x2 < 480:
        andar(457, y2)
    elif 480 < x2 < 540:
        andar(517, y2)
    elif 540 < x2 < 600:
        andar(577, y2)
    else:
        return 0
    return 1

def especifica_y2(x2, y2):
    if 4 <= y2 <= 56:
        andar2(x2, 45)
    elif 64 <= y2 <= 116:
        andar2(x2, 105)
    elif 124 <= y2 <= 176:
        andar2(x2, 165)
    elif 184 <= y2 <= 236:
        andar2(x2, 225)
    elif 244 <= y2 <= 296:
        andar2(x2, 285)
    elif 304 <= y2 <= 356:
        andar2(x2, 345)
    elif 364 <= y2 <= 416:
        andar2(x2, 405)
    elif 424 <= y2 <= 476:
        andar2(x2, 465)
    elif 484 <= y2 <= 536:
        andar2(x2, 525)
    elif 544 <= y2 <= 596:
        andar2(x2, 585)

def linha(x, y): #cada linha tem tamanho 46
    r = 0
    x2 = x - 30
    y2 = y - 15
    if 57 <= x2 <= 63 or 117 <= x2 <= 123 or 177 <= x2 <= 183 or 237 <= x2 <= 243 or 297 <= x2 <= 303 or 357 <= x2 <= 363 or 417 <= x2 <= 423 or 477 <= x2 <= 483 or 537 <= x2 <= 543:
        extra.setheading(90)
        if 57 <= x2 <= 63:
            r = especifica_y(90, y2)
        elif 117 <= x2 <= 123:
            r = especifica_y(150, y2)
        elif 177 <= x2 <= 183:
            r = especifica_y(210, y2)
        elif 237 <= x2 <= 243:
            r = especifica_y(270, y2)
        elif 297 <= x2 <= 303:
            r = especifica_y(330, y2)
        elif 357 <= x2 <= 363:
            r = especifica_y(390, y2)
        elif 417 <= x2 <= 423:
            r = especifica_y(450, y2)
        elif 477 <= x2 <= 483:
            r = especifica_y(510, y2)
        else:
            r = especifica_y(570, y2)
    elif 57 <= y2 <= 63 or 117 <= y2 <= 123 or 177 <= y2 <= 183 or 237 <= y2 <= 243 or 297 <= y2 <= 303 or 357 <= y2 <= 363 or 417 <= y2 <= 423 or 477 <= y2 <= 483 or 537 <= y2 <= 543:
        extra.setheading(0)
        if 57 <= y2 <= 63:
            r = especifica_x(x2, 75)
        elif 117 <= y2 <= 123:
            r = especifica_x(x2, 135)
        elif 177 <= y2 <= 183:
            r = especifica_x(x2, 195)
        elif 237 <= y2 <= 243:
            r = especifica_x(x2, 255)
        elif 297 <= y2 <= 303:
            r = especifica_x(x2, 315)
        elif 357 <= y2 <= 363:
            r = especifica_x(x2, 375)
        elif 417 <= y2 <= 423:
            r = especifica_x(x2, 435)
        elif 477 <= y2 <= 483:
            r = especifica_x(x2, 495)
        else:
            r = especifica_x(x2, 555)
    if r == 1:
        texto.clear()
        texto.setpos(335, 640)
        if texto.pencolor() == 'blue':
            texto.color("red")
            extra.color("red")
            texto.write("Vez do Jogador Vermelho", False, "center", fonte)
            wn.bgcolor("#ffdede")
        else:
            texto.color("blue")
            extra.color("blue")
            texto.write("Vez do Jogador Azul", False, "center", fonte)
            wn.bgcolor("#deebff")
        texto.forward(50)

def teste(x, y):
    x2 = x - 30
    y2 = y - 15
    if 4 <= x2 <= 596 and 4 <= y2 <= 596:
        extra.setheading(90)
        if 4 <= x2 <= 56:
            especifica_y2(60, y2)
        elif 64 <= x2 <= 116:
            especifica_y2(120, y2)
        elif 124 <= x2 <= 176:
            especifica_y2(180, y2)
        elif 184 <= x2 <= 236:
            especifica_y2(240, y2)
        elif 244 <= x2 <= 296:
            especifica_y2(300, y2)
        elif 304 <= x2 <= 356:
            especifica_y2(360, y2)
        elif 364 <= x2 <= 416:
            especifica_y2(420, y2)
        elif 424 <= x2 <= 476:
            especifica_y2(480, y2)
        elif 484 <= x2 <= 536:
            especifica_y2(540, y2)
        elif 544 <= x2 <= 596:
            especifica_y2(600, y2)
        
def f(x, y):
    texto.clear()
    bt.ht()
    extra.shape("square")
    extra.turtlesize(0.3)
    extra.pensize(7)
    area = turtle.Turtle()
    area.speed(0)
    area.penup()
    area.setpos(30, 15)
    area.hideturtle()
    area.pensize(7)
    area.pendown()
    for i in range(2):
        area.forward(600)
        area.left(90)
        area.forward(600)
        area.left(90)
    area.color("light gray")
    for j in range(2):
        for i in range(5):
            area.penup()
            area.forward(60)
            area.left(90)
            area.pendown()
            area.forward(600)
            area.right(90)
            area.penup()
            area.forward(60)
            area.right(90)
            area.pendown()
            area.forward(600)
            area.left(90)
        area.left(90)
    area.color("black")
    for i in range(2):
        area.forward(600)
        area.left(90)
        area.forward(600)
        area.left(90)
    texto.clear()
    texto.setpos(335, 640)
    texto.color("red")
    extra.color("red")
    texto.write("Vez do Jogador Vermelho", False, "center", fonte)
    wn.bgcolor("#ffdede")
    texto.forward(50)
    l = []
    wn.onclick(teste, btn=3)
    wn.onclick(linha, btn=1)
    turtle.mainloop()

turtle.register_shape("botao.gif")
wn = turtle.Screen()
wn.title("Jogo do Quadrado - BetaTest")
turtle.setworldcoordinates(0, 0, 670, 700)
texto = turtle.Turtle()
ponto = turtle.Turtle()
extra = turtle.Turtle()
extra.hideturtle()
texto.hideturtle()
ponto.ht()
texto.speed(0)
texto.penup()
ponto.speed(0)
ponto.pu()
extra.speed(0)
extra.penup()
fonte = ("Comic Sans MS", 25, "normal")
fonte2 = ("Arial", 25, "normal")
texto.setpos(335, 360)
texto.write("Jogo Do Quadrado", False, "center", fonte)
texto.right(90)
texto.forward(1)
bt = turtle.Turtle()
bt.ht()
bt.speed(0)
bt.pu()
bt.setpos(335, 350)
bt.shape("botao.gif")
bt.right(90)
bt.fd(37)
bt.st()
bt.onclick(f)
turtle.mainloop()
