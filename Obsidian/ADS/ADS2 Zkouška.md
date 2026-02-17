# Vyhledávání v textu

## <span style="color:#2ecc71">Definice: Terminologie okolo řetězců</span>
- [x] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**

Nechť $\Sigma$ je konečná abeceda.

- **Slovo (řetězec):** Konečná posloupnost znaků z abecedy $\Sigma$. Délku slova $S$ značíme $|S|$. Prázdné slovo značíme $\epsilon$.
- **Podslovo (substring):** Řetězec $V$ je podslovem $S$, pokud existují řetězce $A, B$ takové, že $S = AVB$.
- **Prefix (předpona):** Řetězec $P$ je prefixem $S$, pokud existuje $B$ takové, že $S = PB$.
- **Suffix (přípona):** Řetězec $E$ je suffixem $S$, pokud existuje $A$ takové, že $S = AE$.

---

## <span style="color:#f1c40f">Algoritmus: Knuth-Morris-Pratt (KMP)</span>
- [x] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**

**Úloha (Jedna jehla v kupce sena):** Najít všechny výskyty vzorku $J$ v textu $S$.

### Princip
Využívá **prefixovou funkci** $\pi$ (zpětná hrana).
1. **Definice $\pi[i]$:** Délka nejdelšího vlastního prefixu části $J[0 \dots i]$, který je zároveň suffixem této části.
2. Při neshodě v textu se nevracíme zpět, ale posuneme se ve vzorku na index $\pi[k-1]$.

### Rozbor korektnosti
Korektnost plyne z definice $\pi$. Víme, že část textu se shodovala s prefixem vzorku. $\pi$ nám říká, jaký menší prefix se shoduje s koncem právě přečtené části, takže můžeme bezpečně přeskočit nemožné pozice. Index v textu nikdy neklesá.

### Složitost
- **Časová:** $O(|J| + |S|)$.
    - Předvýpočet: $O(|J|)$.
    - Vyhledávání: $O(|S|)$ (amortizovaně, index ve vzorku klesne maximálně tolikrát, kolikrát stoupl).
- **Prostorová:** $O(|J|)$ pro pole $\pi$.

---

## <span style="color:#f1c40f">Algoritmus: Aho-Corasicková (AC)</span>
- [x] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**

**Úloha (Více jehel v kupce sena):** Najít výskyty množiny vzorků $\{J_1, \dots, J_k\}$ v textu $S$.

### Princip
Zobecnění KMP na **konečný automat (Trie + Fail hrany)**.
1. **Trie:** Vzorky vložíme do stromu.
2. **Zpětné hrany (Fail):** Pro každý uzel vedou do uzlu reprezentujícího nejdelší vlastní suffix. Počítá se pomocí BFS.
3. **Výstupní hrany:** Zkratky na nejbližší uzel, který ukončuje nějaký vzorek (pro nalezení vzorků uvnitř jiných vzorků).

### Rozbor korektnosti
Automat je vždy ve stavu odpovídajícím nejdelšímu prefixu některého vzorku, který je suffixem přečteného textu. Zpětné hrany zajišťují korektní přechody při neshodě.

### Složitost
- **Časová:** $O(\sum|J_i| + |S| + \text{počet výskytů})$.
- **Prostorová:** $O(\sum|J_i| \cdot |\Sigma|)$.

---

## <span style="color:#f1c40f">Algoritmus: Rabin-Karp (RK)</span>
- [x] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**

**Úloha:** Vyhledávání pomocí **okénkového (rolling) hašování**.

### Princip
1. **Polynomiální haš:** $H(S) = (c_1 x^{k-1} + \dots + c_k x^0) \pmod M$.
2. Spočítáme haš vzorku a prvního okna textu.
3. Posouváme okno v textu a přepočítáváme haš v čase $O(1)$ (odčtení starého, přičtení nového znaku).
4. Při shodě hašů ověříme řetězce znak po znaku (proti kolizím).

### Rozbor korektnosti
Pokud se haše neshodují, řetězce jsou různé. Při shodě hašů musíme ověřit znaky (Las Vegas verze) nebo se spolehnout na malou pravděpodobnost chyby (Monte Carlo verze).

### Složitost
- **Časová (Očekávaná):** $O(|J| + |S|)$.
- **Časová (Worst-case):** $O(|J| \cdot |S|)$ (při mnoha kolizích).
- **Prostorová:** $O(1)$.

---

## <span style="color:#e67e22">Věta: Počet kolizí u okénkového hešování</span>
- [x] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**

### Znění
Nechť $M$ je prvočíslo. Pravděpodobnost, že dva různé řetězce $A, B$ délky $L$ budou mít stejný polynomiální haš modulo $M$ při náhodné volbě základu $x \in \{0, \dots, M-1\}$, je nejvýše $\frac{L}{M}$.

### Důkaz
1. Kolize znamená $H(A) = H(B) \pmod M$, tedy $P_A(x) \equiv P_B(x) \pmod M$.
2. To je ekvivalentní hledání kořenů polynomu $Q(x) = P_A(x) - P_B(x)$ nad tělesem $\mathbb{Z}_M$.
3. $Q(x)$ je nenulový polynom stupně nejvýše $L-1$.
4. Nenulový polynom stupně $d$ nad tělesem má nejvýše $d$ kořenů.
5. Počet "špatných" voleb $x$ je tedy maximálně $L-1$.
6. Pravděpodobnost kolize je $\frac{\text{počet kořenů}}{M} \le \frac{L-1}{M} < \frac{L}{M}$. 

----
# **Toky v sítích**

# Toky v sítích (Kompletní přehled)

---

## <span style="color:#2ecc71">Definice: Síť, tok, přebytek, velikost toku</span>
- [x] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**



- **Síť:** Čtveřice $(G, z, s, c)$, kde $G=(V,E)$ je orientovaný graf, $z \in V$ je **zdroj**, $s \in V$ je **spotřebič** (stok) a $c: E \to \mathbb{R}^+_0$ jsou **kapacity**.
- **Tok (Flow):** Funkce $f: E \to \mathbb{R}^+_0$ splňující:
    1.  **Omezení kapacitou:** $0 \le f(e) \le c(e)$ pro $\forall e \in E$.
    2.  **Kirchhoffův zákon (Zachování toku):** Pro každý vrchol $v \in V \setminus \{z, s\}$ platí:
        $$\sum_{(u,v) \in E} f(u,v) = \sum_{(v,w) \in E} f(v,w)$$
        (Přítok se rovná odtoku).
