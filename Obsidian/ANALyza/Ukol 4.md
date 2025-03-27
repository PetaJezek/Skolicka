**Příklad 1 (1 bod)**

Najděte množinu hromadných bodů posloupnosti  $a_n = n \cdot \sin\left( \frac{n\pi}{2} \right)$ a určete její $\liminf$ a $\limsup$.

Vysledek $\sin\left( \frac{n\pi}{2} \right)$ muze byt:
- $1$ pro $n \mod 4 = 1$,
- $0$ pro $n \mod 4 \in\{0;2\}$,
- $-1$ pro $n \mod 4= 3$.

Tyto tri podposloupnosti $a_{n}$ se blizi k $\{-n,0,n\}$ a to jsou tedy i vsechny prvky mnoziny $\mathcal{H}$ (hromadne body).

Trivialne $\liminf = -n \quad(-\infty)$ a $\limsup = n \quad(\infty)$.

---

**Příklad 2 (2 body)**

Spočtěte limity posloupností nebo ukažte, že neexistují:

a) $$\lim_{n \to \infty} \sqrt[n]{n^2+1}$$
Pouzijeme vetu o dovuch policajtech.

Víme že pro kladna $n$:
$$
n^2 \leq n^2 +1 \leq 2n^2 
$$
Muzeme tedy napsat:
$$
\sqrt[n]{n^2} \leq \sqrt[n]{n^2+1} \leq \sqrt[n]{2n^2}
$$

Leva strana:
$$
\sqrt[n]{n^2} = (n^2)^{1/n} = n^{2/n}
$$
Prava strana:
$$
\sqrt[n]{2n^2} = (2n^2)^{1/n} = 2^{1/n}\cdot n^{2/n}
$$

Protože víme, že pro $x \in \mathbb{R}: \frac{x}{n}=0$ Můžeme levou i pravou stranu přepsat:

$$
n^{2/n} = n^0=1 \leq \sqrt[n]{n^2+1} \leq 2^{1/n}\cdot n^{2/n} \leq 2^0 \cdot n^0 = 1
$$

$$
\lim_{n \to \infty} \sqrt[n]{n^2+1} = 1
$$



b)
$$
\lim_{n \to \infty} \sqrt[n]{n^2+2^n}
$$

Muzeme prepsat jako:

$$
(n^2+2^n)^{1/n} = n^{2/n} + 2 = n^0 + 2 = 1 +2 = 3
$$

$$
\lim_{n \to \infty} \sqrt[n]{n^2+2^n} = 3
$$


---

**Příklad 3 (2 body)**

Rozhodněte, zda řady konvergují nebo divergují:

a) 
$$ 
\sum_{n=1}^{\infty} \sqrt[n]{ \frac{1}{1000}  }
$$




V tomto připade přičitame stále menší a menší hodnoty, ale nikdy nepřičítáme hodnoty záporné. To znamená, tato řada má limitu v nekonečnu a tedy je divergentní. 
Také limita obecného členu
$$
\lim_{ n \to \infty } a_{n}=​1000^{-\frac{1}{n}}​ = 1000^0 = 1 
$$
je nenula. Takže tato řada je divergentní.



b)
$$ 
\sum_{n=1}^{\infty} \frac{3^{n+1}}{2^{2n-3}} 
$$

$$
\lim_{ n \to \infty }   \frac{3^{n+1}}{2^{2n-3}} =  \lim_{ n \to \infty } \frac{3^n \cdot 3}{2^{2n} \cdot {2}^{-3}} = \lim_{ n \to \infty } \frac{3^n\cdot 3}{2^{2n}}\cdot 8= \lim_{ n \to \infty } 24\cdot \left(\frac{3}{4}\right)^n = 0
$$
Protože $(\frac{3}{4})^n$ jde k nule, celá limita se rovná nule. 

To znamená, že řada konverguje.



---

**Příklad 4 (1 bod)**

Určete limitu rekurentně zadané posloupnosti:

$$
a_1 = 1, \quad a_{n+1} = \frac{a_n^2}{4} + 1.
$$
Predpokladejme, že má vlastní limitu:
$$
L = \lim_{ n \to \infty } a_{n} = \lim_{ n \to \infty } a_{n+1}
$$

Pro $a_{n+1}$ dostavame:
$$
L = \frac{L^2}{4}+1
$$
$$
L^2-4L+4 = 0
$$
$$
(L-2)^2=0
$$
$$
L= 2
$$

Omezenost shora $a_{n} < 2$
$\text{Pro } n=1:$
$$
a_{1} = 1 < 2
$$
To platí.

Indukčně pro $a_{n}<2$:
$$
1) \quad a_{n+1} = \frac{a_n^2}{4} + 1 
$$
$$
2) \quad {\frac{a^2_n}{4}} < 1 \implies  \frac{a^2_n}{4} + 1 < L = 2
$$
Takze posloupnost je omezena ze zhora.
Posloupnost nikdy nemuze mit zaporna cisla takze je urcite omezena 0. Muzeme nahlednout ze cisla posloupnosti se bude stale zvetsovat, a proto muzeme odhadnout, ze bude omezena ze spoda 1.

Monotonnost:
$$
a_{n} < \frac{a^2_{n}}{4}+1
$$
$$
4a_{n} < a^2_{n} + 4 
$$
$$
a^2_{n} -4a_{n} + 4 \geq 0
$$
$$
(a_{n}-2)^2 \geq 0
$$

Druhá mocnina je vždy nezáporná.
Máme dokázano. $L=2$   je vlastní limita rekurzivně zadané posloupnosti:

$$
a_1 = 1, \quad a_{n+1} = \frac{a_n^2}{4} + 1.
$$