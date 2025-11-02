# Příklad 1 (6 bodů)

**Spočtěte integrály:**

## a) $$\int_1^3 \frac{18x^4-2}{3x-1} dx$$

Nejprve provedeme dělení polynomu:

$$\frac{18x^4-2}{3x-1} = 6x^3 + 2x^2 + \frac{2x}{3} + \frac{2}{9} - \frac{16}{27} \cdot \frac{1}{3x-1}$$

Integrujeme po částech:

$$\int_1^3 \frac{18x^4-2}{3x-1} dx = \left[\frac{3x^4}{2} + \frac{2x^3}{3} + \frac{x^2}{3} + \frac{2x}{9} - \frac{16}{27}\ln|3x-1|\right]_1^3$$

Dosadíme meze:

- Pro $x=3$: $\frac{243}{2} + 18 + 3 + \frac{2}{3} - \frac{16}{27}\ln(8)$
- Pro $x=1$: $\frac{3}{2} + \frac{2}{3} + \frac{1}{3} + \frac{2}{9} - \frac{16}{27}\ln(2)$

**Výsledek:** $141 - \frac{1}{18} - \frac{32}{27}\ln(2)$

---

## b) $$\int_1^2 \frac{e^{1/x}}{x^2} dx$$

Použijeme substituci: $u = \frac{1}{x}$, $du = -\frac{1}{x^2}dx$

Nové meze: $x=1 \Rightarrow u=1$, $x=2 \Rightarrow u=\frac{1}{2}$

$$\int_1^2 \frac{e^{1/x}}{x^2} dx = -\int_1^{1/2} e^u du = \int_{1/2}^1 e^u du = [e^u]_{1/2}^1$$

**Výsledek:** $e - \sqrt{e}$

---

## c) $$\int_{-1}^0 2x\sqrt{x^2+1} dx$$

Použijeme substituci: $u = x^2 + 1$, $du = 2x dx$

Nové meze: $x=-1 \Rightarrow u=2$, $x=0 \Rightarrow u=1$

$$\int_{-1}^0 2x\sqrt{x^2+1} dx = \int_2^1 \sqrt{u} du = \left[\frac{2u^{3/2}}{3}\right]_2^1$$

$$= \frac{2}{3}(1 - 2\sqrt{2})$$

**Výsledek:** $\frac{2}{3}(1 - 2\sqrt{2})$

---

## d) $$\int_e^{e^2} \frac{\ln^4 x}{x} dx$$

Použijeme substituci: $u = \ln x$, $du = \frac{1}{x}dx$

Nové meze: $x=e \Rightarrow u=1$, $x=e^2 \Rightarrow u=2$

$$\int_e^{e^2} \frac{\ln^4 x}{x} dx = \int_1^2 u^4 du = \left[\frac{u^5}{5}\right]_1^2 = \frac{32}{5} - \frac{1}{5}$$

**Výsledek:** $\frac{31}{5}$

---

## e) $$\int_0^{\pi/2} \sin^2 x dx$$

Použijeme trigonometrickou identitu: $\sin^2 x = \frac{1 - \cos(2x)}{2}$

$$\int_0^{\pi/2} \sin^2 x dx = \int_0^{\pi/2} \frac{1 - \cos(2x)}{2} dx$$

$$= \frac{1}{2}\left[x - \frac{\sin(2x)}{2}\right]_0^{\pi/2} = \frac{1}{2}\left[\frac{\pi}{2} - 0 - 0 + 0\right]$$

**Výsledek:** $\frac{\pi}{4}$

---

## f) $$\int_0^{\pi/2} \sin^3 x dx$$

Rozložíme: $\sin^3 x = \sin x(1 - \cos^2 x) = \sin x - \sin x \cos^2 x$

$$\int_0^{\pi/2} \sin^3 x dx = \int_0^{\pi/2} \sin x dx - \int_0^{\pi/2} \sin x \cos^2 x dx$$

První integrál: $\int_0^{\pi/2} \sin x dx = [-\cos x]_0^{\pi/2} = 0 - (-1) = 1$

Pro druhý integrál použijeme substituci $u = \cos x$, $du = -\sin x dx$: $$\int_0^{\pi/2} \sin x \cos^2 x dx = -\int_1^0 u^2 du = \int_0^1 u^2 du = \left[\frac{u^3}{3}\right]_0^1 = \frac{1}{3}$$

**Výsledek:** $1 - \frac{1}{3} = \frac{2}{3}$

---

## Shrnutí výsledků:

a) $141 - \frac{1}{18} - \frac{32}{27}\ln(2)$

b) $e - \sqrt{e}$

c) $\frac{2}{3}(1 - 2\sqrt{2})$

d) $\frac{31}{5}$

e) $\frac{\pi}{4}$

f) $\frac{2}{3}$