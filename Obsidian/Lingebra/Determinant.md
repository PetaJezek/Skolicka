# Determinant (34 bodů)

**Deadline:** 17. března 2025

## 1. (10 bodů) Spočítejte determinanty:

- a) (1 bod) $\det(-4)$  

Determinant skaláru je daný skalár: $\det(-4)=-4$

- b) (1 bod) $\det(-I_n)$  

$-I_n$ je horní trojúhelníková matice, takže její determinant je roven násobku prvků na hlavní diagonále. Tedy v našem případě $\det(-I_n) = (-1)^n$ 



- c) (2 body)  
$$
\begin{vmatrix}
2 & 4 & 1 \\
3 & 2 & 1 \\
2 & 3 & 2
\end{vmatrix} = 8 + 9 +8 - 4 -6 -24 = -9
$$


- d) (2 body)  
$$
\begin{vmatrix}
0 & a & 0 \\
0 & 0 & b \\
c & 0 & 0
\end{vmatrix} = abc
$$


e) (4 body)  

$$
\begin{vmatrix}
0 & \cdots & 0 & 1 \\
\vdots & \ddots & 1 & 0 \\
0 & 1 & \ddots & \vdots \\
1 & 0 & \cdots & 0
\end{vmatrix}
$$

Na vedlejsi diagonále jsou jedničky a zbytek 0.  Jediná možná permutace, které vráti jiné číslo než nulu, je permutace kdy vybíráme prvky z antidiagonály. Parita permutace a tedy i její znaménko (buď $1$ nebo $-1$) záleží na velikosti dané matice. Pro sudý počet prvků na diagonále máme sudý počet inverzí permutace a znaménko je +. Tedy determinant této matice $A^{n\times n}$ je $\pm 1$ v závislosti na $n$.





---

## 2. (8 bodů) 

Buď $A \in \mathbb{R}^{m \times m}$ a $B \in \mathbb{R}^{n \times n}$. Dokažte, že  

$$
\det \begin{pmatrix} A & 0 \\ 0 & B \end{pmatrix} = \det(A) \det(B).
$$

Matici na levé straně budu označovat $AB_{0} \in \mathbb{R}^{m+n \times m+n}$. 

Při výpočtu determinantu $AB_0$​ bude příspěvek permutace vždy nulový, pokud v prvních $m$ řádcích vybereme alespoň jeden prvek na indexu $i$, kde $i>m$.  To znamená, že pro permutaci, kde prvky $p_{1},..,p_{m} \in A$, můžeme zvolit všechny permutace "matice B". Takže fixní permutaci matice A násobíme všemi permutacemi matice B. Což se rovná $p_{1} \cdot p_{2} \cdot  \dots p_{m} * \det(B)$. To stejné můžeme udělat pro fixní permutaci matice B. Tedy vlastně výsledek je součet násobků všech permutací matice A se všemi permutacemi matice B. (každou permutaci A násobíme všemi permutacemi B a naopak). Výsledky těchto permutací se rovnají $\det(A)$ resp. $\det(B)$. Tedy výsledek  je
$$
\det \begin{pmatrix} A & 0 \\ 0 & B \end{pmatrix} = \det(A) \det(B). 
$$


---

## 3. (16 bodů) 

Říkáme, že celočíselná matice $M \in \mathbb{Z}^{m \times n}$ je **totálně unimodulární** (dále již jen TU), pokud je každý její minor (tzn. determinant čtvercové podmatice) roven $-1, 0,$ či $1$.

Buď $A \in \mathbb{Z}^{n \times n}$ regulární. Dokažte, že je-li $A$ TU, pak nutně i $A^{-1}$ je TU.

*(Zkuste si vedle celočíselnosti dokázat pro začátek alespoň to, že hodnoty determinantů podmatic o rozměrech $1 \times 1$ a $n \times n$ jsou správné. Obecné podmatice jsou potom těžší.)*

*(Při dokazování, že minor je roven $-1,0,1$, tu nemusíte příliš řešit znaménko, ať neskončíte zavalení zbytečnými detaily. Klidně v průběhu pište $\pm$ něco, stejně musíte dokázat primárně to, že to něco je ve výsledku 0 nebo 1.)*


Determinant $A^{-1}$ musí být z množiny celých čísel, protože násobení, sčítání a odčítaní nad celými čísly vždy vrací celé číslo. A jelikož $A \in \mathbb{Z}^{n \times n}$  implikuje $A^{-1} \in \mathbb{Z}^{n \times n}$.  To znamená:$\forall a_{i,j} \in A: a_{i,j} \in \{\pm 1, 0\}$.

Pokud je $A$ TU, znamená to, že každá její podmatice je také TU. Tedy každá podmatice má minory rovné $1,0,-1$. To znamená, že i nejmenší čtercové podmatic0e jsou rovny $1,0,-1$. Tyto podmatice mají velikost $1\times 1$, tedy jednotlivé prvky. Tyto prvky z A jsou také v $A^{-1}$, takže  je-li $A$ TU, pak nutně i jednotlivé prvky (matice $1 \times 1$) $A^{-1}$ jsou TU.

Dle tvrzení z přednášky platí 
$$
A \in \mathbb{T}^{n \times n} \implies  \det(A) = \det(A^t)
$$

Tedy pokud je $A$ TU pak $\det(A) \in \{\pm 1, 0\} \implies \det(A^t) \in \{\pm 1, 0\}$.

Bohužel nemám tušení, jak dokázat tvrzení pro obecné matice. Tipnul bych si, že se využije Cramerovo pravidlo s nějakým trikem. Bohužel to v tom nevidím.