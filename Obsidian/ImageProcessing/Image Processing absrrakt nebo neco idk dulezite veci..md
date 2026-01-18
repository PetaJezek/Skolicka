

KONVOLUCE

### 1. Definice konvoluce **Spojitá (Teorie):** Konvoluce dvou funkcí $f(t)$ a $g(t)$ je definována jako integrál součinu funkce $f$ a časově převrácené a posunuté funkce $g$: $$ (f * g)(t) = \int_{-\infty}^{\infty} f(\tau) \cdot g(t - \tau) \, d\tau $$ **Diskrétní (Praxe/Obrázky):** Pro 2D obrázek $f[x,y]$ a masku $h[i,j]$ o velikosti $M \times N$: $$ (f * h)[x,y] = \sum_{m=0}^{M-1} \sum_{n=0}^{N-1} f[m, n] \cdot h[x-m, y-n] $$ 


### 2. Důkaz: Konvoluční teorém (Convolution Theorem) *Otázka:* Dokažte, že konvoluce v prostorovém čase odpovídá násobení ve frekvenční doméně. Tedy $\mathcal{F}\{f * g\} = F(\omega) \cdot G(\omega)$. **Důkaz:** Vyjdeme z definice Fourierovy transformace aplikované na konvoluci: $$ \mathcal{F}\{f * g\} = \int_{-\infty}^{\infty} (f * g)(t) \cdot e^{-i\omega t} \, dt $$ Dosadíme definici konvoluce za $(f * g)(t)$: $$ \mathcal{F}\{f * g\} = \int_{-\infty}^{\infty} \left[ \int_{-\infty}^{\infty} f(\tau) g(t - \tau) \, d\tau \right] e^{-i\omega t} \, dt $$ Prohodíme pořadí integrace (Fubiniho věta) a sdružíme členy s $t$: $$ = \int_{-\infty}^{\infty} f(\tau) \left[ \int_{-\infty}^{\infty} g(t - \tau) e^{-i\omega t} \, dt \right] d\tau $$ Zavedeme substituci ve vnitřním integrálu: $u = t - \tau$, z čehož plyne $t = u + \tau$ a $dt = du$: $$ = \int_{-\infty}^{\infty} f(\tau) \left[ \int_{-\infty}^{\infty} g(u) e^{-i\omega (u + \tau)} \, du \right] d\tau $$ Rozdělíme exponenciálu $e^{-i\omega(u+\tau)} = e^{-i\omega u} \cdot e^{-i\omega \tau}$: $$ = \int_{-\infty}^{\infty} f(\tau) e^{-i\omega \tau} \left[ \int_{-\infty}^{\infty} g(u) e^{-i\omega u} \, du \right] d\tau $$ V hranaté závorce je přesně definice Fourierovy transformace $G(\omega)$. Ta nezávisí na $\tau$, takže ji můžeme vytknout: $$ = G(\omega) \cdot \int_{-\infty}^{\infty} f(\tau) e^{-i\omega \tau} \, d\tau $$ Zbylý integrál je definice $F(\omega)$. Tedy: $$ \mathcal{F}\{f * g\} = F(\omega) \cdot G(\omega) \quad \blacksquare $$ 


### 3. Důkaz: Shift teorém (Věta o posunutí) *Otázka:* Co se stane se spektrem, když posuneme funkci v čase? **Tvrzení:** $\mathcal{F}\{f(t - t_0)\} = F(\omega) \cdot e^{-i\omega t_0}$. (Posun v čase je změna fáze ve spektru, amplituda se nemění). **Důkaz:** Z definice FT: $$ \mathcal{F}\{f(t - t_0)\} = \int_{-\infty}^{\infty} f(t - t_0) \cdot e^{-i\omega t} \, dt $$ Substituce: $u = t - t_0 \Rightarrow t = u + t_0, dt = du$: $$ = \int_{-\infty}^{\infty} f(u) \cdot e^{-i\omega (u + t_0)} \, du $$ Roztrhněme exponenciálu: $$ = \int_{-\infty}^{\infty} f(u) \cdot e^{-i\omega u} \cdot e^{-i\omega t_0} \, du $$ Člen $e^{-i\omega t_0}$ je konstanta vzhledem k integrační proměnné $u$, vytkneme ho: $$ = e^{-i\omega t_0} \cdot \underbrace{\int_{-\infty}^{\infty} f(u) e^{-i\omega u} \, du}_{F(\omega)} $$ $$ = F(\omega) \cdot e^{-i\omega t_0} \quad \blacksquare $$








