import time
import numpy as np
import pygame
from global_knowledge import *
from constants import *
from learning import *


# Q-table for reinforcement learning
q_table = np.zeros((6, 6))

def update_weights(reward):
    global weights
    weights += learning_rate * (reward - weights)
    print("Weights")
    print(weights)

def get_reward(is_correct_vote):
    return 1 if is_correct_vote else -1

def meeting_called():
    global weights
    start = time.time()
    
    print("ID OF BOT VS THEIR LOCATION")
    for i in mpp:
        print(i, mpp[i][0], mpp[i][1])

    print("Killed players")
    print(killed_players)

    print("Frequency counter")
    for i in range(0, 13):  
        for j in range(0,13):
            if i == j:
                continue
            frequency_counter[i][j]=frequency_counter[i][j]/100000
            print(i, j, frequency_counter[i][j])

    print("Recent killed")
    for i, pos in recent_killed:
        print(i, pos[0], pos[1])

    print("List of player tasks")
    for i in list_player_tasks:
        print(i)

    print("Where were you?")
    str_location = input()
    print("How many tasks did you do?")
    num_tasks = int(input())  
    list_of_tasks = [input() for _ in range(num_tasks)]

    votes_for_each = {i: 0 for i in range(13)}

    print("WHO DO YOU WANT TO VOTE OUT?")
    y = int(input())
    votes_for_each[y] += 1

    def past_haunts_you(id):
        for i in range(13):
            if i == id:
                continue
            probability_for_each[id][i] *= weights[0]

    def how_many_times_i_saw_you(id):
        for i in range(10):
            if i == id:
                continue
            probability_for_each[id][i] += weights[1] * frequency_counter[id][i]

    def kill_radius_found(id):
        center_x, center_y = recent_killed[-1][1]
        time_elapsed = time.time() - min_kill_time

        for j in range(10):
            probability_for_each[j][12] += weights[2] * time_elapsed

        for i in range(10):
            dist = ((center_x - mpp[i][0]) ** 2 + (center_y - mpp[i][1]) ** 2) ** 0.5
            for j in range(10):
                probability_for_each[j][i] += (weights[3] * time_elapsed - dist)

    def i_saw_you_do_that(id):
        if id in killed_players:
            return
        bnt = sum(1 for j in list_of_tasks if j not in list_player_tasks)
        probability_for_each[id][my_id] += bnt * weights[4]
        for i in range(10):
            if i == id:
                continue
            probability_for_each[id][i] += weights[5]

    # **State before voting**
    state = []
    for i in range(10):
        if i in killed_players:
            continue
        state.append(probability_for_each[i][12])  # Probability of voting against impostor

    # **Voting process**
    for i in range(10):
        if i in killed_players:
            continue
        past_haunts_you(i)
        how_many_times_i_saw_you(i)
        kill_radius_found(i)
        i_saw_you_do_that(i)

    for i in range(10):
        if i in killed_players:
            continue
        list_of_prob = [[probability_for_each[i][k] + probability_for_each[my_id][k], k] for k in range(10)]
        list_of_prob.sort(reverse=True, key=lambda x: x[0])
        votes_for_each[list_of_prob[0][1]] += 1

    print("Votes:")
    for i in votes_for_each:
        print(i, votes_for_each[i])

    print(probability_for_each)

    # **Determine highest voted player**
    voted_out = max(votes_for_each, key=votes_for_each.get)

    if votes_for_each[voted_out] == max(votes_for_each.values()) and list(votes_for_each.values()).count(max(votes_for_each.values())) > 1:
        voted_out = -1  # Tie

    # **Determine reward**
    reward = get_reward(voted_out == 12)

    # **Next state after voting**
    next_state = []
    for i in range(10):
        if i in killed_players:
            continue
        next_state.append(probability_for_each[i][12])  # Updated probabilities

    done = voted_out == 12  # Game ends if impostor is voted out

    # **Count correct votes**
    correct_votes = votes_for_each[12]  # Bots that voted against impostor
    total_votes = sum(votes_for_each.values())

    # **Call RL training function**
    after_voting_train(state, voted_out, reward, next_state, done, correct_votes, total_votes)

    # **Update weights**
    update_weights(reward)

    # **Update game state**
    print("VOTED OUT PLAYER IS:")
    print(voted_out)
    if(voted_out==12):
        stop=1
    killed_players.append(voted_out)
    recent_killed.clear()
