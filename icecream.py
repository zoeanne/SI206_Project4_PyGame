import pygame
from pygame.sprite import *
import random
import sys
import time

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("window title")
clock = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

f = pygame.font.Font(None, 40)

class Tub(Sprite):   
    def __init__(self):
        Sprite.__init__(self)
        self.image = pygame.image.load("tub.bmp").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = width/2
        self.rect.y = height - 100       
    def update(self):
        keys = pygame.key.get_pressed()
        dist = 5
        if keys [pygame.K_LEFT]:
            self.rect.x -= dist
        if keys [pygame.K_RIGHT]:
            self.rect.x += dist

class Single_scoop(Sprite):
    def __init__(self, y_pos):
        Sprite.__init__(self)
        self.image = pygame.image.load("singlescoop_pink.bmp").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width-100) #random x position, minus 100 so image does not go off screen
        self.rect.y = -9000 + y_pos #start off screen so starting point to fall down is not visible
##        print(self.rect.y)
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


def gameover():
    f = pygame.font.Font(None, 30)
    t = f.render("Game Over! Your ending score is " + str(score), False, red)
    screen.blit(t, (200,300)) #x, y 
    pygame.display.update()
    time.sleep(5)
    pygame.quit()
    sys.exit()
        
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
score = 0
#maxscore user can reach is 120 points

def game_loop():

    pygame.mixer.music.load("Ice_Cream_Song_Loop.wav")
    pygame.mixer.music.play(-1, 0.0)

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

        
game_loop()


















            #elif tub.rect.colliderect(Singlescoop_pink()):    
##            elif event.type != pygame.QUIT:
##                blocks_hit_list = pygame.sprite.spritecollide(tub, blocks, True)
##                for block in blocks_hit_list:
##                    global score
##                    score += 1
##                    score += len(pygame.sprite.spritecollide(tub, blocks, True))
