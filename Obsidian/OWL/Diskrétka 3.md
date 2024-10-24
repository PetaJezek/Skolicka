

### Příklad 1

Uvažme relaci ⪯ na množině \( R^3 \) definovanou předpisem:

$$
(a_1, b_1, c_1) ⪯ (a_2, b_2, c_2) \iff (a_1 \geq a_2 \land b_1 \geq b_2 \land c_1 \leq c_2).
$$

Jedná se o částečné uspořádání? Pokud ano, dokažte, pokud ne, také pečlivě zdůvodněte.

---

Pokud se jedná o částečné uspořádání, musí tato relace splňovat tři podmínky:
## 1.  Reflexivita
V našem případě to znamená, že:
$$
a_{1} = a_{2}
$$
$$
b_{1} = b_{2}$$
$$
c_{1} = c_{2}
$$
Po dosazení získáme výraz:
$$
(a_1 \geq a_1 \land b_1 \geq b_1 \land c_1 \leq c_1).
$$
Toto tvrzení platí, takže tato relace je relfexivní.
## 2. Slabá antisymetrie
Aby relace mohla být antisymetrická může být pouze symetrická, když,
$$
a_{1} = a_{2}
$$
$$
b_{1} = b_{2}$$
$$
c_{1} = c_{2}
$$
což jsme dokázali v předchozím bodě.
Teď musíme dokázat, že v jiném případě není symetrická.
To dokážeme tak že prohodíme prvky v relaci. Dostáváme tento výraz:
$$
(a_2 \geq a_1 \land b_2 \geq b_1 \land c_2 \leq c_1).
$$
Pokud má ale zároveň platit:
$$
(a_1 \geq a_1 \land b_1 \geq b_1 \land c_1 \leq c_1).
$$
Dostáváme opět výsledek:
$$
a_{1} = a_{2}
$$
$$
b_{1} = b_{2}$$
$$
c_{1} = c_{2}
$$
Tato relace je tedy slabě antisymetrická.
## 3. Tranzitivita
Aby byla relace antisymetrická, musí platit:
$$
(a_1 \geq a_3 \land b_1 \geq b_3 \land c_1 \leq c_3)
$$
S tím že:

$$
\begin{aligned}
a_{3} \leq a_{2} \leq a_{1}  \\
b_{3} \leq b_{2} \leq b_{1}  \\
c_{3} \geq c_{2}\geq c_{1}
\end{aligned}
$$
Můžeme tedy rozepsat naše tvrzení takto:
$$
(a_1 \geq a_{2} \geq a_3 \land b_1 \geq b_{2} \geq b_3 \land c_1 \leq c_{2} \leq c_3).
$$
V porovnání s předchozím tvrzením můžeme vidět, že jsou všechny podmínky zachovány, takže tato relace je tranzitvní.
$$
\begin{aligned}
(a_1 \geq a_2\land b_1 \geq b_2 \land c_1 \leq c_2) \\
(a_2 \geq a_3 \land b_2 \geq b_3 \land c_2 \leq c_3)
\end{aligned}
$$
# Závěr

**Tato relace je částečné uspořádání.**