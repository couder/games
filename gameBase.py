import pygame, sys
import pygame.event as GAME_EVENTS
from random import randint
from time import sleep
pygame.init()

clock = pygame.time.Clock()

frameRate= 60
speedNormal = 20
speedX = 0
speedY = 0
posX = 250
posY = 250

window = pygame.display.set_mode((800,700))

while True:
	window.fill((0,0,0))

	if posX<0:
		posX = 0
	elif 800<posX:
		posX = 800
	else:
		posX = posX + speedX

	if posY<0:
		posY = 0
	elif 700<posY:
		posY = 700
	else:
		posY = posY + speedY

	# pygame.draw.rect(window, (randint(0,255),randint(0,255),randint(0,255)), (0,0, 50, 30) )
	pygame.draw.circle(window, (randint(0,255),randint(0,255),randint(0,255)), (posX,posY), 20, 0 )
	pygame.draw.circle(window, (randint(0,255),randint(0,255),randint(0,255)), (posX,posY), 22, 1 )

	for event in GAME_EVENTS.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT and 0 < posX-20:
				speedX = 0 - speedNormal
			if event.key == pygame.K_RIGHT and posX+20 < 800:
				speedX = speedNormal
			if event.key == pygame.K_UP and 0 < posY-20:
				speedY = 0 - speedNormal
			if event.key == pygame.K_DOWN and posY+20 < 700:
				speedY = speedNormal
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				speedX = 0
			if event.key == pygame.K_RIGHT:
				speedX = 0
			if event.key == pygame.K_UP:
				speedY = 0
			if event.key == pygame.K_DOWN:
				speedY = 0
    
	pygame.display.update()
	clock.tick(frameRate)