1. (6 bodů) Rozhodněte, zda si jsou podobné matice

$$
A = \begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
1 & 1 & 1
\end{pmatrix}, \quad
B = \begin{pmatrix}
-1 & 0 & 1 \\
1 & 0 & 0 \\
-1 & 0 & 2
\end{pmatrix}.
$$

Matice $A$ a $B$ jsou podobne, pokud existuje regularni $S \in \mathbb{R}^{3\times3}$ tak, ze:
$$
A=SBS^{-1}
$$
Z toho plyne veta o vlastnich cisel podobnych matic, ktera rika, ze podobone matice maji stejna vlastni cisla.
Ty tedy zjistime pomoci charakteristickeho polynomu danych matic.

$$
p_{A}(\lambda)=\det(A-\lambda I_{3}) = (1-\lambda)^{3} 
$$
$$
(1-\lambda)^{3} =0
$$
$$
\lambda_{A} = 1: \text{ s geometrickou nasobnosti 3}
$$

Druha matice:
$$
p_{B}(\lambda)= \det(B-\lambda I_{3}) = (-1-\lambda)\cdot (-\lambda) \cdot(2-\lambda) - (\lambda) = (\lambda + \lambda^2)\cdot(2-\lambda)-\lambda
$$
$$
=-\lambda^{3}+\lambda^{2}+\lambda = -\lambda(\lambda^{2}-\lambda-1) 
$$
To se musi rovnat nule:
$$
\lambda_{1}=0
$$
$$
\lambda_{2,3}=\frac{1\pm \sqrt{ 1+4 }}{2} =\frac{1\pm \sqrt{ 5}}{2}
$$
Jelikoz se vlastni cisla nerovnaji, a ani charakteristicke polynomy, matice $A$ a $B$ **nejsou podobne**.

---

2. (4 body) Buď $C \in \mathbb{R}^{n \times n}$ a $D \in \mathbb{R}^{m \times m}$. Ukažte, že

$$
A =\begin{pmatrix}
C & 0 \\
0 & D
\end{pmatrix}
\text{ je podobná: }
B =\begin{pmatrix}
D & 0 \\
0 & C
\end{pmatrix}.
$$

Matice $A$ a $B$ jsou podobne, pokud existuje regularni $S \in \mathbb{R}^{(n+m)\times (n+m)}$ tak, ze:
$$
A=SBS^{-1}
$$

(Pouziti matice s jednickama na vedlejsi diagonale, je napad prevzan z ucebnice Priklad 10.26)

Vidime, ze rozdil mezi temito maticemi je otoceni kolem vedlejsi diagonaly. To muzeme docilit tak, ze nejdrive prohodime sloupce a pak radky. Sloupce matice $A$ prohodime nasobenim z prava permutacni matici , ktera ma na vedlejsi diagonale same jednicky (ozn. $Q^{(n+m)\times(n+m)}$):

$$
AQ=\begin{pmatrix}
C & 0 \\
0 & D
\end{pmatrix}
\begin{pmatrix}
0 & I_{n} \\
I_{m} & 0
\end{pmatrix} = \begin{pmatrix}
0 & C \\
D & 0
\end{pmatrix} 
$$

A ted matici $AQ$ vynasobime z leva matici $Q^{t}$, abychom prohodili radky:
$$
\begin{pmatrix}
0 & I_{m} \\
I_{n} & 0
\end{pmatrix}
\begin{pmatrix}
0 & C \\
D & 0
\end{pmatrix}
= \begin{pmatrix}
D & 0 \\
0 & C
\end{pmatrix} = Q^{t}AQ = B
$$

Protoze $Q$ je ortogonalni matice plati:

$$
Q^{t}=Q^{-1}
$$

A proto:
$$
B=Q^{t}AQ=Q^{-1}AQ 
$$
Pokud $S = Q^{-1}$ pak:
$$
B=SAS^{-1}
$$

