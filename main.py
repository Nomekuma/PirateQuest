import pygame,sys

# pygame setup
pygame.init()
Width=1200
Height=600
fps=60
screen=pygame.display.set_mode((Width,Height))
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
