

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

---

# Image Restoration (Rekonstrukce obrazu)

Na rozdíl od Enhancement (subjektivní vylepšení) se Restoration snaží **objektivně matematicky invertovat degradaci**. Není to heuristika.
Model degradace: $$g = f * h + n$$
(Naměřený obraz = Originál * PSF + Šum)



## 1. Příčiny degradace (Blur)
* **Camera Shake (Pohyb kamery):** Třes ruky.
    * Způsobuje cca **95 %** rozmazaných snímků.
    * PSF = Trajektorie pohybu (světlejší tam, kde se ruka zdržela déle).
* **Wrong Focus (Špatné zaostření):** Fyzické limity optiky.
    * Forenzní využití (zaostření až po vyfocení).
    * PSF = **Kolečko konstantní intenzity** (nebo tvar clony). **NENÍ to Gaussovka!**
* **Medium Turbulence:** Mlha, voda, atmosféra.
    * PSF = Gaussovka (rozmazaný flek).

## 2. Modely degradace
* **Space Invariant:** PSF je všude stejná (např. pohyb celé ploché scény). *Tím se budeme zabývat.*
* **Space Variant:** PSF se mění pixel od pixelu (např. rotace, různá hloubka scény). Složité.

## 3. Problém inverze a šumu
I kdybychom znali přesnou PSF ($h$), nemůžeme prostě udělat inverzi ($1/h$), protože v obraze je vždy šum ($n$).
* Inverze degradace by **invertovala i šum** $\to$ Obrovské zesílení šumu.
* Úloha je **špatně podmíněná** (Ill-posed problem).

### Metody řešení (když známe PSF)
1.  **Inverzní Fourier:**
    * Bez šumu: Funguje perfektně (minimalizuje rozdíl od modelu).
    * Se šumem: Nepoužitelné (zesílí šum).
2.  **Wienerův filtr:**
    * **Statistický přístup.** Minimalizuje střední kvadratickou odchylku (MSE) mezi odhadem a originálem.
    * Vzorec bere v úvahu **poměr Signál/Šum (SNR)**.
    * *Vlastnost:* Najde kompromis mezi "odstraněním rozmazání" a "nezvýrazněním šumu".

---

## 4. Blind Deconvolution (Neznámá PSF)
Co když neznáme masku rozmazání?

### Jak odhadnout PSF?
1.  **Senzory:** Gyroskop/akcelerometr v telefonu.
2.  **Experiment:** Vyfocení bodového zdroje (hvězda) $\to$ Obraz hvězdy JE přímo PSF.
3.  **Ze spektra:** Nulové body ve Fourierově spektru odpovídají tvaru PSF.
4.  **Z hran:** Analýza profilu hran (rozmazaná hrana napoví tvar filtru).

### Variabilní PSF (Space Variant)
* Pokud se PSF mění (např. rotace), převedeme souřadnice (polární), aby se pohyb stal lineárním.
* Nebo rozdělíme obraz na segmenty, kde je PSF cca konstantní.

---

## 5. Pokročilé techniky (Více obrázků)

### Multichannel Restoration
* Vstup: Více rozmazaných fotek téže scény (s různým rozmazáním).
* Empirie: Více než **4 obrázky** už moc nepomáhají. Největší skok je mezi 1 a 2.
* Podmínka: Obrázky musí být perfektně zarovnané (registrované).

### Multifocus Fusion
* Skládání fotek s různou hloubkou ostrosti (např. mikroskopie).
* **Princip:** Nepoužívá konvoluci.
    * Detekuje hrany/gradienty v každém snímku.
    * Pro každou část složeného obrázku vybere ten snímek, kde je daná oblast nejostřejší.

### Super-resolution
* Získání vyššího rozlišení z více snímků s nízkým rozlišením.
* Podmínka: Kamera se musí **pohnout o sub-pixelovou vzdálenost** (mikropohyby).
* Naivní metoda: Zregistrovat a "proložit" pixely do hustší mřížky.
* Realistická metoda: Minimalizace funkcionálu s downsampling/upsampling faktorem.

--- 
# Image Registration (Registrace obrazu)

Proces zarovnání dvou a více obrazů stejné scény do jednoho souřadnicového systému.
* **Reference image:** Ten, který stojí.
* **Sensed image:** Ten, který transformujeme na referenční.