- **Přebytek (Excess) $e(v)$:** Rozdíl mezi přítokem a odtokem ve vrcholu $v$.
  $$e(v) = \sum_{(u,v) \in E} f(u,v) - \sum_{(v,w) \in E} f(v,w)$$
  (U platného toku je $e(v) = 0$ všude kromě $z, s$).
- **Velikost toku $|f|$:** Čistý odtok ze zdroje (nebo přítok do spotřebiče).
  $$|f| = e(s) = -e(z)$$

---

## <span style="color:#2ecc71">Definice: Řez, kapacita řezu</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**



- **Řez:** Rozklad množiny vrcholů $V$ na dvě disjunktní množiny $Z$ a $S$ takové, že $z \in Z$ a $s \in S$.
- **Kapacita řezu $C(Z,S)$:** Součet kapacit hran vedoucích **ze** $Z$ **do** $S$. Hrany jdoucí opačně (ze $S$ do $Z$) se do kapacity nepočítají.
  $$C(Z,S) = \sum_{u \in Z, v \in S} c(u,v)$$

---

## <span style="color:#e67e22">Věta: Velikost toku se dá měřit na každém řezu</span>
- [ ] 🟢 **Umím**
- [x] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**

**Znění:** Pro libovolný tok $f$ a libovolný řez $(Z,S)$ platí, že velikost toku $|f|$ je rovna čistému toku přes tento řez.
$$|f| = \sum_{u \in Z, v \in S} f(u,v) - \sum_{v \in S, u \in Z} f(v,u)$$

**Důkaz (náznak):** Sečteme rovnice zachování toku (Kirchhoffa) pro všechny vrcholy $v \in Z$.
- Toky na hranách uvnitř $Z$ se odečtou (jednou přičteny jako výstup z $u$, podruhé odečteny jako vstup do $v$).
- Zbydou jen hrany vedoucí přes hranici řezu.
- Na levé straně rovnice zbyde jen $e(z) = -|f|$ (protože ostatní mají přebytek 0), což po úpravě znamének sedí.

---

## <span style="color:#2ecc71">Definice: Rezerva hrany, nasycená hrana</span>
- [x] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**



- **Nasycená hrana:** Hrana, kde $f(e) = c(e)$.
- **Rezerva hrany $r(u,v)$:** Množství toku, které můžeme poslat z $u$ do $v$, abychom nezporušili podmínky.
  $$r(u,v) = (c(u,v) - f(u,v)) + f(v,u)$$
  *(Volná kapacita směrem tam + tok, který můžeme vrátit směrem zpět).*
- **Reziduální síť $G_f$:** Síť tvořená hranami s kladnou rezervou. Kapacity v $G_f$ jsou rovny rezervám.

---

## <span style="color:#f1c40f">Algoritmus: Ford-Fulkerson (zlepšující cesty)</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**

**Princip:**
1. Začni s nulovým tokem.
2. Dokud existuje **zlepšující cesta** (cesta ze $z$ do $s$ v reziduální síti $G_f$):
   - Najdi úzké hrdlo cesty $\delta = \min r(e)$.
   - Zvyš tok podél cesty o $\delta$ (tam přičti, v protisměru odečti).
**Složitost:** $O(E \cdot |f|)$ pro celočíselné kapacity. Pro racionální konečný, pro reálná nemusí konvergovat.

---

## <span style="color:#e67e22">Věta: Minimální řez je stejně velký jako maximální tok</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**

**(Max-Flow Min-Cut Theorem)**
Následující tři tvrzení jsou ekvivalentní:
1. $f$ je maximální tok.
2. V reziduální síti $G_f$ neexistuje zlepšující cesta ze $z$ do $s$.
3. Existuje řez $(Z,S)$ takový, že $|f| = C(Z,S)$.

**Důsledek:** $|f|_{max} = \min C(Z,S)$.

---

## <span style="color:#2ecc71">Definice: Průtok (čistý tok)</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**

- **Průtok (Net Flow) $f^\Delta$:** Alternativní matematická definice toku, která je **antisymetrická**.
  $$f^\Delta(u,v) = f(u,v) - f(v,u)$$
  Tedy $f^\Delta(u,v) = -f^\Delta(v,u)$.
- Usnadňuje formální zápisy (nemusíme rozlišovat směr hrany, pracujeme s "algebraickým tokem"). Kirchhoffův zákon pak zní: $\sum_{u} f^\Delta(u,v) = 0$.

---

## <span style="color:#e67e22">Věta: Celočíselná síť má celočíselný maximální tok</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**

**Znění:** Pokud jsou kapacity $c(e)$ celá čísla, pak existuje maximální tok $f$, který je na všech hranách celočíselný.
**Důkaz:** Plyne z Ford-Fulkersonova algoritmu.
1. Začínáme s tokem 0 (celé číslo).
2. Rezervy jsou rozdíly celých čísel $\to$ celá čísla.
3. Kapacita zlepšující cesty ($\min$ rezerv) je celé číslo.
4. Přičítáme celé číslo $\to$ tok zůstává celočíselný.

---

## <span style="color:#2980b9">Důležitý příklad: Největší párování v bipartitním grafu</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**



**Algoritmus:**
1. Bipartitní graf s partitami $A, B$.
2. Přidáme zdroj $z$ a hrany $z \to A$ (kapacita 1).
3. Přidáme spotřebič $s$ a hrany $B \to s$ (kapacita 1).
4. Všechny hrany $A \to B$ orientujeme a dáme kapacitu 1 (nebo $\infty$).
5. Spustíme max-flow.
**Vysvětlení:** Díky celočíselnosti bude tok na hranách 0 nebo 1. Hrany mezi $A$ a $B$ s tokem 1 tvoří maximální párování.

---

## <span style="color:#2ecc71">Definice: Blokující tok, vrstevnatá síť</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**



