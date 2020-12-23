#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import serial

COM_PORT = '/dev/ttyACM0'  
BAUD_RATES = 9600

ser = serial.Serial(COM_PORT, BAUD_RATES)

def serial_com(msg):
    cmdd=(msg.data+"\n").encode()
    ser.write(cmdd)
    while ser.in_waiting:
        mcu_feedback = ser.readline().decode()  # 接收回應訊息並解碼
        pub.publish(mcu_feedback)    


if __name__ == "__main__":
    rospy.init_node('communicate', anonymous=True)
    rospy.Subscriber("arduino_cmd" , String , serial_com)
    pub = rospy.Publisher('arduino_out', String, queue_size=10)
    rospy.spin()