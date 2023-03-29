import pygame
from menu import MenuButton


pygame.init()
# Window
Width, Height = 800, 600
win = pygame.display.set_mode((Width, Height))

# Caption
pygame.display.set_caption("TerraBlock")

# Icon
icon = pygame.image.load("./Terraria_lite/assets/art/icon.png")
pygame.display.set_icon(icon)

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        win.fill((0, 0, 0))
                

        pygame.display.update()

__name__ == "__main__" 
main()



