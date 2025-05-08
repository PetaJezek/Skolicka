Urcete derivace a definicni obory nasledujicich funkci.
a)
$$
f(x)= \log_{2}(x+\sqrt{ 1+x^2 })
$$

pokud $f(x) =g(h(x))$, kde $g(x) = \log_{2}x$ a $h(x) = x + \sqrt{ 1+x^2 }$, pak muzeme pouzit retezove pravidlo:
$$
h'(x) = (x+(1+x^2)^{1/2})'= 1 + ((1+x^2)^{1/2})' = 1 + \frac{1}{2\sqrt{ 1+x^2 }} \cdot 2x
$$

$$
= 1 + \frac{x}{\sqrt{ 1+x^2 }}
$$

Pokud dosadime zpatky:

$$
f'(x) = g'(h(x)) \cdot h'(x) = \frac{1}{(x+ \sqrt{ 1+x^2 })\cdot\ln 2} \cdot \left(1 + \frac{x}{\sqrt{ 1+x^2 }}\right)
$$
$$
f'(x) = g'(h(x)) \cdot h'(x) = \frac{1}{(x+ \sqrt{ 1+x^2 })\cdot\ln 2} \cdot \left(\frac{\sqrt{ 1+x^2 }+x}{\sqrt{ 1+x^2 }}\right)
=\frac{ \sqrt{ 1+x^2 }+x}{(x+\sqrt{ 1+x^2 })\ln 2 \cdot \sqrt{ 1+x^2 }} 
$$
$$
= \frac{1}{\sqrt{ 1+x^2 }\ln 2}
$$

Definicni obor $f(x)$ je cely obor relanych cisel, protoze $\left| x \right|< \sqrt{ 1+x^2 }$.

---

b)

$$
f(x) =\sqrt{ \frac{1-x^2}{1+x^2} }
$$

$$
= \left( \frac{1-x^2}{1+x^2} \right)^{1/2} 
$$

pouzijeme retezove pravidlo a pravidlo pro derivaci podilu.
$f(x)= g(h(x))$ kde $g(x) = x^{1/2}$ a $h(x)= \frac{1-x^2}{1+x^2}$.

$$
f'(x) = g'(h(x)) \cdot h'(x)
$$

$$
h'(x) = \frac{-2x\cdot(1+x^2)-(1 - x^2)\cdot 2x}{(1+x^2)^2} = \frac{-2x -2x^3-2x+2x^3}{x^4+2x^2+1} 
$$
$$
= \frac{-4x}{(x+1)^2}
$$

$$
g'(h(x))= \frac{1}{2} \cdot \left( \frac{1-x^2}{1+x^2}  \right)^{-1/2} = \frac{1}{2} \cdot \left( \frac{1+x^2}{1 -x^2} \right)^{1/2} = \frac{1}{2} \cdot \sqrt{ \left( \frac{1+x^2}{1 -x^2} \right)  }
$$

Pokud dosadime casti zpet:

$$
f'(x)=  \frac{1}{2} \cdot \sqrt{ \left( \frac{1+x^2}{1 -x^2} \right)  } \cdot\frac{-4x}{(x+1)^2} = \frac{-2x \cdot \sqrt{ 1+x^2 }}{(x+1)^2\cdot \sqrt{ 1-x^2 }}
$$

D(f) = $x \in [-1,1]$ kuvli citateli.

---
c)

$$
f(x)=x^2\cdot 2^x
$$
Pomoci pravidla pro soucin:
$$
f'(x)= 2x \cdot 2^x + x^2 2^x \ln(2) = 2^x(2x + x^2 \ln(2))
$$
Definicni obor je cely obor realnych cisel.

---
d)

$$
y = x^{1/x}
$$
$$
\ln(y) = \frac{1}{x}\cdot \ln(x)
$$

Derivujeme obe strany:
$$
\frac{1}{y} = \frac{1 - \ln(x)}{x^2}
$$

Vynasobim obe strany y:

$$
f'(x) = \frac{x^{1/x} - x^{1/x} \ln(x)}{x^2}
$$

Definicni obor f je $\mathbb{R}^+$. protoze  $n^{1/x}$ je definovano pro $x >0$.

---
e)
$$
f(x) = x^{x^x} = y
$$

$$
\ln(y) = x^x\ln(x)
$$

Derivace prave strany:
$$
\frac{d}{dx}(x^x\ln(x)) = \frac{d}{dx}(x^x) \cdot\ln(x) + x^x \cdot\frac{d}{dx}(\ln(x))
$$

Derivace $x^x$:
$$
y = x^x
$$
$$
\ln(y) = x\ln(x)
$$
Zderivujeme
$$
\frac{1}{y} =\ln(x) + 1
$$
$$
= (\ln(x)+1) \cdot x^x
$$

Dosadime zpet:
$$
\frac{d}{dx}(x^x\ln(x)) = ((\ln(x)+1)\cdot x^x) \cdot \ln(x) + x^x \cdot \frac{1}{x}
$$

$$
\frac{1}{y} \cdot \frac{dy}{dx} =\ln(x) \cdot x^x(\ln(x)+1) + \frac{x^x}{x}
$$
$$
f'(x)=\frac{dy}{dx} = x^{x^x}\cdot \left[ \ln(x) \cdot x^x(\ln(x)+1) + \frac{x^x}{x} \right] 
$$

Definicni obor f je $\mathbb{R}^+_{0}$. 

---
f)

$$
f(x) = x^2 \sin\left( \frac{1}{\sqrt[3]{x}} \right)
$$

Pouzijeme retezove pravidlo na toto:

$$
f'(x) = 2x \sin\left( \frac{1}{\sqrt[3]{x}} \right)  + x^2 \cdot \frac{d}{dx} \left( \sin\left( \frac{1}{\sqrt[3]{x}} \right) \right) 
$$

Muzeme napsat
$$
y = g(h(x))
$$
Kde $g(x) = \sin x$ a $h(x)=\frac{1}{\sqrt[3]{ x }}$.

pak $$\frac{dy}{dx} = g'(h(x)) \cdot h'(x)$$

$$
g'(h(x)) = \cos \left( \frac{1}{\sqrt[3]{ x }} \right) 
$$


$h(x) = x^{-1/3}$
$$
h'(x) = -\frac{1}{3} x ^{-4/3} = -\frac{1}{3 \cdot (\sqrt[3]{  x})^4}
$$

Dosadime:

$$
f'(x) = 2x \sin\left( \frac{1}{\sqrt[3]{x}} \right)  + x^2 \cdot \cos \left( \frac{1}{\sqrt[3]{ x }} \right) \cdot \left(  -\frac{1}{3 \cdot (\sqrt[3]{  x})^4}\right) 
$$

Definicni obor jsou vsechna realna cisla krome nuly.