---

## 1. Geometrické deformace
* **Projektivní geometrie:** Zachovává přímky (jmenovatel v rovnici je stejný).
* **Zkreslení čočky (Lens distortion):**
    * Barrel (Soudkovité - GoPro).
    * Pincushion (Poduškovité).
    * Fish-eye (Rybí oko).

## 2. Postup registrace
Cíl: Přesnost překrytí (nikoliv odstranění deformace).

1.  **Feature Detection:** Výběr kontrolních bodů (CP).
2.  **Feature Matching:** Párování bodů.
3.  **Transform Model Estimation:** Výpočet parametrů deformace.
4.  **Resampling:** Přepočet obrazu.

---

## 3. Metody matchingu (Párování)

### A. Signal-based (Area-based)
Nepracuje s body, ale s celými okny pixelů.
* **Image Correlation:**
    * Hledá místo s největším korelačním koeficientem.
    * *Výhody:* Odolné vůči šumu a změně jasu (díky normalizaci). Funguje na satelitních snímcích.
    * *Nevýhody:* Pomalé. Umí jen posun (Shift).
* **Phase Correlation (Fázová korelace):**
    * Pracuje ve Fourierově doméně. Využívá "Whitening" (zahodí amplitudu, nechá jen fázi).
    * Cross-power spektrum dvou posunutých obrazů je **impulz (Delta funkce)** na místě posunu.
    * *Výhody:* Extrémně rychlé, robustní vůči jasu (nezajímá ho), zvládá multimodalitu (pokud sedí hrany).
    * *Trik na rotaci/škálování:* Fourier-Mellin transformace (převedeme amplitudu spektra do Log-Polárních souřadnic $\to$ rotace a scale se změní na posun).

### B. Feature-based
Hledáme význačné body (rohy, blobs) a párujeme je.
* Vhodné pro: Multimodální data (MRI vs CT), velké deformace.
* **Vlastnosti bodů:** Distinktivní, rozprostřené po obraze, invariantní vůči šumu.
* **Metody párování:**
    * Kombinatorické (zkoušíme všechny dvojice).
    * Feature space clustering.

---

## 4. Transformační modely
Jak moc se může obraz deformovat?

Krok, kdy na základě nalezených dvojic bodů (Matched Points) hledáme matematickou funkci, která převede celý obraz "Sensed" na "Reference".

### 1. Globální modely
Používáme jednu transformační rovnici pro celý obraz. Předpokládáme, že deformace je všude stejného charakteru.

#### A. Afinní transformace (Affine)
* **Vlastnosti:**
    * Zachovává **rovnoběžnost přímek** (Parallelism).
    * Čtverec $\to$ Kosodélník (Parallelogram).
    * Operace: Posun (Translation), Rotace, Měřítko (Scale - isotropní i neisotropní), Zkosení (Shear/Skew).
* **Určení:**
    * Model má **6 neznámých parametrů**.
    * Potřebujeme minimálně **3 body** (trojúhelník).

#### B. Projektivní transformace (Projective)
* **Vlastnosti:**
    * Zachovává **přímost přímek** (Straight lines), ale **NE rovnoběžnost**.
    * Čtverec $\to$ Obecný čtyřúhelník (Lichoběžník).
    * Simuluje perspektivu (sbíhání kolejí) nebo focení plochy pod úhlem (keystone).
* **Určení:**
    * Model má **8 neznámých parametrů**.
    * Potřebujeme minimálně **4 body**.

#### C. Prokládání více body (Fitting)
Pokud máme více bodů než minimum (přeurčená soustava), body nezahazujeme!
* **Least-Squares Fit (Metoda nejmenších čtverců):**
    * Hledáme parametry, které minimalizují součet druhých mocnin chyb (vzdáleností mezi transformovaným bodem a cílem).
    * **Proč druhé mocniny?** Předpokládáme, že chyby (šum v detekci bodů) mají **Normální (Gaussovské) rozdělení**.
* **Standard Least Squares:** Předpokládáme chybu jen v jednom obrázku.
* **Total Least Squares:** Předpokládáme chybu v obou souřadnicích (složitější, méně časté).

---

## 2. Lokální modely (Elastic Registration)
Používáme, když je deformace komplexní a nelze ji popsat jednou rovnicí (např. měkké tkáně, papír).

