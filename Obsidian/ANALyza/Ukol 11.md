
Uvažujme funkci $f:R→R$ definovanou vzorcem$f(x)=∣x^2−1∣(x+1)$.

- a) Ve kterých bodech $\mathbb{R}$ má tato funkce vlastní derivaci?
- b) Najděte všechny body, v nichž tato funkce nabývá lokální či globální extrémy, a určete, o jaký typ extrému se jedná (zda jen lokální nebo i globální, zda minimum nebo maximum).
- c) Najděte co největší otevřený interval  $I$ obsahující nulu, na němž je tato funkce konvexní nebo konkávní, a uveďte, zda je $f$ na $I$ konvexní, nebo zda je tam konkávní.


Muzeme funkci prepsat jako:
$$
f(x)= \left| (x - 1)(x+1) \right|(x+1)
$$
Absolutni hodnota otaci znamenko pouze na intervalu $(-1;1)$.

Nejdrive vysetrime derivaci mimo tento interval:

$$
f(x) = (x-1)^2(x+1) = (x^2-2x+1)(x+1) = x^3 -2x^2 +x +x^2 - 2x +1
$$
$$
= x^3 -x^2 -x + 1
$$

Derivace tohoto se rovna:

$$
f'(x)_{1}=3x^2 -2x -1
$$

Nyni na intervalu $(-1;1)$:
$$
f(x) = (1-x^2)(x+1) = x +1 -x^3 -x^2
$$

Derivace tohoto je:
$$
f'(x)_{2}= -3x^2-2x+1
$$
Checeme najit body bez vlastni derivace.

Ty muzou byt na prechodu techto dvou funkci, protoze sami o sobe jsou spojite (trivialni).

Musime vysetrit hodnoty v bodech $\pm 1$.

Pro -1:
$$
3x^2-2x-1 = -3x^2 -2x +1
$$
$$
3 + 2 - 1 \neq -3 +2 + 1
$$
Derivace se tedy nerovna a v bode -1 neexistuje vlastni derivace.

Pro +1:
$$
3 -2 -1 = -3 -2 +1
$$
Taky se nerovnaji, takze ani v bode 1 neexistuje vlastni derivace.

Tedy odpoved na otazku je:
	f(x) ma vsude derivaci krome bodu $\pm 1$.
b)
