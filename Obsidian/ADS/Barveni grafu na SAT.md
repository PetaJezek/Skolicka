
Z prednsaky vime, ze obraveni grafu je od k=3 NP-uplne a to stejne plati pro SAT dle Cookovy vety (tedy ze SAT je NP-uplny.) Tedy je mozne najit prevod. 

Problem 1. : Barveni grafu G nejvyse k barvami.

$V\text{: Mnozina vrcholu G}$
$K\text{: Pocet barev}$
$E\text{: Mnozina hran grafu G}$

Vytvorime si $V\times K$ promennych $x_{i,j}$, kde $i \in V$ a $j\in K$. Tedy vlastne vrchol $i$ ma barvu $j$.

A pro prevod do CNF/SAT musime z techto promennych udelat klauzule.

Pravidla barveni grafu:

Vsechny vrcholy maji barvu.
$$
\forall v\in V: \exists c\in K: x_{v,c} 
$$

Dva sousedi nemaji stejnout barvu.

$$
\forall (v,w) \in E:  x_{v,c} \land x_{w,d} \land c\neq d
$$

Vrchol nemuze mit vic jak jednu barvu. 

$$
\forall v\in V:\forall c,d\in K: x(v,c)\land x(v,d)\implies c=d
$$

PRevod na klauzule:

Prvni pravidlo:

$$
\forall v\in V: (x_{v,j} \lor x_{v,j+1} \lor \dots \lor x_{v,j+k})
$$

Druhe pravidlo:

$$
\forall v,w\in E; \forall c\in K: (\neg x_{v,c} \lor \neg x_{w,c})
$$

Treti pravidlo:
$$
\forall c,d\in K(\neg x_{v,c} \lor \neg x_{v,d})
$$



Dukaz ze se jedna o polynomialni prevod. 

Velikost vstupu prvniho problemu je $O(N+M)$, kde $N$ je pocet vrcholu, a $M$ je pocet hran. Pocet nasich vytvorenych promennych $x_{i,j}$ je $O(N\cdot K)$. Pocet klauzuli je:  

Prvni pravidlo: Pocet $N$ a delka $K$ tedy velikost $O(N\cdot K)$.
Druhe pravidlo: $O(M\cdot K)$
Treti pravidlo: Pro kazdy vrchol musime osetrit vsechy dvojice barev. Tedy velikost je $O\left( N \cdot \frac{K(K-1)}{2} \right)$ coz je vlastne $O(N\cdot K^{2})$

Celkovou velikost muzeme odhadnout na $\approx O(N^{3})$, protoze $K$ nemuze byt vetsi nez $N.$

$N^{3}$ je polynom tedy redukce je polynomiani.



Dukaz prevodu,
Tedy musime dokazat, že graf jde obarvit právě tehdy, když je SAT splnitelný. 
 Nejdříve graf jde obarvit$\implies$

Nastavíme na $true$ promenne $x_{v,c}$ , kde vrchol $v$ je obarven barvou $c$. Ostatni nastavime na false.

Jelikoz jsme nalezli legitimni obarveni, vime ze vsechny pravidla jsou splnena.
Kazdy vrchol ma barvu z K barev - presne jedna promenna v klauzulich prvniho typu budou true, protoze z tretiho pravidla vime, ze vrcholy maji presne jednu barvu. Tedy tyto klauzule pravidla 1 a 3 budou splnitelna. 

Dva sousedi nemaji stejnou barvu -  Klauzule druheho pravidla budou vzdycky true protoze neexistuje dva sousedni body se stejnou barvou.

Tedy pak SAT najde ocisleni promennych, protoze exist



Nyni predpokladame ze existuje ohodnoceni promennych $x_{v,c}$ tak, ze vsechny klauzule jsou splnitelne. 

Z klauzuli pravidla 1 a 3 vyplyva, ze kazdy vrchol  ma presne jednu barvu z K barev. 

A jelikoz jsou splnene i klauzule druheho typu, z toho vyplyva ze zadna dvojice vrcholu, ktere spolu sdileji hranu, nemaji stejnou barvu.

A toto jsou vsechny potrebne podminky, k obarveni grafu. 

Graf je tedy obarvitelny k barvami. 

Tedy tim jsme dokazali ze jsme nalezli funkci f, ktera z problemu obraveni grafu k barvami udela SAT a naopak. 
