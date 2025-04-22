1.

Důkaz o opaku tvrzení provedu sporem.

Nechť matice $P,Q$ jsou tvořeny vektory z báze $B  \text{ (resp. } C)$. Jelikož matice sčítáme, musí mít stejnou velikost.  Tedy báze $B$ a báze $C$ generují stejný prostor. Nechť v i-tém sloupci matice $P$ je vektor $d=(1,0,\dots,0)$ a v matici $Q$ je vektor $e=(-1,0,\dots,0)$. Oba dva vektory jsou ortonormální, takže jsou i ortogonální. Pokud je ale sečteme, získáme nulový vektor. Z definice vlastních vektorů ale víme, že nulový vektor nemůže být ortogonální, a proto $P+Q$ není ortogonální. 
**Tvrzení neplatí.**


2.
Najděte všechny diagonální ortogonální matice řádu n. Kolik jich je?

Hledám všechny matice $Q^{n \times n}$ pro které platí:
$$
Q^TQ = I
$$
Tyto matice zároveň musí být diagonální, to znamená, že všechny vektory mají pouze jeden prvek (I-tý řádek  má prvek na i-té pozici). Získáváme rovnici:
$$
I_{jj} = \sum_{i=1}^{n} q_{ij}q_{ji}^T= q_{jj}^2 
$$
Toto platí, protože na všech pozicích v obou vektorech jsou nuly, kromě toho když $i=j$. 

Tedy získáváme rovnici  
$$
1 = q^2
$$
$$
q = \pm 1
$$

Tedy máme dvě matice, které splňují naše podmínky jsou:
$$
I, -I
$$

3.
Ortogonální matice  $Q$ obsahuje pouze prvky  $\frac{1}{4}$ a $-\frac{1}{4}$. Jaký je rozměr matice  $Q$?

Vektor $v$ ortogonalní matice $Q$ musí být z definice ortonormální. To znamená:
$$
\left| \left| v \right| \right|=1
$$
Z tohoto vztahu dostavame rovnici:
$$
\sqrt{ a \cdot\left(\frac{1}{4} \right)^2 + b \cdot \left( -\frac{1}{4} \right)^2 } =1
$$
Pro $a,b \in \mathbb{N}$. Muzeme upravit na:
$$
\sqrt{ c \cdot \left( \frac{1}{16} \right)  } = 1
$$
$$
c=16
$$
Z tohoto výsledku vyplívá, že na vytvoření ortonormálního vektoru pomocí prvků $\frac{1}{4}$ a $-\frac{1}{4}$ je potřeba vektor délky minimálně 16.
A nezalezi na pozici prvku.

Ted je otazka. Zda jsem pro libovolny vektor v, najit 15 vektoru $u_{i}; i \in[15]$, pro ktere plati:
$$
\forall i :\left| \langle v,u_{i} \rangle  \right|=0
$$
$$
\sum_{j=1}^{n} v_{j}u_{j} = 0
$$
Pro každé $v_{j}$  jsou možnosti $u_{j}$:
$$
\begin{cases} \frac{1}{4}\\ 
-\frac{1}{4}

\end{cases} \\
$$
Tedy
$$
v_{j}u_{j}= \pm \frac{1}{16}
$$
Aby platilo $vu=0$, musí být stejný počet $\frac{1}{16}$ a $-\frac{1}{16}$.

Pokud zacneme s vektorem $v=\left( \frac{1}{4}, -\frac{1}{4}, \frac{1}{4}, -\frac{1}{4},\dots \right)$.

Pak počet validních permutací je 
$$
\binom{16} {8}= 12870
$$
Tedy jsme schopni nalezt 15 vektoru, ktere vudou tvorit $Q$.

To znamena, že rozmer matice $Q$ je $16 \times 16$.

4.
 Pro která $a,b \in \mathbb{R}$ je matice 

$$
\begin{pmatrix} 
a+b & b-a \\
a-b&a+b
\end{pmatrix} 
$$
Ortogonalni.

Podminky:
1) $A+B \neq A-B \neq B-A$
To pak znamena ze $A=B=0$, ale nulova matice neni ortognalni.
2) $\sqrt{ ((a+b)^2 + (a-b)^2}=1$  a $\sqrt{ (b-a)^2 +(a+b)^2 }=1$

Ale jelikoz:
$$
\sqrt{ (a+b)^2 + (a-b)^2} = \sqrt{ (b-a)^2 +(a+b)^2 }
$$
Tak podminku muzeme prepsat:
$$
\sqrt{ a^2 + 2ab + b^2 +a^2 -2ab +b^2}=1
$$

$$
\sqrt{ 2a^2 +2b^2 }=1
$$
$$
\sqrt{ a^2+b^2 }=\frac{\sqrt{ 2 }}{2}
$$
$$
a^2+b^2=\frac{1}{2}
$$

Toto plati kvuli podmince vektoru, ortogonalni matice, být ortonormalni 
3) Dle $A^TA=I$:
Prvni řádek první sloupec.
$(a+b)(a+b)+(a−b)(a−b)=(a+b)2+(a−b)2=2a2+2b$
Prvni řádek, druhý sloupec:
$(a+b)(b−a)+(a−b)(a+b)=(a+b)(b−a+a−b)=(a+b)(0)=0$
Druhy radek, prvni sloupec. Stejne jako prvni radek, druhy sloupec.
Druhý řádek, druhý sloupec:

$(b−a)2+(a+b)2=(a−b)2+(a+b)2=2a^2+2b^2$

Takže:

$A^TA= \begin{pmatrix} 2a^2 + 2b^2 & 0 \\ 0 & 2a^2 + 2b^2 \end{pmatrix}$


To jsou všechny podmínky, které $a,b$ musí splnit, aby zadaná matice byla ortogonální. 

