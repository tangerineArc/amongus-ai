import pygame
from os import walk
from os.path import join
import random

class Bot(pygame.sprite.Sprite):

  def __init__(self, pos, groups, collision_sprites, bot_type="random"):
    super().__init__(groups)
    self.load_images()
    self.state, self.frame_index = "down", 0
    self.image = pygame.image.load(join("images", "bots", "bot1", "down", "0.png")).convert_alpha()
    self.rect = self.image.get_frect(center=pos)
    self.hitbox_rect = self.rect.inflate(-5, -20)
    self.collision_sprites = collision_sprites

        # Movement
    self.direction = pygame.Vector2()
    self.speed = 300  # Bots move slightly slower than the player
    self.bot_type = bot_type  # Movement behavior type
    self.target = None  # Target position for goal-seeking behavior
      
  def load_images(self):
      self.frames = {"left": [], "right": [], "up": [], "down": []}
      
      for state in self.frames.keys():
        for folder_path, sub_folders, file_names in list(walk(join("images", "bots","bot1", state))):
            if file_names:
                for file_name in sorted(file_names, key = lambda name: int(name.split(".")[0])):
                    full_path = join(folder_path, file_name)
                    surface = pygame.image.load(full_path).convert_alpha()
                    self.frames[state].append(surface)

  def move_algorithm(self):
      if self.bot_type == "random":
          if random.randint(1, 100) > 98:  # Random direction change
              self.direction.x = random.choice([-1, 0, 1])
              self.direction.y = random.choice([-1, 0, 1])
              self.direction = self.direction and self.direction.normalize()
      elif self.bot_type == "goal_seeking" and self.target:
          target_vector = pygame.Vector2(self.target) - pygame.Vector2(self.rect.center)
          if target_vector.length() > 1:
              self.direction = target_vector.normalize()
          else:
              self.direction = pygame.Vector2(0, 0)  # Stop when reaching the goal

  def move(self, dt):
      self.hitbox_rect.x += self.direction.x * self.speed * dt
      self.collision("horizontal")
      
      self.hitbox_rect.y += self.direction.y * self.speed * dt
      self.collision("vertical")
      
      self.rect.center = self.hitbox_rect.center

  def collision(self, direction):
      for sprite in self.collision_sprites:
          if sprite.rect.colliderect(self.hitbox_rect):
              if direction == "horizontal":
                  if self.direction.x > 0:
                      self.hitbox_rect.right = sprite.rect.left
                  if self.direction.x < 0:
                      self.hitbox_rect.left = sprite.rect.right
              else:
                  if self.direction.y < 0:
                      self.hitbox_rect.top = sprite.rect.bottom
                  if self.direction.y > 0:
                      self.hitbox_rect.bottom = sprite.rect.top
              self.direction = pygame.Vector2(0, 0)  # Stop when colliding

  def animate(self, dt):
      if self.direction.x != 0:
          self.state = "right" if self.direction.x > 0 else "left"
      if self.direction.y != 0:
          self.state = "down" if self.direction.y > 0 else "up"
      
      self.frame_index += 10 * dt if self.direction else 0
      self.image = self.frames[self.state][int(self.frame_index) % len(self.frames[self.state])]

  def update(self, dt):
      self.move_algorithm()
      self.move(dt)
      self.animate(dt)