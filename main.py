import pygame
import os
import time
import random



WIDTH, HEIGHT = 1000,1000
FENETRE = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("LE GIGA VAMPIRE SURVIVOR DE LUMA")



#Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("images","grass.jpg")),(WIDTH,HEIGHT))

#Player

PLAYER = pygame.image.load(os.path.join("images","pixel_ship_yellow.png"))

#Monsters

PLAYER = pygame.image.load(os.path.join("images","pixel_ship_red_small.png"))
PLAYER = pygame.image.load(os.path.join("images","pixel_ship_green_small.png"))
PLAYER = pygame.image.load(os.path.join("images","pixel_ship_blue_small.png"))

#Projos

RED_LASER = pygame.image.load(os.path.join("images","pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("images","pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("images","pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("images","pixel_laser_yellow.png"))

def main():
	run = True
	FPS = 60
	clock = pygame.time.Clock()


	def redraw_window():
		FENETRE.blit(BG,(0,0))
		pygame.display.update()




	while run:
		clock.tick(FPS)
		redraw_window()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			


main()
