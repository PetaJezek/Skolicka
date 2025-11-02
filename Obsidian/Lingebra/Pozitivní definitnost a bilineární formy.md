## Úloha 1 (10 bodů): Pozitivní semidefinitnost matice A

**Zadání:** Ukažte 3 způsoby, že $A = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ je pozitivně semidefinitní.

### Způsob 1: Definice pomocí kvadratické formy

Matice je pozitivně semidefinitní, pokud pro všechny $\mathbf{x} \in \mathbb{R}^2$ platí $\mathbf{x}^T A \mathbf{x} \geq 0$.

Pro $\mathbf{x} = \begin{pmatrix} x_1 \\ x_2 \end{pmatrix}$ vypočítáme:

$$\mathbf{x}^T A \mathbf{x} = \begin{pmatrix} x_1 & x_2 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix}$$

$$= \begin{pmatrix} x_1 & x_2 \end{pmatrix} \begin{pmatrix} x_1 + x_2 \\ x_1 + x_2 \end{pmatrix} = x_1(x_1 + x_2) + x_2(x_1 + x_2)$$

$$= (x_1 + x_2)^2 \geq 0$$

Protože čtverec reálného čísla je vždy nezáporný, je $A$ pozitivně semidefinitní.

### Způsob 2: Vlastní čísla

Vypočítáme vlastní čísla matice $A$:

Charakteristický polynom: $\det(A - \lambda I) = \det\begin{pmatrix} 1-\lambda & 1 \\ 1 & 1-\lambda \end{pmatrix}$

$$= (1-\lambda)^2 - 1 = \lambda^2 - 2\lambda + 1 - 1 = \lambda^2 - 2\lambda = \lambda(\lambda - 2)$$

Vlastní čísla jsou $\lambda_1 = 0$ a $\lambda_2 = 2$.

Protože všechna vlastní čísla jsou nezáporná ($0 \geq 0$ a $2 > 0$), je matice $A$ pozitivně semidefinitní.

### Způsob 3: Rozklad $A = B^T B$

Hledáme matici $B$ takovou, že $A = B^T B$. Zkusíme $B = \begin{pmatrix} 1 & 1 \end{pmatrix}$ (řádkový vektor).

Ověříme: $B^T B = \begin{pmatrix} 1 \\ 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} = A$

Pro libovolné $\mathbf{x}$ pak:
$$\mathbf{x}^T A \mathbf{x} = \mathbf{x}^T (B^T B) \mathbf{x} = (B\mathbf{x})^T (B\mathbf{x}) = \|B\mathbf{x}\|^2 \geq 0$$

Takže $A$ je pozitivně semidefinitní.

---

## Úloha 2 (6 bodů): Určení parametru pro pozitivní definitnost

**Zadání:** Určete, pro které $a$ je matice $A = \begin{pmatrix} a & 1 & 0 \\ 1 & a & 1 \\ 0 & 1 & a \end{pmatrix}$ pozitivně definitní.

### Řešení pomocí vlastních čísel

Pro pozitivní definitnost musí být všechna vlastní čísla kladná. Vypočítáme charakteristický polynom:

$$\det(A - \lambda I) = \det\begin{pmatrix} a-\lambda & 1 & 0 \\ 1 & a-\lambda & 1 \\ 0 & 1 & a-\lambda \end{pmatrix}$$

Rozložíme podle první řady:
$$= (a-\lambda) \det\begin{pmatrix} a-\lambda & 1 \\ 1 & a-\lambda \end{pmatrix} - 1 \cdot \det\begin{pmatrix} 1 & 1 \\ 0 & a-\lambda \end{pmatrix}$$

$$= (a-\lambda)[(a-\lambda)^2 - 1] - 1 \cdot (a-\lambda)$$

$$= (a-\lambda)[(a-\lambda)^2 - 1 - 1] = (a-\lambda)[(a-\lambda)^2 - 2]$$

$$= (a-\lambda)[(a-\lambda) - \sqrt{2}][(a-\lambda) + \sqrt{2}]$$

Vlastní čísla jsou: $\lambda_1 = a$, $\lambda_2 = a - \sqrt{2}$, $\lambda_3 = a + \sqrt{2}$

### Podmínka pozitivní definitnosti

Pro pozitivní definitnost musí být všechna vlastní čísla kladná:
- $\lambda_1 = a > 0$
- $\lambda_2 = a - \sqrt{2} > 0 \Rightarrow a > \sqrt{2}$  
- $\lambda_3 = a + \sqrt{2} > 0$ (toto je automaticky splněno když $a > \sqrt{2}$)

**Odpověď:** Matice je pozitivně definitní pro $a > \sqrt{2}$.

---

## Úloha 3 (7 bodů): Choleského rozklad

**Zadání:** Najděte Choleského rozklad matice $A = \begin{pmatrix} I_n & I_n \\ I_n & 5I_n \end{pmatrix}$.

### Ověření pozitivní definitnosti

Nejprve ověříme, že matice je pozitivně definitní. Pro blokovou matici:

$$\mathbf{x}^T A \mathbf{x} = \begin{pmatrix} \mathbf{u}^T & \mathbf{v}^T \end{pmatrix} \begin{pmatrix} I_n & I_n \\ I_n & 5I_n \end{pmatrix} \begin{pmatrix} \mathbf{u} \\ \mathbf{v} \end{pmatrix}$$

$$= \mathbf{u}^T\mathbf{u} + \mathbf{u}^T\mathbf{v} + \mathbf{v}^T\mathbf{u} + 5\mathbf{v}^T\mathbf{v} = \|\mathbf{u}\|^2 + 2\mathbf{u}^T\mathbf{v} + 5\|\mathbf{v}\|^2$$

