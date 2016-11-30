from pygame import *
from pygame.sprite import *
import random
import sys

init()

width = 800
height = 600

screen = display.set_mode((width, height))
display.set_caption("window title")
clock = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

f = font.Font(None, 25)

class Tub(Sprite):   
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("tub.bmp").convert_alpha()
        self.image = transform.scale(self.image, (100, 100))
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
        self.image = image.load("singlescoop_pink.bmp").convert_alpha()
        self.image = transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width-100) #random x position, minus 100 so image does not go off screen
        self.rect.y = -5000 + y_pos #start off screen so starting point to fall down is not visible
##        print(self.rect.y)
    def update(self):
        self.rect.y += 3
        if self.rect.y > height:
            self.kill()
            

class Triple_scoop(Single_scoop):
    def __init__(self, y_pos):
        Sprite.__init__(self)
        self.image = image.load("triplescoop.bmp").convert_alpha()
        self.image = transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width-100)
        self.rect.y = -5000 + y_pos
        

tub = Tub()
blocks = []
extra_blocks = []
for i in range(33):
    y = i * 150
    blocks.append(pygame.sprite.RenderPlain(Single_scoop(y)))
for i in range(10):
    y = i * 250
    extra_blocks.append(pygame.sprite.RenderPlain(Triple_scoop(y)))
sprites = pygame.sprite.RenderPlain(tub, *blocks, *extra_blocks)
score = 0


def game_loop():
    
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                sys.exit()
                
        global score
        for i in blocks:
            score += (1*(len(pygame.sprite.spritecollide(tub, i, True))))
        for i in extra_blocks:
            score += (3*(len(pygame.sprite.spritecollide(tub, i, True))))

            
        sprites.update()
        screen.fill(white)
        t = f.render("Score = " + str(score), False, black)
        screen.blit(t, (0,0))
        sprites.update()
        sprites.draw(screen)
        display.update()
        clock.tick(60)

        
game_loop()


















            #elif tub.rect.colliderect(Singlescoop_pink()):    
##            elif event.type != pygame.QUIT:
##                blocks_hit_list = pygame.sprite.spritecollide(tub, blocks, True)
##                for block in blocks_hit_list:
##                    global score
##                    score += 1
##                    score += len(pygame.sprite.spritecollide(tub, blocks, True))
