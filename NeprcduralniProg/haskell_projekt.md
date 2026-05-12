# Návrh semestrálního projektu: Hra Amazonky

**Student:** Petr Ježek  
**Předmět:** Neprocedurální programování  
**Datum:** 4. května 2026  
**Technologie:** Haskell 

---

## 1. Popis problému
Cílem projektu je implementace deterministické deskové hry pro dva hráče s názvem **Amazonky**. Hra se odehrává na čtvercové desce. Každý hráč ovládá několik figur.

**Mechanika:**
Tah se skládá ze dvou fází:
1.  **Pohyb:** Amazonka se pohne jako šachová dáma (libovolný počet polí vodorovně, svisle nebo diagonálně), nesmí však přeskočit jinou figuru ani blokované pole.
2.  **Střelba:** Z místa, kde Amazonka ukončila pohyb, vystřelí "šíp" (opět ve směru šachové dámy). Pole, kam šíp dopadne, se stává trvale zablokovaným (tzv. "spálená země").

Hra končí v okamžiku, kdy hráč, který je na tahu, nemůže provést žádný legální pohyb. Tento hráč prohrává.

---

## 2. Formalizace problému
Problém lze definovat jako stavový prostor $S$, kde každý stav je reprezentován trojicí $S = (B, Q, P)$:
*   **$B$ (Board):** Matice $n \times n$ reprezentující stav polí (volno, obsazeno bílou/černou amazonkou, zablokováno šípem).
*   **$Q$ (Queens):** Množina aktuálních souřadnic všech aktivních figur.
*   **$P$ (Player):** Identifikátor hráče, který je aktuálně na tahu.

Přechodová funkce $\delta: S \rightarrow S'$ je definována tahem $m = (q_{start}, q_{end}, a_{pos})$, kde $q_{end}$ je nová pozice figury a $a_{pos}$ je pozice dopadu šípu.

Koncový stav nastává, pokud pro aktuálního hráče platí:
$$\{m \in \text{Moves} \mid \text{is\_legal}(m, S)\} = \emptyset$$

---

## 3. Návrh algoritmu
Vzhledem k deterministické povaze a vysokému větvení hry bude implementována umělá inteligence využívající následující techniky:

*   **Minimax s Alpha-Beta prořezáváním:** Základní algoritmus pro prohledávání stromu herních stavů.
*   **Heuristická funkce:** Protože Amazonky nelze vyhrát "vzetím figur", heuristika se zaměří na:
    1.  **Mobilitu:** Počet dostupných tahů pro vlastní figury vs. soupeřovy.
    2.  **Teritorialitu:** Rozdělení desky pomocí BFS (Breadth-First Search) pro určení, kolik polí je "blíže" kterému hráči.
*   **Líné vyhodnocování:** Efektivní generování herního stromu do určité hloubky.

---

## 4. Specifikace vstupů a výstupů
### Vstup:
*   Při startu: Velikost desky a volba, zda hráč začíná nebo hraje proti AI.
*   Během hry: Souřadnice tahu zadávané uživatelem v textovém formátu (např. `a4-b5;d7`, což znamená přesun z `a4` na `b5` a výstřel na `d7`).

### Výstup:
*   Reprezentace herní desky po každém tahu (ASCII grid).
*   Seznam možných tahů v případě chyby uživatele.
*   Stav AI (např. "AI přemýšlí...", zvolený tah a hodnocení pozice).

---

## 5. Popis rozhraní
Program bude realizován jako **interaktivní konzolová aplikace**. 
*   **Zobrazení:** Deska bude vykreslována pomocí textových znaků (např. `W` pro bílé amazonky, `B` pro černé, `X` pro zablokovaná pole).
*   **Interakce:** Uživatel zadává příkazy do standardního vstupu. Součástí bude i nápověda (`help`), která vypíše aktuální pravidla nebo doporučení AI.