#### 4. Jak přečíst spektrum (Obrázek ve frekvenční doméně)

Když se díváš na 2D Fourierovo spektrum (čtverec, uprostřed jasná tečka):

1. **Střed (DC složka):** Bod [0,0] uprostřed reprezentuje průměrnou jasovou hodnotu celého obrázku (frekvence 0). Je vždy nejjasnější.
    
2. **Vzdálenost od středu:** Čím dále jsi od středu, tím **vyšší frekvenci** (jemnější detaily/šum) bod reprezentuje.
    
3. **Směr:** Směr ve spektru je kolmý na směr hran v obrázku.
    
    - Pokud vidíš jasnou čáru **svisle** přes střed -> v obrázku jsou **vodorovné** pruhy/hrany.
        
    - Pokud vidíš jasnou čáru **vodorovně** -> v obrázku jsou **svislé** pruhy.
        
4. **Symetrie:** Spektrum reálného obrázku je vždy středově souměrné (podle počátku).

### 4. Důkaz: Věta o linearitě (Linearity Theorem)

*Otázka:* Dokažte, že Fourierova transformace je lineární operátor.

**Tvrzení:**
$$
\mathcal{F}\{a \cdot f(t) + b \cdot g(t)\} = a \cdot F(\omega) + b \cdot G(\omega)
$$
kde $a, b$ jsou komplexní konstanty.

**Důkaz:**
Plyne přímo z linearity integrálu. Dosadíme do definice FT:

$$
\mathcal{F}\{af(t) + bg(t)\} = \int_{-\infty}^{\infty} [a f(t) + b g(t)] \cdot e^{-i\omega t} \, dt
$$

Rozdělíme integrál na dva (integrál součtu je součet integrálů):

$$
= \int_{-\infty}^{\infty} a f(t) e^{-i\omega t} \, dt + \int_{-\infty}^{\infty} b g(t) e^{-i\omega t} \, dt
$$

Vytkneme konstanty $a$ a $b$ před integrály:

$$
= a \underbrace{\int_{-\infty}^{\infty} f(t) e^{-i\omega t} \, dt}_{F(\omega)} + b \underbrace{\int_{-\infty}^{\infty} g(t) e^{-i\omega t} \, dt}_{G(\omega)}
$$

$$
= a F(\omega) + b G(\omega) \quad \blacksquare
$$

---

### 5. Důkaz: Věta o změně měřítka (Scaling Theorem)

*Otázka:* Co se stane se spektrem, když signál v čase "zrychlíme" nebo "zpomalíme" (rozšíříme/zúžíme)?

**Tvrzení:**
$$
\mathcal{F}\{f(at)\} = \frac{1}{|a|} F\left(\frac{\omega}{a}\right)
$$
*Poznámka: Zúžení v čase ($a>1$) vede k rozšíření ve frekvenci (vyšší frekvence) a snížení amplitudy.*

**Důkaz:**
Z definice FT pro $f(at)$:

$$
\mathcal{F}\{f(at)\} = \int_{-\infty}^{\infty} f(at) \cdot e^{-i\omega t} \, dt
$$

Zavedeme substituci $u = at$.
Zde musíme rozlišit dva případy kvůli mezím integrálu:

**A) Pro $a > 0$:**
$dt = \frac{du}{a}$. Meze zůstávají $-\infty \to \infty$.

$$
= \int_{-\infty}^{\infty} f(u) e^{-i\omega \frac{u}{a}} \frac{du}{a} = \frac{1}{a} \int_{-\infty}^{\infty} f(u) e^{-i (\frac{\omega}{a}) u} \, du
$$
Integrál je přesně definice FT, ale s frekvencí $\frac{\omega}{a}$.
$$
= \frac{1}{a} F\left(\frac{\omega}{a}\right)
$$

**B) Pro $a < 0$:**
Při substituci se obrátí meze integrálu ($\infty \to -\infty$). Abychom je vrátili zpět, změníme znaménko, což nám dá absolutní hodnotu $|a|$.

Spojením obou případů:
$$
= \frac{1}{|a|} F\left(\frac{\omega}{a}\right) \quad \blacksquare
$$

---

### 6. Rotační teorém (Rotation Theorem - 2D)

