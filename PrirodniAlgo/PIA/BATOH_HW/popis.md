# Popis genetického algoritmu pro problém batohu

Tento dokument popisuje návrh a implementaci genetického algoritmu pro řešení problému batohu (Knapsack problem).

## Kódování jedince
Kódování jedince je binární. Genotyp je reprezentován jednorozměrným polem (`array.array` s typem `b` pro úsporu paměti), kde hodnota `1` na $i$-tém indexu značí, že $i$-tý předmět je vložen do batohu, a hodnota `0` znamená, že předmět vybrán nebyl.

**Inicializace populace:** Generování počátečních jedinců využívá vychýlenou pravděpodobnost (`biased_coin_flip`), kde šance na vložení předmětu při inicializaci je $p = 5/n$ (kde $n$ je celkový počet předmětů). Zabraňuje se tak tomu, aby na začátku vznikali jedinci, kteří extrémně překračují kapacitu batohu, což by vedlo k neefektivnímu prohledávání.

## Fitness funkce a penalizace
Jedná se o optimalizační problém s jedním cílem (Single-objective Maximization), proto má váha fitness funkce hodnotu `(1.0,)`. Fitness skóre primárně odpovídá součtu cen (hodnot) všech předmětů v batohu.
* **Penalizace (Soft penalty):** Pokud dojde k překročení váhy (např. po křížení, které nekontroluje validitu bezprostředně), je hodnota batohu snížena relativní penalizací: $\text{cena} \cdot (1 - \text{penalty})$, kde $\text{penalty} = (\text{váha} - \text{max\_váha}) / \text{max\_váha}$. 

## Genetické operátory a heuristika
* **Křížení (Crossover):** Používá se dvoubodové křížení (`tools.cxTwoPoint`).
* **Mutace (Mutation):** Vybrána byla bit-flip mutace (`tools.mutFlipBit`), která s definovanou pravděpodobností invertuje jednotlivé geny.
* **Oprava (Repair heuristika):** Po provedení mutace je bezprostředně spuštěna heuristická funkce `repair`. Pokud mutace způsobí nedovolenou váhu, tato funkce vyřadí předměty z batohu (přepíše geny na `0`). Předměty se **řadí podle poměru cena/váha vzestupně**, tzn. z batohu se primárně vyhazují ty *nejméně výhodné* předměty tak dlouho, dokud se váha nevrátí do normy.

## Způsob selekce
Pro výběr rodičů do další generace byla zvolena **Turnajová selekce** (`tools.selTournament`). Parametr `tournsize` (velikost turnaje) je určen dynamicky na základě počtu předmětů: $\max(3, 1 + n/100)$. U vstupu s 1000 předměty je velikost turnaje `11`. Toto dynamické škálování zaručuje dostatečný selekční tlak, aby v rozsáhlém stavovém prostoru převážila lepší řešení poměrně brzy.

V algoritmu je navíc zapojen **Elitismus** (`tools.HallOfFame(1)`), který zaručuje, že v průběhu evoluce se nikdy neztratí globálně nejlepší dosud nalezené řešení.

## Hodnoty hyperparametrů a jejich zdůvodnění
* `population_size = 1000`: Pro 1000-dimenzionální stavový prostor je nutná velká populace, aby byla udržena potřebná genetická diverzita.
* `ngen = 100`: Počet generací dostačuje, protože algoritmus je posílen lokální prohledávací heuristikou (repair method), a konverguje tudíž velmi rychle.
* `cxpb = 0.5` (Pravděpodobnost křížení): U jedince je $50\%$ šance na to, že podstoupí křížení. Umožňuje sdílení informací o dobrých blocích mezi zdatnými rodiči.
* `mutpb = 0.35` (Pravděpodobnost mutace): Vcelku vysoká míra mutace ($35\%$) předchází zamrznutí v lokálních optimech, avšak nedestruuje populaci, protože každá "pokažená" mutace je zaléčena heuristickou opravou.
* `indpb = 0.06` (Pravděpodobnost mutace pro každý gen): Pro instanci velikosti 1000 to znamená, že zmutovaný jedinec změní průměrně ~60 genů. V čistém GA by tato hodnota mohla být příliš vysoká a destruktivní, nicméně v kombinaci s naší heuristickou "repair" funkcí takto velký krok funguje jako makromutace a efektivně prohledává okolní prostor při zachování validní váhy.


# Výsledky

Pro 'input1000.txt' jsem nalezl 54485 jako řešení. Pro input100  jsem nalezl 9147 jako řešení.
