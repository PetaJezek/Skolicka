Martin Pilát

    Výuka
    Výzkum

    English version

Umělá inteligence, výpočetní inteligence a jejich aplikace
Úvod a historie

Oblast umělé inteligence se dá zhruba rozdělit na dvě části - na symbolickou umělou inteligenci a na výpočetní umělou inteligenci. Symbolická umělá inteligence používá symbolický popis světa v nějakém formálním jazyce (např. logice) k řešení problémů např. z oblasti plánování a reprezentace znalostí. Oproti tomu výpočetní inteligence se zaměřuje na učení se chování z dostupných dat a pozorování. Přírodou inspirované algoritmy potom představují velkou část právě výpočetní inteligence.

Přírodou inspirované algoritmy obsahují širokou škálu technik, které v poslední době rychle získávají na popularitě v umělé inteligenci. Mezi nejznámější z nich patří umělé neuronové sítě a evoluční algoritmy. Především umělé neuronové sítě (v podobě tzv. hlubokého učení) dosahují dnes mnoha dobrých výsledků a překonávají tradiční metody v oblasti zpracování obrazu, zpětnovazebního učení, strojového překladu a dalších.

Neuronové sítě jsou inspirované fungováním nervové soustavy. Skládají se z jednoduchých výpočetních jednotek, tzv. neuronů, které jsou propojeny vahami. Při trénování neuronových sítí se právě tyto váhy upravují tak, aby výstupy sítě odpovídaly nějakým požadovaným výstupům. Evoluční algoritmy jsou zase optimalizační algoritmy inspirované Darwinistickou evolucí. Pracují s množinou (populací) kandidátů na řešení (jedinců). Běží v iteracích (generacích) a během každé generace aplikují genetické operátory (křížení a mutaci) na celou populaci. Jedinci, kteří představují kvalitnější řešení, mají větší šanci vytvořit nové potomky.

Zmíněné metody ale rozhodně nejsou nové. První experimenty s umělými neuronovými sítěmi pochází už ze 40. let. V roce 1959 Rosenblatt představuje perceptron, který se později stává základem moderních neuronových sítí. Vývoj neuronových sítí byl ale v 70. a 80. letech poznamenán nedůvěrou v jejich schopnosti, která vycházela především z knihy Perceptrons od Marvina Minského a Seymoura Paperta. Další rozvoj neuronových sítí potom přichází až ve druhé polovině 80. let po (znovu)objevení algoritmu zpětného šíření (backpropagation), který se dodnes používá k trénování neuronových sítí. V současnosti se různé architektury (hlubokých) neuronových sítí objevují v mnoha oblastech strojového učení a dávají nejlepší známé výsledky.

Myšlenka evolučních algoritmů také není nová. Jedny z prvních evolučních strategií (optimalizačních algoritmů pro spojitou optimalizaci, které se vyznačují tím, že automaticky adaptují svoje parametry) pochází už z konce 70. let. Genetický algoritmus jako takový potom z cca poloviny let 80. Dnes se evoluční algoritmy používají kromě samotné optimalizace, např. i k návrhu elektronických obvodů, nebo pro trénování neuronových sítí ve zpětnovazebním učení.
Strojové učení a optimalizace

Hlavními oblastmi aplikace přírodou inspirovaných algoritmů jsou strojové učení a optimalizace. Ve skutečnosti, jak uvidíme, mají tyto oblasti mnoho společného, neboť cílem strojového učení je typicky nastavení parametrů nějakého modelu tak, aby co nejlépe odpovídal dostupným datům. Oblast optimalizace je ale o něco obecnější.

Celá oblast strojového učení se dá rozdělit do třech oblastí:

    V učení s učitelem jsou zadané objekty a k nim příslušné výstupy. Cílem je najít model, který, pokud je mu zadaný nějaký objekt, správně přiřadí správný výstup. Výstupy mohou být dvou typů, buď kategorické, nebo číselné. V prvním případě je cílem přiřadit objekt do správné kategorie (např. rozhodnout, jestli je na obrázku pes, nebo kočka) a problém se nazývá klasifikace. Ve druhém případě je cílem na základě vstupních dat předpovědět číselnou hodnotu (např. cenu nemovitosti na základě informací o ní). Takový problém se nazývá regrese.
    V učení bez učitele jsou zadány pouze objekty bez požadovaných výstupů. Cílem typicky je např. rozdělit objekty do skupin obsahujících podobné objekty (shlukování), nebo se naučit, jak vstupní objekty vypadají, a generovat nové objekty (generativní modely).
    Ve zpětnovazebním učení je cílem naučit se chování nějakého agenta tak, aby co nejlépe řešil zadaný problém na základě zpětné vazby od prostředí, ve kterém se pohybuje. Můžeme si to představit třeba tak, že se snažíme naučit se novou hru tím, že zkoušíme provádět různé akce a díváme se, jak ovlivňují skóre.

Aplikace a výsledky

Přírodou inspirované metody dosáhly v posledních letech mnoha zajímavých výsledků. V oblasti evolučních algoritmů jsou každý rok vyhlašovány Humies awards za výsledky získané pomocí evolučních algoritmů, které mohou svou kvalitou soutěžit s výsledky získanými člověkem. Jedním z pěkných výsledků je např. návrh antény získaný pomocí genetického programování, která byla použita při testovací misi NASA. Evoluční algoritmy se také dají použít k evoluci neuronových sítí, např. pro vytvoření umělé inteligence pro hru Mario.

Neuronové sítě a dnes především hluboké neuronové sítě dosahují velmi dobrých výsledků např. při klasifikaci a zpracování obrazu. Pěkný výsledek je např. automatické vytváření popisků k obrázkům. Hluboké neuronové sítě ale také dosahují velmi dobrých výsledků ve zpětnovazebním učení a jsou schopny porazit lidské hráče v mnoha hrách, např. v Go, Starcraftu, nebo mnoha Atari hrách (článek můžete stáhnout po přihlášení dole - Access through your institution).
Mgr. Martin Pilát, Ph.D.
Malostranské náměstí 25
118 00 Praha
Martin.Pilat@mff.cuni.cz


Martin Pilát

    Výuka
    Výzkum

    English version

Zpětnovazební učení

Jednou z oblastí, kde se přírodou inspirované techniky často používají je zpětnovazební učení. Cílem zpětnovazebního učení je naučit se takové chování agenta, které maximalizuje jeho celkovou odměnu, kterou získá z prostředí, pokud bude dané chování používat. Předpokládáme, že agent se vyskytuje v nějakém prostředí, jehož stav může pozorovat a ovlivňovat. Agent běží v cyklech, v každé iteraci t pozoruje stav prostředí st, na základě pozorování provede akci at a tím převede prostředí do nového stavu st+1. Za provedení akce dostane od prostředí odměnu rt.

Jedním z typických ukázkových problémů pro zpětnovazební učení je Mountain Car. Jde o auto, které je v údolí a snaží se z něj dostat ven, má ale slabý motor, takže přímo vyjet nemůže a musí se “rozhoupat”. Stav je v tomto případě vektor dvou čísel udávajících polohu a rychlost auta. Auto může provádět tři akce - jet dopředu, jet dozadu, nebo nic. Pokud chceme, aby z údolí vyjelo co možná nejrychleji, dostává typicky odměnu -1 za každý krok v údolí a 0 v kroku, kdy vyjede (tím také simulace končí).
Markovské rozhodovací procesy

Prostředí můžeme formálně popsat jako markovský rozhodovací proces (MDP), který je zadaný čtveřicí (S,A,P,R), kde S je konečná množina stavů prostředí, A je (konečná) množina akcí (případně může být nahrazena množinami As akcí aplikovatelných ve stavu s), Pa(s,s′) je přechodová funkce, která udává pravděpodobnost, že aplikací akce a ve stavu s přejde prostředí do stavu s′ a Ra(s,s′) je funkce odměn, která udává okamžitou odměnu, kterou agent dostane od prostředí, pokud ve stavu s provede akci a a převede tím prostředí do stavu s′. U přechodové funkce je důležité, že splňuje tzv. markovskou podmínku, tj. že závisí pouze na aktuálním stavu s a akci a a nikoliv na akcích a stavech předcházejících.

Chování agenta potom můžeme popsat pomocí strategie (policy) π:S×A→[0,1], kde π(s,a) udává pravděpodobnost provedení akce a ve stavu s. Cílem zpětnovazebního učení je potom najít strategii π takovou, že maximalizuje celkovou odměnu, kterou agent získá ∑∞t=0γtRat(st,st+1), kde at=π(st) je akce provedená agentem v kroku t a γ<1 je diskontní faktor, který zajišťuje, že suma je konečná.
Hodnota stavu a hodnota akce

Hodnota Vπ(s) stavu s při použití strategie π se dá definovat jako Vπ(s)=E[R]=E[∑∞t=0γtrt|s0=s], kde R značí celkovou získanou diskontovanou odměnu a rt značí odměnu obdrženou v čase t. Kromě hodnoty stavu se velmi často hodí uvažovat také hodnotu Qπ(s,a) akce a provedené ve stavu s pokud budeme dále sledovat strategii π. Výhodou tohoto modelu je, že agent nepotřebuje mít model prostředí, který popisuje, jakým způsobem akce ovlivňují prostředí a učí se tento model za běhu.

Cílem agenta potom tedy je najít optimální strategii π⋆ takovou, že Vπ⋆(s)=maxπVπ(s). Hodnotu stavů (akcí) pro optimální strategii budeme značit jako V⋆(s) (Q⋆(s,a)).
Strategie prohledávání

Hodnotu obou výše zmíněných funkcí V i Q může agent použít k tomu, aby vylepšil svoji strategii. Je třeba si uvědomit, že agent má relativně složitou úlohu - musí se snažit maximalizovat svůj celkový zisk R, k tomu se musí naučit vhodnou strategii, která ale zpětně ovlivňuje hodnoty stavů odhadované agentem. Agent by mohl sledovat takovou strategii, která vždy přejde do stavu, který slibuje největší užitek. Problém je, že agent hodnoty jednotlivých stavů předem nezná a musí se je učit za běhu. Pokud tedy bude mít špatný (moc nízký) odhad hodnoty některého stavu, nemusí ho nikdy navštívit i přes to, že při použití jiné strategie by jeho hodnota byla o hodně lepší (například přes něj vede zkratka do cíle, kterou agent ještě neobjevil). Agent, který vždy vybírá nejlepší akci (hladový, nebo greedy, agent) tedy špatně prohledává prostředí a akce v něm dostupné. Výběr vhodné strategie pro učení je složitý problém, je potřeba vyvažovat prohledávání prostoru (exploraci) a využívání známého (exploataci). Jednou z populárních metod výběru akce ve zpětnovazebním učení je tzv. ϵ-hladová (ϵ-greedy) strategie. Ta s pravděpodobností (1−ϵ) vybere nejlepší akci a s pravděpodobností ϵ vybere akci náhodnou. Tím kombinuje jak využívání naučených znalostí, tak prohledávání nových stavů.
Monte-Carlo metody

Zpětnovazební učení si lze představit ve dvou krocích - zlepšení strategie a vyhodnocení strategie. Vyhodnocení strategie lze dělat pomocí Monte-Carlo metod, které počítají hodnoty funkce Qπ(s,a). Provedeme ve stavu s akci a a potom začneme provádět strategii π, dokud se nedostaneme do nějakého cíle. Obdrženou odměnu potom zaznamenáme. Vylepšení strategie se potom dělá tak, že se spočítá nová (hladová) strategie na základě právě nových hodnot Q(s,a).

Takto popsaná metoda nefunguje moc dobře. Pokud jsou rozptyly odměn pro akce a stavy velké, může konvergovat velmi pomalu. Navíc v jednom běhu ohodnocení upravíme hodnotu pouze pro jednu dvojici stavu a akce, nelze ji tedy použít pro větší markovské rozhodovací procesy.
Q-učení

Některé výše zmíněné problémy řeší tzv. temporal-difference (TD) metody. Ty jsou založeny na tzv. Bellmanových rovnicích, které říkají, že Vπ(s)=Eπ[r0+γVπ(s1)|s0=s]. Aktualizace hodnotové funkce se potom po každém kroku vyhodnocení strategie (každém kroku agenta) provede jako V(s)←V(s)+α(r+γV(s′)−V(s)), kde r+γV(s′) je nová cílová hodnota pro V(s). Výhodou oproti Monte Carlo metodám je, že se při jednom ohodnocení upraví hodnota více stavů. TD metody si můžeme představovat i tak, že se v nich informace o odměnách propaguje z cílových stavů (kde může být známa) do stavů předcházejících. Navíc tyto metody řeší problém rozdělení odměny v čase. Pokud agent dostane odměnu jen při dosažení cíle, TD metoda tuto odměnu rozdělí postupně mezi akce, které k tomuto cíli vedly.

