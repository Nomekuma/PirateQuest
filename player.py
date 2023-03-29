import pygame


# Create a class for the player
class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image=pygame.Surface((20,50)) #20 pixels wide, 50 pixels tall
        self.image.fill(('red'))# Player-Example-red
        self.rect=self.image.get_rect(topleft=pos)#Top left = were player spawns
        
        # Player attributes/movement
        self.direction= pygame.math.Vector2(0,0)# Direction the player is moving(vector)
        self.speed=5 # Speed of the player
        self.gravity=0.5 # Gravity of the player
        self.jump_speed=-5 # Is the player jumping


    # Get input method
    def get_input(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:# If the left key is pressed
          self.direction.x=-1
        elif keys[pygame.K_RIGHT]:# If the right key is pressed
            self.direction.x=1
        else:
            self.direction.x=0
        if keys[pygame.K_SPACE]:# If the space key is pressed
            self.jump()
    # Apply gravity method
    def apply_gravity(self):
        self.direction.y+=self.gravity# Add gravity to the player
        self.rect.y+=self.direction.y# Move the player down by the gravity amount
    
    # Jump method
    def jump(self):
        self.direction.y=self.jump_speed# Set the direction.y to the jump speed
        

    
    # Update method
    def update(self):
        self.get_input() # Get input method
        