*Otázka:* Jak se změní spektrum, pokud otočíme vstupní obrázek?

**Tvrzení:**
Otočení funkce $f(x,y)$ o úhel $\theta_0$ v prostorovém souřadnicovém systému způsobí otočení jejího spektra $F(u,v)$ o stejný úhel $\theta_0$ ve frekvenčním systému.

**Důkaz (pomocí polárních souřadnic):**
Je výhodnější přejít z kartézských souřadnic $(x,y)$ do polárních $(r, \phi)$, kde:
$x = r \cos \phi, \quad y = r \sin \phi$

A pro frekvence $(u,v)$ do polárních $(\rho, \theta)$:
$u = \rho \cos \theta, \quad v = \rho \sin \theta$

Fourierova transformace v polárních souřadnicích se zapíše jako:
$$
F(\rho, \theta) = \int_{0}^{\infty} \int_{0}^{2\pi} f(r, \phi) e^{-i 2\pi r \rho \cos(\phi - \theta)} r \, d\phi \, dr
$$

Nechť $g$ je otočená verze obrázku $f$ o úhel $\theta_0$:
$$
g(r, \phi) = f(r, \phi + \theta_0)
$$

Dosadíme do definice FT pro $g$:
$$
G(\rho, \theta) = \int_{0}^{\infty} \int_{0}^{2\pi} f(r, \phi + \theta_0) e^{-i 2\pi r \rho \cos(\phi - \theta)} r \, d\phi \, dr
$$

Provedeme substituci v úhlu: $\alpha = \phi + \theta_0 \Rightarrow \phi = \alpha - \theta_0$.
Upravíme člen v exponenciále: $\cos(\phi - \theta) = \cos(\alpha - \theta_0 - \theta) = \cos(\alpha - (\theta + \theta_0))$.

Tím dostáváme:
$$
G(\rho, \theta) = \underbrace{\int_{0}^{\infty} \int_{0}^{2\pi} f(r, \alpha) e^{-i 2\pi r \rho \cos(\alpha - (\theta + \theta_0))} r \, d\alpha \, dr}_{F(\rho, \theta + \theta_0)}
$$

Vidíme, že výsledné spektrum je původní spektrum $F$, ale vyhodnocené na úhlu $\theta + \theta_0$.
$$
G(\rho, \theta) = F(\rho, \theta + \theta_0) \quad \blacksquare
$$




#### 5. Proč použít filtr vs. Konvoluce?

Tohle je chyták. **Filtr a Konvoluce jsou dvě strany téže mince.**

- **V prostorovém čase:** Aplikujeme filtr (masku) pomocí **konvoluce**.
    
    - _Výhoda:_ Pro malé masky (např. 3x3, 5x5) je to výpočetně levné a rychlé.
        
    - _Nevýhoda:_ Pro velké masky (např. rozmazání velkého rozlišení) je to extrémně pomalé (O(N2⋅M2)).
        
- **Ve frekvenční oblasti:** Aplikujeme filtr pomocí **násobení**.
    
    - Postup: Vezmeme obrázek → FFT → Vynásobíme maskou filtru → Inverse FFT.
        
    - _Výhoda:_ Díky Konvolučnímu teorému je to pro velké masky mnohem rychlejší než klasická konvoluce.
        
    - _Nevýhoda:_ Režie na výpočet FFT se nevyplatí pro malé masky.

## Digitalizace a Vzorkování (Sampling)

Proces převodu spojité reality do diskrétních dat počítače.
Děje se ve dvou krocích:
1.  **Vzorkování (Sampling):** Diskretizace souřadnic (prostor $x,y$).
2.  **Kvantování (Quantization):** Diskretizace hodnot (jas $f(x,y)$).

### 1. Matematický model vzorkování
Co vzorkujeme? Spojitý obraz (Irradiance function) promítnutý optikou na senzor.

* **Model:** Vynásobení spojité funkce $f(x,y)$ tzv. vzorkovací funkcí $s(x,y)$.
* **Vzorkovací funkce (Diracův hřeben / Bed of Nails):**
    * Nekonečné pole delta funkcí (impulzů) rozmístěných v mřížce.
    $$s(x,y) = \sum_{m=-\infty}^{\infty} \sum_{n=-\infty}^{\infty} \delta(x - m\Delta x, y - n\Delta y)$$
    * Kde $\Delta x, \Delta y$ jsou rozestupy pixelů (sampling pitch).