Specifickým algoritmem založeným na TD metodách je Q-učení. To se přímo učí funkci Q(s,a). V tradičních případech je Q reprezentována jako matice, na začátku inicializovaná samými nulami. Potom v každém kroku agent postupně pozoruje stav st, provede akci at, dostane odměnu rt a pozoruje nový stav st+1. Na základě těchto informací upraví matici Q takto:

Qnew(st,at)←(1−α)⋅Q(st,at)+α⋅(rt+γ⋅maxaQ(st+1,a)),

kde α je parametr učení a akce at může být vybírána libovolnou z metod zmíněných výše.
SARSA

Algoritmus Q-učení je tzv. off-policy algoritmus, nezávisí totiž na žádné konkrétní strategii, kterou agent sleduje. Algoritmus SARSA je obdobný, výpočet Q se ale provádí podle vztahu Q(st,at)←Q(st,at)+α[rt+γQ(st+1,at+1)−Q(st,at)], kde akce at a at+1 jsou založené na strategii používané agentem.
Problémy ve zpětnovazebním učení

Tradiční implementace Q-učení pomocí matice má ten problém, že funguje jen v diskrétních prostorech a s diskrétními akcemi. První omezení se dá obejít tím, že stavy diskretizujeme, např. v příkladu na Mountain Car můžeme hodnoty polohy a rychlosti rozdělit do intervalů a stav reprezentovat jen intervalem, místo konkrétní hodnoty. Podobně můžeme řešit i problém se spojitými akcemi. Dalším problémem je, že stavové prostory mohou být hodně velké, to potom vede k tomu, že matice jsou také velké a algoritmus se učí pomalu, nebo vůbec.

Později uvidíme i metody, které se učí strategii přímo jako mapování ze stavu na akci - takové se spojitými akcemi problém mít nemusí a typicky nemají problémy ani s velikostí stavu.
Multi-agentní zpětnovazební učení

Zpětnovazební učení se dá použít i v případech, kdy je agentů více. Jedním z jednoduchých způsobů, jak algoritmy zobecnit je místo akce uvažovat n-tice akcí, v takovém případě ale složitost celého problému výrazně zvyšuje. Často používanou metodou je také tzv. self-learning, kde agent předpokládá, že ostatní agenti se chovají stejně jako on. Existují ale i metody založené na modelování chování ostatních agentů.

Jedním z hlavních problémů zpětnovazebního učení s více agenty je to, jak určit, komu přiřadit jakou část odměny. Odměna od prostředí je totiž stále jen jedna. Jednou z možností je určit odměnu daného agenta tak, že se podíváme, jakou odměnu bychom dostali, kdyby tento agent nic nedělal a jakou jsme dostali díky jeho akci - rozdíl mezi těmito dvěma čísly je odměna pro tohoto agenta.
Mgr. Martin Pilát, Ph.D.
Malostranské náměstí 25
118 00 Praha
Martin.Pilat@mff.cuni.cz

Martin Pilát

    Výuka
    Výzkum

    English version

Evoluční algoritmy - úvod

Jednou z nejznámějších přírodou inspirovaných technik jsou evoluční algoritmy. Jsou to obecné optimalizační heuristiky, které mají široké uplatnění v mnoha oblastech, od optimalizace reálných funkcí, přes kombinatorickou optimalizaci, až po vývoj elektronických obvodů, nebo neuronových sítí.

Evoluční algoritmy jsou inspirované (typicky) Darwinovou evoluční teorií. Dalo by se i říct, že evoluční algoritmy simulují život mnoha generací a to, jak je ovlivní selekční tlak prostředí. V evolučních algoritmech pracujeme s množinou kandidátů na řešení daného problému. Každý kandidát se nazývá jedinec a celé množině se říká populace. Evoluční algoritmus běží v iteracích (generacích) a v každé iteraci provede výběr jedinců, které nějak upraví (pomocí tzv. genetických operátorů) a následně vybere, kteří jedinci přežijí do další generace. Přednostně jsou vždy vybíráni jedinci, kteří lépe řeší zadaný problém. Kvalita řešení problému je daná tzv. fitness funkcí. Populace na začátku generace se označuje jako rodiče a populace na konci (po aplikaci genetických operátorů) jako potomci.
Jednoduchý genetický algoritmus

Klasickým příkladem evolučního algoritmu může být tzv. jednoduchý genetický algoritmus. V tom jsou jedinci kódováni jako posloupnosti bitů pevné délky. Fitness funkce (jako vždy) záleží na konkrétním řešeném problému. Na začátku algoritmu jsou jedinci v populaci inicializováni náhodně a je spočítána jejich fitness. Tito jedinci potom tvoří první populaci rodičů. Následně jsou vybrání rodiče, na které budou aplikovány genetické operátory. Výběr se provádí tak, že pravděpodobnost výběru daného jedince je přímo úměrná jeho fitness - tento způsob výběru se nazývá ruletová selekce. Výběr se provádí s opakováním, někteří jedinci tedy mohou být vybrání vícekrát, zatímco jiní nejsou vybráni vůbec. Potom jsou na tyhle vybrané jedince aplikovány genetické operátory - křížení a mutace. Křížení ma za úkol zkombinovat dvě řešení a vytvořit tak řešení nové. Zde se typicky používá tzv. jednobodové křížení - náhodně se vybere jeden bod v jedinci a nový potomek vznikne tak, že se překopíruje část z jednoho rodiče před tímto bodem a z druhého od tohoto bodu dále. Po křížení se ještě aplikuje mutace. V jednoduchém genetickém algoritmu to je typicky mutace, která náhodně změní některé bity v jedinci. Cílem mutace je zlepšit různorodost (diverzitu) populace. Nově vytvoření potomci potom nahradí původní rodiče a algoritmus pokračuje další generací.

Algoritmus může být popsán pomocí pseudokódu níže:

P_0 <- náhodně inicializuj populaci
t <- 0
dokud není konec
    vyhodnoť fitness jedinců v P_t
    M_t <- vyber rodiče pro aplikaci operátorů pomocí ruletové selekce z P_t
    O_t <- vytvoř populaci potomků aplikováním genetických operátorů na M_t
    P_{t+1} <- O_t
    t <- t+1

Fitness funkce je daná problémem, který chceme řešit a evoluční algoritmy ji vždy maximalizují. Typickým příkladem je tzv. problém OneMAX, kde chceme, aby jedinec reprezentovaný jako binární řetězec obsahoval co nejvíce jedniček. V takovém případě můžeme fitness definovat jako počet jedniček v jedinci. Tento příklad není prakticky moc užitečný, stejným způsobem ale můžeme reprezentovat i známý problém nalezení podmnožiny nějaké zadané množiny, takové, že součet prvků v této podmnožině je nějaké zadané číslo. Jednička v jedinci na pozici i
potom znamená, že i

-tý předmět je vybraný do podmnožiny. Fitness se pak dá počítat jako rozdíl součtu všech čísel v množině a absolutní hodnoty rozdílu požadované hodnoty a součtu prvků v podmnožině (chceme minimalizovat absolutní hodnotu rozdílu, protože evoluční algoritmy maximalizují fitness, musíme ji odečíst od nějakého vhodně velkého čísla - např. součtu všech čísel).
Varianty evolučních algoritmů

Jednoduchý genetický algoritmus je jen jedním příkladem evolučních algoritmů. Můžeme si všimnout, že mnoho jeho částí jde snadno nahradit nějakou jinou variantou. Například můžeme změnit selekci, genetické operátory a způsob jakým vzniká nová populace ze staré. Kromě toho můžeme změnit i způsob kódování řešení v jedinci.
Selekce

Zatím jsme zmínili ruletovou selekci, kde pravděpodobnost výběru jedince je přímo úměrná jeho fitness - formálněji pravděpodobnost pi
výběru jedince i se spočítá jako pi=ft∑Nj=1fj, kde fj je fitness jedince j

. Velkou nevýhodou této selekce je, že záleží přímo na hodnotách fitness, pokud tedy fitness změníme tak, že k ní přičteme nějakou velkou konstantu, rozdíly mezi jedinci se zmenší a selekce se začne chovat náhodně. Toho se samozřejmě dá i využít, pokud chceme zesílit/zeslabit vliv selekce.

Alternativ k ruletové selekci existuje celá řada. My zmíníme teď jen jednu a to je turnajová selekce - v té se napřed náhodně vybere několik (typicky 2) jedinců, porovná se jejich fitness a selekce potom s velkou pravděpodobností (třeba 80 %) vybere toho lepšího z nich. Výhodou turnajové selekce je, že její výsledek záleží jen na pořadí jedinců podle fitness, navíc funguje i pro záporné hodnoty fitness.
Genetické operátory

Genetické operátory úzce souvisí s tím, jak je jedinec zakódovaný. Pro binární kódování a jiná kódování založená na posloupnostech konstantní délky se často používá např. již zmíněné jednobodové křížení. To se dá zobecnit na n
-bodové křížení, kde se místo jednoho bodu pro křížení jich zvolí n

a potomci potom vznikají tak, že se alternuje, z jakého rodiče je vybrána jaká část. Kromě toho se ještě občas uvažuje tzv. uniformní křížení, kde se u každé pozice znovu náhodně rozhodujeme, ze kterého rodiče dosadíme hodnotu do potomka.
Přenos jedinců do další generace

V jednoduchém genetickém algoritmu je další generace tvořena přímo potomky vytvořenými v generaci předcházející. Z toho důvodu také musí být počet rodičů a potomků stále stejný. Nevýhodou je i to, že genetické operátory mohou rozbít nejlepší zatím nalezené řešení. Ztrátě nejlepšího řešení se zabraňuje pomocí techniky, které se říká elitismus. V algoritmech s elitismem se typicky malá část nejlepších rodičů rovnou zkopíruje do další generace. Z potomků je potom potřeba vybrat jen tolik, aby se populace naplnila. K výběru se mohou používat stejné selekce jako k výběru před aplikací genetických operátorů.

Je také možné generovat jiný počet potomků, než kolik je rodičů. Práci s populací potom můžeme popsat pomocí notace z evolučních strategií (budou později) jako (μ,λ)
nebo (μ+λ). Zápis značí, že z populace μ rodičů se vygeneruje λ potomků. V prvním případě se potom další populace vybírá jako μ nejlepších z λ potomků (a tedy nutně λ>μ), ve druhém případě se další populace vybírá jako μ nejlepších z rodičů i potomků (a někdy dokonce λ=1

- v tzv. steady-state algoritmech).

V příští přednášce se podíváme na další možnosti kódování jedince a s tím související genetické operátory.
Mgr. Martin Pilát, Ph.D.
Malostranské náměstí 25
118 00 Praha
Martin.Pilat@mff.cuni.cz

Martin Pilát

    Výuka
    Výzkum

    English version

Evoluční algoritmy - spojitá a kombinatorická optimalizace

Minule jsme si povídali o jednoduchém genetickém algoritmu a jeho variantách vzhledem k různým genetickým operátorům a selekcím. Dneska se podíváme především na jiné způsoby, jak kódovat jedince. Ukážeme si i nějaké další aplikace evolučních algoritmů.
Celočíselné kódování

Nejjednodušším rozšířením binárního kódování je celočíselné kódování, tedy zakódování jedince pomocí celých čísel. Takové kódování se hodí např. pokud cílem je řešit problém rozdělení množiny N
čísel na k podmnožin se stejným součtem. Jedince potom reprezentujeme jako vektor N čísel mezi 0 a k−1. Číslo na pozici i potom říká, do které podmnožiny patří i

-té číslo ze vstupní množiny. Využití ale je i více, podobně se dá kódovat i obarvení grafu a jiné problémy.

Pro celočíselné kódování můžeme používat jednoduchá zobecnění operátorů pro binární kódování. Implementace křížení dokonce ani nemusíme měnit - fungují pořád stejně, protože jedinec je stále vektor. Pro mutaci je možné vybrat několik variant. Například můžeme na dané pozici změnit číslo na libovolné jiné, nebo, pokud to pro daný problém dává smysl, číslo zvětšit (případně zmenšit) o 1, nebo jinou konstantu.
Permutační kódování

Speciálním případem celočíselného kódování je permutační kódování. V tom je jedinec také kódován jako seznam čísel od 0 do k

, zároveň ale chceme, aby se každé číslo v jedinci objevilo právě jednou. Takové kódování se hodí při řešení mnoha kombinatorických problémů. Typickým příkladem je známý problém obchodního cestujícího, tedy hledání nejkratší kružnice v úplném grafu, která prochází přes všechny vrcholy. Permutace potom udává pořadí, v jakém máme navštívit vrcholy.

