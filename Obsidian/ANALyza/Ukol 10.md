Urcete derivace a definicni obory nasledujicich funkci.
a)
$$
f(x)= \log_{2}(x+\sqrt{ 1+x^2 })
$$

pokud $f(x) =g(h(x))$, kde $g(x) = \log_{2}x$ a $h(x) = x + \sqrt{ 1+x^2 }$, pak muzeme pouzit retezove pravidlo:
$$
h'(x) = (x+(1+x^2)^{1/2})'= 1 + ((1+x^2)^{1/2})' = 1 + \frac{1}{2\sqrt{ 1+x^2 }} \cdot 2x= 1 + \frac{x}{\sqrt{ 1+x^2 }}
$$



$$
f'(x) = g'(h(x)) \cdot h'(x) = \frac{1}{(x+ \sqrt{ 1+x^2 })\ln_{2}} \cdot \left(1 + \frac{x}{\sqrt{ 1+x^2 }}\right)
$$