* **Vzorkovaný obraz:**
    $$f_s(x,y) = f(x,y) \cdot s(x,y)$$
    * Tímto "vybereme" hodnoty jen v bodech mřížky, jinde je nula.

### 2. Důsledky ve frekvenční oblasti (Spektrum)
Co udělá násobení v prostoru se spektrem?
* Aplikujeme **Konvoluční teorém**: Násobení v prostoru = Konvoluce ve frekvenci.
    $$\mathcal{F}\{f \cdot s\} = F(u,v) * S(u,v)$$
* Spektrum vzorkovací funkce $S(u,v)$ je **také Diracův hřeben** (opět pole impulsů, ale s rozestupem $1/\Delta$).
* **Výsledek:** Konvoluce spektra obrazu $F$ s hřebenem impulsů způsobí, že se **spektrum obrazu $F$ zkopíruje (replikuje) na pozici každého impulsu.**
    * Vzniká periodické spektrum (středově souměrné, opakující se do nekonečna).

### 3. Rekonstrukce a Nyquist
Jak získat zpět spojitý obraz?
* **Teoreticky:** Musíme ve frekvenční oblasti "vyříznout" jen ten jeden centrální kopeček (základní spektrum) a zbytek replik zahodit.
    * To odpovídá aplikaci **Ideálního Low-Pass Filtru** (Obdélníková funkce ve spektru).
    * V prostorovém čase to odpovídá konvoluci s funkcí **sinc** ($sinc(x) = \frac{\sin(\pi x)}{\pi x}$).
* **Nyquistova podmínka:**
    Abychom mohli spektrum vyříznout, **nesmí se repliky překrývat**.
    * Pokud je vzorkovací frekvence moc malá (impulzy ve spektru $S$ jsou moc blízko), kopečky $F$ se srazí.
    * **Aliasing:** Překryv spekter. Vysoké frekvence jedné repliky se vmísí do nízkých frekvencí druhé. Nelze vrátit zpět.
    * Podmínka bez aliasingu:
        $$\Delta x \leq \frac{1}{2 W_u}$$
        (Vzorkovací frekvence > 2x Maximální frekvence obrazu).

### 4. Interpolace (Praktická rekonstrukce)
Protože funkce *sinc* je nekonečná a nelze ji v praxi použít, používáme konvoluci s jednoduššími jádry (rekonstrukčními filtry):

1.  **Nearest Neighbor (Box filter):**
    * Jádro: Obdélník (šířka 1).
    * Efekt: Hranaté "kostičky".
2.  **Lineární (Triangle filter):**
    * Jádro: Trojúhelník (šířka 2). Ve 2D je to jehlan.
    * Matematika: Konvoluce dvou Box filtrů ($Box * Box$).
    * Efekt: Spojí středy pixelů rovnou čárou.
3.  **Bikubická (Cubic B-spline):**
    * Jádro: Zvonovitý tvar (složený z polynomů 3. stupně).
    * Matematika: Aproximuje *sinc* funkci. Hladké napojení i derivací.

### 5. Proč se v praxi vzorkuje Nyquistovsky "samo"?
* Poznámka z přednášek: *"Čočka slouží jako low pass filter"*.
* Fyzikální optika a difrakce přirozeně rozmaže bod na malý flíček (Airy disk).
* Tím čočka **ořízne nekonečně vysoké frekvence** ještě předtím, než dopadnou na senzor.
* Funguje jako přirozený Anti-aliasing filtr.


## Kvantování (Quantization)
Diskretizace hodnot (osy Y/Z). Měříme intenzitu světla s omezenou přesností.

* **Princip:** Převod spojitého signálu (reálné číslo) na diskrétní index $0 \dots L-1$.
    * *Analogie:* Schody místo rampy.
    * **Vždy ztrátové (Lossy):** Zaokrouhlovací chyba je nevratná. Původní reálnou hodnotu nelze zjistit.

* **Parametry:**
    * **$L$ (Počet hladin):** Určuje bitovou hloubku (např. 8-bit = 256 hladin).
    * **Rozmístění prahů:**
        1.  **Rovnoměrné:** Schody jsou stejně vysoké. (Nejčastější).
        2.  **Logaritmické:** Schody jsou jemnější u nuly (ve stínech) a hrubší ve světlech.
            * *Důvod:* Lidské oko je citlivější na změny ve tmě (Weber-Fechnerův zákon).

