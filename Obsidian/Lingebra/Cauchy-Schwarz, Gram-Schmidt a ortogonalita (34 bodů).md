1. Dokažte, že pro každé $a_1, a_2, a_3, a_4 \in \mathbb{R}$ platí:
$$
   5a_1 + a_2 + 3a_3 + a_4 \leq 6 \sqrt{a_1^2 + a_2^2 + a_3^2 + a_4^2}.
$$

Podle Cauchy-Schwarzovy nerovnosti platí:
$$
\left| \langle x,y \rangle  \right| \leq \left| \left| x \right|  \right| \cdot \left| \left| y \right| \right|
$$

Odmocnina na pravé straně vypadá jako norma vektoru $a = (a_{1},a_{2},a_{3},a_{4})^T$

$6$ muzeme prepsat jako $\sqrt{ 6^2 }$

$$
5a_1 + a_2 + 3a_3 + a_4 \leq \sqrt{ 6^2 } \cdot  \sqrt{a_1^2 + a_2^2 + a_3^2 + a_4^2}
$$

To by znamenalo, že $x=6$ a $y = a$ a skalarni soucin mame definovany obecne:
$$

$$



2. **(4 body)** Dokažte vztah mezi aritmetickým a kvadratickým průměrem.

3. **(12 bodů)** Stopa čtvercové matice je definována jako:
   $$
   \text{trace}(A) = \sum_i a_{ii}.
   $$
   Ukažte, že platí:
   - **(4 body)** $\text{trace}(A)^2 \leq n \cdot \text{trace}(A^T A)$,
   - **(4 body)** $\text{trace}(A^2) \leq \text{trace}(A^T A)$,
   - **(4 body)** $\text{trace}(A^T B) \leq \frac{1}{2} (\text{trace}(A^T A) + \text{trace}(B^T B))$.

4. **(10 bodů)** Buď
   $$
   v_1 = (1,1,0)^T, \quad v_2 = (1,1,1)^T.
   $$
   - **(3 body)** Ortonormalizujte vektory $v_1, v_2$.
   - **(3 body)** Proveďte ortonormalizaci v opačném pořadí vektorů.
   - **(4 body)** Najděte projekci $x = (0,1,1)^T$ do podprostoru $U = \text{span} \{ v_1, v_2 \}$. Jaká je vzdálenost $x$ od $U$?

5. **(4 body)** Zortonormalizujte bázi podprostoru $\mathbb{R}^4$ popsaného soustavou:
   $$
   x - y + u + v = 0, \quad x + u = 0.
   $$
