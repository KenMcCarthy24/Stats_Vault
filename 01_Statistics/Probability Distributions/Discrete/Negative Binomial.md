![[Negative_Binomial_pmf.svg]]
## Overview
* **Type:** Discrete
* **Key Intuition:** Number of failures observed before achieving $r$ successes in independent [[Bernoulli]] trials with success probability $p$
* **Example Use Cases:**
    * Number of Tails observed before the $r$-th Head
    * Number of failed sales calls before closing $r$ deals


---

## Mathematical Definition

### Notation
$X \sim NB(r, p)$

### Probability Mass (PMF)
> $$f(k;r, p) = \binom{k+r-1}{r-1} p^r (1-p)^k$$

### Cumulative Distribution Function (CDF)
> $$F(k;r,p) = P(X \le k) = \sum_{j=0}^{k} \binom{j+r-1}{r-1} p^r (1-p)^j$$

---

## Parameters & Support
* **Parameters:**
    * $r$: Number of successes (positive integer)
    * $p$: Probability of success on each trial

* **Support:** $k \in \{0, 1, 2, \dots\}$

---

## Key Properties

| Property                | Formula                                                  |
| :---------------------- | :------------------------------------------------------- |
| **Mean ($E[X]$)**       | $\displaystyle\frac{r(1-p)}{p}$                          |
| **Median**              | No closed form                                           |
| **Mode**                | $\displaystyle\left\lfloor \frac{(r-1)(1-p)}{p} \right\rfloor$ |
| **Variance ($Var(X)$)** | $\displaystyle\frac{r(1-p)}{p^2}$                        |
| **Skewness**            | $\displaystyle\frac{2-p}{\sqrt{r(1-p)}}$                 |
| **Kurtosis**            | $\displaystyle 6 + \frac{p^2}{r(1-p)}$                   |
| **Fisher Information**  | $\displaystyle\frac{r}{p^2(1-p)}$                        |
| **Jeffreys Prior**      | $\displaystyle\frac{1}{p\sqrt{1-p}}$                     |
| **MLE**                 | $\displaystyle\hat{p} = \frac{r}{r+\bar{X}}$             |

---

## Relationships to Other Distributions
* **[[Geometric]]:** Special case when $r = 1$ (failures before first success)

---

## Notes & Implementation (Python/R)
* **Scipy:** `scipy.stats.nbinom` (uses this parameterization)
* **R:** `dnbinom`, `pnbinom`, `qnbinom`, `rnbinom`
