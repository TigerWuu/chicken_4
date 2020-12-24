import sys
import rospy
from std_msgs.msg import String

def send_color(color):
    pub = rospy.Publisher("color" , String , queue_size = 10)
    rospy.init_node("app" , anonymous = True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        color_choice = str(color)
        pub.publisher(color_choice)
        rate.sleep()

if __name__ == '__main__':
    try:
        send_color(sys.argv[1])
    except rospy.ROSInterruptException:
        print("ROS error!!!!!!!!!!")
