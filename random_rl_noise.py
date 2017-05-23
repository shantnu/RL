import gym

import numpy as np

env = gym.make('CartPole-v0')

env.seed(0)
np.random.seed(0)

def run_single_episode(parameters, env):

    total_reward = 0
    observation = env.reset()
    env.render()
    for i_episode in range(100):
        result = np.matmul(parameters,observation)

        if (-0.25 < result < 0)  :
            action = 0
        elif (0 < result < 0.25):
            action = 2
        else:
            action  = 1
        print("action =", action)
        observation, reward, done, info = env.step(action)
        total_reward += reward
        if done:
            break
    
    return total_reward



highest_reward_so_far = 0
best_parameters_so_far = None
scaling_factor = 0.1

parameters = np.random.uniform(-1, 1, 2)

for _ in range(1000):

    parameters_with_noise = parameters + (np.random.uniform(-1, 1, 2) * scaling_factor)
    

    reward = run_single_episode(parameters_with_noise, env)
    print("Reward = ", reward)

    if reward > highest_reward_so_far:
        highest_reward_so_far = reward
        best_parameters_so_far = parameters_with_noise
        print("\n\n Best Current Reward: ", reward)


print("\n\n Best Current Reward: ", reward)        