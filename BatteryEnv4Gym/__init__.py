from gym.envs.registration import register

register(
    id='BatteryEnv-v0',
    entry_point='BatteryEnv4Gym.envs:BatteryEnv',
)