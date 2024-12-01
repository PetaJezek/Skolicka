#### 1. (7 points) Algebraic Structures on Intervals  
Let $\mathbb{IR}$ be the set of closed real intervals, i.e., $[a, b]$ where $a, b \in \mathbb{R}$ and $a \leq b$, with the following operations:

- **Addition**:  
  $$[a_1, a_2] + [b_1, b_2] = [a_1 + b_1, a_2 + b_2],$$

- **Multiplication**:  
  $$[a_1, a_2] \cdot [b_1, b_2] = \left[\min(a_1b_1, a_1b_2, a_2b_1, a_2b_2), \max(a_1b_1, a_1b_2, a_2b_1, a_2b_2)\right].$$

Analyse the algebraic structures $(\mathbb{IR}, +)$ and $(\mathbb{IR}, \cdot)$:  
Which properties of algebraic structures do these satisfy, and which do they not? Are these structures groups?

We are going to be looking at properties of groups and checking if our "possible" groups are satisfying them. 

i) $(\mathbb{IR}, +)$ 

- **Association:** $\forall a, b, c, \in \mathbb{G}: a \circ(b\circ c) = (a\circ b) \circ c$
We have intervals: $$[a_{1},a_{2}],[b_{1},b_{2}],[c_{1},c_{2}],$$
where: $$a_{1} \leq a_{2},\quad b_{1} \leq b_{2},\quad c_{1} \leq c_{2},$$
Let's substitute to both sides of our equation:$$
[a_{1},a_{2}] + ([b_{1},b_{2}] + [c_{1},c_{2}]) = ([a_{1},a_{2}] + [b_{1},b_{2}]) + [c_{1},c_{2}]
$$

We add according to the definition:
$$
[a_{1},a_{2}] + [b_{1} + c_{1},b_{2}+ c_{2}] = [a_{1} + b_{1},a_{2}+ b_{2}] + [c_{1},c_{2}]
$$

$$
[a_{1}+b_{1} + c_{1},a_{2}+b_{2}+ c_{2}] = [a_{1}+b_{1} + c_{1},a_{2}+b_{2}+ c_{2}] 
$$
Both sides are equal, which means $(\mathbb{IR}, +)$ **satisfies** the association condition.

- **Existence of the neutral element:** $\exists  e\in G  \quad \forall a \in G: e \circ a = a \circ e = a$

We have interval $[a_{1},a_{2}]$, where $a_{1} \leq a_{2}$.
We are looking for interval $[e_{1},e_{2}]$, where: $e_{1} \leq e_{2} \land e_{1},e_{2} \in \mathbb{R}$ and $[a_{1}+e_{1}, a_{2}+e_{2}] = [a_{1},a_{2}]$

We get two equations:
$$
a_{1} + e_{1} = a_{1}
$$

and
$$
a_{2} + e_{2} = a_{2}
$$
Answer for both: $e_{1},e_{2} = 0$. It also satisfies condition $e_{1} \leq e_{2}$  That means  in $(\mathbb{IR}, +)$ exists a neutral element for all elements in $(\mathbb{IR}, +)$.



- **Existence of the inverse element**: $\forall a \in \mathbb{IR} \quad \exists b \in \mathbb{G}: a \circ b = b \circ a = e$

We have interval $[a_{1},a_{2}]$, where $a_{1} \leq a_{2}$ and an interval $e = [0,0]$.
We are looking for interval $[b_{1},b_{2}]$, where $b_{1} \leq b_{2} \land b_{1},b_{2} \in \mathbb{R}$ and $[a_{1}+b_{1}, a_{2}+b_{2}]=[0,0]$ 

We get 2 equations
$$
a_{1}+b_{1}=0
$$

$$
a_{2}+b_{2}=0
$$
We get: $$-a_{1} = b_{1} \quad \text{and}\quad -a_{2} = b_{2}.$$
Since elements of intervals in $(\mathbb{IR},+)$ are from a set of real numbers, our equation holds true for all values.

