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
size = (800,600)  
screen = pygame.display.set_mode(size) 

#Puts a caption in the bar at the top of the window
pygame.display.set_caption("Covid Craze") 

# Fills the memory screen surface with colour
screen.fill((0, 0, 0)) 

#Update and refresh the display to end this frame
pygame.display.flip() #<-- refresh the display

#The game loop
clock = pygame.time.Clock() #<-- used to control the frame rate
keepGoing = True 	    #<-- a 'flag' variable for the game loop condition

# Set up the font and the size 
bigfont = pygame.font.SysFont("comicsansms", 42)

#test=pygame.display.get_driver()
state="title"
btnNew=pygame.image.load("btnPlay.png").convert()
btnNew=pygame.transform.scale(btnNew, (150, 80))
btnQuiz=pygame.image.load("btnQuiz.png").convert()
btnQuiz= pygame.transform.scale(btnQuiz, (150, 80))
btnResult=pygame.image.load("btnResult.png").convert()
btnResult= pygame.transform.scale(btnResult, (150, 80))
btnLesson=pygame.image.load("btnLesson.png").convert()
btnLesson= pygame.transform.scale(btnLesson, (150, 80))
btnBack=pygame.image.load("btnBack.png").convert()
btnBack= pygame.transform.scale(btnBack, (150, 80))
btnExit=pygame.image.load("btnExit.png").convert()
btnExit= pygame.transform.scale(btnExit, (150, 80))
btnMenu=pygame.image.load("btnMenu.png").convert()
btnMenu= pygame.transform.scale(btnMenu, (150, 80))

welcome = bigfont.render(('WELCOME TO MY GAME'), True, (255,255,255))
lesson = bigfont.render(('lessons coming soon...'), True, (0,0,0))
quiz = bigfont.render(('quiz coming soon...'), True, (0,0,0))
result = bigfont.render(('results coming soon...'), True, (0,0,0))
error = bigfont.render(('Error!!!!!!!!!'), True, (200,0,10))

#Background images
titleImage = pygame.image.load("title.png").convert()
titleImage = pygame.transform.scale(titleImage, (800, 600))
menuImage = pygame.image.load("menu.png").convert()
menuImage = pygame.transform.scale(menuImage, (800, 600))


try:
    while keepGoing:
        clock.tick(60) #delay
        screen.fill((205,131,180)) 
        if state=="title":
            screen.blit(titleImage,(0,0))
            bm=screen.blit(btnMenu,(490,400))   #bm- menu button
        elif state=="menu":
           # buttons-------------------
                screen.blit(menuImage,(0,0))
                bp=screen.blit(btnNew,(470,50))    #bp- rectangle arround button btnPLay
                bq=screen.blit(btnQuiz,(470,150))    #bq- rectangle arround button btnQuiz
                br=screen.blit(btnResult,(470,250))      #br- rectangle arround button btnResult
                bl=screen.blit(btnLesson,(470,350))    #bl- rectangle around buttonLesson
                be=screen.blit(btnExit,(470,450))    #be- rectangle around buttonExit

        elif state=="game":  
            # ---------------code for the game-------------------               
            screen.blit(welcome, (20,50))   # print text welcome
            bb=screen.blit(btnBack,(400,420))    #bb- rectangle around button btnBack

        elif state=="quiz":
            # ---------------code for the quiz-------------------
            screen.blit(quiz, (20,70))   # print text instructions
            bb=screen.blit(btnBack,(400,420))    #bb- rectangle around button btnBack
            
        elif state=="result":
            # ---------------code for the quiz results-------------------
            screen.blit(result,(20,70))  # print text for results
            bb=screen.blit(btnBack,(400,420))    #bb- rectangle around button btnBack
            
        elif state=="lesson":
            # ---------------code for the quiz results-------------------
            screen.blit(lesson,(20,70))  # print text for results        
            bb=screen.blit(btnBack,(400,420))    #bb- rectangle around button btnBack
            
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
                elif be.collidepoint(pos):
                    keepGoing = False

finally:
    pygame.quit()  # Keep this IDLE friendly 