- **Vrstevnatá síť (Layered Network):** Podgraf reziduální sítě.
  - Vrcholy rozděleny do vrstev $V_0, V_1 \dots$ podle BFS vzdálenosti od zdroje.
  - Obsahuje pouze hrany $(u,v)$, kde $v$ je o vrstvu dál než $u$ ($dist(v) = dist(u) + 1$).
- **Blokující tok:** Tok $g$ ve vrstevnaté síti, který nasytí na **každé** cestě ze $z$ do $s$ alespoň jednu hranu. (Nemusí být maximální v celé síti, ale zablokuje všechny nejkratší cesty).

---

## <span style="color:#f1c40f">Algoritmus: Dinicův algoritmus (zlepšující toky)</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**

**Princip:**
1. Dokud existuje cesta v reziduální síti:
2. Sestroj **vrstevnatou síť** (BFS).
3. Najdi v ní **blokující tok** (DFS).
4. Přičti blokující tok k celkovému toku a uprav reziduální síť.
**Složitost:** $O(V^2 E)$. V každé fázi se délka nejkratší cesty prodlouží min. o 1 (max $V$ fází). Hledání blokujícího toku $O(VE)$.

---

## <span style="color:#2ecc71">Definice: Vlna, převedení přebytku po hraně</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**

- **Vlna (Preflow):** Funkce $f$, která splňuje kapacity, ale uvolňuje Kirchhoffův zákon na:
  $$\sum f(\text{dovnitř}) \ge \sum f(\text{ven})$$
  (Do uzlu může vtékat víc, než vytéká $\to$ vzniká kladný přebytek).
- **Převedení přebytku (Push):** Lokální operace. Pokud má vrchol $u$ přebytek a existuje hrana $(u,v)$ s rezervou, pošleme tok z $u$ do $v$.

---

## <span style="color:#f1c40f">Algoritmus: Goldbergův algoritmus (výšky a přebytky)</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**



**Princip (Metoda preflow-push):**
- Udržujeme **vlnu** a **výškovou funkci** $h(v)$ (odhad vzdálenosti do $s$).
- **Invariant:** Tok teče jen "dolů" ($h(u) = h(v) + 1$). Zdroj je vysoko ($h(z)=N$), spotřebič dole ($h(s)=0$).
- **Operace:**
  1. **Push:** Pošli přebytek do nižšího souseda.
  2. **Relabel (Lift):** Pokud mám přebytek a nemám nižšího souseda, zvedni svou výšku na $1 + \min(h(\text{sousedi}))$.
- Končí, když nejsou přebytky (kromě $z,s$).
**Složitost:** $O(V^2 E)$.

---

## <span style="color:#f1c40f">Algoritmus: Goldbergův algoritmus s výběrem nejvyššího vrcholu</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**

- **Heuristika (Highest Label First):** Mezi vrcholy s přebytkem vybíráme k ošetření (Push/Relabel) vždy ten, který má **největší výšku** $h(v)$.
- **Efekt:** Přebytek se "hrne" směrem ke spotřebiči a méně se vrací zpět. Výrazně zrychluje algoritmus.
- **Složitost:** $O(V^2 \sqrt{E})$.



# Algebraické algoritmy (Polynomy a FFT)

## <span style="color:#2ecc71">Definice: Reprezentace polynomu</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**

Polynom $P(x)$ stupně $n-1$ je funkce $P(x) = \sum_{j=0}^{n-1} a_j x^j$.
Máme dva hlavní způsoby, jak ho uložit v paměti:

1.  **Koeficientová reprezentace:**
    - Vektor koeficientů $a = (a_0, a_1, \dots, a_{n-1})$.
    - **Vyhodnocení** v bodě $x_0$: Hornerovo schéma $O(n)$.
    - **Sčítání:** $O(n)$.
    - **Násobení:** $O(n^2)$ (konvoluce).

2.  **Bodová reprezentace (hodnotami):**
    - Množina $n$ dvojic $\{(x_0, y_0), \dots, (x_{n-1}, y_{n-1})\}$, kde $y_k = P(x_k)$ a všechna $x_k$ jsou navzájem různá.
    - **Věta o jednoznačnosti:** Polynom stupně $n-1$ je jednoznačně určen svými hodnotami v $n$ různých bodech.
    - **Sčítání:** $O(n)$ (bod po bodu).
    - **Násobení:** $O(n)$ (bod po bodu: $C(x_k) = A(x_k) \cdot B(x_k)$).
    - **Vyhodnocení v jiném bodě:** Složité (Lagrangeova interpolace $O(n^2)$).

---

## <span style="color:#2ecc71">Definice: Primitivní n-tá odmocnina z jedničky</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**

Pracujeme v tělese komplexních čísel $\mathbb{C}$.
- **n-tá odmocnina z 1:** Číslo $\omega$ takové, že $\omega^n = 1$.
- **Primitivní n-tá odmocnina:** Taková $\omega$, že $n$ je *nejmenší* kladné číslo, pro které $\omega^n = 1$ (generuje všechny ostatní odmocniny).
- **Hlavní primitivní odmocnina:** $\omega_n = e^{2\pi i / n} = \cos(\frac{2\pi}{n}) + i \sin(\frac{2\pi}{n})$.

---

## <span style="color:#e67e22">Věta: Vlastnosti odmocnin z jedničky</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**

Tyto vlastnosti umožňují rekurzi v FFT.
1.  **Krácení (Halving lemma):** Pro sudé $n > 0$ platí $\omega_{dn}^{dk} = \omega_n^k$. Speciálně čtverce $n$-tých odmocnin jsou $(n/2)$-té odmocniny.
    $$(\omega_n^k)^2 = \omega_{n/2}^k$$
    *(Díky tomu se problém velikosti $n$ rozpadne na poloviční podproblémy).*
2.  **Sumace (Summation lemma):** Pro libovolné celé číslo $k$, které není násobkem $n$:
    $$\sum_{j=0}^{n-1} (\omega_n^k)^j = 0$$
    *(Klíčové pro inverzní transformaci – ortogonalita).*

---

## <span style="color:#f1c40f">Algoritmus: Rychlá Fourierova transformace (FFT)</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**