Permutační kódování se ale používá i v jiných problémech, často jako vstup pro heuristiku, která problém dále řeší. Například při řešení tzv. bin packing problému (naskládání objektů daných velikostí mezi 0 a 1 do přihrádek s jednotkovou velikostí tak, aby bylo přihrádek použito co nejméně), se dá použít tzv. first-fit heuristika, kdy se objekt dá do první přihrádky, kam se vejde, a pokud taková není, tak se vytvoří nová. Tato heuristika na vstupu potřebuje pořadí, ve kterém má objekty zkoušet přidávat - to je dané právě jako permutace.

Největší komplikací pro permutační kódování je, jak vytvořit operátory. Jednoduché operátory pro celočíselné kódování velmi často vytvoří potomky, kteří nebudou permutace. Vymyslet mutaci, která vždy vrátí validní jedince je snadné a máme několik variant. Jedním příkladem může být mutace, která v jedinci prohodí hodnoty na dvou různých pozicích. Můžeme ale mít i mutaci, která podobným způsobem přesune nějakou část jedince na jiné místo, nebo nějakou část otočí pozpátku. To jaká mutace se hodí pro jaký problém závisí na tom, co kódování přesně vyjadřuje.

Větším problémem je, jak vytvořit křížení. Typickým přístupem zde je udělat něco jako 2-bodové křížení a potom opravit vzniklé řešení. Například Order Crossover (OX) funguje tak, že prohodí prostřední část obou rodičů a zbylé pozice v potomcích doplní podle jejich pořadí ve druhém rodiči (začíná se vpravo od druhého křížícího bodu).

12|345|678      ..|186|...      45|186|723 (přeskakujeme čísla 186)
            ->              ->
34|186|527      ..|345|...      86|345|271 (přeskakujeme čísla 345)

Dalším populárním příkladem křížení je Partially Mapped Crossover (PMX). V tom se opět napřed prohodí “prostřední” části jedince. Následně se ještě doplní hodnoty, které zatím v jedinci nejsou na jejich pozice z druhého rodiče. Zbytek se potom doplní tak, že prohozené dvojice v prostřední části udávají mapování, jakou hodnotou se má co nahradit. Například níže, chceme najít hodnotu na první místo prvního jedince. Původně tam byla hodnota 1, ale ta už je v prohozené části. Tam se ale nahrazovala za hodnotu 3, která ještě v jedinci není - místo 1 tedy dáme na tuto pozici hodnotu 3. Pro ostatní pozice podobně. Občas se může stát, že řetězec nahrazení je delší, protože i prohozená hodnota v daném jedinci je. V takovém případě postupujeme úplně stejně s novou hodnotou.

12|345|678      .2|186|.7.      32|186|574 (1->3, 6->5, 8->4)
            ->              ->
34|186|527      ..|345|.27      18|345|627 (3->1, 4->8, 5->6)

Speciálně pro problém obchodního cestujícího se potom ještě často používá tzv. Edge Recombination (ER). V tomto křížení je cílem kombinovat hrany z obou řešení do jednoho. Ke každému vrcholu (hodnotě v jedinci) se tedy vyhledají všechny vrcholy, které s ním v jednom nebo ve druhém jedinci sousedí (nezapomeňte, že první sousedí s posledním - hledáme kružnice). Potom se začne vrcholem, který má nejkratší seznam sousedů. Z těch se zase vybere ten, který má nejkratší seznam sousedů a ten se dá na druhé místo. Oba vrcholy se vyškrtnou ze seznamů sousedů všech ostatních vrcholů. Stejně se potom postupuje s dalšími sousedy, přičemž pokud má více vrcholů stejný (nejmenší) počet sousedů, vybere se jeden z nich náhodně.
Spojitá optimalizace - kódování pomocí reálných čísel

Velmi častou oblastí, kde se používají evoluční algoritmy je optimalizace funkcí Rn→R

. Pomocí takových funkcí je možné zakódovat mnoho praktických problémů od ladění parametrů různých procesů, přes problémy strojového učení, až po hledání vah neuronových sítí - například ve zpětnovazebním učení.

Pro spojitou optimalizaci jsou jedinci kódovaní jako vektory čísel (typicky typu float, nebo double). V takovém případě je relativně snadné vymyslet nějaké genetické operátory. Mutace pro spojité kódování se dělí na dva typy - zatížené (biased) a nezatížené (unbiased). Nezatížené mutace prostě vygenerují nové číslo z rozsahu pro danou proměnnou, naopak zatížené mutace vychází z hodnoty, která se na dané pozici už vyskytuje a pouze ji upraví. Typickým příkladem je Gaussovská mutace, která k danému číslu přičte hodnotu z normálního rozdělení se střední hodnotou 0 a nějakým vhodným rozptylem.

Pro křížení existuje také několik variant - můžeme opět používat n

-bodová křížení, která už známe, nebo můžeme používat tzv. aritmetická křížení, kde se potomek získá jako vážený průměr rodičů.

Problém výše zmíněných operátorů je, že mutují/kříží každou souřadnici vektoru nezávisle. Tohle dobře funguje pro separabilní funkce, tj. takové, které lze optimalizovat po složkách (zafixujeme všechny proměnné kromě jedné, přes tu najdeme optimum a máme jednu souřadnici optima). Navíc tyto operátory dělají ve všech směrech stejně velké změny a tedy nefungují dobře pro funkce, které mají vysokou podmíněnost. Představte si například funkci, jejíž vrstevnice jsou elipsy - funkce s malou podmíněností má obě osy elipsy skoro stejně dlouhé, vysoce podmíněné funkce mají naopak velký poměr délek os. Pokud jsou osy rovnoběžné s osami soustavy souřadnic, máme separabilní funkci. Pokud nejsou, je funkce neseparabilní.

Existuje relativně velké množství evolučních algoritmů, které řeší problémy s neseparabilitou a podmíněností funkcí. My si ukážeme jen tzv. diferenciální evoluci (DE}. V diferenciální evoluci se provádí mutace, která k danému jedinci přičte rozdíl dvou náhodně zvolených jedinců z populace. Díky tomu je tato mutace invariantní vůči libovolným rotacím a škálováním prohledávaného prostoru. Nevadí jí tedy ani neseparabilní nebo vysoce podmíněné funkce. Kromě této mutace se ještě provádí v zásadě uniformní křížení s dalším náhodným jedincem. V rámci selekce se potom potomek porovná s rodičem a v populaci se nechá jen lepší z nich.
Mgr. Martin Pilát, Ph.D.
Malostranské náměstí 25
118 00 Praha
Martin.Pilat@mff.cuni.cz


Martin Pilát

    Výuka
    Výzkum

    English version

Evoluční algoritmy - genetické programování

Zatím jsme se bavili o použití evolučních algoritmů v případě, kdy se řešení dalo zakódovat do jednoduché struktury - vektoru nějakých hodnot - a všichni jedinci měli stejnou délku tohoto vektoru. Dnes se podíváme na několik příkladů, kde je struktura řešení složitější.
Genetické programování

Genetické programování je technika, která umožňuje pomocí evolučních algoritmů automatiky vytvářet programy. Často jen ve formě výrazů. Lze ji ale použít (jak uvidíme níže) k návrhu elektronických obvodů a podobných komplikovaných struktur. Existuje mnoho forem genetického programování podle toho, jakým způsobem je zakódovaný jedinec. My se podíváme na několik z nich. Velmi oblíbenou knihou o genetickém programování je Field Guide to Genetic Programming (je ke stažení zdarma).
Lineární genetické programování

V lineárním genetickém programování je jedinec zapsaný jako posloupnost instrukcí, které se potom provádí na nějakém simulovaném počítači. Příkladem lineárního genetického programu může být například (z Wikipedie).

input/   # gets an input from user and saves it to register F
0/       # sets register I = 0
save/    # saves content of F into data vector D[I] (i.e. D[0] := F)
input/   # gets another input, saves to F
add/     # adds to F current data pointed to by I (i.e. F := F + D[0])
output/. # outputs result from F

Program je zapsaný v jazyce Slash/A, který používá dva registry F
(pro floaty a vstup/výstup) a I (pro indexování do D) a pole hodnot D

. Na stránkách jazyka můžete vidět i složitější programy v něm napsané.

Operace s jedinci v lineárním genetickém programování jsou relativně jednoduché. Sice už nemají všichni jedinci stejnou délku jako dříve, ale pořád je možné dělat například mutace, které změní instrukci za nějakou jinou, nebo můžeme křížit jedince tak, že zkombinujeme části z jednoho programu s částmi z jiného programu.
Kartézské genetické programování

V kartézském genetickém programování (Cartesian GP), jedinec kóduje program zadaný na mřížce r×l
, která má r řádek a l vrstev (sloupců). Jedinec je potom vektor r×l

genů, a každý gen se skládá ze dvou částí - kódu (jména) funkce, kterou počítá, a indexů do předchozích vrstev, ze kterých bere vstupy. V první vrstvě indexy ukazují do pole vstupů. Navíc pro každý požadovaný výstup jedinec obsahuje index, kde se tento výstup v něm počítá.

V kartézském genetickém programování se typicky používá jen mutace, která změní funkci, její vstupy, nebo výstup programu.
Gramatická evoluce

V gramatické evoluci se využívá formálního zápisu syntaxe programovacího jazyka pomocí bezkontextové gramatiky. Jedinec je potom kódován jako posloupnost čísel, která určuje, jaké pravidlo z gramatiky se má použít pro přepis aktuálně prvního neterminálu. Protože pravidel pro každý neterminál může být více, nezáleží přímo na konkrétní hodnotě, ale bere se pravidlo, které se spočítá z hodnoty modulo počet možností.

Problémem v gramatické evoluci je, když je jedinec moc krátký a po jeho zpracování zbydou ve výrazu ještě nějaké neterminály. Takový jedinec potom nemůže být vyhodnocen. Tomu se zabraňuje tím, že se snažíme generovat delší jedince - pokud jedinec nepoužije některé své geny, tak to až tak nevadí.

Jako operátory můžeme zase používat varianty známých n

-bodových operátorů a mutací, které náhodně mění některé geny v jedinci. Kromě toho ale můžeme použít i křížení, které vybere z každého jedince gen, kde se začíná zpracovávat nějaký neterminál a prohodí ho s pozicí ve druhém jedinci, kde se objeví ten samý neterminál. Kromě této pozice se prohazují i další geny, které se týkají zpracování tohoto neterminálu (tj. dokud se nepřejde na další neterminál v jedinci před zpracováním tohoto). Toto křížení vlastně prohazuje celé podstromy mezi danými jedinci. Velkou výhodou tohoto křížení je, že dává sémanticky smysl a navíc pokud máme dva validní rodiče, tak vždy vytvoří validního potomka.
Stromové genetické programování

Stromové genetické programování (běžněji označované jen jako genetické programování) reprezentuje jedince pomocí stromu, který v uzlech obsahuje funkce (neterminály) a v listech vstupy nebo konstanty (terminály). Strom se potom vyhodnocuje od listů ke kořeni. Hodnota kořene je potom výstup programu.

Taková reprezentace umožňuje implementovat celou škálu různých rozumných genetických operátorů a pro genetické programování je typické, že se operátorů používá relativně velké množství najednou. Typickými příklady operátorů jsou křížení, která prohazují podstromy, nebo mutace, které změní terminál/neterminál na nějaký jiný. Další mutace potom třeba nahradí podstrom novým, náhodně vygenerovaným, případě rovnou terminálem.

V genetickém programování je i problém, jak inicializovat počáteční populaci - jednou z možností je generovat náhodné stromy s nějakou pevně danou hloubkou (v této hloubce už se vždy použije terminál), nebo s daným počtem neterminálů (zbytek stromu se opět doplní terminály). Nejčastěji se asi používá varianta těchto dvou přístupů, kdy každý generuje polovinu populace (tomuto přístupu se říká ramped half-and-half).

Otázkou také je, jak v genetickém programování pracovat s číselnými konstantami. Není úplně možné dát všechna čísla mezi terminály - bylo by jich pak moc. Často se zadávají mezi terminály jen základní konstanty (0, 1, 2, apod.) a předpokládá se, že si program další hodnoty spočítá sám z nich. Další možností je mít speciální operátory, které mění hodnoty konstant podobně jako se to dělá ve spojité optimalizaci.

Základní genetické programování popsané výše má řadu rozšíření. V programech se např. často pracuje s hodnotami různých typů jako jsou čísla nebo boolean. To je možné i v genetickém programování, stačí k jednotlivým neterminálům připsat, jaké mají typy vstupů a výstupů. Operátory s tím potom musí umět pracovat. Přidáním typů dostáváme typované genetické programování.

Dalším rozšířením jsou tzv. automaticky definované funkce, kdy dáme algoritmu možnost vytvořit si vlastní definice některých neterminálů. Ty potom může volat na různých místech programu. Někdy se v automaticky definovaných funkcích omezuje množina vstupů, nebo možných neterminálů tak, aby se programu pomohlo s prohledáváním.
Evoluce pravidel

