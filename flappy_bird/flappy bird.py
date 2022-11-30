import gym
import pygame
import random
import numpy as np
import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
from statistics import mean, median
from collections import Counter

from ple.games.flappybird import FlappyBird
game = FlappyBird()
from ple import PLE


p = PLE(game, fps=30, display_screen=True,
        reward_values=
        {
            "positive": 1.0,
            "negative": -1.0,
            "tick": 1.0,
            "loss": 0.0,
            "win": 5.0
        },
            force_fps= True)
p.init()
reward = 0.0
counter = 0
initial_games = 1000
goal_steps = 1000
score_requirement = 50
LR = 1e-5
myKeys = ['next_pipe_dist_to_player','next_pipe_bottom_y','player_vel','next_next_pipe_bottom_y','next_pipe_top_y','next_next_pipe_dist_to_player','player_y','next_next_pipe_top_y']



def initial_population():
    training_data = []
    scores = []
    accepted_scores = []
    reward = 0
    for i in range(initial_games):
        score = 0
        game_memory = []
        prev_observation = []
        for _ in range(goal_steps):
            action = random.randrange(0,10)
            observation = game.getGameState()
            p.act(0)
            if action == 1:
                reward = p.act(119)

            if len(prev_observation) > 0:
                game_memory.append([prev_observation, action])
            prev_observation = observation
            score += reward
            if p.game_over():
                break

        if score >= score_requirement:
            accepted_scores.append(score)
            for data in game_memory:
                if data[1] == 1:
                    output = [0,1]
                elif data[1] == 0:
                    output = [1,0]
                elif data[1] == 2:
                    output = [1, 0]
                elif data[1] == 3:
                    output = [1, 0]
                elif data[1] == 4:
                    output = [1, 0]
                elif data[1] == 5:
                    output = [1, 0]
                elif data[1] == 6:
                    output = [1, 0]
                elif data[1] == 7:
                    output = [1, 0]
                elif data[1] == 8:
                    output = [1, 0]
                elif data[1] == 9:
                    output = [1, 0]
                elif data[1] == 10:
                    output = [1, 0]

                training_data.append([[data[0][k] for k in myKeys], output])

        p.reset_game()
        scores.append(score)

    training_data_save = np.array(training_data)
    #np.save('saved.npy', training_data_save)

    print('Average accepted score:', mean(accepted_scores))
    print('Median accepted score:', median(accepted_scores))
    print(Counter(accepted_scores))

    return training_data



def nueral_netword_model(input_size):
    network = input_data(shape = [None, input_size, 1], name = 'input')

    network = fully_connected(network,128,activation='relu')
    network = dropout(network, 0.8)

    network = fully_connected(network, 256, activation='relu')
    network = dropout(network, 0.8)

    network = fully_connected(network, 512, activation='relu')
    network = dropout(network, 0.8)

    network = fully_connected(network, 256, activation='relu')
    network = dropout(network, 0.8)

    network = fully_connected(network, 128, activation='relu')
    network = dropout(network, 0.8)

    network = fully_connected(network, 2, activation='softmax')
    network = regression(network, optimizer='adam', learning_rate=LR,
                         loss = 'binary_crossentropy', name='targets')
    model = tflearn.DNN(network, tensorboard_dir='log')
    return model


def train_model(training_data, model=False):
    X = np.array([i[0] for i in training_data]).reshape(-1, len(training_data[0][0]),1)
    Y = [i[1] for i in training_data]


    if not model:
        model = nueral_netword_model(input_size=len(X[0]))

    model.fit({'input':X}, {'targets':Y}, n_epoch=2, snapshot_step=500, show_metric=True, run_id='openaistuff')

    return model


training_data = initial_population()
model = train_model(training_data)


scores = []
choices = []

for each_game in range(1000):
    score = 0
    game_memory = []
    prev_obs = []
    p.reset_game()
    for _ in range(goal_steps):
        p.act(0)
        if len(prev_obs) == 0:
            action = random.randrange(0, 10)
        else:
            action = np.argmax(model.predict(prev_obs.reshape(-1, len(prev_obs), 1))[0])
            print("Action is ", action)
        if action == 1:
            reward = p.act(119)


        choices.append(action)
        new_observation = np.asarray([game.getGameState()[k] for k in myKeys])
        p.act(0)
        prev_obs = new_observation
        game_memory.append([new_observation, action])
        score += reward
        if p.game_over():
            break

    scores.append(score)

print('Average Score:',sum(scores)/len(scores))
print('choice 1:{}  choice 0:{}'.format(choices.count(1)/len(choices),choices.count(0)/len(choices)))
print(score_requirement)