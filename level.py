import pygame,sys
from world_tile import tile,Statictile,Crate,Coin,Palm
from settings import tile_size,width,height
from player import Player
from particle import ParticleEffect
from support import import_csv_layout,import_cut_graphics
from enemy import Enemy
from decoration import Sky,Water,Clouds
# level,player,particles
class level(): # No need to inherit from pygame.sprite.Sprite/But we need __init__ method
	def __init__(self,level_data,surface,change_coins,change_health):# level_data is the level map
		# general setup
		self.display_surface = surface
		#self.level_data=level_data # No need set in seperate attribute
		self.world_shift = 0 # The amount of pixels the player moves
		self.current_x = None # The current x position of the player

		# audio setup
		self.coin_sound = pygame.mixer.Sound('./assets/sfx/audio/effects/coin.wav')
		self.stomp_sound = pygame.mixer.Sound('./assets/sfx/audio/effects/stomp.wav')

		# player 
		player_layout = import_csv_layout(level_data['player'])
		self.player = pygame.sprite.GroupSingle()
		self.goal = pygame.sprite.GroupSingle()
		self.player_setup(player_layout)

		# user interface
		self.change_coins = change_coins

		# dust 
		self.dust_sprite = pygame.sprite.GroupSingle()
		self.player_on_ground = False

		# explosion particles
		self.explosion_sprite = pygame.sprite.GroupSingle()

		# terrain setup
		terrain_layout = import_csv_layout(level_data['terrain'])
		self.terrain_sprites = self.create_tile_group(terrain_layout,'terrain')

		# grass setup 
		grass_layout = import_csv_layout(level_data['grass'])
		self.grass_sprites = self.create_tile_group(grass_layout,'grass')

		# crates 
		crate_layout = import_csv_layout(level_data['crates'])
		self.crate_sprites = self.create_tile_group(crate_layout,'crates')

		# coins 
		coin_layout = import_csv_layout(level_data['coins'])
		self.coin_sprites = self.create_tile_group(coin_layout,'coins')

		# foreground palms 
		fg_palm_layout = import_csv_layout(level_data['fg_palms'])
		self.fg_palm_sprites = self.create_tile_group(fg_palm_layout,'fg palms')

		# background palms 
		bg_palm_layout = import_csv_layout(level_data['bg_palms'])
		self.bg_palm_sprites = self.create_tile_group(bg_palm_layout,'bg palms')

		# enemy 
		enemy_layout = import_csv_layout(level_data['enemies'])
		self.enemy_sprites = self.create_tile_group(enemy_layout,'enemies')

		# constraint 
		constraint_layout = import_csv_layout(level_data['constraints'])
		self.constraint_sprites = self.create_tile_group(constraint_layout,'constraint')

		# decoration 
		self.sky = Sky(8)
		level_width = len(terrain_layout[0]) * tile_size #  first row multiplied by tile size
		self.water = Water(height - 20,level_width)
		self.clouds = Clouds(400,level_width,30)
    # this is the function that creates the tile group
	def create_tile_group(self,layout,type):
		sprite_group = pygame.sprite.Group()
         #loop through the layout and create the tiles
		for row_index, row in enumerate(layout):
			for col_index,val in enumerate(row):
				if val != '-1':
					x = col_index * tile_size
					y = row_index * tile_size
                    # create the tile based on the type
					if type == 'terrain':
						terrain_tile_list = import_cut_graphics('./assets/art/graphics/terrain/terrain_tiles.png')
						tile_surface = terrain_tile_list[int(val)]
						sprite = Statictile(tile_size,x,y,tile_surface)
						
					if type == 'grass':
						grass_tile_list = import_cut_graphics('./assets/art/graphics/decoration/grass/grass.png')
						tile_surface = grass_tile_list[int(val)]
						sprite = Statictile(tile_size,x,y,tile_surface)
					
					if type == 'crates':
						sprite = Crate(tile_size,x,y)

					if type == 'coins':
						if val == '0': sprite = Coin(tile_size,x,y,'./assets/art/graphics/coins/gold')
						if val == '1': sprite = Coin(tile_size,x,y,'./assets/art/graphics/coins/silver')

					if type == 'fg palms':
						if val == '0': sprite = Palm(tile_size/2,x,y,'./assets/art/graphics/terrain/palm_small',32)
						if val == '1': sprite = Palm(tile_size-25,x,y,'./assets/art/graphics/terrain/palm_large',64)

					if type == 'bg palms':
						sprite = Palm(tile_size,x,y,'./assets/art/graphics/terrain/palm_bg',64)

					if type == 'enemies':
						sprite = Enemy(tile_size,x,y)

					if type == 'constraint':
						sprite = tile(tile_size,x,y)

					sprite_group.add(sprite)
		
		return sprite_group
    # player setup
	def player_setup(self,layout):
		for row_index, row in enumerate(layout):
			for col_index,val in enumerate(row):
				x = col_index * tile_size
				y = row_index * tile_size
				if val == '0':
					sprite = Player((x,y),self.display_surface,self.create_jump_particles)
					self.player.add(sprite)
				if val == '1':
					hat_surface = pygame.image.load('./assets/art/graphics/character/hat.png').convert_alpha()
					sprite = Statictile(tile_size,x,y,hat_surface)
					self.goal.add(sprite)
    # when enemy collides with constraint, reverse direction
	def enemy_collision_reverse(self):
		for enemy in self.enemy_sprites.sprites():
			if pygame.sprite.spritecollide(enemy,self.constraint_sprites,False):
				enemy.reverse()
    # jump particles
	def create_jump_particles(self,pos):
		if self.player.sprite.facing_right:
			pos -= pygame.math.Vector2(10,5)
		else:
			pos += pygame.math.Vector2(10,-5)
		jump_particle_sprite = ParticleEffect(pos,'jump')
		self.dust_sprite.add(jump_particle_sprite)
    # horizontal movement collision
	def horizontal_movement_collision(self):
		player = self.player.sprite
		player.rect.x += player.direction.x * player.speed
		collidable_sprites = self.terrain_sprites.sprites() + self.crate_sprites.sprites() + self.fg_palm_sprites.sprites()
		for sprite in collidable_sprites:
			if sprite.rect.colliderect(player.rect):
				if player.direction.x < 0: 
					player.rect.left = sprite.rect.right
					player.on_left = True
					self.current_x = player.rect.left
				elif player.direction.x > 0:
					player.rect.right = sprite.rect.left
					player.on_right = True
					self.current_x = player.rect.right

		if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
			player.on_left = False
		if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
			player.on_right = False
    # vertical movement collision
	def vertical_movement_collision(self):
		player = self.player.sprite
		player.apply_gravity()
		collidable_sprites = self.terrain_sprites.sprites() + self.crate_sprites.sprites() + self.fg_palm_sprites.sprites()

		for sprite in collidable_sprites:
			if sprite.rect.colliderect(player.rect):
				if player.direction.y > 0: 
					player.rect.bottom = sprite.rect.top
					player.direction.y = 0
					player.on_ground = True
				elif player.direction.y < 0:
					player.rect.top = sprite.rect.bottom
					player.direction.y = 0
					player.on_ceiling = True

		if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
			player.on_ground = False
		if player.on_ceiling and player.direction.y > 0.1:
			player.on_ceiling = False
    # scroll world
	def scroll_x(self):
		player = self.player.sprite
		player_x = player.rect.centerx
		direction_x = player.direction.x

		if player_x < width / 4 and direction_x < 0:
			self.world_shift = 8
			player.speed = 0
		elif player_x > width - (width / 4) and direction_x > 0:
			self.world_shift = -8
			player.speed = 0
		else:
			self.world_shift = 0
			player.speed = 7
    # When player hits the ground
	def get_player_on_ground(self):
		if self.player.sprite.on_ground:
			self.player_on_ground = True
		else:
			self.player_on_ground = False
    # create landing dust/Layer
	def create_landing_dust(self):
		if not self.player_on_ground and self.player.sprite.on_ground and not self.dust_sprite.sprites():
			if self.player.sprite.facing_right:
				offset = pygame.math.Vector2(10,15)
			else:
				offset = pygame.math.Vector2(-10,15)
			fall_dust_particle = ParticleEffect(self.player.sprite.rect.midbottom - offset,'land')
			self.dust_sprite.add(fall_dust_particle)
	# death
	def death(self):
		if self.player.sprite.rect.top > height:
			self.player.sprite.kill()
			sys.exit()
	def check_for_win(self):
		if pygame.sprite.spritecollide(self.player.sprite,self.goal,False):
			self.player.sprite.kill()
			sys.exit()
	def coin_collision(self):
		collided_coins=pygame.sprite.spritecollide(self.player.sprite,self.coin_sprites,True)
		if collided_coins:
			self.coin_sound.play()
			for coin in collided_coins:
				self.change_coins += coin.value
	
	def enemy_collision(self):
		enemy_collision = pygame.sprite.spritecollide(self.player.sprite,self.enemy_sprites,False)
		if enemy_collision:
			for enemy in enemy_collision:
				enemy_center=enemy.rect.center
				enemy_top=enemy.rect.top
				player_bottom=self.player.sprite.rect.bottom
				if enemy_top < player_bottom < enemy_center and self.player.sprite.direction.y > 0:
					self.stomp_sound.play()
					self.player.sprite.direction.y = -10
					explosive_sprite= ParticleEffect(enemy.rect.center,'explosion')
					self.explosive_sprite.add(explosive_sprite)
					enemy.kill()
				else:
					self.player.sprite.damage(1)

			

    # Run the game
	def run(self):
		# sky 
		self.sky.draw(self.display_surface)
		self.clouds.draw(self.display_surface,self.world_shift)
		
		# background palms
		self.bg_palm_sprites.update(self.world_shift)
		self.bg_palm_sprites.draw(self.display_surface) 

		# terrain 
		self.terrain_sprites.update(self.world_shift)
		self.terrain_sprites.draw(self.display_surface)
		
		# enemy 
		self.enemy_sprites.update(self.world_shift)
		self.constraint_sprites.update(self.world_shift)
		self.enemy_collision_reverse()
		self.enemy_sprites.draw(self.display_surface)

		# crate 
		self.crate_sprites.update(self.world_shift)
		self.crate_sprites.draw(self.display_surface)

		# grass
		self.grass_sprites.update(self.world_shift)
		self.grass_sprites.draw(self.display_surface)

		# coins 
		self.coin_sprites.update(self.world_shift)
		self.coin_sprites.draw(self.display_surface)

		# foreground palms
		self.fg_palm_sprites.update(self.world_shift)
		self.fg_palm_sprites.draw(self.display_surface)

		# dust particles 
		self.dust_sprite.update(self.world_shift)
		self.dust_sprite.draw(self.display_surface)

		# player sprites
		self.player.update()
		self.horizontal_movement_collision()
		# player collision
		self.get_player_on_ground()
		self.vertical_movement_collision()
		self.create_landing_dust()
		# camera scroll
		self.scroll_x()
		self.player.draw(self.display_surface)
		self.goal.update(self.world_shift)
		self.goal.draw(self.display_surface)
		# enemy collision
		self.enemy_collision()
		# coin collision
		self.coin_collision()
		# death
		self.death()
		# win
		self.check_for_win()
		# water 
		self.water.draw(self.display_surface,self.world_shift)