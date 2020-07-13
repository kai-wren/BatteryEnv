import unittest
from battery_env import BatteryEnv

def reward_equationMAX(actual_load_list):
    return max(actual_load_list)

def reward_equationMIN(actual_load_list):
    return min(actual_load_list)

def reward_equationSUM(actual_load_list):
    return sum(actual_load_list)

def reward_equationLAST(actual_load_list):
    return actual_load_list[-1]

def reward_equationCOND(actual_load_list):
    if len(actual_load_list)%24!=0:
        return 0
    else:
        return actual_load_list[-1]

class MyTest(unittest.TestCase):
    def testEnvExist(self):
        env = BatteryEnv(reward_func=reward_equationMAX)
        self.assertIn(env.action_space.sample(), [0, 1, 2])
        
    def testMAX(self):
        env = BatteryEnv(reward_func=reward_equationMAX)
        lst = [1,2,3,3,10,-50]
        self.assertEqual(env.reward_func(lst), 10)
        
    def testMIN(self):
        env = BatteryEnv(reward_func=reward_equationMIN)
        lst = [1,2,3,3,10,-50]
        self.assertEqual(env.reward_func(lst), -50)
        
    def testSUM(self):
        env = BatteryEnv(reward_func=reward_equationSUM)
        lst = [1,2,3,3,10,-50]
        self.assertEqual(env.reward_func(lst), -31)
        
    def testLAST(self):
        env = BatteryEnv(reward_func=reward_equationLAST)
        lst = [1,2,3,3,10,-50]
        self.assertEqual(env.reward_func(lst), -31)
        
    def testCOND(self):
        env = BatteryEnv(reward_func=reward_equationCOND)
        lst = [1,2,3,3,10,-50]
        self.assertEqual(env.reward_func(lst), 0)
        
if __name__ == '__main__':
    unittest.main()