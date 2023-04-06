import pygame, sys
from settings import * 
from level import Level
from overworld import Overworld
from ui import UI
from save import SaveGame
# Note you will have to put your name on terminal first then the game will start
class Game:
	def __init__(self):
		self.player_name=None
		self.player_id=None

		# game attributes
		self.max_level = 0
		self.max_health = 100
		self.cur_health = 100
		self.coins = 0
		
		# audio 
		self.level_bg_music = pygame.mixer.Sound('./assets/sfx/audio/level_music.wav')
		self.overworld_bg_music = pygame.mixer.Sound('./assets/sfx/audio/overworld_music.wav')

		# overworld creation
		self.overworld = Overworld(0,self.max_level,screen,self.create_level)
		self.status = 'overworld'
		self.overworld_bg_music.play(loops = -1)

		# user interface 
		self.ui = UI(screen)
	def get_player_name(self):
		
		while not self.player_name:
			name = input("Enter your name: ")
			if name:
				self.player_name = name


	def create_level(self,current_level):
		self.level = Level(current_level,screen,self.create_overworld,self.change_coins,self.change_health)
		self.status = 'level'
		self.overworld_bg_music.stop()
		self.level_bg_music.play(loops = -1)

	def create_overworld(self,current_level,new_max_level):
		if new_max_level > self.max_level:
			self.max_level = new_max_level
		self.overworld = Overworld(current_level,self.max_level,screen,self.create_level)
		self.status = 'overworld'
		self.overworld_bg_music.play(loops = -1)
		self.level_bg_music.stop()

	def change_coins(self,amount):
		self.coins += amount

	def change_health(self,amount):
		self.cur_health += amount

	def check_game_over(self):
		if self.cur_health <= 0:
			self.cur_health = 100
			self.coins = 0
			self.max_level = 0
			self.overworld = Overworld(0,self.max_level,screen,self.create_level)
			self.status = 'overworld'
			self.level_bg_music.stop()
			self.overworld_bg_music.play(loops = -1)

	def run(self):
		self.get_player_name()
		if self.status == 'overworld':
			self.overworld.run()
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
while True:
	# event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			SaveGame().save(game.max_level,game.max_health,game.cur_health,game.coins,game.player_name,game.player_id)
			pygame.quit()
			sys.exit()
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_ESCAPE:
				SaveGame().save(game.max_level,game.max_health,game.cur_health,game.coins,game.player_name,game.player_id)
				pygame.quit()
				sys.exit()
            
	
	screen.fill('black')
	game.run()

	pygame.display.update()
	clock.tick(fps)
