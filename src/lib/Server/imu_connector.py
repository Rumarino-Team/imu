#!/usr/bin/env python3 
# # this file should be in python 3
"""Here we will import the class and begin to generate random values while setting the class attributes to those random values"""
# from imu_data import IMU_DATA  # this line only works when we run python3 in the terminal
from imu_data import IMU_DATA # this is the class that will be imported
from random import randint, uniform
from vnpy import VnSensor

START_RANGE = 0
END_RANGE = 100
class Test(IMU_DATA): # this class inherites from the IMU_DATA
    def __init__(self):
        super().__init__(IMU_DATA)

        self.vnsensor = VnSensor()
        # self.vnsensor.connect('COM1', 115200) # docu dice que necesito port, baudrate as arguments
     
    """this function is an attempt to use the vnsensor object and to match the values of the sensor to the class
    the assignments are not done since further analysis of the API and its methods."""
    def REAL_DATA(self):
        vn = self.vnsensor

        # self.time_startup = 
        # self.time_sync_in = 
        # self.ypr = vn.read_yaw_pitch_roll()
        # self.attitude = 
        # self.orientation = 
        # self.angular_rate = vn.read_angular_rate_measurements()
        # self.accelearation = 
        # self.imu_accelaration =  
        # self.imu_rate= vn.read_imu_rate_configuration()
        # self.mag = vn.read_magnetic_measurements() # not sure if this is compensated
        # self.temp =
        # self.pres = 
        # self.dtime = 
        # self.dtheta =  # looks like there's a function that reads
        # # both dtheta and dvel
        # self.dvel = vn.read_delta_theta_and_delta_velocity()
        # self.vpe_status = 
        # self.sync_in_cnt = 
        # self.sync_out_cnt = 


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
    
    def show_all_methods(self):
        return dir(self.vnsensor.read_delta_theta_and_delta_velocity())
    
    
# make a vnsensor object with self.vnsensor = VnSensor()
# connect that vnsensor object with self.vnsensor.connect(port, baudrate) 
# then I can start reading values


# obj = Test()
# # obj.generate_data()
# # print(obj.show_data())
# # print("\nRunning it all again \n\n\n")
# # obj.generate_data()
# # print(obj.show_data())
# print(obj.show_all_methods())


# s = VnSensor()

# s.connect('C0M1', 115200)
# print(dir(s.read_yaw_pitch_roll_magnetic_acceleration_and_angular_rates()))

