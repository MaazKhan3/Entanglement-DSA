import pygame
import rand_Tit as r
import TextDraw as te
#A B  E G N T M L 
# 
pygame.init()
fontcolor = (255,255,255)
lettA = [
         te.text_Draw("A",r.fontselect(),fontcolor,120),
         te.text_Draw("A",r.fontselect(),fontcolor,120),
         te.text_Draw("A",r.fontselect(),fontcolor,120),
         te.text_Draw("A",r.fontselect(),fontcolor,120),
         te.text_Draw("A",r.fontselect(),fontcolor,120),
         te.text_Draw("a",r.fontselect(),fontcolor,120),
         te.text_Draw("a",r.fontselect(),fontcolor,120),
         te.text_Draw("a",r.fontselect(),fontcolor,120),
         te.text_Draw("a",r.fontselect(),fontcolor,120),
         te.text_Draw("a",r.fontselect(),fontcolor,120),
        ]        
lettB = [
         te.text_Draw("B",r.fontselect(),fontcolor,120),
         te.text_Draw("B",r.fontselect(),fontcolor,120),
         te.text_Draw("B",r.fontselect(),fontcolor,120),
         te.text_Draw("B",r.fontselect(),fontcolor,120),
         te.text_Draw("B",r.fontselect(),fontcolor,120),
         te.text_Draw("b",r.fontselect(),fontcolor,120),
         te.text_Draw("b",r.fontselect(),fontcolor,120),
         te.text_Draw("b",r.fontselect(),fontcolor,120),
         te.text_Draw("b",r.fontselect(),fontcolor,120),
         te.text_Draw("b",r.fontselect(),fontcolor,120),
        ]        
lettC = [
         te.text_Draw("C",r.fontselect(),fontcolor,120),
         te.text_Draw("C",r.fontselect(),fontcolor,120),
         te.text_Draw("C",r.fontselect(),fontcolor,120),
         te.text_Draw("C",r.fontselect(),fontcolor,120),
         te.text_Draw("C",r.fontselect(),fontcolor,120),
         te.text_Draw("c",r.fontselect(),fontcolor,120),
         te.text_Draw("c",r.fontselect(),fontcolor,120),
         te.text_Draw("c",r.fontselect(),fontcolor,120),
         te.text_Draw("c",r.fontselect(),fontcolor,120),
         te.text_Draw("c",r.fontselect(),fontcolor,120),
        ]    
def wordd(word,v):
    if v>9:
        v = v - (9*int(v/9))

    lettWORD = [
         te.text_Draw(word,r.fontselect(),fontcolor,120),
         te.text_Draw(word,r.fontselect(),fontcolor,120),
         te.text_Draw(word,r.fontselect(),fontcolor,120),
         te.text_Draw(word,r.fontselect(),fontcolor,120),
         te.text_Draw(word,r.fontselect(),fontcolor,120),
         te.text_Draw(word,r.fontselect(),fontcolor,120),
         te.text_Draw(word,r.fontselect(),fontcolor,120),
         te.text_Draw(word,r.fontselect(),fontcolor,120),
         te.text_Draw(word,r.fontselect(),fontcolor,120),
         te.text_Draw(word,r.fontselect(),fontcolor,120),
        ]    
    return lettWORD[v]


lettE = [                 
         te.text_Draw("E",r.fontselect(),fontcolor,120),
         te.text_Draw("E",r.fontselect(),fontcolor,120),
         te.text_Draw("E",r.fontselect(),fontcolor,120),
         te.text_Draw("E",r.fontselect(),fontcolor,120),
         te.text_Draw("E",r.fontselect(),fontcolor,120),
         te.text_Draw("e",r.fontselect(),fontcolor,120),
         te.text_Draw("e",r.fontselect(),fontcolor,120),
         te.text_Draw("e",r.fontselect(),fontcolor,120),
         te.text_Draw("e",r.fontselect(),fontcolor,120),
         te.text_Draw("e",r.fontselect(),fontcolor,120),
        ]                 
lettT=  [                 
         te.text_Draw("T",r.fontselect(),fontcolor,120),
         te.text_Draw("T",r.fontselect(),fontcolor,120),
         te.text_Draw("T",r.fontselect(),fontcolor,120),
         te.text_Draw("T",r.fontselect(),fontcolor,120),
         te.text_Draw("T",r.fontselect(),fontcolor,120),
         te.text_Draw("t",r.fontselect(),fontcolor,120),
         te.text_Draw("t",r.fontselect(),fontcolor,120),
         te.text_Draw("t",r.fontselect(),fontcolor,120),
         te.text_Draw("t",r.fontselect(),fontcolor,120),
         te.text_Draw("t",r.fontselect(),fontcolor,120),
        ]                
