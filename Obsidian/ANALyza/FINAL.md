**Pojmy definované pro podmnožiny R: horní/dolní mez, (shora/zdola) omezená množina, supremum, infimum, maximum, minimum**

Horni mez mnoziny $A$ je libovolne $x \in \mathbb{R}$ takove, ze pro $\forall y\in A: y \leq x$
Dolni mez je to stejne akorat obracena nerovnost

# **Supremum** je $s \in \mathbb{R}$ mnoziny $A$ je nejmensi horni mez mnoziny $A$. Pokud ma mnozina maximum, je to i jeji supremum.

# **Infimum** je nejvetsi horni mez.


# **Metricky prostor** je dvojice $(M,d)$ kde M je libovolna mnozina a $d: M\times M \to \mathbb{R}$ je funkce splnujici nasledujici podminky:

$$
\forall x,y \in M: d(x,y)\geq 0,\quad d(x,y) = 0 \text{ when } x=y
$$
$$
\forall x,y,z \in M :d(x,z) \leq d(x,y)+d(y,z)
$$
$$
\forall x,y \in M :d(x,y) = d(y,x)
$$

# **Posloupnosti reálných čísel, jejich omezenost, monotonie, limita posloupnosti, vlastní a nevlastní limita, konvergentní posloupnost**


# **Posloupnost** 
Necht $M$ je mnozina. Posloupnost s hodnotami v $M$ je zobrazeni z $\mathbb{N}$ do $M$. Kazde prirozene cislo $n$ je tedy zobrazeno na nejaky prvek $a_{n}$ mnoziny $M$. Tomuto prvku rikame n-ty prvek posloupnosti. 

# **Omezenost posloupnosti** 
- Shora omezena pokud existuje $M\in \mathbb{R}$ takove ze, $\forall n:a_{n} \leq M$
- Zdola omezena  pokud existuje $M\in \mathbb{R}$ takove ze, $\forall n:a_{n} \geq M$
- Omezena pokud plati oboji

# **VLASTNI LIMITA POSLOUPNOSTI** 
Necht $a_{n}$ je posloupnost realnych cisel. Rekneme, ze $A\in \mathbb{R}$ je vlastni limita posloupnosti, pokud pro kazde realne cislo $\epsilon >0$ existuje $n_{0} \in \mathbb{N}$ takove, ze pri kazde prirozene cislo $n\geq n_{0}$ je $\left| a_{n}-A \right| <\epsilon$ 


Tohle neumim spocitat....

# **Konvergentni posloupnost**

Pokud posloupnost ma vlastni limitu, rikame, ze konverguje, pripadne, ze je konvergentni a piseme $\lim_{ n \to \infty }a_{n}=A$

# **Okolí bodu, včetně okolí nevlastních bodů ±∞, prstencové okolí, jednostranné prstencové okolí** 

