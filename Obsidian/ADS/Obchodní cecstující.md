Takže nejprve najdeme minimální kostru grafu G a z ní se budeme snažit udělat naši hledanou kružnici. Vybereme libovolný vrchol a z něj spustíme dfs, které bude označovat vrcholy podle toho, kdy je otevře. Z tohoto označení nám vznikne posloupnost vrcholů grafu G resp. minimální kostry grafu G. Nyní budeme postupovat následovně:

 1. Budeme přidávat vrcholy postupne jak určuje získaná posloupnost. Jsou dvě možnost, které mohou nastat když opouštíme bod $u$ a chceme přidat následující bod $v$:
 - a) pokud hrana $\left| uv \right|$ je součástí minmální kostry, přidáme bod v
 - b) pokud hrana $\left| uv \right|$ není součásti minimální kostry, přidáme bod přes tuto hranu, o které víme, že je maximálně stejně dlouhá jako cesta z $u$ do $v$ po hranách naší minimální kostry. 
 Pokud do posloupnosti (fronty) přidáme vrchol, ze kterého jsme spouštěli DFS (tedy bude v posloupnosti dvakrát), získáváme kružnici. Jelikož všechny hrany kostry jsou využity dvakrát, jednou při sestupu z kořene (libovolného bodu) stromu a jednou při návratu zpět. Znamená to, že celková délka této kružnice bude: $$
2\cdot l(K)
$$

kde $l(K)$ je součet hran minimální kostry.

A protože víme, že $l(K)\leq \text{"hledana kruznice"}$, tak získáváme: 

$$
\text{nase kruznice } = 2 \cdot l(K)  \geq \text{"hledana kruznice"}
$$
Našli jsme kruznici, která je maximálně dvakrát delší než minimální kružnice přes všechny vrcholy.
