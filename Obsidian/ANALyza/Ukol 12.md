
Uvažujme funkci $f : \mathbb{R} \to \mathbb{R}$ definovanou vzorcem  
$$
f(x) = x + (|x| - 1)^2.
$$

**a)** V kterých bodech $\mathbb{R}$ má tato funkce vlastní derivaci?


$f$ muzeme prepsat na:
$$
f(x) = x + x^2 -2\left| x \right| +1
$$

Budeme funkci vysetrovat na prechodu  intervalu:
$$
I = (-\infty ;0); \quad J= <0;\infty)
$$
Tedy pro hodnotu $x=0$

Na intervalu $J$:
$$
f(x) = x^2 -x +1
$$

Na intervalu $I$:
$$
f(x) = x^2 +3x +1
$$

Funkce f je v $x=0$ pokud:
$$
\lim_{ x \to 0^{-} } f(x)=\lim_{ x \to 0^{+} } =f(0)
$$

$$
f(0) = 1
$$
$$
\lim_{ x \to 0^{-} } = x^2+3x+1= 1
$$
$$
\lim_{ x \to 0^{+} } = x^2-x+1=1
$$

Podminka spojitosti je splnena.

Muzeme spocitat jednostrane derivace:

Na $J$
$$
f'(x) = 2x-1 
$$
$$
f'(0)=-1
$$

Na $I$:
$$
f'(x) = 2x+3
$$
$$
f'(0) = 3
$$

Derivace se nerovnaji, takze v tomto bode neexistuje derivace.


**b)** Najděte všechny body, v nichž tato funkce nabývá lokální či globální extrémy, a určete, o jaký typ extrému se jedná (zda jen lokální nebo i globální, zda minimum nebo maximum).



Na $J$:
$$
f''(x) = 2
$$
Na $I$:
$$
f''(x) = 2
$$

Stacionarni body ziskame z prvnich derivaci:
$$
x_{1}=-\frac{3}{2}; x_{2}=\frac{1}{2}
$$

A podezrely bod $x_{3}=0$.


$x_{1}$ se nachazi na intervalu $I$:

$$
f\left( -\frac{3}{2} \right)= \left( -\frac{3}{2} \right)^{2}-\frac{9}{2}+1 = \frac{9}{4}-\frac{7}{2}=-\frac{5}{4}
$$

Protože $f''(x) > 0$, jedná se o **lokální minimum**.



$x_{2}$ se nachazi na intervalu $J$.


$$ f\left( \frac{1}{2} \right)= \left( \frac{1}{2} \right)^{2} - \frac{1}{2}+1= \frac{3}{4} $$

Protože $f''(x) > 0$, jedná se o **lokální minimum**.


V bode $x=0$ ma $f$ hodnotu $1$. 


Budeme zkoumat jednostrane limity derivaci v nule:

$$
\lim_{ x \to 0^{-} } 2x+3= 3
$$
Tedy funkce z leva roste.

$$
\lim_{ x \to 0^{+} } 2x-1 = -1
$$
Tedy funkce zprava klesá. Tedy v bodě $x=0$ je lokalni maximum.

$f$ je na obouch intervalech parabola otevrena nahoru, to znamena, ze nejmensi lokalni minimum obou funkci je globalni minimum cele funkce. Tedy $x_{1}=-\frac{3}{2}$ je globalni minimum.




**c)** Najděte co největší otevřený interval tvaru $G = (-\infty, A)$, na němž je funkce $f$ konvexní nebo konkávní, a uveďte, zda je $f$ na $I$ konvexní, nebo zda je tam konkávní.



Jelikoz v bode $x=0$ je lokalni maximum, pro hodnoty vetsi nez $0$ je f konvexni a pred $f$ je konvexni. Jelikoz hledame interval od $-\infty$, hodnota $A$ bude maximalne $0$. 

