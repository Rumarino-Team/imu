#!/bin/bash

# This script will create a standard ROS Inertial Measurement Unit Package

# Script requirements: 
# - ROS Medolic
# - ROS standard workspace
# - A zip file of the vnprogramming library on the user's downloads directory.
# - pip3.

# Process of creating the ROS IMU PKG:

cd ~/catkin_ws/src # Change directory to your source directory of your standard catkin workspace
catkin_create_pkg imu rospy std_msgs geometry_msgs tf message_generation message_runtime # create the dvl package
cd ~/catkin_ws # change directory to your standard catkin workspace
catkin_make # compile workspace 
. ~/catkin_ws/devel/setup.bash # To add the workspace to your ROS environment you need to source the generated setup file

# Standard package process setup:

cd ~/catkin_ws/src/imu # change directory to the DVL pkg dir
touch run.sh& # Creates script that will run the client and server
touch README.md& # creates readme.md for the whole pacage director
echo -e "#Rumarino ROS Inertial Measurement Unit Package \nTODO: Document" >> README.md&
touch .gitignore

## Process of creating necessary directories for the package:

mkdir config& # used for .yaml files 
mkdir msg& # used for .msg files 
mkdir launch& # used for .launch files 
mkdir scripts # used for ros executable files 

## Process of creating initial files that are needed for this package:

## Setup of config Directory: 

cd config 
touch README.md # Creates readme.md for config directory

cd .. # change back 

## Setup of message Directory: 

cd msg
touch Raw_IMU.msg& # Creates .msg file for Raw DVL data
touch README.md # Creates readme.md for message directory

cd .. #change back 

## Setup of launch Directory: 

cd launch 
touch hydrus_imu.launch& # Creates .launch file for DVL component
touch README.md # Creates readme.md for launch directory

cd .. # change back

## Setup of scripts Directory: 

cd scripts 
mkdir Client

### Setup of Client Directory:
 
cd Client
touch __init__.py& # this indicates that this directory will be a python package
touch imu_client_node.py& # Creates the executable that the package will use
touch README.md # Creates readme.md for message directory

cd .. # change back
cd .. # change back

## Setup of Source Directory:

cd src 
touch README.md # Creates readme.md for source directory
mkdir lib # Directory that will hold libraries built by user or any programing library required.
cd lib 
touch README.md # Creates readme.md for lib directory
mkdir Server # Directory designated for anything that is related to the Server that will interface with the DVL 

### Setup of Server Directory: 

cd Server
touch __init__.py& # this indicates that this directory will be a python package
touch imu_connector.py&
touch imu_data.py& 
touch server.py&
touch requirements.txt&
touch start_serv&  
touch README.md # Creates readme.md for server directory

### Setup of Directory for the IMU Programming Library: 


cd ~/Downloads
unzip vnproglib.zip -d ~/catkin_ws/src/imu/src/lib
cd  ~/catkin_ws/src/imu/src/lib/vnproglib/python
pip3 install . # locally install python package

# Compile your catkin worskpace one last time:

cd ~/catkin_ws # change directory to your standard catkin workspace
catkin_make # compile workspace 

# Validation process:
cd
rospack depends1 imu # finally, check package dependacies 
