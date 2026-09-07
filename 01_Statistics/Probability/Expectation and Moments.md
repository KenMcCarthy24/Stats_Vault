For a [[Random Variable]] $X$, the moments of the distribution are a set of key statistics that describe the distribution's shape and characteristics.

There are two types of moment:
* **Raw Moment**: Describe the distribution relative to the origin (0)
* **Central Moment**: Describe the distribution relative to its mean $\mu$

For [[Discrete Probability Distributions|Discrete Distributions]] these are calculated with sums and for [[Continuous Probability Distributions|Continuous Distributions]] these are calculated with integrals.

The $j$-th **raw moment** of a distribution is calculated by:

$$
\mu_j = E[X^j] = \sum_k k^j P(X = k)
\quad \text{(Discrete Case)}
$$

$$
\mu_j = E[X^j] = \int_{-\infty}^{\infty} x^j f(x)\, dx
\quad \text{(Continuous Case)}
$$

The $j$-th **central moment** of a distribution is calculated by:

$$
\mu'_j = E[(X - \mu)^j] = \sum_k (k - \mu)^j P(X = k)
\quad \text{(Discrete Case)}
$$

$$
\mu'_j = E[(X - \mu)^j] = \int_{-\infty}^{\infty} (x - \mu)^j f(x)\, dx
\quad \text{(Continuous Case)}
$$


where $\mu = E[X]$ is the mean of the distribution (and first raw moment).

Note: if a distribution is symmetric about the mean, then all odd central moments $(\mu_1', \mu_3', \dots)$ are 0

---
# Notable special cases:

### 1st Raw Moment: Expectation Value

The first raw moment $\mu=E[X]$ is the **Expectation Value** or **Mean** of the distribution and is a measure representing the center of the distribution. It can also be viewed as a probability weighted average of all possible values $X$ can take. 

Expectation is a linear operator so:
$$E[aX+bY] = aE[X] + bE[Y]$$
If two random variables $X$ & $Y$ are independent of each other then:
$$E[XY] = E[X]E[Y]$$
### 2nd Central Moment: Variance

The second central moment $\mu_2' = \sigma^2= E[(X-\mu)^2]$ is the **variance** of the distribution and is a measure of the spread of a distribution, quantifying how far from the mean the values tend to be.

A related quantity is the **standard deviation** $\sigma = \sqrt{\sigma^2}$, which is the root mean square distance of values from the mean. The standard deviation has the same units as $X$

Variance can also be computed as the difference between the second raw moment and the square of the first raw moment:
$$\sigma^2= E[(X-\mu)^2] = E[X^2] - E[X]^2$$

Other Properties:
* $Var(aX) = a^2Var(X)$
* $Var(X+c) = Var(X)$
* If $X$ and $Y$ are independent then $Var(X+Y) = Var(X) + Var(Y)$
	* In this case $\mathrm{Cov}(X,Y)=0$
* If $X$ and Y are not independent then $Var(X+Y) = Var(X) + Var(Y) + 2\,\mathrm{Cov}(X,Y)$

$\mathrm{Cov}(X,Y)$ is a related concept — the [[Covariance and Correlation]]. 

### 3rd Central Moment: Skewness

The third central moment $\mu_3' = E[(X - \mu)^3]$ measures the **asymmetry** of a distribution about its mean.

Because $\mu_3'$ depends on the scale of $X$, skewness is typically expressed in a **standardized** (dimensionless) form called the **skewness coefficient**:

