#!/usr/bin/env python3 

# from geometry_msgs.msg import Vector3
# from imu.msg import Raw_IMU

# from tf.transformations import euler_from_quaternion # todo lo que sea ROS tiene que ocurrir en el node!!
class IMU_DATA: 

#Method that initializes everything to none so we can set a new value
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

        

        # self.orientation_x, self.orientation_y, self.orientation_w = list(euler_from_quaternion(self.attitude))# esto es una lista que se pasa como parametro.

# NECESITO saber como es qe se ve lo de orientation para saber como se va a estructurar 

        self.angular_rate_x = angular_rate_x, # vector 3 so we need 3 values
        self.angular_rate_y = angular_rate_y
        self.angular_rate_z = angular_rate_z
    

        
        
        

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

    def prepare_data(self, imu_dict: dict):
        for key in vars(self).keys():
             if key in imu_dict:
                setattr(self, key , imu_dict[key])

    def clear_data(self):
        for key in vars(self).keys():
            setattr(self, key , None)


    @staticmethod
    def get_all_var_names_ls():
        return list(vars(IMU_DATA()).keys())


if __name__=='__main__':
    print('IMU_DATA Test Variable Names:')
    print(IMU_DATA.get_all_var_names_ls())


