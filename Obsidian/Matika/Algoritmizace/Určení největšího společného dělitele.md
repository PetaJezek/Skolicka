_Problém_
urči největší společný dělitel

## Algoritmy
1.  Hrubá síla -> postpupně od největšího
2. Prvočíslený rozklad 
3. ## Euklidův algortimus ([[Eukleides]])

## Matematický důkaz Euklidova algoritmu

## Matematický důkaz Euklidova algoritmu

### Cíl:
Najít největšího společného dělitele (NSD) dvou kladných čísel $a$ a $b$.

### Definice:
Euklidův algoritmus je založen na následující skutečnosti: Pro každá dvě celá čísla $a$ a $b$, kde $a \geq b > 0$, platí, že:

$$
\text{NSD}(a, b) = \text{NSD}(b, r),
$$

kde $r$ je zbytek po dělení $a$ číslem $b$. Můžeme zapsat:

$$
a = bq + r \quad \text{kde} \quad 0 \leq r < b.
$$

Tento vztah vychází z dělení se zbytkem, kde $q$ je podíl a $r$ je zbytek. Poté se algoritmus opakuje pro $b$ a $r$ až do chvíle, kdy $r = 0$. V tomto okamžiku je $b$ největším společným dělitelem (NSD).

### Tvrzení:
Největší společný dělitel dvou čísel $a$ a $b$ je stejný jako největší společný dělitel $b$ a $r$, kde $r$ je zbytek po dělení $a$ číslem $b$. Tedy platí:

$$
\text{NSD}(a, b) = \text{NSD}(b, r).
$$

### Důkaz:

#### 1. Existence společného dělitele:
Nechť $d$ je největší společný dělitel čísel $a$ a $b$. To znamená, že $d$ dělí $a$ i $b$, tedy:

$$
d \mid a \quad \text{a} \quad d \mid b.
$$

Z rovnice $a = bq + r$ víme, že zbytek $r$ lze vyjádřit jako:

$$
r = a - bq.
$$

Protože $d \mid a$ a $d \mid b$, musí platit, že $d$ dělí i $r$ (protože $d$ dělí obě strany rovnice). Tedy každý společný dělitel čísel $a$ a $b$ dělí také $r$. Tím jsme prokázali, že každý společný dělitel $a$ a $b$ je zároveň společným dělitelem $b$ a $r$.

#### 2. Redukce problému:
Na základě výše uvedeného můžeme problém zredukovat na hledání NSD mezi $b$ a $r$. Můžeme opakovat stejný postup pro dvojici čísel $b$ a $r$, kde nahradíme $a$ hodnotou $b$ a $b$ hodnotou $r$, a postupujeme dále, dokud nedosáhneme $r = 0$.

#### 3. Rekurze:
Tento postup můžeme iterativně opakovat, dokud $r = 0$. Poslední nenulové $b$ bude největší společný dělitel původních čísel $a$ a $b$.

Formálně tento proces popíšeme takto:

$$
a_0 = a, \quad a_1 = b, \quad a_2 = r_1, \quad \dots
$$

kde každé $a_{n+1}$ je zbytek z dělení $a_n$ a $a_{n+1}$, tedy:

$$
a_{n-1} = a_n q_n + a_{n+1} \quad \text{kde} \quad 0 \leq a_{n+1} < a_n.
$$

Proces pokračuje, dokud $a_{n+1} = 0$. Poslední nenulové $a_n$ je $\text{NSD}(a, b)$.

#### 4. Závěr:
Když $r = 0$, algoritmus končí a máme:

$$
\text{NSD}(a, b) = b.
$$

Tedy poslední nenulový zbytek je největší společný dělitel.

### Příklad:
Najděme $\text{NSD}(252, 105)$ pomocí Euklidova algoritmu:

1. $$ 252 = 105 \times 2 + 42, $$ tedy $\text{NSD}(252, 105) = \text{NSD}(105, 42)$.
2. $$ 105 = 42 \times 2 + 21, $$ tedy $\text{NSD}(105, 42) = \text{NSD}(42, 21)$.
3. $$ 42 = 21 \times 2 + 0, $$ tedy $\text{NSD}(42, 21) = 21$.

Proto $\text{NSD}(252, 105) = 21$.

### Závěr:
Euklidův algoritmus nám umožňuje efektivně vypočítat největšího společného dělitele dvou čísel pomocí opakovaného dělení se zbytkem. Důkaz jsme provedli pomocí postupné redukce problému na menší a menší zbytky, dokud nedosáhneme zbytku rovného nule, kdy se poslední nenulový zbytek stává NSD.
