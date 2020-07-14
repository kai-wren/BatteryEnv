# BatteryEnv
## About
This package contains a custom environment called BatteryEnv for OpenAI Gym package. This environment specifically built for the particular problem of finding an optimal way to operate batteries in order to reduce daily variability of load. Such control problem seems natural for Reinforcement Learning (RL) algorithms and BatteryEnv providing an easy to use Gym-like environment to try and experiment with different RL agents and different reward functions. For this environment we used fixed dataset stored in file **data.csv** which contains hourly data of customer load from 2005-2017 years in Sweden.

## Installation
To install BatteryEnv in Google Colab please follow set of simple steps:

1. Download and install BatteryEnv with ```pip```.
```
!python -m pip install -e git+https://github.com/kai-wren/BatteryEnv4Gym.git#egg=batteryenv4gym
```

2. Next, execute command to identify location of BatteryEnv.
```
!pip show batteryenv4gym
```

Example output:
```
Name: batteryenv4gym
Version: 0.0.1
Summary: UNKNOWN
Home-page: UNKNOWN
Author: UNKNOWN
Author-email: UNKNOWN
License: UNKNOWN
Location: /content/src/batteryenv4gym
Requires: gym, numpy, pandas, matplotlib
Required-by: 
```

3. Execute python code below to add location of BatteryEnv package to system path. 
```python
import sys
sys.path.append('/content/src/batteryenv4gym')
```

After this step you could execute below code to get environment created:
```python
import gym
import batteryenv4gym

def reward_equation(actual_load_list):
    return max(actual_load_list)
    
env = gym.make('batteryenv-v0', reward_func=reward_equation)
```

## Validating environment with help of stochastic agent
After installation is over BatteryEnv could be validated by using simple random agent. 
Sample agent code:
```python
import numpy as np

class StochasticAgent():

    def __init__(self, env):
      self.env = env
    
    def execute(self, num_episodes):
        for episode in range(num_episodes):
            observation = self.env.reset()
            t=0
            while (True):
                t+=1
                action = self.env.action_space.sample()
                observation, reward, done, info = self.env.step(action)
                if done:
                    print("Episode finished after {} timesteps".format(t))
                    arr = np.array(self.env.reward_list)
                    print("Episode reward %.5f", arr.sum())
                    break
```
After agent class is created it could be executed with simple code below:
```python
agent = StochasticAgent(env)
agent.execute(5)
```

For your convinience example notebook with all mentioned code could be found in [Google Colab](https://colab.research.google.com/drive/1sj_G0lFS5UtAiUZTsVlEBSe9DNA9iqWT?usp=sharing)