**Úloha:** Převést polynom z koeficientové reprezentace na bodovou v čase lepším než $O(n^2)$.
**Vstup:** Koeficienty $a = (a_0, \dots, a_{n-1})$, kde $n$ je mocnina 2.
**Výstup:** Hodnoty $y_k = P(\omega_n^k)$ pro $k = 0, \dots, n-1$. (Vyhodnocení v $n$-tých odmocninách z jedničky).

### Princip (Divide & Conquer)
Polynom $P(x)$ rozdělíme na sudé a liché koeficienty:
$$P(x) = (a_0 + a_2 x^2 + \dots) + x(a_1 + a_3 x^2 + \dots)$$
$$P(x) = P_{sudé}(x^2) + x \cdot P_{liché}(x^2)$$
Pro vyhodnocení v bodech $\omega_n^k$ potřebujeme vyhodnotit $P_S$ a $P_L$ v bodech $(\omega_n^k)^2$. Díky Halving lemmatu víme, že $(\omega_n^k)^2$ jsou právě $(n/2)$-té odmocniny.
Tedy rekurzivně voláme FFT pro poloviční polynomy.

### Kroky
1. Pokud $n=1$, vrať $a_0$.
2. $\omega_n \leftarrow e^{2\pi i / n}$, $\omega \leftarrow 1$.
3. $y^{[S]} \leftarrow FFT(a_0, a_2, \dots, a_{n-2})$ (sudé).
4. $y^{[L]} \leftarrow FFT(a_1, a_3, \dots, a_{n-1})$ (liché).
5. Pro $k = 0$ do $n/2 - 1$:
    - $y_k = y^{[S]}_k + \omega \cdot y^{[L]}_k$
    - $y_{k+n/2} = y^{[S]}_k - \omega \cdot y^{[L]}_k$ (využití symetrie $\omega_n^{k+n/2} = -\omega_n^k$)
    - $\omega \leftarrow \omega \cdot \omega_n$
6. Vrať $y$.

### Složitost
- **Časová:** $T(n) = 2T(n/2) + O(n) \implies O(n \log n)$.
- **Prostorová:** $O(n \log n)$ nebo $O(n)$ dle implementace.

---

## <span style="color:#f1c40f">Algoritmus: Inverzní FFT a Interpolace</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**

**Úloha:** Máme hodnoty v odmocninách, chceme koeficienty.
**Princip:** Dá se zapsat jako násobení Vandermondovou maticí $V_n$. Inverzní matice $V_n^{-1}$ má velmi podobný tvar, jen prvky jsou $\omega^{-kj}$ místo $\omega^{kj}$ a celé je to přenásobeno $1/n$.
**Algoritmus:**
1. Zavoláme stejnou funkci FFT, ale místo $\omega_n$ použijeme $\omega_n^{-1}$ (což je komplexně sdružené číslo).
2. Výsledek vydělíme $n$.
**Složitost:** $O(n \log n)$.

---

## <span style="color:#f1c40f">Algoritmus: Násobení polynomů pomocí FFT</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**

**Úloha:** Vynásobit dva polynomy $A(x)$ a $B(x)$ stupně $n$. Výsledný polynom $C(x)$ má stupeň $2n$.
**Klasický postup:** $O(n^2)$.
**Pomocí FFT:** $O(n \log n)$.

### Postup
1.  **Zarovnání (Padding):** Rozšíříme koeficienty $A$ a $B$ nulami na délku $2n$ (aby se tam vešel výsledek a bylo to mocnina 2).
2.  **Vyhodnocení (FFT):** Spočítáme DFT (Diskrétní Fourierovu Transformaci) pro oba vektory.
    - $y_A = FFT(A, 2n)$
    - $y_B = FFT(B, 2n)$
    - Tím získáme bodovou reprezentaci.
3.  **Bodové násobení:** Vynásobíme hodnoty ve odpovídajících bodech.
    - $y_C[k] = y_A[k] \cdot y_B[k]$ pro všechna $k$.
    - Čas $O(n)$.
4.  **Interpolace (Inverse FFT):** Převedeme zpět na koeficienty.
    - $C = InverseFFT(y_C, 2n)$.

### Věta o konvoluci
Násobení polynomů odpovídá konvoluci jejich koeficientů.
Věta říká: **Konvoluce v časové oblasti odpovídá bodovému násobení ve frekvenční oblasti.**



# Hradlové a komparátorové sítě

## <span style="color:#2ecc71">1. Hradlová síť</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**



[Image of boolean circuit diagram]


**Definice:**
- **Hradlová síť:** Orientovaný acyklický graf (DAG).
    - **Vstupní vrcholy:** $x_1, \dots, x_n$ (stupně 0).
    - **Hradla:** Vrcholy počítající logické funkce (AND, OR, NOT). Obvykle mají vstupní stupeň (fan-in) 1 nebo 2.
    - **Výstupní vrcholy:** Určené vrcholy, které nesou výsledek.
- **Velikost sítě $S(n)$:** Počet hradel (odpovídá sekvenčnímu času nebo počtu procesorů).
- **Hloubka sítě $D(n)$:** Délka nejdelší cesty od vstupu k výstupu (odpovídá paralelnímu času).

---

## <span style="color:#f1c40f">2. Sčítání přirozených čísel hradlovou sítí</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**

**Úloha:** Sečíst dvě $n$-bitová čísla $A$ a $B$. Výstup je $S$ ($n+1$ bitů).
**Problém naivní sčítačky (Ripple Carry):** Přenos (carry) se šíří postupně bit po bitu. Hloubka $O(n)$ – to je pomalé.

**Řešení: Carry Lookahead Adder (Sčítačka s předvídáním přenosu)**
1.  **Generování a Propagace:** Pro každý bit $i$ spočteme v čase $O(1)$:
    - $g_i = a_i \land b_i$ (Generate - přenos vzniká tady).
    - $p_i = a_i \lor b_i$ (Propagate - přenos tudy projde). (Někdy $a_i \oplus b_i$).
2.  **Výpočet přenosů:** Přenos $c_i$ platí, pokud ($g_i$ platí) NEBO ($p_i$ platí A $c_{i-1}$ platí).
    $$c_i = g_i \lor (p_i \land c_{i-1})$$
    Tento vzorec vypadá jako **Prefixový součet** (operace skládání funkcí).
