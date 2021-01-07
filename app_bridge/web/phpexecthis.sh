#!/bin/bash

export PYTHONPATH=$PYTHONPATH:/opt/ros/kinetic/lib/python2.7/dist-packages
export ROS_MASTER_URI=http://pSHiANg.local:11311
python app_color.py $1 $2
