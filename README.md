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
3. Execute python code below to 
```python
import sys
sys.path.append('/content/src/batteryenv4gym')
```

## Stochastic baseline agent
