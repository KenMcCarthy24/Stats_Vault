![[Poisson_pmf.svg]]
## Overview
* **Type:** Discrete
* **Key Intuition:** Number of events occurring in a fixed interval of time or space when events occur independently at a constant average rate
* **Example Use Cases:**
    * Number of emails received in an hour
    * Number of mutations along a strand of DNA
    * Number of arrivals to a queue in a fixed time window

---

## Mathematical Definition

### Notation
$X \sim Poisson(\lambda)$

### Probability Mass (PMF)
> $$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$$

### Cumulative Distribution Function (CDF)
> $$F(k) = P(X \le k) = \sum_{j=0}^{k} \frac{\lambda^j e^{-\lambda}}{j!}$$

---

## Parameters & Support
* **Parameters:**
    * $\lambda > 0$: Event rate (mean number of events per interval)

* **Support:** $k \in \{0, 1, 2, \dots\}$

---

## Key Properties

| Property                | Formula                                                                                   |
| :---------------------- | :---------------------------------------------------------------------------------------- |
| **Mean ($E[X]$)**       | $\lambda$                                                                                 |
| **Median**              | Approximately $\displaystyle \lfloor \lambda + \frac{1}{3} - \frac{5}{50\lambda} \rfloor$ |
| **Mode**                | $\lfloor \lambda \rfloor$                                                                 |
| **Variance ($Var(X)$)** | $\lambda$                                                                                 |
| **Skewness**            | $\displaystyle \frac{1}{\sqrt{\lambda}}$                                                  |
| **Kurtosis**            | $\displaystyle \frac{1}{\lambda}$                                                         |
| **Fisher Information**  | $\displaystyle \frac{1}{\lambda}$                                                         |
| **Jeffreys Prior**      | $\displaystyle \lambda^{-1/2}$                                                            |
| **MLE**                 | $\displaystyle \hat{\lambda} = \bar{X}$                                                   |

---

## Relationships to Other Distributions
* **[[Binomial]]:** Limit as $n \to \infty$, $p \to 0$ with $np = \lambda$
* **[[Negative Binomial]]:** Generalization allowing overdispersion
* **[[Gamma]]:** Bayesian Conjugate Prior
	* Also the wait time to the $n$-th event has distribution $\Gamma(n, \lambda)$

---

## Notes & Implementation (Python/R)
* **Scipy:** `scipy.stats.poisson`
* **R:** `dpois`, `ppois`, `qpois`, `rpois`
