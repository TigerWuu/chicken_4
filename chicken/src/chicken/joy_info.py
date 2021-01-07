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

HZ=60


def joy_remapping(msg):
    global count, mode, diff, count2
    buttons = msg.buttons
    axes = msg.axes
    axes = map(lambda x:int(x*100),axes)  
    _,L_UD,_,R_UD,_,_ = axes 
    X,A,B,Y,LB,RB,_,_,back,start,_,_=buttons       
    if back == 1:        ## press back to shutdown
    	p = os.popen('shutdown now')
    
    rate = rospy.Rate(HZ)


    cmd = str(L_UD) +","+ str(R_UD) + ","+str(X)+",0000000000"
    pub_joy.publish(cmd)
    print cmd
    rate.sleep()


 
if __name__ == '__main__':
    rospy.init_node('joy_lai')
    pub_joy = rospy.Publisher('joy_information', String, queue_size=1)
    rospy.Subscriber("/joy", Joy, joy_remapping, queue_size = 1, buff_size = 52428800)
    rospy.spin()
