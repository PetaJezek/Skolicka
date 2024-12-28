1. Let $A \in \mathbb{R}^{n \times n}$. Decide whether $\{ x \in \mathbb{R}^n \mid Ax = 0 \}$ forms a subspace of $\mathbb{R}^n$.

All possible "solutions" to matrix $A$ make a set (we will be calling $S$), which is a subset of $\mathbb{R}^n$,  because $x \in \mathbb{R}^n$. 

Does $S$ contains the zero vector? If $x=0$ then we get $A 0=0$, which is true. (Zero vector is a solution to all homogeneous matrices).

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

a)
- **Zero vector**
If $s=0$ then we get vector $(0,0)$, which is the zero vector in the space $\mathbb{R}^2$.
- **Closed under addition**
$$
s,t \in \mathbb{R}: (s,s^2)^T + (t,t^2)^T \in \mathbb{R}
$$
Addition of these vectors equals to a vector:$$
(s+t,s^2+t^2)^T
$$

Adding two real numbers gives us another real number. Adding two numbers from $\mathbb{R}_{0}^+$ gives us a number from $\mathbb{R}_{0}^+$. Now we need to check if
$$
(s+t)^2 = s^2+t^2
$$
After expanding the parentheses on the left side we get:
$$
s^2 + 2st + t^2 = s^2 + t^2
$$
This equation is not true for all $s \in \mathbb{R}$. Which means ${ (s, s^2)^T : s \in \mathbb{R} }$ **does not form a subspace over $\mathbb{R}^2$**.

b) ${ (s, t)^T \in \mathbb{R}^2 : |s| = |t| }$

- **Zero vector**
If$(s,t) \in \mathbb{R}^2$ and $|s| = |t|$, we can set $s,t = 0$.
Then our conditions are satisfied: $|0| = |0|$ and $(0,0) \in \mathbb{R}^2$.
So the zero vector is in this subspace.
- **Closed under addition**
$$
(s,t),(u,v) \in\mathbb{R}^2, |s| = |t|,|u| = |v|: (s,t) +(u,v) \in \mathbb{R}^2
$$
The resultant vector will be:
$$
(s+u,t+v)^T
$$
The elements of the vector will be in $\mathbb{R}$, because we are adding two real numbers. What we need to check if:
$$
|s+u| = |t+v| 
$$
We get three situations:
1.
$$
s=t, u=v
$$
2.
$$
s = -t, u=v
$$
3.
$$
s = -t, u= -v
$$
We do not need to check when $s =t, u = -v$ because that is the same as the second situation. We can just change the names of the variables.

1) We can rewrite the equation:
$$
|s+u| =|s+u| 
$$
This is **True.**
2) We can rewrite the equation:
$$
|s+u| = |-s+u| 
$$
If $s=3,u=2$ we get $5 = 1$. So for the second situation, the subset is not closed under addition.

That means${ (s, t)^T \in \mathbb{R}^2 : |s| = |t| }$ **does not form a subspace over $\mathbb{R}^2$**.


3. Decide whether $U = V$ for:
$$
U=span\{{(1,2,0)^T,(0,1,−1)^T}\},V=span\{{(2,1,3)^T,(−1,0,−2)^T}\}.
$$ 

So i think that if we can generate basis of $V$ with basis of $U$, it means that we can generate $V$ from basis of $U$. That means $V\subseteq U$.

If we can then generate basis of $U$ by combination of basis from $V$, we should be able to generate $U$ using basis of $V$. That means $U\subseteq V$. 

If we combine these two inclusions, we get $U=V$.
- $V\subseteq U$
Vector $v_{1} = (2,1,3)^T$.
$$
v_{1}=2u_{1}-3u_{2}
$$
Vector $v_{2} = (-1,0,-2)^t$
$$
v_{2}=-u_{1}+2u_{2}
$$
So basis of $U$ generates $V$.
- $V\subseteq U$
Vector $u_{1} = (1,2,0)^T$ 
$$
u_{1}=2v_{1}+3v_{2}
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