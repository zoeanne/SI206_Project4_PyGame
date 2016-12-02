import pygame
from pygame.sprite import *
import random
import sys
import time

pygame.init()

width = 800
height = 600

score = 0

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Super Scooping Challenge")
clock = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
pink = (255,20,147)
blue = (240,248,255)

f = pygame.font.Font("freesansbold.ttf", 30)

class Tub(Sprite):   
    def __init__(self):
        Sprite.__init__(self)
        self.image = pygame.image.load("tub.bmp").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
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

class Truck(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pygame.image.load("truck.bmp").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = height - 100      
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
        self.rect.x = random.randint(0, width-100) #random x position, minus 100 so image does not go off screen
        self.rect.y = -9000 + y_pos #start off screen so starting point to fall down is not visible
    def update(self):
        self.rect.y += 3
        if self.rect.y > height:
            self.kill()
            
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





def game_intro():

    pygame.mouse.set_visible(False)
    
    pygame.mixer.music.load("Ice_Cream_Song_Loop.wav")
    pygame.mixer.music.play(-1, 0.0)

    truck = Truck()
    sprites = pygame.sprite.RenderPlain(truck)

    intro = True
    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
                    
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




def gameover():
    screen.fill(blue)
    a = pygame.font.Font("freesansbold.ttf", 27)
    b = pygame.font.Font(None, 25)
    global score
    if score < 50:
        x = a.render("Novice Scooper! Your scooping score is " + str(score), False, red)
        y = b.render("Keep practicing to become an EXPERT Super Scooper! (press spacebar to play again)", False, black)
    if score >=50 and score <80:
        x = a.render("Super Scooper! Your scooping score is " + str(score), False, red)
        y = b.render("Keep practicing to become an EXPERT Super Scooper! (press spacebar to play again)", False, black)
    if score >=80:
        x = a.render("EXPERT Super Scooper! Your scooping score is " + str(score), False, red)
        y = b.render("You've demonstrated your skills and are now reading to show the world", False, black)
        z = b.render("your Super Scooping abilities! Thanks for playing! (press spacebar to play again)", False, black)
        screen.blit(z, (50, 330))
    screen.blit(x, (50,200)) #x, y
    screen.blit(y, (50, 300))
    pygame.display.update()

    gameover = True

    while gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    score = 0
                    game_loop()

            pygame.display.update()
                    

               
        

#maxscore user can reach is 120 points

def game_loop():

##    bg = pygame.image.load("bg.bmp").convert()
##    screen.blit(bg, (0,0))

    pygame.mouse.set_visible(False)


    tub = Tub()
    blocks = []
    extra_blocks = []
    enemy_blocks = []
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
                
        global score
        for i in blocks:
            score += (1*(len(pygame.sprite.spritecollide(tub, i, True))))
        for i in extra_blocks:
            score += (3*(len(pygame.sprite.spritecollide(tub, i, True))))
        for i in enemy_blocks:
            score -= (3*(len(pygame.sprite.spritecollide(tub, i, True))))
            
        sprites.update()
        screen.fill(white)
        t = f.render("Score = " + str(score), False, black)
        screen.blit(t, (0,0))
        sprites.update()
        sprites.draw(screen)
        pygame.display.update()
##        clock.tick(60)

        if len(sprites) == 1:
            gameover()


game_intro()        



