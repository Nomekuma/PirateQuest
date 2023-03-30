from os import walk # Import walk method from os module
import pygame
# path of image folder
def import_folder(path):# Import folder method
    surface_list=[]# Create a list to hold the surfaces
#---------------------------------------------------------------------------------------------------
    for _,__,img_files in walk(path):# Loop through the walk method
        for img in img_files:# Loop through the image files
            full_path=path+'/'+img# Create the full path
            image_surface=pygame.image.load(full_path).convert_alpha()# Load the image
            surface_list.append(image_surface)# Append the image to the list
#---------------------------------------------------------------------------------------------------      
    return surface_list# Return the list

        #     for info in walk(path):# Loop through the walk method
#         print(info)# Print the info
#         loop over the info
# import_folder('./assets/art/graphics/character/run')# Call the import_folder method