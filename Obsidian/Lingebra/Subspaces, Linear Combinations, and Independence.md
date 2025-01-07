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

If we can then generate basis of $U$ by a combination of basis from $V$, we should be able to generate $U$ using basis of $V$. That means $U\subseteq V$. 

If we combine these two inclusions, we get $U=V$. 
(The bases of the vector spaces will be denoted as $u_{1},u_{2} \in U; v_{1},v_{2} \in V$
- $V\subseteq U$
Vector $v_{1} = (2,1,3)^T$.
$$
v_{1}=2u_{1}-3u_{2}
$$
Vector $v_{2} = (-1,0,-2)^T$
$$
v_{2}=-u_{1}+2u_{2}
$$
So basis of $U$ generates $V$.
- $U\subseteq V$
Vector $u_{1} = (1,2,0)^T$ 
$$
u_{1}=2v_{1}+3v_{2}
$$
Vector $u_{2}=(0,1,-1)^T$
$$
u_{2}=v_{1}+2v_{2}
$$
Basis of $V$ generates $U$.
**Combining said inclusions, we proved that $U=V$.**

4. Let $M = \{a, b, c, d, e\}$ and consider the vector space $2^M$, i.e., the space of all subsets of $M$ over the field $\mathbb{Z}_2$, where addition is understood as exclusive disjunction (XOR) and scalar multiplication follows naturally: $1 \cdot x = x$, $0 \cdot x$ is the zero vector.(
a) Find the zero vector.
b) Find $-v$ for $v = {a, b, c}$.
c) Evaluate the linear combination $u + v - w - z$, where:
$$
u = \{a, d\} , v = \{b, e\} , w = \{c, e\} , z = \{a, b, c\}.
$$

a) 
Zero vector  **0** has to satisfy that:
- $A +$**0** $=A$. Addition is defined as an exclusive disjunction. 

XORing sets involves adding the elements together modulo 2, meaning if an element is in both sets, it cancels out, and if an element is in only one of the sets, it remains. That means that the result of addition of two vectors from our vector space $2^M$ will contain elements that appear only in one vector. That means zero vector cannot contain an element in $A$ or element that is not in $A$.  These two inclusions give us the conclusion that **0** does not contain any elements. Which means **zero vector of the vector space $2^M$ is $\emptyset$ (the null vector).**

b)
- Find $-v$ for: $v = \{a,b,c\}$

We know that $v+(-v)=\emptyset$.
For the result of exclusive disjunction of two vectors to be a null vector, both vectors have to contain the same elements and nothing else. Only then the addition equals $\emptyset$. 

When $v = \{a,b,c\}$, $-v$ has to contain the same elements. 
So $-v = v = \{a,b,c\}$.

c)

Since we found out in the last part that $-A = A$, we can just add everything from left to right. 

$$
u + v = \{a, d\} \oplus \{b, e\}
$$
Therefore:
$$
u + v = \{a, b, d, e\}.
$$
Now, compute $(u + v) + w$:
$$
(u + v) + w = \{a, b, d, e\} \oplus \{c, e\}
$$
XORing these sets gives us:
$$
\{a, b, d, e\} \oplus \{c, e\} = \{a, b, c, d\},
$$

Finally, compute $(u + v + w) + z$:
$$
(u + v + w) + z = \{a, b, c, d\} \oplus \{a, b, c\}
$$
XORing these sets gives:

$$
\{a, b, c, d\} \oplus \{a, b, c\} = \{d\},
$$

Thus, the result of the linear combination $u + v - w - z$ is:

$$
\{d\}
$$

5. Let $u, v, w$ be linearly independent vectors from the space $V$ over $\mathbb{R}$. Determine whether the following sets of vectors are linearly independent:
a) ${u, v + w}$
b) ${0, u, v}$
c) ${u + v, u - v, u + w, u - w}$
d) ${u - v, 2v + w, -u - v - 3w}$

	Set of vectors is linearly dependent when at least one of the vectors in the set can be generated by a non-trivial linear combination of the other vectors. 

a) ${u, v + w}$
Since $u,v,w$ are linearly independent vectors. Any combination of the two of them will not equal  the third one. So this set **is linearly independent.**

b) ${0, u, v}$

0 can be generated by 3 combinations. Here is one: $0\cdot u+0\cdot v = 0$. That means this set  **is linearly dependent.**

c) ${u + v, u - v, u + w, u - w}$

At first sight we can see: 
$$
(u+v)+(u-v)=(u+w)+(u-w)
$$
We can rewrite it as:
$$
(u+v)= (u+w)+(u-w) + (-1)\cdot(u-v)
$$
This proves that this set **is linearly dependent.**. 
d) ${u - v, 2v + w, -u - v - 3w}$

$$
c_{1}(u-v)+c_{2}(2v+w)+c_{3}(-u-v-3w)=0
$$
$$
c_{1}u-c_{1}v+2c_{2}v+c_{2}w-c_{3}u-c_{3}v-3c_{3}v=0
$$
$$
u(c_{1}-c_{3}) + v(-c_{1}+2c_{2}-c_{3})+w(c_{2}-3c_{3})=0
$$
$u,v,w$ is linearly independent which means none of them are equal to the null vector. So we get:
$$
c_{1}-c_{3}=0
$$
$$
2c_{2}-c_{1}-c_{3}=0
$$
$$
c_{2}-3c_{3}=0
$$

From the first equation we get:
$$
c_{1}=c_{3}
$$
Substitute this into the second equation:
$$
2c_{2}-2c_{3}=0
$$
$$
c_{2}=c_{3}
$$
Substitute this into the third equation:
$$
c_{3}-3c_{3}=0
$$
$$
-2c_{3}=0
$$
$$
c_{3}=0
$$
Since:
$$
c_{1}=c_{2}=c_{3}=0
$$
The solution to this system is when all coefficients are equal to 0 which is a trivial solution. That means this set **is linearly independent**.

6. Show that the vectors $v_1, \dots, v_n \in V$ are linearly independent only if the vectors $v_1, v_1 + v_2, v_1 + v_2 + v_3, \dots, \sum_{i=1}^n v_i$ (will be denoted as $V'$) are linearly independent.

Let's prove this by a contradiction. Let us presume that vectors in $V'$ are not linearly independent.
That means, that when we add a vector $u$ to a vector $v$, we get a vector that is linearly dependent. $v+u$ can be generated by vectors whose sum is equal to v, because $v = \sum_{i=1}^n v_i$.  
What we can say about $V'$ before adding $u$ is that we can generate every vector from $V$ until the vector $u$. 
Prove:
If $|V'| = |V| =2$: 
we already have $v_{1}$ and we can generate $v_{2}$ by adding $-1\cdot(v_{1})$ to the second vector $v_{1}+v_{2}$. This way, we can generate all of the vectors  $v_{1},v_{2},v_{3},\dots,v_{k-1}$ ($k$ is the index of the $u$ vector). However, when $u$ is added, the resulting set becomes linearly dependent, according to our assumption. 

This implies that $u$ can be written as a linear combination of the previous vectors in $V'$. But note that $u=\sum_{i=1}^kv_{i}$​, where $v_{k}$​ is a new vector not yet in the span of the previous $v_{1},v_{2},\dots,v_{k−1}$. This would mean that ​ itself can be written as a linear combination of $v_{1},v_{2},\dots,v_{k−1}$.

This directly contradicts the assumption that $v_1, \dots, v_n \in V$ ​ are linearly independent, as $v_k$​ cannot be dependent on the previous vectors in $V$.

So that means vectors in $V$ are linearly independent only when the vectors of $V'$ are too.


