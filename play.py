from os import startfile
from typing import NamedTuple
import pygame
import numpy as np
import random as r
import time as t
import SOLUTIONCHEKCER as aas
import mazegenerator as maaz
import TextDraw 
import words as woo
import HIGHSCOER as hoooo
pygame.init()
fps = 100
fpsclock = pygame.time.Clock()
run = 1

def collider(array,x,y):
    ground = np.empty([1080,600],dtype = int)
    for a in range(0,1080):
        for b in range(0,600):
            ground[a,b] = 0

    for a in range(0,20):
        for b in range(0,15):
                c = array[b,a]
                ground[a*40,b*40] = c
    print(ground)
        

def createmaze():
    ra = r.randint(0,9)
    prrr = maaz.ret_maze(ra)
    arrayy = np.array(prrr)
    arrayy.transpose(1,0)
    return arrayy

def appendfile(finalstr):
    sco = open("scores.txt","a")
    sco.write(finalstr)
    sco.close()

def drawwall(screen,x,y):
    screen.blit(TextDraw.mis_draw(1),(x,y))

def drawmapsss(screen,arr):
    for a in range(0,20):
        for b in range(0,15):
            if(arr[b,a]==0):
                drawwall(screen,(a*40)+280,(b*40)+84)
            

            
            
def playnow(screen):
    pygame.init()
    clock = pygame.time.Clock()
    X= 280
    Y= 84
    step = 8 
    imgnew =TextDraw.ch_draw()
    drawmapsss(screen,createmaze())
    arr = createmaze()
    ground = collider(arr,X,Y)
    STARTSCORE = 4000
    scoretick = 0
    while True:
        mpos = pygame.mouse.get_pos()
        print(mpos)
        clock.tick(24)
        scoretick+=1
        screen.fill((0,0,0))
        screen.blit(TextDraw.playbgdraw(),(0,0))
        screen.blit(woo.wordd("Score:",2,100),(1100,260))
        if scoretick >=48:
            scoretick = 0
            STARTSCORE -= 200
        screen.blit(woo.wordd(str(STARTSCORE),2,100),(1110,310))

       
        screen.blit(imgnew,(X,Y))
        drawmapsss(screen,arr)
        pygame.display.update()
        for eve in pygame.event.get():
            if eve.type==pygame.QUIT:
                pygame.quit()
        pressd = pygame.key.get_pressed()
        if pressd[pygame.K_LEFT]:
            X -= step
            if(X < 280):
                X = 287
            imgnew = TextDraw.ch_rot_draw(-180)
        if pressd[pygame.K_RIGHT]:
            X += step
            if(X > 1045):
                if (Y >=634):
                    break
                else:
                    X = 1036        
            imgnew = TextDraw.ch_rot_draw(180)
        if pressd[pygame.K_UP]:
            Y -= step
            if(Y < 84):
                Y = 90
            imgnew = TextDraw.ch_rot_draw(90)
        if pressd[pygame.K_DOWN]:
            Y += step
            if(Y > 649):
                 if (X >=1030):
                    break
                 else:
                    Y = 640
            imgnew = TextDraw.ch_rot_draw(-90)
        if pressd[pygame.K_BACKSPACE]:
            return
    screen.blit(woo.wordd(("Your score: " +str(STARTSCORE)),2,200),(300,400))
    pygame.display.update()
    charr = "black"
    name33= str(input())
    finalstring = "$"+charr+"@"+name33+"#"+str(STARTSCORE)+"^"
    appendfile(finalstring)
    hoooo.highscore(screen)
    