* **Kvantizační šum a artefakty:**
    * Rozdíl mezi realitou a navzorkovanou hodnotou se chová jako šum.
    * **Falešné hrany (False Contouring / Banding):**
        * Viditelné skoky v plynulých přechodech (např. na obloze).
        * Vznikají při nedostatečném počtu hladin $L$.
        * Pro detektory hran jsou nerozeznatelné od skutečných objektů!

* **Optimalizace (Sampling vs. Kvantování):**
    Kde šetřit, když máme omezená data?
    1.  **Obrázek s detaily (Vysoké frekvence):** Textura, tráva.
        * Investujeme do **Vzorkování** (více pixelů).
        * Oko si nevšimne menší přesnosti barev, ale všimne si chybějících detailů.
    2.  **Obrázek s přechody (Nízké frekvence):** Obloha, portrét.
        * Investujeme do **Kvantování** (více hladin).
        * Vysoké rozlišení je zbytečné (nic se tam nemění), ale nedostatek barev vytvoří ošklivé pruhy.


# Předzpracování obrazu (Image Preprocessing)

Fáze, kdy obraz už máme v počítači (digitální), ale chceme ho vylepšit pro další použití (pro člověka nebo pro algoritmus).

---
## ENCHANCMENT

## 2. Změny kontrastu a jasu

Základní pixelové operace (Point processing). Nepotřebujeme okolí pixelu.

### Histogram
* **Definice:** Graf četnosti jasů. Říká nám **KOLIK** pixelů má danou hodnotu, ale neříká **KDE** jsou.
* **Jas:** Střední hodnota histogramu (těžiště).
* **Kontrast:** Rozptyl hodnot (šířka histogramu).

### Aplikace a Transformace
* **Lineární změny:** $s = a \cdot r + b$
    * Posun ($b$): Změna jasu.
    * Násobení ($a$): Změna kontrastu.
* **Gamma korekce (Nelineární):** $s = r^\gamma$
    * Simuluje lidské oko (nebo nerovnoměrné kvantování).
    * $\gamma < 1$: Zesvětlí stíny (roztáhne tmavé hodnoty).
    * $\gamma > 1$: Ztmaví stíny (zvýrazní světlé hodnoty).

### Ekvalizace histogramu

* **Cíl:** Získat "konstantní" histogram (všechny jasy zastoupeny stejně). Maximalizuje globální kontrast.
* **Princip:** Používá se kumulativní histogram.
* **Problém v diskrétním světě:**
    * Nelze vytvořit skutečně plochý histogram (nelze rozštípnout pixely se stejnou hodnotou).
    * Výsledek je "zubatý" a roztažený.
* **Nevýhoda:** U reálných fotek často vypadá nepřirozeně. Skvělé pro rentgeny nebo satelitní snímky.

### Lokální vs. Globální úpravy
* Globální úpravy selhávají u snímků s vysokým dynamickým rozsahem (HDR) - stín i slunce zároveň.
* **Lokální úpravy (CLAHE):** Histogram se počítá v malém plovoucím okně.

---

## 3. Šum (Noise)

Šum je náhodná chyba v obraze.

### Zdroje šumu
* **Tepelný šum (Thermal):** Zahřívání senzoru (Additive Gaussian).
* **Shot noise (Photon):** Kvantová povaha světla (Multiplicative).
* **Impulzní:** Chyby přenosu, A/D převodníku.

### Typy šumu (Modely)
1.  **Gaussovský bílý šum (AGWN):**
    * Aditivní (přičítá se).
    * **Nekorelovaný:** Hodnota šumu na pixelu nezávisí na sousedech.
    * Spektrum šumu je konstantní rovina (stejná energie na všech frekvencích - jako bílé světlo).
    * Amplituda spektra $\approx \sigma^2$.
2.  **Impulzní šum (Sůl a pepř):**
    * Náhodné extrémní hodnoty (černá 0 / bílá 255).

### Měření kvality (SNR)
* **SNR (Signal-to-Noise Ratio):** Poměr signálu k šumu.
* Vzorec (Akustika/Praxe):
    $$SNR_{dB} = 10 \log_{10} \left( \frac{\text{Výkon signálu}}{\text{Výkon šumu}} \right)$$
