  #include "funshield.h"



//velmi osklivy kod plny globalnich promennych. Ale nemam tuseni jak se jich zbavit
//Napisu si tridu pro Button aby to bylo prehlednejsi
//rozhodne to neni dry kod




  const unsigned long INITIAL_DELAY = 1000;  
  const unsigned long REPEAT_DELAY = 300; 
  unsigned long DELAY1;
  unsigned long DELAY2;


  int ledky[4] = {led1_pin, led2_pin, led3_pin, led4_pin};
  int butony[3] = {button1_pin, button2_pin, button3_pin};
  constexpr int ledky_count = sizeof(ledky) / sizeof(ledky[0]);
  constexpr int butony_count = sizeof(butony) / sizeof(butony[0]);

  long start = millis();
  int pocitadlo = 0;
  


  unsigned long lastTime1 = 0;
  bool stisknuto1 = false;
  unsigned long lastTime2 = 0;
  bool stisknuto2 = false;

 void encoder(int v)
  {
    
    for(int i = 0; i < ledky_count; i++)
    {
      bool sviti = (v>>i) & 1;
      digitalWrite(ledky[ledky_count - 1 - i], !sviti);
    }
  }
void pocitej(int& poc, int pricitani){
  poc = (poc+ pricitani) % 16;
  encoder(poc);
}
void updateCounter(int pin, unsigned long& lastTime, bool& byloZmacknuto, int pricitano, unsigned long& DELAY){

  unsigned long currentMillis = millis();
  bool Zmacknuto = (digitalRead(pin) == LOW); //mozna potreba zmenit


  if(Zmacknuto){
    if(!byloZmacknuto){
          
      pocitej(pocitadlo, pricitano);
      lastTime = currentMillis;
      byloZmacknuto = true;
      }
    else
    //drzime tlacitko
    {
      if(currentMillis - lastTime > DELAY){

        DELAY = REPEAT_DELAY;
        pocitej(pocitadlo, pricitano);
        lastTime = currentMillis;
      }
    }
  }
  //pustili jsme ho ho
  else{
    DELAY = INITIAL_DELAY;
    byloZmacknuto = false;
  }
}  
  
  





  void setup() 
  {
    Serial.begin(9600);
    DELAY1 = INITIAL_DELAY;
    DELAY2 = INITIAL_DELAY;

    for(int i = 0; i < butony_count; i++)
    {
      pinMode(butony[i], INPUT);
    }
    for(int i = 0; i < ledky_count; i++)
    {
      pinMode(ledky[i], OUTPUT);
      digitalWrite(ledky[i], OFF);
    }
  }

 

void loop() 
{
  
  updateCounter(butony[0], lastTime1, stisknuto1, 1, DELAY1);

  updateCounter(butony[1], lastTime2, stisknuto2, 15, DELAY2);
 

}
