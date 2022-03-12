#!/usr/bin/env python3
# from vnproglib.python.vnpy import VnSensor

from vnpy import VnSensor

from flask import Flask, request, jsonify
# vnsensor = VnSensor()
# data = vnsensor.read_binary_output_1()
app = Flask(__name__)
data = {"name": "Jose", "integer": 56}

@app.route("/imu", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return jsonify(data)
    else:
        return "method not supported"