import gym
import numpy as np
from keras.models import Sequential
from keras.optimizers import Adam
from keras.layers import Dense
from queue import Queue
import better_exceptions

env = gym.make('CartPole-v0')

env.seed(0)
np.random.seed(0)
games = 2000
exploration_rate = 1
learning_rate = 0.1




observation_size = env.observation_space.shape[0]
action_size = env.action_space.n


# Create neural network
model = Sequential()
model.add(Dense(30, input_dim=observation_size, activation='relu'))
model.add(Dense(20, activation='relu'))
model.add(Dense(action_size, activation='linear'))
model.compile(loss='mse', optimizer=Adam())

memory = Queue()

def choose_next_state(observation):
    action = model.predict(observation)
    # Choose random action some times
    if np.random.randn() < exploration_rate:
        return env.action_space.sample()
    else:
        return np.argmax(action)

def play():

    # Run for 50 times, or while queue full

    counter = 0

    while counter < 50:
        try:
            state, next_state, action, reward, done = memory.get(False)

        except:
            break

            target = model.predict(state)[0]
            if done:
                target[action] = reward
            else:
                target[action] = reward + (learning_rate  * np.amax(self.model.predict(next_state)[0]))

            model.fit(state, target)
        counter += 1


done = False

for game in range(games):
    observation = env.reset()
    # Needs to be reshaped for the size the model wants
    state = np.reshape(observation, [1, observation_size])

    for counter in range(1000):
        #env.render()
        
        action = choose_next_state(state)
        next_state, reward, done, info = env.step(action)

        if not done:
            reward = -10

        next_state = np.reshape(next_state, [1, observation_size])

        memory.put([state, next_state, action, reward, done])

        if done:
            print("\nDone: For Game: {} Score {}".format(game, counter))
            break

    print("\nStarting play")
    play()