Matice $A$ a $B$ jsou tedy podobne.

---
3. (4 body) Najděte všechny matice podobné matici $I_n$.


Hledana matice $A$ musi splnovat:
$$
S = SA; \quad \text{Pro } S\in \mathbb{R}^{n\times n}
$$

Protoze vychazime ze vztahu o podobnosti. Matice $A$ a $B$ jsou podobne pokud:
$$
BS = SA
$$
Pokud $B=I$:
$$
S=SA
$$
$$
A=I
$$

Tedy jedina matice podobna jednotkova matici je ona sama.

---

4. (8 bodů) Diagonalizujte, nebo ukažte, že není možné diagonalizovat matice

- (a) (3 body)

$$
E = \begin{pmatrix}
1 & 2 \\
0 & 2
\end{pmatrix}
$$

Chceme:
$$
E=PDP^{-1}
$$
Najdeme vlastni cisla:

$$
p_{E}(\lambda)=\det(E-\lambda I) = (1-\lambda)(2-\lambda) \implies \lambda_{1}=1; \lambda_{2}=2
$$

Nyni najdeme vlastni vektory pro jednotliva vl. cisla:
$$
(E-I_{2})\vec{v}=0 \implies\begin{pmatrix}
0 & 2 \\
0 & 1
\end{pmatrix} \vec{v} =0 \implies  \vec{v}=
\begin{pmatrix}
x  \\
0
\end{pmatrix}, \text{kde } x \in \mathbb{R}
$$


$$
(E-2I_{2})\vec{u}=0 \implies\begin{pmatrix}
-1 & 2 \\
0 & 0
\end{pmatrix} \vec{u} =0 \implies  2u_{1}=u_{2} \implies  \vec{u} = 
\begin{pmatrix}
2y  \\
y
\end{pmatrix}, \text{ kde } y \in \mathbb{R}
$$

Pak 
$$
D=\begin{pmatrix} 
1 & 0 \\
0 & 2
\end{pmatrix}
$$

A 
$$
P=\begin{pmatrix}
x & 2y \\
0 & y
\end{pmatrix}
$$

$$
P^{-1} = \begin{bmatrix}
x & 2y  & \vert & 1 & 0\\
0 & y & \vert & 0 & 1
\end{bmatrix}=
 \begin{bmatrix}
x & 0  & \vert & 1 & -2\\
0 & y & \vert & 0 & 1
\end{bmatrix}=
\begin{bmatrix}
1 & 0  & \vert & \frac{1}{x} & -\frac{2}{x}\\
0 & 1 & \vert & 0 & \frac{1}{y}
\end{bmatrix}\implies
$$
$$
P^{-1}= \begin{pmatrix}
\frac{1}{x} & -\frac{2}{x} \\
0 & \frac{1}{y} \\
\end{pmatrix}
$$

Tedy:
$$
E =PDP^{-1}
$$

$$
\begin{pmatrix}
1 & 2 \\
0 & 2
\end{pmatrix} = \begin{pmatrix}
x & 2y \\
0 & y
\end{pmatrix} \cdot \begin{pmatrix} 
1 & 0 \\
0 & 2
\end{pmatrix} \cdot \begin{pmatrix}
\frac{1}{x} & -\frac{2}{x} \\
0 & \frac{1}{y} \\
\end{pmatrix}
$$
- (b) (5 bodů)

$$
F = \begin{pmatrix}
1 & -1 & 0 \\
8 & -2 & 6 \\
1 & 1 & 2
\end{pmatrix}
$$

Chceme:
$$
F = P^{-1}DP
$$

Najdeme vlastni cisla:

$$
p_{F}(\lambda)= (1-\lambda)(-2-\lambda)(2-\lambda)-6-6+6\lambda - 8\lambda + 16 = (1-\lambda)(-4+\lambda^{2}) -2\lambda+4 = 
$$
$$
=-\lambda^{3}+\lambda^{2}+4\lambda-4-2\lambda+4 = -\lambda^{3} + \lambda^{2} +2\lambda= -\lambda(\lambda^{2}-\lambda-2)=-\lambda(\lambda-2)(\lambda+1)
$$

