#include <funshield.h>
int ledky[4] = {led1_pin, led2_pin, led3_pin, led4_pin};
constexpr int ledky_count = sizeof(ledky) / sizeof(ledky[0]);
int konstanta = 0;
bool nesviti = true;
bool stisknuto1;
bool stisknuto2;

// the setup function runs once when you press reset or power the board
void setup() {
  pinMode(led1_pin,OUTPUT);
  pinMode(led2_pin,OUTPUT);
  pinMode(led3_pin,OUTPUT);
  pinMode(led4_pin,OUTPUT);
  pinMode(button1_pin, INPUT);
  pinMode(button2_pin, INPUT);
  pinMode(button3_pin, INPUT);
  stisknuto1 = digitalRead(button1_pin);
  stisknuto2 = digitalRead(button1_pin);




}
void encoder(unsigned int v){
  for(int i = 0; i < ledky_count; i++){
      if(v & 1 == 1){
        digitalWrite(ledky[i], LOW);
      }
      else{
        digitalWrite(ledky[i], HIGH);

      }
      v = v>>1; 
  }
   
}
// the loop function runs over and over again forever
void loop() {
  if(stisknuto1 != digitalRead(button1_pin))
    {
       konstanta = (konstanta + 1)%16;
       encoder(konstanta);
    }
  if(stisknuto2 != digitalRead(button2_pin)){
    konstanta = (konstanta +15)%16;
    encoder(konstanta);
  }
  
    delay(120);
    
  


  
  
     
}
