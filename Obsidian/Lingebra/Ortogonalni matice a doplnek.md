1.

Důkaz o opaku tvrzení provedu sporem.

Nechť matice $P,Q$ jsou tvořeny vektory z báze $B  \text{ (resp. } C)$. Jelikož matice sčítáme, musí mít stejnou velikost.  Tedy báze $B$ a báze $C$ generují stejný prostor. Nechť v i-tém sloupci matice $P$ je vektor $d=(1,0,\dots,0)$ a v matici $Q$ je vektor $e=(-1,0,\dots,0)$. Oba dva vektory jsou ortonormální, takže jsou i ortogonální. Pokud je ale sečteme, získáme nulový vektor. Z definice vlastních vektorů ale víme, že nulový vektor nemůže být ortogonální, a proto $P+Q$ není ortogonální. 
**Tvrzení neplatí.**


2.
Najděte všechny diagonální ortogonální matice řádu n. Kolik jich je?

Hledám všechny matice $Q^{n \times n}$ pro které platí:
$$
Q^TQ = I
$$
Tyto matice zároveň musí být diagonální, to znamená, že všechny vektory mají pouze jeden prvek (I-tý řádek  má prvek na i-té pozici). Získáváme rovnici:
$$
I_{jj} = \sum_{i=1}^{n} q_{ij}q_{ji}^T= q_{jj}^2 
$$
Toto platí, protože na všech pozicích v obou vektorech jsou nuly, kromě toho když $i=j$. 

Tedy získáváme rovnici  
$$
1 = q^2
$$
$$
q = \pm 1
$$

Tedy máme dvě matice, které splňují naše podmínky jsou:
$$
I, -I
$$

3.
Ortogonální matice  $Q$ obsahuje pouze prvky  $\frac{1}{4}$ a $-\frac{1}{4}$. Jaký je rozměr matice  $Q$?


