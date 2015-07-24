#imports
import pygame, sys, random
from pygame.locals import *
pygame.init()

#constants
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600
RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)
level =0
fps = 25
addnewice = 15

#Global variables

mario_up = False
mario_down = False
gravity = False
mario_speed = 20
done = True

#classes
class dragon:
	global dragon_rect, cactus_top_rect, cactus_bottom_rect, canvas
	up = False
	down = True
	speed = 15
	def __init__(self):
		self.dragon_image = load_image('Images/dragon.png')
		self.dragon_rect = self.dragon_image.get_rect()
		self.dragon_rect.right = WINDOW_WIDTH - 50
		self.dragon_rect.top = WINDOW_HEIGHT/2

	def update(self):
		if(self.dragon_rect.top < cactus_top_rect.bottom):
			self.up = False
			self.down = True

		if(self.dragon_rect.bottom > cactus_bottom_rect.top):
			self.up = True
			self.down = False

		if(self.up):
			self.dragon_rect.top -= self.speed

		if(self.down):
			self.dragon_rect.top += self.speed

		canvas.blit(self.dragon_image, self.dragon_rect)
	
	def height(self):
		return self.dragon_rect.top

	def center(self):
		return self.dragon_rect.centery

class flames:
	xspeed = 15
	yspeed = 0
	def __init__(self):
		self.fire_image = load_image('Images/fireball.png')
		self.fire_rect = self.fire_image.get_rect()
		self.surface = pygame.transform.scale(self.fire_image,(20,20))
		self.height = Dragon.height() + 20
		self.fire_rect = pygame.Rect(WINDOW_WIDTH - 156, self.height,20,20)

	def update(self):
		self.yspeed = (Mario.center() - self.fire_rect.centery)/30
		self.fire_rect.right -= self.xspeed
		self.fire_rect.top += self.yspeed

	def collision(self):
		if fire_rect.left ==0:
			return True
		else:
			return False
		
		
class ice:
	xspeed = 15
	yspeed = 0
	def __init__(self):
		self.ice_image = load_image('Images/new_ice.png')
		self.ice_rect = self.ice_image.get_rect()
		self.ice_ball = pygame.transform.scale(self.ice_image,(20,20))
		self.height = Mario.height()+10
		self.ice_rect = pygame.Rect(100,self.height,20,20)

	def update(self):
		self.yspeed = (Dragon.center()-self.ice_rect.centery)/30
		self.ice_rect.centerx += self.xspeed
		self.ice_rect.centery += self.yspeed


class mario:
	global fire_rect, mario_rect,cactus_top, cactus_bottom

	def __init__(self):
		self.mario_image = load_image('Images/maryo.png')
		self.mario_rect = self.mario_image.get_rect()
		self.mario_rect.left = 50
		self.mario_rect.top = WINDOW_HEIGHT/2
		self.score = 0

	def update(self):
		if(mario_up):
			self.mario_rect.top -= mario_speed

		if(mario_down):
			self.mario_rect.top += mario_speed

		if(gravity):
			self.mario_rect.top += mario_speed/2

		canvas.blit(self.mario_image,self.mario_rect)

	def center(self):
		return self.mario_rect.centery	

	def height(self):
		return self.mario_rect.top


def load_image(imagename):
	return pygame.image.load(imagename)

def fire_mario(player_rect,flames):
	for f in flames:
		if player_rect.colliderect(f.fire_rect):
			return True
		return False

def terminate(): 
	done = False       
	pygame.quit()
	sys.exit()

def waitforkey():
	while True :                                     
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				terminate()
			if event.type == pygame.KEYDOWN:    
				if event.key == pygame.K_ESCAPE:
					terminate()
				#if event.key == K_UP:
				#	done = True
	
				return



def drawtext(text, font, surface, x, y):      
    textobj = font.render(text, 1, WHITE)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)



Dragon = dragon()

clock = pygame.time.Clock()
canvas = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('SAIF ALI KHAN')

cactus_top = load_image('Images/cactus_bricks.png')
cactus_top_rect = cactus_top.get_rect()
cactus_top_rect.bottom = 50

cactus_bottom = load_image('Images/fire_bricks.png')
cactus_bottom_rect = cactus_bottom.get_rect()	
cactus_bottom_rect.top = WINDOW_HEIGHT - 50

