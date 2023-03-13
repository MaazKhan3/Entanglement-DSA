import pygame
pygame.init()

bgimg =[ pygame.image.load("menu_bg\\mainbg_0001.png"),
         pygame.image.load("menu_bg\\mainbg_0002.png"),
         pygame.image.load("menu_bg\\mainbg_0003.png"),
         pygame.image.load("menu_bg\\mainbg_0004.png"),
         pygame.image.load("menu_bg\\mainbg_0005.png")
        ]
credimg = [ pygame.image.load("cred_bg\\cred0001.png"),
            pygame.image.load("cred_bg\\cred0002.png"),
            pygame.image.load("cred_bg\\cred0003.png"),
            pygame.image.load("cred_bg\\cred0004.png"),
            pygame.image.load("cred_bg\\cred0005.png") 
        ]
hscoimg = [ pygame.image.load("highscore_bg\\hscore_0001.png"),
            pygame.image.load("highscore_bg\\hscore_0002.png")  
          ]
playimg = [pygame.image.load("play_bg\\playbg.png")]

ch = pygame.image.load("images\\character\\ch1.png")
misc = [pygame.image.load("images\\character\\ch1.png"),
        pygame.image.load("images\\character\\wall_3.png")
        ]


def text_Draw(text,font,textcolor,size):
    fonte = pygame.font.Font(font,int((size-5)/2))
    img = fonte.render(text,True,textcolor)
    return img

def bg_draw(val):
    if (val>=5):
        val = 0
    return bgimg[val]

def creddraw(val):
    if(val>=5):
       val = 0
    return credimg[val]

def hscoredraw(val):
    if(val>1):
        val=val%2
    return hscoimg[val]

def playbgdraw():
    return playimg[0]

def ch_draw():
    return ch
def ch_rot_draw(angle):
    ino = pygame.transform.rotate(ch,angle)
    return ino
def mis_draw(a):
    return misc[a]
