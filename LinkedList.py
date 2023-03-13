import pygame
import TextDraw as te
import words as woo

class Node:
    
    def __init__(self,data):
        self.name = data[0]
        self.char = data[1]
        self.score = data[2]
        self.next = None
        self.prev = None
    
class DL: 
    def __init__(self):
        self.head = None
    
    def insertBeg(self, data):
        n = Node(data)
        
        if self.head == None:
            self.head = n
            return
        else:
            temp = self.head
            n.next = temp
            temp.prev = n
            n.prev = temp
            self.head = n
            return

    def insertEnd(self, data):
        n = Node(data)
        if self.head == None:
            self.head = n
            print("Score Appended at head successfully\n")
            return
        else:
            temp = self.head
            while (temp.next != None):
                temp = temp.next

            temp.next = n
            n.prev = temp
            return

    def sortList(self, order):
        #order = 1
        if(self.head == None):  
            return;  
        else:  
            current = self.head
            while(current.next != None):
                index = current.next
               
                if(order == 1):
                    while(index != None):
                        if(current.score > index.score):  
                            temp = current.score;
                            temp2 = current.name;
                            temp3 = current.char;
                            current.name = index.name;
                            current.score = index.score;
                            current.char = index.char
                            index.score = temp;
                            index.name = temp2;
                            index.char = temp3;
                        index = index.next  
                    current = current.next;
                if(order == 2):
                    while(index != None):  
                        if(current.score < index.score):  
                            temp = current.score;
                            temp2 = current.name;
                            temp3 = current.char;
                            current.name = index.name;
                            current.score = index.score;
                            current.char = index.char
                            index.score = temp;
                            index.name = temp2;
                            index.char = temp3;
                        index = index.next  
                    current = current.next
    def printDCL(self,v,screen):
        startx = 150
        starty = 220
        offsetx = 160
        offsety = 20
        nx = 0
        ny = 0
        count = 0 
        pygame.init()
        #print("\n\tHow do you want the high scores to be sorted? \n \n\t1) Press 1 for Ascending\n\t2) Press 2 for Descending:  ")
        #order = int(input())
        
        temp = self.head
        if(temp != None):
            while (True):
                if count == 10:
                    return
                nx = 0
                screen.blit(woo.wordd(temp.char,v,70),((startx+(offsetx*0)),(starty+(offsety*ny))))
                screen.blit(woo.wordd(temp.name,v,70),((startx+(offsetx*2)),(starty+(offsety*ny))))
                screen.blit(woo.wordd(temp.score,v,70),((startx+(offsetx*4.4)),(starty+(offsety*ny))))
                ny+=2
                count+=1
                temp = temp.next
                if(temp == None):
                    break
            else:
                print("List is empty")    
        return

            