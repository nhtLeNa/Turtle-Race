from turtle import *
import time

f_turtle = 10
b_turtle = -3
#man hinh
screen=Screen()
may=screen.textinput('yes',50)
ex=Turtle()
ex.hideturtle()
for count in range(4): #dem thoi gian
    ex.write(count,move=False,align='left',font=("Arial",16,"normal"))
    time.sleep(1)
    ex.clear()
print(may)


def create_character(char): #ham con thay the cho 3 dong trong def character set
    char.showturtle()
    char.penup()
    char.goto(-160, 80)
    char.pendown()


def character_set(char):
    if char == 'T': #set con rua
        red.color('red')
        red.shape('turtle')
        create_character(red)
        #red.showturtle()
        #red.penup()
        #red.goto(-160, 80)
        #red.pendown()
        namelist[1] = input('Name:\n')

        yellow.color('yellow')
        yellow.shape('turtle')
        yellow.showturtle()
        yellow.penup()
        yellow.goto(-160, 40)
        yellow.pendown()
        namelist[3] = input('Name:\n')

        green.color('green')
        green.shape('turtle')
        green.showturtle()
        green.penup()
        green.goto(-160, 0)
        green.pendown()
        namelist[2] = input('Name:\n')

        blue.color('blue')
        blue.shape('turtle')
        blue.showturtle()
        blue.penup()
        blue.goto(-160, -40)
        blue.pendown()
        namelist[0] = input('Name:\n')

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


speed(10) #toc do
penup()
goto(-140, 140)
penup()
column = input('Enter number of columns( Column 0 included):\n')
therace(int(column))
character = input('Choose your character ( R-Rabbits, T-Turtle.....(update later):\n')

namelist = ['', '', '', ''] #ten cua nhan vat
#khoi tao turtle cho tung con
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
bet = input('Which one would be the winner?: ')#ca cuoc
length=int(column)*20 # do dai duong dua