$$
\gamma_1 = \frac{\mu_3'}{\sigma^3} = \frac{E[(X - \mu)^3]}{\sigma^3}
$$

Interpretation:
* $\gamma_1 > 0$: **Right-skewed** (longer or heavier right tail)
* $\gamma_1 < 0$: **Left-skewed** (longer or heavier left tail)
* $\gamma_1 = 0$: Symmetric distribution (e.g. Normal)

Notes:
* Skewness captures *direction* of asymmetry, not just magnitude.
* A distribution can be highly skewed even if its mean and variance are finite.
* Symmetry implies $\mu_3' = 0$, but $\mu_3' = 0$ alone does not guarantee full symmetry.

---

### 4th Central Moment: Kurtosis

The fourth central moment $\mu_4' = E[(X - \mu)^4]$ measures the **tail heaviness** and **peakedness** of a distribution relative to its variance.

As with skewness, the raw fourth central moment is scale-dependent, so kurtosis is defined in standardized form as:

$$
\gamma_2 = \frac{\mu_4'}{\sigma^4} = \frac{E[(X - \mu)^4]}{\sigma^4}
$$

Kurtosis is often compared to that of the Normal distribution, which has:
$$
\gamma_2 = 3
$$

This leads to the definition of **excess kurtosis**:

$$
\text{Excess Kurtosis} = \gamma_2 - 3
$$

Interpretation:
* Excess kurtosis $> 0$: **Leptokurtic**
  * Heavier tails, more extreme outliers than Normal
* Excess kurtosis $= 0$: **Mesokurtic**
  * Same tail behavior as Normal
* Excess kurtosis $< 0$: **Platykurtic**
  * Lighter tails, fewer extreme values

---

> [!example]-
> Let $X\sim \mathrm{Uniform}(a, b)$ ([[Continuous Uniform]] distribution)
> 
> The pdf $f(x)=\frac{1}{b-a}$, $a\leq x \leq b$
> 
> **Expectation value**: 
> $$
> \begin{split}
> \mu = E[X] = \int_a^bx(\frac{1}{b-a})dx = \frac{1}{b-a}\left[\frac{x^2}{2}\right]_a^b = \frac{a^2-b^2}{2(a-b)} = \frac{(a+b)(a-b)}{2(a-b)} = \frac{a+b}{2}
> \end{split}
> $$
> **Variance**:
> $$E[X^2] = \int_a^bx^2(\frac{1}{b-a})dx = \frac{1}{b-a}\left[\frac{x^3}{3}\right]_a^b = \frac{a^3-b^3}{3(a-b)} = \frac{(a-b)(a^2+ab+b^2)}{3(a-b)} = \frac{a^2+ab+b^2}{3}$$
> $$\sigma^2 = E[X^2] - E[X]^2 = \frac{a^2+ab+b^2}{3} - \left(\frac{a+b}{2}\right)^2 = \dots = \frac{(a-b)^2}{12}$$
> 
> **Skewness**:
> $$
> \gamma_1 = \frac{E[(X-\mu)^3]}{\sigma^3}
> $$
> 
> $\mu=\frac{a+b}{2}$ is half way between $a$ and $b$ meaning the distribution is symmetric about the mean so all odd central moments are zero so 
> 
> $$
> E[(X-\mu)^3] = 0
> $$
> 
> Therefore,
> $$
> \gamma_1 = 0
> $$
> 
> 
> **Kurtosis**:
> 
> The (standardized) kurtosis is defined as
> $$
> \gamma_2 = \frac{E[(X-\mu)^4]}{\sigma^4}
> $$
> 
> $$
> E[(X-\mu)^4]
> = \int_a^b (x-\mu)^4 \frac{1}{b-a}\,dx
> = \dots
> = \frac{(b-a)^4}{80}
> $$
> 
> Using the variance $\sigma^2 = \frac{(b-a)^2}{12}$,
> $$
> \sigma^4 = \left(\frac{(b-a)^2}{12}\right)^2 = \frac{(b-a)^4}{144}
> $$
> 
> Thus,
> $$
> \gamma_2
> = \frac{(b-a)^4/80}{(b-a)^4/144}
> = \frac{144}{80}
> = \frac{9}{5}
> $$
> 
> The **excess kurtosis** is:
> $$
> \gamma_2 - 3 = \frac{9}{5} - 3 = -\frac{6}{5}
> $$
> 