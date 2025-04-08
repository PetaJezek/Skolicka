1. Dokažte, že pro každé $a_1, a_2, a_3, a_4 \in \mathbb{R}$ platí:
$$
   5a_1 + a_2 + 3a_3 + a_4 \leq 6 \sqrt{a_1^2 + a_2^2 + a_3^2 + a_4^2}.
$$

Podle Cauchy-Schwarzovy nerovnosti platí:
$$
\left| \langle x,y \rangle  \right| \leq \left| \left| x \right|  \right| \cdot \left| \left| y \right| \right|
$$

Na levo tedy mame vlastne skalarni soucin vektoru $a$ a vektoru $v=(5,1,6,1)^t$.

$$
x = a;  y = v
$$
Pod CS nerovnosti ziskavame:
$$
\left| \langle a,v \rangle  \right| \leq \left| \left| a \right|  \right| \cdot \left| \left| v \right| \right| = \sum_{i=1}^4a_{i}v_{i} \leq \sqrt{ \sum_{i=0}^4a_{i}^2 } \cdot \sqrt{ \sum_{i=0}^4v_{i}^2 }
$$

$$
 5a_1 + a_2 + 3a_3 + a_4 \leq  \sqrt{a_1^2 + a_2^2 + a_3^2 + a_4^2}\cdot \sqrt{ 5^2+1+3^2+1 } 
$$
$$
5a_1 + a_2 + 3a_3 + a_4 \leq  \sqrt{a_1^2 + a_2^2 + a_3^2 + a_4^2} \cdot 6
$$


Mame dokazano.

---
2. **(4 body)** Dokažte vztah mezi aritmetickým a kvadratickým průměrem.


Aritmeticky prumer $A$:
$$
A = \frac{1}{n}\sum_{i=1}^nx_{i}
$$
Kvadraticky prumer $K$:
$$
B = \sqrt{\frac{1}{n}\sum_{i=1}^nx_{i}^2}
$$

A vztah mezi nimi je definovan jako:
$$
A \leq B
$$

Opet vyuzijeme CS nerovnost.

$A$ muzeme prepsat jako:
$$
A = \sum_{i}^n \frac{1}{n}x_{i}
$$
coz je skalarani soucin mezi vektorem $x$ a $y$, kde $y$ ma na vsech pozicich $\frac{1}{n}$.

Dosadme do CS:

$$
\left| \langle x,y \rangle  \right| \leq \left| \left| x \right|  \right| \cdot \left| \left| y \right| \right|
$$
$$
\sum_{i}^n \frac{1}{n}x_{i} \leq \sqrt{ \sum_{i}^n x_{i}^2} \cdot \sqrt{ \sum_{i}^n \frac{1}{n^2} }
$$

$$
\sum_{i}^n \frac{1}{n}x_{i} \leq \sqrt{ \sum_{i}^n x_{i}} \cdot \sqrt{ n\cdot\frac{1}{n^2} } = \sqrt{ \sum_{i}^n x_{i}} \cdot  \sqrt{ \frac{1}{n} } = \sqrt{\frac{1}{n}\sum_{i=1}^nx_{i}^2}
$$
$$
A \leq B
$$

Pravou stranu jsme upravili tak,  aby se rovnala  $B$. Tvrzeni je dokazano.

---
3. **(12 bodů)** Stopa čtvercové matice je definována jako:
   $$
   \text{trace}(A) = \sum_i a_{ii}.
   $$
   Ukažte, že platí:
   - **(4 body)** $\text{trace}(A)^2 \leq n \cdot \text{trace}(A^T A)$,

$B = A^TA$
$$
\left( \sum_{i}a_{ii}\right)^2 \leq n\cdot \sum_{i}  b_{ii}
$$

Nejdrive rozepiseme hodnoty pro prvky v $B$:
$$
b_{ij} = \sum_{k=1} a_{ik}^Ta_{kj} =  \sum_{k=1} a_{ki}a_{kj}
$$
$$
b_{ii} = \sum_{k} a_{ki}^2 
$$

Dosadime zpatky:
$$
\sum_{i}a_{ii} \cdot \sum_{j}a_{jj}  \leq n\cdot \sum_{i} \sum_{k} a_{ki}^2 
$$
$$
(\text{trace}(A))^2 \leq n \sum_{i} \sum_{k} a_{ki}^2
$$