Vlastni cisla jsou:
$$
\lambda_{1}=0;\lambda_{2}=2;\lambda_{3}=-1
$$
Pak tedy:

$$
D = \begin{pmatrix}
2 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & -1
\end{pmatrix}
$$

Najdeme vlastni vektory:
$$
F\vec{v_{1}}=0 
$$
Vyresime pomoci gausovky:
$$
\begin{pmatrix}
1 & -1 & 0 \\
0 & 6 & 6 \\
0 & 2 & 2 
\end{pmatrix}=
\begin{pmatrix}
1 & 0 & 1 \\
0 & 1 & 1  \\
0 & 0 & 0
\end{pmatrix}
$$
Plati $v_{1}=-v_{3}=v_{2}$

Proto:
$$
\vec{v}_{1}=\begin{pmatrix}
x \\
x \\
-x
\end{pmatrix}, \text{ pro } x \in \mathbb{R}
$$

$$
(F-2I)\vec{v}=0 \implies \begin{pmatrix}
1 & 1 & 0 \\
8 & -4 & 6 \\
1 & 1 & 0
\end{pmatrix}\vec{v} =0 \implies\begin{pmatrix}
1 & 1 & 0 \\
0 & -2 & 1 \\
0 & 0 & 0
\end{pmatrix}\vec{v} =0
$$

Plati $v_{3}=2v_{2}=-2v_{1}$
Proto:
$$
\vec{v}_{2}=\begin{pmatrix}
-y \\
y\\
2y
\end{pmatrix} , \text{pro } y \in \mathbb{R}.
$$
Posledni vektor
$$
(F+I)\vec{v}_{3}=0 \implies \begin{pmatrix}
2 & -1 & 0 \\
8 & -1 & 6 \\
1 & 1 & 3
\end{pmatrix} \vec{v}_{3}=0 \implies \begin{pmatrix}
1 & 1 & 3 \\
0 & -9 & -18 \\
0 & -3 & -6
\end{pmatrix}\vec{v}_{3}=0\implies 
$$
$$
\begin{pmatrix}
1 & 0 & 1 \\
0 & 1 & 2 \\
0 & 0 & 0
\end{pmatrix} \vec{v}_{3}=0
$$
Plati: $-v_{1}=v_{3}=-2v_{2}$

Proto:
$$
\vec{v}_{3}=\begin{pmatrix}
-z \\
-2z \\
z
\end{pmatrix} \text{pro} z \in \mathbb{R}
$$

$$
P=\begin{pmatrix}
x & -y & -z \\
x & y & -2z \\
-x & 2y & z
\end{pmatrix}
$$

Invertujeme:
$$
P^{-1}=\begin{pmatrix}
x & -y & -z & \vert  &  1 & 0 & 0\\
x & y & -2z  & \vert  & 0 & 1 & 0\\
-x & 2y & z & \vert &   0 & 0 & 1
\end{pmatrix} = \begin{pmatrix}
x & -y & -z & \vert  &  1 & 0 & 0\\
0 & 2y & -z  & \vert  & -1 & 1 & 0\\
0 & y & 0 & \vert &   1 & 0 & 1
\end{pmatrix}
$$ 
$$
= \begin{pmatrix}
x & -y & -z & \vert  &  1 & 0 & 0\\ 
0 & y & 0 & \vert &   1 & 0 & 1 \\
0 & 2y & -z  & \vert  & -1 & 1 & 0
\end{pmatrix}=
\begin{pmatrix}
x & -y & -z & \vert  &  1 & 0 & 0\\ 
0 & y & 0 & \vert &   1 & 0 & 1 \\
0 & 0 & z  & \vert  & 3 & -1 & 2
\end{pmatrix}=
$$

