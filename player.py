import pygame
from os import walk
from os.path import join


class Player(pygame.sprite.Sprite):
  def __init__(self, pos, groups, collision_sprites):
    super().__init__(groups)
    self.load_images()
    self.state, self.frame_index = "down", 0
    self.image = pygame.image.load(join("images", "player", "down", "0.png")).convert_alpha()
    self.rect = self.image.get_frect(center = pos)
    self.hitbox_rect = self.rect.inflate(-5, -20)
    self.collision_sprites = collision_sprites

    # movement
    self.direction = pygame.Vector2()
    self.speed = 500

  def load_images(self):
    self.frames = {"left": [], "right": [], "up": [], "down": []}

    for state in self.frames.keys():
      for folder_path, sub_folders, file_names in list(walk(join("images", "player", state))):
        if file_names:
          for file_name in sorted(file_names, key = lambda name: int(name.split(".")[0])):
            full_path = join(folder_path, file_name)
            surface = pygame.image.load(full_path).convert_alpha()
            self.frames[state].append(surface)

  def input(self):
    keys = pygame.key.get_pressed()
    self.direction.x = int(keys[pygame.K_RIGHT] or keys[pygame.K_d]) - int(keys[pygame.K_LEFT] or keys[pygame.K_a])
    self.direction.y = int(keys[pygame.K_DOWN] or keys[pygame.K_s]) - int(keys[pygame.K_UP] or keys[pygame.K_w])

    self.direction = self.direction and self.direction.normalize()

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

  def animate(self,dt):
      # get state
      if self.direction.x !=0:
        self.state = "right" if self.direction.x > 0 else "left"
      if self.direction.y !=0:
        self.state = 'down' if self.direction.y > 0 else "up"

      # animate
      self.frame_index +=  40 * dt if self.direction else 0
      self.image = self.frames[self.state][int(self.frame_index) % len(self.frames[self.state])]

  def update(self, dt):
    self.input()
    self.move(dt)
    self.animate(dt)


#     # Ensure unique integer positions
#     self.unique_positions = getattr(self, "unique_positions", set())

# # Convert position to integers
#     int_x = int(self.rect.topleft[0])
#     int_y = int(self.rect.topleft[1])

# # Store unique integer positions
#     if (int_x, int_y) not in self.unique_positions:
#         self.unique_positions.add((int_x, int_y))
#         print(f"New Unique Position: ({int_x}, {int_y})")




