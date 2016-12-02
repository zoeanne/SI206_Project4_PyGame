# Name: Zoe Halbeisen
# Unique name: zoeanne
# Unique ID: 8419 4416
# Section Day/Time: Wednesday 5:30-6:30 

import pygame
from pygame.sprite import *
import random
import sys
import time

pygame.init()

width = 800
height = 600

score = 0 #max score user can reach is 120

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Super Scooping Challenge")
clock = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
pink = (255,20,147)
blue = (240,248,255)

f = pygame.font.Font("freesansbold.ttf", 30)


#----------------------------Sprite classes--------------------------------------------------------------------
class Tub(Sprite):   
    def __init__(self):
        Sprite.__init__(self)
        self.image = pygame.image.load("tub.bmp").convert_alpha() 
        self.image = pygame.transform.scale(self.image, (100, 100)) #scaling image to proper size
        self.rect = self.image.get_rect()
        self.rect.x = width/2 - 50
        self.rect.y = height - 100       
    def update(self):
        keys = pygame.key.get_pressed()
        dist = 5
        if keys [pygame.K_LEFT]:
            self.rect.x -= dist
        if keys [pygame.K_RIGHT]:
            self.rect.x += dist
        #Adding boundaries so sprite does not go off screen, offset by 100 to account for image size
        if self.rect.x > width - 100:
            self.rect.x = width - 100
        if self.rect.x < 0:
            self.rect.x = 0

class Truck(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pygame.image.load("truck.bmp").convert_alpha()
        self.image = pygame.transform.scale(self.image, (180, 150)) #w,h
        self.rect = self.image.get_rect()
        self.rect.x = -300 #negative because I want Truck sprite to start off screen and come when music starts
        self.rect.y = height - 150 #minus 150 to offset for height of Truck image   
    def update(self):
        dist = 1
        self.rect.x += dist
        if self.rect.x > width:
            self.kill()

class Single_scoop(Sprite):
    def __init__(self, y_pos):
        Sprite.__init__(self)
        self.image = pygame.image.load("singlescoop_pink.bmp").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width-100) #sprite will start at random x position but minus 100 (the image size) so image does not go off screen
        self.rect.y = -9000 + y_pos #negative 9000 to start off screen so starting point to fall down is not visible, also sets how long game will go as other sprites of this class will fall in decreasing intervals
    def update(self):
        self.rect.y += 3
        if self.rect.y > height:
            self.kill() #kill the sprite after it's off screen. Useful later so game will know when to end.


#------------Sprite classes that inherit from Single_scoop class----------------------------------------------       
class Triple_scoop(Single_scoop): 
    def __init__(self, y_pos):
        Sprite.__init__(self)
        self.image = pygame.image.load("triplescoop.bmp").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width-100)
        self.rect.y = -9000 + y_pos

class Scooper(Single_scoop):
    def __init__(self, y_pos):
        Sprite.__init__(self)
        self.image = pygame.image.load("scooper.bmp").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width-100)
        self.rect.y = -9000 + y_pos


#----------------Function for starting screen-------------------------------------------------------------------
def game_intro():
    
    pygame.mixer.music.load("Ice_Cream_Song_Loop.wav")
    pygame.mixer.music.play(-1, 0.0) #play the song on a loop and start at the beginning 

    truck = Truck()
    sprites = pygame.sprite.RenderPlain(truck)

    intro = True
    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            #If user presses spacebar key, game_loop function is called and the game begins     
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_SPACE:
                    game_loop()

            #Creating an easter egg inspired by Warren Robinett :P
            if event.type == pygame.MOUSEBUTTONUP:  
                pos = pygame.mouse.get_pos()
                l = pygame.font.Font("freesansbold.ttf",30)
                m = l.render("Created by Zoe Halbeisen", False, pink)
                if truck.rect.collidepoint(pos):
                    pygame.mouse.set_visible(False)
                    screen.blit(m, (200,400))
                    pygame.display.update()
                    pygame.time.wait(3000)
                                      
        screen.fill(blue)

        x = pygame.font.Font("freesansbold.ttf", 40)
        y = pygame.font.Font("freesansbold.ttf",30)
        z = pygame.font.Font("freesansbold.ttf",20)
        
        a = x.render("Super Scooping Challenge!", False, pink)
        b = y.render("Press the spacebar to start", False, pink)
        c = z.render("Instructions: Use the arrow keys to catch as much ice cream as you can,", False, black)
        d = z.render("but avoid the scooper!", False, black)
        e = z.render("Single scoop = +1", False, black)
        f = z.render("Triple scoop = +3", False, black)
        g = z.render("Scooper = -3", False, black)

        screen.blit(a, (150,100))
        screen.blit(b, (200,150))
        screen.blit(c, (50, 220))
        screen.blit(d, (50, 250))
        screen.blit(e, (50, 300))
        screen.blit(f, (50, 330))
        screen.blit(g, (50, 360))

        sprites.update()
        sprites.update()
        sprites.draw(screen)
        pygame.display.update()


