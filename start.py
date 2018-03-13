
from turtle import *
import time

f_turtle = 10
b_turtle = -3

class point_history:
    fisrt = 0
    second = 0
    third = 0
    fourth = 0

#man hinh

screen=Screen()
may=screen.textinput("Name","Enter your character name:");
ex=Turtle()
ex.hideturtle()


for count in range(1,4,1): #dem thoi gian
    ex.write(count,move=False,align='left',font=("Arial",16,"normal"))
    time.sleep(1)
    ex.clear()



def create_character(char, loca_y): #ham con thay the cho 3 dong trong def character set
    char.showturtle()
    char.penup()
    char.goto(-160, loca_y)
    char.pendown()
    char.penup()


def character_set(char):
    if char == 'T': #set con rua
        red.color('red')
        red.shape('turtle')
        create_character(red, 80)
        namelist[0] = screen.textinput("Name","Enter your character name:");

        yellow.color('yellow')
        yellow.shape('turtle')
        create_character(yellow, 40)
        namelist[1] = screen.textinput("Name","Enter your character name:");

        green.color('green')
        green.shape('turtle')
        create_character(green, 0)
        namelist[2] = screen.textinput("Name","Enter your character name:");

        blue.color('blue')
        blue.shape('turtle')
        create_character(blue, -40)
        namelist[3] = screen.textinput("Name","Enter your character name:");

    elif char == 'D':
        red_disa = "red.gif"
        screen.addshape("red.gif")
        red.shape(red_disa)
        create_character(red, 80)
        namelist[0] = screen.textinput("Name","Enter your character name:");

        yellow_disa = "yellow.gif"
        screen.addshape("yellow.gif")
        yellow.shape(yellow_disa)
        create_character(yellow, 40)
        namelist[1] = screen.textinput("Name","Enter your character name:");

        green_disa = "green.gif"
        screen.addshape("green.gif")
        green.shape(green_disa)
        create_character(green, 0)
        namelist[2] = screen.textinput("Name","Enter your character name:");

        blue_disa = "blue.gif"
        screen.addshape("blue.gif")
        blue.shape(blue_disa)
        create_character(blue, -40)
        namelist[3] = screen.textinput("Name","Enter your character name:");

#ve duong dua
def therace(col):
    for a in range(int(col)):
        write(a, align='center')
        right(90)
        penup()
        forward(20)
        for b in range(7):
            pendown()
            forward(15)
            penup()
            forward(15)
        backward(230)
        left(90)
        penup()
        forward(20)


speed(10)  # toc do
penup()
goto(-140, 140)
penup()

while True:
    column = screen.textinput("", "Enter number of column:")
    if int(column) <= 40:
        break
therace(int(column))
character = screen.textinput("", "Choose your character (R\T):\n")

namelist = ['', '', '', '']  # ten cua nhan vat
    # khoi tao turtle cho tung con
red = Turtle()
red.hideturtle()
blue = Turtle()
blue.hideturtle()
green = Turtle()
green.hideturtle()
yellow = Turtle()
yellow.hideturtle()
character_set(character)

print(namelist)
bet = screen.textinput("", "Which one would be the winner?:")  # ca cuoc
length = int(column) * 20  # do dai duong dua

