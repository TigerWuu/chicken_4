

#include <ros.h>
#include <std_msgs/String.h>
#include <std_msgs/Float32.h>
#include <Servo.h>

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
const int echo_ul = A3;

const int trig_ur = A4;
const int echo_ur = A5;

const int inter_time = 50;
float ultrasound(int in , int out);

ros::NodeHandle tiger;
std_msgs::Float32 str_msg_l , str_msg_r , str_msg_m , str_msg_ul , str_msg_ur;
std_msgs::String str_msg_mode;

String str;
int cmd[3] = {0};

void down() {
  for (int i = bef; i >= bef - 70; i = i - 1) {
    myservo.write(i);
    delay(10);
    aft = i;
  }
}

void up() {
  for (int i = aft; i <= aft + 70; i = i + 1) {
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
  toMotor(cmd[0],cmd[1]);
  if (cmd[2] == 1) {        // if suck  servo motion
    digitalWrite(13, 1);    // suck forever
    down();
    up();
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
  tiger.advertise(pub_mode);
  tiger.subscribe(sub);

  //servo setup
  myservo.attach(3);
  myservo.write(90);
  bef = myservo.read();

  pinMode (trig_l, OUTPUT);
  pinMode (echo_l, INPUT);
  pinMode (trig_r, OUTPUT);
  pinMode (echo_r, INPUT);
  pinMode (trig_m, OUTPUT);
  pinMode (echo_m, INPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(2, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(13, OUTPUT);

}

void loop()
{
  str_msg_l.data = ultrasound(trig_l , echo_l);
  str_msg_r.data = ultrasound(trig_r , echo_r);
  str_msg_m.data = ultrasound(trig_m , echo_m);
  str_msg_ul.data = ultrasound(trig_ul , echo_ul);
  str_msg_ur.data = ultrasound(trig_ur , echo_ur);
  
  pub_l.publish(&str_msg_l);
  pub_r.publish(&str_msg_r);
  pub_m.publish(&str_msg_m);
  pub_r.publish(&str_msg_ul);
  pub_m.publish(&str_msg_ur);

  tiger.spinOnce();
  delay(inter_time);
}

float ultrasound(int in , int out) {
  float duration, distance;
  digitalWrite(in, HIGH);
  delayMicroseconds(1000);
  digitalWrite(in, LOW);
  duration = pulseIn (out, HIGH);
  distance = (duration / 2) / 29;
  return distance;
}
