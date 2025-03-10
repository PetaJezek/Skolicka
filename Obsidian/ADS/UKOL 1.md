
# Jde to?
Existuje spostu protipříkladu, kdy není možné aby doputovalo přesně L láhví. Např. pokud L je liché číslo a posloupnost $p_1,\dots,p_n$ obsahuje pouze čísla sudá. Tedy obecně nejde zaručit správnost algoritmu.


## Algoritmus který najde nejbližší počet láhví.

Protože můžeme odklonit pouze jeden úsek, finalní posloupnosti lahví, ktere vezmeme vypadají bud oooooo...... a nebo .....ooooo kde o je znak pro navozene přepravky.
Náš algoritmus tedy bude postupovat ze předu resp. ze zadu a bude přičítat lahve k proměnné součet_předek (resp. součet_zadek). 
