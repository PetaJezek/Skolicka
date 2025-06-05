
# Definice:
- Výpočetní model RAM
	- Proste teoretický model
	- Má nějaké operace
	- To není tak složité ig

-  Čas a prostor konkrétního výpočtu
	- proste jak dlouho to trva a kolk to zere pameti bro
	- to snad umis
- Asymptoticka notace
	- O je nejhorsi pripad
	-  Omega je nejlepsi 
	-  Theta je nejlepsi a nejhorsi

- BFS 
	- klasika fronta jezis
	- Spravnost: V kazde iteraci se uzavre jeden otevreny vrchol. Ten uz nikdy byt otevreny nemuze takze maximalne n krat se muze opakovat
	- Projdeme az vsechny vrcholy a vsechny hrany takze slozitost je O(V+E)
- DFS
	- Proste do hloubky, misto fronty zasobnik
	- mas tam in and out
	- Spravnost je vlastne stejna jako BFS. Proste vsechny vrcholy se jednou zavrou.  A pote uz nemuzou byt otevreny
- Klasifikace hran v DFS
	- No tohle je celkem crazy
	- Stromová, dopředná, příčná, zpětná
- Hledání mostů
	- Tak tady jde o to,  že most je hrana která není na kružnici
	- Jak zjistíme, že je v neorientovanem grafu hrana kružnice? No Potřebujeme vědět jeslti z podstromy $y$ se dostaneme do nebo nad vrchol $x$. Tedy jestli z něj existuje zpětná hrana.  To spočítáme tak, že si budeme u každého podstromu pomatovat pamatovat jeho $low(v)$, coz je nejnizsi $in(t)$ do ktereho vede z podstromu v zpetna hrana. A pak se staci kouknout jestli $low(y) \lt in(y)$. To znamená, že se dokážu vrátit z podstromu y víš ve stromu než y. Ted minimálně do x. Což znamená že to je kružnice a není to most.



- Detekce cyklů pomocí DFS
	- Jednoduše pokud dfs nalezne zpětnou hranu, graf obsahuje cyklus
- DAG 
	- Proste acyklický graf. 
	- Má zdroj a stok. Když vezmu libovolný vrchol tak někde musím skončit když půjdu po hranách. A když hrany otočím tak zase někdy skončím. To je zdroj. Pokud by se vrcholy někdy opakovaly tak existuje cyklus a není to DAG
	- To znamená, že muzeme vytvorit nejake tologicke usporadani. S tim ze poradi v nemz DFS uzavira vrcholy je tomuto usporadani opacne. To plati protoze pro každou hranu $xy$ platí $in(x) \lt in(y)$. 

- inkluze podle topoligeckeho usporadani
	- Pocet cest mezi dvema vrcholy v DAGu
	- Proste indukcne nevim co vic chces. Kdyz to zname pro vrcholy pred tim hledanym v topoligckem poradi tak to muzeme dopocitat pro nej

- Rozklad grafu na komponenty souvislosti
	- Nejdriv udelame $G^{t}$, kde se prohodili stoky a zdroje. No pak rojzjedeme opakovane dfs do te doby nez obsahneme vsechny vrcholy. Kdyz vrchol zavreme pridame ho do zasobniku. Pak je mame serazene podle outu vzestupne pro $G$ (pro $G^{t}$ sestupně). A pak rozjizdime DFS na vrcholy v zasobniku pokud nejsou prirazene do komponenty. A takhle prirardime vsechny vrcholy do komponent souvislosti


- Vzdalenost v grafu
	- bude pocitana pomoci ohodnoceni hran.  Tedy vzdalenost bodu $x ,y$ je součet všech hran cesty od x do y

- Trojúhelníková nerovnost
	-  $d(u,v) \leq d(u,w)+d(w,v)$
	- pokud je jedna ze vzdalenosti na pravo nekonecno, nerovnost plati
	-  Jinak slozeni nejkratsi uw cesty a wv cesty je nejaky uv-sled a ten nemuze byt kratsi nez uv cesta.


