import pygame
import random as r
import TextDraw as te
import words as woo

from pygame.constants import BLEND_ALPHA_SDL2, KEYDOWN
import LinkedList as ll
import scorereader as sr

def highscore(screen):  
    pygame.init()
    clock = pygame.time.Clock()
    run = 1
    m_pos = pygame.mouse.get_pos()
    ra = r.randint(0,255)
    g = r.randint(0,255)
    b = r.randint(0,255)
    basettick = 0
    w = 0
    offset= 150
    startx = 170
    ww=0 
    flagasc = 0
    flagdec = 0
    texttick = 0
    SCOREBOARD = ll.DL()
    SCOREBOARD = sr.red()
    SCOREBOARD.sortList(2)
    order =1
    while True:
        clock.tick(28.6)
        basettick += 1.43
        texttick += 2.86
        #ra = r.randint(0,255)                                                
        #g = r.randint(0,255)
        #b = r.randint(0,255)
        screen.fill((0,0,0))
        
        if(basettick >=14.3):
            w+=1
            basettick =0 
            screen.blit(te.hscoredraw(w),(0,0))
            screen.blit(woo.wordd("Leaderboard",w,140),(495,35))
            screen.blit(woo.wordd("Top 10 scores: ",w,100),(90,110))
            screen.blit(woo.wordd("Name:",2,60),(startx+(offset*0),170))
            screen.blit(woo.wordd("-----",2,60),(startx+(offset*0),185))
            screen.blit(woo.wordd("Character:",2,60),(startx+(offset*2),170))
            screen.blit(woo.wordd("----------",2,60),(startx+(offset*2),185))
            screen.blit(woo.wordd("Score:",2,60),(startx+(offset*4.5),170))
            screen.blit(woo.wordd("------",2,60),(startx+(offset*4.5),185))
            SCOREBOARD.printDCL(2,screen)
            if m_pos[0]>940 and m_pos[1]>170:
                if m_pos[0]<970 and m_pos[1]<200:
                    screen.blit(woo.wordd("\/",2,60),(940,170))
                    flagasc =1
                    order =1
                else:
                    screen.blit(woo.wordd("\/",w,60),(940,170))
                    flagasc = 0
            else:
                screen.blit(woo.wordd("\/",w,60),(940,170))
                flagasc = 0
            if m_pos[0]>970 and m_pos[1]>170:
                if m_pos[0]<996 and m_pos[1]<200:
                    screen.blit(woo.wordd("/\\",2,60),(970,170))
                    flagdec = 1
                    order = 2
                else:
                    screen.blit(woo.wordd("/\\",w,60),(970,170))
                    flagdec = 0
            else:
                screen.blit(woo.wordd("/\\",w,60),(970,170))
                flagdec= 0
        else:
        #bg 
            screen.blit(te.hscoredraw(w),(0,0))
        #text
            screen.blit(woo.wordd("Leaderboard",w,140),(495,35))
            screen.blit(woo.wordd("Top 10 scores: ",w,100),(90,110))
            screen.blit(woo.wordd("Name:",2,60),(startx+(offset*0),170))
            screen.blit(woo.wordd("-----",2,60),(startx+(offset*0),185))
            screen.blit(woo.wordd("Character:",2,60),(startx+(offset*2),170))
            screen.blit(woo.wordd("----------",2,60),(startx+(offset*2),185))
            screen.blit(woo.wordd("Score:",2,60),(startx+(offset*4.5),170))
            screen.blit(woo.wordd("------",2,60),(startx+(offset*4.5),185))
            SCOREBOARD.printDCL(2,screen)
            if m_pos[0]>940 and m_pos[1]>170:
                if m_pos[0]<966 and m_pos[1]<200:
                    screen.blit(woo.wordd("\/",2,60),(940,170))
                    flagasc =1
                    order = 1
                else:
                    screen.blit(woo.wordd("\/",w,60),(940,170))
                    flagasc = 0
            else:
                screen.blit(woo.wordd("\/",w,60),(940,170))
                flagasc = 0
            if m_pos[0]>970 and m_pos[1]>170:
                if m_pos[0]<996 and m_pos[1]<200:
                    screen.blit(woo.wordd("/\\",2,60),(970,170))
                    flagdec = 1
                    order = 2
                else:
                    screen.blit(woo.wordd("/\\",w,60),(970,170))
                    flagdec = 0
            else:
                screen.blit(woo.wordd("/\\",w,60),(970,170))
                flagdec= 0
           
                
        m_pos = pygame.mouse.get_pos()
        print(m_pos)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if flagasc == 1 : 
                   SCOREBOARD.sortList(order)
                if flagdec == 1 :
                   SCOREBOARD.sortList(order)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    return
        pygame.display.update()      
















