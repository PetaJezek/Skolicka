**Příklad 1**

Najděte suprema a infima následujících množin (pokud existují). Rozhodněte, zda mají množiny maxima a minima.

$$F = \{x \in \mathbb{Q} \mid x^2 \leq 2\}$$  
$$G = \{x \in \mathbb{R} \mid x^2 \leq 2\}$$  
$$H = \{z \in \mathbb{R} \mid -z \leq z\}$$  


F nemá maximum resp. ani minimum , protože to je resp. $\pm\sqrt{ 2 }$ a  to neni  v  $\mathbb{Q}$.
Tato hodnota je rovna supremu resp. infimu.


G má maximu resp. minimum a to jest $\pm\sqrt{ 2 }$ . Narozdíl od F je G množina reálných čísel. Víme, že pokud má množina maximum resp. minimum, to se rovná jeho supremu resp. infimu.


H je množina na intervalu $<0 ;\infty)$. Má tedy minimum (infinum) rovno nule. Jelikož není shora množina omezená nemá maximum ani supremum.


**Příklad 2**

Mějme $A, B \subseteq \mathbb{R}$ takové, že $S_A = \sup(A)$, $S_B = \sup(B)$, $I_A = \inf(A)$, $I_B = \inf(B)$. Co lze pak říci o supremech a infimech následujících množin?

$$AB = \{ab \mid a \in A, b \in B\}$$  
$$A \triangle B = (A \setminus B) \cup (B \setminus A)$$  

### AB

O supremu nemůžeme mluvit přesně, protože součin obou suprem nemusí být supremum AB. Pokud je např jedno supremum záporné, výsledné supremum je také záporné. Tedy $\sup(AB) = max(\sup(A)\cdot \sup(B); \inf(A)\cdot\inf(B) )$. Jenže toto taky neplatí. Protože pokud množina A obsahuje pouze záporná čísla a B pouze kladná čísla, supremum AB je pak $\sup(A)\cdot \inf(B)$.  Pokud vše dáme dohromady $\sup(AB) = max(\sup(A)\cdot \sup(B), \inf(A)\cdot\inf(B), \sup(A)\cdot \inf(B), \sup(B)\cdot \inf(A) )$ A opak platí pro infimum:
$\inf(AB) = \min(\sup(A)\cdot \sup(B), \inf(A)\cdot\inf(B), \sup(A)\cdot \inf(B), \sup(B)\cdot \inf(A))$

## $A \triangle B$

Pokud A a B měli stejné supremum resp. infimum, nedá se o něm pro obecné A,B  říct nic, protože nic o těch množinách nevíme.
Pokud ale stejné supremum resp. infimum neměli, znamená to, že buď $\sup(A)>\sup(B)$ a nebo $\sup(B)>\sup(A)$ resp. infimum. Ve finalní množině to větší supremum (menší infimum) určitě bude, protože jinak by byl spor s předpokladem, že mají různá suprema a že to "druhé" je menší. Tedy $\sup(A \triangle B) = max(S_{A},S_{B}) \text{ a} \inf(A \triangle B) = min(I_{A},I_{B})$. 


