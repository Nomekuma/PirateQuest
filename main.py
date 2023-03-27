import pygame
fps=60
WIDTH,HEIGHT=800,600
icon = pygame.image.load("assets/icon.png")
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("TerraBlock")
pygame.display.set_icon(icon)

def main():
    run = True
    while run:
        for event in pygame.event.get():
            clock = pygame.time.Clock()
            clock.tick(fps)
            if event.type == pygame.QUIT:
                run = False
                quit()

    pygame.quit()
            
if __name__ == "__main__":
    main()