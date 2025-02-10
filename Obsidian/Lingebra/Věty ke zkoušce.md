Seznam vět ke zkoušce z Lineární algebry 1.

- Frobeniova věta
Pokud rank A = rank Ab. A má jednoznačné řešení \ je regulární
- O existenci inverzní matice
Inverzní matice ma splnovat 
A krat inv = I
protože A je regulární tak máme jednoznačné řešení Ax = ei
Pro každý sloupec získáme řešení.  Tyto řešení dosadíme do matice
xi ..... xn a to je naše inverzní matice

Důkaz, že A krat inverze je I. 

Akrát A -1 j = a (A-1)j = Axj = I*j




- Jedna rovnost stačí
- O znaménku složení permutace a transpozice
I J  jsou bud v jednom cyklu nebo ne. Pokud jsou tak počet cyklů zvýšíme o jedna a pokud nejsou tak změníme počet cyklů. Znaménko se změní takže sgn(p) = -sgn(p cdot t) = -sgn(t cdot p)
- Malá Fermatova věta

pro libovolné A a prvočíslo p platí A na p-1 = 1 mod p
- O existenci báze

máme vektory v1 ....vm, které generují VP V nad T. 
Pokud jsou tyto vektory lineárně nezávislé, máme hotovo. Pokud nejsou tak můžeme podle tvrzení z přednášky odstranit vektor s indexem k tak, že
span(v1 ... vk-1, vk+1....vm) = span (v1.....vm) 
- Steinitzova věta o výměně + lemma o výměně

lemma o výměně 

máme SG prostoru V a vektor x z V. x = Suma od i do n alphai vi taková že alespon jedno alpha i se nerovná nule. Lze x vymenit s libovolným Vk což je index alphi která se nerovnala nule, a Vektory v .... vk- 1 x v k+1 ... vn bude stále SG.

ze vztahu x = suma od i= 1 do n alphai yi vyjadříme yk.


yk = 1/alphaK (x - suma od i do n kde i se nerovná k alpha i yi)

Ted potřebujeme dokázat že libovolný vektor u v V lze generovat pomocí našeho nového systemu generatoru obsahujícího x.
z = suma od i do n beta i yi = suma od i do n bez k beta i yi + beta k yk = suma od i do n bez k beta i yi + beta k / alpha k (x - suma od i do n kde i se nerovná k alpha i yi)= beta k / alpha k cdot x +  suma od i = 1 do n bez k   (- 0betak / alpha k krat alphai beta i )yi



Steintzova věta:

máme LN vektory v1 .... vn a máme SG u1 ..... um. 
n menší rovno m

existují navzájem různé indexy k1 až kn-m takové že vektory v1 .... vn, uk1 .....ukn-m tvoří SG.

Pomocí indukce podle m:
pokud m = 0. Máme triviálně hotovo.
Předpokládáme platnost pro m-1.
 1) pro spor: n-1 = m

To znamená že vektory v1......vn-1 generují V. To znamená že vn můžeme zapsat jako suma přes i do n-1 alpha i vi. To je spor s tím že v1...vn jsou lineárně nezávislé.

2)  Využijeme lemma o výměně.

xm můžeme vyjádřit jako suma přes i do n-1 alpha i vi + suma  přes j do n - m + 1 beta j u j
A víme že existuje index k pro který platí beta k != 0 protože pokud by všechny bety byly nula tak pak vektory v nejsou LN.

Diky lemma o výměně můžeme uk vyměnit za vn.
Takže vektory x1....xm, v1 .... v k-1, v k +1 ..... v n-m+1 jsou generátory prostoru V.


- Dimenze podprostoru

Podprostor Prostoru V je  W: Pak  platí

dimW menší rovno dim V


- Dimenze spojení a průniku

dim U + dim V = dim(U prunik V) + dim(U+V)

prostě doufej
- Maticové prostory a RREF
Ar je rref tvar

