#Project 4 PyGame
import pygame

pygame.init()

display_width = 800
display_height = 600

black = (0,0,)
white = ()

gameDisplay = pygame.display.set_mode((display_width,display_height)) #setting window size 
pygame.display.set_caption('A bit Racey') #setting display name
clock = pygame.time.Clock() #setting game clock

#Game loop: logic for game
crashed = False #start the game and have not crashed yet

while not crashed: 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True 


	pygame.display.update() #updates entire surface
	#pygame.display.flip() another way to update the entire surface
	clock.tick(60) #running through loop at 60 frames per second

pygame.quit() 
quit()