Další oblastí, kde se používají jedinci se složitějším kódováním je strojové učení a evoluce klasifikačních pravidel. V té jedinci reprezentují množinu pravidel, která se snaží klasifikovat zadané vstupy. Např. pokud je vstupem vektor n
čísel, tak jedinec může být množina pravidel typu c1,c2,cn→k, která znamená, že pokud pro každé i pro i-tý vstup platí podmínka ci potom objekt patří do třídy k

. Je potřeba nějak vyřešit situaci, kdy daný objekt splňuje všechny podmínky pro více pravidel. Potom můžeme nechat pravidla hlasovat (tj. přiřadíme jako třídu tu nejčastější), nebo se můžeme rozhodnout podle prvního splněného pravidla (potom ale záleží na pořadí v jedinci).

Máme celou řadu genetických operátorů, které můžeme pro zadanou reprezentaci jedince využít - křížení může opět probíhat relativně jednoduše tak, že se zkombinují pravidla z obou rodičů. Pro mutace můžeme například měnit předpovězenou třídu pro dané pravidlo, měnit podmínky na levé straně pravidla (buď za jiné podmínky, nebo v nich upravovat třeba konstanty pokud tam nějaké jsou). V případě, že mají pravidla různé váhy, můžeme měnit i ty.
Mgr. Martin Pilát, Ph.D.
Malostranské náměstí 25
118 00 Praha
Martin.Pilat@mff.cuni.cz


Martin Pilát

    Výuka
    Výzkum

    English version

Hejna a kolonie

V dnešní přednášce se podíváme na další přírodou inspirované algoritmy pro optimalizaci. Konkrétně na algoritmus Particle Swarm Optimization (PSO), který je inspirovaný pohybem hejn ptáků, a na Ant Colony Optimization (ACO), který je inspirovaný chováním mravenců. Nakonec se stručně podíváme i na další přírodou inspirované algoritmy.
Particle Swarm Optimization (PSO)

Optimalizace hejnem částic (PSO) je optimalizační algoritmus inspirovaný chováním hejn ryb nebo ptáků. Je to algoritmus určený pro spojitou optimalizaci, který používá množinu (populaci) částic. Každá částice je reprezentována jako dva vektory v Rn - jeden z nich je její pozice (x) a druhý je její rychlost (v). Navíc si každá částice pamatuje pozici (vektor) v prostoru, kde měla nejlepší hodnotu fitness (pbest) a místo, kde je nejlepší hodnota fitness pro celou populaci (gbest).

Celý algoritmus PSO je potom velmi jednoduchý. Je založený na tom, že každá částice se pohybuje v prostoru a přitom je přitahována k místům, kde sama našla své nejlepší řešení, a kde je zatím nejlepší globální řešení. Na počátku se pozice částic inicializují náhodně v prohledávaném prostoru a potom algoritmus iterativně aktualizuje rychlosti a pozice všech částic podle rovnic v←ωv+φprp(pbest−x)+φbrb(gbest−x)

x←x+v,

kde rp,rb jsou náhodná čísla mezi 0 a 1 (často různá pro různé souřadnice) a ω,φp,φb jsou parametry, které určují setrvačnost a jak moc je jedinec přitahován ke svému a ke globálnímu nejlepšímu řešení.

Takto popsaný algoritmus PSO používá tzv. globální topologii, tj. všechny částice mohou přímo komunikovat se všemi (a sdílet tak informaci o globálním optimu). Existují i varianty PSO, které používají jen lokální topologii, tedy částice mohou komunikovat jen s nějakou podmnožinou hejna, ta potom sdílí lokální nejlepší řešení. Pro výběr topologie existují v zásadě dvě možnosti - buď geometrická, kde spolu komunikují částice, které jsou blízko u sebe, nebo sociální, kde je topologie určena předem, bez ohledu na pozice částic. Ve druhém případě se často používá kruhová topologie, kde každá částice má jen dva sousedy.

PSO se typicky používá pro spojitou optimalizaci a pro tento případ není nutné algoritmus nijak upravovat - pozice částic přímo reprezentují kandidáty na řešení a jejich kvalita je určena podle hodnoty optimalizované funkce. Algoritmus se ale dá použít i pro řešení jiných typů problémů - diskrétních a kombinatorických. Pro celočíselnou optimalizaci se často počítá s reálnými čísly a výsledky se potom zaokrouhlí. Pro obecnější kombinatorickou optimalizaci je potřeba nějakým způsobem definovat operace, které se používají v rovnicích. Jednou z možností je např. použít množinové operace.
Ant Colony Optimization (ACO)

Ant Colony Optimization (optimalizace kolonií mravenců), je algoritmus založený na chování mravenců. Ti jsou schopni hledat krátké cesty mezi mraveništěm a potravou na základě pokládání feromonu do prostředí. Při vyhledávání potravy mravenci cestou od mraveniště kladou malé množství feromonu. Po nalezení potravy se vrací do mraveniště a cestou kladou mnohem větší množství feromonu. Pokud mravenci při svém pohybu (hledání potravy) narazí na feromonovou stopu, mají tendenci ji sledovat - šance, že po ní půjdou je vyšší, pokud je stopa silnější.

Algoritmus ACO je založen právě na této metafoře. Typicky se používá pro řešení problémů, které lze reprezentovat jako hledání cest v grafu, např. problém obchodního cestujícího, nebo směrování v počítačových sítích. Algoritmus běží iterativně a opakuje dvě části - vygenerování řešení a update feromonu.

Vygenerování řešení každým mravencem probíhá tak, že mravenec začne v některém (náhodném) vrcholu grafu a rozhoduje se, do jakého vrcholu půjde dál. Pravděpodobnost přechodu z vrcholu x do vrcholu y závisí na množství feromonu τxy mezi těmito dvěma vrcholy a na atraktivitě (v zásadě heuristické hodnotě) νxy přechodu mezi těmito vrcholy (v obou případech je vyšší hodnota lepší). Pravděpodobnost přechodu je potom úměrná hodnotě (ταxy)(νβxy), kde α a β jsou konstanty,které určují poměr mezi vlivem obou proměnných.

Update feromonu má dva kroky - v prvním kroku se část feromonu vypaří, ve druhém kroku je na hrany, po kterých se pohyboval některý z mravenců, položen feromon v množství, které odpovídá kvalitě řešení nalezených mravenci. Konkrétně, po těchto dvou krocích se množství feromonu upraví podle vztahu τxy←(1−ρ)τxy+∑kτkxy, kde ρ je konstanta, která určuje rychlost vypařování feromonu, Q je vhodně zvolená konstanta, Lk je kvalita řešení nalezeného mravencem k a τkxy=Q/Lk pokud mravenec k prošel přes hranu (x,y) a 0 jinak.

Při použití ACO pro řešení TSP je Lk typicky délka cesty a νxy převrácená hodnota délky hrany (x,y).

Při aplikaci na jiné problémy je typicky rozdíl hlavně v generování cesty mravencem. Například tzv. Vehicle Routing Problem (VRP) je problém, kde je cílem naplánovat trasu pro rozvoz zboží ze skladu k zákazníkům. Cílem je minimalizovat počet vozidel potřebných pro rozvoz a najetou vzdálenost. Vozidla jsou omezena kapacitou (a např. i dobou strávenou na cestě). Při generování cesty tedy mravenci (vozidla) vybírají podle výše zmíněného vztahu dalšího zákazníka k navštívení dokud to je možné (zboží se vejde do auta a cesta není moc dlouhá). Pokud to možné není, vrací se do skladu. Zbytek algoritmu je potom stejný jako u TSP.
Artificial Bee Colony

Umělé včelí kolonie (ABC) jsou optimalizační algoritmus založený na chování včel při hledání potravy. Včely jsou rozděleny do třech skupin - na dělnice, vyčkávající včely a průzkumníky. Každá dělnice opracovává jeden zdroj jídla (pozice těchto zdrojů kódují řešení). Při opracování dělnice navštíví zdroje jídla v okolí, a pokud je kvalitnější (má lepší fitness) nahradí svůj zdroj tímto novým zdrojem. Potom se všechny dělnice sejdou v úle, vymění si informace o kvalitě zdrojů a vyčkávající včely si vyberou některé z těchto zdrojů pomocí ruletové selekce. Dělnice si zároveň pamatují, jak dlouho už opracovávají daný zdroj, a pokud přesáhne tato doba nastavený limit, zdroj opustí a stane se z ní průzkumník. Průzkumníci prohledávají prostor náhodně a hledají nové zdroje potravy.
Artificial Immune Systems

Umělé imunitní systémy (AIS) modelují různé procesy, které probíhají při práci imunitního systému u savců. Použité techniky se zde různí, nicméně typická aplikace AIS je ve strojovém učení, konkrétně pro klasifikaci, nebo detekci anomálií.

Například negativní selekce je inspirovaná pozitivní a negativní selekcí T-lymfocytů, která probíhá v brzlíku při jejich dozrávání. Při negativní selekci se lymfocyty, které reagují na vlastní buňky odstraňují. Algoritmy založené na negativní selekci se typicky používají pro detekci anomálií, nebo jednotřídní (one-class) klasifikaci. V obou případech jde o to poznat, jestli dané vzory jsou normální (patří do trénovacích dat), nebo ne. Algoritmus generuje množství různých pravidel a odstraňuje ta, která reagují na data z trénovací množiny.

Klonální selekce (clonal selection) se na druhou stranu snaží vytvořit pravidla, která dobře rozpoznávají nějaké vzory. Napřed se vygeneruje množina možných pravidel, z těch se potom ta, které lépe odpovídají požadovaným vzorům (mají vyšší afinitu), naklonují a v závislosti na jejich afinitě se na ně aplikuje tzv. hyper-mutace. Celý algoritmus klonální selekce vlastně připomíná evoluční algoritmus bez křížení.
Kritika přírodou inspirovaných heuristik

V současnosti se objevuje celá řada nových přírodou inspirovaných heuristik. Toto je velmi často kritizováno, neboť navržené algoritmy často používají komplikované metafory k tomu, aby zakryly to, že nejsou až tak nové. Při studiu těchto algoritmů je tedy vždy dobré se zamyslet, co je v nich opravdu nové a jestli náhodou metafora nemá za úkol jen zkomplikovat popis algoritmu, aby vypadal nově a zajímavě.
Mgr. Martin Pilát, Ph.D.
Malostranské náměstí 25
118 00 Praha
Martin.Pilat@mff.cuni.cz


Martin Pilát

    Výuka
    Výzkum

    English version

Neuronové sítě - úvod

V minulých přednáškách jsme se věnovali evolučním algoritmům jako přírodou inspirované optimalizační technice. Teď necháme evoluční algoritmy na chvíli stranou a podíváme se na techniku inspirovanou fungováním nervové soustavy - na neuronové sítě.

Neuronové sítě zažívají v současnosti bouřlivý rozmach v oblasti hlubokého učení a dosahují velmi dobrých výsledků v mnoha problémech strojového učení. Velmi populární jsou především tzv. konvoluční sítě, které se používají ke zpracování obrazu. Než se dostaneme k popisu těchto složitějších modelů, podíváme se na úplné základy. Dnes si popíšeme perceptron a vícevrstvý perceptron.
Strojové učení a příprava dat

Neuronové sítě se používají velmi často pro klasifikaci nebo regresi ve strojovém učení. Než se tedy dostaneme k tomu, co neuronové sítě jsou, podívejme se stručně na to, v jaké formě můžeme mít data a jak s nimi pracovat jako se vstupy nebo výstupy modelu strojového učení.

Datové množiny typicky obsahují příznaky ve formě vektorů (budeme je značit x=(x1,…,xn)) a požadované výstupy jako (typicky) jednu hodnotu (y). Různé datové množiny se ale liší typem dat pro jednotlivé příznaky xi a cílovou hodnotu y. Příznaky i výstupy obecně mohou být třech typů - číselné, ordinální a kategorické.

Číselné příznaky mohou být použity přímo jako vstupy většiny modelů. Nicméně, pokud mají různé příznaky rozdílné rozsahy, bývá lepší data nějakým způsobem přeškálovat. Mezi typické přístupy patří škálování každého příznaku do intervalu [0,1], nebo tzv. normalizace, tj. odečtení průměru a vydělení směrodatnou odchylkou. V prvním případě je potřeba nespoléhat na to, že hodnoty budou vždy mezi 0 a 1 - můžeme například později dostat hodnotu větší, než bylo maximum v trénovací množině, potom bude hodnota po naškálování větší než 1.

