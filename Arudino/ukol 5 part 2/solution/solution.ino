#include "funshield.h"

// Třída pro měření času - umožňuje zjistit, kolik času uplynulo od posledního resetu
class CasMeric {
private:
  unsigned long posledniCas; // Uložený časový bod pro referenci

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
  int index;        // Index tlačítka v poli vstupních pinů
  bool predchozi;   // Předchozí stav tlačítka
  bool aktualni;    // Aktuální stav tlačítka

public:
  // Inicializace tlačítka - nastaví pin jako vstup
  void setup(int i) {
    index = i;
    pinMode(vstupPiny[index], INPUT);
    predchozi = aktualni = false;
  }
  //------------------//

  // Aktualizuje stavy tlačítka - volá se v každém cyklu
  bool nacti() {
    predchozi = aktualni;
    aktualni = (digitalRead(vstupPiny[index]) == LOW);
    return praveStisknuto();
  }

  
  // Detekce vzestupné hrany - tlačítko bylo právě stisknuto
  bool praveStisknuto() {
    return aktualni && !predchozi;
  }
};

// Funkce pro výpočet mocniny pomocí binárního umocňování (efektivnější než cyklus)
int mocnina(int zaklad, int exp) {
  int vysledek = 1;
  int temp = zaklad;

  while (exp > 0) {
    if (exp & 1) {          // Pokud je exp liché
      vysledek *= temp;
    }
    exp >>= 1;              // Vydělí exp dvěma
    temp *= temp;           // Umocní temp na druhou
  }

  return vysledek;
}

// Spočítá počet číslic v daném základu pro zadanou hodnotu
int pocetCislic(int zaklad, int hodnota) {
  if (hodnota == 0) return 1; 

  int pocet = 0;
  while (hodnota > 0) {
    hodnota /= zaklad;
    pocet++;
  }

  return pocet;
}

// Konstanty pro práci s displejem
constexpr int pocetSegmentu = 4;  // 4-místný displej
constexpr int soustava = 10;         // Desítková soustava

// Základní třída pro ovládání 7-segmentového displeje
class Displej {
private:
  static const byte prazdnyVzor = 0b11111111;  // Vzor pro prázdný segment
  static const byte vsechnyPozice = 0b00001111; // Maska pro všechny pozice
  static const byte teckaVzor = 0b01111111;     // Maska pro zobrazení tečky


  // Základní funkce pro zobrazení vzoru na zadaných pozicích
  void zobraz(byte vzor, byte pozice) {
    digitalWrite(latch_pin, LOW);                           // Začátek přenosu
    shiftOut(data_pin, clock_pin, MSBFIRST, vzor);         // Pošle vzor segmentů
    shiftOut(data_pin, clock_pin, MSBFIRST, pozice);       // Pošle pozice
    digitalWrite(latch_pin, HIGH);                          // Uloží data do registru
  }


  // Vrátí bit masku pro konkrétní pozici displeje
  // byte poziceVzor(int pozice) {
  //   return 1 << pozice;
  // }

protected:
  void zobrazCislo(int cislo, int pozice) {
    zobraz(digits[cislo], 1 << pozice);
  }

  void zobrazCisloTecka(int cislo, int pozice) {
    zobraz(digits[cislo] & teckaVzor, 1 << pozice);
  }

public:
  virtual ~Displej() {}

  // Inicializace displeje - nastaví piny pro shift registry
  virtual void setup() {
    pinMode(latch_pin, OUTPUT);
    pinMode(clock_pin, OUTPUT);
    pinMode(data_pin, OUTPUT);
    vymaz();
  }

  // Vymaže displej (zhasne všechny segmenty)
  virtual void vymaz() {
    zobraz(prazdnyVzor, vsechnyPozice);
  }
};

// Rozšířená třída displeje pro zobrazování čísel s multiplexováním
class CiselnyDisplej : public Displej {
private:
  int hodnota = 0;      // Zobrazovaná hodnota
  int aktuSeg;      // Aktuálně zobrazovaný segment (pro multiplexování)
  bool aktivni;     // Zda je displej aktivní
  int pozTecky;     // Pozice desetinné tečky (zprava)
  int maxCislic;    // Maximální počet číslic k zobrazení

  // Spočítá maximální počet číslic včetně desetinné tečky
  void spoctiMaxCislic() {
    int pocet = pocetCislic(soustava, hodnota);
    
    // Pokud má tečku, max číslic je buď počet číslic nebo pozice tečky + 1
    maxCislic = ( -1 < pozTecky && pozTecky < 4 ) ? (pocet > pozTecky ? pocet : pozTecky + 1) : pocet;
  }

  // Vrátí číslici na zadané pozici zprava (0 = nejpravější)
  int cisloNaPozici(int poziceZprava) {
    int mocni = mocnina(soustava, poziceZprava);
    return (hodnota / mocni) % soustava;
  }

public:

