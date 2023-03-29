import pygame


# Create a class for the player
class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image=pygame.Surface((20,50)) #20 pixels wide, 50 pixels tall
        self.image.fill(('red'))# Player-Example-red
        self.rect=self.image.get_rect(topleft=pos)#Top left = were player spawns
        self.direction= pygame.math.Vector2(0,0)# Direction the player is moving(vector)


    # Get input method
    def get_input(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
          self.direction.x=-1
        elif keys[pygame.K_RIGHT]:
            self.direction.x=1
        else:
            self.direction.x=0

    # Update method
    def update(self):
        self.get_input() # Get input method
        self.rect.x += self.direction.x * 5 # Move the player 5 pixels to the left/right