import pygame,sys
from settings import *
from level import level
from game_data import level_0
# pygame setup
pygame.init()
#Screen Size
width=1280
height=720
# game fps/frames per second
fps=60
# create screen
screen=pygame.display.set_mode((width,height))
# set caption
pygame.display.set_caption("TerraBlock")
icon=pygame.image.load('./assets/art/graphics/icon/icon.png')
pygame.display.set_icon(icon)
# create clock
clock=pygame.time.Clock()
Level = level(level_0,screen)
# colors
black=(0,0,0)
# game loop
while True:
    # event loop
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    # draw
    screen.fill(black)
    Level.run()    
    # update
    pygame.display.update()
    clock.tick(fps)
