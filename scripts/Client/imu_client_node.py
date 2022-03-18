#!/usr/bin/env python
# git kraken git pull request, git lenght


import rospy

from imu.msg import Raw_IMU 
from requests import get
from requests.exceptions import ConnectionError # this is needed so it wont throw an error when we do the except
from geometry_msgs.msg import Vector3, Quaternion

from tf.transformations import euler_from_quaternion

# WE NEED TO DO THE EULER CALCULATIONS ONCE WE GET HERE!!!! CALCULATIONS CANNOT BE DONE IN PYTHON3!!
vectors = ["ypr", "attitude", "imu_rate", "angular_rate", "acceleration", "imu_acceleration", "mag", "dtheta", "dvel" ]
letters = ["x", "y", "z", "w"]

class IMU_Node(object):
    BASE = "http://127.0.0.1:5000//imu"
    def __init__(self):
        rospy.init_node("imu_node", anonymous=True)
        
        self._pub = rospy.Publisher("/hydrus/IMU", Raw_IMU, queue_size=10) # data_class esta mal, you have to change this.
        self.imu_msg = Raw_IMU()
        self.rate = rospy.Rate(10)

    def get_data(self):
        # print(dir(self.imu_msg))
        server_response = get(self.BASE).json() # CRUCIAL: we turn it into a json BEFORE accessing its items. (not a dict before json())
        
        # # # now that server_response is a dictionary then we can see the attributes and its values by using server_response[ATTRIBUTE]
        
        # for attri in vectors:
        
        #     if attri == "attitude":
        #         for letter in letters: # iterate over the complete list
        #             setattr(self.imu_msg, attri+".{}".format(letter), server_response[attri+"_{}".format(letter)])
        #     elif attri in dir(self.imu_msg):
        #         for letter in letters[:3]:
        #             setattr(self.imu_msg, attri+".{}".format(letter), server_response(attri+"_{}".format(letter)))
                    
        self.imu_msg.ypr.x = server_response["ypr_x"]
        self.imu_msg.ypr.y = server_response["ypr_y"]
        self.imu_msg.ypr.z = server_response["ypr_z"]


        self.imu_msg.attitude.x = server_response['attitude_x']
        self.imu_msg.attitude.y = server_response['attitude_y']
        self.imu_msg.attitude.z = server_response['attitude_z']
        self.imu_msg.attitude.w = server_response['attitude_w']

        self.attitude = [self.imu_msg.attitude.x, self.imu_msg.attitude.y, self.imu_msg.attitude.z, self.imu_msg.attitude.w]

        self.orientation_x, self.orientation_y, self.orientation_z, self.orientation_w = list(euler_from_quaternion(self.attitude))


        self.imu_msg.accelaration.x = server_response['accelaration_x']
        self.imu_msg.accelaration.y = server_response['accelaration_y']
        self.imu_msg.accelaration.z = server_response['accelaration_z']

        self.imu_msg.imu_rate.x = server_response['imu_rate_x']
        self.imu_msg.imu_rate.y = server_response['imu_rate_y']
        self.imu_msg.imu_rate.z = server_response['imu_rate_z']

        self.imu_msg.imu_accelaration.x = server_response['imu_acceleration_x']
        self.imu_msg.imu_accelaration.y = server_response['imu_acceleration_y']
        self.imu_msg.imu_accelaration.z = server_response['imu_acceleration_z']

        self.imu_msg.mag.x = server_response['mag_x']
        self.imu_msg.mag.y = server_response['mag_y']
        self.imu_msg.mag.z = server_response['mag_z']

        self.imu_msg.dtheta.x = server_response['dtheta_x']
        self.imu_msg.dtheta.y = server_response['dtheta_y']
        self.imu_msg.dtheta.z = server_response['dtheta_z']

        self.imu_msg.dvel.x = server_response['dvel_x']
        self.imu_msg.dvel.y = server_response['dvel_y']
        self.imu_msg.dvel.z = server_response['dvel_z']


        # maybe hacer un for loop y a lo ultimo puedes hacer setattr(self.imu_msg, STRING.x, server_response[STRING_x])
        
        
        
        
        
        # for key , val in server_response.items(): # when we create it into a json() then it 'turns' from a response object to a dictionary
        #     if key in dir(self.imu_msg):
        #         setattr(self.imu_msg, key, val) # set the attribute of the object to the the value of the key.
        #         print("The imu message {0} contains: {1}".format(key, getattr(self.imu_msg, key))) # usamos el getattr para ver que realmente tiene el message
        # # print("Dir function: {}".format(dir(self.imu_msg)))# the dir function returns all of the methods and attributes of 
        # return self.publish_data(self.imu_msg) # so we have to make it a json() to not get 'response(200)
    
    def publish_data(self, server_data):
        self._pub.publish(self.imu_msg)
        return self.imu_msg



if __name__ == "__main__":
    try:
        imu_node = IMU_Node()
        # print(imu_node.get_data())
        while not(rospy.is_shutdown()):
            imu_node.get_data()
            

    except ConnectionError:
        print("Make sure that the server is currently running.")