### A. Triangulace
* Obraz rozdělíme na trojúhelníky (vrcholy jsou kontrolní body).
* Uvnitř každého trojúhelníku použijeme Afinní transformaci.
* **Problém:** "Lámání" obrazu na hranách trojúhelníků. Není zajištěna hladkost (spojitost derivace).

### B. Thin-Plate Splines (TPS)
* **Fyzikální model:** Minimalizace ohybové energie tenkého plechu, který je deformován v kontrolních bodech.
* **Vlastnosti:**
    * Zaručuje **hladký přechod** (smooth) v celém obraze.
    * **Globální funkce s lokálním vlivem:** Deformace v jednom bodě ovlivňuje hlavně jeho okolí, vzdálené části zůstávají téměř netknuté.

---

## 5. Resampling (Převzorkování)
Klíčový krok při aplikaci transformace.

* **Forward Mapping (Špatně):**
    * Beru pixel ze zdroje a posílám ho do cíle.
    * *Problém:* Mohou vzniknout **díry** (moiré), pokud cíl zvětšuji.
* **Backward Mapping (Správně):**
    * Procházím pixely CÍLOVÉHO obrazu a ptám se: "Kam dopadnu ve zdroji?"
    * Dopadnu mimo mřížku (neceločíselné souřadnice) $\to$ Použiji **Interpolaci** (Bikubickou, Bilineární).
    * *Výhoda:* Žádné díry, plná síť.

### Chyby registrace
1.  **Lokalizační:** Špatně jsem našel bod (roh není přesně na rohu).
2.  **Matching:** Spojil jsem roh baráku s rohem auta (Nejhorší chyba).
3.  **Alignment:** Vybral jsem moc jednoduchý model (např. afinní na nelineární deformaci).


# Analýza obrazu (Image Analysis)

Zásadní změna oproti preprocessingu:
* **Vstup:** Obrázek.
* **Výstup:** Data / Příznaky (už ne obrázek!). Většinou bod v n-rozměrném **příznakovém prostoru** (Feature Space).
* **Cíl:** Klasifikace, měření, rozpoznávání.

---

## 1. Základní pojmy a Topologie

### 2D Objekt
* Je **binární** (pixel buď patří objektu [1], nebo pozadí [0]).
* Je konečný a má okraj.

### Sousednost pixelů (Connectivity)
Definuje, co považujeme za "jeden objekt".
* **4-okolí:** Sousedé jen nahoře, dole, vlevo, vpravo.
* **8-okolí:** Včetně diagonál.
* **Důsledek (Paradox):** Diagonální řada pixelů.
    * Ve 4-okolí: Hromada samostatných bodů.
    * V 8-okolí: Jedna souvislá čára.
* *Poznámka:* Neexistuje univerzální matematická definice "správné" segmentace. Správnost se určuje jen porovnáním s manuální anotací (Ground Truth).

---

## 2. Segmentace (Jednoduché metody)

Jak dostat z šedotónového obrázku binární objekt?

### A. Prahování (Thresholding)
Funguje pro scény s jasným kontrastem (např. černý text na bílém papíře).
* **Problém:** Jak najít optimální práh $T$?
    * Hledat "dolík mezi dvěma kopci" v histogramu je naivní (šum, nevýrazné kopce).
* **Řešení (Fisherovo kritérium / Otsu):**
    * Snažíme se, aby dvě vzniklé skupiny (popředí/pozadí) byly co **nejkompaktnější** (malý rozptyl) a co **nejdále od sebe**.
    * Optimalizujeme míru separability:
      $$J = \frac{(m_1 - m_2)^2}{\sigma_1^2 + \sigma_2^2} \rightarrow max$$
      (Rozdíl průměrů na druhou lomeno součtem rozptylů).

### B. Region Growing (Narůstání oblastí)
* Algoritmus typu "Floodfill" (plechovka v malování).
* **Princip:**
    1.  Zvolíme **Seed bod** (semínko) - manuálně nebo automaticky.
    2.  Oblast se rozrůstá do sousedů, pokud splňují **podmínku homogenity** (jsou barevně podobní).

---

## 3. Předzpracování binárních dat: Morfologie

Čištění tvarů pomocí **Strukturního elementu ($B$)** (maska, např. kruh nebo čtverec 3x3).

