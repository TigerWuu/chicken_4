#!/usr/bin/env python
import cv2
import numpy as np
import rospy
from std_msgs.msg import String
 
ball = None
home = None
mode = "ball"

def green(a):
    vis=cv2.cvtColor(a,cv2.COLOR_BGR2HSV)
    lower_green=np.array([35,43,46])
    upper_green=np.array([77,255,255])
    kernel=np.ones((15,15),np.uint8)
    mask_green=cv2.inRange(vis, lower_green,upper_green)
    mask_green_op=cv2.morphologyEx(mask_green, cv2.MORPH_OPEN, kernel)
    return mask_green_op
def yellow(a):
    vis=cv2.cvtColor(a,cv2.COLOR_BGR2HSV)
    lower_yellow=np.array([26,43,46])
    upper_yellow=np.array([34,255,255])
    kernel=np.ones((15,15),np.uint8)
    mask_yellow=cv2.inRange(vis, lower_yellow,upper_yellow)
    mask_yellow_op=cv2.morphologyEx(mask_yellow, cv2.MORPH_OPEN, kernel)
    return mask_yellow_op
def orange(a):
    vis=cv2.cvtColor(a,cv2.COLOR_BGR2HSV)
    lower_orange=np.array([11,43,46])
    upper_orange=np.array([25,255,255])
    kernel=np.ones((15,15),np.uint8)
    mask_orange=cv2.inRange(vis, lower_orange,upper_orange)
    mask_orange_op=cv2.morphologyEx(mask_orange, cv2.MORPH_OPEN, kernel)
    return mask_orange_op
def blue(a):
    vis=cv2.cvtColor(a,cv2.COLOR_BGR2HSV)
    lower_blue=np.array([78,43,46])
    upper_blue=np.array([99,255,255])
    kernel=np.ones((15,15),np.uint8)
    mask_blue=cv2.inRange(vis, lower_blue,upper_blue)
    mask_blue_op=cv2.morphologyEx(mask_blue, cv2.MORPH_OPEN, kernel)
    return mask_blue_op
def red(a):
    vis=cv2.cvtColor(a,cv2.COLOR_BGR2HSV)
    lower_red=np.array([0,43,46])
    upper_red=np.array([10,255,255])
    mask_red0=cv2.inRange(vis, lower_red,upper_red)
    lower_red=np.array([156,43,46])
    upper_red=np.array([180,255,255])
    mask_red1=cv2.inRange(vis, lower_red,upper_red)
    mask_red=mask_red0+mask_red1
    kernel=np.ones((15,15),np.uint8)
    mask_red_op=cv2.morphologyEx(mask_red, cv2.MORPH_OPEN, kernel)
    return mask_red_op

def ball_color(msg):
    global ball 
    ball = msg.data

def home_color(msg):
    global home 
    home = msg.data
    
def mode_get(msg):
    global mode
    mode = msg.data

def takepic():
    rospy.init_node("webcame" ,anonymous = True)
    rate = rospy.Rate(10)
    cX=0
    cY=0
    cap=cv2.VideoCapture(0)
    while not rospy.is_shutdown():
        global ball,home,mode
        
        if mode == "ball":
            color = ball
        else:
            color = home

        if color == "Green":
            _, cnts, _ = cv2.findContours(green(vid), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        elif color == "Yellow":
            _, cnts, _ = cv2.findContours(yellow(vid), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        elif color == "Purple":
            _, cnts, _ = cv2.findContours(orange(vid), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)   ##orange or purple ?????
        elif color == "Blue":
            _, cnts, _ = cv2.findContours(blue(vid), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        elif color == "red":
            _, cnts, _ = cv2.findContours(red(vid), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        else:
            continue
        ret, img = cap.read()
        vid=img.copy()

        _, cnts, _ = cv2.findContours(yellow(vid), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours_ball = cv2.drawContours(vid, cnts, -1,(0,0,255),5)
        area=0
        
        for c in cnts:
            M = cv2.moments(c)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cent=cv2.circle(vid, (cX, cY), 10, (1, 227, 254), -1)

            area=cv2.contourArea(c)
        
        image_info = str(cX) + "," + str(cY) + "," + str(int(area))
       
        cam = rospy.Publisher("image" , String ,queue_size = 10)
        rospy.Subscriber("ball_color", String, ball_color)
        rospy.Subscriber("home_color", String, home_color)
        rospy.Subscriber("mode", String, mode_get)

        cam.publish(image_info)

        rospy.spin()
        rate.sleep()
    cap.release()
if __name__ == '__main__':
    try:
        takepic()
    except rospy.ROSInterruptException:
        print("webcame.py has trouble!!!!!!!!1")

