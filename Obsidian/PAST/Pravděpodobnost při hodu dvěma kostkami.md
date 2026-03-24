

Uvažujme náhodný pokus – dvojnásobný hod klasickou šestibokou kostkou. Definujeme následující jevy:

* **$SD$**: „součet hozených čísel je 10“
* **$PS$**: „v prvním hodu padla šestka“
* **$NS$**: „v některém hodu padla šestka“ (alespoň v jednom)

### Úkol:
1. Určete pravděpodobnosti základních jevů:
   $$P(SD), P(PS), P(NS)$$
2. Vypočítejte všechny podmíněné pravděpodobnosti mezi těmito jevy:
   * $P(SD|PS)$ a $P(PS|SD)$
   * $P(SD|NS)$ a $P(NS|SD)$
   * $P(PS|NS)$ a $P(NS|PS)$
3. Určete pravděpodobnosti typu $P(A|A)$ pro všechny tři jevy.
---

1. Počet elementarnich jevu v jevu deleno celkovym poctem  moznych elemntarnich jevu (hodu). 
 
$$
P(SD) = \frac{3}{36}=\frac{1}{12}
$$
$$
P(PS)= \frac{1}{6}
$$
$$
P(NS) = \frac{11}{36}
$$


2. Podle definice

$$
P(SD | PS) = \frac{\frac{1}{36}}{\frac{1}{6}}=\frac{1}{6}
$$
$$
P(SD| NS) = \frac{\frac{2}{36}}{\frac{11}{36}}=\frac{2}{11}
$$
$$
P(PS|SD) =  P(SD | PS) \cdot \frac{P(PS)}{P(SD)} = \frac{1}{6}\cdot \frac{1}{6}\cdot 12 = \frac{1}{3}
$$

$$
P(PS|NS) = \frac{6}{11}
$$

$$
P(NS|SD) =  P(SD| NS)  \cdot \frac{P(NS)}{P(SD)}= \frac{2}{11} \cdot \frac{11}{36} \cdot 12 = \frac{2}{3} 
	$$

$$
P(NS|PS) = 1
$$

$$
P(SD|SD) = 1
$$
$$
P(PS|PS) = 1
$$
$$
P(NS|NS) = 1
$$


