import pygame

damn=0
num_players=0

killed_players=[]
killed_x=-1
killed_y=-1

import time

# from main import *

#map<int,pair<int,int>> sp;

#import killed players list from player.py
#make changes in update function and if that bot is present 

mpp = {}  # Dictionary where keys are int and values are (int, int)
player=0

stop=0



# Initialize a dictionary of dictionaries for storing probabilities
probability_for_each = {i: {j: 0 for j in range(13)} for i in range(13)}

def past_haunts_you(id, W3):
    for i in range(13):
        if i == id:
            continue
        probability_for_each[id][i] *= W3  # ✅ No more KeyError



mpp[0]=(10000,10000)
mpp[1]=(10000,10000)
mpp[2]=(10000,10000)
mpp[3]=(10000,10000)
mpp[4]=(10000,10000)
mpp[5]=(10000,10000)
mpp[6]=(10000,10000)
mpp[7]=(10000,10000)
mpp[8]=(10000,10000)
mpp[9]=(10000,10000)
mpp[10]=(10000,10000)
mpp[11]=(10000,10000)
mpp[12]=(10000,10000)

frequency_counter={}
frequency_counter[0]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
frequency_counter[1]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
frequency_counter[2]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
frequency_counter[3]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
frequency_counter[4]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
frequency_counter[5]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
frequency_counter[6]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
frequency_counter[7]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
frequency_counter[8]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
frequency_counter[9]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
frequency_counter[10]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
frequency_counter[11]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
frequency_counter[12]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]

recent_killed=[]



mp={}  # dictionary of bot id vs current position

list_player_tasks=[]


# recent_kill_time=0
# tracking_kill_timer=False

id_of_admin=0

my_id=12




# my_player_x=0
# my_player_y=0


# for i in (0,13):
#     for j in (0,13):
#         frequency_counter[i][j]=0   

