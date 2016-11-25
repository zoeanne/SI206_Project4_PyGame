#Project 4 PyGame

import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

car_width = 150

gameDisplay = pygame.display.set_mode((display_width,display_height)) #setting window size 
pygame.display.set_caption('A bit Racey') #setting display name
clock = pygame.time.Clock() #setting game clock

carImg = pygame.image.load('pug.png')
carImg = pygame.transform.scale(carImg, (150, 150)) #scaling picture (length, heighth)

def things(thingx, thingy, thingw, thingh, color):
        pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x,y):
        gameDisplay.blit(carImg,(x,y))

def text_objects(text, font): #later on make it def text_objects(text, font, color) to change colors of different messages
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

def message_display(text):
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()
        
        time.sleep(2) #leave message on screen for 2 seconds 

        game_loop() #restart game again

def crash():
        message_display('You Crashed')

def game_loop(): #logic for game
        x = (display_width * 0.45)
        y = (display_height * 0.8)

        x_change = 0

        thing_startx = random.randrange(0, display_width)
        thing_starty = -600 #want object to start off the screen
        thing_speed = 10
        thing_width = 100
        thing_height = 100

        gameExit = False 

        #event handling
        while not gameExit:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                                
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_LEFT:
                                        x_change = -5
                                elif event.key == pygame.K_RIGHT:
                                        x_change = 5

                        if event.type == pygame.KEYUP:
                                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                                        x_change = 0

                
                x += x_change #variable handling

                gameDisplay.fill(white)
                #things(thingx, thingy, thingw, thingh, color)
                things(thing_startx, thing_starty, thing_width, thing_height, black)
                thing_starty += thing_speed #each time we loop, add 10 to it to make object move down y axis 
                car(x,y)
                
                if x > display_width - car_width or x < 0: #adding boundaries for car, minus car_width because accounting for x being top left corner of car picture
                        crash()

                if thing_starty > display_height:
                        thing_starty = 0  - thing_height
                        thing_startx = random.randrange(0, display_width) 

                
                pygame.display.update() #updates entire surface
                #pygame.display.flip() another way to update the entire surface
                clock.tick(60) #running through loop at 60 frames per second

game_loop() 

pygame.quit()
quit()

