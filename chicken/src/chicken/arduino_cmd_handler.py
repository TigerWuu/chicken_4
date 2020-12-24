#!/usr/bin/env python

import rospy
from std_msgs.msg import String

CMD="000,000,0,0000000000"   # left , right , suck ,

def car_move(msg):
    global CMD
    if msg.data == "L":
        CMD="100,050,0,0000000000"
    elif msg.data == "R":
        CMD="050,100,0,0000000000"
    elif msg.data == "S":
        CMD="000,000,1,0000000000"   #suck the ball at the same time
    else:
        CMD="100,100,0,0000000000"
        
    pub.publish(CMD)
<<<<<<< HEAD
=======


def remote_cmd(msg):
    CMD=msg.data
    pub.publish(CMD)
>>>>>>> ae30f0093a2c091df08c41bd69d8387038acf741


if __name__ == "__main__":
    rospy.init_node('arduino_cmd_handler', anonymous=True)
    rospy.Subscriber("car_info" , String , car_move)
<<<<<<< HEAD
=======
    rospy.Subscriber("joy_information" , String , remote_cmd)
>>>>>>> ae30f0093a2c091df08c41bd69d8387038acf741
    pub = rospy.Publisher('arduino_msg', String, queue_size=10)
    
    rospy.spin()