| Operace | Definice | Efekt na objekt |
| :--- | :--- | :--- |
| **Eroze** ($\ominus$) | Element musí být *celý* uvnitř. | **Zmenšuje objekt.** "Ohlodává" okraje. Odstraní malé výstupky a šum. |
| **Dilatace** ($\oplus$) | Stačí průnik elementu s objektem. | **Zvětšuje objekt.** "Nafukuje" okraje. Zaplní malé díry uvnitř. |
| **Otevření** (Opening) | Eroze $\to$ Dilatace | Odstraní tenké vyčuhující čáry ("chlupy") a drobný šum, ale **zachová velikost** objektu. |
| **Uzavření** (Closing) | Dilatace $\to$ Eroze | Slepí úzké praskliny a uzavře malé díry uvnitř objektu. |

---

## 4. Příznaky a Invariance (Feature Extraction)

Hledáme funkcionál (popis) $I$, který je **invariantní** vůči deformacím $D$ (posun, rotace, scale).
$$I(D(f)) = I(f)$$

### Jednoduché geometrické příznaky
* **Kompaktnost (Circularity):** $\frac{Obvod^2}{Obsah}$. (Kruh = 1, složité tvary > 1).
* **Konvexnost:** Poměr obsahu objektu a jeho konvexního obalu (gumička natažená okolo).
* **Elongation:** Poměr stran opsaného obdélníku (Čtverec = 1).

### Shape Vector (Tvarový vektor)
* **Princip:** Z těžiště vyšleme paprsek a měříme vzdálenost k okraji při rotaci o 360° (**Radiální funkce**).
* **Omezení:** Funguje **POUZE pro hvězdicové objekty** (paprsek protne okraj právě jednou).
* **Invariance:**
    * Převedeme 2D tvar na 1D signál (graf vzdálenosti v závislosti na úhlu).
    * Rotace objektu = Cyklický posun v grafu.
    * Měřítko objektu = Změna amplitudy grafu.

### Shape Matrix
* Vzorkování objektu do polární mřížky.
* **Výhoda:** Funguje i pro **ne-hvězdicové** objekty (spirály atd.).
* **Nevýhoda:** Složité řešení rotace (museli bychom rotovat celou matici).

---

## 5. Fourierovy deskriptory (Klíčové téma!)

Popis hranice objektu pomocí Fourierovy transformace.
1.  Souřadnice okraje $(x,y)$ bereme jako komplexní čísla $z = x + iy$.
2.  Získáme posloupnost $z_0, z_1, \dots, z_N$.
3.  Uděláme Fourierku $\to$ Koeficienty $Z_0, Z_1, \dots, Z_{n-1}$.

**Jak zajistit invarianci? (Algoritmus pro zkoušku):**

1.  **Posun (Translation):**
    * Posun objektu je přičtení konstanty ke všem bodům.
    * Ve spektru to změní jen nultý člen (DC složku).
    * **Řešení:** Zahodíme $Z_0$. Používáme $Z_1 \dots Z_{n-1}$.
2.  **Rotace (Rotation):**
    * Rotace o úhel $\alpha$ je v komplexní rovině násobení $e^{-i\alpha}$.
    * To mění fázi, ale ne velikost.
    * **Řešení:** Bereme absolutní hodnotu (modul) $|Z_n|$.
3.  **Měřítko (Scale):**
    * Zvětšení objektu $k$-krát násobí všechny koeficienty $k$.
    * **Řešení:** Normalizujeme vydělením prvním koeficientem. Výsledek: $\frac{|Z_n|}{|Z_1|}$.
4.  **Startovní bod (Starting point):**
    * Kde na hranici začneme měřit?
    * Změna startu je posun v čase $\to$ změna fáze.
    * **Řešení:** Stejné jako u rotace. Absolutní hodnota (amplituda spektra) je na posun v čase necitlivá.

---

## 6. Další transformace a Lokální příznaky

### Radonova transformace
* Projekce obrazu (sčítání sloupců) pod různými úhly natočení.
* Převádí rotaci obrazu na posun v Radonově prostoru.

### Curvature Scale Space (CSS)
* Sleduje **inflexní body** (změna konkávní $\leftrightarrow$ konvexní) při postupném vyhlazování hranice (Low-pass filtrací).
* **Výhoda:** Je to **Lokální** příznak. Pokud se změní jen kus objektu, změní se jen část příznaku (na rozdíl od Fouriera, který se rozsype celý).
* Invariantní vůči afinní transformaci.

