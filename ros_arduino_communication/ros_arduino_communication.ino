

#include <ros.h>
#include <std_msgs/String.h>
#include <std_msgs/Float32.h>
#include <Servo.h>
#include <string.h>
using namespace std;

//servo parameter
Servo myservo;
int bef;
int aft;

//ultrasound parameter
const int trig_l = 9;
const int echo_l = 10;

const int trig_r = 11;
const int echo_r = 12;

const int trig_m = A0;
const int echo_m = A1;

const int trig_ul = A2;
const int echo_ul = A4;

const int trig_ur = A3;
const int echo_ur = A5;

const int inter_time = 2;
//void ultrasound(int in_l , int out_l , int in_r , int out_r , int in_m , int out_m , int in_ul , int out_ul , int in_ur , int out_ur);
ros::NodeHandle tiger;
std_msgs::Float32 str_msg_l , str_msg_r , str_msg_m , str_msg_ul , str_msg_ur;
std_msgs::String str_msg_mode ;// , str_msg;

String str;
int cmd[3] = {0};

void down() {
  for (int i = bef; i >= bef - 65; i = i - 1) {
    myservo.write(i);
    delay(10);
    aft = i;
  }
}

void up() {
  for (int i = aft; i <= aft + 65; i = i + 1) {
    myservo.write(i);
    delay(10);
  }
}

void toMotor(int l, int r) {

  //left motor forward and backward
  if (r > 0) {
    digitalWrite(2, HIGH);
    digitalWrite(4, LOW);
    analogWrite(5, map(r, 0, 100, 0, 255));
  }
  else if (r < 0) {
    digitalWrite(2, LOW);
    digitalWrite(4, HIGH);
    analogWrite(5, map(-r, 0, 100, 0, 255));
  }

  //right motor forward and backward
  if (l > 0) {
    digitalWrite(7, HIGH);
    digitalWrite(8, LOW);
    analogWrite(6, map(l, 0, 100, 0, 255));
  }
  else if (l < 0) {
    digitalWrite(7, LOW);
    digitalWrite(8, HIGH);
    analogWrite(6, map(-l, 0, 100, 0, 255));
  }


}


ros::Publisher pub_l("ultrasound_info_l", &str_msg_l);
ros::Publisher pub_r("ultrasound_info_r", &str_msg_r);
ros::Publisher pub_m("ultrasound_info_m", &str_msg_m);
ros::Publisher pub_ul("ultrasound_info_ul", &str_msg_ul);
ros::Publisher pub_ur("ultrasound_info_ur", &str_msg_ur);

//ros::Publisher pub("ultrasound_info", &str_msg);

ros::Publisher pub_mode("mode", &str_msg_mode);
ros::Subscriber<std_msgs::String> sub("arduino_msg", &message_callback);

void message_callback( const std_msgs::String& arduino_msg) {
  str = arduino_msg.data;
  const char* d = ",";   //分割依據
  char *p;  //儲存每次分割結果
  char buf[100];
  str.toCharArray(buf, sizeof(buf));
  p = strtok(buf, d);
  int i = 0;
  while (p)
  {
    cmd[i] = atoi(p);
    p = strtok(NULL, d);
    i++;
  }
  toMotor(cmd[0], cmd[1]);
  if (cmd[2] == 1) {        // if suck  servo motion
    digitalWrite(13, 1);    // suck forever
    down();
    up();

    str_msg_mode.data = "home";
    pub_mode.publish(&str_msg_mode);
  }
}

void setup()
{
  tiger.initNode();
  tiger.advertise(pub_l);
  tiger.advertise(pub_r);
  tiger.advertise(pub_m);
  tiger.advertise(pub_ul);
  tiger.advertise(pub_ur);
  //tiger.advertise(pub);
  tiger.advertise(pub_mode);
  tiger.subscribe(sub);

  //servo setup
  myservo.attach(3);
  myservo.write(65);
  bef = myservo.read();

  pinMode (trig_l, OUTPUT);
  pinMode (echo_l, INPUT);
  pinMode (trig_r, OUTPUT);
  pinMode (echo_r, INPUT);
  pinMode (trig_m, OUTPUT);
  pinMode (echo_m, INPUT);
  pinMode (trig_ul, OUTPUT);
  pinMode (echo_ul, INPUT);
  pinMode (trig_ur, OUTPUT);
  pinMode (echo_ur, INPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(2, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(13, OUTPUT);

}



float duration_l = 0;
float duration_r = 0;
float duration_m = 0;
float duration_ul = 0;
float duration_ur = 0;;

const long period = 10 ;
unsigned long beftime = 0;

void loop()
{

  /*

    unsigned long nowtime = micros();
    digitalWrite(trig_l, HIGH);
    digitalWrite(trig_r, HIGH);
    digitalWrite(trig_m, HIGH);
    digitalWrite(trig_ul, HIGH);
    digitalWrite(trig_ur, HIGH);

    if (nowtime - beftime > period) {
      beftime = nowtime;
      digitalWrite(trig_l, LOW);
      digitalWrite(trig_r, LOW);
      digitalWrite(trig_m, LOW);
      digitalWrite(trig_ul, LOW);
      digitalWrite(trig_ur, LOW);
      duration_l = pulseIn (echo_l, HIGH, 10000);
      //duration_r = pulseIn (echo_r, HIGH,10000);
      //duration_m = pulseIn (echo_m, HIGH);
      //duration_ul = pulseIn (echo_ul, HIGH);
      // duration_ur = pulseIn (echo_ur, HIGH);

    }
  */

  //    duration_l = ultrasound(trig_l, echo_l);
  //    duration_r = ultrasound(trig_r, echo_r);
  //    duration_m = ultrasound(trig_m, echo_m);
  //    duration_ul = ultrasound(trig_ul, echo_ul);
  //    duration_ur = ultrasound(trig_ur, echo_ur);
  //
  //    str_msg_l.data = (duration_l / 2) / 29;
  //    str_msg_r.data = (duration_r / 2) / 29;
  //    str_msg_m.data = (duration_m / 2) / 29;
  //    str_msg_ul.data = (duration_ul / 2) / 29;
  //    str_msg_ur.data = (duration_ur / 2) / 29;
  //
  //
  //    pub_l.publish(&str_msg_l);
  //    pub_r.publish(&str_msg_r);
  //    pub_m.publish(&str_msg_m);
  //    pub_ul.publish(&str_msg_ul);
  //    pub_ur.publish(&str_msg_ur);

  tiger.spinOnce();
  //delayMicroseconds(inter_time);
}


unsigned long ultrasound(int trigp , int echop) {
  unsigned long puls = 0;

  digitalWrite(trigp, LOW);
  delayMicroseconds(2);
  digitalWrite(trigp, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigp, LOW);

  puls = pulseIn (echop, HIGH, 10000);

  return puls;
}
