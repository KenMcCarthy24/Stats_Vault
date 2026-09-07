A random variable $X$ has a continuous [[Probability Distribution]] if $X$ takes values in an uncountable set (e.g., intervals on the real line $\mathbb{R}$).

The probability that $X$ falls within a specific interval $[a, b]$ is given by the area under the Probability Density Function (PDF), $f(x)$:

$$P(a \leq X \leq b) = \int_a^b f(x) dx$$

Note that for continuous variables, the probability of a single exact value is zero ($P(X=c) = 0$).

The PDF must satisfy:
* $f(x) \geq 0$ for all $x$
* $\int_{-\infty}^{\infty} f(x) dx = 1$

The probability $P(X \leq x)$ that $X$ will take a value less than or equal to $x$ is given by the Cumulative Distribution Function (CDF):

$$F(x) = P(X \leq x) = \int_{-\infty}^{x} f(t) dt$$

The **mean** or **expectation value** of a continuous probability distribution is given by:
$$\mu = E[X] = \int_{-\infty}^{\infty} x f(x) dx$$

The **variance** of a continuous probability distribution is given by:
$$
\begin{split}
\sigma^2 = Var(X) &= E[(X-E[X])^2] \\
&= \int_{-\infty}^{\infty} (x - \mu)^2 f(x) dx \\
&= E[X^2] - E[X]^2
\end{split}
$$

The **median** of a continuous probability distribution is the value $m$ that divides the area under the PDF into two equal halves. It is found by solving:

$$
\int_{-\infty}^m f(x) dx = \frac{1}{2} \quad \text{or} \quad F(m) = 0.5
$$

Information for calculating other useful stats: [[Expectation and Moments]], [[Quantiles]]

Examples: [[Beta]], [[Chi-Squared]], [[Continuous Uniform]], [[Exponential]], [[F-distribution]], [[Gamma]], [[Lognormal]], [[Normal]], [[Student-t]], [[Weibull]]