Kategorické příznaky (např. textové popisy) jsou příznaky, kterou mohou mít hodnotu z nějaké konečné množiny. Zároveň mezi hodnotami není žádné uspořádání. Takové příznaky je potřeba před jejich použitím převést na číselné. Pokud může mít daný kategorický příznak n hodnot, tak se typicky kóduje pomocí vektoru n hodnot z množiny 0,1, přičemž na 1 je nastavena jen ta pozice ve vektoru, která odpovídá dané hodnotě příznaku (např. pokud má příznak i-tou hodnotu z množiny, je pouze i-tá souřadnice vektoru nastavena na 1).

Ordinální příznaky jsou někde mezi číselnými a kategorickými a dají se kódovat pomocí libovolné z metod.

Typ cílových hodnot určuje typ problému, který budeme řešit - kategorické cílové hodnoty vedou na klasifikaci (určení do jaké ze tříd objekt patří), číselné hodnoty na regresi (předpověď hodnoty). Jejich kódování při trénování je stejné jako u příznaků, jen je potřeba myslet na to, že je třeba kódování zase invertovat při odpovědi tak, aby výsledek dával smysl.
Perceptron

Základní jednotkou v neuronové síti je jeden neuron. Perceptron je potom algoritmem (neuronovou sítí) s jediným takovým neuronem - perceptronem. Tento umělý neuron je vzdáleně inspirován přírodními neurony. Má několik vstupů xi a jeden výstup. Každý ze vstupů má přiřazenu váhu wi. Perceptron nejdříve spočítá svojí aktivaci jako vážený součet vstupů ξ=b+∑ni=1wixi. b je tzv. práh (bias) a ovlivňuje nakolik musí být vážený součet větší než 0, aby se peceptron aktivoval. Pokud je tato aktivace větší než práh 0, je výstup perceptronu 1, jinak je 0.

Explicitní práce s prahem b není potřeba a velmi často se upravují vstupy tak, že se k nim přidá jedna souřadnice s konstantní hodnotou 1. Prahy jsou potom přímo součástí vah. Výpočet perceptronu se pak dá zapsat jako f(∑ni=0wifi), kde f je funkce, která pro x<0 vrací 0 a jinak 1.

Kromě varianty, která vrací binární hodnoty 0 a 1 se často používá i varianta, která vrací tzv. bipolární hodnoty −1 a 1. Rozdíl je jen ve funkci f.

Trénování perceptronu je velmi jednoduché - postupně se předkládají vstupy (x,y) z trénovací množiny a aktualizují se váhy podle rovnice wi=wi+r(y−f(x))xi, kde r je parametr učení, který určuje, jak rychle se mění váhový vektor. Všimněte si, že výraz v závorce je 0, pokud perceptron odpověděl správně a 1, nebo -1, pokud odpověděl nesprávně.

Dá se ukázat, že takto popsaný algoritmus konverguje pokud jsou třídy v datech tzv. lineárně separabilní, tj. lze je oddělit nadrovinou ve vstupním prostoru.

V některých případech se třídy pro perceptron kódují jako −1 a 1. Potom se na trénování perceptronu dá dívat i jako na gradientní optimalizaci chybové funkce −∑yi(xTiwi).
Vícevrstvé perceptrony (dopředné neuronové sítě)

Spojením několika perceptronů vznikne nejznámější typ neuronové sítě, tzv. vícevrstvý perceptron, nebo dopředná neuronová sít (feedforward network). Ta se skládá z vrstev perceptronů popsaných výše, přičemž vstupy první (vstupní) vrstvy jsou přímo data z trénovací (testovací) množiny a vstupy dalších (skrytých a výstupní) vrstev jsou výstupy z vrstvy předcházející.

Ve vícevrstvých sítích se zpravidla používají jiné aktivační funkce f než ty zmiňované výše. Hlavní důvod je, že neuronové sítě se typicky trénují pomocí gradientních algoritmů a funkce zmíněné výše mají skoro všude gradient 0. Místo toho se používá tradičně tzv. logistická sigmoida - f(x)=11+e−λx. V současnosti se také velmi často používá funkce ReLU (rectified linear unit) definovaná jako f(x)=max(0,x).

Pro trénování se používá gradientní metoda. Chybová funkce L(x,y|w) neuronové sítě (typicky MSE) se zderivuje podle vah v síti a váhy se potom upraví podle vztahu wi=wi−α∂L(x,y|w)∂wi, kde α je parametr učení.

V současnosti se pro výpočet gradientu nejčastěji používají knihovny, které ho umí spočítat symbolicky. Prakticky tedy je potřeba napsat jen dopředný výpočet sítě a implementovat chybovou funkci. O výpočet gradientu se postarají existující nástroje. Nicméně, pro lepší pochopení neuronových sítí se vyplatí si gradient alespoň v tomto jednoduchém případě zkusit spočítat.

Začneme s výpočtem pro výstupní vrstvu. Označme jako wjk váhu mezi j-tým neuronem v poslední skryté vrstvě a k-tým neuronem ve výstupní vrstvě. Výstup tohoto neuronu je yk=f(ξk), kde xj je výstup j-tého neuronu v poslední skryté vrstvě a ξk=∑wjkxj. Uvažujeme-li chybovou funkci E(x,t|w)=12∑k(yk−tk)2 (t označuje vektor požadovaných výstupů, y označuje výstup sítě), je její derivace podle váhy wLjk dána pomocí výpočtu níže (aplikovali jsme pravidlo pro derivaci složené funkce).

∂E∂wLjk=∂E∂yk∂yk∂ξk∂ξk∂wLjk=(yk−tk)xj∂f(ξj)∂ξj.

Pro výpočet derivace chybové funkce podle vah ve skrytých vrstvách neuronové sítě je užitečné představit si, co přesně počítají poslední dvě vrstvy této sítě. Budeme označovat indexem k neurony ve výstupní vrstvě, indexem j neurony v poslední skryté vrstvě a indexem i neurony ve skryté vrstvě před poslední skrytou vrstvou. Vstupy těchto neuronů budou označeny jako xk, xj, a xi, jejich aktivace budou zase značeny jako ξ s příslušným indexem a aktivační funkce jako f s tímto indexem. Váhy mezi poslední skrytou a výstupní vrstvou označíme jako wL a váhy mezi posledními dvěma skrytými vrstvami jako wL−1. Poslední dvě vrstvy tedy počítají výraz yk=fk(∑jwLjkfj(∑iwL−1ijxi)). Pokud zase budeme uvažovat stejnou chybovou funkci, dostaneme její derivaci opět podle pravidla pro derivaci složené funkce jako

∂E∂wL−1ij=[∑k∂E∂ξk∂ξk∂yj]∂yj∂ξj∂ξj∂wL−1ij=[∑kδkwLjk]yi∂fj(ξj)∂ξj.

Můžeme si všimnout, že první část sumy (∂E∂ξk) jsme spočítali již při výpočtu pro výstupní vrstvu. Označíme ji tedy δk a tím dostaneme zjednodušenou verzi výrazu za posledním =. Nyní si stačí uvědomit, že jsme nikde nepoužili informaci o tom, že k značí výstupní vrstvu a můžeme tedy použít stejný výraz pro všechny skryté vrstvy. Pokud ještě i zde definujeme δj=∂Ev∂ξj=∂fj(ξj)∂ξj∑δkwjk, dostaneme známé adaptační pravidlo pro trénování vah neuronové sítě (definice δj se liší podle toho, jestli jde o skrytou nebo výstupní vrstvu): wk+1ij=wkij−αδjyi.

Zatím jsme se nebavili o tom, jaká je derivace aktivační funkce podle jejího vstupu. Dá se ukázat, že například pro sigmoidu to je λyj(1−yj). Také jsme zatím počítali derivaci jen pro jeden vstupní vzor - pro více vzorů ale dostaneme jen součet těchto derivací.
Mgr. Martin Pilát, Ph.D.
Malostranské náměstí 25
118 00 Praha
Martin.Pilat@mff.cuni.cz


Martin Pilát

    Výuka
    Výzkum

    English version

Neuronové sítě - RBF sítě a rekurentní sítě

V dnešní přednášce se podíváme na dva různé typy neuronových sítí. Napřed si představíme architekturu, která používá lokální jednotky ve vstupní vrstvě a potom se podíváme na rekurentní neuronové sítě, tedy takové, kde váhy mezi neurony mohou tvořit cykly.
RBF sítě

Neuronové funkce s lokálními jednotkami založenými na Radial Basis Functions (RBF sítě) představují zajímavou alternativu k perceptronovým neuronovým sítím. Hlavní rozdíl mezi nimi je v tom, že neurony ve vstupní vrstvě místo skalárního součinu počítají nějakou funkci závislou na vzdálenosti od svého “váhového” vektoru (slovo “váhového” je v uvozovkách, protože se váhy nejedná - typicky se tomuto vektoru říká “střed”). Výpočet těchto neuronů tedy můžeme vyjádřit jako y=ρ(||x−c||), kde ρ je nějaká aktivační funkce (kernel), ci je střed neuronu, xi je vstup a ||⋅|| je nějaká norma - často Euklidovská vzdálenost, ale může být i jiná. Jako kernel se často používá např. Gaussova funkce ρ(x)=e−βx2.

Typická RBF síť má po RBF vrstvě už jen jednu vrstvu neuronů (perceptronového typu). Celá síť tedy počítá funkci φ(x)=N∑i=1wiρ(x,c), kde wi jsou váhy pro výstupní vrstvu (v případě více výstupních neuronů máme zase matici vah).

Všimněte si, že aktivační funkce v RBF síti je lokální, tj. má největší hodnotu pro vstupy, které jsou blízko středu neuronu a pro vstupy dále od středu jejich aktivace klesá až k 0.

Trénování RBF sítí typicky probíhá ve dvou fázích, napřed se pomocí nějakého shlukovacího algoritmu (např. k-means, viz níže) nastaví středy neuronů ve vstupní vrstvě, potom se spočítá parametr β v každém neuronu jako β=12σ2, kde σ je průměrná vzdálenost objektů v příslušném shluku od jeho středu. Nakonec se natrénují váhy výstupní vrstvy. Zde stačí postupně předložit vstupy z trénovací množiny, spočítat aktivace vstupní vrstvy a následně použít algoritmy pro lineární regresi. Výstupní vrstva totiž počítá pouze lineární kombinaci aktivací vstupní vrstvy.

Alternativou k popsanému postupu trénování může být použití gradientní metody pro nastavení středů neuronů i vah ve výstupní vrstvě.
Algoritmus k-means

Zmínili jsme, že pro hledání středů neuronů ve vstupní vrstvě se používají shlukovací algoritmy, nejčastěji tzv. algoritmus k-means. Je to algoritmus, který se snaží ve vstupních datech najít shluky - skupiny dat, které jsou blízko k sobě, ale zároveň daleko od ostatních skupin. Jde o algoritmus učení bez učitele, nepoužívá tedy žádné cílové hodnoty y. Algoritmus dostane na vstupu vektory dat xi a číslo k, které označuje požadovaný počet shluků. Algoritmus začne tak, že náhodně zvolí k středů shluků mj (často jako k vzorků ze vstupních dat). Potom opakuje fáze přiřazování a přepočítávání středů. Ve fázi přiřazování je každý vzorek ze vstupních dat přiřazen do toho shluku, jehož střed je k němu nejblíž. Ve fázi přepočítání středů se každý střed přepočítá jako střed shluku dat, které k němu patří. Tyto dvě fáze se opakují, dokud algoritmus nezkonverguje, nebo po zadaný počet iterací.
Rekurentní neuronové sítě

V neuronových sítí, které jsme zatím zmiňovali, vedou váhy vždy jen jedním směrem a celá neuronová síť tedy tvoří acyklický graf. Takové neuronové sítě se chovají zcela reaktivně a jejich přechozí vstupy nijak neovlivňují vstupy následující. To se hodí pro mnoho běžných problémů, jako jsou např. klasifikace obrázků apod., ale pokud mají být vstupem neuronové sítě posloupnosti různých délek, kde se jednotlivé položky ovlivňují, je vhodnější neuronové síti přidat nějaký vnitřní stav, reprezentovaný typicky pomocí spoje, který vede zpět. Sítě s takovými spoji se nazývají rekurentní a používají se např. pro předpovídání časových řad, strojový překlad, nebo generování textu.

Nejjednodušší rekurentní sítí může být síť pouze s jedním vstupem, jedním výstupem a jedním neuronem v jediné skryté vrstvě. Tento neuron potom bude mít rekurentní spojení sám do sebe. Význam tohoto spoje je takový, že při předložení vzoru neuron dostane kromě svého běžného vstupu ještě svojí aktivaci v předchozím kroku (při předložení předcházejícího vstupu). Neuron tedy vlastně počítá svou aktuální aktivaci jako vážený součet svého vstupu a svého předchozího výstupu. V obecnějších rekurentních sítích je význam podobný - rekurentní váhy předávají stav z předcházejícího časového kroku.

