#!/usr/bin/env python3 
"""Recommended Order to read and understand the IMU task:

1. imu_data.py (YOU ARE HERE!) 
2. imu_connetory.py 
3. server.py
4. imu_client_node.py

"""

class IMU_DATA: 
    """help on IMU_DATA CLASS:
    
    -> the purpose of this class is to be able to create a wrapper around the existing VnSensor class and its read methods that are used
    to retrieve data from the IMU. For example, the VnSensor class has a method named 'read_angular_rate_measurements()' and our job is to
    create a class that contains the attribute 'angular_rate' so it can be easier to obtain the desired attributes from a created object of 
    the IMU_DATA class. In this case, by simply using dot notation we will be able to retrieve the angular_rate attribute of the IMU sensor
    
    -> In the case that we would like to retrieve an attribute that is NOT in the IMU_DATA class, we would simply add the desired attribute's
    name and in imu_connector.py script you would have to add the 'read' method corresponding to the VnSensor class (this method is what retrieves
    the actual value) and 'link' or 'make the connection' between the IMU_DATA object's attribute and the read method of the VnSensor
    
    Example of the link or connection described above:
    
    self.angular_rate_x = VnSensor().read_angular_rate_measurements().x
    
    -> In reality, this IMU_DATA class will be imported into the imu_connector.py script and there we will create another class that INHERITS from 
    this IMU_DATA class. This allows us to separate the 'defining phase' of the class attributes (would be the class initializer or constructor) from
    the 'linking' or 'connection' process that was described above."""

# Method that initializes everything to none so we can set a new value once we perform the 'link' process to the VnSensor read method.
    def __init__(self , time_startup = None, time_sync_in = None, ypr_x = None, ypr_y = None, ypr_z = None, attitude_x = None, attitude_y = None, 
    attitude_z = None, attitude_w = None, orientation_x = None, orientation_y = None, orientation_z=None, 
    angular_rate_x = None, angular_rate_y = None,angular_rate_z = None ,acceleration_x = None,acceleration_y = None,acceleration_z = None,
    imu_acceleration_x = None, imu_acceleration_y= None, imu_acceleration_z=None, imu_rate_x = None, imu_rate_y=None, imu_rate_z=None, mag_x = None, mag_y = None, mag_z = None, 
    temp = None,pres = None,dtime = None, dtheta_x = None, dtheta_y = None, dtheta_z = None, dvel_x = None, dvel_y = None, dvel_z = None, vpe_status = None,sync_in_cnt = None, sync_out_cnt = None, imu_dict_data = None):

        self.time_startup: int = time_startup
        self.time_sync_in: int = time_sync_in
        self.ypr_x: float = ypr_x
        self.ypr_y = ypr_y
        self.ypr_z = ypr_z


        self.attitude_x: float = attitude_x
        self.attitude_y = attitude_y
        self.attitude_z = attitude_z
        self.attitude_w = attitude_w

        

       



        self.angular_rate_x = angular_rate_x, # vector 3 so we need 3 values
        self.angular_rate_y = angular_rate_y
        self.angular_rate_z = angular_rate_z
    

        self.orientation_x = orientation_x
        self.orientation_y = orientation_y
        self.orientation_z = orientation_z
        

        self.acceleration_x : float=  acceleration_x
        self.acceleration_y : float=  acceleration_y
        self.acceleration_z : float=  acceleration_z


        

        self.imu_acceleration_x: float = imu_acceleration_x
        self.imu_acceleration_y: float = imu_acceleration_y
        self.imu_acceleration_z: float = imu_acceleration_z

        self.imu_rate_x: float = imu_rate_x
        self.imu_rate_y: float = imu_rate_y
        self.imu_rate_z: float = imu_rate_z
    

        self.mag_x: float = mag_x
        self.mag_y: float = mag_y
        self.mag_z: float = mag_z
        

        self.temp: float = temp
        self.pres: float = pres

        self.dtime: float = dtime


        self.dtheta_x: float = dtheta_x
        self.dtheta_y: float = dtheta_y
        self.dtheta_z: float = dtheta_z


        self.dvel_x: float = dvel_x
        self.dvel_y: float = dvel_y
        self.dvel_z: float = dvel_z
        

        self.vpe_status: int = vpe_status
        self.sync_in_cnt: int = sync_in_cnt
        self.sync_out_cnt: int = sync_out_cnt

# if there is any problem when using one of the values , check the type. 

        if imu_dict_data:
         self.prepare_data(imu_dict_data)

    """Help on get_all_var_names method:
    
    -> this method utilizes the built-in python function named vars (which returns a dictionary of the attributes of the object and their value) 
    and use .keys() to only return the keys of the dictionary (keys of the vars produced dictionary would be the attribute names) and then create
    a list containing those attribute names.
    
    example output:
    
    [time_startup, time_sync_in, ypr_x, ypr_y ...]
    
    Note: '...' symbolizes the rest of the output (would be the rest of attributes of the IMU_DATA class"""
    @staticmethod
    def get_all_var_names_ls():
        return list(vars(IMU_DATA()).keys())


if __name__=='__main__':
    print('IMU_DATA Test Variable Names:')
    print(IMU_DATA.get_all_var_names_ls())


