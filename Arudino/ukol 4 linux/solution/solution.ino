#include "funshield.h"

constexpr int num_digits = 4;
//int start = 0;
const int interval = 1000;
int ledky[4] = {led1_pin, led2_pin, led3_pin, led4_pin};
constexpr int ledky_count = sizeof(ledky) / sizeof(ledky[0]);

int INITIAL_DELAY = 1000;
int REPEAT_DELAY = 1;




struct Button{
  int pin;
  bool currentState;
  bool previousState;
  //int Delay;
  //unsigned long lastTime = 0;
  Button(int p){
    pin = p;
    currentState = HIGH;
    previousState = HIGH;
    pinMode(p, INPUT);
  }
  bool isPressed(){
    currentState = digitalRead(pin);
    if(previousState != currentState && previousState == HIGH){
      previousState = currentState;
      return true;
    }
    previousState = currentState;
    return false;
  }; 
  
};


class Seven_seg{
  public:
   Seven_seg(){
    pinMode(latch_pin, OUTPUT);
    pinMode(clock_pin, OUTPUT);
    pinMode(data_pin, OUTPUT);

  }
    int displayedNum[4]={0,0,0,0}; //psano zprava do leva
    int cur_digit_displayed=0;

    void displayDigit() {
    digitalWrite(latch_pin, LOW); 
    shiftOut(data_pin, clock_pin, MSBFIRST, digits[displayedNum[cur_digit_displayed]]);
    shiftOut(data_pin, clock_pin, MSBFIRST, 1 << (num_digits - cur_digit_displayed - 1));
    digitalWrite(latch_pin, HIGH); 
    }
    void changePos(){
        cur_digit_displayed = (cur_digit_displayed+1) % 4;
        displayDigit();
    };

   void changeNum(int scitanec) {
    int number = 0;

    
    for (int i = num_digits - 1; i >= 0; i--) {
        number = number * 10 + displayedNum[i];
    }
    for(int i = 0; i < cur_digit_displayed;i++){
      scitanec *= 10;
    }

    
    number +=  scitanec;
   
    
    if (number < 0) {
        number += 10000; 
    }
    number = number % 10000; 

 
    for (int i = 0; i < num_digits; i++) {
        displayedNum[i] = number % 10;
        number = number / 10;
    }

    
    displayDigit();
}
};

class AppController{
  public:
  Seven_seg* display = new Seven_seg();
  Button butony[3] = {Button(button1_pin), Button(button2_pin), Button(button3_pin)};
  int butony_count = sizeof(butony) / sizeof(butony[0]);
  AppController(){
    display->displayDigit();
  }
 
  void handleButtonPressed(int buttonId){
      switch(buttonId) {
        case 0:
            display->changeNum(1);
            break;
        case 1:
            display->changeNum(-1);
            break;
        case 2:
            display->changePos();
            break;
        default:
            break;
    }

  }
  void checkButtonsPressed(){
    for(int i = 0; i < butony_count; i++){

      if(butony[i].isPressed()){
        handleButtonPressed(i);
      }
    }
  };
};
//nevim jak se vyhnout tomuto
AppController* controller = nullptr;

void setup() {
  // put your setup code here, to run once:
  controller = new AppController();
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  controller->checkButtonsPressed();
  
  
  
}
