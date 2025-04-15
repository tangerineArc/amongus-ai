from collections import defaultdict
from itertools import permutations
from main import *
from player import *

# Given task locations
all_tasks = {
    'start_pos1':[3687,730],
    'start_pos2':[2940,634],
    'WEAP':[4416,552],
    'O2': [3987.17, 1187.17],
    'NAVI': [5566.67, 1432.0], 
    'RIGHTCOM': [4303.0, 2525.0],
    'ADM':[3704,1685],
    'CAMM':[1858,1380],
    'COMM': [3904.0, 2763.0], 
    'STOR': [3362.0, 2840.0], 
    'MED': [2643.0, 1327.0], 
    'REACUP': [893.0, 1006.0], 
    'REACDOWN': [885.5, 1919.0], 
    'ELEC': [2474.67, 1724.0], 
    'CAFELEF': [2777.33, 171.333], 
    'CAFERIGHT': [3823.33, 213.333],
    'REAC':[842,1358],
}

