import pygame, sys
import pygame.event as GAME_EVENTS
from random import randint
from time import sleep
pygame.init()


def player(window, pos, size):
	pygame.draw.circle(window, (randint(0,255),randint(0,255),randint(0,255)), pos, size + 2, 1 )
	return pygame.draw.circle(window, (randint(0,255),randint(0,255),randint(0,255)), pos, size, 0 )

def move(event):
	global speedX, speedY, posXPlayer, posYPlayer

	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_LEFT and 0 < posXPlayer-40:
			speedX = -5
			speedY = 0
		if event.key == pygame.K_RIGHT and posXPlayer+40 < 800:
			speedX = 5
			speedY = 0
		if event.key == pygame.K_UP and 0 < posYPlayer-40:
			speedY = -5
			speedX = 0
		if event.key == pygame.K_DOWN and posYPlayer+40 < 700:
			speedY = 5
			speedX = 0
		if event.key == pygame.K_ESCAPE:
			pygame.quit()
			sys.exit()

def food(window,pos):
	return pygame.draw.circle(window, (255,0,0), pos, 10, 0 )

# def eat(posFood,posPlayer):
# 	# if posPlayer[0] - 20 == posFood[0] and posPlayer[1] - 20 == posFood[1]:
# 	# 	return True
# 	# elif posPlayer[0] + 20 == posFood[0] and posPlayer[1] - 20 == posFood[1]:
# 	# 	return True
# 	# elif posPlayer[0] - 20 == posFood[0] and posPlayer[1] + 20 == posFood[1]:
# 	# 	return True
# 	# elif posPlayer[0] + 20 == posFood[0] and posPlayer[1] + 20 == posFood[1]:
# 	# 	return True
# 	# else:
# 	# 	return False
# 	return pygame.

def game():
	global speedX, speedY, posXPlayer, posYPlayer

	clock = pygame.time.Clock()

	frameRate= 60
	speedX = 5
	speedY = 5
	posXPlayer = 250
	posYPlayer = 250
	sizePlayer = 20
	posXFood = randint(0,800)
	posYFood = randint(0,700)

	window = pygame.display.set_mode((800,700))

	while True:
		window.fill((0,0,0))

		if posXPlayer<0:
			posXPlayer = 0
		elif 800<posXPlayer:
			posXPlayer = 800
		else:
			posXPlayer = posXPlayer + speedX

		if posYPlayer<0:
			posYPlayer = 0
		elif 700<posYPlayer:
			posYPlayer = 700
		else:
			posYPlayer = posYPlayer + speedY

		
		foodo = food(window,(posXFood,posYFood))
		playero = player(window,(posXPlayer,posYPlayer), sizePlayer)

		if playero.colliderect(foodo):
			posXFood = randint(0,800)
			posYFood = randint(0,700)
			sizePlayer += 20

		for event in GAME_EVENTS.get():
			move(event)
	    
		pygame.display.update()
		clock.tick(frameRate)


game()