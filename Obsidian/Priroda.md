## 1. Základy strojového učení

**Typy učení**
- S učitelem – vstupy + labely, učí mapování vstup→výstup
- Bez učitele – jen vstupy, hledá strukturu (clustering, redukce dimenze)
- Zpětnovazební – agent + odměny, hledá strategii max. odměny

**Úlohy s učitelem**
- Regrese – výstup spojité číslo
- Klasifikace – výstup diskrétní třída

**Příznaky a předzpracování**
- Kategorické (nominální) → one-hot
- Ordinální → celá čísla zachovávající pořadí
- Číselné → škálování (standardizace / min-max), důležité u vzdálenostních metod a neuronek

## 2. Jednoduchý genetický algoritmus

**Kostra EA**: init → selekce rodičů → křížení+mutace → environmentální selekce → opakuj

**Fitness** – číslo = kvalita jedince, závisí na problému

**Operátory**
- Jednobodové / n-bodové křížení – řezy, úseky střídavě od A/B
- Uniformní křížení – každý bit zvlášť losován
- Mutace – překlopení bitu s malou pravd., drží diverzitu

**Selekce rodičů**
- Ruletová – pravd. ∝ fitness; − citlivá na škálu, předčasná konvergence, nefunguje pro záporné
- Turnajová – nejlepší z k náhodných; + nezávislá na škále, laditelný tlak (k), funguje pro záporné

**Elitismus** – nejlepší jedinec(i) beze změny do další generace

**Environmentální selekce**
- (μ, λ) – vybírá jen z λ potomků; lépe uniká lok. optimům, může ztratit dobré řešení
- (μ + λ) – vybírá z rodičů + potomků; implicitní elitismus, riziko uváznutí

**Celočíselné kódování** – vektor int; mutace = nahrazení náhodným / posun ±1


## 3. Evoluční algoritmy pro spojitou optimalizaci

**Spojitá optimalizace** – hledání x ∈ ℝⁿ minimalizujícího f(x); jedinec = reálný vektor

**Operátory**
- Aritmetické křížení – c = α·a + (1−α)·b (potomek mezi rodiči)
- Mutace – přičtení N(0, σ)
  - Nezatížená – stejné σ pro všechny souřadnice (kulový obláček)
  - Zatížená – různá σ + korelace (elipsa, přizpůsobí se tvaru funkce)

**Separabilní × neseparabilní (funkce)**
- Separabilní – f = Σ gᵢ(xᵢ), lze ladit proměnné nezávisle
- Neseparabilní – proměnné se ovlivňují, nelze po jedné, mnohem těžší

**Diferenciální evoluce (DE)** – mutace přes rozdíl jedinců
- v = a + F·(b − c), pak křížení s x (po složkách, pravd. CR) → u
- u nahradí x, pokud je lepší
- + málo parametrů, robustní, samoškálující se, dobré na neseparabilní

## 4. Evoluční algoritmy pro kombinatorickou optimalizaci

**Permutační kódování** – jedinec = permutace (pořadí prvků), každý prvek právě 1×; operátory musí zachovat platnou permutaci

**Mutace**
- Swap – prohoď dva prvky
- Insertion – vyjmi prvek, vlož jinam
- Inversion – obrať úsek (přirozené pro TSP)
- Scramble – zamíchej úsek

**Křížení**
- OX (Order) – úsek z A, zbytek z B v jeho pořadí; zachovává relativní pořadí
- PMX (Partially Mapped) – úsek z A → mapování, zbytek z B s řešením konfliktů; zachovává pozice
- ER (Edge Recombination) – tabulka sousedů z obou rodičů, zachovává hrany; nejlepší pro TSP

**TSP** – nejkratší trasa přes všechna města právě 1× a zpět
- Jedinec: permutace měst
- Fitness: délka trasy (minimalizuje se)
- Operátory: inversion + ER (rozhodují hrany/sousednost, ne absolutní pozice)

## 5. Particle Swarm Optimization (PSO)

**Myšlenka** – roj částic létá prostorem řešení; každá má polohu (řešení) + rychlost; pro spojitou optimalizaci

**Aktualizace**
- v ← w·v + c₁·r₁·(p_best − x) + c₂·r₂·(g_best − x)
  - w = setrvačnost, c₁ = táhne k vlastnímu nejlepšímu, c₂ = k nejlepšímu v okolí, r = náhoda
- x ← x + v

**Topologie** (co je okolí / odkud g_best)
- Globální (gbest) – celý roj; rychlá konvergence, riziko lok. optima
- Geometrické – sousedé dle vzdálenosti v prostoru
- Sociální (lbest) – pevná struktura (např. kruh), nezávislá na poloze

**Vliv topologie** – lokálnější okolí = pomalejší šíření info = víc diverzity, méně předčasné konvergence (explorace × exploatace)

**Spojitá optimalizace** – poloha = reálný vektor = řešení; alternativa k DE

## 6. Ant Colony Optimization (ACO)

**Pojmy**
- Feromon – stopa na hraně, společná paměť kolonie, vyjadřuje historickou kvalitu volby
- Atraktivita (heuristika) – fixní lokální lákavost (u TSP 1/vzdálenost)

