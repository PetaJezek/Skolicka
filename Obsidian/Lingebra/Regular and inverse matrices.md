1. Let matrix $A$ have odd numbers on the diagonal and even numbers off the diagonal. Can $A$ be singular?

We can safely say, that our matrix $A$ is a square matrix. That is because we call matrices singular (or regular) only when they are square.

To find our answer we can look at it from a different perspective. And that is:
## Can A not be regular?

So let's set A to $2\cdot 2$.  And calculate for that. Maybe we can find a clue to finding our answer.

Let matrix $A$ be (for now) defined as:
$$
A = \begin{bmatrix} 1 & 2 \\ 0 & 3 \end{bmatrix}
$$
As we can see, $A$ is regular so we need to look elsewhere.

We can look at two attributes of regular matrices:
-  Rows are not linearly dependant
- Columns are not linearly dependant

That means that i can't nullify one row or column completely with linear operations.

If:
$$
k \in \mathbb{Z}, \quad 2 | k
$$
(I know it's not right but let's say that $k$ is not a number but a list of numbers)
$$
A =  \begin{bmatrix}  k +1 & k \\ k & k+1 \end{bmatrix}
$$
We can say that these rows and columns are not dependant, because of the elements $k+1$. We can also say that if we keep increasing the size of $A$, this will stay the same, because in every new row and column, there will always be  only one element equal to $k+1$. That means $A$ will always be regular, which means **it can never be singular**.

(I have no idea how to prove this properly. I know this is not enough.)

----
2. Let matrix $A \in \mathbb{R}^{n \times n}$ (where $n > 2$) have elements $a \in \mathbb{R}$ on the diagonal and elements $b \in \mathbb{R}$ off the diagonal. Determine for which values of $a$ and $b$ the matrix $A$ is regular.

Lowest value of $n$ is 3.
$$
A =  \begin{bmatrix}  a & b & b \\ b & a & b \\ b & b & a \end{bmatrix}
$$
Matrix is regular when:
-  Rows are not linearly dependant
- Columns are not linearly dependant

That means that any linear operation within the matrix cannot create a zero vector, which means that the matrix was linearly dependant in some way.

If we subtract any row from the matrix from any row (linear operation) we get this row:
$$
[0, \dots,0, a-b,0, \dots,0, b-a,0 \dots]
$$
Which means that if $a=b$: The whole row would only $0$ (zero vector). So:
$$
a \neq b
$$

Every combination of $n-1$ rows will be containing a combination of these 3 elements: 
$$
{0,a-b,b-a}
$$

But if we add every row (let's say to the first row) we get a row looking like this:
$$
[a+b\cdot(n-1), a+b\cdot(n-1),  \dots, a+b\cdot(n-1)]
$$
The whole row would be made up of a one element $a+b\cdot(n-1)$. That means for A to be regular:
$$
a \neq b\cdot(n-1)
$$

So A is regular when: $$a \neq b \quad \text{and} \quad a \neq b\cdot(n-1)$$

----
3. Determine for which values of $n$ the matrix $A \in \mathbb{R}^{n \times n}$ is regular, given that its elements are defined as follows:
    - (a) $a_{ij} = i \cdot j$,
    - (b) $a_{ij} = i + j$.

a)
$$
A = \begin{bmatrix}
1 \cdot 1 & 1 \cdot 2 & 1 \cdot 3 & \cdots & 1 \cdot n \\
2 \cdot 1 & 2 \cdot 2 & 2 \cdot 3 & \cdots & 2 \cdot n \\
3 \cdot 1 & 3 \cdot 2 & 3 \cdot 3 & \cdots & 3 \cdot n \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
n \cdot 1 & n \cdot 2 & n \cdot 3 & \cdots & n \cdot n
\end{bmatrix}
$$

Every k-th row can be written as:
$$
Row_{k}=Row_{1}\cdot k
$$
Which means every row and column after the first one are linearly dependant on the first. So matrix A is regular only when:
$$
n=1
$$
b)
$$
A = \begin{bmatrix}
1 + 1 & 1 + 2 & 1 + 3 & \cdots & 1 + n \\
2 + 1 & 2 + 2 & 2 + 3 & \cdots & 2 + n \\
3 + 1 & 3 + 2 & 3 + 3 & \cdots & 3 + n \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
n + 1 & n + 2 & n + 3 & \cdots & n + n
\end{bmatrix}.
$$
If we subtract $Row_{k-1}$ from $Row_{k}$ then we get a row containing only number $1$.
Since $k-1=i, l-1=j: a_{ij}-1=a_{kl}$. We can subtract the row containing only number $1$ from the row $i$ to get the same elements that are in row $k$. We need two rows to create the row containing only number $1$ and another row to subtract from. So A can be regular only when:
$$
n \leq 2
$$


