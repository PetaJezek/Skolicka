### Problem Set

1. Let matrix $A$ have odd numbers on the diagonal and even numbers off the diagonal. Can $A$ be singular?
So what are we actually looking at is:
## Can A ever be regular?
If we would find that A can never be regular, that means our predicament is true.

So it only makes sense to calculate for **square matrices** because only them can be **regular**.

So let's set A to $2\cdot 2$.  And calculate for that. Maybe we can find a clue to finding our answer.

Let matrix $A$ be (for now) defined as:
$$
A = \begin{bmatrix} 1 & 2 \\ 0 & 3 \end{bmatrix}
$$
Now let's use the Gauss-elimination 

2. Let matrix $A \in \mathbb{R}^{n \times n}$ (where $n > 2$) have elements $a \in \mathbb{R}$ on the diagonal and elements $b \in \mathbb{R}$ off the diagonal. Determine for which values of $a$ and $b$ the matrix $A$ is regular (invertible).

3. Determine for which values of $n$ the matrix $A \in \mathbb{R}^{n \times n}$ is regular, given that its elements are defined as follows:
    - (a) $a_{ij} = i \cdot j$,
    - (b) $a_{ij} = i + j$.

4. Prove that for matrices $A, B \in \mathbb{R}^{n \times n}$, the following holds:
   $$
   (ABA^{-1})^n = AB^nA^{-1}.
   $$

5. Find a matrix $A \in \mathbb{R}^{n \times n}$ that has no zero elements and satisfies $A = A^{-1}$.

6. Prove that $\text{trace}(A) = \text{trace}(BAB^{-1})$, where $\text{trace}(M)$ is the sum of the diagonal elements of matrix $M$.
