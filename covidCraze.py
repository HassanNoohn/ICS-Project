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
screen.fill((205,131,180)) 

#Update and refresh the display to end this frame
pygame.display.flip() #<-- refresh the display

#The game loop
clock = pygame.time.Clock() #<-- used to control the frame rate
keepGoing = True 	    #<-- a 'flag' variable for the game loop condition

# Set up the font and the size 
bigfont = pygame.font.SysFont("comicsansms", 42)

#test=pygame.display.get_driver()
state="title"
btnNew=pygame.image.load("btn_newGameBig.gif").convert()
btnInrtuct=pygame.image.load("btn_InstrBig.gif").convert()
btnExit=pygame.image.load("btn_ExitBig.gif").convert()
btnMenu=pygame.image.load("btn_ExitBig.gif").convert()

welcome = bigfont.render(('WELCOME TO MY GAME'), True, (255,255,255))
instruct = bigfont.render(('How to play:'), True, (0,0,0))
error = bigfont.render(('Error!!!!!!!!!'), True, (200,0,10))

#Background images
titleImage = pygame.image.load("title.png").convert()

try:
    while keepGoing:
        clock.tick(60) #delay
        screen.fill((205,131,180)) 
        if state=="title":
            bm=screen.blit(btnMenu,(100,50))   #bm- menu button
        elif state=="menu":
           # buttons-------------------
                bn=screen.blit(btnNew,(100,50))    #bn- rectangle arround button btnNew
                bi=screen.blit(btnInrtuct,(100,150))    #bi- rectangle arround button btnInrtuct
                be=screen.blit(btnExit,(100,250))      #be- rectangle arround button btnExit
   

        elif state=="game":  
            # ---------------code for the game-------------------               
            screen.blit(welcome, (20,50))   # print text welcome

           
        elif state=="instructuctions":
            # ---------------code for the instructions-------------------
            screen.blit(instruct, (20,70))   # print text instructions

            
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
                elif bn.collidepoint(pos):
                    state="game"
                elif bi.collidepoint(pos):
                    state="instructuctions"
                elif be.collidepoint(pos):
                    keepGoing = False

finally:
    pygame.quit()  # Keep this IDLE friendly 