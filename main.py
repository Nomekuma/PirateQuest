import pygame,sys

# pygame setup
pygame.init()
width=1200
height=600
fps=60
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("TerraBlock")
clock=pygame.time.Clock()

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
    # update
    pygame.display.update()
    clock.tick(fps)