Dosadime do CS kde $a=\{a_{11},\dots,a_{nn}\}$ a $y=\{1,1,\dots,1\}$.

$$
\left| \langle a,y \rangle  \right| \leq \left| \left| a \right| \right| \cdot \left| \left| y \right| \right|
$$

$$
|\text{trace}(A)| \leq \sqrt{ \sum_{i=1}^n a_{ii}^2 } \cdot \sqrt{ n }
$$
$$
|\text{trace}(A)| \leq \sqrt{ n  \sum_{i=1}^n a_{ii}^2 } 
$$

Protoze CS muzeme upravit na:
$$

\left| \langle x,y \rangle  \right|^2 \leq \left| \left| x \right|  \right|^2 \cdot \left| \left| y \right| \right|^2
$$
Plati:
$$
(\text{trace}(A))^2 \leq n \sum_{i=1}^n a_{ii}^2
$$

Ted musime dokazat ze:

$$
n \sum_{i=1}^n a_{ii}^2 \leq n \sum_{i=1}^n \sum_{k=1}^n a_{ki}^2
$$
$$
\sum_{i=1}^n a_{ii}^2 \leq  \sum_{i=1}^n a_{ii}^2 + \sum_{j=1}^n \sum_{k\neq j}^n a_{ki}^2
$$
$$
0 \leq\sum_{j=1}^n \sum_{k\neq j}^n a_{ki}^2
$$
Tohle vždy bude platit, protože sčítáme druhé mocniny reálných čísel, které jsou vždy větší rovny nule.
Tedy:

$$
(\text{trace}(A))^2 \leq n \sum_{i=1}^n a_{ii}^2 \leq n \cdot \sum_{i=1}^n \sum_{k=1}^n a_{ki}^2 = n\cdot\text{trace}(A^TA)
$$



---
   - **(4 body)** $\text{trace}(A^2) \leq \text{trace}(A^T A)$,

$$
B = A^2; b_{ij} = \sum_{k=1}^{n} a_{ik}a_{kj} 
$$
$$
b_{ii} = \sum_{k=1}^{n} a_{ik}a_{ki}
$$
Ziskavame:
$$
\text{trace}(A^2)=\sum_{i=1}^{n} \sum_{k=1}^{n} a_{ik}a_{ki}
$$
$$
\text{trace}(A^TA) =  \sum_{i=1}^{n}  \sum_{k=1}^{n}  a_{ki}^2
$$


$$
\sum_{i=1}^{n} \sum_{k=1}^{n} a_{ik}a_{ki} \leq \sum_{i=1}^{n}  \sum_{k=1}^{n}  a_{ki}^2
$$


Aplikujeme CS na skalarni soucin radkoveho a sloupcoveho prostoru :
$$
\sum_{i=1}^{n} \sum_{k=1}^{n} a_{ik}a_{ki} \leq \sqrt{ \sum_{i=1}^{n} \sum_{k=1}^{n} a_{ik}^2 } \cdot \sqrt{ \sum_{i=1}^{n} \sum_{k=1}^{n} a_{ki}^2 }
$$
Prohodime indexy na leve strane. Timto nic nezmenime:
$$
\sum_{i=1}^{n} \sum_{k=1}^{n} a_{ik}a_{ki} \leq \sqrt{ \sum_{i=1}^{n} \sum_{k=1}^{n} a_{ik}^2 } \cdot \sqrt{ \sum_{i=1}^{n} \sum_{k=1}^{n} a_{ik}^2} 
$$
$$
\text{trace}(A^2) = \sum_{i=1}^{n} \sum_{k=1}^{n} a_{ik}a_{ki} \leq \sqrt{ \left(\sum_{i=1}^{n} \sum_{k=1}^{n} a_{ik}^2 \right)^2} = \sum_{i=1}^{n}\sum_{k=1}^{n} a_{ik}^2 = \text{trace}(A^TA)  
$$


---
   - **(4 body)** $\text{trace}(A^T B) \leq \frac{1}{2} (\text{trace}(A^T A) + \text{trace}(B^T B))$.