*Okoli bodu* pro $x \in \mathbb{R}; \epsilon \in (0, +\infty)$, definujeme mnozinu $U(x, \epsilon)= (x-\epsilon,x+\epsilon$ kterou nazyvame okoli bodu $x$ o polomeru $\epsilon$

Prstencove okoli je okoli bez bodu $x$.


# **Podposloupnost**

Posloupnost $b_{n}$ je podposloupnost posloupnosti $a_{n}$ pokud existuje rostouci funkce $f: \mathbb{N}\to \mathbb{N}$ takova, ze
$$
\forall n \in \mathbb{N}: b_{n}=a_{f(n)}
$$

# **Hromadny bod**

Necht $a_{n}$. Rozsireme realne cislo $H\in \mathbb{R}*$je jejim hromadnym bodem, pokud $H$ je limitou nejaka podposloupnosti $a_{n}$.

# **Limes superior a Limes inferior** 

Nejvetsi prvek mnoziny vsech hromadnych bodu se nazyva limes superior a nejmensi se nazyva limes inferior.

# **Nekonecna rada** 

Je to vyraz:
$$
\sum_{n=1}^{\infty} a_{n}=a_{1}+a_{2}+a_{3}+\dots
$$
kde, $a_{n}: n\geq_{1}$ je posloupnost realnych cisel


# **Castecny soucet rady** 

Presneji n-ty soucet $s_{n}$, je soucet jeji prvnich n clenu.

# **Konvergentni rada** 
Pokud existuje vlastni limita posloupnosti castecnych souctu dane rady, mluvime o konvergentnti rade a limita $\lim_{ n \to \infty }s_{n}$ je jejim souctem.



# **Limita funkce** 

Rekneme ze $f$ ma v bode $A \in \mathbb{R}^{*}$ limitu $L\in \mathbb{R}$ kdyz 
$$
\forall\epsilon >0, \exists\delta >0, \forall x \in P(A,\delta): f(x) \in U(L,\epsilon) 
$$
Neboli
$$
\forall \epsilon >0,\exists\delta>0: f(P(A,\delta)) \subseteq U(L,\epsilon)
$$


# **Spojitost** 
Rekneme, ze funkce $f$ je v bode $A\in \mathbb{R}$ spojita, pokud $\lim_{ x \to A }f(x)=f(A)$


# **Interval** 

Interval oznacime jakoukoliv mnozinu $I \subseteq \mathbb{R}$ takovou, ze pro kazda tri realna cisla $x<y<z$ plati, ze $x$ a $z$ nalezi $I$, tak i $y\in I$.

Netrivialni interval pokud obsahuje aspon dva body. (a tedy nekonecne bodu)

Vnitrni bod intervalu $I$ je bod, ktery lezi v $I$ i s nejakym svym okolim. 

# **Spojitost funkce na intervalu** 
Necht $M\subseteq \mathbb{R}$ je mnozina, necht $f:M\to \mathbb{R}$ je funkce a necht $I\subseteq M$ je netrivialni interval. Rekneme, ze $f$ je spojita na intervalu $I$, jeli spojita v kazdem vnitrnim bodu $I$ a v kazdem pripadnem krajnim bodu $I$ je odpovidajicim zpusobem jednostranne spojita, tj. pokud $I$ ma nejvetsi prvek, tak je v nem $f$ spojita zleva, a pokud $f$ ma nejmensi prvek, tak je v nem $f$spojita zprava.



# **Extremy funkci: Lokalni a Globalni** 
Necht $M\subseteq \mathbb{R}$ a $f:M\to \mathbb{R}$. Rekneme, ze funkce $f$  v bode $A \in M$ nabyva sveho:
- MAXIMA, kdyz $\forall x \in M: f(x) \leq f(A)$
- ostreho maxima, kdyz $\forall x \in M \setminus \{A\}: f(x) <f(A)$
- LOKALNIHO maxima, kdyz $\exists\delta>0, \forall x \in M \cap U(A,\delta): f(x)\leq f(A)$
- ostreho lokalniho maxima kdyz $\exists\delta>0, \forall x \in M \cap U(A,\delta): f(x) < f(A)$

Obdobne se definuje minima



# **Kompaktni interval** 

Kazdy interval tvaru $[A,B]: A,B\in \mathbb{R}$.

# **Derivace funkce**

Derivace funkce $f$ v bode $A$ je limita:
$$
f'(A):= \lim_{ h \to 0 } \frac{f(A+h)-f(A)}{h}
$$
Neboli s predznacenim $x=A+h$
$$
f'(A):= \lim_{ x \to A } \frac{f(x)-f(A)}{x-A}
$$

Funkce je diferencovatelna v $A$ pokud ma $f$ v bode $A$ vlasnti derivaci.


# **Derivace vyssich radu** 

Pokud ma funkce f na nejakem okoli  $U(A,\epsilon)$ vlastni derivaci $f'$ a pokud existuje limita:
$$
f''(A):= \lim_{ x \to A } \frac{f'(x)-f'(A)}{x-A}
$$
Nazveme ji druhou derivaci.

# **KONVEXITA/KONKAVNOST**
Funkce $f:I\to \mathbb{R}$ je na intervalu $I$ KONVEXNI, pokud:
$$
\forall A,x,B \in I: A<x<B: f(x) \leq f(A)+ (x-A)\cdot\left( \frac{f(B)-f(A)}{B-A} \right)
$$

Prava strana je rovnice primky z bodu. 



# **Tayloruv polynom a Taylorova rada**
Necht $A \in \mathbb{R}$, necht $n \in N_{0}$ a necht $f$ je funkce definovana na okoli A, ktera je v $A$ spojita a ma v $A$ vlastni n-tou derivaci $f_{n}(A)\in \mathbb{R}$. Taylorovym polynomem radu $n$ funkce $f$ v bode $A$ rozumime polynom:  
$$
T^{f,A}_{n}(x)= \sum_{i=0}^{n} \frac{f^{(i)}(A)}{i!}(x-A)^{i}
$$

Ma-li funkce $f$ v bode $A\in \mathbb{R}$ derivace vsech radu, rozumime pro $x \in \mathbb{R}$ jeji Taylorouvou radou se stredem v $A$ radu Tayloruv polynom ale misto $n$ to jde do $\infty$.


# **Primitivni funkce** 
Necht $f:I\to \mathbb{R}$ je funkce definovana na tomto intervalu. Pak funkce $F:I\to \mathbb{R}$ je na intervalu $I$ primitvni funkci pro funkci $f$ , pokud v kazdem bode $x \in I$ plati, ze $F$ ma derivaci v $x$ rovnou $f(x)$.



# **Newtonuv integral** 
Mejme dano $A,B \in \mathbb{R}$ kde $A<B$. Funkce $f:(A,B)\to \mathbb{R}$ ma na intervalu $(A,B)$ Newtonuv integral, kdyz ma na $(A,B)$ primitivni funkci F a ta ma vlastni jednostranne limity $F(A^{+})= \lim_{ x \to A^{+} }F(x)$ a $F(B^{-})=\lim_{ x \to B^{-} }F(x)$ 

Pak integral definujeme jako:

$$
(N)\int_{A}^{B} f(x) \, dx := [F]^{B}_{A}=F(B-)-F(A+)=\lim_{ x \to B^{-} } F(x)-\lim_{ x \to A^{+} } F(x)
$$

# **Deleni intervalu**

Konecna $(k+1)$-tice bodu $D=(A_{0},A_{1},A_{2},\dots,A_{k})$ z intervalu $[A,B]$ je jeho delenim, pokud $A= A_{0}<A_{1}<\dots<A_{k}=B$. Tyto body deli interval $[A,B]$ na intervaly $I_{i}=[A_{i},A_{i+1}]$.


# **Dolni a Horni Reimannova suma**
Pro funkci $f:[A,B]\to \mathbb{R}$ a deleni $D=(A_{0},A_{1},\dots,A_{k})$ intevalu $[A,B]$ definujeme dolni Reimannovu sumu jako 
$$
s(f,D)=\sum_{i=0}^{k-1} \left| I_{i} \right|m_{i}
$$

A horni Reimanovu sumu jako:
$$
S(f,D)=\sum_{i=0}^{k-1} \left| I_{i} \right|M_{i}
$$

Kde $m_{i}= inf\{ f(x); x \in I_{i} \}$ a $M_{i}=sup \{ f(x); x \in I_{i} \}$

# **Horni a Dolni Reimannuv integral** 
Necht $f$ je funkce na intervalu $[A,B]$.   Dolni Reimannuv integral definujeme jako:
$$
(R) \int_{A}^{B} f(x)\, dx=sup\{ s(f,D) \} 
$$

A Horni integral je:
$$
(R) \int_{B}^{A}  f(x)\, dx =  inf \{ S(f,D) \}
$$


