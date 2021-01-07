#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from time import sleep

ball = ""
home = ""


def image_get(image_data):
    center_dist = image_data.data
    center_dist = center_dist.split(",", 2)
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


def ball_callback(d):
    global ball
    ball = d.data


def home_callback(d):
    global home
    home = d.data

    if home != "" and ball != "":
        gogo()


def gogo():
    global ball, home
    print("start request......")
    if ball == "red":
        t = [3, 3, 3, 3, 3]
        Body.publish("L")
        sleep(t[0])
        Body.publish("F")
        sleep(t[1])
        Body.publish("suck")
        sleep(t[2])
        Body.publish("R")
        sleep(t[3])


if __name__ == "__main__":
    rospy.init_node("Aho", anonymous=True)
    Body = rospy.Publisher("car_info", String, queue_size=10)
    rospy.Subscriber("image_info", String, image_get)
    rospy.Subscriber("ultrasound_info", Float32, ultrasound_get)
    rospy.Subscriber("ball_color", String, ball_callback)
    rospy.Subscriber("home_color", String, home_callback)
    rospy.spin()
