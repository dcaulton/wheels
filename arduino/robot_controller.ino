#include <AFMotor.h>

//control a 4 wheel robot via serial port with a protocol that looks like this:
// p0,XXX stop  (int XXX is ignored but needed for now)
// p1,255 forward (eventually at speed 255)
// p2,255 backward (eventually at speed 255)
// p3,122 turn (eventually to heading 122)
// pXX,YY display status (ints XX and YY are ignored as long as XX isn't 0,1,2 or 3)

AF_DCMotor motor1(1);
AF_DCMotor motor2(2);
AF_DCMotor motor3(3);
AF_DCMotor motor4(4);
int current_command = 0;
int current_magnitude = 0;

void setup()
{
  motor1.run(FORWARD);
  motor2.run(FORWARD);
  motor3.run(FORWARD);
  motor4.run(FORWARD);
  motor1.setSpeed(0);
  motor2.setSpeed(0);
  motor3.setSpeed(0);
  motor4.setSpeed(0);
  Serial.begin(9600);
}

void loop()
{
  int command = -1;
  int num = -1;
  if (Serial) {
    if (Serial.find("p")) {
      command = Serial.parseInt();
      num = Serial.parseInt();
    }

    switch (command) {
      case 0:
        current_command = command;
        current_magnitude = 0;
        stop();
        break;
      case 1: 
        current_command = command;
        current_magnitude = num;
        forward(num);
        break;
      case 2:
        current_command = command;
        current_magnitude = num;
        reverse(num);
        break;
      case 3:
        current_command = command;
        current_magnitude = num;
        turn(num);
        break;
      default:
        status();
      break;
    }
  }
}

void forward(int num) {
  motor1.run(FORWARD);
  motor2.run(FORWARD);
  motor3.run(FORWARD);
  motor4.run(FORWARD);
  motor1.setSpeed(num);
  motor2.setSpeed(num);
  motor3.setSpeed(num);
  motor4.setSpeed(num);
  Serial.println(current_command*1000 + current_magnitude);
}
void reverse(int num) {
  motor1.run(BACKWARD);
  motor2.run(BACKWARD);
  motor3.run(BACKWARD);
  motor4.run(BACKWARD);
  motor1.setSpeed(num);
  motor2.setSpeed(num);
  motor3.setSpeed(num);
  motor4.setSpeed(num);
  Serial.println(current_command*1000 + current_magnitude);
}
void turn(int num) {
  if (num > 180) {
    motor1.run(FORWARD);
    motor2.run(BACKWARD);
    motor3.run(FORWARD);
    motor4.run(BACKWARD);
    motor1.setSpeed(150);
    motor2.setSpeed(150);
    motor3.setSpeed(150);
    motor4.setSpeed(150);
  } else {
    motor1.run(BACKWARD);
    motor2.run(FORWARD);
    motor3.run(BACKWARD);
    motor4.run(FORWARD);
    motor1.setSpeed(150);
    motor2.setSpeed(150);
    motor3.setSpeed(150);
    motor4.setSpeed(150);
  }
  Serial.println(current_command*1000 + current_magnitude);
}
void stop() {
  motor1.setSpeed(0);
  motor2.setSpeed(0);
  motor3.setSpeed(0);
  motor4.setSpeed(0);
  Serial.println(current_command*1000 + current_magnitude);
}
void status() {
  Serial.println(90000 + current_command*1000 + current_magnitude);
}