$$
=
\begin{pmatrix}
x & 0 & 0 & \vert  & 5 & -1 & 3\\ 
0 & y & 0 & \vert &   1 & 0 & 1 \\
0 & 0 & z  & \vert  & 3 & -1 & 2
\end{pmatrix}=
\begin{pmatrix}
1 & 0 & 0 & \vert  & \frac{5}{x} & -\frac{1}{x} & \frac{3}{x}\\ 
0 & 1 & 0 & \vert &   \frac{1}{y} & 0 & \frac{1}{y} \\
0 & 0 & 1  & \vert  & \frac{3}{z} & -\frac{1}{z} & \frac{2}{z}
\end{pmatrix}
$$

$$
P^{-1} = \begin{pmatrix}
 \frac{5}{x} & -\frac{1}{x} & \frac{3}{x}\\ 
\frac{1}{y} & 0 & \frac{1}{y}  \\
\frac{3}{z} & -\frac{1}{z} & \frac{2}{z}
\end{pmatrix}
$$

Pak teda:

$$
F = \begin{pmatrix}
1 & -1 & 0 \\
8 & -2 & 6 \\
1 & 1 & 2
\end{pmatrix} = \begin{pmatrix}
 \frac{5}{x} & -\frac{1}{x} & \frac{3}{x}\\ 
\frac{1}{y} & 0 & \frac{1}{y}  \\
\frac{3}{z} & -\frac{1}{z} & \frac{2}{z}
\end{pmatrix} \cdot \begin{pmatrix}
2 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & -1
\end{pmatrix} \cdot\begin{pmatrix}
x & -y & -z \\
x & y & -2z \\
-x & 2y & z
\end{pmatrix}
$$
5. (4 body) Nechť $A = S\Lambda S^{-1}$ je diagonalizační rozklad matice $A$. Určete vlastní vektory $A^T$.

Transponujeme obe strany:
$$
A^{T} =(S^{T})^{-1} \Lambda S^T
$$
Necht $Q=S^{-T}$, pak:
$$
A^{T}=Q\Lambda Q^{-1}
$$
Tedy dostavame opet diagonalizaci a coz znamena ze $\Lambda$ obsahuje vlastni cisla a $Q$ podle definice obsahuje ve sloupcich vlastni vektory.

Pokud $S^{-T}=Q \implies S^{-1}=Q^T \implies$**vlastni vektory $A^{T}$ jsou radky matice $S^{-1}$**. 

6. (4 body) Buď $p(x)$ libovolný polynom a buďte $A, B \in \mathbb{R}^{n \times n}$, takové že $A \sim B$. Rozhodněte, zda $p(A) \sim p(B)$.

Z predpokladu plati:
$$
A=PBP^{-1}
$$

Co se stane pokud umocnime rovnici?

$$
A^{k}=(PBP^{-1})^{k}
$$
To pripomina zimni semester. Pravou stranu muzeme prepsat:
$$
A^{k}=(PBP^{-1})^{k}= PB^kP^{-1}
$$
To znamena ze matice $A$ a $B$ jsou podobne v jakekoliv mocnine. I kdyz zmenime jejich znamenko:
$$
-IA^{k}=-IPB^kP^{-1}
$$

Tedy pro jakykoliv polynom (kombinaci techto matic) plati:

$$
p(A) = \alpha_{0}I+\alpha_{1}A+\dots \alpha_{n}A^n
$$
$$
p(A) = \alpha_{0}I+\alpha_{1}(PBP^{-1})+\dots+\alpha_{n}(PB^nP^{-1})
$$
$$
p(A) = P(\alpha_{0}I+\alpha_{1}B+\dots+\alpha_{n}B^n)P^{-1} = Pp(B)P^{-1}
$$
$$
p(A) = Pp(B)P^{-1}
$$