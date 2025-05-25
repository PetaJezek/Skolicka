#include "funshield.h"


// Třída pro měření času - umožňuje zjistit, kolik času uplynulo od posledního resetu

class CasMeric {

private:

  unsigned long posledniCas;  // Uložený časový bod pro referenci


public:

  // Nastaví referenční časový bod

  void reset(unsigned long cas) {

    posledniCas = cas;
  }


  // Vrátí počet milisekund, které uplynuly od posledního resetu

  unsigned long ubehlo(unsigned long cas) {

    return cas - posledniCas;
  }
};


// Definice pinů pro tlačítka a počtu vstupů

constexpr int vstupPiny[] = { button1_pin, button2_pin, button3_pin };

constexpr int pocetVstupu = sizeof(vstupPiny) / sizeof(vstupPiny[0]);


// Třída pro obsluhu jednoho tlačítka s detekcí stisknutí

class Tlacitko {

private:

  int index;  // Index tlačítka v poli vstupních pinů

  bool predchozi;  // Předchozí stav tlačítka

  bool aktualni;  // Aktuální stav tlačítka


public:

  // Inicializace tlačítka - nastaví pin jako vstup

  void setup(int i) {

    index = i;

    pinMode(vstupPiny[index], INPUT);

    predchozi = aktualni = false;
  }


  // Přečte aktuální fyzický stav tlačítka (LOW = stisknuto)

  bool stisknuto() {

    return digitalRead(vstupPiny[index]) == LOW;
  }


  // Aktualizuje stavy tlačítka - volá se v každém cyklu

  void nacti() {

    predchozi = aktualni;

    aktualni = stisknuto();
  }


  // Vrátí aktuální stav tlačítka

  bool stav() {

    return aktualni;
  }


  // Detekce vzestupné hrany - tlačítko bylo právě stisknuto

  bool pravePrisklo() {

    return aktualni && !predchozi;
  }
};


// Funkce pro výpočet mocniny pomocí binárního umocňování (efektivnější než cyklus)

int mocnina(int zaklad, int exp) {

  int vysledek = 1;

  int temp = zaklad;


  while (exp > 0) {

    if (exp & 1) {  // Pokud je exp liché

      vysledek *= temp;
    }

    exp >>= 1;  // Vydělí exp dvěma

    temp *= temp;  // Umocní temp na druhou
  }


  return vysledek;
}


// Spočítá počet číslic v daném základu pro zadanou hodnotu

int pocetCislic(int zaklad, int hodnota) {

  if (hodnota == 0) return 1;  // Speciální případ pro nulu


  int pocet = 0;

  while (hodnota > 0) {

    hodnota /= zaklad;

    pocet++;
  }


  return pocet;
}


// Konstanty pro práci s displejem

constexpr int pocetSegmentu = 4;  // 4-místný displej

constexpr int deset = 10;  // Desítková soustava


// Základní třída pro ovládání 7-segmentového displeje

class Displej {

private:

  static const byte prazdnyVzor = 0b11111111;  // Vzor pro prázdný segment

  static const byte vsechnyPozice = 0b00001111;  // Maska pro všechny pozice

  static const byte teckaVzor = 0b01111111;  // Maska pro zobrazení tečky


  // Vrátí bit masku pro konkrétní pozici displeje

  byte poziceVzor(int pozice) {

    return 1 << pozice;
  }


public:

  // Inicializace displeje - nastaví piny pro shift registry

  void setup() {

    pinMode(latch_pin, OUTPUT);

    pinMode(clock_pin, OUTPUT);

    pinMode(data_pin, OUTPUT);

    vymaz();
  }


  // Vymaže displej (zhasne všechny segmenty)

  void vymaz() {

    zobraz(prazdnyVzor, vsechnyPozice);
  }


  // Základní funkce pro zobrazení vzoru na zadaných pozicích

