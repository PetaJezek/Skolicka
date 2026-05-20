Necht nahodny vyber $X_{1},\dots X_{n}$~ $Bern(\theta)$, kde $\theta \in [0,1]$ je neznamý parametr. 


$$
S=\sum_{i=1}^{n} X_{i}
$$

Na prednasce byl MLE estimator. 
Nyni zavedeme:

$$
\hat{\theta}'=\frac{S+1}{n+2}
$$



1.  Spočtěte $bias(\hat{\theta}')$. Pro ktere $\theta$ je bias neg/pos?

$$
bias(\hat{\theta}') = E[\hat{\theta}] - \theta
$$

Protoze: 
$$
E[\hat{\theta}] = \frac{E[S]+1}{n+2}
$$
$$
bias(\hat{\theta}') = \frac{E[S]+1}{n+2}  - \theta  = \frac{n\theta+1 - \theta n - 2\theta}{n+2} = \frac{1-2\theta}{n+2}
$$

Pro ktere $\theta$ je bias neg/pos?


Pro $\theta >0.5 \implies$ je bias zaporny.
Pro $\theta < 0.5\implies$ je bias kladny.


2. Spoctete varianci $\hat{\theta}'$.

$$
Var(\hat{\theta}') = E[\hat{\theta}^2] - (E[\hat{\theta}])^{2}
$$

$$
= E[\left( \frac{S+1}{n+2} \right)^{2}] -  \left( \frac{E[S]+1}{n+2} \right)^{2}
$$

$$
= E\left[ \frac{S^{2}+2S+1}{(n+2)^{2}} \right] - \left( \frac{\theta^{2}n^{2}+2\theta n+1}{(n+2)^{2}} \right)
$$

$$
=\frac{n\theta(1-\theta) + n^{2}\theta^{2}+2\theta n+1}{(n+2)^{2}}  - \frac{\theta^{2}n^{2}+2\theta n+1}{(n+2)^{2}} 
$$

$$
Var(\hat{\theta}') = \frac{n\theta  - n\theta^{2}}{(n+2)^{2}}
$$

3. Spoctete $MSE(\hat{\theta}')$

$$
MSE(\hat{\theta}') = E[(\hat{\theta}-\theta)^{2}] = Var(\hat{\theta}') + Bias(\hat{\theta}')^{2}
$$

$$
 =  \frac{n\theta  - n\theta^{2}}{(n+2)^{2}} + \left( \frac{1-2\theta}{n+2} \right) ^{2}
$$
$$
 = \frac{n\theta-n\theta^{2} + 1 - 4\theta + 4\theta^{2}}{(n+2)^{2}} = \frac{(1-\theta)(n-4)\theta+1}{(n+2)^{2}}
$$



