

Plnicí linka má plnit sáčky na průměrnou hmotnost $500$ g. Ve vzorku $n = 36$ sáčků vyšel průměr $\bar{X} = 504.5$ g. Testujeme na hladině $\alpha = 0.05$

$$ H_0:\ \mu = 500 \qquad\text{proti}\qquad H_1:\ \mu > 500 . $$

## a) z-test (známe $\sigma = 12$ g)

**$H_0$:** $\mu = 500$.

$$ Z = \frac{\bar{X} - \mu_0}{\sigma/\sqrt{n}} = \frac{504.5 - 500}{12/\sqrt{36}} = \frac{4.5}{2} = 2.25, \qquad Z \stackrel{H_0}{\sim} N(0,1). $$

**p-hodnota.** Alternativa je pravostranná, takže

$$ p = P(Z > 2.25) = 1 - \Phi(2.25) = 1 - 0.98778 \approx 0.0122 . $$

 Kritická hodnota $q_{0.95} = 1.645$. Protože $2.25 > 1.645$ (resp. $p \approx 0.0122 < 0.05$), zamítáme $H_0$. Data svědčí o tom, že plníme víc než $500$ g.

## b) t-test ($s = 12$ g je výběrová směrodatná odchylka)

**$H_0$:** $\mu = 500$.

Testová statistika. Číselně vychází stejně, jen $\sigma$ nahradíme odhadem $s$:

$$ T = \frac{\bar{X} - \mu_0}{s/\sqrt{n}} = \frac{504.5 - 500}{12/\sqrt{36}} = 2.25, \qquad T \stackrel{H_0}{\sim} t_{35}\quad(n-1 = 35). $$

p-hodnota.

$$ p = P(T_{35} > 2.25) \approx 0.0154 . $$

Z tabulky bychom viděli jen, že leží mezi $0.01$ a $0.025$, neboť $2.030 < 2.25 < 2.438$.

Rozhodnutí. Kritická hodnota $q_{0.95} = 1.690$. Protože $2.25 > 1.690$ (resp. $p \approx 0.0154 < 0.05$), zamítáme $H_0$ i zde.



## c) Porovnání p-hodnot

|Test|p-hodnota|
|---|---|
|z-test|$0.0122$|
|t-test|$0.0154$|

Menší je p-hodnota u z-testu.
