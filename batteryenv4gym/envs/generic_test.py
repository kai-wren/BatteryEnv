import unittest
import numpy as np
from battery_env import BatteryEnv

def reward_equationMAX(actual_load_list):
    return max(actual_load_list)

class GenericTest(unittest.TestCase):
    
    # check that environment has correct action space
    def testEnvActionSpace(self):
        env = BatteryEnv(reward_func=reward_equationMAX)
        self.assertIn(env.action_space.sample(), [0, 1, 2])
        
    # testing that state index properly incremented with steps taken
    def testEnvIndex(self):
        env = BatteryEnv(reward_func=reward_equationMAX)
        self.assertEqual(env.state_idx, 0)
        
        for i in range(10):
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)
        self.assertEqual(env.state_idx, 10)
        
        env.restart_env()
        self.assertEqual(env.state_idx, 0)
    
    # check that actual load properly calculated with certain steps taken in a row
    def testActualLoad(self):
        env = BatteryEnv(reward_func=reward_equationMAX)
        self.assertEqual(len(env.actual_load_list), 0)
        
        for i in range(10):
            action = 0
            observation, reward, done, info = env.step(action)
        self.assertEqual(len(env.actual_load_list), 10)
        
        arr = np.array(env.actual_load_list)
        self.assertEqual(arr.sum(), 158838.65)
        
        arr = np.array(env.actual_load_list)
        self.assertEqual(arr.min(), 15226.48)
        
        arr = np.array(env.actual_load_list)
        self.assertEqual(arr.max(), 16997.13)
        
        arr = np.array(env.actual_load_list)
        self.assertEqual(arr.mean(), 15883.865)
        
        env.restart_env()
        self.assertEqual(len(env.actual_load_list), 0)
        
        for i in range(10):
            action = 1
            observation, reward, done, info = env.step(action)
        self.assertEqual(len(env.actual_load_list), 10)
        
        arr = np.array(env.actual_load_list)
        self.assertEqual(arr.sum(), 159238.65)
        
        arr = np.array(env.actual_load_list)
        self.assertEqual(arr.min(), 15326.48)
        
        arr = np.array(env.actual_load_list)
        self.assertEqual(arr.max(), 16997.13)
        
        arr = np.array(env.actual_load_list)
        self.assertEqual(arr.mean(), 15923.865)
        
        env.restart_env()
        self.assertEqual(len(env.actual_load_list), 0)
        
        for i in range(10):
            action = 2
            observation, reward, done, info = env.step(action)
        self.assertEqual(len(env.actual_load_list), 10)
        
        arr = np.array(env.actual_load_list)
        self.assertEqual(arr.sum(), 159238.65)
        
        arr = np.array(env.actual_load_list)
        self.assertEqual(arr.min(), 15326.48)
        
        arr = np.array(env.actual_load_list)
        self.assertEqual(arr.max(), 16997.13)
        
        arr = np.array(env.actual_load_list)
        self.assertEqual(arr.mean(), 15923.865)
        
        
if __name__ == '__main__':
    unittest.main()