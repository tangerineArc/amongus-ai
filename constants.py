import pygame
from os.path import join
from os import walk
import random
import numpy as np

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
TILE_SIZE = 32
min_kill_distance=100

min_kill_time=20

start_pos=(3687.8798828125, 730.302978515625)

min_body_found=100

min_see_distance=100

# RL Model Parameters
learning_rate = 0.1
discount_factor = 0.9
epsilon = 0.1  # Exploration factor
weights = np.array([0.5, 0.5, 0.5, 0.5, 0.5, 0.5])  # Initial weights for W1 to W6


W1=1
W2=2
W3=3
W4=4
W5=5
W6=6
W7=7
W8=8
W9=9

# Given task locations
all_tasks = {
    'start_pos1':[3687,730],
    'start_pos2':[2940,634],
    'start_pos3':[3224,464],
    'start_pos4':[3208,900],
    'WEAPONS':[4416,552],
    'O2': [3987.17, 1187.17],
    'NAVI': [5566.67, 1432.0], 
    'RIGHTCOM': [4303.0, 2525.0],
    # 'ADM':[3704,1685],
    'CAMS':[1858,1380],
    # 'COMM': [3904.0, 2763.0], 
    'GARBAGE': [3362.0, 2840.0], 
    'MED': [2643.0, 1327.0], 
    'UPPERENGINE': [893.0, 1006.0], 
    'LOWERENGINE': [885.5, 1919.0], 
    'ELECTRICAL': [2474.67, 1724.0], 
    'CAFELEFT': [2777.33, 171.333], 
    'CAFERIGHT': [3823.33, 213.333],
    'REACTOR': [889.0, 1400.0], 
    # 'REAC':[842,1358],
    # 'EXIT-S':[3257,1236],
    # 'EXIT-E':[3909,636],
    # 'EXIT-W':[2465,657],
    # 'LOBB-R':[4764,1205],
    # 'LOBB-L':[1733,673],
    # 'LOBB-ML':[1372,1384],
    # 'LIGHT':[2229,2220]
}