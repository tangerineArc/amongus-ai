import pygame

from pytmx.util_pygame import load_pygame
from os.path import join
from constants import *
from groups import AllSprites

from sprites import *

from player import *

from WELCOME import welcome

#from global_knowledge import *
import time

class Game:
  def __init__(self):
    pygame.init()
    self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Survivor")
    self.clock = pygame.time.Clock()
    self.running = True

    # groups

    self.all_sprites = AllSprites()
    self.collision_sprites = pygame.sprite.Group()
    self.spawn_pos = []
    self.surface_dim = []
    # setup
    self.setup()
    # self.player=0

  def setup(self):
    k = 0
    count = 0
    game_map = load_pygame(join("data", "maps", "map.tmx"))
    for x, y, image in game_map.get_layer_by_name("Ground").tiles():
        Sprite((x * TILE_SIZE, y * TILE_SIZE), image, self.all_sprites)

    for obj in game_map.get_layer_by_name("Objects"):
        CollisionSprite((obj.x, obj.y), pygame.Surface((obj.width, obj.height)), self.collision_sprites)

    for obj in game_map.get_layer_by_name("Entities"):
        if obj.name == "Player":
            self.player = Player((obj.x, obj.y), self.all_sprites, self.collision_sprites)
        elif obj.name == "Bot":
            self.spawn_pos.append((obj.x, obj.y))
            self.surface_dim.append((obj.width , obj.height))
            count += 1
            if count == player:  # ✅ Limit bots to player count
                break

    # ✅ Convert set to list for indexing
    unique_colors = list(listc)
    for i, (x, y) in enumerate(self.spawn_pos):
        if (i < len(unique_colors)) :  # ✅ Prevents IndexError
            bot = Bot((x, y),  self.all_sprites, self.collision_sprites, unique_colors[i],i,all_tasks)
        

  def run(self):
    while self.running:
        dt = self.clock.tick(40) / 1000  # Frame time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        # Update all sprites4
        
        self.all_sprites.update(dt)
        #self.imposter_sprites.update(dt)
        #self.bot_sprites.update(dt)
        # Clear screen
        self.display_surface.fill((30, 30, 30))

        # Draw game objects (with camera movement)
        self.all_sprites.draw(self.player.rect.center)
        #self.bot_sprites.draw(self.display_surface) 

        pygame.display.update()

    pygame.quit()



if __name__ == "__main__":

  pygame.font.init()

  color,player=welcome()
  print(color)
  # print(player)

  # Game window setup
  display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
  font = pygame.font.Font(None, 36)  # Set up a font for displaying text

  #now check the colors i can take 

  #print(color)
  #print(player)

  colors=["Black","Brown","Pink","White", "Blue", "Green", "Yellow", "Purple", "Orange"]

  listc=set()

  for col in colors:
    if(len(listc)==player):
      break
    if(col!=colors[color-1]):
      listc.add(col)
  
  unique_colors = list(listc)
  
  print(len(listc))
  #for h in listc:
   # print(h)
  #now i have the color and number of players selection

  #game_start_time = time.time()  # Store when the game starts

  game=Game()  

  # if(got_killed){
  #    #call sus.py
  #    #make appropriate changes 
  #    #game=Game()
  # }
  game.run()




  

    