That means every interval in $(\mathbb{IR},+)$ has its own inverse element (interval).

$(\mathbb{IR},+)$ **is a group**, because  all  3 axioms mentioned are true for our structure.

- **Abel's group**: $\forall a,b \in \mathbb{IR}: a \circ b =b \circ a$
We get:
$$
[a_{1},a_{2}] + [b_{1},b_{2}] = [b_{1},b_{2}]+ [a_{1},a_{2}]
$$
$$
[a_{1}+b_{1},a_{2}+b_{2}] = [b_{1}+a_{1},b_{2}+a_{2}]
$$

Since addition is commutative, both sides are equal. That means that $(\mathbb{IR},+)$ is a Abel's group.

ii) $(\mathbb{IR},\cdot)$
- **Association** $\forall a, b, c, \in \mathbb{G}: a \circ(b\circ c) = (a\circ b) \circ c$
We have intervals: $$[a_{1},a_{2}],[b_{1},b_{2}],[c_{1},c_{2}],$$
where: $$a_{1} \leq a_{2},\quad b_{1} \leq b_{2},\quad c_{1} \leq c_{2},$$

$$[a_1, a_2] \cdot [b_1, b_2] = \left[\min(a_1b_1, a_1b_2, a_2b_1, a_2b_2), \max(a_1b_1, a_1b_2, a_2b_1, a_2b_2)\right].$$

$$b \cdot c = [e,f]$$
$$e = min[b_{1}c_{1},b_{1}c_{2},b_{2}c_{1},b_{2}c_{2}],$$ $$f=max[b_{1}c_{1},b_{1}c_{2},b_{2}c_{1},b_{2}c_{2}]$$

$$a \cdot b = [g,h]$$
$$g = min[a_{1}b_{1},a_{1}b_{2},a_{2}b_{1},a_{2}b_{2}],$$
$$h = max[a_{1}b_{1},a_{1}b_{2},a_{2}b_{1},a_{2}b_{2}]$$

So the left side is going to look like:
$a⋅(b⋅c)=[min(a_{1}​e,a_{1}f,a_{2}​e,a_{2}​f),max(a_{1}​e,a_{1}​f,a_{2}​e,a_{2}​f)].$

And the right side is going to look like:
$(a⋅b)⋅c=[min(c_{1}​g,c_{1}h,c_{2}​g,c_{2}hf),max(c_{1}​g,c_{1}​h,c_{2}​g,c_{2}​h)].$

Both sides now cover all the products of each elements when multiplying $[a_{1},a_{2}]\cdot[b_{1},b_{2}]\cdot[c_{1},c_{2}]$
Thanks to association of real numbers and the fact that $\min$ and $\max$ functions do not rely on number order, we can say that both sides are equal and thus this structure is **associative**.

- **Existence of the neutral element** $\exists  e\in G  \quad \forall a \in G: e \circ a = a \circ e = a$
$$
[e_{1},e_{2}] \cdot [a_{1},a_{2}] = [a_{1},a_{2}]
$$
Since $\min$ and $\max$ functions do not rely on number order we do not have to look at  $a \cdot e$.

We know that neutral element of multiplication is 1.
When we set both $e_{1},e_{2}=1$ we get:
$$
[min(a_{1}*1,a_{2}*1),max(a_{1}*1),a_{2}*1] = [a_{1},a_{2}]
$$
$$
[min(a_{1},a_{2}),max(a_{1},a_{2})] = [a_{1},a_{2}]
$$
If $a_{1} \neq a_{2}$ :
$$
[a_{1},a_{2}] = [a_{1},a_{2}].
$$
If $a_{1}=a_{2}$ :
$$
[a_{1},a_{1}] = [a_{1},a_{1}].
$$

The **neutral element** of the structure $(\mathbb{IR},\cdot)$ is $[1,1]$.

