import pygame
from world_tile import tile
from settings import tile_size,width
from player import Player
from particle import ParticleEffect
# level,player,particles
class level(): # No need to inherit from pygame.sprite.Sprite/But we need __init__ method
    def __init__(self,level_data,surface):# level_data is the level map
        # Level setup
        self.display_surface=surface
        #self.level_data=level_data # No need set in seperate attribute
        self.setup_level(level_data)
        self.world_shift=0 # The amount of pixels the player moves
        self.current_x=0 # The current x position of the player
        # dust
        self.dust_sprite=pygame.sprite.GroupSingle()# Create a group of dust particles
        self.player_on_ground=False # Check if the player is on the ground
  
    def create_jump_particles(self,pos):
        if self.player.sprite.facing_right:
            pos -= pygame.math.Vector2(10,5)
        else:
            pos += pygame.math.Vector2(10,-5)
            
        jump_particle_sprite=ParticleEffect(pos,'jump')
        self.dust_sprite.add(jump_particle_sprite)

    def get_player_on_ground(self,):# Check if the player is on the ground
        if self.player.sprite.on_ground:
            self.player_on_ground=True
        else:
            self.player_on_ground=False

    def create_landing_dust(self):# Create dust particles when the player lands
        if not self.player_on_ground and self.player.sprite.on_ground and not self.dust_sprite.sprite:# If the player is on the ground
            if self.player.sprite.facing_right:
                offset=pygame.math.Vector2(10,15)# The offset of the dust particles
            else:
                offset=pygame.math.Vector2(-10,15)
            fall_dust_particles=ParticleEffect(self.player.sprite.rect.midbottom - offset,'land')# Create the dust particles
            self.dust_sprite.add(fall_dust_particles)# Add the dust particles to the dust sprite group

    def setup_level(self,layout):# layout is the level map
        self.tiles=pygame.sprite.Group() # Create a group of tiles
        self.player=pygame.sprite.GroupSingle()# Create a group of player

        for row_index,row in enumerate(layout):
             #print(row) # Print each row(from level_map)./see settings.py
            # print(row_index) # Print the index of each row./see settings.py
     
            for col_index,cell in enumerate(row):
                x=col_index*tile_size# x is relative to the column index
                y=row_index*tile_size# y is relative to the row index
                
                # print(f'row:{row_index},col:{col_index},cell:{cell}') # Print the index of each row./see settings.py
                
                if cell == 'X':# If the cell is an X(Tiles)
                    Tile = tile((x,y),tile_size)
                    self.tiles.add(Tile)
                
                if cell == 'P':# If the cell is an P(Player)
                    player_sprite=Player((x,y),self.display_surface,self.create_jump_particles)
                    self.player.add(player_sprite)

    def scroll_x(self):# Scroll the level in the x direction
        player=self.player.sprite
        player_x=player.rect.centerx
        direction_x=player.direction.x    
         
        # Scroll the level in the x direction
        # if player_x <200 and direction_x<0:# If the player is less than 200 pixels from the left side of the screen
        if player_x <width*0.75 and direction_x<0:
            self.world_shift=5
            player.speed=0    
        # elif player_x >400 and direction_x>0:# If the player is more than 400 pixels from the left side of the screen
        elif player_x >width - (width*0.75) and direction_x>0:   
            self.world_shift=-5
            player.speed=0
        else:
            self.world_shift=0
            player.speed=5
      
    def horizontal_movement_collision(self):# Check for collision with the level tiles
        player=self.player.sprite
        player.rect.x += player.direction.x * player.speed # Move the player 5 pixels to the left/right
        # Check for collision with the level tiles
        for sprite in self.tiles.sprites():# Loop through all the tiles
            if sprite.rect.colliderect(player.rect):# If the player collides with a tile
                if player.direction.x < 0:# If the player is moving left
                    player.rect.left = sprite.rect.right
                    player.on_left=True
                    self.current_x=player.rect.left
                elif player.direction.x > 0: # If the player is moving right
                    player.rect.right = sprite.rect.left 
                    player.on_right=True
                    self.current_x=player.rect.right# The current x position of the player

        if player.on_right and (player.rect.right>self.current_x or player.direction.x <=0):# If the player is on the right side of the tile
            player.on_right=False
        if player.on_left and (player.rect.left<self.current_x or player.direction.x >=0):
            player.on_left=False
        
    def vertical_movement_collision(self):# Check for collision with the level tiles vertically
        player=self.player.sprite
        player.apply_gravity() # Apply gravity method # Move the player 5 pixels up/down
        # Check for collision with the level tiles
        for sprite in self.tiles.sprites():# Loop through all the tiles
            if sprite.rect.colliderect(player.rect):# If the player collides with a tile
                if player.direction.y > 0:# If the player is moving down
                   player.rect.bottom = sprite.rect.top# Move the player to the top of the tile
                   player.direction.y = 0 # Stop the player from moving down
                   player.on_ground = True # The player is on the ground

                elif player.direction.y < 0:# If the player is moving up
                    player.rect.top = sprite.rect.bottom # Move the player to the bottom of the tile
                    player.direction.y = 0 # Stop the player from moving up
                    player.on_ceiling = True # The player is on the ceiling
        # Check if the player is on the ground or falling
        if player.on_ground and player.direction.y <0 or player.direction.y >1:
            player.on_ground=False
        # Check if the player is on the ceiling or falling
        if player.on_ceiling and player.direction.y >0:
            player.on_ceiling=False
   #  Run method
    def run(self): 
        
        # dust_particles
        self.dust_sprite.update(self.world_shift)# Update the dust particles
        self.dust_sprite.draw(self.display_surface)# Draw the dust particles
 
        # level tiles
        self.tiles.update(self.world_shift)# x_shift is the amount of pixels the player moves
        self.tiles.draw(self.display_surface)# Draw the tiles
        self.scroll_x()# Scroll the level in the x direction

        # player
        self.player.update()# Update the player
        self.horizontal_movement_collision()# Check for collision with the level tiles
        self.get_player_on_ground()# Check if the player is on the ground
        self.vertical_movement_collision()# Check for collision with the level tiles
        self.create_landing_dust()# Create dust particles when the player lands
        self.player.draw(self.display_surface) # Draw the player

        

        