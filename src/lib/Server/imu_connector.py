#!/usr/bin/env python3 
# # this file should be in python 3
"""Here we will import the class and begin to generate random values while setting the class attributes to those random values"""
# from imu_data import IMU_DATA  # this line only works when we run python3 in the terminal
from Server.imu_data import IMU_DATA # this is the class that will be imported
from random import randint, uniform

START_RANGE = 0
END_RANGE = 100
class Test(IMU_DATA): # this class inherites from the IMU_DATA
    def __init__(self):
        super().__init__(IMU_DATA)

    def generate_data(self):
        
        self.time_startup = randint(START_RANGE, END_RANGE)
        self.time_sync_in = randint(START_RANGE, END_RANGE)
        self.ypr = uniform(START_RANGE, END_RANGE)
        self.attitude = uniform(START_RANGE, END_RANGE)
        self.orientation = uniform(START_RANGE, END_RANGE)
        self.angular_rate = uniform(START_RANGE, END_RANGE)
        self.accelearation = uniform(START_RANGE, END_RANGE)
        self.imu_accelaration = uniform(START_RANGE, END_RANGE)
        self.imu_rate= uniform(START_RANGE, END_RANGE) 
        self.mag = uniform(START_RANGE, END_RANGE)
        self.temp = uniform(START_RANGE, END_RANGE)
        self.pres = uniform(START_RANGE, END_RANGE)
        self.dtime = uniform(START_RANGE, END_RANGE)
        self.dtheta = uniform(START_RANGE, END_RANGE)
        self.dvel = uniform(START_RANGE, END_RANGE)
        self.vpe_status = randint(START_RANGE, END_RANGE)
        self.sync_in_cnt = randint(START_RANGE, END_RANGE)
        self.sync_out_cnt = randint(START_RANGE, END_RANGE)

    def show_data(self):
        self.generate_data()
        return vars(self)


# obj = Test()
# obj.generate_data()
# print(obj.show_data())
# print("\nRunning it all again \n\n\n")
# obj.generate_data()
# print(obj.show_data())


