
# DETERMINANT

Definice: Je-li $A = (a_{ij})$ čtvercová matice řádu $n$ nad tělesem $T$, pak determinant matice A je definován předpisem

$\det(A) = \sum_{\pi \in S_n} sgn(\pi)a_{\pi(1),1}a_{\pi(2),2} \dots a_{\pi(n),n}$

Geometrický význam: Pro reálné matice řádu $n$ určuje determinant, jak zobrazení $f_A$ (určené maticí $A$) mění $n$-dimenzionální objemy
Absolutní hodnota $|\det(A)|$ je rovna objemu rovnoběžnostěnu určeného sloupcovými (nebo řádkovými) vektory matice $A$


Tvrzení: Pro libovolnou čtvercovou matici $A$ platí $\det(A) = \det(A^T)$

Důkaz (myšlenka):


Sčítanec v definici $\det(A^T)$ odpovídající permutaci $\pi$ je $\sgn(\pi)a_{1,\pi(1)}a_{2,\pi(2)} \dots a_{n,\pi(n)}$.


Tento součin lze přeuspořádat na $\sgn(\pi)a_{\pi^{-1}(1),1}a_{\pi^{-1}(2),2} \dots a_{\pi^{-1}(n),n}$.


Vzhledem k tomu, že $\sgn(\pi) = \sgn(\pi^{-1})$, součet přes všechny permutace pro $\det(A^T)$ je stejný jako pro $\det(A)$.

Důsledek: Díky této vlastnosti platí, že všechny vlastnosti determinantu formulované pro řádky matice platí analogicky i pro sloupce

.
Linearita Determinantu

Determinant je lineární funkcí každého svého řádku (nebo sloupce)


Vysvětlení: To znamená, že pokud například jeden sloupec (nebo řádek) rozložíme na součet dvou vektorů, nebo ho vynásobíme skalárem, determinant se chová lineárně.

•

Důkaz (pro sloupec):

◦

Pro součet: $\det(v_1 | \dots | v_i + w_i | \dots | v_n) = \det(v_1 | \dots | v_i | \dots | v_n) + \det(v_1 | \dots | w_i | \dots | v_n)$.

▪

Tato vlastnost vyplývá z roznásobení sumy v definici determinantu. Každý sčítanec v $\det(A)$ je součinem, a pokud se $i$-tý prvek $a_{\pi(i),i}$ v sloupci rozloží na $a'{\pi(i),i} + a''{\pi(i),i}$, pak se celý součin rozdělí na dva a determinant se rozdělí na dva součty.

◦

Pro násobení skalárem: $\det(v_1 | \dots | t v_i | \dots | v_n) = t \det(v_1 | \dots | v_i | \dots | v_n)$.

▪

Tato vlastnost vyplývá z vytknutí skaláru $t$ před sumu v definici determinantu, protože $t$ se nachází v každém $i$-tém činiteli $t a_{\pi(i),i}$ každého sčítance.



Potrebuju se podivat na Cramerovo pravidlo

Adjungovana Matice 
Laplaceuv Rozvoj. Adjungovana matice je ugly



Skalarni soucin:

$$
 ⟨x,x⟩≥0 \text{ a taky plati } 
  $$
  $$  
Bilinearita: ⟨αx+y,z⟩=α⟨x,z⟩+⟨y,z⟩
   $$
   $$ 
Symetrie: ⟨x,y⟩=⟨y,x⟩
$$

Norma odvozena ze skalarniho soucinu:

$$
\left| \left| x \right| \right|=\sqrt{ \langle x,x \rangle  }
$$

### **Cauchy–Schwarzova nerovnost**
$$
∣⟨x,y⟩∣ ≤  \left| \left| x \right| \right| \cdot \left| \left| y \right| \right|
$$
Rovnost nastává právě tehdy, když jsou x,yx, yx,y lineárně závislé.


Ortonormalni baze

Gram-Schmidtova ortonormalizace


Ortogonalni projekce



QR rozklad




Ortogonalni doplnek