Vzorce pro vsechny stopy v prikladu:
$$
\text{trace}(A^TA) =  \sum_{i=1}^{n}  \sum_{k=1}^{n}  a_{ik}^2
$$
$$
\text{trace}(A^TB) = \sum_{i=1}^{n} \sum_{k=1}^{n} a_{ik}b_{ik}
$$
$$
\text{trace}(B^TB) = \sum_{i=1}^{n} \sum_{k=1}^{n} b_{ik}^2
$$

Víme že:
$$
(a-b)^2\geq0
$$
$$
a^2-2ab+b^2 \geq0
$$
$$
\frac{a^2+b^2}{2}\geq ab
$$
A to platí pro $\forall a,b \in \mathbb{R}$.

Tedy pokud si rozepiseme nerovnici, kterou se snazime dokazat:


$$
\sum_{i=1}^{n} \sum_{k=1}^{n} a_{ik}b_{ik} \leq \frac{1}{2}(\sum_{i=1}^{n}  \sum_{k=1}^{n}  a_{ik}^2 + \sum_{i=1}^{n} \sum_{k=1}^{n} b_{ik}^2)
$$
Muzeme nahlednout ze pro kazdy par $i,k \text{ kde } i,k \in [n]$ plati tato nerovnost.
Tedy 
$$
a_{ik}b_{ik} \leq \frac{1}{2}(a_{ik}^2+b_{ik}^2)
$$
Jelikoz to plati pro vsechny $i,k$, muzeme napsat:

$$
\text{trace}(A^TB)=\sum_{i=1}^{n} \sum_{k=1}^{n} a_{ik}b_{ik} \leq \frac{1}{2}(\sum_{i=1}^{n} \sum_{k=1}^{n}a_{ik}^2+\sum_{i=1}^{n} \sum_{k=1}^{n}b_{ik}^2) = \frac{1}{2} (\text{trace}(A^T A) + \text{trace}(B^T B))
$$

---
4. **(10 bodů)** Buď
   $$
   v_1 = (1,1,0)^T, \quad v_2 = (1,1,1)^T.
   $$
   - **(3 body)** Ortonormalizujte vektory $v_1, v_2$.

Vytvorime ortonormalni vektor $a_{1}$ z vektoru $v_{1}$:
$$
a_{1}=\frac{v_{1}}{\left| \left| v_{1} \right| \right|} = v_{1}\cdot \frac{1}{\sqrt{ 2 }}
$$
K ziskani $a_{2*}$ potrebujeme:
$$
a_{2*}=v_{2}-proj_{a_{1}}(v_{2})
$$ 

$$
proj_{a_{1}}(v_{2}) = \frac{\langle v_{2},a_{1} \rangle}{\left| \left| a_{1} \right| \right|} \cdot a_{1}
$$

Skalarni soucin:
$$
\langle v_{2},a_{1} \rangle=\frac{1+1}{\sqrt{ 2 }}= \sqrt{ 2 }
$$
$$
proj_{u_{1}}(v_{2}) = \frac{\langle v_{2},a_{1} \rangle}{\left| \left| a_{1} \right| \right|}=\frac{\sqrt{ 2 }}{1} \cdot \frac{1}{\sqrt{ 2 }} \cdot v_{1} 
$$
Tedy:
$$
a_{2*} = v_{2}-v_{1} = (0,0,1)^T
$$

Normalizujeme $a_{2}*$ :
$$
a_{2}= \frac{a_{2*}}{\left| \left| a_{2*} \right| \right|}=a_{2*} \cdot \frac{1}{1} = (0,0,1)^T
$$
Vysledne vektory.
$$
a_{1}=\frac{1}{\sqrt{ 2 }}u_{1} ; a_{2} = (0,0,1)^T
$$



---

   - **(3 body)** Proveďte ortonormalizaci v opačném pořadí vektorů.



Vytvorime ortonormalni vektor $a_{2}$ z vektoru $v_{2}$:
$$
a_{2}=\frac{v_{2}}{\left| \left| v_{2} \right| \right|} = \frac{1}{\sqrt{ 3 }} v_{2}
$$
K ziskani $a_{1*}$ potrebujeme:
$$
a_{1*}=v_{1}-proj_{a_{2}}(v_{1})
$$ 

