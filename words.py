import pygame
import rand_Tit as r
import TextDraw as te

pygame.init()
fontcolor = (255,255,255)
wordPLAY= [
         te.text_Draw("PLAY",r.fontselect(),fontcolor,80),
         te.text_Draw("PLAY",r.fontselect(),fontcolor,80),
         te.text_Draw("PLAY","font\\f3.ttf",fontcolor,80),
         te.text_Draw("PLAY",r.fontselect(),fontcolor,80),
         te.text_Draw("PLAY",r.fontselect(),fontcolor,80),
         te.text_Draw("play",r.fontselect(),fontcolor,80),
         te.text_Draw("play",r.fontselect(),fontcolor,80),
         te.text_Draw("play",r.fontselect(),fontcolor,80),
         te.text_Draw("play",r.fontselect(),fontcolor,80),
         te.text_Draw("play",r.fontselect(),fontcolor,80),
         te.text_Draw("Play","font\\specialf.otf",fontcolor,80),
          ]       
wordOPTIONS= [
         te.text_Draw("OPTIONS",r.fontselect(),fontcolor,80),
         te.text_Draw("OPTIONS",r.fontselect(),fontcolor,80),
         te.text_Draw("OPTIONS","font\\f3.ttf",fontcolor,80),
         te.text_Draw("OPTIONS",r.fontselect(),fontcolor,80),
         te.text_Draw("OPTIONS",r.fontselect(),fontcolor,80),
         te.text_Draw("options",r.fontselect(),fontcolor,80),
         te.text_Draw("options",r.fontselect(),fontcolor,80),
         te.text_Draw("options",r.fontselect(),fontcolor,80),
         te.text_Draw("options",r.fontselect(),fontcolor,80),
         te.text_Draw("options",r.fontselect(),fontcolor,80),
         te.text_Draw("Options","font\\specialf.otf",fontcolor,80),
          ]
wordCREDITS= [
         te.text_Draw("CREDITS",r.fontselect(),fontcolor,80),
         te.text_Draw("CREDITS",r.fontselect(),fontcolor,80),
         te.text_Draw("CREDITS","font\\f3.ttf",fontcolor,80),
         te.text_Draw("CREDITS",r.fontselect(),fontcolor,80),
         te.text_Draw("CREDITS",r.fontselect(),fontcolor,80),
         te.text_Draw("credits",r.fontselect(),fontcolor,80),
         te.text_Draw("credits",r.fontselect(),fontcolor,80),
         te.text_Draw("credits",r.fontselect(),fontcolor,80),
         te.text_Draw("credits",r.fontselect(),fontcolor,80),
         te.text_Draw("credits",r.fontselect(),fontcolor,80),
         te.text_Draw("Credits","font\\specialf.otf",fontcolor,80),
          ]
wordHIGHSCORE= [
         te.text_Draw("LEADERBOARD",r.fontselect(),fontcolor,80),
         te.text_Draw("LEADERBOARD",r.fontselect(),fontcolor,80),
         te.text_Draw("LEADERBOARD","font\\f3.ttf",fontcolor,80),
         te.text_Draw("LEADERBOARD",r.fontselect(),fontcolor,80),
         te.text_Draw("LEADERBOARD",r.fontselect(),fontcolor,80),
         te.text_Draw("leaderboard",r.fontselect(),fontcolor,80),
         te.text_Draw("leaderboard",r.fontselect(),fontcolor,80),
         te.text_Draw("leaderboard",r.fontselect(),fontcolor,80),
         te.text_Draw("leaderboard",r.fontselect(),fontcolor,80),
         te.text_Draw("leaderboard",r.fontselect(),fontcolor,80),
         te.text_Draw("leaderboard","font\\specialf.otf",fontcolor,80),
          ]
