from pygame import mixer
import pygame
import rand_Tit as t
import TextDraw 
import ALPHABET as alph
import words as wo
import CREDITS as cc
import play as peeeee
import HIGHSCOER as SCO

pygame.init()
#screen display stuff=-=-=-=-=-=-=-=-=-=-=---=-=--=-=-=--=

scrn_h = 768
scrn_w = 1380
screen = pygame.display.set_mode((scrn_w,scrn_h))

title = t.titleselect()
pygame.display.set_caption(title)
#end of screendisplay setting =-=-=-=--=-=-=-=-=-=-=-=--=-=
#music=-=-=-=-=
mixer.init()
mixer.music.load(t.mus_bg_select())
mixer.music.set_volume(0.7)
mixer.music.play()


#MOUSE=-=-=-=-=-=-=-
m = 0
m_pos = pygame.mouse.get_pos()
#=-=--=-==-==-==-=


#clockinit()+++=-=-=--=-=-=--==-=-
clock = pygame.time.Clock()
v = 0
w = 0 
#clock end=-=-=-=-=-=-=-=-=-=-==--=



#button-=-=-=-=--=


animation_tick = 0
def drawplay(v):
    screen.blit(wo.wordPLAY[v],(600,250))
def drawoptions(v):
    screen.blit(wo.wordOPTIONS[v],(570,310))
def drawhighscore(v):
    screen.blit(wo.wordHIGHSCORE[v],(515,370))
def drawcredits(v):
    screen.blit(wo.wordCREDITS[v],(570,430))
def drawexit(v):
    screen.blit(wo.wordEXIT[v],(600,490))

flagcredits = 0
flagplay = 0
flagexit = 0



def draw_ENTANGLEMEMT(v):
    if(v>=10):
        v=0
    startpos = 400
    offset = 50
    screen.blit(alph.lettE[v],((startpos+(offset*0)),170))
    screen.blit(alph.lettN[v],((startpos+(offset*1)),170))
    screen.blit(alph.lettT[v],((startpos+(offset*2)),170))
    screen.blit(alph.lettA[v],((startpos+(offset*3)),170))
    screen.blit(alph.lettN[v],((startpos+(offset*4)),170))
    screen.blit(alph.lettG[v],((startpos+(offset*5)),170))
    screen.blit(alph.lettL[v],((startpos+(offset*6)),170))
    screen.blit(alph.lettE[v],((startpos+(offset*7)),170))
    screen.blit(alph.lettM[v],((startpos+(offset*8)),170))
    screen.blit(alph.lettE[v],((startpos+(offset*9)),170))
    screen.blit(alph.lettN[v],((startpos+(offset*10)),170))
    screen.blit(alph.lettT[v],((startpos+(offset*11)),170))

#credit PAGe




#menu loop=-=-=-=-=-=-=-=-=-=--=-==-=-=-=-=-=
run = 1
while (run==1):
    clock.tick(24.72)

    screen.fill((0,0,0))
    m_pos = pygame.mouse.get_pos()
    print(m_pos)
    animation_tick +=2.43
    if(animation_tick >=20.02212):
        animation_tick = 0
        if(v>=5):
            v = 0
        else:
            v+=1
        if(w>=9):
            w = 0
        else:
            w+=1
        screen.blit((TextDraw.bg_draw(v)),(0,0))
        draw_ENTANGLEMEMT(w)
    else:
        screen.blit((TextDraw.bg_draw(v)),(0,0))
        draw_ENTANGLEMEMT(w)
    #play
    if(m_pos[0]>600 and m_pos[1]>250):
        if(m_pos[0]<710 and m_pos[1]<280):
            drawplay(10)
            flagplay = 1
        else:
            drawplay(2)
            flagplay = 0
    else:
        drawplay(2)
        flagplay =0

    #credits
    if(m_pos[0]>580 and m_pos[1]>430):
        if(m_pos[0]<765 and m_pos[1]<460):
            drawcredits(10)
            flagcredits = 1
        else:
            drawcredits(2)
            flagcredits = 0
    else:
        drawcredits(2)
        flagcredits =0

    #credits
    if(m_pos[0]>600 and m_pos[1]>490):
        if(m_pos[0]<700 and m_pos[1]<520):
            drawexit(10)
            flagexit = 1
        else:
            drawexit(2)
            flagexit = 0
    else:
        drawexit(2)
        flagexit = 0

    #highscore
    if(m_pos[0]>515 and m_pos[1]>370):
        if(m_pos[0]<810 and m_pos[1]<400):
            drawhighscore(10)
            flaghighscore = 1
        else:
            drawhighscore(2)
            flaghighscore = 0
    else:
        drawhighscore(2)
        flaghighscore = 0

    #options
    if(m_pos[0]>570 and m_pos[1]>310):
        if(m_pos[0]<760 and m_pos[1]<340):
            drawoptions(10)
            flagoption = 1
        else:
            drawoptions(2)
            flagoption = 0
    else:
        drawoptions(2)
        flagoption = 0



    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run =0
        if event.type == pygame.MOUSEBUTTONDOWN:
            if flagplay == 1:
                mixer.music.stop()
                mixer.music.load(t.songlist[1])
                mixer.music.set_volume(0.7)
                mixer.music.play()
                peeeee.playnow(screen)
                mixer.music.stop()
                mixer.music.load(t.songlist[4])
                mixer.music.set_volume(0.05)
                mixer.music.play()
                print("play")
            if flagcredits == 1:
                mixer.music.stop()
                mixer.music.load(t.songlist[2])
                mixer.music.set_volume(0.7)
                mixer.music.play()
                cc.credit(screen)
                mixer.music.stop()
                mixer.music.load(t.songlist[4])
                mixer.music.set_volume(0.05)
                mixer.music.play()
                print("creits")
            if flagexit == 1:
                run = 0
            if flaghighscore ==1:
                mixer.music.stop()
                mixer.music.load(t.songlist[5])
                mixer.music.set_volume(0.7)
                mixer.music.play()
                SCO.highscore(screen)
                mixer.music.stop()
                mixer.music.load(t.songlist[4])
                mixer.music.set_volume(0.05)
                mixer.music.play()
                print("highscore")
            if flagoption == 1:
                print("options")
        if event.type == pygame.QUIT:
            run == 0
    pygame.display.update()
pygame.quit()
#menu loop end-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=