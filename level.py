import pygame
from world_tile import tile
from settings import tile_size,width
from player import Player

class level(): # No need to inherit from pygame.sprite.Sprite/But we need __init__ method
    def __init__(self,level_data,surface):# level_data is the level map
        # Level setup
        self.display_surface=surface
        #self.level_data=level_data # No need set in seperate attribute
        self.setup_level(level_data)
        self.whorld_shift=0 # The amount of pixels the player moves

    
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
                    player_sprite=Player((x,y))
                    self.player.add(player_sprite)

    def horizontal_movement_collision(self):
        player=self.player.sprite
        player.rect.x += player.direction.x * player.speed # Move the player 5 pixels to the left/right
        # Check for collision with the level tiles
        for sprite in self.tiles.sprites():# Loop through all the tiles
            if sprite.rect.colliderect(player.rect):# If the player collides with a tile
                if player.direction.x > 0:# If the player is moving right
                    player.rect.right = sprite.rect.left# Move the player to the left of the tile
                elif player.direction.x < 0: # If the player is moving left
                    player.rect.left = sprite.rect.right # Move the player to the right of the tile

    def vertical_movement_collision(self):
        player=self.player.sprite
        player.apply_gravity() # Apply gravity method # Move the player 5 pixels up/down
        # Check for collision with the level tiles
        for sprite in self.tiles.sprites():# Loop through all the tiles
            if player.rect.colliderect(sprite.rect):# If the player collides with a tile
                if player.direction.y > 0:# If the player is moving down
                    player.rect.bottom = sprite.rect.top# Move the player to the top of the tile
                    player.direction.y = 0 # Stop the player from moving down
                elif player.direction.y < 0:# If the player is moving up
                    player.rect.top = sprite.rect.bottom # Move the player to the bottom of the tile
                    player.direction.y = 0 # Stop the player from moving up


    def scroll_x(self):# Scroll the level in the x direction
        player=self.player.sprite
        player_x=player.rect.centerx
        direction_x=player.direction.x    
         
        # Scroll the level in the x direction
        # if player_x <200 and direction_x<0:# If the player is less than 200 pixels from the left side of the screen
        if player_x <width*0.75 and direction_x<0:
            self.whorld_shift=5
            player.speed=0    
        # elif player_x >400 and direction_x>0:# If the player is more than 400 pixels from the left side of the screen
        elif player_x >width - (width*0.75) and direction_x>0:   
            self.whorld_shift=-5
            player.speed=0
        else:
            self.whorld_shift=0
            player.speed=5
            
     
    #  Run method
    def run(self):  
        # level tiles
        self.tiles.update(self.whorld_shift)# x_shift is the amount of pixels the player moves
        self.tiles.draw(self.display_surface)# Draw the tiles
        self.scroll_x()# Scroll the level in the x direction


        # player
        self.player.update()# Update the player
        self.horizontal_movement_collision()# Check for collision with the level tiles
        self.vertical_movement_collision()# Check for collision with the level tiles
        self.player.draw(self.display_surface) # Draw the player

        

        