wordEXIT= [
         te.text_Draw("EXIT",r.fontselect(),fontcolor,80),
         te.text_Draw("EXIT",r.fontselect(),fontcolor,80),
         te.text_Draw("EXIT","font\\f3.ttf",fontcolor,80),
         te.text_Draw("EXIT",r.fontselect(),fontcolor,80),
         te.text_Draw("EXIT",r.fontselect(),fontcolor,80),
         te.text_Draw("exit",r.fontselect(),fontcolor,80),
         te.text_Draw("exit",r.fontselect(),fontcolor,80),
         te.text_Draw("exit",r.fontselect(),fontcolor,80),
         te.text_Draw("exit",r.fontselect(),fontcolor,80),
         te.text_Draw("exit",r.fontselect(),fontcolor,80),
         te.text_Draw("Exit","font\\specialf.otf",fontcolor,80),
          ]
wordEntanglement= [
         te.text_Draw("Entanglement",r.fontselect(),fontcolor,200),
         te.text_Draw("Entanglement",r.fontselect(),fontcolor,200),
         te.text_Draw("Entanglement","font\\f3.ttf",fontcolor,200),
         te.text_Draw("Entanglement",r.fontselect(),fontcolor,200),
         te.text_Draw("Entanglement",r.fontselect(),fontcolor,200),
         te.text_Draw("Entanglement",r.fontselect(),fontcolor,200),
         te.text_Draw("Entanglement",r.fontselect(),fontcolor,200),
         te.text_Draw("Entanglement",r.fontselect(),fontcolor,200),
         te.text_Draw("Entanglement",r.fontselect(),fontcolor,200),
         te.text_Draw("Entanglement",r.fontselect(),fontcolor,200),
          ]
wordMadeBy= [
         te.text_Draw("Made By:","font\\f3.ttf",fontcolor,150),#0
         te.text_Draw("Made By:","font\\f3.ttf",fontcolor,200),
         te.text_Draw("Abdul Rehman","font\\f3.ttf",fontcolor,100),#2
         te.text_Draw("Maaz Muhammad Khan","font\\f3.ttf",fontcolor,100),#3
         te.text_Draw("Shaheer Ul Islam","font\\f3.ttf",fontcolor,100),#4
         te.text_Draw("Made By:",r.fontselect(),fontcolor,200),
         te.text_Draw("Made By:",r.fontselect(),fontcolor,200),
         te.text_Draw("Made By:",r.fontselect(),fontcolor,200),
         te.text_Draw("Made By:",r.fontselect(),fontcolor,200),
         te.text_Draw("Made By:",r.fontselect(),fontcolor,200),
          ]

wordThatsit=[
         te.text_Draw("Thats All. \n Consider giving us 75% plz",r.fontselect(),(20,20,20),290),
         te.text_Draw("Thats All. \n Consider giving us 75% plz",r.fontselect(),(20,20,20),290),
         te.text_Draw("Thats All. \n Consider giving us 75% plz",r.fontselect(),(20,20,20),290),
         te.text_Draw("Thats All. \n Consider giving us 75% plz",r.fontselect(),(20,20,20),290),
         te.text_Draw("Thats All. \n Consider giving us 75% plz",r.fontselect(),(20,20,20),290),
         te.text_Draw("Thats All. \n Consider giving us 75% plz",r.fontselect(),(20,20,20),290),
         te.text_Draw("Thats All. \n Consider giving us 75% plz",r.fontselect(),(20,20,20),290),
         te.text_Draw("Thats All. \n Consider giving us 75% plz",r.fontselect(),(20,20,20),290),
         te.text_Draw("Thats All. \n Consider giving us 75% plz",r.fontselect(),(20,20,20),290),
         te.text_Draw("Thats All. \n Consider giving us 75% plz","font\\f3.ttf",fontcolor,120),
          ]
def wordd(word,v,size):
    if v>1:
        v = v %2
    lettWORD = [
             te.text_Draw(word,"font\\f3.ttf",fontcolor,size),
             te.text_Draw(word,"font\\f6.ttf",fontcolor,size),
            ]    
    return lettWORD[v]