----

4. Prove that for matrices $A, B \in \mathbb{R}^{n \times n}$, the following holds:
   $$
   (ABA^{-1})^n = AB^nA^{-1}.
   $$

We can rewrite the left side of the equation:
$$
ABA^{-1}ABA^{-1}ABA^{-1}\dots ABA^{-1} = AB^nA^{-1}
$$
From definition of inverse matrices:
$$
A \cdot A^{-1} = A^{-1} \cdot A =I
$$
We can add brackets:
$$
AB(A^{-1}A)\cdot B(A^{-1}A) \cdot B(A^{-1}A) \dots \cdot BA^{-1} = AB^nA^{-1}
$$
$$
AB \cdot B^{n-2} \cdot BA^{-1} = AB^nA^{-1}
$$
$$
AB^{n}A^{-1} =  AB^nA^{-1}
$$
----
5. Find a matrix $A \in \mathbb{R}^{n \times n}$ that has no zero elements and satisfies $A = A^{-1}$.

We can adjust our equation $A = A^{-1}$ to $A\cdot A = I$ if we multiply each side by $A$.
Identity matrix to power of $n$ is still identity matrix so we can again rewrite the equation as:
$$
A^2=I^2
$$
This doesn't mean that $A=I$, because square rooting both sides isn't an equivalent operation.
We can divide our problem into a set of problems. First let's look when:
$$
A = I
$$
$I^{n\times n}, n>1$ contains number 0. So the only matrix that satisfies the assignment is  $A \in \mathbb{R}^{1 \times 1}$, which is a scalar.
Now let's look when $A \neq I$.

Let's find a matrix for $n=2$:
$$
A^2 = \begin{bmatrix} a & b \\ c & d \end{bmatrix} \begin{bmatrix} a & b \\ c & d \end{bmatrix} = \begin{bmatrix} a^2 + bc & ab + bd \\ ca + dc & cb + d^2 \end{bmatrix}
$$
$$
a^2+bc = 1
$$
$$
ab + bd = 0
$$
$$
ac +cd = 0
$$
$$
bc+d^2 = 1
$$
There is not existing solution for these equations, when none of these parameters can be 0. I don't know how to prove it, but I would guess that it is same for larger matrices. So my answer: Matrix A doesn't exist.





6. Prove that $\text{trace}(A) = \text{trace}(BAB^{-1})$, where $\text{trace}(M)$ is the sum of the diagonal elements of matrix $M$.

Trace is invariant to cyclic permutations of matrices.(Found on wikipedia) Here is the proof.

We will show that $$ \text{tr}(ABC) = \text{tr}(CAB) $$ for matrices $A$, $B$, and $C$.
By the definition of the trace, we have:

$$
\text{tr}(ABC) = \sum_{i=1}^n (ABC)_{ii}
$$



- $$
\text{tr}(ABC) =  \sum_{i=1}^n \sum_{k=1}^n A_{ik} (BC)_{ki}
$$

- $$
(BC)_{ki} = \sum_{j=1}^n B_{kj} C_{ji}
$$

$$
\text{tr}(ABC) = \sum_{i=1}^n \sum_{k=1}^n A_{ik}\sum_{j=1}^n B_{kj} C_{ji} 
$$

Now, let's compute the trace of $CAB$:

- $$
\text{tr}(CAB) = \sum_{i=1}^n (CAB)_{ii}
$$


- $$
tr(CAB) = \sum_{i=1}^n \sum_{k=1}^n C_{ik} (AB)_{ki}
$$

- $$
(AB)_{ki} = \sum_{j=1}^n A_{kj} B_{ji}
$$

Thus, the trace of $CAB$ becomes:

$$
\text{tr}(CAB) = \sum_{i=1}^n \sum_{k=1}^n C_{ik} \left( \sum_{j=1}^n A_{kj} B_{ji} \right)
$$

Now, compare the two sums for $\text{tr}(ABC)$ and $\text{tr}(CAB)$:


We can notice that these two expressions are similar, except for the names of the indices. We can manipulate the indices to show they are equal. 
Thus, we conclude that: $$ \text{tr}(ABC) = \text{tr}(CAB) $$