lettG = [                 
         te.text_Draw("G",r.fontselect(),fontcolor,120),
         te.text_Draw("G",r.fontselect(),fontcolor,120),
         te.text_Draw("G",r.fontselect(),fontcolor,120),
         te.text_Draw("G",r.fontselect(),fontcolor,120),
         te.text_Draw("G",r.fontselect(),fontcolor,120),
         te.text_Draw("g",r.fontselect(),fontcolor,120),
         te.text_Draw("g",r.fontselect(),fontcolor,120),
         te.text_Draw("g",r.fontselect(),fontcolor,120),
         te.text_Draw("g",r.fontselect(),fontcolor,120),
         te.text_Draw("g",r.fontselect(),fontcolor,120),
        ]                 
lettL = [                 
         te.text_Draw("L",r.fontselect(),fontcolor,120),
         te.text_Draw("L",r.fontselect(),fontcolor,120),
         te.text_Draw("L",r.fontselect(),fontcolor,120),
         te.text_Draw("L",r.fontselect(),fontcolor,120),
         te.text_Draw("L",r.fontselect(),fontcolor,120),
         te.text_Draw("l",r.fontselect(),fontcolor,120),
         te.text_Draw("l",r.fontselect(),fontcolor,120),
         te.text_Draw("l",r.fontselect(),fontcolor,120),
         te.text_Draw("l",r.fontselect(),fontcolor,120),
         te.text_Draw("l",r.fontselect(),fontcolor,120),
        ]                 
lettM = [                 
         te.text_Draw("M",r.fontselect(),fontcolor,120),
         te.text_Draw("M",r.fontselect(),fontcolor,120),
         te.text_Draw("M",r.fontselect(),fontcolor,120),
         te.text_Draw("M",r.fontselect(),fontcolor,120),
         te.text_Draw("M",r.fontselect(),fontcolor,120),
         te.text_Draw("m",r.fontselect(),fontcolor,120),
         te.text_Draw("m",r.fontselect(),fontcolor,120),
         te.text_Draw("m",r.fontselect(),fontcolor,120),
         te.text_Draw("m",r.fontselect(),fontcolor,120),
         te.text_Draw("m",r.fontselect(),fontcolor,120),
        ]
lettN = [
         te.text_Draw("N",r.fontselect(),fontcolor,120),
         te.text_Draw("N",r.fontselect(),fontcolor,120),
         te.text_Draw("N",r.fontselect(),fontcolor,120),
         te.text_Draw("N",r.fontselect(),fontcolor,120),
         te.text_Draw("N",r.fontselect(),fontcolor,120),
         te.text_Draw("n",r.fontselect(),fontcolor,120),
         te.text_Draw("n",r.fontselect(),fontcolor,120),
         te.text_Draw("n",r.fontselect(),fontcolor,120),
         te.text_Draw("n",r.fontselect(),fontcolor,120),
         te.text_Draw("n",r.fontselect(),fontcolor,120),
        ]
def worddisp(word,v):
    lettWORD= [
         te.text_Draw(word,r.fontselect(),fontcolor,120),
         te.text_Draw(word,r.fontselect(),fontcolor,120),
         te.text_Draw(word,r.fontselect(),fontcolor,120),
         te.text_Draw(word,r.fontselect(),fontcolor,120),
         te.text_Draw(word,r.fontselect(),fontcolor,120),
         te.text_Draw(word,r.fontselect(),fontcolor,120),
         te.text_Draw(word,r.fontselect(),fontcolor,120),
         te.text_Draw(word,r.fontselect(),fontcolor,120),
         te.text_Draw(word,r.fontselect(),fontcolor,120),
         te.text_Draw(word,r.fontselect(),fontcolor,120),
        ]        
