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
font_score = pygame.font.SysFont("Bauhaus 93", 30)

#define colours
white = (255, 255, 255)

#sub programs
def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))
def setBackground(file):
  image=pygame.image.load(file).convert()
  image=pygame.transform.scale(image, (800, 449))  
  screen.blit(image, (0,0))
def button(file):
  button=pygame.image.load(file).convert_alpha()
  button=pygame.transform.scale(button, (100, 40))
  return button

def quizOption(file):
  option=pygame.image.load(file).convert_alpha()
  option=pygame.transform.scale(option,(129,109))
  return option
#--------game stuff----------
screen_width = 800
screen_height = 449

#game variables
tile_size = 30
game_over = 0
score = 0

#images for game
sun_img = pygame.image.load('img/sun.png')
bg_img = pygame.image.load('img/sky.png')

#functions below all by Coding With Russ on YouTube

class Player():
    def __init__(self, x, y):
         self.reset(x, y)


    def update(self, game_over):
        dx = 0
        dy = 0
        walk_cooldown = 5

        if game_over == 0:
            #get keypresses
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and self.jumped == False:
                self.vel_y = -15
                self.jumped = True
            if key[pygame.K_SPACE] == False:
                self.jumped = False
            if key[pygame.K_LEFT]:
                dx -= 5
                self.counter += 1
                self.direction = -1
            if key[pygame.K_RIGHT]:
                dx += 5
                self.counter += 1
                self.direction = 1
            if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
                self.counter = 0
                self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]


            #handle animation
            if self.counter > walk_cooldown:
                self.counter = 0    
                self.index += 1
                if self.index >= len(self.images_right):
                    self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]


            #add gravity
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y

            #check for collision
            for tile in world.tile_list:
                #check for collision in x direction
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                #check for collision in y direction
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    #check if below the ground i.e. jumping
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    #check if above the ground i.e. falling
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0

            #check for collision with coins            
            if pygame.sprite.spritecollide(player, coin_group, True):
                score += 1

            #check for collision with enemies
            if pygame.sprite.spritecollide(self, blob_group, False):
                game_over = -1
            #check for collision with exit
            if pygame.sprite.spritecollide(self, exit_group, False):
                game_over = 1

            #update player coordinates
            self.rect.x += dx
            self.rect.y += dy


        elif game_over == -1:
            self.image = self.dead_image
            if self.rect.y > 200:
                self.rect.y -= 5


                
                

        #draw player onto screen
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

        return game_over

    def reset(self, x, y):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for num in range(1, 5):
            img_right = pygame.image.load(f'img/guy{num}.png')
            img_right = pygame.transform.scale(img_right, (40, 80))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.dead_image = pygame.image.load('img/ghost.png')
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
        self.in_air = True

