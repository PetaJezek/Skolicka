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
Let's substitute to both sides of our equation:

$$

$$



---

#### 2. (3 points) Intersection of Subgroups  
Let $H_1$ and $H_2$ be subgroups of a group $G$. Show that $H_1 \cap H_2$ is also a subgroup of $G$.

---

#### 3. (10 points) Solving Systems of Equations  
Solve the following systems of equations **without row swapping**:

1. Over $\mathbb{Z}_3$:  
   $$  
   \begin{bmatrix}  
   2 & 1 & 1 & 0 \\  
   1 & 0 & 2 & 1 \\  
   1 & 1 & 2 & 2  
   \end{bmatrix}.  
   $$

2. Over $\mathbb{Z}_2$ and $\mathbb{Z}_5$:  
   $$  
   \begin{bmatrix}  
   0 & 1 & 1 & 1 \\  
   1 & 0 & 1 & 1 \\  
   1 & 1 & 0 & 1  
   \end{bmatrix}.  
   $$

---

#### 4. (3 points) Matrix Exponentiation in $\mathbb{Z}_7$  
Compute the $100$th power of the matrix in $\mathbb{Z}_7$:  
$$  
\begin{bmatrix}  
3 & 2 \\  
2 & 4  
\end{bmatrix}^{100}.  
$$
