import pygame
from pytmx.util_pygame import load_pygame
from os.path import join

from constants import *
from groups import AllSprites
from player import Player
from sprites import *

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

    # setup
    self.setup()

  def setup(self):
    game_map = load_pygame(join("data", "maps", "map.tmx"))

    for x, y, image in game_map.get_layer_by_name("Ground").tiles():
      Sprite((x * TILE_SIZE, y * TILE_SIZE), image, self.all_sprites)

    for obj in game_map.get_layer_by_name('Objects'):
      CollisionSprite((obj.x, obj.y), pygame.Surface((obj.width, obj.height)), self.collision_sprites)

    for obj in game_map.get_layer_by_name("Entities"):
      if obj.name == "Player":
        self.player = Player((obj.x, obj.y), self.all_sprites, self.collision_sprites)

  def run(self):
    while self.running:
      dt = self.clock.tick() / 1000

      # Event loop
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False

      # draw
      self.all_sprites.update(dt)
      self.all_sprites.draw(self.player.rect.center)

      pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
  game = Game()
  game.run()