3.  **Použití hradlového stromu:** Pomocí vyváženého stromu (prefix sum) spočítáme všechny $c_i$ naráz.

**Složitost:**
- **Hloubka:** $O(\log n)$.
- **Velikost:** $O(n)$.

---

## <span style="color:#f1c40f">3. Násobení přirozených čísel hradlovou sítí</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**

**Úloha:** Vynásobit dvě $n$-bitová čísla. Výsledek má $2n$ bitů.
**Princip (Sčítání $n$ čísel):** Násobení je vlastně součet $n$ posunutých řádků (jak na papíře). Potřebujeme rychle sečíst $n$ čísel.

**Algoritmus (Carry Save Adder / Wallace Tree):**
1.  **Redukce 3 na 2:** Umíme sečíst 3 čísla (řádky) na 2 čísla v čase $O(1)$ (hloubka 1).
    - Použijeme $n$ "full adderů" vedle se, ale nešíříme přenos do strany, nýbrž ho uložíme do druhého čísla.
    - Výsledek: *Suma* (bity bez přenosu) a *Carry* (přenosy). Platí $X+Y+Z = Suma + Carry$.
2.  **Strom redukcí:**
    - Máme $n$ čísel.
    - Rozdělíme na trojice $\to$ zredukujeme na $2/3 n$ čísel.
    - Opakujeme, dokud nezbydou jen **2 čísla**.
    - Výška stromu je $O(\log_{3/2} n) = O(\log n)$.
3.  **Finále:** Poslední 2 čísla sečteme rychlou sčítačkou (viz bod 2).

**Složitost:**
- **Hloubka:** $O(\log n)$.
- **Velikost:** $O(n^2)$.

---

## <span style="color:#2ecc71">4. Komparátorová síť</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**



**Definice:**
- Síť složená jen z drátů a **komparátorů**.
- **Komparátor:** Bere dva vstupy $x, y$.
    - Horní výstup: $\min(x,y)$.
    - Dolní výstup: $\max(x,y)$.
    - (Pokud $x > y$, prohodí je).

**<span style="color:#e67e22">Věta: Nula-jednotkový princip (0-1 Principle)</span>**
- **Znění:** Pokud komparátorová síť správně setřídí každou posloupnost složenou jen z **nul a jedniček**, pak správně setřídí každou posloupnost libovolných čísel.
- **Význam:** Pro důkaz korektnosti třídicích sítí stačí uvažovat vstupy $0/1$. Výrazně to zjednodušuje důkazy (např. u bitonického třídění).

---

## <span style="color:#f1c40f">5. Bitonické třídění komparátorovou sítí</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**



**Definice Bitonické posloupnosti:**
Posloupnost, která nejprve roste a pak klesá (nebo vznikne cyklickým posunem takové posloupnosti). Např. `1, 4, 8, 6, 2` nebo `0, 0, 1, 1, 0`.

**Algoritmus (Bitonic Sort):**
Stavíme rekurzivně (Divide & Conquer).
1.  **Bitonická míchačka (Bitonic Merger):**
    - Vstup: Bitonická posloupnost délky $n$.
    - Výstup: Setříděná posloupnost.
    - Princip: Porovnej $x_i$ a $x_{i+n/2}$. Menší prvky dej doleva, větší doprava. Tím vzniknou dvě poloviční bitonické posloupnosti. Rekurzivně zavolej na obě půlky.
2.  **Třídicí síť:**
    - Chceme setřídit libovolná data.
    - Rozdělíme na půl, setřídíme levou (rostoucí) a pravou (klesající).
    - Tím vznikne jedna velká bitonická posloupnost.
    - Zavoláme Bitonic Merger.

**Složitost:**
- **Hloubka:** $O(\log^2 n)$. (Míchačka má $\log n$, voláme ji v hloubce $\log n$).
- **Velikost:** $O(n \log^2 n)$.

---

# Geometrické algoritmy

## <span style="color:#2ecc71">1. Konvexní obal (Convex Hull)</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**



**Definice:** Nejmenší konvexní množina obsahující dané body $S$.
**Algoritmus: Graham Scan**
1.  **Pivot:** Najdi bod s nejmenším $Y$ (a $X$).
2.  **Sort:** Seřaď ostatní body podle úhlu k pivotu.
3.  **Scan:** Přidávej body do zásobníku. Pokud nová hrana tvoří "pravotočivou" zatáčku (dovnitř), vyhazuj body ze zásobníku, dokud není zatáčka levotočivá.
**Složitost:** $O(N \log N)$ (kvůli třídění).

---

## <span style="color:#f1c40f">2. Průsečíky úseček (Bentley-Ottmann)</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**



**Úloha:** Najít všechny průsečíky množiny úseček.
**Algoritmus: Zametání roviny (Plane Sweep)**
- **Zametací přímka:** Svislá čára jede zleva doprava.
- **Stav (BST):** Udržuje úsečky, které přímka protíná, seřazené podle $Y$.
- **Události (Fronta):** Začátek úsečky, Konec úsečky, Průsečík.
- **Akce:**
    - *Začátek:* Vlož do BST, zkontroluj průsečík se sousedy.
    - *Konec:* Vyndej z BST, zkontroluj průsečík nových sousedů.
    - *Průsečík:* Prohoď úsečky v BST, zkontroluj nové sousedy.
**Složitost:** $O((N+K) \log N)$, kde $K$ je počet průsečíků.

---

## <span style="color:#2ecc71">3. Voroného diagram</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**



**Definice:** Rozdělení roviny na oblasti. Každá oblast náleží jednomu bodu (sítu) a obsahuje místa, která mají k tomuto sítu blíže než k jakémukoliv jinému.
- Hranice jsou osy úseček. Uzly jsou středy kružnic opsaných.
**Vztah:** Duální graf k **Delaunayho triangulaci**.
**Algoritmus (Fortune):** Zametání roviny s "plážovou čárou" (křivka z parabolických oblouků).
**Složitost:** $O(N \log N)$.

---

