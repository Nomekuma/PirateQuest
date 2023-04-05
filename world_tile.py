import pygame 
from support import import_folder
# animation, static, and animated tiles
class tile(pygame.sprite.Sprite):
	def __init__(self,size,x,y):
		super().__init__()
		self.image = pygame.Surface((size,size))#x,y
		#self.image.fill(('grey'))# did not know you could do this
		self.rect = self.image.get_rect(topleft = (x,y))#Top left = were player spawns
    # Update method
	def update(self,shift):#x_shift is the amount of pixels the player moves
		self.rect.x += shift# move the tile with the player
# Static tile
class Statictile(tile):
	def __init__(self,size,x,y,surface):
		super().__init__(size,x,y)
		self.image = surface 
# crate tile are static tiles
class Crate(Statictile):
	def __init__(self,size,x,y):
		super().__init__(size,x,y,pygame.image.load('./assets/art/graphics/terrain/crate.png').convert_alpha())
		offset_y = y + size
		self.rect = self.image.get_rect(bottomleft = (x,offset_y))
# Animated tile
class Animatedtile(tile):
	def __init__(self,size,x,y,path):
		super().__init__(size,x,y)
		self.frames = import_folder(path)
		self.frame_index = 0
		self.image = self.frames[self.frame_index]

	def animate(self):
		self.frame_index += 0.15
		if self.frame_index >= len(self.frames):
			self.frame_index = 0
		self.image = self.frames[int(self.frame_index)]

	def update(self,shift):
		self.animate()
		self.rect.x += shift
# coin tile are animated tiles
class Coin(Animatedtile):
	def __init__(self,size,x,y,path,value):
		super().__init__(size,x,y,path)
		center_x = x + int(size / 2)
		center_y = y + int(size / 2)
		self.rect = self.image.get_rect(center = (center_x,center_y))
		self.value = value
# palm tile are animated tiles
class Palm(Animatedtile):
	def __init__(self,size,x,y,path,offset):
		super().__init__(size,x,y,path)
		offset_y = y - offset
		self.rect.topleft = (x,offset_y)