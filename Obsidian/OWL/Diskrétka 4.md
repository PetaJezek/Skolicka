#### Příklad 1
Dokažte kombinatoricky následující identitu (kombinatoricky interpretujte obě strany a ukažte, že se rovnají):

$$
\binom{n}{k} + \binom{n}{k+1} = \binom{n+1}{k+1}
$$
Máme n případů + jeden zvláštní případ $X$. 
1. Pokud nezvolíme tento objekt, chceme z $n$  vybrat $k$:
$$
\binom{n}{k} 
$$

2. Pokud ho zvolíme, z n objektů volíme k+1:
$$
\binom{n}{k+1} 
$$

3. Součtem obou je počet způsobů jak vybrat k+1 objektů z n+1 což je:
$$
\binom{n+1}{k+1} 
$$