### SIFT (Scale Invariant Feature Transform)
Nejznámější lokální příznak pro šedotónové obrázky. Robustní vůči zákrytu.

1.  **Detekce bodů:** Hledá extrémy v "Scale Space" (rozdíl Gaussovek - DoG). Najde "fleky" různých velikostí.
2.  **Filtrace:** Zahodí body na hranách (málo kontrastní), nechá rohy a průsečíky.
3.  **Deskriptor (HoG):**
    * V okolí bodu (4x4 pod-okna) spočítá gradienty.
    * Udělá **Histogram Gradientů (HoG)** - směry hran.
    * Celý histogram orotuje podle dominantního směru (tím zajistí rotační invarianci).
* **Výhoda:** Funguje, i když vidíme jen půlku objektu.
* **Nevýhoda:** Selže při rozmazání (Blur) nebo silném šumu.

### Momentové invarianty (Moments)
* Projekce obrázku na polynomiální bázi (např. $x^p y^q$).
* Extrémně matematicky propracované.
* **Nevýhoda:** Jsou **globální**. Potřebují vidět celý objekt. Nejsou tak robustní v praxi jako SIFT.

# Rozpoznávání a Klasifikace (Recognition)

Poslední fáze zpracování obrazu.
* **Vstup:** Vektor příznaků (z předchozí fáze analýzy).
* **Výstup:** Rozhodnutí / Třída (např. "Je to pes").

### Princip klasifikace
Cílem je rozdělit příznakový prostor na **přihrádky (regiony)**.
* **Pravidlo:** Jedna přihrádka nesmí odpovídat více třídám. (Ale jedna třída může být rozprostřena do více přihrádek).
* **Trénování:** Proces hledání a nastavování hranic mezi těmito přihrádkami.

---

## 1. Původ příznaků (Handcrafted vs. Learned)

### Handcrafted (Ručně navržené)
* **Definice:** Uživatel (expert) pevně definuje, co se bude měřit (např. "změř kulatost a spočítej Fourierovy koeficienty").
* **Kdy použít:** Pokud jsme schopni rozdíly mezi třídami **matematicky popsat**.
* **Výhoda:** Jsou rychlejší a často přesnější pro specifické, dobře definované úlohy.

### Learned (Naučené - Deep Learning)
* **Definice:** Síť si sama optimalizuje prostor příznaků. Vymýšlí si vlastní "filtry" (konvoluční jádra).
* **Kdy použít:** Pro generické třídy, které **nejsme schopni popsat rovnicí** (např. rozdíl mezi kočkou a psem).
* **Poznámka:** V moderním CV dominantní přístup.

---

## 2. Typy učení

1.  **Supervised (S učitelem):**
    * Třídy jsou předem definované.
    * Trénovací data mají štítky (Labels) $\to$ víme, co je správně.
2.  **Unsupervised (Bez učitele / Clustering):**
    * Třídy nejsou známé.
    * Algoritmus sám hledá shluky (clustery) podobných dat.

### ⚠️ Empirická pozorování (Reality Check)
* **Hranice nejsou ostré:** Rozhodovací hranice není v reálných datech jednoznačně daná.
* **Overtraining (Přeučení):** Snaha o 100% oddělení trénovacích množin je chyba.
    * Pokud se klasifikátor snaží vyhovět každému bodu (i šumu), "přeučí se" a na nových datech selže.
* **Chyba je nevyhnutelná:** Data nejsou vždy klasifikovatelná správně.

---

## 3. Proces rozhodování (Teorie)

Nerozhodujeme jen "podle citu", ale minimalizujeme matematické riziko.

1.  **Měření:** Získáme příznaky.
2.  **Klasifikace (Minimalizace chyby):**
    * Počítáme pravděpodobnost třídy.
    * **Apriorní pravděpodobnost (Priors):** Musíme zohlednit četnost výskytu tříd v realitě (např. "nemoc je vzácná"). Tuto konstantu odhadujeme z trénovací množiny.
3.  **Rozhodnutí (Minimalizace ztrátové funkce):**
    * Vážíme chyby podle jejich závažnosti (Loss function).
    * *Příklad:* Označit bombu jako kufr je horší chyba, než označit kufr jako bombu.
