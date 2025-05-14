#include "funshield.h"


constexpr int vstupPiny[] = { button1_pin, button2_pin, button3_pin };
constexpr int pocetVstupu = sizeof(vstupPiny) / sizeof(vstupPiny[0]);
constexpr int pocetSegmentu = 4;
constexpr int deset = 10;
constexpr int poziceDesetinneTecky = 1;
const int meritko = 100; 


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

  bool pravePrisklo() {
    return aktualni && !predchozi;
  }
};


int mocnina(int zaklad, int exp) {
  int vysledek = 1;
  int temp = zaklad;
  while (exp > 0) {
    if (exp & 1) vysledek *= temp;
    exp >>= 1;
    temp *= temp;
  }
  return vysledek;
}

int pocetCislic(int zaklad, int hodnota) {
  if (hodnota == 0) return 1;
  int pocet = 0;
  int prah = 1;
  while (prah <= hodnota) {
    prah *= zaklad;
    ++pocet;
  }
  return pocet;
}

// --- Třída pro displej ---
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

// --- Třída pro číselný displej ---
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
    maxCislic = maTecku ? max(pozTecky, pocet) : pocet;
  }

  int cisloNaPozici() {
    int sila = mocnina(deset, pocetSegmentu - aktuSeg - 1);
    return (hodnota % (sila * deset)) / sila;
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
    if (aktivni) {
      if (pocetSegmentu - aktuSeg - 1 <= maxCislic) {
        int cislo = cisloNaPozici();
        if (maTecku && pocetSegmentu - aktuSeg - 1 == pozTecky) {
          zobrazCisloTecka(cislo, aktuSeg);
        } else {
          zobrazCislo(cislo, aktuSeg);
        }
      } else {
        vymaz();
      }

      if (++aktuSeg >= pocetSegmentu) {
        aktuSeg = 0;
      }
    }
  }

  void vypni() {
    aktivni = false;
    vymaz();
  }
};


class Stopky {
private:
  enum Stavy { STOJI, BEZI, MEZICAS } stav;
  unsigned long celkovyCas;
  unsigned long zacatek;
  unsigned long mezicas;

  void aktualizujDisplej() {
    int cas = (stav == MEZICAS) ? mezicas : celkovyCas;
    vypisovac.ukazSDeseti(cas / meritko, poziceDesetinneTecky);

    if (stav == BEZI && (millis() / 500) % 2 == 0) {
      vypisovac.zobraz(0b00000000, 0b00001000);
    }
  }

public:
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

    if (tlacitka[0].pravePrisklo()) { 
      if (stav == STOJI) {
        stav = BEZI;
        zacatek = cas - celkovyCas;
      } else if (stav == BEZI) {
        stav = STOJI;
        celkovyCas = cas - zacatek;
      }
    }

    if (tlacitka[1].pravePrisklo()) { /
      if (stav == BEZI) {
        stav = MEZICAS;
        mezicas = cas - zacatek;
      } else if (stav == MEZICAS) {
        stav = BEZI;
        aktualizujDisplej();
      }
    }

    if (tlacitka[2].pravePrisklo()) { 
      if (stav == STOJI) {
        celkovyCas = 0;
        aktualizujDisplej();
      }
    }
  }
};


CiselnyDisplej vypisovac;
Tlacitko tlacitka[pocetVstupu];
Stopky casovac;


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
