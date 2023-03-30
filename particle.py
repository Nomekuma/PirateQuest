import pygame
from support import import_folder
# particle effect, dust particles
class ParticleEffect(pygame.sprite.Sprite):# Create a class for the particle effect
    def __init__(self,pos,type):
        super().__init__()
        self.frame_index=0
        self.animation_speed=0.6
        if type=='jump':
            self.frames=import_folder('./assets/art/graphics/character/dust_particles/jump')# Import the dust run particles
        if type=='land':
            self.frames=import_folder('./assets/art/graphics/character/dust_particles/land')# Import the dust run particles
        self.image=self.frames[self.frame_index]
        self.rect=self.image.get_rect(center=pos)
           
    def animate(self):
        self.frame_index+=self.animation_speed
        if self.frame_index>=len(self.frames):
            self.kill()# destroy the particle effect/Sprite
        else:
            self.image=self.frames[int(self.frame_index)]
        
    def update(self,x_shift):
        self.animate()
        self.rect.x+=x_shift