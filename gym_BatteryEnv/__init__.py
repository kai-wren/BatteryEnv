from gym.envs.registration import register

register(
    id='BatteryEnv-v0',
    entry_point='gym_BatteryEnv.envs:BatteryEnv',
)