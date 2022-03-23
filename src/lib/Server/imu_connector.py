#!/usr/bin/env python3 

"""Recommended Order to read and understand the IMU task:

1. imu_data.py
2. imu_connetory.py (YOU ARE HERE!)
3. server.py
4. imu_client_node.py

"""
from Server.imu_data import IMU_DATA # this is the class that will be imported
from random import randint, uniform
from vnpy import VnSensor

# problem lies en que estamos passing vars(self) and one of the attributes is VnSensor() and that is not jsonserializable 

START_RANGE = 0
END_RANGE = 100
class Test(IMU_DATA): # this class inherites from the IMU_DATA
    """Help on the Test class:
    
    -> The first key concept of this Test class is that it INHERITS from the IMU_DATA class (the IMU_DATA class comes from the imported IMU_DATA.py).
    This inheritance is demonstrated with the declaration of the class: 

        class Test(IMU_DATA):
    
        Having '(IMU_DATA)' tells Python that the Test class is a CHILD of the PARENT IMU_DATA class

    -> The constructor or__init__ method of the Test class utilizes the super() Python function. This function allows us to directly access the 
    constructor method of the parent class since it gives the child class access to that method. In a way, having the super() method would have the same
    effect as copy pasting the IMU_DATA class constructor.
    """
    
    def __init__(self):
        super().__init__()


        # notice how we do not write 'self.vnsensor = VnSensor()'!
        
        # The reason why we do NOT do this is because this would mean that Test class instances would have an attribute named 'vnsesnor'
        # that holds a Class (VnSensor class in this case) as its value. The reason we want to avoid this is because in the imu_client_node.py
        # script, all of the attributes of the Test class instances will be displayed as a json and objects of the type class are NOT JSON SERIALIZABLE.

        # Since classes are not JSON serializable, Python will raise an error saying that it cannot convert a class into data that can be read from a 
        # web server (which is the purpose of JSON)
        
     
    """this function is an attempt to use the vnsensor object and to match the values of the sensor to the class
    the assignments are not done since further analysis of the API and its methods."""
    
    def generate_data(self): # reading real values here.
        """Help on the generate_data method:
        
        
        -> This method performs the 'link' or 'connection' process between the VnSensor object and the Test class. Notice how 
                all of the attributes being used for the Test class are attributes that were intialized in the IMU_DATA class 
                constructor. The 'link' process occurs by setting the Test class instance's  attributes
                to their respective read methods found in the VnSensor() class.
        
        -> The first thing that is performed is the definition of a VnSensor() object followed by connecting this object to the
                computer's '/dev/ttyUSB0' port (this is a physical port in the computer that MUST be connected to an IMU in order to
                receive values.) These values are received by the Test class utilizing the VnSensor 'read' methods (link or connection
                process described above) [to view the ports, enter a linux terminal and write 'ls /dev/tty*', the USB0 port will only appear
                if you have something connected to that port while executing the command in the terminal.]
                
        -> KEY CONCEPT: 
            -> Some of the values received in from the 'read methods' of the VnSensor object are actually Vector3's or Quaternions.
            In simplest terms: 
            Vector3 is a data structure that holds 3 floats. These floats are accessed using '.x', '.y', '.z' depepnding on which 
            values you want in 3D space (values being x,y,z)
            
            Quaternion is similar to a Vector3 but it holds 4 floats instead of 3. A quaternion uses the same dot notation with the addition
            of the fourth valeus which is accessed with '.w'. (values are: x,y,z,w)"""
        vs = VnSensor() 
        vs.connect('/dev/ttyUSB0', 115200) # this function takes the port and baudrate (speed of data transmission) as arguments 
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

        self.imu_acceleration_x = vs.read_imu_measurements().accel.x 
        self.imu_acceleration_y = vs.read_imu_measurements().accel.y
        self.imu_acceleration_z = vs.read_imu_measurements().accel.z 

         
        self.imu_rate_x= vs.read_imu_measurements().gyro.x  
        self.imu_rate_y= vs.read_imu_measurements().gyro.y 
        self.imu_rate_z= vs.read_imu_measurements().gyro.z

        
        self.mag_x = vs.read_imu_measurements().mag.x
        self.mag_y = vs.read_imu_measurements().mag.y
        self.mag_z = vs.read_imu_measurements().mag.z

        self.temp = vs.read_imu_measurements().temp
        

        self.pres = vs.read_imu_measurements().pressure
        self.dtime = vs.read_delta_theta_and_delta_velocity().delta_time

        
        self.dtheta_x = vs.read_delta_theta_and_delta_velocity().delta_theta.x
        self.dtheta_y = vs.read_delta_theta_and_delta_velocity().delta_theta.y
        self.dtheta_z = vs.read_delta_theta_and_delta_velocity().delta_theta.z

        self.dvel_x = vs.read_delta_theta_and_delta_velocity().delta_velocity.x
        self.dvel_y = vs.read_delta_theta_and_delta_velocity().delta_velocity.y
        self.dvel_z = vs.read_delta_theta_and_delta_velocity().delta_velocity.z
        # self.vpe_status = randint(START_RANGE, END_RANGE)
        # self.sync_in_cnt = randint(START_RANGE, END_RANGE)
        # self.sync_out_cnt = randint(START_RANGE, END_RANGE)
        print(vars(self)) # DEBUGGING PURPOSES ONLY. printing all of the attributes of the object that was generated. 
    
    def generate_RANDOM_data(self): # generate dummy values here
        """Help on the generate_RANDOM_data method:
        
        -> this method is to be ONLY used when you are NOT connected to the IMU. The purpose of this method is solely for testing
        purposes since it generates random values from range 0-100. Notice how we do NOT have to create a VnSensor object since we never 
        have to read from the IMU."""
        self.time_startup = randint(START_RANGE, END_RANGE)
        self.time_sync_in = randint(START_RANGE, END_RANGE)
        
        self.ypr_x = uniform(START_RANGE, END_RANGE)
        self.ypr_y = uniform(START_RANGE, END_RANGE)
        self.ypr_z = uniform(START_RANGE, END_RANGE)

        self.attitude_x = uniform(START_RANGE, END_RANGE)
        self.attitude_y = uniform(START_RANGE, END_RANGE)
        self.attitude_z =uniform(START_RANGE, END_RANGE)
        self.attitude_w =uniform(START_RANGE, END_RANGE)
    
    
         # attitude son 4 valores (quaternion)
        self.orientation_x = uniform(START_RANGE, END_RANGE)
        self.orientation_y = uniform(START_RANGE, END_RANGE)
        self.orientation_z = uniform(START_RANGE, END_RANGE)
        self.orientation_w = uniform(START_RANGE, END_RANGE)

        self.angular_rate_x = uniform(START_RANGE, END_RANGE)
        self.angular_rate_y = uniform(START_RANGE, END_RANGE)
        self.angular_rate_z = uniform(START_RANGE, END_RANGE)

        self.imu_acceleration_x = uniform(START_RANGE, END_RANGE)
        self.imu_acceleration_y = uniform(START_RANGE, END_RANGE)
        self.imu_acceleration_z = uniform(START_RANGE, END_RANGE)


        
        self.acceleration_x = uniform(START_RANGE, END_RANGE)
        self.acceleration_y = uniform(START_RANGE, END_RANGE)
        self.acceleration_z = uniform(START_RANGE, END_RANGE)


        self.imu_rate_x= uniform(START_RANGE, END_RANGE) #check if this is the rate
        self.imu_rate_y= uniform(START_RANGE, END_RANGE) # verificar si se hace esto mismo con imu_acceleration de arriba
        self.imu_rate_z= uniform(START_RANGE, END_RANGE)

        self.mag_x = uniform(START_RANGE, END_RANGE)
        self.mag_y = uniform(START_RANGE, END_RANGE)
        self.mag_z = uniform(START_RANGE, END_RANGE)
        

        self.temp = uniform(START_RANGE, END_RANGE)
        self.pres = uniform(START_RANGE, END_RANGE)
        self.dtime = uniform(START_RANGE, END_RANGE)


        self.dtheta_x = uniform(START_RANGE, END_RANGE)
        self.dtheta_y = uniform(START_RANGE, END_RANGE)
        self.dtheta_z = uniform(START_RANGE, END_RANGE)

        self.dvel_x = uniform(START_RANGE, END_RANGE)
        self.dvel_y = uniform(START_RANGE, END_RANGE)
        self.dvel_z = uniform(START_RANGE, END_RANGE)


        self.dvel = uniform(START_RANGE, END_RANGE)
        self.vpe_status = randint(START_RANGE, END_RANGE)
        self.sync_in_cnt = randint(START_RANGE, END_RANGE)
        self.sync_out_cnt = randint(START_RANGE, END_RANGE)

    def show_data(self): # this is the method that gets called from the server.
        """Help onthe show_data method:
        
        -> This is the method that gets called from the server. Inside this method, the generate_data method is called to perfrom the 'connection' process
        between the Test class instance's attributes and the VnSensor read methods (view the help section on generate_data method for more information)

        
        
        -> Notice how this method returns 'vars(self)'. This returns a dictionary that contains the attributes and their respective values. A dictionary
        is the optimal data structure for this task since it is JSON Serializable (being JSON Serializable means that the object that's passsed can be 
        converted into a string) and can be displayed as text by the web server. 

        -> One final note: 
            The generate_RANDOM_data method is commented out to allow for a fast transition between running the task with dummy values and running it with 
            actual values read from the IMU.
        
        """
        
        self.generate_data() 
        # self.generate_RANDOM_data() # comment this to run the real one
        return vars(self)
    
    def show_all_methods(self):
        return dir(self.vnsensor.read_delta_theta_and_delta_velocity())
    
    


