import unittest
from batteryenv4gym.envs.battery_env import BatteryEnv

def reward_equationMAX(actual_load_list):
    return max(actual_load_list)

class MyTest(unittest.TestCase):
    def test(self):
        env = BatteryEnv(reward_func=reward_equationMAX)
        self.assertIn(env.action_space.sample, [0, 1, 2])
        
#if __name__ == '__main__':
#    unittest.main()