Výpočet rekurentní sítě tedy probíhá tak, že ji postupně předkládáme vzory a ona na jejich základě (a na základě svých aktivací v předchozích krocích) počítá výstupy. S výstupy zacházíme podle toho, co chceme se sítí dělat. Pokud má např. předpovídat hodnotu časové řady, předložíme napřed všechny vstupy a až potom se podíváme na výstup. Při překladu předložíme napřed větu v jednom jazyce a potom teprve počkáme, až síť vygeneruje větu v jazyce cílovém. Při generování textu necháme síť generovat samostatně a dáváme jí na vstup její předchozí výstupy. Každopádně na posloupnost vstupů dostaneme posloupnost výstupů, kterou můžeme při trénování porovnat s nějakou požadovanou posloupností.
Trénování rekurentních neuronových sítí

Trénování probíhá pomocí algoritmu back-propagation, který jsme si ukazovali minule, jen je potřeba síť rozvinout v čase, tj. zkopírovat ji pro každý krok vstupu (a výstupu). Takto upravené verzi algoritmu se říká backpropagation through time (algoritmus zpětného šíření v čase).

S trénováním rekurentních vah ale mohou být problémy. Když si uvědomíte, jak algoritmus zpětného šíření funguje, uvidíte, že se v něm gradient z předchozí vrstvy vždy násobí vahou. Pokud je toto rekurentní váha, tak se opakovaně násobí tou samou hodnotou. V případě, že je tato hodnota větší než 1, tak gradienty nekontrolovaně rostou (explodující gradienty), pokud je menší než 1, tak naopak klesají k 0 (mizející gradienty). Obě situace vedou k tomu, že algoritmus nefunguje moc dobře.

Tento problém se dá řešit dvěma způsoby - buď se rekurentní část sítě neučí vůbec, jako v tzv. Echo state networks, nebo se rekurentní váha zafixuje na 1 a práce se stavem sítě se provádí explicitně jako v tzv. Long-short term memory sítích.
Echo state sítě

Echo state sítě (ESN) fungují tak, že hned na vstupu mají velkou rekurentní vrstvu, která má váhy inicializované náhodně, a tyto se dál nijak netrénují. Typicky je tato vrstva implementovaná jako jediná matice k×m, kde k=n+m, m je velikost rekurentní vrstvy a n je počet vstupů. Síť funguje tak, že na vstup dostává vektory délky n a připojí k nim svůj vnitřní stav délky m. Na ten aplikuje svou rekurentní vrstvu a tím dostane nový vnitřní stav. Rekurentní vrstva typicky obsahuje nějakou aktivační funkci, aby byla nelineární (ta se aplikuje po složkách na všechny aktivace - výsledky násobení náhodnou maticí). Tradiční ESN po rekurentní vrstvě obsahují už jen jednu vrstvu, kterou podobně jako u RBF sítí můžeme trénovat pomocí lineární regrese, nebo pomocí gradientní metody.

ESN může na první pohled vypadat zvláštně, proč by měla náhodná matice dávat rozumné výsledky? Důležitým pozorováním je, že díky velikosti vnitřního stavu (který je často větší než počet vstupů), matice vlastně náhodně transformuje informaci ze vstupu do prostoru s větší dimenzí. Další vrstvy se potom vlastně snaží tuto informaci rozkódovat a dostat z ní potřebné informace. Uvědomte si také, že vnitřní stav sítě závisí na všech předcházejících vstupech, nejen na tom posledním, a obsahuje tedy informace o všech z nich.
Long short term memory

Long short term memory (LSTM) sítě řeší problém s trénováním trochu jinak. Nahrazují každý neuron tzv. LSTM buňkou, která explicitně pracuje se svým stavem (pamětí) a rekurentní spoje mezi jednotlivými buňkami potom mají váhu zafixovanou na 1.

Vstupem každé buňky je její stav ct−1 z předcházejícího kroku a spojení jejích výstupů v předcházejícím stavu a nových vstupů [ht−1,xt]. Na základě vstupů se napřed spočítají hodnoty tzv. bran (gates) - zapomínací ft (forget) a vstupní it (input). Obě se počítají podobně a to jako

ft=σ(Wf[ht−1,xt]+bf)

it=σ(Wi[ht−1,xt]+bi),

kde Wf,Wi,bf a bi jsou váhy a prahy pro zapomínací a vstupní bránu a σ je sigmoida. Z těch samých hodnot zároveň spočítáme i kandidáta na nový vnitřní stav jako

¯Ct=tanh(Wc[ht−1,xt]+bc),

kde opět Wc jsou váhy a bc jsou prahy pro výpočet stavu. Nový stav buňky se potom spočítá jako

Ct=ft∗Ct−1+it∗¯Ct,

kde operace ∗ značí násobení po složkách.

Nakonec ještě spočítáme výstup buňky ht. Ten se spočítá z aktuálního stavu buňky a jejího vstupu pomocí výstupní (output) brány ot, jako

ot=σ(Wo[ht−1,xt]+bo)

ht=ot∗tanh(Ct)

kde opět Wo a bo jsou váhy a prahy pro výstupní bránu.

Přenos informace mezi jednotlivými časovými kroky u LSTM sítí probíhá pomocí stavu. S tím není přímo spojena žádná váha a tak se při propagaci chyby v síti můžeme vyhnout problémům s explodujícími a mizejícími gradienty. LSTM sítě si díky této vlastnosti umí zapamatovat delší posloupnosti vstupů než základní typu rekurentních sítí.
Další zdroje

Zdroje v této části nejsou samy o sobě důležité ke zkoušce, ale obsahují další informace, které jsem ukazoval na přednášce (a občas mohou pomoci lépe pochopit text výše).

    A Practical Guide to Applying Echo State Networks - pěkný popis ESN a také toho, jak je prakticky použít pro řešení problémů
    The Unreasonable Effectiveness of Recurrent Neural Networks - stručný popis LSTM sítí a rekurentních sítí obecně s příklady, jak se dají použít ke generování textu po znacích

Mgr. Martin Pilát, Ph.D.
Malostranské náměstí 25
118 00 Praha
Martin.Pilat@mff.cuni.cz



Martin Pilát

    Výuka
    Výzkum

    English version

Neuronové sítě - konvoluční sítě a zpracování obrazu

Velmi častým typem vstupů, kterým se musí neuronové sítě zabývat, jsou obrázky. V této oblasti dosáhly v poslední době neuronové sítě velkých pokroků. Dnes se podíváme, jakým způsobem s neuronovými sítěmi pro zpracování obrazu pracovat, jaké jsou dostupné architektury, a podíváme se i na některé zajímavé výsledky a postupy, jakými jich bylo dosaženo.
Konvoluční sítě

Hlavní problém se zpracováním obrázků pomocí neuronových sítí je jejich velikost – typický obrázek má více než 100×100

pixelů, každý pixel má u barevných obrázků 3 barevné kanály. I takto malé obrázky tedy znamenají, že máme na vstupu 30 000 hodnot. To je pro plně propojené sítě hodně - měly by velmi velké množství parametrů.

Z tohoto důvodu se ve zpracování obrazu často používají tzv. konvoluční sítě. Ty jsou navržené tak, že čtou malé (např. 3×3

) části obrázku a aplikují na ně pořád stejnou operaci (ta je stejně jako u perceptronových sítí jen skalární součin s vahami sítě). Důležité je, že tuto operaci aplikují na všechny možné pozice v obrázku (délka kroku při posunu “okénka” se označuje jako stride, typicky se okénka překrývají) a váhy jsou na všech pozicích sdílené. Pokud tedy máme jednu takovou konvoluční operaci popsanou výše, má neuronová síť jen 9 parametrů (27 pro barevné obrázky). Výstupem takové konvoluční vrstvy je potom “obrázek”, který je stejně velký, jako vstupní obrázek (tady trochu záleží na tom, jak ošetříme okraje obrázku). Takovou konvoluční vrstvu typicky nemáme jen jednu, ale hned několik, které se aplikují na stejný obrázek - to nám umožňuje zpracovat obrázek pomocí mnoha konvolucí najednou. Dostáváme vlastně potom obrázek s podobnými rozměry jako měl vstupní obrázek, ale s větším počtem kanálů. Na ten se potom zase dají aplikovat konvoluční vrstvy stejným způsobem.

Pokud bychom používali jen konvoluční vrstvy, měli bychom pořád stejně velké obrázky a nemohli bychom s nimi pořád nic moc dělat. Proto se v konvolučních sítích střídají konvoluční vrstvy a sub-sampling (pooling) vrstvy. Nejčastější takovou vrstvou je max-pooling, ta se aplikuje podobně jako konvoluční vrstva na všechny části obrázku (např. s rozměry 2×2

) a vrací z nich maximum. U sub-sampling vrstev se naopak překrývání typicky nepoužívá. Tím se sníží rozlišení na polovinu. Při takovém střídání konvolučních a sub-sampling vrstev nakonec dostaneme relativně malou reprezentaci vstupního obrázku, na kterou už můžeme aplikovat plně propojené vrstvy.

Co vlastně konvoluce dělají? Pokud si zobrazíme aktivace neuronů v jednotlivých vrstvách konvoluční sítě jako obrázky, uvidíme, že na prvních vrstvách po vstupu se chovají jako detektory hran, v hlubších vrstvách potom jednotlivé neurony mohou detekovat přítomnost složitějších objektů.
Matoucí vzory

Ačkoliv konvoluční neuronové sítě dosahují velmi dobrých výsledků ve zpracování obrazu, objevuje se u nich jedna zajímavá vlastnost (zranitelnost) – jsou náchylné na tzv. matoucí vzory, tj. obrázky, které jsou drobně upravené tak, že člověk typicky není schopný rozpoznat rozdíl, ale neuronová síť na ně vrací jiné odpovědi než na původní obrázky.

Původní zdůvodnění pro existenci takových vzorů bylo, že neuronové sítě jsou velmi nelineární a tedy drobné změny mohou vést k tomu, že se jejich výstupy výrazně změní. Ukazuje se ale, že na matoucí vzory jsou náchylné i jiné modely strojového učení, včetně lineárních modelů. Důvod pro matoucí vzory tedy může být přesně opačný, tj. že neuronové sítě jsou hodně lineární a malé změny, které se dostatečně nasčítají potom vedou ke špatné klasifikaci.

Na aproximaci neuronových sítí pomocí lineárních modelů je založena velmi populární technika pro generování matoucích vzorů - FGSM (Fast Gradient Sign Method). Ta spočítá derivaci chybové funkce podle vstupu do neuronové sítě a přičte k tomuto vstupu ε⋅sign(∇J)
, kde ∇J je právě tento gradient. Ukazuje se, že i malé změny pro ε<0.1

mohou snadno zmást mnoho modelů neuronových sítí, které jinak dávají velmi dobré výsledky.

Existence matoucích vzorů může být problém pro aplikaci neuronových sítí v oblastech, kde chyby mohou mít závažné důsledky, jako např. pro řízení autonomních vozidel. Ukazuje se dokonce, že matoucí vzory lze vytvořit i v reálném světě, kde např. speciální brýle jsou schopné zmást modely pro rozpoznávání obličejů, nebo speciální nálepky mohou způsobit, že vozidlo není schopné detekovat čáru oddělující jízdní pruhy, případně detekuje čáru tam, kde není.
Přenos uměleckého stylu

Jednou z pěkných aplikací neuronových sítí je přenos uměleckého stylu mezi obrázky. Představte si např., že máte fotografii a chtěli byste z ní udělat obraz ve stylu Picassa. Pro přenos stylu se dají použít aktivace ve vnitřních vrstvách neuronové sítě. Ukazuje se potom, že samotné aktivace odpovídají obsahu obrázku a korelace mezi těmito aktivacemi odpovídají stylu. Přenos stylu se pak definuje jako optimalizační problém, kde cílem je dosáhnout (změnou vstupního obrázku) aktivací, které jsou podobné původní fotografii a zároveň mají korelace podobné obrázku v požadovaném stylu. Podle toho, jak hluboké vrstvy se zvolí dostáváme jiné části stylu - od tahů štětcem až po barvy a deformace obrazu.
Generative Adversarial Networks

Dnes se pro přenos stylu mezi obrázky a pro generování obrázků často používají tzv. Generative Adversarial Networks. Ty se vlastně skládají ze dvou částí - generátoru a diskriminátoru. Generátor ma za úkol generovat obrázky, které jsou podobné obrázkům v nějaké trénovací množině a diskriminátor ma za úkol poznat, jestli předložené obrázky jsou generované generátorem, nebo jestli pochází z trénovací množiny. Generátor se potom snaží maximalizovat chybu diskriminátoru a diskriminátor se snaží svoji chybu minimalizovat. Tímto způsobem se obě sítě navzájem trénují. Po skončení trénování typicky diskriminátor nepoužíváme.
Další zdroje