Doplníme na úplný čtverec:
$$= \|\mathbf{u} + \mathbf{v}\|^2 + 4\|\mathbf{v}\|^2 \geq 0$$

Matice je tedy pozitivně definitní.

### Choleského rozklad

Hledáme dolní trojúhelníkovou matici $L = \begin{pmatrix} X & 0 \\ L_{21} & L_{22} \end{pmatrix}$ tak, že $A = LL^T$.

Z rovnice $A = LL^T$:

$$\begin{pmatrix} I_n & I_n \\ I_n & 5I_n \end{pmatrix} = \begin{pmatrix} X & 0 \\ Y & Z \end{pmatrix} \begin{pmatrix} X^T & Y^T \\ 0 & Z^T \end{pmatrix}$$

$$= \begin{pmatrix} XX^T & XY^T \\ ZX^T & YY^T + ZZ^T \end{pmatrix}$$

Porovnáním bloků:
1. $XX^{t} = I_n \Rightarrow X = I_n$ (volíme pozitivní)
2. $XY^T = I_n  \quad Y^T = I_n \Rightarrow Y = I_n$
3. $YY^T + ZZ^T = 5I_n \Rightarrow I_n + ZZ^T = 5I_n \Rightarrow ZZ^T = 4I_n$

Z posledního získáváme $Z = 2I_n$.

**Choleského rozklad:**
$$L = \begin{pmatrix} I_n & 0 \\ I_n & 2I_n \end{pmatrix}$$


---

## Úloha 4 (4 body): Vlastnost bilineární formy

**Zadání:** Ukažte, že pro každou bilineární formu $b$ platí $b(u, 0) = b(0, u) = 0$.

### Důkaz

Bilineární forma $b: V \times V \to \mathbb{F}$ musí splňovat lineárnost v obou argumentech.

**Lineárnost v prvním argumentu:**
Pro všechna $u, v_1, v_2 \in V$ a $\alpha, \beta \in \mathbb{F}$:
$$b(\alpha u_1 + \beta u_2, v) = \alpha b(u_1, v) + \beta b(u_2, v)$$

**Lineárnost v druhém argumentu:**
Pro všechna $u, v_1, v_2 \in V$ a $\alpha, \beta \in \mathbb{F}$:
$$b(u, \alpha v_1 + \beta v_2) = \alpha b(u, v_1) + \beta b(u, v_2)$$

### Důkaz první části: $b(u, 0) = 0$

Použijeme lineárnost v druhém argumentu. Víme, že $0 = 0 \cdot v$ pro libovolné $v \in V$:

$$b(u, 0) = b(u, 0 \cdot v) = 0 \cdot b(u, v) = 0$$

### Důkaz druhé části: $b(0, u) = 0$

Analogicky, pomocí linearity v prvním argumentu. Víme, že $0 = 0 \cdot w$ pro libovolné $w \in V$:

$$b(0, u) = b(0 \cdot w, u) = 0 \cdot b(w, u) = 0$$

**Závěr:** Pro každou bilineární formu $b$ platí $b(u, 0) = b(0, u) = 0$ pro všechna $u \in V$.

---

## Úloha 5 (8 bodů): Klasifikace bilineárních forem

Nechť $x, y \in \mathbb{R}^n$ jsou sloupcové vektory a $C \in \mathbb{R}^{n \times n}$ je reálná matice.

Mějme funkci:

$$
b(x, y) = x_1^2 + y_2^2 + 2x_2y_1
$$

Zapišme $x = \begin{pmatrix} x_1 \\ x_2 \end{pmatrix}, \quad y = \begin{pmatrix} y_1 \\ y_2 \end{pmatrix}$

Zkusíme najít matici $C$ tak, aby:

$$
x^\top C y = x_1^2 + y_2^2 + 2x_2y_1
$$

Ale každý člen musí být součinem nějakého $x_i y_j$:

$$
x^\top C y = c_{11}x_1y_1 + c_{12}x_1y_2 + c_{21}x_2y_1 + c_{22}x_2y_2
$$

Z toho plyne, že v **žádném případě** se nemůže objevit člen jako $x_1^2$ nebo $y_2^2$, protože:
- $x_1^2$ nemá žádné $y_j$,
- $y_2^2$ nemá žádné $x_i$.

 **Závěr:** Neexistuje matice $C$, která by splňovala $x^\top C y = x_1^2 + y_2^2 + 2x_2y_1$. Tedy to **není bilineární forma**.



b)
Výraz:

$$
c(x, y) = x_1y_1 + 2x_1y_2 - x_1y_2 + y_1y_2 = x_1y_1 + x_1y_2 + y_1y_2
$$

Zapišme vektorově: $x = \begin{pmatrix} x_1 \\ x_2 \end{pmatrix}, \quad y = \begin{pmatrix} y_1 \\ y_2 \end{pmatrix}$

Zkusíme najít matici $C$ tak, že $x^\top C y = c(x, y)$

$$
x^\top C y = c_{11}x_1y_1 + c_{12}x_1y_2 + c_{21}x_2y_1 + c_{22}x_2y_2
$$

Chceme tedy:

$$
x^\top C y = x_1y_1 + x_1y_2 + y_1y_2
$$

Ale člen $y_1y_2$ zde **nemůže vzniknout**, protože není násobkem žádného $x_i$. Tedy:

- člen $y_1y_2$ nelze napsat jako $x^\top C y$,
- celý výraz **není bilineární forma**.

 **Závěr:** Ani v tomto případě neexistuje matice $C$, pro kterou $x^\top C y = c(x, y)$. Tedy výraz **není bilineární forma**.