4.  **Akce:** HW výstup.

---

## 4. Klasifikátory

Dělíme je podle toho, zda používají pravděpodobnostní rozdělení dat.

### A. Deterministické (Geometrické)
Používáme, když **máme málo trénovacích dat** a nemůžeme spolehlivě odhadnout parametry rozdělení (např. Gaussovky).
* *Problém dimenze:* Počet parametrů normální distribuce roste kvadraticky s dimenzí ($N^2$). Málo dat v $N$-D prostoru = špatný statistický model.

#### 1. Minimum Distance (K těžišti)
* Spočítá se těžiště (mean) každé třídy. Bod se přiřadí k nejbližšímu těžišti.
* **Nevýhoda:** Špatně se přizpůsobuje tvaru množin (předpokládá koule).

#### 2. Nearest Neighbor (NN - 1-NN)
* Bod se přiřadí ke třídě svého **nejbližšího souseda**.
* **Nevýhoda:** Citlivé na **Outliers**. Jeden zašuměný bod hluboko v cizím území vytvoří kolem sebe "ostrůvek chyby".

#### 3. k-NN (k-Nearest Neighbors)
* Hledá $k$ nejbližších sousedů a hlasuje. Postupně rozšiřuje okolí, dokud nenajde $k$ bodů.
* **Parametr $k$:**
    * Je to uživatelský parametr (heustika).
    * **Malé $k$:** Citlivé na šum.
    * **Velké $k$:** Vyhlazuje hranici (odolné vůči šumu, ale může setřít detaily).
    * *Příklad:* $k=2$ zvládne 1 outlier, $k=3$ zvládne 2 outliery atd.



#### 4. Lineární klasifikátor (SVM - Support Vector Machine)
* Snaží se najít nadrovinu (čáru), která odděluje třídy s co největším odstupem.
* **Margin:** Vzdálenost hranice od nejbližších bodů. SVM maximalizuje margin.
* **Support Vectors:** Body, o které se hranice "opírá".
* **Soft Margin:** Řešení pro data, která nelze lineárně oddělit (nebo obsahují šum).
    * Maximalizujeme margin + **Penalizační člen** (pokuta za body na špatné straně).



#### B. Statistické (Bayes)
##### Bayesův klasifikátor 

V rozpoznávání se považuje za **statistický "Gold Standard"**.
Pokud máme dostatek dat a známe jejich rozdělení, matematicky **neexistuje přesnější klasifikátor** (má minimální teoretickou chybu).

* **Rozdíl oproti geometrickým (k-NN, SVM):** Nepočítá vzdálenosti v prostoru, ale **pravděpodobnosti**.
* **Princip:** Pro naměřený objekt vybereme tu třídu, která je **nejpravděpodobnější**.

---

### 1. Bayesovo pravidlo (The Formula)

Základní vzorec, který otáčí podmíněnou pravděpodobnost.

$$P(\omega_j | \mathbf{x}) = \frac{p(\mathbf{x} | \omega_j) \cdot P(\omega_j)}{p(\mathbf{x})}$$

### Vysvětlení členů (Slovníček)

1.  **$P(\omega_j | \mathbf{x})$ – A posteriori pravděpodobnost (Posterior)**
    * **TO, CO HLEDÁME.**
    * *"Jaká je pravděpodobnost, že to je **Třída J** (např. Pes), když jsem naměřil **Data X** (např. velké uši)?"*
    * Cílem klasifikace je najít třídu $\omega_j$, pro kterou je toto číslo největší.

2.  **$p(\mathbf{x} | \omega_j)$ – Věrohodnost (Likelihood / Class-conditional density)**
    * **TO, CO SE UČÍME Z DAT.**
    * *"Jaká je pravděpodobnost, že naměřím **Data X** (velké uši), pokud vím, že to je **Pes**?"*
    * Tohle nám říká tvar "kopce" (histogramu) trénovacích dat pro danou třídu.

3.  **$P(\omega_j)$ – A priori pravděpodobnost (Prior)**
    * **NAŠE ZKUŠENOST / KONTEXT.**
    * *"Jaká je pravděpodobnost výskytu **Psa** obecně?"*
    * Pokud jsi v psím útulku, je vysoká. Pokud v oceánu, je nulová. Funguje jako "váha" (pokud je nějaká třída vzácná, Bayes ji bude méně tipovat).

