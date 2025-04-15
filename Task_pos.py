import pygame
from pytmx.util_pygame import load_pygame
from os.path import join
from main import *

from WELCOME import welcome
game = Game()

game_map = load_pygame(join("data", "maps", "map.tmx"))
pos = {}

for obj in game_map.get_layer_by_name("Tasks"):
    pos[obj.name] = [obj.x, obj.y]

print(pos)



# {'O2': [3987.17, 1187.17]
#  'NAVI': [5566.67, 1432.0], 
#  'RIGHTCOM': [4303.0, 2525.0],
#    'COMM': [3904.0, 2763.0], 
#    'STOR': [3362.0, 2840.0], 
#    'MED': [2643.0, 1327.0], 
#    'REACUP': [893.0, 1006.0], 
#    'REACDOWN': [885.5, 1919.0], 
#    'ELEC': [2474.67, 1724.0], 
#    'CAFELEF': [2777.33, 171.333], 
#    'CAFERIGHT': [3823.33, 213.333]}