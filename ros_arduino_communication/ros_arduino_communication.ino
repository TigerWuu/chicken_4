

#include <ros.h>
#include <std_msgs/String.h>
#include <std_msgs/Float32.h>
#include <Servo.h>

//servo parameter
Servo myservo;
int bef;
int aft;

//ultrasound parameter
const int trig = 11;
const int echo = 12;
const int inter_time = 1000;

ros::NodeHandle tiger;

std_msgs::Float32 str_msg;
String str;
int cmd[3] = {0};




void up(){
  for (int i = bef; i >= bef - 70; i = i - 1) {
    myservo.write(i);
    delay(10);
    aft = i;
  }
}

void down(){
  for (int i = aft; i <= aft + 70; i = i + 1) {
    myservo.write(i);
    delay(10);
  }
}


void message_callback( const std_msgs::String& arduino_msg){
    str = arduino_msg.data;
    const char* d = ",";   //分割依據 
    char *p;  //儲存每次分割結果 
    char buf[100];
    str.toCharArray(buf, sizeof(buf));
    p = strtok(buf,d);      
    int i =0;
    while(p)
    {    
        cmd[i] = atoi(p);
        p=strtok(NULL,d);  
        i++;    
    }
    digitalWrite(2, HIGH);    
    digitalWrite(4, LOW);
    digitalWrite(7, HIGH);
    digitalWrite(8, LOW);
    analogWrite(5, cmd[0]);
    analogWrite(6, cmd[1]);
    digitalWrite(13,cmd[2]);  // if suck
    if (cmd[2] == 1){         // if suck  servo motion
      down();
      up();
    }
}

ros::Publisher chatter("chatter_tiger", &str_msg);
ros::Subscriber<std_msgs::String> sub("arduino_msg", &message_callback);

void setup()
{
  tiger.initNode();
  tiger.advertise(chatter);
  tiger.subscribe(sub);

  //servo setup
  myservo.attach(3);
  myservo.write(90);
  bef = myservo.read();
  
  pinMode (trig, OUTPUT);
  pinMode (echo, INPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(2, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(13,OUTPUT);
 
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
