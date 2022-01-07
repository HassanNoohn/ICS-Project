""" 
A basic menu template 
buttons are from the website:
http://www.freebuttons.com/index.php
"""

#Import & initialize the pygame module
import pygame
import random
#pygame.locals contains constants like MOUSEMOTION and MOUSEBUTTONUP and QUIT for events. #It's easier to type MOUSEBUTTONUP instead of pygame.locals.MOUSEBUTTONUP
from pygame.locals import *  
# better use pygame.MOUSEMOTION

#This will allow us to name the colours to use rather than give a name  eg (255,0,0)
from pygame.color import THECOLORS
#c=(255,0,0) instead of THECOLORS['red']????

# initial library itself
pygame.init()  

#Just like python, we will use os and time????
import os, time

#this code is necessary for python to work on tdsb computers????
import platform
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'

#Set-up the main screen display window and caption  in the 
size = (800,449)  
screen = pygame.display.set_mode(size) 

#Puts a caption in the bar at the top of the window
pygame.display.set_caption("Covid Craze") 

# Fills the memory screen surface with colour
screen.fill((9, 200, 0)) 

#Update and refresh the display to end this frame
pygame.display.flip() #<-- refresh the display

#The game loop
clock = pygame.time.Clock() #<-- used to control the frame rate
keepGoing = True 	    #<-- a 'flag' variable for the game loop condition

# Set up the font and the size 
bigfont = pygame.font.SysFont("comicsansms", 42)

#sub programs
def setBackground(file):
    image=pygame.image.load(file).convert()
    image=pygame.transform.scale(image, (800, 449))  
    screen.blit(image, (0,0))
def button(file):
    button=pygame.image.load(file).convert_alpha()
    button=pygame.transform.scale(button, (100, 40))
    return button
#test=pygame.display.get_driver()
state="title"
next=False
btnNew=button("btnPlay.png")
btnQuiz=button("btnQuiz.png")
btnResult=button("btnResult.png")
btnLesson=button("btnLesson.png")
btnBack= button("btnBack.png")
btnExit=button("btnExit.png")
btnMenu=button("btnMenu.png")

welcome = bigfont.render(('WELCOME TO MY GAME'), True, (255,255,255))
lesson = bigfont.render(('lessons coming soon...'), True, (0,0,0))
result = bigfont.render(('results coming soon...'), True, (0,0,0))
error = bigfont.render(('Error!!!!!!!!!'), True, (200,0,10))

try:
    while keepGoing:
        clock.tick(60) #delay
        screen.fill((205,131,180)) 
        if state=="title":
            setBackground("title.png")
            bm=screen.blit(btnMenu,(350,270))   #bm- menu button
        elif state=="menu":
           # buttons-------------------
            setBackground("menu.png")
            bp=screen.blit(btnNew,(100,320))    #bp- rectangle arround button btnPLay
            bq=screen.blit(btnQuiz,(225,320))    #bq- rectangle arround button btnQuiz
            br=screen.blit(btnResult,(350,320))      #br- rectangle arround button btnResult
            bl=screen.blit(btnLesson,(475,320))    #bl- rectangle around buttonLesson
            be=screen.blit(btnExit,(600,320))    #be- rectangle around buttonExit

        elif state=="game":  
            # ---------------code for the game-------------------               
            screen.blit(welcome, (20,50))   # print text welcome
            bb=screen.blit(btnBack,(400,380))    #bb- rectangle around button btnBack

        elif state=="quiz":
            # ---------------code for the quiz-------------------
            #variables
            setBackground("quiz.png")
            btnNext=button("btnNext.png")
            bn=screen.blit(btnNext,(650,380))    #bn- rectangle around button btnNext
            bb=screen.blit(btnBack,(50,380))    #bb- rectangle around button btnBack
            
            
            
            
        elif state=="result":
            # ---------------code for the quiz results-------------------
            screen.blit(result,(20,70))  # print text for results
            bb=screen.blit(btnBack,(400,380))    #bb- rectangle around button btnBack
            
        elif state=="lesson":
            # ---------------code for the quiz results-------------------
            screen.blit(lesson,(20,70))  # print text for results        
            bb=screen.blit(btnBack,(400,380))    #bb- rectangle around button btnBack
            
        else:
            screen.blit(error, (20,60))       # print text error

                
        pygame.display.flip()
        #Handle any events in the current frame
        #print(pygame.event.get())
        for ev in pygame.event.get(): 
            if ev.type == pygame.QUIT: #<-- this special event type happens when the window is closed
                keepGoing = False
            elif ev.type == MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                if bm.collidepoint(pos):
                    state="menu"                
                elif bp.collidepoint(pos):
                    state="game"
                elif bq.collidepoint(pos):
                    state="quiz"
                elif br.collidepoint(pos):
                    state="result"   
                elif bl.collidepoint(pos):
                    state="lesson"            
                elif bb.collidepoint(pos):
                    state="menu"
                elif bn.collidepoint(pos):
                    next=True
                elif be.collidepoint(pos):
                    keepGoing = False

finally:
    pygame.quit()  # Keep this IDLE friendly 