  void zobraz(byte vzor, byte pozice) {

    digitalWrite(latch_pin, LOW);  // Začátek přenosu

    shiftOut(data_pin, clock_pin, MSBFIRST, vzor);  // Pošle vzor segmentů

    shiftOut(data_pin, clock_pin, MSBFIRST, pozice);  // Pošle pozice

    digitalWrite(latch_pin, HIGH);  // Uloží data do registru
  }


  // Zobrazí číslici na zadané pozici

  void zobrazCislo(int cislo, int pozice) {

    zobraz(digits[cislo], poziceVzor(pozice));
  }


  // Zobrazí číslici s tečkou na zadané pozici

  void zobrazCisloTecka(int cislo, int pozice) {

    zobraz(digits[cislo] & teckaVzor, poziceVzor(pozice));
  }
};


// Rozšířená třída displeje pro zobrazování čísel s multiplexováním

class CiselnyDisplej : public Displej {

private:

  int hodnota;  // Zobrazovaná hodnota

  int aktuSeg;  // Aktuálně zobrazovaný segment (pro multiplexování)

  bool aktivni;  // Zda je displej aktivní

  bool maTecku;  // Zda má být zobrazena desetinná tečka

  int pozTecky = 0;  // Pozice desetinné tečky (zprava)

  int maxCislic;  // Maximální počet číslic k zobrazení


  // Spočítá maximální počet číslic včetně desetinné tečky

  void spoctiMaxCislic() {

    int pocet = pocetCislic(deset, hodnota);



    // Pokud má tečku, max číslic je buď počet číslic nebo pozice tečky + 1

    maxCislic = maTecku ? (pocet > pozTecky ? pocet : pozTecky + 1) : pocet;
  }


  // Vrátí číslici na zadané pozici zprava (0 = nejpravější)

  int cisloNaPozici(int poziceZprava) {

    int sila = mocnina(deset, poziceZprava);

    return (hodnota / sila) % deset;
  }
public:

  // Inicializace displeje

  void setup() {

    Displej::setup();

    aktuSeg = 0;

    aktivni = false;
  }


  // Zobrazí celé číslo bez desetinné tečky

  void ukazHodnotu(int h) {

    maTecku = false;

    hodnota = h;

    spoctiMaxCislic();

    aktivni = true;
  }


  // Zobrazí číslo s desetinnou tečkou na zadané pozici

  void ukazSDeseti(int h, int pos) {

    maTecku = true;

    hodnota = h;
    if(pos <4){
          pozTecky = pocetSegmentu - pos;
    }
    else{
      pozTecky = 5;
    }
    
    spoctiMaxCislic();

    aktivni = true;
  }


  // Multiplexování displeje - zobrazí jeden segment a přepne na další

  // Musí se volat dostatečně často pro plynulé zobrazení

  void obnov() {

    if (!aktivni) return;


    if (aktuSeg < pocetSegmentu) {

      int poziceZprava = pocetSegmentu - 1 - aktuSeg;

      // Pokud je pozice mimo rozsah čísla, segment zhasne

      if (poziceZprava >= maxCislic) {

        vymaz();

      } else {

        int cislo = cisloNaPozici(poziceZprava);



        // Zobrazí číslici s tečkou nebo bez ní podle pozice

        if (maTecku && poziceZprava == pozTecky) {

          zobrazCisloTecka(cislo, aktuSeg);

        } else {

          zobrazCislo(cislo, aktuSeg);
        }
      }
    }


    // Přepne na další segment (cyklicky)

    aktuSeg = (aktuSeg + 1) % pocetSegmentu;
  }


  // Vypne displej

  void vypni() {

    aktivni = false;

    vymaz();
  }
};


// Konstanty pro indexy tlačítek

constexpr int tlacStart = 0;  // Tlačítko Start/Stop

constexpr int tlacLap = 1;  // Tlačítko pro mezičas

constexpr int tlacReset = 2;  // Tlačítko Reset

// Pozice desetinné tečky (1 = druhá pozice zprava)


