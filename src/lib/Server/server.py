#!/usr/bin/env python3
# from vnproglib.python.vnpy import VnSensor



from flask import Flask, request, jsonify
# from imu_connector import Test
from Server.imu_connector import Test # Test is a subclass that contains the generate_data() function and show_data()
"""Adding 'Server" to the beginning of the export to symbolize the parent directory fixes the import module error 
whenever we run flask but it causes python3 interpreter to raise ModuleNotFound Error"""

# to switch from dummy to real one follow the checklist below:

# go to imu_connector.py:
# uncomment lines 17-18 (if u want to run real one)
# comment line 143 and uncomment line 142
app = Flask(__name__)

testing = Test()


"""lo voy a configurar de una manera de que cada vez que tu hagas
un GET al server (darle refresh al link) siempre va a llamar a una funcion
de show_data y DENTRO de la funcion de show_data se va a generar el dummy data."""

@app.route("/imu", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return jsonify(testing.show_data())
    else:
        return "method not supported"


if __name__  == "__main__":
    app.run(debug=True)
     # not sure if we can pass args to FLask methods
