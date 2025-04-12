
## Příklad 1: Výpočet limit

### a) $\lim_{x\to 1} \frac{x^m-1}{x^n-1}$

Pou6iju l'Hospitalovo pravidlo, protože při dosazení $x = 1$ dostáváme neurčitý výraz $\frac{0}{0}$.

Když $x \to 1$, pak $x^m - 1 \to 0$ a $x^n - 1 \to 0$.

Aplikuji l'Hospitalovo pravidlo:

- Derivace čitatele: $\frac{d}{dx}(x^m-1) = m\cdot x^{m-1}$
- Derivace jmenovatele: $\frac{d}{dx}(x^n-1) = n\cdot x^{n-1}$

$$\lim_{x\to 1} \frac{x^m-1}{x^n-1} = \lim_{x\to 1} \frac{m\cdot x^{m-1}}{n\cdot x^{n-1}} = \frac{m\cdot 1^{m-1}}{n\cdot 1^{n-1}} = \frac{m}{n}$$

$$\lim_{x\to 1} \frac{x^m-1}{x^n-1} = \frac{m}{n}$$


### b) $$\lim_{x\to 0} x\cdot \left\lfloor\frac{1}{x}\right\rfloor$$
Nemam tušení, co udělat s tim zaokrouhlenim.


## Příklad 2: Spojitost funkcí

### a) $f(x) = \begin{cases} \frac{x^2-4}{x-2} & x \neq 2\\  \quad4 & x = 2 \end{cases}$

Funkce je definována na celém $\mathbb{R}$. Pro $x \neq 2$ lze výraz upravit: $$\frac{x^2-4}{x-2} = \frac{(x-2)(x+2)}{x-2} = x+2$$

Tedy $$f(x) = \begin{cases} x+2  & x \neq 2  \\4 & x = 2 \end{cases}$$

Abych určil spojitost v bodě $x = 2$, spočítám limitu: $$\lim_{x\to 2} f(x) = \lim_{x\to 2} (x+2) = 2+2 = 4$$

$\lim_{x\to 2} f(x) = f(2) = 4$

Tedy funkce $f$ je spojitá na celém definičním oboru $\mathbb{R}$.

Pro nalezení $\delta$ pro dané $\varepsilon$: $$|f(x) - f(a)| = |x+2 - (a+2)| = |x-a|$$

Takže můžeme vybrat $\delta = \varepsilon$ a podmínka $|f(x) - f(a)| < \varepsilon$ pro $|x-a| < \delta$ bude splněna.

### b) $$f(x) = \begin{cases} x\cdot\sin\frac{1}{x} & x \neq 0 \\ 0 & x = 0 \end{cases}$$
 Pro zkoumání spojitosti v bodě $x = 0$ potřebuji zjistit: $$\lim_{x\to 0} f(x) = \lim_{x\to 0} x\cdot\sin\frac{1}{x}$$

$|\sin\frac{1}{x}| \leq 1$ pro všechna $x$, takže $|x\cdot\sin\frac{1}{x}| \leq |x|$ a zárověn $x\cdot\sin\frac{1}{x} \geq -x$. Podle věty o dvou policajtech, když $x \to 0$, také $-x \to 0$, tak $x\cdot\sin\frac{1}{x} \to 0$.

Tedy $\lim_{x\to 0} f(x) = 0 = f(0)$, což znamená, že funkce je spojitá v bodě $x = 0$. Pro všechna $x \neq 0$ je funkce spojitá jako složení spojitých funkcí.

Tedy funkce $f$ je spojitá na celém $\mathbb{R}$.

### c) $$f(x) = \begin{cases} 2x & x \geq 0 \\ -3x & x < 0 \end{cases}$$


Pro nalezení $\delta$ pro dané $\varepsilon$:

Pro $a > 0$ a $x > 0$: $|f(x) - f(a)| = |2x - 2a| = 2|x-a|$, takže $\delta = \frac{\varepsilon}{2}$
Pro $a < 0$ a $x < 0$: $|f(x) - f(a)| = |-3x - (-3a)| = 3|x-a|$, takže $\delta = \frac{\varepsilon}{3}$
Pro $a = 0$: rozlišíme případy pro $x > 0$ a $x < 0$
    - $x > 0$: $|f(x) - f(0)| = |2x - 0| = 2|x|$, takže $\delta = \frac{\varepsilon}{2}$
    - $x < 0$: $|f(x) - f(0)| = |-3x - 0| = 3|x|$, takže $\delta = \frac{\varepsilon}{3}$

Pro $a = 0$ tedy volíme $\delta = \frac{\varepsilon}{3}$. Jelikoz jsme delta nalezli, funkce je spojita.