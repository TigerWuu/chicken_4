

#include <ros.h>
#include <std_msgs/String.h>
#include <std_msgs/Float32.h>

const int trig = 5;
const int echo = 6;
const int inter_time = 1000;

ros::NodeHandle tiger;

std_msgs::Float32 str_msg;
ros::Publisher chatter("chatter_tiger", &str_msg);

void setup()
{
  tiger.initNode();
  tiger.advertise(chatter);
  pinMode (trig, OUTPUT);
  pinMode (echo, INPUT);
}

void loop()
{ 
  float duration, distance;
  digitalWrite(trig, HIGH);
  delayMicroseconds(1000);
  digitalWrite(trig, LOW);
  duration = pulseIn (echo, HIGH);
  distance = (duration/2)/29;
  
  str_msg.data = distance;
  chatter.publish(&str_msg);
  tiger.spinOnce();
  delay(inter_time);
}