## <span style="color:#f1c40f">4. Lokalizace bodu v mnohoúhelníkové síti</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**

**Úloha:** Máme rovinu rozdělenou na oblasti (mnohoúhelníky). Pro daný bod $(x,y)$ chceme rychle najít, ve které oblasti leží.
**Metoda: Proužková dekompozice (Slab decomposition)**
1.  Veď svislé přímky přes každý vrchol sítě.
2.  Tím vzniknou svislé **proužky (slabs)**.
3.  V uvnitř každého proužku se nic nemění – úsečky se neprotínají a jdou od kraje ke kraji. Jsou jasně seřazené zdola nahoru.
4.  **Vyhledávání:**
    - Najdi správný proužek podle $x$ souřadnice (binární vyhledávání nad $x$-souřadnicemi vrcholů).
    - V proužku najdi správnou oblast (binární vyhledávání mezi úsečkami v proužku).
**Složitost:** $O(\log N)$ dotaz. Ale paměť je $O(N^2)$ (naivně). Pro zlepšení paměti na $O(N)$ potřebujeme **Semipersistentní strom**.

---

## <span style="color:#f1c40f">5. Semipersistentní binární vyhledávací strom</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**



**Motivace:** Vylepšení paměti pro lokalizaci bodu (bod 4).
**Problém:** Sousední proužky v dekompozici jsou si velmi podobné (liší se jen v úsečkách, které v daném vrcholu začínají/končí). Nechceme ukládat celý strom pro každý proužek zvlášť.

**Definice:** Datová struktura, která si pamatuje svou historii.
- **Semipersistentní:** Můžeme číst staré verze, ale měnit jen tu nejnovější.

**Implementace (Path Copying / Fat Nodes):**
- Když měníme uzel ve stromu (např. vkládáme úsečku při přechodu do nového proužku), nepřepisujeme ho.
- Vytvoříme **kopii** tohoto uzlu a kopii cesty k němu. Zbytek stromu (který se nemění) sdílíme s minulou verzí.

**Použití pro lokalizaci:**
- Zametáme rovinu zleva doprava.
- Čas $T$ odpovídá souřadnici $X$.
- Strom v čase $T$ reprezentuje uspořádání úseček v daném proužku.
- **Výsledek:** Paměť $O(N)$, Dotaz $O(\log N)$, Preprocessing $O(N \log N)$.


---
# NP-úplnost a Redukce 

## <span style="color:#2ecc71">1. Rozhodovací problémy a Bipartitní párování</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**

**Rozhodovací problém:**
- Problém, kde je výstupem pouze **ANO** nebo **NE** (1/0).
- Teorie složitosti (třídy P, NP) je stavěna primárně na rozhodovacích problémech.
- *Příklad:* Místo "Najdi nejkratší cestu" se ptáme "Existuje cesta délky maximálně $K$?".

**Bipartitní párování jako rozhodovací problém:**
- **Vstup:** Bipartitní graf $G=(U \cup V, E)$ a číslo $k$.
- **Otázka:** Existuje v $G$ párování velikosti alespoň $k$? (Tj. $k$ hran, které nemají žádný společný vrchol).
- **Složitost:** Patří do **P**. (Lze vyřešit tokem v síti nebo Hopcroft-Karpem).

**Kódování vstupu:**
- Vstup musí být zapsán jako řetězec bitů/znaků.
- Graf se kóduje obvykle **maticí sousednosti** ($N^2$ bitů) nebo **seznamem sousedů**.
- Číslo $k$ se kóduje binárně.
- Podstatné je, že velikost vstupu je polynomiální vůči počtu vrcholů.

---

## <span style="color:#2ecc71">2. Vlastnosti převoditelnosti (Redukce)</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**



**Definice ($A \le_P B$):** Problém $A$ se redukuje na $B$, pokud existuje polynomiální funkce $f$ (překladač), která převede vstup $A$ na vstup $B$ tak, že odpovědi se shodují.

**Klíčové vlastnosti:**
1.  **Reflexivita:** $A \le_P A$. (Triviální, funkce $f$ je identita).
2.  **Tranzitivita:** Pokud $A \le_P B$ a $B \le_P C$, pak $A \le_P C$.
    - *Důkaz:* Složení dvou polynomů je polynom. Vstup $x$ převedu na $f(x)$, ten pak na $g(f(x))$.
3.  **Šíření obtížnosti:** Pokud $A$ je těžký (např. NP-úplný) a $A \le_P B$, pak i $B$ musí být těžký.
4.  **Šíření řešitelnosti:** Pokud $B$ je lehký (v P) a $A \le_P B$, pak i $A$ je lehký.

---

## <span style="color:#f1c40f">3. Definice problémů (ZOO)</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**

- **SAT (Splnitelnost):** Je dána booleovská formule (AND, OR, NOT). Existuje dosazení proměnných tak, aby vyšla 1?
- **3-SAT:** Formule je v CNF (konjunktivní normální forma) a každá klauzule (závorka) má **právě 3 literály**.
- **3,3-SAT:** Speciální varianta 3-SATu.
    1.  Každá klauzule má 3 literály.
    2.  Každá proměnná se v celé formuli vyskytuje **maximálně 3x**.
    - *Význam:* I tato omezená verze je NP-úplná (důležité pro redukci na 3D párování).
- **Nezávislá množina (IS):** Graf $G$ a číslo $k$. Existuje $k$ vrcholů, mezi kterými nevede žádná hrana?
- **Klika (Clique):** Graf $G$ a číslo $k$. Existuje $k$ vrcholů, které jsou všechny propojené (úplný podgraf)?
- **3D-Párování (3DM):**
    - Množiny $X, Y, Z$ (stejně velké, velikost $n$).
    - Množina trojic $T \subseteq X \times Y \times Z$.
    - Otázka: Lze vybrat $n$ trojic tak, aby každý prvek z $X, Y, Z$ byl použit právě jednou?
    - *Rozdíl:* Na rozdíl od 2D párování (které je v P), je 3D párování **NP-úplné**.

---

## <span style="color:#e67e22">4. Převody mezi SAT variantami</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**

