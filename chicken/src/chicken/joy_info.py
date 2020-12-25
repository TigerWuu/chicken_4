#! /usr/bin/env python
import rospy
from std_msgs.msg import String, Int16
from sensor_msgs.msg import Joy
import os
import json
count2 = 0     #mode 
count = 0      #mode 0~1
mode = 0
diff = 1       #1~9

other_mode = 0

HZ=4


def joy_remapping(msg):
    global count, mode, diff, count2
    buttons = msg.buttons
    axes = msg.axes
    axes = map(lambda x:int(x*100),axes)  
    LR,UD,_,_,_,_ = axes 
    X,A,B,Y,LB,RB,_,_,back,start,_,_=buttons       
    if back == 1:        ## press back to shutdown
    	p = os.popen('shutdown now')
    
    rate = rospy.Rate(HZ)
    
    if LR>0:
    	left=LR
    	right=0
    else:
   	    left=0
    	right=-LR

    if UD>0:
        up=UD
        if left > 0:
            R_v = up
            L_v = left
        else:
            R_v = right
            L_v = up 
        cmd = str(L_v) +","+ str(R_v) + ",0,0000000000"
    else :
        cmd = "000,000,0,0000000000"

    pub_joy.publish(cmd)
    print cmd
    rate.sleep()


 
if __name__ == '__main__':
    rospy.init_node('joy_lai')
    pub_joy = rospy.Publisher('joy_information', String, queue_size=1)
    rospy.Subscriber("/joy", Joy, joy_remapping, queue_size = 1, buff_size = 52428800)
    rospy.spin()
