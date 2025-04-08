Dokažte z definice že: 
$$
\lim_{ x \to 5 } 2+2x=12 
$$

Definice:
$$
\lim_{ x \to A } = L \leftrightarrow  \forall \epsilon > 0 \quad \exists \delta > 0: \forall x \in P(A,\delta) \cap M:f(x) \in \mathcal{U}(L,\epsilon)
$$

Tedy  pro kazde $\epsilon$ hledame $\delta$ takove aby: 
$$
\forall x: \left| x-5 \right| < \delta \implies \left| 2x+2-12 \right| < \epsilon
$$
Upravim pravou stranu:

$$
\left| 2x+2-12 \right| = 2\left| x-5 \right|
$$

Tedy aby platil nas pozadovany vztah, staci:
$$
\delta = \frac{\epsilon}{2}
$$
Tedy:
$$
\left| x-5 \right| < \delta = \frac{\epsilon}{2}
$$
$$
2\left| x-5 \right| < 2\cdot \frac{\epsilon}{2}= \epsilon
$$
Tím je náš důkaz dokončen.


---
a) 
$$
\lim_{ x \to 1 } \frac{x^3+ x^2-x-1}{x^3 +2x^2-x-2}
$$

Můžeme upravit:

$$
\lim_{ x \to 1 } \frac{x(x^2-1) + x^2 - 1}{x^2(x+2)-1(x+2)} 
$$

$$
\lim_{ x \to 1 } \frac{(x+1)(x^2-1)}{(x^2-1)(x+2)} = \lim_{ x \to 1 } \frac{x+1}{x+2}= \frac{2}{3}
$$

b)
$$
\lim_{ x \to -1 } \frac{x^3-x^2-x+1}{x^3+x^2-x-1} = \lim_{ x \to -1 } \frac{x(x^2-1)-1(x^2-1)}{x(x^2-1)+1(x^2-1)} = \lim_{ x \to -1 } \frac{(x-1)(x^2-1)}{(x+1)(x^2-1)} =
$$

$$
= \lim_{ x \to -1 } \frac{x-1}{x+1}  
$$

Protoze mame 0 v jmenovateli, musime zkontrolovat limity zprava a zleva.

Zprava:
$$
\lim_{ x \to -1^+ } \frac{x-1}{x+1} = -\infty
$$
protoze citatel je zaporne cislo a jmenovatel je kladny a blizi se 0.

Zleva:
$$
\lim_{ x \to -1^+ } \frac{x-1}{x+1} = \infty
$$
protoze citatel je zaporne cislo a jmenovatel je take zaporny a blizi se k nule.
Tedy limita
$$
\lim_{ x \to -1 } \frac{x^3-x^2-x+1}{x^3+x^2-x-1}
$$
Neexistuje, protoze funkce v tomto bode neni spojita, protoze jednosmerne limity se nerovnaji v -1.

c)

$$
\lim_{ x \to -1 } \frac{x^3+x^2-x-1}{x^3+2x^2-x-2} = \lim_{ x \to -1 } \frac{(x+1)(x^2-1)}{(x+2)(x^2-1)}=\lim_{ x \to -1 } \frac{x+1}{x+2} = 0  
$$

d)
$$
\lim_{ x \to 0 } \frac{\sqrt[3]{1+x  }-1}{x} 
$$

Substituce 
$$
y = \sqrt[3]{1+x  }; y^3 = 1+x; x = y^3-1
$$

$$
\lim_{ x \to 0 } \frac{y-1}{y^3-1} = \lim_{ x \to 0 } \frac{y-1}{(y-1)(y^2+y+1)} = \lim_{ x \to 0 } \frac{1}{y^2+y+1} 
$$

Pokud $x\to 0\text{ Tak potom : } y \to 1$, protoze $\sqrt[3]{1+0  }=1$. Dosadime zpet:

$$
\lim_{ x \to 0 } \frac{1}{y^2+y+1} = \lim_{ x \to 0 } \frac{1}{1+1+1} = \frac{1}{3} 
$$

e)

$$
\lim_{ \pi \to \frac{\pi}{6} } \frac{2\sin^2x+\sin (x)-1}{2\sin^2(x)-3\sin(x)+1}
$$

Substituce:
$$
y = \sin x; x = \sin^{-1}y
$$

Dosadime:

$$
\lim_{ \pi \to \frac{\pi}{6} } \frac{2y^2+y-1}{2y^2-3y+1} = \lim_{ \pi \to \frac{\pi}{6} } \frac{(2y-1)(y+1)}{(2y-1)(y-1)} =\lim_{ \pi \to \frac{\pi}{6} } \frac{y+1}{y-1}   
$$

Pokud $x\to \frac{\pi}{6}\text{ Tak potom : } y\to \frac{1}{2}$, protoze $\sin \frac{\pi}{6}=\frac{1}{2}$. Dosadime zpet:

$$
\lim_{ x \to \frac{\pi}{6} } \frac{\frac{1}{2}+1}{\frac{1}{2}-1}= \lim_{ x \to \frac{\pi}{6} } -\frac{\frac{3}{2}}{\frac{1}{2}} = -3 
$$

