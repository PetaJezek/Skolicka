Muj tip pred vypoctem: 

$$
P(A) = 0.4
$$


Kandidati $A, B$

Ze zadani ziskavame 

$P(E|A)=0.7$, 
$P(E|B)=0.4$, 
$P(A|E)=0.6$, 
$P(B|E) = 1- P(A|E) = 0.4$

A hledame $P(A)$.



$$
P(A|E) = \frac{P(E|A)\cdot P(A)}{P(E)}
$$

$$
P(B|E) = \frac{P(E|B)\cdot P(B)}{P(E)}
$$

Po prevedeni $P(E)$ na levou stranu a s vyuzitim porovnavaci metody:


$$
\frac{P(E|A)\cdot P(A)}{P(A|E)} = \frac{P(E|B)\cdot P(B)}{P(B|E)}

$$

Dosadime zname hodnoty:

$$
\frac{0.7P(A)}{0.6} = \frac{0.4P(B)}{0.4}
$$
$$
\frac{7}{6}P(A)=P(B)
$$

A ted muzeme dosadit do posledni rovnice, kterou jsme nezminili:

$$
1=P(A)+P(B) = P(A)+ \frac{7}{6} P(A) = \frac{13}{6}P(A)
$$
Z toho ziskavame:

$$
P(A) = \frac{6}{13}, \quad P(B) = \frac{7}{13}
$$