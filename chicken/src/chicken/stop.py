#!/usr/bin/env python

import rospy
from std_msgs.msg import String

CMD="000,000,0,0000000000"

def stopper():
    pub = rospy.Publisher('arduino_msg', String, queue_size=10)
    rospy.init_node('stopper', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():

        pub.publish(CMD)
        rate.sleep()



if __name__ == '__main__':
    try:
        stopper()
    except rospy.ROSInterruptException:
        pass
