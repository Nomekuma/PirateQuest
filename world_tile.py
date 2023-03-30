import pygame
# Tile settings, colors
class tile(pygame.sprite.Sprite):
    def __init__(self, pos,size):
        super().__init__()
        self.image=pygame.Surface((size,size))#x,y
        self.image.fill(('grey'))# did not know you could do this
        self.rect = self.image.get_rect(topleft=pos)#Top left = were player spawns
    # Update method
    def update(self,x_shift):#x_shift is the amount of pixels the player moves
        self.rect.x += x_shift # move the tile with the player
       