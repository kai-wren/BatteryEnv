from gym.envs.registration import register

register(
    id='battery_env-v0',
    entry_point='battery_env4gym.envs:BatteryEnv',
)