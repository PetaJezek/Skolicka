
# **Priklad 1**
Uvažujme funkci $f:R→R$ definovanou vzorcem$f(x)=∣x^2−1∣(x+1)$.

- a) Ve kterých bodech $\mathbb{R}$ má tato funkce vlastní derivaci?
- b) Najděte všechny body, v nichž tato funkce nabývá lokální či globální extrémy, a určete, o jaký typ extrému se jedná (zda jen lokální nebo i globální, zda minimum nebo maximum).
- c) Najděte co největší otevřený interval  $I$ obsahující nulu, na němž je tato funkce konvexní nebo konkávní, a uveďte, zda je $f$ na $I$ konvexní, nebo zda je tam konkávní.


Muzeme funkci prepsat jako:
$$
f(x)= \left| (x - 1)(x+1) \right|(x+1)
$$
Absolutni hodnota otaci znamenko pouze na intervalu $(-1;1)$.

Nejdrive vysetrime derivaci mimo tento interval:

$$
f(x) = (x^2-1)(x+1)= x^3 +x^2 -x -1 
$$


Derivace tohoto se rovna:

$$
f'(x)_{1}=3x^2 +2x -1
$$

Nyni na intervalu $(-1;1)$:
$$
f(x) = (-x^2+1)(x+1) = -x^3 -x^2 +x +1
$$

Derivace tohoto je:
$$
f'(x)_{2}= -3x^2-2x+1
$$
Checeme najit body bez vlastni derivace.

Ty muzou byt pouze na prechodu techto dvou funkci, protoze sami o sobe jsou spojite (trivialni).

Musime vysetrit hodnoty v bodech $\pm 1$.

Pro -1:
$$
3x^2+2x-1 = -3x^2 -2x +1
$$
$$
3 - 2 - 1 = -3 +2 + 1
$$
Derivace se tedy rovna a bode $-1$ existuje.

Pro +1:
$$
3+2-1=-3-2+1
$$
Tady se nerovnaji, takze v bode 1 neexistuje vlastni derivace.

Tedy odpoved na otazku je:
	f(x) ma vsude vlastni derivaci krome bodu $\{ 1 \}$.

**b)**

Extremy jsou v bodech kde se derivace rovnaji 0.



$$
f'(x)_{1}=3x^2 +2x -1
$$
$$
0 = 3x^2 +2x -1  
$$
$$
0 = (3x-1)(x+1)
$$
$x_{1}=\frac{1}{3}$ a $x_{2}=-1$.
$x_{1}$ ale nemuzeme brat v uvahu protoze je mimo interval na kterem pracujeme.

Pro hodnoty mensi nez minus jedna je derivace kladna.

Podivame se jak se funkce vyvije uvnitr intervalui $(-1,1)$

$$
f'(x)_{2}= -3x^2-2x+1
$$
$$
0 = -3x^2-2x+1
$$
$$
0=(x+1)(-3x+1)
$$
$$
x_{2}=\frac{1}{3}
$$
Pro hodnoty vetsi nez $-1$ ale mensi nez $\frac{1}{3}$ je tato derivace kladna. to znamena ze $-1$ neni extrem protoze derivace $f$ je kladna i pro hodnoty mensi nez $-1$.


Pro hodnoty mensi nez $\frac{1}{3}$ je derivace kladna a pro hodnoty vetsi nez $\frac{1}{3}$ a mensi nez 1 je derivace $f(x)_{2}$ zaporna. Tedy v bode $x=\frac{1}{3}$ ma funkce $f$ maximum. Jelikoz f=$f(x)_{1}$ je exponencialni funkce, ktera jde do nekonecna, toto maximum bude pouze lokalni.

**c)**
Jelikoz $I$ musi obsahovat nulu, nahledneme nejdrive na funkci $f(x)_{2}$, ktera je na intervalu $(-1,1)$.
Druha derivace teto funkce je:
$$
f'(x)_{2}= -3x^2-2x+1
$$
$$
f''(x)_{2} = -6x-2 = 2(-3x-1)
$$
Nulovy bod je $-\frac{1}{3}$.

Na intervalu $\left( -\frac{1}{3}, 1 \right)$ je druha derivace zaporna, a protoze v bode $x=1$ nema funkce $f$ vlastni derivaci, dal zkoumat nemusime. Na intervalu $(-1, -\frac{1}{3})$ je derivace kladna. Tedy nejvetsi interval ktery obsahuje nulu je
$$
\left( -\frac{1}{3}, 1 \right).
$$  
Jelikoz druha derivace na tomto intervalu je zaporna, funkce je na tomto intervalu **konkavni**.

---

# **Příklad 2 (3 body)**

Vhodnou metodou spočtěte integrály:

- **a)**  
  $$
  \int \arcsin x \, dx
  $$

Pomoci perpartes
- $u = \arcsin x \Rightarrow du = \frac{1}{\sqrt{1 - x^2}} dx$
    
- $dv = 1 \Rightarrow v = x$

$$
  \int \arcsin x \, dx = \arcsin x\cdot x - \int \frac{x}{\sqrt{ 1-x^2 }} \, dx 
$$

Pouzijeme substituci. $t = 1-x^2 \implies dt = -2x$ A vyresime zbyly integral

$$
\int \frac{x}{\sqrt{ t }} : (-2x) \, dx = -\frac{1}{2}  \int t^{-1/2} \, dt  
$$
$$
-\frac{1}{2} \cdot 2 \sqrt{ t } = -t = -\sqrt{ 1-x^2 }
$$
Dosadime zpatky:
$$
\arcsin x\cdot x - \int \frac{x}{\sqrt{ 1-x^2 }} \, dx = \arcsin x \cdot x + \sqrt{ 1-x^2 } + C
$$


- **b)**  
  $$
  \int \frac{e^x}{1 + e^{2x}} \, dx
  $$

$$
\int \frac{e^x}{1+(e^x)^2} \, dx 
$$
Pouzijeme substituci $e^x = t \implies dt = e^x$. 

$$
\int \frac{e^x}{1+(e^x)^2} \, dx = \int \frac{t}{1+t^2} : t \, dt = \int \frac{1}{1+t^2} \, dt= \arctan t = \arctan e^x + C
$$

- **c)**  
  $$
  \int (x^2 + 1) e^{2x} \, dx
$$
Pouzijeme metodu perpartes:
- $u =x^2+1 \implies du=2x$
- $dv=e^{2x}\implies v=\frac{e^{2x}}{2}$

$$
= \frac{(x^2+1)e^{2x}}{2} - \int e^{2x}x \, dx 
$$

Opet perpartes:
- $u = x \implies du = 1$
- $dv = e^{2x} \implies v=\frac{e^{2x}}{2}$

Dopocitame integral

$$
\int e^{2x}x \, dx = x\cdot \frac{e^{2x}}{2} - \int \frac{e^{2x}}{2} \, dx  =  x\cdot \frac{e^{2x}}{2} - \frac{e^{2x}}{4}
$$

Dosadime

$$
= \frac{(x^2+1)e^{2x}}{2} - \left( \frac{xe^{2x}}{2} - \frac{e^{2x}}{4} \right)  = x^2\cdot \frac{e^{2x}}{2} - x\cdot \frac{e^{2x}}{2} +  \frac{3}{4} e^{2x} + C
$$