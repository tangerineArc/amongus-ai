import pygame
from os import walk
from os.path import join
# from sprites import sp
# from constants import min_kill_distance
import csv
import math
from sprites import *
from constants import *
#from main import *
from global_knowledge import *


import time

from global_knowledge import *

unique_coordinates = set()

my_player_x=0
my_player_y=0

class Player(pygame.sprite.Sprite):
  def __init__(self, pos, groups, collision_sprites):
    super().__init__(groups)
    self.load_images()
    self.state, self.frame_index = "down", 0
    self.image = pygame.image.load(join("images", "player", "down", "0.png")).convert_alpha()
    self.rect = self.image.get_frect(center = pos)
    self.hitbox_rect = self.rect.inflate(-5, -20)
    self.collision_sprites = collision_sprites

    self.recent_kill_time=time.time()
    self.tracking_kill_timer=False
    

    # movement
    self.direction = pygame.Vector2()
    self.speed = 500

    # Recording movement
    self.movement_data = []
    self.last_recorded_pos = (-1, -1)  # Avoid duplicate consecutive positions

    self.all_tasks = {
              'O2': [3987.17, 1187.17],
              'NAVI': [5566.67, 1432.0], 
              'RIGHTCOM': [4303.0, 2525.0],
              'COMM': [3904.0, 2763.0], 
              'STOR': [3362.0, 2840.0], 
              'MED': [2643.0, 1327.0], 
              'REACUP': [893.0, 1006.0], 
              'REACDOWN': [885.5, 1919.0], 
              'ELEC': [2474.67, 1724.0], 
              'CAFELEF': [2777.33, 171.333], 
              'CAFERIGHT': [3823.33, 213.333]
          }
    
  def kill_nearby_bot(self):
    #print("fuck")
    # print(start_timer)
    # print(time.time()-start_timer)
    # print(time.time()-self.recent_kill_time)

    print(time.time()," is the current time")
    print(self.recent_kill_time," is the try time")


    if((time.time()-self.recent_kill_time)<min_kill_time):
       return
    
    damn=0
    

    for i in range(10):
      #print(mpp[i][0])
      #print(mpp[i][1])
      bnt=0

      for j in killed_players:
        if(j==i):
          bnt=bnt+1

      if(bnt==0 and ((mpp[i][0]-self.rect.center[0])**2+(mpp[i][1]-self.rect.center[1])**2)<=min_kill_distance**2):
        damn+=1

    if(damn>1):
      return
    
    for i in range(10):
      #print(mpp[i][0])
      #print(mpp[i][1])
      bnt=0

      for j in killed_players:
        if(j==i):
          bnt=bnt+1

      if(bnt==0 and ((mpp[i][0]-self.rect.center[0])**2+(mpp[i][1]-self.rect.center[1])**2)<=min_kill_distance**2):
        killed_players.append(i)
        recent_killed.append((i, [mpp[i][0], mpp[i][1]]))  # ✅ Correct
         # Start the timer for the recent kill
        self.recent_kill_time = time.time()
        self.tracking_kill_timer = True
        return  
        #print(killed_players)


  # def kill_nearby_bot(self):
  #   int check=-1;
  #   int store=min_kill_distance;
  #   for(auto it:sp){
  #       if(abs(it.second.first-self.rect.topleft[0])+abs(it.second.second-self.rect.top[1])<=store){
  #         check=self.i;
  #         store=abs(it.second.first-self.rect.topleft[0])+abs(it.second.second-self.rect.top[1]);
  #killed_x=self.rect.topleft[0]
  #killed_y=self.rect.topleft[1]
  #       }
  #   }

  #   if(check==-1) continue;
  #   else{
  #     //make changes in bot sprites of that i and call another function
  #killed_players.append(self.i)
  #
  #   }

  def save_movement_data(self):
    """Save recorded movement data with the nearest task to a CSV file."""
    with open("movement_data.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["X", "Y", "Nearest Task"])  # Column headers

        for x, y in self.movement_data:
            nearest_task = self.find_nearest_task(x, y)  # Find closest task
            writer.writerow([x, y, nearest_task])

        print("Movement data saved to movement_data.csv")
        

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

    if keys[pygame.K_SPACE]:
        self.kill_nearby_bot()  # Call a function to kill a nearby bot

    # keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:  # Press 'Enter' to save data
      self.save_movement_data()

    #print(global_time)

  def display_kill_timer(self,screen,font):
        """ Displays the kill timer on the screen """
        elapsed_time = self.get_kill_elapsed_time()
        if self.tracking_kill_timer:  # Only show timer if a kill happened
            timer_text = font.render(f"Kill Timer: {elapsed_time:.2f} sec", True, (255, 0, 0))
            screen.blit(timer_text, (20, 50))  # Adjust position as needed


  # def get_kill_elapsed_time(self):
  #       """ Returns the time elapsed since the last kill """
  #       if self.tracking_kill_timer and self.recent_kill_time:
  #           return time.time() - self.recent_kill_time
  #       return 0  # Return 0 if no recent kill


  def move(self, dt):
    self.hitbox_rect.x += self.direction.x * self.speed * dt
    self.collision("horizontal")

    self.hitbox_rect.y += self.direction.y * self.speed * dt
    self.collision("vertical")

    self.rect.center = self.hitbox_rect.center

    my_player_x,my_player_y=self.rect.center

    # print("ID OF BOT VS THEIR LOCATION")
    for i in mpp:
       if((self.rect.center[0]-mpp[i][0])**2 +(self.rect.center[1]-mpp[i][1])**2<=min_see_distance**2):
            list_player_tasks.append([mpp[i][0],mpp[i][1]])
            frequency_counter[i][my_id]+=1
  
    # print(my_player_x,my_player_y)

    # print(self.rect.center)
    # unique_coordinates.add(self.rect.center)
    # print(self.rect.center)

    # **Record unique integer positions**
    int_x, int_y = int(self.rect.centerx), int(self.rect.centery)
    if (int_x, int_y) != self.last_recorded_pos:  # Avoid duplicates
        
        self.movement_data.append((int_x, int_y))
        self.last_recorded_pos = (int_x, int_y)

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
    
   
  def find_nearest_task(self, x, y):
    """Find the closest task to the given (x, y) coordinate."""
    min_distance = float("inf")
    closest_task = None

    for task, coords in self.all_tasks.items():
        task_x, task_y = map(int, coords)  # Convert task coordinates to integers
        distance = math.dist((x, y), (task_x, task_y))  # Euclidean distance

        if distance < min_distance:
            min_distance = distance
            closest_task = task

    return closest_task
  


  
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
    if(stop==1):
       return
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