nenulové řádky Ar tvoří bázi RA
sloupce tvoří SA
dim RA = dim SA = r


Protože řádkové úpravy jdou zapsat jako jedna regulární matice. Ar = QA a z přednášky víme že R(QA) = R(A). To znamená že tyto nenulové řádky tvoří bázi RA i RAr


sloupce tvoří SA:
SA tvoří sloupce s indexem p z původní matice A. Jsou to generátory protože v nich jsou všechny pivoty. Jsou lineárně nezávislé protože obsahují pivot.

Sa = r a RA = r takže r = SA = RA



- O dimenzi jádra a hodnosti matice

n - rank(A) = dim(kerA)
n = rank(A) + dim(kerA)


vektory v1 .... vn tvoří dimenzi ker
rozšíříme ker na bázi celého vektorového prostoru o vektory v k+1 ..... v n

To znamená že vektory k+1 až vn generují S(A) protože S(A) = rank(A) = n - k

Získáváme n -k + k = n


Dokázíní že vektory v k+1 až vn tvoří bázi S(A)
generujíctnost ...

LN

- Prosté lineární zobrazení

1) f je prosté
2) Ker f  = o
3) obraz libovolné linearně nezavisle množiny je linearne nezavisla množina

1 => 2 = > 3 = > 1


Pokud je f prosté tak to znamená že každému prvku přiřazujeme pouze jeden prvek. To znamená že jádro f musí obsahovat obshovat jeden a pouze jeden prvek a to je nultý vektor.

x1 ..... xn jsou nezavisle vektory
suma přes i do n alfa i f (x i)  = 0 pak f(suma přes i do n alfa i x i ) = 0 tedy suma přes i do n  alfa i xi musí být v jádru. Takže se to rovná nule. Ale protože jsou linearně nezavislé tak všechny alfy  jsou nula.

Pro spor předpokládáme žeexistují dva různé vektory x,y : f(x) = f(y). To znamená že f(x) - f(y) = 0. tedy f(x-y) = 0.
to znamená že x - y = 0 neboli x = y, to je spor. 

- Maticová reprezentace lineárního zobrazení


Bv[id]bu = matice kde prvky jsou fxj to cely bv


Fx bv = bv fbu cdot [x]Bu
A = bv F bu

x = suma přes i do n alfa i xi 
fx = f (suma přes i do n alfa i x i). = suma přes i do n alfa i f(xi) = suma přes i do n alfa i suma přes j do m a ji y j = suma přes j do n (suma přes i do m alfa i a ij) y j.

(suma přes j do m alfa i a ij) reprezentuje i tou souřadnici f(x) Bv. Můžeme ale také nbnapsat jako  itý řádek A krát [x] bu. což dohromady dává  Fx bv = bv fbu cdot [x]Bu


- Matice složeného lineárního zobrazení

Bg  G CDOT Bu = bg g bv cdot bv f bu

Pro každé x v U platí

(g kolecko f [x])BW = bwgbv cdot (f[x]) bv = bw g bv cdot bv f bu[x] bu. Díky jednoznačnosti linearního zobrazení je matice  bw g bv cdot bv f bu ta hledaná matice.

- Isomorfismus n-dimenzionálních prostorů
Všechny Vektorové prostory dim n jsou isomorfní s T na n.

Protože mají všechny stejnou dimenzi mají stejný počet bází. To znamená že nemůžou generovat mín ani víc než generuje T na n. to znamená že se jedná o bijekci. Je prostá protože souřadnice určují jednozačný vektor.  A je na protože každý vektor je dán jednoznačnou n tici souřadnic.  Bijektivní zobrazení je isomorfismus


- O dimenzi jádra a obrazu

dim Ker f  = dim Ker A

strojíme izomorfismus mezi Ker f a X bu

dim f U = dim SA = rank A

strojíme izomorfismus mezi f U do y bv A opět zobrazení je bijekce 
