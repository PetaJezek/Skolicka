
$$
a) \lim_{ x \to \infty } x \cdot \sin\left( \frac{1}{x^2} \right)
$$

Protože $\sin$ nabývá hodnot $-1$ až $1$, tak jde limita do $\pm \infty$. Můžeme tedy použít L'Hospitalovo pravidlo.

Derivace $x =1$. Derivace $\sin\left( \frac{1}{x^2} \right)$ je slozitejsi.

$$
\left( \sin\left( \frac{1}{x^2} \right)  \right)'    
$$

Definujeme 
$$
g(x) = \frac{1}{x^2};~~~ f(x)=\sin x
$$

Muzeme derivovat jako :
$$
\cos\left( \frac{1}{x^2} \right)\cdot \left(-\frac{2}{x^3}\right) 
$$

Vysledna limita je rovna:
$$
\lim_{ x \to \infty } \cos\left( \frac{1}{x^2} \right)\cdot \left(-\frac{2}{x^3}\right) = 0
$$
To platí protože druhá závorka konverguje k nule.

$$
b)\lim_{ x \to \infty } x^2\cdot \ln\left( 1+\frac{1}{x^2} \right)
$$

$x^2$ jde do nekonečna a $\ln\left( 1+\frac{1}{x^2} \right)$ také. Limita by tedy byla $\infty$. Můžeme tedy použít L'Hospitalovo pravidlo.


Udelame to stejne co u prikladu a). 
	
Derivace $x^2$ je $2x$. U druhe casti vyuzijeme řetězové pravidlo.

Definujeme:
$$
g(x)=\frac{1}{x^2}+1; f(x)=\ln x
$$

$$
\left( \ln\left( 1+\frac{1}{x^2} \right) \right)'= \frac{1}{x+\frac{1}{x^2}}\cdot \left( -\frac{2}{x^3}  \right) 
$$
Muzeme upravit:

$$
=-\frac{2}{x\cdot(x^3+1)}
$$

Spojime to s $x^2$:

$$
\lim_{ x \to \infty }\left( x^2\cdot \ln\left( 1+\frac{1}{x^2} \right)\right)' = 2x \cdot-\frac{2}{x\cdot(x^3+1)} = -\frac{4}{x^3+1}=0
$$
Limita se rovná nule, protože jmenovatel jde konverguje do nekonečna a čitatel je roven $4$.

## Priklad 2

$$
a) ~~~~~~~f(x)=\begin{cases} x^2 + \frac{1}{x} & x \neq 0 \\ 0 & x = 0 \end{cases}​
$$

$x^2+\frac{1}{x}$ je spojita funkce krome $0$. Musime proverit zda plati:

$$
\lim_{ x \to 0 } f(x)=0
$$

$$
\lim_{ x \to 0^+ } x^2+\frac{1}{x}=0+\infty=+\infty 
$$
$$
\lim_{ x \to 0^- } x^2+\frac{1}{x}=0-\infty=-\infty
$$
To znamená, že tato funkce není spojitá. Není spojitá v bodě $x=0$ ani zleva ani zprava.

Funkce $f(x)$ je spojitá na $\mathbb{R} \setminus \{0\}$.

$$
b) f(x)=\begin{cases} \exp(1 + \frac{1}{x}) & x \neq 0 \\ 0 & x = 0 \end{cases} ​
$$

Opet kontrolujeme spojitost v bode 0.

$$
\lim_{ x \to 0 } f(x)=\lim_{ x \to 0 } e^{1+1/x}
$$

$$
\lim_{ x \to 0^- } e^{1+1/x}= \lim_{ x \to 0^- } e^{-\infty}=0
$$
$$
\lim_{ x \to 0^+ } e^{1+1/x}=\lim_{ x \to 0^+ } e^{+\infty}=+\infty
$$

Tedy funkce neni oboustraně spojita v bodě $x=0$, ale je v tomto bodě pouze spojitá z leva.

Funkce $f(x)$ je spojitá na $\mathbb{R} \setminus \{0\}$.