**A. SAT $\to$ 3-SAT:**
- Problém: Klauzule může být moc dlouhá, např. $(x_1 \lor x_2 \lor x_3 \lor x_4 \lor x_5)$.
- Řešení: "Roztrháme" ji pomocí nových pomocných proměnných $y$.
- $(x_1 \lor x_2 \lor y_1) \land (\neg y_1 \lor x_3 \lor y_2) \land (\neg y_2 \lor x_4 \lor x_5)$.
- Formule je splnitelná $\iff$ původní je splnitelná. Délka naroste jen lineárně.

**B. 3-SAT $\to$ 3,3-SAT:**
- Problém: Proměnná $x$ se vyskytuje moc často (např. $k$-krát).
- Řešení: Nahradíme každý výskyt $x$ novou unikátní proměnnou $x_1, x_2, \dots, x_k$.
- Aby se chovaly stejně (byly všechny TRUE nebo všechny FALSE), svážeme je cyklem implikací:
  $(x_1 \implies x_2) \land (x_2 \implies x_3) \dots \land (x_k \implies x_1)$.
- Implikace $(a \implies b)$ se zapíše jako klauzule $(\neg a \lor b)$. Tyto klauzule mají délku 2, což nevadí (doplníme "dummy" proměnnou na 3).

---

## <span style="color:#e67e22">5. Převody Grafové problémy</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**

**A. Klika $\leftrightarrow$ Nezávislá množina (IS):**
- **Klika $\to$ IS:** Vezmeme graf $G$ a sestrojíme **doplněk** $\bar{G}$ (prohodíme hrany a nehrany). Klika v $G$ je IS v $\bar{G}$.
- **IS $\to$ Klika:** Totéž, jen naopak. Vezmeme $G$, uděláme $\bar{G}$. IS v $G$ je Klika v $\bar{G}$.

**B. 3-SAT $\to$ Nezávislá množina (IS):**
- **Konstrukce:** Pro každou klauzuli $(a \lor b \lor c)$ vytvoříme v grafu **trojúhelník** vrcholů.
- **Konflikty:** Pokud je v jednom trojúhelníku $x$ a v jiném $\neg x$, spojíme je hranou (nemůžeme vybrat oba).
- Hledáme IS velikosti $k$ (počet klauzulí). Z každého trojúhelníku musíme vybrat právě jeden vrchol (splněný literál) tak, aby nebyly v konfliktu.

**C. Nezávislá množina $\to$ SAT:**
- Jak zapsat "Existuje $k$ nezávislých vrcholů" pomocí formule?
- **Proměnné:** Pro každý vrchol $v$ jedna proměnná $x_v$ (1 = je v množině).
- **Podmínky (Klauzule):**
    1.  *Nezávislost:* Pro každou hranu $(u,v)$ v grafu přidáme klauzuli $(\neg x_u \lor \neg x_v)$. (Nemůžou být oba vybraní).
    2.  *Velikost:* Musíme zapsat "součet $x_v \ge k$". To se dělá pomocí sčítací sítě převedené do CNF. (Není to triviální na jeden řádek, ale je to polynomiální).

---

## <span style="color:#e67e22">6. Převod 3,3-SAT $\to$ 3D-Párování (3DM)</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**

*Toto je technicky nejnáročnější převod.*

**Myšlenka:**
Chceme sestrojit množinu trojic, která půjde perfektně spárovat právě tehdy, když je formule splnitelná.

1.  **Gadget pro proměnnou:**
    - Proměnná $x$ se vyskytuje max 3x.
    - Vytvoříme kruh z trojic, který má dva stavy: "Lichý" (reprezentuje TRUE) a "Sudý" (reprezentuje FALSE).
    - Tento kruh spotřebuje prvky z množin $X, Y$.
    - Prvky z množiny $Z$ ("přebytečné nožičky") trčí ven a slouží k propojení s klauzulemi.

2.  **Gadget pro klauzuli:**
    - Každá klauzule potřebuje být splněna alespoň jedním literálem.
    - Vytvoříme trojici reprezentující klauzuli, která má v sobě "díry". Tyto díry musí být zaplněny "nožičkami" z gadgetů proměnných.
    - Pokud je proměnná TRUE, její nožička je volná a může "ucpat" díru v klauzuli.

3.  **Garbage collection (Úklid):**
    - 3DM vyžaduje *perfektní* párování (všechny prvky musí být použity).
    - Pokud je formule splněna "moc dobře" (více literálů v klauzuli je true), zbydou nám volné prvky.
    - Přidáme "úklidové trojice", které umožní spárovat i tyto zbylé prvky, aby párování bylo validní.

**Důsledek:**
3,3-SAT je redukovatelný na 3DM $\implies$ **3D-Párování je NP-úplné.**

---

# Jak zvládnout těžký problém

## <span style="color:#2ecc71">1. Strategie pro těžké problémy</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**

Když je problém NP-těžký, nemůžeme čekat, že ho vyřešíme přesně a rychle pro *všechny* vstupy. Máme ale tyto možnosti:
1.  **Speciální vstupy:** Problém je těžký obecně, ale lehký pro specifické grafy (stromy, intervalové grafy...).
2.  **Pseudopolynomiální algoritmy:** Rychlé, pokud jsou čísla na vstupu malá.
3.  **Aproximace:** Slevíme z kvality. Nechceme optimum, stačí nám řešení, které je "dost blízko" a s garancí.
4.  **Parametrizovaná složitost:** Algoritmus je exponenciální jen vůči malému parametru $k$ (např. velikost řešení), ne vůči celému $N$.
5.  **Heuristiky:** Rychlé, často dobré, ale bez garance (např. genetické algoritmy, simulované žíhání).

---

## <span style="color:#f1c40f">2. Nezávislá množina ve stromu</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**

**Problém:** Najít maximální nezávislou množinu (IS). V obecném grafu NP-těžké. Ve stromu $O(N)$.

**Metoda 1: Hladový přístup (Greedy)**
- Dokud strom není prázdný:
  1. Vezmi libovolný **list** $v$. Přidej ho do IS.
  2. Jeho rodič $p(v)$ tím pádem v IS být nesmí.
  3. Odstraň z grafu $v$ i $p(v)$ (a všechny incidentní hrany).
