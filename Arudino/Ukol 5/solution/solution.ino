#include "funshield.h"


const int INTERVAL = 100;

//Pri posunuti tecky zobrazujeme jinak
//tedy max pozice do ktere mazeme nuly zavisi na pos dot

enum State {
  STOPPED,
  RUNNING,
  LAPPED
}


class Button
{
  private:
  int pin;
  bool previousState;
  public:
  
  void init(int p)
  {
    pin = p;
    pinMode(pin, INPUT)
    previousState = false;
  }
  bool isPressed()
  {
    bool currentState = digitalRead(pin);
    if(previousState != currentState && previousState == HIGH){
      previousState = currentState;
      return true;
    }
    previousState = currentState;
    return false;
  };
};
class Seven_seg
{
  private:
  int currentDigit;
  const int num_digits = 4;
  byte buffer[4] = {0,0,0,0};

  public:
  Seven_seg(){
    pinMode(latch_pin, OUTPUT);
    pinMode(clock_pin, OUTPUT);
    pinMode(data_pin, OUTPUT);
    currentDigit = 0;
  }

  void showNextDigit(byte num[4])
  {
    digitalWrite(latch_pin, LOW);
    shiftOut(data_pin, clock_pin, MSBFIRST, num[currentDigit]);
    shiftOut(data_pin, clock_pin, MSBFIRST, 1 << ( num_digits + 1 - currentDigit));

    digitalWrite(latch_pin, HIGH);
    currentDigit = (currentDigit + 1) % num_digits;
  };

  void changeBuffer(byte digits[4]){
    for (int i = 0; i < num_digits; i++) {
        buffer[i] = digits[i];
    }
}


}
class Casovac
{
  private:
  Seven_seg* display;
  State state;
  


void update(unsigned long now) {
  if ((state == RUNNING || state == LAPPED) && (now - lastUpdate >= INTERVAL)) {
    lastUpdate = now;
    
    
    unsigned long timeToFormat = (state == LAPPED) ? lapSnapshot : now - startTime;
    
    formatToDigits(timeToFormat);
  }
}
  unsigned long read();

}





Button btn1, btn2, btn3;
Seven_seg display;
Casovac stopwatch;

int ledky[4] = {led1_pin, led2_pin, led3_pin, led4_pin};
constexpr int ledky_count = sizeof(ledky) / sizeof(ledky[0]);
Button butony[3] = {btn1, btn2, btn3};
int butony_count = sizeof(butony) / sizeof(butony[0]);



void setup() {
  // put your setup code here, to run once:
  

}

void loop() {
  // put your main code here, to run repeatedly:


  display.showNextDigit();

}
