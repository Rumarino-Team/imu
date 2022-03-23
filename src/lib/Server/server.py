#!/usr/bin/env python3

"""Recommended Order to read and understand the IMU task:

1. imu_data.py 
2. imu_connetory.py 
3. server.py (YOU ARE HERE!) 
4. imu_client_node.py

"""



from flask import Flask, request, jsonify
# from imu_connector import Test
from Server.imu_connector import Test # Test is a subclass that contains the generate_data() function and show_data()
"""Adding 'Server" to the beginning of the export to symbolize the parent directory fixes the import module error 
whenever we run flask but it causes python3 interpreter to raise ModuleNotFound Error"""

# to switch from dummy to real one follow the checklist below:

# go to imu_connector.py:
# comment line 219 and uncomment line 220 (should be under show_data method)

app = Flask(__name__) # Creating an instance of the Flask object. Python sets '__name__' variable to the name of the module you are running. 

testing = Test() 

"""Help on the home() Function:

-> We use a decorator that refers to the 'app' variable which is actually an instance of the Flask object (line25) and set the ROUTE to 
        '/imu'. Whenever flask runs, it 'initalizes' the server using a BASE route which is: http://127.0.0.1:5000/ 
        
        When we pass '/imu' as an argument of route, we are telling the flask to CALL the home function if a request is sent to the 
        BASE route + /imu  --> 'http://127.0.0.1:5000//imu'. Notice how it literally is the BASE route with the /imu added to the end of said
        BASE route.
    
        The other argument is the http methods that will be supported. (This being GET)

-> HTTP method GET: The function will first determine what type of request the server is receiving from the client. The most common type of 
    request is GET which tells teh server that the client wants to request data from the http://127.0.0.1:5000//imu.

    Note: Everytime you refresh a page, the client (in this case, you) is sending a GET request to the server where it is requesting some data.

-> Lastly, the home function returns a json version of the passed vars(self) dictionary which contains the attributes and their respective values of the 
    testing instance of the Test object. (see information on show_data in the imu_connector.py script) A JSON is a lightweight form of data for storing 
    and transporting purposes. In this case, we create a JSON version of that dictionary to be able to view said data once we refresh the home function route
    and request it in the imu_client_node.py 

     """

@app.route("/imu", methods=["GET"])
def home():
    if request.method == "GET":
        return jsonify(testing.show_data())
    else:
        return "method not supported"


if __name__  == "__main__":
    app.run(debug=True)
     # not sure if we can pass args to FLask methods
