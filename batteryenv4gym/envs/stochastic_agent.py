import numpy

class StochasticAgent():
    
    def execute(env, num_episodes):
        for episode in range(num_episodes):
            observation = env.reset()
            t=0
            while (True):
                t+=1
                action = env.action_space.sample()
                observation, reward, done, info = env.step(action)
                if done:
                    print("Episode finished after {} timesteps".format(t))
                    arr = np.array(env.reward_list)
                    print("Episode reward %.5f", arr.sum())
                    break