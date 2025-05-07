#include "funshield.h"

constexpr int num_digits = 4;
//int start = 0;
const int interval = 1000;
int ledky[4] = {led1_pin, led2_pin, led3_pin, led4_pin};
constexpr int ledky_count = sizeof(ledky) / sizeof(ledky[0]);
int buttonPins[3] = {button1_pin,button2_pin,button3_pin};
constexpr int button_count = sizeof(buttonPins) / sizeof(buttonPins[0]);
int sevenSegPins[3] = {latch_pin,clock_pin,data_pin};
constexpr int sevSegPin_count = sizeof(sevenSegPins) / sizeof(sevenSegPins[0]);

int INITIAL_DELAY = 1000;
int REPEAT_DELAY = 1;
const int MAX_DISPLAY_VALUE = 10000;



class Button {
  private:
    int pin;
    bool currentState;
    bool previousState;
  public:
    
    Button() {
      pin = 0; 
      currentState = HIGH;
      previousState = HIGH;
    }
    
    void init(int p) {
      pin = p;
    }
    
    bool isPressed() {
      currentState = digitalRead(pin);
      if(previousState != currentState && previousState == HIGH) {
        previousState = currentState;
        return true;
      }
      previousState = currentState;
      return false;
    }
};


class SevenSeg {
  private:
    int displayedNum[num_digits];  // jednotlive digits
    int cur_digit_displayed;       
    int wholeNumber;               
    
    void updateDisplayedNum() {
      int x = wholeNumber;
      for(int i = 0; i < num_digits; i++) {
        displayedNum[i] = x % 10;
        x = x / 10;
      }
    }
    
  public:

    SevenSeg() {
      cur_digit_displayed = 0;
      wholeNumber = 0;
      for(int i = 0; i < num_digits; i++) {
        displayedNum[i] = 0;
      }
    }
    
    void init() {
     
      wholeNumber = 0;
      updateDisplayedNum();
    }
 
    void displayDigit() {
      digitalWrite(latch_pin, LOW);
      shiftOut(data_pin, clock_pin, MSBFIRST, digits[displayedNum[cur_digit_displayed]]);
      shiftOut(data_pin, clock_pin, MSBFIRST, 1 << (num_digits - cur_digit_displayed - 1));
      digitalWrite(latch_pin, HIGH);
    }
    
    void changePos() {
      cur_digit_displayed = (cur_digit_displayed + 1) % num_digits;
      displayDigit();
    }
   
    void changeWholeNumber(int addend) {
      int x = 1;
      for(int i = 0; i < cur_digit_displayed; i++) {
        x *= 10;
      }
      wholeNumber += addend * x;
      if(wholeNumber < 0) {
        wholeNumber += MAX_DISPLAY_VALUE;
      }
      wholeNumber = wholeNumber % MAX_DISPLAY_VALUE;
      updateDisplayedNum();
      displayDigit();
    }
    
    void increment() {
      changeWholeNumber(1);
    }
    
    void decrement() {
      changeWholeNumber(-1);
    }
};


class AppController {
private:
    SevenSeg display;
    Button buttons[button_count];
public:
    void init() {
    
      display.init();
      
      
      for(int i = 0; i < button_count; i++) {
        buttons[i].init(buttonPins[i]);
      }
      

      display.displayDigit();
    }
    
    void checkButtonsPressed() {
     
      if (buttons[0].isPressed()) {
        display.increment();
      }
      if (buttons[1].isPressed()) {
        display.decrement();
      }
      if (buttons[2].isPressed()) {
        display.changePos();
      }
    }
};


AppController controller;

void setup() {

  for(int i = 0; i < sevSegPin_count; i++) {
    pinMode(sevenSegPins[i], OUTPUT);
  }

  for(int i = 0; i < button_count; i++) {
    pinMode(buttonPins[i], INPUT);
  }
  
 
  controller.init();
}

void loop() {
  controller.checkButtonsPressed();
}