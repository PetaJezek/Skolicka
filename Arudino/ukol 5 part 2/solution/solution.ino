#include "funshield.h"

class CasMeric {
private:
  unsigned long posledniCas;

public:
  void reset(unsigned long cas) {
    posledniCas = cas;
  }

  unsigned long ubehlo(unsigned long cas) {
    return cas - posledniCas;
  }
};

constexpr int vstupPiny[] = { button1_pin, button2_pin, button3_pin };
constexpr int pocetVstupu = sizeof(vstupPiny) / sizeof(vstupPiny[0]);

class Tlacitko {
private:
  int index;
  bool predchozi;
  bool aktualni;

public:
  void setup(int i) {
    index = i;
    pinMode(vstupPiny[index], INPUT);
    predchozi = aktualni = false;
  }

  bool stisknuto() {
    return digitalRead(vstupPiny[index]) == LOW;
  }

  void nacti() {
    predchozi = aktualni;
    aktualni = stisknuto();
  }

  bool stav() {
    return aktualni;
  }

  bool pravePrisklo() {
    return aktualni && !predchozi;
  }
};

int mocnina(int zaklad, int exp) {
  int vysledek = 1;
  int temp = zaklad;

  while (exp > 0) {
    if (exp & 1) {
      vysledek *= temp;
    }
    exp >>= 1;
    temp *= temp;
  }

  return vysledek;
}

int pocetCislic(int zaklad, int hodnota) {
  if (hodnota == 0) return 1; 

  int pocet = 0;
  while (hodnota > 0) {
    hodnota /= zaklad;
    pocet++;
  }

  return pocet;
}

constexpr int pocetSegmentu = 4;
constexpr int deset = 10;

class Displej {
private:
  static const byte prazdnyVzor = 0b11111111;
  static const byte vsechnyPozice = 0b00001111;
  static const byte teckaVzor = 0b01111111;

  byte poziceVzor(int pozice) {
    return 1 << pozice;
  }

public:
  void setup() {
    pinMode(latch_pin, OUTPUT);
    pinMode(clock_pin, OUTPUT);
    pinMode(data_pin, OUTPUT);
    vymaz();
  }

  void vymaz() {
    zobraz(prazdnyVzor, vsechnyPozice);
  }

  void zobraz(byte vzor, byte pozice) {
    digitalWrite(latch_pin, LOW);
    shiftOut(data_pin, clock_pin, MSBFIRST, vzor);
    shiftOut(data_pin, clock_pin, MSBFIRST, pozice);
    digitalWrite(latch_pin, HIGH);
  }

  void zobrazCislo(int cislo, int pozice) {
    zobraz(digits[cislo], poziceVzor(pozice));
  }

  void zobrazCisloTecka(int cislo, int pozice) {
    zobraz(digits[cislo] & teckaVzor, poziceVzor(pozice));
  }
};

class CiselnyDisplej : public Displej {
private:
  int hodnota;
  int aktuSeg;
  bool aktivni;
  bool maTecku;
  int pozTecky;
  int maxCislic;

  void spoctiMaxCislic() {
    int pocet = pocetCislic(deset, hodnota);
    
    maxCislic = maTecku ? (pocet > pozTecky ? pocet : pozTecky + 1) : pocet;
  }

  int cisloNaPozici(int poziceZprava) {
    int sila = mocnina(deset, poziceZprava);
    return (hodnota / sila) % deset;
  }

public:
  void setup() {
    Displej::setup();
    aktuSeg = 0;
    aktivni = false;
  }

  void ukazHodnotu(int h) {
    maTecku = false;
    hodnota = h;
    spoctiMaxCislic();
    aktivni = true;
  }

  void ukazSDeseti(int h, int tecka) {
    maTecku = true;
    hodnota = h;
    pozTecky = tecka;  
    spoctiMaxCislic();
    aktivni = true;
  }

  void obnov() {
    if (!aktivni) return;

    if (aktuSeg < pocetSegmentu) {
      
      int poziceZprava = pocetSegmentu - 1 - aktuSeg;
      
      
      if (poziceZprava >= maxCislic) {
        vymaz();
      } else {
        int cislo = cisloNaPozici(poziceZprava);
        
        
        if (maTecku && poziceZprava == pozTecky) {
          zobrazCisloTecka(cislo, aktuSeg);
        } else {
          zobrazCislo(cislo, aktuSeg);
        }
      }
    }

    aktuSeg = (aktuSeg + 1) % pocetSegmentu;
  }

  void vypni() {
    aktivni = false;
    vymaz();
  }
};

constexpr int tlacStart = 0;
constexpr int tlacLap = 1;
constexpr int tlacReset = 2;
constexpr int poziceDesetinneTecky = 1; 

class Stopky {
private:
  enum Stavy { STOJI, BEZI, MEZICAS } stav;
  unsigned long celkovyCas;
  unsigned long zacatek;
  unsigned long mezicas;

  CiselnyDisplej& displej;
  Tlacitko (&tlacitka)[pocetVstupu];

  void aktualizujDisplej() {
   
    unsigned long cas = (stav == MEZICAS) ? mezicas : celkovyCas;
    int displayValue = cas / 100; 
    
    displej.ukazSDeseti(displayValue, poziceDesetinneTecky);
  }

public:
  Stopky(CiselnyDisplej& d, Tlacitko (&tl)[pocetVstupu])
    : displej(d), tlacitka(tl) {}

  void setup(unsigned long cas) {
    stav = STOJI;
    zacatek = mezicas = cas;
    celkovyCas = 0;
    aktualizujDisplej();
  }

  void zpracuj(unsigned long cas) {
    if (stav == BEZI) {
      celkovyCas = cas - zacatek;
      aktualizujDisplej();
    }

    if (tlacitka[tlacStart].pravePrisklo()) {
      if (stav == STOJI) {
        stav = BEZI;
        zacatek = cas - celkovyCas;
      } else if (stav == BEZI) {
        stav = STOJI;
        celkovyCas = cas - zacatek;
      }
    }

    if (tlacitka[tlacLap].pravePrisklo()) {
      if (stav == BEZI) {
        stav = MEZICAS;
        mezicas = cas - zacatek;
      } else if (stav == MEZICAS) {
        stav = BEZI;
        aktualizujDisplej();
      }
    }

    if (tlacitka[tlacReset].pravePrisklo()) {
      if (stav == STOJI) {
        celkovyCas = 0;
        aktualizujDisplej();
      }
    }
  }
};

CiselnyDisplej vypisovac;
Tlacitko tlacitka[pocetVstupu];
Stopky casovac(vypisovac, tlacitka);

void setup() {
  for (int i = 0; i < pocetVstupu; ++i) {
    tlacitka[i].setup(i);
  }
  vypisovac.setup();
  casovac.setup(millis());
}

void loop() {
  unsigned long ted = millis();

  for (int i = 0; i < pocetVstupu; ++i) {
    tlacitka[i].nacti();
  }

  casovac.zpracuj(ted);
  vypisovac.obnov();
}