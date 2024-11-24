### 1. Definujeme množiny:

- A je množina čísel dělitelných 8.
-  je množina čísel dělitelných 12.
- C je množina čísel dělitelných 15.

Počet čísel mezi 1 a 500, která nejsou dělitelná žádným z těchto čísel, spočítáme jako:

Počet$= 500 − ∣A∪B∪C∣$


Pomocí principu inkluze a exkluze spočítáme $|A \cup B \cup C|$ jako:

$∣A∪B∪C∣ = ∣A∣+∣B∣+∣C∣−∣A∩B∣−∣A∩C∣−∣B∩C∣+∣A∩B∩C∣$

### 2. Spočítáme jednotlivé členy:

- Počet čísel dělitelných 8 je $\left\lfloor \frac{500}{8} \right\rfloor = 62$
- Počet čísel dělitelných 12 je $\left\lfloor \frac{500}{12} \right\rfloor = 41$
- Počet čísel dělitelných 15 je $\left\lfloor \frac{500}{15} \right\rfloor = 33$
- Počet čísel dělitelných 8 a 12 (tedy dělitelných 24) je $\left\lfloor \frac{500}{24} \right\rfloor = 20$
- Počet čísel dělitelných 8 a 15 (tedy dělitelných 120) je $\left\lfloor \frac{500}{120} \right\rfloor = 4$
- Počet čísel dělitelných 12 a 15 (tedy dělitelných 60) je $\left\lfloor \frac{500}{60} \right\rfloor = 8$
- Počet čísel dělitelných 8, 12 a 15 (tedy dělitelných 120) je $\left\lfloor \frac{500}{120} \right\rfloor = 4$

### 3. Vypočítáme $|A \cup B \cup C|$:

$∣A∪B∪C∣=62+41+33−20−4−8+4=108$

### 4. Počet čísel, která nejsou dělitelná 8, 12 nebo 15:

Počet$=500−108=392$

Tedy počet přirozených čísel mezi 1 a 500, která nejsou dělitelná čísly 8, 12 a 15, je **392**.