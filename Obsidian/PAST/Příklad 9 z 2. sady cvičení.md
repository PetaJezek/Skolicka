
Pravdepodobnost ze z prvni nadoby vytahneme bily micek je:
$$
\frac{a}{a+b}
$$

Pravdepodobnost ze vytahneme z druhe nadoby pokud jsme prendali bily je:

$$
\frac{a+1}{a+b+1}
$$

A pokud prendame cerny:

$$
\frac{a}{a+b+1}
$$

Tedy muzeme rict ze pravdepodobnost ze vytahneme bily micek $P_{n}$ pro n-tou nadobu muzeme vyjadrit jako:


$$
P_{n}= P_{n-1}\cdot \frac{a+1}{a+b+1} + (1- P_{n-1}) \cdot \frac{a}{a+b+1}
$$

$$
P_{n} = \frac{aP_{n-1} + P_{n-1}+a-aP_{n-1}}{a+b+1} =  \frac{P_{n-1}+a}{a+b+1}
$$

Jelikoz presne zname $P_{1}$, nastavme $n=2$:

$$
P_{2} = \frac{\left( \frac{a}{a+b}+a \right)}{a+b+1}= \frac{a^{2}+ab+a}{a+b}\cdot \frac{1}{a+b+1}
$$
$$
P_{2}= \frac{a}{a+b}
$$
Tedy zjistujeme ze $P_{2}=P_{1}$. A tedy i $P_{n}=P_{n-1}=\dots=P_{1}$ pro $n\in \mathbb{N}$. Nejduleziteji pravdepodobnost se vubec nevztahuje na pocet prechozich nadob. 

Tedy finalni vzorec pravdepodobnosti ze vytahneme v k-te nadobe bily micek je:

$$
P_{k}=\frac{a}{a+b}
$$



