# Příklad 1 (2 body)

Pro přirozené číslo $n \in \mathbb{N}$ definujme funkci $f_n(x)$ následovně:

$f_n(x) = \begin{cases} 0 & x = 0 \ \frac{\sin(x^n)}{x} & x \neq 0 \end{cases}$

Pro jaká přirozená čísla $n$ je funkce $f_n$ spojitá v bodě $x = 0$?

## Řešení:

Funkce $f_n$ je spojitá v bodě $x = 0$, pokud $\lim_{x \to 0} f_n(x) = f_n(0) = 0$.

Potřebujeme vyšetřit limitu: $\lim_{x \to 0} \frac{\sin(x^n)}{x}$

Rozlišíme případy podle hodnoty $n$:

**Případ $n = 1$:** $\lim_{x \to 0} \frac{\sin(x)}{x} = 1 \neq 0$ Funkce není spojitá.

**Případ $n \geq 2$:** Použijeme substituci $t = x^n$, pak $x = t^{1/n}$ a když $x \to 0$, tak $t \to 0$.

$\lim_{x \to 0} \frac{\sin(x^n)}{x} = \lim_{t \to 0} \frac{\sin(t)}{t^{1/n}}$

Pro $n \geq 2$ je $\frac{1}{n} \leq \frac{1}{2} < 1$, takže $t^{1/n} \to 0$ rychleji než $\sin(t)$.

Protože $|\sin(t)| \leq |t|$ pro malá $t$, máme: $\left|\frac{\sin(t)}{t^{1/n}}\right| \leq \frac{|t|}{|t|^{1/n}} = |t|^{1-1/n} = |t|^{(n-1)/n}$

Pro $n \geq 2$ je $(n-1)/n > 0$, takže $|t|^{(n-1)/n} \to 0$ když $t \to 0$.

Tedy $\lim_{x \to 0} \frac{\sin(x^n)}{x} = 0$.

**Odpověď:** Funkce $f_n$ je spojitá v bodě $x = 0$ pro všechna $n \geq 2$.

# Příklad 2 (2 body)

Definujme funkci $f : \mathbb{R} \to \mathbb{R}$ následovně:

$f(x) = \begin{cases} 0 & x \text{ racionální} \ x^2 & x \text{ iracionální} \end{cases}$

Rozhodněte, zda má funkce $f$ derivaci v nule.

## Řešení:

Pro existenci derivace v bodě $x = 0$ musí existovat limita: $f'(0) = \lim_{h \to 0} \frac{f(h) - f(0)}{h}$

Nejprve určíme $f(0)$. Protože $0$ je racionální číslo, máme $f(0) = 0$.

Nyní vyšetříme limitu: $\lim_{h \to 0} \frac{f(h) - 0}{h} = \lim_{h \to 0} \frac{f(h)}{h}$

Rozlišíme dva případy podle povahy čísla $h$:

**Pokud $h$ je racionální a $h \neq 0$:** $\frac{f(h)}{h} = \frac{0}{h} = 0$

**Pokud $h$ je iracionální:** $\frac{f(h)}{h} = \frac{h^2}{h} = h$

Při přiblížení k nule:

- Podél racionálních čísel: $\lim_{h \to 0, h \in \mathbb{Q}} \frac{f(h)}{h} = 0$
- Podél iracionálních čísel: $\lim_{h \to 0, h \notin \mathbb{Q}} \frac{f(h)}{h} = \lim_{h \to 0} h = 0$

Protože obě jednostranné limity jsou stejné a rovny $0$, existuje: $f'(0) = \lim_{h \to 0} \frac{f(h)}{h} = 0$

**Odpověď:** Funkce $f$ má derivaci v nule a $f'(0) = 0$.