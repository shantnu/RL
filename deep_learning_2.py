import gym
import numpy as np
from keras.models import Sequential

from keras.optimizers import Adam
from keras.layers import Dense, Convolution2D, Flatten
from queue import Queue
#import better_exceptions
import random

from rl.agents.dqn import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory


env = gym.make('CartPole-v0') 
#env = gym.make('MountainCar-v0')
env.seed(0)
np.random.seed(0)

observation_size = env.observation_space.shape
action_size = env.action_space.n


# Create neural network
model = Sequential()
model.add(Flatten(input_shape=(1,) + observation_size))
model.add(Dense(50, input_dim=observation_size, activation='relu'))
model.add(Dense(action_size, activation='linear'))
model.compile(loss='mse', optimizer=Adam())


# Create the agent
memory = SequentialMemory(limit=50000, window_length=1)
policy = BoltzmannQPolicy()
dqn = DQNAgent(model=model, nb_actions=action_size, memory=memory, nb_steps_warmup=10,
               target_model_update=1e-2, policy=policy)
dqn.compile(Adam(lr=1e-3), metrics=['mae'])

# Press ctrl+c to exit
dqn.fit(env, nb_steps=50000, visualize=True, verbose=2)

# Finally, evaluate our algorithm for 5 episodes.
dqn.test(env, nb_episodes=5, visualize=True)
