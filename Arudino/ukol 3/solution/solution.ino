#include "funshield.h"

const unsigned long INITIAL_DELAY = 1000;
const unsigned long REPEAT_DELAY = 300;
const int MODULO_VALUE = 16;  


const int ledky[4] = {led1_pin, led2_pin, led3_pin, led4_pin};
const int butony_pin[3] = {button1_pin, button2_pin, button3_pin};
constexpr int ledky_count = sizeof(ledky) / sizeof(ledky[0]);
constexpr int butony_count = sizeof(butony_pin) / sizeof(butony_pin[0]);


struct Button {
  unsigned long lastTime;
  bool stisknuto;
  unsigned long delay;
  int pricitani;
};


int pocitadlo = 0;


Button buttons[2] = {
  {0, false, INITIAL_DELAY, 1},  
  {0, false, INITIAL_DELAY, MODULO_VALUE - 1}  
};


void encoder(int v) {
  for(int i = 0; i < ledky_count; i++) {
    bool sviti = (v >> i) & 1;
    digitalWrite(ledky[ledky_count - 1 - i], !sviti);
  }
}


void Pocitej(int pricitani) {
  pocitadlo = (pocitadlo + pricitani) % MODULO_VALUE;
  encoder(pocitadlo);
}


bool zpracujTlacitko(int pin, Button& button) {
  unsigned long currentMillis = millis();
  bool zmacknuto = (digitalRead(pin) == LOW);
  bool aktivovat = false;

  if (zmacknuto) {
    if (!button.stisknuto) {
     
      aktivovat = true;
      button.lastTime = currentMillis;
      button.stisknuto = true;
    } else {
      if (currentMillis - button.lastTime > button.delay) {
        button.delay = REPEAT_DELAY;
        aktivovat = true;
        button.lastTime = currentMillis;
      }
    }
  } else {
    
    button.delay = INITIAL_DELAY;
    button.stisknuto = false;
  }

  return aktivovat;
}

void setup() {
 

  
  for (int i = 0; i < butony_count; i++) {
    pinMode(butony_pin[i], INPUT);
  }
  
  
  for (int i = 0; i < ledky_count; i++) {
    pinMode(ledky[i], OUTPUT);
    digitalWrite(ledky[i], OFF);
  }
}

void loop() {
  
  for (int i = 0; i < 2; i++) {
    if (zpracujTlacitko(butony_pin[i], buttons[i])) {
      Pocitej(buttons[i].pricitani);
    }
  }
}