endimage = load_image('Images/end.png')
endimagerect = endimage.get_rect()
endimagerect.centerx = WINDOW_WIDTH/2
endimagerect.centery = WINDOW_HEIGHT/2

startimage = load_image('Images/start.png')
startimagerect = startimage.get_rect()
startimagerect.centerx = WINDOW_WIDTH/2
startimagerect.centery = WINDOW_HEIGHT/2

font = pygame.font.SysFont(None, 48)
scorefont = pygame.font.SysFont(None, 30)
result_font = pygame.font.SysFont(None,100)

canvas.blit(startimage, startimagerect)

pygame.display.update()
waitforkey()

topscore = 0

while True:
	flame_list = []
	ice_list = []
	flameadd = 0
	iceadd = 0
	iceball = True
	Mario = mario()
	dragon_health = 10
	addnewflame = 20
	level = 1
	
	
	while(done):
		for event in pygame.event.get():
			if event.type == QUIT:
				done = False
				pygame.quit()
				sys.exit()
	
			if event.type == KEYDOWN:
				if event.key == K_UP:
					mario_up = True
					mario_down = False
					gravity = False

				if event.key == K_DOWN:
					mario_up = False
					mario_down = True
					gravity = False

				if event.key == K_SPACE:
					if(iceball):
						newice = ice()
						ice_list.append(newice)
						iceball = False
						iceadd = 0

			if event.type == KEYUP:
				if event.key == K_UP:
                    			mario_up = False
                  			gravity = True
               			if event.key == K_DOWN:
                  			mario_down = False
                   			gravity = True
				if event.key == K_SPACE:
                  			mario_down = False
                   			gravity = True

		

		flameadd += 1
		if flameadd == addnewflame:
			flameadd = 0
			newflame = flames()
			flame_list.append(newflame)

		for f in flame_list:
			flames.update(f)

		for f in flame_list:
			if f.fire_rect.left <= 0:
				flame_list.remove(f)
	
		
		if(iceball == False):
			iceadd += 1

		if(iceadd == addnewice):
			iceball = True

		for i in ice_list:
			ice.update(i)

		for i in ice_list:
			if i.ice_rect.right >= WINDOW_WIDTH:
				ice_list.remove(i)

	

		Mario.update()
		Dragon.update()

		canvas.fill(BLACK)
		Mario.score += level
		canvas.blit(cactus_top,cactus_top_rect)
		canvas.blit(cactus_bottom,cactus_bottom_rect)
		canvas.blit(Mario.mario_image, Mario.mario_rect)
		canvas.blit(Dragon.dragon_image, Dragon.dragon_rect)

		for f in flame_list:
			canvas.blit(f.surface,f.fire_rect)

		for i in ice_list:
			canvas.blit(i.ice_ball,i.ice_rect)

		for i in ice_list:
			for f in flame_list:
				if (i.ice_rect.colliderect(f.fire_rect)):
					flame_list.remove(f)
					ice_list.remove(i)

		for i in ice_list:
			if Dragon.dragon_rect.colliderect(i.ice_rect):
				dragon_health -= 2
				ice_list.remove(i)

		drawtext('Score : %s | Top score : %s | Level is %d ' %(Mario.score, topscore, level), scorefont, canvas, 350, cactus_top_rect.bottom + 10)
		drawtext('Dragon %d ' %(dragon_health), scorefont, canvas, 1000, cactus_top_rect.bottom + 10)
			
				
		if dragon_health ==0:
			dragon_health = 10
			Mario.score += 500
			level += 1
			if addnewflame >= 10:
				addnewflame -= 2
			
		

		if fire_mario(Mario.mario_rect,flame_list):
			if Mario.score > topscore:
                		topscore = Mario.score
			drawtext('YOU LOST',  result_font, canvas, 410, cactus_top_rect.bottom + 50)
			break


		if ((Mario.mario_rect.top <= cactus_top_rect.bottom) or (Mario.mario_rect.bottom >= cactus_bottom_rect.top)):
			if Mario.score > topscore:
                		topscore = Mario.score
			drawtext('YOU LOST' , result_font, canvas, 410, cactus_top_rect.bottom + 50)
			break


		pygame.display.update()		
		clock.tick(fps)

	canvas.blit(endimage, endimagerect)
	pygame.display.update()
	waitforkey()
		

			




		




