# BatteryEnv
## About
This package contains a custom environment called BatteryEnv for OpenAI Gym package. This environment specifically built for the particular problem of finding an optimal way to operate batteries to reduce daily variability of load. Such control problem seems natural for Reinforcement Learning (RL) algorithms and BatteryEnv providing an easy to use Gym-like environment to try and experiment with different RL agents and different reward functions. For this environment we used fixed dataset stored in file **data.csv** file contains hourly data of customer load from 2005-2017 years in Sweden.

## Installation
```python
import sys
sys.path.append('/content/src/batteryenv4gym')
```

## Stochastic baseline agent
