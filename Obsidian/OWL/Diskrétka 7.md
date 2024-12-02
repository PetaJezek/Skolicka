$X(\pi)=$ počet pevných bodů. Máme množinu $I$, která o každé pozici říká zda se zobrazí na sebe či nikoliv. Jelikož nám sděluje hodnoty True a False: bude obsahovat pouze 0 a 1. 0 pokud se pozice nezobrazuje na sebe a 1 pokud ano. To znamená že:
$$
X(\pi)=\sum_{i=1}^nI_{i}
$$


Když hledáme střední hodnotu $X(\pi)$, můžeme ji spočítat jakou součet středních hodnot prvků $X(\pi)$. (To vychází z linearity střední hodnoty).

Takže:
$$
\mathbb{E}(X)=\mathbb{E}\sum_{i=1}^nI_{i} = \sum_{i=1}^n\mathbb{E}(I_{i})
$$
$$
\mathbb{E}(I_{i}) = \text{pravděpodobnost, že se zobrazí sám  na sebe}
$$
Všechny prvky mají tuto pravěpodobnost stejnou a to: $$\frac{1}{n}.$$

Dosadíme zpátky do naší rovnce:$$
\mathbb{E}(X)= \sum_{i=1}^n\mathbb{E}(I_{i})=\sum_{i=1}^n \frac{1}{n}=n\cdot \frac{1}{n}=1$$

To znamená, že **průměrně každá náhodná permutace má právě jeden pevný bod**.
