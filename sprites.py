import pygame
from constants import *
from player import *
import csv
from global_knowledge import *
from os.path import join

from sus import meeting_called



class Sprite(pygame.sprite.Sprite):
  def __init__(self, pos, surf, groups):
    super().__init__(groups)
    self.image = surf
    self.rect = self.image.get_frect(topleft=pos)
    self.ground = True


class CollisionSprite(pygame.sprite.Sprite):
  def __init__(self, pos, surf, groups):
    super().__init__(groups)
    self.image = surf
    self.rect = self.image.get_frect(topleft=pos)

class Bot(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites, color,i,all_tasks):
        super().__init__(groups)
        self.color = color
        self.load_images()
        self.state, self.frame_index = "down", 0
        self.image = self.frames[self.state][0]
        self.rect = self.image.get_rect(center=pos)

        self.hitbox_rect = self.rect.inflate(30, 50)
        self.collision_sprites = collision_sprites
        self.speed = 250  
        self.movement_index = 0
        self.i = i
        self.all_tasks = all_tasks 
        self.previous_pos = pygame.Vector2(pos)
        self.visited_tasks = set()
        # Movement Timing Variables
        self.current_task = self.find_nearest_task(pos)
        self.visited_tasks.add(self.current_task)

        # Load movement data to the first task
        self.movement_data = []
        self.load_next_movement_data()

        #  # Available task locations
        # self.all_tasks = {
        #     'O2': [3987.17, 1187.17],
        #     'NAVI': [5566.67, 1432.0], 
        #     'RIGHTCOM': [4303.0, 2525.0],
        #     'COMM': [3904.0, 2763.0], 
        #     'STOR': [3362.0, 2840.0], 
        #     'MED': [2643.0, 1327.0], 
        #     'REACUP': [893.0, 1006.0], 
        #     'REACDOWN': [885.5, 1919.0], 
        #     'ELEC': [2474.67, 1724.0], 
        #     'CAFELEF': [2777.33, 171.333], 
        #     'CAFERIGHT': [3823.33, 213.333]
        # }

        #         # Randomly select 7 unique tasks
        # self.selected_tasks = random.sample(list(self.all_tasks.items()), 7)

        # # Convert back to dictionary format
        # self.selected_tasks_dict = dict(self.selected_tasks)


    def load_images(self):
        self.frames = {"left": [], "right": [], "up": [], "down": []}
        directions = ["left", "right", "up", "down"]
        for direction in directions:
            for step in range(1, 4):
                path = join("images", self.color, direction, f"step{step}.png")
                surface = pygame.image.load(path).convert_alpha()
                self.frames[direction].append(surface)

    def find_nearest_task(self, pos):
        """Find the nearest task from the bot's starting position."""
        min_distance = float('inf')
        nearest_task = None
        pos_vector = pygame.Vector2(pos)
        for task, coords in self.all_tasks.items():
            distance = pygame.Vector2(coords).distance_to(pos_vector)
            if distance < min_distance:
                min_distance = distance
                nearest_task = task
        return nearest_task


    def randomize_direction(self):
        """ Picks a smooth random movement direction (normalized) """
        directions = [
            pygame.Vector2(1, 0),   
            pygame.Vector2(-1, 0),  
            pygame.Vector2(0, 1),   
            pygame.Vector2(0, -1),  
            pygame.Vector2(1, 1),   
            pygame.Vector2(-1, -1), 
            pygame.Vector2(1, -1),  
            pygame.Vector2(-1, 1),  
        ]
        self.direction = random.choice(directions).normalize()  

    def move(self, dt):
        """ Moves the bot and handles collisions step-by-step """
        if not self.movement_data:
            remaining_tasks = list(set(self.all_tasks.keys()) - self.visited_tasks)
            if remaining_tasks:
                self.load_next_movement_data()
            else:
                return

        if self.movement_index < len(self.movement_data):
            target_pos = self.movement_data[self.movement_index]
            direction = target_pos - self.previous_pos

            if direction.length() > 0:
                distance = self.speed * dt
                if direction.length() <= distance:
                    self.previous_pos = target_pos
                    self.movement_index += 1
                else:
                    move_vector = direction.normalize() * distance
                    self.previous_pos += move_vector

            self.rect.center = self.previous_pos
            self.hitbox_rect.center = self.previous_pos
            mpp[self.i]=self.rect.center

            # Set animation state based on movement direction
            if abs(direction.x) > abs(direction.y):
                self.state = "right" if direction.x > 0 else "left"
            else:
                self.state = "down" if direction.y > 0 else "up"
        else:
            # Finished current movement segment: snap to the final coordinate,
            # update the current task and load the next movement data.
            self.previous_pos = self.movement_data[-1] if self.movement_data else self.previous_pos
            self.rect.center = self.previous_pos
            self.hitbox_rect.center = self.previous_pos
            self.current_task = self.next_task
            self.load_next_movement_data()

    def animate(self, dt):
            self.frame_index += 10 * dt
            self.image = self.frames[self.state][int(self.frame_index) % len(self.frames[self.state])]


    def load_next_movement_data(self):
        """Choose the next task randomly and load the corresponding movement CSV."""
        remaining_tasks = list(set(self.all_tasks.keys()) - self.visited_tasks)

        if not remaining_tasks:
            self.movement_data = []  # Stop moving when all tasks are done
            return

        self.next_task = random.choice(remaining_tasks)
        self.visited_tasks.add(self.next_task)

        filename = f"./data/movement_data/{self.current_task}_to_{self.next_task}.csv"
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header if present
                self.movement_data = [pygame.Vector2(float(row[0]), float(row[1])) for row in reader]
            self.movement_index = 0
        except FileNotFoundError:
            print(f"Warning: {filename} not found. Skipping this movement.")
            self.movement_data = []



    def check_collision(self):
        """ Checks if bot collides with any obstacles """
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.hitbox_rect):
                return True  
        return False  

    def update(self, dt):
        """ Updates bot movement, pauses randomly, and changes direction at intervals """
        # int cnt=0;

        if(stop==1):
            return

        cnt=0
        for j in killed_players:
           if(j==self.i):
               cnt=cnt+1
        if(cnt!=0):
            return
        num=random.randint(1,20)

        # if((self.rect.center[0]-my_player_x)**2 +(self.rect.center[1]-my_player_y)**2<=min_see_distance**2):
        #     list_player_tasks.append([my_player_x,my_player_y])
        

        if(num%3==0):
            mini=0
            min_dist=999999999
            for j in range(0,10):
                if(j==self.i):
                    continue
                if((self.rect.center[0]-mpp[j][0])**2 +(self.rect.center[1]-mpp[j][1])**2<=min_dist**2):
                    mini=j
                    min_dist=(self.rect.center[0]-mpp[j][0])**2 +(self.rect.center[1]-mpp[j][1])**2

            # if((self.rect.center[0]-my_player_x)**2 +(self.rect.center[1]-my_player_y)**2<=min_dist**2):
            #     mini=my_id

            frequency_counter[self.i][mini]+=1
        

        cur_x=self.rect.center[0]
        cur_y=self.rect.center[1]
        
        for i,(j,k) in recent_killed:
            if((self.rect.center[0]-j)**2+(self.rect.center[1]-k)**2<=min_body_found**2):
                meeting_called()



        # for i in range(0,10):
        #     if((cur_x-mpp[i].first)**2+(cur_y-mpp[i].second)**2<=min_body_found):




        # for(auto it:killed_players){
        #     if(it==self.i){
        #         cnt++;
        #         break;
        #     }
        # }


        # if(cnt){
        #     #no movement and stop this bot entirely
        # }

        # if this bot is not killed check proximity of htis bot with recenetly killed bot
        #if(killed_x==-1) continue
        #else:
        #now report and call another function
        #gotkilled++;

        self.move(dt)
        self.animate(dt)