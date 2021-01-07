import sys
import rospy
from std_msgs.msg import String

def send_color(ball_color , home_color):
    pub_ball = rospy.Publisher("ball_color" , String , queue_size = 10)
    pub_home = rospy.Publisher("home_color" , String , queue_size = 10)
  
    rospy.init_node("app" , anonymous = True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        color_choice = str(ball_color)
        pub_ball.publish(color_choice)
        rate.sleep()

if __name__ == '__main__':
    try:
        send_color(sys.argv[1] , sys.argv[2])
    except rospy.ROSInterruptException:
        print("ROS error!!!!!!!!!!")
