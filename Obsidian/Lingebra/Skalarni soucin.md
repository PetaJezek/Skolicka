
1. **(10 bodů)** Mějme zobrazení  
   $$\langle x, y \rangle = 5x_1y_1 - 2x_1y_2 - 2x_2y_1 + 3x_2y_2$$  
   a vektory  
   $$x' = \begin{pmatrix}1 \\ 2\end{pmatrix}, \quad y' = \begin{pmatrix}2 \\ 5\end{pmatrix}.$$

   (a) **(6 bodů)** Ukažte, že $\langle x, y \rangle$ je skalárním součinem.  

1) $\langle x,x\rangle \geq 0$ pokud $x \neq 0$:   $\langle x, x \rangle= 5x_{1}^2-4x_{1}x_{2}+3x_{2}^2$

Ziskavame kvadratickou kde: $a=5;b=4;c=3$

Dererminant techto koeficientu je roven:
$$
b^2-4ac=16-60=-44
$$ 
A tedy neexistuji nenulove hodnoty $x_{1},x_{2}$ pro ktere by se vyraz rovnal nule. Prvni axiom je splnen.

2)  $\langle x+y,z\rangle = \langle x,z \rangle + \langle y,z \rangle$
$$
\langle x+y,z\rangle =  5(x_1+y_1)z_{1} - 2(x_{1}+y_{1})z_2 - 2(x_2+y_{2})z_1 + 3(x_2+y_{2})z_2 
$$

To muzeme dale rozepsat jako:
$$
5x_{1}z_{1}+5y_{1}z_{1}-2x_{1}z_{2}-2y_{1}z_{2}-2x_{2}z_{1}-2y_{2}z_{1}+3x_{2}z_{2}+3y_{2}z_{2}
$$
Seskupime x a y:
$$
5x_{1}z_{1}-2x_{1}z_{2}-2x_{2}z_{1}+3x_{2}z_{2} + 5y_{1}z_{1}-2y_{1}z_{2}-2y_{2}z_{1}+3y_{2}z_{2}
$$
A vidime ze vyraz muzeme prepsat jako:
$$
\langle x,z \rangle + \langle y,z \rangle
$$
Druhy axiom dokazan.


3) Pro $\alpha \in \mathbb{R}: \langle \alpha x,y \rangle = \alpha \langle x,y \rangle$

$$
\langle \alpha x,y \rangle = 5\alpha x_{1}y_{1}-2\alpha x_{1}y_{2}-2\alpha x_{2}y_{1}+3\alpha x_{2}y_{2} 
$$
Po vytknuti $\alpha$:
$$
= \alpha ( 5x_1y_1 - 2x_1y_2 - 2x_2y_1 + 3x_2y_2) = \alpha \langle x,y \rangle 
$$
Treti axiom dokazan.

4)$\langle x,y \rangle = \langle y,x \rangle$

Prohozeni $x$ a $y$:
$$
\langle y, x \rangle = 5y_1x_1 - 2y_1x_2 - 2y_2x_1 + 3y_2x_2
$$

Po prepsani:
$$
= 5x_1y_1 - 2x_2y_1 - 2x_1y_2 + 3x_2y_2
$$

Muzeme porovnat:
$$
\langle x, y \rangle = 5x_1y_1 - 2x_1y_2 - 2x_2y_1 + 3x_2y_2
$$

$$
\langle y, x \rangle = 5x_1y_1 - 2x_1y_2 - 2x_2y_1 + 3x_2y_2
$$

Ctrvty axiom je dokazan.

**Jedna se o skalarni soucin.**

   (b) **(1 bod)** Spočtěte $\langle x', y' \rangle$.  

$$
5x_1y_1 - 2x_1y_2 - 2x_2y_1 + 3x_2y_2 = 5\cdot 2 - 2 \cdot 5 - 2 \cdot 2 \cdot 2 + 3\cdot 2 \cdot 5 = 22
$$


   (c) **(1 bod)** Spočtěte $\|x'\|$.  

Normu vektoru $x'$ spočítáme pomocí vztahu:

