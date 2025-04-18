# Příklad 1 (2 body)

Spočtěte limity:
a)
$$
\lim_{x \to 1} \frac{x^2 + 2x - 3}{x^2 - 1}
$$
$$
= \lim_{x \to 1} \frac{(x+3)(x-1)}{(x-1)(x+1)}
$$
$$
= \lim_{x \to 1} \frac{x+3}{x+1}
$$
$$
= \frac{4}{2}= 2
$$
b)

$$

\lim_{x \to \frac{\pi}{2}} \frac{\sqrt{\tan(x)}}{2\sin^2(x) - 1}
$$
$$
= \frac{\sqrt{\tan\left(\frac{\pi}{2}\right)}}{2\sin^2\left(\frac{\pi}{2}\right) - 1}
$$
$$
= \frac{\sqrt{\infty}}{2(1)^2 - 1}
$$
$$
= \frac{\infty}{1}
= \infty
$$
Nevim jestli jsem zde mel pouzit lhopitala. Protoze bych si tipnul ze aproximace $\tan\frac{\pi}{2}=\infty$ neni uplne spravne.
Kdyztak rad predelam.



**Vyšetřete spojitost funkcí $f(x)$ v daných bodech pomocí limit.**

### a)

$$
f(x) = 
\begin{cases}
\frac{1}{x^2} & x \ne 0 \\
0 & x = 0
\end{cases}
$$

$$
\lim_{x \to 0} f(x) = \lim_{x \to 0} \frac{1}{x^2} = \infty \ne f(0) = 0
$$

Funkce **není spojitá** v bodě $x_0 = 0$.

b)

$$
f(x) = 
\begin{cases}
\frac{1}{1+e^{ \frac{1}{x-1}}} & x \ne 1 \\
1 & x = 1
\end{cases}
$$

Zkoumame z obou stran

$$
\lim_{x \to 1^-} \frac{1}{1 + e^{\frac{1}{x - 1}}}
= \frac{1}{1 + e^{-\infty}} = \frac{1}{1 + 0} = 1
$$

$$
\lim_{x \to 1^+} \frac{1}{1 + e^{\frac{1}{x - 1}}}
= \frac{1}{1 + e^{+\infty}} = \frac{1}{1 + \infty} = 0
$$

Tedy funkce neni spojita v bode $x_{0}=1$, ale ma jednostranou limitu zleva.

### c)

$$
f(x) = 
\begin{cases}
\frac{1 + x}{1 +x^3} & x \neq-1 \\
\frac{1}{3} & x = -1
\end{cases}
$$

Spočítáme limitu v bodě $x_0 = -1$:

$$
\lim_{x \to -1} \frac{1 + x}{1 + x^3}
$$

Derivujeme čitatel a jmenovatel:
čitatel: $(1 + x)' = 1$
jmenovatel: $(1 + x^3)' = 3x^2$

Použijeme l'Hospitalovo pravidlo:

$$
\lim_{x \to -1} \frac{1 + x}{1 + x^3}
= \lim_{x \to -1} \frac{1}{3x^2}
= \frac{1}{3(-1)^2}
= \frac{1}{3}
$$

Tedy funkce je spojita v bode $x_{0}=-1$, protoze $\frac{1}{3}=\frac{1}{3}=\lim_{ n \to \infty }\frac{1 + x}{1 +x^3} = \lim_{ n \to \infty} \frac{1}{3}$.


### d)

$$
f(x) = 
\begin{cases}
e^{x}+ \frac{1}{x} & x \neq 0 \\
0 & x = 0
\end{cases}
$$


Spočítáme limitu:

$$
\lim_{x \to 0} f(x) = \lim_{x \to 0} \left(e^x + \frac{1}{x}\right)
$$


Z toho vypliva:

$$

 \lim_{x \to 0^-} 1+\frac{1}{x} = -\infty  
 $$
 $$
 \lim_{x \to 0^+} 1+ \frac{1}{x} = +\infty
$$

Jelikoz se neshoduji ani s limitou v bode, neexistuje jak jednostrana tak i oboustrana limita.

Tudiz tato funkce neni spojita.