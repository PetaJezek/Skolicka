1. Let $A \in \mathbb{R}^{n \times n}$. Decide whether $\{ x \in \mathbb{R}^n \mid Ax = 0 \}$ forms a subspace of $\mathbb{R}^n$.

All possible "solutions" to matrix $A$ make a set (we will be calling $S$), which is a subset of $\mathbb{R}^n$,  because $x \in \mathbb{R}^n$. 
Let's check if $S$ is closed under the operations of the vector space $\mathbb{R}^n$.  
- i)**Addition** , $\forall x \in S, \forall y \in S: x +y \in S$

If $x \in S$, then $Ax = 0$. For the statement to be true, we have $x,y \in \mathbb{R}^n: Ax = Ay= 0$.  We are trying to prove that $x+y \in S$. This means $A(x+y) = 0$. We can rewrite this as $Ax + Ay = 0$. Because we $x$ and $y$ are elements of $S$, that means that $Ax = 0$ and $Ay = 0$ and that means this subspaces is closed under addition.

- ii)**Multiplication by a scalar from a field** 

Field we will be working with is $\mathbb{R}$. We have to prove that:
$$
x \in S, t \in \mathbb{R}: t\cdot x \in S
$$
As before, if $x\in S$, then $Ax = 0$.
We need to prove that $A(tx) = 0$. We can rewrite because of commutativity like this $t(Ax)=0$. Since $Ax = 0$: $t \cdot 0 = 0$. That means this statement is true.

Because we proved both conditions, $\{ x \in \mathbb{R}^n \mid Ax = 0 \}$ **forms a subspace of $\mathbb{R}^n$**.

2. Determine whether the following form a subspace of $\mathbb{R}^2$:
- (a) ${ (s, s^2)^T : s \in \mathbb{R} }$
- (b) ${ (s, t)^T \in \mathbb{R}^2 : |s| = |t| }$



3. Decide whether $U = V$ for:
$$
U=span\{{(1,2,0)^T,(0,1,−1)^T}\},V=span\{{(2,1,3)^T,(−1,0,−2)^T}\}.
$$
4. Let $M = {a, b, c, d, e}$ and consider the vector space $2^M$, i.e., the space of all subsets of $M$ over the field $\mathbb{Z}_2$, where addition is understood as exclusive disjunction (XOR) and scalar multiplication follows naturally: $1 \cdot x = x$, $0 \cdot x$ is the zero vector.(
a) Find the zero vector.
b) Find $-v$ for $v = {a, b, c}$.
c) Evaluate the linear combination $u + v - w - z$, where:
$$
u = \{a, d\} , v = \{b, e\} , w = \{c, e\} , z = \{a, b, c\}.
$$

5. Let $u, v, w$ be linearly independent vectors from the space $V$ over $\mathbb{R}$. Determine whether the following sets of vectors are linearly independent:
a) ${u, v + w}$
b) ${0, u, v}$
c) ${u + v, u - v, u + w, u - w}$
d) ${u - v, 2v + w, -u - v - 3w}$


6. Show that the vectors $v_1, \dots, v_n \in V$ are linearly independent if and only if the vectors $v_1, v_1 + v_2, v_1 + v_2 + v_3, \dots, \sum_{i=1}^n v_i$ are linearly independent.