- The existence of the **inverse element**: $\forall a \in \mathbb{IR} \quad \exists b \in \mathbb{G}: a \circ b = b \circ a = e$

$$
[min(a_{1}b_{1},a_{1}b_{2},a_{2}b_{1},a_{2}b_{2}),max(a_{1}b_{1},a_{1}b_{2},a_{2}b_{1},a_{2}b_{2})] = [1,1]
$$
We can rewrite it:
$$
min(a_{1}b_{1},a_{1}b_{2},a_{2}b_{1},a_{2}b_{2}) = max(a_{1}b_{1},a_{1}b_{2},a_{2}b_{1},a_{2}b_{2}) = 1
$$
The inverse of $a$ for multiplication is $a^{-1}$.
Since $\min$ and $\max$ are equal, we can see that if $a_{1}=a_{2} \implies b=[a^{-1},a^{-1}]$.
But what if $a_{1} < a_{2}$. Then for each number, interval b has to contain the numbers $a_{1}^{-1},a_{2}^{-1}$. But if $a_{1} \neq a_{2}$ then $a_{1}\cdot a_{2}^{-1} \neq 1$ and $a_{2}\cdot a_{1}^{-1} \neq 1$. Both of these numbers are regular combinations. There is no way to get rid of them a since they can be smaller and bigger than 1, they can be outputs of the $\min$ and $\max$ functions. That means that for some intervals, the inverse element **does not exist**.

That means this structure is not a group since it doesn't have an inverse element for every element.

---

#### 2. (3 points) Intersection of Subgroups  
Let $H_1$ and $H_2$ be subgroups of a group $G$. Show that $H_1 \cap H_2$ is also a subgroup of $G$.

DEFINITION: Subgroup of group $(\mathbb{G},\circ)$ is group $(\mathbb{H},\mathbin{\square} )$ that satisfies $H \subseteq G$ and $\forall a,b \in H: a \circ b = a \mathbin{\square} b$.
- **Closure** $a \mathbin{\square} b \in H_1 \cap H_2$
We know that $a,b \in H_{1} \land a,b \in H_{2}$.
So $a,b,c$ in  $a \mathbin{\square} b = c$ are all part of $H_{1}$ and $H_{2}$, since both of them are groups and they satisfy the closure  property.


- **Association**
$H_{1}$ and $H_{2}$ are both associative. If they are not equal, their intersection will be smaller. But having less elements does not affect the association property. Because association hold true for all elements, not a specific ones.
- **Existence of the neutral element**: 
Since every subgroup of a group has to have the neutral element $e$, the neutral element will be in the intersection of two and more subgroups. That means that $e \in H_1 \cap H_2$
-**Existence of the inverse element**
Every element in $H_{1}$ and $H_{2}$ has its own inverse element. That means when an element is in both of these subgroups, his inverse element is in both too and thus will be in the intersection. $\forall a \in H_{1} \cap H_{2},  \exists b \in H_{1} \cap H_{2}: a \mathbin{\square} b = e$

Since this set satisfies all the axioms, we can say that $H_1 \cap H_2$ is a subgroup of $G$.

---

#### 3. (10 points) Solving Systems of Equations  
Solve the following systems of equations **without row swapping**:

1. Over $\mathbb{Z}_3$:  
   $$  
   \begin{bmatrix}  
   2 & 1 & 1 & \vert &0 \\  
   1 & 0 & 2 &\vert &1 \\  
   1 & 1 & 2 &\vert& 2  
   \end{bmatrix}.  
   $$
   Add second row to the first row:
$$  
   \begin{bmatrix}  
   0 & 1 & 0 & \vert & 1 \\  
   1 & 0 & 2 &\vert & 1 \\  
   1 & 1 & 2 &\vert & 2  
   \end{bmatrix}.  
   $$
   Add 2 times first row to third row:
$$  
   \begin{bmatrix}  
   0 & 1 & 0 & \vert & 1 \\  
   1 & 0 & 2 &\vert & 1 \\  
   1 & 0 & 2 &\vert & 1  
   \end{bmatrix}.  
   $$
