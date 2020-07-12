import os
import sys

#current_file = os.path.abspath(os.path.dirname(__file__))
#csv_filename = os.path.join(current_file, '/data/data.csv')
#print(csv_filename)

#current_file = os.path.abspath(__file__)
#print(current_file)

#import pathlib
#current_file = pathlib.Path().absolute()
#csv_filename = os.path.join(current_file, '/data/data.csv')
#csv_filename = os.path.join('D:/jupyter\\BatteryEnv4Gym\\batteryenv4gym\\envs', '/data/data.csv')
#print(csv_filename)

csv_filename = (os.path.abspath(os.path.dirname(sys.argv[0])) + "\data\data.csv")

csv_filename = csv_filename
print(csv_filename)