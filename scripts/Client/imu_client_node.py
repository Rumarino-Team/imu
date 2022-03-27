#!/usr/bin/env python

"""Recommended Order to read and understand the IMU task:

1. imu_data.py 
2. imu_connetory.py 
3. server.py 
4. imu_client_node.py (YOU ARE HERE!) 

"""



import rospy

from imu.msg import Raw_IMU 
from requests import get
from requests.exceptions import ConnectionError # this is needed so it wont throw an error when we do the except
from geometry_msgs.msg import Vector3, Quaternion

from tf.transformations import euler_from_quaternion

# ignore the vectors and letters list (they are commented out)
# WE NEED TO DO THE EULER CALCULATIONS ONCE WE GET HERE!!!! CALCULATIONS CANNOT BE DONE IN PYTHON3!!
# vectors = ["ypr", "attitude", "imu_rate", "angular_rate", "acceleration", "imu_acceleration", "mag", "dtheta", "dvel" ]
# letters = ["x", "y", "z", "w"]

class IMU_Node(object):
    """Help on the IMU_Node Class:
    
    -> creating a class varaible named BASE that holds the BASE route of needed to access the Flask server and execute the GET request (see server.py for more information)
    
    __init__ method:
    
    -> Initialization of ROS node followed by creation of ROS publisher passing as arguments the following (topic_name, type_of_msg, queue size)
    
    -> Next, we create an instance of the Raw_IMU() object to refer to said instance and set its values to the values being received from the flask server. """
    BASE = "http://127.0.0.1:5000//imu"
    def __init__(self):
        rospy.init_node("imu_node", anonymous=True)
        
        self._pub = rospy.Publisher("/hydrus/IMU", Raw_IMU, queue_size=10) # data_class esta mal, you have to change this.
        self.imu_msg = Raw_IMU()
        self.rate = rospy.Rate(10)

    def get_data(self):
        """Help on the get_data method:
        
        -> Utilizing the 'get' function that was imported from the requests module (see import statements on top) we are able to retrieve the server
        data by passing in the base route being: http://127.0.0.1:5000//imu (connects to server and executes the get method in which the server will
        return the show_data method of the Test class)
        
        ->SERVER_RESPONSE VARIABLE: Notice how we perform the get function FIRST and then turn what was received from the get method to a JSON. This is done since we want to turn 
        the requested data to a dictionary (using .json()) to be able to access the server response.
        
        -> After creating the server_response variable which returns a dictionary that contains all of the attributes as keys and their respective values, we can 
        begin to set the IMU_MSG object's attributes (which is the ROS MESSAGE) to the respective key of the server_reponse dictionary
        
            example:
            
            self.imu_msg.ypr.x = server_response["ypr_x"] 
            
            --> Here the left side represents the attribute of the IMU_MSG that we want to set. We set said attribute to the VALUE of the KEY named 'ypr_x'. 
            Remember that this dictionary is an exact copy of the vars(self) of the Test class (or IMU_DATA class) This copycomes from the server which in 
            turn comes from the show_data method inside the Test class.  """
        
        # print(dir(self.imu_msg))
        server_response = get(self.BASE).json() # CRUCIAL: we turn it into a json BEFORE accessing its items. (not a dict before json())
        
        print("The server response is: ", server_response)
        # # # now that server_response is a dictionary then we can see the attributes and its values by using server_response[ATTRIBUTE]
        # vectors = ["ypr", "attitude", "imu_rate", "angular_rate", "acceleration", "imu_acceleration", "mag", "dtheta", "dvel" ]
        # letters = ["x", "y", "z", "w"]
        
        # for attri in vectors:
        #     for letter in letters: # iterate over the complete list
        #             if (letter == "w" and attri != "attitude"): # since only attitude is a quaternion, then attitude is the only one allowed to use 'w'.
        #                 continue
                    
        #             else:
        #                 display_imu_msg_attri = attri+"."+letter # THIS VAR is for debugging purposes only. (to be printed on line 39)
        #                 display_server_attri = attri+"_"+letter
        #                 print("DEBUGGING PRINT MESSAGE: Setting {} imu_msg attribute to the value of {}".format(display_imu_msg_attri, display_server_attri))

        #                 setattr(self.imu_msg, attri+".{}".format(letter), server_response[attri+"_{}".format(letter)]) 
        
            # elif attri in dir(self.imu_msg):
            #     for letter in letters[:3]:
            #         display_imu_msg_attri = attri+"."+letter
            #         display_server_attri = attri+"_"+letter
            #         print("DEBUGGING PRINT MESSAGE: Setting {} imu_msg attribute to the value of {}".format(display_imu_msg_attri, display_server_attri))
            #         setattr(self.imu_msg, attri+".{}".format(letter), server_response[attri+"_{}".format(letter)])
                    
            
        self.imu_msg.ypr.x = server_response["ypr_x"]
        self.imu_msg.ypr.y = server_response["ypr_y"]
        self.imu_msg.ypr.z = server_response["ypr_z"]


        self.imu_msg.attitude.x = server_response['attitude_x']
        self.imu_msg.attitude.y = server_response['attitude_y']
        self.imu_msg.attitude.z = server_response['attitude_z']
        self.imu_msg.attitude.w = server_response['attitude_w']

        self.attitude = [self.imu_msg.attitude.x, self.imu_msg.attitude.y, self.imu_msg.attitude.z, self.imu_msg.attitude.w] # this self.attitude
        # attribute creates a list and references that same list ALWAYS!! if you change the values of self.imu_msg.attitude.x, the list will NOT update.

        self.imu_msg.orientation.x, self.imu_msg.orientation.y, self.imu_msg.orientation.z = list(euler_from_quaternion(self.attitude))


        self.imu_msg.acceleration.x = server_response['acceleration_x']
        self.imu_msg.acceleration.y = server_response['acceleration_y']
        self.imu_msg.acceleration.z = server_response['acceleration_z']

        self.imu_msg.angular_rate.x = server_response['angular_rate_x']
        self.imu_msg.angular_rate.y = server_response['angular_rate_y'] # added this part... testing.
        self.imu_msg.angular_rate.z = server_response['angular_rate_z']

        self.imu_msg.imu_rate.x = server_response['imu_rate_x']
        self.imu_msg.imu_rate.y = server_response['imu_rate_y']
        self.imu_msg.imu_rate.z = server_response['imu_rate_z']

        self.imu_msg.imu_acceleration.x = server_response['imu_acceleration_x']
        self.imu_msg.imu_acceleration.y = server_response['imu_acceleration_y']
        self.imu_msg.imu_acceleration.z = server_response['imu_acceleration_z']

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
    
    def publish_data(self): # I removed a parameter called server_data of this function.
        self._pub.publish(self.imu_msg)
        return self.imu_msg



if __name__ == "__main__":
    try:
        imu_node = IMU_Node()
        # print(imu_node.get_data())
        while not(rospy.is_shutdown()):
            imu_node.get_data()
            imu_node.publish_data()
            imu_node.rate.sleep() # not sure about this line. check later.
            

    except ConnectionError:
        print("Make sure that the server is currently running.")
