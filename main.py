import pygame
from character import sprites
WIDTH,HEIGHT=800,600
fps=60
icon = pygame.image.load("assets/art/icon.png")
bg = pygame.image.load("assets/art/bg.png")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


pygame.display.set_icon(icon)
pygame.display.set_caption("TerraBlock")

def bg_1(bg):
    size=pygame.transform.scale(bg,(800,500))
    screen.blit(size,(0,0))



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