#include "funshield.h"
constexpr int num_digits = 4;

///"""
const byte letterMasks[26] = {
    0b00001000, // A (original: 0b01110111)0
    0b10000011, // B (original: 0b01111100)1
    0b11000110, // C (original: 0b00111001)2
    0b10100001, // D (original: 0b01011110)3
    0b10000110, // E (original: 0b01111001)4
    0b10001110, // F (original: 0b01110001)5
    0b11000010, // G (original: 0b00111101)6
    0b10001011, // H (original: 0b01110100)7
    0b11111001, // I (original: 0b00000100)8
    0b11100001, // J (original: 0b00011110)9
    0b10001111, // K (original: 0b01110101)10
    0b11000111, // L (original: 0b00111000)11
    0b11101010, // M (original: 0b00010101)12
    0b11001000, // N (original: 0b01010100)13
    0b11000000, // O (original: 0b00111111)14
    0b10001100, // P (original: 0b01110011)15
    0b10011000, // Q (original: 0b01100111)16
    0b10101111, // R (original: 0b01010000)17
    0b10010010, // S (original: 0b01101101)18
    0b10000111, // T (original: 0b01111000)19
    0b11000001, // U (original: 0b00111110)20
    0b11100011, // V (original: 0b00011100)21
    0b10010101, // W (original: 0b00011101)22
    0b10001001, // X (original: 0b01110110)23
    0b10001101, // Y (original: 0b01101110)24
    0b10100100  // Z (original: 0b01011011)25
    };
    
//"""


void displayDigit(byte digit, byte pos) {
    digitalWrite(latch_pin, LOW); 
    shiftOut(data_pin, clock_pin, MSBFIRST, digit);
    Serial.println(pos);
    shiftOut(data_pin, clock_pin, MSBFIRST, 1 << (num_digits - (int)(pos) - 1 ));
    digitalWrite(latch_pin, HIGH); 
}

void setup() {
    
    pinMode(latch_pin, OUTPUT);
    pinMode(clock_pin, OUTPUT);
    pinMode(data_pin, OUTPUT);
   
}

void loop() {
    
    for(int i = 0; i < 1000; i++){
        displayDigit(digits[5],3);
        displayDigit(letterMasks[20],2);
        displayDigit(letterMasks[2],1);
        displayDigit(letterMasks[10],0);
    }
    displayDigit(0xff, 0);
    delay(500);
    for(int i = 0; i < 1000; i++){
        displayDigit(letterMasks[24],3);
        displayDigit(letterMasks[14],2);
        displayDigit(letterMasks[20],1);
        displayDigit(0b01111101,0);
    }
    
    
    
  displayDigit(0xff, 0);
        delay(500);
    
    
    
}