**Generování řešení** – mravenec staví řešení po krocích, volí pravděpodobnostně ∝ (feromon)^α · (atraktivita)^β

**Aktualizace feromonu**
- Vypařování – feromon ×(1−ρ), zapomíná staré stopy
- Posílení – přidání na použité hrany úměrně kvalitě řešení

**TSP** – hrany = komponenty, atraktivita 1/vzdálenost, feromon na hranách → konverguje ke krátké trase
**VRP** – rozšíření na víc vozidel s kapacitou, stejný princip

## 7. Lineární a kartézské GP, gramatická evoluce

Cíl GP: evolvovat programy. Liší se kódováním.

**Lineární GP (LGP)**
- Kódování: posloupnost instrukcí nad registry, `r2 = op(r1, r3)`; výstup z určeného registru
- Operátory: křížení = výměna úseků instrukcí; mutace = změna instrukce
- Introny = instrukce neovlivňující výstup; proměnná délka

**Kartézské GP (CGP)**
- Kódování: graf v mřížce uzlů; řetězec celých čísel pevné délky; uzel = funkce + indexy vstupů; zvlášť volba výstupů
- Operátory: hlavně mutace genu; křížení zřídka
- Neaktivní uzly → neutralita, pomáhá prohledávání

**Gramatická evoluce (GE)**
- Odděluje genotyp (posloupnost int „kodonů") od fenotypu (program dle BNF gramatiky)
- Operátory = obyčejné GA na posloupnosti čísel
- Překlad: pro neterminál vyber pravidlo `kodon mod počet_pravidel`, spotřebuj kodon, opakuj
- Výhoda: vždy platný program, nezávislé na jazyce

**Krátký/dlouhý jedinec v GE**
- Krátký → wrapping (čteš kodony znovu od začátku); po max. počtu wrapů neplatný → nejhorší fitness
- Dlouhý → přebytečné kodony se ignorují


## 8. Stromové genetické programování

**Kódování** – jedinec = strom; vnitřní uzly = funkce, listy = terminály (proměnné, konstanty); vyhodnocení rekurzivně

**Operátory**
- Křížení – prohození podstromů mezi rodiči
- Mutace – náhrada podstromu novým náhodným
- Bloat – stromy nekontrolovaně rostou → omezení max. hloubky

**Konstanty**
- Efemerní náhodné konstanty (ERC) – speciální terminál → při generování se vyrobí náhodná fixní konstanta, šíří se operátory
- Volitelně doladit zvlášť (lokální optimalizace)

**Typované GP** – uzly mají typy vstupů/výstupu; operátory spojují jen typově kompatibilní podstromy → vždy platný program, lze míchat typy

**Automaticky definované funkce (ADF)** – jedinec má víc stromů: main + ADF (vlastní podprogramy); main je volá → modularita, znovupoužitelnost

**Zabránění rekurzi u ADF** – hierarchie volání: ADF volá jen ADF s nižším indexem → acyklický graf volání

**Porovnání**
- Stromové – přirozené pro výrazy; − bloat
- Lineární – blízko HW, rychlé; − introny, méně názorné
- Kartézské – pevná délka, neutralita, vhodné pro obvody; − méně intuitivní
- GE – jazyková nezávislost, GA operátory; − slabá lokálnost genotyp↔fenotyp


## 9. Perceptronové neuronové sítě

**Jeden perceptron**
- ξ = Σ wᵢxᵢ + b, y = f(ξ); klasicky f = skoková → lineární klasifikátor (dělí prostor nadrovinou)

**Trénování perceptronu**
- wᵢ ← wᵢ + η·(d − y)·xᵢ
- Konverguje právě pro lineárně separabilní data (věta o konvergenci); XOR nikdy

**MLP** – vrstvy vstupní → skryté → výstupní, plně propojené, feedforward; nelineární aktivace → řeší i neseparabilní (univerzální aproximátor)

**Aktivační funkce**
- Sigmoida σ=1/(1+e^−ξ), (0,1), σ'=σ(1−σ); saturuje
- Tanh (−1,1), vycentrovaná; saturuje
- ReLU max(0,ξ); nesaturuje pro ξ>0, rychlá; umírající ReLU

**Backpropagation** – minimalizace E (např. ½Σ(yⱼ−dⱼ)²) gradientním sestupem; chyba se šíří zpět přes chain rule

**Odvození – výstupní vrstva**
- ∂E/∂w_ij = (∂E/∂y_j)(∂y_j/∂ξ_j)(∂ξ_j/∂w_ij) = (y_j − d_j)·f'(ξ_j)·y_i
- δ_j = (y_j − d_j)·f'(ξ_j)
- w_ij ← w_ij − η·δ_j·y_i

**Skryté vrstvy** – nemáme d; chyba se propaguje zpět:
- δ_j = f'(ξ_j)·Σ_k(δ_k·w_jk)
- stejné pravidlo: w_ij ← w_ij − η·δ_j·y_i


## 10. RBF sítě

**RBF jednotka** – reaguje na vzdálenost vstupu od středu $\mathbf{c}$ (ne na nadrovinu):
$$\varphi(\mathbf{x}) = \exp\!\left(-\frac{\lVert \mathbf{x} - \mathbf{c}\rVert^2}{2\sigma^2}\right)$$
- $\mathbf{c}$ = střed (max odezva), $\sigma$ = šířka; odezva klesá do všech stran

**Architektura** – 3 vrstvy:
1. vstupní
2. skrytá = RBF jednotky (každá svůj $\mathbf{c}$, $\sigma$)
3. výstupní = lineární kombinace $y = \sum_i w_i \varphi_i(\mathbf{x})$

**Trénování – dva oddělené kroky**
1. středy $\mathbf{c}$ bez učitele (k-means), šířky z průměrných vzdáleností
2. výstupní váhy $w_i$ = lineární regrese (nejmenší čtverce, přímo)
→ rychlejší a stabilnější než MLP

**k-means**
1. zvol $k$ středů
2. přiřaď každý bod k nejbližšímu středu
3. posuň střed do těžiště přiřazených bodů
4. opakuj 2–3 do ustálení
- lokální optimum, závisí na inicializaci

**RBF vs. MLP (geometrie)**
- MLP – dělí prostor nadrovinami, globální/neomezené oblasti, lépe extrapoluje
- RBF – lokální „bubliny" kolem středů, rychlé učení, dobrá interpolace, špatná extrapolace (daleko → ~0)


## 11. Konvoluční sítě

**Konvoluční filtr** – malá mřížka vah klouže po obrázku, v každé pozici vážený součet + aktivace → feature mapa
- sdílení vah (méně parametrů, detekce vzoru kdekoli, translační invariance)
- lokální propojení (receptivní pole)
- víc filtrů = víc feature map; hlubší vrstvy = složitější vzory

**Pooling** – zmenší prostorový rozměr; okno → 1 číslo
- max pooling (max), average pooling (průměr)
- méně dat, necitlivost na přesnou polohu, větší receptivní pole; bez parametrů

**Architektura** – [konv+aktivace → pooling]×N → flatten → plně propojené → výstup; konv. část = extraktor příznaků, FC část = klasifikace

**Matoucí vzory** – pro člověka normální obrázek, síť klasifikuje špatně; bezpečnostní riziko (značky, obličeje, filtry); síť se učí křehké vzory, ne pojmy

**FGSM** – gradient chyby podle vstupu, krok ve směru růstu chyby:
$$\mathbf{x}_{adv} = \mathbf{x} + \varepsilon \cdot \operatorname{sign}(\nabla_{\mathbf{x}} E(\mathbf{x}, d))$$
- backprop obráceně: fixuješ váhy, měníš vstup

**Přenos stylu** – obsah (aktivace vyšších vrstev) + styl (Gramovy matice korelací feature map); optimalizuješ obrázek, ne síť

**GAN** – generátor (šum → padělky) vs. diskriminátor (reálné/falešné); souboj → G dělá realističtější vzorky; rovnováha při 50% úspěšnosti D


## 12. Rekurentní neuronové sítě

**Co to je** – síť se zpětnou vazbou, má paměť (skrytý stav z minulého kroku):
$$h_t = f(W_x x_t + W_h h_{t-1} + b), \quad y_t = g(W_y h_t + c)$$
- váhy sdílené přes všechny časové kroky

**Použití** – posloupnosti: text, překlad, řeč, časové řady, hudba, video

**BPTT (zpětné šíření v čase)** – síť se rozbalí v čase na dopřednou (kopie/krok, sdílené váhy) → běžný backprop; gradient váhy = součet přes všechny kroky

**Mizející/explodující gradienty** – gradient se přes kroky opakovaně násobí
- faktor < 1 → mizí → neučí dlouhodobé závislosti
- faktor > 1 → exploduje (řeší gradient clipping)

**Echo State sítě (ESN)**
- rezervoár = velká náhodná rekurentní vrstva, váhy fixní (netrénují se)
- echo state property: dynamika vyhasíná (spektrální poloměr < 1)
- trénuje se jen výstupní vrstva = lineární regrese
- trénink: zmraz rezervoár → posbírej stavy → lineární regrese; žádné BPTT

**LSTM** – buněčný stav $c_t$ (paměť, teče přičítáním → gradient nemizí) + brány:
$$f_t=\sigma(W_f[h_{t-1},x_t]+b_f) \quad i_t=\sigma(W_i[\dots]) \quad \tilde{c}_t=\tanh(W_c[\dots])$$
$$c_t = f_t \odot c_{t-1} + i_t \odot \tilde{c}_t$$
$$o_t=\sigma(W_o[\dots]), \quad h_t = o_t \odot \tanh(c_t)$$
- forget = co zapomenout, input = co zapsat, output = co vydat
- architektura = řetěz buněk, $c_t$ teče celým řetězem

**Výhody vs. základní RNN**
- LSTM – řeší mizející gradient, dlouhodobé závislosti, brány řídí paměť
- ESN – obejde gradienty (netrénuje rekurenci), rychlý trénink (lin. regrese)







