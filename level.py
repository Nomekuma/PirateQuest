import pygame
from world_tile import tile
from settings import tile_size
from player import Player

class level(): # No need to inherit from pygame.sprite.Sprite/But we need __init__ method
    def __init__(self,level_data,surface):
        # Level setup
        self.display_surface=surface
        #self.level_data=level_data # No need set in seperate attribute
        self.setup_level(level_data)
        self.whorld_shift=0 # The amount of pixels the player moves

    
    def setup_level(self,layout):
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

                
            
     
    #  Run method
    def run(self):  
        # level tiles
        self.tiles.update(self.whorld_shift)# x_shift is the amount of pixels the player moves
        self.tiles.draw(self.display_surface)# Draw the tiles


        # player
        self.player.update()# Update the player
        self.player.draw(self.display_surface) # Draw the player

        

        