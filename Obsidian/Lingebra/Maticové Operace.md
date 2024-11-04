1. Dokažte z definice, že platí $$
\alpha(AB) = (\alpha A)B = A(\alpha B)
$$

Ze vzorce pro násobení matic dostáváme: $$
\alpha \cdot \sum_{k=1}^{n} a_{ik}\cdot b_{kj} = \sum_{k=1}^{n} (\alpha a_{ik})\cdot b_{kj} = \sum_{k=1}^{n} (a_{ik}\cdot (\alpha b_{kj}) $$
A z pravidla distributivity získáme:
$$
\sum_{k=1}^{n} \alpha(a_{ik}b_{kj}) = \sum_{k=1}^{n} \alpha(a_{ik}b_{kj}) = \sum_{k=1}^{n} \alpha(a_{ik}b_{kj}) 
$$
Všechno se rovná. Tvrzení je pravdivé.

2. Dokažte, že $$A^tA$$ je symetrická matice pro každé:
$$
A \in R^{m\cdot n}
$$
Nejdříve zjistíme, jeslti je výsledek tohoto součinu vůbec matice.
$$
A^{m\cdot n} \cdot A^{t^{n\cdot m}} = B^{n\cdot n}
$$
Výsledek tedy je matice a to čtvercová. Na wikipedii jsem našel vlastnost symetrické matice A:
$$
A = A^t
$$
To znamena:
$$
A \cdot A^t = (A\cdot A^t)^t
$$
Z "vzorce" pro transpozici závorek:
$$
A \cdot A^t = A \cdot A^t
$$
Obě strany se rovnají. Tento součin tedy splňuje vlastnost symetrické matice a jeho výsledek tedy je symetrická matice.

#
3. Ukažte, že součin horních trojúhelníkových matic je zase horní trojúhelníková matice. Matice \(A\) je horní trojúhelníková, pokud $$a_{ij} = 0 \quad \text{pro všechny} \quad i > j$$

Toto je naše obecné A:
$$
A = \begin{pmatrix}
a_{11} & a_{12} & a_{13} & \cdots & a_{1n} \\
0 & a_{22} & a_{23} & \cdots & a_{2n} \\
0 & 0 & a_{33} & \cdots & a_{3n} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \cdots & a_{nn}
\end{pmatrix}
$$

Pro náš součin budeme tedy uvažovat matice $$
A^{m\cdot n}, B^{n\cdot m} = C^{n\cdot n}$$
Pro obě platí  $$a_{ij}, b_{ij} = 0 \quad \text{pro všechny} \quad i > j$$
 
Ze vzorce pro násobení matic:
$$
c_{ij} = \sum_{k=1}^{n} a_{ik}\cdot b_{kj}
$$
Aby C byla taky horní trojúhelníková matice, musí platit:

$$c_{ij} = 0 \quad \text{pro všechny} \quad i > j$$
Musíme tedy pouze zkontrolovat všechny i > j.

Pokud je k < i: 
$$
a_{ik} = 0
$$
Pokud je k > j
$$
b_{kj} = 0
$$
A pokud k = j,i,
je nám výsledek jedno, protože to se nacházíme na diagonále a neovliňuje to výsledek.

Nemůže se stát jiná situace např.
$$
k >i \land k > j
$$
protože i > j.

Tím jsme dokázali pravdivost našeho tvrzení.


 4. Najděte čtvercovou matici řádu $n$, která splňuje $I - A = A^2$.
$$
I_n = \begin{pmatrix} 
1 & 0 & 0 & \cdots & 0 \\ 
0 & 1 & 0 & \cdots & 0 \\ 
0 & 0 & 1 & \cdots & 0 \\ 
\vdots & \vdots & \vdots & \ddots & \vdots \\ 
0 & 0 & 0 & \cdots & 1 
\end{pmatrix}
$$

Pro ujasnění zadání můžeme tento příklad spočitítat pro $n = 1$.

Získáváme rovnici:


$$
1 - x = x^2
$$
$$
1 = x(x+1)
$$
(po dosazení do kalkulačky) Získáváme výsledek: 
$$\alpha_1 = \frac{-1 + \sqrt{5}}{2}, \quad \alpha_{2} = \frac{-1 - \sqrt{5}}{2}$$

Pokud bychom zvolili n > 1, už bychom nedostali takto pěknou rovnici, protože např. pro n = 2 bychom od dvou jedniček bychom odečítali $a_{11}$ a $a_{22}$ ale zbylé prvky matice a bychom odečítal od nuly což nám vrátí invertovanou hodnotu prvku. To znamená, že na hlavní diagonále musí být prvky rovny jednomu z kořenů naší první rovnice, neboť to jsou jediná čísla splňující danou rovnici. Co se týče zbylých prvků, získáváme rovnici:
$$
0 - x = x^2
$$
$$
x(x+1) = 0
$$
$$
x_{1} = 0, \quad x_{2} = -1
$$
To znamená, že všechny matice která na hlavní diagonále mají čísla$\frac{-1 + \sqrt{5}}{2}\quad \text{nebo} \quad x_2 = \frac{-1 - \sqrt{5}}{2}$ a zbytek roven bud 0 nebo -1.

TED MI DOŠLO ŽE POUŽÍVAM ELEMENT-WISE UMOCNĚNÍ MATICE.



Pokud bereme v potaz že $A^2=A\cdot A$ pak výsledek získáme následovně:

Vždy když budeme odečítat od hlavní diagonály matici A, která má čísla rovna kořenům z naší první rovnice, podmínka bude platit. 

$$
A = \begin{pmatrix}
\alpha_1 & 0 & 0 & \cdots & 0 \\
0 & \alpha_2 & 0 & \cdots & 0 \\
0 & 0 & \alpha_1 & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \cdots & \alpha_2 \\
\end{pmatrix}_{n \times n}
$$
Příklad pro n = 4:
$$
A = \begin{pmatrix}
\frac{-1 + \sqrt{5}}{2} & 0 & 0 & 0 \\
0 & \frac{-1 - \sqrt{5}}{2} & 0 & 0 \\
0 & 0 & \frac{-1 + \sqrt{5}}{2} & 0 \\
0 & 0 & 0 & \frac{-1 - \sqrt{5}}{2} \\
\end{pmatrix}_{4 \times 4}
$$


5.  Najděte matici $B \in \mathbb{R}^{n \times n}$ takovou, aby pro každou matici $A \in \mathbb{R}^{n \times n}$ platilo:
   - (a) $BA = 5A$,
   - (b) $BA = 5B$,
   - (c) všechny řádky $BA$ jsou stejné jako první řádek $A$.


a)

