#!/usr/bin/env python
# git kraken git pull request, git lenght
import rospy

from imu.msg import Raw_IMU 
from requests import get



class IMU_Node(object):
    BASE = "http://127.0.0.1:5000//imu"
    def __init__(self):
        # rospy.init_node("imu_node")
        pass
        # self._pub = rospy.Publisher("/hydrus/IMU", data_class, queue_size=10) # data_class esta mal, you have to change this.
    
        # self._pub.publish(imu_msg)

    def get_data(self):
        server_response = get(self.BASE)
        return server_response.json() # so we have to make it a json() to not get 'response(200)


if __name__ == "__main__":
    
    imu_node = IMU_Node()

    data = imu_node.get_data()
    print(data)


    
# hacerle un try except con el error code Connection Error