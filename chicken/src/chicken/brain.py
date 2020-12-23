#!/usr/bin/env python
import rospy
from std_msgs.msg import String


def image_get(image_data):
    center_dist = image_data.data
    center_dist = center_dist.split("," , 2)
    if int(center_dist[0]) > 350:
        orientation = "R"
    elif int(center_dist[0]) < 290:
        orientation = "L"
    elif int(center_dist[2]) < 25:
        orientation = "S"
    else:
        orientation = "F"
        
    Body.publish(orientation)

def ultrasonic_get(data):
    #Body.pub()
    pass

def encoder_get(data):

    #Body.pub()
    pass


if __name__ == "__main__":
    rospy.init_node("brain" ,anonymous = True)
    Arm = rospy.Publisher("arm_info" , String ,queue_size = 10)
    Body = rospy.Publisher("car_info" , String ,queue_size = 10)
    rospy.Subscriber("image" , String , image_get)
    rospy.Subscriber("ultrasonic" , String , ultrasonic_get)
    rospy.Subscriber("encoder" , String , encoder_get)
    rospy.spin()