$$
\|x'\| = \sqrt{\langle x', x' \rangle}
$$

$$
\langle x', x' \rangle = 1 \cdot 1 + 2 \cdot 2 = 1 + 4 = 5
$$

Nyní spočítáme normu:

$$
\|x'\| = \sqrt{\langle x', x' \rangle} = \sqrt{5}
$$

Takže norma vektoru $x'$ je $\|x'\| = \sqrt{5}$.

   
   (d) **(2 body)** Spočtěte vzdálenost $x'$ od $y'$.

Vzdalenost spocitame pomoci normy. Vektor mezi dvema vektory se rovna jejch rozdilu. 
$$
||x'-y'|| = \sqrt{ \langle x'-y', x'-y' \rangle  } =
$$
$$
= \sqrt{-1\cdot(-1) + (-3)\cdot(-3)} = \sqrt{ 10 }
$$

2. **(3 body)** Dokažte, nebo vyvraťte, že v prostoru matic $\mathbb{R}^{m \times n}$ je zobrazení  
   $$\langle A, B \rangle = \sum_{i=1}^{m} \sum_{j=1}^{n} a_{ij} b_{ij}$$  
   skalární součin. 

Pro skalarni soucin musi platit:  
$\langle x,x\rangle \geq 0$ pokud $x \neq 0$
Vysledek je soucet vsech hodnot v matici x na druhou. To znamena, ze vsechna cisla jsou bud nula nebo kladna. Jedina mozna kombinace jak zajistit abych soucet techto cisel byl nula je, ze vsechna cisla musi byt nula. Prvni axiom plati.

$\langle x+y,z\rangle = \langle x,z \rangle + \langle y,z \rangle$
Muzeme dokazat pro libovolnou (obecnou) pozici $i,j$. Nemusime koukat na cele matice ale staci koukat na jednu pozici  protoze:
$$\langle A, B \rangle = \sum_{i=1}^{m} \sum_{j=1}^{n} a_{ij} b_{ij}$$  
Muzeme zapsat jako:
$$
\forall i,j \in \mathbb{R}:\langle a_{ij}, b_{ij} \rangle = a_{ij}b_{ij}
$$

Potom dosadime:
$$
\langle x_{ij}+y_{ij} , z_{ij}\rangle = x_{ij}z_{ij} + y_{ij}z_{ij} = \langle x_{ij},z_{ij} \rangle  + \langle y_{ij},z_{ij} \rangle 
$$

Druhy axiom plati.



$\alpha \in \mathbb{R}: \langle \alpha x,y \rangle = \alpha \langle x,y \rangle$

Jednoduse muzeme upravit:
$$\langle \alpha A, B \rangle = \sum_{i=1}^{m} \sum_{j=1}^{n} \alpha a_{ij} b_{ij} = \alpha\sum_{i=1}^{m} \sum_{j=1}^{n} a_{ij} b_{ij} = \alpha \langle A, B \rangle$$  
Treti axiom plati.
$\langle x,y \rangle = \langle y,x \rangle$
Staci prehodit pismena alfa a beta. Nasobeni je komutativni, takze poradi nema vliv.
Posledni axiom dokazan.
**Jedna se o skalarni soucin.**




4. **(3 body)** Je skalární součin lineárním zobrazením, jak ho máme zadefinované v Lineární algebře 1?


$\text{Lineární zobrazení } T: V \to W \text{ splňuje dvě vlastnosti:}$
$$
1. \quad T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})
$$
$$
2. \quad T(c \mathbf{v}) = c T(\mathbf{v})
$$
A taky: Zobrazuje nulu na nulu. (Trivialni dukaz)

Soucet skalarnich soucinu je roven skalarnimu soucinu souctu:

$$
\langle x+y,x+y \rangle = \langle x,x \rangle + \langle y,y \rangle 
$$
Tohle neplati, pro vsechny zobrazeni. Napr. 
$$
\langle x,y \rangle = x_{1}y_{1}+x_{2}y_{2}
$$