// Hlavní třída stopek

class Stopky {

private:

  // Stavy stopek

  enum Stavy { STOJI,
               BEZI,
               MEZICAS } stav;

  unsigned long celkovyCas;  // Celkový naměřený čas

  unsigned long zacatek;  // Časový bod spuštění

  unsigned long mezicas;  // Uložený mezičas


  CiselnyDisplej& displej;  // Reference na displej

  Tlacitko (&tlacitka)[pocetVstupu];  // Reference na pole tlačítek


  // Aktualizuje zobrazení na displeji

  void aktualizujDisplej() {

    // Zobrazuje mezičas nebo aktuální čas podle stavu

    unsigned long cas = (stav == MEZICAS) ? mezicas : celkovyCas;
    bool ctyriCifry = false;
    int rad = 1;
    
    while(!ctyriCifry){
      int zbytek = cas / 10000;
      
      if(zbytek == 0){
        ctyriCifry = true;
      }
      else{
        cas = cas / 10;
        rad++;
      }

    }
    int displayValue = cas;
    displej.ukazSDeseti(displayValue, rad);
  }


public:

  // Konstruktor - přijímá reference na displej a tlačítka

  Stopky(CiselnyDisplej& d, Tlacitko (&tl)[pocetVstupu])

    : displej(d), tlacitka(tl) {}


  // Inicializace stopek

  void setup(unsigned long cas) {

    stav = STOJI;

    zacatek = mezicas = cas;

    celkovyCas = 0;

    aktualizujDisplej();
  }


  // Hlavní funkce stopek - zpracovává tlačítka a aktualizuje čas

  void zpracuj(unsigned long cas) {

    // Pokud stopky běží, aktualizuje celkový čas

    if (stav == BEZI) {

      celkovyCas = cas - zacatek;

      aktualizujDisplej();
    }


    // Tlačítko Start/Stop

    if (tlacitka[tlacStart].pravePrisklo()) {

      if (stav == STOJI) {

        // Spuštění stopek - zachová předchozí čas

        stav = BEZI;

        zacatek = cas - celkovyCas;

      } else if (stav == BEZI) {

        // Zastavení stopek

        stav = STOJI;

        celkovyCas = cas - zacatek;
      }
    }


    // Tlačítko pro mezičas

    if (tlacitka[tlacLap].pravePrisklo()) {

      if (stav == BEZI) {

        // Zobrazení mezičasu (stopky běží dál)

        stav = MEZICAS;

        mezicas = cas - zacatek;

      } else if (stav == MEZICAS) {

        // Návrat k aktuálnímu času

        stav = BEZI;

        aktualizujDisplej();
      }
    }


    // Tlačítko Reset - pouze když stopky stojí

    if (tlacitka[tlacReset].pravePrisklo()) {

      if (stav == STOJI) {

        celkovyCas = 0;

        aktualizujDisplej();
      }
    }
  }
};


// Globální objekty

CiselnyDisplej vypisovac;  // Displej pro zobrazení času

Tlacitko tlacitka[pocetVstupu];  // Pole tlačítek

Stopky casovac(vypisovac, tlacitka);  // Hlavní objekt stopek


// Inicializace Arduino

void setup() {

  Serial.begin(9600);

  // Inicializace všech tlačítek

  for (int i = 0; i < pocetVstupu; ++i) {

    tlacitka[i].setup(i);
  }

  vypisovac.setup();  // Inicializace displeje

  casovac.setup(millis());  // Inicializace stopek s aktuálním časem
}


// Hlavní smyčka Arduino

void loop() {

  unsigned long ted = millis();  // Získání aktuálního času


  // Čtení stavu všech tlačítek

  for (int i = 0; i < pocetVstupu; ++i) {

    tlacitka[i].nacti();
  }


  casovac.zpracuj(ted);  // Zpracování logiky stopek

  vypisovac.obnov();  // Aktualizace displeje (multiplexování)
}