---
5) 
Najděte matici projekce do:

$(a) U=span\{(2,1,1)^T\}$

Projekční matice do směru vektoru $u$ (do přímky) je:

$P= \frac{u u^T}{u^T u}$​

Spočítáme $P$:
$$
u^Tu=2^2+1+1=6
$$
$$
uu^T= \begin{pmatrix} 2  \\1\\1
\end{pmatrix}\cdot ( 2\quad 1\quad 1)= \begin{pmatrix} 
4 & 2 & 2 \\
2 & 1 & 1  \\
2 &1 &1
\end{pmatrix}
$$

Tedy:
$$
P=\frac{1}{6}\cdot \begin{pmatrix} 
4 & 2 & 2 \\
2 & 1 & 1  \\
2 &1 &1
\end{pmatrix}
$$


b)

$$
V = span\{ \begin{pmatrix}
1 \\
1 \\
1
\end{pmatrix}, \begin{pmatrix} 1 \\
0 \\
-1\end{pmatrix}, \begin{pmatrix}
0 \\
0 \\
-1
\end{pmatrix}   \}
$$

Vyrobime matici:
$$A=
\begin{pmatrix}
1 & 1 & 0 \\
1 & 0 & 0 \\
1 & -1 & 1
\end{pmatrix}
$$
Vidime, ze matice je regularni. 
Tedy pokrývá celou dymenzi $\mathbb{R}^3$.
Tedy:
$$
P = I 
$$
---

6)
Buď  
$$
A= \begin{pmatrix}
1 & 2 & 5 \\
7 & 14 & 35 \\
-3 & -6 & -15
\end{pmatrix}
$$
Najděte její ortogonální doplněk a kernel.

Kernel:
$$
\begin{pmatrix}
1 & 2 & 5 \\
7 & 14 & 35 \\
-3 & -6 & -15
\end{pmatrix} \approx \begin{pmatrix}
1 & 2 & 5 \\
1 & 2 & 5 \\
1 & 2 & 5
\end{pmatrix}\approx
\begin{pmatrix}
1 & 2 & 5 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{pmatrix}
$$
Z toho:
$$
x=-5z-2y
$$

Tedy kernel je :
$$
Ker(A)=span\{ (-2,1,0)^T,(-5,0,1)^T  \}
$$
A ortogonální doplněk je  roven $R(A)$.
Tedy:
$$
doplnek= span\{(1,2,5)^T\}
$$


7) 

(a) $U = \{(1, 0, 1, 1)^T, (1, 1, 1, 0)^T\}$

Potřebujeme najít všechny vektory, které jsou kolmé na oba vektory z množiny $U$.

Pro vektor $v_1 = (1, 0, 1, 1)^T$ musí platit:
$$x_1 \cdot 1 + x_2 \cdot 0 + x_3 \cdot 1 + x_4 \cdot 1 = 0$$
$$\Rightarrow x_1 + x_3 + x_4 = 0$$

Pro vektor $v_2 = (1, 1, 1, 0)^T$ musí platit:
$$x_1 \cdot 1 + x_2 \cdot 1 + x_3 \cdot 1 + x_4 \cdot 0 = 0$$
$$\Rightarrow x_1 + x_2 + x_3 = 0$$

Máme tedy soustavu rovnic:
$$\begin{cases}
x_1 + x_3 + x_4 = 0 \\
x_1 + x_2 + x_3 = 0
\end{cases}$$

Z druhé rovnice vyjádříme $x_1 = -x_2 - x_3$ a dosadíme do první:
$$(-x_2 - x_3) + x_3 + x_4 = 0$$
$$-x_2 + x_4 = 0$$
$$x_2 = x_4$$


Tedy:
$$\begin{cases}
x_1 = -x_2 - x_3 \\
x_2 = x_4
\end{cases}$$

Můžeme zvolit $x_2$ a $x_3$ jako volné parametry a vyjádřit ostatní:

Základní vektory ortogonálního doplňku jsou tedy:
- Pro $x_2 = 1, x_3 = 0$: $v_1 = (-1, 1, 0, 1)^T$
- Pro $x_2 = 0, x_3 = 1$: $v_2 = (-1, 0, 1, 0)^T$

Ortogonální doplněk je tedy:
$$U^{\perp} = \text{span}\{(-1, 1, 0, 1)^T, (-1, 0, 1, 0)^T\}$$

b) $V = \{x \in \mathbb{R}^3 : x_1 + x_2 + 2x_3 = 0\}$

Množina $V$ je definována podmínkou $x_1 + x_2 + 2x_3 = 0$, kde $x \in \mathbb{R}^3$.

Tato podmínka představuje lineární rovnici, která definuje rovinu procházející počátkem souřadnic v prostoru $\mathbb{R}^3$. Množina $V$ je tedy dvourozměrný podprostor (rovina) v $\mathbb{R}^3$.
$V$ je dvourozměrná, protože podprostor $V$ je určen jednou lineární rovnicí v prostoru $\mathbb{R}^3.$


Hledáme normálový vektor na tuto rovinu

Normálový vektor k rovině $x_1 + x_2 + 2x_3 = 0$ přímo odečteme z koeficientů rovnice:

Pro rovinu $ax_1 + bx_2 + cx_3 + d = 0$ je normálový vektor $n = (a, b, c)^T$

V našem případě $a = 1$, $b = 1$, $c = 2$, tedy $n = (1, 1, 2)^T$.
Normálový vektor roviny $V$ je  tedy $n = (1, 1, 2)^T$.

Proto ortogonální doplněk $V$ je přímka generovaná vektorem $(1, 1, 2)^T$:

$$V^{\perp} = \text{span}\{(1, 1, 2)^T\}$$






