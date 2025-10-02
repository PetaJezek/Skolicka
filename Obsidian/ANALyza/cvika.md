absolutni hodnota:
$$
M= \mathbb{R}, d(x,y) = \left| x-y \right|
$$

$$
d(x,y) = 0
$$




Euklidovska metrika

$$
d_{2}(x,y)= \sqrt{ \sum_{i=1}^{n} \left| x_{i}-y_{i} \right|^2 }
$$


3)
$$
\forall x,y,z : d(x,y) \leq d(x,z) +d(z,y)
$$

$$
\sqrt{ \sum_{i=1}^{n} \left| x_{i}-y_{i} \right|^2 } \leq \sqrt{ \sum_{i=1}^{n} \left| x_{i}-z_{i} \right|^2 } + \sqrt{ \sum_{i=1}^{n} \left| z_{i}-y_{i} \right|^2 } 
$$
$$
\sum_{i=1}^{n} \left| x_{i}-y_{i} \right|^2 \leq  \sum_{i=1}^{n} \left| x_{i}-z_{i} \right|^2  + \sqrt{ \sum_{i=1}^{n} \left| x_{i}-z_{i} \right|^2\cdot \left| z_{i}-y_{i} \right|^2 } + (\sum_{i=1}^{n} \left| z_{i}-y_{i} \right|^2)
$$