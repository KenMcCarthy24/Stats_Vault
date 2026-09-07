A random variable $X$ has a discrete [[Probability Distribution]] if $X$ takes values in a countable set (e.g., $\{0,1,2,\dots\}$)

The probability $P(X=k)$ for a particular result $k$ is given by the probability mass function (PMF):

$$f(k) = P(X=k) \text{ for }k\in \mathbb{R}$$
A PMF must satisfy:
* $P(X=k) \geq 0$ for all $k$
* $\sum_k P(X=k) = 1$

The probability $P(X \leq k)$ that $X$ will take a value less than or equal to $k$ is given by the Cumulative Distribution Function (CDF):

$$P(X \leq k) = \sum_{x_i \leq k}P(X = x_i)$$

The **mean** or **expectation value** of a discrete probability distribution is given by:
 $$\mu = E[X] = \sum_k kP(X=k)$$
The **variance** of a discrete probability distribution is given by:
$$
\begin{split}
\sigma^2 = Var(X) &= E[(X-E(X))^2] \\
&= E[X^2] - E[X]^2
\end{split}
$$

The **median** of a discrete probability distribution is the smallest value where the cumulative probability reaches at least 50%, it is given by:
$$
m = \min\left\{x_k : \sum_{i=1}^k P(X = x_i) \ge \tfrac12 \right\}
$$

Information for calculating other useful stats: [[Expectation and Moments]], [[Quantiles]]

Examples: [[Bernoulli]], [[Binomial]], [[Categorical]], [[Discrete Uniform]], [[Geometric]], [[Hypergeometric]], [[Negative Binomial]], [[Poisson]]
