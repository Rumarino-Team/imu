#!/usr/bin/env python3 
# # this file should be in python 3
"""Here we will import the class and begin to generate random values while setting the class attributes to those random values"""
# from imu_data import IMU_DATA  # this line only works when we run python3 in the terminal
from Server.imu_data import IMU_DATA # this is the class that will be imported
from random import randint, uniform
from vnpy import VnSensor



START_RANGE = 0
END_RANGE = 100
class Test(IMU_DATA): # this class inherites from the IMU_DATA
    def __init__(self):
        super().__init__(IMU_DATA)

        self.vnsensor = VnSensor()
        self.vnsensor.connect('/dev/tty/USB0', 115200) # docu dice que necesito port, baudrate as arguments
     
    """this function is an attempt to use the vnsensor object and to match the values of the sensor to the class
    the assignments are not done since further analysis of the API and its methods."""
    
    def generate_data(self): # reading real values here.
        # self.ypr = Quaternion()
        vs = self.vnsensor
        # self.time_startup = randint(START_RANGE, END_RANGE)
        # self.time_sync_in = randint(START_RANGE, END_RANGE)
        
        

        self.ypr_x = vs.read_yaw_pitch_roll_magnetic_acceleration_and_angular_rates().yaw_pitch_roll.x
        self.ypr_y = vs.read_yaw_pitch_roll_magnetic_acceleration_and_angular_rates().yaw_pitch_roll.y
        self.ypr_z = vs.read_yaw_pitch_roll_magnetic_acceleration_and_angular_rates().yaw_pitch_roll.z

        # self.attitude = uniform(START_RANGE, END_RANGE) # attitude son 4 valores (quaternion)
        self.attitude_x = vs.read_attitude_quaternion().x
        self.attitude_y = vs.read_attitude_quaternion().y
        self.attitude_z =vs.read_attitude_quaternion().z
        self.attitude_w =vs.read_attitude_quaternion().w

        self.angular_rate_x = vs.read_angular_rate_measurements().x
        self.angular_rate_y = vs.read_angular_rate_measurements().y
        self.angular_rate_z = vs.read_angular_rate_measurements().z
        

        self.acceleration_x = vs.read_acceleration_measurements().x
        self.acceleration_y = vs.read_acceleration_measurements().y
        self.acceleration_z = vs.read_acceleration_measurements().z

        self.imu_accelaration_x = vs.read_imu_measurements().accel # se SUPONE QUE ESTO SEA UN VECTOR 3 (que tenga 3 valores ASK!!!!!!!111)
        self.imu_rate= vs.read_imu_measurements().gyro   #check if this is the rate
        
        """Lo de mag yo lo hice y no se si se puede hacer lo de ponerle la x,y,z al final."""
        self.mag_x = vs.read_imu_measurements().mag.x
        self.mag_y = vs.read_imu_measurements().mag.y
        self.mag_z = vs.read_imu_measurements().mag.z

        self.temp = vs.read_imu_measurements().temp
        self.temp = vs.read_imu_measurements().temp
        self.temp = vs.read_imu_measurements().temp

        self.pres = vs.read_imu_measurements().pressure
        self.dtime = vs.read_delta_theta_and_delta_velocity().delta_time

        """FALTA HACERLE LO DEL VECTOR3  CON DTHETA Y DVEL"""
        self.dtheta_x = vs.read_delta_theta_and_delta_velocity().delta_theta.x
        self.dtheta_y = vs.read_delta_theta_and_delta_velocity().delta_theta.y
        self.dtheta_z = vs.read_delta_theta_and_delta_velocity().delta_theta.z

        self.dvel_x = vs.read_delta_theta_and_delta_velocity().delta_velocity.x
        self.dvel_y = vs.read_delta_theta_and_delta_velocity().delta_velocity.y
        self.dvel_z = vs.read_delta_theta_and_delta_velocity().delta_velocity.z
        # self.vpe_status = randint(START_RANGE, END_RANGE)
        # self.sync_in_cnt = randint(START_RANGE, END_RANGE)
        # self.sync_out_cnt = randint(START_RANGE, END_RANGE)
    
    def generate_RANDOM_data(self): # generate dummy values here
        # self.ypr = Quaternion()
        self.time_startup = randint(START_RANGE, END_RANGE)
        self.time_sync_in = randint(START_RANGE, END_RANGE)
        
        self.ypr_x = uniform(START_RANGE, END_RANGE)
        self.ypr_y = uniform(START_RANGE, END_RANGE)
        self.ypr_z = uniform(START_RANGE, END_RANGE)

        self.attitude = uniform(START_RANGE, END_RANGE) # attitude son 4 valores (quaternion)
        self.orientation_x = uniform(START_RANGE, END_RANGE)
        self.orientation_y = uniform(START_RANGE, END_RANGE)
        self.orientation_z = uniform(START_RANGE, END_RANGE)
        self.orientation_w = uniform(START_RANGE, END_RANGE)

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

    def show_data(self): # this is the function that gets called from the server.
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

