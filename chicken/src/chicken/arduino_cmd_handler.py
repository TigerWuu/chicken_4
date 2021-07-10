#!/usr/bin/env python

import rospy
from std_msgs.msg import String

CMD = "000,000,0,0000000000"   # left , right , suck ,


def car_move(msg):
    global CMD
    if msg.data == "L":
        CMD = "0,050,0,0000000000"
    elif msg.data == "R":
        CMD = "050,0,0,0000000000"
    elif msg.data == "S":
        CMD = "000,000,0,0000000000"
    elif msg.data == "suck":
        CMD = "000,000,1,0000000000"  # suck the ball at the same time
    elif msg.data == "F":
        CMD = "100,100,0,0000000000"

    pub.publish(CMD)


def remote_cmd(msg):
    CMD = msg.data
    pub.publish(CMD)


if __name__ == "__main__":
    rospy.init_node('arduino_cmd_handler')
    rospy.Subscriber("car_info", String, car_move)
    pub = rospy.Publisher('arduino_msg', String, queue_size=10)
    rospy.Subscriber("joy_information", String, remote_cmd)

    rospy.spin()
