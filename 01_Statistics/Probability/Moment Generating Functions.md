
The **moment generating function (MGF)** of a [[Random Variable]] $X$ is a function that encodes all of the [[Expectation and Moments|raw moments]] of the distribution (when it exists).

It is defined as:
$$
M_X(t) = E[e^{tX}]
$$

For discrete and continuous random variables:

$$
M_X(t) = \sum_k e^{tk} P(X = k)
\quad \text{(Discrete Case)}
$$

$$
M_X(t) = \int_{-\infty}^{\infty} e^{tx} f(x)\, dx
\quad \text{(Continuous Case)}
$$

---

#### Relationship to Moments

If $M_X(t)$ exists in an open interval around $t = 0$, then the $j$-th raw moment can be obtained by differentiation:

$$
\mu_j = E[X^j] = M_X^{(j)}(0)
$$

That is, the $j$-th moment is the $j$-th derivative of the MGF evaluated at $t = 0$.

---

#### Key Properties

* **Uniqueness**: If two random variables have the same MGF (in a neighborhood of $0$), they have the same distribution.
* **MGF of a sum**: If $X$ and $Y$ are independent,
  $$
  M_{X+Y}(t) = M_X(t)\, M_Y(t)
  $$
* **Existence**: Not all distributions have an MGF (e.g. Cauchy).

---

> [!example]-
> The moment generating function can be used to find the mean and variance of the [[Exponential]] distribution
> 
> If $X\sim \text{Exp}(\lambda)$, the known MGF is:
> 
> $$M_X(t) = \frac{\lambda}{\lambda - t}\text{  for  }t<\lambda$$The first two derivatives are
> 
> $$M_X^{(1)}(t) = \frac{\lambda}{(\lambda - t)^2}$$
> $$M_X^{(2)}(t) = \frac{2\lambda}{(\lambda - t)^3}$$
> So:
> $$\mu = E[X] = M_X^{(1)}(0) = \frac{\lambda}{\lambda^2} = \frac{1}{\lambda}$$
> $$E[X^2] = M_X^{(2)}(t) = \frac{2\lambda}{\lambda^3} = \frac{2}{\lambda^2}$$
> $$\sigma^2 = E[X^2] -E[X]^2 = \frac{2}{\lambda^2} -(\frac{1}{\lambda})^2 = \frac{1}{\lambda^2}$$
> 
> These match the mean and variance obtained by integration of the pdf.