Zdroje v této části nejsou samy o sobě důležité ke zkoušce, ale obsahují další informace, které jsem ukazoval na přednášce (a občas mohou pomoci lépe pochopit text výše).

    Breaking neural networks with adversarial attacks - ukázky několika typů nepřátelských vzorů s odkazy na další články
    Generating adversarial patches against YOLOv2 - ukázka nepřátelských útoků proti modelu pro detekci objektů
    A Neural Algorithm of Artistic Style - přenos uměleckého stylu (více detailů a ukázky k textu výše)
    Inceptionism: Going Deeper into Neural Networks

Mgr. Martin Pilát, Ph.D.
Malostranské náměstí 25
118 00 Praha
Martin.Pilat@mff.cuni.cz


Martin Pilát

    Výuka
    Výzkum

    English version

Neuroevoluce

Bavili jsme se už o evolučních algoritmech i neuronových sítích. Dnešní téma je neuroevoluce, tj. evoluce neuronových sítí. Toto téma se aktuálně opět stává velmi aktuálním kvůli rozvoji metod založených na hlubokém učení. Algoritmy pro neuroevoluci se v poslední době rozšiřují do algoritmů pro hledání architektur neuronových sítí.

Oblast neuroevoluce můžeme rozdělit do třech podoblastí podle toho, co algoritmy přesně hledají - na evoluci vah sítí, evoluci topologie a na evoluci obojího najednou.
Evoluce vah sítě

Evoluce vah neuronové sítě je z hlediska kódování jedince nejjednodušší. Předpokládáme zde, že architektura neuronové sítě je fixní, tj. je fixní i počet jejích vah, celá evoluce se redukuje na problém spojité optimalizace. Nejčastěji se v této oblasti používají jednoduché evoluční strategie - ke každému genu jedince se přičte náhodné číslo z normálního rozdělení s nulovou střední hodnotou a malých rozptylem (který je stejný pro všechny váhy). Složitější evoluční strategie se typicky moc nepoužívají, protože jejich režie na adaptaci vah může být dost velká.

Proč používat evoluci místo gradientních metod? Gradientní metody jsou často rychlejší v případě učení s učitelem, např. pro trénování sítí pro klasifikaci. Pro zpětnovazební učení ale má evoluce několik podstatných výhod. Jednou z nich jsou výrazně lepší možnosti paralelizace a více CPU jader - ve zpětnovazebním učení je totiž hlavní problém vyhodnocení prostředí, které může trvat relativně dlouho ve srovnání s dobou potřebnou na vypočítání gradientu a propagaci vah. Navíc toto vyhodnocení často nelze dělat na GPU. Evoluční strategie lze velmi dobře paralelizovat a nejsou výjimkou ani algoritmy, kde evoluční strategie běží na stovkách CPU.

Druhou oblastí, kde evoluční strategie mají navrch jsou prostředí s řídkými odměnami - představte si hru, kde dostanete skóre až na konci a ne v každém kroku v průběhu. V takové hře běžné algoritmy pro hluboké zpětnovazební učení naráží na to, že se jejich odhady odměn propagují velmi pomalu (pro všechny stavy kromě toho posledního je po prvním dohrání hry odhad 0). Evolučním strategiím tohle nevadí - tak jako tak používají fitness až na konci. Občas se dokonce evoluční strategie kombinují s algoritmy pro hluboké zpětnovazební učení tak, že hry odehrané v evoluci se používají pro trénování sítí právě v algoritmech hlubokého zpětnovazebního učení.
Evoluce vah i topologie

Typickým algoritmem, který vyvíjí váhy sítě i její topologii zároveň je NEAT (Neuro-evolution of Augmenting Topologies). Algoritmus NEAT je trochu podobný algoritmům kartézského genetického programování. Jeho jedinci jsou tvořeni seznamem, který obsahuje v každé položce informaci o jedné váze v neuronové síti - odkud vede, kam, a jaká je její hodnota. Kromě toho každá váha ještě má příznak, jestli je tento spoj v síti aktivní a také své “inovační číslo” - identifikátor, který má za cíl poznat, jaké váhy ve dvou různých jedincích mají stejnou historii a tedy by měly mít i podobnou funkci. To se používá v rámci genetických operátorů.

NEAT používá dva typy mutací - přidání neuronu a přidání hrany. V obou případech se při přidání hrany generuje pro každou novou hranu nové inovační číslo. Při přidání hrany se přidá nová hrana na konec jedince, při přidání neuronu se vybere hrana v jedinci, ta se rozdělí na dvě přidáním neuronu, nové hrany se přidají na konec jedince a původní hrana se nastaví jako neaktivní.

Křížení se v NEAT dělá pomocí inovačních čísel. Dva jedinci, kteří se mají křížit se “zarovnají” podle inovačních čísel. Hrany se stejným inovačním číslem, které jsou v obou jedincích se dědí náhodně z jednoho nebo z druhého. Hrany, které jsou jen v jednom jedinci se dědí z toho lepšího z těchto dvou. Pokud je nějaká hrana v jednom jedinci neaktivní a v druhém aktivní, ve výsledku je aktivní/neaktivní s danou pravděpodobností.

Kromě těchto operátorů NEAT používá ještě zajímavou techniku rozdělení populace na více druhů. Jedinci každého druhu potom explicitně sdílí fitness, tj. fitness každého jedince je vydělena počtem jedinců stejného druhu, a tím se dává nově objeveným myšlenkám (strukturám) čas pro to, aby se vylepšily pomocí genetických operátorů. Druhy jsou definovány pomocí vzdálenosti mezi jedinci. Ta se počítá na základě počtu stejných a různých genů (podle inovačních čísel) a podle podobnosti genů, které jsou v obou jedincích.

Při inicializaci NEAT začíná z minimálních struktur, tj. neuronových sítí, které neobsahují žádné skryté neurony - všechny spoje vedou jen mezi vstupy a výstupy.
HyperNEAT

Algoritmus hyperNEAT je rozšířením algoritmu NEAT. V algoritmu HyperNEAT se topologie sítě zafixuje na začátku (typicky jako hyper-krychle) a váhy se reprezentují pomocí jiné neuronové sítě. Tato neuronová síť dostává na vstupu souřadnice neuronů ve výsledné sítí a vrací pro ně přímo váhy. Síť pro výpočet vah se potom vytváří pomocí algoritmu NEAT.

Výhodou algoritmu HyperNEAT je, že vytváří mnohem pravidelnější sítě než NEAT, které mohou být blíže biologickým neuronovým sítím a navíc je schopen vyvíjet větší sítě.
Vytváření architektur neuronových sítí

V současnosti jsou velmi populární algoritmy pro hledání celé struktury neuronových sítí, která se později trénuje pomocí běžných gradientních technik. Z hlediska evolučních algoritmů je v takovém případě potřeba zakódovat strukturu sítě (na úrovni vrstev nebo bloků neuronů) do jedince. Pokud bychom chtěli vytvářet pouze vrstvy, situace je docela jednoduchá - jedinec může být např. posloupnost těchto vrstev včetně jejich parametrů. Operátory jsou potom úpravy parametrů těchto vrstev, přidání dalších vrstev, nebo i přidání spojení mezi vrstvami, které spolu nesousedí (skip connections).

Existují ale i algoritmy jako CoDeepNEAT, které kódují jedince podobně jako NEAT. Rozdíl ale je v tom, že jednotlivé uzly neobsahují jednotlivé neurony, ale přímo moduly neuronové sítě (bloky neuronů). Tyto moduly jsou také vytvářeny pomocí NEAT algoritmu. Při vyhodnocení fitness se celkový jedinec vytvoří pomocí kombinace těchto modulů, tak, jak je popsáno v jedinci.
Novelty Search

Algoritmus Novelty Search se netýká jen evoluce neuronových sítí, ale je obecnější. Nicméně velmi často se používá právě ve spojení s neuroevolucí. Principem novelty search je vynechání fitness funkce, která by přímo hodnotila kvalitu nalezených řešení. Tato fitness funkce je nahrazena funkcí, která porovnává chování vytvořených jedinců (např. při hledání cesty v bludišti se může počítat vzdálenost pozic, kam jedinec došel, od pozic, kam došli jedinci před ním). Může se zdát, že takový algoritmus nebude moc dobře fungovat, ale ukazuje se, že to není pravda. Zvláště v prostředích, kde klasická fitness funkce obsahuje složitá lokální optima se ukazuje, že novelty search dává dobré výsledky i z hlediska kvality nalezených řešení.
Další zdroje

    Původní článek o algoritmu NEAT
    Článek o CoDeepNEAT
    Video ukazující aplikaci NEATu na hru Mario

Mgr. Martin Pilát, Ph.D.
Malostranské náměstí 25
118 00 Praha
Martin.Pilat@mff.cuni.cz



Martin Pilát

    Výuka
    Výzkum

    English version

Hluboké zpětnovazební učení

Zatím jsme se na přednášce bavili o zpětnovazebním učení, evolučních algoritmech a neuronových sítí. Minule jsme spojili evoluci a neuronové sítě, dnes se podíváme na použití neuronových sítí ve zpětnovazebním učení - na hluboké zpětnovazební učení. Tímto tématem také uzavřeme všechny tři tyto kapitoly.

Připomeňme si napřed terminologii a značení (kopie textu z kapitoly o zpětnovazebním učení):

    Prostředí můžeme formálně popsat jako markovský rozhodovací proces (MDP), který je zadaný čtveřicí (S,A,P,R), kde S je konečná množina stavů prostředí, A je (konečná) množina akcí (případně může být nahrazena množinami As akcí aplikovatelných ve stavu s), Pa(s,s′) je přechodová funkce, která udává pravděpodobnost, že aplikací akce a ve stavu s přejde prostředí do stavu s′ a Ra(s,s′) je funkce odměn, která udává okamžitou odměnu, kterou agent dostane od prostředí, pokud ve stavu s provede akci a a převede tím prostředí do stavu s′. U přechodové funkce je důležité, že splňuje tzv. markovskou podmínku, tj. že závisí pouze na aktuálním stavu s a akci a a nikoliv na akcích a stavech předcházejících.

    Chování agenta potom můžeme popsat pomocí strategie (policy) π:S×A→[0,1], kde π(s,a) udává pravděpodobnost provedení akce a ve stavu s. Cílem zpětnovazebního učení je potom najít strategii π takovou, že maximalizuje celkovou odměnu, kterou agent získá ∑∞t=0γtRat(st,st+1), kde at=π(st) je akce provedená agentem v kroku t a γ<1 je diskontní faktor, který zajišťuje, že suma je konečná.

    Hodnota Vπ(s) stavu s při použití strategie π se dá definovat jako Vπ(s)=E[R]=E[∑∞t=0γtrt|s0=s], kde R značí celkovou získanou diskontovanou odměnu a rt značí odměnu obdrženou v čase t. Kromě hodnoty stavu se velmi často hodí uvažovat také hodnotu Qπ(s,a) akce a provedené ve stavu s pokud budeme dále sledovat strategii π. Výhodou tohoto modelu je, že agent nepotřebuje mít model prostředí, který popisuje, jakým způsobem akce ovlivňují prostředí a učí se tento model za běhu.

    Cílem agenta potom tedy je najít optimální strategii π⋆ takovou, že Vπ⋆(s)=maxπVπ(s). Hodnotu stavů (akcí) pro optimální strategii budeme značit jako V⋆(s) (Q⋆(s,a)).

Z těchto definici můžeme snadno odvodit tzv. Bellmanovy rovnice, které jsou nutnou podmínkou optimality pro strategii π. Qπ(s,a)=∑s′Pa(s,s′)[Ra(s,s′)+γ∑a′π(s′,a′)Qπ(s′,a′)] Vπ(s)=∑aπ(s,a)∑s′Pa(s,s′)[Ra(s,s′)+γVπ(s′)]
Hluboké Q-učení

Hluboké Q-učení je založeno na stejné myšlence jako Q-učení, tj. chceme pro každý stav s a každou akci a odhadnout jakou diskontovanou odměnu bychom dostali, pokud bychom akci a ve stavu s provedli. V tradičním Q-učení jsou tyto hodnoty reprezentovány jako matice Q. Tato reprezentace je ale problematická, pokud je hodně stavů, nebo hodně různých akcí. V hlubokém Q-učení se tedy pro reprezentaci této matice používá neuronová síť, která pro každý stav vrací ohodnocení všech akcí.

