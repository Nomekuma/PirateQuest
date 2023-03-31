from os import walk # Import walk method from os module
from csv import reader
from settings import tile_size

import pygame
# path of image folder
def import_folder(path):# Import folder method
	surface_list=[]# Create a list to hold the surfaces

	for _,__,image_files in walk(path):# Loop through the walk method
		for image in image_files:
			full_path = path + '/' + image
			image_surf = pygame.image.load(full_path).convert_alpha()# Load the image
			surface_list.append(image_surf)
			   #     for info in walk(path):# Loop through the walk method
#         print(info)# Print the info
#         loop over the info
# import_folder('./assets/art/graphics/character/run')# Call the import_folder method

	return surface_list
# import_folder('./assets/art/graphics/character/run')# Call the import_folder method
def import_csv_layout(path):# Import the csv layout
	terrain_map = []
	with open(path) as map:
		level = reader(map,delimiter = ',')# Read the map
		for row in level:
			terrain_map.append(list(row))
		return terrain_map
# import_csv_layout('./assets/art/level/level_0.csv')# Call the import_csv_layout method
def import_cut_graphics(path):
	surface = pygame.image.load(path).convert_alpha()# Load the image
	tile_num_x = int(surface.get_size()[0] / tile_size)
	tile_num_y = int(surface.get_size()[1] / tile_size)

	cut_tiles = []
	for row in range(tile_num_y):
		for col in range(tile_num_x):
			x = col * tile_size
			y = row * tile_size
			new_surf = pygame.Surface((tile_size,tile_size),flags = pygame.SRCALPHA)
			new_surf.blit(surface,(0,0),pygame.Rect(x,y,tile_size,tile_size))
			cut_tiles.append(new_surf)

	return cut_tiles
# import_cut_graphics('./assets/art/graphics/tiles/tiles.png')# Call the import_cut_graphics method