def withsize(lett,siz,num):
    lettA = [
             te.text_Draw("A",r.fontselect(),fontcolor,siz),
             te.text_Draw("A",r.fontselect(),fontcolor,siz),
             te.text_Draw("A",r.fontselect(),fontcolor,siz),
             te.text_Draw("A",r.fontselect(),fontcolor,siz),
             te.text_Draw("A",r.fontselect(),fontcolor,siz),
             te.text_Draw("a",r.fontselect(),fontcolor,siz),
             te.text_Draw("a",r.fontselect(),fontcolor,siz),
             te.text_Draw("a",r.fontselect(),fontcolor,siz),
             te.text_Draw("a",r.fontselect(),fontcolor,siz),
             te.text_Draw("a",r.fontselect(),fontcolor,siz),
            ]                                          
    lettE = [                                          
             te.text_Draw("E",r.fontselect(),fontcolor,siz),
             te.text_Draw("E",r.fontselect(),fontcolor,siz),
             te.text_Draw("E",r.fontselect(),fontcolor,siz),
             te.text_Draw("E",r.fontselect(),fontcolor,siz),
             te.text_Draw("E",r.fontselect(),fontcolor,siz),
             te.text_Draw("e",r.fontselect(),fontcolor,siz),
             te.text_Draw("e",r.fontselect(),fontcolor,siz),
             te.text_Draw("e",r.fontselect(),fontcolor,siz),
             te.text_Draw("e",r.fontselect(),fontcolor,siz),
             te.text_Draw("e",r.fontselect(),fontcolor,siz),
            ]                                          
    lettT=  [                                          
             te.text_Draw("T",r.fontselect(),fontcolor,siz),
             te.text_Draw("T",r.fontselect(),fontcolor,siz),
             te.text_Draw("T",r.fontselect(),fontcolor,siz),
             te.text_Draw("T",r.fontselect(),fontcolor,siz),
             te.text_Draw("T",r.fontselect(),fontcolor,siz),
             te.text_Draw("t",r.fontselect(),fontcolor,siz),
             te.text_Draw("t",r.fontselect(),fontcolor,siz),
             te.text_Draw("t",r.fontselect(),fontcolor,siz),
             te.text_Draw("t",r.fontselect(),fontcolor,siz),
             te.text_Draw("t",r.fontselect(),fontcolor,siz),
            ]                                          
    lettG = [                                          
             te.text_Draw("G",r.fontselect(),fontcolor,siz),
             te.text_Draw("G",r.fontselect(),fontcolor,siz),
             te.text_Draw("G",r.fontselect(),fontcolor,siz),
             te.text_Draw("G",r.fontselect(),fontcolor,siz),
             te.text_Draw("G",r.fontselect(),fontcolor,siz),
             te.text_Draw("g",r.fontselect(),fontcolor,siz),
             te.text_Draw("g",r.fontselect(),fontcolor,siz),
             te.text_Draw("g",r.fontselect(),fontcolor,siz),
             te.text_Draw("g",r.fontselect(),fontcolor,siz),
             te.text_Draw("g",r.fontselect(),fontcolor,siz),
            ]                                          
    lettL = [                                          
             te.text_Draw("L",r.fontselect(),fontcolor,siz),
             te.text_Draw("L",r.fontselect(),fontcolor,siz),
             te.text_Draw("L",r.fontselect(),fontcolor,siz),
             te.text_Draw("L",r.fontselect(),fontcolor,siz),
             te.text_Draw("L",r.fontselect(),fontcolor,siz),
             te.text_Draw("l",r.fontselect(),fontcolor,siz),
             te.text_Draw("l",r.fontselect(),fontcolor,siz),
             te.text_Draw("l",r.fontselect(),fontcolor,siz),
             te.text_Draw("l",r.fontselect(),fontcolor,siz),
             te.text_Draw("l",r.fontselect(),fontcolor,siz),
            ]                                          
    lettM = [                                          
             te.text_Draw("M",r.fontselect(),fontcolor,siz),
             te.text_Draw("M",r.fontselect(),fontcolor,siz),
             te.text_Draw("M",r.fontselect(),fontcolor,siz),
             te.text_Draw("M",r.fontselect(),fontcolor,siz),
             te.text_Draw("M",r.fontselect(),fontcolor,siz),
             te.text_Draw("m",r.fontselect(),fontcolor,siz),
             te.text_Draw("m",r.fontselect(),fontcolor,siz),
             te.text_Draw("m",r.fontselect(),fontcolor,siz),
             te.text_Draw("m",r.fontselect(),fontcolor,siz),
             te.text_Draw("m",r.fontselect(),fontcolor,siz),
            ]                                          
    lettN = [                                          
             te.text_Draw("N",r.fontselect(),fontcolor,siz),
             te.text_Draw("N",r.fontselect(),fontcolor,siz),
             te.text_Draw("N",r.fontselect(),fontcolor,siz),
             te.text_Draw("N",r.fontselect(),fontcolor,siz),
             te.text_Draw("N",r.fontselect(),fontcolor,siz),
             te.text_Draw("n",r.fontselect(),fontcolor,siz),
             te.text_Draw("n",r.fontselect(),fontcolor,siz),
             te.text_Draw("n",r.fontselect(),fontcolor,siz),
             te.text_Draw("n",r.fontselect(),fontcolor,siz),
             te.text_Draw("n",r.fontselect(),fontcolor,siz),
            ]    
    if lett == "A":
        return lettA[num]
    elif lett == "E":
        return lettE[num]
    elif lett == "T":
        return lettT[num]
    elif lett == "G":
        return lettG[num]
    elif lett == "L":
        return lettL[num]
    elif lett == "M":
        return lettM[num]
    elif lett == "N":
        return lettN[num]
    