#----------------Function for ending screen----------------------------------------------------------------------
def gameover():

    screen.fill(blue)
    image = pygame.image.load("triplescoop.bmp").convert_alpha()
    a = pygame.font.Font("freesansbold.ttf", 27)
    b = pygame.font.Font(None, 25)

    global score #need this since score was created in global name space 
    if score < 50:
        x = a.render("Novice Scooper! Your scooping score is " + str(score), False, pink)
        y = b.render("Keep practicing to become an EXPERT Super Scooper! (press spacebar to play again)", False, black)
    if score >=50 and score <80:
        x = a.render("Super Scooper! Your scooping score is " + str(score), False, pink)
        y = b.render("Keep practicing to become an EXPERT Super Scooper! (press spacebar to play again)", False, black)
    if score >=80:
        x = a.render("EXPERT Super Scooper! Your scooping score is " + str(score), False, pink)
        y = b.render("You've demonstrated your skills and are now reading to show the world", False, black)
        z = b.render("your Super Scooping abilities! Thanks for playing! (press spacebar to play again)", False, black)
        screen.blit(z, (50, 280))

    screen.blit(x, (50,200)) #x, y
    screen.blit(y, (50, 250))
    screen.blit(image, (width/2, height/2))
    pygame.display.update()

    gameover = True

    while gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            #If user presses spacebar key, game_loop function is called and the game starts again. Score also resets to zero.    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    score = 0
                    game_loop()

            pygame.display.update()
                    

#----------------Function for game logic-------------------------------------------------------------------------
def game_loop():

    pygame.mouse.set_visible(False) #hide mouse pointer so it's not in the way of the game

    tub = Tub()
    #Initiated lists to append sprites to
    blocks = []
    extra_blocks = []
    enemy_blocks = []

    #Appending sprites to lists. Range is how many sprites of a certain class I want in the game.
    #And changing y values so the sprites fall at decreasing intevals 
    for i in range(60):
        y = i * 150 
        blocks.append(pygame.sprite.RenderPlain(Single_scoop(y)))
    for i in range(20):
        y = i * 350
        extra_blocks.append(pygame.sprite.RenderPlain(Triple_scoop(y)))
    for i in range(30):
        y = i * 250 
        enemy_blocks.append(pygame.sprite.RenderPlain(Scooper(y)))

    sprites = pygame.sprite.RenderPlain(tub, *blocks, *extra_blocks, *enemy_blocks)

    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        #incrementing or decrementing the score based on sprite collision. 
        #spritecollide detects collision and also kills the sprite (and removes from groups)       
        global score
        for i in blocks:
            score += (1*(len(pygame.sprite.spritecollide(tub, i, True))))
        for i in extra_blocks:
            score += (3*(len(pygame.sprite.spritecollide(tub, i, True))))
        for i in enemy_blocks:
            score -= (3*(len(pygame.sprite.spritecollide(tub, i, True))))
            
        sprites.update()
        screen.fill(blue)
        t = f.render("Score = " + str(score), False, black) #update the scare and blit it to the screen
        screen.blit(t, (0,0))
        sprites.update()
        sprites.draw(screen)
        pygame.display.update()

        #When there is only 1 sprite left (the tub sprite) then the game is over and goes to the gameover screen
        if len(sprites) == 1:
            gameover()

            
#----------------------------------------------------------------------------------------------------------------

#Call game_intro function to display start screen which calls game_loop function to start the game 
game_intro()        



