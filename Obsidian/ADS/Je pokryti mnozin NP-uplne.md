Musime dokazat dve veci:

Zda je v NP.
A zda je to NP-tezky problem.

1. zda patri do NP?

Pokud dostaneme certifikat, ktery rekne jake mnoziny mame vybrat, staci spocitat zda jich je maximalne $t$ a jeslti jejich sjednoceni obsahuje vsechny prvky $X$. 

Vsechny tyto operace jsou trivialne polynomialni. Tedy Pokryti mnozin patri do NP.


2. NP-tezkost
Dokazeme to pomoci 3DM -> Pokryti mnozin. 

Mame 3DM (prvky a trojice, hledame $q$ disjunktnich trojic). 

Udelame z toho Set Cover takto: 

Mame na vstuptu tri disjunktni mnoziny $W,Y,Z$ kazda o velikost $q$.
A mnozinu trojic $T⊆W×Y×Z$
Existuje $q$trojic  ze se v nich kazdy prvek objevi jednou.

Co je vstup Set Cover. 

Mnozina vsech prvku $U$. $\left| U \right|=3q$  Mnozina mnozin $A$. Kde tedy kazda mnozina je jedna mnozina z $T$.  A $t$ nastavime na $q$, protoze v 3DM hledame $q$ mnozin. 

Dukaz funkcni redukce

Pokud existuje $q$ trojic ktere pokryvaji vsechny prvky naseho univerza, nalezli jsme perfektni 3D parovani a i Set Cover, protoze jsem pokryli vsechny prvky. Pouzili jsme na to presne $q$ mnozin co se rovna $t$. Podminka Set Coveru je splnena. 


DUkaz ze pokud mame set cover mame i perfektni 3D parovani. 

Nalezli jsme set cover, tedy mame maximalne $t=q$ mnozin. Tyto mnoziny pokryvaji cele univerzum prvku $W \cup Y\cup Z$.  To je $3q$ prvku pokrytych $q$ mnozinama. Abychom mohli vybrat $3q$ prvku $q$ mnozinama, musi byt vsechny mnoziny disjunktni, protoze vsech $q$ mnozin maji z predpokladu velikost $3$.  Tyto disjukntni mnoziny odpovidaji nasim hledanym trojcim, takze mame perfektni 3D parovani. 


Tim jsme dokazali obe podminky a tedt Set Cover je NP-uplny problem. 
