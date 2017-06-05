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
        action = 0 if np.matmul(parameters,observation) < 0 else 1

        observation, reward, done, info = env.step(action)
        total_reward += reward
        if done:
            break
    
    return total_reward



highest_reward_so_far = 0
best_parameters_so_far = None
scaling_factor = 0.1

parameters = np.random.uniform(-1, 1, 4)

count = 0

for _ in range(1000):
    
    parameters_with_noise = parameters + (np.random.uniform(-1, 1, 4) * scaling_factor)

    reward = run_single_episode(parameters_with_noise, env)
    print("Reward = ", reward)

    if reward > highest_reward_so_far:
        count +=1
        highest_reward_so_far = reward
        parameters = parameters_with_noise
        print("\n\n Best Current Reward: ", reward)


print("\n\n Best Current Reward: {} found on count {} ".format(highest_reward_so_far, count))