Protoze leva strana se pak rovna:
$$
\langle x,x \rangle + \langle y,y \rangle  +2\cdot \langle x,y \rangle \neq \langle x,x \rangle + \langle y,y \rangle  
$$

Tedy skalarni soucin neni linearni zobrazeni, pro vsechny svoje zobrazeni.

4. **(6 bodů)** Určete úhel mezi:  
   (a) **(3 body)** vektory  	 
$$
x = \begin{pmatrix}0 \\ 0 \\ 1\end{pmatrix}, \quad y = \begin{pmatrix}1 \\ 0 \\ -1\end{pmatrix}.
$$  


$$
\cos \theta = \frac{\langle \mathbf{x}, \mathbf{y} \rangle}{\|\mathbf{x}\| \|\mathbf{y}\|}
$$

Skalární součin:

$$
\langle \mathbf{x}, \mathbf{y} \rangle = 0 \cdot 1 + 0 \cdot 0 + 1 \cdot (-1) = -1
$$

$$
\|\mathbf{x}\| = 1
$$
$$
\|\mathbf{y}\| = \sqrt{2}
$$

$$
\cos \theta = \frac{-1}{1 \cdot \sqrt{2}} = \frac{-1}{\sqrt{2}}
$$

Uhel se rovna:
$$
\cos^{-1} \frac{-1}{\sqrt{ 2 }} = 135^\circ
$$



   (b) **(3 body)** hlavní diagonálou krychle a její podstavou.
To se rovna uhlu mezi vektory hlavni diagonaly a diagnoaly dane podstavy .

Pro krychli o stranach $a$ se vektory budou rovnat:

$$
\mathbf{d_1} = \begin{pmatrix} a \\ a \\ a \end{pmatrix}, \quad \mathbf{d_2} = \begin{pmatrix} a \\ a \\ 0 \end{pmatrix}
$$
Skalarni soucin:
$$
\langle \mathbf{d_1}, \mathbf{d_2} \rangle = a \cdot a + a \cdot a + a \cdot 0 = 2a^2
$$
Normy:
$$
\|\mathbf{d_1}\| = \sqrt{a^2 + a^2 + a^2} = \sqrt{3}a, \quad \|\mathbf{d_2}\| = \sqrt{a^2 + a^2} = \sqrt{2}a
$$

Pod dosazeni ziskavame:
$$
\theta = \arccos\left( \frac{\sqrt{6}}{3} \right) \approx 35.26^\circ
$$

5. **(4 body)** Buď $A \in \mathbb{R}^{n \times n}$ regulární. Ukažte, že pro $i \neq j$ je $i$-tý řádek matice $A$ kolmý na $j$-tý sloupec matice $A^{-1}$.


$A\cdot A^{-1}=I_{n}$

To znamená, že pouze pri  souctu nasobku prvku i-teho radku matice A a i-teho sloupce matice $A^{-1}$ je  vysledek  1. Jinak  je vzdy nula. 

Protoze kolmost je definovana:

$x,y \text{ jsou kolme pokud } \langle x,y\rangle =0$

Muzeme tento dusledek pouzit na sklarani soucin (kolmost),
jelikoz vzorec pro prvek soucinu matic:
$$
c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}
$$

Je totozny se vzorcem skalarniho soucinu. Soucet soucinu jednotlivych prvku.
Tedy pro vsechna $x_{ij} \in I_{n}: i \neq j; x_{ij}=0$. 

Tedy skalarni soucet  $i$-tho řádku matice $A$ a$j$-teho sloupce matice $A^{-1}$ pro $i \neq j$ vzdycky bude 0 resp. kolme.. A naopak kdyz i=j, bude skalarni soucin roven 1.


6. **(8 bodů)** Zaveďte v prostoru $\mathbb{R}^2$ skalární součin tak, aby $x'$ bylo kolmé na $y'$, kde  
   $$x' = \begin{pmatrix}1 \\ 2\end{pmatrix}, \quad y' = \begin{pmatrix}2 \\ 3\end{pmatrix}.$$  
