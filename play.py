import pygame
pygame.init()

win_sound = pygame.mixer.Sound("win.ogg")
lose_sound = pygame.mixer.Sound("lose.ogg")
pygame.mixer.music.load("play_turtle.ogg")

from start import *
from random import randint

def movingbackward(char, number):#di lui
    char.setheading(180)
    char.forward(0 - number)

def play_music():
    pygame.mixer.music.play(-1)

def racing():

    play_music()
    d1 = 0 #random vi tri di truoc
    d2 = 0
    d3 = 0
    d4 = 0
    rank_val = 0 #bien xep hang
    while d1 < length or d2 < length or d3 < length or d4 < length:
        if d1 < length:
            random = randint(1, 4) #cho random tu 1->4
        else:
            random = 0 #neu toi dich roi thi k dua nua
        if d2 < length:
            random2 = randint(1, 4)
            while random2 == random: #random nhung phai khac voi so da duoc random truoc
                random2 = randint(1, 4)
        else:
            random2 = 0
        if d3 < length:
            random3 = randint(1, 4)
            while random3 == random2 or random3 == random:
                random3 = randint(1, 4)
        else:
            random3 = 0
        if d4 < length:
            random4 = randint(1, 4)
            while random4 == random3 or random4 == random2 or random4 == random:
                random4 = randint(1, 4)
        else:
            random4 = 0
        List = [random, random2, random3, random4]
        for count in range(4):
            if List[count] == 1 and d1 < length:
                move = randint(b_turtle, f_turtle) #random buoc di
                if move == 0:
                    move = randint(b_turtle, f_turtle) #khong cho dung lai
                if move < 0:
                    if blue.xcor() <= -140: #o vach xuat phat khong duoc di lui
                        move = randint(0, f_turtle)
                    else:
                        movingbackward(blue, move)
                if move > 0:
                    blue.setheading(0)
                    blue.forward(move)
                d1 += move
            if d1 >= length and pointlist[0] == 0:
                rank_val += 1
                pointlist[0] += rank_val

            if List[count] == 2 and d2 < length:
                move = randint(b_turtle, f_turtle)
                if move == 0:
                    move = randint(b_turtle, f_turtle)
                if move < 0:
                    if red.xcor() <= -140:
                        move = randint(0, f_turtle)
                    else:
                        movingbackward(red, move)
                if move > 0:
                    red.setheading(0)
                    red.forward(move)
                d2 += move
            if d2 >= length and pointlist[1] == 0:
                rank_val += 1
                pointlist[1] += rank_val

            if List[count] == 3 and d3 < length:
                move = randint(b_turtle, f_turtle)
                if move == 0:
                    move = randint(b_turtle, f_turtle)
                if move < 0:
                    if green.xcor() <= -140:
                        move = randint(0, f_turtle)
                    else:
                        movingbackward(green, move)
                if move > 0:
                    green.setheading(0)
                    green.forward(move)
                d3 += move
            if d3 >= length and pointlist[2] == 0:
                rank_val += 1
                pointlist[2] += rank_val

            if List[count] == 4 and d4 < length:
                move = randint(b_turtle, f_turtle)
                if move == 0:
                    move = randint(b_turtle, f_turtle)
                if move < 0:
                    if yellow.xcor() <= -140:
                        move = randint(0, f_turtle)
                    else:
                        movingbackward(yellow, move)
                if move > 0:
                    yellow.setheading(0)
                    yellow.forward(move)
                d4 += move
            if d4 >= length and pointlist[3] == 0:
                rank_val += 1
                pointlist[3] += rank_val


def winner(): #kiem tra thang thua
    m = 5
    for c in range(4):
        if pointlist[c] < m:
            m = pointlist[c]
    win = namelist[c]
    print('The winner is:\n', win)
    if bet == win:
        pygame.mixer.Sound.play(win_sound)
        pygame.mixer.music.stop()
        print('You won the bet')
    else:
        pygame.mixer.Sound.play(lose_sound)
        pygame.mixer.music.stop()
        print('You lost the bet')

#while True:
    pointlist = [0, 0, 0, 0]
    racing()
    print(pointlist)
    winner()
   # tmp = input('You want to play again ? (Y/N) ')
   # if tmp == 'N':
   #     break




