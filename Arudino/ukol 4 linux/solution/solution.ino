#include <funshield.h>
int start;
const int interval = 1000;
int ledky[4] = {led1_pin, led2_pin, led3_pin, led4_pin};
constexpr int ledky_count = sizeof(ledky) / sizeof(ledky[0]);
Button butony[3];

struct Button{
  int pin;
  bool currentState;
  bool previousState;
  int Delay;
  unsigned long lastTime = 0;

  Button(int p){
    pin = p;
    currentState = false;
    previousState =false;
    

  }
  
}


class Seven_seg{
  public:
    int displayedNum=0;
    int cur_digit=0;


};


void show_num_pos(unsigned int v){
  return;
}


void setup() {
  // put your setup code here, to run once:
  start = 0;
  Seven_seg* display = new Seven_seg();

}

void loop() {
  // put your main code here, to run repeatedly:
  int cur_time= millis();
  if(cur_time-start > interval)
  {
    
      //button input
  }
  
  

}
