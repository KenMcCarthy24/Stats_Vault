![[Binomial_pmf 1.svg]]
## Overview
* **Type:** Discrete
* **Key Intuition:** Number of successes observed in a fixed number of independent [[Bernoulli]] trials with success probability $p$
* **Example Use Cases:**
    * Number of Heads in $n$ coin flips
    * Number of defective items in a batch of size $n$
    * Number of users who click an ad out of $n$ impressions

---

## Mathematical Definition

### Notation
$X \sim Bin(n, p)$

### Probability Mass (PMF)
> $$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$$

### Cumulative Distribution Function (CDF)
> $$F(k) = P(X \le k) = \sum_{j=0}^{k} \binom{n}{j} p^j (1-p)^{n-j}$$

---

## Parameters & Support
* **Parameters:**
    * $n$: Number of trials ($n \in \mathbb{N}$)
    * $p$: Probability of success on each trial, $0 \le p \le 1$

* **Support:** $k \in \{0, 1, 2, \dots, n\}$

---

## Key Properties

| Property                | Formula                                      |
| :---------------------- | :------------------------------------------- |
| **Mean ($E[X]$)**       | $\displaystyle np$                           |
| **Median**              | $\displaystyle \lfloor (n+1)p \rfloor$ or $\lceil (n+1)p \rceil - 1$ |
| **Mode**                | $\displaystyle \lfloor (n+1)p \rfloor$      |
| **Variance ($Var(X)$)** | $\displaystyle np(1-p)$                      |
| **Skewness**            | $\displaystyle \frac{1-2p}{\sqrt{np(1-p)}}$ |
| **Kurtosis**            | $\displaystyle 3 + \frac{1-6p(1-p)}{np(1-p)}$ |
| **Fisher Information**  | $\displaystyle \frac{n}{p(1-p)}$             |
| **Jeffreys Prior**      | $\displaystyle \frac{1}{\sqrt{p(1-p)}}$     |
| **MLE**                 | $\displaystyle \hat{p} = \frac{\bar{X}}{n}$ |

---

## Relationships to Other Distributions
* **[[Bernoulli]]:** Special case when $n = 1$
* **[[Poisson]]:** Limit as $n \to \infty$, $p \to 0$ with $np = \lambda$.
	* $Poisson(\lambda=np)$ is a good approximation of $Bin(n, p)$ if:
		* $n \geq 20$ and $p \leq 0.05$
		* $n \geq 50$ and $p \leq 0.1$
		* $n \geq 100$ and $np \leq 10$
* **[[Normal]]:** For high $n$ $Bin(n, p)$ can be approximated as $N(np, np(1-p))$
	* Both expected numbers of successes and failures should be at least 5
		* $np \geq 5$ and $n(p-1) \geq 5$
		* Even better if they are both $\geq 10$
* **[[Beta]]:** Bayesian conjugate prior for $p$

---

## Notes & Implementation (Python/R)
* **Scipy:** `scipy.stats.binom`
* **R:** `dbinom`, `pbinom`, `qbinom`, `rbinom`
