$$
X,Y  \dots     \text{Množiny}
$$
Intuice: vztah mezi nimi
$$
X = \{1,2,3\}  \qquad Y = \{2,3,4\}
$$


Pokud jsou X a Y konečné, můžeme vypsat všechny dvojice.

## Systematický popis

*DEF:* nechť x,y jsou množiny, potom kartézským součin X a Y Rozumíme:
$$
X \cdot Y = \{x,y\}: x  \in X, \quad y \in Y   
$$


## Vlastnosti

*DEF:* nechť R je relace na možině x. $$
R \subseteq X x X$$
Řekneme že,
1.  R je _Reflektivní_, pokud $$ \forall x \in X: xRx $$
2. R  je _Symetrická_, pokud $$ \forall x,y \in X: xRy \implies yRx$$
3. R je _Tranzitivní_, pokud $$\forall x,y,z \in X: xRy \land  yRz \implies xRz $$
4. 
Pokud je relace R na množině X, a je Reflektivní, Symetrická a Tranzitvní, potom je R ekvivalence.


DEFINICE:
Nechť R je relace ekvivalnec na množině  X a nechť $$
x \in X$$
Potom Třídou EKVIVALENCE prvku x rozumíme množinu: $$
R[x]:=\{y \in X: xRy\}$$

# Věta (o rozkladu na třídy ekvivalence)
Nechť R je ekvivalence na množině X.
Potom platí:
$$
i) \forall x \in X : R[x] \neq \emptyset
$$
$$
ii) \forall x \in X: [x] = R[y] \qquad \text{Pokud    } xRy \qquad  \text{A }
$$
$$
R[x] \cap R[y] = \emptyset \qquad \text{if x not }  R y
$$
$$
iii) \quad \text{Třídy ekvivlanece jednoznačně určují R. Jinými slovy, známe-li třídy ekvivalence, můžeme jednoznačně zkonstruovat R.}
$$