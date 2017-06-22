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


import gym
env = gym.make('CartPole-v0')
env.reset()
for _ in range(100):
    env.render()
    env.step(env.action_space.sample())