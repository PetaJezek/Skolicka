a)
$$
\lim_{n \to \infty} \frac{2^n + 3^n + 5^n}{2^{n+1} + 3^{n+1} + 5^{n+1}}
$$
Muzeme vydelit zlomek $5^n$:
$$
\lim_{n \to \infty} \frac{  \frac{2^n}{5^n} + \frac{3^n}{5^n}+ 1}{2\cdot\frac{2^{n}}{5n} + 3 \cdot \frac{3^{n+1}}{5^n} + 5}
$$
Všechny členy obsahující zlomek jdou k nule, takže nám zbyde: 
$$
\lim_{n \to \infty} \frac{2^n + 3^n + 5^n}{2^{n+1} + 3^{n+1} + 5^{n+1}} = \lim_{n \to \infty} \frac{1}{5}
$$


b)
$$
\lim_{n \to \infty} \frac{3n^2 + 2n + 1}{n^2 + 2n + 3}
$$

Po vydeleni $n^2$ nam zbyde,:
$$
\lim_{n \to \infty} \frac{3n^2 + 2n + 1}{n^2 + 2n + 3} =\lim_{n \to \infty} \frac{3}{1}=3
$$
protoze vsechno ostatni jde k nule.

c)
$$
\lim_{n \to \infty} \frac{2^n}{n!}
$$
Pokud rozepiseme citatele dostaneme: $2_{1}\cdot 2_{2} \cdot \dots  2_{n}$. 
Pokud rozepise jmenovatele dostaneme: $n \cdot (n-1) \cdot (n-2) \cdot \dots . 2 \cdot 1$
Pro n>4 je jmenovatel vetsi nez citatel. Pro $n+1$ se citatel vynasobi dvema a jmenovatel n. Tedy jmenovatel exponencialne roste oproti citateli. Proto
$$
\lim_{n \to \infty} \frac{2^n}{n!} = 0
$$
Proste roste mnohem rychleji.

d)
$$
\lim_{n \to \infty} \frac{3^n + n!}{3n! - 2^n}
$$

Cleny $3^n$ a $2^n$ nerostou tak rychle jako faktorialy. Pro velke n na nich tedy nebude zalezet. Proto muzeme limitu upravit jako:
$$

\lim_{n \to \infty} \frac{3^n + n!}{3n! - 2^n}=\lim_{ n \to \infty } \frac{n!}{3n!}= \lim_{ n \to \infty } \frac{1}{3}
$$


e)
$$
\lim_{n \to \infty} \frac{\lfloor \sqrt{ n } \rfloor}{\sqrt{ n }}
$$

Cim vetsi n budeme mit, tim vic budou zanedbatelne rozdily v zaokrouhleni. Ty rozdili totiz nebudou nikdy nic vic nez jedna. Proto zaokrouhleni zanedbat a ziskavame:
$$

\lim_{n \to \infty} \frac{\lfloor \sqrt{ n } \rfloor}{\sqrt{ n }} = \lim_{ n \to \infty } \frac{\sqrt{ n }}{\sqrt{ n }}=\lim_{ n \to \infty }  1
$$


f)
$$
\lim_{n \to \infty} \sqrt{ n }(\sqrt{ n+1 } -\sqrt{ n-1 })
$$

Pro velke $n$ se zavorka $(\sqrt{ n+1 } -\sqrt{ n-1 })$ bude blizit 1. Protoze rozdil mezi $\sqrt{ n+1 }$ a $\sqrt{ n-1 }$ bude zanedbatelny. Dostavame:
$$
\lim_{n \to \infty} \sqrt{ n }(\sqrt{ n+1 } -\sqrt{ n-1 }) = \lim_{ n \to \infty }\sqrt{ n }(1)=\lim_{ n \to \infty }\sqrt{ n }  
$$

g)
$$
\lim_{n \to \infty} \left( \frac{1}{n^2+1} + \frac{1}{n^2+2} + \dots + \frac{1}{n^2+n} \right)=
$$

$$
= \lim_{n \to \infty} \sum^{n}_{i=1} \frac{1}{n^2 + i} = \sum^{n}_{i=1}\lim_{n \to \infty} \frac{1}{n^2 + i}
$$

Tato limita:
$$
\lim_{ n \to \infty } \frac{1}{n^2+i}; i \in \{1,\dots,n\} 
$$
pro kazde $i$ míří k 0.  Soucet techto limit je tedy take nula.

$$
\lim_{n \to \infty} \left( \frac{1}{n^2+1} + \frac{1}{n^2+2} + \dots + \frac{1}{n^2+n} \right)=0
$$