class World():
    def __init__(self, data):
        self.tile_list = []

        #load images
        dirt_img = pygame.image.load('img/dirt.png')
        grass_img = pygame.image.load('img/grass.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    blob = Enemy(col_count * tile_size, row_count * tile_size + 15)
                    blob_group.add(blob)
                if tile == 4:
                    coin = Coin(col_count * tile_size + (tile_size // 2), row_count * tile_size + (tile_size // 2))
                    coin_group.add(coin)
                if tile == 8:
                    exit = Exit(col_count * tile_size, row_count * tile_size - (tile_size // 2))
                    exit_group.add(exit)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)



class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/blob.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/coin.png')
        self.image = pygame.transform.scale(img, (int(tile_size * 1.5), int(tile_size * 1.5)))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    
            
class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/exit.png')
        self.image = pygame.transform.scale(img, (tile_size, int(tile_size * 1.5)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

world_data = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 1], 
[1, 0, 3, 0, 0, 2, 2, 2, 0, 0, 0, 0, 2, 2, 0, 0, 0, 2, 2, 0, 0, 0, 2, 2, 2, 2, 1], 
[1, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 1],
[1, 0, 0, 0, 0, 2, 2, 2, 0, 0, 3, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 0, 0, 0, 2, 1, 1, 1, 4, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

player = Player(100, screen_height - 130)
blob_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()

world = World(world_data)

state="title"
next=False
btnNew=button("btnPlay.png")
btnQuiz=button("btnQuiz.png")
btnResult=button("btnResult.png")
btnLesson=button("btnLesson.png")
btnBack= button("btnBack.png")
btnExit=button("btnExit.png")
btnMenu=button("btnMenu.png")
btnNext=button("btnNext.png")


welcome = bigfont.render(('WELCOME TO MY GAME'), True, (255,255,255))
result = bigfont.render(('results coming soon...'), True, (0,0,0))
error = bigfont.render(('Error!!!!!!!!!'), True, (200,0,10))

try:
  while keepGoing:
    clock.tick(60) #delay
    screen.fill((9,131,180)) 

    if state=="title":
        setBackground("title.png")
        bm=screen.blit(btnMenu,(350,270))#bm- menu button

    elif state=="menu":
       # buttons-------------------
        setBackground("menu.png")
        bp=screen.blit(btnNew,(100,320))   #bp- rectangle arround button btnPLay
        bq=screen.blit(btnQuiz,(225,320))    #bq- rectangle arround button btnQuiz
        br=screen.blit(btnResult,(350,320))     #br- rectangle arround button btnResult
        bl=screen.blit(btnLesson,(475,320))    #bl- rectangle around buttonLesson
        be=screen.blit(btnExit,(600,320))    #be- rectangle around buttonExit

    elif state=="game":  
      screen.blit(bg_img, (0, 0))
      screen.blit(sun_img, (100, 100))

      world.draw()

      if game_over == 0:
        blob_group.update()

        if pygame.sprite.spritecollide(player, coin_group, True):
          score += 1
        draw_text("X " + str(score), font_score, white, tile_size - 10, 10)
    
      blob_group.draw(screen)
      coin_group.draw(screen)
      exit_group.draw(screen)

      game_over = player.update(game_over)
      
      #if play has died
      if game_over == -1:
            player.reset(100, screen_height - 130)
            game_over = 0   
            score = 0
      #if player has completed the level
      if game_over == 1:
            #reset game and go to next level
            state="menu"

    elif state=="quiz":
            # ---------------code for the quiz-------------------
      question=0
      correctAnswers=0
      correct=bool()

      setBackground("quiz.png")

      btnNext=button("btnNext.png")
      bnq=screen.blit(btnNext,(650,380))   #bnq- rectangle around button btnNext(questions)
      bb=screen.blit(btnBack,(50,380))   #bb- rectangle around button btnBack

    elif state=="questions":
      setBackground("q"+str(question)+".png")

      # answer choices for each question 
      option1=quizOption("q"+str(question)+"o1.png")
      o1=screen.blit(option1,(35,200))

      option2=quizOption("q"+str(question)+"o2.png")
      o2=screen.blit(option2,(235,200))

      option3=quizOption("q"+str(question)+"o3.png")
      o3=screen.blit(option3,(435,200))


      option4=quizOption("q"+str(question)+"o4.png")
      o4=screen.blit(option4,(635,200))
      if correct:
        setBackground("correct.png")
        bnq=screen.blit(btnNext,(650,380)) 
      else:
        setBackground("incorrect.png")
        bnq=screen.blit(btnNext,(650,380)) 

    elif state=="result":
            # ---------------code for the quiz results-------------------
      setBackground("result.png")
      bb=screen.blit(btnBack,(400,380))   #bb- rectangle around button btnBack


    elif state=="lesson":
            # ---------------code for the lesson 
      lessonNumber=0            
      setBackground("lesson.png")
      bnl=screen.blit(btnNext,(650,380)) #bnl - button next lesson
      bb=screen.blit(btnBack,(50,380))

    elif state=="lessons":
            
      if lessonNumber<5:
        setBackground("lesson"+str(lessonNumber)+".png")
        bnl=screen.blit(btnNext,(650,380)) #bnl - button next lesson
      elif lessonNumber==5:
        setBackground("lesson5.png")
        bb=screen.blit(btnBack,(50,380))
            
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

        elif state=="menu":              
          if bp.collidepoint(pos):
            state="game"
          elif bq.collidepoint(pos):
            state="quiz"
          elif br.collidepoint(pos):
            state="result"   
          elif bl.collidepoint(pos):
            state="lesson"  
          elif be.collidepoint(pos):
            keepGoing = False

        elif state=="results":
          
          if bb.collidepoint(pos):
            state="menu"  

        elif state=="quiz":
          if bnq.collidepoint(pos):
            state="questions"
            question+=1
          elif bb.collidepoint(pos):
            state="menu"  

        elif state=="questions":
            if bnq.collidepoint(pos):
              question+=1

            #correct answers
            if o1.collidepoint(pos) and question!=1 or question!=5:
              correctAnswers+=1
              correct=True
            elif o3.collidepoint(pos) and question==5:
              correctAnswers+=1
              correct=True
            elif o4.collidepoint(pos) and question==1:
              correctAnswers+=1
              correct=True

            #wrong answers
            elif (o1.collidepoint(pos) and (question==1 or question==5)) or o2.collidepoint(pos) or (o3.collidepoint(pos) and question!=5) or (o4.collidepoint(pos) and question!=1):
              correct=False

            if question==5:
              state="menu"

        #elif bb.collidepoint(pos):
          #state="menu"

        elif state=="lesson" or state=="lessons":
          if bnl.collidepoint(pos):
            state="lessons" 
            lessonNumber+=1    
          elif bb.collidepoint(pos):
            state="menu"  

finally:
  pygame.quit()  # Keep this IDLE friendly 