4.  **$p(\mathbf{x})$ – Evidence (Total probability)**
    * Pravděpodobnost výskytu znaku X obecně.
    * Pro porovnávání tříd (Pes vs. Kočka) je to jen konstanta (stejná pro oba). **Můžeme ji ignorovat.**

---

### 2. Rozhodovací pravidla (Jak vybrat vítěze?)

### A. Pravidlo minimální chyby (Minimum Error Rate)
Používáme, pokud jsou všechny chyby "stejně drahé".
* **Akce:** Vyber třídu s nejvyšší a posteriori pravděpodobností $P(\omega_j | \mathbf{x})$.
* Tím minimalizujeme počet špatných rozhodnutí.

### B. Pravidlo minimálního rizika (Minimum Risk)
Používáme, pokud mají chyby různou váhu (např. v medicíně).
* Zavádíme **Ztrátovou funkci (Loss Function) $\lambda_{ij}$**: *"Cena za to, že řeknu třídu $i$, ale pravda je $j$."*
* **Akce:** Vybereme třídu, která má nejmenší celkové **Riziko** (očekávanou ztrátu).
* *Příklad:* Raději označíme zdravého člověka za nemocného (malá ztráta, jde na test), než nemocného za zdravého (velká ztráta, smrt).

---

### 3. Bayes a Normální rozdělení (Parametrický přístup)

Abychom mohli použít vzorec, musíme znát člen **$p(\mathbf{x} | \omega_j)$** (Věrohodnost).
Nejčastěji předpokládáme, že data mají **Gaussovo (Normální) rozdělení**.

Třídu pak popíšeme jen dvěma parametry:
1.  **Střední hodnota ($\mu$):** Kde je střed třídy (těžiště).
2.  **Kovarianční matice ($\Sigma$):** Jaký má třída tvar a natočení.

### Co je Kovarianční matice ($\Sigma$)?
Je to "návod na tvar" té Gaussovy bubliny v N-dimenzionálním prostoru.

* **Diagonála matice (Rozptyly):** Říká, jak je bublina **tlustá** ve směru os (X, Y...).
* **Mimo diagonálu (Kovariance):** Říká, jak je bublina **natočená/šikmá**.
    * Pokud jsou kovariance nula $\to$ Třída má tvar koule nebo elipsy srovnané s osami.
    * Pokud jsou nenulové $\to$ Třída je "šikmá" (existuje závislost mezi příznaky).

#### Diskriminační funkce
Když dosadíme Gaussovku do Bayesova vzorce a zlogaritmujeme to (aby zmizela exponenciála), získáme **kvadratické rovnice**.
* Hranice mezi třídami nejsou rovné čáry, ale křivky (paraboly, hyperboly, elipsy).
* To umožňuje Bayesovi perfektně obalit data různých tvarů.

---

## 4. Problémy v praxi (Proč to nepoužíváme vždy?)

Aby Bayes fungoval, musíme přesně spočítat parametry ($\mu, \Sigma$) z trénovacích dat.

1.  **Problém dimenze:** Počet parametrů v Kovarianční matici roste kvadraticky s počtem příznaků ($N^2$).
2.  **Nedostatek dat:** Pokud máme málo obrázků a hodně příznaků, **nedokážeme Kovarianční matici spočítat** (bude singulární/nepřesná).
    * *Důsledek:* Bayesův klasifikátor selže ("nejsme schopni fitovat distribuci").
    * *Řešení:* Musíme použít jednodušší metody (např. Naive Bayes - předpokládáme, že kovariance je nula, nebo geometrické klasifikátory).

---

## 5. Konvoluční sítě (CNN) - Limity

V kontextu analýzy obrazu je chápeme jako metodu, která si "sama tvoří třídy/příznaky" (unsupervised/learned features část).

* **Problém s invariancí:**
    * Klasické CNN **nejsou** invariantní vůči rotaci a deformaci.
    * *Příklad:* Rotace objektu o 30° může snížit pravděpodobnost správné klasifikace z 95 % na 50 % (úroveň náhody).
* **Řešení:**
    1.  **Data Augmentation:** Trénovat i na otočených datech.
    2.  **Equivariant Networks:** Hybridní sítě navržené tak, aby rotaci zvládaly matematicky.
