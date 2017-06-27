import gym
import time

envs = ['CartPole-v0','MountainCar-v0', 'FrozenLake-v0']

for e in envs:
    env = gym.make(e)

    for _ in range(10):
       observation = env.reset()
       for t in range(100):
            env.render()
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)

            if done:
              print("Episode finished after {} timesteps".format(t+1))
              break

    time.sleep(2)