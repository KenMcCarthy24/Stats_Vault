$Y$ is a random variable from the exponential family if its distribution can be written as:

$$
f(y;\theta,\phi) = exp\left(\frac{y\theta - b(\theta)}{a(\phi)} + c(y, \phi)\right)
$$
Where:
* a, b, and c are some functions
* $\theta$ is a canonical or natural parameter controlling the location of the distribution
* $\phi$ is a dispersion parameter controlling the scale of a distribution
---
# Properties
* Only distributions in this family can be used as the basis for a [[Generalized Linear Model]]
* Exponential Family distributions always have conjugate priors
* For distributions in the exponential family the mean and variance can be found by:
	* $\mu = b'(\theta)$
	* $\sigma^2 = \phi b''(\theta)$
---
## Examples of Exponential Family Distributions

* [[Normal]]
* [[Gamma]]
* [[Beta]]
* [[Bernoulli]]
* [[Binomial]] (with fixed number of trials)
* [[Negative Binomial]] (with fixed number of failures)
* [[Poisson]]
* [[Exponential]]
* [[Chi-Squared]]
* [[Dirichlet]]
* [[Categorical]]
* [[Geometric]]
---

> [!example]- Example: [[Binomial]] Distribution Proof
> Assume number of trials $n$ is fixed
> 
> $Y \sim Bin(n, p)$ has a PMF given by
> 
> $$f(y;n,p)= \binom{n}{y} p^y (1-p)^{n-y}$$
> Take the exp of the natural log and simplify:
> 
> $$
> \begin{split}
> f(y;n,p) &= exp(\ln(\binom{n}{y} p^y (1-p)^{n-y})) \\
> &=exp(\ln(\binom{n}{y}) + y\ln(p) + (n-y)\ln(1-p)) \\
> &=exp(y\ln(\frac{p}{1-p}) + n\ln(1-p) + ln(\binom{n}{y}))
> \end{split}
> $$
> Let:
> * $a(\phi) = 1$
> * $b(\theta) = -n\ln(1-p)$
> * $c(y, \phi) = ln(\binom{n}{y})$
> * $\displaystyle \theta = \frac{p}{1-p}$ or $\displaystyle p=\frac{e^\theta}{1+e^\theta}$
> 
> Now:
> $$
> f(y;n,p) = exp\left(\frac{y\theta - b(\theta)}{a(\phi)} + c(y, \phi)\right)
> $$
> 
> $\therefore Bin(n, p)$ is in the exponential family of distributions. 
> 
> $$
> \begin{split}
> \mu = b'(\theta) &= \frac{\partial}{\partial \theta} \left[ -n\ln(1-p)\right] \\
> &= -n\frac{\partial}{\partial \theta} \left[\ln(1-\frac{e^\theta}{1+e^\theta})\right] \\
> &= -n\frac{\partial}{\partial \theta} \left[\ln(\frac{1}{1+e^\theta})\right] \\
> &= n\frac{\partial}{\partial \theta} \left[\ln(1+e^\theta)\right] \\
> &= \frac{ne^\theta}{1+e^\theta} \\
> &= np
> \end{split}
> $$
> 
> $$
> \begin{split}
> \sigma^2 = \phi b''(\theta) &= 1*\frac{\partial}{\partial \theta} \left[\frac{ne^\theta}{1+e^\theta}\right] \\
> &=n\left(\frac{e^\theta(1+e^\theta)-e^\theta e^\theta}{(1+e^\theta)^2}\right) \\
> &=n\left(\frac{e^\theta}{(1+e^\theta)^2}\right) \\
> &=np\left(\frac{1}{1+e^\theta}\right) \\
> &=np\left(1-\frac{e^\theta}{1+e^\theta}\right) \\
> &=np(1-p)
> \end{split}
> $$
> These match the known mean and variance of the binomial distribution.