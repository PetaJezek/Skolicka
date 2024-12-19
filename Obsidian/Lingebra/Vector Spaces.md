## 1. (20 points) Determine whether the following form a vector space:

(a) $\mathbb{R}^n$ over $\mathbb{C}$,

(b) $\mathbb{R}^\infty$ over $\mathbb{C}$,

(c) the set of positive real numbers $\mathbb{R}^+$ over $\mathbb{R}$ with operations 
$x \oplus y = x \cdot y$ and $\alpha \cdot x = x^\alpha$,

(d) the set of all rotations in space $\mathbb{R}^n$, where addition is defined as composition of rotations and 
$\alpha$-multiplication as a rotation by $\alpha$ times the angle.


a)

We can take a vector $v$ from $\mathbb{R}^n$ and try to multiply it by a scalar $s = a\cdot bi$ from $\mathbb{C}$, the result should be an element in $\mathbb{R}^n$. But an easy example of when that does not happen is when $b\neq 0$. Because then all elements of $v$ will contain the complex components, which is in fact not in $\mathbb{R}^n$. So $\mathbb{R}^n$ is not a vector space over $\mathbb{C}$.

b)

The same thing we have pointed out in the part a) applies here. Even if there are infinite elements in the vectors, none of them can generate vectors with complex components. So $\mathbb{R}^\infty$ is not a vector space over $\mathbb{C}$

c)


A vector space must have a neutral element $\mathbf{0}$ such that:
$$
x \oplus \mathbf{0} = x, \quad \forall x \in \mathbb{R}^+.
$$

For $x \oplus y = x \cdot y$, the neutral element is $1$, because:
$$
x \cdot 1 = x.
$$
A vector space requires every $x \in \mathbb{R}^+$ to have an additive inverse $y \in \mathbb{R}^+$ such that:
$$
x \oplus y = \mathbf{0}.
$$

With $x \oplus y = x \cdot y$ and $\mathbf{0} = 1$, the equation becomes:
$$
x \cdot y = 1.
$$

The solution is:
$$
y = \frac{1}{x}.
$$

Since $\frac{1}{x} \in \mathbb{R}^+$ for all $x > 0$, additive inverses exist.

For $\alpha \in \mathbb{R}$ and $x \in \mathbb{R}^+$, scalar multiplication is defined as:
$$
\alpha \cdot x = x^\alpha.
$$

- Since $x > 0$, $x^\alpha > 0$ for all $\alpha \in \mathbb{R}$, so scalar multiplication always produces an element of $\mathbb{R}^+$.

We check the distributive laws:
$$
\alpha \cdot (x \oplus y) = (\alpha \cdot x) \oplus (\alpha \cdot y).
$$

- Left-hand side:
$$
\alpha \cdot (x \oplus y) = \alpha \cdot (x \cdot y) = (x \cdot y)^\alpha.
$$
- Right-hand side:
$$
(\alpha \cdot x) \oplus (\alpha \cdot y) = (x^\alpha) \cdot (y^\alpha) = (x \cdot y)^\alpha.
$$

This is satisfied.

Distribution:

$$
(\alpha + \beta) \cdot x = (\alpha \cdot x) \oplus (\beta \cdot x).
$$

- Left-hand side:
$$
(\alpha + \beta) \cdot x = x^{\alpha + \beta}.
$$
- Right-hand side:
$$
(\alpha \cdot x) \oplus (\beta \cdot x) = x^\alpha \cdot x^\beta = x^{\alpha + \beta}.
$$

This is satisfied.


### **Conclusion**
All vector space axioms are satisfied under the given operations. Therefore:
$$
(\mathbb{R}^+, \oplus, \cdot)
$$
**is a valid vector space** over $\mathbb{R}$ with these  operations.

---
d) 


#### **Closure under Addition**:
The sum of two rotations, defined by their angle addition, is still a rotation. Therefore, the set of rotations is **closed under addition**.



#### **Additive Identity (Neutral Element)**:
The identity element for addition (composition of rotations) is the rotation by 0 degrees, since a rotation by 0 degrees does not change the orientation of the space.
Therefore, the additive identity is the **rotation by 0 degrees**.



#### **Additive Inverse**:
The inverse of a rotation by $\theta$ is the rotation by $-\theta$, because rotating by $\theta$ and then $-\theta$ results in no rotation (identity rotation).
Thus, each rotation has an **additive inverse**.

#### **Closure under Scalar Multiplication**:
Scalar multiplication of a rotation by a scalar $\alpha$ gives a rotation by$\alpha \cdot \theta$, which is still a valid rotation.
Therefore, the set of rotations is **closed under scalar multiplication**.

---

#### **Distributivity**:
Scalar multiplication satisfies both distributivity over vector addition and scalar addition. 
- For vector addition: $\alpha \cdot (R_\theta \oplus R_\phi) = R_{\alpha \cdot (\theta + \phi)}$.
- For scalar addition: $(\alpha + \beta) \cdot R_\theta = R_{(\alpha + \beta) \cdot \theta} = R_{\alpha \cdot \theta} \oplus R_{\beta \cdot \theta}$.

Thus, **distributivity** holds for scalar multiplication.


Since the set of rotations satisfies all the vector space axioms:  the set of rotations in$\mathbb{R}^n$ **forms a vector space**.

---

## 2. (3 points)

Let $U, V$ be arbitrary vector spaces over a field $T$. Can it happen that $U \cap V = \emptyset$?
If $U, V$ are vector spaces over the same field, both of them have to contain the zero vector. That means that the statement can never be true.


---

## 3. (7 points)

Determine whether the set of upper triangular matrices $\mathbb{R}^{n \times n}$, i.e., matrices $U$ such that $(U)_{ij} = 0$ whenever $i > j$, forms a vector space.


Let $U$ and $V$ be two upper triangular matrices in $\mathbb{R}^{n \times n}$. We need to check whether their sum $U + V$ is also an upper triangular matrix. 

If  $U$ and $V$ are upper triangular, then for any $i > j$, $(U)_{ij} = 0$ and $(V)_{ij} = 0$. - Therefore, for $(U + V)_{ij} = (U)_{ij} + (V)_{ij}$, we get $(U + V)_{ij} = 0 + 0 = 0$ for all $i > j$. Thus, the sum $U + V$ is also upper triangular.

The additive neutral element must be a matrix $0 \in \mathbb{R}^{n \times n}$ such that for any upper triangular matrix $U$, $U + 0 = U$. - The zero matrix is an upper triangular matrix,  and it satisfies $(0)_{ij} = 0$ for all $i, j$. 

For each upper triangular matrix $U$, we need to find an additive inverse $-U$ such that $U + (-U) = 0$. - The matrix $-U$ is formed by negating each entry of $U$. Since negating the entries of an upper triangular matrix gives another upper triangular matrix, $-U$ is also upper triangular. Every matrix has an **additive inverse** in the set. 

Let $\alpha \in \mathbb{R}$. We need to check whether $\alpha \cdot U$ is also an upper triangular matrix.  The matrix $\alpha \cdot U:$ multiplying each entry of $U$ by $\alpha$. 
If $U$ is upper triangular, then $\alpha \cdot U$  has to be an upper triangular matrix too. Elements with positions $i>j$ are still going to be $0$. 


Distributivity and associativity hold because the set of upper triangular matrices behaves like any other matrix space under addition and scalar multiplication.


Since the set of upper triangular matrices satisfies all the vector space axioms, the set of upper triangular matrices in $\mathbb{R}^{n \times n}$ forms a vector space.