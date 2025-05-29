#include "funshield.h"

long start = millis();

constexpr int interval = 300;

int ledky[4] = {led1_pin, led2_pin, led3_pin, led4_pin};

constexpr int ledky_count = sizeof(ledky) / sizeof(ledky[0]);

int pos = 0;

int direction = 1;


void setup() {

  for(int i = 0; i < ledky_count; i++){

    pinMode(ledky[i], OUTPUT);

    digitalWrite(ledky[i], HIGH);

  }

  digitalWrite(ledky[0], LOW);

}

void changeLed(int& pos, int& direction){


  digitalWrite(ledky[pos], ON);

  pos += direction;

  pos = (pos) % ledky_count;

  digitalWrite(ledky[pos], OFF);

  if(pos == ledky_count - 1 || pos == 0){

    direction *= -1;

  }

}

void loop() {


  if(millis()-start > interval){

    changeLed(pos, direction);

    start = millis();

  }


  


}