$$  
   \begin{bmatrix}  
   0 & 1 & 0 & \vert & 1 \\  
   1 & 0 & 2 &\vert & 1 \\  
   0 & 0 & 0 &\vert & 0  
   \end{bmatrix}.  
   $$

$$
x_{2}=1
$$
$$
x_{1}=1-2x_{3}
$$
$$
(x_{1},x_{2},x_{3})=(1-2x_{3}, 1, x_{3} \in \mathbb{Z}_{3})
$$


2. Over $\mathbb{Z}_2$ and $\mathbb{Z}_5$:  
$$
\begin{bmatrix}  
   0 & 1 & 1 & \vert & 1 \\  
   1 & 0 & 1 & \vert & 1 \\  
   1 & 1 & 0 & \vert & 1  
\end{bmatrix}
$$
i) $\mathbb{Z}_2$

Add second and third row to first row:
$$
\begin{bmatrix}  
   1 & 0 & 0 & \vert & 1 \\  
   1 & 0 & 1 & \vert & 1 \\  
   1 & 1 & 0 & \vert & 1  
\end{bmatrix}
$$
   Subtract first row from second and third row:
   $$
\begin{bmatrix}  
   0 & 0 & 0 & \vert & 1 \\  
   0 & 0 & 1 & \vert & 0 \\  
   0 & 1 & 0 & \vert & 0  
\end{bmatrix}
$$
$$
0x_{1}+0x_{2}+0x_{3}=1
$$
That means this matrix does not have a solution.

ii) $\mathbb{Z}_5$
 $$
\begin{bmatrix}  
   0 & 1 & 1 & \vert & 1 \\  
   1 & 0 & 1 & \vert & 1 \\  
   1 & 1 & 0 & \vert & 1  
\end{bmatrix}
$$
Add second row to the first row:

 $$
\begin{bmatrix}  
   1 & 1 & 2 & \vert & 2 \\  
   1 & 0 & 1 & \vert & 1 \\  
   1 & 1 & 0 & \vert & 1  
\end{bmatrix}
$$
Subtract first row from the second and third row:
$$
\begin{bmatrix}  
   1 & 1 & 2 & \vert & 2 \\  
   0 & 4 & 4 & \vert & 4 \\  
   0 & 0 & 3 & \vert & 4  
\end{bmatrix}
$$
$$
3x_{3}=4
$$
$$
x_{3}=3
$$
Substitute:
$$
4x_{2}+ 12 = 4
$$
$$
4x_{2}+2=4
$$
$$
4x_{2}=2
$$

$$
x_{2}=3
$$
Substitute:
$$
x_{1}+3+1=2
$$
$$
x_{1} +4 = 2
$$
$$
x_{1}=3
$$
$$
(x_{1},x_{2},x_{3})=(3,3,3)
$$

#### 4. (3 points) Matrix Exponentiation in $\mathbb{Z}_7$  
Compute the $100$th power of the matrix in $\mathbb{Z}_7$:  
$$  
\begin{bmatrix}  
3 & 2 \\  
2 & 4  
\end{bmatrix}^{100}.  
$$
We can only hope that after a few powers the matrix returns to its original state. Let's find the period.

$\begin{bmatrix}  3 & 2 \\  2 & 4  \end{bmatrix}$$\to$ $\begin{bmatrix}  6 & 0 \\  0 & 6  \end{bmatrix}$ $\to$$\begin{bmatrix}  4 & 5 \\  5 & 3  \end{bmatrix}$$\to$$\begin{bmatrix}  1 & 0 \\  0 & 1  \end{bmatrix}$
That means that $A=A^5$. We can rewrite $A^{100}$ as $A^{4^{25}} = A^4$. So the answer is $A^4$:
$$
\begin{bmatrix}  1 & 0 \\  0 & 1  \end{bmatrix}
$$
 