* **0 dB:** Šum je stejně silný jako obraz.
* Histogram zašuměného obrázku = Konvoluce původního histogramu s Gaussovou křivkou (rozmazání histogramu).

---

## 4. Odstraňování šumu (Denoising)

Dilema: Jak odstranit šum a nezničit (nerozmazat) hrany?

### A. Průměrování v čase (Temporal Averaging)
* **Nejlepší metoda.**
* Vyžaduje **více snímků** téže scény (statická kamera).
* Šum (náhodný) se vyruší, signál (stálý) zůstane. Neodstraňuje detaily!
* *Poznámka:* Dlouhá expozice NENÍ to samé (tam se šum načítá na senzoru).

### B. Konvoluční filtry (Prostorové)
1.  **Průměrování (Mean Filter):**
    * Rozmaže šum, ale **zničí vysoké frekvence** (hrany).
    * Čím větší maska, tím méně šumu, ale větší rozmazání.
2.  **Rotující okno:**
    * Zkouší 8 poloh masky, vybere tu s nejmenším rozptylem (tam asi není hrana). Pomalé, dělá artefakty.

### C. Nelineární filtry (Rank Filters)
1.  **Medián:**
    * Seřadit hodnoty v okolí -> vzít prostřední.
    * **Ideální na Impulzní šum (Sůl a pepř).** Extrémy zahodí.
    * Zachovává rovné hrany, ale "okusuje" rohy.
    * Fast median filtering: Složitost $O(N \cdot c)$ (lineární vůči velikosti obrazu).

### D. Moderní / Pokročilé metody
1.  **Bilaterální filtr:**
    * Váží pixely podle **prostoru** (jsi blízko?) A podle **intenzity** (jsi podobné barvy?).
    * Neprůměruje přes hrany -> zachová ostrost.
2.  **Non-local Means (NL-means):**
    * Hledá podobné "kousky" (patches) v celém obraze a průměruje je.
    * Velmi kvalitní (BM3D), ale extrémně pomalé.
3.  **Minimalizace funkcionálu (Variační metody):**
    * Hledáme kompromis mezi věrností datům a hladkostí.
    * Rovnice: $\sum (f - y)^2 + \lambda \int (f'')^2$
    * $\lambda$ (Regularizační člen): Určuje, jak moc chceme odšumovat vs. zachovat detaily.

---

## 5. Detekce a zvýraznění hran

Lidské oko potřebuje hrany (vysoké frekvence) k rozpoznání objektů.
* *Experiment:* Trojúhelník poznáme jen podle rohů (vysoké frekvence). Samotné čáry (nižší frekvence) nestačí.

### Ostření (Sharpening)
Princip: Zvýšit strmost hrany (overshoot).
* **Unsharp Masking (Neostré maskování):**
    * Myšlenka z fotokomory.
    * $Výsledek = Originál + k \cdot (Originál - Blur)$
    * $(Originál - Blur)$ jsou hrany. My je přičteme zpátky.
* **Laplaceovo ostření:**
    * Matematicky ekvivalentní Unsharp maskingu.
    * $f_{new} = f - \alpha \nabla^2 f$
    * Využívá 2. derivaci k detekci změn.
    * *Pozor:* Pokud je v obraze šum, ostření ho brutálně zesílí!

### Detektory hran (Edge Detectors)

**1. Založené na 1. derivaci (Gradient)**
* Hledáme **MAXIMUM** derivace.
* **Sobel, Roberts, Prewitt.**
* Problém: Šum vytvoří falešná maxima.

**2. Založené na 2. derivaci (Laplace)**
* Hledáme **PRŮCHOD NULOU (Zero-crossing)**.
* **Marr-Hildreth (LoG - Laplacian of Gaussian):**
    * Nejdřív rozmazat Gaussem (potlačení šumu), pak Laplace.
    * Vytváří uzavřené smyčky ("špagety").

**3. Cannyho detektor (The Best)**
* Optimalizovaný pro odolnost vůči šumu a přesnou lokalizaci (hrana = 1 pixel).
* **Kroky:**
    1.  Vyhlazení (Gauss).
    2.  Gradient (Sobel).
    3.  **Non-maxima suppression:** Ztenčení hran na 1 pixel (hledání lokálního maxima ve směru gradientu).
    4.  **Hystereze (Prahování):**
        * Práh $T_2$: Jistá hrana.
        * Práh $T_1$: Možná hrana (bereme jen, když navazuje na jistou hranu).






