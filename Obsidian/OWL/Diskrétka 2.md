Výrok budeme dokazovat indukční metodou. Pokud výrok bude platit pro nejmenší $n$ a pro $n + 1$,tak můžeme říct, že výrok platí.

Pojdmě dokázat, že platí pro nejmenší n.
$$
\frac{1}{1*3} + \frac{1}{3*5} + \frac{1}{5*7} + \cdots + \frac{1}{(2n+1)*(2n-1)} = \frac{n}{2n+1}
$$


Protože $n \in \mathbb{N}:$ nejmenší n je 1.

Dostáváme rovnici:
$$
\frac{1}{(2n+1)*(2n-1)} = \frac{n}{2n+1}
$$


Po dosazení $n = 1$:
$$
\frac{1}{(3)*(1)} = \frac{1}{3}
$$
To platí.

A teď pro n + 1:
$$
\frac{n}{(2n+1)} +\frac{1}{(2n+3)*(2n+1)} = \frac{n+1}{2n+3}
$$
$$
n(2n+3) + 1 = (n+1)\cdot(2n+1)
$$
$$
2n^2 + 3n + 1 = 2n^2 + 3n + 1
$$
Strany se rovnají, takže tvrzení bylo pravdivé.