$f$ je na intervalu $I$ parabola otevrena nahoru tedy na celem intervalu $I$ je funkce konvexni. ( Protože $f''(x) = 2 > 0$ na celém intervalu $I$.) To je nas hledany interval. $A = 0$.

---

## Příklad 2 (3 body)

Uvažujme funkci $f : \mathbb{R} \to \mathbb{R}$ definovanou takto:
$$
f(x) = 
\begin{cases}
0, & x \leq 0 \\
\exp(-1/x), & x > 0,
\end{cases}
$$
kde $\exp(x)$ označuje exponenciální funkci $e^x$.

**a)** Rozhodněte, zda je funkce $f$ spojitá v bodě $x = 0$ a zda má limitu v $+\infty$.

Prosetrime jednostrane limity v bode $x=0$.

$$
\lim_{ x \to 0^{-} } 0=0
$$
$$
\lim_{ x \to 0^{+} } e^{-1/x} = e^{-\infty} = 0
$$
Limity se rovnaji, takze funkce $f$ je spojita v bode $x=0$.

Limita v $+\infty$:
$$
\lim_{ x \to \infty } e^{-1/x}=e^{0}=1
$$
$f$ ma limitu v $+\infty$.

**b)** Rozhodněte, zda má funkce $f(x)$ derivaci v bodě $x = 0$, případně zda má v tomto bodě alespoň jednostranné derivace.

Jelikoz je funkce spojita v bode $x=0$, muzeme prosetrit jednostrane derivace:

$f_{1}$ je funkce $f$ na intervalu $x \in (-\infty;0>$ a $f_{2}$ na zbytku.

$$
f_{1}'(x)=0
$$

$$
f_{2}'(x) = (e^{-1/x})'= x^{-2} \cdot e^{-1/x} = \frac{e^{-1/x}}{x^{2}}
$$

$$
\lim_{ x \to 0^{+} } \frac{e^{-1/x}}{x^{2}} = \frac{0}{0}
$$
Jelikoz derivovat $e^{-1/x}$ nedava smysl protoze budeme stale dostavat 0 ve jmenovateli i citateli, udelame to odhadem. 

Pro $n \in \mathbb{N}$:
$$
e^{-1/x} < x^n
$$

Pak:
$$
\frac{e^{-1/x}}{x^{2} } < \frac{x^{n}}{x^{2}} = x^{n-2}
$$

Pro $n > 2$ pak plati:

$$
\lim_{ x \to 0^{+} } x^{n-2}=0 \implies \lim_{ x \to 0^{+} } \frac{e^{-1/x}}{x^{2} } = 0
$$
Podle vety o sevreni funkci (dvou policajtech idk ....).

Obe derivace se rovnaji takze v bode $x=0$ existuje derivace.

**c)** Najděte maximální intervaly, na nichž je funkce $f$ konvexní, a maximální intervaly, na nichž je konkávní.

Druha derivace $0$ je $0$.

Druha derivace $\frac{e^{-1/x}}{x^{2}}$:
$$
f_{2}''(x) = \frac{e^{-1/x}}{x^{2}} \cdot \frac{1}{x^2} + \left( -\frac{2}{x^{3}} \right) \cdot e^{-1/x}= \frac{e^{-1/x}}{x^{4}}-\frac{2e^{-1/x}}{x^{3}} =  \frac{e^{-1/x}}{x^{4}} \cdot (1-2x)
$$

$x^{4}$ je kladne pro $x>0$ a i $e^{-1/x}$ je kladne pro $x>0$. Tedy znamenko urcuje $1-2x$.

Pro $x> \frac{1}{2}$ je druha derivace zaporna (konkavni). A pro $x< \frac{1}{2}$ je derivace kladna (konvexni).

Tedy maximalni interval $f$ kde je konvexni je:
$$
\left( -\infty; \frac{1}{2} \right)
$$

A maximalni interval kde je konkavni je:
$$
\left( \frac{1}{2};+\infty \right)
$$