#!/usr/bin/env python
# git kraken git pull request, git lenght

import rospy

from imu.msg import Raw_IMU 
from requests import get
from requests.exceptions import ConnectionError # this is needed so it wont throw an error when we do the except
from geometry_msgs.msg import Vector3, Quaternion

from tf.transformations import euler_from_quaternion


class IMU_Node(object):
    BASE = "http://127.0.0.1:5000//imu"
    def __init__(self):
        rospy.init_node("imu_node", anonymous=True)
        
        self._pub = rospy.Publisher("/hydrus/IMU", Raw_IMU, queue_size=10) # data_class esta mal, you have to change this.
        self.imu_msg = Raw_IMU()
        self.rate = rospy.Rate(10)

    def get_data(self):
        print(dir())
        # server_response = get(self.BASE).json() # CRUCIAL: we turn it into a json BEFORE accessing its items. (not a dict before json())
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

        # while not(rospy.is_shutdown()):
        #     imu_node.get_data()
            

    except ConnectionError:
        print("Make sure that the server is currently running.")
