import gym

import numpy as np
import pdb

def modify_reward(reward, done):
    if done and reward == 0:
        return -100.0
    elif done:
        return 50.0
    else:
        return 1.0

env = gym.make('FrozenLake-v0')

env.seed(0)
np.random.seed(0)

learning_rate = .05

discount_factor = .99

exploration_rate = 0.99

Q_Table = np.zeros([env.observation_space.n, env.action_space.n])
print("Q_Table Table shape = ", Q_Table.shape)


games = 2000
num_episodes = 2000

reward_total = []

for game in range(1, games):
    state = env.reset()
    env.render()
    
    done = False

    reward_current_state = 0

    while not done:
              
        action = np.argmax(Q_Table[state,:] + np.random.randn(1, env.action_space.n) * (1 / game ) ) 
         
           
        state_new, reward, done, _  = env.step(action)

        reward_modified = modify_reward(reward,done)

        #update Q_Table-Table with new knowledge
        Q_Table[state, action] = Q_Table[state, action] + learning_rate*(reward_modified+ (discount_factor * np.max(Q_Table[state_new,:])-Q_Table[state, action]))


        reward_current_state += reward
        if done:
            print("For game {}, award = {}".format(game, reward))
            break

        state = state_new
    


    reward_total.append(reward_current_state)


env.close()


# This function taken from https://stackoverflow.com/a/14314054 by user @Jamie
# because I coudlnt find an inbuilt moving average function
def moving_average(a, n=100) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

print("Reward average = {} ".format(sum(reward_total) / games))

average = moving_average(np.asarray(reward_total))
print("Best 100 run average = ", average.max())