- *Důkaz:* Každá IS se dá upravit tak, aby obsahovala listy (výměnou rodiče za list se velikost nezmenší).

**Metoda 2: Dynamické programování (Zdola nahoru)**
- Pro každý vrchol $u$ počítáme dvě čísla:
  - $I(u)$: Velikost max IS v podstromu $u$, pokud $u$ **JE** v množině.
    $$I(u) = 1 + \sum_{v \in syn(u)} O(v)$$ (Když beru $u$, nesmím vzít syny).
  - $O(u)$: Velikost max IS v podstromu $u$, pokud $u$ **NENÍ** v množině.
    $$O(u) = \sum_{v \in syn(u)} \max(I(v), O(v))$$ (Když neberu $u$, u synů si můžu vybrat to lepší).
- Výsledek je $\max(I(kořen), O(kořen))$.

---

## <span style="color:#f1c40f">3. Barvení intervalového grafu</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**

**Problém:** Máme množinu intervalů (časových úseků). Chceme je obarvit tak, aby se překrývající intervaly lišily barvou, a použít min. počet barev.
- V obecném grafu NP-těžké. Zde $O(N \log N)$.

**Algoritmus (Hladový):**
1.  Seřaď intervaly podle **začátků** ($S_i$).
2.  Procházej intervaly v tomto pořadí.
3.  Každému intervalu přiřaď **nejmenší možnou barvu** (takovou, kterou nemají jeho *momentálně aktivní* sousedé).
    - Technicky: Udržujeme si množinu "volných" barev. Když interval skončí, jeho barva se uvolní.

**Vlastnost:** Tento hladový algoritmus najde **optimální** řešení. Počet barev se rovná velikosti největší kliky (max počet intervalů překrývajících se v jednom bodě).

---

## <span style="color:#f1c40f">4. Pseudopolynomiální algoritmus (Batoh)</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**

**Problém Batohu (Knapsack):** Předměty s vahou $w_i$ a cenou $c_i$. Kapacita $K$.
- Je NP-těžký, protože záleží na *hodnotách* čísel, ne jen na počtu předmětů.

**Algoritmus (Dynamické programování):**
- $DP[i][w]$ = Maximální cena, kterou získáme výběrem z prvních $i$ věcí, pokud součet vah je přesně $w$.
- Tabulka má velikost $N \times K$.
- Výpočet: $O(N \cdot K)$.

**Proč "Pseudopolynomiální"?**
- Složitost závisí na $K$ (číslo na vstupu).
- Pokud $K$ zapíšeme binárně, má $b$ bitů ($K \approx 2^b$).
- Složitost je $O(N \cdot 2^b)$, což je **exponenciální** vzhledem k délce vstupu (počtu bitů).
- Pokud je ale $K$ "rozumně malé" (např. $K=10000$), běží to rychle.

---

## <span style="color:#2ecc71">5. Aproximační algoritmus</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**

**Definice:** Algoritmus $A$ pro optimalizační problém je **$\alpha$-aproximační**, pokud:
1.  Běží v polynomiálním čase.
2.  Pro každý vstup vrátí řešení s cenou $C$, pro kterou platí:
    - **Minimlaizace:** $C \le \alpha \cdot OPT$
    - **Maximalizace:** $C \ge \frac{1}{\alpha} \cdot OPT$
    (Kde $OPT$ je cena optimálního řešení).

- $\alpha$ (aproximační poměr) je garance kvality. Čím blíže k 1, tím lépe.

---

## <span style="color:#f1c40f">6. 2-aproximace Obchodního cestujícího (Metric TSP)</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**

**Předpoklad:** Metrický prostor (platí trojúhelníková nerovnost: cesta přímo je kratší než oklikou).
**Obecný TSP:** Nelze aproximovat (ani s velkým $\alpha$).
**Metrický TSP:** Jde aproximovat.

**Algoritmus (Double Tree):**
1.  Najdi **Minimální kostru (MST)** grafu.
    - Cena $MST \le OPT$ (protože i $OPT$ cesta bez jedné hrany je kostra).
2.  Zdvoj každou hranu v kostře.
    - Vznikne Eulerovský graf (všechny stupně sudé).
    - Cena je $2 \cdot MST \le 2 \cdot OPT$.
3.  Najdi Eulerův tah v tomto zdvojeném grafu.
4.  Tah převeď na Hamiltonovskou kružnici pomocí **zkratek** (Shortcuts):
    - Když procházíš tah a narazíš na vrchol, kde už jsi byl, přeskoč ho a jdi rovnou do dalšího.
    - Díky trojúhelníkové nerovnosti zkratka cestu neprodlouží.

**Výsledek:** Cena nalezené cesty $\le 2 \cdot OPT$.

---

## <span style="color:#e67e22">7. Aproximační schéma pro Batoh (FPTAS)</span>
- [ ] 🟢 **Umím**
- [ ] 🟡 **Znám**
- [ ] 🔴 **V hajzlu**

**Cíl:** Chceme řešení s chybou maximálně $\epsilon$ (např. 1%). Tedy cena $\ge (1-\epsilon) \cdot OPT$.
**Idea:** Využijeme toho, že batoh umíme řešit rychle, když jsou **ceny předmětů malé** (DP podle cen).

**Algoritmus (Škálování):**
1.  Máme předměty s cenami $c_i$. Ty jsou moc velké (DP by trvalo dlouho).
2.  Zvolíme škálovací faktor $S = \frac{\epsilon \cdot \max(c_i)}{N}$.
3.  Všechny ceny vydělíme $S$ a zaokrouhlíme dolů: $c'_i = \lfloor c_i / S \rfloor$.
4.  Tím jsme "ořezali" dolní bity. Hodnoty $c'_i$ jsou malé (polynomiální vůči $N/\epsilon$).
5.  Spustíme DP na těchto malých cenách.

**Výsledek:**
- Získáme řešení v čase $O(N^3 / \epsilon)$.
- Chyba způsobená zaokrouhlením se nasčítá maximálně na $\epsilon \cdot OPT$.
- Toto se nazývá **FPTAS** (Plně polynomiální aproximační schéma) – čas je polynomem v $N$ i v $1/\epsilon$.