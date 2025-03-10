Rozhodněte, jaký výsledek dává vzhledem k argumentům x,y∈Nx,y∈N následující funkce. Zápis není v žádném konkrétním programovacím jazyku, operátor `/` značí celočíselné dělení. Určete časovou složitost vůči hodnotám $x,y$ a přepište funkci na nerekurzivní.

```
f(x,y):
  if y==0 => return 0
  else if even(y) => return 2*f(x, y/2)
  else => return 2*f(x, y/2) + x
```



pro x,y (2,3):
f(2,3) = 2*f(2,1) + 2 = 2*(2*f(2,0)+2)+2= 2*(2*0+2)+2= 6= 2 + 2 + 2


Pokud bychom zvýšili y o jedna, dostali bychom že y je liché a výsledek by se zvýšil o dva.

Protože to jak "probíhá" funkce f nezáleží na x, nemusíme za něj dosazovat číslo.
Output pro:
- y = 1: x
- y = 2: 2x
- y = 3: 3x
....
To znamená, že f odpovídá násobení dvou přirozených čísel x,y.

**Takže výsledek této funkce je $x*y$.**

Časová složitost nezávisý na x, ale pouze na y.

Každým druhým zvýšením y se zvyší počet výpočtů. Takže časová složitost je O(n/2+1). 


```
f(x,y):
 int n
 int m
  while y is even:
	  n++ 
	  y = y/2
  while y /2 is int:
	  m= 2*m + x
	y = y/2
  return 2**n * m
```