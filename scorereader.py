import abc
from os import abort
import LinkedList as m

def red():
    f = open("scores.txt", "r")
    fn = f.readline()
    score = name = character = "" 
    print(fn)
    DC = m.DL()
    final = ["","",""]
    for a in fn:
        if(a == '$'):
            flagchar = 1
            flagname = 0
            flagscore = 0
        if(a == '@'):
            flagname = 1
            flagchar = 0
            flagscore = 0
        if(a == '#'):
            flagscore = 1
            flagchar = 0
            flagname = 0
        if(a=='^'):
            final = [character, name, score]
            DC.insertEnd(final)
            final = ["","",""]
            character = ""
            name = ""
            score = ""
        if(flagname == 1 and a != '@'):
            name = name + a
        if(flagchar == 1 and a != '$'):
            character = character + a
        if(flagscore == 1 and a != '#' and a!='^'):
            score = score + a
    return DC
    #DC.printDCL()
    #print("\n")

