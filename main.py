import pygame
from character import sprites
# screen size
WIDTH,HEIGHT=800,600

# game speed/frames per second
fps=60

#icon
icon = pygame.image.load("./assets/art/icon.png")

#background
bg = pygame.image.load("./assets/art/bg.png")
#------------------------------------------------#

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# set icon/displays icon
pygame.display.set_icon(icon)
# set display name
pygame.display.set_caption("TerraBlock")

# set background
def bg_1(bg):
    size=pygame.transform.scale(bg,(800,500))
    screen.blit(size,(0,0))


# main loop
def main():
    run=True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.fill((0,0,0))
        bg_1(bg)
        sprites.update()
        sprites.draw(screen)
        pygame.display.update()
    
    pygame.quit()
    
if __name__ == "__main__":
    main()    