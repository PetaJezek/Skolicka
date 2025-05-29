#include "funshield.h"
#include "input.h"


// map of letter glyphs
constexpr byte LETTER_GLYPH[] {
  0b10001000,   // A
  0b10000011,   // b
  0b11000110,   // C
  0b10100001,   // d
  0b10000110,   // E
  0b10001110,   // F
  0b10000010,   // G
  0b10001001,   // H
  0b11111001,   // I
  0b11100001,   // J
  0b10000101,   // K
  0b11000111,   // L
  0b11001000,   // M
  0b10101011,   // n
  0b10100011,   // o
  0b10001100,   // P
  0b10011000,   // q
  0b10101111,   // r
  0b10010010,   // S
  0b10000111,   // t
  0b11000001,   // U
  0b11100011,   // v
  0b10000001,   // W
  0b10110110,   // ksi
  0b10010001,   // Y
  0b10100100,   // Z
};
constexpr byte EMPTY_GLYPH = 0b11111111;
constexpr int pocetSegmentu = 4; 
constexpr unsigned int scrollingInterval = 300;

byte charToGlyph(char ch)
{
  byte glyph = EMPTY_GLYPH;
  if (isAlpha(ch)) {
    glyph = LETTER_GLYPH[ ch - (isUpperCase(ch) ? 'A' : 'a') ];
  }
  // similarly, you can extend this function for digits
  // if (isDigit(ch))
  //   glyph = ....[ ch - '0' ];
  // ....

  return glyph;
};
byte numToGlyph(int i){
  return digits[i];
}

class Display {
private:
  
  static const byte vsechnyPozice = 0b00001111;
  //static const byte teckaVzor = 0b01111111;

  char view[pocetSegmentu] = {' ', ' ', ' ', ' '};
  int aktuSeg = 0;

  byte poziceVzor(int pozice) {
    return 1 << pozice;
  }

  void zobraz(byte vzor, byte pozice) {
    digitalWrite(latch_pin, LOW);
    shiftOut(data_pin, clock_pin, MSBFIRST, vzor);
    shiftOut(data_pin, clock_pin, MSBFIRST, pozice);
    digitalWrite(latch_pin, HIGH);
  }

  char charNaPozici(int poziceZprava) {
    return view[pocetSegmentu - poziceZprava - 1];
  }
  byte getGlyph(char ch)
  {
    if (ch >= '0' && ch <= '9')
    {
      return numToGlyph(ch - '0');
    } 
    return charToGlyph(ch);
  }

public:
  void setup() {
    pinMode(latch_pin, OUTPUT);
    pinMode(clock_pin, OUTPUT);
    pinMode(data_pin, OUTPUT);
    vymaz();
  }

  void vymaz() {
    zobraz(EMPTY_GLYPH, vsechnyPozice);
    for (int i = 0; i < pocetSegmentu; i++) {
      view[i] = ' ';
    }
  }

  void nastavView(const char* novaData) {
    for (int i = 0; i < pocetSegmentu; i++) {
      view[i] = *novaData++;
      
    }
  }

  void obnov() {
    char ch = charNaPozici(pocetSegmentu - 1 - aktuSeg);
    byte vzor = getGlyph(ch);

    zobraz(vzor, poziceVzor(aktuSeg));
    aktuSeg = (aktuSeg + 1) % pocetSegmentu;
  }
};


class Scroller
{
  private:
    
    
    const char* scrollPtr;       // Aktuální pozice pro scrollování
    bool zobrazenaNeprazdnaZprava;
  
  bool vsePozicePrazdne() 
  {
    for (int i = 0; i < pocetSegmentu; i++) {
      if (view[i] != ' ') {
        return false;
      }
    }
    return true;
  }
public:
  char view[pocetSegmentu];
  bool aktivni = false; 
  void setup()
  {
      scrollPtr = nullptr;
      zobrazenaNeprazdnaZprava = false;
      for (int i = 0; i < pocetSegmentu; i++) {
      view[i] = ' ';
    }
  }
  void setNewMessage(const char* msg)
  {
    //Serial.println("Nastavuju Novou zpravu");
    scrollPtr = msg;
    aktivni = true;
    zobrazenaNeprazdnaZprava = true;

    for (int i = 0; i < pocetSegmentu; i++) {
      view[i] = ' ';
    }
  }
  void scroll()
  {
    if (scrollPtr == nullptr || !aktivni) return;
      
      // Posuneme všechny znaky v view o jednu pozici doleva
      for (int i = 0; i < pocetSegmentu - 1; i++)
      {
        view[i] = view[i + 1];
      }

      if(*scrollPtr != '\0'){
        view[pocetSegmentu-1] = *scrollPtr++;
        
      }
      else{
        //jsme na konci zpravy
        view[pocetSegmentu-1] = ' ';

        if (vsePozicePrazdne())
        {
          aktivni = false;
        }
      }
  }

};


class 
/** 
 * Convert a chararcter to a glyph. If character is not letter, empty glyph is displayed instead.
 * @param ch character to be displayed
 * return value: a glyph to be displayed using time multiplex
 * hint: use/extend your class (or functions) for multiplexind the display developed in previous labs
 */




SerialInputHandler input;
Display display;
Scroller scroller;

void setup() {
  display.setup();
  scroller.setup();
  input.initialize();
   Serial.begin(9600); 
};

void loop() 
{  
  unsigned long now = millis();
  static unsigned long lastScrollTime = now;
  
  input.updateInLoop();
  if(!scroller.aktivni){
      Serial.println("Nastavuju zpravu");
      const char* newMessage = input.getMessage();
      if (newMessage != nullptr) {

      scroller.setNewMessage(newMessage);
      }
  }
  if(now - lastScrollTime > scrollingInterval){
    lastScrollTime += scrollingInterval;
    scroller.scroll();
  }
  display.nastavView(scroller.view); 
  display.obnov();
}
