import pygame,sys
from settings import *
from level import level


# pygame setup
pygame.init()

#Screen Size
width=1200
height=550

# game fps/frames per second
fps=60

# create screen
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("TerraBlock")
clock=pygame.time.Clock()
level = level(level_map,screen)

# colors
black=(0,0,0)
# game loop
while True:
    # event loop
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    # draw
    screen.fill(black)
    level.run()
    
    # update
    pygame.display.update()
    clock.tick(fps)
