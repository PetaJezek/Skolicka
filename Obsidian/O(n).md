
```
a) If f(n) = O(g(n)), then g(n) = O(f(n)).
b) If f(n) = O(g(n)), then 2^f(n) = O(2^g(n)).
c) If f(n) = O(g(n)), then g(n) = Ω(f(n)).
d) f(n) = O(f(n)^2)
```


a) NEPLATÍ pouze pokud f(n) = g(n)
b) PLATÍ, n v 2^n bude vždy větší v g(n) než v f(n), protože platí f(n) = O(g(n)).
c) PLATÍ. druhé věta je inverze věty první
d)NEPLATÍ,  pouze od $$ n > 1 $$ . 