import pygame,sys
from settings import *
from world_tile import tile

# pygame setup
pygame.init()
width=1200
height=600
fps=60
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("TerraBlock")
clock=pygame.time.Clock()
test_tile= pygame.sprite.Group(tile((100,100),200))

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
    test_tile.draw(screen)
    # update
    pygame.display.update()
    clock.tick(fps)
