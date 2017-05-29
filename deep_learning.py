import gym
import numpy as np
from keras.models import Sequential

from keras.optimizers import Adam
from keras.layers import Dense, Convolution2D
from queue import Queue
import better_exceptions
import random

env = gym.make('CartPole-v0') 
#env = gym.make('MountainCar-v0')
env.seed(0)
np.random.seed(0)
games = 100

learning_rate = 0.5


observation_size = env.observation_space.shape[0]
action_size = env.action_space.n


# Create neural network

model = Sequential()
model.add(Dense(30, input_dim=observation_size, activation='relu'))
#model.add(Dense(300, input_dim=observation_size, activation='relu'))
model.add(Dense(50, input_dim=observation_size, activation='relu'))
#model.add(Dense(20, activation='relu'))
model.add(Dense(1, activation='linear'))
model.compile(loss='mse', optimizer=Adam())

memory = []



def choose_next_state(observation, exploration_rate):
    action = model.predict(observation)

    # Choose random action some times
    if np.random.randn() < exploration_rate:   
        return env.action_space.sample()
    
    else:
        return np.argmax(action)

def play():

    # Run for 50 times, or while queue full
    batch_size = 500
    batch_size = min(batch_size, len(memory))
    batch = random.sample(memory, batch_size)
    
    X = np.zeros((batch_size, observation_size))
    Y = np.zeros((batch_size, 1))

    for i in range(batch_size):

        state, next_state, action, reward, done = batch[i]
      
        target = model.predict(state)[0]
        if done:
            target = reward
        else:
            target = reward + (learning_rate  * np.amax(model.predict(next_state)[0]))

        #pdb.set_trace()
        #target = np.reshape(target, [1,action_size])
        X[i] = state
        Y[i] = target

    model.train_on_batch(X, Y) #, batch_size = batch_size, initial_epoch=5, verbose = 0)


done = False

import pdb
#pdb.set_trace()
exploration_rate = 0.99
for game in range(games):
    observation = env.reset()
    # Needs to be reshaped for the size the model wants
    state = np.reshape(observation, [1, observation_size])
    print("starting game ", game)
    for counter in range(2000):

        #env.render()
        
        #if counter % 20:
        #    exploration_rate *= 0.1
        action = choose_next_state(state, exploration_rate)
        next_state, reward, done, info = env.step(action)


        if not done:
            reward = -100
        else:
            reward = 100

        next_state = np.reshape(next_state, [1, observation_size])

        memory.append([state, next_state, action, reward, done])

        state = next_state

        if done:
            print("\nDone: For Game: {}/{} Score {}".format(game, games, counter))
            
            break

    #print("\nStarting play")
    play()