Trénování neuronové sítě se provádí podle Bellmanovy rovnice pro Q takovým způsobem, že se porovnává aktuální odměna od prostředí Ra(s,s′) s hodnotou spočítanou pomocí Bellmanových rovnic z Q a minimalizuje se střední čtvercová chyba jejich rozdílu. Naším cílem tedy je minimalizovat rozdíl mezi Q(s,a) a Ra(s,s′)+γmaxa′Qk(s′,a′). Všimněte si, že stejně jako v standardním Q-učení uvažujeme, že v dalším stavu vybereme nejlepší akci podle aktuálního odhadu Q. Chybová funkce tedy je

Es′∼Pa(s,s′)[(Ra(s,s′)+γmaxa′Qθ(s′,a′)−Qθ(s,a))2]|θ=θk

kde Qθ jsou parametry neuronové sítě reprezentující matici Q.

Pro výpočet chybové funkce tedy potřebujeme znát stav s, vybranou akci a, získanou odměnu Ra(s,s′) a následující stav s′. Všechny tyto údaje snadno získáme, pokud necháme agenta provádět akce v prostředí. Při trénování se ale často objevuje problém s tím, že měníme přímo funkci, která odhaduje Q a tím měníme i chování agenta a odhady zároveň, je ale vidět, že oba tyto aspekty spolu úzce souvisí - vlastně se snažíme učit funkci, kde se pořád mění vstupy i výstupy. Pro zachování větší stability trénování se používají dva triky - cílová síť (target network) a přehrávání zkušeností (experience replay).

Podstatou triku s cílovou sítí je, že oddělíme síť pro výběr akce a síť pro odhad hodnoty. Typicky jen tak, že se zafixují parametry sítě, podle které se vybírá akce, a měníme jen parametry sítě, která se učí ohodnocení. Po daném počtu iterací se parametry obou sítí nastaví na stejné hodnoty a pokračuje se s trénováním podle stejného postupu. Chybová funkce tedy v tomto případě vypadá jako Es′∼Pa(s,s′)[(Ra(s,s′)+γmaxa′Qθ−(s′,a′)−Qθ(s,a))2]|θ=θk, kde θ− jsou právě parametry sítě pro výběr akce, které se aktualizují méně často, než parametry θ, které odhadují hodnotu Q.

Podstatou experience replay je, že si pamatujeme čtveřice (s,a,r,s′) stavu, akce, odměny a následujícího stavu a při trénování náhodně vybíráme přechody z této paměti místo toho, abychom vždy používali poslední přechod. Tím se zbavíme závislostí mezi po sobě jdoucími vstupy.

Hluboké Q-učení se proslavilo jako technika, která je schopná naučit se hrát Atari hry na podobné úrovni jako lidští hráči s tím, že vstupem je pouze obrazová informace a odměny se počítají jako změny skóre hry.
DDPG

Hluboké Q-učení vyžaduje počítání maxima přes všechny akce - tato operace je ale složitá, pokud je prostor akcí spojitý (představte si třeba řízení auta, kde akce je úhel otočení volantu a sešlápnutí plynu/brzdy). Z tohoto důvodu algoritmus DDPG (Deep Deterministic Policy Gradient) nahrazuje tuto operaci novou sítí, která přímo vrací akci, která se má provést. Označme tuto funkci s parametry θ jako μθ. Jde o funkci z prostoru stavů do prostoru akcí. Označme zároveň funkci počítající hodnotu Q s parametry ϕ jako Qϕ. DDPG používá oba triky zmíněné výše, označme tedy pomocí θ− a ϕ− parametry cílových sítí pro θ a ϕ.

Aktualizace parametrů ϕ sítě pro Q se potom počítá pomocí upravené chybové funkce Es′∼Pa(s,s′)[(Ra(s,s′)+γQϕ−(s′,μθ−(s′))−Qϕ(s,a))2]|θ=θk. Myšlenka trénování sítě μ je velmi jednoduchá - chceme aby vracela akce, které maximalizují Qθ(s,a) ve stavu s. Maximalizujeme tedy pomocí gradientní metody výraz Es[Qϕ(s,μθ(s))].
Policy gradient metody

Na zpětnovazební učení se také můžeme dívat tak, že cílem je najít policy parametrizovanou pomocí θ, která bude maximalizovat celkovou odměnu J(θ)=E[∑T−1t=0rt+1], tj. součet odměn, které agent získá při následování policy v prostředí. Při troše snahy a derivování se dá ukázat, že gradient této celkové odměny je ∇θJ(θ)=∑T−1t=0∇θlogπθ(at|st)Gt, kde πθ(a|s) je pravděpodobnost výběru akce a ve stavu s pomocí policy π parametrizované θ a Gt jsou kumulované (diskontované) odměny od času t do T−1.
Actor-critic

Nevýhodou tohoto popisu učení je, že při velkých odměnách Gt můžeme dostávat velké rozptyly hodnot gradientu. Z toho důvodu se Gt často nahrazuje jinými výrazy - jednou z možností je přímo hodnota Q(s,a), která se potom učí podobně jako Q hodnoty v DQN. Populární je ale i tzv. advantage (výhoda), ta se spočítá jako rozdíl mezi provedením akce at ve stavu st (tj. hodnotu Q(st,at)) a hodnotou stavu V(st) - A(st,at)=Q(st,at)−V(st). Počítáme tedy, o kolik lepší je provést akci st oproti nějaké obecné akci. Pro určení advantage nepotřebujeme trénovat sítě pro Q a V, stačí jedna síť pro V, ze vztahů mezi Q a V lze odvodit, že advantage se dá spočítat i jako A(st,at)=Ra(st,st+1)+γV(st+1)−V(st). Takto implementovaná metoda se nazývá advantage actor-critic. Síť pro V hraje roli kritika a říká, jak dobré jsou stavy, kdo kterých se agent dostal, síť pro policy π potom vybírá prováděné akce.

Existuje i velmi populární metoda A3C - Asynchronous Advantage Actor-Critic. Ta nahrazuje použití experience replay tím, že se hraje více her najednou, aktualizace vah se potom průměrují přes aktualizace spočítané ve všech nezávislých hrách.
Mgr. Martin Pilát, Ph.D.
Malostranské náměstí 25
118 00 Praha
Martin.Pilat@mff.cuni.cz




Martin Pilát

    Výuka
    Výzkum

    English version

Umělý život

Poslední téma, o kterém se budeme bavit, je umělý život. Ten se zabývá systémy připomínajícími skutečný život. Cílem je pochopit, jak život (organismy) fungují a komunikují, případně život vytvořit. V umělém životě se studuje i chování skupin různých organismů.

Oblast umělého života se dá rozdělit do třech částí, podle nástrojů, které používá. V softwarovém (soft) umělém životě se používají počítačové simulace k popisu a modelování života, interakcí mezi jedinci a druhy apod. V hardwarovém umělém životě je cílem vytvořit umělé organismy, typicky jako roboty. Mokrý (anglicky wet) umělý život zase studuje biochemické procesy s cílem vytvořit např. umělou DNA.

Oblast umělého života naráží i na filosofické otázky, jako co vůbec je život, a jestli ho lze vytvořit mimo oblast chemie a biologie. Zastánci tzv. silného umělého života (strong ALife) tvrdí, že to možné je, a že život je obecný proces, který nezávisí na konkrétním médiu. Naopak pozice slabého umělého života je, že to nejde, a cílem slabého umělého života je život studovat pomocí simulací.
Celulární automaty

Jednou z prvních technik, které byly v umělém životě studovány jsou celulární automaty. To jsou (typicky) 1D nebo 2D mřížky, kde každé políčko může mít jednu z k

barev. V nejjednodušším případě jsou barvy jen dvě. Potom se často říká, že na některých políčkách je organismus a na jiných není. Na základě barvy políčka a jeho sousedů do dané vzdálenosti se potom definují pravidla pro změny barev políček.

Cíle výzkumu celulárních automatů mohou být různé - od studia celulárních automatů jako takových, až po hledání pravidel, která umožňují modelování reálných systémů (např. šíření požáru, nebo pohyb aut na silnici).
Game of Life

Jedním z nejznámějších 2D celulárních automatů je Conwayova Game of Life. Ve 2D automatech závisí nová hodnota každého políčka na všech okolních políčkách. V případě Game of Life jsou pravidla jednoduchá:

    živá buňka s méně než dvěma nebo více než třemi živými sousedy umírá
    živá buňka s dvěma nebo třemi živými sousedy přežívá
    mrtvá buňka s právě třemi živými sousedy ožívá

Na základě těchto velmi jednoduchých pravidel se dají implementovat docela zajímavé organismy, které se množí, pohybují apod. Doporučuji si najít nějaký online simulátor a pohrát si s ním (případně se podívat na materiály ze cvičení).

Z hlediska teoretické informatiky je zajímavé, že takto definovaný celulární automat je ve skutečnosti Turingovsky úplný. Na game of life implementující univerzální Turingův stroj se můžete podívat na web Paula Rendella.
Langtonův mravenec

Dalším příkladem jednoduchého chování, které může mít relativně komplikované projevy je tzv. Langtonův mravenec. Jde o mravence, který se pohybuje na mřížce se dvěma barvami. Při každém pohybu přebarví svoje políčko na opačnou barvu. V závislosti na počáteční barvě políčka se potom rozhoduje, jestli má jít doleva, nebo doprava.

Tato jednoduchá pravidla vedou k velmi složitému emergentnímu chování. Na počátku je chování mravence celkem jednoduché s vytvářením jednoduchých tvarů, potom se mravenec začne chovat chaoticky a pseudonáhodně. Nakonec ale začne opakovat posloupnost 104 kroků, které tvoří tzv. dálnici - mravenec tím utíká stále jedním směrem.

Zdá se (ale zatím to není dokázáno), že nezávisle na počáteční konfiguraci (pokud je tato konečná) mravenec vždy nakonec začne generovat tuto dálnici.

Naopak se podařilo dokázat, že i mravence lze považovat za úplný výpočetní model.
Simulace života (Tierra)

Zajímavou oblastí umělého života jsou simulace a prostředí, kde se simuluje život počítačových programů. Typickým příkladem takového systému je Tierra. Ta je implementována jako emulátor jednoduchého počítačového kódu s 32 různými instrukcemi (32 je možných kombinací instrukcí a parametrů). Tyto instrukce obsahují jednoduché aritmetické instrukce, podmínky, skoky a dva typy no-op - NOP0 a NOP1. Tyto dva typy se používají pro definování cílů skoků. Pokud máme někde instrukci pro skok, následuje po ní několik NOPx instrukcí. Při skoku se potom hledá nejbližší místo v paměti, kde je komplementární posloupnost instrukcí (NOP0 je komplementární k NOP1 a naopak). Tímto způsobem Tierra řeší problém s adresováním místo používání absolutních nebo relativních adres. Má to také připomínat komplementární páry bází v DNA.

Všichni jedinci v systému Tierra běží “paralelně” - každý má přiřazen virtuální procesor, který vždy provede několik instrukcí jedince a následně se provede několik instrukcí dalšího jedince atd. Jedinci nemohou přepisovat instrukce jiného jedince, ale mohou je číst a vykonávat (cíle skoku mohou být i v jiných jedincích).

Na začátku simulace začíná s jedním jedincem, který umí sám sebe zkopírovat. Při kopírování je malá šance, že dojde k mutaci bitu v jedinci. Ukazuje se, že tímto způsobem se po nějaké době vyvinou zajímaví jedinci - někteří se chovají jako paraziti, neobsahují vlastní kopírovací proceduru, ale pokud žijí v populace s jedinci, kteří ji mají, tak ji mohou použít. Díky tomu jsou menší a mohou se rychleji kopírovat. Objevily se ale i další zajímavé typy jedinců. Někteří se umí těmto parazitům bránit. Jiní jsou hyper-paraziti - “přesvědčí” parazita, aby kopíroval je, místo sebe.

Moc pěkné povídání o systému Tierra je přímo v originálním článku.

Systém Tierra inspiroval další podobné systémy, jako např. Avida.
Creatures

Počítačová hra Creatures je dalším příkladem umělého života. Hráč v ní má za úkol starat se o tzv. Norny, což jsou hravé příšerky. Musí je učit (Norni mají neuronovou síť jako mozek), pomáhat jim prozkoumávat prostředí a bránit se před jinými druhy.
Simulace složitých systémů

Jednou z aplikací umělého života jsou i simulace složitých (nejen) biologických systémů. Takové simulace mohou být dvou základních typů. Black-box simulace se soustředí na imitaci nějakého chování bez ohledu na to, jestli jejich vnitřní struktura nějakým způsobem souvisí s reálnou vnitřní strukturou. Na druhou stranu white-box modely se soustředí na simulaci založenou na principech, které byly pozorovány i v reálném světě. Typicky jsou založené na přesném pochopení studovaného systému.
Mgr. Martin Pilát, Ph.D.
Malostranské náměstí 25
118 00 Praha
Martin.Pilat@mff.cuni.cz
