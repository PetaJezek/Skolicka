Martin Pilát

    Výuka
    Výzkum

    English version

Průběh zkoušky a požadavky

Zkouška se skládá ze dvou částí - v jedné dostanete za úkol navrhnout způsob, jak pomocí probíraných metod vyřešit zadaný problém. Může se například jednat o optimalizační problém řešitelný pomocí evolučních algoritmů, nebo o problém ze strojového učení řešitelný pomocí neuronových sítí. V prvním případě je potřeba navrhnout celý evoluční algoritmus (kódování jedince, operátory), ve druhém případě je potřeba popsat vhodnou architekturu neuronové sítě a popsat, jak ji trénovat (jaká je chybová funkce). V obou případech očekávám, že své volby budete umět nějak zdůvodnit, případně diskutovat, jaké jiné možnosti pro řešení připadají v úvahu.

V další části dostanete dvě otázky týkající se přímo témat probíraných na přednáškách (viz seznam níže).

Na vyřešení první části budete mít dostatek času (30 minut), ve druhé části budete mít také čas na přípravu. Při online zkoušce bude potřeba řešení první části (napsané na papíře) vyfotit/naskenovat a poslat ihned po ukončení této části. Druhá část probíhá hned po první části, napřed projdeme vaše řešení první části a potom dostanete zadané dvě otázky z probraných témat. Výsledek první části nemá vliv na postup do druhé části, pořadí částí je dané hlavně praktičností provedení celé zkoušky.
Co je potřeba umět?

    Základy strojového učení

    vysvětlit rozdíly mezi jednotlivými typy strojového učení (učení s učitelem, bez učitele, zpětnovazební učení)
    vysvětlit rozdíly mezi jednotlivými úlohami strojového učení s učitelem (regrese, klasifikace)
    popsat typy příznaků (kategorické, ordinální, číselné) a jejich předzpracování (kódování kategorických a ordinálních příznaků, škálování číselných příznaků)

    Zpětnovazební učení

    popsat problém zpětnovazebního učení intuitivně (agent, prostředí, hledání strategie)
    popsat prostředí jako Markovský rozhodovací proces
    definovat zpětnovazební učení jako problém hledání strategie maximalizující celkovou odměnu agenta
    definovat pojmy hodnota stavu a hodnota akce
    popsat základní myšlenku Monte-Carlo metod (v rozsahu podle textu na webu)
    vysvětlit Q-učení (včetně vzorce pro aktualizaci matice Q)
    popsat algoritmus SARSA
    vysvětlit, jak použít Q-učení v prostorech se spojitými stavy a akcemi

    Jednoduchý genetický algoritmus

    popsat základní verzi evolučního algoritmu s binárním kódováním
    popsat základní genetické operátory (jednobodové, n

-bodové křížení, mutace)
popsat ruletovou a turnajovou selekci
vysvětlit výhody a nevýhody turnajové a ruletové selekce
vysvětlit, co je fitness funkce
popsat elitismus
popsat metody pro environmentální selekci (přenos jedinců do další populace), (μ,λ)
a (μ+λ)

    popsat rozšíření jednoduchého GA na problémy s celočíselným kódováním

    Evoluční algoritmy pro spojitou optimalizaci

    definovat problém spojité optimalizace
    popsat genetické operátory používané ve spojité optimalizaci - aritmetické křížení, zatížené a nezatížené mutace
    vysvětlit rozdíl mezi separabilními a neseparabilními funkcemi
    popsat algoritmus diferenciální evoluce a jeho výhody

    Evoluční algoritmy pro kombinatorickou optimalizaci

    popsat mutace pro permutační kódování
    popsat křížení používaná při permutačním kódování (OX, PMX, ER)
    vysvětlit použití evolučních algoritmů pro problém obchodního cestujícího

    Lineární a kartézské GP, gramatická evoluce

    popsat lineární genetické programování (kódování jedince, operátory)
    popsat kartézské genetické programování (kódování jedince, operátory)
    popsat gramatickou evoluci (kódování jedince, operátory)
    vysvětlit, jak řešit problém s příliš krátkým nebo dlouhým jedincem v gramatické evoluci

    Stromové genetické programování

    popsat stromové genetické programování a jeho genetické operátory
    popsat práci s konstantami ve stromovém genetickém programování
    popsat typované genetické programování
    popsat automaticky definované funkce
    vysvětlit, jak u automaticky definovaných funkcí zabránit zacyklení/nekonečné rekurzi
    porovnat jednotlivé typy genetického programování a jejich výhody/nevýhody

    Perceptronové neuronové sítě

    popsat, jakým způsobem počítá jeden perceptron
    popsat algoritmus pro trénování perceptronu a vysvětlit, kdy konverguje
    popsat strukturu vícevrstvých perceptronových sítí
    popsat aktivační funkce používané ve vícevrstvých perceptronech (sigmoida, tanh, ReLU)
    popsat metodu pro trénování neuronových sítí (backpropagation)
    odvodit pravidla pro adaptaci vah v metodě zpětného šíření (alespoň pro výstupní vrstvu + ideu pro skryté vrstvy)

    RBF sítě

    popsat RBF jednotku a architekturu RBF sítě
    vysvětlit princip trénování RBF sítí
    popsat algoritmus k

    -means
    porovnat geometrické vlastnosti RBF sítí a vícevrstvých perceptronů

    Konvoluční sítě

    popsat funkci konvolučního filtru
    popsat funkci pooling vrstev v konvoluční síti
    popsat architekturu konvoluční neuronové sítě
    vysvětlit, co jsou matoucí vzory a jak ovlivňují praktické nasazení neuronových sítí
    popsat algoritmus FGSM pro vytváření matoucích vzorů
    vysvětlit myšlenku přenosu uměleckého stylu
    vysvětlit základní fungovaní generative adversarial networks (podle rozsahu v textu na webu)

    Rekurentní neuronové sítě

    definovat, co jsou rekurentní neuronové sítě
    vysvětlit, kde se rekurentní sítě používají
    vysvětlit trénování rekurentních sítí pomoci algoritmu zpětného šíření v čase
    vysvětlit problém s explodujícími a mizejícími gradienty
    popsat princip Echo State sítí
    popsat trénování Echo State sítí
    popsat LSTM buňku a architekturu LSTM sítě
    vysvětlit výhody Echo State sítí a LSMT sítí v porovnání se základními rekurentními sítěmi

    Neuroevoluce

    popsat použití evolučních algoritmů pro trénování vah v neuronové síti
    popsat algoritmus NEAT - reprezentace jedince, operátory
    vysvětlit význam inovačních čísel v algoritmu NEAT
    popsat myšlenku algoritmu HyperNEAT
    popsat rozšíření algoritmu NEAT pro hledání architektur neuronových sítí (algoritmus coDeepNEAT)
    vysvětlit myšlenku algoritmu novelty search
    porovnat novelty search a evoluční algoritmy a diskutovat jejich výhody/nevýhody

    Hluboké zpětnovazební učení

    vysvětlit algoritmus hlubokého Q-učení
    porovnat Q-učení a hluboké Q-učení
    popsat triky s experience replay a target network
    vysvětlit vliv experience replay a target network na hluboké Q-učení
    popsat algoritmus DDPG
    popsat actor-critic přístupy
    popsat advantage a zdůvodnit, proč se používá
    popsat metodu A3C

    Particle Swarm Optimization

    popsat aktualizaci poloh a rychlostí v PSO
    popsat topologie používané v PSO (globální, geometrické, sociální)
    vysvětlit vliv topologií na algoritmus PSO
    vysvětlit použití PSO pro řešení problémů ve spojité optimalizaci

    Ant Colony Optimization

    vysvětlit základní pojmy ACO - feromon, atraktivita
    popsat generování řešení pomocí ACO
    popsat aktualizaci feromonu na základě kvality nalezeného řešení
    popsat použití ACO pro řešení problému obchodního cestujícího a vehicle routing problému

    Artificial Life

    vysvětlit rozdíly mezi jednotlivými typy umělého života (soft, hard, wet)
    vysvětlit rozdíly mezi silným a slabým umělým životem
    popsat 1D a 2D celulární automaty
    popsat pravidla Game of Life
    popsat pravidla Langtonova mravence
    vysvětlit pojem dálnice u Langtonova mravence
    popsat systém Tierra
    popsat jedince v systému Tierra
    vysvětlit způsob adresování (definování cílů skoku) v systému Tierra
    popsat příklady vytvořených jedinců v sytému Tierra (paraziti)

Mgr. Martin Pilát, Ph.D.
Malostranské náměstí 25
118 00 Praha
Martin.Pilat@mff.cuni.cz