  // Inicializace displeje
  void setup() override {
    Displej::setup();
    aktuSeg = 0;
    aktivni = false;
    obnov();
  }
  // Nastaveni hondnoty displeje
  void nastavHodnotu(unsigned long value){

    //prevod hodnoty na destiky sekundy
    hodnota = value / 100;
    aktivni = true;
    ukazSDeseti(hodnota, 1);
  }
  // Zobrazí celé číslo bez desetinné tečky
  void ukazHodnotu(int h) {
    pozTecky = -1;
    hodnota = h;
    spoctiMaxCislic();
    aktivni = true;
  }

  // Zobrazí číslo s desetinnou tečkou na zadané pozici
  void ukazSDeseti(int h, int tecka) {
    hodnota = h;
    pozTecky = tecka;  
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
        if ((-1< pozTecky  && pozTecky < 4) && poziceZprava == pozTecky) {
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
constexpr int tlacStart = 0;    // Tlačítko Start/Stop
constexpr int tlacLap = 1;      // Tlačítko pro mezičas
constexpr int tlacReset = 2;    // Tlačítko Reset


// Hlavní třída stopek
class Stopky {
private:
  // Stavy stopek
  enum class Stav { STOJI, BEZI, MEZICAS };
  Stav stav = Stav::STOJI;

  unsigned long celkovyCas;  // Celkový naměřený čas
  unsigned long zacatek;     // Časový bod spuštění
  unsigned long mezicas;     // Uložený mezičas
  


  // Aktualizuje hodnotu kterou chceme predat displeji
  void outputStopek() {
    // Zobrazuje mezičas nebo aktuální čas podle stavu
    displayValue = (stav == Stav::MEZICAS) ? mezicas : celkovyCas;

  }

public:
  // Konstruktor - přijímá reference na displej a tlačítka
  unsigned long displayValue;

  // Inicializace stopek
  void setup(unsigned long cas) {
    stav = Stav::STOJI;
    zacatek = mezicas = cas;
    celkovyCas = 0;
  }

  // Hlavní funkce stopek - zpracovává tlačítka a aktualizuje čas
  void aktualizuj(unsigned long cas){
       if (stav == Stav::BEZI) {
        celkovyCas += (cas - zacatek);
        zacatek = cas;
    }
    outputStopek();
  }

  void zpracuj(unsigned long cas, int indexTlacitka){

   
    switch(indexTlacitka)
    {
      case 0: // tlačítko start/stop

        if (stav == Stav::STOJI) {
          stav = Stav::BEZI;
          zacatek = cas;
        } else if (stav == Stav::BEZI) {
          stav = Stav::STOJI;
          Serial.print("PRED:");
          Serial.println(celkovyCas);
          celkovyCas += (cas - zacatek);

          Serial.println(cas);
          Serial.println(zacatek);
          Serial.print("PO:");
          Serial.println(celkovyCas);
        }
        break;

      case 1: // tlačítko mezicas
        if (stav == Stav::BEZI) {
          mezicas = celkovyCas + (cas - zacatek);
          stav = Stav::MEZICAS;
        }
        else if(stav == Stav::MEZICAS){
          stav= Stav::BEZI;
        }
        break;

      case 2: // tlačítko reset
        if(stav == Stav::STOJI){
          stav = Stav::STOJI;
          celkovyCas = 0;
          zacatek = 0;
          mezicas = 0;
        }
        break;
      
    }
    
  }
 
};

// Globální objekty
CiselnyDisplej vypisovac;                    // Displej pro zobrazení času
Tlacitko tlacitka[pocetVstupu];             // Pole tlačítek
Stopky casovac;        // Hlavní objekt stopek

// Inicializace Arduino
void setup() {
  Serial.begin(9600);
  // Inicializace všech tlačítek
  for (int i = 0; i < pocetVstupu; ++i) {
    tlacitka[i].setup(i);

  }
  vypisovac.setup();           // Inicializace displeje
  casovac.setup(millis());     // Inicializace stopek s aktuálním časem
}

// Hlavní smyčka Arduino
void loop() {
  
  unsigned long ted = millis();  // Získání aktuálního času

  // Čtení stavu všech tlačítek

  for (int i = 0; i < pocetVstupu; ++i) {
    bool stisknuto = tlacitka[i].nacti();
    if(stisknuto){
      casovac.zpracuj(ted, i);
      Serial.print("Zpracovam:");
      Serial.println(i);
      Serial.println(casovac.displayValue);
    }
  }
  casovac.aktualizuj(ted);
  vypisovac.nastavHodnotu(casovac.displayValue);
  vypisovac.obnov();          // Aktualizace displeje (multiplexování)
}