- Dijskrta 
	- To snad ani nemusim vysvetlovat 
	- Ale slozitost je O ($n^{2}$)
	-  S binarni haldou s funkcema decrease extractMin a insert slozitost je $\log n(m+n)$.
	-  Vsechny tyto funkce trvaji $\log n$ a zbyle veci trvaji $O(m+n)$
	-
- Obecný relaxační algoritmus
	- Proste dijkstra akorát místo vybírání vrcholu s nejmenším budíkem vybíráme náhodně.

- Bellman-Ford 
	- No tady jsme trochu v hajzlu. Proste skonci po $\left| N \right|-1$ krocich. Relaxujes dokud neco menis. Pokud algo nezkonci tak obsahuje zaporny cyklus
	- Slozitost je $O(nm)$
	
- Floyd-Warshall
	- Vzdalenost vsech vrcholu od vsech vrcholu
	- Cool trik vole pocitas to v jedny matici a ver ze to funguje. 
	- Slozitost je $O (n^{3})$ a pametova je jen kvadraticka


- Jarnikuv algoritmus
	- absolutne nadherny algoritmus 
	- Vlastne funguje díky řezovému lemmatu ktere je taky pekne
	- Klasicka verze bezi v $O(mn)$
	-  Pokud pouzijeme haldu a budeme si pomatovat jen sousedy naseho stromu tak je slozitost $O(m\log n)$
- Veta o jedinečnosti minimální kostry
	- Ta je u souvislého grafu s unikátními vahami hran dána. Protože existuje minimum váhy minimalni kostry.
	- Z řezového lemmatu a jarnikova algoritmu vyplývá, že vzdycky existuje jen jedna a jarnik ji najde 
- Borůvkův algoritmus
	- Najde minimalni kostru v $O(m\log n)$
	- Vlastne jarnik akorat to dela pro vsechny vrcholy najednou
	- Takze po log n iteracich se vsechny vrcholy spoji
- Kruskalův algoritmus
	- No proste jde po hranach po jejich ohodnecni od nejmensiho po nejvetsi
	- Pokud vytvori cyklus pridanim te hrany tak ji skipuje. Takhle jde dokud vsechny vrcholy nejsou pridane
	- Je to nahovno. Ale pokud pouzijeme UnionFind s kerikama tak to zacne hitovat. 
	- Invariant: Keřík hloubky h obsahuje alespoň 2h vrcholů. 
	- Casova slozitost union a find je log n pro tyto keriky 
	- Takze kruskaluv algoritmus najde tu kostru v case $O(m\log n)$

- BVS
	- Bro binarni vyhledavaci strom je bread and butter fosho
	- JEN BACHA NA DELETE
- Dokonale vyvazeny strom
	- Proste se pocet prvku v levem podstromu a pravem lisi max o jeden
	- Plati pro vsechny prvky
	- Coz je celkem crazy takze proto zmensime podminku 
- AVL Stromy
	- Musi splnovat to co dokonale  vyvazene stromy akorat misto poctu prvku jde o hloubku. Pak se nazývá hloubkově vyvážený
	- Slozitost operaci find insert delete  je log n. A ma hloubku log n. Ten dukaz je crazy. Pomoci fibbonaciho posloupnosti ig

- ab stromy
	- maji hloubku log n. Pocet klicu roste exponencialne, takze hloubka musi rust maximalne logaritmicky. Vic ti nereknu
	- nejlepsi je vyber a, 2b nebo a 2b-1 
-  Dynamicke rozsireni tabulky
	- Vyjde ze amortizovane to trva $O(n)$. Ale nevim ani jak jinak nez amortizovane to zpocitat tbh. 
- MergeSort
	- Porste pulis a slevas a pulis a slevas
	- 
- Karacabuv algoritmus
	- nasobeni lepe. TO si pamatujes

- Kucharkova veta / Master theorem
	- Vypocet slozitosti rekurzivnich algoritmu
	- Mozna se koukni na video dukaz
	- Podle $q  = \frac{a}{b^{c}}$: Pokud $q=1$ Slozitost je $O(n^{c}\log n)$. Pokud $q\lt 1$  Složitost je $O(n^{c})$. Jinak slozitost je $O(n^{\log_{b}a})$
- 

