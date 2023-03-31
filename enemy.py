import pygame 
from world_tile import Animatedtile
from random import randint

class Enemy(Animatedtile):
	def __init__(self,size,x,y):
		super().__init__(size,x,y,'./assets/art/graphics/enemy/run')
		self.rect.y += size - self.image.get_size()[1]
		self.speed = randint(1,4)# Random speed
    # move enemy
	def move(self):
		self.rect.x += self.speed
    # reverse enemy
	def reverse_image(self):
		if self.speed > 0:
			self.image = pygame.transform.flip(self.image,True,False)
    # reverse enemy direction
	def reverse(self):
		self.speed *= -1
    # update enemy
	def update(self,shift):
		self.rect.x += shift
		self.animate()
		self.move()
		self.reverse_image()