import pygame
import TextDraw as gee
import random as r
import ALPHABET as alph
import words as wee
clock = pygame.time.Clock()

def credit(screen):
    #screen display stuff=-=-=-=-=-=-=-=-=-=-=---=-=--=-=-=--=
    pygame.init()
    clock = pygame.time.Clock()
    run = 1
    ra = r.randint(0,255)
    g = r.randint(0,255)
    b = r.randint(0,255) 
    spiraltick = 0
    v= 0
    w= 0
    ypos = 300
    enttick = 0
    framecount = 0
    while (run==1):
        clock.tick(18.75)
        framecount +=1.65
        spiraltick+=1.65
        if spiraltick >8.25:
            w =0
            spiraltick =0 
        else:
            w+=1
        screen.blit(gee.creddraw(w),(0,0))
        rh = r.randint(0,8)
        screen.blit(wee.wordThatsit[rh],(0,-20))
        screen.blit(wee.wordThatsit[rh],(0,30))
        screen.blit(wee.wordThatsit[rh],(0,70))
        screen.blit(wee.wordThatsit[rh],(0,110))
        screen.blit(wee.wordThatsit[rh],(0,150))
        screen.blit(wee.wordThatsit[rh],(0,190))
        screen.blit(wee.wordThatsit[rh],(0,230))
        screen.blit(wee.wordThatsit[rh],(0,270))
        screen.blit(wee.wordThatsit[rh],(0,310))
        screen.blit(wee.wordThatsit[rh],(0,350))
        screen.blit(wee.wordThatsit[rh],(0,390))
        screen.blit(wee.wordThatsit[rh],(0,430))
        screen.blit(wee.wordThatsit[rh],(0,470))
        screen.blit(wee.wordThatsit[rh],(0,510))
        screen.blit(wee.wordThatsit[rh],(0,550))
        screen.blit(wee.wordThatsit[rh],(0,590))
        screen.blit(wee.wordThatsit[rh],(0,630))
        screen.blit(wee.wordThatsit[rh],(0,670))
        screen.blit(wee.wordThatsit[rh],(0,710))
        screen.blit(wee.wordThatsit[rh],(0,750))
        if framecount<=123.75:
            #entanglemtn
            enttick +=1.65
            if enttick >=19.8:
                enttick =0
                if(v>=9):
                    v=0
                else:
                    v+=1
            startpos = 300
            screen.blit(wee.wordEntanglement[v],(300,300))
        elif framecount >=123.75 and framecount <=247.5:
                screen.blit(wee.wordMadeBy[0],(250,200))
                screen.blit(wee.wordMadeBy[2],(345,300))
                screen.blit(wee.wordMadeBy[3],(345,350))
                screen.blit(wee.wordMadeBy[4],(345,400))
        elif framecount >247.5:
                screen.blit(wee.wordThatsit[9],(100,300))

        #ra = r.randint(0,255)
        #g = r.randint(0,255)
        #b = r.randint(0,255)
       
        #screen.fill((ra,g,b))
        m_pos = pygame.mouse.get_pos()
        
        print(m_pos)
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    return
        pygame.display.update()
               

    
    


