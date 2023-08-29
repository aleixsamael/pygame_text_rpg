import pygame

# This first part of the game is mostly taken from the pygame documentation.

# pygame setup
pygame.init()
screen = pygame.display.set_mode((700,400))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption('pygame RPG')


while running:

	# poll for events
	# enable user to quit game by clicking X to close the window
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			# this will end the program
			running = False

	# filling screen with a colour here to wipe away anything from the last frame
	background_colour = (123,23,80)
	screen.fill(background_colour)

	# RENDER GAME HERE

	# flip() the display to put the work on the screen
	pygame.display.flip()

	clock.tick(60) # limits FPS to 60

pygame.quit()