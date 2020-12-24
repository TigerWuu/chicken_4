#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32


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

def ultrasound_get(dis_data):
    distance = dis_data.data
    if distance < 10:
        orientation = "S"
        Body.publish(orientation)


if __name__ == "__main__":
    rospy.init_node("brain" ,anonymous = True)
    Body = rospy.Publisher("car_info" , String ,queue_size = 10)
    rospy.Subscriber("image_info" , String , image_get)
    rospy.Subscriber("ultrasound_info" , Float32 , ultrasound_get)
    rospy.spin()
