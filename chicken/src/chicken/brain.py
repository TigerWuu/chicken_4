#!/usr/bin/env python
import rospy
from time import time
from std_msgs.msg import String
from std_msgs.msg import Float32

dis_l = 0
dis_r = 0
dis_m = 0
dis_ul = 0
dis_ur = 0
mode="ball"
center_dist = 0

def action():
    global dis_l , dis_m , dis_r , dis_r , dis_r , center_dist ,mode
    orientation = "F"
    # if mode == "ball":
    #     if int(center_dist[2]) < 100:   # area < bias use the ultrasound info 
    #         if dis_l < dis_r - 10:
    #             orientation = "L"
    #         elif dis_r < dis_l - 10:
    #             orientation = "R"
    #         elif dis_l < 5 and dis_r < 5:
    #             orientation = "S"
    #         else:
    #             orientation = "F"
    #     elif int(center_dist[0]) > 350:
    #         orientation = "R"
    #     elif int(center_dist[0]) < 290:
    #         orientation = "L"
    #     else:
    #         orientation = "F"
    # else:
    #     if int(center_dist[2]) > 100:  
    #         orientation = "S"
    #     elif int(center_dist[0]) > 350:
    #         orientation = "R"
    #     elif int(center_dist[0]) < 290:
    #         orientation = "L"
    #     else:
    #         orientation = "F"

    #     # avoid 
    #     if dis_ul < dis_ur - 10:
    #         avoid_action("R")
    #     elif dis_ur < dis_ul - 10:
    #         avoid_action("L")
    #     else:
    #         orientation = "F"
    Body.publish(orientation)

def avoid_action(orient):
    if orient == "L":     #turn left
        action_serial = ["L","F","R","F","R","F","L"]
    else:
        action_serial = ["R","F","L","F","L","F","R"]

    for i in action_serial:
        Body.publish(orientation)
        sleep(1)

def image_get(image_data):
    global center_dist
    center_dist = image_data.data
    center_dist = center_dist.split("," , 2)

def ultrasound_get_l(dis_data):
    global dis_l  
    dis_l = dis_data.data

def ultrasound_get_r(dis_data):
    global dis_r 
    dis_r = dis_data.data

def ultrasound_get_m(dis_data):
    global dis_m 
    dis_m = dis_data.data

def ultrasound_get_ul(dis_data):
    global dis_ul 
    dis_ul = dis_data.data

def ultrasound_get_ur(dis_data):
    global dis_ur
    dis_ur = dis_data.data

def mode_get(data):
    global mode
    mode = data.data


if __name__ == "__main__":
    rospy.init_node("brain")
    Body = rospy.Publisher("car_info" , String ,queue_size = 10)

    rospy.Subscriber("mode" , String , mode_get)
    rospy.Subscriber("image_info" , String , image_get)
    rospy.Subscriber("ultrasound_info_l" , Float32 , ultrasound_get_l)
    rospy.Subscriber("ultrasound_info_r" , Float32 , ultrasound_get_r)
    rospy.Subscriber("ultrasound_info_m" , Float32 , ultrasound_get_m)
    rospy.Subscriber("ultrasound_info_ul" , Float32 , ultrasound_get_ul)
    rospy.Subscriber("ultrasound_info_ur" , Float32 , ultrasound_get_ur)

    while not rospy.is_shutdown():
        action()