Aby B nezměnilo A ale jen ho skalarne vynasobilo 5, musí mít podobu Jednotkové matice skalarně vynasobené pěti.
$$
B = \begin{pmatrix}
5 & 0 & 0 & \cdots & 0 \\
0 & 5 & 0 & \cdots & 0 \\
0 & 0 & 5 & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \cdots & 5 \\
\end{pmatrix}_{n \times n}

$$
b)
Protože je matice A libovolná, jediný způsob jak můžeme zaručit že BA bude 5B je když je B bude nulové. Protože jinak nám libovolné A vytvoří libovolné výsledky
$$
B = \begin{pmatrix}
0 & 0 & 0 & \cdots & 0 \\
0 & 0 & 0 & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \cdots & 0
\end{pmatrix}_{n \times n}


$$
c)
Chceme abychom pomocí B vybrali na každý řádek výsledné matice první řádek A.
Toho dosáhneme tak že první sloupec matice B budou jedničky a zbytek nuly.

$$
B = \begin{pmatrix}
1 & 0 & 0 & \cdots & 0 \\
1 & 0 & 0 & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & 0 & 0 & \cdots & 0
\end{pmatrix}_{n \times n}

$$
6. Matice $A \in \mathbb{R}^{n \times n}$ je stochastická (nebo také markovská), pokud její prvky leží v intervalu $[0, 1]$ a součet každého sloupce je 1. Dokažte, že součin stochastických matic je stochastická matice.



