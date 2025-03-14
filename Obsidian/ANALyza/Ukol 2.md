# Příklad 1

Podle definice určete limitu posloupnosti  
$$
(a_n)_{n=1}^{\infty} = \frac{n-1}{n+1}
$$

Můžeme předpokládat, že limita bude jedna protože čitatel i jmenovat se neustále přibližují:
$$
\dots,\frac{1000}{1002}, \dots, \frac{1000000}{1000002},\dots
$$

Dle definice limit cheme dokázat že $\exists n_{0}: n_{0}<n:|a_{n}-1| < \epsilon$

$$
a_{n}=\frac{n-1}{n+1} 
$$

Rozepiseme:
$$
\left|  \frac{n-1}{n+1}  - 1\right| < \epsilon
$$
$$
\left| \frac{n-1 - n -1}{n+1} \right| < \epsilon
$$
$$
\left| \frac{-2}{n+1} \right| = \frac{2}{n+1} < \epsilon
$$
 Z teto rovnice ziskavame:
 $$
\frac{2}{\epsilon} < n+1 
$$
$$
\frac{2}{\epsilon} -1 < n 
$$
To znamena ze pro kazde epsilon jsme schopni zvolit n tak, aby vyraz platil. Tedy :

$$\lim_{ n \to \infty } \frac{n-1}{n+1} = 1$$

Pro epsilon $\epsilon = 2$ bude $n_{0}=2$. Pro libovolné epsilon se bude $n_0 = \left\lceil \frac{2}{\varepsilon} - 1 \right\rceil$.






# Příklad 2

Rozhodněte, zda mají následující posloupnosti $(a_n)$ limitu. Spočtěte, nebo ukažte, že neexistuje.

- **a)**  $a_n = (-1)^{n!}$

Vysledek pro $\forall n > 1 \in \mathbb{N}: (-1)^{n!}  1$, protože faktoriál libovolného přirozeného čísla (kromě 1) je sudý (v jeho "rozpisu" je dvojka). Tato posloupnost nenabývá hodnoty větší než 1 a tedy"
$$
\lim_{ n \to \infty } (-1)^{n!} = 1
$$



- **b)** $a_n = \cos\left(\frac{n\pi}{4}\right)$
Jelikož cosinus není prostá funkce, nemá limitu na celém definičním oboru. Má limity na intervalech, ale na to se doufám zadání neptá. Cosinus je periodická funkce a input této funkce je lineární, takže obor hodnot bude interval $<-1;1>$.  S tím, že pokud 
$$
a_{n}	\lim_{ n \to \infty }  \cos\left(\frac{n\pi}{4}\right) = 1
$$
Pak musí  platit:
$$
a_{n+4} \lim_{ n \to \infty }  \cos\left(\frac{(n + 4)\pi}{4}\right) = -1
$$

**Pokud máme dvě podposloupnosti, které konvergují k jiným hodnotám, pak posloupnost, ze které tyto podposloupnosti jsou, nemá limitu.** 





- **c)** $a_n = \log(\sqrt{ n })$

Logaritmus roste pomalu, ale "nekončí", takže jeho má nevlastní limitu $+\infty$

Použijeme mé dřivější tvrzení které se týkalo čistého logaritmu n. 

Posloupnost můžeme rozepsat jako:
$$
\log\left( n^\frac{1}{2} \right) = \frac{1}{2}\log n
$$

Víme že $\lim_{ n \to \infty }\log n=+\infty$
Řekneme, že funkce $f(n)$ diverguje k $\infty$, pokud pro každé reálné číslo M existuje N, takové že pro všechna $n≥N$ platí:
$$
f(n)>M
$$
To že nasobime jednou polovinou nic nemeni protože to je konstanta. Takže výsledná limita je nekonečno.



# Příklad 3

Spočtěte limitu  
$$
\lim_{n \to \infty} \frac{3n^4 - n^2 + 1}{n^4 + n^3 + n - 2}
$$
Po vydeleni $n_{4}$:
$$
\lim_{n \to \infty} \frac{3- \frac{1}{n^{3}} + \frac{1}{n^{4}}}{1 + \frac{1}{n} + \frac{1}{n^{3}} - \frac{2}{n^{4}}}
$$
Všechny zlomky divergují k nule, takže nám zbyde:
$$
\lim_{n \to \infty} \frac{3n^4 - n^2 + 1}{n^4 + n^3 + n - 2} =\lim_{ n \to \infty } 3 
$$

