Polomer = 1

Distribucni funkce:

$$
F_{X}(x) = P(X<x) = P(X\leq x)
$$
Druha rovnost vychazi z toho ze hazeni nase distribucni funkce bude spojita, protoze hod na terc je diskretni pouze pri pocitani bodu a ne pri pocitani vzdalenosti od stredu.


Pak tedy pro $x \in [0,1]$ distribucni funkce vzdalenosti hodu od stredu na terc s polomerem 1 je:

$$
P(X\leq x) = \frac{\pi x^{2}}{\pi} = x^{2}
$$

Hustotni funkce je derivace Distribucni funkce:

$$
f_{X}(x) = F'_{X}(x) = 2x
$$



Ocekavana hodnota $E(X)$:

$$
E(X) =  \int_{0}^{1} x\cdot f_{X}(x) \, dx = \int_{0}^{1} 2x^{2} \, dx = \frac{2}{3}
$$


$$
E(X^{2})= \int_{0}^{1} x^{2} f_{X}(x) \, dx = \int_{0}^{1} 2x^{3} \, dx = \frac{2}{3}
$$


Rozptyl :

$$
var(X) = E(X^{2})- (E(X))^{2} = \frac{2}{3}-\frac{4}{9} = \frac{2}{9}
$$


Smerodatna odchylka:

$$
\sigma_{X} = \sqrt{ var(X) }= \sqrt{ \frac{2}{9} }= \frac{\sqrt{ 2 }}{3}
$$


Na pociti bych samploval nasledovne. Pro kazdy hod bych zvolil nahodne souradnice $x$ a $y$ na intervalech od -1 do 1. Aby byl hod platny, musi jeste platit:

$$
\sqrt{ x^{2}+y^{2} } \leq1
$$
Pokud je podminka splnena hod je platny a mohu ho zapocitat jako vzorek. 



