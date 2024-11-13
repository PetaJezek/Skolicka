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
We can say that these rows and columns are not dependant, because of the elements $k+1$. We can also say that if we keep increasing the size of $A$, this will stay the same, because in every row and column will always be one element equal to $k+1$. That means $A$ will always be regular, which means **it can never be singular**.


2. Let matrix $A \in \mathbb{R}^{n \times n}$ (where $n > 2$) have elements $a \in \mathbb{R}$ on the diagonal and elements $b \in \mathbb{R}$ off the diagonal. Determine for which values of $a$ and $b$ the matrix $A$ is regular.

Lowest value of $n$ is 3.
$$
A =  \begin{bmatrix}  a & b & b \\ b & a & b \\ b & b & a \end{bmatrix}
$$
Matrix is regular when:
-  Rows are not linearly dependant
- Columns are not linearly dependant

At first sight, we can say that $a \neq b \quad \text{and} \quad a\neq 0$, because then all rows and columns are dependant.

Also the matrix will not be regular when we can eradicate a with linear operations using the value of b.(Like a- 3b = 0) because then again we are getting a singular matrix. So the final condition for A to be regular is 
$$
k \in \mathbb{R}
$$
$$
a \neq k\cdot b
$$

3. Determine for which values of $n$ the matrix $A \in \mathbb{R}^{n \times n}$ is regular, given that its elements are defined as follows:
    - (a) $a_{ij} = i \cdot j$,
    - (b) $a_{ij} = i + j$.

4. Prove that for matrices $A, B \in \mathbb{R}^{n \times n}$, the following holds:
   $$
   (ABA^{-1})^n = AB^nA^{-1}.
   $$

5. Find a matrix $A \in \mathbb{R}^{n \times n}$ that has no zero elements and satisfies $A = A^{-1}$.

6. Prove that $\text{trace}(A) = \text{trace}(BAB^{-1})$, where $\text{trace}(M)$ is the sum of the diagonal elements of matrix $M$.
