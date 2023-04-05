import pygame,sys
from settings import *
from level import level
from game_data import level_0
from ui import UI

class Game:
    def __init__(self):
      
      # game attributes
        self.max_level = 2
        self.max_health = 100
        self.cur_health = 100
        self.coins = 0

        # audio
        self.level_bg_music = pygame.mixer.Sound('./assets/sfx/audio/level_music.wav')
        self.overworld_bg_music = pygame.mixer.Sound('./assets/sfx/audio/overworld_music.wav')

        # level creation
        self.level = level(level_0,screen,self.change_coins,self.change_health)
        self.status = 'level'
        self.level_bg_music.play(loops = -1)


        # ui
        self.ui = UI(screen)

        # change coins
    def change_coins(self,amount):
        self.coins += amount
        
        # change health
    def change_health(self,amount):
        self.cur_health += amount
        
    def check_game_over(self):
        if self.cur_health <= 0:
            self.cur_health = 100
            self.coins = 0
            self.max_level = 0
            self.level = level(level_0,screen)
            self.level_bg_music.stop()
            self.overworld_bg_music.play(loops = -1)
    
    def run(self):
        if self.status == 'level':
            self.level.run()
        else:
            self.level.run()
            self.ui.show_health(self.cur_health,self.max_health)
            self.ui.show_coins(self.coins)
            self.check_game_over()
   


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
# create game
game=Game()

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
    game.run()    
    # update
    pygame.display.update()
    clock.tick(fps)
