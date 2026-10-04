# Dokumentace pro vývojáře: Hra Amazonky

## 1. Popis problému a celkový přístup
Cílem projektu bylo vytvořit plně funkční konzolovou verzi deskové hry Amazonky s umělou inteligencí (AI), která dokáže plánovat tahy dopředu v reálném čase. 

Hlavní výzvou při vývoji CPU schopné hrát Amazonky je obrovský branching factor. Každý tah se skládá ze dvou fází (pohyb figurky a výstřel šípu), což znamená, že v jednom kole může existovat mnohem více legálních tahů než v šachách. Běžné prohledávání stavového prostoru dochází ke kombinatorické explozi a zpotřebování veškeré paměti.

**Přístup k řešení:**
Problém byl vyřešen na dvou úrovních:
1. **Datové struktury:** Deska není reprezentována standardním líným spojovým seznamem, ale pomocí `Data.Array.Unboxed`. To zajišťuje okamžitý přístup (O(1)) pro čtení i zápis, což je pro algoritmus prohledávající miliony stavů velmi důležité.
2. **Optimalizovaná AI:** Umělá inteligence využívá algoritmus Alfa-Beta prořezávání. Aby bylo možné dosáhnout hloubky prohledávání 2 a více v řádech vteřin, byla navržena odlehčená heuristika. Místo drahého generování všech možných výstřelů šípů heuristika počítá pouze počet volných polí, na která mohou amazonky v daném stavu dojít.

## 2. Struktura kódu a organizace
Kód je napsán v jednom souboru `amazonky.hs` a je logicky rozdělen do několika funkčních bloků.

### Klíčové datové typy
* `Board`: Definováno jako `UArray (Int, Int) Int`. Mapuje 2D souřadnice na celé číslo reprezentující stav políčka (0 = prázdno, 1 = bílý, 2 = černý, 3 = šíp).
* `Pos`: Dvojice `(Int, Int)` reprezentující souřadnici na desce.
* `Move`: Trojice pozic `(Pos, Pos, Pos)` kódující počátek, cíl a dopad šípu.

### Modul herní logiky a stavu
Tyto funkce zajišťují základní mechaniky hry a validaci pravidel:
* `updateBoard`: Přijímá aktuální desku a platný tah. Aplikuje změny na desce a vrací novou desku.
* `checkMoveLegality`: Ověřují zda tah neporušuje žádná pravidla. Zajišťují, že figurka střílí ze své nové pozice a že jí v cestě nestojí žádná překážka.
* `getPath`: Generuje seznam souřadnic mezi dvěma body pro kontrolu volné cesty.

### Modul herní smyčky a IO
Řídí interakci s uživatelem a běh programu:
* `gameLoop`: Hlavní rekurzivní funkce udržující stav partie. Střídá tahy člověka a AI, zajišťuje vykreslení desky (`renderBoard`) a vypisuje text, podle kterého se hráč má řídit.
* `parseMove` / `parseCord`: Zajišťují překlad uživatelského textového vstupu ("D1 D4 D5") na interní souřadnice `Move`.

### Modul umělé inteligence
Jádro rozhodovacího procesu CPU:
* `alphabeta`: Implementace Alfa-Beta prořezávání. Zajišťuje rekurzivní průchod stromem tahů, kde funkce `evaluateMax` a `evaluateMin` maximalizují a minimalizují skóre, čímž odřezávají větve.
* `getBestMove`: Vstupní bod pro AI. Pro všechny aktuální legální tahy vygeneruje skóre pomocí `alphabeta` a vybere tah s nejvyšší hodnotou.
* `getAllLegalMoves`: Generátor tahů. Postupně skládá pohyb amazonek a výstřely šípů pomocí iterativního prohledávání (`walk` a `getReachable`).
* `evaluateBoard`: Rychlá heuristická funkce. Pro daný stav získá pozice všech amazonek (`getPlayerAmazons`) a sečte délky dostupných cest v jejich okolí. Rozdíl mobility obou hráčů vrací jako celkové skóre pozice.