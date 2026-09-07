Let $X$ be some [[Random Variable]] and let $Y=g(X)$ be some transformation of that random variable. The pdf of the distribution of the random variable $Y$ is given by:
$$f_Y(y) = f_X(g^{-1}(y))\left|\frac{dg^{-1}(y)}{dy}\right|$$

Where:
* $f_Y(y)$: The pdf of the transformed random variable $Y$
* $f_X(x)$: The pdf of the original random variable $X$
* $g(x)$: The transformation function.
	* Must be monotonically increasing on the support of $X$ for the above equation to be valid.
* $g^{-1}(x)$: The inverse function of the transformation function $g(x)$ between $X$ and $Y$

> [!example]- Example: [[Exponential]] Transform
> Let $X \sim Exp(\lambda)$. What is the distribution of $Y=X^2 + 4$
> 
> $$f_X(x) = \lambda \exp(-\lambda x), x \geq 0$$
> $$g(x) = x^2 + 4$$
> 
> $g(x)$ is monotonically increasing for $x \geq 0$.  
> 
> $$g^{-1}(y) = \sqrt{y-4}$$
> $$\left|\frac{dg^{-1}(y)}{dy}\right| = \left|\frac{d}{dy}\sqrt{y-4}\right| = \frac{1}{2\sqrt{y-4}}$$
> 
> So:
> 
> $$f_Y(y) = \begin{cases} \frac{\lambda \exp(-\lambda\sqrt{y-4})}{2\sqrt{y-4}} & y \ge 4 \\ 0 & \text{otherwise} \end{cases}$$

# Law of the Unconscious Statistician
The **Law of the Unconscious Statistician (LOTUS)** states that the expectation value of a transformed random variable $E(g(X))$ can be found using only $f_X(x)$ — the probability distribution of $X$ — directly, without having to first calculate $f_Y(y)$. 

In the discrete case:
$$E[g(X)] = \sum_ig(x_i)P(X=x_i)$$

In the continuous case:
$$E(g(X)) = \int_{-\infty}^\infty g(x)f_X(x)dx$$

> [!example]- Example: LOTUS with [[Continuous Uniform]] Distribution
> Let $X \sim \text{Uniform}(0,1)$. Find $E[X^2]$.
> 
> Here $g(X) = X^2$ and $f_X(x) = 1$ for $x \in [0,1]$. By LOTUS, compute the expectation directly without finding the distribution of $Y = X^2$:
> 
> $$E[X^2] = \int_0^1 x^2 \cdot 1 \, dx = \left[\frac{x^3}{3}\right]_0^1 = \frac{1}{3}$$

