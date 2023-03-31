import pygame
from support import import_folder
# player particle,animation, and movement
class Player(pygame.sprite.Sprite):
    def __init__(self,pos,surface,create_jump_particles):
        super().__init__()
        self.character_assets()# Load the character assets
        self.frame_index=0 # The current frame of the animation
        self.animation_speed=0.12 # The speed of the animation
        self.image=self.animations['idle'][self.frame_index] 
        self.rect=self.image.get_rect(topleft=pos)#Top left = were player spawns
        # Dust particles ---------------------------------------------
        self.import_dust_run_particles()# Import the dust run particles
        self.dust_frame_index=0
        self.dust_animation_speed=0.12
        self.display_surface=surface# The surface to display the dust particles on
        self.create_jump_particles=create_jump_particles# Create the jump particles
        # Player attributes/movement----------------------------------
        self.direction= pygame.math.Vector2(0,0)# Direction the player is moving(vector)
        self.speed=5 # Speed of the player
        self.gravity=0.7 # Gravity of the player
        self.jump_speed=-15# Is the player jumping
        # Player status-----------------------------------------------
        self.status='idle' # The current status of the player
        self.facing_right=True # Is the player facing right
        self.on_ground=False # Is the player on the ground
        self.on_ceiling=False # Is the player on the ceiling
        self.on_left=False # Is the player on the left
        self.on_right=False # Is the player on the right
        self.attack=False # Is the player attacking
    #path
    def import_dust_run_particles(self):# Import the dust run particles
        self.dust_run_particles=import_folder('./assets/art/graphics/character/dust_particles/run')# Import the dust run particles    
    #path
    def character_assets(self):# Load the character assets
        character_path='./assets/art/graphics/character/'# Character path
        self.animations={'idle':[],'run':[],'jump':[],'fall':[],'attack':[]}# Create a dictionary for the animations
        # Loop through the animations
        for animation in self.animations.keys():# Loop through the animations
            full_path= character_path+ animation# Full path
            self.animations[animation]=import_folder(full_path)# Load the animation
    # animation
    def animate(self):# Animate method
        animation=self.animations[self.status]
        #loop over the frame_index
        self.frame_index+=self.animation_speed
        if self.frame_index>=len(animation):
            self.frame_index=0
        # Set the image 
        image=animation[int(self.frame_index)]# Set the image to the current frame of the animation/note: int is used as self.frame_index is a float
        if self.facing_right:
            self.image=image
        else:                                      #x   #y
            flipped_img=pygame.transform.flip(image,True,False)# Flip the image
            self.image=flipped_img# Set the image to the flipped image
        # set the rect
        if self.on_ground and self.on_right:
            self.rect=self.image.get_rect(bottomright=self.rect.bottomright)# Set the rect to the bottom right of the image
        elif self.on_ground and self.on_left:
            self.rect=self.image.get_rect(bottomleft=self.rect.bottomleft)# Set the rect to the bottom left of the image
        elif self.on_ground:
            self.rect=self.image.get_rect(midbottom=self.rect.midbottom)# Set the rect to the midbottom of the image
        elif self.on_ceiling and self.on_right:
            self.rect=self.image.get_rect(topright=self.rect.topright)# Set the rect to the topright of the image
        elif self.on_ceiling and self.on_left:
            self.rect=self.image.get_rect(topleft=self.rect.topleft)# Set the rect to the topleft of the image
        elif self.on_ceiling:
            self.rect=self.image.get_rect(midtop=self.rect.midtop) # Set the rect to the midtop of the image       
    # Run particle animation
    def run_dust_animation(self):# Run the dust animation
        if self.status=='run' and self.on_ground:# Not necessary to put self.on_ground as the player can't run in the air but it won't hurt
            self.dust_frame_index+=self.dust_animation_speed
            if self.dust_frame_index>=len(self.dust_run_particles):
                self.dust_frame_index=0
            # Set the dust particle
            dust_particle=self.dust_run_particles[int(self.dust_frame_index)]# Set the dust particle to the current frame of the animation/note: int is used as self.frame_index is a float
            if self.facing_right:
                pos= self.rect.bottomleft - pygame.math.Vector2(7,9)# Set the position of the dust particle to the bottom left of the player
                self.display_surface.blit(dust_particle,pos)
            else:
                pos= self.rect.bottomright - pygame.math.Vector2(7,9)# Set the position of the dust particle to the bottom right of the player
                flipped_dust_particle=pygame.transform.flip(dust_particle,True,False)# Flip the dust particle
                self.display_surface.blit(flipped_dust_particle,pos)
    # Get input method
    def get_input(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:# If the left key is pressed
          self.direction.x=-1
          self.facing_right=False
        elif keys[pygame.K_RIGHT]:# If the right key is pressed
            self.direction.x=1
            self.facing_right=True
        else:
            self.direction.x=0
        if keys[pygame.K_SPACE] and self.on_ground:# If the space key is pressed
            self.jump()
            self.create_jump_particles(self.rect.midbottom)# Create the jump particles  
    # status method, identifies the status of the player(idle,run,jump,fall)
    def get_status(self):
        if self.direction.y<0:
            self.status= 'jump'
        elif self.direction.y>1:# Not zero as it will mess up the animation(greater than gravity)
            self.status= 'fall'
        elif self.direction.x!=0:
            self.status= 'run'
        else:
            self.status= 'idle'
    # Apply gravity method
    def apply_gravity(self):
        self.direction.y+=self.gravity# Add gravity to the player
        self.rect.y+=self.direction.y# Move the player down by the gravity amount   
    # Jump method
    def jump(self):
        self.direction.y=self.jump_speed# Set the direction.y to the jump speed       
    # Update method
    def update(self):
        # Update the player
        self.get_input() # Get input method
        self.get_status() # Get status method
        self.animate()
        self.run_dust_animation()
        