$$
proj_{a_{2}}(v_{1}) = \frac{\langle v_{1},a_{2} \rangle}{\left| \left| a_{2} \right| \right|} \cdot a_{2}
$$
Skalarni soucin:
$$
\langle v_{1},a_{2} \rangle = \frac{2}{\sqrt{ 3 }}
$$
$$
proj_{a_{2}}(v_{1}) = \frac{2}{\sqrt{ 3 }} \cdot  \frac{1}{\sqrt{ 3 }} v_{2} = \frac{2}{3}v_{2}
$$
Tedy:
$$
a_{1*} = v_{1} - \frac{2}{3}v_{2} = \left( \frac{1}{3}, \frac{1}{3}, -\frac{2}{3} \right)
$$

Normalizujeme $a_{1*}$ :
$$
a_{1}=\frac{a_{1*}}{\left| \left| a_{1*} \right| \right|} = \frac{a_{1*}}{\sqrt{ \frac{1}{9}+\frac{1}{9}+\frac{4}{9} }}=a_{1*}\cdot \frac{3}{\sqrt{ 6 }}
$$
Vysledne vektory:
$$
a_{1}=\left( \frac{1}{\sqrt{ 6 }}, \frac{1}{\sqrt{ 6 }}, -\frac{2}{\sqrt{ 6 }} \right)^T; \quad a_{2}=\left( \frac{1}{3}, \frac{1}{3}, \frac{1}{3} \right)^T
$$

---
   - **(4 body)** Najděte projekci $x = (0,1,1)^T$ do podprostoru $U = \text{span} \{ v_1, v_2 \}$. Jaká je vzdálenost $x$ od $U$?

$$
a_{1}=\left( \frac{1}{\sqrt{ 2 }}, \frac{1}{\sqrt{ 2 }},0 \right); a_{2} = (0,0,1)^T
$$
$$
proj_{U}(x) = \langle x,a_{1} \rangle \cdot a_{1} + \langle x,a_{2} \rangle a_{2} 
$$

$$
= \frac{1}{\sqrt{ 2 }} \cdot a_{1} + a_{2}
$$
$$
proj_{U}(x) = \left( \frac{1}{2}, \frac{1}{2}, 1 \right)^T
$$

Vzdalenost je dana normou rozdilu x a projekce x do U.

$$
\left| \left| x-proj_{U}(x) \right| \right|=\sqrt{ \frac{1}{4}+\frac{1}{4}+0 } = \sqrt{ \frac{1}{2} }
$$

---
5. **(4 body)** Zortonormalizujte bázi podprostoru $\mathbb{R}^4$ popsaného soustavou:
   $$
   x - y + u + v = 0, \quad x + u = 0.
   $$

Ziskavame:
$$
x = -u; \text{ A tedy: } y=v
$$

Soustavu muzeme zapsat pomoci vektoru:
$$
(x,y,u,v ) = (-u,y,u,y) = u(-1,0,1,0)^T + y(0,1,0,1)^T
$$

To jsou dva vektory, ktere generuji tento podprostor.


Normalizujeme vektor $u =(-1,0,1,0)^T$:
$$
a_{1}=\frac{u}{\left| \left| u \right| \right|}=u\cdot \frac{1}{\sqrt{ 2 }}
$$
K ziskani $a_{2*}$  z vektoru $y = (0,1,0,1)^T$potrebujeme:
$$
a_{2*} = y - proj_{a_{1}}(y)
$$
$$
proj_{a_{1}}(y) = \frac{\langle y,a_{1} \rangle}{\left| \left| a_{1} \right| \right|}\cdot a_{1} 
$$

$$
\langle y,a_{1} \rangle = 0
$$
To znamena, ze je jiz ortogonalni protoze $y$ je kolme na $a_{1}$,
Tedy $a_{2*}=y$

Normalizace $y$ :
$$
a_{2} = \frac{y}{\left| \left| y \right| \right|} = y \cdot \frac{1}{\sqrt{ 2 }}
$$
Vysledne vektory:
$$
a_{1}=\left( -\frac{1}{\sqrt{ 2 }}, 0, -\frac{1}{\sqrt{ 2 }},0 \right); a_{2}= \left( 0,-\frac{1}{\sqrt{ 2 }}, 0, \frac{1}{\sqrt{ 2 }}  \right)
$$



