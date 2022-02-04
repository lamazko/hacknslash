import pygame
import os
import time
import random

#initialise les fonts
pygame.font.init()

WIDTH, HEIGHT = 1000,1000
FENETRE = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("LE GIGA VAMPIRE SURVIVOR DE LUMA")



#Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("images","grass.jpg")),(WIDTH,HEIGHT))

#Player

PLAYER = pygame.image.load(os.path.join("images","pixel_ship_yellow.png"))

#Monsters

ENEMY_red = pygame.image.load(os.path.join("images","pixel_ship_red_small.png"))
ENEMY_green = pygame.image.load(os.path.join("images","pixel_ship_green_small.png"))
ENEMY_blue = pygame.image.load(os.path.join("images","pixel_ship_blue_small.png"))

#Projos

RED_LASER = pygame.image.load(os.path.join("images","pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("images","pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("images","pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("images","pixel_laser_yellow.png"))

class Character:
	def __init__(self,x,y,health=100):
		self.x = x
		self.y = y
		self.health = health
		self.char_img = None
		self.attack_img = None
		self.attack = []
		self.cooldown = 0

	def draw(self,window):
		#pygame.draw.rect(fenetre,couleur,(positionx, positiony, largeur,longueur),opacité)
		#pygame.draw.rect(window,(255,0,0),(self.x,self.y, 50,50),0)
		window.blit(self.char_img,(self.x,self.y))

	def get_width(self):
		return self.char_img.get_width()

	def get_height(self):
		return self.char_img.get_height()


class Player(Character):
	def __init__(self,x,y,health=100):
		super().__init__(x,y,health)
		self.char_img = PLAYER
		self.attack_img = YELLOW_LASER
		# recupere la hitbox exacte au lieu d'un carré
		self.mask = pygame.mask.from_surface(self.char_img)
		self.max_health = health


class Enemy(Character):
	ENEMY_MAP = {"red": (ENEMY_red,RED_LASER),
				"green": (ENEMY_green,GREEN_LASER),
				"blue": (ENEMY_blue,BLUE_LASER)
				}
	#color pour differencier les enemies
	def __init__(self,x,y,color,health=100):
		super().__init__(x,y,health)
		self.char_img, self.attack_img = self.ENEMY_MAP[color]
		self.mask = pygame.mask.from_surface(self.char_img)

#move que pour space invaders
	def move(self,velocity):
		self.y += velocity



class Projos:
	def __init__(self,x,y,img):
		self.x = x 
		self.y = y 
		self.img = img 
		self.mask = pygame.mask.from_surface(self.img)

	def draw(self,window):
		window.blit(self.img,(self.x , self.y))


	def move(self,velocity):
		self.y += velocity 


	def off_screen(self,height):
		return self.y <= height and self.y >= 0

	def collision(self,obj):
		return collide(obj,self)


def collide(obj1,obj2):
	offset_x = obj2.x - obj1.x 
	offset_y = obj2.y - obj1.y
	return obj1.mask.overlap(obj2.mask,(offset_x,offset_y)) != None

def main():
	lost = False
	lost_count = 0
	run = True
	FPS = 60
	level = 0
	lives = 20
	player_velocity = 5
	enemy_velocity = 5
	#choisi notre fonts)
	main_font = pygame.font.SysFont("comicsans",50)
	loss_font = pygame.font.SysFont("comicsans",60)
	clock = pygame.time.Clock()

	perso = Player(300,650)

	enemies = []
	wave_length = 5

	def redraw_window():
		FENETRE.blit(BG,(0,0))

		# écrire du texte
		#color = (RGB) (black = 0,0,0 / white = 255)
		lives_label = main_font.render(f"lives: {lives}", 1, (255,255,0))
		level_label = main_font.render(f"Level: {level}",1,(255,0,255))

		FENETRE.blit(lives_label,(10,10))
		FENETRE.blit(level_label,(WIDTH - level_label.get_width() - 10,10))

		for enemy in enemies:
			enemy.draw(FENETRE)

		perso.draw(FENETRE)

		if lost:
			lost_label = loss_font.render("You giga lost tarlouse",1,(255,255,255))
			FENETRE.blit(lost_label,(WIDTH//2 - lost_label.get_width() /2 , HEIGHT//2 - lost_label.get_height() /2 ))



		pygame.display.update()


	while run:
		clock.tick(FPS)
		redraw_window()
		if lives <= 0 or perso.health <= 0:
			lost = True
			lost_count += 1

		if lost:
			if lost_count > FPS * 3:
				run = False
			else:
				continue



		if len(enemies) == 0:
			level += 1
			wave_length += 5
			for i in range(wave_length):
				enemy = Enemy(random.randrange(50,WIDTH - 100),random.randrange(-1000,-100),random.choice(["red","blue","green"]))
				enemies.append(enemy)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		keys = pygame.key.get_pressed()
		if (keys[pygame.K_q] or keys[pygame.K_LEFT]) and perso.x - player_velocity > 0: #left
			perso.x -= player_velocity
		if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and perso.x + player_velocity + perso.get_width() < WIDTH: #right
			perso.x += player_velocity			
		if (keys[pygame.K_z] or keys[pygame.K_UP]) and perso.y - player_velocity > 0: #up
			perso.y -= player_velocity
		if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and perso.y + player_velocity + perso.get_height() < HEIGHT: #down
			perso.y += player_velocity

		for enemy in enemies.copy():
			enemy.move(enemy_velocity)
			if enemy.y + enemy.get_height()> HEIGHT:
				lives -= 1
				enemies.remove(enemy)



		
main()
